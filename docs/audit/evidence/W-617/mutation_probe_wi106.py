"""مسبارُ طفراتِ WI-106 (الدفعةُ F1) — دليلُ قيدِ W-617.

الغرض: تطبيقُ كلِّ طفرةٍ مُعلَنةٍ في ملحقِ التصميمِ (§ 5 · M1–M5) على نسخةِ الوحدةِ،
وتشغيلُ فحوصِ البندِ، وإثباتُ أنَّ كلَّ طفرةٍ تُسقِطُ فحصَها المُعلَنَ ثمَّ استعادةُ الأصلِ
بايتًا ببايتٍ (البصمةُ قبلُ وبعدُ).
التشغيل: من جذرِ المستودعِ — `.venv/bin/python docs/audit/evidence/W-617/mutation_probe_wi106.py`
المالك: Perplexity Computer · تاريخ الإنشاء: 2026-10-22
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SERVICES = ROOT / "federal" / "executive" / "services"
TARGET = SERVICES / "src/amos_federation/services/governance/federation.py"
TESTS = "tests/test_wi106_federation_coordinate_sovereign.py"


def _m1(src: str) -> str:
    head, tail = src.split('operation = "LegislativeBranch.propose"', 1)
    guard = re.search(r"_federation_authorizer\(\)\.guard_declared\(.*?\n        \)\n", tail, re.S)
    assert guard
    return head + 'operation = "LegislativeBranch.propose"' + tail.replace(
        guard.group(0), "_apply(None)\n", 1
    )


MUTATIONS = {
    "M1 · propose يكتبُ بلا عبورٍ": (_m1, ["t1", "t3"]),
    "M2 · الفاعلُ JUDICIAL": (
        lambda s: s.replace('FEDERATION_ACTOR = "EXECUTIVE"', 'FEDERATION_ACTOR = "JUDICIAL"', 1),
        ["t1", "t8"],
    ),
    "M3 · المُعوِّضُ لا يفعلُ شيئًا": (
        lambda s: s.replace(
            "    def _restore(self) -> None:\n", "    def _restore(self) -> None:\n        return\n", 1
        ),
        ["t4", "t5"],
    ),
    "M4 · vote بلا تسجيلِ السابقِ": (
        lambda s: re.sub(r"\n *undo\.prior\(record, \"voters\"[^\n]*", "", s, count=1),
        ["t5"],
    ),
    "M5 · مفتاحُ enact بمُعرِّفِ استدعاءٍ": (
        lambda s: s.replace(
            'f"legislations/{legislation_id}/enact"',
            'f"legislations/{legislation_id}/enact/{_nonce()}"',
            1,
        ),
        ["t6"],
    ),
}


def _run(selector: str) -> tuple[int, str]:
    r = subprocess.run(
        [sys.executable, "-m", "pytest", TESTS, "-q", "-p", "no:cacheprovider", "-k", selector],
        cwd=SERVICES,
        capture_output=True,
        text=True,
        timeout=900,
        check=False,
    )
    lines = [ln for ln in r.stdout.splitlines() if "passed" in ln or "failed" in ln]
    return r.returncode, (lines[-1] if lines else r.stdout[-300:])


def main() -> int:
    original = TARGET.read_bytes()
    digest = hashlib.sha256(original).hexdigest()
    print(f"sha256 قبلُ: {digest}")
    rc, line = _run("wi106")
    print(f"الأصلُ: rc={rc} · {line}")
    all_killed = rc == 0
    try:
        for name, (mutate, expected) in MUTATIONS.items():
            mutated = mutate(original.decode("utf-8"))
            assert mutated != original.decode("utf-8"), f"الطفرةُ لم تُطبَّق: {name}"
            TARGET.write_text(mutated, encoding="utf-8")
            for test in expected:
                rc, line = _run(f"wi106_{test}_")
                killed = rc != 0
                all_killed = all_killed and killed
                print(f"{name} ⇒ {test}: {'سقطَ (قُتِلَت)' if killed else 'نجحَ (نجَت!)'} · {line}")
            TARGET.write_bytes(original)
    finally:
        TARGET.write_bytes(original)
    after = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    print(f"sha256 بعدُ: {after} · {'مطابقٌ' if after == digest else 'مختلفٌ!'}")
    print("الحكمُ: كلُّ الطفراتِ قُتِلَت" if all_killed and after == digest else "الحكمُ: فشلٌ")
    return 0 if all_killed and after == digest else 1


if __name__ == "__main__":
    raise SystemExit(main())
