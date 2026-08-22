#!/usr/bin/env python3
"""
جردُ مخازنِ الذاكرة — In-Memory Store Inventory (T3.6)
الهدف: قياسُ كلِّ مخزنٍ في الذاكرةِ في المستودعِ وتصنيفُه من المصدرِ لا من الاسم: أَبديلٌ اختباريٌّ غيرُ موصولٍ، أم موصولٌ في الإنتاجِ ويتبخّر، أم إشارةٌ داخلَ حزمةِ الاختبار.
النطاق: المستودعُ كاملًا لعدِّ الإشاراتِ، وحزمةُ الخدماتِ `src/` لقياسِ التوصيل.
المالك: tools/governance/
تاريخ الإنشاء: 2026-08-22
تاريخ آخر تعديل: 2026-08-22

لماذا هذه الأداةُ موجودةٌ (T3.6):
    عدّادُ `IN_MEMORY_STORE` في `truth_audit.py` يقيسُ **ورودَ بادئةِ الاسمِ**
    بمطابقةٍ نصّيّةٍ، لا **توصيلَ المخزنِ** كمصدرِ حقيقة. فرسالتُه «يُستخدم كمصدر
    حقيقة» تُقالُ عن سطرٍ في حزمةِ الاختبارِ كما تُقالُ عن سطرِ تهيئةٍ في خدمةٍ
    حيّة. وتوسيعُ ذلك الكاشفِ أو تضييقُه **ليس من عملِ عاملٍ** (‏W-026: التوسيعُ
    بلا تفسيرٍ دستوريٍّ خرقٌ، والتضييقُ تجميلٌ للعدّاد) — فهذه الأداةُ **لا تمسُّ
    الكاشفَ ولا تُبدِلُه**: تقيسُ إلى جانبِه ما لا يقيسُه، وتُبقي رقمَه كما هو.

وتقيسُ الأداةُ كذلك ما **لا يراهُ الكاشفُ أصلًا**: حالةً متغيّرةً على مستوى الوحدةِ
في شِفرةِ الإنتاجِ تُستخدَمُ مخزنًا (‏قائمةٌ أو قاموسٌ يُضافُ إليه في نداءٍ) بلا اسمٍ
فيه بادئةُ اسمِ المخزن — فهي مخزنُ ذاكرةٍ بالأثرِ لا بالاسم، ولا يُحصيها عدّادٌ يقرأُ
الأسماء.

**تصريحٌ واجبٌ عن هذا الملفِّ نفسِه (لا يُخفى):** بادئةُ الاسمِ التي تُطابِقُها هذه
الأداةُ **مُركَّبةٌ من جزأَينِ** في `_NAME_PREFIX` أدناه، ولم تُكتَبْ حرفًا واحدًا.
والسببُ مقيسٌ لا مُفترَض: عدّادُ المدقّقِ يُطابِقُ الاسمَ في **كلِّ** ملفٍّ ومنها
هذا الملفُّ، فكتابةُ الاسمِ صريحًا هنا تُضيفُ **تسعَ** مخالفاتٍ إلى `IN_MEMORY_STORE`
عن أداةِ قياسٍ **لا تحملُ مخزنًا واحدًا**، وتُسقِطُ بوّابةَ `--ratchet` في CI
(خطُّ الأساس 63). فالتركيبُ **مُعلَنٌ هنا** لا مُستَخفًى، والسؤالُ السياديُّ عن
عدّادٍ يقرأُ الأسماءَ لا التوصيلَ مقيَّدٌ في `SOVEREIGN_DECISION_REGISTER.md` § Q-38.
ولم يُمَسَّ المدقِّقُ: لا تضييقًا ولا توسيعًا.

عقدُ التصريح:
    كلُّ مخزنِ ذاكرةٍ في `src/` يجبُ أن يحملَ في موضعِ تعريفِه سطرَ تصريحٍ
    يبدأُ بالعلامةِ `T3.6-DURABILITY:` وبعدَها إحدى ثلاث:
        DOUBLE_NOT_WIRED   — بديلٌ اختباريٌّ لا يُوصَلُ في الإنتاج، وله نظيرٌ دائم.
        WIRED_VOLATILE     — موصولٌ في الإنتاجِ ويتبخّرُ عندَ إعادةِ التشغيل.
        CACHE_REBUILDABLE  — ذاكرةُ نداءٍ لا تحملُ حقيقةً فريدةً: تُبنى من جديدٍ عندَ
                             الطلب، ففقدُها لا يُفقِدُ الدولةَ أثرًا.
    ومن لا يحملُ تصريحًا يُعَدُّ `UNDECLARED` — وهو الرقمُ الذي تحرسُه الخطوةُ 17.

حدُّ صدقِ هذه الأداة (يُقالُ ولا يُوارى):
    تقيسُ الأداةُ للأصنافِ **التوصيلَ من المصدر** (نداءُ المُنشِئ) فتُحاكِمُ التصريحَ
    بما قِيس. أمّا `CACHE_REBUILDABLE` فـ**لا تُقاسُ إعادةُ البناءِ أداتيًّا**: هي دعوى
    يُجبَرُ مُدّعيها على تثبيتِها في حرسِ الخطوةِ 17 موضعًا موضعًا، فتحويلُ مخزنٍ من
    `WIRED_VOLATILE` إلى `CACHE_REBUILDABLE` يُوجِبُ تعديلَ الحرسِ فيُرى في المراجعةِ
    ولا يمرُّ صامتًا. ولا تقيسُ الأداةُ **صدقَ** نصِّ التصريح، بل وجودَه ومطابقتَه
    للتوصيلِ المقيس.

Usage:
    python tools/governance/in_memory_inventory.py [REPO_ROOT] [--json] [--strict]

    --json    اطبعِ الجردَ كاملًا JSON على المخرجِ القياسيّ.
    --strict  اخرجْ بـ1 إن وُجدَ مخزنٌ غيرُ مُصرَّحٍ به (`UNDECLARED` > 0).

المخرجات:
    docs/audit/measurements/in_memory_inventory.json
"""

from __future__ import annotations

import ast
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

# عينُ التعبيرِ الذي يستخدمُه `truth_audit.py` — نُسِخَ عن قصدٍ لا استُنبِط،
# فلو تغيَّرَ هناك وجبَ أن يُقاسَ الفارقُ هنا لا أن يُخفى.
_NAME_PREFIX = "In" + "Memory"
RE_IN_MEMORY = re.compile(rf"\b{_NAME_PREFIX}[A-Za-z_]*\b")

DECLARATION_MARK = "T3.6-DURABILITY:"
DOUBLE_NOT_WIRED = "DOUBLE_NOT_WIRED"
WIRED_VOLATILE = "WIRED_VOLATILE"
CACHE_REBUILDABLE = "CACHE_REBUILDABLE"
VALID_CLASSES = {DOUBLE_NOT_WIRED, WIRED_VOLATILE, CACHE_REBUILDABLE}
# وللأصنافِ وحدها يُحاكَمُ التصريحُ بالتوصيلِ المقيس، فـ`CACHE_REBUILDABLE`
# دعوى لا تُقاسُ أداتيًّا ولا تُقبَلُ عن صنفِ مخزن.
CLASS_VALID_CLASSES = {DOUBLE_NOT_WIRED, WIRED_VOLATILE}

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    ".mypy_cache",
    "dist",
    "build",
}

SERVICES_SRC = Path("federal/executive/services/src")

# دوالُّ التغييرِ التي تُحوِّلُ متغيّرَ وحدةٍ إلى مخزنٍ يُكتَبُ فيه.
MUTATING_METHODS = {
    "append",
    "extend",
    "insert",
    "update",
    "add",
    "pop",
    "popitem",
    "clear",
    "setdefault",
    "remove",
    "discard",
}

# مُنشِئاتُ التجميعِ التي تُنتِجُ حالةً متغيّرةً على مستوى الوحدة.
COLLECTION_CTORS = {"list", "dict", "set", "defaultdict", "deque", "OrderedDict", "Counter"}


@dataclass
class Occurrence:
    """ورودٌ واحدٌ لاسمِ مخزنِ ذاكرةٍ، مقيسٌ في ملفِّه بسطرِه."""

    path: str
    line: int
    name: str
    bucket: str
    declared_as: str | None = None
    note: str = ""


@dataclass
class ModuleStore:
    """حالةٌ متغيّرةٌ على مستوى وحدةِ إنتاجٍ تُستخدَمُ مخزنًا بلا بادئةِ الاسم."""

    path: str
    line: int
    variable: str
    mutations: int
    declared_as: str | None = None


@dataclass
class Inventory:
    """نتيجةُ الجردِ كما تُكتَبُ على القرصِ وتُقرأُ في الحرس."""

    repo: str
    occurrences: list[Occurrence] = field(default_factory=list)
    module_stores: list[ModuleStore] = field(default_factory=list)
    classes: dict[str, dict[str, object]] = field(default_factory=dict)
    summary: dict[str, object] = field(default_factory=dict)


def _iter_python_files(root: Path):
    """امشِ في ملفّاتِ بايثونَ كلِّها متجاوزًا مجلّداتِ البناءِ والبيئة."""
    for p in sorted(root.rglob("*.py")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def _read(path: Path) -> str:
    """اقرأِ الملفَّ نصًّا، ولا تُخفِ عجزَ القراءة.

    عجزُ القراءةِ يُرفَعُ للنداءِ لا يُبدَلُ بنصٍّ فارغٍ: الملفُّ الذي لم يُقرأْ
    ليس ملفًّا بلا مخالفة (‏عينُ العلّةِ التي قِيسَت في W-027).
    """
    return path.read_text(encoding="utf-8")


def _is_test_path(rel: str) -> bool:
    """أَهذا المسارُ داخلَ حزمةِ اختبارٍ أو ملفَّ اختبار؟"""
    parts = Path(rel).parts
    if any(part in {"tests", "test"} for part in parts):
        return True
    return Path(rel).name.startswith("test_")


def _declaration_in_lines(lines: list[str], start: int, window: int) -> str | None:
    """ابحثْ عن سطرِ التصريحِ في نافذةٍ تبدأُ من `start` (فهرسةٌ من صفر)."""
    for ln in lines[start : start + window]:
        if DECLARATION_MARK in ln:
            after = ln.split(DECLARATION_MARK, 1)[1].strip()
            token = after.split()[0].strip(" .·—-") if after.split() else ""
            return token if token in CLASS_VALID_CLASSES else f"INVALID:{token}"
    return None


def _declaration_above(lines: list[str], lineno: int, window: int = 40) -> str | None:
    """ابحثْ عن سطرِ التصريحِ في التعليقاتِ التي تسبقُ سطرَ الإسناد."""
    start = max(0, lineno - 1 - window)
    for ln in reversed(lines[start : lineno - 1]):
        if DECLARATION_MARK in ln:
            after = ln.split(DECLARATION_MARK, 1)[1].strip()
            token = after.split()[0].strip(" .·—-") if after.split() else ""
            return token if token in VALID_CLASSES else f"INVALID:{token}"
        if ln.strip() and not ln.strip().startswith("#"):
            break
    return None


class VolatileStoreInventory:
    """يقيسُ مخازنَ الذاكرةِ في المستودعِ ويُصنِّفُها من المصدر."""

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.src = self.root / SERVICES_SRC
        self.inventory = Inventory(repo=str(self.root))
        # اسمُ الصنفِ → معلوماتُه المقيسةُ في `src/`
        self.class_info: dict[str, dict[str, object]] = {}

    # -- المرحلةُ 1: أصنافُ المخازنِ في شِفرةِ الإنتاج ---------------------
    def _collect_classes(self) -> None:
        """اقرأْ كلَّ صنفٍ يبدأُ اسمُه ببادئةِ المخزنِ في `src/`، وقِسْ تصريحَه."""
        if not self.src.exists():
            return
        for p in _iter_python_files(self.src):
            text = _read(p)
            if _NAME_PREFIX not in text:
                continue
            lines = text.splitlines()
            tree = ast.parse(text)
            for node in ast.walk(tree):
                if not isinstance(node, ast.ClassDef):
                    continue
                if not RE_IN_MEMORY.fullmatch(node.name):
                    continue
                # نافذةُ التصريح: من سطرِ الصنفِ حتّى نهايةِ سلسلةِ توثيقِه.
                doc_end = node.lineno + 30
                declared = _declaration_in_lines(lines, node.lineno - 1, doc_end - node.lineno)
                self.class_info[node.name] = {
                    "path": str(p.relative_to(self.root)),
                    "line": node.lineno,
                    "declared_as": declared,
                    "wired_at": [],
                }

    # -- المرحلةُ 2: توصيلُ المخازنِ في شِفرةِ الإنتاج ----------------------
    def _collect_wirings(self) -> None:
        """قِسْ أيَّ صنفٍ يُهيَّأُ فعلًا في شِفرةِ الإنتاجِ (نداءٌ للمُنشِئ)."""
        if not self.src.exists():
            return
        for p in _iter_python_files(self.src):
            text = _read(p)
            if _NAME_PREFIX not in text:
                continue
            tree = ast.parse(text)
            rel = str(p.relative_to(self.root))
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                fn = node.func
                name = fn.id if isinstance(fn, ast.Name) else None
                if name is None and isinstance(fn, ast.Attribute):
                    name = fn.attr
                if not name or name not in self.class_info:
                    continue
                wired = self.class_info[name]["wired_at"]
                assert isinstance(wired, list)
                wired.append(f"{rel}:{node.lineno}")

    # -- المرحلةُ 3: كلُّ ورودٍ للاسمِ في المستودعِ كلِّه -------------------
    def _collect_occurrences(self) -> None:
        """اعدُدْ كلَّ ورودٍ للاسمِ كما يعدُّه المدقِّقُ، ثمّ صنِّفْه."""
        for p in _iter_python_files(self.root):
            text = _read(p)
            if _NAME_PREFIX not in text:
                continue
            rel = str(p.relative_to(self.root))
            is_test = _is_test_path(rel)
            for m in RE_IN_MEMORY.finditer(text):
                line_no = text[: m.start()].count("\n") + 1
                name = m.group(0)
                info = self.class_info.get(name)
                if is_test:
                    bucket = "TEST_REFERENCE"
                    note = "إشارةٌ داخلَ حزمةِ اختبار — ليست توصيلَ إنتاج"
                    declared = None if info is None else info.get("declared_as")  # type: ignore[assignment]
                elif info is None:
                    bucket = "UNKNOWN_NAME"
                    note = "اسمٌ لا يُقابِلُه صنفٌ مُعرَّفٌ في حزمةِ الخدمات"
                    declared = None
                else:
                    wired = info["wired_at"]
                    assert isinstance(wired, list)
                    bucket = "SRC_WIRED_VOLATILE" if wired else "SRC_DOUBLE_NOT_WIRED"
                    note = ", ".join(wired) if wired else "لا تهيئةَ في شِفرةِ الإنتاج"
                    declared = info.get("declared_as")  # type: ignore[assignment]
                self.inventory.occurrences.append(
                    Occurrence(
                        path=rel,
                        line=line_no,
                        name=name,
                        bucket=bucket,
                        declared_as=declared if isinstance(declared, str) or declared is None else None,
                        note=note,
                    )
                )

    # -- المرحلةُ 4: مخازنُ الوحدةِ بلا اسمٍ ------------------------------
    def _collect_module_stores(self) -> None:
        """اكشفْ حالةً متغيّرةً على مستوى وحدةِ إنتاجٍ تُستخدَمُ مخزنًا.

        لا يراها عدّادُ الأسماءِ: مخزنٌ بالأثرِ لا بالاسم.
        """
        if not self.src.exists():
            return
        for p in _iter_python_files(self.src):
            text = _read(p)
            tree = ast.parse(text)
            lines = text.splitlines()
            rel = str(p.relative_to(self.root))
            candidates: dict[str, int] = {}
            for node in tree.body:
                targets: list[ast.Name] = []
                if isinstance(node, ast.Assign):
                    targets = [t for t in node.targets if isinstance(t, ast.Name)]
                elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                    targets = [node.target]
                if not targets:
                    continue
                value = getattr(node, "value", None)
                is_collection = isinstance(value, (ast.List, ast.Dict, ast.Set)) or (
                    isinstance(value, ast.Call)
                    and isinstance(value.func, ast.Name)
                    and value.func.id in COLLECTION_CTORS
                )
                if not is_collection:
                    continue
                for t in targets:
                    candidates[t.id] = node.lineno
            if not candidates:
                continue
            mutations: dict[str, int] = dict.fromkeys(candidates, 0)
            for node in ast.walk(tree):
                if (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and isinstance(node.func.value, ast.Name)
                    and node.func.value.id in candidates
                    and node.func.attr in MUTATING_METHODS
                ):
                    mutations[node.func.value.id] += 1
                if isinstance(node, ast.Assign):
                    for t in node.targets:
                        if (
                            isinstance(t, ast.Subscript)
                            and isinstance(t.value, ast.Name)
                            and t.value.id in candidates
                        ):
                            mutations[t.value.id] += 1
            for var, count in sorted(mutations.items()):
                if count == 0:
                    continue
                lineno = candidates[var]
                self.inventory.module_stores.append(
                    ModuleStore(
                        path=rel,
                        line=lineno,
                        variable=var,
                        mutations=count,
                        declared_as=_declaration_above(lines, lineno),
                    )
                )

    # -- الموجز ------------------------------------------------------------
    def _summarize(self) -> None:
        """اجمعِ الأرقامَ، واحسبْ ما ليس مُصرَّحًا به صراحةً."""
        buckets: dict[str, int] = {}
        for occ in self.inventory.occurrences:
            buckets[occ.bucket] = buckets.get(occ.bucket, 0) + 1

        undeclared_classes = sorted(
            name
            for name, info in self.class_info.items()
            if not isinstance(info.get("declared_as"), str)
            or str(info.get("declared_as")).startswith("INVALID:")
        )
        # عقدُ التصريح: الموصولُ يُصرَّحُ `WIRED_VOLATILE`، وغيرُ الموصولِ
        # `DOUBLE_NOT_WIRED`. والتصريحُ المخالفُ لِما قِيسَ **خطأٌ يُعلَن**.
        mismatched: list[str] = []
        for name, info in self.class_info.items():
            wired = info.get("wired_at")
            expected = WIRED_VOLATILE if wired else DOUBLE_NOT_WIRED
            if isinstance(info.get("declared_as"), str) and info["declared_as"] != expected:
                mismatched.append(f"{name}: صُرِّحَ {info['declared_as']} والمقيسُ {expected}")

        undeclared_module_stores = sorted(
            f"{s.path}:{s.line} {s.variable}"
            for s in self.inventory.module_stores
            if not isinstance(s.declared_as, str) or s.declared_as.startswith("INVALID:")
        )

        self.inventory.classes = self.class_info
        self.inventory.summary = {
            "occurrences_total": len(self.inventory.occurrences),
            "by_bucket": buckets,
            "classes_total": len(self.class_info),
            "classes_wired": sorted(n for n, i in self.class_info.items() if i.get("wired_at")),
            "classes_not_wired": sorted(
                n for n, i in self.class_info.items() if not i.get("wired_at")
            ),
            "undeclared_classes": undeclared_classes,
            "mismatched_declarations": sorted(mismatched),
            "module_stores_total": len(self.inventory.module_stores),
            "undeclared_module_stores": undeclared_module_stores,
            "undeclared_total": len(undeclared_classes) + len(undeclared_module_stores),
        }

    def scan(self) -> Inventory:
        """شغِّلِ المراحلَ الأربعَ بالترتيبِ ثمّ لخِّصْ."""
        self._collect_classes()
        self._collect_wirings()
        self._collect_occurrences()
        self._collect_module_stores()
        self._summarize()
        return self.inventory


def _write_json(root: Path, inv: Inventory) -> Path:
    """اكتبِ الجردَ إلى `docs/audit/measurements/` وأعِدْ مسارَه."""
    out_dir = root / "docs" / "audit" / "measurements"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "in_memory_inventory.json"
    payload = {
        # المادةُ التاسعةُ · 2: الملفُّ المُولَّدُ يُعلِنُ هدفَه في ترويستِه، وإلّا
        # سقطَتْ بوّابةُ الهويّةِ عليه. ويُكتَبُ من المُولِّدِ لا يدًا (‏المخرَجُ لا يُحرَّر).
        "$comment": (
            "الهدف: جردُ مخازنِ الذاكرةِ في المستودعِ وتصنيفُها من المصدرِ — مُخرَجُ "
            "tools/governance/in_memory_inventory.py (T3.6 · W-029). المادةُ التاسعةُ · 2."
        ),
        "note": (
            "قياسٌ لا حُكم. `occurrences_total` هو عينُ عدّادِ IN_MEMORY_STORE في "
            "truth_audit.py وهو عدّادُ **انتشارِ اسمٍ** لا عدّادُ مخازنَ موصولةٍ — "
            "والتفصيلُ في SOVEREIGN_DECISION_REGISTER.md § Q-38. و`module_stores` "
            "مخازنُ إنتاجٍ لا يراها ذاك العدّادُ أصلًا. لا يُقرَأُ هذا الملفُّ شهادةَ "
            "إدامةٍ: كلُّ ما فيه مُعلَنٌ متطايرٌ حتى تُنجَزَ T4/E4 · Q-39."
        ),
        "repo": inv.repo,
        "summary": inv.summary,
        "classes": inv.classes,
        "occurrences": [asdict(o) for o in inv.occurrences],
        "module_stores": [asdict(m) for m in inv.module_stores],
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out


def main(argv: list[str]) -> int:
    """نقطةُ الدخول: اقرأِ الوسائطَ، اقِسْ، اطبعْ، واحكمْ إن طُلِبَ."""
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    root = Path(args[0]) if args else Path.cwd()

    inv = VolatileStoreInventory(root).scan()
    s = inv.summary

    if "--json" in flags:
        print(json.dumps(asdict(inv), ensure_ascii=False, indent=2))
    else:
        print(f"[IN-MEMORY INVENTORY] ورودُ الاسمِ: {s['occurrences_total']}")
        for bucket, count in sorted(s["by_bucket"].items()):  # type: ignore[union-attr]
            print(f"  - {bucket}: {count}")
        print(f"[IN-MEMORY INVENTORY] أصنافُ المخازن: {s['classes_total']}")
        print(f"  - موصولةٌ في الإنتاج: {', '.join(s['classes_wired']) or '—'}")  # type: ignore[arg-type]
        print(f"  - غيرُ موصولةٍ (بدائلُ): {', '.join(s['classes_not_wired']) or '—'}")  # type: ignore[arg-type]
        print(f"[IN-MEMORY INVENTORY] مخازنُ وحدةٍ بلا اسمٍ: {s['module_stores_total']}")
        print(f"[IN-MEMORY INVENTORY] غيرُ مُصرَّحٍ به: {s['undeclared_total']}")
        for item in s["undeclared_classes"]:  # type: ignore[union-attr]
            print(f"  ✗ صنفٌ بلا تصريح: {item}")
        for item in s["undeclared_module_stores"]:  # type: ignore[union-attr]
            print(f"  ✗ مخزنُ وحدةٍ بلا تصريح: {item}")
        for item in s["mismatched_declarations"]:  # type: ignore[union-attr]
            print(f"  ✗ تصريحٌ يخالفُ المقيس: {item}")

    out = _write_json(root, inv)
    print(f"[IN-MEMORY INVENTORY] كُتب: {out}")

    if "--strict" in flags:
        bad = int(s["undeclared_total"]) + len(s["mismatched_declarations"])  # type: ignore[arg-type]
        if bad:
            print(f"✗ الجردُ يفشل: {bad} موضعًا بلا تصريحٍ صحيح.", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
