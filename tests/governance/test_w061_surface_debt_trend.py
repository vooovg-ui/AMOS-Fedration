#!/usr/bin/env python3
"""حرسُ اتِّجاهِ دَينِ الأسطحِ — أنَّ الصعودَ يُسقِطُ فعلًا لا يُلاحَظُ (W-061).

الهدف:
    أن تكونَ أداةُ `surface_debt_trend.py` **حرسًا يبيتُ لا عدَّادًا يُقرأُ**: يُبنى
    تاريخٌ صناعيٌّ يصعدُ فيه دَينُ الأسطحِ بينَ قيدَينِ، فيجبُ أن تخرُجَ الأداةُ
    بمخالفةٍ مُسمّاةٍ؛ ويُبنى تاريخٌ يهبطُ فيه، فيجبُ أن تمرَّ. وتُحرَسُ معَها
    الحدودُ المُعلَنةُ في ترويسةِ الأداةِ: القاعدةُ الواحدةُ · أوّلُ التزامٍ أدخلَ
    الصفَّ · الرفضُ المُصنَّفُ عندَ غيابِ التاريخِ · وألّا تكتبَ الأداةُ في شجرةٍ.
النطاق:
    فحوصٌ ساكنةٌ على مستودعاتٍ صناعيّةٍ تحتَ `tmp_path`، وتشغيلةٌ واحدةٌ على
    المستودعِ الحقيقيِّ للتحقُّقِ من أنَّ القياسَ يجري فيه ولا يُلوِّثُه. لا شبكةَ
    ولا قاعدةَ بياناتٍ ولا سرَّ.
المالك: tests/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-29
تاريخ آخر تعديل: 2026-08-29

الحدُّ المُعلَنُ:
    هذا الحرسُ يُثبِتُ أنَّ **الأداةَ** تسقُطُ عندَ الصعودِ. ولا يُثبِتُ أنَّ عدَّ
    الجردِ نفسِه صحيحٌ — ذاك محروسٌ في حرّاسِ الجردِ، ومعيارُه مُعلَنٌ في
    ترويسةِ `tools/audit/sovereign_write_inventory.py`.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "surface_debt_trend.py"


def _load_tool():
    """تحميلُ الأداةِ من مسارِها — كما في بقيّةِ حرّاسِ هذه الطبقة."""
    spec = importlib.util.spec_from_file_location("surface_debt_trend", TOOL_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


TOOL = _load_tool()

#: دالّةٌ عامّةٌ تكتبُ في جلسةِ تخزينٍ بلا عبورِ الحدِّ = موضعُ دَينٍ واحدٌ.
WRITER = """
def write_{index}(session, row):
    session.add(row)
    session.commit()
"""


def _git(root: Path, *args: str) -> str:
    done = subprocess.run(
        [
            "git",
            "-c",
            "user.name=Guard",
            "-c",
            "user.email=guard@example.invalid",
            *args,
        ],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    return done.stdout


def _ledger(entries: list[str]) -> str:
    head = "# سجلٌّ صناعيٌّ\n\n## 8 · سجلُّ العملِ المنفَّذ\n\n"
    rows = "".join(
        f"| {work} | 2026-08-2{i} | عنوان | جسم | — | — |\n"
        for i, work in enumerate(entries, start=1)
    )
    return head + rows


def _write_surfaces(root: Path, count: int) -> None:
    """كتابةُ `count` موضعَ دَينٍ في ملفٍّ إنتاجيٍّ واحدٍ."""
    target = root / "svc" / "service.py"
    target.parent.mkdir(parents=True, exist_ok=True)
    body = '"""وحدةٌ صناعيّةٌ."""\n' + "".join(
        WRITER.format(index=index) for index in range(count)
    )
    target.write_text(body, encoding="utf-8")


def _make_history(
    tmp_path: Path,
    counts: list[int],
    *,
    sabotage_old_rule: bool = False,
    published: int | None = None,
) -> Path:
    """مستودعٌ صناعيٌّ: لكلِّ عددٍ في `counts` قيدٌ وملفٌّ بذلك العددِ من الأسطح."""
    root = tmp_path / "clone"
    (root / "docs" / "audit").mkdir(parents=True)
    _git(root.parent, "init", "-q", "-b", "main", root.name)

    works = [f"W-{index:03d}" for index in range(1, len(counts) + 1)]
    for step, count in enumerate(counts, start=1):
        _write_surfaces(root, count)
        (root / "docs" / "audit" / "COMPLETION_LEDGER.md").write_text(
            _ledger(works[:step]), encoding="utf-8"
        )
        if sabotage_old_rule and step == 1:
            # قاعدةٌ مكسورةٌ في اللقطةِ القديمةِ: لو قِيسَت كلُّ لقطةٍ بأداتِها
            # لانقلبَ الحكمُ — والحدُّ المُعلَنُ أنَّ القاعدةَ واحدةٌ حاضرةٌ.
            broken = root / "tools" / "audit"
            broken.mkdir(parents=True, exist_ok=True)
            (broken / "sovereign_write_inventory.py").write_text(
                "raise SystemExit('قاعدةٌ مكسورةٌ')\n", encoding="utf-8"
            )
        if published is not None:
            measurements = root / "docs" / "audit" / "measurements"
            measurements.mkdir(parents=True, exist_ok=True)
            (measurements / "write_inventory_p13.json").write_text(
                json.dumps({"summary": {TOOL.DEBT_KEY: published}}), encoding="utf-8"
            )
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", f"قيدُ {works[step - 1]}")
    return root


def test_rising_debt_bites(tmp_path: Path) -> None:
    """صعودُ الدَّينِ بينَ قيدَينِ يُسقِطُ الأداةَ بمخالفةٍ مُسمّاةٍ — لا يُلاحَظُ."""
    root = _make_history(tmp_path, [3, 5])
    report = TOOL.measure(root)
    kinds = [violation["kind"] for violation in report.violations]
    assert "SURFACE_DEBT_RISING" in kinds, report.violations
    assert [s.debt_sites for s in report.snapshots] == [3, 5]
    assert report.steps[-1]["debt_delta"] == 2
    assert TOOL.main(["--root", str(root)]) == 1


def test_falling_debt_passes(tmp_path: Path) -> None:
    """هبوطُ الدَّينِ يمرُّ — الحرسُ يمنعُ الصعودَ لا يمنعُ الإصلاحَ."""
    root = _make_history(tmp_path, [6, 2])
    report = TOOL.measure(root)
    assert [v["kind"] for v in report.violations] == []
    assert report.steps[-1]["debt_delta"] == -4
    assert TOOL.main(["--root", str(root)]) == 0


def test_flat_debt_passes(tmp_path: Path) -> None:
    """الثباتُ يمرُّ ويُعلَنُ صافيًا — لا يُقرأُ سكونًا ولا إصلاحًا."""
    root = _make_history(tmp_path, [4, 4])
    report = TOOL.measure(root)
    assert report.violations == []
    assert report.steps[-1]["debt_delta"] == 0
    trend = [note for note in report.notes if note["kind"] == "SURFACE_TREND"]
    assert trend and "+0" in trend[0]["detail"]


def test_more_than_two_points_measured_in_order(tmp_path: Path) -> None:
    """يُقاسُ أكثرُ من قيدَينِ بالترتيبِ العدديِّ، وكلُّ خطوةٍ تُعلَنُ وحدَها."""
    root = _make_history(tmp_path, [2, 3, 3, 9])
    report = TOOL.measure(root, entries=4)
    assert [s.work for s in report.snapshots] == ["W-001", "W-002", "W-003", "W-004"]
    assert [s.debt_sites for s in report.snapshots] == [2, 3, 3, 9]
    assert [step["debt_delta"] for step in report.steps] == [1, 0, 6]
    assert (
        len([v for v in report.violations if v["kind"] == "SURFACE_DEBT_RISING"]) == 2
    )


def test_rule_is_the_present_tree_not_the_snapshot(tmp_path: Path) -> None:
    """القاعدةُ الواحدةُ: قاعدةٌ مكسورةٌ في اللقطةِ القديمةِ لا تُفسِدُ القياسَ."""
    root = _make_history(tmp_path, [3, 5], sabotage_old_rule=True)
    report = TOOL.measure(root)
    assert [s.debt_sites for s in report.snapshots] == [3, 5]
    assert report.rule_source == TOOL.INVENTORY_TOOL.as_posix()


def test_published_inventory_divergence_bites(tmp_path: Path) -> None:
    """حِملٌ منشورٌ يُخالِفُ المقيسَ يُسقِطُ — رقمٌ متقادِمٌ لا يُقرأُ حاضرًا."""
    root = _make_history(tmp_path, [4, 4], published=99)
    report = TOOL.measure(root)
    assert "PUBLISHED_INVENTORY_DIVERGES" in [v["kind"] for v in report.violations]


def test_published_inventory_agreement_is_noted(tmp_path: Path) -> None:
    """وحينَ يتساويانِ يُعلَنُ ذلك ملاحظةً مقيسةً لا صمتًا."""
    root = _make_history(tmp_path, [4, 4], published=4)
    report = TOOL.measure(root)
    assert report.violations == []
    assert "PUBLISHED_INVENTORY_AGREES" in [n["kind"] for n in report.notes]


def test_entry_commit_is_first_introduction(tmp_path: Path) -> None:
    """القيدُ يُنسَبُ إلى **أوّلِ** التزامٍ أدخلَ صفَّه لا إلى آخرِ من ذكرَه.

    والحالةُ مبنيّةٌ لتُفرِّقَ فعلًا: التزامٌ لاحقٌ يذكرُ المعرِّفَ ثانيًا في
    السجلِّ (إحالةُ صفٍّ أحدثَ إليه)، فيصيرُ في التاريخِ التزامانِ يمسّانِ
    المعرِّفَ — فمن أخذَ آخرَهما نسبَ القيدَ إلى غيرِ زمنِه.
    """
    root = _make_history(tmp_path, [3, 5])
    first = TOOL.entry_commit(root, "W-002")
    ledger = root / "docs" / "audit" / "COMPLETION_LEDGER.md"
    ledger.write_text(
        ledger.read_text(encoding="utf-8")
        + "| W-003 | 2026-08-24 | عنوان | جسم | يُكمِلُ | W-002 |\n",
        encoding="utf-8",
    )
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "-m", "صفٌّ أحدثُ يُحيلُ إلى W-002")
    touching = [
        line
        for line in TOOL._git(
            root, "log", "--format=%H", "-SW-002", "--", TOOL.LEDGER.as_posix()
        ).splitlines()
        if line.strip()
    ]
    assert len(touching) >= 2, "الحالةُ لا تُفرِّقُ إن مسَّ المعرِّفَ التزامٌ واحدٌ"
    assert TOOL.entry_commit(root, "W-002") == first


def test_git_failure_is_refused_as_git_failure(tmp_path: Path) -> None:
    """فشلُ `git` نفسِه يُعلَنُ **بجنسِه** — لا يُبتلَعُ فيُقرأَ «لا صفَّ في التاريخِ».

    والتفريقُ مقصودٌ: مجلَّدٌ بلا تاريخٍ يُخرِجُ `GIT_FAILED`، ومستودعٌ سليمٌ لم
    يُلتَزَمْ فيه الصفُّ يُخرِجُ `ENTRY_COMMIT_NOT_FOUND`. ومن ابتلعَ الأوّلَ
    أعلنَ الثانيَ عن حالٍ ثالثةٍ.
    """
    root = tmp_path / "bare"
    (root / "docs" / "audit").mkdir(parents=True)
    (root / "docs" / "audit" / "COMPLETION_LEDGER.md").write_text(
        _ledger(["W-001", "W-002"]), encoding="utf-8"
    )
    with pytest.raises(TOOL.MeasurementRefused) as refusal:
        TOOL.measure(root)
    assert refusal.value.kind in {"GIT_FAILED", "GIT_UNAVAILABLE"}, refusal.value.kind
    assert TOOL.main(["--root", str(root)]) == 2


def test_uncommitted_ledger_row_is_refused_as_missing_entry(tmp_path: Path) -> None:
    """صفٌّ في شجرةِ العملِ لم يُلتَزَمْ: رفضٌ باسمِه هو، لا حكمٌ بلا صعودٍ."""
    root = tmp_path / "fresh"
    root.mkdir()
    _git(root.parent, "init", "-q", "-b", "main", root.name)
    (root / "seed.txt").write_text("بذرةٌ\n", encoding="utf-8")
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "-m", "بذرةٌ")
    (root / "docs" / "audit").mkdir(parents=True)
    (root / "docs" / "audit" / "COMPLETION_LEDGER.md").write_text(
        _ledger(["W-001", "W-002"]), encoding="utf-8"
    )
    with pytest.raises(TOOL.MeasurementRefused) as refusal:
        TOOL.measure(root)
    assert refusal.value.kind == "ENTRY_COMMIT_NOT_FOUND", refusal.value.kind


def test_missing_ledger_is_refused(tmp_path: Path) -> None:
    """سجلٌّ غائبٌ رفضٌ لا صفرُ مخالفاتٍ."""
    with pytest.raises(TOOL.MeasurementRefused) as refusal:
        TOOL.measure(tmp_path)
    assert refusal.value.kind == "SOURCE_MISSING"


def test_ledger_without_rows_is_refused(tmp_path: Path) -> None:
    """جدولٌ بلا صفوفٍ لا يُقاسُ عليه اتِّجاهٌ."""
    (tmp_path / "docs" / "audit").mkdir(parents=True)
    (tmp_path / "docs" / "audit" / "COMPLETION_LEDGER.md").write_text(
        "# لا صفوفَ هنا\n", encoding="utf-8"
    )
    with pytest.raises(TOOL.MeasurementRefused) as refusal:
        TOOL.measure(tmp_path)
    assert refusal.value.kind == "NO_LEDGER_ROWS"


def test_single_point_is_refused(tmp_path: Path) -> None:
    """نقطةٌ واحدةٌ لا تُنتِجُ اتِّجاهًا — والطلبُ يُرفَضُ مُصنَّفًا."""
    root = _make_history(tmp_path, [3, 5])
    with pytest.raises(TOOL.MeasurementRefused) as refusal:
        TOOL.measure(root, entries=1)
    assert refusal.value.kind == "TOO_FEW_POINTS"


def test_more_points_than_rows_is_refused(tmp_path: Path) -> None:
    """لا يُخترَعُ قيدٌ ليُقاسَ عليه اتِّجاهٌ."""
    root = _make_history(tmp_path, [3, 5])
    with pytest.raises(TOOL.MeasurementRefused) as refusal:
        TOOL.measure(root, entries=5)
    assert refusal.value.kind == "TOO_FEW_LEDGER_ROWS"


def _porcelain() -> str:
    """حالُ الشجرةِ سطرًا سطرًا — قبلَ القياسِ وبعدَه."""
    return subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def test_real_repository_is_measured_and_not_written_to() -> None:
    """تشغيلةٌ على المستودعِ الحقيقيِّ: إمّا قياسٌ وإمّا رفضٌ مُسمَّى، ولا يُلمَسُ ملفٌّ.

    وقاعدةُ المستودعِ `PUSH = Work + Its Record, Together` تعني أنَّ القيدَ يُكتَبُ
    **قبلَ** الدفعِ؛ ففي تلكَ اللحظةِ أحدَثُ صفٍّ في § 8 لم يُلتَزَمْ بعدُ، والأداةُ
    ترفضُ أن تقيسَ ما ليسَ في التاريخِ. فالمطلوبُ هنا أن تُعلَنَ الحالُ **بجنسِها**
    لا أن تُقرأَ خُضرةً، وأن تبقى الشجرةُ كما هي في الحالَينِ كلَيهما.
    """
    before = _porcelain()
    refusal = None
    report = None
    try:
        report = TOOL.measure(REPO_ROOT)
    except TOOL.MeasurementRefused as raised:
        refusal = raised
    after = _porcelain()
    assert after == before, "بوّابةٌ تكتبُ في ما تحكمُ عليه لا تُثبِتُ شيئًا"

    if refusal is not None:
        # الرفضُ الوحيدُ المقبولُ في شجرةٍ سليمةٍ: قيدٌ كُتِبَ ولمّا يُدفَعْ.
        assert refusal.kind == "ENTRY_COMMIT_NOT_FOUND", refusal.kind
        rows = TOOL.ledger_entries(
            (REPO_ROOT / TOOL.LEDGER).read_text(encoding="utf-8")
        )
        newest = TOOL.newest_entries(rows, 2)[-1]
        touching = TOOL._git(
            REPO_ROOT,
            "log",
            "--format=%H",
            f"-S| {newest} |",
            "--",
            TOOL.LEDGER.as_posix(),
        ).strip()
        assert touching == "", "رفضٌ بلا سببٍ مقيسٍ: الصفُّ موجودٌ في التاريخِ"
        return

    assert report is not None
    assert len(report.snapshots) == 2
    assert all(s.debt_sites >= 0 for s in report.snapshots)
    assert report.rule_source == "tools/audit/sovereign_write_inventory.py"
