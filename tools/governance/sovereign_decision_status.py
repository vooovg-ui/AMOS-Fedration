#!/usr/bin/env python3
"""حالةُ القراراتِ السياديّةِ وما تحجُبُه — رقمٌ يُقاسُ لا ذاكرةٌ تُروى (W-056).

طريقُ الإنفاذ: OWNER_HELD_VERDICT — يُعلِنُ انقضاءَ سندِ الإبلاغِ وA-3 معلَّقًا، فحكمُه رهنُ قرارِ مالكٍ لا شِفرةٍ

الهدف:
    أن يُنتِجَ أيُّ عاملٍ بأمرٍ واحدٍ الجوابَ عن سؤالَينِ صارا يُتناقَلانِ في
    النصِّ ولا يقيسُهما شيءٌ: **ما حالةُ كلِّ قرارٍ سياديٍّ في § 16 من خارطةِ
    العملِ؟** و**ما الذي يُعلِنُ في هذا المستودعِ أنَّه موقوفٌ عليه؟** فتصيرَ
    جملةُ «`A-2` لا يزالُ مُعلَّقًا» قياسًا يُعادُ إنتاجُه، لا خبرًا يحفظُه من
    قرأَ القيدَ الأخير.
النطاق:
    قراءةٌ محضة. يقرأُ جدولَ § 16 وبنودَه من `THE_ROADMAP.md`، ويقرأُ إشاراتِ
    المستودعِ إلى معرِّفاتِ القراراتِ، ويقرأُ صفوفَ `ACTIVE_WORK.md`. **لا
    يُعدِّلُ الخارطةَ ولا سجلًّا ولا يُصدِرُ قرارًا ولا يُفعِّلُ بوّابةً.**
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-08-27

لماذا أداةٌ لا فقرةٌ في وثيقة
-----------------------------
قِيسَ قبلَ كتابةِ هذا الملفِّ أنَّ حالةَ القراراتِ السياديّةِ **يُبنى عليها
عملٌ ولا يقرأُها أحد**:

1. `DISC-012` يحبِسُ بنودًا مدموجةً مفتوحةً لأنَّ `A-2` مُعلَّقٌ، وذاك مكتوبٌ
   في السجلّاتِ **نصًّا** — فمن أرادَ التحقُّقَ قرأَ فقرةً، ومن نسيَ أعادَ
   السؤالَ. لا أمرَ يطبعُ الحالةَ.
2. وفي شِفرةِ `check_work_governance.py` تعليقٌ وسطرُ مساعدةٍ يقولانِ إنَّ
   الحرسَ «يُسقِطُ … **بعدَ اعتمادِ `A-2`/`A-3`**» — و**لا سطرَ في الشجرةِ
   كلِّها يقرأُ حالةَ `A-2` أو `A-3`** قبلَ هذا الملفِّ. فالشرطُ المُعلَنُ
   وعدٌ لا آلة: لو اعتُمِدَ القرارانِ اليومَ لَما تغيَّرَ سلوكُ حرفٍ واحدٍ
   بنفسِه.

فهذه الأداةُ **تُنشِئُ المقياسَ الغائبَ** ولا تُنشِئُ سلطةً: تطبعُ الحالةَ،
وتُسمّي التناقُضَ حيثُ يقعُ، وتعدُّ ما يُعلِنُ توقُّفَه على قرارٍ مُعلَّقٍ.

ما يُسقِطُ وما يُبلِغُ — والفرقُ مقصودٌ
--------------------------------------
* **يُسقِطُ (رمز 1) على ما تُصلِحُه يدُ من يُحرِّرُ الجدولَ**: حالةٌ لا تُعرَفُ
  (`UNKNOWN_DECISION_STATUS`) · قرارٌ «مُعتمَدٌ» بلا تاريخٍ (`APPROVED_WITHOUT_DATE`)
  · قرارٌ «مُعلَّقٌ» يحملُ تاريخَ حسمٍ (`PENDING_WITH_DATE`) · تاريخٌ في
  المستقبلِ (`DECISION_DATE_IN_FUTURE`) · معرِّفٌ يُبنى عليه في المستودعِ ولا
  صفَّ له في الجدولِ (`DANGLING_DECISION_REF`).
* **يُبلِغُ ولا يُسقِطُ** على `ADVISORY_BASIS_EXPIRED`: أن يكونَ سندُ وضعِ
  الإبلاغِ في § 16 معلَّقًا على كونِ الوثيقةِ `PROPOSED` وهي لم تبقَ كذلك.
  حسمُ ذلك بيدِ المالكِ (`A-3`) لا بيدِ منفِّذٍ، وإسقاطٌ على ما لا يُستطاعُ
  عقوبةٌ لا حرسٌ (سابقةُ § 13.3 · `W-054`). ويُسقِطُ بـ`--enforce-basis` صريحًا.

الحدُّ المُعلَنُ ولا يُزعَمُ أكثرُ منه
------------------------------------
* **لا يُقاسُ عمرُ التعليقِ**: جدولُ § 16 لا يحملُ تاريخَ طلبِ القرارِ، فلا
  يُعرَفُ متى صارَ `A-2` مُعلَّقًا. والمطبوعُ **حدٌّ أدنى مُشتَقٌّ** من تاريخِ
  أوّلِ قرارٍ مُعتمَدٍ، ويُسمّى حدًّا أدنى لا عمرًا.
* **لا تُقاسُ صحّةُ دعوى التوقُّفِ**: تُعَدُّ الإشاراتُ التي تقولُ «موقوفٌ على
  `A-2`»، ولا يُحكَمُ هل التوقُّفُ لازمٌ حقًّا — ذاك حكمٌ على معنًى.
* **لا تُفعَّلُ بوّابةٌ ولا يُوصَلُ حرسٌ**: وصلُ هذا المقياسِ بـ
  `check_work_governance.py` يمسُّ ملفًّا **محجوزًا للبندِ `WI-006`/`WI-009`**،
  وتفعيلُ الإسقاطِ نفسُه هو `A-3` — قرارُ مالكٍ. فالمقياسُ يُبنى اليومَ
  ويُوصَلُ حينَ يُؤذَنُ.
* **ولا تُعدَّلُ الخارطةُ من هنا**: بوّابةٌ تُصلِحُ ما تحكمُ عليه لا تُثبِتُ
  شيئًا (سابقتا `W-037` · `W-038`).

الاستعمالُ
---------
    python tools/governance/sovereign_decision_status.py
    python tools/governance/sovereign_decision_status.py --json
    python tools/governance/sovereign_decision_status.py --enforce-basis

يخرجُ بصفرٍ إن استقامَ الجدولُ، وبواحدٍ على مخالفةٍ تُصلَحُ بيدٍ، وباثنَينِ إذا
عجزَ عن القراءةِ أصلًا — فلا يُقالُ «لا مخالفة» عن جدولٍ لم يُقرَأ.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import UTC, date, datetime
from pathlib import Path

#: جذرُ المستودعِ — يُشتَقُّ من موضعِ الملفِّ لا من مجلَّدِ التشغيل.
REPO_ROOT = Path(__file__).resolve().parents[2]

#: الوثيقةُ التي تحملُ جدولَ القراراتِ السياديّة.
ROADMAP = Path("docs/governance/work/THE_ROADMAP.md")

#: سجلُّ العملِ النشِطِ — منه يُعَدُّ ما يُعلِنُ توقُّفَه على قرارٍ مُعلَّق.
ACTIVE_WORK = Path("docs/governance/work/ACTIVE_WORK.md")

#: حالةُ الوثيقةِ المُعلَنةُ في ترويستِها: «> **الحالة:** `ACTIVE — …`».
DOC_STATE_RE = re.compile(r"^>\s*\*\*الحالة:\*\*\s*`([A-Z_]+)", re.MULTILINE)

#: عنوانُ قسمِ الاعتماد: «## 16 · اعتمادُ هذه الوثيقةِ وتعديلُها».
SECTION_RE = re.compile(r"^##\s+16\s*·", re.MULTILINE)

#: صفُّ قرارٍ في جدولِ § 16: «| A-2 | تعيينُ … | المالك | — | `PENDING` |».
DECISION_ROW_RE = re.compile(
    r"^\|\s*(A-\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|", re.MULTILINE
)

#: رمزُ الحالةِ داخلَ خليّتِها: «`APPROVED` (نافذة)» ← `APPROVED`.
STATUS_TOKEN_RE = re.compile(r"`([A-Z_]+)`")

#: تاريخٌ بصيغةِ ISO في خليّةٍ.
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

#: إشارةٌ إلى معرِّفِ قرارٍ في نصِّ المستودع.
REF_RE = re.compile(r"\bA-(\d+)\b")

#: الحالاتُ المعروفةُ لقرارٍ سياديّ — وما خرجَ عنها لا يُفسَّرُ باجتهادٍ.
KNOWN_STATUSES = frozenset(
    {"APPROVED", "PENDING", "REJECTED", "DEFERRED", "SUPERSEDED"}
)

#: حالاتٌ تُعَدُّ حجبًا: عملٌ يُعلِنُ توقُّفَه عليها لا يجدُ طريقًا.
BLOCKING_STATUSES = frozenset({"PENDING", "DEFERRED"})

#: أين تُلتقَطُ الإشاراتُ — نصُّ الدولةِ وشِفرتُها، لا مخرجاتُ تشغيلٍ.
SCAN_DIRS = ("docs", "tools", "tests")
SCAN_SUFFIXES = (".md", ".py", ".yml", ".yaml")
SKIP_PARTS = frozenset({".git", "__pycache__", ".venv", "node_modules", "backups"})

#: يُستثنى من عدِّ الإشاراتِ: الخارطةُ (الجدولُ ليس إشارةً إلى نفسِه)، وهذا
#: الملفُّ وفحصُه — **وصفُ الحجبِ ليس حجبًا**، وعدُّ الأداةِ نفسَها يُنفِّخُ
#: الرقمَ الذي تقيسُه (سابقةُ `W-029`: «وصفُ الدَّينِ يُعَدُّ دَينًا»).
SELF_EXCLUDED = (
    ROADMAP.as_posix(),
    "tools/governance/sovereign_decision_status.py",
    "tests/governance/test_w056_sovereign_decision_status.py",
)


class MeasurementRefused(Exception):
    """عجزٌ عن القياسِ يُعلَنُ مُصنَّفًا — لا يُبتلَعُ فيُقرأَ نظافةً."""

    def __init__(self, kind: str, detail: str) -> None:
        super().__init__(detail)
        self.kind = kind
        self.detail = detail


@dataclass(frozen=True)
class Decision:
    """صفُّ قرارٍ كما هو مكتوبٌ — لا كما يُفهَمُ."""

    ident: str
    subject: str
    owner: str
    date_text: str
    status: str
    on_date: str | None

    @property
    def is_blocking(self) -> bool:
        return self.status in BLOCKING_STATUSES


@dataclass
class Report:
    """ما قِيسَ في تشغيلةٍ واحدةٍ — يُطبَعُ نصًّا أو JSON."""

    measured_at: str
    doc_state: str
    advisory_basis_state: str | None
    decisions: list[Decision] = field(default_factory=list)
    references: dict[str, list[str]] = field(default_factory=dict)
    frozen_items: dict[str, list[str]] = field(default_factory=dict)
    violations: list[dict[str, str]] = field(default_factory=list)
    notes: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "measured_at": self.measured_at,
            "doc_state": self.doc_state,
            "advisory_basis_state": self.advisory_basis_state,
            "decisions": [asdict(d) for d in self.decisions],
            "references": self.references,
            "frozen_items": self.frozen_items,
            "violations": self.violations,
            "notes": self.notes,
        }


def _v(kind: str, detail: str) -> dict[str, str]:
    return {"kind": kind, "detail": detail}


def _read(root: Path, rel: Path) -> str:
    path = root / rel
    if not path.is_file():
        raise MeasurementRefused(
            "SOURCE_MISSING", f"«{rel}» غيرُ موجودٍ — لا جدولَ يُقرَأُ ولا حكمَ يُقال."
        )
    return path.read_text(encoding="utf-8")


def section_16(text: str) -> str:
    """نصُّ § 16 وحدَه — ولا يُقاسُ جدولٌ من قسمٍ آخرَ يُشبِهُه."""
    match = SECTION_RE.search(text)
    if not match:
        raise MeasurementRefused(
            "SECTION_MISSING",
            "قسمُ «§ 16 · اعتمادُ هذه الوثيقةِ» غيرُ موجودٍ في الخارطةِ — "
            "فلا مصدرَ لحالةِ القراراتِ السياديّة.",
        )
    rest = text[match.end() :]
    nxt = re.search(r"^##\s", rest, re.MULTILINE)
    return rest[: nxt.start()] if nxt else rest


def parse_decisions(section: str) -> list[Decision]:
    """صفوفُ الجدولِ كما كُتِبَت — والجدولُ الخالي رفضٌ لا نتيجةٌ خالية."""
    out: list[Decision] = []
    for row in DECISION_ROW_RE.finditer(section):
        ident, subject, owner, date_cell, status_cell = (
            row.group(1),
            row.group(2).strip(),
            row.group(3).strip(),
            row.group(4).strip(),
            row.group(5).strip(),
        )
        token = STATUS_TOKEN_RE.search(status_cell)
        status = token.group(1) if token else status_cell.strip("* ").upper()
        found = DATE_RE.search(date_cell)
        out.append(
            Decision(
                ident=ident,
                subject=subject,
                owner=owner,
                date_text=date_cell,
                status=status,
                on_date=found.group(1) if found else None,
            )
        )
    if not out:
        raise MeasurementRefused(
            "NO_DECISION_ROWS",
            "قسمُ § 16 موجودٌ ولا صفَّ قرارٍ يُقرَأُ فيه — "
            "لا يُقالُ «لا مخالفة» عن جدولٍ لم يُفهَمْ شكلُه.",
        )
    return out


def advisory_basis_state(section: str) -> str | None:
    """الحالةُ التي عُلِّقَ عليها وضعُ الإبلاغِ في § 16 — أو `None` إن لم تُذكَرْ."""
    for line in section.splitlines():
        if "الإبلاغ" in line and "`--advisory`" in line:
            token = re.search(r"`?([A-Z_]{4,})`?", line)
            if token:
                return token.group(1)
    return None


def doc_state(text: str) -> str:
    match = DOC_STATE_RE.search(text)
    if not match:
        raise MeasurementRefused(
            "DOC_STATE_MISSING",
            "الخارطةُ لا تُعلِنُ حالتَها («> **الحالة:** `…`») — "
            "فلا يُقاسُ هل سندُ وضعِ الإبلاغِ قائمٌ أم انقضى.",
        )
    return match.group(1)


def _scan_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for folder in SCAN_DIRS:
        base = root / folder
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix not in SCAN_SUFFIXES:
                continue
            if SKIP_PARTS & set(path.parts):
                continue
            files.append(path)
    return files


def collect_references(
    root: Path, known: set[str]
) -> tuple[dict[str, list[str]], set[str], list[str]]:
    """مواضعُ الإشارةِ إلى كلِّ معرِّفِ قرارٍ — ومعرِّفاتٌ يُبنى عليها بلا صفٍّ.

    يُستثنى ما في `SELF_EXCLUDED`: الجدولُ ليس إشارةً إلى نفسِه، وأداةُ القياسِ
    لا تُعَدُّ من المتوقِّفِ على القرارِ لمجرَّدِ أنَّها تسمّيه.
    """
    refs: dict[str, list[str]] = {}
    unknown: set[str] = set()
    unreadable: list[str] = []
    for path in _scan_files(root):
        rel = path.relative_to(root).as_posix()
        if rel in SELF_EXCLUDED:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError as err:
            # لا يُبتلَعُ: ملفٌّ لم يُقرَأْ يُسمّى في التقريرِ، وإلّا قُرِئَ
            # نقصُ العدِّ اكتمالًا (سابقةُ `SILENT_FALLBACK` · § 13).
            unreadable.append(f"{rel} ({err.reason})")
            continue
        for number, line in enumerate(lines, start=1):
            for hit in REF_RE.finditer(line):
                ident = f"A-{hit.group(1)}"
                refs.setdefault(ident, []).append(f"{rel}:{number}")
                if ident not in known:
                    unknown.add(ident)
    return refs, unknown, unreadable


def collect_frozen_items(
    root: Path, blocking: set[str]
) -> tuple[dict[str, list[str]], bool]:
    """بنودُ `ACTIVE_WORK` التي يُعلِنُ صفُّها توقُّفَها على قرارٍ حاجبٍ.

    تُعيدُ معها عَلَمًا يقولُ: هل قُرِئَ سجلُّ العملِ أصلًا؟ غيابُه ليس «لا بندَ
    متوقِّفًا» — بل قياسٌ لم يُجرَ، ويُعلَنُ كذلك في التقرير.
    """
    frozen: dict[str, list[str]] = {}
    if not (root / ACTIVE_WORK).is_file():
        return frozen, False
    text = _read(root, ACTIVE_WORK)
    for line in text.splitlines():
        row = re.match(r"^\|\s*(WI-\d+)\s*\|", line)
        if not row:
            continue
        for ident in blocking:
            if ident in line:
                frozen.setdefault(ident, []).append(row.group(1))
    return frozen, True


def measure(root: Path | None = None, today: date | None = None) -> Report:
    """القياسُ كلُّه في دالّةٍ واحدةٍ تُستدعى من فحصٍ كما تُستدعى من سطرِ أمر."""
    root = root or REPO_ROOT
    now = today or datetime.now(UTC).date()
    text = _read(root, ROADMAP)
    section = section_16(text)
    decisions = parse_decisions(section)
    state = doc_state(text)
    basis = advisory_basis_state(section)

    known = {d.ident for d in decisions}
    refs, unknown, unreadable = collect_references(root, known)
    blocking = {d.ident for d in decisions if d.is_blocking}
    frozen, work_read = collect_frozen_items(root, blocking)

    report = Report(
        measured_at=datetime.now(UTC).isoformat(timespec="seconds"),
        doc_state=state,
        advisory_basis_state=basis,
        decisions=decisions,
        references={k: refs.get(k, []) for k in sorted(known)},
        frozen_items=frozen,
    )

    for d in decisions:
        if d.status not in KNOWN_STATUSES:
            report.violations.append(
                _v(
                    "UNKNOWN_DECISION_STATUS",
                    f"«{d.ident}» حالتُه «{d.status}» وليست من الحالاتِ المعروفةِ "
                    f"({' · '.join(sorted(KNOWN_STATUSES))}) — حالةٌ لا تُفسَّرُ باجتهادٍ.",
                )
            )
        if d.status == "APPROVED" and not d.on_date:
            report.violations.append(
                _v(
                    "APPROVED_WITHOUT_DATE",
                    f"«{d.ident}» مُعتمَدٌ بلا تاريخٍ — اعتمادٌ لا يُعرَفُ متى وقعَ "
                    "لا يُقاسُ عليه أثرٌ.",
                )
            )
        if d.is_blocking and d.on_date:
            report.violations.append(
                _v(
                    "PENDING_WITH_DATE",
                    f"«{d.ident}» حالتُه «{d.status}» ويحملُ تاريخَ {d.on_date} — "
                    "إمّا حُسِمَ فتُصحَّحُ حالتُه، وإمّا لم يُحسَمْ فيُرفَعُ تاريخُه.",
                )
            )
        if d.on_date and date.fromisoformat(d.on_date) > now:
            report.violations.append(
                _v(
                    "DECISION_DATE_IN_FUTURE",
                    f"«{d.ident}» مؤرَّخٌ بـ{d.on_date} وهو بعدَ اليومِ ({now}) — "
                    "قرارٌ لم يقعْ يُعلَنُ واقعًا.",
                )
            )

    for ident in sorted(unknown):
        where = refs.get(ident, [])
        report.violations.append(
            _v(
                "DANGLING_DECISION_REF",
                f"«{ident}» يُبنى عليه في {len(where)} موضعًا "
                f"(أوّلُها {where[0] if where else '—'}) ولا صفَّ له في § 16 — "
                "إحالةٌ إلى قرارٍ لا وجودَ له.",
            )
        )

    if basis and state != basis:
        report.violations.append(
            _v(
                "ADVISORY_BASIS_EXPIRED",
                f"سندُ وضعِ الإبلاغِ في § 16 معلَّقٌ على كونِ الوثيقةِ «{basis}» "
                f"وحالتُها المُعلَنةُ «{state}» — فالسندُ انقضى، ومع ذلك يبقى "
                f"{len(blocking)} قرارًا حاجبًا مُعلَّقًا "
                f"({' · '.join(sorted(blocking)) or '—'}). "
                "حسمُ ذلك بيدِ المالكِ (تعديلُ § 16 أو اعتمادُ التفعيلِ) لا بيدِ منفِّذٍ.",
            )
        )

    approved = [date.fromisoformat(d.on_date) for d in decisions if d.on_date]
    if blocking and approved:
        floor = min(approved)
        report.notes.append(
            _v(
                "PENDING_SINCE_AT_LEAST",
                f"{' · '.join(sorted(blocking))}: مُعلَّقٌ منذُ {floor} على الأقلِّ "
                f"({(now - floor).days} يومًا) — **حدٌّ أدنى مُشتَقٌّ** من أوّلِ "
                "قرارٍ مؤرَّخٍ، لا عمرٌ مقيسٌ: الجدولُ لا يحملُ تاريخَ طلبِ القرار.",
            )
        )
    if unreadable:
        report.notes.append(
            _v(
                "UNREADABLE_SOURCE",
                f"{len(unreadable)} ملفًّا لم يُقرَأْ في عدِّ الإشاراتِ "
                f"({' · '.join(unreadable[:5])}) — العدُّ أدناه **ناقصٌ بقدرِها**، "
                "ولا يُقرأُ نقصُه اكتمالًا.",
            )
        )
    if not work_read:
        report.notes.append(
            _v(
                "WORK_REGISTER_UNREAD",
                f"«{ACTIVE_WORK.as_posix()}» غيرُ موجودٍ — فقائمةُ البنودِ المتوقِّفةِ "
                "**لم تُقَسْ**، وليست صفرًا مقيسًا.",
            )
        )
    for ident in sorted(blocking):
        report.notes.append(
            _v(
                "BLOCKING_DECISION",
                f"{ident}: يُشارُ إليه في {len(refs.get(ident, []))} موضعًا · "
                f"وبنودٌ تُعلِنُ توقُّفَها عليه: "
                f"{' · '.join(frozen.get(ident, [])) or 'لا شيء'}.",
            )
        )
    return report


def render(report: Report) -> str:
    lines = ["[SOVEREIGN DECISIONS] حالةُ § 16 كما هي مكتوبةٌ:"]
    lines.append(f"  حالةُ الخارطةِ المُعلَنةُ: {report.doc_state}")
    lines.append(
        f"  سندُ وضعِ الإبلاغِ في § 16: {report.advisory_basis_state or '— غيرُ مذكورٍ'}"
    )
    lines.append("  استُثنيَ من عدِّ الإشاراتِ: " + " · ".join(SELF_EXCLUDED))
    for d in report.decisions:
        refs = len(report.references.get(d.ident, []))
        lines.append(
            f"  {d.ident} · {d.status:<10} · تاريخٌ: {d.on_date or '—'} · "
            f"إشاراتٌ: {refs} · {d.subject[:60]}"
        )
    for note in report.notes:
        lines.append(f"  ملاحظة · {note['kind']}: {note['detail']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="قياسُ حالةِ القراراتِ السياديّةِ في § 16 وما يُعلِنُ توقُّفَه عليها"
    )
    parser.add_argument("--root", default=str(REPO_ROOT), help="جذرُ المستودعِ المقيس")
    parser.add_argument(
        "--json", action="store_true", help="مخرَجٌ بصيغةِ JSON على المخرَجِ القياسيّ"
    )
    parser.add_argument(
        "--enforce-basis",
        action="store_true",
        help="جعلُ ADVISORY_BASIS_EXPIRED مُسقِطًا (الافتراضيُّ: إبلاغٌ — حسمُه بيدِ المالك)",
    )
    args = parser.parse_args(argv)

    try:
        report = measure(Path(args.root))
    except MeasurementRefused as exc:
        print(
            f"[SOVEREIGN DECISIONS] رفضٌ مُصنَّفٌ · {exc.kind}: {exc.detail}",
            file=sys.stderr,
        )
        return 2

    if args.json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(render(report))

    advisory = [v for v in report.violations if v["kind"] == "ADVISORY_BASIS_EXPIRED"]
    hard = [v for v in report.violations if v["kind"] != "ADVISORY_BASIS_EXPIRED"]
    for v in advisory:
        suffix = (
            ""
            if args.enforce_basis
            else " — إبلاغٌ بلا إسقاطٍ: الحسمُ بيدِ المالكِ (§ 13.3)"
        )
        print(
            f"[SOVEREIGN DECISIONS] {v['kind']}: {v['detail']}{suffix}", file=sys.stderr
        )
    for v in hard:
        print(
            f"[SOVEREIGN DECISIONS] مخالفة · {v['kind']}: {v['detail']}",
            file=sys.stderr,
        )

    if hard or (advisory and args.enforce_basis):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
