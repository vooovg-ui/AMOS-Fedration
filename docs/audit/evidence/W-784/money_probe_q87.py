"""الهدف: قياسُ مِسبارِ المالِ بعدَ WI-126 (التوجيه 38 § 2 بند 3) قبلَ تصميمِ M1 الدفعة 2:
STATE وINSTITUTION يُرفَضانِ · HUMAN يحتاجُ موافقةً موسومةً · TREASURY يبقى مقبولًا.

النطاق: قراءةٌ فقط — `ConstitutionalEngine.evaluate` على سجلٍّ مؤقّتٍ في مجلدٍ مؤقّت؛ لا يمسُّ شِفرةَ الإنتاج.
يُكمِلُ `evidence/W-739/engine_probe_money_actor.py` (الذي لا يُمرِّرُ موافقةً) بثلاثِ صيغٍ لـHUMAN.
المالك: Perplexity Computer (WI-100 · التوجيه 38).

التشغيلُ (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-784/money_probe_q87.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402
from core.constitutional_engine.rules import TREASURY_ACTIONS  # noqa: E402

VARIANTS = {
    "TREASURY": dict(actor=Branch.TREASURY),
    "STATE": dict(actor=Branch.STATE),
    "INSTITUTION": dict(actor=Branch.INSTITUTION),
    "HUMAN·بلا موافقة": dict(actor=Branch.HUMAN),
    "HUMAN·موافقة بلا وسم": dict(actor=Branch.HUMAN, human_approved=True),
    "HUMAN·وسم فارغ": dict(
        actor=Branch.HUMAN,
        human_approved=True,
        metadata={"human_approval_source": "  "},
    ),
    "HUMAN·وسم بلا موافقة": dict(
        actor=Branch.HUMAN, metadata={"human_approval_source": "probe-ticket-1"}
    ),
    "HUMAN·موافقة موسومة": dict(
        actor=Branch.HUMAN,
        human_approved=True,
        metadata={"human_approval_source": "probe-ticket-1"},
    ),
}
EXPECT = {
    "TREASURY": "ALLOW",
    "STATE": "DENY",
    "INSTITUTION": "DENY",
    "HUMAN·بلا موافقة": "DENY",
    "HUMAN·موافقة بلا وسم": "DENY",
    "HUMAN·وسم فارغ": "DENY",
    "HUMAN·وسم بلا موافقة": "DENY",
    "HUMAN·موافقة موسومة": "ALLOW",
}


def main() -> int:
    actions = sorted(TREASURY_ACTIONS)
    print(f"TREASURY_ACTIONS ({len(actions)}): {actions}")
    tally: dict[str, dict[str, int]] = {}
    with tempfile.TemporaryDirectory() as tmp:
        engine = ConstitutionalEngine(ledger_path=Path(tmp) / "ledger.jsonl")
        for name, kw in VARIANTS.items():
            for action in actions:
                req = ActionRequest(action=action, target="probe", channel="api", **kw)
                v = engine.evaluate(req)
                d = str(getattr(v.decision, "value", v.decision)).upper()
                fired = [x.rule_id for x in getattr(v, "violations", [])] or getattr(
                    v, "rules_triggered", []
                )
                print(f"{name:22} {action:22} → {d} {fired}")
                tally.setdefault(name, {}).setdefault(d, 0)
                tally[name][d] += 1
    bad = 0
    for name, counts in tally.items():
        ok = counts.get(EXPECT[name], 0) == len(actions)
        bad += 0 if ok else 1
        print(
            f"SUMMARY {name:22} {counts} expected={EXPECT[name]}×{len(actions)} → {'MATCH' if ok else 'MISMATCH'}"
        )
    print(f"PROBE RESULT: variants={len(tally)} mismatches={bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
