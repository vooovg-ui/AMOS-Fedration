"""
AMOS-Federation — إعداداتُ جلسةِ PostgreSQL في الاختبارات تُطبَّقُ بعدَ الاتصالِ وتُتحقَّقُ (WI-066)
الهدف: أن يعزلَ كلُّ اختبارٍ حيٍّ نفسَه في مخطّطِه وبمنطقتِه الزمنيّةِ **فعلًا** خلفَ أيِّ مُجمِّعِ
       اتصالاتٍ (pooler)، وأن يسقطَ بصوتٍ عالٍ إن لم يُطبَّقِ الإعدادُ — لا أن يكتبَ صامتًا في
       مخطّطٍ مشترك.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-12 (WI-066 · W-290)
تاريخ آخر تعديل: 2026-10-12 (WI-066 · W-290)

## لماذا لا يكفي `connect_args={"options": "-csearch_path=…"}`

خيارُ `options` في libpq يُرسَلُ في رسالةِ بدءِ الاتصال. PostgreSQL المباشرُ يحترمُه، لكنَّ
مُجمِّعَ Supabase (‏Supavisor · منفذ 5432 بوضعِ الجلسة) **يتجاهلُه بلا خطأ**: قِيسَ في
2026-10-12 أنَّ `SHOW search_path` بعدَ الاتصالِ بـ`-csearch_path=amos_test` يُرجِعُ
`"$user", public, extensions`. فكانت اختباراتُ الهجراتِ تبني «مخطّطَها المعزول» في المخطّطِ
الافتراضيِّ نفسِه وتتصادم (‏`agents_pkey` مكرَّر)، واختباراتُ المنطقةِ الزمنيّةِ في WI-066 كانت
ستختبرُ منطقةً غيرَ المقصودة. وفي CI لا يظهرُ ذلك لأنَّ خدمةَ PostgreSQL هناك مباشرة.

الحلّ: `set_config(name, value, false)` على كلِّ اتصالٍ جديدٍ عبرَ حدثِ `connect`، ثمَّ قراءةُ
`current_setting(name)` ومقارنتُها؛ والاختلافُ `SessionSettingNotAppliedError` لا تجاوز.
"""

from __future__ import annotations

from typing import Any


class SessionSettingNotAppliedError(RuntimeError):
    """إعدادُ جلسةٍ طُلِبَ ولم يُطبَّقْ — الاختبارُ لا يعملُ في المكانِ الذي يظنُّه."""


def session_engine(
    url: str,
    *,
    search_path: str | None = None,
    timezone: str | None = None,
    **engine_kwargs: Any,
):
    """محرّكُ SQLAlchemy يُطبِّقُ `search_path` و`TimeZone` بعدَ كلِّ اتصالٍ ويتحقّقُ منهما.

    يعملُ مع PostgreSQL المباشرِ ومع مُجمِّعٍ بوضعِ الجلسة. لا يصلحُ لوضعِ المعاملات
    (‏منفذ 6543)، لأنَّ الإعدادَ هناك لا يبقى بينَ المعاملات — والتحقّقُ يكشفُ ذلك عندَ أوّلِ اتصال.
    """
    from sqlalchemy import create_engine, event

    if "connect_args" in engine_kwargs and "options" in engine_kwargs["connect_args"]:
        raise ValueError("session_engine يرفضُ connect_args.options — المُجمِّعُ يتجاهلُه بصمت")

    wanted: dict[str, str] = {}
    if search_path is not None:
        wanted["search_path"] = search_path
    if timezone is not None:
        wanted["TimeZone"] = timezone

    engine = create_engine(url, **engine_kwargs)
    if not wanted:
        return engine

    @event.listens_for(engine, "connect")
    def _apply(dbapi_conn: Any, _record: Any) -> None:
        cur = dbapi_conn.cursor()
        try:
            for name, value in wanted.items():
                cur.execute("SELECT set_config(%s, %s, false)", (name, value))
            for name, value in wanted.items():
                cur.execute("SELECT current_setting(%s)", (name,))
                got = cur.fetchone()[0]
                if got != value:
                    raise SessionSettingNotAppliedError(
                        f"{name}: طُلِبَ «{value}» والجلسةُ تقولُ «{got}»"
                    )
        finally:
            cur.close()
        # set_config داخلَ معاملةٍ ضمنيّةٍ يُلغى إن أُلغيَت؛ فتُثبَّتُ الآنَ قبلَ أيِّ استعمال.
        if not getattr(dbapi_conn, "autocommit", False):
            dbapi_conn.commit()

    return engine
