#!/usr/bin/env python3
"""
اختبارُ الوجهِ الرابعِ: إزاحةُ رأسِ الفرعِ المدفوعِ (W-179 · WI-041 · DISC-049)

الهدف: التحقُّقُ من أنَّ الوجهَ الرابعَ في `commit_timestamp_integrity.py`\n       يكشفُ الإزاحةَ المحلّيّةَ في رأسِ الفرعِ المدفوعِ لا المحلّيِّ وحدَه.\n
النطاق: اختبارُ الوجهِ الجديدِ وحدَه — لا يُمسُّ الحرسانِ القائمانِ (W-110 · W-113).
nالمالك: tools/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-10-02 (W-179 · WI-041)
nالمسار: tools/governance/commit_timestamp_integrity.py
n"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

from tools.governance.commit_timestamp_integrity import (
    PushedHeadUnreadable,
    pushed_head_is_utc,
    pushed_head_offset,
    pushed_head_stamp,
    pushed_head_violation,
    upstream_ref,
)


def _git(args: list[str], repo: Path) -> str:
    out = subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, timeout=60, check=False
    )
    if out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {out.stderr.strip()}")
    return out.stdout.strip()


@pytest.fixture
def temp_repo(tmp_path: Path) -> Path:
    """مستودعُ git مؤقَّتٌ بفرعٍ بعيدٍ يُحاكي المدفوعَ."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(["init", "-b", "main"], repo)
    _git(["config", "user.name", "test"], repo)
    _git(["config", "user.email", "test@test.com"], repo)
    # التزامٌ أوّلُ بإزاحةٍ عالميّةٍ
    (repo / "file.txt").write_text("hello", encoding="utf-8")
    _git(["add", "file.txt"], repo)
    _git(["commit", "-m", "init"], repo)
    # أنشئ مستودعًا بعيدًا وادفَعْ إليه
    remote = tmp_path / "remote.git"
    _git(["init", "--bare", "-b", "main", str(remote)], repo)
    _git(["remote", "add", "origin", str(remote)], repo)
    _git(["push", "-u", "origin", "main"], repo)
    return repo


def test_الوجهُ_الرابعُ_يقيسُ_إزاحةَ_رأسِ_الفرعِ_المدفوعِ(temp_repo: Path):
    """الوجهُ الرابعُ يقرأُ المرجعَ البعيدَ ويُعيدُ طابعَه."""
    ref, stamp = pushed_head_stamp(temp_repo)
    assert "origin/main" in ref or "main" in ref
    # طابعُ الالتزامِ بصيغةِ ISO 8601
    assert "T" in stamp


def test_الإزاحةُ_العالميّةُ_تمرُّ_سالمةً(temp_repo: Path):
    """التزامٌ بإزاحةِ +00:00 يُقرأُ عالميًّا — فلا خرقَ."""
    # الالتزامُ الأوّلُ أُنشئَ بإزاحةِ المنشئِ المحلّيّةِ — نُنشئُ آخرَ بـTZ=UTC
    (temp_repo / "file2.txt").write_text("world", encoding="utf-8")
    _git(["add", "file2.txt"], temp_repo)
    env = {"TZ": "UTC", "PATH": os.environ["PATH"]}
    subprocess.run(
        ["git", "commit", "-m", "utc commit"],
        cwd=temp_repo, capture_output=True, text=True, timeout=60,
        check=True, env={**os.environ, **env},
    )
    _git(["push", "origin", "main"], temp_repo)
    assert pushed_head_is_utc(temp_repo) is True
    assert pushed_head_violation(temp_repo) is None


def test_الإزاحةُ_المحلّيّةُ_تُكشَفُ_خرقًا(temp_repo: Path):
    """طابعٌ بإزاحةٍ محلّيّةٍ (+03:00) في رأسِ الفرعِ المدفوعِ — يُسقِطُ الفحصَ.

    هذه طفرةٌ مقصودةٌ: التزامٌ بإزاحةٍ غيرِ عالميّةٍ يُدفَعُ إلى المرجعِ البعيدِ،
    فيكشفُهُ الوجهُ الرابعُ لا الحرسانِ القائمانِ (W-110 · W-113) اللذانِ يقرآنِ المحلّيَّ.
    """
    # أنشئ التزامًا بإزاحةٍ محلّيّةٍ (+03:00)
    (temp_repo / "bad.txt").write_text("bad", encoding="utf-8")
    _git(["add", "bad.txt"], temp_repo)
    # استخدم GIT_AUTHOR_DATE و GIT_COMMITTER_DATE لإجبارِ إزاحةٍ محلّيّةٍ
    env = {
        **os.environ,
        "GIT_AUTHOR_DATE": "2026-10-02T10:00:00+03:00",
        "GIT_COMMITTER_DATE": "2026-10-02T10:00:00+03:00",
    }
    subprocess.run(
        ["git", "commit", "-m", "bad tz"],
        cwd=temp_repo, capture_output=True, text=True, timeout=60,
        check=True, env=env,
    )
    _git(["push", "origin", "main"], temp_repo)
    # الوجهُ الرابعُ يكشفُ الخرقَ
    violation = pushed_head_violation(temp_repo)
    assert violation is not None, "طابعٌ بإزاحةٍ +03:00 لم يُكشَفْ — الوجهُ الرابعُ معطوبٌ"
    ref, stamp = next(iter(violation.items()))
    assert "+03:00" in stamp
    assert pushed_head_is_utc(temp_repo) is False
    offset = pushed_head_offset(temp_repo)
    assert offset == "+03:00"


def test_غيابُ_المرجعِ_البعيدِ_مُعلَنٌ_لا_مطويٌّ(tmp_path: Path, capsys):
    """لا مرجعَ بعيدَ — فالوجهُ يُعلِنُ غيابَه ولا يُخمِّنُ."""
    repo = tmp_path / "noremote"
    repo.mkdir()
    _git(["init", "-b", "main"], repo)
    _git(["config", "user.name", "test"], repo)
    _git(["config", "user.email", "test@test.com"], repo)
    (repo / "file.txt").write_text("hello", encoding="utf-8")
    _git(["add", "file.txt"], repo)
    _git(["commit", "-m", "init"], repo)
    # لا remote — pushed_head_violation تُعيدُ None (غيابٌ مُعلَنٌ)
    assert pushed_head_violation(repo) is None
    captured = capsys.readouterr()
    assert "لم يُقَس" in captured.err
    # ولكن pushed_head_stamp ترفعُ PushedHeadUnreadable
    with pytest.raises(PushedHeadUnreadable):
        pushed_head_stamp(repo)


def test_upstream_ref_يقرأُ_المرجعَ_البعيدَ(temp_repo: Path):
    """upstream_ref تُعيدُ اسمَ المرجعِ البعيدِ المتتبَّعِ."""
    ref = upstream_ref(temp_repo)
    assert "origin/main" in ref or "main" in ref
