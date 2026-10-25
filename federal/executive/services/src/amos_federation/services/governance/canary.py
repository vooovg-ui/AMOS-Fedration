"""
AMOS-Federation Kill Switch + Promotion Gates + Canary Controller
الهدف: مفتاح إيقاف متعدد المستويات + بوابات ترقية + Canary deployment
النطاق: governance (canary)
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
تاريخ آخر تعديل: 2026-10-25 (W-675 — WI-114 السطحانِ 1 و3 يعبرانِ الحدَّ السياديّ)
"""

import uuid
from datetime import UTC, datetime
from typing import Any

from fastapi import HTTPException

from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    _core_sovereignty,
    compensator,
    declared_effect,
    operation_key,
)

# === عبورُ الحدِّ السياديِّ (WI-114 · A1(أ) · تصميمُ docs/audit/A1A_CANARY_CROSSING_DESIGN.md § 3.3) ===
#
# السطحانِ 1 و3 وحدَهما (التوجيهُ 23 § 2: «WI-114 السطحين 1 و3: الشفرة الآن»). والسطحانِ 2
# (`reset_kill_switch`) و4 (`check_gate` حينَ تنقلُ النتيجةُ إلى `promoted`) **خارجَ هذه الشِّفرة**
# حتّى يُنفَّذَ قرارُ D25-1 بشروطِه (أ)/(ب)/(ج).
#
#: فاعلُ العبورِ فرعٌ دستوريٌّ ثابتٌ في الوحدة (سابقةُ D1 في `national_registry.REGISTRY_ACTOR`
#: و`factories.FACTORY_ACTOR`) — لأنَّ الجسرَ لا يقبلُ إلّا `Branch` (`sovereignty_bridge._request`).
#: أمّا **مَن طلبَ** فيُحمَلُ في بياناتِ طلبِ العبورِ (`requested_by`) كما يُمرِّرُه المُنادي.
#: والحدُّ المُعلَنُ (DISC-139): § 3.3 يطلبُ الفاعلَ من `sub` الرمزِ لا من `activated_by` الجسم،
#: وذلك تعديلٌ في ملفَّي المسارِ وهما في مساراتِ WI-117 — فلم يُنفَّذ هنا، والمسارُ ما زالَ يُمرِّرُ
#: `activated_by` من الجسم.
CANARY_ACTOR = "EXECUTIVE"

#: رفعُ الزرِّ — ALLOW للفاعلِ التنفيذيِّ اليومَ (مسبارُ W-664 · وأُعيدَ قياسُه في W-675).
ACTION_ACTIVATE_KILL_SWITCH = "activate_kill_switch"
#: الخفضُ — فعلُ المعجمِ المحروسُ بـR008-3 (`human_approved` إلزاميّ). يُوجَّهُ إليه كلُّ
#: «تفعيلٍ» بمستوى أدنى من القائمِ (DISC-138)، فيرفضُه الحدُّ اليومَ إذ لا قناةَ لموافقةٍ بشريّةٍ
#: عبرَ الجسر (§ 3.2). والخفضُ المشروعُ طريقُه `reset_kill_switch` (السطحُ 2) لا التفعيل.
ACTION_LOWER_KILL_SWITCH = "lower_kill_switch"
#: طلبُ ترقيةٍ لا ترقية — فعلٌ حرٌّ ALLOW (مسبارُ W-675)؛ و`promote_model` يبقى للانتقالِ إلى
#: `promoted` وحدَه (السطحُ 4 · بعدَ D25-1).
ACTION_REQUEST_PROMOTION = "request_promotion"

KILL_SWITCH_SCOPE = "governance.kill_switch.activate"
PROMOTION_REQUEST_SCOPE = "governance.promotion.request"
SYSTEM_STATE_TARGET = "governance/system_state"

_CANARY_AUTHORIZER: ConstitutionalAuthorizer | None = None


def _canary_authorizer() -> ConstitutionalAuthorizer:
    """المُصرِّحُ بفاعلِ الوحدةِ المُسمّى — واحدٌ للوحدة."""
    global _CANARY_AUTHORIZER
    if _CANARY_AUTHORIZER is None:
        _CANARY_AUTHORIZER = ConstitutionalAuthorizer(actor=CANARY_ACTOR)
    return _CANARY_AUTHORIZER


class KillSwitchRefusedError(HTTPException):
    """رفضَ الحدُّ السياديُّ كتابةَ الزرِّ (`SovereigntyViolation`) — لم يُكتَب شيء ⇒ 403.

    صنفٌ مُسمًّى في الوحدةِ لأنَّ الجسرَ لا يُعيدُ تصديرَ صنفِ البوّابة. وهو `HTTPException`
    على سابقةِ `enforce_kill_switch` في الوحدةِ نفسِها (503)، فيُجيبُ المسارُ 403 بلا مسٍّ لملفِّ
    المسار — ومسارا `governance/main.py` و`control_console/main.py` في مساراتِ WI-117 لا WI-114.
    """

    def __init__(self, verb: str, explanation: str) -> None:
        self.verb = verb
        super().__init__(
            status_code=403,
            detail={
                "error": "sovereign_refusal",
                "action": verb,
                "message": f"«{verb}» مرفوضٌ عندَ الحدِّ السياديّ: {explanation}",
            },
        )


def reset_canary_authorizer() -> None:
    """أفرِغِ المُصرِّحَ المحفوظَ — للاختباراتِ التي تبدّلُ الفاعلَ أو موضعَ السجلّ."""
    global _CANARY_AUTHORIZER
    _CANARY_AUTHORIZER = None


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


def kill_switch_verb(current_level: str, requested_level: str) -> str:
    """فعلُ المعجمِ لطلبِ «تفعيل»: رفعٌ أو إبقاءٌ ⇒ `activate_kill_switch` · أدنى من القائمِ ⇒ خفض.

    `set_level` لا يقارنُ بالقائم (`canary.py` قبلَ W-675)، فقِيسَ في W-672 أنَّ رمزَ مواطنٍ
    يخفضُ `halt` إلى `normal` عبرَ مسارِ التفعيل (DISC-138). فالمقارنةُ هنا قبلَ الحدِّ لا بعدَه.
    """
    if KILL_SWITCH_LEVELS.index(requested_level) < KILL_SWITCH_LEVELS.index(current_level):
        return ACTION_LOWER_KILL_SWITCH
    return ACTION_ACTIVATE_KILL_SWITCH


def _guard_kill_switch(
    verb: str,
    target: str,
    nonce: str,
    effect: Any,
    apply: Any,
    restore: Any,
    activated_by: str,
    before: dict[str, Any],
    level: str,
) -> Any:
    """نداءُ الحدِّ لكتابةِ الزرِّ — مفصولٌ ليبقى الرفضُ المُترجَمُ في موضعٍ واحد."""
    return _canary_authorizer().guard_declared(
        verb,
        target,
        declared_effects=(effect,),
        applier=apply,
        # مُعرِّفُ الاستدعاءِ نفسُه: تكرارُ رفعِ الزرِّ مشروعٌ، فلا مفتاحَ طبيعيَّ يُعادُ عليه.
        operation_key=operation_key(KILL_SWITCH_SCOPE, nonce),
        compensators=(
            compensator(
                effect.signature,
                restore,
                "استعادةُ مستوى الزرِّ وسببِه وفاعلِه كما كانت قبلَ الكتابة",
            ),
        ),
        metadata={
            "requested_by": activated_by,
            "level_before": before["level"],
            "level_requested": level,
        },
    )


def activate_kill_switch(level: str, reason: str, activated_by: str) -> dict[str, Any]:
    """تفعيل مفتاح الإيقاف — عبرَ الحدِّ السياديِّ (WI-114 السطح 1).

    المستوى الأدنى من القائمِ يعبرُ بفعلِ الخفضِ فيرفضُه الحدُّ (`KillSwitchRefusedError` · 403)
    ولا يُكتَبُ شيء (DISC-138). و`activated_by` كما يُمرِّرُه المُنادي — والمسارُ اليومَ يُمرِّرُ حقلَ
    الجسمِ لا `sub` الرمز (DISC-139 · خارجَ مساراتِ WI-114).
    """
    if level not in KILL_SWITCH_LEVELS:
        raise ValueError(f"مستوى غير صالح: {level}")
    store = _system_state_store()
    before = store.get()
    verb = kill_switch_verb(before["level"], level)
    # مُعرِّفُ استدعاءٍ في الهدفِ (سابقةُ D3 في `national_registry._nonce`): تكرارُ رفعِ الزرِّ مشروعٌ،
    # ومعرِّفُ الإذنِ `EP-<العقد>-<الثانية>` — فبلا مُعرِّفٍ في الهدفِ يتصادمُ رفعانِ في ثانيةٍ واحدة.
    nonce = uuid.uuid4().hex
    target = f"{SYSTEM_STATE_TARGET}/{nonce}"
    effect = declared_effect(
        "WRITE",
        target,
        f"زرُّ التوقّفِ «{before['level']}» → «{level}» بطلبِ «{activated_by}»",
    )

    def _apply(_effect: Any) -> dict[str, Any]:
        return store.set_level(level, reason, activated_by)

    def _restore() -> None:
        # عكسٌ باللقطةِ السابقةِ — والحدُّ المُعلَن: `activated_at` يُعادُ ختمُه لا يُستعاد.
        if before["level"] == "normal":
            store.reset()
        else:
            store.set_level(before["level"], before["reason"], before["activated_by"])

    violation = _core_sovereignty("gateway").SovereigntyViolation
    try:
        guarded = _guard_kill_switch(
            verb, target, nonce, effect, _apply, _restore, activated_by, before, level
        )
    except violation as exc:
        raise KillSwitchRefusedError(verb, str(exc)) from exc
    state = guarded.value
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


def create_promotion(model_id: str, requested_by: str | None = None) -> dict[str, Any]:
    """إنشاء طلب ترقية نموذج — عبرَ الحدِّ بفعلِ طلبٍ لا بفعلِ ترقية (WI-114 السطح 3).

    `requested_by` يُحمَلُ في بياناتِ طلبِ العبورِ كما يُمرِّرُه المُنادي؛ والمسارُ اليومَ لا يُمرِّرُه
    (`None` · DISC-139 · ملفُّ المسارِ في مساراتِ WI-117).
    والمُعوِّضُ **إبطالٌ لا حذف**: الحدُّ يشترطُ خطّةَ تعويضٍ للإنشاءِ (`CompensationNotDeclaredError`)،
    ولا حذفَ في `PersistentPromotionStore` و`persistent.py` لا يُمَسّ (التصميم § 3.1)، فيُنقَلُ الطلبُ
    إلى `cancelled` بـ`save_gates` القائم. والحدُّ مُعلَن: يبقى صفٌّ مُبطَلٌ في الجدولِ بعدَ التعويض.
    """
    now = datetime.now(UTC).isoformat()
    promotion_id = f"promo-{uuid.uuid4()}"
    promotion = {
        "promotion_id": promotion_id,
        "model_id": model_id,
        "gates": {gate: {"status": "pending", "checked_at": None} for gate in PROMOTION_GATES},
        "status": "in_progress",
        "created_at": now,
        "updated_at": now,
    }
    target = f"governance/promotions/{promotion_id}"
    effect = declared_effect(
        "CREATE", target, f"طلبُ ترقيةٍ للنموذجِ «{model_id}» بطلبِ «{requested_by}»"
    )

    def _apply(_effect: Any) -> dict[str, Any]:
        _promotion_store().create(promotion)
        return promotion

    def _cancel() -> None:
        _promotion_store().save_gates(
            promotion_id, promotion["gates"], "cancelled", datetime.now(UTC).isoformat()
        )

    guarded = _canary_authorizer().guard_declared(
        ACTION_REQUEST_PROMOTION,
        target,
        declared_effects=(effect,),
        applier=_apply,
        operation_key=operation_key(PROMOTION_REQUEST_SCOPE, promotion_id),
        compensators=(
            compensator(
                effect.signature,
                _cancel,
                "إبطالُ طلبِ الترقيةِ المُنشَأِ (`cancelled`) — لا حذفَ في المخزن",
            ),
        ),
        metadata={"requested_by": requested_by, "model_id": model_id},
    )
    return dict(guarded.value)


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
