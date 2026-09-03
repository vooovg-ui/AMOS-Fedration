"""
حرسُ مقامِ الخُضرةِ — «كم قرأَت؟» سؤالٌ يُقاسُ لا يُفترَضُ
الهدف: إنفاذُ أنَّ عددَ جملِ النجاحِ **الكلّيّةِ الحكمِ بلا مقامٍ مقيسٍ** لا يعلو، وأنَّ الجملَ التي تُرفِقُ مقامَها لا تنقُصُ، وأنَّ القياسَ يرى العَطبَ على شجرةٍ مصنوعةٍ ويرى عكسَه.
النطاق: tools/governance/green_denominator_closure.py — القياسُ ووجهُ `--check` وحدَهما · والرقمُ المُعلَنُ في `DISCOVERIES.md`
المالك: tests/governance/
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

العَطبُ المقيسُ (`DISC-053`):
    بوّابةٌ تُعلِنُ عندَ النجاحِ حكمًا كلّيًّا ولا تقولُ كم قرأَت، فـ«قِيسَ ألفٌ فلم
    يُخالِفْ واحدٌ» و«قِيسَ صفرٌ» يُطبَعانِ بحرفٍ واحدٍ ورمزِ خروجٍ واحدٍ. وذاكَ حدَثَ
    فعلًا في `DISC-052`: ضاقَ مقامُ بوّابةٍ إلى دعوَيَينِ وبقيَ حكمُها الكلّيُّ يُطبَعُ.

حدُّ الحرسِ — مُعلَنٌ لا مطويٌّ:
    - يقيسُ **شكلَ** الجملةِ لا صدقَ رقمِها: جملةٌ تُرفِقُ عددًا محسوبًا من مجموعةٍ
      خاطئةٍ تُقرأُ «بمقامٍ». فالمُنجَزُ منعُ الحكمِ الكلّيِّ الأصمِّ.
    - والسبعَ عشرةَ الصامتةُ **لا تُبَرَّأُ**: المُنجَزُ منعُ نموِّها وتسميتُها.
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
    """جذرُ القياسِ يُعرَفُ **بعلامةٍ** لا بعُمقٍ مكتوبٍ (`DISC-041`)."""
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
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "green_denominator_closure.py"

_SPEC = importlib.util.spec_from_file_location("amos_green_denominator", TOOL_PATH)
if _SPEC is None or _SPEC.loader is None:  # pragma: no cover - عَطبُ تحميلٍ لا سلوكٌ
    raise ImportError(f"تعذّرَ تحميلُ الأداةِ من {TOOL_PATH}")
closure = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(closure)

BASELINE_LINE = (
    "\nملاحظةٌ · GREEN_DENOMINATOR_BASELINE: "
    "tools={tools} green_sentences={green_sentences} universal={universal} "
    "bounded={bounded} unbounded={unbounded}\n"
)

#: جملةُ نجاحٍ كلّيّةُ الحكمِ تُرفِقُ كمًّا محسوبًا — «بمقامٍ».
BOUNDED_SOURCE = '''\
"""أداةٌ تقولُ كم قرأَت."""


def main(rows: list[str]) -> int:
    print(f"[GATE] ✓ كلُّ ما قِيسَ سليمٌ: {len(rows)} صفًّا")
    return 0
'''

#: جملةُ نجاحٍ كلّيّةُ الحكمِ بلا كمٍّ محسوبٍ — عينُ العَطبِ.
UNBOUNDED_SOURCE = '''\
"""أداةٌ تُعلِنُ الكُلّيّةَ صامتةً."""


def main() -> int:
    print("[GATE] ✓ كلُّ شيءٍ سليمٌ — لا مخالفة.")
    return 0
'''

#: حكمٌ كلّيٌّ يُرفِقُ **رقمًا مكتوبًا حرفًا** لا كمًّا محسوبًا — ليس مقامًا.
LITERAL_DIGIT_SOURCE = '''\
"""أداةٌ تكتُبُ رقمَها حرفًا."""


def main() -> int:
    print("[GATE] ✓ كلُّ الـ12 صفًّا سليمٌ")
    return 0
'''

#: «✓» في تعليقٍ أو نصِّ وثيقةٍ — ليست جملةَ نجاحٍ تُطبَعُ.
MARK_NOT_PRINTED_SOURCE = '''\
"""أداةٌ ترويستُها تحمِلُ ✓ ولا تُطلِقُ جملةَ نجاحٍ.

مثالُ خرجٍ: ✓ كلُّ شيءٍ سليمٌ.
"""


def main() -> int:
    # ✓ كلُّ شيءٍ سليمٌ — تعليقٌ لا خرجٌ
    return 0
'''

#: جملةُ نجاحٍ ليست كلّيّةَ الحكمِ — تقريرُ عملٍ يُحصى إبلاغًا لا يُحاسَبُ.
NOT_UNIVERSAL_SOURCE = '''\
"""أداةٌ تُقرِّرُ ما فعلَت."""


def main(n: int) -> int:
    print(f"✓ كُتِبَت {n} بطاقةً")
    return 0
'''


def _seed_tree(
    tmp_path: Path,
    tools: dict[str, str] | None = None,
    baseline: str | None = None,
) -> Path:
    """شجرةٌ مؤقَّتةٌ تحملُ أدواتَها ورقمَها المُعلَنَ — لا المستودعُ الحقيقيُّ.

    وتُعادُ **قيمةً واحدةً** لا زوجًا مُفكَّكًا: حرسُ مواضعِ القياسِ يقتفي اسمَ الشجرةِ
    المؤقَّتةِ عبرَ الإسنادِ إلى اسمٍ مفردٍ، والتفكيكُ يُخفي الاسمَ عنه فيُقرأُ موضعُ
    القياسِ «مستودعًا حقيقيًّا» وهو مؤقَّتٌ.
    """
    tree = tmp_path / "repo"
    (tree / "tools").mkdir(parents=True)
    (tree / "docs" / "governance" / "work").mkdir(parents=True)
    for name, source in (tools or {}).items():
        (tree / "tools" / name).write_text(source, encoding="utf-8")
    declared = (
        baseline
        if baseline is not None
        else BASELINE_LINE.format(
            tools=len(tools or {}),
            green_sentences=0,
            universal=0,
            bounded=0,
            unbounded=0,
        )
    )
    (tree / "docs" / "governance" / "work" / "DISCOVERIES.md").write_text(
        "# سجلُّ الاكتشافاتِ\n" + declared, encoding="utf-8"
    )
    return tree


# ── ما هي جملةُ النجاحِ: خرجٌ يُطبَعُ لا حرفٌ في نثرٍ ──────────────────────────


def test_the_mark_in_prose_is_not_a_green_sentence(tmp_path: Path) -> None:
    """«✓» في ترويسةٍ أو تعليقٍ لا تُعَدُّ جملةَ نجاحٍ — الحكمُ على خرجٍ لا على ذِكرٍ."""
    tree = _seed_tree(tmp_path, tools={"quiet.py": MARK_NOT_PRINTED_SOURCE})
    assert closure.census(tree) == []


def test_a_non_universal_green_sentence_is_counted_but_not_charged(
    tmp_path: Path,
) -> None:
    """تقريرُ عملٍ يُحصى في جملِ النجاحِ ولا يُحاسَبُ على مقامٍ."""
    tree = _seed_tree(tmp_path, tools={"reporter.py": NOT_UNIVERSAL_SOURCE})
    counts = closure.measured_counts(tree)
    assert counts["green_sentences"] == 1
    assert counts["universal"] == 0
    assert closure.unbounded_sentences(tree) == []


# ── ما هو المقامُ: كمٌّ محسوبٌ لا رقمٌ مكتوبٌ ─────────────────────────────────


def test_a_computed_quantity_is_a_denominator(tmp_path: Path) -> None:
    tree = _seed_tree(tmp_path, tools={"bounded.py": BOUNDED_SOURCE})
    counts = closure.measured_counts(tree)
    assert (counts["universal"], counts["bounded"], counts["unbounded"]) == (1, 1, 0)


def test_a_universal_verdict_without_a_quantity_is_unbounded(tmp_path: Path) -> None:
    """عينُ العَطبِ: حكمٌ كلّيٌّ يُطبَعُ ولا يقولُ كم قرأَ."""
    tree = _seed_tree(tmp_path, tools={"silent.py": UNBOUNDED_SOURCE})
    gap = closure.unbounded_sentences(tree)
    assert [s.path for s in gap] == ["tools/silent.py"]


def test_a_literal_digit_is_not_a_denominator(tmp_path: Path) -> None:
    """رقمٌ مكتوبٌ حرفًا في الجملةِ لا يُشترى به مقامٌ — المقامُ يُحسَبُ لا يُكتَبُ."""
    tree = _seed_tree(tmp_path, tools={"literal.py": LITERAL_DIGIT_SOURCE})
    counts = closure.measured_counts(tree)
    assert (counts["bounded"], counts["unbounded"]) == (0, 1)


# ── السقّاطاتُ: لا تعلو ولا تُترَكُ رخوةً ─────────────────────────────────────


def test_growth_in_the_silent_verdicts_fails(tmp_path: Path) -> None:
    """جملةٌ كلّيّةٌ جديدةٌ بلا مقامٍ تُسقِطُ الوجهَ — وهذا عينُ ما لم يكُنْ يُقاسُ."""
    tree = _seed_tree(
        tmp_path,
        tools={"a.py": UNBOUNDED_SOURCE, "b.py": UNBOUNDED_SOURCE},
        baseline=BASELINE_LINE.format(
            tools=2, green_sentences=2, universal=2, bounded=0, unbounded=1
        ),
    )
    problems = closure.verdicts(tree)
    assert any("DENOMINATOR_GAP_GROWTH" in problem for problem in problems)
    assert any("tools/b.py" in problem for problem in problems)


def test_losing_a_denominator_fails(tmp_path: Path) -> None:
    """جملةٌ كانت تقولُ كم قرأَت فصارَت صامتةً تُسقِطُ — تراجُعٌ لا تنظيمٌ."""
    tree = _seed_tree(
        tmp_path,
        tools={"a.py": UNBOUNDED_SOURCE},
        baseline=BASELINE_LINE.format(
            tools=1, green_sentences=1, universal=1, bounded=1, unbounded=1
        ),
    )
    problems = closure.verdicts(tree)
    assert any("DENOMINATOR_LOSS" in problem for problem in problems)


def test_an_undeclared_universal_count_fails(tmp_path: Path) -> None:
    """عددُ الأحكامِ الكلّيّةِ يُطابِقُ المُعلَنَ تمامًا فلا يُحذَفُ حكمٌ في الظلِّ."""
    tree = _seed_tree(
        tmp_path,
        tools={"a.py": BOUNDED_SOURCE},
        baseline=BASELINE_LINE.format(
            tools=1, green_sentences=1, universal=2, bounded=1, unbounded=0
        ),
    )
    problems = closure.verdicts(tree)
    assert any("UNIVERSAL_COUNT_UNDECLARED" in problem for problem in problems)


def test_a_stale_measurement_base_fails(tmp_path: Path) -> None:
    """تغيُّرُ مقامِ القياسِ نفسِه (‏وحداتٌ · جملٌ) يُسقِطُ فلا يُقاسُ على قيدٍ متقادِمٍ."""
    tree = _seed_tree(
        tmp_path,
        tools={"a.py": BOUNDED_SOURCE, "b.py": MARK_NOT_PRINTED_SOURCE},
        baseline=BASELINE_LINE.format(
            tools=1, green_sentences=1, universal=1, bounded=1, unbounded=0
        ),
    )
    problems = closure.verdicts(tree)
    assert any("STALE_DENOMINATOR_BASELINE" in problem for problem in problems)


def test_a_matching_tree_passes(tmp_path: Path) -> None:
    """وشجرةٌ مُطابِقةٌ تمرُّ — فلا تُقاسُ حُمرةٌ بلا فرقٍ."""
    tree = _seed_tree(
        tmp_path,
        tools={"a.py": BOUNDED_SOURCE, "b.py": UNBOUNDED_SOURCE},
        baseline=BASELINE_LINE.format(
            tools=2, green_sentences=2, universal=2, bounded=1, unbounded=1
        ),
    )
    assert closure.verdicts(tree) == []


# ── الرقمُ المُعلَنُ: مصدرٌ واحدٌ لا يُخمَّنُ ─────────────────────────────────


def test_a_missing_baseline_line_is_refused(tmp_path: Path) -> None:
    tree = _seed_tree(tmp_path, tools={"a.py": BOUNDED_SOURCE}, baseline="")
    with pytest.raises(closure.BaselineRecordMissing):
        closure.declared_baseline(tree)


def test_a_duplicated_baseline_line_is_refused(tmp_path: Path) -> None:
    """رقمانِ مُعلَنانِ = مصدرا حقيقةٍ، فلا يُختارُ أحدُهما بالتقديرِ."""
    twice = BASELINE_LINE.format(
        tools=1, green_sentences=1, universal=1, bounded=1, unbounded=0
    ) + BASELINE_LINE.format(
        tools=2, green_sentences=2, universal=2, bounded=1, unbounded=1
    )
    tree = _seed_tree(tmp_path, tools={"a.py": BOUNDED_SOURCE}, baseline=twice)
    with pytest.raises(closure.BaselineRecordMissing):
        closure.declared_baseline(tree)


def test_an_incomplete_baseline_line_is_refused(tmp_path: Path) -> None:
    tree = _seed_tree(
        tmp_path,
        tools={"a.py": BOUNDED_SOURCE},
        baseline="\nملاحظةٌ · GREEN_DENOMINATOR_BASELINE: tools=1 green_sentences=1\n",
    )
    with pytest.raises(closure.BaselineRecordMissing):
        closure.declared_baseline(tree)


# ── القياسُ لا يُتخطّى بصمتٍ ──────────────────────────────────────────────────


def test_an_unparsable_unit_stops_the_measure(tmp_path: Path) -> None:
    """ملفٌّ لا يُحَلُّ نحوًا عَطبُ قياسٍ يُرفَعُ — وتخطّيهِ يُقرأُ انخفاضًا في العَطبِ."""
    tree = _seed_tree(tmp_path, tools={"broken.py": "def main(:\n"})
    with pytest.raises(closure.SourceUnreadable):
        closure.census(tree)


def test_an_unreadable_unit_stops_the_measure(tmp_path: Path) -> None:
    """بايتاتٌ ليست نصًّا تُسقِطُ القياسَ ولا تُتخطّى."""
    tree = _seed_tree(tmp_path)
    (tree / "tools" / "binary.py").write_bytes(b"\xff\xfe\x00\x01")
    with pytest.raises(closure.SourceUnreadable):
        closure.census(tree)


# ── المستودعُ الحقيقيُّ ───────────────────────────────────────────────────────


def test_the_repository_matches_its_declared_baseline() -> None:
    """المقيسُ على المستودعِ الحقيقيِّ يُطابِقُ رقمَه المُعلَنَ — REAL_TREE_ON_PURPOSE."""
    assert closure.measured_counts(REPO_ROOT) == closure.declared_baseline(REPO_ROOT)


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
        "مقامُ الخُضرةِ على المستودعِ لا يُطابِقُ المُعلَنَ:\n"
        f"{result.stdout}\n{result.stderr}"
    )


def test_the_guard_counts_its_own_green_sentence() -> None:
    """الحرسُ يُحصي نفسَه ويحمِلُ مقامَه — فقارئٌ يُعفي نفسَه يُعلِّمُ الإعفاءَ."""
    own = [
        sentence
        for sentence in closure.census(REPO_ROOT)
        if sentence.path == "tools/governance/green_denominator_closure.py"
    ]
    assert own, "جملةُ نجاحِ الحرسِ نفسِه غائبةٌ من العدِّ — الإعفاءُ يُبطِلُ الحرسَ"
    assert all(
        sentence.verdict == closure.UNIVERSAL_WITH_DENOMINATOR for sentence in own
    ), "جملةُ نجاحِ الحرسِ لا تحمِلُ مقامًا، فهو يُطالِبُ بما لا يفعلُ"


def test_the_measured_gap_is_named_not_only_counted() -> None:
    """الصامتُ يُسمّى بموضعِه — فالعددُ وحدَه لا يُراجَعُ."""
    gap = closure.unbounded_sentences(REPO_ROOT)
    assert gap, "لو خلا الفراغُ لوجبَ خفضُ الرقمِ المُعلَنِ لا حذفُ هذا الفحصِ"
    assert all(sentence.line > 0 for sentence in gap)
    assert len({(s.path, s.line) for s in gap}) == len(gap)


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
