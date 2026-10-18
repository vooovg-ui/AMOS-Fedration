"""
حارسُ انحدارِ أداءِ الإلحاقِ في السجلِّ الدستوريِّ — DISC-100 · WI-086 (W-426).
الهدف: يسقطُ إن عادَ `append()` إلى التحقّقِ الكاملِ من السلسلةِ مع كلِّ قيد (O(N) بثابتِ ~20 µs لكلِّ قيدٍ سابق).
النطاق: نسبةٌ لا عتبةٌ مطلقة — وسيطُ زمنِ الإلحاقِ ÷ وسيطُ زمنِ `_verify(entries())` على السجلِّ نفسِه في اللحظةِ نفسِها،
  فضجيجُ العاملِ (CPU · قرص) يقعُ على الطرفينِ معًا. قبلَ WI-086 كانت النسبةُ ~1.0 (الإلحاقُ = تحقّقٌ كاملٌ + fsync)
  وبالبديلِ أ-2 ~0.05 (بصمةُ بايتاتٍ + fsync) — والحدُّ 0.25 بينهما بهامشٍ واسعٍ في الاتجاهين.
المالك: core/constitutional_engine/ (WI-086 · Perplexity Computer)
تاريخ الإنشاء: 2026-10-17
تاريخ آخر تعديل: 2026-10-17
"""

from __future__ import annotations

import json
import os
import statistics
import time
from pathlib import Path

from core.constitutional_engine.ledger import GENESIS_HASH, ConstitutionalLedger, _hash_entry

N = 4000
APPENDS = 15
VERIFIES = 5
MAX_RATIO = 0.25

BODY = {
    "type": "CONSTITUTIONAL_VERDICT",
    "actor": "executive",
    "action": "disburse_funds",
    "decision": "DENY",
    "rules_evaluated": 31,
    "violations": [{"article_id": "A003", "rule_id": "R-003-1", "severity": "CRITICAL"}],
}


def _write_valid_chain(path: Path, n: int) -> None:
    """سلسلةٌ صحيحةٌ تُكتَبُ مباشرةً — التحضيرُ بـappend نفسِه تربيعيٌّ قبلَ الإصلاح."""
    prev = GENESIS_HASH
    ts = "2026-10-17T00:00:00.000000+00:00"
    with open(path, "w", encoding="utf-8") as fh:
        for i in range(n):
            sealed = {"index": i, "timestamp": ts, **BODY}
            h = _hash_entry(prev, sealed)
            rec = {"index": i, "timestamp": ts, "prev_hash": prev, "entry_hash": h, "body": sealed}
            fh.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")
            prev = h
        fh.flush()
        os.fsync(fh.fileno())


def test_append_costs_a_small_fraction_of_a_full_chain_verification(tmp_path):
    path = tmp_path / "perf.jsonl"
    _write_valid_chain(path, N)
    led = ConstitutionalLedger(path)
    led.append(BODY)  # أوّلُ إلحاقٍ في العمليّة: تحقّقٌ كاملٌ يبني الحالة — لا يُقاس

    appends = []
    for _ in range(APPENDS):
        t0 = time.perf_counter()
        led.append(BODY)
        appends.append(time.perf_counter() - t0)

    verifies = []
    for _ in range(VERIFIES):
        t0 = time.perf_counter()
        ConstitutionalLedger._verify(led.entries())
        verifies.append(time.perf_counter() - t0)

    a, v = statistics.median(appends), statistics.median(verifies)
    ratio = a / v
    assert led.verify_chain() == []
    assert ratio < MAX_RATIO, (
        f"الإلحاقُ عند N={N} يكلّفُ {ratio:.2f} من تحقّقٍ كاملٍ (وسيطُ الإلحاقِ {a * 1e3:.2f} ms · "
        f"وسيطُ التحقّقِ {v * 1e3:.2f} ms) والحدُّ {MAX_RATIO} — هل عادَ append إلى التحقّقِ الكاملِ في كلِّ قيد؟ (DISC-100)"
    )
