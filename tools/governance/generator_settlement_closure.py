#!/usr/bin/env python3
"""
قياسُ إغلاقِ رباطِ المُولِّداتِ — Generator Settlement Closure Measure

الهدف: تصييرُ `DISC-051` رقمًا يُقاسُ لا قائمةً تُكتَبُ بخطِّ اليدِ. الأداةُ التي
       تكتُبُ أثرًا في الشجرةِ وتُعلِنُ وجهَ `--check` **لا يُنتفَعُ بوجهِها إن لم
       يُشغَّلْ على المستودعِ الحقيقيِّ**: فالأثرُ يتقادَمُ في الشجرةِ ولا تحمَرُّ
       بوّابةٌ محلّيّةٌ، وذاكَ عينُ ما حمَّرَ التشغيلَ 55 في `DISC-040`. وأُغلِقَ
       ذاكَ العَطبُ **لأداةٍ واحدةٍ** (`truth_audit.py` · `W-099`) لا لجنسِه،
       والرباطُ الباقي قائمةُ أسماءٍ في فحصٍ: مُولِّدٌ جديدٌ يولَدُ خارجَ الحرسِ
       بصمتٍ. فهذا الملفُّ يُعيدُ ثلاثةَ أرقامٍ من الشجرةِ نفسِها:
         - عددَ المُولِّداتِ (‏تكتُبُ أثرًا · وتُعلِنُ `--check`)،
         - المربوطَ منها (‏وجهُ `--check` يُشغَّلُ على جذرِ المستودعِ الحقيقيِّ)،
         - وغيرَ المربوطِ.

النطاق: القياسُ وحدَه. لا يكتُبُ هذا الملفُّ فحصًا، ولا يربطُ مُولِّدًا، ولا
        يُعدِّلُ أداةً، ولا يُضيفُ أمرًا إلى مجموعةِ ما قبلَ الدفعِ (§ 5.4) —
        فزيادةُ أمرٍ إلى وثيقةٍ حاكمةٍ قرارُ مالكٍ لا فعلُ عاملٍ، وطريقُ الإنفاذِ
        قائمٌ أصلًا: `pytest tests/governance/` تُشغَّلُ في CI ومحلّيًّا.
المالك: tools/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

## حدُّ الأداةِ — مُعلَنٌ لا مطويٌّ

1. **«مُولِّدٌ» يُقاسُ من شجرةِ التحليلِ لا من نصِّ الملفِّ**: نداءُ كتابةٍ في
   الشجرةِ (`write_text` · `write_bytes` · `json.dump`) **مع** نصٍّ حرفيٍّ
   `--check` في الشِفرةِ. والقياسُ نحويٌّ **قصدًا**: أوّلُ نسخةٍ من هذه الأداةِ
   قاسَتْه نصًّا فعَدَّت **نفسَها** مُولِّدًا لأنَّ ترويستَها تحكي عن الكتابةِ —
   فحكمَت على ذِكرٍ في نثرٍ لا على نداءٍ في شِفرةٍ، وأُصلِحَ السببُ لا العَرَضُ.
   وأداةٌ تكتُبُ بوسيلةٍ خارجَ هذه الثلاثةِ لا تُرى، والتعريفُ يُوسَّعُ بالقياسِ
   لا بالتقديرِ.
2. **«الرباطُ» يُقاسُ موضعَ نداءٍ لا ملفًّا**: يُقرأُ من شجرةِ التحليلِ كلُّ نداءٍ
   لعمليّةٍ فرعيّةٍ في `tests/`، فيُشترَطُ فيه `--check` **وذكرُ جذرِ المستودعِ
   الحقيقيِّ** (`REPO_ROOT`) **وخلوُّه من شجرةٍ مؤقَّتةٍ** (`tmp_path` · `tree`).
   ثمَّ يُحَلُّ اسمُ الأداةِ المُنادى بها من ثوابتِ الملفِّ ومن قائمةِ
   `parametrize` — فلا يُعَدُّ الرباطُ قائمًا لمجرَّدِ ورودِ اسمِ الأداةِ في الملفِّ.
3. **والرباطُ ليس كفايةً**: الأداةُ تقيسُ أنَّ الوجهَ **يُشغَّلُ على الشجرةِ
   الحقيقيّةِ**، لا أنَّ ما يقيسُه ذاكَ الوجهُ صادقٌ ولا أنَّ الفحصَ يُسقِطُ
   بحقٍّ. وحكمُ الكفايةِ بشريٌّ يُراجَعُ صفًّا صفًّا.
4. **وملفٌّ لا يُقرأُ نصًّا أو لا يُحَلُّ نحوًا يُسقِطُ القياسَ ولا يُتخطّى بصمتٍ**:
   تخطّيهِ يُنقِصُ المقيسَ فيُقرأُ نقصُ القياسِ انخفاضًا في العَطبِ.

## سقّاطةٌ لا تعلو ولا تُترَكُ رخوةً

`unbound` **لا يعلو** عن المُعلَنِ، وإن انخفضَ وجبَ خفضُ المُعلَنِ فلا تبقى
سقّاطةٌ رخوةً تُخفي عودةَ العَطبِ. و`bound` **أرضيّةٌ لا تنقُصُ**: نقصانُه يعني
أنَّ رباطًا قائمًا حُذِفَ أو عُمِيَ، وحذفُ حرسٍ إخفاءُ فشلٍ لا إصلاحُه. و`generators`
يُطابِقُ `bound + unbound` مطابقةً تامّةً فلا يُطوى مُولِّدٌ في الفرقِ.

الاستخدام:
    python tools/governance/generator_settlement_closure.py --check
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import re
import sys
from pathlib import Path

_ROOT_FINDER_PATH = Path(__file__).resolve().with_name("repo_root.py")
_ROOT_FINDER_SPEC = importlib.util.spec_from_file_location(
    "amos_repo_root_finder", _ROOT_FINDER_PATH
)
if _ROOT_FINDER_SPEC is None or _ROOT_FINDER_SPEC.loader is None:
    raise ImportError(f"تعذّرَ تحميلُ مُكتشِفِ الجذرِ من {_ROOT_FINDER_PATH}")
_ROOT_FINDER = importlib.util.module_from_spec(_ROOT_FINDER_SPEC)
_ROOT_FINDER_SPEC.loader.exec_module(_ROOT_FINDER)

REPO_ROOT = _ROOT_FINDER.discover_repo_root(__file__)

#: موضعُ الأدواتِ المقيسةِ وموضعُ الفحوصِ الرابطةِ — بالاسمِ لا بالتقديرِ.
TOOLS_DIR = Path("tools")
TESTS_DIR = Path("tests")

#: موضعُ الرقمِ المُعلَنِ — سطرٌ واحدٌ لا ثابتٌ في فحصٍ.
BASELINE_RECORD = Path("docs/governance/work/DISCOVERIES.md")
BASELINE_KEY = "GENERATOR_SETTLEMENT_BASELINE:"
GENERATORS_FIELD = "generators"
BOUND_FIELD = "bound"
UNBOUND_FIELD = "unbound"
BASELINE_FIELDS = (GENERATORS_FIELD, BOUND_FIELD, UNBOUND_FIELD)

#: نداءاتُ الكتابةِ في الشجرةِ — تُقرأُ نحوًا لا نصًّا، وحدُّها مُعلَنٌ أعلاه.
ARTIFACT_WRITE_CALLS = frozenset({"write_text", "write_bytes"})
ARTIFACT_DUMP_CALL = "dump"
ARTIFACT_DUMP_MODULES = frozenset({"json", "yaml"})

#: وجهُ الاستقرارِ كما يُكتَبُ في مُحلِّلِ الأمرِ.
CHECK_FACE = "--check"

#: أسماءُ نداءاتِ العمليّاتِ الفرعيّةِ المقروءةُ.
SUBPROCESS_CALLS = frozenset({"run", "check_output", "check_call", "Popen"})

#: علامةُ جذرِ المستودعِ الحقيقيِّ في موضعِ النداءِ.
REAL_ROOT_MARK = "REPO_ROOT"

#: علاماتُ الشجرةِ المؤقَّتةِ — موضعُ نداءٍ يحملُها لا يحكُمُ على المستودعِ.
TEMPORARY_TREE_RES = (re.compile(r"\btmp_path\b"), re.compile(r"\btree\b"))

#: مجلَّداتٌ ليست من المستودعِ المقيسِ — تُستثنى بالاسمِ لا بالتقديرِ.
SKIPPED_DIRS = frozenset(
    {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"}
)


class SourceUnreadable(RuntimeError):
    """يُرفَعُ حينَ لا يُقرأُ ملفُّ شِفرةٍ نصًّا أو لا يُحَلُّ نحوًا.

    فملفٌّ لاحقتُه `.py` ولا يُقرأُ **عَطبٌ في القياسِ** لا حالةٌ عاديّةٌ:
    تخطّيهِ بصمتٍ يُنقِصُ المُولِّداتَ أو الرباطَ المقيسَ فيُقرأُ نقصُ القياسِ
    انخفاضًا في العَطبِ — وذاكَ إخفاءُ فشلٍ.
    """


class BaselineRecordMissing(RuntimeError):
    """يُرفَعُ حينَ يغيبُ سطرُ الرقمِ المُعلَنِ أو يتكرَّرُ — فلا مرجعَ يُقاسُ عليه."""


def _read(path: Path) -> str:
    """يقرأُ ملفَّ شِفرةٍ نصًّا — والتعذُّرُ يُرفَعُ ولا يُتخطّى."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise SourceUnreadable(f"ملفُّ شِفرةٍ لا يُقرأُ نصًّا: {path} — {exc}") from exc


def _parse(path: Path, source: str) -> ast.Module:
    """يُحَلُّ الملفُّ نحوًا — وفشلُ التحليلِ عَطبُ قياسٍ يُرفَعُ."""
    try:
        return ast.parse(source)
    except SyntaxError as exc:
        raise SourceUnreadable(f"ملفُّ شِفرةٍ لا يُحَلُّ نحوًا: {path} — {exc}") from exc


def _python_files(root: Path, relative: Path) -> list[Path]:
    """ملفّاتُ الشِفرةِ تحتَ مجلَّدٍ — مرتَّبةً ليكونَ المُخرَجُ مُستقرًّا."""
    base = root / relative
    if not base.is_dir():
        return []
    found = [
        path
        for path in base.rglob("*.py")
        if not SKIPPED_DIRS.intersection(path.parts)
    ]
    return sorted(found)


def _writes_artifact(module: ast.Module) -> bool:
    """نداءُ كتابةٍ في الشجرةِ — يُقرأُ نحوًا فلا يُحكَمُ على ذِكرٍ في نثرٍ."""
    for node in ast.walk(module):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not isinstance(func, ast.Attribute):
            continue
        if func.attr in ARTIFACT_WRITE_CALLS:
            return True
        if func.attr == ARTIFACT_DUMP_CALL and isinstance(func.value, ast.Name):
            if func.value.id in ARTIFACT_DUMP_MODULES:
                return True
    return False


def _declares_check_face(module: ast.Module) -> bool:
    """وجهُ `--check` مُعلَنًا نصًّا حرفيًّا في الشِفرةِ لا في ترويسةٍ."""
    return any(
        isinstance(node, ast.Constant) and node.value == CHECK_FACE
        for node in ast.walk(module)
        if isinstance(node, ast.Constant)
    )


def generators(repo: Path | None = None) -> dict[str, str]:
    """المُولِّداتُ: تكتُبُ أثرًا في الشجرةِ **وتُعلِنُ** وجهَ `--check`."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    found: dict[str, str] = {}
    for path in _python_files(repo, TOOLS_DIR):
        module = _parse(path, _read(path))
        if not _declares_check_face(module):
            continue
        if not _writes_artifact(module):
            continue
        found[path.stem] = path.relative_to(repo).as_posix()
    return found


def _string_constants(node: ast.AST) -> list[str]:
    """كلُّ نصٍّ حرفيٍّ داخلَ عقدةٍ — مادّةُ حلِّ اسمِ الأداةِ المُنادى بها."""
    return [
        child.value
        for child in ast.walk(node)
        if isinstance(child, ast.Constant) and isinstance(child.value, str)
    ]


def _module_symbols(module: ast.Module) -> dict[str, list[str]]:
    """ثوابتُ الملفِّ: اسمٌ ⇒ النصوصُ الحرفيّةُ في قيمتِه (مثلُ `TOOL_PATH`)."""
    symbols: dict[str, list[str]] = {}
    for statement in module.body:
        if not isinstance(statement, ast.Assign):
            continue
        values = _string_constants(statement.value)
        if not values:
            continue
        for target in statement.targets:
            if isinstance(target, ast.Name):
                symbols[target.id] = values
    return symbols


def _parametrized_strings(function: ast.AST, source: str) -> list[str]:
    """نصوصُ `parametrize` — فقائمةُ الأدواتِ تُقرأُ من الزينةِ لا تُخمَّنُ."""
    decorators = getattr(function, "decorator_list", [])
    values: list[str] = []
    for decorator in decorators:
        segment = ast.get_source_segment(source, decorator) or ""
        if "parametrize" in segment:
            values.extend(_string_constants(decorator))
    return values


def _is_real_root_check(segment: str) -> bool:
    """موضعُ نداءٍ يحكُمُ على المستودعِ الحقيقيِّ بوجهِ `--check`."""
    if CHECK_FACE not in segment or REAL_ROOT_MARK not in segment:
        return False
    return not any(mark.search(segment) for mark in TEMPORARY_TREE_RES)


def _call_name(call: ast.Call) -> str:
    func = call.func
    if isinstance(func, ast.Attribute):
        return func.attr
    return getattr(func, "id", "")


def settlement_sites(repo: Path | None = None) -> dict[str, set[str]]:
    """اسمُ الأداةِ ⇒ ملفّاتُ الفحصِ التي تُشغِّلُ وجهَها على الجذرِ الحقيقيِّ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    stems = set(generators(repo))
    sites: dict[str, set[str]] = {}
    for path in _python_files(repo, TESTS_DIR):
        if not path.name.startswith("test_"):
            continue
        source = _read(path)
        module = _parse(path, source)
        symbols = _module_symbols(module)
        functions = [
            node
            for node in ast.walk(module)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        for function in functions:
            parametrized = _parametrized_strings(function, source)
            for node in ast.walk(function):
                if not isinstance(node, ast.Call):
                    continue
                if _call_name(node) not in SUBPROCESS_CALLS:
                    continue
                segment = ast.get_source_segment(source, node) or ""
                if not _is_real_root_check(segment):
                    continue
                candidates = set(_string_constants(node)) | set(parametrized)
                for name in {
                    child.id for child in ast.walk(node) if isinstance(child, ast.Name)
                }:
                    candidates.update(symbols.get(name, []))
                blob = " ".join(sorted(candidates))
                for stem in stems:
                    if stem in blob:
                        sites.setdefault(stem, set()).add(
                            path.relative_to(repo).as_posix()
                        )
    return sites


def measure(repo: Path | None = None) -> dict[str, int]:
    """الأرقامُ الثلاثةُ — تُعادُ من الشجرةِ نفسِها لا من ذاكرةِ كاتبٍ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    tools = generators(repo)
    bound = set(settlement_sites(repo))
    return {
        GENERATORS_FIELD: len(tools),
        BOUND_FIELD: len(bound),
        UNBOUND_FIELD: len(set(tools) - bound),
    }


def unbound_generators(repo: Path | None = None) -> list[str]:
    """المُولِّداتُ بلا رباطٍ مقيسٍ — بأسمائِها لا بعددِها وحدَه."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    return sorted(set(generators(repo)) - set(settlement_sites(repo)))


def declared_baseline(repo: Path | None = None) -> dict[str, int]:
    """يقرأُ الرقمَ المُعلَنَ من سجلِّ الاكتشافاتِ — مصدرٌ واحدٌ لا يُنازَع."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    text = (repo / BASELINE_RECORD).read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if BASELINE_KEY in line]
    if len(lines) != 1:
        raise BaselineRecordMissing(
            f"سطرُ `{BASELINE_KEY}` في {BASELINE_RECORD} وُجِدَ {len(lines)} مرّةً "
            "والمطلوبُ مرّةً واحدةً — لا يُخمَّنُ رقمٌ ولا يُتجاوَزُ الحرسُ"
        )
    values: dict[str, int] = {}
    for field in BASELINE_FIELDS:
        match = re.search(rf"{field}=(\d+)", lines[0])
        if match is None:
            raise BaselineRecordMissing(
                f"الحقلُ `{field}` غائبٌ عن سطرِ `{BASELINE_KEY}` — الرقمُ المُعلَنُ ناقصٌ"
            )
        values[field] = int(match.group(1))
    return values


def verdict(repo: Path | None = None) -> tuple[int, list[str]]:
    """الحكمُ ورسائلُه — رمزُ خروجٍ يُقاسُ لا تقريرٌ يُقرَأُ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    measured = measure(repo)
    declared = declared_baseline(repo)
    problems: list[str] = []

    if measured[UNBOUND_FIELD] > declared[UNBOUND_FIELD]:
        problems.append(
            f"SETTLEMENT_GAP_GROWTH: بلا رباطٍ مقيسٌ {measured[UNBOUND_FIELD]} · "
            f"المُعلَنُ {declared[UNBOUND_FIELD]} — مُولِّدٌ وُلِدَ خارجَ الحرسِ: "
            + " · ".join(unbound_generators(repo))
        )
    elif measured[UNBOUND_FIELD] < declared[UNBOUND_FIELD]:
        problems.append(
            f"STALE_SETTLEMENT_BASELINE: بلا رباطٍ مقيسٌ {measured[UNBOUND_FIELD]} · "
            f"المُعلَنُ {declared[UNBOUND_FIELD]} — انخفضَ ولم يُخفَضِ المُعلَنُ "
            "فلا تُترَكُ سقّاطةٌ رخوةً"
        )

    if measured[BOUND_FIELD] < declared[BOUND_FIELD]:
        problems.append(
            f"SETTLEMENT_BINDING_LOSS: مربوطٌ مقيسٌ {measured[BOUND_FIELD]} · "
            f"المُعلَنُ {declared[BOUND_FIELD]} — رباطٌ قائمٌ حُذِفَ أو عُمِيَ، "
            "وحذفُ حرسٍ إخفاءُ فشلٍ لا إصلاحُه"
        )

    if measured[GENERATORS_FIELD] != declared[GENERATORS_FIELD]:
        problems.append(
            f"GENERATOR_COUNT_UNDECLARED: مُولِّداتٌ مقيسةٌ {measured[GENERATORS_FIELD]} · "
            f"المُعلَنُ {declared[GENERATORS_FIELD]} — يُحدَّثُ سطرُ `{BASELINE_KEY}` "
            "فلا يُزادُ مُولِّدٌ ولا يُحذَفُ في الظلِّ"
        )

    if measured[GENERATORS_FIELD] != measured[BOUND_FIELD] + measured[UNBOUND_FIELD]:
        problems.append(
            "MEASURE_INCONSISTENT: المُولِّداتُ لا تُساوي المربوطَ زائدَ غيرِ المربوطِ "
            "— عَطبٌ في القياسِ نفسِه لا في الشجرةِ"
        )
    return (1 if problems else 0), problems


def main() -> int:
    parser = argparse.ArgumentParser(description="قياسُ إغلاقِ رباطِ المُولِّداتِ")
    parser.add_argument(
        "--check", action="store_true", help="يقيسُ ويُقارِنُ بالمُعلَنِ"
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="جذرُ القياسِ صريحًا — يُقاسُ ما يُقالُ لا ما يُخمَّنُ (`DISC-032`)",
    )
    args = parser.parse_args()
    repo = Path(args.repo_root).resolve() if args.repo_root else REPO_ROOT

    measured = measure(repo)
    declared = declared_baseline(repo)
    print(
        "GENERATOR_SETTLEMENT: مقيسٌ "
        + " · ".join(f"{key}={measured[key]}" for key in BASELINE_FIELDS)
        + " · المُعلَنُ "
        + " · ".join(f"{key}={declared[key]}" for key in BASELINE_FIELDS)
    )
    sites = settlement_sites(repo)
    for stem in sorted(sites):
        print(f"  مربوطٌ · {stem}: " + " · ".join(sorted(sites[stem])))
    gap = unbound_generators(repo)
    if gap:
        print("  بلا رباطٍ مقيسٍ: " + " · ".join(gap))
    if not args.check:
        return 0

    code, problems = verdict(repo)
    if code:
        for problem in problems:
            print(f"[GENERATOR SETTLEMENT] ✗ {problem}", file=sys.stderr)
        return code
    print(
        "[GENERATOR SETTLEMENT] ✓ لا نموَّ في المُولِّداتِ بلا رباطٍ، "
        "والمربوطُ لم ينقُصْ، والعددُ المُعلَنُ مُطابِقٌ."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
