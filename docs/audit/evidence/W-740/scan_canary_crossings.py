"""الهدف: فحصُ «عبورانِ متعاقبانِ خارجَ عبورٍ واحدٍ» على أسطحِ canary الأربعةِ (A1A § 7.5/4 · قيدُ W-740).

نظيرُ أداةِ W-735 (`../W-735/scan_sequential_crossings.py`) على أسطحِ WI-114: يُحمَّلُ
إضافةً لـpytest (`-p scan_canary_crossings`) فيلفُّ الدوالَّ العامةَ الأربعَ في
`governance.canary` (`activate_kill_switch` · `reset_kill_switch` · `create_promotion` ·
`check_gate`) — النداءُ الأبعدُ وحدَه «استدعاءُ سطحٍ»؛ و`ConstitutionalAuthorizer.guard_declared`
— كلُّ عبورٍ في المستوى الأعلىِ يُنسَبُ إلى استدعاءِ السطحِ الأبعدِ الجاري. ثمَّ يكتبُ لكلِّ
سطحٍ: عددَ الاستدعاءاتِ المرصودةِ وأكبرَ عددِ عبوراتٍ في استدعاءٍ واحدٍ وتسلسلَ أفعالِه.
«≥2» = عبوراتٌ متعاقبةٌ خارجَ عبورٍ واحد. يقيسُ ما تمرُّ به الفحوصُ القائمةُ فقط. لا يمسُّ
شِفرةَ الإنتاج.
"""

from __future__ import annotations

import contextvars
import functools
import json
import os
from collections import defaultdict

MODULE = "amos_federation.services.governance.canary"
SURFACES = (
    "activate_kill_switch",
    "reset_kill_switch",
    "create_promotion",
    "check_gate",
)

_inv: contextvars.ContextVar = contextvars.ContextVar("scan_inv", default=None)
_depth: contextvars.ContextVar = contextvars.ContextVar("scan_depth", default=0)
STATS: dict[str, dict] = defaultdict(
    lambda: {"calls": 0, "max": 0, "seqs": defaultdict(int)}
)


def _wrap_surface(qual: str, fn):
    @functools.wraps(fn)
    def wrapper(*a, **kw):
        if _inv.get() is not None:
            return fn(*a, **kw)
        rec: list[str] = []
        tok = _inv.set(rec)
        try:
            return fn(*a, **kw)
        finally:
            _inv.reset(tok)
            s = STATS[qual]
            s["calls"] += 1
            s["max"] = max(s["max"], len(rec))
            s["seqs"][" → ".join(rec) or "(لا عبور)"] += 1

    return wrapper


def _install() -> None:
    from amos_federation.services.executive_core.sovereignty_bridge import (
        ConstitutionalAuthorizer,
    )

    orig = ConstitutionalAuthorizer.guard_declared

    @functools.wraps(orig)
    def guard(self, action, target, **kw):
        rec = _inv.get()
        if rec is not None and _depth.get() == 0:
            rec.append(f"{action}@{str(target).split(':')[0]}")
        tok = _depth.set(_depth.get() + 1)
        try:
            return orig(self, action, target, **kw)
        finally:
            _depth.reset(tok)

    ConstitutionalAuthorizer.guard_declared = guard
    import importlib

    mod = importlib.import_module(MODULE)
    for mname in SURFACES:
        setattr(
            mod,
            mname,
            _wrap_surface(f"canary.{mname}", getattr(mod, mname)),
        )


def pytest_collection_finish(
    session,
):  # بعدَ conftest والجمعِ: الوحدةُ مستورَدةٌ ببيئةِ الفحوصِ نفسِها
    _install()


def pytest_unconfigure(config):
    out = os.environ.get("SCAN_OUT", "scan_canary_crossings.json")
    data = {
        "$comment": "الهدف: مخرجُ فحصِ العبوراتِ المتعاقبةِ لأسطحِ canary الأربعةِ (W-740) — max ≥ 2 = عبوراتٌ متعاقبةٌ خارجَ عبورٍ واحد",
        "surfaces": {
            k: {
                "calls": v["calls"],
                "max_crossings_per_call": v["max"],
                "sequences": dict(v["seqs"]),
            }
            for k, v in sorted(STATS.items())
        },
    }
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)


def _summarize(paths: list[str]) -> int:
    """يدمجُ مخرجاتِ عدّةِ تشغيلاتٍ ويطبعُ جدولَ الأسطحِ — EXIT 0 دائمًا (قياسٌ لا بوّابة)."""
    merged: dict[str, dict] = {}
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for k, v in json.load(fh)["surfaces"].items():
                m = merged.setdefault(
                    k, {"calls": 0, "max": 0, "seqs": defaultdict(int)}
                )
                m["calls"] += v["calls"]
                m["max"] = max(m["max"], v["max_crossings_per_call"])
                for s, n in v["sequences"].items():
                    m["seqs"][s] += n
    print(f"{'max':>3} {'calls':>5}  surface  —  أطولُ تسلسلٍ مرصود")
    for k in sorted(merged, key=lambda k: (-merged[k]["max"], k)):
        m = merged[k]
        longest = max(m["seqs"], key=lambda s: (s.count("→"), m["seqs"][s]))
        flag = "  ⚠ متعاقبة" if m["max"] >= 2 else ""
        print(f"{m['max']:>3} {m['calls']:>5}  {k}  —  {longest}{flag}")
    print(
        f"SCAN SUMMARY: surfaces={len(merged)} sequential(max>=2)={sum(m['max'] >= 2 for m in merged.values())}"
    )
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(_summarize(sys.argv[1:]))
