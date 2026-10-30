"""W-750 · دفعةُ المعجم — create_batch · enroll_batch · evaluate_model تعبرُ الحدَّ السياديّ.

الهدف: إثباتُ قراراتِ المالكِ Q-77 ② (create_batch على `create_task` ≥4 · enroll_batch على
       `spawn_agent` ≥3) وQ-80 ② (evaluate_model على `record_curriculum_step` ≥1) بأصنافِ G1 § 4
       الخمسة، وقياسُ أنَّ `graceful_shutdown` لا يمنعُه القاطعُ (Q-76 ② · منفَّذٌ في W-724)،
       وأنَّ خطَّ التوسّعِ القصيرَ (إنشاءٌ ⇒ تسجيلٌ ⇒ تخريجٌ ⇒ توظيفٌ) يعبرُ كلُّه.
النطاق: سلوكُ الأسطحِ الثلاثةِ وحدَه (تصميمُ G1 § 9.11 · W-749). تحويلُ graduate_batch
        وcomplete_training إلى `activate_agent` (Q-78 ③) مفحوصٌ في test_w724/test_w728.
        حقنُ مستوى القاطعِ في الطلبِ محاكاةٌ لحالتِه معلَنةٌ هنا (نمطُ WI-082 · E1)، لأنَّ الجسرَ
        لا يحقنُه في الإنتاج (DISC-099/WI-085) — فهذه الفحوصُ لا تُثبِتُ منعًا في الإنتاج.
        ولا أحدَ من الأفعالِ محجوزٌ بشريًّا — فلا `human_approval` في أيِّ نداء.
المالك: federal/executive/services — WI-120 (G1 · تصميمُ W-749 § 9.11).
تاريخ الإنشاء: 2026-10-30 (W-750)

الدليلُ المُعادُ تشغيلُه (من federal/executive/services):
    ../../../.venv/bin/python -m pytest tests/test_w750_lexicon_batch.py -q
"""

from __future__ import annotations

import ast
import inspect
import textwrap
import uuid
from typing import Any

import pytest

from amos_federation.services.agent_runtime.population import get_population_registry
from amos_federation.services.governance import expansion as ex
from amos_federation.services.governance import learning_cycle as lc
from amos_federation.services.governance.expansion import (
    ExpansionBatchModel,
    PopulationExpansion,
)
from amos_federation.services.governance.learning_cycle import (
    EvaluationResultModel,
    EvaluationSystem,
)
from amos_federation.services.governance.system_life import SystemLifecycle
from tests.test_w724_g1_expansion import (
    BROKEN,
    KillSwitchAuthorizer,
    RecordingAuthorizer,
    _batch,
    _break_commit,
    _count,
    _evidence,
    _violation,
)


def _bid() -> str:
    return f"w750-batch-{uuid.uuid4().hex[:6]}"


@pytest.fixture
def rec() -> RecordingAuthorizer:
    return RecordingAuthorizer()


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 1 — الرفضُ قبلَ الكتابة (مستوى القاطعِ محقونٌ في الطلب)
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.parametrize(("level", "blocked"), [(3, False), (4, True), (5, True)])
def test_c1_create_batch_blocked_from_level4(level: int, blocked: bool) -> None:
    ks = KillSwitchAuthorizer(level)
    pe = PopulationExpansion(authorizer=ks)
    batch_id = _bid()
    if blocked:
        with pytest.raises(_violation()):
            pe.create_batch("reserve", 2, operation_id=batch_id)
        assert _count(pe, ExpansionBatchModel, batch_id=batch_id) == 0
    else:
        out = pe.create_batch("reserve", 2, operation_id=batch_id)
        assert out["batch_id"] == batch_id
        assert _count(pe, ExpansionBatchModel, batch_id=batch_id) == 1
        assert _evidence(ks)["action"] == "create_task"


@pytest.mark.parametrize(("level", "blocked"), [(2, False), (3, True), (4, True)])
def test_c1_enroll_blocked_from_level3_no_registration(level: int, blocked: bool) -> None:
    pe = PopulationExpansion()
    batch_id = pe.create_batch("reserve", 2, operation_id=_bid())["batch_id"]
    ks = KillSwitchAuthorizer(level)
    pe_ks = PopulationExpansion(authorizer=ks)
    before = len(get_population_registry().list_agents())
    if blocked:
        with pytest.raises(_violation()):
            pe_ks.enroll_batch(batch_id, 2)
        assert ks.results == []
        assert _batch(pe, batch_id).enrolled == 0
        assert len(get_population_registry().list_agents()) == before
    else:
        enrolled = pe_ks.enroll_batch(batch_id, 2)
        assert len(enrolled) == 2 and _batch(pe, batch_id).enrolled == 2
        assert _evidence(ks)["action"] == "spawn_agent"


@pytest.mark.parametrize(("level", "blocked"), [(0, False), (1, True), (2, True)])
def test_c1_evaluate_blocked_from_level1_no_row(level: int, blocked: bool) -> None:
    ks = KillSwitchAuthorizer(level)
    evs = EvaluationSystem(authorizer=ks)
    eval_id = f"w750-eval-{level}-{uuid.uuid4().hex[:6]}"
    if blocked:
        with pytest.raises(_violation()):
            evs.evaluate_model("amos-alpha", "bench-1", 90, operation_id=eval_id)
        assert _count(evs, EvaluationResultModel, eval_id=eval_id) == 0
    else:
        out = evs.evaluate_model("amos-alpha", "bench-1", 90, operation_id=eval_id)
        assert out["eval_id"] == eval_id
        assert _count(evs, EvaluationResultModel, eval_id=eval_id) == 1
        assert _evidence(ks)["action"] == "record_curriculum_step"


def test_c1_no_surface_needs_human_approval() -> None:
    """لا فعلَ من الثلاثةِ محجوزٌ بشريًّا — المسبارُ (W-749) والقاعدةُ متطابقان."""
    from core.constitutional_engine.rules import HUMAN_GATED_ACTIONS

    for action in (ex.ACTION_CREATE_BATCH, ex.ACTION_ENROLL_BATCH, lc.ACTION_EVALUATE_MODEL):
        assert action not in HUMAN_GATED_ACTIONS, action


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 2 — النجاحُ عبرَ الحدِّ بالفعلِ المسمّى
# ═════════════════════════════════════════════════════════════════════════════
def test_c2_create_batch_named_action(rec: RecordingAuthorizer) -> None:
    PopulationExpansion(authorizer=rec).create_batch("reserve", 1)
    evidence = _evidence(rec)
    assert evidence["action"] == "create_task" and evidence["decision"] == "ALLOW"


def test_c2_evaluate_named_action(rec: RecordingAuthorizer) -> None:
    EvaluationSystem(authorizer=rec).evaluate_model("amos-alpha", "bench-1", 88)
    evidence = _evidence(rec)
    assert evidence["action"] == "record_curriculum_step" and evidence["decision"] == "ALLOW"


def test_c2_enroll_permit_first_inner_registrations_then_counter(
    rec: RecordingAuthorizer,
) -> None:
    """التحقّقُ المسبقُ على `spawn_agent` أوّلًا، ثمَّ عبورُ كلِّ تسجيل، ثمَّ عبورُ العدّادِ آخرًا."""
    pe = PopulationExpansion(authorizer=rec)
    batch_id = pe.create_batch("reserve", 3)["batch_id"]
    rec.results.clear()
    rec.permits.clear()
    enrolled = pe.enroll_batch(batch_id, 3)
    assert len(enrolled) == 3 and _batch(pe, batch_id).enrolled == 3
    assert rec.permits and rec.permits[0] == "spawn_agent"
    actions = [r.evidence.as_dict()["action"] for r in rec.results]
    assert actions.count("spawn_agent") == 4  # ثلاثةُ تسجيلاتٍ + عبورُ العدّاد
    assert actions[-1] == "spawn_agent"


def test_c2_short_pipeline_crosses_every_step(rec: RecordingAuthorizer) -> None:
    """خطُّ التوسّعِ القصيرُ عندَ المستوى 0: كلُّ خطوةٍ تعبرُ بفعلِها (create → enroll → graduate → employ)."""
    pe = PopulationExpansion(authorizer=rec)
    batch_id = pe.create_batch("reserve", 1)["batch_id"]
    pe.enroll_batch(batch_id, 1)
    pe.graduate_batch(batch_id)
    pe.employ_batch(batch_id)
    actions = [r.evidence.as_dict()["action"] for r in rec.results]
    for expected in ["create_task", "spawn_agent", "activate_agent", "dispatch_agent"]:
        assert expected in actions, expected
    assert actions.index("create_task") < actions.index("spawn_agent")
    assert actions[-1] == "dispatch_agent"


def test_c2_short_pipeline_level3_stops_at_enroll() -> None:
    """عندَ المستوى 3 يُنشأُ صفُّ الدفعةِ ويتوقّفُ الخطُّ عندَ التسجيلِ قبلَ أيِّ وكيل."""
    ks = KillSwitchAuthorizer(3)
    pe = PopulationExpansion(authorizer=ks)
    batch_id = pe.create_batch("reserve", 1)["batch_id"]
    before = len(get_population_registry().list_agents())
    with pytest.raises(_violation()):
        pe.enroll_batch(batch_id, 1)
    assert len(get_population_registry().list_agents()) == before
    assert _batch(pe, batch_id).enrolled == 0


@pytest.mark.parametrize("level", [0, 3, 5])
def test_c2_graceful_shutdown_not_blocked_measured(level: int) -> None:
    """Q-76 ② (منفَّذٌ في W-724): `graceful_shutdown` لا يمنعُه القاطعُ عندَ أيِّ مستوى — يُقاسُ ولا يُعاد."""
    ks = KillSwitchAuthorizer(level)
    out = SystemLifecycle(authorizer=ks).graceful_shutdown("w750")
    assert out["status"] == "shutdown_complete"
    assert _evidence(ks)["action"] == "graceful_shutdown"


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 3 — طفرةٌ لكلِّ سطح (والحملةُ السلوكيّةُ في evidence/W-750/mutations.txt)
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.parametrize(
    ("owner", "surface", "const", "module", "action"),
    [
        (PopulationExpansion, "create_batch", "ACTION_CREATE_BATCH", ex, "create_task"),
        (PopulationExpansion, "enroll_batch", "ACTION_ENROLL_BATCH", ex, "spawn_agent"),
        (EvaluationSystem, "evaluate_model", "ACTION_EVALUATE_MODEL", lc, "record_curriculum_step"),
    ],
)
def test_c3_guard_call_literally_in_public_body(
    owner: type, surface: str, const: str, module: Any, action: str
) -> None:
    tree = ast.parse(textwrap.dedent(inspect.getsource(getattr(owner, surface))))
    calls = [
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr == "guard_declared"
    ]
    assert len(calls) == 1, f"{surface}: نداءُ العبورِ ليس واحدًا في الجسد"
    first = calls[0].args[0]
    assert isinstance(first, ast.Name) and first.id == const
    assert getattr(module, const) == action


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 4 — الإعادةُ لا تُكرِّرُ الأثر
# ═════════════════════════════════════════════════════════════════════════════
def test_c4_create_batch_replay_one_row(rec: RecordingAuthorizer) -> None:
    pe = PopulationExpansion(authorizer=rec)
    batch_id = _bid()
    pe.create_batch("reserve", 1, operation_id=batch_id)
    again = pe.create_batch("reserve", 1, operation_id=batch_id)
    assert again["replayed"] is True
    assert _count(pe, ExpansionBatchModel, batch_id=batch_id) == 1


def test_c4_enroll_replay_registers_nobody(rec: RecordingAuthorizer) -> None:
    pe = PopulationExpansion(authorizer=rec)
    batch_id = pe.create_batch("reserve", 2)["batch_id"]
    first = pe.enroll_batch(batch_id, 2, operation_id="w750-enroll-replay")
    before = len(get_population_registry().list_agents())
    again = pe.enroll_batch(batch_id, 2, operation_id="w750-enroll-replay")
    assert len(first) == 2 and again == []
    assert len(get_population_registry().list_agents()) == before
    assert _batch(pe, batch_id).enrolled == 2


def test_c4_evaluate_replay_one_row(rec: RecordingAuthorizer) -> None:
    evs = EvaluationSystem(authorizer=rec)
    eval_id = f"w750-eval-replay-{uuid.uuid4().hex[:6]}"
    evs.evaluate_model("amos-alpha", "bench-1", 90, operation_id=eval_id)
    again = evs.evaluate_model("amos-alpha", "bench-1", 90, operation_id=eval_id)
    assert again["replayed"] is True
    assert _count(evs, EvaluationResultModel, eval_id=eval_id) == 1


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 5 — المعوِّضُ على المسارِ الحقيقيّ
# ═════════════════════════════════════════════════════════════════════════════
def test_c5_create_batch_failure_deletes_row(monkeypatch: pytest.MonkeyPatch) -> None:
    pe = PopulationExpansion()
    batch_id = _bid()
    _break_commit(monkeypatch, ex.BATCH_CREATE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        pe.create_batch("reserve", 1, operation_id=batch_id)
    assert _count(pe, ExpansionBatchModel, batch_id=batch_id) == 0


def test_c5_enroll_failure_restores_previous_count(monkeypatch: pytest.MonkeyPatch) -> None:
    """المعوِّضُ يُعيدُ العدّاد؛ والتسجيلاتُ الداخليّةُ عبرت بعبورِها (حدٌّ معلَن · § 9.9.6 (1))."""
    pe = PopulationExpansion()
    batch_id = pe.create_batch("reserve", 1)["batch_id"]
    _break_commit(monkeypatch, ex.BATCH_ENROLL_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        pe.enroll_batch(batch_id, 1)
    assert _batch(pe, batch_id).enrolled == 0


def test_c5_evaluate_failure_deletes_row(monkeypatch: pytest.MonkeyPatch) -> None:
    evs = EvaluationSystem()
    eval_id = f"w750-eval-c5-{uuid.uuid4().hex[:6]}"
    _break_commit(monkeypatch, lc.EVAL_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        evs.evaluate_model("amos-alpha", "bench-1", 90, operation_id=eval_id)
    assert _count(evs, EvaluationResultModel, eval_id=eval_id) == 0
