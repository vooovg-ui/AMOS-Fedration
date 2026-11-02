"""W-796 · WI-127 · M1 الدفعة 2 (§ 2.10/§ 2.11): ثلاثةُ أسطحٍ مركَّبةٍ تعبرُ بعبورِ الخزانةِ الواحد.

الهدف: قياسُ — لا افتراضُ — أنَّ سجلَّ العمليّةِ وحالةَ المركَّبِ يُكتَبانِ **داخلَ** عبورِ `disburse`
نفسِه بـ`follow_up`، فإن فشلَ أثرٌ لاحقٌ عُكِسَت الحركةُ وحُذِفَ الصفُّ وعادت الحالة. والطفراتُ
الخمسُ المُكيَّفةُ في `docs/audit/evidence/W-796/` تُقتَلُ بهذه الفحوص (§ 2.11 قرار 7).

الأسطح: `execute_expenditure` · `execute_transfer` · `execute_scoped_disbursement`.
و`enforce_ruling_via_treasury` مؤجَّلٌ بـDISC-155 فلا فحصَ له هنا.
"""

from __future__ import annotations

import uuid
from decimal import Decimal
from typing import Any

import pytest

from amos_federation.services.executive_core.money_authority import MoneyFollowUp
from amos_federation.services.federal_state import service as federal_state_module
from amos_federation.services.federal_state.models import GovernmentOperationModel
from amos_federation.services.federal_state.service import get_federal_state
from amos_federation.services.national_economy.models import (
    EconomicTransferModel,
    ExpenditureAuthorizationModel,
)
from amos_federation.services.national_economy.service import get_national_economy
from amos_federation.services.national_registry.models import TransactionAuthorityModel
from amos_federation.services.national_registry.service import get_national_registry
from amos_federation.services.state_registry.service import get_state_registry
from amos_federation.services.state_treasury.models import LedgerEntryModel, TransactionModel
from amos_federation.services.state_treasury.service import get_state_treasury
from tests.test_r9_national_economic_state import (  # noqa: F401 — المُثبِّتُ التلقائيُّ نفسُه
    _authority_chain,
    _context,
    _federal_and_states,
    _fresh_state,
    _program,
    _session,
    _treasury_chain,
)


@pytest.fixture(autouse=True)
def _drop_reversals() -> Any:
    """بعدَ كلِّ فحص: احذفْ قيودَ الدفترِ والحركاتِ العكسيّة — مُثبِّتُ R9 لا يعرفُها
    (`reverses_transaction_id` مفتاحٌ أجنبيٌّ مقيَّد)، فتبقى القاعدةُ نظيفةً لمن بعدَه."""
    yield
    session = _session()
    try:
        session.query(TransactionAuthorityModel).delete()
        session.query(LedgerEntryModel).delete()
        session.query(TransactionModel).filter(
            TransactionModel.reverses_transaction_id.isnot(None)
        ).delete()
        session.commit()
    finally:
        session.close()


@pytest.fixture
def registry() -> Any:
    return get_state_registry()


@pytest.fixture
def national() -> Any:
    return get_national_registry()


@pytest.fixture
def treasury() -> Any:
    return get_state_treasury()


@pytest.fixture
def federation() -> Any:
    return get_federal_state()


@pytest.fixture
def economy() -> Any:
    return get_national_economy()


@pytest.fixture
def crown(national: Any) -> Any:
    """التاجُ بهويّةٍ كانونيّةٍ — كمُثبِّتِ اختبارِ R9 نفسِه."""
    context = _context("king", username="crown")
    identity = national.create_identity(context=context, identity_type="PERSON", label="التاج")
    national.link_principal(
        context=context, principal_id=context.principal_id, identity_id=identity["id"]
    )
    return context


def _counts() -> dict[str, int]:
    session = _session()
    try:
        return {
            "transactions": session.query(TransactionModel).count(),
            "reversals": session.query(TransactionModel)
            .filter(TransactionModel.reverses_transaction_id.isnot(None))
            .count(),
            "operations": session.query(GovernmentOperationModel).count(),
        }
    finally:
        session.close()


def _expenditure(economy, registry, national, federation, treasury, crown, user):  # noqa: ANN001, ANN202
    _federal, (state, _other) = _federal_and_states(federation, crown)
    officer = _context("royal", username=user)
    chain = _authority_chain(
        registry,
        national,
        federation,
        crown,
        officer,
        government_code=state["code"],
        scope="INSTITUTION",
        operations=(
            "economy.program.create",
            "economy.expenditure.authorize",
            "treasury.disbursement.post",
        ),
        max_amount="10000.0000",
    )
    money = _treasury_chain(treasury, crown, chain.institution["code"], chain.official["id"])
    program = _program(economy, officer, chain, "INSTITUTION")
    authorization = economy.authorize_expenditure(
        officer,
        program_code=program["code"],
        allocation_id=money["allocation"]["id"],
        institution_code=chain.institution["code"],
        scope_level="INSTITUTION",
        amount=Decimal("1200.0000"),
        purpose="صرفُ برنامجٍ بعبورٍ واحد",
    )
    return officer, chain, money, authorization


def _transfer(economy, registry, national, federation, treasury, crown, user):  # noqa: ANN001, ANN202
    _federal, (state, _other) = _federal_and_states(federation, crown)
    officer = _context("royal", username=user)
    chain = _authority_chain(
        registry,
        national,
        federation,
        crown,
        officer,
        government_code=state["code"],
        scope="INSTITUTION",
        operations=(
            "economy.program.create",
            "economy.grant.authorize",
            "treasury.disbursement.post",
        ),
        max_amount="10000.0000",
    )
    money = _treasury_chain(treasury, crown, chain.institution["code"], chain.official["id"])
    program = _program(economy, officer, chain, "INSTITUTION")
    beneficiary = national.create_identity(context=crown, identity_type="PERSON", label="مستفيد")
    transfer = economy.authorize_transfer(
        officer,
        transfer_kind="GRANT",
        program_code=program["code"],
        beneficiary_identity_id=beneficiary["id"],
        allocation_id=money["allocation"]["id"],
        institution_code=chain.institution["code"],
        scope_level="INSTITUTION",
        amount=Decimal("750.2500"),
        purpose="منحةٌ بعبورٍ واحد",
    )
    return officer, chain, money, transfer


def _fail_trace(monkeypatch: pytest.MonkeyPatch) -> None:
    """يُفشِلُ أثرَ التدقيقِ بعدَ التزامِ صفِّ العمليّة — الأثرُ «ربما طُبِّق» (§ 2.11 قرار 5)."""

    def _boom(*_args: Any, **_kwargs: Any) -> Any:
        raise RuntimeError("فشلٌ مُحقَنٌ بعدَ التزامِ سجلِّ العمليّة")

    monkeypatch.setattr(federal_state_module, "record_domain_trace", _boom)


# ── 1. المسارُ السليم: حركةٌ واحدةٌ وسجلٌّ واحدٌ وحالةٌ منفَّذة ─────────────────


def test_1_expenditure_writes_record_and_status_inside_the_crossing(
    economy, registry, national, federation, treasury, crown
) -> None:  # noqa: ANN001
    officer, _chain, money, authorization = _expenditure(
        economy, registry, national, federation, treasury, crown, "w796e1"
    )
    before = _counts()
    executed = economy.execute_expenditure(
        officer,
        treasury=treasury,
        reference=authorization["reference"],
        expense_account_code=money["expense"]["code"],
    )
    after = _counts()
    assert executed["status"] == "executed"
    assert executed["transaction_reference"] == executed["transaction"]["reference"]
    assert executed["operation_id"], "لكلِّ صرفٍ أثرُ عمليةٍ حكوميّ"
    assert "follow_up" not in executed["transaction"], "نتائجُ الصفوفِ لا تتسرّبُ إلى المُنادي"
    assert after["transactions"] == before["transactions"] + 1
    assert after["operations"] == before["operations"] + 1
    session = _session()
    try:
        row = session.get(GovernmentOperationModel, executed["operation_id"])
        assert row is not None and row.transaction_reference == executed["transaction_reference"]
    finally:
        session.close()


def test_2_transfer_writes_record_and_status_inside_the_crossing(
    economy, registry, national, federation, treasury, crown
) -> None:  # noqa: ANN001
    officer, _chain, money, transfer = _transfer(
        economy, registry, national, federation, treasury, crown, "w796t1"
    )
    before = _counts()
    paid = economy.execute_transfer(
        officer,
        treasury=treasury,
        reference=transfer["reference"],
        expense_account_code=money["expense"]["code"],
    )
    after = _counts()
    assert paid["status"] == "executed" and paid["operation_id"]
    assert paid["transaction_reference"] == paid["transaction"]["reference"]
    assert after["transactions"] == before["transactions"] + 1
    assert after["operations"] == before["operations"] + 1


# ── 2. فشلُ أثرٍ لاحقٍ يُعوِّضُ ما قبلَه بالحدِّ نفسِه (الطفرتان ① و②) ────────────


def test_3_expenditure_late_failure_reverses_money_and_removes_the_record(
    economy, registry, national, federation, treasury, crown, monkeypatch
) -> None:  # noqa: ANN001
    officer, _chain, money, authorization = _expenditure(
        economy, registry, national, federation, treasury, crown, "w796e3"
    )
    before = _counts()
    _fail_trace(monkeypatch)
    with pytest.raises(RuntimeError, match="فشلٌ مُحقَن"):
        economy.execute_expenditure(
            officer,
            treasury=treasury,
            reference=authorization["reference"],
            expense_account_code=money["expense"]["code"],
        )
    after = _counts()
    assert after["reversals"] == before["reversals"] + 1, "الحركةُ عُكِسَت بقيدٍ عكسيّ"
    assert after["operations"] == before["operations"], "صفُّ العمليّةِ حُذِفَ بمعوِّضِه"
    session = _session()
    try:
        row = session.get(ExpenditureAuthorizationModel, authorization["id"])
        assert row.status == "authorized" and row.operation_id is None
    finally:
        session.close()


def test_4_transfer_late_failure_reverses_money_and_removes_the_record(
    economy, registry, national, federation, treasury, crown, monkeypatch
) -> None:  # noqa: ANN001
    officer, _chain, money, transfer = _transfer(
        economy, registry, national, federation, treasury, crown, "w796t4"
    )
    before = _counts()
    _fail_trace(monkeypatch)
    with pytest.raises(RuntimeError, match="فشلٌ مُحقَن"):
        economy.execute_transfer(
            officer,
            treasury=treasury,
            reference=transfer["reference"],
            expense_account_code=money["expense"]["code"],
        )
    after = _counts()
    assert after["reversals"] == before["reversals"] + 1
    assert after["operations"] == before["operations"]
    session = _session()
    try:
        row = session.get(EconomicTransferModel, transfer["id"])
        assert row.status == "authorized" and row.operation_id is None
    finally:
        session.close()


def test_5_status_update_failure_restores_fields_and_removes_the_record(
    economy, registry, national, federation, treasury, crown, monkeypatch
) -> None:  # noqa: ANN001
    """فشلُ الأثرِ الأخيرِ (UPDATE) بعدَ التزامِه: الحقولُ تعودُ والصفُّ يُحذَفُ والحركةُ تُعكَس."""
    officer, _chain, money, authorization = _expenditure(
        economy, registry, national, federation, treasury, crown, "w796e5"
    )
    before = _counts()

    def _boom(_row: Any) -> Any:
        raise RuntimeError("فشلٌ مُحقَنٌ بعدَ التزامِ الحالة")

    monkeypatch.setattr(economy, "_expenditure_dict", _boom)
    with pytest.raises(RuntimeError, match="فشلٌ مُحقَن"):
        economy.execute_expenditure(
            officer,
            treasury=treasury,
            reference=authorization["reference"],
            expense_account_code=money["expense"]["code"],
        )
    after = _counts()
    assert after["reversals"] == before["reversals"] + 1
    assert after["operations"] == before["operations"]
    session = _session()
    try:
        row = session.get(ExpenditureAuthorizationModel, authorization["id"])
        assert row.status == "authorized"
        assert row.transaction_reference is None and row.operation_id is None
    finally:
        session.close()


# ── 3. الصرفُ المُنطَّق: السجلُّ في العبور والإعادةُ لا تكتبُ سجلًّا ثانيًا ────────


def _scoped(federation, chain, money, treasury, officer, key, amount="1000.0000"):  # noqa: ANN001, ANN202
    return federation.execute_scoped_disbursement(
        officer,
        treasury=treasury,
        institution_code=chain.institution["code"],
        level="INSTITUTION",
        allocation_id=money["allocation"]["id"],
        expense_account_code=money["expense"]["code"],
        amount=Decimal(amount),
        purpose="صرفٌ مُنطَّقٌ بعبورٍ واحد",
        idempotency_key=key,
    )


def test_6_scoped_disbursement_records_inside_and_replay_writes_no_second_record(
    economy, registry, national, federation, treasury, crown
) -> None:  # noqa: ANN001
    officer, chain, money, _authorization = _expenditure(
        economy, registry, national, federation, treasury, crown, "w796s6"
    )
    key = f"idem-{uuid.uuid4().hex[:8]}"
    before = _counts()
    executed = _scoped(federation, chain, money, treasury, officer, key)
    assert executed["kind"] == "TREASURY" and executed["status"] == "executed"
    assert executed["transaction_reference"] == executed["transaction"]["reference"]
    middle = _counts()
    assert middle["transactions"] == before["transactions"] + 1
    assert middle["operations"] == before["operations"] + 1
    replay = _scoped(federation, chain, money, treasury, officer, key)
    assert replay["idempotent"] is True and replay["id"] is None
    assert _counts() == middle, "الإعادةُ بالمفتاحِ نفسِه لا تكتبُ حركةً ولا سجلًّا ثانيًا"


def test_7_scoped_disbursement_late_failure_reverses_and_removes(
    economy, registry, national, federation, treasury, crown, monkeypatch
) -> None:  # noqa: ANN001
    officer, chain, money, _authorization = _expenditure(
        economy, registry, national, federation, treasury, crown, "w796s7"
    )
    before = _counts()
    _fail_trace(monkeypatch)
    with pytest.raises(RuntimeError, match="فشلٌ مُحقَن"):
        _scoped(federation, chain, money, treasury, officer, f"idem-{uuid.uuid4().hex[:8]}")
    after = _counts()
    assert after["reversals"] == before["reversals"] + 1
    assert after["operations"] == before["operations"]


# ── 4. صفٌّ بلا معوِّضٍ يُرفَضُ قبلَ أيِّ كتابة (الطفرة ⑤) ─────────────────────


def test_8_follow_up_without_compensator_is_refused_before_any_write(
    economy, registry, national, federation, treasury, crown
) -> None:  # noqa: ANN001
    officer, chain, money, _authorization = _expenditure(
        economy, registry, national, federation, treasury, crown, "w796n8"
    )
    before = _counts()
    session = _session()
    try:
        official_id = chain.official["id"]
    finally:
        session.close()
    with pytest.raises(Exception) as caught:  # noqa: PT011 — الحدُّ يرفعُ صنفَه
        treasury.disburse(
            context=officer,
            allocation_id=money["allocation"]["id"],
            expense_account_code=money["expense"]["code"],
            amount=Decimal("10.0000"),
            purpose="صفٌّ بلا معوِّض",
            official_id=official_id,
            idempotency_key=f"idem-{uuid.uuid4().hex[:8]}",
            follow_up=(
                MoneyFollowUp(
                    kind="CREATE",
                    suffix="orphan",
                    detail="أثرٌ بلا معوِّض",
                    apply=lambda _t: None,
                    undo=None,
                    undo_description="—",
                ),
            ),
        )
    assert "Uncompensatable" in type(caught.value).__name__ or "معوّض" in str(caught.value)
    assert _counts() == before, "لا حركةَ ولا سجلَّ قبلَ ربطِ المعوِّضات"


def test_9_follow_up_kind_outside_the_declared_set_is_refused(treasury) -> None:  # noqa: ANN001
    from amos_federation.services.executive_core.money_authority import money_crossing_contract

    with pytest.raises(ValueError, match="CREATE"):
        money_crossing_contract(
            operation="treasury.disbursement.post",
            entrypoint="disburse",
            target="treasury/t/allocations/a/transactions/k",
            effect_kind="TRANSFER",
            detail="—",
            key_value="k",
            apply=lambda: {},
            undo=lambda _r: None,
            undo_description="—",
            metadata={},
            follow_up=(
                MoneyFollowUp(
                    kind="TRANSFER",
                    suffix="x",
                    detail="مالٌ ثانٍ",
                    apply=lambda _t: None,
                    undo=lambda _r: None,
                    undo_description="—",
                ),
            ),
        )
