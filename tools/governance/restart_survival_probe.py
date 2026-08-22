"""مِسبارُ نجاةِ الحالةِ عبرَ إعادةِ التشغيل — قياسٌ لا تصريح.

الهدف:
    تحويلُ تصاريحِ الإدامةِ التي أُضيفَت في `T3.6 · W-029` من **دعوى مكتوبةٍ في
    الشِّفرةِ** إلى **واقعٍ مقيسٍ بالتجربة**: يُكتَبُ الشيءُ في عمليّةٍ، ثمّ تُقتَلُ
    العمليّةُ، ثمّ يُقرَأُ الشيءُ في عمليّةٍ جديدةٍ على قاعدةِ البياناتِ نفسِها.
    فما نجا نجا حقًّا، وما فُقِدَ فُقِدَ حقًّا.

    والفرقُ بينَ هذا وبينَ اختبارِ وحدةٍ عاديٍّ جوهريّ: `importlib.reload` لا يُعيدُ
    تشغيلًا — يبقى المفسِّرُ نفسُه ويبقى مخزنُ الوحدةِ حيًّا في حالاتٍ كثيرةٍ. ولذلك
    **كلُّ مرحلةٍ هنا عمليّةُ نظامٍ مستقلّةٌ** (`subprocess`)، وهو أقربُ ما يُحاكي
    إعادةَ تشغيلِ الخدمةِ في الإنتاج.

النطاق:
    اثنا عشرَ سطحًا: عشرةٌ مُصرَّحٌ بتطايرِها في `W-029` (ومنها **مفتاحُ الإيقافِ**)،
    وسطحُ ذاكرةٍ مؤقّتةٍ يُعادُ بناؤُه من قاعدةِ البياناتِ، وسطحٌ دائمٌ **شاهدُ ضبطٍ**
    لولاه لصارَ «فُقِدَ الكلُّ» تفسيرَه أنَّ المِسبارَ نفسَه مكسورٌ لا أنَّ الحالةَ
    تتطايَر.

    ولا يُقيسُ هذا المِسبارُ صوابَ المعمار: لا يقولُ «يجبُ أن تكونَ دائمةً». يقولُ
    «هذه تتطايَرُ، وهذا ما يُفقَدُ حينَ تتطايَر». والحكمُ على ما يجبُ أن يُدامَ
    قرارٌ سياديٌّ مفتوحٌ — `Q-39` في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`.

المالك:
    `tools/governance` — ديوانُ الحوكمة. والمُخرَجُ يُكتَبُ آليًّا إلى
    `docs/audit/measurements/restart_survival.json` ولا يُحرَّرُ باليد.

الاستخدام:
    python tools/governance/restart_survival_probe.py            # قِسْ واكتُبْ
    python tools/governance/restart_survival_probe.py --check    # افشلْ إن خالفَ التصريحَ
    python tools/governance/restart_survival_probe.py --json     # اطبعْ ولا تكتُبْ

تاريخ الإنشاء: 2026-08-22
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable

_HERE = Path(__file__).resolve()
_REPO_ROOT = _HERE.parents[2]
_SERVICES_SRC = _REPO_ROOT / "federal" / "executive" / "services" / "src"

# التصنيفاتُ المُعلَنةُ في W-029 — نفسُ المفرداتِ حرفًا بحرفٍ لئلّا يتفرّقَ المعجمُ
# بينَ أداتَينِ في مستودعٍ واحد.
VOLATILE = "WIRED_VOLATILE"
CACHE_REBUILDABLE = "CACHE_REBUILDABLE"
DURABLE = "DURABLE_CONTROL"


# =============================================================================
# 1) عقدُ السطحِ المقيس
# =============================================================================
@dataclass
class Surface:
    """سطحُ حالةٍ يُقاسُ: كيفَ يُكتَبُ، وكيفَ يُقرَأُ بعدَ إعادةِ التشغيل."""

    surface_id: str
    service: str
    declared: str
    what_is_lost: str
    writer: str
    reader: str


@dataclass
class Result:
    """نتيجةُ قياسِ سطحٍ واحدٍ — واقعٌ لا تقدير."""

    surface_id: str
    service: str
    declared: str
    what_is_lost: str
    wrote_ok: bool
    survived: bool | None
    expected_survival: bool
    verdict: str
    detail: str = ""
    extra: dict[str, Any] = field(default_factory=dict)


# =============================================================================
# 2) مراحلُ الكتابةِ والقراءةِ — تُنفَّذُ كلُّ واحدةٍ في عمليّةٍ مستقلّة
# =============================================================================
def _client(service: str) -> Any:
    """عميلُ اختبارٍ على تطبيقِ الخدمةِ، مُهيَّأٌ برمزِ دخولٍ صالح."""
    import importlib

    from fastapi.testclient import TestClient

    module = importlib.import_module(f"amos_federation.services.{service}.main")
    return TestClient(module.app), module


def _headers() -> dict[str, str]:
    """ترويسةُ تخويلٍ — كلُّ نقاطِ هذه الأسطحِ تكتفي بـ`require_auth`."""
    from amos_federation.common.auth import create_access_token

    token = create_access_token("restart_probe", ["*"])
    return {"Authorization": f"Bearer {token}"}


def _sample_experiences() -> list[dict[str, Any]]:
    """خبرتانِ تكفيانِ لإنشاءِ مجموعةِ بياناتٍ صالحة."""
    return [
        {
            "experience_id": "probe-exp-1",
            "type": "success",
            "agent_id": "probe-agent",
            "model_used": "alpha",
            "quality_score": 0.9,
            "created_at": "2026-08-22T10:00:00Z",
            "outcome": {"input": "قِسْ", "output": "قِيسَ", "domain": "governance"},
        },
        {
            "experience_id": "probe-exp-2",
            "type": "failure",
            "agent_id": "probe-agent",
            "model_used": "alpha",
            "quality_score": 0.2,
            "created_at": "2026-08-22T11:00:00Z",
            "outcome": {"input": "قِسْ", "output": "", "domain": "governance"},
        },
    ]


# --- training -----------------------------------------------------------------
def _write_training_dataset() -> dict[str, Any]:
    client, _ = _client("training")
    resp = client.post(
        "/v1/datasets", headers=_headers(), json={"experiences": _sample_experiences()}
    )
    resp.raise_for_status()
    return {"key": resp.json()["dataset_id"]}


def _read_training_dataset(key: str) -> dict[str, Any]:
    client, _ = _client("training")
    resp = client.get(f"/v1/datasets/{key}", headers=_headers())
    return {"survived": resp.status_code == 200, "detail": f"HTTP {resp.status_code}"}


def _write_training_model() -> dict[str, Any]:
    client, _ = _client("training")
    dataset = client.post(
        "/v1/datasets", headers=_headers(), json={"experiences": _sample_experiences()}
    )
    dataset.raise_for_status()
    resp = client.post(
        "/v1/models/train",
        headers=_headers(),
        json={"dataset_id": dataset.json()["dataset_id"]},
    )
    resp.raise_for_status()
    return {"key": resp.json()["model_id"]}


def _read_training_model(key: str) -> dict[str, Any]:
    client, _ = _client("training")
    resp = client.get(f"/v1/models/{key}", headers=_headers())
    return {"survived": resp.status_code == 200, "detail": f"HTTP {resp.status_code}"}


# --- model_gateway ------------------------------------------------------------
def _write_shadow() -> dict[str, Any]:
    client, _ = _client("model_gateway")
    resp = client.post(
        "/v1/shadow/test", headers=_headers(), json={"prompt": "قياسُ الظلِّ"}
    )
    resp.raise_for_status()
    return {"key": resp.json()["shadow_id"]}


def _read_shadow(key: str) -> dict[str, Any]:
    client, _ = _client("model_gateway")
    resp = client.get(f"/v1/shadow/results/{key}", headers=_headers())
    return {"survived": resp.status_code == 200, "detail": f"HTTP {resp.status_code}"}


def _write_cost() -> dict[str, Any]:
    """نداءُ نموذجٍ واحدٌ يُقيَّدُ في مَصدرَي تكلفةٍ متنافسَين."""
    client, _ = _client("model_gateway")
    resp = client.post(
        "/v1/models/invoke", headers=_headers(), json={"prompt": "قِسْ تكلفةً"}
    )
    resp.raise_for_status()
    volatile = client.get("/v1/cost/summary", headers=_headers()).json()
    persistent = client.get("/v1/models/cost-summary", headers=_headers()).json()
    return {
        "key": "cost",
        "extra": {
            "volatile_before": _cost_count(volatile),
            "persistent_before": _cost_count(persistent),
        },
    }


def _cost_count(payload: Any) -> int:
    """عدُّ النداءاتِ من ملخّصِ تكلفةٍ أيًّا كانَ مفتاحُه."""
    if not isinstance(payload, dict):
        return -1
    for key in (
        "total_invocations",
        "total_requests",
        "requests",
        "count",
        "invocations",
    ):
        value = payload.get(key)
        if isinstance(value, int):
            return value
    for value in payload.values():
        if isinstance(value, dict):
            nested = _cost_count(value)
            if nested >= 0:
                return nested
    return -1


def _read_cost(key: str) -> dict[str, Any]:
    client, _ = _client("model_gateway")
    volatile = _cost_count(client.get("/v1/cost/summary", headers=_headers()).json())
    persistent = _cost_count(
        client.get("/v1/models/cost-summary", headers=_headers()).json()
    )
    return {
        "survived": volatile > 0,
        "detail": f"المتطايرُ بعدَ الإقلاعِ {volatile} · الدائمُ {persistent}",
        "extra": {"volatile_after": volatile, "persistent_after": persistent},
    }


# --- governance ---------------------------------------------------------------
def _write_kill_switch() -> dict[str, Any]:
    client, _ = _client("governance")
    resp = client.post(
        "/v1/system/kill-switch",
        headers=_headers(),
        json={"level": "halt", "reason": "مِسبارُ نجاةٍ", "activated_by": "restart_probe"},
    )
    resp.raise_for_status()
    return {"key": "halt", "extra": {"level_after_write": resp.json().get("level")}}


def _read_kill_switch(key: str) -> dict[str, Any]:
    client, _ = _client("governance")
    resp = client.get("/v1/system/status", headers=_headers())
    level = resp.json().get("level") if resp.status_code == 200 else None
    return {
        "survived": level == key,
        "detail": f"المستوى بعدَ الإقلاعِ: {level!r} (‏كُتِبَ {key!r})",
        "extra": {"level_after_restart": level},
    }


def _write_promotion() -> dict[str, Any]:
    client, _ = _client("governance")
    resp = client.post(
        "/v1/promotions", headers=_headers(), json={"model_id": "probe-model"}
    )
    resp.raise_for_status()
    return {"key": resp.json()["promotion_id"]}


def _read_promotion(key: str) -> dict[str, Any]:
    client, _ = _client("governance")
    resp = client.get(f"/v1/promotions/{key}", headers=_headers())
    return {"survived": resp.status_code == 200, "detail": f"HTTP {resp.status_code}"}


def _write_canary() -> dict[str, Any]:
    client, _ = _client("governance")
    resp = client.post(
        "/v1/canary",
        headers=_headers(),
        json={"model_id": "probe-model", "traffic_percentage": 5},
    )
    resp.raise_for_status()
    body = resp.json()
    return {"key": body.get("canary_id") or body.get("id") or ""}


def _read_canary(key: str) -> dict[str, Any]:
    client, _ = _client("governance")
    resp = client.get(f"/v1/canary/{key}", headers=_headers())
    return {"survived": resp.status_code == 200, "detail": f"HTTP {resp.status_code}"}


def _write_audit() -> dict[str, Any]:
    """شاهدُ الضبطِ الأوّلُ: سجلُّ التدقيقِ متسلسلُ التجزئةِ في قاعدةِ البيانات."""
    client, _ = _client("governance")
    client.post("/v1/promotions", headers=_headers(), json={"model_id": "probe-audit"})
    resp = client.get("/v1/audit", headers=_headers())
    resp.raise_for_status()
    return {"key": "audit", "extra": {"entries_before": len(resp.json() or [])}}


def _read_audit(key: str) -> dict[str, Any]:
    client, _ = _client("governance")
    resp = client.get("/v1/audit", headers=_headers())
    entries = len(resp.json() or []) if resp.status_code == 200 else -1
    return {
        "survived": entries > 0,
        "detail": f"مداخلُ التدقيقِ بعدَ الإقلاعِ: {entries}",
        "extra": {"entries_after": entries},
    }


def _probe_factory_id(factories_module: Any) -> str:
    """مصنعٌ مُعلَنٌ في `FACTORIES` — فـ`_init_factory` لا يُنشئُ صفَّ مصنعٍ لغيرِه.

    وهذا نفسُه واقعٌ يُقاس: لا مصانعَ في الجدولِ عندَ الإقلاعِ البارد، والقاموسُ
    `_factories` يُبنى عندَ أوّلِ نداءٍ لا عندَ التهيئة.
    """
    return next(iter(factories_module.FACTORIES))


def _write_factory_product() -> dict[str, Any]:
    """سطحُ الذاكرةِ المؤقّتة: القاموسُ يُعادُ بناؤُه، والمُنتَجُ في جدول."""
    from amos_federation.services.governance import factories as factories_module

    factory_id = _probe_factory_id(factories_module)
    factory = factories_module.Factory(factory_id)
    product = factory.run_full_pipeline(
        "مُنتَجُ مِسبارِ النجاة", producer_agent_id="restart_probe"
    )
    return {
        "key": str(product.get("product_id", "")),
        "extra": {"cached_factories_before": len(factories_module._factories)},
    }


def _read_factory_product(key: str) -> dict[str, Any]:
    from amos_federation.services.governance import factories as factories_module

    factory_id = _probe_factory_id(factories_module)
    found = factories_module.Factory(factory_id).get_product(key)
    return {
        "survived": found is not None,
        "detail": "المُنتَجُ موجودٌ في الجدولِ بعدَ الإقلاعِ" if found else "المُنتَجُ غيرُ موجود",
        "extra": {"cached_factories_after_boot": len(factories_module._factories)},
    }


# --- api_gateway --------------------------------------------------------------
def _agent_manifest() -> dict[str, Any]:
    return {
        "agent_id": "probe-agent",
        "name": "وكيلُ مِسبارٍ",
        "version": "1.0.0",
        "description": "وكيلٌ يُسجَّلُ لقياسِ النجاةِ عبرَ إعادةِ التشغيل",
        "capabilities": ["measure"],
        "tools": [],
        "model_preferences": [],
        "owner": "tools/governance",
    }


def _write_agent() -> dict[str, Any]:
    client, _ = _client("api_gateway")
    resp = client.post("/v1/agents", headers=_headers(), json=_agent_manifest())
    if resp.status_code >= 400:
        return {"key": "", "detail": f"HTTP {resp.status_code}: {resp.text[:200]}"}
    return {"key": resp.json()["agent_id"]}


def _read_agent(key: str) -> dict[str, Any]:
    client, _ = _client("api_gateway")
    resp = client.get("/v1/agents", headers=_headers())
    ids = [a.get("agent_id") for a in resp.json()] if resp.status_code == 200 else []
    return {
        "survived": key in ids,
        "detail": f"عددُ الوكلاءِ بعدَ الإقلاعِ: {len(ids)}",
        "extra": {"agents_after_restart": len(ids)},
    }


def _write_task() -> dict[str, Any]:
    """شاهدُ الضبطِ الثاني: المهامُّ في `PersistentTaskStore` فيجبُ أن تنجو."""
    client, _ = _client("api_gateway")
    resp = client.post(
        "/v1/tasks",
        headers=_headers(),
        json={"type": "generic", "description": "مهمّةُ مِسبارِ النجاة"},
    )
    if resp.status_code >= 400:
        return {"key": "", "detail": f"HTTP {resp.status_code}: {resp.text[:200]}"}
    body = resp.json()
    return {"key": body.get("task_id") or body.get("id") or ""}


def _read_task(key: str) -> dict[str, Any]:
    client, _ = _client("api_gateway")
    resp = client.get(f"/v1/tasks/{key}", headers=_headers())
    return {"survived": resp.status_code == 200, "detail": f"HTTP {resp.status_code}"}


WRITERS: dict[str, Callable[[], dict[str, Any]]] = {
    "training_dataset": _write_training_dataset,
    "training_model": _write_training_model,
    "shadow_result": _write_shadow,
    "cost_log": _write_cost,
    "kill_switch": _write_kill_switch,
    "promotion": _write_promotion,
    "canary": _write_canary,
    "registered_agent": _write_agent,
    "factory_product": _write_factory_product,
    "audit_chain": _write_audit,
    "task": _write_task,
}

READERS: dict[str, Callable[[str], dict[str, Any]]] = {
    "training_dataset": _read_training_dataset,
    "training_model": _read_training_model,
    "shadow_result": _read_shadow,
    "cost_log": _read_cost,
    "kill_switch": _read_kill_switch,
    "promotion": _read_promotion,
    "canary": _read_canary,
    "registered_agent": _read_agent,
    "factory_product": _read_factory_product,
    "audit_chain": _read_audit,
    "task": _read_task,
}

SURFACES: tuple[Surface, ...] = (
    Surface(
        "kill_switch",
        "governance",
        VOLATILE,
        "مستوى مفتاحِ الإيقافِ: نظامٌ أُوقِفَ لطارئٍ يعودُ `normal` من نفسِه",
        "kill_switch",
        "kill_switch",
    ),
    Surface(
        "promotion",
        "governance",
        VOLATILE,
        "موافقاتُ ترقيةِ النماذجِ وبوّاباتُها المقطوعة",
        "promotion",
        "promotion",
    ),
    Surface(
        "canary",
        "governance",
        VOLATILE,
        "نشراتُ الـcanary ونسبةُ مرورِها",
        "canary",
        "canary",
    ),
    Surface(
        "training_dataset",
        "training",
        VOLATILE,
        "مجموعاتُ بياناتِ التدريبِ المُولَّدة",
        "training_dataset",
        "training_dataset",
    ),
    Surface(
        "training_model",
        "training",
        VOLATILE,
        "سجلُّ النماذجِ وبطاقاتُها وحالةُ ترقيتِها للإنتاج",
        "training_model",
        "training_model",
    ),
    Surface(
        "shadow_result",
        "model_gateway",
        VOLATILE,
        "نتائجُ اختبارِ الظلِّ التي يُقارَنُ بها نموذجٌ جديد",
        "shadow_result",
        "shadow_result",
    ),
    Surface(
        "cost_log",
        "model_gateway",
        VOLATILE,
        "سجلُّ تكلفةِ النداءاتِ في `/v1/cost/summary` — ولها مصدرٌ دائمٌ منافسٌ (Q-39)",
        "cost_log",
        "cost_log",
    ),
    Surface(
        "registered_agent",
        "api_gateway",
        VOLATILE,
        "بياناتُ الوكلاءِ المُسجَّلينَ عبرَ البوّابة",
        "registered_agent",
        "registered_agent",
    ),
    Surface(
        "factory_product",
        "governance",
        CACHE_REBUILDABLE,
        "لا شيءَ: القاموسُ ذاكرةٌ مؤقّتةٌ والمُنتَجُ في جدولٍ — والقياسُ يُثبِتُه",
        "factory_product",
        "factory_product",
    ),
    Surface(
        "audit_chain",
        "governance",
        DURABLE,
        "لا شيءَ: سجلُّ التدقيقِ في قاعدةِ البيانات — شاهدُ ضبطٍ",
        "audit_chain",
        "audit_chain",
    ),
    Surface(
        "task",
        "api_gateway",
        DURABLE,
        "لا شيءَ: المهامُّ في مخزنٍ دائمٍ — شاهدُ ضبطٍ",
        "task",
        "task",
    ),
)


# =============================================================================
# 3) التنسيقُ بينَ العمليّات
# =============================================================================
def _phase_env(db_path: Path) -> dict[str, str]:
    """بيئةٌ واحدةٌ للمرحلتَينِ: نفسُ القاعدةِ ونفسُ السرِّ، وإلّا فالقياسُ باطل."""
    env = dict(os.environ)
    env["AMOS_DATABASE_URL"] = f"sqlite:///{db_path}"
    env["AMOS_ENVIRONMENT"] = "test"
    # سجلُّ ذرّيّةِ النواةِ التنفيذيّةِ يُوجَّهُ إلى موضعِ القياسِ المؤقّتِ لا إلى
    # `.runtime/` داخلَ شجرةِ المستودع: القياسُ لا يُلوِّثُ المقيس، وأثرُ التشغيلِ
    # في الشجرةِ يُسقِطُ بوّابةَ الهويّةِ (‏المادةُ التاسعةُ) كما قِيسَ في W-030
    # وقُيِّدَ سؤالًا مفتوحًا (‏Q-40) — ولا يُحسَمُ هنا بتضييقِ كاشفٍ ولا بحكمِ عامل.
    env["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = str(
        db_path.parent / "sovereignty" / "executive_core_idempotency.json"
    )
    env.setdefault("AMOS_JWT_SECRET", "restart_probe_secret_at_least_32_characters")
    env["AMOS_CLAUDE_API_KEY"] = env.get("AMOS_CLAUDE_API_KEY", "probe_key_not_real")
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = (
        f"{_SERVICES_SRC}{os.pathsep}{existing}" if existing else str(_SERVICES_SRC)
    )
    return env


def _run_phase(
    phase: str, surface: Surface, db_path: Path, key: str = ""
) -> dict[str, Any]:
    """شغِّلْ مرحلةً في **عمليّةٍ مستقلّةٍ** وأعِدْ حصيلتَها."""
    cmd = [
        sys.executable,
        str(_HERE),
        "--phase",
        phase,
        "--surface",
        surface.surface_id,
    ]
    if key:
        cmd += ["--key", key]
    proc = subprocess.run(
        cmd,
        cwd=str(_REPO_ROOT),
        env=_phase_env(db_path),
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    marker = "PROBE_RESULT:"
    for line in reversed(proc.stdout.splitlines()):
        if line.startswith(marker):
            return json.loads(line[len(marker) :])
    tail = (proc.stderr or proc.stdout).strip().splitlines()
    return {"error": tail[-1] if tail else f"رمزُ الخروجِ {proc.returncode}"}


def measure(db_path: Path) -> list[Result]:
    """قِسْ كلَّ سطحٍ: اكتُبْ في عمليّةٍ، واقرأْ في عمليّةٍ أخرى."""
    results: list[Result] = []
    for surface in SURFACES:
        expected_survival = surface.declared in (CACHE_REBUILDABLE, DURABLE)
        wrote = _run_phase("write", surface, db_path)
        if "error" in wrote or not wrote.get("key"):
            results.append(
                Result(
                    surface.surface_id,
                    surface.service,
                    surface.declared,
                    surface.what_is_lost,
                    wrote_ok=False,
                    survived=None,
                    expected_survival=expected_survival,
                    verdict="UNMEASURED",
                    detail=str(
                        wrote.get("error") or wrote.get("detail") or "لا مفتاحَ كتابةٍ"
                    ),
                )
            )
            continue
        read = _run_phase("read", surface, db_path, str(wrote["key"]))
        if "error" in read:
            results.append(
                Result(
                    surface.surface_id,
                    surface.service,
                    surface.declared,
                    surface.what_is_lost,
                    wrote_ok=True,
                    survived=None,
                    expected_survival=expected_survival,
                    verdict="UNMEASURED",
                    detail=str(read["error"]),
                )
            )
            continue
        survived = bool(read.get("survived"))
        verdict = (
            "MATCHES_DECLARATION"
            if survived == expected_survival
            else "CONTRADICTS_DECLARATION"
        )
        extra = dict(wrote.get("extra") or {})
        extra.update(read.get("extra") or {})
        results.append(
            Result(
                surface.surface_id,
                surface.service,
                surface.declared,
                surface.what_is_lost,
                wrote_ok=True,
                survived=survived,
                expected_survival=expected_survival,
                verdict=verdict,
                detail=str(read.get("detail", "")),
                extra=extra,
            )
        )
    return results


def summarize(results: list[Result]) -> dict[str, Any]:
    """خلاصةٌ تُقرأُ بلا تفسيرٍ: كم فُقِدَ · كم نجا · كم لم يُقَسْ · كم خالفَ التصريح."""
    return {
        "surfaces_total": len(results),
        "lost_on_restart": sum(1 for r in results if r.survived is False),
        "survived_restart": sum(1 for r in results if r.survived is True),
        "unmeasured": sum(1 for r in results if r.survived is None),
        "contradicts_declaration": sum(
            1 for r in results if r.verdict == "CONTRADICTS_DECLARATION"
        ),
        "declared_volatile": sum(1 for r in results if r.declared == VOLATILE),
        "control_surfaces": sum(1 for r in results if r.declared == DURABLE),
    }


def _write_json(results: list[Result], summary: dict[str, Any]) -> Path:
    """اكتُبِ المُخرَجَ الخامَّ — ولا يُحرَّرُ باليدِ بعدَها."""
    out_dir = _REPO_ROOT / "docs" / "audit" / "measurements"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "restart_survival.json"
    payload = {
        "$comment": (
            "الهدف: قياسُ ما ينجو من حالةِ الخدماتِ عبرَ إعادةِ التشغيلِ الحقيقيّةِ "
            "(عمليّةٌ تكتبُ وعمليّةٌ أخرى تقرأُ) — مُخرَجُ "
            "tools/governance/restart_survival_probe.py (T3.6 · W-030). المادةُ التاسعةُ · 2."
        ),
        "note": (
            "قياسٌ لا حُكم: يقولُ ما يُفقَدُ، ولا يقولُ ما يجبُ أن يُدامَ — ذاك قرارٌ "
            "سياديٌّ مفتوحٌ (Q-39). و`lost_on_restart` **ليس** مخالفةً جديدةً ولا يدخلُ "
            "عدّادَ المصفوفةِ: هو بيانُ أثرِ الستّينَ المعروفةِ. وشاهدا الضبطِ "
            "(audit_chain · task) يجبُ أن ينجُوا، فإن سقطا فالمِسبارُ هو المكسورُ لا الحالة."
        ),
        "summary": summary,
        "surfaces": [asdict(r) for r in results],
    }
    out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return out


# =============================================================================
# 4) نقطةُ الدخول
# =============================================================================
def _emit(payload: dict[str, Any]) -> None:
    print("PROBE_RESULT:" + json.dumps(payload, ensure_ascii=False))


def main(argv: list[str] | None = None) -> int:
    """قِسْ، أو نفِّذْ مرحلةً واحدةً عندَ استدعاءِ نفسِك في عمليّةٍ فرعيّة."""
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--phase", choices=["write", "read"])
    parser.add_argument("--surface")
    parser.add_argument("--key", default="")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if args.phase:
        if str(_SERVICES_SRC) not in sys.path:
            sys.path.insert(0, str(_SERVICES_SRC))
        try:
            if args.phase == "write":
                _emit(WRITERS[args.surface]())
            else:
                _emit(READERS[args.surface](args.key))
        except Exception as exc:  # لا يُبتلَع: الخطأُ يُعلَنُ ويصيرُ UNMEASURED
            _emit({"error": f"{type(exc).__name__}: {exc}"})
            return 2
        return 0

    with tempfile.TemporaryDirectory(prefix="amos_restart_probe_") as tmp:
        db_path = Path(tmp) / "probe.db"
        results = measure(db_path)

    summary = summarize(results)

    if args.json:
        print(
            json.dumps(
                {"summary": summary, "surfaces": [asdict(r) for r in results]},
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(f"[RESTART PROBE] أسطحٌ مقيسةٌ: {summary['surfaces_total']}")
        print(f"  - فُقِدَت عندَ إعادةِ التشغيل: {summary['lost_on_restart']}")
        print(f"  - نجَت: {summary['survived_restart']}")
        print(f"  - لم تُقَسْ: {summary['unmeasured']}")
        print(f"  - خالفَت تصريحَها: {summary['contradicts_declaration']}")
        for r in results:
            state = {True: "نجا", False: "فُقِدَ", None: "لم يُقَسْ"}[r.survived]
            print(
                f"    · {r.surface_id} ({r.service}) → {state} · {r.verdict} · {r.detail}"
            )

    out = _write_json(results, summary)
    print(f"[RESTART PROBE] كُتب: {out.relative_to(_REPO_ROOT)}")

    if args.check:
        if summary["contradicts_declaration"] or summary["unmeasured"]:
            print("[RESTART PROBE] ✗ قياسٌ يخالفُ التصريحَ أو سطحٌ لم يُقَسْ.")
            return 1
        print("[RESTART PROBE] ✓ كلُّ سطحٍ يتصرّفُ كما صُرِّحَ به.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
