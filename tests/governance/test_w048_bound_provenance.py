"""
AMOS-Federation — حرسُ الرباطِ المقيسِ في عقدِ نَسَبِ القياساتِ (W-048)
الهدف: أن لا يُعتذَرَ عن قياسٍ منشورٍ بحرسٍ «قائمٍ في وظيفةٍ أخرى» إلّا وذاكَ
       الحرسُ **مقيسٌ نصًّا**: موجودٌ في ملفِّ الوقائعِ، وغيرُ منزوعِ الأثرِ،
       ومُشغَّلٌ حينَ يتغيَّرُ ما يقيسُه.
النطاق: tests/governance
المالك: الجذر (حكمُ المستودعِ)
تاريخ الإنشاء: 2026-08-26 (W-048)
تاريخ آخر تعديل: 2026-08-26 (W-048)

## لماذا وُجِدَ هذا الملفُّ

كانَ `restart_survival.json` مُعلَنًا بلا حرسٍ في عقدِ W-037، وسببُه المكتوبُ:
«وله فحصُه الخاصُّ `--check` يُشغَّلُ في وظيفةٍ أخرى؛ فلا يُكرَّرُ هنا». فقِيسَ
السببُ فبانَ ثلاثةُ عيوبٍ مُتراكِبةٍ:

1. الفحصُ المزعومُ كانَ في `measure.yml` منزوعَ الأثرِ بـ`|| true` واسمُ خطوتِه
   «عرضُ القياسِ في السجلّ» — فلا يُسقِطُ وظيفةً أبدًا. فكانَ الاعتذارُ بحرسٍ
   لا يحرسُ.
2. ولم يكن في الشجرةِ شيءٌ يقيسُ تلكَ الدعوى عن CI — فلو حُذِفَتِ الخطوةُ كلُّها
   لبقيَ السببُ المكتوبُ مُطمئنًّا كما هو.
3. والمِسبارُ في وضعِ `--check` كانَ يكتبُ الملفَ الذي يحكمُ عليه — وهي العلّةُ
   نفسُها التي أُصلِحتْ لمِسبارَيِ القضاءِ والخزانةِ في W-038.

فأُضيفَ وضعٌ رابعٌ `bound`: لا إعادةَ قياسٍ في البوّابةِ (‏فثمنُه دقائقُ وبيئةُ
خدمةٍ كاملةٌ)، **بل رباطٌ يُقاسُ نصًّا** على سابقةِ حارسِ `ci.yml` في W-038.

## وما يحرسُه هذا الملفُّ من الحرسِ نفسِه

وضعٌ جديدٌ في عقدٍ قد يصيرُ إعفاءً متنكِّرًا في صورةِ حرسٍ: يُعلَنُ الرباطُ ثمَّ
لا يُقاسُ، أو يُقاسُ الوجودُ ولا يُقاسُ نزعُ الأثرِ، أو يُقاسُ الأمرُ ولا يُقاسُ
أنَّ الوظيفةَ تُشغَّلُ أصلًا حينَ يتغيَّرُ المُولِّدُ. فهذه الفحوصُ تصنعُ كلَّ
واحدةٍ من تلكَ الحالاتِ قصدًا وتنتظرُ الحُمرةَ.

## وما لا يفعلُه

لا يزعمُ أنَّ `bound` يحرسُ **طزاجةَ** الملفِّ المنشورِ: هو يحرسُ **القدرةَ**
(‏أنَّ الأسطحَ تتصرّفُ كما صُرِّحَ بها). والطزاجةُ محروسةٌ بمُشغِّلاتِ
`measure.yml` التي تُعيدُ التوليدَ وتدفعُ، و**مضمونُ** المنشورِ محروسٌ في كلِّ
دفعةٍ بـ`test_step18_restart_survival.py`. وهذا الحدُّ مُعلَنٌ في `reason` لا
مطويٌّ.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[2]
TOOL = REPO / "tools" / "governance" / "measurement_provenance.py"
MEASURE_WORKFLOW = REPO / ".github" / "workflows" / "measure.yml"
PROBE = REPO / "tools" / "governance" / "restart_survival_probe.py"


def _load(path: Path, name: str) -> Any:
    """حمِّلِ الأداةَ وحدَها بلا حزمةٍ — كما تُشغَّلُ في البوّابةِ نفسِها."""
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(name, None)
        raise
    return module


@pytest.fixture(scope="module")
def tool() -> Any:
    return _load(TOOL, "measurement_provenance_bound_under_test")


# ---------------------------------------------------------------------------
# 1) العقدُ على المستودعِ كما هو مدفوعٌ — الرقمُ يُقالُ لا يُنطبَعُ
# ---------------------------------------------------------------------------


def test_the_bound_strategy_is_a_known_strategy(tool: Any) -> None:
    """`bound` وضعٌ مُقيَّدٌ في العقدِ لا سلسلةٌ حرّةٌ تُكتَبُ كيفَ شِيءَ."""
    assert "bound" in tool.STRATEGIES
    assert "bound" not in tool.PROBING, (
        "`bound` لا يُشغِّلُ أمرَ قياسٍ في هذه البوّابةِ — وإلّا فقد ضاعَ سببُ وجودِه."
    )


def test_restart_survival_is_bound_not_declared(tool: Any) -> None:
    """القيدُ الذي كانَ مُعلَنًا بلا حرسٍ صارَ مربوطًا برباطٍ يُقاسُ."""
    entry = next(e for e in tool.REGISTRY if e.name == "restart_survival.json")
    assert entry.strategy == "bound", entry.strategy
    assert entry.bound_workflow == ".github/workflows/measure.yml"
    assert entry.bound_commands, "رباطٌ بلا أمرٍ مربوطٍ ليسَ رباطًا."
    assert entry.reason.strip(), "الرباطُ يُعلَنُ حدُّه لا يُقالُ دونَه."


def test_guarded_count_is_a_ratchet_not_a_transcript(tool: Any) -> None:
    """الحرسُ لا يتراجعُ، والمُعلَنُ بلا حرسٍ لا يتكاثرُ.

    كانَ هذا الفحصُ يُثبِّتُ «10 مقيَّدًا · 8 محروسًا · 2 مُعلَنًا» بالمساواةِ،
    فكانَ يسقُطُ على **إضافةِ قياسٍ مشروعٍ** لا على تخفيفِ حرسٍ — وذاك عيبٌ
    في الفحصِ لا في العمل. فصارَ **ترباسًا**: العددُ الكلِّيُّ يجوزُ أن يرتفعَ،
    و`المحروسُ` لا يجوزُ أن ينقُصَ، و`المُعلَنُ بلا حرسٍ` لا يجوزُ أن يرتفعَ
    فوقَ أرضِيّتِه المُعلَنةِ — وكلُّ واحدٍ منها له **سببٌ مكتوبٌ** تُلزِمُ به
    البوّابةُ نفسُها.

    الأرضيّةُ المُعلَنةُ (‏W-051 · 2026-08-27): 11 مقيَّدًا · 8 محروسًا ·
    3 مُعلَنًا بسببٍ · 1 برباطٍ مقيسٍ.
    """
    _, counts = tool.audit(REPO, freshness=False)
    assert counts["registered"] >= 11, counts
    assert counts["guarded"] >= 8, counts
    assert counts["declared_only"] <= 3, counts
    assert counts["bound"] == 1, counts
    assert counts["registered"] == counts["guarded"] + counts["declared_only"], counts


def test_contract_holds_on_the_repository_as_pushed(tool: Any) -> None:
    """عقدُ النَّسَبِ مستقيمٌ على الشجرةِ كما هي — بلا إعادةِ قياسٍ تحتاجُ سجلَّ git."""
    breaches, _ = tool.audit(REPO, freshness=False)
    assert breaches == [], breaches


def test_the_report_names_the_binding_site(tool: Any) -> None:
    """مَن قرأَ التقريرَ يعرفُ **أينَ** الحرسُ لا أنَّه موجودٌ فحسب."""
    text = tool.report(REPO)
    assert ".github/workflows/measure.yml" in text
    assert "برباطٍ مقيسٍ" in text


# ---------------------------------------------------------------------------
# 2) الرباطُ في المستودعِ الحقيقيِّ — يُقرَأُ ملفُّ الوقائعِ نصًّا
# ---------------------------------------------------------------------------


def test_the_measure_workflow_verdict_is_not_neutralised() -> None:
    """`|| true` على سطرِ الحكمِ يُبطِلُه — وهي العلّةُ التي كشفَها W-048."""
    lines = MEASURE_WORKFLOW.read_text(encoding="utf-8").splitlines()
    verdicts = [
        (i, line)
        for i, line in enumerate(lines, start=1)
        if "restart_survival_probe.py --check" in line
    ]
    assert verdicts, "غابَ حكمُ المِسبارِ عن `measure.yml` — رباطٌ بلا مربوطٍ."
    for number, line in verdicts:
        assert "|| true" not in line, f"{MEASURE_WORKFLOW.name}:{number} — حكمٌ منزوعُ الأثرِ."
        assert "continue-on-error" not in line, f"{MEASURE_WORKFLOW.name}:{number}"


def test_the_measure_workflow_reruns_when_the_generator_changes() -> None:
    """مُشغِّلاتُ الوظيفةِ تذكرُ المُولِّدَ — وإلّا فقد يتغيَّرُ ولا يُشغَّلُ الحرسُ."""
    text = MEASURE_WORKFLOW.read_text(encoding="utf-8")
    assert "tools/governance/restart_survival_probe.py" in text
    assert "tests/governance/test_step18_restart_survival.py" in text


def test_the_probe_check_mode_does_not_write_what_it_judges() -> None:
    """الحرسُ لا يكتبُ ما يحكمُ عليه — يُقاسُ من المصدرِ لا من الظنِّ."""
    text = PROBE.read_text(encoding="utf-8")
    assert "if not args.check:" in text, (
        "وضعُ `--check` يجبُ أن يتخطّى النشرَ — وإلّا كانَ شاهدًا وقاضيًا وموضوعًا."
    )
    write_line = next(
        i for i, line in enumerate(text.splitlines()) if "_write_json(results, summary)" in line
    )
    guard_line = next(
        i for i, line in enumerate(text.splitlines()) if "if not args.check:" in line
    )
    assert guard_line < write_line, "شرطُ الامتناعِ عن الكتابةِ يجبُ أن يسبِقَ الكتابةَ."


# ---------------------------------------------------------------------------
# 3) الحرسُ يَحمَرُّ فعلًا — يُصنَعُ كلُّ عيبٍ قصدًا وتُنتظَرُ الحُمرةُ
# ---------------------------------------------------------------------------

_GENERATOR = """#!/usr/bin/env python3
import json
print(json.dumps({"$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.",
                  "count": 2}, ensure_ascii=False))
"""

_WORKFLOW = """name: قياسٌ مُصطنَعٌ
on:
  push:
    paths:
      - 'tools/fake_gen.py'
jobs:
  measure:
    runs-on: ubuntu-latest
    steps:
      - name: الحكمُ
        run: python tools/fake_gen.py --check
"""


def _fake_tree(tmp_path: Path, workflow: str | None = _WORKFLOW) -> Path:
    """اصنعْ شجرةً فيها مُولِّدٌ وملفٌّ منشورٌ وملفُّ وقائعَ يحملُ الحرسَ."""
    root = tmp_path / "repo"
    (root / "tools").mkdir(parents=True)
    (root / "tools" / "fake_gen.py").write_text(_GENERATOR, encoding="utf-8")
    measurements = root / "docs" / "audit" / "measurements"
    measurements.mkdir(parents=True)
    (measurements / "fake.json").write_text(
        json.dumps(
            {
                "$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.",
                "count": 2,
            },
            ensure_ascii=False,
            indent=1,
        )
        + "\n",
        encoding="utf-8",
    )
    if workflow is not None:
        flows = root / ".github" / "workflows"
        flows.mkdir(parents=True)
        (flows / "fake.yml").write_text(workflow, encoding="utf-8")
    return root


def _bound_entry(tool: Any, **overrides: Any) -> tuple:
    fields: dict[str, Any] = {
        "name": "fake.json",
        "generator": "tools/fake_gen.py",
        "command": "python tools/fake_gen.py > docs/audit/measurements/fake.json",
        "strategy": "bound",
        "bound_workflow": ".github/workflows/fake.yml",
        "bound_commands": ("python tools/fake_gen.py --check",),
        "reason": "سببٌ مكتوبٌ — قياسٌ مُصطنَعٌ للفحصِ.",
    }
    fields.update(overrides)
    return (tool.Provenance(**fields),)


def test_a_correct_binding_is_green(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """قبلَ انتظارِ الحُمرةِ تُثبَتُ الخُضرةُ — وإلّا فالحرسُ يَحمَرُّ دائمًا لا عن سببٍ."""
    root = _fake_tree(tmp_path)
    monkeypatch.setattr(tool, "REGISTRY", _bound_entry(tool))
    breaches, counts = tool.audit(root)
    assert breaches == [], breaches
    assert counts["guarded"] == 1 and counts["bound"] == 1, counts


def test_gate_reddens_when_the_bound_workflow_is_missing(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """رباطٌ إلى ملفٍّ لا وجودَ له = رباطٌ بلا موضِعٍ."""
    root = _fake_tree(tmp_path, workflow=None)
    monkeypatch.setattr(tool, "REGISTRY", _bound_entry(tool))
    breaches, _ = tool.audit(root)
    assert any("مفقودٌ" in b for b in breaches), breaches


def test_gate_reddens_when_the_bound_command_is_absent(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """أمرٌ يُزعَمُ في الوظيفةِ ولا يُوجَدُ فيها = دعوى لا رباطٌ."""
    root = _fake_tree(tmp_path)
    monkeypatch.setattr(
        tool,
        "REGISTRY",
        _bound_entry(tool, bound_commands=("python tools/fake_gen.py --verify-all",)),
    )
    breaches, _ = tool.audit(root)
    assert any("غائبٌ عن" in b for b in breaches), breaches


def test_gate_reddens_when_the_bound_command_is_neutralised(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """`|| true` هي العيبُ الأصليُّ — فيُصنَعُ قصدًا ويُنتظَرُ الحُمرةُ."""
    root = _fake_tree(
        tmp_path, workflow=_WORKFLOW.replace("--check", "--check || true")
    )
    monkeypatch.setattr(tool, "REGISTRY", _bound_entry(tool))
    breaches, _ = tool.audit(root)
    assert any("منزوعُ الأثرِ" in b for b in breaches), breaches


def test_gate_reddens_on_a_step_level_exemption(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """`continue-on-error: true` إعفاءٌ آخرُ بصورةٍ أنظفَ — ويُحمَرُّ كذلك."""
    root = _fake_tree(
        tmp_path,
        workflow=_WORKFLOW.replace(
            "      - name: الحكمُ\n", "      - name: الحكمُ\n        continue-on-error: true\n"
        ),
    )
    monkeypatch.setattr(tool, "REGISTRY", _bound_entry(tool))
    breaches, _ = tool.audit(root)
    assert any("continue-on-error" in b for b in breaches), breaches


def test_gate_reddens_when_the_workflow_ignores_the_generator(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """حرسٌ لا يُشغَّلُ حينَ يتغيَّرُ المُولِّدُ يحرسُ ماضيًا لا حاضرًا."""
    root = _fake_tree(tmp_path, workflow=_WORKFLOW.replace("tools/fake_gen.py", "x.py"))
    monkeypatch.setattr(tool, "REGISTRY", _bound_entry(tool))
    breaches, _ = tool.audit(root)
    assert any("مسارُ المُولِّدِ" in b for b in breaches), breaches


def test_gate_reddens_on_a_bound_entry_without_a_workflow_field(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """وضعُ `bound` بلا موضِعِ حرسٍ مُعلَنٍ = إعفاءٌ متنكِّرٌ في صورةِ حرسٍ."""
    root = _fake_tree(tmp_path)
    monkeypatch.setattr(tool, "REGISTRY", _bound_entry(tool, bound_workflow=""))
    breaches, _ = tool.audit(root)
    assert any("رباطٌ بلا موضِع" in b for b in breaches), breaches


def test_gate_reddens_on_a_bound_entry_without_commands(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """ولا رباطَ بلا مربوطٍ."""
    root = _fake_tree(tmp_path)
    monkeypatch.setattr(tool, "REGISTRY", _bound_entry(tool, bound_commands=()))
    breaches, _ = tool.audit(root)
    assert any("رباطٌ بلا مربوط" in b for b in breaches), breaches


def test_gate_reddens_on_a_bound_entry_without_a_reason(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """والحدُّ يُعلَنُ: رباطٌ بلا سببٍ مكتوبٍ يُخفي ما لا يحرسُه."""
    root = _fake_tree(tmp_path)
    monkeypatch.setattr(tool, "REGISTRY", _bound_entry(tool, reason=""))
    breaches, _ = tool.audit(root)
    assert any("بلا سببٍ مكتوبٍ" in b for b in breaches), breaches


def test_gate_reddens_when_a_bound_test_file_is_missing(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """فحصٌ يُعلَنُ حارسًا للمضمونِ ولا وجودَ له = شاهدٌ غائبٌ."""
    root = _fake_tree(tmp_path)
    monkeypatch.setattr(
        tool, "REGISTRY", _bound_entry(tool, bound_tests=("tests/nope.py",))
    )
    breaches, _ = tool.audit(root)
    assert any("مفقودٌ" in b for b in breaches), breaches


def test_gate_reddens_on_decorative_binding_fields(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """حقلُ رباطٍ في وضعٍ لا يقيسُه زينةٌ تُوهِمُ حرسًا — فيُحمَرُّ."""
    root = _fake_tree(tmp_path)
    monkeypatch.setattr(
        tool,
        "REGISTRY",
        _bound_entry(
            tool,
            strategy="declared",
            bound_commands=("python tools/fake_gen.py --check",),
        ),
    )
    breaches, _ = tool.audit(root)
    assert any("زينةٌ" in b for b in breaches), breaches
