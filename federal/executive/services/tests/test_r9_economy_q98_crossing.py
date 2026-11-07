"""الهدف: عبورُ أسطحِ `national_economy` التسعةِ الحدَّ السياديَّ بأفعالِها (Q-98 · W-820).

التعريف: قرارُ المالكِ Q-98 (التوجيه 43 § 1) أقرَّ تسعةَ أفعالٍ تنفيذيّةٍ جديدةٍ باسمِ أسطحِها
في `EXECUTIVE_ACTIONS` بنهجِ Q-97، وتصميمُ العبورِ في
`docs/audit/Q83C_LEXICON_TABLE_DESIGN.md` § 7. يقيسُ هذا الملفُّ على قاعدةٍ حقيقيّةٍ ومحرّكٍ
حقيقيٍّ بلا محاكاةٍ للنواة:

  الصنفُ 1 · الرفضُ قبلَ الكتابة: JUDICIAL ⇒ `SovereigntyViolation` بـR-003-1 ولا صفَّ
            ولا قرارَ يُكتَب — لكلِّ سطحٍ من التسعة.
  الصنفُ 2 · النجاحُ بالدليل: التنفيذيُّ ⇒ ALLOW بفعلِ السطحِ حرفيًّا وأثرٍ معلَنٍ واحد.
  الصنفُ 3 · الإعادةُ لا تُكرِّرُ الأثر: مفتاحُ الذرّيّةِ نفسُه ⇒ `replayed: True` بلا صفٍّ ثانٍ.
  الصنفُ 4 · التعويضُ الحقيقيّ: فشلٌ بعدَ التثبيتِ داخلَ المُطبِّق ⇒ الصفُّ وقرارُه يُحذَفان
            (والسياسةُ قبلَ قرارِها لأنّ `decision_id` مفتاحٌ أجنبيّ).
  الصنفُ 6 · المسارُ كاملًا بتوصيلِ الإنتاج: `NationalEconomy()` بلا مُصرِّحٍ محقون ⇒
            `get_authorizer()` ⇒ البوّابة ⇒ قيدُ `CONSTITUTIONAL_VERDICT` في سجلِّ النواةِ نفسِه
            يُقرأُ من القرص بفعلِ السطحِ والفاعلِ EXECUTIVE وALLOW، وتُطابِقُ بصمتُه سجلَّ
            البوّابة، و`verify_chain()` فارغ (التوجيه 43 § 2 — لم يُقَس صراحةً في الدفعة 1).

اسمُ الملفِّ `test_r9_economy_…` ليُجمَعَ **قبلَ** `test_r9_national_economic_state` فيُنظِّفَ مثبِّتُها
`_fresh_state` صفوفَه (درسُ W-818، وقيسَ هنا: الاسمُ الأوّلُ `test_r9_q98_…` جُمِعَ بعدَها فبقيَت
صفوفُه وأسقطَت تنظيفَ `test_w755` بقيدٍ مرجعيٍّ على `state_officials` — 59 خطأَ إعدادٍ في الحزمةِ الكاملة).
[تحديثٌ مؤرَّخٌ (2026-11-07 · W-826 · DISC-161):] عُولِجَ الجذرُ — مثبِّتُ R9 صارَ ينظِّفُ
بعدَ الاختبارِ أيضًا (`yield`) فلم يعدْ نجاحُ الحزمةِ يعتمدُ على هذا الترتيبِ؛ يُقاسُ
بالزوجِ المعكوسِ في `docs/audit/evidence/W-826/disc161_repro_after.txt`.
النطاق: `national_economy/service.py` وحدَه؛ والطفراتُ في
`docs/audit/evidence/W-819/q98_mutation_probe.py`.
المالك: Perplexity Computer (WI-127 · قيدُ W-820).
"""

from __future__ import annotations

from decimal import Decimal
from typing import Any

import pytest

from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from amos_federation.services.national_economy import service as ne_service
from amos_federation.services.national_economy.models import (
    EconomicCategoryModel,
    EconomicDecisionModel,
    EconomicIndicatorDefinitionModel,
    EconomicPolicyModel,
    EconomicProgramModel,
    EconomicSectorModel,
    PublicAssetModel,
    PublicEconomicEntityModel,
    PublicLiabilityModel,
    RevenueSourceModel,
)
from amos_federation.services.national_economy.service import (
    Q98_NATIONAL_ECONOMY_ACTIONS,
    NationalEconomy,
)
from tests.test_r9_national_economic_state import (  # noqa: F401 — مثبِّتاتُ R9 نفسُها
    _authority_chain,
    _code,
    _federal_and_states,
    _fresh_state,
    _session,
    crown,
    economy,
    federation,
    national,
    registry,
    treasury,
)

OPERATIONS = (
    "economy.entity.register",
    "economy.program.create",
    "economy.policy.issue",
    "economy.revenue.register",
    "economy.asset.register",
    "economy.liability.register",
)

MODEL_OF = {
    "register_sector": EconomicSectorModel,
    "register_category": EconomicCategoryModel,
    "define_indicator": EconomicIndicatorDefinitionModel,
    "register_public_entity": PublicEconomicEntityModel,
    "create_program": EconomicProgramModel,
    "issue_policy": EconomicPolicyModel,
    "register_revenue_source": RevenueSourceModel,
    "register_public_asset": PublicAssetModel,
    "register_public_liability": PublicLiabilityModel,
}
WITH_DECISION = {
    "register_public_entity",
    "create_program",
    "issue_policy",
    "register_revenue_source",
    "register_public_asset",
    "register_public_liability",
}


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


def _count(model: Any) -> int:
    session = _session()
    try:
        return session.query(model).count()
    finally:
        session.close()


@pytest.fixture
def world(registry, national, federation, economy, crown) -> dict[str, Any]:  # noqa: F811
    """عالمٌ حقيقيٌّ بالأسطحِ العلنيّة: ولايةٌ · سلسلةُ سلطةٍ بالمِنحِ الستّ · قطاع · هويّات."""
    _federal, (state, _other) = _federal_and_states(federation, crown)
    chain = _authority_chain(
        registry,
        national,
        federation,
        crown,
        crown,
        government_code=state["code"],
        scope="STATE",
        operations=OPERATIONS,
        max_amount="1000000.0000",
    )
    sector = economy.register_sector(
        crown, code=_code("SEC"), name="قطاعٌ", government_code=state["code"], scope_level="STATE"
    )
    return {
        "state": state,
        "chain": chain,
        "sector": sector,
        "crown": crown,
        "entity_identity": national.create_identity(
            context=crown, identity_type="ORGANIZATION", label="صندوقٌ عامّ"
        ),
        "custodian": national.create_identity(
            context=crown, identity_type="PERSON", label="أمينُ أصل"
        ),
        "creditor": national.create_identity(
            context=crown, identity_type="ORGANIZATION", label="دائن"
        ),
    }


def _call(
    ne: NationalEconomy, verb: str, w: dict[str, Any], code: str | None = None
) -> dict[str, Any]:
    """نداءُ السطحِ الواحدِ بالمثبِّتِ نفسِه — والفعلُ اسمُ السطحِ حرفيًّا (Q-98)."""
    ctx = w["crown"]
    institution = w["chain"].institution["code"]
    state = w["state"]["code"]
    sector = w["sector"]["code"]
    if verb == "register_sector":
        return ne.register_sector(
            ctx,
            code=code or _code("SEC"),
            name="قطاع",
            government_code=state,
            scope_level="STATE",
        )
    if verb == "register_category":
        return ne.register_category(ctx, sector_code=sector, code=code or _code("CAT"), name="فئة")
    if verb == "define_indicator":
        return ne.define_indicator(
            ctx,
            code=code or _code("IND"),
            name="مؤشّر",
            unit="ريال",
            method="طريقةٌ معلَنة",
            government_code=state,
            scope_level="STATE",
        )
    if verb == "register_public_entity":
        return ne.register_public_entity(
            ctx,
            code=code or _code("PUB"),
            name="صندوقٌ عامّ",
            entity_kind="PUBLIC_FUND",
            institution_code=institution,
            scope_level="STATE",
            identity_id=w["entity_identity"]["id"],
            sector_code=sector,
        )
    if verb == "create_program":
        return ne.create_program(
            ctx,
            code=code or _code("PRG"),
            name="برنامج",
            institution_code=institution,
            scope_level="STATE",
            sector_code=sector,
        )
    if verb == "issue_policy":
        return ne.issue_policy(
            ctx,
            code=code or _code("POL"),
            title="سياسة",
            policy_type="FISCAL",
            institution_code=institution,
            scope_level="STATE",
        )
    if verb == "register_revenue_source":
        return ne.register_revenue_source(
            ctx,
            code=code or _code("REV"),
            name="رسم",
            revenue_kind="TAX",
            basis="نسبة",
            institution_code=institution,
            scope_level="STATE",
        )
    if verb == "register_public_asset":
        return ne.register_public_asset(
            ctx,
            code=code or _code("AST"),
            name="أرض",
            asset_class="LAND",
            institution_code=institution,
            scope_level="STATE",
            custodian_identity_id=w["custodian"]["id"],
            book_value=Decimal("100.0000"),
            currency="SAR",
        )
    if verb == "register_public_liability":
        return ne.register_public_liability(
            ctx,
            code=code or _code("LIA"),
            name="سند",
            liability_class="BOND",
            institution_code=institution,
            scope_level="STATE",
            creditor_identity_id=w["creditor"]["id"],
            principal_amount=Decimal("50.0000"),
        )
    raise AssertionError(verb)


def test_q98_0_nine_verbs_are_executive_exclusive() -> None:
    """الأفعالُ التسعةُ في الحصرِ التنفيذيِّ حرفيًّا — حذفُ واحدٍ من rules.py يُسقِطُ هذا."""
    from core.constitutional_engine import rules

    assert len(Q98_NATIONAL_ECONOMY_ACTIONS) == 9
    assert set(Q98_NATIONAL_ECONOMY_ACTIONS) == set(MODEL_OF)
    for verb in Q98_NATIONAL_ECONOMY_ACTIONS:
        assert verb in rules.EXECUTIVE_ACTIONS, verb
        assert rules._exclusive_owner(verb).name == "EXECUTIVE", verb


# ── الصنفُ 1 · الرفضُ قبلَ الكتابة ───────────────────────────────────────────


@pytest.mark.parametrize("verb", Q98_NATIONAL_ECONOMY_ACTIONS)
def test_q98_1_non_executive_actor_is_denied_before_any_write(
    verb: str, world: dict[str, Any]
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    model = MODEL_OF[verb]
    before = _count(model)
    decisions = _count(EconomicDecisionModel)
    denied = NationalEconomy(authorizer=ConstitutionalAuthorizer(actor="JUDICIAL"))

    with pytest.raises(SovereigntyViolation) as excinfo:
        _call(denied, verb, world)

    message = str(excinfo.value)
    assert verb in message
    assert "R-003-1" in message
    assert _count(model) == before, "الرفضُ كتبَ صفًّا"
    assert _count(EconomicDecisionModel) == decisions, "الرفضُ كتبَ قرارًا"


# ── الصنفُ 2 · النجاحُ بالدليل ────────────────────────────────────────────────


@pytest.mark.parametrize("verb", Q98_NATIONAL_ECONOMY_ACTIONS)
def test_q98_2_executive_crosses_with_literal_core_evidence(
    verb: str, world: dict[str, Any]
) -> None:
    recorder = RecordingAuthorizer()
    ne = NationalEconomy(authorizer=recorder)
    before = _count(MODEL_OF[verb])

    result = _call(ne, verb, world)

    assert len(recorder.results) == 1, "نقطةُ عبورٍ واحدةٌ للسطح"
    call = recorder.calls[0]
    effects = call["declared_effects"]
    assert len(effects) == 1
    assert effects[0].resource == call["target"]
    assert call["target"].startswith("economy/")
    evidence = recorder.results[0].evidence.as_dict()
    assert evidence["action"] == verb
    assert evidence["decision"] == "ALLOW"
    assert evidence["ledger_entry_hash"], "لا قيدَ في سجلِّ النواة"
    assert result["replayed"] is False
    assert _count(MODEL_OF[verb]) == before + 1
    if verb in WITH_DECISION:
        assert result["decision"]["reference"].startswith("ECD-")


# ── الصنفُ 3 · الإعادةُ لا تُكرِّرُ الأثر ────────────────────────────────────


def _purge(model: Any, row_id: str, decision_id: str | None = None) -> None:
    session = _session()
    try:
        session.query(model).filter(model.id == row_id).delete()
        if decision_id:
            session.query(EconomicDecisionModel).filter(
                EconomicDecisionModel.id == decision_id
            ).delete()
        session.commit()
    finally:
        session.close()


def test_q98_3_sector_replay_by_key_writes_no_second_row(world: dict[str, Any]) -> None:
    """منادٍ ثانٍ اجتازَ الفحصَ المسبقَ (يُحاكى بحذفِ الصفِّ يدويًّا) ⇒ إعادةٌ لا صفٌّ ثانٍ."""
    ne = NationalEconomy(authorizer=RecordingAuthorizer())
    code = _code("SEC")
    first = _call(ne, "register_sector", world, code=code)
    _purge(EconomicSectorModel, first["id"])
    before = _count(EconomicSectorModel)

    again = _call(ne, "register_sector", world, code=code)

    assert again["replayed"] is True
    assert again["operation_key"]
    assert _count(EconomicSectorModel) == before, "الإعادةُ كتبَت صفًّا ثانيًا"


def test_q98_3b_program_replay_writes_no_row_and_no_decision(world: dict[str, Any]) -> None:
    ne = NationalEconomy(authorizer=RecordingAuthorizer())
    code = _code("PRG")
    first = _call(ne, "create_program", world, code=code)
    _purge(EconomicProgramModel, first["id"], first["decision"]["id"])
    programs = _count(EconomicProgramModel)
    decisions = _count(EconomicDecisionModel)

    again = _call(ne, "create_program", world, code=code)

    assert again["replayed"] is True
    assert _count(EconomicProgramModel) == programs
    assert _count(EconomicDecisionModel) == decisions, "الإعادةُ أصدرَت قرارًا ثانيًا"


# ── الصنفُ 4 · التعويضُ الحقيقيّ ──────────────────────────────────────────────


def _boom(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError("فشلٌ مُصطنَعٌ بعدَ التثبيت")


def test_q98_4_sector_create_is_compensated_by_delete(
    world: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    ne = NationalEconomy(authorizer=RecordingAuthorizer())
    before = _count(EconomicSectorModel)
    monkeypatch.setattr(ne_service, "_iso", _boom)

    with pytest.raises(_compensation_required()):
        _call(ne, "register_sector", world)

    assert _count(EconomicSectorModel) == before, "صفُّ CREATE بقيَ بعدَ التعويض"


@pytest.mark.parametrize("verb", ("create_program", "issue_policy", "register_public_liability"))
def test_q98_4b_row_and_decision_are_both_compensated(
    verb: str, world: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    """`_announce` بعدَ التثبيتِ يفشل ⇒ يُحذَفُ الصفُّ وقرارُه معًا (والسياسةُ قبلَ قرارِها)."""
    ne = NationalEconomy(authorizer=RecordingAuthorizer())
    rows = _count(MODEL_OF[verb])
    decisions = _count(EconomicDecisionModel)
    monkeypatch.setattr(NationalEconomy, "_announce", _boom)

    with pytest.raises(_compensation_required()):
        _call(ne, verb, world)

    assert _count(MODEL_OF[verb]) == rows, "الصفُّ بقيَ بعدَ التعويض"
    assert _count(EconomicDecisionModel) == decisions, "القرارُ بقيَ بعدَ التعويض"


# ── الصنفُ 6 · المسارُ كاملًا بتوصيلِ الإنتاج: إعلانٌ ⇒ جسرٌ ⇒ نواة ───────────


@pytest.mark.parametrize("verb", Q98_NATIONAL_ECONOMY_ACTIONS)
def test_q98_6_full_path_default_wiring_reaches_the_kernel_ledger(
    verb: str, world: dict[str, Any]
) -> None:
    ne = NationalEconomy()  # لا مُصرِّحَ محقونًا: get_authorizer() كما في الإنتاج
    gateway = ne.authorizer.gateway  # المفردُ المشترك: نعدُّ ما يُضافُ بهذا النداءِ وحدَه
    seen = len(gateway.records)

    result = _call(ne, verb, world)

    records = [r for r in gateway.records[seen:] if r.action == verb]
    # البوّابةُ تُسجِّلُ مرحلتَين للتنفيذِ الواحد: AUTHORIZED ثمّ COMPLETED، ببصمةٍ وقيدٍ واحدَين.
    assert [str(r.completion.value) for r in records] == ["AUTHORIZED", "COMPLETED"]
    assert len({r.fingerprint for r in records}) == 1
    assert len({r.ledger_entry_hash for r in records}) == 1
    record = records[-1]
    assert str(record.actor).upper() == "EXECUTIVE"
    assert str(record.decision).upper() == "ALLOW"
    assert record.ledger_entry_hash
    ledger = gateway.engine.ledger
    entries = [e for e in ledger.entries() if e.entry_hash == record.ledger_entry_hash]
    assert len(entries) == 1, "قيدُ النواةِ غائبٌ عن السجلِّ على القرص"
    body = entries[0].body
    assert body["type"] == "CONSTITUTIONAL_VERDICT"
    assert body["action"] == verb
    assert str(body["actor"]).upper() == "EXECUTIVE"
    assert str(body["decision"]).upper() == "ALLOW"
    assert ledger.verify_chain() == [], "سلسلةُ سجلِّ النواةِ مكسورة"
    assert result["replayed"] is False
