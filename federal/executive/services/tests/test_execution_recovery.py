"""مسبارُ القبولِ الدائمُ لـ WI-116: إسقاطُ العاملِ بينَ dispatch والتثبيت

الهدف: إثباتُ معيارِ القبولِ في قرارِ المالكِ D24-R2 — مسلكُ استردادٍ معلَنٌ للمهمّةِ
    العالقةِ في EXECUTING بعدَ سقوطِ العامل، ومسبارٌ يُسقِطُ العاملَ هناك فعلًا
النطاق: `executive_core/engine.py` (علامةُ بدءِ التنفيذ · `recover`) و`core/sovereignty/outbox.py`
    (سقفُ المحاولةِ الواحدةِ لنوعِ EXECUTION)
المالك: W-720 · WI-116
تاريخ الإنشاء: 2026-10-28

السقوطُ حقيقيٌّ كما في مسبارِ W-719 (`docs/audit/evidence/W-719/probe_execution_crash.py`):
عمليّةٌ فرعيّةٌ تُنهي نفسَها بـ`os._exit(137)` بعدَ عودةِ `dispatch` فلا يكتبُ أيُّ
`finally` شيئًا، والمُستعيدُ عمليّةٌ أخرى. ما قاسَه W-719 ثغرةً (dispatch=2 من
`advance` المباشر ومن الصادرِ المُقِرِّ بالتفرّد) يُقاسُ هنا مسدودًا.
"""

from __future__ import annotations

import os
import subprocess
import sys
import textwrap
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, Any

import pytest

from amos_federation.common.database import init_db
from amos_federation.services.executive_core import (
    ExecutionRefusedError,
    ExecutiveCore,
    TaskState,
    register_agent,
    reset_executive_core,
)
from amos_federation.services.executive_core.dispatcher import WILDCARD
from amos_federation.services.executive_core.engine import (
    EXECUTION_BEGIN_FIELD,
    EXECUTION_RECOVERY_GRACE_SECONDS,
)
from amos_federation.services.executive_core.sovereignty_bridge import locate_repo_root

ROOT = locate_repo_root()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.sovereignty.outbox import (  # noqa: E402
    DEFAULT_LEASE_SECONDS,
    DeliveryOutcome,
    DeliveryReceipt,
    DeliveryStatus,
    EffectPayload,
    OutboxError,
    OutboxLedger,
    OutboxWorker,
    compute_effect_id,
)

if TYPE_CHECKING:
    from pathlib import Path

PROVIDER = "executive.run"

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
        real_dispatch(*args, **kwargs)
        with counter.open("a", encoding="utf-8") as fh:
            fh.write("dispatch\\n")
        os._exit(137)  # سقوطٌ بينَ dispatch والتثبيت — لا finally ولا تسجيل

    core._runtime.dispatch = dispatch_then_die

    class RunAdapter:
        name = {provider!r}
        supports_idempotency = False

        def deliver(self, envelope):
            core.run(envelope.payload["task_id"])
            return DeliveryReceipt(outcome=DeliveryOutcome.SUCCESS)

    worker = OutboxWorker(
        ledger=OutboxLedger(Path({ledger!r})),
        adapters={{{provider!r}: RunAdapter()}},
        worker_id="worker-A",
        max_attempts=3,  # العاملُ يطلبُ ثلاثًا — والسقفُ من التوقيعِ واحد
    )
    worker.run_once()
    sys.exit(0)  # لا يُبلَغ إن صدقَ السقوط
    """
)


@pytest.fixture(autouse=True)
def _fresh_core() -> None:
    """قاعدةُ الاختبارِ طازجةٌ للجلسة (`tests/conftest.py`)، وكلُّ مهمّةٍ بمعرِّفٍ جديد.

    لا تطهيرَ ولا عدَّ عامًّا: التأكيداتُ على مهمّةِ الاختبارِ نفسِها لا على أعدادِ `recover`.
    """
    init_db()
    reset_executive_core()


@pytest.fixture
def worker() -> dict[str, Any]:
    return register_agent(
        "worker-wi116",
        "عامل مسبار WI-116",
        "worker",
        allowed_tools=[WILDCARD],
        status="active",
    )


#: نداءاتُ dispatch في هذه العمليّة — وما في العمليّةِ الفرعيّةِ يُقرأُ من ملفِّها.
_IN_PROCESS: list[str] = []


def _counted(counter: Path) -> int:
    child = 0
    if counter.exists():
        child = len(counter.read_text(encoding="utf-8").splitlines())
    return child + _IN_PROCESS.count(str(counter))


def _counting(core: ExecutiveCore, counter: Path) -> None:
    real_dispatch = core._runtime.dispatch

    def counted_dispatch(*args: Any, **kwargs: Any) -> Any:
        outcome = real_dispatch(*args, **kwargs)
        _IN_PROCESS.append(str(counter))
        return outcome

    core._runtime.dispatch = counted_dispatch


def _to_executing(core: ExecutiveCore, label: str) -> str:
    task_id = core.submit("analysis", label)["id"]
    for _ in range(4):
        core.advance(task_id)
    assert core._repo.state_of(task_id) is TaskState.EXECUTING
    return task_id


def _enqueue(ledger: OutboxLedger, task_id: str, *, supports: bool = False) -> str:
    payload = EffectPayload(data={"task_id": task_id})
    signature = f"EXECUTION:executive.task:{task_id}"
    op_key = f"wi116:{task_id}"
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
        permit_id="wi116-permit",
        authorization_anchor="wi116-anchor",
    )
    return effect_id


def _crash(tmp_path: Path, ledger: OutboxLedger, counter: Path) -> None:
    script = CHILD.format(
        root=str(ROOT), counter=str(counter), provider=PROVIDER, ledger=str(ledger.path)
    )
    child = subprocess.run(
        [sys.executable, "-c", script], env=dict(os.environ), capture_output=True, text=True
    )
    assert child.returncode == 137, child.stderr[-2000:]


def _interrupted(report: dict[str, Any], task_id: str) -> bool:
    return any(item.get("task_id") == task_id for item in report["interrupted"])


def _deferred(report: dict[str, Any], task_id: str) -> bool:
    return any(item["task_id"] == task_id for item in report["deferred"])


def test_crash_between_dispatch_and_commit_has_one_declared_path(
    tmp_path: Path, worker: dict[str, Any]
) -> None:
    """المعيارُ كلُّه: سقوطٌ حقيقيٌّ ⇒ تنفيذٌ واحد، ولا مسلكَ إلّا `recover()` بعدَ المهلة."""
    core = ExecutiveCore()
    task_id = _to_executing(core, "مسبار WI-116 — سقوط")
    ledger = OutboxLedger(tmp_path / "outbox.json")
    effect_id = _enqueue(ledger, task_id)
    counter = tmp_path / "dispatch_count.txt"

    _crash(tmp_path, ledger, counter)
    assert _counted(counter) == 1
    stuck = core._repo.require(task_id)
    assert stuck["status"] == TaskState.EXECUTING.value
    marker = stuck["result"][EXECUTION_BEGIN_FIELD]
    assert marker["at"] and marker["by"]
    assert "dispatch" in stuck["result"], "العلامةُ لا تمحو تعيينَ التوزيع"

    # الصادرُ: الغامضُ لا يُعادُ حجزُه — والسقفُ من التوقيعِ لا من `max_attempts=3`.
    later = datetime.now(UTC) + timedelta(seconds=DEFAULT_LEASE_SECONDS + 5)
    ledger.reclaim_expired(now=later)
    record = ledger.require(effect_id)
    assert record.status is DeliveryStatus.INDETERMINATE
    assert record.requires_human_resolution
    assert not record.is_claimable(now=later)

    survivor = ExecutiveCore()
    _counting(survivor, counter)
    second = OutboxWorker(
        ledger=ledger,
        adapters={PROVIDER: _Adapter(survivor)},
        worker_id="worker-B",
        max_attempts=3,
    ).run_once(now=later)
    assert second is None

    # `POST /advance` و`POST /run`: رفضٌ صريحٌ لا dispatch ثانٍ.
    with pytest.raises(ExecutionRefusedError):
        survivor.advance(task_id)
    with pytest.raises(ExecutionRefusedError):
        survivor.run(task_id)
    assert _counted(counter) == 1

    # `recover()` قبلَ المهلة يؤجِّل — لا يُسقِطُ تنفيذًا قد يكونُ حيًّا.
    began = datetime.fromisoformat(marker["at"])
    early = survivor.recover(now=began + timedelta(seconds=EXECUTION_RECOVERY_GRACE_SECONDS))
    assert _deferred(early, task_id)
    assert not _interrupted(early, task_id)
    assert survivor._repo.state_of(task_id) is TaskState.EXECUTING

    # وبعدَها يُعلِنُ الفشلَ ويقولُ إنَّ dispatch وقع.
    late = survivor.recover(now=began + timedelta(seconds=EXECUTION_RECOVERY_GRACE_SECONDS + 1))
    assert _interrupted(late, task_id)
    final = survivor._repo.require(task_id)
    assert final["status"] == TaskState.FAILED.value
    assert final["result"]["error"] == "interrupted_execution"
    assert final["result"]["dispatched"] is True
    assert final["result"][EXECUTION_BEGIN_FIELD] == marker
    assert _counted(counter) == 1


class _Adapter:
    name = PROVIDER
    supports_idempotency = False

    def __init__(self, core: ExecutiveCore) -> None:
        self.core = core

    def deliver(self, envelope: Any) -> DeliveryReceipt:
        self.core.run(envelope.payload["task_id"])
        return DeliveryReceipt(outcome=DeliveryOutcome.SUCCESS)


def test_never_dispatched_executing_task_fails_with_dispatched_false(
    worker: dict[str, Any],
) -> None:
    """ما لم تُكتَب عليه علامةٌ لم يُنادِ dispatch — يُسترَدُّ فورًا ويقولُ ذلك."""
    core = ExecutiveCore()
    task_id = _to_executing(core, "مسبار WI-116 — بلا dispatch")
    report = core.recover()
    assert _interrupted(report, task_id)
    final = core._repo.require(task_id)
    assert final["status"] == TaskState.FAILED.value
    assert final["result"]["dispatched"] is False
    assert final["result"][EXECUTION_BEGIN_FIELD] is None


def test_successful_execution_keeps_marker_and_completes_once(
    tmp_path: Path, worker: dict[str, Any]
) -> None:
    """المسارُ السليمُ لم يتغيّر: dispatch واحدٌ ثمّ `COMPLETED`، والعلامةُ لا تُعيقُه."""
    core = ExecutiveCore()
    counter = tmp_path / "ok.txt"
    _counting(core, counter)
    task_id = _to_executing(core, "مسبار WI-116 — سليم")
    core.advance(task_id)
    assert core._repo.state_of(task_id) is TaskState.COMPLETED
    assert _counted(counter) == 1


def test_marker_refused_when_task_left_executing(worker: dict[str, Any]) -> None:
    """العلامةُ مشروطةٌ بالحالة: إن سبقَها استردادٌ فلا علامةَ ولا dispatch."""
    core = ExecutiveCore()
    task_id = _to_executing(core, "مسبار WI-116 — سباق")
    stale = core._repo.require(task_id)
    core.recover()
    assert core._repo.state_of(task_id) is TaskState.FAILED
    with pytest.raises(ExecutionRefusedError):
        core._mark_execution_begin(stale)


def test_marker_operation_key_is_single_use(worker: dict[str, Any]) -> None:
    """مفتاحُ الذرّيّةِ `<id>:execution-begin` لا يُثبِّتُ العلامةَ مرّتين."""
    core = ExecutiveCore()
    task_id = _to_executing(core, "مسبار WI-116 — مفتاح")
    task = core._repo.require(task_id)
    core._mark_execution_begin(task)
    with pytest.raises(ExecutionRefusedError):
        core._mark_execution_begin(task)


def test_execution_signature_refuses_declared_idempotency(tmp_path: Path) -> None:
    """الجزءُ (ب): مزوِّدُ EXECUTION لا يُقِرُّ بالتفرّد — فالثغرةُ المقيسةُ في P1 مُغلقة."""
    ledger = OutboxLedger(tmp_path / "outbox.json")
    with pytest.raises(OutboxError):
        _enqueue(ledger, "t-wi116-b", supports=True)


def test_grace_equals_outbox_lease() -> None:
    """المهلةُ هي ساعةُ هجرِ العاملِ نفسُها في الصادر — يُقاسُ التطابقُ ولا يُفترَض."""
    assert EXECUTION_RECOVERY_GRACE_SECONDS == DEFAULT_LEASE_SECONDS
