"""مسبارُ فجوةِ WI-085 — هل يصلُ زرُّ الإيقافِ التشغيليُّ إلى البوّابةِ الدستوريّة؟

الهدف: قياسُ ما قبلَ أيِّ شِفرة: يُرفَعُ الزرُّ التشغيليُّ إلى `halt` في الجدولِ الدائم، ثمَّ يُنادى سطحٌ
       محروسٌ فعلُه ممنوعٌ عندَ ≥4 (`University.submit_output` · `create_task`) بالمُصرِّحِ الافتراضيّ،
       ويُقرأُ: هل كُتِبَ الصفّ؟ وما المستوى الذي حملَه الطلبُ إلى المحرّك؟
النطاق: قاعدةُ بياناتٍ مؤقّتةٌ في /tmp — لا كتابةَ في المشروع. قياسٌ لا إصلاح.
المالك: Perplexity Computer (قيدُ W-726 · البندُ WI-085).
تاريخ الإنشاء: 2026-10-29
التشغيل (من federal/executive/services):
    ../../../.venv/bin/python ../../../docs/audit/evidence/W-726/probe_wi085_gap.py
"""

import os
import sys
import tempfile

_DB = os.path.join(tempfile.mkdtemp(prefix="wi085-"), "probe.db")
os.environ["AMOS_DATABASE_URL"] = f"sqlite:///{_DB}"
os.environ["DATABASE_URL"] = f"sqlite:///{_DB}"
# دفترُ التكرارِ معزولٌ في القاعدةِ المؤقّتة (اسمُ المتغيّرِ المقروءُ فعلًا: sovereignty_bridge.py:189).
# تصحيحُ W-726: النسخةُ الأولى ضبطت اسمًا لا يُقرأ فكتبت في دفترِ .runtime المحلّيّ فصار التشغيلُ الثاني إعادة.
os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = _DB + ".ledger.json"

from amos_federation.common.persistent import PersistentSystemStateStore  # noqa: E402
from amos_federation.services.executive_core.sovereignty_bridge import (  # noqa: E402
    ConstitutionalAuthorizer,
)
from amos_federation.services.governance.expansion import (  # noqa: E402
    University,
    UniversityOutputModel,
)

seen: list[int] = []


class _Spy(ConstitutionalAuthorizer):
    """يقرأُ المستوى الذي يحملُه الطلبُ فعلًا — لا يغيّرُه."""

    def _request(self, *a, **k):  # type: ignore[no-untyped-def]
        req = super()._request(*a, **k)
        seen.append(req.kill_switch_level)
        return req


store = PersistentSystemStateStore()
print("1· الحالةُ قبلَ الرفع:", store.get()["level"])
store.set_level("halt", "مسبارُ WI-085", "probe")
print("2· الحالةُ بعدَ الرفع:", store.get()["level"])

uni = University(authorizer=_Spy())
try:
    out = uni.submit_output(
        "paper", "مسبار", "probe-agent", "science", "x", operation_id="wi085"
    )
    if out.get("replayed"):
        outcome = f"REPLAY — {out}"
    else:
        outcome = "ALLOWED — كُتِبَ" if "output_id" in out else f"result={out}"
except Exception as exc:  # noqa: BLE001
    outcome = f"DENIED — {type(exc).__name__}: {exc}"
session = uni._Session()
rows = session.query(UniversityOutputModel).filter_by(output_id="wi085").count()
session.close()
print("3· نداءُ submit_output (create_task · ممنوعٌ عندَ ≥4) والزرُّ halt:", outcome)
print("4· صفوفٌ مكتوبة:", rows)
print("5· المستوى الذي حملَه الطلبُ إلى المحرّك:", seen)
print(
    "الخلاصة:",
    "الفجوةُ قائمة — الزرُّ halt والطلبُ يحملُ 0 والكتابةُ تمّت"
    if rows == 1 and seen and all(v == 0 for v in seen)
    else "النتيجةُ تخالفُ الفجوةَ المتوقَّعة — تُقرأُ كما هي",
)
sys.exit(0)
