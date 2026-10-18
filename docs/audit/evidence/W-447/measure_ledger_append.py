"""
قياسُ زمنِ الإلحاقِ في سجلِّ المحركِ الدستوريِّ بدلالةِ طولِ السلسلة — دليلُ DISC-100 (WI-085 · W-411).
الهدف: إثباتُ منحنى الكلفةِ أو نفيُه بالقياس: هل زمنُ `append()` الواحدِ خطّيٌّ في N (فالتراكميُّ تربيعيٌّ O(N²))؟
النطاق: يستعملُ الصنفَ الإنتاجيَّ `core.constitutional_engine.ledger.ConstitutionalLedger` كما هو — بلا تعديلٍ ولا ترقيع —
  على سجلٍّ مؤقّتٍ في مجلّدٍ مؤقّت؛ فلا يمسُّ السجلَّ الافتراضيَّ ولا أيَّ ملفٍّ في المستودع.
المالك: Perplexity Computer (WI-085 · توجيهُ المستشارِ 10 § 2)
تاريخ الإنشاء: 2026-10-17
تاريخ آخر تعديل: 2026-10-17

التشغيل (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-411/measure_ledger_append.py
    .venv/bin/python docs/audit/evidence/W-411/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400

ما يُقاسُ عند كلِّ N:
  - append_median_ms : وسيطُ زمنِ `append()` واحدٍ (M إلحاقًا متتاليًا عند الطولِ N تقريبًا)
  - verify_median_ms : وسيطُ زمنِ `_verify(entries())` وحدَه (ما يفعلُه `append()` داخلَ القفلِ قبلَ الكتابة)
  - fsync_floor_ms   : وسيطُ زمنِ كتابةِ سطرٍ بالحجمِ نفسِه + fsync في ملفٍّ منفصل — أرضيّةٌ ثابتةٌ لا تتعلّقُ بـN
  - cumulative_s     : الزمنُ التراكميُّ لبناءِ السجلِّ من 0 إلى N بالإلحاقِ وحدَه
الحدودُ المعلنة: الأزمنةُ تتعلّقُ بالآلةِ والقرص؛ المعتبَرُ النسبُ بينَ نقاطِ N لا الأرقامُ المطلقة.
"""

from __future__ import annotations

import argparse
import os
import platform
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT))

from core.constitutional_engine.ledger import ConstitutionalLedger  # noqa: E402

# جسمٌ بشكلِ الجسمِ الذي يكتبُه المحرّكُ فعلًا (engine.py: CONSTITUTIONAL_VERDICT) — منسوخُ البنيةِ من قيدٍ حقيقيّ.
BODY = {
    "type": "CONSTITUTIONAL_VERDICT",
    "actor": "executive",
    "action": "disburse_funds",
    "target": "test/q18",
    "criticality": "normal",
    "kill_switch_level": 0,
    "decision": "DENY",
    "decision_kind": "",
    "authority_layer": "",
    "sovereign_path": False,
    "request_fingerprint": "08416e2ff2ad195bd9e867ee0d8375aa",
    "rules_evaluated": 31,
    "advisory_violations": [],
    "violations": [
        {
            "article_id": "A003",
            "article_title": "المادة الثالثة — الفصل بين السلطات",
            "clause": "الفروع الأربعة — الحدود",
            "reason": "الفرع «executive» يمارس «disburse_funds» وهو اختصاص حصري للفرع «treasury». "
            "الفصل بين السلطات يمنع ذلك.",
            "rule_id": "R-003-1",
            "severity": "CRITICAL",
        }
    ],
}


def _git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        return f"unknown ({exc})"


def _fsync_floor(dirpath: Path, line: str, reps: int) -> float:
    p = dirpath / "fsync_probe.txt"
    samples = []
    for _ in range(reps):
        t0 = time.perf_counter()
        with open(p, "a", encoding="utf-8") as fh:
            fh.write(line)
            fh.flush()
            os.fsync(fh.fileno())
        samples.append(time.perf_counter() - t0)
    return statistics.median(samples)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--sizes", default="200,400,800,1600,3200")
    ap.add_argument(
        "--appends",
        type=int,
        default=20,
        help="عددُ الإلحاقاتِ المقيسةِ عند كلِّ N (الوسيط)",
    )
    ap.add_argument("--verify-reps", type=int, default=5)
    args = ap.parse_args()
    sizes = sorted(int(s) for s in args.sizes.split(","))

    print(
        "# قياسُ زمنِ append() في ConstitutionalLedger بدلالةِ N — DISC-100 · WI-085 · W-411"
    )
    print(f"# commit: {_git_head()}")
    print(f"# python: {platform.python_version()} · platform: {platform.platform()}")
    print(
        f"# sizes: {sizes} · appends/N: {args.appends} · verify reps: {args.verify_reps}"
    )

    rows = []
    with tempfile.TemporaryDirectory(prefix="w411_ledger_") as tmp:
        tmpdir = Path(tmp)
        ledger = ConstitutionalLedger(tmpdir / "ledger.jsonl")
        build_elapsed = 0.0
        n = 0
        for target in sizes:
            t0 = time.perf_counter()
            while n < target:
                ledger.append(BODY)
                n += 1
            build_elapsed += time.perf_counter() - t0
            cumulative = build_elapsed

            samples = []
            for _ in range(args.appends):
                t1 = time.perf_counter()
                ledger.append(BODY)
                samples.append(time.perf_counter() - t1)
                n += 1
            # الإلحاقاتُ المقيسةُ تدخلُ في الطولِ؛ وزمنُها يُضافُ إلى التراكميِّ ليبقى صادقًا
            build_elapsed += sum(samples)

            vs = []
            for _ in range(args.verify_reps):
                t2 = time.perf_counter()
                ConstitutionalLedger._verify(ledger.entries())
                vs.append(time.perf_counter() - t2)

            line_len = (
                len(
                    (tmpdir / "ledger.jsonl")
                    .read_text(encoding="utf-8")
                    .splitlines()[-1]
                )
                + 1
            )
            floor = _fsync_floor(tmpdir, "x" * (line_len - 1) + "\n", args.appends)
            rows.append(
                {
                    "N": target,
                    "append_ms": statistics.median(samples) * 1e3,
                    "verify_ms": statistics.median(vs) * 1e3,
                    "fsync_ms": floor * 1e3,
                    "cum_s": cumulative,
                }
            )
        problems = ledger.verify_chain()

    print()
    print(
        f"{'N':>6} | {'append_median_ms':>16} | {'verify_median_ms':>16} | {'fsync_floor_ms':>14} | {'cumulative_s':>12}"
    )
    print("-" * 78)
    for r in rows:
        print(
            f"{r['N']:>6} | {r['append_ms']:>16.3f} | {r['verify_ms']:>16.3f} | {r['fsync_ms']:>14.3f} | {r['cum_s']:>12.3f}"
        )

    print()
    print("# النسبُ بينَ نقاطٍ متتاليةٍ (N يتضاعف): خطّيٌّ ⇒ ~2 · تربيعيٌّ ⇒ ~4")
    print(f"{'N→2N':>12} | {'append ×':>9} | {'verify ×':>9} | {'cumulative ×':>12}")
    for a, b in zip(rows, rows[1:]):
        print(
            f"{a['N']:>5}→{b['N']:<6} | {b['append_ms'] / a['append_ms']:>9.2f} | "
            f"{b['verify_ms'] / a['verify_ms']:>9.2f} | {b['cum_s'] / a['cum_s']:>12.2f}"
        )

    # ملاءمةٌ خطّيّةٌ لزمنِ الإلحاقِ: append(N) ≈ a + b·N  (a ثابتٌ يضمُّ fsync · b كلفةُ القيدِ الواحدِ في التحقّق)
    xs = [r["N"] for r in rows]
    ys = [r["append_ms"] for r in rows]
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    a = my - b * mx
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    r2 = 1 - ss_res / ss_tot if ss_tot else float("nan")
    print()
    print(
        f"# ملاءمةٌ خطّيّة: append_ms(N) ≈ {a:.3f} + {b * 1e3:.3f}·N/1000   (R² = {r2:.4f})"
    )
    print(
        f"#   ⇒ كلفةُ القيدِ الواحدِ في كلِّ إلحاقٍ ≈ {b * 1e3:.1f} µs · والتراكميُّ ≈ a·N + b·N²/2 (تربيعيٌّ في N)"
    )
    for n_ref in (19119, 50000):
        print(f"#   استقراءٌ (لا قياس): append عند N={n_ref} ≈ {a + b * n_ref:.1f} ms")
    print(f"# سلامةُ السلسلةِ بعدَ القياس: {'سليمة' if not problems else problems}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
