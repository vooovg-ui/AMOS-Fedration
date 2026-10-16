# -*- coding: utf-8 -*-
"""الهدف: حارسُ قرارِ المالكِ `Q-H` — `VERIFIED` لبندٍ حسّاسٍ يشترطُ إعادةَ تشغيلٍ من المراجع.

النطاق: يقرأُ قائمةَ «الحسّاسِ» من `THE_ROADMAP.md § 16` (شرط 4 · كتلةُ
`Q-H-SENSITIVE-PATHS`) — مصدرٌ واحدٌ لا نسخةٌ هنا — ثمَّ صفوفَ وكتلَ
`ACTIVE_WORK.md`، ويُسقِطُ:

(أ) بندًا `VERIFIED` تمسُّ مساراتُه القائمةَ بلا سطرِ `Q-H-STATUS:` في كتلتِه ·
(ب) `Q-H-STATUS: MET <مسار>` بمسارِ تقريرٍ غيرِ موجودٍ في الشجرة ·
(ج) بندًا `CLOSED` حسّاسًا آخرُ سطرِ `Q-H-STATUS:` فيه `UNMET`.

ولا يُطبَّقُ بأثرٍ رجعيٍّ على `CLOSED` سابقٍ للقانونِ لا يحملُ السطرَ أصلًا (مُعلَنٌ
في نصِّ القانون). والحاكمُ **آخرُ** سطرٍ: التصحيحُ بالإضافةِ لا بالمحو.

المالك: WI-080 (قيدُ W-368 · قرارُ المالكِ Q-H · توجيهُ المستشارِ 8).
"""

from __future__ import annotations

import re
from pathlib import Path


def _discover_root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here, *here.parents):
        if (candidate / ".git").exists() or (candidate / "PROJECT_STATE.md").is_file():
            return candidate
    raise RuntimeError("لم يُعرَفْ جذرُ المستودعِ بعلامةٍ — والقياسُ يقِفُ ولا يُخمَّن.")


REPO_ROOT = _discover_root()
ROADMAP = REPO_ROOT / "docs" / "governance" / "work" / "THE_ROADMAP.md"
ACTIVE_WORK = REPO_ROOT / "docs" / "governance" / "work" / "ACTIVE_WORK.md"

LAW_TEXT = (
    "«VERIFIED لبند حساس (أمن/مال/سيادة/بيانات) يشترط أن يعيد المراجع تشغيل أوامر "
    "معاييره الأساسية بنفسه ويحفظ تقريره حرفيًّا؛ بنود التوثيق لا تشترط»"
)
CATEGORIES = ("أمن", "مال", "سيادة", "بيانات")
_ROW = re.compile(r"^\|\s*(WI-\d+)\s*\|")
_BLOCK = re.compile(r"^###\s+(WI-\d+)\b")
_STATUS_LINE = re.compile(r"^\s*Q-H-STATUS:\s*(MET|UNMET)\b\s*(.*)$")


def parse_sensitive(roadmap_text: str) -> dict[str, list[str]]:
    """كتلةُ `Q-H-SENSITIVE-PATHS` ⇒ {فئةٌ: [بادئات]} — بلا تخمين."""
    start = roadmap_text.find("Q-H-SENSITIVE-PATHS\n")
    end = roadmap_text.find("END-Q-H-SENSITIVE-PATHS", start)
    if start < 0 or end < 0:
        return {}
    out: dict[str, list[str]] = {}
    current = None
    for raw in roadmap_text[start:end].splitlines()[1:]:
        line = raw.strip()
        if not line:
            continue
        if line.endswith(":"):
            current = line[:-1]
            out[current] = []
        elif current is not None:
            out[current].append(line)
    return out


def _covers(prefix: str, path: str) -> bool:
    if prefix.endswith("/"):
        return path == prefix.rstrip("/") or path.startswith(prefix)
    return path == prefix


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line)]


def parse_items(active_text: str) -> dict[str, dict[str, object]]:
    lines = active_text.splitlines()
    items: dict[str, dict[str, object]] = {}
    for line in lines:
        if _ROW.match(line):
            cells = _cells(line)
            if len(cells) < 13:
                continue
            paths = [
                part.strip().strip("`").strip()
                for part in cells[7].split("·")
                if part.strip()
            ]
            items[cells[1]] = {"status": cells[6], "paths": paths, "qh": []}
    current = None
    for line in lines:
        block = _BLOCK.match(line)
        if block:
            current = block.group(1)
            continue
        if line.startswith("## "):
            current = None
            continue
        match = _STATUS_LINE.match(line)
        if match and current in items:
            items[current]["qh"].append((match.group(1), match.group(2).strip()))
    return items


def sensitive_hits(paths: list[str], sensitive: dict[str, list[str]]) -> list[str]:
    hits = []
    for category, prefixes in sensitive.items():
        for prefix in prefixes:
            if any(_covers(prefix, p) for p in paths):
                hits.append(f"{category}:{prefix}")
    return hits


def violations(active_text: str, roadmap_text: str, root: Path) -> list[str]:
    sensitive = parse_sensitive(roadmap_text)
    found: list[str] = []
    for wid, item in parse_items(active_text).items():
        hits = sensitive_hits(item["paths"], sensitive)  # type: ignore[arg-type]
        if not hits:
            continue
        qh = item["qh"]
        status = item["status"]
        last = qh[-1] if qh else None
        if status == "VERIFIED" and last is None:
            found.append(f"{wid}: VERIFIED حسّاسٌ ({hits[0]}) بلا سطرِ Q-H-STATUS — (أ)")
        if last and last[0] == "MET":
            report = last[1].split()[0].strip("`") if last[1] else ""
            if not report or not (root / report).exists():
                found.append(f"{wid}: Q-H-STATUS: MET بمسارِ تقريرٍ غائبٍ «{report}» — (ب)")
        if status == "CLOSED" and last and last[0] == "UNMET":
            found.append(f"{wid}: CLOSED حسّاسٌ وآخرُ سطرِه UNMET — (ج)")
    return found


def _texts() -> tuple[str, str]:
    return (
        ACTIVE_WORK.read_text(encoding="utf-8"),
        ROADMAP.read_text(encoding="utf-8"),
    )


def test_law_text_is_in_roadmap_verbatim() -> None:
    _, roadmap = _texts()
    assert LAW_TEXT in roadmap, "نصُّ قانونِ Q-H غائبٌ أو مُحرَّفٌ في THE_ROADMAP.md"


def test_sensitive_list_has_four_categories_and_live_prefixes() -> None:
    _, roadmap = _texts()
    sensitive = parse_sensitive(roadmap)
    assert tuple(sensitive) == CATEGORIES, sensitive.keys()
    for category, prefixes in sensitive.items():
        assert prefixes, f"فئةُ «{category}» فارغة"
        for prefix in prefixes:
            assert (REPO_ROOT / prefix.rstrip("/")).exists(), (
                f"بادئةٌ ميتةٌ في قائمةِ الحسّاس: {prefix} — تُطمئِنُ ولا تقيس"
            )


def test_live_tree_has_no_q_h_violation() -> None:
    active, roadmap = _texts()
    assert violations(active, roadmap, REPO_ROOT) == []


def test_wi076_is_sensitive_and_declared_unmet() -> None:
    active, roadmap = _texts()
    item = parse_items(active)["WI-076"]
    assert sensitive_hits(item["paths"], parse_sensitive(roadmap))  # type: ignore[arg-type]
    assert item["status"] == "VERIFIED", "حالةُ WI-076 لا تُغيَّرُ بيدِ المنفِّذ"
    assert item["qh"] and item["qh"][-1][0] == "UNMET"  # type: ignore[index]
    assert "لا يستوفي Q-H الجديد؛ لا CLOSED حتى مقعدين يعيدان التشغيل" in active


def test_negative_removing_wi076_marker_is_caught() -> None:
    active, roadmap = _texts()
    mutated = "\n".join(
        line for line in active.splitlines() if not _STATUS_LINE.match(line)
    )
    found = violations(mutated, roadmap, REPO_ROOT)
    assert any(v.startswith("WI-076:") and "(أ)" in v for v in found), found


def test_negative_closed_with_unmet_is_caught() -> None:
    active, roadmap = _texts()
    lines = active.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| WI-076 |"):
            cells = line.split("|")
            cells[6] = " CLOSED "
            lines[index] = "|".join(cells)
    found = violations("\n".join(lines), roadmap, REPO_ROOT)
    assert any(v.startswith("WI-076:") and "(ج)" in v for v in found), found


def test_negative_met_with_missing_report_is_caught() -> None:
    active, roadmap = _texts()
    mutated = active.replace(
        "Q-H-STATUS: UNMET",
        "Q-H-STATUS: MET docs/audit/evidence/__absent__/report.log",
        1,
    )
    found = violations(mutated, roadmap, REPO_ROOT)
    assert any("(ب)" in v for v in found), found


def test_documentation_item_is_not_sensitive() -> None:
    _, roadmap = _texts()
    sensitive = parse_sensitive(roadmap)
    assert sensitive_hits(["docs/audit/SOVEREIGN_DECISION_REGISTER.md"], sensitive) == []
    assert sensitive_hits(["tools/ops/pg_backup_restore.py"], sensitive)
