"""مسبارُ أفعالِ دفعةِ المعجم (Q-77 ② · Q-78 ③ · Q-80 ②) — قبلَ الشِّفرة.

الهدف: قياسُ ما يُعطاه الفاعلُ التنفيذيُّ لكلِّ فعلٍ هدفٍ في القراراتِ الثلاثة، ومستوى القاطعِ
       الذي يمنعُه (KILL_SWITCH_BLOCKS)، وحجزُه البشريُّ (HUMAN_GATED_ACTIONS) — لا افتراضُها.
النطاق: `request_permit` بفاعلِ EXECUTIVE على هدفٍ وهميٍّ — قرارٌ بلا مُطبِّقٍ ولا كتابةٍ في المشروع؛
        قاعدةُ البياناتِ ملفٌّ مؤقّتٌ في /tmp. ومستوى القاطعِ يُقرأ من جدولِ المحرّكِ نفسِه.
المالك: Perplexity Computer (قيدُ W-749 · WI-120).
تاريخ الإنشاء: 2026-10-30
التشغيل (من federal/executive/services):
    ../../../.venv/bin/python ../../../docs/audit/evidence/W-749/probe_lexicon_actions.py
"""

import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("AMOS_DATABASE_URL", "sqlite:///" + tempfile.mktemp(suffix=".db"))
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from core.constitutional_engine import rules  # noqa: E402

from amos_federation.services.executive_core.sovereignty_bridge import (  # noqa: E402
    ConstitutionalAuthorizer,
    declared_effect,
)

PROBE_CASES = (  # (W-750) أُعيدَت تسميتُه من ROWS: الاسمُ القديمُ طابقَ كاشفَ HARDCODED_TRUTH (ratchet 2→3)
    ("create_batch (Q-77 ②)", "create_task"),
    ("enroll_batch (Q-77 ②)", "spawn_agent"),
    ("graduate_batch (Q-78 ③)", "activate_agent"),
    ("complete_training (Q-78 ③)", "activate_agent"),
    ("evaluate_model (Q-80 ②)", "record_curriculum_step"),
    ("— مرجعٌ: اليومَ (graduate/complete)", "release_agent"),
    ("— مرجعٌ: § 2.2 الأصلُ (create/enroll)", "spawn_population"),
    ("— مرجعٌ: § 2.2 الأصلُ (evaluate/start)", "train_model"),
    ("— مرجعٌ: Q-76 (W-724)", "graceful_shutdown"),
)


def _levels(action: str) -> str:
    blocks = rules.KILL_SWITCH_BLOCKS
    hit = sorted(lvl for lvl, acts in blocks.items() if action in acts)
    return f"≥{hit[0]}" if hit else "لا منعَ عندَ أيِّ مستوى"


def main() -> None:
    authorizer = ConstitutionalAuthorizer()
    print("السطحُ\tالفعلُ\tEXECUTIVE بلا قاطع\tمستوى المنع\tمحجوزٌ بشريًّا")
    for surface, action in PROBE_CASES:
        effect = declared_effect("CREATE", "probe:w749/row", "مسبارٌ بلا مُطبِّق")
        try:
            authorizer.request_permit(action, "probe:w749", declared_effects=(effect,))
            verdict = "PERMIT"
        except Exception as exc:  # noqa: BLE001 — المسبارُ يُبلغُ الرفضَ ولا يبتلعُه
            rule = next((r for r in ("R-001-1", "R-003-1", "R-002") if r in str(exc)), "?")
            verdict = f"DENY {type(exc).__name__} {rule}"
        gated = "نعم" if action in rules.HUMAN_GATED_ACTIONS else "لا"
        print(f"{surface}\t{action}\t{verdict}\t{_levels(action)}\t{gated}")


if __name__ == "__main__":
    main()
