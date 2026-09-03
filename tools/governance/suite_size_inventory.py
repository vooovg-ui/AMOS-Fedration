#!/usr/bin/env python3
"""
قياسُ صدقِ أحجامِ الحزمِ المكتوبةِ — Suite Size Claim Inventory Measure

الهدف: تصييرُ `DISC-046` رقمًا يُقاسُ لا فقرةً تُروى. دليلُ المشروعِ يُصدِّرُ § 4
       بأنَّ «كلَّ سطرٍ هنا قِيسَ في هذه البيئةِ بالأمرِ المذكورِ»، ثمَّ يكتبُ حجمَ
       حزمةِ الاختباراتِ عددًا صريحًا («N نجحَت · M مُتخطّاة»). ولا بوّابةَ كانت
       تقرأُ رقمًا مكتوبًا في نثرٍ: حرسُ نَسَبِ القياساتِ (`W-037`) يحرسُ ملفّاتِ
       [`docs/audit/measurements/`] وحدَها. فبقيَ الرقمُ يُنقَلُ سنةً بعدَ قياسِه
       ويُقرَأُ حاضرًا. وهذا الملفُّ يجمعُ الحزمَ **حيًّا** ويُقارِنُ المقيسَ
       بالمكتوبِ، فيُصبِحُ الرقمُ المَيّتُ إخفاقًا مُسمًّى لا اكتشافًا متأخِّرًا.

النطاق: القياسُ والحكمُ. لا يُعدِّلُ هذا الملفُّ رقمًا مكتوبًا ولا يُصحِّحُ نصًّا:
        تصحيحُ الرقمِ فعلُ كاتبٍ في ملفٍّ مملوكٍ، والأداةُ تقيسُ وتحكُمُ فقط.

المالك: tools/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

## المخالفاتُ المُسمّاةُ
- `STALE_SUITE_CLAIM` — رقمٌ مكتوبٌ يُخالِفُ الجمعَ الحيَّ للحزمةِ نفسِها.
- `UNREADABLE_CLAIM_SHAPE` — «N نجحَت» بلا «M مُتخطّاة» على سطرِها، فالمجموعُ لا يُقرأُ.
- `UNATTRIBUTED_SUITE_CLAIM` — رقمٌ لا يُعرَفُ لأيِّ حزمةٍ هو.
- `UNDATED_HISTORICAL_CLAIM` — رقمٌ مُعلَنٌ تاريخيًّا بلا قيدٍ يَنسِبُه.
- `SUITE_UNCOLLECTABLE` — حزمةٌ مُعلَنةٌ للقياسِ لم تُجمَعْ، فلا يُدَّعى صدقُ رقمِها.

## حدُّ الأداةِ المُعلَنُ
1. **النطاقُ المقروءُ مُعلَنٌ بمسارِه** لا بنثرٍ (`DISC-042`): [`docs/PROJECT_HANDBOOK.md`]
   وحدَه. فرقمٌ من جنسِه في ملفٍّ آخرَ لا يُرى هنا — وذاكَ حدٌّ مكتوبٌ لا مطويٌّ،
   ووسعُ النطاقِ يوجِبُ إضافةَ المسارِ صراحةً.
2. **المجموعُ هو المقيسُ**: الجمعُ الحيُّ يُعطي عددَ المُجمَّعِ (نجاحًا وتخطّيًا)،
   فيُقارَنُ بـ«N نجحَت + M مُتخطّاة». ولا يُقاسُ هنا **نجاحُ** الحزمةِ ولا زمنُها:
   حزمةٌ صحيحةُ العددِ قد تفشلُ — وذاكَ تقيسُه CI لا هذا الملفُّ.
3. **حزمةٌ غيرُ مُثبَّتةٍ تُعلَنُ ولا تُطوى**: بيئةٌ لا تحملُ حزمةَ الخدماتِ
   (‏وظيفةُ بوّاباتِ الحوكمةِ في CI منها) لا تجمعُها، فيُطبَعُ «غيرُ مقيسٍ هنا»
   بسببِه المكتوبِ في السجلِّ ولا يُدَّعى صدقٌ لم يُقَسْ. والغيابُ يُقاسُ
   بالاستيرادِ (`probe`) لا بابتلاعِ فشلِ جمعٍ — فحزمةٌ **مُثبَّتةٌ** لا تُجمَعُ
   إخفاقٌ مُسمًّى (`SUITE_UNCOLLECTABLE`) لا إعفاءٌ.
4. **التاريخيُّ يُعفى بإعلانٍ لا بصمتٍ**: سطرُ سلسلةِ القيودِ («تاريخ آخر تعديل»)
   ورقمٌ مُعلَنٌ «إحالةٌ لا قياسي» يُقرآنِ تاريخًا، ويُشترَطُ فيهما قيدٌ ينسِبُهما.

الاستخدام:
    python tools/governance/suite_size_inventory.py --check
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
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

#: النطاقُ المقروءُ — مسارٌ مُعلَنٌ صراحةً لا نثرٌ يُفسَّرُ (`DISC-042`).
CLAIM_PATHS = (Path("docs/PROJECT_HANDBOOK.md"),)

#: كم سطرًا يُنظَرُ إلى الوراءِ لنسبةِ الرقمِ إلى حزمتِه — النسبةُ تُقرأُ لا تُخمَّنُ.
ATTRIBUTION_LOOKBACK = 4

_TASHKEEL = {chr(c) for c in range(0x064B, 0x0653)} | {"\u0640", "\u0670"}

#: «N نجحَت» — كلُّ ظهورٍ لهذه الصيغةِ في النطاقِ يُصنَّفُ، ولا يُتخطّى واحدٌ بصمتٍ.
CLAIM_RE = re.compile(r"(\d+)\s*نجحت")

#: «M مُتخطّاة» على سطرِ الدعوى نفسِه — بها وحدَها يُقرأُ المجموعُ.
SKIPPED_RE = re.compile(r"(\d+)\s*متخطاة")

#: سطرُ سلسلةِ القيودِ في الترويسةِ — رقمٌ فيه روايةٌ عن قيدٍ لا دعوى حاضرةٍ.
RECORD_CHAIN_RE = re.compile(r"^\s*تاريخ آخر تعديل\s*:")

#: إعلانٌ صريحٌ أنَّ الرقمَ منقولٌ لا مقيسٌ هنا.
HISTORICAL_MARKER = "إحالة لا قياسي"

#: عباراتٌ تُعلِنُ أنَّ الرقمَ **التالِيَ لها** روايةٌ عن مكتوبٍ سابقٍ لا دعوى حاضرةٌ.
#: وتُقرأُ في نافذةٍ قصيرةٍ قبلَ الرقمِ، فسطرٌ واحدٌ قد يحملُ مقيسًا وماضيًا معًا.
INLINE_HISTORICAL_MARKERS = ("كان المكتوب", "المكتوب قبله", HISTORICAL_MARKER)

#: طولُ النافذةِ المقروءةِ قبلَ الرقمِ — إعلانٌ قريبٌ لا تفسيرٌ بعيدٌ.
INLINE_MARKER_WINDOW = 80

#: القيدُ الذي يَنسِبُ الرقمَ التاريخيَّ — بلا قيدٍ لا يُعفى رقمٌ.
RECORD_ID_RE = re.compile(r"\bW-\d+\b")


class SuiteCollectionFailed(RuntimeError):
    """يُرفَعُ حينَ لا تُجمَعُ حزمةٌ مُعلَنةٌ — ولا يُفترَضُ رقمٌ مكانَ القياسِ.

    الابتلاعُ الصامتُ هنا **إخفاءُ فشلٍ**: حزمةٌ لا تُجمَعُ تُقرَأُ «لا مخالفةَ»
    فيمرُّ الرقمُ المَيّتُ. فيُعلَنُ العَطبُ ويُسقِطُ الفحصَ.
    """


class ClaimPathMissing(RuntimeError):
    """يُرفَعُ حينَ يغيبُ مسارٌ مُعلَنٌ في النطاقِ — نطاقٌ ناقصٌ لا يُقاسُ عليه."""


def normalize(text: str) -> str:
    """يُجرِّدُ التشكيلَ — الدعوى تُقرأُ بمعناها لا بشكلِ حركاتِها."""
    return "".join(
        ch for ch in unicodedata.normalize("NFC", text) if ch not in _TASHKEEL
    )


class Suite:
    """حزمةٌ مُعلَنةٌ: اسمُها · هدفُ الجمعِ · بيئتُها · علامةُ نَسَبِها في النصِّ."""

    def __init__(
        self,
        key: str,
        target: str,
        marker: str,
        env: dict[str, str] | None = None,
        probe: str | None = None,
        unmeasured_reason: str = "",
    ) -> None:
        self.key = key
        self.target = target
        self.marker = normalize(marker)
        self.env = env or {}
        #: وحدةٌ يلزمُ استيرادُها لتُجمَعَ الحزمةُ — بها يُفرَّقُ «غيرُ مُثبَّتةٍ» عن «معطوبةٍ».
        self.probe = probe
        #: سببٌ مكتوبٌ يُعلَنُ حينَ تغيبُ الحزمةُ — إعفاءٌ مكتوبٌ لا صمتٌ.
        self.unmeasured_reason = unmeasured_reason

    def installed(self) -> bool:
        """أمُثبَّتةٌ حزمتُها في هذه البيئةِ؟ — يُقاسُ بالاستيرادِ لا بالظنِّ."""
        if self.probe is None:
            return True
        return importlib.util.find_spec(self.probe) is not None


#: الحزمُ المُعلَنةُ — تُعَدُّ صراحةً، ولا تُكتشَفُ حزمةٌ بالتقديرِ.
SUITES: tuple[Suite, ...] = (
    Suite(key="root", target="tests/", marker="حزمةُ الجذر"),
    Suite(
        key="services",
        target="federal/executive/services/tests",
        marker="حزمةُ الخدمات",
        env={"AMOS_DATABASE_URL": "sqlite:///{tmp}/amos_suite_size.db"},
        probe="amos_federation",
        unmeasured_reason=(
            "حزمةُ الخدماتِ غيرُ مُثبَّتةٍ في هذه البيئةِ (‏`pip install -e "
            '"federal/executive/services[dev]"`) — ووظيفةُ بوّاباتِ الحوكمةِ في CI '
            "لا تُثبِّتُها. فيُعلَنُ أنَّ رقمَها **غيرُ مقيسٍ هنا** ويبقى إنفاذُه "
            "محلّيًّا وفي وظيفةِ `test` ذاتِ التبعيّاتِ الكاملةِ"
        ),
    ),
)

_COLLECTED_RE = re.compile(r"(\d+)\s+tests?\s+collected")
_NO_TESTS_RE = re.compile(r"no tests ran|collected 0 items")


def collect_size(suite: Suite, repo: Path | None = None) -> int:
    """عددُ ما تجمعُه الحزمةُ حيًّا — يُشغَّلُ `pytest --collect-only` ويُقرأُ خرجُه."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    with tempfile.TemporaryDirectory(prefix="amos-suite-size-") as tmp:
        merged = os.environ.copy()
        merged.update({k: v.format(tmp=tmp) for k, v in suite.env.items()})
        completed = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                suite.target,
                "-q",
                "--collect-only",
                "-p",
                "no:cacheprovider",
            ],
            cwd=repo,
            env=merged,
            capture_output=True,
            text=True,
        )
    if completed.returncode != 0:
        raise SuiteCollectionFailed(
            f"SUITE_UNCOLLECTABLE · {suite.key} ({suite.target}) — رمزُ الخروجِ "
            f"{completed.returncode}. آخرُ الخرجِ: "
            f"{(completed.stdout or completed.stderr).strip()[-400:]}"
        )
    matches = _COLLECTED_RE.findall(completed.stdout)
    if not matches:
        raise SuiteCollectionFailed(
            f"SUITE_UNCOLLECTABLE · {suite.key} ({suite.target}) — لم يُقرأْ عددُ "
            "المُجمَّعِ من خرجِ `pytest --collect-only`، فلا يُخمَّنُ رقمٌ"
        )
    return int(matches[-1])


class Claim:
    """دعوى حجمٍ مكتوبةٌ: موضعُها · نصُّها · تصنيفُها · عددُها إن قُرِئَ."""

    def __init__(
        self,
        path: str,
        line_number: int,
        line: str,
        kind: str,
        suite: str | None = None,
        written_total: int | None = None,
        passed: int | None = None,
        skipped: int | None = None,
        paragraph: str = "",
    ) -> None:
        self.paragraph = paragraph or line
        self.path = path
        self.line_number = line_number
        self.line = line
        self.kind = kind
        self.suite = suite
        self.written_total = written_total
        self.passed = passed
        self.skipped = skipped

    #: فقرةُ الدعوى — سطرُها وما يليهِ حتّى أوّلِ سطرٍ فارغٍ (‏نَسَبُ التاريخيِّ يُقرأُ فيها).
    paragraph: str = ""

    @property
    def where(self) -> str:
        return f"{self.path}:{self.line_number}"

    def to_dict(self) -> dict[str, object]:
        return {
            "path": self.path,
            "line": self.line_number,
            "kind": self.kind,
            "suite": self.suite,
            "written_total": self.written_total,
            "passed": self.passed,
            "skipped": self.skipped,
        }


#: كم سطرًا تمتدُّ فقرةُ الدعوى — نَسَبُ الرقمِ التاريخيِّ قد يقعُ في سطرٍ تالٍ.
PARAGRAPH_SPAN = 4


def _paragraph(lines: list[str], index: int) -> str:
    """سطرُ الدعوى وما يليهِ حتّى أوّلِ سطرٍ فارغٍ — الفقرةُ تُقرأُ كما كُتِبَت."""
    collected = [lines[index]]
    for cursor in range(index + 1, min(index + 1 + PARAGRAPH_SPAN, len(lines))):
        if not lines[cursor].strip():
            break
        collected.append(lines[cursor])
    return "\n".join(collected)


def _attributed_suite(lines: list[str], index: int) -> Suite | None:
    """أقربُ علامةِ حزمةٍ على السطرِ أو فوقَه — النسَبُ يُقرأُ من النصِّ."""
    for offset in range(0, ATTRIBUTION_LOOKBACK + 1):
        cursor = index - offset
        if cursor < 0:
            break
        plain = normalize(lines[cursor])
        for suite in SUITES:
            if suite.marker in plain:
                return suite
    return None


def claims(repo: Path | None = None) -> list[Claim]:
    """كلُّ دعوى «N نجحَت» في النطاقِ المُعلَنِ، مُصنَّفةً — لا يُتخطّى ظهورٌ بصمتٍ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    found: list[Claim] = []
    for relative in CLAIM_PATHS:
        path = repo / relative
        if not path.is_file():
            raise ClaimPathMissing(
                f"مسارٌ مُعلَنٌ في النطاقِ غيرُ موجودٍ: {relative} — "
                "النطاقُ يُصحَّحُ ولا يُتجاوَزُ الحرسُ"
            )
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, raw in enumerate(lines):
            plain = normalize(raw)
            for match in CLAIM_RE.finditer(plain):
                passed = int(match.group(1))
                prefix = plain[max(0, match.start() - INLINE_MARKER_WINDOW) : match.start()]
                if RECORD_CHAIN_RE.match(plain):
                    kind = "HISTORICAL_RECORD_CHAIN"
                elif any(marker in prefix for marker in INLINE_HISTORICAL_MARKERS):
                    kind = "HISTORICAL_DECLARED"
                else:
                    kind = "LIVE"
                if kind != "LIVE":
                    found.append(
                        Claim(
                            path=str(relative),
                            line_number=index + 1,
                            line=raw,
                            kind=kind,
                            passed=passed,
                            paragraph=_paragraph(lines, index),
                        )
                    )
                    continue
                skipped_match = SKIPPED_RE.search(plain, match.end())
                skipped = int(skipped_match.group(1)) if skipped_match else None
                suite = _attributed_suite(lines, index)
                found.append(
                    Claim(
                        path=str(relative),
                        line_number=index + 1,
                        line=raw,
                        kind=kind,
                        suite=suite.key if suite else None,
                        written_total=(
                            passed + skipped if skipped is not None else None
                        ),
                        passed=passed,
                        skipped=skipped,
                    )
                )
    return found


def measure(repo: Path | None = None) -> dict[str, object]:
    """المقيسُ: أحجامُ الحزمِ حيًّا · الدعاوى المصنَّفةُ — يُعادُ من النصِّ لا من ذاكرةٍ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    written = claims(repo)
    needed = needed_suites(written)
    unmeasured = unmeasured_suites(needed)
    sizes = {
        s.key: collect_size(s, repo)
        for s in SUITES
        if s.key in needed and s.key not in unmeasured
    }
    return {
        "collected": sizes,
        "unmeasured": sorted(unmeasured),
        "claims": [c.to_dict() for c in written],
    }


def needed_suites(written: list[Claim]) -> set[str]:
    """الحزمُ التي يلزمُ جمعُها — ما نُسِبَ إليه رقمٌ حيٌّ لا غيرُ."""
    return {c.suite for c in written if c.kind == "LIVE" and c.suite is not None}


def unmeasured_suites(needed: set[str]) -> frozenset[str]:
    """الحزمُ المُعلَنُ غيابُها في هذه البيئةِ — إعفاءٌ بسببٍ مكتوبٍ لا بتخطٍّ صامتٍ."""
    return frozenset(
        s.key for s in SUITES if s.key in needed and not s.installed()
    )


def judge(
    written: list[Claim],
    sizes: dict[str, int],
    unmeasured: frozenset[str] = frozenset(),
) -> list[str]:
    """الحكمُ على دعاوى مقروءةٍ وأحجامٍ مقيسةٍ — دالّةٌ خالصةٌ تُجرَّبُ بإعادةِ العَطبِ.

    و`unmeasured` حزمٌ **مُعلَنٌ** غيابُها بسببٍ مكتوبٍ في السجلِّ: دعاواها تُطبَعُ
    ظاهرةً ولا يُحكَمُ عليها هنا، فلا يُدَّعى صدقٌ لم يُقَسْ ولا يُصطنَعُ إخفاقٌ
    سببُه البيئةُ. وإنفاذُها يبقى حيثُ تُثبَّتُ حزمتُها.
    """
    problems: list[str] = []

    for claim in written:
        if claim.kind != "LIVE":
            if not RECORD_ID_RE.search(claim.paragraph):
                problems.append(
                    f"UNDATED_HISTORICAL_CLAIM · {claim.where} — رقمٌ مُعلَنٌ تاريخيًّا "
                    "بلا قيدٍ يَنسِبُه، فلا يُفرَّقُ عن دعوى حاضرةٍ"
                )
            continue
        if claim.suite is None:
            problems.append(
                f"UNATTRIBUTED_SUITE_CLAIM · {claim.where} — رقمُ حزمةٍ لا تُعرَفُ "
                "حزمتُه، فلا يُقاسُ صدقُه"
            )
            continue
        if claim.written_total is None:
            problems.append(
                f"UNREADABLE_CLAIM_SHAPE · {claim.where} — «{claim.passed} نجحَت» "
                "بلا «مُتخطّاة» على سطرِها، فالمجموعُ لا يُقرأُ"
            )

    for claim in written:
        if claim.kind != "LIVE" or claim.suite is None or claim.written_total is None:
            continue
        if claim.suite in unmeasured:
            continue
        if claim.suite not in sizes:
            problems.append(
                f"SUITE_UNCOLLECTABLE · {claim.where} · {claim.suite} — رقمٌ مكتوبٌ "
                "لحزمةٍ لم تُجمَعْ، فلا يُدَّعى صدقُه ولا يُمرَّرُ بصمتٍ"
            )
            continue
        live = sizes[claim.suite]
        if claim.written_total != live:
            problems.append(
                f"STALE_SUITE_CLAIM · {claim.where} · {claim.suite} — المكتوبُ "
                f"{claim.passed}+{claim.skipped}={claim.written_total} · "
                f"المجموعُ حيًّا {live} — يُعادُ القياسُ ويُكتَبُ المقيسُ بتاريخِه، "
                "ولا يُحذَفُ الرقمُ ليمرَّ الفحصُ"
            )
    return problems


def verdict(repo: Path | None = None) -> tuple[int, list[str]]:
    """الحكمُ ورسائلُه — رمزُ خروجٍ يُقاسُ لا تقريرٌ يُقرَأُ."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    written = claims(repo)
    needed = needed_suites(written)
    unmeasured = unmeasured_suites(needed)
    sizes = {
        s.key: collect_size(s, repo)
        for s in SUITES
        if s.key in needed and s.key not in unmeasured
    }
    problems = judge(written, sizes, unmeasured)
    return (1 if problems else 0), problems


def main() -> int:
    parser = argparse.ArgumentParser(description="قياسُ صدقِ أحجامِ الحزمِ المكتوبةِ")
    parser.add_argument("--check", action="store_true", help="يقيسُ ويحكُمُ برمزِ خروجٍ")
    parser.add_argument("--json", action="store_true", help="يطبعُ المقيسَ خامًا")
    parser.add_argument(
        "--repo-root",
        default=None,
        help="جذرُ القياسِ صريحًا — يُقاسُ ما يُقالُ لا ما يُخمَّنُ (`DISC-032`)",
    )
    args = parser.parse_args()
    repo = Path(args.repo_root).resolve() if args.repo_root else REPO_ROOT

    if args.json:
        print(json.dumps(measure(repo), ensure_ascii=False, indent=2))
        return 0

    code, problems = verdict(repo)
    written = claims(repo)
    live = [c for c in written if c.kind == "LIVE"]
    print(
        f"SUITE SIZE: {len(written)} دعوى مقروءةً · {len(live)} حيّةً · "
        f"{len(written) - len(live)} مُعلَنةً تاريخيّةً"
    )
    for suite in SUITES:
        if suite.key in unmeasured_suites(needed_suites(written)):
            print(f"  ! غيرُ مقيسٍ هنا · {suite.key} — {suite.unmeasured_reason}")
    for problem in problems:
        print(f"  ✗ {problem}")
    if not problems:
        print("  ✓ لا مخالفةَ مقيسةً: كلُّ رقمِ حزمةٍ مكتوبٍ يُطابِقُ الجمعَ الحيَّ.")
    return code if args.check else 0


if __name__ == "__main__":
    raise SystemExit(main())
