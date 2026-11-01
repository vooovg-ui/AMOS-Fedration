"""
اختبارات Q-87 (ج) — الفاعلون الأربعة على الأفعالِ الحصريّة (WI-126 · قيد W-774)
الهدف: إثباتُ القرارِ 5 من Q-87: STATE وINSTITUTION يُرفَضانِ بـR-003-1 على كلِّ فعلٍ حصريّ · HUMAN يحتاجُ
موافقةً بشريّةً موسومةً (`human_approved` ومصدرُ `metadata["human_approval_source"]` من قناةِ W-740) على
الحصريّةِ وعلى أفعالِ المال · ROYAL بلا مرسومٍ رفضٌ في `review` كما في `execute` · ROYAL بمرسومٍ لا يُمنَع.
النطاق: core/constitutional_engine/rules.py::_r003_1 — docs/audit/Q87_FOUR_ACTORS_DESIGN.md § 2 و§ 5.
المالك: tests/constitutional/
تاريخ الإنشاء: 2026-11-01
تاريخ آخر تعديل: 2026-11-01 (W-774 — الإنشاء)
"""

from __future__ import annotations

import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import core.sovereignty.crown as crown_mod  # noqa: E402
from core.constitutional_engine import (  # noqa: E402
    ActionRequest,
    Branch,
    ConstitutionalEngine,
    Decision,
)
from core.constitutional_engine import rules as rules_module  # noqa: E402
from core.constitutional_engine.ledger import ConstitutionalLedger  # noqa: E402
from core.constitutional_engine.rules import (  # noqa: E402
    _BRANCH_EXCLUSIVE,
    NON_CONSTITUTIONAL_MONEY_ACTIONS,
)
from core.sovereignty.crown import provision_crown  # noqa: E402
from core.sovereignty.decree import RoyalDecree, sign_decree  # noqa: E402
from core.sovereignty.gateway import RoyalImpersonation, SovereignGateway  # noqa: E402
from cryptography.hazmat.primitives import serialization  # noqa: E402

_TMP = tempfile.TemporaryDirectory()
ENGINE = ConstitutionalEngine(ledger_path=Path(_TMP.name) / "ledger.jsonl")

# المعجمُ يُقرأُ من مصدرِه — لا قائمةَ منسوخة.
CASES = sorted(
    (action, owner)
    for owner, actions in _BRANCH_EXCLUSIVE.items()
    for action in actions
)
# فعلٌ حصريٌّ واحدٌ من كلِّ فرعٍ (أصغرُها اسمًا) — «فعلٌ حصريٌّ من كلِّ فرع» بنصِّ § 5.
ONE_PER_BRANCH = sorted(
    (sorted(actions)[0], owner) for owner, actions in _BRANCH_EXCLUSIVE.items()
)
MONEY = sorted(NON_CONSTITUTIONAL_MONEY_ACTIONS)
_SOURCE = "require_king"  # القيمةُ التي تكتبُها قناةُ W-740 في مسارِ الكناري (test_wi114_canary_sovereign)


def _req(actor: Branch, action: str, **kw) -> ActionRequest:
    return ActionRequest(
        actor=actor, action=action, target="probe/q87", channel="api", **kw
    )


def _tagged(action: str) -> ActionRequest:
    return _req(
        Branch.HUMAN,
        action,
        human_approved=True,
        metadata={"human_approval_source": _SOURCE},
    )


def _rule_ids(violations) -> set[str]:
    return {v.rule_id for v in violations}


def _denied_by_r003_1(req: ActionRequest) -> bool:
    verdict = ENGINE.evaluate(req)
    return verdict.decision is Decision.DENY and "R-003-1" in _rule_ids(
        verdict.violations
    )


def test_q87_0_lexicons_are_measured_not_empty() -> None:
    assert len(CASES) >= 56
    assert len(ONE_PER_BRANCH) == 4
    assert MONEY, "معجمُ أفعالِ المالِ فرغَ صامتًا"


# ── STATE وINSTITUTION: رفضٌ على كلِّ حصريّ ─────────────────────────────────
@pytest.mark.parametrize(
    "actor", (Branch.STATE, Branch.INSTITUTION), ids=lambda b: b.name
)
@pytest.mark.parametrize("action,owner", CASES, ids=lambda x: getattr(x, "name", x))
def test_q87_1_state_and_institution_are_denied_on_every_exclusive(
    action: str, owner: Branch, actor: Branch
) -> None:
    assert _denied_by_r003_1(_req(actor, action)), (actor, action, owner)


# ── الأربعةُ × فعلٌ حصريٌّ من كلِّ فرعٍ (بلا وسمٍ ولا مرسوم) ⇐ DENY ────────────
@pytest.mark.parametrize(
    "actor",
    (Branch.STATE, Branch.INSTITUTION, Branch.HUMAN, Branch.ROYAL),
    ids=lambda b: b.name,
)
@pytest.mark.parametrize(
    "action,owner", ONE_PER_BRANCH, ids=lambda x: getattr(x, "name", x)
)
def test_q87_2_four_actors_denied_one_exclusive_per_branch(
    action: str, owner: Branch, actor: Branch
) -> None:
    assert _denied_by_r003_1(_req(actor, action)), (actor, action, owner)


# ── HUMAN ────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("action,owner", CASES, ids=lambda x: getattr(x, "name", x))
def test_q87_3_human_approved_without_source_is_denied(
    action: str, owner: Branch
) -> None:
    # «موسومة»: human_approved=True وحدَه لا يكفي.
    assert _denied_by_r003_1(_req(Branch.HUMAN, action, human_approved=True)), action


@pytest.mark.parametrize("source", ("", "   ", None, 7), ids=repr)
def test_q87_4_human_with_empty_or_non_text_source_is_denied(source) -> None:
    action = ONE_PER_BRANCH[0][0]
    req = _req(
        Branch.HUMAN,
        action,
        human_approved=True,
        metadata={"human_approval_source": source},
    )
    assert _denied_by_r003_1(req), source


def test_q87_5_source_without_human_approved_is_denied() -> None:
    action = ONE_PER_BRANCH[0][0]
    req = _req(Branch.HUMAN, action, metadata={"human_approval_source": _SOURCE})
    assert _denied_by_r003_1(req)


@pytest.mark.parametrize("action,owner", CASES, ids=lambda x: getattr(x, "name", x))
def test_q87_6_human_with_tagged_approval_is_not_refused_by_r003_1(
    action: str, owner: Branch
) -> None:
    verdict = ENGINE.evaluate(_tagged(action))
    assert "R-003-1" not in _rule_ids(verdict.violations), (action, verdict.explain())


@pytest.mark.parametrize("action", MONEY)
def test_q87_7_human_on_money_without_tag_is_denied(action: str) -> None:
    assert _denied_by_r003_1(_req(Branch.HUMAN, action)), action
    assert _denied_by_r003_1(_req(Branch.HUMAN, action, human_approved=True)), action


@pytest.mark.parametrize("action", MONEY)
def test_q87_8_human_on_money_with_tag_is_not_refused_by_r003_1(action: str) -> None:
    verdict = ENGINE.evaluate(_tagged(action))
    assert "R-003-1" not in _rule_ids(verdict.violations), (action, verdict.explain())


def test_q87_9_human_on_non_exclusive_non_money_is_untouched() -> None:
    action = "run_local_task"
    assert all(action not in s for s in _BRANCH_EXCLUSIVE.values())
    assert action not in NON_CONSTITUTIONAL_MONEY_ACTIONS
    verdict = ENGINE.evaluate(_req(Branch.HUMAN, action))
    assert "R-003-1" not in _rule_ids(verdict.violations)


# ── ROYAL ────────────────────────────────────────────────────────────────────
@pytest.fixture
def crown(monkeypatch, tmp_path):
    key_path = tmp_path / "crown.pem"
    registry = tmp_path / "CROWN_KEYS.json"
    provision_crown(key_path, registry_path=registry)
    monkeypatch.setattr(crown_mod, "CROWN_KEYS_PATH", registry)
    priv = serialization.load_pem_private_key(key_path.read_bytes(), password=None)
    return priv, crown_mod.load_crown().key_id


@pytest.fixture
def gateway(tmp_path) -> SovereignGateway:
    return SovereignGateway(
        ConstitutionalEngine(ledger=ConstitutionalLedger(tmp_path / "l.jsonl"))
    )


@pytest.mark.parametrize(
    "action,owner", ONE_PER_BRANCH, ids=lambda x: getattr(x, "name", x)
)
def test_q87_10_royal_without_decree_review_and_execute_both_refuse(
    gateway: SovereignGateway, action: str, owner: Branch
) -> None:
    # التوحيد: `review` يُقيِّمُه تابعًا فيرفضُه R-003-1، و`execute` يرفضُه انتحالًا — كلاهما رفض.
    req = ActionRequest(actor=Branch.ROYAL, action=action, target="probe/q87")
    verdict = gateway.review(req)
    assert verdict.decision is Decision.DENY, (action, verdict.explain())
    assert "R-003-1" in _rule_ids(verdict.violations)
    ran: list[str] = []
    with pytest.raises(RoyalImpersonation):
        gateway.execute(req, lambda: ran.append("ran"))
    assert ran == []


@pytest.mark.parametrize(
    "action,owner", ONE_PER_BRANCH, ids=lambda x: getattr(x, "name", x)
)
def test_q87_11_royal_with_signed_decree_is_not_blocked(
    crown, gateway: SovereignGateway, action: str, owner: Branch
) -> None:
    key, key_id = crown
    decree = sign_decree(
        RoyalDecree(
            decree_id=f"q87-{action}",
            action=action,
            issued_at=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            key_id=key_id,
        ),
        key,
    )
    ran: list[str] = []
    gateway.execute(
        ActionRequest(actor=Branch.ROYAL, action=action, royal_decree=decree),
        lambda: ran.append("ran"),
    )
    assert ran == ["ran"], action


def test_q87_12_crown_effect_of_r003_1_stays_advisory() -> None:
    # الأثرُ للتاجِ لا يتغيّر: في المسارِ السياديِّ R-003-1 رأيٌ لا منع.
    verdict = ENGINE.evaluate(_req(Branch.STATE, ONE_PER_BRANCH[0][0]), sovereign=True)
    assert verdict.decision is Decision.ALLOW
    assert "R-003-1" in _rule_ids(verdict.advisory_violations)


# ── الطفرتانِ (داخلَ الملفِّ أيضًا · والمقيستانِ على المصدرِ في evidence/W-774) ───
def test_q87_13_mutation_dropping_state_institution_reopens_the_gap(
    monkeypatch,
) -> None:
    action = ONE_PER_BRANCH[0][0]
    assert _denied_by_r003_1(_req(Branch.STATE, action))
    monkeypatch.setattr(
        rules_module, "_NON_BRANCH_EXCLUDED", frozenset({Branch.AGENT, Branch.SYSTEM})
    )
    assert not _denied_by_r003_1(_req(Branch.STATE, action))
    assert not _denied_by_r003_1(_req(Branch.INSTITUTION, action))


def test_q87_14_mutation_ignoring_the_tag_reopens_the_gap(monkeypatch) -> None:
    action = ONE_PER_BRANCH[0][0]
    untagged = _req(Branch.HUMAN, action, human_approved=True)
    assert _denied_by_r003_1(untagged)
    monkeypatch.setattr(
        rules_module,
        "_r003_1_human",
        lambda req: None if req.human_approved else "mutant",
    )
    assert not _denied_by_r003_1(untagged)
