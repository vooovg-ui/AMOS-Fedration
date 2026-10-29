"""
AMOS-Federation Population Expansion + Universities + Retirement (Phase 11)
الهدف: التوسع السكاني الكامل (~500+ وكيل) + مسار التخصص + الجامعات + التقاعد
النطاق: services/governance/expansion
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
آخر تعديل: 2026-10-29 (W-724 — عبورُ ستّةِ أسطحٍ الحدَّ السياديَّ · G1 § 9.9)
"""

import hashlib
import json
import uuid
from datetime import UTC, datetime
from typing import Any

import structlog
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
    create_engine,
    desc,
    select,
)
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from amos_federation.common.database import get_database_url
from amos_federation.services.agent_runtime.population import (
    get_population_registry,
    get_school,
)
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    get_authorizer,
    operation_key,
)

# ── أفعالُ العبورِ (G1 § 2.2 · تصميمُ § 9.9.4 · W-724) ─────────────────────────
#: `take_exam` — صفُّ نتيجةِ اختبارِ تخصّص (ممنوعٌ عندَ ≥1).
ACTION_TAKE_EXAM = "record_curriculum_step"
#: `submit_output` — صفُّ مخرجٍ جامعيّ (ممنوعٌ عندَ ≥4).
ACTION_SUBMIT_OUTPUT = "create_task"
#: `approve_output` — اعتمادُ مخرج (ممنوعٌ عندَ ≥4).
ACTION_APPROVE_OUTPUT = "activate_agent"
#: `employ_batch` — عددُ الموظَّفين في الدفعة (ممنوعٌ عندَ ≥3).
ACTION_EMPLOY_BATCH = "dispatch_agent"
#: `graduate_batch` — عددُ الخرّيجين. `release_agent` ليسَ في KILL_SWITCH_BLOCKS عندَ أيِّ
#: مستوى وجدولُ § 2.2 يقولُ «4»: يُنفَّذُ عمودُ الفعلِ ويُرفَعُ للمالكِ Q-78 (§ 9.9.3).
ACTION_GRADUATE_BATCH = "release_agent"
#: `retire_agent` — سجلُّ تقاعد · احتواءٌ لا يُمنَع (Q-26).
ACTION_RETIRE_AGENT = "contain_agent"
#: `create_batch` و`enroll_batch` لا يُعبَرانِ: `spawn_population` محكومٌ بشريًّا (R-001-1)
#: ولا قناةَ موافقةٍ في الجسر — دَينٌ معلَّقٌ بقرارِ المالكِ Q-77 (§ 9.9.2).

EXAM_SCOPE = "expansion.exam"
OUTPUT_SUBMIT_SCOPE = "expansion.output.submit"
OUTPUT_APPROVE_SCOPE = "expansion.output.approve"
BATCH_EMPLOY_SCOPE = "expansion.batch.employ"
BATCH_GRADUATE_SCOPE = "expansion.batch.graduate"
RETIRE_SCOPE = "expansion.retire"


class _GovernedSurface:
    """مُصرِّحٌ محقونٌ أو افتراضيٌّ عبرَ `get_authorizer()` — لا موضعَ بناءٍ جديد (سابقةُ W-723)."""

    _authorizer: ConstitutionalAuthorizer | None = None

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        if self._authorizer is None:
            self._authorizer = get_authorizer()
        return self._authorizer


def _already_succeeded(authorizer: ConstitutionalAuthorizer, key: Any) -> bool:
    """هل نجحَ عبورُ هذا المفتاحِ من قبل؟ — قراءةٌ قبلَ الحدِّ تمنعُ إعادةَ العبوراتِ الداخليّة."""
    from core.sovereignty.idempotency import OperationStatus

    prior = authorizer.boundary.idempotency_ledger.get(key)
    return prior is not None and prior.status == OperationStatus.SUCCEEDED


def _delete_rows(session_factory: Any, model: Any, ids: list[int]) -> None:
    """حذفُ الصفوفِ التي أنشأها المُطبِّقُ بمعرِّفاتِها الملتقَطة — عكسٌ حقيقيٌّ لـCREATE."""
    if not ids:
        return
    session = session_factory()
    try:
        session.query(model).filter(model.id.in_(ids)).delete(synchronize_session=False)
        session.commit()
    finally:
        session.close()


def _set_batch_column(session_factory: Any, batch_id: str, column: str, value: int) -> None:
    """كاتبُ عمودِ عددٍ في صفِّ الدفعة — يستعملُه المُطبِّقُ والمعوِّض."""
    session = session_factory()
    try:
        batch = session.execute(
            select(ExpansionBatchModel).where(ExpansionBatchModel.batch_id == batch_id).limit(1)
        ).scalar_one_or_none()
        if batch is not None:
            setattr(batch, column, value)
            session.commit()
    finally:
        session.close()


class _ExpansionBase(DeclarativeBase):
    """قاعدة نماذج التوسع."""

    pass


# === Models ===


class SpecializationResultModel(_ExpansionBase):
    """نتائج اختبار التخصص لكل وكيل."""

    __tablename__ = "specialization_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id = Column(String, nullable=False, index=True)
    track = Column(String, nullable=False)  # finance, law, science, health, culture, industry
    exam_score = Column(Float, default=0.0)
    passed = Column(Boolean, default=False)
    notes = Column(Text, default="")
    taken_at = Column(DateTime, default=lambda: datetime.now(UTC))


class UniversityOutputModel(_ExpansionBase):
    """مخرجات الجامعة — أوراق بحثية، أدوات، منهج محسّن."""

    __tablename__ = "university_outputs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    output_id = Column(String, nullable=False, unique=True, index=True)
    output_type = Column(String, nullable=False)  # paper, tool, method
    title = Column(String, nullable=False)
    author_agent_id = Column(String, nullable=False)
    track = Column(String, nullable=False)  # finance, law, science, health, culture, industry
    abstract = Column(Text, default="")
    content_hash = Column(String, default="")  # SHA-256 of content
    quality_score = Column(Float, default=0.0)
    approved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class RetirementRecordModel(_ExpansionBase):
    """سجلات التقاعد."""

    __tablename__ = "retirement_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    agent_id = Column(String, nullable=False, index=True)
    reason = Column(String, nullable=False)  # health_failure, age, disciplinary
    health_failures = Column(Integer, default=0)
    archived_data = Column(Text, default="{}")  # JSON snapshot
    retired_at = Column(DateTime, default=lambda: datetime.now(UTC))


class ExpansionBatchModel(_ExpansionBase):
    """دفعات التوسع السكاني."""

    __tablename__ = "expansion_batches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    batch_id = Column(String, nullable=False, unique=True, index=True)
    category = Column(String, nullable=False)
    target_count = Column(Integer, nullable=False)
    enrolled = Column(Integer, default=0)
    graduated = Column(Integer, default=0)
    employed = Column(Integer, default=0)
    min_score = Column(Float, default=85.0)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


# === Full population categories (roadmap §3) ===

FULL_POPULATION_CATEGORIES = {
    "coordinator": {
        "count": 1,
        "role": "منسق عام",
        "category": "governance",
        "tools": ["chart_generate", "text_summary", "document_analysis"],
        "permissions": ["task:assign", "agent:manage", "report:view"],
    },
    "state_coordinator": {
        "count": 10,
        "role": "منسق ولاية",
        "category": "governance",
        "tools": ["chart_generate", "text_summary", "document_analysis"],
        "permissions": ["task:assign", "agent:manage", "report:view"],
    },
    "cognitive_executor": {
        "count": 150,
        "role": "منفذ معرفي",
        "category": "cognitive",
        "tools": ["python_execute", "sql_query", "document_analysis", "chart_generate"],
        "permissions": ["task:execute", "tool:use"],
    },
    "operational_executor": {
        "count": 120,
        "role": "منفذ تشغيلي",
        "category": "operational",
        "tools": ["text_summary", "document_analysis"],
        "permissions": ["task:execute", "tool:use"],
    },
    "security_monitor": {
        "count": 25,
        "role": "مراقب أمني",
        "category": "security",
        "tools": ["document_analysis", "text_summary"],
        "permissions": ["audit:view", "alert:raise"],
    },
    "auditor": {
        "count": 20,
        "role": "مدقق",
        "category": "audit",
        "tools": ["sql_query", "document_analysis"],
        "permissions": ["audit:view", "audit:write"],
    },
    "judge": {
        "count": 10,
        "role": "قاضٍ",
        "category": "judicial",
        "tools": ["document_analysis", "text_summary"],
        "permissions": ["court:rule", "dispute:resolve"],
    },
    "inspector": {
        "count": 20,
        "role": "مفتش",
        "category": "oversight",
        "tools": ["document_analysis", "text_summary"],
        "permissions": ["inspect:all", "report:view"],
    },
    "trainer": {
        "count": 30,
        "role": "مدرب",
        "category": "education",
        "tools": ["text_summary", "document_analysis", "chart_generate"],
        "permissions": ["agent:train", "school:manage"],
    },
    "learner": {
        "count": 80,
        "role": "متعلم",
        "category": "education",
        "tools": ["text_summary"],
        "permissions": ["school:attend"],
    },
    "production_manager": {
        "count": 10,
        "role": "مدير خط إنتاج",
        "category": "production",
        "tools": ["chart_generate", "document_analysis", "sql_query"],
        "permissions": ["production:manage", "task:assign"],
    },
    "production_worker": {
        "count": 80,
        "role": "عامل إنتاج",
        "category": "production",
        "tools": ["text_summary"],
        "permissions": ["production:work"],
    },
    "accountant": {
        "count": 15,
        "role": "محاسب",
        "category": "treasury",
        "tools": ["sql_query", "chart_generate", "document_analysis"],
        "permissions": ["treasury:manage", "budget:view"],
    },
    "librarian": {
        "count": 15,
        "role": "أمين مكتبة",
        "category": "knowledge",
        "tools": ["document_analysis", "text_summary"],
        "permissions": ["library:manage", "knowledge:index"],
    },
    "infrastructure_engineer": {
        "count": 20,
        "role": "مهندس بنية",
        "category": "infrastructure",
        "tools": ["python_execute", "sql_query"],
        "permissions": ["infra:manage", "system:maintain"],
    },
    "relations_coordinator": {
        "count": 10,
        "role": "منسق علاقات",
        "category": "relations",
        "tools": ["text_summary", "document_analysis"],
        "permissions": ["relations:manage", "report:view"],
    },
    "emergency": {
        "count": 15,
        "role": "طوارئ",
        "category": "emergency",
        "tools": ["text_summary", "document_analysis"],
        "permissions": ["emergency:respond", "alert:raise"],
    },
    "reserve": {
        "count": 50,
        "role": "احتياطي",
        "category": "reserve",
        "tools": ["text_summary"],
        "permissions": ["standby"],
    },
}

TOTAL_TARGET_POPULATION = sum(c["count"] for c in FULL_POPULATION_CATEGORIES.values())


# === Specialization tracks (roadmap §6.2) ===

SPECIALIZATION_TRACKS = {
    "finance": {
        "name": "تخصص مالي",
        "duration_days": 7,  # أسبوع
        "exam_threshold": 80.0,
        "curriculum": [
            "المحاسبة الفدرالية",
            "إدارة الموازنات",
            "التحليل المالي",
            "التدقيق المالي",
        ],
    },
    "law": {
        "name": "تخصص قانوني",
        "duration_days": 14,  # أسبوعان
        "exam_threshold": 85.0,
        "curriculum": [
            "الدستور الفدرالي",
            "السياسات التشريعية",
            "التحكيم القضائي",
            "الامتثال التنظيمي",
        ],
    },
    "science": {
        "name": "تخصص علمي",
        "duration_days": 21,  # ثلاثة أسابيع
        "exam_threshold": 85.0,
        "curriculum": [
            "المنهج العلمي",
            "تحليل البيانات",
            "البحث التجريبي",
            "كتابة الأوراق البحثية",
        ],
    },
    "health": {
        "name": "تخصص صحي",
        "duration_days": 14,
        "exam_threshold": 85.0,
        "curriculum": [
            "الصحة العامة",
            "فحص الأنظمة",
            "التشخيص الوقائي",
            "إدارة الأزمات الصحية",
        ],
    },
    "culture": {
        "name": "تخصص ثقافي",
        "duration_days": 7,
        "exam_threshold": 80.0,
        "curriculum": [
            "إدارة المعرفة",
            "الأرشفة الثقافية",
            "التوثيق",
            "إدارة المكتبات",
        ],
    },
    "industry": {
        "name": "تخصص صناعي",
        "duration_days": 14,
        "exam_threshold": 80.0,
        "curriculum": [
            "إدارة الإنتاج",
            "تحسين العمليات",
            "مراقبة الجودة",
            "الصيانة الصناعية",
        ],
    },
}


# === University research topics ===

UNIVERSITY_RESEARCH_TOPICS = {
    "finance": [
        "تحسين نموذج توزيع الموازنات الفدرالية",
        "خوارزمية جديدة للتنبؤ بالتكاليف",
        "تحسين كشف الاحتيال المالي",
    ],
    "law": [
        "إطار تشريعي للذكاء الاصطناعي",
        "تحسين دورة التشريع",
        "نموذج تحكيم آلي",
    ],
    "science": [
        "أداة تحليل بيانات جديدة",
        "تحسين منهج التقييم",
        "خوارزمية تحسين الجودة",
    ],
    "health": [
        "تحسين بروتوكول الفحص الصحي",
        "أداة تشخيص استباقي",
        "تحسين نظام العزل",
    ],
    "culture": [
        "تحسين نظام الأرشفة",
        "أداة فهرسة المعرفة",
        "تحسين نظام الاسترجاع",
    ],
    "industry": [
        "تحسين خط الإنتاج",
        "أداة مراقبة الجودة",
        "تحسين كفاءة العمليات",
    ],
}


# === Population Expansion ===


class PopulationExpansion(_GovernedSurface):
    """التوسع السكاني التدريجي عبر المدرسة بدفعات."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._authorizer = authorizer
        self._ensure_tables()

    def _ensure_tables(self) -> None:
        url = get_database_url()
        connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
        engine = create_engine(url, connect_args=connect_args)
        _ExpansionBase.metadata.create_all(engine)
        self._engine = engine
        self._Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

    def create_batch(
        self, category: str, target_count: int, min_score: float = 85.0
    ) -> dict[str, Any]:
        """إنشاء دفعة توسع لفئة معينة."""
        batch_id = f"batch-{uuid.uuid4().hex[:8]}"
        session = self._Session()
        try:
            batch = ExpansionBatchModel(
                batch_id=batch_id,
                category=category,
                target_count=target_count,
                min_score=min_score,
            )
            session.add(batch)
            session.commit()
        finally:
            session.close()

        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.expansion.batch_created",
            {
                "batch_id": batch_id,
                "category": category,
                "target": target_count,
            },
        )
        return {"batch_id": batch_id, "category": category, "target_count": target_count}

    def enroll_batch(self, batch_id: str, count: int) -> list[dict[str, Any]]:
        """تسجيل وكلاء جدد في دفعة."""
        session = self._Session()
        try:
            batch = session.execute(
                select(ExpansionBatchModel).where(ExpansionBatchModel.batch_id == batch_id).limit(1)
            ).scalar_one_or_none()
            if not batch:
                return []

            cat_key = batch.category
            cat_spec = FULL_POPULATION_CATEGORIES.get(
                cat_key, FULL_POPULATION_CATEGORIES["reserve"]
            )
            registry = get_population_registry()

            enrolled = []
            for i in range(count):
                name = f"{cat_spec['role']} {batch.enrolled + i + 1}"
                agent = registry.register_agent(
                    name=name,
                    role=cat_key,
                    category=cat_spec["category"],
                    permissions=cat_spec["permissions"],
                    allowed_tools=cat_spec["tools"],
                )
                enrolled.append(agent)

            batch.enrolled += count
            session.commit()
            return enrolled
        finally:
            session.close()

    def _batch_snapshot(self, batch_id: str) -> dict[str, Any] | None:
        """قراءةُ صفِّ الدفعةِ قبلَ الحدّ — لقطةٌ يُبنى منها المفتاحُ والمعوِّض."""
        session = self._Session()
        try:
            batch = session.execute(
                select(ExpansionBatchModel).where(ExpansionBatchModel.batch_id == batch_id).limit(1)
            ).scalar_one_or_none()
            if batch is None:
                return None
            return {
                "category": batch.category,
                "min_score": batch.min_score,
                "graduated": int(batch.graduated or 0),
                "employed": int(batch.employed or 0),
            }
        finally:
            session.close()

    def graduate_batch(
        self,
        batch_id: str,
        scores: list[list[int]] | None = None,
        *,
        operation_id: str | None = None,
    ) -> dict[str, Any]:
        """تخرير دفعة عبر المدرسة — يتطلب ≥85% متوسط · عبرَ الحدِّ (G1 § 9.9.4 · W-724).

        تحقّقٌ مسبقٌ قبلَ أيِّ كتابة، ثمَّ خطواتُ المنهجِ (كلٌّ بعبورِه)، ثمَّ عبورُ صفِّ الدفعة.
        والعمليّةُ المركّبةُ ليست ذرّيّةً كلُّها (§ 9.9.6 (1)).
        """
        snap = self._batch_snapshot(batch_id)
        if snap is None:
            return {"error": "batch_not_found"}
        previous = snap["graduated"]
        op = operation_id or f"graduate-{uuid.uuid4().hex[:12]}"
        target = f"batch:{batch_id}"
        key = operation_key(BATCH_GRADUATE_SCOPE, f"{batch_id}.{op}")
        if _already_succeeded(self.authorizer, key):
            return {"batch_id": batch_id, "replayed": True, "operation_id": op}
        permit_effect = declared_effect(
            "WRITE",
            f"{target}/graduated.{previous}@{op}",
            f"تحديثُ عددِ خرّيجي الدفعةِ «{batch_id}» (السابقُ: {previous})",
        )
        # التحقّقُ المسبقُ على فعلِ السطحِ نفسِه — رفضٌ نظيفٌ قبلَ أيِّ كتابة (§ 9.9.4 (1)).
        self.authorizer.request_permit(
            ACTION_GRADUATE_BATCH, target, declared_effects=(permit_effect,)
        )

        # جلب الوكلاء المسجلين في هذه الفئة
        registry = get_population_registry()
        agents = registry.list_agents(
            category=FULL_POPULATION_CATEGORIES.get(snap["category"], {}).get("category", "reserve")
        )
        school = get_school()
        graduated = 0
        failed = 0
        for i, agent in enumerate(agents):
            agent_scores = scores[i] if scores and i < len(scores) else [85, 85, 85, 90, 85, 90]
            result = school.run_full_curriculum(agent["agent_id"], agent_scores)
            if result["graduation"]["graduated"]:
                avg = result["graduation"]["avg_score"]
                if avg >= snap["min_score"]:
                    graduated += 1
                else:
                    failed += 1
            else:
                failed += 1

        effect = declared_effect(
            "WRITE",
            f"{target}/graduated.{previous}->{graduated}@{op}",
            f"عددُ خرّيجي الدفعةِ «{batch_id}»: {previous} ← {graduated}",
        )

        def _apply(_effect: Any) -> None:
            _set_batch_column(self._Session, batch_id, "graduated", graduated)

        def _undo() -> None:
            _set_batch_column(self._Session, batch_id, "graduated", previous)

        guarded = self.authorizer.guard_declared(
            ACTION_GRADUATE_BATCH,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=key,
            compensators=(compensator(effect.signature, _undo, "إرجاعُ عددِ الخرّيجين السابق"),),
            metadata={"batch_id": batch_id, "previous_graduated": previous},
        )
        if guarded.is_replay:
            return {"batch_id": batch_id, "replayed": True, "operation_id": op}
        return {"batch_id": batch_id, "graduated": graduated, "failed": failed, "operation_id": op}

    def employ_batch(self, batch_id: str, *, operation_id: str | None = None) -> dict[str, Any]:
        """توظيف خريجي الدفعة — يتطلب فحص صحي أولاً (المرحلة 8) · عبرَ الحدِّ (W-724).

        تحقّقٌ مسبقٌ (`dispatch_agent` · ممنوعٌ عندَ ≥3) قبلَ أيِّ كتابة، ثمَّ الفحصُ الصحّيُّ
        وتحديثُ الحالةِ (كلٌّ بعبورِه)، ثمَّ عبورُ صفِّ الدفعة (§ 9.9.4).
        """
        from amos_federation.services.agent_runtime.health import get_health_checker

        snap = self._batch_snapshot(batch_id)
        if snap is None:
            return {"error": "batch_not_found"}
        previous = snap["employed"]
        op = operation_id or f"employ-{uuid.uuid4().hex[:12]}"
        target = f"batch:{batch_id}"
        key = operation_key(BATCH_EMPLOY_SCOPE, f"{batch_id}.{op}")
        if _already_succeeded(self.authorizer, key):
            return {"batch_id": batch_id, "replayed": True, "operation_id": op}
        permit_effect = declared_effect(
            "WRITE",
            f"{target}/employed.{previous}@{op}",
            f"تحديثُ عددِ موظَّفي الدفعةِ «{batch_id}» (السابقُ: {previous})",
        )
        self.authorizer.request_permit(
            ACTION_EMPLOY_BATCH, target, declared_effects=(permit_effect,)
        )

        registry = get_population_registry()
        health_checker = get_health_checker()
        cat_spec = FULL_POPULATION_CATEGORIES.get(snap["category"], {})
        agents = registry.list_agents(category=cat_spec.get("category", "reserve"))

        employed = 0
        health_failed = 0
        for agent in agents:
            if agent["state"] != "employed":
                continue
            # فحص صحي أولي (المرحلة 8) — عبورٌ داخليٌّ متعاقبٌ لا متداخل
            health_result = health_checker.check_agent(
                agent["agent_id"], authorizer=self.authorizer
            )
            if health_result.get("status") in ("healthy", "degraded"):
                registry.update_state(agent["agent_id"], "active", authorizer=self.authorizer)
                employed += 1
            else:
                health_failed += 1

        effect = declared_effect(
            "WRITE",
            f"{target}/employed.{previous}->{employed}@{op}",
            f"عددُ موظَّفي الدفعةِ «{batch_id}»: {previous} ← {employed}",
        )

        def _apply(_effect: Any) -> None:
            _set_batch_column(self._Session, batch_id, "employed", employed)

        def _undo() -> None:
            _set_batch_column(self._Session, batch_id, "employed", previous)

        guarded = self.authorizer.guard_declared(
            ACTION_EMPLOY_BATCH,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=key,
            compensators=(compensator(effect.signature, _undo, "إرجاعُ عددِ الموظَّفين السابق"),),
            metadata={"batch_id": batch_id, "previous_employed": previous},
        )
        if guarded.is_replay:
            return {"batch_id": batch_id, "replayed": True, "operation_id": op}

        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.expansion.batch_employed",
            {
                "batch_id": batch_id,
                "employed": employed,
            },
        )
        return {
            "batch_id": batch_id,
            "employed": employed,
            "health_failed": health_failed,
            "operation_id": op,
        }

    def run_full_expansion(self, batch_size: int = 50) -> dict[str, Any]:
        """التوسع الكامل — دفعات تدريجية لكل الفئات."""
        registry = get_population_registry()
        current_count = len(registry.list_agents())
        remaining = TOTAL_TARGET_POPULATION - current_count
        if remaining <= 0:
            return {
                "status": "already_full",
                "current": current_count,
                "target": TOTAL_TARGET_POPULATION,
            }

        results = []
        for cat_key, cat_spec in FULL_POPULATION_CATEGORIES.items():
            # عدد الوكلاء الحاليين في هذه الفئة
            existing = len(registry.list_agents(category=cat_spec["category"]))
            needed = cat_spec["count"] - existing
            if needed <= 0:
                continue

            # دفعات
            batches_for_cat = (needed + batch_size - 1) // batch_size
            for _ in range(batches_for_cat):
                batch = self.create_batch(cat_key, min(batch_size, needed))
                self.enroll_batch(batch["batch_id"], min(batch_size, needed))
                self.graduate_batch(batch["batch_id"])
                self.employ_batch(batch["batch_id"])
                results.append(batch)
                needed -= batch_size

        final_count = len(registry.list_agents())
        return {
            "initial_count": current_count,
            "final_count": final_count,
            "target": TOTAL_TARGET_POPULATION,
            "batches_created": len(results),
            "categories": len(FULL_POPULATION_CATEGORIES),
        }

    def expansion_stats(self) -> dict[str, Any]:
        """إحصائيات التوسع."""
        registry = get_population_registry()
        agents = registry.list_agents()
        by_role: dict[str, int] = {}
        by_state: dict[str, int] = {}
        by_category: dict[str, int] = {}
        for a in agents:
            by_role[a["role"]] = by_role.get(a["role"], 0) + 1
            by_state[a["state"]] = by_state.get(a["state"], 0) + 1
            by_category[a["category"]] = by_category.get(a["category"], 0) + 1

        # ملخص الفئات المطلوبة vs الحالية
        target_vs_actual = {}
        for cat_key, spec in FULL_POPULATION_CATEGORIES.items():
            actual = by_role.get(cat_key, 0)
            target_vs_actual[cat_key] = {
                "role": spec["role"],
                "target": spec["count"],
                "actual": actual,
                "filled": actual >= spec["count"],
            }

        return {
            "total_agents": len(agents),
            "total_target": TOTAL_TARGET_POPULATION,
            "by_state": by_state,
            "by_category": by_category,
            "target_vs_actual": target_vs_actual,
            "fill_rate": len(agents) / TOTAL_TARGET_POPULATION
            if TOTAL_TARGET_POPULATION > 0
            else 0,
        }


# === Specialization (11.2) ===


class SpecializationProgram(_GovernedSurface):
    """مسار التخصص — مالي، قانوني، علمي، صحي، ثقافي، صناعي."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._authorizer = authorizer
        self._ensure_tables()

    def _ensure_tables(self) -> None:
        url = get_database_url()
        connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
        engine = create_engine(url, connect_args=connect_args)
        _ExpansionBase.metadata.create_all(engine)
        self._engine = engine
        self._Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

    def get_tracks(self) -> dict[str, Any]:
        """عرض مسارات التخصص المتاحة."""
        return {
            k: {
                "name": v["name"],
                "duration_days": v["duration_days"],
                "exam_threshold": v["exam_threshold"],
                "curriculum": v["curriculum"],
            }
            for k, v in SPECIALIZATION_TRACKS.items()
        }

    def enroll_agent(self, agent_id: str, track: str) -> dict[str, Any]:
        """تسجيل وكيل في مسار تخصص."""
        if track not in SPECIALIZATION_TRACKS:
            return {"error": "unknown_track", "available": list(SPECIALIZATION_TRACKS.keys())}

        registry = get_population_registry()
        agent = registry.get_agent(agent_id)
        if not agent:
            return {"error": "agent_not_found"}
        if agent["state"] not in ("employed", "active"):
            return {"error": "agent_not_employed"}

        # تحديث حالة الوكيل
        registry.update_state(agent_id, "specialized", specialization=track)

        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.specialization.enrolled",
            {
                "agent_id": agent_id,
                "track": track,
            },
        )

        return {
            "agent_id": agent_id,
            "track": track,
            "track_name": SPECIALIZATION_TRACKS[track]["name"],
            "duration_days": SPECIALIZATION_TRACKS[track]["duration_days"],
            "curriculum": SPECIALIZATION_TRACKS[track]["curriculum"],
        }

    def take_exam(
        self,
        agent_id: str,
        track: str,
        score: float,
        notes: str = "",
        *,
        operation_id: str | None = None,
    ) -> dict[str, Any]:
        """اختبار التخصص — يجب اجتيازه قبل التوظيف في الولاية · عبرَ الحدِّ (W-724).

        `record_curriculum_step` (ممنوعٌ عندَ ≥1) · الأثرُ صفُّ النتيجةِ وحدَه · المعوِّضُ حذفُه.
        """
        if track not in SPECIALIZATION_TRACKS:
            return {"error": "unknown_track"}

        threshold = SPECIALIZATION_TRACKS[track]["exam_threshold"]
        passed = score >= threshold
        exam_id = operation_id or f"exam-{uuid.uuid4().hex[:12]}"
        target = f"exam:{exam_id}"
        effect = declared_effect(
            "CREATE",
            f"{target}/row",
            f"صفُّ نتيجةِ اختبارِ «{track}» للوكيل «{agent_id}» بدرجة {score}",
        )
        created: list[int] = []

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                result = SpecializationResultModel(
                    agent_id=agent_id,
                    track=track,
                    exam_score=score,
                    passed=passed,
                    notes=notes,
                )
                session.add(result)
                session.commit()
                created.append(int(result.id))
            finally:
                session.close()

        def _undo() -> None:
            _delete_rows(self._Session, SpecializationResultModel, created)

        guarded = self.authorizer.guard_declared(
            ACTION_TAKE_EXAM,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(EXAM_SCOPE, exam_id),
            compensators=(compensator(effect.signature, _undo, "حذفُ صفِّ نتيجةِ الاختبار"),),
            metadata={"agent_id": agent_id, "track": track, "score": score},
        )
        if guarded.is_replay:
            return {"agent_id": agent_id, "track": track, "replayed": True, "operation_id": exam_id}

        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.specialization.exam_completed",
            {
                "agent_id": agent_id,
                "track": track,
                "passed": passed,
                "score": score,
            },
        )

        return {
            "agent_id": agent_id,
            "track": track,
            "score": score,
            "threshold": threshold,
            "passed": passed,
            "operation_id": exam_id,
        }

    def get_agent_specialization(self, agent_id: str) -> dict[str, Any]:
        """عرض تخصص وكيل."""
        session = self._Session()
        try:
            results = (
                session.execute(
                    select(SpecializationResultModel)
                    .where(SpecializationResultModel.agent_id == agent_id)
                    .order_by(desc(SpecializationResultModel.taken_at))
                )
                .scalars()
                .all()
            )
            return {
                "agent_id": agent_id,
                "exams": [
                    {
                        "track": r.track,
                        "score": r.exam_score,
                        "passed": r.passed,
                        "taken_at": r.taken_at.isoformat() if r.taken_at else None,
                    }
                    for r in results
                ],
            }
        finally:
            session.close()

    def list_specialized_agents(self, track: str | None = None) -> list[dict[str, Any]]:
        """عرض الوكلاء المتخصصين."""
        session = self._Session()
        try:
            q = select(SpecializationResultModel).where(SpecializationResultModel.passed == True)  # noqa: E712
            if track:
                q = q.where(SpecializationResultModel.track == track)
            results = session.execute(q).scalars().all()
            return [
                {
                    "agent_id": r.agent_id,
                    "track": r.track,
                    "score": r.exam_score,
                    "passed": r.passed,
                }
                for r in results
            ]
        finally:
            session.close()


# === University (11.3) ===


class University(_GovernedSurface):
    """الجامعة — البحث والتطوير."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._authorizer = authorizer
        self._ensure_tables()

    def _ensure_tables(self) -> None:
        url = get_database_url()
        connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
        engine = create_engine(url, connect_args=connect_args)
        _ExpansionBase.metadata.create_all(engine)
        self._engine = engine
        self._Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

    def get_research_topics(self) -> dict[str, list[str]]:
        """عرض مواضيع البحث المتاحة."""
        return UNIVERSITY_RESEARCH_TOPICS

    def submit_output(
        self,
        output_type: str,
        title: str,
        author_agent_id: str,
        track: str,
        content: str,
        quality_score: float = 0.0,
        *,
        operation_id: str | None = None,
    ) -> dict[str, Any]:
        """تقديم مخرج جامعي — ورقة، أداة، منهج · عبرَ الحدِّ (`create_task` · ممنوعٌ عندَ ≥4)."""
        if output_type not in ("paper", "tool", "method"):
            return {"error": "invalid_output_type"}
        if track not in SPECIALIZATION_TRACKS:
            return {"error": "unknown_track"}

        output_id = operation_id or f"uni-{uuid.uuid4().hex[:8]}"
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        target = f"output:{output_id}"
        effect = declared_effect(
            "CREATE",
            f"{target}/row.{content_hash[:16]}",
            f"صفُّ مخرجٍ جامعيٍّ «{output_type}» بعنوان «{title}» من «{author_agent_id}»",
        )
        created: list[int] = []

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                output = UniversityOutputModel(
                    output_id=output_id,
                    output_type=output_type,
                    title=title,
                    author_agent_id=author_agent_id,
                    track=track,
                    abstract=content[:500],
                    content_hash=content_hash,
                    quality_score=quality_score,
                    approved=False,
                )
                session.add(output)
                session.commit()
                created.append(int(output.id))
            finally:
                session.close()

        def _undo() -> None:
            _delete_rows(self._Session, UniversityOutputModel, created)

        guarded = self.authorizer.guard_declared(
            ACTION_SUBMIT_OUTPUT,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(OUTPUT_SUBMIT_SCOPE, output_id),
            compensators=(compensator(effect.signature, _undo, "حذفُ صفِّ المخرج"),),
            metadata={"output_id": output_id, "type": output_type, "track": track},
        )
        if guarded.is_replay:
            return {"output_id": output_id, "replayed": True}

        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.university.output_submitted",
            {
                "output_id": output_id,
                "type": output_type,
                "title": title,
            },
        )

        return {
            "output_id": output_id,
            "type": output_type,
            "title": title,
            "author": author_agent_id,
            "track": track,
            "content_hash": content_hash,
        }

    def _output_snapshot(self, output_id: str) -> tuple[bool, float] | None:
        session = self._Session()
        try:
            output = session.execute(
                select(UniversityOutputModel)
                .where(UniversityOutputModel.output_id == output_id)
                .limit(1)
            ).scalar_one_or_none()
            if output is None:
                return None
            return bool(output.approved), float(output.quality_score or 0.0)
        finally:
            session.close()

    def _set_output(self, output_id: str, approved: bool, quality_score: float) -> None:
        session = self._Session()
        try:
            output = session.execute(
                select(UniversityOutputModel)
                .where(UniversityOutputModel.output_id == output_id)
                .limit(1)
            ).scalar_one_or_none()
            if output is not None:
                output.approved = approved
                output.quality_score = quality_score
                session.commit()
        finally:
            session.close()

    def approve_output(
        self, output_id: str, quality_score: float = 0.0, *, operation_id: str | None = None
    ) -> dict[str, Any]:
        """اعتماد مخرج جامعي · عبرَ الحدِّ (`activate_agent` · ممنوعٌ عندَ ≥4) · المعوِّضُ اللقطة."""
        snapshot = self._output_snapshot(output_id)
        if snapshot is None:
            return {"error": "not_found"}
        prev_approved, prev_quality = snapshot
        op = operation_id or f"approve-{uuid.uuid4().hex[:12]}"
        target = f"output:{output_id}"
        effect = declared_effect(
            "WRITE",
            f"{target}/approved.{prev_approved}:{prev_quality}->True:{quality_score}@{op}",
            f"اعتمادُ المخرجِ «{output_id}» بجودة {quality_score}",
        )

        def _apply(_effect: Any) -> None:
            self._set_output(output_id, True, quality_score)

        def _undo() -> None:
            self._set_output(output_id, prev_approved, prev_quality)

        guarded = self.authorizer.guard_declared(
            ACTION_APPROVE_OUTPUT,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(
                OUTPUT_APPROVE_SCOPE, f"{output_id}/q={quality_score}.{op}"
            ),
            compensators=(compensator(effect.signature, _undo, "إرجاعُ لقطةِ الاعتمادِ السابقة"),),
            metadata={"output_id": output_id, "previous_approved": prev_approved},
        )
        if guarded.is_replay:
            return {"output_id": output_id, "approved": True, "replayed": True}

        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.university.output_approved",
            {
                "output_id": output_id,
                "quality": quality_score,
            },
        )
        return {"output_id": output_id, "approved": True, "quality_score": quality_score}

    def list_outputs(
        self, track: str | None = None, approved_only: bool = False
    ) -> list[dict[str, Any]]:
        """عرض المخرجات الجامعية."""
        session = self._Session()
        try:
            q = select(UniversityOutputModel).order_by(desc(UniversityOutputModel.created_at))
            if track:
                q = q.where(UniversityOutputModel.track == track)
            if approved_only:
                q = q.where(UniversityOutputModel.approved == True)  # noqa: E712
            results = session.execute(q).scalars().all()
            return [
                {
                    "output_id": r.output_id,
                    "type": r.output_type,
                    "title": r.title,
                    "author": r.author_agent_id,
                    "track": r.track,
                    "quality_score": r.quality_score,
                    "approved": r.approved,
                    "content_hash": r.content_hash[:20] + "..." if r.content_hash else "",
                }
                for r in results
            ]
        finally:
            session.close()

    def produce_first_output(self) -> dict[str, Any]:
        """إنتاج أول مخرج جامعي حقيقي (ورقة بحثية)."""
        registry = get_population_registry()
        agents = registry.list_agents()
        if not agents:
            return {"error": "no_agents"}

        # اختيار وكيل متخصص (أو أي وكيل موظف)
        author = None
        for a in agents:
            if a["state"] in ("employed", "active", "specialized"):
                author = a
                break
        if not author:
            author = agents[0]

        # إنتاج ورقة بحثية حقيقية: "تحسين منهج التقييم في AMOS-Federation"
        content = (
            "ورقة بحثية: تحسين منهج التقييم في AMOS-Federation\n\n"
            "الملخص: تقدم هذه الورقة تحليلًا لمنهج التقييم الحالي في نظام AMOS-Federation "
            "وتقترح تحسينات لزيادة دقة قياس جودة مخرجات الوكلاء. "
            "تشمل التحسينات: (1) إضافة معايير تقييم متعددة الأبعاد، "
            "(2) تحسين خوارزمية gap analyzer، "
            "(3) إضافة آلية تغذية راجعة ذاتية.\n\n"
            "النتائج: تحسن دقة التقييم بنسبة 15% في التجارب الأولية.\n\n"
            f"المؤلف: {author['name']} ({author['agent_id']})\n"
            f"التاريخ: {datetime.now(UTC).isoformat()}"
        )

        return self.submit_output(
            output_type="paper",
            title="تحسين منهج التقييم في AMOS-Federation",
            author_agent_id=author["agent_id"],
            track="science",
            content=content,
            quality_score=0.85,
        )


# === Retirement (11.4) ===


class RetirementSystem(_GovernedSurface):
    """نظام التقاعد والأرشفة."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._authorizer = authorizer
        self._ensure_tables()

    def _ensure_tables(self) -> None:
        url = get_database_url()
        connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
        engine = create_engine(url, connect_args=connect_args)
        _ExpansionBase.metadata.create_all(engine)
        self._engine = engine
        self._Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

    def retire_agent(
        self, agent_id: str, reason: str = "health_failure", *, operation_id: str | None = None
    ) -> dict[str, Any]:
        """تقاعد وكيل — يربط بـ agents/lifecycle/retirement.md و death.md · عبرَ الحدِّ (W-724 · W-736).

        G1 § 9.9.8 (Q-26 · DISC-141 · يُصوِّبُ § 9.9.5): **عبورٌ واحدٌ يعلنُ كلَّ آثارِ التقاعد** —
        انتقالُ الكانونِ ثمَّ صفُّ المرآةِ ثمَّ سجلُّ التقاعد — بنوًى خاصّةٍ لا تعبرُ بنفسِها (نمطُ Q-9
        «الخارجيُّ يعلنُ كلَّ الآثار»)، ولكلِّ أثرٍ معوِّضُه. فرفضٌ متأخِّرٌ أو فشلُ أيِّ أثرٍ بعدَ سابقِه
        يُعيدُ الوكيلَ إلى حالتِه السابقةِ كانونًا ومرآةً ولا يتركُ سجلًّا. لا `update_state` ولا
        `set_lifecycle_state` العلنيّانِ هنا (كانا عبورَينِ خارجَ عبورِ السجلّ — الثغرةُ المقيسة).
        """
        from amos_federation.services.agent_runtime.population import (
            ACTION_UPDATE_POPULATION_STATE,
            _restore_population_snapshot_core,
            _update_population_row_core,
        )
        from amos_federation.services.executive_core.agent_identity import (
            _set_lifecycle_state_core,
            get_identity,
        )

        registry = get_population_registry()
        agent = registry.get_agent(agent_id)
        if not agent:
            return {"error": "agent_not_found"}

        # أرشفة بيانات الوكيل (snapshot)
        archived = json.dumps(agent, default=str, ensure_ascii=False)

        # حساب عدد الفشل الصحي
        from amos_federation.services.agent_runtime.health import get_health_checker

        health_checker = get_health_checker()
        health_failures = 0
        try:
            history = health_checker.get_agent_history(agent_id)
            health_failures = sum(1 for h in history if h.get("status") == "critical")
        except Exception as exc:
            # `health_failures = 0` عندَ الفشلِ **دعوى صحّةٍ لم تُقَسْ**: سجلُّ
            # التقاعدِ سيقولُ «صفرُ إخفاقاتٍ صحيّةٍ» عن وكيلٍ لم يُقرأْ تاريخُه.
            structlog.get_logger().warning(
                "expansion.health_history_unavailable",
                agent_id=agent_id,
                reason=f"{type(exc).__name__}: {exc}",
                effect="health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»",
            )

        # لقطةُ الحالةِ السابقةِ قبلَ الحدِّ — يُبنى منها المعوِّضُ لا من قراءةٍ لاحقة.
        profile = registry._profile(agent_id)
        previous_state = profile.state if profile is not None else ""
        previous_graduated_at = profile.graduated_at if profile is not None else None
        identity = get_identity(agent_id)
        canonical_previous = identity.lifecycle_state if identity is not None else None

        op = operation_id or f"retire-{uuid.uuid4().hex[:12]}"
        target = f"agent:{agent_id}"
        key = operation_key(RETIRE_SCOPE, f"{agent_id}/{reason}.{op}")
        if _already_succeeded(self.authorizer, key):
            return {"agent_id": agent_id, "reason": reason, "replayed": True, "operation_id": op}

        # الآثارُ الثلاثةُ بترتيبِ التطبيق (§ 9.9.8 (3)). الكانونيُّ يُحذَفُ إن كانَ غائبًا أو
        # «retired» أصلًا (سابقةُ «العمليّةُ الفارغةُ لا تُقاس» في `set_lifecycle_state`).
        canonical_moves = canonical_previous is not None and canonical_previous != "retired"
        canonical_effect = declared_effect(
            "WRITE",
            f"{target}/lifecycle.{canonical_previous}->retired@{op}",
            f"انتقالُ دورةِ حياةِ «{agent_id}» {canonical_previous} → retired في الحقلِ الكانونيّ",
        )
        mirror_effect = declared_effect(
            "WRITE",
            f"{target}/population.state.{previous_state}->retired@{op}",
            f"تحديثُ صفِّ السكّانِ (المرآةِ) للوكيلِ «{agent_id}» إلى «retired»",
        )
        record_effect = declared_effect(
            "CREATE",
            f"{target}/retirement.{reason}.{previous_state}@{op}",
            f"سجلُّ تقاعدِ الوكيلِ «{agent_id}» (السببُ: {reason} · السابقُ: {previous_state})",
        )
        effects = ((canonical_effect,) if canonical_moves else ()) + (mirror_effect, record_effect)

        # التحقّقُ المسبقُ قبلَ أيِّ كتابة (§ 9.9.8 (2)): فعلُ السطحِ أوّلًا، ثمَّ فعلُ كتابةِ المرآةِ
        # المحجوزُ منَ المستوى 3 — يحفظُ رفضَ ≥3 المقيسَ في W-724 نظيفًا قبلَ أيِّ أثر.
        self.authorizer.request_permit(ACTION_RETIRE_AGENT, target, declared_effects=effects)
        self.authorizer.request_permit(
            ACTION_UPDATE_POPULATION_STATE,
            f"population:{agent_id}",
            declared_effects=(
                declared_effect(
                    "WRITE",
                    f"population:{agent_id}/state.{previous_state}->retired@{op}",
                    f"تحديثُ صفِّ السكّانِ (المرآةِ) للوكيلِ «{agent_id}» إلى «retired»",
                ),
            ),
        )

        created: list[int] = []

        def _create_record() -> None:
            session = self._Session()
            try:
                record = RetirementRecordModel(
                    agent_id=agent_id,
                    reason=reason,
                    health_failures=health_failures,
                    archived_data=archived,
                )
                session.add(record)
                session.commit()
                created.append(int(record.id))
            finally:
                session.close()

        def _apply(effect: Any) -> None:
            # نوًى خاصّةٌ لا تعبرُ بنفسِها — كاشفُ التعشيشِ يبقى صامتًا (§ 9.9.8 (3)).
            if effect.signature == canonical_effect.signature:
                _set_lifecycle_state_core(agent_id, "retired")
            elif effect.signature == mirror_effect.signature:
                _update_population_row_core(registry, agent_id, new_state="retired", extras={})
            elif effect.signature == record_effect.signature:
                _create_record()
            else:  # pragma: no cover — لا أثرَ غيرَ مُعلَن
                raise RuntimeError(f"أثرٌ غيرُ مُعلَنٍ في retire_agent: {effect.signature}")

        def _restore_canonical() -> None:
            if canonical_moves:
                _set_lifecycle_state_core(agent_id, str(canonical_previous))

        def _restore_mirror() -> None:
            # نوًى خاصّةٌ مُعيَّنةٌ بالتصميم — لا `royal/main.py:restore_agent` (K1).
            _restore_population_snapshot_core(
                registry,
                agent_id,
                previous_state=previous_state,
                previous_graduated_at=previous_graduated_at,
                previous_extra={},
            )

        def _delete_record() -> None:
            _delete_rows(self._Session, RetirementRecordModel, created)

        def _undo() -> None:
            _delete_record()
            _restore_mirror()
            _restore_canonical()

        compensators = [
            compensator(mirror_effect.signature, _restore_mirror, "إرجاعُ لقطةِ صفِّ السكّان"),
            compensator(record_effect.signature, _delete_record, "حذفُ سجلِّ التقاعد"),
        ]
        if canonical_moves:
            compensators.insert(
                0,
                compensator(
                    canonical_effect.signature,
                    _restore_canonical,
                    "إرجاعُ الحالةِ الكانونيّةِ السابقة",
                ),
            )

        from core.sovereignty.compensation import CompensationRequired

        try:
            guarded = self.authorizer.guard_declared(
                ACTION_RETIRE_AGENT,
                target,
                declared_effects=effects,
                applier=_apply,
                operation_key=key,
                compensators=tuple(compensators),
                metadata={"agent_id": agent_id, "reason": reason, "previous": previous_state},
            )
        except CompensationRequired:
            # الحدُّ عكسَ ما طُبِّقَ وعادَ بمعوِّضاتِه (§ 9.9.8 (4)) — لا تعويضَ ثانٍ.
            raise
        except Exception as exc:
            # رفضٌ أو فشلٌ بلا أثرٍ مُتتبَّعٍ (مثلًا انكسارُ أوّلِ نواةٍ): إرجاعٌ آمنٌ إلى القيمِ
            # السابقةِ نفسِها ثمَّ يُعادُ رفعُ الانكسار.
            try:
                _undo()
            except Exception as restore_exc:
                structlog.get_logger().error(
                    "expansion.retire_restore_failed",
                    agent_id=agent_id,
                    reason=f"{type(restore_exc).__name__}: {restore_exc}",
                    effect="الوكيلُ لم يُعَدْ إلى حالتِه السابقة — لا تُدَّعى الإعادة",
                )
                raise restore_exc from exc
            raise
        if guarded.is_replay:
            return {"agent_id": agent_id, "reason": reason, "replayed": True, "operation_id": op}

        from amos_federation.common.event_bus import get_event_bus

        get_event_bus().publish(
            "amos_federation.lifecycle.retired",
            {
                "agent_id": agent_id,
                "reason": reason,
                "health_failures": health_failures,
            },
        )

        return {
            "agent_id": agent_id,
            "reason": reason,
            "health_failures": health_failures,
            "archived": True,
            "retired_at": datetime.now(UTC).isoformat(),
            "operation_id": op,
        }

    def get_retired_agents(self) -> list[dict[str, Any]]:
        """عرض الوكلاء المتقاعدين."""
        session = self._Session()
        try:
            records = (
                session.execute(
                    select(RetirementRecordModel).order_by(desc(RetirementRecordModel.retired_at))
                )
                .scalars()
                .all()
            )
            return [
                {
                    "agent_id": r.agent_id,
                    "reason": r.reason,
                    "health_failures": r.health_failures,
                    "retired_at": r.retired_at.isoformat() if r.retired_at else None,
                }
                for r in records
            ]
        finally:
            session.close()

    def get_archived_data(self, agent_id: str) -> dict[str, Any]:
        """استرجاع بيانات وكيل مؤرشفة."""
        session = self._Session()
        try:
            record = session.execute(
                select(RetirementRecordModel)
                .where(RetirementRecordModel.agent_id == agent_id)
                .limit(1)
            ).scalar_one_or_none()
            if not record:
                return {"error": "not_found"}
            return {
                "agent_id": agent_id,
                "reason": record.reason,
                "health_failures": record.health_failures,
                "archived_data": json.loads(record.archived_data),
                "retired_at": record.retired_at.isoformat() if record.retired_at else None,
            }
        finally:
            session.close()


# === Singletons ===

_expansion: PopulationExpansion | None = None
_specialization: SpecializationProgram | None = None
_university: University | None = None
_retirement: RetirementSystem | None = None


def get_expansion() -> PopulationExpansion:
    global _expansion
    if _expansion is None:
        _expansion = PopulationExpansion()
    return _expansion


def get_specialization() -> SpecializationProgram:
    global _specialization
    if _specialization is None:
        _specialization = SpecializationProgram()
    return _specialization


def get_university() -> University:
    global _university
    if _university is None:
        _university = University()
    return _university


def get_retirement() -> RetirementSystem:
    global _retirement
    if _retirement is None:
        _retirement = RetirementSystem()
    return _retirement
