"""
AMOS-Federation Model Gateway Service
الهدف: توجيه طلبات النماذج إلى مزود خارجي (Claude) مع fallback محلي حتمي + تتبع التكلفة + Shadow Testing
النطاق: خدمة model-gateway على المنفذ 8004
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
"""

import time
import uuid
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from amos_federation.common.auth import require_auth
from amos_federation.common.config import settings
from amos_federation.common.money import COST_SCALE
from amos_federation.common.registry import SERVICES
from amos_federation.common.service import create_service_app
from amos_federation.services.executive_core.fidelity import ExecutionFidelity
from amos_federation.services.executive_core.repository import TaskNotFoundError
from amos_federation.services.executive_core.subsystem_boundary import (
    ActivityKind,
    SubsystemRefusedError,
    get_subsystem_boundary,
)
from amos_federation.services.model_gateway.model_layer import get_model_layer
from amos_federation.services.model_gateway.shadow import (
    InMemoryShadowStore,
    _alpha_response,
    _beta_response,
)

router = APIRouter(prefix="/v1", tags=["model-gateway"])

# Cost tracking: تكلفة التقديم بالدولار لكل ألف رمز
#
# ## جدولانِ مُقَرَّانِ وفرقُهما مُقيَّدٌ — Q-42 · الشقُّ الأوّلُ · (ج) · W-036
#
# هذا جدولُ **مسارِ النداءِ** — الطريقُ الذي يكتبُ قيدَ المالِ في `model_cost_log`.
# وفي الخدمةِ جدولٌ ثانٍ `ModelLayer.PRICING` في `model_layer.py`. وقد سُئِلَ
# المالكُ: أيُوحَّدانِ أم يُقَرَّانِ؟ فأجابَ في Q-42 (ج) بتاريخ 2026-08-24:
# **«يُقَرُّ الجدولانِ ويُقيَّدُ الفرقُ»**. فبقيَ الجدولانِ، وصارَ الفرقُ **مقيسًا
# منشورًا محروسًا** لا مستورًا — لا مُلغًى ولا مُجمَّلًا.
#
# والفرقُ المقيسُ ثلاثةُ أوجهٍ (المصدر: `docs/audit/measurements/pricing_divergence.json`
# ويُعادُ توليدُه بـ`python tools/governance/pricing_divergence.py .`):
#
#   1. **شكلًا** — هذا الجدولُ سعرٌ واحدٌ مسطَّحٌ للنموذجِ، وجدولُ الطبقةِ سعرانِ
#      (`input` و`output`). فليسَ الخلافُ في رقمٍ بل في بنيةِ التسعيرِ.
#   2. **سعرًا** — في النماذجِ الثلاثةِ المشتركةِ يُطابِقُ السعرُ المسطَّحُ هنا
#      سعرَ **الخَرْجِ** في الطبقةِ ويبلغُ **خمسةَ أضعافِ** سعرِ الدَخلِ
#      (سونِت 0.015 مقابلَ 0.003 · أوپُس 0.075 مقابلَ 0.015). أي أنَّ رمزَ
#      الدَخلِ يُحاسَبُ في هذا الطريقِ بسعرِ الخَرْجِ — **فالقيدُ أعلى لا أدنى**،
#      وهو ميلٌ إلى تحميلِ الدولةِ لا إلى إخفاءِ نفقةٍ.
#   3. **تغطيةً** — `claude-haiku-3.5` مُسعَّرٌ بمالٍ حقيقيٍّ في الطبقةِ وغائبٌ عن
#      هذا الجدولِ، والقراءةُ أدناهُ `.get(model, 0.0)` فيُقيَّدُ **مجّانًا** لو
#      نُودِيَ من هذا الطريقِ. وهذا **الوجهُ الوحيدُ الذي يُنقِصُ** مالَ الدولةِ،
#      وهو مُعلَنٌ مقيسٌ محروسٌ — ولم يُسَدَّ بإضافةِ سطرٍ لأنَّ إضافةَ سعرٍ إلى
#      جدولٍ **قرارُ مالٍ** لا حكمُ عاملٍ، وقد أُقِرَّ الجدولانِ كما هما.
COST_PER_1K_TOKENS = {
    "local-fallback": 0.0,
    "alpha-local": 0.0,
    "beta-candidate": 0.0,
    "claude-sonnet-4": 0.015,
    "claude-opus-4": 0.075,
}

#: تصنيفُ إدامةِ **مخزنِ نتائجِ الظلِّ** — مُعلَنٌ في الشِفرةِ لا مُستنتَجٌ من قارئٍ (T3.6).
#: بقيَ متطايرًا بعدَ W-033: حسمُ Q-39 (ج) نصَّ على **المالِ** ولم ينُصَّ على الظلِّ،
#: والقياسُ على قرارٍ سياديٍّ اختراعٌ له. والاسمُ لم يُغيَّرْ لأنَّه **قيمةٌ منشورةٌ**
#: في خرجِ `GET /v1/shadow/stats`.
STORE_DURABILITY = "in_memory_volatile"

#: تصنيفُ إدامةِ **سجلِّ المالِ** — W-033 · حسمُ Q-39 (ج).
#: كانَ سجلُّ التكلفةِ قائمةً في ذاكرةِ العمليّةِ (`_cost_log`) يقرأُ منها
#: `GET /v1/cost/summary`، وفي الخدمةِ نفسِها ملخَّصٌ ثانٍ دائمٌ
#: (`GET /v1/models/cost-summary`) — رقمانِ للمالِ في واجهةٍ واحدةٍ أحدُهما يتبخّر.
#: فحُسِمَ: «الدائمُ سجلًّا · ويُكتَبُ فيه في مسارِ النداءِ · والملخَّصُ المتطايرُ
#: يُعادُ بناؤُه فوقَه لا يُنافِسُه». فحُذِفَت القائمةُ، وصارَ `POST /v1/models/invoke`
#: يكتبُ في جدولِ `model_cost_log` **في مسارِ النداءِ نفسِه**، و`GET /v1/cost/summary`
#: يُعادُ بناؤُه فوقَ الجدولِ بشكلِ خرجِه المنشورِ بلا حذفِ مفتاحٍ.
COST_STORE_DURABILITY = "durable_record"

#: النقطةُ التي تُعلِنُ نفسَها مصدرَ الحقيقةِ للمالِ — مكتوبةٌ مرّةً وتُقرأُ في الخرجِ.
COST_RECORD_ENDPOINT = "/v1/models/cost-summary"

_shadow_store = InMemoryShadowStore()


class ModelInvokeRequest(BaseModel):
    """طلب استدعاء نموذج."""

    prompt: str = Field(min_length=1, max_length=50000)
    model: str | None = None
    max_tokens: int = Field(default=1024, ge=1, le=8192)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    #: المهمّة التنفيذية التي يخدمها هذا الاستدعاء — إن وُجدت، تُتحقَّق من المستودع القانوني.
    task_id: str | None = None


class ModelInvokeResponse(BaseModel):
    """استجابة استدعاء نموذج — تُعلن صدق مخرَجها وإذنه ونسبه."""

    text: str
    model_used: str
    tokens_used: int
    latency_ms: int
    source: str  # "external" أو "local_fallback"
    cost_usd: float = 0.0
    execution_fidelity: str = ExecutionFidelity.REAL.value
    fidelity_reason: str | None = None
    task_id: str | None = None
    activity_id: str | None = None
    authority_decision: str | None = None


class ModelRouteResponse(BaseModel):
    """استجابة توجيه نموذج."""

    recommended_model: str
    available_models: list[str]
    fallback_chain: list[str]


def _local_fallback(prompt: str, max_tokens: int) -> tuple[str, int]:
    """مولد حتمي محلي عند غياب مفتاح Claude API."""
    prompt_preview = prompt[:200]
    text = (
        f'[local-fallback] تم استلام الطلب: "{prompt_preview}...". '
        f"لا يتوفر مفتاح Claude API — هذه استجابة محلية حتمية للاختبارات."
    )
    tokens = len(text.split())
    return text, tokens


async def _invoke_claude(prompt: str, model: str, max_tokens: int) -> tuple[str, int]:
    """استدعاء Claude API عند توفر المفتاح."""
    import httpx

    api_key = settings.claude_api_key
    if not api_key:
        raise ValueError("لا يتوفر مفتاح Claude API")

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": model,
                "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": prompt}],
            },
        )
        response.raise_for_status()
        data = response.json()
        text = data["content"][0]["text"]
        tokens = data.get("usage", {}).get("output_tokens", len(text.split()))
        return text, tokens


@router.post("/models/route", response_model=ModelRouteResponse)
async def route_model(
    _: Annotated[dict[str, object], Depends(require_auth)],
) -> ModelRouteResponse:
    """توجيه النموذج الموصى به مع سلسلة fallback."""
    default = settings.default_model
    available = [default] if settings.claude_api_key else ["local-fallback"]
    fallback = [default, "local-fallback"] if settings.claude_api_key else ["local-fallback"]
    return ModelRouteResponse(
        recommended_model=available[0],
        available_models=available,
        fallback_chain=fallback,
    )


@router.post("/models/invoke", response_model=ModelInvokeResponse)
async def invoke_model(
    request: ModelInvokeRequest,
    _: Annotated[dict[str, object], Depends(require_auth)],
) -> ModelInvokeResponse:
    """استدعاء نموذج تحت سلطة النواة، مع إعلان صريح لصدق المخرَج.

    ثلاثة فروق عن ما قبل R2:

    1. الاستدعاء يمرّ بحدّ النواة (`SubsystemBoundary`): إذن دستوري fail-closed،
       ثم قيد تدقيق وحدث دائم. البوابة لم تبق سلطة مستقلة عن البوابة السيادية.
    2. إن ذُكرت `task_id` فهي تُقرأ من المستودع القانوني؛ معرّف وهمي يُرد بـ404.
       ولا تُغيَّر حالة المهمّة هنا بحال — الأثر يُرفَق ولا يُحرّك دورة الحياة.
    3. الفشل لا يُبتلع: كان `except Exception` يُرجع نصًّا محليًّا كأنه نجاح.
       الآن يُعلَن `UNAVAILABLE` مع سبب مُسمّى — لا `SIMULATION` تُغطّي انقطاعًا.
    """
    model = request.model or settings.default_model
    boundary = get_subsystem_boundary()

    start = time.monotonic()
    source = "external"
    fidelity = ExecutionFidelity.REAL
    fidelity_reason: str | None = None
    try:
        if not settings.claude_api_key:
            raise ValueError("لا يتوفر مفتاح Claude API")
        text, tokens = await _invoke_claude(request.prompt, model, request.max_tokens)
    except Exception as exc:  # الانقطاع يُسمّى ولا يُقدَّم كأنه استدعاء ناجح
        text, tokens = _local_fallback(request.prompt, request.max_tokens)
        source = "local_fallback"
        model = "local-fallback"
        fidelity = ExecutionFidelity.UNAVAILABLE
        fidelity_reason = (
            "claude_api_key_missing"
            if not settings.claude_api_key
            else f"external_invocation_failed:{type(exc).__name__}"
        )
    latency = int((time.monotonic() - start) * 1000)
    # يُقرَّبُ إلى مقياسِ عمودِ الكلفةِ (`COST_SCALE` = 8) لا إلى `6` منسوخةٍ
    # (W-036 · Q-42 (أ)): تقريبٌ أضيقُ من العمودِ يُضيعُ الكسرَ قبلَ أن يبلغَه،
    # فيصيرُ توسيعُ العمودِ حلًّا لا يُحَلُّ به شيءٌ.
    cost = round(tokens * COST_PER_1K_TOKENS.get(model, 0.0) / 1000, COST_SCALE)
    # W-033 · حسمُ Q-39 (ج): الكتابةُ **في مسارِ النداءِ** وفي السجلِّ الدائمِ نفسِه،
    # لا في قائمةِ ذاكرةٍ تُنافِسُه. وموضعُ الكتابةِ **حيثُ أُنفِقَ المالُ**: قبلَ بوّابةِ
    # الصلاحيةِ أدناه، لأنَّ الرموزَ استُهلِكَت فعلًا حتى لو رُفِضَ نسبُ النشاطِ —
    # فقيدُ الإنفاقِ يبقى ولو رُدَّ الطلبُ بـ403، وهذا هو الترتيبُ الذي كانَ قائمًا
    # قبلَ الإدامةِ فلم يُغيَّرْ ترتيبٌ معَ تغييرِ الموضعِ.
    invocation_id = f"inv-{uuid.uuid4()}"
    get_model_layer().log_cost(
        invocation_id=invocation_id,
        model=model,
        tokens=tokens,
        cost_usd=cost,
        latency_ms=latency,
        source=source,
    )
    try:
        activity = boundary.authorized_activity(
            ActivityKind.MODEL_INVOCATION,
            f"model:{model}",
            fidelity,
            {
                "tokens_used": tokens,
                "cost_usd": cost,
                "latency_ms": latency,
                "source": source,
                "fidelity_reason": fidelity_reason,
            },
            task_id=request.task_id,
            context={"model": model, "max_tokens": request.max_tokens},
        )
    except TaskNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"لا يوجد مهمّة قانونية بهذا المعرّف، فلا نسب للاستدعاء: {exc}",
        ) from exc
    except SubsystemRefusedError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(exc),
        ) from exc

    return ModelInvokeResponse(
        text=text,
        model_used=model,
        tokens_used=tokens,
        latency_ms=latency,
        source=source,
        cost_usd=cost,
        execution_fidelity=fidelity.value,
        fidelity_reason=fidelity_reason,
        task_id=request.task_id,
        activity_id=activity.activity_id,
        authority_decision=activity.authority["decision"],
    )


class ShadowTestRequest(BaseModel):
    """طلب اختبار shadow بين نموذجين."""

    prompt: str = Field(min_length=1, max_length=50000)


@router.post("/shadow/test", response_model=dict, status_code=status.HTTP_201_CREATED)
async def run_shadow_test(
    request: ShadowTestRequest,
    _: Annotated[dict[str, object], Depends(require_auth)],
) -> dict[str, Any]:
    """تشغيل اختبار shadow: توجيه الطلب لكلا النموذجين (ألفا + بيتا) ومقارنة النتائج."""
    alpha = _alpha_response(request.prompt)
    beta = _beta_response(request.prompt)
    return _shadow_store.record({"prompt": request.prompt, "alpha": alpha, "beta": beta})


@router.get("/shadow/results", response_model=list[dict])
async def get_shadow_results(
    _: Annotated[dict[str, object], Depends(require_auth)],
    limit: int = Query(default=50, ge=1, le=200),
) -> list[dict[str, Any]]:
    """عرض نتائج اختبارات shadow."""
    return _shadow_store.list_all(limit=limit)


@router.get("/shadow/results/{shadow_id}", response_model=dict)
async def get_shadow_result(
    shadow_id: str,
    _: Annotated[dict[str, object], Depends(require_auth)],
) -> dict[str, Any]:
    """إرجاع نتيجة shadow بالمعرّف."""
    result = _shadow_store.get(shadow_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="نتيجة shadow غير موجودة")
    return result


@router.get("/shadow/stats", response_model=dict)
async def shadow_stats(
    _: Annotated[dict[str, object], Depends(require_auth)],
) -> dict[str, Any]:
    """ملخص إحصائيات shadow testing — يُعلن تطايرَ مصدرِه."""
    # مفتاحٌ مُضافٌ لا مُبدَّلٌ: لا يُحذَفُ مفتاحٌ ولا يُغيَّرُ رقمٌ، فالإعلانُ زيادةٌ
    # في الصدقِ لا تغييرٌ في العقد (T3.6 · W-029).
    return {**_shadow_store.summary(), "store_type": STORE_DURABILITY}


@router.get("/cost/summary", response_model=dict)
async def cost_summary(
    _: Annotated[dict[str, object], Depends(require_auth)],
) -> dict[str, Any]:
    """ملخص التكاليف لكل النماذج — **يُعادُ بناؤُه فوقَ السجلِّ الدائمِ** (W-033 · Q-39 ج).

    كانَ يُحسَبُ من `_cost_log` في الذاكرةِ فيصفرُ عندَ إعادةِ التشغيلِ، وفي الخدمةِ
    نفسِها ملخَّصٌ ثانٍ دائمٌ — رقمانِ للمالِ أحدُهما يتبخّر. فحُسِمَ أنَّ الدائمَ هو
    السجلُّ، فصارَ هذا الملخَّصُ **قراءةً على الجدولِ نفسِه** لا مخزنًا منافسًا.

    **ولم يُحذَفْ مفتاحٌ ولم يُبدَّلْ شكلٌ:** `total_invocations` و`total_cost_usd`
    و`by_model{invocations,total_tokens,total_cost}` كما كانت، لأنَّ حذفَ مفتاحٍ
    منشورٍ عقدٌ مع مُستهلِكيه. والذي تغيَّرَ **قيمةُ** `store_type`: صارت
    `durable_record` بدلَ `in_memory_volatile` — إعلانٌ صارَ صادقًا لا مفتاحٌ جديد.
    """
    rows = get_model_layer().cost_rows()
    total_cost = sum(r["cost_usd"] for r in rows)
    by_model: dict[str, dict[str, float]] = {}
    for entry in rows:
        m = entry["model"]
        if m not in by_model:
            by_model[m] = {"invocations": 0, "total_tokens": 0, "total_cost": 0.0}
        by_model[m]["invocations"] += 1
        by_model[m]["total_tokens"] += entry["tokens"]
        by_model[m]["total_cost"] += entry["cost_usd"]
    # W-036 · Q-42 (أ): يُقرَّبُ الملخَّصُ إلى **مقياسِ الصفوفِ نفسِه**. وكانَ
    # يُقرَّبُ إلى `6` فوقَ صفوفٍ صارَت تحملُ ثمانِ منازلَ — أي ملخَّصٌ يُنقِضُ
    # الجدولَ الذي بُنِيَ فوقَه، وهو عينُ ما حُسِمَ في Q-39 (ج) أن لا يكون:
    # «الملخَّصُ يُعادُ بناؤُه فوقَه لا يُنافِسُه». والشكلُ لم يتغيَّرْ ولا مفتاحٌ:
    # القيمةُ صارت أدقَّ لا أكثرَ.
    for m in by_model:
        by_model[m]["total_cost"] = round(by_model[m]["total_cost"], COST_SCALE)
    return {
        "total_invocations": len(rows),
        "total_cost_usd": round(total_cost, COST_SCALE),
        "by_model": by_model,
        # المفتاحانِ باقيانِ بلا تبديلٍ، وقيمةُ الأوّلِ صارت صادقةً بعدَ W-033،
        # والثاني يُشيرُ إلى **نفسِ** الجدولِ الذي بُنِيَ فوقَه هذا الملخَّصُ.
        "store_type": COST_STORE_DURABILITY,
        "persistent_source": COST_RECORD_ENDPOINT,
    }


# === Model Layer endpoints ===


@router.get("/models/cost-summary", response_model=dict)
async def get_persistent_cost_summary(
    _: Annotated[dict[str, object], Depends(require_auth)],
) -> dict[str, Any]:
    """ملخص التكلفة الدائم من DB."""
    from amos_federation.services.model_gateway.model_layer import get_model_layer

    return get_model_layer().get_cost_summary()


@router.post("/models/invoke-cached", response_model=dict)
async def invoke_model_cached(
    request: ModelInvokeRequest,
    _: Annotated[dict[str, object], Depends(require_auth)],
) -> dict[str, Any]:
    """استدعاء نموذج مع caching و cost tracking دائم."""
    from amos_federation.services.model_gateway.model_layer import get_model_layer

    model = request.model or settings.default_model or "local-fallback"
    return get_model_layer().invoke_with_cache(request.prompt, model, request.max_tokens)


@router.post("/models/benchmark", response_model=dict)
async def benchmark_models(
    _: Annotated[dict[str, object], Depends(require_auth)],
    prompts: Annotated[list[str], Query()] = ...,  # type: ignore[assignment]
    models: Annotated[list[str], Query()] = None,
) -> dict[str, Any]:
    """مقارنة أداء النماذج."""
    if models is None:
        models = ["local-fallback"]
    from amos_federation.services.model_gateway.model_layer import get_model_layer

    return get_model_layer().benchmark_models(prompts, models)


_service = SERVICES["model-gateway"]
app = create_service_app(
    _service["name"], _service["port"], "توجيه واستدعاء النماذج + Shadow Testing", [router]
)
