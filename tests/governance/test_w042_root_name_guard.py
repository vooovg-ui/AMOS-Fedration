"""الهدف: حراسةُ الحرسِ الذي بُنِيَ في W-042 — تحويلُ القاعدةِ 14 من نصٍّ في دليلِ
المشروعِ إلى فحصٍ يُسقِطُ البناءَ، فلا يعودَ غريبٌ يهبِطُ جذرَ المستودعِ وتمرُّ
وظائفُ خضراءُ فوقَه.

الخطرُ الذي تحرسُه هذه الفحوصُ أربعةٌ:

١. أن يعودَ ما جرى في `W-038`: شجرةٌ بُنِيَت من مفاتيحِ فهرسةِ الأجسامِ لا من
   خريطةِ المساراتِ، فتهبِطُ ملفّاتٌ أسماؤها `0…12` في الجذرِ **ولا تحمرُّ بوّابةٌ**.
٢. أن يصيرَ الحرسُ نمطًا مفتوحًا يمنعُ الأرقامَ وحدَها، فيَمُرَّ غريبٌ اسمُه
   `blob` أو `tmp` أو بصمةٌ سِتَّ عشريّةٌ. فالإعلانُ **مُغلَقٌ** لا مفتوحًا.
٣. أن يتعفَّنَ الإعلانُ: أن يُحذَفَ ملفٌّ جذريٌّ مُعلَنٌ فيبقى اسمُه في القائمةِ
   ويُظَنَّ الحرسُ قائمًا — فالمُعلَنُ الغائبُ مخالفةٌ كذلك.
٤. أن يُبنى الحرسُ **ولا يُربَطَ** في CI ولا يُذكَرَ في القاعدةِ 14، فيصيرَ ملفًّا
   لا بوّابةً (القاعدةُ 12: حارسٌ يُتخطَّى بصمتٍ ليس حارسًا).

والفحوصُ تقرأُ المصدرَ نصًّا وتبني شجرةً مؤقّتةً، ولا تستوردُ حزمةَ الخدماتِ،
عملًا بقاعدةِ الحوكمةِ: فحصُ الحوكمةِ لا يعتمدُ على بيئةِ التنفيذِ التي يحكمُ
عليها.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

from tools.governance.repo_root import discover_repo_root  # noqa: E402

ROOT = discover_repo_root(__file__)
TOOL = ROOT / "tools/governance/check_root_file_names.py"
WORKFLOW = ROOT / ".github/workflows/ci.yml"
HANDBOOK = ROOT / "docs/PROJECT_HANDBOOK.md"


def _load():
    """استوردِ الأداةَ من مسارِها بلا حزمةٍ.

    يُسجَّلُ الموديولُ في `sys.modules` قبلَ التنفيذِ للسببِ المُعلَنِ في
    `test_w038_probe_measure_mode.py`: قراءةُ الموديولِ من السجلِّ عندَ بناءِ
    الأصنافِ مع `from __future__ import annotations`.
    """
    spec = importlib.util.spec_from_file_location("w042_root_names", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["w042_root_names"] = module
    spec.loader.exec_module(module)
    return module


def _real_source() -> str:
    """مصدرُ أسماءِ الشجرةِ الحقيقيّةِ — مُعلَنٌ لا مُستنتَجٌ داخلَ الأداةِ.

    في CI سجلُّ git حاضرٌ فيُقاسُ منه (‏وهو ما تُشغِّلُه البوّابةُ 8). وفي بيئةِ
    عاملٍ استُنسِخَت بواجهةِ الكائناتِ بلا سجلٍّ، يُعلَنُ القرصُ صريحًا هنا — ولا
    تهبِطُ الأداةُ إليه من نفسِها.
    """
    return "git" if (ROOT / ".git").is_dir() else "disk"


def _fake_root(base: Path, declared: dict) -> Path:
    """شجرةٌ مؤقّتةٌ نظيفةٌ: كلُّ مُعلَنٍ حاضرٌ ولا غريبَ فيها."""
    root = base / "repo"
    root.mkdir(parents=True, exist_ok=True)
    for name in declared:
        (root / name).write_text("# الهدف: ملفُّ اختبارٍ مؤقّتٌ\n", encoding="utf-8")
    (root / "docs").mkdir(exist_ok=True)
    (root / "docs" / "README.md").write_text("# الهدف: بطاقةٌ\n", encoding="utf-8")
    return root


def test_the_real_tree_is_clean() -> None:
    """شجرةُ المستودعِ الحاضرةُ لا غريبَ فيها — وهذا هو الحكمُ المقيسُ لا المُفترَضُ."""
    mod = _load()
    violations, source = mod.audit(ROOT, _real_source())
    assert violations == [], violations
    assert source


def test_declaration_matches_the_real_root() -> None:
    """الإعلانُ = ملفّاتُ الجذرِ الفعليّةُ، لا أكثرَ ولا أقلَّ."""
    mod = _load()
    files, _ = mod.collect(ROOT, _real_source())
    real = {rel.name for rel in files if len(Path(rel).parts) == 1}
    assert real == set(mod.DECLARED_ROOT_FILES), {
        "غيرُ مُعلَنٍ": sorted(real - set(mod.DECLARED_ROOT_FILES)),
        "مُعلَنٌ غائبٌ": sorted(set(mod.DECLARED_ROOT_FILES) - real),
    }


def test_clean_fake_tree_has_no_violation(tmp_path: Path) -> None:
    mod = _load()
    root = _fake_root(tmp_path, mod.DECLARED_ROOT_FILES)
    violations, _ = mod.audit(root, "disk")
    assert violations == [], violations


def test_index_key_name_in_root_is_caught(tmp_path: Path) -> None:
    """بصمةُ حادثةِ W-038 بعينِها: ملفٌّ اسمُه رقمٌ محضٌ في الجذرِ."""
    mod = _load()
    root = _fake_root(tmp_path, mod.DECLARED_ROOT_FILES)
    (root / "12").write_text("محتوًى صحيحٌ بايتًا واسمٌ خاطئٌ\n", encoding="utf-8")
    violations, _ = mod.audit(root, "disk")
    kinds = {v["kind"] for v in violations if v["path"] == "12"}
    assert "INDEX_KEY_NAME" in kinds
    assert "ROOT_FILE_WITHOUT_SUFFIX" in kinds


def test_index_key_name_deeper_in_the_tree_is_caught(tmp_path: Path) -> None:
    """الاسمُ الرقميُّ يُلاحَقُ في كلِّ الشجرةِ لا في الجذرِ وحدَه."""
    mod = _load()
    root = _fake_root(tmp_path, mod.DECLARED_ROOT_FILES)
    (root / "docs" / "5").write_text("غريبٌ في عمقِ الشجرةِ\n", encoding="utf-8")
    violations, _ = mod.audit(root, "disk")
    assert any(
        v["kind"] == "INDEX_KEY_NAME" and v["path"].endswith("5")
        for v in violations
    ), violations


def test_undeclared_root_file_is_caught_even_with_a_normal_name(tmp_path: Path) -> None:
    """الحرسُ إعلانٌ مُغلَقٌ: اسمٌ حسنُ الهيئةِ لا يمرُّ بلا إعلانٍ."""
    mod = _load()
    root = _fake_root(tmp_path, mod.DECLARED_ROOT_FILES)
    (root / "NOTES.md").write_text("# الهدف: مذكّرةٌ\n", encoding="utf-8")
    violations, _ = mod.audit(root, "disk")
    assert any(
        v["kind"] == "UNDECLARED_ROOT_FILE" and v["path"] == "NOTES.md"
        for v in violations
    ), violations


def test_missing_declared_file_is_caught(tmp_path: Path) -> None:
    """المُعلَنُ الغائبُ مخالفةٌ — لئلّا يتعفَّنَ الإعلانُ فيَضعُفَ الحرسُ بلا حُمرةٍ."""
    mod = _load()
    root = _fake_root(tmp_path, mod.DECLARED_ROOT_FILES)
    (root / "README.md").unlink()
    violations, _ = mod.audit(root, "disk")
    assert any(
        v["kind"] == "DECLARED_FILE_MISSING" and v["path"] == "README.md"
        for v in violations
    ), violations


def test_exit_codes_and_json_report(tmp_path: Path, capsys) -> None:
    """رمزُ 0 للنظيفةِ و1 للمخالفةِ، والحكمُ يُكتَبُ ملفًّا حينَ يُطلَبُ."""
    mod = _load()
    root = _fake_root(tmp_path, mod.DECLARED_ROOT_FILES)
    out = tmp_path / "verdict.json"

    assert mod.main([str(root), "--source", "disk", "--json", str(out)]) == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["summary"]["total"] == 0
    assert sorted(payload["declared_root_files"]) == sorted(mod.DECLARED_ROOT_FILES)

    (root / "9").write_text("غريبٌ\n", encoding="utf-8")
    assert mod.main([str(root), "--source", "disk", "--json", str(out)]) == 1
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["summary"]["INDEX_KEY_NAME"] == 1
    capsys.readouterr()


def test_missing_root_is_usage_error(tmp_path: Path) -> None:
    mod = _load()
    assert mod.main([str(tmp_path / "لا-وجودَ-له")]) == 2


def test_absent_git_history_does_not_fall_back_silently(tmp_path: Path) -> None:
    """شجرةٌ بلا سجلِّ git تُرفَعُ برمزِ 2 لا تُقاسُ من القرصِ بلا إعلانٍ.

    الهبوطُ الصامتُ إلى مصدرٍ آخرَ هو عينُ علّةِ `W-038`: حرسٌ يقيسُ شجرةً غيرَ
    التي يُظَنُّ أنّه يقيسُها. فالمصدرُ يُعلَنُ بيدِ المُشغِّلِ أو يرتفعُ.
    """
    mod = _load()
    root = _fake_root(tmp_path, mod.DECLARED_ROOT_FILES)
    assert mod.main([str(root)]) == 2
    assert mod.main([str(root), "--source", "disk"]) == 0


def test_the_tool_writes_nothing_into_the_tree_it_judges() -> None:
    """الحارسُ لا يكتبُ ما يحكمُ عليه — المحرَّمةُ الأصليّةُ."""
    mod = _load()
    before = {rel for rel, _ in [(r, None) for r in mod.collect(ROOT, _real_source())[0]]}
    mod.audit(ROOT, _real_source())
    after = {rel for rel, _ in [(r, None) for r in mod.collect(ROOT, _real_source())[0]]}
    assert before == after


def test_the_gate_is_wired_in_ci() -> None:
    """حارسٌ غيرُ مربوطٍ ليس حارسًا (القاعدةُ 12)."""
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "tools/governance/check_root_file_names.py" in text


def test_rule_fourteen_points_at_its_guard() -> None:
    """القاعدةُ 14 تُشيرُ إلى فحصِها — نصٌّ بلا فحصٍ أضعفُ من بوّابةٍ."""
    text = HANDBOOK.read_text(encoding="utf-8")
    assert "check_root_file_names.py" in text
