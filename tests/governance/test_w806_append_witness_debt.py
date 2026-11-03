"""الهدف: حرسُ الدَّينِ المُسمّى — القياسُ المنشورُ يُطابِقُ الشجرةَ الحيّةَ لا
يُنسخُ رقمُه إلى الفحصِ فيصيرَ «حقيقةً مثبَّتةً في الشِّفرة» (§ 3 من A1_CD_DESIGN.md
· قرارُ المالكِ (ج-1)(أ) · W-806).

النطاق: `tools/audit/append_witness_debt.py` وقياسُه المنشورُ
`docs/audit/measurements/append_witness_debt_p15.json` — تصنيفُ نداءاتِ شهودِ
الإلحاقِ (`.append`/`.publish` على مُستقبِلٍ من جنسِ الشاهدِ · `record_domain_trace`)
في الإنتاجِ بموقعِها من العمليّاتِ المحروسة.

المالك: governance/
تاريخ الإنشاء: 2026-11-03
تاريخ آخر تعديل: 2026-11-03

## لماذا هذا الحرسُ موجود

قرارُ المالكِ (ج-1)(أ) قال: «ما خارجَ _apply دَينٌ مسمّى» — فالدَّينُ يُقاسُ
ويُنشرُ ولا يُخفى. وبلا حرسٍ يتقادَمُ المنشورُ عن الشجرةِ (تُضافُ نداءاتٌ أو
تُهجَّرُ) فتُقرأ الوثائقُ رقمًا كاذبًا. هذا الفحصُ يعيدُ القياسَ من الشجرةِ
الحيةِ ويطابقُه بالمنشورِ — فكلُّ انحرافٍ يسقُطُ هنا لا في قرارٍ يتلو.

## حدُّ صدقِ هذا الحرس

بنيويٌّ: أداةُ القياسِ نفسُها على الشجرةِ الحيّةِ مقابلَ الملفِّ المنشورِ —
لا رقمٌ منسوخٌ في هذا الملفِ. والمفاتيحُ ثابتةٌ (ملفٌّ · دالّةٌ خارجيّةٌ) بلا
أرقامِ أسطرٍ (درسُ DISC-039): لو عادَ القياسُ يحملُ إحداثيًّا متحرّكًا سقطَ
الفحصُ الآخِرُ.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from types import ModuleType

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
DEBT_TOOL = REPO_ROOT / "tools" / "audit" / "append_witness_debt.py"
PUBLISHED = (
    REPO_ROOT / "docs" / "audit" / "measurements" / "append_witness_debt_p15.json"
)


def _load_debt_tool() -> ModuleType:
    spec = importlib.util.spec_from_file_location("append_witness_debt", DEBT_TOOL)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["append_witness_debt"] = module
    spec.loader.exec_module(module)
    return module


def test_القياسُ_المنشورُ_يطابقُ_الشجرةَ_الحيّةَ() -> None:
    # الموضعُ المنشورُ مثبَّتٌ إلى جذرِ المستودعِ لا إلى ملفٍّ آخرَ — وهذه
    # الإحالةُ الحيّةُ هي التي تجعلُ الفحصَ يشملُ الأداةَ (طريقُ الإنفاذِ).
    assert PUBLISHED == REPO_ROOT / "docs" / "audit" / "measurements" / (
        "append_witness_debt_p15.json"
    )
    tool = _load_debt_tool()
    measured = tool.measure()
    published = json.loads(PUBLISHED.read_text(encoding="utf-8"))
    assert measured["counts"] == published["counts"], (
        f"تصنيفُ الشهودِ انحرفَ عن المنشورِ: {measured['counts']} ≠ "
        f"{published['counts']} — أُعيدِ النشرُ لا التبرير."
    )
    assert measured["total_calls"] == published["total_calls"]
    assert measured["named_debt"] == published["named_debt"]
    assert measured["outside_debt_keys"] == published["outside_debt_keys"], (
        "مفاتيحُ الدَّينِ المسمّى انحرفَتْ عن المنشورِ — تُعادُ مطابقةُ النشرِ."
    )


def test_الفئاتُ_الثلاثُ_تُفسِّرُ_المجموعَ() -> None:
    tool = _load_debt_tool()
    measured = tool.measure()
    counts = measured["counts"]
    assert set(counts) == {
        "داخلَ مطبِّقٍ متداخلٍ في عمليّةٍ محروسةٍ",
        "في جسدِ عمليّةٍ محروسةٍ خارجَ المتداخلة",
        "خارجَ أيِّ عمليّةٍ محروسةٍ",
    }, "فئاتُ التصنيفِ تغيَّرَت — التصنيفُ حدٌّ مُعلَنٌ لا اجتهادَ أداة."
    assert sum(counts.values()) == measured["total_calls"]
    assert counts["خارجَ أيِّ عمليّةٍ محروسةٍ"] == measured["named_debt"]


def test_المفاتيحُ_ثابتةٌ_بلا_أرقامِ_أسطرٍ() -> None:
    tool = _load_debt_tool()
    measured = tool.measure()
    for key in measured["outside_debt_keys"]:
        assert re.search(r":\d+", key) is None, (
            f"مفتاحٌ يحملُ إحداثيًّا متحرّكًا (رقمَ سطرٍ): {key} — درسُ DISC-039: "
            "الإحداثيُّ يتحرَّكُ بسطرِ تعليقٍ فيُقادِمُ قياسًا لم يتغيَّرْ سلوكُه."
        )
        assert key.count("::") == 1, f"مفتاحٌ خارجَ الصيغةِ (ملفٌّ · دالّة): {key}"
