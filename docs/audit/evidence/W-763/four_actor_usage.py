"""قياسٌ ساكنٌ لاستعمالِ الفاعلين HUMAN وSTATE وINSTITUTION (وROYAL) في شِفرةِ الإنتاج (W-763 · التوجيهُ 35 § 1 «الفاعلون الأربعة»).

الهدف: أن يسبقَ القياسُ التصميمَ والشِّفرةَ (بندُ C4): أين يُبنى فاعلٌ من هذه الأربعةِ في الإنتاجِ، وأين يدخلُ اسمُه نصًّا.
النطاق: ملفّاتُ `.py` خارجَ `tests/` و`docs/` و`.venv` · قراءةٌ فقط · لا يستورد شِفرةَ المشروع.
المالك: Perplexity Computer (قيدُ W-763 · البندُ WI-109).
التشغيل (من جذرِ المستودع): python3 docs/audit/evidence/W-763/four_actor_usage.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKIP = ("tests", "docs", ".venv", ".git", "node_modules", "__pycache__")
ACTORS = ("HUMAN", "STATE", "INSTITUTION", "ROYAL")
ENUM_USE = re.compile(r"\bBranch\.(HUMAN|STATE|INSTITUTION|ROYAL)\b")
DYNAMIC = re.compile(r"Branch\[|Branch\(|choices=\[?[^\n]*Branch")


def production_files() -> list[Path]:
    out = []
    for p in sorted(ROOT.rglob("*.py")):
        rel = p.relative_to(ROOT).parts
        if any(part in SKIP or part.startswith("test") for part in rel):
            continue
        out.append(p)
    return out


counts = {a: 0 for a in ACTORS}
sites: dict[str, list[str]] = {a: [] for a in ACTORS}
dynamic: list[str] = []
files = production_files()
for p in files:
    rel = p.relative_to(ROOT).as_posix()
    for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        for m in ENUM_USE.finditer(line):
            counts[m.group(1)] += 1
            sites[m.group(1)].append(f"{rel}:{n}")
        if DYNAMIC.search(line):
            dynamic.append(f"{rel}:{n}: {line.strip()[:110]}")

print(f"ملفّاتُ الإنتاجِ المفحوصة: {len(files)}")
for a in ACTORS:
    print(f"\nBranch.{a}: {counts[a]} موضعًا")
    for s in sites[a]:
        print(f"  {s}")
print(f"\nبناءٌ ديناميكيٌّ للفاعل (Branch[...] / Branch(...) / choices من Branch): {len(dynamic)}")
for d in dynamic:
    print(f"  {d}")

# اسمُ الفاعلِ نصًّا قربَ actor/branch (يدخلُ إلى Branch[...] في sovereignty_bridge مثلًا)
LITERAL = re.compile(r"[\"'](HUMAN|STATE|INSTITUTION)[\"']")
literal_sites = []
for p in files:
    rel = p.relative_to(ROOT).as_posix()
    for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if LITERAL.search(line) and re.search(r"actor|branch", line, re.I):
            literal_sites.append(f"{rel}:{n}: {line.strip()[:110]}")
print(f"\nاسمُ HUMAN/STATE/INSTITUTION نصًّا قربَ actor/branch: {len(literal_sites)}")
for s in literal_sites:
    print(f"  {s}")
