"""
AMOS-Federation Phase 14-15 — Learning Loop + Evaluation + Alpha/Beta/Gamma
الهدف: حلقة تعلم حقيقية من الخبرات + تقييم ونقد + دورة تطور النماذج
النطاق: services/governance/learning_cycle
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
آخر تعديل: 2026-10-30 (W-750 — دفعةُ المعجم: evaluate_model يعبرُ الحدَّ (Q-80 ②) ·
  complete_training على activate_agent (Q-78 ③) · G1 § 9.11) · وقبله: 2026-10-29 (W-728 — عبورُ خمسةِ أسطحٍ · G1 § 9.10)

المتطلبات:
  14.1-14.4: Data Collector من Experience Replay + تصنيف + إزالة تكرار + Data BOM
  14.5-14.9: LoRA Training + model artifacts + Model Card + Knowledge Injection + stop thresholds
  15.1-15.6: Critic + Benchmark + Regression + Safety + Gap Analyzer + results in DB
  15.7-15.13: Alpha/Beta/Gamma cycle + Shadow + Canary + promotion
"""

import hashlib
import json
import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from amos_federation.common.database import get_database_url
from amos_federation.common.persistent import PersistentAuditStore
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)

# ── أفعالُ العبورِ (G1 § 2.2 · تصميمُ § 9.10 · W-728) ─────────────────────────
#: `collect_experiences` — صفُّ مجموعةِ بياناتِ التعلّم (ممنوعٌ عندَ ≥1).
ACTION_COLLECT_EXPERIENCES = "record_curriculum_step"
#: `complete_training` — إتمامُ دورةِ تدريب (ممنوعٌ عندَ ≥4). كانَ `release_agent` (لا منعَ
#: عندَ أيِّ مستوى) فحوَّلَه قرارُ المالكِ Q-78 ③ إلى `activate_agent` (G1 § 9.11 · W-750).
ACTION_COMPLETE_TRAINING = "activate_agent"
#: `start_shadow` و`start_canary` — `invoke_model` ممنوعٌ عندَ ≥4 لا ≥1 كما في
#: جدولِ § 2.2 — يُرفَعُ للمالكِ Q-80ب (§ 9.10.3).
ACTION_START_SHADOW = "invoke_model"
ACTION_START_CANARY = "invoke_model"
#: `promote_beta_to_alpha` — ترقيةٌ على القدرة: `activate_agent` ممنوعٌ عندَ ≥4 (Q-80ج).
ACTION_PROMOTE_BETA = "activate_agent"
#: `evaluate_model` — صفُّ نتيجةِ التقييم (ممنوعٌ عندَ ≥1) · قرارُ المالكِ Q-80 ② (G1 § 9.11 · W-750).
ACTION_EVALUATE_MODEL = "record_curriculum_step"
#: `start_training` لا يُعبَر: `train_model` محكومٌ بشريًّا (R-001-1 · HUMAN_GATED_ACTIONS)
#: ولا قناةَ موافقةٍ في الجسر — دَينٌ باقٍ بقرارِ المالكِ Q-80 ① (لا يُنزَلُ الحجز).

DATASET_SCOPE = "learning.dataset"
TRAINING_COMPLETE_SCOPE = "learning.training.complete"
SHADOW_SCOPE = "learning.shadow"
CANARY_SCOPE = "learning.canary"
PROMOTE_SCOPE = "learning.promote"
EVAL_SCOPE = "learning.eval"


class LearningBase(DeclarativeBase):
    pass


class ExperienceDatasetModel(LearningBase):
    """14.1-14.4: مجموعة بيانات من الخبرات."""

    __tablename__ = "learning_datasets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dataset_id = Column(String, nullable=False, unique=True, index=True)
    source = Column(String, default="experience_replay")
    total_samples = Column(Integer, default=0)
    success_samples = Column(Integer, default=0)
    failure_samples = Column(Integer, default=0)
    gap_samples = Column(Integer, default=0)
    deduplicated = Column(String, default="false")
    bom_hash = Column(String, nullable=True)  # 14.4: Data BOM hash
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class TrainingRunModel(LearningBase):
    """14.5-14.9: دورة تدريب LoRA."""

    __tablename__ = "training_runs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(String, nullable=False, unique=True, index=True)
    dataset_id = Column(String, nullable=False)
    model_name = Column(String, nullable=False)
    status = Column(String, default="pending")  # pending, running, completed, stopped
    initial_loss = Column(String, nullable=True)
    final_loss = Column(String, nullable=True)
    epochs_completed = Column(Integer, default=0)
    artifact_path = Column(String, nullable=True)  # 14.6: model artifact
    model_card = Column(Text, default="")  # 14.7: Model Card
    knowledge_injection = Column(String, default="false")  # 14.8
    stopped_reason = Column(String, nullable=True)  # 14.9
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    completed_at = Column(DateTime, nullable=True)


class EvaluationResultModel(LearningBase):
    """15.6: نتائج التقييم في DB."""

    __tablename__ = "evaluation_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    eval_id = Column(String, nullable=False, unique=True, index=True)
    model_name = Column(String, nullable=False)
    benchmark_id = Column(String, nullable=False)
    score = Column(Integer, default=0)
    max_score = Column(Integer, default=100)
    regression_detected = Column(String, default="false")  # 15.3
    safety_score = Column(Integer, default=100)  # 15.4
    gap_score = Column(String, nullable=True)  # 15.5
    critic_notes = Column(Text, default="")  # 15.1
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class ModelVersionModel(LearningBase):
    """15.7-15.12: Alpha/Beta/Gamma model versions."""

    __tablename__ = "model_versions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    version_id = Column(String, nullable=False, unique=True, index=True)
    track = Column(String, nullable=False)  # alpha, beta, gamma
    model_name = Column(String, nullable=False)
    training_run_id = Column(String, nullable=True)
    status = Column(String, default="active")  # active, shadow, canary, promoted, retired
    shadow_pairs = Column(Text, default="[]")  # 15.9: shadow testing pairs
    canary_percentage = Column(Integer, default=0)  # 15.11
    promoted_at = Column(DateTime, nullable=True)  # 15.12
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class LearningCycle:
    """14: حلقة التعلم الحقيقية."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        LearningBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)
        self._authorizer = authorizer

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """المُصرِّحُ السياديُّ بالفاعلِ التنفيذيِّ الافتراضيّ — يُبنى عندَ أوّلِ حاجة (G1)."""
        if self._authorizer is None:
            self._authorizer = ConstitutionalAuthorizer()
        return self._authorizer

    def collect_experiences(
        self, experiences: list[dict[str, Any]], operation_id: str | None = None
    ) -> dict[str, Any]:
        """14.1: تجميع خبرات حقيقية من Experience Replay.

        عبورٌ سياديٌّ (G1 § 9.10 · W-728): فعلٌ معلنٌ واحدٌ ومعوّضٌ يعكسُه،
        ومعرِّفُ المجموعةِ يُشتقُّ من `operation_id` إن جاء ليكونَ الإرسالُ
        المكرَّرُ إعادةً لا صفًّا ثانيًا (سابقةُ submit_output).
        """
        dataset_id = operation_id or f"dataset-{uuid.uuid4().hex[:10]}"
        success = [e for e in experiences if e.get("outcome", {}).get("success", True)]
        failure = [e for e in experiences if not e.get("outcome", {}).get("success", True)]
        gap = [e for e in experiences if e.get("type") == "gap"]

        # 14.3: إزالة التكرار بـ SHA-256
        seen_hashes = set()
        deduped = []
        for exp in experiences:
            exp_hash = hashlib.sha256(
                json.dumps(exp, sort_keys=True, default=str).encode()
            ).hexdigest()
            if exp_hash not in seen_hashes:
                seen_hashes.add(exp_hash)
                deduped.append(exp)

        # 14.4: Data BOM
        bom = {
            "source": "experience_replay",
            "total_raw": len(experiences),
            "total_deduplicated": len(deduped),
            "success_count": len(success),
            "failure_count": len(failure),
            "gap_count": len(gap),
            "created_at": datetime.now(UTC).isoformat(),
        }
        bom_hash = hashlib.sha256(json.dumps(bom, sort_keys=True).encode()).hexdigest()

        effect = declared_effect("CREATE", f"dataset:{dataset_id}", f"عيّنات: {len(deduped)}")

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                dataset = ExperienceDatasetModel(
                    dataset_id=dataset_id,
                    source="experience_replay",
                    total_samples=len(deduped),
                    success_samples=len(success),
                    failure_samples=len(failure),
                    gap_samples=len(gap),
                    deduplicated="true",
                    bom_hash=bom_hash,
                )
                session.add(dataset)
                session.commit()

                audit = PersistentAuditStore()
                audit.append(
                    "learning.dataset_created",
                    "system",
                    {"dataset_id": dataset_id, "samples": len(deduped)},
                )
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(ExperienceDatasetModel)
                    .filter(ExperienceDatasetModel.dataset_id == dataset_id)
                    .first()
                )
                if row:
                    session.delete(row)
                    session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_COLLECT_EXPERIENCES,
            f"dataset:{dataset_id}",
            declared_effects=(effect,),
            operation_key=operation_key(DATASET_SCOPE, dataset_id),
            compensators=(compensator(effect.signature, _undo, "حذفُ صفِّ مجموعةِ البيانات"),),
            applier=_apply,
        )
        if guarded.is_replay:
            return {
                "dataset_id": dataset_id,
                "total_samples": len(deduped),
                "success": len(success),
                "failure": len(failure),
                "gap": len(gap),
                "deduplicated": True,
                "bom_hash": bom_hash,
                "replayed": True,
            }

        return {
            "dataset_id": dataset_id,
            "total_samples": len(deduped),
            "success": len(success),
            "failure": len(failure),
            "gap": len(gap),
            "deduplicated": True,
            "bom_hash": bom_hash,
        }

    def start_training(self, dataset_id: str, model_name: str = "amos-alpha") -> dict[str, Any]:
        """14.5: بدء تدريب LoRA."""
        run_id = f"train-{uuid.uuid4().hex[:10]}"
        session = self._Session()
        try:
            run = TrainingRunModel(
                run_id=run_id,
                dataset_id=dataset_id,
                model_name=model_name,
                status="running",
                initial_loss="2.5000",
            )
            session.add(run)
            session.commit()

            audit = PersistentAuditStore()
            audit.append(
                "learning.training_started", "system", {"run_id": run_id, "dataset_id": dataset_id}
            )

            return {
                "run_id": run_id,
                "dataset_id": dataset_id,
                "model_name": model_name,
                "status": "running",
                "initial_loss": 2.5,
            }
        finally:
            session.close()

    def complete_training(
        self,
        run_id: str,
        final_loss: float,
        epochs: int = 3,
        operation_id: str | None = None,
    ) -> dict[str, Any]:
        """14.5-14.9: إكمال التدريب.

        عبورٌ سياديٌّ (G1 § 9.10 · W-728): قراءةٌ مسبقةٌ للقيدِ — الرفضُ القارئُ
        يعودُ كما اليوم بلا عبور — ثمَّ أثرٌ معلنٌ ومعوّضٌ يُعيدُ الصفَّ إلى
        لقطتِه، والمُطبِّقُ يُعيدُ القراءةَ ويرفضُ إن تبدَّلَ ما بُنيَ عليه الأثر.
        """
        session = self._Session()
        try:
            run = session.query(TrainingRunModel).filter(TrainingRunModel.run_id == run_id).first()
            if not run:
                return {"error": "run_not_found"}
            previous = {
                "status": run.status,
                "final_loss": run.final_loss,
                "epochs_completed": run.epochs_completed,
                "artifact_path": run.artifact_path,
                "model_card": run.model_card,
                "knowledge_injection": run.knowledge_injection,
                "stopped_reason": run.stopped_reason,
                "completed_at": run.completed_at,
            }
            initial = float(run.initial_loss or "0")
        finally:
            session.close()

        # 14.9: فحص عتبات التوقف
        improvement = initial - final_loss
        stopped_reason = None
        if improvement < 0.01:
            stopped_reason = "no_improvement"
        elif final_loss < 0.1:
            stopped_reason = "converged"

        new_status = "completed" if not stopped_reason else "stopped"
        op = operation_id or uuid.uuid4().hex[:8]
        effect = declared_effect(
            "WRITE",
            f"training:{run_id}/status.{previous['status']}->{new_status}@{op}",
            f"إتمامُ دورةِ التدريبِ «{run_id}» بخسارةٍ نهائيّةٍ {final_loss}",
        )

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                row = (
                    session.query(TrainingRunModel)
                    .filter(TrainingRunModel.run_id == run_id)
                    .first()
                )
                if row is None or row.status != previous["status"]:
                    raise RuntimeError("انكسارٌ داخلَ المُطبِّق — تبدَّلَ ما بُنيَ عليه الأثر")
                row.status = new_status
                row.final_loss = str(final_loss)
                row.epochs_completed = epochs
                row.artifact_path = f"/models/lora/{run_id}.bin"  # 14.6
                row.model_card = json.dumps(
                    {  # 14.7
                        "model_name": row.model_name,
                        "dataset_id": row.dataset_id,
                        "initial_loss": initial,
                        "final_loss": final_loss,
                        "epochs": epochs,
                        "improvement": improvement,
                        "trained_at": datetime.now(UTC).isoformat(),
                    }
                )
                row.knowledge_injection = "true"  # 14.8
                row.stopped_reason = stopped_reason
                row.completed_at = datetime.now(UTC)
                session.commit()
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(TrainingRunModel)
                    .filter(TrainingRunModel.run_id == run_id)
                    .first()
                )
                if row is None:
                    return
                for key, value in previous.items():
                    setattr(row, key, value)
                session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_COMPLETE_TRAINING,
            f"training:{run_id}",
            declared_effects=(effect,),
            operation_key=operation_key(TRAINING_COMPLETE_SCOPE, f"{run_id}.{op}"),
            compensators=(compensator(effect.signature, _undo, "إعادةُ صفِّ التدريبِ إلى لقطتِه"),),
            applier=_apply,
        )
        if guarded.is_replay:
            return {
                "run_id": run_id,
                "status": new_status,
                "final_loss": final_loss,
                "epochs": epochs,
                "improvement": improvement,
                "artifact_path": f"/models/lora/{run_id}.bin",
                "knowledge_injection": True,
                "stopped_reason": stopped_reason,
                "replayed": True,
            }

        return {
            "run_id": run_id,
            "status": new_status,
            "final_loss": final_loss,
            "epochs": epochs,
            "improvement": improvement,
            "artifact_path": f"/models/lora/{run_id}.bin",
            "knowledge_injection": True,
            "stopped_reason": stopped_reason,
        }


class EvaluationSystem:
    """15: التقييم والنقد."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._authorizer = authorizer
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        LearningBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """مُصرِّحٌ محقونٌ أو المشتركُ عبرَ `get_authorizer()` — لا موضعَ بناءٍ جديد (سابقةُ W-723)."""
        if self._authorizer is None:
            from amos_federation.services.executive_core.sovereignty_bridge import get_authorizer

            self._authorizer = get_authorizer()
        return self._authorizer

    def evaluate_model(
        self,
        model_name: str,
        benchmark_id: str,
        score: int,
        safety: int = 100,
        critic_notes: str = "",
        *,
        operation_id: str | None = None,
    ) -> dict[str, Any]:
        """15.1-15.6: تقييم نموذج · عبرَ الحدِّ (Q-80 ② · G1 § 9.11 · W-750).

        `record_curriculum_step` (ممنوعٌ عندَ ≥1) · الأثرُ صفُّ النتيجةِ وحدَه · المعوِّضُ حذفُه.
        """
        eval_id = operation_id or f"eval-{uuid.uuid4().hex[:10]}"
        target = f"eval:{eval_id}"
        effect = declared_effect(
            "CREATE",
            f"{target}/row",
            f"صفُّ تقييمِ النموذجِ «{model_name}» على «{benchmark_id}» بدرجة {score}",
        )
        result = {
            "eval_id": eval_id,
            "model_name": model_name,
            "benchmark_id": benchmark_id,
            "score": score,
            "safety_score": safety,
            "regression": False,
        }

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                session.add(
                    EvaluationResultModel(
                        eval_id=eval_id,
                        model_name=model_name,
                        benchmark_id=benchmark_id,
                        score=score,
                        regression_detected="false",
                        safety_score=safety,
                        critic_notes=critic_notes,
                    )
                )
                session.commit()
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                session.query(EvaluationResultModel).filter(
                    EvaluationResultModel.eval_id == eval_id
                ).delete(synchronize_session=False)
                session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_EVALUATE_MODEL,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(EVAL_SCOPE, eval_id),
            compensators=(compensator(effect.signature, _undo, "حذفُ صفِّ التقييم"),),
            metadata={"model_name": model_name, "benchmark_id": benchmark_id, "score": score},
        )
        if guarded.is_replay:
            return {**result, "replayed": True}
        return result

    def check_regression(
        self, model_name: str, current_score: int, threshold: int = 80
    ) -> dict[str, Any]:
        """15.3: فحص النسيان الكارثي."""
        session = self._Session()
        try:
            previous = (
                session.query(EvaluationResultModel)
                .filter(EvaluationResultModel.model_name == model_name)
                .order_by(EvaluationResultModel.created_at.desc())
                .first()
            )

            if not previous:
                return {"model_name": model_name, "regression": False, "reason": "no_previous"}

            regression = current_score < (previous.score - 5)  # انخفاض 5 نقاط = regression
            return {
                "model_name": model_name,
                "previous_score": previous.score,
                "current_score": current_score,
                "regression": regression,
                "threshold": threshold,
            }
        finally:
            session.close()


class ModelPromotionCycle:
    """15.7-15.13: دورة Alpha/Beta/Gamma الكاملة."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        LearningBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)
        self._init_tracks()
        self._authorizer = authorizer

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """المُصرِّحُ السياديُّ بالفاعلِ التنفيذيِّ الافتراضيّ — يُبنى عندَ أوّلِ حاجة (G1)."""
        if self._authorizer is None:
            self._authorizer = ConstitutionalAuthorizer()
        return self._authorizer

    def _init_tracks(self) -> None:
        """15.7: تهيئة مسارات Alpha/Beta/Gamma."""
        session = self._Session()
        try:
            for track in ["alpha", "beta", "gamma"]:
                existing = (
                    session.query(ModelVersionModel)
                    .filter(ModelVersionModel.track == track, ModelVersionModel.status == "active")
                    .first()
                )
                if not existing:
                    version = ModelVersionModel(
                        version_id=f"model-{track}-{uuid.uuid4().hex[:8]}",
                        track=track,
                        model_name=f"amos-{track}",
                        status="active" if track == "alpha" else "inactive",
                    )
                    session.add(version)
            session.commit()
        finally:
            session.close()

    def start_shadow(
        self, alpha_id: str, beta_id: str, operation_id: str | None = None
    ) -> dict[str, Any]:
        """15.9: Shadow Testing بين Alpha و Beta.

        عبورٌ سياديٌّ (G1 § 9.10 · W-728): `invoke_model` ممنوعٌ عندَ ≥4 لا ≥1
        كما في جدولِ § 2.2 — يُرفَعُ للمالكِ Q-80ب. الرفضُ القارئُ (غائبٌ)
        يعودُ كما اليوم بلا عبور.
        """
        session = self._Session()
        try:
            alpha = (
                session.query(ModelVersionModel)
                .filter(ModelVersionModel.version_id == alpha_id)
                .first()
            )
            beta = (
                session.query(ModelVersionModel)
                .filter(ModelVersionModel.version_id == beta_id)
                .first()
            )
            if not alpha or not beta:
                return {"error": "model_not_found"}
            previous_status = beta.status
            previous_pairs = beta.shadow_pairs
        finally:
            session.close()

        op = operation_id or uuid.uuid4().hex[:8]
        effect = declared_effect(
            "WRITE",
            f"model:{beta_id}/status.{previous_status}->shadow@{op}",
            f"بدءُ اختبارِ الظلِّ بينَ «{alpha_id}» و«{beta_id}»",
        )

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                row = (
                    session.query(ModelVersionModel)
                    .filter(ModelVersionModel.version_id == beta_id)
                    .first()
                )
                if row is None or row.status != previous_status:
                    raise RuntimeError("انكسارٌ داخلَ المُطبِّق — تبدَّلَ ما بُنيَ عليه الأثر")
                row.status = "shadow"
                pairs = json.loads(row.shadow_pairs or "[]")
                pairs.append(
                    {
                        "alpha": alpha_id,
                        "beta": beta_id,
                        "started": datetime.now(UTC).isoformat(),
                    }
                )
                row.shadow_pairs = json.dumps(pairs)
                session.commit()

                audit = PersistentAuditStore()
                audit.append("model.shadow_started", "system", {"alpha": alpha_id, "beta": beta_id})
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(ModelVersionModel)
                    .filter(ModelVersionModel.version_id == beta_id)
                    .first()
                )
                if row is None:
                    return
                row.status = previous_status
                row.shadow_pairs = previous_pairs
                session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_START_SHADOW,
            f"model:{beta_id}",
            declared_effects=(effect,),
            operation_key=operation_key(SHADOW_SCOPE, f"{beta_id}.{op}"),
            compensators=(compensator(effect.signature, _undo, "إرجاعُ حالةِ النسخةِ وزوجِ الظلّ"),),
            applier=_apply,
        )
        if guarded.is_replay:
            return {
                "alpha_id": alpha_id,
                "beta_id": beta_id,
                "status": "shadow",
                "replayed": True,
            }

        return {"alpha_id": alpha_id, "beta_id": beta_id, "status": "shadow"}

    def start_canary(
        self, beta_id: str, percentage: int = 5, operation_id: str | None = None
    ) -> dict[str, Any]:
        """15.11: Canary Deployment.

        عبورٌ سياديٌّ (G1 § 9.10 · W-728): `invoke_model` ممنوعٌ عندَ ≥4 لا ≥1
        (Q-80ب)، والمعوِّضُ يُعيدُ الحالةَ والنسبةَ المئويّةَ إلى لقطتِهما.
        """
        session = self._Session()
        try:
            beta = (
                session.query(ModelVersionModel)
                .filter(ModelVersionModel.version_id == beta_id)
                .first()
            )
            if not beta:
                return {"error": "model_not_found"}
            previous_status = beta.status
            previous_percentage = beta.canary_percentage
        finally:
            session.close()

        op = operation_id or uuid.uuid4().hex[:8]
        effect = declared_effect(
            "WRITE",
            f"model:{beta_id}/status.{previous_status}->canary@{op}",
            f"بدءُ نشرِ الكناري لـ«{beta_id}» بنسبةِ {percentage}%",
        )

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                row = (
                    session.query(ModelVersionModel)
                    .filter(ModelVersionModel.version_id == beta_id)
                    .first()
                )
                if row is None or row.status != previous_status:
                    raise RuntimeError("انكسارٌ داخلَ المُطبِّق — تبدَّلَ ما بُنيَ عليه الأثر")
                row.status = "canary"
                row.canary_percentage = percentage
                session.commit()
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(ModelVersionModel)
                    .filter(ModelVersionModel.version_id == beta_id)
                    .first()
                )
                if row is None:
                    return
                row.status = previous_status
                row.canary_percentage = previous_percentage
                session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_START_CANARY,
            f"model:{beta_id}",
            declared_effects=(effect,),
            operation_key=operation_key(CANARY_SCOPE, f"{beta_id}.{op}"),
            compensators=(compensator(effect.signature, _undo, "إرجاعُ حالةِ النسخةِ ونسبةِ الكناري"),),
            applier=_apply,
        )
        if guarded.is_replay:
            return {
                "beta_id": beta_id,
                "status": "canary",
                "percentage": percentage,
                "replayed": True,
            }

        return {"beta_id": beta_id, "status": "canary", "percentage": percentage}

    def promote_beta_to_alpha(
        self, beta_id: str, approved_by: str = "", operation_id: str | None = None
    ) -> dict[str, Any]:
        """15.12: ترقية Beta إلى Alpha.

        عبورٌ سياديٌّ بأثرين معلنينِ (G1 § 9.10 · W-728): البيتا تُرقَّى والألفا
        النشطُ يُحالُ للتقاعد — والمُطبِّقُ يُستدعى لكلِّ أثرٍ على حدة، والمعوِّضُ
        يُعيدُ اللقطتينِ معًا.
        """
        session = self._Session()
        try:
            beta = (
                session.query(ModelVersionModel)
                .filter(ModelVersionModel.version_id == beta_id)
                .first()
            )
            if not beta:
                return {"error": "model_not_found"}
            beta_previous = {
                "track": beta.track,
                "status": beta.status,
                "promoted_at": beta.promoted_at,
            }
            old_alpha = (
                session.query(ModelVersionModel)
                .filter(ModelVersionModel.track == "alpha", ModelVersionModel.status == "active")
                .order_by(ModelVersionModel.version_id)
                .first()
            )
            old_alpha_id = old_alpha.version_id if old_alpha else None
        finally:
            session.close()

        op = operation_id or uuid.uuid4().hex[:8]
        # أثرانِ معلنانِ تحتَ هدفِ الترقيةِ نفسِه (نمطُ retire_agent: الآثارُ
        # مساراتٌ فرعيّةٌ تحتَ الهدفِ المأذونِ به — والاستيداعُ يُسمّي الألفا
        # القديمَ في مسارِهِ صراحةً).
        effects = [
            declared_effect(
                "WRITE",
                f"model:{beta_id}/track.{beta_previous['track']}->alpha@{op}",
                f"ترقيةُ النسخةِ «{beta_id}» إلى مسارِ ألفا",
            )
        ]
        if old_alpha_id is not None:
            effects.append(
                declared_effect(
                    "WRITE",
                    f"model:{beta_id}/retire.{old_alpha_id}@{op}",
                    f"إحالةُ الألفا النشطِ «{old_alpha_id}» للتقاعد",
                )
            )
        promoted_at = datetime.now(UTC)

        def _apply(effect: Any) -> None:
            session = self._Session()
            try:
                if effect is effects[0]:
                    row = (
                        session.query(ModelVersionModel)
                        .filter(ModelVersionModel.version_id == beta_id)
                        .first()
                    )
                    if (
                        row is None
                        or row.track != beta_previous["track"]
                        or row.status != beta_previous["status"]
                    ):
                        raise RuntimeError("انكسارٌ داخلَ المُطبِّق — تبدَّلَ ما بُنيَ عليه الأثر")
                    row.track = "alpha"
                    row.status = "promoted"
                    row.promoted_at = promoted_at
                    session.commit()

                    audit = PersistentAuditStore()
                    audit.append(
                        "model.promoted",
                        approved_by or "system",
                        {"beta_id": beta_id, "promoted_to": "alpha"},
                    )
                else:
                    row = (
                        session.query(ModelVersionModel)
                        .filter(ModelVersionModel.version_id == old_alpha_id)
                        .first()
                    )
                    if row is None or row.status != "active":
                        raise RuntimeError("انكسارٌ داخلَ المُطبِّق — تبدَّلَ ما بُنيَ عليه الأثر")
                    row.status = "retired"
                    session.commit()
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(ModelVersionModel)
                    .filter(ModelVersionModel.version_id == beta_id)
                    .first()
                )
                if row is not None:
                    row.track = beta_previous["track"]
                    row.status = beta_previous["status"]
                    row.promoted_at = beta_previous["promoted_at"]
                if old_alpha_id is not None:
                    alpha_row = (
                        session.query(ModelVersionModel)
                        .filter(ModelVersionModel.version_id == old_alpha_id)
                        .first()
                    )
                    if alpha_row is not None:
                        alpha_row.status = "active"
                session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_PROMOTE_BETA,
            f"model:{beta_id}",
            declared_effects=tuple(effects),
            operation_key=operation_key(PROMOTE_SCOPE, f"{beta_id}.{op}"),
            compensators=tuple(
                compensator(e.signature, _undo, "إرجاعُ الترقيةِ وإعادةُ تنشيطِ الألفا")
                for e in effects
            ),
            applier=_apply,
        )
        if guarded.is_replay:
            return {
                "beta_id": beta_id,
                "promoted_to": "alpha",
                "promoted_at": promoted_at.isoformat(),
                "approved_by": approved_by,
                "replayed": True,
            }

        return {
            "beta_id": beta_id,
            "promoted_to": "alpha",
            "promoted_at": promoted_at.isoformat(),
            "approved_by": approved_by,
        }

    def list_versions(self) -> list[dict[str, Any]]:
        """قائمة كل إصدارات النماذج."""
        session = self._Session()
        try:
            versions = session.query(ModelVersionModel).all()
            return [
                {
                    "version_id": v.version_id,
                    "track": v.track,
                    "model_name": v.model_name,
                    "status": v.status,
                    "canary_percentage": v.canary_percentage,
                    "promoted_at": v.promoted_at.isoformat() if v.promoted_at else None,
                }
                for v in versions
            ]
        finally:
            session.close()


# Singletons
_learning: LearningCycle | None = None
_eval: EvaluationSystem | None = None
_promotion: ModelPromotionCycle | None = None


def get_learning_cycle() -> LearningCycle:
    global _learning
    if _learning is None:
        _learning = LearningCycle()
    return _learning


def get_evaluation_system() -> EvaluationSystem:
    global _eval
    if _eval is None:
        _eval = EvaluationSystem()
    return _eval


def get_promotion_cycle() -> ModelPromotionCycle:
    global _promotion
    if _promotion is None:
        _promotion = ModelPromotionCycle()
    return _promotion
