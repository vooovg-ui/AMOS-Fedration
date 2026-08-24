"""
AMOS-Federation — اختبارُ توحيدِ تمثيلِ المبلغ (Q-20)
الهدف: أن يُثبَّتَ قرارُ Q-20 بحيث لا يُنتقَضَ صمتًا: كلُّ عمودٍ ماليٍّ يملكُه
       هذا المستودعُ تمثيلُه `NUMERIC(20,4)` عبرَ `MoneyType`، والهجرةُ 014
       تُعلِنُ التحويلَ نصًّا صريحًا، والمستثنياتُ مستثناةٌ بعلّةٍ لا بسهو.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-20 (Q-20)
تاريخ آخر تعديل: 2026-08-24 (Q-42 · (أ) · W-036 — أعمدةُ الكلفةِ صارَ لها مقياسٌ
             مُعلَنٌ خاصٌّ بحسمِ المالكِ، فنُقِلَت إلى حرسٍ خاصٍّ بها **ولم تُحذَفْ
             من الحراسةِ**، ويُثبِتُ ذلكَ `test_10`)

## لماذا اختبارٌ ساكنٌ لا حيٌّ فقط

لأنَّ الانتقاضَ المُحتمَلَ ليس خطأً في التشغيلِ بل **رجوعٌ في التصريح**: أن
يكتبَ آتٍ `Column(String)` لمبلغٍ جديدٍ فيمرَّ لأنَّ كلَّ الاختباراتِ الحيّةِ
تنجح. فالحرسُ هنا يقرأُ التصريحَ نفسَه: أنواعَ الأعمدةِ في `metadata`، ونصَّ
الهجرةِ على القرص. ومن أرادَ نقضَ Q-20 فعليه أن يُسقِطَ هذا الملفَّ صراحةً،
وذلك أثرٌ يُرى في المُراجعةِ لا يمرُّ في الظلّ.
"""

from __future__ import annotations

import re
from decimal import Decimal
from pathlib import Path

import pytest
from sqlalchemy import Numeric

from amos_federation.common.money import (
    COST_MAX,
    COST_SCALE,
    MONEY_MAX,
    MONEY_SCALE,
    CostMoneyType,
    MoneyType,
    to_cost,
    to_money,
)

MIGRATION = (
    Path(__file__).resolve().parents[1] / "migrations" / "014_unify_money_representation.sql"
)

#: هجرةُ توسيعِ دقّةِ أعمدةِ الكلفةِ وحدَها — Q-42 (أ) · W-036.
COST_MIGRATION = Path(__file__).resolve().parents[1] / "migrations" / "016_widen_cost_precision.sql"

#: الأعمدةُ التي وحَّدَها القرار وبقيَت على `NUMERIC(20,4)` — (الجدول، العمود، أيُسمَحُ بالغياب).
UNIFIED_MONEY_COLUMNS: tuple[tuple[str, str, bool], ...] = (
    ("state_case_claims", "amount", True),
    ("state_authority_grants", "max_amount", True),
    ("state_government_delegations", "max_amount", True),
)

#: أعمدةُ **الكلفةِ** — وحدَها وُسِّعَت إلى `NUMERIC(20,8)` بحسمِ Q-42 (أ) · هجرةُ 016.
#:
#: ## لماذا نُقِلَ `model_cost_log.cost_usd` من الجدولِ الأعلى إلى هنا
#:
#: كانَ في `UNIFIED_MONEY_COLUMNS` يُحرَسُ بـ`MoneyType` و`MONEY_SCALE`. ثمَّ حسمَ
#: المالكُ في **Q-42 · الشقِّ الثاني · (أ)** بتاريخ 2026-08-24: «توسيعُ دقّةِ أعمدةِ
#: الكلفةِ وحدَها». فصارَ الحرسُ الأوّلُ **يكذِّبُ حسمًا سياديًّا** لو بقيَ.
#:
#: **ولم يُحذَفْ من الحراسةِ ولم تُضيَّقْ بوّابةٌ لتمرَّ دفعةٌ** (سابقةُ W-026):
#: نُقِلَ إلى حرسٍ **أقوى** (‏نوعٌ · مقياسٌ · دقّةٌ · نصُّ هجرةٍ · قيدُ مقدارٍ ·
#: سلوكٌ حيٌّ)، و`test_10` أدناهُ يُثبِتُ أنَّ اتّحادَ الجدولَينِ يساوي مجموعةَ
#: Q-20 الأصليّةَ حرفًا — فمن أسقطَ عمودًا من الحراسةِ سقطَ عليه ذلكَ الحرسُ.
COST_COLUMNS_WIDENED_BY_Q42: tuple[tuple[str, str, bool], ...] = (
    ("model_cost_log", "cost_usd", False),
)

#: مجموعةُ Q-20 الأصليّةُ قبلَ النقلِ — مكتوبةٌ صريحةً كي يُقاسَ النقلُ لا يُوصَفَ.
Q20_ORIGINAL_COLUMNS: frozenset[tuple[str, str, bool]] = frozenset(
    (
        ("state_case_claims", "amount", True),
        ("state_authority_grants", "max_amount", True),
        ("state_government_delegations", "max_amount", True),
        ("model_cost_log", "cost_usd", False),
    )
)

#: مفرداتُ الكلفةِ التي **لا** يُعيدُ بابُ الخزانةِ القديمُ تصديرَها — بقصدٍ مُعلَنٍ.
#: والعلّةُ في ترويسةِ `services/state_treasury/money.py`: بابُ الخزانةِ لو صدَّرَ
#: مقياسًا أوسعَ لصارَ حدُّ صرفٍ قابلًا للكتابةِ بثمانِ منازلَ من مسارٍ يُقرأُ
#: «خزانة» — أي ثغرةٌ في عقدِ Q-20 لا يراها مُراجِعٌ.
COST_PRIMITIVES_NOT_REEXPORTED: frozenset[str] = frozenset(
    {"COST_MAX", "COST_QUANT", "COST_SCALE", "CostMoneyType", "cost_check", "to_cost"}
)

#: أعمدةٌ اسمُها ماليٌّ ومعناها ليس مالًا — لا تُهاجَرُ، وهذا مُثبَّتٌ لا مُفترَض.
NOT_MONEY_BY_MEANING: tuple[tuple[str, str, str], ...] = (
    ("agents", "token_budget", "ميزانيّةُ رِموزٍ لا مال"),
    ("agent_population", "token_budget", "ميزانيّةُ رِموزٍ لا مال"),
    ("compliance_reports", "total_audits", "عَدَدٌ لا مبلغ"),
)


def _column(table_name: str, column_name: str):
    """يجدُ العمودَ في `metadata` بعدَ تحميلِ كلِّ النماذجِ المعنيّة."""
    import amos_federation.services.federal_state.models  # noqa: F401
    import amos_federation.services.model_gateway.model_layer as _model_layer  # noqa: F401
    from amos_federation.common.database import Base

    table = Base.metadata.tables.get(table_name)
    if table is None:
        # `model_cost_log` يعيشُ على قاعدةٍ تعريفيّةٍ أخرى في بوّابةِ النماذج.
        for obj in vars(_model_layer).values():
            if getattr(obj, "__tablename__", None) == table_name:
                table = obj.__table__
                break
    assert table is not None, f"لا جدولَ باسم {table_name} في أيِّ قاعدةٍ تعريفيّة"
    assert column_name in table.c, f"لا عمودَ {column_name} في {table_name}"
    return table.c[column_name]


# ============================================================================
# 1 · التصريحُ نفسُه
# ============================================================================


@pytest.mark.parametrize(("table", "column", "nullable"), UNIFIED_MONEY_COLUMNS)
def test_01_unified_columns_declare_the_money_type(table: str, column: str, nullable: bool) -> None:
    """كلُّ عمودٍ وحَّدَه Q-20 نوعُه `MoneyType` لا نصًّا ولا عائمًا ولا صحيحًا."""
    col = _column(table, column)
    assert isinstance(col.type, MoneyType), (
        f"{table}.{column} نوعُه {type(col.type).__name__} لا MoneyType — "
        "وهذا نقضٌ لِـQ-20: للمبلغِ تمثيلٌ واحدٌ لا أربعة"
    )
    assert (
        col.nullable is nullable
    ), f"{table}.{column} احتمالُ غيابِه تغيَّر — وغيابُ المبلغِ معنًى لا تفصيلٌ فنّيّ"


@pytest.mark.parametrize(("table", "column", "_nullable"), UNIFIED_MONEY_COLUMNS)
def test_02_unified_columns_carry_the_declared_precision(
    table: str, column: str, _nullable: bool
) -> None:
    """الدقّةُ مُعلَنةٌ لا ضِمنيّة: `NUMERIC(20,4)` تحتَ `MoneyType`."""
    impl = _column(table, column).type.impl
    assert isinstance(impl, Numeric), f"{table}.{column} تحقيقُه ليس Numeric"
    assert impl.scale == MONEY_SCALE, f"{table}.{column} منازلُه {impl.scale} لا {MONEY_SCALE}"
    assert impl.precision == 20, f"{table}.{column} دقّتُه {impl.precision} لا 20"
    assert impl.asdecimal is True, f"{table}.{column} يُقرأُ عائمًا — وهذا هو الخطأُ عينُه"


@pytest.mark.parametrize(("table", "column", "why"), NOT_MONEY_BY_MEANING)
def test_03_a_money_looking_name_is_not_migrated_by_its_name(
    table: str, column: str, why: str
) -> None:
    """ما اسمُه ماليٌّ ومعناه ليس مالًا يبقى كما هو — الهجرةُ للمعنى لا للاسم."""
    import amos_federation.services.federal_state.models  # noqa: F401
    from amos_federation.common.database import Base

    tbl = Base.metadata.tables.get(table)
    if tbl is None or column not in tbl.c:
        pytest.skip(f"{table}.{column} ليس في هذه القاعدةِ التعريفيّة")
    assert not isinstance(tbl.c[column].type, MoneyType), (
        f"{table}.{column} هُوجِرَ إلى MoneyType وهو {why} — " "ومن هاجرَ اسمًا لا معنًى أفسدَ المعنيَين"
    )


# ============================================================================
# 2 · الهجرةُ على القرص
# ============================================================================


def test_04_the_migration_file_exists_and_declares_its_identity() -> None:
    """الهجرةُ 014 موجودةٌ وتُعلِنُ هدفَها ومالكَها — مادةُ 009."""
    assert MIGRATION.is_file(), "الهجرةُ 014 غائبةٌ — فالتحويلُ في النماذجِ بلا سَنَدٍ في القاعدة"
    text = MIGRATION.read_text(encoding="utf-8")
    for field in ("الهدف:", "النطاق:", "المالك:", "تاريخ الإنشاء:"):
        assert field in text, f"الهجرةُ 014 لا تُعلِنُ «{field}»"


@pytest.mark.parametrize(("table", "column", "_nullable"), UNIFIED_MONEY_COLUMNS)
def test_05_the_migration_alters_every_unified_column(
    table: str, column: str, _nullable: bool
) -> None:
    """لكلِّ عمودٍ وحَّدَه القرارُ سطرُ تحويلٍ صريحٌ في الهجرة."""
    text = MIGRATION.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"ALTER TABLE IF EXISTS {table}\s+ALTER COLUMN {column} TYPE NUMERIC\(20,4\)",
        re.MULTILINE,
    )
    assert pattern.search(text), f"لا سطرَ تحويلٍ لـ{table}.{column} في الهجرة 014"
    assert "::NUMERIC(20,4)" in text, "التحويلُ بلا `USING ... ::NUMERIC` قد يفشلُ على نصٍّ قائم"


@pytest.mark.parametrize(("table", "column", "_nullable"), UNIFIED_MONEY_COLUMNS)
def test_06_every_unified_column_gains_a_bound_check(
    table: str, column: str, _nullable: bool
) -> None:
    """التحويلُ بلا `CHECK` يُبدِّلُ التمثيلَ ولا يحرسُ المقدار."""
    text = MIGRATION.read_text(encoding="utf-8")
    assert f"ck_{table}_{column}" in text, f"لا قيدَ مقدارٍ لـ{table}.{column}"
    assert str(int(MONEY_MAX)) in text, (
        f"حدُّ المالِ الأعلى {MONEY_MAX} غيرُ مذكورٍ في الهجرة — " "فالقيدُ إمّا أوسعُ من العقدِ أو أضيق"
    )


def test_07_the_migration_does_not_touch_what_it_declared_untouched() -> None:
    """المستثنياتُ مستثناةٌ فعلًا: لا `ALTER` لِـamos-credit ولا لِـ`institutions`."""
    text = MIGRATION.read_text(encoding="utf-8")
    alter_lines = [ln for ln in text.splitlines() if ln.strip().startswith("ALTER TABLE")]
    forbidden = ("treasury_reports", "treasury_transactions", "institutions ", "agents ")
    for line in alter_lines:
        for name in forbidden:
            assert name not in line, (
                f"الهجرةُ 014 تمسُّ «{name.strip()}» وقد أعلنَت أنّها لا تمسُّه — "
                "والحدُّ المُعلَنُ المخروقُ أسوأُ من غيرِ المُعلَن"
            )
    # وتُعلِنُ العلّةَ لا تسكتُ عنها.
    assert "Q-17" in text, "استثناءُ amos-credit بلا سَنَدٍ في Q-17 يصيرُ سهوًا"
    assert "Q-28" in text, "استثناءٌ بلا سؤالٍ مُقيَّدٍ هو صمتٌ لا قرار"


# ============================================================================
# 3 · العقدُ حيًّا
# ============================================================================


def test_08_the_money_gate_still_refuses_float() -> None:
    """بابُ المالِ يرفضُ العائمَ — وهذا هو أصلُ Q-20 لا فرعُه."""
    with pytest.raises(Exception):  # noqa: B017 — MoneyError نوعُه من الوحدةِ نفسِها
        to_money(1.5)  # type: ignore[arg-type]
    assert to_money("1.5") == Decimal("1.5000")
    assert to_money(Decimal("2")) == Decimal("2.0000")


def test_09_the_old_import_path_is_the_same_object_not_a_copy() -> None:
    """بابُ الخزانةِ القديمُ يفتحُ على المصدرِ الواحد — لا عقدَين لمالٍ واحد.

    ## ما تغيَّرَ في W-036 ولماذا ليسَ تضييقًا للحرسِ

    كانَ يُشترَطُ أن يُصدِّرَ البابُ القديمُ **كلَّ** اسمٍ في `canonical.__all__`.
    ثمَّ أُضيفَت مفرداتُ الكلفةِ (Q-42 (أ)) ولم تُعَدْ من ذلكَ البابِ **بقصدٍ
    مُعلَنٍ في ترويستِه**. فلو بقيَ الشرطُ حرفيًّا لسقطَ الفحصُ على قرارٍ مكتوبٍ.

    والشرطُ لم يُرفَعْ بل **صارَ أدقَّ**: كلُّ اسمٍ يُصدَّرُ إلّا ما في قائمةِ
    استثناءٍ **مكتوبةٍ**، ويُثبَتُ لكلِّ مستثنًى أنَّه (‏1) قائمٌ في المصدرِ،
    و(‏2) غائبٌ عن البابِ فعلًا — فالاستثناءُ مقيسٌ لا مُدَّعًى، و(‏3) اسمُه
    اسمُ كلفةٍ — فلا يُخبَّأُ خلفَ القائمةِ اسمٌ ليسَ منها.
    """
    from amos_federation.common import money as canonical
    from amos_federation.services.state_treasury import money as legacy_door

    assert legacy_door.MoneyType is canonical.MoneyType, "بابانِ لعقدَين — وهذا انشقاقٌ لا توافق"
    assert legacy_door.MONEY_MAX == canonical.MONEY_MAX
    assert legacy_door.to_money is canonical.to_money
    for name in canonical.__all__:
        if name in COST_PRIMITIVES_NOT_REEXPORTED:
            continue
        assert hasattr(legacy_door, name), f"البابُ القديمُ لا يُصدِّرُ {name} — كسرٌ صامتٌ لمستوردٍ قائم"

    for name in sorted(COST_PRIMITIVES_NOT_REEXPORTED):
        assert hasattr(canonical, name), f"{name} مُستثنًى من بابٍ وهو غيرُ موجودٍ في المصدرِ أصلًا"
        assert name in canonical.__all__, f"{name} ليسَ في `__all__` — فاستثناؤُه لا معنى له"
        assert not hasattr(legacy_door, name), (
            f"{name} أُعيدَ تصديرُه من بابِ الخزانةِ خلافًا لما أُعلِنَ في ترويستِه — "
            "فمقياسُ الكلفةِ صارَ في متناولِ حدِّ صرفٍ ومطالبةِ دعوى"
        )
        assert "cost" in name.lower(), (
            f"{name} في قائمةِ استثناءِ الكلفةِ وليسَ اسمَ كلفةٍ — "
            "والقائمةُ ليست بابًا خلفيًّا لإسقاطِ اسمٍ من الحراسة"
        )


# ============================================================================
# 4 · أعمدةُ الكلفةِ وحدَها — Q-42 · الشقُّ الثاني · (أ) · W-036
# ============================================================================


def test_10_no_money_column_left_the_guard_it_only_moved() -> None:
    """اتّحادُ الجدولَينِ يساوي مجموعةَ Q-20 الأصليّةَ — لا عمودَ أُسقِطَ من الحراسة.

    هذا هو الحرسُ الذي يمنعُ أن يُقرأَ عملُ W-036 «تضييقًا للبوّابةِ». فمن أرادَ
    أن يُخرِجَ عمودَ مالٍ من الحراسةِ فعليه أن يُعدِّلَ `Q20_ORIGINAL_COLUMNS`
    صراحةً — وذلكَ أثرٌ يُرى في المُراجعةِ لا يمرُّ في الظلّ (سابقةُ W-026).
    """
    guarded = set(UNIFIED_MONEY_COLUMNS) | set(COST_COLUMNS_WIDENED_BY_Q42)
    assert guarded == set(Q20_ORIGINAL_COLUMNS), (
        "مجموعةُ الأعمدةِ المحروسةِ لا تُطابِقُ مجموعةَ Q-20 الأصليّةَ: "
        f"ناقصٌ {sorted(set(Q20_ORIGINAL_COLUMNS) - guarded)} · "
        f"زائدٌ {sorted(guarded - set(Q20_ORIGINAL_COLUMNS))}"
    )
    assert not set(UNIFIED_MONEY_COLUMNS) & set(
        COST_COLUMNS_WIDENED_BY_Q42
    ), "عمودٌ في الجدولَينِ معًا — فله عقدانِ متعارضانِ وهذا أصلُ ما جاءَ Q-20 يمنعُه"


@pytest.mark.parametrize(("table", "column", "nullable"), COST_COLUMNS_WIDENED_BY_Q42)
def test_11_cost_columns_declare_the_cost_type(table: str, column: str, nullable: bool) -> None:
    """عمودُ الكلفةِ نوعُه `CostMoneyType` لا `MoneyType` — بحسمِ Q-42 (أ)."""
    col = _column(table, column)
    assert isinstance(col.type, CostMoneyType), (
        f"{table}.{column} نوعُه {type(col.type).__name__} لا CostMoneyType — "
        "فحسمُ Q-42 (أ) لم يُنفَّذْ في التصريحِ"
    )
    assert not isinstance(
        col.type, MoneyType
    ), f"{table}.{column} لا يزالُ MoneyType — والمقياسانِ لا يجتمعانِ في عمودٍ"
    assert col.nullable is nullable, f"{table}.{column} احتمالُ غيابِه تغيَّر"


@pytest.mark.parametrize(("table", "column", "_nullable"), COST_COLUMNS_WIDENED_BY_Q42)
def test_12_cost_columns_carry_eight_declared_places(
    table: str, column: str, _nullable: bool
) -> None:
    """`NUMERIC(20,8)` مُعلَنةٌ لا ضِمنيّة، والمقياسُ مقروءٌ من `COST_SCALE`."""
    impl = _column(table, column).type.impl
    assert isinstance(impl, Numeric), f"{table}.{column} تحقيقُه ليس Numeric"
    assert impl.scale == COST_SCALE, f"{table}.{column} منازلُه {impl.scale} لا {COST_SCALE}"
    assert impl.scale > MONEY_SCALE, "دقّةُ الكلفةِ ليست أوسعَ من دقّةِ المالِ — فلا توسيعَ وقعَ"
    assert impl.precision == 20, f"{table}.{column} دقّتُه {impl.precision} لا 20"
    assert impl.asdecimal is True, f"{table}.{column} يُقرأُ عائمًا — وهذا هو الخطأُ عينُه"


def test_13_the_cost_migration_exists_and_alters_only_the_cost_column() -> None:
    """هجرةُ 016 موجودةٌ، تُعلِنُ هويّتَها، وتمسُّ عمودَ الكلفةِ **وحدَه**."""
    assert COST_MIGRATION.is_file(), "هجرةُ 016 غائبةٌ — فتوسيعُ النموذجِ بلا سَنَدٍ في القاعدة"
    text = COST_MIGRATION.read_text(encoding="utf-8")
    for field in ("الهدف:", "النطاق:", "المالك:", "تاريخ الإنشاء:"):
        assert field in text, f"هجرةُ 016 لا تُعلِنُ «{field}»"
    assert "Q-42" in text, "هجرةٌ تُعدِّلُ عقدَ مالٍ بلا سَنَدٍ في قرارٍ مُقيَّدٍ"
    assert re.search(
        r"ALTER TABLE IF EXISTS model_cost_log\s+ALTER COLUMN cost_usd TYPE NUMERIC\(20,8\)",
        text,
        re.MULTILINE,
    ), "لا سطرَ تحويلٍ لـmodel_cost_log.cost_usd إلى NUMERIC(20,8) في الهجرة 016"

    # لا تمسُّ عمودَ مالٍ آخرَ: هذا هو معنى «أعمدةِ الكلفةِ وحدَها».
    #
    # ويُقاسُ على **العباراتِ** لا على الترويسةِ: الترويسةُ تُسمّي الجداولَ التي لا
    # تُمَسُّ *كي تُعلِنَ أنّها لا تُمَسّ*، فمن قاسَ النصَّ كلَّه سقطَ على إعلانِ
    # الكاتبِ نفسِه وحسِبَ الإفصاحَ خرقًا. فتُطرَحُ سطورُ التعليقِ أوّلًا.
    statements = "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith("--"))
    altered = [ln for ln in statements.splitlines() if ln.strip().startswith("ALTER TABLE")]
    assert altered, "هجرةٌ بلا عبارةِ تحويلٍ واحدةٍ خارجَ التعليقِ — كلامٌ لا هجرة"
    for line in altered:
        assert "model_cost_log" in line, (
            f"هجرةُ 016 تمسُّ جدولًا غيرَ جدولِ الكلفةِ: «{line.strip()}» — "
            "والحسمُ قالَ «أعمدةَ الكلفةِ وحدَها»"
        )
    for other_table, other_column, _ in UNIFIED_MONEY_COLUMNS:
        assert (
            other_table not in statements
        ), f"هجرةُ 016 تمسُّ {other_table}.{other_column} في عبارةٍ نافذةٍ وهو باقٍ على عقدِ Q-20"
        assert other_table in text, (
            f"هجرةُ 016 لا تذكرُ {other_table} حتى في ترويستِها — "
            "واستثناءٌ لا يُعلَنُ يُقرأُ سهوًا بعدَ حينٍ"
        )


def test_14_the_cost_migration_replaces_the_bound_it_invalidated() -> None:
    """القيدُ القديمُ (9×10¹¹) لم يبقَ صحيحًا بمقياسِ ثمانٍ، فيُبدَّلُ لا يُترَكُ.

    والثمنُ مُثبَّتٌ لا مُخفًى: الحدُّ **ضاقَ**. فمن قرأَ التوسيعَ مكسبًا بلا مقابلٍ
    أسقطَه هذا الفحصُ.
    """
    text = COST_MIGRATION.read_text(encoding="utf-8")
    assert (
        "DROP CONSTRAINT IF EXISTS ck_model_cost_log_cost_usd" in text
    ), "قيدُ الهجرةِ 014 يسمحُ حتى 9×10¹¹ ولم يُحذَفْ — فالقيدُ أوسعُ من العقدِ"
    assert (
        "ck_model_cost_log_cost_usd" in text.split("DROP CONSTRAINT", 1)[1]
    ), "حُذِفَ القيدُ ولم يُوضَعْ بديلٌ — فالعمودُ صارَ بلا حرسِ مقدارٍ"
    assert str(int(COST_MAX)) in text, f"حدُّ الكلفةِ {COST_MAX} غيرُ مذكورٍ في الهجرة"
    assert COST_MAX < MONEY_MAX, "حدُّ الكلفةِ ليسَ أضيقَ من حدِّ المالِ — وهذا يعني أنَّ حسابَ 2⁵³ لم يُحترَمْ"
    assert (
        COST_MAX * (10**COST_SCALE) < 2**53
    ), "حدُّ الكلفةِ × 10^المقياس يتجاوزُ 2⁵³ — فالدقّةُ غيرُ مضمونةٍ على SQLite"


def test_15_the_cost_gate_refuses_float_and_keeps_eight_places() -> None:
    """بابُ الكلفةِ يرفضُ العائمَ كبابِ المالِ، ويُبقي ثمانَ منازلَ حيًّا لا تصريحًا."""
    with pytest.raises(Exception):  # noqa: B017 — MoneyError نوعُه من الوحدةِ نفسِها
        to_cost(1.5)  # type: ignore[arg-type]
    assert to_cost("0.00000080") == Decimal("0.00000080"), "ثمانُ منازلَ لم تُحفَظْ"
    assert to_cost("0.00000080").as_tuple().exponent == -COST_SCALE, "الأُسُّ ليسَ -8"
    assert format(to_cost("0.00000080"), "f") == "0.00000080"
    assert str(to_cost("7.77")) == "7.77000000"
    # وهذا هو العيبُ الذي جاءَ الحسمُ يرفعُه، مقيسًا في سطرَين:
    assert str(to_money("0.00003")) == "0.0000", "عقدُ المالِ لم يكن يُبلِعُ الكسرَ — فلا عيبَ إذن"
    assert str(to_cost("0.00003")) == "0.00003000", "عقدُ الكلفةِ لا يزالُ يُبلِعُ الكسرَ"


def test_15b_a_measured_consequence_of_eight_places_the_scientific_rendering() -> None:
    """أثرٌ لم يكن مقصودًا وقد ظهرَ بالقياسِ فيُقيَّدُ لا يُداوَرُ.

    `Decimal.__str__` يُنتِجُ الصيغةَ العلميّةَ متى كانَ الأُسُّ المُعدَّلُ أصغرَ من
    `-6`. وثمانُ منازلَ تُدخِلُ هذا المدى أوّلَ مرّةٍ في تاريخِ هذا المستودعِ:
    فكلفةُ `0.0000008$` تُطبَعُ **`8.0E-7`** لا `0.00000080`، و`float()` عليها
    تُنتِجُ `8e-07`.

    **والقيمةُ صحيحةٌ** — لا فقدَ ولا تقريبَ؛ الخللُ في **العرضِ** لا في التخزينِ.
    ولم يُخترَعْ لها مُنسِّقٌ في هذا العملِ: إضافةُ `format_cost` قرارُ عرضٍ يتّصلُ
    بسؤالٍ مفتوحٍ مُقيَّدٍ (**Q-29**: نوعُ `cost_usd` في الجوابِ المنشور)، ومن حسمَ
    سؤالًا مفتوحًا بيدِه في هامشِ عملٍ آخرَ اختلقَ قرارًا سياديًّا.

    فهذا الفحصُ **يُثبِّتُ الأثرَ كما هو**: إن غُيِّرَ العرضُ يومًا فليُغيَّرْ بقرارٍ
    يُسقِطُ هذا الفحصَ صراحةً، لا بانحرافٍ صامتٍ.
    """
    tiny = to_cost("0.0000008")
    assert str(tiny) == "8.0E-7", "صيغةُ الطبعِ تغيَّرَت — إن كانَ ذلكَ بقرارٍ فليُقيَّدْ في Q-29"
    assert format(tiny, "f") == "0.00000080", "الصيغةُ الصريحةُ هي المخرجُ الصحيحُ للعرض"
    assert tiny == Decimal("0.0000008"), "القيمةُ نفسُها سليمةٌ — والخللُ في العرضِ لا التخزين"
    # وحدُّ ظهورِ الصيغةِ العلميّةِ مقيسٌ لا مُقدَّرٌ: عندَ الأُسِّ المُعدَّلِ -7.
    assert "E" not in str(to_cost("0.000001")), "عندَ 1e-6 لا تظهرُ الصيغةُ العلميّة"
    assert "E" in str(to_cost("0.0000001")), "وعندَ 1e-7 تظهرُ — وهذا هو الحدُّ"


def test_16_widening_the_cost_scale_did_not_widen_any_other_money_column() -> None:
    """سائرُ أعمدةِ المالِ باقيةٌ على أربعِ منازلَ — فالاستثناءُ مقصورٌ فعلًا.

    هذا هو الحرسُ الذي يمنعُ أن يتسرَّبَ مقياسُ الكلفةِ إلى عقدِ Q-20 لاحقًا:
    من وسَّعَ حدَّ صرفٍ أو مطالبةَ دعوى بثمانِ منازلَ أسقطَه هذا الفحصُ.
    """
    for table, column, _ in UNIFIED_MONEY_COLUMNS:
        impl = _column(table, column).type.impl
        assert impl.scale == MONEY_SCALE, (
            f"{table}.{column} صارَ {impl.scale} منازلَ — وحسمُ Q-42 قالَ "
            "«أعمدةَ الكلفةِ وحدَها» لا كلَّ مبلغٍ"
        )
