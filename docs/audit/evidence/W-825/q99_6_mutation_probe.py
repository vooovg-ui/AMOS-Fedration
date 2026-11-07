"""الهدف: مسبارُ طفراتِ تشديدِ حزمةِ PostgreSQL (Q-99 البند 6 · W-825) — كلُّ طفرةٍ يجبُ أن تُقتَل.

التعريف: يطبّقُ طفرةً واحدةً نصّيّةً على ملفٍّ واحد، يشغّلُ الفحصَ القاتلَ، ثمّ يعيدُ الملفَّ مطابقًا بالبايت.
م1 تُقاسُ على PostgreSQL حقيقيٍّ (تلزمُها AMOS_RUN_POSTGRES_TESTS وAMOS_TEST_DATABASE_URL).
النطاق: docs/audit/evidence/W-825
المالك: Perplexity Computer (WI-127)
تاريخ الإنشاء: 2026-11-05
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SVC = ROOT / "federal/executive/services"
PY = str(ROOT / ".venv/bin/python")
PLUGIN = SVC / "tests/pg_session_dialect.py"
TOOL = ROOT / "tools/governance/verify_cross_system_suites.py"

GOV = (
    [
        PY,
        "-m",
        "pytest",
        "-q",
        "-p",
        "no:cacheprovider",
        "tests/governance/test_cross_system_suites.py",
    ],
    ROOT,
)
UNIT = (
    [
        PY,
        "-m",
        "pytest",
        "-q",
        "-p",
        "no:cacheprovider",
        "tests/test_pg_session_dialect_plugin.py",
    ],
    SVC,
)
PGRUN = (
    [
        PY,
        "-m",
        "pytest",
        "-q",
        "-p",
        "no:cacheprovider",
        "-p",
        "tests.pg_session_dialect",
        "tests/test_r8_q97_federal_state_crossing.py",
        "-k",
        "q97_0 or q97_2",
    ],
    SVC,
)

MUTATIONS = [
    (
        "M1 plugin does not switch the session",
        PLUGIN,
        '    os.environ["AMOS_DATABASE_URL"] = os.environ[PG_URL_ENV]\n',
        "",
        PGRUN,
    ),
    (
        "M2 plugin dropped from SUITES",
        TOOL,
        '        plugins=("tests.pg_session_dialect",),\n',
        "",
        GOV,
    ),
    (
        "M3 q98 crossing file dropped",
        TOOL,
        '            "tests/test_r9_economy_q98_crossing.py",\n',
        "",
        GOV,
    ),
    (
        "M4 env gate always passes",
        PLUGIN,
        '    if env.get(PG_FLAG_ENV) != "1":\n',
        "    if False:\n",
        UNIT,
    ),
    (
        "M5 dialect gate always passes",
        PLUGIN,
        "    if dialect != REQUIRED_DIALECT:\n",
        "    if False:\n",
        UNIT,
    ),
    (
        "M6 hook skips the dialect check",
        PLUGIN,
        "    reason = dialect_violation(database.db_dialect())\n",
        "    reason = None\n",
        UNIT,
    ),
]

survived = 0
for name, path, old, new, (cmd, cwd) in MUTATIONS:
    original = path.read_bytes()
    text = original.decode()
    assert text.count(old) == 1, f"{name}: anchor not unique"
    path.write_text(text.replace(old, new), encoding="utf-8")
    try:
        env = dict(os.environ, OTEL_SDK_DISABLED="true")
        proc = subprocess.run(
            cmd, cwd=cwd, env=env, capture_output=True, text=True, check=False
        )
        last = [ln for ln in proc.stdout.splitlines() if ln.strip()][-1:] or [
            "<no output>"
        ]
        killed = proc.returncode != 0
        survived += not killed
        print(
            f"{name:40s} pytest_exit={proc.returncode} {'KILLED' if killed else 'SURVIVED'} · {last[0]}"
        )
    finally:
        path.write_bytes(original)
    assert path.read_bytes() == original
print("files restored byte-identical: True")
print(f"MUTATION RESULT: total={len(MUTATIONS)} survived={survived}")
sys.exit(1 if survived else 0)
