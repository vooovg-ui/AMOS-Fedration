"""إثباتُ الخطوةِ 19 — إدامةُ مفتاحِ الإيقافِ وطلباتِ الترقيةِ تُقاسُ بعمليّتَين.

الهدف:
    تحويلُ قرارِ المالكِ في `Q-39 (أ)` — 2026-08-23 — من نصٍّ في سجلِّ القراراتِ إلى
    **واقعٍ مقيسٍ**: تكتبُ عمليّةٌ `halt` وموافقةَ ترقيةٍ، ثمّ تموتُ العمليّةُ، ثمّ
    تقرأُ عمليّةٌ **أخرى** القيمةَ نفسَها من قاعدةِ البياناتِ نفسِها.

    ولا يكفي `importlib.reload` ولا مخزنُ وحدةٍ في المفسِّرِ نفسِه: كِلاهما قد يُبقي
    الحالةَ حيّةً فيُوهِمَ نجاةً لم تحدُث. فكلُّ مرحلةٍ هنا **عمليّةُ نظامٍ مستقلّةٌ**
    (`subprocess`) — وهو أقربُ ما يُحاكي إعادةَ تشغيلِ الخدمةِ في الإنتاج.

النطاق:
    `services/governance/canary.py` بعدَ `W-031`، و`common/persistent.py`
    (‏`PersistentSystemStateStore` · `PersistentPromotionStore`‏)، وجدولاها
    `system_state` و`promotions` في `common/database.py`.

    وأثرُ الإدامةِ على عقدِ التشغيلِ مقصودٌ ومُقاسٌ هنا: **الإقلاعُ لا يرفعُ
    الإيقافَ**، ورفعُه فعلٌ صريحٌ (`reset_kill_switch`).

المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-23
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

SERVICES_SRC = Path(__file__).resolve().parents[1] / "src"

#: الكودُ المُشغَّلُ في عمليّةٍ مستقلّةٍ: يُنفِّذُ تعبيرًا ويطبعُ حصيلتَه سطرًا واحدًا.
_RUNNER = (
    "import json, sys\n"
    "from amos_federation.services.governance import canary\n"
    "out = eval(sys.argv[1])\n"
    "print('RESULT:' + json.dumps(out, ensure_ascii=False, default=str))\n"
)


def _run_in_fresh_process(db_path: Path, expression: str) -> object:
    """شغِّلْ تعبيرًا في **عمليّةٍ جديدةٍ** على قاعدةِ البياناتِ نفسِها."""
    env = dict(os.environ)
    env["AMOS_DATABASE_URL"] = f"sqlite:///{db_path}"
    env["AMOS_ENVIRONMENT"] = "test"
    env.setdefault("AMOS_JWT_SECRET", "step19_secret_at_least_32_characters_long")
    env.setdefault("AMOS_CLAUDE_API_KEY", "step19_key_not_real")
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = (
        f"{SERVICES_SRC}{os.pathsep}{existing}" if existing else str(SERVICES_SRC)
    )
    proc = subprocess.run(
        [sys.executable, "-c", _RUNNER, expression],
        env=env,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
    )
    for line in reversed(proc.stdout.splitlines()):
        if line.startswith("RESULT:"):
            return json.loads(line[len("RESULT:") :])
    raise AssertionError(
        f"العمليّةُ لم تُعِدْ حصيلةً — الخروجُ {proc.returncode}:\n"
        f"{proc.stderr.strip()[-2000:]}"
    )


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    """قاعدةُ بياناتٍ واحدةٌ للمرحلتَينِ — وإلّا فالقياسُ باطل."""
    return tmp_path / "step19_durability.db"


def test_halt_survives_a_real_restart(db_path: Path) -> None:
    """نظامٌ أُوقِفَ بمستوى `halt` يبقى موقوفًا في عمليّةٍ جديدة."""
    wrote = _run_in_fresh_process(
        db_path, "canary.activate_kill_switch('halt', 'إثباتُ إدامةٍ', 'step19')"
    )
    assert isinstance(wrote, dict) and wrote["level"] == "halt"

    read = _run_in_fresh_process(db_path, "canary.get_system_status()")
    assert isinstance(read, dict)
    assert read["level"] == "halt", "الإقلاعُ رفعَ الإيقافَ — نقضٌ لقرارِ المالكِ في Q-39 (أ)."
    assert read["reason"] == "إثباتُ إدامةٍ"
    assert read["activated_by"] == "step19"


def test_halt_still_blocks_execution_after_restart(db_path: Path) -> None:
    """الإدامةُ ليست حقلًا في جدولٍ فحسب: الحجبُ نفسُه يبقى بعدَ الإقلاع."""
    _run_in_fresh_process(
        db_path, "canary.activate_kill_switch('halt', 'حجبٌ دائمٌ', 'step19')"
    )
    assert _run_in_fresh_process(db_path, "canary.is_system_halted()") is True
    assert _run_in_fresh_process(db_path, "canary.is_execution_blocked()") is True


def test_reset_is_the_only_way_back_to_normal(db_path: Path) -> None:
    """الرفعُ فعلٌ صريحٌ — والنتيجةُ تنجو هي أيضًا لئلّا يعودَ الإيقافُ من نفسِه."""
    _run_in_fresh_process(
        db_path, "canary.activate_kill_switch('halt', 'ثمّ يُرفَعُ', 'step19')"
    )
    lifted = _run_in_fresh_process(db_path, "canary.reset_kill_switch()")
    assert isinstance(lifted, dict) and lifted["level"] == "normal"

    after = _run_in_fresh_process(db_path, "canary.get_system_status()")
    assert isinstance(after, dict) and after["level"] == "normal"
    assert after["activated_at"] is None


def test_degraded_level_survives_too(db_path: Path) -> None:
    """ليست النجاةُ خاصّةً بـ`halt`: كلُّ مستوًى مكتوبٍ حالةُ دولةٍ لا حالةُ عمليّة."""
    _run_in_fresh_process(
        db_path, "canary.activate_kill_switch('degraded', 'تدهورٌ', 'step19')"
    )
    blocked = _run_in_fresh_process(db_path, "canary.is_execution_blocked('sql_query')")
    assert blocked is True
    allowed = _run_in_fresh_process(db_path, "canary.is_execution_blocked('chart_generate')")
    assert allowed is False


def test_human_approval_of_a_promotion_survives_a_restart(db_path: Path) -> None:
    """إذنُ الإنسانِ يبقى مقروءًا بعدَ الإقلاعِ — وإلّا فلا أثرَ لموافقتِه يُقاس."""
    created = _run_in_fresh_process(db_path, "canary.create_promotion('step19-model')")
    assert isinstance(created, dict)
    promotion_id = created["promotion_id"]

    approved = _run_in_fresh_process(
        db_path,
        f"canary.check_gate({promotion_id!r}, 'human_approval', True, 'أذِنَ المالك')",
    )
    assert isinstance(approved, dict)
    assert approved["gates"]["human_approval"]["status"] == "passed"

    read = _run_in_fresh_process(db_path, f"canary.get_promotion({promotion_id!r})")
    assert isinstance(read, dict), "طلبُ الترقيةِ زالَ بإعادةِ التشغيل."
    assert read["gates"]["human_approval"]["status"] == "passed"
    assert read["gates"]["human_approval"]["notes"] == "أذِنَ المالك"
    assert read["model_id"] == "step19-model"


def test_a_failed_gate_stays_failed_after_restart(db_path: Path) -> None:
    """بوّابةٌ سقطَت لا تُنسى: الحالةُ `failed` مكتوبةٌ لا محسوبةٌ في الذاكرة."""
    created = _run_in_fresh_process(db_path, "canary.create_promotion('step19-fail')")
    assert isinstance(created, dict)
    promotion_id = created["promotion_id"]
    _run_in_fresh_process(
        db_path, f"canary.check_gate({promotion_id!r}, 'canary', False, 'سقطَت')"
    )

    read = _run_in_fresh_process(db_path, f"canary.get_promotion({promotion_id!r})")
    assert isinstance(read, dict)
    assert read["status"] == "failed"
    assert read["gates"]["canary"]["status"] == "failed"


def test_promotions_are_listed_from_the_table_not_from_memory(db_path: Path) -> None:
    """القائمةُ تُقرأُ من الجدولِ: عمليّةٌ تكتبُ وعمليّةٌ أخرى ترى ما كُتِب."""
    _run_in_fresh_process(db_path, "canary.create_promotion('step19-a')")
    _run_in_fresh_process(db_path, "canary.create_promotion('step19-b')")
    listed = _run_in_fresh_process(db_path, "canary.list_promotions()")
    assert isinstance(listed, list)
    models = sorted(entry["model_id"] for entry in listed)
    assert models == ["step19-a", "step19-b"]


def test_the_module_keeps_no_mutable_state_of_its_own() -> None:
    """لا قاموسَ حالةٍ ولا قائمةَ ترقياتٍ في الوحدةِ — وإلّا عادَ التطايرُ بابًا خلفيًّا."""
    module = SERVICES_SRC / "amos_federation" / "services" / "governance" / "canary.py"
    source = module.read_text(encoding="utf-8")
    assert "_system_state = {" not in source
    assert "_promotions: list" not in source
    assert "T4-DURABILITY: WIRED_DURABLE" in source
    assert "Q-39" in source
