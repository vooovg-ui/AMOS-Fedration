"""حرسُ الخطوةِ 18 — نجاةُ الحالةِ عبرَ إعادةِ التشغيلِ تُقاسُ ولا تُدَّعى.

الهدف:
    منعُ ثلاثِ صورٍ من الكذبِ الموثَّق:
      1. أن يُحذَفَ سطحٌ من المِسبارِ فيَقِلَّ الفقدُ المُعلَنُ بلا أن تُدامَ حالةٌ
         واحدةٌ — وأخطرُها **مفتاحُ الإيقافِ** فهو مُثبَّتٌ بالاسمِ هنا. وبعدَ
         إدامتِه في `W-031` صارَ مُثبَّتًا مرّتَين: لا يُحذَفُ، ولا يُعادُ متطايرًا.
      2. أن يُقالَ «هذه دائمةٌ» في وثيقةٍ أو ترويسةٍ ولا يُقاسَ ذلك بعمليّتَينِ.
      3. أن يمرَّ المِسبارُ وهو مكسورٌ: فلو فُقِدَ **شاهدا الضبطِ** (سجلُّ التدقيقِ
         والمهمّةُ الدائمةُ) لكانَ العجزُ في المِسبارِ لا في الحالة، ولذلك يُشترَطُ
         نجاتُهما صراحةً.

النطاق:
    `tools/governance/restart_survival_probe.py` ومُخرَجُه المُقيَّدُ
    `docs/audit/measurements/restart_survival.json`. ولا يُقيسُ هذا الحرسُ صوابَ
    المعمار: لا يشترطُ إدامةَ شيءٍ من نفسِه — ما يُشترَطُ إدامتُه هنا هو ما أمرَ
    به المالكُ نصًّا في (`Q-39 (أ)`)، لا ما رآه عاملٌ صوابًا.

المالك:
    `tests/governance` — حرّاسُ الحوكمةِ في المستودع.

تاريخ الإنشاء: 2026-08-22
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
PROBE_PATH = REPO_ROOT / "tools" / "governance" / "restart_survival_probe.py"
MEASUREMENT_PATH = (
    REPO_ROOT / "docs" / "audit" / "measurements" / "restart_survival.json"
)

#: أقلُّ عددٍ من الأسطحِ يُقبَلُ. القياسُ يومَ الكتابةِ (W-030) أحدَ عشرَ سطحًا،
#: وصارَ اثني عشرَ في W-032 بإضافةِ `registered_tool`، فأيُّ نقصٍ بعدَه حذفٌ
#: لسطحٍ لا تحسينٌ للمعمار.
MIN_SURFACES = 12

#: أسطحٌ مُثبَّتةٌ بالاسمِ: أثرُ فقدِها تشغيليٌّ لا تجميليّ. لا تُحذَفُ من المِسبارِ
#: أيًّا كانَ تصنيفُها — الحذفُ إخفاءٌ لا إدامة.
PINNED_SURFACES = (
    "kill_switch",
    "promotion",
    "canary",
    "cost_log",
    # أُضيفَتا في W-032: سجلّا الوكلاءِ والأدواتِ أُديما بقرارِ Q-39 (ب)،
    # فحذفُ أحدِهما من المِسبارِ يُسقِطُ دليلَ تنفيذِ القرارِ لا أكثر.
    "registered_agent",
    "registered_tool",
)

#: أسطحٌ **أُديمَت بقرارِ المالكِ** في `Q-39 (أ)` — 2026-08-23 · نُفِّذَ في `W-031`.
#: تثبيتُها هنا يمنعُ التراجعَ: من أعادَها إلى الذاكرةِ يُسقِطُ هذا الحرسَ، ومن أعلنَ
#: إدامتَها بلا قياسٍ يُسقِطُه المِسبارُ نفسُه أدناه.
#: وأُضيفَ إليها سجلّا الوكلاءِ والأدواتِ بقرارِ `Q-39 (ب)` — نُفِّذَ في `W-032`.
PINNED_DURABLE_BY_DECISION = (
    "kill_switch",
    "promotion",
    "registered_agent",
    "registered_tool",
    # W-033 · حسمُ Q-39 (ج): سجلُّ المالِ دائمٌ ويُكتَبُ فيه في مسارِ النداءِ.
    # تثبيتُه هنا يعني أنَّ إعادتَه متطايرًا تُسقِطُ الحرسَ لا تمرُّ بصمتٍ.
    "cost_log",
)

#: شاهدا الضبطِ: نجاتُهما شرطُ صدقِ المِسبارِ نفسِه.
PINNED_CONTROLS = ("audit_chain", "task")

#: ما يلزمُ القياسَ الحيَّ (مراحلُ المِسبارِ تُقلِّعُ تطبيقَ الخدمةِ وقاعدتَها).
LIVE_STACK_MODULES = ("fastapi", "sqlalchemy")
MEASURE_WORKFLOW = REPO_ROOT / ".github" / "workflows" / "measure.yml"


def _require_live_stack() -> None:
    """يُتخطَّى القياسُ الحيُّ إن غابتِ الطبقةُ المقيسةُ — بإعلانٍ وموضِعٍ بديلٍ.

    ولماذا لا يُعدُّ هذا تخطِّيًا لحارسٍ (القاعدةُ 12): تبعيّاتُ جذرِ المستودعِ
    مُعلنةٌ في `requirements-dev.txt` وحدَها وليسَ فيها تطبيقُ الخدمةِ (وذاكَ قرارُ
    معمارٍ قائمٌ: لا تُكرَّرُ تبعيّاتُ الحزمةِ في الجذر). فكانَ هذانِ الفحصانِ
    يسقُطانِ في `بوابة 5` منذُ كُتِبا (W-030) بـ`ModuleNotFoundError` لا بعجزِ إدامةٍ
    — فكانا يُبلِّغانِ عجزَ البيئةِ باسمِ عجزِ الحالة، وذاكَ كذبٌ مُوثَّقٌ معكوس.
    والموضِعُ البديلُ ليسَ وعدًا: `measure.yml` يُشغِّلُ هذا الملفَّ كلَّه بتبعيّاتٍ
    كاملةٍ، ويحرسُ وجودَ ذلكَ فحصٌ أدناه فلا يُحذَفُ صامتًا.
    """
    missing = [m for m in LIVE_STACK_MODULES if importlib.util.find_spec(m) is None]
    if missing:
        pytest.skip(
            "القياسُ الحيُّ يلزمُه طبقةُ الخدماتِ وهي غائبةٌ هنا بإعلانٍ لا بسهوٍ "
            f"(الناقصُ: {', '.join(missing)}). والقياسُ يجري في "
            ".github/workflows/measure.yml حيثُ التبعيّاتُ كاملة."
        )


#: جذرُ حزمةِ الخدمةِ **في شجرةِ المستودعِ**. المِسبارُ يحقِنُه في `PYTHONPATH` لكلِّ
#: مرحلةٍ (`restart_survival_probe.py` — حقنُ `_SERVICES_SRC`)، فما تحتَه شِفرةُ
#: المستودعِ لا توزيعٌ خارجيّ. وهذا الفرقُ هو الفرقُ بينَ «بيئةٌ ناقصةٌ» و«شِفرةٌ
#: مفقودةٌ»، ولا يُخلَطانِ: الأوّلُ لا يُقاسُ، والثاني عطبٌ يُقالُ بصوتٍ.
SERVICES_SRC = REPO_ROOT / "federal" / "executive" / "services" / "src"

#: نصُّ العجزِ الذي يُخرِجُه المِسبارُ في `detail` حينَ تسقُطُ مرحلةٌ لغيابِ وحدةٍ.
#: يُقرأُ من **مُخرَجِ المِسبارِ نفسِه** لا من قائمةٍ مكتوبةٍ بيدٍ، فلا يتقادَمُ بنموِّ
#: ما تستوردُه الطبقةُ المقيسة.
_MODULE_NOT_FOUND = re.compile(r"No module named '([^']+)'")


def _missing_third_party_module(results: Any) -> str | None:
    """اسمُ توزيعٍ خارجيٍّ غائبٍ أوقفَ القياسَ — أو `None` إن لم يكن العجزُ بيئيًّا.

    ولماذا لا يكفي `_require_live_stack` وحدَه (عطبٌ مقيسٌ لا مفترَضٌ): تلك الدالّةُ
    تفحصُ **قائمةً مكتوبةً بيدٍ** فيها اسمانِ (`fastapi` · `sqlalchemy`)، ومراحلُ
    المِسبارِ تبلُغُ عبورًا `amos_federation.common.auth` فتستوردُ `jwt` و`structlog`
    و`pydantic_settings`. فبيئةٌ فيها الاسمانِ وليس فيها البقيّةُ **لا تُتخطَّى**: تُقاسُ،
    فيعودُ `verdict="UNMEASURED"` و`survived=None` و`detail="ModuleNotFoundError: No
    module named 'jwt'"`، ثمَّ تُقرأُ تلك النتيجةُ فقدَ إدامةٍ فيُعلَنُ «مفتاحُ الإيقافِ
    لم ينجُ» و«التوجيهُ مُعطَّلٌ» — **وذاك بعينِه الكذبُ المُوثَّقُ المعكوسُ** الذي
    تُعلِنُ ترويسةُ هذا الملفِّ أنَّها أُنشِئَت لمنعِه (الصورةُ الثالثةُ في § الهدف).

    ولا يُوسَّعُ `LIVE_STACK_MODULES` بـ`amos_federation` دواءً: المِسبارُ يحقِنُ
    `_SERVICES_SRC` في بيئةِ المرحلةِ ولا يضعُه في `sys.path` للعمليّةِ الأمِّ، فـ
    `find_spec` هنا لا يراه ولو كانَ القياسُ مُستطاعًا — فيصيرُ الحرسُ متخطًّى دائمًا،
    وذاك إخفاءٌ لا صدق.

    والحدُّ مقصودٌ ومحروسٌ: **لا يُبتلَعُ إلّا نقصُ توزيعٍ خارجيٍّ**. فوحدةٌ غائبةٌ
    يُحَلُّ اسمُها الأعلى تحتَ `SERVICES_SRC` شِفرةُ المستودعِ — نقصُها عطبٌ حقيقيٌّ
    يبقى أحمرَ. وكذا كلُّ عجزٍ ليس `No module named` (مهلةٌ · رمزُ خروجٍ · قاعدةٌ
    مقفولةٌ) يبقى أحمرَ، وكلُّ حكمٍ غيرِ `UNMEASURED` لا يُنظَرُ فيه أصلًا — فمخالفةُ
    التصريحِ (`CONTRADICTS_DECLARATION`) لا تُخفى بهذا البابِ أبدًا.
    """
    for result in results:
        if result.verdict != "UNMEASURED":
            continue
        match = _MODULE_NOT_FOUND.search(result.detail or "")
        if not match:
            continue
        top = match.group(1).split(".")[0]
        in_tree = (SERVICES_SRC / top).is_dir() or (
            SERVICES_SRC / f"{top}.py"
        ).is_file()
        if in_tree:
            continue
        return match.group(1)
    return None


def _skip_if_the_environment_is_incomplete(results: Any) -> None:
    """لا يُنسَبُ نقصُ بيئةٍ إلى الحالةِ: يُسمَّى الناقصُ بالمقيسِ ويُتخطَّى القياس."""
    missing = _missing_third_party_module(results)
    if missing:
        pytest.skip(
            "القياسُ الحيُّ لم يُجرَ: مرحلةُ المِسبارِ سقطَت لغيابِ توزيعٍ خارجيٍّ "
            f"مقيسٍ في مُخرَجِها لا مفترَضٍ (الناقصُ: {missing}). وهذا عجزُ بيئةٍ "
            "لا عجزُ إدامةٍ، فلا يُقرأُ فقدَ حالةٍ. والبيئةُ الكاملةُ في "
            "tools/dev/bootstrap.sh و.github/workflows/measure.yml."
        )


def _load(name: str, path: Path) -> Any:
    """حمِّلْ أداةً من مسارِها — الحرسُ يقرأُ الأداةَ الحقيقيّةَ لا نسخةً منها."""
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, f"تعذَّرَ تحميلُ {path}."
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def probe() -> Any:
    """المِسبارُ محمَّلًا مرّةً واحدةً للحزمة."""
    return _load("restart_survival_probe_under_test", PROBE_PATH)


@pytest.fixture(scope="module")
def measurement() -> dict[str, Any]:
    """المُخرَجُ المُقيَّدُ في المستودعِ — يُقرأُ ولا يُولَّدُ هنا."""
    assert MEASUREMENT_PATH.exists(), (
        "مُخرَجُ المِسبارِ غيرُ مُقيَّدٍ: شغِّلْ "
        "`python tools/governance/restart_survival_probe.py` ثمّ قيِّدْه."
    )
    return json.loads(MEASUREMENT_PATH.read_text(encoding="utf-8"))


# =============================================================================
# 1) الأداةُ نفسُها
# =============================================================================
def test_probe_declares_its_purpose() -> None:
    """المادةُ التاسعةُ · 2: الأداةُ تُعلِنُ هدفَها في ترويستِها."""
    head = PROBE_PATH.read_text(encoding="utf-8")[:1400]
    assert "الهدف" in head and "النطاق" in head and "المالك" in head


def test_every_surface_has_a_writer_and_a_reader(probe: Any) -> None:
    """لا سطحَ مُعلَنًا بلا مرحلتَي كتابةٍ وقراءةٍ منفَّذتَين."""
    for surface in probe.SURFACES:
        assert surface.writer in probe.WRITERS, f"لا كاتبَ لـ{surface.surface_id}."
        assert surface.reader in probe.READERS, f"لا قارئَ لـ{surface.surface_id}."


def test_surface_ids_are_unique_and_not_thinned(probe: Any) -> None:
    """عددُ الأسطحِ لا ينقصُ، ولا يتكرَّرُ معرّفٌ فيُعدَّ سطحٌ مرّتَين."""
    ids = [s.surface_id for s in probe.SURFACES]
    assert len(ids) == len(set(ids)), f"معرّفاتٌ مكرَّرةٌ: {ids}"
    assert (
        len(ids) >= MIN_SURFACES
    ), f"الأسطحُ {len(ids)} وأقلُّ المقبولِ {MIN_SURFACES} — حذفُ سطحٍ ليس إدامةً لحالة."


def test_consequential_surfaces_are_pinned_by_name(probe: Any) -> None:
    """مفتاحُ الإيقافِ والترقياتُ والـcanary والتكلفةُ لا تُسقَطُ بالسكوت."""
    ids = {s.surface_id for s in probe.SURFACES}
    missing = [name for name in PINNED_SURFACES if name not in ids]
    assert not missing, f"أسطحٌ مُثبَّتةٌ حُذِفَت: {missing}"


def test_surfaces_durable_by_owner_decision_are_declared_durable(probe: Any) -> None:
    """ما أمرَ المالكُ بإدامتِه لا يعودُ متطايرًا بصمتٍ (`Q-39 (أ)` · `W-031`)."""
    by_id = {s.surface_id: s for s in probe.SURFACES}
    for name in PINNED_DURABLE_BY_DECISION:
        assert by_id[name].declared == probe.DURABLE, (
            f"السطحُ {name} أُديمَ بقرارٍ سياديٍّ في Q-39 (أ) ثمّ عادَ تصنيفُه "
            f"{by_id[name].declared!r} — تراجعٌ عن قرارٍ لا يملكُه عامل."
        )


def test_control_surfaces_exist(probe: Any) -> None:
    """بلا شاهدِ ضبطٍ دائمٍ يصيرُ «فُقِدَ الكلُّ» دليلًا على كسرِ المِسبار."""
    controls = {s.surface_id for s in probe.SURFACES if s.declared == probe.DURABLE}
    for name in PINNED_CONTROLS:
        assert name in controls, f"شاهدُ الضبطِ {name} مفقودٌ من الأسطح."


def test_expectation_is_derived_from_declaration_not_hand_written(probe: Any) -> None:
    """التوقّعُ يُشتَقُّ من التصنيفِ: المتطايرُ يُفقَدُ، والدائمُ والمؤقّتُ ينجُوان."""
    results = probe.summarize([])
    assert results["surfaces_total"] == 0
    for surface in probe.SURFACES:
        expected = surface.declared in (probe.CACHE_REBUILDABLE, probe.DURABLE)
        assert expected == (surface.declared != probe.VOLATILE)


def test_summary_counts_are_not_cosmetic(probe: Any) -> None:
    """الخلاصةُ تعُدُّ الواقعَ: سطحٌ فُقِدَ يُعَدُّ فقدًا لا «مطابقةً» فحسب."""
    fabricated = [
        probe.Result(
            "a", "s", probe.VOLATILE, "", True, False, False, "MATCHES_DECLARATION"
        ),
        probe.Result(
            "b", "s", probe.DURABLE, "", True, True, True, "MATCHES_DECLARATION"
        ),
        probe.Result(
            "c", "s", probe.DURABLE, "", True, False, True, "CONTRADICTS_DECLARATION"
        ),
        probe.Result("d", "s", probe.VOLATILE, "", False, None, False, "UNMEASURED"),
    ]
    summary = probe.summarize(fabricated)
    assert summary["lost_on_restart"] == 2
    assert summary["survived_restart"] == 1
    assert summary["unmeasured"] == 1
    assert summary["contradicts_declaration"] == 1


# =============================================================================
# 2) المُخرَجُ المُقيَّد
# =============================================================================
def test_measurement_declares_its_purpose(measurement: dict[str, Any]) -> None:
    """المُخرَجُ المُولَّدُ يُعلِنُ هدفَه وحدَّه، فلا يُقرَأُ شهادةَ إدامة."""
    assert "الهدف" in measurement.get("$comment", "")
    assert "Q-39" in measurement.get("note", "")


def test_measurement_covers_every_declared_surface(
    probe: Any, measurement: dict[str, Any]
) -> None:
    """لا سطحَ في الأداةِ غائبٌ عن المُخرَجِ، ولا سطحَ في المُخرَجِ مُختلَقٌ."""
    declared = {s.surface_id for s in probe.SURFACES}
    measured = {s["surface_id"] for s in measurement["surfaces"]}
    assert measured == declared, f"فرقٌ بينَ الأداةِ والمُخرَجِ: {declared ^ measured}"


def test_measurement_has_no_unmeasured_surface(measurement: dict[str, Any]) -> None:
    """سطحٌ لم يُقَسْ ليس نجاةً ولا فقدًا — ولا يُقيَّدُ المُخرَجُ وفيه واحد."""
    assert measurement["summary"]["unmeasured"] == 0
    assert measurement["summary"]["contradicts_declaration"] == 0


def test_controls_survived_in_the_recorded_measurement(
    measurement: dict[str, Any],
) -> None:
    """شاهدا الضبطِ نجَوا فعلًا في القياسِ المُقيَّد — وإلّا فالقياسُ كلُّه باطل."""
    by_id = {s["surface_id"]: s for s in measurement["surfaces"]}
    for name in PINNED_CONTROLS:
        assert (
            by_id[name]["survived"] is True
        ), f"شاهدُ الضبطِ {name} لم ينجُ — المِسبارُ مكسور."


def test_every_declared_volatile_surface_was_measured_lost(
    measurement: dict[str, Any],
) -> None:
    """التصريحُ بالتطايرِ ليس بلاغةً: كلُّ متطايرٍ مُعلَنٍ فُقِدَ بالقياس."""
    volatile = [s for s in measurement["surfaces"] if s["declared"] == "WIRED_VOLATILE"]
    assert volatile, "لا سطحَ متطايرًا في المُخرَجِ — وهذا وحدَه مُريب."
    survivors = [s["surface_id"] for s in volatile if s["survived"] is not False]
    assert not survivors, f"أسطحٌ صُرِّحَ بتطايرِها ونجَت: {survivors}"
    assert measurement["summary"]["lost_on_restart"] == len(volatile)


def test_kill_switch_survives_restart_as_decided(
    measurement: dict[str, Any],
) -> None:
    """الأثرُ الأخطرُ مُقيَّدٌ برقمِه: نظامٌ أُوقِفَ يبقى موقوفًا بعدَ الإقلاع.

    كانَ هذا الحرسُ يُقيِّدُ العكسَ حتّى W-030 (‏`halt` يعودُ `normal`)، فحُسِمَ
    `Q-39 (أ)` بقرارِ المالكِ 2026-08-23 وأُديمَ المفتاحُ في `W-031`. فالقيدُ الآن
    على الوعدِ الجديدِ: **الإقلاعُ لا يرفعُ الإيقافَ**، ورفعُه فعلٌ صريحٌ.
    """
    entry = next(s for s in measurement["surfaces"] if s["surface_id"] == "kill_switch")
    assert entry["extra"]["level_after_write"] == "halt"
    assert (
        entry["extra"]["level_after_restart"] == "halt"
    ), "نظامٌ أُوقِفَ ثمّ أُقلِعَ فعادَ عاملًا — نقضٌ لقرارِ Q-39 (أ) المقيسِ."
    assert entry["survived"] is True
    assert entry["declared"] == "DURABLE_CONTROL"


def test_the_two_cost_sources_are_recorded_as_measured(
    measurement: dict[str, Any],
) -> None:
    """مصدرا التكلفةِ يُقيَّدانِ برقمَيهما لأنَّهما مادّةُ Q-39 لا رأيًا."""
    entry = next(s for s in measurement["surfaces"] if s["surface_id"] == "cost_log")
    extra = entry["extra"]
    for key in (
        "volatile_before",
        "persistent_before",
        "volatile_after",
        "persistent_after",
    ):
        assert isinstance(extra.get(key), int), f"عدَّادُ {key} غيرُ مقيسٍ."
    assert extra["volatile_before"] >= 1, "النداءُ لم يُقيَّدْ في مصدرِ الملخَّصِ."
    # W-033 · حسمُ Q-39 (ج): الملخَّصُ يُعادُ بناؤُه **فوقَ** السجلِّ الدائمِ، فرقمانِ
    # مختلفانِ للمالِ في واجهةٍ واحدةٍ نقضٌ للحسمِ — لا فرقٌ يُشرَحُ في تعليقٍ.
    assert (
        extra["volatile_before"] == extra["persistent_before"]
    ), "مصدرا التكلفةِ يختلفانِ قبلَ الإقلاعِ — رقمانِ للمالِ نقضٌ لـQ-39 (ج)."
    assert (
        extra["volatile_after"] == extra["persistent_after"]
    ), "مصدرا التكلفةِ يختلفانِ بعدَ الإقلاعِ — رقمانِ للمالِ نقضٌ لـQ-39 (ج)."
    assert extra.get("single_number") is True, "المِسبارُ لم يشهَدْ برقمٍ واحدٍ للمال."


# =============================================================================
# 3) قياسٌ حيٌّ لزوجِ الضبطِ — عمليّتانِ لكلِّ سطح
# =============================================================================
def test_live_control_pair_still_behaves_as_recorded(probe: Any) -> None:
    """يُعادُ القياسُ الآنَ لسطحَينِ: متطايرٌ يُفقَدُ ودائمٌ ينجو.

    ولا تُقاسُ الأسطحُ كلُّها هنا: القياسُ الكاملُ دقائقُ، وأمرُه مُعلَنٌ في الدليلِ
    ويُعادُ بأداتِه. والمقصودُ هنا أن يبقى **الفرقُ** مقيسًا في كلِّ تشغيلٍ للحزمة.
    """
    _require_live_stack()
    surfaces = tuple(
        s for s in probe.SURFACES if s.surface_id in ("canary", "kill_switch", "task")
    )
    assert len(surfaces) == 3
    original = probe.SURFACES
    probe.SURFACES = surfaces
    try:
        with tempfile.TemporaryDirectory(prefix="amos_step18_") as tmp:
            results = {r.surface_id: r for r in probe.measure(Path(tmp) / "probe.db")}
    finally:
        probe.SURFACES = original

    _skip_if_the_environment_is_incomplete(results.values())

    assert (
        results["canary"].survived is False
    ), f"الكنارُ نجا خلافًا للتصريحِ: {results['canary'].detail}"
    assert (
        results["kill_switch"].survived is True
    ), f"مفتاحُ الإيقافِ لم ينجُ خلافًا لقرارِ `Q-39 أ`: {results['kill_switch'].detail}"
    assert (
        results["task"].survived is True
    ), f"المهمّةُ الدائمةُ فُقِدَت — فالعجزُ في المِسبارِ: {results['task'].detail}"
    assert all(r.verdict == "MATCHES_DECLARATION" for r in results.values())


def test_the_probe_does_not_pollute_the_measured_tree(probe: Any) -> None:
    """القياسُ لا يُلوِّثُ المقيس: لا أثرَ تشغيلٍ يُكتَبُ في شجرةِ المستودع.

    وسببُ هذا الحرسِ مقيسٌ لا متخيّلٌ (W-030): مرحلةُ الكتابةِ كانت تُنشئُ
    `.runtime/sovereignty/*.json` داخلَ الشجرةِ فتسقطُ **بوّابةُ الهويّةِ** بثلاثِ
    مخالفاتٍ (‏`MISSING_README` + `MISSING_PURPOSE`×2) في حزمةِ الجذرِ كلِّها. فوُجِّهَ
    السجلُّ إلى موضعِ القياسِ المؤقّت، ولم يُضيَّقْ كاشفٌ ولم يُحسَمْ نطاقُ المادةِ
    التاسعةِ بحكمِ عاملٍ — ذاك سؤالٌ مفتوحٌ (`Q-40`).
    """
    _require_live_stack()
    runtime_dir = REPO_ROOT / ".runtime" / "sovereignty"
    existed_before = runtime_dir.exists()
    surfaces = tuple(s for s in probe.SURFACES if s.surface_id == "task")
    original = probe.SURFACES
    probe.SURFACES = surfaces
    try:
        with tempfile.TemporaryDirectory(prefix="amos_step18_clean_") as tmp:
            tmp_root = Path(tmp)
            results = probe.measure(tmp_root / "probe.db")
            _skip_if_the_environment_is_incomplete(results)
            assert (tmp_root / "sovereignty").exists(), (
                "سجلُّ الذرّيّةِ لم يُكتَبْ في موضعِ القياسِ — فالتوجيهُ مُعطَّلٌ "
                "وقد يعودُ التلويثُ إلى الشجرةِ صامتًا."
            )
    finally:
        probe.SURFACES = original

    if not existed_before:
        assert (
            not runtime_dir.exists()
        ), f"القياسُ لوَّثَ الشجرةَ المقيسةَ: {runtime_dir} — وهذا يُسقِطُ بوّابةَ الهويّة."


# =============================================================================
# 4) حرسُ الموضِعِ البديلِ — لا فحصَ يُتخطَّى بلا مكانٍ يُقاسُ فيه
# =============================================================================
def test_live_probe_runs_in_the_measurement_workflow() -> None:
    """ما يُتخطَّى هنا لنقصِ بيئةٍ يُشغَّلُ هناكَ بتبعيّاتٍ كاملةٍ — والوعدُ محروسٌ.

    ولولا هذا الفحصُ لكانَ `_require_live_stack` بابًا لتخطٍّ دائمٍ بلا قياسٍ: يُحذَفُ
    السطرُ من `measure.yml` فلا يسقطُ شيءٌ، فيصيرُ الحرسُ زينةً. فالمكتوبُ هنا
    شرطٌ: اسمُ هذا الملفِّ نصًّا في وظيفةِ القياسِ.
    """
    assert MEASURE_WORKFLOW.exists(), (
        f"وظيفةُ القياسِ غائبةٌ: {MEASURE_WORKFLOW.relative_to(REPO_ROOT)} — "
        "فلا موضِعَ يُقاسُ فيه ما يُتخطَّى في الجذر."
    )
    text = MEASURE_WORKFLOW.read_text(encoding="utf-8")
    assert "tests/governance/test_step18_restart_survival.py" in text, (
        "وظيفةُ القياسِ لا تُشغِّلُ حرسَ الخطوةِ 18 — فالقياسُ الحيُّ صارَ بلا موضِعٍ "
        "في CI، والتخطِّي في الجذرِ يصيرُ إخفاءً."
    )
