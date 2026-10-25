"""
الهدف: إثباتُ أنَّ إعادةَ صرفٍ بمفتاحِ حركةٍ معكوسةٍ تُرفَضُ ولا تُعادُ «نجاحًا متطابقًا» (WI-115 · Q-9 § 3.5)
النطاق: federal/executive/services — `StateTreasury._existing_idempotent` ومُناديه `disburse`
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-25 (WI-115)
تاريخ آخر تعديل: 2026-10-25

قاسَت وثيقةُ التصميمِ (`docs/audit/Q9_NESTING_DETECTOR_DESIGN.md` § 1 بند 4) أنَّ
`_existing_idempotent` يُرشِّحُ بالمستأجرِ والمفتاحِ وحدَهما، فإعادةُ الصرفِ بمفتاحِ حركةٍ
عكسَها `reverse_transaction` كانت تُعيدُ الحركةَ المعكوسةَ بـ`idempotent=True`.

ويُفحَصُ الشِّقّان: الرفضُ (الإصلاح)، وبقاءُ الإعادةِ المتطابقةِ لحركةٍ قائمةٍ (لا كسرَ
لعقدِ عدمِ التكرار). وما **لا** يُفحَصُ هنا: `post_funding` و`execute_decision_disbursement`
— يشتركانِ في الدالّةِ نفسِها ولم يُمارَسا في هذا الملفّ (حدٌّ مُعلَن).
"""

from __future__ import annotations

import uuid

import pytest

from amos_federation.common.database import get_session_factory
from amos_federation.services.state_treasury.models import TransactionModel
from amos_federation.services.state_treasury.service import EntityStateError
from tests.test_r7b_state_treasury import (  # noqa: F401 — مثبِّتاتُ pytest تُستورَدُ بأسمائها
    _allocate,
    _fiscal,
    _fresh_state,
    crown,
    registry,
    treasury,
)


def _disburse(store, context, fiscal, allocation, key: str, purpose: str) -> dict:
    return store.disburse(
        context=context,
        allocation_id=allocation["id"],
        expense_account_code=fiscal.expense["code"],
        amount="1500",
        purpose=purpose,
        official_id=fiscal.official["id"],
        idempotency_key=key,
    )


def _transactions() -> int:
    session = get_session_factory()()
    try:
        return session.query(TransactionModel).count()
    finally:
        session.close()


def test_replay_of_reversed_disbursement_is_refused(treasury, registry, crown) -> None:  # noqa: F811
    """صرفٌ ← عكسٌ ← إعادةُ الصرفِ بالمفتاحِ نفسِه: خطأٌ صريحٌ، لا نجاحٌ ولا حركةٌ جديدة."""
    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
    allocation = _allocate(treasury, crown, fiscal, amount="10000")
    key = f"wi115-{uuid.uuid4().hex[:8]}"
    posted = _disburse(treasury, crown, fiscal, allocation, key, "صرفٌ سيُعكَس")
    treasury.reverse_transaction(
        context=crown,
        reference=posted["reference"],
        reason="خطأٌ في المستند",
        official_id=fiscal.official["id"],
    )
    before = _transactions()

    with pytest.raises(EntityStateError, match="معكوسةٌ"):
        _disburse(treasury, crown, fiscal, allocation, key, "إعادةُ الطلبِ نفسِه")

    assert _transactions() == before, "الرفضُ لا يُنشئُ حركةً"
    budget = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])
    assert budget["spent"] == "0.0000", "المصروفُ بعدَ العكسِ صفرٌ ولم يتغيّرْ بالإعادة"


def test_replay_of_live_disbursement_stays_idempotent(treasury, registry, crown) -> None:  # noqa: F811
    """لا كسرَ لعقدِ عدمِ التكرار: الحركةُ القائمةُ تُعادُ بعينِها كما كانت."""
    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
    allocation = _allocate(treasury, crown, fiscal, amount="10000")
    key = f"wi115-{uuid.uuid4().hex[:8]}"
    first = _disburse(treasury, crown, fiscal, allocation, key, "صرفٌ مرّةً واحدة")
    second = _disburse(treasury, crown, fiscal, allocation, key, "الطلبُ نفسُه مُعادًا")
    assert second["id"] == first["id"]
    assert second.get("idempotent") is True
