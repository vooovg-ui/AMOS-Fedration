#!/usr/bin/env python3
"""
قياسُ فرقِ جدولَي التسعيرِ — Pricing Divergence Measurement (Q-42 · الشقُّ الأوّلُ · W-036)
الهدف: أن يكونَ الفرقُ بينَ جدولَي تسعيرِ الرموزِ في بوّابةِ النماذجِ **مقيسًا مُقيَّدًا منشورًا** لا مستورًا، تنفيذًا لحسمِ المالكِ في Q-42 (ج): «يُقَرُّ الجدولانِ ويُقيَّدُ الفرقُ».
النطاق: federal/executive/services/src/amos_federation/services/model_gateway/{main.py,model_layer.py}
المالك: tools/governance/
تاريخ الإنشاء: 2026-08-24 (W-036)
تاريخ آخر تعديل: 2026-08-24 (W-036)

## بأيِّ سلطةٍ وُجِدَت هذه الأداةُ

بنصِّ المالكِ في Q-42 · الشقِّ الأوّلِ · الخيارِ (ج) بتاريخ 2026-08-24 المُقيَّدِ في
`docs/audit/SOVEREIGN_DECISION_REGISTER.md`: **«يُقَرُّ الجدولانِ ويُقيَّدُ الفرقُ»**.
فالمطلوبُ ليسَ توحيدًا ولا حذفًا — بل **قيدُ الفرقِ**. وقيدُ فرقٍ بيدٍ في وثيقةٍ
يتقادَمُ بأوّلِ تعديلِ سعرٍ، فالقيدُ **قياسٌ من المصدرِ** يُعادُ توليدُه ويُحرَسُ
من التقادمِ، ومعَه حرسٌ يُثبِّتُ الفرقَ فلا يتبدَّلُ صامتًا.

## ما تقيسُه (ولا تحكمُ)

`COST_PER_1K_TOKENS` في `main.py` هو جدولُ **مسارِ النداءِ** — الطريقُ الذي يكتبُ
قيدَ المالِ في `model_cost_log`. و`PRICING` في `model_layer.py` هو جدولُ **طبقةِ
النماذجِ**. والفرقُ بينَهما ثلاثةُ أوجهٍ، كلُّها مقيسةٌ هنا:

1. **فرقُ شكلٍ (`shape`)** — جدولُ مسارِ النداءِ سعرٌ **واحدٌ مسطَّحٌ** للنموذجِ،
   وجدولُ الطبقةِ **سعرانِ** (‏`input` و`output`). فليسَ الاختلافُ في رقمٍ بل في
   بنيةِ التسعيرِ نفسِها، ولا يُردمُ بمقارنةِ قيمتَينِ.
2. **فرقُ سعرٍ للمشتركِ (`rate`)** — لكلِّ نموذجٍ في الجدولَينِ: أيَّ سعرٍ من
   سعرَي الطبقةِ يُطابِقُ السعرَ المسطَّحَ، ونسبةُ المسطَّحِ إلى سعرِ الدَخلِ.
3. **فرقُ تغطيةٍ (`coverage`)** — نموذجٌ مُسعَّرٌ في جدولٍ وغائبٌ عن الآخرِ.
   والغيابُ ليسَ حياديًّا: مسارُ النداءِ يقرأُ بـ`.get(model, 0.0)`، فنموذجٌ
   غائبٌ عن جدولِه **يُسعَّرُ صفرًا** — أي يُقيَّدُ مجّانًا وهو ليسَ كذلك.

## ما لا تفعلُه هذه الأداةُ صريحًا

- **لا تُوحِّدُ الجدولَينِ ولا تُعدِّلُ سعرًا.** التوحيدُ خيارٌ (أ) أو (ب) وقد
  رُدَّ بنصِّ المالكِ، وتعديلُ سعرٍ قرارُ مالٍ لا حكمُ أداةٍ.
- **لا تدَّعي أنَّ أحدَ الجدولَينِ صحيحٌ والآخرَ خطأٌ.** الحسمُ أقرَّهما كلَيهما،
  فالأداةُ تُظهِرُ الأثرَ المالي للفرقِ ولا تُصدِرُ فيه حكمًا.
- **لا تقرأُ الجدولَينِ باستيرادِ الوحدةِ** بل بالتحليلِ النحويِّ (`ast`): استيرادُ
  `main.py` يُشعِلُ تطبيقَ الخدمةِ وقاعدتَها، فيصيرُ القياسُ رهنَ بيئةٍ. والقراءةُ
  من المصدرِ تعملُ في أيِّ بيئةٍ وتُطابِقُ ما يُراجَعُ في الطلبِ.

## حدُّ صدقِها (يُقالُ ولا يُوارى)

تقيسُ الأداةُ **الجدولَينِ الحرفيَّينِ** في موضعَيهما. فلو صارَ سعرٌ يُقرأُ من
إعدادٍ أو من قاعدةٍ في المستقبلِ (‏وهو خيارُ (ب) الذي لم يُختَرْ) لم تَرَه هذه
الأداةُ، وسقطَ الحرسُ الساكنُ الذي يُثبِّتُ وجودَ الجدولَينِ فلَزِمَ قرارٌ مكتوبٌ.
ولا تقيسُ الأداةُ **أيُّ الجدولَينِ يُستعمَلُ فعلًا في نداءٍ حيٍّ** — ذاكَ يقيسُه
حرسُ `tests/test_w036_cost_precision_and_pricing_divergence.py` بنداءٍ حقيقيٍّ.

Usage:
    python tools/governance/pricing_divergence.py [REPO_ROOT] [--json] [--check]

    --json   اطبعِ القياسَ كاملًا JSON على المخرجِ القياسيّ.
    --check  اخرجْ بفشلٍ إن كانَ القياسُ المنشورُ متقادمًا عن المصدرِ، ولا يكتبْ
             شيئًا: يحكمُ ويُعلِنُ الفرقَ حقلًا حقلًا (نفسُ عقدِ W-035).

المخرجات:
    docs/audit/measurements/pricing_divergence.json
"""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path
from typing import Any

#: موضعُ جدولِ مسارِ النداءِ واسمُه — الطريقُ الذي يكتبُ قيدَ المالِ.
CALL_PATH_FILE = (
    "federal/executive/services/src/amos_federation/services/model_gateway/main.py"
)
CALL_PATH_TABLE = "COST_PER_1K_TOKENS"

#: موضعُ جدولِ طبقةِ النماذجِ واسمُه.
LAYER_FILE = (
    "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py"
)
LAYER_TABLE = "PRICING"

#: عددُ الرموزِ الذي يُسعَّرُ به كلا الجدولَينِ — ألفُ رمزٍ في كلَيهما.
TOKENS_PER_UNIT = 1000


class PricingReadError(RuntimeError):
    """تعذَّرَ استخراجُ جدولِ تسعيرٍ من موضعِه — لا يُفترَضُ جدولٌ فارغٌ بديلًا عنه."""


def _read_table(root: Path, rel_path: str, name: str) -> dict[str, Any]:
    """استخرِجْ قاموسَ تسعيرٍ من المصدرِ بالتحليلِ النحويِّ لا بالاستيراد.

    يُبحَثُ عن الإسنادِ في مستوى الوحدةِ **وفي جسمِ الصنفِ** معًا، لأنَّ
    `PRICING` عضوُ صنفٍ (`ModelLayer.PRICING`) و`COST_PER_1K_TOKENS` ثابتُ وحدةٍ.
    فمُطابِقٌ يقرأُ مستوى الوحدةِ وحدَه كانَ سيُعيدُ «لا جدولَ» عن جدولٍ قائمٍ —
    وهو أسوأُ من الفشلِ لأنَّه يُقرأُ نفيًا.

    Raises:
        PricingReadError: الملفُّ غيرُ موجودٍ، أو لا إسنادَ بهذا الاسمِ، أو قيمتُه
            ليست حرفيّةً يُمكِنُ تقييمُها بأمانٍ.
    """
    path = root / rel_path
    if not path.exists():
        raise PricingReadError(f"موضعُ جدولِ التسعيرِ غيرُ موجودٍ: {rel_path}")
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                try:
                    value = ast.literal_eval(node.value)
                except (ValueError, SyntaxError) as exc:
                    raise PricingReadError(
                        f"`{name}` في {rel_path} ليسَ قيمةً حرفيّةً تُقرأُ من المصدرِ: {exc}"
                    ) from exc
                if not isinstance(value, dict):
                    raise PricingReadError(
                        f"`{name}` في {rel_path} ليسَ قاموسًا بل {type(value).__name__}"
                    )
                return value
    raise PricingReadError(f"لا إسنادَ باسمِ `{name}` في {rel_path}")


def _rate_divergence(flat: float, split: dict[str, Any]) -> dict[str, Any]:
    """قِسْ فرقَ السعرِ لنموذجٍ مشتركٍ: أيَّ طرفٍ يُطابِقُ المسطَّحُ، وبأيِّ نسبةٍ.

    النسبةُ تُحسَبُ إلى سعرِ الدَخلِ لأنَّها **الأثرُ المالي** للفرقِ: مسارُ النداءِ
    يُسعِّرُ كلَّ رمزٍ بسعرٍ واحدٍ، فرمزُ دَخلٍ يُحاسَبُ بالمسطَّحِ لا بسعرِ الدَخلِ.
    """
    price_in = float(split.get("input", 0.0))
    price_out = float(split.get("output", 0.0))
    return {
        "flat_per_1k": flat,
        "layer_input_per_1k": price_in,
        "layer_output_per_1k": price_out,
        "flat_equals_layer_input": flat == price_in,
        "flat_equals_layer_output": flat == price_out,
        # `None` لا `0` ولا `1`: لا نسبةَ حينَ المقامُ صفرٌ، وادّعاءُ رقمٍ اختراعٌ.
        "flat_over_layer_input": (flat / price_in) if price_in else None,
        "input_token_overcharge": (flat - price_in) if flat != price_in else 0.0,
    }


def measure(root: Path) -> dict[str, Any]:
    """اقِسِ الفرقَ بأوجهِه الثلاثةِ وأعِدْ حِملًا واحدًا — لا حكمَ فيه ولا إصلاح."""
    call_path = _read_table(root, CALL_PATH_FILE, CALL_PATH_TABLE)
    layer = _read_table(root, LAYER_FILE, LAYER_TABLE)

    shared = sorted(set(call_path) & set(layer))
    only_call_path = sorted(set(call_path) - set(layer))
    only_layer = sorted(set(layer) - set(call_path))

    rate_divergence = {m: _rate_divergence(float(call_path[m]), layer[m]) for m in shared}

    # نموذجٌ مُسعَّرٌ بمالٍ حقيقيٍّ في الطبقةِ وغائبٌ عن جدولِ مسارِ النداءِ يُقيَّدُ
    # **صفرًا** في السجلِّ، لأنَّ القراءةَ هناكَ `.get(model, 0.0)`. وهذا أثرٌ مالي
    # لا نقصُ تغطيةٍ شكليٌّ، فيُفرَدُ بحقلٍ يُقرأُ وحدَه.
    priced_in_layer_free_in_call_path = sorted(
        m
        for m in only_layer
        if any(float(v) > 0 for v in layer[m].values())
    )

    nonzero_rates = [float(v) for v in call_path.values() if float(v) > 0] + [
        float(v) for d in layer.values() for v in d.values() if float(v) > 0
    ]
    smallest_rate = min(nonzero_rates) if nonzero_rates else 0.0

    return {
        # المادةُ التاسعةُ · 2: المُخرَجُ المُولَّدُ يُعلِنُ هدفَه في ترويستِه.
        "$comment": (
            "الهدف: قياسُ الفرقِ بينَ جدولَي تسعيرِ الرموزِ في بوّابةِ النماذجِ — "
            "مُخرَجُ tools/governance/pricing_divergence.py (Q-42 (ج) · W-036). "
            "المادةُ التاسعةُ · 2. لا يُحرَّرُ بيدٍ: يُعادُ توليدُه."
        ),
        "note": (
            "قياسٌ لا حُكم. أُقِرَّ الجدولانِ بنصِّ المالكِ في Q-42 (ج) فلا يُقرأُ "
            "هذا الملفُّ دعوةً لتوحيدِهما، ولا يُقرأُ شهادةَ صحّةِ سعرٍ: صحّةُ "
            "السعرِ نفسِه تلزمُها فاتورةُ مُزوِّدٍ لا مِلكَ هذا المستودعِ."
        ),
        "authority": (
            "حسمُ المالكِ في Q-42 · الشقُّ الأوّلُ · الخيارُ (ج) — 2026-08-24: "
            "«يُقَرُّ الجدولانِ ويُقيَّدُ الفرقُ». والمرجعُ: "
            "docs/audit/SOVEREIGN_DECISION_REGISTER.md § Q-42."
        ),
        "tables": {
            "call_path": {"file": CALL_PATH_FILE, "name": CALL_PATH_TABLE, "table": call_path},
            "layer": {"file": LAYER_FILE, "name": LAYER_TABLE, "table": layer},
        },
        "summary": {
            "shape_divergence": "flat_single_rate_vs_split_input_output",
            "tokens_per_unit": TOKENS_PER_UNIT,
            "models_in_call_path": len(call_path),
            "models_in_layer": len(layer),
            "models_shared": shared,
            "models_only_in_call_path": only_call_path,
            "models_only_in_layer": only_layer,
            "priced_in_layer_free_in_call_path": priced_in_layer_free_in_call_path,
            "shared_models_where_flat_equals_layer_output": sorted(
                m for m, d in rate_divergence.items() if d["flat_equals_layer_output"]
            ),
            "shared_models_where_flat_differs_from_layer_input": sorted(
                m for m, d in rate_divergence.items() if not d["flat_equals_layer_input"]
            ),
            "smallest_nonzero_rate_per_1k": smallest_rate,
            "smallest_nonzero_rate_per_token": smallest_rate / TOKENS_PER_UNIT,
        },
        "rate_divergence": rate_divergence,
    }


def _output_path(root: Path) -> Path:
    """موضعُ القياسِ المنشورِ — يُقرأُ منه ويُكتَبُ إليه بنفسِ الدالّة."""
    return root / "docs" / "audit" / "measurements" / "pricing_divergence.json"


def _comparable(payload: dict[str, Any]) -> str:
    """ثبِّتْ ترتيبَ الحِملِ للمقارنةِ.

    ولا حقلَ محليًّا للآلةِ يُجرَّدُ هنا: تعلَّمَت W-035 أنَّ حقلًا يحملُ مسارَ
    الآلةِ (`repo`) يُلوِّثُ القياسَ فيُقارَنُ بين آلتَينِ لا بين حالتَينِ — فهذا
    الحِملُ **لا يحملُ مسارًا مطلقًا أصلًا**، والمساراتُ فيه نسبيّةٌ من جذرِ المستودعِ.
    """
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def check_published_is_fresh(root: Path, fresh: dict[str, Any]) -> tuple[bool, str]:
    """أَيُطابِقُ القياسُ المنشورُ على القرصِ قياسًا طازجًا من المصدر؟

    نفسُ عقدِ بوّابةِ W-035: تحكمُ ولا تكتبُ. وبوّابةٌ تُصلِحُ ما تحكمُ عليهِ
    تُخفي التقادمَ بإزالتِه في نفسِ النَّفَسِ، فتمرُّ الدَّفعةُ والملفُّ لم يُلتَزم.
    """
    out = _output_path(root)
    if not out.exists():
        return False, f"القياسُ المنشورُ غيرُ موجودٍ: {out} — شغِّلِ الأداةَ بلا `--check`."
    try:
        published = json.loads(out.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return False, f"تعذَّرَ قراءةُ القياسِ المنشورِ ({out}): {exc}"
    if _comparable(published) != _comparable(fresh):
        pub = published.get("summary", {})
        now = fresh["summary"]
        diffs = [
            f"    - {key}: المنشورُ {pub.get(key)!r} · المقيسُ الآنَ {now.get(key)!r}"
            for key in sorted(set(now) | set(pub))
            if pub.get(key) != now.get(key)
        ]
        detail = "\n" + "\n".join(diffs) if diffs else "\n    - الفرقُ في التفاصيلِ لا في الملخَّصِ."
        return False, (
            f"القياسُ المنشورُ متقادمٌ ({out}): لا يُطابِقُ قياسًا طازجًا من المصدرِ.{detail}\n"
            "    والإصلاحُ توليدٌ لا تحريرٌ بيدٍ: "
            "`python tools/governance/pricing_divergence.py .`"
        )
    return True, f"القياسُ المنشورُ طازجٌ ويُطابِقُ المصدرَ: {out}"


def _write_json(root: Path, payload: dict[str, Any]) -> Path:
    """اكتبِ القياسَ إلى `docs/audit/measurements/` وأعِدْ مسارَه."""
    out = _output_path(root)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out


def main(argv: list[str]) -> int:
    """نقطةُ الدخول: اقرأِ الوسائطَ، اقِسْ، اطبعْ، واحكمْ إن طُلِبَ."""
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    root = Path(args[0]) if args else Path.cwd()

    try:
        payload = measure(root)
    except PricingReadError as exc:
        print(f"[PRICING DIVERGENCE] ✗ {exc}", file=sys.stderr)
        return 2

    if "--check" in flags:
        ok, message = check_published_is_fresh(root, payload)
        print(f"[PRICING DIVERGENCE --check] {'✓' if ok else '✗'} {message}")
        return 0 if ok else 1

    if "--json" in flags:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        s = payload["summary"]
        print(f"[PRICING DIVERGENCE] فرقُ الشكلِ: {s['shape_divergence']}")
        print(
            f"[PRICING DIVERGENCE] نماذجُ مسارِ النداءِ {s['models_in_call_path']} · "
            f"نماذجُ الطبقةِ {s['models_in_layer']} · مشتركةٌ {len(s['models_shared'])}"
        )
        for model, d in sorted(payload["rate_divergence"].items()):
            ratio = d["flat_over_layer_input"]
            ratio_text = "—" if ratio is None else f"×{ratio:g}"
            print(
                f"  - {model}: مسطَّحٌ {d['flat_per_1k']:g} · دَخلٌ {d['layer_input_per_1k']:g} · "
                f"خَرْجٌ {d['layer_output_per_1k']:g} · المسطَّحُ/الدَخلُ {ratio_text}"
            )
        print(f"  - مُسعَّرٌ في الطبقةِ ومجّانٌ في مسارِ النداءِ: "
              f"{', '.join(s['priced_in_layer_free_in_call_path']) or '—'}")
        print(f"  - أصغرُ سعرٍ غيرِ صفريٍّ للرمزِ: {s['smallest_nonzero_rate_per_token']:.10f}$")

    out = _write_json(root, payload)
    print(f"[PRICING DIVERGENCE] كُتب: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
