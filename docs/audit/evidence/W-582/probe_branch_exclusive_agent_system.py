"""
الهدف: إعادةُ إنتاجِ القسمِ (د) من مخرجِ W-581 (ALLOW 54/54 لـAGENT وSYSTEM على أفعالِ _BRANCH_EXCLUSIVE) بسكربتٍ مُلتزَمٍ — فالسكربتُ المُلتزَمُ في W-581 لا يحوي القسمَ (د) (DISC-122)
النطاق: docs/audit/evidence/W-582 — قياسٌ بالمراجعةِ وحدَها (review_only) · لا كتابةَ ولا تنفيذَ
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — قيدُ W-582 · بتوجيهِ المالكِ 17
تاريخ الإنشاء: 2026-10-21

التشغيل:
  PYTHONPATH=federal/executive/services/src:. \
    .venv/bin/python docs/audit/evidence/W-582/probe_branch_exclusive_agent_system.py
"""

from __future__ import annotations

from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer
from core.constitutional_engine.rules import _BRANCH_EXCLUSIVE

ACTORS = ("AGENT", "SYSTEM")


def main() -> int:
    total = allow = 0
    print("## (د) review_only لكلِّ فعلٍ حصريٍّ في _BRANCH_EXCLUSIVE — الفاعلانِ AGENT وSYSTEM")
    for branch, actions in _BRANCH_EXCLUSIVE.items():
        for action in sorted(actions):
            cells = []
            for actor in ACTORS:
                ev = ConstitutionalAuthorizer(actor=actor).review_only(action, f"probe/w582/{action}")
                total += 1
                allow += ev.decision == "ALLOW"
                cells.append(f"{actor}={ev.decision}")
            print(f"{branch.value:<12} {action:<24} {' '.join(cells)}")
    print(f"ALLOW {allow}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
