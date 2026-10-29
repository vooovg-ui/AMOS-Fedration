"""الهدف: قياسُ حكمِ المحرّكِ الدستوريِّ على فعلَي السطحَين 2 و4 من WI-114 (lower_kill_switch · promote_model)
لكلِّ تركيبةٍ من الفاعلِ والموافقةِ البشريّةِ والتوقيعِ والحرجيّةِ ومستوى القاطع — قبلَ أيِّ شِفرة (التوجيهُ 29 · D25-1).

النطاق: قراءةٌ فقط: `ConstitutionalEngine.evaluate` على سجلٍّ مؤقّتٍ في مجلدٍ مؤقّت؛ لا يمسُّ شِفرةَ الإنتاج ولا سجلَّها.
المالك: Perplexity Computer (قيدُ W-737 · WI-114).
تاريخ الإنشاء: 2026-10-29

التشغيلُ (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-737/engine_probe_surfaces_2_4.py
"""

from __future__ import annotations

import itertools
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        engine = ConstitutionalEngine(ledger_path=Path(tmp) / "ledger.jsonl")
        rows = 0
        for action, actor, approved, signed, crit, level in itertools.product(
            ("lower_kill_switch", "promote_model", "record_promotion_gate"),
            (Branch.EXECUTIVE, Branch.HUMAN),
            (False, True),
            (False, True),
            ("normal", "fateful"),
            (0, 3, 5),
        ):
            if signed and not approved:
                continue
            req = ActionRequest(
                actor=actor,
                action=action,
                target="probe",
                channel="api",
                human_approved=approved,
                human_signature="sig-probe" if signed else None,
                criticality=crit,
                kill_switch_level=level,
            )
            verdict = engine.evaluate(req)
            decision = getattr(verdict.decision, "value", verdict.decision)
            fired = [v.rule_id for v in getattr(verdict, "violations", [])] or getattr(
                verdict, "rules_triggered", []
            )
            print(
                f"{action:22} actor={actor.name:9} approved={approved!s:5} signed={signed!s:5} "
                f"crit={crit:7} level={level} → {decision} {fired}"
            )
            rows += 1
        print(f"PROBE SUMMARY: rows={rows}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
