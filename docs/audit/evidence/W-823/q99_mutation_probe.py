"""الهدف: طفراتُ Q-99 للدفعةِ 3 (أسطحُ الخزانةِ في national_economy) — يجبُ أن تُقتَلَ الستُّ كلُّها (W-823).

الصنفُ أ (3 طفرات · الحصر): نسخةُ `core/` في مجلدٍ مؤقّت، ويُحذَفُ منها فعلٌ واحدٌ من
`TREASURY_ACTIONS` في `rules.py` (نصًّا على القرص)، ثمّ يُشغَّلُ المسبارُ الخام
`q99_engine_probe.py --root <المؤقّت>` ⇒ يجبُ أن يخرجَ 1 (الطفرةُ مقتولة).

الصنفُ ب (3 طفرات · العبور): في `national_economy/service.py` يُستبدَلُ نداءُ
`contract["authorizer"].guard_declared(` في جسمِ سطحٍ واحدٍ بمُطبِّقٍ مباشرٍ يتجاوزُ الحدّ،
ثمّ يُشغَّلُ `tests/test_r9_economy_q99_treasury_crossing.py -k <حالاتُ السطح>` ⇒ يجبُ أن يفشل.
ويُعادُ الملفُّ الأصليُّ في `finally` ويُقارَنُ بصمةً قبلَ الخروج.

الخروج: 0 إن قُتِلَت الطفراتُ كلُّها وعادَ الملفُّ كما كان، وإلّا 1.
النطاق: نسخٌ مؤقّتةٌ لـcore/ وكتابةٌ مُستعادةٌ لملفِّ الخدمة — لا أثرَ باقٍ.
المالك: Perplexity Computer (WI-127 · قرارُ Q-99 · قيدُ W-823).

التشغيل (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-823/q99_mutation_probe.py
"""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PY = ROOT / ".venv" / "bin" / "python"
PROBE = Path(__file__).resolve().parent / "q99_engine_probe.py"
SERVICES = ROOT / "federal" / "executive" / "services"
SERVICE = (
    SERVICES
    / "src"
    / "amos_federation"
    / "services"
    / "national_economy"
    / "service.py"
)
VERBS = ("authorize_expenditure", "award_procurement", "authorize_transfer")
#: السطح ⇒ مُرشِّحُ `-k` لحالاتِه في ملفِّ العبور
SURFACES = {
    "authorize_expenditure": "expenditure",
    "authorize_procurement": "procurement",
    "authorize_transfer": "grant or subsidy",
}
GUARD = 'contract["authorizer"].guard_declared('
BYPASS = """

def _q99_bypass(action, target, *, declared_effects, applier, **_kwargs):  # طفرة
    class _Result:
        is_replay = False
        value = None

    result = _Result()
    result.value = applier(declared_effects[0])
    return result
"""


def rules_mutations() -> int:
    survived = 0
    for verb in VERBS:
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(ROOT / "core", Path(tmp) / "core")
            rules = Path(tmp) / "core" / "constitutional_engine" / "rules.py"
            text = rules.read_text(encoding="utf-8")
            start = text.index("TREASURY_ACTIONS = frozenset({")
            end = text.index("})", start)
            block = text[start:end]
            token = f'"{verb}",'
            assert block.count(token) == 1, verb
            rules.write_text(
                text[:start] + block.replace(token, "") + text[end:], encoding="utf-8"
            )
            rc = subprocess.run(
                [str(PY), str(PROBE), "--root", tmp], capture_output=True, text=True
            ).returncode
        killed = rc != 0
        survived += 0 if killed else 1
        print(
            f"A rules-drop {verb:24} probe_exit={rc} {'KILLED' if killed else 'SURVIVED'}"
        )
    return survived


def guard_mutations() -> int:
    original = SERVICE.read_text(encoding="utf-8")
    digest = hashlib.sha256(original.encode()).hexdigest()
    survived = 0
    env = {**os.environ, "OTEL_SDK_DISABLED": "true"}
    try:
        for verb, selector in SURFACES.items():
            start = original.index(f"    def {verb}(")
            at = original.index(GUARD, start)
            mutated = (
                original[:at] + "_q99_bypass(" + original[at + len(GUARD) :] + BYPASS
            )
            SERVICE.write_text(mutated, encoding="utf-8")
            proc = subprocess.run(
                [
                    str(PY),
                    "-m",
                    "pytest",
                    "tests/test_r9_economy_q99_treasury_crossing.py",
                    "-q",
                    "-p",
                    "no:cacheprovider",
                    "-k",
                    selector,
                ],
                cwd=SERVICES,
                capture_output=True,
                text=True,
                env=env,
            )
            tail = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else ""
            killed = proc.returncode != 0
            survived += 0 if killed else 1
            print(
                f"B guard-drop {verb:24} pytest_exit={proc.returncode} "
                f"{'KILLED' if killed else 'SURVIVED'} · {tail}"
            )
    finally:
        SERVICE.write_text(original, encoding="utf-8")
    restored = hashlib.sha256(SERVICE.read_bytes()).hexdigest() == digest
    print(f"service.py restored byte-identical: {restored}")
    return survived + (0 if restored else 1)


def main() -> int:
    a = rules_mutations()
    b = guard_mutations()
    print(f"MUTATION RESULT: total=6 survived={a + b}")
    return 1 if a + b else 0


if __name__ == "__main__":
    sys.exit(main())
