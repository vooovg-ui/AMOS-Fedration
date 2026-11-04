"""قياسُ مُنادي `log_cost` (W-817 · Q-97 السؤال 5 · التوجيه 42 § 2 بند 3).

الهدف: قراءةٌ فقط بلا شِّفرة — مَن ينادي `ModelLayer.log_cost` في الشِّفرةِ الإنتاجيّة،
وفي أيِّ دالّة، ومَن الفاعلُ هناك، وهل في نطاقِ النداءِ كائنُ مُصرِّحٍ (`authorizer` /
`guard_declared` / `ConstitutionalAuthorizer`) يُمكنُ أن يحملَ العبور.

الطريقة: AST لكلِّ `.py` تحتَ `federal/` و`core/` و`tools/` خارجَ `tests/`: كلُّ نداءٍ
اسمُه `log_cost` يُطبَعُ بموضعِه ودالّتِه المحيطة، ثمّ يُطبَعُ لكلِّ دالّةٍ محيطة:
- أسماءُ المعاملاتِ (ومنها معاملُ المبدأ إن كان)،
- هل يرِدُ فيها `authorizer` أو `guard_declared` أو `ConstitutionalAuthorizer`،
- النداءاتُ السياديّةُ فيها بترتيبِ الأسطرِ (`get_subsystem_boundary` · `authorized_activity`).

لا يُعدِّلُ شيئًا، والخروجُ 0 دائمًا — الحكمُ في المطبوع.

الاستعمال:
    python docs/audit/evidence/W-817/log_cost_caller_scan.py --root .
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path

ROOTS = ("federal", "core", "tools")
AUTH_NAMES = {
    "authorizer",
    "guard_declared",
    "ConstitutionalAuthorizer",
    "get_authorizer",
}
SOVEREIGN_CALLS = {"get_subsystem_boundary", "authorized_activity", "require_auth"}


def _name(node: ast.AST) -> str:
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Name):
        return node.id
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    root = Path(parser.parse_args().root).resolve()
    callers = 0
    for top in ROOTS:
        for path in sorted((root / top).rglob("*.py")):
            if "tests" in path.parts or ".venv" in path.parts:
                continue
            rel = path.relative_to(root).as_posix()
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for fn in ast.walk(tree):
                if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                calls = [
                    n
                    for n in ast.walk(fn)
                    if isinstance(n, ast.Call) and _name(n.func) == "log_cost"
                ]
                if not calls or fn.name == "log_cost":
                    continue
                for call in calls:
                    callers += 1
                    print(f"CALLER {rel}:{call.lineno} in {fn.name}()")
                params = [a.arg for a in fn.args.args + fn.args.kwonlyargs]
                print(f"  params      : {params}")
                names = {_name(n) for n in ast.walk(fn)}
                print(f"  authorizer  : {sorted(AUTH_NAMES & names) or 'NONE'}")
                seq = sorted(
                    (n.lineno, _name(n.func))
                    for n in ast.walk(fn)
                    if isinstance(n, ast.Call)
                    and _name(n.func) in SOVEREIGN_CALLS | {"log_cost"}
                )
                print(f"  order       : {seq}")
                deps = [
                    (n.lineno, ast.unparse(n)[:90])
                    for n in ast.walk(fn)
                    if isinstance(n, ast.Call) and _name(n.func) == "Depends"
                ]
                print(f"  depends     : {deps or 'NONE'}")
    print(f"CALLERS={callers}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
