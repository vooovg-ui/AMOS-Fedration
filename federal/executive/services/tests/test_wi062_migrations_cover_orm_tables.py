"""
AMOS-Federation — كلُّ جدولٍ يُعلِنُه النموذجُ تُنشئُه هجرة (WI-062 · DISC-088)
الهدف: أن تحويَ قاعدةٌ بُنِيَت بالهجراتِ وحدَها كلَّ جدولٍ في `Base.metadata`، وأن
       يكونَ الجدولُ الذي تُنشئُه الهجرةُ هو الجدولَ الذي يُنشئُه المحرّكُ عمودًا عمودًا.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-10 (WI-062)
تاريخ آخر تعديل: 2026-10-10 (WI-062)

## ما الذي قِيسَ قبلَ هذا الملفّ

على PostgreSQL 18.6: الهجراتُ 001–016 على قاعدةٍ فارغةٍ ⇒ 62 جدولًا؛ و`init_db()` بعدَ
استيرادِ الحزمةِ كلِّها ⇒ 59. وثلاثةٌ في النموذجِ بلا هجرة: `system_state` (مستوى مفتاحِ
الإيقاف) و`promotions` (موافقاتُ الترقية) و`training_models`. فمن رحَّلَ بالـSQL وحدَه
لم يجدْها حتى يُقلِعَ تطبيقٌ ينادي `init_db()`.

## الحارسان

1. **ساكنٌ** (يعملُ في كلِّ تشغيلٍ وعلى SQLite): كلُّ اسمِ جدولٍ في `Base.metadata` بعدَ
   استيرادِ وحداتِ الحزمةِ كلِّها يظهرُ في `CREATE TABLE` داخلَ ملفٍّ من `migrations/`.
   فجدولٌ نموذجيٌّ جديدٌ بلا هجرةٍ يُسقِطُه.
2. **حيٌّ** (PostgreSQL المُفعَّلُ صراحةً وحدَه): تُطبَّقُ الهجراتُ كلُّها بالترتيبِ في
   مخطّطٍ مؤقّتٍ، ويَبني المحرّكُ الجداولَ الثلاثةَ في مخطّطٍ ثانٍ، فتُقارَنُ أعمدتُها
   نوعًا وقبولًا للفراغ؛ وتُعادُ 017 مرّةً ثانيةً لإثباتِ أنّها إضافةٌ لا تتكسّرُ بالتكرار.
   والمخطّطانِ يُنشآنِ ويُسقَطانِ في الاختبارِ نفسِه — لا يُمَسُّ مخطّطٌ قائم.

## وما لا يُدَّعى

لا يُدَّعى تطابقُ الهجراتِ والنموذجِ في **سائرِ** الجداول: قِيسَ افتراقٌ قائمٌ في أنواعِ
أعمدةٍ (`jsonb`/`json` · `timestamptz`/`timestamp`) وأعمدةٍ في الهجرةِ وحدَها، وهو مُقيَّدٌ
في `DISC-088` بندًا لاحقًا لا في هذا الملفّ.
"""

from __future__ import annotations

import importlib
import os
import re
import uuid
from pathlib import Path

import pytest

import amos_federation
from amos_federation.common.database import Base

MIGRATIONS_DIR = Path(__file__).resolve().parents[1] / "migrations"
NEW_MIGRATION = MIGRATIONS_DIR / "017_orm_tables_without_migration.sql"
#: الجداولُ التي أتت بها 017 — تُقارَنُ حيًّا مع ما يُنشئُه المحرّك.
TABLES_ADDED_BY_017 = ("system_state", "promotions", "training_models")


def _import_whole_package() -> None:
    """يستوردُ كلَّ وحدةٍ في الحزمةِ حتى يحويَ `Base.metadata` كلَّ جدولٍ مُعلَن.

    قِيسَ في `WI-061` أنَّ كلَّ وحدةٍ (141) تُستورَدُ منفردةً بلا خطأ؛ فخطأُ استيرادٍ
    هنا عطبٌ حقيقيٌّ يُرفَعُ لا يُبتلَع.
    """
    # مشيٌ على الملفّاتِ لا `pkgutil.walk_packages`: الأخيرُ يتخطّى الحزمَ بلا `__init__.py`
    # (‏قِيسَ: `services/training/` منها، ففاتَه `training_models` بصمت).
    root = Path(amos_federation.__file__).resolve().parent
    for path in sorted(root.rglob("*.py")):
        parts = path.relative_to(root.parent).with_suffix("").parts
        if parts[-1] == "__init__":
            parts = parts[:-1]
        importlib.import_module(".".join(parts))


def _migration_sql() -> str:
    files = sorted(MIGRATIONS_DIR.glob("[0-9][0-9][0-9]_*.sql"))
    assert files, f"لا هجرةَ في {MIGRATIONS_DIR}"
    return "\n".join(f.read_text(encoding="utf-8") for f in files)


def _created_tables(sql: str) -> set[str]:
    pattern = re.compile(
        r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?\"?([A-Za-z_][A-Za-z0-9_]*)\"?",
        re.IGNORECASE,
    )
    return {m.group(1).lower() for m in pattern.finditer(sql)}


def test_every_orm_table_is_created_by_a_migration() -> None:
    _import_whole_package()
    declared = {name.lower() for name in Base.metadata.tables}
    created = _created_tables(_migration_sql())
    missing = sorted(declared - created)
    assert not missing, (
        "جداولُ في Base.metadata لا تُنشئُها هجرةٌ في migrations/ — قاعدةٌ مُرحَّلةٌ بالـSQL "
        f"لن تجدَها: {missing}"
    )


def test_migration_017_is_additive_only() -> None:
    """017 تُنشئُ إن لم يوجدْ ولا تُسقِطُ ولا تُعدِّلُ ولا تكتبُ صفًّا."""
    sql = NEW_MIGRATION.read_text(encoding="utf-8")
    code = "\n".join(line for line in sql.splitlines() if not line.lstrip().startswith("--"))
    for forbidden in ("DROP ", "ALTER ", "DELETE ", "TRUNCATE ", "UPDATE ", "INSERT "):
        assert forbidden not in code.upper(), f"017 تحوي {forbidden.strip()} خارجَ التعليق"
    creates = re.findall(r"CREATE\s+TABLE\s+(IF\s+NOT\s+EXISTS\s+)?(\w+)", code, re.IGNORECASE)
    assert sorted(name for _, name in creates) == sorted(TABLES_ADDED_BY_017)
    assert all(guard for guard, _ in creates), "كلُّ CREATE TABLE في 017 يلزمُه IF NOT EXISTS"


def _pg_enabled() -> bool:
    return os.environ.get("AMOS_RUN_POSTGRES_TESTS") == "1" and os.environ.get(
        "AMOS_TEST_DATABASE_URL", ""
    ).startswith("postgresql")


@pytest.mark.skipif(
    not _pg_enabled(),
    reason="Set AMOS_RUN_POSTGRES_TESTS=1 and AMOS_TEST_DATABASE_URL=postgresql://... to run",
)
def test_migrations_and_engine_build_identical_tables_on_postgres() -> None:
    from sqlalchemy import create_engine, text

    from amos_federation.common.database import with_declared_driver

    _import_whole_package()
    url = with_declared_driver(os.environ["AMOS_TEST_DATABASE_URL"])
    suffix = uuid.uuid4().hex[:10]
    mig_schema, orm_schema = f"wi062_mig_{suffix}", f"wi062_orm_{suffix}"
    admin = create_engine(url, isolation_level="AUTOCOMMIT")
    try:
        with admin.connect() as conn:
            conn.execute(text(f'CREATE SCHEMA "{mig_schema}"'))
            conn.execute(text(f'CREATE SCHEMA "{orm_schema}"'))

        # الهجراتُ كلُّها بالترتيبِ في مخطّطِها — وكلُّ ملفٍّ يحملُ BEGIN/COMMIT بنفسِه.
        mig_engine = create_engine(
            url,
            isolation_level="AUTOCOMMIT",
            connect_args={"options": f"-csearch_path={mig_schema}"},
        )
        files = sorted(MIGRATIONS_DIR.glob("[0-9][0-9][0-9]_*.sql"))
        raw = mig_engine.raw_connection()
        try:
            cur = raw.cursor()
            for f in files:
                cur.execute(f.read_text(encoding="utf-8"))
            # 017 مرّةً ثانيةً: إضافةٌ محضةٌ لا تتكسّرُ على قاعدةٍ فيها الجداول.
            cur.execute(NEW_MIGRATION.read_text(encoding="utf-8"))
            cur.close()
        finally:
            raw.close()
        mig_engine.dispose()

        orm_engine = create_engine(url, connect_args={"options": f"-csearch_path={orm_schema}"})
        tables = [Base.metadata.tables[name] for name in TABLES_ADDED_BY_017]
        Base.metadata.create_all(orm_engine, tables=tables)
        orm_engine.dispose()

        query = text(
            "SELECT table_name, column_name, data_type, is_nullable "
            "FROM information_schema.columns WHERE table_schema = :s "
            "AND table_name = ANY(:t) ORDER BY table_name, column_name"
        )
        with admin.connect() as conn:
            got_mig = conn.execute(query, {"s": mig_schema, "t": list(TABLES_ADDED_BY_017)}).all()
            got_orm = conn.execute(query, {"s": orm_schema, "t": list(TABLES_ADDED_BY_017)}).all()
        assert {r[0] for r in got_mig} == set(TABLES_ADDED_BY_017)
        assert got_mig == got_orm
    finally:
        with admin.connect() as conn:
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{mig_schema}" CASCADE'))
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{orm_schema}" CASCADE'))
        admin.dispose()
