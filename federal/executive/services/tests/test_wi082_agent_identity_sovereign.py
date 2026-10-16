"""الهدف: إثباتُ هجرةِ `register_identity` إلى حدِّ التنفيذِ السياديّ (WI-082 · Q-15 ①)

النطاق: `executive_core/agent_identity.py::register_identity` — إنشاءُ الهويّةِ
       يُعلَنُ بالفعلِ الدستوريِّ `spawn_agent` فيقفُ عندَ المستوىِ الثالثِ من زرِّ
       الإيقافِ (المادةُ الثامنة). ولا يُهاجَرُ في هذه الدفعةِ `update_identity` ولا
       `set_lifecycle_state` (تسميتُهما للمالكِ · PENDING_OWNER).

المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-16 (WI-082)
تاريخ آخر تعديل: 2026-10-16

الدعاوى المقيسةُ هنا (على سابقةِ 2A/2B لا بمعاييرَ جديدة):

- W-1 الحدُّ: الإنشاءُ يعبرُ الحدَّ فعلًا ومراحلُه الإلزاميّةُ كلُّها مرَّت.
- W-2 الأثرُ: صفٌّ في `agents` تحتَ الهدفِ المُعلَنِ نفسِه، والقيمةُ تُقرأ بعدَه.
- W-3 الإيقافُ: الفعلُ `spawn_agent` يُرفَضُ عندَ المستوى الثالثِ ولا صفَّ يُكتب.
- W-4 التعويضُ: المعوّضُ المربوطُ عكسٌ حقيقيٌّ يحذفُ الصفَّ، والفشلُ يُغلقُ ولا
  يُدَّعى نجاحًا (والتشغيلُ الآليُّ للتعويضِ بعدَ الفشلِ غيرُ مبنيٍّ — مُعلَنٌ في
  `PROJECT_STATE.md` — فلا يُدَّعى هنا).
- W-5 الإعادةُ: مفتاحٌ واحدٌ لا يُنتِجُ أثرًا ثانيًا ولا يَختلِقُ وكيلًا من إعادة.
- W-6 العقدُ: لا كسرَ في توقيعِ النداءِ القائمِ ولا معاملَ تجاوزٍ في الوجهِ الجديد.
"""

from __future__ import annotations

import uuid
from dataclasses import replace
from typing import Any

import pytest

from amos_federation.common.database import AgentModel, get_session_factory, init_db
from amos_federation.services.executive_core import agent_identity as identity_module
from amos_federation.services.executive_core.agent_identity import (
    UnknownAgentIdentityError,
    register_identity,
)
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    GuardedResult,
)


def _row_exists(agent_id: str) -> bool:
    """قياسٌ على الأثرِ في الجدولِ لا على استثناءٍ مرتفع."""
    session = get_session_factory()()
    try:
        return session.query(AgentModel).filter(AgentModel.id == agent_id).first() is not None
    finally:
        session.close()


def _delete_row_directly(agent_id: str) -> None:
    """حذفٌ خارجيٌّ مباشرٌ لمحاكاةِ افتراقِ السجلِّ عن الجدولِ (لا مسارَ إنتاجيًّا)."""
    session = get_session_factory()()
    try:
        row = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        if row is not None:
            session.delete(row)
            session.commit()
    finally:
        session.close()


class RecordingAuthorizer(ConstitutionalAuthorizer):
    """المُصرِّحُ نفسُه يُسجِّلُ حصائلَ الحدِّ ليُقاسَ ما مرَّ فعلًا (سابقةُ 2B).

    لا بدائيّةَ جديدةَ ولا مسارَ ثانيًا: وراثةٌ لا تلمسُ منطقَ التصريح.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.results: list[GuardedResult] = []
        self.calls: list[dict[str, Any]] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> GuardedResult:
        self.calls.append({"action": args[0] if args else None, "kwargs": kwargs})
        result = super().guard_declared(*args, **kwargs)
        self.results.append(result)
        return result


class HaltedAtLevel3Authorizer(ConstitutionalAuthorizer):
    """مُصرِّحٌ يحملُ زرَّ الإيقافِ عندَ المستوى الثالثِ في كلِّ طلبٍ يبنيه.

    `kill_switch_level` حقلُ طلبٍ دستوريّ (المادةُ الثامنة) يُحمَلُ في `ActionRequest`
    نفسِه — والاختبارُ يثبتُ الرفضَ على مسارِ الإنتاجِ الحقيقيِّ (الحرسُ والبوّابةُ
    وقواعدُ المادةِ الثامنة) بلا محاكاةِ حكمٍ.
    """

    def _request(self, action: str, target: str, metadata: dict[str, Any] | None):
        request = super()._request(action, target, metadata)
        return replace(request, kill_switch_level=3)


@pytest.fixture(autouse=True)
def _fresh_db() -> None:
    init_db()


@pytest.fixture
def agent_id() -> str:
    return f"wi082-{uuid.uuid4().hex[:10]}"


def test_register_identity_crosses_boundary_with_mandatory_stages(agent_id: str) -> None:
    """W-1: الإنشاءُ يعبرُ الحدَّ فعلًا ومراحلُه الإلزاميّةُ كلُّها مرَّت."""
    from core.sovereignty.enforcement_boundary import MANDATORY_INTERNAL_STAGES

    authorizer = RecordingAuthorizer()
    identity = register_identity(agent_id, "وكيل قياس WI-082", "worker", authorizer=authorizer)

    assert identity.agent_id == agent_id
    assert _row_exists(agent_id)
    assert len(authorizer.results) == 1
    outcome = authorizer.results[0].outcome
    passed_stages = {
        str(getattr(stage, "name", stage)) for stage in outcome.stages
    }
    for mandatory in MANDATORY_INTERNAL_STAGES:
        mandatory_name = str(getattr(mandatory, "name", mandatory))
        assert mandatory_name in passed_stages, f"مرحلةٌ إلزاميّةٌ لم تمرّ: {mandatory_name}"
    # حكمُ البوّابةِ مقروءٌ لا مظنون: الأثرُ الدستوريُّ مُوثَّقٌ في نتيجةِ الحدِّ.
    assert authorizer.results[0].evidence.decision == "ALLOW"


def test_register_identity_declares_effect_under_target(agent_id: str) -> None:
    """W-2: الأثرُ المُعلَنُ صفٌّ في `agents` تحتَ الهدفِ المُعلَنِ نفسِه."""
    authorizer = RecordingAuthorizer()
    register_identity(agent_id, "وكيل قياس WI-082", "worker", authorizer=authorizer)

    call = authorizer.calls[0]
    assert call["action"] == "spawn_agent"
    assert call["kwargs"]["operation_key"].value == agent_id
    (effect,) = call["kwargs"]["declared_effects"]
    assert effect.kind.value == "CREATE"
    assert effect.resource == f"agent/{agent_id}"


def test_register_identity_refused_at_kill_switch_level_3(agent_id: str) -> None:
    """W-3: المستوى الثالثُ يُجمّدُ `spawn_agent` فلا تُنشأُ هويّةٌ (قرارُ المالكِ Q-15 ①)."""
    from core.sovereignty.gateway import SovereigntyViolation

    authorizer = HaltedAtLevel3Authorizer()
    with pytest.raises(SovereigntyViolation) as excinfo:
        register_identity(agent_id, "وكيل مرفوض", "worker", authorizer=authorizer)

    assert "زر التوقف" in str(excinfo.value) or "spawn_agent" in str(excinfo.value)
    assert not _row_exists(agent_id)


def test_register_identity_compensator_is_real_reversal(agent_id: str) -> None:
    """W-4: المعوّضُ المربوطُ عكسٌ حقيقيٌّ يحذفُ الصفَّ فعلًا (1I — سابقةُ 2B S-5).

    التشغيلُ الآليُّ للتعويضِ بعدَ الفشلِ **غيرُ مبنيٍّ** (مُعلَنٌ في `PROJECT_STATE.md`:
    «لا وصل تلقائيًا بين RECOVERY_REQUIRED وخطّة تعويض 1I») — فيُقاسُ المعوّضُ
    المربوطُ نفسُه: يُنادى فيحذفُ الصفَّ، لا وعدًا في خطة.
    """
    authorizer = RecordingAuthorizer()
    register_identity(agent_id, "وكيل قياس التعويض", "worker", authorizer=authorizer)

    outcome = authorizer.results[0].outcome
    plan = outcome.compensation_plan
    assert plan is not None, "لم تُبنَ خطّةُ تعويض."
    applied = set(outcome.applied_signatures)
    assert applied, "لا أثرًا مُطبَّقًا مُسجَّلًا."
    assert applied <= plan.covered_signatures, (
        f"أثرٌ بلا معوّضٍ مربوط: {applied - plan.covered_signatures}"
    )
    assert _row_exists(agent_id)

    entry = plan.compensator_for(next(iter(applied)))
    assert entry.apply() is True, "المعوّضُ لم يفعلْ شيئًا."
    assert not _row_exists(agent_id), "المعوّضُ المربوطُ لم يحذفِ الصفَّ — فهو وعدٌ لا عكس."


def test_register_identity_failure_is_fail_closed(agent_id: str) -> None:
    """W-4: فشلٌ بعدَ الكتابةِ يُغلقُ ولا يُدَّعى نجاحًا (1J — سابقةُ 2B S-6).

    الحدُّ يرفعُ `IdempotencyError` حاملةً سببَ الفشلِ ولا يُقلَبُ نجاحًا، ولا
    تُرجَعُ حصيلةُ نجاحٍ من نداءٍ فاشل. (والتعويضُ الآليُّ بعدَ الفشلِ غيرُ مبنيٍّ
    — مُعلَنٌ فوقُ — فلا يُدَّعى هنا.)
    """
    from core.sovereignty.idempotency import IdempotencyError

    def _write_then_fail(row: AgentModel) -> None:
        # كتابةٌ مباشرةٌ ثمّ فشلٌ: لا يُنادى الاسمُ المعوّضُ نفسُه (وإلّا استدعاءٌ ذاتيٌّ).
        session = get_session_factory()()
        try:
            session.add(row)
            session.commit()
        finally:
            session.close()
        raise RuntimeError("فشلٌ مُفتعَلٌ بعدَ الكتابةِ — يُقاسُ الإغلاقُ")

    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(identity_module, "_write_identity_row", _write_then_fail)
    authorizer = RecordingAuthorizer()
    try:
        with pytest.raises((IdempotencyError, RuntimeError)):
            register_identity(agent_id, "وكيل قياس الإغلاق", "worker", authorizer=authorizer)
    finally:
        monkeypatch.undo()

    # لا حصيلةَ نجاحٍ من نداءٍ فاشل — والقيمةُ لا تُقْرَأُ أصلًا.
    assert authorizer.results == [], "أُرجِعت حصيلةُ نجاحٍ من نداءٍ فاشل."


def test_register_identity_replay_does_not_invent_or_duplicate(agent_id: str) -> None:
    """W-5: مفتاحٌ واحدٌ لا يُنتِجُ أثرًا ثانيًا — والإعادةُ لا تَختلِقُ وكيلًا."""
    register_identity(agent_id, "وكيل الإعادة", "worker")
    assert _row_exists(agent_id)

    # افتراقٌ مُفتعَلٌ بينَ السجلِّ والجدولِ: حُذفَ الصفُّ خارجيًّا ثمّ أُعيدَ النداءُ
    # بالمفتاحِ نفسِه — فالحدَّ يرى العمليّةَ مُثبَّتةً فلا يُطبِّقُ الأثرَ مرّةً ثانيةً.
    _delete_row_directly(agent_id)
    with pytest.raises(UnknownAgentIdentityError):
        register_identity(agent_id, "وكيل الإعادة", "worker")
    assert not _row_exists(agent_id)


def test_register_identity_signature_breaks_nothing_and_has_no_bypass() -> None:
    """W-6: صفرُ كسرٍ في العقدِ القائمِ — ولا معاملَ تجاوزٍ في الوجهِ الجديدِ."""
    import inspect

    signature = inspect.signature(register_identity)
    # النداءُ القائمُ (8 مواضعَ إنتاجيّةً و28 نداءَ اختبارٍ) لا يُمرِّرُ `authorizer`:
    # فكلُّ معاملاتِه الجديدةُ اختياريّةٌ بالاسمِ لا تُلزمُ أحدًا.
    assert signature.parameters["authorizer"].default is None
    assert signature.parameters["authorizer"].kind == inspect.Parameter.KEYWORD_ONLY
    forbidden = {"force", "bypass", "skip_check", "unchecked", "override", "no_verify", "unsafe"}
    assert not (set(signature.parameters) & forbidden), "معاملُ تجاوزٍ في وجهِ الحدّ"
