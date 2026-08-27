#!/usr/bin/env python3
"""إغلاقُ تبعيّاتِ البوّابات — أتُثبِّتُ كلُّ وظيفةٍ ما تستوردُه بوّاباتُها؟ (W-053).

الهدف:
    إنفاذُ التخفيفِ المُعلَنِ في `RK-010` أداةً لها رمزُ خروجٍ. نصُّ التخفيفِ في
    سجلِّ المخاطرِ: «كلُّ بوّابةٍ بالمكتبةِ القياسيّةِ وحدَها، أو تُعلَنُ تبعيّتُها
    في ملفِّها» — وهي قاعدةٌ لم يكنْ في الشجرةِ ما يقيسُها: الحرسُ القائمُ
    (`tests/governance/test_root_dependencies_declared.py`) يقيسُ الاتِّجاهَ
    الواحدَ (‏ألّا يُبَثَّ اسمُ حزمةٍ عاريًا في CI، وأن تكونَ الإعلاناتُ قائمةً)
    ولا يقيسُ الاتِّجاهَ المقابلَ: **أنَّ ما تستوردُه بوّابةٌ مُثبَّتٌ فعلًا في
    الوظيفةِ التي تُشغِّلُها**. وهذا الملفُّ هو ذاكَ الاتِّجاهُ منفَّذًا.

النطاق:
    قراءةُ ملفّاتِ `.github/workflows/*.yml` نصًّا، واستخراجُ ما تُثبِّتُه كلُّ
    وظيفةٍ (`pip install`) وما تُشغِّلُه (`python <ملفّ>.py` · `python -m <وحدة>`
    · مساراتُ `pytest`)، ثمَّ مسحُ الاستيراداتِ **عبورًا** بشجرةِ التجريدِ
    (`ast`) من كلِّ مدخلٍ. والحكمُ على التوزيعاتِ لا على الوحدات.

المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-08-27

لماذا بالمكتبةِ القياسيّةِ وحدَها
--------------------------------
لأنَّ أداةً تحرسُ إعلانَ التبعيّاتِ ثمَّ تلزمُها تبعيّةٌ غيرُ مُعلَنةٍ تكونُ
مثالَ العطبِ الذي تحرسُ منه. فلا `PyYAML` هنا: تفكيكُ المسارِ نصِّيٌّ
بالمسافاتِ البادئةِ على سابقةِ حارسِ `ci.yml` في `W-038`، و`tomllib` من
المكتبةِ القياسيّةِ منذُ 3.11 (‏وCI على 3.12) فقراءةُ `pyproject.toml` مشروعةٌ.

الرفضُ مُصنَّفٌ لا مطويٌّ
------------------------
حينَ لا تملكُ الأداةُ ما تقيسُ به، **ترفضُ ولا تحكُمُ**: `REFUSED:` في مجرى
الخطأِ وخروجٌ **2** — يُميِّزُ العجزَ عن القياسِ من حكمٍ سلبيٍّ (1) ومن إغلاقٍ
تامٍّ (0). ومن أبوابِ الرفضِ **وحدةٌ لا تُصنَّفُ**: لو خُمِّنَ لها اسمُ توزيعٍ
لجازَ أن تُعلَنَ ناقصةً وهي مُثبَّتةٌ — فتصيرُ الأداةُ نفسُها بوّابةً حمراءَ
بسببٍ غيرِ حقيقيٍّ، وذاك عينُ `RK-010`.

الأساسُ المُعلَنُ (‏ترباسٌ لا رخصةٌ)
-----------------------------------
عطبٌ واحدٌ مقيسٌ قائمٌ اليومَ في الشجرةِ، مكتوبٌ في `KNOWN_OPEN` بمُوجِّهِه إلى
`DISC-009`: وظيفةُ `sovereignty-kernel` تُثبِّتُ `requirements-dev.txt` وحدَه ثمَّ
تُشغِّلُ `pytest tests/sovereignty/`، وفيها تجهيزٌ يستوردُ `amos_federation`
فتسقطُ ثلاثةُ فحوصٍ بـ`ModuleNotFoundError` — سقوطٌ لا يقولُ شيئًا عن السيادةِ.
والأساسُ يُشتَرَطُ عليه شرطانِ: لا يُزادُ عليه بلا قيدٍ، **ولا يُترَكُ بعدَ
إصلاحِه** — فمتى أُصلِحَ العطبُ وبقيَ الاسمُ في الأساسِ سقطَتِ الأداةُ عن قصدٍ.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import tomllib
from pathlib import Path

WORKFLOWS_DIR = Path(".github/workflows")

STDLIB = set(sys.stdlib_module_names) | {"__future__"}

#: وحداتٌ اسمُ توزيعِها غيرُ اسمِها — تُعلَنُ ولا تُخمَّن.
MODULE_TO_DIST = {
    "yaml": "pyyaml",
    "PIL": "pillow",
    "jwt": "pyjwt",
    "nacl": "pynacl",
    "dotenv": "python-dotenv",
    "jose": "python-jose",
    "dateutil": "python-dateutil",
    "psycopg2": "psycopg2-binary",
    "Crypto": "pycryptodome",
    "nats": "nats-py",
    "grpc": "grpcio",
    "attr": "attrs",
    "google": "googleapis-common-protos",
    "opentelemetry": "opentelemetry-api",
    "amos_federation": "amos-federation",
}

#: العطبُ المقيسُ القائمُ — (ملفُّ المسارِ · الوظيفة) ← التوزيعاتُ الناقصةُ ومُوجِّهُها.
KNOWN_OPEN: dict[tuple[str, str], dict[str, object]] = {
    ("ci.yml", "sovereignty-kernel"): {
        "missing": ["amos-federation"],
        "routed": "DISC-009",
        "why": (
            "الوظيفةُ تُثبِّتُ requirements-dev.txt وحدَه ثمَّ تُشغِّلُ pytest "
            "tests/sovereignty/، وفيها تجهيزٌ يستوردُ amos_federation — "
            "وإسنادُ الإصلاحِ (‏تركيبُ الحزمةِ في الوظيفةِ · أو نقلُ الفحوصِ "
            "إلى وظيفةٍ تُثبِّتُها · أو إعلانُ التبعيّةِ) قرارُ المالكِ."
        ),
    },
}


#: ما يمسِكُ فقدانَ حزمةٍ فعلًا حينَ يُنفَّدُ — لا ما يُستحسَنُ أن يُمسَكَ.
#: `except Exception` يمسِكُ `ModuleNotFoundError` لأنَّه فرعٌ منه، فإن عُدَّ
#: الاستيرادُ تحتَه تبعيّةً لازمةً حُمِّرَت بوّابةٌ بسببٍ غيرِ حقيقيٍّ.
#: والأداةُ تقيسُ ما يجري لا تُفتي في الأسلوبِ: سعةُ `except Exception`
#: دَينٌ موضوعُ أدواتٍ أُخرى، وليسَ شأنَ إغلاقِ التبعيّات.
_CATCHES_IMPORT = frozenset(
    {"ImportError", "ModuleNotFoundError", "Exception", "BaseException"}
)


class MeasurementRefused(Exception):
    """لا تملكُ الأداةُ ما تقيسُ به — فلا تحكُمُ."""


def _refuse(reason: str) -> None:
    raise MeasurementRefused(reason)


def normalise(name: str) -> str:
    """اسمُ توزيعٍ مُسوًّى: بلا حدِّ إصدارٍ ولا زياداتٍ، وبشُرطةٍ لا بشُرطةٍ سفليّة."""
    head = re.split(r"[<>=!;\[ ]", name.strip())[0].strip()
    return head.lower().replace("_", ".").replace(".", "-")


# ═══════════════════════════════════════════════════════════════════════════
# ١ — تفكيكُ ملفِّ مسارٍ: وظائفُه وخطواتُه (نصًّا · بلا PyYAML)
# ═══════════════════════════════════════════════════════════════════════════
def strip_comments(text: str) -> str:
    """التعليقُ ليسَ أمرًا — سطرٌ أوّلُ حرفٍ فيه `#` لا يُنفِّذُ شيئًا."""
    return "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith("#"))


def parse_jobs(path: Path) -> dict[str, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not any(re.match(r"^jobs:\s*$", ln) for ln in lines):
        _refuse(f"ملفُّ مسارٍ بلا مفتاحِ `jobs`: {path}")
    jobs: dict[str, list[str]] = {}
    cur: str | None = None
    in_jobs = False
    for ln in lines:
        if re.match(r"^jobs:\s*$", ln):
            in_jobs = True
            continue
        if not in_jobs:
            continue
        head = re.match(r"^  ([A-Za-z0-9_-]+):\s*$", ln)
        if head:
            cur = head.group(1)
            jobs[cur] = []
            continue
        if cur is not None and (not ln.strip() or ln.startswith("    ")):
            jobs[cur].append(ln)
    if not jobs:
        _refuse(f"لم تُقرأْ وظيفةٌ واحدةٌ في {path} — بنيةٌ لا تُفكَّكُ نصًّا")
    return jobs


def job_working_dir(body: list[str]) -> str:
    for i, ln in enumerate(body):
        if re.match(r"^    defaults:\s*$", ln):
            for ln2 in body[i : i + 6]:
                m = re.search(r"working-directory:\s*(\S+)", ln2)
                if m:
                    return m.group(1)
    return "."


def steps_of(body: list[str]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    cur: dict[str, object] | None = None
    for ln in body:
        if re.match(r"^      - ", ln):
            if cur is not None:
                out.append(cur)
            cur = {"text": [], "wd": None}
        if cur is None:
            continue
        m = re.search(r"working-directory:\s*(\S+)", ln)
        if m:
            cur["wd"] = m.group(1)
        cur["text"].append(ln)  # type: ignore[union-attr]
    if cur is not None:
        out.append(cur)
    return out


# ═══════════════════════════════════════════════════════════════════════════
# ٢ — ما تُثبِّتُه وظيفةٌ: توزيعاتٌ مُعلَنةٌ ووحداتٌ يُوفِّرُها مشروعٌ محليٌّ
# ═══════════════════════════════════════════════════════════════════════════
def requirement_names(path: Path) -> set[str]:
    if not path.exists():
        _refuse(f"ملفُّ متطلّباتٍ مذكورٌ في مسارٍ وغيرُ موجودٍ: {path}")
    out: set[str] = set()
    for ln in path.read_text(encoding="utf-8").splitlines():
        ln = ln.split("#")[0].strip()
        if not ln or ln.startswith("-"):
            continue
        out.add(normalise(ln))
    if not out:
        _refuse(f"ملفُّ متطلّباتٍ لا يُعلِنُ اسمًا واحدًا: {path}")
    return out


def local_project(project_dir: Path, extras: list[str], no_deps: bool) -> tuple[set[str], set[str]]:
    py = project_dir / "pyproject.toml"
    if not py.exists():
        _refuse(f"تركيبٌ قابلٌ للتحريرِ لمشروعٍ بلا `pyproject.toml`: {project_dir}")
    data = tomllib.loads(py.read_text(encoding="utf-8"))
    proj = data.get("project", {})
    name = proj.get("name", "")
    if not name:
        _refuse(f"`pyproject.toml` بلا اسمِ مشروعٍ: {py}")
    dists = {normalise(name)}
    if not no_deps:
        dists |= {normalise(d) for d in proj.get("dependencies", [])}
        optional = proj.get("optional-dependencies", {})
        for ex in extras:
            dists |= {normalise(d) for d in optional.get(ex, [])}
    where = (
        data.get("tool", {})
        .get("setuptools", {})
        .get("packages", {})
        .get("find", {})
        .get("where", ["."])
    )
    modules: set[str] = set()
    roots: set[Path] = set()
    for w in where:
        base = project_dir / w
        if base.is_dir():
            roots.add(base)
            modules |= {p.name for p in base.iterdir() if (p / "__init__.py").exists()}
            modules |= {p.stem for p in base.glob("*.py") if p.stem != "setup"}
    for r in roots:
        _SEARCH_ROOTS.add(r)
    return dists, modules


#: أدلّةٌ يُبحَثُ فيها عن وحداتٍ محليّةٍ رُكِّبَت قابلةً للتحرير.
_SEARCH_ROOTS: set[Path] = set()


def declared_vocabulary(root: Path) -> set[str]:
    """كلُّ اسمِ توزيعٍ تُعلِنُه الشجرةُ في موضِعٍ واحدٍ على الأقلِّ.

    وفائدتُها فرقٌ لا يُطوى: وحدةٌ اسمُ توزيعِها **معروفٌ** وغيرُ مُثبَّتٍ في
    وظيفةٍ بعينِها حكمٌ سلبيٌّ صادقٌ (1)؛ أمّا وحدةٌ **لا يُعرَفُ اسمُ
    توزيعِها** فلا حكمَ فيها بل رفضٌ (2) — وخلطُ البابَينِ يُنتِجُ حُمرةً
    بلا سببٍ أو خُضرةً بلا قياسٍ.
    """
    vocab: set[str] = set()
    for req in sorted(root.glob("requirements*.txt")):
        for ln in req.read_text(encoding="utf-8").splitlines():
            ln = ln.split("#")[0].strip()
            if ln and not ln.startswith("-"):
                vocab.add(normalise(ln))
    for py in sorted(root.rglob("pyproject.toml")):
        if ".git" in py.parts or "node_modules" in py.parts:
            continue
        try:
            data = tomllib.loads(py.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            _refuse(f"`pyproject.toml` لا يُفكَّكُ: {py} — {exc}")
        proj = data.get("project", {})
        if name := proj.get("name"):
            vocab.add(normalise(name))
        for dep in proj.get("dependencies", []):
            vocab.add(normalise(dep))
        for group in proj.get("optional-dependencies", {}).values():
            vocab |= {normalise(d) for d in group}
    for lock in sorted(root.rglob("requirements*.lock")):
        for ln in lock.read_text(encoding="utf-8").splitlines():
            ln = ln.split("#")[0].strip()
            if ln and not ln.startswith("-"):
                vocab.add(normalise(ln))
    if not vocab:
        _refuse("لا مُعجمَ إعلاناتٍ في الشجرةِ — فلا يُميَّزُ ناقصٌ من مجهولٍ")
    return vocab


# ═══════════════════════════════════════════════════════════════════════════
# ٣ — الاستيراداتُ عبورًا: ما يبلُغُه مدخلٌ من الطرفِ الثالث
# ═══════════════════════════════════════════════════════════════════════════
def module_file(
    root: Path,
    module: str,
    provided: set[str],
    script_dir: Path | None = None,
    wd_root: Path | None = None,
) -> Path | None:
    """ملفُّ وحدةٍ محليّةٍ إن كانت محليّةً — وإلّا `None` (‏طرفٌ ثالثٌ).

    ودليلُ المدخلِ نفسِه بابٌ مشروعٌ: بايثون يضعُ دليلَ النَّصِّ المُشغَّلِ في
    `sys.path` أوّلًا، فـ`import check_repository_identity` من
    `tools/governance/x.py` استيرادٌ محليٌّ لا طرفٌ ثالثٌ. وحصرُه بدليلِ
    **المدخلِ** لا بكلِّ ملفٍّ يُعبَرُ إليه مقصودٌ: تلكَ هي دلالةُ التشغيلِ.
    """
    rel = module.replace(".", "/")
    bases = [root, *sorted(_SEARCH_ROOTS)] if module.split(".")[0] in provided else [root]
    if wd_root is not None and wd_root != root:
        bases = [*bases, wd_root]
    if script_dir is not None:
        bases = [*bases, script_dir]
    for base in bases:
        f = base / f"{rel}.py"
        if f.exists():
            return f
        pkg = base / rel / "__init__.py"
        if pkg.exists():
            return pkg
        if (base / rel).is_dir():
            return base / rel  # حزمةُ فضاءِ أسماءٍ: محليّةٌ ولا ملفَّ لها
    return None


def _string_constants(node: ast.AST) -> list[str]:
    """الحروفُ الثابتةُ بترتيبِ المصدرِ — عمقًا أوّلًا، لا `ast.walk` عرضًا.

    والترتيبُ ليسَ تفصيلًا: `REPO_ROOT / "tools" / "governance"` يُنتِجُ بالعرضِ
    `governance` قبلَ `tools` فيُبنى دليلٌ مقلوبٌ لا وجودَ له، فتُعَدُّ وحدةٌ
    محليّةٌ طرفًا ثالثًا ويُرفَضُ القياسُ بلا سببٍ.
    """
    out: list[str] = []
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        out.append(node.value)
    for child in ast.iter_child_nodes(node):
        out += _string_constants(child)
    return out


def path_injections(tree: ast.Module, root: Path) -> list[Path]:
    """أدلّةٌ يُدخِلُها ملفٌّ في `sys.path` صريحًا — تُقرأُ ولا تُخمَّنُ.

    فحوصُ الحوكمةِ في هذه الشجرةِ تستوردُ البوّاباتَ نفسَها بعدَ
    `sys.path.insert(0, REPO_ROOT / "tools" / "governance")`، فوحدةٌ بلغَتها
    بهذا البابِ **محليّةٌ** لا طرفٌ ثالثٌ. وتُجمَعُ الحروفُ الثابتةُ في نداءِ
    الإدخالِ وتُلحَقُ بالجذرِ؛ فإن لم يوجدْ الدليلُ أُهمِلَ — ولا يُخمَّنُ متغيّرٌ.
    """
    out: list[Path] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        if node.func.attr not in {"insert", "append"}:
            continue
        target = node.func.value
        if not (
            isinstance(target, ast.Attribute)
            and target.attr == "path"
            and isinstance(target.value, ast.Name)
            and target.value.id == "sys"
        ):
            continue
        parts = _string_constants(node)
        if not parts:
            continue
        cand = root.joinpath(*[p.strip("/") for p in parts if p.strip("/")])
        if cand.is_dir():
            out.append(cand)
    return out


def guarded_imports(tree: ast.Module) -> set[ast.AST]:
    """استيراداتٌ اختياريّةٌ مُعلَنةٌ — تحتَ `try` يمسِكُ `ImportError` أو فرعَهُ.

    واستثناءُها من القياسِ ليسَ تساهلًا بل صدقٌ: حزمةٌ يُمسَكُ فقدانُها
    ويُتَرجَمُ إلى تخطٍٍ مُعلَنٍ ليسَ تبعيّةً لازمةً للوظيفةِ؛ وعدُّها نقصًا
    يُحمِّرُ بوّابةً بسببٍ غيرِ حقيقيٍّ — وذاك عينُ الخطرِ `RK-010`. وقد قيسَ
    هذا فـ`tools/audit/live_truth.py` يستوردُ `sqlalchemy` تحتَ `try` ويرفعُ
    `SourceNotConfigured` — فلا تلزمُ وظيفةً تمرُّ عليه.
    """
    guarded: set[ast.AST] = set()
    for node in ast.walk(tree):  # noqa: PLR1702
        if not isinstance(node, ast.Try):
            continue
        catches = False
        for handler in node.handlers:
            names: list[str] = []
            exc = handler.type
            if isinstance(exc, ast.Name):
                names = [exc.id]
            elif isinstance(exc, ast.Tuple):
                names = [e.id for e in exc.elts if isinstance(e, ast.Name)]
            elif isinstance(exc, ast.Attribute):
                names = [exc.attr]
            elif exc is None:
                names = ["BaseException"]  # `except:` عارٍ يمسِكُ كلَّ شيءٍ
            if _CATCHES_IMPORT & set(names):
                catches = True
        if not catches:
            continue
        for stmt in node.body:
            for inner in ast.walk(stmt):
                if isinstance(inner, (ast.Import, ast.ImportFrom)):
                    guarded.add(inner)
    return guarded


def third_party_closure(
    root: Path,
    entry: Path,
    provided: set[str],
    seen: set[Path],
    script_dir: Path | None = None,
    wd_root: Path | None = None,
) -> set[str]:
    if script_dir is None:
        script_dir = entry.parent
    if entry in seen:
        return set()
    seen.add(entry)
    if entry.is_dir() or not entry.exists():
        return set()
    try:
        tree = ast.parse(entry.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError) as exc:
        _refuse(f"ملفُّ بايثون يُبلَغُ من بوّابةٍ ولا يُفكَّكُ: {entry} — {exc}")
    extra_roots = path_injections(tree, root)  # type: ignore[arg-type]
    guarded = guarded_imports(tree)  # type: ignore[arg-type]
    modules: set[str] = set()
    for node in ast.walk(tree):  # type: ignore[arg-type]
        if node in guarded:
            continue
        if isinstance(node, ast.Import):
            modules |= {a.name for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            modules.add(node.module)
    out: set[str] = set()
    for mod in modules:
        if mod.split(".")[0] in STDLIB:
            continue
        local = module_file(root, mod, provided, script_dir, wd_root)
        if local is None:
            for extra in extra_roots:
                local = module_file(root, mod, provided, extra, wd_root)
                if local is not None:
                    break
        if local is not None:
            out |= third_party_closure(root, local, provided, seen, script_dir, wd_root)
        else:
            out.add(mod.split(".")[0])
    return out


# ═══════════════════════════════════════════════════════════════════════════
# ٤ — قياسُ وظيفةٍ واحدةٍ
# ═══════════════════════════════════════════════════════════════════════════
def measure_job(
    root: Path, wf_name: str, job: str, body: list[str], vocab: set[str]
) -> dict[str, object] | None:
    base_wd = job_working_dir(body)
    installed: set[str] = set()
    provided: set[str] = set()
    entries: list[Path] = []
    needed_dists: set[str] = set()
    for step in steps_of(body):
        wd = step["wd"] or base_wd  # type: ignore[index]
        text = strip_comments("\n".join(step["text"]))  # type: ignore[arg-type]
        for spec in re.findall(r"pip install\s+(.+)", text):
            spec = spec.strip().rstrip("\\").strip()
            if m := re.search(r"-r\s+(\S+)", spec):
                installed |= requirement_names(root / wd / m.group(1))  # type: ignore[operator]
            elif m := re.search(r"-e\s+\"?([^\"\s\[]+)(?:\[([^\]]+)\])?\"?", spec):
                extras = [e.strip() for e in (m.group(2) or "").split(",") if e.strip()]
                dists, mods = local_project(
                    (root / wd / m.group(1)).resolve(),  # type: ignore[operator]
                    extras,
                    "--no-deps" in spec,
                )
                installed |= dists
                provided |= mods
            elif re.match(r"^[A-Za-z][\w.-]*==", spec):
                installed.add(normalise(spec))
            else:
                _refuse(f"وسيطُ `pip install` لا يُحسَمُ إلى إعلانٍ: {wf_name}/{job}: {spec!r}")
        for m in re.finditer(r"python\s+(?!-)(\S+\.py)", text):
            entries.append(root / wd / m.group(1))  # type: ignore[operator]
        for m in re.finditer(r"(?:python -m ([\w.]+)|(?<![-\w])(pytest))((?:\s+[^\s\\|&;]+)*)", text):
            module, rest = m.group(1) or m.group(2), m.group(3)
            local = module_file(root, module, provided)
            if local is not None:
                entries.append(local)
            else:
                needed_dists.add(MODULE_TO_DIST.get(module.split(".")[0], normalise(module)))
            if module.split(".")[0] == "pytest":
                for token in rest.split():
                    if token.startswith("-"):
                        continue
                    p = root / wd / token  # type: ignore[operator]
                    if p.is_dir():
                        entries += sorted(p.rglob("*.py"))
                    elif p.suffix == ".py" and p.exists():
                        entries.append(p)
    if not entries and not needed_dists:
        return None
    needed = set(needed_dists)
    unclassified: set[str] = set()
    for entry in entries:
        for mod in third_party_closure(root, entry, provided, set(), None, root / base_wd):
            if mod in MODULE_TO_DIST:
                needed.add(MODULE_TO_DIST[mod])
            elif normalise(mod) in installed or normalise(mod) in vocab:
                needed.add(normalise(mod))
            else:
                unclassified.add(mod)
    missing = sorted(needed - installed)
    baseline = KNOWN_OPEN.get((wf_name, job), {})
    known = {normalise(x) for x in baseline.get("missing", [])}  # type: ignore[arg-type]
    for mod in sorted(unclassified):
        if normalise(mod) in known or MODULE_TO_DIST.get(mod, "") in known:
            missing.append(normalise(MODULE_TO_DIST.get(mod, mod)))
        else:
            _refuse(
                f"وحدةٌ لا تُصنَّفُ: {mod!r} في {wf_name}/{job} — "
                "لا هي مكتبةٌ قياسيّةٌ ولا محليّةٌ ولا لها اسمُ توزيعٍ مُعلَنٌ. "
                "يُعلَنُ اسمُها في MODULE_TO_DIST أو يُقيَّدُ العطبُ في KNOWN_OPEN؛ "
                "ولا تُخمَّنُ، فتخمينُها يُنتِجُ حُمرةً بسببٍ غيرِ حقيقيٍّ (RK-010)."
            )
    missing = sorted(set(missing))
    return {
        "workflow": wf_name,
        "job": job,
        "working_directory": base_wd,
        "installed_count": len(installed),
        "entry_points": len(entries),
        "needed": sorted(needed),
        "missing": missing,
        "verdict": "CLOSED" if not missing else "OPEN",
    }


# ═══════════════════════════════════════════════════════════════════════════
# ٥ — الحكمُ على الشجرةِ كلِّها
# ═══════════════════════════════════════════════════════════════════════════
def measure(root: Path) -> dict[str, object]:
    wfs = root / WORKFLOWS_DIR
    if not wfs.is_dir():
        _refuse(f"لا دليلَ مساراتٍ: {wfs}")
    files = sorted(wfs.glob("*.yml")) + sorted(wfs.glob("*.yaml"))
    if not files:
        _refuse(f"دليلُ مساراتٍ بلا ملفٍّ واحدٍ: {wfs}")
    vocab = declared_vocabulary(root)
    jobs: list[dict[str, object]] = []
    for wf in files:
        for job, body in parse_jobs(wf).items():
            row = measure_job(root, wf.name, job, body, vocab)
            if row is not None:
                jobs.append(row)
    if not jobs:
        _refuse("لا وظيفةَ واحدةً تُشغِّلُ بايثون — لا شيءَ يُقاسُ")
    open_jobs = {(j["workflow"], j["job"]): j["missing"] for j in jobs if j["missing"]}
    unexpected = {
        k: v for k, v in open_jobs.items()
        if sorted(normalise(x) for x in KNOWN_OPEN.get(k, {}).get("missing", [])) != sorted(v)  # type: ignore[arg-type,union-attr]
    }
    # والتقادُمُ يُحكَمُ به على وظيفةٍ **موجودةٍ في الشجرةِ المقيسةِ** لا على غائبةٍ:
    # الأساسُ قيدٌ على هذه الشجرةِ، فلو حُكِمَ به على شجرةٍ أُخرى (‏كتجهيزٍ
    # موقوتٍ في فحصٍ) سقَطَ بـ«أساسٍ تقادمَ» وهو لم يتقادمْ — حُمرةٌ بلا
    # سببٍ، وهي عينُ `RK-010`. وقد كشفَ هذا العيبَ حرسُ الحرسِ نفسُه (`W-053`).
    measured_keys = {(j["workflow"], j["job"]) for j in jobs}
    stale = [k for k in KNOWN_OPEN if k in measured_keys and k not in open_jobs]
    return {
        "$comment": (
            "الهدف: قياسُ إغلاقِ تبعيّاتِ كلِّ وظيفةٍ في CI مقابلَ ما تستوردُه "
            "بوّاباتُها فعلًا — مُخرَجُ tools/governance/gate_dependency_closure.py. "
            "يقيسُ ولا يُصلِح. المادةُ التاسعةُ · 2. (RK-010 · W-053)"
        ),
        "jobs_measured": len(jobs),
        "jobs_closed": sum(1 for j in jobs if j["verdict"] == "CLOSED"),
        "jobs_open": len(open_jobs),
        "known_open": {f"{k[0]}::{k[1]}": v for k, v in KNOWN_OPEN.items()},
        "unexpected_open": {f"{k[0]}::{k[1]}": v for k, v in unexpected.items()},
        "stale_baseline": [f"{k[0]}::{k[1]}" for k in stale],
        "detail": jobs,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="إغلاقُ تبعيّاتِ بوّاباتِ CI (RK-010 · W-053).")
    parser.add_argument("path", nargs="?", default=".", help="جذرُ المستودعِ")
    parser.add_argument("--check", action="store_true", help="حكمٌ برمزِ خروجٍ")
    parser.add_argument("--json", action="store_true", help="طبعُ الحِملِ كاملًا")
    args = parser.parse_args(argv)
    try:
        payload = measure(Path(args.path).resolve())
    except MeasurementRefused as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not args.check:
        if not args.json:
            print(
                f"وظائفُ مقيسةٌ: {payload['jobs_measured']} · مُغلَقةٌ: "
                f"{payload['jobs_closed']} · مفتوحةٌ: {payload['jobs_open']}"
            )
        return 0
    unexpected = payload["unexpected_open"]
    stale = payload["stale_baseline"]
    if unexpected:
        for key, missing in unexpected.items():  # type: ignore[union-attr]
            print(f"✗ {key}: تستوردُ ولا تُثبِّتُ: {missing}", file=sys.stderr)
        print(
            "بوّابةٌ تسقُطُ لسببٍ غيرِ حقيقيٍّ — تُعلَنُ التبعيّةُ في ملفِّ "
            "الوظيفةِ أو تُكتَبُ بالمكتبةِ القياسيّةِ وحدَها (RK-010).",
            file=sys.stderr,
        )
        return 1
    if stale:
        print(f"✗ أساسٌ تقادمَ: {stale} — أُصلِحَ العطبُ ولم يُنزَعْ من KNOWN_OPEN.", file=sys.stderr)
        return 1
    print(
        f"[GATE DEPS] ✓ {payload['jobs_closed']} من {payload['jobs_measured']} وظيفةً "
        f"مُغلَقةُ التبعيّاتِ · {payload['jobs_open']} مفتوحةٌ مُقيَّدةٌ في الأساسِ."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
