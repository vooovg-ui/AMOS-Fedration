"""الهدف: مصدرُ مستوى زرِّ التوقّفِ للبوّابةِ السياديّةِ من الجدولِ الدائم — WI-085 · المرحلةُ الأولى (مراقبةٌ بلا منع).

النطاق: federal/executive/services — قراءةُ `system_state` بلا إنشاءِ صفٍّ وترجمتُها إلى المستوى الدستوريِّ 0..5
        بغ1، ومُصرِّفُ الملاحظاتِ إلى سجلِّ التشغيل. لا كتابةَ ولا منعَ ولا مساسَ بـ`persistent.py`.
المالك: federal/executive/services — البندُ WI-085 (قيدُ W-752 · التصميمُ § 10.4–10.5)
تاريخ الإنشاء: 2026-10-30
تاريخ آخر تعديل: 2026-10-30

لماذا لا يُقرأُ بـ`PersistentSystemStateStore.get()`: مقيسٌ في W-751 أنَّه يُنشئُ صفَّ `normal` عندَ الغياب — أي يفشلُ
مفتوحًا، وقرارُ المالكِ غ1 (الغيابُ يُقرأُ 5). فالقراءةُ هنا استعلامٌ مباشرٌ لا يُنشئُ شيئًا.

م2 في هذه المرحلةِ فجوةٌ معلَنة (§ 10.4): الكاتبُ اليومَ يقبلُ الأسماءَ الأربعةَ وحدَها، فيُقرأُ الشكلان: الرقمُ الدستوريُّ
(`constitutional`) والاسمُ القديمُ مترجَمًا بأدنى مستوًى يوافقُ اشتقاقَ م2 (`legacy_name`) — والشكلُ مكتوبٌ في كلِّ ملاحظة.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from amos_federation.common.database import SystemStateModel, get_session_factory

#: اسمُ السجلِّ الذي يُراجَعُ قبلَ تفعيلِ المنع (§ 10.5).
OBSERVATION_LOGGER = "amos.kill_switch.observe"

#: الاسمُ التشغيليُّ ⇐ أدنى مستوًى دستوريٍّ يوافقُ اشتقاقَ م2 (0 normal · 1–2 alert · 3 degraded · 4–5 halt).
LEGACY_NAME_LEVEL: dict[str, int] = {"normal": 0, "alert": 1, "degraded": 3, "halt": 4}

_STATE_ROW_ID = "system"
_FAIL_CLOSED = 5

_log = logging.getLogger(OBSERVATION_LOGGER)


def level_from_stored(value: Any) -> tuple[int, str]:
    """ترجمةُ القيمةِ المخزَّنةِ إلى (المستوى، الشكل) بغ1 — المجهولُ 5 ولا يُخمَّن."""
    if isinstance(value, str):
        text = value.strip()
        if text.isdigit() and 0 <= int(text) <= _FAIL_CLOSED:
            return int(text), "constitutional"
        if text in LEGACY_NAME_LEVEL:
            return LEGACY_NAME_LEVEL[text], "legacy_name"
    return _FAIL_CLOSED, "unknown"


class PersistentKillSwitchLevelSource:
    """يقرأُ صفَّ `system_state` في كلِّ نداءٍ بلا تخزينٍ مؤقّت (§ 3) وبلا إنشاءٍ عندَ الغياب (غ1)."""

    def read(self) -> Any:
        from core.sovereignty.kill_switch_source import LevelReading

        session = get_session_factory()()
        try:
            row = (
                session.query(SystemStateModel).filter(SystemStateModel.id == _STATE_ROW_ID).first()
            )
            if row is None:
                return LevelReading(_FAIL_CLOSED, "absent")
            level, form = level_from_stored(row.level)
            return LevelReading(level, form)
        finally:
            session.close()


def log_observation(observation: Any) -> None:
    """المُصرِّفُ: سطرُ JSON واحدٌ بمستوى WARNING في `amos.kill_switch.observe` — هو السجلُّ الذي يُراجَع."""
    _log.warning(
        "kill_switch_would_block %s", json.dumps(observation.as_dict(), ensure_ascii=False)
    )
