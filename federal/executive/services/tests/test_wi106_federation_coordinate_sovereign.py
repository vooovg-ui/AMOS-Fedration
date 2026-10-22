"""
WI-106 · F1 — أسطحُ `governance/federation.py` الخمسةَ عشرَ تعبرُ الحدَّ السياديَّ بفاعلٍ
تنفيذيٍّ مُعلَنٍ بالفعلِ `coordinate` (قرارُ المالكِ D17-1 · نصُّ Q-24: «تنسيق لا سلطة»).

الهدف: إثباتُ أنَّ كلَّ سطحٍ عامٍّ مُغيِّرٍ في الوحدةِ يعبرُ الحدَّ بالفعلِ نفسِه وبالفاعلِ
       الثابتِ في الوحدةِ، وأنَّ الكتابةَ كلَّها خلفَ الحدِّ (لا صفَّ يُكتَبُ إن رُفِضَ)،
       وأنَّ المُعوِّضَ يستعيدُ الحالةَ كما كانت، وأنَّ الإعادةَ على مفتاحٍ طبيعيٍّ تُرفَعُ صريحةً.
النطاق: قياسُ سلوكِ الوحدةِ عبرَ الحدِّ وحدَه — لا تعديلَ للبوابةِ ولا للقواعدِ ولا لـ
        `test_federation.py` (بلا تعديلٍ).
المالك: federal/executive/services — WI-106 (تصميمُ docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md
        المُلتزَمُ قبلَ الشِّفرةِ في W-615).
تاريخ الإنشاء: 2026-10-22 (WI-106 · الدفعةُ F1)

الفحوصُ كما وردتْ في التصميمِ (§ 4) — T1–T8:
- T1 · العبورُ: الأسطحُ الخمسةَ عشرَ كلُّها ⇒ 15 عمليّةً متمايزةً بالفعلِ `coordinate` وALLOW.
- T2 · الفاعلُ مُعلَنٌ لا مُثبَّتٌ: `FEDERATION_ACTOR="JUDICIAL"` ⇒ رفضٌ ولا صفَّ.
- T3 · لا كتابةَ خارجَ المُطبِّقِ: الرفضُ لكلِّ سطحٍ ⇒ الصفوفُ والأعمدةُ كما كانت.
- T4 · المُعوِّضُ على الإنشاءِ (`propose`) · T5 · على التحديثِ (`vote`).
- T6 · الإعادةُ الطبيعيّةُ (`enact` الثاني) ⇒ `FederationReplayError` بلا كتابةٍ ثانيةٍ.
- T7 · الجردُ: 15 عامًّا في الوحدةِ كلُّها عابرةٌ · T8 · الثابتانِ.

الحدُّ المُعلَنُ: لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذِ (§ 4.3) — ملفُّ قياسٍ لا حُكمِ مراجعةٍ.

الدليلُ المُعادُ تشغيلُه (من federal/executive/services):
    ../../../.venv/bin/python -m pytest tests/test_wi106_federation_coordinate_sovereign.py -q
"""

from __future__ import annotations

import importlib.util
import math
import sys
import time
from pathlib import Path
from typing import Any

import pytest
from sqlalchemy import create_engine, delete, select

from amos_federation.common.database import get_database_url, get_session_factory
from amos_federation.services.agent_runtime.population import get_population_registry
from amos_federation.services.governance import federation as federation_module
from amos_federation.services.governance.federation import (
    ApprovalModel,
    ApprovalSystem,
    ComplianceReportModel,
    CourtCaseModel,
    ExecutiveBranch,
    ExecutiveRoleModel,
    FederationReplayError,
    JudicialBranch,
    LegislationModel,
    LegislativeBranch,
    PromotionGateModel,
    PromotionSystem,
    SupremeOversight,
    _GovBase,
)

#: الأسطحُ الخمسةَ عشرَ المقيسةُ قبلَ الشِّفرةِ (evidence/W-615/federation_sites_before.txt).
EXPECTED_OPERATIONS = frozenset(
    {
        "ApprovalSystem.request_approval",
        "ApprovalSystem.decide_approval",
        "PromotionSystem.start_promotion",
        "PromotionSystem.pass_gate",
        "PromotionSystem.fail_gate",
        "ExecutiveBranch.appoint",
        "LegislativeBranch.propose",
        "LegislativeBranch.open_debate",
        "LegislativeBranch.open_voting",
        "LegislativeBranch.vote",
        "LegislativeBranch.enact",
        "JudicialBranch.file_case",
        "JudicialBranch.add_argument",
        "JudicialBranch.rule",
        "SupremeOversight.generate_compliance_report",
    }
)

_MODELS = (
    ApprovalModel,
    PromotionGateModel,
    LegislationModel,
    CourtCaseModel,
    ComplianceReportModel,
)


@pytest.fixture(autouse=True)
def clean_federation() -> Any:
    """جداولُ الوحدةِ نظيفةٌ قبلَ كلِّ فحصٍ وبعدَه · والمُفوِّضُ المحفوظُ مُفرَغٌ (D1)."""
    url = get_database_url()
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    _GovBase.metadata.create_all(create_engine(url, connect_args=connect_args))
    get_population_registry().seed_initial_population()
    federation_module.reset_federation_authorizer()
    yield
    session = get_session_factory()()
    try:
        for model in _MODELS:
            session.execute(delete(model))
        for role in session.execute(select(ExecutiveRoleModel)).scalars().all():
            role.agent_id = None
            role.status = "vacant"
            role.appointed_at = None
        session.commit()
    finally:
        session.close()
    federation_module.reset_federation_authorizer()


class RecordingFederationAuthorizer(federation_module.ConstitutionalAuthorizer):
    """يسجّلُ كلَّ عبورٍ (اسمَ العمليّةِ والدليلَ) — لقياسِ العبورِ لا لاتخاذِ قرارٍ."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.crossings: list[tuple[str, Any]] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.crossings.append(((kwargs.get("metadata") or {}).get("operation", ""), guarded))
        return guarded


def _install_recording_authorizer() -> RecordingFederationAuthorizer:
    """مُصرِّحٌ مسجِّلٌ بثابتِ الوحدةِ نفسِه — المسارُ الإنتاجيُّ كما هو (D1)."""
    authorizer = RecordingFederationAuthorizer(actor=federation_module.FEDERATION_ACTOR)
    federation_module._DEFAULT_FEDERATION_AUTHORIZER = authorizer
    return authorizer


def _agent_id(index: int = 0) -> str:
    return get_population_registry().list_agents()[index]["agent_id"]


def _keys() -> tuple[str, str]:
    return ApprovalSystem().signer.generate_keypair()


def _legislation(leg_id: str) -> LegislationModel:
    session = get_session_factory()()
    try:
        row = session.get(LegislationModel, leg_id)
        assert row is not None
        session.expunge(row)
        return row
    finally:
        session.close()


def _count(model: type) -> int:
    session = get_session_factory()()
    try:
        return len(session.execute(select(model)).scalars().all())
    finally:
        session.close()


def _snapshot() -> dict[str, list[tuple[Any, ...]]]:
    """لقطةُ كلِّ صفوفِ الوحدةِ بأعمدتِها — للمقارنةِ قبلَ الرفضِ وبعدَه (T3)."""
    session = get_session_factory()()
    try:
        out: dict[str, list[tuple[Any, ...]]] = {}
        for model in (*_MODELS, ExecutiveRoleModel):
            columns = [c.key for c in model.__table__.columns]
            rows = session.execute(select(model)).scalars().all()
            out[model.__name__] = sorted(
                (tuple(repr(getattr(r, c)) for c in columns) for r in rows), key=repr
            )
        return out
    finally:
        session.close()


def _drop_settle(monkeypatch: pytest.MonkeyPatch, ledger: Any, label: str) -> Any:
    """إسقاطُ تثبيتِ النجاحِ بعدَ التزامِ المُطبِّقِ — يُرجِعُ الأصلَ لرفعِ الإسقاط."""
    original = type(ledger).mark_succeeded

    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError(f"تثبيتُ النجاحِ مُسقَطٌ — {label}")

    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)
    return original


def _next_second() -> None:
    """معرِّفُ الإذنِ `EP-<العقد>-<الثانية>` (سابقةُ W-603): الإعادةُ تعبرُ إلى الثانيةِ التاليةِ."""
    now = time.time()
    time.sleep(math.ceil(now) - now + 0.05)


def _voting_legislation(title: str) -> str:
    branch = LegislativeBranch()
    leg_id = branch.propose(title, "نصُّ الفحصِ", "tester")["legislation_id"]
    branch.open_debate(leg_id)
    branch.open_voting(leg_id)
    return leg_id


def _exercise_all_surfaces() -> None:
    """استدعاءُ الأسطحِ الخمسةَ عشرَ كلِّها مرّةً على الأقلِّ — بالواجهةِ العامّةِ كما هي."""
    priv, pub = _keys()
    approvals = ApprovalSystem()
    approval = approvals.request_approval("policy_change", "t1", "tester", priv, pub)
    approvals.decide_approval(approval["approval_id"], "approve", priv, pub)

    promotions = PromotionSystem()
    promotions.start_promotion("model", "t1-model", "tester")
    promotions.pass_gate("model", "t1-model", "evaluation", {"score": 0.9})
    promotions.fail_gate("model", "t1-model", "shadow", "فحصٌ")

    ExecutiveBranch().appoint("coordinator", _agent_id())

    legislative = LegislativeBranch()
    leg_id = _voting_legislation("قانونُ T1")
    legislative.vote(leg_id, _agent_id(0), "for")
    legislative.enact(leg_id)

    judicial = JudicialBranch()
    case_id = judicial.file_case("a", "b", "موضوعُ الفحصِ")["case_id"]
    judicial.add_argument(case_id, "حجّةٌ", "a")
    judicial.rule(case_id, "حكمُ تنسيقٍ", "judge")

    SupremeOversight().generate_compliance_report("2026-10")


# ── T1 · العبورُ: خمسَ عشرةَ عمليّةً بالفعلِ coordinate ─────────────────────────


def test_wi106_t1_every_surface_crosses_as_coordinate() -> None:
    authorizer = _install_recording_authorizer()
    _exercise_all_surfaces()

    operations = {name for name, _ in authorizer.crossings}
    assert operations == EXPECTED_OPERATIONS
    for name, guarded in authorizer.crossings:
        evidence = guarded.evidence.as_dict()
        assert evidence["action"] == "coordinate", name
        assert evidence["decision"] == "ALLOW", name
        assert evidence["target"].startswith("federation/"), name
    record = authorizer.gateway.records[-1]
    assert record.action == "coordinate"
    assert record.actor == "executive"


# ── T2 · الفاعلُ ثابتُ الوحدةِ — تبديلُه يُسقِطُ العبورَ ───────────────────────


def test_wi106_t2_judicial_actor_is_denied_and_nothing_is_written(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation  # يُتاحُ أوّلًا (الجسرُ)

    monkeypatch.setattr(federation_module, "FEDERATION_ACTOR", "JUDICIAL")
    federation_module.reset_federation_authorizer()
    priv, pub = _keys()

    with pytest.raises(SovereigntyViolation):
        LegislativeBranch().propose("مرفوضٌ", "نصٌّ", "tester")
    with pytest.raises(SovereigntyViolation):
        ApprovalSystem().request_approval("policy_change", "t2", "tester", priv, pub)

    assert _count(LegislationModel) == 0
    assert _count(ApprovalModel) == 0


# ── T3 · لا كتابةَ خارجَ المُطبِّقِ — لكلِّ سطحٍ ───────────────────────────────


def test_wi106_t3_denied_crossing_leaves_every_surface_untouched(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    # التحضيرُ بالفاعلِ الصحيحِ: كيانٌ قائمٌ لكلِّ سطحِ تحديثٍ
    priv, pub = _keys()
    approval_id = ApprovalSystem().request_approval("policy_change", "t3", "tester", priv, pub)[
        "approval_id"
    ]
    PromotionSystem().start_promotion("model", "t3-model", "tester")
    leg_debate = LegislativeBranch().propose("قانونُ T3", "نصٌّ", "tester")["legislation_id"]
    leg_vote = _voting_legislation("قانونُ T3-ب")
    case_id = JudicialBranch().file_case("a", "b", "موضوعٌ")["case_id"]
    agent = _agent_id()
    before = _snapshot()

    monkeypatch.setattr(federation_module, "FEDERATION_ACTOR", "JUDICIAL")
    federation_module.reset_federation_authorizer()

    calls = [
        lambda: ApprovalSystem().request_approval("policy_change", "x", "tester", priv, pub),
        lambda: ApprovalSystem().decide_approval(approval_id, "approve", priv, pub),
        lambda: PromotionSystem().start_promotion("model", "t3-other", "tester"),
        lambda: PromotionSystem().pass_gate("model", "t3-model", "evaluation", {}),
        lambda: PromotionSystem().fail_gate("model", "t3-model", "evaluation", "x"),
        lambda: ExecutiveBranch().appoint("coordinator", agent),
        lambda: LegislativeBranch().propose("x", "y", "z"),
        lambda: LegislativeBranch().open_debate(leg_debate),
        lambda: LegislativeBranch().open_voting(leg_debate),
        lambda: LegislativeBranch().vote(leg_vote, agent, "for"),
        lambda: LegislativeBranch().enact(leg_vote),
        lambda: JudicialBranch().file_case("p", "d", "s"),
        lambda: JudicialBranch().add_argument(case_id, "x", "p"),
        lambda: JudicialBranch().rule(case_id, "x", "j"),
        lambda: SupremeOversight().generate_compliance_report("2026-10"),
    ]
    assert len(calls) == len(EXPECTED_OPERATIONS)
    for call in calls:
        with pytest.raises(SovereigntyViolation):
            call()

    assert _snapshot() == before


# ── T4 · المُعوِّضُ على الإنشاءِ ─────────────────────────────────────────────


def test_wi106_t4_compensator_removes_created_row(monkeypatch: pytest.MonkeyPatch) -> None:
    from core.sovereignty.compensation import CompensationRequired

    ledger = federation_module._federation_authorizer().boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T4")
    with pytest.raises(CompensationRequired) as caught:
        LegislativeBranch().propose("قانونُ T4", "نصٌّ", "tester")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    assert caught.value.outcome.state_is_clean is True
    assert caught.value.outcome.requires_human is False
    assert _count(LegislationModel) == 0

    LegislativeBranch().propose("قانونُ T4", "نصٌّ", "tester")
    assert _count(LegislationModel) == 1


# ── T5 · المُعوِّضُ على التحديثِ ─────────────────────────────────────────────


def test_wi106_t5_compensator_restores_vote_counters(monkeypatch: pytest.MonkeyPatch) -> None:
    from core.sovereignty.compensation import CompensationRequired
    from core.sovereignty.idempotency import IdempotencyKey, OperationStatus

    leg_id = _voting_legislation("قانونُ T5")
    agent = _agent_id()
    ledger = federation_module._federation_authorizer().boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T5")
    with pytest.raises(CompensationRequired) as caught:
        LegislativeBranch().vote(leg_id, agent, "for")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    assert caught.value.outcome.state_is_clean is True
    row = _legislation(leg_id)
    assert (row.votes_for, row.votes_against, row.votes_abstain) == (0, 0, 0)
    assert list(row.voters or []) == []
    record = ledger.get(
        IdempotencyKey(
            scope="federation.LegislativeBranch.vote",
            value=f"legislations/{leg_id}/votes/{agent}",
        )
    )
    assert record is not None and record.status is OperationStatus.FAILED_RETRYABLE

    _next_second()
    LegislativeBranch().vote(leg_id, agent, "for")
    row = _legislation(leg_id)
    assert row.votes_for == 1
    assert list(row.voters) == [agent]


# ── T6 · الإعادةُ الطبيعيّةُ مرفوعةٌ صريحةً ─────────────────────────────────


def test_wi106_t6_second_enact_is_refused_without_second_write() -> None:
    leg_id = _voting_legislation("قانونُ T6")
    branch = LegislativeBranch()
    branch.vote(leg_id, _agent_id(), "for")
    first = branch.enact(leg_id)
    assert first["status"] == "enacted"
    updated_before = _legislation(leg_id).updated_at

    _next_second()
    with pytest.raises(FederationReplayError):
        branch.enact(leg_id)
    after = _legislation(leg_id)
    assert after.status == "enacted"
    assert after.updated_at == updated_before


# ── T7 · الجردُ: الوحدةُ بلا دَينٍ ────────────────────────────────────────────


def _repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "audit" / "sovereign_write_inventory.py").is_file():
            return parent
    raise AssertionError("جذرُ المستودعِ غيرُ موجود")


def test_wi106_t7_inventory_counts_fifteen_guarded_and_zero_debt() -> None:
    root = _repo_root()
    tool = root / "tools" / "audit" / "sovereign_write_inventory.py"
    spec = importlib.util.spec_from_file_location("_wi106_inventory", tool)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    sites = [s for s in module.collect(root) if s.path.endswith("governance/federation.py")]
    public = [s for s in sites if s.public]
    assert {f"{s.owner}.{s.function}" for s in public} == EXPECTED_OPERATIONS
    assert all(s.guarded for s in public), [s.function for s in public if not s.guarded]


# ── T8 · الثابتانِ (D1 · D2) ──────────────────────────────────────────────────


def test_wi106_t8_actor_and_verb_constants() -> None:
    assert federation_module.FEDERATION_ACTOR == "EXECUTIVE"
    assert federation_module.FEDERATION_VERB == "coordinate"
    assert federation_module._federation_authorizer()._actor == "EXECUTIVE"
