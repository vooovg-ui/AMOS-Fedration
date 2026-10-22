"""مسبارُ الفعلِ `coordinate` لكلِّ فاعلٍ — دليلُ قيدِ W-615 (بندُ WI-106 · الدفعةُ F1).

الغرض: قياسُ قرارِ البوابةِ الدستوريّةِ (`ConstitutionalAuthorizer.review_only`) على الفعلِ
`coordinate` لكلِّ فاعلٍ قبلَ أيِّ شِفرةٍ، سندًا لاختيارِ الفاعلِ التنفيذيِّ (D17-1).
التشغيل: من federal/executive/services — `python <هذا الملف>` · قراءةٌ فقط، لا كتابةَ.
المالك: Perplexity Computer · تاريخ الإنشاء: 2026-10-22
"""
import os
import tempfile
os.environ.setdefault("AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER", tempfile.mktemp(suffix=".json"))
from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer
for actor in ["EXECUTIVE","LEGISLATIVE","JUDICIAL","TREASURY","AGENT","SYSTEM"]:
    a = ConstitutionalAuthorizer(actor=actor)
    try:
        ev = a.review_only("coordinate", "federation/probe/x")
        print(actor, ev.decision, ev.authority_layer, ev.decision_kind)
    except Exception as e:
        print(actor, "RAISE", type(e).__name__, str(e)[:120])
