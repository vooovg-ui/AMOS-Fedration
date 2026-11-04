"""
اختبارات معجم الدفعة 1 من Q-83 (ج) — قرار المالك Q-97 · WI-127 · قيد W-818
الهدف: إثبات أن الأفعال الثمانية لأسطح federal_state صارت حصرًا تنفيذيًّا في
EXECUTIVE_ACTIONS: فاعلٌ مقبولٌ واحد (EXECUTIVE) وتسعةٌ مرفوضون، وأن كلَّ اسمٍ في معجمٍ
واحد، وأنها خارج KILL_SWITCH_BLOCKS بقرار التصميم (Q83C_LEXICON_TABLE_DESIGN.md § 6.4).
النطاق: core/constitutional_engine/rules.py — المعجم وحده؛ والعبور في
federal/executive/services/tests/test_r8_q97_federal_state_crossing.py.
المالك: tests/constitutional/
تاريخ الإنشاء: 2026-11-04
تاريخ آخر تعديل: 2026-11-04 (W-818)
"""

from __future__ import annotations

import sys

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.constitutional_engine import (  # noqa: E402
    ActionRequest,
    Branch,
    ConstitutionalEngine,
    Decision,
)
from core.constitutional_engine.rules import (  # noqa: E402
    EXECUTIVE_ACTIONS,
    JUDICIAL_ACTIONS,
    KILL_SWITCH_BLOCKS,
    LEGISLATIVE_ACTIONS,
    TREASURY_ACTIONS,
)

Q97_VERBS = (
    "register_government",
    "set_government_status",
    "bind_institution",
    "record_relation",
    "grant_delegation",
    "revoke_delegation",
    "scope_service",
    "scope_case",
)
DENIED = tuple(b for b in Branch if b is not Branch.EXECUTIVE)


@pytest.fixture
def engine(tmp_path) -> ConstitutionalEngine:
    return ConstitutionalEngine(ledger_path=tmp_path / "ledger.jsonl")


def test_q97v_0_ten_actors_one_allowed_nine_denied() -> None:
    assert len(Branch) == 10
    assert len(DENIED) == 9


@pytest.mark.parametrize("action", Q97_VERBS)
def test_q97v_1_executive_is_allowed(action: str, engine: ConstitutionalEngine) -> None:
    verdict = engine.evaluate(
        ActionRequest(actor=Branch.EXECUTIVE, action=action, target="probe/q97")
    )
    assert verdict.decision is Decision.ALLOW, verdict.explain()


@pytest.mark.parametrize("action", Q97_VERBS)
def test_q97v_2_nine_others_are_denied(
    action: str, engine: ConstitutionalEngine
) -> None:
    for actor in DENIED:
        verdict = engine.evaluate(
            ActionRequest(actor=actor, action=action, target="probe/q97")
        )
        assert verdict.decision is Decision.DENY, (actor, action)


def test_q97v_3_each_name_belongs_to_exactly_one_vocabulary() -> None:
    vocabularies = (
        EXECUTIVE_ACTIONS,
        LEGISLATIVE_ACTIONS,
        JUDICIAL_ACTIONS,
        TREASURY_ACTIONS,
    )
    for action in Q97_VERBS:
        owners = [v for v in vocabularies if action in v]
        assert owners == [EXECUTIVE_ACTIONS], action


def test_q97v_4_not_in_kill_switch_blocks_by_design() -> None:
    blocked = set().union(*KILL_SWITCH_BLOCKS.values())
    assert not set(Q97_VERBS) & blocked
