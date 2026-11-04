"""الهدف: طفراتُ Q-98 للدفعةِ 2 (national_economy) — يجبُ أن تُقتَلَ الثمانيَ عشرةَ كلُّها (W-820).

الصنفُ أ (9 طفرات · الحصر): نسخةُ `core/` في مجلدٍ مؤقّت، ويُحذَفُ منها فعلٌ واحدٌ من
`EXECUTIVE_ACTIONS` في `rules.py` (نصًّا على القرص)، ثمّ يُشغَّلُ المسبارُ الخام
`q98_engine_probe.py --root <المؤقّت>` ⇒ يجبُ أن يخرجَ 1 (الطفرةُ مقتولة).

الصنفُ ب (9 طفرات · العبور): في `national_economy/service.py` يُستبدَلُ نداءُ
`self.authorizer.guard_declared(` في جسمِ سطحٍ واحدٍ بمُطبِّقٍ مباشرٍ يتجاوزُ الحدّ،
ثمّ يُشغَّلُ `tests/test_r9_economy_q98_crossing.py -k <الفعل>` ⇒ يجبُ أن يفشل.
ويُعادُ الملفُّ الأصليُّ في `finally` ويُقارَنُ بصمةً قبلَ الخروج.

الخروج: 0 إن قُتِلَت الطفراتُ كلُّها وعادَ الملفُّ كما كان، وإلّا 1.
المالك: Perplexity Computer (WI-127 · قرارُ Q-98 · قيدُ W-820).

التشغيل (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-819/q98_mutation_probe.py
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
PROBE = Path(__file__).resolve().parent / "q98_engine_probe.py"
SERVICES = ROOT / "federal" / "executive" / "services"
SERVICE = (
    SERVICES
    / "src"
    / "amos_federation"
    / "services"
    / "national_economy"
    / "service.py"
)
VERBS = (
    "register_sector",
    "register_category",
    "define_indicator",
    "register_public_entity",
    "create_program",
    "issue_policy",
    "register_revenue_source",
    "register_public_asset",
    "register_public_liability",
)
BYPASS = """

def _q98_bypass(action, target, *, declared_effects, applier, **_kwargs):  # طفرة
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
            line = f'        "{verb}",\n'
            assert text.count(line) == 1, verb
            rules.write_text(text.replace(line, ""), encoding="utf-8")
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
        for verb in VERBS:
            start = original.index(f"    def {verb}(")
            at = original.index("self.authorizer.guard_declared(", start)
            mutated = (
                original[:at]
                + "_q98_bypass("
                + original[at + len("self.authorizer.guard_declared(") :]
                + BYPASS
            )
            SERVICE.write_text(mutated, encoding="utf-8")
            proc = subprocess.run(
                [
                    str(PY),
                    "-m",
                    "pytest",
                    "tests/test_r9_economy_q98_crossing.py",
                    "-q",
                    "-p",
                    "no:cacheprovider",
                    "-k",
                    verb,
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
    print(f"MUTATION RESULT: total=18 survived={a + b}")
    return 1 if a + b else 0


if __name__ == "__main__":
    sys.exit(main())
