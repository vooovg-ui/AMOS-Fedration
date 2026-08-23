"""
AMOS-Federation Kill Switch + Promotion Gates + Canary Controller
الهدف: مفتاح إيقاف متعدد المستويات + بوابات ترقية + Canary deployment
النطاق: governance (canary)
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
"""

import uuid
from datetime import UTC, datetime
from typing import Any

# === Kill Switch ===

KILL_SWITCH_LEVELS = ["normal", "alert", "degraded", "halt"]
# T4-DURABILITY: WIRED_DURABLE — **حُسِمَ في Q-39 (أ) بقرارِ المالكِ 2026-08-23**:
# «مفتاحُ الإيقافِ والترقياتُ أوّلًا». وكانَ المستوى قاموسًا في ذاكرةِ العمليّةِ، فقِيسَ
# في W-030 أنَّ نظامًا أُوقِفَ بمستوى `halt` يعودُ `normal` بإعادةِ التشغيلِ — أي أنَّ
# الدولةَ تُلغي إيقافَ نفسِها، وأنَّ القيمةَ **لكلِّ عمليّةِ عاملٍ على حِدَة** فلا تُقرأُ
# حالةٌ واحدةٌ للدولة. فصارَ المستوى صفًّا في جدولِ `system_state` (W-031).
#
# وأثرُ ذلكَ على عقدِ التشغيلِ مُعلَنٌ لا مسكوتٌ عنه: **إعادةُ التشغيلِ لا تُطفِئُ
# الإيقافَ**؛ فمن أوقفَ النظامَ لطارئٍ لا يرفعُه إقلاعٌ، بل رفعٌ صريحٌ عبرَ
# `reset_kill_switch`. وهذا هو نفسُ ما كانَ يُمنَعُ على العاملِ في W-029 لأنَّه تغييرُ
# عقدٍ لا إصلاحُ عيبٍ — فأذِنَ به المالكُ نصًّا، فنُفِّذَ.


_SYSTEM_STATE_STORE: Any = None


def _system_state_store() -> Any:
    """مخزنُ حالةِ الدولةِ الدائمُ — يُستورَدُ عندَ الحاجةِ لا عندَ تحميلِ الوحدة.

    الاستيرادُ المتأخّرُ مقصودٌ: `common.persistent` يُهيِّئُ قاعدةَ البياناتِ عندَ
    استيرادِه، فلا يُجبَرُ من يستوردُ هذه الوحدةَ لقراءةِ ثابتٍ على تهيئةِ قاعدة.
    """
    from amos_federation.common.persistent import PersistentSystemStateStore

    global _SYSTEM_STATE_STORE
    if _SYSTEM_STATE_STORE is None:
        _SYSTEM_STATE_STORE = PersistentSystemStateStore()
    return _SYSTEM_STATE_STORE


def get_system_status() -> dict[str, Any]:
    """حالة النظام الحالية — تُقرأُ من الجدولِ الدائمِ في كلِّ نداء."""
    return _system_state_store().get()


def activate_kill_switch(level: str, reason: str, activated_by: str) -> dict[str, Any]:
    """تفعيل مفتاح الإيقاف."""
    if level not in KILL_SWITCH_LEVELS:
        raise ValueError(f"مستوى غير صالح: {level}")
    state = _system_state_store().set_level(level, reason, activated_by)
    # نشر حدث
    from amos_federation.common.event_bus import get_event_bus

    get_event_bus().publish(
        "amos_federation.policy.checked",
        {
            "policy_name": "kill_switch",
            "allowed": level == "normal",
            "violations": [reason] if level != "normal" else [],
            "level": level,
            "activated_by": activated_by,
        },
    )
    return state


def reset_kill_switch() -> dict[str, Any]:
    """إعادة ضبط مفتاح الإيقاف — الرفعُ فعلٌ صريحٌ لا نتيجةُ إقلاع."""
    return _system_state_store().reset()


def is_system_halted() -> bool:
    """هل النظام متوقف؟"""
    return get_system_status()["level"] == "halt"


def is_execution_blocked(tool: str | None = None) -> bool:
    """هل التنفيذ محجوب؟ في halt كل شيء محجوب. في degraded الأدوات الخطيرة محجوبة."""
    level = get_system_status()["level"]
    if level == "halt":
        return True
    return bool(level == "degraded" and tool in ["python_execute", "sql_query", "http_request"])


def enforce_kill_switch(tool: str, role: str = "user") -> dict[str, Any]:
    """تطبيق Kill Switch على تنفيذ أداة. يرمي HTTPException إذا محجوب."""
    from fastapi import HTTPException

    state = get_system_status()
    level = state["level"]
    if level == "halt":
        raise HTTPException(
            status_code=503,
            detail={
                "error": "system_halted",
                "message": "النظام متوقف — Kill Switch مفعّل بمستوى halt",
                "level": level,
                "reason": state["reason"],
            },
        )
    if level == "degraded" and tool in ["python_execute", "sql_query", "http_request"]:
        raise HTTPException(
            status_code=503,
            detail={
                "error": "system_degraded",
                "message": f"النظام في وضع متدهور — الأداة '{tool}' محجوبة",
                "level": level,
                "reason": state["reason"],
            },
        )
    return {"allowed": True, "level": level}


# === Promotion Gates ===

PROMOTION_GATES = [
    "evaluation",
    "shadow",
    "canary",
    "human_approval",
    "activation",
]

# T4-DURABILITY: WIRED_DURABLE — **حُسِمَ في Q-39 (أ) بقرارِ المالكِ 2026-08-23**.
# قِيسَ في W-029/W-030: **موافقةُ إنسانٍ على ترقيةٍ** (`human_approval`) تزولُ بإعادةِ
# التشغيلِ ولا يبقى لها أثرٌ يُقاس. فصارت الطلباتُ وبوّاباتُها صفوفًا في جدولِ
# `promotions` (W-031)، فإذنُ الإنسانِ يبقى بعدَ الإقلاعِ ويُراجَع.


_PROMOTION_STORE: Any = None


def _promotion_store() -> Any:
    """مخزنُ طلباتِ الترقيةِ الدائمُ — استيرادٌ متأخّرٌ لنفسِ سببِ حالةِ الدولة."""
    from amos_federation.common.persistent import PersistentPromotionStore

    global _PROMOTION_STORE
    if _PROMOTION_STORE is None:
        _PROMOTION_STORE = PersistentPromotionStore()
    return _PROMOTION_STORE


def create_promotion(model_id: str) -> dict[str, Any]:
    """إنشاء طلب ترقية نموذج."""
    promotion = {
        "promotion_id": f"promo-{uuid.uuid4()}",
        "model_id": model_id,
        "gates": {gate: {"status": "pending", "checked_at": None} for gate in PROMOTION_GATES},
        "status": "in_progress",
        "created_at": datetime.now(UTC).isoformat(),
        "updated_at": datetime.now(UTC).isoformat(),
    }
    _promotion_store().create(promotion)
    return promotion


def check_gate(promotion_id: str, gate_name: str, passed: bool, notes: str = "") -> dict[str, Any]:
    """فحص بوابة ترقية."""
    store = _promotion_store()
    promo = store.get(promotion_id)
    if promo is None:
        raise ValueError(f"ترقية غير موجودة: {promotion_id}")
    gates = dict(promo["gates"])
    if gate_name not in gates:
        raise ValueError(f"بوابة غير صالحة: {gate_name}")
    gates[gate_name] = {
        "status": "passed" if passed else "failed",
        "checked_at": datetime.now(UTC).isoformat(),
        "notes": notes,
    }
    status = promo["status"]
    # إذا فشلت بوابة، تتوقف الترقية
    if not passed:
        status = "failed"
    # إذا اجتازت كل البوابات
    elif all(g["status"] == "passed" for g in gates.values()):
        status = "promoted"
    updated = store.save_gates(promotion_id, gates, status, datetime.now(UTC).isoformat())
    if updated is None:
        raise ValueError(f"ترقية غير موجودة: {promotion_id}")
    return updated


def get_promotion(promotion_id: str) -> dict[str, Any] | None:
    """إرجاع طلب ترقية — من الجدولِ الدائمِ، فينجو من إعادةِ التشغيل."""
    return _promotion_store().get(promotion_id)


def list_promotions(limit: int = 50) -> list[dict[str, Any]]:
    """عرض طلبات الترقية."""
    return _promotion_store().list_all(limit)


# === Canary Controller ===

# T3.6-DURABILITY: WIRED_VOLATILE — نشرُ الـcanary ونسبةُ مرورِه في قائمةِ ذاكرةٍ:
# قِيسَ في W-029 أنَّ إعادةَ التشغيلِ تُنسي الدولةَ أنَّ نشرًا تدريجيًّا **قائمٌ الآن**.
# الإدامةُ عملُ T4/E4 · Q-39.
_canary_deployments: list[dict[str, Any]] = []


def create_canary(model_id: str, traffic_percentage: int = 5) -> dict[str, Any]:
    """إنشاء Canary deployment لنموذج."""
    if traffic_percentage < 1 or traffic_percentage > 100:
        raise ValueError("نسبة المرور يجب أن تكون 1-100")
    deployment = {
        "canary_id": f"canary-{uuid.uuid4()}",
        "model_id": model_id,
        "traffic_percentage": traffic_percentage,
        "status": "active",
        "metrics": {
            "requests": 0,
            "errors": 0,
            "avg_latency_ms": 0,
            "quality_score": 0.0,
        },
        "created_at": datetime.now(UTC).isoformat(),
        "updated_at": datetime.now(UTC).isoformat(),
    }
    _canary_deployments.append(deployment)
    return deployment


def update_canary_metrics(
    canary_id: str, requests: int, errors: int, avg_latency: int, quality: float
) -> dict[str, Any]:
    """تحديث مقاييس Canary."""
    for d in _canary_deployments:
        if d["canary_id"] == canary_id:
            d["metrics"] = {
                "requests": requests,
                "errors": errors,
                "avg_latency_ms": avg_latency,
                "quality_score": quality,
            }
            d["updated_at"] = datetime.now(UTC).isoformat()
            # فحص شروط التراجع
            error_rate = errors / requests if requests > 0 else 0
            if error_rate > 0.1 or quality < 0.5:
                d["status"] = "rolled_back"
            return d.copy()
    raise ValueError(f"Canary غير موجود: {canary_id}")


def rollback_canary(canary_id: str) -> dict[str, Any]:
    """تراجع عن Canary deployment."""
    for d in _canary_deployments:
        if d["canary_id"] == canary_id:
            d["status"] = "rolled_back"
            d["updated_at"] = datetime.now(UTC).isoformat()
            return d.copy()
    raise ValueError(f"Canary غير موجود: {canary_id}")


def get_canary(canary_id: str) -> dict[str, Any] | None:
    """إرجاع Canary."""
    for d in _canary_deployments:
        if d["canary_id"] == canary_id:
            return d.copy()
    return None


def list_canaries(limit: int = 50) -> list[dict[str, Any]]:
    """عرض Canary deployments."""
    return [d.copy() for d in _canary_deployments[:limit]]
