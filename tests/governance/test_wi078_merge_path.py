#!/usr/bin/env python3
"""
حرسُ وجهِ الدمجِ `--merge <sha>` — المسلكُ الوحيدُ الموثَّقُ إلى main (WI-078)

الهدف: منعُ حذفِ أداةِ الدمجِ الآمنةِ أو تعطيلِها بصمتٍ: يُثبِتُ أنَّ
       `prepush_gate.py` يُسجِّلُ وجهَ `--merge` ويستدعي أداةَ الحكمِ القائمةَ
       كما هي ويقدِّمُ التقديمَ السريعَ وحدَهُ، وأنَّ خُطّافَ `pre-push` مصدرُهُ
       متتبَّعٌ وأنَّ `bootstrap.sh` يُثبِّتُهُ وأنَّ دليلَ المشروعِ يوثِّقُ المسلكَ —
       ويُقتَلُ بالتحويرِ: كلُّ عطبٍ مصنوعٍ يُسقِطُ الفحصَ المعنيَّ وحدَه.
النطاق: ملفّاتُ الأداةِ وأدلّتُها المكتوبةُ وحدَها — لا شبكةَ ولا `gh` ولا دفعًا
        حقيقيًّا في الفحوصِ: منطقُ الرفضِ يُقاسُ على حِمولاتٍ مصنوعةٍ وأشجارٍ
        مؤقّتةٍ، والدفعُ الحيُّ دليلُ قيدِ العملِ لا الفحصِ.
المالك: tests/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-10-16 (W-360 · WI-078 · توجيهُ المستشارِ 6 · H2)
تاريخ آخر تعديل: 2026-10-16 (W-360 · المرّةُ الأولى)
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[2]
_GATE_PATH = _REPO_ROOT / "tools" / "dev" / "prepush_gate.py"
_HOOK_PATH = _REPO_ROOT / "tools" / "dev" / "hooks" / "pre-push"
_BOOTSTRAP_PATH = _REPO_ROOT / "tools" / "dev" / "bootstrap.sh"
_HANDBOOK_PATH = _REPO_ROOT / "docs" / "PROJECT_HANDBOOK.md"
_VERDICT_TOOL = _REPO_ROOT / "tools" / "governance" / "ci_verdict_readability.py"

_GATE_SPEC = importlib.util.spec_from_file_location("amos_prepush_gate_wi078", _GATE_PATH)
if _GATE_SPEC is None or _GATE_SPEC.loader is None:
    raise ImportError(f"prepush_gate.py not loadable from {_GATE_PATH}")
gate = importlib.util.module_from_spec(_GATE_SPEC)
_GATE_SPEC.loader.exec_module(gate)

_FAKE_SHA = "a" * 40
_OTHER_SHA = "b" * 40


def _green_payload(sha: str) -> dict:
    """حِملُ تشغيلٍ أخضرَ مقروءٍ على العقدةِ نفسِها — بالحقولِ التي تقرأها الأداةُ."""
    return {
        "jobs": [
            {
                "name": "Tests",
                "id": 1,
                "run_id": 9001,
                "conclusion": "success",
                "status": "completed",
                "runner_id": 7,
                "head_sha": sha,
                "steps": [{"name": "run", "started_at": "2026-10-16T00:00:00Z"}],
            }
        ]
    }


def _red_payload(sha: str) -> dict:
    """حِملُ تشغيلٍ أحمرَ — خُضرةُ الصورةِ لا تنفعُ معَ فشلٍ مقيسٍ في وظيفةٍ."""
    payload = _green_payload(sha)
    payload["jobs"][0]["conclusion"] = "failure"
    return payload


def _write_payload(tmp_path: Path, name: str, payload: dict) -> Path:
    path = tmp_path / name
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    return path


# ── 1· الوجودُ والتوثيقُ: الأداةُ والخُطّافُ والتثبيتُ والدليلُ ───────────────


def _gate_source_has_merge_face(source: str) -> bool:
    markers = (
        '"--merge"',
        '"--require-readable"',
        '"--expect-sha"',
        "f\"{sha}:main\"",
        '"TZ": "UTC"',
    )
    return all(marker in source for marker in markers)


def test_gate_registers_merge_face() -> None:
    source = _GATE_PATH.read_text(encoding="utf-8")
    assert _gate_source_has_merge_face(source), (
        "وجهُ --merge غائبٌ من prepush_gate.py — المسلكُ الموثَّقُ الوحيدُ "
        "إلى main لا يُحذفُ بصمتًا (WI-078)."
    )


def test_hook_source_is_tracked_and_runs_the_gate() -> None:
    assert _HOOK_PATH.is_file(), "خُطّافُ pre-push المصدرُ غيرُ موجودٍ (WI-078)."
    mode = _HOOK_PATH.stat().st_mode
    assert mode & 0o111, "خُطّافُ pre-push ليسَ تنفيذيًّا — لا يُشغِّلُهُ git."
    source = _HOOK_PATH.read_text(encoding="utf-8")
    assert "prepush_gate.py" in source, "الخُطّافُ لا يُشغِّلُ حرسَ ما قبلَ الدفعِ."
    assert "show-toplevel" in source, "الخُطّافُ لا يعرفُ جذرَ الشجرةِ."


def test_bootstrap_installs_the_hook() -> None:
    source = _BOOTSTRAP_PATH.read_text(encoding="utf-8")
    assert "tools/dev/hooks/pre-push" in source, (
        "bootstrap.sh لا يُثبِّتُ الخُطّافَ من مصدرِهِ المتتبَّعِ (WI-078)."
    )
    assert ".git/hooks/pre-push" in source, (
        "bootstrap.sh لا يُثبِّتُ الخُطّافَ في موضعهِ الذي يقرؤهُ git."
    )


def test_handbook_documents_merge_as_only_path() -> None:
    source = _HANDBOOK_PATH.read_text(encoding="utf-8")
    assert "--merge <sha>" in source, (
        "دليلُ المشروعِ لا يوثِّقُ وجهَ الدمجِ --merge (WI-078)."
    )
    assert "tools/dev/hooks/pre-push" in source, (
        "دليلُ المشروعِ لا يعلنُ أنَّ bootstrap.sh يُثبِّتُ الخُطّافَ (الخطوةَ 1)."
    )


# ── 2· المنطقُ: الاستخراجُ والانتقاءُ والحكمُ على حِمولاتٍ مصنوعةٍ ────────────


def test_slug_from_url_https_and_ssh() -> None:
    assert gate._slug_from_url("https://github.com/owner/name.git") == "owner/name"
    assert gate._slug_from_url("https://github.com/owner/name") == "owner/name"
    assert gate._slug_from_url("git@github.com:owner/name.git") == "owner/name"
    assert gate._slug_from_url("https://github.com/o/n/") == "o/n"


def test_slug_from_url_rejects_the_unknown() -> None:
    for bad in ("", "https://gitlab.com/o/n", "https://github.com/o", "x"):
        with pytest.raises(ValueError, match="يُرفَضُ"):
            gate._slug_from_url(bad)


def test_select_completed_runs_filters_by_sha_and_completion() -> None:
    runs = [
        {
            "databaseId": 1,
            "headSha": _FAKE_SHA,
            "status": "completed",
            "workflowName": gate.CI_WORKFLOW_NAME,
        },
        {
            "databaseId": 2,
            "headSha": _FAKE_SHA,
            "status": "in_progress",
            "workflowName": gate.CI_WORKFLOW_NAME,
        },
        {
            "databaseId": 3,
            "headSha": _OTHER_SHA,
            "status": "completed",
            "workflowName": gate.CI_WORKFLOW_NAME,
        },
        "ليس قاموسًا",
    ]
    selected = gate._select_completed_runs(runs, _FAKE_SHA)
    assert [r["databaseId"] for r in selected] == [1]


def test_matrix_run_alone_is_not_a_ci_verdict() -> None:
    """مصفوفةُ الحقيقةِ خضراءُ مكتملةٌ وتشغيلُ CI جارٍ ⇒ لا حكمَ فلا دمجَ.

    عيبٌ رصدهُ مراجعُ التسليمِ (W-362): انتقاءُ «كلِّ تشغيلٍ مكتملٍ» كانَ
    يقبلُ تشغيلَ المصفوفةِ وحدَهُ حكمًا أخضرَ فيُقدِّمُ الوجهُ العقدةَ بلا
    انتظارِ حكمِ CI — وهوَ عينُ ما وُضعَ الوجهُ لأجلِ منعِهِ.
    """
    runs = [
        {
            "databaseId": 11,
            "headSha": _FAKE_SHA,
            "status": "completed",
            "conclusion": "success",
            "workflowName": "مصفوفةُ الحقيقةِ المولَّدة",
        },
        {
            "databaseId": 12,
            "headSha": _FAKE_SHA,
            "status": "in_progress",
            "conclusion": None,
            "workflowName": gate.CI_WORKFLOW_NAME,
        },
    ]
    selected = gate._select_completed_runs(runs, _FAKE_SHA)
    assert selected == [], "تشغيلُ المصفوفةِ وحدَهُ ليسَ حكمَ CI — لا يُنتقى أصلًا"


def test_verdict_green_on_crafted_payload(tmp_path: Path) -> None:
    payload = _write_payload(tmp_path, "green.json", _green_payload(_FAKE_SHA))
    exit_code, text = gate._read_verdict(
        _REPO_ROOT, "owner/name", _FAKE_SHA, [payload]
    )
    assert exit_code == 0, f"حِملٌ أخضرُ مقروءٌ رُفضَ: {text}"


def test_verdict_red_refused(tmp_path: Path) -> None:
    payload = _write_payload(tmp_path, "red.json", _red_payload(_FAKE_SHA))
    exit_code, _ = gate._read_verdict(_REPO_ROOT, "owner/name", _FAKE_SHA, [payload])
    assert exit_code != 0, "حِملٌ أحمرُ لا يُرفَضُ — لا دمجَ على أحمرَ (WI-078)."


def test_verdict_wrong_node_refused(tmp_path: Path) -> None:
    payload = _write_payload(tmp_path, "other.json", _green_payload(_OTHER_SHA))
    exit_code, _ = gate._read_verdict(_REPO_ROOT, "owner/name", _FAKE_SHA, [payload])
    assert exit_code != 0, "حِملٌ من عقدةٍ أخرى لا يُرفَضُ — تُقاسُ العقدةُ نفسُها."


def test_verdict_unreadable_refused(tmp_path: Path) -> None:
    payload = _green_payload(_FAKE_SHA)
    payload["jobs"][0]["steps"] = []  # لا خطوةَ نُفِّذَت ⇒ غيرُ مقروءٍ
    path = _write_payload(tmp_path, "unreadable.json", payload)
    exit_code, _ = gate._read_verdict(_REPO_ROOT, "owner/name", _FAKE_SHA, [path])
    assert exit_code != 0, "«غيرُ مقروءٍ» ليسَ أخضرَ ولا أحمرَ — لا يُمرَّرُ."


def test_merge_refuses_when_head_is_not_the_node(tmp_path: Path) -> None:
    """الرفضُ قبلَ أيِّ شبكةٍ: الشجرةُ المقيسةُ هيَ العقدةُ المدموجةُ أو لا دمجَ."""
    repo = tmp_path / "forged"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", "-b", "main", "."], cwd=repo, check=True)
    subprocess.run(
        ["git", "config", "user.email", "wi078@amos.local"], cwd=repo, check=True
    )
    subprocess.run(
        ["git", "config", "user.name", "WI-078 Guard"], cwd=repo, check=True
    )
    (repo / "README.md").write_text("x", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(
        ["git", "commit", "-q", "-m", "init", "--date=2026-10-16T00:00:00+00:00"],
        cwd=repo,
        check=True,
        env={**__import__("os").environ, "TZ": "UTC"},
    )
    exit_code = gate._merge_flow("f" * 40, repo, [])
    assert exit_code != 0, "عقدةٌ لا تطابقُ HEAD مُرَّتْ — الحرسُ يقيسُ الشجرةَ الحاضرةَ."


# ── 3· قتلُ الفحصِ بالتحويرِ: كلُّ عطبٍ مصنوعٍ يُسقِطُ الفحصَ المعنيَّ ──────────


def test_gate_marker_check_catches_removal() -> None:
    source = _GATE_PATH.read_text(encoding="utf-8")
    mutated = source.replace('"--merge"', '"--murged"')
    assert mutated != source, "التحويرُ لم يُنفَّذْ."
    assert not _gate_source_has_merge_face(mutated), (
        "حذفُ وجهِ --merge لا يُكتشَفُ — الفحصُ يحرسُ لا يُزيِّنُ."
    )


def test_hook_marker_check_catches_emptying() -> None:
    assert not _hook_markers_present("#!/bin/sh\necho x\n"), (
        "تخوينُ الخُطّافِ لا يُكتشَفُ."
    )


def _hook_markers_present(source: str) -> bool:
    return "prepush_gate.py" in source and "show-toplevel" in source


def test_bootstrap_marker_check_catches_removal() -> None:
    source = _BOOTSTRAP_PATH.read_text(encoding="utf-8")
    mutated = source.replace("tools/dev/hooks/pre-push", "tools/dev/hooks/absent")
    assert mutated != source, "التحويرُ لم يُنفَّذْ."
    assert "tools/dev/hooks/pre-push" not in mutated
    assert "tools/dev/hooks/pre-push" in source


def test_verdict_tool_is_untouched_companion() -> None:
    """الأداةُ تُستدعى كما هي — حرسُ الجوارِ يحرسُ بقاءَها (لا إعادةَ كتابةٍ)."""
    source = _VERDICT_TOOL.read_text(encoding="utf-8")
    assert "--require-readable" in source and "--expect-sha" in source
    assert "--from-json" in source
