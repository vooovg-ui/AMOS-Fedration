"""مسبارُ كلفةِ القراءةِ التقريبيُّ لمرحلةِ المراقبة (WI-085 · § 3 · § 10.7) — لا حملٌ حقيقيّ.

الهدف: زمنُ قراءةِ المصدرِ الفدراليِّ لكلِّ عبورٍ، وزمنُ `review` ببوّابةٍ بمصدرٍ وبغيرِه، على SQLite مؤقّتةٍ.
النطاق: قاعدةٌ في /tmp · لا كتابةَ في المشروع · رقمٌ تقريبيٌّ على هذه الآلةِ وحدَها.
المالك: Perplexity Computer (قيدُ W-752 · البندُ WI-085).
تاريخ الإنشاء: 2026-10-30
التشغيل (من federal/executive/services):
    ../../../.venv/bin/python ../../../docs/audit/evidence/W-752/probe_read_cost.py
"""

import os
import tempfile
import time

_DB = os.path.join(tempfile.mkdtemp(prefix="wi085c-"), "probe.db")
os.environ["AMOS_DATABASE_URL"] = f"sqlite:///{_DB}"
os.environ["DATABASE_URL"] = f"sqlite:///{_DB}"

from amos_federation.common.persistent import PersistentSystemStateStore  # noqa: E402
from amos_federation.services.executive_core.kill_switch_level_source import (  # noqa: E402
    PersistentKillSwitchLevelSource,
)
from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer  # noqa: E402

ConstitutionalAuthorizer._ensure_core_importable()

from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402
from core.sovereignty.gateway import SovereignGateway  # noqa: E402
from core.sovereignty.kill_switch_source import LevelReading  # noqa: E402

PersistentSystemStateStore().set_level("halt", "probe", "probe")
N = 1000
src = PersistentKillSwitchLevelSource()
t = time.perf_counter()
for _ in range(N):
    src.read()
read_ms = (time.perf_counter() - t) * 1000 / N
print(f"1· قراءةُ المصدرِ الفدراليّ: {read_ms:.3f} ms/قراءة (N={N})")


def bench(gw: SovereignGateway) -> float:
    req = ActionRequest(actor=Branch.EXECUTIVE, action="create_task", target="probe")
    t0 = time.perf_counter()
    for _ in range(N):
        gw.review(req)
    return (time.perf_counter() - t0) * 1000 / N


class _Zero:
    def read(self) -> LevelReading:
        return LevelReading(0, "constitutional")


bare = SovereignGateway(ConstitutionalEngine(ledger_path=_DB + ".a.jsonl"))
bare.register_kill_switch_source(_Zero())
wired = SovereignGateway(ConstitutionalEngine(ledger_path=_DB + ".b.jsonl"))
wired.register_kill_switch_source(src)
a = bench(bare)
b = bench(wired)
print(f"2· review بمصدرٍ ثابتٍ (0): {a:.3f} ms · بالمصدرِ الفدراليّ (halt): {b:.3f} ms · الفرق: {b - a:.3f} ms/عبور")
print(f"3· ملاحظاتُ البوّابةِ الموصولة: {len(wired.kill_switch_observations)} من {N} (create_task عندَ halt=4)")
