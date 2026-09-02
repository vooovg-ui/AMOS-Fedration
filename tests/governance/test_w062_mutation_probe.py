#!/usr/bin/env python3
"""حرسُ مِسبارِ الطفرةِ — من يحرسُ الحارسَ الذي يُجرِّبُ الحرسَ (W-062).

الهدف:
    أن يسقُطَ فحصٌ إن ضَعُفَ المِسبارُ نفسُه: إن قرأَ نجاةَ طفرةٍ التقاطًا، أو
    قَبِلَ رقمًا غيرَ المُعلَنِ، أو تجاهَلَ دعوى صارَ نصُّها غيرَ موجودٍ، أو شغَّلَ
    على قاعدةٍ ساقطةٍ، أو كتبَ في الشجرةِ التي يحكمُ عليها.
النطاق:
    مستودعاتٌ صناعيّةٌ صغيرةٌ تحتَ `tmp_path` (سريعةٌ) + فحصٌ واحدٌ على الشجرةِ
    الحاضرةِ يتحقَّقُ أنَّ نصوصَ الدعاوى المُسجَّلةِ ما زالَت موجودةً مرّةً واحدةً
    بلا تشغيلِ طفراتٍ. لا شبكةَ ولا سرَّ.
المالك: tests/governance — ديوانُ التدقيق
تاريخ الإنشاء: 2026-08-29
تاريخ آخر تعديل: 2026-08-29
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

ROOT = discover_repo_root(__file__)
TOOL = ROOT / "tools" / "governance" / "mutation_probe.py"
CLAIMS = ROOT / "tools" / "governance" / "mutation_claims.py"


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


probe_mod = _load(TOOL, "mutation_probe_under_test")
claims_mod = _load(CLAIMS, "mutation_claims_under_test")


GUARDED_TOOL = '''\
"""أداةٌ صناعيّةٌ: تُعلِنُ مخالفةً عندَ الصعود."""


def delta(before: int, after: int) -> int:
    return after - before


def verdict(before: int, after: int) -> str:
    if delta(before, after) > 0:
        return "RISING"
    return "FLAT"
'''

GUARD_TEST = '''\
"""حرسٌ صناعيٌّ."""

import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("t", Path(__file__).parents[1] / "tool.py")
mod = importlib.util.module_from_spec(spec)
sys.modules["t"] = mod
spec.loader.exec_module(mod)


def test_rising_detected():
    assert mod.verdict(1, 5) == "RISING"


def test_flat_detected():
    assert mod.verdict(5, 5) == "FLAT"
'''


def _claims_source(mutations: str) -> str:
    return f'''\
"""دعاوى صناعيّةٌ."""

from dataclasses import dataclass, field

MINIMUM_FAILURES = 1


@dataclass(frozen=True)
class Mutation:
    kind: str
    target: str
    old: str
    new: str
    expected_failures: int
    note: str = ""


@dataclass(frozen=True)
class Claim:
    work: str
    item: str
    tests: tuple
    mutations: tuple = field(default_factory=tuple)


CLAIMS = (
    Claim(
        work="W-900",
        item="WI-900",
        tests=("tests/test_tool.py",),
        mutations=({mutations}),
    ),
)


def claims_for(work=None):
    if work is None:
        return CLAIMS
    picked = tuple(c for c in CLAIMS if c.work == work)
    if not picked:
        raise KeyError(work)
    return picked
'''


CATCHING_MUTATION = (
    'Mutation(kind="BREAK_RISE", target="tool.py", '
    'old="if delta(before, after) > 0:", new="if False:", expected_failures=1),'
)


def _repo(tmp_path: Path, mutations: str) -> Path:
    root = tmp_path / "repo"
    (root / "tests").mkdir(parents=True)
    (root / "tools" / "governance").mkdir(parents=True)
    (root / "tool.py").write_text(GUARDED_TOOL, encoding="utf-8")
    (root / "tests" / "test_tool.py").write_text(GUARD_TEST, encoding="utf-8")
    (root / "tools" / "governance" / "mutation_claims.py").write_text(
        _claims_source(mutations), encoding="utf-8"
    )
    for args in (
        ("init", "-q"),
        ("config", "user.email", "probe@test.invalid"),
        ("config", "user.name", "probe"),
        ("add", "-A"),
        ("commit", "-q", "-m", "synthetic"),
    ):
        subprocess.run(
            ["git", *args], cwd=str(root), check=True, capture_output=True, text=True
        )
    return root


def _status(root: Path) -> str:
    return subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=str(root),
        check=True,
        capture_output=True,
        text=True,
    ).stdout


# ----------------------------------------------------------------- قراءةُ الخلاصةِ


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("3 failed, 12 passed in 1.20s", (3, 12)),
        ("15 passed in 12.63s", (0, 15)),
        ("1 error in 0.30s", (1, 0)),
        ("2 failed, 1 error, 4 passed in 2s", (3, 4)),
    ],
)
def test_summary_is_read_not_guessed(line, expected):
    assert probe_mod.count_failures(line) == expected


def test_unreadable_summary_is_refused_not_zero():
    with pytest.raises(probe_mod.ProbeRefused) as raised:
        probe_mod.count_failures("collected nothing at all")
    assert raised.value.kind == "PYTEST_OUTPUT_UNREADABLE"


# ------------------------------------------------------------------ الحالُ السليمُ


def test_caught_mutation_reports_zero_violations(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    report = probe_mod.probe(root)
    assert report.violations == []
    outcome = report.results[0].outcomes[0]
    assert (outcome.verdict, outcome.observed_failures) == (probe_mod.CAUGHT, 1)
    assert report.results[0].baseline_passed == 2
    assert "مُلتقَطةٌ 1" in dict(report.notes)["PROBE_TALLY"]


def test_probe_leaves_the_tree_exactly_as_it_found_it(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    before_status, before_text = _status(root), (root / "tool.py").read_text("utf-8")
    probe_mod.probe(root)
    assert _status(root) == before_status
    assert (root / "tool.py").read_text("utf-8") == before_text


# ------------------------------------------------------- الدعوى الساقطةُ لا تُجمَّلُ


def test_surviving_mutation_is_a_named_violation(tmp_path):
    """طفرةٌ لا يراها أيُّ فحصٍ = `GUARD_SURVIVED_MUTATION` وخروجٌ 1."""
    harmless = (
        'Mutation(kind="COSMETIC", target="tool.py", '
        'old="أداةٌ صناعيّةٌ", new="أداةٌ", expected_failures=1),'
    )
    root = _repo(tmp_path, harmless)
    report = probe_mod.probe(root)
    kinds = [kind for kind, _ in report.violations]
    assert kinds == ["GUARD_SURVIVED_MUTATION"]
    assert report.results[0].outcomes[0].verdict == probe_mod.SURVIVED


def test_wrong_declared_count_is_a_named_violation(tmp_path):
    """رقمٌ مُعلَنٌ لا يطابقُ المقيسَ = `FAILURE_COUNT_MISMATCH`."""
    overstated = CATCHING_MUTATION.replace("expected_failures=1", "expected_failures=2")
    root = _repo(tmp_path, overstated)
    report = probe_mod.probe(root)
    kinds = [kind for kind, _ in report.violations]
    assert kinds == ["FAILURE_COUNT_MISMATCH"]
    outcome = report.results[0].outcomes[0]
    assert (outcome.verdict, outcome.observed_failures) == (probe_mod.MISCOUNTED, 1)


def test_stale_claim_text_is_a_violation_not_a_skip(tmp_path):
    """نصٌّ مُعلَنٌ غيرُ موجودٍ = مخالفةٌ، ولا يُقرأُ صمتُه التقاطًا."""
    stale = (
        'Mutation(kind="GONE", target="tool.py", '
        'old="if delta(before, after) > 9999:", new="if False:", expected_failures=1),'
    )
    root = _repo(tmp_path, stale)
    report = probe_mod.probe(root)
    kinds = [kind for kind, _ in report.violations]
    assert kinds == ["MUTATION_PATTERN_STALE"]
    assert report.results[0].outcomes[0].verdict == probe_mod.STALE


def test_ambiguous_claim_text_is_stale_too(tmp_path):
    """نصٌّ يتكرَّرُ مرّتَينِ لا يُستبدَلُ صامتًا — الاستبدالُ المُبهَمُ مخالفةٌ."""
    ambiguous = (
        'Mutation(kind="AMBIGUOUS", target="tool.py", '
        'old="after", new="0", expected_failures=1),'
    )
    root = _repo(tmp_path, ambiguous)
    report = probe_mod.probe(root)
    assert [kind for kind, _ in report.violations] == ["MUTATION_PATTERN_STALE"]


# --------------------------------------------------------------- الرفضُ المُصنَّفُ


def test_red_baseline_is_refused_not_measured(tmp_path):
    """قاعدةٌ ساقطةٌ قبلَ الطفرةِ: لا يُقاسُ التقاطٌ على أنقاضٍ."""
    root = _repo(tmp_path, CATCHING_MUTATION)
    (root / "tests" / "test_tool.py").write_text(
        GUARD_TEST + "\n\ndef test_broken():\n    assert False\n", encoding="utf-8"
    )
    with pytest.raises(probe_mod.ProbeRefused) as raised:
        probe_mod.probe(root)
    assert raised.value.kind == "BASELINE_NOT_GREEN"


def test_tree_without_history_is_refused(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    subprocess.run(["rm", "-rf", str(root / ".git")], check=True)
    with pytest.raises(probe_mod.ProbeRefused) as raised:
        probe_mod.probe(root)
    assert raised.value.kind == "GIT_UNAVAILABLE"


def test_missing_claims_source_is_refused(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    (root / "tools" / "governance" / "mutation_claims.py").unlink()
    with pytest.raises(probe_mod.ProbeRefused) as raised:
        probe_mod.probe(root)
    assert raised.value.kind == "CLAIMS_SOURCE_MISSING"


def test_broken_claim_contract_is_refused(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    (root / "tools" / "governance" / "mutation_claims.py").write_text(
        '"""بلا عقدٍ."""\n\nNOTHING = 1\n', encoding="utf-8"
    )
    with pytest.raises(probe_mod.ProbeRefused) as raised:
        probe_mod.probe(root)
    assert raised.value.kind == "CLAIM_CONTRACT_BROKEN"


def test_claim_without_mutations_is_refused(tmp_path):
    root = _repo(tmp_path, "")
    with pytest.raises(probe_mod.ProbeRefused) as raised:
        probe_mod.probe(root)
    assert raised.value.kind == "CLAIM_CONTRACT_BROKEN"


def test_unregistered_work_is_refused_not_silently_empty(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    with pytest.raises(probe_mod.ProbeRefused) as raised:
        probe_mod.probe(root, work="W-999")
    assert raised.value.kind == "WORK_NOT_REGISTERED"


# ------------------------------------------------------------------ الواجهةُ والأمرُ


def test_exit_codes_and_json_shape(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    assert probe_mod.main([str(root), "--json"]) == 0
    bad = _repo(
        tmp_path / "b",
        CATCHING_MUTATION.replace("expected_failures=1", "expected_failures=3"),
    )
    assert probe_mod.main([str(bad)]) == 1
    empty = _repo(tmp_path / "c", "")
    assert probe_mod.main([str(empty)]) == 2


def test_listing_does_not_run_anything(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    before = _status(root)
    assert probe_mod.main([str(root), "--list"]) == 0
    assert _status(root) == before


def test_render_shows_every_verdict(tmp_path):
    root = _repo(tmp_path, CATCHING_MUTATION)
    text = probe_mod.render(probe_mod.probe(root))
    assert "BREAK_RISE" in text
    assert probe_mod.CAUGHT in text
    assert "W-900" in text


# --------------------------------------------- الشجرةُ الحاضرةُ: الدعاوى لا تتعفَّنُ


def test_registered_claims_still_describe_the_living_source():
    """كلُّ نصٍّ مُعلَنٍ موجودٌ **مرّةً واحدةً** في هدفِه في الشجرةِ الحاضرةِ.

    فحصٌ رخيصٌ بلا تشغيلِ طفراتٍ: يسقُطُ يومَ يُعادُ صياغةُ أداةٍ فتصيرُ دعوى
    حرسِها غيرَ قابلةٍ للتجريبِ — قبلَ أن يُقرأَ صمتُها اطمئنانًا.
    """
    assert claims_mod.CLAIMS, "لا دعوى مُسجَّلةً"
    for claim in claims_mod.CLAIMS:
        for relative in claim.tests:
            assert (ROOT / relative).is_file(), f"{claim.work}: {relative}"
        for mutation in claim.mutations:
            target = ROOT / mutation.target
            assert target.is_file(), f"{claim.work}: {mutation.target}"
            found = target.read_text(encoding="utf-8").count(mutation.old)
            assert found == 1, f"{claim.work} · {mutation.kind}: وُجِدَ {found} مرّةً"
            assert mutation.expected_failures >= claims_mod.MINIMUM_FAILURES


def test_w061_claim_is_registered_with_its_measured_numbers():
    """الأرقامُ السبعةُ المنشورةُ في `W-061` مُسجَّلةٌ كما نُشِرَت لا أقلَّ."""
    (claim,) = claims_mod.claims_for("W-061")
    assert claim.item == "WI-016"
    declared = {m.kind: m.expected_failures for m in claim.mutations}
    assert declared == {
        "RISE_NEVER_FIRES": 2,
        "BLIND_COUNT": 5,
        "INVERTED_PUBLISHED": 2,
        "LAST_COMMIT_NOT_FIRST": 1,
        "NO_MINIMUM_POINTS": 1,
        "SWALLOW_GIT_FAILURE": 1,
        "WRITES_INTO_TREE": 1,
    }


def test_tree_change_during_run_is_a_named_violation(tmp_path, monkeypatch):
    """لو تغيَّرَت الشجرةُ الحاكمةُ أثناءَ التشغيلِ فالمخالفةُ تُعلَنُ لا تُبتلَعُ."""
    root = _repo(tmp_path, CATCHING_MUTATION)
    seen: list[int] = []

    def drifting_status(path: Path) -> str:
        seen.append(1)
        return "" if len(seen) == 1 else "?? كتابةٌ في الشجرةِ\n"

    monkeypatch.setattr(probe_mod, "git_status", drifting_status)
    report = probe_mod.probe(root)
    assert "PROBE_WROTE_INTO_TREE" in [kind for kind, _ in report.violations]


def test_each_mutation_runs_on_a_restored_tree(tmp_path):
    """طفرةٌ لا تُلوِّثُ التي بعدَها: تُقاسُ الثانيةُ على شجرةٍ مُستعادةٍ."""
    both = CATCHING_MUTATION + (
        'Mutation(kind="SECOND", target="tool.py", '
        'old=\'return "FLAT"\', new=\'return "RISING"\', expected_failures=1),'
    )
    root = _repo(tmp_path, both)
    report = probe_mod.probe(root)
    verdicts = [out.verdict for out in report.results[0].outcomes]
    assert verdicts == [probe_mod.CAUGHT, probe_mod.CAUGHT]
    assert report.violations == []
