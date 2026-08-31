#!/usr/bin/env python3
"""سجلُّ طرقِ الإنفاذِ — أداةٌ حاكمةٌ لا تُشغِّلُها دفعةٌ تُعلِنُ سببَها أو تسقُط (W-080).

الهدف:
    أن يكونَ لكلِّ ملفٍّ **قابلٍ للتشغيلِ** في `tools/` أحدُ أمرَينِ لا ثالثَ:
    **طريقُ إنفاذٍ مقيسٌ** (خطوةُ تشغيلٍ في CI تُسمّي مسارَه · أو استدعاءُ
    `pytest` في CI يشملُه · أو فحصٌ يشملُه ذاك الاستدعاءُ ويحكُمُ على
    **الشجرةِ الحاضرةِ** ويربطُ نفسَه بالأداةِ)، أو **سببٌ مُصنَّفٌ مكتوبٌ في
    ترويستِه** من مفرداتٍ مغلقةٍ. فأداةٌ حاكمةٌ لا يُشغِّلُها شيءٌ ولا تُعلِنُ
    لماذا **صمتٌ في جردٍ** لا نقصٌ مُعلَنٌ — وهذا ما تُسقِطُه هذه البوّابة.

النطاق:
    ملفّاتُ `tools/**/*.py` · `.github/workflows/*.yml` · وملفّاتُ الفحصِ التي
    يشملُها استدعاءُ `pytest` في تلك الوظائفِ. لا شبكةَ ولا قاعدةَ بياناتٍ ولا
    سرَّ، ولا تكتبُ الأداةُ بايتًا في شجرةٍ تحكمُ عليها. مكتبةٌ قياسيّةٌ وحدَها
    (‏`RK-010`).
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-31
تاريخ آخر تعديل: 2026-08-31

طريقُ الإنفاذ: COVERED_TEST · tests/governance/test_w079_enforcement_path_ledger.py يحكُمُ على الشجرةِ الحاضرةِ ويشملُه استدعاءُ `pytest` في CI

لماذا أداةٌ لا فقرةٌ:
    قِيسَ في `DISC-037` أنَّ أدواتٍ حاكمةً لا تُسمّيها خطوةُ تشغيلٍ، فأُعلِنَ
    العددُ **ملاحظةً**. والملاحظةُ لا تمنعُ أداةً جديدةً من أن تُولَدَ غيرَ
    مربوطةٍ في اليومِ التالي: لا رمزَ خروجٍ يقفُ في وجهِ ذلك. ثمَّ قِيسَ في
    `W-079` أنَّ الملاحظةَ نفسَها **غيرُ دقيقةٍ في اتِّجاهَينِ**: عَدَّت مكتبةً
    بلا مدخلِ تشغيلٍ أداةً مهجورةً، وعَدَّت أدواتٍ يُشغِّلُها فحصٌ يحكُمُ على
    الشجرةِ الحاضرةِ غيرَ مربوطةٍ، وقصَرَت نظرَها على مجلَّدَينِ من خمسةٍ.
    فالعلاجُ قياسٌ يُصنِّفُ كلَّ ملفٍّ من مصدرِه، ويُلزِمُ ما لا طريقَ له
    بإعلانٍ **يُكذِّبُه الواقعُ إن كذبَ**.

الحدُّ المُعلَنُ — لا مطويٌّ:
    * الأداةُ تُلزِمُ **الإعلانَ** لا **التشغيلَ**: لا تُنشئُ واجبَ «يُشغَّلُ في
      كلِّ دفعةٍ» لم يكتبْه أحدٌ، ولا تحكُمُ على صوابِ السببِ المُعلَنِ. من
      أرادَ ربطًا فبندُ عملٍ وبوّابةٌ، لا سطرُ ترويسةٍ.
    * تصنيفُ «قابلٍ للتشغيلِ» و«قادرٍ على الحكمِ» **ساكنٌ** يُقرأُ من الشِفرةِ:
      حرسُ `__main__` · نداءٌ في أعلى الملفِّ · `sys.exit` برمزٍ غيرِ صفرٍ أو
      `SystemExit`. فأداةٌ تحكُمُ بطريقٍ آخرَ (‏رمزُ خروجٍ من مكتبةٍ تُستورَدُ)
      لا يراها هذا القياسُ: نقصٌ يُعلَنُ لا يُطوى.
    * الإعلانُ يُقرأُ في **نافذةٍ مُعلَنةٍ** من أوّلِ الملفِّ
      (`HEADER_WINDOW_LINES`)، ورمزُه يُقرأُ من **مفرداتٍ مغلقةٍ**: فرمزٌ
      خارجَها مخالفةٌ لا اجتهادٌ مقبولٌ.
    * «فحصٌ يحكُمُ على الشجرةِ الحاضرةِ» قاعدةٌ مكتوبةٌ لا استنباطٌ: دالّةُ
      فحصٍ لا تأخذُ `tmp_path` ويذكرُ متنُها `REPO_ROOT`، في ملفٍّ يستوردُ
      الأداةَ أو يُسمّي مسارَها في ثابتٍ. وهي عينُ قاعدةِ
      `guard_enforcement_closure.py` — قصدًا، فلا معياران لشيءٍ واحدٍ.
    * الأداةُ **لا تُصنِّفُ الملفَّ حسبَ مجلَّدِه**: `tools/stubs` و
      `tools/migrations` تُقاسُ كغيرِها، ومن أرادَ استثناءً أعلنَه سببًا
      مُصنَّفًا في الترويسةِ.

الاستعمال:
    python tools/governance/enforcement_path_ledger.py
    python tools/governance/enforcement_path_ledger.py --json
    python tools/governance/enforcement_path_ledger.py --root /مسار/استنساخٍ

رموزُ الخروج:
    0 = لا مخالفةَ · 1 = مخالفةٌ مقيسةٌ · 2 = **رفضٌ مُصنَّفٌ** (القياسُ لم يُجرَ)
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

#: جذرُ الأدواتِ المقيسُ — كلُّ ما تحتَه يُقاسُ بلا استثناءِ مجلَّدٍ.
TOOL_ROOT = Path("tools")

WORKFLOWS_DIR = Path(".github/workflows")

#: نافذةُ قراءةِ الإعلانِ من أوّلِ الملفِّ — حدٌّ مكتوبٌ لا تقديرٌ.
HEADER_WINDOW_LINES = 60

#: مفتاحُ الإعلانِ كما يُكتَبُ في الترويسةِ (يُقرأُ بعدَ تجريدِ التشكيلِ).
DECL_KEY = "طريق الإنفاذ"

#: رموزُ **طريقِ إنفاذٍ قائمٍ** — تُقارَنُ بالواقعِ فتُكذَّبُ إن كذبَت.
WIRED_MARKS = ("CI_STEP", "CI_PYTEST", "COVERED_TEST")

#: رموزُ **سببِ تركِ الربطِ** — مفرداتٌ مغلقةٌ لا يُزادُ فيها إلّا ببندِ عملٍ.
REASON_MARKS = (
    "NEEDS_LIVE_DB",        # يلزمُه رابطُ قاعدةِ بياناتٍ حيٍّ فيرفضُ بلا سرٍّ
    "NEEDS_RUN_INPUT",      # يلزمُه مُدخَلٌ لا تملكُه دفعةٌ (‏حِملُ تشغيلٍ منتهٍ)
    "NEEDS_LIVE_SECRET",    # يلزمُه سرُّ خدمةٍ بيدِ المالكِ
    "ONE_SHOT_MIGRATION",   # هجرةٌ تُشغَّلُ مرّةً ولا تُعادُ في كلِّ دفعةٍ
    "REPORT_NO_VERDICT",    # يطبعُ تقريرًا ولا يحكُمُ، فلا معنى لبوّابةٍ منه
    "OWNER_HELD_VERDICT",   # حكمُه اليومَ معلَّقٌ على قرارِ مالكٍ لا على شِفرةٍ
    "TEST_FIXTURE_STUB",    # سِنادٌ للفحوصِ لا أداةُ حوكمةٍ
    "LIBRARY",              # لا مدخلَ تشغيلٍ له أصلًا
    "PENDING_GATE_ITEM",    # ربطُه مشروعٌ ومؤجَّلٌ ببندِ عملٍ **مُسمّى** لا بنيّةٍ
)

#: مِرساةُ سببِ التأجيلِ — سببٌ «لاحقًا» بلا بندٍ مُسمّى وعدٌ لا التزامٌ.
ITEM_ANCHOR_RE = re.compile(r"WI-\d{3}")

ALL_MARKS = WIRED_MARKS + REASON_MARKS

KIND_ENTRYPOINT = "ENTRYPOINT_GUARDED"
KIND_IMPORT_RUN = "RUNS_AT_IMPORT"
KIND_LIBRARY = "LIBRARY"

PYTEST_TARGET_RE = re.compile(r"tests/[A-Za-z0-9_./-]*")
RUN_KEY_RE = re.compile(r"^(\s*)(?:-\s+)?run:\s*(.*)$")
MARK_RE = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b")

_TASHKEEL = {chr(c) for c in range(0x064B, 0x0653)} | {"\u0640", "\u0670"}


def normalize(text: str) -> str:
    """يُجرِّدُ التشكيلَ ويُوحِّدُ المسافاتِ — النصُّ يُقارَنُ بمعناهُ لا بشكلِه."""
    plain = "".join(ch for ch in unicodedata.normalize("NFC", text) if ch not in _TASHKEEL)
    return re.sub(r"\s+", " ", plain).strip()


class UnparsableSource(Exception):
    """مصدرٌ لا يُحلَّلُ نحويًّا — يُرفَعُ ولا يُبتلَعُ.

    لو قُرِئَ سكوتُ المُحلِّلِ «مكتبةٌ بلا مدخلٍ» لصارَ ملفٌّ معطوبٌ سببًا صامتًا
    في إعفاءِ أداةٍ من الإعلانِ. والرفضُ المُصنَّفُ أصدقُ من حكمٍ مبنيٍّ على
    قراءةٍ فاشلةٍ.
    """


@dataclass
class ToolRecord:
    """ملفٌّ واحدٌ في `tools/`: نوعُه · قدرتُه على الحكمِ · طريقُه · إعلانُه."""

    path: str
    kind: str
    verdict_capable: bool
    wiring: str = "NONE"
    wiring_evidence: str = ""
    declared_mark: str = ""
    declared_text: str = ""


@dataclass
class Report:
    """حِملُ القياسِ — يُطبَعُ نصًّا أو JSON، ولا يُخترَعُ منه رقمٌ."""

    records: list[ToolRecord] = field(default_factory=list)
    violations: list[dict[str, str]] = field(default_factory=list)
    notes: list[dict[str, str]] = field(default_factory=list)
    refusal: str = ""


def _v(kind: str, detail: str) -> dict[str, str]:
    return {"kind": kind, "detail": detail}


# ── تصنيفُ الملفِّ من مصدرِه ──────────────────────────────────────────────────


def classify_kind(source: str, label: str = "<مصدرٌ بلا اسمٍ>") -> str:
    """قابلٌ للتشغيلِ بحرسِ `__main__` · أو يعملُ عندَ الاستيرادِ · أو مكتبةٌ."""
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise UnparsableSource(f"{label}: {exc}") from exc
    for node in tree.body:
        if isinstance(node, ast.If) and "__main__" in ast.dump(node.test):
            return KIND_ENTRYPOINT
    for node in tree.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            return KIND_IMPORT_RUN
    return KIND_LIBRARY


def is_verdict_capable(source: str, label: str = "<مصدرٌ بلا اسمٍ>") -> bool:
    """هل يخرجُ الملفُّ برمزٍ غيرِ صفرٍ في شِفرتِه — أي يحكُمُ لا يحكي؟"""
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise UnparsableSource(f"{label}: {exc}") from exc
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            named_exit = (
                (isinstance(func, ast.Attribute) and func.attr == "exit")
                or (isinstance(func, ast.Name) and func.id in ("exit", "SystemExit"))
            )
            if named_exit:
                for arg in node.args:
                    if not (isinstance(arg, ast.Constant) and arg.value in (0, None)):
                        return True
        if isinstance(node, ast.Raise):
            exc_node = node.exc
            name = ""
            if isinstance(exc_node, ast.Call) and isinstance(exc_node.func, ast.Name):
                name = exc_node.func.id
            elif isinstance(exc_node, ast.Name):
                name = exc_node.id
            if name == "SystemExit":
                return True
    return False


def read_declaration(source: str) -> tuple[str, str]:
    """رمزُ الإعلانِ ونصُّه من نافذةِ الترويسةِ — أو فراغانِ إن لم يُعلَنْ."""
    window = source.splitlines()[:HEADER_WINDOW_LINES]
    for line in window:
        plain = normalize(line)
        if DECL_KEY not in plain:
            continue
        tail = plain.split(DECL_KEY, 1)[1].lstrip(": ").strip()
        match = MARK_RE.search(tail)
        mark = match.group(0) if match else ""
        return mark, tail
    return "", ""


# ── قراءةُ وظائفِ CI ──────────────────────────────────────────────────────────


def run_blocks(text: str) -> list[str]:
    """نصوصُ خطواتِ `run:` وحدَها — لا تعليقٌ ولا اسمُ خطوةٍ يُقرأُ تشغيلًا."""
    blocks: list[str] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = RUN_KEY_RE.match(lines[i])
        if not m:
            i += 1
            continue
        indent, inline = len(m.group(1)), m.group(2).strip()
        body = [] if inline in ("|", ">", "|-", ">-", "") else [inline]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if not nxt.strip():
                body.append("")
                i += 1
                continue
            if len(nxt) - len(nxt.lstrip()) <= indent:
                break
            body.append(nxt.strip())
            i += 1
        blocks.append("\n".join(body))
    return blocks


def workflow_runs(root: Path) -> tuple[list[str], str]:
    """كلُّ خطواتِ التشغيلِ في كلِّ مسارِ عملٍ — أو رفضٌ إن لا مسارَ."""
    directory = root / WORKFLOWS_DIR
    if not directory.is_dir():
        return [], f"WORKFLOWS_MISSING: {WORKFLOWS_DIR}"
    files = sorted(p for p in directory.iterdir() if p.suffix in (".yml", ".yaml"))
    if not files:
        return [], f"WORKFLOWS_MISSING: {WORKFLOWS_DIR}"
    blocks: list[str] = []
    for wf in files:
        blocks.extend(run_blocks(wf.read_text(encoding="utf-8")))
    return blocks, ""


def pytest_targets(blocks: list[str]) -> list[str]:
    """أهدافُ `pytest` المذكورةُ في خطواتِ التشغيلِ — نصًّا كما كُتِبَت."""
    targets: list[str] = []
    for block in blocks:
        for line in block.splitlines():
            if "pytest" not in line:
                continue
            targets.extend(PYTEST_TARGET_RE.findall(line))
    return list(dict.fromkeys(targets))


def covered_by_pytest(path: str, targets: list[str]) -> str:
    """اسمُ الهدفِ الذي يشملُ هذا الملفَّ، أو نصٌّ فارغٌ إن لم يشملْه هدفٌ."""
    for target in targets:
        if target == path:
            return target
        prefix = target if target.endswith("/") else target + "/"
        if path.startswith(prefix):
            return target
    return ""


def covered_test_files(root: Path, targets: list[str]) -> list[Path]:
    """ملفّاتُ الفحصِ التي يشملُها استدعاءُ `pytest` في CI فعلًا."""
    found: list[Path] = []
    for target in targets:
        candidate = root / target
        if candidate.is_file():
            found.append(candidate)
        elif candidate.is_dir():
            found.extend(sorted(candidate.rglob("test_*.py")))
    return list(dict.fromkeys(found))


def binds_tool(source: str, stem: str, label: str = "<مصدرٌ بلا اسمٍ>") -> bool:
    """هل يربطُ الملفُّ نفسَه بالأداةِ استيرادًا أو ثابتَ مسارٍ — لا وصفًا؟"""
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise UnparsableSource(f"{label}: {exc}") from exc
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(stem == a.name.split(".")[-1] for a in node.names):
                return True
        elif isinstance(node, ast.ImportFrom):
            if node.module and stem == node.module.split(".")[-1]:
                return True
        elif isinstance(node, ast.Assign):
            expr = ast.unparse(node.value)
            if stem in expr and any(
                anchor in expr for anchor in ("REPO_ROOT", "__file__", "Path(", "parents")
            ):
                return True
    return False


def real_tree_tests(source: str, label: str = "<مصدرٌ بلا اسمٍ>") -> list[str]:
    """أسماءُ دوالِّ الفحصِ التي لا تأخذُ `tmp_path` ويذكرُ متنُها `REPO_ROOT`."""
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise UnparsableSource(f"{label}: {exc}") from exc
    names: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef) or not node.name.startswith("test"):
            continue
        args = {a.arg for a in node.args.args} | {a.arg for a in node.args.kwonlyargs}
        if "tmp_path" in args or "tmp_path_factory" in args:
            continue
        body_names = {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}
        if "REPO_ROOT" in body_names:
            names.append(node.name)
    return names


# ── القياسُ ───────────────────────────────────────────────────────────────────


def measure_wiring(
    record: ToolRecord, root: Path, blocks: list[str], targets: list[str], tests: list[Path]
) -> None:
    """يُثبِتُ طريقَ الإنفاذِ المقيسَ لهذا الملفِّ — أو يتركُه `NONE`."""
    for block in blocks:
        if record.path in block:
            first = next(
                (ln.strip() for ln in block.splitlines() if record.path in ln), record.path
            )
            record.wiring, record.wiring_evidence = "CI_STEP", first
            return
    target = covered_by_pytest(record.path, targets)
    if target:
        record.wiring, record.wiring_evidence = "CI_PYTEST", f"هدفُ pytest: {target}"
        return
    stem = Path(record.path).stem
    for test in tests:
        label = str(test.relative_to(root)) if test.is_relative_to(root) else str(test)
        source = test.read_text(encoding="utf-8")
        if not binds_tool(source, stem, label):
            continue
        live = real_tree_tests(source, label)
        if live:
            record.wiring = "COVERED_TEST"
            record.wiring_evidence = f"{label}::{live[0]}"
            return


def judge(record: ToolRecord) -> list[dict[str, str]]:
    """أحكامُ صفٍّ واحدٍ: إعلانٌ غائبٌ · رمزٌ مجهولٌ · إعلانٌ يُكذِّبُه الواقعُ."""
    found: list[dict[str, str]] = []
    runnable = record.kind in (KIND_ENTRYPOINT, KIND_IMPORT_RUN)
    mark, wiring = record.declared_mark, record.wiring

    if mark and mark not in ALL_MARKS:
        found.append(_v(
            "ENFORCEMENT_PATH_UNKNOWN_REASON",
            f"{record.path}: رمزٌ خارجَ المفرداتِ المغلقةِ «{mark}» — "
            f"المسموحُ: {' · '.join(ALL_MARKS)}",
        ))
        return found

    if not mark:
        if runnable and wiring == "NONE":
            found.append(_v(
                "ENFORCEMENT_PATH_UNDECLARED",
                f"{record.path}: {record.kind} ولا خطوةَ تشغيلٍ ولا فحصَ يشملُه، "
                "وترويستُه لا تُعلِنُ «طريقُ الإنفاذ» — صمتٌ لا نقصٌ مُعلَنٌ",
            ))
        return found

    if mark == "PENDING_GATE_ITEM" and not ITEM_ANCHOR_RE.search(record.declared_text):
        found.append(_v(
            "ENFORCEMENT_PATH_REASON_UNANCHORED",
            f"{record.path}: يُعلِنُ تأجيلَ الربطِ ولا يُسمّي بندَ عملٍ (`WI-###`) — "
            "«لاحقًا» بلا مِرساةٍ وعدٌ لا التزامٌ",
        ))
        return found

    if mark in WIRED_MARKS and wiring == "NONE":
        found.append(_v(
            "ENFORCEMENT_PATH_FALSE",
            f"{record.path}: يُعلِنُ «{mark}» ولا يقيسُ القياسُ له طريقًا — "
            "إعلانٌ أكبرُ من الواقعِ",
        ))
    elif mark in WIRED_MARKS and wiring != mark:
        found.append(_v(
            "ENFORCEMENT_PATH_FALSE",
            f"{record.path}: يُعلِنُ «{mark}» والمقيسُ «{wiring}» "
            f"({record.wiring_evidence}) — الطريقُ غيرُ الذي أُعلِنَ",
        ))
    elif mark in REASON_MARKS and wiring != "NONE":
        found.append(_v(
            "ENFORCEMENT_PATH_STALE",
            f"{record.path}: يُعلِنُ سببَ تركِ الربطِ «{mark}» وقد صارَ مربوطًا "
            f"«{wiring}» ({record.wiring_evidence}) — إعلانٌ تخلَّفَ عن الواقعِ",
        ))
    elif mark == "LIBRARY" and record.kind != KIND_LIBRARY:
        found.append(_v(
            "ENFORCEMENT_PATH_STALE",
            f"{record.path}: يُعلِنُ «LIBRARY» والمقيسُ «{record.kind}» — "
            "ملفٌّ يُشغَّلُ لا يُعلَنُ مكتبةً",
        ))
    return found


def measure(root: Path) -> Report:
    """يقرأُ الأدواتَ ووظائفَ CI ويحكُمُ — أو يرفضُ رفضًا مُصنَّفًا."""
    report = Report()
    tools_dir = root / TOOL_ROOT
    if not tools_dir.is_dir():
        report.refusal = f"TOOLS_MISSING: {TOOL_ROOT}"
        return report
    blocks, refusal = workflow_runs(root)
    if refusal:
        report.refusal = refusal
        return report
    targets = pytest_targets(blocks)
    tests = covered_test_files(root, targets)

    sources = sorted(p for p in tools_dir.rglob("*.py"))
    if not sources:
        report.refusal = f"TOOLS_MISSING: {TOOL_ROOT} بلا ملفٍّ واحدٍ"
        return report

    try:
        for path in sources:
            rel = str(path.relative_to(root))
            text = path.read_text(encoding="utf-8")
            record = ToolRecord(
                path=rel,
                kind=classify_kind(text, rel),
                verdict_capable=is_verdict_capable(text, rel),
            )
            record.declared_mark, record.declared_text = read_declaration(text)
            measure_wiring(record, root, blocks, targets, tests)
            report.records.append(record)
    except UnparsableSource as exc:
        report.refusal = f"SOURCE_UNPARSABLE: {exc}"
        report.records = []
        return report

    for record in report.records:
        report.violations.extend(judge(record))

    kinds = {k: sum(1 for r in report.records if r.kind == k)
             for k in (KIND_ENTRYPOINT, KIND_IMPORT_RUN, KIND_LIBRARY)}
    report.notes.append(_v(
        "KIND_TALLY",
        f"ملفّاتٌ مقيسةٌ {len(report.records)} · بحرسِ `__main__` {kinds[KIND_ENTRYPOINT]} · "
        f"تعملُ عندَ الاستيرادِ {kinds[KIND_IMPORT_RUN]} · مكتبةٌ بلا مدخلٍ {kinds[KIND_LIBRARY]}",
    ))
    unwired = [r for r in report.records
               if r.wiring == "NONE" and r.kind in (KIND_ENTRYPOINT, KIND_IMPORT_RUN)]
    capable = [r.path for r in unwired if r.verdict_capable]
    report.notes.append(_v(
        "VERDICT_CAPABLE_UNWIRED",
        f"أدواتٌ تحكُمُ برمزِ خروجٍ ولا يُشغِّلُها شيءٌ: {len(capable)}"
        + (f" — {' · '.join(capable)}" if capable else "")
        + " · إبلاغٌ لا إسقاطٌ: الإعلانُ وحدَه مُلزِمٌ",
    ))
    reasons: dict[str, int] = {}
    for record in report.records:
        if record.declared_mark in REASON_MARKS:
            reasons[record.declared_mark] = reasons.get(record.declared_mark, 0) + 1
    report.notes.append(_v(
        "REASON_TALLY",
        "أسبابٌ مُعلَنةٌ لِتركِ الربطِ: "
        + (" · ".join(f"{k} {v}" for k, v in sorted(reasons.items())) if reasons else "لا شيءَ"),
    ))
    return report


# ── الطباعةُ والمدخلُ ─────────────────────────────────────────────────────────


def render(report: Report) -> str:
    lines = ["[ENFORCEMENT PATH] كلُّ أداةٍ قابلةٍ للتشغيلِ: طريقُها أو سببُها"]
    for record in report.records:
        if record.wiring != "NONE":
            lines.append(f"  {record.path} · {record.wiring} — {record.wiring_evidence}")
        elif record.declared_mark:
            lines.append(f"  {record.path} · {record.kind} · مُعلَنٌ: {record.declared_text}")
    for note in report.notes:
        lines.append(f"  ملاحظة · {note['kind']}: {note['detail']}")
    if report.violations:
        lines.append(f"[ENFORCEMENT PATH] ✗ مخالفات: {len(report.violations)}")
        for violation in report.violations:
            lines.append(f"  {violation['kind']}: {violation['detail']}")
    else:
        lines.append("  ✓ لا مخالفةَ مقيسةً: كلُّ أداةٍ قابلةٍ للتشغيلِ لها طريقٌ أو سببٌ مُعلَنٌ.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="سجلُّ طرقِ الإنفاذِ: أداةٌ لا يُشغِّلُها شيءٌ تُعلِنُ سببَها أو تسقُط",
    )
    parser.add_argument("--root", default=str(REPO_ROOT), help="جذرُ المستودعِ المقيسُ")
    parser.add_argument("--json", action="store_true", help="حِملُ القياسِ JSON")
    args = parser.parse_args(argv)

    report = measure(Path(args.root).resolve())
    if args.json:
        payload = {
            "records": [asdict(r) for r in report.records],
            "violations": report.violations,
            "notes": report.notes,
            "refusal": report.refusal,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=1))
    elif report.refusal:
        print(f"[ENFORCEMENT PATH] ✗ القياسُ مرفوضٌ: {report.refusal}")
    else:
        print(render(report))

    if report.refusal:
        return 2
    return 1 if report.violations else 0


if __name__ == "__main__":
    sys.exit(main())
