#!/usr/bin/env python3
"""إغلاقُ إنفاذِ الحرسِ — «يُشغَّلُ في كلِّ دفعةٍ» دعوى تُقاسُ لا عبارةٌ تُقرَأُ (W-077).

الهدف:
    أن تكونَ كلُّ دعوى مكتوبةٍ في سجلِّي الاكتشافاتِ والمخاطرِ تقولُ عن ملفٍّ في
    الشجرةِ إنَّه **يُشغَّلُ في كلِّ دفعةٍ** دعوى **مقيسةً**: يُطلَبُ لها طريقُ
    إنفاذٍ لا تستطيعُ دفعةٌ أن تتجاوزَه — خطوةٌ في وظيفةِ CI تُسمّي الملفَّ، أو
    فحصٌ يشملُه استدعاءُ `pytest` في CI، أو فحصٌ يجري في CI ويحكُمُ على
    **الشجرةِ الحقيقيّةِ** لا على شجرةٍ مؤقَّتةٍ. فما لا طريقَ له مخالفةٌ مُسمّاةٌ.
النطاق:
    `docs/governance/work/DISCOVERIES.md` · `docs/governance/work/RISK_REGISTER.md`
    · `.github/workflows/*.yml` · وملفّاتُ الفحوصِ التي تشملُها استدعاءاتُ
    `pytest` في تلك الوظائفِ. لا شبكةَ ولا قاعدةَ بياناتٍ ولا سرَّ، ولا تكتبُ
    الأداةُ بايتًا في شجرةٍ تحكمُ عليها. مكتبةٌ قياسيّةٌ وحدَها (‏`RK-010`).
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-31
تاريخ آخر تعديل: 2026-08-31

لماذا أداةٌ لا فقرةٌ:
    قِيسَ في `DISC-037` أنَّ أربعةَ اكتشافاتٍ مفتوحةٍ تُسنِدُ بقاءَها إلى حرسٍ
    «قائمٍ مقامَها يُشغَّلُ في كلِّ دفعةٍ»، وأنَّ اثنَينِ من ذلك الحرسِ
    (`state_document_drift.py` و`mutation_probe.py`) **لا تُشغِّلُهما وظيفةٌ في
    CI ولا فحصٌ يحكُمُ على الشجرةِ الحقيقيّةِ**: فحوصُهما كلُّها على شجرةٍ
    مؤقَّتةٍ تُثبِتُ **قاعدةَ** الأداةِ ولا تُثبِتُ **حكمَها على المستودعِ**.
    فوثيقةُ حالةٍ متأخِّرةٌ ما كانت لتُحمِّرَ دفعةً واحدةً. والدعوى المكتوبةُ لا
    تُصلِحُ نفسَها بمرورِ الوقتِ: هي عينُ ما يُحاسِبُ عليه المشروعُ — ادِّعاءٌ
    أكبرُ من الواقعِ. فما يمنعُ تكرارَه قياسٌ يسقُطُ حينَ تُكتَبُ الدعوى بلا
    إنفاذٍ.

الحدُّ المُعلَنُ — لا مطويٌّ:
    * تقيسُ الأداةُ **وجودَ طريقِ إنفاذٍ** لا **صدقَ ما يقيسُه الحرسُ**: فحصٌ
      يذكرُ `REPO_ROOT` ولا يُؤكِّدُ شيئًا ذا معنًى يمرُّ من هنا. صدقُ الحكمِ
      واجبُ من يكتبُ الفحصَ، وحرسُه مراجعةٌ بشريّةٌ ومِسبارُ الطفرةِ.
    * «فحصٌ يحكُمُ على الشجرةِ الحقيقيّةِ» **قاعدةٌ مكتوبةٌ لا استنباطٌ**: دالّةُ
      فحصٍ لا تأخذُ `tmp_path` ويذكرُ متنُها الاسمَ `REPO_ROOT`، في ملفٍّ
      **يستوردُ الأداةَ أو يُسمّي مسارَها في ثابتٍ** لا في نصٍّ وصفيٍّ. فمن قاسَ
      الشجرةَ الحقيقيّةَ باسمٍ آخرَ لا تراهُ هذه الأداةُ — نقصٌ يُعلَنُ.
    * الدعوى تُقرأُ في **الجُملةِ التي فيها العبارةُ** لا في الخليّةِ كلِّها،
      وحدُّ الجُملةِ فواصلُ مكتوبةٌ (`CLAUSE_SEPARATORS`) لا تقديرٌ: خليّةٌ
      واحدةٌ تحملُ جملًا كثيرةً، وحملُ ملفّاتِ الخليّةِ كلِّها على عبارةٍ
      واحدةٍ **ادِّعاءٌ عن الكاتبِ** لا قياسٌ لِما كتبَ. ولا يُقطَعُ عندَ
      النُّقطةِ لأنَّ المساراتِ تحملُها (`.py`).
    * كلُّ صفٍّ في السجلَّينِ يُقرأُ مُلزِمًا ولا يُستثنى بحالةٍ: دعوى تبقى
      مكتوبةً تبقى مُلزِمةً حتّى تُصحَّحَ أو تُرفَعَ. وهذا **أشدُّ** من قراءةِ
      عمودِ الحالةِ، وقُصِدَ كذلك: صفوفُ السجلَّينِ فيها فواصلُ أعمدةٍ داخلَ
      أوامرَ مكتوبةٍ، فقراءةُ الحالةِ بالعمودِ غيرُ موثوقةٍ (‏عَطبُ شكلٍ مُقيَّدٌ
      في `DISC-037`).
    * جردُ «حرسٍ غيرِ موصولٍ بـCI» **إبلاغٌ لا إسقاطٌ**: ليس كلُّ أداةٍ يجبُ أن
      تُشغَّلَ في كلِّ دفعةٍ، وإنَّما تُلزِمُ الدعوى المكتوبةُ وحدَها.

الاستعمال:
    python tools/governance/guard_enforcement_closure.py
    python tools/governance/guard_enforcement_closure.py --json
    python tools/governance/guard_enforcement_closure.py --root /مسار/استنساخٍ

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

#: السجلّاتُ التي تُقرأُ منها الدعاوى — قائمةٌ مكتوبةٌ لا مُكتشَفةٌ.
REGISTERS = (
    Path("docs/governance/work/DISCOVERIES.md"),
    Path("docs/governance/work/RISK_REGISTER.md"),
)

WORKFLOWS_DIR = Path(".github/workflows")

#: جذورُ الأدواتِ التي يُجرَدُ اتِّصالُها بـCI — إبلاغٌ لا إسقاطٌ.
TOOL_ROOTS = (Path("tools/governance"), Path("tools/audit"))

#: الدعوى المُلزِمةُ بنصِّها بعدَ تجريدِ التشكيلِ.
CLAIM_PHRASE = "في كل دفعة"

#: حدُّ الجُملةِ التي تُقرأُ فيها الدعوى — فواصلُ مكتوبةٌ لا تقديرٌ.
CLAUSE_SEPARATORS = ("\u061b", "\u00b7", ":", "\n", "\u060c")

PATH_RE = re.compile(r"(?:tools|tests)/[A-Za-z0-9_./-]+\.py")
PYTEST_TARGET_RE = re.compile(r"tests/[A-Za-z0-9_./-]*")
RUN_KEY_RE = re.compile(r"^(\s*)(?:-\s+)?run:\s*(.*)$")

_TASHKEEL = {chr(c) for c in range(0x064B, 0x0653)} | {"\u0640", "\u0670"}


def normalize(text: str) -> str:
    """يُجرِّدُ التشكيلَ ويُوحِّدُ المسافاتِ — النصُّ يُقارَنُ بمعناهُ لا بشكلِه."""
    plain = "".join(ch for ch in unicodedata.normalize("NFC", text) if ch not in _TASHKEEL)
    return re.sub(r"\s+", " ", plain).strip()


@dataclass
class Claim:
    """دعوى واحدةٌ: ملفٌّ قيلَ عنه إنَّه يُشغَّلُ في كلِّ دفعةٍ، وأينَ قيلَ."""

    register: str
    row_id: str
    path: str
    verdict: str = "UNENFORCED"
    evidence: str = ""


@dataclass
class Report:
    """حِملُ القياسِ — يُطبَعُ نصًّا أو JSON، ولا يُخترَعُ منه رقمٌ."""

    claims: list[Claim] = field(default_factory=list)
    violations: list[dict[str, str]] = field(default_factory=list)
    notes: list[dict[str, str]] = field(default_factory=list)
    refusal: str = ""

    @property
    def enforced(self) -> int:
        return sum(1 for c in self.claims if c.verdict != "UNENFORCED")


def _v(kind: str, detail: str) -> dict[str, str]:
    return {"kind": kind, "detail": detail}


# ── قراءةُ السجلَّينِ ─────────────────────────────────────────────────────────


def table_rows(text: str) -> list[list[str]]:
    """صفوفُ جداولِ Markdown خامًا — بلا افتراضِ عددِ أعمدةٍ."""
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if all(set(c) <= {"-", ":"} and c for c in cells):
            continue
        rows.append(cells)
    return rows


def row_identifier(cells: list[str]) -> str:
    """معرِّفُ الصفِّ كما كُتِبَ — أو «صفٌّ بلا معرِّفٍ» إن غابَ."""
    for cell in cells:
        m = re.search(r"\b(?:DISC|RK)-\d{3}\b", cell)
        if m:
            return m.group(0)
    return "صفٌّ بلا معرِّفٍ"


def claimed_paths(cell: str) -> list[str]:
    """ملفّاتُ الجُملةِ التي فيها العبارةُ — لا كلُّ ملفٍّ في الخليّةِ."""
    text = normalize(cell)
    for sep in CLAUSE_SEPARATORS[1:]:
        text = text.replace(sep, CLAUSE_SEPARATORS[0])
    found: list[str] = []
    for clause in text.split(CLAUSE_SEPARATORS[0]):
        if CLAIM_PHRASE in clause:
            found.extend(PATH_RE.findall(clause))
    return list(dict.fromkeys(found))


def read_claims(root: Path) -> tuple[list[Claim], str]:
    """كلُّ ملفٍّ ذُكِرَ في خليّةٍ فيها الدعوى المُلزِمةُ — بلا استثناءِ حالةٍ."""
    claims: list[Claim] = []
    for register in REGISTERS:
        target = root / register
        if not target.is_file():
            return [], f"REGISTER_MISSING: {register}"
        rows = table_rows(target.read_text(encoding="utf-8"))
        for cells in rows:
            row_id = row_identifier(cells)
            for cell in cells:
                for path in claimed_paths(cell):
                    claims.append(Claim(register=str(register), row_id=row_id, path=path))
    return claims, ""


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


# ── فحصٌ يحكُمُ على الشجرةِ الحقيقيّةِ ────────────────────────────────────────


class UnparsableSource(Exception):
    """ملفُّ فحصٍ لا يُحلَّلُ نحويًّا.

    يُرفَعُ ولا يُبتلَعُ: لو قُرِئَ سكوتُ المُحلِّلِ «لا رباطَ» لصارَ ملفٌّ معطوبٌ
    سببًا صامتًا في إسقاطِ دعوى صحيحةٍ — والرفضُ المُصنَّفُ أصدقُ من حكمٍ مبنيٍّ
    على قراءةٍ فاشلةٍ.
    """


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
            # ثابتُ مسارٍ لا نصٌّ وصفيٌّ: يُشترطُ أن يذكرَ التعبيرُ الأداةَ
            # **وجذرَ المستودعِ** معًا، فلا يُقرأُ رباطًا جدولٌ مُصطنعٌ في
            # فحصٍ مجاورٍ يذكرُ اسمَ الأداةِ مثالًا لا حرسًا.
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


def judge(claim: Claim, root: Path, blocks: list[str], targets: list[str], tests: list[Path]) -> None:
    """يُسنِدُ لكلِّ دعوى طريقَ إنفاذِها المقيسَ — أو يتركُها غيرَ منفَذةٍ."""
    if not (root / claim.path).is_file():
        claim.verdict = "PATH_MISSING"
        claim.evidence = "لا ملفَّ بهذا المسارِ في الشجرةِ"
        return

    for block in blocks:
        if claim.path in block:
            claim.verdict = "CI_STEP"
            claim.evidence = "خطوةُ تشغيلٍ في CI تُسمّي المسارَ"
            return

    target = covered_by_pytest(claim.path, targets)
    if target:
        claim.verdict = "CI_PYTEST"
        claim.evidence = f"يشملُه استدعاءُ pytest في CI: {target}"
        return

    stem = Path(claim.path).stem
    for test_file in tests:
        source = test_file.read_text(encoding="utf-8")
        label = str(test_file)
        if not binds_tool(source, stem, label):
            continue
        real = real_tree_tests(source, label)
        if real:
            rel = test_file.relative_to(root)
            claim.verdict = "REAL_TREE_TEST"
            claim.evidence = f"{rel}::{real[0]} يحكُمُ على الشجرةِ الحقيقيّةِ"
            return

    claim.verdict = "UNENFORCED"
    claim.evidence = "لا خطوةَ CI تُسمّيه، ولا فحصَ في CI يحكُمُ به على الشجرةِ الحقيقيّةِ"


def unwired_tools(root: Path, blocks: list[str]) -> list[str]:
    """أدواتٌ في الشجرةِ لا تُسمّيها خطوةُ تشغيلٍ — جردٌ يُعلَنُ ولا يُسقِطُ."""
    unwired: list[str] = []
    joined = "\n".join(blocks)
    for tool_root in TOOL_ROOTS:
        directory = root / tool_root
        if not directory.is_dir():
            continue
        for tool in sorted(directory.glob("*.py")):
            rel = str(tool.relative_to(root))
            if rel not in joined:
                unwired.append(rel)
    return unwired


def measure(root: Path) -> Report:
    """القياسُ كلُّه في دالّةٍ واحدةٍ تُعادُ — ولا تكتبُ في الشجرةِ."""
    report = Report()

    claims, refusal = read_claims(root)
    if refusal:
        report.refusal = refusal
        return report
    blocks, refusal = workflow_runs(root)
    if refusal:
        report.refusal = refusal
        return report

    targets = pytest_targets(blocks)
    tests = covered_test_files(root, targets)
    report.claims = claims

    for claim in claims:
        try:
            judge(claim, root, blocks, targets, tests)
        except UnparsableSource as exc:
            report.claims = []
            report.violations.clear()
            report.notes.clear()
            report.refusal = f"SOURCE_UNPARSABLE: {exc}"
            return report
        if claim.verdict == "UNENFORCED":
            report.violations.append(
                _v(
                    "PUSH_CLAIM_UNENFORCED",
                    f"{claim.row_id} ({claim.register}): `{claim.path}` مُدَّعًى أنَّه "
                    "يُشغَّلُ في كلِّ دفعةٍ — ولا طريقَ إنفاذٍ مقيسًا: "
                    f"{claim.evidence}",
                )
            )
        elif claim.verdict == "PATH_MISSING":
            report.violations.append(
                _v(
                    "PUSH_CLAIM_PATH_MISSING",
                    f"{claim.row_id} ({claim.register}): `{claim.path}` مُدَّعًى في "
                    "كلِّ دفعةٍ ولا وجودَ له في الشجرةِ",
                )
            )

    report.notes.append(
        _v(
            "CLAIM_TALLY",
            f"دعاوى مقروءةٌ {len(claims)} · منفَذةٌ {report.enforced} · "
            f"غيرُ منفَذةٍ {len(claims) - report.enforced} · "
            f"أهدافُ pytest في CI {len(targets)} · فحوصٌ مشمولةٌ {len(tests)}",
        )
    )
    unwired = unwired_tools(root, blocks)
    report.notes.append(
        _v(
            "UNWIRED_TOOL_INVENTORY",
            f"أدواتٌ لا تُسمّيها خطوةُ تشغيلٍ في CI: {len(unwired)} — "
            + (" · ".join(unwired) if unwired else "لا شيء")
            + " · إبلاغٌ لا إسقاطٌ: تُلزِمُ الدعوى المكتوبةُ وحدَها",
        )
    )
    return report


def render(report: Report) -> None:
    """يطبعُ ما قِيسَ — كلُّ رقمٍ من الحِملِ لا من الظنِّ."""
    print("[GUARD ENFORCEMENT] دعوى «يُشغَّلُ في كلِّ دفعةٍ» تُقابَلُ بطريقِ إنفاذِها:")
    for claim in report.claims:
        print(f"  {claim.row_id} · {claim.path} · {claim.verdict} — {claim.evidence}")
    for note in report.notes:
        print(f"  ملاحظة · {note['kind']}: {note['detail']}")
    for violation in report.violations:
        print(f"  مخالفة · {violation['kind']}: {violation['detail']}")
    if not report.violations:
        print("  ✓ لا مخالفةَ مقيسةً: كلُّ دعوى دفعةٍ لها طريقُ إنفاذٍ.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="إغلاقُ إنفاذِ الحرسِ (W-077)")
    parser.add_argument("--root", default=str(REPO_ROOT), help="جذرُ المستودع")
    parser.add_argument("--json", action="store_true", help="إخراجٌ آليٌّ")
    args = parser.parse_args(argv)

    report = measure(Path(args.root).resolve())
    if args.json:
        print(json.dumps(asdict(report), ensure_ascii=False, indent=1))
    else:
        if report.refusal:
            print(f"[GUARD ENFORCEMENT] رفضٌ مُصنَّفٌ: {report.refusal}")
        else:
            render(report)
    if report.refusal:
        return 2
    return 1 if report.violations else 0


if __name__ == "__main__":
    sys.exit(main())
