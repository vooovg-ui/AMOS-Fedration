"""مسحُ أثرِ الحصرِ الجديدِ على المنادين القائمين (W-819 · Q-98 · نهجُ Q-97 القيد (د)).

الهدف: قبلَ أن تصيرَ الأفعالُ التسعةُ حصرًا للفرعِ التنفيذيِّ في
`core/constitutional_engine/rules.py`، يُقاسُ: هل في الشِّفرةِ منادٍ يُمرِّرُ أحدَ
هذه الأسماءِ إلى المحرّكِ (أو إلى `guard`/`guard_declared`/`review_only`/
`request_permit`/`ActionRequest`) اليومَ باسمٍ مجهولٍ فيمرّ، وسيُحجَبُ غدًا؟

الطريقة: قراءةٌ ساكنةٌ (AST) لكلِّ ملفِّ `.py` في المستودع خارجَ `.venv` و`.git`
وخارجَ أدلّةِ هذا القيد: كلُّ ثابتٍ نصّيٍّ يساوي أحدَ الأفعالِ التسعةِ حرفيًّا يُطبَعُ
بموضعِه وبالنداءِ الذي يحتويه إن كان. ولا يُعدِّلُ شيئًا.

الحكم: `ENGINE_CALLERS=<n>` = عددُ المواضعِ التي يقعُ فيها الاسمُ وسيطًا أوّلَ
أو `action=` لنداءٍ من نداءاتِ الحدِّ أعلاه. الصفرُ يعني: لا منادٍ قائمٌ يُحجَب.
والأمرُ يخرجُ بـ0 دائمًا — الحكمُ في الرقمِ المطبوعِ لا في رمزِ الخروج.

الاستعمال:
    python docs/audit/evidence/W-819/caller_impact_scan.py --root .
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path

VERBS = (
    "register_sector",
    "register_category",
    "define_indicator",
    "register_public_entity",
    "create_program",
    "issue_policy",
    "register_revenue_source",
    "register_public_asset",
    "register_public_liability",
)
ENGINE_CALLS = {
    "guard",
    "guard_declared",
    "review_only",
    "request_permit",
    "ActionRequest",
    "evaluate",
    "authorize",
}
SKIP_PARTS = {".venv", ".git", "node_modules", "__pycache__", ".runtime"}
SELF_DIR = "docs/audit/evidence/W-819"


def _call_name(node: ast.Call) -> str:
    func = node.func
    if isinstance(func, ast.Attribute):
        return func.attr
    if isinstance(func, ast.Name):
        return func.id
    return ""


def scan(root: Path) -> tuple[list[str], int]:
    lines: list[str] = []
    engine_callers = 0
    for path in sorted(root.rglob("*.py")):
        rel = path.relative_to(root).as_posix()
        if SKIP_PARTS & set(path.parts) or rel.startswith(SELF_DIR):
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError) as exc:
            # لا يُبتلَعُ صامتًا: يُسجَّلُ الملفُّ المتروكُ في الخرجِ نفسِه
            lines.append(f"UNPARSED {rel}: {type(exc).__name__}")
            continue
        engine_args: set[int] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and _call_name(node) in ENGINE_CALLS:
                candidates = list(node.args[:1]) + [
                    k.value for k in node.keywords if k.arg == "action"
                ]
                for arg in candidates:
                    if isinstance(arg, ast.Constant) and arg.value in VERBS:
                        engine_args.add(id(arg))
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and node.value in VERBS:
                kind = "ENGINE_CALLER" if id(node) in engine_args else "literal"
                if kind == "ENGINE_CALLER":
                    engine_callers += 1
                lines.append(f"{kind:13} {rel}:{node.lineno} {node.value!r}")
    return lines, engine_callers


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    lines, engine_callers = scan(Path(args.root).resolve())
    for line in lines:
        print(line)
    print(f"LITERALS={len(lines)}")
    print(f"ENGINE_CALLERS={engine_callers}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
