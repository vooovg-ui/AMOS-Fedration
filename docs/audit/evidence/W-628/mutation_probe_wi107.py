"""مسبارُ طفراتِ WI-107 (الدفعةُ R1) — دليلُ قيدِ W-628.

الغرض: تطبيقُ كلِّ طفرةٍ مُعلَنةٍ في ملحقِ التصميمِ (§ 5 · M1–M5 · بحصادِ M5
المصحَّحِ كما قُيِّدَ في evidence/W-625/README.md) على نسخةِ الوحدةِ، وتشغيلُ
فحوصِ البندِ، وإثباتُ أنَّ كلَّ طفرةٍ تُسقِطُ فحصَها المُعلَنَ ثمَّ استعادةُ الأصلِ
بايتًا ببايتٍ (البصمةُ قبلُ وبعدُ).
التشغيل: من جذرِ المستودعِ — `.venv/bin/python docs/audit/evidence/W-628/mutation_probe_wi107.py`
النمطُ: mutation_probe_wi106.py (سابقةُ W-617) — لا اختلافَ في الميكانيكا.
المالك: Perplexity Computer · تاريخ الإنشاء: 2026-10-23 (W-628)
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SERVICES = ROOT / "federal" / "executive" / "services"
TARGET = SERVICES / "src/amos_federation/services/national_registry/service.py"
TESTS = "tests/test_wi107_national_registry_register_sovereign.py"

_M1_OLD = """        guarded = _registry_authorizer().guard_declared(
            REGISTRY_VERB, target, applier=_apply, **crossing
        )
        _refuse_replay(guarded, "NationalRegistry.create_identity", target)
        identity = guarded.value
"""
_M1_NEW = "        identity = _apply(None)\n"


def _m1(src: str) -> str:
    assert src.count(_M1_OLD) == 1, "مرساةُ M1 ليست فريدةً"
    return src.replace(_M1_OLD, _M1_NEW, 1)


MUTATIONS = {
    "M1 · create_identity يكتبُ بلا عبورٍ": (_m1, ["t1", "t3"]),
    "M2 · الفاعلُ JUDICIAL": (
        lambda s: s.replace('REGISTRY_ACTOR = "EXECUTIVE"', 'REGISTRY_ACTOR = "JUDICIAL"', 1),
        ["t1", "t8"],
    ),
    "M3 · المُعوِّضُ لا يفعلُ شيئًا": (
        lambda s: s.replace(
            "    def _restore(self) -> None:\n", "    def _restore(self) -> None:\n        return\n", 1
        ),
        ["t4", "t5"],
    ),
    "M4 · revoke_assignment بلا تسجيلِ السابقِ": (
        lambda s: s.replace(
            '                row = session.get(OfficialPositionModel, assignment_id)\n'
            '                undo.prior(row, "status", "revoked_at", "revocation_reason")\n',
            '                row = session.get(OfficialPositionModel, assignment_id)\n',
            1,
        ),
        ["t5"],
    ),
    "M5 · link_principal بلا رفضِ الإعادةِ (D5 مقتولةٌ)": (
        lambda s: s.replace("            if existing is not None:\n", "            if False:\n", 1),
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
    rc, line = _run("wi107")
    print(f"الأصلُ: rc={rc} · {line}")
    all_killed = rc == 0
    try:
        for name, (mutate, expected) in MUTATIONS.items():
            mutated = mutate(original.decode("utf-8"))
            assert mutated != original.decode("utf-8"), f"الطفرةُ لم تُطبَّق: {name}"
            TARGET.write_text(mutated, encoding="utf-8")
            for test in expected:
                rc, line = _run(f"wi107_{test}_")
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
