"""
AMOS-Federation Federal Judiciary — Docket: Cases, Parties, Claims, Evidence, Proceedings
الهدف: دورةُ حياةٍ صريحةٌ للقضية، وأطرافٌ بهويّاتٍ لا بأسماء، وإجراءاتٌ مُرتَّبةٌ مفروضة
النطاق: services/federal_judiciary
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-17 (R7-D5/D6/D7/D8)

## دورة الحياة خريطةٌ لا نصّ (R7-D5)

    opened → filed → assigned → hearing → decided → enforcement → closed

و`ALLOWED_TRANSITIONS` قاموسٌ صريحٌ يُقرأ ويُختبَر. ولا انتقالَ قسريّ: لا وسيطَ
`force`، ولا دالّةَ `set_status` عامّة، ولا مسارَ يتخطّى الإسناد إلى الحكم. ومن
أراد تخطّيًا فليس له في هذه الوحدة طريق — وهذا هو المقصود من «لا `force`».

وثلاثةُ انتقالاتٍ لها شرطٌ زائدٌ على الخريطة:

| الانتقال | الشرط الزائد | لماذا |
| --- | --- | --- |
| `filed → assigned` | قاضٍ مُقلَّدٌ نشطٌ في محكمة القضية | لا إسنادَ إلى قاضٍ معزول أو من محكمةٍ أخرى |
| `hearing → decided` | يجري في `rulings.py` مع الحكم في حركةٍ واحدة | لا «مقضيّة» بلا حكمٍ مكتوب |
| `decided → enforcement` | يجري في `enforcement.py` مع أثر التنفيذ | لا «تنفيذ» بلا مهمّةٍ أو حركةٍ حقيقية |

## الطرف هويةٌ إلزامًا (R7-D6)

`add_party` لا يأخذ اسمًا: يأخذ `identity_id` ويقرأ الصفّ من `state_identities`
ويطلب أن يكون في المستأجر نفسه. فلا يستطيع مقدِّمُ الطلب أن يقول «خصمي فلان»
نصًّا. و`display_label` يُشتَقّ من الهوية أو يُمرَّر للعرض — ولا يُبحَث به.

## الدليلُ سجلُّ إيداعٍ لا سلسلة حيازة (R7-D7)

`submit_evidence` يقبل بصمةً اختيارية ويفرض طولها `64` (sha256) وأن تُذكَر
الخوارزمية معها. وما يُكتب: من أودع (مبدأً وهويةً)، ومتى، ونوعٌ ومصدرٌ وحالة.
وما **لا** يُدَّعى: حرزٌ مادّي، ولا سلسلةُ نقلٍ موقَّعة، ولا منعُ تغيير الأصل.
والدليل لا يُحذَف: `withdraw` تغييرُ حالةٍ بسببٍ مكتوب.

## الإجراءُ صفٌّ مُرتَّبٌ لا نصّ (R7-D8)

`record_proceeding` يحسب `sequence = max + 1` داخل القضية، والقيدُ الفريد
`(case_id, sequence)` يفرض الترتيب في القاعدة. فتاريخُ القضية سلسلةُ صفوفٍ
قابلةٌ للقراءة، لا حقلَ ملاحظاتٍ ينمو.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import func, select
from sqlalchemy import inspect as sa_inspect

from amos_federation.common.database import get_session_factory
from amos_federation.services.executive_core.sovereignty_bridge import (
    compensator,
    declared_effect,
    operation_key,
)
from amos_federation.services.federal_judiciary.jurisdiction import assert_jurisdiction_match
from amos_federation.services.federal_judiciary.models import (
    CASE_TYPES,
    CLAIM_TYPES,
    EVIDENCE_TYPES,
    LEGAL_BASIS_KINDS,
    PARTY_ROLES,
    PROCEEDING_TYPES,
    CaseClaimModel,
    CaseEvidenceModel,
    CasePartyModel,
    CaseProceedingModel,
    CourtJudgeModel,
    LegalCaseModel,
)
from amos_federation.services.federal_judiciary.registry import (
    JudiciaryError,
    load_court,
)
from amos_federation.services.national_registry.models import IdentityModel

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

#: خريطةُ الانتقالات المسموحة — المصدرُ الوحيد، ولا انتقالَ خارجها.
ALLOWED_TRANSITIONS: dict[str, tuple[str, ...]] = {
    "opened": ("filed",),
    "filed": ("assigned",),
    "assigned": ("hearing", "decided"),
    "hearing": ("decided",),
    "decided": ("enforcement", "closed"),
    "enforcement": ("closed",),
    "closed": (),
}


class CaseNotFoundError(JudiciaryError):
    """لا قضية بهذا المعرّف في هذا المستأجر."""


class CaseTransitionError(JudiciaryError):
    """انتقالُ حالةٍ غير مسموحٍ في خريطة دورة الحياة."""


class PartyIdentityError(JudiciaryError):
    """طرفٌ بلا هويةٍ كانونية — لا يُقبَل اسمٌ نصّيّ بديلًا."""


class EvidenceError(JudiciaryError):
    """إيداعُ دليلٍ مرفوض — بصمةٌ أو مصدرٌ أو حالةٌ لا تصلح."""


def _now() -> datetime:
    return datetime.now(UTC)


def _iso(value: datetime | None) -> str:
    return value.isoformat() if value else ""


def case_dict(row: LegalCaseModel) -> dict[str, Any]:
    return {
        "id": row.id,
        "reference": row.reference,
        "court_id": row.court_id,
        "jurisdiction": row.jurisdiction,
        "case_type": row.case_type,
        "subject": row.subject,
        "status": row.status,
        "opened_by_principal": row.opened_by_principal,
        "opened_by_identity_id": row.opened_by_identity_id,
        "assigned_judge_id": row.assigned_judge_id,
        "assigned_at": _iso(row.assigned_at),
        "opened_at": _iso(row.opened_at),
        "closed_at": _iso(row.closed_at),
        "closure_reason": row.closure_reason or "",
        "tenant_id": row.tenant_id,
    }


def party_dict(row: CasePartyModel) -> dict[str, Any]:
    return {
        "id": row.id,
        "case_id": row.case_id,
        "party_role": row.party_role,
        "identity_id": row.identity_id,
        "institution_id": row.institution_id,
        "display_label": row.display_label or "",
        "added_by": row.added_by,
        "tenant_id": row.tenant_id,
        "created_at": _iso(row.created_at),
    }


def claim_dict(row: CaseClaimModel) -> dict[str, Any]:
    return {
        "id": row.id,
        "case_id": row.case_id,
        "claimant_party_id": row.claimant_party_id,
        "claim_type": row.claim_type,
        "statement": row.statement,
        "legal_basis_kind": row.legal_basis_kind,
        "legal_basis_ref": row.legal_basis_ref or "",
        "legal_basis_verified": bool(row.legal_basis_verified),
        "amount": row.amount,
        "filed_by": row.filed_by,
        "tenant_id": row.tenant_id,
        "created_at": _iso(row.created_at),
    }


def evidence_dict(row: CaseEvidenceModel) -> dict[str, Any]:
    return {
        "id": row.id,
        "case_id": row.case_id,
        "evidence_type": row.evidence_type,
        "source": row.source,
        "content_hash": row.content_hash,
        "fingerprint_algo": row.fingerprint_algo or "",
        "submitted_by_principal": row.submitted_by_principal,
        "submitted_by_identity_id": row.submitted_by_identity_id,
        "submitted_at": _iso(row.submitted_at),
        "status": row.status,
        "status_reason": row.status_reason or "",
        "tenant_id": row.tenant_id,
    }


def proceeding_dict(row: CaseProceedingModel) -> dict[str, Any]:
    return {
        "id": row.id,
        "case_id": row.case_id,
        "sequence": row.sequence,
        "proceeding_type": row.proceeding_type,
        "actor_principal": row.actor_principal,
        "actor_identity_id": row.actor_identity_id,
        "summary": row.summary,
        "record": row.record or {},
        "status": row.status,
        "occurred_at": _iso(row.occurred_at),
        "tenant_id": row.tenant_id,
    }


# ── العبورُ السياديُّ (WI-111 · الدفعةُ J2+J3 · ملحقُ التصميمِ D1–D8) ─────────────
#
# الفاعلُ واحدٌ للوحدةِ: مُصرِّحُ J1 نفسُه (`rulings._judiciary_authorizer` · D1) —
# يُستورَدُ كسولًا لأنَّ `rulings` يستوردُ هذه الوحدةَ. وكلُّ عمليّةٍ عامّةٍ تعبرُ
# تحملُ نداءَ الحدِّ **في جسدِها** (هكذا يقيسُ الجردُ)، والمُساعداتُ هنا تبني
# المعاملاتِ فقط: الأثرَ والمفتاحَ والمُطبِّقَ والمُعوِّضَ وطلبَ الاختصاصِ.


class JudicialLedgerDivergenceError(JudiciaryError):
    """سجلُّ الذرّيّةِ يُثبِتُ العمليّةَ والصفُّ غائبٌ — استعادةٌ لا نجاحٌ يُزعَم (D6)."""


def _authorizer() -> Any:
    """مُصرِّحُ الوحدةِ القضائيّةِ الواحدُ (D1) — لا مُصرِّحَ ثانٍ."""
    from amos_federation.services.federal_judiciary.rulings import _judiciary_authorizer

    return _judiciary_authorizer()


def judicial_request(
    action: str,
    *,
    court: Any,
    case_scope: str,
    target: str,
    actor_scope: str | None = None,
    institution_id: str | None = None,
) -> Any:
    """طلبُ الاختصاصِ منَ البياناتِ الحيّةِ (D4) — نطاقُ المحكمةِ ونطاقُ القضيّةِ منَ الصفوفِ.

    `actor_scope` منصبُ القاضي المُثبَتُ حيثُ يُثبَتُ (`vacate_ruling`)؛ وإلّا فنطاقُ
    المحكمةِ **مُعلَنًا** — حدٌّ معلَنٌ في الملحقِ (D4): هذه الأسطحُ لا تُثبِتُ منصبًا
    اليومَ، فيصيرُ فحصُ المنصبِ عندَها تحصيلَ حاصلٍ لا ادّعاءَ إثباتٍ.
    """
    import sys as _sys

    from amos_federation.services.executive_core.sovereignty_bridge import locate_repo_root

    root = locate_repo_root()
    if str(root) not in _sys.path:
        _sys.path.insert(0, str(root))
    from core.sovereignty.jurisdiction import JudicialAction

    return JudicialAction(
        action=action,
        court_scope=court.jurisdiction,
        case_scope=case_scope,
        actor_scope=court.jurisdiction if actor_scope is None else actor_scope,
        target=target,
        institution_id=institution_id or court.institution_id,
        case_institution_id=court.institution_id,
        is_royal_decree_target=False,
    )


def _snapshot(row: Any) -> dict[str, Any]:
    """قيمُ الأعمدةِ كلِّها قبلَ العمليّةِ — يستعيدُها المُعوِّضُ حرفيًّا (D7)."""
    return {attr.key: getattr(row, attr.key) for attr in sa_inspect(row).mapper.column_attrs}


class Crossing:
    """معاملاتُ عبورٍ واحدٍ — يبنيها `_plan_crossing` ويُمرِّرُها النداءُ إلى الحدِّ."""

    def __init__(self, action: str, target: str, kwargs: dict[str, Any]) -> None:
        self.action = action
        self.target = target
        self.kwargs = kwargs


def _plan_crossing(
    session: Session,
    *,
    action: str,
    court: Any,
    case_scope: str,
    namespace: str,
    key: str,
    kind: str,
    description: str,
    mutate: Any,
    snapshots: tuple[Any, ...] = (),
    actor_scope: str | None = None,
    institution_id: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> Crossing:
    """ابنِ عبورًا: أثرٌ واحدٌ مُعلَنٌ · مفتاحٌ · مُطبِّقٌ يكتبُ ويلتزمُ · مُعوِّضٌ تقنيٌّ.

    `mutate(created)` يكتبُ في `session` ويُلحِقُ بـ`created` كلَّ صفٍّ يُدرِجُه
    (`(النموذج, المعرِّف)`)؛ و`snapshots` صفوفٌ قائمةٌ يُغيِّرُها — تُلتقَطُ قيمُها قبلَ
    الحدِّ ويُعيدُها المُعوِّضُ. والهدفُ يحملُ المفتاحَ (درسُ J1 D5: بصمةُ الإذنِ منَ
    الفاعلِ والفعلِ والهدفِ والآثارِ، فهدفٌ بلا هويّةِ العمليّةِ يتصادمُ في الثانيةِ نفسِها).
    """
    target = f"judiciary/{action}/{key}"
    effect = declared_effect(kind, target, description)
    before = [(type(row), row.id, _snapshot(row)) for row in snapshots]
    created: list[tuple[Any, str]] = []

    def _apply(_effect: Any) -> Any:
        """المُطبِّقُ — الكتابةُ والالتزامُ في معاملةٍ واحدةٍ خلفَ الحدِّ."""
        value = mutate(created)
        session.commit()
        return value

    def _restore() -> None:
        """المُعوِّضُ (D7): استعادةٌ تقنيّةٌ في جلسةٍ جديدةٍ — حذفُ المُدرَجِ وإرجاعُ المنقولِ.

        العمليّةُ لم تثبتْ (فشلٌ بعدَ الالتزامِ) فلا أثرَ قضائيًّا وُجِدَ؛ «الحذفُ شأنٌ
        تنفيذيّ» — والمُعوِّضُ ليس أثرًا مُعلَنًا، فيُكتَبُ ذلك صريحًا هنا كما في J1.
        """
        restore = get_session_factory()()
        try:
            for model, row_id in reversed(created):
                row = restore.get(model, row_id)
                if row is not None:
                    restore.delete(row)
            for model, row_id, values in before:
                row = restore.get(model, row_id)
                if row is not None:
                    for name, value in values.items():
                        setattr(row, name, value)
            restore.commit()
        finally:
            restore.close()

    kwargs: dict[str, Any] = {
        "declared_effects": (effect,),
        "applier": _apply,
        "operation_key": operation_key(namespace, key),
        "compensators": (
            compensator(
                effect.signature,
                _restore,
                "استعادةٌ تقنيّةٌ: حذفُ الصفوفِ المُدرَجةِ وإرجاعُ الحقولِ المنقولةِ "
                "إلى قيمِها قبلَ العمليّةِ — العمليّةُ لم تثبتْ",
            ),
        ),
        "metadata": {"key": key, **(metadata or {})},
        "judicial_action": judicial_request(
            action,
            court=court,
            case_scope=case_scope,
            target=target,
            actor_scope=actor_scope,
            institution_id=institution_id,
        ),
    }
    return Crossing(action, target, kwargs)


def crossed_value(guarded: Any, *, replay: Any, what: str) -> Any:
    """قيمةُ العبورِ — والإعادةُ تُقرأُ ولا تُكتَبُ (D6): إن غابَ الصفُّ فتفرُّقٌ صريحٌ."""
    if not guarded.is_replay:
        return guarded.value
    value = replay()
    if value is None:
        raise JudicialLedgerDivergenceError(
            f"سجلُّ الذرّيّةِ يُثبِتُ {what} ولا صفَّ قائمًا — استعادةٌ مطلوبةٌ لا نجاحٌ يُزعَم"
        )
    return value


def load_case(session: Session, case_id: str, *, tenant_id: str) -> LegalCaseModel:
    row = session.get(LegalCaseModel, case_id)
    if row is None or row.tenant_id != tenant_id:
        raise CaseNotFoundError(f"لا قضية بالمعرّف '{case_id}' في مستأجر '{tenant_id}'")
    return row


def _load_identity(session: Session, identity_id: str, *, tenant_id: str) -> IdentityModel:
    row = session.get(IdentityModel, identity_id)
    if row is None or row.tenant_id != tenant_id:
        raise PartyIdentityError(f"لا هوية كانونية بالمعرّف '{identity_id}' في مستأجر '{tenant_id}'")
    return row


def assert_transition(current: str, target: str) -> None:
    """اطلب أن يكون الانتقال في الخريطة — ولا استثناءَ ولا تخطّي.

    Raises:
        CaseTransitionError: الانتقالُ غير مسموح (بما فيه الانتقال إلى الحالة نفسها).
    """
    allowed = ALLOWED_TRANSITIONS.get(current)
    if allowed is None:  # pragma: no cover — يمنعه قيد `CHECK` على الحالة
        raise CaseTransitionError(f"حالةٌ غير معروفة '{current}'")
    if target not in allowed:
        readable = ", ".join(allowed) if allowed else "لا شيء"
        raise CaseTransitionError(
            f"انتقالٌ غير مسموح '{current}' → '{target}' — المسموح من '{current}': {readable}"
        )


def open_case(
    session: Session,
    *,
    court_id: str,
    case_type: str,
    subject: str,
    reference: str,
    opened_by_principal: str,
    opened_by_identity_id: str,
    tenant_id: str,
) -> LegalCaseModel:
    """افتح قضيةً في محكمةٍ نشطة بنطاقها هي — لا بنطاقٍ يختاره المُقدِّم.

    نطاقُ القضية **يُنسَخ من المحكمة** ثم يُفحَص بالمساواة: فلا يستطيع مُقدِّمُ
    الطلب أن يفتح قضيةً فدرالية في محكمة ولاية بتمرير حقلٍ في الطلب.
    """
    if case_type not in CASE_TYPES:
        raise JudiciaryError(f"نوعُ قضيةٍ غير معروف '{case_type}' — المسموح: {', '.join(CASE_TYPES)}")
    if not subject.strip():
        raise JudiciaryError("موضوعُ القضية لا يكون فارغًا")
    court = load_court(session, court_id, tenant_id=tenant_id)
    if court.status != "active":
        raise JudiciaryError(f"المحكمة '{court.code}' حالتها '{court.status}' — لا تُفتَح فيها قضية")
    _load_identity(session, opened_by_identity_id, tenant_id=tenant_id)

    assert_jurisdiction_match(
        court_jurisdiction=court.jurisdiction,
        case_jurisdiction=court.jurisdiction,
        court_institution_id=court.institution_id,
        case_institution_id=court.institution_id,
    )

    existing = session.execute(
        select(LegalCaseModel).where(
            LegalCaseModel.reference == reference, LegalCaseModel.tenant_id == tenant_id
        )
    ).scalar_one_or_none()
    if existing is not None:
        raise JudiciaryError(f"مرجعُ القضية '{reference}' مستعمَلٌ في مستأجر '{tenant_id}'")

    row = LegalCaseModel(
        id=f"lcs-{uuid.uuid4()}",
        reference=reference,
        court_id=court.id,
        jurisdiction=court.jurisdiction,
        case_type=case_type,
        subject=subject,
        status="opened",
        opened_by_principal=opened_by_principal,
        opened_by_identity_id=opened_by_identity_id,
        tenant_id=tenant_id,
    )

    def _insert(created: list[tuple[Any, str]]) -> LegalCaseModel:
        session.add(row)
        session.flush()
        created.append((LegalCaseModel, row.id))
        return row

    # `admit_case` (D17-2) · المفتاحُ (المستأجرُ · المرجعُ) — فريدٌ بقيدِ القاعدةِ (D6).
    plan = _plan_crossing(
        session,
        action="admit_case",
        court=court,
        case_scope=court.jurisdiction,
        namespace="judiciary.case.open",
        key=f"{tenant_id}:{reference}",
        kind="CREATE",
        description=f"قبولُ قضيّةٍ بالمرجعِ '{reference}' في المحكمةِ '{court.code}'",
        mutate=_insert,
    )
    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)
    return crossed_value(
        guarded,
        replay=lambda: session.execute(
            select(LegalCaseModel).where(
                LegalCaseModel.reference == reference, LegalCaseModel.tenant_id == tenant_id
            )
        ).scalar_one_or_none(),
        what=f"قبولَ القضيّةِ '{reference}'",
    )


def file_case(session: Session, *, case_id: str, tenant_id: str) -> LegalCaseModel:
    """`opened → filed` — القضية صارت مقيَّدةً رسميًّا في المحكمة."""
    row = load_case(session, case_id, tenant_id=tenant_id)
    assert_transition(row.status, "filed")
    row.status = "filed"
    session.flush()
    return row


def check_assign(
    session: Session, *, case_id: str, judge_id: str, tenant_id: str
) -> tuple[LegalCaseModel, CourtJudgeModel]:
    """فحوصُ الإسنادِ كلُّها — تُنادى قبلَ الحدِّ وفي الكاتبِ نفسِه (مصدرٌ واحدٌ)."""
    row = load_case(session, case_id, tenant_id=tenant_id)
    assert_transition(row.status, "assigned")
    judge = session.get(CourtJudgeModel, judge_id)
    if judge is None or judge.tenant_id != tenant_id:
        raise JudiciaryError(f"لا تقليدَ قضاءٍ بالمعرّف '{judge_id}' في مستأجر '{tenant_id}'")
    if judge.status != "active":
        raise JudiciaryError(f"القاضي حالتُه '{judge.status}' لا 'active' — لا إسنادَ إليه")
    if judge.court_id != row.court_id:
        raise JudiciaryError("القاضي مُقلَّدٌ في محكمةٍ أخرى — لا إسنادَ عبر المحاكم")
    return row, judge


def assign_case(session: Session, *, case_id: str, judge_id: str, tenant_id: str) -> LegalCaseModel:
    """`filed → assigned` بقاضٍ مُقلَّدٍ نشطٍ في محكمة القضية بالذات."""
    row, judge = check_assign(session, case_id=case_id, judge_id=judge_id, tenant_id=tenant_id)
    row.assigned_judge_id = judge.id
    row.assigned_at = _now()
    row.status = "assigned"
    session.flush()
    return row


def open_hearing(session: Session, *, case_id: str, tenant_id: str) -> LegalCaseModel:
    """`assigned → hearing`."""
    row = load_case(session, case_id, tenant_id=tenant_id)
    assert_transition(row.status, "hearing")
    row.status = "hearing"
    session.flush()
    return row


def advance_case(session: Session, *, case_id: str, target: str, tenant_id: str) -> LegalCaseModel:
    """انقُل القضية إلى حالةٍ مسموحةٍ في الخريطة — مدخلُ `rulings`/`enforcement`.

    ليست `set_status` عامّة: الخريطةُ تُفحَص، و`closed` يمرّ عبر `close_case` وحدها
    لأنها تلزمها `closed_at` وسببٌ مكتوب.
    """
    if target == "closed":
        raise CaseTransitionError("إغلاقُ القضية يجري بـ`close_case` وحدها — يلزمه سببٌ وطابع")
    row = load_case(session, case_id, tenant_id=tenant_id)
    assert_transition(row.status, target)
    row.status = target
    session.flush()
    return row


def check_close(session: Session, *, case_id: str, reason: str, tenant_id: str) -> LegalCaseModel:
    """فحوصُ الإغلاقِ — قبلَ الحدِّ وفي الكاتبِ نفسِه (مصدرٌ واحدٌ)."""
    if not reason.strip():
        raise JudiciaryError("إغلاقُ القضية يلزمه سببٌ مكتوب")
    row = load_case(session, case_id, tenant_id=tenant_id)
    assert_transition(row.status, "closed")
    return row


def close_case(
    session: Session, *, case_id: str, reason: str, tenant_id: str
) -> tuple[LegalCaseModel, str]:
    """`decided|enforcement → closed` بسببٍ مكتوبٍ وطابعِ إغلاق."""
    row = check_close(session, case_id=case_id, reason=reason, tenant_id=tenant_id)
    previous = row.status
    row.status = "closed"
    row.closed_at = _now()
    row.closure_reason = reason
    session.flush()
    return row, previous


def add_party(
    session: Session,
    *,
    case_id: str,
    party_role: str,
    identity_id: str,
    added_by: str,
    tenant_id: str,
    institution_id: str | None = None,
    display_label: str = "",
) -> CasePartyModel:
    """أضِف طرفًا بهويةٍ كانونية — ولا يُقبَل اسمٌ نصّيّ بديلًا عنها."""
    if party_role not in PARTY_ROLES:
        raise JudiciaryError(
            f"دورُ طرفٍ غير معروف '{party_role}' — المسموح: {', '.join(PARTY_ROLES)}"
        )
    case = load_case(session, case_id, tenant_id=tenant_id)
    if case.status == "closed":
        raise JudiciaryError("لا تُضاف أطرافٌ إلى قضيةٍ مُغلقة")
    identity = _load_identity(session, identity_id, tenant_id=tenant_id)

    duplicate = session.execute(
        select(CasePartyModel).where(
            CasePartyModel.case_id == case_id,
            CasePartyModel.identity_id == identity_id,
            CasePartyModel.party_role == party_role,
        )
    ).scalar_one_or_none()
    if duplicate is not None:
        raise JudiciaryError(f"هذه الهوية مُسجَّلةٌ أصلًا بدور '{party_role}' في القضية")

    row = CasePartyModel(
        id=f"cpt-{uuid.uuid4()}",
        case_id=case.id,
        party_role=party_role,
        identity_id=identity.id,
        institution_id=institution_id,
        display_label=display_label or (identity.label or ""),
        added_by=added_by,
        tenant_id=tenant_id,
    )

    def _insert(created: list[tuple[Any, str]]) -> CasePartyModel:
        session.add(row)
        session.flush()
        created.append((CasePartyModel, row.id))
        return row

    # `join_party` (D17-2) · المفتاحُ (القضيّةُ · الهويّةُ · الدورُ) — والمكرَّرُ رُفِضَ قبلَ الحدِّ.
    plan = _plan_crossing(
        session,
        action="join_party",
        court=load_court(session, case.court_id, tenant_id=tenant_id),
        case_scope=case.jurisdiction,
        namespace="judiciary.party.add",
        key=f"{case.id}:{identity.id}:{party_role}",
        kind="CREATE",
        description=f"ضمُّ طرفٍ بدورِ '{party_role}' إلى القضيّةِ '{case.reference}'",
        mutate=_insert,
    )
    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)
    return crossed_value(
        guarded,
        replay=lambda: session.execute(
            select(CasePartyModel).where(
                CasePartyModel.case_id == case.id,
                CasePartyModel.identity_id == identity.id,
                CasePartyModel.party_role == party_role,
            )
        ).scalar_one_or_none(),
        what=f"ضمَّ الطرفِ إلى القضيّةِ '{case.reference}'",
    )


def add_claim(
    session: Session,
    *,
    case_id: str,
    claimant_party_id: str,
    claim_type: str,
    statement: str,
    filed_by: str,
    tenant_id: str,
    legal_basis_kind: str = "NONE",
    legal_basis_ref: str = "",
    amount: str | None = None,
) -> CaseClaimModel:
    """أضِف مطالبةً لطرفٍ في القضية — والمرجعُ القانونيّ **غير محقَّق** افتراضًا.

    `legal_basis_verified` يبقى `False` دائمًا في هذه الوحدة: لا سجلَّ نصوصٍ
    قانونية تنفيذيًّا يُقرأ منه المرجع، فرفعُ العَلَم سيكون ادّعاءً. وهذا مكتوبٌ
    كدَينٍ صريحٍ لا كنقصٍ مُخفى.
    """
    if claim_type not in CLAIM_TYPES:
        raise JudiciaryError(f"نوعُ مطالبةٍ غير معروف '{claim_type}'")
    if legal_basis_kind not in LEGAL_BASIS_KINDS:
        raise JudiciaryError(f"نوعُ مرجعٍ قانونيّ غير معروف '{legal_basis_kind}'")
    if not statement.strip():
        raise JudiciaryError("نصُّ المطالبة لا يكون فارغًا")
    if legal_basis_kind == "NONE" and legal_basis_ref:
        raise JudiciaryError("مرجعٌ قانونيّ بلا نوعٍ — حدِّد النوع أو اترك المرجع فارغًا")
    if legal_basis_kind != "NONE" and not legal_basis_ref.strip():
        raise JudiciaryError(f"نوعُ المرجع '{legal_basis_kind}' يلزمه مرجعٌ مكتوب")

    case = load_case(session, case_id, tenant_id=tenant_id)
    party = session.get(CasePartyModel, claimant_party_id)
    if party is None or party.case_id != case.id:
        raise JudiciaryError("المُطالِب ليس طرفًا مُسجَّلًا في هذه القضية")

    row = CaseClaimModel(
        id=f"clm-{uuid.uuid4()}",
        case_id=case.id,
        claimant_party_id=party.id,
        claim_type=claim_type,
        statement=statement,
        legal_basis_kind=legal_basis_kind,
        legal_basis_ref=legal_basis_ref,
        legal_basis_verified=False,
        amount=amount,
        filed_by=filed_by,
        tenant_id=tenant_id,
    )

    def _insert(created: list[tuple[Any, str]]) -> CaseClaimModel:
        session.add(row)
        session.flush()
        created.append((CaseClaimModel, row.id))
        return row

    # `admit_claim` (D17-2) · لا مفتاحَ طبيعيًّا: المفتاحُ معرِّفُ الصفِّ نفسُه — حدٌّ معلَنٌ
    # (D6): لا ذرّيّةَ عبرَ إعادةِ المُنادي، والإعادةُ داخلَ النداءِ الواحدِ وحدَها.
    plan = _plan_crossing(
        session,
        action="admit_claim",
        court=load_court(session, case.court_id, tenant_id=tenant_id),
        case_scope=case.jurisdiction,
        namespace="judiciary.claim.add",
        key=row.id,
        kind="CREATE",
        description=f"قبولُ مطالبةٍ من نوعِ '{claim_type}' في القضيّةِ '{case.reference}'",
        mutate=_insert,
    )
    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)
    return crossed_value(
        guarded,
        replay=lambda: session.get(CaseClaimModel, row.id),
        what=f"قبولَ المطالبةِ في القضيّةِ '{case.reference}'",
    )


def submit_evidence(
    session: Session,
    *,
    case_id: str,
    evidence_type: str,
    source: str,
    submitted_by_principal: str,
    submitted_by_identity_id: str,
    tenant_id: str,
    content_hash: str | None = None,
    fingerprint_algo: str = "",
) -> CaseEvidenceModel:
    """أودِع دليلًا في قضيةٍ غير مُغلقة — سجلُّ إيداعٍ لا سلسلةُ حيازة."""
    if evidence_type not in EVIDENCE_TYPES:
        raise EvidenceError(f"نوعُ دليلٍ غير معروف '{evidence_type}'")
    if not source.strip():
        raise EvidenceError("مصدرُ الدليل لا يكون فارغًا")
    if content_hash is not None:
        normalized = content_hash.strip().lower()
        if len(normalized) != 64 or any(ch not in "0123456789abcdef" for ch in normalized):
            raise EvidenceError("البصمةُ يجب أن تكون sha256 سِتّينيةً بطول 64")
        if not fingerprint_algo.strip():
            fingerprint_algo = "sha256"
        content_hash = normalized
    elif fingerprint_algo.strip():
        raise EvidenceError("خوارزميةُ بصمةٍ بلا بصمة — لا يُدَّعى تبصيمٌ لم يجرِ")

    case = load_case(session, case_id, tenant_id=tenant_id)
    if case.status == "closed":
        raise EvidenceError("لا يُودَع دليلٌ في قضيةٍ مُغلقة")
    _load_identity(session, submitted_by_identity_id, tenant_id=tenant_id)

    row = CaseEvidenceModel(
        id=f"evd-{uuid.uuid4()}",
        case_id=case.id,
        evidence_type=evidence_type,
        source=source,
        content_hash=content_hash,
        fingerprint_algo=fingerprint_algo if content_hash else "",
        submitted_by_principal=submitted_by_principal,
        submitted_by_identity_id=submitted_by_identity_id,
        status="submitted",
        tenant_id=tenant_id,
    )
    session.add(row)
    session.flush()
    return row


def check_evidence_status(
    session: Session, *, evidence_id: str, status: str, reason: str, tenant_id: str
) -> CaseEvidenceModel:
    """فحوصُ تغييرِ حالةِ الدليلِ — قبلَ الحدِّ وفي الكاتبِ نفسِه (مصدرٌ واحدٌ)."""
    if status not in ("admitted", "excluded", "withdrawn"):
        raise EvidenceError(f"حالةُ دليلٍ غير مسموحة '{status}'")
    if not reason.strip():
        raise EvidenceError("تغييرُ حالة دليلٍ يلزمه سببٌ مكتوب")
    row = session.get(CaseEvidenceModel, evidence_id)
    if row is None or row.tenant_id != tenant_id:
        raise EvidenceError(f"لا دليل بالمعرّف '{evidence_id}' في مستأجر '{tenant_id}'")
    return row


def set_evidence_status(
    session: Session, *, evidence_id: str, status: str, reason: str, tenant_id: str
) -> tuple[CaseEvidenceModel, str]:
    """اقبل الدليل أو استبعِده أو اسحبه — بأثرٍ مكتوبٍ لا بحذف صفّ."""
    row = check_evidence_status(
        session, evidence_id=evidence_id, status=status, reason=reason, tenant_id=tenant_id
    )
    previous = row.status
    row.status = status
    row.status_reason = reason
    session.flush()
    return row, previous


def _check_proceeding(
    session: Session,
    *,
    case_id: str,
    proceeding_type: str,
    actor_identity_id: str,
    summary: str,
    tenant_id: str,
) -> LegalCaseModel:
    """فحوصُ الإجراءِ كلُّها قبلَ الحدِّ — مصدرٌ واحدٌ للكاتبِ الخاصِّ وللعمليّةِ العامّةِ."""
    if proceeding_type not in PROCEEDING_TYPES:
        raise JudiciaryError(f"نوعُ إجراءٍ غير معروف '{proceeding_type}'")
    if not summary.strip():
        raise JudiciaryError("خلاصةُ الإجراء لا تكون فارغة")
    case = load_case(session, case_id, tenant_id=tenant_id)
    _load_identity(session, actor_identity_id, tenant_id=tenant_id)
    return case


def _insert_proceeding(
    session: Session,
    *,
    case_id: str,
    proceeding_type: str,
    actor_principal: str,
    actor_identity_id: str,
    summary: str,
    tenant_id: str,
    record: dict[str, Any] | None = None,
    created: list[tuple[Any, str]] | None = None,
) -> CaseProceedingModel:
    """الكاتبُ الخامُ للإجراءِ — **خاصٌّ** يُنادى من داخلِ مُطبِّقاتٍ عابرةٍ فقط (D3).

    يُناديه مُطبِّقُ `record_proceeding` ومُطبِّقاتُ `file_case`/`open_hearing` في الخدمةِ
    و`rulings.issue_ruling`؛ فلا يقعُ عبورٌ داخلَ عبورٍ (Q-9 لم يُحسَمْ — WI-110).
    """
    case = _check_proceeding(
        session,
        case_id=case_id,
        proceeding_type=proceeding_type,
        actor_identity_id=actor_identity_id,
        summary=summary,
        tenant_id=tenant_id,
    )
    current_max = session.execute(
        select(func.max(CaseProceedingModel.sequence)).where(CaseProceedingModel.case_id == case.id)
    ).scalar()
    row = CaseProceedingModel(
        id=f"prc-{uuid.uuid4()}",
        case_id=case.id,
        sequence=int(current_max or 0) + 1,
        proceeding_type=proceeding_type,
        actor_principal=actor_principal,
        actor_identity_id=actor_identity_id,
        summary=summary,
        record=record or {},
        status="recorded",
        tenant_id=tenant_id,
    )
    session.add(row)
    session.flush()
    if created is not None:
        created.append((CaseProceedingModel, row.id))
    return row


def record_proceeding(
    session: Session,
    *,
    case_id: str,
    proceeding_type: str,
    actor_principal: str,
    actor_identity_id: str,
    summary: str,
    tenant_id: str,
    record: dict[str, Any] | None = None,
) -> CaseProceedingModel:
    """قيِّد إجراءً بترتيبٍ مفروضٍ في القاعدة — بديلُ النصّ الحرّ — عابرًا الحدَّ (`record_proceeding`)."""
    case = _check_proceeding(
        session,
        case_id=case_id,
        proceeding_type=proceeding_type,
        actor_identity_id=actor_identity_id,
        summary=summary,
        tenant_id=tenant_id,
    )
    # لا مفتاحَ طبيعيًّا قبلَ الحدِّ (التسلسلُ يُحسَبُ داخلَه): مفتاحٌ فريدٌ لكلِّ نداءٍ (D6).
    key = f"{case.id}:{uuid.uuid4()}"

    def _insert(created: list[tuple[Any, str]]) -> CaseProceedingModel:
        return _insert_proceeding(
            session,
            case_id=case.id,
            proceeding_type=proceeding_type,
            actor_principal=actor_principal,
            actor_identity_id=actor_identity_id,
            summary=summary,
            tenant_id=tenant_id,
            record=record,
            created=created,
        )

    plan = _plan_crossing(
        session,
        action="record_proceeding",
        court=load_court(session, case.court_id, tenant_id=tenant_id),
        case_scope=case.jurisdiction,
        namespace="judiciary.proceeding.record",
        key=key,
        kind="CREATE",
        description=f"قيدُ إجراءٍ من نوعِ '{proceeding_type}' في القضيّةِ '{case.reference}'",
        mutate=_insert,
    )
    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)
    return crossed_value(
        guarded,
        replay=lambda: None,
        what=f"قيدَ الإجراءِ في القضيّةِ '{case.reference}'",
    )


def list_proceedings(
    session: Session, *, case_id: str, tenant_id: str
) -> list[CaseProceedingModel]:
    return list(
        session.execute(
            select(CaseProceedingModel)
            .where(
                CaseProceedingModel.case_id == case_id,
                CaseProceedingModel.tenant_id == tenant_id,
            )
            .order_by(CaseProceedingModel.sequence)
        ).scalars()
    )


__all__ = [
    "ALLOWED_TRANSITIONS",
    "CaseNotFoundError",
    "Crossing",
    "JudicialLedgerDivergenceError",
    "CaseTransitionError",
    "EvidenceError",
    "PartyIdentityError",
    "add_claim",
    "add_party",
    "advance_case",
    "assert_transition",
    "assign_case",
    "case_dict",
    "check_assign",
    "check_close",
    "check_evidence_status",
    "crossed_value",
    "claim_dict",
    "close_case",
    "evidence_dict",
    "file_case",
    "list_proceedings",
    "load_case",
    "open_case",
    "open_hearing",
    "judicial_request",
    "party_dict",
    "proceeding_dict",
    "record_proceeding",
    "set_evidence_status",
    "submit_evidence",
]
