"""أعمارُ البنودِ بلا مراجعةٍ — تُحسَبُ بأداةٍ من تاريخِ git لا يدويًّا (التوجيهُ 36 § 3 · W-764).

الهدف: لكلِّ بندٍ حالتُه الآن `IN_REVIEW` أو `IN_PROGRESS` في `ACTIVE_WORK.md`، يُقرأُ أوّلُ التزامٍ على
       الخطِّ الأوّلِ لـ`main` ظهرَ فيه صفُّ البندِ بهذه الحالة (ومنه تاريخُ الانتقال)، ثمَّ يُحسَبُ العمرُ
       بالأيّامِ إلى يومِ القياس. والدمجُ في هذا المستودعِ تقديمٌ سريعٌ فتاريخُ الالتزامِ أقربُ ما يُقرأُ
       لتاريخِ دخولِه `main` — وتاريخُ الدفعِ نفسُه لا يحفظُه git، وهذا مُعلَنٌ لا مستور.
النطاق: قراءةٌ فقط · `git log --first-parent <ref> -- docs/governance/work/ACTIVE_WORK.md` و`git show` · لا شبكة.
المالك: Perplexity Computer (قيدُ W-764 · البندُ WI-125).
التشغيل (من جذرِ المستودع): python3 docs/audit/evidence/W-764/review_ages.py [--ref origin/main] [--today YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import re
import subprocess
from datetime import date, datetime, timezone

PATH = "docs/governance/work/ACTIVE_WORK.md"
STATUSES = ("IN_REVIEW", "IN_PROGRESS")


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=True
    ).stdout


def _rows(text: str, *, field: int = 5) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        if line.startswith("| WI-"):
            cells = line.split(" | ")
            if len(cells) > field:
                out[cells[0][2:].strip()] = cells[field].strip()
    return out


def _wid(subject: str) -> str:
    m = re.match(r"(W-\d+(?:-[^\s:·]+)?)", subject)
    return m.group(1) if m else subject[:20]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/main")
    ap.add_argument("--today", default=datetime.now(timezone.utc).date().isoformat())
    a = ap.parse_args()
    today = date.fromisoformat(a.today)
    text_now = _git("show", f"{a.ref}:{PATH}")
    now = _rows(text_now)
    registered = _rows(text_now, field=7)  # عمودُ «بدأ» — تاريخُ التسجيلِ لا الانتقال
    wanted = {wid: st for wid, st in now.items() if st in STATUSES}
    log = _git(
        "log", "--first-parent", "--reverse", "--format=%H %cI %s", a.ref, "--", PATH
    ).splitlines()
    first_seen: dict[str, tuple[str, str]] = {}
    first_ever: dict[str, tuple[str, str]] = {}
    previous: dict[str, str] = {}
    for line in log:
        sha, stamp, subject = line.split(" ", 2)
        rows = _rows(_git("show", f"{sha}:{PATH}"))
        for wid, st in rows.items():
            if wid in wanted and st == wanted[wid] and previous.get(wid) != st:
                # آخرُ دخولٍ إلى الحالةِ الحاليّة (لو خرجَ ثمَّ عادَ يُحسَبُ الدخولُ الأخير)
                first_seen[wid] = (stamp[:10], _wid(subject))
                first_ever.setdefault(wid, first_seen[wid])
        previous = rows
    print(
        f"المرجع: {a.ref} ({_git('rev-parse', '--short', a.ref).strip()}) · يومُ القياس: {today} · التزاماتٌ مقروءة: {len(log)}"
    )
    print(
        "| البند | الحالة | التسجيل (بدأ) | أوّلُ دخولٍ إلى الحالة | القيد | العمرُ منه | "
        "آخرُ دخولٍ إلى الحالة | القيد | العمرُ منه |"
    )
    print("|---|---|---|---|---|---|---|---|---|")
    ranked = sorted(wanted, key=lambda w: first_seen.get(w, ("9999-12-31", ""))[0])
    for wid in ranked:
        d, w = first_seen.get(wid, ("?", "?"))
        d0, w0 = first_ever.get(wid, ("?", "?"))
        age = (today - date.fromisoformat(d)).days if d != "?" else "?"
        age0 = (today - date.fromisoformat(d0)).days if d0 != "?" else "?"
        reg = registered.get(wid, "?")
        print(
            f"| {wid} | {wanted[wid]} | {reg} | {d0} | {w0} | {age0} | {d} | {w} | {age} |"
        )
    counts = {s: sum(1 for v in wanted.values() if v == s) for s in STATUSES}
    print(
        f"المجموع: IN_REVIEW={counts['IN_REVIEW']} · IN_PROGRESS={counts['IN_PROGRESS']}"
    )


if __name__ == "__main__":
    main()
