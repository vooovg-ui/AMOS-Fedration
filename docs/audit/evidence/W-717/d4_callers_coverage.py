#!/usr/bin/env python3
"""تحليلٌ قياسيٌّ لمساراتِ الاستدعاءِ العامةِ لمواقعِ كتابةِ persistent.py (WI-118) — قياسٌ لا حكم.

السؤالُ (التوجيهُ 24 § 1): هل تُعدُّ كتابةُ persistent.py مغطّاةً إذا كانت كلُّ مساراتِ
استدعائِها العامةِ محروسةً؟ مع عددِ المساراتِ غيرِ المحروسةِ اليومَ لكلِّ موقع.

هذه الأداةُ **لا تغيِّرُ مقياسَ D-4** ولا تُستعمَلُ بوّابةً: هي تَعُدُّ وتعرضُ فقط.

التعريفاتُ المستعمَلةُ (معلَنةٌ لتُنقَدَ):
- **الموقعُ**: إحدى العمليّاتِ العامّةِ الـ13 في persistent.py التي يعدُّها
  `tools/audit/sovereign_write_inventory.py` «لا تعبرُ الحدَّ» (المصدرُ: حِملُ الجردِ نفسُه).
- **موقعُ الاستدعاءِ المباشر**: نداءٌ `X.m(...)` في ملفِّ إنتاجٍ (بتعريفِ أداةِ الجردِ نفسِها)
  حيثُ يُحَلُّ `X` ساكنًا إلى نسخةٍ من الصنفِ (`Cls()` مباشرةً · اسمٌ أُسنِدَ إليه `Cls()` في
  الوحدةِ نفسِها · مُعيدٌ (getter) في الوحدةِ نفسِها يُعيدُ نسخةً · `module.alias` لاسمٍ معرَّفٍ
  في وحدةٍ أخرى مستوردةٍ).
- **المدخلُ العامُّ**: (أ) معالِجُ HTTP (مزخرفٌ بـ`@<x>.get/post/put/patch/delete/api_route/
  websocket`) (ب) معالِجُ حدثٍ مُشترَكٌ (`subscribe(..., handler)`) (ج) نداءٌ على مستوى الوحدةِ
  (عندَ الاستيراد) (د) جذرٌ بلا مُنادٍ إنتاجيٍّ محلولٍ ساكنًا — يُعلَنُ «جذرًا غيرَ محلول».
- **المسارُ**: سلسلةُ نداءاتٍ بسيطةٌ (بلا تكرارِ دالّةٍ) من مدخلٍ عامٍّ إلى موقعِ الكتابة.
- **المسارُ المحروس**: حلقةٌ واحدةٌ على الأقلِّ من السلسلةِ (أو نداءُ الكتابةِ نفسُه) تقعُ
  لفظيًّا داخلَ دالّةٍ متداخلةٍ أو `lambda` **مُمرَّرةٍ وسيطًا** إلى نداءٍ في دالّةٍ أمٍّ يصلُ
  إلى `guard_declared(` (في جسدِها أو في معاونٍ من وحدتِها تناديه). أي أنَّ الكتابةَ تُنفَّذُ
  مُطبِّقًا (applier) أو معوِّضًا تحتَ الحدِّ. ووجودُ `guard_declared(` في جسدِ المُنادي
  والكتابةُ خارجَ المُطبِّقِ **لا يُعدُّ حراسةً** (تُنفَّذُ الكتابةُ خارجَ الحدّ).
- الحراسةُ بالهويّةِ (`require_king` · `Depends(...)`) تُسجَّلُ معلومةً ثانويّةً للمدخلِ
  ولا تُعدُّ حراسةً بتعريفِ D-4 (D-4 يقيسُ عبورَ الحدِّ السياديِّ لا المصادقة).

الحدودُ المعلَنة:
- تحليلٌ ساكنٌ (AST): النداءُ الديناميكيُّ (getattr · حقنٌ بوسيطٍ · سجلّاتُ معالِجاتٍ) لا يُرى
  إلا إن أُسنِدَ اسمًا. وما لا يُحَلُّ يظهرُ «جذرًا غيرَ محلول» لا يُسقَط.
- حلُّ المُنادين بالاسمِ داخلَ الوحدةِ وبالاستيرادِ وبالنسخِ المُسنَدةِ عبرَ الوحدات —
  ونداءُ دالّةٍ باسمٍ مجرَّدٍ يتطابقُ مع غيرِها في وحدةٍ لا تستوردُها لا يُعَدّ.
- الأداةُ لا تشغّلُ شيئًا ولا تكتبُ في قاعدة.

الاستعمال:
    .venv/bin/python docs/audit/evidence/W-717/d4_callers_coverage.py --json OUT.json > OUT.txt
"""

from __future__ import annotations

import argparse
import ast
import json
import sys
from collections import defaultdict
from collections.abc import Iterator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "tools" / "audit"))
import sovereign_write_inventory as inv  # noqa: E402

PERSISTENT = "federal/executive/services/src/amos_federation/common/persistent.py"
ROUTE_VERBS = {
    "get",
    "post",
    "put",
    "patch",
    "delete",
    "api_route",
    "websocket",
    "head",
    "options",
}
GUARD = "guard_declared("
MAX_PATHS = 5000


def last(node: ast.AST | None) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


class Fn:
    """دالّةٌ إنتاجيّة: مفتاحُها (وحدةٌ · اسمٌ مؤهَّلٌ لفظيًّا)."""

    def __init__(
        self, module: str, qual: str, node: ast.AST, cls: str | None, parent: Fn | None
    ):
        self.module, self.qual, self.node, self.cls, self.parent = (
            module,
            qual,
            node,
            cls,
            parent,
        )
        self.name = qual.rsplit(".", 1)[-1]
        self.key = f"{module}::{qual}"
        self.src = ""
        self.route: str | None = None
        self.auth: list[str] = []

    def __repr__(self) -> str:  # pragma: no cover
        return self.key


def site_list() -> list[tuple[str, str]]:
    sites = inv.collect(ROOT)
    out = []
    for s in sites:
        if s.path == PERSISTENT and s.public and not s.guarded and not s.closed_legacy:
            out.append((s.owner, s.function))
    return sorted(set(out))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", dest="json_out")
    args = ap.parse_args()

    sites = site_list()
    site_set = set(sites)
    store_classes = {c for c, _ in sites}

    files = [
        p
        for p in inv.iter_source_files(ROOT)
        if inv.is_production_file(p.relative_to(ROOT))
    ]
    mods: dict[str, ast.Module] = {}
    texts: dict[str, str] = {}
    for p in files:
        rel = str(p.relative_to(ROOT))
        text = p.read_text(encoding="utf-8")
        # ملفُّ إنتاجٍ لا يُحلَّلُ يُسقِطُ القياسَ كلَّه — لا يُتخطّى بصمت (الجردُ نفسُه يُحلِّلُها كلَّها).
        mods[rel] = ast.parse(text, filename=rel)
        texts[rel] = text

    # ---- 1. الدوالّ وأصنافُ الإنتاج
    fns: dict[str, Fn] = {}
    by_module_name: dict[str, dict[str, list[Fn]]] = defaultdict(
        lambda: defaultdict(list)
    )
    class_methods: dict[str, dict[str, list[Fn]]] = defaultdict(
        lambda: defaultdict(list)
    )
    class_module: dict[str, set[str]] = defaultdict(set)
    fn_of_node: dict[int, Fn] = {}

    def walk(
        module: str, node: ast.AST, prefix: str, cls: str | None, parent: Fn | None
    ) -> None:
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.ClassDef):
                class_module[child.name].add(module)
                walk(module, child, f"{prefix}{child.name}.", child.name, parent)
            elif isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                f = Fn(
                    module,
                    f"{prefix}{child.name}",
                    child,
                    cls if parent is None else None,
                    parent,
                )
                f.src = ast.get_source_segment(texts[module], child) or ""
                for d in child.decorator_list:
                    if (
                        isinstance(d, ast.Call)
                        and isinstance(d.func, ast.Attribute)
                        and d.func.attr in ROUTE_VERBS
                    ):
                        path = (
                            d.args[0].value
                            if d.args and isinstance(d.args[0], ast.Constant)
                            else "?"
                        )
                        f.route = f"{d.func.attr.upper()} {path}"
                        for kw in d.keywords:
                            if kw.arg == "dependencies":
                                f.auth.append(ast.unparse(kw.value))
                if f.route:
                    for a in (
                        child.args.posonlyargs + child.args.args + child.args.kwonlyargs
                    ):
                        if a.annotation is not None:
                            for sub in ast.walk(a.annotation):
                                if (
                                    isinstance(sub, ast.Call)
                                    and last(sub.func) == "Depends"
                                ):
                                    f.auth.append(ast.unparse(sub))
                    for dflt in child.args.defaults + [
                        x for x in child.args.kw_defaults if x is not None
                    ]:
                        if isinstance(dflt, ast.Call) and last(dflt.func) == "Depends":
                            f.auth.append(ast.unparse(dflt))
                    for sub in ast.walk(child):
                        if isinstance(sub, ast.Call) and last(sub.func) in {
                            "require_king",
                            "require_auth",
                            "require_role",
                        }:
                            f.auth.append(f"body:{last(sub.func)}()")
                    f.auth = sorted(set(f.auth))
                fns[f.key] = f
                fn_of_node[id(child)] = f
                by_module_name[module][child.name].append(f)
                if f.cls and parent is None:
                    class_methods[f.cls][child.name].append(f)
                walk(module, child, f"{prefix}{child.name}.", None, f)

    for m, t in mods.items():
        walk(m, t, "", None, None)
    prod_classes = set(class_module)

    # ---- 2. الأسماءُ المُسنَدةُ إلى نسخِ أصنافٍ — بنطاقٍ: الوحدة · الدالّة · سماتُ الصنف (self.x)
    imports = {m: import_map(m, t, mods) for m, t in mods.items()}
    local_imports: dict[str, dict[str, tuple[str, str | None]]] = {}
    for f in fns.values():
        local_imports[f.key] = import_map(f.module, f.node, mods, own_only=True)
    all_classes = prod_classes | store_classes
    alias: dict[str, dict[str, str]] = defaultdict(
        dict
    )  # module -> name -> class (نطاقُ الوحدة)
    local_alias: dict[str, dict[str, str]] = defaultdict(
        dict
    )  # fn key -> name -> class
    self_alias: dict[tuple[str, str], dict[str, str]] = defaultdict(
        dict
    )  # (module, class) -> attr -> class
    getters: dict[str, dict[str, str]] = defaultdict(dict)  # module -> fn -> class

    def getter_class(m: str, call: ast.Call) -> str | None:
        n = last(call.func)
        if n in all_classes:
            return n
        if isinstance(call.func, ast.Name):
            if n in getters[m]:
                return getters[m][n]
            src = imports[m].get(n)
            if src and src[1] and src[1] in getters.get(src[0], {}):
                return getters[src[0]][src[1]]
        if isinstance(call.func, ast.Attribute) and isinstance(
            call.func.value, ast.Name
        ):
            modref = imports[m].get(call.func.value.id)
            if modref and modref[1] is None and n in getters.get(modref[0], {}):
                return getters[modref[0]][n]
        return None

    def ann_class(a: ast.expr | None) -> str | None:
        if a is None:
            return None
        if isinstance(a, ast.Constant) and isinstance(a.value, str):
            nm = a.value.split("|")[0].strip().split(".")[-1]
            return nm if nm in all_classes else None
        if isinstance(a, ast.BinOp):
            return ann_class(a.left) or ann_class(a.right)
        if isinstance(a, ast.Subscript):
            return ann_class(a.slice)
        nm = last(a)
        return nm if nm in all_classes else None

    def owner_fn(node_stack: list) -> Fn | None:
        for x in reversed(node_stack):
            if id(x) in fn_of_node:
                return fn_of_node[id(x)]
        return None

    for _ in range(4):  # مُعيداتٌ تُعيدُ أسماءً تُسنَدُ من مُعيدات — نقطةٌ ثابتةٌ بأربعِ جولات
        for m, t in mods.items():

            def scan(node: ast.AST, st: list, m: str = m) -> None:
                if (
                    isinstance(node, (ast.Assign, ast.AnnAssign))
                    and node.value is not None
                ):
                    cls = (
                        getter_class(m, node.value)
                        if isinstance(node.value, ast.Call)
                        else None
                    )
                    if cls is None and isinstance(node, ast.AnnAssign):
                        cls = None  # التعليقُ وحدَه لا يُسنِدُ نسخة
                    if cls:
                        f = owner_fn(st)
                        tg = (
                            node.targets
                            if isinstance(node, ast.Assign)
                            else [node.target]
                        )
                        for x in tg:
                            if isinstance(x, ast.Name):
                                glob = f is not None and any(
                                    isinstance(g, ast.Global) and x.id in g.names
                                    for g in ast.walk(f.node)
                                )
                                if f is None or glob:
                                    alias[m][x.id] = cls
                                else:
                                    local_alias[f.key][x.id] = cls
                            elif (
                                isinstance(x, ast.Attribute)
                                and isinstance(x.value, ast.Name)
                                and x.value.id == "self"
                            ):
                                f2 = f
                                while f2 is not None and f2.cls is None:
                                    f2 = f2.parent
                                if f2 is not None:
                                    self_alias[(m, f2.cls)][x.attr] = cls
                if (
                    isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and id(node) in fn_of_node
                ):
                    f = fn_of_node[id(node)]
                    a = node.args
                    params = a.posonlyargs + a.args + a.kwonlyargs
                    defaults = (
                        [None] * (len(a.posonlyargs + a.args) - len(a.defaults))
                        + list(a.defaults)
                        + list(a.kw_defaults)
                    )
                    for prm, d in zip(params, defaults):
                        cls = ann_class(prm.annotation)
                        if (
                            cls is None
                            and isinstance(d, ast.Call)
                            and last(d.func) == "Depends"
                            and d.args
                            and isinstance(d.args[0], (ast.Name, ast.Attribute))
                        ):
                            gn = last(d.args[0])
                            cls = getters[m].get(gn) or next(
                                (
                                    getters[s0][s1]
                                    for s0, s1 in [imports[m].get(gn, ("", None))]
                                    if s1 and s1 in getters.get(s0, {})
                                ),
                                None,
                            )
                        if cls:
                            local_alias[f.key][prm.arg] = cls
                    for r in ast.walk(node):
                        if isinstance(r, ast.Return) and r.value is not None:
                            v = r.value
                            if isinstance(v, ast.Call) and getter_class(m, v):
                                getters[m][f.name] = getter_class(m, v)
                            elif isinstance(v, ast.Name):
                                c = local_alias[f.key].get(v.id) or alias[m].get(v.id)
                                if c:
                                    getters[m][f.name] = c
                    if (
                        node.returns is not None
                        and ann_class(node.returns)
                        and f.name.startswith("get")
                    ):
                        getters[m].setdefault(f.name, ann_class(node.returns))
                for ch in ast.iter_child_nodes(node):
                    scan(ch, st + [node])

            scan(t, [])

    def resolve_class(recv: ast.expr, f: Fn) -> str | None:
        m = f.module
        if isinstance(recv, ast.Call):
            return getter_class(m, recv)
        if isinstance(recv, ast.Name):
            if recv.id == "self":
                p = f
                while p is not None and p.cls is None:
                    p = p.parent
                return p.cls if p is not None else None
            p = f
            while p is not None:
                if recv.id in local_alias.get(p.key, {}):
                    return local_alias[p.key][recv.id]
                p = p.parent
            if recv.id in alias[m]:
                return alias[m][recv.id]
            src = imports[m].get(recv.id)
            if src and src[1] and src[1] in alias.get(src[0], {}):
                return alias[src[0]][src[1]]
            return None
        if isinstance(recv, ast.Attribute) and isinstance(recv.value, ast.Name):
            if recv.value.id == "self":
                p = f
                while p is not None and p.cls is None:
                    p = p.parent
                if p is not None:
                    return self_alias.get((m, p.cls), {}).get(recv.attr)
                return None
            modref = imports[m].get(recv.value.id)
            if modref and modref[1] is None and recv.attr in alias.get(modref[0], {}):
                return alias[modref[0]][recv.attr]
        return None

    def enclosing_fn(stack: list[Fn]) -> Fn | None:
        return stack[-1] if stack else None

    # ---- 3. الحوافُّ: (مُنادٍ لفظيّ) → (مُنادى) مع عُقدةِ النداء
    edges: dict[str, list[tuple[str, int, ast.Call]]] = defaultdict(
        list
    )  # callee_key -> [(caller_key, line, call)]
    write_calls: list[tuple[tuple[str, str], str, int, ast.Call]] = []
    module_level_calls: dict[str, list[tuple[str, int]]] = defaultdict(list)
    subscribed: set[str] = set()

    for m, t in mods.items():
        if m == PERSISTENT:
            continue
        stack: list[Fn] = []

        def visit(node: ast.AST, m: str = m) -> None:
            pushed = False
            if (
                isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                and id(node) in fn_of_node
            ):
                stack.append(fn_of_node[id(node)])
                pushed = True
            if isinstance(node, ast.Call):
                caller = enclosing_fn(stack)
                targets: list[Fn] = []
                func = node.func
                if caller is not None and isinstance(func, ast.Attribute):
                    cls = resolve_class(func.value, caller)
                    if cls and (cls, func.attr) in site_set:
                        write_calls.append(
                            ((cls, func.attr), caller.key, node.lineno, node)
                        )
                    elif (
                        cls and cls in class_methods and func.attr in class_methods[cls]
                    ):
                        targets += class_methods[cls][func.attr]
                    elif isinstance(func.value, ast.Name):
                        modref = imports[m].get(func.value.id)
                        if modref and modref[1] is None:
                            targets += by_module_name[modref[0]].get(func.attr, [])
                elif caller is not None and isinstance(func, ast.Name):
                    # اسمٌ مرئيٌّ: دالّةٌ متداخلةٌ في سلسلةِ الآباء · دالّةُ وحدةٍ · مستوردة
                    found = False
                    p = caller
                    while p is not None and not found:
                        for c in fns.values():
                            if c.parent is p and c.name == func.id:
                                targets.append(c)
                                found = True
                        p = p.parent
                    if not found:
                        p = caller
                        while p is not None and not found:
                            src = local_imports.get(p.key, {}).get(func.id)
                            if src and src[1]:
                                targets += [
                                    c
                                    for c in by_module_name[src[0]].get(src[1], [])
                                    if c.parent is None and c.cls is None
                                ]
                                found = True
                            p = p.parent
                    if not found:
                        top = [
                            c
                            for c in by_module_name[m].get(func.id, [])
                            if c.parent is None and c.cls is None
                        ]
                        if top:
                            targets += top
                        else:
                            src = imports[m].get(func.id)
                            if src and src[1]:
                                targets += [
                                    c
                                    for c in by_module_name[src[0]].get(src[1], [])
                                    if c.parent is None and c.cls is None
                                ]
                elif caller is None:
                    if isinstance(func, ast.Name):
                        module_level_calls[m].append((func.id, node.lineno))
                    if isinstance(func, ast.Attribute):
                        module_level_calls[m].append((func.attr, node.lineno))
                # اشتراكُ المعالِجات: subscribe(event, handler) أو add_listener / on
                if last(func) in {
                    "subscribe",
                    "add_listener",
                    "register_handler",
                    "on_event",
                    "add_event_handler",
                }:
                    for a in list(node.args) + [k.value for k in node.keywords]:
                        hn = last(a)
                        if hn:
                            for c in fns.values():
                                if c.name == hn and (
                                    c.module == m or (imports[m].get(hn))
                                ):
                                    subscribed.add(c.key)
                            if (
                                isinstance(a, ast.Attribute)
                                and isinstance(a.value, ast.Name)
                                and a.value.id == "self"
                            ):
                                for c in fns.values():
                                    if c.module == m and c.name == a.attr:
                                        subscribed.add(c.key)
                for tfn in targets:
                    if caller is not None:
                        edges[tfn.key].append((caller.key, node.lineno, node))
            for ch in ast.iter_child_nodes(node):
                visit(ch)
            if pushed:
                stack.pop()

        visit(t)

    # دالّةٌ متداخلةٌ مُمرَّرةٌ وسيطًا (مُطبِّقٌ · معوِّضٌ · callback) يُناديها الإطارُ لا أمُّها لفظيًّا:
    # فتُصَلُ بأمِّها حافّةً، وإلا ظهرَ كلُّ مُطبِّقٍ جذرًا غيرَ محلول.
    for f in list(fns.values()):
        if f.parent is None:
            continue
        for n in ast.walk(f.parent.node):
            if isinstance(n, ast.Call):
                vals = list(n.args) + [k.value for k in n.keywords]
                if any(
                    isinstance(sub, ast.Name) and sub.id == f.name
                    for v in vals
                    for sub in ast.walk(v)
                ):
                    edges[f.key].append((f.parent.key, n.lineno, n))
                    break

    # نداءاتُ الوحدةِ عندَ الاستيرادِ تُحوَّلُ مداخلَ
    module_entry: set[str] = set()
    for m, calls in module_level_calls.items():
        for name, _line in calls:
            for c in by_module_name[m].get(name, []):
                if c.parent is None:
                    module_entry.add(c.key)

    # ---- 4. هل النداءُ يقعُ تحتَ الحدّ؟
    def reaches_guard(f: Fn, seen: set[str] | None = None) -> bool:
        seen = seen or set()
        if f.key in seen:
            return False
        seen.add(f.key)
        if GUARD in f.src:
            return True
        for callee_key, lst in edges.items():
            for ck, _l, _n in lst:
                if (
                    ck == f.key
                    and fns[callee_key].module == f.module
                    and reaches_guard(fns[callee_key], seen)
                ):
                    return True
        return False

    def passed_as_arg(name: str, parent: Fn) -> list[ast.Call]:
        out = []
        for n in ast.walk(parent.node):
            if isinstance(n, ast.Call):
                vals = list(n.args) + [k.value for k in n.keywords]
                for v in vals:
                    for sub in ast.walk(v):
                        if isinstance(sub, ast.Name) and sub.id == name:
                            out.append(n)
        return out

    applier_cache: dict[str, bool] = {}

    def is_applier(f: Fn) -> bool:
        """دالّةٌ متداخلةٌ مُمرَّرةٌ وسيطًا في أمِّها إلى نداءٍ يصلُ إلى guard_declared."""
        if f.key in applier_cache:
            return applier_cache[f.key]
        res = False
        if f.parent is not None:
            for call in passed_as_arg(f.name, f.parent):
                txt = ast.unparse(call)
                if GUARD in txt + "(" or txt.split("(")[0].endswith("guard_declared"):
                    res = True
                    break
                callee = last(call.func)
                for c in by_module_name[f.module].get(callee or "", []):
                    if reaches_guard(c):
                        res = True
                if res:
                    break
        applier_cache[f.key] = res
        return res

    def under_guard(caller_key: str, call: ast.Call) -> bool:
        """النداءُ داخلَ مُطبِّقٍ: الدالّةُ المُنادِيةُ نفسُها أو أحدُ آبائِها اللفظيّين مُطبِّق،
        أو النداءُ داخلَ lambda مُمرَّرةٍ إلى guard_declared."""
        f = fns[caller_key]
        p: Fn | None = f
        while p is not None:
            if is_applier(p):
                return True
            p = p.parent
        # lambda: ابحثْ عن lambda تحوي النداءَ ومُمرَّرةٍ إلى نداءٍ نصُّه فيه guard_declared
        for n in ast.walk(f.node):
            if isinstance(n, ast.Call) and last(n.func) == "guard_declared":
                for v in list(n.args) + [k.value for k in n.keywords]:
                    for sub in ast.walk(v):
                        if sub is call:
                            return True
        return False

    def lineage(f: Fn) -> list[Fn]:
        out = []
        p: Fn | None = f
        while p is not None:
            out.append(p)
            p = p.parent
        return out

    def mentions(f: Fn) -> list[str]:
        """ملفّاتُ إنتاجٍ أخرى يرِدُ فيها اسمُ الجذرِ معرِّفًا أو نصًّا — قرينةُ نداءٍ ديناميكيٍّ تُفحَصُ يدويًّا."""
        import re as _re

        pat = _re.compile(rf"(?<![A-Za-z0-9_]){_re.escape(f.name)}(?![A-Za-z0-9_])")
        out = []
        for mm, tx in texts.items():
            if mm == f.module or mm == PERSISTENT:
                continue
            code = "\n".join(
                line for line in tx.splitlines() if not line.lstrip().startswith("#")
            )
            if pat.search(code):
                out.append(mm)
        return sorted(out)

    # ---- 5. تعدادُ المساراتِ صعودًا
    def entry_kind(f: Fn) -> str | None:
        if f.route:
            return "HTTP"
        if f.key in subscribed:
            return "EVENT"
        if f.key in module_entry:
            return "IMPORT"
        return None

    results = []
    for site in sites:
        calls = [w for w in write_calls if w[0] == site]
        paths = []
        truncated = False
        for _s, caller_key, line, call in calls:
            g0 = under_guard(caller_key, call)
            stackp: list[tuple[str, list[str], bool]] = [(caller_key, [caller_key], g0)]
            while stackp:
                cur, chain, guarded = stackp.pop()
                f = fns[cur]
                kind = entry_kind(f)
                ups = [
                    (ck, ln, n) for ck, ln, n in edges.get(cur, []) if ck not in chain
                ]
                lex = any(reaches_guard(a) for k in chain for a in lineage(fns[k]))
                if kind:
                    paths.append(
                        dict(
                            entry=f.key,
                            kind=kind,
                            route=f.route,
                            auth=f.auth,
                            chain=list(reversed(chain)),
                            write_line=line,
                            guarded=guarded,
                            guarded_lexical=lex,
                        )
                    )
                if not ups and not kind:
                    paths.append(
                        dict(
                            entry=f.key,
                            kind="UNRESOLVED_ROOT",
                            route=None,
                            auth=[],
                            chain=list(reversed(chain)),
                            write_line=line,
                            guarded=guarded,
                            guarded_lexical=lex,
                            mentions_elsewhere=mentions(f),
                        )
                    )
                for ck, _l, n in ups:
                    if len(paths) > MAX_PATHS:
                        truncated = True
                        break
                    stackp.append((ck, chain + [ck], guarded or under_guard(ck, n)))
        results.append(
            dict(
                site=f"{site[0]}.{site[1]}",
                direct_call_sites=[
                    dict(caller=c, line=ln, under_guard=under_guard(c, n))
                    for _s, c, ln, n in calls
                ],
                paths_total=len(paths),
                paths_guarded=sum(1 for p in paths if p["guarded"]),
                paths_unguarded=sum(1 for p in paths if not p["guarded"]),
                paths_guarded_lexical=sum(1 for p in paths if p["guarded_lexical"]),
                paths_unguarded_lexical=sum(
                    1 for p in paths if not p["guarded_lexical"]
                ),
                by_kind={
                    k: dict(
                        total=sum(1 for p in paths if p["kind"] == k),
                        unguarded=sum(
                            1 for p in paths if p["kind"] == k and not p["guarded"]
                        ),
                        unguarded_lexical=sum(
                            1
                            for p in paths
                            if p["kind"] == k and not p["guarded_lexical"]
                        ),
                    )
                    for k in sorted({p["kind"] for p in paths})
                },
                truncated=truncated,
                paths=sorted(
                    paths,
                    key=lambda p: (p["guarded"], p["kind"], p["entry"], p["chain"]),
                ),
            )
        )

    short = lambda k: k.replace("federal/executive/services/src/amos_federation/", "~/")  # noqa: E731
    print("== تحليلُ مساراتِ الاستدعاءِ العامةِ لمواقعِ persistent.py (WI-118) ==")
    print(f"  المواقعُ المقيسةُ (من الجردِ نفسِه): {len(sites)}")
    print(f"  ملفّاتُ الإنتاجِ المقروءة: {len(mods)}")
    print()
    hdr = (
        "الموقع",
        "نداءات",
        "مسارات",
        "HTTP",
        "حدث",
        "استيراد",
        "جذر",
        "✗ تنفيذيًّا",
        "✗ لفظيًّا",
    )
    print("  " + " | ".join(hdr))

    def kc(r: dict, k: str) -> int:
        return r["by_kind"].get(k, {}).get("total", 0)

    for r in results:
        print(
            f"  {r['site']} | {len(r['direct_call_sites'])} | {r['paths_total']} | {kc(r,'HTTP')} | {kc(r,'EVENT')} | {kc(r,'IMPORT')} | {kc(r,'UNRESOLVED_ROOT')} | {r['paths_unguarded']} | {r['paths_unguarded_lexical']}"
        )
    tot = sum(r["paths_total"] for r in results)
    print(
        f"  المجموع | {sum(len(r['direct_call_sites']) for r in results)} | {tot} | "
        + " | ".join(
            str(sum(kc(r, k) for r in results))
            for k in ("HTTP", "EVENT", "IMPORT", "UNRESOLVED_ROOT")
        )
        + f" | {sum(r['paths_unguarded'] for r in results)} | {sum(r['paths_unguarded_lexical'] for r in results)}"
    )
    print(
        "  (✗ تنفيذيًّا = الكتابةُ لا تُنفَّذُ داخلَ مُطبِّقٍ تحتَ guard_declared · ✗ لفظيًّا = لا دالّةَ في السلسلةِ يقعُ في جسدِها guard_declared)"
    )
    print()
    for r in results:
        print(
            f"--- {r['site']}  (مسارات {r['paths_total']} · غيرُ محروسة {r['paths_unguarded']}) {'· مقطوعٌ' if r['truncated'] else ''}"
        )
        for d in r["direct_call_sites"]:
            print(
                f"    نداءٌ مباشر: {short(d['caller'])}:{d['line']}  تحتَ الحدّ={d['under_guard']}"
            )
        for p in r["paths"]:
            mark = (
                ("✓ تنفيذيًّا" if p["guarded"] else "✗ تنفيذيًّا")
                + " · "
                + ("✓ لفظيًّا" if p["guarded_lexical"] else "✗ لفظيًّا")
            )
            extra = f" [{p['route']}]" if p["route"] else ""
            auth = f" auth={p['auth']}" if p["auth"] else ""
            ment = (
                f" · يرِدُ اسمُه في: {[short(x) for x in p['mentions_elsewhere']]}"
                if p.get("mentions_elsewhere")
                else ""
            )
            print(f"    {mark} · {p['kind']}{extra}{auth}{ment}")
            print(f"        {' → '.join(short(c) for c in p['chain'])}")
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(
                {
                    "$comment": "WI-118 · مساراتُ الاستدعاءِ العامّةِ لمواقعِ persistent.py تحتَ D-4 — قياسٌ لا حكم (D4_CALLERS_COVERAGE_ANALYSIS.md)",
                    "sites": results,
                },
                ensure_ascii=False,
                indent=1,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
    return 0


def module_name(rel: str) -> str | None:
    p = Path(rel)
    parts = list(p.with_suffix("").parts)
    if "src" in parts:
        parts = parts[parts.index("src") + 1 :]
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts) if parts else None


_MODNAME_CACHE: dict[str, str] = {}


def _rev(mods: dict[str, ast.Module]) -> dict[str, str]:
    if not _MODNAME_CACHE:
        for rel in mods:
            n = module_name(rel)
            if n:
                _MODNAME_CACHE[n] = rel
    return _MODNAME_CACHE


def _own_nodes(root: ast.AST) -> Iterator[ast.AST]:
    """عُقَدُ النطاقِ نفسِه: لا ينزلُ إلى دوالَّ أو أصنافٍ متداخلة."""
    stack = list(ast.iter_child_nodes(root))
    while stack:
        n = stack.pop()
        yield n
        if not isinstance(
            n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)
        ):
            stack.extend(ast.iter_child_nodes(n))


def import_map(
    m: str, t: ast.AST, mods: dict[str, ast.Module], own_only: bool = False
) -> dict[str, tuple[str, str | None]]:
    """اسمٌ محلّيٌّ → (وحدةُ المصدر، الاسمُ فيها أو None إن كانَ الاسمُ وحدةً).

    نطاقُ الوحدةِ يضمُّ استيراداتِ المستوى الأعلى واستيراداتِ الدوالِّ معًا (الاستيرادُ المتأخِّرُ
    شائعٌ هنا) ما لم يُعارضْها اسمٌ؛ ونطاقُ الدالّةِ (own_only) استيراداتُها هي فقط — ويُقدَّمُ عندَ
    الحلّ، فاستيرادٌ محلّيٌّ يحجبُ دالّةً بالاسمِ نفسِه في الوحدة.
    """
    rev = _rev(mods)
    out: dict[str, tuple[str, str | None]] = {}
    nodes = _own_nodes(t) if own_only else ast.walk(t)
    for n in nodes:
        if isinstance(n, ast.ImportFrom) and (n.module or n.level):
            base = n.module or ""
            if n.level:
                pkg = (module_name(m) or "").split(".")
                base = ".".join(
                    pkg[: len(pkg) - n.level] + ([n.module] if n.module else [])
                )
            for a in n.names:
                local = a.asname or a.name
                if f"{base}.{a.name}" in rev:
                    out.setdefault(local, (rev[f"{base}.{a.name}"], None))
                elif base in rev:
                    out.setdefault(local, (rev[base], a.name))
        elif isinstance(n, ast.Import):
            for a in n.names:
                if a.name in rev:
                    out.setdefault(a.asname or a.name, (rev[a.name], None))
    return out


def imported_modules(m: str, mods: dict[str, ast.Module], t: ast.Module) -> list[str]:
    return sorted({v[0] for v in import_map(m, t, mods).values()})


if __name__ == "__main__":
    raise SystemExit(main())
