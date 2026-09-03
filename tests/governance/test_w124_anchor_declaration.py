#!/usr/bin/env python3
"""حرسُ إعلانِ المِرساةِ — نثرٌ فيه مسارٌ لا يُشترى به ضمانٌ (WI-039 · DISC-021).

الهدف:
    أن يصيرَ العَطبُ المُقيَّدُ في `DISC-021` مقيسًا لا موصوفًا: صفٌّ يكتبُ نفيًا
    صريحًا («لا حرسَ، وهذانِ الملفّانِ لا يقيسانِ هذا») يُقرأُ اليومَ `GUARD`
    لمجرَّدِ مرورِ مسارٍ في كلامِه. فأُضيفَ إلى الأداةِ **إعلانٌ مُهيكَلٌ**
    (`حرسٌ قائمٌ:` / `حرسٌ مُثبَتٌ:`) يُقرأُ وحدَه ضمانًا، وصفوفُ «مسارٍ في نثرٍ»
    الباقيةُ تُعَدُّ وتُسمَّى وتُسقَّطُ برقمٍ **لا يعلو** — سقّاطةٌ تمنعُ النموَّ
    ولا تُبيحُ القائمَ.
النطاق:
    شجرةٌ مؤقّتةٌ تُبنى في كلِّ حالةٍ، وفحصٌ واحدٌ يقرأُ المستودعَ الحقيقيَّ
    فيُثبِتُ أنَّ الرقمَ المُعلَنَ في `DISCOVERIES.md` يُطابِقُ المقيسَ. لا شبكةَ
    ولا قاعدةَ ولا سرَّ، ولا كتابةَ في سجلٍّ يُحكَمُ عليه.
المالك: tests/governance — ديوانُ التدقيق
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

الحدُّ المُعلَنُ — لا مطويٌّ:
    * هذا الفحصُ يحرسُ **طبقةَ الإعلانِ** لا تصنيفَ `anchor` نفسَه: تحويلُ
      `GUARD` إلى «بلا مِرساةٍ» لصفوفِ النثرِ يمسُّ
      `tests/governance/test_w059_open_record_accountability.py` **وهو مُدَّعًى
      لـ`WI-033` وحالتُه `IN_REVIEW`** — فلا يُمَسُّ، والسقّاطةُ هي ما يُمكِنُ
      إنزالُه اليومَ بلا خرقِ ملكيّةٍ.
    * والسقّاطةُ تقيسُ **عددَ الصفوفِ لا كفايةَ حرسِها**: صفٌّ يُعلِنُ حرسَه
      إعلانًا مُهيكَلًا قد لا يحرسُ عينَ العَطبِ، وذاك حكمٌ بشريٌّ لا نصٌّ.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root

REPO_ROOT = discover_repo_root(__file__)
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "open_record_accountability.py"


def _load():
    spec = importlib.util.spec_from_file_location("ora_declaration", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ORA = _load()

DISC_HEAD = """# سجلُّ الاكتشافات

## 1 · الاكتشافاتُ المُقيَّدة

| المعرِّف | الخطورة | موضعُ الظهور | ما اكتُشِف | الدليل | الأثر | الوجهة | الحالة |
|---|---|---|---|---|---|---|---|
"""

RISK_HEAD = """# سجلُّ المخاطر

## 1 · المخاطرُ المفتوحة

| المعرِّف | الخطر | الاحتمال | الأثر | الإشارةُ المبكِّرةُ | التصرُّف | المالك | المصدر |
|---|---|---|---|---|---|---|---|
"""

BASELINE_LINE = "\nملاحظةٌ · ANCHOR_PROSE_BASELINE: rows={rows}\n"

#: النصُّ الذي أنتجَ الخُضرةَ الكاذبةَ في `W-060`: نفيٌ صريحٌ يمرُّ فيه مسارانِ.
DENYING_PROSE = (
    "| DISC-201 | P2 | موضع | ما اكتُشِف | دليل | أثر | "
    "لا حرسَ لهذا القيدِ، و`tools/governance/probe.py` "
    "و`tests/governance/test_probe.py` لا يقيسانِ هذا العَطبَ | مفتوحٌ |"
)
#: الصفُّ نفسُه بعدَ أن صارَ إعلانًا مُهيكَلًا.
DECLARED_ROW = (
    "| DISC-202 | P2 | موضع | ما اكتُشِف | دليل | أثر | "
    "**حرسٌ قائمٌ**: `tools/governance/probe.py` · "
    "`tests/governance/test_probe.py` — ثمَّ كلامٌ لا يُقرأُ مسارًا | مفتوحٌ |"
)
RISK_DECLARED = (
    "| RK-201 | خطرٌ مقيسٌ | مرتفع | أثر | عدَّادٌ يصعدُ | "
    "**حرسٌ مُثبَتٌ**: `tools/governance/probe.py` "
    "و`tests/governance/test_probe.py` | مالكُ النطاقِ | قيدُ W-001 |"
)
RISK_PROSE = (
    "| RK-202 | خطرٌ مقيسٌ | مرتفع | أثر | عدَّادٌ يصعدُ | "
    "يُنظَرُ في `tools/governance/probe.py` لاحقًا | مالكُ النطاقِ | قيدُ W-001 |"
)


#: صفّانِ محايدانِ: لا مسارَ فيهما فلا يُعَدّانِ في الإعلانِ، ووجودُهما لازمٌ
#: لأنَّ الأداةَ ترفُضُ القياسَ على سجلٍّ بلا صفوفٍ.
DISC_FILLER = (
    "| DISC-299 | P3 | موضع | ما اكتُشِف | دليل | أثر | "
    "قرارُ المالكِ | مفتوحٌ |"
)
RISK_FILLER = (
    "| RK-299 | خطرٌ مقيسٌ | منخفض | أثر | عدَّادٌ يصعدُ | "
    "يُرفَعُ إلى المالكِ | المالك | قيدُ W-001 |"
)


def _tree(
    root: Path,
    *,
    disc_rows: tuple[str, ...] = (),
    risk_rows: tuple[str, ...] = (),
    baseline: str | None = "0",
) -> None:
    """شجرةٌ مؤقّتةٌ فيها السجلّانِ والمساراتُ التي تذكرُها صفوفُهما."""
    work = root / "docs/governance/work"
    work.mkdir(parents=True, exist_ok=True)
    disc_rows = disc_rows or (DISC_FILLER,)
    risk_rows = risk_rows or (RISK_FILLER,)
    disc = DISC_HEAD + "".join(f"{row}\n" for row in disc_rows)
    if baseline is not None:
        disc += BASELINE_LINE.format(rows=baseline)
    (work / "DISCOVERIES.md").write_text(disc, encoding="utf-8")
    (work / "RISK_REGISTER.md").write_text(
        RISK_HEAD + "".join(f"{row}\n" for row in risk_rows) + "\n",
        encoding="utf-8",
    )
    for rel in ("tools/governance/probe.py", "tests/governance/test_probe.py"):
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# مِسبارٌ\n", encoding="utf-8")


# ——— قراءةُ الإعلانِ المُهيكَلِ نفسِه ———


def test_declaration_reads_paths_after_the_marker() -> None:
    assert ORA.declared_guard_paths(
        "**حرسٌ قائمٌ**: `tools/governance/a.py` · `tests/governance/test_a.py`"
    ) == ("tools/governance/a.py", "tests/governance/test_a.py")


def test_declaration_accepts_the_waw_separator_and_the_second_marker() -> None:
    assert ORA.declared_guard_paths(
        "**حرسٌ مُثبَتٌ**: `tools/governance/a.py` و`tests/governance/test_a.py`"
    ) == ("tools/governance/a.py", "tests/governance/test_a.py")


def test_declaration_accepts_a_markdown_link_form() -> None:
    assert ORA.declared_guard_paths(
        "حرسٌ قائمٌ: [`tools/governance/a.py`](../../tools/governance/a.py)"
    ) == ("tools/governance/a.py",)


def test_declaration_stops_at_the_first_segment_that_is_not_a_path() -> None:
    """المسحُ لا يبتلعُ ما بعدَ المقطعِ: مسارٌ بعدَ كلامٍ ليسَ مُعلَنًا."""
    assert ORA.declared_guard_paths(
        "حرسٌ قائمٌ: `tools/governance/a.py` — ويُنظَرُ في "
        "`tests/governance/test_b.py` لاحقًا"
    ) == ("tools/governance/a.py",)


def test_a_path_without_any_marker_is_not_a_declaration() -> None:
    assert ORA.declared_guard_paths("يُنظَرُ في `tools/governance/a.py`") == ()


def test_the_denial_that_bought_green_in_w060_declares_nothing() -> None:
    """عينُ `DISC-021`: النفيُ الصريحُ لا يُقرأُ إعلانًا مهما ذكرَ مساراتٍ."""
    assert (
        ORA.declared_guard_paths(
            "لا حرسَ لهذا القيدِ، و`tools/governance/probe.py` "
            "و`tests/governance/test_probe.py` لا يقيسانِ هذا العَطبَ"
        )
        == ()
    )


# ——— أثرُ ذلك في صفوفِ القياسِ ———


def test_prose_row_is_counted_prose_and_declared_row_is_counted_declared(
    tmp_path: Path,
) -> None:
    _tree(tmp_path, disc_rows=(DENYING_PROSE, DECLARED_ROW), baseline="1")
    report = ORA.measure(tmp_path)
    prose = next(r for r in report.records if r.record_id == "DISC-201")
    declared = next(r for r in report.records if r.record_id == "DISC-202")
    assert prose.declared_paths == ()
    assert prose.prose_paths == (
        "tools/governance/probe.py",
        "tests/governance/test_probe.py",
    )
    assert declared.declared_paths == (
        "tools/governance/probe.py",
        "tests/governance/test_probe.py",
    )
    assert declared.prose_paths == ()


def test_the_original_anchor_classification_is_untouched(tmp_path: Path) -> None:
    """الطبقةُ تُضافُ ولا تُبدِّلُ حكمًا قائمًا — والحدُّ مُعلَنٌ في ترويسةِ الفحصِ."""
    _tree(tmp_path, disc_rows=(DENYING_PROSE,), baseline="1")
    report = ORA.measure(tmp_path)
    assert next(r for r in report.records if r.record_id == "DISC-201").anchor == (
        ORA.ANCHOR_GUARD
    )


def test_risk_rows_read_the_same_two_markers(tmp_path: Path) -> None:
    _tree(tmp_path, risk_rows=(RISK_DECLARED, RISK_PROSE), baseline="1")
    report = ORA.measure_declarations(tmp_path)
    assert report.declared_rows == ["RK-201"]
    assert report.prose_rows == ["RK-202"]


# ——— السقّاطةُ: تمنعُ النموَّ ولا تُبيحُ القائمَ ———


def test_matching_baseline_is_clean(tmp_path: Path) -> None:
    _tree(tmp_path, disc_rows=(DENYING_PROSE, DECLARED_ROW), baseline="1")
    assert ORA.measure_declarations(tmp_path).violations == []
    assert ORA.main(["--root", str(tmp_path), "--declaration-check"]) == 0


def test_growth_is_a_named_violation(tmp_path: Path) -> None:
    _tree(tmp_path, disc_rows=(DENYING_PROSE,), risk_rows=(RISK_PROSE,), baseline="1")
    report = ORA.measure_declarations(tmp_path)
    assert [v["kind"] for v in report.violations] == ["PROSE_ANCHOR_GROWTH"]
    assert "DISC-201" in report.violations[0]["detail"]
    assert ORA.main(["--root", str(tmp_path), "--declaration-check"]) == 1


def test_a_baseline_left_loose_is_a_named_violation(tmp_path: Path) -> None:
    """انخفضَ المقيسُ ولم يُخفَضِ المُعلَنُ — سقّاطةٌ رخوةٌ تُعيدُ ما زالَ."""
    _tree(tmp_path, disc_rows=(DECLARED_ROW,), baseline="3")
    report = ORA.measure_declarations(tmp_path)
    assert [v["kind"] for v in report.violations] == ["STALE_PROSE_BASELINE"]
    assert ORA.main(["--root", str(tmp_path), "--declaration-check"]) == 1


def test_a_missing_baseline_is_a_classified_refusal(tmp_path: Path) -> None:
    _tree(tmp_path, disc_rows=(DENYING_PROSE,), baseline=None)
    with pytest.raises(ORA.MeasurementRefused) as refusal:
        ORA.measure_declarations(tmp_path)
    assert refusal.value.kind == "PROSE_BASELINE_MISSING"
    assert ORA.main(["--root", str(tmp_path), "--declaration-check"]) == 2


def test_two_different_baselines_are_a_classified_refusal(tmp_path: Path) -> None:
    _tree(tmp_path, disc_rows=(DENYING_PROSE,), baseline="1")
    disc = tmp_path / "docs/governance/work/DISCOVERIES.md"
    disc.write_text(
        disc.read_text(encoding="utf-8") + "ANCHOR_PROSE_BASELINE: rows=9\n",
        encoding="utf-8",
    )
    with pytest.raises(ORA.MeasurementRefused) as refusal:
        ORA.measure_declarations(tmp_path)
    assert refusal.value.kind == "PROSE_BASELINE_AMBIGUOUS"


def test_the_same_baseline_written_twice_is_not_a_refusal(tmp_path: Path) -> None:
    """تكرارُ الرقمِ نفسِه ليسَ تعدُّدَ حقيقةٍ — الرفضُ للاختلافِ لا للتكرارِ."""
    _tree(tmp_path, disc_rows=(DENYING_PROSE,), baseline="1")
    disc = tmp_path / "docs/governance/work/DISCOVERIES.md"
    disc.write_text(
        disc.read_text(encoding="utf-8") + "ANCHOR_PROSE_BASELINE: rows=1\n",
        encoding="utf-8",
    )
    assert ORA.read_prose_baseline(tmp_path) == 1


def test_the_declaration_check_writes_nothing_into_the_registers(
    tmp_path: Path,
) -> None:
    _tree(tmp_path, disc_rows=(DENYING_PROSE, DECLARED_ROW), baseline="1")
    work = tmp_path / "docs/governance/work"
    before = {path: path.read_bytes() for path in work.rglob("*.md")}
    ORA.main(["--root", str(tmp_path), "--declaration-check"])
    assert {path: path.read_bytes() for path in work.rglob("*.md")} == before


def test_json_payload_carries_the_numbers(tmp_path: Path, capsys) -> None:
    _tree(tmp_path, disc_rows=(DENYING_PROSE, DECLARED_ROW), baseline="1")
    assert ORA.main(["--root", str(tmp_path), "--declaration-check", "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["baseline_rows"] == 1
    assert payload["prose_count"] == len(payload["prose_rows"]) == 1
    assert payload["declared_count"] == len(payload["declared_rows"]) == 1
    assert payload["declared_markers"] == list(ORA.GUARD_DECLARATION_MARKERS)


# ——— طفرةٌ مقصودةٌ: يُثبَتُ أنَّ شرطَ الإعلانِ حاملٌ لا زينةٌ ———


def test_reverting_to_any_path_counts_makes_the_counter_go_silent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """الطفرةُ هي السلوكُ القديمُ نفسُه: أيُّ مسارٍ يُقرأُ إعلانًا فيسكُتُ العدَّادُ."""
    _tree(tmp_path, disc_rows=(DENYING_PROSE,), baseline="1")
    assert ORA.measure_declarations(tmp_path).prose_rows == ["DISC-201"]
    monkeypatch.setattr(
        ORA,
        "declared_guard_paths",
        lambda text: tuple(dict.fromkeys(ORA.PATH_RE.findall(text))),
    )
    mutated = ORA.measure_declarations(tmp_path)
    assert mutated.prose_rows == []
    assert [v["kind"] for v in mutated.violations] == ["STALE_PROSE_BASELINE"]


def test_an_empty_marker_is_skipped_and_does_not_spin(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """علامةٌ فارغةٌ تُطابِقُ كلَّ موضعٍ وتقدُّمُها صِفرٌ — تُتخطَّى لا تدورُ."""
    monkeypatch.setattr(ORA, "GUARD_DECLARATION_MARKERS", ("", "حرسٌ قائمٌ:"))
    assert ORA.declared_guard_paths("يُنظَرُ في `tools/governance/a.py`") == ()
    assert ORA.declared_guard_paths("حرسٌ قائمٌ: `tools/governance/a.py`") == (
        "tools/governance/a.py",
    )


# ——— المستودعُ الحقيقيُّ: الرقمُ المُعلَنُ يُطابِقُ المقيسَ ———


def test_the_real_repository_matches_its_declared_baseline() -> None:
    report = ORA.measure_declarations(REPO_ROOT)
    assert report.violations == [], report.violations
    assert len(report.prose_rows) == report.baseline


def test_the_real_repository_declares_at_least_one_guard() -> None:
    """لو صارَ الإعلانُ شكلًا لا يستعمِلُه أحدٌ، سقطَ هذا الفحصُ لا الرقمُ وحدَه."""
    assert ORA.measure_declarations(REPO_ROOT).declared_rows


# ——— حدُّ الأعمدةِ: الرفضُ في الجهتَينِ لا في جهةٍ واحدةٍ (`DISC-048`) ———

#: صفٌّ فيه أنبوبٌ غيرُ مهروبٍ داخلَ خليّةِ وجهتِه: تسعُ خلايا لا ثمانٍ،
#: فتزحفُ الأعمدةُ ويُقرأُ ذيلُ الوجهةِ حالةً — وهو الصفُّ الذي مرَّ صامتًا.
OVERFLOWING_DISC_ROW = (
    "| DISC-203 | P2 | موضع | ما اكتُشِف | دليل | أثر | "
    "الوجهةُ `WI-001` وأمرُ قياسِها `grep tests/ | wc -l` | مفتوحٌ |"
)
#: الصفُّ نفسُه بعدَ الهربِ: ثمانِ خلايا، والأنبوبُ محتوًى لا حدٌّ.
ESCAPED_DISC_ROW = OVERFLOWING_DISC_ROW.replace("| wc -l", r"\| wc -l")

OVERFLOWING_RISK_ROW = (
    "| RK-203 | خطرٌ مقيسٌ | منخفض | أثر | عدَّادٌ يصعدُ | "
    r"يُستثنى `try/except ImportError|Exception` | المالك | قيدُ W-001 |"
)
ESCAPED_RISK_ROW = OVERFLOWING_RISK_ROW.replace("ImportError|", r"ImportError\|")


def _codes(report) -> list[str]:
    return [v["kind"] for v in report.violations]


def test_a_discovery_row_with_more_cells_than_declared_is_refused(
    tmp_path: Path,
) -> None:
    """الزيادةُ تُرفَضُ كما يُرفَضُ النقصُ — وإلّا حُكِمَ على صفٍّ لم يُقرَأْ."""
    _tree(tmp_path, disc_rows=(OVERFLOWING_DISC_ROW,), baseline="0")
    report = ORA.measure(tmp_path)
    assert "MALFORMED_ROW" in _codes(report)
    assert not [r for r in report.records if r.record_id == "DISC-203"]


def test_a_risk_row_with_more_cells_than_declared_is_refused(tmp_path: Path) -> None:
    _tree(tmp_path, risk_rows=(OVERFLOWING_RISK_ROW,), baseline="0")
    report = ORA.measure(tmp_path)
    assert "MALFORMED_ROW" in _codes(report)
    assert not [r for r in report.records if r.record_id == "RK-203"]


def test_the_refusal_names_the_unescaped_pipe_as_the_cause(tmp_path: Path) -> None:
    """رسالةٌ لا تُسمّي السببَ تدفعُ إلى حذفِ النصِّ بدلَ هربِ محرفِه."""
    _tree(tmp_path, disc_rows=(OVERFLOWING_DISC_ROW,), baseline="0")
    detail = next(
        v["detail"]
        for v in ORA.measure(tmp_path).violations
        if v["kind"] == "MALFORMED_ROW"
    )
    assert "|" in detail
    assert "9" in detail


def test_an_escaped_pipe_is_content_and_the_row_reads_eight_cells(
    tmp_path: Path,
) -> None:
    """`\\|` محتوًى لا حدٌّ (‏قاعدةُ GFM) — فالصفُّ يُقرأُ ولا يُرفَضُ."""
    _tree(tmp_path, disc_rows=(ESCAPED_DISC_ROW,), risk_rows=(ESCAPED_RISK_ROW,))
    report = ORA.measure(tmp_path)
    assert "MALFORMED_ROW" not in _codes(report)
    row = next(r for r in report.records if r.record_id == "DISC-203")
    assert row.anchor == ORA.ANCHOR_NONE
    assert next(r for r in report.records if r.record_id == "RK-203")


def test_the_escaped_pipe_is_unescaped_inside_the_cell_text(tmp_path: Path) -> None:
    """الهربُ يُزالُ عندَ القراءةِ، فلا يتغيَّرُ النصُّ الذي تُقاسُ عليه المِرساةُ."""
    _tree(tmp_path, disc_rows=(ESCAPED_DISC_ROW,))
    cells = ORA._cells(ESCAPED_DISC_ROW)
    assert len(cells) == ORA.DECLARED_COLUMNS
    assert "grep tests/ | wc -l" in cells[6]
    assert "\\|" not in cells[6]


def test_reverting_the_column_limit_makes_the_overflowing_row_pass(
    tmp_path: Path, monkeypatch
) -> None:
    """طفرةٌ أولى: لولا حدُّ العددِ لمرَّ صفُّ التسعِ خلايا ولحُكِمَ عليه بعمودٍ مُزاحٍ."""
    _tree(tmp_path, disc_rows=(OVERFLOWING_DISC_ROW,), baseline="0")
    assert "MALFORMED_ROW" in _codes(ORA.measure(tmp_path))
    before = ORA.measure(tmp_path).records
    assert not [r for r in before if r.record_id == "DISC-203"]
    monkeypatch.setattr(ORA, "DECLARED_COLUMNS", 9)
    passed = ORA.measure(tmp_path)
    shifted = next(r for r in passed.records if r.record_id == "DISC-203")
    assert shifted.open_basis == "STATUS_UNDECLARED_READ_OPEN", (
        "بعدَ رفعِ الحدِّ يُقرأُ ذيلُ خليّةِ الوجهةِ حالةً، فتُقرأُ «مفتوحٌ» "
        "المكتوبةُ في عمودٍ لا يُنظَرُ إليه — وهو عينُ العَطبِ المُقيَّدِ"
    )



def test_reverting_the_naive_split_refuses_a_legitimately_escaped_row(
    tmp_path: Path, monkeypatch
) -> None:
    """طفرةٌ ثانيةٌ: لولا تمييزُ المهروبِ لصارَ الهربُ الصحيحُ نفسُه رفضًا."""
    _tree(tmp_path, disc_rows=(ESCAPED_DISC_ROW,), baseline="0")
    assert "MALFORMED_ROW" not in _codes(ORA.measure(tmp_path))
    monkeypatch.setattr(ORA, "_CELL_SPLIT_RE", re.compile(r"\|"))
    assert "MALFORMED_ROW" in _codes(ORA.measure(tmp_path))


def test_the_real_registers_hold_no_malformed_row(tmp_path: Path) -> None:
    """السجلّانِ الحقيقيّانِ يُقرآنِ ثمانيًا — وإلّا حُكِمَ عليهما بعمودٍ مُزاحٍ."""
    report = ORA.measure(REPO_ROOT)
    assert "MALFORMED_ROW" not in _codes(report), [
        v["detail"] for v in report.violations if v["kind"] == "MALFORMED_ROW"
    ]
