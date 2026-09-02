"""
حرسُ مُكتشِفِ جذرِ المستودعِ — العلامةُ تُثبِتُ، والغيابُ يُرفَعُ لا يُخمَّنُ
الهدف: إثباتُ أنَّ `tools/governance/repo_root.py` يُعطي جذرًا **مُثبَتًا بعلامةٍ** مهما اختلفَ عُمقُ الطالبِ، وأنَّه **يرفعُ خطأً** إذا غابَت العلامةُ بدلَ أن يهبطَ إلى تخمينٍ (`DISC-041` · `WI-032`).
النطاق: tests/governance/ (`WI-032`)
المالك: tests/governance/
تاريخ الإنشاء: 2026-09-02
تاريخ آخر تعديل: 2026-09-02

لماذا هذا الحرسُ:
    المُكتشِفُ نفسُه صارَ محلَّ القياسِ لعشراتِ الفحوصِ. فإن هبطَ صامتًا مرّةً واحدةً
    صارَ العَطبُ **مركزيًّا** بدلَ أن يكونَ متفرِّقًا — فيُقاسُ هو أوّلًا:
    اكتشافٌ من أعماقٍ مختلفةٍ · ورفعٌ صريحٌ عندَ الغيابِ · وثباتُ الجذرِ عندَ نقلِ الملفِّ
    (‏وهو عينُ العَطبِ الذي يُعالَج: `parents[N]` يتغيَّرُ بالنقلِ، والعلامةُ لا تتغيَّرُ).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.governance.repo_root import (
    ROOT_MARKERS,
    RepositoryRootNotFound,
    discover_repo_root,
    is_repository_root,
)


def _build_tree(base: Path) -> Path:
    """يبني شجرةً مُعلَّمةً فيها مجلَّداتٌ متفاوتةُ العُمقِ."""
    root = base / "repo"
    (root / "docs" / "governance" / "work").mkdir(parents=True)
    (root / "PROJECT_STATE.md").write_text("حالةٌ", encoding="utf-8")
    (root / "docs" / "governance" / "work" / "THE_ROADMAP.md").write_text("خارطةٌ", encoding="utf-8")
    return root


def test_يُكتشَفُ_الجذرُ_من_أعماقٍ_مختلفةٍ(tmp_path: Path) -> None:
    """الجذرُ واحدٌ مهما بعُدَ الطالبُ — ولا عُمقَ مكتوبًا في الطريقِ."""
    root = _build_tree(tmp_path)
    shallow = root / "tools"
    deep = root / "tests" / "governance" / "nested" / "deeper"
    shallow.mkdir()
    deep.mkdir(parents=True)
    (shallow / "a.py").write_text("", encoding="utf-8")
    (deep / "b.py").write_text("", encoding="utf-8")

    assert discover_repo_root(shallow / "a.py") == root
    assert discover_repo_root(deep / "b.py") == root
    assert discover_repo_root(root) == root


def test_نقلُ_الملفِّ_لا_يُغيِّرُ_الجذرَ_المُكتشَفَ(tmp_path: Path) -> None:
    """عينُ العَطبِ المُعالَجِ: `parents[N]` يتغيَّرُ بالنقلِ، والعلامةُ لا تتغيَّرُ."""
    root = _build_tree(tmp_path)
    first = root / "tests" / "governance"
    second = root / "tools" / "governance" / "inner"
    first.mkdir(parents=True)
    second.mkdir(parents=True)
    (first / "moved.py").write_text("", encoding="utf-8")

    before = discover_repo_root(first / "moved.py")
    (first / "moved.py").rename(second / "moved.py")
    after = discover_repo_root(second / "moved.py")

    assert before == after == root, "الجذرُ تغيَّرَ بنقلِ الملفِّ — وهذا العَطبُ نفسُه"

    depth_based_before = (first / "moved.py").resolve().parents[2]
    depth_based_after = (second / "moved.py").resolve().parents[2]
    assert depth_based_before != depth_based_after, (
        "الشجرةُ المبنيّةُ لا تُظهِرُ الفرقَ، فالمقارنةُ لا تُثبِتُ شيئًا"
    )


def test_غيابُ_العلامةِ_يُرفَعُ_ولا_يُخمَّنُ(tmp_path: Path) -> None:
    """لا هبوطَ صامتًا إلى جذرٍ «معقولٍ»: خطأٌ يُسمّي الموضعَ."""
    bare = tmp_path / "بلا_علامةٍ" / "عميقٌ"
    bare.mkdir(parents=True)
    (bare / "c.py").write_text("", encoding="utf-8")

    with pytest.raises(RepositoryRootNotFound) as raised:
        discover_repo_root(bare / "c.py")
    assert str(bare.resolve()) in str(raised.value), "الخطأُ لا يُسمّي الموضعَ"


def test_علامةٌ_ناقصةٌ_ليست_جذرًا(tmp_path: Path) -> None:
    """اجتماعُ العلاماتِ شرطٌ — وواحدةٌ منها لا تكفي."""
    half = tmp_path / "نصفُ_جذرٍ"
    half.mkdir()
    (half / "PROJECT_STATE.md").write_text("حالةٌ", encoding="utf-8")

    assert not is_repository_root(half)
    with pytest.raises(RepositoryRootNotFound):
        discover_repo_root(half)


def test_الجذرُ_الحقيقيُّ_يُكتشَفُ_من_هذا_الملفِّ() -> None:
    """قياسٌ على الشجرةِ الحقيقيّةِ لا على المؤقَّتةِ وحدَها."""
    root = discover_repo_root(__file__)
    assert (root / "docs" / "audit" / "COMPLETION_LEDGER.md").exists()
    for marker in ROOT_MARKERS:
        assert (root / marker).exists(), f"علامةٌ مفقودةٌ في الجذرِ الحقيقيِّ: {marker}"
