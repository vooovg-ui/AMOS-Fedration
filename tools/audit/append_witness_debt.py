"""الهدف: قياسُ الدَّينُ المسمّى — نداءاتُ شهودِ الإلحاقِ في الإنتاجِ مصنَّفةً بموقعِها (§ 3 من A1_CD_DESIGN.md).

قرارُ المالكِ (ج-1)(أ) في Q-87: «ما خارجَ _apply دَينٌ مسمّى» — فما كانَ من نداءاتِ
الشاهدِ (إلحاقٍ بسجلٍّ أو نشرٍ على ناقلٍ) داخلَ جسدِ عمليّةٍ محروسةٍ فهو مؤمَّنٌ بإعلانِ
مستدعيهِ، وما كانَ خارجَها فهو دَينٌ **مسمّى**: يُقاسُ ويُنشرُ ولا يُخفى. وهذا القياسُ
يحوّلُ التصنيفَ الساكنَ الذي كانَ في مِسبارِ W-799 (`evidence/W-799/a1cd_projection_probe.py`
§ 5) إلى أداةٍ دائمةٍ تنشرُ قياسًا محروسًا بعقدِ النسبِ.

التصنيفُ ساكنٌ بالنصِّ — حدٌّ مُعلَنٌ لا اجتهادَ: `guard_declared(` في جسدِ الدالّةِ
الخارجيّةِ المحيطةِ بالنداءِ:
- «داخلَ مطبِّقٍ متداخلٍ في عمليّةٍ محروسةٍ»: النداءُ في دالّةٍ متداخلةٍ داخلَ محروسة.
- «في جسدِ عمليّةٍ محروسةٍ خارجَ المتداخلة»: النداءُ في جسدِ المحروسةِ نفسِها.
- «خارجَ أيِّ عمليّةٍ محروسةٍ»: لا محروسةَ تحيطُه — وهذا هو الدَّينُ المسمّى.

والمفاتيحُ ثابتةٌ (ملفٌّ · دالّةٌ خارجيّةٌ) ولا تحملُ رقمَ سطرٍ: الإحداثيُّ يتحرَّكُ بسطرِ
تعليقٍ فيُقادِمُ قياسًا لم يتغيَّرْ سلوكُه (درسُ DISC-039 المُعمَّمُ في W-806).

طريقُ الإنفاذ: COVERED_TEST · tests/governance/test_w806_append_witness_debt.py يحكُمُ على الشجرةِ الحاضرةِ (القياسُ المنشورُ يُطابِقُ الشجرةَ الحيّةَ) ويشملُه استدعاءُ `pytest` في CI · والقياسُ محروسٌ بعقدِ النسبِ في `measurement_provenance`.

يُشغَّلُ من جذرِ المستودع:
    python tools/audit/append_witness_debt.py            # طباعةٌ + مفتاحُ الدَّينِ
    python tools/audit/append_witness_debt.py --json OUT # + تفصيلٌ JSON
"""

from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

#: جذرُ شفرةِ الإنتاجِ الذي يُقاسُ (لا فحوصَ فيه ولا أدواتَ).
PRODUCTION_SRC = ROOT / "federal/executive/services/src/amos_federation"

#: أسماءُ نداءاتِ الشاهدِ — الإلحاقُ والنشرُ وتتبُّعُ النطاق.
WITNESS_CALLS = {"record_domain_trace", "publish", "append"}

#: مُستقبِلاتُ الشاهدِ — لا يُعَدُّ النداءُ شاهدًا إلّا على مُستقبِلٍ من هذا الجنسِ
#: (أو باسمِ الشاهدِ الصريحِ `record_domain_trace`).
WITNESS_RECEIVER = ("audit", "bus", "publisher", "event")

#: فئاتُ التصنيفِ الثلاثُ — نصوصُها هي المفاتيحُ في القياسِ المنشورِ.
CATEGORY_NESTED = "داخلَ مطبِّقٍ متداخلٍ في عمليّةٍ محروسةٍ"
CATEGORY_GUARDED_BODY = "في جسدِ عمليّةٍ محروسةٍ خارجَ المتداخلة"
CATEGORY_OUTSIDE = "خارجَ أيِّ عمليّةٍ محروسةٍ"


def _is_witness_call(call: ast.Call) -> bool:
    f = call.func
    name = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")
    if name not in WITNESS_CALLS:
        return False
    if name == "record_domain_trace":
        return True
    if isinstance(f, ast.Attribute):
        receiver = ast.unparse(f.value).lower()
        return any(token in receiver for token in WITNESS_RECEIVER)
    return False


def _stable_key(path: Path, stack: list[ast.FunctionDef | ast.AsyncFunctionDef]) -> str:
    """مفتاحٌ ثابتٌ (ملفٌّ · دالّةٌ خارجيّةٌ) — لا رقمَ سطرٍ ولا إحداثيَّ متحرّكًا."""
    outer = stack[0].name if stack else "<module>"
    return f"{path.relative_to(ROOT)}::{outer}"


def _classify(
    source: str,
    stack: list[ast.FunctionDef | ast.AsyncFunctionDef],
) -> str:
    if not stack:
        return CATEGORY_OUTSIDE
    outer = stack[0]
    guarded = "guard_declared(" in (ast.get_source_segment(source, outer) or "")
    if guarded and len(stack) > 1:
        return CATEGORY_NESTED
    if guarded:
        return CATEGORY_GUARDED_BODY
    return CATEGORY_OUTSIDE


def measure() -> dict[str, object]:
    """القياسُ الخامُّ — يقرأُ الشجرةَ الحيّةَ لا ملفًّا منشورًا."""
    counts = {
        CATEGORY_NESTED: 0,
        CATEGORY_GUARDED_BODY: 0,
        CATEGORY_OUTSIDE: 0,
    }
    outside_keys: list[str] = []
    for p in sorted(PRODUCTION_SRC.rglob("*.py")):
        if "tests" in p.parts:
            continue
        source = p.read_text(encoding="utf-8")
        tree = ast.parse(source)

        def visit(
            node: ast.AST, stack: list[ast.FunctionDef | ast.AsyncFunctionDef]
        ) -> None:
            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    visit(child, [*stack, child])
                    continue
                if isinstance(child, ast.Call) and _is_witness_call(child):
                    category = _classify(source, stack)
                    counts[category] += 1
                    if category == CATEGORY_OUTSIDE:
                        outside_keys.append(_stable_key(p, stack))
                visit(child, stack)

        visit(tree, [])
    return {
        "counts": counts,
        "total_calls": sum(counts.values()),
        "named_debt": len(outside_keys),
        "outside_debt_keys": outside_keys,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="الدَّينُ المسمّى: شهودُ الإلحاقِ بموقعِها")
    ap.add_argument("--json", dest="json_out", default=None, help="مسارُ ملفِّ التفصيلِ")
    args = ap.parse_args()

    result = measure()
    counts = result["counts"]
    assert isinstance(counts, dict)
    print("== الدَّينُ المسمّى: نداءاتُ شهودِ الإلحاقِ في الإنتاجِ ==")
    for category in (CATEGORY_NESTED, CATEGORY_GUARDED_BODY, CATEGORY_OUTSIDE):
        print(f"  {category}: {counts[category]}")
    print(f"  المجموعُ: {result['total_calls']} · الدَّينُ المسمّى: {result['named_debt']}")

    if args.json_out:
        # المادةُ التاسعةُ · 2: المُخرَجُ يُعلِنُ هدفَه في ترويستِه.
        payload = {
            "$comment": (
                "الهدف: قياسُ الدَّينِ المسمّى — نداءاتُ شهودِ الإلحاقِ (ج-1)(أ) في "
                "الإنتاجِ مصنَّفةً بموقعِها من العمليّاتِ المحروسة. مُخرَجُ "
                "tools/audit/append_witness_debt.py --json (§ 3 من A1_CD_DESIGN.md · "
                "W-806). والمفاتيحُ ثابتةٌ (ملفٌّ · دالّةٌ خارجيّةٌ) ولا تحملُ رقمَ "
                "سطرٍ (DISC-039). والتصنيفُ ساكنٌ بالنصِّ: guard_declared( في جسدِ "
                "الدالّةِ الخارجيّةِ — حدٌّ مُعلَنٌ لا اجتهادَ أداة."
            ),
            **result,
        }
        Path(args.json_out).write_text(
            json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        print(f"  التفصيلُ محفوظٌ في: {args.json_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
