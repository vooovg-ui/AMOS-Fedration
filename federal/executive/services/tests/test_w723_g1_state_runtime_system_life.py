"""W-723 · G1 الدفعة 2 — عبورُ state_runtime (5) وsystem_life (6) الحدَّ السياديّ.

الهدف: إثباتُ أنَّ الأسطحَ الأحدَ عشرَ تعبرُ الحدَّ بأفعالِ جدولِ G1 § 2، وأنَّ الرفضَ
       قبلَ أيِّ كتابة، وأنَّ الإعادةَ لا تُكرِّرُ الأثر، وأنَّ المعوِّضَ عكسٌ حقيقيّ،
       وQ-13 (مرسومُ `create_state`) وQ-14 (إيقافٌ محكومٌ لا ينقضُه `self_heal`).
النطاق: سلوكُ الأسطحِ المعبَّرةِ وحدَه — لا تعديلَ للبوابةِ ولا للقواعد. حقنُ مستوى
        القاطعِ في الطلبِ محاكاةٌ لحالتِه معلَنةٌ هنا (نمطُ WI-082 · E1)، لأنَّ الجسرَ
        لا يحقنُه في الإنتاج (DISC-099/WI-085). والتاجُ يُنصَّبُ في مجلَّدٍ مؤقَّت.
المالك: federal/executive/services — WI-120 (G1 · تصميمُ W-721 § 9 و§ 9.8).
تاريخ الإنشاء: 2026-10-28 (W-723)

أصنافُ الفحصِ الخمسةُ (G1 § 4): 1 الرفضُ قبلَ الكتابة · 2 النجاحُ عبرَ الحدّ ·
3 طفرةٌ لكلِّ سطح · 4 الإعادةُ لا تُكرِّر · 5 المعوِّضُ على المسارِ الحقيقيّ.

الدليلُ المُعادُ تشغيلُه (من federal/executive/services):
    ../../../.venv/bin/python -m pytest tests/test_w723_g1_state_runtime_system_life.py -q
"""

from __future__ import annotations

import ast
import dataclasses
import inspect
import textwrap
import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

import pytest

from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from amos_federation.services.governance import state_runtime as sr
from amos_federation.services.governance import system_life as sl
from amos_federation.services.governance.state_runtime import (
    DecreeTargetMismatchError,
    FederalMessageBus,
    StateAgentAssignment,
    StateMessage,
    StateModel,
    StateRuntime,
    StateSuspensionRecord,
)
from amos_federation.services.governance.system_life import (
    BackupModel,
    SystemEventModel,
    SystemLifecycle,
)

if TYPE_CHECKING:
    from pathlib import Path


# ── مُصرِّحاتُ القياس ─────────────────────────────────────────────────────────
class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجِّلُ كلَّ نتيجةٍ محروسة — للقياسِ لا للقرار (نمطُ WI-082)."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.results.append(guarded)
        return guarded


class KillSwitchAuthorizer(RecordingAuthorizer):
    """الطلبُ يحملُ مستوى القاطع — محاكاةُ حالتِه لا تجاوزٌ (نمطُ WI-082 · E1)."""

    def __init__(self, level: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._level = level

    def _request(self, action: str, target: str, metadata: dict[str, Any] | None = None) -> Any:
        request = super()._request(action, target, metadata)
        return dataclasses.replace(request, kill_switch_level=self._level)


def _violation() -> type[Exception]:
    from core.sovereignty.gateway import SovereigntyViolation

    return SovereigntyViolation


def _compensated() -> type[Exception]:
    """المعوِّضُ وقعَ فعلًا: الحدُّ يرفعُ `CompensationRequired` بحالةِ COMPENSATED."""
    from core.sovereignty.compensation import CompensationRequired

    return CompensationRequired


def _impersonation() -> type[Exception]:
    from core.sovereignty.gateway import RoyalImpersonation

    return RoyalImpersonation


# ── تجهيزات ──────────────────────────────────────────────────────────────────
@pytest.fixture(autouse=True)
def _cleanup_seeds() -> Any:
    """تنظيفُ بذورِ هذا الملفِّ بعدَ كلِّ فحص — لا بقايا تمسُّ فحوصًا أخرى."""
    yield
    rt = StateRuntime()
    session = rt._Session()
    try:
        for model in (StateModel, StateAgentAssignment, StateSuspensionRecord):
            column = model.state_id
            session.query(model).filter(column.like("w723-%")).delete(synchronize_session=False)
        session.query(StateMessage).filter(StateMessage.subject.like("w723%")).delete(
            synchronize_session=False
        )
        session.commit()
    finally:
        session.close()


@pytest.fixture
def rec() -> RecordingAuthorizer:
    return RecordingAuthorizer()


@pytest.fixture
def runtime(rec: RecordingAuthorizer) -> StateRuntime:
    return StateRuntime(authorizer=rec)


def _seed(rt: StateRuntime, status: str = "active") -> str:
    """بذرةُ ولايةٍ للفحصِ بجلسةٍ مباشرة — تجهيزٌ لا سطحٌ مَقيس."""
    state_id = f"w723-{uuid.uuid4().hex[:8]}"
    session = rt._Session()
    try:
        session.add(StateModel(state_id=state_id, name=state_id, type="test", status=status))
        session.commit()
    finally:
        session.close()
    return state_id


def _count(rt: Any, model: Any, **filters: Any) -> int:
    session = rt._Session()
    try:
        q = session.query(model)
        for key, value in filters.items():
            q = q.filter(getattr(model, key) == value)
        return int(q.count())
    finally:
        session.close()


def _evidence(r: RecordingAuthorizer) -> dict[str, Any]:
    assert r.results, "لم يُعبَرِ الحدُّ السياديُّ أصلًا"
    return dict(r.results[-1].evidence.as_dict())


@pytest.fixture
def crown(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> tuple[Any, str]:
    """تاجٌ منصَّبٌ في مجلَّدٍ مؤقَّت — لا يُمَسُّ `royal/crown/` في المستودع."""
    ConstitutionalAuthorizer().review_only("run_health_check", "system:health")  # تحميلُ النواة
    import core.sovereignty.crown as crown_mod
    from core.sovereignty.crown import provision_crown
    from cryptography.hazmat.primitives import serialization

    registry = tmp_path / "CROWN_KEYS.json"
    provision_crown(tmp_path / "crown.pem", registry_path=registry)
    monkeypatch.setattr(crown_mod, "CROWN_KEYS_PATH", registry)
    priv = serialization.load_pem_private_key((tmp_path / "crown.pem").read_bytes(), password=None)
    return priv, crown_mod.load_crown().key_id


def _decree(crown: tuple[Any, str], action: str, target: str) -> Any:
    from core.sovereignty.decree import RoyalDecree, sign_decree

    priv, key_id = crown
    unsigned = RoyalDecree(
        decree_id=f"d-{uuid.uuid4().hex[:8]}",
        action=action,
        target=target,
        issued_at=datetime.now(UTC).replace(microsecond=0).isoformat(),
        key_id=key_id,
    )
    return sign_decree(unsigned, priv)


# ═════════════════════════════════════════════════════════════════════════════
# Q-13 — register_state بمرسومٍ ملكيّ (G1 § 3.1 و§ 9.8.1)
# ═════════════════════════════════════════════════════════════════════════════
def test_q13_signed_decree_crosses_as_sovereign_royal(crown: tuple[Any, str]) -> None:
    royal = RecordingAuthorizer(actor="ROYAL")
    rt = StateRuntime(royal_authorizer=royal)
    state_id = f"w723-q13-{uuid.uuid4().hex[:6]}"
    out = rt.register_state(
        state_id, "ولاية", "test", royal_decree=_decree(crown, "create_state", f"state:{state_id}")
    )
    assert out["registered"] is True and out["replayed"] is False
    ev = _evidence(royal)
    assert ev["action"] == "create_state"
    assert ev["decision_kind"] == "SOVEREIGN_ROYAL"
    assert ev["authority_layer"] == "CROWN"
    # R-004-1 (75% + توقيعٌ بشريّ) مُخبِرٌ في المسارِ السياديّ — المرسومُ هوَ البوّابة.
    assert "A004" in ev["advisory_violations"]
    assert rt.get_state(state_id) is not None
    rt._delete_state_row(state_id)


def test_q13_royal_without_decree_refused_before_write(crown: tuple[Any, str]) -> None:
    rt = StateRuntime(royal_authorizer=RecordingAuthorizer(actor="ROYAL"))
    state_id = f"w723-q13-{uuid.uuid4().hex[:6]}"
    with pytest.raises(_impersonation(), match="ROYAL_COMMAND_UNSIGNED"):
        rt.register_state(state_id, "ولاية", "test")
    assert rt.get_state(state_id) is None


def test_q13_executive_fallback_is_denied_by_constitution() -> None:
    """بلا مُصرِّحٍ ملكيٍّ مُمرَّرٍ يعبرُ بالتنفيذيِّ فيرفضُه R-010-1 — لا كتابة."""
    rt = StateRuntime()
    state_id = f"w723-q13-{uuid.uuid4().hex[:6]}"
    with pytest.raises(_violation(), match="R-010-1"):
        rt.register_state(state_id, "ولاية", "test")
    assert rt.get_state(state_id) is None


def test_q13_decree_for_another_action_refused(crown: tuple[Any, str]) -> None:
    rt = StateRuntime(royal_authorizer=RecordingAuthorizer(actor="ROYAL"))
    state_id = f"w723-q13-{uuid.uuid4().hex[:6]}"
    with pytest.raises(_impersonation(), match="DECREE_ACTION_MISMATCH"):
        rt.register_state(
            state_id,
            "ولاية",
            "test",
            royal_decree=_decree(crown, "dissolve_state", f"state:{state_id}"),
        )
    assert rt.get_state(state_id) is None


def test_q13_decree_for_another_state_refused_before_crossing(crown: tuple[Any, str]) -> None:
    royal = RecordingAuthorizer(actor="ROYAL")
    rt = StateRuntime(royal_authorizer=royal)
    state_id = f"w723-q13-{uuid.uuid4().hex[:6]}"
    with pytest.raises(DecreeTargetMismatchError):
        rt.register_state(
            state_id, "ولاية", "test", royal_decree=_decree(crown, "create_state", "state:other")
        )
    assert rt.get_state(state_id) is None
    assert royal.results == []


def test_q13_decree_is_single_use_no_second_row(crown: tuple[Any, str]) -> None:
    """الصنفُ 4 للمسارِ الملكيّ: المرسومُ يُستهلَك — إعادتُه تُرفَضُ ولا صفَّ ثانيًا."""
    from core.sovereignty.decree import DecreeReplayError

    rt = StateRuntime(royal_authorizer=RecordingAuthorizer(actor="ROYAL"))
    state_id = f"w723-q13-{uuid.uuid4().hex[:6]}"
    decree = _decree(crown, "create_state", f"state:{state_id}")
    rt.register_state(state_id, "ولاية", "test", royal_decree=decree)
    rt._delete_state_row(state_id)
    with pytest.raises(DecreeReplayError):
        rt.register_state(state_id, "ولاية", "test", royal_decree=decree)
    assert rt.get_state(state_id) is None


# ═════════════════════════════════════════════════════════════════════════════
# Q-14 — suspend/reactivate وسجلُّ الإيقافِ المحكوم وself_heal بشرطِه
# ═════════════════════════════════════════════════════════════════════════════
def test_q14_suspend_declares_effect_with_previous_and_reason(
    runtime: StateRuntime, rec: RecordingAuthorizer
) -> None:
    state_id = _seed(runtime)
    out = runtime.suspend_state(state_id, "قرارُ احتواء")
    assert out["status"] == "suspended" and out["previous_status"] == "active"
    ev = _evidence(rec)
    assert ev["action"] == "contain_agent" and ev["target"] == f"state:{state_id}"
    applied = rec.results[-1].outcome.as_dict()["applied_effects"]
    assert applied == [f"WRITE:state:{state_id}/status.active->suspended@{out['operation_id']}"]
    assert runtime.has_governed_suspension(state_id)


def test_q14_self_heal_skips_governed_and_reactivates_automatic(runtime: StateRuntime) -> None:
    """شرطُ المالك: المحكومُ يبقى معلَّقًا · التلقائيُّ (بلا سجلّ) يُعادُ كما كان."""
    governed = _seed(runtime)
    runtime.suspend_state(governed, "قرار")
    automatic = _seed(runtime, status="suspended")  # تعليقٌ بلا قرار: لا سجلَّ له
    assert not runtime.has_governed_suspension(automatic)

    heal_rec = RecordingAuthorizer()
    out = SystemLifecycle(authorizer=heal_rec, state_runtime=runtime).self_heal("states")

    assert runtime.get_state(governed)["status"] == "suspended"
    assert runtime.get_state(automatic)["status"] == "active"
    assert {"action": "reactivate", "target": automatic} in out["actions"]
    assert {"action": "noop", "target": governed, "message": "governed_suspension"} in out[
        "actions"
    ]
    assert _evidence(heal_rec)["action"] == "self_heal"
    applied = heal_rec.results[-1].outcome.as_dict()["applied_effects"]
    assert f"WRITE:system:heal:states/state:{automatic}" in applied
    assert not any(governed in a for a in applied)


def test_q14_reactivate_clears_record_then_self_heal_has_nothing(runtime: StateRuntime) -> None:
    state_id = _seed(runtime)
    runtime.suspend_state(state_id, "قرار")
    runtime.reactivate_state(state_id)
    assert runtime.get_state(state_id)["status"] == "active"
    assert not runtime.has_governed_suspension(state_id)


def test_q14_kill_switch_level5_blocks_reactivate_not_suspend(runtime: StateRuntime) -> None:
    """على المسارِ الحقيقيّ: القاطعُ 5 يمنعُ `activate_agent` ولا يمنعُ `contain_agent`."""
    state_id = _seed(runtime)
    ks = StateRuntime(authorizer=KillSwitchAuthorizer(5))
    ks.suspend_state(state_id, "احتواءٌ تحتَ القاطع")
    assert ks.get_state(state_id)["status"] == "suspended"
    with pytest.raises(_violation(), match="activate_agent"):
        ks.reactivate_state(state_id)
    assert ks.get_state(state_id)["status"] == "suspended"
    assert ks.has_governed_suspension(state_id)


def test_q14_rules_level_kill_switch_semantics() -> None:
    """على مستوى القواعد (المحرّك نفسُه): ≥4 يمنعُ activate_agent · contain_agent لا يُمنَع."""
    ConstitutionalAuthorizer().review_only("run_health_check", "system:health")
    from core.constitutional_engine.engine import ConstitutionalEngine
    from core.constitutional_engine.model import ActionRequest, Branch, Decision

    engine = ConstitutionalEngine()

    def verdict(action: str, level: int) -> Any:
        return engine.evaluate(
            ActionRequest(
                actor=Branch.EXECUTIVE,
                action=action,
                target="state:x",
                channel="official",
                kill_switch_level=level,
            )
        ).decision

    assert verdict("activate_agent", 3) is Decision.ALLOW
    assert verdict("activate_agent", 4) is Decision.DENY
    assert verdict("activate_agent", 5) is Decision.DENY
    for level in range(6):
        assert verdict("contain_agent", level) is Decision.ALLOW


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 1 — الرفضُ قبلَ أيِّ كتابة (القاطعُ على المسارِ الحقيقيّ)
# ═════════════════════════════════════════════════════════════════════════════
def test_c1_assign_agent_blocked_at_level3_no_row(runtime: StateRuntime) -> None:
    state_id = _seed(runtime)
    ks = StateRuntime(authorizer=KillSwitchAuthorizer(3))
    with pytest.raises(_violation(), match="dispatch_agent"):
        ks.assign_agent(state_id, "agent-w723", "worker")
    assert _count(ks, StateAgentAssignment, state_id=state_id) == 0


def test_c1_send_message_blocked_at_level4_no_row(runtime: StateRuntime) -> None:
    a, b = _seed(runtime), _seed(runtime)
    subject = f"w723-{uuid.uuid4().hex[:6]}"
    bus = FederalMessageBus(authorizer=KillSwitchAuthorizer(4))
    with pytest.raises(_violation(), match="coordinate"):
        bus.send_message(a, b, subject)
    assert _count(bus, StateMessage, subject=subject) == 0


@pytest.mark.parametrize(
    ("surface", "event_type", "action"),
    [
        ("bootstrap", "bootstrap", "orchestrate"),
        ("graceful_shutdown", "shutdown", "orchestrate"),  # Q-76: المقيسُ لا المكتوب
        ("launch_checklist", "launch", "orchestrate"),  # Q-76: المقيسُ لا المكتوب
    ],
)
def test_c1_orchestrate_surfaces_blocked_at_level4_no_event(
    surface: str, event_type: str, action: str
) -> None:
    """Q-76 (G1 § 9.8.3): `orchestrate` ∈ KILL_SWITCH_BLOCKS[4] — يُثبَّتُ المقيسُ ويُرفَعُ للمالك."""
    life = SystemLifecycle(authorizer=KillSwitchAuthorizer(4))
    before = _count(life, SystemEventModel, event_type=event_type)
    with pytest.raises(_violation(), match=action):
        getattr(life, surface)()
    assert _count(life, SystemEventModel, event_type=event_type) == before


def test_c1_self_heal_blocked_at_level4_state_untouched(runtime: StateRuntime) -> None:
    automatic = _seed(runtime, status="suspended")
    life = SystemLifecycle(authorizer=KillSwitchAuthorizer(4), state_runtime=runtime)
    with pytest.raises(_violation(), match="self_heal"):
        life.self_heal("states")
    assert runtime.get_state(automatic)["status"] == "suspended"


@pytest.mark.parametrize("surface", ["health_check", "create_backup"])
def test_c1_monitoring_and_recovery_never_blocked(surface: str) -> None:
    life = SystemLifecycle(authorizer=KillSwitchAuthorizer(5))
    out = getattr(life, surface)()
    assert out.get("event_id") or out.get("backup_id")


# ═════════════════════════════════════════════════════════════════════════════
# الصنفان 2 و3 — النجاحُ عبرَ الحدِّ بالفعلِ المُسمّى، وطفرةٌ لكلِّ سطح
# ═════════════════════════════════════════════════════════════════════════════
def _call_surface(name: str, rt: StateRuntime, rec: RecordingAuthorizer) -> None:
    life = SystemLifecycle(authorizer=rec, state_runtime=rt)
    state_id = _seed(rt)
    calls = {
        "suspend_state": lambda: rt.suspend_state(state_id, "س"),
        "reactivate_state": lambda: (
            rt.suspend_state(state_id, "س"),
            rt.reactivate_state(state_id),
        ),
        "assign_agent": lambda: rt.assign_agent(state_id, f"ag-{state_id}", "worker"),
        "send_message": lambda: FederalMessageBus(authorizer=rec).send_message(
            state_id, _seed(rt), "w723"
        ),
        "bootstrap": life.bootstrap,
        "health_check": life.health_check,
        "self_heal": lambda: life.self_heal("audit_chain"),
        "graceful_shutdown": life.graceful_shutdown,
        "create_backup": life.create_backup,
        "launch_checklist": life.launch_checklist,
    }
    calls[name]()


SURFACES = [
    # (الصنف، السطح، الفعلُ المتوقَّع، ثابتُ الفعلِ في المصدر)
    (StateRuntime, "suspend_state", "contain_agent", "ACTION_SUSPEND_STATE"),
    (StateRuntime, "reactivate_state", "activate_agent", "ACTION_REACTIVATE_STATE"),
    (StateRuntime, "assign_agent", "dispatch_agent", "ACTION_ASSIGN_AGENT"),
    (FederalMessageBus, "send_message", "coordinate", "ACTION_SEND_MESSAGE"),
    (SystemLifecycle, "bootstrap", "orchestrate", "ACTION_ORCHESTRATE"),
    (SystemLifecycle, "health_check", "run_health_check", "ACTION_HEALTH_CHECK"),
    (SystemLifecycle, "self_heal", "self_heal", "ACTION_SELF_HEAL"),
    (SystemLifecycle, "graceful_shutdown", "orchestrate", "ACTION_ORCHESTRATE"),
    (SystemLifecycle, "create_backup", "create_backup", "ACTION_CREATE_BACKUP"),
    (SystemLifecycle, "launch_checklist", "orchestrate", "ACTION_ORCHESTRATE"),
]


@pytest.mark.parametrize(("owner", "surface", "action", "const"), SURFACES)
def test_c2_surface_crosses_with_named_action(
    owner: type,
    surface: str,
    action: str,
    const: str,
    runtime: StateRuntime,
    rec: RecordingAuthorizer,
) -> None:
    _call_surface(surface, runtime, rec)
    assert _evidence(rec)["action"] == action
    assert _evidence(rec)["decision"] == "ALLOW"


@pytest.mark.parametrize(("owner", "surface", "action", "const"), SURFACES)
def test_c3_mutation_guard_call_literally_in_public_body(
    owner: type, surface: str, action: str, const: str
) -> None:
    """طفرةُ رفعِ الحرس: نداءُ `guard_declared` بثابتِ الفعلِ في جسدِ السطحِ نفسِه.

    حذفُ النداءِ أو تبديلُ الفعلِ يُسقطُ هذا الفحص، والصنفُ 2 يُسقطُه سلوكيًّا (لا دليل).
    """
    tree = ast.parse(textwrap.dedent(inspect.getsource(getattr(owner, surface))))
    calls = [
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr == "guard_declared"
    ]
    assert len(calls) == 1, f"{surface}: نداءُ العبورِ ليس واحدًا في الجسد"
    first = calls[0].args[0]
    assert isinstance(first, ast.Name) and first.id == const
    module = sr if owner in (StateRuntime, FederalMessageBus) else sl
    assert getattr(module, const) == action


def test_c3_mutation_register_state_and_restore_backup_untouched() -> None:
    """register_state يعبرُ بـACTION_CREATE_STATE · restore_backup دَينٌ لم يُمَسّ (G1 § 9.4)."""
    src = textwrap.dedent(inspect.getsource(StateRuntime.register_state))
    assert "guard_declared(" in src and "ACTION_CREATE_STATE" in src
    assert sr.ACTION_CREATE_STATE == "create_state"
    assert "guard_declared" not in inspect.getsource(SystemLifecycle.restore_backup)


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 4 — الإعادةُ لا تُكرِّرُ الأثر
# ═════════════════════════════════════════════════════════════════════════════
def test_c4_suspend_replay_same_key_writes_no_second_record(
    runtime: StateRuntime, rec: RecordingAuthorizer
) -> None:
    state_id = _seed(runtime)
    runtime.suspend_state(state_id, "س", operation_id="op-w723")
    runtime._set_status(state_id, "active")  # الحالةُ السابقةُ تعودُ فيتطابقُ المفتاح
    out = runtime.suspend_state(state_id, "س", operation_id="op-w723")
    assert out.get("replayed") is True and rec.results[-1].is_replay
    assert runtime.get_state(state_id)["status"] == "active"  # لا أثرَ ثانٍ
    assert _count(runtime, StateSuspensionRecord, state_id=state_id) == 1


def test_c4_reactivate_of_active_is_noop_without_crossing(
    runtime: StateRuntime, rec: RecordingAuthorizer
) -> None:
    state_id = _seed(runtime)
    out = runtime.reactivate_state(state_id)
    assert out == {"state_id": state_id, "status": "active", "noop": True}
    assert rec.results == []


def test_c4_assign_replay_same_operation_one_row(
    runtime: StateRuntime, rec: RecordingAuthorizer
) -> None:
    state_id = _seed(runtime)
    runtime.assign_agent(state_id, "ag-r", "worker", operation_id="op-a")
    out = runtime.assign_agent(state_id, "ag-r", "worker", operation_id="op-a")
    assert out.get("replayed") is True
    assert _count(runtime, StateAgentAssignment, state_id=state_id) == 1


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 5 — المعوِّضُ على المسارِ الحقيقيّ
# ═════════════════════════════════════════════════════════════════════════════
def _boom(*_a: Any, **_k: Any) -> None:
    raise RuntimeError("فشلٌ بعدَ الكتابةِ الأولى")


def _break_commit(monkeypatch: pytest.MonkeyPatch) -> None:
    """انكسارُ مرحلةِ التثبيتِ بعدَ عودةِ المُطبِّق (نمطُ E1 الصنف 5 · test_e1_13).

    الحدُّ يُعوِّضُ ما طُبِّقَ من آثار؛ أمّا فشلٌ **داخلَ** مُطبِّقٍ وحيدِ الأثرِ فدَينٌ
    مُعلَنٌ منذ 2A (test_2a G-7) لا يُزعَمُ هنا تعويضُه.
    """
    ConstitutionalAuthorizer().review_only("run_health_check", "system:health")
    from core.sovereignty.idempotency import IdempotencyLedger

    def _fail(self: Any, *args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("فشلٌ بعدَ الكتابة — انكسارُ مرحلةِ التثبيت")

    monkeypatch.setattr(IdempotencyLedger, "mark_succeeded", _fail)


BROKEN = "فشلٌ بعدَ الكتابة"


def test_c5_q13_compensator_removes_row(
    crown: tuple[Any, str], monkeypatch: pytest.MonkeyPatch
) -> None:
    rt = StateRuntime(royal_authorizer=RecordingAuthorizer(actor="ROYAL"))
    state_id = f"w723-q13-{uuid.uuid4().hex[:6]}"
    decree = _decree(crown, "create_state", f"state:{state_id}")
    _break_commit(monkeypatch)
    with pytest.raises(Exception, match=BROKEN):
        rt.register_state(state_id, "ولاية", "test", royal_decree=decree)
    assert rt.get_state(state_id) is None


def test_c5_suspend_failure_restores_status_and_deletes_record(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rt = StateRuntime()
    state_id = _seed(rt)
    _break_commit(monkeypatch)
    with pytest.raises(Exception, match=BROKEN):
        rt.suspend_state(state_id, "س")
    assert rt.get_state(state_id)["status"] == "active"
    assert _count(rt, StateSuspensionRecord, state_id=state_id) == 0


def test_c5_reactivate_failure_restores_suspension_and_record(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rt = StateRuntime()
    state_id = _seed(rt)
    rt.suspend_state(state_id, "س")
    _break_commit(monkeypatch)
    with pytest.raises(Exception, match=BROKEN):
        rt.reactivate_state(state_id)
    assert rt.get_state(state_id)["status"] == "suspended"
    assert rt.has_governed_suspension(state_id)


def test_c5_assign_failure_deletes_row(monkeypatch: pytest.MonkeyPatch) -> None:
    rt = StateRuntime()
    state_id = _seed(rt)
    _break_commit(monkeypatch)
    with pytest.raises(Exception, match=BROKEN):
        rt.assign_agent(state_id, "ag-c5", "worker")
    assert _count(rt, StateAgentAssignment, state_id=state_id) == 0


def test_c5_send_message_failure_deletes_row(
    runtime: StateRuntime, monkeypatch: pytest.MonkeyPatch
) -> None:
    a, b = _seed(runtime), _seed(runtime)
    subject = f"w723-{uuid.uuid4().hex[:6]}"
    bus = FederalMessageBus()
    _break_commit(monkeypatch)
    with pytest.raises(Exception, match=BROKEN):
        bus.send_message(a, b, subject)
    assert _count(bus, StateMessage, subject=subject) == 0


def test_c5_create_backup_failure_deletes_backup_row(monkeypatch: pytest.MonkeyPatch) -> None:
    life = SystemLifecycle()
    before = (_count(life, BackupModel), _count(life, SystemEventModel, event_type="backup"))
    _break_commit(monkeypatch)
    with pytest.raises(Exception, match=BROKEN):
        life.create_backup("w723")
    after = (_count(life, BackupModel), _count(life, SystemEventModel, event_type="backup"))
    assert after == before


@pytest.mark.parametrize(
    ("surface", "event_type"),
    [
        ("bootstrap", "bootstrap"),
        ("health_check", "health"),
        ("graceful_shutdown", "shutdown"),
        ("launch_checklist", "launch"),
    ],
)
def test_c5_event_surfaces_failure_deletes_event(
    surface: str, event_type: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    life = SystemLifecycle()
    before = _count(life, SystemEventModel, event_type=event_type)
    _break_commit(monkeypatch)
    with pytest.raises(Exception, match=BROKEN):
        getattr(life, surface)()
    assert _count(life, SystemEventModel, event_type=event_type) == before


def test_c5_self_heal_failure_resuspends_healed_states(
    runtime: StateRuntime, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _seed(runtime, status="suspended")
    second = _seed(runtime, status="suspended")
    life = SystemLifecycle(state_runtime=runtime)
    monkeypatch.setattr(sl.PersistentAuditStore, "append", _boom)
    with pytest.raises(_compensated(), match="COMPENSATED"):
        life.self_heal("states")
    assert runtime.get_state(first)["status"] == "suspended"
    assert runtime.get_state(second)["status"] == "suspended"
