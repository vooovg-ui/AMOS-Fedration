"""الهدف: قياسُ حكمِ المحرّكِ الدستوريِّ على أفعالِ المالِ التي سيحملُها غلافُ M1 لكلِّ فاعل —
قبلَ أيِّ شِفرة (التوجيهُ 29 · D30 · WI-122 · Q-9 § 3.5 «فاعلُ المال» · R-003-1).

النطاق: قراءةٌ فقط: `ConstitutionalEngine.evaluate` على سجلٍّ مؤقّتٍ في مجلدٍ مؤقّت؛ لا يمسُّ شِفرةَ الإنتاج ولا سجلَّها.
المالك: Perplexity Computer (قيدُ W-739 · WI-122).
تاريخ الإنشاء: 2026-10-29

التشغيلُ (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-739/engine_probe_money_actor.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402
from core.constitutional_engine.rules import (  # noqa: E402
    MONEY_OPERATION_LEXICON,
    TREASURY_ACTIONS,
)


def main() -> int:
    actions = sorted(TREASURY_ACTIONS)
    print(f"TREASURY_ACTIONS ({len(actions)}): {actions}")
    print(f"MONEY_OPERATION_LEXICON ({len(MONEY_OPERATION_LEXICON)}): {MONEY_OPERATION_LEXICON}")
    actors = [b for b in Branch]
    print(f"Branch members: {[b.name for b in actors]}")
    rows = 0
    allow = {}
    with tempfile.TemporaryDirectory() as tmp:
        engine = ConstitutionalEngine(ledger_path=Path(tmp) / "ledger.jsonl")
        for action in actions:
            for actor in actors:
                req = ActionRequest(actor=actor, action=action, target="probe", channel="api")
                verdict = engine.evaluate(req)
                decision = getattr(verdict.decision, "value", verdict.decision)
                fired = [v.rule_id for v in getattr(verdict, "violations", [])] or getattr(
                    verdict, "rules_triggered", []
                )
                print(f"{action:22} actor={actor.name:10} → {decision} {fired}")
                allow.setdefault(actor.name, 0)
                if str(decision).upper() == "ALLOW":
                    allow[actor.name] += 1
                rows += 1
    print(f"ALLOW per actor (of {len(actions)}): {allow}")
    print(f"PROBE SUMMARY: rows={rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
