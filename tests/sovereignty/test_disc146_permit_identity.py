"""الهدف: قياسُ إصلاحِ DISC-146 — هويّةُ الإذنِ السياديِّ فريدةٌ لكلِّ إصدارٍ لا لكلِّ ثانية.

النطاق: `core/sovereignty/enforcement.py` (`issue_permit`) عبرَ `SovereignExecutionBoundary`
الحقيقيِّ بسجلّاتٍ على القرص · الساعةُ مُجمَّدةٌ في وحدةِ الإذنِ وحدَها فلا يتعلّقُ الحكمُ
بحظِّ حدِّ الثانية.
المالك: tests/sovereignty/ — البندُ WI-125 · القيدُ W-762 · قرارُ المالكِ Q-87 (7).
تاريخ الإنشاء: 2026-10-31
تاريخ آخر تعديل: 2026-10-31

ما يُثبَت (التصميمُ `docs/audit/DISC146_PERMIT_IDENTITY_DESIGN.md` § 5):
- P1: إذنانِ للعقدِ نفسِه في الثانيةِ نفسِها مختلفان، ولا يحوي أيٌّ منهما الطابعَ الزمنيّ.
- P2: الأثرُ الثاني يفشلُ فيُعوَّضُ تعويضًا نظيفًا ⇒ الإعادةُ في الثانيةِ نفسِها تنجحُ مرّةً واحدة.
- P3: تعويضٌ غيرُ نظيف ⇒ `FAILED_FINAL` والإعادةُ مرفوضةٌ (حراسةُ Q-12 في 1H لا في الإذن).
- P4: فشلٌ قبلَ أيِّ أثر ⇒ الإعادةُ في الثانيةِ نفسِها تنجحُ مرّةً واحدة.
- P5: إعادةُ تقديمِ الإذنِ نفسِه مرفوضةٌ (`PermitReplayError`).
- العبثُ بـ`permit_id` بعدَ الإصدارِ يُبطِلُ التوقيع.
"""

from __future__ import annotations

import dataclasses
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest
from cryptography.hazmat.primitives.asymmetric import ed25519

from core.constitutional_engine.engine import ConstitutionalEngine
from core.constitutional_engine.ledger import ConstitutionalLedger
from core.constitutional_engine.model import ActionRequest, Branch
from core.sovereignty import enforcement as enf
from core.sovereignty.compensation import Compensator
from core.sovereignty.contract import EffectKind, SovereignEffect, bind_contract
from core.sovereignty.enforcement import (
    ConsumedPermitLedger,
    PermitInvalidError,
    PermitReplayError,
    PolicyEnforcementPoint,
    issue_permit,
)
from core.sovereignty.enforcement_boundary import SovereignExecutionBoundary
from core.sovereignty.gateway import SovereignGateway
from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger, OperationStatus

FIXED = datetime(2026, 10, 31, 12, 0, 0, tzinfo=timezone.utc)
TARGET = "treasury/account-A"
CREDIT = SovereignEffect(kind=EffectKind.WRITE, resource=TARGET, detail="قيد")
SEAL = SovereignEffect(kind=EffectKind.CREATE, resource=TARGET, detail="ختم")


class _Frozen(datetime):
    @classmethod
    def now(cls, tz=None):  # noqa: D102
        return FIXED if tz is None else FIXED.astimezone(tz)


@pytest.fixture()
def frozen(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(enf, "datetime", _Frozen)


@pytest.fixture()
def boundary(tmp_path: Path, frozen: None):
    gateway = SovereignGateway(
        ConstitutionalEngine(ledger=ConstitutionalLedger(tmp_path / "l.jsonl"))
    )
    ledger = IdempotencyLedger(tmp_path / "IDEMPOTENCY.json")
    consumed = ConsumedPermitLedger(tmp_path / "CONSUMED.json")
    return (
        SovereignExecutionBoundary(
            gateway=gateway, idempotency_ledger=ledger, consumed_permits=consumed
        ),
        ledger,
        consumed,
    )


def _request() -> ActionRequest:
    return ActionRequest(
        actor=Branch.EXECUTIVE, action="credit_account", target=TARGET, channel="official"
    )


def _run(b: SovereignExecutionBoundary, key: IdempotencyKey, state: dict, *, mode: str,
         broken_comp: bool = False) -> None:
    effects = (CREDIT, SEAL)

    def apply(effect: SovereignEffect) -> None:
        if mode == "fail_before":
            raise RuntimeError("فشلٌ قبلَ أيِّ أثر")
        if effect.signature == SEAL.signature:
            if mode == "fail_second":
                raise RuntimeError("الأثرُ الثاني فشل")
            return
        state["balance"] += 100
        state["applied"] += 1

    def undo() -> None:
        if broken_comp:
            raise RuntimeError("المعوِّضُ تعذّر")
        state["balance"] -= 100

    b.execute(
        _request(),
        declared_effects=effects,
        planner=lambda _: effects,
        applier=apply,
        operation_key=key,
        compensators=(
            Compensator(effect_signature=CREDIT.signature, apply=undo, description="عكس"),
            Compensator(effect_signature=SEAL.signature, apply=lambda: None, description="فك"),
        ),
    )


def test_p1_two_permits_in_one_second_differ_and_carry_no_timestamp(frozen: None) -> None:
    contract = bind_contract(
        actor="EXECUTIVE",
        action="credit_account",
        target=TARGET,
        request_fingerprint="fp",
        declared_effects=(CREDIT,),
    )
    key = ed25519.Ed25519PrivateKey.generate()
    ids = [
        issue_permit(
            contract=contract,
            request_fingerprint="fp",
            decision="ALLOW",
            ledger_entry_hash=None,
            private_key=key,
            now=FIXED,
        ).permit_id
        for _ in range(2)
    ]
    assert ids[0] != ids[1], "إذنانِ في الثانيةِ نفسِها متطابقان — عادَ DISC-146."
    assert all(i.startswith(f"EP-{contract.contract_id[3:]}-") for i in ids)
    assert all(str(int(FIXED.timestamp())) not in i for i in ids), "عادَ الوقتُ إلى المعرّف."


@pytest.mark.parametrize("mode", ["fail_second", "fail_before"], ids=["P2", "P4"])
def test_p2_p4_same_second_retry_succeeds_exactly_once(boundary, mode: str) -> None:
    b, ledger, consumed = boundary
    key = IdempotencyKey(scope="treasury", value=f"disc146-{mode}")
    state = {"balance": 1000, "applied": 0}
    with pytest.raises(Exception):
        _run(b, key, state, mode=mode)
    assert ledger.get(key).status is OperationStatus.FAILED_RETRYABLE
    assert state["balance"] == 1000, "بقيَ أثرٌ بعدَ الفشلِ الأوّل."

    _run(b, key, state, mode="ok")  # الثانيةُ نفسُها: الساعةُ مُجمَّدة

    assert ledger.get(key).status is OperationStatus.SUCCEEDED
    assert state["balance"] == 1100, "الإعادةُ المشروعةُ لم تُنتِجْ أثرَها مرّةً واحدة."
    assert consumed.count() == 2, "لكلِّ محاولةٍ إذنٌ مستقلٌّ مُستهلَك."


def test_p3_unclean_compensation_stays_closed_regardless_of_permit(boundary) -> None:
    b, ledger, _ = boundary
    key = IdempotencyKey(scope="treasury", value="disc146-p3")
    state = {"balance": 1000, "applied": 0}
    with pytest.raises(Exception):
        _run(b, key, state, mode="fail_second", broken_comp=True)
    assert ledger.get(key).status is OperationStatus.FAILED_FINAL
    with pytest.raises(Exception):
        _run(b, key, state, mode="ok")
    assert ledger.get(key).status is OperationStatus.FAILED_FINAL
    assert state["applied"] == 1, "أُعيدَ تنفيذٌ فوقَ أثرٍ باقٍ — نُقِضَ Q-12."


def test_p5_resubmitting_the_same_permit_is_rejected(boundary) -> None:
    b, _, _ = boundary
    pep = b.policy_enforcement_point
    permit = b.gateway.decide(_request(), declared_effects=(CREDIT,))
    pep.enforce(permit, planner=lambda _: (CREDIT,), applier=lambda e: None)
    with pytest.raises(PermitReplayError):
        pep.enforce(permit, planner=lambda _: (CREDIT,), applier=lambda e: None)


def test_tampering_with_permit_id_breaks_the_signature(tmp_path: Path, frozen: None) -> None:
    contract = bind_contract(
        actor="EXECUTIVE",
        action="credit_account",
        target=TARGET,
        request_fingerprint="fp",
        declared_effects=(CREDIT,),
    )
    key = ed25519.Ed25519PrivateKey.generate()
    permit = issue_permit(
        contract=contract,
        request_fingerprint="fp",
        decision="ALLOW",
        ledger_entry_hash=None,
        private_key=key,
        now=FIXED,
    )
    forged = dataclasses.replace(permit, permit_id=permit.permit_id[:-1] + "0")
    if forged.permit_id == permit.permit_id:
        forged = dataclasses.replace(permit, permit_id=permit.permit_id[:-1] + "1")
    pep = PolicyEnforcementPoint(
        verifying_key=key.public_key(), consumed=ConsumedPermitLedger(tmp_path / "C.json")
    )
    pep.verify(permit, now=FIXED + timedelta(seconds=1))
    with pytest.raises(PermitInvalidError):
        pep.verify(forged, now=FIXED + timedelta(seconds=1))
