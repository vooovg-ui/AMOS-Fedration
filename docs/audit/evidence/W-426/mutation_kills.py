"""
قتلُ التحويراتِ في شِفرةِ البديلِ أ-2 — WI-086 (W-426).
الهدف: إثباتُ أنَّ كلَّ مكوّنٍ من مكوّناتِ الحالةِ المُتحقَّقِ منها في `ledger.py` محروسٌ بفحصٍ يسقطُ عندَ تعطيله.
النطاق: يُطبِّقُ كلَّ تحويرٍ على `core/constitutional_engine/ledger.py` مؤقّتًا، يُشغِّلُ `tests/constitutional/`،
  ثمَّ يُعيدُ الملفَّ بايتًا ببايت (ويتحقّقُ من sha256) — ويخرجُ بغيرِ صفرٍ إن نجا تحويرٌ أو لم يُعَدِ الملف.
المالك: docs/audit/evidence/W-426 (WI-086 · Perplexity Computer)
تاريخ الإنشاء: 2026-10-17
تاريخ آخر تعديل: 2026-10-17
الاستعمال: .venv/bin/python docs/audit/evidence/W-426/mutation_kills.py
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TARGET = ROOT / "core" / "constitutional_engine" / "ledger.py"

# (المعرِّف · الوصف · النصُّ الأصليُّ · بديلُه) — كلُّ أصلٍ يظهرُ في الملفِّ مرّةً واحدةً بالضبط
MUTATIONS = [
    ("K1", "تعطيلُ مطابقةِ بصمةِ البادئة",
     "        if hasher.digest() != state.prefix_sha256:\n",
     "        if False:\n"),
    ("K2", "تعطيلُ التحقّقِ من الذيل",
     "        self._verify(new, start_index=state.count, prev_hash=state.last_hash)\n",
     "        pass\n"),
    ("K3", "تعطيلُ فحصِ (dev, ino)",
     "        if (st.st_dev, st.st_ino) != (state.dev, state.ino):\n",
     "        if False:\n"),
    ("K4", "تخطّي التحقّقِ الكاملِ الأوّلِ حينَ لا حالة",
     "            self._verify(entries)\n            last = entries[-1].entry_hash if entries else GENESIS_HASH\n",
     "            last = entries[-1].entry_hash if entries else GENESIS_HASH\n"),
    ("K5", "مفتاحُ الحالةِ بالكائنِ لا بالمسارِ الحقيقيّ (في القراءةِ والكتابة)",
     "        key = os.path.realpath(self.path)\n        st, raw = None, b\"\"\n",
     "        key = id(self)\n        st, raw = None, b\"\"\n"),
    ("K6", "تعطيلُ فحصِ اختفاءِ الملف",
     "        if st is None:\n            raise LedgerTamperError(\n",
     "        if False:\n            raise LedgerTamperError(\n"),
    ("K7", "عدمُ تحديثِ الحالةِ بعدَ الإلحاق (كلُّ إلحاقٍ تحقّقٌ كامل — انحدارُ الأداء)",
     "                if st.st_size == verified_size + len(data):\n",
     "                if False:\n"),
    ("K8", "بدءُ الذيلِ من موضعٍ خاطئ (index الذيلِ يبدأ بصفر)",
     "        self._verify(new, start_index=state.count, prev_hash=state.last_hash)\n",
     "        self._verify(new, prev_hash=state.last_hash)\n"),
]

# K5 يحتاجُ المفتاحَ نفسَه في الكتابةِ أيضًا — وإلّا لم يكن تحويرًا متّسقًا
K5_WRITE = ("            key = os.path.realpath(self.path)\n            with _VERIFIED_GUARD:\n",
            "            key = id(self)\n            with _VERIFIED_GUARD:\n")


def main() -> int:
    original = TARGET.read_bytes()
    digest = hashlib.sha256(original).hexdigest()
    text = original.decode("utf-8")
    survivors = []
    print(f"الهدف: {TARGET.relative_to(ROOT)} · sha256 {digest}")
    try:
        for mid, desc, old, new in MUTATIONS:
            assert text.count(old) == 1, f"{mid}: الأصلُ ليس فريدًا"
            mutated = text.replace(old, new)
            if mid == "K5":
                assert mutated.count(K5_WRITE[0]) == 1
                mutated = mutated.replace(*K5_WRITE)
            TARGET.write_text(mutated, encoding="utf-8")
            r = subprocess.run(
                [sys.executable, "-m", "pytest", "tests/constitutional", "-q", "-p", "no:cacheprovider", "-x"],
                cwd=ROOT, capture_output=True, text=True, timeout=900,
            )
            failed = [ln for ln in r.stdout.splitlines() if ln.startswith("FAILED")]
            summary = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
            killed = r.returncode != 0
            print(f"\n[{mid}] {desc}\n  ⇒ {'قُتِل' if killed else 'نجا ✗'} · {summary}")
            for ln in failed[:3]:
                print(f"    {ln[:200]}")
            if not killed:
                survivors.append(mid)
            TARGET.write_bytes(original)
    finally:
        TARGET.write_bytes(original)
    restored = hashlib.sha256(TARGET.read_bytes()).hexdigest() == digest
    print(f"\nأُعيدَ الملفُّ بايتًا ببايت: {'نعم' if restored else 'لا ✗'}")
    print(f"الحصيلة: {len(MUTATIONS) - len(survivors)}/{len(MUTATIONS)} قُتِلت · الناجية: {survivors or 'لا شيء'}")
    return 0 if restored and not survivors else 1


if __name__ == "__main__":
    raise SystemExit(main())
