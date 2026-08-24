"""
AMOS-Federation State Treasury — Money Primitive (إعادةُ تصدير)
الهدف: إبقاءُ المسارِ القديمِ صالحًا بعدَ رفعِ مفردةِ المالِ إلى `common/money.py`
       في Q-20، فلا يُكسَرُ مستوردٌ قائمٌ ولا يُنسَخُ عقدٌ مرّتين.
النطاق: services/state_treasury
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-17 (R7-B)
تاريخ آخر تعديل: 2026-08-20 (Q-20)

## لماذا ملفٌّ لا يحملُ منطقًا

لأنَّ نسخَ العقدِ في موضعَين هو الطريقُ إلى عقدَين مختلفَين. فالمصدرُ الوحيدُ
`amos_federation.common.money`، وهذا الملفُّ بابٌ إليه لا نسخةٌ منه. ومن أرادَ
تعديلَ دقّةِ المالِ أو حدِّه فليُعدِّلْه هناك؛ فلا شيءَ هنا يُعدَّل.

## ولماذا لا تُعادُ هنا مفرداتُ الكلفةِ (`to_cost` · `CostMoneyType`) — 2026-08-24 · W-036

أُضيفَ في `common/money.py` مقياسٌ ثانٍ **مقصورٌ على أعمدةِ الكلفةِ** بحسمِ المالكِ
في Q-42 (أ). ولم يُعَدْ تصديرُه من هذا البابِ **بقصدٍ يُعلَنُ لا بسهوٍ**: هذا البابُ
بابُ الخزانةِ، وإعادةُ تصديرِ مقياسٍ أوسعَ منه تجعلُ حدَّ صرفٍ أو مطالبةَ دعوى
قابلَينِ لأن يُكتَبا بثمانِ منازلَ من مسارٍ يُقرأُ «خزانة» — أي تُفتَحُ على عقدِ
Q-20 ثغرةٌ لا يراها مُراجِعٌ. فمن أرادَ مفردةَ الكلفةِ فليستوردْها من موضعِها
الصريحِ `amos_federation.common.money`، ويُقرأُ في سطرِ الاستيرادِ أنَّها كلفةٌ.
"""

from __future__ import annotations

from amos_federation.common.money import (  # noqa: F401 — إعادةُ تصديرٍ مقصودة
    CURRENCY_LENGTH,
    MONEY_MAX,
    MONEY_QUANT,
    MONEY_SCALE,
    MoneyError,
    MoneyType,
    currency_check,
    format_money,
    money_sum,
    normalize_currency,
    positive_money_check,
    require_positive,
    to_money,
)

__all__ = [
    "CURRENCY_LENGTH",
    "MONEY_MAX",
    "MONEY_QUANT",
    "MONEY_SCALE",
    "MoneyError",
    "MoneyType",
    "currency_check",
    "format_money",
    "money_sum",
    "normalize_currency",
    "positive_money_check",
    "require_positive",
    "to_money",
]
