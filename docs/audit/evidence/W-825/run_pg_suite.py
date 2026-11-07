"""الهدف: قياسُ حزمةِ `services-postgres` بالأداةِ نفسِها (`run_suite` و`evaluate`) لا بأمرٍ موازٍ (W-825 · Q-99 البند 6).

التعريف: يستوردُ `SUITES` من `tools/governance/verify_cross_system_suites.py` ويشغّلُ حزمةَ PostgreSQL وحدَها
— فلا يُعادُ توليدُ `CROSS_SYSTEM_SUITE_MATRIX.md` (ذاك عملُ CI) ولا تُشغَّلُ الحزمتانِ الأخريان.
النطاق: docs/audit/evidence/W-825
المالك: Perplexity Computer (WI-127)
تاريخ الإنشاء: 2026-11-05
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "tools" / "governance"))

import verify_cross_system_suites as gate  # noqa: E402

(suite,) = [s for s in gate.SUITES if s.name == "services-postgres"]
print("targets:", *suite.targets, sep="\n  ")
print("plugins:", suite.plugins, "forbid_skips:", suite.forbid_skips)
result = gate.run_suite(suite)
print("exit_code:", result.exit_code)
print("counts:", result.counts)
print("summary:", result.summary_line)
print("violations:", result.violations or "none")
print("duration_s:", round(result.duration_s, 1))
print("--- tail ---")
print(result.tail)
print("SUITE_OK" if result.ok else "SUITE_FAIL")
sys.exit(0 if result.ok else 1)
