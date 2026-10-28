"""
اختبارات دفعة المعجم G1 (§ 5.1) — WI-120 · قيد W-722
الهدف: إثبات أن الأسماء الخمسة المعتمدة (OWNER-DECISIONS-D28) صارت حصرًا لفرعها بـR-003-1،
وأن مستويات زر الإيقاف المضافة تمنع عند كل مستوى ≥ N، وأن المستثنى بالتعديلين (أ) و(ب) غائب.
النطاق: core/constitutional_engine/rules.py — المعجم وحده، لا سلوك جديد.
المالك: tests/constitutional/
تاريخ الإنشاء: 2026-10-28
تاريخ آخر تعديل: 2026-10-28
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
)  # noqa: E402
from core.constitutional_engine.rules import (  # noqa: E402
    EXECUTIVE_ACTIONS,
    JUDICIAL_ACTIONS,
    KILL_SWITCH_BLOCKS,
    LEGISLATIVE_ACTIONS,
    TREASURY_ACTIONS,
)

FOUR = (Branch.EXECUTIVE, Branch.LEGISLATIVE, Branch.JUDICIAL, Branch.TREASURY)
NEW_NAMES = {
    "issue_certificate": Branch.EXECUTIVE,
    "create_backup": Branch.EXECUTIVE,
    "self_heal": Branch.EXECUTIVE,
    "suspend_policy": Branch.LEGISLATIVE,
    "vote": Branch.LEGISLATIVE,
}
ENGINE = ConstitutionalEngine()


def _rule_ids(verdict) -> set[str]:
    return {v.rule_id for v in verdict.violations}


@pytest.mark.parametrize("action,owner", sorted(NEW_NAMES.items()))
def test_g1v_1_owner_branch_is_allowed(action: str, owner: Branch) -> None:
    verdict = ENGINE.evaluate(
        ActionRequest(actor=owner, action=action, target="probe/g1")
    )
    assert verdict.decision is Decision.ALLOW, verdict.explain()


@pytest.mark.parametrize("action,owner", sorted(NEW_NAMES.items()))
def test_g1v_2_other_branches_are_denied_by_r003_1(action: str, owner: Branch) -> None:
    for actor in FOUR:
        if actor is owner:
            continue
        verdict = ENGINE.evaluate(
            ActionRequest(actor=actor, action=action, target="probe/g1")
        )
        assert verdict.decision is Decision.DENY, (actor, action)
        assert "R-003-1" in _rule_ids(verdict), (actor, action, _rule_ids(verdict))


def test_g1v_3_each_name_belongs_to_exactly_one_vocabulary() -> None:
    vocabularies = (
        EXECUTIVE_ACTIONS,
        LEGISLATIVE_ACTIONS,
        JUDICIAL_ACTIONS,
        TREASURY_ACTIONS,
    )
    for action in NEW_NAMES:
        assert sum(action in vocab for vocab in vocabularies) == 1, action


def test_g1v_4_excluded_names_stay_out() -> None:
    """(أ) store_secret وrestore_backup دَين · (ب) reward_agent يتبع M1 — لا يدخل أيٌّ منها."""
    vocabularies = (
        EXECUTIVE_ACTIONS | LEGISLATIVE_ACTIONS | JUDICIAL_ACTIONS | TREASURY_ACTIONS
    )
    for action in ("store_secret", "restore_backup", "reward_agent"):
        assert action not in vocabularies, action


@pytest.mark.parametrize("action,level", [("issue_certificate", 3), ("self_heal", 4)])
def test_g1v_5_kill_switch_blocks_at_and_above_level(action: str, level: int) -> None:
    assert action in KILL_SWITCH_BLOCKS[level]
    for current in range(0, 6):
        verdict = ENGINE.evaluate(
            ActionRequest(
                actor=Branch.EXECUTIVE,
                action=action,
                target="probe/g1",
                kill_switch_level=current,
            )
        )
        blocked = "R-008-2" in _rule_ids(verdict)
        assert blocked is (current >= level), (action, current, verdict.explain())


def test_g1v_6_create_backup_is_never_blocked_by_kill_switch() -> None:
    for current in range(0, 6):
        verdict = ENGINE.evaluate(
            ActionRequest(
                actor=Branch.EXECUTIVE,
                action="create_backup",
                target="probe/g1",
                kill_switch_level=current,
            )
        )
        assert "R-008-2" not in _rule_ids(verdict), current
