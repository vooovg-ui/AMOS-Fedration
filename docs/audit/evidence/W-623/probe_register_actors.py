"""مسبارُ الفعلِ `register` لكلِّ فاعلٍ — دليلُ قيدِ W-623 (بندُ WI-107 · الدفعةُ R1).

الغرض: قياسُ قرارِ البوابةِ الدستوريّةِ (`ConstitutionalAuthorizer.review_only`) على الفعلِ
`register` لكلِّ فاعلٍ قبلَ أيِّ شِفرةٍ — سندًا لنقطةِ التصميمِ D1/D2 في ملحقِ R1
(نمطُ مسبارِ F1 `probe_coordinate_actors.py` · قيدِ W-615).
التشغيل: من federal/executive/services — `python <هذا الملف>` · قراءةٌ فقط، لا كتابةَ.
المالك: Perplexity Computer · تاريخ الإنشاء: 2026-10-23
"""
import os
import tempfile
os.environ.setdefault("AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER", tempfile.mktemp(suffix=".json"))
from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer
for actor in ["EXECUTIVE","LEGISLATIVE","JUDICIAL","TREASURY","AGENT","SYSTEM"]:
    a = ConstitutionalAuthorizer(actor=actor)
    try:
        ev = a.review_only("register", "registry/probe/x")
        print(actor, ev.decision, ev.authority_layer, ev.decision_kind)
    except Exception as e:
        print(actor, "RAISE", type(e).__name__, str(e)[:120])
