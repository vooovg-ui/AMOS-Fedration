#!/usr/bin/env python3
"""
حرسُ الطابعِ قبلَ كتابتِه — كلُّ التزامٍ جديدٍ إزاحتُه عالميّةٌ أو يسقُطُ الفحصُ

الهدف: قطعُ **سببِ** نموِّ دَينِ طوابعِ الالتزامِ لا رصدُ أثرِه بعدَ وقوعِه. كانَ
       حرسُ `W-110` بَعديًّا محضًا: يقيسُ المجموعَ فيكشفُ النموَّ **في الدفعةِ
       التاليةِ**، ولا يمنعُ التزامًا مغلوطًا لحظةَ إنشائِه — وهو حدٌّ كانَ
       مُعلَنًا في بندِ `WI-035` ثمَّ **وقعَ مقيسًا**: العقدةُ `66c217b` التي
       أعلنَت `non_utc=134` حملَت نفسُها إزاحةً `+03:00`، فصارَ المقيسُ 135
       والمُعلَنُ 134، فأسقطَت العقدةُ سقّاطتَها بنفسِها في وظيفتَينِ من CI
       (تشغيلٌ `33621763476`). فصارَ الشرطُ هنا: **ما بعدَ العقدةِ المُعلَنةِ
       (`baseline_node`) إزاحتُه `+00:00`** — يُقاسُ محلّيًّا قبلَ الدفعِ وفي CI.
النطاق: طوابعُ الالتزاماتِ الواقعةِ بعدَ العقدةِ المُعلَنةِ حتّى `HEAD`. ولا يُقاسُ
        الماضي: مائةٌ وخمسةٌ وثلاثونَ إزاحةً محلّيّةً تبقى مُعلَنةً مقيسةً، وتصحيحُها
        يوجبُ إعادةَ كتابةِ التاريخِ ومحوَ قيودٍ مدفوعةٍ وهو ممنوعٌ (§ 10 حدًّا 9).
المالك: tests/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-02
تاريخ آخر تعديل: 2026-09-02
"""

from __future__ import annotations

import os
import subprocess

import pytest

from tools.governance.commit_timestamp_integrity import (
    BASELINE_NODE_FIELD,
    REPO_ROOT,
    BaselineNodeUnreachable,
    commits_after_baseline,
    declared_baseline_node,
    forward_violations,
)


def test_العقدةُ_المُعلَنةُ_مكتوبةٌ_في_السطرِ_الواحدِ():
    """حدُّ الماضي والمستقبلِ يُقرأُ من مصدرِ الحقيقةِ الواحدِ لا يُقدَّرُ."""
    node = declared_baseline_node(REPO_ROOT)
    assert len(node) >= 7, f"`{BASELINE_NODE_FIELD}` أقصرُ من أن يُعرَّفَ به التزامٌ: {node}"
    assert all(character in "0123456789abcdef" for character in node), node


def test_كلُّ_التزامٍ_بعدَ_العقدةِ_المُعلَنةِ_إزاحتُه_عالميّةٌ():
    """الحرسُ يقرأُ الشجرةَ الحاضرةَ: خرقٌ واحدٌ يُسقِطُ الفحصَ قبلَ الدفعِ."""
    try:
        violations = forward_violations(REPO_ROOT)
    except BaselineNodeUnreachable as unreachable:
        pytest.skip(
            f"العقدةُ المُعلَنةُ غيرُ مرئيّةٍ في هذه المرآةِ ({unreachable}) — "
            "والشرطُ يُقاسُ في CI بعمقٍ كاملٍ (`fetch-depth: 0`)، ولا تُدَّعى هنا خُضرةٌ"
        )
    assert not violations, (
        "التزامٌ جديدٌ بإزاحةٍ محلّيّةٍ: "
        + " · ".join(f"{sha[:10]}={stamp}" for sha, stamp in violations.items())
        + " — يُعادُ إنشاؤُه بإزاحةٍ `+00:00` (`TZ=UTC git commit`)، "
        "ولا يُرفَعُ الرقمُ المُعلَنُ ليمرَّ الفحصُ"
    )


def test_القياسُ_يُثبِتُ_الفخَّ_على_سجلٍّ_مصنوعٍ(tmp_path):
    """خُضرةٌ بلا فرقٍ ليست دليلًا: يُبنى سجلٌّ فيه الخرقُ فيُقاسُ، ثمَّ يُقاسُ زوالُه."""
    repo = tmp_path / "forged"
    repo.mkdir()

    def run(args: list[str], env_extra: dict[str, str] | None = None) -> str:
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

    run(["init", "-q", "-b", "main", "."])
    run(["config", "user.email", "guard@amos.local"])
    run(["config", "user.name", "Guard"])

    def commit(name: str, stamp: str) -> None:
        (repo / f"{name}.txt").write_text(name, encoding="utf-8")
        run(["add", "-A"])
        run(
            ["commit", "-q", "-m", f"التزامٌ {name}"],
            env_extra={"GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp},
        )

    # العقدةُ المُعلَنةُ نفسُها إزاحتُها محلّيّةٌ — وهي ماضٍ مُجمَّدٌ لا يُقاسُ عليها
    commit("baseline", "2026-01-01T10:00:00+03:00")
    baseline = run(["rev-parse", "HEAD"])

    # ما بعدَها: التزامٌ بإزاحةٍ محلّيّةٍ خرقٌ يُرى
    commit("local_offset", "2026-01-02T10:00:00+03:00")
    seen = forward_violations(repo, baseline)
    assert len(seen) == 1, f"الفخُّ لم يُرَ: {seen}"
    assert next(iter(seen.values())).endswith("+03:00"), seen

    # والتزامٌ عالميُّ الإزاحةِ لا يُبلَّغُ خرقًا — ولا يُخفي الخرقَ الأوّلَ
    commit("utc_offset", "2026-01-03T10:00:00+00:00")
    after = commits_after_baseline(repo, baseline)
    assert len(after) == 2, after
    assert len(forward_violations(repo, baseline)) == 1, forward_violations(repo, baseline)

    # وعقدةٌ مُعلَنةٌ لا تُرى تُعلَنُ ولا تُطوى صامتةً
    with pytest.raises(BaselineNodeUnreachable):
        forward_violations(repo, "0" * 40)
