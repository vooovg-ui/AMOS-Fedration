"""
AMOS-Federation Real Model Layer
الهدف: طبقة نماذج حقيقية مع caching، cost tracking دائم، و benchmark
النطاق: services/model_gateway/model_layer
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
تاريخ آخر تعديل: 2026-08-24 (W-036 — تنفيذُ Q-42 بشقَّيه)
"""

import hashlib
import time
import uuid
from datetime import UTC, datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from amos_federation.common.database import get_database_url
from amos_federation.common.money import COST_SCALE, CostMoneyType, to_cost


class ModelBase(DeclarativeBase):
    pass


class ModelCacheModel(ModelBase):
    """ذاكرة تخزين مؤقت للاستدعاءات النماذج."""

    __tablename__ = "model_cache"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cache_key = Column(String, nullable=False, unique=True, index=True)
    prompt_hash = Column(String, nullable=False, index=True)
    model = Column(String, nullable=False)
    response = Column(Text, nullable=False)
    tokens = Column(Integer, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class CostLogModel(ModelBase):
    """سجل التكلفة الدائم."""

    __tablename__ = "model_cost_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    invocation_id = Column(String, nullable=False, unique=True)
    model = Column(String, nullable=False)
    tokens = Column(Integer, default=0)
    #: كلفةٌ بالدولارِ الحقيقيِّ — مالٌ بلا خلافٍ في تصنيفِه، فـ`NUMERIC(20,4)`
    #: لا نصًّا ولا عائمًا (الهجرة 014 · Q-20). والقيمةُ في بايثون `Decimal`.
    #:
    #: ومقياسُه منذُ W-036 هو `NUMERIC(20,8)` لا `(20,4)` — بحسمِ المالكِ في
    #: **Q-42 · الشقِّ الثاني · (أ)**: «توسيعُ دقّةِ أعمدةِ الكلفةِ وحدَها»
    #: (الهجرة 016). والسببُ مقيسٌ: كلفةُ نداءٍ أقلَّ من `0.00005$` كانَت
    #: تُقَيّدُ **صفرًا** في الرقمِ المنشورِ، وأرخصُ سعرٍ في جدولَي التسعيرِ
    #: `0.0000008$` للرمزِ — فأربعُ منازلَ كانَت تُبلِعُ ألفَ نداءٍ صغيرٍ.
    #: ولا يُقرأُ هذا نقضًا لـQ-20: سائرُ أعمدةِ المالِ باقيةٌ على `MoneyType`.
    cost_usd = Column(CostMoneyType, nullable=False, default=Decimal("0"))
    latency_ms = Column(Integer, default=0)
    source = Column(String, default="local")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


def _money_from_provider_float(value: float) -> Decimal:
    """يُحوِّلُ كلفةً عائمةً آتيةً من حسابِ التسعيرِ إلى مبلغٍ عشريٍّ — نقطةً واحدةً مُعلَنة.

    ## لماذا دالّةٌ باسمٍ لا `str()` في مكانِها

    `to_money` يرفضُ العائمَ عن قصدٍ («خطأٌ لا رأي»). وكان الرمزُ يكتبُ
    `str(cost_usd)` فيُبيِّضُ العائمَ نصًّا ويمرُّ من البابِ الذي جاءَ ليردَّه.
    فالتبييضُ الصامتُ أُلغيَ، وبقيَ التحويلُ **واحدًا وباسمٍ يُقرأ**، لأنَّ سلسلةَ
    حسابِ الكلفةِ في هذه البوّابةِ (`PRICING` و`compute_cost`) عائمةٌ كلُّها،
    وتحويلُها إلى `Decimal` يُغيِّرُ نوعَ ردٍّ عامٍّ (`cost_usd: float` في
    `main.py`) فلا يُفعَلُ بلا قرار: هو مُقيَّدٌ سؤالًا مستقلًّا **Q-29**.

    والتقريبُ قبلَ التحويلِ مقصودٌ: هو دقّةُ عقدِ العمودِ نفسِها، فلا تُخزَّنُ
    منازلُ لا يعترفُ بها العقد.

    ## ما تغيَّرَ في W-036 (Q-42 · (أ)) ولماذا ليسَ انحرافًا صامتًا

    كانَ التقريبُ إلى **أربعِ** منازلَ والتحويلُ بـ`to_money`، فكانَت كلفةُ نداءٍ
    أقلَّ من `0.00005$` تُقَيّدُ `0.0000`. وصارَ إلى **ثمانٍ** وبـ`to_cost` بنصِّ
    المالكِ في Q-42 (أ). والمقياسُ مقروءٌ من `COST_SCALE` لا مكتوبٌ رقمًا هنا:
    رقمٌ منسوخٌ في موضعِ التقريبِ هو الطريقُ إلى مقياسَينِ يختلفانِ بلا أن يراهُما
    أحدٌ — فيُقرَّبَ إلى أربعٍ ويُخزَّنَ في عمودٍ ذي ثمانٍ.

    والاسمُ لم يُغيَّرْ وهو يُستدعى في حرسٍ قائمٍ باسمِه، وإبدالُه كانَ سيُسقِطُ
    الحرسَ لسببٍ ليسَ هو السببَ المقصودَ.
    """
    return to_cost(f"{value:.{COST_SCALE}f}")


class ModelLayer:
    """طبقة النماذج الحقيقية مع caching و cost tracking دائم."""

    # أسعار حقيقية لكل ألف رمز (USD)
    PRICING = {
        "claude-sonnet-4": {"input": 0.003, "output": 0.015},
        "claude-opus-4": {"input": 0.015, "output": 0.075},
        "claude-haiku-3.5": {"input": 0.0008, "output": 0.004},
        "local-fallback": {"input": 0.0, "output": 0.0},
        "local-model": {"input": 0.0, "output": 0.0},
    }

    def __init__(self) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        ModelBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)

    def _hash_prompt(self, prompt: str, model: str) -> str:
        """إنشاء مفتاح تخزين مؤقت للطلب."""
        combined = f"{model}:{prompt}"
        return hashlib.sha256(combined.encode()).hexdigest()

    def get_cached(self, prompt: str, model: str) -> dict[str, Any] | None:
        """البحث في ذاكرة التخزين المؤقت."""
        cache_key = self._hash_prompt(prompt, model)
        session = self._Session()
        try:
            row = (
                session.query(ModelCacheModel)
                .filter(ModelCacheModel.cache_key == cache_key)
                .first()
            )
            if row:
                return {
                    "text": row.response,
                    "tokens": row.tokens,
                    "model": row.model,
                    "cached": True,
                }
            return None
        finally:
            session.close()

    def set_cached(self, prompt: str, model: str, response: str, tokens: int) -> None:
        """تخزين استجابة في ذاكرة التخزين المؤقت."""
        cache_key = self._hash_prompt(prompt, model)
        session = self._Session()
        try:
            existing = (
                session.query(ModelCacheModel)
                .filter(ModelCacheModel.cache_key == cache_key)
                .first()
            )
            if existing:
                return  # لا نعيد الكتابة
            row = ModelCacheModel(
                cache_key=cache_key,
                prompt_hash=hashlib.sha256(prompt.encode()).hexdigest(),
                model=model,
                response=response,
                tokens=tokens,
            )
            session.add(row)
            session.commit()
        finally:
            session.close()

    def compute_cost(self, model: str, input_tokens: int, output_tokens: int) -> float:
        """حساب التكلفة الحقيقية."""
        pricing = self.PRICING.get(model, {"input": 0.0, "output": 0.0})
        cost = (input_tokens / 1000) * pricing["input"] + (output_tokens / 1000) * pricing["output"]
        # يُقرَّبُ إلى مقياسِ عمودِ الكلفةِ لا إلى رقمٍ منسوخٍ (W-036 · Q-42 (أ)):
        # كانَ `round(cost, 6)` يُصفِّرُ ما دونَ `5e-7`، وأرخصُ رمزٍ في الجدولِ
        # `8e-7` — فحدُّ الحسابِ كانَ يلتقي حدَّ العمودِ في إضاعةِ الكسرِ مرّتَين.
        return round(cost, COST_SCALE)

    def log_cost(
        self,
        invocation_id: str,
        model: str,
        tokens: int,
        cost_usd: float,
        latency_ms: int,
        source: str,
    ) -> None:
        """تسجيل التكلفة دائمًا في DB."""
        session = self._Session()
        try:
            row = CostLogModel(
                invocation_id=invocation_id,
                model=model,
                tokens=tokens,
                cost_usd=_money_from_provider_float(cost_usd),
                latency_ms=latency_ms,
                source=source,
            )
            session.add(row)
            session.commit()
        finally:
            session.close()

    def cost_rows(self) -> list[dict[str, Any]]:
        """كلُّ قيدٍ في سجلِّ التكلفةِ الدائمِ — صفوفٌ لا ملخَّصٌ (W-033).

        ## لماذا صفوفٌ وقد وُجِدَ `get_cost_summary`

        حُسِمَ **Q-39 (ج)**: «الدائمُ سجلًّا · ويُكتَبُ فيه في مسارِ النداءِ، والملخَّصُ
        المتطايرُ يُعادُ بناؤُه فوقَه لا يُنافِسُه». ولنقطةِ `GET /v1/cost/summary`
        شكلُ خرجٍ **منشورٌ** يختلفُ عن شكلِ `get_cost_summary` (‏`invocations` ·
        `total_tokens` · `total_cost` مقابلَ `count` · `tokens` · `cost`)، وحذفُ
        مفتاحٍ منشورٍ عقدٌ مع مُستهلِكيه لا حكمُ عاملٍ. فتُقرأُ الصفوفُ مرّةً
        ويُعادُ بناءُ **كلِّ** شكلٍ فوقَها، فيبقى مصدرُ الحقيقةِ واحدًا والشكلانِ
        اثنَينِ — وهذا هو معنى «يُعادُ بناؤُه فوقَه».

        والكلفةُ تُعادُ `float` هنا لأنَّ عقدَ النقطةِ العامّةِ عائمٌ، وتحويلُ نوعِ
        الردِّ العامِّ مُقيَّدٌ سؤالًا مستقلًّا (**Q-29**) لا يُخترَعُ جوابُه هنا.
        والقيمةُ في القاعدةِ `NUMERIC(20,4)` كما هي.
        """
        session = self._Session()
        try:
            rows = session.query(CostLogModel).order_by(CostLogModel.id).all()
            return [
                {
                    "invocation_id": r.invocation_id,
                    "model": r.model,
                    "tokens": r.tokens or 0,
                    "cost_usd": float(r.cost_usd),
                    "latency_ms": r.latency_ms or 0,
                    "source": r.source,
                    "created_at": r.created_at.isoformat() if r.created_at else None,
                }
                for r in rows
            ]
        finally:
            session.close()

    def get_cost_summary(self) -> dict[str, Any]:
        """ملخص التكلفة التراكمي."""
        session = self._Session()
        try:
            rows = session.query(CostLogModel).all()
            total_cost = sum(float(r.cost_usd) for r in rows)
            total_tokens = sum(r.tokens for r in rows)
            total_invocations = len(rows)
            by_model: dict[str, dict] = {}
            for r in rows:
                if r.model not in by_model:
                    by_model[r.model] = {"cost": 0.0, "tokens": 0, "count": 0}
                by_model[r.model]["cost"] += float(r.cost_usd)
                by_model[r.model]["tokens"] += r.tokens
                by_model[r.model]["count"] += 1
            return {
                # `W-036`: كانَ `round(total_cost, 6)` هنا **بوّابةً رابعةً** لم
                # تُصلِحْها الهجرةُ ولا العقدُ: الصفُّ يُخزَّنُ بثمانِ منازلَ
                # صحيحةً، ثمَّ يُقرَّبُ في **مسارِ القراءةِ** فتقولُ هذه الواجهةُ
                # `1e-06` عن مالٍ مقدارُه `8e-07`. وبانَ ذلكَ بالقياسِ لا
                # بالمراجعةِ: فحصٌ يُقارِنُ `/v1/cost/summary` بـ
                # `/v1/models/cost-summary` احمرَّ بالرقمَينِ المختلفَينِ.
                # **فالتقريبُ يُشتقُّ الآنَ من `COST_SCALE` لا من رقمٍ مكتوبٍ**،
                # فتصيرُ الواجهتانِ قراءتَينِ لحقيقةٍ واحدةٍ كما يُلزِمُ حسمُ
                # Q-39 (ج). ونوعُ الحقلِ باقٍ `float` كما نُشِرَ — تبديلُه
                # عقدٌ مع مُستهلِكيه ومسألتُه **Q-29** المفتوحةُ لا حكمُ عاملٍ.
                "total_cost_usd": round(total_cost, COST_SCALE),
                "total_tokens": total_tokens,
                "total_invocations": total_invocations,
                "by_model": by_model,
            }
        finally:
            session.close()

    def invoke_with_cache(
        self, prompt: str, model: str, max_tokens: int, invoke_fn=None
    ) -> dict[str, Any]:
        """استدعاء نموذج مع caching."""
        # 1. فحص الذاكرة المؤقتة
        cached = self.get_cached(prompt, model)
        if cached:
            return {
                **cached,
                "latency_ms": 0,
                "cost_usd": 0.0,
                "source": "cache",
            }

        # 2. استدعاء النموذج
        start = time.monotonic()
        if invoke_fn:
            text, tokens = invoke_fn(prompt, model, max_tokens)
        else:
            # fallback محلي حقيقي
            text = f"[local-model] استجابة محلية للطلب: {prompt[:100]}..."
            tokens = len(text.split())
        latency = int((time.monotonic() - start) * 1000)

        # 3. حساب التكلفة
        input_tokens = len(prompt.split())
        cost = self.compute_cost(model, input_tokens, tokens)

        # 4. تسجيل في ذاكرة التخزين المؤقت
        self.set_cached(prompt, model, text, tokens)

        # 5. تسجيل التكلفة
        invocation_id = f"inv-{uuid.uuid4()}"
        source = "local" if model in ("local-fallback", "local-model") else "external"
        self.log_cost(invocation_id, model, tokens, cost, latency, source)

        return {
            "text": text,
            "tokens": tokens,
            "model": model,
            "latency_ms": latency,
            "cost_usd": cost,
            "source": source,
            "invocation_id": invocation_id,
            "cached": False,
        }

    def benchmark_models(
        self, prompts: list[str], models: list[str], invoke_fn=None
    ) -> dict[str, Any]:
        """مقارنة أداء النماذج."""
        results: dict[str, list] = {}
        for model in models:
            results[model] = []
            for prompt in prompts:
                start = time.monotonic()
                resp = self.invoke_with_cache(prompt, model, 256, invoke_fn)
                time.monotonic() - start
                results[model].append(
                    {
                        "latency_ms": resp["latency_ms"],
                        "tokens": resp["tokens"],
                        "cost_usd": resp["cost_usd"],
                        "cached": resp["cached"],
                    }
                )

        # حساب المتوسطات
        summary: dict[str, dict] = {}
        for model, runs in results.items():
            summary[model] = {
                "avg_latency_ms": sum(r["latency_ms"] for r in runs) / max(len(runs), 1),
                "avg_tokens": sum(r["tokens"] for r in runs) / max(len(runs), 1),
                "total_cost_usd": sum(r["cost_usd"] for r in runs),
                "cache_hits": sum(1 for r in runs if r["cached"]),
                "run_count": len(runs),
            }
        return {"results": summary, "raw": results}


# Singleton
_layer: ModelLayer | None = None


def get_model_layer() -> ModelLayer:
    global _layer
    if _layer is None:
        _layer = ModelLayer()
    return _layer
