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
  [W-603 · 2026-10-22 · Q-70] كُتِبَ إنتاجيًّا (T6p): النداءُ الإنتاجيُّ وحدَه بلا تعويضٍ يدويٍّ.
- T7 · التفرُّق: إعادةٌ وصفُّ الحكمِ غائبٌ ⇒ `RulingLedgerDivergenceError`.

[إضافةٌ مؤرَّخةٌ · 2026-10-22 · W-603 · قرارُ المالكِ Q-70 · ملحقُ التصميمِ § 7.6]:
- T8 · نظيرُ T6p لـWI-082: `register_identity` وحدَه مع الإسقاطِ ⇒ `CompensationRequired`
  نظيفًا والصفُّ غائبٌ والذرّيّةُ `FAILED_RETRYABLE` والإعادةُ تنجح.
- T9 · فشلُ المُعوِّضِ نفسِه ⇒ `state_is_clean is False` · `requires_human` · الباقي مُسمًّى ·
  الذرّيّةُ `FAILED_FINAL` · والإعادةُ مرفوضةٌ.
- T10 · الحلقةُ الثانيةُ: فشلانِ متتاليانِ بعدَ الالتزامِ ⇒ كلٌّ يعكسُ صفوفَه فعلًا.

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

import math
import time
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



def _ruling_results(authorizer: Any) -> list[Any]:
    """عبوراتُ `issue_ruling` وحدَها منَ المُصرِّحِ المشتركِ.

    مُضافٌ في WI-111 (J2+J3 · W-640): المُصرِّحُ نفسُه صارَ يعبرُ به تجهيزُ الفحصِ أيضًا
    (فتحُ القضيّةِ وقيدُها وإسنادُها وإلغاءُ الحكمِ) — فعدُّ `authorizer.results` كلِّها
    لم يعُدْ يقيسُ `issue_ruling`. والتصفيةُ بالفعلِ تُبقي قصدَ الفحصِ كما هو: عددُ
    عبوراتِ إصدارِ الحكمِ بعينِه (لا تخفيفَ — والقيدُ الثاني في T5 على سجلِّ البوابةِ باقٍ).
    """
    return [r for r in authorizer.results if r.evidence.as_dict()["action"] == "issue_ruling"]

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
    assert len(_ruling_results(authorizer)) == 1
    evidence = _ruling_results(authorizer)[0].evidence.as_dict()
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

    assert len(_ruling_results(authorizer)) == 2
    targets = [r.evidence.as_dict()["target"] for r in _ruling_results(authorizer)]
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
    assert len(_ruling_results(authorizer)) == 1
    assert len(authorizer.gateway.records) == decisions_before


# ── T6p · المُعوِّضُ على المسارِ الإنتاجيِّ — الحدُّ يُعوِّضُ آليًّا (W-603 · Q-70) ──
#
# [إضافةٌ مؤرَّخةٌ · 2026-10-22 · W-603] T6 القديمُ (W-593) كانَ يتوقّعُ `RuntimeError`
# خامًا من النداءِ الإنتاجيِّ ثمَّ يُعوِّضُ يدويًّا بحارسِ 1I. وقرارُ المالكِ Q-70 وصلَ
# التعويضَ في الحدِّ نفسِه، فصارَ النداءُ الإنتاجيُّ وحدَه يرفعُ `CompensationRequired`
# بعدَ العكسِ — فيُكتَبُ الفحصُ إنتاجيًّا (تشديدٌ لا تخفيفٌ: لا تعويضَ يدويًّا هنا).


def _drop_settle(monkeypatch: pytest.MonkeyPatch, ledger: Any, label: str) -> Any:
    """إسقاطُ تثبيتِ النجاحِ بعدَ التزامِ المُطبِّقِ — يُرجِعُ الأصلَ لرفعِ الإسقاط."""
    original = type(ledger).mark_succeeded

    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError(f"تثبيتُ النجاحِ مُسقَطٌ — {label}")

    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)
    return original


def _next_second() -> None:
    """حدٌّ معلنٌ مقيسٌ (W-603): معرِّفُ الإذنِ `EP-<العقد>-<الثانية>` (enforcement.py خارجَ
    النطاقِ) فإعادةُ العقدِ نفسِه في الثانيةِ نفسِها تُرفَضُ `PermitReplayError` — إغلاقًا لا
    فتحًا. فالإعادةُ في الفحصِ تعبرُ إلى الثانيةِ التاليةِ ولا تُزوِّرُ الزمن."""
    now = time.time()
    time.sleep(math.ceil(now) - now + 0.05)


def _ruling_key(case_id: str) -> Any:
    from core.sovereignty.idempotency import IdempotencyKey

    return IdempotencyKey(scope="judiciary.ruling.issue", value=f"{case_id}:FIRST_INSTANCE:g0")


def _ruling_rows(case_id: str) -> tuple[int, int, str]:
    session = _session()
    try:
        rulings = session.query(RulingModel).filter(RulingModel.case_id == case_id).count()
        procs = (
            session.query(CaseProceedingModel)
            .filter(
                CaseProceedingModel.case_id == case_id,
                CaseProceedingModel.proceeding_type == "RULING",
            )
            .count()
        )
        case = session.get(LegalCaseModel, case_id)
        assert case is not None
        return rulings, procs, case.status
    finally:
        session.close()


def _issue(judiciary: FederalJudiciary, judge_ctx: AuthorizationContext, case_id: str) -> Any:
    return judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case_id,
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ الفحصِ — إثباتُ المُعوِّضِ",
    )


def test_wi105_t6p_boundary_compensates_failed_settle_on_production_path(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """T6p · نداءُ `issue_ruling` وحدَه مع إسقاطِ التثبيتِ ⇒ الحدُّ يعكسُ ويرفعُ — لا يدويَّ."""
    from core.sovereignty.compensation import CompensationRequired
    from core.sovereignty.idempotency import OperationStatus

    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t6p")
    status_before = _ruling_rows(case_id)[2]
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T6p")

    with pytest.raises(CompensationRequired) as caught:
        _issue(judiciary, judge_ctx, case_id)
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    outcome = caught.value.outcome
    assert outcome.state_is_clean is True
    assert outcome.requires_human is False
    assert isinstance(caught.value.__cause__, Exception)  # الأصلُ محفوظٌ لا مُبتلَع
    # الصفوفُ غائبةٌ والقضيّةُ بحالتِها السابقةِ (مُعوِّضُ D7-أ نفسُه)
    assert _ruling_rows(case_id) == (0, 0, status_before)
    # والذرّيّةُ قابلةٌ للإعادةِ بآثارٍ مطبَّقةٍ لا شيءَ
    record = ledger.get(_ruling_key(case_id))
    assert record is not None
    assert record.status is OperationStatus.FAILED_RETRYABLE
    assert tuple(record.applied_effect_signatures) == ()

    # الإعادةُ بعدَ رفعِ الإسقاطِ تنجحُ بحكمٍ واحدٍ
    _next_second()
    issued = _issue(judiciary, judge_ctx, case_id)
    assert issued["id"]
    rulings, procs, status_after = _ruling_rows(case_id)
    assert (rulings, procs) == (1, 1)
    assert status_after == "decided"


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


# ── T8 · نظيرُ T6p لـWI-082 — الوصلُ في الحدِّ مرّةً لكلِّ سطحٍ مُهجَّرٍ ──────────


def test_wi105_t8_boundary_compensates_register_identity_on_production_path(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired
    from core.sovereignty.idempotency import IdempotencyKey, OperationStatus

    from amos_federation.services.executive_core import agent_identity as agent_identity_module
    from amos_federation.services.executive_core.agent_identity import get_identity
    from amos_federation.services.executive_core.sovereignty_bridge import (
        ConstitutionalAuthorizer,
    )

    agent_id = _code("wi105-t8")
    authorizer = ConstitutionalAuthorizer(actor=agent_identity_module.AGENT_IDENTITY_ACTOR)
    ledger = authorizer.boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T8")
    try:
        with pytest.raises(CompensationRequired) as caught:
            register_identity(agent_id, "فحص T8", "probe", authorizer=authorizer)
        monkeypatch.setattr(type(ledger), "mark_succeeded", original)

        assert caught.value.outcome.state_is_clean is True
        assert get_identity(agent_id) is None
        record = ledger.get(
            IdempotencyKey(scope=agent_identity_module.IDENTITY_SPAWN_SCOPE, value=agent_id)
        )
        assert record is not None
        assert record.status is OperationStatus.FAILED_RETRYABLE

        _next_second()
        register_identity(agent_id, "فحص T8", "probe", authorizer=authorizer)
        assert get_identity(agent_id) is not None
    finally:
        agent_identity_module._delete_identity_row(agent_id)


# ── T9 · فشلُ المُعوِّضِ نفسِه — إغلاقٌ عندَ الفشلِ والحسمُ بيدِ إنسانٍ ─────────────


def test_wi105_t9_failing_compensator_closes_operation_final(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired, Compensator
    from core.sovereignty.idempotency import IdempotencyError, OperationStatus

    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t9")
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger

    # المُعوِّضاتُ المُعلَنةُ نفسُها بأسمائِها — لكنَّ عكسَها يرفع (عطبُ القاعدةِ مثلًا).
    original_guard = rulings_module.ConstitutionalAuthorizer.guard_declared

    def _raiser() -> None:
        raise RuntimeError("المُعوِّضُ مُعطَّلٌ — فحصُ T9")

    def breaking_guard(self: Any, *args: Any, **kwargs: Any) -> Any:
        kwargs["compensators"] = tuple(
            Compensator(effect_signature=c.effect_signature, apply=_raiser, description="T9")
            for c in kwargs.get("compensators", ())
        )
        return original_guard(self, *args, **kwargs)

    monkeypatch.setattr(rulings_module.ConstitutionalAuthorizer, "guard_declared", breaking_guard)
    original = _drop_settle(monkeypatch, ledger, "T9")

    with pytest.raises(CompensationRequired) as caught:
        _issue(judiciary, judge_ctx, case_id)
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    monkeypatch.setattr(rulings_module.ConstitutionalAuthorizer, "guard_declared", original_guard)

    outcome = caught.value.outcome
    assert outcome.state_is_clean is False
    assert outcome.requires_human is True
    assert outcome.residual_signatures  # الباقي مُسمًّى لا مطويٌّ
    assert "يلزمُ قرارٌ بشريّ" in str(caught.value)
    # الحالةُ النصفيّةُ مُعلَنةٌ لا مُخفاةٌ: الصفُّ باقٍ والذرّيّةُ مُغلَقةٌ نهائيًّا
    assert _ruling_rows(case_id)[0] == 1
    record = ledger.get(_ruling_key(case_id))
    assert record is not None
    assert record.status is OperationStatus.FAILED_FINAL
    assert tuple(record.applied_effect_signatures) == tuple(outcome.residual_signatures)

    # والإعادةُ مرفوضةٌ: لا أثرَ فوقَ أثرٍ باقٍ (لا تُطبَّقُ الصفوفُ مرّتين)
    _next_second()
    with pytest.raises((IdempotencyError, DuplicateRulingError)):
        _issue(judiciary, judge_ctx, case_id)
    assert _ruling_rows(case_id)[0] == 1


# ── T10 · الحلقةُ الثانيةُ — لا يُعادُ سجلُّ تعويضٍ مُغلَقٌ بلا عكسٍ ─────────────


def test_wi105_t10_second_failed_episode_compensates_again(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired

    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t10")
    status_before = _ruling_rows(case_id)[2]
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T10")

    ids: list[str] = []
    for _episode in range(2):
        with pytest.raises(CompensationRequired) as caught:
            _issue(judiciary, judge_ctx, case_id)
        assert caught.value.outcome.state_is_clean is True
        # كلُّ حلقةٍ تعكسُ صفوفَها فعلًا — القياسُ على القاعدةِ لا على الادّعاء
        assert _ruling_rows(case_id) == (0, 0, status_before)
        ids.append(caught.value.outcome.record.compensation_id)
        _next_second()
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    assert ids[0] != ids[1]  # حلقتانِ بسجلَّينِ لا سجلٌّ مُعادٌ
    _issue(judiciary, judge_ctx, case_id)
    assert _ruling_rows(case_id)[:2] == (1, 1)
