"""الهدف: قراءةٌ ساكنةٌ (AST) لأثرِ الكتابةِ في كلٍّ من الأسطحِ الأربعةِ والعشرين لجدولِ معجمِ Q-83 (ج).

لكلِّ سطحٍ: عمليّةُ النطاق (`require_domain_permission`) · النماذجُ المُنشأة (`XModel(`) ·
النماذجُ المقروءةُ قبلَ الكتابة (`session.get`) · والدوالُّ الخاصّةُ المُناداةُ التي تُنشئُ نموذجًا.
النطاق: قراءةٌ فقط · لا تشغيلَ لشِفرةِ الإنتاج.
المالك: Perplexity Computer (WI-122 · Q-83 (ج) · قيدُ W-816).

التشغيل: .venv/bin/python docs/audit/evidence/W-816/surface_effects_scan.py
"""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "federal/executive/services/src/amos_federation/services"
FILES = {
    "federal_state": [
        "register_government",
        "set_government_status",
        "bind_institution",
        "record_relation",
        "grant_delegation",
        "revoke_delegation",
        "scope_service",
        "scope_case",
        "execute_scoped_operation",
    ],
    "national_economy": [
        "register_sector",
        "register_category",
        "define_indicator",
        "register_public_entity",
        "create_program",
        "issue_policy",
        "register_revenue_source",
        "register_public_asset",
        "register_public_liability",
        "authorize_expenditure",
        "authorize_procurement",
        "authorize_transfer",
        "activate_policy",
        "execute_economic_decision",
    ],
}


def _scan(fn: ast.FunctionDef) -> tuple[list[str], set[str], set[str], set[str]]:
    perms, made, read, priv = [], set(), set(), set()
    for c in ast.walk(fn):
        if not isinstance(c, ast.Call):
            continue
        name = ast.unparse(c.func)
        if name.endswith("require_domain_permission") and len(c.args) > 1:
            perms.append(ast.unparse(c.args[1]))
        elif name.endswith("Model") and name[:1].isupper():
            made.add(name)
        elif name.endswith("session.get") and c.args:
            read.add(ast.unparse(c.args[0]))
        elif name.startswith("self._"):
            priv.add(name[5:])
    return perms, made, read, priv


def main() -> int:
    total = 0
    for svc, names in FILES.items():
        tree = ast.parse((SRC / svc / "service.py").read_text(encoding="utf-8"))
        methods = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
        for name in names:
            fn = methods[name]
            perms, made, read, priv = _scan(fn)
            via = sorted(
                f"{p}→{sorted(_scan(methods[p])[1])}"
                for p in priv
                if p in methods and _scan(methods[p])[1]
            )
            print(
                f"{svc}.{name} L{fn.lineno}-{fn.end_lineno} · perm={perms} · creates={sorted(made)} "
                f"· reads={sorted(read)} · via={via}"
            )
            total += 1
    lc = ast.parse((SRC / "model_gateway/model_layer.py").read_text(encoding="utf-8"))
    fn = next(
        n
        for n in ast.walk(lc)
        if isinstance(n, ast.FunctionDef) and n.name == "log_cost"
    )
    print(
        f"model_gateway.log_cost L{fn.lineno}-{fn.end_lineno} · creates={sorted(_scan(fn)[1])}"
    )
    total += 1
    print(f"SCANNED={total}")
    return 0 if total == 24 else 1


if __name__ == "__main__":
    raise SystemExit(main())
