#!/usr/bin/env python3
"""
نطاقُ قياسِ الطوابعِ: عقدةُ الدمجِ التي تُولِّدُها المنصّةُ ليست من تاريخِ المستودعِ

الهدف: قطعُ **سببِ** لاحتميّةِ حكمِ CI على حدثِ `pull_request` (‏`DISC-065`) لا
       مطاردةِ عَرَضِه بإعادةِ الدفعِ: كانَ حرسا `W-110` و`W-113` يقيسانِ
       `git log HEAD`، و`HEAD` في فحصِ طلبِ الدمجِ **عقدةُ دمجٍ عارضةٌ
       يُولِّدُها GitHub** في `refs/pull/<N>/merge` بإزاحةِ ساعةِ المُولِّدِ —
       فحملَت `+03:00` مرّةً (‏تشغيلا 30 و32: `non_utc` مقيسٌ 136 والمُعلَنُ 135)
       و`+00:00` مرّةً على الشجرةِ نفسِها (‏تشغيلُ 28 أخضرَ 13/13)، والشجرةُ
       المُراجَعةُ واحدةٌ. فصارَ الشرطُ هنا: **يُستثنى ما لا يملكُه المستودعُ
       وحدَه، ويُقاسُ كلُّ تاريخِ أبوَيه، ويُعلَنُ الاستثناءُ**.
النطاق: مدى القياسِ فقط. لا يُرفَعُ رقمٌ مُعلَنٌ، ولا يُخفَّفُ شرطٌ، ولا يُستثنى
        التزامٌ يحويه فرعٌ أو وسمٌ ولو كانَ دمجًا — والخرقُ الحقيقيُّ يبقى مقيسًا.
المالك: tests/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-14
تاريخ آخر تعديل: 2026-09-14
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

from tools.governance.commit_timestamp_integrity import (
    REPO_ROOT,
    forward_violations,
    measure,
    measurement_scope,
    platform_merge_head,
)


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
    """سجلٌّ مصنوعٌ يُعادُ فيه عَطبُ `DISC-065` بعينِه: عقدةُ دمجٍ عارضةٌ بإزاحةٍ محلّيّةٍ."""
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

    baseline = commit("baseline", "2026-01-01T10:00:00+00:00")
    _git(repo, ["checkout", "-q", "-b", "work"])
    branch_tip = commit("work", "2026-01-02T10:00:00+00:00")

    # مرجعُ الدمجِ العارضُ: عقدةٌ لا يحويها فرعٌ، طابعُها محلّيُّ الإزاحةِ
    _git(repo, ["checkout", "-q", "--detach", "main"])
    _git(
        repo,
        ["merge", "-q", "--no-ff", "--no-edit", "-m", "Merge pull request #1", "work"],
        env_extra={
            "GIT_AUTHOR_DATE": "2026-01-03T10:00:00+03:00",
            "GIT_COMMITTER_DATE": "2026-01-03T10:00:00+03:00",
        },
    )
    ephemeral = _git(repo, ["rev-parse", "HEAD"])
    _git(repo, ["update-ref", "refs/pull/1/merge", ephemeral])
    return {
        "repo": repo,
        "baseline": baseline,
        "branch_tip": branch_tip,
        "ephemeral": ephemeral,
    }


def test_العقدةُ_العارضةُ_تُعرَفُ_ولا_تُقاسُ(forged):
    """شرطُ الاستثناءِ ثلاثيٌّ مقيسٌ: دمجٌ · لا يحويه فرعٌ · آباؤُه مرئيّونَ."""
    repo = forged["repo"]
    assert platform_merge_head(repo) == forged["ephemeral"]
    revs, excluded = measurement_scope(repo)
    assert excluded == forged["ephemeral"], (revs, excluded)
    assert set(revs) == {forged["baseline"], forged["branch_tip"]}, revs


def test_الاستثناءُ_لا_يُخفي_خرقًا_ولا_يُنقِصُ_دَينًا(forged):
    """يُقاسُ **كلُّ** تاريخِ الأبوَينِ: عددُ الالتزاماتِ يبقى، والخرقُ الحقيقيُّ يُرى."""
    repo = forged["repo"]
    counts = measure(repo)
    assert counts["commits"] == 2, counts  # الأبوانِ كلاهما مقيسانِ، والعارضةُ وحدَها استُثنِيَت
    assert counts["non_utc"] == 0, counts
    assert not forward_violations(repo, forged["baseline"]), forward_violations(
        repo, forged["baseline"]
    )

    # وخرقٌ حقيقيٌّ على فرعٍ يبقى مقيسًا بعدَ الاستثناءِ — فليس الاستثناءُ بابًا
    _git(repo, ["checkout", "-q", "work"])
    (repo / "breach.txt").write_text("breach", encoding="utf-8")
    _git(repo, ["add", "-A"])
    _git(
        repo,
        ["commit", "-q", "-m", "خرقٌ حقيقيٌّ"],
        env_extra={
            "GIT_AUTHOR_DATE": "2026-01-04T10:00:00+03:00",
            "GIT_COMMITTER_DATE": "2026-01-04T10:00:00+03:00",
        },
    )
    breach = _git(repo, ["rev-parse", "HEAD"])
    assert platform_merge_head(repo) is None, "رأسٌ على فرعٍ ليس عقدةً عارضةً"
    assert measure(repo)["non_utc"] == 1, measure(repo)
    assert breach in forward_violations(repo, forged["baseline"])


def test_دمجٌ_يحويه_فرعٌ_يُقاسُ_ولا_يُستثنى(forged):
    """عقدةٌ يحويها مرجعُ المستودعِ من تاريخِه: تُقاسُ ولو كانت دمجًا بإزاحةٍ محلّيّةٍ."""
    repo = forged["repo"]
    _git(repo, ["branch", "-f", "merged", forged["ephemeral"]])
    assert platform_merge_head(repo) is None
    revs, excluded = measurement_scope(repo)
    assert (revs, excluded) == (["HEAD"], None)
    assert measure(repo)["non_utc"] == 1, measure(repo)


def test_مستودعُ_العملِ_نفسُه_يُقاسُ_بلا_استثناءٍ():
    """على مرآةِ العملِ (‏رأسٌ على فرعٍ) لا استثناءَ — فلا يُغيِّرُ الإصلاحُ نطاقًا سليمًا."""
    revs, excluded = measurement_scope(REPO_ROOT)
    if excluded is not None:  # فحصُ طلبِ دمجٍ في CI: الاستثناءُ مشروعٌ ومُعلَنٌ
        pytest.skip(f"الرأسُ عقدةُ دمجٍ عارضةٌ ({excluded[:10]}) — والشرطُ مقيسٌ في اختبارِ الفخِّ")
    assert (revs, excluded) == (["HEAD"], None)
