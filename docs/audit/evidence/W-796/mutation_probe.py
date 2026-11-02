"""مِسبارُ الطفراتِ الخمسِ المُكيَّفةِ لـWI-127 (W-796 · § 2.11 قرار 7).

الهدف: قياسُ أنَّ فحوصَ `test_w792_m1_batch2_composites.py` تقتلُ كلَّ طفرةٍ **سلوكًا** — يُطبَّقُ
تغييرٌ نصّيٌّ واحدٌ على ملفِّ مصدرٍ، ويُشغَّلُ الفحصُ المُسمّى، ويُطلَبُ سقوطُه، ثمَّ يُعادُ الملفُّ
كما كان (يُتحقَّقُ بالبصمة). يُشغَّلُ من جذرِ المستودع: `.venv/bin/python <this> [--json out]`.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

SRC = Path("federal/executive/services/src/amos_federation/services")
MA = SRC / "executive_core/money_authority.py"
NE = SRC / "national_economy/service.py"
TEST = "tests/test_w792_m1_batch2_composites.py"

MUTATIONS = [
    {
        "id": "①",
        "what": "معوِّضُ الصفِّ اللاحقِ فارغ (لا يحذفُ ولا يُرجِع)",
        "file": MA,
        "old": 'lambda: undo_item(applied["follow_up"].get(declared.signature)),',
        "new": "lambda: None,",
        "test": "test_3_expenditure_late_failure_reverses_money_and_removes_the_record",
    },
    {
        "id": "②",
        "what": "سجلُّ العمليّةِ وحالتُها يُكتَبانِ بعدَ `disburse` خارجَ العبور (الشكلُ السابقُ للقيد)",
        "file": NE,
        "first": [
            (
                "            follow_up=(\n",
                "            follow_up=()\n            if True\n            else (\n",
            ),
            (
                '        follow = transaction.pop("follow_up", None)\n',
                '        transaction.pop("follow_up", None)\n'
                "        follow = [_record(transaction), _mark_executed(transaction)]\n",
            ),
        ],
        "test": "test_3_expenditure_late_failure_reverses_money_and_removes_the_record",
    },
    {
        "id": "③",
        "what": "فاعلُ `EXECUTIVE` بدلَ مدخلِ الجدولِ للعبورِ ذي الصفوف",
        "file": MA,
        "old": '"authorizer": build(delegation.actor),',
        "new": '"authorizer": build("EXECUTIVE" if follow_effects else delegation.actor),',
        "test": "test_1_expenditure_writes_record_and_status_inside_the_crossing",
    },
    {
        "id": "④",
        "what": "الصفوفُ تُعلَنُ قبلَ أثرِ الحركة (سجلٌّ بلا مرجعِ حركة)",
        "file": MA,
        "old": '"declared_effects": (effect, *(e for e, _ in follow_effects)),',
        "new": '"declared_effects": (*(e for e, _ in follow_effects), effect),',
        "test": "test_1_expenditure_writes_record_and_status_inside_the_crossing",
    },
    {
        "id": "⑤",
        "what": "صفٌّ بلا معوِّضٍ يُعطى معوِّضًا فارغًا بدلَ أن يُرفَضَ العقد",
        "file": MA,
        "old": "_follow_compensator(e, item, item.undo)\n                for e, item in follow_effects\n                if item.undo is not None",
        "new": "_follow_compensator(e, item, item.undo or (lambda _r: None))\n                for e, item in follow_effects",
        "test": "test_8_follow_up_without_compensator_is_refused_before_any_write",
    },
]


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _run(test: str) -> tuple[int, str]:
    cmd = [
        str(Path.cwd() / ".venv/bin/python"),
        "-m",
        "pytest",
        "-q",
        "-x",
        "-p",
        "no:cacheprovider",
        f"{TEST}::{test}",
    ]
    done = subprocess.run(  # noqa: S603 — أمرٌ ثابتٌ بلا مُدخَلٍ خارجيّ
        cmd,
        cwd="federal/executive/services",
        capture_output=True,
        text=True,
        check=False,
    )
    reason = [ln for ln in done.stdout.splitlines() if ln.startswith("E ")][:3]
    return done.returncode, " | ".join(reason)[:400]


def main() -> int:
    results = []
    baseline = {m["test"]: _run(m["test"])[0] for m in MUTATIONS}
    for m in MUTATIONS:
        path: Path = m["file"]
        original = path.read_text(encoding="utf-8")
        before = _sha(path)
        mutated = original
        if "old" in m:
            assert original.count(m["old"]) == 1, (m["id"], original.count(m["old"]))
            mutated = original.replace(m["old"], m["new"])
        for a, b in m.get("first", []):
            # أوّلُ موضعٍ هو `execute_expenditure` (يسبقُ `execute_transfer` في الملفّ).
            assert mutated.index(a) < mutated.index("    def execute_transfer("), (
                m["id"],
                a,
            )
            mutated = mutated.replace(a, b, 1)
        try:
            path.write_text(mutated, encoding="utf-8")
            rc, reason = _run(m["test"])
        finally:
            path.write_text(original, encoding="utf-8")
        assert _sha(path) == before, "الملفُّ لم يَعُدْ كما كان"
        results.append(
            {
                "id": m["id"],
                "what": m["what"],
                "file": str(path),
                "test": m["test"],
                "baseline_rc": baseline[m["test"]],
                "mutated_rc": rc,
                "reason": reason,
                "killed": baseline[m["test"]] == 0 and rc != 0,
            }
        )
    for r in results:
        verdict = "KILLED" if r["killed"] else "SURVIVED"
        print(
            f"{r['id']} {verdict} · أساس={r['baseline_rc']} · طفرة={r['mutated_rc']} · {r['what']}"
        )
        print(f"   السبب: {r['reason']}")
    killed = sum(r["killed"] for r in results)
    print(f"المجموع: {killed}/{len(results)} مقتولة")
    if len(sys.argv) > 2 and sys.argv[1] == "--json":
        Path(sys.argv[2]).write_text(
            json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    return 0 if killed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
