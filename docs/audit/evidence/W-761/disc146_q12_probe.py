"""DISC-146 · Q-11/Q-12 — مسبارٌ حتميٌّ بساعةٍ مُجمَّدة (لا يتعلّقُ بحظِّ حدِّ الثانية).

الهدف: قياسُ إعادةِ المحاولةِ بالمفتاحِ نفسِه في الثانيةِ نفسِها وبعدَ ثانيتين عبرَ `SovereignExecutionBoundary`
الحقيقيّ، قبلَ إصلاحِ هويّةِ الإذنِ وبعدَه، وفصلُ ما يحرسُه الإذنُ عمّا يحرسُه سجلُّ الذرّيّة (1H).
النطاق: سجلّاتٌ على القرصِ في مجلّدٍ مؤقّت · الساعةُ مُجمَّدةٌ في `core/sovereignty/enforcement.py` وحدَها · لا كتابةَ في المشروع.
المالك: Perplexity Computer (قيدُ W-761 · البندُ WI-125).
التشغيل (من جذرِ المستودع): PYTHONPATH=. .venv/bin/python docs/audit/evidence/W-761/disc146_q12_probe.py
"""

from __future__ import annotations

import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from core.constitutional_engine.engine import ConstitutionalEngine
from core.constitutional_engine.ledger import ConstitutionalLedger
from core.constitutional_engine.model import ActionRequest, Branch
from core.sovereignty import enforcement as enf
from core.sovereignty.compensation import Compensator
from core.sovereignty.contract import EffectKind, SovereignEffect
from core.sovereignty.enforcement import ConsumedPermitLedger
from core.sovereignty.enforcement_boundary import SovereignExecutionBoundary
from core.sovereignty.gateway import SovereignGateway
from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger

CLOCK = {"t": datetime(2026, 10, 31, 12, 0, 0, tzinfo=timezone.utc)}


class _Frozen(datetime):
    @classmethod
    def now(cls, tz=None):  # noqa: D102
        return CLOCK["t"] if tz is None else CLOCK["t"].astimezone(tz)


def _tick() -> None:
    CLOCK["t"] = CLOCK["t"] + timedelta(seconds=2)


enf.datetime = _Frozen  # الساعةُ مُجمَّدةٌ في وحدةِ الإذنِ وحدَها

TARGET = "treasury/account-A"


def _boundary(d: Path):
    gw = SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(d / "l.jsonl")))
    led = IdempotencyLedger(d / "IDEMPOTENCY.json")
    consumed = ConsumedPermitLedger(d / "CONSUMED.json")
    return SovereignExecutionBoundary(gateway=gw, idempotency_ledger=led, consumed_permits=consumed), led, consumed


def _req():
    return ActionRequest(actor=Branch.EXECUTIVE, action="credit_account", target=TARGET, channel="official")


EFFECT = SovereignEffect(kind=EffectKind.WRITE, resource=TARGET, detail="قياس")
SEAL = SovereignEffect(kind=EffectKind.CREATE, resource=TARGET, detail="ختم")


def _attempt(b, key, state, *, mode, counters, broken_comp=False):
    """mode: ok · fail_before · fail_inside (يُغيِّرُ ثمَّ يرفعُ في النداءِ نفسِه) · fail_second (الأثرُ الثاني يفشل)."""
    effects = (EFFECT, SEAL)

    def apply(effect):
        if mode == "fail_before":
            raise RuntimeError("فشلٌ قبلَ أيِّ أثر")
        if effect is SEAL or effect.signature == SEAL.signature:
            if mode == "fail_second":
                raise RuntimeError("الأثرُ الثاني فشل")
            state["seal"] = "SEALED"
            return
        state[TARGET] = str(int(state[TARGET]) + 100)
        counters["applied"] += 1
        if mode == "fail_inside":
            raise RuntimeError("فشلٌ بعدَ التغييرِ داخلَ النداءِ نفسِه")

    def comp():
        if broken_comp:
            raise RuntimeError("المعوِّضُ تعذّر")
        state[TARGET] = str(int(state[TARGET]) - 100)
        counters["compensated"] += 1

    try:
        b.execute(
            _req(),
            declared_effects=effects,
            planner=lambda _: effects,
            applier=apply,
            operation_key=key,
            compensators=(
                Compensator(effect_signature=EFFECT.signature, apply=comp, description="عكس"),
                Compensator(effect_signature=SEAL.signature, apply=lambda: state.pop("seal", None), description="فكُّ الختم"),
            ),
        )
        return "OK"
    except Exception as exc:  # noqa: BLE001 — القياسُ يُسمّي النوعَ ولا يبتلعُه
        tag = type(exc).__name__
        if "استُهلِك" in str(exc):
            tag += "(PermitReplay)"
        return tag


def case(name, first_mode, *, broken_comp=False, tick=False):
    with tempfile.TemporaryDirectory() as t:
        d = Path(t)
        b, led, consumed = _boundary(d)
        state = {TARGET: "1000"}
        c = {"applied": 0, "compensated": 0}
        key = IdempotencyKey(scope="treasury", value="probe")
        r1 = _attempt(b, key, state, mode=first_mode, counters=c, broken_comp=broken_comp)
        s1 = led.get(key).status.value if led.get(key) else "-"
        if tick:
            _tick()
        r2 = _attempt(b, key, state, mode="ok", counters=c)
        s2 = led.get(key).status.value if led.get(key) else "-"
        when = "بعدَ ثانيتين" if tick else "الثانيةُ نفسُها"
        print(
            f"{name} [{when}]: محاولة1={r1} [{s1}] · محاولة2={r2} [{s2}] · "
            f"الرصيد={state[TARGET]} (البدء 1000 · الصحيحُ بعدَ نجاحٍ واحد 1100) · طُبِّقَ={c['applied']} · "
            f"عُكِسَ={c['compensated']} · أذوناتٌ مُستهلَكة={consumed.count()}"
        )


# P1 — هويّةُ الإذنِ نفسُها
with tempfile.TemporaryDirectory() as t:
    b, _, _ = _boundary(Path(t))
    gw = b.gateway
    p1 = gw.decide(_req(), declared_effects=(EFFECT,))
    p2 = gw.decide(_req(), declared_effects=(EFFECT,))
    print(f"P1 إذنانِ للعقدِ نفسِه في الثانيةِ نفسِها: متطابقان={p1.permit_id == p2.permit_id} · الأوّل={p1.permit_id} · الثاني={p2.permit_id}")

for tick in (False, True):
    case("P2 الأثرُ الثاني يفشل + تعويضٌ نظيف", "fail_second", tick=tick)
    case("P3 الأثرُ الثاني يفشل + تعويضٌ غيرُ نظيف", "fail_second", broken_comp=True, tick=tick)
    case("P4 فشلٌ قبلَ أيِّ أثر", "fail_before", tick=tick)
    case("P6 مُطبِّقٌ غيرُ ذرّيّ (يُغيِّرُ ثمَّ يرفع)", "fail_inside", tick=tick)

# P5 — إعادةُ تقديمِ الإذنِ نفسِه
with tempfile.TemporaryDirectory() as t:
    b, _, consumed = _boundary(Path(t))
    pep = enf.PolicyEnforcementPoint(verifying_key=b.gateway_verifying_key) if hasattr(b, "gateway_verifying_key") else b.policy_enforcement_point
    permit = b.gateway.decide(_req(), declared_effects=(EFFECT,))
    pep.enforce(permit, planner=lambda _: (EFFECT,), applier=lambda e: None)
    try:
        pep.enforce(permit, planner=lambda _: (EFFECT,), applier=lambda e: None)
        print("P5 إعادةُ تقديمِ الإذنِ نفسِه: قُبِلَت (!)")
    except Exception as exc:  # noqa: BLE001
        print(f"P5 إعادةُ تقديمِ الإذنِ نفسِه: رُفِضَت {type(exc).__name__}")
