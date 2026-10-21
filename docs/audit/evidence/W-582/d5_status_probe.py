"""
الهدف: قياسُ D-5 (Q-1…Q-27) بأمرٍ واحدٍ من نصِّ السجلِّ السياديِّ — أوّلُ حالةٍ في قسمِ كلِّ سؤالٍ وآخرُ حالةٍ مذكورةٍ فيه (الإضافاتُ المؤرَّخةُ) — وإظهارُ الفرقِ عن العدِّ اليدويِّ 15/27 (W-577) بلا ادّعاءِ أنّ أحدَهما الحاكمُ
النطاق: docs/audit/evidence/W-582 — قراءةٌ وحدَها لـdocs/audit/SOVEREIGN_DECISION_REGISTER.md
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — قيدُ W-582
تاريخ الإنشاء: 2026-10-21

التشغيل: python docs/audit/evidence/W-582/d5_status_probe.py
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

REG = Path("docs/audit/SOVEREIGN_DECISION_REGISTER.md")
STATUS = re.compile(r"`?\b(DECIDED|RESOLVED_[A-Z_]+|HUMAN_DECISION_REQUIRED|ANALYSIS_PENDING|PENDING_OWNER|OPEN_EXTERNAL[A-Z_]*)\b`?")
HEAD = re.compile(r"^## Q-(\d+) · ", re.M)
SETTLED = ("DECIDED", "RESOLVED_")


def main() -> int:
    text = REG.read_text(encoding="utf-8")
    heads = [(int(m.group(1)), m.start()) for m in HEAD.finditer(text)]
    sections: dict[int, str] = {}
    for i, (n, start) in enumerate(heads):
        end = heads[i + 1][1] if i + 1 < len(heads) else len(text)
        sections.setdefault(n, "")
        sections[n] += text[start:end]
    first_c: Counter[str] = Counter()
    last_c: Counter[str] = Counter()
    for n in range(1, 28):
        found = STATUS.findall(sections.get(n, ""))
        first = found[0] if found else "—"
        last = found[-1] if found else "—"
        first_c[first] += 1
        last_c[last] += 1
        print(f"Q-{n:<3} أوّلُ={first:<28} آخرُ={last}")
    settled = lambda c: sum(v for k, v in c.items() if k.startswith(SETTLED))
    print(f"\nبأوّلِ حالةٍ في القسم: محسومٌ {settled(first_c)}/27 · {dict(first_c)}")
    print(f"بآخرِ حالةٍ في القسم:  محسومٌ {settled(last_c)}/27 · {dict(last_c)}")
    print("المرجعُ اليدويُّ W-577: 15/27 (يستعملُ أيضًا مواضعَ خارجَ القسمِ — D16 § 1)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
