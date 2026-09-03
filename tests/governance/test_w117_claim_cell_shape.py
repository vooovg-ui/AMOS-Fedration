#!/usr/bin/env python3
"""
حرسُ شكلِ خليّةِ المساراتِ — نثرٌ لا يُغطّي ملفًّا، ودعوى لا تتَّسِعُ بما لم تُكتَبْ

الهدف: منعُ عودةِ العَطبِ المُقيَّدِ في `DISC-042`: خليّةُ المساراتِ في § 1 من
       [`ACTIVE_WORK.md`] تُشطَرُ على «·» ويُعامَلُ كلُّ جزءٍ مسارًا، ثمَّ تُقاسُ
       التغطيةُ بالبادئةِ — فجزءٌ **نثريٌّ** يذكرُ مجلَّدًا كانَ **يُغطّيه كلَّه**،
       فتمرُّ ملفّاتٌ لم يُعلِنْها البندُ اسمًا ويضعُفُ `CLAIM_CONFLICT` (§ 6.1).
النطاق: شكلُ الجزءِ وحدَه — لا وجودُ الملفِّ ولا صدقُ الدعوى. وخليّةٌ تبدأُ
        بعلامةِ فراغٍ تُقرأُ «لا مسارَ يُحجَزُ» وما بعدَها تعليلٌ لا دعوى.
المالك: tests/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03
"""

from __future__ import annotations

from pathlib import Path

from tools.governance.check_work_governance import (
    ACTIVE_PATH,
    CLAIMING_STATUSES,
    REPO_ROOT,
    _covers,
    parse_claim_cell,
    parse_items,
)

# نصُّ الفخِّ: عينُ الشكلِ الذي قِيسَ في `W-106` — مسارٌ صريحٌ ثمَّ نثرٌ يذكرُ
# مجلَّدًا. الجزءُ النثريُّ هو المحكومُ عليه، لا المسارُ الصريحُ.
PROSE_CELL = (
    "tools/governance/check_work_governance.py · "
    "و34 ملفَّ فحصٍ تحتَ `tests/governance/` رُحِّلَت في هذا البندِ"
)
CLEAN_CELL = "tools/governance/check_work_governance.py · tests/governance"


def _claims(cell: str) -> tuple[list[str], list[dict[str, str]]]:
    return parse_claim_cell("WI-XXX", cell)


def test_النثرُ_في_خليّةِ_المساراتِ_يُرفَضُ_صراحةً_ولا_يُقرأُ_دعوى() -> None:
    """الفخُّ يُرى: الجزءُ النثريُّ مخالفةٌ مُسمّاةٌ ولا يدخُلُ المساراتِ."""
    paths, violations = _claims(PROSE_CELL)
    assert paths == ["tools/governance/check_work_governance.py"]
    assert [v["kind"] for v in violations] == ["NONPATH_CLAIM"]
    assert "DISC-042" in violations[0]["detail"]


def test_النثرُ_الذي_يذكرُ_مجلَّدًا_لا_يُغطّي_ملفًّا_تحتَه() -> None:
    """جوهرُ `DISC-042`: التغطيةُ تُقاسُ بعدَ الرفضِ فلا يمرُّ ملفٌّ لم يُعلَنْ."""
    victim = "tests/governance/test_work_governance_gate.py"
    paths, _ = _claims(PROSE_CELL)
    assert not any(_covers(claim, victim) for claim in paths)


def test_المسارُ_المكتوبُ_اسمًا_يبقى_يُغطّي_ما_تحتَه() -> None:
    """العكسُ يُثبَتُ: التشديدُ لم يُلغِ دعوى المجلَّدِ المكتوبةِ مسارًا."""
    victim = "tests/governance/test_work_governance_gate.py"
    paths, violations = _claims(CLEAN_CELL)
    assert violations == []
    assert any(_covers(claim, victim) for claim in paths)


def test_خليّةٌ_تبدأُ_بعلامةِ_الفراغِ_لا_تُدَّعي_ولا_تُخالِفُ() -> None:
    """صفٌّ صادقٌ يشرحُ لِمَ لا يُحجَزُ شيءٌ لا يُكسَرُ بالتشديدِ."""
    cell = "— (لا مسارَ يُحجَزُ: كلُّ ما يُمَسُّ مُعفًى من الحجزِ بنصِّ § 6)"
    paths, violations = _claims(cell)
    assert paths == []
    assert violations == []


def test_علامةُ_الفراغِ_لا_تُغطّي_شيئًا_فلا_تصيرُ_بابًا_خلفيًّا() -> None:
    """الإعفاءُ إعلانُ فراغٍ لا دعوى واسعةٌ: لا ملفَّ يُغطّيه."""
    paths, _ = _claims("— (سُلِّمَ المسارُ · § 6.4)")
    assert all(
        not any(_covers(claim, candidate) for claim in paths)
        for candidate in ("tools/governance/check_work_governance.py", "README.md")
    )


def test_المسارُ_بين_علامتَي_اقتباسٍ_مائلٍ_يُقرأُ_مسارًا_لا_نثرًا() -> None:
    """الكتابةُ بـ`backticks` عادةٌ في السجلِّ، فلا تُقلَبُ مخالفةً."""
    paths, violations = _claims("`tools/governance/repo_root.py`")
    assert paths == ["tools/governance/repo_root.py"]
    assert violations == []


def test_الشكلُ_يُقاسُ_لا_الوجودُ_فبندٌ_يُعلِنُ_ملفًّا_سيُنشِئُه_يمرُّ() -> None:
    """حدٌّ مُعلَنٌ: ملفٌّ لم يوجدْ بعدُ دعوى مشروعةٌ."""
    unborn = "tools/governance/not_yet_written_guard.py"
    assert not (REPO_ROOT / unborn).exists()
    paths, violations = _claims(unborn)
    assert paths == [unborn] and violations == []


def test_الشجرةُ_الحيّةُ_خاليةٌ_من_الأجزاءِ_غيرِ_المساريّةِ() -> None:
    """القياسُ على الشجرةِ الحاضرةِ لا على نصٍّ مصنوعٍ وحدَه."""
    text = (REPO_ROOT / ACTIVE_PATH).read_text(encoding="utf-8")
    _, violations = parse_items(text)
    assert [v for v in violations if v["kind"] == "NONPATH_CLAIM"] == []


def test_كلُّ_مسارٍ_مُعلَنٍ_في_بندٍ_حاجزٍ_شكلُه_مسارٌ() -> None:
    """لا دعوى قائمةً تحمِلُ نثرًا بعدَ النقلِ إلى كتلِ التفاصيلِ."""
    text = (REPO_ROOT / ACTIVE_PATH).read_text(encoding="utf-8")
    items, _ = parse_items(text)
    claiming = [it for it in items if str(it["status"]) in CLAIMING_STATUSES]
    assert claiming, "جدولُ § 1 لا يخلو من بندٍ حاجزٍ"
    for item in claiming:
        for claim in item["paths"]:  # type: ignore[union-attr]
            assert " " not in str(claim), f"{item['id']}: «{claim}»"


def test_النصُّ_المنقولُ_لم_يُحذَفْ_بل_سكنَ_كتلةَ_تفاصيلِه() -> None:
    """نقلٌ لا إخفاءٌ: تعليلُ السجلّاتِ المُعفاةِ ما زالَ مكتوبًا."""
    text = (REPO_ROOT / ACTIVE_PATH).read_text(encoding="utf-8")
    assert text.count("تُمَسُّ ولا تُدَّعى مِلكًا") >= 2


def test_محلُّ_القياسِ_مُمرَّرٌ_لا_مُستنتَجٌ_بعُمقٍ_مكتوبٍ() -> None:
    """`DISC-041`: جذرُ القياسِ يُعرَفُ بعلامةٍ لا بعددِ آباءٍ."""
    assert (Path(REPO_ROOT) / ACTIVE_PATH).is_file()
