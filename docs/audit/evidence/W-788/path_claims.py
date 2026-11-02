"""قياسُ مَن يحجزُ مساراتِ شِفرةِ WI-127 قبلَ حجزِه (W-788).

الهدف: أن تُعلَنَ القسمةُ (§ 6.1) من قياسٍ يُعادُ لا من ذاكرة. يُشغَّلُ من جذرِ المستودع.
"""

A = "docs/governance/work/ACTIVE_WORK.md"
S = "federal/executive/services/"
want = [
    S + "src/amos_federation/services/state_treasury/service.py",
    S + "src/amos_federation/services/national_economy/service.py",
    S + "src/amos_federation/services/federal_state/service.py",
    S + "src/amos_federation/services/federal_judiciary/service.py",
    S + "src/amos_federation/common/money_delegation.py",
    S + "tests/test_q19_money_delegation.py",
    S + "tests/test_q31_money_engine_wiring.py",
    S + "tests/test_q32_money_enforcement_surface.py",
    "docs/audit/M1_MONEY_CROSSING_DESIGN.md",
    "docs/audit/evidence/W-784",
    "docs/audit/evidence/W-785",
]
claiming = {"RESERVED", "IN_PROGRESS", "IN_REVIEW", "VERIFIED", "BLOCKED"}
rows = [ln.split("|") for ln in open(A, encoding="utf-8") if ln.startswith("| WI-")]
for w in want:
    hits = []
    for c in rows:
        ps = [p.strip().rstrip("/") for p in c[7].split("·")]
        if any(p and (w == p or w.startswith(p + "/")) for p in ps):
            st = c[6].strip()
            hits.append(f"{c[1].strip()} {st}{' (حاجز)' if st in claiming else ''}")
    print(w, "→", " · ".join(hits) or "لا بندَ يُعلِنُه")
