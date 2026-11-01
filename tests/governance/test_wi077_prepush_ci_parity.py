#!/usr/bin/env python3
"""
حرسُ تكافؤِ حرسِ ما قبلَ الدفعِ مع CI (DISC-150 · قرارُ المالكِ Q-89 · WI-077)

الهدف: إثباتُ أنَّ `tools/dev/prepush_gate.py` يُشغِّلُ فحصَي مِرساةِ القيودِ المفتوحةِ
       وطزاجةِ مصفوفةِ الحقيقةِ وruff على المستودعِ كلِّه، وأنَّ كلَّ وظيفةٍ في
       `.github/workflows/ci.yml` إمّا مُغطّاةٌ بخطوةٍ محلّيّةٍ مُسمّاةٍ أو مُسمّاةٌ فرقًا
       بسببِها؛ وأنَّ فشلَ خطوةٍ واحدةٍ يمنعُ الدفعَ سلوكًا لا نصًّا؛ وأنَّ سقفَ دَينِ
       التنسيقِ يُسقِطُ الملفَّ الزائدَ ولا يُسقِطُ القائمةَ نفسَها.
النطاق: بنيةُ `_gates` وقاموسا التكافؤ و`_format_debt_verdict` و`main()` بتشغيلٍ مُحاكًى —
        لا شبكةَ ولا أدواتٍ حقيقيّة. والسلوكُ على العقدِ الحقيقيّةِ في مسبارِ
        docs/audit/evidence/W-769/.
المالك: tests/governance — WI-077 (DISC-150 · Q-89 · التوجيهُ 37 § 1)
تاريخ الإنشاء: 2026-11-01 (W-769 · WI-077)
تاريخ آخر تعديل: 2026-11-01 (W-769 · المرّةُ الأولى)
"""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[2]
_GATE_PATH = _REPO_ROOT / "tools" / "dev" / "prepush_gate.py"
_CI_PATH = _REPO_ROOT / ".github" / "workflows" / "ci.yml"

_SPEC = importlib.util.spec_from_file_location("amos_prepush_gate_wi077", _GATE_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"prepush_gate.py not loadable from {_GATE_PATH}")
gate = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(gate)


def _steps(base: str = "origin/main") -> list[tuple[str, list[str], Path | None]]:
    return gate._gates(_REPO_ROOT, "2026-11-05", base)


def _step_number(name: str) -> int:
    return int(name.split("·", 1)[0])


def _ci_jobs() -> set[str]:
    """معرِّفاتُ الوظائفِ في ci.yml: مفاتيحُ المستوى الثاني تحتَ `jobs:` (بلا yaml)."""
    text = _CI_PATH.read_text(encoding="utf-8")
    block = text.split("\njobs:\n", 1)[1]
    return set(re.findall(r"^  ([A-Za-z0-9_-]+):\s*$", block, flags=re.MULTILINE))


# ── التكافؤُ البنيويّ ────────────────────────────────────────────────────────


def test_every_ci_job_is_covered_or_named() -> None:
    covered = set(gate.CI_PARITY_COVERED)
    named = set(gate.CI_PARITY_NAMED_DIFFERENCES)
    assert not covered & named, f"وظيفةٌ مُغطّاةٌ ومُسمّاةٌ فرقًا معًا: {covered & named}"
    unaccounted = _ci_jobs() - covered - named
    assert (
        not unaccounted
    ), f"وظيفةُ CI بلا خطوةٍ محلّيّةٍ ولا فرقٍ مُسمًّى: {sorted(unaccounted)}"
    phantom = (covered | named) - _ci_jobs()
    assert not phantom, f"قاموسُ التكافؤِ يُسمّي وظيفةً ليست في ci.yml: {sorted(phantom)}"


def test_covered_step_numbers_exist() -> None:
    numbers = {_step_number(name) for name, _cmd, _cwd in _steps()}
    for job, steps in gate.CI_PARITY_COVERED.items():
        assert steps, f"{job}: مُغطّاةٌ بلا خطوة"
        missing = set(steps) - numbers
        assert not missing, f"{job}: خطواتٌ غيرُ موجودة {sorted(missing)}"


def test_step_numbers_are_unique_and_contiguous() -> None:
    numbers = [_step_number(name) for name, _cmd, _cwd in _steps()]
    assert numbers == list(range(1, len(numbers) + 1))


def test_original_seven_steps_unchanged() -> None:
    names = [name for name, _cmd, _cwd in _steps()][:7]
    assert [n.split("·", 1)[0] for n in names] == [str(i) for i in range(1, 8)]
    joined = " ".join(" ".join(cmd) for _n, cmd, _c in _steps()[:7])
    for needle in (
        "check_work_governance.py --commit HEAD",
        "--self-check --today 2026-11-05",
        "commit_timestamp_integrity.py --check",
        "check_completion_ledger.py --commit HEAD",
        "--ratchet",
        "state_document_drift.py",
        "test_w154_reviewer_consistency.py",
    ):
        assert needle in joined, f"خطوةٌ من السبعِ الأصليّةِ تغيّرت: {needle}"


# ── الفحوصُ المأمورُ بها نصًّا في Q-89 ───────────────────────────────────────


def _find(predicate) -> list[tuple[str, list[str], Path | None]]:
    return [s for s in _steps() if predicate(s[1])]


def test_open_record_anchor_step_present() -> None:
    hits = _find(
        lambda cmd: any(c.endswith("open_record_accountability.py") for c in cmd)
    )
    assert len(hits) == 1


def test_matrix_freshness_step_after_ratchet() -> None:
    steps = _steps()
    ratchet = next(i for i, (_n, cmd, _c) in enumerate(steps) if "--ratchet" in cmd)
    fresh = [
        i
        for i, (_n, cmd, _c) in enumerate(steps)
        if cmd[:3] == ["git", "diff", "--exit-code"]
        and "docs/audit/TRUTH_MATRIX.md" in cmd
        and "docs/audit/truth_matrix.json" in cmd
    ]
    assert len(fresh) == 1
    assert fresh[0] > ratchet, "فحصُ الطزاجةِ يجبُ أن يأتيَ بعدَ توليدِ المصفوفة"


def test_ruff_whole_repo_steps_present() -> None:
    root_check = _find(lambda cmd: cmd[-3:] == ["ruff", "check", "."])
    assert root_check and root_check[0][2] == _REPO_ROOT
    debt = _find(lambda cmd: cmd[-4:-2] == ["--internal", "format-debt"])
    assert len(debt) == 1


def test_range_steps_use_base() -> None:
    joined = [" ".join(cmd) for _n, cmd, _c in _steps("abc123")]
    assert any("check_work_governance.py --range abc123..HEAD" in j for j in joined)
    assert any("check_completion_ledger.py --range abc123..HEAD" in j for j in joined)
    assert any("pre_push_merge_guard.py --base-ref abc123" in j for j in joined)


# ── الرفضُ سلوكًا: فشلُ خطوةٍ واحدةٍ يمنعُ الدفع ─────────────────────────────


def _run_main(monkeypatch, failing: str) -> int:
    def fake_run(cmd, cwd=None, capture_output=True, text=True, check=False):
        code = 1 if any(failing in c for c in cmd) else 0
        return subprocess.CompletedProcess(cmd, code, stdout="", stderr="")

    monkeypatch.setattr(gate.subprocess, "run", fake_run)
    monkeypatch.setattr(sys, "argv", ["prepush_gate.py"])
    return gate.main()


def test_anchor_failure_alone_blocks_push(monkeypatch, capsys) -> None:
    assert _run_main(monkeypatch, "open_record_accountability.py") == 1
    assert "ممنوعٌ الدفعُ" in capsys.readouterr().out


def test_freshness_failure_alone_blocks_push(monkeypatch, capsys) -> None:
    assert _run_main(monkeypatch, "docs/audit/truth_matrix.json") == 1
    assert "ممنوعٌ الدفعُ" in capsys.readouterr().out


def test_all_green_allows_push_and_names_differences(monkeypatch, capsys) -> None:
    assert _run_main(monkeypatch, "__nothing_fails__") == 0
    out = capsys.readouterr().out
    assert "جائزٌ الدفعُ" in out
    for reason in gate.CI_PARITY_NAMED_DIFFERENCES.values():
        assert reason in out


# ── سقفُ دَينِ التنسيق ───────────────────────────────────────────────────────


def test_format_debt_extra_file_fails() -> None:
    code, extra = gate._format_debt_verdict({"a.py", "new.py"}, {"a.py", "b.py"})
    assert code == 1 and extra == ["new.py"]


@pytest.mark.parametrize("unformatted", [set(), {"a.py"}, {"a.py", "b.py"}])
def test_format_debt_subset_passes(unformatted: set[str]) -> None:
    assert gate._format_debt_verdict(unformatted, {"a.py", "b.py"}) == (0, [])


def test_would_reformat_parser() -> None:
    out = "Would reformat: x/a.py\nWould reformat: b.py\n2 files would be reformatted\n"
    assert gate._would_reformat(out) == {"x/a.py", "b.py"}


def test_debt_list_is_the_measured_212() -> None:
    debt = gate._read_debt(gate.FORMAT_DEBT_PATH)
    assert 0 < len(debt) <= 212, "القائمةُ تنقصُ بالتسديدِ ولا تزيدُ إلّا بقرارِ المالك"
    assert all((_REPO_ROOT / name).suffix == ".py" for name in debt)


def test_lockfile_internal_check_names_all_six(capsys) -> None:
    assert gate._internal("lockfile", _REPO_ROOT) == 0
    out = capsys.readouterr().out
    for package in (
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "anthropic",
        "structlog",
        "pydantic",
    ):
        assert package in out


def test_unknown_internal_check_fails() -> None:
    assert gate._internal("no-such-check", _REPO_ROOT) == 2
