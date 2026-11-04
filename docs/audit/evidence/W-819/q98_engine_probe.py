"""الهدف: مسبارُ المحرّكِ الخامُ للأفعالِ التسعةِ في `national_economy` (Q-98 بنهجِ Q-97 القيد (ج) · W-820).

يقرأُ `core/constitutional_engine/rules.py` **من القرص** كما هو في الشجرةِ المعطاة
(`--root`، والافتراضُ جذرُ هذا المستودع) — لا ترقيعَ في الذاكرة — ويُقيِّمُ بـ
`ConstitutionalEngine.evaluate` لكلِّ فعلٍ عشرةَ فاعلين:
  - المقبول: EXECUTIVE وحدَه (ALLOW)،
  - المرفوضون التسعة: LEGISLATIVE · JUDICIAL · TREASURY · ROYAL · HUMAN · STATE ·
    INSTITUTION · AGENT · SYSTEM (DENY).
ومعه حكمُ EXECUTIVE عندَ مستوياتِ مفتاحِ الإيقافِ 0–5 (تُطبَعُ قياسًا — الأفعالُ ليست
في `KILL_SWITCH_BLOCKS` بقرارِ التصميم § 7.4، فلا يُشترطُ فيها حكم).

الخروج: 0 إن طابقَ كلُّ فعلٍ «1 مقبول + 9 مرفوضون»، وإلّا 1 — وبه تُقاسُ الطفرةُ (هـ):
حذفُ فعلٍ من `EXECUTIVE_ACTIONS` في نسخةٍ مؤقّتةٍ يجبُ أن يُخرِجَ 1.

النطاق: قراءةٌ فقط — سجلُّ المحرّكِ في مجلدٍ مؤقّت.
المالك: Perplexity Computer (WI-127 · قرارُ Q-98 · التوجيه 43 § 2 · قيدُ W-820).

التشغيل (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-819/q98_engine_probe.py [--root <شجرة>]
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

VERBS = (
    "register_sector",
    "register_category",
    "define_indicator",
    "register_public_entity",
    "create_program",
    "issue_policy",
    "register_revenue_source",
    "register_public_asset",
    "register_public_liability",
)
ALLOWED = "EXECUTIVE"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[4]))
    root = Path(parser.parse_args().root).resolve()
    sys.path.insert(0, str(root))

    from core.constitutional_engine import rules
    from core.constitutional_engine.engine import ConstitutionalEngine
    from core.constitutional_engine.model import ActionRequest, Branch

    print(f"RULES FILE: {Path(rules.__file__).resolve()}")
    actors = [
        Branch.EXECUTIVE,
        Branch.LEGISLATIVE,
        Branch.JUDICIAL,
        Branch.TREASURY,
        Branch.ROYAL,
        Branch.HUMAN,
        Branch.STATE,
        Branch.INSTITUTION,
        Branch.AGENT,
        Branch.SYSTEM,
    ]
    blocked = sorted(set(VERBS) & set().union(*rules.KILL_SWITCH_BLOCKS.values()))
    print(f"IN KILL_SWITCH_BLOCKS: {blocked}")

    def verdict(engine, actor, action, level=0) -> str:
        v = engine.evaluate(
            ActionRequest(
                actor=actor,
                action=action,
                target="probe",
                channel="official",
                kill_switch_level=level,
            )
        )
        d = str(getattr(v.decision, "value", v.decision)).upper()
        fired = sorted({x.rule_id for x in getattr(v, "violations", [])})
        return d if not fired else f"{d}{fired}"

    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        engine = ConstitutionalEngine(ledger_path=Path(tmp) / "ledger.jsonl")
        for verb in VERBS:
            owner = rules._exclusive_owner(verb)
            row = {a.name: verdict(engine, a, verb) for a in actors}
            allowed = [a for a, v in row.items() if v == "ALLOW"]
            denied = [a for a, v in row.items() if v.startswith("DENY")]
            ok = allowed == [ALLOWED] and len(denied) == 9
            bad += 0 if ok else 1
            levels = " ".join(
                f"L{lvl}={verdict(engine, Branch.EXECUTIVE, verb, lvl)}"
                for lvl in range(6)
            )
            print(
                f"{'OK ' if ok else 'BAD'} {verb:24} owner={owner.name if owner else '—':10} "
                f"allowed={allowed} denied={len(denied)}/9"
            )
            print("     " + " ".join(f"{a}={v}" for a, v in row.items()))
            print(f"     EXECUTIVE kill-switch: {levels}")
    print(f"PROBE RESULT: verbs={len(VERBS)} mismatched={bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
