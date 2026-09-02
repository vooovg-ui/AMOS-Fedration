"""حرسُ الحرسِ — شرطُ القياسِ الحيِّ يُقاسُ من مُخرَجِ المِسبارِ لا من قائمةٍ بيدٍ.

الهدف:
    منعُ عودةِ **الكذبِ المُوثَّقِ المعكوسِ** الذي أعلنَ حرسُ الخطوةِ 18 أنَّه أُنشِئَ
    لمنعِه ثمَّ وقعَ فيه: أن يُقرأَ **عجزُ بيئةٍ** عجزَ **إدامةِ حالةٍ**. فقد كانَ
    `_require_live_stack` يفحصُ اسمَينِ مكتوبَينِ بيدٍ (`fastapi` · `sqlalchemy`)،
    ومراحلُ المِسبارِ تبلُغُ عبورًا حزمةَ الخدمةِ فتستوردُ `jwt` و`structlog` و
    `pydantic_settings`؛ فبيئةٌ فيها الاسمانِ وليس فيها البقيّةُ كانت **تُقاسُ**
    فتُخرِجُ `UNMEASURED`، ثمَّ تُقرأُ تلك النتيجةُ فقدَ حالةٍ فيُعلَنُ حرفًا: «مفتاحُ
    الإيقافِ لم ينجُ خلافًا لقرارِ Q-39 (أ)» و«سجلُّ الذرّيّةِ لم يُكتَبْ — فالتوجيهُ
    مُعطَّلٌ». والرسالتانِ كاذبتانِ والسببُ وحدةٌ غائبةٌ.

    ويحرسُ هذا الملفُّ **الحدَّ** بقدرِ ما يحرسُ الإصلاحَ: التخطِّي لا يُبتلَعُ به
    إلّا نقصُ **توزيعٍ خارجيٍّ**؛ فوحدةٌ من شجرةِ المستودعِ تبقى حمراءَ، وعجزٌ ليس
    `No module named` يبقى أحمرَ، ومخالفةُ التصريحِ لا تُخفى بهذا البابِ أبدًا.

النطاق:
    الدالّتانِ `_missing_third_party_module` و`_skip_if_the_environment_is_incomplete`
    في `tests/governance/test_step18_restart_survival.py`، واستدعاؤهما في الفحصَينِ
    الحيَّينِ. ولا يُقيسُ هذا الملفُّ إدامةَ سطحٍ ولا صوابَ معمارٍ: ذاك عملُ المِسبارِ
    نفسِه، وهذا يقيسُ **صدقَ نسبةِ السقوطِ إلى سببِه**.

المالك:
    `tests/governance` — حرّاسُ الحوكمةِ في المستودع.

تاريخ الإنشاء: 2026-08-27
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Any

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
GUARD_PATH = REPO_ROOT / "tests" / "governance" / "test_step18_restart_survival.py"
PROBE_PATH = REPO_ROOT / "tools" / "governance" / "restart_survival_probe.py"


def _load(name: str, path: Path) -> Any:
    """حمِّلْ الملفَّ المحروسَ من مسارِه — يُقرأُ الحرسُ الحقيقيُّ لا نسخةٌ منه."""
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, f"تعذَّرَ تحميلُ {path}."
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


guard = _load("step18_guard_under_test", GUARD_PATH)
probe = _load("restart_survival_probe_for_w058", PROBE_PATH)


def _result(verdict: str, detail: str) -> Any:
    """نتيجةٌ مُصطنَعةٌ بحكمٍ ونصِّ عجزٍ — لا تُقلَّدُ بنيةٌ، تُستعملُ بنيةُ المِسبارِ."""
    return probe.Result(
        surface_id="task",
        service="governance",
        declared=probe.DURABLE,
        what_is_lost="—",
        wrote_ok=False,
        survived=None,
        expected_survival=True,
        verdict=verdict,
        detail=detail,
    )


# =============================================================================
# 1) ما يُبتلَعُ: نقصُ توزيعٍ خارجيٍّ وحدَه — ويُسمَّى بالمقيسِ لا بالمفترَضِ
# =============================================================================
def test_a_missing_third_party_distribution_is_named_not_blamed_on_state() -> None:
    """`jwt` غائبةٌ = عجزُ بيئةٍ: يُسمَّى الناقصُ ويُتخطَّى، ولا يُقالُ «فُقِدَت حالةٌ»."""
    missing = guard._missing_third_party_module(
        [_result("UNMEASURED", "ModuleNotFoundError: No module named 'jwt'")]
    )
    assert missing == "jwt", (
        "نقصُ توزيعٍ خارجيٍّ لم يُسمَّ — فسيُقرأُ فقدَ إدامةٍ، وذاك الكذبُ المعكوسُ "
        "الذي أُنشِئَ هذا الحرسُ لمنعِه."
    )


def test_the_named_module_is_read_from_the_probe_output_not_guessed() -> None:
    """الاسمُ المُعلَنُ هو الاسمُ الكاملُ في `detail`، لا اسمًا يُخترَعُ من قائمةٍ."""
    missing = guard._missing_third_party_module(
        [_result("UNMEASURED", "ModuleNotFoundError: No module named 'pydantic_settings'")]
    )
    assert missing == "pydantic_settings"


# =============================================================================
# 2) ما لا يُبتلَعُ — حدُّ الحرسِ محروسٌ في أربعةِ أوجهٍ
# =============================================================================
def test_a_missing_repository_module_stays_red() -> None:
    """وحدةٌ من شجرةِ المستودعِ ناقصةٌ عطبٌ حقيقيٌّ: لا تُتخطَّى ولا تُبرَّرُ ببيئةٍ."""
    missing = guard._missing_third_party_module(
        [
            _result(
                "UNMEASURED",
                "ModuleNotFoundError: No module named 'amos_federation.common.auth'",
            )
        ]
    )
    assert missing is None, (
        "نقصُ شِفرةِ المستودعِ ابتُلِعَ باسمِ نقصِ بيئةٍ — فحذفُ وحدةٍ من حزمةِ الخدمةِ "
        "يمرُّ بصمتٍ، وذاك إخفاءٌ لا تصنيف."
    )


def test_the_repository_module_case_is_not_vacuous() -> None:
    """الفحصُ أعلاه لا يُثبِتُ شيئًا إن لم تكن الحزمةُ في الشجرةِ فعلًا — فيُقاسُ."""
    assert (guard.SERVICES_SRC / "amos_federation").is_dir(), (
        f"حزمةُ الخدمةِ ليست تحتَ {guard.SERVICES_SRC} — ففحصُ «وحدةُ الشجرةِ تبقى "
        "حمراءَ» يمرُّ لأنَّه فارغٌ لا لأنَّه صادق."
    )


def test_an_unmeasured_result_without_a_module_error_stays_red() -> None:
    """عجزٌ آخرُ (مهلةٌ · رمزُ خروجٍ · قاعدةٌ مقفولةٌ) لا يُتخطَّى: لم يُسَمَّ سببُه بيئةً."""
    for detail in (
        "انقضت المهلةُ قبلَ أن تُتِمَّ المرحلةُ",
        "رمزُ الخروجِ 1",
        "sqlite3.OperationalError: database is locked",
        "",
    ):
        assert guard._missing_third_party_module([_result("UNMEASURED", detail)]) is None


def test_a_contradicting_verdict_is_never_swallowed() -> None:
    """مخالفةُ التصريحِ لا تُخفى ولو حملَ نصُّها ما يُشبِهُ عجزَ بيئةٍ — الحكمُ يُقرأُ أوّلًا."""
    for verdict in ("CONTRADICTS_DECLARATION", "MATCHES_DECLARATION"):
        assert (
            guard._missing_third_party_module(
                [_result(verdict, "ModuleNotFoundError: No module named 'jwt'")]
            )
            is None
        ), (
            f"حكمٌ {verdict} ابتُلِعَ بنصِّ عجزٍ بيئيٍّ — فمخالفةُ إدامةٍ حقيقيّةٌ "
            "تُخفى بنصٍّ يُدَسُّ في التفصيل."
        )


def test_the_in_tree_check_is_load_bearing() -> None:
    """طفرةٌ مقصودةٌ: بحذفِ فحصِ الشجرةِ يُبتلَعُ نقصُ شِفرةِ المستودعِ — فالفحصُ يعضُّ.

    ولا يُعدَّلُ الحرسُ ليُثبَتَ ذلك: يُعادُ بناءُ **النسخةِ المُضعَفةِ** هنا بصراحةٍ
    ويُقاسُ فرقُها. فلو رُفِعَ الفحصُ من الحرسِ غدًا لصارَ سلوكُه سلوكَ هذه النسخةِ،
    وهذا الفحصُ يُعلِنُ الفرقَ رقمًا لا رأيًا.
    """
    detail = "ModuleNotFoundError: No module named 'amos_federation.common.auth'"
    weakened = guard._MODULE_NOT_FOUND.search(detail)
    assert weakened is not None
    assert weakened.group(1) == "amos_federation.common.auth", (
        "النسخةُ المُضعَفةُ لا تُنتِجُ اسمًا — فالمقارنةُ لا معنى لها."
    )
    assert guard._missing_third_party_module([_result("UNMEASURED", detail)]) is None, (
        "الحرسُ يُطابِقُ النسخةَ المُضعَفةَ — أي أنَّ فحصَ الشجرةِ لا يعملُ."
    )


# =============================================================================
# 3) الوصلُ: الفحصانِ الحيّانِ يستشيرانِ الشرطَ المقيسَ فعلًا لا اسمًا
# =============================================================================
def test_both_live_tests_consult_the_measured_precondition() -> None:
    """حرسٌ لا يُستدعى زينةٌ: يُقاسُ حضورُ الاستدعاءِ في جسمِ كلِّ فحصٍ حيٍّ."""
    text = GUARD_PATH.read_text(encoding="utf-8")
    for name in (
        "def test_live_control_pair_still_behaves_as_recorded",
        "def test_the_probe_does_not_pollute_the_measured_tree",
    ):
        start = text.index(name)
        end = text.find("\ndef ", start + 1)
        body = text[start : end if end != -1 else len(text)]
        assert "_skip_if_the_environment_is_incomplete(" in body, (
            f"الفحصُ {name} لا يستشيرُ الشرطَ المقيسَ — فعجزُ البيئةِ يعودُ يُقرأُ "
            "عجزَ حالةٍ."
        )


def test_the_hand_written_precondition_is_kept_as_a_cheap_pre_filter() -> None:
    """الشرطُ الرخيصُ لا يُحذَفُ: يوفِّرُ دقائقَ حينَ تغيبُ الطبقةُ كلُّها بإعلانٍ."""
    text = GUARD_PATH.read_text(encoding="utf-8")
    assert "LIVE_STACK_MODULES" in text and "_require_live_stack()" in text


def test_the_service_package_is_not_added_to_the_hand_written_list() -> None:
    """`amos_federation` لا تُوضَعُ في القائمةِ اليدويّةِ — سببٌ مقيسٌ لا ذوقٌ.

    المِسبارُ يحقِنُ `federal/executive/services/src` في `PYTHONPATH` لكلِّ مرحلةٍ
    ولا يضعُه في `sys.path` للعمليّةِ الأمِّ؛ فـ`find_spec("amos_federation")` هنا
    يعودُ `None` **ولو كانَ القياسُ مُستطاعًا تمامًا**. فوضعُها في القائمةِ يُحوِّلُ
    الفحصَينِ إلى متخطَّيَينِ دائمًا في كلِّ بيئةٍ — وحرسٌ يُتخطَّى دائمًا إخفاءٌ.
    """
    assert "amos_federation" not in guard.LIVE_STACK_MODULES
    probe_text = PROBE_PATH.read_text(encoding="utf-8")
    assert "PYTHONPATH" in probe_text and "_SERVICES_SRC" in probe_text, (
        "المِسبارُ لم يبقَ يحقِنُ مسارَ الحزمةِ في بيئةِ المرحلةِ — فسببُ هذا الحدِّ "
        "تغيَّرَ ويلزمُه قياسٌ جديدٌ لا نصٌّ قديمٌ."
    )


def test_the_precondition_reads_the_verdict_not_the_environment() -> None:
    """الشرطُ المقيسُ لا يسألُ البيئةَ: يقرأُ ما أخرجَه المِسبارُ — فلا يتقادَمُ بنموِّها."""
    text = GUARD_PATH.read_text(encoding="utf-8")
    start = text.index("def _missing_third_party_module")
    end = text.index("def _skip_if_the_environment_is_incomplete")
    # الشرحُ يذكرُ `find_spec` ليُعلِّلَ تركَهُ، فيُقاسُ العملُ لا الكلامُ: تُطرحُ
    # وثيقةُ الدالّةِ ثمَّ يُفحَصُ ما يُنفَّذُ منها.
    declaration = text[start:end]
    doc_open = declaration.index('"""')
    doc_close = declaration.index('"""', doc_open + 3) + 3
    code = declaration[:doc_open] + declaration[doc_close:]
    assert '"""' in declaration and "find_spec" in declaration[doc_open:doc_close], (
        "تركُ `find_spec` لم يبقَ مُعلَّلًا في وثيقةِ الدالّةِ — فالقيدُ صارَ عرفًا "
        "لا قرارًا مكتوبًا."
    )
    assert "find_spec" not in code, (
        "الشرطُ المقيسُ صارَ يسألُ البيئةَ — فعادَ إلى القائمةِ اليدويّةِ من بابٍ آخرَ."
    )


# =============================================================================
# 4) الدليلُ الأخيرُ: الفحصانِ الحيّانِ لا يسقُطانِ في هذه البيئةِ — يمرّانِ أو يُتخطَّيانِ
# =============================================================================
def test_the_live_tests_never_report_a_false_failure_here() -> None:
    """قياسٌ لا دعوى: يُشغَّلُ الفحصانِ في عمليّةٍ ويُقرأُ حكمُهما.

    وقبلَ هذا الإصلاحِ كانَ هذا الفحصُ يسقُطُ في بيئةٍ فيها `fastapi` و`sqlalchemy`
    بلا حزمةِ الخدمةِ: `2 failed`. وبعدَه إمّا `2 passed` (بيئةٌ كاملةٌ فالإدامةُ
    مقيسةٌ) أو `2 skipped` (بيئةٌ ناقصةٌ فالعجزُ مُسمًّى) — ولا ثالثَ صادقٌ.
    """
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            str(GUARD_PATH.relative_to(REPO_ROOT)),
            "-q",
            "-p",
            "no:cacheprovider",
            "-k",
            "live_control_pair or pollute",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=900,
        check=False,  # الحكمُ يُقرأُ ويُفسَّرُ هنا، ولا يُرمى استثناءً بلا بيانٍ
    )
    tail = (proc.stdout or "") + (proc.stderr or "")
    assert proc.returncode == 0, (
        "الفحصانِ الحيّانِ يسقُطانِ في هذه البيئةِ — وإن كانَ سببُ السقوطِ وحدةً "
        f"غائبةً فهو الكذبُ المعكوسُ عادَ:\n{tail[-2000:]}"
    )
    assert "failed" not in tail, f"سقوطٌ مُعلَنٌ في المُخرَجِ:\n{tail[-2000:]}"
