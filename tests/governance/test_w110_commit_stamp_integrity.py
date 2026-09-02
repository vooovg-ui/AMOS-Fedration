#!/usr/bin/env python3
"""
حرسُ صدقِ طوابعِ الالتزامِ — Commit Timestamp Integrity Guard

الهدف: منعُ نموِّ حدِّ الصدقِ 9 في [`COMPLETION_LEDGER.md § 10`]: التزامٌ بإزاحةٍ
       غيرِ `+00:00`، أو طابعٌ مكرَّرٌ بينَ التزامَينِ مختلفَينِ (‏علامةُ طابعٍ
       محفورٍ نصًّا لا مقروءٍ من ساعةٍ — وقعَ في `W-023`…`W-027`)، أو طفلٌ يسبقُ
       أباهُ زمنًا. **الحدُّ لا يُصحَّحُ ماضيًا** لأنَّ تصحيحَه يوجبُ إعادةَ كتابةِ
       التاريخِ ومحوَ قيودٍ مدفوعةٍ — فيُحرَسُ من النموِّ ويُقرأُ مقيسًا.
النطاق: سجلُّ الالتزاماتِ المرئيُّ للفحصِ. ولا يُقاسُ ما لا يُرى: على مرآةٍ ضحلةٍ
        تُعلَنُ الضحالةُ ويُكتفى بمنعِ النموِّ، وفي CI (`fetch-depth: 0`) يُقاسُ
        السجلُّ كاملًا ويُطلَبُ خفضُ المُعلَنِ إن انخفضَ المقيسُ.
المالك: tools/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-02
تاريخ آخر تعديل: 2026-09-02

## حدٌّ مُعلَنٌ صراحةً (W-112)
لا يُدَّعى هنا أنَّ كلَّ التزامٍ إزاحتُه عالميّةٌ: قِيسَ في CI أنَّ **134** التزامًا
تحملُ إزاحةً محلّيّةً. فالمحروسُ **ألّا يعلوَ العددُ**، لا أن يكونَ صفرًا.
"""

from __future__ import annotations

import subprocess

import pytest

from tools.governance.commit_timestamp_integrity import (
    BASELINE_FIELDS,
    REPO_ROOT,
    declared_baseline,
    has_full_history,
    measure,
)


@pytest.fixture(scope="module")
def measured() -> dict[str, int]:
    return measure(REPO_ROOT)


def test_دَينُ_طوابعِ_الالتزامِ_لا_يعلو(measured):
    """أيُّ حقلٍ يعلو على المُعلَنِ إخفاقٌ — والمُعلَنُ يُقرأُ من سجلِّ الاكتشافاتِ."""
    declared = declared_baseline(REPO_ROOT)
    grown = {
        field: (measured[field], declared[field])
        for field in BASELINE_FIELDS
        if measured[field] > declared[field]
    }
    assert not grown, (
        "عَلا دَينُ طوابعِ الالتزامِ: "
        + " · ".join(f"{k}: مقيسٌ {m} · المُعلَنُ {d}" for k, (m, d) in grown.items())
        + " — يُصحَّحُ الطابعُ في الالتزامِ الجديدِ (‏ساعةٌ تُقرأُ · إزاحةٌ `+00:00`)، "
        "ولا يُرفَعُ الرقمُ المُعلَنُ ليمرَّ الفحصُ"
    )


def test_انخفاضُ_المقيسِ_يوجِبُ_خفضَ_المُعلَنِ_على_سجلٍّ_كاملٍ(measured):
    """على سجلٍّ كاملٍ: مُعلَنٌ أرخى من الواقعِ سقّاطةٌ كاذبةٌ، فيُخفَضُ."""
    if not has_full_history(REPO_ROOT, measured):
        pytest.skip(
            "سجلٌّ ناقصٌ (‏مرآةٌ أقلُّ من العددِ المُعلَنِ): القياسُ على جزءٍ فلا يُطلَبُ "
            "خفضٌ — وفي CI يُستنسَخُ بعمقٍ كاملٍ (`fetch-depth: 0`) فيُقاسُ هذا الشرطُ"
        )
    declared = declared_baseline(REPO_ROOT)
    shrunk = {
        field: (measured[field], declared[field])
        for field in BASELINE_FIELDS
        if measured[field] < declared[field]
    }
    assert not shrunk, (
        "انخفضَ المقيسُ ولم يُخفَضِ المُعلَنُ: "
        + " · ".join(f"{k}: مقيسٌ {m} · المُعلَنُ {d}" for k, (m, d) in shrunk.items())
        + " — يُخفَضُ في سطرِ `COMMIT_STAMP_BASELINE:` داخلَ docs/governance/work/DISCOVERIES.md"
    )


def test_القياسُ_يُثبِتُ_الفخَّ_على_سجلٍّ_مصنوعٍ(tmp_path):
    """خُضرةٌ بلا فرقٍ ليست دليلًا: يُبنى سجلٌّ فيه العيوبُ الثلاثةُ فتُقاسُ."""
    repo = tmp_path / "forged"
    repo.mkdir()

    def run(args: list[str], env_extra: dict[str, str] | None = None) -> None:
        import os

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

    run(["init", "-q", "-b", "main", "."])
    run(["config", "user.email", "guard@amos.local"])
    run(["config", "user.name", "Guard"])
    forged = "2026-01-02T10:00:00+00:00"
    for index, (stamp, name) in enumerate(
        [(forged, "أ"), (forged, "ب"), ("2026-01-01T10:00:00+03:00", "ج")]
    ):
        (repo / f"f{index}.txt").write_text(name, encoding="utf-8")
        run(["add", "-A"])
        run(
            ["commit", "-q", "-m", f"التزامٌ {name}"],
            env_extra={"GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp},
        )

    got = measure(repo)
    assert got["duplicate_groups"] == 1, got
    assert got["duplicate_commits"] == 2, got
    assert got["non_utc"] == 1, got
    assert got["non_monotonic"] == 1, got
