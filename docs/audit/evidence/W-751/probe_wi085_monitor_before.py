"""مسبارُ ما قبلَ مرحلةِ المراقبةِ لـWI-085 (Q-79 · ب · م2 · غ1 · «يسجّلُ ما كانَ سيمنعُه، بلا منع»).

الهدف: قياسُ ما يحتاجُه ملحقُ التصميمِ § 10 قبلَ أيِّ شِفرة:
  (1) هل في البوّابةِ اليومَ موضعٌ لمصدرِ المستوى؟
  (2) هل `_r008_2` نقيّةٌ (لا تكتبُ في السجلِّ الدستوريّ) فيُعادُ استعمالُها لحكمِ «ما كانَ سيمنعُه» بلا منطقٍ مكرَّر؟
  (3) مصفوفةُ «ما كانَ سيُمنَع» عندَ المستوياتِ 0..5 لأفعالٍ ممثِّلة — هي ما سيُسجَّلُ في المراقبة.
  (4) هل قراءةُ الجدولِ الدائمِ اليومَ تُنشئُ صفًّا `normal` عندَ غيابِه (يفشلُ مفتوحًا) — فلا تصلحُ لغ1؟
النطاق: قاعدةٌ مؤقّتةٌ في /tmp · لا كتابةَ في المشروع · قياسٌ لا إصلاح.
المالك: Perplexity Computer (قيدُ W-751 · البندُ WI-085).
تاريخ الإنشاء: 2026-10-30
التشغيل (من federal/executive/services):
    ../../../.venv/bin/python ../../../docs/audit/evidence/W-751/probe_wi085_monitor_before.py
"""

import os
import sys
import tempfile
from dataclasses import replace

_DB = os.path.join(tempfile.mkdtemp(prefix="wi085m-"), "probe.db")
os.environ["AMOS_DATABASE_URL"] = f"sqlite:///{_DB}"
os.environ["DATABASE_URL"] = f"sqlite:///{_DB}"

# الفدراليُّ أوّلًا: هو من يضعُ النواةَ `core/` في المسار (sovereignty_bridge.py).
from amos_federation.common.database import SystemStateModel, get_session_factory  # noqa: E402
from amos_federation.common.persistent import PersistentSystemStateStore  # noqa: E402
from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer  # noqa: E402

ConstitutionalAuthorizer._ensure_core_importable()

from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402
from core.constitutional_engine.rules import KILL_SWITCH_BLOCKS, _r008_2  # noqa: E402
from core.sovereignty.gateway import SovereignGateway  # noqa: E402

gw = SovereignGateway(ConstitutionalEngine(ledger_path=_DB + ".constitutional.jsonl"))
hooks = [n for n in dir(gw) if "kill" in n.lower()]
print("1· أسماءٌ في البوّابةِ تحوي kill:", hooks or "لا شيء")

before = len(gw.engine.ledger)
base = ActionRequest(actor=Branch.EXECUTIVE, action="create_task")
results = [_r008_2(replace(base, kill_switch_level=lvl)) is not None for lvl in range(6)]
after = len(gw.engine.ledger)
print("2· _r008_2 على create_task عندَ 0..5:", results, "· السجلُّ قبل/بعد:", before, after)

print("3· عددُ الأفعالِ الممنوعةِ تراكميًّا عندَ كلِّ مستوى:")
acc: set[str] = set()
for lvl in range(1, 6):
    acc |= KILL_SWITCH_BLOCKS.get(lvl, frozenset())
    print(f"   المستوى {lvl}: {len(acc)}")

PROBE_CASES = [
    (Branch.EXECUTIVE, "create_task"),
    (Branch.EXECUTIVE, "record_curriculum_step"),
    (Branch.EXECUTIVE, "spawn_agent"),
    (Branch.EXECUTIVE, "activate_agent"),
    (Branch.EXECUTIVE, "update_population_state"),
    (Branch.EXECUTIVE, "orchestrate"),
    (Branch.EXECUTIVE, "run_health_check"),
    (Branch.EXECUTIVE, "contain_agent"),
    (Branch.EXECUTIVE, "release_agent"),
    (Branch.EXECUTIVE, "graceful_shutdown"),
    (Branch.EXECUTIVE, "create_backup"),
    (Branch.HUMAN, "lower_kill_switch"),
]
print("4· مصفوفةُ «ما كانَ سيُمنَع» (X = يُمنَع) عندَ 0..5:")
for actor, action in PROBE_CASES:
    req = ActionRequest(actor=actor, action=action)
    row = "".join("X" if _r008_2(replace(req, kill_switch_level=lvl)) else "." for lvl in range(6))
    print(f"   {actor.value:>9} · {action:<24} {row}")

store = PersistentSystemStateStore()
session = get_session_factory()()
had = session.query(SystemStateModel).count()
session.close()
level = store.get()["level"]
session = get_session_factory()()
now = session.query(SystemStateModel).count()
session.close()
print(f"5· صفوفُ system_state قبلَ get(): {had} · المقروء: {level} · بعدَه: {now}")
print(
    "الخلاصة:",
    "لا موضعَ للمصدرِ في البوّابة · _r008_2 نقيّة · get() يُنشئُ normal عندَ الغياب (مفتوح)"
    if not hooks and before == after and had == 0 and now == 1 and level == "normal"
    else "النتيجةُ تخالفُ المتوقَّع — تُقرأُ كما هي",
)
sys.exit(0)
