"""
حرسُ الملاحظاتِ — دَينٌ يُعَدُّ، فيُرتَّجُ عددُ ما لا سقفَ له
الهدف: إحصاءُ كلِّ **ملاحظةِ إبلاغٍ** تُطلِقُها بوّابةٌ تحتَ `tools/` وتحمِلُ **عددًا مقيسًا**، وتمييزُ ما رمزُه مذكورٌ في سجلِّ الأرقامِ المُعلَنةِ (‏مرتَّجٌ) مِمّا لا سقفَ له، ثمَّ جعلُ **عددِ ما لا سقفَ له سقفًا لا يعلو** و**عددِ المرتَّجِ أرضًا لا تنزلُ**.
طريقُ الإنفاذ: COVERED_TEST · tests/governance/test_w132_report_note_ratchet.py يحكُمُ على الشجرةِ الحاضرةِ (‏`test_real_tree_check_passes`) ويشملُه استدعاءُ `pytest` في CI
النطاق: tools/governance/ — قارئٌ تركيبيٌّ لا يُعدِّلُ بوّابةً ولا يُدَّعى ملكًا على مسارٍ محجوزٍ
المالك: tools/governance/
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

العَطبُ المقيسُ (`DISC-055` · وجنسُه `DISC-053` و`DISC-054`):
    بوّابةٌ تطبعُ سطرًا يبدأُ بـ«ملاحظة ·» يحمِلُ **عددًا مقيسًا** — أدواتٌ بلا طريقِ
    إنفاذٍ · صفوفٌ بيدِ المالكِ بلا حرسٍ · أرقامٌ خارجَ مدى الترقيمِ — ثمَّ تخرجُ
    برمزِ **0**. فالعددُ يُقرأُ ولا يُمسَكُ، ولا يُفرَّقُ في الخرجِ بينَ رقمٍ
    **إخباريٍّ** لا يُرادُ حبسُه ورقمِ **دَينٍ** يجبُ ألّا يعلوَ: الحرفُ واحدٌ
    والرمزُ واحدٌ. فيستطيعُ الدَّينُ أن ينموَ بلا نهايةٍ وكلُّ البوّاباتِ خضراءُ.

    وذاكَ حدَثَ فعلًا لا فرضًا: صعِدَ جردُ `UNWIRED_TOOL_INVENTORY` **20 ← 21** بينَ
    `W-130` و`W-131` بنزولِ حرسٍ جديدٍ، فلم تُسقِطْ ذاكَ الصعودَ بوّابةٌ ولا سمَّتْه —
    قُرِئَ بالعينِ في سطرِ خرجٍ.

    فـ`DISC-053` قالَ إنَّ الحكمَ الكلّيَّ لا يقولُ كم قرأَ، و`DISC-054` قالَ إنَّ
    الأثرَ يشهدُ بنقصِه ولا سامِعَ — وهذا ثالثُهما: البوّابةُ **تقولُ الرقمَ صراحةً**
    ثمَّ تُخرِجُ 0. فالمقامُ حاضرٌ والشهادةُ حاضرةٌ **والسقفُ غائبٌ**.

لماذا رَتْجُ العددِ لا سقفٌ لكلِّ رقمٍ:
    تحويلُ ملاحظةٍ بعينِها إلى مخالفةٍ يُغيِّرُ حكمَ بوّابةٍ قائمةٍ ويمسُّ ستَّ أدواتٍ
    أكثرُها **مُدَّعًى لبنودٍ في يدِ المراجعِ** (§ 6.1)، وهو قرارٌ في كلِّ رقمٍ على
    حدةٍ لا فعلُ عاملٍ. فالمُستطاعُ بلا مصادمةٍ: **أن يصيرَ عددُ الأعدادِ بلا سقفٍ
    سقفًا** لا يعلو — ثمَّ يُنزَلُ رقمًا رقمًا حينَ تنفكُّ الدعاوى.

حدُّ الحرسِ — مُعلَنٌ لا مطويٌّ:
    - **الرَّتْجُ إعلانٌ مقصودٌ لا ذِكرٌ عارضٌ**: يُقرأُ من سطرٍ واحدٍ مُخصَّصٍ
      (`REPORT_NOTE_RATCHETED:`) يُسمّي الرموزَ التي يحبِسُ عددَها أساسٌ مُعلَنٌ.
      وذاكَ **قُيِّدَ بعدَ عَطبٍ في هذا الحرسِ نفسِه**: كانَ القياسُ الأوّلُ يعُدُّ كلَّ
      رمزٍ **يَرِدُ ذِكرُه** في `DISCOVERIES.md` مرتَّجًا، فرقّى نثرُ القيدِ ثلاثةَ رموزٍ
      إلى «مرتَّجةٍ» بمجرَّدِ أنَّه ضربَ بها المثلَ — وذاكَ إخضارٌ بالكلامِ لا بالحبسِ.
    - **وهذا الحرسُ يمنعُ نموَّ الصمتِ** ولا يُنشِئُ سقفًا لكلِّ رقمٍ — والفرقُ مكتوبٌ
      هنا لا مطويٌّ.
    - **والشكلُ مُدرَجٌ**: تُقاسُ الملاحظاتُ المبنيّةُ على شكلِ
      `‹تقرير›.notes.append(‹بانٍ›("CODE", …))`. بوّابةٌ تطبعُ ملاحظةً بشكلٍ آخرَ
      تُفلِتُ حتّى يُدرَجَ شكلُها.
    - **والعَدُّ شرطُه عددٌ محسوبٌ**: رسالةٌ بلا `FormattedValue` لا تُعَدُّ عادّةً —
      فرسالةٌ تغرِسُ رقمًا حرفيًّا تُفلِتُ، وذاكَ حدٌّ لا ستارَ عليه.
    - **والحرسُ يُحصي نفسَه**: ملاحظتُه داخلةٌ في العدِّ ورمزُها مذكورٌ في القيدِ،
      وجملةُ نجاحِه تحمِلُ مقامَها (`DISC-053`). وقارئٌ يُعفي نفسَه يُعلِّمُ الإعفاءَ.
    - **والرقمُ لا يسكنُ الأداةَ**: يُقرأُ من سطرِ `REPORT_NOTE_BASELINE:` في قيدِ
      `DISC-055`، فمصدرُ الحقيقةِ واحدٌ وتعليتُه تمرُّ بالسجلِّ المراجَعِ.
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import sys
from pathlib import Path
from typing import NamedTuple

_ROOT_FINDER_PATH = Path(__file__).resolve().with_name("repo_root.py")
_ROOT_FINDER_SPEC = importlib.util.spec_from_file_location(
    "amos_repo_root_finder", _ROOT_FINDER_PATH
)
if _ROOT_FINDER_SPEC is None or _ROOT_FINDER_SPEC.loader is None:
    raise ImportError(f"تعذّرَ تحميلُ مُكتشِفِ الجذرِ من {_ROOT_FINDER_PATH}")
_ROOT_FINDER = importlib.util.module_from_spec(_ROOT_FINDER_SPEC)
_ROOT_FINDER_SPEC.loader.exec_module(_ROOT_FINDER)

REPO_ROOT = _ROOT_FINDER.discover_repo_root(__file__)

#: موضعُ البوّاباتِ المقروءةِ — بالاسمِ لا بالتقديرِ.
TOOLS_DIR = Path("tools")

#: موضعُ الرقمِ المُعلَنِ — سطرٌ واحدٌ لا ثابتٌ في أداةٍ.
BASELINE_RECORD = Path("docs/governance/work/DISCOVERIES.md")
BASELINE_MARKER = "REPORT_NOTE_BASELINE:"
#: سطرُ الإعلانِ المقصودِ للرموزِ المحبوسِ عددُها — لا يُغني عنه ذِكرٌ عارضٌ في نثرٍ.
RATCHET_MARKER = "REPORT_NOTE_RATCHETED:"
BASELINE_FIELDS = ("notes", "counted", "ratcheted", "unratcheted")

#: اسمُ الحقلِ الذي تُجمَعُ فيه ملاحظاتُ الإبلاغِ — الشكلُ المُدرَجُ المقيسُ.
NOTES_ATTRIBUTE = "notes"

#: ملاحظةٌ رمزُها مذكورٌ في سجلِّ الأرقامِ المُعلَنةِ — لها سقفٌ مُعلَنٌ.
RATCHETED = "RATCHETED"
#: ملاحظةٌ تطبعُ عددًا مقيسًا ولا سقفَ له.
UNRATCHETED = "UNRATCHETED"


class BaselineRecordMissing(RuntimeError):
    """سطرُ الرقمِ المُعلَنِ غائبٌ أو مكرَّرٌ أو ناقصُ حقولٍ — يُرفَعُ ولا يُبتلَعُ."""


class SourceUnreadable(RuntimeError):
    """ملفٌّ لا يُقرأُ أو لا يُحَلُّ نحوًا — يُرفَعُ ولا يُعَدُّ «بلا ملاحظاتٍ»."""


class Report:
    """حاملُ ملاحظاتِ هذا الحرسِ — بالشكلِ المقيسِ نفسِه، فيُحصي نفسَه."""

    def __init__(self) -> None:
        self.notes: list[dict[str, str]] = []


def _note(kind: str, detail: str) -> dict[str, str]:
    """بانِي الملاحظةِ — الوسيطُ الأوّلُ رمزٌ ثابتٌ كما يقيسُ هذا الحرسُ."""
    return {"kind": kind, "detail": detail}


class Note(NamedTuple):
    """ملاحظةُ إبلاغٍ واحدةٌ، مقروءةً من شجرةِ التحليلِ."""

    path: str
    line: int
    code: str
    counted: bool
    verdict: str


def _counts_something(call: ast.AST) -> bool:
    """هل تحمِلُ الرسالةُ عددًا **محسوبًا** لا رقمًا مغروسًا؟"""
    for node in ast.walk(call):
        if isinstance(node, ast.JoinedStr) and any(
            isinstance(part, ast.FormattedValue) for part in node.values
        ):
            return True
    return False


def _note_calls(tree: ast.AST) -> list[tuple[int, str, bool]]:
    """كلُّ استدعاءِ `‹تقرير›.notes.append(‹بانٍ›("CODE", …))` في وحدةٍ واحدةٍ."""
    found: list[tuple[int, str, bool]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not (isinstance(func, ast.Attribute) and func.attr == "append"):
            continue
        target = func.value
        if not (isinstance(target, ast.Attribute) and target.attr == NOTES_ATTRIBUTE):
            continue
        for argument in node.args:
            if not (isinstance(argument, ast.Call) and argument.args):
                continue
            first = argument.args[0]
            if not (isinstance(first, ast.Constant) and isinstance(first.value, str)):
                continue
            found.append((node.lineno, first.value, _counts_something(argument)))
    return found


def census(root: Path, cited: frozenset[str]) -> list[Note]:
    """كلُّ ملاحظةِ إبلاغٍ في `tools/` — مقروءةً تركيبيًّا لا نصًّا."""
    notes: list[Note] = []
    for path in sorted((root / TOOLS_DIR).rglob("*.py")):
        label = path.relative_to(root).as_posix()
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            raise SourceUnreadable(
                f"تعذَّرَ قراءةُ {label} فلا يُعَدُّ «بلا ملاحظاتٍ» ولا يُتخطّى: {exc}"
            ) from exc
        try:
            tree = ast.parse(source)
        except SyntaxError as exc:
            raise SourceUnreadable(f"تعذَّرَ حلُّ {label} نحوًا: {exc}") from exc
        for line, code, counted in _note_calls(tree):
            verdict = RATCHETED if code in cited else UNRATCHETED
            notes.append(Note(label, line, code, counted, verdict))
    return notes


def cited_codes(root: Path) -> frozenset[str]:
    """الرموزُ المُعلَنُ حبسُ عددِها — من سطرٍ مقصودٍ لا من ذِكرٍ عارضٍ في نثرٍ."""
    record = root / BASELINE_RECORD
    try:
        text = record.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise BaselineRecordMissing(
            f"تعذَّرَ قراءةُ سجلِّ الرقمِ المُعلَنِ {BASELINE_RECORD}: {exc}"
        ) from exc

    marked = [line for line in text.splitlines() if RATCHET_MARKER in line]
    if len(marked) != 1:
        raise BaselineRecordMissing(
            f"سطرُ الإعلانِ `{RATCHET_MARKER}` يجبُ أن يكونَ واحدًا في "
            f"{BASELINE_RECORD} — وُجِدَ {len(marked)}: الحبسُ إعلانٌ مقصودٌ لا ذِكرٌ عارضٌ"
        )

    tail = marked[0].split(RATCHET_MARKER, 1)[1]
    return frozenset(
        chunk
        for chunk in tail.replace("`", " ").replace("·", " ").split()
        if chunk.isupper() and chunk.replace("_", "").isalpha()
    )


def measured_counts(root: Path) -> dict[str, int]:
    """الأرقامُ المقيسةُ — تُقارَنُ بالمُعلَنةِ حرفًا بحرفٍ."""
    read = census(root, cited_codes(root))
    counted = [n for n in read if n.counted]
    return {
        "notes": len(read),
        "counted": len(counted),
        "ratcheted": sum(1 for n in counted if n.verdict == RATCHETED),
        "unratcheted": sum(1 for n in counted if n.verdict == UNRATCHETED),
    }


def declared_baseline(root: Path) -> dict[str, int]:
    """يقرأُ الرقمَ المُعلَنَ من قيدِ `DISC-055` — ولا يُخترَعُ رقمٌ في الأداةِ."""
    record = root / BASELINE_RECORD
    try:
        text = record.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise BaselineRecordMissing(
            f"تعذَّرَ قراءةُ سجلِّ الرقمِ المُعلَنِ {BASELINE_RECORD}: {exc}"
        ) from exc

    marked = [line for line in text.splitlines() if BASELINE_MARKER in line]
    if len(marked) != 1:
        raise BaselineRecordMissing(
            f"سطرُ الرقمِ المُعلَنِ `{BASELINE_MARKER}` يجبُ أن يكونَ واحدًا في "
            f"{BASELINE_RECORD} — وُجِدَ {len(marked)}: القيدُ مصدرُ الحقيقةِ لا الأداةُ"
        )

    tail = marked[0].split(BASELINE_MARKER, 1)[1]
    fields: dict[str, int] = {}
    for chunk in tail.replace("`", " ").split():
        key, _, value = chunk.partition("=")
        if key in BASELINE_FIELDS and value.isdigit():
            fields[key] = int(value)

    missing = [name for name in BASELINE_FIELDS if name not in fields]
    if missing:
        raise BaselineRecordMissing(
            f"سطرُ الرقمِ المُعلَنِ ناقصٌ حقولًا: {missing} — ولا يُكمَّلُ بتقديرٍ"
        )
    return fields


def verdicts(root: Path) -> list[str]:
    """السقّاطاتُ — كلٌّ باسمِها لا برمزٍ عامٍّ."""
    measured = measured_counts(root)
    declared = declared_baseline(root)
    problems: list[str] = []

    if measured["unratcheted"] > declared["unratcheted"]:
        loose = census(root, cited_codes(root))
        named = " · ".join(
            f"{n.path}:{n.line} {n.code}"
            for n in loose
            if n.counted and n.verdict == UNRATCHETED
        )
        problems.append(
            "UNRATCHETED_NOTE_GROWTH: دَينٌ جديدٌ يُعَدُّ ولا سقفَ له — "
            f"مقيسٌ {measured['unratcheted']} · المُعلَنُ {declared['unratcheted']}: "
            "يُذكَرُ رمزُ الملاحظةِ في سجلِّ الأرقامِ المُعلَنةِ أو يُنزَلُ سقفُه، "
            f"ولا يُحذَفُ الإبلاغُ ولا يُرفَعُ الرقمُ. العادّاتُ بلا سقفٍ: {named}"
        )

    if measured["ratcheted"] < declared["ratcheted"]:
        problems.append(
            "RATCHET_LOSS: سقفٌ مُعلَنٌ اختفى — "
            f"مقيسٌ {measured['ratcheted']} · المُعلَنُ {declared['ratcheted']}: "
            "حُذِفَت ملاحظةٌ مرتَّجةٌ أو أُسقِطَ ذِكرُ رمزِها من القيدِ، وكلاهما "
            "خروجٌ من الحبسِ لا إصلاحٌ — والمرتَّجُ أرضٌ لا تنزلُ"
        )

    if measured["notes"] != declared["notes"] or measured["counted"] != declared["counted"]:
        problems.append(
            "STALE_NOTE_BASELINE: مقامُ القياسِ نفسُه تغيَّرَ فالقيدُ متقادِمٌ — "
            f"notes: مقيسٌ {measured['notes']} · المُعلَنُ {declared['notes']} · "
            f"counted: مقيسٌ {measured['counted']} · المُعلَنُ {declared['counted']}: "
            "يُعادُ القياسُ ويُصحَّحُ القيدُ، ولا يُترَكُ الفرقُ صامتًا"
        )

    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="حرسُ الملاحظاتِ: عددُ ما يُعَدُّ بلا سقفٍ سقفٌ لا يعلو"
    )
    parser.add_argument("root", nargs="?", default=str(REPO_ROOT))
    parser.add_argument(
        "--check", action="store_true", help="يُسقِطُ إن نما الصامتُ أو نقصَ المرتَّجُ"
    )
    parser.add_argument("--json", action="store_true", help="القياسُ كاملًا مُهيكَلًا")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    read = census(root, cited_codes(root))

    if args.json:
        print(
            json.dumps(
                {
                    "measured": measured_counts(root),
                    "declared": declared_baseline(root),
                    "notes": [n._asdict() for n in read],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    measured = measured_counts(root)
    print(
        "[REPORT NOTE] الدَّينُ المعدودُ يُقاسُ لا يُفترَضُ: "
        f"ملاحظاتٌ مقروءةٌ {measured['notes']} · عادّةٌ {measured['counted']} · "
        f"مرتَّجةٌ {measured['ratcheted']} · بلا سقفٍ {measured['unratcheted']}"
    )
    for note in read:
        if note.counted and note.verdict == UNRATCHETED:
            print(f"  بلا سقفٍ · {note.path}:{note.line} · {note.code}")
    report = Report()
    report.notes.append(
        _note(
            "REPORT_NOTE_TALLY",
            f"رموزٌ مُعلَنٌ حبسُ عددِها {measured['ratcheted']} من "
            f"{measured['counted']} ملاحظةً عادّةً — والرَّتْجُ إعلانٌ مقصودٌ في "
            "القيدِ لا إسقاطٌ لكلِّ رقمٍ (‏حدٌّ مُعلَنٌ) · وهذه الملاحظةُ نفسُها "
            "داخلةٌ في العدِّ فلا يُعفي القارئُ نفسَه",
        )
    )
    for entry in report.notes:
        print(f"  ملاحظة · {entry['kind']}: {entry['detail']}")

    if not args.check:
        return 0

    problems = verdicts(root)
    if problems:
        print(f"[REPORT NOTE] ✗ مخالفات: {len(problems)}", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print(
        f"[REPORT NOTE] ✓ كلُّ ما قِيسَ مُطابِقٌ للمُعلَنِ: {measured['ratcheted']} "
        f"مرتَّجةً · {measured['unratcheted']} بلا سقفٍ في {measured['counted']} "
        f"ملاحظةً عادّةً من {measured['notes']} مقروءةً"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
