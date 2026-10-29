"""الهدف: جردُ الأسطحِ العامّةِ الـ33 لـM1 (national_economy · federal_state · state_treasury) من
`write_inventory_p13.json` ونداءاتِ كلِّ سطحٍ المؤثّرةِ في تصميمِ العبور: عبورُ مالٍ داخليٌّ
(`.disburse(`)، النواةُ التنفيذيّةُ (`_execute_via_core` · `.submit(` · `.run(`)، تفويضُ المال
(`resolve_money_delegation` · `_authorize_money`)، والحرسُ القائمُ (`guard_declared`) — قراءةٌ ساكنةٌ بالـAST.

النطاق: قراءةٌ فقط لملفّاتِ الشِّفرةِ وملفِّ الجرد؛ لا تشغيلَ لخدمة.
المالك: Perplexity Computer (قيدُ W-739 · WI-122).
تاريخ الإنشاء: 2026-10-29

التشغيلُ (من جذرِ المستودع):
    python3 docs/audit/evidence/W-739/m1_surface_scan.py
"""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SRC = "federal/executive/services/src/amos_federation/services/"
FILES = {
    "national_economy": SRC + "national_economy/service.py",
    "federal_state": SRC + "federal_state/service.py",
    "state_treasury": SRC + "state_treasury/service.py",
}
MARKS = {
    "disburse": lambda n: n == "disburse",
    "core": lambda n: n in {"_execute_via_core", "submit", "run"},
    "delegation": lambda n: n in {"resolve_money_delegation", "_authorize_money"},
    "guard": lambda n: n == "guard_declared",
}


def called_names(fn: ast.AST, methods: dict[str, ast.AST], depth: int = 0) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(fn):
        if isinstance(node, ast.Call):
            f = node.func
            name = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", None)
            if name:
                names.add(name)
                # يتبعُ النداءاتِ الخاصّةَ داخلَ الصنفِ نفسِه عمقًا واحدًا (self._x)
                if (
                    depth == 0
                    and isinstance(f, ast.Attribute)
                    and isinstance(f.value, ast.Name)
                    and f.value.id == "self"
                    and name.startswith("_")
                    and name in methods
                    and name != "_execute_via_core"
                ):
                    names |= {f"{n}" for n in called_names(methods[name], methods, 1)}
    return names


def main() -> int:
    inv = json.loads((ROOT / "docs/audit/measurements/write_inventory_p13.json").read_text())
    public = {}
    for s in inv["sites"]:
        for unit, path in FILES.items():
            if s["path"] == path and s["public"]:
                public.setdefault(unit, []).append((s["function"], s["guarded"]))
    total = 0
    counts = {k: 0 for k in MARKS}
    for unit, path in FILES.items():
        tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
        methods: dict[str, ast.AST] = {}
        lines: dict[str, int] = {}
        for cls in [n for n in tree.body if isinstance(n, ast.ClassDef)]:
            for fn in cls.body:
                if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    methods[fn.name] = fn
                    lines[fn.name] = fn.lineno
        rows = sorted(public.get(unit, []))
        print(f"== {unit} ({len(rows)}) · {path}")
        for name, guarded in rows:
            names = called_names(methods[name], methods)
            marks = [k for k, pred in MARKS.items() if any(pred(n) for n in names)]
            for k in marks:
                counts[k] += 1
            print(f"  {name:30} l.{lines[name]:<5} guarded={guarded!s:5} marks={marks}")
            total += 1
    print(f"SCAN SUMMARY: surfaces={total} marks={counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
