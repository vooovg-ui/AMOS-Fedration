"""
حرسُ الحرسِ — دَينٌ يُعَدُّ فيُرتَّجُ، والفرقُ مُجرَّبٌ لا مُدَّعًى (`W-132` · `WI-047` · `DISC-055`)
الهدف: إثباتُ أنَّ `report_note_ratchet.py` يُفرِّقُ فعلًا بينَ ملاحظةِ إبلاغٍ تحمِلُ عددًا مقيسًا وأخرى لا تحمِلُ، وأنَّ الحبسَ يُقرأُ من **إعلانٍ مقصودٍ** لا من ذِكرٍ عارضٍ في نثرٍ، وأنَّ نموَّ الصامتِ يُسقِطُ الوجهَ ونقصَ المحبوسِ يُسقِطُه، وأنَّ عَطبَ القياسِ يُرفَعُ لا يُبتلَعُ.
النطاق: tests/governance/
المالك: tools/governance/
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

#: علاماتُ الجذرِ — تُكتَشَفُ ولا تُعَدُّ بالقفزِ على الآباءِ (`DISC-046`).
ROOT_MARKERS = ("PROJECT_STATE.md", "docs/MASTER_PLAN.md", "tools/governance")


def _discover_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if all((candidate / marker).exists() for marker in ROOT_MARKERS):
            return candidate
    raise RuntimeError(f"لم يُكتشَفْ جذرُ المستودعِ انطلاقًا من {start}")


REPO_ROOT = _discover_root(Path(__file__).resolve())
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "report_note_ratchet.py"

_SPEC = importlib.util.spec_from_file_location("amos_report_note_ratchet", TOOL_PATH)
assert _SPEC is not None and _SPEC.loader is not None
guard = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(guard)


COUNTED_NOTE = '''
def build(report, rows):
    report.notes.append(_v("ALPHA_TALLY", f"صفوفٌ {len(rows)} — إبلاغٌ لا إسقاطٌ"))
'''

UNCOUNTED_NOTE = '''
def build(report, rows):
    report.notes.append(_v("BETA_STATIC", "لا رقمَ محسوبًا هنا"))
'''

SECOND_COUNTED = '''
def build(report, rows):
    report.notes.append(_v("GAMMA_TALLY", f"أخرى {len(rows)}"))
'''

NOT_A_NOTE = '''
def build(report, rows):
    report.violations.append(_v("DELTA_TALLY", f"مخالفةٌ {len(rows)}"))
    print(f"ملاحظة · EPSILON_TALLY: {len(rows)}")
'''

RECORD = """# اكتشافات

| DISC-055 | ... `REPORT_NOTE_BASELINE: notes={notes} counted={counted} ratcheted={ratcheted} unratcheted={unratcheted}` ... |
| ... `REPORT_NOTE_RATCHETED: {held}` ... |
"""


def _seed(
    tmp_path: Path,
    modules: dict[str, str],
    *,
    notes: int,
    counted: int,
    ratcheted: int,
    unratcheted: int,
    held: str = "",
) -> Path:
    """شجرةٌ مصنوعةٌ صغيرةٌ: بوّاباتٌ تحتَ `tools/` وقيدٌ يحملُ الإعلانَ."""
    root = tmp_path / "tree"
    (root / "tools" / "governance").mkdir(parents=True)
    (root / "docs" / "governance" / "work").mkdir(parents=True)
    for name, body in modules.items():
        (root / "tools" / "governance" / name).write_text(body, encoding="utf-8")
    (root / "docs" / "governance" / "work" / "DISCOVERIES.md").write_text(
        RECORD.format(
            notes=notes,
            counted=counted,
            ratcheted=ratcheted,
            unratcheted=unratcheted,
            held=held,
        ),
        encoding="utf-8",
    )
    return root


# ————————————————————————————— الفرقُ نفسُه —————————————————————————————


def test_counted_note_is_measured(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=1, counted=1, ratcheted=0, unratcheted=1
    )
    assert guard.verdicts(root) == []
    assert guard.measured_counts(root) == {
        "notes": 1,
        "counted": 1,
        "ratcheted": 0,
        "unratcheted": 1,
    }


def test_note_without_a_computed_number_is_not_counted(tmp_path: Path) -> None:
    """رسالةٌ بلا عددٍ محسوبٍ ليست دَينًا معدودًا — والحدُّ مُعلَنٌ."""
    root = _seed(
        tmp_path, {"a.py": UNCOUNTED_NOTE}, notes=1, counted=0, ratcheted=0, unratcheted=0
    )
    assert guard.verdicts(root) == []
    assert guard.measured_counts(root)["counted"] == 0


def test_growth_of_silent_debt_is_caught(tmp_path: Path) -> None:
    root = _seed(
        tmp_path,
        {"a.py": COUNTED_NOTE, "b.py": SECOND_COUNTED},
        notes=1,
        counted=1,
        ratcheted=0,
        unratcheted=1,
    )
    problems = guard.verdicts(root)
    assert any(p.startswith("UNRATCHETED_NOTE_GROWTH") for p in problems)


def test_growth_violation_names_the_notes(tmp_path: Path) -> None:
    root = _seed(
        tmp_path,
        {"a.py": COUNTED_NOTE, "b.py": SECOND_COUNTED},
        notes=1,
        counted=1,
        ratcheted=0,
        unratcheted=1,
    )
    message = "\n".join(guard.verdicts(root))
    assert "GAMMA_TALLY" in message
    assert "tools/governance/b.py" in message


def test_losing_a_declared_ratchet_is_caught(tmp_path: Path) -> None:
    """المحبوسُ أرضٌ لا تنزلُ: حذفُ الملاحظةِ المحبوسةِ يُسقِطُ الوجهَ."""
    root = _seed(
        tmp_path,
        {"a.py": UNCOUNTED_NOTE},
        notes=1,
        counted=1,
        ratcheted=1,
        unratcheted=0,
        held="ALPHA_TALLY",
    )
    problems = guard.verdicts(root)
    assert any(p.startswith("RATCHET_LOSS") for p in problems)


def test_declaring_a_code_moves_it_out_of_the_silent_count(tmp_path: Path) -> None:
    root = _seed(
        tmp_path,
        {"a.py": COUNTED_NOTE},
        notes=1,
        counted=1,
        ratcheted=1,
        unratcheted=0,
        held="ALPHA_TALLY",
    )
    assert guard.verdicts(root) == []
    assert guard.measured_counts(root)["ratcheted"] == 1


def test_only_the_notes_channel_is_measured(tmp_path: Path) -> None:
    """المخالفاتُ ليست ملاحظاتٍ، وسطرُ طباعةٍ حرٌّ ليس ملاحظةً — الشكلُ مُدرَجٌ."""
    root = _seed(
        tmp_path, {"a.py": NOT_A_NOTE}, notes=0, counted=0, ratcheted=0, unratcheted=0
    )
    assert guard.verdicts(root) == []
    assert guard.measured_counts(root)["notes"] == 0


def test_stale_baseline_is_caught(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=9, counted=9, ratcheted=0, unratcheted=1
    )
    assert any(p.startswith("STALE_NOTE_BASELINE") for p in guard.verdicts(root))


# ———————————— الحبسُ إعلانٌ مقصودٌ لا ذِكرٌ عارضٌ ————————————


def test_incidental_mention_does_not_ratchet(tmp_path: Path) -> None:
    """ذِكرُ الرمزِ في نثرِ القيدِ لا يُخضِرُه — وهذا سببُ عَطبٍ أُصلِحَ في `W-132`."""
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=1, counted=1, ratcheted=0, unratcheted=1
    )
    record = root / "docs" / "governance" / "work" / "DISCOVERIES.md"
    record.write_text(
        record.read_text(encoding="utf-8")
        + "\nونضربُ المثلَ بـ`ALPHA_TALLY` وهو ليس محبوسًا.\n",
        encoding="utf-8",
    )
    assert "ALPHA_TALLY" not in guard.cited_codes(root)
    assert guard.verdicts(root) == []


def test_ratchet_line_must_be_single(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=1, counted=1, ratcheted=0, unratcheted=1
    )
    record = root / "docs" / "governance" / "work" / "DISCOVERIES.md"
    record.write_text(
        record.read_text(encoding="utf-8") + "\n`REPORT_NOTE_RATCHETED: X_TALLY`\n",
        encoding="utf-8",
    )
    with pytest.raises(guard.BaselineRecordMissing):
        guard.cited_codes(root)


def test_missing_ratchet_line_is_raised(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=1, counted=1, ratcheted=0, unratcheted=1
    )
    record = root / "docs" / "governance" / "work" / "DISCOVERIES.md"
    record.write_text("# بلا إعلانٍ\n", encoding="utf-8")
    with pytest.raises(guard.BaselineRecordMissing):
        guard.cited_codes(root)


# ———————————————————— الرقمُ يُقرأُ من القيدِ ————————————————————


def test_baseline_is_read_from_the_record(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=4, counted=3, ratcheted=2, unratcheted=1
    )
    assert guard.declared_baseline(root) == {
        "notes": 4,
        "counted": 3,
        "ratcheted": 2,
        "unratcheted": 1,
    }


def test_missing_baseline_record_is_raised(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=1, counted=1, ratcheted=0, unratcheted=1
    )
    record = root / "docs" / "governance" / "work" / "DISCOVERIES.md"
    record.write_text("# لا سطرَ هنا\n", encoding="utf-8")
    with pytest.raises(guard.BaselineRecordMissing):
        guard.declared_baseline(root)


def test_partial_baseline_record_is_raised(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=1, counted=1, ratcheted=0, unratcheted=1
    )
    record = root / "docs" / "governance" / "work" / "DISCOVERIES.md"
    record.write_text("`REPORT_NOTE_BASELINE: notes=1 counted=1`\n", encoding="utf-8")
    with pytest.raises(guard.BaselineRecordMissing):
        guard.declared_baseline(root)


def test_no_number_is_buried_in_the_tool() -> None:
    source = TOOL_PATH.read_text(encoding="utf-8")
    assert "REPORT_NOTE_BASELINE" in source
    assert "unratcheted=18" not in source


# ———————————————————— عَطبُ القياسِ يُرفَعُ ————————————————————


def test_unreadable_source_is_raised(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=1, counted=1, ratcheted=0, unratcheted=1
    )
    (root / "tools" / "governance" / "bad.py").write_bytes(b"\xff\xfe\x00 \xd8\x00")
    with pytest.raises(guard.SourceUnreadable):
        guard.census(root, frozenset())


def test_unparsable_source_is_raised(tmp_path: Path) -> None:
    root = _seed(
        tmp_path, {"a.py": COUNTED_NOTE}, notes=1, counted=1, ratcheted=0, unratcheted=1
    )
    (root / "tools" / "governance" / "broken.py").write_text(
        "def f(:\n", encoding="utf-8"
    )
    with pytest.raises(guard.SourceUnreadable):
        guard.census(root, frozenset())


# ———————————————————— الجذرُ والخُضرةُ ————————————————————


def test_root_discovery_matches_the_shared_finder() -> None:
    spec = importlib.util.spec_from_file_location(
        "amos_repo_root_parity_w132", REPO_ROOT / "tools" / "governance" / "repo_root.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.discover_repo_root(str(TOOL_PATH)) == REPO_ROOT == guard.REPO_ROOT


def test_green_sentence_carries_its_denominator() -> None:
    """جملةُ نجاحِ هذا الحرسِ تحملُ مقامَها (`DISC-053`)."""
    source = TOOL_PATH.read_text(encoding="utf-8")
    marker = "✓ كلُّ ما قِيسَ مُطابِقٌ للمُعلَنِ"
    assert marker in source
    tail = source.split(marker, 1)[1][:260]
    assert "measured['counted']" in tail


def test_the_guard_counts_its_own_note() -> None:
    """الحرسُ لا يُعفي نفسَه: ملاحظتُه مبنيّةٌ بالشكلِ المقيسِ فتدخُلُ العدَّ."""
    codes = {n.code for n in guard.census(REPO_ROOT, guard.cited_codes(REPO_ROOT))}
    assert "REPORT_NOTE_TALLY" in codes
    assert "REPORT_NOTE_TALLY" in guard.cited_codes(REPO_ROOT)


# ———————————————————— الشجرةُ الحقيقيّةُ ————————————————————


def test_real_tree_check_passes() -> None:
    result = subprocess.run(  # noqa: S603 — REAL_TREE_ON_PURPOSE
        [sys.executable, str(TOOL_PATH), str(REPO_ROOT), "--check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def test_real_tree_json_is_structured() -> None:
    result = subprocess.run(  # noqa: S603 — REAL_TREE_ON_PURPOSE
        [sys.executable, str(TOOL_PATH), str(REPO_ROOT), "--json"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["measured"] == payload["declared"]
    assert payload["measured"]["ratcheted"] + payload["measured"]["unratcheted"] == (
        payload["measured"]["counted"]
    )
    assert all(
        note["verdict"] in {guard.RATCHETED, guard.UNRATCHETED}
        for note in payload["notes"]
    )


def test_real_tree_names_the_known_debt() -> None:
    """الدَّينُ المسمّى حاضرٌ في القياسِ — لا رقمٌ مجرَّدٌ."""
    codes = {
        n.code
        for n in guard.census(REPO_ROOT, guard.cited_codes(REPO_ROOT))
        if n.verdict == guard.UNRATCHETED
    }
    assert "VERDICT_CAPABLE_UNWIRED" in codes
    assert "UNWIRED_TOOL_INVENTORY" in codes
