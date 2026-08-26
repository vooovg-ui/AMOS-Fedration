"""الهدف: حراسةُ ما رُفِعَ في W-038 — وضعُ قياسٍ لا يكتبُ في الشجرةِ لمِسبارَي
القضاءِ والمالِ، ونقلُ قيدَيهما من «مُعلَنٍ» إلى «محروسٍ»، وقسمةُ الحرسِ على
شطرَينِ **مُعلَنةً ومربوطةً** لا صامتةً.

الخطرُ الذي تحرسُه هذه الفحوصُ ثلاثةٌ:

١. أن يعودَ المِسبارُ فيكتبَ إلى مسارِ قياسِه ثابتًا، فيصيرَ حرسُه كتابةً لِما
   يحكمُ عليه — وهي المحرَّمةُ الأصليّةُ (الحارسُ لا يكتبُ ما يحكمُ عليه).
٢. أن يتغيَّرَ سلوكُ المِسبارِ **بلا رايةٍ**، فينقُضَ قياسًا منشورًا كانَ قد
   وُلِّدَ بذاكَ السلوكِ نفسِه.
٣. أن تنهارَ القسمةُ إلى تخطٍّ صامتٍ: أن تُنزَعَ إحدى الخطوتَينِ من ملفِّ
   الوقائعِ فيبقى نصفُ الحرسِ ويُظَنَّ أنَّه كلُّه (القاعدةُ 10 · W-012).

والفحوصُ تقرأُ المصدرَ نصًّا ولا تستوردُ حزمةَ الخدماتِ، عملًا بقاعدةِ
الحوكمةِ: فحصُ الحوكمةِ لا يعتمدُ على بيئةِ التنفيذِ التي يحكمُ عليها.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/governance/measurement_provenance.py"
WORKFLOW = ROOT / ".github/workflows/ci.yml"
PROBES = (
    ROOT / "tools/audit/judicial_gate_probe.py",
    ROOT / "tools/audit/treasury_gate_probe.py",
)


def _load():
    """استوردِ الأداةَ من مسارِها بلا حزمةٍ.

    يُسجَّلُ الموديولُ في `sys.modules` **قبلَ** التنفيذِ لأنَّ `@dataclass` مع
    `from __future__ import annotations` يقرأُ الموديولَ من السجلِّ عند بناءِ
    الصنفِ، فيسقطُ بـAttributeError لو غابَ (مقيسٌ على 3.14).
    """
    spec = importlib.util.spec_from_file_location("w038_provenance", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["w038_provenance"] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop("w038_provenance", None)
        raise
    return module


MP = _load()


def _entry(name: str):
    for candidate in MP.REGISTRY:
        if candidate.name == name:
            return candidate
    raise AssertionError(f"لا قيدَ باسمِ {name}")


# ───────────────────────── ١) المِسبارُ لا يكتبُ ما يُحكَمُ عليه ─────────────────────────


@pytest.mark.parametrize("probe", PROBES, ids=lambda p: p.name)
def test_probe_accepts_dictated_path(probe: Path) -> None:
    """المسارُ يُملى على المِسبارِ ولا يُفرَضُ عليه."""
    text = probe.read_text(encoding="utf-8")
    assert '"--json" in sys.argv' in text, (
        f"{probe.name}: لا وضعَ قياسٍ يُملى مسارُه — فحرسُه يقتضي أن يكتبَ "
        "الحارسُ ما يحكمُ عليه."
    )
    assert "OUT = Path(sys.argv[_i + 1])" in text
    assert "OUT.parent.mkdir(parents=True, exist_ok=True)" in text


@pytest.mark.parametrize("probe", PROBES, ids=lambda p: p.name)
def test_probe_default_path_unchanged(probe: Path) -> None:
    """بلا رايةٍ يبقى المسارُ الافتراضيُّ هو نفسَه — فلا يُنقَضُ منشورٌ."""
    text = probe.read_text(encoding="utf-8")
    assert 'DEFAULT_OUT = ROOT / "docs/audit/measurements/' in text
    assert "OUT = DEFAULT_OUT" in text, (
        f"{probe.name}: السلوكُ الافتراضيُّ لم يُصَنْ — والقياسُ المنشورُ وُلِّدَ به."
    )


@pytest.mark.parametrize("probe", PROBES, ids=lambda p: p.name)
def test_probe_rejects_flag_without_path(probe: Path) -> None:
    """رايةٌ بلا مسارٍ تُرَدُّ صراحةً ولا تُبتلَعُ صمتًا."""
    text = probe.read_text(encoding="utf-8")
    assert "raise SystemExit" in text
    assert "if _i + 1 >= len(sys.argv):" in text


# ───────────────────────── ٢) القيدانِ صارا محروسَينِ ─────────────────────────


@pytest.mark.parametrize(
    "name", ("judicial_gate_matrix.json", "treasury_gate_matrix.json")
)
def test_probe_entries_are_guarded_now(name: str) -> None:
    """ما كانَ مُعلَنًا في W-037 صارَ محروسًا بإعادةِ قياسٍ في W-038."""
    entry = _entry(name)
    assert entry.strategy == "tmpfile", (
        f"{name}: عادَ إلى الإعلانِ بلا حرسٍ — وقد أمكنَ حرسُه، فالتراجعُ نقضٌ."
    )
    assert entry.probe and entry.probe[-2:] == ("--json", "{out}")
    assert entry.needs == ("cryptography",)


def test_guarded_count_matches_the_registry() -> None:
    """العددُ المنشورُ في الوثائقِ يُطابِقُ السجلَّ حرفًا.

    كانَ 7 من 10 في W-038، وصارَ **8 من 10** في W-048 حينَ خرجَ
    `restart_survival.json` من الإعلانِ إلى رباطٍ مقيسٍ (‏وضعُ `bound`).
    والرقمُ يُقاسُ هنا ويُحرسُ تفصيلُه في `test_w048_bound_provenance.py`.
    """
    guarded = [e for e in MP.REGISTRY if e.strategy != "declared"]
    bound = [e for e in MP.REGISTRY if e.strategy == "bound"]
    assert len(MP.REGISTRY) == 10
    assert len(guarded) == 8
    assert len(bound) == 1
    assert len(MP.REGISTRY) - len(guarded) == 2


# ───────────────────────── ٣) القسمةُ مُعلَنةٌ ومعدودةٌ ─────────────────────────


def test_partition_is_exhaustive() -> None:
    """لا قيدَ يسقطُ بينَ الشطرَينِ: مجموعُهما هو المحروسُ كلُّه بلا زيادةٍ."""
    without = {e.name for e in MP.REGISTRY if e.strategy != "declared" and not e.needs}
    only = {e.name for e in MP.REGISTRY if e.strategy != "declared" and e.needs}
    guarded = {e.name for e in MP.REGISTRY if e.strategy != "declared"}
    assert without | only == guarded
    assert without & only == set()
    assert only, "الشطرُ الثاني فارغٌ — فالقسمةُ عبثٌ أو أُلغِيَ الحرسُ."


def test_deferred_is_counted_not_silenced() -> None:
    """المُؤَجَّلُ يُعَدُّ رقمًا — فحارسٌ يُتخطَّى بصمتٍ ليس حارسًا."""
    _, counts = MP.audit(ROOT, freshness=True, deps=False)
    assert counts["needs_deps"] == 2
    assert counts["deferred"] == 2, "التأجيلُ لم يُعَدَّ — وهذا هو التخطي الصامتُ."


def test_green_line_names_the_deferred_number() -> None:
    """سطرُ الخُضرةِ نفسُه يُظهِرُ ما لم يُقَسْ هنا."""
    source = TOOL.read_text(encoding="utf-8")
    assert 'if counts.get("deferred"):' in source
    assert "ومُؤَجَّلٌ إلى الشطرِ الآخرِ" in source


def test_flags_are_mutually_exclusive() -> None:
    """الشطرانِ لا يُجمَعانِ: جمعُهما التباسٌ يُرَدُّ برمزٍ لا يُخضَّرُ."""
    result = subprocess.run(
        [sys.executable, str(TOOL), ".", "--check", "--only-deps", "--without-deps"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2, result.stdout + result.stderr


def test_needs_is_not_a_backdoor_to_exemption() -> None:
    """`needs` قسمةٌ لا إعفاءٌ: مُعلَنٌ يزعمُ حزمًا لازمةً خَرْمٌ.

    وكانَ الموضوعُ `restart_survival.json` لأنَّه كانَ مُعلَنًا بلا حرسٍ، فلمّا
    صارَ مربوطًا في W-048 نُقِلَ الفحصُ إلى مُعلَنٍ قائمٍ فعلًا — فالمقصودُ
    الحكمُ لا اسمُ الملفِّ، ولو لم يُنقَلْ لمرَّ الفحصُ بلا أن يقيسَ شيئًا.
    """
    target = next(e.name for e in MP.REGISTRY if e.strategy == "declared")
    entry = replace(_entry(target), needs=("cryptography",))
    original = MP.REGISTRY
    try:
        MP.REGISTRY = tuple(entry if e.name == target else e for e in original)
        breaches, _ = MP.audit(ROOT, freshness=False)
    finally:
        MP.REGISTRY = original
    assert any("قسمةٌ لا إعفاءٌ" in b for b in breaches), (
        "حقلُ `needs` صارَ بابًا خلفيًّا: يُعفي من الحرسِ بلا سببٍ مكتوبٍ."
    )


# ───────────────────────── ٤) رباطُ الشطرَينِ في ملفِّ الوقائعِ ─────────────────────────


def test_both_splits_are_wired_in_ci() -> None:
    """الخطوتانِ كلتاهما موجودةٌ — فنزعُ إحداهما يُسقِطُ فحصًا لا يُنقِصُه."""
    workflow = WORKFLOW.read_text(encoding="utf-8")
    for flag in ("--check --without-deps", "--check --only-deps"):
        assert f"measurement_provenance.py . {flag}" in workflow, (
            f"شطرُ `{flag}` غيرَ مربوطٍ في ملفِّ الوقائعِ — فالقسمةُ انهارت إلى "
            "تخطٍّ صامتٍ: نصفُ الحرسِ يُظَنُّ كلَّه."
        )


def test_deps_split_runs_where_deps_are_installed() -> None:
    """شطرُ الحزمِ يُشغَّلُ في وظيفةٍ تُنصِّبُ الحزمَ فعلًا لا في وظيفةٍ عارية."""
    workflow = WORKFLOW.read_text(encoding="utf-8")
    marker = "measurement_provenance.py . --check --only-deps"
    index = workflow.index(marker)
    # الوظيفةُ هي كلُّ ما قبلَ الخطوةِ منذُ آخرِ رأسِ وظيفةٍ (سطرٌ بمسافتَينِ ثمَّ اسمٌ).
    head = workflow[:index]
    job_start = max(
        head.rfind("\n  constitutional-kernel:"),
        head.rfind("\n  truth-audit:"),
    )
    assert job_start != -1
    job_text = head[job_start:]
    assert "pip install -r requirements-dev.txt" in job_text, (
        "شطرُ `--only-deps` في وظيفةٍ لا تُنصِّبُ `cryptography` — فسيسقطُ "
        "بـModuleNotFoundError قبلَ أن يُقاسَ شيءٌ، وذلك سقوطُ وظيفةٍ لا حكمُ حرسٍ."
    )
    assert "constitutional-kernel:" in job_text, (
        "موضِعُ الشطرِ ليس وظيفةَ النواةِ الدستوريّةِ — والمِسبارانِ يقيسانِ أحكامَها."
    )


def test_truth_audit_step_declares_the_split_in_its_name() -> None:
    """اسمُ الخطوةِ يقولُ إنَّها شطرٌ — فلا يُقرَأُ خُضرتُها على أنَّها الكلُّ."""
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "ما لا يحتاج حزما (W-037 · W-038)" in workflow
