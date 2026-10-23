"""
AMOS-Federation Federal Judiciary — Rulings
الهدف: الحكم قرارٌ مربوطٌ بقضيةٍ وقاضٍ مُثبَت، وحكمٌ واحدٌ لكل مرحلةٍ قضائية
النطاق: services/federal_judiciary
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-17 (R7-D10)

## أربعةُ قيودٍ على الحكم، كلٌّ منها مفروض

| القيد | كيف يُفرَض |
| --- | --- |
| لا حكمَ بلا قضية | `case_id` مفتاحٌ أجنبيّ `NOT NULL` إلى `state_legal_cases` |
| لا حكمَ بلا سلطةٍ قضائية | `issue_ruling` تأخذ `JudicialAuthority` مُثبَتةً (`PROVEN`) لا مُنادىً مجهولًا |
| لا حكمين لمرحلةٍ واحدة | فهرسٌ فريدٌ جزئيّ `(case_id, stage)` على `issued`/`enforced` — في القاعدة |
| لا حكمَ يُحذَف | الإلغاء تغييرُ حالةٍ إلى `vacated` بسببٍ مكتوبٍ وطابعٍ زمنيّ |

والقيدُ الثالث مفروضٌ **مرّتين**: قراءةٌ سابقة تُعطي رفضًا مفهومًا
(`DuplicateRulingError`)، والفهرسُ في القاعدة يُغلق الباب حتى لو كُتب صفٌّ من مسارٍ
آخر. فلو حُذف الفحصُ من الكود لَبقي القيد.

## لا منفِّذَ موازٍ في هذا الملفّ

`issue_ruling` تكتب الحكم، وتُقيِّد إجراءً من نوع `RULING`، وتنقل القضية إلى
`decided`. ولا تُقدِّم مهمّةً ولا تُحرِّك مالًا: التنفيذ في `enforcement.py` عبر
`ExecutiveCore` والخزانة القائمين. فالمحكمة تقضي، والتنفيذ لغيرها.

## `PROVEN` شرطٌ لا وصف

`issue_ruling` ترفض تصنيفًا أدنى من `PROVEN`: التخويلُ على مستوى المحكمة
(`PARTIAL`) يكفي للقراءة ولا يكفي لإصدار حكمٍ في قضيةٍ بعينها. فالتصنيف مدخلٌ في
القرار لا حَشوًا في السجلّ.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import func, select

from amos_federation.common.database import get_session_factory
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)
from amos_federation.services.federal_judiciary.docket import (
    _insert_proceeding,
    advance_case,
    load_case,
)
from amos_federation.services.federal_judiciary.models import (
    RULING_DECISIONS,
    RULING_STAGES,
    CaseProceedingModel,
    LegalCaseModel,
    RulingModel,
)
from amos_federation.services.federal_judiciary.registry import JudiciaryError

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from amos_federation.services.federal_judiciary.authority import JudicialAuthority

#: الحالاتُ التي يبقى فيها الحكمُ قائمًا ويحجز مرحلتَه القضائية.
ACTIVE_RULING_STATUSES: tuple[str, ...] = ("issued", "enforced")

#: فاعلُ إصدارِ الحكمِ (تصميمُ J1 · WI-105 · قرارُ المالكِ Q-6 ①): القضاءُ فرعٌ
#: مستقلٌّ بفاعلٍ قضائيٍّ مُعلَنٍ — **ثابتٌ في الوحدةِ لا معاملًا للمُنادي**. من يملكُ
#: تمريرَ مُفوِّضٍ بفاعلٍ آخرَ يُصدِرُ حكمًا (ثغرةُ DISC-121)، فاختيارُ الفاعلِ يبقى
#: هنا وحدَه (D1) — والاختبارُ يُبدِّلُه بـ`monkeypatch` على هذا الثابتِ لا بمعاملٍ
#: إنتاجيّ.
JUDICIARY_ACTOR = "JUDICIAL"

_DEFAULT_JUDICIARY_AUTHORIZER: ConstitutionalAuthorizer | None = None


def _judiciary_authorizer() -> ConstitutionalAuthorizer:
    """المُصرِّحُ الافتراضيُّ بفاعلِ إصدارِ الحكمِ المُسمّى — واحدٌ للوحدةِ (D1)."""
    global _DEFAULT_JUDICIARY_AUTHORIZER
    if _DEFAULT_JUDICIARY_AUTHORIZER is None:
        _DEFAULT_JUDICIARY_AUTHORIZER = ConstitutionalAuthorizer(actor=JUDICIARY_ACTOR)
    return _DEFAULT_JUDICIARY_AUTHORIZER


def reset_judiciary_authorizer() -> None:
    """أفرِغِ المُفوِّضَ المحفوظَ — للاختباراتِ التي تبدّلُ الفاعلَ (D1)."""
    global _DEFAULT_JUDICIARY_AUTHORIZER
    _DEFAULT_JUDICIARY_AUTHORIZER = None


class RulingError(JudiciaryError):
    """إصدارُ حكمٍ مرفوض — مدخلٌ غير صالحٍ أو حالةٌ لا تسمح."""


class DuplicateRulingError(RulingError):
    """للقضية حكمٌ قائمٌ في هذه المرحلة القضائية — لا حكمَ ثانٍ."""


class RulingLedgerDivergenceError(RulingError):
    """سجلُّ الذرّيّةِ يُثبِتُ إصدارَ حكمٍ والصفُّ غائبٌ — استعادةٌ لا إصدارٌ يُزعَم."""


def _now() -> datetime:
    return datetime.now(UTC)


def _iso(value: datetime | None) -> str:
    return value.isoformat() if value else ""


def ruling_dict(row: RulingModel) -> dict[str, Any]:
    return {
        "id": row.id,
        "case_id": row.case_id,
        "court_id": row.court_id,
        "judge_id": row.judge_id,
        "judge_identity_id": row.judge_identity_id,
        "stage": row.stage,
        "decision": row.decision,
        "disposition": row.disposition,
        "status": row.status,
        "provenance_class": row.provenance_class,
        "authority": row.authority or {},
        "issued_by_principal": row.issued_by_principal,
        "issued_at": _iso(row.issued_at),
        "vacated_at": _iso(row.vacated_at),
        "vacatur_reason": row.vacatur_reason or "",
        "tenant_id": row.tenant_id,
    }


def load_ruling(session: Session, ruling_id: str, *, tenant_id: str) -> RulingModel:
    row = session.get(RulingModel, ruling_id)
    if row is None or row.tenant_id != tenant_id:
        raise RulingError(f"لا حكم بالمعرّف '{ruling_id}' في مستأجر '{tenant_id}'")
    return row


def active_ruling_for_stage(session: Session, *, case_id: str, stage: str) -> RulingModel | None:
    """اقرأ الحكم القائم لمرحلةٍ قضائية إن وُجد — القراءةُ التي تسبق الفهرس."""
    return session.execute(
        select(RulingModel).where(
            RulingModel.case_id == case_id,
            RulingModel.stage == stage,
            RulingModel.status.in_(ACTIVE_RULING_STATUSES),
        )
    ).scalar_one_or_none()


def issue_ruling(
    session: Session,
    *,
    authority: JudicialAuthority,
    decision: str,
    disposition: str,
    tenant_id: str,
    stage: str = "FIRST_INSTANCE",
) -> tuple[RulingModel, Any]:
    """أصدِر حكمًا بسلطةٍ قضائية مُثبَتة، وقيِّد إجراءه، وانقل القضية إلى `decided`.

    Args:
        authority: قرارُ حلّ السلطة القضائية — يلزم `allowed` وتصنيف `PROVEN`.
        decision: من `RULING_DECISIONS`.
        disposition: منطوقُ الحكم — نصٌّ غير فارغ.
        stage: المرحلة القضائية — حكمٌ واحدٌ قائمٌ لكلٍّ منها.

    Returns:
        `(صفُّ الحكم، صفُّ الإجراء المُقيَّد)`.

    Raises:
        RulingError: سلطةٌ غير مُثبَتة، أو مدخلٌ غير صالح.
        DuplicateRulingError: للقضية حكمٌ قائمٌ في هذه المرحلة.
        CaseTransitionError: حالةُ القضية لا تسمح بالانتقال إلى `decided`.
    """
    if not authority.allowed or authority.classification != "PROVEN":
        raise RulingError(
            "إصدارُ الحكم يلزمه سلطةٌ قضائية مُثبَتةٌ بتصنيف PROVEN — "
            f"الحاصل: allowed={authority.allowed} classification={authority.classification}"
        )
    if authority.case_id is None or authority.judge_id is None or authority.court_id is None:
        raise RulingError("قرارُ السلطة ناقصٌ: يلزمه قضيةٌ وقاضٍ ومحكمة")
    if stage not in RULING_STAGES:
        raise RulingError(f"مرحلةٌ غير معروفة '{stage}' — المسموح: {', '.join(RULING_STAGES)}")
    if decision not in RULING_DECISIONS:
        raise RulingError(f"قرارٌ غير معروف '{decision}' — المسموح: {', '.join(RULING_DECISIONS)}")
    if not disposition.strip():
        raise RulingError("منطوقُ الحكم لا يكون فارغًا")

    case = load_case(session, authority.case_id, tenant_id=tenant_id)
    existing = active_ruling_for_stage(session, case_id=case.id, stage=stage)
    if existing is not None:
        raise DuplicateRulingError(
            f"القضية '{case.reference}' لها حكمٌ قائم '{existing.id}' في المرحلة '{stage}' — "
            "لا حكمَ ثانٍ لنفس المرحلة القضائية"
        )

    # جيلُ المفتاحِ (D6): عددُ الأحكامِ المُلغاةِ للقضيةِ في هذه المرحلةِ — يُقرأُ
    # قبلَ الحدِّ. فبعدَ الإلغاءِ يُسمَحُ بديلٌ للمرحلةِ نفسِها، ومفتاحٌ بلا جيلٍ
    # يُعيدُ الحكمَ الأوّلَ «إعادةً» صامتةً ولا يكتبُ البديلَ.
    vacated = session.execute(
        select(func.count())
        .select_from(RulingModel)
        .where(
            RulingModel.case_id == case.id,
            RulingModel.stage == stage,
            RulingModel.status == "vacated",
        )
    ).scalar()
    generation = int(vacated or 0)

    # حالةُ القضيةِ قبلَ العمليّةِ — يُستعيدُها المُعوِّضُ التقنيُّ (D7-أ).
    previous_status = case.status

    def _judicial_action() -> Any:
        """طلبُ الاختصاصِ منَ البياناتِ الحيّةِ لا من ثوابتَ (D3)."""
        import sys as _sys

        from amos_federation.services.executive_core.sovereignty_bridge import (
            locate_repo_root,
        )

        root = locate_repo_root()
        if str(root) not in _sys.path:
            _sys.path.insert(0, str(root))
        from core.sovereignty.jurisdiction import JudicialAction

        return JudicialAction(
            action="issue_ruling",
            court_scope=authority.jurisdiction or "",
            case_scope=case.jurisdiction,
            actor_scope=authority.position_scope or "",
            target=case.id,
            institution_id=authority.institution_id,
            # القضيّةُ بلا عمودِ مؤسّسةٍ: مؤسّستُها مؤسّسةُ محكمتِها — مُعلَنٌ لا مُخمَّنٌ
            case_institution_id=authority.institution_id,
            is_royal_decree_target=False,
        )

    # هدفُ العبورِ يحملُ جيلَ الإلغاءِ (D5 + D6): بصمةُ العقدِ تُشتقُّ من
    # (الفاعلِ · الفعلِ · الهدفِ · الآثارِ) فقط، فلو حملَها المفتاحُ وحدَه
    # لتصادمَ الحكمانِ للمرحلةِ نفسِها في الثانيةِ نفسِها في معرِّفِ الإذنِ
    # (EP-…) فرُفضَ البديلُ بعدَ الإلغاءِ رفضَ إعادةِ إذنٍ — وهو اكتشافُ تنفيذٍ
    # أُعلِنَ بإضافةٍ مؤرَّخةٍ في وثيقةِ التصميمِ (§ D5). والجيلُ جزءُ هويةِ
    # العمليّةِ في المفتاحِ والهدفِ معًا، فالدلالةُ كما هي: أثرٌ واحدٌ
    # لمعاملةٍ واحدةٍ.
    target = f"judiciary/rulings/{case.id}/{stage}/g{generation}"
    effect = declared_effect(
        "CREATE",
        target,
        f"حكمٌ في المرحلة '{stage}' وإجراؤه وانتقالُ القضيّةِ إلى decided",
    )
    op_key = operation_key("judiciary.ruling.issue", f"{case.id}:{stage}:g{generation}")

    created: dict[str, str] = {}

    def _apply(_effect: Any) -> tuple[RulingModel, Any]:
        """المُطبِّقُ المتداخلُ الخاصُّ — الكتابةُ الوحيدةُ للحكمِ داخلَ الحدِّ (D4).

        دالّةٌ واحدةٌ متداخلةٌ على نمطِ `agent_identity._apply` (WI-082): تحملُ
        `add` + `flush` + `record_proceeding` + `advance_case` + `commit` في
        معاملةٍ واحدةٍ، فتُحصى موضعَ كتابةٍ مستقلًّا في الجردِ (public=False).
        """
        row = RulingModel(
            id=f"rul-{uuid.uuid4()}",
            case_id=case.id,
            court_id=authority.court_id,
            judge_id=authority.judge_id,
            judge_identity_id=authority.identity_id,
            stage=stage,
            decision=decision,
            disposition=disposition,
            status="issued",
            provenance_class=authority.classification,
            authority=authority.as_dict(),
            issued_by_principal=authority.principal_id,
            tenant_id=tenant_id,
        )
        session.add(row)
        session.flush()
        # الكاتبُ الخاصُّ لا العمليّةُ العامّةُ العابرةُ (WI-111 · D3): لا عبورَ داخلَ عبورٍ.
        proceeding = _insert_proceeding(
            session,
            case_id=case.id,
            proceeding_type="RULING",
            actor_principal=authority.principal_id,
            actor_identity_id=authority.identity_id or "",
            summary=f"حكمٌ في المرحلة '{stage}': {decision}",
            tenant_id=tenant_id,
            record={"ruling_id": row.id, "stage": stage, "decision": decision},
        )
        if case.status != "decided":
            advance_case(session, case_id=case.id, target="decided", tenant_id=tenant_id)
        session.commit()
        created["ruling_id"] = row.id
        created["proceeding_id"] = proceeding.id
        return row, proceeding

    def _restore() -> None:
        """المُعوِّضُ (D7-أ): استعادةٌ تقنيّةٌ دقيقةٌ في جلسةٍ جديدةٍ — لا إلغاءٌ قضائيّ.

        الصفوفُ مُلتزَمةٌ والعمليّةُ لم تثبتْ (فشلٌ بعدَ الالتزامِ): فلا حكمَ قانونيًّا
        وُجِدَ. يُحذفُ صفُّ الإجراءِ (آخرُ تسلسلٍ للقضيّةِ) وصفُّ الحكمِ بمعرِّفَيهما
        وتُرجَعُ حالةُ القضيّةِ إلى ما كانت قبلَ العمليّةِ. «الحذفُ شأنٌ تنفيذيّ» —
        والمُعوِّضُ ليس أثرًا مُعلَنًا ولا تراجعُه البوابة، فيُكتَبُ ذلك صريحًا هنا.
        """
        restore = get_session_factory()()
        try:
            ruling_row = restore.get(RulingModel, created.get("ruling_id", ""))
            if ruling_row is not None:
                restore.delete(ruling_row)
            proceeding_row = restore.get(CaseProceedingModel, created.get("proceeding_id", ""))
            if proceeding_row is not None:
                restore.delete(proceeding_row)
            case_row = restore.get(LegalCaseModel, case.id)
            if case_row is not None and case_row.status != previous_status:
                case_row.status = previous_status
            restore.commit()
        finally:
            restore.close()

    guarded = _judiciary_authorizer().guard_declared(
        "issue_ruling",
        target,
        declared_effects=(effect,),
        applier=_apply,
        operation_key=op_key,
        compensators=(
            compensator(
                effect.signature,
                _restore,
                "استعادةٌ تقنيّةٌ: حذفُ صفَّي الحكمِ والإجراءِ وإرجاعُ حالةِ القضيّةِ — "
                "العمليّةُ لم تثبتْ فلا حكمَ قانونيًّا وُجِدَ",
            ),
        ),
        metadata={
            "case_reference": case.reference,
            "stage": stage,
            "generation": generation,
        },
        judicial_action=_judicial_action(),
    )
    if guarded.is_replay:
        # الإعادةُ ليست نجاحًا ثانيًا: يُقرأُ الحكمُ القائمُ للمرحلةِ، فإن غابَ
        # رُفِعَ التفرُّقُ صريحًا — ولا كتابةَ ثانيةً خارجَ الحدِّ (D6).
        standing = active_ruling_for_stage(session, case_id=case.id, stage=stage)
        if standing is None:
            raise RulingLedgerDivergenceError(
                f"سجلُّ الذرّيّةِ يُثبِتُ إصدارَ حكمٍ للقضيّةِ '{case.reference}' "
                f"في المرحلةِ '{stage}' ولا صفَّ حكمٍ قائمًا — استعادةٌ مطلوبةٌ "
                "لا إصدارٌ يُزعَم"
            )
        return standing, None
    value = guarded.value
    row, proceeding = value
    return row, proceeding


def check_vacate(session: Session, *, ruling_id: str, reason: str, tenant_id: str) -> RulingModel:
    """فحوصُ الإلغاءِ — قبلَ الحدِّ وفي الكاتبِ نفسِه (مصدرٌ واحدٌ · WI-111)."""
    if not reason.strip():
        raise RulingError("إلغاءُ حكمٍ يلزمه سببٌ مكتوب")
    row = load_ruling(session, ruling_id, tenant_id=tenant_id)
    if row.status == "vacated":
        raise RulingError(f"الحكم '{ruling_id}' مُلغىً أصلًا")
    if row.status == "enforced":
        raise RulingError(f"الحكم '{ruling_id}' نُفِّذ — عكسُ أثرٍ تنفيذيّ ليس مبنيًّا في هذه الوحدة")
    return row


def vacate_ruling(
    session: Session, *, ruling_id: str, reason: str, tenant_id: str
) -> tuple[RulingModel, str]:
    """ألغِ حكمًا بسببٍ مكتوب — تغييرُ حالةٍ لا حذفُ صفّ.

    والحكمُ المُنفَّذ (`enforced`) لا يُلغى في هذه الوحدة: إلغاءُ أثرٍ تنفيذيّ جرى
    يحتاج عكسَ حركةٍ أو إبطالَ مهمّة، وذاك مسارٌ **غير مبنيّ** ويُقال ولا يُموَّه.
    """
    row = check_vacate(session, ruling_id=ruling_id, reason=reason, tenant_id=tenant_id)
    previous = row.status
    row.status = "vacated"
    row.vacated_at = _now()
    row.vacatur_reason = reason
    session.flush()
    return row, previous


def mark_ruling_enforced(session: Session, *, ruling_id: str, tenant_id: str) -> RulingModel:
    """علِّم الحكم منفَّذًا — تُناديه `enforcement.py` بعد أثرٍ حقيقيّ فقط."""
    row = load_ruling(session, ruling_id, tenant_id=tenant_id)
    if row.status != "issued":
        raise RulingError(f"الحكم حالته '{row.status}' — لا يُعلَّم منفَّذًا")
    row.status = "enforced"
    session.flush()
    return row


def list_rulings(session: Session, *, case_id: str, tenant_id: str) -> list[RulingModel]:
    return list(
        session.execute(
            select(RulingModel)
            .where(RulingModel.case_id == case_id, RulingModel.tenant_id == tenant_id)
            .order_by(RulingModel.issued_at)
        ).scalars()
    )


__all__ = [
    "ACTIVE_RULING_STATUSES",
    "DuplicateRulingError",
    "RulingError",
    "active_ruling_for_stage",
    "issue_ruling",
    "list_rulings",
    "load_ruling",
    "mark_ruling_enforced",
    "ruling_dict",
    "vacate_ruling",
]
