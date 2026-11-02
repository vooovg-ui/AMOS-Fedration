"""مِسبارُ إسقاطِ D-4 لتصاميمِ WI-128 (A1 (ج-1)(أ) · (د-1) · (د-2)) قبلَ أوّلِ سطرِ شِفرة (W-799).

الهدف: قياسُ — لا تقديرُ — ما يصيرُ إليه D-4 لو طُبِّقَت القراراتُ الثلاثةُ كما يقترحُ
`docs/audit/A1_CD_DESIGN.md`، بالأداةِ نفسِها (`tools/audit/sovereign_write_inventory.py`
بلا تعديل: `collect` و`summarize`). لا يكتبُ في المستودعِ ولا يُشغِّلُ شِفرةَ إنتاج.

ويقيسُ معه:
- (د-2) شرطَ المالك «إثباتُ الغيابِ أمرًا»: كلُّ ذكرٍ للاسمِ في federal وcore وtools وtests
  (نداءٌ · `getattr` بنصٍّ · اسمٌ نصّيٌّ · tool_registry · استيرادٌ من الفحوص).
- (ج-1)(أ) «ما خارجَ _apply دَينٌ مسمّى»: نداءاتُ شهودِ الإلحاقِ في الإنتاج مصنَّفةً بموقعِها:
  داخلَ دالّةٍ متداخلةٍ في عمليّةٍ محروسة · في جسدِ عمليّةٍ محروسةٍ خارجَ المتداخلة · خارجَ أيِّ
  عمليّةٍ محروسة. التصنيفُ ساكنٌ بالنصِّ (`guard_declared(` في جسدِ الدالّةِ الخارجيّة)، حدٌّ مُعلَن.

يُشغَّلُ من جذرِ المستودع: `.venv/bin/python docs/audit/evidence/W-799/a1cd_projection_probe.py`
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from tools.audit.sovereign_write_inventory import collect, summarize  # noqa: E402

COMMON = "federal/executive/services/src/amos_federation/common/"

#: (الملف · المالك · الدالّة) ← (رقمُ ورقةِ المالك W-759 · الفئةُ المقترحة)
DECISIONS = {
    ("persistent.py", "PersistentAuditStore", "append"): ("8", "ج-1(أ) حدٌّ مُعلَن"),
    ("durable_event_bus.py", "DurableEventBus", "publish"): ("25", "ج-1(أ) حدٌّ مُعلَن"),
    ("event_bus.py", "EventBus", "publish"): ("27", "ج-1(أ) حدٌّ مُعلَن"),
    ("events.py", "EventPublisher", "publish"): ("28", "ج-1(أ) حدٌّ مُعلَن"),
    ("database.py", "-", "ensure_added_columns"): ("21", "د-1 حدٌّ مُعلَن"),
    ("persistent.py", "PersistentSystemStateStore", "get"): ("9", "د-1 حدٌّ مُعلَن"),
    ("database.py", "-", "db_cursor"): ("24", "د-1 حدٌّ مُعلَن"),
    ("database.py", "-", "with_db"): ("22", "د-2 حذف"),
    ("database.py", "-", "wrapper"): ("23", "د-2 حذف"),
    ("durable_event_bus.py", "DurableEventBus", "ack"): ("26", "د-2 حذف"),
    ("persistent.py", "PersistentTaskStore", "create"): ("3", "د-2 حذف"),
    ("persistent.py", "PersistentTaskStore", "update_status"): ("4", "د-2 حذف"),
}

#: أسماءٌ يُبحَثُ عنها لشرطِ (د-2) — النمطُ ووصفُه.
ABSENCE = {
    "with_db": r"\bwith_db\b",
    "DurableEventBus.ack": r"\.ack\(|\"ack\"|'ack'",
    "PersistentTaskStore": r"\bPersistentTaskStore\b",
}
SEARCH_DIRS = ("federal", "core", "tools", "tests")


def key_of(site) -> tuple[str, str, str]:  # noqa: ANN001
    return (site.path.removeprefix(COMMON), site.owner, site.function)


def project() -> None:
    sites = collect(ROOT)
    before = summarize(sites)
    print("== (1) الجردُ كما هو اليوم ==")
    for k in (
        "write_sites_total",
        "public_write_operations",
        "sovereign_write_operations",
        "closed_legacy_paths",
        "non_sovereign_write_operations",
    ):
        print(f"  {k}: {before[k]}")
    matched: dict[tuple[str, str, str], object] = {}
    for s in sites:
        if s.path.startswith(COMMON) and key_of(s) in DECISIONS:
            matched[key_of(s)] = s
    print("\n== (2) المواضعُ الاثنا عشرَ بقراراتِها ==")
    for k, (num, cat) in DECISIONS.items():
        s = matched.get(k)
        state = (
            f"public={s.public} guarded={s.guarded} closed={s.closed_legacy} line={s.line}"
            if s
            else "**غيرُ موجودٍ في الجرد**"
        )
        print(f"  {num:>2} · {k[0]}:{k[1]}.{k[2]} · {cat} · {state}")
    counted = [
        s
        for s in matched.values()
        if s.public and not s.guarded and not s.closed_legacy
    ]
    by_cat: dict[str, int] = {}
    for s in counted:
        cat = DECISIONS[key_of(s)][1]
        by_cat[cat] = by_cat.get(cat, 0) + 1
    d4 = before["non_sovereign_write_operations"]
    print("\n== (3) إسقاطُ D-4 (المواضعُ العامّةُ غيرُ المحروسةِ منها) ==")
    for cat, n in sorted(by_cat.items()):
        print(f"  {cat}: {n}")
    deletion_zero = sum(
        1
        for s in counted
        if DECISIONS[key_of(s)][1] == "د-2 حذف" and s.function in {"with_db", "wrapper"}
    )
    deletion_tested = by_cat.get("د-2 حذف", 0) - deletion_zero
    declared = sum(n for c, n in by_cat.items() if "حدٌّ مُعلَن" in c)
    print(f"  D-4 اليوم: {d4}")
    print(f"  بعدَ (ج-1)(أ) و(د-1) فئةً مطبوعةً منفصلة: {d4 - declared}")
    print(
        f"  وبعدَ حذفِ ما لا مستدعيَ له حتى في الفحوص ({deletion_zero}): {d4 - declared - deletion_zero}"
    )
    print(
        f"  وبعدَ حذفِ ما يُنادى من الفحوصِ وحدَها ({deletion_tested}) إن أذنَ المالك: {d4 - declared - deletion_zero - deletion_tested}"
    )


def absence() -> None:
    print("\n== (4) شرطُ (د-2): كلُّ ذكرٍ للاسمِ خارجَ تعريفِه ==")
    files = [
        p
        for d in SEARCH_DIRS
        for p in (ROOT / d).rglob("*.py")
        if ".venv" not in p.parts and "site-packages" not in p.parts
    ]
    for name, pat in ABSENCE.items():
        rx = re.compile(pat)
        hits: list[str] = []
        for p in files:
            try:
                text = p.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError) as exc:
                hits.append(
                    f"{p.relative_to(ROOT)}: تعذَّرت قراءتُه ({type(exc).__name__}) — يُعَدُّ ذكرًا حتى يُقرأ"
                )
                continue
            for i, line in enumerate(text.splitlines(), 1):
                if rx.search(line) and not re.search(r"^\s*(def|class) ", line):
                    hits.append(f"{p.relative_to(ROOT)}:{i}")
        dyn = [h for h in hits if "getattr" in h]
        print(f"  {name}: {len(hits)} ذكرًا")
        for h in hits:
            print(f"    {h}")
        if dyn:
            print(f"    منها getattr: {len(dyn)}")
    reg = [
        p
        for p in files
        if "tool_registry" in p.read_text(encoding="utf-8", errors="ignore")
        and any(
            n in p.read_text(encoding="utf-8", errors="ignore")
            for n in ("with_db", "PersistentTaskStore", ".ack(")
        )
    ]
    print(f"  ملفّاتٌ تذكرُ tool_registry وأحدَ الأسماءِ معًا: {len(reg)}")
    for p in reg:
        print(f"    {p.relative_to(ROOT)}")


WITNESS_CALLS = {"record_domain_trace", "publish", "append"}
WITNESS_RECEIVER = re.compile(r"(audit|bus|publisher|event)", re.I)


def witnesses() -> None:
    print("\n== (5) (ج-1)(أ): نداءاتُ شهودِ الإلحاقِ في الإنتاجِ بموقعِها ==")
    src = ROOT / "federal/executive/services/src/amos_federation"
    tally = {
        "داخلَ مطبِّقٍ متداخلٍ في عمليّةٍ محروسة": 0,
        "في جسدِ عمليّةٍ محروسةٍ خارجَ المتداخلة": 0,
        "خارجَ أيِّ عمليّةٍ محروسة": 0,
    }
    outside: list[str] = []
    for p in sorted(src.rglob("*.py")):
        if "tests" in p.parts:
            continue
        text = p.read_text(encoding="utf-8")
        tree = ast.parse(text)

        def visit(node, stack):  # noqa: ANN001, ANN202
            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    visit(child, [*stack, child])
                    continue
                if isinstance(child, ast.Call):
                    f = child.func
                    name = (
                        f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")
                    )
                    if name in WITNESS_CALLS:
                        recv = (
                            ast.unparse(f.value) if isinstance(f, ast.Attribute) else ""
                        )
                        if name == "record_domain_trace" or WITNESS_RECEIVER.search(
                            recv
                        ):
                            classify(p, child, stack)
                visit(child, stack)

        def classify(path, call, stack):  # noqa: ANN001, ANN202
            if not stack:
                cat = "خارجَ أيِّ عمليّةٍ محروسة"
            else:
                outer = stack[0]
                guarded = "guard_declared(" in (
                    ast.get_source_segment(text, outer) or ""
                )
                if guarded and len(stack) > 1:
                    cat = "داخلَ مطبِّقٍ متداخلٍ في عمليّةٍ محروسة"
                elif guarded:
                    cat = "في جسدِ عمليّةٍ محروسةٍ خارجَ المتداخلة"
                else:
                    cat = "خارجَ أيِّ عمليّةٍ محروسة"
            tally[cat] += 1
            if cat == "خارجَ أيِّ عمليّةٍ محروسة":
                outside.append(f"{path.relative_to(ROOT)}:{call.lineno}")

        visit(tree, [])
    for k, v in tally.items():
        print(f"  {k}: {v}")
    print(f"  الدَّينُ المسمّى (خارجَ أيِّ عمليّةٍ محروسة) — {len(outside)} نداءً:")
    for o in outside:
        print(f"    {o}")


if __name__ == "__main__":
    project()
    absence()
    witnesses()
