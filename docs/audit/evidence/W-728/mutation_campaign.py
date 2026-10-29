"""حملةُ طفرةِ W-728 — نزعُ الحارسِ من كلِّ سطحٍ ثمَّ تشغيلُ فحصِ الصنفِ 2 له.

الهدف: إثباتُ أنَّ فحصَ الصنفِ 2 يقتلُ طفرةَ نزعِ الحدِّ من كلِّ سطحٍ من
التسعةِ على تأكيدِ الدليل.

النطاق: أسطحُ learning_cycle وsecurity التسعةُ في W-728 وحدَها — الطفرةُ في
الذاكرةِ لا في الملفّ.

المالك: Perplexity Computer (قيدُ W-728).
تاريخ الإنشاء: 2026-10-29

لكلِّ سطح: خطُّ أساسٍ بلا طفرةٍ يجبُ أن ينجح، ثمَّ الطفرةُ (استبدالُ
`self.authorizer.guard_declared(` بمُطبِّقٍ مباشرٍ بلا حدٍّ) يجبُ أن تُسقِطَ **تأكيدَ
الدليلِ** تحديدًا — لا فشلًا عارضًا يُحتسبُ قتلًا (سابقةُ W-699 · W-724).

التشغيلُ (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-728/mutation_campaign.py
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
TEST = "tests/test_w728_g1_learning_security.py"

SURFACES = {
    "collect_experiences": ("learning_cycle", "LearningCycle", "record_curriculum_step"),
    "complete_training": ("learning_cycle", "LearningCycle", "release_agent"),
    "start_shadow": ("learning_cycle", "ModelPromotionCycle", "invoke_model"),
    "start_canary": ("learning_cycle", "ModelPromotionCycle", "invoke_model"),
    "promote_beta_to_alpha": ("learning_cycle", "ModelPromotionCycle", "activate_agent"),
    "create_session": ("security", "RBACSystem", "execute_task"),
    "check_rate": ("security", "RateLimiter", "log_isolated_action"),
    "issue_certificate": ("security", "TLSCertManager", "issue_certificate"),
    "verify_certificate": ("security", "TLSCertManager", "log_isolated_action"),
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
    from amos_federation.services.governance import learning_cycle as lc_mod
    from amos_federation.services.governance import security as sec_mod

    module_name, owner_name, surface = os.environ["W728_MUTANT"].split(".")
    module = lc_mod if module_name == "learning_cycle" else sec_mod
    owner = getattr(module, owner_name)
    src = textwrap.dedent(inspect.getsource(getattr(owner, surface)))
    assert src.count("self.authorizer.guard_declared(") == 1
    src = src.replace("self.authorizer.guard_declared(", "_unguarded(")
    scope = dict(vars(module))
    scope["_unguarded"] = _unguarded
    exec(compile(src, module.__file__, "exec"), scope)
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
            Path(tmp, "w728_mutant_plugin.py").write_text(PLUGIN, encoding="utf-8")
            env["PYTHONPATH"] = tmp + os.pathsep + env.get("PYTHONPATH", "")
            env["W728_MUTANT"] = mutant
            args[3:3] = ["-p", "w728_mutant_plugin"]
        proc = subprocess.run(
            args, cwd=SERVICES, env=env, capture_output=True, text=True
        )
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    cases = []
    for surface, (module_name, owner, verb) in SURFACES.items():
        base_rc, _ = _run(surface, None)
        mut_rc, out = _run(surface, f"{module_name}.{owner}.{surface}")
        err = next((ln.strip() for ln in out.splitlines() if ln.startswith("E ")), "")
        on_evidence = mut_rc != 0 and (
            "لم يُعبَرِ الحدُّ السياديُّ أصلًا" in out
            or re.search(r"assert '[a-z_]+' == '" + verb, out)
        )
        cases.append(
            {
                "verb": verb,
                "surface": f"{module_name}.{owner}.{surface}",
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
            "حملةُ طفرةِ أسطحِ W-728 (G1 الدفعة 4 · learning_cycle + security): لكلِّ "
            "سطحٍ من التسعةِ خطُّ أساسٍ ناجحٌ ثمَّ نزعُ نداءِ الحدِّ (مُطبِّقٌ مباشرٌ بلا "
            "عبور) يُسقِطُ تأكيدَ الدليلِ تحديدًا. "
            "المولِّد: docs/audit/evidence/W-728/mutation_campaign.py"
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
