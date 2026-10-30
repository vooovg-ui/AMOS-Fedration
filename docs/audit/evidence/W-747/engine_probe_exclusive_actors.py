"""الهدف: قياسُ حكمِ المحرّكِ الدستوريِّ على كلِّ فعلٍ حصريٍّ في المعاجمِ الأربعةِ لكلِّ فاعلٍ —
قبلَ شِفرةِ Q-68 وبعدَها (التوجيهُ 32 § 1 · Q-68 الخيارُ 1 · R-003-1 · DISC-121).

النطاق: قراءةٌ فقط: `ConstitutionalEngine.evaluate` على سجلٍّ مؤقّتٍ في مجلدٍ مؤقّت؛ لا يمسُّ شِفرةَ
الإنتاجِ ولا سجلَّها. امتدادٌ لمسبارِ M1 (evidence/W-739/engine_probe_money_actor.py · 150 صفًّا)
من معجمِ المالِ وحدَه إلى المعاجمِ الأربعةِ في `_BRANCH_EXCLUSIVE`.
المالك: Perplexity Computer (قيدُ W-747 · WI-124).
تاريخ الإنشاء: 2026-10-30

التشغيلُ (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-747/engine_probe_exclusive_actors.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402
from core.constitutional_engine.rules import _BRANCH_EXCLUSIVE  # noqa: E402


def main() -> int:
    actors = list(Branch)
    print(f"Branch members ({len(actors)}): {[b.name for b in actors]}")
    for owner, actions in _BRANCH_EXCLUSIVE.items():
        print(f"LEXICON {owner.name} ({len(actions)}): {sorted(actions)}")
    rows = 0
    allow: dict[tuple[str, str], int] = {}
    sizes: dict[str, int] = {}
    with tempfile.TemporaryDirectory() as tmp:
        engine = ConstitutionalEngine(ledger_path=Path(tmp) / "ledger.jsonl")
        for owner, actions in _BRANCH_EXCLUSIVE.items():
            sizes[owner.name] = len(actions)
            for action in sorted(actions):
                for actor in actors:
                    req = ActionRequest(actor=actor, action=action, target="probe", channel="api")
                    verdict = engine.evaluate(req)
                    decision = str(getattr(verdict.decision, "value", verdict.decision)).upper()
                    fired = [v.rule_id for v in getattr(verdict, "violations", [])]
                    print(f"{owner.name:11} {action:24} actor={actor.name:11} → {decision} {fired}")
                    key = (owner.name, actor.name)
                    allow.setdefault(key, 0)
                    if decision == "ALLOW":
                        allow[key] += 1
                    rows += 1
        # مسارُ المرسومِ الموقَّعِ (Q-68: «عدا مرسوم ملكي موقع كما هو اليوم»): البوّابةُ السياديّةُ
        # تمرِّرُ sovereign=True بعدَ ثبوتِ توقيعِ Ed25519 — فالقاعدةُ ذاتُ الأثرِ ADVISORY تُدرَجُ رأيًا لا منعًا.
        sov_allow = {"AGENT": 0, "SYSTEM": 0}
        sov_rows = 0
        for owner, actions in _BRANCH_EXCLUSIVE.items():
            for action in sorted(actions):
                for actor in (Branch.AGENT, Branch.SYSTEM):
                    req = ActionRequest(actor=actor, action=action, target="probe", channel="api")
                    verdict = engine.evaluate(req, sovereign=True)
                    decision = str(getattr(verdict.decision, "value", verdict.decision)).upper()
                    adv = [v.rule_id for v in getattr(verdict, "advisory_violations", [])]
                    print(f"SOVEREIGN {owner.name:11} {action:24} actor={actor.name:6} → {decision} advisory={adv}")
                    sov_rows += 1
                    if decision == "ALLOW":
                        sov_allow[actor.name] += 1
    print(f"SOVEREIGN (signed-decree path) rows={sov_rows} ALLOW AGENT={sov_allow['AGENT']} SYSTEM={sov_allow['SYSTEM']}")
    print("ALLOW matrix (lexicon × actor · ALLOW/size):")
    header = "  " + " ".join(f"{a.name[:6]:>6}" for a in actors)
    print(f"{'':11}{header}")
    for owner in _BRANCH_EXCLUSIVE:
        cells = " ".join(f"{allow[(owner.name, a.name)]:>3}/{sizes[owner.name]:<2}" for a in actors)
        print(f"{owner.name:11}   {cells}")
    total = sum(sizes.values())
    for name in ("AGENT", "SYSTEM", "HUMAN", "STATE", "INSTITUTION"):
        n = sum(allow[(o.name, name)] for o in _BRANCH_EXCLUSIVE)
        print(f"ALLOW for {name} on exclusive acts: {n}/{total}")
    print(f"PROBE SUMMARY: lexicons={len(_BRANCH_EXCLUSIVE)} actions={total} actors={len(actors)} rows={rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
