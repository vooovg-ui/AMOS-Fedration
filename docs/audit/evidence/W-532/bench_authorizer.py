"""الهدف: قياسُ كلفةِ المُصرِّحِ: لكلِّ نداءٍ (نسخةُ 1c52572) أم كائنٌ واحدٌ للوحدةِ — W-532 · قرارُ المالكِ Q-62 ②.

يُنسَخُ إلى federal/executive/services/tests/test_zz_bench_authorizer.py ويُشغَّلُ بـpytest -q -s
(فتُهيِّئُ جلسةُ الفحصِ سجلَّ الذرّيّةِ والقاعدةَ) ثمَّ يُحذَف. لا يمسُّ الشِفرةَ.
"""
from __future__ import annotations

import time
import uuid

from amos_federation.services.executive_core.agent_identity import AGENT_IDENTITY_ACTOR, register_identity
from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer

N = 150


def _run(label: str, make_auth) -> float:
    ids = [f"bench-{label}-{uuid.uuid4().hex[:8]}" for _ in range(N)]
    t0 = time.perf_counter()
    for i in ids:
        register_identity(i, i, "worker", **make_auth())
    dt = time.perf_counter() - t0
    return dt


def test_bench_authorizer_cost():
    shared = ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    t_ctor0 = time.perf_counter()
    for _ in range(N):
        ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    ctor = time.perf_counter() - t_ctor0
    rounds = []
    for r in range(3):
        per_call = _run(f"pc{r}", lambda: {})
        module = _run(f"md{r}", lambda: {"authorizer": shared})
        rounds.append((per_call, module))
    print(f"\nBENCH N={N} ctor_only_total={ctor:.4f}s per_ctor={ctor / N * 1e3:.3f}ms")
    for r, (pc, md) in enumerate(rounds):
        print(f"BENCH round={r} per_call={pc:.4f}s ({pc / N * 1e3:.3f}ms/op) module={md:.4f}s ({md / N * 1e3:.3f}ms/op) ratio={pc / md:.3f}")
