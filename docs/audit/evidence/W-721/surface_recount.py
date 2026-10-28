"""إعادةُ عدِّ أسطحِ G1 بعدَ تعديلاتِ التوجيهِ 27 — قراءةٌ فقط.

الهدف: إعادةُ عدِّ أسطحِ G1 بعدَ استثناءاتِ التوجيهِ 27 من حمولةِ أداةِ الجرد
النطاق: قراءةٌ فقط — لا كتابةَ في ملفٍّ ولا قاعدة
المالك: W-721
تاريخ الإنشاء: 2026-10-28

المصدرُ: `docs/audit/measurements/write_inventory_p13.json` (مخرجُ أداةِ الجردِ).
يُعَدُّ السطحُ: موقعٌ عامٌّ (public) غيرُ محروسٍ وغيرُ مغلقٍ في `services/governance/`.
المستثنى بالتوجيه 27: (أ) store_secret · restore_backup ⇒ دَين · (ب) treasury.py كلُّه ⇒ M1.
"""

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = json.loads(
    (ROOT / "docs/audit/measurements/write_inventory_p13.json").read_text(
        encoding="utf-8"
    )
)
DEBT = {"store_secret", "restore_backup"}
by_file: dict[str, list[str]] = defaultdict(list)
for site in DATA["sites"]:
    path = site["path"]
    if "/services/governance/" not in path:
        continue
    if not site.get("public") or site.get("guarded") or site.get("closed_legacy"):
        continue
    by_file[Path(path).name].append(site["function"])
total = sum(len(v) for v in by_file.values())
print(f"أسطحُ الحوكمةِ العامّةُ المفتوحةُ: {total}")
for name in sorted(by_file):
    print(f"  {name}: {len(by_file[name])} — {' · '.join(sorted(by_file[name]))}")
treasury = len(by_file.get("treasury.py", []))
debt = sum(1 for v in by_file.values() for f in v if f in DEBT)
print(
    f"المستثنى: treasury ⇒ M1 = {treasury} · دَينٌ (store_secret/restore_backup) = {debt}"
)
print(f"المتبقّي لـ G1 = {total - treasury - debt}")
batches = {
    "state_runtime+system_life": ["state_runtime.py", "system_life.py"],
    "expansion": ["expansion.py"],
    "learning_cycle+security": ["learning_cycle.py", "security.py"],
}
for label, files in batches.items():
    count = sum(1 for f in files for fn in by_file.get(f, []) if fn not in DEBT)
    print(f"  دفعة {label}: {count}")
