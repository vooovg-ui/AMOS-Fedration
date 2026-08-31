"""فحوصُ سجلِّ طرقِ الإنفاذِ (W-080) — تُشغَّلُ في CI فتصيرُ الأداةُ مُنفَذةً.

الغرض:
    أن يُقاسَ حكمُ `tools/governance/enforcement_path_ledger.py` مرّتَينِ: في
    **شجرةٍ مؤقَّتةٍ** تُبنى بيدِ الفحصِ فيُرى كلُّ حكمٍ ورمزِ خروجٍ على حالةٍ
    مصنوعةٍ، وفي **الشجرةِ الحاضرةِ** فلا يكونُ الحكمُ صحيحًا في المختبرِ
    كاذبًا في المستودعِ. والفحوصُ على الشجرةِ الحاضرةِ هي عينُها طريقُ إنفاذِ
    الأداةِ (‏`COVERED_TEST`) لأنَّ `.github/workflows/ci.yml` مسارٌ مقفولٌ
    بـ`WI-023` وهو `IN_REVIEW` فلا خطوةَ تشغيلٍ تُضافُ في هذا البندِ.
المالك: tests/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-31
تاريخ آخر تعديل: 2026-08-31
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "governance"))

import enforcement_path_ledger as epl  # noqa: E402

TOOL_PATH = REPO_ROOT / "tools" / "governance" / "enforcement_path_ledger.py"

WORKFLOW = """name: ci
on: [push]
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - name: بوابة
        run: |
          python tools/governance/wired.py
          pytest tests/governance -q
"""

RUNNABLE = '''"""أداةٌ.

{decl}
"""
import sys


def main() -> int:
    return 1


if __name__ == "__main__":
    sys.exit(main())
'''

LIBRARY = '''"""مكتبةٌ بلا مدخلِ تشغيلٍ."""


def helper() -> int:
    return 0
'''

IMPORT_RUN = '''"""أداةٌ تعملُ عندَ الاستيرادِ.

{decl}
"""
import sys


def main() -> int:
    return 2


sys.exit(main())
'''

COVERING_TEST = '''"""فحصٌ يحكُمُ على الشجرةِ الحاضرةِ."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

import {stem}  # noqa: E402


def test_real_tree() -> None:
    assert REPO_ROOT.is_dir()
    assert {stem} is not None
'''


def build_tree(
    tmp_path: Path,
    tools: dict[str, str],
    tests: dict[str, str] | None = None,
    workflow: str | None = WORKFLOW,
) -> Path:
    """يبني شجرةً مؤقَّتةً: وظائفَ CI وأدواتٍ وفحوصًا — بلا مساسٍ بالمستودعِ."""
    root = tmp_path / "tree"
    for rel, text in tools.items():
        target = root / "tools" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    for rel, text in (tests or {}).items():
        target = root / "tests" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    if workflow is not None:
        wf = root / ".github" / "workflows"
        wf.mkdir(parents=True, exist_ok=True)
        (wf / "ci.yml").write_text(workflow, encoding="utf-8")
    return root


# ── التصنيفُ الساكنُ ─────────────────────────────────────────────────────────


def test_kind_classification_separates_entrypoint_import_and_library() -> None:
    """ثلاثةُ أنواعٍ لا نوعٌ واحدٌ — وهذا عينُ ما خلَطَه جردُ `W-077`."""
    assert epl.classify_kind(RUNNABLE.format(decl="")) == epl.KIND_ENTRYPOINT
    assert epl.classify_kind(IMPORT_RUN.format(decl="")) == epl.KIND_IMPORT_RUN
    assert epl.classify_kind(LIBRARY) == epl.KIND_LIBRARY


def test_unparsable_source_is_refused_not_read_as_library() -> None:
    """ملفٌّ معطوبٌ يُرفَعُ رفضًا، فلا يصيرُ سكوتُ المُحلِّلِ إعفاءً صامتًا."""
    with pytest.raises(epl.UnparsableSource):
        epl.classify_kind("def ملفٌّ معطوبٌ(:\n", "broken.py")


def test_verdict_capability_reads_exit_codes_not_prose() -> None:
    assert epl.is_verdict_capable("import sys\nsys.exit(1)\n") is True
    assert epl.is_verdict_capable("import sys\nsys.exit(0)\n") is False
    assert epl.is_verdict_capable("raise SystemExit(2)\n") is True
    assert epl.is_verdict_capable("print('أحكُمُ')\n") is False


def test_declaration_is_read_only_inside_the_declared_window() -> None:
    """الإعلانُ في الترويسةِ — لا في آخرِ الملفِّ حيثُ لا يراهُ قارئٌ."""
    header = RUNNABLE.format(decl="طريقُ الإنفاذ: LIBRARY · سببٌ")
    assert epl.read_declaration(header)[0] == "LIBRARY"
    buried = "\n" * (epl.HEADER_WINDOW_LINES + 5) + "# طريقُ الإنفاذ: LIBRARY"
    assert epl.read_declaration(buried) == ("", "")


# ── قياسُ الطريقِ ────────────────────────────────────────────────────────────


def test_ci_step_path_is_measured_from_run_blocks(tmp_path: Path) -> None:
    root = build_tree(tmp_path, {"governance/wired.py": RUNNABLE.format(decl="")})
    report = epl.measure(root)
    record = next(r for r in report.records if r.path.endswith("wired.py"))
    assert record.wiring == "CI_STEP"
    assert report.violations == []


def test_covered_test_path_requires_binding_and_real_tree(tmp_path: Path) -> None:
    """فحصٌ يربطُ نفسَه بالأداةِ ويحكُمُ على الشجرةِ الحاضرةِ = طريقُ إنفاذٍ."""
    root = build_tree(
        tmp_path,
        {"governance/quiet.py": RUNNABLE.format(decl="")},
        {"governance/test_quiet.py": COVERING_TEST.format(stem="quiet")},
    )
    report = epl.measure(root)
    record = next(r for r in report.records if r.path.endswith("quiet.py"))
    assert record.wiring == "COVERED_TEST"
    assert report.violations == []


def test_tmp_path_only_test_is_not_a_path_of_enforcement(tmp_path: Path) -> None:
    """فحصٌ في شجرةٍ مصنوعةٍ وحدَه لا يحكُمُ على الواقعِ فلا يُعَدُّ طريقًا."""
    synthetic = COVERING_TEST.format(stem="quiet").replace(
        "def test_real_tree() -> None:\n    assert REPO_ROOT.is_dir()",
        "def test_synthetic(tmp_path) -> None:\n    assert tmp_path.exists()",
    )
    root = build_tree(
        tmp_path,
        {"governance/quiet.py": RUNNABLE.format(decl="")},
        {"governance/test_quiet.py": synthetic},
    )
    report = epl.measure(root)
    record = next(r for r in report.records if r.path.endswith("quiet.py"))
    assert record.wiring == "NONE"
    assert [v["kind"] for v in report.violations] == ["ENFORCEMENT_PATH_UNDECLARED"]


# ── الأحكامُ ─────────────────────────────────────────────────────────────────


def test_silent_unwired_tool_is_a_violation(tmp_path: Path) -> None:
    root = build_tree(tmp_path, {"audit/silent.py": RUNNABLE.format(decl="")})
    report = epl.measure(root)
    assert [v["kind"] for v in report.violations] == ["ENFORCEMENT_PATH_UNDECLARED"]


def test_declared_reason_clears_the_violation(tmp_path: Path) -> None:
    """الأداةُ تُلزِمُ الإعلانَ لا التشغيلَ — فالسببُ المُصنَّفُ يُقنِعُها."""
    root = build_tree(
        tmp_path,
        {"audit/silent.py": RUNNABLE.format(decl="طريقُ الإنفاذ: NEEDS_LIVE_DB · يلزمُه رابطٌ")},
    )
    report = epl.measure(root)
    assert report.violations == []
    assert any(n["kind"] == "REASON_TALLY" and "NEEDS_LIVE_DB" in n["detail"]
               for n in report.notes)


def test_reason_vocabulary_is_closed(tmp_path: Path) -> None:
    root = build_tree(
        tmp_path,
        {"audit/silent.py": RUNNABLE.format(decl="طريقُ الإنفاذ: LATER · لاحقًا")},
    )
    report = epl.measure(root)
    assert [v["kind"] for v in report.violations] == ["ENFORCEMENT_PATH_UNKNOWN_REASON"]


def test_declared_wiring_that_does_not_exist_is_falsified(tmp_path: Path) -> None:
    """إعلانٌ أكبرُ من الواقعِ يسقُطُ — وإلّا صارَ السطرُ بديلًا عن الربطِ."""
    root = build_tree(
        tmp_path,
        {"audit/liar.py": RUNNABLE.format(decl="طريقُ الإنفاذ: CI_STEP · مربوطٌ زعمًا")},
    )
    report = epl.measure(root)
    assert [v["kind"] for v in report.violations] == ["ENFORCEMENT_PATH_FALSE"]


def test_stale_reason_after_wiring_is_flagged(tmp_path: Path) -> None:
    """سببٌ بقيَ بعدَ أن رُبِطَت الأداةُ = إعلانٌ تخلَّفَ عن الواقعِ."""
    root = build_tree(
        tmp_path,
        {"governance/wired.py": RUNNABLE.format(
            decl="طريقُ الإنفاذ: REPORT_NO_VERDICT · تقريرٌ")},
    )
    report = epl.measure(root)
    assert [v["kind"] for v in report.violations] == ["ENFORCEMENT_PATH_STALE"]


def test_library_needs_no_declaration(tmp_path: Path) -> None:
    root = build_tree(tmp_path, {"governance/lib.py": LIBRARY})
    report = epl.measure(root)
    assert report.violations == []


def test_library_claim_on_a_runnable_file_is_flagged(tmp_path: Path) -> None:
    root = build_tree(
        tmp_path,
        {"audit/silent.py": RUNNABLE.format(decl="طريقُ الإنفاذ: LIBRARY · مكتبةٌ زعمًا")},
    )
    report = epl.measure(root)
    assert [v["kind"] for v in report.violations] == ["ENFORCEMENT_PATH_STALE"]


def test_postponed_wiring_must_name_a_work_item(tmp_path: Path) -> None:
    """«لاحقًا» بلا بندٍ مُسمّى وعدٌ — فالمِرساةُ شرطُ قبولِ التأجيلِ."""
    loose = build_tree(
        tmp_path / "a",
        {"audit/later.py": RUNNABLE.format(decl="طريقُ الإنفاذ: PENDING_GATE_ITEM · لاحقًا")},
    )
    anchored = build_tree(
        tmp_path / "b",
        {"audit/later.py": RUNNABLE.format(
            decl="طريقُ الإنفاذ: PENDING_GATE_ITEM · مؤجَّلٌ ببندِ WI-023")},
    )
    assert [v["kind"] for v in epl.measure(loose).violations] == [
        "ENFORCEMENT_PATH_REASON_UNANCHORED"
    ]
    assert epl.measure(anchored).violations == []


# ── الرفضُ المُصنَّفُ ─────────────────────────────────────────────────────────


def test_missing_tools_directory_is_a_classified_refusal(tmp_path: Path) -> None:
    root = tmp_path / "empty"
    root.mkdir()
    report = epl.measure(root)
    assert report.refusal.startswith("TOOLS_MISSING")
    assert report.violations == []


def test_missing_workflows_is_a_classified_refusal(tmp_path: Path) -> None:
    """بلا وظائفَ لا يُقاسُ طريقٌ — فالرفضُ أصدقُ من «كلُّ الأدواتِ صامتةٌ»."""
    root = build_tree(tmp_path, {"governance/wired.py": RUNNABLE.format(decl="")}, workflow=None)
    report = epl.measure(root)
    assert report.refusal.startswith("WORKFLOWS_MISSING")
    assert report.violations == []


def test_unparsable_tool_refuses_the_whole_measurement(tmp_path: Path) -> None:
    root = build_tree(tmp_path, {"governance/broken.py": "def س(:\n"})
    report = epl.measure(root)
    assert report.refusal.startswith("SOURCE_UNPARSABLE")
    assert report.records == []


def test_exit_codes_are_zero_one_two(tmp_path: Path) -> None:
    """رمزُ الخروجِ هو الحكمُ: 0 سلامةٌ · 1 مخالفةٌ · 2 رفضٌ مُصنَّفٌ."""
    clean = build_tree(tmp_path / "a", {"governance/wired.py": RUNNABLE.format(decl="")})
    violating = build_tree(tmp_path / "b", {"audit/silent.py": RUNNABLE.format(decl="")})
    refusing = tmp_path / "c" / "empty"
    refusing.mkdir(parents=True)
    assert epl.main(["--root", str(clean)]) == 0
    assert epl.main(["--root", str(violating)]) == 1
    assert epl.main(["--root", str(refusing)]) == 2


# ── الشجرةُ الحاضرةُ — هي طريقُ إنفاذِ هذه الأداةِ ────────────────────────────


def test_real_repository_measures_clean_and_is_not_written_to() -> None:
    """المستودعُ الحاضرُ: لا مخالفةَ ولا رفضَ — وهذا حكمٌ على الواقعِ لا على مختبرٍ."""
    before = subprocess.run(
        ["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout
    report = epl.measure(REPO_ROOT)
    after = subprocess.run(
        ["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout
    assert report.refusal == "", report.refusal
    assert report.violations == [], [v["detail"] for v in report.violations]
    assert before == after, "الأداةُ كتبَت في شجرةٍ تحكمُ عليها"


def test_real_repository_tool_declares_its_own_path_truthfully() -> None:
    """الأداةُ لا تُعفي نفسَها: طريقُها المُعلَنُ يُقاسُ كغيرِه."""
    report = epl.measure(REPO_ROOT)
    rel = str(TOOL_PATH.relative_to(REPO_ROOT))
    record = next(r for r in report.records if r.path == rel)
    assert record.declared_mark == "COVERED_TEST"
    assert record.wiring == "COVERED_TEST"
    assert Path(__file__).name in record.wiring_evidence


def test_real_repository_every_runnable_file_has_path_or_reason() -> None:
    """الحكمُ الجوهريُّ: لا ملفَّ قابلًا للتشغيلِ بلا طريقٍ مقيسٍ أو سببٍ مُعلَنٍ."""
    report = epl.measure(REPO_ROOT)
    silent = [
        r.path
        for r in report.records
        if r.kind in (epl.KIND_ENTRYPOINT, epl.KIND_IMPORT_RUN)
        and r.wiring == "NONE"
        and not r.declared_mark
    ]
    assert silent == [], f"أدواتٌ صامتةٌ: {silent}"
