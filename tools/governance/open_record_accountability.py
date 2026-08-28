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
تاريخ آخر تعديل: 2026-08-28

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


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


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
        if len(cells) < 8:
            report.violations.append(
                _v(
                    "MALFORMED_ROW",
                    f"{record_id}: صفُّ اكتشافٍ بـ{len(cells)} خليّةً — الإلزاميُّ "
                    "ثمانٍ، فلا تُقرأُ حالتُه ولا وجهتُه.",
                )
            )
            continue
        is_open, basis = _classify_open(cells[7])
        # مِرساةُ الاكتشافِ تُقرأُ من **الوجهةِ والحالةِ** لا من الصفِّ كلِّهِ:
        # ملفٌّ يُذكَرُ في خليّةِ الدليلِ موضِعُ عَطبٍ لا حارِسٌ له.
        anchor_text = f"{cells[6]} {cells[7]}"
        owner_text = anchor_text
        guard_paths, missing = _paths_in(root, anchor_text)
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
            )
        )

    for line_no, record_id, line in risk_rows:
        cells = _cells(line)
        if len(cells) < 8:
            report.violations.append(
                _v(
                    "MALFORMED_ROW",
                    f"{record_id}: صفُّ خطرٍ بـ{len(cells)} خليّةً — الإلزاميُّ "
                    "ثمانٍ، فلا تُقرأُ إشارتُه المبكِّرةُ ولا مالكُه.",
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
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else REPO_ROOT
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
