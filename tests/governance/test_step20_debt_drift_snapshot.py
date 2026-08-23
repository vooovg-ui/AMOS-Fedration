"""حرسُ الخطوةِ 20 — لقطةُ انحرافِ الدَّينِ تُسجَّلُ بشرطٍ لا بمزاجٍ.

الهدف:
    الدَّينُ السياديُّ (كتاباتٌ عامّةٌ لا تعبرُ الحدَّ) يرتفعُ حينَ يُضافُ سطحُ
    كتابةٍ جديدٌ في عملٍ هندسيّ. وقد وقعَ ذلك مقيسًا في `W-031`: طبقةُ الإدامةِ
    (‏`Q-39 أ`) رفعَتِ الدَّينَ **168 ← 179**، فسقطَ حارسُ الانحرافِ في
    `test_step7_factory_surfaces.py` — وكانَ محقًّا.
    والمخرَجُ المشروعُ من ذلكَ **واحدٌ**: تُسجَّلُ لقطةُ قياسٍ منسوبةٌ إلى العملِ
    بسببٍ مكتوبٍ (`--record-work`). وما يحرسُه هذا الملفُّ أن لا يصيرَ ذلكَ البابُ
    بابَ تجميلٍ: لقطةٌ بلا سببٍ، أو بلا قيدٍ في دفترِ الإنجازِ، أو مكتوبةٌ فوقَ
    لقطةٍ سابقةٍ لتُخفى زيادةٌ جديدة.

النطاق:
    `tools/audit/decision_gate.py --record-work` وحدَه — مساراتُ **الرفضِ** فقط.
    ولا يُشغِّلُ هذا الحرسُ جردًا حقيقيًّا ولا يكتبُ في دفترِ اللقطاتِ: التحقُّقُ
    كلُّه يقعُ قبلَ القياسِ في الأداةِ نفسِها، فالفحصُ سريعٌ ولا يُلوِّثُ قياسًا.

المالك:
    `tests/governance` — حرّاسُ الحوكمةِ في المستودع.

تاريخ الإنشاء: 2026-08-23
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GATE_TOOL = REPO_ROOT / "tools" / "audit" / "decision_gate.py"
LEDGER_PATH = (
    REPO_ROOT / "docs" / "audit" / "measurements" / "decision_gate_ledger.json"
)
GOOD_REASON = "سببٌ مكتوبٌ طويلٌ بما يكفي للمُساءَلةِ لا كلمةٌ واحدة"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(GATE_TOOL), *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def test_the_option_exists_and_is_documented() -> None:
    """البابُ مُعلَنٌ في مساعدةِ الأداةِ وفي ترويستِها — لا خيارٌ خفيٌّ."""
    helped = _run("--help")
    assert helped.returncode == 0
    assert "--record-work" in helped.stdout
    text = GATE_TOOL.read_text(encoding="utf-8")
    assert "--record-work" in text
    assert "COMPLETION_LEDGER" in text, "الأداةُ لا تربطُ اللقطةَ بدفترِ الإنجاز"


def test_a_snapshot_without_a_written_reason_is_refused() -> None:
    """لا لقطةَ بلا سببٍ مكتوبٍ — والاعتذارُ القصيرُ ليسَ سببًا."""
    empty = _run("--record-work", "W-031")
    assert empty.returncode == 1, empty.stdout
    assert "سبب" in empty.stdout
    short = _run("--record-work", "W-031", "--reason", "زيادةٌ")
    assert short.returncode == 1, short.stdout


def test_a_snapshot_for_an_unledgered_work_is_refused() -> None:
    """عملٌ بلا قيدٍ في دفترِ الإنجازِ لا لقطةَ له — فلا لقطةَ يتيمةً بلا مُساءَلة."""
    orphan = _run("--record-work", "W-999", "--reason", GOOD_REASON)
    assert orphan.returncode == 1, orphan.stdout
    assert "W-999" in orphan.stdout


def test_a_malformed_work_id_is_refused() -> None:
    """الصيغةُ محروسةٌ: `Q-39` قرارٌ لا عملٌ، ولا يُخلَطُ البابانِ."""
    wrong = _run("--record-work", "Q-39", "--reason", GOOD_REASON)
    assert wrong.returncode == 1, wrong.stdout
    assert "W-NNN" in wrong.stdout


def test_the_ledger_keeps_every_snapshot_named_and_dated() -> None:
    """كلُّ لقطةٍ مسجَّلةٍ منسوبةٌ ومؤرَّخةٌ — ولا لقطةَ بلا دَينٍ مقيس."""
    snapshots = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))["snapshots"]
    assert snapshots, "لا لقطةَ في الدفتر"
    for snap in snapshots:
        assert snap.get("decision"), "لقطةٌ بلا نسبةٍ إلى قرارٍ أو عمل"
        assert snap.get("recorded_at"), "لقطةٌ بلا تاريخ"
        assert isinstance(snap.get("debt"), int), "لقطةٌ بلا دَينٍ مقيس"
        if str(snap["decision"]).startswith("W-"):
            assert len(str(snap.get("reason", ""))) >= 20, (
                f"لقطةُ عملٍ بلا سببٍ مكتوبٍ: {snap['decision']} — "
                "وهذا هو البابُ الذي يُحرَسُ هنا."
            )
