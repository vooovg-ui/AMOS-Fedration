"""
حرسُ إغلاقِ رباطِ المُولِّداتِ — «وجهُ `--check` يُشغَّلُ على الشجرةِ الحقيقيّةِ» يُقاسُ لا يُروى
الهدف: إنفاذُ أنَّ عددَ المُولِّداتِ التي تكتُبُ أثرًا في الشجرةِ وتُعلِنُ وجهَ `--check` بلا رباطٍ مقيسٍ **لا يعلو**، وأنَّ الرباطَ القائمَ **لا ينقُصُ**، وأنَّ القياسَ يرى العَطبَ على شجرةٍ مصنوعةٍ ويرى عكسَه.
النطاق: tools/governance/generator_settlement_closure.py — القياسُ ووجهُ `--check` وحدَهما · والرقمُ المُعلَنُ في `DISCOVERIES.md`
المالك: tests/governance/
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

العَطبُ المقيسُ (`DISC-051`):
    الفحصُ الذي يُثبِتُ استقرارَ المُولِّدِ على المستودعِ الحقيقيِّ يُسمّي ثلاثةَ مُولِّداتٍ
    بأسمائِها نصًّا، فمُولِّدٌ جديدٌ يُضافُ إلى `tools/` لا يدخُلُ الحرسَ **ولا يُبلَّغُ عن
    غيابِه**. وغيابُ الرباطِ لم يكُنْ يُقاسُ أصلًا: قِيسَ في `W-129` أنَّ إحدى عشرةَ أداةً
    تكتُبُ أثرًا وتُعلِنُ `--check`، ولا يُشغَّلُ وجهُها على الجذرِ الحقيقيِّ إلّا لأربعٍ.

ولماذا يُقاسُ نحوًا لا نصًّا:
    أوّلُ نسخةٍ من الأداةِ قاسَتِ الكتابةَ **نصًّا** فعَدَّت نفسَها مُولِّدًا لأنَّ ترويستَها
    تحكي عن الكتابةِ — حكمٌ على ذِكرٍ في نثرٍ. فصارَ القياسُ من شجرةِ التحليلِ، وهذا
    الحرسُ يُثبِتُ ذلك بشجرةٍ فيها أداةٌ تذكُرُ الكتابةَ في ترويستِها ولا تكتُبُ.

حدُّ الحرسِ — مُعلَنٌ لا مطويٌّ:
    - يقيسُ أنَّ الوجهَ **يُشغَّلُ على الشجرةِ الحقيقيّةِ**، لا أنَّ ما يقيسُه صادقٌ ولا أنَّه يُسقِطُ بحقٍّ.
    - والسبعةُ غيرُ المربوطةِ **لا تُبَرَّأُ**: المُنجَزُ منعُ نموِّها لا ربطُها.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

#: علاماتٌ لا تجتمعُ إلّا في جذرِ هذا المستودعِ — نُسخَتُها الحاكمةُ في
#: `tools/governance/repo_root.py`، وتُعادُ هنا لأنَّ تحميلَ ذاكَ الملفِّ نفسِه
#: يحتاجُ الجذرَ أوّلًا. وتباعُدُهما دَينٌ مُعلَنٌ لا مطويٌّ: يُحرَسُ بفحصٍ أدناه.
ROOT_MARKERS = ("PROJECT_STATE.md", "docs/governance/work/THE_ROADMAP.md")


def _discover_root(start: Path) -> Path:
    """جذرُ القياسِ يُعرَفُ **بعلامةٍ** لا بعُمقٍ مكتوبٍ (`DISC-041`).

    فـ`parents[N]` يُثبِّتُ محلَّ القياسِ برقمٍ: يُنقَلُ الملفُّ فيُقاسُ مجلَّدٌ آخرُ
    بلا أيِّ خطأٍ، ويُخرَجُ رمزُ صفرٍ على شجرةٍ لم تُقصَدْ.
    """
    origin = start.resolve()
    for candidate in (origin, *origin.parents):
        if candidate.is_dir() and all(
            (candidate / marker).exists() for marker in ROOT_MARKERS
        ):
            return candidate
    raise RuntimeError(
        f"لم تُوجَدْ علامةُ جذرٍ ({' · '.join(ROOT_MARKERS)}) صعودًا من {origin} "
        "— ولا يُخمَّنُ جذرٌ"
    )


REPO_ROOT = _discover_root(Path(__file__))
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "generator_settlement_closure.py"

_SPEC = importlib.util.spec_from_file_location("amos_generator_settlement", TOOL_PATH)
if _SPEC is None or _SPEC.loader is None:  # pragma: no cover - عَطبُ تحميلٍ لا سلوكٌ
    raise ImportError(f"تعذّرَ تحميلُ الأداةِ من {TOOL_PATH}")
closure = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(closure)

BASELINE_LINE = (
    "\nملاحظةٌ · GENERATOR_SETTLEMENT_BASELINE: "
    "generators={generators} bound={bound} unbound={unbound}\n"
)

#: أداةٌ تكتُبُ أثرًا وتُعلِنُ وجهَ `--check` — مُولِّدٌ بحقٍّ.
GENERATOR_SOURCE = '''\
"""أداةٌ تكتُبُ أثرًا."""
import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        Path("out.md").write_text("أثرٌ\\n", encoding="utf-8")
    return 0
'''

#: أداةٌ **تحكي** عن الكتابةِ في ترويستِها ولا تكتُبُ — عينُ العَطبِ الأوّلِ.
PROSE_ONLY_SOURCE = '''\
"""أداةٌ تقيسُ غيرَها.

تقرأُ الأدواتَ التي تكتُبُ أثرًا بـ`write_text(` أو `json.dump(` وتُعلِنُ `--check`.
"""
import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.parse_args()
    return 0
'''

#: أداةٌ تكتُبُ ولا تُعلِنُ وجهًا — ليست مُولِّدًا بحدِّ الأداةِ المُعلَنِ.
WRITER_WITHOUT_FACE_SOURCE = '''\
"""أداةٌ تكتُبُ بلا وجهِ استقرارٍ."""
from pathlib import Path


def main() -> int:
    Path("out.md").write_text("أثرٌ\\n", encoding="utf-8")
    return 0
'''

#: فحصٌ يُشغِّلُ الوجهَ على الجذرِ الحقيقيِّ — رباطٌ مقيسٌ.
BINDING_TEST_SOURCE = '''\
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools" / "generator_one.py"


def test_settled() -> None:
    result = subprocess.run(
        [sys.executable, str(TOOL), "--check"],
        cwd=str(REPO_ROOT), capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0
'''

#: فحصٌ يُشغِّلُ الوجهَ على شجرةٍ مؤقَّتةٍ — ليس رباطًا على المستودعِ.
TEMPORARY_TEST_SOURCE = '''\
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL = REPO_ROOT / "tools" / "generator_one.py"


def test_on_a_temporary_tree(tmp_path: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(TOOL), "--check"],
        cwd=str(tmp_path), capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0
'''

#: فحصٌ يذكُرُ الأداةَ ولا يُشغِّلُ وجهَها — ذِكرٌ لا رباطٌ.
MENTION_ONLY_TEST_SOURCE = '''\
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_the_tool_exists() -> None:
    assert (REPO_ROOT / "tools" / "generator_one.py").exists()
'''

#: فحصٌ يُشغِّلُ وجهَ أدواتٍ من قائمةِ `parametrize` — الرباطُ يُحَلُّ من الزينةِ.
PARAMETRIZED_TEST_SOURCE = '''\
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "tools"


@pytest.mark.parametrize("tool", ["generator_one", "generator_two"])
def test_settled(tool: str) -> None:
    result = subprocess.run(
        [sys.executable, str(TOOLS / f"{tool}.py"), "--check"],
        cwd=str(REPO_ROOT), capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0
'''


def _seed_tree(
    tmp_path: Path,
    tools: dict[str, str] | None = None,
    tests: dict[str, str] | None = None,
    baseline: str | None = None,
) -> Path:
    """شجرةٌ مؤقَّتةٌ تحملُ أدواتِها وفحوصَها ورقمَها المُعلَنَ — لا المستودعُ الحقيقيُّ.

    وتُعادُ **قيمةً واحدةً** لا زوجًا مُفكَّكًا: حرسُ مواضعِ القياسِ يقتفي اسمَ الشجرةِ
    المؤقَّتةِ عبرَ الإسنادِ إلى اسمٍ مفردٍ، والتفكيكُ يُخفي الاسمَ عنه فيُقرأُ موضعُ
    القياسِ «مستودعًا حقيقيًّا» وهو مؤقَّتٌ.
    """
    tree = tmp_path / "repo"
    (tree / "tools").mkdir(parents=True)
    (tree / "tests" / "governance").mkdir(parents=True)
    (tree / "docs" / "governance" / "work").mkdir(parents=True)
    for name, source in (tools or {}).items():
        (tree / "tools" / name).write_text(source, encoding="utf-8")
    for name, source in (tests or {}).items():
        (tree / "tests" / "governance" / name).write_text(source, encoding="utf-8")
    declared = baseline if baseline is not None else BASELINE_LINE.format(
        generators=1, bound=0, unbound=1
    )
    (tree / "docs" / "governance" / "work" / "DISCOVERIES.md").write_text(
        "# سجلُّ الاكتشافاتِ\n" + declared, encoding="utf-8"
    )
    return tree


# ── تعريفُ المُولِّدِ: نداءٌ في شِفرةٍ لا ذِكرٌ في نثرٍ ──────────────────────────


def test_a_writing_tool_with_a_check_face_is_a_generator(tmp_path: Path) -> None:
    """كتابةٌ في الشجرةِ مع وجهِ `--check` = مُولِّدٌ يُقاسُ."""
    tree = _seed_tree(tmp_path, tools={"generator_one.py": GENERATOR_SOURCE})
    assert set(closure.generators(tree)) == {"generator_one"}


def test_prose_about_writing_is_not_a_write(tmp_path: Path) -> None:
    """أداةٌ تحكي عن الكتابةِ في ترويستِها لا تُعَدُّ مُولِّدًا — عينُ العَطبِ الأوّلِ.

    وهذا هو الفرقُ بينَ القياسِ النحويِّ والنصّيِّ: النسخةُ الأولى من الأداةِ عَدَّت
    نفسَها مُولِّدًا لهذا السببِ بعينِه.
    """
    tree = _seed_tree(tmp_path, tools={"prose_only.py": PROSE_ONLY_SOURCE})
    assert closure.generators(tree) == {}


def test_a_writer_without_a_check_face_is_not_a_generator(tmp_path: Path) -> None:
    """الكتابةُ وحدَها لا تكفي: الحرسُ يقيسُ رباطَ **وجهِ الاستقرارِ**."""
    tree = _seed_tree(tmp_path, tools={"writer.py": WRITER_WITHOUT_FACE_SOURCE})
    assert closure.generators(tree) == {}


def test_json_dump_counts_as_writing_an_artifact(tmp_path: Path) -> None:
    """`json.dump` كتابةٌ في الشجرةِ كما `write_text` — الصيغةُ لا تُغيِّرُ الحكمَ."""
    source = (
        '"""أداةٌ تكتُبُ أثرًا بصيغةٍ أخرى."""\n'
        "import argparse\n"
        "import json\n\n\n"
        "def main() -> int:\n"
        "    parser = argparse.ArgumentParser()\n"
        '    parser.add_argument("--check", action="store_true")\n'
        "    parser.parse_args()\n"
        '    with open("out.json", "w", encoding="utf-8") as handle:\n'
        "        json.dump({}, handle)\n"
        "    return 0\n"
    )
    tree = _seed_tree(tmp_path, tools={"dumper.py": source})
    assert set(closure.generators(tree)) == {"dumper"}


# ── تعريفُ الرباطِ: موضعُ نداءٍ على الجذرِ الحقيقيِّ ───────────────────────────


def test_a_real_root_check_call_binds_the_generator(tmp_path: Path) -> None:
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        tests={"test_binding.py": BINDING_TEST_SOURCE},
    )
    assert set(closure.settlement_sites(tree)) == {"generator_one"}
    assert closure.unbound_generators(tree) == []


def test_a_temporary_tree_call_is_not_a_binding(tmp_path: Path) -> None:
    """وجهٌ يُشغَّلُ على شجرةٍ مؤقَّتةٍ لا يُثبِتُ طزاجةَ أثرِ المستودعِ."""
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        tests={"test_temporary.py": TEMPORARY_TEST_SOURCE},
    )
    assert closure.settlement_sites(tree) == {}
    assert closure.unbound_generators(tree) == ["generator_one"]


def test_mentioning_the_tool_is_not_a_binding(tmp_path: Path) -> None:
    """ذِكرُ اسمِ الأداةِ في فحصٍ لا يشتري رباطًا — الرباطُ نداءٌ لا كلمةٌ."""
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        tests={"test_mention.py": MENTION_ONLY_TEST_SOURCE},
    )
    assert closure.settlement_sites(tree) == {}


def test_parametrized_tool_names_are_resolved(tmp_path: Path) -> None:
    """قائمةُ `parametrize` تُحَلُّ فيُقرأُ رباطُ كلِّ أداةٍ فيها لا واحدةٍ."""
    tree = _seed_tree(
        tmp_path,
        tools={
            "generator_one.py": GENERATOR_SOURCE,
            "generator_two.py": GENERATOR_SOURCE,
        },
        tests={"test_parametrized.py": PARAMETRIZED_TEST_SOURCE},
    )
    assert set(closure.settlement_sites(tree)) == {"generator_one", "generator_two"}


# ── السقّاطةُ: لا تعلو ولا تُترَكُ رخوةً ──────────────────────────────────────


def test_growth_in_the_gap_fails(tmp_path: Path) -> None:
    """مُولِّدٌ جديدٌ بلا رباطٍ يُسقِطُ الوجهَ — وهذا عينُ ما لم يكُنْ يُقاسُ."""
    tree = _seed_tree(
        tmp_path,
        tools={
            "generator_one.py": GENERATOR_SOURCE,
            "generator_two.py": GENERATOR_SOURCE,
        },
        baseline=BASELINE_LINE.format(generators=1, bound=0, unbound=1),
    )
    code, problems = closure.verdict(tree)
    assert code == 1
    assert any("SETTLEMENT_GAP_GROWTH" in problem for problem in problems)
    assert any("generator_two" in problem for problem in problems)


def test_a_slack_baseline_fails(tmp_path: Path) -> None:
    """انخفاضُ المقيسِ بلا خفضِ المُعلَنِ يُسقِطُ — فلا سقّاطةَ رخوةً تُخفي عودةَ العَطبِ."""
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        tests={"test_binding.py": BINDING_TEST_SOURCE},
        baseline=BASELINE_LINE.format(generators=1, bound=1, unbound=1),
    )
    code, problems = closure.verdict(tree)
    assert code == 1
    assert any("STALE_SETTLEMENT_BASELINE" in problem for problem in problems)


def test_losing_a_binding_fails(tmp_path: Path) -> None:
    """رباطٌ قائمٌ يُحذَفُ أو يُعمى يُسقِطُ — حذفُ حرسٍ إخفاءُ فشلٍ لا إصلاحُه."""
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        baseline=BASELINE_LINE.format(generators=1, bound=1, unbound=0),
    )
    code, problems = closure.verdict(tree)
    assert code == 1
    assert any("SETTLEMENT_BINDING_LOSS" in problem for problem in problems)


def test_an_undeclared_generator_count_fails(tmp_path: Path) -> None:
    """عددُ المُولِّداتِ يُطابِقُ المُعلَنَ تمامًا فلا يُحذَفُ مُولِّدٌ في الظلِّ."""
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        tests={"test_binding.py": BINDING_TEST_SOURCE},
        baseline=BASELINE_LINE.format(generators=2, bound=1, unbound=0),
    )
    code, problems = closure.verdict(tree)
    assert code == 1
    assert any("GENERATOR_COUNT_UNDECLARED" in problem for problem in problems)


def test_a_settled_tree_passes(tmp_path: Path) -> None:
    """وشجرةٌ رباطُها تامٌّ تمرُّ — فلا تُقاسُ حُمرةٌ بلا فرقٍ."""
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        tests={"test_binding.py": BINDING_TEST_SOURCE},
        baseline=BASELINE_LINE.format(generators=1, bound=1, unbound=0),
    )
    assert closure.verdict(tree) == (0, [])


# ── الرقمُ المُعلَنُ: مصدرٌ واحدٌ لا يُخمَّنُ ─────────────────────────────────


def test_a_missing_baseline_line_is_refused(tmp_path: Path) -> None:
    tree = _seed_tree(tmp_path, tools={"generator_one.py": GENERATOR_SOURCE}, baseline="")
    with pytest.raises(closure.BaselineRecordMissing):
        closure.declared_baseline(tree)


def test_a_duplicated_baseline_line_is_refused(tmp_path: Path) -> None:
    """رقمانِ مُعلَنانِ = مصدرا حقيقةٍ، فلا يُختارُ أحدُهما بالتقديرِ."""
    twice = BASELINE_LINE.format(generators=1, bound=0, unbound=1) + BASELINE_LINE.format(
        generators=2, bound=0, unbound=2
    )
    tree = _seed_tree(
        tmp_path, tools={"generator_one.py": GENERATOR_SOURCE}, baseline=twice
    )
    with pytest.raises(closure.BaselineRecordMissing):
        closure.declared_baseline(tree)


def test_an_incomplete_baseline_line_is_refused(tmp_path: Path) -> None:
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        baseline="\nملاحظةٌ · GENERATOR_SETTLEMENT_BASELINE: generators=1 bound=0\n",
    )
    with pytest.raises(closure.BaselineRecordMissing):
        closure.declared_baseline(tree)


# ── القياسُ لا يُتخطّى بصمتٍ ──────────────────────────────────────────────────


def test_an_unparsable_tool_stops_the_measure(tmp_path: Path) -> None:
    """ملفٌّ لا يُحَلُّ نحوًا عَطبُ قياسٍ يُرفَعُ — وتخطّيهِ يُقرأُ انخفاضًا في العَطبِ."""
    tree = _seed_tree(tmp_path, tools={"broken.py": "def main(:\n"})
    with pytest.raises(closure.SourceUnreadable):
        closure.generators(tree)


def test_an_unreadable_tool_stops_the_measure(tmp_path: Path) -> None:
    """بايتاتٌ ليست نصًّا تُسقِطُ القياسَ ولا تُتخطّى."""
    tree = _seed_tree(tmp_path)
    (tree / "tools" / "binary.py").write_bytes(b"\xff\xfe\x00\x01")
    with pytest.raises(closure.SourceUnreadable):
        closure.generators(tree)


def test_an_unparsable_test_stops_the_binding_measure(tmp_path: Path) -> None:
    tree = _seed_tree(
        tmp_path,
        tools={"generator_one.py": GENERATOR_SOURCE},
        tests={"test_broken.py": "def test_x(:\n"},
    )
    with pytest.raises(closure.SourceUnreadable):
        closure.settlement_sites(tree)


# ── المستودعُ الحقيقيُّ ───────────────────────────────────────────────────────


def test_the_repository_matches_its_declared_baseline() -> None:
    """المقيسُ على المستودعِ الحقيقيِّ يُطابِقُ رقمَه المُعلَنَ — REAL_TREE_ON_PURPOSE."""
    assert closure.measure(REPO_ROOT) == closure.declared_baseline(REPO_ROOT)


def test_the_check_face_passes_on_the_repository() -> None:
    """وجهُ `--check` يُشغَّلُ على المستودعِ الحقيقيِّ ويمرُّ — REAL_TREE_ON_PURPOSE."""
    result = subprocess.run(  # noqa: S603 — REAL_TREE_ON_PURPOSE: الحكمُ على المستودعِ مقصودٌ
        [sys.executable, str(TOOL_PATH), "--check"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, (
        "رباطُ المُولِّداتِ على المستودعِ لا يُطابِقُ المُعلَنَ:\n"
        f"{result.stdout}\n{result.stderr}"
    )


def test_the_root_markers_match_the_governing_copy() -> None:
    """علاماتُ الجذرِ المُعادةُ هنا تُطابِقُ نُسخَتَها الحاكمةَ — فلا مصدرا حقيقةٍ."""
    finder_path = REPO_ROOT / "tools" / "governance" / "repo_root.py"
    spec = importlib.util.spec_from_file_location("amos_root_finder", finder_path)
    assert spec is not None and spec.loader is not None
    finder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(finder)
    assert tuple(finder.ROOT_MARKERS) == ROOT_MARKERS, (
        "علاماتُ الجذرِ تباعدَت عن نُسخَتِها الحاكمةِ — تُوحَّدُ ولا يُخفَّفُ الفحصُ"
    )


def test_the_measured_gap_is_named_not_only_counted() -> None:
    """غيرُ المربوطِ يُسمّى بأسمائِه — فالعددُ وحدَه لا يُراجَعُ."""
    gap = closure.unbound_generators(REPO_ROOT)
    assert gap, "لو خلا الفراغُ لوجبَ خفضُ الرقمِ المُعلَنِ لا حذفُ هذا الفحصِ"
    assert set(gap).isdisjoint(set(closure.settlement_sites(REPO_ROOT)))
