#!/usr/bin/env python3
"""اتِّجاهُ دَينِ الأسطحِ بينَ قيدَينِ متتاليَينِ — إشارةُ `RK-003` تصيرُ رقمًا (W-061).

الهدف:
    أن يكونَ الخطرُ المُقيَّدُ في `RK-003` — «دَينُ الأسطحِ غيرِ السياديّةِ يتجاوزُ
    قدرةَ المعالجةِ التدريجيّة» — **محروسًا بقياسٍ** لا موصوفًا بنثرٍ: تُقاسُ
    الأسطحُ عندَ القيدِ الأحدثِ وعندَ الذي قبلَه **بالقاعدةِ الواحدةِ نفسِها**،
    فيُعرَفُ اتِّجاهُ العَدِّ صعودًا أو هبوطًا أو ثباتًا برقمٍ يُعادُ بأمرٍ واحدٍ.
النطاق:
    سجلُّ الإكمالِ § 8 (مصدرُ القيودِ) · تاريخُ `git` (مصدرُ اللقطاتِ) · وجردُ
    الكتاباتِ `tools/audit/sovereign_write_inventory.py` (مصدرُ القاعدةِ). لا شبكةَ
    ولا قاعدةَ بياناتٍ ولا سرَّ. ولا تكتبُ الأداةُ سطرًا في وثيقةٍ تحكمُ عليها.
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-29
تاريخ آخر تعديل: 2026-08-29

لماذا أداةٌ لا فقرةٌ:
    قِيسَ في `W-060` أنَّ `RK-003` **آخرُ قيدٍ مفتوحٍ بلا مِرساةٍ** في السجلَّينِ:
    قارئا جردِ الأسطحِ في الشجرةِ اثنانِ (أداةُ التدقيقِ النهائيِّ وحرسُ بصمةِ
    التاريخِ) وكلاهما يقرأُ الجردَ **ولا يقيسُ اتِّجاهَ عدِّه بينَ قيدَينِ**. وإشارةُ
    خطرٍ لا يقيسُها شيءٌ إشارةٌ لا تُشعِلُ: يتَّسِعُ الدَّينُ قيدًا بعدَ قيدٍ ولا
    يعترضُه سطرٌ، كما اتَّسَعَ `DISC-013` من ستّةٍ إلى تسعةٍ وهو «مفتوحٌ»
    (`DISC-018`). فهذه الأداةُ تُنشئُ للإشارةِ حرسًا يسقُطُ عندَ الصعود.

القاعدةُ المُلزِمةُ في القياس — القاعدةُ الواحدةُ:
    تُقاسُ اللقطتانِ كلتاهما بـ**قاعدةِ الشجرةِ الحاضرةِ** (وحدةُ الجردِ كما هي
    اليومَ)، لا بقاعدةِ كلِّ لقطةٍ في زمنِها. ولو قِيسَت كلُّ لقطةٍ بأداتِها
    لكانَ الفارقُ المُعلَنُ **فارقَ أداتَينِ لا فارقَ دَينٍ** — وذاك أخطرُ من
    غيابِ القياسِ لأنَّه يُقرأُ إصلاحًا.

الحدُّ المُعلَنُ — لا مطويٌّ:
    * تقيسُ الأداةُ **مواضعَ الكتابةِ في المصدرِ** كما يعُدُّها الجردُ، لا عددَ
      الكتاباتِ في التشغيلِ، ولا **خطورةَ** سطحٍ: سطحٌ يُضافُ وسطحٌ يُهاجَرُ في
      قيدٍ واحدٍ يتعادلانِ في هذا العدَّادِ ويمرّانِ. فالثباتُ هنا ليس شهادةَ
      سكونٍ، بل شهادةُ **صافٍ** لا يصعدُ.
    * لا تحكمُ على **وجوبِ** هجرةِ سطحٍ: ذاك حكمٌ دستوريٌّ في سجلِّ القرارات.
    * تلزمُها **لقطتانِ من تاريخِ `git`**: في استنساخٍ ضحلٍ أو بلا تاريخٍ
      يُعلَنُ **رفضٌ مُصنَّفٌ** (خروجٌ 2) ولا يُقالُ «لا صعود».
    * القيدُ يُنسَبُ إلى **أوّلِ التزامٍ أدخلَ صفَّه** في § 8؛ فقيدٌ كُتِبَ صفُّه
      ثمَّ أُعيدَت صياغتُه لاحقًا يُقاسُ عندَ إدخالِه الأوّلِ لا عندَ صياغتِه.
    * تقيسُ الأداةُ الشجرةَ المُلتَقَطةَ من `git` لا شجرةَ العملِ: تغييرٌ غيرُ
      مُلتَزَمٍ لا يراهُ هذا الحرسُ (ويراهُ الجردُ نفسُه بأمرِه المباشر).

الاستعمال:
    python tools/governance/surface_debt_trend.py
    python tools/governance/surface_debt_trend.py --json
    python tools/governance/surface_debt_trend.py --entries 4
    python tools/governance/surface_debt_trend.py --root /مسار/استنساخٍ

رموزُ الخروج:
    0 = لا صعودَ مقيسًا · 1 = مخالفةٌ مقيسةٌ · 2 = **رفضٌ مُصنَّفٌ** (القياسُ لم يُجرَ)
"""

from __future__ import annotations

import argparse
import importlib.util
import io
import json
import re
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType

REPO_ROOT = Path(__file__).resolve().parents[2]

LEDGER = Path("docs/audit/COMPLETION_LEDGER.md")

#: أداةُ الجردِ — مصدرُ **القاعدةِ** الواحدةِ التي تُقاسُ بها كلُّ لقطةٍ.
INVENTORY_TOOL = Path("tools/audit/sovereign_write_inventory.py")

#: الحِملُ المنشورُ للجردِ — يُقابَلُ بالمقيسِ حيًّا فلا يُقرأُ متقادِمًا حاضرًا.
PUBLISHED_INVENTORY = Path("docs/audit/measurements/write_inventory_p13.json")

#: مفتاحُ الدَّينِ في مُلخَّصِ الجردِ — قاعدةُ العدِّ المُعلَنةُ في وثيقةِ الأسطح.
DEBT_KEY = "non_sovereign_write_operations"

#: عددُ الأسطحِ كلِّها — يُعلَنُ إبلاغًا بجانبِ الدَّين.
TOTAL_KEY = "write_sites_total"

LEDGER_ROW_RE = re.compile(
    r"^\|\s*W-(\d{3})\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", re.MULTILINE
)


class MeasurementRefused(Exception):
    """عجزٌ عن القياسِ يُعلَنُ مُصنَّفًا — لا يُبتلَعُ فيُقرأَ نظافةً."""

    def __init__(self, kind: str, detail: str) -> None:
        super().__init__(f"{kind}: {detail}")
        self.kind = kind
        self.detail = detail


@dataclass(frozen=True)
class Snapshot:
    """ما قِيسَ عندَ قيدٍ واحدٍ: التزامُه وتاريخُه وعدداهُ."""

    work: str
    entry_date: str
    commit: str
    total_sites: int
    debt_sites: int


@dataclass
class Report:
    """ما قِيسَ في تشغيلةٍ واحدةٍ — يُطبَعُ نصًّا أو JSON."""

    measured_at: str
    rule_source: str
    ledger_rows: int
    snapshots: list[Snapshot] = field(default_factory=list)
    steps: list[dict[str, object]] = field(default_factory=list)
    violations: list[dict[str, str]] = field(default_factory=list)
    notes: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "measured_at": self.measured_at,
            "rule_source": self.rule_source,
            "debt_key": DEBT_KEY,
            "ledger_rows": self.ledger_rows,
            "snapshots": [asdict(s) for s in self.snapshots],
            "steps": self.steps,
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
            "ولا يُقالُ «لا صعودَ» عن ملفٍّ لم يُقرَأْ.",
        )
    return target.read_text(encoding="utf-8")


def _git(root: Path, *args: str) -> str:
    """نداءُ `git` في جذرٍ مُعطًى — وفشلُه يُعلَنُ رفضًا لا يُبتلَعُ."""
    try:
        done = subprocess.run(
            ["git", *args],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as failure:
        raise MeasurementRefused(
            "GIT_UNAVAILABLE",
            f"لم يُنفَّذْ `git {' '.join(args)}` تحتَ «{root}»: {failure} — "
            "وبلا تاريخٍ لا يُقاسُ اتِّجاهٌ.",
        ) from failure
    if done.returncode != 0:
        raise MeasurementRefused(
            "GIT_FAILED",
            f"`git {' '.join(args)}` خرجَ بـ{done.returncode}: "
            f"{done.stderr.strip()[:200]} — القياسُ لم يُجرَ.",
        )
    return done.stdout


def load_inventory_rule(root: Path) -> ModuleType:
    """تحميلُ وحدةِ الجردِ من الشجرةِ الحاضرةِ — قاعدةٌ واحدةٌ لكلِّ اللقطات."""
    tool = REPO_ROOT / INVENTORY_TOOL
    if not tool.is_file():
        raise MeasurementRefused(
            "RULE_SOURCE_MISSING",
            f"وحدةُ الجردِ «{INVENTORY_TOOL.as_posix()}» غيرُ موجودةٍ — "
            "ولا يُقاسُ اتِّجاهٌ بلا قاعدةِ عَدٍّ واحدةٍ.",
        )
    spec = importlib.util.spec_from_file_location("_swi_rule", tool)
    if spec is None or spec.loader is None:
        raise MeasurementRefused(
            "RULE_SOURCE_UNLOADABLE",
            f"لم تُحمَّلْ وحدةُ الجردِ «{INVENTORY_TOOL.as_posix()}» — القياسُ لم يُجرَ.",
        )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    for needed in ("collect", "summarize"):
        if not hasattr(module, needed):
            raise MeasurementRefused(
                "RULE_CONTRACT_BROKEN",
                f"وحدةُ الجردِ بلا «{needed}» — تغيَّرَ عقدُها فلا يُقاسُ بها.",
            )
    return module


def ledger_entries(text: str) -> dict[str, str]:
    """قيودُ § 8: المعرِّفُ ← تاريخُه، كما هي مكتوبةٌ في الصفوف."""
    rows = {f"W-{num}": on_date for num, on_date in LEDGER_ROW_RE.findall(text)}
    if not rows:
        raise MeasurementRefused(
            "NO_LEDGER_ROWS",
            "لم يُقرَأْ صفُّ قيدٍ واحدٌ في سجلِّ الإكمالِ — إمّا تغيَّرَ شكلُ الجدولِ "
            "وإمّا قُرِئَ ملفٌّ آخرُ، وكلاهما يمنعُ القياسَ.",
        )
    return rows


def newest_entries(rows: dict[str, str], count: int) -> list[str]:
    """أحدثُ القيودِ بالعددِ لا بترتيبِ الظهورِ — الجدولُ لا يُفترَضُ مرتَّبًا."""
    if count < 2:
        raise MeasurementRefused(
            "TOO_FEW_POINTS",
            f"طُلِبَ قياسُ {count} قيدٍ — والاتِّجاهُ لا يُقاسُ بأقلَّ من نقطتَينِ.",
        )
    ordered = sorted(rows, key=lambda w: int(w.split("-")[1]))
    if len(ordered) < count:
        raise MeasurementRefused(
            "TOO_FEW_LEDGER_ROWS",
            f"في § 8 {len(ordered)} قيدًا والمطلوبُ {count} — "
            "ولا يُخترَعُ قيدٌ ليُقاسَ عليه اتِّجاهٌ.",
        )
    return ordered[-count:]


def entry_commit(root: Path, work: str) -> str:
    """أوّلُ التزامٍ أدخلَ صفَّ القيدِ في § 8 — حدٌّ مُعلَنٌ في ترويسةِ الملفِّ."""
    out = _git(
        root,
        "log",
        "--reverse",
        "--format=%H",
        f"-S| {work} |",
        "--",
        LEDGER.as_posix(),
    )
    commits = [line.strip() for line in out.splitlines() if line.strip()]
    if not commits:
        raise MeasurementRefused(
            "ENTRY_COMMIT_NOT_FOUND",
            f"لم يُوجَدْ في تاريخِ «{LEDGER.as_posix()}» التزامٌ أدخلَ صفَّ «{work}» — "
            "إمّا الاستنساخُ ضحلٌ وإمّا الصفُّ لم يُدفَعْ بعدُ؛ وكلاهما يمنعُ القياسَ.",
        )
    return commits[0]


def count_at(root: Path, commit: str, rule: ModuleType) -> tuple[int, int]:
    """عدَّا اللقطةِ عندَ التزامٍ: الأسطحُ كلُّها · ودَينُها غيرُ السياديّ."""
    payload = subprocess.run(
        ["git", "archive", commit],
        cwd=root,
        capture_output=True,
        check=False,
    )
    if payload.returncode != 0:
        raise MeasurementRefused(
            "SNAPSHOT_FAILED",
            f"`git archive {commit[:12]}` خرجَ بـ{payload.returncode}: "
            f"{payload.stderr.decode('utf-8', 'replace').strip()[:160]}",
        )
    with tempfile.TemporaryDirectory(prefix="surface_trend_") as workspace:
        with tarfile.open(fileobj=io.BytesIO(payload.stdout)) as bundle:
            bundle.extractall(workspace, filter="data")
        summary = rule.summarize(rule.collect(Path(workspace)))
    for key in (TOTAL_KEY, DEBT_KEY):
        if key not in summary:
            raise MeasurementRefused(
                "SUMMARY_CONTRACT_BROKEN",
                f"مُلخَّصُ الجردِ بلا «{key}» — تغيَّرَ عقدُ العَدِّ فلا يُقاسُ اتِّجاهٌ.",
            )
    return int(summary[TOTAL_KEY]), int(summary[DEBT_KEY])


def published_debt(root: Path) -> int | None:
    """دَينُ الحِملِ المنشورِ — أو `None` إن لم يُنشَرْ حِملٌ يُقابَلُ به."""
    target = root / PUBLISHED_INVENTORY
    if not target.is_file():
        return None
    try:
        payload = json.loads(target.read_text(encoding="utf-8"))
        value = payload["summary"][DEBT_KEY]
    except (json.JSONDecodeError, KeyError, TypeError) as failure:
        raise MeasurementRefused(
            "PUBLISHED_INVENTORY_UNREADABLE",
            f"«{PUBLISHED_INVENTORY.as_posix()}» لا يُقرأُ منه «{DEBT_KEY}»: "
            f"{failure} — وحِملٌ منشورٌ لا يُقرأُ لا يُقابَلُ به مقيسٌ.",
        ) from failure
    return int(value)


def measure(root: Path | None = None, entries: int = 2) -> Report:
    """القياسُ كلُّه في دالّةٍ واحدةٍ تُستدعى من فحصٍ كما تُستدعى من سطرِ أمر."""
    root = root or REPO_ROOT
    rows = ledger_entries(_read(root, LEDGER))
    wanted = newest_entries(rows, entries)
    rule = load_inventory_rule(root)

    report = Report(
        measured_at=datetime.now(UTC).isoformat(timespec="seconds"),
        rule_source=INVENTORY_TOOL.as_posix(),
        ledger_rows=len(rows),
    )

    for work in wanted:
        commit = entry_commit(root, work)
        total, debt = count_at(root, commit, rule)
        report.snapshots.append(
            Snapshot(
                work=work,
                entry_date=rows[work],
                commit=commit,
                total_sites=total,
                debt_sites=debt,
            )
        )

    for older, newer in zip(report.snapshots, report.snapshots[1:], strict=False):
        delta = newer.debt_sites - older.debt_sites
        total_delta = newer.total_sites - older.total_sites
        report.steps.append(
            {
                "from": older.work,
                "to": newer.work,
                "debt_delta": delta,
                "total_delta": total_delta,
            }
        )
        if delta > 0:
            report.violations.append(
                _v(
                    "SURFACE_DEBT_RISING",
                    f"دَينُ الأسطحِ صعِدَ بينَ «{older.work}» و«{newer.work}»: "
                    f"{older.debt_sites} ← {newer.debt_sites} (+{delta}) — "
                    "وإشارةُ `RK-003` هي هذا الصعودُ بعينِه: يُوقَفُ توسيعُ السطحِ "
                    "ويُدخَلُ كلُّ سطحٍ جديدٍ بندًا مُقيَّدًا.",
                )
            )
        elif total_delta > 0:
            report.notes.append(
                _v(
                    "TOTAL_SITES_ROSE_DEBT_DID_NOT",
                    f"أسطحُ «{newer.work}» كلُّها أكثرُ من «{older.work}» بـ"
                    f"{total_delta} والدَّينُ لم يصعَدْ ({newer.debt_sites}) — "
                    "إبلاغٌ لا إسقاطٌ: كتابةٌ أُضيفَت داخلَ الحدِّ السياديِّ.",
                )
            )

    newest_point = report.snapshots[-1]
    declared = published_debt(root)
    if declared is None:
        report.notes.append(
            _v(
                "NO_PUBLISHED_INVENTORY",
                f"لا حِملَ منشورًا في «{PUBLISHED_INVENTORY.as_posix()}» يُقابَلُ "
                "بالمقيسِ — فلا يُقاسُ تقادُمُ المنشورِ في هذه التشغيلةِ.",
            )
        )
    elif declared != newest_point.debt_sites:
        report.violations.append(
            _v(
                "PUBLISHED_INVENTORY_DIVERGES",
                f"الحِملُ المنشورُ يُعلِنُ دَينًا {declared} والمقيسُ عندَ "
                f"«{newest_point.work}» {newest_point.debt_sites} — "
                "رقمٌ منشورٌ يُخالِفُ المقيسَ يُقرأُ حاضرًا وهو ماضٍ.",
            )
        )
    else:
        report.notes.append(
            _v(
                "PUBLISHED_INVENTORY_AGREES",
                f"الحِملُ المنشورُ والمقيسُ عندَ «{newest_point.work}» "
                f"متساويانِ: {declared}.",
            )
        )

    report.notes.append(
        _v(
            "SURFACE_TREND",
            f"نقاطٌ مقيسةٌ {len(report.snapshots)} · "
            + " → ".join(f"{s.work}:{s.debt_sites}" for s in report.snapshots)
            + f" · صافي التغيُّرِ {report.snapshots[-1].debt_sites - report.snapshots[0].debt_sites:+d}"
            f" · الأسطحُ كلُّها عندَ الرأسِ {newest_point.total_sites}"
            f" · القاعدةُ {INVENTORY_TOOL.as_posix()}.",
        )
    )
    return report


def render(report: Report) -> str:
    lines = ["[SURFACE TREND] اتِّجاهُ دَينِ الأسطحِ بينَ قيودِ § 8:"]
    for snapshot in report.snapshots:
        lines.append(
            f"  {snapshot.work} ({snapshot.entry_date}) · {snapshot.commit[:12]} · "
            f"أسطحٌ {snapshot.total_sites} · دَينٌ {snapshot.debt_sites}"
        )
    for step in report.steps:
        lines.append(
            f"  {step['from']} → {step['to']}: دَينٌ {step['debt_delta']:+d} · "
            f"أسطحٌ {step['total_delta']:+d}"
        )
    for note in report.notes:
        lines.append(f"  ملاحظة · {note['kind']}: {note['detail']}")
    for violation in report.violations:
        lines.append(f"  ✗ {violation['kind']}: {violation['detail']}")
    if not report.violations:
        lines.append("  ✓ لا صعودَ مقيسًا في دَينِ الأسطحِ بينَ القيدَينِ المقيسَينِ.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="قياسُ اتِّجاهِ دَينِ الأسطحِ بينَ قيدَينِ متتاليَينِ (W-061)."
    )
    parser.add_argument("--root", default=None, help="جذرُ استنساخٍ يُقاسُ بدلًا من هذا.")
    parser.add_argument(
        "--entries",
        type=int,
        default=2,
        help="عددُ أحدثِ قيودِ § 8 التي تُقاسُ (نقطتانِ على الأقلِّ).",
    )
    parser.add_argument("--json", action="store_true", help="طبعُ الحِملِ كاملًا JSON.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else REPO_ROOT
    try:
        report = measure(root, entries=args.entries)
    except MeasurementRefused as refusal:
        print(
            f"[SURFACE TREND] رفضٌ · {refusal.kind}: {refusal.detail}",
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
