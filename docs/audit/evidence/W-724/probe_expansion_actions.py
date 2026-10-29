"""مسبارُ أفعالِ دفعةِ expansion — ما يُعطاه الفاعلُ التنفيذيُّ لكلِّ فعلٍ في جدولِ G1 § 2.2.

الهدف: قياسُ تعارضِ Q-77 (spawn_population محجوزٌ بشريًّا) قبلَ الشِّفرة، لا افتراضُه.
النطاق: `request_permit` بفاعلِ EXECUTIVE على هدفٍ وهميٍّ — قرارٌ بلا مُطبِّقٍ ولا كتابةٍ في المشروع؛
قاعدةُ البياناتِ ملفٌّ مؤقّتٌ في /tmp.
المالك: Perplexity Computer (قيدُ W-724).
تاريخ الإنشاء: 2026-10-29
التشغيل (من federal/executive/services):
    ../../../.venv/bin/python ../../../docs/audit/evidence/W-724/probe_expansion_actions.py
"""

import os
import tempfile

os.environ.setdefault("AMOS_DATABASE_URL", "sqlite:///" + tempfile.mktemp(suffix=".db"))

from amos_federation.services.executive_core.sovereignty_bridge import (  # noqa: E402
    ConstitutionalAuthorizer,
    declared_effect,
)

ACTIONS = (
    ("create_batch/enroll_batch", "spawn_population"),
    ("employ_batch", "dispatch_agent"),
    ("graduate_batch", "release_agent"),
    ("retire_agent", "contain_agent"),
    ("take_exam", "record_curriculum_step"),
    ("approve_output", "activate_agent"),
    ("submit_output", "create_task"),
)


def main() -> None:
    authorizer = ConstitutionalAuthorizer()
    for surface, action in ACTIONS:
        effect = declared_effect("CREATE", "probe:w724/row", "مسبارٌ بلا مُطبِّق")
        try:
            authorizer.request_permit(action, "probe:w724", declared_effects=(effect,))
            verdict = "PERMIT"
        except Exception as exc:  # noqa: BLE001 — المسبارُ يُبلغُ الرفضَ ولا يبتلعُه
            first = str(exc).splitlines()[0][:120]
            rule = "R-001-1" if "R-001-1" in str(exc) else "?"
            verdict = f"DENY {type(exc).__name__} {rule} · {first}"
        print(f"{surface}\t{action}\t{verdict}")


if __name__ == "__main__":
    main()
