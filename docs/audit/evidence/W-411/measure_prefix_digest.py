"""
قياسُ كلفةِ مكوّناتِ البديلينِ المقترحينِ في وثيقةِ تصميمِ DISC-100 — لا تنفيذَ لهما (WI-085 · W-411).
الهدف: رقمٌ مقيسٌ لا تخمينٌ لكلفةِ كلِّ مكوّنٍ يقترحُه التصميمُ عند كلِّ إلحاق، مقابلَ كلفةِ التحقّقِ الكاملِ الحاليّ:
  (1) verify_full   : `ConstitutionalLedger._verify(entries())` — ما يفعلُه `append()` اليومَ
  (2) prefix_digest : قراءةُ بايتاتِ الملفِّ كلِّها وحسابُ sha256 لها — مكوّنُ البديلِ «أ-2» (كشفٌ فوريٌّ بلا نافذة)
  (3) stat_tail     : `os.stat` + قراءةُ آخرِ سطرٍ بإزاحةٍ معلومةٍ وإعادةُ حسابِ بصمتِه — مكوّنُ البديلِ «أ-1»
النطاق: الصنفُ الإنتاجيُّ `ConstitutionalLedger` بلا تعديلٍ يبني سجلًّا مؤقّتًا؛ والمكوّنانِ (2) و(3) محاكاةُ قياسٍ
  في هذا الملفِّ وحدَه — **ليسا تنفيذًا للبديلِ ولا يُستورَدانِ من أيِّ مكان**.
المالك: Perplexity Computer (WI-085 · توجيهُ المستشارِ 10 § 2)
تاريخ الإنشاء: 2026-10-17
تاريخ آخر تعديل: 2026-10-17

التشغيل (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-411/measure_prefix_digest.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import statistics
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core.constitutional_engine.ledger import ConstitutionalLedger, _hash_entry  # noqa: E402
from measure_ledger_append import BODY, _git_head  # noqa: E402


def _median(fn, reps: int) -> float:
    s = []
    for _ in range(reps):
        t0 = time.perf_counter()
        fn()
        s.append(time.perf_counter() - t0)
    return statistics.median(s)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sizes", default="200,400,800,1600,3200,6400,12800")
    ap.add_argument("--reps", type=int, default=7)
    args = ap.parse_args()
    sizes = sorted(int(s) for s in args.sizes.split(","))
    print(
        "# كلفةُ مكوّناتِ البديلينِ (محاكاةُ قياسٍ لا تنفيذ) مقابلَ التحقّقِ الكاملِ — DISC-100 · WI-085 · W-411"
    )
    print(f"# commit: {_git_head()} · reps: {args.reps}")
    print(
        "# البناءُ هنا بكتابةِ أسطرٍ صحيحةِ السلسلةِ مباشرةً (لا بـappend) لتجنّبِ الكلفةِ التربيعيّةِ في التحضير؛"
    )
    print("# ثمَّ يُتحقَّقُ من السلسلةِ بالصنفِ الإنتاجيِّ قبلَ القياس.")
    print()
    print(
        f"{'N':>6} | {'bytes':>10} | {'verify_full_ms':>14} | {'prefix_digest_ms':>16} | {'stat_tail_ms':>12} | {'full/digest':>11}"
    )
    print("-" * 86)
    with tempfile.TemporaryDirectory(prefix="w411_digest_") as tmp:
        path = Path(tmp) / "ledger.jsonl"
        led = ConstitutionalLedger(path)
        prev = "0" * 64
        n = 0
        ts = "2026-10-17T00:00:00.000000+00:00"
        with open(path, "a", encoding="utf-8") as fh:
            for target in sizes:
                while n < target:
                    sealed = {"index": n, "timestamp": ts, **BODY}
                    h = _hash_entry(prev, sealed)
                    rec = {
                        "index": n,
                        "timestamp": ts,
                        "prev_hash": prev,
                        "entry_hash": h,
                        "body": sealed,
                    }
                    fh.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")
                    prev = h
                    n += 1
                fh.flush()
                os.fsync(fh.fileno())
                assert led.verify_chain() == [], "السلسلةُ المبنيّةُ غيرُ سليمة"
                size = path.stat().st_size

                def verify_full() -> None:
                    ConstitutionalLedger._verify(led.entries())

                def prefix_digest() -> None:
                    with open(path, "rb") as f:
                        hashlib.sha256(f.read()).hexdigest()

                last_off = size - len(path.read_bytes().rsplit(b"\n", 2)[-2]) - 1

                def stat_tail() -> None:
                    st = os.stat(path)
                    _ = (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns)
                    with open(path, "rb") as f:
                        f.seek(last_off)
                        r = json.loads(f.readline())
                    assert _hash_entry(r["prev_hash"], r["body"]) == r["entry_hash"]

                vf = _median(verify_full, args.reps)
                pd = _median(prefix_digest, args.reps)
                stt = _median(stat_tail, args.reps * 5)
                print(
                    f"{target:>6} | {size:>10} | {vf * 1e3:>14.3f} | {pd * 1e3:>16.3f} | {stt * 1e3:>12.4f} | {vf / pd:>11.1f}"
                )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
