"""
AMOS-Federation Persistent Model Registry
الهدف: سجل نماذج دائم في قاعدة البيانات — لا يتبخّر بإعادة التشغيل
النطاق: training (model registry)
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-04

قرارُ المالكِ في Q-39 (أ) — 2026-08-23. كان سجلُّ النماذجِ في ذاكرةِ العمليّةِ
(`InMemoryModelRegistry`)، فترقيةُ نموذجٍ إلى الإنتاجِ قرارٌ يُدوَّنُ في الذاكرةِ
و يزولُ بإعادةِ التشغيل. والآن صار في جدولٍ دائمٍ على `Base` المشترك، يُنشأُ
آليًّا عبر `init_db()`، ويُقرأُ في عمليّةٍ مستقلّةٍ بعدَ انتهاءِ الأولى — وهو ما
يُثبِتُه مِسبارُ نجاةِ الحالةِ (`restart_survival_probe.py`).

لا يُلمَسُ `common/database.py` (WI-054) — الاستيرادُ منه فقط: `Base` و
`get_session_factory` و`init_db`.
"""

import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import JSON, Column, String

from amos_federation.common.database import Base, get_session_factory, init_db


class TrainingModelModel(Base):
    """جدولُ سجلِّ النماذجِ الدائم — قرارُ المالكِ في Q-39 (أ) · WI-055.

    كلُّ نموذجٍ يُدرَّبُ ويُرقّى إلى الإنتاجِ يُكتَبُ هنا، فلا يزولُ بإعادةِ
    التشغيل. و`model_card` كائنٌ JSON كاملٌ يحفظُ بطاقةَ النموذجِ كما كانت
    في الذاكرةِ — لا تُفقدُ تفاصيلُها.
    """

    __tablename__ = "training_models"

    id = Column(String, primary_key=True)
    model_card = Column(JSON, default=dict)
    status = Column(String, default="registered")
    #: نصوصُ ISO حفظًا لعقدِ الواجهةِ كما كانَ قبلَ الإدامةِ — لا تغييرَ في الشكل.
    created_at = Column(String, default="")
    updated_at = Column(String, default="")


# تهيئة قاعدة البيانات عند الاستيراد — مثل `common/persistent.py`.
# يضمنُ أنَّ الجدولَ موجودٌ قبلَ أيِّ كتابةٍ، في الاختبارِ وفي الإنتاجِ.
init_db()


class PersistentModelRegistry:
    """سجلُّ نماذجَ دائمٌ في قاعدةِ البياناتِ — ينجو من إعادةِ التشغيل.

    T4/E4-DURABILITY: WI-055 · قرارُ المالكِ في Q-39 (أ). النماذجُ المُدرَّبةُ
    وترقياتُها إلى الإنتاجِ تُكتَبُ في جدولِ `training_models` الدائمِ، فلا تُفقَدُ
    بإعادةِ التشغيلِ. والقرارُ السياديُّ هو الذي أذِنَ بهذا الانتقالَ من الذاكرةِ
    إلى القاعدةِ — لا تُغيِّرُ الحوكمةُ من أجلِ تمريرِ العمل.
    """

    @staticmethod
    def _as_dict(row: TrainingModelModel) -> dict[str, Any]:
        return {
            "model_id": row.id,
            "model_card": row.model_card or {},
            "status": row.status,
            "created_at": row.created_at,
            "updated_at": row.updated_at,
        }

    def register(self, model_data: dict[str, Any]) -> dict[str, Any]:
        """تسجيل نموذج جديد مع Model Card تلقائي."""
        model_id = model_data.get("model_id") or f"model-{uuid.uuid4()}"
        timestamp = datetime.now(UTC).isoformat()

        model_card = {
            "model_id": model_id,
            "name": model_data.get("name", "unnamed"),
            "version": model_data.get("version", "1.0"),
            "base_model": model_data.get("base_model", "unknown"),
            "training_dataset": model_data.get("dataset_id"),
            "training_date": timestamp,
            "training_method": model_data.get("training_method", "LoRA"),
            "hyperparameters": model_data.get("hyperparameters", {}),
            "metrics": model_data.get("metrics", {}),
            "description": model_data.get("description", ""),
            "license": model_data.get("license", "proprietary"),
            "intended_use": model_data.get("intended_use", ""),
            "limitations": model_data.get("limitations", []),
            "knowledge_injection": model_data.get("knowledge_injection", False),
        }

        record = {
            "model_id": model_id,
            "model_card": model_card,
            "status": model_data.get("status", "registered"),
            "created_at": timestamp,
            "updated_at": timestamp,
        }

        session_local = get_session_factory()
        session = session_local()
        try:
            row = TrainingModelModel(
                id=model_id,
                model_card=model_card,
                status=record["status"],
                created_at=timestamp,
                updated_at=timestamp,
            )
            session.merge(row)
            session.commit()
            return record
        finally:
            session.close()

    def get(self, model_id: str) -> dict[str, Any] | None:
        """إرجاع نموذج بالمعرّف."""
        session_local = get_session_factory()
        session = session_local()
        try:
            row = (
                session.query(TrainingModelModel).filter(TrainingModelModel.id == model_id).first()
            )
            return None if row is None else self._as_dict(row)
        finally:
            session.close()

    def list_all(self, status: str | None = None, limit: int = 50) -> list[dict[str, Any]]:
        """عرض النماذج مع فلترة اختيارية."""
        session_local = get_session_factory()
        session = session_local()
        try:
            query = session.query(TrainingModelModel)
            if status:
                query = query.filter(TrainingModelModel.status == status)
            rows = query.limit(limit).all()
            return [self._as_dict(r) for r in rows]
        finally:
            session.close()

    def update_status(self, model_id: str, new_status: str) -> dict[str, Any] | None:
        """تحديث حالة نموذج (registered → trained → evaluated → promoted)."""
        session_local = get_session_factory()
        session = session_local()
        try:
            row = (
                session.query(TrainingModelModel).filter(TrainingModelModel.id == model_id).first()
            )
            if row is None:
                return None
            row.status = new_status
            row.updated_at = datetime.now(UTC).isoformat()
            session.commit()
            return self._as_dict(row)
        finally:
            session.close()

    def count(self) -> int:
        """عدد النماذج."""
        session_local = get_session_factory()
        session = session_local()
        try:
            return session.query(TrainingModelModel).count()
        finally:
            session.close()
