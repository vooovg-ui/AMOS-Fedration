"""الهدف: P14 — تدقيقٌ نهائيٌّ يُطابِقُ المستودعَ بالوثيقة. يقيسُ ولا يُصلِحُ.

طريقُ الإنفاذ: NEEDS_RUN_INPUT — يقرأُ مسارَ المستودعِ من `sys.argv[1]` ويسقُطُ بلا مُدخَلٍ (قِيسَ: 0.19ث · يطبعُ JSON)
"""

import json
import re
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "docs/audit"
# المادةُ التاسعةُ · 2: المُخرَجُ يُعلِنُ هدفَه في ترويستِه، والمفتاحُ أوّلُ ما يُكتَب.
out: dict[str, object] = {
    "$comment": (
        "الهدف: 21 قياسَ مطابقةٍ بينَ ما يقولُه المستودعُ وما تقولُه الوثيقةُ — "
        "مُخرَجُ tools/audit/final_audit.py (P14). يقيسُ ولا يُصلِح، ولا يُقرَأُ "
        "شهادةَ نجاح. المادةُ التاسعةُ · 2."),
}

# 1) الدَّينُ المقيسُ الآن
INV = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "docs/audit/measurements/write_inventory_p13.json"
inv = json.loads(INV.read_text(encoding="utf-8"))
s = inv["summary"]
debt = len([x for x in inv["sites"] if x["public"] and not x["guarded"] and not x["closed_legacy"]])
out["debt_summary_field"] = s["non_sovereign_write_operations"]
out["debt_recount"] = debt
out["sovereign"] = s["sovereign_write_operations"]
out["closed_legacy"] = s["closed_legacy_paths"]
out["public"] = s["public_write_operations"]
out["total_sites"] = s["write_sites_total"]

# 2) الأرقامُ المذكورةُ في الوثيقةِ المركزيّة
prog = (D / "SOVEREIGN_MIGRATION_PROGRAM.md").read_text(encoding="utf-8")
out["program_mentions_168"] = prog.count("168")
# صيغتانِ للعلامةِ المؤقّتةِ: عبارةُ P14 ورمزُ P15/P16 — عُدَّتِ الأولى وحدَها
# حتى P16 فكانَ العدُّ أعمى عن الثانية، فوُسِّعَ صريحًا لا صامتًا.
# تُعَدُّ العلامةُ في **خليّةِ جدولٍ** لا في شرحٍ نصّيٍّ يذكرُ الرمزَ: وسَّعْنا العدَّ
# في P16 فعَدَّ ذكرَ الرمزِ في § 8.5 علامةً باقيةً (3 لا 2)، فضُيِّقَ صريحًا.
out["program_placeholders"] = (prog.count("يُسجَّلُ عند الدفع")
                               + len(re.findall(r"\|\s*`PENDING_PUSH`\s*\|", prog)))
out["program_todo_markers"] = len(re.findall(r"TODO|FIXME|XXX|<<<|>>>", prog))

# 3) الأسئلةُ في السجلّ
reg = (D / "SOVEREIGN_DECISION_REGISTER.md").read_text(encoding="utf-8")
qs = sorted({int(m) for m in re.findall(r"##\s+\**Q-(\d+)", reg)})
out["questions_headed"] = qs
out["questions_count"] = len(qs)
out["questions_missing_1_to_max"] = [n for n in range(1, (max(qs) if qs else 0) + 1) if n not in qs]

# 4) وجودُ الوثائقِ المُدَّعاة
claimed = [
    "SOVEREIGN_MIGRATION_PROGRAM.md", "SOVEREIGN_DECISION_REGISTER.md",
    "MIGRATION_DEBT_INVENTORY.md", "STATE_RUNTIME_MIGRATION_ANALYSIS.md",
    "AGENT_IDENTITY_MIGRATION_ANALYSIS.md", "TREASURY_MIGRATION_ANALYSIS.md",
    "JUDICIARY_LEGISLATIVE_MIGRATION_ANALYSIS.md",
    "GOVERNANCE_NESTING_MIGRATION_ANALYSIS.md",
    "ROYAL_SYSTEM_LIFE_MIGRATION_ANALYSIS.md",
    "REMAINING_SURFACES_INVENTORY.md", "STAGE_2B_HANDOFF.md",
    "measurements/README.md", "measurements/treasury_gate_matrix.json",
    "measurements/judicial_gate_matrix.json",
    "evidence/README.md", "evidence/evidence_registry.jsonl",
]
out["missing_docs"] = [c for c in claimed if not (D / c).exists()]

# 5) الأدواتُ المُدَّعاة
tools = [
    "tools/audit/sovereign_write_inventory.py", "tools/audit/treasury_gate_probe.py",
    "tools/audit/judicial_gate_probe.py", "tools/governance/evidence_registry.py",
    "tools/governance/truth_audit.py",
    "tools/audit/final_audit.py",
]
out["missing_tools"] = [t for t in tools if not (ROOT / t).exists()]

# 6) الهاشاتُ المذكورةُ في الوثيقةِ: أموجودةٌ في تاريخِ الفرع؟
#
# ثلاثةُ أعطابٍ قِيسَت في W-052 وأُصلِحَت هنا، وكانت كلُّها تكذبُ في الاتّجاهِ
# المُطمئِنِ أو تشتكي بلا حقيقة:
#
# ١) نافذةٌ مقطوعةٌ: كانَ الحكمُ يُبنى على `git log -n 400`، فبصمةٌ أقدمُ من
#    أحدثِ 400 التزامٍ تُعَدُّ «ليست في السجلِّ» وهي فيه. وهذه الهشاشةُ كانت
#    **مُعلَنةً** في قيدِ نَسَبِ هذا القياسِ منذُ W-037 («عندَها تُوسَّعُ النافذةُ
#    أو يُراجَعُ تعريفُ الحقلِ، والعدُّ يومَ القيدِ 243 التزامًا»). فلا تُوسَّعُ
#    النافذةُ إلى رقمٍ أكبرَ — لأنَّ رقمًا أكبرَ يُؤجِّلُ الكذبَ ولا يمنعُه — بل
#    تُرفَعُ النافذةُ كلُّها: السجلُّ يُقرَأُ بعمقِه التامّ.
# ٢) طولُ الاختصارِ ليس عقدًا: `%h` يُختصَرُ بطولٍ يزيدُ بنموِّ عددِ الكائناتِ
#    (`core.abbrev=auto`)، وكانَ الحكمُ مُطابَقةً نصّيّةً تامّةً بسبعةِ محارفَ.
#    فيومَ يُختصِرُ git بثمانيةٍ، تُعَدُّ **كلُّ** بصمةٍ في الوثيقةِ مفقودةً. فصارَ
#    السجلُّ يُقرَأُ بالبصمةِ التامّةِ (`%H`) والحكمُ بالبادئة.
# ٣) قاعدةُ الاستخراجِ كانت تُلزِمُ سبعةَ محارفَ **بالضبط**، فبصمةٌ تامّةٌ (40)
#    مذكورةٌ في الوثيقةِ لا تُفحَصُ أصلًا. وقِيسَ في W-052 أنَّ في الوثيقةِ
#    بصمتَينِ تامّتَينِ (رأسُ `origin/main` ورأسُ الشجرةِ المحلّيّةِ قبلَ المواءمة)
#    كانتا خارجَ القياسِ كلِّه: 41 مفحوصةً من 43 مذكورة.
HASH_IN_DOC_RE = re.compile(r"`([0-9a-f]{7,40})`")
hashes = sorted(set(HASH_IN_DOC_RE.findall(prog)))


def _refuse(reason: str) -> None:
    """لا يُطبَعُ قياسٌ لم يُقَسْ: الرفضُ يُعلَنُ ويُخرَجُ به بالرمز 2.

    قياسٌ يعتمدُ على سجلٍّ غائبٍ أو منقوصٍ فيُخرِجُ قائمةً فارغةً — يُقرَأُ
    «لا بصمةَ مفقودةً» وحقيقتُه «لم تُقَسْ بصمةٌ». وهذا هو الابتلاعُ الصامتُ
    الذي مُنِعَ في W-027، فلا يُكرَّرُ في أداةِ قياسٍ.
    """
    print(f"REFUSED: {reason}", file=sys.stderr)
    raise SystemExit(2)


_shallow = subprocess.run(["git", "rev-parse", "--is-shallow-repository"],
                          cwd=ROOT, capture_output=True, text=True)
if _shallow.returncode != 0:
    _refuse(
        f"لم يُقرأْ سجلُّ git في {ROOT}: "
        f"{_shallow.stderr.strip() or 'رمزُ خروجٍ ' + str(_shallow.returncode)}"
        " — الحكمُ على البصماتِ يحتاجُ سجلًّا، ولا يُستنتَجُ من غيابِه."
    )
if _shallow.stdout.strip() == "true":
    _refuse(
        "السجلُّ مبتورٌ (استنساخٌ ضحلٌ) — كلُّ بصمةٍ ستُعَدُّ مفقودةً بلا حقيقة. "
        "يُستنسَخُ بعمقٍ تامٍّ (`fetch-depth: 0`) ثمَّ يُعادُ القياس."
    )

_log = subprocess.run(["git", "log", "--format=%H"], cwd=ROOT,
                      capture_output=True, text=True)
if _log.returncode != 0:
    _refuse(
        "فشلَ `git log`: "
        f"{_log.stderr.strip() or 'رمزُ خروجٍ ' + str(_log.returncode)}"
    )
# ولا يُزادُ حرسٌ لسجلٍّ فارغٍ: جُرِّبَ في W-052 فكانَ فرعًا لا يُبلَغُ — `git log`
# نفسُه يُخرِجُ برمزٍ غيرِ صفرٍ على مستودعٍ بلا التزامٍ، فالرفضُ قائمٌ أعلاه.
# وحرسٌ لا يُبلَغُ فرعُه زينةٌ تُوهِمُ حمايةً (سابقةُ W-051).
history = _log.stdout.split()

out["hashes_in_doc"] = hashes
out["hashes_not_in_history"] = [
    h for h in hashes if not any(full.startswith(h) for full in history)
]

# 7) سلسلةُ الدليلِ: أسليمةٌ ولم تُمَسّ؟
lines = [json.loads(x) for x in (D / "evidence/evidence_registry.jsonl").read_text(
    encoding="utf-8").splitlines() if x.strip()]
out["evidence_entries"] = len(lines)
chain_ok, prev = True, None
for e in lines:
    if prev is not None and e.get("prev_hash") not in (prev, None):
        chain_ok = False
        break
    prev = e.get("hash", prev)
out["evidence_chain_consistent"] = chain_ok

# 8) مساراتُ التجاوزِ: هل بقيَ معامَلُ تجاوزٍ في الكتاباتِ المُهاجَرة؟
migrated = [
    "federal/executive/services/src/amos_federation/services/state_registry/service.py",
    "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
    "federal/executive/services/src/amos_federation/services/government_services/service.py",
    "federal/executive/services/src/amos_federation/services/governance/factories.py",
]
bad = {}
for m in migrated:
    src = (ROOT / m).read_text(encoding="utf-8")
    hits = [f for f in ("force=", "bypass=", "skip_check=", "unchecked=", "override=") if f in src]
    if hits:
        bad[m] = hits
out["bypass_params_in_migrated"] = bad
out["closed_legacy_functions"] = sorted(
    x["function"] for x in inv["sites"] if x["closed_legacy"]
)

# 9) الأفعالُ العابرةُ للحدِّ بأسمائِها
out["sovereign_sites"] = sorted(
    f"{Path(x['path']).name}::{x['function']}" for x in inv["sites"] if x["guarded"]
)

print(json.dumps(out, ensure_ascii=False, indent=2))
