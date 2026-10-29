"""مسبارُ أفعالِ الدفعةِ 4 (learning_cycle + security) — قبلَ الشِّفرة.

الهدف: قياسُ ما يُعطاه الفاعلُ التنفيذيُّ لكلِّ فعلٍ في جدولِ G1 § 2.2 للأسطحِ الأحدَ عشرَ، وأدنى مستوى
       يمنعُه زرُّ الإيقافِ (`KILL_SWITCH_BLOCKS` · الدلالةُ التراكميّةُ § 9.3) — لا افتراضُهما.
النطاق: `request_permit` بفاعلِ EXECUTIVE على هدفٍ وهميٍّ — قرارٌ بلا مُطبِّقٍ ولا كتابةٍ في المشروع؛
        قاعدةُ البياناتِ ودفترُ التكرارِ ملفّانِ مؤقّتانِ في /tmp. قياسٌ لا إصلاح.
المالك: Perplexity Computer (قيدُ W-727 · البندُ WI-120).
تاريخ الإنشاء: 2026-10-29
التشغيل (من federal/executive/services):
    ../../../.venv/bin/python ../../../docs/audit/evidence/W-727/probe_batch4_actions.py
"""

import os
import sys
import tempfile
from pathlib import Path

_TMP = tempfile.mkdtemp(prefix="w727-")
os.environ["AMOS_DATABASE_URL"] = f"sqlite:///{_TMP}/probe.db"
os.environ["DATABASE_URL"] = f"sqlite:///{_TMP}/probe.db"
os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = f"{_TMP}/ledger.json"

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from core.constitutional_engine.rules import (  # noqa: E402
    EXECUTIVE_ACTIONS,
    HUMAN_GATED_ACTIONS,
    KILL_SWITCH_BLOCKS,
)
from amos_federation.services.executive_core.sovereignty_bridge import (  # noqa: E402
    ConstitutionalAuthorizer,
    declared_effect,
)

ACTIONS = (
    ("collect_experiences", "record_curriculum_step"),
    ("start_training", "train_model"),
    ("complete_training", "release_agent"),
    ("evaluate_model", "train_model"),
    ("start_shadow", "invoke_model"),
    ("start_canary", "invoke_model"),
    ("promote_beta_to_alpha", "activate_agent"),
    ("create_session", "execute_task"),
    ("check_rate", "log_isolated_action"),
    ("issue_certificate", "issue_certificate"),
    ("verify_certificate", "log_isolated_action"),
)


def _min_level(action: str) -> str:
    for level in sorted(KILL_SWITCH_BLOCKS):
        if action in KILL_SWITCH_BLOCKS[level]:
            return f">={level}"
    return "لا منع"


def main() -> None:
    authorizer = ConstitutionalAuthorizer()
    print("السطح\tالفعل\tتنفيذيّ؟\tمحجوزٌ بشريًّا؟\tأدنى مستوى منع\tالقرارُ بفاعلٍ تنفيذيّ")
    for surface, action in ACTIONS:
        effect = declared_effect("CREATE", "probe:w727/row", "مسبارٌ بلا مُطبِّق")
        try:
            authorizer.request_permit(action, "probe:w727", declared_effects=(effect,))
            verdict = "PERMIT"
        except Exception as exc:  # noqa: BLE001 — المسبارُ يُبلغُ الرفضَ ولا يبتلعُه
            verdict = f"DENY {type(exc).__name__} · {str(exc).splitlines()[0][:100]}"
        print(
            f"{surface}\t{action}\t{action in EXECUTIVE_ACTIONS}\t"
            f"{action in HUMAN_GATED_ACTIONS}\t{_min_level(action)}\t{verdict}"
        )


if __name__ == "__main__":
    main()
