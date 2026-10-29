"""الهدف: فحصُ «عبورانِ متعاقبانِ خارجَ عبورٍ واحدٍ» على أسطحِ G1 المنفَّذةِ (التوجيهُ 29 § 2 · قيدُ W-735).

يُحمَّلُ إضافةً لـpytest (`-p scan_sequential_crossings`) فيلفُّ:
  * كلَّ دالّةٍ عامّةٍ في أصنافِ وحداتِ G1 المنفَّذةِ (state_runtime · system_life · expansion ·
    learning_cycle · security) و`PopulationRegistry.update_state` (سطحُ E1 للمقارنة) — النداءُ الأبعدُ
    وحدَه «استدعاءُ سطحٍ»؛
  * `ConstitutionalAuthorizer.guard_declared` — كلُّ عبورٍ في المستوى الأعلى (لا داخلَ عبورٍ آخر)
    يُنسَبُ إلى استدعاءِ السطحِ الأبعدِ الجاري.
ثمَّ يكتبُ لكلِّ سطحٍ: عددَ الاستدعاءاتِ المرصودةِ في الفحوصِ وأكبرَ عددِ عبوراتٍ في استدعاءٍ واحدٍ وتسلسلَ
أفعالِه. «≥2» = عبوراتٌ متعاقبةٌ خارجَ عبورٍ واحد. يقيسُ ما تمرُّ به الفحوصُ القائمةُ فقط — سطحٌ لم تستدعِه
الفحوصُ يُكتَبُ «لم يُرصَد» لا «نظيف». لا يمسُّ شِفرةَ الإنتاج.
"""

from __future__ import annotations

import contextvars
import functools
import importlib
import inspect
import json
import os
from collections import defaultdict

MODULES = (
    "amos_federation.services.governance.state_runtime",
    "amos_federation.services.governance.system_life",
    "amos_federation.services.governance.expansion",
    "amos_federation.services.governance.learning_cycle",
    "amos_federation.services.governance.security",
)
EXTRA = (
    (
        "amos_federation.services.agent_runtime.population",
        "PopulationRegistry",
        "update_state",
    ),
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
    for name in MODULES:
        mod = importlib.import_module(name)
        for cname, cls in vars(mod).items():
            if not inspect.isclass(cls) or cls.__module__ != name:
                continue
            for mname, m in list(vars(cls).items()):
                if mname.startswith("_") or not inspect.isfunction(m):
                    continue
                setattr(
                    cls,
                    mname,
                    _wrap_surface(f"{name.rsplit('.', 1)[1]}.{cname}.{mname}", m),
                )
    for name, cname, mname in EXTRA:
        cls = getattr(importlib.import_module(name), cname)
        setattr(
            cls,
            mname,
            _wrap_surface(
                f"{name.rsplit('.', 1)[1]}.{cname}.{mname}", vars(cls)[mname]
            ),
        )


def pytest_collection_finish(
    session,
):  # بعدَ conftest والجمعِ: الوحداتُ مستورَدةٌ ببيئةِ الفحوصِ نفسِها
    _install()


def pytest_unconfigure(config):
    out = os.environ.get("SCAN_OUT", "scan_sequential_crossings.json")
    data = {
        "$comment": "الهدف: مخرجُ فحصِ العبوراتِ المتعاقبةِ لكلِّ سطحٍ (W-735) — max ≥ 2 = عبوراتٌ متعاقبةٌ خارجَ عبورٍ واحد",
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
