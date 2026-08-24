"""
AMOS-Federation State Treasury — Money Primitive
الهدف: مالٌ بـDecimal دقيق، ونوع عمود واحد لكل مبلغ في الدولة
النطاق: common — مفردةٌ مشتركةٌ لا مِلكَ خدمةٍ واحدة
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-17 (R7-B)
تاريخ آخر تعديل: 2026-08-24 (Q-42 · الشقُّ الثاني · (أ) — دقّةُ أعمدةِ الكلفةِ وحدَها)

## لماذا نُقِلَ هذا الملفُّ من `services/state_treasury` إلى `common`

وُلِدَ في خزانةِ الدولةِ لأنّها كانت وحدَها تعرفُ المال. ثمّ حُسِمَ **Q-20** بأن
يكونَ لكلِّ مبلغٍ تمثيلٌ واحد، فصارَ العقدُ لازمًا لأربعِ خدماتٍ: القضاءُ
(`state_case_claims.amount`) والسجلُّ (`state_authority_grants.max_amount`)
والولايةُ (`state_government_delegations.max_amount`) وبوّابةُ النماذج
(`model_cost_log.cost_usd`). واستيرادُه من موضعِه القديمِ كان يُشعِلُ
استيرادًا دائريًّا حقيقيًّا (`state_treasury/__init__` يجرُّ الخدمةَ كلَّها،
وهي تجرُّ `government_services`، وهي تعودُ إلى `national_registry`).

فالنقلُ **رفعُ مفردةٍ إلى موضعِها الصحيح** لا تفكيكُ خدمة: المضمونُ لم يتغيّرْ
حرفًا، والمسارُ القديمُ يبقى صالحًا بإعادةِ تصديرٍ صريحةٍ في
`services/state_treasury/money.py` كي لا يُكسَرَ ما يستوردُ منه.

## لماذا ليس `Float`

في المستودع خزانةٌ سابقة (Phase 10، `services/governance/treasury.py`) تخزّن المال
في `Float`، وفي PostgreSQL صار العمود `double precision`. هذا خطأ لا رأي: جمع
`0.1 + 0.2` في العائم لا يساوي `0.3`، وميزانيةُ دولة لا تُبنى على تقريب. فلا يُلمس
ذلك الجدول القديم في هذه الوحدة (ليس هذا نطاقها)، **ولا يُبنى الجديد بخطئه**.

## ما يفعله هذا الملفّ

- `MoneyType`: عمود `NUMERIC(20, 4)` حقيقي في PostgreSQL، والقيمة في بايثون
  `Decimal` مُقرَّبة إلى أربع منازل دائمًا، ذهابًا وعودة.
- `to_money`: البوّابة الوحيدة لتحويل مدخلٍ إلى مبلغ. تقبل `Decimal` و`int`
  و`str`، و**ترفض `float` صراحةً** — فلا يتسرّب العائم من واجهةٍ أو اختبار.
- `money_sum`: جمع مبالغ بـ`Decimal`.

## حدٌّ يُقال ولا يُخفى

SQLite لا يملك نوعًا عشريًّا حقيقيًّا؛ يخزّن `NUMERIC` عائمًا مزدوجًا. فالدقّة
المطلقة مضمونة على **PostgreSQL** (المصدر التشغيلي)، وعلى SQLite تُضمَن ضمن حدّ
المقدار المفروض أدناه: `MONEY_MAX × 10⁴ < 2⁵³`. لذلك `MONEY_MAX` ليس رقمًا
تجميليًّا، بل هو ما يجعل الدقّة قابلة للبرهان في اللهجتين، وهو مفروض بقيد `CHECK`
في القاعدة لا بفحصٍ في بايثون وحده.

## لا `SUM` على المال في SQL

مجاميع المال تُحسب في بايثون فوق `Decimal` (`money_sum`)، لا بـ`func.sum`: على
SQLite كان المجموع سيمرّ بالعائم فيُنتج `1234.5599999999999` في تقرير موازنة.
وهذا محروسٌ باختبار ساكن يمنع `func.sum` في خدمة الخزانة.
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Iterable

from sqlalchemy import Numeric
from sqlalchemy.types import TypeDecorator

#: أربع منازل عشرية — تكفي العملات ذات المنزلتين وتترك مجالًا لأسعار الوحدة.
MONEY_SCALE = 4
MONEY_QUANT = Decimal(1).scaleb(-MONEY_SCALE)  # Decimal("0.0001")

#: الحدّ الأعلى للمبلغ الواحد: 9×10¹¹. وهو مشتقّ لا مُختار:
#: 9e11 × 10⁴ = 9e15 < 2⁵³ ≈ 9.007e15، فيبقى كل مبلغ قابلًا للتمثيل تمامًا حتى
#: على SQLite. ومفروض بـ`CHECK` في كل عمود مبلغ.
MONEY_MAX = Decimal("900000000000")

CURRENCY_LENGTH = 3

#: ثمانِ منازلَ عشريّةٍ — **لأعمدةِ الكلفةِ وحدَها** (Q-42 · الشقُّ الثاني · (أ) · W-036).
#:
#: ## بأيِّ سلطةٍ يُوجَدُ مقياسٌ ثانٍ في ملفِّ «تمثيلٍ واحدٍ للمبلغِ»
#:
#: بنصِّ المالكِ في Q-42 · الشقِّ الثاني · الخيارِ (أ) بتاريخ 2026-08-24:
#: **«توسيعُ دقّةِ أعمدةِ الكلفةِ وحدَها»**. فهذا ليسَ نقضًا لحسمِ Q-20 ولا التفافًا
#: عليه: `MONEY_SCALE = 4` يبقى عقدَ **كلِّ مبلغٍ** في الدولةِ كما هو، ولا يُمَسُّ
#: عمودٌ واحدٌ منه. والاستثناءُ **مقصورٌ نصًّا على أعمدةِ الكلفةِ** ومُعلَنٌ هنا في
#: نفسِ الملفِّ الذي يحملُ العقدَ الأصلَ كي لا يُبنى عقدُ مالٍ ثانٍ في زاويةٍ.
#:
#: ## لماذا ثمانٍ لا سِتٌّ ولا عَشرٌ — رقمٌ مُشتقٌّ لا مُختارٌ
#:
#: أرخصُ سعرٍ غيرِ صفريٍّ في جدولَي التسعيرِ `0.0008$` لكلِّ ألفِ رمزٍ (‏مقيسٌ في
#: `docs/audit/measurements/pricing_divergence.json`)، أي `0.0000008$` للرمزِ
#: الواحدِ — فسبعُ منازلَ هي **أوّلُ** منزلةٍ يظهرُ فيها رمزٌ واحدٌ، والثامنةُ هامشٌ
#: لسعرٍ أرخصَ يأتي. وستٌّ كانَت ستُقيِّدُ الرمزَ الواحدَ `0.000001` بتقريبٍ لا
#: بقياسٍ، وعَشرٌ كانَت ستهبِطُ بالحدِّ الأعلى إلى أقلَّ من مليونِ دولارٍ.
COST_SCALE = 8
COST_QUANT = Decimal(1).scaleb(-COST_SCALE)  # Decimal("0.00000001")

#: الحدُّ الأعلى لقيدِ كلفةٍ واحدٍ: 9×10⁷. وهو **مُشتقٌّ بنفسِ حسابِ `MONEY_MAX`**:
#: 9e7 × 10⁸ = 9e15 < 2⁵³ ≈ 9.007e15، فيبقى كلُّ قيدِ كلفةٍ قابلًا للتمثيلِ تمامًا
#: حتى على SQLite.
#:
#: **وهذا ثمنٌ يُقالُ ولا يُخفى:** توسيعُ الدقّةِ أربعَ منازلَ **يُنقِصُ** الحدَّ
#: الأعلى من 9×10¹¹ إلى 9×10⁷ — لأنَّ حاصلَ الضربِ محكومٌ بـ2⁵³ لا بالرغبةِ. فهو
#: **تضييقٌ حقيقيٌّ** في المقدارِ مقابلَ توسيعٍ حقيقيٍّ في الدقّةِ، لا مكسبٌ بلا
#: مقابلٍ. ومقبولٌ هنا بقياسٍ: قيدُ كلفةِ نداءٍ واحدٍ يتجاوزُ تسعينَ مليونَ دولارٍ
#: ليسَ مالًا بل خطأً، ورفضُه في القاعدةِ أولى من قبولِه. والحدُّ مفروضٌ بـ`CHECK`
#: في الهجرةِ 016 لا بفحصٍ في بايثون وحدَه.
COST_MAX = Decimal("90000000")


class MoneyError(ValueError):
    """مبلغ غير مقبول — نوعًا أو مقدارًا."""


def to_money(value: Any, *, field: str = "amount") -> Decimal:
    """حوِّل مدخلًا إلى مبلغ `Decimal` بأربع منازل، أو ارفضه.

    `float` مرفوض بقصد: قبولُه يعني إدخال خطأ التمثيل من الحدّ الخارجي، ثم
    الاعتذار عنه في التقارير. من يملك عائمًا يحوّله نصًّا أولًا وهو يعلم أنه يقرّب.

    Raises:
        MoneyError: عائم، أو نوع غير مفهوم، أو مقدار خارج الحدّ.
    """
    if isinstance(value, bool):
        raise MoneyError(f"{field}: قيمة منطقية ليست مبلغًا")
    if isinstance(value, float):
        raise MoneyError(f"{field}: العائم غير مقبول للمال — مرِّر Decimal أو نصًّا مثل '12.3400'")
    if isinstance(value, Decimal):
        amount = value
    elif isinstance(value, int):
        amount = Decimal(value)
    elif isinstance(value, str):
        try:
            amount = Decimal(value.strip())
        except InvalidOperation as exc:
            raise MoneyError(f"{field}: نصٌّ ليس عددًا عشريًّا: '{value}'") from exc
    else:
        raise MoneyError(f"{field}: نوع غير مقبول للمال: {type(value).__name__}")

    if not amount.is_finite():
        raise MoneyError(f"{field}: مبلغ غير منتهٍ")
    quantized = amount.quantize(MONEY_QUANT)
    if abs(quantized) > MONEY_MAX:
        raise MoneyError(f"{field}: المقدار يتجاوز الحدّ المسموح {MONEY_MAX}")
    return quantized


def to_cost(value: Any, *, field: str = "cost") -> Decimal:
    """حوِّل مدخلًا إلى **كلفةٍ** `Decimal` بثمانِ منازلَ، أو ارفضه.

    نفسُ انضباطِ `to_money` حرفًا: `float` مرفوضٌ، والحدُّ مفروضٌ، والنتيجةُ
    مُقرَّبةٌ إلى مقياسٍ مُعلَنٍ. والفرقُ الوحيدُ **المقياسُ والحدُّ**، وهما
    مقصورانِ على أعمدةِ الكلفةِ بنصِّ الحسمِ (Q-42 · (أ)).

    ولماذا دالّةٌ ثانيةٌ لا وسيطُ `scale` في `to_money`: وسيطٌ اختياريٌّ يجعلُ
    مقياسَ المالِ **قابلًا للتغييرِ في موضعِ النداءِ**، فيكفي أن يُمرِّرَه أحدٌ في
    خزانةٍ حتى يصيرَ لعقدِ Q-20 استثناءٌ لا يراهُ مُراجِعٌ. فالمقياسُ الثاني
    **مُسمًّى ومقصورٌ** ويُقرأُ في كلِّ موضعٍ يُستدعى فيه.

    Raises:
        MoneyError: عائم، أو نوع غير مفهوم، أو مقدار خارج الحدّ.
    """
    if isinstance(value, bool):
        raise MoneyError(f"{field}: قيمة منطقية ليست كلفةً")
    if isinstance(value, float):
        raise MoneyError(f"{field}: العائم غير مقبول للكلفة — مرِّر Decimal أو نصًّا مثل '0.00000080'")
    if isinstance(value, Decimal):
        amount = value
    elif isinstance(value, int):
        amount = Decimal(value)
    elif isinstance(value, str):
        try:
            amount = Decimal(value.strip())
        except InvalidOperation as exc:
            raise MoneyError(f"{field}: نصٌّ ليس عددًا عشريًّا: '{value}'") from exc
    else:
        raise MoneyError(f"{field}: نوع غير مقبول للكلفة: {type(value).__name__}")

    if not amount.is_finite():
        raise MoneyError(f"{field}: مبلغ غير منتهٍ")
    quantized = amount.quantize(COST_QUANT)
    if abs(quantized) > COST_MAX:
        raise MoneyError(f"{field}: المقدار يتجاوز الحدّ المسموح للكلفة {COST_MAX}")
    return quantized


def require_positive(value: Any, *, field: str = "amount") -> Decimal:
    """مبلغٌ موجب حصرًا — الصفر والسالب مرفوضان في الحركة المالية.

    السالب يُعبَّر عنه باتجاه القيد (`debit`/`credit`) لا بإشارة المبلغ. ولو سُمح
    بالإشارتين لصار للحركة الواحدة تمثيلان، واختلّ كل مجموع.
    """
    amount = to_money(value, field=field)
    if amount <= 0:
        raise MoneyError(f"{field}: المبلغ يجب أن يكون موجبًا (وُجد {amount})")
    return amount


def money_sum(values: Iterable[Any]) -> Decimal:
    """اجمع مبالغ بـ`Decimal` — لا عائم في أي خطوة."""
    total = Decimal(0)
    for value in values:
        total += to_money(value)
    return total.quantize(MONEY_QUANT)


def format_money(value: Any) -> str:
    """نصٌّ ثابت المنازل، صالحٌ للحمولة والحدث والتقرير.

    الحمولات تحمل المال نصًّا لا عددًا: `json` لا يعرف `Decimal`، وتحويله إلى
    `float` في الحدث كان سيُعيد الخطأ الذي طُرد من القاعدة.
    """
    return f"{to_money(value):.{MONEY_SCALE}f}"


def normalize_currency(value: str, *, field: str = "currency") -> str:
    """رمز عملة من ثلاثة أحرف كبيرة (ISO-4217 شكلًا لا تحقّقًا من قائمة).

    لا قائمة عملات مُغلقة هنا: التحقّق من وجود العملة فعلًا يلزمه مصدرٌ خارجي،
    وادّعاؤه اليوم كان سيكون تحقّقًا وهميًّا. المفروض هو الشكل، في القاعدة أيضًا.
    """
    code = (value or "").strip().upper()
    if len(code) != CURRENCY_LENGTH or not code.isalpha() or not code.isascii():
        raise MoneyError(f"{field}: رمز العملة يجب أن يكون ثلاثة أحرف لاتينية، وُجد '{value}'")
    return code


class MoneyType(TypeDecorator):  # type: ignore[type-arg]
    """عمود مبلغ: `NUMERIC(20, 4)` في القاعدة، و`Decimal` في بايثون دائمًا."""

    impl = Numeric(20, MONEY_SCALE, asdecimal=True)
    cache_ok = True

    def process_bind_param(self, value: Any, dialect: Any) -> Decimal | None:
        if value is None:
            return None
        return to_money(value)

    def process_result_value(self, value: Any, dialect: Any) -> Decimal | None:
        """التقريب عند القراءة يجعل SQLite يعيد ما كُتب لا تقريبَ عائمٍ له."""
        if value is None:
            return None
        if isinstance(value, float):  # SQLite: NUMERIC مخزَّن عائمًا
            return Decimal(repr(value)).quantize(MONEY_QUANT)
        return to_money(value)


class CostMoneyType(TypeDecorator):  # type: ignore[type-arg]
    """عمود كلفة: `NUMERIC(20, 8)` في القاعدة، و`Decimal` في بايثون دائمًا.

    مقصورٌ على أعمدةِ الكلفةِ (Q-42 · (أ) · هجرةُ 016). وسائرُ المبالغِ تبقى على
    `MoneyType` أي `NUMERIC(20, 4)` بحسمِ Q-20 — فلا يُستعملُ هذا النوعُ لمبلغٍ
    ليسَ كلفةً، ومن استعملَه كذلك وسَّعَ عقدًا بلا قرارٍ.
    """

    impl = Numeric(20, COST_SCALE, asdecimal=True)
    cache_ok = True

    def process_bind_param(self, value: Any, dialect: Any) -> Decimal | None:
        if value is None:
            return None
        return to_cost(value)

    def process_result_value(self, value: Any, dialect: Any) -> Decimal | None:
        """التقريب عند القراءة يجعل SQLite يعيد ما كُتب لا تقريبَ عائمٍ له."""
        if value is None:
            return None
        if isinstance(value, float):  # SQLite: NUMERIC مخزَّن عائمًا
            return Decimal(repr(value)).quantize(COST_QUANT)
        return to_cost(value)


#: تعبير `CHECK` مشترك لكل عمود مبلغ موجب — نصٌّ واحد فلا تتباعد الصياغات.
def positive_money_check(column: str) -> str:
    """قيد: موجبٌ وداخل الحدّ. يعمل حرفيًّا في PostgreSQL وSQLite."""
    return f"{column} > 0 AND {column} <= {MONEY_MAX}"


def currency_check(column: str = "currency") -> str:
    """قيد شكل العملة — ثلاثة أحرف كبيرة، بتعبير تقبله اللهجتان."""
    return f"length({column}) = {CURRENCY_LENGTH} AND {column} = upper({column})"


def cost_check(column: str) -> str:
    """قيد عمود كلفة: غيرُ سالبٍ وداخلَ حدِّ الكلفةِ. يعمل حرفيًّا في اللهجتين.

    والصفرُ **مقبولٌ** هنا خلافًا لـ`positive_money_check`: كلفةُ نداءٍ محليٍّ صفرٌ
    حقيقيٌّ لا غيابُ قيمةٍ، ومنعُه كانَ سيمنعَ قيدَ نداءٍ وقعَ فعلًا.
    """
    return f"{column} >= 0 AND {column} <= {COST_MAX}"


__all__ = [
    "COST_MAX",
    "COST_QUANT",
    "COST_SCALE",
    "CURRENCY_LENGTH",
    "MONEY_MAX",
    "MONEY_QUANT",
    "MONEY_SCALE",
    "CostMoneyType",
    "MoneyError",
    "MoneyType",
    "cost_check",
    "currency_check",
    "format_money",
    "money_sum",
    "normalize_currency",
    "positive_money_check",
    "require_positive",
    "to_cost",
    "to_money",
]
