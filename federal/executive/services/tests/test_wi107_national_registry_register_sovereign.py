"""
WI-107 · R1 — أسطحُ `national_registry/service.py` التسعةُ تعبرُ الحدَّ السياديَّ
بفاعلٍ تنفيذيٍّ مُعلَنٍ بالفعلِ `register` (قرارُ المالكِ D17-3 · سؤالُ Q-2 المعلَّقُ).

الهدف: إثباتُ أنَّ كلَّ سطحٍ عامٍّ مُغيِّرٍ في الوحدةِ يعبرُ الحدَّ بالفعلِ نفسِه وبالفاعلِ
       الثابتِ في الوحدةِ، وأنَّ الكتابةَ كلَّها خلفَ الحدِّ (لا صفَّ يُكتَبُ إن رُفِضَ)،
       وأنَّ المُعوِّضَ يستعيدُ الحالةَ كما كانت، وأنَّ الإعادةَ على مفتاحٍ طبيعيٍّ تُرفَعُ صريحةً.
النطاق: قياسُ سلوكِ الوحدةِ عبرَ الحدِّ وحدَه — لا تعديلَ للبوابةِ ولا للقواعدِ ولا لـ
        `test_r7c_national_registry.py` ولا `test_2b_state_registry_sovereign.py` (بلا تعديلٍ).
المالك: federal/executive/services — WI-107 (تصميمُ docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md
        المُلتزَمُ قبلَ الشِّفرةِ في W-623، والشِّفرةُ في W-625).
تاريخ الإنشاء: 2026-10-23 (WI-107 · الدفعةُ R1)

الفحوصُ كما وردتْ في التصميمِ (§ 4) — T1–T8:
- T1 · العبورُ: الأسطحُ التسعةُ كلُّها ⇒ 9 عمليّاتٍ متمايزةً بالفعلِ `register` وALLOW.
- T2 · الفاعلُ مُعلَنٌ لا مُثبَّتٌ (تصحيحٌ مؤرَّخٌ W-625): `register` مُنطَّقٌ لا حصريٌّ
        (مسبارُ W-623) فتبديلُ الثابتِ لا يُرفضُ — المقيسُ أنّ فاعلَ العبورِ يسري من
        ثابتِ الوحدةِ إلى سجلِّ البوّابةِ (LEGISLATIVE فوقَ الاختبارِ).
- T3 · لا كتابةَ خارجَ المُطبِّقِ: حكمُ رفضٍ حقيقيٌّ من المحرّكِ يُحاكى في `gateway.decide`
        (نمطُ 2B) ⇒ لكلِّ سطحٍ: الصفوفُ والأعمدةُ كما كانت.
- T4 · المُعوِّضُ على الإنشاءِ (`create_identity`) · T5 · على التحديثِ (`revoke_assignment`).
- T6 · الإعادةُ: (أ) الربطُ القائمُ نفسُهُ ⇒ `created: False` بلا عبورٍ ثانٍ ·
        (ب) على مستوى الحدِّ ⇒ `is_replay` و`RegistryReplayError` صريحًا ·
        (ج) الاسمُ نفسُهُ في مستأجرينِ مختلفَينِ ليسَ إعادةً (المفتاحُ بيشملُ المستأجرَ).
- T7 · الجردُ: 9 عامًّا في الوحدةِ كلُّها عابرةٌ · T8 · الثابتانِ.

الحدُّ المُعلَنُ: لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذِ (§ 4.3) — ملفُّ قياسٍ لا حُكمِ مراجعةٍ.

الدليلُ المُعادُ تشغيلُه (من federal/executive/services):
    ../../../.venv/bin/python -m pytest tests/test_wi107_national_registry_register_sovereign.py -q
"""

from __future__ import annotations

import importlib.util
import math
import sys
import time
import uuid
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any, Iterator

import pytest
from sqlalchemy import create_engine, delete, select

from amos_federation.common.database import get_database_url, get_session_factory, init_db
from amos_federation.common.principal import (
    DEFAULT_TENANT,
    AuthorizationContext,
    Principal,
)
from amos_federation.services.executive_core.agent_identity import register_identity
from amos_federation.services.national_registry import service as national_registry_module
from amos_federation.services.national_registry.models import (
    GRANTABLE_OPERATIONS,
    AuthorityGrantModel,
    IdentityAgentModel,
    IdentityModel,
    IdentityPrincipalModel,
    OfficialPositionModel,
    PositionModel,
    DecisionProvenanceModel,
    TransactionAuthorityModel,
)
from amos_federation.services.national_registry.service import (
    REGISTRY_ACTOR,
    REGISTRY_VERB,
    RegistryReplayError,
    get_national_registry,
    reset_national_registry,
)
from amos_federation.services.state_registry.models import (
    DepartmentModel,
    InstitutionModel,
    OfficialModel,
)
from amos_federation.services.state_registry.service import (
    get_state_registry,
    reset_state_registry,
)
from amos_federation.services.state_treasury.models import LedgerEntryModel
from tests.conftest import purge_agents, purge_tasks

#: الأسطحُ التسعةُ المقيسةُ بعدَ الشِّفرةِ (جردُ evidence/W-623 + تعديلاتُ W-625).
EXPECTED_OPERATIONS = frozenset(
    {
        "NationalRegistry.create_identity",
        "NationalRegistry.set_identity_status",
        "NationalRegistry.link_principal",
        "NationalRegistry.link_agent",
        "NationalRegistry.create_position",
        "NationalRegistry.assign_position",
        "NationalRegistry.revoke_assignment",
        "NationalRegistry.grant_authority",
        "NationalRegistry.revoke_authority",
    }
)

_MODELS = (
    AuthorityGrantModel,
    OfficialPositionModel,
    PositionModel,
    IdentityAgentModel,
    IdentityPrincipalModel,
    IdentityModel,
)
_STATE_MODELS = (
    OfficialModel,
    DepartmentModel,
    InstitutionModel,
)

def _purge_registry_state() -> None:
    """مسحٌ شاملٌ لكلِّ جداولِ قاعدةِ الفحصِ — من الفاحصِ لا من نماذجِ ORM.

    جداولُ الخدماتِ موزَّعةٌ على عدةِّ `Base` — فالترتيبُ من نماذجِ ORM ناقصٌ
    (قِيسَ في W-625: `DELETE FROM state_institutions` يُرفَضُ بقيودٍ من حساباتٍ
    خلَّفها ملفٌّ سابقٌ). فالفاحصُ يعدِّدُ الجداولِ الفعليةَ كلَّها، والمسحُ
    الكليُّ في اتصالٍ واحدٍ مخصَّصٍ معَ تعطيلِ فرضِ المفاتيحِ فيه لا يُخلِّفُ
    يتيمًا — وهو عينُ ما يفعلهُ حذفُ ملفِّ القاعدةِ نفسِه في بدايةِ الجلسةِ
    (`pytest_sessionstart`)، بلا إعادةِ إنشاءِ المخطَّطِ.
    """
    from sqlalchemy import inspect as sa_inspect, text as sa_text

    init_db()
    session = get_session_factory()()
    try:
        session.execute(sa_text("PRAGMA foreign_keys=OFF"))
        for table in sa_inspect(session.get_bind()).get_table_names():
            session.execute(sa_text(f'DELETE FROM "{table}"'))  # noqa: S608 — اسمٌ من الفاحصِ
        session.commit()
    finally:
        session.close()

_KING_PERMISSIONS = ("*",)


@pytest.fixture(autouse=True)
def _fresh_registry(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """جداولُ الوحدتينِ نظيفةٌ قبلَ كلِّ فحصٍ وبعدَه · والمُفوِّضُ المحفوظُ مُفرَغٌ (D1).

    وسجلُّ الذرّيّةِ **معزولٌ لكلِّ فحصٍ** (توجيهُ المستشارِ في W-625): المسارُ
    يُقرأُ من البيئةِ عندَ بناءِ الحدِّ، فتوجيهُهُ إلى ملفٍّ مؤقّتٍ يعزلُ الفحوصَ
    عن سجلِّ التشغيلِ الدائمِ — لا مسحَ لملفِّ `.runtime` لحلِّ مشكلةِ اختبارٍ.
    """
    monkeypatch.setenv(
        "AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER", str(tmp_path / "wi107-idempotency.json")
    )
    _purge_registry_state()
    reset_state_registry()
    reset_national_registry()
    national_registry_module.reset_registry_authorizer()
    yield
    _purge_registry_state()
    reset_state_registry()
    reset_national_registry()
    national_registry_module.reset_registry_authorizer()


class RecordingRegistryAuthorizer(national_registry_module.ConstitutionalAuthorizer):
    """يسجّلُ كلَّ عبورٍ (اسمَ العمليّةِ والدليلَ) — لقياسِ العبورِ لا لاتخاذِ قرارٍ."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.crossings: list[tuple[str, Any]] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.crossings.append(((kwargs.get("metadata") or {}).get("operation", ""), guarded))
        return guarded


def _install_recording_authorizer() -> RecordingRegistryAuthorizer:
    """مُصرِّحٌ مسجِّلٌ بثابتِ الوحدةِ نفسِه — المسارُ الإنتاجيُّ كما هو (D1)."""
    authorizer = RecordingRegistryAuthorizer(actor=national_registry_module.REGISTRY_ACTOR)
    national_registry_module._DEFAULT_REGISTRY_AUTHORIZER = authorizer
    return authorizer


def _context(role_id: str = "king", tenant_id: str = DEFAULT_TENANT) -> AuthorizationContext:
    """سياقٌ مُتحقَّقٌ منه بدورٍ وصلاحيّاتٍ صريحة — لا ادّعاءَ دورٍ من الطلب.

    الاسمُ فريدٌ في كلّ استدعاءٍ: مفتاحُ `link_principal` الطبيعيّ على `principal_id`
    وسجلُّ الذرّيّةِ ملفٌّ ثابتٌ — فتكرارُ الاسمِ بينَ الفحوصِ يُصبحُ إعادةً مرفوضةً
    لا علاقةَ لها بالمقيسِ (D6).
    """
    suffix = uuid.uuid4().hex[:8]
    return AuthorizationContext.from_principal(
        Principal.from_session_record(
            session_id=f"wi107-{role_id}-{suffix}",
            username=f"{role_id}-{suffix}",
            role_id=role_id,
            permissions=_KING_PERMISSIONS,
            expires_at=datetime.now(UTC) + timedelta(hours=1),
            tenant_id=tenant_id,
        )
    )


def _crown() -> AuthorizationContext:
    """التاج — `*` فيمرّ في كل حدّ عبر `has_permission` نفسها."""
    return _context("king")


def _code(prefix: str) -> str:
    return f"{prefix}-WI107-{uuid.uuid4().hex[:8].upper()}"


def _agent() -> str:
    """وكيلٌ حقيقيٌّ في `agents` — سجلّ R4 الكانوني، ولا يُنشئه السجلّ الوطني."""
    agent_id = f"agent-wi107-{uuid.uuid4().hex[:10]}"
    register_identity(agent_id, f"وكيل {agent_id}", "executor", tenant_id=DEFAULT_TENANT)
    return agent_id


def _count(model: type) -> int:
    session = get_session_factory()()
    try:
        return len(session.execute(select(model)).scalars().all())
    finally:
        session.close()


def _snapshot() -> dict[str, list[tuple[Any, ...]]]:
    """لقطةُ صفوفِ الوحدتينِ بأعمدتها — للمقارنةِ قبلَ الرفضِ وبعدَه (T3)."""
    session = get_session_factory()()
    try:
        out: dict[str, list[tuple[Any, ...]]] = {}
        for model in (*_STATE_MODELS, *_MODELS):
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


class _Chain:
    """سلسلةٌ كاملة جاهزة: مؤسسة · مسؤول · هوية · منصب · تقليد · مِنحة."""

    def __init__(self, **kwargs: object) -> None:
        self.__dict__.update(kwargs)


def _chain(crown: AuthorizationContext) -> _Chain:
    """ابنِ السلسلةَ بالعملياتِ الحقيقيةِ — لا صفوفًا مزروعةً يدويًّا.

    الترتيبُ كترتيبِ `test_r7c_national_registry._chain`: المؤسسةُ قبلَ المسؤولِ قبلَ
    الهويةِ قبلَ المنصبِ قبلَ التقليدِ — فكلُّ سطحٍ يعبُرُ بعبورِهِ المستقلِّ (D8).
    """
    state = get_state_registry()
    national = get_national_registry()
    institution = state.register_institution(
        context=crown,
        code=_code("INST"),
        name="وزارةُ قياسِ R1",
        kind="ministry",
        branch="executive",
    )
    agent_id = _agent()
    official = state.appoint_official(
        context=crown,
        agent_id=agent_id,
        institution_code=institution["code"],
        title="أمينُ الخزانة",
    )
    identity = national.create_identity(
        context=crown, identity_type="PERSON", label="أمينُ الخزانة"
    )
    national.link_principal(
        context=crown, principal_id=crown.principal_id, identity_id=identity["id"]
    )
    national.link_agent(context=crown, agent_id=agent_id, identity_id=identity["id"])
    position = national.create_position(
        context=crown,
        code=_code("POS"),
        title="أمينُ الخزانة",
        institution_code=institution["code"],
        authority_scope="INSTITUTION",
    )
    assignment = national.assign_position(
        context=crown, official_id=official["id"], position_id=position["id"]
    )
    grant = national.grant_authority(
        context=crown,
        position_id=position["id"],
        operation=GRANTABLE_OPERATIONS[0],
        scope="INSTITUTION",
    )
    return _Chain(
        institution=institution,
        agent_id=agent_id,
        official=official,
        identity=identity,
        position=position,
        assignment=assignment,
        grant=grant,
    )


def _exercise_all_surfaces(crown: AuthorizationContext) -> None:
    """استدعاءُ الأسطحِ التسعةِ كلِّها مرّةً — بالواجهةِ العامّةِ كما هي."""
    state = get_state_registry()
    national = get_national_registry()
    chain = _chain(crown)

    # بقايا السلسلةِ: الحالةُ والعزلُ والسحبُ — أسطحُ التحديثِ الثلاثةُ
    national.set_identity_status(
        context=crown, identity_id=chain.identity["id"], status="suspended", reason="قياسُ T1"
    )
    national.revoke_assignment(
        context=crown, assignment_id=chain.assignment["id"], reason="قياسُ T1"
    )
    national.revoke_authority(
        context=crown, grant_id=chain.grant["id"], reason="قياسُ T1"
    )


# ── T1 · العبورُ: تسعُ عمليّاتٍ بالفعلِ register ──────────────────────────────


def test_wi107_t1_every_surface_crosses_as_register() -> None:
    authorizer = _install_recording_authorizer()
    crown = _crown()
    _exercise_all_surfaces(crown)

    operations = {name for name, _ in authorizer.crossings}
    assert operations == EXPECTED_OPERATIONS
    for name, guarded in authorizer.crossings:
        evidence = guarded.evidence.as_dict()
        assert evidence["action"] == "register", name
        assert evidence["decision"] == "ALLOW", name
        assert evidence["target"].startswith("registry/"), name
    record = authorizer.gateway.records[-1]
    assert record.action == "register"
    assert record.actor == "executive"


# ── T2 · الفاعلُ ثابتُ الوحدةِ — تبديلُه يُسقِطُ العبورَ ───────────────────────


def test_wi107_t2_declared_actor_flows_from_the_unit_constant(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """تصحيحٌ مؤرّخٌ (W-625): مسبارُ W-623 أثبتَ أنّ `register` مُنطّقٌ لا حصريٌّ —
    فتبديلُ الفاعلِ لا يُرفضُ (بخلافِ `coordinate` في F1). فالمقيسُ هنا جوهرُ D1:
    الفاعلُ **مُعلَنٌ في الوحدةِ** يسري على العبورِ كلِّه — ليس معاملًا للمُنادي ولا
    مثبتًا في نداءِ الحدّ — والرفضُ الحقيقيّ يُقاسُ في T3 بحكمِ محرّكٍ صريحٍ.
    """
    crown = _crown()
    monkeypatch.setattr(national_registry_module, "REGISTRY_ACTOR", "LEGISLATIVE")
    national_registry_module.reset_registry_authorizer()

    # لا مُصرِّحٌ مُحقونٌ هنا (توجيهُ المستشارِ): المسارُ الإنتاجيُّ نفسُهُ يبني
    # المُصرِّحَ عندَ أوّلِ عبورٍ، فسجلُّ البوّابةِ يُقرأُ من كائنِ الإنتاجِ
    national = get_national_registry()
    identity = national.create_identity(
        context=crown, identity_type="PERSON", label="فاعلٌ مُعلَنٌ"
    )
    link = national.link_principal(
        context=crown,
        principal_id=f"pid-wi107-t2-{uuid.uuid4().hex[:8]}",
        identity_id=identity["id"],
    )
    assert _count(IdentityModel) == 1
    assert _count(IdentityPrincipalModel) == 1
    assert link["created"] is True

    # السطحانِ اللذانِ نصَّ عليهما التصميمُ (create_identity وlink_principal)
    # عبَرا بمُصرِّحِ الإنتاجِ وفاعلِهِ من ثابتِ الوحدةِ المُبدَّلِ فوقَ الاختبارِ
    authorizer = national_registry_module._registry_authorizer()
    records = authorizer.gateway.records
    assert len(records) >= 2
    for record in records:
        assert record.actor.lower() == "legislative", "الفاعلُ لا يسري من ثابتِ الوحدةِ"
    assert any(r.action == "register" for r in records)


# ── T3 · لا كتابةَ خارجَ المُطبِّقِ — لكلِّ سطحٍ ───────────────────────────────


def _real_denial_verdict() -> Any:
    """حكمُ رفضٍ **حقيقيٌّ** من المحرّكِ الدستوريّ نفسِه — لا نصٌّ مُصطنَع (نمطُ 2B).

    يُقرأُ على فعلٍ حصريٍّ لفاعلٍ لا يملكُه (المادةُ الثالثةُ · R-003-1)، ويُستعملُ
    ليُقاسَ **تصرّفُ الخدمةِ عندَ الرفضِ**، لا ليُقاسَ الدستورُ من جديد.
    """
    from core.constitutional_engine.engine import ConstitutionalEngine
    from core.constitutional_engine.model import ActionRequest, Branch

    return ConstitutionalEngine().evaluate(
        ActionRequest(actor=Branch.EXECUTIVE, action="allocate_budget", target="probe"),
        record=False,
    )


def test_wi107_t3_denied_crossing_leaves_every_surface_untouched(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    # التحضيرُ بالفاعلِ الصحيحِ: كيانٌ قائمٌ لكلِّ سطحٍ، وسلسلةٌ كاملةٌ
    crown = _crown()
    state = get_state_registry()
    national = get_national_registry()
    chain = _chain(crown)
    spare_identity = national.create_identity(
        context=crown, identity_type="PERSON", label="احتياطيّة"
    )
    spare_agent = _agent()
    spare_position = national.create_position(
        context=crown,
        code=_code("POS"),
        title="احتياطيّ",
        institution_code=chain.institution["code"],
        authority_scope="INSTITUTION",
    )
    before = _snapshot()

    # الرفضُ يُحاكى في موضعِهِ الحقيقيّ (`gateway.decide`) بحكمٍ حقيقيٍّ من
    # المحرّكِ — لا بتعطيلِ الحدّ ولا باستبدالِهِ (نمطُ 2B · تصحيحٌ مؤرّخٌ W-625:
    # مسبارُ W-623 أثبتَ أنّ تبديلَ الفاعلِ لا يرفضُ `register` فالرفضُ يُقرأُ صريحًا)
    authorizer = _install_recording_authorizer()
    denial = _real_denial_verdict()
    assert denial.decision.name == "DENY", "لم يُقرأْ حكمُ رفضٍ حقيقيٍّ من الدستور."

    def _deny(*_args: Any, **_kwargs: Any) -> None:
        raise SovereigntyViolation(denial)

    monkeypatch.setattr(authorizer.gateway, "decide", _deny)

    calls = [
        lambda: national.create_identity(context=crown, identity_type="PERSON", label="x"),
        lambda: national.set_identity_status(
            context=crown, identity_id=chain.identity["id"], status="suspended", reason="x"
        ),
        lambda: national.link_principal(
            context=crown, principal_id=f"pid-wi107-{uuid.uuid4().hex[:8]}",
            identity_id=spare_identity["id"],
        ),
        lambda: national.link_agent(
            context=crown, agent_id=spare_agent, identity_id=spare_identity["id"]
        ),
        lambda: national.create_position(
            context=crown, code=_code("POS"), title="x",
            institution_code=chain.institution["code"], authority_scope="INSTITUTION",
        ),
        lambda: national.assign_position(
            context=crown, official_id=chain.official["id"], position_id=spare_position["id"]
        ),
        lambda: national.revoke_assignment(
            context=crown, assignment_id=chain.assignment["id"], reason="x"
        ),
        lambda: national.grant_authority(
            context=crown, position_id=chain.position["id"],
            operation=GRANTABLE_OPERATIONS[-1], scope="INSTITUTION",
        ),
        lambda: national.revoke_authority(
            context=crown, grant_id=chain.grant["id"], reason="x"
        ),
    ]
    assert len(calls) == len(EXPECTED_OPERATIONS)
    for call in calls:
        with pytest.raises(SovereigntyViolation):
            call()

    assert _snapshot() == before


# ── T4 · المُعوِّضُ على الإنشاءِ ─────────────────────────────────────────────


def test_wi107_t4_compensator_removes_created_identity(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired
    from core.sovereignty.idempotency import OperationStatus

    crown = _crown()
    # لا مُصرِّحٌ مُحقونٌ (توجيهُ المستشارِ): يُلتقطُ مفتاحُ العمليّةِ الفعليُّ
    # بلفٍّ يُفوِّضُ التنفيذَ الأصليَّ — فالقياسُ على مفتاحِ هذه العمليّةِ تحديدًا
    authorizer = national_registry_module._registry_authorizer()
    ledger = authorizer.boundary.idempotency_ledger
    captured: dict[str, Any] = {}
    original_guard = authorizer.guard_declared

    def _capturing_guard(*args: Any, **kwargs: Any) -> Any:
        captured["key"] = kwargs.get("operation_key")
        return original_guard(*args, **kwargs)

    monkeypatch.setattr(authorizer, "guard_declared", _capturing_guard)
    original = _drop_settle(monkeypatch, ledger, "T4")
    with pytest.raises(CompensationRequired) as caught:
        get_national_registry().create_identity(
            context=crown, identity_type="PERSON", label="مُعوَّضٌ"
        )
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    monkeypatch.setattr(authorizer, "guard_declared", original_guard)

    assert caught.value.outcome.state_is_clean is True
    assert caught.value.outcome.requires_human is False
    assert _count(IdentityModel) == 0
    # السجلُّ الإضافيُّ يشهدُ: فاشلةٌ قابلةٌ للإعادةِ — لا ناجحةً كاذبةً
    assert captured["key"] is not None, "لم يُلتقطْ مفتاحُ العمليّةِ الفاشلةِ"
    record = ledger.get(captured["key"])
    assert record is not None, "السجلُّ الإضافيُّ لم يشهدْ العمليّةَ الفاشلةَ"
    assert record.status is OperationStatus.FAILED_RETRYABLE
    assert record.key.scope == "registry.NationalRegistry.create_identity"

    # نداءٌ جديدٌ بعدَ التعويضِ ينجحُ (مفتاحُهُ جديدٌ بمعرّفِ استدعاءٍ — إثباتُ
    # الإعادةِ على المفتاحِ نفسِهِ فيما بعدُ هو T5): البوّابةُ لا تُعاقِبُ من
    # عُوِّضَ أثرُهُ، والمُعوِّضُ لم يتركْ صفًّا يتيمًا
    _next_second()
    identity = get_national_registry().create_identity(
        context=crown, identity_type="PERSON", label="نداءٌ جديدٌ بعدَ التعويضِ"
    )
    assert _count(IdentityModel) == 1
    assert identity["status"] == "active"


# ── T5 · المُعوِّضُ على التحديثِ ─────────────────────────────────────────────


def _assignment_fields(assignment_id: str) -> tuple[Any, Any, Any]:
    """أعمدةُ صفِّ التقليدِ من القاعدةِ — جلسةٌ واحدةٌ تُفتَحُ وتُغلَقُ نفسُها."""
    session = get_session_factory()()
    try:
        row = session.get(OfficialPositionModel, assignment_id)
        assert row is not None
        return (row.status, row.revoked_at, row.revocation_reason)
    finally:
        session.close()


def test_wi107_t5_compensator_restores_revoked_assignment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired
    from core.sovereignty.idempotency import IdempotencyKey, OperationStatus

    _install_recording_authorizer()
    crown = _crown()
    chain = _chain(crown)
    assignment_id = chain.assignment["id"]
    ledger = national_registry_module._registry_authorizer().boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T5")
    with pytest.raises(CompensationRequired) as caught:
        get_national_registry().revoke_assignment(
            context=crown, assignment_id=assignment_id, reason="قياسُ T5"
        )
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    assert caught.value.outcome.state_is_clean is True
    # كلُّ الأعمدةِ التي يُلزمُ المُعوِّضُ استعادتَها (توجيهُ المستشارِ): الحالةُ
    # ووقتُ العزلِ وسببهُ — لا الحالةَ وحدها. والجلسةُ تُفتَحُ وتُغلَقُ نفسُها
    assert _assignment_fields(assignment_id) == ("active", None, ""), (
        "المُعوِّضُ لم يُرجِعْ الصفَّ كما كان"
    )
    record = ledger.get(
        IdempotencyKey(
            scope="registry.NationalRegistry.revoke_assignment",
            value=f"assignments/{assignment_id}/revoke",
        )
    )
    assert record is not None and record.status is OperationStatus.FAILED_RETRYABLE

    _next_second()
    revoked = get_national_registry().revoke_assignment(
        context=crown, assignment_id=assignment_id, reason="قياسُ T5"
    )
    assert revoked["changed"] is True
    status, revoked_at, revocation_reason = _assignment_fields(assignment_id)
    assert status == "revoked"
    assert revoked_at is not None
    assert revocation_reason == "قياسُ T5"


# ── T6 · الإعادةُ الطبيعيّةُ مرفوعةٌ صريحةً ─────────────────────────────────


def test_wi107_t6_second_link_is_refused_without_second_write() -> None:
    authorizer = _install_recording_authorizer()
    crown = _crown()
    national = get_national_registry()
    identity = national.create_identity(
        context=crown, identity_type="PERSON", label="ربطٌ واحدٌ"
    )
    principal_id = f"pid-wi107-{uuid.uuid4().hex[:8]}"
    first = national.link_principal(
        context=crown, principal_id=principal_id, identity_id=identity["id"]
    )
    assert first["created"] is True
    link_id = first["id"]
    links_before = _count(IdentityPrincipalModel)
    crossings_before = len(authorizer.crossings)

    # (أ) الربطُ القائمُ نفسُهُ يُرجِعُ الردَّ الخاملَ **قبلَ العبورِ** (D5)
    second = national.link_principal(
        context=crown, principal_id=principal_id, identity_id=identity["id"]
    )
    assert second["created"] is False
    assert second["id"] == link_id
    assert _count(IdentityPrincipalModel) == links_before
    assert len(authorizer.crossings) == crossings_before, "الردُّ الخاملُ عبرَ الحدَّ"

    # (ب) على مستوى الحدِّ: مفتاحٌ طبيعيٌّ مُعادٌ ⇒ إعادةٌ تُرفَعُ صريحةً (D6)
    undo = national_registry_module._RegistryUndo()
    target, crossing = national_registry_module._crossing(
        "NationalRegistry.link_principal",
        "CREATE",
        f"principals/{DEFAULT_TENANT}/{principal_id}/link",
        "قياسُ الإعادةِ على مستوى الحدِّ",
        undo,
    )
    guarded = authorizer.guard_declared(
        national_registry_module.REGISTRY_VERB, target, applier=lambda _effect: {}, **crossing
    )
    assert guarded.is_replay
    with pytest.raises(RegistryReplayError):
        national_registry_module._refuse_replay(guarded, "NationalRegistry.link_principal", target)


    # (ج) الاسمُ نفسُهُ في مستأجرينِ مختلفَينِ ليسَ إعادةً (تصحيحٌ مؤرَّخٌ W-625:
    # قيدُ القاعدةِ `UNIQUE (tenant_id, principal_id)` فالمفتاحُ الطبيعيُّ يشملُ
    # المستأجرَ — ولو لم يشملْهُ لحَجَبَ سجلُّ الذرّيّةِ الربطَ الثانيَ ظلمًا)
    tenant_a = _crown()
    tenant_b = _context("king", tenant_id=f"tenant-wi107-{uuid.uuid4().hex[:8]}")
    identity_b = national.create_identity(
        context=tenant_b, identity_type="PERSON", label="هويةُ المستأجرِ الثاني"
    )
    shared_name = f"shared-{uuid.uuid4().hex[:8]}"
    first = national.link_principal(
        context=tenant_a, principal_id=shared_name, identity_id=identity["id"]
    )
    second = national.link_principal(
        context=tenant_b, principal_id=shared_name, identity_id=identity_b["id"]
    )
    assert first["created"] is True
    assert second["created"] is True, "ربطُ الاسمِ نفسِهِ في مستأجرٍ آخرَ حُجِبَ كإعادةٍ"


# ── T7 · الجردُ: الوحدةُ بلا دَينٍ ────────────────────────────────────────────

# ── T7 · الجردُ: الوحدةُ بلا دَينٍ ────────────────────────────────────────────


def _repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "audit" / "sovereign_write_inventory.py").is_file():
            return parent
    raise AssertionError("جذرُ المستودعِ غيرُ موجود")


def test_wi107_t7_inventory_counts_nine_guarded_and_zero_debt() -> None:
    root = _repo_root()
    tool = root / "tools" / "audit" / "sovereign_write_inventory.py"
    spec = importlib.util.spec_from_file_location("_wi107_inventory", tool)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    sites = [
        s for s in module.collect(root)
        if s.path.endswith("national_registry/service.py")
    ]
    public = [s for s in sites if s.public]
    assert {f"{s.owner}.{s.function}" for s in public} == EXPECTED_OPERATIONS
    assert all(s.guarded for s in public), [s.function for s in public if not s.guarded]


# ── T8 · الثابتانِ (D1 · D2) ──────────────────────────────────────────────────


def test_wi107_t8_actor_and_verb_constants() -> None:
    assert national_registry_module.REGISTRY_ACTOR == "EXECUTIVE"
    assert national_registry_module.REGISTRY_VERB == "register"
    assert national_registry_module._registry_authorizer()._actor == "EXECUTIVE"
    assert REGISTRY_ACTOR == "EXECUTIVE"
    assert REGISTRY_VERB == "register"


# ═══════════════════════════════════════════════════════════════════════════
# الأسطحُ القائمةُ لا تُمَسُّ — الاختباراتُ المرافقةُ تُشغَّلُ بلا تعديلٍ (التصميمُ § 3)
# ═══════════════════════════════════════════════════════════════════════════


def test_wi107_existing_r7c_suite_still_collects() -> None:
    """الملفُّ المرافقُ `test_r7c_national_registry.py` يُجمعُ كما هو — لا تعديلَ عليه."""
    path = Path(__file__).parent / "test_r7c_national_registry.py"
    assert path.is_file()
