"""أداةُ منحنى التراكمِ لملفِ الذرّيّةِ — WI-096 (محفوظةٌ في المستودعِ لا تُحذف).

الهدف: قياسٌ قابلٌ لإعادةِ التشغيلِ من المستودعِ لزمنِ جولةِ البذرِ (20 وكيلًا)
وحجمِ ملفِ الذرّيّةِ بالبايتاتِ عندَ كلِّ جولةٍ — قبلَ العلاجِ وبعدَهُ.
النطاق: فحصُ test_seed_initial_population_20 في حزمةِ الخدماتِ (المسارُ المشتركُ للجذرِ).
المالك: Perplexity Computer (WI-096).

التشغيلُ: تُنسَخُ هذه الأداةُ إلى federal/executive/services/tests/test_zz_bench_curve.py
ثمَّ: .venv/bin/python -m pytest federal/executive/services/tests/test_zz_bench_curve.py -q -s
(تُحذفُ النسخةُ من حزمةِ الفحوصِ بعدَ القياسِ — الأداةُ تبقى هنا مرجعًا).
"""
from __future__ import annotations

import json
import time
from pathlib import Path


def test_accumulation_curve() -> None:
    from amos_federation.services.agent_runtime.population import PopulationRegistry

    times: list[float] = []
    sizes: list[int] = []
    ledger_path = Path(
        __import__("os").environ.get(
            "AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER",
            "/tmp/amos_federation_test_artifacts/amos_federation_test_idempotency.json",
        )
    )
    for round_no in range(12):
        registry = PopulationRegistry()
        t0 = time.perf_counter()
        agents = registry.seed_initial_population()
        elapsed = time.perf_counter() - t0
        assert len(agents) == 20
        times.append(round(elapsed, 3))
        sizes.append(ledger_path.stat().st_size if ledger_path.exists() else 0)
    print("CURVE_TIMES:", times)
    print("FILE_SIZES:", sizes)
    print("RATIO:", round(times[-1] / times[1], 2))
    print("JSON:", json.dumps({"times": times, "sizes": sizes}))
