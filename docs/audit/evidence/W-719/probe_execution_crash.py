"""مسبارُ جدوى WI-116: إسقاطُ العاملِ بينَ dispatch وتثبيتِ الحالة

الهدف: قياسُ ما يحدثُ اليومَ (قبلَ أيِّ شِفرةٍ) حينَ يموتُ العاملُ بعدَ `dispatch` وقبلَ `EXECUTING → COMPLETED`
النطاق: صندوقُ الصادرِ (`core/sovereignty/outbox.py`) والنواةُ التنفيذيّةُ (`engine.py`) — قراءةٌ وتشغيلٌ بلا تعديل
المالك: W-719 · WI-116
تاريخ الإنشاء: 2026-10-28

يُشغَّلُ من `federal/executive/services`:
    python -m pytest -p tests.conftest <هذا الملف> -q -s
السقوطُ حقيقيٌّ: عمليّةٌ فرعيّةٌ تُنهي نفسَها بـ`os._exit(137)` بعدَ عودةِ `dispatch`
(لا استثناءَ يُلتقَطُ)، فلا يكتبُ أيُّ `finally` شيئًا. والمُستعيدُ عمليّةٌ أخرى.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import textwrap
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import pytest

from amos_federation.common.database import init_db
from amos_federation.services.executive_core import (
    ExecutiveCore,
    TaskState,
    register_agent,
    reset_executive_core,
)
from amos_federation.services.executive_core.dispatcher import WILDCARD
from amos_federation.services.executive_core.sovereignty_bridge import locate_repo_root

ROOT = locate_repo_root()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.sovereignty.outbox import (  # noqa: E402
    DeliveryOutcome,
    DeliveryReceipt,
    DeliveryStatus,
    EffectPayload,
    OutboxLedger,
    OutboxWorker,
    compute_effect_id,
)

PROVIDER = "executive.run"
LEASE = 30

CHILD = textwrap.dedent(
    """
    import os, sys
    sys.path.insert(0, {root!r})
    from pathlib import Path
    from amos_federation.services.executive_core import ExecutiveCore
    from core.sovereignty.outbox import DeliveryOutcome, DeliveryReceipt, OutboxLedger, OutboxWorker

    counter = Path({counter!r})
    core = ExecutiveCore()
    real_dispatch = core._runtime.dispatch

    def dispatch_then_die(*args, **kwargs):
        outcome = real_dispatch(*args, **kwargs)
        with counter.open("a", encoding="utf-8") as fh:
            fh.write("dispatch\\n")
        os._exit(137)  # سقوطٌ بينَ dispatch والتثبيت — لا finally ولا تسجيل

    core._runtime.dispatch = dispatch_then_die

    class RunAdapter:
        name = {provider!r}
        supports_idempotency = {supports!r}

        def deliver(self, envelope):
            core.run(envelope.payload["task_id"])
            return DeliveryReceipt(outcome=DeliveryOutcome.SUCCESS)

    worker = OutboxWorker(
        ledger=OutboxLedger(Path({ledger!r})),
        adapters={{{provider!r}: RunAdapter()}},
        worker_id="worker-A",
        lease_seconds={lease},
        max_attempts=1,
    )
    worker.run_once()
    sys.exit(0)  # لا يُبلَغ إن صدقَ السقوط
    """
)


@pytest.fixture(autouse=True)
def _fresh_core() -> None:
    """قاعدةُ الاختبارِ تُنشَأُ طازجةً لكلِّ جلسةٍ (`tests/conftest.py`) — ولا تطهيرَ هنا.

    لا كتابةَ في هذا المصدر (جردُ الكتابةِ يقرأُ المستودعَ كلَّه): كلُّ مهمّةٍ بمعرِّفٍ جديد،
    وتسجيلُ العاملِ نفسِه يُعادُ بلا أثرٍ على القياس.
    """
    init_db()
    reset_executive_core()


#: نداءاتُ dispatch في عمليّةِ المسبارِ نفسِها (الذاكرة) — وما في العمليّةِ الفرعيّةِ يُقرأُ من ملفِّها.
#: (لا كتابةَ ملفٍّ في هذا المصدر: جردُ الكتابةِ يقرأُ المستودعَ كلَّه.)
_IN_PROCESS: list[str] = []


def _counted(counter: Path) -> int:
    child = 0
    if counter.exists():
        child = len(counter.read_text(encoding="utf-8").splitlines())
    return child + _IN_PROCESS.count(str(counter))


def _stage(
    tmp_path: Path, *, supports: bool
) -> tuple[ExecutiveCore, str, OutboxLedger, Path, str]:
    register_agent(
        "worker-probe",
        "عامل المسبار",
        "worker",
        allowed_tools=[WILDCARD],
        status="active",
    )
    core = ExecutiveCore()
    task = core.submit("analysis", "مسبار WI-116")
    task_id = task["id"]
    for _ in range(4):
        core.advance(task_id)
    assert core._repo.state_of(task_id) is TaskState.EXECUTING

    ledger = OutboxLedger(tmp_path / "outbox.json")
    payload = EffectPayload(data={"task_id": task_id})
    signature = f"EXECUTION:executive.task:{task_id}"
    op_key = f"probe:{task_id}"
    effect_id = compute_effect_id(
        operation_key=op_key,
        effect_signature=signature,
        provider=PROVIDER,
        payload_digest=payload.digest,
    )
    ledger.enqueue(
        effect_id=effect_id,
        operation_key=op_key,
        effect_signature=signature,
        provider=PROVIDER,
        provider_supports_idempotency=supports,
        payload=payload,
        permit_id="probe-permit",
        authorization_anchor="probe-anchor",
    )
    counter = tmp_path / "dispatch_count.txt"
    script = CHILD.format(
        root=str(ROOT),
        counter=str(counter),
        provider=PROVIDER,
        ledger=str(ledger.path),
        lease=LEASE,
        supports=supports,
    )
    child = subprocess.run(
        [sys.executable, "-c", script],
        env=dict(os.environ),
        capture_output=True,
        text=True,
    )
    print(f"\n[probe] child exit code = {child.returncode}")
    assert child.returncode == 137, child.stderr[-2000:]
    return core, task_id, ledger, counter, effect_id


def _counting(core: ExecutiveCore, counter: Path) -> None:
    real_dispatch = core._runtime.dispatch

    def counted_dispatch(*args: Any, **kwargs: Any) -> Any:
        outcome = real_dispatch(*args, **kwargs)
        _IN_PROCESS.append(str(counter))
        return outcome

    core._runtime.dispatch = counted_dispatch


class _RunAdapter:
    name = PROVIDER

    def __init__(self, core: ExecutiveCore, supports: bool) -> None:
        self.core = core
        self.supports_idempotency = supports

    def deliver(self, envelope: Any) -> DeliveryReceipt:
        self.core.run(envelope.payload["task_id"])
        return DeliveryReceipt(outcome=DeliveryOutcome.SUCCESS)


def _report(name: str, data: dict[str, Any]) -> None:
    print(f"[probe] {name} = " + json.dumps(data, ensure_ascii=False, sort_keys=True))


@pytest.mark.parametrize("supports", [False, True])
def test_p1_crash_then_reclaim(tmp_path: Path, supports: bool) -> None:
    """السقوطُ ⇒ ما يفعلُه الصادرُ بعدَ انقضاءِ الحجز، بحسبِ إقرارِ التفرّد.

    `supports=False`: لا إعادة، والمسلكُ المعلَنُ (`recover`) يُعلِنُ الفشل.
    `supports=True`: **الثغرةُ المقيسة** — الغامضُ يُعادُ حجزُه رغمَ `max_attempts=1`.
    """
    core, task_id, ledger, counter, effect_id = _stage(tmp_path, supports=supports)
    after_crash = ledger.require(effect_id)
    state_after_crash = core._repo.state_of(task_id)

    later = datetime.now(UTC) + timedelta(seconds=LEASE + 5)
    reclaimed = ledger.reclaim_expired(now=later)
    record = ledger.require(effect_id)
    status_after_reclaim = record.status
    human = record.requires_human_resolution
    claimable = record.is_claimable(now=later)

    survivor = ExecutiveCore()
    _counting(survivor, counter)
    second = OutboxWorker(
        ledger=ledger,
        adapters={PROVIDER: _RunAdapter(survivor, supports)},
        worker_id="worker-B",
        lease_seconds=LEASE,
        max_attempts=1,
    ).run_once(now=later)

    report = survivor.recover()
    final = core._repo.require(task_id)
    settled = ledger.require(effect_id)
    _report(
        f"P1[supports_idempotency={supports}]",
        {
            "task_state_after_crash": state_after_crash.value,
            "outbox_status_after_crash": after_crash.status.value,
            "in_flight_after_crash": after_crash.in_flight_attempt_id is not None,
            "reclaimed": len(reclaimed),
            "outbox_status_after_reclaim": status_after_reclaim.value,
            "requires_human_resolution": human,
            "claimable_after_reclaim": claimable,
            "redelivery_by_second_worker": second is not None,
            "dispatch_count": _counted(counter),
            "attempt_count": settled.attempt_count,
            "outbox_status_final": settled.status.value,
            "recover_interrupted_count": report["interrupted_count"],
            "task_state_final": final["status"],
            "task_error": (final["result"] or {}).get("error"),
        },
    )
    assert state_after_crash is TaskState.EXECUTING
    assert after_crash.status is DeliveryStatus.CLAIMED
    assert status_after_reclaim is DeliveryStatus.INDETERMINATE
    if supports:
        assert second is not None
        assert _counted(counter) == 2
        assert settled.attempt_count == 2
        assert final["status"] == TaskState.COMPLETED.value
    else:
        assert human
        assert second is None
        assert _counted(counter) == 1
        assert final["status"] == TaskState.FAILED.value
        assert final["result"]["error"] == "interrupted_execution"


def test_p2_measured_gap_direct_advance_redispatches(tmp_path: Path) -> None:
    """الثغرةُ المقيسة: `advance` المباشرُ على مهمّةٍ عالقةٍ يُعيدُ dispatch اليوم."""
    core, task_id, ledger, counter, effect_id = _stage(tmp_path, supports=False)
    _counting(core, counter)
    core.advance(task_id)  # كما يفعلُ POST /v1/executive/tasks/{id}/advance
    final_state = core._repo.state_of(task_id)
    _report(
        "P2",
        {
            "dispatch_count": _counted(counter),
            "task_state": final_state.value,
            "outbox_status": ledger.require(effect_id).status.value,
        },
    )
    assert _counted(counter) == 2
    assert final_state is TaskState.COMPLETED


@pytest.mark.parametrize("max_attempts", [1, 3])
def test_p3_retryable_failure_by_max_attempts(
    tmp_path: Path, max_attempts: int
) -> None:
    """أثرُ `max_attempts` وحدَه: فشلٌ يقبلُ الإعادةَ عندَ المحاولةِ الأولى."""
    ledger = OutboxLedger(tmp_path / "outbox.json")
    payload = EffectPayload(data={"task_id": "t-p3"})
    signature = "EXECUTION:executive.task:t-p3"
    effect_id = compute_effect_id(
        operation_key="probe:p3",
        effect_signature=signature,
        provider=PROVIDER,
        payload_digest=payload.digest,
    )
    ledger.enqueue(
        effect_id=effect_id,
        operation_key="probe:p3",
        effect_signature=signature,
        provider=PROVIDER,
        provider_supports_idempotency=True,
        payload=payload,
        permit_id="probe-permit",
        authorization_anchor="probe-anchor",
    )
    ledger.claim(effect_id=effect_id, worker_id="w")
    ledger.begin_attempt(effect_id=effect_id, worker_id="w")
    record = ledger.record_result(
        effect_id=effect_id,
        worker_id="w",
        receipt=DeliveryReceipt(outcome=DeliveryOutcome.RETRYABLE_FAILURE),
        max_attempts=max_attempts,
    )
    _report(
        f"P3[max_attempts={max_attempts}]",
        {"status": record.status.value, "terminal_reason": record.terminal_reason},
    )
    expected = (
        DeliveryStatus.DEAD if max_attempts == 1 else DeliveryStatus.FAILED_RETRYABLE
    )
    assert record.status is expected
