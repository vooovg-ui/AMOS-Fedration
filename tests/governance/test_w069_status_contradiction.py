"""الهدف: حرسُ اتفاقِ الحالةِ المكتوبةِ مرّتَين — صفُّ § 2 وكتلةُ § 3 من سجلِّ العملِ.

الحدُّ المحروس: البندُ الواحدُ لا تكونُ له حالتانِ مكتوبتانِ. و§ 2 حكم 14 يقولُ إنَّ
ما كُتِبَ هو حالةُ المشروعِ — فمكتوبانِ متناقضانِ حالتانِ لا حالةٌ، وإحداهما كاذبةٌ
قطعًا. وكانَ الحرسُ يقرأُ الصفَّ وحدَه، فمرَّ إغلاقٌ (`W-067`) حُدِّثَ فيه أربعةَ عشرَ
صفًّا إلى `CLOSED` وبقيَت كتلُها تقولُ `VERIFIED`، والبوّابةُ خضراءُ — وذاك مقيسٌ في
`DISC-035`: أربعةَ عشرَ تناقضًا قِيسَت عندَ الرأسِ `899b422` قبلَ الإصلاحِ.

وهذا الحرسُ يُحاولُ **نقضَ** البوّابةِ الجديدةِ بطفرةٍ: يُزرَعُ التناقضُ في شجرةٍ
مؤقَّتةٍ فيلزمُ أن يُرصَد، ويُرفَعُ فيلزمُ أن تسكُتَ. وبوّابةٌ لا تُنقَضُ في محاولةٍ
جادّةٍ هي وحدَها بوّابةٌ.

حدُّ هذا الحرسِ — مُعلَنٌ لا مطويٌّ: يقيسُ اتفاقَ الحرفِ لا صدقَ الحالةِ نفسِها؛
فبندٌ حالتُه `CLOSED` في الموضعَينِ وهو غيرُ مُنجَزٍ لا يُرصَدُ هنا، وذاك عملُ
فحوصٍ أخرى (قيدُ السجلِّ · واجبُ ما بعدَ الدمجِ).

النطاق: حرسُ حوكمة
المالك: التنفيذ (بتفويضِ المالك)
تاريخ الإنشاء: 2026-08-30
تاريخ آخر تعديل: 2026-08-30
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "check_work_governance.py"
ACTIVE_PATH = REPO_ROOT / "docs" / "governance" / "work" / "ACTIVE_WORK.md"


def _load():
    spec = importlib.util.spec_from_file_location("check_work_governance_w069", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gate = _load()


def _items_and_blocks():
    text = ACTIVE_PATH.read_text(encoding="utf-8")
    items, _ = gate.parse_items(text)
    return items, gate.parse_detail_blocks(text)


# ── المستودعُ الحقيقيُّ: الاتفاقُ مقيسٌ لا مُدَّعًى ──────────────────────────


def test_لا_بندَ_في_السجلِّ_له_حالتانِ_مكتوبتان() -> None:
    items, blocks = _items_and_blocks()
    violations = gate.check_block_status_agrees(items, blocks)
    assert violations == [], violations


def test_لكلِّ_بندٍ_له_كتلةٌ_سطرُ_حالةٍ_يُقرَأ() -> None:
    """الاتفاقُ لا يُقاسُ إن لم يُكتَبْ أحدُ الطرفَينِ — فيُلزَمُ وجودُ السطرِ."""
    _, blocks = _items_and_blocks()
    assert blocks, "لا كتلةَ تفاصيلَ واحدةً — القياسُ بلا مادّة"
    for wid, block in blocks.items():
        assert gate.BLOCK_STATUS_RE.search(block), f"{wid}: كتلةٌ بلا سطرِ «الحالة:»"


# ── طفرةٌ: التناقضُ يُزرَعُ فيُرصَد ─────────────────────────────────────────


def _pair(status_row: str, status_block: str) -> tuple[list, dict]:
    items = [{
        "id": "WI-900", "status": status_row, "scope": "s", "track": "T0",
        "owner": "o", "reviewer": "r", "paths": ["p"], "start": "2026-01-01",
        "expires": "2026-12-31", "blocker": "—", "next": "n", "ledger": "—",
        "deferred_row": False,
    }]
    return items, {"WI-900": f"النطاق: s\nالحالة: {status_block}\n"}


@pytest.mark.parametrize(
    ("row", "block"),
    [
        ("CLOSED", "VERIFIED"),
        ("VERIFIED", "CLOSED"),
        ("IN_REVIEW", "VERIFIED"),
        ("VERIFIED", "IN_PROGRESS"),
    ],
)
def test_التناقضُ_المزروعُ_يُرصَد(row: str, block: str) -> None:
    violations = gate.check_block_status_agrees(*_pair(row, block))
    assert len(violations) == 1, f"تناقضٌ «{row}»/«{block}» لم يُرصَد — البوّابةُ دعوى"
    assert violations[0]["kind"] == "STATUS_CONTRADICTION"
    assert row in violations[0]["detail"] and block in violations[0]["detail"], (
        "الرصدُ بلا إعلانِ الحالتَينِ لا يُفيدُ قارئًا"
    )


@pytest.mark.parametrize("status", ["CLOSED", "VERIFIED", "IN_REVIEW", "IN_PROGRESS"])
def test_الاتفاقُ_يُسكِتُ_الحرس(status: str) -> None:
    assert gate.check_block_status_agrees(*_pair(status, status)) == []


def test_كتلةٌ_غائبةٌ_لا_تُرصَدُ_هنا() -> None:
    """حدُّ الفحصِ: غيابُ الكتلةِ يرصُدُه `MALFORMED_ITEM` لا هذا الفحصُ."""
    items, _ = _pair("CLOSED", "CLOSED")
    assert gate.check_block_status_agrees(items, {}) == []


def test_كتلةٌ_بلا_سطرِ_حالةٍ_لبندٍ_نشِطٍ_تُرصَد() -> None:
    items, _ = _pair("IN_REVIEW", "IN_REVIEW")
    violations = gate.check_block_status_agrees(items, {"WI-900": "النطاق: s\n"})
    assert len(violations) == 1
    assert violations[0]["kind"] == "MALFORMED_ITEM"


def test_الفحصُ_موصولٌ_بمَجرى_البوابةِ_لا_معزولًا() -> None:
    """فحصٌ لا يُنادى من `run` حرسٌ ميتٌ — فيُقاسُ وصلُه بالمصدرِ."""
    src = TOOL_PATH.read_text(encoding="utf-8")
    body = src[src.index("def run("):]
    assert re.search(r"violations \+= check_block_status_agrees\(", body), (
        "الفحصُ غيرُ موصولٍ بمَجرى البوّابةِ — حرسٌ لا يُنادى لا يحرُسُ"
    )
