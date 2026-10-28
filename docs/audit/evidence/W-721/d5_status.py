"""قياسُ D-5: حالةُ Q-1…Q-27 كما هي مكتوبةٌ في السجلِّ السياديّ (قراءةٌ فقط)

الهدف: عدُّ ما في سجلِّ القراراتِ من حسمٍ لـQ-1…Q-27 بقاعدةٍ مكتوبةٍ لا بتقدير
النطاق: docs/audit/SOVEREIGN_DECISION_REGISTER.md — قراءةٌ فقط، لا كتابة
المالك: W-721
تاريخ الإنشاء: 2026-10-28

القاعدة: تُجمَعُ كلُّ أقسامِ `## Q-n ·` للرقمِ نفسِه (الأصلُ وذيولُه)، ويُعَدُّ السؤالُ
«محسومًا» إن ظهرَ فيها رمزٌ من DECIDED · RESOLVED_* (غيرَ PARTIALLY_*)، **أو** ظهرَ
`Q-n` بحدِّه في سطرٍ واحدٍ معَ رمزٍ منها في أيِّ موضعٍ من السجلّ (جداولُ القراراتِ
المجمَّعةُ وعناوينُ «القرارُ البشريُّ في Q-n») غيرَ سطرِ «تاريخ آخر تعديل»، **أو** كانَ
صفًّا يبدأُ بـ `| **Q-n**` أو `| Q-n |` تحتَ عنوانٍ `##`/`###` يحملُ DECIDED. وإلّا فحالتُه أوّلُ «**الحالة: X**» فيه.
«منفَّذٌ في الكود» لا يُقاسُ هنا — والقاعدةُ قد تُخطئُ بالزيادةِ على سطرٍ يذكرُ رقمينِ.
"""

import re
from collections import defaultdict
from pathlib import Path

TEXT = Path("docs/audit/SOVEREIGN_DECISION_REGISTER.md").read_text(encoding="utf-8")
sections: dict[int, list[str]] = defaultdict(list)
for part in re.split(r"\n(?=## Q-\d+ )", TEXT):
    head = re.match(r"## Q-(\d+) ", part)
    if head and int(head.group(1)) <= 27:
        sections[int(head.group(1))].append(part)

decided, other, why = [], defaultdict(list), {}
LINES = TEXT.splitlines()
UNDER_DECIDED: set[int] = set()
heading_decided = False
for line in LINES:
    if line.startswith("#"):
        heading_decided = "DECIDED" in line
    row = re.match(r"\|\s*\**Q-(\d+)\**\s*\|", line)
    if heading_decided and row:
        UNDER_DECIDED.add(int(row.group(1)))
for number in range(1, 28):
    body = "\n".join(sections.get(number, []))
    status_re = r"(?<!PARTIALLY_)(?:\bDECIDED\b|\bRESOLVED\w*)"
    named = re.compile(rf"(?<![\w-])Q-{number}(?!\d)")
    hits = [
        i + 1
        for i, line in enumerate(LINES)
        if named.search(line)
        and re.search(status_re, line)
        and not line.startswith("تاريخ آخر تعديل")
    ]
    if re.search(status_re, body) or hits or number in UNDER_DECIDED:
        decided.append(number)
        why[number] = (
            ("قسمُه" if re.search(status_re, body) else "")
            + (f" · أسطر {hits[:3]}" if hits else "")
            + (" · صفٌّ تحتَ عنوانٍ DECIDED" if number in UNDER_DECIDED else "")
        )
    else:
        first = re.search(r"\*\*الحالة: `?([A-Z_]+)", body)
        other[first.group(1) if first else "NO_STATUS_LINE"].append(number)

print(f"محسومٌ مكتوبًا: {len(decided)} / 27 — " + " · ".join(f"Q-{n}" for n in decided))
for number in decided:
    print(f"  Q-{number}: {why[number]}")
for status, numbers in sorted(other.items()):
    print(f"{status}: {len(numbers)} — " + " · ".join(f"Q-{n}" for n in numbers))
