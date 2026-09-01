#!/usr/bin/env python3
"""انحرافُ وثائقِ الحالةِ عن سجلِّ الإكمالِ — رقمٌ يُقاسُ لا انطباعٌ يُقرَأُ (W-057).

الهدف:
    أن تكونَ دعوى «أينَ يقفُ المشروعُ» في وثائقِ الحالةِ **مقيسةً مقابلَ سجلِّ
    الإكمالِ**: كلُّ وثيقةٍ تُعلِنُ آخرَ عملٍ أو تُحيلُ إلى مدى القيودِ تُقابَلُ
    بأعلى قيدٍ مكتوبٍ في § 8، فيُعرَفُ التأخُّرُ بعددِه لا بالظنِّ.
النطاق:
    وثائقُ الحالةِ المُعلَنةُ في `STATE_DOCUMENTS` وحدَها، وسجلُّ الإكمالِ § 8.
    لا شبكةَ ولا قاعدةَ ولا سرَّ. لا تكتبُ الأداةُ في أيِّ وثيقةٍ تحكمُ عليها.
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-09-01

لماذا أداةٌ لا فقرةٌ:
    وقِيدَ في `DISC-031` أنَّ «أقصى ذكرٍ» وحدَه يُخضِرُّ على وثيقةٍ تكذبُ: حقلُ
    «Last Completed Work» بقيَ عندَ `W-057` والسجلُّ عندَ `W-064` — **تأخُّرُ
    ثمانيةِ قيودٍ** مرَّ لأنَّ ذكرَ الأحدثِ في ترويسةِ التاريخِ أرضى القياسَ. فما
    يُصلِحُه أن يُقرَأَ **موضعُ الدعوى** لا أيُّ ذكرٍ في الملفِّ (`W-090`).

    قِيدَ في `DISC-013` أنَّ `PROJECT_STATE.md` تقولُ «آخرُ عملٍ W-047» والسجلُّ
    فيه `W-053` مدموجًا — أي قارئٌ يبدأُ من وثيقةِ الحالةِ يقرأُ ماضيًا حالةً.
    والقيدُ وحدَه لا يمنعُ تكرارَ الانحرافِ: بقيَ مفتوحًا ثلاثةَ قيودٍ أُخرى
    فاتّسعَ الفارقُ من ستّةٍ إلى تسعةٍ. فما يُصلِحُ هذا ليس تصحيحًا يدويًّا
    يتقادَمُ بعدَ أوّلِ دمجٍ، بل قياسٌ يسقُطُ حينَ يتقادَمُ.

الحدُّ المُعلَنُ — لا مطويٌّ:
    * تقيسُ الأداةُ **أحدثَ قيدٍ تذكرُه الوثيقةُ** ومدى تأخُّرِه، لا صدقَ نصِّها:
      وثيقةٌ تذكرُ `W-056` وتكذبُ في وصفِه تمرُّ من هذا الحرسِ. صدقُ الوصفِ
      واجبُ من يكتبُ، وحرسُه مراجعةٌ بشريّةٌ لا مُطابَقةُ نصٍّ.
    * قائمةُ وثائقِ الحالةِ **مُعلَنةٌ في الشِفرةِ** لا مُكتشَفةٌ: وثيقةٌ جديدةٌ
      تُعلِنُ حالةً ولا تُضافُ هنا لا يراها هذا الحرسُ.
    * **ومِرساةُ الحقلِ مُعلَنةٌ كذلك** (`W-090`): تقيسُ الأداةُ — فوقَ أقصى ذكرٍ —
      **القيدَ في الحقلِ الذي تُعلِنُه الوثيقةُ حالةً** بمِرساةٍ مكتوبةٍ في
      `STATE_FIELD_ANCHORS`. ووثيقةٌ تُعلِنُ حالتَها في حقلٍ لم يُسمَّ هنا لا
      يراها هذا الوجهُ، **وغيابُ المِرساةِ المُسمّاةِ من الوثيقةِ مخالفةٌ
      مُصنَّفةٌ** لا سكوتٌ: حقلٌ يُعادُ تسميتُه يُسقِطُ الحرسَ ولا يُسكِتُه.
    * لا تكتبُ الأداةُ سطرًا في وثيقةٍ ولا في السجلِّ: بوّابةٌ تُصلِحُ ما تحكمُ
      عليه لا تُثبِتُ شيئًا (سابقةُ `W-037`/`W-038`).

الاستعمال:
    python tools/governance/state_document_drift.py
    python tools/governance/state_document_drift.py --json
    python tools/governance/state_document_drift.py --root /مسار/استنساخٍ

رموزُ الخروج:
    0 = لا مخالفةَ · 1 = مخالفةٌ مقيسةٌ · 2 = **رفضٌ مُصنَّفٌ** (القياسُ لم يُجرَ)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import UTC, date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

LEDGER = Path("docs/audit/COMPLETION_LEDGER.md")

#: وثائقُ الحالةِ المُعلَنةُ — قائمةٌ مكتوبةٌ لا مُكتشَفةٌ (حدٌّ مُعلَنٌ أعلاه).
STATE_DOCUMENTS = (
    Path("PROJECT_STATE.md"),
    Path("docs/PROJECT_HANDBOOK.md"),
)

#: مِرساةُ الحقلِ الذي تُعلِنُه الوثيقةُ حالةً — مكتوبةٌ لا مُكتشَفةٌ (`DISC-031`).
STATE_FIELD_ANCHORS: dict[Path, tuple[str, str]] = {
    Path("PROJECT_STATE.md"): (
        "Last Completed Work",
        r"\|\s*\*\*Last Completed Work\*\*\s*\|(?P<value>.*)",
    ),
    Path("docs/PROJECT_HANDBOOK.md"): (
        "تاريخ آخر تعديل",
        r"تاريخ آخر تعديل:(?P<value>.*)",
    ),
}

WORK_RE = re.compile(r"\bW-(\d{3})\b")
LEDGER_ROW_RE = re.compile(
    r"^\|\s*W-(\d{3})\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", re.MULTILINE
)
LAST_MODIFIED_RE = re.compile(r"تاريخ آخر تعديل:\s*(\d{4}-\d{2}-\d{2})")


class MeasurementRefused(Exception):
    """عجزٌ عن القياسِ يُعلَنُ مُصنَّفًا — لا يُبتلَعُ فيُقرأَ نظافةً."""

    def __init__(self, kind: str, detail: str) -> None:
        super().__init__(f"{kind}: {detail}")
        self.kind = kind
        self.detail = detail


@dataclass(frozen=True)
class DocState:
    """ما تُعلِنُه وثيقةُ حالةٍ واحدةٌ عن موضعِها من الطريق."""

    path: str
    newest_work: str | None
    newest_work_line: int | None
    declared_date: str | None
    mentions: int
    #: اسمُ الحقلِ المُعلَنِ حالةً كما سُمِّيَ في `STATE_FIELD_ANCHORS` (أو `None`).
    declared_field: str | None = None
    #: هل وُجِدَ الحقلُ المُسمّى في نصِّ الوثيقةِ فعلًا.
    declared_field_found: bool = False
    #: أحدثُ قيدٍ **داخلَ** الحقلِ المُعلَنِ وحدَه.
    declared_field_work: str | None = None
    declared_field_line: int | None = None


@dataclass
class Report:
    """ما قِيسَ في تشغيلةٍ واحدةٍ — يُطبَعُ نصًّا أو JSON."""

    measured_at: str
    ledger_newest_work: str
    ledger_newest_date: str
    ledger_rows: int
    documents: list[DocState] = field(default_factory=list)
    violations: list[dict[str, str]] = field(default_factory=list)
    notes: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "measured_at": self.measured_at,
            "ledger_newest_work": self.ledger_newest_work,
            "ledger_newest_date": self.ledger_newest_date,
            "ledger_rows": self.ledger_rows,
            "declared_documents": [d.as_posix() for d in STATE_DOCUMENTS],
            "declared_field_anchors": {
                path.as_posix(): label
                for path, (label, _pattern) in STATE_FIELD_ANCHORS.items()
            },
            "documents": [asdict(d) for d in self.documents],
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
            "ولا يُقالُ «لا انحراف» عن ملفٍّ لم يُقرَأْ.",
        )
    return target.read_text(encoding="utf-8")


def ledger_entries(text: str) -> dict[str, str]:
    """قيودُ § 8: المعرِّفُ ← تاريخُه، كما هي مكتوبةٌ في الصفوف.

    Raises:
        MeasurementRefused: إن لم يُقرَأْ صفٌّ واحدٌ — جدولٌ بلا صفوفٍ لا يُقاسُ عليه.
    """
    rows = {f"W-{num}": on_date for num, on_date in LEDGER_ROW_RE.findall(text)}
    if not rows:
        raise MeasurementRefused(
            "NO_LEDGER_ROWS",
            "لم يُقرَأْ صفُّ قيدٍ واحدٌ في سجلِّ الإكمالِ — إمّا تغيَّرَ شكلُ الجدولِ "
            "وإمّا قُرِئَ ملفٌّ آخرُ، وكلاهما يمنعُ القياسَ.",
        )
    return rows


def newest(ids: list[str] | set[str]) -> str | None:
    """أحدثُ معرِّفٍ بالعددِ لا بترتيبِ الظهورِ — الجدولُ لا يُفترَضُ مرتَّبًا."""
    numbered = sorted(ids, key=lambda w: int(w.split("-")[1]))
    return numbered[-1] if numbered else None


def _declared_field(rel: Path, text: str) -> tuple[str | None, str | None, int | None]:
    """الحقلُ الذي تُعلِنُه الوثيقةُ حالةً: اسمُه · أحدثُ قيدٍ فيه · سطرُه.

    تُقرَأُ المِرساةُ من `STATE_FIELD_ANCHORS` وحدَها — فلا يُخلَطُ ذكرٌ عارضٌ في
    نصٍّ حرٍّ بدعوى الوثيقةِ عن موضعِها (`DISC-031`).
    """
    anchor = STATE_FIELD_ANCHORS.get(rel)
    if anchor is None:
        return None, None, None
    label, pattern = anchor
    compiled = re.compile(pattern)
    for number, line in enumerate(text.splitlines(), start=1):
        found = compiled.search(line)
        if found is None:
            continue
        ids = [f"W-{hit.group(1)}" for hit in WORK_RE.finditer(found.group("value"))]
        return label, newest(ids), number
    return label, None, None


def read_document(root: Path, rel: Path) -> DocState:
    """ما تُعلِنُه وثيقةٌ واحدةٌ: أحدثُ قيدٍ تذكرُه · تاريخُها · عددُ الذِّكرِ."""
    text = _read(root, rel)
    found: dict[str, int] = {}
    for number, line in enumerate(text.splitlines(), start=1):
        for hit in WORK_RE.finditer(line):
            found.setdefault(f"W-{hit.group(1)}", number)
    top = newest(list(found))
    stamp = LAST_MODIFIED_RE.search(text)
    label, field_work, field_line = _declared_field(rel, text)
    return DocState(
        path=rel.as_posix(),
        newest_work=top,
        newest_work_line=found.get(top) if top else None,
        declared_date=stamp.group(1) if stamp else None,
        mentions=len(found),
        declared_field=label,
        declared_field_found=field_line is not None,
        declared_field_work=field_work,
        declared_field_line=field_line,
    )


def measure(root: Path | None = None, today: date | None = None) -> Report:
    """القياسُ كلُّه في دالّةٍ واحدةٍ تُستدعى من فحصٍ كما تُستدعى من سطرِ أمر."""
    root = root or REPO_ROOT
    now = today or datetime.now(UTC).date()
    rows = ledger_entries(_read(root, LEDGER))
    top = newest(list(rows))
    assert top is not None  # `ledger_entries` يرفضُ الجدولَ الخالي قبلَ هذا السطر
    report = Report(
        measured_at=datetime.now(UTC).isoformat(timespec="seconds"),
        ledger_newest_work=top,
        ledger_newest_date=rows[top],
        ledger_rows=len(rows),
    )
    top_number = int(top.split("-")[1])

    for rel in STATE_DOCUMENTS:
        doc = read_document(root, rel)
        report.documents.append(doc)

        if doc.newest_work is None:
            report.violations.append(
                _v(
                    "STATE_DOC_CITES_NO_WORK",
                    f"«{doc.path}» لا تذكرُ قيدًا واحدًا من § 8 — وثيقةُ حالةٍ لا "
                    "تُحالُ إلى قيدٍ لا يُقاسُ موضعُها من الطريق.",
                )
            )
        else:
            unknown = doc.newest_work not in rows
            gap = top_number - int(doc.newest_work.split("-")[1])
            if unknown:
                report.violations.append(
                    _v(
                        "STATE_DOC_CITES_UNKNOWN_WORK",
                        f"«{doc.path}:{doc.newest_work_line}» تذكرُ «{doc.newest_work}» "
                        "ولا صفَّ له في § 8 — دعوى عملٍ غيرِ مقيَّدٍ.",
                    )
                )
            elif gap > 0:
                report.violations.append(
                    _v(
                        "STATE_DOC_BEHIND",
                        f"«{doc.path}» أحدثُ ما تذكرُه «{doc.newest_work}» "
                        f"(السطرُ {doc.newest_work_line}) وأحدثُ قيدٍ في § 8 «{top}» — "
                        f"متأخِّرةٌ **{gap} قيدًا**، فمن يبدأُ منها يقرأُ ماضيًا حالةً.",
                    )
                )

        if doc.declared_field is None:
            report.notes.append(
                _v(
                    "NO_DECLARED_FIELD_ANCHOR",
                    f"«{doc.path}» لا مِرساةَ حقلٍ مُسمّاةً لها في "
                    "`STATE_FIELD_ANCHORS` — فلا يُقاسُ فيها إلَّا أقصى ذكرٍ، "
                    "وهذا حدٌّ مُعلَنٌ لا سكوتٌ.",
                )
            )
        elif not doc.declared_field_found:
            report.violations.append(
                _v(
                    "STATE_DOC_FIELD_ANCHOR_MISSING",
                    f"«{doc.path}» لا تحوي حقلَها المُعلَنَ «{doc.declared_field}» — "
                    "والمِرساةُ إن غابَت لم يُقرَأْ موضعُ الدعوى، فلا يُقالُ «لا "
                    "انحراف» عن حقلٍ لم يُوجَدْ.",
                )
            )
        elif doc.declared_field_work is None:
            report.violations.append(
                _v(
                    "STATE_DOC_FIELD_CITES_NO_WORK",
                    f"«{doc.path}:{doc.declared_field_line}» حقلُها المُعلَنُ "
                    f"«{doc.declared_field}» لا يذكرُ قيدًا واحدًا — حقلُ حالةٍ بلا "
                    "إحالةٍ لا يُقاسُ موضعُه من الطريق.",
                )
            )
        elif doc.declared_field_work not in rows:
            report.violations.append(
                _v(
                    "STATE_DOC_FIELD_CITES_UNKNOWN_WORK",
                    f"«{doc.path}:{doc.declared_field_line}» حقلُها المُعلَنُ "
                    f"«{doc.declared_field}» يذكرُ «{doc.declared_field_work}» ولا صفَّ "
                    "له في § 8 — دعوى عملٍ غيرِ مقيَّدٍ في موضعِ الحالةِ نفسِه.",
                )
            )
        else:
            field_gap = top_number - int(doc.declared_field_work.split("-")[1])
            if field_gap > 0:
                report.violations.append(
                    _v(
                        "STATE_DOC_FIELD_BEHIND",
                        f"«{doc.path}:{doc.declared_field_line}» حقلُها المُعلَنُ "
                        f"«{doc.declared_field}» يقولُ «{doc.declared_field_work}» "
                        f"وأحدثُ قيدٍ في § 8 «{top}» — **{field_gap} قيدًا** تأخُّرًا "
                        "في موضعِ الدعوى نفسِه، ولو ذُكِرَ الأحدثُ في مكانٍ آخرَ من "
                        "الوثيقةِ.",
                    )
                )

        if doc.declared_date is None:
            report.violations.append(
                _v(
                    "STATE_DOC_UNDECLARED_DATE",
                    f"«{doc.path}» بلا «تاريخ آخر تعديل» — وثيقةٌ لا يُعرَفُ عُمرُها "
                    "تُقرأُ حاضرةً أبدًا.",
                )
            )
        else:
            declared = date.fromisoformat(doc.declared_date)
            if declared > now:
                report.violations.append(
                    _v(
                        "STATE_DOC_DATE_IN_FUTURE",
                        f"«{doc.path}» تُعلِنُ تعديلَها في {doc.declared_date} وهو بعدَ "
                        f"اليومِ ({now}) — تاريخٌ لم يقعْ يُعلَنُ واقعًا.",
                    )
                )
            elif doc.newest_work == top and declared < date.fromisoformat(rows[top]):
                report.notes.append(
                    _v(
                        "DATE_OLDER_THAN_LATEST_ENTRY",
                        f"«{doc.path}» تذكرُ أحدثَ قيدٍ «{top}» وتاريخُها المُعلَنُ "
                        f"{doc.declared_date} أقدمُ من تاريخِ القيدِ {rows[top]} — "
                        "إبلاغٌ لا إسقاطٌ: قد يكونُ النصُّ صحيحًا وتاريخُه ناقصًا.",
                    )
                )

    behind = [v for v in report.violations if v["kind"] == "STATE_DOC_BEHIND"]
    field_behind = [
        v for v in report.violations if v["kind"] == "STATE_DOC_FIELD_BEHIND"
    ]
    report.notes.append(
        _v(
            "LEDGER_HEAD",
            f"أحدثُ قيدٍ مقروءٍ في § 8: {top} ({rows[top]}) · وعددُ الصفوفِ "
            f"{len(rows)} · ووثائقُ الحالةِ المُعلَنةُ {len(STATE_DOCUMENTS)} "
            f"منها {len(behind)} متأخِّرةٌ · وحقولٌ مُعلَنةٌ متأخِّرةٌ "
            f"{len(field_behind)}.",
        )
    )
    return report


def render(report: Report) -> str:
    lines = ["[STATE DRIFT] موضعُ وثائقِ الحالةِ من سجلِّ الإكمالِ:"]
    lines.append(
        f"  أحدثُ قيدٍ في § 8: {report.ledger_newest_work} "
        f"({report.ledger_newest_date}) · صفوفٌ: {report.ledger_rows}"
    )
    for doc in report.documents:
        lines.append(
            f"  {doc.path}: أحدثُ قيدٍ مذكورٍ {doc.newest_work or '—'} · "
            f"تاريخٌ مُعلَنٌ {doc.declared_date or '—'} · قيودٌ مذكورةٌ {doc.mentions}"
        )
        lines.append(
            f"    الحقلُ المُعلَنُ حالةً: {doc.declared_field or '— (لا مِرساةَ)'} · "
            f"قيدُه {doc.declared_field_work or '—'} · "
            f"السطرُ {doc.declared_field_line or '—'}"
        )
    for note in report.notes:
        lines.append(f"  ملاحظة · {note['kind']}: {note['detail']}")
    for violation in report.violations:
        lines.append(f"  ✗ {violation['kind']}: {violation['detail']}")
    if not report.violations:
        lines.append("  ✓ لا انحرافَ مقيسًا: كلُّ وثيقةِ حالةٍ تذكرُ أحدثَ قيدٍ.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="قياسُ انحرافِ وثائقِ الحالةِ عن سجلِّ الإكمالِ (W-057)."
    )
    parser.add_argument("--root", default=None, help="جذرُ استنساخٍ يُقاسُ بدلًا من هذا.")
    parser.add_argument("--json", action="store_true", help="طبعُ الحِملِ كاملًا JSON.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else REPO_ROOT
    try:
        report = measure(root)
    except MeasurementRefused as refusal:
        print(f"[STATE DRIFT] رفضٌ · {refusal.kind}: {refusal.detail}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(render(report))
    return 1 if report.violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
