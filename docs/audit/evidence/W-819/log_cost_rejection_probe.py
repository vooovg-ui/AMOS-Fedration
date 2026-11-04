"""الهدف: مسبارُ قراءةٍ فقط (التوجيه 43 § 1): «هل يُسجَّل كلفة طلب يُرفض لاحقًا بالحاجز؟» (W-821).

التعريف: `model_gateway/main.py::invoke_model` يستدعي `get_model_layer().log_cost(...)` ثمّ
`boundary.authorized_activity(...)`. يقيسُ المسبارُ ذلك بطريقتَين ولا يُعدِّلُ شيفرةً:

  (أ) ساكنًا بشجرةِ AST: رقمُ سطرِ `log_cost` مقابلَ رقمِ سطرِ `authorized_activity` داخلَ
      `invoke_model`، واسمُ وسيطِ هويّةِ المنادي (`_` يعني أنّها تُستلَمُ ثمّ تُطرَح)، وهل
      يحملُ نداءُ `log_cost` أيَّ وسيطٍ للهويّة.
  (ب) تشغيلًا بقاعدةٍ مؤقّتة (`AMOS_DATABASE_URL` إلى ملفٍّ في مجلدٍ مؤقّت) وبالتطبيقِ الحقيقيّ
      عبرَ `TestClient`:
      ب1 · رفضٌ حقيقيٌّ بلا حقن: `task_id` غيرُ موجود ⇒ الحاجزُ يرفعُ `TaskNotFoundError` ⇒ 404.
      ب2 · رفضٌ دستوريٌّ محقون: `authorized_activity` يُستبدَلُ بدالّةٍ ترفعُ
          `SubsystemRefusedError` ⇒ 403. الحقنُ يُحاكي حكمَ الرفضِ وحدَه، والسؤالُ سؤالُ ترتيب.
      في كلٍّ منهما يُعَدُّ `cost_rows()` قبلُ وبعد.

الخروج: 0 إن اكتملَ القياس (أيًّا كان الجواب)، و1 إن تعذّرَ قياسُ شيءٍ ممّا سبق.
النطاق: قراءةٌ فقط — لا كتابةَ في المستودع، والقاعدةُ مؤقّتةٌ تُحذَفُ بانتهاءِ المسبار.
المالك: Perplexity Computer (قيدُ W-821 · DISC-160).

التشغيل (من جذرِ المستودع):
    OTEL_SDK_DISABLED=true .venv/bin/python docs/audit/evidence/W-819/log_cost_rejection_probe.py
"""

from __future__ import annotations

import ast
import importlib
import os
import secrets
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SERVICES = ROOT / "federal" / "executive" / "services"
MAIN = SERVICES / "src" / "amos_federation" / "services" / "model_gateway" / "main.py"


def static_order() -> dict[str, object]:
    tree = ast.parse(MAIN.read_text(encoding="utf-8"))
    fn = next(
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.AsyncFunctionDef | ast.FunctionDef)
        and n.name == "invoke_model"
    )
    log_line = boundary_line = None
    log_kwargs: list[str] = []
    for node in ast.walk(fn):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "log_cost":
                log_line = node.lineno
                log_kwargs = [k.arg or "**" for k in node.keywords]
            elif node.func.attr == "authorized_activity":
                boundary_line = node.lineno
    params = [a.arg for a in fn.args.args]
    return {
        "invoke_model_line": fn.lineno,
        "log_cost_line": log_line,
        "authorized_activity_line": boundary_line,
        "log_before_boundary": bool(
            log_line and boundary_line and log_line < boundary_line
        ),
        "params": params,
        "principal_param_discarded": "_" in params,
        "log_cost_kwargs": log_kwargs,
        "log_cost_carries_identity": any(
            k in {"principal", "actor", "subject", "identity", "user"}
            for k in log_kwargs
        ),
    }


def runtime(tmp: str) -> dict[str, object]:
    # بيئةُ اختبارٍ معزولةٌ كما يفعلُ `tests/conftest.py` للخدمات — قبلَ أيِّ استيراد:
    # قاعدةٌ وسجلُّ ذرّيّةٍ في المجلدِ المؤقّت، وسرُّ توقيعٍ عشوائيٌّ لهذا التشغيلِ وحدَه،
    # وبلا مفتاحِ Claude فيُجيبُ النموذجُ الاحتياطيُّ المحليُّ بلا شبكة.
    os.environ["AMOS_ENVIRONMENT"] = "test"
    os.environ["AMOS_DATABASE_URL"] = f"sqlite:///{Path(tmp) / 'probe.db'}"
    os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = str(Path(tmp) / "idem.jsonl")
    os.environ["AMOS_JWT_SECRET"] = secrets.token_hex(32)
    os.environ.pop("AMOS_CLAUDE_API_KEY", None)
    os.environ.setdefault("OTEL_SDK_DISABLED", "true")
    sys.path.insert(0, str(SERVICES / "src"))
    from fastapi.testclient import TestClient

    from amos_federation.common.auth import create_access_token

    main = importlib.import_module("amos_federation.services.model_gateway.main")
    layer = importlib.import_module(
        "amos_federation.services.model_gateway.model_layer"
    )
    boundary_mod = importlib.import_module(
        "amos_federation.services.executive_core.subsystem_boundary"
    )
    headers = {"Authorization": f"Bearer {create_access_token('w821-probe', ['*'])}"}
    client = TestClient(main.app)
    cost = layer.get_model_layer()

    out: dict[str, object] = {}
    before = len(cost.cost_rows())
    r1 = client.post(
        "/v1/models/invoke",
        headers=headers,
        json={"prompt": "مسبار", "task_id": "task-does-not-exist-w821"},
    )
    out["b1_status"] = r1.status_code
    out["b1_cost_rows_delta"] = len(cost.cost_rows()) - before

    boundary = boundary_mod.get_subsystem_boundary()
    original = boundary.authorized_activity

    def _refuse(*_a: object, **_k: object) -> object:
        raise boundary_mod.SubsystemRefusedError("رفضٌ دستوريٌّ محقونٌ للمسبار")

    boundary.authorized_activity = _refuse  # type: ignore[method-assign]
    try:
        before = len(cost.cost_rows())
        r2 = client.post("/v1/models/invoke", headers=headers, json={"prompt": "مسبار"})
        out["b2_status"] = r2.status_code
        out["b2_cost_rows_delta"] = len(cost.cost_rows()) - before
        rows = cost.cost_rows()
        out["b2_last_row_keys"] = sorted(rows[-1]) if rows else []
    finally:
        boundary.authorized_activity = original  # type: ignore[method-assign]
    return out


def main() -> int:
    s = static_order()
    for k, v in s.items():
        print(f"STATIC {k} = {v}")
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            r = runtime(tmp)
        finally:
            os.chdir(cwd)
    for k, v in r.items():
        print(f"RUNTIME {k} = {v}")
    measured = (
        s["log_cost_line"] is not None
        and s["authorized_activity_line"] is not None
        and "b1_status" in r
        and "b2_status" in r
    )
    rejected_yet_logged = (
        r.get("b1_status") == 404
        and r.get("b1_cost_rows_delta") == 1
        and r.get("b2_status") == 403
        and r.get("b2_cost_rows_delta") == 1
    )
    print(
        "ANSWER: نعم — تُسجَّلُ كلفةُ الطلبِ المرفوضِ بالحاجز"
        if rejected_yet_logged
        else "ANSWER: لا يثبتُ تسجيلُ كلفةِ الطلبِ المرفوض (انظر الأرقام أعلاه)"
    )
    print(f"MEASURED={measured}")
    return 0 if measured else 1


if __name__ == "__main__":
    sys.exit(main())
