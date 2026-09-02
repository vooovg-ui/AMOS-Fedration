"""
حرسُ نسَبِ محلِّ القياسِ — جذرُ المستودعِ يُعرَفُ بعلامةٍ أو بعلمٍ صريحٍ، لا بعُمقٍ مكتوبٍ
الهدف: إحصاءُ كلِّ وحدةٍ تحتَ `tools/` و`tests/` تُشتَقُّ فيها جذرُ المستودعِ من `__file__` بعُمقٍ ثابتٍ (`parents[N]`)، وتمييزُ ما لا يقبلُ جذرًا صريحًا ألبتّةَ، ومنعُ نموِّ الرقمَينِ — فالسببُ الأعمقُ لـ`DISC-032` مقيسٌ لا مرويٌّ.
النطاق: tests/governance/ — قارئٌ تركيبيٌّ لا يُعدِّلُ أداةً ولا يُدَّعى ملكًا على مسارٍ محجوزٍ
المالك: tests/governance/
تاريخ الإنشاء: 2026-09-02
تاريخ آخر تعديل: 2026-09-02

العَطبُ المقيسُ (`DISC-032` · سببُه الأعمقُ · `DISC-041`):
    `REPO_ROOT = Path(__file__).resolve().parents[2]` يُثبِّتُ محلَّ القياسِ **بعُمقٍ
    مكتوبٍ** لا بعلامةٍ. فإن نُقِلَ الملفُّ أو أُعيدَ تنظيمُ المجلَّداتِ صارَ الجذرُ
    مجلَّدًا آخرَ **بلا أيِّ خطأٍ**: البوّابةُ تُشغَّلُ، وتقرأُ شجرةً غيرَ التي يُظَنُّ
    أنَّها تُقرأُ، وتُخرِجُ رمزَ صفرٍ. وهذا عينُ عائلةِ `DISC-032` («فحصٌ يحكُمُ على
    شجرةٍ لا يقرؤها») لكن في **الأدواتِ** لا في الفحوصِ.

لماذا سقّاطةٌ لا إصلاحٌ شاملٌ في هذا البندِ:
    إصلاحُ النمطِ يمسُّ عشراتِ الأدواتِ، ومنها مساراتٌ **مُدَّعاةٌ لبنودٍ في يدِ
    المراجعِ** (`WI-023`…`WI-030`) — فالمسُّ الشاملُ الآنَ يُصادِمُ الدعاوى (§ 6.1)
    ويُخرِجُ حجمَ التغييرِ عن حدِّ بندٍ واحدٍ. فالمُستطاعُ بلا مصادمةٍ: **أن يصيرَ
    الدَّينُ مقيسًا برقمٍ لا يعلو** — ثمَّ يُنزَلُ رقمًا رقمًا حينَ تنفكُّ الدعاوى.
    والسقّاطةُ تمنعُ النموَّ ولا تُبيحُ القائمَ: `EXPECTED_DEPTH_ONLY` رقمُ دَينٍ مُعلَنٍ.

حدُّ الحرسِ — مُعلَنٌ لا مطويٌّ:
    - يقرأُ `tools/` و`tests/` وحدَهما؛ ووحداتُ `core/` وغيرِها تُحصى إبلاغًا لا إسقاطًا.
    - **الحرسُ يُحصي نفسَه**: إسنادُ `REPO_ROOT` في هذا الملفِّ داخلٌ في الرقمِ (‏صنفُ
      «يقبلُ جذرًا صريحًا»)، فرقمُ `tests` **53** يشملُه، و**52** قبلَ نزولِه. ولا
      يُستثنى الحرسُ من حكمِه: قارئٌ يُعفي نفسَه يُعلِّمُ الإعفاءَ.
    - **والرقمُ لا يسكنُ الفحصَ**: يُقرأُ من سطرِ `ROOT_PROVENANCE_BASELINE:` في قيدِ
      `DISC-041`، فمصدرُ الحقيقةِ واحدٌ، وتعليتُه تمرُّ بالسجلِّ المراجَعِ لا بثابتٍ.
    - «العلامةُ» تُقرأُ تركيبيًّا: صعودٌ حتّى ملفٍّ دالٍّ، أو عَلَمٌ/مُعامِلٌ يُمرِّرُ الجذرَ.
      فوحدةٌ تفعلُ ذلك بأسلوبٍ لا يُشبِهُ المقروءَ تُقرأُ `DEPTH_ONLY` — وهذا **يُشدِّدُ**
      ولا يُرخي، ويُصحَّحُ بإعلانٍ لا بتخفيفٍ.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import NamedTuple

REPO_ROOT = Path(__file__).resolve().parents[2]

#: أسماءٌ تُستعمَلُ جذرًا للقياسِ.
ROOT_NAMES = frozenset({"REPO_ROOT", "PROJECT_ROOT", "ROOT", "REPO", "TREE_ROOT"})

#: ما يدلُّ على أنَّ الجذرَ يُعرَفُ بعلامةٍ أو بعلمٍ صريحٍ لا بعُمقٍ وحدَه.
MARKERS = (
    "THE_ROADMAP.md",
    "PROJECT_STATE.md",
    "pyproject.toml",
    '".git"',
    "'.git'",
    "--repo-root",
    "--root",
    "--tree",
    "argparse",
    "sys.argv",
    "_discover_root",
    "find_root",
    "repo_root(",
)

#: الأسوأُ: جذرٌ من عُمقٍ ثابتٍ **ولا وجهَ** يُمرِّرُ غيرَه.
DEPTH_NO_OVERRIDE = "DEPTH_ONLY_NO_OVERRIDE"
#: أقلُّ سوءًا: الجذرُ من عُمقٍ ثابتٍ لكنَّ الوحدةَ تقبلُ جذرًا صريحًا.
DEPTH_WITH_OVERRIDE = "DEPTH_WITH_EXPLICIT_OVERRIDE"

#: الدَّينُ المُعلَنُ **لا يُكتَبُ هنا**: يُقرأُ من قيدِ `DISC-041` في سجلِّ الاكتشافاتِ،
#: فمصدرُ الحقيقةِ واحدٌ لا اثنانِ، وتعليتُه تمرُّ بالقيدِ لا بثابتٍ في فحصٍ.
BASELINE_RECORD = "docs/governance/work/DISCOVERIES.md"
BASELINE_MARKER = "ROOT_PROVENANCE_BASELINE:"


class Unit(NamedTuple):
    """وحدةٌ تُشتَقُّ فيها جذرُ القياسِ، مُصنَّفةً."""

    path: str
    line: int
    verdict: str

    def __str__(self) -> str:  # pragma: no cover - للتقريرِ لا للحكمِ
        return f"{self.path}:{self.line}"


def _classify(source: str, label: str) -> list[Unit]:
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:  # ملفٌّ لا يُحلَّلُ يُرفَعُ صوتُه، ولا يُبتلَعُ
        raise AssertionError(
            f"تعذَّرَ تحليلُ {label} تركيبيًّا فلا يُحكَمُ عليه ولا يُطوى: {exc}"
        ) from exc

    anchored_module = any(marker in source for marker in MARKERS)
    units: list[Unit] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        value = ast.unparse(node.value)
        if "__file__" not in value or "parent" not in value:
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ROOT_NAMES:
                verdict = DEPTH_WITH_OVERRIDE if anchored_module else DEPTH_NO_OVERRIDE
                units.append(Unit(label, node.lineno, verdict))
    return units


def declared_baseline() -> dict[str, dict[str, int]]:
    """يقرأُ الدَّينَ المُعلَنَ من قيدِ `DISC-041` — ولا يُخترَعُ رقمٌ في الفحصِ."""
    record = (REPO_ROOT / BASELINE_RECORD).read_text(encoding="utf-8")
    marked = [ln for ln in record.splitlines() if BASELINE_MARKER in ln]
    assert len(marked) == 1, (
        f"سطرُ الدَّينِ المُعلَنِ `{BASELINE_MARKER}` يجبُ أن يكونَ واحدًا في "
        f"{BASELINE_RECORD} — وُجِدَ {len(marked)}: القيدُ مصدرُ الحقيقةِ لا الفحصُ"
    )
    fields = dict(re.findall(r"(\w+)=(\d+)", marked[0].split(BASELINE_MARKER, 1)[1]))
    needed = ("tools", "tests", "tools_no_override", "tests_no_override")
    missing = [k for k in needed if k not in fields]
    assert not missing, f"القيدُ ناقصٌ حقولًا: {missing}"
    return {
        "total": {"tools": int(fields["tools"]), "tests": int(fields["tests"])},
        "no_override": {
            "tools": int(fields["tools_no_override"]),
            "tests": int(fields["tests_no_override"]),
        },
    }


def census(*roots: str) -> list[Unit]:
    """يُحصي وحداتِ الشجرةِ المطلوبةِ — مُرتَّبةً فيُعادُ الرقمُ نفسُه."""
    units: list[Unit] = []
    for root in roots:
        base = REPO_ROOT / root
        for path in sorted(base.rglob("*.py")):
            if ".venv" in path.parts or "site-packages" in path.parts:
                continue
            label = path.relative_to(REPO_ROOT).as_posix()
            units.extend(_classify(path.read_text(encoding="utf-8"), label))
    return units


# ── الحرسُ ───────────────────────────────────────────────────────────────────


def test_دَينُ_الجذرِ_المُثبَّتِ_بعُمقٍ_لا_يعلو() -> None:
    """سقّاطتانِ لا تُبيحانِ القائمَ بل تمنعانِ نموَّه — والرقمُ يُخفَضُ ولا يُعَلَّى."""
    baseline = declared_baseline()
    worst = {
        root: len([u for u in census(root) if u.verdict == DEPTH_NO_OVERRIDE])
        for root in baseline["no_override"]
    }
    total = {root: len(census(root)) for root in baseline["total"]}
    print(
        "ROOT_PROVENANCE: جذرٌ من عُمقٍ ثابتٍ "
        f"{total} · منها بلا وجهٍ يُمرِّرُ غيرَه {worst} · "
        f"الدَّينُ المُعلَنُ في `DISC-041` {baseline}"
    )

    for measured, declared, وصفٌ in (
        (worst, baseline["no_override"], "بلا وجهٍ يُمرِّرُ جذرًا صريحًا"),
        (total, baseline["total"], "جذرٌ مُشتَقٌّ من عُمقٍ ثابتٍ"),
    ):
        grew = {r: (n, declared[r]) for r, n in measured.items() if n > declared[r]}
        assert not grew, (
            f"دَينُ «{وصفٌ}» نما — ولا تُعَلَّى السقّاطةُ: يُعرَفُ الجذرُ بعلامةٍ "
            "(صعودٌ حتّى ملفٍّ دالٍّ) أو بعلمٍ صريحٍ يُمرِّرُه:\n  "
            + "\n  ".join(f"{r}: مقيسٌ {n} · المُعلَنُ {e}" for r, (n, e) in grew.items())
        )
        shrank = {r: (n, declared[r]) for r, n in measured.items() if n < declared[r]}
        assert not shrank, (
            f"دَينُ «{وصفٌ}» انخفضَ — وهذا مطلوبٌ، فيُخفَضُ الرقمُ المُعلَنُ في القيدِ "
            "نفسِه حتّى لا تبقى سقّاطةٌ أرخى من الواقعِ:\n  "
            + "\n  ".join(f"{r}: مقيسٌ {n} · المُعلَنُ {e}" for r, (n, e) in shrank.items())
            + f"\n  ويُخفَضُ في سطرِ `{BASELINE_MARKER}` داخلَ {BASELINE_RECORD}"
        )


def test_الإحصاءُ_يقرأُ_شيئًا_فلا_يُقرأُ_أخضرَ_وهو_أعمى() -> None:
    """قارئٌ يُحصي صفرًا يُقرأُ خضرةً وهو أعمى — فالإحصاءُ نفسُه مقيسٌ."""
    units = census("tools", "tests")
    assert units, "لا وحدةَ أُحصِيَت — القارئُ أعمى لا الشجرةُ نظيفةٌ"
    assert all(u.verdict in (DEPTH_NO_OVERRIDE, DEPTH_WITH_OVERRIDE) for u in units), (
        "صنفٌ ثالثٌ يُخفي وحدةً عن الحكمِ"
    )


def test_القارئُ_يُميِّزُ_العلامةَ_من_العُمقِ() -> None:
    """قياسُ القارئِ نفسِه: يُقرأُ عليه نصّانِ فيُحكَمُ عليهما حكمَينِ مختلفَينِ."""
    depth_only = "from pathlib import Path\nREPO_ROOT = Path(__file__).resolve().parents[2]\n"
    anchored = (
        "import argparse\nfrom pathlib import Path\n"
        "REPO_ROOT = Path(__file__).resolve().parents[2]\n"
        "parser = argparse.ArgumentParser()\nparser.add_argument('--repo-root')\n"
    )
    assert [u.verdict for u in _classify(depth_only, "x.py")] == [DEPTH_NO_OVERRIDE]
    assert [u.verdict for u in _classify(anchored, "y.py")] == [DEPTH_WITH_OVERRIDE]
    assert _classify("VALUE = 1\n", "z.py") == []
