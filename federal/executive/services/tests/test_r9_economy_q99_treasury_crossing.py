"""الهدف: عبورُ أسطحِ الخزانةِ الثلاثةِ في `national_economy` الحدَّ بفاعلِ الخزانة (Q-99 · W-823).

التعريف: قرارُ المالكِ Q-99 (التوجيه 44 § 1) جعلَ الدفعةَ 3 أسطحَ الخزانةِ الثلاثة:
`authorize_expenditure` (فعلٌ قائم) · `authorize_procurement` (`award_procurement` ومدخلُ معجمٍ
وتفويضٌ جديدان) · `authorize_transfer` (فعلٌ جديدٌ زوجُ `execute_transfer`) — وتصميمُ العبورِ
في `docs/audit/Q83C_LEXICON_TABLE_DESIGN.md` § 8. يقيسُ هذا الملفُّ على قاعدةٍ حقيقيّةٍ ومحرّكٍ
حقيقيٍّ بلا محاكاةٍ للنواة، لكلِّ حالةٍ من الأربع (المنحةُ والإعانةُ عمليّتانِ لسطحٍ واحد):

  الصنفُ 0 · المفردات: الأفعالُ في `TREASURY_ACTIONS` ومالكُها الخزانة، والعمليّاتُ في المعجم،
            ومداخلُ التفويضِ بفاعلِ TREASURY.
  الصنفُ 1 · الرفضُ قبلَ الكتابة: مُصرِّحٌ بفاعلٍ غيرِ الخزانة (EXECUTIVE — فاعلُ الخدمةِ قبلَ
            Q-99 — وJUDICIAL) ⇒ رفضٌ بـR-003-1 ولا صفَّ ولا قرارَ يُكتَب.
  الصنفُ 2 · النجاحُ بالدليل: الفاعلُ المطلوبُ من الجدولِ TREASURY وحدَه · عبورٌ واحد · الفعلُ
            حرفيًّا · أثرٌ معلَنٌ واحدٌ على `economy/{tenant}/<المجموعة>/<المرجع>` · قيدٌ في النواة.
  الصنفُ 3 · لا إعادةَ مدّعاة: لا مفتاحَ طبيعيَّ للإجازات، فنداءانِ ⇒ صفّانِ بمفتاحَين مختلفَين.
  الصنفُ 4 · التعويض (DISC-146/148/149 · Q-88): فشلُ `_announce` بعدَ التثبيت ⇒ «ربما نُفِّذ» ⇒
            يُحذَفُ الصفُّ وقرارُه ويُرفَعُ السببُ الأصليُّ بملاحظةِ [Q-88]؛ وإن فشلَ المعوِّضُ
            أيضًا ⇒ `CompensationRequired` غيرُ نظيف (FAILED_FINAL) لا نجاحٌ صامت.
  الصنفُ 6 · المسارُ كاملًا بتوصيلِ الإنتاج: `NationalEconomy()` بلا مَنفذِ حقن ⇒ مُصرِّحُ الخزانةِ
            من نقطةِ الفرضِ الواحدة ⇒ البوّابة (AUTHORIZED ثمّ COMPLETED بفاعلِ TREASURY) ⇒ قيدُ
            `CONSTITUTIONAL_VERDICT` في سجلِّ النواةِ نفسِه، و`verify_chain()` فارغ.

اسمُ الملفِّ `test_r9_economy_…` ليُجمَعَ **قبلَ** `test_r9_national_economic_state` فيُنظِّفَ مثبِّتُها
`_fresh_state` صفوفَه (درسُ W-818/W-820 · DISC-161).
[تحديثٌ مؤرَّخٌ (2026-11-07 · W-826 · DISC-161):] عُولِجَ الجذرُ — مثبِّتُ R9 صارَ ينظِّفُ
بعدَ الاختبارِ أيضًا (`yield`) فلم يعدْ نجاحُ الحزمةِ يعتمدُ على هذا الترتيبِ.
النطاق: `national_economy/service.py` وحدَه؛ والطفراتُ في `docs/audit/evidence/W-823/q99_mutation_probe.py`.
المالك: Perplexity Computer (WI-127 · قيدُ W-823).
"""

from __future__ import annotations

from decimal import Decimal
from typing import Any

import pytest

from amos_federation.common.money_delegation import MONEY_DELEGATIONS
from amos_federation.services.executive_core import money_authority
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from amos_federation.services.national_economy.models import (
    EconomicDecisionModel,
    EconomicTransferModel,
    ExpenditureAuthorizationModel,
    ProcurementModel,
)
from amos_federation.services.national_economy.service import NationalEconomy
from tests.test_r9_national_economic_state import (  # noqa: F401 — مثبِّتاتُ R9 نفسُها
    _authority_chain,
    _code,
    _federal_and_states,
    _fresh_state,
    _program,
    _session,
    _treasury_chain,
    crown,
    economy,
    federation,
    national,
    registry,
    treasury,
)

#: الحالةُ ⇒ (الفعلُ الدستوريّ · العمليّة · المدخل · النموذج · المجموعةُ في الهدف)
CASES: dict[str, tuple[str, str, str, Any, str]] = {
    "expenditure": (
        "authorize_expenditure",
        "economy.expenditure.authorize",
        "authorize_expenditure",
        ExpenditureAuthorizationModel,
        "expenditures",
    ),
    "procurement": (
        "award_procurement",
        "economy.procurement.authorize",
        "authorize_procurement",
        ProcurementModel,
        "procurements",
    ),
    "grant": (
        "authorize_transfer",
        "economy.grant.authorize",
        "authorize_transfer",
        EconomicTransferModel,
        "transfers",
    ),
    "subsidy": (
        "authorize_transfer",
        "economy.subsidy.authorize",
        "authorize_transfer",
        EconomicTransferModel,
        "transfers",
    ),
}
OPERATIONS = ("economy.program.create", *(case[1] for case in CASES.values()))


def _compensation_required() -> type[Exception]:
    """`core/` يُستورَدُ بعدَ أن يضعَ الجسرُ جذرَ المستودعِ على المسار (نمط E1)."""
    from core.sovereignty.compensation import CompensationRequired

    return CompensationRequired


class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجّلُ كلَّ نتيجةٍ محروسة — للقياسِ لا للقرار (نمط W-818)."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []
        self.calls: list[dict[str, Any]] = []

    def guard_declared(self, action: str, target: str, **kwargs: Any) -> Any:
        self.calls.append({"action": action, "target": target, **kwargs})
        guarded = super().guard_declared(action, target, **kwargs)
        self.results.append(guarded)
        return guarded


class Factory:
    """مَنفذُ الحقن: يُسجِّلُ الفاعلَ المطلوبَ من الجدول، ويُجبِرُ غيرَه إن طُلِب (نمط W-755)."""

    def __init__(self, tmp_path: Any, force_actor: str | None = None) -> None:
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
                idempotency_ledger_path=self.tmp_path / f"Q99-{effective}-IDEM.json",
            )
        return self.by_actor[effective]

    @property
    def calls(self) -> list[dict[str, Any]]:
        return [c for a in self.by_actor.values() for c in a.calls]

    @property
    def results(self) -> list[Any]:
        return [r for a in self.by_actor.values() for r in a.results]


def _count(model: Any) -> int:
    session = _session()
    try:
        return session.query(model).count()
    finally:
        session.close()


@pytest.fixture
def world(registry, national, federation, economy, treasury, crown) -> dict[str, Any]:  # noqa: F811
    """عالمٌ حقيقيٌّ بالأسطحِ العلنيّة: ولاية · سلسلةُ سلطة · خزانةٌ مموَّلة · برنامج · هويّات."""
    _federal, (state, _other) = _federal_and_states(federation, crown)
    chain = _authority_chain(
        registry,
        national,
        federation,
        crown,
        crown,
        government_code=state["code"],
        scope="INSTITUTION",
        operations=OPERATIONS,
        max_amount="100000.0000",
    )
    money = _treasury_chain(treasury, crown, chain.institution["code"], chain.official["id"])
    program = _program(economy, crown, chain, "INSTITUTION")
    return {
        "crown": crown,
        "chain": chain,
        "money": money,
        "program": program,
        "beneficiary": national.create_identity(
            context=crown, identity_type="PERSON", label="مستفيدٌ حقيقيّ"
        ),
        "supplier": national.create_identity(
            context=crown, identity_type="ORGANIZATION", label="مورِّدٌ مسجَّل"
        ),
    }


def _call(ne: NationalEconomy, case: str, w: dict[str, Any]) -> dict[str, Any]:
    """نداءُ السطحِ بالمثبِّتِ نفسِه — العمليّةُ من الحالةِ لا من تخمين."""
    ctx = w["crown"]
    institution = w["chain"].institution["code"]
    if case == "expenditure":
        return ne.authorize_expenditure(
            ctx,
            program_code=w["program"]["code"],
            allocation_id=w["money"]["allocation"]["id"],
            institution_code=institution,
            scope_level="INSTITUTION",
            amount=Decimal("1500.5000"),
            purpose="تشغيلُ برنامج",
        )
    if case == "procurement":
        return ne.authorize_procurement(
            ctx,
            title="توريدُ معدّات",
            program_code=w["program"]["code"],
            institution_code=institution,
            scope_level="INSTITUTION",
            supplier_identity_id=w["supplier"]["id"],
            estimated_amount=Decimal("4000.0000"),
            specification="مواصفةٌ مكتوبة",
        )
    return ne.authorize_transfer(
        ctx,
        transfer_kind=case.upper(),
        program_code=w["program"]["code"],
        beneficiary_identity_id=w["beneficiary"]["id"],
        allocation_id=w["money"]["allocation"]["id"],
        institution_code=institution,
        scope_level="INSTITUTION",
        amount=Decimal("750.2500"),
        purpose="تحويلٌ مُجاز",
    )


# ── الصنفُ 0 · المفردات ──────────────────────────────────────────────────────


@pytest.mark.parametrize("case", sorted(CASES))
def test_q99_0_vocabulary_lexicon_and_delegation_name_the_treasury(case: str) -> None:
    from core.constitutional_engine import rules

    verb, operation, entrypoint, _model, _collection = CASES[case]
    assert verb in rules.TREASURY_ACTIONS
    assert rules._exclusive_owner(verb).name == "TREASURY"
    assert rules.MONEY_OPERATION_LEXICON[operation] == verb
    matches = [
        d for d in MONEY_DELEGATIONS if (d.operation, d.entrypoint) == (operation, entrypoint)
    ]
    assert len(matches) == 1, f"لا تفويضَ واحدًا لـ{operation} · {entrypoint}"
    assert matches[0].constitutional_action == verb
    assert matches[0].actor.upper() == "TREASURY"


# ── الصنفُ 1 · الرفضُ قبلَ الكتابة ───────────────────────────────────────────


@pytest.mark.parametrize("actor", ("EXECUTIVE", "JUDICIAL"))
@pytest.mark.parametrize("case", sorted(CASES))
def test_q99_1_non_treasury_actor_is_denied_before_any_write(
    case: str, actor: str, world: dict[str, Any], tmp_path: Any
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    verb, _operation, _entrypoint, model, _collection = CASES[case]
    rows = _count(model)
    decisions = _count(EconomicDecisionModel)
    factory = Factory(tmp_path, force_actor=actor)
    denied = NationalEconomy(money_authorizer_factory=factory)

    with pytest.raises(SovereigntyViolation) as excinfo:
        _call(denied, case, world)

    message = str(excinfo.value)
    assert verb in message
    assert "R-003-1" in message
    assert factory.requested == ["TREASURY"], "الفاعلُ المطلوبُ من الجدولِ ليس الخزانة"
    assert _count(model) == rows, "الرفضُ كتبَ صفًّا"
    assert _count(EconomicDecisionModel) == decisions, "الرفضُ كتبَ قرارًا"


# ── الصنفُ 2 · النجاحُ بالدليل ────────────────────────────────────────────────


@pytest.mark.parametrize("case", sorted(CASES))
def test_q99_2_treasury_crosses_once_with_literal_core_evidence(
    case: str, world: dict[str, Any], tmp_path: Any
) -> None:
    verb, operation, _entrypoint, model, collection = CASES[case]
    factory = Factory(tmp_path)
    ne = NationalEconomy(money_authorizer_factory=factory)
    rows = _count(model)
    decisions = _count(EconomicDecisionModel)

    result = _call(ne, case, world)

    assert factory.requested == ["TREASURY"]
    assert len(factory.results) == 1, "نقطةُ عبورٍ واحدةٌ للسطح"
    call = factory.calls[0]
    assert call["action"] == verb
    effects = call["declared_effects"]
    assert len(effects) == 1
    assert effects[0].resource == call["target"]
    assert call["target"].startswith("economy/")
    assert call["target"].split("/")[2] == collection
    assert call["target"].endswith("/" + result["reference"])
    evidence = factory.results[0].evidence.as_dict()
    assert evidence["action"] == verb
    assert evidence["decision"] == "ALLOW"
    assert evidence["ledger_entry_hash"], "لا قيدَ في سجلِّ النواة"
    assert result["status"] == "authorized"
    assert result["decision"]["operation"] == operation
    assert result["decision_id"] == result["decision"]["id"]
    assert _count(model) == rows + 1
    assert _count(EconomicDecisionModel) == decisions + 1


# ── الصنفُ 3 · لا إعادةَ مدّعاة ───────────────────────────────────────────────


@pytest.mark.parametrize("case", ("expenditure", "grant"))
def test_q99_3_two_calls_are_two_crossings_not_a_false_replay(
    case: str, world: dict[str, Any], tmp_path: Any
) -> None:
    """الإجازاتُ تتكرّرُ مقصودة: المفتاحُ معرّفُ الصفِّ المولَّد ⇒ لا «إعادة» لم تكن."""
    _verb, _operation, _entrypoint, model, _collection = CASES[case]
    factory = Factory(tmp_path)
    ne = NationalEconomy(money_authorizer_factory=factory)
    rows = _count(model)

    first = _call(ne, case, world)
    second = _call(ne, case, world)

    assert first["id"] != second["id"]
    assert "replayed" not in first and "replayed" not in second
    keys = {c["operation_key"] for c in factory.calls}
    assert len(keys) == 2, "مفتاحُ الذرّيّةِ تكرَّرَ لإجازتَين"
    assert _count(model) == rows + 2


# ── الصنفُ 4 · التعويض ───────────────────────────────────────────────────────


def _boom(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError("فشلٌ مُصطنَعٌ بعدَ التثبيت")


@pytest.mark.parametrize("case", sorted(CASES))
def test_q99_4_maybe_applied_is_compensated_row_then_decision(
    case: str, world: dict[str, Any], tmp_path: Any, monkeypatch: pytest.MonkeyPatch
) -> None:
    """`_announce` يفشلُ بعدَ التثبيت ⇒ يُحذَفُ الصفُّ ثمّ قرارُه، ويُرفَعُ السببُ بملاحظةِ Q-88."""
    _verb, _operation, _entrypoint, model, _collection = CASES[case]
    ne = NationalEconomy(money_authorizer_factory=Factory(tmp_path))
    rows = _count(model)
    decisions = _count(EconomicDecisionModel)
    monkeypatch.setattr(NationalEconomy, "_announce", _boom)

    with pytest.raises(RuntimeError, match="فشلٌ مُصطنَع") as excinfo:
        _call(ne, case, world)

    assert any("[Q-88]" in note for note in getattr(excinfo.value, "__notes__", ()))
    assert _count(model) == rows, "الصفُّ بقيَ بعدَ التعويض"
    assert _count(EconomicDecisionModel) == decisions, "القرارُ بقيَ بعدَ التعويض"


def test_q99_4b_failed_compensation_is_failed_final_not_silent(
    world: dict[str, Any], tmp_path: Any, monkeypatch: pytest.MonkeyPatch
) -> None:
    """المطبِّقُ والمعوِّضُ يفشلان ⇒ `CompensationRequired` غيرُ نظيفٍ يُرفَع — لا نجاحَ ولا صمت."""
    ne = NationalEconomy(money_authorizer_factory=Factory(tmp_path))
    monkeypatch.setattr(NationalEconomy, "_announce", _boom)
    monkeypatch.setattr(NationalEconomy, "_delete_rows", _boom)

    with pytest.raises(_compensation_required()) as excinfo:
        _call(ne, "procurement", world)

    assert not excinfo.value.state_is_clean


# ── الصنفُ 6 · المسارُ كاملًا بتوصيلِ الإنتاج: إعلانٌ ⇒ جسرٌ ⇒ نواة ───────────


@pytest.mark.parametrize("case", sorted(CASES))
def test_q99_6_full_path_default_wiring_reaches_the_kernel_ledger(
    case: str, world: dict[str, Any]
) -> None:
    verb, _operation, _entrypoint, model, _collection = CASES[case]
    ne = NationalEconomy()  # لا مَنفذَ حقن: مُصرِّحُ الخزانةِ من نقطةِ الفرضِ كما في الإنتاج
    before = money_authority._CROSSING_GATEWAY
    seen = len(before.records) if before is not None else 0
    rows = _count(model)

    result = _call(ne, case, world)

    gateway = money_authority._CROSSING_GATEWAY
    assert gateway is not None, "العبورُ لم يبنِ بوّابةَ الخزانة"
    records = [r for r in gateway.records[seen:] if r.action == verb]
    # البوّابةُ تُسجِّلُ مرحلتَين للتنفيذِ الواحد: AUTHORIZED ثمّ COMPLETED، ببصمةٍ وقيدٍ واحدَين.
    assert [str(r.completion.value) for r in records] == ["AUTHORIZED", "COMPLETED"]
    assert len({r.fingerprint for r in records}) == 1
    assert len({r.ledger_entry_hash for r in records}) == 1
    record = records[-1]
    assert str(record.actor).upper() == "TREASURY"
    assert str(record.decision).upper() == "ALLOW"
    assert record.ledger_entry_hash
    ledger = gateway.engine.ledger
    entries = [e for e in ledger.entries() if e.entry_hash == record.ledger_entry_hash]
    assert len(entries) == 1, "قيدُ النواةِ غائبٌ عن السجلِّ على القرص"
    body = entries[0].body
    assert body["type"] == "CONSTITUTIONAL_VERDICT"
    assert body["action"] == verb
    assert str(body["actor"]).upper() == "TREASURY"
    assert str(body["decision"]).upper() == "ALLOW"
    assert ledger.verify_chain() == [], "سلسلةُ سجلِّ النواةِ مكسورة"
    assert result["status"] == "authorized"
    assert _count(model) == rows + 1
