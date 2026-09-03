"""
حرسُ شهادةِ الأثرِ — أثرٌ يشهدُ على نقصِ بيئتِه، فتُقرأُ شهادتُه
الهدف: قراءةُ **شهادةِ التوليدِ** التي يكتُبُها الأثرُ المُولَّدُ في متنِه (‏زمنُ التوليدِ · حالُ بيئةِ القياسِ · حالُ كلِّ حزمةٍ)، ورفضُ أثرٍ **مُقيَّدٍ في الشجرةِ** يُعلِنُ بلسانِه أنَّ قياسَه جرى في بيئةٍ ناقصةٍ أو أنَّ حزمةً سقطَت — ومنعُ حذفِ الشهادةِ هربًا من قراءتِها.
طريقُ الإنفاذ: COVERED_TEST · tests/governance/test_w131_artifact_witness_integrity.py يحكُمُ على الشجرةِ الحاضرةِ (‏`test_real_tree_check_passes`) ويشملُه استدعاءُ `pytest` في CI
النطاق: tools/governance/ — قارئٌ للأثرِ المُقيَّدِ لا مُعدِّلٌ له ولا لمُولِّدِه
المالك: tools/governance/
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03

العَطبُ المقيسُ (`DISC-054`) — حدَثَ فعلًا لا فرضًا:
    في `W-130` أعادَ تشغيلُ `verify_cross_system_suites.py` بلا وسائطَ توليدَ
    `docs/audit/CROSS_SYSTEM_SUITE_MATRIX.md` في بيئةٍ **ناقصةِ التبعيّاتِ**، فصارَ
    متنُ الوثيقةِ المُقيَّدةِ يقولُ `root-core` **FAIL** و`services-sqlite` **0/0/0
    FAIL** و«بيئةُ PostgreSQL … **غائبة**» بدلًا من المقيسِ الكاملِ في الفرعِ. ثمَّ
    بقيَ رمزُ خروجِ **كلِّ** بوّاباتِ § 5.4 صفرًا — بما فيها بوّابةُ طزاجةِ الأثرِ
    المُولَّدِ — ولم تُقَسْ المخالفةُ إلّا بمقارنةِ بايتاتِ الملفِّ بنسخةِ الفرعِ يدويًّا.

    فالوثيقةُ المُولَّدةُ تقولُ عن نفسِها «تحريرُها يدويًّا لا يُغيِّرُ شيئًا في
    الواقعِ» — وهي محقّةٌ: **الخطرُ ليسَ التحريرَ بل التوليدَ الناقصَ**. والإعفاءُ من
    حرسِ التحريرِ اليدويِّ صارَ إعفاءً من الحرسِ كلِّه.

    وهذا **جنسٌ أوسعُ** من `DISC-053`: هناكَ الخُضرةُ لا تقولُ كم قرأَت، وهنا الأثرُ
    **يقولُ إنَّه لم يقرأْ** ولا يُصدِّقُه أحدٌ.

حدُّ الحرسِ — مُعلَنٌ لا مطويٌّ:
    - **الشهادةُ تُقرأُ نصًّا**: أثرٌ يُعلِنُ نقصَه بصيغةٍ غيرِ مُدرَجةٍ يُفلِتُ حتّى
      تُدرَجَ صيغتُه. والصيغُ المُدرَجةُ أدناه في `WITNESS_MARKERS` و`DEFICIENCY_MARKS`،
      ويُصحَّحُ الحدُّ **بإضافةِ صيغةٍ** لا بتخفيفِ السقّاطةِ.
    - **ولا يُقاسُ صدقُ الأرقامِ** في الأثرِ: يُقاسُ أنَّ الأثرَ **لا يشهدُ على نفسِه
      بالنقصِ**. فأثرٌ وُلِّدَ في بيئةٍ كاملةٍ بأرقامٍ خاطئةٍ يمرُّ — وذاكَ حدٌّ من جنسِ
      كلِّ حرسٍ يقرأُ إعلانًا لا يُعيدُ القياسَ.
    - **ولا يُمنَعُ التوليدُ الناقصُ** أصلًا: يُمنَعُ **قيدُه في الشجرةِ**. والمنعُ في
      المُولِّدِ نفسِه بندٌ آخرُ في مسارٍ مُدَّعًى (§ 6.1).
    - **وعددُ الشاهدينَ أرضٌ لا تنزلُ**: حذفُ شهادةِ التوليدِ من وثيقةٍ هربًا من
      قراءتِها يُسقِطُ الوجهَ كما يُسقِطُه النقصُ نفسُه.
    - **والرقمُ لا يسكنُ الأداةَ**: يُقرأُ من سطرِ `ARTIFACT_WITNESS_BASELINE:` في قيدِ
      `DISC-054`، فمصدرُ الحقيقةِ واحدٌ وتعليتُه تمرُّ بالسجلِّ المراجَعِ.
"""

from __future__ import annotations

import argparse
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

#: موضعُ الآثارِ المُقيَّدةِ المقروءةِ — بالاسمِ لا بالتقديرِ.
DOCS_DIR = Path("docs")

#: موضعُ الرقمِ المُعلَنِ — سطرٌ واحدٌ لا ثابتٌ في أداةٍ.
BASELINE_RECORD = Path("docs/governance/work/DISCOVERIES.md")
BASELINE_MARKER = "ARTIFACT_WITNESS_BASELINE:"
BASELINE_FIELDS = ("witnessing", "degraded")

#: ما يجعلُ الوثيقةَ **شاهدةً على شروطِ قياسِها** — صيغٌ مُدرَجةٌ مُعلَنةٌ.
WITNESS_MARKERS: tuple[str, ...] = ("آخر توليد:", "لحظة التوليد")

#: ما تشهدُ به الوثيقةُ على **نقصِ** قياسِها — صيغٌ مُدرَجةٌ مُعلَنةٌ.
DEFICIENCY_MARKS: tuple[str, ...] = ("**غائبة**", "**FAIL**", "**SKIPPED**")

#: أثرٌ مُقيَّدٌ يشهدُ على نقصِ بيئتِه أو سقوطِ حزمةٍ.
DEGRADED = "DEGRADED"
#: أثرٌ شاهدٌ لا يُعلِنُ نقصًا.
SOUND = "SOUND"


class BaselineRecordMissing(RuntimeError):
    """سطرُ الرقمِ المُعلَنِ غائبٌ أو مكرَّرٌ أو ناقصُ حقولٍ — يُرفَعُ ولا يُبتلَعُ."""


class ArtifactUnreadable(RuntimeError):
    """أثرٌ لا يُقرأُ — يُرفَعُ ولا يُقرأُ «سليمًا» بصمتٍ."""


class Witness(NamedTuple):
    """شهادةُ أثرٍ مُقيَّدٍ، مقروءةً."""

    path: str
    verdict: str
    marks: tuple[str, ...]

    def __str__(self) -> str:  # pragma: no cover - للتقريرِ لا للحكمِ
        return self.path


def _read(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise ArtifactUnreadable(
            f"تعذَّرَ قراءةُ الأثرِ {label} فلا يُقرأُ سليمًا ولا يُتخطّى: {exc}"
        ) from exc


def witnesses(root: Path) -> list[Witness]:
    """كلُّ أثرٍ مُقيَّدٍ تحتَ `docs/` يشهدُ على شروطِ قياسِه — مقروءًا لا مُقدَّرًا."""
    found: list[Witness] = []
    for path in sorted((root / DOCS_DIR).rglob("*.md")):
        label = path.relative_to(root).as_posix()
        text = _read(path, label)
        if not any(marker in text for marker in WITNESS_MARKERS):
            continue
        marks = tuple(mark for mark in DEFICIENCY_MARKS if mark in text)
        found.append(
            Witness(label, DEGRADED if marks else SOUND, marks)
        )
    return found


def degraded_artifacts(root: Path) -> list[Witness]:
    """الآثارُ التي تشهدُ على نقصِها — تُسمّى بموضعِها لا بعددِها وحدَه."""
    return [w for w in witnesses(root) if w.verdict == DEGRADED]


def measured_counts(root: Path) -> dict[str, int]:
    """الرقمانِ المقيسانِ — يُقارَنانِ بالمُعلَنِ حرفًا بحرفٍ."""
    read = witnesses(root)
    return {
        "witnessing": len(read),
        "degraded": sum(1 for w in read if w.verdict == DEGRADED),
    }


def declared_baseline(root: Path) -> dict[str, int]:
    """يقرأُ الرقمَ المُعلَنَ من قيدِ `DISC-054` — ولا يُخترَعُ رقمٌ في الأداةِ."""
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
    """السقّاطتانِ — كلٌّ باسمِها لا برمزٍ عامٍّ."""
    measured = measured_counts(root)
    declared = declared_baseline(root)
    problems: list[str] = []

    if measured["degraded"] > declared["degraded"]:
        named = "\n    ".join(
            f"{w.path} · شهادتُه: {' · '.join(w.marks)}"
            for w in degraded_artifacts(root)
        )
        problems.append(
            "DEGRADED_ARTIFACT_COMMITTED: أثرٌ مُقيَّدٌ يشهدُ بلسانِه أنَّ قياسَه ناقصٌ — "
            f"مقيسٌ {measured['degraded']} · المُعلَنُ {declared['degraded']}. "
            "يُعادُ توليدُه في بيئةٍ تملكُ ما يقيسُه أو تُسترجَعُ نسختُه المقيسةُ، "
            "ولا تُحذَفُ شهادتُه ولا يُرفَعُ الرقمُ:\n    " + named
        )

    if measured["witnessing"] != declared["witnessing"]:
        problems.append(
            "WITNESS_COUNT_UNDECLARED: عددُ الآثارِ الشاهدةِ لا يُطابِقُ المُعلَنَ — "
            f"مقيسٌ {measured['witnessing']} · المُعلَنُ {declared['witnessing']}: "
            "نقصانُه حذفُ شهادةٍ (‏هربٌ من القراءةِ لا إصلاحٌ)، وزيادتُه أثرٌ شاهدٌ "
            "جديدٌ يُقيَّدُ — وكلاهما يُصحَّحُ في القيدِ لا في الأداةِ"
        )

    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="حرسُ شهادةِ الأثرِ: أثرٌ يشهدُ على نقصِ بيئتِه لا يُقيَّدُ في الشجرةِ"
    )
    parser.add_argument("root", nargs="?", default=str(REPO_ROOT))
    parser.add_argument(
        "--check", action="store_true", help="يُسقِطُ إن شهدَ أثرٌ بنقصٍ أو حُذِفَت شهادةٌ"
    )
    parser.add_argument("--json", action="store_true", help="القياسُ كاملًا مُهيكَلًا")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if args.json:
        print(
            json.dumps(
                {
                    "measured": measured_counts(root),
                    "declared": declared_baseline(root),
                    "witnesses": [w._asdict() for w in witnesses(root)],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    read = witnesses(root)
    measured = measured_counts(root)
    print(
        "[ARTIFACT WITNESS] شهادةُ الأثرِ تُقرأُ لا تُفترَضُ: "
        f"آثارٌ شاهدةٌ {measured['witnessing']} · تشهدُ بنقصٍ {measured['degraded']}"
    )
    for witness in read:
        state = "يشهدُ بنقصٍ" if witness.verdict == DEGRADED else "لا يشهدُ بنقصٍ"
        detail = f" · {' · '.join(witness.marks)}" if witness.marks else ""
        print(f"  {state} · {witness.path}{detail}")

    if not args.check:
        return 0

    problems = verdicts(root)
    if problems:
        print(f"[ARTIFACT WITNESS] ✗ مخالفات: {len(problems)}", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print(
        f"[ARTIFACT WITNESS] ✓ كلُّ ما قُرِئَ لا يشهدُ بنقصٍ: "
        f"{measured['witnessing']} أثرًا شاهدًا · {measured['degraded']} تشهدُ بنقصٍ"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
