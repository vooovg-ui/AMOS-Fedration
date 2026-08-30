#!/usr/bin/env python3
"""
بوابة حوكمة العمل — Work Governance Gate

الهدف: أن تكون «الخارطةُ الحاكمة» طريقًا **مُنفَذًا** لا وصيّةً مكتوبة. تفشل هذه
       البوابةُ إذا بدأ عملٌ بلا قيدٍ في `ACTIVE_WORK.md`، أو تقاطعَ بندانِ في
       مسارٍ واحدٍ، أو تغيَّرَ مسارٌ لا يملكُه بندٌ نشِط، أو انتهى حجزٌ فبقيَ
       معلَّقًا، أو أُغلِقَ بندٌ بلا قيدٍ في سجلِّ الإكمال.
النطاق: سجلّاتُ `docs/governance/work/` ومجموعةُ التغييرِ (المُدرَجُ للالتزام، أو
        مدى التزاماتٍ، أو التزامٌ واحد). لا تحكم هذه الأداةُ على **صدقِ** مضمونِ
        البند — تحكم على وجودِه وشكلِه وتقاطعِه. الحكمُ على المضمون للمراجعِ
        المستقلِّ وديوانِ التدقيق، كما في `THE_ROADMAP.md § 13`.
المالك: tools/governance — ديوان التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-25
تاريخ آخر تعديل: 2026-08-27

لماذا أداةٌ لا فقرةٌ في وثيقة
-----------------------------
العطبُ الذي تُعالجُه هذه الطبقةُ مقيسٌ لا متخيَّل: القيدُ `W-024` في سجلِّ الإكمال
سجَّلَ أنَّ الخارطةَ أرسلَت عاملًا إلى عملٍ كان مُنجَزًا قبلَ اليوم. وقاعدةٌ تقول
«سجِّلْ بندَك قبلَ أن تبدأ» ولا يحرسُها إلّا نصٌّ هي قاعدةٌ تُنسى في أوّلِ التزامٍ
عاجل. فتُنفَّذ هنا بوّابةً لها رمزُ خروج.

المخالفات
---------
  REGISTER_MISSING          سجلٌّ من سجلّات الطبقة غير موجود
  REGISTER_SECTION_MISSING  سجلٌّ فقدَ قسمًا إلزاميًّا
  DUPLICATE_ITEM_ID         مُعرِّفٌ (WI/RK/DISC) مُكرَّر
  MALFORMED_ITEM            حقلٌ إلزاميٌّ ناقصٌ أو تاريخٌ بغيرِ YYYY-MM-DD
  ILLEGAL_STATUS            حالةٌ خارجَ آلةِ الحالات (THE_ROADMAP § 4.3)
  ILLEGAL_TRANSITION        انتقالُ حالةٍ خارجَ الرسمِ المسموح
  OWNERLESS_ITEM            بندٌ نشِطٌ بلا مالك
  SCOPE_UNOWNED             نطاقُ بندٍ غيرُ مُسجَّلٍ في OWNERSHIP.md
  CLAIM_CONFLICT            بندانِ نشِطانِ يتقاطعانِ في مسار
  PATH_UNCLAIMED            تغيَّرَ مسارٌ لا يملكُه بندٌ نشِط
  RESERVATION_EXPIRED       مرَّ تاريخُ الحجزِ والبندُ ما زال نشِطًا
  POST_MERGE_NOT_CLOSED     قُيِّدَ عملُ بندٍ في سجلِّ الإكمالِ وبقيَ بندُه غيرَ CLOSED
                            يُقاسُ باتِّجاهَينِ: من البندِ إلى قيدِه في مجموعةِ التغيير،
                            ومن القيدِ المدموجِ في `main` إلى بندِه (‏§ 13.3)
  MISSING_LEDGER_LINK       بندٌ CLOSED بلا قيدِ W-###
  UNROUTED_DISCOVERY        اكتشافٌ بلا وجهةٍ مُعلَنة

الاستخدام
---------
    python tools/governance/check_work_governance.py --self-check
    python tools/governance/check_work_governance.py --staged
    python tools/governance/check_work_governance.py --commit HEAD
    python tools/governance/check_work_governance.py --range origin/main..HEAD
    python tools/governance/check_work_governance.py --staged --advisory
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

WORK_DIR = "docs/governance/work"
ROADMAP_PATH = f"{WORK_DIR}/THE_ROADMAP.md"
ACTIVE_PATH = f"{WORK_DIR}/ACTIVE_WORK.md"
OWNERSHIP_PATH = f"{WORK_DIR}/OWNERSHIP.md"
RISK_PATH = f"{WORK_DIR}/RISK_REGISTER.md"
DISCOVERIES_PATH = f"{WORK_DIR}/DISCOVERIES.md"
HANDOFF_TEMPLATE_PATH = f"{WORK_DIR}/HANDOFFS/TEMPLATE.md"
LEDGER_PATH = "docs/audit/COMPLETION_LEDGER.md"

REQUIRED_REGISTERS = (
    ROADMAP_PATH,
    ACTIVE_PATH,
    OWNERSHIP_PATH,
    RISK_PATH,
    DISCOVERIES_PATH,
    HANDOFF_TEMPLATE_PATH,
)

# الأقسامُ الإلزاميّةُ مكتوبةٌ **منزوعةَ التشكيل**: الوثائقُ مُشكَّلةٌ عن قصدٍ،
# ومطابقةُ نصٍّ مُشكَّلٍ حرفًا بحرفٍ تكسِرُ البوّابةَ عند أوّلِ فتحةٍ تُضاف.
REQUIRED_SECTIONS: dict[str, tuple[str, ...]] = {
    ROADMAP_PATH: (
        "## 2 · القانون الأعلى للعمل",
        "## 4 · بند العمل",
        "## 6 · منع تكرار العمل",
        "## 7 · الواجب بعد كل دمج",
        "## 13 · الإنفاذ الآلي",
    ),
    ACTIVE_PATH: (
        "## 1 · البنود النشطة",
        "## 3 · تفاصيل البنود النشطة",
    ),
    OWNERSHIP_PATH: ("## 1 · النطاقات المسجلة",),
    RISK_PATH: ("## 1 · المخاطر المفتوحة",),
    DISCOVERIES_PATH: ("## 1 · الاكتشافات المقيدة",),
}

ACTIVE_STATUSES = frozenset({
    "PROPOSED", "READY", "RESERVED", "IN_PROGRESS", "BLOCKED", "IN_REVIEW", "VERIFIED",
})
TERMINAL_STATUSES = frozenset({"CLOSED", "DEFERRED", "CANCELLED"})
ALL_STATUSES = ACTIVE_STATUSES | TERMINAL_STATUSES

# الحالاتُ التي تقفلُ مساراتِها فعلًا (THE_ROADMAP § 6.1)، ويجوزُ للتغييرِ أن
# يستندَ إليها. تُضافُ `CLOSED` لأنَّ الإغلاقَ يقعُ في التزامِ التسجيلِ نفسِه.
CLAIMING_STATUSES = frozenset({"RESERVED", "IN_PROGRESS", "BLOCKED", "IN_REVIEW", "VERIFIED", "CLOSED"})
# الحالاتُ التي يجبُ فيها مالكٌ مُسمًّى
OWNER_REQUIRED_STATUSES = frozenset({"RESERVED", "IN_PROGRESS", "BLOCKED", "IN_REVIEW", "VERIFIED", "CLOSED"})

LEGAL_TRANSITIONS: dict[str, frozenset[str]] = {
    "PROPOSED": frozenset({"READY", "DEFERRED", "CANCELLED"}),
    "READY": frozenset({"RESERVED", "DEFERRED", "CANCELLED"}),
    "RESERVED": frozenset({"IN_PROGRESS", "READY", "BLOCKED", "CANCELLED"}),
    "IN_PROGRESS": frozenset({"IN_REVIEW", "BLOCKED", "CANCELLED"}),
    "BLOCKED": frozenset({"IN_PROGRESS", "RESERVED", "DEFERRED", "CANCELLED"}),
    "IN_REVIEW": frozenset({"VERIFIED", "IN_PROGRESS"}),
    "VERIFIED": frozenset({"CLOSED", "IN_PROGRESS"}),
    "DEFERRED": frozenset({"READY", "CANCELLED"}),
    "CLOSED": frozenset(),
    "CANCELLED": frozenset(),
}

WI_RE = re.compile(r"^\|\s*(WI-[A-Z]?\d{2,3})\s*\|")
RK_RE = re.compile(r"^\|\s*(RK-\d{3})\s*\|")
DISC_RE = re.compile(r"^\|\s*(DISC-\d{3})\s*\|")
SCOPE_RE = re.compile(r"^\|\s*([a-z][a-z0-9-]{2,})\s*\|")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ADDED_WORK_ID_RE = re.compile(r"^\+\|\s*(W-\d{3})\s*\|", re.MULTILINE)
WORK_ID_IN_TEXT_RE = re.compile(r"W-\d{3}")

# صفُّ قيدٍ في سجلِّ الإكمالِ: معرِّفُه ثمَّ بقيّةُ الصفِّ نصًّا (الصفُّ سطرٌ واحد).
LEDGER_ROW_RE = re.compile(r"^\|\s*(W-\d{3})\s*\|(.*)$", re.MULTILINE)
# **الإعلانُ الصريحُ** لبندِ القيد: `WI-###` مكتوبًا رابطًا إلى `ACTIVE_WORK.md`.
# ولا يُقاسُ الذكرُ العارضُ (‏قيدٌ يذكرُ بندَ غيرِه ليقولَ «لم أمسَّ محجوزَه»)،
# لأنَّ حرسًا يُحمِّرُ على ذكرٍ عارضٍ يُعلِّمُ الناسَ ألّا يذكروا — وذاك خسرانُ صدقٍ
# أكبرُ من الخرقِ الذي يمنعُه. والحدُّ مُعلَنٌ في THE_ROADMAP § 13.3.
LEDGER_ITEM_LINK_RE = re.compile(r"\[`?(WI-[A-Z]?\d{2,3})`?\]\([^)]*ACTIVE_WORK\.md[^)]*\)")

# أساسُ قياسِ ما بعدَ الدمج: الفرعُ الذي يصيرُ العملُ فيه حالةَ الدولة.
MERGE_BASE_ENV = "AMOS_WORK_GATE_MERGE_BASE"
MERGE_BASE_CANDIDATES = ("origin/main", "main")

EMPTY_MARKS = frozenset({"", "—", "-", "–", "لا شيء", "غير معين", "(غير معين)"})

# ما لا يُلزِمُ حجزًا: سجلّاتُ الطبقةِ نفسُها (وإلّا لزمَ حجزُ حجزٍ)، والمخرجاتُ
# المولَّدةُ آليًّا، وقياساتُ التدقيق.
EXEMPT_EXACT = frozenset({
    ROADMAP_PATH, ACTIVE_PATH, OWNERSHIP_PATH, RISK_PATH, DISCOVERIES_PATH,
    LEDGER_PATH,
    "docs/audit/TRUTH_MATRIX.md",
    "docs/audit/truth_matrix.json",
    "docs/audit/truth_baseline.json",
    "docs/audit/CROWN_TRUTH_MATRIX.md",
    "docs/audit/CROSS_SYSTEM_SUITE_MATRIX.md",
    "docs/audit/constitution_history_digests.json",
})
EXEMPT_PREFIXES = (
    f"{WORK_DIR}/HANDOFFS/",
    "docs/audit/measurements/",
    "docs/audit/backups/",
)
EXEMPT_SUFFIXES = (".lock", ".egg-info", ".pyc")

DETAIL_KEYS = ("خارج النطاق", "معيار القبول", "الدليل المطلوب")

_DIACRITICS = dict.fromkeys(
    [*range(0x064B, 0x0653), 0x0640, 0x0670, 0x06D6, 0x0653, 0x0654, 0x0655]
)


def _norm(text: str) -> str:
    """نصٌّ منزوعُ التشكيلِ موحَّدُ المسافات — لمطابقةِ العناوينِ لا لعرضِها."""
    stripped = unicodedata.normalize("NFC", text).translate(_DIACRITICS)
    return re.sub(r"\s+", " ", stripped).strip()


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _is_empty(cell: str) -> bool:
    return _norm(cell).strip("() ") in {_norm(m).strip("() ") for m in EMPTY_MARKS}


def _v(kind: str, detail: str) -> dict[str, str]:
    return {"kind": kind, "detail": detail}


# ── قراءةُ السجلّات ──────────────────────────────────────────────────────────


def _git(*args: str) -> str:
    out = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=False
    )
    if out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} → {out.returncode}: {out.stderr.strip()}")
    return out.stdout


def parse_scopes(text: str) -> set[str]:
    """أسماءُ النطاقاتِ المُسجَّلة. الصفُّ نطاقٌ إن كان أوّلُ خليّةٍ اسمًا لاتينيًّا."""
    scopes: set[str] = set()
    for line in text.splitlines():
        m = SCOPE_RE.match(line)
        if m and len(_cells(line)) >= 5:
            scopes.add(m.group(1))
    return scopes


def parse_items(text: str) -> tuple[list[dict[str, object]], list[dict[str, str]]]:
    """بنودُ العملِ من جدولِ § 1 (اثنَتا عشرةَ خليّة) و§ 2 (ستُّ خلايا للمؤجَّل)."""
    items: list[dict[str, object]] = []
    violations: list[dict[str, str]] = []
    for line in text.splitlines():
        m = WI_RE.match(line)
        if not m:
            continue
        cells = _cells(line)
        wid = m.group(1)
        if len(cells) == 12:
            items.append({
                "id": wid, "scope": cells[1], "track": cells[2], "owner": cells[3],
                "reviewer": cells[4], "status": cells[5],
                "paths": [p.strip() for p in cells[6].split("·") if p.strip()],
                "start": cells[7], "expires": cells[8], "blocker": cells[9],
                "next": cells[10], "ledger": cells[11], "deferred_row": False,
            })
        elif len(cells) == 6:
            items.append({
                "id": wid, "scope": cells[1], "track": "", "owner": cells[2],
                "reviewer": "", "status": cells[3], "paths": [], "start": "",
                "expires": "", "blocker": "", "next": cells[4], "ledger": "",
                "deferred_row": True,
            })
        else:
            violations.append(_v(
                "MALFORMED_ITEM",
                f"{wid}: صفٌّ بـ{len(cells)} خليّةً — جدولُ البنودِ النشِطةِ اثنَتا عشرةَ خليّةً "
                "وجدولُ المؤجَّلِ ستٌّ",
            ))
    return items, violations


def parse_detail_blocks(text: str) -> dict[str, str]:
    """كتلةُ تفاصيلِ كلِّ بندٍ نشِطٍ في § 3، مفتاحُها معرِّفُ البند."""
    blocks: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []
    in_fence = False
    for line in text.splitlines():
        heading = re.match(r"^###\s+(WI-[A-Z]?\d{2,3})", line.strip())
        if heading:
            if current:
                blocks[current] = "\n".join(buffer)
            current, buffer, in_fence = heading.group(1), [], False
            continue
        if current is None:
            continue
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            buffer.append(line)
    if current:
        blocks[current] = "\n".join(buffer)
    return blocks


def parse_ids(text: str, pattern: re.Pattern[str]) -> list[str]:
    return [m.group(1) for line in text.splitlines() if (m := pattern.match(line))]


# ── فحوصُ الشكلِ والاتّساق ───────────────────────────────────────────────────


def check_registers_exist() -> list[dict[str, str]]:
    return [
        _v("REGISTER_MISSING", f"{p} غير موجود — طبقةُ الحوكمةِ ناقصة")
        for p in REQUIRED_REGISTERS
        if not (REPO_ROOT / p).exists()
    ]


def check_sections(texts: dict[str, str]) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for path, sections in REQUIRED_SECTIONS.items():
        body = _norm(texts.get(path, ""))
        for section in sections:
            if _norm(section) not in body:
                violations.append(_v(
                    "REGISTER_SECTION_MISSING",
                    f"{path}: القسمُ «{section}» غير موجود",
                ))
    return violations


def check_duplicate_ids(texts: dict[str, str]) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for path, pattern, label in (
        (ACTIVE_PATH, WI_RE, "بندِ عمل"),
        (RISK_PATH, RK_RE, "خطر"),
        (DISCOVERIES_PATH, DISC_RE, "اكتشاف"),
    ):
        seen: set[str] = set()
        for item_id in parse_ids(texts.get(path, ""), pattern):
            if item_id in seen:
                violations.append(_v(
                    "DUPLICATE_ITEM_ID",
                    f"{path}: مُعرِّفُ {label} {item_id} مُكرَّرٌ — لا يُعادُ استخدامُ معرِّف",
                ))
            seen.add(item_id)
    return violations


def check_items(
    items: list[dict[str, object]],
    blocks: dict[str, str],
    scopes: set[str],
    today: date,
) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for it in items:
        wid = str(it["id"])
        status = str(it["status"])

        if status not in ALL_STATUSES:
            violations.append(_v(
                "ILLEGAL_STATUS",
                f"{wid}: الحالةُ «{status}» خارجَ آلةِ الحالات — THE_ROADMAP § 4.3",
            ))
            continue

        if _is_empty(str(it["scope"])):
            violations.append(_v("MALFORMED_ITEM", f"{wid}: النطاقُ فارغ"))
        elif str(it["scope"]) not in scopes:
            violations.append(_v(
                "SCOPE_UNOWNED",
                f"{wid}: النطاقُ «{it['scope']}» غيرُ مُسجَّلٍ في {OWNERSHIP_PATH}",
            ))

        if status in OWNER_REQUIRED_STATUSES and _is_empty(str(it["owner"])):
            violations.append(_v(
                "OWNERLESS_ITEM",
                f"{wid}: حالتُه {status} بلا مالكٍ مُسمًّى — لا نطاقَ بلا مالكٍ واحد",
            ))

        if status == "CLOSED" and not WORK_ID_IN_TEXT_RE.search(str(it["ledger"])):
            violations.append(_v(
                "MISSING_LEDGER_LINK",
                f"{wid}: أُغلِقَ بلا قيدِ W-### في سجلِّ الإكمال — THE_ROADMAP § 7",
            ))

        if it["deferred_row"]:
            if status != "DEFERRED":
                violations.append(_v(
                    "MALFORMED_ITEM",
                    f"{wid}: مُدرَجٌ في جدولِ المؤجَّلِ وحالتُه {status}",
                ))
            if _is_empty(str(it["next"])):
                violations.append(_v(
                    "MALFORMED_ITEM",
                    f"{wid}: مؤجَّلٌ بلا trigger يُعيدُه — التأجيلُ بلا شرطٍ إلغاءٌ مُقنَّع",
                ))
            continue

        if status in ACTIVE_STATUSES:
            if not it["paths"]:
                violations.append(_v(
                    "MALFORMED_ITEM",
                    f"{wid}: بندٌ نشِطٌ بلا مساراتٍ مُعلَنةٍ — لا حجزَ بلا نطاقٍ محدَّد",
                ))
            if _is_empty(str(it["track"])):
                violations.append(_v(
                    "MALFORMED_ITEM",
                    f"{wid}: لا ينتسبُ إلى مسارٍ T# ولا مرحلةٍ E## — THE_ROADMAP § 9",
                ))
            if _is_empty(str(it["next"])):
                violations.append(_v(
                    "MALFORMED_ITEM", f"{wid}: بلا خطوةٍ تاليةٍ بفعلٍ واحد"
                ))
            for field, label in (("start", "بدأ"), ("expires", "ينتهي الحجز")):
                value = str(it[field])
                if not DATE_RE.match(value):
                    violations.append(_v(
                        "MALFORMED_ITEM",
                        f"{wid}: «{label}» = «{value}» — الصيغةُ الملزمةُ YYYY-MM-DD",
                    ))
            block = _norm(blocks.get(wid, ""))
            if not block:
                violations.append(_v(
                    "MALFORMED_ITEM",
                    f"{wid}: بندٌ نشِطٌ بلا كتلةِ تفاصيلَ في § 3 من {ACTIVE_PATH}",
                ))
            else:
                for key in DETAIL_KEYS:
                    if _norm(key) not in block:
                        violations.append(_v(
                            "MALFORMED_ITEM",
                            f"{wid}: كتلةُ التفاصيلِ بلا حقلِ «{key}»",
                        ))

        if status in {"RESERVED", "IN_PROGRESS", "IN_REVIEW"}:
            expires = str(it["expires"])
            if DATE_RE.match(expires) and date.fromisoformat(expires) < today:
                violations.append(_v(
                    "RESERVATION_EXPIRED",
                    f"{wid}: انتهى الحجزُ في {expires} والحالةُ ما زالت {status} — "
                    "يُحدَّثُ الحجزُ أو يُسلَّمُ البندُ (THE_ROADMAP § 6.3)",
                ))
    return violations


def check_claim_conflicts(items: list[dict[str, object]]) -> list[dict[str, str]]:
    """تقاطعُ مسارٍ بينَ بندَينِ نشِطَينِ — البابُ الأوّلُ لتكرارِ العمل."""
    violations: list[dict[str, str]] = []
    claiming = [
        it for it in items
        if str(it["status"]) in CLAIMING_STATUSES and str(it["status"]) != "CLOSED"
    ]
    for i, first in enumerate(claiming):
        for second in claiming[i + 1:]:
            for pa in first["paths"]:  # type: ignore[union-attr]
                for pb in second["paths"]:  # type: ignore[union-attr]
                    if _paths_overlap(str(pa), str(pb)):
                        violations.append(_v(
                            "CLAIM_CONFLICT",
                            f"{first['id']} و{second['id']} يتقاطعانِ في «{pa}» ↔ «{pb}» — "
                            "يُقسَمُ البندُ أو يُستلَم (THE_ROADMAP § 6.1)",
                        ))
    return violations


def _paths_overlap(a: str, b: str) -> bool:
    a, b = a.rstrip("/"), b.rstrip("/")
    return a == b or a.startswith(f"{b}/") or b.startswith(f"{a}/")


def check_discoveries(text: str) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for line in text.splitlines():
        m = DISC_RE.match(line)
        if not m:
            continue
        cells = _cells(line)
        if len(cells) < 8:
            violations.append(_v(
                "MALFORMED_ITEM",
                f"{m.group(1)}: صفُّ اكتشافٍ بـ{len(cells)} خليّةً — الإلزاميُّ ثمانٍ",
            ))
            continue
        if _is_empty(cells[6]):
            violations.append(_v(
                "UNROUTED_DISCOVERY",
                f"{m.group(1)}: بلا وجهةٍ مُعلَنة — THE_ROADMAP § 11",
            ))
    return violations


# ── فحوصُ مجموعةِ التغيير ────────────────────────────────────────────────────


def changed_paths(mode: str, ref: str | None) -> list[str]:
    if mode == "staged":
        raw = _git("diff", "--cached", "--name-only", "--diff-filter=ACMRD")
    elif mode == "range":
        raw = _git("diff", "--name-only", "--diff-filter=ACMRD", str(ref))
    else:
        raw = _git("show", "--pretty=format:", "--name-only", "--diff-filter=ACMRD", str(ref))
    return sorted({line.strip() for line in raw.splitlines() if line.strip()})


def ledger_diff(mode: str, ref: str | None) -> str:
    if mode == "staged":
        return _git("diff", "--cached", "--unified=0", "--", LEDGER_PATH)
    if mode == "range":
        return _git("diff", "--unified=0", str(ref), "--", LEDGER_PATH)
    return _git("show", "--pretty=format:", "--unified=0", str(ref), "--", LEDGER_PATH)


def base_ref(mode: str, ref: str | None) -> str | None:
    if mode == "staged":
        return "HEAD"
    if mode == "range":
        return str(ref).split("..")[0] or None
    return f"{ref}^"


def base_items(mode: str, ref: str | None) -> list[dict[str, object]] | None:
    """بنودُ الأساسِ لقياسِ الانتقال. `None` إن تعذَّرَ قراءةُ الأساس."""
    base = base_ref(mode, ref)
    if not base:
        return None
    probe = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{base}:{ACTIVE_PATH}"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    if probe.returncode != 0:
        return None
    items, _ = parse_items(_git("show", f"{base}:{ACTIVE_PATH}"))
    return items


def ledger_reverse_links(text: str) -> dict[str, set[str]]:
    """قيدُ `W-###` ← البنودُ التي **يُعلِنُها** صفُّه رابطًا (القياسُ العكسيّ).

    القياسُ القائمُ في `check_change_set` يقرأُ الرابطَ من **البندِ إلى القيدِ**
    (‏خليّةُ «قيدُ السجلّ»)، وتلك الخليّةُ يكتبُها من يجبُ عليه الإغلاقُ — فتكونُ
    فارغةً بعينِ الحالةِ التي بُنِيَ الحرسُ لها. فيُقاسُ هنا الاتِّجاهُ المقابلُ:
    من **القيدِ إلى البند**.
    """
    links: dict[str, set[str]] = {}
    for work_id, body in LEDGER_ROW_RE.findall(text):
        declared = set(LEDGER_ITEM_LINK_RE.findall(body))
        if declared:
            links.setdefault(work_id, set()).update(declared)
    return links


def _has_ledger_at(ref: str) -> bool:
    probe = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{ref}:{LEDGER_PATH}"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    return probe.returncode == 0


def resolve_merge_base(explicit: str | None = None) -> str | None:
    """مرجعُ الفرعِ المدموجِ إليه، أو `None` إن لم يُقرَأْ منه سجلُّ الإكمال.

    ومرجعٌ مُمَرَّرٌ صراحةً لا يُتجاوَزُ إلى غيرِه: من طلبَ أساسًا بعينِه يلزمُه
    جوابٌ عنه لا قياسٌ عن أساسٍ أخرَ في زيِّ جوابِه.
    """
    if explicit:
        return explicit if _has_ledger_at(explicit) else None
    for ref in (os.environ.get(MERGE_BASE_ENV), *MERGE_BASE_CANDIDATES):
        if ref and _has_ledger_at(ref):
            return ref
    return None


def check_post_merge_closure(
    items: list[dict[str, object]], base: str
) -> list[dict[str, str]]:
    """بندٌ قُيِّدَ عملُه في سجلِّ الإكمالِ **المدموجِ** وبقيَ غيرَ `CLOSED` (§ 7)."""
    links = ledger_reverse_links(_git("show", f"{base}:{LEDGER_PATH}"))
    owner: dict[str, set[str]] = {}
    for work_id, declared in links.items():
        for item_id in declared:
            owner.setdefault(item_id, set()).add(work_id)

    violations: list[dict[str, str]] = []
    for it in items:
        item_id = str(it["id"])
        status = str(it["status"])
        if status == "CLOSED" or item_id not in owner:
            continue
        violations.append(_v(
            "POST_MERGE_NOT_CLOSED",
            f"{item_id}: قيدُه ({'، '.join(sorted(owner[item_id]))}) مدموجٌ في «{base}» "
            f"وحالتُه ما زالت {status} — يُنقَلُ إلى CLOSED ويُكتَبُ فيه W-### "
            f"ورقمُ الدمجِ (THE_ROADMAP § 7 واجب 2)",
        ))
    return violations


def requires_claim(path: str) -> bool:
    if path in EXEMPT_EXACT or path.startswith(EXEMPT_PREFIXES):
        return False
    return not path.endswith(EXEMPT_SUFFIXES)


def check_change_set(
    mode: str, ref: str | None, items: list[dict[str, object]]
) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    paths = changed_paths(mode, ref)
    governed = [p for p in paths if requires_claim(p)]

    claimed: list[tuple[str, str]] = [
        (str(it["id"]), str(p))
        for it in items
        if str(it["status"]) in CLAIMING_STATUSES
        for p in it["paths"]  # type: ignore[union-attr]
    ]
    for path in governed:
        if not any(_covers(claim, path) for _, claim in claimed):
            violations.append(_v(
                "PATH_UNCLAIMED",
                f"«{path}» تغيَّرَ ولا بندَ نشِطٌ يُعلِنُه في مساراتِه — "
                f"سجِّلْ بندَك في {ACTIVE_PATH} قبلَ العمل (THE_ROADMAP § 2 قاعدة 1)",
            ))

    recorded = set(ADDED_WORK_ID_RE.findall(ledger_diff(mode, ref)))
    if recorded:
        for it in items:
            links = set(WORK_ID_IN_TEXT_RE.findall(str(it["ledger"])))
            if links & recorded and str(it["status"]) != "CLOSED":
                violations.append(_v(
                    "POST_MERGE_NOT_CLOSED",
                    f"{it['id']}: قُيِّدَ عملُه في سجلِّ الإكمال ({'، '.join(sorted(links & recorded))}) "
                    f"وحالتُه ما زالت {it['status']} — واجبُ ما بعدَ الدمج (THE_ROADMAP § 7)",
                ))

    previous = base_items(mode, ref)
    if previous is not None:
        before = {str(it["id"]): str(it["status"]) for it in previous}
        for it in items:
            old = before.get(str(it["id"]))
            new = str(it["status"])
            if old is None or old == new or new not in ALL_STATUSES or old not in ALL_STATUSES:
                continue
            if new not in LEGAL_TRANSITIONS[old]:
                violations.append(_v(
                    "ILLEGAL_TRANSITION",
                    f"{it['id']}: {old} → {new} انتقالٌ غيرُ مسموحٍ — THE_ROADMAP § 4.3",
                ))
    return violations


def _covers(claim: str, path: str) -> bool:
    claim = claim.rstrip("/")
    return path == claim or path.startswith(f"{claim}/")


# ── التشغيل ─────────────────────────────────────────────────────────────────


def run(
    mode: str,
    ref: str | None,
    shape_only: bool,
    today: date,
    merge_base: str | None = None,
    notes: list[str] | None = None,
    enforce_post_merge: bool = False,
) -> list[dict[str, str]]:
    missing = check_registers_exist()
    if missing:
        return missing

    texts = {p: (REPO_ROOT / p).read_text(encoding="utf-8") for p in REQUIRED_REGISTERS}
    items, violations = parse_items(texts[ACTIVE_PATH])
    blocks = parse_detail_blocks(texts[ACTIVE_PATH])
    scopes = parse_scopes(texts[OWNERSHIP_PATH])

    violations += check_sections(texts)
    violations += check_duplicate_ids(texts)
    violations += check_items(items, blocks, scopes, today)
    violations += check_claim_conflicts(items)
    violations += check_discoveries(texts[DISCOVERIES_PATH])
    if not shape_only:
        violations += check_change_set(mode, ref, items)

    # واجبُ ما بعدَ الدمجِ يُقاسُ بأساسِ الدمجِ لا بمجموعةِ التغيير، لأنَّ القيدَ
    # يُدفَعُ معَ العملِ قبلَ الدمجِ والبندُ يومَها `IN_REVIEW` بحقٍ، وإنما يلزمُ
    # الإغلاقُ متى صارَ القيدُ حالةَ الدولةِ في `main`.
    base = resolve_merge_base(merge_base)
    if base:
        overdue = check_post_merge_closure(items, base)
        # إسقاطٌ أم إبلاغٌ؟ `A-2` اعتُمِدَ في 2026-08-30 فطريقُ الإغلاقِ لم يبقَ
        # مقطوعًا — والعلّةُ القائمةُ أخرى: القيدُ يُدفَعُ معَ العملِ (§ 7 واجب 1)
        # فيصيرُ حالةَ الدولةِ لحظةَ الدمجِ، والإغلاقُ لا يصدُقُ قبلَ الدمجِ ولا
        # يُقرأُ حكمُ CI قبلَه (§ 7 واجب 6) — فبينَ الدمجِ والإغلاقِ التزامٌ واحدٌ
        # لا مهربَ منه، وإسقاطٌ فيه يُعلِّمُ الإغلاقَ قبلَ الدمجِ أي دعوى مكانَ قيدٍ.
        # فيُقاسُ ويُعلَنُ دائمًا، ويُسقِطُ بـ`--enforce-post-merge` صريحًا أو بعدَ
        # اعتمادِ `A-3` (§ 13.3 · § 16.4 · `DISC-030`).
        if enforce_post_merge:
            violations += overdue
        elif notes is not None:
            for v in overdue:
                notes.append(f"{v['kind']}: {v['detail']} — إبلاغٌ بلا إسقاطٍ: بينَ الدمجِ والإغلاقِ نافذةُ التزامٍ واحدٍ مشروعةٌ؛ الإسقاطُ بـ`--enforce-post-merge` أو بقرارِ `A-3` (§ 13.3 · `DISC-030`)")
    elif notes is not None:
        notes.append(
            "حرسُ ما بعدَ الدمجِ **لم يُقَسْ**: لا يُقرأُ سجلُّ الإكمالِ من "
            f"«{merge_base or ' أو '.join(MERGE_BASE_CANDIDATES)}» في هذه الشجرةِ — يُمرَّرُ الأساسُ "
            f"بـ`--merge-base REF` أو بمتغيّرِ البيئةِ {MERGE_BASE_ENV}"
        )
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="بوابة حوكمة العمل — لا عملَ غيرُ مُسجَّل، ولا نطاقَ لجهتَين"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--staged", action="store_true", help="فحصُ ما أُدرِجَ للالتزام (الافتراضيّ)")
    group.add_argument("--range", dest="rng", metavar="A..B", help="فحصُ مدى التزامات")
    group.add_argument("--commit", metavar="SHA", help="فحصُ التزامٍ واحد")
    group.add_argument(
        "--self-check", action="store_true", help="فحصُ شكلِ السجلّاتِ وحدَه بلا مجموعةِ تغيير"
    )
    parser.add_argument(
        "--advisory",
        action="store_true",
        help="إبلاغٌ بلا إسقاط — يُستعمَلُ قبلَ اعتمادِ الخارطة (THE_ROADMAP § 16)",
    )
    parser.add_argument(
        "--today", metavar="YYYY-MM-DD", help="تاريخُ المرجعِ لفحصِ انتهاءِ الحجز (للاختبار)"
    )
    parser.add_argument(
        "--merge-base",
        metavar="REF",
        help="مرجعُ الفرعِ المدموجِ إليه لقياسِ واجبِ ما بعدَ الدمج (الافتراضيّ: origin/main ثمَّ main)",
    )
    parser.add_argument(
        "--require-merge-base",
        action="store_true",
        help="رفضٌ (رمز 2) إن لم يُقرأْ أساسُ الدمج — لمنعِ مرورٍ صامتٍ في التكامل",
    )
    parser.add_argument(
        "--enforce-post-merge",
        action="store_true",
        help="جعلُ POST_MERGE_NOT_CLOSED مُسقِطًا (الافتراضيُّ: إبلاغٌ حتّى يُعتمَدَ A-2/A-3)",
    )
    args = parser.parse_args()

    if args.rng:
        mode, ref = "range", args.rng
    elif args.commit:
        mode, ref = "commit", args.commit
    else:
        mode, ref = "staged", None

    try:
        today = date.fromisoformat(args.today) if args.today else date.today()
    except ValueError as exc:
        print(
            f"[WORK GATE] --today يحتاجُ صيغةَ YYYY-MM-DD: {exc}",
            file=sys.stderr,
        )
        return 2

    notes: list[str] = []
    try:
        violations = run(
            mode,
            ref,
            shape_only=bool(args.self_check),
            today=today,
            merge_base=args.merge_base,
            notes=notes,
            enforce_post_merge=bool(args.enforce_post_merge),
        )
    except RuntimeError as exc:
        print(f"[WORK GATE] تعذّرت القراءةُ من git: {exc}", file=sys.stderr)
        return 2

    # حدُّ القياسِ يُعلَنُ دائمًا: ما لم يُقَسْ لا يُسكَتُ عنه.
    for note in notes:
        print(f"[WORK GATE] ⚠ {note}", file=sys.stderr)
    if args.require_merge_base and resolve_merge_base(args.merge_base) is None:
        print("[WORK GATE] رفضٌ: طُلِبَ أساسُ الدمجِ ولم يُقرأْ.", file=sys.stderr)
        return 2

    if not violations:
        print("[WORK GATE] ✓ كلُّ عملٍ مُسجَّلٌ ومملوكٌ ولا تقاطع — لا مخالفة.")
        return 0

    print(f"[WORK GATE] ✗ مخالفات: {len(violations)}")
    for v in violations:
        print(f"  {v['kind']}: {v['detail']}")
    print(f"\n  القانونُ الملزم: {ROADMAP_PATH} § 2 · § 6 · § 7")
    if args.advisory:
        print("  [ADVISORY] الخارطةُ لم تُعتمَدْ بعد — إبلاغٌ بلا إسقاط (§ 16).")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
