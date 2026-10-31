"""الهدف: مسبارُ طفراتِ M1 الدفعة 1 (W-757 · WI-125) — كلُّ طفرةٍ تُطبَّقُ على نسخةِ العمل، تُشغَّلُ
الفحوص، ثمَّ يُعادُ الملفُّ كما كان. المطلوب: كلُّ طفرةٍ «قُتِلَت» (فحصٌ واحدٌ على الأقلِّ فشل) سلوكًا.

النطاق: ست طفراتٍ في `money_authority.py` و`state_treasury/service.py` · ثلاثةُ ملفّاتِ فحص.
التوجيهُ 33 § 2: «مسابير وطفرات أوسع من المعتاد (ليس طفرة موجّهة واحدة)».
المالك: Perplexity Computer (قيدُ W-757 · WI-125).
تاريخ الإنشاء: 2026-10-31
التشغيل (من جذر المستودع): .venv/bin/python docs/audit/evidence/W-757/m1_mutation_probe.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SVC = ROOT / "federal/executive/services"
SRC = SVC / "src/amos_federation/services"
MA = SRC / "executive_core/money_authority.py"
TS = SRC / "state_treasury/service.py"
TESTS = [
    "tests/test_w755_m1_treasury_single_crossing.py",
    "tests/test_r7b_state_treasury.py",
    "tests/test_treasury.py",
]

# فحصُ 6b نصّيٌّ يقتلُ M-f بالنصّ؛ يُستبعَدُ هنا ليُقاسَ القتلُ **سلوكًا**.
STATIC_6B = (
    "tests/test_w755_m1_treasury_single_crossing.py::"
    "test_m1_6b_the_unwrap_is_exact_and_does_not_swallow_sovereign_errors"
)

MUTATIONS = [
    (
        "M-a الفاعلُ مُثبَّتٌ EXECUTIVE",
        MA,
        '"authorizer": build(delegation.actor),',
        '"authorizer": build("EXECUTIVE"),',
    ),
    (
        "M-b حذفُ فكِّ اللفّ",
        MA,
        "            raise exc.__cause__ from exc\n",
        "            raise\n",
    ),
    (
        "M-c إسقاطُ المعوِّض",
        MA,
        '        "compensators": (\n            compensator(effect.signature, lambda: undo(applied.get("result")), undo_description),\n        ),',
        '        "compensators": (),',
    ),
    (
        "M-d حذفُ فحصِ التكرارِ قبلَ العبور (الحساب)",
        TS,
        "            if duplicate is not None:\n                raise DuplicateCodeError(f\"رمز الحساب '{code}' مستعمل في هذه الخزانة\")",
        "            pass",
    ),
    (
        "M-e حذفُ العبورِ من التأسيس (تطبيقٌ مباشر)",
        TS,
        '        return settle_money_crossing(\n            lambda: contract["authorizer"].guard_declared(\n                contract["action"], contract["target"], **money_crossing_kwargs(contract)\n            ),\n            contract,\n        )\n\n    # ── 2. فتح حساب',
        "        return _apply()\n\n    # ── 2. فتح حساب",
    ),
    (
        "M-f الإعادةُ تُطبِّقُ ثانيةً (تجاهلُ is_replay)",
        MA,
        "    if guarded.is_replay:",
        "    if False:",
    ),
]


def run_tests() -> tuple[int, str]:
    proc = subprocess.run(
        [
            str(ROOT / ".venv/bin/python"),
            "-m",
            "pytest",
            *TESTS,
            "-q",
            "-p",
            "no:cacheprovider",
            "-x",
            "--deselect",
            STATIC_6B,
        ],
        cwd=SVC,
        capture_output=True,
        text=True,
        check=False,
    )
    tail = [
        ln
        for ln in proc.stdout.splitlines()
        if " passed" in ln or " failed" in ln or ln.startswith("FAILED")
    ]
    return proc.returncode, " | ".join(tail[-2:])


def main() -> int:
    rc, line = run_tests()
    print(f"[الأساس] rc={rc} {line}")
    if rc != 0:
        return 2
    survived = 0
    for name, path, old, new in MUTATIONS:
        original = path.read_text(encoding="utf-8")
        count = original.count(old)
        if count < 1:
            print(f"[{name}] لم يُعثَر على النصّ — الطفرةُ غيرُ مُطبَّقة")
            survived += 1
            continue
        try:
            path.write_text(original.replace(old, new, 1), encoding="utf-8")
            rc, line = run_tests()
        finally:
            path.write_text(original, encoding="utf-8")
        verdict = "قُتِلَت" if rc != 0 else "نجَت"
        survived += rc == 0
        print(f"[{name}] {verdict} · rc={rc} · {line}")
    print(f"== المجموع: {len(MUTATIONS)} طفرات · نجا منها {survived} ==")
    return 1 if survived else 0


if __name__ == "__main__":
    sys.exit(main())
