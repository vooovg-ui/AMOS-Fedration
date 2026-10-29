"""W-724 · G1 الدفعة 3 — عبورُ ستّةِ أسطحٍ من expansion الحدَّ السياديّ.

الهدف: إثباتُ أنَّ take_exam · submit_output · approve_output · employ_batch · graduate_batch ·
       retire_agent تعبرُ الحدَّ بأفعالِ جدولِ G1 § 2.2 (تصميمُ § 9.9.4)، وأنَّ الرفضَ قبلَ أيِّ
       كتابةٍ (ولا عبورَ داخليًّا قبلَه في الأسطحِ المركّبة)، وأنَّ الإعادةَ لا تُكرِّر، وأنَّ
       المعوِّضَ عكسٌ حقيقيٌّ — ومنه إعادةُ الوكيلِ إلى حالتِه في retire_agent (Q-26 · § 9.9.5).
النطاق: سلوكُ الأسطحِ الستّة وحدَه. create_batch وenroll_batch لا يُعبَرانِ (Q-77 · § 9.9.2).
        حقنُ مستوى القاطعِ في الطلبِ محاكاةٌ لحالتِه معلَنةٌ هنا (نمطُ WI-082 · E1)، لأنَّ الجسرَ
        لا يحقنُه في الإنتاج (DISC-099/WI-085) — فهذه الفحوصُ لا تُثبِتُ منعًا في الإنتاج.
المالك: federal/executive/services — WI-120 (G1 · تصميمُ W-724 § 9.9).
تاريخ الإنشاء: 2026-10-29 (W-724)

أصنافُ الفحصِ الخمسةُ (G1 § 4): 1 الرفضُ قبلَ الكتابة · 2 النجاحُ عبرَ الحدّ ·
3 طفرةٌ لكلِّ سطح · 4 الإعادةُ لا تُكرِّر · 5 المعوِّضُ على المسارِ الحقيقيّ.

الدليلُ المُعادُ تشغيلُه (من federal/executive/services):
    ../../../.venv/bin/python -m pytest tests/test_w724_g1_expansion.py -q
"""

from __future__ import annotations

import ast
import dataclasses
import inspect
import textwrap
import uuid
from typing import Any

import pytest

from amos_federation.services.agent_runtime.population import get_population_registry
from amos_federation.services.executive_core.agent_identity import get_identity
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from amos_federation.services.governance import expansion as ex
from amos_federation.services.governance.expansion import (
    ExpansionBatchModel,
    PopulationExpansion,
    RetirementRecordModel,
    RetirementSystem,
    SpecializationProgram,
    SpecializationResultModel,
    University,
    UniversityOutputModel,
)


# ── مُصرِّحاتُ القياس ─────────────────────────────────────────────────────────
class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجِّلُ كلَّ نتيجةٍ محروسةٍ وكلَّ طلبِ إذن — للقياسِ لا للقرار (نمطُ WI-082)."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []
        self.permits: list[str] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.results.append(guarded)
        return guarded

    def request_permit(self, action: str, *args: Any, **kwargs: Any) -> Any:
        permit = super().request_permit(action, *args, **kwargs)
        self.permits.append(action)
        return permit


class KillSwitchAuthorizer(RecordingAuthorizer):
    """الطلبُ يحملُ مستوى القاطع — محاكاةُ حالتِه لا تجاوزٌ (نمطُ WI-082 · E1)."""

    def __init__(self, level: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._level = level

    def _request(
        self,
        action: str,
        target: str,
        metadata: dict[str, Any] | None = None,
        human_approval: Any = None,
    ) -> Any:
        request = super()._request(action, target, metadata, human_approval)
        return dataclasses.replace(request, kill_switch_level=self._level)


def _violation() -> type[Exception]:
    from core.sovereignty.gateway import SovereigntyViolation

    return SovereigntyViolation


def _evidence(r: RecordingAuthorizer) -> dict[str, Any]:
    assert r.results, "لم يُعبَرِ الحدُّ السياديُّ أصلًا"
    return dict(r.results[-1].evidence.as_dict())


def _count(owner: Any, model: Any, **filters: Any) -> int:
    session = owner._Session()
    try:
        q = session.query(model)
        for key, value in filters.items():
            q = q.filter(getattr(model, key) == value)
        return int(q.count())
    finally:
        session.close()


# ── تجهيزات ──────────────────────────────────────────────────────────────────
@pytest.fixture
def rec() -> RecordingAuthorizer:
    return RecordingAuthorizer()


def _seed_agent(state: str | None = None, category: str = "reserve") -> str:
    """وكيلٌ للفحصِ عبرَ `register_agent` المحروس — تجهيزٌ لا سطحٌ مَقيس."""
    registry = get_population_registry()
    agent_id = f"w724-{uuid.uuid4().hex[:8]}"
    registry.register_agent(
        name=agent_id, role="reserve", category=category, permissions=[], agent_id=agent_id
    )
    if state is not None:
        registry.update_state(agent_id, state)
    return agent_id


def _seed_batch(owner: PopulationExpansion, category: str = "reserve") -> str:
    """صفُّ دفعةٍ بجلسةٍ مباشرة — create_batch غيرُ معبَّرٍ (Q-77) فلا يُستعمَلُ تجهيزًا."""
    batch_id = f"w724-batch-{uuid.uuid4().hex[:6]}"
    session = owner._Session()
    try:
        session.add(ExpansionBatchModel(batch_id=batch_id, category=category, target_count=1))
        session.commit()
    finally:
        session.close()
    return batch_id


def _batch(owner: PopulationExpansion, batch_id: str) -> ExpansionBatchModel:
    session = owner._Session()
    try:
        return session.query(ExpansionBatchModel).filter_by(batch_id=batch_id).one()
    finally:
        session.close()


def _submit(uni: University, **kw: Any) -> dict[str, Any]:
    return uni.submit_output("paper", "عنوان", "w724-author", "science", "محتوى", **kw)


def _states(agent_id: str) -> tuple[str, str | None]:
    """(المرآة، الكانون) — الحالتانِ اللتانِ يجبُ أن يُعيدَهما معوِّضُ retire_agent."""
    mirror = get_population_registry().get_agent(agent_id)["state"]
    identity = get_identity(agent_id)
    return mirror, identity.lifecycle_state if identity is not None else None


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 1 — الرفضُ قبلَ الكتابة (مستوى القاطعِ محقونٌ في الطلب)
# ═════════════════════════════════════════════════════════════════════════════
def test_c1_take_exam_blocked_at_level1_no_row() -> None:
    sp = SpecializationProgram(authorizer=KillSwitchAuthorizer(1))
    with pytest.raises(_violation()):
        sp.take_exam("w724-ag", "finance", 90.0, operation_id="exam-c1")
    assert _count(sp, SpecializationResultModel, agent_id="w724-ag") == 0


@pytest.mark.parametrize(("level", "blocked"), [(3, False), (4, True), (5, True)])
def test_c1_submit_output_blocked_from_level4(level: int, blocked: bool) -> None:
    uni = University(authorizer=KillSwitchAuthorizer(level))
    op = f"uni-c1-{level}-{uuid.uuid4().hex[:4]}"
    if blocked:
        with pytest.raises(_violation()):
            _submit(uni, operation_id=op)
    else:
        _submit(uni, operation_id=op)
    assert _count(uni, UniversityOutputModel, output_id=op) == (0 if blocked else 1)


def test_c1_approve_output_blocked_at_level4_unchanged() -> None:
    out = _submit(University())
    uni = University(authorizer=KillSwitchAuthorizer(4))
    with pytest.raises(_violation()):
        uni.approve_output(out["output_id"], 0.9)
    assert uni._output_snapshot(out["output_id"]) == (False, 0.0)


def test_c1_employ_blocked_at_level3_before_any_inner_crossing() -> None:
    """الرفضُ بالتحقّقِ المسبق: لا فحصَ صحّيًّا ولا تحديثَ حالةٍ ولا عبورَ داخليّ (§ 9.9.4 (1))."""
    agent_id = _seed_agent("employed")
    ks = KillSwitchAuthorizer(3)
    pe = PopulationExpansion(authorizer=ks)
    batch_id = _seed_batch(pe)
    with pytest.raises(_violation()):
        pe.employ_batch(batch_id)
    assert ks.results == []
    assert _batch(pe, batch_id).employed == 0
    assert get_population_registry().get_agent(agent_id)["state"] == "employed"


def test_c1_graduate_not_blocked_at_level5_q78_measured() -> None:
    """Q-78: `release_agent` خارجَ KILL_SWITCH_BLOCKS — المقيسُ يُثبَّتُ ويُرفَعُ للمالك."""
    _seed_agent()
    ks = KillSwitchAuthorizer(5)
    pe = PopulationExpansion(authorizer=ks)
    out = pe.graduate_batch(_seed_batch(pe))
    assert "error" not in out
    assert _evidence(ks)["action"] == "release_agent"


def test_c1_retire_is_containment_crosses_at_level2_and_writes_record() -> None:
    """`contain_agent` لا يُمنَع؛ والمستوى 2 لأنَّ `update_population_state` الداخليَّ يُمنَعُ عندَ ≥3."""
    agent_id = _seed_agent("employed")
    ks = KillSwitchAuthorizer(2)
    rs = RetirementSystem(authorizer=ks)
    rs.retire_agent(agent_id)
    assert _evidence(ks)["action"] == "contain_agent"
    assert _count(rs, RetirementRecordModel, agent_id=agent_id) == 1


def test_c1_retire_inner_denial_at_level3_leaves_no_record_and_no_transition() -> None:
    """المقيس: عندَ ≥3 يرفضُ العبورُ الداخليُّ للمرآةِ فلا سجلَّ ولا انتقالَ يبقى قائمًا."""
    agent_id = _seed_agent("employed")
    before = _states(agent_id)
    rs = RetirementSystem(authorizer=KillSwitchAuthorizer(3))
    with pytest.raises(_violation()):
        rs.retire_agent(agent_id)
    assert _count(rs, RetirementRecordModel, agent_id=agent_id) == 0
    assert _states(agent_id) == before


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 2 — النجاحُ عبرَ الحدِّ بالفعلِ المسمّى
# ═════════════════════════════════════════════════════════════════════════════
SURFACES = [
    (SpecializationProgram, "take_exam", "record_curriculum_step", "ACTION_TAKE_EXAM"),
    (University, "submit_output", "create_task", "ACTION_SUBMIT_OUTPUT"),
    (University, "approve_output", "activate_agent", "ACTION_APPROVE_OUTPUT"),
    (PopulationExpansion, "employ_batch", "dispatch_agent", "ACTION_EMPLOY_BATCH"),
    (PopulationExpansion, "graduate_batch", "release_agent", "ACTION_GRADUATE_BATCH"),
    (RetirementSystem, "retire_agent", "contain_agent", "ACTION_RETIRE_AGENT"),
]


def _call_surface(name: str, rec: RecordingAuthorizer) -> None:
    if name == "take_exam":
        SpecializationProgram(authorizer=rec).take_exam("w724-ag", "finance", 90.0)
    elif name == "submit_output":
        _submit(University(authorizer=rec))
    elif name == "approve_output":
        out = _submit(University())
        University(authorizer=rec).approve_output(out["output_id"], 0.9)
    elif name == "employ_batch":
        _seed_agent("employed")
        pe = PopulationExpansion(authorizer=rec)
        pe.employ_batch(_seed_batch(pe))
    elif name == "graduate_batch":
        _seed_agent()
        pe = PopulationExpansion(authorizer=rec)
        pe.graduate_batch(_seed_batch(pe))
    elif name == "retire_agent":
        RetirementSystem(authorizer=rec).retire_agent(_seed_agent("employed"))
    else:  # pragma: no cover
        raise AssertionError(name)


@pytest.mark.parametrize(("owner", "surface", "action", "const"), SURFACES)
def test_c2_surface_crosses_with_named_action(
    owner: type, surface: str, action: str, const: str, rec: RecordingAuthorizer
) -> None:
    _call_surface(surface, rec)
    evidence = _evidence(rec)
    assert evidence["action"] == action
    assert evidence["decision"] == "ALLOW"


@pytest.mark.parametrize(
    "surface", ["employ_batch", "graduate_batch", "retire_agent"], ids=lambda s: s
)
def test_c2_composite_permit_precedes_and_surface_crossing_is_last(
    surface: str, rec: RecordingAuthorizer
) -> None:
    """التحقّقُ المسبقُ على فعلِ السطحِ أوّلًا، وعبورُ السطحِ نفسِه آخرًا (§ 9.9.4 (1)–(3))."""
    action = {s: a for _o, s, a, _c in SURFACES}[surface]
    _call_surface(surface, rec)
    assert rec.permits and rec.permits[0] == action
    assert _evidence(rec)["action"] == action


def test_c2_employ_activates_through_inner_crossings(
    rec: RecordingAuthorizer, monkeypatch: pytest.MonkeyPatch
) -> None:
    """الفحصُ الصحّيُّ يعبرُ حقًّا، ونتيجتُه تُقرَأُ «سليمًا» — وكيلٌ جديدٌ بلا خبراتٍ يُقاسُ
    «monitor» فلا يُوظَّف؛ فالتجاوزُ هنا لقيمةِ الحالةِ المُعادةِ وحدَها لا للعبور."""
    from amos_federation.services.agent_runtime.health import HealthChecker

    original = HealthChecker.check_agent

    def _healthy(self: Any, *args: Any, **kwargs: Any) -> dict[str, Any]:
        return {**original(self, *args, **kwargs), "status": "healthy"}

    monkeypatch.setattr(HealthChecker, "check_agent", _healthy)
    agent_id = _seed_agent("employed")
    pe = PopulationExpansion(authorizer=rec)
    batch_id = _seed_batch(pe)
    out = pe.employ_batch(batch_id)
    assert out["employed"] >= 1 and _batch(pe, batch_id).employed == out["employed"]
    assert get_population_registry().get_agent(agent_id)["state"] == "active"
    actions = [r.evidence.as_dict()["action"] for r in rec.results]
    assert "run_health_check" in actions and actions[-1] == "dispatch_agent"


def test_c2_retire_moves_mirror_and_canonical(rec: RecordingAuthorizer) -> None:
    agent_id = _seed_agent("employed")
    RetirementSystem(authorizer=rec).retire_agent(agent_id)
    mirror, canonical = _states(agent_id)
    assert mirror == "retired" and canonical == "retired"


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 3 — طفرةٌ لكلِّ سطح (والحملةُ السلوكيّةُ في evidence/W-724/mutation_results.json)
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.parametrize(("owner", "surface", "action", "const"), SURFACES)
def test_c3_mutation_guard_call_literally_in_public_body(
    owner: type, surface: str, action: str, const: str
) -> None:
    """نداءُ `guard_declared` بثابتِ الفعلِ في جسدِ السطحِ نفسِه — واحدٌ لا أكثر."""
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
    assert getattr(ex, const) == action


def test_c3_create_and_enroll_batch_untouched_q77() -> None:
    """create_batch وenroll_batch دَينٌ معلَّقٌ بـQ-77 — لم يُمَسّا ولم يُنزَلا إلى فعلٍ أخفّ."""
    for name in ("create_batch", "enroll_batch"):
        src = inspect.getsource(getattr(PopulationExpansion, name))
        assert "guard_declared" not in src and "request_permit" not in src, name


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 4 — الإعادةُ لا تُكرِّرُ الأثر
# ═════════════════════════════════════════════════════════════════════════════
def test_c4_take_exam_replay_one_row(rec: RecordingAuthorizer) -> None:
    sp = SpecializationProgram(authorizer=rec)
    sp.take_exam("w724-r", "law", 90.0, operation_id="exam-r")
    out = sp.take_exam("w724-r", "law", 90.0, operation_id="exam-r")
    assert out.get("replayed") is True and rec.results[-1].is_replay
    assert _count(sp, SpecializationResultModel, agent_id="w724-r") == 1


def test_c4_submit_replay_one_row(rec: RecordingAuthorizer) -> None:
    uni = University(authorizer=rec)
    _submit(uni, operation_id="uni-r")
    assert _submit(uni, operation_id="uni-r").get("replayed") is True
    assert _count(uni, UniversityOutputModel, output_id="uni-r") == 1


def test_c4_approve_replay_no_second_write(rec: RecordingAuthorizer) -> None:
    out = _submit(University())
    uni = University(authorizer=rec)
    uni.approve_output(out["output_id"], 0.9, operation_id="ap-r")
    uni._set_output(out["output_id"], False, 0.0)  # تُعادُ اللقطةُ فيظهرُ أيُّ أثرٍ ثانٍ
    assert uni.approve_output(out["output_id"], 0.9, operation_id="ap-r").get("replayed") is True
    assert uni._output_snapshot(out["output_id"]) == (False, 0.0)


@pytest.mark.parametrize("surface", ["employ_batch", "graduate_batch"])
def test_c4_batch_replay_skips_inner_crossings(surface: str, rec: RecordingAuthorizer) -> None:
    """إعادةُ العمليّةِ المركّبةِ بمفتاحِها لا تُعيدُ العبوراتِ الداخليّة (قراءةُ السجلِّ قبلَ الحدّ)."""
    _seed_agent("employed" if surface == "employ_batch" else None)
    pe = PopulationExpansion(authorizer=rec)
    batch_id = _seed_batch(pe)
    getattr(pe, surface)(batch_id, operation_id="op-r")
    crossings = len(rec.results)
    assert getattr(pe, surface)(batch_id, operation_id="op-r").get("replayed") is True
    assert len(rec.results) == crossings


def test_c4_retire_replay_one_record(rec: RecordingAuthorizer) -> None:
    agent_id = _seed_agent("employed")
    rs = RetirementSystem(authorizer=rec)
    rs.retire_agent(agent_id, operation_id="ret-r")
    assert rs.retire_agent(agent_id, operation_id="ret-r").get("replayed") is True
    assert _count(rs, RetirementRecordModel, agent_id=agent_id) == 1


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 5 — المعوِّضُ على المسارِ الحقيقيّ
# ═════════════════════════════════════════════════════════════════════════════
BROKEN = "فشلٌ بعدَ الكتابة"


def _break_commit(monkeypatch: pytest.MonkeyPatch, scope: str) -> None:
    """انكسارُ مرحلةِ التثبيتِ لعبورِ السطحِ وحدَه (نطاقُ مفتاحِه) بعدَ عودةِ المُطبِّق.

    التقييدُ بالنطاقِ لازمٌ في الأسطحِ المركّبة: العبوراتُ الداخليّةُ (فحصُ الصحّة ·
    `update_state` · خطواتُ المنهج) تمرُّ، وينكسرُ عبورُ السطحِ نفسِه فيُشغِّلُ الحدُّ معوِّضَه.
    """
    ConstitutionalAuthorizer().review_only("run_health_check", "system:health")
    from core.sovereignty.idempotency import IdempotencyLedger

    original = IdempotencyLedger.mark_succeeded

    def _fail(self: Any, *args: Any, **kwargs: Any) -> Any:
        if kwargs["key"].scope == scope:
            raise RuntimeError("فشلٌ بعدَ الكتابة — انكسارُ مرحلةِ التثبيت")
        return original(self, *args, **kwargs)

    monkeypatch.setattr(IdempotencyLedger, "mark_succeeded", _fail)


def test_c5_take_exam_failure_deletes_row(monkeypatch: pytest.MonkeyPatch) -> None:
    sp = SpecializationProgram()
    _break_commit(monkeypatch, ex.EXAM_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        sp.take_exam("w724-c5", "finance", 90.0)
    assert _count(sp, SpecializationResultModel, agent_id="w724-c5") == 0


def test_c5_submit_failure_deletes_row(monkeypatch: pytest.MonkeyPatch) -> None:
    uni = University()
    _break_commit(monkeypatch, ex.OUTPUT_SUBMIT_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        _submit(uni, operation_id="uni-c5")
    assert _count(uni, UniversityOutputModel, output_id="uni-c5") == 0


def test_c5_approve_failure_restores_snapshot(monkeypatch: pytest.MonkeyPatch) -> None:
    uni = University()
    out = _submit(uni, quality_score=0.3)
    _break_commit(monkeypatch, ex.OUTPUT_APPROVE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        uni.approve_output(out["output_id"], 0.9)
    assert uni._output_snapshot(out["output_id"]) == (False, 0.3)


@pytest.mark.parametrize(
    ("surface", "scope", "column", "state"),
    [
        ("employ_batch", "expansion.batch.employ", "employed", "employed"),
        ("graduate_batch", "expansion.batch.graduate", "graduated", None),
    ],
)
def test_c5_batch_failure_restores_previous_count(
    surface: str, scope: str, column: str, state: str | None, monkeypatch: pytest.MonkeyPatch
) -> None:
    _seed_agent(state)
    pe = PopulationExpansion()
    batch_id = _seed_batch(pe)
    _break_commit(monkeypatch, scope)
    with pytest.raises(Exception, match=BROKEN):
        getattr(pe, surface)(batch_id)
    assert getattr(_batch(pe, batch_id), column) == 0


def test_c5_retire_failure_deletes_record_and_restores_agent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Q-26 · § 9.9.5: المعوِّضُ يحذفُ السجلَّ ويُعيدُ المرآةَ والكانونَ إلى ما كانا عليه."""
    agent_id = _seed_agent("employed")
    before = _states(agent_id)
    rs = RetirementSystem()
    _break_commit(monkeypatch, ex.RETIRE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        rs.retire_agent(agent_id)
    assert _count(rs, RetirementRecordModel, agent_id=agent_id) == 0
    assert _states(agent_id) == before and before[0] == "employed"


def test_c5_retire_in_applier_failure_surface_compensates_both(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """فشلٌ داخلَ المُطبِّقِ (الحدُّ لا يُشغِّلُ المعوِّض): السطحُ يُعيدُ الوكيلَ ثمَّ يرفع."""
    agent_id = _seed_agent("employed")
    before = _states(agent_id)

    class _Exploding:
        id = RetirementRecordModel.id
        agent_id = RetirementRecordModel.agent_id

        def __init__(self, **_kw: Any) -> None:
            raise RuntimeError("انكسارٌ داخلَ المُطبِّق")

    monkeypatch.setattr(ex, "RetirementRecordModel", _Exploding)
    with pytest.raises(Exception, match="انكسارٌ داخلَ المُطبِّق"):
        RetirementSystem().retire_agent(agent_id)
    monkeypatch.undo()
    assert _count(RetirementSystem(), RetirementRecordModel, agent_id=agent_id) == 0
    assert _states(agent_id) == before
