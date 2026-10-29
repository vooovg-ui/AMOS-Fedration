"""الهدف: طفرةٌ تُسقِطُ معوِّضَ الكانونِ في retire_agent — يجبُ أن تقتلَها فحوصُ (3أ) و(3ب) تحديدًا (التوجيهُ 29 § 2 · قيدُ W-736).

النطاق: سطرٌ واحدٌ في `governance/expansion.py` (`_restore_canonical`) يُستبدَلُ بلا شيءٍ في نسخةٍ
مؤقّتةٍ على القرصِ ثمَّ يُعادُ الأصلُ بايتًا ببايتٍ (تُقاسُ البصمةُ قبلَ وبعد). خطُّ أساسٍ بلا طفرةٍ يجبُ
أن ينجح أوّلًا، فلا يُحتسَبُ فشلٌ عارضٌ قتلًا.
المالك: Perplexity Computer (قيدُ W-736).
تاريخ الإنشاء: 2026-10-29

التشغيلُ (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-736/mutation_canonical_compensator.py
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SERVICES = ROOT / "federal/executive/services"
SRC = SERVICES / "src/amos_federation/services/governance/expansion.py"
TESTS = [
    "tests/test_w736_q26_retire_single_crossing.py::test_3a_mirror_failure_after_canonical_restores_canonical",
    "tests/test_w736_q26_retire_single_crossing.py::test_3b_record_failure_after_canonical_and_mirror_restores_both",
]
ORIGINAL_LINE = (
    "                _set_lifecycle_state_core(agent_id, str(canonical_previous))\n"
)
MUTANT_LINE = "                pass  # MUTATION W-736: معوِّضُ الكانونِ مُسقَط\n"


def _run(test: str) -> tuple[int, str]:
    proc = subprocess.run(
        [
            str(ROOT / ".venv/bin/python"),
            "-m",
            "pytest",
            "-q",
            "-p",
            "no:cacheprovider",
            test,
        ],
        cwd=SERVICES,
        capture_output=True,
        text=True,
    )
    tail = [ln for ln in proc.stdout.splitlines() if " passed" in ln or " failed" in ln]
    return proc.returncode, (tail[-1] if tail else proc.stdout[-300:])


def main() -> int:
    original = SRC.read_bytes()
    sha0 = hashlib.sha256(original).hexdigest()
    text = original.decode("utf-8")
    assert text.count(ORIGINAL_LINE) == 1, "سطرُ معوِّضِ الكانونِ غيرُ فريد"
    print(f"sha256(expansion.py) قبلَ: {sha0}")
    killed = 0
    for test in TESTS:
        rc, line = _run(test)
        print(f"BASELINE  {test.split('::')[1]}: rc={rc} · {line}")
        if rc != 0:
            print("خطُّ الأساسِ أحمرُ — لا تُقاسُ الطفرة")
            return 2
    try:
        SRC.write_text(text.replace(ORIGINAL_LINE, MUTANT_LINE), encoding="utf-8")
        for test in TESTS:
            rc, line = _run(test)
            verdict = "KILLED" if rc != 0 else "SURVIVED"
            killed += rc != 0
            print(f"MUTANT    {test.split('::')[1]}: rc={rc} · {line} → {verdict}")
    finally:
        SRC.write_bytes(original)
    sha1 = hashlib.sha256(SRC.read_bytes()).hexdigest()
    print(f"sha256(expansion.py) بعدَ: {sha1} · {'مطابقٌ' if sha1 == sha0 else 'مخالف!'}")
    print(f"MUTATION SUMMARY: tests={len(TESTS)} killed={killed}")
    return 0 if killed == len(TESTS) and sha1 == sha0 else 1


if __name__ == "__main__":
    sys.exit(main())
