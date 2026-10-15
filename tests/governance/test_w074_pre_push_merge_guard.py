#!/usr/bin/env python3
"""
حرسُ إزاحةِ التزامِ الدمجِ قبلَ الدفعِ — الوجهُ الصريحُ للمدى (`Q-E` · `WI-074`)

الهدف: قطعُ **سببِ** دخولِ التزامِ دمجٍ بإزاحةٍ محلّيّةٍ إلى `main` قبلَ أن يُدفَعَ
       لا رصدُ أثرِهِ بعدَ وصولِهِ. كانَ الحرسُ القائمُ (`W-110`/`W-113` · بوّابةُ
       `Identity Law`) بَعديًّا على حدثِ `push`: يكشفُ التزامَ الدمجِ الحاملَ للإزاحةِ
       **بعدَ** أن يدخلَ `main`. فالوجهُ هنا **صريحُ المدى**: يُطالَبُ بمرجعٍ أساسٍ
       ورأسٍ مُثبَتَينِ بـSHA، ويُقاسُ كلُّ التزامِ دمجٍ في المدى بينهما قبلَ الدفعِ.
النطاق: واجهةُ `pre_push_merge_guard.guard_report` وحدَها — مدىً صريحٌ (`base..head`)
        على شجرةٍ مصنوعةٍ (‏آباءُ مُعلَنونَ) لا على شجرةِ المستودعِ الحيّةِ (‏فذلكَ
        حكمُ `test_w113`/`test_w164` القائمِ). ولا يُرفَعُ رقمٌ مُعلَنٌ ولا يُغيَّرُ
        `baseline_node`.
المالك: tests/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-10-15 (W-335 · WI-074)
تاريخ آخر تعديل: 2026-10-15 (W-335 · المرّةُ الأولى)
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

import importlib.util

_GUARD_PATH = (
    Path(__file__).resolve().parents[2] / "tools" / "governance" / "pre_push_merge_guard.py"
)
_GUARD_SPEC = importlib.util.spec_from_file_location("amos_pre_push_merge_guard", _GUARD_PATH)
if _GUARD_SPEC is None or _GUARD_SPEC.loader is None:
    raise ImportError(f"pre_push_merge_guard.py not loadable from {_GUARD_PATH}")
guard = importlib.util.module_from_spec(_GUARD_SPEC)
_GUARD_SPEC.loader.exec_module(guard)


def _git(repo: Path, args: list[str], env_extra: dict[str, str] | None = None) -> str:
    out = subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
        env={**os.environ, **(env_extra or {})},
    )
    if out.returncode != 0:
        raise AssertionError(f"فشلَ `git {' '.join(args)}`: {out.stderr.strip()}")
    return out.stdout.strip()


@pytest.fixture()
def forged(tmp_path: Path) -> dict[str, object]:
    """سجلٌّ مصنوعٌ يُعادُ فيه عَطبُ `W-293` بعينِهِ: التزامُ دمجٍ حقيقيٌّ بإزاحةٍ محلّيّةٍ."""
    repo = tmp_path / "forged"
    repo.mkdir()
    _git(repo, ["init", "-q", "-b", "main", "."])
    _git(repo, ["config", "user.email", "guard@amos.local"])
    _git(repo, ["config", "user.name", "Guard"])

    def commit(name: str, stamp: str) -> str:
        (repo / f"{name}.txt").write_text(name, encoding="utf-8")
        _git(repo, ["add", "-A"])
        _git(
            repo,
            ["commit", "-q", "-m", f"التزامٌ {name}"],
            env_extra={"GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp},
        )
        return _git(repo, ["rev-parse", "HEAD"])

    base = commit("base", "2026-01-01T10:00:00+00:00")
    _git(repo, ["checkout", "-q", "-b", "work"])
    tip = commit("work", "2026-01-02T10:00:00+00:00")
    # التزامُ دمجٍ حقيقيٌّ بإزاحةٍ محلّيّةٍ — عَطبُ `8186ec8` نفسُهُ (`W-329`)
    _git(repo, ["checkout", "-q", "main"])
    _git(
        repo,
        ["merge", "-q", "--no-ff", "--no-edit", "-m", "Merge branch 'work'", "work"],
        env_extra={
            "GIT_AUTHOR_DATE": "2026-01-03T10:00:00+03:00",
            "GIT_COMMITTER_DATE": "2026-01-03T10:00:00+03:00",
        },
    )
    breach_merge = _git(repo, ["rev-parse", "HEAD"])
    _git(repo, ["checkout", "-q", "work"])
    return {
        "repo": repo,
        "base": base,
        "tip": tip,
        "breach_merge": breach_merge,
    }


def test_دمجٌ_حقيقيٌّ_بإزاحةٍ_محلّيّةٍ_يُرفَضُ(forged):
    """الوجهُ الصريحُ: التزامُ الدمجِ الحقيقيُّ الحاملُ للإزاحةِ يسقُطُ الحرسُ بهِ."""
    repo = forged["repo"]
    report, code = guard.guard_report(
        repo=repo,
        base_ref=forged["base"],
        head_ref=forged["breach_merge"],
    )
    assert code == 1, (report, code)
    assert forged["breach_merge"][:10] in report, report
    assert "+03:00" in report, report


def test_دمجٌ_حقيقيٌّ_بإزاحةٍ_عالميّةٍ_يُقبَلُ(tmp_path):
    """المسموحُ صراحةً: `TZ=UTC git merge --no-ff` — التزامُ الدمجِ العالميُّ يمرُّ.

    شجرةٌ مستقلّةٌ لا تحملُ التزامَ الدمجِ الحقيقيَّ الحاملَ للإزاحةِ (‏`breach_merge`)
    في نسبِها — فالحكمُ على المدى لا يُحمَرُّ بسببِ عقدةٍ خارجةٍ عنهُ.
    """
    repo = tmp_path / "utc_only"
    repo.mkdir()
    _git(repo, ["init", "-q", "-b", "main", "."])
    _git(repo, ["config", "user.email", "guard@amos.local"])
    _git(repo, ["config", "user.name", "Guard"])

    def commit(name: str, stamp: str) -> str:
        (repo / f"{name}.txt").write_text(name, encoding="utf-8")
        _git(repo, ["add", "-A"])
        _git(
            repo,
            ["commit", "-q", "-m", f"التزامٌ {name}"],
            env_extra={"GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp},
        )
        return _git(repo, ["rev-parse", "HEAD"])

    base = commit("base", "2026-01-01T10:00:00Z")
    _git(repo, ["checkout", "-q", "-b", "work"])
    _git(repo, ["commit", "-q", "--allow-empty", "-m", "عملٌ"])
    _git(repo, ["checkout", "-q", "main"])
    _git(
        repo,
        ["merge", "-q", "--no-ff", "--no-edit", "-m", "Merge branch 'work'", "work"],
        env_extra={
            "GIT_AUTHOR_DATE": "2026-01-05T10:00:00Z",
            "GIT_COMMITTER_DATE": "2026-01-05T10:00:00Z",
        },
    )
    utc_merge = _git(repo, ["rev-parse", "HEAD"])
    report, code = guard.guard_report(
        repo=repo,
        base_ref=base,
        head_ref=utc_merge,
    )
    assert code == 0, (report, code)
    assert "إزاحتُه عالميّةٌ" in report, report


def test_تقديمٌ_سريعٌ_بلا_دمجٍ_يمرُّ(forged):
    """التقديمُ السريعُ (fast-forward) مسموحٌ: مدىً بلا التزامِ دمجٍ ⇒ أخضرُ."""
    repo = forged["repo"]
    report, code = guard.guard_report(
        repo=repo,
        base_ref=forged["base"],
        head_ref=forged["tip"],
    )
    assert code == 0, (report, code)
    assert "fast-forward-safe" in report or "لا يحتوي" in report, report


def test_غيابُ_المرجعِ_الأساسِ_خرجٌ_لا_حكمٌ(forged):
    """القاعدةُ 12: غيابُ المرجعِ خرجٌ 2 مُعلَنٌ لا صفرٌ صامتٌ — فلا يُقالَ «أخضرُ»."""
    repo = forged["repo"]
    report, code = guard.guard_report(
        repo=repo,
        base_ref="refs/heads/does-not-exist",
        head_ref=forged["tip"],
    )
    assert code == 2, (report, code)
    assert "لم يُقَس" in report, report


def test_استثناءُ_العقدةِ_العارضةِ_لا_يُخفي_خرقًا(forged):
    """الاستثناءُ (`DISC-065`) لا يُخفي خرقًا حقيقيًّا: عقدةُ دمجٍ عارضةٌ تُستثنى وحدَها."""
    repo = forged["repo"]
    # عقدةُ دمجٍ عارضةٌ: detached HEAD بلا فرعٍ يحويهِ، وطابعُها محلّيُّ الإزاحةِ
    _git(repo, ["checkout", "-q", "--detach", "main"])
    _git(
        repo,
        ["merge", "-q", "--no-ff", "--no-edit", "-m", "Merge pull request #1", "work"],
        env_extra={
            "GIT_AUTHOR_DATE": "2026-01-06T10:00:00+03:00",
            "GIT_COMMITTER_DATE": "2026-01-06T10:00:00+03:00",
        },
    )
    ephemeral = _git(repo, ["rev-parse", "HEAD"])
    _git(repo, ["update-ref", "refs/pull/1/merge", ephemeral])

    # بدونَ الاستثناءِ: الخرقُ الحقيقيُّ (التزامُ الدمجِ `breach_merge`) مقيسٌ
    # لأنّهُ في المدى `base..ephemeral` وَحدهُ لا في الاستثناءِ
    report, code = guard.guard_report(
        repo=repo,
        base_ref=forged["base"],
        head_ref=ephemeral,
        exclude_ephemeral=True,
    )
    # الخرقُ الحقيقيُّ في تاريخِ الأبوَينِ لا يُستثنى — الاستثناءُ أضيقُ من أن يُخفيَهُ
    assert code == 1, (report, code)
    assert forged["breach_merge"][:10] in report, report


def test_العقدةُ_العارضةُ_وحدَها_لا_تُقاسُ_بإزاحتِهَا(tmp_path):
    """إن كانَ المدى يحوي العقدةَ العارضةَ **وحدَها** فلا خرقَ يقيسُ عليها الحرسُ.

    شجرةٌ مستقلّةٌ لا تحملُ التزامَ الدمجِ الحقيقيَّ الحاملَ للإزاحةِ في نسبِها —
    فالاستثناءُ (`DISC-065`) لا يُخفي خرقًا لأنّهُ لا يوجدُ خرقٌ في المدى أصلًا.
    """
    repo = tmp_path / "ephemeral_only"
    repo.mkdir()
    _git(repo, ["init", "-q", "-b", "main", "."])
    _git(repo, ["config", "user.email", "guard@amos.local"])
    _git(repo, ["config", "user.name", "Guard"])

    def commit(name: str, stamp: str) -> str:
        (repo / f"{name}.txt").write_text(name, encoding="utf-8")
        _git(repo, ["add", "-A"])
        _git(
            repo,
            ["commit", "-q", "-m", f"التزامٌ {name}"],
            env_extra={"GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp},
        )
        return _git(repo, ["rev-parse", "HEAD"])

    base = commit("base", "2026-01-01T10:00:00Z")
    _git(repo, ["checkout", "-q", "-b", "work"])
    commit("work", "2026-01-02T10:00:00Z")
    # عقدةُ دمجٍ عارضةٌ فوقَ الشجرةِ السليمةِ — طابعُها لا يُملَكُ ولا يُقاسُ
    _git(repo, ["checkout", "-q", "--detach", "work"])
    _git(
        repo,
        ["merge", "-q", "--no-ff", "--no-edit", "-m", "Merge pull request #2", "main"],
        env_extra={
            "GIT_AUTHOR_DATE": "2026-01-07T10:00:00+03:00",
            "GIT_COMMITTER_DATE": "2026-01-07T10:00:00+03:00",
        },
    )
    ephemeral2 = _git(repo, ["rev-parse", "HEAD"])
    _git(repo, ["update-ref", "refs/pull/2/merge", ephemeral2])

    # استثناءُ العقدةِ العارضةِ: حكمُ المدى لا يحمُرُّ بسببِها وحدَها
    report, code = guard.guard_report(
        repo=repo,
        base_ref=base,
        head_ref=ephemeral2,
        exclude_ephemeral=True,
    )
    # المدى base..ephemeral2 لا يحملُ التزامَ دمجٍ حقيقيًّا — فلا يُحمَرُّ بسببِ
    # العارضةِ وحدَها (`DISC-065`) · وإلا فالحكمُ دالٌّ في إزاحةِ المنصّةِ لا في
    # شجرةِ المستودعِ
    assert code == 0, (report, code)


def test_قدرةُ_الحرسِ_مُعلَنةٌ_لا_مُزعَمَةٌ():
    """الحدُّ المُعلَنُ في توثيقِ الأداةِ: القدرةُ أضيقُ من المنعِ الشاملِ.

    حرسُ `pull_request` لا يمنعُ التزامًا سيُنشِئُهُ `gh pr merge` لاحقًا — والنصُّ
    (`W-293`) باقٍ حظرًا لا حرسًا. هذا الفحصُ يُثبِتُ أنَّ التوثيقَ يقولُ ذلكَ
    صراحةً فلا يُدَّعى سدُّ ذلكَ المسارِ الخادميِّ.
    """
    doc = guard.__doc__ or ""
    assert "لا يمنعُ التزامًا سيُنشِئُهُ الخادمُ لاحقًا" in doc or (
        "فحصُ `pull_request` **لا يمنعُ التزامًا سيُنشِئُهُ `gh pr merge` لاحقًا**"
    ) in doc, "التوثيقُ لا يُعلنُ حدودَ القدرةِ — ادِّعاءٌ أوسعُ من الواقعِ"

def test_دمجٌ_على_detached_بلا_مرجعٍ_لا_يُستثنى(forged):
    """ثغرةُ W-336: رأسٌ على detached HEAD لا يحويه مرجعٌ ليس عقدةَ منصةٍ.

    قبلَ W-336 كانت قائمةُ المراجعِ الفارغةُ تمرُّ من شرطِ «كلُّها عارضةٌ» فَيُعَدُّ
    التزامُ الدمجِ الحقيقيَّ عارضًا ويُستثنى — فاستُثنيَ خرقٌ حقيقيٌّ بغيابِ مرجعٍ.
    """
    repo = forged["repo"]
    # عقدةُ دمجٍ حقيقيّةٍ على detached HEAD بلا أيِّ مرجعٍ يحويها
    _git(repo, ["checkout", "-q", "--detach", "work"])
    _git(
        repo,
        ["merge", "-q", "--no-ff", "--no-edit", "-m", "Merge main", "main"],
        env_extra={
            "GIT_AUTHOR_DATE": "2026-01-08T10:00:00+03:00",
            "GIT_COMMITTER_DATE": "2026-01-08T10:00:00+03:00",
        },
    )
    detached_merge = _git(repo, ["rev-parse", "HEAD"])
    refs = _git(repo, ["for-each-ref", "--contains", detached_merge, "--format=%(refname)"])
    assert refs == "", "الفحصُ يفترضُ لا مرجعَ يحوي العقدةَ"

    # الاستثناءُ لا يعُدُّها عارضةً: الخرقُ مقيسٌ (خرجٌ 1)
    report, code = guard.guard_report(
        repo=repo,
        base_ref=forged["base"],
        head_ref=detached_merge,
        exclude_ephemeral=True,
    )
    assert code == 1, (report, code)
    assert detached_merge[:10] in report, report


def test_سجلٌّ_ضحلٌ_يُعلِنُ_عجزَهُ_بلا_خُضرةٍ(forged):
    """ثغرةُ W-336: استنساخٌ ضحلٌ = قياسٌ على جزءٍ فخرجٌ 2 لا صفرٌ يوهمُ التمامَ.

    قبلَ W-336 كانَ المدى يُقرأُ من مرآةٍ ضحلةٍ فتخرجُ قائمةُ الدمجِ فارغةً
    ويُقالَ «أخضرُ» على شجرةٍ لم يُقرأْ آباؤُها.
    """
    import subprocess as sp
    repo = forged["repo"]
    # استنساخٌ ضحلٌ (عمقٌ 1) من الشجرةِ المُصنوعةِ
    shallow = repo.parent / "shallow_clone"
    sp.run(
        ["git", "clone", "-q", "--depth", "1", f"file://{repo}", str(shallow)],
        check=True, capture_output=True, text=True, timeout=60,
    )
    # العقدةُ في الاستنساخِ موجودةٌ لكنّ آباءَها خارجَ المرآةِ
    report, code = guard.guard_report(
        repo=shallow,
        base_ref="HEAD",
        head_ref="HEAD",
    )
    assert code == 2, (report, code)
    assert "ضحلٌ" in report or "ضحل" in report, report


def test_غيابُ_رأسِ_المدى_خرجٌ_2_لا_صفرٌ(forged):
    """ثغرةُ W-336: رأسٌ غائبٌ = عجزٌ مُعلَنٌ (خرجٌ 2) لا نجاحٌ صامتٌ."""
    repo = forged["repo"]
    report, code = guard.guard_report(
        repo=repo,
        base_ref=forged["base"],
        head_ref="refs/heads/does-not-exist",
    )
    assert code == 2, (report, code)
    assert "لم يُقَس" in report, report

