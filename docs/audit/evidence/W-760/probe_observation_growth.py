"""مسبارُ نموِّ قائمةِ ملاحظاتِ مراقبةِ زرِّ التوقّف (WI-085 · التوجيهُ 33 § 1 بند 5) — قياسٌ قبلَ تصميمِ السقف.

الهدف: قياسُ أنَّ `SovereignGateway._kill_switch_observations` تنمو بلا حدٍّ (ملاحظةٌ لكلِّ عبورٍ «كانَ سيُمنَع»)،
وكلفةِ الذاكرةِ لكلِّ ملاحظةٍ بـtracemalloc، كي يُبنى السقفُ على رقمٍ مقيسٍ لا مقدَّر.
النطاق: بوّابةٌ في الذاكرةِ بمصدرٍ ثابتٍ (المستوى 4) · سجلٌّ دستوريٌّ في /tmp · لا كتابةَ في المشروع · لا شبكة.
المالك: Perplexity Computer (قيدُ W-760 · البندُ WI-085).
تاريخ الإنشاء: 2026-10-31
التشغيل (من جذرِ المستودع): PYTHONPATH=. .venv/bin/python docs/audit/evidence/W-760/probe_observation_growth.py
"""

import os
import tempfile
import tracemalloc

from core.constitutional_engine.engine import ConstitutionalEngine
from core.constitutional_engine.model import ActionRequest, Branch
from core.sovereignty.gateway import SovereignGateway
from core.sovereignty.kill_switch_source import LevelReading


class _Halt:
    def read(self) -> LevelReading:
        return LevelReading(4, "constitutional")


d = tempfile.mkdtemp(prefix="wi085g-")
gw = SovereignGateway(ConstitutionalEngine(ledger_path=os.path.join(d, "l.jsonl")))
gw.register_kill_switch_source(_Halt())
req = ActionRequest(actor=Branch.EXECUTIVE, action="create_task", target="probe")
safe = ActionRequest(actor=Branch.EXECUTIVE, action="run_health_check", target="probe")

for n in (1000, 5000):
    gw._kill_switch_observations.clear()
    tracemalloc.start()
    s0 = tracemalloc.take_snapshot()
    for _ in range(n):
        gw.review(req)
    s1 = tracemalloc.take_snapshot()
    tracemalloc.stop()
    obs_bytes = sum(
        st.size_diff
        for st in s1.compare_to(s0, "filename")
        if "kill_switch_source.py" in str(st.traceback) or "gateway.py" in str(st.traceback)
    )
    print(
        f"N={n}: ملاحظات={len(gw.kill_switch_observations)} · "
        f"ذاكرةٌ منسوبةٌ لـkill_switch_source.py+gateway.py ≈ {obs_bytes} بايت "
        f"(≈ {obs_bytes / max(1, len(gw.kill_switch_observations)):.0f} بايت/ملاحظة)"
    )

before = len(gw.kill_switch_observations)
for _ in range(100):
    gw.review(safe)
print(f"فعلٌ لا يُمنَعُ عندَ 4 (run_health_check ×100): زيادةُ القائمة = {len(gw.kill_switch_observations) - before}")
print(f"السقفُ في الشِّفرةِ اليوم: {'لا يوجد' if isinstance(gw._kill_switch_observations, list) else type(gw._kill_switch_observations).__name__} (النوعُ {type(gw._kill_switch_observations).__name__})")
print(f"أعطالُ المراقبة: {gw.kill_switch_observation_errors}")
