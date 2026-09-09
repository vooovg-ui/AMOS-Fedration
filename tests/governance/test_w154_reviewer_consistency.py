# -*- coding: utf-8 -*-
"""الهدف: حارسٌ مقيسٌ — مراجعُ الصفِّ في § 1 من `ACTIVE_WORK.md` هو نفسُه مراجعُ كتلةِ البندِ.

سببُ وجودِه (‏`W-154`): طُبِّقَ قرارُ المالكِ `Q-43` (‏تعيينُ مجلسِ المراجعةِ) على
الصفوفِ والكتلِ في `W-152`، فبقيَ بندٌ واحدٌ (`WI-033`) صفُّه يقولُ «مجلسُ المراجعةِ»
وكتلتُه تقولُ «— (‏النطاقُ بلا مراجعٍ مُسجَّلٍ)». كشفَه المراجعُ المستقلُّ أ في الجولةِ
الثالثةِ عيبًا `P1` (‏«الإجراءُ غيرُ ذَرِّيٍّ»)، فصارَ الحدُّ مقيسًا بحارسٍ لا مطويًّا
في وعدٍ: أيُّ انحرافٍ بينَ الصفِّ والكتلةِ في حقلِ المراجعِ يُسقِطُ هذا الاختبارَ.

ولا يفحصُ هذا الحارسُ **مَن** المراجعُ (‏ذاكَ قرارُ مالكٍ في `OWNERSHIP.md`)، بل
**تطابُقَ الإعلانَينِ** فقط — فالتناقضُ نفسُه هو العيبُ.
"""

from __future__ import annotations

import re
from pathlib import Path

def _discover_root() -> Path:
    """جذرُ المستودعِ **بعلامةٍ لا بعُمقٍ مكتوبٍ** (‏`W-102` · حرسُ نسَبِ محلِّ القياسِ).

    `parents[2]` يصدُقُ ما دامَ الملفُّ في `tests/governance/` ويكذِبُ صامتًا أوّلَ
    ما يُنقَلُ — فيُقاسُ مستودعٌ آخرُ ويُقرأُ الحكمُ صحيحًا. فالصعودُ حتى علامةٍ دالّةٍ.
    """
    here = Path(__file__).resolve()
    for candidate in (here, *here.parents):
        if (candidate / ".git").exists() or (candidate / "PROJECT_STATE.md").is_file():
            return candidate
    raise RuntimeError(  # pragma: no cover - يمنعُ القياسَ ولا يُخمَّنُ عندَه
        "لم يُعرَفْ جذرُ المستودعِ بعلامةٍ (`.git` أو `PROJECT_STATE.md`) — "
        "والقياسُ يقِفُ ولا يُستأنَفُ بعُمقٍ مظنونٍ."
    )


REPO_ROOT = _discover_root()
ACTIVE_WORK = REPO_ROOT / "docs" / "governance" / "work" / "ACTIVE_WORK.md"

_ROW = re.compile(r"^\|\s*(WI-\d+)\s*\|")
_BLOCK_HEADER = re.compile(r"^###\s+(WI-\d+)\b")


def _normalise(value: str) -> str:
    """يُسقِطُ التشكيلَ والعلاماتَ الزخرفيّةَ لتُقارَنَ الأسماءُ على معناها."""
    value = value.replace("`", "").replace("*", "")
    value = re.sub(r"[\u064B-\u0652\u0670\u200f\u200e\u0640]", "", value)
    value = value.replace("ـ", "")
    return re.sub(r"\s+", " ", value).strip(" .·—-")


def _read_rows(lines: list[str]) -> dict[str, tuple[int, str, str]]:
    """يقرأُ صفوفَ § 1: المعرّفُ ⇒ (‏رقمُ السطرِ · الحالةُ · المراجعُ)."""
    rows: dict[str, tuple[int, str, str]] = {}
    for index, line in enumerate(lines, start=1):
        match = _ROW.match(line)
        if not match:
            continue
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) < 13:
            continue
        rows[match.group(1)] = (index, cells[6], cells[5])
    return rows


def _read_blocks(lines: list[str]) -> dict[str, tuple[int, str, str]]:
    """يقرأُ كتلَ § 2: المعرّفُ ⇒ (‏رقمُ سطرِ حقلِ المراجعِ · الحالةُ · المراجعُ)."""
    blocks: dict[str, tuple[int, str, str]] = {}
    current: str | None = None
    inside = False
    reviewer = ""
    reviewer_line = 0
    status = ""
    for index, line in enumerate(lines, start=1):
        header = _BLOCK_HEADER.match(line)
        if header:
            current = header.group(1)
            reviewer, reviewer_line, status, inside = "", 0, "", False
            continue
        if current is None:
            continue
        if line.strip() == "```text":
            inside = True
            continue
        if inside and line.strip() == "```":
            inside = False
            if reviewer and current not in blocks:
                blocks[current] = (reviewer_line, status, reviewer)
            continue
        if not inside:
            continue
        if line.startswith("الحالة:") and not status:
            status = line.split(":", 1)[1].strip()
        if "المراجع:" in line and not reviewer:
            reviewer = line.split("المراجع:", 1)[1].strip()
            reviewer_line = index
    return blocks


def test_row_reviewer_matches_block_reviewer_for_active_items() -> None:
    lines = ACTIVE_WORK.read_text(encoding="utf-8").split("\n")
    rows = _read_rows(lines)
    blocks = _read_blocks(lines)
    assert rows, "لم يُقرأْ أيُّ صفٍّ من § 1 — الحارسُ نفسُه معطوبٌ لا الوثيقةُ"

    mismatches: list[str] = []
    for item, (row_line, row_status, row_reviewer) in sorted(rows.items()):
        if row_status.startswith("CLOSED"):
            continue
        block = blocks.get(item)
        if block is None:
            continue
        block_line, _block_status, block_reviewer = block
        if _normalise(row_reviewer) != _normalise(block_reviewer):
            mismatches.append(
                f"{item}: الصفُّ (‏سطر {row_line}) «{_normalise(row_reviewer)}» "
                f"≠ الكتلةُ (‏سطر {block_line}) «{_normalise(block_reviewer)}»"
            )

    assert not mismatches, (
        "REVIEWER_ROW_BLOCK_MISMATCH — حقلُ المراجعِ مُعلَنٌ مرَّتَينِ بقيمتَينِ "
        "مختلفتَينِ لبندٍ غيرِ مُغلَقٍ:\n  " + "\n  ".join(mismatches)
    )
