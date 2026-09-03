#!/usr/bin/env python3
"""
حرسُ سلامةِ أرقامِ حدودِ الصدقِ — إحالةٌ لا تُحَلُّ عَطبٌ يُقاسُ لا يُروى

الهدف: منعُ نموِّ العَطبِ المُقيَّدِ في `DISC-045`: قسمُ حدودِ الصدقِ المُعلَنةِ في
       [`COMPLETION_LEDGER.md § 10`] يُحالُ إليه بعبارةِ «الحدُّ N»، ورقمٌ واحدٌ
       فيه يحملُ **حدَّينِ مختلفَينِ** — فكلُّ إحالةٍ بذاكَ الرقمِ حجّةٌ لا
       تُحَلُّ إلى حدٍّ بعينِه. والترقيمُ **لا يُعادُ** لأنَّ أرقامَه مُحالٌ إليها
       من قيودٍ مدفوعةٍ لا تُمحى، فالعلاجُ المشروعُ: رقمٌ يُقاسُ وسقّاطةٌ لا تعلو.
النطاق: أربعةُ أرقامٍ تُعادُ من النصِّ (‏عددُ الحدودِ · الأرقامُ المكرَّرةُ ·
        الفجواتُ · الإحالاتُ الملتبسةُ) مقابلَ سطرٍ واحدٍ مُعلَنٍ في
        [`DISCOVERIES.md`]. ولا يُقاسُ هنا **صدقُ الحدِّ** ولا مضمونُه.
المالك: tests/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.governance.truth_limit_integrity import (
    BASELINE_FIELDS,
    BASELINE_KEY,
    LIMITS_FIELD,
    RATCHET_FIELDS,
    REPO_ROOT,
    ScanUnreadable,
    ambiguous_references,
    declared_baseline,
    declared_limit_numbers,
    duplicate_numbers,
    measure,
    numbering_gaps,
    references,
    verdict,
)

#: قسمٌ مصنوعٌ فيه العُيوبُ الثلاثةُ معًا — الحرسُ يُثبِتُ أنَّه يراها.
FORGED_SECTION = """# سجلٌّ مصنوعٌ للفحصِ

## 10 · حدودُ الصدقِ المُعلَنة

1. **حدٌّ أوّلُ** — نصٌّ.
2. **حدٌّ ثانٍ** — نصٌّ.
2. **حدٌّ ثالثٌ برقمٍ مكرَّرٍ** — نصٌّ.
5. **حدٌّ رابعٌ بعدَ فجوةٍ** — نصٌّ.

## 11 · قسمٌ آخرُ لا يُقاسُ

7. **ليس حدًّا** — خارجَ القسمِ فلا يُعَدُّ.
"""

FORGED_REFERENCES = """# وثيقةٌ مصنوعةٌ

الحدُّ 2 يُحتَجُّ به مرّتَينِ: الحدُّ 2 أيضًا — وكلاهما ملتبسٌ.
والحدُّ 1 يُحَلُّ إلى حدٍّ واحدٍ فلا يُعَدُّ التباسًا.
وتغطيةُ الشِّفرةِ حدُّها 90% — نسبةٌ لا إحالةٌ.
"""


def _forge(
    tmp_path: Path,
    *,
    section: str = FORGED_SECTION,
    baseline: str = "TRUTH_LIMIT_BASELINE: limits=4 duplicate_numbers=1 gaps=2 ambiguous_references=2",
    extra: str | None = FORGED_REFERENCES,
) -> Path:
    """مستودعٌ مصنوعٌ: قسمٌ وسطرٌ مُعلَنٌ وإحالاتٌ — يُقاسُ فيه لا في الشجرةِ الحيّةِ."""
    (tmp_path / "docs" / "audit").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs" / "governance" / "work").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs" / "audit" / "COMPLETION_LEDGER.md").write_text(section, encoding="utf-8")
    (tmp_path / "docs" / "governance" / "work" / "DISCOVERIES.md").write_text(
        f"# اكتشافاتٌ مصنوعةٌ\n\n{baseline}\n", encoding="utf-8"
    )
    if extra is not None:
        (tmp_path / "docs" / "REFS.md").write_text(extra, encoding="utf-8")
    return tmp_path


# ─────────────────────────────────────────────────────────────────────────────
# 1 · إثباتُ أنَّ القياسَ يرى العَطبَ — قبلَ أن يُقاسَ به شيءٌ
# ─────────────────────────────────────────────────────────────────────────────


def test_القياسُ_يرى_التكرارَ_والفجوةَ_في_قسمٍ_مصنوعٍ(tmp_path):
    """خُضرةٌ بلا فرقٍ لا تُقاسُ: القياسُ يُجرَّبُ على نصٍّ عُيوبُه معروفةٌ."""
    repo = _forge(tmp_path)
    numbers = declared_limit_numbers(repo)
    assert numbers == [1, 2, 2, 5], numbers
    assert duplicate_numbers(numbers) == {2: 2}
    assert numbering_gaps(numbers) == [3, 4]
    assert measure(repo) == {
        LIMITS_FIELD: 4,
        "duplicate_numbers": 1,
        "gaps": 2,
        "ambiguous_references": 2,
    }


def test_الإحالةُ_الملتبسةُ_تُعَدُّ_والنسبةُ_المئويّةُ_لا_تُعَدُّ(tmp_path):
    """الرقمُ المكرَّرُ إحالتُه ملتبسةٌ، و«90%» نسبةٌ لا حجّةٌ على حدٍّ."""
    repo = _forge(tmp_path)
    ambiguous = ambiguous_references(repo)
    assert ambiguous == {"docs/REFS.md": [2, 2]}, ambiguous
    hits = references(repo)["docs/REFS.md"]
    assert 90 not in hits, hits
    assert hits.count(1) == 1, hits


def test_قسمٌ_سليمُ_الترقيمِ_لا_يُبلَّغُ_عنه(tmp_path):
    """ولا يُخفي الفخُّ عكسَه: نصٌّ سليمٌ يُقاسُ سليمًا فلا حرسٌ بلا معنًى."""
    clean = """# سجلٌّ مصنوعٌ

## 10 · حدودُ الصدقِ المُعلَنة

1. **حدٌّ أوّلُ** — نصٌّ.
2. **حدٌّ ثانٍ** — نصٌّ.
"""
    repo = _forge(
        tmp_path,
        section=clean,
        baseline="TRUTH_LIMIT_BASELINE: limits=2 duplicate_numbers=0 gaps=0 ambiguous_references=0",
        extra="والحدُّ 1 يُحَلُّ إلى حدٍّ واحدٍ.\n",
    )
    assert measure(repo) == {
        LIMITS_FIELD: 2,
        "duplicate_numbers": 0,
        "gaps": 0,
        "ambiguous_references": 0,
    }
    assert verdict(repo) == (0, [])


# ─────────────────────────────────────────────────────────────────────────────
# 2 · السقّاطةُ لا تعلو ولا تُترَكُ رخوةً ولا يُحذَفُ حدٌّ في الظلِّ
# ─────────────────────────────────────────────────────────────────────────────


def test_نموُّ_الالتباسِ_يُسقِطُ_الفحصَ(tmp_path):
    """رقمٌ مقيسٌ أعلى من المُعلَنِ = عَطبٌ اتَّسعَ، فلا يمرُّ بصمتٍ."""
    repo = _forge(
        tmp_path,
        baseline="TRUTH_LIMIT_BASELINE: limits=4 duplicate_numbers=1 gaps=2 ambiguous_references=1",
    )
    code, problems = verdict(repo)
    assert code == 1
    assert any("ambiguous_references" in p and "علا" in p for p in problems), problems


def test_انخفاضُ_المقيسِ_يوجبُ_خفضَ_المُعلَنِ(tmp_path):
    """سقّاطةٌ رخوةٌ تُخفي عودةَ العَطبِ — فالانخفاضُ يُوجِبُ التصحيحَ لا يُغتفَرُ."""
    repo = _forge(
        tmp_path,
        baseline="TRUTH_LIMIT_BASELINE: limits=4 duplicate_numbers=1 gaps=2 ambiguous_references=9",
    )
    code, problems = verdict(repo)
    assert code == 1
    assert any("لم يُخفَضِ المُعلَنُ" in p for p in problems), problems


def test_حذفُ_حدٍّ_مُعلَنٍ_يُسقِطُ_الفحصَ(tmp_path):
    """حذفُ حدِّ صدقٍ إخفاءُ فشلٍ لا إصلاحُه — فنقصانُ العددِ يُسقِطُ الفحصَ."""
    shrunk = """# سجلٌّ مصنوعٌ

## 10 · حدودُ الصدقِ المُعلَنة

1. **حدٌّ أوّلُ** — نصٌّ.
"""
    repo = _forge(
        tmp_path,
        section=shrunk,
        baseline="TRUTH_LIMIT_BASELINE: limits=4 duplicate_numbers=0 gaps=0 ambiguous_references=0",
        extra=None,
    )
    code, problems = verdict(repo)
    assert code == 1
    assert any("حُذِفَ" in p for p in problems), problems


def test_زيادةُ_حدٍّ_توجِبُ_إعلانَ_عددِه(tmp_path):
    """حدٌّ يُزادُ في الظلِّ يُفسِدُ الإحالةَ لاحقًا — فالعددُ يُعلَنُ صراحةً."""
    repo = _forge(
        tmp_path,
        baseline="TRUTH_LIMIT_BASELINE: limits=3 duplicate_numbers=1 gaps=2 ambiguous_references=2",
    )
    code, problems = verdict(repo)
    assert code == 1
    assert any("زِيدَ" in p for p in problems), problems


def test_ملفُّ_قياسٍ_لا_يُقرأُ_يُسقِطُ_القياسَ_ولا_يُتخطّى_بصمتٍ(tmp_path):
    """تخطّي ملفٍّ بصمتٍ يُنقِصُ الإحالاتَ فيُقرأُ خفضًا كاذبًا — فيُرفَعُ عَطبٌ."""
    repo = _forge(tmp_path)
    (repo / "docs" / "BROKEN.md").write_bytes(b"\xff\xfe\x00\x9c\x9d")
    with pytest.raises(ScanUnreadable):
        references(repo)


# ─────────────────────────────────────────────────────────────────────────────
# 3 · الشجرةُ الحيّةُ: المُعلَنُ يُطابِقُ المقيسَ الآنَ
# ─────────────────────────────────────────────────────────────────────────────


def test_الرقمُ_المُعلَنُ_في_الشجرةِ_الحيّةِ_يُطابِقُ_المقيسَ():
    """سقّاطةُ المستودعِ نفسِه: لا نموَّ ولا رخاوةَ، والعددُ مُعلَنٌ مُطابِقٌ."""
    measured = measure(REPO_ROOT)
    declared = declared_baseline(REPO_ROOT)
    assert declared == {k: measured[k] for k in BASELINE_FIELDS}, (
        f"سطرُ `{BASELINE_KEY}` لا يُطابِقُ المقيسَ — مقيسٌ {measured} · المُعلَنُ {declared}. "
        "يُصحَّحُ الرقمُ المُعلَنُ ولا يُخفَّفُ الفحصُ"
    )
    code, problems = verdict(REPO_ROOT)
    assert code == 0, problems


def test_مصدرُ_الرقمِ_المُعلَنِ_سطرٌ_واحدٌ_لا_ثابتٌ_في_فحصٍ():
    """مصدرُ حقيقةٍ واحدٌ: لو تكرَّرَ السطرُ أو غابَ حقلٌ رُفِعَ خطأٌ لا خُمِّنَ رقمٌ."""
    declared = declared_baseline(REPO_ROOT)
    assert set(declared) == set(BASELINE_FIELDS)
    assert set(RATCHET_FIELDS) < set(BASELINE_FIELDS)
    text = (REPO_ROOT / "docs/governance/work/DISCOVERIES.md").read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if BASELINE_KEY in ln]
    assert len(lines) == 1, f"سطرُ `{BASELINE_KEY}` وُجِدَ {len(lines)} مرّةً"
