#!/usr/bin/env python3
"""حرسُ إغلاقِ إنفاذِ الحرسِ — يُثبِتُ أنَّ دعوى الدفعةِ لا تُقبَلُ بلا إنفاذٍ (W-077).

الهدف:
    أن يكونَ معيارُ `guard_enforcement_closure.py` محروسًا لا موصوفًا: كلُّ
    مخالفةٍ تُعلِنُها الأداةُ لها فحصٌ يُثبِتُ اشتعالَها عندَ سببِها **وسكوتَها
    عندَ غيابِه**، وكلُّ قاعدةٍ مكتوبةٍ (حدُّ الجُملةِ · رباطُ الفحصِ بالأداةِ ·
    تجريدُ التشكيلِ) لها فحصٌ يُثبِتُ أنَّها قاعدةٌ تعملُ لا نصٌّ في توصيفٍ.
النطاق:
    شجرةٌ مؤقّتةٌ تُبنى في كلِّ حالةٍ، وفحصانِ يقرآنِ المستودعَ الحقيقيَّ
    ليُثبِتا أنَّ الأداةَ تحكُمُ على الشجرةِ الحاضرةِ ولا تكتبُ فيها. لا شبكةَ
    ولا قاعدةَ بيانات.
المالك: tests/governance — ديوانُ التدقيق
تاريخ الإنشاء: 2026-08-31
تاريخ آخر تعديل: 2026-08-31
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "guard_enforcement_closure.py"


def _load():
    spec = importlib.util.spec_from_file_location(
        "guard_enforcement_closure", TOOL_PATH
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    # لا بدَّ من تسجيلِ الوحدةِ قبلَ تنفيذِها: `dataclass` يقرأُ `sys.modules`.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


GEC = _load()

REGISTER_HEAD = """# سجلٌّ

| المعرِّف | الأثر | المصير |
|---|---|---|
"""


def _write(root: Path, rel: str, text: str) -> None:
    target = root / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def _tree(
    root: Path,
    *,
    discoveries_rows: str = "",
    risk_rows: str = "",
    workflow: str = "jobs:\n  a:\n    steps:\n      - run: echo لا شيء\n",
    files: tuple[str, ...] = (),
    file_bodies: dict[str, str] | None = None,
) -> None:
    """شجرةٌ صغيرةٌ فيها سجلّانِ ومسارُ عملٍ — أقلُّ ما تقرأُه الأداةُ."""
    _write(
        root, "docs/governance/work/DISCOVERIES.md", REGISTER_HEAD + discoveries_rows
    )
    _write(root, "docs/governance/work/RISK_REGISTER.md", REGISTER_HEAD + risk_rows)
    _write(root, ".github/workflows/ci.yml", workflow)
    for rel in files:
        _write(root, rel, (file_bodies or {}).get(rel, "# ملفٌّ للفحصِ\n"))


def _kinds(report) -> list[str]:
    return [v["kind"] for v in report.violations]


# ── الدعوى تُقرأُ كما كُتِبَت ────────────────────────────────────────────────


def test_claim_named_in_a_ci_run_step_is_enforced(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        discoveries_rows=(
            "| DISC-100 | أثرٌ | والحرسُ القائمُ tools/governance/probe.py "
            "يُشغَّلُ في كلِّ دفعةٍ فيُظهِرُ العَطبَ |\n"
        ),
        workflow=(
            "jobs:\n  a:\n    steps:\n      - run: python tools/governance/probe.py\n"
        ),
        files=("tools/governance/probe.py",),
    )
    report = GEC.measure(tmp_path)
    assert [c.verdict for c in report.claims] == ["CI_STEP"]
    assert report.violations == []


def test_claim_without_any_enforcement_path_is_a_violation(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        discoveries_rows=(
            "| DISC-101 | أثرٌ | والحرسُ tools/governance/probe.py يُشغَّلُ في كلِّ دفعةٍ |\n"
        ),
        files=("tools/governance/probe.py",),
    )
    report = GEC.measure(tmp_path)
    assert [c.verdict for c in report.claims] == ["UNENFORCED"]
    assert _kinds(report) == ["PUSH_CLAIM_UNENFORCED"]
    assert "DISC-101" in report.violations[0]["detail"]


def test_claimed_path_absent_from_the_tree_is_a_violation(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        discoveries_rows=(
            "| DISC-102 | أثرٌ | والحرسُ tools/governance/ghost.py يُشغَّلُ في كلِّ دفعةٍ |\n"
        ),
        workflow=(
            "jobs:\n  a:\n    steps:\n      - run: python tools/governance/ghost.py\n"
        ),
    )
    report = GEC.measure(tmp_path)
    assert [c.verdict for c in report.claims] == ["PATH_MISSING"]
    assert _kinds(report) == ["PUSH_CLAIM_PATH_MISSING"]


def test_risk_register_is_read_too(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        risk_rows=(
            "| RK-100 | أثرٌ | ويحرسُه tools/governance/probe.py يُشغَّلُ في كلِّ دفعةٍ |\n"
        ),
        files=("tools/governance/probe.py",),
    )
    report = GEC.measure(tmp_path)
    assert [c.row_id for c in report.claims] == ["RK-100"]
    assert _kinds(report) == ["PUSH_CLAIM_UNENFORCED"]


def test_no_claim_written_means_no_violation(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        discoveries_rows="| DISC-103 | أثرٌ | وصفٌ بلا دعوى دفعةٍ |\n",
        files=("tools/governance/probe.py",),
    )
    report = GEC.measure(tmp_path)
    assert report.claims == []
    assert report.violations == []


# ── حدُّ الجُملةِ: لا تُحمَلُ ملفّاتُ الخليّةِ كلُّها على عبارةٍ واحدةٍ ──────


def test_path_in_another_clause_is_not_attributed_to_the_claim(tmp_path: Path) -> None:
    """`؛` تفصلُ جملةً عن جملةٍ، فما بعدَها لا يُحاسَبُ بدعوى ما قبلَها."""
    _tree(
        tmp_path,
        discoveries_rows=(
            "| DISC-104 | أثرٌ | و tools/governance/unwired.py يُصنِّفُ الأحكامَ؛ "
            "ويحرسُ معيارَه في كلِّ دفعةٍ tests/governance/test_probe.py |\n"
        ),
        workflow=("jobs:\n  a:\n    steps:\n      - run: python -m pytest tests/ -q\n"),
        files=("tools/governance/unwired.py", "tests/governance/test_probe.py"),
    )
    report = GEC.measure(tmp_path)
    assert [c.path for c in report.claims] == ["tests/governance/test_probe.py"]
    assert [c.verdict for c in report.claims] == ["CI_PYTEST"]
    assert report.violations == []


def test_claim_phrase_is_read_without_diacritics(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        discoveries_rows=(
            "| DISC-105 | أثرٌ | tools/governance/probe.py يُشغَّلُ فِي كُلِّ دَفْعَةٍ |\n"
        ),
        files=("tools/governance/probe.py",),
    )
    report = GEC.measure(tmp_path)
    assert len(report.claims) == 1


# ── رباطُ الفحصِ بالأداةِ: نصٌّ وصفيٌّ لا يُقرأُ حرسًا ───────────────────────


REAL_TREE_TEST_BODY = """from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "probe.py"


def test_real_tree() -> None:
    assert TOOL_PATH.is_file()
    assert REPO_ROOT.is_dir()
"""

MENTION_ONLY_BODY = '''from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ROW = "| tools/governance/probe.py | 2026-08-27 | مثالٌ لا حرسٌ |"


def test_real_tree() -> None:
    """يذكرُ اسمَ الأداةِ في جدولٍ مُصطنَعٍ ولا يحكُمُ عليها."""
    assert REPO_ROOT.is_dir()
    assert ROW
'''

TMP_ONLY_BODY = """from pathlib import Path

TOOL_PATH = Path("tools") / "governance" / "probe.py"


def test_tmp_only(tmp_path: Path) -> None:
    assert tmp_path.is_dir()
    assert TOOL_PATH.name
"""


def _real_tree_case(tmp_path: Path, body: str):
    _tree(
        tmp_path,
        discoveries_rows=(
            "| DISC-106 | أثرٌ | tools/governance/probe.py يُشغَّلُ في كلِّ دفعةٍ |\n"
        ),
        workflow=(
            "jobs:\n  a:\n    steps:\n      - run: python -m pytest tests/governance/ -q\n"
        ),
        files=("tools/governance/probe.py", "tests/governance/test_probe.py"),
        file_bodies={"tests/governance/test_probe.py": body},
    )
    return GEC.measure(tmp_path)


def test_real_tree_test_bound_to_the_tool_enforces_the_claim(tmp_path: Path) -> None:
    report = _real_tree_case(tmp_path, REAL_TREE_TEST_BODY)
    assert [c.verdict for c in report.claims] == ["REAL_TREE_TEST"]
    assert "test_real_tree" in report.claims[0].evidence
    assert report.violations == []


def test_descriptive_mention_is_not_read_as_a_binding(tmp_path: Path) -> None:
    """ذِكرُ اسمِ الأداةِ في نصٍّ لا يجعلُ الفحصَ حرسًا لها."""
    report = _real_tree_case(tmp_path, MENTION_ONLY_BODY)
    assert [c.verdict for c in report.claims] == ["UNENFORCED"]
    assert _kinds(report) == ["PUSH_CLAIM_UNENFORCED"]


def test_tmp_tree_only_test_does_not_enforce_the_claim(tmp_path: Path) -> None:
    """فحصٌ يبني شجرةً مؤقّتةً لا يحكُمُ على الشجرةِ الحاضرةِ."""
    report = _real_tree_case(tmp_path, TMP_ONLY_BODY)
    assert [c.verdict for c in report.claims] == ["UNENFORCED"]


def test_import_of_the_tool_is_a_binding(tmp_path: Path) -> None:
    body = "import probe\nfrom pathlib import Path\n\nREPO_ROOT = Path(__file__).resolve().parents[2]\n\n\ndef test_real_tree() -> None:\n    assert probe\n    assert REPO_ROOT.is_dir()\n"
    report = _real_tree_case(tmp_path, body)
    assert [c.verdict for c in report.claims] == ["REAL_TREE_TEST"]


# ── الرفضُ مُصنَّفٌ لا نتيجةٌ خالية ─────────────────────────────────────────


def test_missing_register_is_a_classified_refusal(tmp_path: Path) -> None:
    _tree(tmp_path)
    (tmp_path / "docs/governance/work/RISK_REGISTER.md").unlink()
    report = GEC.measure(tmp_path)
    assert report.refusal.startswith("REGISTER_MISSING")
    assert report.claims == []
    assert GEC.main(["--root", str(tmp_path)]) == 2


def test_missing_workflows_is_a_classified_refusal(tmp_path: Path) -> None:
    _tree(tmp_path)
    (tmp_path / ".github/workflows/ci.yml").unlink()
    report = GEC.measure(tmp_path)
    assert report.refusal.startswith("WORKFLOWS_MISSING")
    assert GEC.main(["--root", str(tmp_path)]) == 2


def test_unparsable_covered_test_file_is_refused_not_read_as_unbound(tmp_path: Path) -> None:
    """ملفُّ فحصٍ معطوبٌ نحويًّا يُرفَضُ الحكمُ عندَه، ولا يُقرأُ سكوتُه «لا رباطَ»."""
    _tree(
        tmp_path,
        discoveries_rows=(
            "| DISC-104 | أثرٌ | والحرسُ القائمُ tools/governance/probe.py "
            "يُشغَّلُ في كلِّ دفعةٍ |\n"
        ),
        workflow=(
            "jobs:\n  a:\n    steps:\n      - run: python -m pytest tests/governance/ -q\n"
        ),
        files=("tools/governance/probe.py", "tests/governance/test_broken.py"),
        file_bodies={"tests/governance/test_broken.py": "def test_x(:\n    pass\n"},
    )
    report = GEC.measure(tmp_path)
    assert report.refusal.startswith("SOURCE_UNPARSABLE")
    assert report.claims == []
    assert report.violations == []
    assert GEC.main(["--root", str(tmp_path)]) == 2


def test_broken_source_raises_instead_of_claiming_no_binding() -> None:
    """الدالّتانِ ترفعانِ ولا تُعيدانِ حكمًا مبنيًّا على قراءةٍ فاشلةٍ."""
    with pytest.raises(GEC.UnparsableSource):
        GEC.binds_tool("def f(:\n", "probe")
    with pytest.raises(GEC.UnparsableSource):
        GEC.real_tree_tests("def f(:\n")


# ── الجردُ إبلاغٌ لا إسقاطٌ ──────────────────────────────────────────────────


def test_unwired_tool_inventory_reports_and_does_not_fail(tmp_path: Path) -> None:
    _tree(tmp_path, files=("tools/governance/unwired.py",))
    report = GEC.measure(tmp_path)
    inventory = [n for n in report.notes if n["kind"] == "UNWIRED_TOOL_INVENTORY"]
    assert inventory and "tools/governance/unwired.py" in inventory[0]["detail"]
    assert report.violations == []
    assert GEC.main(["--root", str(tmp_path)]) == 0


def test_exit_code_is_one_when_a_claim_is_unenforced(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        discoveries_rows=(
            "| DISC-107 | أثرٌ | tools/governance/probe.py يُشغَّلُ في كلِّ دفعةٍ |\n"
        ),
        files=("tools/governance/probe.py",),
    )
    assert GEC.main(["--root", str(tmp_path)]) == 1


# ── الشجرةُ الحقيقيّةُ تُقاسُ ولا تُكتَبُ ────────────────────────────────────


def test_real_repository_claims_are_all_enforced() -> None:
    """الحرسُ الذي يُسقِطُ دعوى دفعةٍ تُكتَبُ اليومَ بلا طريقِ إنفاذٍ."""
    report = GEC.measure(REPO_ROOT)
    assert report.refusal == ""
    assert report.claims, "لا دعوى مقروءةً في السجلَّينِ — الحرسُ يقيسُ فراغًا"
    assert report.violations == []


def test_real_repository_is_not_written_to() -> None:
    before = {
        path: path.stat().st_mtime_ns
        for path in (
            REPO_ROOT / "docs/governance/work/DISCOVERIES.md",
            REPO_ROOT / "docs/governance/work/RISK_REGISTER.md",
            REPO_ROOT / ".github/workflows/ci.yml",
        )
    }
    GEC.measure(REPO_ROOT)
    assert {p: p.stat().st_mtime_ns for p in before} == before
