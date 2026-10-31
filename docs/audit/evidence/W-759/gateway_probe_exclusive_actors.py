"""
الهدف: قياسُ ما تفعلُه البوّابةُ السياديّةُ (`SovereignGateway.review`) — لا المحرّكُ وحدَه — بطلباتِ HUMAN وSTATE وINSTITUTION وROYAL بلا مرسومٍ على الأفعالِ الحصريّةِ الـ56 (ورقةُ المالكِ A1 (ج)/(د) § 5 · W-759). لا كتابةَ في المشروع: السجلُّ في /tmp.
التشغيل (من جذرِ المستودع): PYTHONPATH=. .venv/bin/python docs/audit/evidence/W-759/gateway_probe_exclusive_actors.py
"""
import os
import tempfile
from collections import Counter
from core.constitutional_engine import rules as r
from core.constitutional_engine.engine import ConstitutionalEngine
from core.constitutional_engine.model import ActionRequest, Branch
from core.sovereignty.gateway import SovereignGateway

d = tempfile.mkdtemp(prefix="w759g-")
gw = SovereignGateway(ConstitutionalEngine(ledger_path=os.path.join(d, "l.jsonl")))
acts = sorted({a for s in r._BRANCH_EXCLUSIVE.values() for a in s})
print(f"أفعالٌ حصريّة: {len(acts)}")
for actor in (Branch.HUMAN, Branch.STATE, Branch.INSTITUTION, Branch.ROYAL, Branch.AGENT, Branch.TREASURY):
    c = Counter()
    sample = None
    for a in acts:
        try:
            v = gw.review(ActionRequest(actor=actor, action=a, target="probe"))
            c[f"allowed={v.allowed}·kind={getattr(v.decision_kind, 'value', v.decision_kind)}·layer={getattr(v.authority_layer, 'value', v.authority_layer)}"] += 1
        except Exception as e:  # noqa: BLE001 — القياسُ يسجّلُ نوعَ الرفض
            c[f"raise={type(e).__name__}"] += 1
            sample = sample or f"{a}: {type(e).__name__}: {str(e)[:120]}"
    print(f"{actor.value:12s} {dict(c)}" + (f"\n   مثال: {sample}" if sample else ""))

# ── مسارُ التنفيذ: execute(request, executor) — هل يُستدعى المُنفِّذُ فعلًا؟ ──
print("== مسارُ التنفيذ (gw.execute بمُنفِّذٍ يَعُدُّ نداءاتِه)")
for actor in (Branch.HUMAN, Branch.STATE, Branch.INSTITUTION, Branch.ROYAL, Branch.AGENT):
    calls = [0]

    def _ex():
        calls[0] += 1
        return "ok"

    c = Counter()
    for a in acts:
        try:
            gw.execute(ActionRequest(actor=actor, action=a, target="probe"), _ex)
            c["executed"] += 1
        except Exception as e:  # noqa: BLE001
            c[f"raise={type(e).__name__}"] += 1
    print(f"{actor.value:12s} {dict(c)} · نداءاتُ المُنفِّذ={calls[0]}")
