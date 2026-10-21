"""
WI-105 · J1 — عبورُ `issue_ruling` الحدَّ السياديَّ بفاعلٍ قضائيٍّ مُعلَنٍ (Q-6 ①).

الهدف: إثباتُ أنَّ إصدارَ الحكمِ يعبرُ الحدَّ السياديَّ منَ البياناتِ الحيّةِ
       (طلبُ اختصاصٍ لا ثوابتَ) بفاعلٍ قضائيٍّ ثابتٍ في الوحدةِ، وأنّ الكتابةَ
       الوحيدةَ للحكمِ صارت خلفَ الحدِّ في معاملةٍ واحدةٍ، وأنّ المكرَّرَ يُرفَضُ
       قبلَ الحدِّ، والبديلَ بعدَ الإلغاءِ بجيلٍ جديدٍ، وأنّ المُعوِّضَ يستعيدُ
       الحالةَ كما كانت، والإعادةَ بلا صفٍّ تفرُّقٌ صريحٌ لا نجاحٌ يُزعَم.
النطاق: قياسُ سلوكِ `rulings.issue_ruling` عبرَ الحدِّ وحدَه — لا تعديلَ للبوابةِ
        ولا للقواعدِ الدستوريّةِ ولا لفحوصِ r7d القائمةِ (كلُّها بلا تعديلٍ).
المالك: federal/executive/services — WI-105 (بقرارِ المالكِ Q-6 ① وتصميمِ J1
        المعتمدِ بتوجيهِ المستشارِ 17 § 1 · D17-6).
تاريخ الإنشاء: 2026-10-21 (W-593 · WI-105 · الدفعةُ J1)

الفحوصُ كما وردتْ في وثيقةِ التصميمِ (§ 3) — T1–T7:
- T1 · ALLOW للقضائيّ: الحكمُ يصدرُ عبرَ الخدمةِ · وآخرُ قرارٍ في سجلِّ البوابةِ
  `issue_ruling` بفاعلِ `judicial` · والصفوفُ الثلاثةُ مُلتزَمةٌ.
- T2 · DENY للتنفيذيّ: `JUDICIARY_ACTOR="EXECUTIVE"` ⇒ `SovereigntyViolation`
  ولا صفَّ حكمٍ ولا إجراءَ وحالةُ القضيّةِ كما كانت.
- T3 · الاختصاصُ منَ البيانات: الطلبُ المُمرَّرُ يحملُ `case.jurisdiction`
  و`position_scope` الحقيقيَّينِ (جاسوسٌ على `boundary.execute`).
- T4 · البديلُ بعدَ الإلغاء: حكمٌ ← إلغاءٌ ← بديلٌ = صفّانِ بجيلَي `g0` و`g1`.
- T5 · المكرَّرُ قبلَ الحدّ: الطلبُ الثاني للمرحلةِ ⇒ `DuplicateRulingError`
  ولا قرارَ جديدٌ في سجلِّ البوابةِ.
- T6 · المُعوِّض: إسقاطُ تثبيتِ النجاحِ بعدَ الالتزامِ ⇒ `CompensationRequired`
  و`state_is_clean` والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ.
- T7 · التفرُّق: إعادةٌ وصفُّ الحكمِ غائبٌ ⇒ `RulingLedgerDivergenceError`.

الحدُّ المُعلَنُ في هذا الفحصِ:
- تبديلُ الفاعلِ في T2 بـ`monkeypatch` على ثابتِ الوحدةِ وإفراغِ المُفوِّضِ
  المحفوظِ — لا معاملَ إنتاجيًّا (D1: الفاعلُ ثابتٌ في الوحدةِ).
- لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذِ (§ 4.3) — هذا ملفُّ قياسٍ لا حُكمِ
  مراجعةٍ، والجولةُ على الدفعةِ كلِّها قرارُ مجلسٍ مستقلٌ.

الدليلُ المُعادُ تشغيلُه:
    AMOS_DATABASE_URL="sqlite:////tmp/amos_w593.db" .venv/bin/python -m pytest \\
        federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py -q
"""

from __future__ import annotations

import uuid
from typing import Any

import pytest

from amos_federation.common.database import get_session_factory, init_db
from amos_federation.common.principal import (
    DEFAULT_TENANT,
    AuthorizationContext,
    Principal,
)
from amos_federation.services.executive_core.agent_identity import register_identity
from amos_federation.services.executive_core.engine import reset_executive_core
from amos_federation.services.federal_judiciary import (
    DuplicateRulingError,
    FederalJudiciary,
    get_federal_judiciary,
    reset_federal_judiciary,
)
from amos_federation.services.federal_judiciary import rulings as rulings_module
from amos_federation.services.federal_judiciary.authority import (
    resolve_judicial_authority,
)
from amos_federation.services.federal_judiciary.models import (
    CaseProceedingModel,
    CourtJudgeModel,
    CourtModel,
    LegalCaseModel,
    RulingModel,
)
from amos_federation.services.governance.security import DEFAULT_ROLES
from amos_federation.services.government_services.service import (
    reset_government_services,
)
from amos_federation.services.national_registry.models import (
    AuthorityGrantModel,
    DecisionProvenanceModel,
    IdentityAgentModel,
    IdentityModel,
    IdentityPrincipalModel,
    OfficialPositionModel,
    PositionModel,
)
from amos_federation.services.national_registry.service import (
    NationalRegistry,
    get_national_registry,
    reset_national_registry,
)
from amos_federation.services.state_registry.service import (
    StateRegistry,
    get_state_registry,
    reset_state_registry,
)
from amos_federation.services.state_treasury.models import (
    AccountModel as TreasuryAccountModel,
)
from amos_federation.services.state_treasury.models import (
    AllocationModel,
    BudgetModel,
    LedgerEntryModel,
    TransactionModel,
    TreasuryModel,
)
from amos_federation.services.state_treasury.service import (
    reset_state_treasury,
)
from tests.conftest import purge_agents, purge_tasks

_ROLE_PERMISSIONS = {role["role_id"]: tuple(role["permissions"]) for role in DEFAULT_ROLES}


def _context(
    role_id: str,
    *,
    tenant_id: str | None = None,
    username: str = "wi105-user",
) -> AuthorizationContext:
    return AuthorizationContext.from_principal(
        Principal.from_session_record(
            session_id=f"wi105-{role_id}-{username}",
            username=username,
            role_id=role_id,
            permissions=_ROLE_PERMISSIONS[role_id],
            expires_at=None,
            tenant_id=tenant_id,
        )
    )


def _session():
    return get_session_factory()()


def _code(prefix: str = "WI105") -> str:
    """قيمةٌ لا تتكرّرُ — سلاسلُ الاختبارِ تحتاجُ تمايزًا في القاعدةِ الواحدةِ."""
    return f"{prefix}-{uuid.uuid4().hex[:10]}"


def _agent(tenant_id: str = DEFAULT_TENANT) -> str:
    """وكيلٌ حقيقيٌّ في `agents` — سجلُّ R4 الكانونيّ، ولا يُنشئهُ القضاءُ."""
    agent_id = f"agent-wi105-{uuid.uuid4().hex[:10]}"
    register_identity(agent_id, f"وكيل {agent_id}", "executor", tenant_id=tenant_id)
    return agent_id


class Bench:
    """منصّةٌ قضائيةٌ جاهزةٌ — نسخةٌ من نمطِ r7d (الأصلُ بلا تعديلٍ)."""

    def __init__(self, **kwargs: object) -> None:
        self.__dict__.update(kwargs)


def _judicial_chain(
    registry: StateRegistry,
    national: NationalRegistry,
    crown: AuthorizationContext,
    context: AuthorizationContext,
    *,
    scope: str = "FEDERAL",
) -> Bench:
    institution = registry.register_institution(
        context=crown,
        code=_code("JUD"),
        name="المحكمة الفدرالية",
        kind="court",
        branch="judicial",
    )
    agent_id = _agent()
    official = registry.appoint_official(
        context=crown,
        agent_id=agent_id,
        institution_code=institution["code"],
        title="قاضٍ",
    )
    identity = national.create_identity(context=crown, identity_type="PERSON", label="قاضٍ")
    national.link_principal(
        context=crown, principal_id=context.principal_id, identity_id=identity["id"]
    )
    national.link_agent(context=crown, agent_id=agent_id, identity_id=identity["id"])
    position = national.create_position(
        context=crown,
        code=_code("POS"),
        title="قاضٍ",
        institution_code=institution["code"],
        authority_scope=scope,
    )
    assignment = national.assign_position(
        context=crown, official_id=official["id"], position_id=position["id"]
    )
    return Bench(
        institution=institution,
        agent_id=agent_id,
        official=official,
        identity=identity,
        position=position,
        assignment=assignment,
    )


def _bench(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    judge_ctx: AuthorizationContext,
    *,
    jurisdiction: str = "FEDERAL",
) -> Bench:
    """سلسلةٌ قضائيةٌ كاملةٌ تنتهي بمحكمةٍ نشطةٍ وقاضٍ مُقلَّدٍ فيها."""
    bench = _judicial_chain(registry, national, crown, judge_ctx, scope=jurisdiction)
    bench.court = judiciary.register_court(
        context=crown,
        code=_code("CRT"),
        name="محكمة اختبار WI-105",
        level="FIRST_INSTANCE",
        jurisdiction=jurisdiction,
        institution_code=bench.institution["code"],
    )
    bench.judge = judiciary.appoint_judge(
        context=crown,
        court_id=bench.court["id"],
        official_id=bench.official["id"],
        position_id=bench.position["id"],
    )
    return bench


def _party_identity(
    national: NationalRegistry, crown: AuthorizationContext, context: AuthorizationContext
) -> dict[str, Any]:
    identity = national.create_identity(context=crown, identity_type="PERSON", label="مُدَّعٍ")
    national.link_principal(
        context=crown, principal_id=context.principal_id, identity_id=identity["id"]
    )
    return identity


def _open_and_assign(
    judiciary: FederalJudiciary,
    filer_ctx: AuthorizationContext,
    crown: AuthorizationContext,
    bench: Bench,
) -> str:
    """قضيّةٌ مفتوحةٌ ومُقدَّمةٌ ومُسندةٌ إلى قاضي المنصّةِ — بالتتابعِ المفروضِ."""
    case = judiciary.open_case(
        context=filer_ctx,
        court_id=bench.court["id"],
        case_type="CIVIL",
        subject="نزاعٌ على تنفيذِ التزامٍ (WI-105)",
        reference=_code("CASE"),
    )
    judiciary.file_case(context=filer_ctx, case_id=case["id"])
    assigned = judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
    return str(assigned["id"])


@pytest.fixture
def registry() -> StateRegistry:
    return get_state_registry()


@pytest.fixture
def national() -> NationalRegistry:
    return get_national_registry()


@pytest.fixture
def judiciary() -> FederalJudiciary:
    return get_federal_judiciary()


@pytest.fixture
def crown(national: NationalRegistry) -> AuthorizationContext:
    """التاجُ — `*` فيمرُّ في كلِّ حدٍّ، ولهُ هويةٌ كانونيّةٌ كأيِّ فاعلٍ آخر."""
    context = _context("king", username="crown")
    identity = national.create_identity(context=context, identity_type="PERSON", label="التاج")
    national.link_principal(
        context=context, principal_id=context.principal_id, identity_id=identity["id"]
    )
    return context


@pytest.fixture(autouse=True)
def _fresh_state() -> None:
    """قاعدةٌ نظيفةٌ قبلَ كلِّ فحصٍ — القياسُ على سجلٍّ حقيقيٍّ لا على بقايا.

    ترتيبُ الحذفِ مقصودٌ (الأثرُ قبلَ الحكمِ والحكمُ قبلَ القضيّةِ) — نسخةٌ من
    نمطِ `test_r7d_federal_judiciary._fresh_state` بلا تعديلِ الأصلِ المحروسِ.
    """
    init_db()
    session = get_session_factory()()
    try:
        session.query(RulingModel).delete()
        session.query(CaseProceedingModel).delete()
        session.query(LegalCaseModel).delete()
        session.query(CourtJudgeModel).delete()
        session.query(CourtModel).delete()
        session.query(AuthorityGrantModel).delete()
        session.query(DecisionProvenanceModel).delete()
        session.query(LedgerEntryModel).delete()
        session.query(TransactionModel).delete()
        session.query(AllocationModel).delete()
        session.query(BudgetModel).delete()
        session.query(TreasuryAccountModel).delete()
        session.query(TreasuryModel).delete()
        session.query(OfficialPositionModel).delete()
        session.query(PositionModel).delete()
        session.query(IdentityAgentModel).delete()
        session.query(IdentityPrincipalModel).delete()
        session.query(IdentityModel).delete()
        purge_tasks(session)
        purge_agents(session)
        session.commit()
    finally:
        session.close()
    reset_executive_core()
    reset_state_registry()
    reset_government_services()
    reset_state_treasury()
    reset_national_registry()
    reset_federal_judiciary()
    # إفراغُ المُفوِّضِ القضائيِّ المحفوظِ أيضًا: تبديلُ الفاعلِ في فحصٍ لا يتسرّبُ
    # إلى فحصٍ آخرَ (البناءُ كسولٌ يُبنى بثابتِ الوحدةِ عندَ أوّلِ نداءٍ بعدهُ).
    rulings_module.reset_judiciary_authorizer()


class RecordingJudiciaryAuthorizer(rulings_module.ConstitutionalAuthorizer):
    """يسجّلُ كلَّ نتيجةٍ محروسةٍ — لقياسِ العبورِ لا لاتخاذِ قرارٍ."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.results.append(guarded)
        return guarded


def _install_recording_authorizer() -> RecordingJudiciaryAuthorizer:
    """ثبِّتْ مُصرِّحًا مسجِّلًا بثابتِ الوحدةِ نفسِهِ — المسارُ الإنتاجيُّ كما هو.

    D1: لا معاملَ `authorizer` في `rulings.issue_ruling` — الاختبارُ يلمسُ
    المُفوِّضَ الافتراضيَّ المحفوظَ في الوحدةِ (المُبدَّلُ بثابتِ الفاعلِ نفسِهِ).
    """
    authorizer = RecordingJudiciaryAuthorizer(actor=rulings_module.JUDICIARY_ACTOR)
    rulings_module._DEFAULT_JUDICIARY_AUTHORIZER = authorizer
    return authorizer


def _prepared_case(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    username: str,
) -> tuple[Bench, str, AuthorizationContext]:
    """منصّةٌ وقضيّةٌ مُسندةٌ — الترتيبُ نفسُهُ الذي تفحصُهُ r7d بلا تعديلٍ."""
    judge_ctx = _context("official", username=username)
    bench = _bench(registry, national, judiciary, crown, judge_ctx)
    filer = _context("official", username=f"filer-{username}")
    _party_identity(national, crown, filer)
    case_id = _open_and_assign(judiciary, filer, crown, bench)
    return bench, case_id, judge_ctx


# ── T1 · ALLOW للقضائيّ — العبورُ والصفوفُ الثلاثةُ ──────────────────────────


def test_wi105_t1_issue_ruling_crosses_boundary_as_judicial(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    authorizer = _install_recording_authorizer()
    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t1")

    payload = judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case_id,
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
    )

    # الحكمُ صدرَ عبرَ الخدمةِ كما كان — عقدُ الإرجاعِ القائمُ لم يتغيّرْ.
    assert payload["status"] == "issued"

    # عبورٌ واحدٌ بدليلِهِ الحرفيِّ: الفعلُ والقرارُ والهدفُ بجيلِهِ.
    assert len(authorizer.results) == 1
    evidence = authorizer.results[0].evidence.as_dict()
    assert evidence["action"] == "issue_ruling"
    assert evidence["decision"] == "ALLOW"
    assert evidence["target"] == f"judiciary/rulings/{case_id}/FIRST_INSTANCE/g0"

    # وآخرُ قرارٍ في سجلِّ البوابةِ: `issue_ruling` بفاعلٍ قضائيٍّ مُعلَنٍ.
    record = authorizer.gateway.records[-1]
    assert record.action == "issue_ruling"
    assert record.actor == "judicial"
    assert record.decision == "ALLOW"

    # والصفوفُ الثلاثةُ مُلتزَمةٌ معًا: الحكمُ والإجراءُ وحالةُ القضيّةِ.
    session = _session()
    try:
        row = session.query(RulingModel).filter(RulingModel.case_id == case_id).one_or_none()
        assert row is not None and row.status == "issued"
        proceedings = (
            session.query(CaseProceedingModel)
            .filter(
                CaseProceedingModel.case_id == case_id,
                CaseProceedingModel.proceeding_type == "RULING",
            )
            .all()
        )
        assert len(proceedings) == 1
        case = session.get(LegalCaseModel, case_id)
        assert case is not None and case.status == "decided"
    finally:
        session.close()


# ── T2 · DENY للتنفيذيّ — فصلُ السلطاتِ ينطقُ ────────────────────────────────


def test_wi105_t2_executive_actor_is_denied(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation  # يُتاحُ أوّلًا (الجسرُ)

    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t2")

    # تبديلُ الفاعلِ منَ الثابتِ المحروسِ لا من معاملٍ إنتاجيٍّ (D1).
    monkeypatch.setattr(rulings_module, "JUDICIARY_ACTOR", "EXECUTIVE")
    rulings_module.reset_judiciary_authorizer()

    with pytest.raises(SovereigntyViolation):
        judiciary.issue_ruling(
            context=judge_ctx,
            case_id=case_id,
            stage="FIRST_INSTANCE",
            decision="GRANTED",
            disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
        )

    # الرفضُ منعٌ حقيقيٌّ: لا صفَّ حكمٍ ولا إجراءَ حكمٍ، وحالةُ القضيّةِ كما كانت.
    session = _session()
    try:
        assert session.query(RulingModel).filter(RulingModel.case_id == case_id).count() == 0
        assert (
            session.query(CaseProceedingModel)
            .filter(
                CaseProceedingModel.case_id == case_id,
                CaseProceedingModel.proceeding_type == "RULING",
            )
            .count()
            == 0
        )
        case = session.get(LegalCaseModel, case_id)
        assert case is not None and case.status != "decided"
    finally:
        session.close()


# ── T3 · الاختصاصُ منَ البياناتِ الحيّةِ ─────────────────────────────────────


def test_wi105_t3_jurisdiction_request_carries_live_data(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    bench, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t3")

    authorizer = rulings_module._judiciary_authorizer()
    captured: dict[str, Any] = {}
    original_execute = type(authorizer.boundary).execute

    def spying_execute(self: Any, *args: Any, **kwargs: Any) -> Any:
        captured["judicial_action"] = kwargs.get("judicial_action")
        return original_execute(self, *args, **kwargs)

    monkeypatch.setattr(type(authorizer.boundary), "execute", spying_execute)

    judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case_id,
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
    )

    action = captured.get("judicial_action")
    assert action is not None, "الحدَّ لم يستلمْ طلبَ اختصاصٍ"
    assert action.action == "issue_ruling"

    # القيمُ منَ البياناتِ الحيّةِ لا من ثوابتَ: تُقرأُ منَ الصفوفِ نفسِها —
    # القضيّةِ والسلطةِ المحلولةِ منَ القاعدةِ بقرارِ الفحصِ لا بتخمينِهِ.
    session = _session()
    try:
        case = session.get(LegalCaseModel, case_id)
        assert case is not None
        assert action.case_scope == case.jurisdiction
        assert action.target == case.id
        authority = resolve_judicial_authority(
            session, judge_ctx, court_id=bench.court["id"], case_id=case_id
        )
        assert authority.classification == "PROVEN"
        assert action.court_scope == authority.jurisdiction
        assert action.actor_scope == authority.position_scope
        assert action.institution_id == authority.institution_id
        # مؤسّسةُ القضيّةِ هي مؤسّسةُ محكمتِها — مُعلَنٌ لا مُخمَّنٌ (D3).
        assert action.case_institution_id == authority.institution_id
        assert action.is_royal_decree_target is False
    finally:
        session.close()


# ── T4 · البديلُ بعدَ الإلغاءِ — جيلانِ لا إعادةٌ ──────────────────────────────


def test_wi105_t4_replacement_after_vacation_uses_new_generation(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    authorizer = _install_recording_authorizer()
    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t4")

    first = judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case_id,
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
    )
    first_id = first["id"]

    judiciary.vacate_ruling(
        context=judge_ctx, ruling_id=first_id, reason="إلغاءٌ لاختبارِ البديلِ (T4)"
    )

    second = judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case_id,
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
    )
    assert second["status"] == "issued"

    # صفّانِ للمرحلةِ: الأوّلُ مُلغى والثاني قائمٌ — والجيلانِ في هدفَي العبورِ.
    session = _session()
    try:
        rows = (
            session.query(RulingModel)
            .filter(RulingModel.case_id == case_id)
            .order_by(RulingModel.created_at)
            .all()
        )
        assert len(rows) == 2
        assert rows[0].status == "vacated"
        assert rows[1].status == "issued"
        assert rows[1].id != first_id
    finally:
        session.close()

    assert len(authorizer.results) == 2
    targets = [r.evidence.as_dict()["target"] for r in authorizer.results]
    assert targets[0] == f"judiciary/rulings/{case_id}/FIRST_INSTANCE/g0"
    assert targets[1] == f"judiciary/rulings/{case_id}/FIRST_INSTANCE/g1"


# ── T5 · المكرَّرُ قبلَ الحدِّ — لا قرارَ جديدَ ──────────────────────────────


def test_wi105_t5_duplicate_rejected_before_boundary(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    authorizer = _install_recording_authorizer()
    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t5")

    judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case_id,
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
    )
    decisions_before = len(authorizer.gateway.records)

    with pytest.raises(DuplicateRulingError):
        judiciary.issue_ruling(
            context=judge_ctx,
            case_id=case_id,
            stage="FIRST_INSTANCE",
            decision="GRANTED",
            disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
        )

    # المكرَّرُ لم يعبُرِ الحدَّ أصلًا: لا عبورَ جديدَ ولا قرارَ في البوابةِ.
    assert len(authorizer.results) == 1
    assert len(authorizer.gateway.records) == decisions_before


# ── T6 · المُعوِّضُ — استعادةٌ تقنيّةٌ دقيقةٌ ────────────────────────────────


def test_wi105_t6_compensator_restores_state_after_failed_settle(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Any,
) -> None:
    """T6 · المُعوِّضُ — استعادةٌ تقنيّةٌ دقيقةٌ عبرَ حارسِ 1I بالخطةِ المربوطةِ.

    اكتشافُ تنفيذٍ مُعلَنٌ في وثيقةِ التصميمِ (إضافةٌ مؤرَّخةٌ): مسارُ الحدِّ
    أحاديَّ الأثرِ ينفّذُ عبرَ `run_once` لا عبرَ معاملةِ 1I المُعوَّضةَ، فالتعويضُ
    الآليُّ غيرُ موصولٍ هناك. فيُقاسُ المُعوِّضُ هنا كما تقيسُهُ حوكمةُ 1I: بإسقاطِ
    تثبيتِ النجاحِ بعدَ الالتزامِ (الصفوفُ مُلتزَمةٌ والسجلُّ RUNNING) ثمّ
    التعويضِ بحارسِ 1I بالعقدِ والخطةِ والمفتاحِ الحقيقيّةِ المُلتقَطةِ من
    العبورِ نفسِهِ.
    """
    from core.sovereignty.compensation import (
        CompensationGuard,
        CompensationJournal,
        bind_compensation_plan,
    )
    from core.sovereignty.contract import bind_contract
    from core.sovereignty.idempotency import IdempotencyGuard

    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t6")
    authorizer = rulings_module._judiciary_authorizer()

    # جاسوسٌ على العبورِ: يلتقطُ العقدَ (الآثارَ) والمعوّضاتِ والمفتاحَ كما
    # تُمرَّرُ إلى الحدِّ — فالخطةُ تُبنى بها كما يربطُها الحدُّ نفسُهُ.
    crossing: dict[str, Any] = {}
    original_guard = rulings_module.ConstitutionalAuthorizer.guard_declared

    def spying_guard(self: Any, *args: Any, **kwargs: Any) -> Any:
        crossing["action"], crossing["target"] = args[0], args[1]
        crossing.update(kwargs)
        return original_guard(self, *args, **kwargs)

    monkeypatch.setattr(rulings_module.ConstitutionalAuthorizer, "guard_declared", spying_guard)

    # إسقاطُ تثبيتِ النجاحِ بعدَ الالتزامِ: المُطبِّقُ يلتزمُ الصفوفَ ثمّ يفشلُ
    # الختامُ — فهذا موضعُ المُعوِّضِ (تصميمُ D7-أ).
    ledger = authorizer.boundary.idempotency_ledger

    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("تثبيتُ النجاحِ مُسقَطٌ — فحصُ المُعوِّضِ (T6)")

    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)

    with pytest.raises(RuntimeError):
        judiciary.issue_ruling(
            context=judge_ctx,
            case_id=case_id,
            stage="FIRST_INSTANCE",
            decision="GRANTED",
            disposition="قضاءُ الفحصِ — إثباتُ المُعوِّضِ",
        )
    monkeypatch.setattr(
        type(ledger),
        "mark_succeeded",
        ledger.mark_succeeded.__func__
        if hasattr(ledger.mark_succeeded, "__func__")
        else type(ledger).mark_succeeded,
    )  # type: ignore[arg-type]

    # والصفوفُ مُلتزَمةٌ فعلًا (الفشلُ بعدَ الالتزامِ لا قبلهُ) — وهذا موضعُ
    # الاستعادةِ لا قبلَهُ.
    session = _session()
    try:
        assert session.query(RulingModel).filter(RulingModel.case_id == case_id).count() == 1
    finally:
        session.close()

    # التعويضُ بحارسِ 1I: العقدُ والخطةُ والمفتاحُ من العبورِ الحقيقيِّ نفسِهِ.
    effects = crossing["declared_effects"]
    contract = bind_contract(
        actor="judicial",
        action="issue_ruling",
        target=crossing["target"],
        declared_effects=effects,
    )
    plan = bind_compensation_plan(contract=contract, compensators=crossing["compensators"])
    guard = CompensationGuard(
        journal=CompensationJournal(path=tmp_path / "wi105_t6_compensation.json"),
        idempotency=IdempotencyGuard(ledger=ledger),
    )
    outcome = guard.compensate(
        contract=contract,
        plan=plan,
        operation_key=crossing["operation_key"],
        applied_signatures=tuple(e.signature for e in effects),
        reason="فشلُ تثبيتِ النجاحِ بعدَ الالتزامِ (T6)",
    )

    # الحصيلةُ صادقةٌ: الدولةُ رجعتْ كما كانت بالضبطِ.
    assert outcome.state_is_clean is True

    # والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ إلى ما قبلَ العمليّةِ.
    session = _session()
    try:
        assert session.query(RulingModel).filter(RulingModel.case_id == case_id).count() == 0
        assert (
            session.query(CaseProceedingModel)
            .filter(
                CaseProceedingModel.case_id == case_id,
                CaseProceedingModel.proceeding_type == "RULING",
            )
            .count()
            == 0
        )
        case = session.get(LegalCaseModel, case_id)
        assert case is not None and case.status != "decided"
    finally:
        session.close()


# ── T7 · التفرُّقُ — إعادةٌ بلا صفٍّ لا تُسكَتُ ──────────────────────────────


def test_wi105_t7_replay_with_missing_row_raises_divergence(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t7")

    first = judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case_id,
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
    )

    # حذفُ صفِّ الحكمِ خارجَ العمليّةِ (كما يفعلُ تفريغُ الاختباراتِ): سجلُّ
    # الذرّيّةِ يُثبِتُ النجاحَ والصفُّ غائبٌ — تفرُّقٌ لا يُسكَتُ عنهُ ولا
    # يُعادُ الإنشاءُ خارجَ الحدِّ ولا يُزعَمُ نجاحٌ لم يقعْ.
    session = _session()
    try:
        row = session.get(RulingModel, first["id"])
        assert row is not None
        session.delete(row)
        session.commit()
    finally:
        session.close()

    with pytest.raises(rulings_module.RulingLedgerDivergenceError):
        judiciary.issue_ruling(
            context=judge_ctx,
            case_id=case_id,
            stage="FIRST_INSTANCE",
            decision="GRANTED",
            disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
        )
