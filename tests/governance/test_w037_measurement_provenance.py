"""
AMOS-Federation — حرسُ نَسَبِ القياساتِ المنشورةِ (W-037)
الهدف: أن لا يُنشَرَ قياسٌ في `docs/audit/measurements/` بلا قيدِ نَسَبٍ، وأن
       يُعادَ قياسُ ما يُمكِنُ إعادةُ قياسِه بلا كتابةٍ في الشجرةِ، وأن يُعلَنَ
       ما لا يُمكِنُ **بسببٍ مكتوبٍ ورقمٍ ظاهرٍ** لا بصمتٍ.
النطاق: tests/governance
المالك: الجذر (حكمُ المستودعِ)
تاريخ الإنشاء: 2026-08-24 (W-037)
تاريخ آخر تعديل: 2026-08-24 (W-037)

## لماذا وُجِدَ هذا الملفُّ

كانَ في مجلَّدِ القياساتِ عشرةُ ملفّاتٍ منشورةٍ واثنانِ فقط محروسانِ. فجُرِّبَت
إعادةُ توليدِ الباقي في W-037 فوُجِدَت ثلاثةُ قياساتٍ متقادمةً فعلًا: مواقعُ
الكتابةِ 203 والحقُّ 217، ودَينُ الهجرةِ 168 والحقُّ 182، والأسئلةُ السياديّةُ
27 والحقُّ 42. لم يكنِ العيبُ في الأرقامِ بل في أنَّ لا شيءَ كانَ يُظهِرُها.

## وما يحرسُه هذا الملفُّ من الحرسِ نفسِه

بوّابةٌ قد تصيرُ زينةً: تُقيَّدُ الملفّاتُ ثمَّ لا يُقارَنُ شيءٌ، أو يُقارَنُ ثمَّ
لا يُحمَرُّ عندَ الانحرافِ، أو يُصلِحُ الحرسُ ما يحكمُ عليه فيُصادِقُ على نفسِه.
فهذه الفحوصُ تُثبِتُ الأمورَ الثلاثةَ: الحرسُ **يَحمَرُّ** عندَ انحرافٍ مُصطنَعٍ،
و**لا يكتبُ** ما يحكمُ عليه، و**لا يمرُّ** ملفٌّ بلا قيدٍ ولا قيدٌ بلا سببٍ.

## وما لا يفعلُه

لا يشترطُ أن يكونَ كلُّ قياسٍ محروسًا بإعادةِ توليدٍ — فبعضُها يُقاسُ من قاعدةٍ
حيّةٍ أو بإطلاقِ عملياتٍ، ولا يُزوَّرُ له مُولِّدٌ. ويشترطُ بدلًا من ذلكَ أن
يكونَ **مُعلَنًا بسببٍ**، وأن يُعَدَّ الباقي بلا حرسٍ رقمًا يُقرَأُ.
"""

from __future__ import annotations

import ast
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO = discover_repo_root(__file__)
TOOL = REPO / "tools" / "governance" / "measurement_provenance.py"
INVENTORY_TOOL = REPO / "tools" / "governance" / "in_memory_inventory.py"
AUDIT_TOOL = REPO / "tools" / "governance" / "truth_audit.py"
MEASUREMENTS = REPO / "docs" / "audit" / "measurements"


def _load(path: Path, name: str) -> Any:
    """حمِّلِ الأداةَ وحدَها بلا حزمةٍ — كما تُشغَّلُ في البوّابةِ نفسِها."""
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    # تُسجَّلُ الوحدةُ قبلَ تنفيذِها لا بعدَه: `dataclass` يحلُّ التأشيراتِ
    # النصّيّةَ من `sys.modules[cls.__module__]`، فإن غابَت سقطَ التحميلُ بـ`AttributeError`
    # ولا علاقةَ للأداةِ بالعيبِ — وهو عيبُ مُحمِّلِ الفحصِ لا عيبُ المقيسِ.
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(name, None)
        raise
    return module


@pytest.fixture(scope="module")
def tool() -> Any:
    return _load(TOOL, "measurement_provenance_under_test")


# ---------------------------------------------------------------------------
# 1) العقدُ على المستودعِ كما هو مدفوعٌ
# ---------------------------------------------------------------------------


def test_contract_holds_on_the_repository_as_pushed(tool: Any) -> None:
    """العقدُ مستقيمٌ على الشجرةِ المدفوعةِ — بلا إعادةِ قياسٍ تحتاجُ سجلَّ git."""
    breaches, counts = tool.audit(REPO, freshness=False)
    assert breaches == [], "خُرومٌ في عقدِ النَّسَبِ: " + " | ".join(breaches)
    assert counts["registered"] == len(tool.REGISTRY)
    assert counts["guarded"] + counts["declared_only"] == counts["registered"]


def test_every_published_measurement_is_registered(tool: Any) -> None:
    """لا ملفَّ بلا قيدٍ: كلُّ ملفٍّ في المجلَّدِ مُقيَّدٌ أو مُعلَنٌ نصًّا لا قياسًا."""
    on_disk = {p.name for p in MEASUREMENTS.iterdir() if p.is_file()}
    registered = {e.name for e in tool.REGISTRY}
    orphans = on_disk - registered - set(tool.PROSE_FILES)
    assert orphans == set(), f"قياساتٌ منشورةٌ بلا قيدِ نَسَبٍ: {sorted(orphans)}"
    phantoms = registered - on_disk
    assert phantoms == set(), f"قيودُ نَسَبٍ بلا ملفٍّ: {sorted(phantoms)}"


def test_every_registered_generator_exists_or_is_declared_absent(tool: Any) -> None:
    """لا نَسَبَ إلى معدومٍ: المُولِّدُ المُعلَنُ موجودٌ، أو لا مُولِّدَ ومعه سببٌ."""
    for entry in tool.REGISTRY:
        if entry.generator:
            assert (REPO / entry.generator).exists(), (
                f"{entry.name}: المُولِّدُ المُعلَنُ مفقودٌ: {entry.generator}"
            )
        else:
            assert entry.reason.strip(), (
                f"{entry.name}: بلا مُولِّدٍ وبلا سببٍ مكتوبٍ — وذاكَ نَسَبٌ مجهولٌ."
            )
        assert entry.command.strip(), f"{entry.name}: بلا أمرٍ يُعيدُ توليدَه."


def test_declared_only_entries_carry_a_written_reason(tool: Any) -> None:
    """ما لا يُعادُ قياسُه يُعلِنُ سببَه — وإلّا صارَ الإعلانُ سترًا للنقصِ."""
    for entry in tool.REGISTRY:
        if entry.strategy == "declared":
            assert len(entry.reason.strip()) >= 40, (
                f"{entry.name}: سببُ تركِ الحرسِ أقصرُ من أن يكونَ سببًا."
            )


def test_ignored_fields_are_justified(tool: Any) -> None:
    """لا حقلَ يُستثنى من المقارنةِ بلا سببٍ — وإلّا فُتِحَ بابُ تخفيفِ الحكمِ."""
    for entry in tool.REGISTRY:
        if entry.ignore:
            assert entry.reason.strip(), f"{entry.name}: استثناءٌ بلا سببٍ."
            for field in entry.ignore:
                assert field in entry.reason, (
                    f"{entry.name}: الحقلُ {field} مُستثنًى ولا يُسمّيه السببُ."
                )


def test_strategies_are_known(tool: Any) -> None:
    # W-048: صارَ في العقدِ وضعٌ محروسٌ بلا أمرِ قياسٍ في هذه البوّابةِ: `bound`،
    # حرسُه قائمٌ في وظيفةٍ أخرى و**رباطُه يُقاسُ نصًّا**. فلم يُوسَّعِ
    # الفحصُ بل تُركَ لـ`PROBING` أن تُسميَ من يلزمُه الأمرُ، وزيدَ أنَّ
    # `bound` يلزمُه رباطٌ — فلا يصيرُ بابًا يُفلَتُ منه من أمرٍ ورباطٍ معًا.
    for entry in tool.REGISTRY:
        assert entry.strategy in tool.STRATEGIES, entry.strategy
        if entry.strategy in tool.PROBING:
            assert entry.probe, f"{entry.name}: وضعُه يقتضي أمرَ قياسٍ ولا أمرَ له."
        elif entry.strategy == "bound":
            assert entry.bound_workflow and entry.bound_commands, (
                f"{entry.name}: محروسٌ بلا أمرٍ ولا رباطٍ — فما حرسُه؟"
            )
        else:
            assert entry.strategy == "declared", entry.strategy


# ---------------------------------------------------------------------------
# 2) لا مسارَ جهازِ عاملٍ في قياسٍ منشورٍ — علّةُ W-035 تُمنَعُ لا تُستثنى
# ---------------------------------------------------------------------------


def test_no_published_measurement_carries_a_machine_path(tool: Any) -> None:
    """كانَ جردُ المخازنِ ينشرُ `/home/<عاملٍ>/...` في حقلِ `repo`؛ فلا يعودُ."""
    offenders: list[str] = []
    for path in sorted(MEASUREMENTS.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for hit in tool._machine_paths(payload):
            offenders.append(f"{path.name}: {hit}")
    assert offenders == [], "مساراتُ أجهزةٍ منشورةٌ في قياساتٍ: " + " | ".join(offenders)


def test_inventory_publishes_an_identity_not_a_path() -> None:
    """حقلُ `repo` هُويّةٌ لا مسارٌ — يُقرَأُ من الملفِّ المنشورِ نفسِه."""
    payload = json.loads(
        (MEASUREMENTS / "in_memory_inventory.json").read_text(encoding="utf-8")
    )
    repo = payload["repo"]
    assert not repo.startswith("/"), f"مسارٌ مُطلَقٌ منشورٌ: {repo}"
    assert "/" not in repo and "\\" not in repo, f"ليس هُويّةً: {repo}"


def test_repo_identity_does_not_drift_from_truth_audit() -> None:
    """نسخةُ `_repo_identity` في أداتَينِ محروسةٌ: تفترقانِ فيسقطُ هذا الفحصُ.

    `tools/` ليست حزمةً فلا تُستورَدُ أداةٌ من أداةٍ؛ فالنسخُ مقصودٌ، وثمنُه هذا
    الفحصُ: يُقارَنُ جسدُ الدالّتَينِ نصًّا (بلا التوثيقِ) فلا تنحرفُ إحداهما صامتةً.
    """

    def body(path: Path) -> str:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "_repo_identity":
                statements = node.body
                if statements and isinstance(statements[0], ast.Expr):
                    first = statements[0].value
                    if isinstance(first, ast.Constant) and isinstance(first.value, str):
                        statements = statements[1:]
                return "\n".join(ast.dump(s) for s in statements)
        raise AssertionError(f"لا دالّةَ `_repo_identity` في {path}")

    assert body(INVENTORY_TOOL) == body(AUDIT_TOOL), (
        "نسختا `_repo_identity` افترقتا — وحِّدْهما أو انزعِ النسخَ."
    )


# ---------------------------------------------------------------------------
# 3) الحرسُ يَحمَرُّ فعلًا — بشجرةٍ مُصطنَعةٍ يُصنَعُ فيها الانحرافُ قصدًا
# ---------------------------------------------------------------------------

_GENERATOR = """#!/usr/bin/env python3
import json, sys
print(json.dumps({"$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.",
                  "count": 2}, ensure_ascii=False))
"""


def _fake_tree(tmp_path: Path, published: dict) -> Path:
    """اصنعْ شجرةً صغيرةً فيها مُولِّدٌ يطبعُ قياسًا وملفٌّ منشورٌ."""
    root = tmp_path / "repo"
    (root / "tools").mkdir(parents=True)
    (root / "tools" / "fake_gen.py").write_text(_GENERATOR, encoding="utf-8")
    measurements = root / "docs" / "audit" / "measurements"
    measurements.mkdir(parents=True)
    (measurements / "fake.json").write_text(
        json.dumps(published, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    return root


def _fake_registry(tool: Any) -> tuple:
    return (
        tool.Provenance(
            name="fake.json",
            generator="tools/fake_gen.py",
            command="python tools/fake_gen.py > docs/audit/measurements/fake.json",
            strategy="stdout",
            probe=("python", "tools/fake_gen.py"),
        ),
    )


def test_gate_reddens_when_a_published_measurement_goes_stale(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """بوّابةٌ لا تَحمَرُّ عندَ انحرافٍ ليست بوّابةً — فيُصنَعُ الانحرافُ ويُنتظَرُ الحُمرةُ."""
    root = _fake_tree(
        tmp_path,
        {"$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.", "count": 1},
    )
    monkeypatch.setattr(tool, "REGISTRY", _fake_registry(tool))
    breaches, _ = tool.audit(root)
    assert any("متقادمٌ" in b for b in breaches), breaches
    assert any("count" in b for b in breaches), breaches


def test_gate_is_green_when_the_published_measurement_is_fresh(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """وبوّابةٌ تَحمَرُّ دائمًا ليست بوّابةً أيضًا — فيُثبَتُ خُضرتُها عندَ الطزاجةِ."""
    root = _fake_tree(
        tmp_path,
        {"$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.", "count": 2},
    )
    monkeypatch.setattr(tool, "REGISTRY", _fake_registry(tool))
    breaches, counts = tool.audit(root)
    assert breaches == [], breaches
    # W-038: زِيدَ في العدِّ حقلانِ يُظهِرانِ القسمةَ على الحزمِ اللازمةِ رقمًا،
    # ولم يُنقَصْ حقلٌ — فالتصحيحُ إضافةٌ لا محوٌ.
    # W-048: وزِيدَ `bound` ليُقرأَ من المحروسِ ما حرسُه رباطٌ مقيسٌ لا
    # إعادةُ قياسٍ — فلا يُقرأُ الرقمُ المجموعُ أكثرَ ممّا يقول. ولم يُنقَصْ حقلٌ.
    assert counts == {
        "registered": 1,
        "guarded": 1,
        "declared_only": 0,
        "bound": 0,
        "needs_deps": 0,
        "deferred": 0,
    }


def test_gate_does_not_write_what_it_judges(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """الحرسُ يحكمُ ولا يُصلِحُ: المنشورُ المنحرفُ يبقى كما هو بعدَ الحكمِ."""
    stale = {"$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.", "count": 1}
    root = _fake_tree(tmp_path, stale)
    published = root / "docs" / "audit" / "measurements" / "fake.json"
    before, before_mtime = published.read_bytes(), published.stat().st_mtime_ns
    monkeypatch.setattr(tool, "REGISTRY", _fake_registry(tool))
    breaches, _ = tool.audit(root)
    assert breaches, "كانَ يجبُ أن يَحمَرَّ"
    assert published.read_bytes() == before, "الحرسُ كتبَ ما يحكمُ عليه"
    assert published.stat().st_mtime_ns == before_mtime, "الحرسُ مسَّ زمنَ الملفِّ"


def test_gate_reddens_on_an_unregistered_file(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """ملفٌّ يُنشَرُ بلا قيدٍ يُسقِطُ البوّابةَ — فالقيدُ شرطُ النشرِ لا زينةٌ بعدَه."""
    root = _fake_tree(
        tmp_path,
        {"$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.", "count": 2},
    )
    intruder = root / "docs" / "audit" / "measurements" / "smuggled.json"
    intruder.write_text('{"$comment": "دخيلٌ"}\n', encoding="utf-8")
    monkeypatch.setattr(tool, "REGISTRY", _fake_registry(tool))
    breaches, _ = tool.audit(root)
    assert any("smuggled.json" in b and "بلا قيدِ نَسَبٍ" in b for b in breaches), breaches


def test_gate_reddens_on_a_machine_path_in_a_measurement(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """مسارُ جهازٍ منشورٌ يُسقِطُ البوّابةَ حتّى لو دُفِنَ في عمقِ البنيةِ."""
    root = _fake_tree(
        tmp_path,
        {
            "$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.",
            "count": 2,
            "meta": {"where": ["/home/worker/checkout/AMOS-Fedration"]},
        },
    )
    monkeypatch.setattr(tool, "REGISTRY", _fake_registry(tool))
    breaches, _ = tool.audit(root)
    assert any("مسارُ جهازٍ منشورٌ" in b for b in breaches), breaches


def test_gate_reddens_when_the_header_stops_naming_its_generator(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """القيدُ والنصُّ لا يفترقانِ صامتَينِ: ترويسةٌ لا تُسمّي مُولِّدَها تُحمِّرُ."""
    root = _fake_tree(
        tmp_path, {"$comment": "الهدف: قياسٌ بلا نَسَبٍ في ترويستِه.", "count": 2}
    )
    monkeypatch.setattr(tool, "REGISTRY", _fake_registry(tool))
    breaches, _ = tool.audit(root)
    assert any("لا تُسمّي المُولِّدَ" in b for b in breaches), breaches


def test_gate_reddens_on_a_missing_generator(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """نَسَبٌ إلى أداةٍ غيرِ موجودةٍ يُسقِطُ البوّابةَ — وهي حالةُ ملفٍّ يُتَّمَ مُولِّدُه."""
    root = _fake_tree(
        tmp_path,
        {"$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/gone.py.", "count": 2},
    )
    monkeypatch.setattr(
        tool,
        "REGISTRY",
        (
            tool.Provenance(
                name="fake.json",
                generator="tools/gone.py",
                command="python tools/gone.py",
                strategy="declared",
                reason="سببٌ مكتوبٌ طويلٌ بما يكفي ليُقبَلَ في الفحصِ الخاصِّ بالأسبابِ.",
            ),
        ),
    )
    breaches, _ = tool.audit(root)
    assert any("المُولِّدُ المُعلَنُ مفقودٌ" in b for b in breaches), breaches


def test_gate_reddens_on_a_declared_entry_without_a_reason(
    tool: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """إعلانٌ بلا سببٍ هو النقصُ مستورًا — فيُحمَّرُ."""
    root = _fake_tree(
        tmp_path,
        {"$comment": "الهدف: قياسٌ مُصطنَعٌ — مُخرَجُ tools/fake_gen.py.", "count": 2},
    )
    monkeypatch.setattr(
        tool,
        "REGISTRY",
        (
            tool.Provenance(
                name="fake.json",
                generator="tools/fake_gen.py",
                command="python tools/fake_gen.py",
                strategy="declared",
                reason="",
            ),
        ),
    )
    breaches, _ = tool.audit(root)
    assert any("بلا سببٍ مكتوبٍ" in b for b in breaches), breaches


# ---------------------------------------------------------------------------
# 4) الحرسُ أمرٌ يُشغَّلُ لا دالّةٌ تُقرَأُ
# ---------------------------------------------------------------------------


def test_gate_runs_as_a_command() -> None:
    """`DONE = Capability Proven`: يُشغَّلُ كما يُشغَّلُ في CI ويُقرَأُ حكمُه."""
    done = subprocess.run(
        [sys.executable, str(TOOL), str(REPO), "--check", "--contract-only"],
        capture_output=True,
        text=True,
        check=False,
        timeout=600,
    )
    assert done.returncode == 0, done.stdout + done.stderr
    assert "عقدُ نَسَبِ القياساتِ مستقيمٌ" in done.stdout


def test_report_names_the_unguarded_residual() -> None:
    """الباقي بلا حرسٍ يُقرَأُ رقمًا لا انطباعًا — فالتقريرُ يُعلِنُه."""
    done = subprocess.run(
        [sys.executable, str(TOOL), str(REPO), "--report"],
        capture_output=True,
        text=True,
        check=False,
        timeout=120,
    )
    assert done.returncode == 0, done.stderr
    assert "المُعلَنُ بلا حرسٍ:" in done.stdout
    assert "مُعلَنٌ فقط" in done.stdout
