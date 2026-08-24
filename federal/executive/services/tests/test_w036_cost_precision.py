"""
AMOS-Federation — إثباتُ توسيعِ دقّةِ الكلفةِ حيًّا (W-036 · Q-42 · الشقُّ الثاني · (أ))
الهدف: أن يُثبَتَ **بالتشغيلِ لا بالتصريحِ** أنَّ كلفةً أصغرَ من `0.00005$` تُقيَّدُ
       بقيمتِها في السجلِّ الدائمِ بعدَ توسيعِ المقياسِ، وأنَّ التوسيعَ **لم يتسرَّبْ**
       إلى سائرِ أعمدةِ المالِ، وأنَّ بابَ الكلفةِ يرفضُ العائمَ ويحرسُ الحدَّ.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-24 (W-036)
تاريخ آخر تعديل: 2026-08-24 (W-036)

## لماذا فحصٌ حيٌّ وقد وُجِدَ الحرسُ الساكنُ في `test_q20_money_representation.py`

لأنَّ الساكنَ يُثبِتُ أنَّ **العقدَ** ثمانِ منازلَ، ولا يُثبِتُ أنَّ **المسارَ** يُوصِلُ
الكسرَ إلى القاعدةِ. وبينَ العقدِ والمسارِ ثلاثُ بوّاباتٍ كلُّ واحدةٍ منها كانت
تُصفِّرُ الكسرَ وحدَها:

1. `ModelLayer.compute_cost` كانت تُقرِّبُ إلى ستِّ منازلَ (`round(cost, 6)`)،
2. `_money_from_provider_float` كانت تُنسِّقُ بأربعِ منازلَ ثمَّ تُمرِّرُها لعقدِ المالِ،
3. وعمودُ `cost_usd` كانَ `NUMERIC(20,4)` في القاعدةِ نفسِها.

فلو أُصلِحَت واحدةٌ وبقيَت أُخرى لكانَ العملُ **دعوى إصلاحٍ**. وهذا الملفُّ يقيسُ
النتيجةَ عندَ المخرجِ: صفٌّ في `model_cost_log` قيمتُه ما دونَ حدِّ الأربعِ منازلَ
وليسَ صفرًا. وهو الأمرُ الذي تُثبِتُ به المادةُ «تمَّ = قدرةٌ مُبرهَنة».

## وما لا يُدَّعى في هذا الملفِّ

لا يُدَّعى أنَّ الكلفةَ صارَت **صحيحةً**. صِحّةُ الكلفةِ مسألةُ الشقِّ الأوّلِ من
Q-42 (افتراقُ جدولَي التسعيرِ) وقد أقرَّ المالكُ الجدولَينِ وقُيِّدَ الفرقُ مقيسًا في
`tools/governance/pricing_divergence.py`. وهذا الملفُّ يُثبِتُ **الدقّةَ** وحدَها:
أنَّ ما يُحسَبُ يُقيَّدُ كما هو. ومن قرأَ نجاحَه شهادةً بصحّةِ التسعيرِ أخطأَ.
"""

from __future__ import annotations

import importlib
import pathlib
from decimal import Decimal
from typing import Any

import pytest
from sqlalchemy import Numeric

from amos_federation.common.money import (
    COST_MAX,
    COST_SCALE,
    MONEY_SCALE,
    CostMoneyType,
    MoneyError,
    MoneyType,
    to_cost,
    to_money,
)

model_gateway_main = importlib.import_module("amos_federation.services.model_gateway.main")
model_layer_module = importlib.import_module("amos_federation.services.model_gateway.model_layer")

#: كلفةٌ أصغرُ من نصفِ أصغرِ وحدةٍ في عقدِ المالِ القديمِ (`0.00005$`) — أي ما كانَ
#: يُقيَّدُ صفرًا حتمًا. ومصدرُها ليسَ اختراعًا: أرخصُ رمزٍ في `ModelLayer.PRICING`
#: هو `claude-haiku-3.5` بمُدخَلٍ `0.0008$/1k` أي `8e-7$` للرمزِ الواحد.
SUB_SCALE_COST = 0.0000008


@pytest.fixture()
def layer() -> Any:
    """طبقةُ النماذجِ الحقيقيّةُ لا مُحاكاةٌ — والقيدُ يُقرأُ من القاعدةِ نفسِها."""
    return model_layer_module.get_model_layer()


# =============================================================================
# 1) العيبُ مقيسًا قبلَ الإصلاحِ — كي لا يكونَ الإصلاحُ إصلاحًا لِما ليسَ عيبًا
# =============================================================================
def test_01_the_old_contract_did_swallow_the_fraction() -> None:
    """العقدُ القديمُ (`NUMERIC(20,4)`) يُصفِّرُ `8e-7$` فعلًا — هذا هو موضوعُ Q-42.

    ويُقاسُ العقدُ القديمُ بذاتِه لا بذكرى: `to_money` باقيةٌ كما هي بحسمِ Q-20،
    فتُستدعى مباشرةً. فلو لم يُصفِّرْ لسقطَ هذا الفحصُ وعُلِمَ أنَّ Q-42 كانَ عن
    عيبٍ لا وجودَ له — وذلكَ أشدُّ ما يُخشى على سجلِّ قرارٍ.
    """
    assert to_money(f"{SUB_SCALE_COST:.4f}") == Decimal(
        "0.0000"
    ), "عقدُ المالِ القديمُ لا يُصفِّرُ الكسرَ — فلا موضوعَ لِـQ-42 · الشقِّ الثاني"
    assert (
        round(SUB_SCALE_COST, 6) == 0.000001 or round(SUB_SCALE_COST, 6) == 0.0
    ), "قياسُ التقريبِ القديمِ (ستُّ منازلَ) لم يُعطِ ما هو مُتوقَّعٌ حسابًا"
    # وبعدَ التوسيعِ: القيمةُ نفسُها تُحفَظُ لا تُبلَعُ.
    assert to_cost(f"{SUB_SCALE_COST:.{COST_SCALE}f}") == Decimal("0.0000008")


# =============================================================================
# 2) الإثباتُ الحيُّ: قيدٌ في القاعدةِ لا صفرٌ
# =============================================================================
def test_02_a_sub_scale_cost_is_now_recorded_as_itself_not_zero(layer: Any) -> None:
    """قيدٌ حقيقيٌّ في `model_cost_log` بكلفةِ `8e-7$` يُقرأُ غيرَ صفرٍ.

    هذا هو **الأمرُ المُعادُ تشغيلُه** الذي يجعلُ W-036 «تمَّ» لا «قيلَ».
    """
    invocation = "inv-w036-sub-scale"
    layer.log_cost(
        invocation_id=invocation,
        model="claude-haiku-3.5",
        tokens=1,
        cost_usd=SUB_SCALE_COST,
        latency_ms=1,
        source="local_fallback",
    )
    row = next(r for r in layer.cost_rows() if r["invocation_id"] == invocation)
    assert row["cost_usd"] > 0, (
        "كلفةٌ موجبةٌ قُيِّدَت صفرًا بعدَ توسيعِ المقياسِ — فإحدى البوّاباتِ الثلاثِ "
        "لا تزالُ تُقرِّبُ إلى أربعٍ أو ستٍّ"
    )
    assert row["cost_usd"] == pytest.approx(
        SUB_SCALE_COST, rel=1e-9
    ), "القيمةُ المقيَّدةُ ليست القيمةَ المُرسَلةَ — فالتوسيعُ نقلَ العيبَ ولم يرفعْه"


def test_03_the_computation_path_no_longer_rounds_the_fraction_away(layer: Any) -> None:
    """`compute_cost` تُبقي الكسرَ: رمزٌ واحدٌ بسعرِ الهايكو لا يُحسَبُ صفرًا.

    وهذا يُثبِتُ البوّابةَ الأولى وحدَها (الحسابَ) بمعزلٍ عن القاعدةِ — فإن سقطَ
    هذا ونجحَ ما قبلَه عُرِفَ **أيُّ** بوّابةٍ رجعَت، لا أنَّ «شيئًا ما» رجعَ.
    """
    cost = layer.compute_cost("claude-haiku-3.5", input_tokens=1, output_tokens=0)
    assert cost > 0, "حسابُ كلفةِ رمزٍ واحدٍ بسعرٍ مُعلَنٍ أعطى صفرًا — التقريبُ رجعَ"
    assert cost == pytest.approx(0.0000008, rel=1e-9)


def test_04_the_provider_gate_carries_eight_places_end_to_end() -> None:
    """`_money_from_provider_float` تُمرِّرُ ثمانَ منازلَ لا أربعًا.

    والاسمُ لم يُبدَّلْ عن قصدٍ: حرسٌ قائمٌ في `test_w033_cost_record_durability.py`
    ينادي هذه الدالّةَ **باسمِها**، وتغييرُ الاسمِ يُسقِطُ حرسًا لا يُصلِحُ عيبًا.
    """
    convert = model_layer_module._money_from_provider_float
    value = convert(SUB_SCALE_COST)
    assert isinstance(value, Decimal), "بابُ المزوّدِ يُعيدُ عائمًا — وهذا أصلُ العيبِ"
    assert (
        value.as_tuple().exponent == -COST_SCALE
    ), f"الأُسُّ {value.as_tuple().exponent} لا -{COST_SCALE}"
    assert value == Decimal("0.0000008")


# =============================================================================
# 3) التوسيعُ لم يتسرَّبْ: «أعمدةَ الكلفةِ وحدَها»
# =============================================================================
def test_05_the_cost_column_is_the_only_widened_column_in_the_gateway() -> None:
    """في بوّابةِ النماذجِ عمودُ الكلفةِ وحدَه `CostMoneyType`، وما عداهُ لم يُمَسَّ."""
    table = model_layer_module.CostLogModel.__table__
    cost = table.c["cost_usd"]
    assert isinstance(cost.type, CostMoneyType), "عمودُ الكلفةِ لم يُوسَّعْ — Q-42 (أ) غيرُ مُنفَّذٍ"
    impl = cost.type.impl
    assert isinstance(impl, Numeric)
    assert impl.scale == COST_SCALE and impl.precision == 20

    for name, column in table.c.items():
        if name == "cost_usd":
            continue
        assert not isinstance(
            column.type, CostMoneyType
        ), f"العمودُ {name} صارَ عمودَ كلفةٍ بلا قرارٍ — والحسمُ خصَّ `cost_usd`"


def test_06_the_general_money_contract_did_not_move() -> None:
    """عقدُ المالِ العامُّ باقٍ على أربعِ منازلَ — فالاستثناءُ استثناءٌ لا عقدٌ جديدٌ."""
    assert MONEY_SCALE == 4, "مقياسُ المالِ العامُّ تغيَّرَ — وهذا نقضٌ لِـQ-20 لا تنفيذٌ لِـQ-42"
    assert COST_SCALE > MONEY_SCALE, "لا توسيعَ وقعَ"
    assert not issubclass(
        CostMoneyType, MoneyType
    ), "نوعُ الكلفةِ يُوَرَّثُ من نوعِ المالِ — فحرسُ Q-20 يقبلُه ويُقرأُ المقياسانِ واحدًا"
    assert str(to_money("7.77")) == "7.7700", "تمثيلُ المالِ العامِّ تبدَّلَ"


# =============================================================================
# 4) بابُ الكلفةِ يحرسُ ما يحرسُه بابُ المالِ — لا أقلَّ
# =============================================================================
def test_07_the_cost_gate_refuses_float_like_the_money_gate() -> None:
    """العائمُ مرفوضٌ عندَ البابِ: من قبِلَ `float` أدخلَ الخطأَ الذي جاءَ يمنعُه."""
    with pytest.raises(MoneyError):
        to_cost(1.5)  # type: ignore[arg-type]
    with pytest.raises(MoneyError):
        to_cost(0.0000008)  # type: ignore[arg-type]
    assert to_cost("1.5") == Decimal("1.50000000")
    assert to_cost(Decimal("2")) == Decimal("2.00000000")


def test_08_the_cost_gate_enforces_the_narrowed_ceiling() -> None:
    """الحدُّ الأعلى ضاقَ إلى `9e7$` وهو **مُنفَّذٌ** لا مُعلَنٌ فقط.

    والضيقُ ثمنٌ مقيسٌ: دقّةُ SQLite مضمونةٌ ما دامَ `MAX × 10^SCALE < 2⁵³`. فمن
    رفعَ الحدَّ دونَ أن يُنقِصَ المقياسَ أدخلَ فقدًا صامتًا في المالِ.
    """
    assert Decimal("90000000") == COST_MAX
    assert COST_MAX * (10**COST_SCALE) < 2**53, "الحدُّ يتجاوزُ مدى التمثيلِ الدقيقِ"
    assert to_cost(str(COST_MAX)) == COST_MAX, "الحدُّ نفسُه مرفوضٌ — فالقيدُ أضيقُ ممّا أُعلِنَ"
    with pytest.raises(MoneyError):
        to_cost(str(COST_MAX + 1))


def test_09_the_gate_mirrors_the_money_gate_and_the_column_carries_the_sign_guard() -> None:
    """أينَ يُمنَعُ السالبُ — مقيسًا لا مفترضًا.

    ## عيبٌ في فحصٍ كتبتُه، ظهرَ بالتشغيلِ فيُقيَّدُ

    كتبتُ أوّلًا أنَّ `to_cost("-0.00000001")` يجبُ أن يرفعَ خطأً، فلم يرفعْ. وقياسُ
    البابِ الأصلِ أظهرَ العلّةَ: **`to_money("-1")` يقبلُ السالبَ أيضًا**. فبابُ
    التحويلِ في هذا المستودعِ يحرسُ **التمثيلَ والمدى** لا **الإشارةَ**، والإشارةُ
    تُحرَسُ حيثُ يُحرَسُ المعنى: في قيدِ العمودِ (`cost_check`) وفي
    `positive_money_check` لمن أرادَها.

    ولم يُزَدْ منعُ السالبِ في البابِ: حسمُ Q-42 (أ) توسيعُ دقّةٍ، ومن أضافَ قيدَ
    إشارةٍ في بابِ التحويلِ باسمِه غيَّرَ عقدًا لم يُؤذَنْ له فيه — وقد يكسرُ نداءً
    قائمًا بردٍّ سالبٍ من مزوّدٍ فيُخفي الشُذوذَ بدلَ أن يُقيَّدَ.
    """
    assert to_cost("-1") == Decimal("-1.00000000"), "بابُ الكلفةِ صارَ يرفضُ السالبَ بلا قرارٍ"
    assert to_money("-1") == Decimal("-1.0000"), "بابُ المالِ تبدَّلَ — والمقارنةُ سقطَت"

    # والصفرُ مقبولٌ بقصدٍ: نداءٌ محليٌّ سعرُه صفرٌ مُعلَنٌ، ومنعُه يمنعُ قيدَ واقعٍ.
    assert to_cost("0") == 0

    # والإشارةُ محروسةٌ في العمودِ — والقيدُ في الهجرةِ **هو** ما يُولِّدُه العقدُ
    # لا نسخةٌ مكتوبةٌ بيدٍ قد تفترقُ عنه (سابقةُ `_W032_ADDED_COLUMNS`).
    from amos_federation.common.money import cost_check

    generated = " ".join(cost_check("cost_usd").split())
    migration = (
        pathlib.Path(__file__).resolve().parents[1] / "migrations" / "016_widen_cost_precision.sql"
    ).read_text(encoding="utf-8")
    assert generated in " ".join(migration.split()), (
        f"قيدُ الهجرةِ يُخالفُ ما يُولِّدُه العقدُ «{generated}» — "
        "فإمّا القاعدةُ أوسعُ من العقدِ أو أضيقُ منه، وكلاهُما فقدٌ صامتٌ"
    )
    assert "cost_usd >= 0" in generated, "قيدُ العمودِ لا يمنعُ السالبَ — فلا حرسَ للإشارةِ أصلًا"


def test_10_the_read_path_publishes_a_sub_scale_cost_without_rounding_it(
    layer: Any,
) -> None:
    """واجهتانِ منشورتانِ لا تقولانِ رقمَينِ لمالٍ واحدٍ — حتّى تحتَ `1e-6`.

    **وهذا الفحصُ وُلِدَ من عيبٍ حقيقيٍّ ظهرَ بالقياسِ داخلَ `W-036` نفسِه**: بعدَ
    توسيعِ العقدِ والهجرةِ ومسارِ الحسابِ بقيَت **بوّابةٌ رابعةٌ** في `مسارِ
    القراءةِ` — `ModelLayer.get_cost_summary` كانت تُقرِّبُ إلى **ستِّ** منازلَ،
    فيُخزَّنُ `8e-07` صحيحًا ثمَّ تُنشِرُه الواجهةُ `1e-06`. فكانَ
    `/v1/cost/summary` يقولُ رقمًا و`/v1/models/cost-summary` رقمًا آخرَ **لمالِ
    الدولةِ نفسِه** — نقضٌ لحسمِ Q-39 (ج) لا يراهُ مُراجِعٌ لأنَّ الصفَّ سليمٌ.

    فلا يكفي أن يُصلَحَ الموضعُ؛ يلزمُ حرسٌ يُسقِطُ من أعادَه.
    """
    before = layer.get_cost_summary()["total_cost_usd"]
    layer.log_cost(
        invocation_id="inv-w036-read-path",
        model="claude-haiku-3.5",
        tokens=1,
        cost_usd=SUB_SCALE_COST,
        latency_ms=1,
        source="local_fallback",
    )
    after = layer.get_cost_summary()["total_cost_usd"]
    delta = after - before
    assert delta > 0, "قيدٌ موجبٌ لم يُحرِّكِ المنشورَ قِيدَ أنملةٍ — مسارُ القراءةِ يُبلِعُه."
    assert delta == pytest.approx(float(SUB_SCALE_COST), rel=1e-6), (
        "مسارُ القراءةِ يُقرِّبُ ما خُزِّنَ صحيحًا — بوّابةٌ رابعةٌ عادَت، "
        f"فالزيادةُ المنشورةُ {delta!r} لا {float(SUB_SCALE_COST)!r}."
    )


def test_11_the_read_path_rounding_is_derived_from_the_cost_scale() -> None:
    """التقريبُ في مسارِ القراءةِ مشتقٌّ من `COST_SCALE` لا رقمًا مكتوبًا.

    الفحصُ الذي قبلَه يمنعُ العيبَ عندَ قيمةٍ واحدةٍ؛ وهذا يمنعُ عودةَ **سببِه**:
    رقمٌ منسوخٌ بيدٍ في مسارِ القراءةِ يُخالِفُ المقياسَ المُعلَنَ. فإن وُسِّعَ
    المقياسُ يومًا ولم يُوسَّعِ النشرُ، احمرَّ هذا.
    """
    source = pathlib.Path(model_layer_module.__file__).read_text(encoding="utf-8").splitlines()
    summary_body = [line for line in source if "total_cost_usd" in line and "round(" in line]
    assert summary_body, "لم يُوجَدْ سطرُ نشرِ الكلفةِ الكلّيّةِ — بُدِّلَ الشكلُ بلا قيدٍ."
    for line in summary_body:
        assert "COST_SCALE" in line, (
            "مسارُ القراءةِ يُقرِّبُ برقمٍ مكتوبٍ لا بالمقياسِ المُعلَنِ: " f"{line.strip()!r}"
        )
