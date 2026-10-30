"""
مصدرُ مستوى زرِّ التوقّفِ ومراقبتُه — WI-085 (المرحلةُ الأولى: المراقبةُ بلا منع)
الهدف: أن تقرأَ البوّابةُ مستوى المادةِ الثامنةِ من مصدرٍ مُسجَّلٍ لا من الطالب، وتُسجِّلَ «ما كانَ سيُمنَع» ولا تمنعَه — بقرارِ المالكِ في Q-79 (ب · م2 · غ1 بشرطِ مرحلةِ مراقبة).
النطاق: الواجهةُ (`KillSwitchLevelSource`) وقراءتُها بغ1 وسجلُّ الملاحظةِ وحكمُها من `_r008_2` نفسِها — لا منعَ، ولا فرعَ لتفعيلِ المنعِ، ولا مساسَ بقواعدِ الدستورِ ولا بجدولِ `KILL_SWITCH_BLOCKS`.
المالك: core/sovereignty/ — البندُ WI-085 (قيدُ W-752 · التصميمُ `docs/audit/WI085_KILL_SWITCH_INJECTION_DESIGN.md` § 10)
تاريخ الإنشاء: 2026-10-30
تاريخ آخر تعديل: 2026-10-30

## لماذا وُجِدت هذه الوحدة

قِيسَ في W-726 أنَّ الطلبَ الدستوريَّ يحملُ `kill_switch_level=0` دائمًا في الإنتاج: الزرُّ `halt` والكتابةُ تمرّ.
وقرارُ المالكِ: «يُحقَن المستوى أولًا في وضع «يسجّل ما كان سيمنعه» دون منع، ثم يُفعَّل المنع بعد مراجعة السجل».
فهذه الوحدةُ **لا تمنعُ شيئًا**: تقرأُ المستوى، وتأخذُ الأعلى بينَه وبينَ ما في الطلب، وتسألُ `_r008_2` نفسَها
«أكنتَ ستمنعُ؟» على نسخةٍ من الطلبِ لا تُقيَّمُ ولا تُسجَّلُ في السجلِّ الدستوريّ.

## غيابُ المفتاح (غ1)
لا مصدر · استثناء · قيمةٌ خارجَ 0..5 ⇐ المستوى 5 بشكلٍ معلَّمٍ (`no_source` · `error` · `unknown`). وفي هذه المرحلةِ
يعني ذلك «ملاحظةً» لا منعًا.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from typing import Protocol, runtime_checkable

from core.constitutional_engine.model import ActionRequest, Verdict
from core.constitutional_engine.rules import _r008_2

#: النمطُ الوحيدُ في هذه المرحلة. لا نمطَ «منعٍ» هنا: تفعيلُه دفعةٌ لاحقةٌ بعدَ مراجعةِ السجلِّ بيدِ المالك.
KILL_SWITCH_INJECTION_MODE = "OBSERVE"

#: أقصى المادةِ الثامنة: «طوارئُ قصوى» — وهو ما يُقرأُ عندَ غيابِ المفتاحِ أو عطلِه (غ1).
FAIL_CLOSED_LEVEL = 5

FORM_NO_SOURCE = "no_source"
FORM_ERROR = "error"
FORM_UNKNOWN = "unknown"

#: أعطالُ المصدرِ والمراقبةِ تُسجَّلُ هنا — لا تُبتلَعُ صامتة (عقدُ الارتدادِ الصامت · W-027).
_log = logging.getLogger("core.sovereignty.kill_switch")


@dataclass(frozen=True)
class LevelReading:
    """قراءةٌ واحدةٌ للمستوى الدستوريِّ 0..5 وشكلُها (من أين جاءت)."""

    level: int
    form: str


@runtime_checkable
class KillSwitchLevelSource(Protocol):
    """مصدرُ المستوى: يُسجِّلُه الفدراليُّ عندَ الإقلاع، و`core` لا يستوردُ `federal`."""

    def read(self) -> LevelReading: ...


def resolve_reading(source: KillSwitchLevelSource | None) -> LevelReading:
    """اقرأ المستوى بغ1: الغيابُ والعطلُ والمجهولُ تُقرأُ 5 بشكلٍ معلَّم — لا تُخفى."""
    if source is None:
        return LevelReading(FAIL_CLOSED_LEVEL, FORM_NO_SOURCE)
    try:
        reading = source.read()
    except Exception:  # noqa: BLE001 — عطلُ المصدرِ يُقرأُ 5 (غ1) ويُسجَّلُ: شكلُه error
        _log.exception("مصدرُ مستوى زرِّ التوقّفِ معطوبٌ — يُقرأُ %d (غ1)", FAIL_CLOSED_LEVEL)
        return LevelReading(FAIL_CLOSED_LEVEL, FORM_ERROR)
    level = getattr(reading, "level", None)
    if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= FAIL_CLOSED_LEVEL:
        return LevelReading(FAIL_CLOSED_LEVEL, FORM_UNKNOWN)
    return LevelReading(level, str(getattr(reading, "form", FORM_UNKNOWN)))


@dataclass(frozen=True)
class KillSwitchObservation:
    """«ما كانَ سيُمنَع»: فعلٌ مرَّ لأنَّ المستوى لم يُحقَن، وكانت R-008-2 ستمنعُه بالمستوى المقروء."""

    action: str
    actor: str
    target: str
    path: str
    request_level: int
    source_level: int
    source_form: str
    effective_level: int
    verdict_decision: str
    would_block_reason: str
    observed_at: str
    mode: str = KILL_SWITCH_INJECTION_MODE

    def as_dict(self) -> dict[str, object]:
        return {
            "action": self.action,
            "actor": self.actor,
            "target": self.target,
            "path": self.path,
            "request_level": self.request_level,
            "source_level": self.source_level,
            "source_form": self.source_form,
            "effective_level": self.effective_level,
            "verdict_decision": self.verdict_decision,
            "would_block_reason": self.would_block_reason,
            "observed_at": self.observed_at,
            "mode": self.mode,
        }


ObservationSink = Callable[[KillSwitchObservation], None]


def observe(
    request: ActionRequest,
    verdict: Verdict,
    *,
    path: str,
    source: KillSwitchLevelSource | None,
) -> KillSwitchObservation | None:
    """احكمْ «أكانَ سيُمنَع؟» بلا منع.

    المستوى الفعّالُ هو الأعلى بينَ ما في الطلبِ وما في المصدر — فالطالبُ لا يُخفِّضُه. والحكمُ من `_r008_2`
    نفسِها على نسخةٍ من الطلب: نقيّةٌ لا تكتبُ في السجلِّ الدستوريِّ (مقيسٌ في W-751). وتُعادُ ملاحظةٌ إن كانَ
    الفعلُ سيُمنَعُ بالمستوى الفعّالِ ولم يُمنَعْ بمستوى الطلب؛ وما مُنِعَ فعلًا لا يُلاحَظُ لأنَّه ليسَ «ما كانَ سيُمنَع».
    """
    reading = resolve_reading(source)
    effective = max(request.kill_switch_level, reading.level)
    would = _r008_2(replace(request, kill_switch_level=effective))
    if would is None or _r008_2(request) is not None:
        return None
    return KillSwitchObservation(
        action=request.action,
        actor=request.actor.value,
        target=request.target or "",
        path=path,
        request_level=request.kill_switch_level,
        source_level=reading.level,
        source_form=reading.form,
        effective_level=effective,
        verdict_decision=verdict.decision.value,
        would_block_reason=would,
        observed_at=datetime.now(UTC).isoformat(),
    )
