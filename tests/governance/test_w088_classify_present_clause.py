#!/usr/bin/env python3
"""مُصنِّفُ الحالةِ يقرأُ الحاضرَ لا سردَ الماضي (WI-088 · DISC-061 · قرارُ المالكِ Q-50).

الهدف:
    أن يصيرَ عطبُ `DISC-061` مقيسًا محروسًا: خليّةُ حالةٍ تقولُ «**مُغلَق** — … وكانَ:
    **مفتوح**» كانت تُقرأُ مفتوحةً لأنَّ `_classify_open` يفحصُ «مفتوح» في أيِّ موضعٍ
    من الخليّة. فصارَ الحاضرُ (ما قبلَ أوّلِ «وكان») يحسمُ أوّلًا، وإن خلا من العلامتَينِ
    قُرِئَت الخليّةُ كلُّها بالترتيبِ القديمِ (المفتوحُ يغلبُ).
النطاق:
    حالاتٌ مُصنَّعةٌ للقاعدةِ وحدودِها، وفحصٌ يقرأُ المستودعَ الحقيقيَّ فيُثبِتُ أنَّ
    القاعدةَ على صفوفِ DISCOVERIES وRISK_REGISTER تقلبُ DISC-081 وDISC-083 **لا غيرَهما**.
    لا شبكةَ ولا قاعدةَ ولا سرَّ، ولا كتابةَ في أيِّ سجلّ.
المالك: tests/governance — ديوانُ التدقيق
تاريخ الإنشاء: 2026-10-18
تاريخ آخر تعديل: 2026-10-18

الحدُّ المُعلَنُ — لا مطويٌّ:
    * فاتحةُ الماضي كلمةٌ واحدةٌ («وكان»). صفٌّ يسردُ ماضيَه بصيغةٍ أخرى («سابقًا: مفتوح»)
      يبقى يُقرأُ بالترتيبِ القديمِ — مفتوحًا — وذاك اتّجاهُ الأمانِ لا اتّجاهُ الخُضرة.
    * والقلبُ المحروسُ هنا مقيسٌ على حالةِ السجلّاتِ يومَ 2026-10-18؛ فإن أُضيفَ صفٌّ تقلبُه
      القاعدةُ سقطَ الفحصُ الأخيرُ ليُراجَعَ بعينٍ — لا ليُحدَّثَ رقمُه صامتًا.
"""

from __future__ import annotations

import importlib.util
import re
import sys

from tools.governance.repo_root import discover_repo_root

REPO_ROOT = discover_repo_root(__file__)
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "open_record_accountability.py"


def _load():
    spec = importlib.util.spec_from_file_location("ora_present_clause", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ORA = _load()


def _old_rule(cell: str) -> bool:
    """الترتيبُ السابقُ لـWI-088 حرفيًّا: «مفتوح» في أيِّ موضعٍ يغلب."""
    c = ORA._norm(cell)
    if ORA._has_marker(c, ORA.OPEN_MARKERS):
        return True
    if ORA._has_marker(c, ORA.CLOSED_MARKERS):
        return False
    return True


def test_مُغلَقٌ_حاضرًا_بماضٍ_مفتوحٍ_يُقرأُ_مُغلَقًا() -> None:
    is_open, basis = ORA._classify_open(
        "**مُغلَق** — بحكمِ الجولةِ التاسعة · **وكانَ:** **مفتوح** — قيدٌ سابق"
    )
    assert (is_open, basis) == (False, "STATUS_SAYS_CLOSED")


def test_مفتوحٌ_حاضرًا_بماضٍ_مُغلَقٍ_يبقى_مفتوحًا() -> None:
    """لا تخفيف: الحاضرُ المفتوحُ يغلبُ ولو تلاه ماضٍ مُغلَق."""
    is_open, _ = ORA._classify_open(
        "**مفتوح** — أُعيدَ فتحُه · وكانَ: **مُغلَق** في قيدٍ سابق"
    )
    assert is_open is True


def test_حاضرٌ_مختلطٌ_يبقى_مفتوحًا() -> None:
    """«مغلق وصفًا — ومفتوح حدًّا» (صيغةُ DISC-028) مفتوحٌ عمدًا ولا يُقلَب."""
    is_open, _ = ORA._classify_open(
        "**مغلق وصفا — ومفتوح حدا**: الواقعة مقيدة · وكان قبله شيء"
    )
    assert is_open is True


def test_بلا_فاتحةِ_ماضٍ_يبقى_الترتيبُ_القديم() -> None:
    cell = "معالج بالبند WI-007 — والشق الثاني مفتوح بحجز WI-006"
    assert ORA._classify_open(cell)[0] is _old_rule(cell) is True


def test_حاضرٌ_بلا_علامةٍ_يُقرأُ_بالخليّةِ_كلِّها() -> None:
    """حاضرٌ خالٍ من العلامتَينِ لا يُشترى به إغلاقٌ من الماضي."""
    is_open, _ = ORA._classify_open("قيدٌ في W-100 · وكانَ: **مُغلَق** ثمَّ **مفتوح**")
    assert is_open is True


def test_الفاتحةُ_في_أوّلِ_الخليّةِ_لا_تُفرِغُ_الحاضر() -> None:
    is_open, _ = ORA._classify_open("وكانَ مُغلَقًا ثمَّ صارَ **مفتوح**")
    assert is_open is True


def _real_rows():
    for rel in (
        "docs/governance/work/DISCOVERIES.md",
        "docs/governance/work/RISK_REGISTER.md",
    ):
        for line in (REPO_ROOT / rel).read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*((?:DISC|RK)-\d{3})\s*\|", line)
            if not m:
                continue
            cells = ORA._cells(line)
            if len(cells) < 8:
                continue
            yield m.group(1), cells[7]


def test_القاعدةُ_على_السجلّاتِ_الحقيقيّةِ_تقلبُ_صفَّينِ_لا_ثالثَ_لهما() -> None:
    rows = list(_real_rows())
    assert len(rows) >= 100, f"قُرِئَ {len(rows)} صفًّا فقط — القارئُ لم يقرأ السجلَّ"
    flipped = sorted(
        rid for rid, cell in rows if ORA._classify_open(cell)[0] is not _old_rule(cell)
    )
    assert flipped == ["DISC-081", "DISC-083"], (
        f"القاعدةُ تقلبُ {flipped} — المقيسُ يومَ 2026-10-18 صفّانِ (DISC-081 · DISC-083)؛ "
        "صفٌّ جديدٌ تقلبُه يُراجَعُ بعينٍ ولا يُحدَّثُ هذا الرقمُ صامتًا"
    )
    # والقلبُ في اتّجاهٍ واحدٍ: من مفتوحٍ إلى مُغلَقٍ بنصِّه الحاضرِ — لا العكس.
    for rid, cell in rows:
        if rid in flipped:
            assert _old_rule(cell) is True and ORA._classify_open(cell) == (
                False,
                "STATUS_SAYS_CLOSED",
            )
