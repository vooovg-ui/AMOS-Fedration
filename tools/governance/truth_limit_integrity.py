#!/usr/bin/env python3
"""
قياسُ سلامةِ أرقامِ حدودِ الصدقِ — Truth Limit Numbering Integrity Measure

الهدف: تصييرُ `DISC-045` رقمًا يُقاسُ لا فقرةً تُروى. حدودُ الصدقِ المُعلَنةُ في
       [`COMPLETION_LEDGER.md § 10`] تُحالُ إليها القيودُ والبنودُ بعبارةِ «الحدُّ N»،
       فإن حملَ رقمٌ واحدٌ حدَّينِ صارَت الإحالةُ **لا تُحَلُّ**: القارئُ لا يعرفُ
       أيَّ حدٍّ يُحتَجُّ به. وهذا الملفُّ يقيسُ أربعةَ أرقامٍ تُعادُ:
         - عددُ الحدودِ المُعلَنةِ في القسمِ،
         - الأرقامُ المكتوبةُ **أكثرَ من مرّةٍ**،
         - الفجواتُ في تسلسلِ 1…أقصى،
         - والإحالاتُ في المستودعِ التي **لا تُحَلُّ** إلى حدٍّ واحدٍ بعينِه
           (‏رقمٌ داخلَ مدى الترقيمِ يحملُه حدّانِ فأكثرُ — فالإحالةُ ملتبسةٌ).

النطاق: القياسُ وحدَه. لا يُعيدُ هذا الملفُّ ترقيمَ حدٍّ ولا يُعدِّلُ نصَّ القسمِ
        ولا يُصحِّحُ إحالةً — وإعادةُ الترقيمِ **ممنوعةٌ** لأنَّ الأرقامَ مُحال
        إليها من قيودٍ مدفوعةٍ لا تُمحى، فترقيمٌ جديدٌ يكسِرُ إحالاتٍ صادقةً
        ويُنشِئُ مصدرَ حقيقةٍ ثانيًا (`DISC-045`).
المالك: tools/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

## الحدُّ المُعلَنُ في الأداةِ نفسِها
القياسُ **نصّيٌّ**: يقرأُ صيغَ الإحالةِ المعروفةَ («الحدُّ N» · «حدُّ الصدقِ N»)
بعدَ تجريدِ التشكيلِ. فصياغةٌ جديدةٌ للإحالةِ لا تُرى، والأداةُ لا تقيسُ
**صدقَ الحدِّ** ولا اكتمالَه: حدٌّ فريدُ الرقمِ قد يكونُ كاذبَ المضمونِ — وذاكَ
لا يُقاسُ هنا.

**والالتباسُ وحدَه يُحكَمُ به**: العبارةُ نفسُها تُستعمَلُ لأرقامٍ أجنبيّةٍ عن
القسمِ («الحدُّ 90%» عن تغطيةٍ · «الحدُّ 80%» عن نسبةٍ)، فلا يصدُقُ عَدُّ كلِّ
رقمٍ إحالةً. فالمقيسُ في السقّاطةِ **الإحالةُ الملتبسةُ**: رقمٌ داخلَ مدى
الترقيمِ (1…أقصى) يحملُه أكثرُ من حدٍّ. وما كانَ خارجَ المدى يُطبَعُ **إبلاغًا
لا حكمًا** لأنَّ الرقمَ الأجنبيَّ لا يُفرَّقُ نصًّا عن إحالةٍ معلَّقةٍ — وهذا
حدٌّ مُعلَنٌ لا مطويٌّ. والنسبةُ المئويّةُ تُستثنى صراحةً بعلامتِها.

## سقّاطةٌ لا تعلو ولا تُترَكُ رخوةً
الأرقامُ الثلاثةُ (‏التكرارُ · الفجواتُ · الإحالاتُ الملتبسةُ) **لا تعلو** عن
المُعلَنِ، وإن انخفضَت وجبَ خفضُ المُعلَنِ فلا تبقى سقّاطةٌ رخوةً تُخفي عودةَ
العَطبِ. وعددُ الحدودِ يُطابِقُ المُعلَنَ **مطابقةً تامّةً**: نقصانُه يعني أنَّ
حدَّ صدقٍ مُعلَنًا حُذِفَ (‏وحذفُ حدٍّ إخفاءُ فشلٍ لا إصلاحُه)، وزيادتُه توجِبُ
إعلانَ العددِ الجديدِ صراحةً فلا يُزادُ حدٌّ في الظلِّ.

الاستخدام:
    python tools/governance/truth_limit_integrity.py --check
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
import unicodedata
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

#: موضعُ الحدودِ المُعلَنةِ — مصدرُ الحقيقةِ الوحيدُ لأرقامِها.
LEDGER_PATH = Path("docs/audit/COMPLETION_LEDGER.md")

#: موضعُ الرقمِ المُعلَنِ — سطرٌ واحدٌ لا ثابتٌ في فحصٍ.
BASELINE_RECORD = Path("docs/governance/work/DISCOVERIES.md")
BASELINE_KEY = "TRUTH_LIMIT_BASELINE:"
RATCHET_FIELDS = ("duplicate_numbers", "gaps", "ambiguous_references")
LIMITS_FIELD = "limits"
BASELINE_FIELDS = (LIMITS_FIELD, *RATCHET_FIELDS)

#: ترويسةُ القسمِ تُطابَقُ برقمِها لا بنصِّها كلِّه — النصُّ يُصاغُ والرقمُ يحكُمُ.
SECTION_RE = re.compile(r"^##\s*10\s*·", re.MULTILINE)
NEXT_SECTION_RE = re.compile(r"^##\s", re.MULTILINE)

#: عنصرُ حدٍّ مُعلَنٍ: رقمٌ ثمَّ نقطةٌ ثمَّ عنوانٌ عريضٌ.
LIMIT_ITEM_RE = re.compile(r"^(\d+)\.\s+\*\*", re.MULTILINE)

#: صيغُ الإحالةِ المقروءةُ (‏بعدَ تجريدِ التشكيلِ) — حدٌّ مُعلَنٌ في الترويسةِ.
#: والنسبةُ المئويّةُ ليست إحالةً — تُستثنى بعلامتِها لا بالتقديرِ.
REFERENCE_RES = (
    re.compile(r"حد الصدق\s*(\d+)(?!\d)(?!\s*%)"),
    re.compile(r"الحد\s*(\d+)(?!\d)(?!\s*%)"),
    re.compile(r"حدا\s*(\d+)(?!\d)(?!\s*%)"),
)

#: ما يُقاسُ فيه الإحالاتُ — نصُّ الحوكمةِ وشِفرةُ أدواتِها وفحوصُها.
SCANNED_SUFFIXES = (".md", ".py")

#: مجلَّداتٌ ليست من المستودعِ المقيسِ — تُستثنى بالاسمِ لا بالتقديرِ.
SKIPPED_DIRS = frozenset({".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"})

_TASHKEEL = {chr(c) for c in range(0x064B, 0x0653)} | {"\u0640", "\u0670"}


class SectionUnreadable(RuntimeError):
    """يُرفَعُ حينَ لا يوجدُ قسمُ الحدودِ أو يتكرَّرُ — ولا يُخمَّنُ رقمٌ."""


class BaselineRecordMissing(RuntimeError):
    """يُرفَعُ حينَ يغيبُ سطرُ الرقمِ المُعلَنِ أو يتكرَّرُ — فلا مرجعَ يُقاسُ عليه."""


class ScanUnreadable(RuntimeError):
    """يُرفَعُ حينَ لا يُقرأُ ملفٌّ نصّيٌّ من ملفّاتِ القياسِ.

    فملفٌّ لاحقتُه `.md`/`.py` ولا يُقرأُ نصًّا **عَطبٌ في القياسِ** لا حالةٌ
    عاديّةٌ: تخطّيهِ بصمتٍ يُنقِصُ الإحالاتَ المقيسةَ فيُقرأُ نقصُ القياسِ
    انخفاضًا في العَطبِ — وذاكَ إخفاءُ فشلٍ. فيُعلَنُ ويُسقِطُ الفحصَ.
    """


def normalize(text: str) -> str:
    """يُجرِّدُ التشكيلَ — الإحالةُ تُقرأُ بمعناها لا بشكلِ حركاتِها."""
    return "".join(
        ch for ch in unicodedata.normalize("NFC", text) if ch not in _TASHKEEL
    )


def section_text(repo: Path | None = None) -> str:
    """نصُّ § 10 وحدَه — يُقتَطعُ بترويستِه وبأوّلِ ترويسةٍ بعدَها."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    text = (repo / LEDGER_PATH).read_text(encoding="utf-8")
    heads = list(SECTION_RE.finditer(text))
    if len(heads) != 1:
        raise SectionUnreadable(
            f"ترويسةُ «## 10 ·» في {LEDGER_PATH} وُجِدَت {len(heads)} مرّةً "
            "والمطلوبُ مرّةً واحدةً — لا يُقاسُ قسمٌ لا يُعرَفُ حدُّه"
        )
    start = heads[0].end()
    following = NEXT_SECTION_RE.search(text, start)
    return text[heads[0].start() : following.start() if following else len(text)]


def declared_limit_numbers(repo: Path | None = None) -> list[int]:
    """أرقامُ الحدودِ كما هي مكتوبةٌ — بتكرارِها إن تكرَّرَت، لا منزوعةَ التكرارِ."""
    return [int(m.group(1)) for m in LIMIT_ITEM_RE.finditer(section_text(repo))]


def duplicate_numbers(numbers: list[int]) -> dict[int, int]:
    """الأرقامُ المكتوبةُ أكثرَ من مرّةٍ ومرّاتُها — كلُّ واحدٍ منها إحالةٌ ملتبسةٌ."""
    tally: dict[int, int] = {}
    for number in numbers:
        tally[number] = tally.get(number, 0) + 1
    return {number: count for number, count in tally.items() if count > 1}


def numbering_gaps(numbers: list[int]) -> list[int]:
    """الأرقامُ الغائبةُ من 1 إلى الأقصى — فجوةٌ تعني حدًّا حُذِفَ أو ترقيمًا مكسورًا."""
    if not numbers:
        return []
    present = set(numbers)
    return [n for n in range(1, max(numbers) + 1) if n not in present]


def scanned_files(repo: Path | None = None) -> list[Path]:
    """ملفّاتُ القياسِ — تُعَدُّ صراحةً ولا يُستثنى مجلَّدٌ بالتقديرِ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    found: list[Path] = []
    for path in sorted(repo.rglob("*")):
        if path.suffix not in SCANNED_SUFFIXES or not path.is_file():
            continue
        if SKIPPED_DIRS & set(path.relative_to(repo).parts):
            continue
        found.append(path)
    return found


def references(repo: Path | None = None) -> dict[str, list[int]]:
    """إحالاتُ «الحدِّ N» في المستودعِ مرتَّبةً بملفِّها — نصٌّ يُقرأُ لا يُخمَّنُ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    found: dict[str, list[int]] = {}
    for path in scanned_files(repo):
        try:
            raw = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as unreadable:
            # لا يُبتلَعُ عَطبُ قياسٍ: التخطّي الصامتُ يُنقِصُ الإحالاتَ فيُقرأُ خفضًا كاذبًا
            raise ScanUnreadable(
                f"ملفُّ قياسٍ لا يُقرأُ نصًّا: {path.relative_to(repo)} ({unreadable}) — "
                "القياسُ ناقصٌ فلا يُدَّعى رقمٌ"
            ) from unreadable
        plain = normalize(raw)
        hits = [int(m.group(1)) for pattern in REFERENCE_RES for m in pattern.finditer(plain)]
        if hits:
            found[str(path.relative_to(repo))] = sorted(hits)
    return found


def _tally(numbers: list[int]) -> dict[int, int]:
    tally: dict[int, int] = {}
    for number in numbers:
        tally[number] = tally.get(number, 0) + 1
    return tally


def ambiguous_references(repo: Path | None = None) -> dict[str, list[int]]:
    """الإحالاتُ الملتبسةُ: رقمٌ **داخلَ المدى** يحملُه أكثرُ من حدٍّ واحدٍ.

    وهذا وحدَه ما يُحكَمُ به: رقمٌ خارجَ المدى لا يُفرَّقُ نصًّا عن رقمٍ أجنبيٍّ
    عن القسمِ، فيُبلَّغُ عنه ولا يُبنى عليه حكمٌ (‏حدُّ الأداةِ مُعلَنٌ).
    """
    numbers = declared_limit_numbers(repo)
    tally = _tally(numbers)
    ceiling = max(numbers) if numbers else 0
    found: dict[str, list[int]] = {}
    for path, hits in references(repo).items():
        bad = [n for n in hits if 1 <= n <= ceiling and tally.get(n, 0) != 1]
        if bad:
            found[path] = bad
    return found


def outside_range_references(repo: Path | None = None) -> dict[str, list[int]]:
    """إحالاتٌ برقمٍ خارجَ مدى الترقيمِ — إبلاغٌ لا حكمٌ (‏قد تكونُ أرقامًا أجنبيّةً)."""
    numbers = declared_limit_numbers(repo)
    ceiling = max(numbers) if numbers else 0
    found: dict[str, list[int]] = {}
    for path, hits in references(repo).items():
        outside = [n for n in hits if not 1 <= n <= ceiling]
        if outside:
            found[path] = outside
    return found


def measure(repo: Path | None = None) -> dict[str, int]:
    """الأرقامُ الأربعةُ — تُعادُ من النصِّ نفسِه لا من ذاكرةِ كاتبٍ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    numbers = declared_limit_numbers(repo)
    ambiguous = ambiguous_references(repo)
    return {
        LIMITS_FIELD: len(numbers),
        "duplicate_numbers": len(duplicate_numbers(numbers)),
        "gaps": len(numbering_gaps(numbers)),
        "ambiguous_references": sum(len(v) for v in ambiguous.values()),
    }


def declared_baseline(repo: Path | None = None) -> dict[str, int]:
    """يقرأُ الرقمَ المُعلَنَ من سجلِّ الاكتشافاتِ — مصدرٌ واحدٌ لا يُنازَع."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    text = (repo / BASELINE_RECORD).read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if BASELINE_KEY in ln]
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

    if measured[LIMITS_FIELD] < declared[LIMITS_FIELD]:
        problems.append(
            f"حدُّ صدقٍ مُعلَنٌ حُذِفَ: مقيسٌ {measured[LIMITS_FIELD]} · "
            f"المُعلَنُ {declared[LIMITS_FIELD]} — حذفُ حدٍّ إخفاءُ فشلٍ لا إصلاحُه"
        )
    elif measured[LIMITS_FIELD] > declared[LIMITS_FIELD]:
        problems.append(
            f"حدٌّ زِيدَ ولم يُعلَنْ عددُه: مقيسٌ {measured[LIMITS_FIELD]} · "
            f"المُعلَنُ {declared[LIMITS_FIELD]} — يُحدَّثُ سطرُ `{BASELINE_KEY}`"
        )

    for field in RATCHET_FIELDS:
        if measured[field] > declared[field]:
            problems.append(
                f"{field}: مقيسٌ {measured[field]} · المُعلَنُ {declared[field]} — الالتباسُ علا"
            )
        elif measured[field] < declared[field]:
            problems.append(
                f"{field}: مقيسٌ {measured[field]} · المُعلَنُ {declared[field]} — "
                "انخفضَ ولم يُخفَضِ المُعلَنُ فلا تُترَكُ سقّاطةٌ رخوةً"
            )
    return (1 if problems else 0), problems


def main() -> int:
    parser = argparse.ArgumentParser(description="قياسُ سلامةِ أرقامِ حدودِ الصدقِ")
    parser.add_argument("--check", action="store_true", help="يقيسُ ويُقارِنُ بالمُعلَنِ")
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
        "TRUTH_LIMIT: مقيسٌ "
        + " · ".join(f"{k}={measured[k]}" for k in BASELINE_FIELDS)
        + " · المُعلَنُ "
        + " · ".join(f"{k}={declared[k]}" for k in BASELINE_FIELDS)
    )
    duplicates = duplicate_numbers(declared_limit_numbers(repo))
    if duplicates:
        print(
            "  أرقامٌ مكرَّرةٌ: "
            + " · ".join(f"{n} (‏{c} مرّاتٍ)" for n, c in sorted(duplicates.items()))
        )
    for path, hits in sorted(ambiguous_references(repo).items()):
        print(f"  إحالةٌ ملتبسةٌ · {path}: " + " · ".join(str(h) for h in hits))
    outside = outside_range_references(repo)
    if outside:
        print(
            "  ملاحظة · OUTSIDE_RANGE_REFERENCES: أرقامٌ خارجَ مدى الترقيمِ "
            + " · ".join(
                f"{path}={','.join(str(h) for h in hits)}" for path, hits in sorted(outside.items())
            )
            + " — إبلاغٌ لا إسقاطٌ: لا يُفرَّقُ نصًّا رقمٌ أجنبيٌّ عن إحالةٍ معلَّقةٍ"
        )
    if not args.check:
        return 0

    code, problems = verdict(repo)
    if code:
        for problem in problems:
            print(f"[TRUTH LIMIT] ✗ {problem}", file=sys.stderr)
        return code
    print("[TRUTH LIMIT] ✓ لا نموَّ في التباسِ أرقامِ الحدودِ، والعددُ المُعلَنُ مُطابِقٌ.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
