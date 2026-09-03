#!/usr/bin/env python3
"""مساءلةُ القيدِ المفتوحِ — قيدٌ بلا حرسٍ ولا استحقاقٍ يُقاسُ لا يُقرَأُ (W-059).

الهدف:
    أن يكونَ لكلِّ قيدٍ مفتوحٍ في سجلَّي الاكتشافاتِ والمخاطرِ **مِرساةُ
    مساءلةٍ** مقيسةٌ من الشجرةِ: إمّا حرسٌ قائمٌ يسقُطُ حينَ يعودُ العطبُ أو
    يتَّسِعُ، وإمّا تاريخُ استحقاقٍ مُعلَنٌ، وإمّا إعلانٌ صريحٌ أنَّ القيدَ بيدِ
    المالكِ فلا فعلَ لمنفِّذٍ فيه. والقيدُ الذي لا مِرساةَ له يُعَدُّ ويُسمَّى.
النطاق:
    `docs/governance/work/DISCOVERIES.md § 1` و`docs/governance/work/RISK_REGISTER.md § 1`
    وحدَهما، ووجودُ المساراتِ التي تذكرُها صفوفُهما في الشجرة. لا شبكةَ ولا
    قاعدةَ ولا سرَّ ولا حسابَ Actions. ولا تكتبُ الأداةُ سطرًا في سجلٍّ تحكمُ عليه.
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-28
تاريخ آخر تعديل: 2026-09-03

لماذا أداةٌ لا فقرةٌ:
    قِيدَ في `DISC-018` أنَّ **القيدَ المفتوحَ لا يمنعُ اتِّساعَ العطبِ**:
    `DISC-013` كُتِبَ بفارقِ ستَّةِ قيودٍ وبقيَ مفتوحًا حتى بلغَ الفارقُ تسعةً،
    أي أنَّ ثلاثةَ قيودٍ أُضيفَت بعدَ اكتشافِ العطبِ ولم تُصحِّحْ أيٌّ منها
    الوثيقةَ. ووجهةُ ذلك الاكتشافِ المكتوبةُ: «تعميمُ القاعدةِ — لكلِّ قيدٍ حرسٌ
    أو تاريخُ استحقاقٍ». والتعميمُ إن كُتِبَ فقرةً في وثيقةٍ عادَ إلى ما يشتكي
    منه: نصٌّ لا يقرؤه شيءٌ. فصارَ **آلةً لها رمزُ خروجٍ**.

الحدُّ المُعلَنُ — لا مطويٌّ:
    * تقيسُ الأداةُ **وجودَ المِرساةِ لا كفايتَها**: صفٌّ يذكرُ ملفَّ حرسٍ قائمًا
      يُعَدُّ مُرسًى ولو كانَ ذاك الحرسُ لا يحرسُ عينَ العطبِ المُقيَّدِ. مطابقةُ
      «ما يحرسُه الحرسُ» بـ«ما يشتكيه القيدُ» حكمٌ بشريٌّ لا مُطابَقةُ نصٍّ.
    * وتقيسُ **ما تُعلِنُه الخليّةُ لا ما يُنويه كاتبُها**: قيدٌ محروسٌ فعلًا ولا
      يذكرُ حرسَه في صفِّه يُعَدُّ بلا مِرساةٍ — وذاك مقصودٌ: المِرساةُ غيرُ
      المُعلَنةِ لا يجدُها قارئٌ.
    * ولا تفصلُ الأداةُ في **صدقِ** إعلانِ «بيدِ المالكِ»: من كتبَ ذلك أعلنَه،
      وحرسُه مراجعةٌ بشريّةٌ. وهذه الفئةُ تُعَدُّ **إبلاغًا لا إسقاطًا**.
    * وسجلُّ المخاطرِ **لا عمودَ حالةٍ فيه**: كلُّ صفٍّ في § 1 مفتوحٌ بنصِّ
      عنوانِ القسمِ، فلا يُستنبَطُ إغلاقٌ من نصٍّ حرٍّ.
    * ولا تُنشَرُ الأداةُ ملفَّ قياسٍ في `docs/audit/measurements/`: نشرُ ملفٍّ
      هناك يوجِبُ قيدَ نَسَبٍ في `measurement_provenance.py` وهو **محجوزٌ**
      لبندٍ مفتوحٍ (`DISC-014`) — فالمُخرَجُ إلى المِخرَجِ القياسيِّ وحدَه.

الاستعمال:
    python tools/governance/open_record_accountability.py
    python tools/governance/open_record_accountability.py --json
    python tools/governance/open_record_accountability.py --root /مسار/استنساخٍ

رموزُ الخروج:
    0 = لا مخالفةَ · 1 = مخالفةٌ مقيسةٌ · 2 = **رفضٌ مُصنَّفٌ** (القياسُ لم يُجرَ)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass, field
from datetime import UTC, date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

WORK_DIR = Path("docs/governance/work")
DISCOVERIES = WORK_DIR / "DISCOVERIES.md"
RISKS = WORK_DIR / "RISK_REGISTER.md"

#: عنوانُ قسمِ الصفوفِ في كلِّ سجلٍّ — يُطلَبُ حضورُه قبلَ أيِّ قياسٍ.
SECTION_HEADINGS = {
    DISCOVERIES.as_posix(): "## 1 · الاكتشافاتُ المُقيَّدة",
    RISKS.as_posix(): "## 1 · المخاطرُ المفتوحة",
}

DISC_ROW_RE = re.compile(r"^\|\s*(DISC-\d{3})\s*\|")
RISK_ROW_RE = re.compile(r"^\|\s*(RK-\d{3})\s*\|")

#: مسارٌ في الشجرةِ يُذكَرُ في صفٍّ — بعلامةِ اقتباسٍ خلفيّةٍ أو بلا.
PATH_RE = re.compile(r"(?:tools|tests)/[A-Za-z0-9_./-]+\.py\b")
#: تاريخُ استحقاقٍ مُعلَنٌ صراحةً في الصفِّ.
DUE_RE = re.compile(r"استحقاق\s*:\s*(\d{4}-\d{2}-\d{2})")

#: علاماتُ **الإعلانِ المُهيكَلِ للحرسِ** (`WI-039` · `DISC-021`) — والمسارُ لا يُقرأُ
#: إعلانًا إلّا إذا وقعَ في المقطعِ الذي تفتحُه إحداها. وهما علامتانِ مُعلَنتانِ
#: هنا لا جذرُ كلمةٍ يُبحَثُ عنه في نصٍّ حرٍّ: «حرس» في نفيٍ لا يُشبِهُ «حرسٌ قائمٌ:».
GUARD_DECLARATION_MARKERS = ("حرسٌ قائمٌ:", "حرسٌ مُثبَتٌ:")

#: مسارٌ واحدٌ في مقطعِ الإعلانِ — يُقبَلُ فاصلًا `·` أو `و` أو فاصلةً، ويُقبَلُ
#: بعلامةِ اقتباسٍ خلفيّةٍ أو في رابطِ Markdown، ويقفُ المسحُ عندَ أوّلِ ما ليسَ مسارًا.
_DECLARED_TOKEN_RE = re.compile(
    r"\s*(?:[·،,]|و)?\s*\[?`?((?:tools|tests)/[A-Za-z0-9_./-]+\.py)`?(?:\]\([^)]*\))?"
)

#: السقّاطةُ المُعلَنةُ لصفوفِ «مسارٌ في نثرٍ» — مصدرُ حقيقةٍ واحدٌ في سجلِّ
#: الاكتشافاتِ، لا ثابتٌ مدفونٌ في شِفرةٍ. تُقرأُ ولا تُكتَبُ من هنا.
PROSE_BASELINE_RE = re.compile(r"ANCHOR_PROSE_BASELINE:\s*rows=(\d+)")

#: ما يُعلِنُ أنَّ القيدَ بيدِ المالكِ فلا فعلَ لمنفِّذٍ فيه (§ 16.3) — تُقرأُ من
#: **خليّةِ الوجهةِ/المالكِ** وحدَها لا من وصفِ العَطبِ.
OWNER_HELD_MARKERS = (
    "المالك",
    "المجلس التأسيسي",
    "حسمٌ سياديٌّ",
    "قرارًا سياديًّا",
    "قرارٌ سياديٌّ",
)

#: ما يُعلِنُ أنَّ القيدَ لم يَعُدْ مفتوحًا — يُقرأُ من خليّةِ الحالةِ وحدَها.
CLOSED_MARKERS = ("مُغلَق", "مغلق", "مُعالَج", "معالَج", "مُنفَّذ")
OPEN_MARKERS = ("مفتوح",)

#: حركاتٌ وتطويلٌ تُنزَعُ قبلَ المقارنةِ — هي عَينُ جدولِ `check_work_governance.py`
#: ولا تُوسَّعُ إلى مدى يبتلعُ الحروفَ نفسَها (فذاك يُفرِغُ النصَّ فيُطابِقُ كلَّ علامةٍ).
_DIACRITICS = dict.fromkeys(
    [*range(0x064B, 0x0653), 0x0640, 0x0670, 0x06D6, 0x0653, 0x0654, 0x0655]
)

#: عددُ الأعمدةِ المُعلَنِ في ترويسةِ كلِّ سجلٍّ — يُقرأُ حدًّا لا يُظَنُّ.
#: وزيادتُه أخطرُ من نقصِه: خليّةٌ فيها `|` غيرُ مهروبٍ **تنشطرُ**، فتزحفُ
#: الخلايا فيُقرأُ ذيلُ خليّةِ الوجهةِ حالةً وتُقرأُ الحالةُ الحقيقيّةُ في
#: عمودٍ لا يُنظَرُ إليه — حكمٌ على صفٍّ لم يُقرَأْ (‏`DISC-048`).
DECLARED_COLUMNS = 8

ANCHOR_GUARD = "GUARD"
ANCHOR_DUE = "DUE"
ANCHOR_OWNER_HELD = "OWNER_HELD"
ANCHOR_NONE = "NONE"


class MeasurementRefused(Exception):
    """عجزٌ عن القياسِ يُعلَنُ مُصنَّفًا — لا يُبتلَعُ فيُقرأَ نظافةً."""

    def __init__(self, kind: str, detail: str) -> None:
        super().__init__(f"{kind}: {detail}")
        self.kind = kind
        self.detail = detail


@dataclass(frozen=True)
class Record:
    """قيدٌ واحدٌ كما قُرِئَ من صفِّه — لا كما يُظَنُّ به."""

    record_id: str
    register: str
    line: int
    is_open: bool
    open_basis: str
    anchor: str
    guard_paths: tuple[str, ...]
    missing_paths: tuple[str, ...]
    due: str | None
    #: ما وقعَ منها في **إعلانٍ مُهيكَلٍ** (`GUARD_DECLARATION_MARKERS`).
    declared_paths: tuple[str, ...] = ()
    #: ما مرَّ في نثرِ الخليّةِ بلا إعلانٍ — يُعَدُّ ويُسمَّى ولا يُقرأُ ضمانًا.
    prose_paths: tuple[str, ...] = ()


@dataclass
class Report:
    """ما قِيسَ في تشغيلةٍ واحدةٍ — يُطبَعُ نصًّا أو JSON."""

    measured_at: str
    records: list[Record] = field(default_factory=list)
    violations: list[dict[str, str]] = field(default_factory=list)
    notes: list[dict[str, str]] = field(default_factory=list)

    @property
    def open_records(self) -> list[Record]:
        return [r for r in self.records if r.is_open]

    def counted(self, anchor: str) -> int:
        return sum(1 for r in self.open_records if r.anchor == anchor)

    def to_dict(self) -> dict[str, object]:
        return {
            "measured_at": self.measured_at,
            "declared_registers": [DISCOVERIES.as_posix(), RISKS.as_posix()],
            "rows_read": len(self.records),
            "open_rows": len(self.open_records),
            "by_anchor": {
                ANCHOR_GUARD: self.counted(ANCHOR_GUARD),
                ANCHOR_DUE: self.counted(ANCHOR_DUE),
                ANCHOR_OWNER_HELD: self.counted(ANCHOR_OWNER_HELD),
                ANCHOR_NONE: self.counted(ANCHOR_NONE),
            },
            "records": [asdict(r) for r in self.records],
            "violations": self.violations,
            "notes": self.notes,
        }


def _v(kind: str, detail: str) -> dict[str, str]:
    return {"kind": kind, "detail": detail}


def _read(root: Path, rel: Path) -> str:
    target = root / rel
    if not target.is_file():
        raise MeasurementRefused(
            "SOURCE_MISSING",
            f"المصدرُ «{rel.as_posix()}» غيرُ موجودٍ تحتَ «{root}» — "
            "ولا يُقالُ «كلُّ قيدٍ مُرسًى» عن سجلٍّ لم يُقرَأْ.",
        )
    return target.read_text(encoding="utf-8")


def _norm(text: str) -> str:
    """توحيدُ التشكيلِ والمسافاتِ قبلَ أيِّ مقارنةٍ — الحركاتُ لا تُعتَمَدُ حدًّا.

    وهذا شرطٌ لا زينةٌ: السجلّاتُ مشكولةٌ، فمقارنةُ نصٍّ مشكولٍ بعلامةٍ مشكولةٍ
    تسقُطُ على أوّلِ حركةٍ تُزادُ أو تُنقَصُ — فتُقرأُ حالةٌ مُعالَجةٌ «مفتوحةً».
    """
    stripped = unicodedata.normalize("NFC", text).translate(_DIACRITICS)
    return re.sub(r"\s+", " ", stripped).strip()


def _has_marker(text: str, markers: tuple[str, ...]) -> bool:
    """حضورُ علامةٍ بعدَ توحيدِ الطرفَينِ — لا يُقارَنُ مشكولٌ بمشكولٍ."""
    haystack = _norm(text)
    return any(_norm(marker) in haystack for marker in markers)


def _require_section(text: str, rel: Path) -> None:
    heading = SECTION_HEADINGS[rel.as_posix()]
    if _norm(heading) not in _norm(text):
        raise MeasurementRefused(
            "SECTION_MISSING",
            f"«{rel.as_posix()}» بلا القسمِ «{heading}» — إمّا تغيَّرَ شكلُ السجلِّ "
            "وإمّا قُرِئَ ملفٌّ آخرُ، وكلاهما يمنعُ القياسَ.",
        )


#: فاصلُ الخلايا هو `|` **غيرُ مهروبٍ** وحدَه — و`\|` محتوًى لا حدٌّ
#: (‏وهي عينُ قاعدةِ GFM للجداول). وقسمٌ ساذجٌ على `|` يشطرُ خليّةً
#: فيها أمرُ أنبوبٍ، فتزحفُ الأعمدةُ ويُحكَمُ على صفٍّ لم يُقرَأْ (‏`DISC-048`).
_CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")


def _cells(line: str) -> list[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|") and not body.endswith("\\|"):
        body = body[:-1]
    return [c.strip().replace("\\|", "|") for c in _CELL_SPLIT_RE.split(body)]


def _classify_open(status_cell: str) -> tuple[bool, str]:
    """هل الصفُّ مفتوحٌ؟ ومن أيِّ نصٍّ عُرِفَ ذلك — لا من ظنٍّ."""
    cell = _norm(status_cell)
    if _has_marker(cell, OPEN_MARKERS):
        return True, "STATUS_SAYS_OPEN"
    if _has_marker(cell, CLOSED_MARKERS):
        return False, "STATUS_SAYS_CLOSED"
    if not cell or cell == "—":
        return True, "STATUS_EMPTY_READ_OPEN"
    return True, "STATUS_UNDECLARED_READ_OPEN"


def _paths_in(root: Path, text: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """المساراتُ المذكورةُ في خلايا المِرساةِ: ما وُجِدَ في الشجرةِ وما لم يوجَدْ."""
    found: list[str] = []
    missing: list[str] = []
    for raw in dict.fromkeys(PATH_RE.findall(text)):
        if (root / raw).is_file():
            found.append(raw)
        else:
            missing.append(raw)
    return tuple(found), tuple(missing)


def _anchor_of(
    guard_paths: tuple[str, ...], due: str | None, owner_text: str
) -> str:
    """مِرساةُ الصفِّ بترتيبٍ مُعلَنٍ: حرسٌ قائمٌ ، فاستحقاقٌ ، فإعلانُ يدِ المالكِ."""
    if guard_paths:
        return ANCHOR_GUARD
    if due:
        return ANCHOR_DUE
    if _has_marker(owner_text, OWNER_HELD_MARKERS):
        return ANCHOR_OWNER_HELD
    return ANCHOR_NONE


def declared_guard_paths(text: str) -> tuple[str, ...]:
    """المساراتُ الواقعةُ في **إعلانٍ مُهيكَلٍ** للحرسِ داخلَ نصِّ خليّةٍ.

    ولمَ إعلانٌ لا ذِكرٌ: قِيسَ في `W-060` (`DISC-021`) أنَّ صفًّا يكتبُ «لا حرسَ،
    وهذانِ الملفّانِ لا يقيسانِ هذا» يُقرأُ **محروسًا** لمجرَّدِ مرورِ مسارٍ في
    نثرِه — فالنفيُ نفسُه يشتري خُضرةً. والمسحُ هنا يبدأُ من علامةٍ مُعلَنةٍ
    ويقفُ عندَ أوّلِ مقطعٍ ليسَ مسارًا، فلا يبتلعُ ما بعدَه من كلامٍ.
    """
    haystack = _norm(text.replace("*", ""))
    found: list[str] = []
    for marker in GUARD_DECLARATION_MARKERS:
        needle = _norm(marker)
        if not needle:
            # علامةٌ فارغةٌ تُطابِقُ كلَّ موضعٍ فلا تُميِّزُ إعلانًا من نثرٍ — وتقدُّمُ
            # المسحِ بها صِفرٌ فيدورُ بلا نهايةٍ. تُتخطَّى صراحةً لا صمتًا.
            continue
        index = haystack.find(needle)
        while index >= 0:
            position = index + len(needle)
            while match := _DECLARED_TOKEN_RE.match(haystack, position):
                found.append(match.group(1))
                position = match.end()
            index = haystack.find(needle, index + len(needle))
    return tuple(dict.fromkeys(found))


def _rows(text: str, pattern: re.Pattern[str]) -> list[tuple[int, str, str]]:
    out: list[tuple[int, str, str]] = []
    for number, line in enumerate(text.splitlines(), start=1):
        match = pattern.match(line)
        if match:
            out.append((number, match.group(1), line))
    return out


def measure(root: Path | None = None, today: date | None = None) -> Report:
    """القياسُ كلُّه في دالّةٍ واحدةٍ تُستدعى من فحصٍ كما تُستدعى من سطرِ أمر."""
    root = root or REPO_ROOT
    now = today or datetime.now(UTC).date()
    report = Report(measured_at=datetime.now(UTC).isoformat(timespec="seconds"))

    disc_text = _read(root, DISCOVERIES)
    risk_text = _read(root, RISKS)
    _require_section(disc_text, DISCOVERIES)
    _require_section(risk_text, RISKS)

    disc_rows = _rows(disc_text, DISC_ROW_RE)
    risk_rows = _rows(risk_text, RISK_ROW_RE)
    if not disc_rows or not risk_rows:
        raise MeasurementRefused(
            "NO_ROWS",
            "لم يُقرَأْ صفٌّ واحدٌ في أحدِ السجلَّينِ "
            f"(اكتشافاتٌ: {len(disc_rows)} · مخاطرُ: {len(risk_rows)}) — "
            "سجلٌّ بلا صفوفٍ لا يُقاسُ عليه.",
        )

    for line_no, record_id, line in disc_rows:
        cells = _cells(line)
        if len(cells) != DECLARED_COLUMNS:
            report.violations.append(
                _v(
                    "MALFORMED_ROW",
                    f"{record_id}: صفُّ اكتشافٍ بـ{len(cells)} خليّةً — الإلزاميُّ "
                    f"{DECLARED_COLUMNS}، فلا تُقرأُ حالتُه ولا وجهتُه"
                    + (
                        " (‏زيادةٌ سببُها `|` غيرُ مهروبٍ في خليّةٍ: الخلايا تزحفُ "
                        "فيُقرأُ عمودٌ مكانَ عمودٍ)."
                        if len(cells) > DECLARED_COLUMNS
                        else "."
                    ),
                )
            )
            continue
        is_open, basis = _classify_open(cells[7])
        # مِرساةُ الاكتشافِ تُقرأُ من **الوجهةِ والحالةِ** لا من الصفِّ كلِّهِ:
        # ملفٌّ يُذكَرُ في خليّةِ الدليلِ موضِعُ عَطبٍ لا حارِسٌ له.
        anchor_text = f"{cells[6]} {cells[7]}"
        owner_text = anchor_text
        guard_paths, missing = _paths_in(root, anchor_text)
        declared = tuple(p for p in guard_paths if p in declared_guard_paths(anchor_text))
        prose = tuple(p for p in guard_paths if p not in declared)
        due_match = DUE_RE.search(anchor_text)
        due = due_match.group(1) if due_match else None
        report.records.append(
            Record(
                record_id=record_id,
                register=DISCOVERIES.as_posix(),
                line=line_no,
                is_open=is_open,
                open_basis=basis,
                anchor=_anchor_of(guard_paths, due, owner_text),
                guard_paths=guard_paths,
                missing_paths=missing,
                due=due,
                declared_paths=declared,
                prose_paths=prose,
            )
        )

    for line_no, record_id, line in risk_rows:
        cells = _cells(line)
        if len(cells) != DECLARED_COLUMNS:
            report.violations.append(
                _v(
                    "MALFORMED_ROW",
                    f"{record_id}: صفُّ خطرٍ بـ{len(cells)} خليّةً — الإلزاميُّ "
                    f"{DECLARED_COLUMNS}، فلا تُقرأُ إشارتُه المبكِّرةُ ولا مالكُه"
                    + (
                        " (‏زيادةٌ سببُها `|` غيرُ مهروبٍ في خليّةٍ: الخلايا تزحفُ "
                        "فيُقرأُ عمودٌ مكانَ عمودٍ)."
                        if len(cells) > DECLARED_COLUMNS
                        else "."
                    ),
                )
            )
            continue
        # مِرساةُ الخطرِ: الإشارةُ المبكِّرةُ · التصرُّفُ · المالكُ · المصدرُ — وهي الخلايا
        # التي تقولُ ما يُرى وما يُفعَلُ ومن يُسأَلُ، دونَ خليّةِ وصفِ الخطرِ نفسِهِ.
        anchor_text = " ".join(cells[4:8])
        # ويدُ المالكِ تُقرأُ من **خليّةِ المالكِ والتصرُّفِ** لا من وصفِ الخطرِ:
        # خطرٌ موضوعُهُ تأخُّرُ قرارِ المالكِ ليس خطرًا بيدِهِ بمجرَّدِ ذِكرِهِ.
        owner_text = f"{cells[5]} {cells[6]}"
        guard_paths, missing = _paths_in(root, anchor_text)
        declared = tuple(p for p in guard_paths if p in declared_guard_paths(anchor_text))
        prose = tuple(p for p in guard_paths if p not in declared)
        due_match = DUE_RE.search(anchor_text)
        due = due_match.group(1) if due_match else None
        if not cells[4] or cells[4] == "—":
            report.violations.append(
                _v(
                    "RISK_SIGNAL_EMPTY",
                    f"{record_id}: بلا «إشارةٍ مبكِّرةٍ تُقاس» — والقاعدةُ 1 من "
                    "`RISK_REGISTER.md § 2`: خطرٌ بلا إشارةٍ قلقٌ مكتوبٌ لا خطرٌ مُدارٌ.",
                )
            )
        report.records.append(
            Record(
                record_id=record_id,
                register=RISKS.as_posix(),
                line=line_no,
                is_open=True,
                open_basis="SECTION_DECLARES_OPEN",
                anchor=_anchor_of(guard_paths, due, owner_text),
                guard_paths=guard_paths,
                missing_paths=missing,
                due=due,
                declared_paths=declared,
                prose_paths=prose,
            )
        )

    for record in report.records:
        if record.missing_paths:
            report.violations.append(
                _v(
                    "DEAD_ANCHOR",
                    f"{record.record_id} ({record.register}:{record.line}): يذكرُ "
                    f"«{' · '.join(record.missing_paths)}» ولا وجودَ له في الشجرةِ — "
                    "مِرساةٌ مكتوبةٌ لا تحمِلُ شيئًا.",
                )
            )
        if not record.is_open:
            continue
        if record.anchor == ANCHOR_NONE:
            report.violations.append(
                _v(
                    "OPEN_RECORD_WITHOUT_ANCHOR",
                    f"{record.record_id} ({record.register}:{record.line}): قيدٌ "
                    "مفتوحٌ بلا حرسٍ مذكورٍ ولا تاريخِ استحقاقٍ ولا إعلانِ أنَّه "
                    "بيدِ المالكِ — فلا شيءَ يمنعُ اتِّساعَ عطبِه (`DISC-018`).",
                )
            )
        elif record.anchor == ANCHOR_OWNER_HELD:
            report.notes.append(
                _v(
                    "OWNER_HELD_WITHOUT_GUARD",
                    f"{record.record_id} ({record.register}:{record.line}): مُعلَنٌ "
                    "بيدِ المالكِ ولا حرسَ له — إبلاغٌ لا إسقاطٌ: لا فعلَ لمنفِّذٍ "
                    "فيه، وتاريخُ استحقاقِه قرارُ المالكِ لا اختراعُ عاملٍ.",
                )
            )
        elif (
            record.anchor == ANCHOR_DUE
            and record.due
            and date.fromisoformat(record.due) < now
        ):
            report.violations.append(
                _v(
                    "DUE_DATE_PASSED",
                    f"{record.record_id} ({record.register}:{record.line}): "
                    f"استحقاقُه {record.due} وقد مضى (اليومَ {now}) — "
                    "الاستحقاقُ الفائتُ ليس مِرساةً.",
                )
            )

    report.notes.append(
        _v(
            "ANCHOR_TALLY",
            f"صفوفٌ مقروءةٌ {len(report.records)} · مفتوحةٌ "
            f"{len(report.open_records)} · محروسةٌ {report.counted(ANCHOR_GUARD)} · "
            f"باستحقاقٍ {report.counted(ANCHOR_DUE)} · بيدِ المالكِ "
            f"{report.counted(ANCHOR_OWNER_HELD)} · بلا مِرساةٍ "
            f"{report.counted(ANCHOR_NONE)}.",
        )
    )
    return report


@dataclass
class DeclarationReport:
    """قياسُ **إعلانِ الحرسِ** وسقّاطتُه — طبقةٌ فوقَ القياسِ لا بديلٌ عنه."""

    measured_at: str
    prose_rows: list[str] = field(default_factory=list)
    declared_rows: list[str] = field(default_factory=list)
    baseline: int | None = None
    violations: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "measured_at": self.measured_at,
            "declared_markers": list(GUARD_DECLARATION_MARKERS),
            "baseline_rows": self.baseline,
            "prose_rows": self.prose_rows,
            "prose_count": len(self.prose_rows),
            "declared_rows": self.declared_rows,
            "declared_count": len(self.declared_rows),
            "violations": self.violations,
        }


def read_prose_baseline(root: Path) -> int:
    """الرقمُ المُعلَنُ في سجلِّ الاكتشافاتِ — مصدرُ حقيقةٍ واحدٌ لا ثابتٌ مدفونٌ."""
    text = _read(root, DISCOVERIES)
    matches = PROSE_BASELINE_RE.findall(text)
    if not matches:
        raise MeasurementRefused(
            "PROSE_BASELINE_MISSING",
            "لا سطرَ `ANCHOR_PROSE_BASELINE: rows=N` في "
            f"«{DISCOVERIES.as_posix()}» — وسقّاطةٌ بلا رقمٍ مُعلَنٍ لا تُقاسُ، "
            "ولا يُخترَعُ لها رقمٌ في شِفرةٍ.",
        )
    if len(set(matches)) > 1:
        raise MeasurementRefused(
            "PROSE_BASELINE_AMBIGUOUS",
            f"رقمُ السقّاطةِ مكتوبٌ بأكثرَ من قيمةٍ ({' · '.join(sorted(set(matches)))}) "
            "— مصدرانِ للحقيقةِ لا يُرجَّحُ أحدُهما بالظنِّ.",
        )
    return int(matches[0])


def measure_declarations(
    root: Path | None = None, today: date | None = None
) -> DeclarationReport:
    """صفوفٌ مفتوحةٌ تُقرأُ `GUARD` وحرسُها غيرُ مُعلَنٍ — تُعَدُّ وتُسمَّى وتُسقَّطُ."""
    root = root or REPO_ROOT
    base = measure(root, today)
    out = DeclarationReport(measured_at=base.measured_at)
    for record in base.open_records:
        if record.anchor != ANCHOR_GUARD:
            continue
        if record.declared_paths:
            out.declared_rows.append(record.record_id)
        else:
            out.prose_rows.append(record.record_id)
    out.baseline = read_prose_baseline(root)
    measured = len(out.prose_rows)
    if measured > out.baseline:
        out.violations.append(
            _v(
                "PROSE_ANCHOR_GROWTH",
                f"صفوفُ «مسارٌ في نثرٍ» مقيسةٌ {measured} والمُعلَنُ "
                f"{out.baseline} — ارتفعَ العددُ: صفٌّ جديدٌ اشترى `GUARD` بمرورِ "
                "مسارٍ في كلامِه، وذاك عينُ `DISC-021`. "
                f"الصفوفُ: {' · '.join(out.prose_rows)}",
            )
        )
    elif measured < out.baseline:
        out.violations.append(
            _v(
                "STALE_PROSE_BASELINE",
                f"صفوفُ «مسارٌ في نثرٍ» مقيسةٌ {measured} والمُعلَنُ "
                f"{out.baseline} — انخفضَ ولم يُخفَضِ المُعلَنُ، فلا تُترَكُ "
                "سقّاطةٌ رخوةً تسمحُ بعودةِ ما زالَ.",
            )
        )
    return out


def render_declarations(report: DeclarationReport) -> str:
    lines = [
        "[ANCHOR DECLARATION] الحرسُ يُقرأُ من إعلانٍ مُهيكَلٍ لا من مسارٍ في نثرٍ:",
        f"  مُعلَنٌ حرسُها: {len(report.declared_rows)} "
        f"({' · '.join(report.declared_rows) or '—'})",
        f"  مسارٌ في نثرٍ: {len(report.prose_rows)} · السقّاطةُ {report.baseline}",
        f"  الصفوفُ: {' · '.join(report.prose_rows) or '—'}",
    ]
    for violation in report.violations:
        lines.append(f"  ✗ {violation['kind']}: {violation['detail']}")
    if not report.violations:
        lines.append("  ✓ لا نموَّ في «مسارٍ في نثرٍ» — والرقمُ المُعلَنُ يُطابِقُ المقيسَ.")
    return "\n".join(lines)


def render(report: Report) -> str:
    lines = ["[OPEN RECORD] مساءلةُ القيودِ المفتوحةِ في سجلَّي الاكتشافِ والخطرِ:"]
    for record in report.records:
        if not record.is_open:
            continue
        guard = " · ".join(record.guard_paths) or record.due or "—"
        lines.append(
            f"  {record.record_id} ({record.register}:{record.line}): "
            f"{record.anchor} · {guard}"
        )
    for note in report.notes:
        lines.append(f"  ملاحظة · {note['kind']}: {note['detail']}")
    for violation in report.violations:
        lines.append(f"  ✗ {violation['kind']}: {violation['detail']}")
    if not report.violations:
        lines.append("  ✓ لا مخالفةَ مقيسةً: كلُّ قيدٍ مفتوحٍ له مِرساةُ مساءلةٍ.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="قياسُ مِرساةِ المساءلةِ لكلِّ قيدٍ مفتوحٍ (W-059 · DISC-018)."
    )
    parser.add_argument("--root", default=None, help="جذرُ استنساخٍ يُقاسُ بدلًا من هذا.")
    parser.add_argument("--json", action="store_true", help="طبعُ الحِملِ كاملًا JSON.")
    parser.add_argument(
        "--declaration-check",
        action="store_true",
        help="قياسُ إعلانِ الحرسِ وسقّاطتِه (`DISC-021`) — لا يُبدِّلُ القياسَ الأصليَّ.",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else REPO_ROOT
    if args.declaration_check:
        try:
            declarations = measure_declarations(root)
        except MeasurementRefused as refusal:
            print(
                f"[ANCHOR DECLARATION] رفضٌ · {refusal.kind}: {refusal.detail}",
                file=sys.stderr,
            )
            return 2
        if args.json:
            print(json.dumps(declarations.to_dict(), ensure_ascii=False, indent=2))
        else:
            print(render_declarations(declarations))
        return 1 if declarations.violations else 0

    try:
        report = measure(root)
    except MeasurementRefused as refusal:
        print(
            f"[OPEN RECORD] رفضٌ · {refusal.kind}: {refusal.detail}",
            file=sys.stderr,
        )
        return 2

    if args.json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(render(report))
    return 1 if report.violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
