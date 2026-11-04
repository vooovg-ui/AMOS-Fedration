"""تصنيفُ مواضعِ D-4 المقيسةِ بحاجزِها (W-813 · التوجيه 40 § 2 بند 1).

يقرأُ مخرجَ الجردِ كما هو (لا يُعدِّلُ الأداةَ ولا التعريف) ويُصنِّفُ كلَّ موضعٍ
غيرِ عابرٍ بصنفِ المنطقةِ (service_common · services · tools · core) وبحاجزِه
المُسمّى في وثائقِ المشروع. الموضعُ الذي لا قاعدةَ له هنا يُطبَعُ «غيرَ مصنَّف»
ويُسقِطُ الأمرَ (EXIT=1) — فلا يُخفى موضعٌ جديدٌ تحتَ صنفٍ قديم.

الاستعمال:
    python tools/audit/sovereign_write_inventory.py --root . --json /tmp/inv.json
    python docs/audit/evidence/W-813/classify_d4.py /tmp/inv.json
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict

# (المسارُ الجزئي، المالكُ، الدالّة) ← (الحاجز، هل يُحرَقُ الآنَ بلا قرار؟)
# None في المالك/الدالّة = أيُّ قيمة.
RULES: list[tuple[str, str | None, set[str] | None, str]] = [
    ("services/royal/main.py", None, None, "K1 — ممنوعُ المَسّ (Q-4)"),
    (
        "common/durable_event_bus.py",
        "DurableEventBus",
        {"ack"},
        "DISC-156 → دَينٌ مسمّى (Q-95 قرار 1)",
    ),
    (
        "common/persistent.py",
        "PersistentTaskStore",
        {"create", "update_status"},
        "DISC-156 → دَينٌ مسمّى (Q-95 قرار 1)",
    ),
    (
        "common/persistent.py",
        "PersistentMemoryStore",
        {"store"},
        "Q-87 (ج-2) — عبورٌ عندَ المستدعي بعدَ M1",
    ),
    (
        "common/persistent.py",
        "PersistentExperienceStore",
        {"record"},
        "Q-87 (ج-2) — عبورٌ عندَ المستدعي بعدَ M1",
    ),
    (
        "common/persistent.py",
        None,
        None,
        "A1 — العبورُ عندَ المستدعي لا يُنقِصُ D-4 (Q-75 ①) · العبورُ داخلَ المخزنِ غيرُ مقرَّر",
    ),
    (
        "services/api_gateway/store.py",
        "DatabaseTaskStore",
        {"create"},
        "DISC-157 — بلا مستدعٍ إنتاجيٍّ وتقومُ عليه فحوص (نمطُ DISC-156)",
    ),
    (
        "services/federal_judiciary/",
        None,
        {"enforce_ruling_via_treasury"},
        "DISC-155 — حرّاسُ Q-19/Q-31/Q-32",
    ),
    (
        "services/federal_judiciary/",
        None,
        {"enforce_ruling_via_task", "record_enforcement"},
        "J4 — Q-16 + جولةُ WI-084 (D30: لا نصاب)",
    ),
    (
        "services/federal_judiciary/",
        None,
        None,
        "D17-2 / D21-أ بند 9 — الأفعالُ الأربعةُ مؤجَّلة",
    ),
    (
        "services/federal_state/service.py",
        None,
        {"execute_scoped_disbursement"},
        "M1 § 2.11 — عابرٌ بصيغة S1 والجردُ لا يراه (توسيعُ الجردِ تصميمٌ مستقلٌّ للمالك)",
    ),
    (
        "services/federal_state/service.py",
        None,
        {"execute_scoped_operation"},
        "Q-83 (أ)① + (ج) — مركَّبُ النواة (M1 الدفعة 4)",
    ),
    (
        "services/federal_state/service.py",
        None,
        None,
        "Q-83 (ج) — معجمُ الأسطحِ العشرين (M1 الدفعة 3)",
    ),
    (
        "services/national_economy/service.py",
        None,
        {"execute_expenditure", "execute_transfer"},
        "M1 § 2.11 — عابرٌ بصيغة S1 والجردُ لا يراه (توسيعُ الجردِ تصميمٌ مستقلٌّ للمالك)",
    ),
    (
        "services/national_economy/service.py",
        None,
        {"activate_policy", "execute_economic_decision"},
        "Q-83 (أ)① + (ج) — مركَّبُ النواة (M1 الدفعة 4)",
    ),
    (
        "services/national_economy/service.py",
        None,
        None,
        "Q-83 (ج) — معجمُ الأسطحِ العشرين (M1 الدفعة 3)",
    ),
    (
        "services/governance/treasury.py",
        None,
        None,
        "G1 § 9.2 — مالٌ متعشِّشٌ (Q-9) · بعدَ كاشفِ التعشيشِ وM1 وجولةٍ بأعلى فئة (D30)",
    ),
    (
        "services/state_treasury/service.py",
        None,
        {"reverse_transaction"},
        "M1 § 2.9 قرار 1 — معوِّضُ العكسِ سؤالٌ للمالك",
    ),
    (
        "services/governance/learning_cycle.py",
        None,
        {"start_training"},
        "Q-80 ① — دَينٌ حتى قناةِ الموافقةِ البشريّة",
    ),
    (
        "services/training/persistent_registry.py",
        None,
        None,
        "أفعالٌ بشريّةُ البوّابة (train_model · promote_model) — قناةُ الموافقةِ نفسُها (Q-80 ①) · غيرُ مقيسٍ بمسبارِ المحرّكِ هنا",
    ),
    (
        "services/governance/security.py",
        None,
        {"store_secret"},
        "G1 § 9.1 — تصميمٌ مستقلٌّ (المعوِّضُ يضعُ سرًّا في الأثر)",
    ),
    (
        "services/governance/system_life.py",
        None,
        {"restore_backup"},
        "G1 § 9.1 + Q-10 BLOCKED — لا قدرةَ استرجاع",
    ),
    (
        "services/government_services/service.py",
        None,
        {"process_case"},
        "Q-16 ③ — DECIDED · التنفيذُ BLOCKED حتى الشرطين",
    ),
    (
        "services/model_gateway/model_layer.py",
        None,
        {"log_cost"},
        "مشتقُّ مالٍ — بعدَ الأصل (حزمةُ القرار W2 · Q-83 (ج))",
    ),
    (
        "services/model_gateway/model_layer.py",
        None,
        {"set_cached"},
        "Q-25 ① — فئةُ INFRASTRUCTURE: إعادةُ تصنيفٍ لا حرق",
    ),
    (
        "tools/migrations/r4_unify_agent_identity.py",
        None,
        {"emit_sql"},
        "إيجابٌ كاذبٌ في الجرد — تُعيدُ نصَّ SQL ولا تكتب · إصلاحُ الأداةِ إعادةُ تصنيفٍ بقرارِ المالك",
    ),
]


def zone(path: str) -> str:
    if path.startswith("core/"):
        return "core"
    if path.startswith("tools/"):
        return "tools"
    if "/common/" in path:
        return "service_common"
    return "services"


def classify(site: dict) -> str | None:
    for frag, owner, funcs, blocker in RULES:
        if frag not in site["path"]:
            continue
        if owner is not None and site.get("owner") != owner:
            continue
        if funcs is not None and site.get("function") not in funcs:
            continue
        return blocker
    return None


def main(argv: list[str]) -> int:
    data = json.load(open(argv[1], encoding="utf-8"))
    debt = [
        s
        for s in data["sites"]
        if s.get("public")
        and (s.get("writes") or s.get("writes_via"))
        and not s.get("guarded")
        and not s.get("closed_legacy")
        and not s.get("declared_boundary")
    ]
    # الموضعُ الواحدُ قد يتكرّرُ بمواقعِ كتابةٍ متعدّدة؛ العدُّ بالعمليّة (المسار·المالك·الدالّة).
    ops: dict[tuple[str, str, str], dict] = {}
    for s in debt:
        ops.setdefault((s["path"], s.get("owner") or "-", s["function"]), s)
    by_zone: Counter[str] = Counter()
    by_blocker: dict[str, list[str]] = defaultdict(list)
    unclassified = []
    for (path, owner, func), s in sorted(ops.items()):
        z = zone(path)
        by_zone[z] += 1
        b = classify(s)
        name = f"{z} · {path.split('amos_federation/')[-1]}::{owner}.{func}"
        if b is None:
            unclassified.append(name)
        else:
            by_blocker[b].append(name)
    print(f"D-4 (عمليّاتٌ عامّةٌ كاتبةٌ غيرُ عابرة) = {len(ops)}")
    print(
        "بالمنطقة: "
        + " · ".join(
            f"{z} {by_zone[z]}" for z in ("service_common", "services", "tools", "core")
        )
    )
    print()
    for b, names in sorted(by_blocker.items(), key=lambda kv: -len(kv[1])):
        print(f"[{len(names)}] {b}")
        for n in names:
            print(f"      {n}")
    print()
    print(f"غيرُ مصنَّف = {len(unclassified)}")
    for n in unclassified:
        print(f"      {n}")
    return 1 if unclassified else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
