"""W-699 · E1 — عبورُ أسطحِ وقتِ التشغيلِ الثمانيةِ (تصميمُ E1 المعتمَدِ).

الهدف: إثباتُ أنَّ أسطحَ agent_runtime الثمانيةَ تعبرُ الحدَّ السياديَّ بأفعالِ
       القاموسِ المعتمدِ («اعتمادُ تصميمِ E1 (13 اسمًا)» — سجلُّ قراراتِ
       المالكِ)، وأنَّ الرفضَ قبلَ الكتابةِ المرتكزةِ، وأنَّ الإعادةَ لا تُكرِّرُ
       الأثرَ، وأنَّ التعويضَ عكسٌ حقيقيٌّ، وأنَّ التعشيشَ ممنوعٌ.
النطاق: قياسُ سلوكِ الأسطحِ المعبَّرةِ وحدَه — لا تعديلَ للبوابةِ ولا للقواعدِ.
        حقنُ مستوى زرِّ الإيقافِ في الطلبِ محاكاةٌ لحالةِ الزرِّ معلَنةٌ هنا
        لا تجاوزٌ للبوّابةِ (نمطُ WI-082/W-696).
المالك: federal/executive/services — W-699 (تصميمُ E1 § 2.2 · § 3).

الأسطحُ المُعايَنةُ (تصميمُ E1 § 2.2 — النصفُ الثاني: agent_runtime الثمانيةُ):
    check_agent → run_health_check · start_treatment → start_agent_treatment (L1)
    · isolate → isolate_agent · log_action → log_isolated_action · release →
    release_agent (والاتجاهُ يُحرسُ مسبقًا: retire⇒contain_agent · release⇒
    activate_agent (L4) · retrain⇒start_agent_treatment (L1)) ·
    population.register_agent → spawn_agent (L3) · update_state →
    update_population_state (L3) · take_step → record_curriculum_step (L1).

أصنافُ الفحصِ الخمسةُ (تصميمُ E1 § 3):
    1. الرفضُ قبلَ الكتابةِ المرتكزةِ — زرُّ الإيقافِ يمنعُ بالاسمِ ولا يُكتَبُ شيءٌ.
    2. النجاحُ بالفاعلِ الصحيحِ معَ الأثرِ المُعلَنِ — الدليلُ الحرفيُّ مُسجَّلٌ.
    3. طفرةٌ واحدةٌ لكلِّ سطحٍ منَ الـ14 — نزعُ الحارسِ يُسقِطُ فحصَ الصنفِ 2
       (تنفيذٌ فعليٌّ مسجَّلُ النتائجِ: خطَّ الأساسِ ثمَّ الطفرةُ ثمَّ العودةُ).
    4. لا تكرارَ أثرٍ عندَ الإعادةِ + قبولُ العمليّةِ المشروعةِ اللاحقةِ.
    5. كاشفُ التعشيشِ — عبورٌ داخلَ مُطبِّقِ عبورٍ يرتفعُ صريحًا.

الدليلُ المُعادُ تشغيلُه:
    .venv/bin/python -m pytest federal/executive/services/tests/test_w699_agent_runtime_crossing.py -q
"""

from __future__ import annotations

import dataclasses
import json
import linecache
import os
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable

from amos_federation.services.agent_runtime.health import (
    ACTION_ISOLATE_AGENT,
    ACTION_LOG_ISOLATED_ACTION,
    ACTION_RELEASE_AGENT,
    ACTION_RUN_HEALTH_CHECK,
    ACTION_START_AGENT_TREATMENT,
    get_isolation_system,
    get_treatment_system,
)
from amos_federation.services.agent_runtime.population import (
    ACTION_RECORD_CURRICULUM_STEP,
    ACTION_UPDATE_POPULATION_STATE,
    AgentSchool,
    PopulationRegistry,
)
from amos_federation.services.executive_core.agent_identity import (
    register_identity,
    set_lifecycle_state,
)
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    GuardedResult,
    compensator,
)
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
    """الطلبُ يحملُ مستوى زرِّ الإيقافِ — محاكاةُ حالةِ الزرِّ لا تجاوز (نمط WI-082)."""

    def __init__(self, level: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._kill_switch_level = level

    def _request(
        self,
        action: str,
        target: str,
        metadata: dict[str, Any] | None = None,
        human_approval: Any = None,
    ) -> Any:
        request = super()._request(action, target, metadata, human_approval)
        return dataclasses.replace(request, kill_switch_level=self._kill_switch_level)


def _reset_runtime_tables() -> None:
    """قاعدة نظيفة — القياس على سجل حقيقي لا على بقايا (نمط test_r4 · WI-082).

    دالةٌ صريحةٌ لا تجهيزةً: يُستدعى التجهيزُ التلقائيُّ لكلِّ فحصٍ ويُستدعى
    هذا التنظيفُ نفسُهُ داخلَ فحصِ الطفرةِ قبلَ كلِّ حالةٍ (لا يُستدعى التجهيزُ
    مباشرةً — يمنعُهُ pytest).
    """
    from sqlalchemy import create_engine

    from amos_federation.common.database import (
        get_database_url,
        get_session_factory,
        init_db,
    )
    from amos_federation.services.agent_runtime.health import (
        AgentHealthCheckModel,
        IsolationRecordModel,
        TreatmentRecordModel,
        _HealthBase,
    )
    from amos_federation.services.agent_runtime.population import (
        AgentPopulationModel,
        PopulationBase,
        SchoolResultModel,
    )
    from amos_federation.services.executive_core.agent_identity import AgentModel
    from tests.conftest import purge_tasks

    init_db()
    engine = create_engine(get_database_url())
    _HealthBase.metadata.create_all(engine)
    PopulationBase.metadata.create_all(engine)
    session = get_session_factory()()
    try:
        purge_tasks(session)
        # من الأخصّ إلى الأعمّ: جداولُ وقتِ التشغيلِ قبلَ الهويّاتِ.
        for model in (
            AgentHealthCheckModel,
            TreatmentRecordModel,
            IsolationRecordModel,
            SchoolResultModel,
            AgentPopulationModel,
        ):
            session.query(model).delete()
        purge_agents(session)
        session.query(AgentModel).delete()
        session.commit()
    finally:
        session.close()
    # إعادةُ ضبطِ المُصرِّحينَ الافتراضيينَ للوحدتينِ (كائنٌ واحدٌ لكلِّ وحدةٍ).
    import amos_federation.services.agent_runtime.health as _health_mod
    import amos_federation.services.agent_runtime.population as _population_mod

    _health_mod._DEFAULT_AUTHORIZER = None
    _population_mod._DEFAULT_AUTHORIZER = None


@pytest.fixture(autouse=True)
def _fresh_runtime_tables() -> None:
    """قاعدةٌ نظيفةٌ لكلِّ فحصٍ — التنظيفُ نفسُهُ الذي تستدعيهِ حالةُ الطفرةِ."""
    _reset_runtime_tables()


def _spawn(agent_id: str, *, state: str = "active") -> None:
    """بذرةُ وكيلٍ عاملةٍ عبرَ المسارِ العلنيِّ المحروسِ نفسِهِ."""
    register_identity(agent_id, f"وكيل {agent_id}", "worker")
    if state != "registered":
        set_lifecycle_state(agent_id, state)


def _evidence(recorder: RecordingAuthorizer, index: int = -1) -> dict[str, Any]:
    """الدليلُ الحرفيُّ لآخرِ عبورٍ — أو عبورٍ بفهرسِهِ (العبورُ الأولُ/الأخيرُ)."""
    assert recorder.results, "لم يُعبَرِ الحدُّ السياديُّ أصلًا"
    return recorder.results[index].evidence.as_dict()


def _isolation_row(isolation_id: str) -> Any:
    from amos_federation.services.agent_runtime.health import (
        _get_isolation_record_core,
    )

    return _get_isolation_record_core(isolation_id)


# ── الصنفُ 2 · النجاحُ بالفاعلِ الصحيحِ معَ الأثرِ المُعلَنِ (الدليلُ الحرفيُّ) ──


def test_w699_2_check_agent_crosses_run_health_check() -> None:
    """check_agent يعبرُ بفعلِ run_health_check ويسجلُ سجلَّ الفحصِ."""
    _spawn("w699-check")
    checker = get_health_checker_for_test()
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    result = checker.check_agent("w699-check", check_id="w699-check-1", authorizer=recorder)

    assert result["agent_id"] == "w699-check"
    evidence = _evidence(recorder)
    assert evidence["action"] == ACTION_RUN_HEALTH_CHECK == "run_health_check"
    assert evidence["decision"] == "ALLOW"
    assert evidence["ledger_entry_hash"]
    assert "agents.health.check" in recorder.results[-1].outcome.operation_key
    # الصدقُ أن يُقرأَ الأثرُ بعدَ العبورِ: الصفُّ موجودٌ فعلًا بسلسلةِ التجزئةِ.
    from amos_federation.services.agent_runtime.health import _health_check_hash

    assert _health_check_hash("w699-check-1"), "سجلُّ الفحصِ غائبٌ بعدَ عبورٍ ناجحٍ"


def test_w699_2_start_treatment_crosses_with_two_sessions() -> None:
    """start_treatment: عبورُ البدءِ بأثرَينِ معلنَينِ ثمَّ عبورُ الإتمامِ المستقلُّ."""
    _spawn("w699-treat")
    system = get_treatment_system()
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    system.start_treatment(
        "w699-treat",
        "reset_context",
        "اختبار العبور",
        treatment_id="w699-treat-1",
        authorizer=recorder,
    )

    # ثلاثةُ عبوراتٍ متعاقبةٍ: البدءُ (أثرانِ) ثمَّ الإتمامُ ثمَّ العودةُ الكانونيّةُ
    # إلى active عبرَ العبورِ العلنيِّ (activate_agent) — كلٌّ بفعلِهِ ومفتاحِهِ.
    assert len(recorder.results) == 3, "البدءُ والإتمامُ والعودةُ ثلاثةُ عبوراتٍ مستقلةٍ"
    assert _evidence(recorder, 0)["action"] == ACTION_START_AGENT_TREATMENT
    assert _evidence(recorder, 1)["action"] == ACTION_START_AGENT_TREATMENT
    assert _evidence(recorder, 2)["action"] == "activate_agent"
    assert "agents.treatment" in recorder.results[0].outcome.operation_key
    # مفتاحُ الإتمامِ مميّزٌ بالإتمامِ — فعمليّتانِ لا إعادةٌ واحدةٌ (تصميمُ E1 § 2.5).
    assert "agents.treatment.complete" in recorder.results[1].outcome.operation_key
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("w699-treat").lifecycle_state == "active"


def test_w699_2_isolate_crosses_with_two_declared_effects() -> None:
    """isolate يعبرُ بأثرَينِ معلنَينِ في عبورٍ واحدٍ (سجلُّ العزلِ + الانتقالُ)."""
    _spawn("w699-iso")
    system = get_isolation_system()
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    system.isolate("w699-iso", "اختبار", isolation_id="w699-iso-1", authorizer=recorder)

    evidence = _evidence(recorder)
    assert evidence["action"] == ACTION_ISOLATE_AGENT == "isolate_agent"
    assert evidence["decision"] == "ALLOW"
    assert "agents.isolation" in recorder.results[-1].outcome.operation_key
    assert _isolation_row("w699-iso-1") is not None
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("w699-iso").lifecycle_state == "paused"


def test_w699_2_log_action_crosses_log_isolated_action() -> None:
    """log_action يعبرُ بفعلِ log_isolated_action ويُلحِقُ بالإدخالِ مُعرِّفًا."""
    _spawn("w699-log")
    system = get_isolation_system()
    system.isolate("w699-log", "اختبار", isolation_id="w699-log-1")
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    result = system.log_action(
        "w699-log-1", "tool_call", {"tool": "search"}, entry_id="w699-log-e1", authorizer=recorder
    )

    assert result["logged"] is True
    evidence = _evidence(recorder)
    assert evidence["action"] == ACTION_LOG_ISOLATED_ACTION == "log_isolated_action"
    assert "agents.isolation.log" in recorder.results[-1].outcome.operation_key
    row = _isolation_row("w699-log-1")
    assert row is not None and len(row.actions_log) == 1
    assert row.actions_log[0]["entry_id"] == "w699-log-e1"


def test_w699_2_release_crosses_and_guards_direction_prechecked() -> None:
    """release يعبرُ بفعلِ release_agent والاتجاهُ محروسٌ بتحققٍ مسبقٍ قبلَ الكتابةِ."""
    _spawn("w699-rel")
    system = get_isolation_system()
    system.isolate("w699-rel", "اختبار", isolation_id="w699-rel-1")
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    system.release("w699-rel-1", "retire", authorizer=recorder)

    evidence = _evidence(recorder)
    assert evidence["action"] == ACTION_RELEASE_AGENT == "release_agent"
    assert "agents.isolation.release" in recorder.results[-1].outcome.operation_key
    row = _isolation_row("w699-rel-1")
    assert row is not None and row.status == "retire"
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("w699-rel").lifecycle_state == "retired"


def test_w699_2_population_register_agent_crosses_spawn() -> None:
    """register_agent يعبرُ بأثرَي الهويّةِ والملفِّ التدريبيِّ في عبورٍ واحدٍ."""
    registry = PopulationRegistry()
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    registry.register_agent(
        "وكيل عبور",
        "executor",
        "cognitive_executor",
        agent_id="w699-reg-1",
        authorizer=recorder,
    )

    evidence = _evidence(recorder)
    assert evidence["action"] == "spawn_agent"
    assert "agents.population.spawn" in recorder.results[-1].outcome.operation_key
    from amos_federation.services.agent_runtime.population import AgentPopulationModel
    from amos_federation.services.executive_core.agent_identity import get_identity

    assert get_identity("w699-reg-1") is not None, "الهويّةُ غائبةٌ بعدَ عبورٍ ناجحٍ"
    session = registry._Session()
    try:
        assert (
            session.query(AgentPopulationModel)
            .filter(AgentPopulationModel.agent_id == "w699-reg-1")
            .first()
            is not None
        ), "الملفُّ التدريبيُّ غائبٌ بعدَ عبورٍ ناجحٍ"
    finally:
        session.close()


def test_w699_2_update_state_crosses_population_mirror() -> None:
    """update_state: الانتقالُ الكانونيُّ ثمَّ عبورُ المرآةِ بفعلِ update_population_state."""
    registry = PopulationRegistry()
    # صفُّ الملفِّ التدريبيِّ عبرَ المسارِ المحروسِ نفسِهِ.
    registry.register_agent("وكيل تحديث", "executor", "cognitive_executor", agent_id="w699-upd")
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    updated = registry.update_state("w699-upd", "paused", authorizer=recorder)

    assert updated is True
    evidence = _evidence(recorder)
    # عبورُ السطحِ هو الأخيرُ (الكانونيُّ يقعُ أولًا بفعلِهِ الموجَّهِ).
    assert evidence["action"] == ACTION_UPDATE_POPULATION_STATE == "update_population_state"
    assert "agents.population.state" in recorder.results[-1].outcome.operation_key
    from amos_federation.services.agent_runtime.population import AgentPopulationModel

    session = registry._Session()
    try:
        row = (
            session.query(AgentPopulationModel)
            .filter(AgentPopulationModel.agent_id == "w699-upd")
            .first()
        )
        assert row is not None and row.state == "paused"
    finally:
        session.close()


def test_w699_2_take_step_crosses_record_curriculum_step() -> None:
    """take_step يعبرُ بفعلِ record_curriculum_step ويُلحِقُ نتيجةَ الخطوةِ."""
    _spawn("w699-step")
    school = AgentSchool()
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    result = school.take_step("w699-step", 1, 90, result_id="w699-step-1", authorizer=recorder)

    assert "error" not in result
    evidence = _evidence(recorder)
    assert evidence["action"] == ACTION_RECORD_CURRICULUM_STEP == "record_curriculum_step"
    assert "agents.curriculum.step" in recorder.results[-1].outcome.operation_key


# ── الصنفُ 1 · الرفضُ قبلَ الكتابةِ المرتكزةِ (زرُّ الإيقافِ بالاسمِ) ───────────


def _sovereignty_violation() -> type[Exception]:
    from core.sovereignty.gateway import SovereigntyViolation

    return SovereigntyViolation


def _compensation_required() -> type[Exception]:
    """فشلُ المُطبِّقِ داخلَ العبورِ يُخاطِبُ الحدَّ فيعوِّضُ ثمَّ يرفعُ
    CompensationRequired صريحًا — لا الانكسارَ الأصليَّ عاريًا."""
    from core.sovereignty.compensation import CompensationRequired

    return CompensationRequired


def _idempotency_error() -> type[Exception]:
    """فشلُ عبورٍ قبلَ تطبيقِ أيِّ أثرٍ يُعيدُهُ الحدُّ عاريًا ملفوفًا
    IdempotencyError — لا معوِّضًا يُشغِّلُهُ الحدُّ فلا CompensationRequired."""
    from core.sovereignty.idempotency import IdempotencyError

    return IdempotencyError


def test_w699_1_level1_blocks_treatment_without_write() -> None:
    """المستوى 1 يمنعُ start_agent_treatment قبلَ أيِّ كتابةٍ (صنفُ train_model)."""
    _spawn("w699-block-treat")
    system = get_treatment_system()
    authorizer = KillSwitchLevelAuthorizer(level=1, actor="EXECUTIVE")

    with pytest.raises(_sovereignty_violation()):
        system.start_treatment(
            "w699-block-treat",
            "reset_context",
            "اختبار المنع",
            treatment_id="w699-block-treat-1",
            authorizer=authorizer,
        )

    from amos_federation.services.agent_runtime.health import _get_treatment_record_core
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert _get_treatment_record_core("w699-block-treat-1") is None, "سجلٌّ كُتِبَ بعدَ منعٍ"
    assert require_identity("w699-block-treat").lifecycle_state == "active", "انتقالٌ كُتِبَ بعدَ منعٍ"


def test_w699_1_level4_blocks_release_restore_without_write() -> None:
    """المستوى 4 يمنعُ رفعَ العزلِ استعادةًً (activate_agent) قبلَ أيِّ كتابةٍ."""
    _spawn("w699-block-rel")
    system = get_isolation_system()
    system.isolate("w699-block-rel", "اختبار", isolation_id="w699-block-rel-1")
    authorizer = KillSwitchLevelAuthorizer(level=4, actor="EXECUTIVE")

    with pytest.raises(_sovereignty_violation()):
        system.release("w699-block-rel-1", "release", authorizer=authorizer)

    row = _isolation_row("w699-block-rel-1")
    assert row is not None and row.status == "active", "سجلُّ العزلِ حُدِّثَ بعدَ منعٍ"
    assert row.released_at is None, "وقتُ الرفعِ كُتِبَ بعدَ منعٍ"
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("w699-block-rel").lifecycle_state == "paused", "استعادةُ قدرةٍ بعدَ منعٍ"


def test_w699_1_level1_blocks_release_retrain_without_write() -> None:
    """المستوى 1 يمنعُ رفعَ العزلِ بإعادةِ تدريبٍ (start_agent_treatment) قبلَ الكتابةِ."""
    _spawn("w699-block-ret")
    system = get_isolation_system()
    system.isolate("w699-block-ret", "اختبار", isolation_id="w699-block-ret-1")
    authorizer = KillSwitchLevelAuthorizer(level=1, actor="EXECUTIVE")

    with pytest.raises(_sovereignty_violation()):
        system.release("w699-block-ret-1", "retrain", authorizer=authorizer)

    row = _isolation_row("w699-block-ret-1")
    assert row is not None and row.status == "active", "سجلُّ العزلِ حُدِّثَ بعدَ منعٍ"


def test_w699_1_level3_blocks_population_spawn_without_write() -> None:
    """المستوى 3 يمنعُ spawn_agent قبلَ أيِّ كتابةٍ (لا هويّةَ ولا ملفًّا تدريبيًّا)."""
    registry = PopulationRegistry()
    authorizer = KillSwitchLevelAuthorizer(level=3, actor="EXECUTIVE")

    with pytest.raises(_sovereignty_violation()):
        registry.register_agent(
            "وكيل ممنوع",
            "executor",
            "cognitive_executor",
            agent_id="w699-block-spawn",
            authorizer=authorizer,
        )

    from amos_federation.services.executive_core.agent_identity import get_identity

    assert get_identity("w699-block-spawn") is None, "هويّةٌ كُتِبَتْ بعدَ منعٍ"
    session = registry._Session()
    try:
        from amos_federation.services.agent_runtime.population import AgentPopulationModel

        assert (
            session.query(AgentPopulationModel)
            .filter(AgentPopulationModel.agent_id == "w699-block-spawn")
            .first()
            is None
        ), "ملفٌّ تدريبيٌّ كُتِبَ بعدَ منعٍ"
    finally:
        session.close()


def test_w699_1_level3_blocks_population_mirror_without_write() -> None:
    """المستوى 3 يمنعُ update_population_state قبلَ أيِّ كتابةٍ (تحقّقٌ مسبقٌ)."""
    registry = PopulationRegistry()
    registry.register_agent(
        "وكيل مرآة", "executor", "cognitive_executor", agent_id="w699-block-mirror"
    )
    authorizer = KillSwitchLevelAuthorizer(level=3, actor="EXECUTIVE")

    with pytest.raises(_sovereignty_violation()):
        registry.update_state("w699-block-mirror", "paused", authorizer=authorizer)

    from amos_federation.services.agent_runtime.population import AgentPopulationModel
    from amos_federation.services.executive_core.agent_identity import require_identity

    # لا كتابةً كانونيّةً ولا مرآةً: الرفضُ المسبقُ سبقَ الانتقالَ الكانونيَّ نفسَهُ.
    assert (
        require_identity("w699-block-mirror").lifecycle_state == "registered"
    ), "انتقالٌ كانونيٌّ كُتِبَ بعدَ منعٍ"
    session = registry._Session()
    try:
        row = (
            session.query(AgentPopulationModel)
            .filter(AgentPopulationModel.agent_id == "w699-block-mirror")
            .first()
        )
        assert row is not None and row.state == "registered", "مرآةٌ كُتِبَتْ بعدَ منعٍ"
    finally:
        session.close()


def test_w699_1_level4_blocks_mirror_restore_via_canonical() -> None:
    """المستوى 4: تحديثُ السكّانِ إلى active يمنعُهُ العبورُ الكانونيُّ (activate_agent)
    بعدَ نجاحِ تحقّقِ المرآةِ المسبقِ — فلا مرآةً تكذبُ بحالةٍ لم تقعْ."""
    registry = PopulationRegistry()
    registry.register_agent(
        "وكيل استعادة", "executor", "cognitive_executor", agent_id="w699-block-restore"
    )
    set_lifecycle_state("w699-block-restore", "paused")
    authorizer = KillSwitchLevelAuthorizer(level=4, actor="EXECUTIVE")

    with pytest.raises(_sovereignty_violation()):
        registry.update_state("w699-block-restore", "active", authorizer=authorizer)

    from amos_federation.services.agent_runtime.population import AgentPopulationModel

    session = registry._Session()
    try:
        row = (
            session.query(AgentPopulationModel)
            .filter(AgentPopulationModel.agent_id == "w699-block-restore")
            .first()
        )
        assert row is not None and row.state == "registered", "مرآةٌ كاذبةٌ بعدَ منعٍ"
    finally:
        session.close()


def test_w699_1_level1_blocks_curriculum_step_without_write() -> None:
    """المستوى 1 يمنعُ record_curriculum_step قبلَ أيِّ كتابةٍ."""
    _spawn("w699-block-step")
    school = AgentSchool()
    authorizer = KillSwitchLevelAuthorizer(level=1, actor="EXECUTIVE")

    with pytest.raises(_sovereignty_violation()):
        school.take_step(
            "w699-block-step", 1, 90, result_id="w699-block-step-1", authorizer=authorizer
        )

    session = school._Session()
    try:
        from amos_federation.services.agent_runtime.population import SchoolResultModel

        assert (
            session.query(SchoolResultModel)
            .filter(SchoolResultModel.agent_id == "w699-block-step")
            .first()
            is None
        ), "نتيجةُ منهجٍ كُتِبَتْ بعدَ منعٍ"
    finally:
        session.close()


def test_w699_1_containment_works_at_every_level() -> None:
    """قاعدةُ التصميمِ § 2.2 رقمُ 3: أدواتُ الاحتواءِ لا تُمنعُ عندَ أيِّ مستوىً."""
    _spawn("w699-contain")
    system = get_isolation_system()
    # المستوى 5: الاحتواءُ يعملُ — والاستعادةُ لا تُفكُّ (تصميمُ E1 قاعدةٌ 2).
    authorizer = KillSwitchLevelAuthorizer(level=5, actor="EXECUTIVE")

    system.isolate("w699-contain", "احتواء عند أعلى مستوى", authorizer=authorizer)
    result = system.log_action(
        _last_isolation_id("w699-contain"),
        "inspect",
        {"note": "فحص أثناء العزل"},
        authorizer=authorizer,
    )

    assert result["logged"] is True
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("w699-contain").lifecycle_state == "paused"
    # سجلُّ العزلِ موجودٌ عبرَ المسارِ المحروسِ (استُخرجَ معرِّفُهُ أعلاهُ).
    assert _last_isolation_id("w699-contain")


def _last_isolation_id(agent_id: str) -> str:
    from amos_federation.common.database import get_session_factory
    from amos_federation.services.agent_runtime.health import IsolationRecordModel

    session = get_session_factory()()
    try:
        row = (
            session.query(IsolationRecordModel)
            .filter(IsolationRecordModel.agent_id == agent_id)
            .order_by(IsolationRecordModel.created_at.desc())
            .first()
        )
        assert row is not None, f"لا سجلَّ عزلٍ للوكيلِ {agent_id}"
        return row.id
    finally:
        session.close()


# ── الصنفُ 4 · لا تكرارَ أثرٍ عندَ الإعادةِ + قبولُ العمليّةِ اللاحقةِ ──────────


def test_w699_4_check_agent_replay_writes_once() -> None:
    """إعادةُ الفحصِ بذاتِ check_id إعادةٌ واحدةٌ — لا صفًّا ثانيًا."""
    _spawn("w699-replay-check")
    checker = get_health_checker_for_test()
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    checker.check_agent("w699-replay-check", check_id="w699-replay-1", authorizer=recorder)
    checker.check_agent("w699-replay-check", check_id="w699-replay-1", authorizer=recorder)

    assert len(recorder.results) == 2
    assert recorder.results[1].is_replay is True, "الإعادةُ لم تُعلَنْ إعادةً"
    assert recorder.results[1].outcome.operation_key == recorder.results[0].outcome.operation_key
    from amos_federation.common.database import get_session_factory
    from amos_federation.services.agent_runtime.health import AgentHealthCheckModel

    session = get_session_factory()()
    try:
        count = (
            session.query(AgentHealthCheckModel)
            .filter(AgentHealthCheckModel.agent_id == "w699-replay-check")
            .count()
        )
        assert count == 1, f"الأثرُ تكرَّرَ ({count} صفًّا)"
    finally:
        session.close()


def test_w699_4_log_action_replay_appends_once() -> None:
    """إعادةُ الإلحاقِ بذاتِ entry_id إعادةٌ واحدةٌ — لا إدخالًا ثانيًا."""
    _spawn("w699-replay-log")
    system = get_isolation_system()
    system.isolate("w699-replay-log", "اختبار", isolation_id="w699-replay-log-1")
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    system.log_action(
        "w699-replay-log-1", "tool_call", {"n": 1}, entry_id="w699-replay-e1", authorizer=recorder
    )
    system.log_action(
        "w699-replay-log-1", "tool_call", {"n": 1}, entry_id="w699-replay-e1", authorizer=recorder
    )

    assert recorder.results[1].is_replay is True
    row = _isolation_row("w699-replay-log-1")
    assert row is not None and len(row.actions_log) == 1, "الإلحاقُ تكرَّرَ"


def test_w699_4_take_step_replay_and_later_operation() -> None:
    """إعادةُ الخطوةِ بذاتِ النتيجةِ إعادةٌ واحدةٌ، وخطوةٌ جديدةٌ عمليّةٌ لاحقةٌ."""
    _spawn("w699-replay-step")
    school = AgentSchool()
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    school.take_step("w699-replay-step", 1, 90, result_id="w699-replay-s1", authorizer=recorder)
    school.take_step("w699-replay-step", 1, 90, result_id="w699-replay-s1", authorizer=recorder)
    assert recorder.results[1].is_replay is True

    school.take_step("w699-replay-step", 2, 85, result_id="w699-replay-s2", authorizer=recorder)
    assert recorder.results[2].is_replay is False, "العمليّةُ المشروعةُ اللاحقةُ رُفضَتْ كإعادةٍ"

    session = school._Session()
    try:
        from amos_federation.services.agent_runtime.population import SchoolResultModel

        count = (
            session.query(SchoolResultModel)
            .filter(SchoolResultModel.agent_id == "w699-replay-step")
            .count()
        )
        assert count == 2, f"خطوتانِ متوقّعتانِ لا {count}"
    finally:
        session.close()


def test_w699_4_start_treatment_replay_writes_once() -> None:
    """إعادةُ العلاجِ بذاتِ المفتاحِ لا تُنشئُ سجلًّا ثانيًا ولا تُتمِّمُ مرتينِ."""
    _spawn("w699-replay-treat")
    system = get_treatment_system()
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    system.start_treatment(
        "w699-replay-treat",
        "reset_context",
        "اختبار",
        treatment_id="w699-replay-t1",
        authorizer=recorder,
    )
    system.start_treatment(
        "w699-replay-treat",
        "reset_context",
        "اختبار",
        treatment_id="w699-replay-t1",
        authorizer=recorder,
    )

    # الدفعةُ الأولى ثلاثةُ عبوراتٍ (بدءٌ · إتمامٌ · عودةٌ كانونيّةٌ) — والثانيةُ
    # تُعلَنُ إعادتَينِ على عبورَيِ البدءِ والإتمامِ (لا رابعَ: العودةُ الكانونيّةُ
    # عمليّةٌ فارغةٌ لا تُقاسُ — سابقةُ `set_lifecycle_state`).
    assert recorder.results[3].is_replay is True, "عبورُ البدءِ الثاني لم يُعلَنْ إعادةً"
    assert recorder.results[4].is_replay is True, "عبورُ الإتمامِ الثاني لم يُعلَنْ إعادةً"
    assert len(recorder.results) == 5
    from amos_federation.common.database import get_session_factory
    from amos_federation.services.agent_runtime.health import TreatmentRecordModel

    session = get_session_factory()()
    try:
        count = (
            session.query(TreatmentRecordModel)
            .filter(TreatmentRecordModel.id == "w699-replay-t1")
            .count()
        )
        assert count == 1, f"سجلُّ العلاجِ تكرَّرَ ({count})"
    finally:
        session.close()


def test_w699_4_update_state_replay_and_later_operation() -> None:
    """إعادةُ التحديثِ بذاتِ الحمولةِ إعادةٌ واحدةٌ، وحالةٌ جديدةٌ عمليّةٌ لاحقةٌ."""
    registry = PopulationRegistry()
    registry.register_agent(
        "وكيل إعادة", "executor", "cognitive_executor", agent_id="w699-replay-upd"
    )
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    registry.update_state("w699-replay-upd", "paused", authorizer=recorder)
    # العبورُ الأخيرُ هو المرآةُ — إعادةُ الإرسالِ بذاتِ الحمولةِ إعادةٌ واحدةٌ.
    mirror_keys = [
        r.outcome.operation_key
        for r in recorder.results
        if "agents.population.state" in r.outcome.operation_key
    ]
    assert len(mirror_keys) == 1

    # إعادةُ الإرسالِ بذاتِ الحمولةِ عمليّةٌ فارغةٌ لا تُقاسُ (سابقةُ
    # `set_lifecycle_state` · تصميمُ E1 § 2.4): لا عبورَ جديدَ ولا كتابةً ثانيةً.
    before = len(recorder.results)
    registry.update_state("w699-replay-upd", "paused", authorizer=recorder)
    assert len(recorder.results) == before, "الإعادةُ عبرتْ عبورًا جديدًا"

    registry.update_state("w699-replay-upd", "active", authorizer=recorder)
    assert recorder.results[-1].is_replay is False, "التحديثُ المختلفُ رُفضَ كإعادةٍ"


def test_w699_4_start_treatment_replay_executes_once() -> None:
    """إعادةُ إرسالِ العلاجِ المُتِمِّ لا تُعيدُ تنفيذَهُ — والمعرِّفُ الجديدُ ينفَّذُ.

    التنفيذُ يقعُ خارجَ العبورِ (جلسةٌ لاحقةٌ مستقلةٌ)، فلولا قراءةُ الحقلِ
    الدائمِ قبلَ التنفيذِ لإعادةتُ الإرسالِ المُتِمِّ تنفيذَهُ ثانيةً — وهنا
    يُقاسُ ذلكَ عدًّا: نفسُ المعرفِ مرتينِ تنفيذٌ واحدٌ، ومعرِّفٌ جديدٌ تنفيذٌ
    جديدٌ (تصميمُ E1 § 2.4: العمليةُ الفارغةُ لا تُعيدُ ما وقعَ).
    """
    _spawn("w699-exec-treat")
    system = get_treatment_system()
    calls = {"n": 0}
    real_execute = system._execute_treatment

    def _counting(agent_id: str, treatment_type: str) -> Any:
        calls["n"] += 1
        return real_execute(agent_id, treatment_type)

    system._execute_treatment = _counting  # type: ignore[method-assign]
    try:
        system.start_treatment(
            "w699-exec-treat",
            "reset_context",
            "اختبار",
            treatment_id="w699-exec-t1",
            authorizer=RecordingAuthorizer(actor="EXECUTIVE"),
        )
        assert calls["n"] == 1
        # إعادةُ الإرسالِ بذاتِ المعرفِ: العلاجُ مُتِمٌّ في الحقلِ الدائمِ —
        # لا تنفيذَ ثانيًا (تُعادُ نتيجتُهُ المخزَّنةُ لا فعلُهُ).
        system.start_treatment(
            "w699-exec-treat",
            "reset_context",
            "اختبار",
            treatment_id="w699-exec-t1",
            authorizer=RecordingAuthorizer(actor="EXECUTIVE"),
        )
        assert calls["n"] == 1, "إعادةُ الإرسالِ أعادتِ التنفيذَ"
        # معرِّفٌ جديدٌ على الوكيلِ نفسِهِ: علاجٌ جديدٌ عمليةٌ جديدةٌ بمفتاحٍ
        # جديدٍ (تصميمُ E1 § 2.4: «عمليةٌ جديدةٌ على الكيانِ نفسِهِ ⇒ مفتاحٌ
        # جديدٌ») — يُنشئُ العلاجَ ويُكمِلُ دورتَهُ حتى النهايةِ فالتنفيذُ اثنانِ.
        system.start_treatment(
            "w699-exec-treat",
            "reset_context",
            "اختبار",
            treatment_id="w699-exec-t2",
            authorizer=RecordingAuthorizer(actor="EXECUTIVE"),
        )
        assert calls["n"] == 2, "المعرِّفُ الجديدُ لم يُنفَّذْ"
    finally:
        system._execute_treatment = real_execute  # type: ignore[method-assign]


def test_w699_4_update_state_mirror_failure_compensates_canonical() -> None:
    """فشلُ عبورِ المرآةِ بعدَ نجاحِ الكانونيِّ يعوِّضُ الأثرَينِ ثمَّ تقبلُ الإعادةَ.

    عبورُ المرآةِ آخرُ عبورَيِ العمليةِ، فإذا انكسرَ كاتبُها **بعدَ أن كتبَ
    فعلًا** (لا قبلَ الكتابةِ) وجبَ أن يعوِّضَ معوِّضُهُ المنسَّقُ الأثرَينِ:
    إرجاعُ صفِّ السكّانِ **وعكسُ الانتقالِ الكانونيِّ الذي نجحَ قبلَهُ** — وإلا
    بقيَ الكانونُ قد انتقلَ والعمليةُ كلُّها فاشلةٌ (تعويضٌ منسَّقٌ · تصميمُ E1
    § 2.3). وبعدَ التعويضِ الكاملِ: إعادةُ الطلبِ نفسِهِ بالسجلِّ نفسِهِ — بلا
    تصفيرِ الذرّيّةِ — محاولةٌ جديدةٌ (هويّةُ العمليةِ المركَّبةِ تُرقّمُ
    المحاولةَ الفاشلةَ القابلةَ للإعادةِ فمفتاحُها جديدٌ) تنجحُ وتُتمُّ
    الانتقالَ في الحقلينِ معًا: فالتعويضُ أعادَ الحالةَ الكانونيّةَ، وعبورُ
    المرآةِ الفاشلُ بقيَ مسجَّلًا فاشلًا قابلًا للإعادةِ — لا يُعادُ إنتاجُ
    تضاربِ الذرّيّةِ (IdentityLedgerDivergenceError) على عبورٍ نجحَ وعُوّضَ.
    """
    registry = PopulationRegistry()
    registry.register_agent(
        "وكيل تعويض", "executor", "cognitive_executor", agent_id="w699-comp-mirror"
    )
    recorder = RecordingAuthorizer(actor="EXECUTIVE")
    # الحالةُ الأوليّةُ: مسجَّلٌ في المرآةِ والكانونِ على «registered».
    registry.update_state("w699-comp-mirror", "paused", authorizer=recorder)

    from amos_federation.services.agent_runtime import population as population_mod
    from amos_federation.services.executive_core.agent_identity import require_identity

    original = population_mod._update_population_row_core

    def _poisoned(*args: Any, **kwargs: Any) -> None:
        # الكاتبُ المسمومُ يستدعي الكاتبَ الأصليَّ فعلًا (الكتابةُ تقعُ) ثمَّ
        # يرفعُ الانكسارَ **بعدَ الكتابةِ الفعليةِ** — فالأثرُ واقعٌ والتعويضُ
        # واجبٌ لا رفضٌ نظيفٌ بلا أثرٍ.
        original(*args, **kwargs)
        raise RuntimeError("انكسارٌ مُفتعَلٌ بعدَ كتابةِ المرآةِ")

    population_mod._update_population_row_core = _poisoned
    try:
        with pytest.raises(_idempotency_error()):
            registry.update_state("w699-comp-mirror", "active", authorizer=recorder)
    finally:
        population_mod._update_population_row_core = original

    # المرآةُ عُوّضَتْ: كتبَها السمُّ إلى «active» ثمَّ أعادها المعوّضُ إلى
    # «paused» (يُقرأُ صفُّ السكّانِ نفسُهُ لا إسقاطَ get_agent الذي يشتقُّ
    # الحالةَ منَ الكانونيِّ).
    from amos_federation.common.database import get_session_factory
    from amos_federation.services.agent_runtime.population import AgentPopulationModel

    def _mirror_row_state() -> str | None:
        session = get_session_factory()()
        try:
            row = (
                session.query(AgentPopulationModel)
                .filter(AgentPopulationModel.agent_id == "w699-comp-mirror")
                .one_or_none()
            )
            return row.state if row is not None else None
        finally:
            session.close()

    assert _mirror_row_state() == "paused", "صفُّ السكّانِ لم يُستعَدْ بعدَ فشلِ المرآةِ"
    # والكانونُ عُكِسَ انتقالُهُ الناجحُ إلى «active» — عادَ إلى «paused».
    assert (
        require_identity("w699-comp-mirror").lifecycle_state == "paused"
    ), "الانتقالُ الكانونيُّ الناجحُ لم يُعوَّضْ بعدَ فشلِ المرآةِ"

    # إعادةُ الطلبِ نفسِهِ بالسجلِّ نفسِهِ بعدَ زوالِ العطلِ: محاولةٌ جديدةٌ
    # بمفتاحٍ جديدٍ (المرآةُ الفاشلةُ القابلةُ للإعادةِ تُرقّمُ المحاولةَ) —
    # تنجحُ وتُتمُّ الانتقالَ في الحقلينِ معًا.
    # فاصلُ ثانيةٍ قبلَ الإعادةِ — لا تفضيلًا بل قيدًا مقرَّرًا (Q-11 · قرارُ
    # المالكِ 2026-08-19 الخيارُ 2): هويّةُ الإذنِ السياديِّ دقّتُها ثانيةٌ واحدةٌ،
    # فإعادةُ المحاولةِ على العقدِ نفسِهِ في الثانيةِ نفسِها تُرفَضُ عمدًا —
    # «حمايةٌ من الأثرِ المزدوجِ مدّتُها ثانيةٌ واحدةٌ لا ضمانٌ من المفتاحِ»
    # (سجلُّ القراراتِ السياديّةِ § Q-11). الإعادةُ بعدَ الثانيةِ تمرُّ منَ
    # المسارِ المُصمَّمِ: المفتاحُ نفسُهُ (1H يُعيدُ المحاولةَ الفاشلةَ القابلةَ
    # للإعادةِ) والمفتاحُ الكانونيُّ جديدٌ (§ 2.4: محاولةٌ جديدةٌ بعدَ تعويضٍ
    # كاملٍ — لا يُعادُ إنتاجُ تضاربِ الذرّيّةِ).
    import time

    time.sleep(1.2)

    assert (
        registry.update_state("w699-comp-mirror", "active", authorizer=recorder) is True
    ), "إعادةُ الطلبِ بعدَ التعويضِ لم تنجحْ"
    assert _mirror_row_state() == "active", "صفُّ السكّانِ لم يُكتَبْ بعدَ نجاحِ الإعادةِ"
    assert (
        require_identity("w699-comp-mirror").lifecycle_state == "active"
    ), "الحقلُ الكانونيُّ لم ينتقلْ بعدَ نجاحِ الإعادةِ"


def test_w699_4_register_agent_second_effect_failure_restores_first() -> None:
    """فشلُ الأثرِ الثاني في العبورِ المركَّبِ يعوِّضُ الأثرَ الأولَ (spawn_agent).

    إنشاءُ الهويّةِ وإنشاءُ صفِّ الملفِّ أثرانِ في عبورٍ واحدٍ (تصميمُ E1
    § 2.3) — إذا انكسرَ كاتبُ صفِّ الملفِّ بعدَ أن كُتِبَ صفُّ الهويّةِ وجبَ أن
    يحذفَ المعوِّضُ صفَّ الهويّةِ: لا يبقى أثرٌ نصفُ مكتوبٍ لعمليةٍ فاشلةٍ.
    """
    registry = PopulationRegistry()
    from amos_federation.services.agent_runtime import population as population_mod
    from amos_federation.services.executive_core.agent_identity import get_identity

    original = population_mod._create_population_profile_core

    def _poisoned(*args: Any, **kwargs: Any) -> None:
        raise RuntimeError("انكسارٌ مُفتعَلٌ في كاتبِ صفِّ الملفِّ")

    population_mod._create_population_profile_core = _poisoned
    try:
        with pytest.raises(_compensation_required()):
            registry.register_agent(
                "وكيل فاشل", "executor", "cognitive_executor", agent_id="w699-comp-reg"
            )
    finally:
        population_mod._create_population_profile_core = original

    # أثرُ الأثرِ الأولِ (صفُّ الهويّةِ الكانونيّةِ) عُوِّضَ: لا هويةَ نصفَ مسجَّلةٍ.
    assert get_identity("w699-comp-reg") is None, "صفُّ الهويّةِ لم يُحذَفْ بعدَ فشلِ الأثرِ الثاني"
    assert registry.get_agent("w699-comp-reg") is None, "صفُّ الملفِّ كُتِبَ رغمَ فشلِ كاتبِهِ"


# ── الصنفُ 5 · كاشفُ التعشيشِ ────────────────────────────────────────────────


def test_w699_5_nested_crossing_is_refused() -> None:
    """عبورٌ داخلَ مُطبِّقِ عبورٍ يرتفعُ NestedSovereignCallError صريحًا."""
    from core.sovereignty.enforcement_boundary import NestedSovereignCallError
    from core.sovereignty.idempotency import IdempotencyError

    _spawn("w699-nested")
    checker = get_health_checker_for_test()
    authorizer = ConstitutionalAuthorizer(actor="EXECUTIVE")
    from amos_federation.services.agent_runtime.health import declared_effect, operation_key

    target = "health_check:w699-nested"
    effect = declared_effect("CREATE", f"{target}/nested-1", "فحصٌ من داخلِ مُطبِّقٍ")

    def _nested_apply(_effect: Any) -> None:
        checker.check_agent("w699-nested", check_id="w699-nested-1")

    # الكاشفُ يُطلقُ الخطأَ الصريحَ داخلَ إطارِ الذرّيّةِ فيصلَ ملفوفًا بهِ
    # (`IdempotencyError` سببُهُ `NestedSovereignCallError`) — والسببُ هو المعلومُ.
    with pytest.raises(IdempotencyError) as excinfo:
        authorizer.guard_declared(
            ACTION_RUN_HEALTH_CHECK,
            target,
            declared_effects=(effect,),
            applier=_nested_apply,
            operation_key=operation_key("agents.health.check", "w699-nested/nested-1"),
            compensators=(
                compensator(
                    effect.signature,
                    lambda: None,
                    "معوّضُ اختبارٍ — الأثرُ لا يقعُ أصلًا وراءَ كاشفِ التعشيشِ",
                ),
            ),
        )
    assert isinstance(excinfo.value.__cause__, NestedSovereignCallError)


# ── الصنفُ 3 · طفرةٌ واحدةٌ لكلِّ سطحٍ منَ الـ14 (تنفيذٌ فعليٌّ مسجَّلُ النتائجِ) ──


class _NoEvidence:
    """دليلٌ زائفٌ للطفرةِ: لا فعلَ ولا قرارَ ولا بصمةَ سجلٍّ — ففحوصُ الصنفِ 2
    تفشلُ على ادّعاءِ الدليلِ الحرفيِّ لا على انكسارٍ عارضٍ."""

    def as_dict(self) -> dict[str, Any]:
        return {"action": None, "decision": None, "ledger_entry_hash": "", "target": None}


def _mutate_guard_for(verb: str) -> Callable[[], None]:
    """نزعُ الحارسِ عن فعلٍ واحدٍ: المُطبِّقُ يُنفَّذُ فعلًا ولا يُسجَّلُ شيءٌ.

    بقيةُ الأفعالِ تعبرُ الحدَّ الحقيقيَّ كما هي — فالطفرةُ موضعيّةٌ لا عالميّةٌ.
    """
    original = ConstitutionalAuthorizer.guard_declared

    def bypass(self: Any, action: str, *args: Any, **kwargs: Any) -> Any:
        if action != verb:
            return original(self, action, *args, **kwargs)
        declared_effects = kwargs.get("declared_effects") or (args[0] if args else ())
        applier = kwargs.get("applier")
        # قيمةُ المُنادي تُلتقَط منَ المُطبِّقِ نفسِهِ (عقدُ الجسرِ: «الحدُّ لا
        # يُرجِعُها») — فالطفرةُ أمينةٌ لعقدِ القيمةِ ولا تُكسِرُ إلا الدليلَ:
        # لا فعلًا ولا قرارَ ولا بصمةَ سجلٍّ (هذا هوَ المنزوعُ وحدَهُ).
        captured = [applier(effect) for effect in declared_effects]
        return GuardedResult(
            value=captured[0] if len(captured) == 1 else tuple(captured),
            evidence=_NoEvidence(),
            outcome=SimpleNamespace(is_replay=False, operation_key=None),
        )

    ConstitutionalAuthorizer.guard_declared = bypass  # type: ignore[method-assign]

    def restore() -> None:
        ConstitutionalAuthorizer.guard_declared = original  # type: ignore[method-assign]

    return restore


# سجلُّ نتائجِ الطفرةِ المهيكلُ لكلِّ حالةٍ — يُجمَعُ هنا ليُصدَّرَ حِملًا
# موثّقًا (المادةُ التاسعةُ) عبرَ سكربتِ توليدِ الحملةِ لا نصًّا خامًا.
_MUTATION_CASE_RECORDS: list[dict[str, Any]] = []

#: علاماتُ سطرِ تأكيدِ الدليلِ — الفشلُ لا يُحتسبُ قتلًا للطفرةِ إلا إذا وقعَ
#: على تأكيدِ الدليلِ تحديدًا (استخراجِهِ أو مساواتِهِ الحرفيةِ أو بصمةِ العبورِ).
_EVIDENCE_ASSERTION_MARKERS = (
    "evidence",
    "is_replay",
    "ledger_entry_hash",
    "recorder.results",
    "operation_key",
)


def _deepest_test_module_frame(exc: BaseException) -> tuple[str, int, str] | None:
    """أعمقُ إطارٍ في ملفاتِ الفحوصِ — يُقرأُ سطرُهُ ليُتحقَّقَ من موضعِ الفشلِ."""
    frame = exc.__traceback__
    found: tuple[str, int, str] | None = None
    while frame is not None:
        filename = frame.tb_frame.f_code.co_filename
        if filename.endswith("test_w699_agent_runtime_crossing.py") or filename.endswith(
            "test_e1_executive_identity_crossing.py"
        ):
            line = linecache.getline(filename, frame.tb_lineno).strip()
            found = (filename, frame.tb_lineno, line)
        frame = frame.tb_next
    return found


def _run_expecting_failure(test_function: Callable[[], None], verb: str) -> dict[str, Any]:
    """تشغيلُ فحصِ الصنفِ 2 تحتَ الطفرةِ — يجبُ أن يفشلَ على الدليلِ لا على انكسارٍ.

    خطُّ الأساسِ أولًا: الفحصُ نفسُهُ ينجحُ بلا طفرةٍ (وإلا فالفشلُ لا يُعزى
    للطفرةِ)، ثمَّ تحتَ الطفرةِ يجبُ أن يفشلَ الفحصُ **على تأكيدِ الدليلِ
    تحديدًا** — يُقرأُ أعمقُ سطرٍ في ملفِّ الفحصِ منَ الأثرِ، ولا يُحتسبُ قتلًا
    للطفرةِ إلا إذا كانَ سطرَ دليلٍ (استخراجُ الدليلِ أو مساواتُهُ الحرفيّةُ أو
    بصمةُ العبورِ)؛ فشلٌ في غيرِ الدليلِ يُسجَّلُ ولا يُعتدُّ بهِ. يعيدُ سجلَّ
    الحالةِ المهيكلَ (نجاحُ الفحصِ تحتَ الطفرةِ = فشلُ الفحصِ نفسِهِ).
    """
    from tests.conftest import _fresh_test_idempotency_ledger

    # 1) خطُّ الأساسِ بلا طفرةٍ: نجاحٌ نظيفٌ يُثبِتُ أنَّ أيَّ فشلٍ لاحقًا سببُهُ الطفرةُ.
    _reset_runtime_tables()
    _fresh_test_idempotency_ledger()
    test_function()

    # 2) تحتَ الطفرةِ — حالةٌ نظيفةٌ لكلِّ حالةٍ: القاعدةُ والسجلُّ يُستبدلانِ
    # كما يفعلُ التجهيزُ التلقائيُّ لكلِّ فحصٍ (قرارُ المالكِ Q-71).
    _reset_runtime_tables()
    _fresh_test_idempotency_ledger()
    restore = _mutate_guard_for(verb)
    try:
        test_function()
    except (AssertionError, KeyError, IndexError) as exc:
        frame_info = _deepest_test_module_frame(exc)
        assertion_line = frame_info[2] if frame_info is not None else ""
        on_evidence = any(marker in assertion_line for marker in _EVIDENCE_ASSERTION_MARKERS)
        record = {
            "verb": verb,
            "test": test_function.__name__,
            "baseline_without_mutation": "passed",
            "mutant_outcome": "failed_on_evidence" if on_evidence else "failed_not_on_evidence",
            "failing_assertion": assertion_line[:200],
            "failure": f"{type(exc).__name__}: {str(exc)[:200]}",
        }
        _MUTATION_CASE_RECORDS.append(record)
        _dump_mutation_records_if_requested()
        return record
    except Exception as exc:  # noqa: BLE001 — يُسجَّلُ ولا يُبتلَعُ
        record = {
            "verb": verb,
            "test": test_function.__name__,
            "baseline_without_mutation": "passed",
            "mutant_outcome": "failed_other_exception",
            "failing_assertion": "",
            "failure": f"{type(exc).__name__}: {str(exc)[:200]}",
        }
        _MUTATION_CASE_RECORDS.append(record)
        _dump_mutation_records_if_requested()
        return record
    else:
        pytest.fail(f"الطفرةُ لم تُسقِطِ الفحصَ: {test_function.__name__} تحتَ نزعِ حارسِ «{verb}»")
        raise AssertionError("unreachable")
    finally:
        restore()


def _dump_mutation_records_if_requested() -> None:
    """تصديرُ سجلِّ الحالاتِ المهيكلِ حِملًا موثّقًا عندَ الطلبِ (سكربتُ توليدِ
    حملةِ الطفرةِ يضبطُ `AMOS_W699_MUTATION_DUMP` ثمَّ يشغِّلُ pytest)."""
    path = os.environ.get("AMOS_W699_MUTATION_DUMP")
    if not path:
        return
    payload = {
        "$comment": (
            "حملةُ طفرةِ أسطحِ W-699/E1: لكلِّ فعلٍ مُستهدَفٍ خطُّ أساسٍ ناجحٌ بلا "
            "طفرةٍ ثمَّ فشلٌ على تأكيدِ الدليلِ تحديدًا تحتَ نزعِ الحارسِ — لا فشلًا "
            "عارضًا يُحتسبُ قتلًا (المادةُ التاسعةُ · W-699)"
        ),
        "cases": list(_MUTATION_CASE_RECORDS),
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)


def test_w699_3_guard_removal_drops_each_agent_runtime_test() -> None:
    """نزعُ الحارسِ عن كلِّ سطحٍ منَ أسطحِ agent_runtime الثمانيةِ يُسقِطُ فحصَهُ."""

    def _check_agent_case() -> None:
        test_w699_2_check_agent_crosses_run_health_check()

    def _start_treatment_case() -> None:
        test_w699_2_start_treatment_crosses_with_two_sessions()

    def _isolate_case() -> None:
        test_w699_2_isolate_crosses_with_two_declared_effects()

    def _log_action_case() -> None:
        test_w699_2_log_action_crosses_log_isolated_action()

    def _release_case() -> None:
        test_w699_2_release_crosses_and_guards_direction_prechecked()

    def _register_agent_case() -> None:
        test_w699_2_population_register_agent_crosses_spawn()

    def _update_state_case() -> None:
        test_w699_2_update_state_crosses_population_mirror()

    def _take_step_case() -> None:
        test_w699_2_take_step_crosses_record_curriculum_step()

    results = [
        _run_expecting_failure(_check_agent_case, ACTION_RUN_HEALTH_CHECK),
        _run_expecting_failure(_start_treatment_case, ACTION_START_AGENT_TREATMENT),
        _run_expecting_failure(_isolate_case, ACTION_ISOLATE_AGENT),
        _run_expecting_failure(_log_action_case, ACTION_LOG_ISOLATED_ACTION),
        _run_expecting_failure(_release_case, ACTION_RELEASE_AGENT),
        _run_expecting_failure(_register_agent_case, "spawn_agent"),
        _run_expecting_failure(_update_state_case, ACTION_UPDATE_POPULATION_STATE),
        _run_expecting_failure(_take_step_case, ACTION_RECORD_CURRICULUM_STEP),
    ]
    # كلُّ الطفراتِ أَسقطَتْ فحوصَها على الدليلِ — لا انكسارًا عارضًا ولا نجاحًا زائفًا.
    for record in results:
        assert record["mutant_outcome"] == "failed_on_evidence", record
    assert len(results) == 8
    _dump_mutation_records_if_requested()


def test_w699_3_guard_removal_drops_each_executive_core_test() -> None:
    """نزعُ الحارسِ عن كلِّ سطحٍ منَ أسطحِ executive_core الستةِ يُسقِطُ فحصَهُ.

    أسطحُ W-696 الستةُ (تصميمُ E1 § 2.2 — الوجيزةُ الأولى) تُطفَّرُ هنا بنمطِ
    W-699 نفسِهِ: فحوصُ الصنفِ 2 منَ الملفِّ المعتمدِ تُشغَّلُ تحتَ نزعِ حارسِ
    كلِّ فعلٍ على حدةٍ، ويجبُ أن تفشلَ على الدليلِ الحرفيِّ.
    """
    from tests.test_e1_executive_identity_crossing import (
        test_e1_5_update_identity_crosses_with_literal_evidence,
        test_e1_6_lifecycle_crosses_by_direction,
        test_e1_7_dispatcher_register_agent_crosses_spawn,
        test_e1_8_task_surfaces_cross_with_literal_evidence,
    )

    results = [
        _run_expecting_failure(
            test_e1_5_update_identity_crosses_with_literal_evidence,
            "update_agent_identity",
        ),
        _run_expecting_failure(test_e1_6_lifecycle_crosses_by_direction, "contain_agent"),
        _run_expecting_failure(test_e1_6_lifecycle_crosses_by_direction, "activate_agent"),
        _run_expecting_failure(test_e1_7_dispatcher_register_agent_crosses_spawn, "spawn_agent"),
        _run_expecting_failure(test_e1_8_task_surfaces_cross_with_literal_evidence, "create_task"),
        _run_expecting_failure(test_e1_8_task_surfaces_cross_with_literal_evidence, "delete_task"),
        _run_expecting_failure(
            test_e1_8_task_surfaces_cross_with_literal_evidence, "transition_task_state"
        ),
    ]
    for record in results:
        assert record["mutant_outcome"] == "failed_on_evidence", record
    assert len(results) == 7
    _dump_mutation_records_if_requested()


def get_health_checker_for_test() -> Any:
    """فاحصٌ نظيفٌ لكلِّ حالةٍ — لا حالةَ مشتركةً بينَ الفحوصِ."""
    from amos_federation.services.agent_runtime.health import HealthChecker

    return HealthChecker()


# ═════════════════════════════════════════════════════════════════════════════
# الفئةُ الخامسةُ · فروعُ الرفضِ والمساراتُ الجانبيةُ — استكمالُ ما كشفَهُ حرسُ
# تغطيةِ الفروعِ في CI (≥80%) بعدَ جولةِ التحققِ: فروعُ الرفضِ النظيفِ (الوكلاءُ
# المفقودونَ والقراراتُ الحرةُ والخطواتُ خارجَ المنهجِ)، ومساراتُ الإعادةِ
# والتعويضِ الجزئيُّ في الأسطحِ الثمانيةِ — تُقاسُ لا تُفترَضُ.
# ═════════════════════════════════════════════════════════════════════════════


def test_w699_5_take_step_rejects_steps_outside_curriculum() -> None:
    """الخطوةُ خارجَ حدودِ المنهجِ (1..6) رفضٌ نظيفٌ بلا عبورٍ ولا كتابةٍ."""
    school = AgentSchool()

    below = school.take_step("w699-5-range", 0, 90)
    above = school.take_step("w699-5-range", 7, 90)

    assert below == {"error": "step_out_of_range"}
    assert above == {"error": "step_out_of_range"}


def test_w699_5_register_agent_rejects_existing_identity() -> None:
    """تكرارُ التسجيلِ بالمعرّفِ نفسِهِ رفضٌ مبكّرٌ صريحٌ قبلَ أيِّ كتابةٍ."""
    from amos_federation.services.executive_core.agent_identity import (
        DuplicateAgentIdentityError,
    )

    registry = PopulationRegistry()
    registry.register_agent("وكيل مكرر", "executor", "cognitive_executor", agent_id="w699-5-dup")

    with pytest.raises(DuplicateAgentIdentityError):
        registry.register_agent("وكيل آخر", "executor", "cognitive_executor", agent_id="w699-5-dup")


def test_w699_5_update_state_on_identity_without_population_row() -> None:
    """تحديثُ حالةِ وكيلٍ له هويةٌ كانونيةٌ ولا صفَّ سكّانٍ: الكانونيُّ ينتقلُ
    وكاتبُ المرآةِ لا شيءَ يكتبُهُ (لا صفَّ) فلا يُنشئُ صفًّا ولا يفشلُ."""
    _spawn("w699-5-no-pop")
    registry = PopulationRegistry()

    assert registry.update_state("w699-5-no-pop", "paused") is True

    assert registry._profile("w699-5-no-pop") is None, "صفُّ سكّانٍ أُنشئ بلا تسجيل"
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("w699-5-no-pop").lifecycle_state == "paused"


def test_w699_5_update_state_ignores_extra_without_matching_attribute() -> None:
    """الحقولُ الزائدةُ في «extra» التي لا عمودَ لها في صفِّ السكّانِ تُتجاهَلُ
    ولا تفشلُ العمليةَ — فالعمليةُ تُكملُ بمرورِها على ما يعرفُهُ الصفُّ."""
    registry = PopulationRegistry()
    registry.register_agent("وكيل حقول", "executor", "cognitive_executor", agent_id="w699-5-extra")

    result = registry.update_state(
        "w699-5-extra",
        "paused",
        authorizer=RecordingAuthorizer(actor="EXECUTIVE"),
        **{"حقل_غير_موجود": "قيمة"},
    )

    assert result is True


def test_w699_5_mirror_failure_on_identity_without_population_row() -> None:
    """فشلُ عبورِ المرآةِ على وكيلٍ بلا صفِّ سكّانٍ: لا لقطةَ تُستعادُ (لا صفَّ)
    والكانونيُّ الذي نجحَ قبلَهُ يُعكَسُ — ثم يُعادُ رفعُ الانكسارِ كما هو."""
    _spawn("w699-5-no-pop-mirror")
    from amos_federation.services.agent_runtime import population as population_mod

    original = population_mod._update_population_row_core

    def _poisoned(*args: Any, **kwargs: Any) -> None:
        original(*args, **kwargs)
        raise RuntimeError("انكسارٌ مُفتعَلٌ بعدَ كتابةِ المرآةِ")

    registry = PopulationRegistry()
    population_mod._update_population_row_core = _poisoned
    try:
        with pytest.raises(_idempotency_error()):
            registry.update_state("w699-5-no-pop-mirror", "paused")
    finally:
        population_mod._update_population_row_core = original

    # الكانونيُّ عُوِّضَ رجوعًا إلى حالِهِ قبلَ العبورِ الفاشلِ.
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("w699-5-no-pop-mirror").lifecycle_state == "active"


def test_w699_5_mirror_failure_with_unchanged_target_skips_canonical_restore() -> None:
    """فشلُ عبورِ المرآةِ والحالةُ الكانونيةُ مساويةٌ للهدفِ: عكسُ الانتقالِ
    الكانونيِّ يُتخطّى (لا انتقالَ وقعَ) ولقطةُ صفِّ السكّانِ وحدها تُستعادُ."""
    registry = PopulationRegistry()
    registry.register_agent(
        "وكيل هدف ثابت", "executor", "cognitive_executor", agent_id="w699-5-same"
    )
    registry.update_state("w699-5-same", "paused")
    from amos_federation.services.agent_runtime import population as population_mod

    original = population_mod._update_population_row_core

    def _poisoned(*args: Any, **kwargs: Any) -> None:
        original(*args, **kwargs)
        raise RuntimeError("انكسارٌ مُفتعَلٌ بعدَ كتابةِ المرآةِ")

    population_mod._update_population_row_core = _poisoned
    try:
        with pytest.raises(_idempotency_error()):
            # الحمولةُ تتغيّرُ (الاسمُ) فالعمليةُ ليست «مُطبَّقةً فعلًا»،
            # والحالةُ الكانونيةُ «paused» مساويةٌ للهدفِ «paused».
            registry.update_state("w699-5-same", "paused", name="اسم جديد بعد الفشل")
    finally:
        population_mod._update_population_row_core = original

    # الكانونيُّ بقيَ على «paused» (لم يُعكَسْ إلى ما قبلَهُ — لا انتقالَ وقعَ)
    # وصفُّ السكّانِ استُعيدَ بلقطةِ الاسمِ الأصليِّ.
    from amos_federation.services.executive_core.agent_identity import require_identity

    assert require_identity("w699-5-same").lifecycle_state == "paused"
    assert registry._profile("w699-5-same").name == "وكيل هدف ثابت"


def test_w699_5_set_lifecycle_state_replay_returns_true() -> None:
    """إعادةُ الإرسالِ بالمفتاحِ نفسِهِ (انتقالُ الحالةِ إلى حالِها) إعادةٌ
    نظيفةٌ: لا عبورَ جديدَ ولا كتابةٌ — النتيجةُ المخزّنةُ تُعادُ."""
    _spawn("w699-5-replay")

    first = set_lifecycle_state("w699-5-replay", "active", operation_id="w699-5-rep-1")
    second = set_lifecycle_state("w699-5-replay", "active", operation_id="w699-5-rep-1")

    assert first is True
    assert second is True


def test_w699_5_set_lifecycle_state_replay_detects_divergence() -> None:
    """إعادةُ المفتاحِ نفسِهِ بعدَ رجّعِ الحالةِ يدويًّا (لا عبورَ) تضاربٌ
    مقيسٌ: السجلُّ يقولُ «تمّ» والكانونُ يقولُ غيرَ ذلكَ — رفضٌ صريحٌ."""
    from amos_federation.services.executive_core.agent_identity import (
        IdentityLedgerDivergenceError,
        _set_lifecycle_state_core,
    )

    _spawn("w699-5-div")
    set_lifecycle_state("w699-5-div", "paused", operation_id="w699-5-div-1")
    # سُمَّ الكانونَ: رجّعَ الحالةَ بلا عبورٍ — المفتاحُ نفسُهُ سيُعادُ.
    _set_lifecycle_state_core("w699-5-div", "active")

    with pytest.raises(IdentityLedgerDivergenceError):
        set_lifecycle_state("w699-5-div", "paused", operation_id="w699-5-div-1")


def test_w699_5_set_lifecycle_state_core_unknown_agent_returns_false() -> None:
    """الكتابةُ الكانونيةُ الصافيةُ على وكيلٍ لا هويةَ لهُ رفضٌ هادئٌ: False."""
    from amos_federation.services.executive_core.agent_identity import (
        _set_lifecycle_state_core,
    )

    assert _set_lifecycle_state_core("w699-5-unknown", "paused") is False


def test_w699_5_clean_rejections_of_missing_entities() -> None:
    """الرفضُ النظيفُ قبلَ أيِّ كتابةٍ: علاجُ وكيلٍ مفقودٍ، وعزلُ وكيلٍ مفقودٍ،
    وتسجيلُ فعلٍ على سجلِّ عزلٍ غيرِ موجودٍ، ورفعُ عزلٍ غيرِ موجودٍ أو بقرارٍ
    حرٍّ غيرِ موجَّهٍ."""
    treatment = get_treatment_system()
    isolation = get_isolation_system()

    with pytest.raises(ValueError):
        treatment.start_treatment("w699-5-missing", "retrain", "اختبار الرفض")
    with pytest.raises(ValueError):
        isolation.isolate("w699-5-missing", reason="اختبار الرفض")
    with pytest.raises(ValueError):
        isolation.log_action("w699-5-no-isolation", "فحص", {})
    with pytest.raises(ValueError):
        isolation.release("w699-5-no-isolation", decision="retire")

    _spawn("w699-5-rel")
    record = isolation.isolate("w699-5-rel", reason="اختبار القرار الحر")
    with pytest.raises(ValueError):
        isolation.release(record["isolation_id"], decision="نص حر غير موجّه")


def test_w699_5_release_retrain_skips_lifecycle_effect() -> None:
    """رفعُ العزلِ بقرارِ «retrain» لا يعلنُ أثرَ انتقالِ دورةِ حياةٍ (لا
    استعادةَ قدرةٍ) — أثرُ سجلِّ العزلِ وحدهُ يُعلَنُ ويُطبَّقُ."""
    _spawn("w699-5-ret")
    isolation = get_isolation_system()
    isolation.isolate("w699-5-ret", reason="اختبار", isolation_id="w699-5-ret-1")
    recorder = RecordingAuthorizer(actor="EXECUTIVE")

    isolation.release("w699-5-ret-1", "retrain", authorizer=recorder)

    row = _isolation_row("w699-5-ret-1")
    assert row is not None and row.status == "retrain"
    from amos_federation.services.executive_core.agent_identity import require_identity

    # عبورُ الرفعِ نفسُهُ لا يُعلنُ أثرَ انتقالِ (لا «activate» من هذا الطريقِ):
    # العودةُ إلى «active» وقعتَ في عبورِ العلاجِ اللاحقِ لا في عبورِ الرفعِ.
    assert require_identity("w699-5-ret").lifecycle_state == "active"


def _w699_5_experience(agent_id: str, quality: float, success: bool) -> None:
    """خبرةٌ مصنوعةٌ لقياسِ تصنيفِ الفحصِ — لا افتراضَ بلا قياسٍ."""
    from amos_federation.common.persistent import PersistentExperienceStore

    PersistentExperienceStore().record(
        {
            "experience_id": f"w699-5-exp-{agent_id}-{quality}",
            "agent_id": agent_id,
            "type": "success" if success else "failure",
            "quality_score": quality,
            "outcome": {"success": success},
        }
    )


def _w699_5_reset_global_stores() -> None:
    """تصفيرُ المخازنِ العالميةِ (التدقيقِ والخبراتِ) — قياسٌ محكمٌ على سجلٍّ
    يملؤهُ الفحصُ نفسُهُ لا على بقايا فحوصٍ سابقةٍ في الجلسةِ (سجلُّ التدقيقِ
    والمخازنُ العالميةُ خارجَ تنظيفِ التجهيزةِ التلقائيةِ)."""
    from amos_federation.common.database import get_session_factory
    from amos_federation.common.persistent import AuditEntryModel, ExperienceModel

    session = get_session_factory()()
    try:
        session.query(AuditEntryModel).delete()
        session.query(ExperienceModel).delete()
        session.commit()
    finally:
        session.close()


def _w699_5_audit(action: str) -> None:
    from amos_federation.common.persistent import PersistentAuditStore

    PersistentAuditStore().append(action, "EXECUTIVE", {})


def test_w699_5_health_check_classifies_thresholds() -> None:
    """تصنيفُ الفحصِ يقيسُ العتباتِ المعلنةَ: الأداءُ الحرجُ عزلٌ، والأداءُ
    المنخفضُ معَ مخالفةِ سياسةٍ أو أخطاءٍ علاجٌ — بلا افتراضِ «سليم» لكلِّ وكيلٍ."""
    _w699_5_reset_global_stores()
    checker = get_health_checker_for_test()
    # سجلُّ تدقيقٍ عالميٌّ: مخالفتانِ من أربعِ — التزامٌ بالسياساتِ 0.5.
    _w699_5_audit("policy_violation: تجاوز حدّ")
    _w699_5_audit("policy_violation: تجاوز آخر")
    _w699_5_audit("tool_call")
    _w699_5_audit("read")

    _spawn("w699-5-iso")
    _spawn("w699-5-retrain")
    _spawn("w699-5-reset")
    _w699_5_experience("w699-5-iso", 0.2, False)
    _w699_5_experience("w699-5-retrain", 0.4, False)
    _w699_5_experience("w699-5-reset", 0.4, True)

    iso = checker.check_agent("w699-5-iso")
    retrain = checker.check_agent("w699-5-retrain")
    reset = checker.check_agent("w699-5-reset")

    assert iso["status"] == "isolated", "الأداءُ الحرجُ (<0.3) عزلٌ لا غيرَ"
    assert retrain["status"] == "treatment", "الأداءُ المنخفضُ معَ أخطاءٍ علاجٌ"
    assert reset["status"] == "treatment", "الأداءُ المنخفضُ معَ مخالفةِ سياسةٍ علاجٌ"


def test_w699_5_health_check_monitor_and_healthy() -> None:
    """تصنيفُ الفحصِ: أداءٌ دونَ عتبةِ المراقبةِ بلا أخطاءٍ ومخالفاتٍ «مراقبة»،
    وأداءٌ جيدٌ «سليم» — والقراءةُ منَ الخبراتِ الفعليةِ لا منَ الافتراضِ."""
    _w699_5_reset_global_stores()
    checker = get_health_checker_for_test()
    # مخالفةٌ واحدةٌ من عشرِ — التزامٌ بالسياساتِ 0.9: فوقَ عتبةِ المراقبةِ
    # (0.9) فالوكيلُ الجيدُ «سليم»، وفوقَ عتبةِ العلاجِ (0.7) فالمنخفضُ «مراقبة».
    _w699_5_audit("policy_violation: مخالفة وحيدة")
    for _ in range(9):
        _w699_5_audit("tool_call")

    _spawn("w699-5-monitor")
    _spawn("w699-5-healthy")
    _w699_5_experience("w699-5-monitor", 0.5, True)
    _w699_5_experience("w699-5-healthy", 0.9, True)

    monitor = checker.check_agent("w699-5-monitor")
    healthy = checker.check_agent("w699-5-healthy")

    assert monitor["status"] == "monitor", "الأداءُ دونَ 0.7 بلا أخطاءٍ مراقبةٌ"
    assert healthy["status"] == "healthy", "الأداءُ الجيدُ سليمٌ"


def test_w699_5_run_health_cycle_remediates() -> None:
    """دورةُ الفحصِ الصحيةِ الكاملةُ تعالجُ وتعزلُ فعليًّا: نتائجُ الفحصِ
    تصنّفُ الوكلاءَ ثمّ يعالجُ التابعُ المعالَجَ ويَعزلُ الحرجَ — قياسًا منَ
    السجلِّ لا منَ الوعدِ."""
    from amos_federation.services.agent_runtime.health import run_health_cycle
    from amos_federation.services.executive_core.agent_identity import require_identity

    _w699_5_reset_global_stores()
    # التزامٌ بالسياساتِ 0.75 — فالمنخفضُ علاجٌ بلا حاجةِ مخالفةٍ.
    _w699_5_audit("policy_violation: مخالفة وحيدة")
    _w699_5_audit("tool_call")
    _w699_5_audit("read")
    _w699_5_audit("write")

    _spawn("w699-5-cycle-treat")
    _spawn("w699-5-cycle-iso")
    _w699_5_experience("w699-5-cycle-treat", 0.4, False)
    _w699_5_experience("w699-5-cycle-iso", 0.2, False)

    summary = run_health_cycle()

    assert summary["treatment"] == 1 and summary["treatments_started"] == 1
    assert summary["isolated"] == 1 and summary["isolations_started"] == 1
    # المعالَجُ دخلَ العلاجَ (بدءُ علاجٍ يعيدُه «active» بعدَ إتمامِهِ) والحرجُ
    # عُزلَ فانتقلَ إلى «paused».
    assert require_identity("w699-5-cycle-treat").lifecycle_state == "active"
    assert require_identity("w699-5-cycle-iso").lifecycle_state == "paused"
