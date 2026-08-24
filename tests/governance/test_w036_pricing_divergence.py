"""
AMOS-Federation — حرسُ قياسِ افتراقِ التسعيرِ (W-036 · Q-42 · الشقُّ الأوّلُ · (ج))
الهدف: أن يبقى الفرقُ بينَ جدولَي التسعيرِ **مقيَّدًا لا مكتومًا** بعدَ أن أقرَّ
       المالكُ الجدولَينِ، وأن تبقى أداةُ القياسِ **قائسةً لا مُصلِحةً**، وأن
       تسقطَ البوّابةُ إن انحرفَ جدولٌ عن قياسِه المنشورِ.
النطاق: tests/governance
المالك: الجذر (حكمُ المستودعِ)
تاريخ الإنشاء: 2026-08-24 (W-036)
تاريخ آخر تعديل: 2026-08-24 (W-036)

## لماذا يُحرَسُ افتراقٌ **أُقِرَّ**

حسمَ المالكُ في Q-42 · الشقِّ الأوّلِ · (ج): «يُقَرُّ الجدولانِ ويُقيَّدُ الفرقُ».
والإقرارُ لا يُغني عن الحرسِ بل يُوجِبُه: جدولانِ مُقَرّانِ بلا قياسٍ منشورٍ يصيرانِ
بعدَ حينٍ جدولَينِ **مجهولَي الفرقِ**، فيُعدَّلُ أحدُهما ولا يشعرُ أحدٌ. فالقياسُ
هو ثمنُ الإقرارِ، وهذا الملفُّ هو الذي يجعلُ الثمنَ مدفوعًا لا موعودًا.

## وما لا يفعلُه هذا الملفُّ

لا يشترطُ توحيدَ الجدولَينِ، ولا يشترطُ سعرًا بعينِه، ولا يُصحِّحُ سعرًا. من قرأَ
سقوطَه دعوةً للتوحيدِ خالفَ نصَّ الحسمِ؛ وسقوطُه يعني شيئًا واحدًا: **الجدولُ
تغيَّرَ ولم يُعَدْ توليدُ قياسِه**.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[2]
TOOL = REPO / "tools" / "governance" / "pricing_divergence.py"
MEASUREMENT = REPO / "docs" / "audit" / "measurements" / "pricing_divergence.json"
CALL_PATH_SOURCE = (
    REPO
    / "federal/executive/services/src/amos_federation/services/model_gateway/main.py"
)
LAYER_SOURCE = (
    REPO
    / "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py"
)


def _load_tool() -> Any:
    """حمِّلِ الأداةَ وحدَها بلا حزمةٍ — كما تُشغَّلُ في البوّابةِ نفسِها."""
    spec = importlib.util.spec_from_file_location("pricing_divergence_under_test", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def tool() -> Any:
    return _load_tool()


@pytest.fixture(scope="module")
def measured(tool: Any) -> dict[str, Any]:
    """قياسٌ طازجٌ من المصدرِ الحيِّ — لا من الملفِّ المنشورِ."""
    return tool.measure(REPO)


# =============================================================================
# 1) الجدولانِ قائمانِ — فالقياسُ عن شيءٍ موجودٍ
# =============================================================================
def test_01_both_pricing_tables_still_exist_where_the_measurement_says() -> None:
    """الجدولانِ في موضعَيهِما المُعلَنَينِ — فلو نُقِلَ أحدُهما سقطَ القياسُ لا صمتَ."""
    assert CALL_PATH_SOURCE.is_file(), "ملفُّ مسارِ النداءِ غائبٌ"
    assert LAYER_SOURCE.is_file(), "ملفُّ طبقةِ النماذجِ غائبٌ"
    assert "COST_PER_1K_TOKENS" in CALL_PATH_SOURCE.read_text(encoding="utf-8"), (
        "جدولُ تسعيرِ مسارِ النداءِ اختفى — وهذا إمّا توحيدٌ لم يُقيَّدْ أو حذفٌ صامتٌ"
    )
    assert "PRICING" in LAYER_SOURCE.read_text(encoding="utf-8"), "جدولُ تسعيرِ الطبقةِ اختفى"


def test_02_the_tool_reads_the_tables_without_importing_the_service(tool: Any) -> None:
    """الأداةُ تقرأُ الشِفرةَ نصًّا (`ast`) ولا تستوردُ الخدمةَ — فلا آثارَ جانبيّةَ.

    ولو استوردَت `main.py` لأنشأَت تطبيقًا وفتحَت قاعدةً في أداةِ حكمٍ، فصارَ
    القياسُ يُغيِّرُ ما يقيسُه.
    """
    source = TOOL.read_text(encoding="utf-8")
    assert "import ast" in source, "الأداةُ لا تقرأُ بـ`ast` — فهي إمّا تستوردُ أو تُخمِّنُ"
    for forbidden in ("import amos_federation", "from amos_federation"):
        assert forbidden not in source, (
            f"الأداةُ تستوردُ الخدمةَ («{forbidden}») — وأداةُ الحكمِ لا تُشغِّلُ ما تحكمُ عليه"
        )


# =============================================================================
# 2) الفرقُ مُثبَّتٌ بأوجهِه الثلاثةِ — كما قِيسَ يومَ الحسمِ
# =============================================================================
def test_03_the_shape_divergence_is_pinned(measured: dict[str, Any]) -> None:
    """وجهٌ أوّلُ: مسطَّحٌ واحدٌ مقابلَ دَخلٍ وخَرْجٍ منفصلَين."""
    assert measured["summary"]["shape_divergence"] == "flat_single_rate_vs_split_input_output"


def test_04_the_rate_divergence_is_pinned_as_measured_on_the_day_of_the_ruling(
    measured: dict[str, Any],
) -> None:
    """وجهٌ ثانٍ: في كلِّ نموذجٍ مشتركٍ المسطَّحُ = الخَرْجُ = خمسةُ أضعافِ الدَخلِ.

    وهذا يعني أنَّ رموزَ الدَخلِ **تُحمَّلُ زائدًا** في مسارِ النداءِ — أي انحيازٌ
    إلى **الأعلى**، فلا يُخفي إنفاقًا. وهو مُقَرٌّ بنصِّ المالكِ لا مُصلَحٌ هنا.
    """
    s = measured["summary"]
    shared = s["models_shared"]
    assert shared, "لا نموذجَ مشتركٌ — فالجدولانِ افترقا كُلِّيًّا وهذا تغيُّرٌ لم يُقيَّدْ"
    assert sorted(s["shared_models_where_flat_equals_layer_output"]) == sorted(shared), (
        "لم يبقَ المسطَّحُ مساويًا لسعرِ الخَرْجِ في كلِّ نموذجٍ مشتركٍ — "
        "تغيَّرَ أحدُ الجدولَينِ ولم يُعَدْ توليدُ القياسِ"
    )
    for model, d in measured["rate_divergence"].items():
        if d["layer_input_per_1k"] and d["flat_per_1k"]:
            assert d["flat_over_layer_input"] == pytest.approx(5.0), (
                f"نسبةُ المسطَّحِ إلى الدَخلِ في {model} صارَت "
                f"{d['flat_over_layer_input']} لا 5 — وهذا فرقٌ ماليٌّ غيرُ مقيَّدٍ"
            )


def test_05_the_coverage_gap_that_understates_money_is_named_not_summarised(
    measured: dict[str, Any],
) -> None:
    """وجهٌ ثالثٌ — وهو الوحيدُ الذي يُنقِصُ مالَ الدولةِ فيُسمّى باسمِه.

    نموذجٌ مُسعَّرٌ بمالٍ حقيقيٍّ في الطبقةِ وغائبٌ عن جدولِ مسارِ النداءِ يُقرأُ
    `.get(model, 0.0)` فيُقيَّدُ **مجّانًا**. وهذا باقٍ **غيرَ مُصلَحٍ** عن قصدٍ:
    إضافةُ سعرٍ إلى جدولٍ قرارُ مالٍ لا حكمُ عاملٍ، والمالكُ أقرَّ الجدولَينِ كما
    هما. فيُقيَّدُ الأثرُ باسمِه كي لا يُقرأَ الإقرارُ نسيانًا.
    """
    named = measured["summary"]["priced_in_layer_free_in_call_path"]
    assert named == ["claude-haiku-3.5"], (
        f"قائمةُ «مُسعَّرٌ في الطبقةِ ومجّانٌ في مسارِ النداءِ» صارَت {named} — "
        "فإمّا سُدَّت الثغرةُ (فليُقيَّدْ ذلكَ قرارًا) أو اتّسعَت (فذلكَ نقصٌ جديدٌ في المال)"
    )


def test_06_the_smallest_rate_is_the_one_that_justified_eight_places(
    measured: dict[str, Any],
) -> None:
    """أصغرُ سعرٍ غيرِ صفريٍّ هو سَنَدُ اختيارِ ثمانِ منازلَ — لا رقمٌ مُستحسَنٌ.

    `0.0008$/1k` أي `8e-7$` للرمزِ: يلزمُه سبعُ منازلَ ليُمثَّلَ، فثمانٌ هي أوّلُ
    مقياسٍ يُمثِّلُه **ومعَه هامشُ رمزٍ واحدٍ**. فإن هبطَ أرخصُ سعرٍ يومًا سقطَ هذا
    الفحصُ ولزمَ إعادةُ النظرِ في المقياسِ — لا أن يُبلَعَ الكسرُ صامتًا.
    """
    per_token = measured["summary"]["smallest_nonzero_rate_per_token"]
    assert per_token == pytest.approx(8e-7), f"أصغرُ سعرٍ للرمزِ صارَ {per_token} لا 8e-7"

    from decimal import Decimal

    sys.path.insert(0, str(REPO / "federal/executive/services/src"))
    from amos_federation.common.money import COST_SCALE  # noqa: PLC0415

    assert Decimal(str(per_token)).quantize(Decimal(1).scaleb(-COST_SCALE)) > 0, (
        f"أرخصُ سعرٍ لا يزالُ يُصفَّرُ بمقياسِ {COST_SCALE} — فالمقياسُ لا يكفي"
    )


# =============================================================================
# 3) البوّابةُ تحكمُ ولا تكتبُ ما تحكمُ عليه
# =============================================================================
def test_07_the_published_measurement_is_fresh(tool: Any, measured: dict[str, Any]) -> None:
    """القياسُ المنشورُ يُطابِقُ المصدرَ الحيَّ — وهذا هو ما تفحصُه البوّابةُ في CI."""
    assert MEASUREMENT.is_file(), "القياسُ المنشورُ غائبٌ — فالفرقُ مُقَرٌّ وغيرُ مقيَّدٍ"
    ok, message = tool.check_published_is_fresh(REPO, measured)
    assert ok, f"القياسُ المنشورُ بائتٌ: {message} — أعِدْ توليدَه بـ`pricing_divergence.py .`"


def test_08_the_check_flag_does_not_write_what_it_judges(tool: Any) -> None:
    """البوّابةُ لا تُصلِحُ ما تحكمُ عليه — وإلّا لم تسقطْ أبدًا.

    وهذا هو العيبُ الذي وقعَ في أداةٍ سابقةٍ فصارَ `--check` ينجحُ دائمًا لأنَّه
    يكتبُ الجوابَ ثمَّ يقارنُه بنفسِه. فيُقاسُ هنا **زمنُ التعديلِ وبَصمةُ النصِّ**.
    """
    before_text = MEASUREMENT.read_text(encoding="utf-8")
    before_mtime = MEASUREMENT.stat().st_mtime_ns

    exit_code = tool.main(["pricing_divergence.py", str(REPO), "--check"])

    assert exit_code == 0, "البوّابةُ سقطَت على قياسٍ طازجٍ"
    assert MEASUREMENT.read_text(encoding="utf-8") == before_text, (
        "`--check` عدَّلَ القياسَ المنشورَ — فالبوّابةُ تكتبُ الجوابَ الذي تُصحِّحُه"
    )
    assert MEASUREMENT.stat().st_mtime_ns == before_mtime, (
        "`--check` أعادَ كتابةَ الملفِّ بنفسِ النصِّ — والكتابةُ في وضعِ الحكمِ لا تجوزُ أصلًا"
    )


def test_09_the_gate_fails_when_a_pricing_table_drifts(tool: Any, tmp_path: Path) -> None:
    """حرسُ الحرسِ: لو تغيَّرَ سعرٌ ولم يُعَدْ توليدُ القياسِ **يجبُ** أن تسقطَ البوّابةُ.

    ويُقاسُ ذلكَ على نسخةٍ في `tmp_path` لا على المستودعِ نفسِه — فأداةُ حكمٍ
    تُجرَّبُ بتعديلِ المصدرِ الحقيقيِّ قد تتركُ أثرَها فيه إن سقطَ الفحصُ في منتصفِه.
    """
    import shutil

    for rel in (
        "docs/audit/measurements/pricing_divergence.json",
        "federal/executive/services/src/amos_federation/services/model_gateway/main.py",
        "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py",
    ):
        dest = tmp_path / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / rel, dest)

    # البوّابةُ راضيةٌ قبلَ الانحرافِ — وإلّا لم يكن السقوطُ التاليُّ دليلًا.
    assert tool.main(["t", str(tmp_path), "--check"]) == 0, "النسخةُ غيرُ صالحةٍ للقياسِ ابتداءً"

    layer = tmp_path / (
        "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py"
    )
    text = layer.read_text(encoding="utf-8")
    assert '"output": 0.075' in text, "شكلُ جدولِ الطبقةِ تغيَّرَ — فمحاكاةُ الانحرافِ لم تُطبَّقْ"
    layer.write_text(text.replace('"output": 0.075', '"output": 0.999', 1), encoding="utf-8")

    assert tool.main(["t", str(tmp_path), "--check"]) == 1, (
        "سعرٌ تغيَّرَ والبوّابةُ راضيةٌ — فالحرسُ صوريٌّ والفرقُ يعودُ مكتومًا"
    )


def test_10_the_measurement_declares_its_authority_and_its_generator() -> None:
    """المُخرَجُ المُولَّدُ يُعلِنُ مُولِّدَه وسَنَدَه — المادةُ التاسعةُ · 2."""
    payload = json.loads(MEASUREMENT.read_text(encoding="utf-8"))
    assert "pricing_divergence.py" in payload["$comment"], "قياسٌ لا يُعلِنُ مُولِّدَه يُحرَّرُ بيدٍ"
    assert "Q-42" in payload["authority"], "قياسٌ بلا سَنَدٍ في قرارٍ مُقيَّدٍ"
    assert "قياسٌ لا حُكم" in payload["note"], "القياسُ لا يُعلِنُ أنَّه ليسَ حكمًا"


def test_11_the_measurement_carries_no_machine_local_path() -> None:
    """لا مسارَ آلةٍ في مُخرَجٍ مُشتَرَكٍ — وإلّا صارَ القياسُ يختلفُ بينَ آلةٍ وأُخرى.

    وهذا درسٌ مدفوعُ الثمنِ من `W-035`: حقلٌ يحملُ جِذرَ المستودعِ جعلَ ملفًّا
    مُولَّدًا يتغيَّرُ بتغيُّرِ الآلةِ، فصارَت البوّابةُ تسقطُ في CI بلا سببٍ حقيقيٍّ.
    """
    text = MEASUREMENT.read_text(encoding="utf-8")
    for leak in ("/home/", "/Users/", "C:\\\\", str(REPO)):
        assert leak not in text, f"القياسُ يحملُ مسارَ آلةٍ «{leak}» — فهو غيرُ قابلٍ للمقارنةِ"


def test_12_the_tool_runs_as_a_command_not_only_as_an_import() -> None:
    """أمرٌ يُعادُ تشغيلُه — وهذا شرطُ «تمَّ = قدرةٌ مُبرهَنة» لا التوثيقُ وحدَه."""
    result = subprocess.run(  # noqa: S603
        [sys.executable, str(TOOL), str(REPO), "--check"],
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )
    assert result.returncode == 0, f"الأمرُ سقطَ:\n{result.stdout}\n{result.stderr}"
    assert "PRICING DIVERGENCE" in result.stdout, "الأمرُ لا يُعلِنُ حكمَه على المُخرَجِ القياسيِّ"
