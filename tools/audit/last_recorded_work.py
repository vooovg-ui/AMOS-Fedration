#!/usr/bin/env python3
"""الهدف: طبعُ **آخرِ لقطةِ انحرافِ دَينٍ منسوبةٍ إلى عملٍ** من سجلِّ بوّابةِ القرارِ.

## هدفُ هذا الملفِّ (المادة التاسعة · 2)

أداةُ قراءةٍ واحدةُ الغرضِ: تفتحُ
`docs/audit/measurements/decision_gate_ledger.json` — وهو **خرجٌ مولَّدٌ** بأداتِه
`tools/audit/decision_gate.py` — وتطبعُ حقلًا واحدًا من آخرِ لقطةٍ نوعُها
`work_drift`. لا تكتبُ شيئًا ولا تُصلِحُ شيئًا ولا تخترعُ قيمةً: إن لم تكن هناك
لقطةُ عملٍ سقطتْ مُعلِنةً ذلك.

## بأيِّ سلطةٍ وُجِدَت (W-033)

كانت خطوةُ CI في `.github/workflows/measure.yml` تكتبُ رقمَ القيدِ **بيدٍ**
(`--record-work W-031`). فلمّا سُجِّلَت لقطةُ `W-032` سقطتِ الخطوةُ في `main`،
لأنَّ الأداةَ ترفضُ لقطةً فوقَ لقطةٍ سابقةٍ بدَينٍ مختلفٍ — وهو رفضٌ **صحيحٌ**
سقطَ على مَن كتبَ الرقمَ لا على مَن قاسَه. وكانَ أمامَ العاملِ طريقانِ: أن
يُبدِّلَ الرقمَ في كلِّ موجةٍ (فيبقى العيبُ ينتظرُ الموجةَ التاليةَ)، أو أن
يُقرأَ القيدُ من مصدرِه المولَّدِ. فاختيرَ الثاني: **لا رقمَ بلا أداتِه** — وهي
القاعدةُ نفسُها التي تمنعُ تحريرَ الخرجِ المولَّدِ بيدٍ.

فتصيرُ خطوةُ CI **حرسًا** لا تصريحًا: إن طابقَ الدَّينُ آخرَ لقطةٍ فلا كتابةَ،
وإن انحرفَ بلا قيدٍ جديدٍ في `COMPLETION_LEDGER.md` سقطتِ الخطوةُ مُعلِنةً
الانحرافَ.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

#: مسارُ السجلِّ المولَّدِ — يُقرأُ ولا يُكتَبُ من هنا.
LEDGER_PATH = Path("docs/audit/measurements/decision_gate_ledger.json")

#: نوعُ اللقطةِ المنسوبةِ إلى عملٍ (تُميِّزُها من لقطاتِ إغلاقِ القرارات).
WORK_KIND = "work_drift"

#: الحقولُ التي يجوزُ طلبُها — قائمةٌ مُعلَنةٌ فلا يُطلَبُ حقلٌ غيرُ مقصودٍ.
ALLOWED_FIELDS = ("decision", "reason", "debt", "git_head", "recorded_at")


def last_work_snapshot(ledger_path: Path = LEDGER_PATH) -> dict[str, object]:
    """آخرُ لقطةِ عملٍ في السجلِّ — أو سقوطٌ مُعلِنٌ إن لم توجَدْ."""
    if not ledger_path.exists():
        raise SystemExit(f"لا سجلَّ لقطاتٍ في {ledger_path} — يُولَّدُ بـ decision_gate.py")
    data = json.loads(ledger_path.read_text(encoding="utf-8"))
    snapshots = [s for s in data.get("snapshots", []) if s.get("kind") == WORK_KIND]
    if not snapshots:
        raise SystemExit(
            f"لا لقطةَ عملٍ (kind={WORK_KIND}) في {ledger_path} — لا شيءَ يُعادُ تسجيلُه"
        )
    return snapshots[-1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="حقلٌ واحدٌ من آخرِ لقطةِ انحرافِ دَينٍ منسوبةٍ إلى عمل"
    )
    parser.add_argument(
        "--field",
        required=True,
        choices=ALLOWED_FIELDS,
        help="الحقلُ المطلوبُ طبعُه بلا زخرفةٍ (لِيُقرأَ في سكربتٍ)",
    )
    args = parser.parse_args(argv)
    snapshot = last_work_snapshot()
    value = snapshot.get(args.field)
    if value is None:
        raise SystemExit(
            f"الحقلُ {args.field} غيرُ موجودٍ في آخرِ لقطةِ عملٍ — لا قيمةَ تُخترَعُ"
        )
    print(value)
    return 0


if __name__ == "__main__":
    sys.exit(main())
