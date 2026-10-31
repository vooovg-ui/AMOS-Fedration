"""DISC-148 — مسبارُ «يُغيِّرُ ثمَّ يرفع» عبرَ `SovereignExecutionBoundary` الحقيقيّ، قبلَ الإصلاحِ وبعدَه.

الهدف: قياسُ قاعدةِ المالكِ في `Q-88` (1) على حالاتِ W-761 نفسِها (P2–P6) وحالتَينِ جديدتَين:
       P7 «لا معوِّض» (مرفوضٌ بنيويًّا قبلَ التنفيذ) وP7ب «معوِّضٌ يتعذّر» (المتوقَّعُ بعدَ الإصلاح:
       FAILED_FINAL ولا إعادة) · P8 «معوِّضٌ مُثبِّتٌ مُعلَن»
       (المتوقَّعُ: عكسٌ ثمَّ إعادةٌ تُطبِّقُ مرّةً واحدة) · وP4ذ «مُطبِّقٌ مُصرِّحٌ بالذرّيّة».
       السكربتُ نفسُه يُشغَّلُ قبلُ وبعدُ: يستعملُ `applier_atomic` و`Compensator(idempotent=…)` إن وُجِدا،
       ويكتبُ «غيرُ مدعوم» إن لم يوجدا — فلا يُخترَعُ رقمٌ لواجهةٍ لم تُكتَب.
النطاق: سجلّاتٌ على القرصِ في مجلّدٍ مؤقّت · بلا ساعةٍ مُجمَّدة (DISC-146 أُصلِحَ في W-762) · لا كتابةَ في المشروع.
المالك: Perplexity Computer (قيدُ W-764 · البندُ WI-125).
التشغيل (من جذرِ المستودع): PYTHONPATH=. .venv/bin/python docs/audit/evidence/W-764/disc148_probe.py
"""

from __future__ import annotations

import dataclasses
import inspect
import tempfile
from pathlib import Path

from core.constitutional_engine.engine import ConstitutionalEngine
from core.constitutional_engine.ledger import ConstitutionalLedger
from core.constitutional_engine.model import ActionRequest, Branch
from core.sovereignty.compensation import Compensator
from core.sovereignty.contract import EffectKind, SovereignEffect
from core.sovereignty.enforcement import ConsumedPermitLedger
from core.sovereignty.enforcement_boundary import SovereignExecutionBoundary
from core.sovereignty.gateway import SovereignGateway
from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger

TARGET = "treasury/account-A"
EFFECT = SovereignEffect(kind=EffectKind.WRITE, resource=TARGET, detail="قياس")
SEAL = SovereignEffect(kind=EffectKind.CREATE, resource=TARGET, detail="ختم")

HAS_ATOMIC = (
    "applier_atomic" in inspect.signature(SovereignExecutionBoundary.execute).parameters
)
HAS_IDEMPOTENT = "idempotent" in {f.name for f in dataclasses.fields(Compensator)}


def _boundary(d: Path):
    gw = SovereignGateway(
        ConstitutionalEngine(ledger=ConstitutionalLedger(d / "l.jsonl"))
    )
    led = IdempotencyLedger(d / "IDEMPOTENCY.json")
    consumed = ConsumedPermitLedger(d / "CONSUMED.json")
    return SovereignExecutionBoundary(
        gateway=gw, idempotency_ledger=led, consumed_permits=consumed
    ), led


def _req():
    return ActionRequest(
        actor=Branch.EXECUTIVE,
        action="credit_account",
        target=TARGET,
        channel="official",
    )


def _attempt(b, key, state, *, mode, counters, comp_kind, atomic):
    """mode: ok · fail_before · fail_inside · fail_second. comp_kind: relative · broken · restore · none."""
    effects = (EFFECT, SEAL)
    snapshot = state[TARGET]

    def apply(effect):
        if mode == "fail_before":
            raise RuntimeError("فشلٌ قبلَ أيِّ أثر")
        if effect.signature == SEAL.signature:
            if mode == "fail_second":
                raise RuntimeError("الأثرُ الثاني فشل")
            state["seal"] = "SEALED"
            return
        state[TARGET] = str(int(state[TARGET]) + 100)
        counters["applied"] += 1
        if mode == "fail_inside":
            raise RuntimeError("فشلٌ بعدَ التغييرِ داخلَ النداءِ نفسِه")

    def relative():
        state[TARGET] = str(int(state[TARGET]) - 100)
        counters["compensated"] += 1

    def broken():
        raise RuntimeError("المعوِّضُ تعذّر")

    def restore():
        # مُثبِّت: يُعيدُ لقطةَ ما قبلَ المحاولة — تشغيلُه بلا أثرٍ واقعٍ لا يُغيِّرُ شيئًا.
        if state[TARGET] != snapshot:
            counters["compensated"] += 1
        state[TARGET] = snapshot

    def _comp(sig, fn, desc, idem):
        kw = {"idempotent": idem} if (HAS_IDEMPOTENT and idem) else {}
        return Compensator(effect_signature=sig, apply=fn, description=desc, **kw)

    if comp_kind == "none":
        comps = ()
    else:
        fn = {"relative": relative, "broken": broken, "restore": restore}[comp_kind]
        comps = (
            _comp(EFFECT.signature, fn, "عكس", comp_kind == "restore"),
            _comp(SEAL.signature, lambda: state.pop("seal", None), "فكُّ الختم", True),
        )
    kwargs = {"applier_atomic": True} if (atomic and HAS_ATOMIC) else {}
    try:
        b.execute(
            _req(),
            declared_effects=effects,
            planner=lambda _: effects,
            applier=apply,
            operation_key=key,
            compensators=comps,
            **kwargs,
        )
        return "OK"
    except Exception as exc:  # noqa: BLE001 — القياسُ يُسمّي النوعَ ولا يبتلعُه
        return type(exc).__name__


def case(name, first_mode, *, comp_kind="relative", atomic=False):
    if atomic and not HAS_ATOMIC:
        print(
            f"{name}: غيرُ مدعوم — لا معامِلَ `applier_atomic` في `execute` (الواجهةُ لم تُكتَب)"
        )
        return
    if comp_kind == "restore" and not HAS_IDEMPOTENT:
        note = (
            " · (لا حقلَ `idempotent` في `Compensator`: المعوِّضُ مُثبِّتٌ فعلًا لكنّه غيرُ مُعلَن)"
        )
    else:
        note = ""
    with tempfile.TemporaryDirectory() as t:
        b, led = _boundary(Path(t))
        state = {TARGET: "1000"}
        c = {"applied": 0, "compensated": 0}
        key = IdempotencyKey(scope="treasury", value="probe")
        r1 = _attempt(
            b,
            key,
            state,
            mode=first_mode,
            counters=c,
            comp_kind=comp_kind,
            atomic=atomic,
        )
        s1 = led.get(key).status.value if led.get(key) else "-"
        bal1 = state[TARGET]
        r2 = _attempt(
            b, key, state, mode="ok", counters=c, comp_kind=comp_kind, atomic=atomic
        )
        s2 = led.get(key).status.value if led.get(key) else "-"
        print(
            f"{name}: محاولة1={r1} [{s1}] الرصيد={bal1} · محاولة2 بالمفتاحِ نفسِه={r2} [{s2}] · "
            f"الرصيدُ النهائيّ={state[TARGET]} (البدء 1000 · الصحيحُ بعدَ نجاحٍ واحد 1100) · "
            f"طُبِّقَ={c['applied']} · عُكِسَ={c['compensated']}{note}"
        )


print(
    f"الواجهة: applier_atomic={'موجود' if HAS_ATOMIC else 'غائب'} · Compensator.idempotent={'موجود' if HAS_IDEMPOTENT else 'غائب'}"
)
case("P2 الأثرُ الثاني يفشل + تعويضٌ نظيف", "fail_second")
case("P3 الأثرُ الثاني يفشل + تعويضٌ غيرُ نظيف", "fail_second", comp_kind="broken")
case("P4 المُطبِّقُ يرفعُ قبلَ أيِّ تغيير (معوِّضٌ نسبيٌّ غيرُ مُثبِّت)", "fail_before")
case("P4ذ المُطبِّقُ يرفعُ قبلَ أيِّ تغيير + مُصرِّحٌ بالذرّيّة", "fail_before", atomic=True)
case("P6 مُطبِّقٌ غيرُ ذرّيّ يُغيِّرُ ثمَّ يرفع (معوِّضٌ نسبيٌّ غيرُ مُثبِّت)", "fail_inside")
# P7 «لا معوِّض» حرفيًّا: الحدُّ يرفضُ أثرًا مُغيِّرًا بلا خطّةٍ قبلَ التنفيذِ (1I · CompensationNotDeclaredError)،
# فـ«لا معوِّض» وقتَ التشغيلِ صورتُه معوِّضٌ غيرُ مُثبِّتٍ (P6) أو معوِّضٌ يتعذّر (P7ب).
case("P7 مُطبِّقٌ غيرُ ذرّيّ يُغيِّرُ ثمَّ يرفع + لا معوِّضَ مُعلَن", "fail_inside", comp_kind="none")
case("P7ب مُطبِّقٌ غيرُ ذرّيّ يُغيِّرُ ثمَّ يرفع + معوِّضٌ يتعذّر", "fail_inside", comp_kind="broken")
case(
    "P8 مُطبِّقٌ غيرُ ذرّيّ يُغيِّرُ ثمَّ يرفع + معوِّضٌ مُثبِّتٌ (لقطة)",
    "fail_inside",
    comp_kind="restore",
)
