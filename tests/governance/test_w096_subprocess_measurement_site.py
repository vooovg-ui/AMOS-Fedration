"""
الهدف: أن تكونَ دعوى «الفحصُ يقرأُ الشجرةَ التي يُعلِنُها» **مقيسةً بحرسٍ** لا
       مأمولةً بعينٍ: يُحصى كلُّ تشغيلِ أداةٍ في عمليّةٍ فرعيّةٍ داخلَ `tests/`،
       ويُسقِطُ الفحصُ على كلِّ موضعٍ يُمهِّدُ لشجرةٍ مؤقَّتةٍ ثمَّ يحكُمُ على
       غيرِها (‏نمطُ `DISC-032`).
النطاق: `tests/**/*.py` قراءةً تركيبيّةً (AST). لا يُقاسُ هنا صوابُ ما تقيسُه
        الفحوصُ ولا قصدُها — يُقاسُ **محلُّ القياسِ** وحدَه.
المالك: tests-root — بندُ `WI-029`
تاريخ الإنشاء: 2026-09-01
تاريخ آخر تعديل: 2026-09-01 (`W-096` · `WI-029` · `DISC-032`)

حرسٌ يجعلُ «الفحصُ يقرأُ الشجرةَ التي يُعلِنُها» مقيسًا لا مأمولًا — `DISC-032`.

العَطبُ المقيسُ الذي يُحرَسُ هنا
--------------------------------
فحصٌ يبني شجرةً مؤقَّتةً ثمَّ يُشغِّلُ أداةً من **مسارِها الحقيقيِّ** في عمليّةٍ
فرعيّةٍ، ويحكُمُ على رمزِ خروجِها — **لا يقيسُ شجرتَه**. والسببُ مقيسٌ لا
متخيَّلٌ: `REPO_ROOT` في أدواتِ هذا المستودعِ مُشتَقٌّ من **موضعِ الملفِّ**
(‏`Path(__file__).resolve().parents[2]`) لا من `cwd`، و`monkeypatch.setattr`
**لا يعبُرُ إلى عمليّةٍ أخرى**. فالحكمُ يأتي من حالِ المستودعِ الحقيقيِّ لحظةَ
التشغيلِ، وأيُّ إصلاحٍ للمستودعِ يُحمِّرُ الفحصَ — أي أنَّه **مِسمارٌ يعاقِبُ
الإصلاحَ**. وهذا وقعَ فعلًا: الحالةُ المُسمّاةُ في `DISC-032` احمَرَّت يومَ
وُفِّيَ الواجبُ في `W-065`.

و**فحصٌ لا يقيسُ ما يُعلِنُ أنَّه يقيسُه أخطرُ من غيابِ فحصٍ**: يُعطي ثقةً
كاذبةً بأنَّ الحرسَ مقيسٌ.

لماذا حرسٌ لا عينٌ
------------------
الحالةُ المُسمّاةُ أُصلِحَت في `W-065`، و**النمطُ لم يُحصَ**: نصُّ `DISC-032`
نفسُه يقولُ إنَّ `grep` يُظهِرُ نمطًا قد يتكرَّرُ، وإنَّ البندَ التاليَ يجعلُ
الدعوى «مقيسةً بحرسٍ لا بعينٍ». فالعينُ تُحصي مرّةً ثمَّ تنسى، والحرسُ يُحصي
في كلِّ دفعةٍ. وهذا الملفُّ هو ذاك الحرسُ: يُصنِّفُ **كلَّ** تشغيلِ أداةٍ في
عمليّةٍ فرعيّةٍ داخلَ `tests/`، ويُسقِطُ على كلِّ موضعٍ يحكُمُ على شجرةٍ لا
يقرؤها.

طريقُ الإنفاذِ (‏`W-077`)
--------------------------
لا خطوةَ تشغيلٍ جديدةً في CI ولا أداةَ جديدةً في `tools/`: هذا الملفُّ تحتَ
`tests/governance/` فيُنفِّذُه `ci.yml` بخطوتَينِ قائمتَينِ —
`python -m pytest tests/governance/ -q` في وظيفةِ الهُويّةِ، و
`pytest tests/ --cov` في وظيفةِ التغطيةِ. فالإنفاذُ قائمٌ بلا مسِّ مسارٍ
مقفولٍ بـ`WI-023`، وبلا مصدرِ حقيقةٍ مُكرَّرٍ، وبلا صفٍّ جديدٍ في
`VERDICT_CAPABLE_UNWIRED`.

حدُّ هذا الحرسِ — مُعلَنٌ لا مطويٌّ
------------------------------------
1. **يقرأُ الشِفرةَ تركيبيًّا (AST) لا سلوكًا**: فحصٌ يُبني قائمةَ أمرِه في
   مُعامِلٍ مُتغيِّرٍ أو دالّةٍ مساعدةٍ في ملفٍّ آخرَ لا يُحصى. وهذا حدُّ كلِّ
   قارئٍ ساكنٍ، ويُقاسُ أثرُه: العددُ الكلّيُّ مطبوعٌ فمَن أرادَ راجَعَه.
2. **يعرِفُ محلَّ القياسِ بعلمٍ صريحٍ** (`--repo-root` وما يُشبِهُه) أو
   بموضعِ المُشغَّلِ. تمريرُ المحلِّ **بمتغيّرِ بيئةٍ** لا يُقرأُ محلًّا هنا —
   فمَن مرَّرَه بالبيئةِ يُحصى موضعُه غيرَ مُرسًى حتّى يُصرَّحَ بعلمٍ.
3. **لا يحكُمُ على قصدِ الفحصِ**: موضعٌ يقصِدُ المستودعَ الحقيقيَّ عن عمدٍ
   (‏`cwd` ليست شجرةً مؤقَّتةً) مشروعٌ ويُحصى على حالِه، لا يُمنَعُ.

"""

from __future__ import annotations

import ast
from pathlib import Path
from typing import NamedTuple

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TESTS_ROOT = REPO_ROOT / "tests"

#: أسماءُ دوالِّ `subprocess` التي تُنشئُ عمليّةً فرعيّةً.
RUNNERS = frozenset({"run", "check_output", "check_call", "call", "Popen"})

#: تجهيزاتُ pytest التي تُنتِجُ شجرةً مؤقَّتةً — بذرةُ أسماءِ الشجرةِ.
TMP_SEEDS = frozenset({"tmp_path", "tmpdir", "tmp_path_factory", "tmp_path_factory"})

#: أعلامٌ تُمرِّرُ محلَّ القياسِ صريحًا فتُرسي الحكمَ في شجرةٍ مقصودةٍ.
SITE_FLAGS = ("--repo-root", "--root", "--source", "--tree")

#: تصنيفاتُ الموضعِ.
REAL_TREE = "REAL_TREE_ON_PURPOSE"
ANCHORED = "ANCHORED"
UNANCHORED = "UNANCHORED"


class Site(NamedTuple):
    """موضعُ تشغيلِ أداةٍ في عمليّةٍ فرعيّةٍ، مُصنَّفًا."""

    path: str
    line: int
    func: str
    verdict: str
    asserts_returncode: bool

    def __str__(self) -> str:  # pragma: no cover - للتقريرِ لا للحكمِ
        return f"{self.path}:{self.line} · {self.func}"


def _tool_names(scope: ast.AST, *, deep: bool = False) -> frozenset[str]:
    """أسماءٌ مربوطةٌ بمسارِ أداةٍ (‏`TOOL_PATH = ... / "tools" / ...`).

    تُقرأُ على مستوى الوحدةِ **وداخلَ الدالّةِ نفسِها**: فحصٌ ينسخُ
    الأداةَ إلى شجرتِه يربطُ المسارَ باسمٍ محليٍّ، فلو لم يُقرأْ لسقَطَ
    موضعٌ من الإحصاءِ صامتًا — وقارئٌ يُسقِطُ مواضعَ يُقرأُ خضرةً وهو أعمى.
    """
    body = ast.walk(scope) if deep else getattr(scope, "body", [])
    found: set[str] = set()
    for node in body:
        if not isinstance(node, ast.Assign):
            continue
        source = ast.unparse(node.value)
        if "tools" in source or "TOOL" in source:
            found.update(
                target.id for target in node.targets if isinstance(target, ast.Name)
            )
    return frozenset(found)


def _tmp_names(func: ast.AST) -> frozenset[str]:
    """أسماءُ الشجرةِ المؤقَّتةِ في دالّةٍ: البذرةُ وما اشتُقَّ منها بالإسنادِ."""
    names = set(TMP_SEEDS)
    changed = True
    while changed:
        changed = False
        for node in ast.walk(func):
            if not isinstance(node, ast.Assign):
                continue
            source = ast.unparse(node.value)
            if not any(name in source for name in names):
                continue
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id not in names:
                    names.add(target.id)
                    changed = True
    return frozenset(names)


def _is_runner(call: ast.Call) -> bool:
    func = call.func
    return (
        isinstance(func, ast.Attribute)
        and func.attr in RUNNERS
        and isinstance(func.value, ast.Name)
        and func.value.id == "subprocess"
    )


def classify_source(source: str, label: str = "<نصٌّ>") -> list[Site]:
    """يُصنِّفُ كلَّ تشغيلِ أداةٍ في عمليّةٍ فرعيّةٍ في نصٍّ واحدٍ.

    التصنيفُ ثلاثةٌ لا اثنانِ، لأنَّ «يقرأُ المستودعَ الحقيقيَّ» ليس عَطبًا
    بذاتِه: العَطبُ أن يُبنى تمهيدٌ لشجرةٍ مؤقَّتةٍ ثمَّ يُحكَمَ على غيرِها.
    """
    tree = ast.parse(source)
    tool_names = _tool_names(tree)
    sites: list[Site] = []

    for func in ast.walk(tree):
        if not isinstance(func, ast.FunctionDef | ast.AsyncFunctionDef):
            continue
        tmp_names = _tmp_names(func)
        names = tool_names | _tool_names(func, deep=True)
        asserts_returncode = "returncode" in ast.unparse(func)

        for call in ast.walk(func):
            if not isinstance(call, ast.Call) or not _is_runner(call):
                continue
            if not call.args or not isinstance(call.args[0], ast.List | ast.Tuple):
                continue

            argv = [ast.unparse(element) for element in call.args[0].elts]
            keywords = {
                keyword.arg: ast.unparse(keyword.value)
                for keyword in call.keywords
                if keyword.arg
            }

            tool = next(
                (
                    element
                    for element in argv[1:]
                    if "tools" in element
                    or any(name in element for name in names)
                ),
                None,
            )
            if tool is None:
                continue

            cwd = keywords.get("cwd", "")
            if not any(name in cwd for name in tmp_names):
                verdict = REAL_TREE
            else:
                joined = " ".join(argv)
                runs_inside_tree = tool.startswith(("'", '"')) or any(
                    name in tool for name in tmp_names
                )
                site_passed = any(flag in joined for flag in SITE_FLAGS) and any(
                    name in joined for name in tmp_names
                )
                verdict = ANCHORED if runs_inside_tree or site_passed else UNANCHORED

            sites.append(
                Site(label, call.lineno, func.name, verdict, asserts_returncode)
            )

    return sites


def census() -> list[Site]:
    """يُحصي مواضعَ `tests/` كلَّها — مُرتَّبةً فيُعادُ الرقمُ نفسُه."""
    sites: list[Site] = []
    for path in sorted(TESTS_ROOT.rglob("*.py")):
        label = path.relative_to(REPO_ROOT).as_posix()
        sites.extend(classify_source(path.read_text(encoding="utf-8"), label))
    return sites


# ── الحرسُ ───────────────────────────────────────────────────────────────────


def test_لا_فحصَ_يحكُمُ_على_شجرةٍ_لا_يقرؤها() -> None:
    """كلُّ موضعٍ يُمهِّدُ لشجرةٍ مؤقَّتةٍ يقيسُ **تلك** الشجرةَ لا غيرَها."""
    sites = census()
    tally = {
        verdict: [site for site in sites if site.verdict == verdict]
        for verdict in (REAL_TREE, ANCHORED, UNANCHORED)
    }
    print(
        "SITE_TALLY: مواضعُ تشغيلِ أدواتٍ في عمليّاتٍ فرعيّةٍ "
        f"{len(sites)} · تقصِدُ المستودعَ الحقيقيَّ {len(tally[REAL_TREE])} · "
        f"مُرساةٌ {len(tally[ANCHORED])} · غيرُ مُرساةٍ {len(tally[UNANCHORED])}"
    )
    assert not tally[UNANCHORED], (
        "مواضعُ تحكُمُ على شجرةٍ لا تقرؤها — يُمرَّرُ محلُّ القياسِ صريحًا "
        "(`--repo-root <شجرة>`) أو يُشغَّلُ المُشغَّلُ داخلَ الشجرةِ، "
        "ولا يُحذَفُ تأكيدٌ ولا يُلَيَّنُ رمزُ خروجٍ:\n  "
        + "\n  ".join(str(site) for site in tally[UNANCHORED])
    )


def test_المواضعُ_تُحصى_كلُّها_فلا_يسقُطُ_موضعٌ_صامتًا() -> None:
    """مجموعُ التصنيفاتِ = مجموعُ المواضعِ: لا صنفَ رابعَ يُخفي موضعًا."""
    sites = census()
    counted = sum(
        len([site for site in sites if site.verdict == verdict])
        for verdict in (REAL_TREE, ANCHORED, UNANCHORED)
    )
    assert counted == len(sites), "صنفٌ خارجَ الثلاثةِ يُخفي موضعًا عن الحكمِ"
    assert sites, "لا موضعَ أُحصِيَ — قارئٌ صامتٌ يُقرأُ خضرةً وهو أعمى"


# ── قياسُ الحرسِ نفسِه: لا يُطمَأنُّ إلى خضرةٍ لم تُختَبَرْ ───────────────────

_عَطبٌ = '''
import subprocess, sys
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "gate.py"

def test_شيء(tmp_path):
    repo = _mkrepo(tmp_path)
    out = subprocess.run([sys.executable, str(TOOL_PATH), "--self-check"], cwd=repo)
    assert out.returncode == 2
'''

_مُرسًى_بعلمٍ = '''
import subprocess, sys
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "gate.py"

def test_شيء(tmp_path):
    repo = _mkrepo(tmp_path)
    out = subprocess.run(
        [sys.executable, str(TOOL_PATH), "--self-check", "--repo-root", str(repo)],
        cwd=repo,
    )
    assert out.returncode == 2
'''

_مُرسًى_بموضعِ_المُشغَّلِ = '''
import subprocess, sys

def test_شيء(tmp_path):
    repo = _mkrepo(tmp_path)
    out = subprocess.run(
        [sys.executable, "tools/governance/gate.py", "--self-check"], cwd=repo
    )
    assert out.returncode == 2
'''

_مُرسًى_بنسخِ_الأداةِ = '''
import subprocess, sys

def test_شيء(tmp_path):
    repo = _mkrepo(tmp_path)
    أداةٌ = repo / "tools" / "governance" / "gate.py"
    out = subprocess.run([sys.executable, str(أداةٌ), "--self-check"], cwd=repo)
    assert out.returncode == 2
'''

_قصدٌ_مشروعٌ = '''
import subprocess, sys
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "gate.py"

def test_شيء(tmp_path):
    مُخرَجٌ = tmp_path / "تقرير.json"
    out = subprocess.run([sys.executable, str(TOOL_PATH), "--json", str(مُخرَجٌ)])
    assert out.returncode == 0
'''


def test_الحرسُ_يُسقِطُ_على_النمطِ_المقيسِ() -> None:
    """نصٌّ يحملُ عَطبَ `DISC-032` يُقرأُ غيرَ مُرسًى — وإلّا فالحرسُ زينةٌ."""
    sites = classify_source(_عَطبٌ)
    assert [site.verdict for site in sites] == [UNANCHORED]
    assert sites[0].asserts_returncode, "الحكمُ على رمزِ الخروجِ هو ما يجعلُ العَطبَ ضارًّا"


@pytest.mark.parametrize(
    ("نصٌّ", "وجهُ_الإرساءِ"),
    [
        (_مُرسًى_بعلمٍ, "محلُّ القياسِ مُمرَّرٌ بعلمٍ صريحٍ"),
        (_مُرسًى_بموضعِ_المُشغَّلِ, "المُشغَّلُ مسارٌ نسبيٌّ فيُقرأُ من الشجرةِ"),
        (_مُرسًى_بنسخِ_الأداةِ, "الأداةُ منسوخةٌ داخلَ الشجرةِ"),
    ],
)
def test_الحرسُ_لا_يُسقِطُ_على_موضعٍ_مُرسًى(نصٌّ: str, وجهُ_الإرساءِ: str) -> None:
    """ثلاثةُ أوجهٍ مشروعةٍ للإرساءِ لا يُحمِّرُها الحرسُ — فلا يُدفَعُ العاملُ إلى تخفيفٍ."""
    sites = classify_source(نصٌّ)
    assert [site.verdict for site in sites] == [ANCHORED], وجهُ_الإرساءِ


def test_قصدُ_المستودعِ_الحقيقيِّ_لا_يُقرأُ_عَطبًا() -> None:
    """شجرةٌ مؤقَّتةٌ للمُخرَجِ وحدَه، والقياسُ على المستودعِ الحقيقيِّ عن عمدٍ: مشروعٌ."""
    sites = classify_source(_قصدٌ_مشروعٌ)
    assert [site.verdict for site in sites] == [REAL_TREE]
