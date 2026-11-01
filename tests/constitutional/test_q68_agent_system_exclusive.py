"""
اختبارات Q-68 — حصرُ أفعالِ الفروعِ الحصريّةِ عن AGENT وSYSTEM (WI-124 · قيد W-747)
الهدف: إثباتُ أن R-003-1 تمنعُ AGENT وSYSTEM من كلِّ فعلٍ في المعاجمِ الأربعةِ (_BRANCH_EXCLUSIVE)،
وأن الفرعَ المالكَ ما زالَ مُجازًا، وأن المرسومَ الموقَّعَ (المسارُ السياديّ) يُبقي الفعلَ مُجازًا
برأيٍ استشاريٍّ كما هو اليوم، وأن المجموعةَ مغلقةٌ على الفاعلَينِ بنصِّ القرار.
النطاق: core/constitutional_engine/rules.py::_r003_1 — Q68_AGENT_SYSTEM_EXCLUSIVE_DESIGN.md § 4.
المالك: tests/constitutional/
تاريخ الإنشاء: 2026-10-30
تاريخ آخر تعديل: 2026-11-01 (W-774 — test_q68_4: المجموعةُ أربعةٌ بقرارِ Q-87) · وقبله: 2026-10-30 (W-747 — الإنشاء)
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

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
from core.constitutional_engine import rules as rules_module  # noqa: E402
from core.constitutional_engine.rules import _BRANCH_EXCLUSIVE  # noqa: E402

_TMP = tempfile.TemporaryDirectory()
ENGINE = ConstitutionalEngine(ledger_path=Path(_TMP.name) / "ledger.jsonl")

# المعجمُ يُقرأُ من مصدرِه — لا قائمةَ منسوخة: كلُّ اسمٍ يُضافُ لفرعٍ لاحقًا يُحصَرُ تلقائيًّا.
CASES = sorted(
    (action, owner) for owner, actions in _BRANCH_EXCLUSIVE.items() for action in actions
)
EXCLUDED = (Branch.AGENT, Branch.SYSTEM)


def _req(actor: Branch, action: str) -> ActionRequest:
    return ActionRequest(actor=actor, action=action, target="probe/q68", channel="api")


def _rule_ids(violations) -> set[str]:
    return {v.rule_id for v in violations}


def test_q68_0_lexicons_are_measured_not_empty() -> None:
    # 56 فعلًا يومَ القيد (مسبارُ W-747) — الحدُّ الأدنى يحرسُ أن المعلمةَ لم تفرغْ صامتة.
    assert len(CASES) >= 56
    assert set(_BRANCH_EXCLUSIVE) == {
        Branch.EXECUTIVE, Branch.LEGISLATIVE, Branch.JUDICIAL, Branch.TREASURY,
    }


@pytest.mark.parametrize("actor", EXCLUDED, ids=lambda b: b.name)
@pytest.mark.parametrize("action,owner", CASES, ids=lambda x: getattr(x, "name", x))
def test_q68_1_agent_and_system_are_denied_by_r003_1(
    action: str, owner: Branch, actor: Branch
) -> None:
    verdict = ENGINE.evaluate(_req(actor, action))
    assert verdict.decision is Decision.DENY, (actor, action, owner)
    assert "R-003-1" in _rule_ids(verdict.violations), (actor, action, verdict.explain())


@pytest.mark.parametrize("action,owner", CASES, ids=lambda x: getattr(x, "name", x))
def test_q68_2_owner_branch_is_still_allowed(action: str, owner: Branch) -> None:
    verdict = ENGINE.evaluate(_req(owner, action))
    assert "R-003-1" not in _rule_ids(verdict.violations), (owner, action, verdict.explain())


@pytest.mark.parametrize("actor", EXCLUDED, ids=lambda b: b.name)
@pytest.mark.parametrize("action,owner", CASES, ids=lambda x: getattr(x, "name", x))
def test_q68_3_signed_decree_path_stays_allowed_with_advisory(
    action: str, owner: Branch, actor: Branch
) -> None:
    # «عدا مرسوم ملكي موقع كما هو اليوم»: البوّابةُ السياديّةُ تمرِّرُ sovereign=True بعدَ ثبوتِ التوقيع.
    verdict = ENGINE.evaluate(_req(actor, action), sovereign=True)
    assert verdict.decision is Decision.ALLOW, (actor, action, verdict.explain())
    assert "R-003-1" in _rule_ids(verdict.advisory_violations), (actor, action)


def test_q68_4_excluded_set_is_exactly_agent_and_system() -> None:
    # لا يتّسعُ صامتًا — اتّسعَ مرّةً بقرارِ المالكِ Q-87 القرارُ 5 (W-774 · WI-126): «يُمنَع STATE وINSTITUTION
    # بـR-003-1 كما أُضيف AGENT وSYSTEM في Q-68». وHUMAN وROYAL خارجَها: لهما شرطاهما في `_r003_1` (Q-87).
    # (اسمُ الفحصِ يبقى كما هو حفظًا لتاريخِه؛ والمجموعةُ المقيسةُ أربعةٌ بالاسم.)
    assert rules_module._NON_BRANCH_EXCLUDED == frozenset(
        {Branch.AGENT, Branch.SYSTEM, Branch.STATE, Branch.INSTITUTION}
    )
    assert Branch.HUMAN not in rules_module._NON_BRANCH_EXCLUDED
    assert Branch.ROYAL not in rules_module._NON_BRANCH_EXCLUDED


def test_q68_5_mutation_emptying_the_set_reopens_the_gap(monkeypatch) -> None:
    # طفرة: إفراغُ المجموعةِ يُعيدُ AGENT مُجازًا على فعلِ خزانة — فالفحوصُ أعلاه تحرسُ الحصرَ لا تمرُّ صدفة.
    money = sorted(_BRANCH_EXCLUSIVE[Branch.TREASURY])[0]
    assert ENGINE.evaluate(_req(Branch.AGENT, money)).decision is Decision.DENY
    monkeypatch.setattr(rules_module, "_NON_BRANCH_EXCLUDED", frozenset())
    assert ENGINE.evaluate(_req(Branch.AGENT, money)).decision is Decision.ALLOW
