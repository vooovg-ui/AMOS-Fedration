#!/usr/bin/env python3
"""مِسبارُ الطفرةِ — «الحرسُ مُثبَتٌ» يصيرُ أمرًا يُعادُ لا دعوى تُقرأُ (W-062).

الهدف:
    أن يُثبِتَ المستودعُ **بنفسِه** أنَّ حرسًا يسقُطُ عندَ عودةِ العَطبِ الذي بُنِيَ
    لأجلِه: يُعادُ كلُّ عَطبٍ مُعلَنٍ في `tools/governance/mutation_claims.py` على
    **نسخةٍ معزولةٍ**، وتُشغَّلُ فحوصُ الحرسِ، ويُقاسُ كم فحصًا سقَطَ. فما سقَطَ
    عندَه فحصٌ فأكثرُ دعواهُ **مقيسةٌ**، وما نجَت طفرتُه فدعواهُ **ساقطةٌ** ولو
    كانَت مكتوبةً في سجلٍّ ومقروءةً شهرًا.
النطاق:
    شجرةُ العملِ الحاضرةُ (المصدرُ) · `git` (لنسخِ الشجرةِ وللتحقُّقِ أنَّها لم
    تُمَسَّ) · `pytest` (للتشغيلِ). لا شبكةَ ولا قاعدةَ بياناتٍ ولا سرَّ.
    **ولا تكتبُ الأداةُ سطرًا واحدًا في الشجرةِ التي تحكمُ عليها**: كلُّ طفرةٍ
    تُكتَبُ في مجلَّدٍ مؤقَّتٍ يُمحى، والشجرةُ تُقارَنُ قبلَ التشغيلِ وبعدَه.
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-29
تاريخ آخر تعديل: 2026-08-29

لماذا أداةٌ لا فقرةٌ:
    صارَت «مُجرَّبٌ بطفرةٍ» عبارةً تتكرَّرُ في القيودِ من `W-051` إلى `W-061`، وكلُّ
    مرّةٍ جُرِّبَت **بيدٍ في نسخةٍ مؤقَّتةٍ تُمحى بعدَها**: لا يُعادُ التجريبُ بأمرٍ،
    ولا يعترضُ شيءٌ من أضعفَ حرسًا لاحقًا. وهذا هو `RK-019` في جوهرِه — قيدٌ
    يُقرأُ حرسًا وليس في الشجرةِ ما يقيسُه. فمن هنا: الدعوى بيانٌ في مِلَفٍّ،
    والتجريبُ أمرٌ، والنقصُ مُعلَنٌ.

القاعدةُ المُلزِمةُ:
    الطفرةُ تُقاسُ بـ**عددِ الفحوصِ الساقطةِ** مقابلَ العددِ المُعلَنِ في الدعوى:
    لا يكفي «سقَطَ شيءٌ»، ولا يجوزُ أن يسقُطَ أكثرُ ممّا أُعلِنَ بلا تفسيرٍ —
    فكلا الطرفَينِ مخالفةٌ مُسمّاةٌ، لأنَّ الرقمَ المُعلَنَ في السجلِّ إمّا صادقٌ
    وإمّا لا، ولا ثالثَ.

الحدُّ المُعلَنُ — لا مطويٌّ:
    * لا يُثبِتُ المِسبارُ أنَّ كلَّ حرسٍ في المستودعِ مُجرَّبٌ؛ يُثبِتُ الدعاوى
      **المُسجَّلةَ** فقط. وغيرُ المُسجَّلِ نقصٌ يُعلَنُ ولا يُقرأُ اكتمالًا.
    * الطفرةُ استبدالُ نصٍّ، فهي تُحاكي **عَطبًا بعينِه** لا كلَّ عَطبٍ ممكنٍ.
    * لا يُدَّعى حكمٌ من CI: أحكامُ Actions غيرُ مقروءةٍ (`DISC-006`).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

CLAIMS_SOURCE = Path("tools/governance/mutation_claims.py")
SUMMARY_RE = re.compile(r"(?:(\d+) failed)|(?:(\d+) passed)|(?:(\d+) error)")
COPY_EXCLUDES = ("__pycache__", ".venv", ".pytest_cache", ".ruff_cache")
CAUGHT = "CAUGHT"
SURVIVED = "SURVIVED"
MISCOUNTED = "MISCOUNTED"
STALE = "STALE"


class ProbeRefused(Exception):
    """رفضٌ مُصنَّفٌ: لا يُدَّعى «الحرسُ مُثبَتٌ» ولا «ساقطٌ» بلا تشغيلٍ صحيحٍ."""

    def __init__(self, kind: str, detail: str) -> None:
        super().__init__(f"{kind}: {detail}")
        self.kind = kind
        self.detail = detail


@dataclass
class Outcome:
    """نتيجةُ طفرةٍ واحدةٍ."""

    kind: str
    target: str
    expected_failures: int
    observed_failures: int
    verdict: str
    note: str = ""


@dataclass
class ClaimResult:
    """نتيجةُ دعوى قيدٍ واحدٍ."""

    work: str
    item: str
    tests: list[str]
    baseline_passed: int
    outcomes: list[Outcome] = field(default_factory=list)


@dataclass
class Report:
    """ما يُعلَنُ: نتائجُ الدعاوى والمخالفاتُ والملاحظات."""

    root: str
    claims_source: str
    results: list[ClaimResult] = field(default_factory=list)
    violations: list[tuple[str, str]] = field(default_factory=list)
    notes: list[tuple[str, str]] = field(default_factory=list)


def _run(cmd: list[str], cwd: Path, timeout: int = 900) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError as exc:
        raise ProbeRefused("TOOL_UNAVAILABLE", f"لا يوجدُ الأمرُ «{cmd[0]}»") from exc
    except subprocess.TimeoutExpired as exc:
        raise ProbeRefused(
            "RUN_TIMED_OUT", f"تجاوزَ «{cmd[0]}» {timeout} ثانيةً"
        ) from exc


def git_status(root: Path) -> str:
    """بصمةُ حالةِ الشجرةِ — تُقارَنُ قبلَ التشغيلِ وبعدَه."""
    done = _run(["git", "status", "--porcelain"], root, timeout=120)
    if done.returncode != 0:
        raise ProbeRefused(
            "GIT_FAILED", done.stderr.strip()[:200] or "فشلَ `git status`"
        )
    return done.stdout


def load_claims(root: Path):
    """يُحمَّلُ مِلَفُّ الدعاوى بمسارِه، ويُرفَضُ إن غابَ أو خالفَ عقدَه."""
    source = root / CLAIMS_SOURCE
    if not source.is_file():
        raise ProbeRefused("CLAIMS_SOURCE_MISSING", f"لا يوجدُ {CLAIMS_SOURCE}")
    spec = importlib.util.spec_from_file_location("mutation_claims", source)
    if spec is None or spec.loader is None:
        raise ProbeRefused("CLAIMS_SOURCE_UNLOADABLE", str(source))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    # لا بايتكودَ يُكتَبُ في الشجرةِ الحاكمةِ: التحميلُ نفسُه كتابةٌ لو أُهمِلَ هذا.
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # أيُّ خطأِ تحميلٍ يُترجَمُ رفضًا مُصنَّفًا
        raise ProbeRefused(
            "CLAIMS_SOURCE_UNLOADABLE", f"{type(exc).__name__}: {exc}"
        ) from exc
    finally:
        sys.dont_write_bytecode = previous
    for attribute in ("CLAIMS", "claims_for", "MINIMUM_FAILURES"):
        if not hasattr(module, attribute):
            raise ProbeRefused("CLAIM_CONTRACT_BROKEN", f"غابَ «{attribute}»")
    return module


def selected_claims(module, work: str | None):
    """الدعاوى المطلوبةُ — ويُرفَضُ قيدٌ غيرُ مُسجَّلٍ بدلَ تجاهُلِه."""
    try:
        claims = module.claims_for(work)
    except KeyError as exc:
        raise ProbeRefused("WORK_NOT_REGISTERED", str(exc)) from exc
    if not claims:
        raise ProbeRefused("NO_CLAIMS", "لا دعوى مُسجَّلةً في مِلَفِّ الدعاوى")
    for claim in claims:
        if not claim.tests:
            raise ProbeRefused("CLAIM_CONTRACT_BROKEN", f"دعوى «{claim.work}» بلا فحوصٍ")
        if not claim.mutations:
            raise ProbeRefused(
                "CLAIM_CONTRACT_BROKEN", f"دعوى «{claim.work}» بلا طفراتٍ"
            )
    return claims


def copy_tree(root: Path, destination: Path) -> None:
    """نسخةٌ معزولةٌ **بتاريخِها**: بعضُ الحرسِ يلزمُه `git` في الشجرةِ."""
    try:
        shutil.copytree(
            root,
            destination,
            symlinks=True,
            ignore=shutil.ignore_patterns(*COPY_EXCLUDES),
            dirs_exist_ok=True,
        )
    except OSError as exc:
        raise ProbeRefused("COPY_FAILED", f"{type(exc).__name__}: {exc}") from exc
    if not (destination / ".git").exists():
        raise ProbeRefused("COPY_FAILED", "النسخةُ بلا تاريخِ `git`")


def count_failures(output: str) -> tuple[int, int]:
    """(الساقطُ، الناجحُ) من سطرِ خلاصةِ `pytest` — ويُرفَضُ ما لا يُقرأُ."""
    failed = passed = errors = None
    for line in reversed(output.strip().splitlines()):
        if not any(word in line for word in ("passed", "failed", "error")):
            continue
        found = SUMMARY_RE.findall(line)
        if not found:
            continue
        for fail, ok, err in found:
            if fail:
                failed = int(fail)
            if ok:
                passed = int(ok)
            if err:
                errors = int(err)
        break
    if failed is None and passed is None and errors is None:
        raise ProbeRefused(
            "PYTEST_OUTPUT_UNREADABLE", output.strip()[-200:] or "لا خلاصةَ"
        )
    return (failed or 0) + (errors or 0), passed or 0


def run_tests(copy: Path, tests: list[str]) -> tuple[int, int]:
    """تشغيلُ فحوصِ الحرسِ في النسخةِ — بمُفسِّرِ الجلسةِ نفسِه."""
    done = _run(
        [
            sys.executable,
            "-m",
            "pytest",
            *tests,
            "-q",
            "--tb=no",
            "-p",
            "no:cacheprovider",
        ],
        copy,
    )
    return count_failures(done.stdout + done.stderr)


def probe(root: Path | None = None, work: str | None = None) -> Report:
    """يُعادُ كلُّ عَطبٍ مُعلَنٍ في نسخةٍ معزولةٍ، ويُقاسُ ما سقَطَ من فحوصٍ."""
    root = Path(root or Path.cwd()).resolve()
    if not (root / ".git").exists():
        raise ProbeRefused("GIT_UNAVAILABLE", f"لا تاريخَ `git` في {root}")
    before = git_status(root)
    module = load_claims(root)
    claims = selected_claims(module, work)
    minimum = int(module.MINIMUM_FAILURES)
    report = Report(root=str(root), claims_source=str(CLAIMS_SOURCE))

    with tempfile.TemporaryDirectory(prefix="mutation-probe-") as raw:
        copy = Path(raw) / "tree"
        copy_tree(root, copy)
        for claim in claims:
            for relative in (*claim.tests, *{m.target for m in claim.mutations}):
                if not (copy / relative).is_file():
                    raise ProbeRefused(
                        "PATH_MISSING", f"«{relative}» في دعوى {claim.work}"
                    )
            baseline_failed, baseline_passed = run_tests(copy, list(claim.tests))
            if baseline_failed:
                raise ProbeRefused(
                    "BASELINE_NOT_GREEN",
                    f"فحوصُ {claim.work} تسقُطُ بلا طفرةٍ: {baseline_failed}",
                )
            result = ClaimResult(
                work=claim.work,
                item=claim.item,
                tests=list(claim.tests),
                baseline_passed=baseline_passed,
            )
            for mutation in claim.mutations:
                target = copy / mutation.target
                pristine = target.read_text(encoding="utf-8")
                occurrences = pristine.count(mutation.old)
                if occurrences != 1:
                    result.outcomes.append(
                        Outcome(
                            kind=mutation.kind,
                            target=mutation.target,
                            expected_failures=mutation.expected_failures,
                            observed_failures=-1,
                            verdict=STALE,
                            note=f"النصُّ المُعلَنُ وُجِدَ {occurrences} مرّةً لا مرّةً واحدةً",
                        )
                    )
                    report.violations.append(
                        (
                            "MUTATION_PATTERN_STALE",
                            (
                                f"{claim.work} · {mutation.kind}: الدعوى تصفُ "
                                f"نصًّا غيرَ موجودٍ مرّةً واحدةً في "
                                f"«{mutation.target}» — دعوى لا تُجرَّبُ كدعوى ساقطةٍ."
                            ),
                        )
                    )
                    continue
                try:
                    target.write_text(
                        pristine.replace(mutation.old, mutation.new), encoding="utf-8"
                    )
                    observed, _ = run_tests(copy, list(claim.tests))
                finally:
                    target.write_text(pristine, encoding="utf-8")
                if observed < minimum:
                    verdict = SURVIVED
                    report.violations.append(
                        (
                            "GUARD_SURVIVED_MUTATION",
                            (
                                f"{claim.work} · {mutation.kind}: أُعيدَ العَطبُ "
                                "ولم يسقُطْ فحصٌ واحدٌ — الحرسُ لا يحرسُ ما يُدَّعى."
                            ),
                        )
                    )
                elif observed != mutation.expected_failures:
                    verdict = MISCOUNTED
                    report.violations.append(
                        (
                            "FAILURE_COUNT_MISMATCH",
                            (
                                f"{claim.work} · {mutation.kind}: المُعلَنُ "
                                f"{mutation.expected_failures} والمقيسُ "
                                f"{observed} — الرقمُ المنشورُ في السجلِّ غيرُ مطابقٍ."
                            ),
                        )
                    )
                else:
                    verdict = CAUGHT
                result.outcomes.append(
                    Outcome(
                        kind=mutation.kind,
                        target=mutation.target,
                        expected_failures=mutation.expected_failures,
                        observed_failures=observed,
                        verdict=verdict,
                        note=mutation.note,
                    )
                )
            report.results.append(result)

    if git_status(root) != before:
        report.violations.append(
            (
                "PROBE_WROTE_INTO_TREE",
                (
                    "تغيَّرَت حالةُ الشجرةِ الحاكمةِ أثناءَ التشغيلِ — المِسبارُ "
                    "لا يجوزُ أن يكتبَ فيما يحكمُ عليه."
                ),
            )
        )
    caught = sum(
        1 for res in report.results for out in res.outcomes if out.verdict == CAUGHT
    )
    total = sum(len(res.outcomes) for res in report.results)
    report.notes.append(
        (
            "PROBE_TALLY",
            (
                f"دعاوى مُشغَّلةٌ {len(report.results)} · طفراتٌ {total} · "
                f"مُلتقَطةٌ {caught} · حدُّ القبولِ {minimum} فحصٌ ساقطٌ لكلِّ طفرةٍ."
            ),
        )
    )
    return report


def render(report: Report) -> str:
    """إعلانٌ مقروءٌ: كلُّ طفرةٍ بسطرِها ورقمِها وحكمِها."""
    lines = ["[MUTATION PROBE] الحرسُ يُجرَّبُ بإعادةِ العَطبِ:"]
    for result in report.results:
        lines.append(
            f"  {result.work} · {result.item} · قاعدةٌ خضراءُ "
            f"{result.baseline_passed} فحصًا · فحوصٌ: {' · '.join(result.tests)}"
        )
        for out in result.outcomes:
            observed = "—" if out.observed_failures < 0 else str(out.observed_failures)
            mark = {CAUGHT: "✓", SURVIVED: "✗", MISCOUNTED: "!", STALE: "!"}[
                out.verdict
            ]
            lines.append(
                f"    {mark} {out.kind}: مُعلَنٌ {out.expected_failures} · "
                f"مقيسٌ {observed} · {out.verdict}"
                + (f" — {out.note}" if out.note else "")
            )
    for kind, detail in report.notes:
        lines.append(f"  ملاحظة · {kind}: {detail}")
    for kind, detail in report.violations:
        lines.append(f"  ✗ {kind}: {detail}")
    if not report.violations:
        lines.append("  ✓ كلُّ دعوى مُسجَّلةٍ سقَطَ عندَها ما أُعلِنَ من فحوصٍ — لا مخالفة.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """خروجٌ 0 لا مخالفةَ · 1 مخالفةٌ مقيسةٌ · 2 رفضٌ مُصنَّفٌ."""
    parser = argparse.ArgumentParser(description="تجريبُ دعاوى الحرسِ بإعادةِ العَطبِ")
    parser.add_argument("root", nargs="?", default=".", help="جذرُ المستودع")
    parser.add_argument("--work", default=None, help="قيدٌ بعينِه، مثل W-061")
    parser.add_argument("--json", action="store_true", help="إخراجٌ آليٌّ")
    parser.add_argument("--list", action="store_true", help="سردُ الدعاوى بلا تشغيلٍ")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    try:
        if args.list:
            module = load_claims(root)
            claims = selected_claims(module, args.work)
            for claim in claims:
                print(f"{claim.work} · {claim.item} · طفراتٌ {len(claim.mutations)}")
                for mutation in claim.mutations:
                    print(
                        f"    {mutation.kind} → {mutation.target} · "
                        f"مُعلَنٌ {mutation.expected_failures}"
                    )
            return 0
        report = probe(root, args.work)
    except ProbeRefused as refusal:
        payload = {"refused": refusal.kind, "detail": refusal.detail}
        print(
            json.dumps(payload, ensure_ascii=False)
            if args.json
            else f"[MUTATION PROBE] رفضٌ · {refusal.kind}: {refusal.detail}",
            file=sys.stderr,
        )
        return 2
    if args.json:
        print(
            json.dumps(
                {
                    "root": report.root,
                    "claims_source": report.claims_source,
                    "results": [
                        {
                            "work": res.work,
                            "item": res.item,
                            "tests": res.tests,
                            "baseline_passed": res.baseline_passed,
                            "outcomes": [vars(out) for out in res.outcomes],
                        }
                        for res in report.results
                    ],
                    "violations": [
                        {"kind": k, "detail": d} for k, d in report.violations
                    ],
                    "notes": [{"kind": k, "detail": d} for k, d in report.notes],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(render(report))
    return 1 if report.violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
