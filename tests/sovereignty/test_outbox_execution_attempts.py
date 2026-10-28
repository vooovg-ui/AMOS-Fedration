"""سقفُ المحاولةِ الواحدةِ لأثرِ التشغيلِ في الصادر — WI-116

الهدف: إثباتُ الجزأينِ (أ) و(ب) من `docs/audit/EXECUTION_RECOVERY_DESIGN.md` (قرارُ المالكِ
    D24-R2 · الخيارُ 1): السقفُ يُحسَبُ من **توقيعِ الأثر** لا من العامل، ومزوِّدُ التشغيلِ
    لا يُقِرُّ بالتفرّد، والغامضُ من التشغيلِ لا يُعادُ آليًّا مهما قالَ سجلُّه
النطاق: `core/sovereignty/outbox.py`
المالك: W-720 · WI-116
تاريخ الإنشاء: 2026-10-28
"""

from __future__ import annotations

from dataclasses import replace
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING

import pytest

from core.sovereignty.outbox import (
    DEFAULT_LEASE_SECONDS,
    EXECUTION_MAX_DELIVERY_ATTEMPTS,
    DeliveryOutcome,
    DeliveryReceipt,
    DeliveryStatus,
    EffectPayload,
    OutboxClaimError,
    OutboxError,
    OutboxLedger,
    OutboxRecord,
    compute_effect_id,
    is_execution_signature,
    max_attempts_for,
)

if TYPE_CHECKING:
    from pathlib import Path

EXECUTION_SIG = "EXECUTION:executive.task:t-wi116"
EXTERNAL_SIG = "EXTERNAL:notify.email:t-wi116"


def _ledger(tmp_path: Path) -> OutboxLedger:
    return OutboxLedger(tmp_path / "outbox.json")


def _enqueue(ledger: OutboxLedger, signature: str, *, supports: bool = False) -> str:
    payload = EffectPayload(data={"task_id": "t-wi116"})
    op_key = f"wi116:{signature}"
    effect_id = compute_effect_id(
        operation_key=op_key,
        effect_signature=signature,
        provider="executive.run",
        payload_digest=payload.digest,
    )
    ledger.enqueue(
        effect_id=effect_id,
        operation_key=op_key,
        effect_signature=signature,
        provider="executive.run",
        provider_supports_idempotency=supports,
        payload=payload,
        permit_id="wi116-permit",
        authorization_anchor="wi116-anchor",
    )
    return effect_id


def _fail_retryable(
    ledger: OutboxLedger, effect_id: str, max_attempts: int
) -> OutboxRecord:
    ledger.claim(effect_id=effect_id, worker_id="w")
    ledger.begin_attempt(effect_id=effect_id, worker_id="w")
    return ledger.record_result(
        effect_id=effect_id,
        worker_id="w",
        receipt=DeliveryReceipt(outcome=DeliveryOutcome.RETRYABLE_FAILURE),
        max_attempts=max_attempts,
    )


def test_signature_classification_and_cap() -> None:
    assert EXECUTION_MAX_DELIVERY_ATTEMPTS == 1
    assert is_execution_signature(EXECUTION_SIG)
    assert not is_execution_signature(EXTERNAL_SIG)
    assert max_attempts_for(EXECUTION_SIG, 3) == 1
    assert max_attempts_for(EXECUTION_SIG, 1) == 1
    assert max_attempts_for(EXTERNAL_SIG, 3) == 3


def test_execution_dead_on_first_retryable_failure_even_if_worker_allows_three(
    tmp_path: Path,
) -> None:
    """الجزءُ (أ): عاملٌ بـ`max_attempts=3` لا يُعيدُ أثرَ تشغيل — يموتُ من الأولى."""
    ledger = _ledger(tmp_path)
    effect_id = _enqueue(ledger, EXECUTION_SIG)
    record = _fail_retryable(ledger, effect_id, max_attempts=3)
    assert record.status is DeliveryStatus.DEAD
    assert not record.is_claimable()


def test_non_execution_behaviour_unchanged(tmp_path: Path) -> None:
    """خارجَ النطاقِ نصًّا: الأثرُ الخارجيُّ يبقى قابلًا للإعادةِ بسقفِ العامل."""
    ledger = _ledger(tmp_path)
    effect_id = _enqueue(ledger, EXTERNAL_SIG, supports=True)
    record = _fail_retryable(ledger, effect_id, max_attempts=3)
    assert record.status is DeliveryStatus.FAILED_RETRYABLE
    assert record.is_claimable()


def test_execution_enqueue_refuses_declared_idempotency(tmp_path: Path) -> None:
    """الجزءُ (ب): الإقرارُ بالتفرّدِ لتشغيلٍ ليس أحاديًّا مرفوضٌ عندَ الإدراج."""
    ledger = _ledger(tmp_path)
    with pytest.raises(OutboxError):
        _enqueue(ledger, EXECUTION_SIG, supports=True)
    assert ledger.all_records() == []


def test_legacy_indeterminate_execution_record_needs_human(tmp_path: Path) -> None:
    """سجلٌّ قديمٌ كتبَ أنَّ مُزوّدَ التشغيلِ متفرِّد: غموضُه بشريٌّ ولا يُحجَز."""
    ledger = _ledger(tmp_path)
    effect_id = _enqueue(ledger, EXECUTION_SIG)
    data = ledger.require(effect_id).as_dict()
    data.update(
        provider_supports_idempotency=True,
        status=DeliveryStatus.INDETERMINATE.value,
        attempt_count=1,
    )
    record = OutboxRecord.from_dict(data)
    assert record.is_execution
    assert record.requires_human_resolution
    assert not record.is_claimable()

    data["attempt_count"] = 0
    fresh = OutboxRecord.from_dict(data)
    assert fresh.requires_human_resolution
    assert not fresh.is_claimable()


def test_expired_claim_of_started_execution_is_not_reclaimed(tmp_path: Path) -> None:
    """حجزٌ منقضٍ بعدَ محاولةٍ بدأت: لا حجزَ جديد — `reclaim_expired` تُعلِنُه غامضًا."""
    ledger = _ledger(tmp_path)
    effect_id = _enqueue(ledger, EXECUTION_SIG)
    ledger.claim(effect_id=effect_id, worker_id="w")
    started = ledger.begin_attempt(effect_id=effect_id, worker_id="w")
    assert started.attempt_count == 1

    later = datetime.now(UTC) + timedelta(seconds=DEFAULT_LEASE_SECONDS + 5)
    with pytest.raises(OutboxClaimError):
        ledger.claim(effect_id=effect_id, worker_id="w2", now=later)

    reclaimed = ledger.reclaim_expired(now=later)
    assert [r.effect_id for r in reclaimed] == [effect_id]
    record = ledger.require(effect_id)
    assert record.status is DeliveryStatus.INDETERMINATE
    assert record.requires_human_resolution
    assert not record.is_claimable(now=later)


def test_pending_execution_is_claimable_once(tmp_path: Path) -> None:
    """المحاولةُ الأولى مسموحة: السقفُ واحدٌ لا صفر."""
    ledger = _ledger(tmp_path)
    effect_id = _enqueue(ledger, EXECUTION_SIG)
    record = ledger.require(effect_id)
    assert record.is_claimable()
    assert not replace(record, attempt_count=1).is_claimable()
