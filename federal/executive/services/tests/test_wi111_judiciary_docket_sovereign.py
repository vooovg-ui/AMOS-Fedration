"""
الهدف: إثباتُ الدفعةِ J2+J3 (WI-111) — الأسطحُ القضائيّةُ الخمسةَ عشرَ المحسومةُ تعبرُ
       الحدَّ بفاعلِ الوحدةِ القضائيِّ وبأفعالِ D17-2، ولا عبورَ داخلَ عبورٍ.
النطاق: `federal_judiciary/{service,docket,rulings}.py` ومعجمُ المُحرِّكِ وجدارُ الاختصاصِ —
        على ملحقِ التصميمِ `docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md` (T1–T8 · M1–M5).
المالك: federal/executive/services/tests
تاريخ الإنشاء: 2026-10-23
تاريخ آخر تعديل: 2026-10-23

لماذا
-----
D17-2 (خيارُ 1): «تُنفَّذ الأسطح الأخرى بالأفعال المعتمدة في D17-2». فكلُّ فعلٍ منَ العشرةِ
يُثبَتُ هنا حصرًا قضائيًّا في المُحرِّكِ (T1)، ويُثبَتُ عبورُه على المسارِ الإنتاجيِّ نفسِه
بالفعلِ المعتمدِ (T2) وبأثرٍ مُعلَنٍ ومُعوِّضٍ (T3)، ورفضُه لفاعلٍ تنفيذيٍّ منعًا حقيقيًّا (T2b)،
والإعادةُ بلا صفٍّ تفرُّقًا (T4)، والمُعوِّضُ استعادةً حقيقيّةً (T5)، والجردُ بلا دَينٍ في
الأسطحِ الخمسةَ عشرَ (T6)، و`issue_ruling` بلا عبورٍ متداخلٍ (T7).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

import tests.test_wi105_issue_ruling_sovereign as j1
from amos_federation.services.federal_judiciary import FederalJudiciary
from amos_federation.services.federal_judiciary import docket as docket_module
from amos_federation.services.federal_judiciary import rulings as rulings_module
from amos_federation.services.federal_judiciary.models import (
    CaseClaimModel,
    CaseEvidenceModel,
    CasePartyModel,
    CaseProceedingModel,
    CourtJudgeModel,
    LegalCaseModel,
)

if TYPE_CHECKING:
    from amos_federation.common.principal import AuthorizationContext
    from amos_federation.services.national_registry.service import NationalRegistry
    from amos_federation.services.state_registry.service import StateRegistry

# التجهيزاتُ نفسُها منَ J1 (لا نسخَ): السجلّاتُ والتاجُ.
registry = j1.registry
national = j1.national
judiciary = j1.judiciary
crown = j1.crown


@pytest.fixture(autouse=True)
def _fresh_state() -> None:
    """قاعدةٌ نظيفةٌ قبلَ كلِّ فحصٍ: أبناءُ القضيّةِ أوّلًا (مطالبةٌ · دليلٌ · طرفٌ) ثمَّ ترتيبُ J1.

    تجهيزُ J1 لا يحذفُ المطالباتِ والأدلّةَ والأطرافَ لأنَّ فحوصَه لا تُنشئُها؛ وهذه
    الفحوصُ تُنشئُها، فقيدُ المفتاحِ الأجنبيِّ يمنعُ حذفَ القضيّةِ قبلَها. والباقي حرفيًّا
    ترتيبُ `j1._fresh_state` بأسمائه في وحدتِه (لا نسخَ للنماذج).
    """
    j1.init_db()
    session = j1.get_session_factory()()
    try:
        session.query(CaseClaimModel).delete()
        session.query(CaseEvidenceModel).delete()
        session.query(CasePartyModel).delete()
        for model in (
            j1.RulingModel,
            CaseProceedingModel,
            LegalCaseModel,
            CourtJudgeModel,
            j1.CourtModel,
            j1.AuthorityGrantModel,
            j1.DecisionProvenanceModel,
            j1.LedgerEntryModel,
            j1.TransactionModel,
            j1.AllocationModel,
            j1.BudgetModel,
            j1.TreasuryAccountModel,
            j1.TreasuryModel,
            j1.OfficialPositionModel,
            j1.PositionModel,
            j1.IdentityAgentModel,
            j1.IdentityPrincipalModel,
            j1.IdentityModel,
        ):
            session.query(model).delete()
        j1.purge_tasks(session)
        j1.purge_agents(session)
        session.commit()
    finally:
        session.close()
    j1.reset_executive_core()
    j1.reset_state_registry()
    j1.reset_government_services()
    j1.reset_state_treasury()
    j1.reset_national_registry()
    j1.reset_federal_judiciary()
    rulings_module.reset_judiciary_authorizer()


#: الأفعالُ العشرةُ المضافةُ إلى معجمِ المُحرِّكِ (D17-2 · ملحقُ التصميمِ D2).
NEW_ENGINE_VERBS = (
    "refer_case",
    "admit_case",
    "vacate_ruling",
    "admit_evidence",
    "recuse_judge",
    "register_judgment",
    "assign_case",
    "record_proceeding",
    "join_party",
    "admit_claim",
)

#: الأسطحُ الخمسةَ عشرَ المحسومةُ (قيسَت عندَ 6f3fba2 · W-636).
SETTLED_SURFACES = {
    ("service.py", "vacate_ruling"),
    ("service.py", "file_case"),
    ("service.py", "open_case"),
    ("docket.py", "open_case"),
    ("service.py", "set_evidence_status"),
    ("service.py", "set_judge_status"),
    ("service.py", "close_case"),
    ("service.py", "assign_case"),
    ("service.py", "open_hearing"),
    ("service.py", "record_proceeding"),
    ("docket.py", "record_proceeding"),
    ("service.py", "add_party"),
    ("docket.py", "add_party"),
    ("service.py", "add_claim"),
    ("docket.py", "add_claim"),
}


class SpyingAuthorizer(rulings_module.ConstitutionalAuthorizer):
    """يسجّلُ كلَّ نداءٍ محروسٍ بمعاملاتِه وعمقِ تداخلِه — قياسٌ لا قرار."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.calls: list[dict[str, Any]] = []
        self.depth = 0
        self.max_depth = 0

    def guard_declared(self, action: str, target: str, **kwargs: Any) -> Any:
        self.depth += 1
        self.max_depth = max(self.max_depth, self.depth)
        try:
            guarded = super().guard_declared(action, target, **kwargs)
        finally:
            self.depth -= 1
        self.calls.append(
            {"action": action, "target": target, "kwargs": kwargs, "guarded": guarded}
        )
        return guarded

    def actions(self) -> list[str]:
        return [c["action"] for c in self.calls]


def _install_spy() -> SpyingAuthorizer:
    spy = SpyingAuthorizer(actor=rulings_module.JUDICIARY_ACTOR)
    rulings_module._DEFAULT_JUDICIARY_AUTHORIZER = spy
    return spy


def _world(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    username: str,
) -> tuple[Any, AuthorizationContext, AuthorizationContext, dict[str, Any]]:
    judge_ctx = j1._context("official", username=username)
    bench = j1._bench(registry, national, judiciary, crown, judge_ctx)
    filer = j1._context("official", username=f"filer-{username}")
    identity = j1._party_identity(national, crown, filer)
    return bench, judge_ctx, filer, identity


def _open(judiciary: FederalJudiciary, filer: AuthorizationContext, bench: Any) -> dict[str, Any]:
    return judiciary.open_case(
        context=filer,
        court_id=bench.court["id"],
        case_type="CIVIL",
        subject="نزاعٌ لفحصِ WI-111",
        reference=j1._code("W111"),
    )


# ── T1 · المعجمُ: الأفعالُ العشرةُ حصرٌ قضائيٌّ ─────────────────────────────────


@pytest.mark.parametrize("verb", NEW_ENGINE_VERBS)
def test_wi111_t1_engine_denies_non_judicial_and_allows_judicial(verb: str) -> None:
    from core.constitutional_engine.engine import ConstitutionalEngine
    from core.constitutional_engine.model import ActionRequest, Branch

    engine = ConstitutionalEngine()

    def decide(actor: str) -> tuple[str, list[str]]:
        verdict = engine.evaluate(
            ActionRequest(actor=Branch[actor], action=verb, target="wi111/probe")
        )
        decision = getattr(verdict, "decision", verdict)
        rules = [str(getattr(v, "rule_id", v)) for v in getattr(verdict, "violations", []) or []]
        return str(getattr(decision, "name", decision)), rules

    for actor in ("EXECUTIVE", "LEGISLATIVE"):
        decision, rules = decide(actor)
        assert decision == "DENY", (verb, actor, decision)
        assert "R-003-1" in rules, (verb, actor, rules)
    assert decide("JUDICIAL")[0] == "ALLOW"


def test_wi111_t1b_wall_knows_the_four_new_verbs_and_not_the_deferred() -> None:
    from core.constitutional_engine.rules import JUDICIAL_ACTIONS as ENGINE_VERBS
    from core.sovereignty.jurisdiction import JUDICIAL_ACTIONS as WALL_VERBS

    for verb in ("assign_case", "record_proceeding", "join_party", "admit_claim"):
        assert verb in WALL_VERBS
    for verb in NEW_ENGINE_VERBS:
        assert verb in ENGINE_VERBS
    # الأفعالُ الأربعةُ المؤجَّلةُ (D17-2 · D21-أ بند 9) غائبةٌ عمدًا منَ المعجمِ.
    for verb in ("establish_court", "set_court_status", "appoint_judge", "submit_evidence"):
        assert verb not in ENGINE_VERBS


# ── T2 · المسارُ الإنتاجيُّ: كلُّ سطحٍ يعبرُ بفعلِه المعتمدِ ─────────────────────


def _full_flow(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    username: str,
) -> dict[str, Any]:
    bench, judge_ctx, filer, identity = _world(registry, national, judiciary, crown, username)
    spy = _install_spy()
    case = _open(judiciary, filer, bench)
    party = judiciary.add_party(
        context=filer, case_id=case["id"], party_role="PLAINTIFF", identity_id=identity["id"]
    )
    judiciary.add_claim(
        context=filer,
        case_id=case["id"],
        claimant_party_id=party["id"],
        claim_type="DECLARATORY",
        statement="مطالبةُ فحصِ WI-111",
    )
    judiciary.record_proceeding(
        context=filer, case_id=case["id"], proceeding_type="MOTION", summary="طلبٌ إجرائيٌّ"
    )
    judiciary.file_case(context=filer, case_id=case["id"])
    judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
    judiciary.open_hearing(context=judge_ctx, case_id=case["id"])
    evidence = judiciary.submit_evidence(
        context=filer, case_id=case["id"], evidence_type="DOCUMENT", source="فحصُ WI-111"
    )
    judiciary.set_evidence_status(
        context=judge_ctx, evidence_id=evidence["id"], status="admitted", reason="مقبولٌ للفحص"
    )
    ruling = judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case["id"],
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ فحصِ WI-111",
    )
    judiciary.vacate_ruling(context=judge_ctx, ruling_id=ruling["id"], reason="إلغاءٌ للفحص")
    judiciary.close_case(context=judge_ctx, case_id=case["id"], reason="إغلاقٌ للفحص")
    judiciary.set_judge_status(
        context=crown, judge_id=bench.judge["id"], status="suspended", reason="تعليقٌ للفحص"
    )
    return {"spy": spy, "case": case, "bench": bench, "evidence": evidence}


def test_wi111_t2_production_path_crosses_with_d17_2_verbs(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    flow = _full_flow(registry, national, judiciary, crown, "t2")
    spy: SpyingAuthorizer = flow["spy"]
    assert spy.actions() == [
        "admit_case",
        "join_party",
        "admit_claim",
        "record_proceeding",
        "refer_case",
        "assign_case",
        "adjudicate",
        "admit_evidence",
        "issue_ruling",
        "vacate_ruling",
        "register_judgment",
        "recuse_judge",
    ]
    for call in spy.calls:
        evidence = call["guarded"].evidence.as_dict()
        assert evidence["decision"] == "ALLOW", call["action"]
        assert evidence["action"] == call["action"]
    records = [r for r in spy.gateway.records if r.action in set(spy.actions())]
    assert records and all(r.actor == "judicial" and r.decision == "ALLOW" for r in records)


@pytest.mark.parametrize("surface", ["open_case", "assign_case", "add_party"])
def test_wi111_t2b_executive_actor_is_denied_and_nothing_is_written(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
    surface: str,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    bench, _judge_ctx, filer, identity = _world(
        registry, national, judiciary, crown, f"t2b{surface}"
    )
    case = _open(judiciary, filer, bench)
    judiciary.file_case(context=filer, case_id=case["id"])
    monkeypatch.setattr(rulings_module, "JUDICIARY_ACTOR", "EXECUTIVE")
    rulings_module.reset_judiciary_authorizer()

    session = j1._session()
    try:
        cases_before = session.query(LegalCaseModel).count()
        parties_before = session.query(CasePartyModel).count()
    finally:
        session.close()

    with pytest.raises(SovereigntyViolation):
        if surface == "open_case":
            _open(judiciary, filer, bench)
        elif surface == "assign_case":
            judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
        else:
            judiciary.add_party(
                context=filer,
                case_id=case["id"],
                party_role="PLAINTIFF",
                identity_id=identity["id"],
            )

    session = j1._session()
    try:
        assert session.query(LegalCaseModel).count() == cases_before
        assert session.query(CasePartyModel).count() == parties_before
        row = session.get(LegalCaseModel, case["id"])
        assert row is not None and row.status == "filed" and row.assigned_judge_id is None
    finally:
        session.close()


# ── T3 · الأثرُ المُعلَنُ ونوعُه ومُعوِّضُه وطلبُ الاختصاصِ ─────────────────────────


def test_wi111_t3_each_crossing_declares_effect_compensator_and_jurisdiction(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    flow = _full_flow(registry, national, judiciary, crown, "t3")
    spy: SpyingAuthorizer = flow["spy"]
    creates = {"admit_case", "join_party", "admit_claim", "record_proceeding", "issue_ruling"}
    for call in spy.calls:
        kwargs = call["kwargs"]
        (effect,) = kwargs["declared_effects"]
        expected = "CREATE" if call["action"] in creates else "WRITE"
        assert effect.kind.name == expected, call["action"]
        assert len(kwargs["compensators"]) == 1, call["action"]
        request = kwargs["judicial_action"]
        assert request.action == call["action"]
        assert request.court_scope == flow["bench"].court["jurisdiction"]
        if call["action"] != "issue_ruling":  # J1 يجعلُ هدفَ طلبِه القضيّةَ (فحوصُه في wi105)
            assert request.target == call["target"]
        assert request.is_royal_decree_target is False


# ── T4 · الإعادةُ بلا صفٍّ تفرُّقٌ لا نجاحٌ ──────────────────────────────────────


def test_wi111_t4_replay_with_missing_case_raises_divergence(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    bench, _judge_ctx, filer, _identity = _world(registry, national, judiciary, crown, "t4")
    reference = j1._code("W111R")
    first = judiciary.open_case(
        context=filer,
        court_id=bench.court["id"],
        case_type="CIVIL",
        subject="فحص",
        reference=reference,
    )
    session = j1._session()
    try:
        row = session.get(LegalCaseModel, first["id"])
        assert row is not None
        session.delete(row)
        session.commit()
    finally:
        session.close()
    with pytest.raises(docket_module.JudicialLedgerDivergenceError):
        judiciary.open_case(
            context=filer,
            court_id=bench.court["id"],
            case_type="CIVIL",
            subject="فحص",
            reference=reference,
        )


# ── T5 · المُعوِّضُ على المسارِ الإنتاجيِّ: فشلُ التثبيتِ ⇒ استعادةٌ حقيقيّةٌ ──────────


def test_wi111_t5_failed_settle_restores_assignment_and_closure(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired

    bench, judge_ctx, filer, _identity = _world(registry, national, judiciary, crown, "t5")
    case = _open(judiciary, filer, bench)
    judiciary.file_case(context=filer, case_id=case["id"])
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger

    original = j1._drop_settle(monkeypatch, ledger, "WI-111 T5 assign")
    with pytest.raises(CompensationRequired) as caught:
        judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    assert caught.value.outcome.state_is_clean is True
    session = j1._session()
    try:
        row = session.get(LegalCaseModel, case["id"])
        assert row is not None and row.status == "filed" and row.assigned_judge_id is None
    finally:
        session.close()

    j1._next_second()
    judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
    judiciary.open_hearing(context=judge_ctx, case_id=case["id"])
    judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case["id"],
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ فحصِ WI-111 T5",
    )

    original = j1._drop_settle(monkeypatch, ledger, "WI-111 T5 close")
    with pytest.raises(CompensationRequired):
        judiciary.close_case(context=judge_ctx, case_id=case["id"], reason="إغلاقٌ للفحص")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    session = j1._session()
    try:
        row = session.get(LegalCaseModel, case["id"])
        assert row is not None and row.status == "decided" and row.closed_at is None
    finally:
        session.close()


def test_wi111_t5b_failed_settle_removes_inserted_party_and_proceeding(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired

    bench, _judge_ctx, filer, identity = _world(registry, national, judiciary, crown, "t5b")
    case = _open(judiciary, filer, bench)
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger

    original = j1._drop_settle(monkeypatch, ledger, "WI-111 T5b party")
    with pytest.raises(CompensationRequired):
        judiciary.add_party(
            context=filer, case_id=case["id"], party_role="PLAINTIFF", identity_id=identity["id"]
        )
    with pytest.raises(CompensationRequired):
        judiciary.file_case(context=filer, case_id=case["id"])
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    session = j1._session()
    try:
        assert (
            session.query(CasePartyModel).filter(CasePartyModel.case_id == case["id"]).count() == 0
        )
        assert (
            session.query(CaseProceedingModel)
            .filter(CaseProceedingModel.case_id == case["id"])
            .count()
            == 0
        )
        row = session.get(LegalCaseModel, case["id"])
        assert row is not None and row.status == "opened"
    finally:
        session.close()


# ── T6 · الجردُ: الأسطحُ الخمسةَ عشرَ بلا دَينٍ ──────────────────────────────────


def _inventory() -> Any:
    root = next(
        p
        for p in Path(__file__).resolve().parents
        if (p / "tools" / "audit" / "sovereign_write_inventory.py").is_file()
    )
    tool = root / "tools" / "audit" / "sovereign_write_inventory.py"
    spec = importlib.util.spec_from_file_location("_wi111_inventory", tool)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.collect(root)


def test_wi111_t6_inventory_has_no_debt_on_settled_surfaces() -> None:
    sites = [s for s in _inventory() if "/federal_judiciary/" in s.path and s.public]
    debt = {(Path(s.path).name, s.function) for s in sites if not s.guarded and not s.closed_legacy}
    assert not (debt & SETTLED_SURFACES), sorted(debt & SETTLED_SURFACES)
    guarded = {(Path(s.path).name, s.function) for s in sites if s.guarded}
    for surface in (
        ("docket.py", "open_case"),
        ("docket.py", "add_party"),
        ("docket.py", "add_claim"),
        ("docket.py", "record_proceeding"),
    ):
        assert surface in guarded, surface
    # والمؤجَّلُ وJ4 دَينٌ باقٍ كما هو (لا مساسَ — D21-أ بند 9).
    for surface in (("service.py", "submit_evidence"), ("service.py", "appoint_judge")):
        assert surface in debt, surface


# ── T7 · لا عبورَ داخلَ عبورٍ ────────────────────────────────────────────────────


def test_wi111_t7_no_nested_crossing_on_any_surface(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    flow = _full_flow(registry, national, judiciary, crown, "t7")
    spy: SpyingAuthorizer = flow["spy"]
    assert spy.max_depth == 1
    session = j1._session()
    try:
        # إجراءُ الحكمِ قُيِّدَ بالكاتبِ الخاصِّ داخلَ مُطبِّقِ `issue_ruling` (لا `record_proceeding` عابرًا).
        assert (
            session.query(CaseProceedingModel)
            .filter(
                CaseProceedingModel.case_id == flow["case"]["id"],
                CaseProceedingModel.proceeding_type == "RULING",
            )
            .count()
            == 1
        )
        assert spy.actions().count("record_proceeding") == 1
        assert (
            session.query(CaseClaimModel)
            .filter(CaseClaimModel.case_id == flow["case"]["id"])
            .count()
            == 1
        )
        evidence = session.get(CaseEvidenceModel, flow["evidence"]["id"])
        assert evidence is not None and evidence.status == "admitted"
        judge = session.get(CourtJudgeModel, flow["bench"].judge["id"])
        assert judge is not None and judge.status == "suspended"
    finally:
        session.close()
