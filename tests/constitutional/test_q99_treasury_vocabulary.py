"""
اختبارات معجم الدفعة 3 من Q-83 (ج) — قرار المالك Q-99 · WI-127 · قيد W-823
الهدف: إثبات أن أفعال أسطح الخزانة الثلاثة في national_economy حصرٌ للخزانة في
TREASURY_ACTIONS: فاعلٌ مقبولٌ واحد (TREASURY) وتسعةٌ مرفوضون، وأن `authorize_transfer`
جديدٌ بقرار Q-99 وكان مجهولًا يمرّ لكلّ فاعل (المسبار الخام قبلُ: 10/10 ALLOW)، وأن عمليّات
الأسطح الثلاثة في MONEY_OPERATION_LEXICON بأسمائها الحقيقيّة، وأنها خارج KILL_SWITCH_BLOCKS
(Q83C_LEXICON_TABLE_DESIGN.md § 8).
النطاق: core/constitutional_engine/rules.py — المعجم وحده؛ والعبور في
federal/executive/services/tests/test_r9_economy_q99_treasury_crossing.py.
المالك: tests/constitutional/
تاريخ الإنشاء: 2026-11-04
تاريخ آخر تعديل: 2026-11-04 (W-823)
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
    MONEY_OPERATION_LEXICON,
    TREASURY_ACTIONS,
)

Q99_VERBS = (
    "authorize_expenditure",
    "award_procurement",
    "authorize_transfer",
)
#: العمليّةُ في الشِّفرة ⇒ فعلُها (§ 8.1 · تصحيحُ الصفّ 20 بالقياس)
Q99_OPERATIONS = {
    "economy.expenditure.authorize": "authorize_expenditure",
    "economy.procurement.authorize": "award_procurement",
    "economy.grant.authorize": "authorize_transfer",
    "economy.subsidy.authorize": "authorize_transfer",
}
DENIED = tuple(b for b in Branch if b is not Branch.TREASURY)


@pytest.fixture
def engine(tmp_path) -> ConstitutionalEngine:
    return ConstitutionalEngine(ledger_path=tmp_path / "ledger.jsonl")


def test_q99v_0_ten_actors_one_allowed_nine_denied() -> None:
    assert len(Branch) == 10
    assert len(DENIED) == 9


@pytest.mark.parametrize("action", Q99_VERBS)
def test_q99v_1_treasury_is_allowed(action: str, engine: ConstitutionalEngine) -> None:
    verdict = engine.evaluate(
        ActionRequest(actor=Branch.TREASURY, action=action, target="probe/q99")
    )
    assert verdict.decision is Decision.ALLOW, verdict.explain()


@pytest.mark.parametrize("action", Q99_VERBS)
def test_q99v_2_nine_others_are_denied(
    action: str, engine: ConstitutionalEngine
) -> None:
    for actor in DENIED:
        verdict = engine.evaluate(
            ActionRequest(actor=actor, action=action, target="probe/q99")
        )
        assert verdict.decision is Decision.DENY, (actor, action)


def test_q99v_3_each_name_belongs_to_exactly_one_vocabulary() -> None:
    vocabularies = (
        EXECUTIVE_ACTIONS,
        LEGISLATIVE_ACTIONS,
        JUDICIAL_ACTIONS,
        TREASURY_ACTIONS,
    )
    for action in Q99_VERBS:
        owners = [v for v in vocabularies if action in v]
        assert owners == [TREASURY_ACTIONS], action


def test_q99v_4_operations_map_to_their_verbs_in_the_lexicon() -> None:
    for operation, verb in Q99_OPERATIONS.items():
        assert MONEY_OPERATION_LEXICON.get(operation) == verb, operation


def test_q99v_5_not_in_kill_switch_blocks_by_design() -> None:
    blocked = set().union(*KILL_SWITCH_BLOCKS.values())
    assert not set(Q99_VERBS) & blocked
