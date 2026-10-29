"""حملةُ طفرةِ W-724 — نزعُ الحارسِ من كلِّ سطحٍ ثمَّ تشغيلُ فحصِ الصنفِ 2 له.

الهدف: إثباتُ أنَّ فحصَ الصنفِ 2 يقتلُ طفرةَ نزعِ الحدِّ من كلِّ سطحٍ من الستّةِ على تأكيدِ الدليل.
النطاق: أسطحُ expansion الستّةُ في W-724 وحدَها — الطفرةُ في الذاكرةِ لا في الملفّ.
المالك: Perplexity Computer (قيدُ W-724).
تاريخ الإنشاء: 2026-10-29

لكلِّ سطح: خطُّ أساسٍ بلا طفرةٍ يجبُ أن ينجح، ثمَّ الطفرةُ (استبدالُ
`self.authorizer.guard_declared(` بمُطبِّقٍ مباشرٍ بلا حدٍّ) يجبُ أن تُسقِطَ **تأكيدَ الدليل**
تحديدًا — لا فشلًا عارضًا يُحتسبُ قتلًا (سابقةُ W-699 · المادةُ التاسعة).

التشغيلُ (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-724/mutation_campaign.py
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SERVICES = ROOT / "federal/executive/services"
OUT = Path(__file__).with_name("mutation_results.json")
TEST = "tests/test_w724_g1_expansion.py"

SURFACES = {
    "take_exam": ("SpecializationProgram", "record_curriculum_step"),
    "submit_output": ("University", "create_task"),
    "approve_output": ("University", "activate_agent"),
    "employ_batch": ("PopulationExpansion", "dispatch_agent"),
    "graduate_batch": ("PopulationExpansion", "release_agent"),
    "retire_agent": ("RetirementSystem", "contain_agent"),
}

PLUGIN = """
import inspect, os, textwrap

_DONE = []

class _Unguarded:
    def __init__(self, value):
        self.value = value
        self.is_replay = False

def _unguarded(_action, _target, *, declared_effects, applier, **_kw):
    return _Unguarded(applier(declared_effects[0]))

def pytest_runtest_setup(item):
    # بعدَ تحميلِ conftest وعزلِ القاعدة — لا استيرادَ مبكّرًا يربطُ محرّكًا بقاعدةٍ أخرى.
    if _DONE:
        return
    _DONE.append(True)
    from amos_federation.services.governance import expansion as ex

    owner_name, surface = os.environ["W724_MUTANT"].split(".")
    owner = getattr(ex, owner_name)
    src = textwrap.dedent(inspect.getsource(getattr(owner, surface)))
    assert src.count("self.authorizer.guard_declared(") == 1
    src = src.replace("self.authorizer.guard_declared(", "_unguarded(")
    scope = dict(vars(ex))
    scope["_unguarded"] = _unguarded
    exec(compile(src, ex.__file__, "exec"), scope)
    setattr(owner, surface, scope[surface])
"""


def _run(surface: str, mutant: str | None) -> tuple[int, str]:
    env = dict(os.environ)
    args = [
        str(ROOT / ".venv/bin/python"),
        "-m",
        "pytest",
        "-q",
        "-p",
        "no:cacheprovider",
        f"{TEST}::test_c2_surface_crosses_with_named_action",
        "-k",
        surface,
    ]
    with tempfile.TemporaryDirectory() as tmp:
        if mutant:
            Path(tmp, "w724_mutant_plugin.py").write_text(PLUGIN, encoding="utf-8")
            env["PYTHONPATH"] = tmp + os.pathsep + env.get("PYTHONPATH", "")
            env["W724_MUTANT"] = mutant
            args[3:3] = ["-p", "w724_mutant_plugin"]
        proc = subprocess.run(
            args, cwd=SERVICES, env=env, capture_output=True, text=True
        )
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    cases = []
    for surface, (owner, verb) in SURFACES.items():
        base_rc, _ = _run(surface, None)
        mut_rc, out = _run(surface, f"{owner}.{surface}")
        err = next((ln.strip() for ln in out.splitlines() if ln.startswith("E ")), "")
        on_evidence = mut_rc != 0 and (
            "لم يُعبَرِ الحدُّ السياديُّ أصلًا" in out
            or re.search(r"assert '[a-z_]+' == '" + verb, out)
        )
        cases.append(
            {
                "verb": verb,
                "surface": f"{owner}.{surface}",
                "test": "test_c2_surface_crosses_with_named_action",
                "baseline_without_mutation": "passed" if base_rc == 0 else "FAILED",
                "mutant_outcome": "failed_on_evidence"
                if on_evidence
                else ("survived" if mut_rc == 0 else "failed_elsewhere"),
                "failing_assertion": err,
            }
        )
    result = {
        "$comment": (
            "حملةُ طفرةِ أسطحِ W-724 (G1 الدفعة 3 · expansion): لكلِّ سطحٍ خطُّ أساسٍ ناجحٌ ثمَّ "
            "نزعُ نداءِ الحدِّ (مُطبِّقٌ مباشرٌ بلا عبور) يُسقِطُ تأكيدَ الدليلِ تحديدًا. "
            "المولِّد: docs/audit/evidence/W-724/mutation_campaign.py"
        ),
        "cases": cases,
        "killed_on_evidence": sum(
            c["mutant_outcome"] == "failed_on_evidence" for c in cases
        ),
        "total": len(cases),
    }
    OUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: result[k] for k in ("killed_on_evidence", "total")}))
    ok = all(
        c["baseline_without_mutation"] == "passed"
        and c["mutant_outcome"] == "failed_on_evidence"
        for c in cases
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
