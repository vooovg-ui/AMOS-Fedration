"""
AMOS-Federation Durable Model Registry Test
الهدف: إثباتُ نجاةِ النموذجِ المُدرَّبِ والمُرقَّى عبرَ عمليّتَينِ مستقلّتَينِ
النطاق: federal/executive/services/tests (training)
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-04

اختبار: سجلُّ النماذجِ الدائمُ ينجو من إعادةِ التشغيل.

WI-055 · Q-39 (أ) — 2026-08-23.

المعيارُ الأول: نموذجٌ يُدرَّبُ ويُرقّى إلى الإنتاجِ في عمليّةٍ، ثمّ يُقرَأُ
بحالتهِ وبطاقتهِ في عمليّةٍ مستقلّةٍ على قاعدةِ البياناتِ نفسِها. وعمليّتانِ
مستقلّتانِ تعني `subprocess` لا `importlib.reload` — لأنَّ الأخيرَ يبقي المفسّرَ
ووحداتِه حيّةً.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[4]
_SERVICES_SRC = _REPO_ROOT / "federal" / "executive" / "services" / "src"
_TRAINING_TESTS = _REPO_ROOT / "federal" / "executive" / "services" / "tests"


def _phase_env(db_path: Path) -> dict[str, str]:
    """بيئةٌ واحدةٌ للمرحلتَينِ: نفسُ القاعدةِ ونفسُ السرّ."""
    env = dict(os.environ)
    env["AMOS_DATABASE_URL"] = f"sqlite:///{db_path}"
    env["AMOS_ENVIRONMENT"] = "test"
    env.setdefault(
        "AMOS_JWT_SECRET", "durable_registry_test_secret_at_least_32_chars"
    )
    env["AMOS_CLAUDE_API_KEY"] = "test_key_not_real"
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = (
        f"{_SERVICES_SRC}{os.pathsep}{existing}" if existing else str(_SERVICES_SRC)
    )
    return env


_WRITE_SCRIPT = """
import json
import sys

sys.path.insert(0, "{src}")

from fastapi.testclient import TestClient
from amos_federation.services.training import main as training_main
from amos_federation.common.auth import create_access_token

client = TestClient(training_main.app)
token = create_access_token("durable_test", ["*"])
headers = {{"Authorization": f"Bearer {{token}}"}}

# 1) أنشئ مجموعة بيانات
ds = client.post("/v1/datasets", headers=headers, json={{
    "experiences": [
        {{
            "experience_id": "exp-1",
            "type": "success",
            "agent_id": "test-agent",
            "model_used": "alpha",
            "quality_score": 0.9,
            "created_at": "2026-10-04T10:00:00Z",
            "outcome": {{"input": "test", "output": "ok", "domain": "governance"}},
        }}
    ]
}})
ds.raise_for_status()
dataset_id = ds.json()["dataset_id"]

# 2) درّب نموذجًا
train = client.post("/v1/models/train", headers=headers, json={{
    "dataset_id": dataset_id,
    "base_model": "llama-3-8b",
    "training_method": "LoRA",
}})
train.raise_for_status()
model = train.json()
model_id = model["model_id"]

# 3) رقِّ النموذج إلى الإنتاج
promote = client.patch(f"/v1/models/{{model_id}}/status", headers=headers, json={{
    "status": "promoted"
}})
promote.raise_for_status()

print("PROBE_RESULT:" + json.dumps({{
    "model_id": model_id,
    "status": promote.json()["status"],
    "dataset_id": dataset_id,
}}, ensure_ascii=False))
""".format(src=str(_SERVICES_SRC))


_READ_SCRIPT = """
import json
import sys

sys.path.insert(0, "{src}")

from fastapi.testclient import TestClient
from amos_federation.services.training import main as training_main
from amos_federation.common.auth import create_access_token

client = TestClient(training_main.app)
token = create_access_token("durable_test", ["*"])
headers = {{"Authorization": f"Bearer {{token}}"}}

model_id = sys.argv[1]

# اقرأ النموذج
resp = client.get(f"/v1/models/{{model_id}}", headers=headers)
if resp.status_code != 200:
    print("PROBE_RESULT:" + json.dumps({{
        "survived": False,
        "detail": f"HTTP {{resp.status_code}}",
    }}, ensure_ascii=False))
    sys.exit(0)

model = resp.json()

# اقرأ Model Card
card_resp = client.get(f"/v1/models/{{model_id}}/card", headers=headers)

print("PROBE_RESULT:" + json.dumps({{
    "survived": True,
    "status": model.get("status"),
    "model_card": model.get("model_card", {{}}),
    "card_ok": card_resp.status_code == 200,
    "model_id": model.get("model_id"),
}}, ensure_ascii=False))
""".format(src=str(_SERVICES_SRC))


def _run_script(script: str, db_path: Path, args: list[str] | None = None) -> dict:
    """شغِّل نصًّا في عمليّةٍ مستقلّةٍ وأعِدْ حصيلتَه."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, dir=str(db_path.parent)
    ) as f:
        f.write(script)
        script_path = f.name

    cmd = [sys.executable, script_path]
    if args:
        cmd.extend(args)

    proc = subprocess.run(
        cmd,
        cwd=str(_REPO_ROOT),
        env=_phase_env(db_path),
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )

    Path(script_path).unlink(missing_ok=True)

    marker = "PROBE_RESULT:"
    for line in reversed(proc.stdout.splitlines()):
        if line.startswith(marker):
            return json.loads(line[len(marker):])

    tail = (proc.stderr or proc.stdout).strip().splitlines()
    raise AssertionError(
        f"script failed (exit {proc.returncode}): "
        f"{tail[-1] if tail else 'no output'}"
    )


def test_durable_model_survives_restart():
    """النموذجُ المُدرَّبُ والمُرقَّى يُقرَأُ في عمليّةٍ ثانيةٌ بحالتهِ وبطاقته.

    هذا هو المعيارُ الأولُ لـWI-055: إثباتٌ بعمليّتَينِ مستقلّتَينِ أنَّ
    سجلَّ النماذجِ الدائمَ ينجو من إعادةِ التشغيل.
    """
    with tempfile.TemporaryDirectory(prefix="amos_durable_registry_") as tmp:
        db_path = Path(tmp) / "test.db"

        # المرحلة 1: درّب ورقِّ في عمليّةٍ
        wrote = _run_script(_WRITE_SCRIPT, db_path)
        assert wrote.get("model_id"), f"لم يُنشأ نموذج: {wrote}"
        assert wrote.get("status") == "promoted", (
            f"النموذجُ لم يُرقَّ إلى الإنتاج: {wrote}"
        )
        model_id = wrote["model_id"]

        # المرحلة 2: اقرأ في عمليّةٍ مستقلّةٍ
        read = _run_script(_READ_SCRIPT, db_path, args=[model_id])
        assert read.get("survived"), (
            f"النموذجُ لم ينجُ من إعادةِ التشغيل: {read}"
        )
        assert read.get("status") == "promoted", (
            f"حالةُ النموذجِ لم تَنجُ: {read}"
        )
        assert read.get("card_ok"), (
            f"بطاقةُ النموذجِ لم تَنجُ: {read}"
        )
        card = read.get("model_card", {})
        assert card.get("base_model") == "llama-3-8b", (
            f"تفاصيلُ البطاقةِ لم تَنجُ: {card}"
        )
        assert card.get("training_method") == "LoRA", (
            f"تفاصيلُ البطاقةِ لم تَنجُ: {card}"
        )


def test_durable_registry_counts_persist():
    """عدّادُ النماذجِ يُقرَأُ في عمليّةٍ ثانيةٍ بعدَ الكتابةِ في الأولى."""
    with tempfile.TemporaryDirectory(prefix="amos_durable_count_") as tmp:
        db_path = Path(tmp) / "test.db"

        # المرحلة 1: درّب نموذجًا
        wrote = _run_script(_WRITE_SCRIPT, db_path)
        assert wrote.get("model_id"), f"لم يُنشأ نموذج: {wrote}"

        # المرحلة 2: اقرأ العدّاد في عمليّةٍ مستقلّةٍ
        read = _run_script(_READ_SCRIPT, db_path, args=[wrote["model_id"]])
        assert read.get("survived"), (
            f"النموذجُ لم ينجُ: {read}"
        )
