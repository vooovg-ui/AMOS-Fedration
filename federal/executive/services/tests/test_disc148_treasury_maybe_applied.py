"""DISC-148/DISC-149 · Q-88: مُطبِّقاتُ الخزانةِ تُعوَّضُ إذا سقطَ ما بعدَ الالتزام.

الهدف: تثبيتُ ما قِيسَ في `evidence/W-765/treasury_atomicity_probe_after.txt`: فشلٌ في
       `record_domain_trace` بعدَ `session.commit()` لا يتركُ أثرًا، والإعادةُ بلا مفتاحٍ
       لا تُضاعِفُ المال، والمعوِّضُ لا يمسُّ حركةً ليست للعمليّة.
النطاق: `StateTreasury` على SQLite الاختبار · الحقنُ بـmonkeypatch على `record_domain_trace`.
المالك: Perplexity Computer (قيدُ W-765 · البندُ WI-125).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

from amos_federation.common.database import get_session_factory
from amos_federation.services.state_registry.service import get_state_registry
from amos_federation.services.state_treasury import service as treasury_module
from amos_federation.services.state_treasury.models import AllocationModel, TransactionModel
from amos_federation.services.state_treasury.service import StateTreasury
from tests.test_r7b_state_treasury import (  # noqa: F401 — المُثبِّتُ التلقائيُّ نفسُه
    _allocate,
    _context,
    _fiscal,
    _fresh_state,
)
from tests.test_w755_m1_treasury_single_crossing import Factory

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path


class _FailTraceOnce:
    def __init__(self, real: Callable[..., Any]) -> None:
        self.real = real
        self.armed = False

    def __call__(self, *a: Any, **k: Any) -> Any:
        if self.armed:
            self.armed = False
            raise RuntimeError("حقنُ W-765: فشلُ التتبّعِ بعدَ الالتزام")
        return self.real(*a, **k)


def _count(model: Any) -> int:
    s = get_session_factory()()
    try:
        return s.query(model).count()
    finally:
        s.close()


def _setup(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, *, allocate: bool = False):
    crown = _context("king")
    treasury = StateTreasury(money_authorizer_factory=Factory(tmp_path))
    fiscal = _fiscal(treasury, get_state_registry(), crown)
    allocation = _allocate(treasury, crown, fiscal) if allocate else None
    injector = _FailTraceOnce(treasury_module.record_domain_trace)
    monkeypatch.setattr(treasury_module, "record_domain_trace", injector)
    return crown, treasury, fiscal, allocation, injector


def _cash(treasury: StateTreasury, crown: Any, fiscal: Any) -> str:
    return str(
        treasury.account_balance(
            context=crown, treasury_code=fiscal.treasury["code"], account_code=fiscal.cash["code"]
        )["balance"]
    )


def _fund(treasury, crown, fiscal, **extra):
    return treasury.post_funding(
        context=crown,
        treasury_code=fiscal.treasury["code"],
        cash_account_code=fiscal.cash["code"],
        revenue_account_code=fiscal.revenue["code"],
        amount="100.0000",
        purpose="DISC-149",
        official_id=fiscal.official["id"],
        **extra,
    )


def test_keyless_funding_retry_does_not_double_money(tmp_path, monkeypatch):
    crown, treasury, fiscal, _, injector = _setup(tmp_path, monkeypatch)
    before = _cash(treasury, crown, fiscal)
    injector.armed = True
    with pytest.raises(RuntimeError):
        _fund(treasury, crown, fiscal)
    assert _cash(treasury, crown, fiscal) == before, "الأثرُ عُوِّضَ بقيدٍ عكسيّ"
    _fund(treasury, crown, fiscal)
    assert _cash(treasury, crown, fiscal) == "50100.0000"


def test_keyless_disburse_retry_does_not_double_money(tmp_path, monkeypatch):
    crown, treasury, fiscal, allocation, injector = _setup(tmp_path, monkeypatch, allocate=True)

    def disburse():
        return treasury.disburse(
            context=crown,
            allocation_id=allocation["id"],
            expense_account_code=fiscal.expense["code"],
            amount="100.0000",
            purpose="DISC-149",
            official_id=fiscal.official["id"],
        )

    injector.armed = True
    with pytest.raises(RuntimeError):
        disburse()
    assert _cash(treasury, crown, fiscal) == "50000.0000"
    disburse()
    assert _cash(treasury, crown, fiscal) == "49900.0000"


def test_allocate_retry_creates_exactly_one_allocation(tmp_path, monkeypatch):
    crown, treasury, fiscal, _, injector = _setup(tmp_path, monkeypatch)
    injector.armed = True
    with pytest.raises(RuntimeError):
        _allocate(treasury, crown, fiscal, amount="100.0000")
    assert _count(AllocationModel) == 0
    _allocate(treasury, crown, fiscal, amount="100.0000")
    assert _count(AllocationModel) == 1


def test_compensator_never_reverses_a_transaction_of_another_operation(tmp_path, monkeypatch):
    """نداءٌ ثانٍ بالمرجعِ نفسِه يُعادُ فيه الحركةُ الأولى، ثمّ يسقطُ ما بعدَه إن نُودِي:
    المعوِّضُ يقرأُ بمعرِّفِ هذه العمليّةِ (المُولَّدِ قبلَ العبور) فلا يعكسُ الحركةَ الأولى."""
    crown, treasury, fiscal, _, injector = _setup(tmp_path, monkeypatch)
    first = _fund(treasury, crown, fiscal, reference="TX-DISC149-DUP")
    injector.armed = True
    try:
        _fund(treasury, crown, fiscal, reference="TX-DISC149-DUP")
        replay = "OK"
    except RuntimeError as exc:  # الحقنُ وقعَ في مسارِ الإعادة — والمطلوبُ ما بعدَه
        replay = type(exc).__name__
    assert replay in {"OK", "RuntimeError"}
    s = get_session_factory()()
    try:
        row = s.get(TransactionModel, first["id"])
        assert row is not None and row.status == "posted"
    finally:
        s.close()
    assert _cash(treasury, crown, fiscal) == "50100.0000"
