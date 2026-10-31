"""الهدف: إثباتُ M1 § 2.7 الدفعة 1 — عمليّاتُ الخزانةِ الذرّيّةُ تعبرُ الحدَّ مرّةً واحدةً بفاعلِ التفويض
النطاق: `StateTreasury.establish_treasury` · `open_account` · `create_budget` · `allocate`
       · `post_funding` · `disburse` (ستُّ عمليّات) — و`reverse_transaction` **خارجَها عمدًا**
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-31 (W-755)
تاريخ آخر تعديل: 2026-10-31

القياسُ على **الأثرِ في القاعدة** وعلى **حصيلةِ الحدّ**، لا على وجودِ نداء:

- M1-1 العبور: كلُّ عمليّةٍ تعبرُ مرّةً واحدة، بالفعلِ الدستوريِّ من جدولِ التفويضِ وفاعلِه.
- M1-2 الفاعل: بفاعلٍ غيرِ الخزانةِ (EXECUTIVE · AGENT · SYSTEM) تُرفَضُ بـ R-003-1 ولا يُكتَبُ صفّ.
- M1-3 الأخطاء: خطأُ النطاقِ داخلَ المُطبِّقِ يصلُ المُناديَ بنوعِه هو، بلا أثر، وقابلًا للإعادة.
- M1-4 الإعادة: مفتاحُ الذرّيّةِ لا يُنتِجُ حركةً ثانية.
- M1-5 التعويض: المعوّضُ عكسٌ حقيقيٌّ — حذفُ الصفِّ للإنشاء، وقيدٌ عكسيٌّ للحركة.
- M1-6 الساكن: لا مسارَ كتابةٍ عامًّا للستِّ بجانبِ الحدّ، والعكسُ لم يُدَّعَ عبورُه.
"""

from __future__ import annotations

import ast
import inspect
import textwrap
import time
import uuid
from pathlib import Path
from typing import Any

import pytest

from amos_federation.common.database import get_session_factory
from amos_federation.common.money_delegation import resolve_money_delegation
from amos_federation.services.executive_core import money_authority
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    GuardedResult,
    _core_sovereignty,
)
from amos_federation.services.state_registry.service import StateRegistry, get_state_registry
from amos_federation.services.state_treasury import service as treasury_module
from amos_federation.services.state_treasury.models import (
    AccountModel,
    AllocationModel,
    BudgetModel,
    TransactionModel,
    TreasuryModel,
)
from amos_federation.services.state_treasury.service import (
    AllocationExceededError,
    BudgetExceededError,
    DuplicateCodeError,
    InsufficientFundsError,
    StateTreasury,
)
from tests.test_r7b_state_treasury import (  # noqa: F401 — المُثبِّتُ التلقائيُّ نفسُه
    _allocate,
    _code,
    _context,
    _fiscal,
    _fresh_state,
)

#: رفضُ البوّابةِ نفسُه من النواة — لا نوعَ مُعاد تسميتُه في الجسر.
SovereigntyViolation = _core_sovereignty("gateway").SovereigntyViolation

#: العمليّاتُ الستُّ ومدخلُها في جدولِ التفويض — مصدرٌ واحدٌ للاختبار والساكن.
CROSSED: dict[str, str] = {
    "establish_treasury": "treasury.establish",
    "open_account": "treasury.account.open",
    "create_budget": "treasury.budget.create",
    "allocate": "treasury.allocation.create",
    "post_funding": "treasury.funding.post",
    "disburse": "treasury.disbursement.post",
}


class RecordingAuthorizer(ConstitutionalAuthorizer):
    """المُصرِّحُ نفسُه يُسجِّلُ ما مرَّ — وراثةٌ لا تلمسُ منطقَ التصريح."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.calls: list[dict[str, Any]] = []
        self.results: list[GuardedResult] = []

    def guard_declared(self, action: str, target: str, **kwargs: Any) -> GuardedResult:
        self.calls.append({"action": action, "target": target, **kwargs})
        result = super().guard_declared(action, target, **kwargs)
        self.results.append(result)
        return result


class Factory:
    """مصنعُ مُصرِّحاتٍ يُسجِّلُ الفاعلَ الذي طُلِبَ لكلِّ عبور — ويُمكنُه فرضُ فاعلٍ آخر."""

    def __init__(self, tmp_path: Path, force_actor: str | None = None) -> None:
        self.tmp_path = tmp_path
        self.force_actor = force_actor
        self.requested: list[str] = []
        self.by_actor: dict[str, RecordingAuthorizer] = {}

    def __call__(self, actor: str) -> RecordingAuthorizer:
        self.requested.append(actor)
        effective = self.force_actor or actor
        if effective not in self.by_actor:
            self.by_actor[effective] = RecordingAuthorizer(
                actor=effective,
                idempotency_ledger_path=self.tmp_path / f"M1-{effective}-IDEM.json",
            )
        return self.by_actor[effective]

    @property
    def calls(self) -> list[dict[str, Any]]:
        return [c for a in self.by_actor.values() for c in a.calls]


@pytest.fixture
def crown():
    return _context("king")


@pytest.fixture
def registry() -> StateRegistry:
    return get_state_registry()


@pytest.fixture
def factory(tmp_path: Path) -> Factory:
    return Factory(tmp_path)


@pytest.fixture
def treasury(factory: Factory) -> StateTreasury:
    return StateTreasury(money_authorizer_factory=factory)


def _count(model: Any, **filters: Any) -> int:
    session = get_session_factory()()
    try:
        query = session.query(model)
        for name, value in filters.items():
            query = query.filter(getattr(model, name) == value)
        return query.count()
    finally:
        session.close()


# ── M1-1 العبورُ الواحدُ بفعلِ الجدولِ وفاعلِه ─────────────────────────────


def test_m1_1_each_atomic_surface_crosses_once_with_its_declared_action_and_actor(
    treasury: StateTreasury, registry: StateRegistry, crown, factory: Factory
) -> None:
    fiscal = _fiscal(treasury, registry, crown)
    allocation = _allocate(treasury, crown, fiscal)
    treasury.disburse(
        context=crown,
        allocation_id=allocation["id"],
        expense_account_code=fiscal.expense["code"],
        amount="100.0000",
        purpose="صرف",
        official_id=fiscal.official["id"],
    )
    # _fiscal: خزانة · 3 حسابات · موازنة · تمويل — ثمّ تخصيص · صرف = 8 عبورات.
    actions = [c["action"] for c in factory.calls]
    assert actions == [
        "establish_treasury",
        "open_account",
        "open_account",
        "open_account",
        "create_budget",
        "post_funding",
        "allocate_funds",
        "disburse_funds",
    ]
    assert set(factory.requested) == {"TREASURY"}
    for entrypoint, operation in CROSSED.items():
        delegation = resolve_money_delegation(operation, entrypoint=entrypoint)
        assert delegation.actor == "TREASURY"
        assert delegation.constitutional_action in actions
    results = factory.by_actor["TREASURY"].results
    assert len(results) == 8
    assert all(r.evidence.decision == "ALLOW" for r in results)
    # الدليلُ دليلُ العبورِ نفسِه (فعلُه وهدفُه)، لا سجلُّ المراجعةِ داخلَ المُطبِّق.
    assert [r.evidence.action for r in results] == actions
    assert [r.evidence.target for r in results] == [c["target"] for c in factory.calls]
    assert all(not r.is_replay for r in results)
    # الأثرُ المُعلَنُ واحدٌ ومحصورٌ في الهدف، ونوعُه يطابقُ الفعل.
    for call in factory.calls:
        (effect,) = call["declared_effects"]
        assert effect.resource == call["target"]
        expected = "TRANSFER" if call["action"] in ("post_funding", "disburse_funds") else "CREATE"
        assert effect.kind.value == expected
        assert len(call["compensators"]) == 1


# ── M1-2 الفاعلُ: غيرُ الخزانةِ يُرفَضُ بلا صفّ ──────────────────────────────


@pytest.mark.parametrize("actor", ["EXECUTIVE", "AGENT", "SYSTEM", "JUDICIAL", "LEGISLATIVE"])
def test_m1_2_a_non_treasury_actor_is_denied_by_r_003_1_and_writes_nothing(
    tmp_path: Path, crown, actor: str
) -> None:
    forced = Factory(tmp_path, force_actor=actor)
    treasury = StateTreasury(money_authorizer_factory=forced)
    code = _code("TRS")
    with pytest.raises(SovereigntyViolation) as denied:
        treasury.establish_treasury(context=crown, code=code, name="خزانة", currency="SAR")
    assert "R-003-1" in str(denied.value)
    assert _count(TreasuryModel, code=code) == 0


def test_m1_2b_a_non_treasury_actor_cannot_disburse_and_no_money_moves(
    treasury: StateTreasury, registry: StateRegistry, crown, tmp_path: Path
) -> None:
    fiscal = _fiscal(treasury, registry, crown)
    allocation = _allocate(treasury, crown, fiscal)
    before = _count(TransactionModel)
    executive = StateTreasury(money_authorizer_factory=Factory(tmp_path, force_actor="EXECUTIVE"))
    with pytest.raises(SovereigntyViolation) as denied:
        executive.disburse(
            context=crown,
            allocation_id=allocation["id"],
            expense_account_code=fiscal.expense["code"],
            amount="100.0000",
            purpose="صرف",
            official_id=fiscal.official["id"],
        )
    assert "R-003-1" in str(denied.value)
    assert _count(TransactionModel) == before


# ── M1-3 خطأُ النطاقِ يصلُ بنوعِه ولا أثرَ له ───────────────────────────────


def test_m1_3_domain_errors_inside_the_applier_keep_their_type_and_leave_no_row(
    treasury: StateTreasury, registry: StateRegistry, crown
) -> None:
    fiscal = _fiscal(treasury, registry, crown, limit_amount="1000.0000", funding="50.0000")
    with pytest.raises(BudgetExceededError):
        _allocate(treasury, crown, fiscal, amount="5000.0000")
    assert _count(AllocationModel) == 0
    allocation = _allocate(treasury, crown, fiscal, amount="500.0000")
    before = _count(TransactionModel)
    with pytest.raises(InsufficientFundsError):
        treasury.disburse(
            context=crown,
            allocation_id=allocation["id"],
            expense_account_code=fiscal.expense["code"],
            amount="100.0000",
            purpose="صرف",
            official_id=fiscal.official["id"],
            idempotency_key="M1-RETRY",
        )
    with pytest.raises(AllocationExceededError):
        treasury.disburse(
            context=crown,
            allocation_id=allocation["id"],
            expense_account_code=fiscal.expense["code"],
            amount="900.0000",
            purpose="صرف",
            official_id=fiscal.official["id"],
        )
    assert _count(TransactionModel) == before
    # الفشلُ قابلٌ للإعادةِ بالمفتاحِ نفسِه بعدَ زوالِ سببه — لا قفلَ نهائيّ.
    # مقيسٌ (W-755): معرّفُ الإذنِ في النواةِ بدقّةِ ثانية (`EP-<عقد>-<ثانية>`)، فإعادةُ
    # الطلبِ نفسِه في الثانيةِ نفسِها تُرفَضُ `PermitReplayError` (رفضٌ مغلق لا تمرير).
    # الانتظارُ هنا يقيسُ الإعادةَ الحقيقيّةَ لا يُخفي ذلك؛ والسلوكُ مُسجَّلٌ اكتشافًا.
    time.sleep(1.1)
    treasury.post_funding(
        context=crown,
        treasury_code=fiscal.treasury["code"],
        cash_account_code=fiscal.cash["code"],
        revenue_account_code=fiscal.revenue["code"],
        amount="1000.0000",
        purpose="تمويل",
        official_id=fiscal.official["id"],
    )
    retried = treasury.disburse(
        context=crown,
        allocation_id=allocation["id"],
        expense_account_code=fiscal.expense["code"],
        amount="100.0000",
        purpose="صرف",
        official_id=fiscal.official["id"],
        idempotency_key="M1-RETRY",
    )
    assert retried["status"] == "posted"
    assert _count(TransactionModel, idempotency_key="M1-RETRY") == 1


def test_m1_3b_duplicate_codes_are_still_duplicates_not_replays(
    treasury: StateTreasury, registry: StateRegistry, crown
) -> None:
    fiscal = _fiscal(treasury, registry, crown, funding=None)
    with pytest.raises(DuplicateCodeError):
        treasury.establish_treasury(
            context=crown, code=fiscal.treasury["code"], name="ثانية", currency="SAR"
        )
    with pytest.raises(DuplicateCodeError):
        treasury.open_account(
            context=crown,
            treasury_code=fiscal.treasury["code"],
            code=fiscal.cash["code"],
            name="ثانٍ",
            kind="cash",
        )
    with pytest.raises(DuplicateCodeError):
        treasury.create_budget(
            context=crown,
            treasury_code=fiscal.treasury["code"],
            institution_code=fiscal.institution["code"],
            code=fiscal.budget["code"],
            period="2026",
            limit_amount="10.0000",
        )


# ── M1-4 الإعادة ───────────────────────────────────────────────────────────


def test_m1_4_the_same_idempotency_key_moves_money_once(
    treasury: StateTreasury, registry: StateRegistry, crown, factory: Factory
) -> None:
    fiscal = _fiscal(treasury, registry, crown)
    allocation = _allocate(treasury, crown, fiscal)
    kwargs = dict(
        context=crown,
        allocation_id=allocation["id"],
        expense_account_code=fiscal.expense["code"],
        amount="100.0000",
        purpose="صرف",
        official_id=fiscal.official["id"],
        idempotency_key=f"M1-ONCE-{uuid.uuid4().hex[:6]}",
    )
    first = treasury.disburse(**kwargs)
    crossings = len(factory.calls)
    second = treasury.disburse(**kwargs)
    assert second["idempotent"] is True and second["id"] == first["id"]
    assert len(factory.calls) == crossings  # الإعادةُ لا تعبرُ ثانيةً ولا تُعلِنُ أثرًا
    assert _count(TransactionModel, idempotency_key=kwargs["idempotency_key"]) == 1


# ── M1-5 المعوّضُ عكسٌ حقيقيّ ───────────────────────────────────────────────


def test_m1_5_compensators_really_undo_what_the_crossing_did(
    treasury: StateTreasury, registry: StateRegistry, crown, factory: Factory
) -> None:
    fiscal = _fiscal(treasury, registry, crown)
    allocation = _allocate(treasury, crown, fiscal)
    paid = treasury.disburse(
        context=crown,
        allocation_id=allocation["id"],
        expense_account_code=fiscal.expense["code"],
        amount="100.0000",
        purpose="صرف",
        official_id=fiscal.official["id"],
    )
    balance_after_pay = treasury.account_balance(
        context=crown, treasury_code=fiscal.treasury["code"], account_code=fiscal.cash["code"]
    )["balance"]
    by_action = {c["action"]: c for c in factory.calls}

    # الحركة: قيدٌ عكسيٌّ يُعيدُ الرصيدَ ويُعلِّمُ الأصلَ `reversed` — لا حذف.
    by_action["disburse_funds"]["compensators"][0].apply()
    session = get_session_factory()()
    try:
        original = session.query(TransactionModel).filter_by(id=paid["id"]).one()
        assert original.status == "reversed"
        assert (
            session.query(TransactionModel).filter_by(reverses_transaction_id=paid["id"]).count()
            == 1
        )
    finally:
        session.close()
    restored = treasury.account_balance(
        context=crown, treasury_code=fiscal.treasury["code"], account_code=fiscal.cash["code"]
    )["balance"]
    assert restored != balance_after_pay

    # التخصيص: حذفُ صفِّه نفسِه (لا صرفَ قائمًا عليه بعدَ العكس؟ القيدُ العكسيُّ يشيرُ إليه،
    # فيُقاسُ المعوّضُ على تخصيصٍ جديدٍ نظيف).
    fresh = _allocate(treasury, crown, fiscal, amount="10.0000")
    allocate_call = [c for c in factory.calls if c["action"] == "allocate_funds"][-1]
    assert _count(AllocationModel, id=fresh["id"]) == 1
    allocate_call["compensators"][0].apply()
    assert _count(AllocationModel, id=fresh["id"]) == 0

    # الإنشاء: حذفُ صفِّ الخزانةِ المُؤسَّسة.
    lone = treasury.establish_treasury(
        context=crown, code=_code("TRS"), name="منفردة", currency="SAR"
    )
    establish_call = [c for c in factory.calls if c["action"] == "establish_treasury"][-1]
    assert _count(TreasuryModel, id=lone["id"]) == 1
    establish_call["compensators"][0].apply()
    assert _count(TreasuryModel, id=lone["id"]) == 0


# ── M1-6 الساكن ────────────────────────────────────────────────────────────


def _method_source(name: str) -> str:
    return textwrap.dedent(inspect.getsource(getattr(StateTreasury, name)))


def test_m1_6_the_six_publics_cross_in_their_own_body_once() -> None:
    for entrypoint, operation in CROSSED.items():
        body = _method_source(entrypoint)
        # العبورُ في جسدِ العامِّ نفسِه (شرطُ الجرد)، مرّةً واحدة، بعقدٍ واحدٍ ومُطبِّقٍ واحد.
        assert body.count("guard_declared(") == 1, entrypoint
        assert body.count("money_crossing_contract(") == 1, entrypoint
        assert body.count("settle_money_crossing(") == 1, entrypoint
        assert body.count("def _apply(") == 1, entrypoint
        assert f'operation="{operation}"' in body
        assert f'entrypoint="{entrypoint}"' in body
    # لا مُطبِّقَ مالٍ خاصٌّ على مستوى الصنفِ يُنادى من خارجِ العبور.
    tree = ast.parse(Path(treasury_module.__file__).read_text(encoding="utf-8"))
    methods = {
        node.name
        for cls in tree.body
        if isinstance(cls, ast.ClassDef) and cls.name == "StateTreasury"
        for node in cls.body
        if isinstance(node, ast.FunctionDef)
    }
    assert not {m for m in methods if m.endswith("_apply")}
    # والعكسُ لم يُدَّعَ عبورُه: معوِّضُه سؤالٌ مفتوح (M1 § 2.9).
    assert "guard_declared(" not in _method_source("reverse_transaction")
    assert "money_crossing_contract(" not in _method_source("reverse_transaction")


def test_m1_6b_the_unwrap_is_exact_and_does_not_swallow_sovereign_errors() -> None:
    body = textwrap.dedent(inspect.getsource(money_authority.settle_money_crossing))
    assert "type(exc) is idempotency_error and exc.__cause__ is not None" in body
    assert "raise exc.__cause__ from exc" in body
    # لا `except` يبتلع: كلُّ فرعٍ يرفع.
    handler = body.split("except Exception as exc:", 1)[1].split("if guarded.is_replay", 1)[0]
    # [W-765 · Q-88] فرعٌ ثالثٌ يرفع: فكُّ CompensationRequired النظيفِ وحدَه إلى سببِه الأصليّ.
    assert handler.count("raise") == 3 and "return" not in handler
    assert "isinstance(exc, compensation_required) and exc.state_is_clean" in handler
    assert "raise original from exc" in handler


def test_m1_6e_a_ledger_replay_reports_replayed_and_never_returns_a_value() -> None:
    """فرعُ الإعادةِ سلوكًا لا نصًّا: فحصُ التكرارِ في الخدمةِ يسبقُه عادةً، فيُقاسُ هنا وحدَه."""
    from types import SimpleNamespace

    outcome = SimpleNamespace(operation_key="state_treasury.disburse:K")
    replay = SimpleNamespace(is_replay=True, outcome=outcome, value={"moved": "again"})
    fresh = SimpleNamespace(is_replay=False, outcome=outcome, value={"moved": "once"})
    contract = {"target": "treasury/t/X"}
    assert money_authority.settle_money_crossing(lambda: replay, contract) == {
        "replayed": True,
        "operation_key": "state_treasury.disburse:K",
        "target": "treasury/t/X",
    }
    assert money_authority.settle_money_crossing(lambda: fresh, contract) == {"moved": "once"}


def test_m1_6d_the_crossing_authorizer_is_built_per_call_and_never_kept() -> None:
    """الآلةُ تُحفَظُ والفاعلُ لا (Q-19 · سابقةُ 2A): مُصرِّحانِ لنداءَين، وبوّابةٌ وحدٌّ واحدان."""
    first = money_authority._crossing_authorizer_for("TREASURY")
    second = money_authority._crossing_authorizer_for("TREASURY")
    assert first is not second
    assert first.gateway is second.gateway
    assert first.boundary is second.boundary
    # وبوّابةُ العبورِ غيرُ بوّابةِ المراجعة: دليلُ العبورِ لا يُقرأُ من سجلِّ مراجعةٍ لاحقة.
    assert money_authority._authorizer_for("TREASURY").gateway is not first.gateway


def test_m1_6c_accounts_budgets_without_crossing_are_not_left_behind(
    treasury: StateTreasury, registry: StateRegistry, crown, factory: Factory
) -> None:
    """كلُّ صفٍّ مُنشأٍ في النطاقِ له عبورٌ مُسجَّل بهدفٍ يحملُ رمزَه — لا كتابةَ خارجَ الحدّ."""
    fiscal = _fiscal(treasury, registry, crown)
    targets = [c["target"] for c in factory.calls]
    for code in (fiscal.treasury["code"], fiscal.cash["code"], fiscal.budget["code"]):
        assert any(code in t for t in targets), code
    assert _count(AccountModel, treasury_id=fiscal.treasury["id"]) == 3
    assert _count(BudgetModel, id=fiscal.budget["id"]) == 1
