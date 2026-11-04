"""الهدف: مسبارُ المحرّكِ الخامُ لأفعالِ الخزانةِ الثلاثةِ في `national_economy` (Q-99 · التوجيه 44 § 2 · W-823).

يقرأُ `core/constitutional_engine/rules.py` **من القرص** كما هو في الشجرةِ المعطاة
(`--root`، والافتراضُ جذرُ هذا المستودع) — لا ترقيعَ في الذاكرة — ويُقيِّمُ بـ
`ConstitutionalEngine.evaluate` لكلِّ فعلٍ عشرةَ فاعلين:
  - المقبول: TREASURY وحدَه (ALLOW)،
  - المرفوضون التسعة: EXECUTIVE · LEGISLATIVE · JUDICIAL · ROYAL · HUMAN · STATE ·
    INSTITUTION · AGENT · SYSTEM (DENY).
ومعه حكمُ TREASURY عندَ مستوياتِ مفتاحِ الإيقافِ 0–5 (قياسٌ يُطبَع).
والأفعالُ: `authorize_expenditure` (قائم) · `award_procurement` (قائم) · `authorize_transfer` (جديدٌ بـQ-99).

الخروج: 0 إن طابقَ كلُّ فعلٍ «1 مقبول + 9 مرفوضون»، وإلّا 1 — وبه تُقاسُ الطفرة:
حذفُ فعلٍ من `TREASURY_ACTIONS` في نسخةٍ مؤقّتةٍ يجبُ أن يُخرِجَ 1.

النطاق: قراءةٌ فقط — سجلُّ المحرّكِ في مجلدٍ مؤقّت.
المالك: Perplexity Computer (WI-127 · قرارُ Q-99 · التوجيه 44 § 2 · قيدُ W-823).

التشغيل (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-823/q99_engine_probe.py [--root <شجرة>]
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

VERBS = (
    "authorize_expenditure",
    "award_procurement",
    "authorize_transfer",
)
ALLOWED = "TREASURY"


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
        Branch.TREASURY,
        Branch.EXECUTIVE,
        Branch.LEGISLATIVE,
        Branch.JUDICIAL,
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
                f"L{lvl}={verdict(engine, Branch.TREASURY, verb, lvl)}"
                for lvl in range(6)
            )
            print(
                f"{'OK ' if ok else 'BAD'} {verb:24} owner={owner.name if owner else '—':10} "
                f"allowed={allowed} denied={len(denied)}/9"
            )
            print("     " + " ".join(f"{a}={v}" for a, v in row.items()))
            print(f"     TREASURY kill-switch: {levels}")
    print(f"PROBE RESULT: verbs={len(VERBS)} mismatched={bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
