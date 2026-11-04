"""الهدف: عبورُ أسطحِ `federal_state` الثمانيةِ الحدَّ السياديَّ بأفعالِها (Q-97 · W-818).

التعريف: قرارُ المالكِ Q-97 (التوجيه 42 § 1 السؤالانِ 1 و2) أقرَّ ثمانيةَ أفعالٍ تنفيذيّةٍ
جديدةٍ باسمِ أسطحِها في `EXECUTIVE_ACTIONS`، وتصميمُ العبورِ في
`docs/audit/Q83C_LEXICON_TABLE_DESIGN.md` § 6. وهذا الملفُّ يقيسُ المسارَ الكاملَ
«إعلانٌ ⇒ جسرٌ ⇒ نواة» على قاعدةٍ حقيقيّةٍ ومحرّكٍ حقيقيّ — لا محاكاةَ للنواة:

  الصنفُ 1 · الرفضُ قبلَ الكتابة: فاعلٌ غيرُ تنفيذيٍّ (JUDICIAL) ⇒ `SovereigntyViolation`
            بـR-003-1 ولا صفَّ يُكتَب — لكلِّ سطحٍ من الثمانية.
  الصنفُ 2 · النجاحُ بالدليل: التنفيذيُّ ⇒ ALLOW بفعلِ السطحِ حرفيًّا وبصمةِ الطلبِ وتجزئةِ
            قيدِ السجلّ وأثرٍ معلَنٍ واحدٍ تحتَ الهدف — لكلِّ سطح.
  الصنفُ 3 · الإعادةُ لا تُكرِّرُ الأثر: مفتاحُ الذرّيّةِ نفسُه ⇒ `replayed: True` بلا صفٍّ ثانٍ.
  الصنفُ 4 · التعويضُ الحقيقيّ: فشلٌ بعدَ الكتابةِ داخلَ المُطبِّق ⇒ CREATE يُحذَف · WRITE يُعاد.
  الصنفُ 5 · العمليّةُ المشروعةُ اللاحقةُ ليست إعادة (مفتاحٌ بالنسخةِ لا بالمحتوى).

اسمُ الملفِّ `test_r8_q97_…` لا `test_q97_…` عمدًا: يُجمَعُ بعدَ `test_r8_federal_state_integration`
وقبلَ `test_r9_…` فتُنظِّفُ مثبِّتاتُ R9 صفوفَه كما تُنظِّفُ صفوفَ R8 — وبالاسمِ الأوّلِ سبقَ
`test_r1`…`test_r7d` في التشغيلِ الكاملِ فكسرَ تنظيفَها (201 خطأَ إعدادٍ مقيسًا · FOREIGN KEY).
النطاق: `federal_state/service.py` وحدَه؛ والطفراتُ في
`docs/audit/evidence/W-817/q97_mutation_probe.py`.
المالك: Perplexity Computer (WI-127 · قيدُ W-818).
"""

from __future__ import annotations

from typing import Any

import pytest

from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from amos_federation.services.federal_state import service as fs_service
from amos_federation.services.federal_state.models import (
    CaseScopeModel,
    GovernmentDelegationModel,
    GovernmentModel,
    GovernmentRelationModel,
    InstitutionGovernmentModel,
    ServiceScopeModel,
)
from amos_federation.services.federal_state.service import (
    Q97_FEDERAL_STATE_ACTIONS,
    FederalStateGovernment,
)
from tests.test_r8_federal_state_integration import (  # noqa: F401 — مثبِّتاتُ R8 نفسُها
    _authority_chain,
    _code,
    _context,
    _federal_and_states,
    _fresh_state,
    _open_case,
    _session,
    crown,
    federation,
    national,
    registry,
    services,
)


def _compensation_required() -> type[Exception]:
    """`core/` يُستورَدُ بعدَ أن يضعَ الجسرُ جذرَ المستودعِ على المسار (نمط E1)."""
    from core.sovereignty.compensation import CompensationRequired

    return CompensationRequired


class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجّلُ كلَّ نتيجةٍ محروسة — للقياسِ لا للقرار (نمط WI-082 · E1)."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []
        self.calls: list[dict[str, Any]] = []

    def guard_declared(self, action: str, target: str, **kwargs: Any) -> Any:
        self.calls.append({"action": action, "target": target, **kwargs})
        guarded = super().guard_declared(action, target, **kwargs)
        self.results.append(guarded)
        return guarded


MODEL_OF = {
    "register_government": GovernmentModel,
    "set_government_status": GovernmentModel,
    "bind_institution": InstitutionGovernmentModel,
    "record_relation": GovernmentRelationModel,
    "grant_delegation": GovernmentDelegationModel,
    "revoke_delegation": GovernmentDelegationModel,
    "scope_service": ServiceScopeModel,
    "scope_case": CaseScopeModel,
}


def _count(model: Any) -> int:
    session = _session()
    try:
        return session.query(model).count()
    finally:
        session.close()


def _row(model: Any, row_id: str) -> Any:
    session = _session()
    try:
        row = session.get(model, row_id)
        if row is not None:
            session.expunge(row)
        return row
    finally:
        session.close()


@pytest.fixture
def world(registry, national, federation, services, crown) -> dict[str, Any]:  # noqa: F811
    """عالمٌ حقيقيٌّ يُبنى بالأسطحِ العلنيّةِ نفسِها (فدراليةٌ · ولاية · سلسلةُ سلطة · قضيّة · تفويض)."""
    federal, (state, _other) = _federal_and_states(federation, crown)
    officer = _context("official", username="q97")
    chain = _authority_chain(
        registry,
        national,
        federation,
        crown,
        officer,
        government_code=state["code"],
        scope="STATE",
    )
    bundle = _open_case(services, registry, crown, chain)
    delegation = federation.grant_delegation(
        crown,
        from_government_code=federal["code"],
        to_government_code=state["code"],
        operation="gov.case.decide",
        scope="FEDERAL",
        reason="تفويضٌ للنقض",
    )
    spare = registry.register_institution(
        context=crown,
        code=_code("INS"),
        name="مؤسسةٌ غيرُ مربوطة",
        kind="ministry",
        branch="executive",
    )
    return {
        "federal": federal,
        "state": state,
        "officer": officer,
        "chain": chain,
        "bundle": bundle,
        "delegation": delegation,
        "spare": spare,
        "crown": crown,
    }


def _call(fs: FederalStateGovernment, verb: str, w: dict[str, Any]) -> dict[str, Any]:
    """نداءُ السطحِ الواحدِ بالمثبِّتِ نفسِه — والفعلُ اسمُ السطحِ حرفيًّا (Q-97 السؤال 1)."""
    crown_ctx = w["crown"]
    if verb == "register_government":
        return fs.register_government(
            crown_ctx,
            code=_code("ST"),
            name="ولايةٌ جديدة",
            level="STATE",
            parent_code=w["federal"]["code"],
        )
    if verb == "set_government_status":
        return fs.set_government_status(crown_ctx, w["state"]["code"], "suspended", "تعليقٌ مؤقّت")
    if verb == "bind_institution":
        return fs.bind_institution(
            crown_ctx, institution_code=w["spare"]["code"], government_code=w["state"]["code"]
        )
    if verb == "record_relation":
        return fs.record_relation(
            crown_ctx,
            from_kind="GOVERNMENT",
            from_ref=w["federal"]["id"],
            to_kind="GOVERNMENT",
            to_ref=w["state"]["id"],
            relation="governs",
        )
    if verb == "grant_delegation":
        return fs.grant_delegation(
            crown_ctx,
            from_government_code=w["federal"]["code"],
            to_government_code=w["state"]["code"],
            operation="gov.case.decide",
            scope="FEDERAL",
            reason="تفويضٌ ثانٍ",
        )
    if verb == "revoke_delegation":
        return fs.revoke_delegation(crown_ctx, w["delegation"]["id"], "انتهى الغرض")
    if verb == "scope_service":
        return fs.scope_service(
            crown_ctx,
            institution_code=w["chain"].institution["code"],
            service_code=w["bundle"]["service"]["code"],
            level="STATE",
        )
    if verb == "scope_case":
        return fs.scope_case(
            w["officer"], case_reference=w["bundle"]["case"]["reference"], level="STATE"
        )
    raise AssertionError(verb)


def test_q97_0_eight_verbs_are_executive_exclusive() -> None:
    """الأفعالُ الثمانيةُ في الحصرِ التنفيذيِّ حرفيًّا — حذفُ واحدٍ من rules.py يُسقِطُ هذا."""
    from core.constitutional_engine import rules

    assert len(Q97_FEDERAL_STATE_ACTIONS) == 8
    assert set(Q97_FEDERAL_STATE_ACTIONS) == set(MODEL_OF)
    for verb in Q97_FEDERAL_STATE_ACTIONS:
        assert verb in rules.EXECUTIVE_ACTIONS, verb
        assert rules._exclusive_owner(verb).name == "EXECUTIVE", verb


# ── الصنفُ 1 · الرفضُ قبلَ الكتابة ───────────────────────────────────────────


@pytest.mark.parametrize("verb", Q97_FEDERAL_STATE_ACTIONS)
def test_q97_1_non_executive_actor_is_denied_before_any_write(
    verb: str, world: dict[str, Any]
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    model = MODEL_OF[verb]
    before = _count(model)
    snapshot_state = _row(GovernmentModel, world["state"]["id"]).status
    snapshot_delegation = _row(GovernmentDelegationModel, world["delegation"]["id"]).status
    denied = FederalStateGovernment(authorizer=ConstitutionalAuthorizer(actor="JUDICIAL"))

    with pytest.raises(SovereigntyViolation) as excinfo:
        _call(denied, verb, world)

    message = str(excinfo.value)
    assert verb in message
    assert "R-003-1" in message
    assert _count(model) == before, "الرفضُ كتبَ صفًّا"
    assert _row(GovernmentModel, world["state"]["id"]).status == snapshot_state
    assert _row(GovernmentDelegationModel, world["delegation"]["id"]).status == (
        snapshot_delegation
    )


# ── الصنفُ 2 · النجاحُ بالدليل: إعلانٌ ⇒ جسرٌ ⇒ نواة ───────────────────────────


@pytest.mark.parametrize("verb", Q97_FEDERAL_STATE_ACTIONS)
def test_q97_2_executive_crosses_with_literal_core_evidence(
    verb: str, world: dict[str, Any]
) -> None:
    recorder = RecordingAuthorizer()
    fs = FederalStateGovernment(authorizer=recorder)

    result = _call(fs, verb, world)

    assert len(recorder.results) == 1, "نقطةُ عبورٍ واحدةٌ للسطح"
    call = recorder.calls[0]
    effects = call["declared_effects"]
    assert len(effects) == 1
    assert effects[0].resource == call["target"]
    assert call["target"].startswith("federation/")
    evidence = recorder.results[0].evidence.as_dict()
    assert evidence["action"] == verb
    assert evidence["target"] == call["target"]
    assert evidence["decision"] == "ALLOW"
    assert evidence["request_fingerprint"]
    assert evidence["ledger_entry_hash"], "لا قيدَ في سجلِّ النواة"
    assert recorder.results[0].outcome is not None
    assert recorder.results[0].is_replay is False
    assert result["replayed"] is False


# ── الصنفُ 3 · الإعادةُ لا تُكرِّرُ الأثر ────────────────────────────────────


def test_q97_3_register_replay_by_key_writes_no_second_row(world: dict[str, Any]) -> None:
    """منادٍ ثانٍ اجتازَ الفحصَ المسبقَ (يُحاكى بحذفِ الصفِّ يدويًّا) ⇒ إعادةٌ لا صفٌّ ثانٍ."""
    recorder = RecordingAuthorizer()
    fs = FederalStateGovernment(authorizer=recorder)
    code = _code("ST")
    first = fs.register_government(
        world["crown"], code=code, name="ولاية", level="STATE", parent_code=world["federal"]["code"]
    )
    session = _session()
    try:
        session.query(GovernmentModel).filter(GovernmentModel.id == first["id"]).delete()
        session.commit()
    finally:
        session.close()
    before = _count(GovernmentModel)

    again = fs.register_government(
        world["crown"], code=code, name="ولاية", level="STATE", parent_code=world["federal"]["code"]
    )

    assert again["replayed"] is True
    assert again["operation_key"]
    assert _count(GovernmentModel) == before, "الإعادةُ كتبَت صفًّا ثانيًا"


def test_q97_3b_scope_case_replay_by_key_writes_no_second_row(world: dict[str, Any]) -> None:
    fs = FederalStateGovernment(authorizer=RecordingAuthorizer())
    first = _call(fs, "scope_case", world)
    session = _session()
    try:
        session.query(CaseScopeModel).filter(CaseScopeModel.id == first["id"]).delete()
        session.commit()
    finally:
        session.close()

    again = _call(fs, "scope_case", world)

    assert again["replayed"] is True
    assert _count(CaseScopeModel) == 0


# ── الصنفُ 4 · التعويضُ الحقيقيّ ──────────────────────────────────────────────


def _failing_trace(*_args: Any, **_kwargs: Any) -> Any:
    raise RuntimeError("فشلٌ مُصطنَعٌ بعدَ الكتابة")


def test_q97_4_create_is_compensated_by_delete(
    world: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    fs = FederalStateGovernment(authorizer=RecordingAuthorizer())
    before = _count(GovernmentModel)
    monkeypatch.setattr(fs_service, "record_domain_trace", _failing_trace)

    with pytest.raises(_compensation_required()):
        _call(fs, "register_government", world)

    assert _count(GovernmentModel) == before, "صفُّ CREATE بقيَ بعدَ التعويض"


def test_q97_4b_write_is_compensated_by_restore(
    world: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    fs = FederalStateGovernment(authorizer=RecordingAuthorizer())
    state_id = world["state"]["id"]
    before = _row(GovernmentModel, state_id)
    monkeypatch.setattr(fs_service, "record_domain_trace", _failing_trace)

    with pytest.raises(_compensation_required()):
        _call(fs, "set_government_status", world)

    after = _row(GovernmentModel, state_id)
    assert after.status == before.status == "active"
    assert after.status_reason == before.status_reason


def test_q97_4c_revoke_is_compensated_by_restore(
    world: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    fs = FederalStateGovernment(authorizer=RecordingAuthorizer())
    delegation_id = world["delegation"]["id"]
    monkeypatch.setattr(fs_service, "record_domain_trace", _failing_trace)

    with pytest.raises(_compensation_required()):
        _call(fs, "revoke_delegation", world)

    row = _row(GovernmentDelegationModel, delegation_id)
    assert row.status == "active"
    assert row.revoked_at is None


# ── الصنفُ 5 · المشروعُ اللاحقُ ليس إعادة ────────────────────────────────────


def test_q97_5_later_legitimate_status_changes_are_distinct_operations(
    world: dict[str, Any],
) -> None:
    recorder = RecordingAuthorizer()
    fs = FederalStateGovernment(authorizer=recorder)
    code = world["state"]["code"]

    first = fs.set_government_status(world["crown"], code, "suspended", "تعليق")
    second = fs.set_government_status(world["crown"], code, "active", "استئناف")
    third = fs.set_government_status(world["crown"], code, "suspended", "تعليقٌ ثانٍ")

    assert [r["replayed"] for r in (first, second, third)] == [False, False, False]
    assert len(recorder.results) == 3
    assert _row(GovernmentModel, world["state"]["id"]).status == "suspended"


def test_q97_5b_rebinding_is_a_declared_write_not_a_replay(world: dict[str, Any]) -> None:
    recorder = RecordingAuthorizer()
    fs = FederalStateGovernment(authorizer=recorder)
    institution_code = world["chain"].institution["code"]

    result = fs.bind_institution(
        world["crown"],
        institution_code=institution_code,
        government_code=world["federal"]["code"],
    )

    assert result["replayed"] is False
    assert result["government_id"] == world["federal"]["id"]
    assert recorder.calls[0]["declared_effects"][0].kind.value == "WRITE"
