"""
AMOS-Federation Phase 12 — State Runtime
الهدف: كل ولاية لها services/agents/tools منفصلة فعليًا، مع عزل قاعدة بيانات
النطاق: services/governance/state_runtime
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
تاريخ آخر تعديل: 2026-10-28 (W-723 — G1 الدفعة 2: خمسةُ أسطحٍ تعبرُ الحدَّ · سجلُّ الإيقافِ المحكوم) · وقبله: 2026-08-22 (W-019 — نقضُ سابقةِ 2A: فعلٌ غيرُ دستوريٍّ وفاعلٌ تنفيذيّ)

المتطلبات (من خارطة الطريق):
  12.1: State Runtime بحيث كل ولاية لها services/agents/tools منفصلة
  12.2: عزل قاعدة بيانات لكل ولاية (schema منفصل)
  12.3: Federal Message Bus بين الولايات
  12.4: Federal Budget Allocation
  12.5: Federal Policy Enforcement
  12.6: البنية الإدارية لكل ولاية
  12.7: اختبار عزل ولاية كاملة
  12.8: إضافة ولاية جديدة بلا تعديل الدستور
"""

import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from amos_federation.common.database import get_database_url
from amos_federation.common.persistent import PersistentAuditStore
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    UndeclaredExecutionError,
    compensator,
    declared_effect,
    get_authorizer,
    operation_key,
)

#: وحدةُ تقويمِ العمودِ الذي تكتبُ فيه هذه الوحدة — مُعلَنةٌ في المخطَّطِ نفسِه
#: (`StateModel.budget` أدناه: `# amos-credit`)، وتُقرأُ هنا ولا تُستنبَط.
BUDGET_UNIT = "amos-credit"

#: فعلُ العمليّة بعدَ **نقضِ سابقةِ 2A** (W-019 · أثرُ القرارِ Q-17 · الخيارِ 2).
#:
#: كانَ الفعلُ `allocate_budget` — وهو **حصرُ الخزانةِ** في المادة الثالثة. وقُضِيَ
#: في Q-17 أنَّ `amos-credit` **وحدةُ قياسٍ تشغيليّةٌ لا مالٌ دستوريّ**، وهذا العمودُ
#: مقوَّمٌ بها. فكانت السابقةُ تُمارِسُ فعلًا حصريًّا على **غيرِ مال**: تُوهِمُ حركةَ
#: مالٍ عامٍّ حيثُ لا مالَ عامّ، وتُميِّعُ حصريّةَ الفعلِ التي يحرسُها R-003-1.
#:
#: فصارَ للعمليّةِ فعلُها الصريحُ، مُثبَتًا في `NON_CONSTITUTIONAL_MONEY_ACTIONS` في
#: `core/constitutional_engine/rules.py`. وما بقيَ كما هو: الحدُّ السياديُّ نفسُه —
#: أثرٌ مُعلَنٌ قبلَ وقوعِه، ومفتاحُ عمليّةٍ، ومعوّضٌ يعكسُ الفرقَ فعلًا.
ACTION_ALLOCATE_OPERATIONAL_CREDIT = "allocate_operational_credit"

#: نطاقُ مفاتيحِ الذرّيّة (1H) لتوزيعِ الميزانية.
BUDGET_OPERATION_SCOPE = "state_runtime.budget.allocate"


class BudgetAllocationError(RuntimeError):
    """توزيعُ ميزانيةٍ تعذّرَ تطبيقُه — رفعٌ صريحٌ لا قيمةٌ صامتة."""


# ── G1 الدفعة 2 (W-723): أفعالُ الأسطحِ الخمسةِ من جدولِ G1 § 2 بنصِّه ──────
#: `register_state` = `create_state` الملكيُّ (Q-13 · G1 § 3.1) — يعبرُ بمرسومٍ موقَّع.
ACTION_CREATE_STATE = "create_state"
#: الإيقافُ احتواءٌ: `contain_agent` لا يمنعُه القاطعُ في أيِّ مستوى (G1 § 5 بند 2).
ACTION_SUSPEND_STATE = "contain_agent"
#: إعادةُ التفعيلِ استعادةُ قدرةٍ: `activate_agent` ممنوعٌ عندَ ≥4.
ACTION_REACTIVATE_STATE = "activate_agent"
#: تعيينُ وكيلٍ: `dispatch_agent` ممنوعٌ عندَ ≥3.
ACTION_ASSIGN_AGENT = "dispatch_agent"
#: رسالةٌ بينَ ولايتين: `coordinate` ممنوعٌ عندَ ≥4.
ACTION_SEND_MESSAGE = "coordinate"

#: نطاقاتُ مفاتيحِ الذرّيّة (1H) — لكلِّ سطحٍ نطاقُه فلا تصادم.
CREATE_STATE_SCOPE = "state_runtime.state.create"
SUSPEND_STATE_SCOPE = "state_runtime.state.suspend"
REACTIVATE_STATE_SCOPE = "state_runtime.state.reactivate"
ASSIGN_AGENT_SCOPE = "state_runtime.state.assign"
SEND_MESSAGE_SCOPE = "state_runtime.message.send"


class DecreeTargetMismatchError(ValueError):
    """مرسومٌ هدفُه غيرُ الولايةِ المطلوبة — يُرفَضُ قبلَ العبور (G1 § 9.8.1).

    `classify` يطابقُ فعلَ المرسومِ لا هدفَه (المقيسُ في `core/sovereignty/authority.py`)،
    فمرسومُ إنشاءِ ولايةٍ لا يُعادُ توجيهُه إلى ولايةٍ أخرى.
    """


class StateBase(DeclarativeBase):
    pass


class StateModel(StateBase):
    """جدول الولايات الفدرالية."""

    __tablename__ = "federal_states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    type = Column(
        String, nullable=False
    )  # finance, law, science, health, culture, infrastructure, industry, trade, education
    status = Column(String, default="active")  # active, suspended, closed
    head_agent_id = Column(String, nullable=True)
    budget = Column(String, default="0")  # amos-credit
    established_at = Column(DateTime, default=lambda: datetime.now(UTC))
    closed_at = Column(DateTime, nullable=True)
    metadata_json = Column(Text, default="{}")


class StateAgentAssignment(StateBase):
    """تعيين الوكلاء في الولايات."""

    __tablename__ = "state_agent_assignments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id = Column(String, nullable=False, index=True)
    agent_id = Column(String, nullable=False, index=True)
    role = Column(
        String, nullable=False
    )  # coordinator, council, judge, monitor, factory_manager, worker, trainer, learner, accountant
    assigned_at = Column(DateTime, default=lambda: datetime.now(UTC))


class StateMessage(StateBase):
    """رسائل بين الولايات عبر Federal Message Bus."""

    __tablename__ = "state_messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(String, nullable=False, unique=True)
    from_state = Column(String, nullable=False, index=True)
    to_state = Column(String, nullable=False, index=True)
    subject = Column(String, nullable=False)
    body = Column(Text, default="")
    policy_check = Column(String, default="pending")  # pending, approved, denied
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    delivered_at = Column(DateTime, nullable=True)


class StateSuspensionRecord(StateBase):
    """سجلُّ الإيقافِ المحكوم (التوجيهُ 27 § 1 · G1 § 9.6 و§ 9.8.2).

    جدولٌ جديدٌ يُنشئُه `create_all` — لا عمودَ يُضافُ إلى `federal_states` فتنكسرَ
    قاعدةٌ قائمة. سجلٌّ **نشطٌ** (`cleared_at` فارغ) = إيقافٌ عبرَ `suspend_state`
    المحروس، فلا يُعيدُ `self_heal` تفعيلَ ولايتِه. وولايةٌ معلَّقةٌ بلا سجلٍّ نشطٍ
    = تعليقٌ تلقائيٌّ (بلا قرار) يُعادُ تفعيلُه كما كان.
    """

    __tablename__ = "state_suspension_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    record_id = Column(String, nullable=False, unique=True, index=True)
    state_id = Column(String, nullable=False, index=True)
    operation_id = Column(String, nullable=False)
    previous_status = Column(String, nullable=False)
    reason = Column(Text, default="")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    cleared_at = Column(DateTime, nullable=True)


# الولايات التسع المعرفة في الدستور
FEDERAL_STATES = {
    "finance": {"name": "ولاية المال", "type": "finance", "target_population": 45},
    "law": {"name": "ولاية القانون", "type": "law", "target_population": 40},
    "science": {"name": "ولاية العلم", "type": "science", "target_population": 45},
    "health": {"name": "ولاية الصحة", "type": "health", "target_population": 35},
    "culture": {"name": "ولاية الثقافة", "type": "culture", "target_population": 40},
    "infrastructure": {
        "name": "ولاية البنية التحتية",
        "type": "infrastructure",
        "target_population": 45,
    },
    "industry": {"name": "ولاية الصناعة", "type": "industry", "target_population": 50},
    "trade": {"name": "ولاية التجارة", "type": "trade", "target_population": 30},
    "education": {"name": "ولاية التعليم", "type": "education", "target_population": 40},
}

# البنية الإدارية الموحدة لكل ولاية
STATE_ADMIN_STRUCTURE = {
    "coordinator": {"count": 1, "role": "منسق الولاية"},
    "council": {"count": 3, "role": "مجلس الولاية"},
    "judge": {"count": 1, "role": "قاضي الولاية"},
    "monitor": {"count": 1, "role": "مراقب الولاية"},
    "factory_manager": {"count": 1, "role": "مدير المصنع"},
    "worker": {"count": 10, "role": "عامل إنتاج"},
    "trainer": {"count": 1, "role": "مدرب"},
    "learner": {"count": 3, "role": "متعلم"},
    "accountant": {"count": 1, "role": "محاسب"},
}


class StateRuntime:
    """12.1: State Runtime — كل ولاية وحدة تشغيل معزولة."""

    def __init__(
        self,
        authorizer: ConstitutionalAuthorizer | None = None,
        royal_authorizer: ConstitutionalAuthorizer | None = None,
    ) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        StateBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)
        self._init_states()
        # المُصرِّحُ نفسُه لا مُصرِّحٌ ثانٍ. والفاعلُ **تنفيذيٌّ** بعدَ نقضِ سابقةِ 2A:
        # لا يُوسَمُ كائنُ التشغيلِ كلُّه بفاعلِ خزانةٍ (وهذا نصُّ ما منعَه Q-19)،
        # والصادقُ أنَّ عدَّ وحدةٍ تشغيليّةٍ في خدمةٍ تنفيذيّةٍ عملُ الفرعِ التنفيذيّ.
        self._authorizer = authorizer
        # مُصرِّحُ المسارِ الملكيِّ لـ`register_state` وحدَه (G1 § 9.8.1) — **يُمرَّرُ صريحًا ولا
        # يُبنى هنا** (سابقةُ Q-19: «من أرادَ فاعلًا آخرَ يُمرِّرُ مُصرِّحَه صريحًا»). وبلا
        # تمريرٍ يعبرُ السطحُ بالمُصرِّحِ التنفيذيِّ فيرفضُه الدستورُ (R-010-1 · R-010-5).
        self._royal_authorizer = royal_authorizer

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """المُصرِّحُ السياديُّ بالفاعلِ التنفيذيِّ الافتراضيّ — يُبنى عندَ أوّلِ حاجة.

        لا `actor=` هنا: الفاعلُ الافتراضيُّ في الجسرِ هو `EXECUTIVE`، فلا وسمَ
        جملةٍ بفرعٍ آخر. ومن أرادَ فاعلًا آخرَ يُمرِّرُ مُصرِّحَه صريحًا فيُقرأُ
        إعلانُه عندَ موضعِه لا يُخفى في بناءِ الخدمة.
        """
        if self._authorizer is None:
            self._authorizer = ConstitutionalAuthorizer()
        return self._authorizer

    # ── المسارُ القديمُ المُغلَق · 2A (والحدُّ باقٍ بعدَ نقضِها) ──────────
    def _allocate_budget_unguarded(self, state_id: str, amount: str) -> None:
        """مسارٌ **مُغلَقٌ** منذ 2A — يُرفَعُ دائمًا ولا يمسُّ ميزانيةً.

        نقضُ سابقةِ 2A غيَّرَ **الفعلَ والفاعلَ** لا الحدَّ: هذا المسارُ يبقى مُغلَقًا.

        هذا هو شكلُ الكتابةِ التي كانت تقعُ قبلَ 2A: قراءةُ الميزانيةِ وجمعُها
        وتثبيتُها بلا إذنٍ سياديٍّ ولا أثرٍ مُعلَنٍ ولا ذرّيّةٍ ولا معوّض. وبقاءُ
        التوقيعِ مقصودٌ: مَن أعادَه يرى رفضًا صريحًا لا أثرًا يقعُ بجانبِ الحدّ.
        """
        raise UndeclaredExecutionError(
            f"توزيعُ ميزانيةٍ مباشرٌ على الولاية «{state_id}» بمقدار «{amount}» "
            "لا يعبرُ حدَّ التنفيذِ السياديَّ. المسارُ الوحيدُ هو `allocate_budget` "
            "بإذنٍ سياديٍّ وأثرٍ مُعلَنٍ ومفتاحِ عمليّةٍ ومعوّضٍ يعكسُ الفرقَ فعلًا."
        )

    def _add_to_budget(self, state_id: str, delta: int) -> int | None:
        """أضِفْ إلى ميزانيةِ ولايةٍ فرقًا موقَّعًا — تُستعملُ للأثرِ وللعكسِ معًا.

        استعمالُها في المعوّضِ بفرقٍ سالبٍ يجعلُ العكسَ **حقيقيًّا**: الميزانيةُ
        تعودُ إلى قيمتِها لا إلى قيمةٍ يُظنُّ أنّها كانت. وترجعُ `None` إن غابت
        الولاية، فلا يُزعَمُ عكسٌ لما لا وجودَ له.
        """
        session = self._Session()
        try:
            state = session.query(StateModel).filter(StateModel.state_id == state_id).first()
            if not state:
                return None
            updated = int(state.budget or "0") + delta
            state.budget = str(updated)
            session.commit()
            return updated
        finally:
            session.close()

    def _init_states(self) -> None:
        """تهيئة الولايات التسع إذا لم تكن موجودة."""
        session = self._Session()
        try:
            for state_id, info in FEDERAL_STATES.items():
                existing = session.query(StateModel).filter(StateModel.state_id == state_id).first()
                if not existing:
                    state = StateModel(
                        state_id=state_id,
                        name=info["name"],
                        type=info["type"],
                        budget="1000",  # ميزانية أولية
                    )
                    session.add(state)
            session.commit()
        finally:
            session.close()

    def _delete_state_row(self, state_id: str) -> None:
        """معوِّضُ `register_state`: حذفُ الصفِّ الذي أنشأه العبور."""
        session = self._Session()
        try:
            session.query(StateModel).filter(StateModel.state_id == state_id).delete()
            session.commit()
        finally:
            session.close()

    def register_state(
        self,
        state_id: str,
        name: str,
        state_type: str,
        budget: str = "0",
        *,
        royal_decree: Any | None = None,
    ) -> dict[str, Any]:
        """12.8: تسجيل ولاية جديدة — عبرَ المسارِ الملكيِّ بمرسومٍ موقَّع (Q-13 · W-723).

        الفعلُ دستوريًّا `create_state` (G1 § 3.1): فاعلُه `ROYAL` والمرسومُ الموقَّعُ هوَ
        البوّابة. بلا مرسومٍ يرفعُ `classify` `RoyalImpersonation` قبلَ أيِّ كتابة،
        ومرسومٌ هدفُه غيرُ `state:{state_id}` يُرفَضُ قبلَ العبور.
        """
        session = self._Session()
        try:
            existing = session.query(StateModel).filter(StateModel.state_id == state_id).first()
            if existing:
                return {"error": "state_already_exists", "state_id": state_id}
        finally:
            session.close()

        target = f"state:{state_id}"
        if royal_decree is not None and getattr(royal_decree, "target", None) != target:
            raise DecreeTargetMismatchError(
                f"المرسومُ «{getattr(royal_decree, 'decree_id', '—')}» هدفُه "
                f"«{getattr(royal_decree, 'target', None)}» والمطلوبُ «{target}» — "
                "لا يُعادُ توجيهُ مرسومٍ إلى ولايةٍ أخرى."
            )
        decree_id = getattr(royal_decree, "decree_id", "—")
        effect = declared_effect(
            "CREATE",
            target,
            f"صفُّ ولايةٍ جديدةٍ «{state_id}» في federal_states بالمرسوم «{decree_id}»",
        )

        def _apply(_effect: Any) -> dict[str, Any]:
            session = self._Session()
            try:
                session.add(
                    StateModel(state_id=state_id, name=name, type=state_type, budget=budget)
                )
                session.commit()
            finally:
                session.close()
            PersistentAuditStore().append(
                "state.registered",
                "system",
                {"state_id": state_id, "name": name, "decree_id": decree_id},
            )
            return {
                "state_id": state_id,
                "name": name,
                "type": state_type,
                "budget": budget,
                "status": "active",
                "registered": True,
            }

        crossing = self._royal_authorizer if self._royal_authorizer is not None else self.authorizer
        guarded = crossing.guard_declared(
            ACTION_CREATE_STATE,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(CREATE_STATE_SCOPE, f"{state_id}:{decree_id}"),
            compensators=(
                compensator(
                    effect.signature,
                    lambda: self._delete_state_row(state_id),
                    "حذفُ صفِّ الولايةِ المُنشَأ",
                ),
            ),
            metadata={"state_id": state_id, "name": name, "type": state_type},
            royal_decree=royal_decree,
        )
        if guarded.is_replay:
            return {"state_id": state_id, "registered": False, "replayed": True}
        return {**guarded.value, "replayed": False}

    def get_state(self, state_id: str) -> dict[str, Any] | None:
        """تفاصيل ولاية."""
        session = self._Session()
        try:
            state = session.query(StateModel).filter(StateModel.state_id == state_id).first()
            if not state:
                return None
            return {
                "state_id": state.state_id,
                "name": state.name,
                "type": state.type,
                "status": state.status,
                "head_agent_id": state.head_agent_id,
                "budget": state.budget,
                "established_at": state.established_at.isoformat()
                if state.established_at
                else None,
            }
        finally:
            session.close()

    def list_states(self) -> list[dict[str, Any]]:
        """قائمة كل الولايات."""
        session = self._Session()
        try:
            states = session.query(StateModel).all()
            return [
                {
                    "state_id": s.state_id,
                    "name": s.name,
                    "type": s.type,
                    "status": s.status,
                    "budget": s.budget,
                }
                for s in states
            ]
        finally:
            session.close()

    # ── نوى خاصّةٌ للحالةِ وسجلِّ الإيقاف (تُنادى من المُطبِّقِ والمعوِّضِ فقط) ──
    def _state_status(self, state_id: str) -> str | None:
        session = self._Session()
        try:
            state = session.query(StateModel).filter(StateModel.state_id == state_id).first()
            return None if state is None else str(state.status)
        finally:
            session.close()

    def _set_status(self, state_id: str, status: str, *, expected: str | None = None) -> bool:
        """غيِّرْ حالةَ ولايةٍ — وإن مُرِّرَ `expected` فلا تمسَّ تحديثًا أحدث."""
        session = self._Session()
        try:
            state = session.query(StateModel).filter(StateModel.state_id == state_id).first()
            if state is None or (expected is not None and state.status != expected):
                return False
            state.status = status
            session.commit()
            return True
        finally:
            session.close()

    def _open_suspension_record(
        self, state_id: str, operation_id: str, previous: str, reason: str
    ) -> str:
        record_id = f"susp-{uuid.uuid4().hex[:12]}"
        session = self._Session()
        try:
            session.add(
                StateSuspensionRecord(
                    record_id=record_id,
                    state_id=state_id,
                    operation_id=operation_id,
                    previous_status=previous,
                    reason=reason,
                )
            )
            session.commit()
            return record_id
        finally:
            session.close()

    def _delete_suspension_records(self, state_id: str, operation_id: str) -> None:
        session = self._Session()
        try:
            session.query(StateSuspensionRecord).filter(
                StateSuspensionRecord.state_id == state_id,
                StateSuspensionRecord.operation_id == operation_id,
            ).delete()
            session.commit()
        finally:
            session.close()

    def _set_records_cleared(self, record_ids: list[str], cleared: bool) -> None:
        session = self._Session()
        try:
            for rec in (
                session.query(StateSuspensionRecord)
                .filter(StateSuspensionRecord.record_id.in_(record_ids))
                .all()
            ):
                rec.cleared_at = datetime.now(UTC) if cleared else None
            session.commit()
        finally:
            session.close()

    def _active_record_ids(self, state_id: str) -> list[str]:
        session = self._Session()
        try:
            return [
                r.record_id
                for r in session.query(StateSuspensionRecord)
                .filter(
                    StateSuspensionRecord.state_id == state_id,
                    StateSuspensionRecord.cleared_at.is_(None),
                )
                .all()
            ]
        finally:
            session.close()

    def has_governed_suspension(self, state_id: str) -> bool:
        """هل للولايةِ إيقافٌ محكومٌ نشط؟ — قراءةٌ لا كتابة (G1 § 9.6)."""
        return bool(self._active_record_ids(state_id))

    def _heal_reactivate_core(self, state_id: str) -> bool:
        """نواةُ `self_heal` الخاصّة (G1 § 5.3 و§ 9.8.2) — لا عبورَ ثانٍ داخلَ عبور.

        تُعيدُ تفعيلَ ولايةٍ معلَّقةٍ **بلا سجلٍّ محكومٍ نشط** فقط، وتُرجِعُ هل وقعَ الأثر.
        """
        if self.has_governed_suspension(state_id):
            return False
        return self._set_status(state_id, "active", expected="suspended")

    def suspend_state(
        self, state_id: str, reason: str = "", *, operation_id: str | None = None
    ) -> dict[str, Any]:
        """12.7: إيقاف ولاية — احتواءٌ محكومٌ عبرَ الحدِّ (Q-14 · W-723).

        الأثرُ المُعلَنُ يحملُ `state:{state_id}` والحالةَ السابقةَ والسببَ (G1 § 3.2 الشرطُ 1)،
        والمُطبِّقُ يكتبُ **سجلَّ الإيقافِ المحكوم** فلا ينقضُه `self_heal`.
        """
        previous = self._state_status(state_id)
        if previous is None:
            return {"error": "state_not_found"}
        op = operation_id or f"suspend-{uuid.uuid4().hex[:12]}"
        target = f"state:{state_id}"
        effect = declared_effect(
            "WRITE",
            f"{target}/status.{previous}->suspended@{op}",
            f"إيقافُ الولايةِ «{state_id}» (السابقُ: {previous}) — السبب: {reason or 'بلا سبب'}",
        )

        def _apply(_effect: Any) -> dict[str, Any]:
            self._set_status(state_id, "suspended")
            self._open_suspension_record(state_id, op, previous, reason)
            PersistentAuditStore().append(
                "state.suspended",
                "system",
                {"state_id": state_id, "reason": reason, "previous": previous, "op": op},
            )
            return {"state_id": state_id, "status": "suspended", "reason": reason}

        def _undo() -> None:
            self._delete_suspension_records(state_id, op)
            self._set_status(state_id, previous, expected="suspended")

        guarded = self.authorizer.guard_declared(
            ACTION_SUSPEND_STATE,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(SUSPEND_STATE_SCOPE, f"{state_id}:{previous}:{op}"),
            compensators=(compensator(effect.signature, _undo, "إرجاعُ الحالةِ السابقةِ وحذفُ السجل"),),
            metadata={"state_id": state_id, "previous_status": previous, "reason": reason},
        )
        if guarded.is_replay:
            return {"state_id": state_id, "status": "suspended", "replayed": True}
        return {**guarded.value, "previous_status": previous, "operation_id": op}

    def reactivate_state(self, state_id: str, *, operation_id: str | None = None) -> dict[str, Any]:
        """إعادة تفعيل ولاية — استعادةُ قدرةٍ عبرَ الحدِّ (`activate_agent` · ممنوعٌ عندَ ≥4).

        تُغلِقُ سجلَّ الإيقافِ المحكومِ النشط، والمعوِّضُ يُرجِعُ الحالةَ ويُعيدُ فتحَه.
        """
        previous = self._state_status(state_id)
        if previous is None:
            return {"error": "state_not_found"}
        records = self._active_record_ids(state_id)
        if previous == "active" and not records:
            # عمليّةٌ فارغةٌ لا تُقاس (سابقةُ E1): لا عبورَ لما لم يقع.
            return {"state_id": state_id, "status": "active", "noop": True}
        op = operation_id or f"reactivate-{uuid.uuid4().hex[:12]}"
        target = f"state:{state_id}"
        effect = declared_effect(
            "WRITE",
            f"{target}/status.{previous}->active@{op}",
            f"إعادةُ تفعيلِ الولايةِ «{state_id}» (السابقُ: {previous}) وإغلاقُ {len(records)} سجل",
        )

        def _apply(_effect: Any) -> dict[str, Any]:
            self._set_status(state_id, "active")
            self._set_records_cleared(records, True)
            return {"state_id": state_id, "status": "active"}

        def _undo() -> None:
            self._set_records_cleared(records, False)
            self._set_status(state_id, previous, expected="active")

        guarded = self.authorizer.guard_declared(
            ACTION_REACTIVATE_STATE,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(REACTIVATE_STATE_SCOPE, f"{state_id}:{previous}:{op}"),
            compensators=(
                compensator(effect.signature, _undo, "إرجاعُ الحالةِ السابقةِ وإعادةُ فتحِ السجل"),
            ),
            metadata={"state_id": state_id, "previous_status": previous},
        )
        if guarded.is_replay:
            return {"state_id": state_id, "status": "active", "replayed": True}
        return {**guarded.value, "previous_status": previous, "operation_id": op}

    def assign_agent(
        self, state_id: str, agent_id: str, role: str, *, operation_id: str | None = None
    ) -> dict[str, Any]:
        """12.6: تعيين وكيل في ولاية — عبرَ الحدِّ (`dispatch_agent` · ممنوعٌ عندَ ≥3)."""
        op = operation_id or f"assign-{uuid.uuid4().hex[:12]}"
        target = f"state:{state_id}/agent:{agent_id}"
        effect = declared_effect(
            "CREATE",
            f"{target}/row@{op}",
            f"صفُّ تعيينِ الوكيلِ «{agent_id}» بدورِ «{role}» في الولاية «{state_id}»",
        )
        created: list[int] = []

        def _apply(_effect: Any) -> dict[str, Any]:
            session = self._Session()
            try:
                row = StateAgentAssignment(state_id=state_id, agent_id=agent_id, role=role)
                session.add(row)
                session.commit()
                created.append(int(row.id))
            finally:
                session.close()
            return {"state_id": state_id, "agent_id": agent_id, "role": role, "assigned": True}

        def _undo() -> None:
            session = self._Session()
            try:
                if created:
                    session.query(StateAgentAssignment).filter(
                        StateAgentAssignment.id.in_(created)
                    ).delete(synchronize_session=False)
                    session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_ASSIGN_AGENT,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(ASSIGN_AGENT_SCOPE, f"{state_id}:{agent_id}:{op}"),
            compensators=(compensator(effect.signature, _undo, "حذفُ صفِّ التعيين"),),
            metadata={"state_id": state_id, "agent_id": agent_id, "role": role},
        )
        if guarded.is_replay:
            return {"state_id": state_id, "agent_id": agent_id, "role": role, "replayed": True}
        return {**guarded.value, "operation_id": op}

    def get_state_agents(self, state_id: str) -> list[dict[str, Any]]:
        """وكلاء ولاية معينة."""
        session = self._Session()
        try:
            assignments = (
                session.query(StateAgentAssignment)
                .filter(StateAgentAssignment.state_id == state_id)
                .all()
            )
            return [
                {
                    "agent_id": a.agent_id,
                    "role": a.role,
                    "assigned_at": a.assigned_at.isoformat() if a.assigned_at else None,
                }
                for a in assignments
            ]
        finally:
            session.close()

    def check_isolation(self, state_id: str) -> dict[str, Any]:
        """12.1: فحص العزل — ولاية لا تصل لأدوات ولاية أخرى."""
        session = self._Session()
        try:
            # كل ولاية لها وكلاؤها فقط
            state_agents = (
                session.query(StateAgentAssignment)
                .filter(StateAgentAssignment.state_id == state_id)
                .all()
            )
            other_states = (
                session.query(StateAgentAssignment)
                .filter(StateAgentAssignment.state_id != state_id)
                .all()
            )

            # فحص: هل هناك وكيل مشترك بين ولايتين؟
            state_agent_ids = {a.agent_id for a in state_agents}
            other_agent_ids = {a.agent_id for a in other_states}
            overlap = state_agent_ids & other_agent_ids

            return {
                "state_id": state_id,
                "isolated": len(overlap) == 0,
                "state_agents": len(state_agent_ids),
                "other_agents": len(other_agent_ids),
                "overlapping_agents": list(overlap),
            }
        finally:
            session.close()

    def allocate_budget(
        self,
        state_id: str,
        amount: str,
        reason: str = "",
        allocation_id: str | None = None,
    ) -> dict[str, Any]:
        """12.4: توزيع الميزانية الفدرالية — عبرَ حدِّ التنفيذِ السياديّ (2A · مَنقوضةً في W-019).

        الفرقُ عن ما قبلَ 2A ليس شكليًّا: الأثرُ يُعلَنُ قبلَ وقوعِه، والإذنُ من
        البوابةِ نفسِها، والعمليّةُ ذرّيّةٌ بمفتاحٍ، ولها معوّضٌ يعكسُ الفرقَ فعلًا.

        **وما نُقِضَ (W-019):** الفعلُ لم يعدُ `allocate_budget` الحصريَّ، والفاعلُ لم
        يعدُ خزانةً. فهذا العمودُ مقوَّمٌ بـ`amos-credit`، وقُضِيَ في Q-17 أنَّها وحدةُ
        قياسٍ تشغيليّةٌ لا مالٌ دستوريّ. فلا يُمارَسُ عليها حصرُ الخزانة، ولا يُقالُ
        للبوابةِ إنَّ مالًا عامًّا يتحرَّك. ولم يُنقَصِ حرسٌ: المراحلُ الإلزاميّةُ كلُّها
        قائمةٌ، و`allocate_budget` ما زالَ مرفوضًا على الفاعلِ التنفيذيِّ في البوابةِ نفسِها.

        `allocation_id` مفتاحُ العمليّةِ من المُنادي: توزيعانِ مقصودانِ بالمقدارِ
        نفسِه عمليّتانِ مختلفتانِ، فيُمرَّرُ لكلٍّ مفتاحُه. وإذا لم يُمرَّر اشتُقَّ
        المفتاحُ من (الولاية · المقدار · السبب)، فتكرارُ النداءِ نفسِه إعادةٌ لا
        توزيعٌ ثانٍ — وهذا هو الافتراضُ الآمن.
        """
        session = self._Session()
        try:
            state = session.query(StateModel).filter(StateModel.state_id == state_id).first()
            if not state:
                return {"error": "state_not_found"}
            current = int(state.budget or "0")
        finally:
            session.close()

        delta = int(amount)
        target = f"federal_states/{state_id}"
        effect = declared_effect(
            "WRITE",
            f"{target}/budget",
            f"توزيعُ ميزانيةٍ بمقدار {delta} {BUDGET_UNIT}: {reason or 'بلا سبب'}",
        )

        def _apply(_effect: Any) -> dict[str, Any]:
            """التطبيقُ الحقيقيّ: تغييرُ الميزانيةِ ثمّ تدقيقٌ دائم."""
            new_budget = self._add_to_budget(state_id, delta)
            if new_budget is None:  # pragma: no cover - فُحِصَ وجودُها قبلَ الحدّ
                raise BudgetAllocationError(
                    f"الولاية «{state_id}» غابت بينَ الفحصِ والتطبيق — لا أثرَ يُزعَم"
                )
            # الفاعلُ في التدقيقِ صادقٌ بعدَ النقض: من كتبَ هو زمنُ تشغيلِ الولاياتِ
            # لا الخزانةُ — ووحدةُ المبلغِ مُعلَنةٌ فلا يُقرأُ الرقمُ غدًا مالًا عامًّا.
            PersistentAuditStore().append(
                "state.budget_allocated",
                "state_runtime",
                {
                    "state_id": state_id,
                    "amount": amount,
                    "unit": BUDGET_UNIT,
                    "reason": reason,
                },
            )
            return {
                "state_id": state_id,
                "previous_budget": current,
                "new_budget": new_budget,
                "allocated": delta,
            }

        guarded = self.authorizer.guard_declared(
            ACTION_ALLOCATE_OPERATIONAL_CREDIT,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(
                BUDGET_OPERATION_SCOPE,
                allocation_id or f"{state_id}:{amount}:{reason}",
            ),
            compensators=(
                compensator(
                    effect.signature,
                    lambda: self._add_to_budget(state_id, -delta),
                    "طرحُ المقدارِ المُوزَّعِ من الميزانية — عكسٌ حقيقيٌّ للفرق",
                ),
            ),
            metadata={
                "state_id": state_id,
                "amount": amount,
                "unit": BUDGET_UNIT,
                "reason": reason,
            },
        )
        if guarded.is_replay:
            # إعادةٌ لمفتاحٍ مُثبَّت: لا توزيعَ ثانيًا. والصدقُ أن يُقال «أُعيدَ».
            return {
                "state_id": state_id,
                "previous_budget": current,
                "new_budget": current,
                "allocated": 0,
                "replayed": True,
                "operation_key": guarded.outcome.operation_key,
            }
        return {**guarded.value, "replayed": False}


class FederalMessageBus:
    """12.3: Federal Message Bus — توجيه الرسائل بين الولايات عبر فحص صلاحية."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        StateBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)
        self._authorizer = authorizer

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """المُصرِّحُ التنفيذيُّ الافتراضيّ — يُبنى عندَ أوّلِ حاجة.

        عبرَ `get_authorizer()` في الجسرِ (موضعُ بناءٍ افتراضيٌّ قائمٌ معدودٌ) لا بموضعِ
        بناءٍ جديد: الفاعلُ الافتراضيُّ `EXECUTIVE` نفسُه، ومن أرادَ غيرَه يُمرِّرُه صريحًا.
        """
        if self._authorizer is None:
            self._authorizer = get_authorizer()
        return self._authorizer

    def _delete_message(self, message_id: str) -> None:
        session = self._Session()
        try:
            session.query(StateMessage).filter(StateMessage.message_id == message_id).delete()
            session.commit()
        finally:
            session.close()

    def send_message(
        self, from_state: str, to_state: str, subject: str, body: str = ""
    ) -> dict[str, Any]:
        """إرسال رسالة بين ولايتين — فحصُ السياسةِ ثمَّ العبورُ (`coordinate` · ممنوعٌ عندَ ≥4).

        الفحصُ قراءةٌ قبلَ الحدّ، والكتابةُ (صفُّ الرسالةِ + التدقيق) داخلَ المُطبِّق.
        """
        message_id = f"msg-{uuid.uuid4().hex[:12]}"
        session = self._Session()
        try:
            # فحص السياسة: هل الولايتان موجودتان ونشطتان؟
            from_ok = (
                session.query(StateModel)
                .filter(StateModel.state_id == from_state, StateModel.status == "active")
                .first()
            )
            to_ok = (
                session.query(StateModel)
                .filter(StateModel.state_id == to_state, StateModel.status == "active")
                .first()
            )
        finally:
            session.close()
        policy_check = "approved" if (from_ok and to_ok) else "denied"

        target = f"msg:{message_id}"
        effect = declared_effect(
            "CREATE",
            target,
            f"صفُّ رسالةٍ {from_state} → {to_state} (فحصُ السياسة: {policy_check})",
        )

        def _apply(_effect: Any) -> dict[str, Any]:
            session = self._Session()
            try:
                session.add(
                    StateMessage(
                        message_id=message_id,
                        from_state=from_state,
                        to_state=to_state,
                        subject=subject,
                        body=body,
                        policy_check=policy_check,
                        delivered_at=datetime.now(UTC) if policy_check == "approved" else None,
                    )
                )
                session.commit()
            finally:
                session.close()
            PersistentAuditStore().append(
                "state.message_sent",
                from_state,
                {
                    "message_id": message_id,
                    "to": to_state,
                    "subject": subject,
                    "policy_check": policy_check,
                },
            )
            return {
                "message_id": message_id,
                "from_state": from_state,
                "to_state": to_state,
                "subject": subject,
                "policy_check": policy_check,
                "delivered": policy_check == "approved",
            }

        guarded = self.authorizer.guard_declared(
            ACTION_SEND_MESSAGE,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(SEND_MESSAGE_SCOPE, message_id),
            compensators=(
                compensator(
                    effect.signature,
                    lambda: self._delete_message(message_id),
                    "حذفُ صفِّ الرسالة",
                ),
            ),
            metadata={"from_state": from_state, "to_state": to_state, "policy": policy_check},
        )
        return dict(guarded.value)

    def get_messages(
        self, state_id: str, direction: str = "received", limit: int = 50
    ) -> list[dict[str, Any]]:
        """استقبال رسائل ولاية."""
        session = self._Session()
        try:
            if direction == "received":
                msgs = (
                    session.query(StateMessage)
                    .filter(StateMessage.to_state == state_id)
                    .order_by(StateMessage.created_at.desc())
                    .limit(limit)
                    .all()
                )
            else:
                msgs = (
                    session.query(StateMessage)
                    .filter(StateMessage.from_state == state_id)
                    .order_by(StateMessage.created_at.desc())
                    .limit(limit)
                    .all()
                )
            return [
                {
                    "message_id": m.message_id,
                    "from_state": m.from_state,
                    "to_state": m.to_state,
                    "subject": m.subject,
                    "body": m.body,
                    "policy_check": m.policy_check,
                    "created_at": m.created_at.isoformat() if m.created_at else None,
                }
                for m in msgs
            ]
        finally:
            session.close()


# Singletons
_state_runtime: StateRuntime | None = None
_message_bus: FederalMessageBus | None = None


def get_state_runtime() -> StateRuntime:
    global _state_runtime
    if _state_runtime is None:
        _state_runtime = StateRuntime()
    return _state_runtime


def get_federal_message_bus() -> FederalMessageBus:
    global _message_bus
    if _message_bus is None:
        _message_bus = FederalMessageBus()
    return _message_bus
