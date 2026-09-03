"""
حرسُ الحرسِ — شهادةُ الأثرِ تُقرأُ، والفرقُ مُجرَّبٌ لا مُدَّعًى (`W-131` · `WI-046` · `DISC-054`)
الهدف: إثباتُ أنَّ `artifact_witness_integrity.py` يُفرِّقُ فعلًا بينَ أثرٍ مُقيَّدٍ يشهدُ بلسانِه على نقصِ بيئةِ قياسِه وأثرٍ لا يشهدُ، وأنَّ حذفَ الشهادةِ هربًا من القراءةِ يُسقِطُ الوجهَ كما يُسقِطُه النقصُ، وأنَّ الرقمَ المُعلَنَ يُقرأُ من القيدِ لا من الأداةِ، وأنَّ عَطبَ القراءةِ يُرفَعُ لا يُبتلَعُ.
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
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "artifact_witness_integrity.py"

_SPEC = importlib.util.spec_from_file_location("amos_artifact_witness", TOOL_PATH)
assert _SPEC is not None and _SPEC.loader is not None
guard = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(guard)


SOUND_ARTIFACT = """# مصفوفةٌ مُولَّدةٌ

هذه الوثيقة مولَّدة، وأرقامها مقيسة لحظة التوليد.

آخر توليد: **2026-08-19 10:42 UTC**

بيئة PostgreSQL الحقيقية لحظة التوليد: **مُفعّلة**

| الحزمة | الحال |
| --- | --- |
| root-core | **PASS** |
"""

DEGRADED_ENV = SOUND_ARTIFACT.replace("**مُفعّلة**", "**غائبة**")
DEGRADED_SUITE = SOUND_ARTIFACT.replace("**PASS**", "**FAIL**")
NO_WITNESS = "# وثيقةٌ مكتوبةٌ يدًا\n\nلا شهادةَ توليدٍ فيها ولا أرقامَ مقيسةً.\n"

BASELINE_RECORD = """# اكتشافات

| DISC-054 | P2 | ... ⇒ `ARTIFACT_WITNESS_BASELINE: witnessing={witnessing} degraded={degraded}` | ... |
"""


def _seed(tmp_path: Path, artifacts: dict[str, str], *, witnessing: int, degraded: int) -> Path:
    """شجرةٌ مصنوعةٌ صغيرةٌ: آثارٌ تحتَ `docs/` وقيدٌ يحملُ الرقمَ المُعلَنَ."""
    root = tmp_path / "tree"
    (root / "docs" / "audit").mkdir(parents=True)
    (root / "docs" / "governance" / "work").mkdir(parents=True)
    for name, body in artifacts.items():
        (root / "docs" / "audit" / name).write_text(body, encoding="utf-8")
    (root / "docs" / "governance" / "work" / "DISCOVERIES.md").write_text(
        BASELINE_RECORD.format(witnessing=witnessing, degraded=degraded), encoding="utf-8"
    )
    return root


# ————————————————————————————— الفرقُ نفسُه —————————————————————————————


def test_sound_artifact_passes(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"A.md": SOUND_ARTIFACT}, witnessing=1, degraded=0)
    assert guard.verdicts(root) == []


def test_degraded_environment_is_caught(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"A.md": DEGRADED_ENV}, witnessing=1, degraded=0)
    problems = guard.verdicts(root)
    assert any(p.startswith("DEGRADED_ARTIFACT_COMMITTED") for p in problems)


def test_failed_suite_cell_is_caught(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"A.md": DEGRADED_SUITE}, witnessing=1, degraded=0)
    problems = guard.verdicts(root)
    assert any(p.startswith("DEGRADED_ARTIFACT_COMMITTED") for p in problems)


def test_the_difference_is_the_witness_not_the_file(tmp_path: Path) -> None:
    """الوثيقتانِ متطابقتانِ إلّا في كلمةِ الشهادةِ — والحكمُ يختلفُ."""
    sound = _seed(tmp_path / "s", {"A.md": SOUND_ARTIFACT}, witnessing=1, degraded=0)
    broken = _seed(tmp_path / "b", {"A.md": DEGRADED_ENV}, witnessing=1, degraded=0)
    assert guard.verdicts(sound) == []
    assert guard.verdicts(broken) != []


def test_violation_names_the_artifact_and_its_words(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"CROSS.md": DEGRADED_ENV}, witnessing=1, degraded=0)
    message = "\n".join(guard.verdicts(root))
    assert "docs/audit/CROSS.md" in message
    assert "**غائبة**" in message


# ———————————————————— الشهادةُ أرضٌ لا تنزلُ ————————————————————


def test_deleting_the_witness_is_caught_like_the_deficiency(tmp_path: Path) -> None:
    """حذفُ الشهادةِ هربًا من قراءتِها يُسقِطُ الوجهَ — لا يُنجّي."""
    root = _seed(tmp_path, {"A.md": NO_WITNESS}, witnessing=1, degraded=0)
    problems = guard.verdicts(root)
    assert any(p.startswith("WITNESS_COUNT_UNDECLARED") for p in problems)


def test_new_witness_must_be_declared(tmp_path: Path) -> None:
    root = _seed(
        tmp_path,
        {"A.md": SOUND_ARTIFACT, "B.md": SOUND_ARTIFACT},
        witnessing=1,
        degraded=0,
    )
    assert any(p.startswith("WITNESS_COUNT_UNDECLARED") for p in guard.verdicts(root))


def test_raising_the_declared_number_does_not_buy_a_degraded_artifact(tmp_path: Path) -> None:
    """رفعُ الرقمِ المُعلَنِ لا يشتري تمريرَ أثرٍ يشهدُ بنقصِه — ما دامَ الفارقُ قائمًا."""
    root = _seed(tmp_path, {"A.md": DEGRADED_ENV}, witnessing=1, degraded=0)
    assert any(p.startswith("DEGRADED_ARTIFACT_COMMITTED") for p in guard.verdicts(root))


def test_a_document_without_witness_is_not_counted(tmp_path: Path) -> None:
    root = _seed(
        tmp_path,
        {"A.md": SOUND_ARTIFACT, "PLAIN.md": NO_WITNESS},
        witnessing=1,
        degraded=0,
    )
    assert guard.verdicts(root) == []
    assert guard.measured_counts(root)["witnessing"] == 1


# ———————————————————— الرقمُ يُقرأُ من القيدِ ————————————————————


def test_baseline_is_read_from_the_record(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"A.md": SOUND_ARTIFACT}, witnessing=7, degraded=3)
    assert guard.declared_baseline(root) == {"witnessing": 7, "degraded": 3}


def test_missing_baseline_record_is_raised(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"A.md": SOUND_ARTIFACT}, witnessing=1, degraded=0)
    (root / "docs" / "governance" / "work" / "DISCOVERIES.md").write_text(
        "# لا سطرَ هنا\n", encoding="utf-8"
    )
    with pytest.raises(guard.BaselineRecordMissing):
        guard.declared_baseline(root)


def test_duplicated_baseline_record_is_raised(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"A.md": SOUND_ARTIFACT}, witnessing=1, degraded=0)
    record = root / "docs" / "governance" / "work" / "DISCOVERIES.md"
    record.write_text(record.read_text(encoding="utf-8") * 2, encoding="utf-8")
    with pytest.raises(guard.BaselineRecordMissing):
        guard.declared_baseline(root)


def test_partial_baseline_record_is_raised(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"A.md": SOUND_ARTIFACT}, witnessing=1, degraded=0)
    record = root / "docs" / "governance" / "work" / "DISCOVERIES.md"
    record.write_text(
        "| ... `ARTIFACT_WITNESS_BASELINE: witnessing=2` ... |\n", encoding="utf-8"
    )
    with pytest.raises(guard.BaselineRecordMissing):
        guard.declared_baseline(root)


def test_no_number_is_buried_in_the_tool() -> None:
    """الأداةُ لا تحملُ رقمًا مُعلَنًا مدفونًا — مصدرُ الحقيقةِ القيدُ."""
    source = TOOL_PATH.read_text(encoding="utf-8")
    assert "ARTIFACT_WITNESS_BASELINE" in source
    assert "witnessing=2" not in source


# ———————————————————— عَطبُ القياسِ يُرفَعُ ————————————————————


def test_unreadable_artifact_is_raised_not_swallowed(tmp_path: Path) -> None:
    root = _seed(tmp_path, {"A.md": SOUND_ARTIFACT}, witnessing=1, degraded=0)
    (root / "docs" / "audit" / "B.md").write_bytes(b"\xff\xfe\x00 \xd8\x00")
    with pytest.raises(guard.ArtifactUnreadable):
        guard.witnesses(root)


# ———————————————————— الجذرُ والخُضرةُ ————————————————————


def test_root_discovery_matches_the_shared_finder() -> None:
    """اكتشافُ الجذرِ هنا يُطابِقُ `repo_root.py` — لا قفزَ على الآباءِ (`DISC-046`)."""
    spec = importlib.util.spec_from_file_location(
        "amos_repo_root_parity", REPO_ROOT / "tools" / "governance" / "repo_root.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.discover_repo_root(str(TOOL_PATH)) == REPO_ROOT == guard.REPO_ROOT


def test_green_sentence_carries_its_denominator() -> None:
    """جملةُ نجاحِ هذا الحرسِ تحملُ مقامَها — لا تُزادُ خُضرةٌ صامتةٌ (`DISC-053`)."""
    source = TOOL_PATH.read_text(encoding="utf-8")
    marker = "✓ كلُّ ما قُرِئَ لا يشهدُ بنقصٍ"
    assert marker in source
    tail = source.split(marker, 1)[1][:220]
    assert "measured['witnessing']" in tail


def test_deficiency_marks_are_declared_not_hidden() -> None:
    """صيغُ الشهادةِ مُعلَنةٌ في نصِّ الأداةِ — الحدُّ مكتوبٌ لا مطويٌّ."""
    assert guard.WITNESS_MARKERS
    assert "**غائبة**" in guard.DEFICIENCY_MARKS
    assert "**FAIL**" in guard.DEFICIENCY_MARKS


# ———————————————————— الشجرةُ الحقيقيّةُ ————————————————————


def test_real_tree_check_passes() -> None:
    """الشجرةُ الحقيقيّةُ الآنَ: لا أثرَ مُقيَّدًا يشهدُ بنقصِه."""
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
    assert payload["measured"] == payload["declared"] | {
        "degraded": payload["measured"]["degraded"]
    }
    assert payload["measured"]["degraded"] == 0
    assert all(w["verdict"] in {guard.SOUND, guard.DEGRADED} for w in payload["witnesses"])


def test_real_tree_witness_set_is_the_generated_artifacts() -> None:
    """الشاهدانِ المقيسانِ هما الأثرانِ المُولَّدانِ — لا وثيقةَ مكتوبةً يدًا."""
    paths = {w.path for w in guard.witnesses(REPO_ROOT)}
    assert "docs/audit/CROSS_SYSTEM_SUITE_MATRIX.md" in paths
    assert all(p.startswith("docs/") and p.endswith(".md") for p in paths)
