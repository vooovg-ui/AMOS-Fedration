"""حرسُ W-051 — لا يُقرأُ حكمُ CI إلّا إذا نُفِّذَت خطوةٌ فعلًا.

الهدف:
    منعُ أربعِ صورٍ من الكذبِ الموثَّقِ التي فتحَها `DISC-006` وقيَّدَها `RK-011`:
      1. أن يُقرأَ `conclusion` حكمًا على الشجرةِ في تشغيلٍ **لم يُسنَدْ له عاملٌ**
         (`steps=[]` · `runner_id=0`) — فيُقالَ «CI أحمرُ» عن شجرةٍ لم تُفحَصْ.
      2. أن يُقالَ «أخضرُ» لأنَّ لا خطوةَ سقطَت، والخطواتُ كلُّها لم تُشغَّلْ.
      3. أن تُخفَّفَ الأداةُ فتُعِدَّ الوظيفةَ المُتخطّاةَ (`skipped`) عطبًا، أو
         تُعِدَّها تنفيذًا — فالغيابُ فيها مشروعٌ وتُخرَجُ من المقامِ لا من الجرد.
      4. أن تُبتلَعَ الأخطاءُ: حِملٌ ناقصٌ أو ملفٌّ غائبٌ أو توكنٌ مفقودٌ يُرجِعُ
         حكمًا مُخترَعًا بدلَ أن يُعلِنَ عجزَه ويسقُط (القاعدة 12).

النطاق:
    `tools/governance/ci_verdict_readability.py` وحدَه. ولا يقيسُ هذا الحرسُ
    صحّةَ CI ولا يطلبُ شبكةً: كلُّ فحصٍ هنا يعملُ على حِملٍ مُصطنَعٍ أو محفوظٍ.
    وحالةُ حسابِ `Actions` **ليست** موضوعَ هذا الحرس — تلك بيدِ المالكِ بنصِّ
    `DISC-006`، وحارسٌ يشترطُ ما لا يملكُه حارسٌ يسقُطُ بلا عطبٍ في الشِفرة.

المالك:
    `tests/governance` — حرّاسُ الحوكمةِ في المستودع.

تاريخ الإنشاء: 2026-08-27
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "ci_verdict_readability.py"


def _load_tool():
    """تحميلُ الأداةِ من مسارِها — لا حزمةَ لها، فلا يُفترَضُ استيرادٌ."""
    spec = importlib.util.spec_from_file_location("ci_verdict_readability", TOOL_PATH)
    assert spec is not None and spec.loader is not None, f"لا يُحمَّلُ {TOOL_PATH}"
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


tool = _load_tool()


def _job(
    name: str,
    *,
    steps: list[dict[str, object]] | None = None,
    runner_id: int | None = 0,
    conclusion: str | None = "failure",
) -> dict[str, object]:
    return {
        "id": abs(hash(name)) % 1_000_000,
        "name": name,
        "conclusion": conclusion,
        "status": "completed",
        "runner_id": runner_id,
        "run_id": 1,
        "steps": [] if steps is None else steps,
    }


def _step(started: bool) -> dict[str, object]:
    return {
        "name": "Run",
        "conclusion": "success" if started else None,
        "started_at": "2026-08-25T21:58:11Z" if started else None,
    }


# ── 1 · تصنيفُ الوظيفةِ الواحدة ──────────────────────────────────────────────


def test_job_without_steps_and_without_runner_is_not_dispatched() -> None:
    """`steps=[]` و`runner_id=0` = لم يُسنَدْ عاملٌ — لا «فشلٌ»."""
    reading = tool.classify_job(_job("lint"))
    assert reading.classification == tool.JOB_NOT_DISPATCHED
    assert reading.steps_total == 0
    assert reading.steps_started == 0


def test_job_with_started_step_is_executed() -> None:
    reading = tool.classify_job(_job("lint", steps=[_step(True)], runner_id=41))
    assert reading.classification == tool.JOB_EXECUTED
    assert reading.steps_started == 1


def test_skipped_job_is_neither_executed_nor_broken() -> None:
    """الوظيفةُ المُتخطّاةُ لا خطواتَ لها مشروعًا — لا تُعَدُّ عطبًا ولا تنفيذًا."""
    reading = tool.classify_job(_job("optional", conclusion="skipped"))
    assert reading.classification == tool.JOB_SKIPPED


def test_job_with_runner_but_no_steps_is_ambiguous_not_guessed() -> None:
    """عاملٌ مُسنَدٌ بلا خطواتٍ حالةٌ لا يُخمَّنُ فيها — تُعلَنُ `AMBIGUOUS`."""
    reading = tool.classify_job(_job("lint", runner_id=77))
    assert reading.classification == tool.JOB_AMBIGUOUS


def test_step_present_but_never_started_is_not_execution() -> None:
    """خطوةٌ مُعلَنةٌ بلا `started_at` ليست تنفيذًا — وهذا لبُّ العطب."""
    reading = tool.classify_job(_job("lint", steps=[_step(False)], runner_id=0))
    assert reading.classification == tool.JOB_AMBIGUOUS
    assert reading.steps_total == 1
    assert reading.steps_started == 0


# ── 2 · حكمُ التشغيل ────────────────────────────────────────────────────────


def test_run_with_no_executed_job_is_unreadable_and_conclusion_not_quotable() -> None:
    payload = {"jobs": [_job("a"), _job("b"), _job("c")]}
    run = tool.read_run("1", payload)
    assert run.verdict == tool.RUN_UNREADABLE
    assert run.conclusion_quotable is False
    assert run.jobs_not_dispatched == 3


def test_run_with_all_jobs_executed_is_readable() -> None:
    payload = {
        "jobs": [
            _job("a", steps=[_step(True)], runner_id=1),
            _job("b", steps=[_step(True)], runner_id=2, conclusion="success"),
        ]
    }
    run = tool.read_run("1", payload)
    assert run.verdict == tool.RUN_READABLE
    assert run.conclusion_quotable is True


def test_partially_executed_run_is_not_quotable_as_a_verdict() -> None:
    """اثنتا عشرةَ من ثلاثةَ عشرَ ليست حكمًا: نتيجةُ التشغيلِ مجموعُ وظائفِه."""
    payload = {"jobs": [_job("a", steps=[_step(True)], runner_id=1), _job("b")]}
    run = tool.read_run("1", payload)
    assert run.verdict == tool.RUN_PARTIAL
    assert run.conclusion_quotable is False


def test_skipped_jobs_leave_the_denominator_but_stay_in_the_inventory() -> None:
    payload = {
        "jobs": [
            _job("a", steps=[_step(True)], runner_id=1),
            _job("skipped-one", conclusion="skipped"),
        ]
    }
    run = tool.read_run("1", payload)
    assert run.jobs_total == 2
    assert run.jobs_considered == 1
    assert run.jobs_skipped == 1
    assert run.verdict == tool.RUN_READABLE


def test_run_of_only_skipped_jobs_is_undetermined_not_readable() -> None:
    payload = {"jobs": [_job("a", conclusion="skipped")]}
    run = tool.read_run("1", payload)
    assert run.verdict == tool.RUN_UNDETERMINED
    assert run.conclusion_quotable is False


# ── 3 · الرفضُ لا الابتلاع ───────────────────────────────────────────────────


def test_payload_without_jobs_list_is_refused_not_guessed() -> None:
    with pytest.raises(tool.MeasurementRefused):
        tool.read_run("1", {"total_count": 0})


def test_non_object_job_entry_is_refused() -> None:
    with pytest.raises(tool.MeasurementRefused):
        tool.read_run("1", {"jobs": [_job("a"), "not-a-job"]})


def test_steps_of_wrong_type_is_refused() -> None:
    with pytest.raises(tool.MeasurementRefused):
        tool.classify_job({"name": "a", "steps": "13"})


def test_missing_payload_file_is_refused(tmp_path: Path) -> None:
    with pytest.raises(tool.MeasurementRefused):
        tool._load_payload(tmp_path / "absent.json")


def test_missing_token_is_refused_and_never_falls_back(monkeypatch) -> None:
    """بلا توكنٍ **يسقُطُ** القياسُ ولا يُرجَعُ حكمٌ — ولا يُطبَعُ سرٌّ."""
    for name in tool.TOKEN_ENV_VARS:
        monkeypatch.delenv(name, raising=False)
    with pytest.raises(tool.MeasurementRefused) as excinfo:
        tool._token()
    assert "--from-json" in str(excinfo.value)


def test_token_is_read_from_environment_only(monkeypatch) -> None:
    monkeypatch.setenv(tool.TOKEN_ENV_VARS[0], "قيمةٌ-للاختبارِ-لا-سرَّ")
    assert tool._token() == "قيمةٌ-للاختبارِ-لا-سرَّ"


def test_no_secret_name_is_hardcoded_as_a_value() -> None:
    """لا سرَّ في الشِفرةِ: تُقرأُ أسماءُ متغيّراتِ بيئةٍ لا قيمُها (الحظر 4)."""
    source = TOOL_PATH.read_text(encoding="utf-8")
    assert "ghp_" not in source
    assert "github_pat_" not in source


# ── 4 · رمزُ الخروجِ والحِملُ المنشور ────────────────────────────────────────


def test_exit_code_is_one_when_a_run_is_unreadable(tmp_path: Path) -> None:
    payload = tmp_path / "1.json"
    payload.write_text(json.dumps({"jobs": [_job("a")]}), encoding="utf-8")
    assert tool.main(["--from-json", str(payload)]) == 1


def test_exit_code_is_zero_when_every_run_is_readable(tmp_path: Path) -> None:
    payload = tmp_path / "2.json"
    payload.write_text(
        json.dumps({"jobs": [_job("a", steps=[_step(True)], runner_id=9)]}),
        encoding="utf-8",
    )
    assert tool.main(["--from-json", str(payload)]) == 0


def test_refusal_exits_with_two_not_with_a_verdict(tmp_path: Path) -> None:
    """العجزُ رمزُه غيرُ رمزِ الحكمِ — فلا يُخلَطُ «لم أقِسْ» بـ«قِستُ فسقطَ»."""
    bad = tmp_path / "3.json"
    bad.write_text(json.dumps({"total_count": 0}), encoding="utf-8")
    assert tool.main(["--from-json", str(bad)]) == 2


def test_written_measurement_carries_the_numbers_that_produced_the_verdict(
    tmp_path: Path,
) -> None:
    payload = tmp_path / "4.json"
    payload.write_text(json.dumps({"jobs": [_job("a"), _job("b")]}), encoding="utf-8")
    out = tmp_path / "measure.json"
    assert tool.main(["--from-json", str(payload), "--json", str(out)]) == 1
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["schema_version"] == tool.SCHEMA_VERSION
    assert data["runs_total"] == 1
    assert data["runs_unreadable"] == 1
    assert data["runs"][0]["jobs_not_dispatched"] == 2


def test_live_mode_requires_a_repository(capsys) -> None:
    with pytest.raises(SystemExit):
        tool.main(["--run", "123"])
    assert "--repo" in capsys.readouterr().err


def test_no_input_at_all_is_refused(capsys) -> None:
    with pytest.raises(SystemExit):
        tool.main([])
    assert "--from-json" in capsys.readouterr().err


# ── 5 · الأداةُ تُعيدُ رقمَ DISC-006 المُقيَّدَ حرفًا ─────────────────────────


def test_tool_reproduces_the_recorded_disc006_reading() -> None:
    """`DISC-006` قيَّدَ `with_steps=12` من 13 للتشغيلِ 32903824510.

    الحِملُ المحفوظُ لذاكَ التشغيلِ **ليس** في الشجرةِ (‏وثيقةُ وقائعَ خارجيّةٌ
    لا مِلكَ للمستودعِ)، فيُصطنَعُ هنا الشكلُ نفسُه: اثنتا عشرةَ وظيفةً نُفِّذَت
    وواحدةٌ لم يُسنَدْ لها عاملٌ. والمقصودُ إثباتُ أنَّ **معيارَ الأداةِ** هو
    المعيارُ الذي قِيسَ به يدًا في `W-049`، لا إثباتُ رقمِ تشغيلٍ بعينِه.
    """
    jobs = [_job(f"j{i}", steps=[_step(True)], runner_id=i + 1) for i in range(12)]
    jobs.append(_job("j12"))
    run = tool.read_run("32903824510", {"jobs": jobs})
    assert run.jobs_executed == 12
    assert run.jobs_considered == 13
    assert run.verdict == tool.RUN_PARTIAL
    assert run.conclusion_quotable is False
