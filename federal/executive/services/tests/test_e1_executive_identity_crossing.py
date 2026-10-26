"""WI-119 · E1 — عبورُ أسطحِ الهويّةِ التنفيذيّةِ (تصميمُ W-694 · اعتمادُ المالكِ 2026-10-26).

الهدف: إثباتُ أنَّ أسطحَ executive_core الستةَ تعبرُ الحدَّ السياديَّ بأفعالِ
       القاموسِ الثالثَ عشرَ المعتمدِ («اعتمادُ تصميمِ E1 (13 اسمًا)» — سجلُّ
       قراراتِ المالكِ)، وأنَّ الرفضَ قبلَ الكتابةِ المرتكزةِ، وأنَّ الإعادةَ لا
       تُكرِّرُ الأثرَ، وأنَّ التعويضَ عكسٌ حقيقيٌّ.
النطاق: قياسُ سلوكِ الأسطحِ المعبَّرةِ وحدَه — لا تعديلَ للبوابةِ ولا للقواعدِ.
        حقنُ مستوى زرِّ الإيقافِ في الطلبِ محاكاةٌ لحالةِ الزرِّ معلَنةٌ هنا
        لا تجاوزٌ للبوّابةِ (نمطُ WI-082).
المالك: federal/executive/services — WI-119 (تصميمُ W-694 · تصميمُ E1).
تاريخ الإنشاء: 2026-10-27 (W-696 · WI-119)

الأسطحُ المُعايَنةُ (تصميمُ E1 § 2.2 — وجيزةُ executive_core الستةُ):
    update_identity → update_agent_identity (L3) · set_lifecycle_state →
    contain_agent/activate_agent بالاتجاهِ (الاحتواءُ بلا منعٍ · الاستعادةُ L4) ·
    dispatcher.register_agent → spawn_agent (L3) · repository.create → create_task
    · repository.delete → delete_task · repository.compare_and_set →
    transition_task_state (الثلاثةُ L4).

أصنافُ الفحصِ الخمسةُ (تصميمُ E1 § 3):
    1. الرفضُ قبلَ الكتابةِ المرتكزةِ — زرُّ الإيقافِ يمنعُ بالاسمِ ولا يُكتَبُ شيءٌ.
    2. النجاحُ بالفاعلِ الصحيحِ معَ الأثرِ المُعلَنِ — الدليلُ الحرفيُّ مُسجَّلٌ.
    3. طفرةٌ واحدةٌ لكلِّ سطحٍ — رفعُ العبورِ يُسقِطُ الفحصَ (أدلةُ الصنفِ 2 هي
       كاشفُ الطفرةِ: بلا عبورٍ لا دليلَ) ورفعُ الاسمِ من القاموسِ يُسقِطُ فحوصَ
       المستوياتَ.
    4. لا تكرارَ أثرٍ عندَ الإعادةِ + قبولُ العمليّةِ المشروعةِ اللاحقةِ.
    5. التعويضُ الحقيقيُّ — فشلٌ بعدَ الحارسِ يُرجِعُ الحالةَ بلا مسِّ أحدثِ منها.

الدليلُ المُعادُ تشغيلُه:
    .venv/bin/python -m pytest federal/executive/services/tests/test_e1_executive_identity_crossing.py -q
"""

from __future__ import annotations

import dataclasses
from typing import Any

import pytest

from amos_federation.services.executive_core.agent_identity import (
    ACTION_ACTIVATE_AGENT,
    ACTION_CONTAIN_AGENT,
    ACTION_UPDATE_AGENT_IDENTITY,
    AGENT_IDENTITY_ACTOR,
    register_identity,
    set_lifecycle_state,
    update_identity,
)
from amos_federation.services.executive_core.dispatcher import register_agent
from amos_federation.services.executive_core.repository import ExecutiveTaskRepository
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from amos_federation.services.executive_core.states import TaskState
from tests.conftest import purge_agents


class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجل كل نتيجة محروسة — لأجل قياس الاعتمادية، لا لاتخاذ قرار (نمط WI-082)."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.results.append(guarded)
        return guarded


class KillSwitchLevelAuthorizer(ConstitutionalAuthorizer):
    """الطلبُ يحملُ مستوى زرِّ الإيقافِ — محاكاةُ حالةِ الزرِّ لا تجاوزٌ (نمط WI-082)."""

    def __init__(self, level: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._kill_switch_level = level

    def _request(
        self,
        action: str,
        target: str,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        request = super()._request(action, target, metadata)
        return dataclasses.replace(request, kill_switch_level=self._kill_switch_level)


@pytest.fixture(autouse=True)
def _fresh_tables() -> None:
    """قاعدة نظيفة — القياس على سجل حقيقي لا على بقايا (نمط test_r4 · WI-082)."""
    from amos_federation.common.database import TaskModel, get_session_factory, init_db
    from amos_federation.services.executive_core.agent_identity import AgentModel
    from tests.conftest import purge_tasks

    init_db()
    session = get_session_factory()()
    try:
        purge_tasks(session)
        purge_agents(session)
        session.query(AgentModel).delete()
        session.query(TaskModel).delete()
        session.commit()
    finally:
        session.close()


def _spawn(agent_id: str, *, state: str = "active") -> None:
    """بذرةُ وكيلٍ عاملةٍ عبرَ المسارِ العلنيِّ المحروسِ نفسِهِ."""
    register_identity(agent_id, f"وكيل {agent_id}", "worker")
    if state != "registered":
        set_lifecycle_state(agent_id, state)


def _evidence(recorder: RecordingAuthorizer) -> dict[str, Any]:
    assert recorder.results, "لم يُعبَرِ الحدُّ السياديُّ أصلًا"
    return recorder.results[-1].evidence.as_dict()


# ── الصنفُ 1 · الرفضُ قبلَ الكتابةِ المرتكزةِ (زرُّ الإيقافِ بالاسمِ) ───────────


def test_e1_1_level3_blocks_update_agent_identity_without_write() -> None:
    authorizer = KillSwitchLevelAuthorizer(level=3, actor=AGENT_IDENTITY_ACTOR)
    _spawn("e1-l3-update")
    before = update_identity("e1-l3-update", authorizer=RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR))

    from core.sovereignty.gateway import SovereigntyViolation

    with pytest.raises(SovereigntyViolation) as excinfo:
        update_identity("e1-l3-update", name="اسم محجوز", authorizer=authorizer)

    message = str(excinfo.value)
    assert "update_agent_identity" in message
    assert "المستوى 3" in message

    # الرفضُ منعٌ حقيقيٌّ: الحقلُ لم يتغيّرْ.
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("e1-l3-update").name == before.name


def test_e1_2_level4_blocks_restoration_but_not_containment() -> None:
    """بالاسمِ لا بالتخمينِ: `activate_agent` محجوزٌ منَ الرابعِ و`contain_agent` لا يُمنَعُ."""
    authorizer = KillSwitchLevelAuthorizer(level=4, actor=AGENT_IDENTITY_ACTOR)
    _spawn("e1-l4-agent")
    set_lifecycle_state("e1-l4-agent", "paused")  # الاحتواءُ يعملُ تحتَ الرابعِ

    from core.sovereignty.gateway import SovereigntyViolation

    with pytest.raises(SovereigntyViolation) as excinfo:
        set_lifecycle_state("e1-l4-agent", "active", authorizer=authorizer)

    assert "activate_agent" in str(excinfo.value)
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("e1-l4-agent").lifecycle_state == "paused"


def test_e1_3_level4_blocks_task_surfaces_without_write() -> None:
    repo = ExecutiveTaskRepository()
    from core.sovereignty.gateway import SovereigntyViolation

    original = ExecutiveTaskRepository._authorizer
    ExecutiveTaskRepository._authorizer = lambda self: KillSwitchLevelAuthorizer(
        level=4
    )
    try:
        with pytest.raises(SovereigntyViolation) as excinfo:
            repo.create("e1-l4-task", "analysis", "مهمة تحت المستوى الرابع")
    finally:
        ExecutiveTaskRepository._authorizer = original

    assert "create_task" in str(excinfo.value)
    assert repo.get("e1-l4-task") is None, "الرفضُ كتبَ صفًّا"


def test_e1_4_delete_of_missing_task_never_crosses() -> None:
    """قاعدةُ نطاقٍ قبلَ الحدِّ: محوُ ما لا وجودَ لهُ لا عمليّةً سياديّةً أصلًا."""
    recorder = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    repo = ExecutiveTaskRepository()
    original = ExecutiveTaskRepository._authorizer
    ExecutiveTaskRepository._authorizer = lambda self: recorder
    try:
        assert repo.delete("e1-ghost-task") is False
    finally:
        ExecutiveTaskRepository._authorizer = original
    assert not recorder.results, "عبورٌ سياديٌّ لِما لم يقعْ"


# ── الصنفُ 2 · النجاحُ بالفاعلِ الصحيحِ معَ الأثرِ المُعلَنِ (كاشفُ الطفرةِ) ────


def test_e1_5_update_identity_crosses_with_literal_evidence() -> None:
    recorder = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    _spawn("e1-update")

    updated = update_identity("e1-update", name="اسم محدَّث", authorizer=recorder)

    assert updated.name == "اسم محدَّث"
    evidence = _evidence(recorder)
    assert evidence["action"] == ACTION_UPDATE_AGENT_IDENTITY == "update_agent_identity"
    assert evidence["target"] == "agent:e1-update"
    assert evidence["decision"] == "ALLOW"
    assert evidence["request_fingerprint"]
    assert evidence["ledger_entry_hash"]


def test_e1_6_lifecycle_crosses_by_direction() -> None:
    recorder = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    _spawn("e1-lifecycle")

    assert set_lifecycle_state("e1-lifecycle", "paused", authorizer=recorder) is True
    assert _evidence(recorder)["action"] == ACTION_CONTAIN_AGENT == "contain_agent"

    assert set_lifecycle_state("e1-lifecycle", "active", authorizer=recorder) is True
    assert _evidence(recorder)["action"] == ACTION_ACTIVATE_AGENT == "activate_agent"


def test_e1_7_dispatcher_register_agent_crosses_spawn() -> None:
    recorder = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)

    register_agent("e1-dispatch", "وكيل الديسپاتش", "worker", authorizer=recorder)

    evidence = _evidence(recorder)
    assert evidence["action"] == "spawn_agent"
    assert evidence["decision"] == "ALLOW"


def test_e1_8_task_surfaces_cross_with_literal_evidence() -> None:
    recorder = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    repo = ExecutiveTaskRepository()
    original = ExecutiveTaskRepository._authorizer
    ExecutiveTaskRepository._authorizer = lambda self: recorder
    try:
        task = repo.create("e1-task", "analysis", "مهمة عبور")
        assert task["id"] == "e1-task"
        assert _evidence(recorder)["action"] == "create_task"

        assert repo.compare_and_set(
            "e1-task", TaskState.CREATED, TaskState.AUTHORIZED
        )
        assert _evidence(recorder)["action"] == "transition_task_state"

        assert repo.delete("e1-task") is True
        assert _evidence(recorder)["action"] == "delete_task"
    finally:
        ExecutiveTaskRepository._authorizer = original


def test_e1_9_vocabulary_is_registered_in_the_constitution() -> None:
    """القاموسُ الثالثَ عشرَ معتمَدٌ ومقيَّدٌ — رفعُ اسمٍ من rules.py يُسقِطُ هذا."""
    from core.constitutional_engine.rules import EXECUTIVE_ACTIONS

    # الأسماءُ الستةُ الجديدةُ على أسطحِ executive_core (من الثلاثةَ عشرَ
    # المعتمدةِ — spawn_agent اسمُ WI-082 القائمُ ومسارُهُ غيرُ هذا القاموسِ).
    for name in (
        "update_agent_identity",
        "contain_agent",
        "activate_agent",
        "create_task",
        "delete_task",
        "transition_task_state",
    ):
        assert name in EXECUTIVE_ACTIONS, f"اسمٌ معتمَدٌ غائبٌ عن القاموسِ: {name}"


# ── الصنفُ 4 · لا تكرارَ أثرٍ عندَ الإعادةِ + قبولُ المشروعِ اللاحقِ ───────────


def test_e1_10_lifecycle_round_trip_is_two_ops_and_resend_is_replay() -> None:
    """ACTIVE→PAUSED→ACTIVE عمليّتانِ؛ وإعادةُ إرسالِ الانتقالِ نفسِهِ إعادةٌ لا تُكرِّرُ."""
    recorder = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    _spawn("e1-roundtrip")

    assert set_lifecycle_state("e1-roundtrip", "paused", authorizer=recorder) is True
    assert set_lifecycle_state("e1-roundtrip", "active", authorizer=recorder) is True
    assert len(recorder.results) == 2, "عمليّتانِ لا ثلاثٌ"

    # إعادةُ إرسالِ بعدَ نجاحِ الانتقالِ: عمليّةٌ فارغةٌ لا تعبرُ الحدَّ أصلًا
    # (سابقةُ `update_identity` بلا حقولٍ) — فلا أثرٌ مكرَّرٌ ولا مفتاحُ ذرّيّةٍ
    # لما لم يقعْ (تصميمُ E1 § 3 الصنفُ 4 · § 2.4).
    assert set_lifecycle_state("e1-roundtrip", "active", authorizer=recorder) is True
    assert len(recorder.results) == 2, "الإعادةُ الفارغةُ عبرتِ الحدَّ"

    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("e1-roundtrip").lifecycle_state == "active"


def test_e1_11_later_legitimate_update_is_accepted() -> None:
    """تحديثانِ مختلفانِ للوكيلِ نفسِهِ عمليّتانِ — بصمةُ الحمولةِ تفرّقُ."""
    recorder = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    _spawn("e1-two-updates")

    update_identity("e1-two-updates", name="الاسم الأول", authorizer=recorder)
    update_identity("e1-two-updates", name="الاسم الثاني", authorizer=recorder)

    assert len(recorder.results) == 2
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("e1-two-updates").name == "الاسم الثاني"


def test_e1_12_task_transition_replay_refused_not_reapplied() -> None:
    recorder = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    repo = ExecutiveTaskRepository()
    original = ExecutiveTaskRepository._authorizer
    ExecutiveTaskRepository._authorizer = lambda self: recorder
    try:
        repo.create("e1-replay-task", "analysis", "مهمة إعادة")
        assert repo.compare_and_set(
            "e1-replay-task", TaskState.CREATED, TaskState.AUTHORIZED
        )

        # إعادةُ الانتقالِ المُثبَّتِ: شرطُ المقارنةِ فشلَ (الحالةُ لم تعدْ
        # متوقَّعةً) فيُرجَعُ False لا replay — «compare_and_set حارسُ التزامنِ
        # الحقيقيُّ» (حرفُّ التصميمِ § 2.4) — ولا يُطبَّقُ الأثرُ مرتينِ.
        assert (
            repo.compare_and_set("e1-replay-task", TaskState.CREATED, TaskState.AUTHORIZED)
            is False
        )
        assert repo.state_of("e1-replay-task") is TaskState.AUTHORIZED

        # والعمليّةُ المشروعةُ اللاحقةُ (اتجاهٌ مختلفٌ) مقبولةٌ.
        assert repo.compare_and_set(
            "e1-replay-task", TaskState.AUTHORIZED, TaskState.PLANNED
        )
        assert len(recorder.results) == 4
        assert recorder.results[-1].is_replay is False
    finally:
        ExecutiveTaskRepository._authorizer = original


# ── الصنفُ 5 · التعويضُ الحقيقيُّ — عكسٌ بعدَ فشلٍ لا وعظٌ ────────────────────


def test_e1_13_lifecycle_failure_after_guard_restores_previous_state() -> None:
    """فشلٌ بعدَ الحارسِ وبعدَ الكتابةِ: المعوّضُ يُرجِعُ الحالةَ السابقةَ.

    مسارُ التعويضِ في الحدِّ يُغطّي الانكسارَ بعدَ عودةِ المُطبِّقِ (تطبيقُ
    الأثرِ تمَّ ثمَّ انكسرَت مرحلةٌ لاحقةٌ) — فيُحاكى ذلكَ بانكسارِ مرحلةِ تثبيتِ
    سجلِّ الذرّيّةِ ذاتِها بعدَ التنفيذِ، والقياسُ: المعوّضُ المربوطُ سلفًا (1I)
    يعملُ فتعودُ الحالةُ السابقةُ.
    """
    _spawn("e1-compensate", state="active")
    from core.sovereignty.idempotency import IdempotencyLedger

    original_mark = IdempotencyLedger.mark_succeeded

    def _fail_after_apply(self: Any, *args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("فشلٌ بعدَ الكتابةِ — انكسارُ مرحلةِ التثبيتِ")

    IdempotencyLedger.mark_succeeded = _fail_after_apply
    try:
        with pytest.raises(Exception, match="فشلٌ بعدَ الكتابةِ"):
            set_lifecycle_state(
                "e1-compensate",
                "paused",
                authorizer=ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR),
            )
    finally:
        IdempotencyLedger.mark_succeeded = original_mark

    from amos_federation.services.executive_core.agent_identity import require_identity

    assert (
        require_identity("e1-compensate").lifecycle_state == "active"
    ), "المعوّضُ لم يُرجِعِ الحالةَ السابقةَ"


def test_e1_14_task_create_failure_after_guard_erases_the_row() -> None:
    """فشلٌ بعدَ الحارسِ وبعدَ الإنشاءِ: المعوّضُ يحذفُ الصفَّ المُنشَأ حقيقةً.

    انكسارُ مرحلةٍ لاحقةٍ لتطبيقِ الأثرِ (تثبيتُ سجلِّ الذرّيّةِ) — فيعملُ
    المعوّضُ المربوطُ سلفًا (1I): حذفُ الصفِّ المُنشَأ لا وعظٌ.
    """
    repo = ExecutiveTaskRepository()
    from core.sovereignty.idempotency import IdempotencyLedger

    original_mark = IdempotencyLedger.mark_succeeded

    def _fail_after_apply(self: Any, *args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("فشلٌ بعدَ الإنشاءِ — انكسارُ مرحلةِ التثبيتِ")

    IdempotencyLedger.mark_succeeded = _fail_after_apply
    try:
        with pytest.raises(Exception, match="فشلٌ بعدَ الإنشاءِ"):
            repo.create("e1-compensate-task", "analysis", "مهمة معوّض")
    finally:
        IdempotencyLedger.mark_succeeded = original_mark

    assert repo.get("e1-compensate-task") is None, "المعوّضُ لم يحذفِ الصفَّ المُنشَأ"
