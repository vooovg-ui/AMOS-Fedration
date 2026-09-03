"""
حرسُ المقامِ — خُضرةٌ تقولُ كم قرأَت، أو يُقاسُ سكوتُها
الهدف: إحصاءُ كلِّ جملةِ نجاحٍ تُطلِقُها وحدةٌ تحتَ `tools/` (‏تحمِلُ «✓»)، وتمييزُ ما حكمُه **كلّيٌّ** مِمّا هو تقريرُ عددٍ، ثمَّ قياسُ أيُّها يُرفِقُ **مقامًا مقيسًا** (‏كمًّا محسوبًا من المقروءِ) وأيُّها يُعلِنُ الكُلّيّةَ صامتًا عن مقامِه — ومنعُ نموِّ الصامتِ ونقصِ المُقامِ.
النطاق: tools/governance/ — قارئٌ تركيبيٌّ لا يُعدِّلُ أداةً ولا يُدَّعى ملكًا على مسارٍ محجوزٍ
المالك: tools/governance/
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

العَطبُ المقيسُ (`DISC-053` · وجنسُه `DISC-046` و`DISC-052`):
    بوّابةٌ تُخرِجُ عندَ النجاحِ حكمًا **كلّيًّا** («كلُّ …» · «لا مخالفةَ» · «مطابقٌ»)
    ولا تقولُ **كم قرأَت**. فقارئُ الخرجِ لا يملكُ سبيلًا لتمييزِ «قِيسَ ألفٌ فلم
    يُخالِفْ واحدٌ» من «قِيسَ صفرٌ فلم يُخالِفْ شيءٌ»: الحرفُ واحدٌ ورمزُ الخروجِ
    واحدٌ. وذاكَ حدَثَ فعلًا لا فرضًا: في `DISC-052` ضاقَ مقامُ بوّابةِ أحجامِ الحزمِ
    إلى **دعوَيَينِ** وبقيَ حكمُها الكلّيُّ يُطبَعُ، فتقادَمَ رقمٌ مكتوبٌ ومرَّ بخُضرةٍ.

    فالمقامُ ليس زينةَ تقريرٍ: هو **الشرطُ الذي يجعلُ الخُضرةَ قابلةً للتكذيبِ**.

لماذا سقّاطةٌ لا إصلاحٌ شاملٌ في هذا البندِ:
    إرفاقُ المقامِ بكلِّ جملةٍ يمسُّ خمسةَ عشرَ ملفًّا أكثرُها **مُدَّعًى لبنودٍ في يدِ
    المراجعِ** (`WI-023`…`WI-043`)، فالمسُّ الشاملُ الآنَ يُصادِمُ الدعاوى (§ 6.1).
    فالمُستطاعُ بلا مصادمةٍ: **أن يصيرَ العددُ مقيسًا لا يعلو** ويُسمّى أصحابُه —
    ثمَّ يُنزَلُ رقمًا رقمًا حينَ تنفكُّ الدعاوى.

حدُّ الحرسِ — مُعلَنٌ لا مطويٌّ:
    - **يقرأُ `tools/` وحدَها.** وجملُ النجاحِ في `tests/` و`core/` وغيرِها خارجةٌ من
      العدِّ — لا لأنَّها بريئةٌ بل لأنَّ حدَّ البندِ واحدٌ، والحدُّ مكتوبٌ لا مطويٌّ.
    - **الحرسُ يُحصي نفسَه**: جملةُ نجاحِ هذا الملفِّ داخلةٌ في العدِّ وتحمِلُ مقامَها،
      فرقمُ «بمقامٍ» يشملُها. وقارئٌ يُعفي نفسَه يُعلِّمُ الإعفاءَ.
    - **المقامُ يُقاسُ شكلًا لا صدقًا**: جملةٌ تُرفِقُ عددًا محسوبًا من مجموعةٍ **خاطئةٍ**
      تُقرأُ «بمقامٍ». فهذا الحرسُ يمنعُ **الحكمَ الكلّيَّ الأصمَّ** ولا يُصدِّقُ الرقمَ
      المُرفَقَ — وذاكَ حدٌّ من جنسِ كلِّ حرسٍ يقيسُ الشكلَ لا المضمونَ.
    - **الكُلّيّةُ تُعرَفُ بألفاظٍ مُدرَجةٍ** (`UNIVERSAL_TOKENS`): جملةٌ تُعلِنُ الكُلّيّةَ
      بلفظٍ غيرِ مُدرَجٍ تُقرأُ غيرَ كلّيّةٍ فتخرُجُ من العدِّ. وهذا **جنسُ العَطبِ الذي
      يُحرَسُ هنا** بعينِه (`DISC-052`)، فهو مكتوبٌ صريحًا، ويُصحَّحُ **بإضافةِ لفظٍ**
      لا بتخفيفِ السقّاطةِ.
    - **والقراءةُ تركيبيّةٌ (AST) لا نصّيّةٌ**: أداةٌ تبني سطرَ نجاحِها بما لا يراه قارئٌ
      ساكنٌ (‏تجميعٌ في متغيِّرٍ بعيدٍ · قالبٌ يُقرأُ من ملفٍّ) لا تُحصى. وذاكَ **يُضيِّقُ
      العدَّ ولا يُوسِّعُه**، فالسقّاطةُ تبقى صادقةً فيما تراه.
    - **والرقمُ لا يسكنُ الأداةَ**: يُقرأُ من سطرِ `GREEN_DENOMINATOR_BASELINE:` في قيدِ
      `DISC-053`، فمصدرُ الحقيقةِ واحدٌ، وتعليتُه تمرُّ بالسجلِّ المراجَعِ لا بثابتٍ.
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

#: موضعُ الوحداتِ المقيسةِ — بالاسمِ لا بالتقديرِ.
TOOLS_DIR = Path("tools")

#: موضعُ الرقمِ المُعلَنِ — سطرٌ واحدٌ لا ثابتٌ في أداةٍ.
BASELINE_RECORD = Path("docs/governance/work/DISCOVERIES.md")
BASELINE_MARKER = "GREEN_DENOMINATOR_BASELINE:"
BASELINE_FIELDS = ("tools", "green_sentences", "universal", "bounded", "unbounded")

#: علامةُ جملةِ النجاحِ في هذا المستودعِ — الحرفُ الذي تُوسَمُ به الخُضرةُ.
GREEN_MARK = "✓"

#: ألفاظُ الحكمِ الكلّيِّ. مُدرَجةٌ قصدًا، وحدُّها مكتوبٌ في ترويسةِ هذا الملفِّ.
UNIVERSAL_TOKENS: tuple[str, ...] = (
    "كل",
    "جميع",
    "لا مخالف",
    "لا نموَّ",
    "لا انحراف",
    "لا تقاطع",
    "لا عائق",
    "سليم",
    "مطابق",
    "يطابق",
    "يُطابِقُ",
    "مستقيم",
)

#: ما يدلُّ على أنَّ المُدرَجَ في الجملةِ **كمٌّ محسوبٌ من المقروءِ** لا رقمٌ مكتوبٌ.
COUNTING_MARKERS: tuple[str, ...] = (
    "len(",
    "count",
    "total",
    "measured",
    "read",
    "rows",
    "changed",
    "written",
    "closed",
    "exercised",
    "targets",
    "headers",
    "readmes",
    "sentences",
    "universal",
    "bounded",
    "unbound",
)

#: أسوأُ الأصنافِ: حكمٌ كلّيٌّ بلا مقامٍ مقيسٍ.
UNIVERSAL_NO_DENOMINATOR = "UNIVERSAL_WITHOUT_DENOMINATOR"
#: حكمٌ كلّيٌّ يُرفِقُ مقامَه.
UNIVERSAL_WITH_DENOMINATOR = "UNIVERSAL_WITH_DENOMINATOR"
#: جملةُ نجاحٍ لا تُعلِنُ حكمًا كلّيًّا (‏تقريرُ عددٍ أو كتابةُ ملفٍّ) — تُحصى إبلاغًا.
NOT_UNIVERSAL = "NOT_UNIVERSAL"


class BaselineRecordMissing(RuntimeError):
    """سطرُ الرقمِ المُعلَنِ غائبٌ أو مكرَّرٌ أو ناقصُ حقولٍ — يُرفَعُ ولا يُبتلَعُ."""


class SourceUnreadable(RuntimeError):
    """ملفٌّ لا يُقرأُ أو لا يُحَلُّ نحوًا — يُرفَعُ ولا يُتخطّى بصمتٍ."""


class Sentence(NamedTuple):
    """جملةُ نجاحٍ مقيسةٌ، مُصنَّفةً."""

    path: str
    line: int
    verdict: str
    text: str

    def __str__(self) -> str:  # pragma: no cover - للتقريرِ لا للحكمِ
        return f"{self.path}:{self.line}"


def _literal_text(call: ast.Call) -> str:
    """نصُّ ما يُطبَعُ من ثوابتِ السطرِ — تُجمَعُ أجزاءُ `f-string` أيضًا."""
    parts: list[str] = []
    for arg in call.args:
        for node in ast.walk(arg):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                parts.append(node.value)
    return " ".join(parts)


def _interpolated_expressions(call: ast.Call) -> list[str]:
    """تعبيراتُ الإدراجِ في السطرِ — رقمٌ مكتوبٌ حرفًا لا يظهرُ هنا قصدًا."""
    return [
        ast.unparse(node.value)
        for arg in call.args
        for node in ast.walk(arg)
        if isinstance(node, ast.FormattedValue)
    ]


def _is_universal(text: str) -> bool:
    """أحكمُها كلّيٌّ؟ — بألفاظٍ مُدرَجةٍ، وحدُّ الإدراجِ مكتوبٌ في الترويسةِ."""
    return any(token in text for token in UNIVERSAL_TOKENS)


def _carries_denominator(call: ast.Call) -> bool:
    """أيُرفِقُ السطرُ كمًّا **محسوبًا من المقروءِ**؟"""
    return any(
        marker in expression
        for expression in _interpolated_expressions(call)
        for marker in COUNTING_MARKERS
    )


def _classify_source(source: str, label: str) -> list[Sentence]:
    """يُصنِّفُ جملَ النجاحِ في وحدةٍ واحدةٍ — تركيبيًّا لا نصًّا."""
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise SourceUnreadable(
            f"تعذَّرَ تحليلُ {label} نحويًّا فلا يُحكَمُ عليه ولا يُطوى: {exc}"
        ) from exc

    found: list[Sentence] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not (isinstance(node.func, ast.Name) and node.func.id == "print"):
            continue
        text = _literal_text(node)
        if GREEN_MARK not in text:
            continue
        if not _is_universal(text):
            verdict = NOT_UNIVERSAL
        elif _carries_denominator(node):
            verdict = UNIVERSAL_WITH_DENOMINATOR
        else:
            verdict = UNIVERSAL_NO_DENOMINATOR
        found.append(Sentence(label, node.lineno, verdict, text.strip()[:120]))
    return found


def measured_units(root: Path) -> list[Path]:
    """كلُّ وحدةٍ تحتَ `tools/` تُحَلُّ نحوًا — والحدُّ مُعلَنٌ في الترويسةِ."""
    return sorted((root / TOOLS_DIR).rglob("*.py"))


def census(root: Path) -> list[Sentence]:
    """جملُ النجاحِ كلُّها مُصنَّفةً — وعَطبُ قراءةٍ يُرفَعُ لا يُتخطّى."""
    sentences: list[Sentence] = []
    for path in measured_units(root):
        label = path.relative_to(root).as_posix()
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            raise SourceUnreadable(
                f"تعذَّرَ قراءةُ {label} فلا يُحكَمُ عليه ولا يُطوى: {exc}"
            ) from exc
        sentences.extend(_classify_source(source, label))
    return sentences


def unbounded_sentences(root: Path) -> list[Sentence]:
    """الحكمُ الكلّيُّ الأصمُّ — يُسمّى بموضعِه لا بعددِه وحدَه."""
    return [s for s in census(root) if s.verdict == UNIVERSAL_NO_DENOMINATOR]


def measured_counts(root: Path) -> dict[str, int]:
    """الأرقامُ المقيسةُ الخمسةُ — تُقارَنُ بالمُعلَنِ حرفًا بحرفٍ."""
    sentences = census(root)
    return {
        "tools": len(measured_units(root)),
        "green_sentences": len(sentences),
        "universal": sum(1 for s in sentences if s.verdict != NOT_UNIVERSAL),
        "bounded": sum(1 for s in sentences if s.verdict == UNIVERSAL_WITH_DENOMINATOR),
        "unbounded": sum(
            1 for s in sentences if s.verdict == UNIVERSAL_NO_DENOMINATOR
        ),
    }


def declared_baseline(root: Path) -> dict[str, int]:
    """يقرأُ الرقمَ المُعلَنَ من قيدِ `DISC-053` — ولا يُخترَعُ رقمٌ في الأداةِ."""
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
        if "=" not in chunk:
            continue
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
    """السقّاطاتُ الأربعُ — كلٌّ باسمِها لا برمزٍ عامٍّ."""
    measured = measured_counts(root)
    declared = declared_baseline(root)
    problems: list[str] = []

    if measured["unbounded"] > declared["unbounded"]:
        named = "\n    ".join(
            f"{s.path}:{s.line} · {s.text}" for s in unbounded_sentences(root)
        )
        problems.append(
            "DENOMINATOR_GAP_GROWTH: حكمٌ كلّيٌّ جديدٌ بلا مقامٍ — "
            f"مقيسٌ {measured['unbounded']} · المُعلَنُ {declared['unbounded']}. "
            "والمقامُ شرطُ تكذيبِ الخُضرةِ، فلا يُرفَعُ الرقمُ ليسَعَ جملةً صامتةً:\n    "
            + named
        )

    if measured["bounded"] < declared["bounded"]:
        problems.append(
            "DENOMINATOR_LOSS: مقامٌ مقيسٌ نقصَ — "
            f"مقيسٌ {measured['bounded']} · المُعلَنُ {declared['bounded']}: "
            "جملةٌ كانت تقولُ كم قرأَت صارَت صامتةً، وذاكَ تراجُعٌ لا تنظيمٌ"
        )

    if measured["universal"] != declared["universal"]:
        problems.append(
            "UNIVERSAL_COUNT_UNDECLARED: عددُ الأحكامِ الكلّيّةِ لا يُطابِقُ المُعلَنَ — "
            f"مقيسٌ {measured['universal']} · المُعلَنُ {declared['universal']}: "
            "يُعادُ القياسُ ويُصحَّحُ القيدُ، ولا يُترَكُ الفرقُ صامتًا"
        )

    stale = {
        name: (measured[name], declared[name])
        for name in ("tools", "green_sentences")
        if measured[name] != declared[name]
    }
    if stale:
        detail = " · ".join(
            f"{name}: مقيسٌ {got} · المُعلَنُ {want}"
            for name, (got, want) in stale.items()
        )
        problems.append(
            "STALE_DENOMINATOR_BASELINE: مقامُ القياسِ نفسُه تغيَّرَ فالقيدُ متقادِمٌ — "
            f"{detail}: يُعادُ القياسُ ويُصحَّحُ القيدُ"
        )

    return problems


def _report(root: Path) -> dict[str, object]:
    sentences = census(root)
    measured = measured_counts(root)
    return {
        "measured": measured,
        "declared": declared_baseline(root),
        "sentences": [s._asdict() for s in sentences],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "حرسُ المقامِ: جملةُ نجاحٍ كلّيّةُ الحكمِ تقولُ كم قرأَت، أو يُقاسُ سكوتُها"
        )
    )
    parser.add_argument("root", nargs="?", default=str(REPO_ROOT))
    parser.add_argument(
        "--check", action="store_true", help="يُسقِطُ إن نما الصامتُ أو نقصَ المُقامُ"
    )
    parser.add_argument("--json", action="store_true", help="القياسُ كاملًا مُهيكَلًا")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if args.json:
        print(json.dumps(_report(root), ensure_ascii=False, indent=2))
        return 0

    measured = measured_counts(root)
    print(
        "[GREEN DENOMINATOR] مقامُ الخُضرةِ يُقاسُ لا يُفترَضُ: "
        f"وحداتٌ مقروءةٌ {measured['tools']} · جملُ نجاحٍ {measured['green_sentences']} · "
        f"أحكامٌ كلّيّةٌ {measured['universal']} · بمقامٍ {measured['bounded']} · "
        f"بلا مقامٍ {measured['unbounded']}"
    )
    for sentence in unbounded_sentences(root):
        print(f"  بلا مقامٍ · {sentence.path}:{sentence.line} · {sentence.text}")

    if not args.check:
        return 0

    problems = verdicts(root)
    if problems:
        print(f"[GREEN DENOMINATOR] ✗ مخالفات: {len(problems)}", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print(
        f"[GREEN DENOMINATOR] ✓ كلُّ ما قِيسَ مُطابِقٌ للمُعلَنِ: "
        f"{measured['universal']} حكمًا كلّيًّا · {measured['bounded']} بمقامٍ · "
        f"{measured['unbounded']} بلا مقامٍ في {measured['tools']} وحدةً مقروءةً"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
