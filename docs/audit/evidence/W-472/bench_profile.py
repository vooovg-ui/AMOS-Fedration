"""أداةُ تفكيكِ cProfile لجولةِ بذرٍ بعدَ تراكمٍ — WI-096 (محفوظةٌ لا تُحذف · W-490).

الهدف: إعادةُ إنتاجِ التفكيكِ (قبل/بعد) الذي بهِ قيسَت هيمنةُ `_atomic_write` —
أداةُ القياسِ محفوظةٌ في المستودعِ لا مخرجُها وحدَهُ (تصحيحُ مراجعةِ المستشارِ الثالثةِ § 5).
النطاق: جولةُ بذرٍ واحدةٍ بعدَ 10 جولاتِ تراكمٍ فوقَ سياقِ WI-082.
المالك: Perplexity Computer (WI-096).

التشغيلُ: تُنسَخُ إلى federal/executive/services/tests/test_zz_bench_profile.py ثمَّ
`.venv/bin/python -m pytest federal/executive/services/tests/test_zz_bench_profile.py -q -s`
(تُحذفُ النسخةُ من حزمةِ الفحوصِ بعدَ القياسِ — الأداةُ تبقى هنا مرجعًا).
"""
from __future__ import annotations

import cProfile
import io
import pstats


def test_breakdown() -> None:
    from amos_federation.services.agent_runtime.population import PopulationRegistry

    for _ in range(10):  # تراكمٌ: 10 جولاتٍ ثمَّ القياسُ على الحاديةِ عشرةِ
        PopulationRegistry().seed_initial_population()
    profiler = cProfile.Profile()
    profiler.enable()
    agents = PopulationRegistry().seed_initial_population()
    profiler.disable()
    assert len(agents) == 20
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
    stats.print_stats(30)
    print("PROFILE_OUTPUT:")
    print(stream.getvalue())
