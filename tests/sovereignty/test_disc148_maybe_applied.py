"""DISC-148 · Q-88 (القرار 1): المُطبِّقُ الذي يرفعُ «ربما طبَّق» — عبرَ الحدِّ الحقيقيّ.

الهدف: تثبيتُ قاعدةِ المالكِ بنصِّها: يُشغَّلُ معوِّضُ الأثرِ المُعلَنِ إن كانَ مُثبِّتًا؛
       وإن لم يوجد معوِّضٌ قابلٌ للتشغيلِ أو فشلَ فالعمليّةُ FAILED_FINAL ولا تُعادُ تلقائيًّا؛
       ولا يُوسَمُ فشلٌ «قابلًا للإعادة» إلّا إن صرّحَ المُطبِّقُ بالذرّيّة.
النطاق: `SovereignExecutionBoundary.execute` بسجلّاتٍ على القرص · بلا محاكاةٍ للحدّ.
المالك: Perplexity Computer (قيدُ W-765 · البندُ WI-125 · التصميم DISC148_MAYBE_APPLIED_DESIGN.md).
"""

from __future__ import annotations

import dataclasses
import inspect
from pathlib import Path

import pytest

from core.constitutional_engine.engine import ConstitutionalEngine
from core.constitutional_engine.ledger import ConstitutionalLedger
from core.constitutional_engine.model import ActionRequest, Branch
from core.sovereignty.compensation import CompensationRequired, Compensator
from core.sovereignty.contract import EffectKind, SovereignEffect
from core.sovereignty.enforcement import ConsumedPermitLedger
from core.sovereignty.enforcement_boundary import (
    CompensationNotDeclaredError,
    SovereignExecutionBoundary,
)
from core.sovereignty.gateway import SovereignGateway
from core.sovereignty.idempotency import (
    IdempotencyError,
    IdempotencyKey,
    IdempotencyLedger,
    OperationStatus,
)

TARGET = "treasury/account-A"
EFFECT = SovereignEffect(kind=EffectKind.WRITE, resource=TARGET, detail="رصيد")
SEAL = SovereignEffect(kind=EffectKind.CREATE, resource=TARGET, detail="ختم")


class _Boom(RuntimeError):
    """فشلٌ مُحقَنٌ داخلَ المُطبِّق."""


def _boundary(d: Path) -> tuple[SovereignExecutionBoundary, IdempotencyLedger]:
    gw = SovereignGateway(
        ConstitutionalEngine(ledger=ConstitutionalLedger(d / "l.jsonl"))
    )
    led = IdempotencyLedger(d / "IDEMPOTENCY.json")
    return (
        SovereignExecutionBoundary(
            gateway=gw,
            idempotency_ledger=led,
            consumed_permits=ConsumedPermitLedger(d / "CONSUMED.json"),
        ),
        led,
    )


def _req() -> ActionRequest:
    return ActionRequest(
        actor=Branch.EXECUTIVE,
        action="credit_account",
        target=TARGET,
        channel="official",
    )


class _World:
    """رصيدٌ وعدّادات — والمُطبِّقُ يُغيِّرُ ثمّ يرفعُ أو يرفعُ قبلَ أن يُغيِّر."""

    def __init__(self) -> None:
        self.balance = 1000
        self.applied = 0
        self.compensated = 0
        self.snapshot = 1000

    def applier(self, mode: str):
        self.snapshot = self.balance

        def apply(effect: SovereignEffect) -> None:
            if effect.signature != EFFECT.signature:
                if mode == "fail_second":
                    raise _Boom("الأثرُ الثاني سقط")
                return
            if mode == "fail_before":
                raise _Boom("رفضٌ قبلَ أيِّ تغيير")
            self.balance += 100
            self.applied += 1
            if mode == "fail_inside":
                raise _Boom("سقطَ بعدَ التغيير")

        return apply

    def restore(self) -> None:
        if self.balance != self.snapshot:
            self.compensated += 1
        self.balance = self.snapshot

    def relative(self) -> None:
        self.balance -= 100
        self.compensated += 1


def _run(
    b, world, key, *, mode, comp, idempotent, atomic=False, effects=(EFFECT, SEAL)
):
    comps = (
        Compensator(EFFECT.signature, comp, "عكسُ الرصيد", idempotent=idempotent),
        Compensator(SEAL.signature, lambda: None, "فكُّ الختم", idempotent=True),
    )
    return b.execute(
        _req(),
        declared_effects=effects,
        planner=lambda _p: effects,
        applier=world.applier(mode),
        operation_key=key,
        compensators=comps,
        applier_atomic=atomic,
    )


def _key() -> IdempotencyKey:
    return IdempotencyKey(scope="treasury", value="disc148")


def test_defaults_are_the_cautious_ones():
    """الافتراضُ «ربما طبَّق» ومعوِّضٌ غيرُ مُصرَّحٍ بثباتِه — لا العكس."""
    assert {f.name: f.default for f in dataclasses.fields(Compensator)}[
        "idempotent"
    ] is False
    param = inspect.signature(SovereignExecutionBoundary.execute).parameters[
        "applier_atomic"
    ]
    assert param.default is False


def test_change_then_raise_without_idempotent_compensator_is_final(tmp_path):
    """P6 بعدَ الإصلاح: لا تعويضَ بمعوِّضٍ نسبيٍّ غيرِ مُثبِّت، والعمليّةُ FAILED_FINAL، ولا إعادة."""
    b, led = _boundary(tmp_path)
    w = _World()
    with pytest.raises(IdempotencyError) as first:
        _run(b, w, _key(), mode="fail_inside", comp=w.relative, idempotent=False)
    assert any("Q-88" in n for n in getattr(first.value, "__notes__", []))
    record = led.get(_key())
    assert record.status is OperationStatus.FAILED_FINAL
    assert EFFECT.signature in record.applied_effect_signatures
    assert w.compensated == 0 and w.balance == 1100
    with pytest.raises(IdempotencyError):
        _run(b, w, _key(), mode="ok", comp=w.relative, idempotent=False)
    assert w.balance == 1100, "الإعادةُ بالمفتاحِ نفسِه لا تُطبِّقُ أثرًا ثانيًا"


def test_change_then_raise_with_idempotent_compensator_is_compensated(tmp_path):
    """P8 بعدَ الإصلاح: المعوِّضُ المُثبِّتُ يُشغَّلُ على الأثرِ «ربما طُبِّق» ثمّ تُعادُ مرّةً واحدة."""
    b, led = _boundary(tmp_path)
    w = _World()
    with pytest.raises(CompensationRequired) as first:
        _run(b, w, _key(), mode="fail_inside", comp=w.restore, idempotent=True)
    assert first.value.state_is_clean and first.value.unresolved == ()
    assert w.balance == 1000 and w.compensated == 1
    assert led.get(_key()).status is OperationStatus.FAILED_RETRYABLE
    _run(b, w, _key(), mode="ok", comp=w.restore, idempotent=True)
    assert w.balance == 1100 and led.get(_key()).status is OperationStatus.SUCCEEDED


def test_raise_before_change_with_idempotent_compensator_is_a_noop_compensation(
    tmp_path,
):
    """المعوِّضُ المُثبِّتُ على أثرٍ لم يقع لا يُغيِّرُ شيئًا، والمفتاحُ قابلٌ للإعادة."""
    b, led = _boundary(tmp_path)
    w = _World()
    with pytest.raises(CompensationRequired) as first:
        _run(b, w, _key(), mode="fail_before", comp=w.restore, idempotent=True)
    assert first.value.state_is_clean
    assert w.balance == 1000 and w.compensated == 0
    assert led.get(_key()).status is OperationStatus.FAILED_RETRYABLE


def test_declared_atomic_applier_keeps_retryable(tmp_path):
    """P4ذ: المُطبِّقُ المُصرِّحُ بالذرّيّةِ يرفعُ قبلَ التغيير ⇐ FAILED_RETRYABLE والإعادةُ تنجح."""
    b, led = _boundary(tmp_path)
    w = _World()
    with pytest.raises(IdempotencyError):
        _run(
            b,
            w,
            _key(),
            mode="fail_before",
            comp=w.relative,
            idempotent=False,
            atomic=True,
        )
    assert led.get(_key()).status is OperationStatus.FAILED_RETRYABLE
    _run(b, w, _key(), mode="ok", comp=w.relative, idempotent=False, atomic=True)
    assert w.balance == 1100


def test_undeclared_applier_raising_before_change_is_final(tmp_path):
    """الثمنُ المُعلَن (التصميم § 5): مُطبِّقٌ لم يُصرِّح ومعوِّضٌ غيرُ مُثبِّت ⇐ FAILED_FINAL ولو لم يُغيِّر."""
    b, led = _boundary(tmp_path)
    w = _World()
    with pytest.raises(IdempotencyError):
        _run(b, w, _key(), mode="fail_before", comp=w.relative, idempotent=False)
    assert led.get(_key()).status is OperationStatus.FAILED_FINAL
    assert w.balance == 1000


def test_idempotent_compensator_that_fails_is_final(tmp_path):
    """المعوِّضُ المُثبِّتُ إن فشلَ فالعمليّةُ FAILED_FINAL والأثرُ في البقيّة."""
    b, led = _boundary(tmp_path)
    w = _World()

    def broken() -> None:
        raise RuntimeError("المعوِّضُ تعذّر")

    with pytest.raises(CompensationRequired) as first:
        _run(b, w, _key(), mode="fail_inside", comp=broken, idempotent=True)
    assert not first.value.state_is_clean
    assert led.get(_key()).status is OperationStatus.FAILED_FINAL
    with pytest.raises(IdempotencyError):
        _run(b, w, _key(), mode="ok", comp=broken, idempotent=True)
    assert w.balance == 1100


def test_applied_effect_compensated_but_unresolved_in_flight_is_final(tmp_path):
    """أثرٌ عادَ فيُعوَّض، وأثرٌ ثانٍ ربما طُبِّقَ بلا معوِّضٍ مُثبِّت ⇐ FAILED_FINAL و`unresolved`."""
    b, led = _boundary(tmp_path)
    w = _World()
    comps = (
        Compensator(EFFECT.signature, w.relative, "عكسُ الرصيد", idempotent=False),
        Compensator(SEAL.signature, lambda: None, "فكُّ الختم", idempotent=False),
    )
    with pytest.raises(CompensationRequired) as first:
        b.execute(
            _req(),
            declared_effects=(EFFECT, SEAL),
            planner=lambda _p: (EFFECT, SEAL),
            applier=w.applier("fail_second"),
            operation_key=_key(),
            compensators=comps,
        )
    assert first.value.unresolved == (SEAL.signature,)
    assert first.value.outcome.state_is_clean and not first.value.state_is_clean
    assert w.balance == 1000 and w.compensated == 1
    record = led.get(_key())
    assert record.status is OperationStatus.FAILED_FINAL
    assert SEAL.signature in record.applied_effect_signatures


def test_planner_failure_is_not_maybe_applied(tmp_path):
    """فشلُ المخطِّطِ قبلَ أيِّ مُطبِّقٍ لا يُعَدُّ «ربما طُبِّق» — السلوكُ القائمُ كما هو."""
    b, led = _boundary(tmp_path)

    def planner(_p):
        raise _Boom("المخطِّطُ سقط")

    w = _World()
    with pytest.raises(IdempotencyError):
        b.execute(
            _req(),
            declared_effects=(EFFECT,),
            planner=planner,
            applier=w.applier("ok"),
            operation_key=_key(),
            compensators=(Compensator(EFFECT.signature, w.relative, "عكس"),),
        )
    assert led.get(_key()).status is OperationStatus.FAILED_RETRYABLE


def test_no_compensator_is_rejected_before_execution(tmp_path):
    """P7: أثرٌ مُغيِّرٌ بلا معوِّضٍ مُعلَنٍ لا يبلغُ المُطبِّقَ أصلًا."""
    b, led = _boundary(tmp_path)
    w = _World()
    with pytest.raises(CompensationNotDeclaredError):
        b.execute(
            _req(),
            declared_effects=(EFFECT,),
            planner=lambda _p: (EFFECT,),
            applier=w.applier("fail_inside"),
            operation_key=_key(),
            compensators=(),
        )
    assert w.applied == 0 and led.get(_key()) is None
