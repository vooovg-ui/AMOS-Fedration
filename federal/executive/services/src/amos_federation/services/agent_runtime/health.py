"""
AMOS-Federation Agent Health System
الهدف: النظام الصحي المؤسسي للوكلاء — فحص دوري، علاج، عزل
النطاق: services/agent_runtime/health
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
"""

import hashlib
import json
import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import (
    JSON,
    Column,
    DateTime,
    Float,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase

from amos_federation.common.database import get_database_url, get_session_factory
from amos_federation.services.executive_core.agent_identity import (
    ACTION_ACTIVATE_AGENT,
    ACTION_CONTAIN_AGENT,
    AgentLifecycleState,
    IdentityLedgerDivergenceError,
    _set_lifecycle_state_core,
    get_identity,
    set_lifecycle_state,
)
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)

# ── E1 · أفعالُ عبورِ أسطحِ وقتِ التشغيلِ (W-699 · تصميمُ E1 المعتمَدِ § 2.2) ────

#: فحصُ صحةِ الوكيلِ — بلا منعٍ عندَ أيِّ مستوىً (التصميمُ § 2.2 قاعدةٌ 3).
ACTION_RUN_HEALTH_CHECK = "run_health_check"

#: بدءُ علاجِ الوكيلِ — المحجوزُ منَ المستوى 1 (صنفُ train_model · التصميمُ § 2.2).
ACTION_START_AGENT_TREATMENT = "start_agent_treatment"

#: عزلُ الوكيلِ — أداةُ الإيقافِ نفسُها لا تُمنَعُ عندَ أيِّ مستوىً (قاعدةٌ 3).
ACTION_ISOLATE_AGENT = "isolate_agent"

#: إلحاقُ فعلٍ بسجلِّ العزلِ — بلا منعٍ عندَ أيِّ مستوىً (قاعدةٌ 3).
ACTION_LOG_ISOLATED_ACTION = "log_isolated_action"

#: رفعُ العزلِ — الفعلُ بلا منعٍ عالميًّا والاتجاهُ يُحرسُ بالتحققِ المسبقِ
#: (تصميمُ E1 § 2.2 · تعليقُ قواعدِ W-696): retire⇒`contain_agent` ·
#: release⇒`activate_agent` المحجوزِ منَ المستوى 4 · retrain⇒`start_agent_treatment`
#: المحجوزِ منَ المستوى 1 — والتحققُ يقعُ قبلَ أيِّ كتابةٍ فلا حالةٌ ناقصة.
ACTION_RELEASE_AGENT = "release_agent"

#: فاعلُ أسطحِ وقتِ التشغيلِ — سابقةُ WI-082/Q-15 ①: الفاعلُ يُعلَنُ تنفيذيًّا
#: ولا يُثبَّتُ، والمُصرِّحُ يبقى قابلًا للتمريرِ صراحةً.
AGENT_RUNTIME_ACTOR = "EXECUTIVE"

#: المُصرِّحُ الافتراضيُّ — كائنٌ واحدٌ للوحدةِ (سابقةُ W-532/Q-62 ②).
_DEFAULT_AUTHORIZER: ConstitutionalAuthorizer | None = None


def _default_authorizer() -> ConstitutionalAuthorizer:
    """المُصرِّحُ الافتراضيُّ بفاعلٍ مسمّى — واحدٌ للوحدةِ (سابقةُ W-532)."""
    global _DEFAULT_AUTHORIZER
    if _DEFAULT_AUTHORIZER is None:
        _DEFAULT_AUTHORIZER = ConstitutionalAuthorizer(actor=AGENT_RUNTIME_ACTOR)
    return _DEFAULT_AUTHORIZER


# === Health Check Model ===


class _HealthBase(DeclarativeBase):
    """قاعدة نماذج الفحص الصحي."""

    pass


class AgentHealthCheckModel(_HealthBase):
    """جدول فحوصات الوكلاء الصحية."""

    __tablename__ = "agent_health_checks"

    id = Column(String, primary_key=True)
    agent_id = Column(String, nullable=False, index=True)
    check_date = Column(DateTime, default=lambda: datetime.now(UTC))
    status = Column(String, nullable=False)  # healthy / monitor / treatment / isolated
    performance_score = Column(Float, default=0.0)
    resource_usage = Column(JSON, default=dict)
    policy_compliance = Column(Float, default=0.0)
    tool_success_rate = Column(Float, default=0.0)
    error_rate = Column(Float, default=0.0)
    findings = Column(JSON, default=list)
    recommendations = Column(JSON, default=list)
    prev_hash = Column(String, nullable=False, default="0" * 64)
    hash = Column(String, nullable=False, default="")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class IsolationRecordModel(_HealthBase):
    """جدول سجلات العزل."""

    __tablename__ = "agent_isolations"

    id = Column(String, primary_key=True)
    agent_id = Column(String, nullable=False, index=True)
    isolated_at = Column(DateTime, default=lambda: datetime.now(UTC))
    reason = Column(Text, nullable=False)
    sandbox_id = Column(String, nullable=True)
    actions_log = Column(JSON, default=list)  # كل فعل أثناء العزل
    status = Column(String, default="active")  # active / released / retired
    released_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class TreatmentRecordModel(_HealthBase):
    """جدول سجلات العلاج."""

    __tablename__ = "agent_treatments"

    id = Column(String, primary_key=True)
    agent_id = Column(String, nullable=False, index=True)
    treatment_type = Column(
        String, nullable=False
    )  # retrain / replace_model / fix_tool / reset_context
    started_at = Column(DateTime, default=lambda: datetime.now(UTC))
    completed_at = Column(DateTime, nullable=True)
    status = Column(String, default="in_progress")  # in_progress / completed / failed
    details = Column(JSON, default=dict)
    result = Column(JSON, default=dict)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


# === Health Status Enum ===

HEALTHY = "healthy"
MONITOR = "monitor"
TREATMENT = "treatment"
ISOLATED = "isolated"

ALL_STATUSES = [HEALTHY, MONITOR, TREATMENT, ISOLATED]


# === Health Checker ===


class HealthChecker:
    """الفاحص الصحي للوكلاء — يفحص كل وكيل دوريًا."""

    def __init__(self) -> None:
        self._ensure_tables()

    def _ensure_tables(self) -> None:
        """إنشاء جداول الفحص الصحي إذا لم تكن موجودة."""
        url = get_database_url()
        connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
        engine = create_engine(url, connect_args=connect_args)
        _HealthBase.metadata.create_all(engine)

    def _compute_hash(self, action: str, actor: str, details: dict, prev_hash: str) -> str:
        """حساب SHA-256 hash للفحص (تماثل سلسلة التدقيق)."""
        import hashlib

        payload = json.dumps(
            {
                "action": action,
                "actor": actor,
                "details": details,
                "prev_hash": prev_hash,
            },
            sort_keys=True,
            default=str,
        )
        return hashlib.sha256(payload.encode()).hexdigest()

    def check_agent(
        self,
        agent_id: str,
        check_id: str | None = None,
        authorizer: ConstitutionalAuthorizer | None = None,
    ) -> dict[str, Any]:
        """
        8.1: فحص وكيل واحد — الأداء، استهلاك الموارد، الالتزام بالسياسات.
        النتيجة واحدة من أربع: سليم / مراقبة / علاج / عزل.

        كتابةُ سجلِّ الفحصِ لا تقعُ إلّا عبرَ الحدِّ السياديِّ بالفعلِ «run_health_check»
        (W-699 · تصميمُ E1 § 2.2): فعلٌ بلا منعٍ عندَ أيِّ مستوىً (قاعدةٌ 3) وأثرٌ
        مُعلنٌ ومعوّضٌ حقيقيٌّ (حذفُ صفِّ الفحصِ) ومفتاحُ ذرّيّةٍ من (الوكيلِ، الفحصِ) —
        فإعادةُ المحاولةِ بذاتِ «check_id» إعادةٌ واحدةٌ ولا يُلحَقُ السجلُّ مرتينِ.
        """
        from amos_federation.common.persistent import PersistentExperienceStore

        # R4: الهوية والقدرات تُقرآن من السجل الكانوني `agents`، لا من جدول
        # السكّان. جدول السكّان صار إسقاطًا وملفًّا تدريبيًّا لا مصدر هوية.
        identity = get_identity(agent_id)
        if identity is None:
            raise ValueError(f"الوكيل {agent_id} غير موجود")
        agent = identity.as_dict()

        # جمع البيانات الحقيقية
        exp_store = PersistentExperienceStore()
        experiences = exp_store.list_all(agent_id=agent_id, limit=50)

        # حساب الأداء
        if experiences:
            scores = [
                e.get("quality_score", 0.5)
                for e in experiences
                if e.get("quality_score") is not None
            ]
            performance_score = sum(scores) / len(scores) if scores else 0.5
        else:
            performance_score = 0.5  # لا خبرات بعد

        # معدل نجاح الأدوات (من الخبرات)
        tool_successes = sum(1 for e in experiences if e.get("outcome", {}).get("success", True))
        tool_success_rate = tool_successes / len(experiences) if experiences else 1.0

        # معدل الأخطاء
        error_count = sum(1 for e in experiences if not e.get("outcome", {}).get("success", True))
        error_rate = error_count / len(experiences) if experiences else 0.0

        # الالتزام بالسياسات (من سجل التدقيق)
        from amos_federation.common.persistent import PersistentAuditStore

        audit = PersistentAuditStore()
        audit_entries = audit.list_all(limit=100)
        policy_violations = sum(
            1 for a in audit_entries if "violation" in a.get("action", "").lower()
        )
        policy_compliance = 1.0 - (policy_violations / max(len(audit_entries), 1))

        # استهلاك الموارد
        resource_usage = {
            "token_budget": agent.get("token_budget", 10000),
            "tokens_used": sum(e.get("outcome", {}).get("tokens_used", 0) for e in experiences),
            "tools_available": len(agent.get("allowed_tools", [])),
        }

        # تحديد الحالة الصحية
        findings: list[str] = []
        recommendations: list[str] = []

        if performance_score < 0.3 or error_rate > 0.5:
            status = ISOLATED
            findings.append(f"أداء حرج: {performance_score:.1%}، معدل أخطاء: {error_rate:.1%}")
            recommendations.append("عزل فوري وإعادة تقييم شامل")
        elif performance_score < 0.5 or error_rate > 0.3 or policy_compliance < 0.7:
            status = TREATMENT
            findings.append(f"أداء منخفض: {performance_score:.1%}")
            if error_rate > 0.3:
                recommendations.append("إعادة تدريب عبر المدرسة")
            if policy_compliance < 0.7:
                recommendations.append("مراجعة السياسات")
        elif performance_score < 0.7 or error_rate > 0.1 or policy_compliance < 0.9:
            status = MONITOR
            findings.append(f"أداء دون المستهدف: {performance_score:.1%}")
            recommendations.append("مراقبة مستمرة لمدة دورة كاملة")
        else:
            status = HEALTHY
            findings.append(f"أداء جيد: {performance_score:.1%}")

        # عبورُ كتابةِ سجلِّ الفحصِ (W-699 · تصميمُ E1 § 2.2): القراءاتُ كلُّها فوقَ
        # وقعتْ، والكتابةُ لا تقعُ إلّا بإذنٍ دستوريٍّ — والمعوّضُ حذفُ صفِّ الفحصِ.
        actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
        if check_id is None:
            check_id = str(uuid.uuid4())
        target = f"health_check:{agent_id}"
        effect = declared_effect(
            "CREATE",
            f"{target}/{check_id}",
            f"سجلُّ فحصٍ للوكيلِ «{agent_id}» ({status})",
        )

        def _apply(_effect: Any) -> None:
            _write_health_check_core(
                check_id,
                agent_id=agent_id,
                status=status,
                performance_score=performance_score,
                resource_usage=resource_usage,
                policy_compliance=policy_compliance,
                tool_success_rate=tool_success_rate,
                error_rate=error_rate,
                findings=findings,
                recommendations=recommendations,
            )

        actor_authorizer.guard_declared(
            ACTION_RUN_HEALTH_CHECK,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key("agents.health.check", f"{agent_id}/{check_id}"),
            compensators=(
                compensator(
                    effect.signature,
                    lambda: _delete_health_check_core(check_id),
                    "حذفُ صفِّ فحصٍ غيرِ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإلحاقِ",
                ),
            ),
        )
        # الصدقُ أن يُقرأَ الأثرُ بعدَ العبورِ لا أن يُفترَضَ — وإعادةُ الإرسالِ بذاتِ
        # المفتاحِ تُعادُ نتيجتُها منَ الحقلِ الدائمِ بلا إلحاقٍ ثانٍ.
        check_hash = _health_check_hash(check_id)

        # نشر حدث
        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.health.check_completed",
            {
                "agent_id": agent_id,
                "status": status,
                "performance_score": performance_score,
            },
        )

        return {
            "check_id": check_id,
            "agent_id": agent_id,
            "status": status,
            "performance_score": performance_score,
            "resource_usage": resource_usage,
            "policy_compliance": policy_compliance,
            "tool_success_rate": tool_success_rate,
            "error_rate": error_rate,
            "findings": findings,
            "recommendations": recommendations,
            "hash": check_hash,
        }

    def check_all_agents(self, limit: int = 50) -> list[dict[str, Any]]:
        """فحص الوكلاء المسجلين (مع حد لتجنب عنق الزجاجة)."""
        from amos_federation.services.executive_core.agent_identity import list_identities

        # R4: قائمة من يُفحَص تأتي من السجل الكانوني.
        identities = list_identities()
        # تقييد العدد لتجنب عنق الزجاجة عند وجود مئات الوكلاء
        results = []
        for identity in identities[:limit]:
            results.append(self.check_agent(identity.agent_id))
        return results

    def get_agent_health_history(self, agent_id: str, limit: int = 30) -> list[dict[str, Any]]:
        """عرض تاريخ الفحوصات الصحية لوكيل."""
        session = get_session_factory()()
        try:
            from sqlalchemy import desc, select

            records = (
                session.execute(
                    select(AgentHealthCheckModel)
                    .where(AgentHealthCheckModel.agent_id == agent_id)
                    .order_by(desc(AgentHealthCheckModel.created_at))
                    .limit(limit)
                )
                .scalars()
                .all()
            )
            return [
                {
                    "id": r.id,
                    "agent_id": r.agent_id,
                    "check_date": r.check_date.isoformat() if r.check_date else None,
                    "status": r.status,
                    "performance_score": r.performance_score,
                    "policy_compliance": r.policy_compliance,
                    "tool_success_rate": r.tool_success_rate,
                    "error_rate": r.error_rate,
                    "findings": r.findings or [],
                    "recommendations": r.recommendations or [],
                    "hash": r.hash,
                }
                for r in records
            ]
        finally:
            session.close()

    def get_latest_status(self, agent_id: str) -> str:
        """أحدث حالة صحية لوكيل."""
        history = self.get_agent_health_history(agent_id, limit=1)
        return history[0]["status"] if history else "unknown"


# === Treatment System ===


class TreatmentSystem:
    """نظام العلاج — ينفّذ مسار العلاج للوكلاء."""

    def __init__(self) -> None:
        self._ensure_tables()

    def _ensure_tables(self) -> None:
        url = get_database_url()
        connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
        engine = create_engine(url, connect_args=connect_args)
        _HealthBase.metadata.create_all(engine)

    def start_treatment(
        self,
        agent_id: str,
        treatment_type: str,
        reason: str,
        treatment_id: str | None = None,
        authorizer: ConstitutionalAuthorizer | None = None,
    ) -> dict[str, Any]:
        """
        8.2: بدء مسار العلاج — إعادة تدريب / استبدال نموذج / إصلاح أداة / إعادة تعيين سياق.
        يُنفَّذ فعليًا عبر استدعاء المدرسة أو Model Gateway.

        عبورٌ واحدٌ لبدءِ العلاجِ (W-699 · تصميمُ E1 § 2.2/§ 2.5): إنشاءُ السجلِ
        والانتقالُ إلى «training» يقعانِ بإذنٍ واحدٍ بالفعلِ «start_agent_treatment»
        (المحجوزِ منَ المستوى 1 — صنفُ train_model) عبرَ نواةِ الكتابةِ الصافيةِ
        فلا تعشيشَ، ومعوّضانِ يحذفانِ السجلَ ويرجعانِ الحالةَ السابقةَ. والتنفيذُ خارجَ
        العبورِ، والإتمامُ عبورٌ لاحقٌ مستقلٌّ بذاتِ الفعلِ ومفتاحٍ مميَّزٍ بالإتمامِ
        (تصميمُ E1 § 2.5)، ثمَّ العودةُ إلى «active» عبرَ العبورِ العلنيِّ المحروسِ.
        """
        if treatment_type not in ["retrain", "replace_model", "fix_tool", "reset_context"]:
            raise ValueError(f"نوع علاج غير معروف: {treatment_type}")

        actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
        # قاعدةُ نطاقٍ قبلَ الحدِّ (قراءةٌ لا كتابةٌ): لا علاجَ لوكيلٍ لا هويةَ له.
        identity = get_identity(agent_id)
        if identity is None:
            raise ValueError(f"الوكيل {agent_id} غير موجود")
        previous_state = identity.lifecycle_state
        if treatment_id is None:
            treatment_id = str(uuid.uuid4())

        # ── العبورُ الأولُ: إنشاءُ السجلِ + الانتقالُ إلى training (أثرانِ معلنانِ) ──
        # الهدفُ «agent:» يغطِّي أثرَي السجلِ والانتقالِ معًا: فالبوابةُ لا تأذنُ بفعلٍ
        # على هدفٍ إلّا بما هوَ داخلَه (EffectOutOfScopeError) — والهدفُ الحاويُ للآثارِ
        # المُعلنةِ هو الوكيلُ نفسُهُ (تصميمُ E1 § 2.2: الأثرانِ في عبورٍ واحدٍ).
        target = f"agent:{agent_id}"
        record_effect = declared_effect(
            "CREATE",
            f"{target}/treatment/{treatment_id}",
            f"سجلُّ علاجٍ ({treatment_type}) للوكيلِ «{agent_id}»",
        )
        lifecycle_effect = declared_effect(
            "WRITE",
            f"agent:{agent_id}/lifecycle.{previous_state}->"
            f"{AgentLifecycleState.TRAINING.value}",
            f"انتقالُ دورةِ الحياةِ {previous_state} → "
            f"{AgentLifecycleState.TRAINING.value} عندَ بدءِ العلاجِ",
        )

        def _apply(effect: Any) -> None:
            # الحدُّ يمرّرُ كلَّ أثرٍ على حدةٍ — كلُّ أثرٍ يُطبِّقُ كتابتَهُ لا غيرَ.
            if effect.signature == record_effect.signature:
                _create_treatment_record_core(treatment_id, agent_id, treatment_type, reason)
            elif effect.signature == lifecycle_effect.signature:
                _set_lifecycle_state_core(agent_id, AgentLifecycleState.TRAINING.value)

        guarded = actor_authorizer.guard_declared(
            ACTION_START_AGENT_TREATMENT,
            target,
            declared_effects=(record_effect, lifecycle_effect),
            applier=_apply,
            operation_key=operation_key("agents.treatment", f"{agent_id}/{treatment_id}"),
            compensators=(
                compensator(
                    record_effect.signature,
                    lambda: _delete_treatment_record_core(treatment_id),
                    "حذفُ صفِّ علاجٍ غيرِ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإنشاءِ",
                ),
                compensator(
                    lifecycle_effect.signature,
                    lambda: _set_lifecycle_state_core(agent_id, previous_state),
                    "إرجاعُ حالةِ دورةِ الحياةِ السابقةِ — عكسٌ حقيقيٌّ للانتقالِ",
                ),
            ),
        )
        if guarded.is_replay and _get_treatment_record_core(treatment_id) is None:
            # العمليّةُ مُثبَتةٌ ناجحةٌ لهذا المفتاحِ وصفُّها غائبٌ — تفرُّقٌ يُرفَعُ
            # صريحًا ولا يُزعَمُ إنشاءٌ ولا يُعادُ التنفيذُ خارجَ الحدِّ (نمطُ register_identity).
            raise IdentityLedgerDivergenceError(
                f"سجلُّ الذرّيّةِ يُثبِتُ علاجَ «{treatment_id}» وصفُّهُ غائبٌ — "
                "استعادةٌ مطلوبةٌ (1H) لا إنشاءٌ يُزعَم"
            )

        # تنفيذ العلاج فعليًا — خارجَ العبورِ (جلساتٌ لاحقةٌ مستقلةٌ بأفعالِها) —
        # معَ قراءةِ الحقلِ الدائمِ قبلَ التنفيذِ: سجلٌّ مُتِمٌّ فعلًا يعني أنَّ التنفيذَ
        # قد وقعَ في عبورٍ سابقٍ، فإعادةُ الإرسالِ لا تُعيدُ التنفيذَ (تصميمُ E1
        # § 2.4: العمليةُ الفارغةُ) بل تُعيدُ نتيجتَهُ المخزَّنةَ.
        existing_record = _get_treatment_record_core(treatment_id)
        if existing_record is not None and existing_record.status == "completed":
            result = dict(existing_record.result or {})
        else:
            result = self._execute_treatment(agent_id, treatment_type)

        # ── جلسةُ الإتمامِ: عبورٌ مستقلٌّ بذاتِ الفعلِ ومفتاحٍ مميَّزٍ بالإتمامِ (§ 2.5) ──
        completion_effect = declared_effect(
            "WRITE",
            f"agent:{agent_id}/treatment/{treatment_id}/completion",
            f"إتمامُ سجلِّ العلاجِ «{treatment_id}» بنتيجةِ التنفيذِ",
        )

        def _complete(_effect: Any) -> None:
            _complete_treatment_record_core(treatment_id, result)

        completion_guarded = actor_authorizer.guard_declared(
            ACTION_START_AGENT_TREATMENT,
            target,
            declared_effects=(completion_effect,),
            applier=_complete,
            operation_key=operation_key("agents.treatment.complete", treatment_id),
            compensators=(
                compensator(
                    completion_effect.signature,
                    lambda: _restore_treatment_in_progress_core(treatment_id),
                    "إرجاعُ السجلِّ إلى قيدِ التنفيذِ — عكسٌ حقيقيٌّ للإتمامِ",
                ),
            ),
        )

        # إعادة الوكيل للحالة النشطة — عبرَ العبورِ العلنيِّ (activate_agent · المستوى 4).
        # هويةُ العمليةِ معرِّفُ العلاجِ نفسُهُ (تصميمُ E1 § 2.4: عمليةٌ جديدةٌ على
        # الكيانِ نفسِهِ ⇒ مفتاحٌ جديدٌ): فإعادةُ إرسالِ العلاجِ نفسِهِ إعادةٌ واحدةٌ
        # على المفتاحِ نفسِهِ، وعلاجٌ لاحقٌ جديدٌ على الوكيلِ نفسِهِ عمليةٌ جديدةٌ.
        set_lifecycle_state(
            agent_id,
            AgentLifecycleState.ACTIVE.value,
            authorizer=actor_authorizer,
            operation_id=treatment_id,
        )

        # نشر حدث — عبورُ الإتمامِ إعادةُ إرسالٍ يعني أنَّ الحدثَ قد نُشِرَ في
        # الجلسةِ الأولى، فلا يُنشرُ ثانيةً (عمليةٌ فارغةٌ · E1 § 2.4)
        if not completion_guarded.is_replay:
            from amos_federation.common.event_bus import get_event_bus

            get_event_bus().publish(
                "amos_federation.health.treatment_completed",
                {
                    "agent_id": agent_id,
                    "treatment_type": treatment_type,
                    "result": result,
                },
            )

        return {
            "treatment_id": treatment_id,
            "agent_id": agent_id,
            "treatment_type": treatment_type,
            "status": "completed",
            "result": result,
        }

    def _execute_treatment(self, agent_id: str, treatment_type: str) -> dict[str, Any]:
        """تنفيذ العلاج فعليًا حسب النوع."""
        if treatment_type == "retrain":
            # 8.2: استدعاء المدرسة (المرحلة 6)
            from amos_federation.services.agent_runtime.population import AgentSchool

            school = AgentSchool()
            # محاكاة التدريب — في الإنتاج سيكون تدريبًا حقيقيًا
            result = school.run_full_curriculum(agent_id)
            return {"retrain_result": result, "method": "AgentSchool.run_full_curriculum"}

        elif treatment_type == "replace_model":
            # 8.2: استدعاء Model Gateway (المرحلة 5)
            from amos_federation.services.model_gateway.model_layer import get_model_layer

            model_layer = get_model_layer()
            # استدعاء نموذج بديل
            result = model_layer.invoke_with_cache(
                prompt="System health recovery check",
                model="claude-sonnet",
                max_tokens=100,
            )
            return {"replace_result": result, "method": "ModelLayer.invoke_with_cache"}

        elif treatment_type == "fix_tool":
            # فحص الأدوات المسموح بها وإصلاحها
            from amos_federation.services.executive_core.agent_identity import get_identity

            identity = get_identity(agent_id)
            tools = list(identity.allowed_tools) if identity else []
            return {"fixed_tools": tools, "method": "tool_audit"}

        elif treatment_type == "reset_context":
            # إعادة تعيين السياق — حذف ذاكرة الوكيل
            # مسح الذاكرة المرتبطة بالوكيل عبر query وإعادة التخزين بسياق فارغ
            from amos_federation.common.persistent import PersistentMemoryStore

            memory = PersistentMemoryStore()
            # لا يوجد clear_agent مباشر — نسجل سياقًا جديدًا فارغًا
            memory.store(
                f"agent_context_reset:{agent_id}",
                {"reset": True, "timestamp": datetime.now(UTC).isoformat()},
            )
            return {"reset": True, "method": "MemoryStore.context_reset"}

        return {"error": "unknown treatment"}


# === Isolation System ===


class IsolationSystem:
    """نظام العزل — ينقل الوكيل لـ Sandbox معزول."""

    def __init__(self) -> None:
        self._ensure_tables()

    def _ensure_tables(self) -> None:
        url = get_database_url()
        connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
        engine = create_engine(url, connect_args=connect_args)
        _HealthBase.metadata.create_all(engine)

    def isolate(
        self,
        agent_id: str,
        reason: str,
        isolation_id: str | None = None,
        authorizer: ConstitutionalAuthorizer | None = None,
    ) -> dict[str, Any]:
        """
        8.3: مسار العزل — نقل لـ Sandbox معزول، فحص كل الأفعال.
        الوكيل المعزول لا يمكنه تنفيذ أي أداة إنتاجية.

        عبورٌ واحدٌ (W-699 · تصميمُ E1 § 2.2/§ 2.3): إنشاءُ سجلِّ العزلِ والانتقالُ
        إلى «paused» أثرانِ معلنانِ في عبورٍ واحدٍ بالفعلِ «isolate_agent» — أداةُ
        الإيقافِ نفسُها لا تُمنعُ عندَ أيِّ مستوىً (قاعدةٌ 3) — والانتقالُ عبرَ نواةِ
        الكتابةِ الصافيةِ فلا تعشيشَ، ومعوّضانِ يحذفانِ السجلَ ويرجعانِ الحالةَ.
        """
        actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
        # قاعدةُ نطاقٍ قبلَ الحدِّ (قراءةٌ لا كتابةٌ): لا عزلَ لوكيلٍ لا هويةَ له.
        identity = get_identity(agent_id)
        if identity is None:
            raise ValueError(f"الوكيل {agent_id} غير موجود")
        previous_state = identity.lifecycle_state
        if isolation_id is None:
            isolation_id = str(uuid.uuid4())
        sandbox_id = f"sandbox-{agent_id[:8]}-{uuid.uuid4().hex[:4]}"

        # الهدفُ «agent:» يغطِّي أثرَي سجلِّ العزلِ والانتقالِ معًا (in_scope) —
        # الإذنُ بفعلٍ على هدفٍ ليسَ إذنًا بما سواهُ.
        target = f"agent:{agent_id}"
        record_effect = declared_effect(
            "CREATE",
            f"{target}/isolation/{isolation_id}",
            f"سجلُّ عزلٍ للوكيلِ «{agent_id}» ({reason})",
        )
        lifecycle_effect = declared_effect(
            "WRITE",
            f"agent:{agent_id}/lifecycle.{previous_state}->" f"{AgentLifecycleState.PAUSED.value}",
            f"انتقالُ دورةِ الحياةِ {previous_state} → {AgentLifecycleState.PAUSED.value}",
        )

        def _apply(effect: Any) -> None:
            # الحدُّ يمرّرُ كلَّ أثرٍ على حدةٍ — كلُّ أثرٍ يُطبِّقُ كتابتَهُ لا غيرَ.
            if effect.signature == record_effect.signature:
                _create_isolation_record_core(isolation_id, agent_id, reason, sandbox_id)
            elif effect.signature == lifecycle_effect.signature:
                _set_lifecycle_state_core(agent_id, AgentLifecycleState.PAUSED.value)

        actor_authorizer.guard_declared(
            ACTION_ISOLATE_AGENT,
            target,
            declared_effects=(record_effect, lifecycle_effect),
            applier=_apply,
            operation_key=operation_key("agents.isolation", f"{agent_id}/{isolation_id}"),
            compensators=(
                compensator(
                    record_effect.signature,
                    lambda: _delete_isolation_record_core(isolation_id),
                    "حذفُ صفِّ عزلٍ غيرِ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإنشاءِ",
                ),
                compensator(
                    lifecycle_effect.signature,
                    lambda: _set_lifecycle_state_core(agent_id, previous_state),
                    "إرجاعُ حالةِ دورةِ الحياةِ السابقةِ — عكسٌ حقيقيٌّ للانتقالِ",
                ),
            ),
        )

        # نشر حدث
        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.health.agent_isolated",
            {
                "agent_id": agent_id,
                "sandbox_id": sandbox_id,
                "reason": reason,
            },
        )

        return {
            "isolation_id": isolation_id,
            "agent_id": agent_id,
            "sandbox_id": sandbox_id,
            "status": "active",
            "reason": reason,
        }

    def log_action(
        self,
        isolation_id: str,
        action: str,
        details: dict,
        entry_id: str | None = None,
        authorizer: ConstitutionalAuthorizer | None = None,
    ) -> dict[str, Any]:
        """تسجيل فعل أثناء العزل — كل فعل يُفحص.

        الإلحاقُ لا يقعُ إلّا عبرَ الحدِّ السياديِّ بالفعلِ «log_isolated_action»
        (W-699 · تصميمُ E1 § 2.2): فعلٌ بلا منعٍ عندَ أيِّ مستوىٍ (قاعدةٌ 3)،
        ومفتاحُ الذرّيّةِ من (سجلِّ العزلِ، المُعرِّفِ) — فإعادةُ الإرسالِ بذاتِ
        المُعرِّفِ إعادةٌ واحدةٌ ولا يُلحَقُ الفعلُ مرتينِ.
        """
        actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
        record = _get_isolation_record_core(isolation_id)
        if record is None:
            raise ValueError(f"سجل عزل غير موجود: {isolation_id}")
        if entry_id is None:
            entry_id = str(uuid.uuid4())

        target = f"isolation:{record.agent_id}"
        effect = declared_effect(
            "CREATE",
            f"{target}/{isolation_id}/actions_log/{entry_id}",
            f"إلحاقُ فعلٍ ({action}) بسجلِّ عزلِ «{isolation_id}»",
        )

        def _apply(_effect: Any) -> None:
            _append_isolation_log_core(isolation_id, entry_id, action, details)

        actor_authorizer.guard_declared(
            ACTION_LOG_ISOLATED_ACTION,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key("agents.isolation.log", f"{isolation_id}/{entry_id}"),
            compensators=(
                compensator(
                    effect.signature,
                    lambda: _remove_isolation_log_entry_core(isolation_id, entry_id),
                    "حذفُ الإدخالِ المُلحَقِ منَ السجلِّ — عكسٌ حقيقيٌّ للإلحاقِ",
                ),
            ),
        )
        return {"logged": True, "action": action, "entry_id": entry_id}

    def release(
        self,
        isolation_id: str,
        decision: str,
        authorizer: ConstitutionalAuthorizer | None = None,
    ) -> dict[str, Any]:
        """
        8.3: إنهاء العزل — إعادة تدريب أو تقاعد.
        decision: retrain / retire / release

        عبورٌ واحدٌ + تحقّقٌ مسبقٌ (W-699 · تصميمُ E1 § 2.2/§ 2.3): الفعلُ
        «release_agent» بلا منعٍ عالميًّا (تعليقُ قواعدِ W-696: الاحتواءُ لا يُمنعُ
        والاستعادةُ تعبرُ بـactivate_agent المحجوزِ منَ المستوى 4) — والاتجاهُ
        يُحرسُ بطلبِ إذنٍ مسبقٍ على فعلِ الانتقالِ **قبلَ أيِّ كتابةٍ**: retire⇒
        contain_agent · release⇒activate_agent · retrain⇒start_agent_treatment —
        فالرفضُ عندَ المستوى المانعِ يقعُ بلا كتابةٍ واحدةٍ (التصميمُ § 3 الصنفُ 1).
        وسجلُّ العزلِ والانتقالُ (retire/release) أثرانِ معلنانِ في عبورٍ واحدٍ عبرَ
        نواةِ الكتابةِ فلا تعشيشَ، ومعوّضانِ يُرجعانِ السجلَ والحالةَ. وإعادةُ
        التدريبِ عمليّةٌ لاحقةٌ مستقلةٌ بعبورِها الخاصِّ (start_agent_treatment).
        """
        if decision not in ["retrain", "retire", "release"]:
            raise ValueError(f"قرار غير معروف: {decision}")
        actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
        record = _get_isolation_record_core(isolation_id)
        if record is None:
            raise ValueError(f"سجل عزل غير موجود: {isolation_id}")
        agent_id = record.agent_id
        identity = get_identity(agent_id)
        if identity is None:
            raise ValueError(f"الوكيل {agent_id} غير موجود")
        previous_state = identity.lifecycle_state
        decision_state = (
            AgentLifecycleState.RETIRED.value
            if decision == "retire"
            else AgentLifecycleState.ACTIVE.value
        )

        # ── التحقّقُ المسبقُ على فعلِ الانتقالِ — قبلَ أيِّ كتابةٍ (رفضٌ نظيفٌ) ──
        transition_action = {
            "retire": ACTION_CONTAIN_AGENT,
            "release": ACTION_ACTIVATE_AGENT,
            "retrain": ACTION_START_AGENT_TREATMENT,
        }[decision]
        transition_target = (
            f"treatment:{agent_id}" if decision == "retrain" else f"agent:{agent_id}"
        )
        transition_effects: tuple[Any, ...]
        if decision == "retrain":
            transition_effects = (
                declared_effect("CREATE", transition_target, f"سجلُّ علاجٍ للوكيلِ «{agent_id}»"),
            )
        else:
            transition_effects = (
                declared_effect(
                    "WRITE",
                    f"agent:{agent_id}/lifecycle.{previous_state}->{decision_state}",
                    f"انتقالُ دورةِ الحياةِ {previous_state} → {decision_state}",
                ),
            )
        # رفضُ الإذنِ المسبقِ يرتفعُ SovereigntyViolation قبلَ أيِّ كتابةٍ — لا
        # حالةً ناقصةً (سجلٌّ مُحدَّثٌ وانتقالٌ مرفوضٌ).
        actor_authorizer.request_permit(
            transition_action,
            transition_target,
            declared_effects=transition_effects,
        )

        # ── العبورُ: تحديثُ سجلِّ العزلِ + الانتقالُ (retire/release) — أثرانِ معلنانِ ──
        # الهدفُ «agent:» يغطِّي أثرَي السجلِ والانتقالِ معًا (in_scope).
        target = f"agent:{agent_id}"
        record_effect = declared_effect(
            "WRITE",
            f"{target}/isolation/{isolation_id}/release.{decision}",
            f"رفعُ العزلِ «{isolation_id}» بقرارِ {decision}",
        )
        effects: tuple[Any, ...] = (record_effect,)
        lifecycle_effect: Any = None
        if decision in ("retire", "release"):
            lifecycle_effect = declared_effect(
                "WRITE",
                f"agent:{agent_id}/lifecycle.{previous_state}->{decision_state}",
                f"انتقالُ دورةِ الحياةِ {previous_state} → {decision_state}",
            )
            effects = (record_effect, lifecycle_effect)

        def _apply(effect: Any) -> None:
            if effect.signature == record_effect.signature:
                _release_isolation_record_core(isolation_id, decision)
            elif lifecycle_effect is not None and effect.signature == lifecycle_effect.signature:
                _set_lifecycle_state_core(agent_id, decision_state)

        compensators: tuple[Any, ...] = (
            compensator(
                record_effect.signature,
                lambda: _restore_isolation_record_core(isolation_id, record.status),
                "إرجاعُ حالةِ سجلِّ العزلِ — عكسٌ حقيقيٌّ للرفعِ",
            ),
        )
        if lifecycle_effect is not None:
            compensators = (
                *compensators,
                compensator(
                    lifecycle_effect.signature,
                    lambda: _set_lifecycle_state_core(agent_id, previous_state),
                    "إرجاعُ حالةِ دورةِ الحياةِ السابقةِ — عكسٌ حقيقيٌّ للانتقالِ",
                ),
            )

        actor_authorizer.guard_declared(
            ACTION_RELEASE_AGENT,
            target,
            declared_effects=effects,
            applier=_apply,
            operation_key=operation_key(
                "agents.isolation.release", f"{isolation_id}/{decision}/{previous_state}"
            ),
            compensators=compensators,
        )

        # تنفيذ القرار — إعادةُ التدريبِ عمليّةٌ لاحقةٌ مستقلةٌ بعبورِها الخاصِّ
        # (start_agent_treatment · المحجوزِ منَ المستوى 1).
        if decision == "retrain":
            treatment = TreatmentSystem()
            treatment.start_treatment(
                agent_id, "retrain", "إعادة تدريب بعد عزل", authorizer=actor_authorizer
            )

        # نشر حدث
        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.health.agent_released",
            {
                "agent_id": agent_id,
                "decision": decision,
            },
        )

        return {
            "isolation_id": isolation_id,
            "agent_id": agent_id,
            "decision": decision,
            "released_at": datetime.now(UTC).isoformat(),
        }

    def is_isolated(self, agent_id: str) -> bool:
        """هل الوكيل معزول حاليًا؟"""
        session = get_session_factory()()
        try:
            from sqlalchemy import select

            record = session.execute(
                select(IsolationRecordModel)
                .where(IsolationRecordModel.agent_id == agent_id)
                .where(IsolationRecordModel.status == "active")
                .limit(1)
            ).scalar_one_or_none()
            return record is not None
        finally:
            session.close()

    def list_active_isolations(self) -> list[dict[str, Any]]:
        """عرض كل حالات العزل النشطة."""
        session = get_session_factory()()
        try:
            from sqlalchemy import select

            records = (
                session.execute(
                    select(IsolationRecordModel).where(IsolationRecordModel.status == "active")
                )
                .scalars()
                .all()
            )
            return [
                {
                    "id": r.id,
                    "agent_id": r.agent_id,
                    "reason": r.reason,
                    "sandbox_id": r.sandbox_id,
                    "isolated_at": r.isolated_at.isoformat() if r.isolated_at else None,
                    "actions_count": len(r.actions_log or []),
                }
                for r in records
            ]
        finally:
            session.close()


# === Full Health Cycle ===


def run_health_cycle(limit: int = 20) -> dict[str, Any]:
    """تشغيل دورة فحص صحي كاملة على الوكلاء (مع حد لتجنب عنق الزجاجة)."""
    checker = HealthChecker()
    results = checker.check_all_agents(limit=limit)

    treatment = TreatmentSystem()
    isolation = IsolationSystem()

    treatments_started = 0
    isolations_started = 0

    for result in results:
        if result["status"] == TREATMENT:
            treatment.start_treatment(
                result["agent_id"],
                "retrain" if result["error_rate"] > 0.3 else "reset_context",
                f"علاج تلقائي: {result['findings'][0] if result['findings'] else 'أداء منخفض'}",
            )
            treatments_started += 1
        elif result["status"] == ISOLATED:
            isolation.isolate(
                result["agent_id"],
                f"عزل تلقائي: {result['findings'][0] if result['findings'] else 'أداء حرج'}",
            )
            isolations_started += 1

    return {
        "total_agents_checked": len(results),
        "healthy": sum(1 for r in results if r["status"] == HEALTHY),
        "monitor": sum(1 for r in results if r["status"] == MONITOR),
        "treatment": sum(1 for r in results if r["status"] == TREATMENT),
        "isolated": sum(1 for r in results if r["status"] == ISOLATED),
        "treatments_started": treatments_started,
        "isolations_started": isolations_started,
        "cycle_date": datetime.now(UTC).isoformat(),
    }


# === R4: صحّة طبقة الهوية والسكّان ===


def population_health() -> dict[str, Any]:
    """صحّة السكّان مبنيّة على مكوّنات حقيقية — لا على «الخدمة تعمل».

    R4-F: التقرير لا يقول `healthy` لمجرّد أن العملية قائمة. يُفحَص فعليًّا:
    السجل الكانوني، ناقل الأحداث، تناسق الإسقاط السكّاني، ونظام العزل. أي
    مكوّن غير متوفّر يُعلَن `unavailable` والحالة الكلية تنزل معه.
    """
    from amos_federation.services.executive_core.agent_identity import identity_health

    report = identity_health()
    components = report["components"]
    try:
        isolations = get_isolation_system().list_active_isolations()
        components["isolation_system"] = {
            "status": "available",
            "active_isolations": len(isolations),
        }
    except Exception as exc:  # noqa: BLE001 — تُعلَن كغير متوفّرة لا تُخفى
        components["isolation_system"] = {"status": "unavailable", "error": str(exc)}

    statuses = {component["status"] for component in components.values()}
    if "unavailable" in statuses:
        report["status"] = "unavailable"
    elif "degraded" in statuses:
        report["status"] = "degraded"
    return report


# === Singleton Accessors ===

_health_checker: HealthChecker | None = None
_treatment_system: TreatmentSystem | None = None
_isolation_system: IsolationSystem | None = None


def get_health_checker() -> HealthChecker:
    global _health_checker
    if _health_checker is None:
        _health_checker = HealthChecker()
    return _health_checker


def get_treatment_system() -> TreatmentSystem:
    global _treatment_system
    if _treatment_system is None:
        _treatment_system = TreatmentSystem()
    return _treatment_system


def get_isolation_system() -> IsolationSystem:
    global _isolation_system
    if _isolation_system is None:
        _isolation_system = IsolationSystem()
    return _isolation_system


# ── E1 · نوى كتابةٍ صافيةٌ بلا عبورٍ (W-699 · تصميمُ E1 § 2.3) ──────────────────
#
# تستعملُها الأسطحُ المحروسةُ أعلاهُ في عبورِها الأعلى فلا تعشيشَ (عبورٌ داخلَ
# مُطبِّقِ عبورٍ يرتفعُ NestedSovereignCallError). ولا تُستعملُ مباشرةً من خارجِ
# الوحدةِ: المرجعُ العلنيُّ هو الأسطحُ المحروسةُ نفسُها.


def _write_health_check_core(
    check_id: str,
    *,
    agent_id: str,
    status: str,
    performance_score: float,
    resource_usage: dict,
    policy_compliance: float,
    tool_success_rate: float,
    error_rate: float,
    findings: list,
    recommendations: list,
) -> None:
    """نواةُ كتابةِ سجلِّ الفحصِ — إلحاقُ صفٍّ واحدٍ بسلسلةِ التجزئةِ."""
    session = get_session_factory()()
    try:
        from sqlalchemy import desc, select

        last_check = session.execute(
            select(AgentHealthCheckModel).order_by(desc(AgentHealthCheckModel.created_at)).limit(1)
        ).scalar_one_or_none()
        prev_hash = last_check.hash if last_check else "0" * 64
        details = {
            "agent_id": agent_id,
            "performance_score": performance_score,
            "error_rate": error_rate,
            "policy_compliance": policy_compliance,
            "tool_success_rate": tool_success_rate,
        }
        payload = json.dumps(
            {
                "action": "health_check",
                "actor": agent_id,
                "details": details,
                "prev_hash": prev_hash,
            },
            sort_keys=True,
            default=str,
        )
        check_hash = hashlib.sha256(payload.encode()).hexdigest()
        session.add(
            AgentHealthCheckModel(
                id=check_id,
                agent_id=agent_id,
                status=status,
                performance_score=performance_score,
                resource_usage=resource_usage,
                policy_compliance=policy_compliance,
                tool_success_rate=tool_success_rate,
                error_rate=error_rate,
                findings=findings,
                recommendations=recommendations,
                prev_hash=prev_hash,
                hash=check_hash,
            )
        )
        session.commit()
    finally:
        session.close()


def _health_check_hash(check_id: str) -> str:
    """قراءةُ تجزئةِ سجلِّ فحصٍ منَ الحقلِ الدائمِ — لا افتراضَ بعدَ العبورِ."""
    session = get_session_factory()()
    try:
        row = session.get(AgentHealthCheckModel, check_id)
        return row.hash if row is not None else ""
    finally:
        session.close()


def _delete_health_check_core(check_id: str) -> bool:
    """حذفُ صفِّ فحصٍ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإلحاقِ (معوّضُ 1I)."""
    session = get_session_factory()()
    try:
        row = session.get(AgentHealthCheckModel, check_id)
        if row is None:
            return False
        session.delete(row)
        session.commit()
        return True
    finally:
        session.close()


def _create_treatment_record_core(
    treatment_id: str, agent_id: str, treatment_type: str, reason: str
) -> None:
    """نواةُ كتابةِ إنشاءِ سجلِّ العلاجِ — قيدُ تنفيذٍ."""
    session = get_session_factory()()
    try:
        session.add(
            TreatmentRecordModel(
                id=treatment_id,
                agent_id=agent_id,
                treatment_type=treatment_type,
                status="in_progress",
                details={"reason": reason, "started_by": "health_system"},
            )
        )
        session.commit()
    finally:
        session.close()


def _get_treatment_record_core(treatment_id: str) -> TreatmentRecordModel | None:
    """قراءةُ سجلِّ علاجٍ — لا يُخترَعُ سجلٌّ."""
    session = get_session_factory()()
    try:
        return session.get(TreatmentRecordModel, treatment_id)
    finally:
        session.close()


def _delete_treatment_record_core(treatment_id: str) -> bool:
    """حذفُ صفِّ علاجٍ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإنشاءِ (معوّضُ 1I)."""
    session = get_session_factory()()
    try:
        row = session.get(TreatmentRecordModel, treatment_id)
        if row is None:
            return False
        session.delete(row)
        session.commit()
        return True
    finally:
        session.close()


def _complete_treatment_record_core(treatment_id: str, result: dict) -> None:
    """نواةُ كتابةِ إتمامِ سجلِّ العلاجِ — تُعيدُ قراءةَ الحقلِ الدائمِ وتأبى
    إتمامَ ما ليسَ قيدَ التنفيذِ (لا إعادةَ تنفيذٍ عمياءَ عندَ الإعادةِ)."""
    session = get_session_factory()()
    try:
        row = session.get(TreatmentRecordModel, treatment_id)
        if row is None:
            raise ValueError(f"سجل علاج غير موجود: {treatment_id}")
        if row.status != "in_progress":
            raise ValueError(
                f"سجل العلاج «{treatment_id}» ليس قيد التنفيذ ({row.status}) — لا إتمام يُزعم"
            )
        row.status = "completed"
        row.completed_at = datetime.now(UTC)
        row.result = result
        session.commit()
    finally:
        session.close()


def _restore_treatment_in_progress_core(treatment_id: str) -> None:
    """إرجاعُ السجلِّ إلى قيدِ التنفيذِ — عكسٌ حقيقيٌّ للإتمامِ."""
    session = get_session_factory()()
    try:
        row = session.get(TreatmentRecordModel, treatment_id)
        if row is None:
            return
        row.status = "in_progress"
        row.completed_at = None
        session.commit()
    finally:
        session.close()


def _create_isolation_record_core(
    isolation_id: str, agent_id: str, reason: str, sandbox_id: str
) -> None:
    """نواةُ كتابةِ إنشاءِ سجلِّ العزلِ."""
    session = get_session_factory()()
    try:
        session.add(
            IsolationRecordModel(
                id=isolation_id,
                agent_id=agent_id,
                reason=reason,
                sandbox_id=sandbox_id,
                status="active",
                actions_log=[],
            )
        )
        session.commit()
    finally:
        session.close()


def _get_isolation_record_core(isolation_id: str) -> IsolationRecordModel | None:
    """قراءةُ سجلِّ عزلٍ — لا يُخترَعُ سجلٌّ."""
    session = get_session_factory()()
    try:
        return session.get(IsolationRecordModel, isolation_id)
    finally:
        session.close()


def _delete_isolation_record_core(isolation_id: str) -> bool:
    """حذفُ صفِّ عزلٍ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإنشاءِ (معوّضُ 1I)."""
    session = get_session_factory()()
    try:
        row = session.get(IsolationRecordModel, isolation_id)
        if row is None:
            return False
        session.delete(row)
        session.commit()
        return True
    finally:
        session.close()


def _release_isolation_record_core(isolation_id: str, decision: str) -> None:
    """نواةُ كتابةِ رفعِ العزلِ — تحديثُ السجلِّ بوضعِ القرارِ."""
    session = get_session_factory()()
    try:
        row = session.get(IsolationRecordModel, isolation_id)
        if row is None:
            raise ValueError(f"سجل عزل غير موجود: {isolation_id}")
        row.status = decision
        row.released_at = datetime.now(UTC)
        session.commit()
    finally:
        session.close()


def _restore_isolation_record_core(isolation_id: str, previous_status: str) -> None:
    """إرجاعُ حالةِ سجلِّ العزلِ السابقةِ — عكسٌ حقيقيٌّ للرفعِ."""
    session = get_session_factory()()
    try:
        row = session.get(IsolationRecordModel, isolation_id)
        if row is None:
            return
        row.status = previous_status
        row.released_at = None
        session.commit()
    finally:
        session.close()


def _append_isolation_log_core(
    isolation_id: str, entry_id: str, action: str, details: dict
) -> None:
    """نواةُ كتابةِ إلحاقِ فعلٍ بسجلِّ العزلِ — ترفضُ تكرارَ المُعرِّفِ."""
    session = get_session_factory()()
    try:
        row = session.get(IsolationRecordModel, isolation_id)
        if row is None:
            raise ValueError(f"سجل عزل غير موجود: {isolation_id}")
        actions = list(row.actions_log or [])
        if any(str(entry.get("entry_id")) == entry_id for entry in actions):
            raise ValueError(
                f"الإدخال «{entry_id}» مُلحَقٌ فعلًا بسجلِّ «{isolation_id}» — لا يُلحَقُ مرتينِ"
            )
        actions.append(
            {
                "entry_id": entry_id,
                "action": action,
                "details": details,
                "timestamp": datetime.now(UTC).isoformat(),
            }
        )
        row.actions_log = actions
        session.commit()
    finally:
        session.close()


def _remove_isolation_log_entry_core(isolation_id: str, entry_id: str) -> bool:
    """حذفُ الإدخالِ المُلحَقِ منَ السجلِّ — عكسٌ حقيقيٌّ للإلحاقِ."""
    session = get_session_factory()()
    try:
        row = session.get(IsolationRecordModel, isolation_id)
        if row is None:
            return False
        actions = [
            entry for entry in (row.actions_log or []) if str(entry.get("entry_id")) != entry_id
        ]
        row.actions_log = actions
        session.commit()
        return True
    finally:
        session.close()
