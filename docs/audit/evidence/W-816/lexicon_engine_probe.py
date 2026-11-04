"""الهدف: قياسُ المحرّكِ الدستوريِّ على كلِّ فعلٍ مقترحٍ في جدولِ معجمِ Q-83 (ج) قبلَ اقتراحِه.

يُقاسُ لكلِّ مرشَّحٍ (الفعلِ المقترحِ وما يُقاربُه من أفعالٍ قائمة) حكمُ `ConstitutionalEngine.evaluate`
لكلٍّ من الفاعلينَ العشرة في وضعين:
  - «الآن»: المعجمُ كما هو في الشِّفرة (الفعلُ الجديدُ مجهولٌ للمحرّك).
  - «مقترح»: المعجمُ بعدَ إضافةِ الأفعالِ الجديدةِ إلى حصرِ فرعِها المقترح — ترقيعٌ في الذاكرةِ
    لـ`rules._BRANCH_EXCLUSIVE` داخلَ هذا التشغيلِ وحدَه، لا يمسُّ ملفًّا في `core/`.

النطاق: قراءةٌ فقط — سجلٌّ مؤقّتٌ في مجلدٍ مؤقّت؛ لا يمسُّ شِفرةَ الإنتاجِ ولا يكتبُ في المستودع.
المالك: Perplexity Computer (WI-122 · Q-83 (ج) · توجيهُ المستشارِ 41 § 2 بند 2 · قيدُ W-816).

التشغيلُ (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-816/lexicon_engine_probe.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from core.constitutional_engine import rules  # noqa: E402
from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402

ACTORS = [
    Branch.EXECUTIVE,
    Branch.LEGISLATIVE,
    Branch.JUDICIAL,
    Branch.TREASURY,
    Branch.ROYAL,
    Branch.HUMAN,
    Branch.STATE,
    Branch.INSTITUTION,
    Branch.AGENT,
    Branch.SYSTEM,
]

# الأفعالُ الجديدةُ المقترحة وحصرُ فرعِها — لا شيءَ منها في الشِّفرةِ اليوم.
NEW_EXECUTIVE = (
    "register_government",
    "set_government_status",
    "bind_institution",
    "record_relation",
    "grant_delegation",
    "revoke_delegation",
    "scope_service",
    "scope_case",
    "register_sector",
    "register_category",
    "define_indicator",
    "register_public_entity",
    "create_program",
    "issue_policy",
    "register_revenue_source",
    "register_public_asset",
    "register_public_liability",
    "execute_scoped_operation",
    "activate_policy",
    "execute_economic_decision",
)
NEW_TREASURY = ("authorize_transfer",)
NEW_NON_CONSTITUTIONAL_MONEY = ("log_cost",)

# (السطح، الفعلُ المقترح، الفاعلُ المقترح، البدائلُ القائمةُ المقيسة)
SURFACES = [
    (
        "federal_state.register_government",
        "register_government",
        Branch.EXECUTIVE,
        ("create_state", "admit_state"),
    ),
    (
        "federal_state.set_government_status",
        "set_government_status",
        Branch.EXECUTIVE,
        ("dissolve_state",),
    ),
    (
        "federal_state.bind_institution",
        "bind_institution",
        Branch.EXECUTIVE,
        ("create_institution",),
    ),
    ("federal_state.record_relation", "record_relation", Branch.EXECUTIVE, ()),
    (
        "federal_state.grant_delegation",
        "grant_delegation",
        Branch.EXECUTIVE,
        ("grant_authority",),
    ),
    (
        "federal_state.revoke_delegation",
        "revoke_delegation",
        Branch.EXECUTIVE,
        ("revoke_authority",),
    ),
    (
        "federal_state.scope_service",
        "scope_service",
        Branch.EXECUTIVE,
        ("deploy_service",),
    ),
    ("federal_state.scope_case", "scope_case", Branch.EXECUTIVE, ("assign_case",)),
    ("national_economy.register_sector", "register_sector", Branch.EXECUTIVE, ()),
    ("national_economy.register_category", "register_category", Branch.EXECUTIVE, ()),
    ("national_economy.define_indicator", "define_indicator", Branch.EXECUTIVE, ()),
    (
        "national_economy.register_public_entity",
        "register_public_entity",
        Branch.EXECUTIVE,
        ("create_institution",),
    ),
    (
        "national_economy.create_program",
        "create_program",
        Branch.EXECUTIVE,
        ("create_budget",),
    ),
    (
        "national_economy.issue_policy",
        "issue_policy",
        Branch.EXECUTIVE,
        ("enact_policy",),
    ),
    (
        "national_economy.register_revenue_source",
        "register_revenue_source",
        Branch.EXECUTIVE,
        ("open_account",),
    ),
    (
        "national_economy.register_public_asset",
        "register_public_asset",
        Branch.EXECUTIVE,
        ("book_expense",),
    ),
    (
        "national_economy.register_public_liability",
        "register_public_liability",
        Branch.EXECUTIVE,
        ("book_expense",),
    ),
    (
        "national_economy.authorize_expenditure",
        "authorize_expenditure",
        Branch.TREASURY,
        (),
    ),
    (
        "national_economy.authorize_procurement",
        "award_procurement",
        Branch.TREASURY,
        (),
    ),
    (
        "national_economy.authorize_transfer",
        "authorize_transfer",
        Branch.TREASURY,
        ("authorize_expenditure",),
    ),
    (
        "federal_state.execute_scoped_operation",
        "execute_scoped_operation",
        Branch.EXECUTIVE,
        ("execute_task",),
    ),
    (
        "national_economy.activate_policy",
        "activate_policy",
        Branch.EXECUTIVE,
        ("enact_policy",),
    ),
    (
        "national_economy.execute_economic_decision",
        "execute_economic_decision",
        Branch.EXECUTIVE,
        ("execute_task",),
    ),
    ("model_gateway.log_cost", "log_cost", Branch.EXECUTIVE, ("charge_model_invoke",)),
]


def _verdict(engine: ConstitutionalEngine, actor: Branch, action: str) -> str:
    v = engine.evaluate(
        ActionRequest(actor=actor, action=action, target="probe", channel="official")
    )
    d = str(getattr(v.decision, "value", v.decision)).upper()
    fired = sorted({x.rule_id for x in getattr(v, "violations", [])})
    return d if not fired else f"{d}{fired}"


def _row(engine: ConstitutionalEngine, action: str) -> dict[str, str]:
    return {a.name: _verdict(engine, a, action) for a in ACTORS}


def _owner(action: str) -> str:
    o = rules._exclusive_owner(action)
    if o is not None:
        return o.name
    if action in rules.NON_CONSTITUTIONAL_MONEY_ACTIONS:
        return "NON_CONSTITUTIONAL_MONEY"
    return "—"


def _apply_proposal() -> dict:
    saved = dict(rules._BRANCH_EXCLUSIVE), rules.NON_CONSTITUTIONAL_MONEY_ACTIONS
    rules._BRANCH_EXCLUSIVE[Branch.EXECUTIVE] = rules.EXECUTIVE_ACTIONS | frozenset(
        NEW_EXECUTIVE
    )
    rules._BRANCH_EXCLUSIVE[Branch.TREASURY] = rules.TREASURY_ACTIONS | frozenset(
        NEW_TREASURY
    )
    rules.NON_CONSTITUTIONAL_MONEY_ACTIONS = (
        rules.NON_CONSTITUTIONAL_MONEY_ACTIONS | frozenset(NEW_NON_CONSTITUTIONAL_MONEY)
    )
    return {"saved": saved}


def main() -> int:
    candidates = sorted(
        {s[1] for s in SURFACES} | {alt for s in SURFACES for alt in s[3]}
    )
    collisions = sorted(
        set(NEW_EXECUTIVE + NEW_TREASURY + NEW_NON_CONSTITUTIONAL_MONEY)
        & (
            set().union(*rules._BRANCH_EXCLUSIVE.values())
            | rules.NON_CONSTITUTIONAL_MONEY_ACTIONS
            | rules.HUMAN_GATED_ACTIONS
            | rules.MEMORY_DESTRUCTIVE_ACTIONS
            | rules.SELF_GOVERNANCE_ACTIONS
            | rules.KILL_SWITCH_TAMPER_ACTIONS
            | set().union(*rules.KILL_SWITCH_BLOCKS.values())
        )
    )
    print(
        f"NEW VERBS: executive={len(NEW_EXECUTIVE)} treasury={len(NEW_TREASURY)} "
        f"non_constitutional_money={len(NEW_NON_CONSTITUTIONAL_MONEY)} · collisions_with_existing_sets={collisions}"
    )
    print("ACTORS:", " ".join(a.name for a in ACTORS))
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        engine = ConstitutionalEngine(ledger_path=Path(tmp) / "ledger.jsonl")
        now = {c: (_owner(c), _row(engine, c)) for c in candidates}
        _apply_proposal()
        prop = {c: (_owner(c), _row(engine, c)) for c in candidates}
    for mode, table in (("NOW", now), ("PROPOSED", prop)):
        print(f"\n== {mode} ==")
        for c in candidates:
            owner, row = table[c]
            cells = " ".join(f"{a}={v}" for a, v in row.items())
            print(f"{mode:8} {c:28} owner={owner:24} {cells}")
    print("\n== SURFACES (proposed verb · proposed actor) ==")
    for surface, verb, actor, alts in SURFACES:
        n_owner, n_row = now[verb]
        p_owner, p_row = prop[verb]
        allow_now = [a for a, v in n_row.items() if v == "ALLOW"]
        allow_prop = [a for a, v in p_row.items() if v == "ALLOW"]
        ok = p_row[actor.name] == "ALLOW"
        bad += 0 if ok else 1
        alt_txt = (
            "; ".join(
                f"{alt}(owner={now[alt][0]} · {actor.name}={now[alt][1][actor.name]})"
                for alt in alts
            )
            or "—"
        )
        print(
            f"SURFACE {surface:44} verb={verb:26} actor={actor.name:9} "
            f"now: owner={n_owner} allow={len(allow_now)}/10 · proposed: owner={p_owner} "
            f"allow={allow_prop} · actor_allowed={'YES' if ok else 'NO'} · alternatives: {alt_txt}"
        )
    print(
        f"\nPROBE RESULT: surfaces={len(SURFACES)} candidates={len(candidates)} actor_denied={bad}"
    )
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
