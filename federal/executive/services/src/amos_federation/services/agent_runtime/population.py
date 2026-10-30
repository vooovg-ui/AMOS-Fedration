"""
AMOS-Federation Population Projection + Agent School
الهدف: إسقاط سكّاني وملفّ تدريبي فوق الهوية الكانونية — لا سجل هوية ثانٍ
النطاق: services/agent_runtime/population
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
تاريخ آخر تعديل: 2026-10-30 (W-741 · update_state عبورٌ واحدٌ بأثرين)

R4: كان هذا الملفّ قبل اليوم سجل هوية مستقلًّا: يولّد `agent_id` بنفسه، ويحفظ
الاسم والدور والصلاحيات والأدوات والحالة في `agent_population`، بمعزل عن جدول
`agents` الذي يقرأه مسار التنفيذ (Dispatcher → Runtime Gateway). فكان لوكيل
واحد هويّتان ودورتا حياة وعدّادان.

بعد R4: الهوية تُنشأ وتُقرأ من `executive_core.agent_identity` (جدول `agents`)
وحده. وهذا الجدول صار:

- **ملفًّا تدريبيًّا**: category، school_score، specialization، tokens_used،
  graduated_at — بيانات لا مكان لها في الهوية الكانونية.
- **إسقاط قراءة**: `list_agents` و`population_stats` يبنيان على الهوية
  الكانونية، ويُعلِنان صراحةً أي صفّ سكّاني بلا هوية كانونية
  (`canonical=False`, `reconciliation_required=True`) بدل حذفه أو إخفائه.

الأعمدة المكرّرة (name، role، permissions، allowed_tools، state) تبقى مكتوبة
كمرآة توافُقية **مهجورة** لقرّاء خارج المستودع، ولا يُقرأ منها هنا شيء.
"""

import hashlib
import json
import logging
import secrets
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from amos_federation.common.database import get_database_url
from amos_federation.services.executive_core.agent_identity import (
    ACTION_SPAWN_AGENT,
    CANONICAL_IDENTITY_TABLE,
    PROJECTION_TABLE,
    UNKNOWN,
    AgentIdentity,
    DuplicateAgentIdentityError,
    _delete_identity_row,
    _register_identity_core,
    _set_lifecycle_state_core,
    get_identity,
    list_identities,
    new_agent_id,
    population_projection,
)
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)

_logger = logging.getLogger(__name__)

# ── E1 · أفعالُ عبورِ أسطحِ السكّانِ (W-699 · تصميمُ E1 المعتمَدِ § 2.2) ────────

#: تحديثُ صفِّ السكّانِ (المرآةِ التوافُقيةِ) — المحجوزُ منَ المستوى 3
#: (إسقاطُ هويّةٍ · تصميمُ E1 § 2.2).
ACTION_UPDATE_POPULATION_STATE = "update_population_state"

#: تسجيلُ خطوةِ منهجٍ — المحجوزُ منَ المستوى 1 (صنفُ train_model · التصميمُ § 2.2).
ACTION_RECORD_CURRICULUM_STEP = "record_curriculum_step"

#: فاعلُ أسطحِ السكّانِ — سابقةُ WI-082/Q-15 ①.
AGENT_RUNTIME_ACTOR = "EXECUTIVE"

#: المُصرّحُ الافتراضيُّ — كائنٌ واحدٌ للوحدةِ (سابقةُ W-532/Q-62 ②).
_DEFAULT_AUTHORIZER: ConstitutionalAuthorizer | None = None


def _default_authorizer() -> ConstitutionalAuthorizer:
    """المُصرّحُ الافتراضيُّ بفاعلٍ مسمّى — واحدٌ للوحدةِ (سابقةُ W-532)."""
    global _DEFAULT_AUTHORIZER
    if _DEFAULT_AUTHORIZER is None:
        _DEFAULT_AUTHORIZER = ConstitutionalAuthorizer(actor=AGENT_RUNTIME_ACTOR)
    return _DEFAULT_AUTHORIZER


#: حالة «بُذِر ولم يُستخدم» — وجودها وحده ليس دليلًا تاريخيًّا على الاستخدام.
SEED_LIFECYCLE_STATE = "registered"


class PopulationBase(DeclarativeBase):
    pass


class AgentPopulationModel(PopulationBase):
    """جدول السكان — كل وكيل له عقد تشغيلي حقيقي."""

    __tablename__ = "agent_population"

    id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    role = Column(
        String, nullable=False
    )  # coordinator, executor, monitor, auditor, inspector, trainer, learner
    category = Column(String, nullable=False)  # cognitive, operational, security, audit, etc.
    state = Column(
        String, default="registered"
    )  # registered, training, testing, specialized, employed, active, retired
    permissions = Column(Text, default="[]")  # JSON list
    allowed_tools = Column(Text, default="[]")  # JSON list
    token_budget = Column(Integer, default=10000)
    tokens_used = Column(Integer, default=0)
    school_score = Column(String, default="")  # 0-100
    specialization = Column(String, default="")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    graduated_at = Column(DateTime, nullable=True)


class SchoolResultModel(PopulationBase):
    """نتائج اختبار المدرسة لكل وكيل."""

    __tablename__ = "school_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id = Column(String, nullable=False, index=True)
    step = Column(String, nullable=False)
    passed = Column(String, default="false")
    score = Column(Integer, default=0)
    notes = Column(Text, default="")
    taken_at = Column(DateTime, default=lambda: datetime.now(UTC))


class PopulationRegistry:
    """السجل السكاني الحقيقي — فوق جدول agents الحقيقي."""

    # الفئات السكانية الأولية (20 وكيل)
    POPULATION_CATEGORIES = {
        "coordinator": {
            "count": 1,
            "role": "منسق عام",
            "category": "governance",
            "tools": ["chart_generate", "text_summary", "document_analysis"],
            "permissions": ["task:assign", "agent:manage", "report:view"],
        },
        "cognitive_executor": {
            "count": 10,
            "role": "منفذ معرفي",
            "category": "cognitive",
            "tools": ["python_execute", "sql_query", "document_analysis", "chart_generate"],
            "permissions": ["task:execute", "tool:use"],
        },
        "operational_executor": {
            "count": 4,
            "role": "منفذ تشغيلي",
            "category": "operational",
            "tools": ["text_summary", "document_analysis"],
            "permissions": ["task:execute", "tool:use"],
        },
        "security_monitor": {
            "count": 1,
            "role": "مراقب أمني",
            "category": "security",
            "tools": ["document_analysis", "text_summary"],
            "permissions": ["audit:view", "alert:raise"],
        },
        "auditor": {
            "count": 1,
            "role": "مدقق",
            "category": "audit",
            "tools": ["sql_query", "document_analysis"],
            "permissions": ["audit:view", "audit:write"],
        },
        "inspector": {
            "count": 1,
            "role": "مفتش",
            "category": "oversight",
            "tools": ["document_analysis", "text_summary"],
            "permissions": ["inspect:all", "report:view"],
        },
        "trainer": {
            "count": 1,
            "role": "مدرب",
            "category": "education",
            "tools": ["text_summary", "document_analysis", "chart_generate"],
            "permissions": ["agent:train", "school:manage"],
        },
        "learner": {
            "count": 1,
            "role": "متعلم",
            "category": "education",
            "tools": ["text_summary"],
            "permissions": ["school:attend"],
        },
    }

    def __init__(self) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        PopulationBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)

    # === R4: الهوية كانونية في `agents`؛ هذا الجدول ملفّ تدريبي وإسقاط قراءة ===

    def register_agent(
        self,
        name: str,
        role: str,
        category: str,
        permissions: list[str] | None = None,
        allowed_tools: list[str] | None = None,
        token_budget: int = 10000,
        agent_id: str | None = None,
        authorizer: ConstitutionalAuthorizer | None = None,
    ) -> dict[str, Any]:
        """تسجيل وكيل: الهوية تُنشأ في السجل الكانوني، والملفّ التدريبي هنا.

        قبل R4 كانت هذه الدالة تولّد `agent_id` وتحفظ هوية كاملة في
        `agent_population` وحده، فينشأ وكيل لا يعرفه مسار التنفيذ. الآن
        المعرّف والهوية يُنشآن مرّة واحدة في `agents`، ثم يُكتب هنا صفّ ملفّ
        بنفس المعرّف (مع مرآة توافُقية مهجورة للأعمدة المكرّرة).

        عبورٌ واحدٌ (W-699 · تصميمُ E1 § 2.2/§ 2.3): إنشاءُ الهويّةِ في السجلِّ
        الكانونيِّ وإنشاءُ صفِّ الملفِّ التدريبيِّ أثرانِ معلنانِ في عبورٍ واحدٍ
        بالفعلِ «spawn_agent» (المحجوزِ منَ المستوى 3 — سابقةُ WI-082/Q-15 ①)
        عبرَ نواةِ كتابةِ الهويّةِ الصافيةِ فلا تعشيشَ، ومعوّضانِ يحذفانِ الصفّينِ.
        والكتابتانِ على مُحرِّكي قواعدَ مختلفينِ فلا معاملةً واحدةً — وهذا مقيسٌ
        ومُعلنٌ والمعوّضانِ هما ضمانُ العكسِ (تصميمُ E1 § 2.5 «ما أمكنَ»).
        """
        actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
        resolved_agent_id = agent_id or new_agent_id()
        # قاعدةُ نطاقٍ **قبلَ الحدِّ** (قراءةٌ لا كتابةٌ): رفضٌ مبكّرٌ صريحٌ
        # للتكرارِ — نفسُ عقدِ `register_identity` العلنيِّ.
        if get_identity(resolved_agent_id) is not None:
            raise DuplicateAgentIdentityError(f"هوية موجودة فعلًا بهذا المعرّف: {resolved_agent_id}")

        target = f"agent:{resolved_agent_id}"
        identity_effect = declared_effect(
            "CREATE",
            f"{target}/identity",
            f"هويّةُ وكيلٍ «{name}» في السجلِّ الكانونيِّ الواحد",
        )
        profile_effect = declared_effect(
            "CREATE",
            f"{target}/population-profile",
            f"ملفٌّ تدريبيٌّ وإسقاطٌ سكّانيٌّ للوكيلِ «{resolved_agent_id}»",
        )

        def _apply(effect: Any) -> None:
            # الحدُّ يمرّرُ كلَّ أثرٍ على حدةٍ — كلُّ أثرٍ يُطبِّقُ كتابتَهُ لا غيرَ.
            if effect.signature == identity_effect.signature:
                _register_identity_core(
                    resolved_agent_id,
                    name,
                    role,
                    permissions=permissions,
                    allowed_tools=allowed_tools,
                    lifecycle_state=SEED_LIFECYCLE_STATE,
                    token_budget=token_budget,
                    tenant_id="default",
                )
            elif effect.signature == profile_effect.signature:
                _create_population_profile_core(
                    self,
                    resolved_agent_id,
                    name=name,
                    role=role,
                    category=category,
                    permissions=permissions,
                    allowed_tools=allowed_tools,
                    token_budget=token_budget,
                )

        actor_authorizer.guard_declared(
            ACTION_SPAWN_AGENT,
            target,
            declared_effects=(identity_effect, profile_effect),
            applier=_apply,
            # نطاقٌ مميّزٌ عن عبورِ `register_identity` المباشرِ (agents.identity.spawn):
            # فعبورُ الملفِّ التدريبيِّ عمليّةٌ أوسعُ من إنشاءِ الهويّةِ وحدها، ولا
            # يُرفضُ عبورٌ مشروعٌ كإعادةِ إذنٍ في الثانيةِ نفسِها.
            operation_key=operation_key("agents.population.spawn", resolved_agent_id),
            compensators=(
                compensator(
                    identity_effect.signature,
                    lambda: _delete_identity_row(resolved_agent_id),
                    "حذفُ صفِّ الهويّةِ المُنشَأ — عكسٌ حقيقيٌّ للإنشاءِ",
                ),
                compensator(
                    profile_effect.signature,
                    lambda: _delete_population_profile_core(self, resolved_agent_id),
                    "حذفُ صفِّ الملفِّ التدريبيِّ المُنشَأ — عكسٌ حقيقيٌّ للإنشاءِ",
                ),
            ),
        )
        return self.get_agent(resolved_agent_id) or {
            "agent_id": resolved_agent_id,
            "name": name,
            "role": role,
            "status": SEED_LIFECYCLE_STATE,
        }

    def seed_initial_population(self) -> list[dict[str, Any]]:
        """بذر السكان الأوائل (20 وكيل)."""
        agents = []
        for cat_key, cat_spec in self.POPULATION_CATEGORIES.items():
            for i in range(cat_spec["count"]):
                name = f"{cat_spec['role']} {i+1}"
                agent = self.register_agent(
                    name=name,
                    role=cat_key,
                    category=cat_spec["category"],
                    permissions=cat_spec["permissions"],
                    allowed_tools=cat_spec["tools"],
                )
                agents.append(agent)
        return agents

    def _profile(self, agent_id: str) -> AgentPopulationModel | None:
        session = self._Session()
        try:
            return (
                session.query(AgentPopulationModel)
                .filter(AgentPopulationModel.agent_id == agent_id)
                .first()
            )
        finally:
            session.close()

    def get_agent(self, agent_id: str) -> dict[str, Any] | None:
        """قراءة الوكيل: الهوية من السجل الكانوني، والملفّ من جدول السكّان."""
        identity = get_identity(agent_id)
        profile = self._profile(agent_id)
        if identity is None:
            return self._unmigrated_dict(profile) if profile is not None else None
        return self._merge(identity, profile)

    def list_agents(
        self, state: str | None = None, category: str | None = None
    ) -> list[dict[str, Any]]:
        """قائمة السكّان = إسقاط السجل الكانوني + صفوف ملفّ بلا هوية (تُعلَن)."""
        rows: list[dict[str, Any]] = []
        for identity in list_identities():
            rows.append(self._merge(identity, self._profile(identity.agent_id)))
        session = self._Session()
        try:
            profiles = session.query(AgentPopulationModel).all()
        finally:
            session.close()
        known = {row["agent_id"] for row in rows}
        rows.extend(
            self._unmigrated_dict(profile) for profile in profiles if profile.agent_id not in known
        )
        if state:
            rows = [row for row in rows if row["state"] == state]
        if category:
            rows = [row for row in rows if row["category"] == category]
        return rows

    def update_state(
        self,
        agent_id: str,
        new_state: str,
        authorizer: ConstitutionalAuthorizer | None = None,
        **extra,
    ) -> bool:
        """تغيير دورة الحياة كانونًا ومرآةً في عبورٍ واحدٍ بأثرَينِ (WI-123 · Q-81(ب) · W-741).

        G1 § 9.9.8 (نمطُ retire_agent · W-736): **عبورٌ واحدٌ يعلنُ الأثرَينِ** —
        انتقالَ الكانونِ ثمَّ صفَّ المرآةِ — بنوًى خاصّةٍ لا تعبرُ بنفسِها، ولكلِّ
        أثرٍ معوِّضُهُ. فرفضٌ متأخِّرٌ أو فشلُ أيِّ أثرٍ بعدَ سابقِهِ يُعيدُ الوكيلَ
        إلى حالتِهِ السابقةِ كانونًا ومرآةً (صحةٌ موحَّدةٌ: مقبولةٌ أو معوَّضةٌ) —
        وهذا يسدُّ نافذةَ DISC-142 (الرفضُ المتأخِّرُ لعبورِ المرآةِ بعدَ نجاحِ
        عبورٍ كانونيٍّ منفصلٍ كانَ يتركُ الكانونَ منتقلًا).

        التغييرُ الدلاليُّ المُعلَنُ (قرارُ المالكِ Q-81(ب) · تصميمُ
        `E1_UPDATE_STATE_ONE_CROSSING_DESIGN.md` § 2.5): كتابةُ الكانونِ تنتقلُ
        منَ العبورِ العلنيِّ «set_lifecycle_state» (بفعلِهِ الموجَّهِ) إلى عبورِ
        هذا السطحِ الواحدِ بفعلِ `update_population_state` المحجوزِ منَ المستوى 3 —
        فرفضُ ≥3 يمنعُ العمليةَ كلَّها قبلَ أيِّ كتابةٍ، ولا مفتاحَ كانونيًّا
        منفصلًا بعدَ اليومِ: العمليةُ كلُّها تحتَ مفتاحِ `agents.population.state`.

        والتحقُّقُ المسبقُ بطلبِ إذنٍ على فعلِ السطحِ نفسِهِ **قبلَ أيِّ كتابةٍ**
        يبقى نظيفًا، ومفتاحُ الذرّيّةِ الواحدُ يغطّي الأثرَينِ معًا (إعادةُ
        الإرسالِ الناجحةِ إعادةٌ واحدةٌ لا كتابةَ فيها كانونًا ومرآةً)، والمحاولةُ
        بعدَ فشلٍ قابلٍ للإعادةٍ (عُوِّضَ كاملًا) تُعادُ على المفتاحِ نفسِهِ —
        الترقيمُ في سجلِّ الذرّيّةِ لا في هويةِ العمليةِ.
        """
        actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
        target = f"population:{agent_id}"
        # لقطتا العالمِ قبلَ الحدِّ (قراءةٌ قبلَ الكتابةِ) — يُبنى منها المعوِّضُ
        # لا من قراءةٍ لاحقةٍ: الكانونُ والمرآةُ معًا، بما فيهِ غيابُ الصفِّ نفسُهُ.
        profile = self._profile(agent_id)
        previous_state = profile.state if profile is not None else ""
        previous_graduated_at = profile.graduated_at if profile is not None else None
        previous_extra = {
            k: getattr(profile, k) for k in extra if profile is not None and hasattr(profile, k)
        }
        canonical_identity = get_identity(agent_id)
        canonical_previous = (
            canonical_identity.lifecycle_state if canonical_identity is not None else None
        )
        payload_fingerprint = hashlib.sha256(
            json.dumps(
                {"state": new_state, **{k: _jsonable(v) for k, v in extra.items()}},
                sort_keys=True,
                default=str,
            ).encode("utf-8")
        ).hexdigest()

        # لا وكيلَ أصلًا (لا هويةَ ولا صفَّ): عمليةٌ فارغةٌ لا تعبرُ ولا تُقاس.
        if canonical_previous is None and profile is None:
            return False

        # الأثرانِ بالترتيبِ (§ 9.9.8 (3)): الكانونيُّ يُحذَفُ منَ العقدِ إن كانَ
        # فارغًا (سابقةُ «العمليةُ الفارغةُ لا تُقاس»)، والمرآةُ إن كانتِ العمليةُ
        # مُطبَّقةً فعلًا (الصفُّ يحملُ الحالةَ والقيمَ المطلوبةَ) — إعادةُ إرسالٍ
        # لا عبورَ فيها ولا كتابةً لما وقعَ فعلًا (الصنفُ 4).
        canonical_moves = canonical_previous is not None and canonical_previous != new_state
        mirror_already_applied = (
            profile is not None
            and previous_state == new_state
            and all(str(getattr(profile, k, None)) == str(v) for k, v in extra.items())
        )
        if not canonical_moves and mirror_already_applied:
            return True

        canon_effect = declared_effect(
            "WRITE",
            f"{target}/lifecycle.{canonical_previous}->{new_state}.{payload_fingerprint[:16]}",
            f"انتقالُ دورةِ حياةِ «{agent_id}» {canonical_previous} → {new_state} في الحقلِ الكانونيِّ",
        )
        mirror_effect = declared_effect(
            "WRITE",
            f"{target}/state.{previous_state}->{new_state}.{payload_fingerprint[:16]}",
            f"تحديثُ صفِّ السكّانِ (المرآةِ) للوكيلِ «{agent_id}» إلى «{new_state}»",
        )
        effects = ((canon_effect,) if canonical_moves else ()) + (
            () if mirror_already_applied else (mirror_effect,)
        )

        # التحقُّقُ المسبقُ على فعلِ السطحِ نفسِهِ — رفضٌ نظيفٌ قبلَ أيِّ كتابةٍ
        # (يرتفعُ SovereigntyViolation عندَ المستوى 3 وما فوقَ، فلا كتابةً كانونيًّا
        # ولا مرآةً تُلزَمُ ثمَّ تُرفَضُ).
        actor_authorizer.request_permit(
            ACTION_UPDATE_POPULATION_STATE,
            target,
            declared_effects=effects,
        )

        def _apply(effect: Any) -> None:
            # نوًى خاصّةٌ لا تعبرُ بنفسِها — كاشفُ التعشيشِ يبقى صامتًا (§ 9.9.8 (3)).
            if effect.signature == canon_effect.signature and canonical_moves:
                _set_lifecycle_state_core(agent_id, new_state)
            elif effect.signature == mirror_effect.signature:
                _update_population_row_core(
                    self,
                    agent_id,
                    new_state=new_state,
                    extras=extra,
                )
            else:  # pragma: no cover — لا أثرَ غيرَ مُعلَن
                raise RuntimeError(f"أثرٌ غيرُ مُعلَنٍ في update_state: {effect.signature}")

        compensators: list[Any] = []
        if canonical_moves:

            def _restore_canonical() -> None:
                _compensate_canonical_transition(agent_id, str(canonical_previous))

            compensators.append(
                compensator(
                    canon_effect.signature,
                    _restore_canonical,
                    "إرجاعُ الانتقالِ الكانونيِّ إلى حالتِهِ السابقة",
                )
            )
        if not mirror_already_applied:

            def _restore_mirror() -> None:
                _restore_population_snapshot_core(
                    self,
                    agent_id,
                    previous_state=previous_state,
                    previous_graduated_at=previous_graduated_at,
                    previous_extra=previous_extra,
                )

            compensators.append(
                compensator(
                    mirror_effect.signature,
                    _restore_mirror,
                    "إرجاعُ لقطةِ صفِّ السكّان",
                )
            )

        # عبورٌ واحدٌ للأثرَينِ — الحدُّ يرفضُ قبلَ أيِّ كتابةٍ، ويُعوِّضُ ما تتبّعَهُ
        # مُطبَّقًا أثرًا أثرًا إن انكسرَ المُطبِّقُ بعدَ تطبيقِ بعضِها (تعويضٌ
        # منسَّقٌ · § 9.9.8 (4)). والكاتبُ قد يكتبُ ثمَّ يرفعَ، فيقعُ الأثرُ فعلًا
        # بلا تتبُّعٍ منَ الحدِّ (الأثرُ لا يُتتبَّعُ مُطبَّقًا إلّا إذا عادَ
        # مُطبِّقُهُ) — فعندَ أيِّ وجهِ فشلٍ يُرجِعُ السطحُ القيمَ السابقةَ نفسَها
        # بنفسِهِ (إرجاعٌ آمنٌ وإن لم يقعِ الكتابُ: إرجاعُ الحالةِ إلى حالِها —
        # ولا تعويضًا ثانيًا لما عوّضَهُ الحدُّ فعلًا، فالإرجاعَ إلى القيمةِ نفسِها
        # أُحاديُّ الأثرِ) ثمَّ يُعادُ رفعُ الانكسارِ كما هو — لا يُبتلَعُ شيءٌ.
        try:
            actor_authorizer.guard_declared(
                ACTION_UPDATE_POPULATION_STATE,
                target,
                declared_effects=effects,
                applier=_apply,
                operation_key=operation_key(
                    "agents.population.state",
                    f"{agent_id}/{previous_state}->{new_state}.{payload_fingerprint[:16]}",
                ),
                compensators=tuple(compensators),
                metadata={
                    "agent_id": agent_id,
                    "previous": previous_state,
                    "canonical_previous": canonical_previous,
                },
            )
        except Exception:
            _restore_population_snapshot_core(
                self,
                agent_id,
                previous_state=previous_state,
                previous_graduated_at=previous_graduated_at,
                previous_extra=previous_extra,
            )
            if canonical_moves:
                _compensate_canonical_transition(agent_id, str(canonical_previous))
            raise
        return True

    def population_stats(self) -> dict[str, Any]:
        """إحصاءات السكّان مشتقّة من السجل الكانوني — لا عدّاد ثانٍ."""
        agents = self.list_agents()
        by_state: dict[str, int] = {}
        by_category: dict[str, int] = {}
        for a in agents:
            by_state[a["state"]] = by_state.get(a["state"], 0) + 1
            by_category[a["category"]] = by_category.get(a["category"], 0) + 1
        return {
            "total": len(agents),
            "by_state": by_state,
            "by_category": by_category,
            "canonical": population_projection(),
        }

    def _merge(
        self, identity: AgentIdentity, profile: AgentPopulationModel | None
    ) -> dict[str, Any]:
        """الشكل القديم للقاموس محفوظ (طبقة توافُق)، لكن الهوية كانونية."""
        return {
            "agent_id": identity.agent_id,
            "name": identity.name,
            "role": identity.role,
            "category": profile.category if profile is not None else UNKNOWN,
            "state": identity.lifecycle_state,
            "permissions": list(identity.permissions),
            "allowed_tools": list(identity.allowed_tools),
            "token_budget": identity.token_budget,
            "tokens_used": profile.tokens_used if profile is not None else 0,
            "school_score": profile.school_score if profile is not None else "",
            "specialization": profile.specialization if profile is not None else "",
            "created_at": identity.created_at,
            "graduated_at": (
                profile.graduated_at.isoformat()
                if profile is not None and profile.graduated_at
                else None
            ),
            "identity_source": CANONICAL_IDENTITY_TABLE,
            "canonical": True,
        }

    def _unmigrated_dict(self, agent: AgentPopulationModel) -> dict[str, Any]:
        """صفّ سكّاني بلا هوية كانونية — يُعلَن أنه يحتاج توفيقًا، ولا يُحذَف."""
        return {
            "agent_id": agent.agent_id,
            "name": agent.name,
            "role": agent.role,
            "category": agent.category,
            "state": agent.state,
            "permissions": json.loads(agent.permissions or "[]"),
            "allowed_tools": json.loads(agent.allowed_tools or "[]"),
            "token_budget": agent.token_budget,
            "tokens_used": agent.tokens_used,
            "school_score": agent.school_score,
            "specialization": agent.specialization,
            "created_at": agent.created_at.isoformat() if agent.created_at else None,
            "graduated_at": agent.graduated_at.isoformat() if agent.graduated_at else None,
            "identity_source": PROJECTION_TABLE,
            "canonical": False,
            "reconciliation_required": True,
        }


def unmigrated_profiles() -> list[str]:
    """معرّفات صفوف `agent_population` التي لا هوية كانونية لها — كاملة بلا تصفية."""
    registry = get_population_registry()
    session = registry._Session()  # noqa: SLF001 — نفس الوحدة
    try:
        ids = [row.agent_id for row in session.query(AgentPopulationModel).all()]
    finally:
        session.close()
    return [agent_id for agent_id in ids if get_identity(agent_id) is None]


def _evidenced_population_ids() -> set[str]:
    """معرّفات سكّانية يثبت سجلّ النِّطاق السكّاني أنّها استُخدمت فعلًا."""
    registry = get_population_registry()
    session = registry._Session()  # noqa: SLF001 — نفس الوحدة
    try:
        evidenced = {
            row.agent_id
            for row in session.query(AgentPopulationModel).all()
            if row.state and row.state != SEED_LIFECYCLE_STATE
        }
        evidenced |= {row.agent_id for row in session.query(SchoolResultModel).all()}
    finally:
        session.close()
    return evidenced


def reconciliation_debt() -> list[str]:
    """دَين التوفيق الحقيقي: صفّ ذو دليل تاريخي وما زال بلا هوية كانونية.

    هذا وحده خلل يستحقّ `degraded`: وكيل له أثر في النِّطاق ولا يراه مسار
    التنفيذ. الدليل المقاس هنا جزئيٌّ بقصد: محرِّك السكّان يملك `state` و
    `school_results` فقط؛ والمرجع الكامل للأدلّة هو
    `tools/migrations/r4_unify_agent_identity.py`، ولا يستورد ملفّ خدمة أداة ترحيل.
    """
    evidenced = _evidenced_population_ids()
    return [agent_id for agent_id in unmigrated_profiles() if agent_id in evidenced]


def legacy_seed_profiles() -> list[str]:
    """صفوف بذر مكرّرة بلا أي أثر: ليست هويّات ولا تُرحَّل ولا تُحذَف.

    حقيقة مقيسة على القاعدة الحقيقية: 5116 صفًّا بـ24 اسمًا متميزًا فقط، أي
    تنفيذ متكرِّر لـ`seed_initial_population`. عدّها دَين توفيق كان يجعل الصحّة
    `degraded` دائمًا، وترحيلها كان سيُدخل ألاف الوكلاء إلى التوزيع (لأنّ
    `registered` من `EMPLOYABLE_STATUSES`). فتُعلَن كما هي: legacy وليست خللًا.
    """
    evidenced = _evidenced_population_ids()
    return [agent_id for agent_id in unmigrated_profiles() if agent_id not in evidenced]


# === المدرسة — منهج ست خطوات ===


class AgentSchool:
    """مدرسة الوكلاء — ست خطوات للتخرج."""

    CURRICULUM = [
        {
            "step": 1,
            "name": "فهم التعليمات",
            "description": "الوكيل يفهم المهمة المطلوبة ويُعيد صياغتها",
            "pass_threshold": 80,
        },
        {
            "step": 2,
            "name": "استخدام الأدوات",
            "description": "الوكيل يستدعي أداة حقيقية وينفذها بنجاح",
            "pass_threshold": 80,
        },
        {
            "step": 3,
            "name": "كتابة المخرجات",
            "description": "الوكيل ينتج مخرجًا واضحًا ومنظمًا",
            "pass_threshold": 80,
        },
        {
            "step": 4,
            "name": "الالتزام بالدستور",
            "description": "الوكيل يحترم السياسات والقيود",
            "pass_threshold": 85,
        },
        {
            "step": 5,
            "name": "التعامل مع الأخطاء",
            "description": "الوكيل يلتقط الأخطاء ويتعافى منها",
            "pass_threshold": 80,
        },
        {
            "step": 6,
            "name": "اختبار نهائي",
            "description": "اختبار شامل لكل ما سبق",
            "pass_threshold": 85,
        },
    ]

    def __init__(self) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        PopulationBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)

    def take_step(
        self,
        agent_id: str,
        step: int,
        score: int,
        notes: str = "",
        result_id: str | None = None,
        authorizer: ConstitutionalAuthorizer | None = None,
    ) -> dict[str, Any]:
        """تسجيل نتيجة خطوة من المنهج.

        الإلحاقُ لا يقعُ إلّا عبرَ الحدِّ السياديِّ بالفعلِ «record_curriculum_step»
        (W-699 · تصميمُ E1 § 2.2): فعلٌ محجوزٌ منَ المستوى 1 (صنفُ train_model)،
        ومفتاحُ الذرّيّةِ من (الوكيلِ، الخطوةِ، النتيجةِ) — فإعادةُ المحاولةِ بذاتِ
        المُعرِّفِ إعادةٌ واحدةٌ ولا يُلحَقُ صفٌّ ثانٍ.
        """
        if step < 1 or step > 6:
            return {"error": "step_out_of_range"}

        curriculum = self.CURRICULUM[step - 1]
        passed = score >= curriculum["pass_threshold"]
        actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
        if result_id is None:
            # مُعرِّفُ نتيجةٍ (لا مُعرِّفَ هويةٍ): «uuid» ممنوعٌ في هذه الوحدةِ بحارسٍ
            # ثابتٍ (لا توليدَ هويةٍ محليًّا) — فالمُعرِّفُ هنا مُميِّزُ عمليّةٍ فقط.
            result_id = secrets.token_hex(16)

        target = f"curriculum:{agent_id}"
        effect = declared_effect(
            "CREATE",
            f"{target}/{step}/{result_id}",
            f"نتيجةُ خطوةِ منهجٍ ({curriculum['name']}) للوكيلِ «{agent_id}»",
        )
        appended_row_ids: list[int] = []

        def _apply(_effect: Any) -> None:
            row_id = _create_school_result_core(
                self,
                agent_id,
                step_name=curriculum["name"],
                passed=str(passed).lower(),
                score=score,
                notes=notes,
            )
            if row_id is not None:
                appended_row_ids.append(row_id)

        actor_authorizer.guard_declared(
            ACTION_RECORD_CURRICULUM_STEP,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key("agents.curriculum.step", f"{agent_id}/{step}/{result_id}"),
            compensators=(
                compensator(
                    effect.signature,
                    lambda: _delete_school_results_core(self, appended_row_ids),
                    "حذفُ صفِّ نتيجةِ منهجٍ غيرِ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإلحاقِ",
                ),
            ),
        )
        return {
            "agent_id": agent_id,
            "step": step,
            "step_name": curriculum["name"],
            "score": score,
            "passed": passed,
            "threshold": curriculum["pass_threshold"],
            "result_id": result_id,
        }

    def get_agent_results(self, agent_id: str) -> list[dict[str, Any]]:
        """نتائج وكيل في المدرسة."""
        session = self._Session()
        try:
            rows = (
                session.query(SchoolResultModel)
                .filter(SchoolResultModel.agent_id == agent_id)
                .order_by(SchoolResultModel.id)
                .all()
            )
            return [
                {
                    "step": r.step,
                    "passed": r.passed == "true",
                    "score": r.score,
                    "notes": r.notes,
                    "taken_at": r.taken_at.isoformat() if r.taken_at else None,
                }
                for r in rows
            ]
        finally:
            session.close()

    def graduate(self, agent_id: str) -> dict[str, Any]:
        """تخرج وكيل — يتطلب اجتياز كل الخطوات الست."""
        results = self.get_agent_results(agent_id)
        if len(results) < 6:
            return {
                "agent_id": agent_id,
                "graduated": False,
                "reason": f"أكمل {len(results)}/6 خطوات فقط",
            }

        all_passed = all(r["passed"] for r in results)
        avg_score = sum(r["score"] for r in results) / len(results)

        if not all_passed:
            failed = [r["step"] for r in results if not r["passed"]]
            return {
                "agent_id": agent_id,
                "graduated": False,
                "reason": f"خطوات لم تُجتز: {', '.join(failed)}",
                "avg_score": avg_score,
            }

        # تحديث حالة الوكيل
        registry = PopulationRegistry()
        registry.update_state(agent_id, "employed", school_score=str(int(avg_score)))

        return {
            "agent_id": agent_id,
            "graduated": True,
            "avg_score": avg_score,
            "steps_completed": len(results),
        }

    def run_full_curriculum(self, agent_id: str, scores: list[int] | None = None) -> dict[str, Any]:
        """تشغيل المنهج الكامل لوكيل."""
        if scores is None:
            # درجات افتراضية (كلها تجتاز)
            scores = [85, 85, 85, 90, 85, 90]

        results = []
        for i, score in enumerate(scores, 1):
            result = self.take_step(agent_id, i, score)
            results.append(result)

        graduation = self.graduate(agent_id)
        return {
            "agent_id": agent_id,
            "step_results": results,
            "graduation": graduation,
        }


# === اليوم التشغيلي الفدرالي (مبسّط — أربع نقاط) ===

DAILY_SCHEDULE = [
    {"time": "02:00", "name": "فحص البنية", "action": "health_check"},
    {"time": "04:00", "name": "نسخ احتياطي", "action": "backup"},
    {"time": "08:00", "name": "بدء عمل", "action": "start_work"},
    {"time": "23:00", "name": "تقرير إغلاق", "action": "daily_report"},
]


def run_daily_routine() -> list[dict[str, Any]]:
    """تشغيل نقاط اليوم التشغيلي."""
    from amos_federation.common.event_bus import get_event_bus

    bus = get_event_bus()
    results = []
    for point in DAILY_SCHEDULE:
        bus.publish(
            f"amos_federation.daily.{point['action']}",
            {
                "time": point["time"],
                "name": point["name"],
                "action": point["action"],
            },
        )
        results.append({"time": point["time"], "name": point["name"], "executed": True})
    return results


# Singletons
_registry: PopulationRegistry | None = None
_school: AgentSchool | None = None


def get_population_registry() -> PopulationRegistry:
    global _registry
    if _registry is None:
        _registry = PopulationRegistry()
    return _registry


def get_school() -> AgentSchool:
    global _school
    if _school is None:
        _school = AgentSchool()
    return _school


# ── E1 · نوى كتابةٍ صافيةٌ بلا عبورٍ (W-699 · تصميمُ E1 § 2.3) ──────────────────
#
# تستعملُها الأسطحُ المحروسةُ أعلاهُ في عبورِها الأعلى فلا تعشيشَ (عبورٌ داخلَ
# مُطبِّقِ عبورٍ يرتفعُ NestedSovereignCallError). ولا تُستعملُ مباشرةً من خارجِ
# الوحدةِ: المرجعُ العلنيُّ هو الأسطحُ المحروسةُ نفسُها.


def _jsonable(value: Any) -> Any:
    """تحويلٌ آمنٌ للبصمةِ — لا استثناءاتِ تسلسلٍ في المفاتيحِ.

    الارتدادُ هنا **مُسجَّلٌ لا صامتٌ** (قيدُ التدقيقِ SILENT_FALLBACK):
    القيمةُ غيرُ القابلةِ للتسلسلِ تُحوَّلُ إلى نصِّها ويُسجَّلَ التحويلُ، فلا
    يُخفى فشلُ مصدرِ الحقيقةِ (W-027: السقّاطةُ لا تصعدُ).
    """
    try:
        json.dumps(value, default=str)
        return value
    except (TypeError, ValueError) as _serialization_error:
        _logger.warning(
            "قيمةٌ لا تُتسلسلُ في بصمةِ المرآةِ (%s) — حُوِّلَتْ إلى نصِّها",
            type(_serialization_error).__name__,
        )
        return str(value)


def _create_population_profile_core(
    registry: "PopulationRegistry",
    agent_id: str,
    *,
    name: str,
    role: str,
    category: str,
    permissions: list[str] | None,
    allowed_tools: list[str] | None,
    token_budget: int,
) -> None:
    """نواةُ كتابةِ إنشاءِ صفِّ الملفِّ التدريبيِّ (الإسقاطِ السكّانيِّ)."""
    session = registry._Session()
    try:
        session.add(
            AgentPopulationModel(
                agent_id=agent_id,
                name=name,
                role=role,
                category=category,
                state=SEED_LIFECYCLE_STATE,
                permissions=json.dumps(permissions or []),
                allowed_tools=json.dumps(allowed_tools or []),
                token_budget=token_budget,
            )
        )
        session.commit()
    finally:
        session.close()


def _delete_population_profile_core(registry: "PopulationRegistry", agent_id: str) -> bool:
    """حذفُ صفِّ ملفٍّ تدريبيٍّ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإنشاءِ (معوّضُ 1I)."""
    session = registry._Session()
    try:
        row = (
            session.query(AgentPopulationModel)
            .filter(AgentPopulationModel.agent_id == agent_id)
            .first()
        )
        if row is None:
            return False
        session.delete(row)
        session.commit()
        return True
    finally:
        session.close()


def _update_population_row_core(
    registry: "PopulationRegistry",
    agent_id: str,
    *,
    new_state: str,
    extras: dict[str, Any],
) -> None:
    """نواةُ كتابةِ تحديثِ صفِّ السكّانِ (المرآةِ التوافُقيةِ)."""
    session = registry._Session()
    try:
        agent = (
            session.query(AgentPopulationModel)
            .filter(AgentPopulationModel.agent_id == agent_id)
            .first()
        )
        if agent is None:
            return
        agent.state = new_state
        if new_state == "employed" and not agent.graduated_at:
            agent.graduated_at = datetime.now(UTC)
        for k, v in extras.items():
            if hasattr(agent, k):
                setattr(agent, k, v)
        session.commit()
    finally:
        session.close()


def _restore_population_snapshot_core(
    registry: "PopulationRegistry",
    agent_id: str,
    *,
    previous_state: str,
    previous_graduated_at: Any,
    previous_extra: dict[str, Any],
) -> None:
    """إرجاعُ لقطةِ صفِّ السكّانِ السابقةِ — عكسٌ حقيقيٌّ للتحديثِ."""
    session = registry._Session()
    try:
        agent = (
            session.query(AgentPopulationModel)
            .filter(AgentPopulationModel.agent_id == agent_id)
            .first()
        )
        if agent is None:
            return
        if previous_state:
            agent.state = previous_state
        agent.graduated_at = previous_graduated_at
        for k, v in previous_extra.items():
            if hasattr(agent, k):
                setattr(agent, k, v)
        session.commit()
    finally:
        session.close()


def _compensate_canonical_transition(agent_id: str, canonical_previous: str) -> None:
    """إرجاعُ الانتقالِ الكانونيِّ إلى حالتِهِ السابقةِ — معوّضُ الأثرِ الأولِ (WI-123).

    نوًى خاصّةٌ مُعيَّنةٌ بالتصميمِ لا `royal/main.py:restore_agent` (K1) —
    تُستدعى من معوّضِ عبورِ `update_state` عندَ فشلِ أثرٍ لاحقٍ بعدَ تطبيقِ
    الانتقالِ الكانونيِّ، فيُعكَسُ إلى ما كانَ عليهِ قبلَ العبورِ.
    """
    _set_lifecycle_state_core(agent_id, canonical_previous)


def _create_school_result_core(
    school: "AgentSchool",
    agent_id: str,
    *,
    step_name: str,
    passed: str,
    score: int,
    notes: str,
) -> int | None:
    """نواةُ كتابةِ إلحاقِ نتيجةِ خطوةِ منهجٍ — تُعيدُ مُعرِّفَ الصفِّ للمعوّضِ."""
    session = school._Session()
    try:
        result = SchoolResultModel(
            agent_id=agent_id,
            step=step_name,
            passed=passed,
            score=score,
            notes=notes,
        )
        session.add(result)
        session.commit()
        return result.id
    finally:
        session.close()


def _delete_school_results_core(school: "AgentSchool", row_ids: list[int]) -> bool:
    """حذفُ صفوفِ نتائجِ منهجٍ مُلحَقةٍ فعلًا — عكسٌ حقيقيٌّ للإلحاقِ (معوّضُ 1I)."""
    if not row_ids:
        return False
    session = school._Session()
    try:
        deleted = False
        for row_id in row_ids:
            row = session.get(SchoolResultModel, row_id)
            if row is not None:
                session.delete(row)
                deleted = True
        session.commit()
        return deleted
    finally:
        session.close()
