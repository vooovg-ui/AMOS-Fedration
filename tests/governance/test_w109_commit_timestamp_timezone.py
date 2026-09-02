#!/usr/bin/env python3
"""
حرسُ منطقةِ زمنِ الالتزامِ — Commit Timestamp Timezone Guard

الهدف: منعُ عودةِ الفخِّ المُعلَنِ في `COMPLETION_LEDGER.md § 10` حدًّا 8: أن
       يُشتَقَّ «تاريخُ آخرِ تعديلٍ» من سجلِّ git **بمنطقةِ الالتزامِ نفسِه** أو
       أن يُشتَقَّ «اليومُ» **بمنطقةِ الجهازِ** — فيرى جهازٌ بـ+03:00 قربَ
       منتصفِ الليلِ يومًا غيرَ الذي يراهُ CI بـ+00:00، فتسقطَ بوّابتانِ بلا
       عَطبٍ حقيقيٍّ (وقعَ فعلًا في `W-005`).
النطاق: اشتقاقُ التاريخِ في `tools/governance/stamp_readme_identity.py` وحدَه.
        لا يحرسُ هذا الملفُّ صدقَ طابعِ الالتزامِ نفسِه (حدٌّ 9) — ذاك دَينٌ آخرُ
        يبقى مُعلَنًا ولا يُقرأُ هذا الحرسُ إبراءً منه.
المالك: tools/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-02
تاريخ آخر تعديل: 2026-09-02

## لِمَ لا يكفي فحصٌ نصّيٌّ وحدَه
خُضرةٌ بلا فرقٍ ليست دليلًا. فهذا الحرسُ **يُثبِتُ أوّلًا أنَّ الفخَّ حقيقيٌّ**:
يبني مستودعًا صغيرًا فيه التزامٌ طابعُه `+03:00` قربَ منتصفِ الليلِ، فيَقيسُ أنَّ
`--date=short` يُري يومًا و`--date=format-local:%Y-%m-%d` بـ`TZ=UTC` يُري اليومَ
الآخرَ — ثمَّ يقيسُ أنَّ الأداةَ تُرجِعُ **يومَ UTC** لا يومَ منطقةِ الالتزامِ.
"""

from __future__ import annotations

import ast
import os
import subprocess

import pytest

from tools.governance.repo_root import discover_repo_root

REPO_ROOT = discover_repo_root(__file__)

# التزامٌ عندَ 01:30 بـ+03:00 = 22:30 من اليومِ السابقِ بالتوقيتِ العالميّ
COMMIT_STAMP = "2026-01-02T01:30:00+03:00"
LOCAL_DAY = "2026-01-02"
UTC_DAY = "2026-01-01"


def _run(args: list[str], cwd, env_extra: dict[str, str] | None = None) -> str:
    env = {**os.environ, **(env_extra or {})}
    out = subprocess.run(
        args, cwd=cwd, capture_output=True, text=True, timeout=30, check=False, env=env
    )
    if out.returncode != 0:
        raise AssertionError(f"فشلَ الأمرُ {args}: {out.stderr.strip()}")
    return out.stdout.strip()


@pytest.fixture(scope="module")
def repo_with_offset_commit(tmp_path_factory):
    """مستودعٌ صغيرٌ فيه التزامٌ واحدٌ طابعُه +03:00 قربَ منتصفِ الليلِ."""
    root = tmp_path_factory.mktemp("tz_trap")
    _run(["git", "init", "-q", "-b", "main", "."], cwd=root)
    _run(["git", "config", "user.email", "guard@amos.local"], cwd=root)
    _run(["git", "config", "user.name", "Guard"], cwd=root)
    (root / "README.md").write_text("# ملفٌّ للقياسِ\n", encoding="utf-8")
    _run(["git", "add", "README.md"], cwd=root)
    _run(
        ["git", "commit", "-q", "-m", "قياسُ منطقةِ الزمنِ"],
        cwd=root,
        env_extra={"GIT_AUTHOR_DATE": COMMIT_STAMP, "GIT_COMMITTER_DATE": COMMIT_STAMP},
    )
    return root


def test_الفخُّ_حقيقيٌّ_لا_مفترَضٌ(repo_with_offset_commit):
    """`--date=short` يُري يومَ منطقةِ الالتزامِ، والمُوحَّدُ يُري يومَ UTC."""
    root = repo_with_offset_commit
    naive = _run(
        ["git", "log", "-1", "--format=%ad", "--date=short", "--", "README.md"], cwd=root
    )
    normalized = _run(
        [
            "git", "log", "-1", "--format=%ad",
            "--date=format-local:%Y-%m-%d", "--", "README.md",
        ],
        cwd=root,
        env_extra={"TZ": "UTC"},
    )
    assert naive == LOCAL_DAY, f"الطابعُ الخامُ تغيَّرَ عمّا قِيسَ: {naive}"
    assert normalized == UTC_DAY, f"المُوحَّدُ ليسَ يومَ UTC: {normalized}"
    assert naive != normalized, (
        "لا فرقَ بينَ الاشتقاقَينِ في هذه البيئةِ، فالحرسُ يقيسُ خُضرةً بلا معنًى — "
        "يُراجَعُ الطابعُ لا يُسكَتُ الفحصُ"
    )


def test_الأداةُ_تشتقُّ_يومَ_UTC_لا_يومَ_منطقةِ_الالتزامِ(repo_with_offset_commit, monkeypatch):
    """`git_last_modified` تُرجِعُ يومَ UTC ولو كانَ الالتزامُ بمنطقةٍ أُخرى."""
    from tools.governance import stamp_readme_identity as stamper

    root = repo_with_offset_commit
    monkeypatch.setattr(stamper, "REPO_ROOT", root)
    monkeypatch.setenv("TZ", "Asia/Riyadh")
    got = stamper.git_last_modified(root / "README.md")
    assert got == UTC_DAY, (
        f"الأداةُ أرجعَت «{got}» والمُنتظَرُ يومَ UTC «{UTC_DAY}» — "
        "عادَ الاشتقاقُ إلى منطقةِ الالتزامِ (‏حدُّ § 10 رقم 8)"
    )


def test_اليومُ_يُقرأُ_بـUTC_لا_بمنطقةِ_الجهازِ():
    """`utc_today()` لا يتبعُ منطقةَ الجهازِ، ولا بقيَ نداءٌ لـ`date.today()`."""
    from datetime import datetime, timezone

    from tools.governance import stamp_readme_identity as stamper

    assert stamper.utc_today() == datetime.now(timezone.utc).date().isoformat()
    source = (REPO_ROOT / "tools/governance/stamp_readme_identity.py").read_text(
        encoding="utf-8"
    )
    offenders = [
        node.lineno
        for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "today"
    ]
    assert not offenders, (
        "عادَ اشتقاقُ اليومِ إلى منطقةِ الجهازِ (‏نداءُ `.today()`) في الأسطرِ: "
        + " · ".join(str(n) for n in offenders)
    )


def test_لا_يُشتَقُّ_تاريخٌ_بـshort_في_الأداةِ():
    """`--date=short` ممنوعٌ في هذه الأداةِ: هو عينُ الفخِّ المُعلَنِ."""
    source = (REPO_ROOT / "tools/governance/stamp_readme_identity.py").read_text(
        encoding="utf-8"
    )
    tree = ast.parse(source)
    literals = [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    ]
    docstrings = {
        ast.get_docstring(node, clean=False)
        for node in ast.walk(tree)
        if isinstance(node, ast.Module | ast.FunctionDef | ast.ClassDef)
    }
    code = "\n".join(lit for lit in literals if lit not in docstrings)
    assert "--date=short" not in code, (
        "`--date=short` يُصيِّرُ التاريخَ تابعًا لمنطقةِ الالتزامِ — يُستبدَلُ بـ"
        "`--date=format-local:%Y-%m-%d` مع `TZ=UTC`، ولا يُخفَّفُ الفحصُ"
    )
