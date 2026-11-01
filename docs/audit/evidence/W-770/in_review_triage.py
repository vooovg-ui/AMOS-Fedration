#!/usr/bin/env python3
"""
فرزُ بنودِ IN_REVIEW قياسًا — عرضٌ للمالكِ لا انتقالُ حالة (قرارُ المالكِ Q-89 · القرارُ 2)

الهدف: لكلِّ بندٍ حالتُه في صفِّ ACTIVE_WORK «IN_REVIEW»: الرقم · الفئةُ C0–C4 · نوعُ
       مساراتِه (شِفرةُ إنتاجٍ أم أدواتٌ واختباراتٌ أم وثائق) · تاريخُ أوّلِ دمجٍ لشِفرةٍ
       من مساراتِه · هل له جولةُ مجلسٍ سابقةٌ في الأدلّة — ثمّ صنفُه (أ)/(ب)/(ج) بنصِّ
       القرار، و(د) لما لا يطابقُ نصَّ صنفٍ منها. ويُوفِّقُ بينَ عدِّ الصفوفِ (49)
       وعدِّ عناوينِ البطاقاتِ (20).
النطاق: قراءةٌ فقط: ACTIVE_WORK.md · OWNERSHIP.md § 1 · `git log --first-parent origin/main`
        · أسماءُ ملفّاتِ docs/audit/evidence وأسطرُها الأولى. لا يكتبُ في المستودع.
المالك: Perplexity Computer (WI-100 · قيدُ W-770 · التوجيهُ 37 § 1 القرارُ 2)
تاريخ الإنشاء: 2026-11-01 (W-770)
تاريخ آخر تعديل: 2026-11-01 (W-770 · المرّةُ الأولى)

الاستعمال: python3 docs/audit/evidence/W-770/in_review_triage.py [--ref origin/main] [--json PATH]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ACTIVE = ROOT / "docs" / "governance" / "work" / "ACTIVE_WORK.md"
OWNERSHIP = ROOT / "docs" / "governance" / "work" / "OWNERSHIP.md"
EVIDENCE = ROOT / "docs" / "audit" / "evidence"

#: نصُّ ACTIVE_WORK المقيس: الشجرةُ الحاضرةُ، أو `git show <REF>:…` بـ`--active-from`.
_ACTIVE_TEXT: list[str] = []


def active_text() -> str:
    return _ACTIVE_TEXT[0] if _ACTIVE_TEXT else ACTIVE.read_text(encoding="utf-8")


CLASS_RANK = {"C0": 0, "C1": 1, "C2": 2, "C3": 3, "C4": 4}


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=str(ROOT), capture_output=True, text=True, check=True
    ).stdout


def domain_classes() -> list[tuple[str, str, str]]:
    """(البادئة، النطاق، الفئة) من جدولِ OWNERSHIP § 1، الأطولُ أوّلًا."""
    text = OWNERSHIP.read_text(encoding="utf-8")
    section = text.split("## 1 ·", 1)[1].split("\n## 2", 1)[0]
    out: list[tuple[str, str, str]] = []
    for line in section.splitlines():
        if (
            not line.startswith("| ")
            or line.startswith("| النطاق")
            or line.startswith("|---")
        ):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        domain, paths, klass = cells[0], cells[1], cells[-1]
        for p in paths.split("·"):
            p = p.strip()
            if p and not p.startswith("—"):
                out.append((p, domain, klass))
    out.sort(key=lambda t: -len(t[0]))
    return out


def path_domain(path: str, table: list[tuple[str, str, str]]) -> tuple[str, str]:
    for prefix, domain, klass in table:
        if path == prefix or path.startswith(prefix.rstrip("/") + "/"):
            return domain, klass
    return "غيرُ مُسجَّل", "C0"


def path_kind(path: str) -> str:
    """إنتاج · أدوات · اختبارات · وثائق — بالمسارِ وحدَه."""
    if path.endswith(".md") or path.startswith("docs/") or path.endswith(".txt"):
        return "وثائق"
    name = Path(path).name
    if (
        path.startswith("tests/")
        or "/tests/" in path
        or name.startswith("test_")
        or name == "conftest.py"
    ):
        return "اختبارات"
    if path.startswith(("tools/", ".github/", "requirements")):
        return "أدوات"
    return "إنتاج"


def rows() -> list[list[str]]:
    out = []
    for line in active_text().splitlines():
        if line.startswith("| WI-"):
            out.append([c.strip() for c in line[2:-2].split(" | ")])
    return out


def cards() -> dict[str, dict[str, str]]:
    """لكلِّ بطاقةٍ `### WI-…`: سطرُ العنوانِ وأوّلُ سطرِ «الحالة:» بعدَه."""
    lines = active_text().splitlines()
    out: dict[str, dict[str, str]] = {}
    for i, line in enumerate(lines):
        m = re.match(r"^### (WI-\d{3})\b", line)
        if not m:
            continue
        status = ""
        for nxt in lines[i + 1 : i + 80]:
            if nxt.startswith("### "):
                break
            if nxt.startswith("الحالة:"):
                status = nxt
                break
        out.setdefault(m.group(1), {"header": line, "status": status})
    return out


def split_paths(cell: str) -> list[str]:
    return [
        p.strip().strip("`")
        for p in cell.split("·")
        if p.strip() and ("/" in p or "." in p)
    ]


def ledger_rows_added(ref: str) -> dict[str, str]:
    """sha ← نصُّ صفوفِ السجلِّ (`| W-### |`) التي أضافها ذلك الالتزامُ (الأبُ الأوّل)."""
    raw = _git(
        "log",
        "--first-parent",
        "--format=\x01%H",
        "-p",
        "-U0",
        ref,
        "--",
        "docs/audit/COMPLETION_LEDGER.md",
    )
    out: dict[str, str] = {}
    for block in raw.split("\x01")[1:]:
        sha, _, rest = block.partition("\n")
        added = [ln[1:] for ln in rest.splitlines() if ln.startswith("+| W-")]
        out[sha.strip()] = "\n".join(added)
    return out


def first_code_merge(
    wi: str,
    claimed: list[str],
    log: list[tuple[str, str, str, list[str]]],
    ledger_added: dict[str, str],
) -> tuple[str, str, str, str] | None:
    """أقدمُ التزامٍ على الأبِ الأوّلِ يذكرُ البندَ (في عنوانِه أو في صفِّ سجلٍّ أضافه) ويمسُّ
    ملفًّا غيرَ وثائقيٍّ من مساراتِه المُعلَنة. (sha، التاريخ، W-###، مصدرُ الذِّكر)."""
    pat = re.compile(rf"\b{re.escape(wi)}\b")
    code_claims = [c.rstrip("/") for c in claimed if path_kind(c) != "وثائق"]
    for sha, cdate, subject, files in log:  # الأقدمُ أوّلًا
        if pat.search(subject):
            source = "العنوان"
        elif pat.search(ledger_added.get(sha, "")):
            source = "صفُّ السجلّ"
        else:
            continue
        for f in files:
            if path_kind(f) == "وثائق":
                continue
            if any(f == c or f.startswith(c + "/") for c in code_claims):
                w = re.search(r"(W-\d{3,4})", subject) or re.search(
                    r"\| (W-\d{3,4}) \|", ledger_added.get(sha, "")
                )
                return sha[:8], cdate[:10], (w.group(1) if w else "—"), source
    return None


def first_parent_log(ref: str) -> list[tuple[str, str, str, list[str]]]:
    raw = _git(
        "log",
        "--first-parent",
        "--reverse",
        "--format=\x01%H\x02%cI\x02%s",
        "--name-only",
        ref,
    )
    out = []
    for block in raw.split("\x01")[1:]:
        head, _, rest = block.partition("\n")
        sha, cdate, subject = head.split("\x02", 2)
        files = [f for f in rest.splitlines() if f.strip()]
        out.append((sha, cdate, subject, files))
    return out


FAMILY = re.compile(
    r"^(?:briefing_|verdict_|brief_)?(kimi|grok|gemini|gpt|claude|deepseek|glm|qwen|mistral|llama)",
    re.IGNORECASE,
)


def _title_ids(readme: Path) -> set[str]:
    """معرِّفاتُ البنودِ في سطرِ العنوانِ الأوّلِ (`# …`) من بطاقةِ المجلّد."""
    if not readme.is_file():
        return set()
    with readme.open(encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("#"):
                ids = set(re.findall(r"WI-\d{3}", line))
                for lo, hi in re.findall(
                    r"WI-(\d{3})\s*(?:…|\.\.\.|–|-)\s*WI-(\d{3})", line
                ):
                    ids |= {f"WI-{n:03d}" for n in range(int(lo), int(hi) + 1)}
                return ids
    return set()


def _head_ids(path: Path, lines: int = 12) -> set[str]:
    """معرِّفاتُ البنودِ في الأسطرِ الأولى من ملفِّ جولة (مع مدى «WI-068…WI-074»)."""
    with path.open(encoding="utf-8", errors="replace") as fh:
        head = "".join(next(fh, "") for _ in range(lines))
    ids = set(re.findall(r"WI-\d{3}", head))
    for lo, hi in re.findall(r"WI-(\d{3})\s*(?:…|\.\.\.|–)\s*WI-(\d{3})", head):
        ids |= {f"WI-{n:03d}" for n in range(int(lo), int(hi) + 1)}
    return ids


def prior_rounds() -> dict[str, set[str]]:
    """البندُ ← «W-### (أحكام|إحاطات)» لكلِّ مجلّدِ أدلّةٍ فيه أثرُ جولة.

    مجلّدُ جولةٍ = فيه ملفٌّ باسمِ عائلةِ نموذجٍ (kimi_k3.md · briefing_gpt_….md …) أو
    advisory_review* أو verdict*. وموضوعُه = البنودُ في عنوانِ بطاقتِه (أو بطاقةِ أقربِ
    أبٍ لها بطاقة) + رموزُ wiNNN في مسارِه. «أحكام» إن كانَ فيه ملفُّ مقعدٍ أو حكمٍ لا
    إحاطةً فحسب، وإلّا «إحاطات» (جولةٌ أُعِدَّت ولا يثبتُ هنا أنّها جرت).
    """
    out: dict[str, set[str]] = {}
    dirs = {f.parent for f in EVIDENCE.rglob("*") if f.is_file()}
    for d in sorted(dirs):
        names = [f.name for f in d.iterdir() if f.is_file()]
        seat = [
            n
            for n in names
            if FAMILY.match(n)
            and n.endswith(".md")
            and not n.lower().startswith(("briefing", "brief_"))
        ]
        verdict = [
            n
            for n in names
            if re.search(r"verdict|advisory_review", n, re.IGNORECASE)
            and n.endswith(".md")
            and not re.search(r"(^|[_.-])ci([_.-]|$)|jobs", n, re.IGNORECASE)
        ]
        brief = [n for n in names if re.match(r"(briefing|brief_)", n, re.IGNORECASE)]
        if not (seat or verdict or brief):
            continue
        rel = d.relative_to(EVIDENCE)
        ids = {
            f"WI-{n}" for n in re.findall(r"wi[-_]?(\d{3})", str(rel), re.IGNORECASE)
        }
        probe = d
        while not ids and probe != EVIDENCE:
            ids = _title_ids(probe / "README.md")
            if (probe / "README.md").is_file():
                break
            probe = probe.parent
        if not ids:
            for n in sorted(seat + verdict):
                ids |= _head_ids(d / n)
        if seat:
            kind = "أحكامُ مقاعد"
        elif verdict:
            kind = "مراجعةٌ استشاريّة" if any("advisory" in n for n in verdict) else "حكم"
        else:
            kind = "إحاطات"
        for wi in ids:
            out.setdefault(wi, set()).add(f"{rel.parts[0]}:{kind}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/main")
    ap.add_argument("--json", default="")
    ap.add_argument(
        "--today", default="", help="YYYY-MM-DD لحسابِ العمر (الافتراضيُّ ساعةُ الآلة)"
    )
    ap.add_argument(
        "--active-from",
        default="",
        help="مرجعٌ يُقرأُ منه ACTIVE_WORK.md بدلَ الشجرةِ الحاضرة",
    )
    a = ap.parse_args()
    if a.active_from:
        _ACTIVE_TEXT.append(
            _git("show", f"{a.active_from}:docs/governance/work/ACTIVE_WORK.md")
        )
    today = date.fromisoformat(a.today) if a.today else date.today()
    print(f"ACTIVE_WORK من: {a.active_from or 'الشجرةِ الحاضرة'} · السجلُّ من: {a.ref}")

    table = domain_classes()
    all_rows = rows()
    in_review = [r for r in all_rows if r[5] == "IN_REVIEW"]
    card = cards()
    log = first_parent_log(a.ref)
    ledger_added = ledger_rows_added(a.ref)
    rounds = prior_rounds()

    # ── التوفيقُ 49 ↔ 20 ──
    hdr_backtick = sorted(w for w, c in card.items() if "`IN_REVIEW`" in c["header"])
    card_status = sorted(
        w for w, c in card.items() if c["status"].split()[1:2] == ["IN_REVIEW"]
    )
    row_ids = sorted(r[0] for r in in_review)
    print(f"صفوفُ ACTIVE_WORK حالتُها IN_REVIEW: {len(row_ids)}")
    print(f"بطاقاتٌ سطرُ «الحالة:» فيها IN_REVIEW: {len(card_status)}")
    print(f"عناوينُ بطاقاتٍ فيها `IN_REVIEW` بعلامتَي الشِّفرة: {len(hdr_backtick)}")
    other = sorted(set(row_ids) - set(hdr_backtick))
    print(f"الفرقُ ({len(other)}): صفوفٌ IN_REVIEW وعنوانُ بطاقتِها لا يقولُ `IN_REVIEW`:")
    for w in other:
        h = card.get(w, {}).get("header", "")
        states = re.findall(r"`([A-Z_]{4,})`", h)
        bare = "IN_REVIEW" in h and "`IN_REVIEW`" not in h
        print(
            f"  {w}: حالاتُ العنوان {states or '—'}{' · IN_REVIEW بلا علامتين' if bare else ''}"
        )
    print()

    results = []
    for r in in_review:
        wi, domain_cell, tier_cell = r[0], r[1], r[2]
        claimed = split_paths(r[6])
        kinds = sorted({path_kind(p) for p in claimed})
        doms = sorted({path_domain(p, table) for p in claimed}, key=lambda t: t[0])
        declared = sorted(
            set(
                re.findall(
                    r"\bC[0-4]\b", tier_cell + " " + card.get(wi, {}).get("header", "")
                )
            )
        )
        tier = (re.findall(r"\bT[0-3]\b", tier_cell) or ["—"])[0]
        dom_class = {d: k for _p, d, k in table}
        row_class = dom_class.get(domain_cell, "C0")
        path_max = max([CLASS_RANK[k] for _d, k in doms] + [CLASS_RANK[row_class]])
        decl_max = max((CLASS_RANK[k] for k in declared), default=-1)
        eff = f"C{max(path_max, decl_max)}"
        merge = first_code_merge(wi, claimed, log, ledger_added)
        rnd = sorted(rounds.get(wi, set()))
        has_prod = "إنتاج" in kinds
        if CLASS_RANK[eff] >= 3 and has_prod:
            cat = "أ"
        elif tier == "T0" and not has_prod and CLASS_RANK[eff] <= 1:
            cat = "ب"
        else:
            cat = "د"
        results.append(
            {
                "wi": wi,
                "tier": tier,
                "declared_class": declared,
                "path_domains": [f"{d}:{k}" for d, k in doms],
                "effective_class": eff,
                "kinds": kinds,
                "first_code_merge": merge,
                "age_days_from_first_code_merge": (
                    (today - date.fromisoformat(merge[1])).days if merge else None
                ),
                "prior_round_evidence": rnd,
                "category": cat,
                "row_domain": f"{domain_cell}:{row_class}",
            }
        )

    print(
        f"الرقم | الطبقة | نطاقُ الصفّ | الفئةُ المعلنة | فئةُ المسارات | الفعّالة | النوع | أوّلُ دمجٍ لشِفرة | العمرُ يومًا (إلى {today}) | جولةٌ سابقة | الصنف"
    )
    for x in results:
        m = x["first_code_merge"]
        print(
            f"{x['wi']} | {x['tier']} | {x['row_domain']} | {','.join(x['declared_class']) or '—'} | "
            f"{' '.join(x['path_domains'])} | {x['effective_class']} | {'+'.join(x['kinds'])} | "
            f"{(m[1] + ' ' + m[2] + ' ' + m[0] + ' (' + m[3] + ')') if m else '—'} | "
            f"{x['age_days_from_first_code_merge'] if m else '—'} | "
            f"{','.join(x['prior_round_evidence']) or '—'} | {x['category']}"
        )
    counts: dict[str, int] = {}
    for x in results:
        counts[x["category"]] = counts.get(x["category"], 0) + 1
    print("\nالأصناف:", " · ".join(f"({k}) {v}" for k, v in sorted(counts.items())))
    if a.json:
        Path(a.json).write_text(
            json.dumps(
                {
                    "الهدف": "فرزُ بنودِ IN_REVIEW المقيسُ عرضًا للمالك (Q-89 · W-770)",
                    "in_review_rows": row_ids,
                    "header_backtick": hdr_backtick,
                    "card_status": card_status,
                    "items": results,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
