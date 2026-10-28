"""مسبارٌ حرفيٌّ لمعنى «المستوى N» في KILL_SWITCH_BLOCKS — قراءةٌ فقط (التوجيه 27 §1 ج).

الهدف: قياسُ دلالةِ «المستوى N» في KILL_SWITCH_BLOCKS بمخرجِ القاعدةِ نفسِها
النطاق: قراءةٌ فقط — لا كتابةَ في ملفٍّ ولا قاعدة
المالك: W-721
تاريخ الإنشاء: 2026-10-28

يستدعي القاعدةَ `_r008_2` نفسَها لأفعالٍ مختارةٍ عندَ المستوياتِ 0…5 ويطبعُ رسالتَها الحرفيّة.
"""

from core.constitutional_engine.model import ActionRequest, Branch
from core.constitutional_engine.rules import KILL_SWITCH_BLOCKS, _r008_2

for lvl in sorted(KILL_SWITCH_BLOCKS):
    print(f"KILL_SWITCH_BLOCKS[{lvl}] = {sorted(KILL_SWITCH_BLOCKS[lvl])}")
for action in (
    "activate_agent",
    "dispatch_agent",
    "spawn_population",
    "record_curriculum_step",
):
    for level in range(0, 6):
        verdict = _r008_2(
            ActionRequest(
                actor=Branch.EXECUTIVE, action=action, kill_switch_level=level
            )
        )
        print(
            f"{action} @ level {level}: {'ALLOW' if verdict is None else 'BLOCK — ' + verdict}"
        )
