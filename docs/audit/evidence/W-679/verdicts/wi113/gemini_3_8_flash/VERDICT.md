# حكمُ مقعدِ المجلسِ — gemini_3_8_flash · جولةُ WI-113 (W-679)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-113 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w673/gemini_3_8_flash/wi113) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `4c9b084551d01977db7ba445a249a98ef7bcc8c021932a7bcae19813ef453f75`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-113 عندَ العقدةِ `79abc6a2` — إحاطةٌ مبصومةٌ (W-673) ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9) · والفحصُ النهائيُّ للنصابِ معلَّقٌ على شرائطِ § 4.7 (قياسُ عيبَي الفاحصِ في W-679).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-679) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-25

## تاريخ آخر تعديل
2026-10-25

---
MODEL: gemini_3_8_flash
FAMILY: Google · Gemini
RUN_DATE: 2026-10-25 23:45 +00:00
NODE: 79abc6a206000e162689d642d1ebc42af36f445a
CLONE_PATH: /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/
 2. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/)
 3. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git log --format='%h %cI %s' -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
 5. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git show --stat 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7
 6. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git diff 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7 -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
 7. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
 8. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && .venv/bin/python tools/audit/decision_gate.py --measure
 9. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 10. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && rm -rf ../old && git worktree add --detach ../old 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ && cp tests/governance/test_wi113_inventory_qualified_index.py ../old/tests/governance/ && cd ../old && /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
 11. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo/../old && /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo/.venv/bin/python tools/audit/decision_gate.py --measure
 12. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && nl -ba federal/executive/services/src/amos_federation/common/persistent.py | sed -n '880,960p'
 13. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && rg -n 'WI-113|A1\(هـ\)|تصحيح قياس' docs/audit/SOVEREIGN_DECISION_REGISTER.md
 14. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && sha256sum docs/audit/evidence/W-673/briefs_wi113/briefing_gemini_3_8_flash.md
 15. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && cat docs/audit/evidence/W-673/briefs_wi113/SHA256SUMS
 16. nl -ba /home/user/workspace/council_w673/gemini_3_8_flash/wi113/probe/probe_wi113.py
 17. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && .venv/bin/python /home/user/workspace/council_w673/gemini_3_8_flash/wi113/probe/probe_wi113.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/)
EXIT: 0
BYTES: 329
SHA256: 820b1154c5055620984fd0bba0e902931b07c236382c0e2d712be5b3ef5bcc27
NO_EOL: 0
--- OUTPUT ---
HEAD is now at 79abc6a2 W-673: WI-113 وWI-115 IN_PROGRESS→IN_REVIEW · ستُّ إحاطاتٍ مبصومةٍ لجولةِ المجلسِ (gemini_3_8_flash · grok_4_7 · kimi_k3) ونصوصُ الإطلاقِ حرفيًّا · WI-115 بنطاقِ § 3.5 وحدَه · لا شِفرةَ — المنسِّقُ Claude Opus 5.5
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git log --format='%h %cI %s' -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 0
BYTES: 1370
SHA256: 6fe169c22f08029da04086f91e91dc89a6a5cbc978b194d1bea1d27c1ab74886
NO_EOL: 0
--- OUTPUT ---
6605fa88 2026-10-25T08:40:22Z W-669: WI-113 — أداةُ الجردِ تفهرسُ بالاسمِ المؤهَّلِ · تصحيحُ قياسٍ لا حرقٌ: D-4 142→135 (W3 97→90) · فحصٌ (4) وطفرتانِ · اللقطاتُ المحروسةُ مُعادةٌ — المنسِّقُ Claude Opus 5.5
d206e3d7 2026-09-01T09:27:53+03:00 W-084 · مفتاحُ الموقعِ في القياسِ المنشورِ صارَ مُقاسًا لا إحداثيًّا في المصدرِ
68a087c9 2026-08-22T09:55:00Z W-027 · T3.5: الارتداداتُ الصامتةُ 26 ← 0 — وأربعةٌ منها كانت في أدواتِ القياسِ نفسِها
2f90aedb 2026-08-22T09:55:00Z W-022 · إصلاحُ فخِّ قياسٍ في جردِ الكتابةِ السياديّة (T0)
34ee562f 2026-08-19T01:17:11Z fix(P17-ب): إقفالُ دَينِ المادةِ التاسعةِ الـ22 وإعادةُ identity-check إلى الأخضر
a00f12eb 2026-08-18T17:00:30+03:00 sovereignty(stage-2b): هجرةُ تقليدِ المسؤولِ وعزلِه + تصحيحُ المقياسِ v3
e814cd2c 2026-08-18T16:25:57+03:00 sovereignty(stage-2b): هجرةُ set_institution_status عبرَ الحدِّ السياديّ + إصلاحُ عيبٍ في أداةِ القياس
7823bf12 2026-08-18T16:01:46+03:00 sovereignty(program): baseline and program control
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git show --stat 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7
EXIT: 0
BYTES: 1172
SHA256: 5ef1579c5fe0e23087f6141442922c9b853384e7650fc033294fb6035fac78b3
NO_EOL: 0
--- OUTPUT ---
commit 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7
Author: vooovg-ui <326082239+vooovg-ui@users.noreply.github.com>
Date:   Sun Oct 25 08:40:22 2026 +0000

    W-669: WI-113 — أداةُ الجردِ تفهرسُ بالاسمِ المؤهَّلِ · تصحيحُ قياسٍ لا حرقٌ: D-4 142→135 (W3 97→90) · فحصٌ (4) وطفرتانِ · اللقطاتُ المحروسةُ مُعادةٌ — المنسِّقُ Claude Opus 5.5

 docs/audit/COMPLETION_LEDGER.md                    |   3 +
 docs/audit/evidence/W-669/README.md                |  27 +++++
 docs/audit/evidence/W-669/d4_after.txt             |  69 +++++++++++
 docs/audit/evidence/W-669/mutations.txt            |  33 ++++++
 docs/audit/measurements/decision_gate_ledger.json  |  16 +++
 docs/audit/measurements/decision_wave_map.json     |   6 +-
 docs/audit/measurements/final_audit_p14.json       |  10 +-
 docs/audit/measurements/write_inventory_p13.json   | 117 +++----------------
 .../test_wi113_inventory_qualified_index.py        | 127 +++++++++++++++++++++
 tools/audit/sovereign_write_inventory.py           |  92 +++++++++++----
 10 files changed, 368 insertions(+), 132 deletions(-)
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && git diff 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7 -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 0
BYTES: 14077
SHA256: 975f342a0d380d4ccae40ac2118347097ddd8acd7759fbc3c2dcb754ded5584d
NO_EOL: 0
--- OUTPUT ---
diff --git a/tests/governance/test_wi113_inventory_qualified_index.py b/tests/governance/test_wi113_inventory_qualified_index.py
new file mode 100644
index 00000000..eb16a17c
--- /dev/null
+++ b/tests/governance/test_wi113_inventory_qualified_index.py
@@ -0,0 +1,127 @@
+"""الهدف: إثباتُ أنَّ جردَ الكتاباتِ يتتبّعُ المعاونينَ بالاسمِ المؤهَّلِ لا بالاسمِ المجرَّد.
+
+النطاق: `tools/audit/sovereign_write_inventory.py` — `synthesize_public_sites` و`resolve_callees`.
+المالك: governance/
+تاريخ الإنشاء: 2026-10-25
+تاريخ آخر تعديل: 2026-10-25
+
+## ما يحرسُه هذا الملفّ (WI-113 · تصحيحُ قياسٍ A1(هـ) · التوجيهُ 22)
+
+قاسَ تحليلُ A1 (§ 1.3) أنَّ الجردَ يحتسبُ 7 قراءاتٍ في `common/persistent.py` مواقعَ
+كتابة: الفهرسُ بالاسمِ المجرَّدِ يدمجُ كلَّ `get` في الوحدةِ في مدخلٍ واحد، فيصلُ كلٌّ
+منها إلى `_row` الكاتبِ في `PersistentSystemStateStore` (بذرٌ كسولٌ حقيقيّ)، ويُنسَبُ
+المالكُ إلى آخرِ صنفٍ يُعرِّفُ `get`. فكانَ الجردُ يُركِّبُ 8 مواقعَ كلُّها بهويّةِ
+`PersistentPromotionStore.get`، والحقُّ موقعٌ واحدٌ بهويّةِ `PersistentSystemStateStore.get`.
+
+والحرسُ يقيسُ الشِقَّين: لا يُحسَبُ ما لا يكتب (الإصلاح)، ولا يُسقَطُ ما يكتب (لا إسكات).
+"""
+
+from __future__ import annotations
+
+import ast
+import importlib.util
+import sys
+from pathlib import Path
+from types import ModuleType
+
+
+def _repo_root() -> Path:
+    """الجذرُ بعلامةٍ لا بعُمقٍ ثابت (DISC-041): صعودٌ حتّى `THE_ROADMAP.md`."""
+    here = Path(__file__).resolve()
+    for candidate in here.parents:
+        if (candidate / "docs" / "governance" / "work" / "THE_ROADMAP.md").is_file():
+            return candidate
+    raise AssertionError(f"لا جذرَ فوقَ {here} يحملُ THE_ROADMAP.md")
+
+
+REPO_ROOT = _repo_root()
+TOOL_PATH = REPO_ROOT / "tools" / "audit" / "sovereign_write_inventory.py"
+PERSISTENT = Path("federal/executive/services/src/amos_federation/common/persistent.py")
+
+#: صنفانِ يُعرِّفانِ `get` و`_row`: الأوّلُ يكتبُ في معاونِه، والثاني يقرأُ فقط.
+TWO_STORES = '''"""وحدةٌ للاختبار."""
+
+
+class SeedingStore:
+    def _row(self, session):
+        session.add(object())
+        session.commit()
+
+    def get(self, session):
+        return self._row(session)
+
+
+class ReadingStore:
+    def _row(self, session):
+        return session.query(object).first()
+
+    def get(self, session):
+        return self._row(session)
+'''
+
+
+def _load_tool() -> ModuleType:
+    """حمِّلِ الأداةَ من مسارِها — بلا اعتمادٍ على `sys.path`."""
+    name = "amos_write_inventory_qualified_under_test"
+    spec = importlib.util.spec_from_file_location(name, TOOL_PATH)
+    assert spec is not None and spec.loader is not None, f"لا يُحمَّلُ: {TOOL_PATH}"
+    module = importlib.util.module_from_spec(spec)
+    sys.modules[name] = module
+    try:
+        spec.loader.exec_module(module)
+    except BaseException:
+        sys.modules.pop(name, None)
+        raise
+    return module
+
+
+def _synthesized(tool: ModuleType, source: str, path: str = "svc/stores.py") -> list:
+    tree = ast.parse(source)
+    visitor = tool._WriteVisitor(path, source)
+    visitor.visit(tree)
+    return tool.synthesize_public_sites(
+        visitor.sites, visitor.qcalls, visitor.qnodes, path, source
+    )
+
+
+def test_reader_sharing_a_name_with_a_writer_is_not_a_write_site() -> None:
+    """`ReadingStore.get` لا يُحسَبُ كتابةً لأنَّ `SeedingStore._row` يكتب."""
+    tool = _load_tool()
+    added = _synthesized(tool, TWO_STORES)
+    identities = [(site.owner, site.function, site.writes_via) for site in added]
+    assert identities == [("SeedingStore", "get", ("_row",))], identities
+
+
+def test_real_writer_through_helper_is_still_counted() -> None:
+    """لا إسكات: العمليّةُ العامّةُ التي تكتبُ بمعاونِها تبقى موضعًا بمالكِها الحقّ."""
+    tool = _load_tool()
+    added = _synthesized(tool, TWO_STORES)
+    assert any(site.owner == "SeedingStore" and site.public for site in added)
+
+
+def test_unknown_receiver_keeps_the_declared_conservative_limit() -> None:
+    """نداءٌ على مُستقبِلٍ غيرِ `self` يبقى بالاسمِ: الحدُّ القديمُ لا يُخفَّفُ حيثُ لا يُعرَفُ النوع."""
+    tool = _load_tool()
+    source = (
+        TWO_STORES
+        + """
+
+def flush(store, session):
+    return store._row(session)
+"""
+    )
+    added = _synthesized(tool, source)
+    assert ("-", "flush") in {(site.owner, site.function) for site in added}
+
+
+def test_persistent_py_has_one_synthesized_get_owned_by_system_state() -> None:
+    """الشجرةُ الحاضرة: 8 مواقعَ كاذبةُ الهويّةِ صارت موقعًا واحدًا بهويّتِه الحقّ."""
+    tool = _load_tool()
+    source = (REPO_ROOT / PERSISTENT).read_text(encoding="utf-8")
+    added = _synthesized(tool, source, str(PERSISTENT))
+    gets = [
+        (site.owner, site.function, site.writes_via)
+        for site in added
+        if site.function == "get"
+    ]
+    assert gets == [("PersistentSystemStateStore", "get", ("_row",))], gets
diff --git a/tools/audit/sovereign_write_inventory.py b/tools/audit/sovereign_write_inventory.py
index 4cbde9df..959dc52e 100644
--- a/tools/audit/sovereign_write_inventory.py
+++ b/tools/audit/sovereign_write_inventory.py
@@ -163,6 +163,14 @@ class _WriteVisitor(ast.NodeVisitor):
         self.sites: list[WriteSite] = []
         #: خريطةُ الاستدعاءِ داخلَ الوحدة: دالّةٌ ← أسماءُ ما تُناديه.
         self.calls: dict[str, set[str]] = {}
+        #: الخريطةُ نفسُها **بالاسمِ المؤهَّلِ** (`Class.method` أو اسمُ دالّةِ الوحدة)
+        #: ومعها نوعُ كلِّ نداءٍ — `self` (على `self`/`cls`) · `name` (اسمٌ مجرَّد) ·
+        #: `attr` (صفةٌ على مُستقبِلٍ آخر). سببُها مقيسٌ (WI-113 · A1 § 1.3): الفهرسةُ
+        #: بالاسمِ المجرَّدِ تدمجُ كلَّ `get` في الوحدةِ في مدخلٍ واحدٍ، فتُنسَبُ كتابةُ
+        #: معاونِ صنفٍ إلى قراءاتِ أصنافٍ أخرى (7 قراءاتٍ في `common/persistent.py`).
+        self.qcalls: dict[str, set[tuple[str, str]]] = {}
+        #: العُقَدُ بالاسمِ المؤهَّلِ وصنفِها — لتركيبِ المواقعِ العامّةِ بمالكِها الحقّ.
+        self.qnodes: list[tuple[str, str, ast.FunctionDef | ast.AsyncFunctionDef]] = []
 
     def visit_ClassDef(self, node: ast.ClassDef) -> None:  # noqa: N802
         self._classes.append(node.name)
@@ -173,13 +181,23 @@ class _WriteVisitor(ast.NodeVisitor):
         segment = ast.get_source_segment(self._source, node) or ""
         writes: set[str] = set()
         called: set[str] = self.calls.setdefault(node.name, set())
+        owner = self._classes[-1] if self._classes else "-"
+        qualified = qualify(owner, node.name)
+        qcalled = self.qcalls.setdefault(qualified, set())
+        self.qnodes.append((qualified, owner, node))
         for sub in ast.walk(node):
             if isinstance(sub, ast.Call):
                 target = sub.func
                 if isinstance(target, ast.Name):
                     called.add(target.id)
+                    qcalled.add(("name", target.id))
                 elif isinstance(target, ast.Attribute):
                     called.add(target.attr)
+                    on_self = isinstance(target.value, ast.Name) and target.value.id in {
+                        "self",
+                        "cls",
+                    }
+                    qcalled.add(("self" if on_self else "attr", target.attr))
             if (
                 isinstance(sub, ast.Call)
                 and isinstance(sub.func, ast.Attribute)
@@ -268,6 +286,42 @@ def iter_source_files(base: Path) -> Iterator[Path]:
     return iter(sorted(collected))
 
 
+def qualify(owner: str, function: str) -> str:
+    """الاسمُ المؤهَّلُ لدالّة: `Class.method` في صنف، واسمُها وحدَه في الوحدة."""
+    return f"{owner}.{function}" if owner and owner != "-" else function
+
+
+def _bare(qualified: str) -> str:
+    """الاسمُ المجرَّدُ من الاسمِ المؤهَّل."""
+    return qualified.rsplit(".", 1)[-1]
+
+
+def resolve_callees(
+    caller: str, qcalls: dict[str, set[tuple[str, str]]]
+) -> set[str]:
+    """حُلَّ نداءاتِ `caller` إلى أسماءٍ مؤهَّلةٍ معرَّفةٍ في الوحدة.
+
+    - `self.x()`/`cls.x()` ← `Owner.x` إن عُرِّفَ في الصنفِ نفسِه؛ وإلّا (موروثٌ أو
+      غيرُ معروف) فكلُّ تعريفٍ بالاسم — تحفُّظٌ مُعلَنٌ: الإسقاطُ أخطرُ من الزيادة.
+    - `x()` ← دالّةُ الوحدةِ `x` إن وُجدَت؛ وإلّا فكلُّ تعريفٍ بالاسم (دالّةٌ متداخلة).
+    - `obj.x()` على مُستقبِلٍ آخر ← كلُّ تعريفٍ بالاسم: أداةٌ ساكنةٌ لا تعرفُ النوع،
+      وهذا هو الحدُّ القديمُ نفسُه باقيًا حيثُ لا يُعرَفُ المُستقبِلُ — لا يُخفَّف.
+    """
+    by_bare: dict[str, set[str]] = {}
+    for name in qcalls:
+        by_bare.setdefault(_bare(name), set()).add(name)
+    owner = caller.rsplit(".", 1)[0] if "." in caller else ""
+    resolved: set[str] = set()
+    for kind, name in qcalls.get(caller, ()):
+        if kind == "self" and owner and f"{owner}.{name}" in qcalls:
+            resolved.add(f"{owner}.{name}")
+        elif kind == "name" and name in qcalls:
+            resolved.add(name)
+        else:
+            resolved.update(by_bare.get(name, ()))
+    return resolved
+
+
 def attribute_helper_writes(
     sites: list[WriteSite], calls: dict[str, set[str]]
 ) -> list[WriteSite]:
@@ -317,48 +371,46 @@ def attribute_helper_writes(
 
 def synthesize_public_sites(
     sites: list[WriteSite],
-    calls: dict[str, set[str]],
+    qcalls: dict[str, set[tuple[str, str]]],
+    qnodes: list[tuple[str, str, ast.FunctionDef | ast.AsyncFunctionDef]],
     path: str,
     source: str,
-    tree: ast.AST,
 ) -> list[WriteSite]:
     """أضِفْ عمليّاتٍ عامّةً تكتبُ **بمعاونِها** ولا كتابةَ في جسدِها.
 
     هذه بعينُها الحالةُ التي كان المقياسُ يُسقِطها: `set_institution_status` بعدَ
     هجرتِها في P1أ.
+
+    **والتتبُّعُ بالاسمِ المؤهَّلِ** (WI-113 · تصحيحُ قياسٍ A1(هـ)): كانَ الفهرسُ
+    بالاسمِ المجرَّدِ فتصلُ `PromotionStore.get` إلى `_row` الكاتبِ في صنفٍ آخر،
+    ويُنسَبُ المالكُ إلى آخرِ صنفٍ يُعرِّفُ الاسم — فتُحسَبُ 7 قراءاتٍ كتاباتٍ.
     """
-    writer_helpers = {s.function for s in sites if s.writes and not s.public}
-    known = {s.function for s in sites}
+    writer_helpers = {
+        qualify(s.owner, s.function) for s in sites if s.writes and not s.public
+    }
+    known = {qualify(s.owner, s.function) for s in sites}
     added: list[WriteSite] = []
-    classes: dict[str, str] = {}
-    for node in ast.walk(tree):
-        if isinstance(node, ast.ClassDef):
-            for child in node.body:
-                if isinstance(child, ast.FunctionDef | ast.AsyncFunctionDef):
-                    classes[child.name] = node.name
-    for node in ast.walk(tree):
-        if not isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
-            continue
-        if node.name.startswith("_") or node.name in known:
+    for qualified, owner, node in qnodes:
+        if node.name.startswith("_") or qualified in known:
             continue
         seen: set[str] = set()
-        stack = list(calls.get(node.name, ()))
+        stack = list(resolve_callees(qualified, qcalls))
         via: set[str] = set()
         while stack:
             name = stack.pop()
-            if name in seen or not name.startswith("_"):
+            if name in seen or not _bare(name).startswith("_"):
                 continue
             seen.add(name)
             if name in writer_helpers:
-                via.add(name)
-            stack.extend(calls.get(name, ()))
+                via.add(_bare(name))
+            stack.extend(resolve_callees(name, qcalls))
         if not via:
             continue
         segment = ast.get_source_segment(source, node) or ""
         added.append(
             WriteSite(
                 path=path,
-                owner=classes.get(node.name, "-"),
+                owner=owner,
                 function=node.name,
                 line=node.lineno,
                 public=True,
@@ -391,7 +443,7 @@ def collect(root: Path, subtree: Path | None = None) -> list[WriteSite]:
         visitor = _WriteVisitor(str(relative), source)
         visitor.visit(tree)
         module_sites = visitor.sites + synthesize_public_sites(
-            visitor.sites, visitor.calls, str(relative), source, tree
+            visitor.sites, visitor.qcalls, visitor.qnodes, str(relative), source
         )
         sites.extend(attribute_helper_writes(module_sites, visitor.calls))
     return sites
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 0
BYTES: 98
SHA256: f87e1ec159e73ceaff96b34a3bc29b017111816d05b56b64e23a829128ce891b
NO_EOL: 0
--- OUTPUT ---
....                                                                     [100%]
4 passed in 0.08s
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && .venv/bin/python tools/audit/decision_gate.py --measure
EXIT: 0
BYTES: 159
SHA256: fe6b3b0ee73ecec5a923b2ca1a2a5c7f5c74255968dfb82393822f9bb55ef0cb
NO_EOL: 0
--- OUTPUT ---
{
 "debt": 135,
 "sovereign": 46,
 "closed_legacy": 7,
 "write_sites_total": 232,
 "git_head": "79abc6a2",
 "waves": {
  "W1": 11,
  "W2": 34,
  "W3": 90
 }
}
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3221
SHA256: 2ec33e328181e6319782870ba1cc38a684084d34abebadae98330823a800d2bb
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 232
  عمليّاتٌ عامّةٌ مُغيِّرة   : 183
  منها تعبرُ الحدَّ        : 46
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 135
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     21 /   0 /   21
    services          160 /  46 /  113
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
      13  federal/executive/services/src/amos_federation/common/persistent.py
      10  federal/executive/services/src/amos_federation/services/federal_state/service.py
       9  federal/executive/services/src/amos_federation/services/governance/treasury.py
       9  federal/executive/services/src/amos_federation/services/royal/main.py
       8  federal/executive/services/src/amos_federation/services/governance/expansion.py
       7  federal/executive/services/src/amos_federation/services/governance/learning_cycle.py
       7  federal/executive/services/src/amos_federation/services/governance/system_life.py
       7  federal/executive/services/src/amos_federation/services/state_treasury/service.py
       6  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
       5  federal/executive/services/src/amos_federation/services/agent_runtime/health.py
       5  federal/executive/services/src/amos_federation/services/governance/security.py
       5  federal/executive/services/src/amos_federation/services/governance/state_runtime.py
       4  federal/executive/services/src/amos_federation/common/database.py
       3  federal/executive/services/src/amos_federation/services/agent_runtime/population.py
       3  federal/executive/services/src/amos_federation/services/executive_core/repository.py
       2  federal/executive/services/src/amos_federation/common/durable_event_bus.py
       2  federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
       2  federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py
       2  federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py
       2  federal/executive/services/src/amos_federation/services/training/persistent_registry.py
       1  federal/executive/services/src/amos_federation/common/event_bus.py
       1  federal/executive/services/src/amos_federation/common/events.py
       1  federal/executive/services/src/amos_federation/services/api_gateway/store.py
       1  federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py
       1  federal/executive/services/src/amos_federation/services/government_services/service.py
       1  tools/migrations/r4_unify_agent_identity.py
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && rm -rf ../old && git worktree add --detach ../old 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ && cp tests/governance/test_wi113_inventory_qualified_index.py ../old/tests/governance/ && cd ../old && /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 1
BYTES: 7706
SHA256: c304c20d5af21965c5f0b858d249416008ebc9db1af07139651d9e065c6cec3e
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD 6aacee81)
HEAD is now at 6aacee81 W-668: WI-113 وWI-115 RESERVED→IN_PROGRESS · حكمُ N+1 لدفعةِ W-664…W-667 — PR #150 على 7d3d5b6f مقروءٌ أخضرَ (13/13 · 1/1 · EXIT 0) قبلَ الدفعِ السريعِ · لا شِفرةَ — المنسِّقُ Claude Opus 5.5
FFFF                                                                     [100%]
=================================== FAILURES ===================================
_________ test_reader_sharing_a_name_with_a_writer_is_not_a_write_site _________

    def test_reader_sharing_a_name_with_a_writer_is_not_a_write_site() -> None:
        """`ReadingStore.get` لا يُحسَبُ كتابةً لأنَّ `SeedingStore._row` يكتب."""
        tool = _load_tool()
>       added = _synthesized(tool, TWO_STORES)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/governance/test_wi113_inventory_qualified_index.py:90: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/gemini_3_8_flash/wi113/old/tools/audit/sovereign_write_inventory.py'>
source = '"""وحدةٌ للاختبار."""\n\n\nclass SeedingStore:\n    def _row(self, session):\n        session.add(object())\n        ...on):\n        return session.query(object).first()\n\n    def get(self, session):\n        return self._row(session)\n'
path = 'svc/stores.py'

    def _synthesized(tool: ModuleType, source: str, path: str = "svc/stores.py") -> list:
        tree = ast.parse(source)
        visitor = tool._WriteVisitor(path, source)
        visitor.visit(tree)
        return tool.synthesize_public_sites(
>           visitor.sites, visitor.qcalls, visitor.qnodes, path, source
                           ^^^^^^^^^^^^^^
        )
E       AttributeError: '_WriteVisitor' object has no attribute 'qcalls'. Did you mean: 'calls'?

tests/governance/test_wi113_inventory_qualified_index.py:83: AttributeError
_______________ test_real_writer_through_helper_is_still_counted _______________

    def test_real_writer_through_helper_is_still_counted() -> None:
        """لا إسكات: العمليّةُ العامّةُ التي تكتبُ بمعاونِها تبقى موضعًا بمالكِها الحقّ."""
        tool = _load_tool()
>       added = _synthesized(tool, TWO_STORES)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/governance/test_wi113_inventory_qualified_index.py:98: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/gemini_3_8_flash/wi113/old/tools/audit/sovereign_write_inventory.py'>
source = '"""وحدةٌ للاختبار."""\n\n\nclass SeedingStore:\n    def _row(self, session):\n        session.add(object())\n        ...on):\n        return session.query(object).first()\n\n    def get(self, session):\n        return self._row(session)\n'
path = 'svc/stores.py'

    def _synthesized(tool: ModuleType, source: str, path: str = "svc/stores.py") -> list:
        tree = ast.parse(source)
        visitor = tool._WriteVisitor(path, source)
        visitor.visit(tree)
        return tool.synthesize_public_sites(
>           visitor.sites, visitor.qcalls, visitor.qnodes, path, source
                           ^^^^^^^^^^^^^^
        )
E       AttributeError: '_WriteVisitor' object has no attribute 'qcalls'. Did you mean: 'calls'?

tests/governance/test_wi113_inventory_qualified_index.py:83: AttributeError
_________ test_unknown_receiver_keeps_the_declared_conservative_limit __________

    def test_unknown_receiver_keeps_the_declared_conservative_limit() -> None:
        """نداءٌ على مُستقبِلٍ غيرِ `self` يبقى بالاسمِ: الحدُّ القديمُ لا يُخفَّفُ حيثُ لا يُعرَفُ النوع."""
        tool = _load_tool()
        source = (
            TWO_STORES
            + """
    
    def flush(store, session):
        return store._row(session)
    """
        )
>       added = _synthesized(tool, source)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/governance/test_wi113_inventory_qualified_index.py:113: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/gemini_3_8_flash/wi113/old/tools/audit/sovereign_write_inventory.py'>
source = '"""وحدةٌ للاختبار."""\n\n\nclass SeedingStore:\n    def _row(self, session):\n        session.add(object())\n        ...t(self, session):\n        return self._row(session)\n\n\ndef flush(store, session):\n    return store._row(session)\n'
path = 'svc/stores.py'

    def _synthesized(tool: ModuleType, source: str, path: str = "svc/stores.py") -> list:
        tree = ast.parse(source)
        visitor = tool._WriteVisitor(path, source)
        visitor.visit(tree)
        return tool.synthesize_public_sites(
>           visitor.sites, visitor.qcalls, visitor.qnodes, path, source
                           ^^^^^^^^^^^^^^
        )
E       AttributeError: '_WriteVisitor' object has no attribute 'qcalls'. Did you mean: 'calls'?

tests/governance/test_wi113_inventory_qualified_index.py:83: AttributeError
_______ test_persistent_py_has_one_synthesized_get_owned_by_system_state _______

    def test_persistent_py_has_one_synthesized_get_owned_by_system_state() -> None:
        """الشجرةُ الحاضرة: 8 مواقعَ كاذبةُ الهويّةِ صارت موقعًا واحدًا بهويّتِه الحقّ."""
        tool = _load_tool()
        source = (REPO_ROOT / PERSISTENT).read_text(encoding="utf-8")
>       added = _synthesized(tool, source, str(PERSISTENT))
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/governance/test_wi113_inventory_qualified_index.py:121: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/gemini_3_8_flash/wi113/old/tools/audit/sovereign_write_inventory.py'>
source = '"""\nAMOS-Federation Persistent Stores\nالهدف: تخزين دائم بـ SQLAlchemy (SQLite/PostgreSQL) بدلاً من In-Memory\nالنطا...\n            session.commit()\n            return self._as_dict(row)\n        finally:\n            session.close()\n'
path = 'federal/executive/services/src/amos_federation/common/persistent.py'

    def _synthesized(tool: ModuleType, source: str, path: str = "svc/stores.py") -> list:
        tree = ast.parse(source)
        visitor = tool._WriteVisitor(path, source)
        visitor.visit(tree)
        return tool.synthesize_public_sites(
>           visitor.sites, visitor.qcalls, visitor.qnodes, path, source
                           ^^^^^^^^^^^^^^
        )
E       AttributeError: '_WriteVisitor' object has no attribute 'qcalls'. Did you mean: 'calls'?

tests/governance/test_wi113_inventory_qualified_index.py:83: AttributeError
=========================== short test summary info ============================
FAILED tests/governance/test_wi113_inventory_qualified_index.py::test_reader_sharing_a_name_with_a_writer_is_not_a_write_site
FAILED tests/governance/test_wi113_inventory_qualified_index.py::test_real_writer_through_helper_is_still_counted
FAILED tests/governance/test_wi113_inventory_qualified_index.py::test_unknown_receiver_keeps_the_declared_conservative_limit
FAILED tests/governance/test_wi113_inventory_qualified_index.py::test_persistent_py_has_one_synthesized_get_owned_by_system_state
4 failed in 0.10s
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo/../old && /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo/.venv/bin/python tools/audit/decision_gate.py --measure
EXIT: 0
BYTES: 159
SHA256: 7f9727c85f92795ace96cad8a72260bb5dc788d2c40a9d1c2f7934d663107190
NO_EOL: 0
--- OUTPUT ---
{
 "debt": 142,
 "sovereign": 46,
 "closed_legacy": 7,
 "write_sites_total": 239,
 "git_head": "6aacee81",
 "waves": {
  "W1": 11,
  "W2": 34,
  "W3": 97
 }
}
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && nl -ba federal/executive/services/src/amos_federation/common/persistent.py | sed -n '880,960p'
EXIT: 0
BYTES: 3944
SHA256: 626ca4c8ca4538fadc8efc4e987aff9c21608823e6700390e129b90ae0d0fc98
NO_EOL: 0
--- OUTPUT ---
   880	                    "valid": False,
   881	                    "entries": len(rows),
   882	                    "message": f"تلاعب في السجل {entry.id} — hash لا يطابق المحتوى",
   883	                }
   884	            return {"valid": True, "entries": len(rows), "message": "السلسلة سليمة"}
   885	        finally:
   886	            session.close()
   887	
   888	    def tamper_attempt(self, audit_id: str) -> dict[str, Any]:
   889	        """محاولة تعديل سجل — مرفوضة دائمًا."""
   890	        return {
   891	            "error": "INSERT-only: لا يمكن تعديل أو حذف سجلات التدقيق",
   892	            "audit_id": audit_id,
   893	            "blocked": True,
   894	        }
   895	
   896	
   897	class PersistentSystemStateStore:
   898	    """حالةُ النظامِ (مفتاحُ الإيقافِ) في جدولٍ دائمٍ لا في ذاكرةِ عمليّة.
   899	
   900	    قرارُ المالكِ في Q-39 (أ) — 2026-08-23: «مفتاحُ الإيقافِ والترقياتُ أوّلًا».
   901	    وأثرُه على عقدِ التشغيلِ مُعلَنٌ ولا يُسكَتُ عنه: **إعادةُ التشغيلِ لا تُطفِئُ
   902	    الإيقافَ**، فمن أوقفَ النظامَ لا يرفعُه إلا رفعٌ صريحٌ (`reset`).
   903	    """
   904	
   905	    DEFAULT_ID = "system"
   906	
   907	    def _row(self, session: Any) -> Any:
   908	        """الصفُّ الواحدُ، يُنشأُ بالحالةِ الطبيعيّةِ إن لم يكن موجودًا."""
   909	        query = session.query(SystemStateModel)
   910	        row = query.filter(SystemStateModel.id == self.DEFAULT_ID).first()
   911	        if row is None:
   912	            row = SystemStateModel(
   913	                id=self.DEFAULT_ID,
   914	                level="normal",
   915	                reason="",
   916	                activated_at=None,
   917	                activated_by="",
   918	            )
   919	            session.add(row)
   920	            session.commit()
   921	        return row
   922	
   923	    @staticmethod
   924	    def _as_dict(row: Any) -> dict[str, Any]:
   925	        return {
   926	            "level": row.level,
   927	            "reason": row.reason or "",
   928	            "activated_at": row.activated_at,
   929	            "activated_by": row.activated_by or "",
   930	        }
   931	
   932	    def get(self) -> dict[str, Any]:
   933	        """الحالةُ الحاليّةُ للدولةِ — تُقرأُ من القاعدةِ في كلِّ نداء."""
   934	        session_local = get_session_factory()
   935	        session = session_local()
   936	        try:
   937	            return self._as_dict(self._row(session))
   938	        finally:
   939	            session.close()
   940	
   941	    def set_level(self, level: str, reason: str, activated_by: str) -> dict[str, Any]:
   942	        """اكتُبْ مستوًى جديدًا — كتابةٌ دائمةٌ تنجو من إعادةِ التشغيل."""
   943	        session_local = get_session_factory()
   944	        session = session_local()
   945	        try:
   946	            row = self._row(session)
   947	            row.level = level
   948	            row.reason = reason
   949	            row.activated_at = datetime.now(UTC).isoformat()
   950	            row.activated_by = activated_by
   951	            session.commit()
   952	            return self._as_dict(row)
   953	        finally:
   954	            session.close()
   955	
   956	    def reset(self) -> dict[str, Any]:
   957	        """ارفعِ الإيقافَ صراحةً — الرفعُ فعلٌ مقصودٌ لا نتيجةُ إقلاع."""
   958	        session_local = get_session_factory()
   959	        session = session_local()
   960	        try:
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && rg -n 'WI-113|A1\(هـ\)|تصحيح قياس' docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 1
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && sha256sum docs/audit/evidence/W-673/briefs_wi113/briefing_gemini_3_8_flash.md
EXIT: 0
BYTES: 134
SHA256: 86af0c909d127b23c97b1aa5c58f563daeea5c7da077c98c583cf53d398a7726
NO_EOL: 0
--- OUTPUT ---
cf46f61134efed7ab504ddc333ce6a1bedd520aadcddf1d0e3171d9fc27d5eb8  docs/audit/evidence/W-673/briefs_wi113/briefing_gemini_3_8_flash.md
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && cat docs/audit/evidence/W-673/briefs_wi113/SHA256SUMS
EXIT: 0
BYTES: 268
SHA256: bc71f2a392dfafbac053abcffad9db8031f801833c09ce344fce10f5d2b77842
NO_EOL: 0
--- OUTPUT ---
cf46f61134efed7ab504ddc333ce6a1bedd520aadcddf1d0e3171d9fc27d5eb8  briefing_gemini_3_8_flash.md
f3dbbcb67a9d4ab2c43ca3423343c4107eff1a857a090a76d48aae5a89eb3ffd  briefing_grok_4_7.md
4ca60bb75474edcab8de7a3dc6ac8c30a7174fb9aa23af965671d84af125509f  briefing_kimi_k3.md
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w673/gemini_3_8_flash/wi113/probe/probe_wi113.py
EXIT: 0
BYTES: 13246
SHA256: c82381cd54226a5c19a1ae48a96060319495be0304fbab4d788a51ad0c303b69
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ المقعدِ الخاصِّ — WI-113 (مقعد gemini_3_8_flash).
     3	
     4	الهدف:
     5	    فحصُ واختبارُ خاصيّةِ الفهرسةِ بالاسمِ المؤهَّلِ في أداةِ جردِ الكتاباتِ
     6	    (tools/audit/sovereign_write_inventory.py) ومحاولةُ كسرِ الخصائصِ المُدَّعاة:
     7	    1. كسرُ خاصيّةِ عزلِ القارئِ عن الكاتبِ عندَ تشارُكِ أسماءِ التوابعِ والمعاونين:
     8	       صنفان مستقلان يعرفان التابع والمعاون بالاسم نفسه — هل تُنسَب كتابة للقارئ؟
     9	    2. كسرُ خاصيّةِ صيانةِ الكتابةِ في الأصنافِ الوارثة (منع الإسقاط الكاذب):
    10	       صنف وارث يستدعي معاونًا كاتبًا معرَّفًا في الصنف الأساس عبر `self._helper()` —
    11	       هل تسقط كتابة حقيقية من العدّ بعد الإصلاح؟
    12	    3. كسرُ خاصيّةِ حفظِ التتبُّعِ للمُستقبِلِ المجهول:
    13	       استدعاء على مُستقبِلٍ مجهول `obj._step()` — هل يُحفظ الحد المتحفظ القديم؟
    14	    4. تتبُّعُ السلاسلِ العميقةِ للمعاونين (Multi-step helper chains):
    15	       تابع عام يستدعي معاونًا وسيطًا يستدعي معاونًا كاتبًا — هل يُتتبّع بنجاح؟
    16	    5. فحصُ الشجرةِ الإنتاجيّةِ الحقيقيّةِ على common/persistent.py وكاملِ المستودع:
    17	       - التحقق من سقوط القراءات السبع الزائفة لـ PersistentPromotionStore.get.
    18	       - التحقق من بقاء البذر الكسول الحقيقي لـ PersistentSystemStateStore.get.
    19	       - مطابقة إجمالي مواقع الكتابة (232) ودين الهجرة D-4 (135).
    20	"""
    21	
    22	from __future__ import annotations
    23	
    24	import ast
    25	import importlib.util
    26	import sys
    27	from pathlib import Path
    28	
    29	REPO_ROOT = Path("/home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo")
    30	TOOL_PATH = REPO_ROOT / "tools" / "audit" / "sovereign_write_inventory.py"
    31	PERSISTENT_FILE = REPO_ROOT / "federal/executive/services/src/amos_federation/common/persistent.py"
    32	
    33	
    34	def load_tool():
    35	    spec = importlib.util.spec_from_file_location("probe_inv_tool", TOOL_PATH)
    36	    mod = importlib.util.module_from_spec(spec)
    37	    sys.modules["probe_inv_tool"] = mod
    38	    spec.loader.exec_module(mod)
    39	    return mod
    40	
    41	
    42	def run_probe() -> int:
    43	    print("=== بدء تشغيل مسبار WI-113 لمقعد gemini_3_8_flash ===")
    44	    tool = load_tool()
    45	    failures = []
    46	
    47	    # -------------------------------------------------------------------------
    48	    # اختبار 1: صنفان يشتركان في اسم التابع العام واسم المعاون (قارئ مقابل كاتب)
    49	    # -------------------------------------------------------------------------
    50	    print("\n[فحص 1] اختبار عزل صنف قارئ يشارك صنفًا كاتبًا اسم التابع والمعاون...")
    51	    src_two_classes = '''
    52	class DBWriter:
    53	    def _save(self, session):
    54	        session.commit()
    55	
    56	    def process(self, session):
    57	        return self._save(session)
    58	
    59	class CacheReader:
    60	    def _save(self, session):
    61	        return session.get("cache_key")
    62	
    63	    def process(self, session):
    64	        return self._save(session)
    65	'''
    66	    tree = ast.parse(src_two_classes)
    67	    visitor = tool._WriteVisitor("test_mod.py", src_two_classes)
    68	    visitor.visit(tree)
    69	    synthesized = tool.synthesize_public_sites(
    70	        visitor.sites, visitor.qcalls, visitor.qnodes, "test_mod.py", src_two_classes
    71	    )
    72	    synth_identities = {(s.owner, s.function, tuple(s.writes_via)) for s in synthesized}
    73	
    74	    expected_writer = ("DBWriter", "process", ("_save",))
    75	    forbidden_reader = ("CacheReader", "process", ("_save",))
    76	
    77	    if expected_writer in synth_identities and forbidden_reader not in synth_identities:
    78	        print("  ✓ ثبتت الخاصية: DBWriter.process محتسَب كتابة، وCacheReader.process لم يُحتسَب.")
    79	    else:
    80	        msg = f"انكسرت خاصية عزل القارئ: identities={synth_identities}"
    81	        print(f"  ✗ {msg}")
    82	        failures.append(msg)
    83	
    84	    # -------------------------------------------------------------------------
    85	    # اختبار 2: وراثة واستدعاء معاون كاتب في الصنف الأساس عبر self._helper
    86	    # -------------------------------------------------------------------------
    87	    print("\n[فحص 2] اختبار صنف وارث يستدعي معاونًا كاتبًا في الصنف الأساس (منع الإسقاط الكاذب)...")
    88	    src_inheritance = '''
    89	class BaseRepository:
    90	    def _persist(self, session):
    91	        session.add(object())
    92	        session.commit()
    93	
    94	class EntityService(BaseRepository):
    95	    def update_record(self, session):
    96	        return self._persist(session)
    97	'''
    98	    tree2 = ast.parse(src_inheritance)
    99	    vis2 = tool._WriteVisitor("test_inh.py", src_inheritance)
   100	    vis2.visit(tree2)
   101	    synth2 = tool.synthesize_public_sites(
   102	        vis2.sites, vis2.qcalls, vis2.qnodes, "test_inh.py", src_inheritance
   103	    )
   104	    synth2_ids = {(s.owner, s.function, tuple(s.writes_via)) for s in synth2}
   105	
   106	    expected_inh = ("EntityService", "update_record", ("_persist",))
   107	    if expected_inh in synth2_ids:
   108	        print("  ✓ ثبتت الخاصية: EntityService.update_record احتُسِب كتابةً بمعاونِه الموروث _persist.")
   109	    else:
   110	        msg = f"انكسرت خاصية تتبع المعاون الموروث: synth2_ids={synth2_ids}"
   111	        print(f"  ✗ {msg}")
   112	        failures.append(msg)
   113	
   114	    # -------------------------------------------------------------------------
   115	    # اختبار 3: استدعاء على مستقبل مجهول obj._step() (صيانة الحد القديم المتحفظ)
   116	    # -------------------------------------------------------------------------
   117	    print("\n[فحص 3] اختبار صيانة تتبع المستقبل المجهول (obj._step)...")
   118	    src_unknown = '''
   119	class Worker:
   120	    def _execute(self, session):
   121	        session.commit()
   122	
   123	def run_job(target, session):
   124	    return target._execute(session)
   125	'''
   126	    tree3 = ast.parse(src_unknown)
   127	    vis3 = tool._WriteVisitor("test_unk.py", src_unknown)
   128	    vis3.visit(tree3)
   129	    synth3 = tool.synthesize_public_sites(
   130	        vis3.sites, vis3.qcalls, vis3.qnodes, "test_unk.py", src_unknown
   131	    )
   132	    synth3_ids = {(s.owner, s.function) for s in synth3}
   133	
   134	    if ("-", "run_job") in synth3_ids:
   135	        print("  ✓ ثبتت الخاصية: الدالة العامة run_job احتُسِبت بالحد المتحفظ للمستقبل المجهول.")
   136	    else:
   137	        msg = f"انكسرت خاصية تتبع المستقبل المجهول: synth3_ids={synth3_ids}"
   138	        print(f"  ✗ {msg}")
   139	        failures.append(msg)
   140	
   141	    # -------------------------------------------------------------------------
   142	    # اختبار 4: سلسلة معاونين متعددة الحلقات (multi-step chain: public -> _mid -> _leaf)
   143	    # -------------------------------------------------------------------------
   144	    print("\n[فحص 4] اختبار تتبع سلسلة معاونين متعددة المراحل...")
   145	    src_chain = '''
   146	class PipelineStore:
   147	    def _leaf_write(self, session):
   148	        session.commit()
   149	
   150	    def _mid_helper(self, session):
   151	        self._leaf_write(session)
   152	
   153	    def submit(self, session):
   154	        self._mid_helper(session)
   155	'''
   156	    tree4 = ast.parse(src_chain)
   157	    vis4 = tool._WriteVisitor("test_chain.py", src_chain)
   158	    vis4.visit(tree4)
   159	    synth4 = tool.synthesize_public_sites(
   160	        vis4.sites, vis4.qcalls, vis4.qnodes, "test_chain.py", src_chain
   161	    )
   162	    synth4_ids = {(s.owner, s.function, tuple(s.writes_via)) for s in synth4}
   163	
   164	    expected_chain = ("PipelineStore", "submit", ("_leaf_write",))
   165	    if expected_chain in synth4_ids:
   166	        print("  ✓ ثبتت الخاصية: PipelineStore.submit تتبّع السلسلة بنجاح إلى _leaf_write.")
   167	    else:
   168	        msg = f"انكسرت خاصية السلسلة متعددة المراحل: synth4_ids={synth4_ids}"
   169	        print(f"  ✗ {msg}")
   170	        failures.append(msg)
   171	
   172	    # -------------------------------------------------------------------------
   173	    # اختبار 5: التحقق من شجرة persistent.py الإنتاجية الحقيقية والمستودع
   174	    # -------------------------------------------------------------------------
   175	    print("\n[فحص 5] التحقق من ملف الإنتاج persistent.py وسقوط القراءات السبع وبقاء البذر الكسول...")
   176	    source_persistent = PERSISTENT_FILE.read_text(encoding="utf-8")
   177	    tree_p = ast.parse(source_persistent)
   178	    vis_p = tool._WriteVisitor(str(PERSISTENT_FILE), source_persistent)
   179	    vis_p.visit(tree_p)
   180	    synth_p = tool.synthesize_public_sites(
   181	        vis_p.sites, vis_p.qcalls, vis_p.qnodes, str(PERSISTENT_FILE), source_persistent
   182	    )
   183	
   184	    get_sites = [s for s in synth_p if s.function == "get"]
   185	    print(f"  عدد مواقع 'get' المركبة الناتجة في persistent.py: {len(get_sites)}")
   186	    for s in get_sites:
   187	        print(f"    - owner={s.owner}, function={s.function}, writes_via={s.writes_via}")
   188	
   189	    if len(get_sites) == 1 and get_sites[0].owner == "PersistentSystemStateStore":
   190	        print("  ✓ ثبتت الخاصية: يوجد موقع 'get' واحد فقط لـ PersistentSystemStateStore.")
   191	    else:
   192	        msg = f"فشل فحص persistent.py: get_sites={[(s.owner, s.function) for s in get_sites]}"
   193	        print(f"  ✗ {msg}")
   194	        failures.append(msg)
   195	
   196	    # التحقق من أن PersistentPromotionStore.get غير موجود
   197	    promo_gets = [s for s in get_sites if s.owner == "PersistentPromotionStore"]
   198	    if not promo_gets:
   199	        print("  ✓ ثبتت الخاصية: قراءات PersistentPromotionStore.get غير محتسبة إطلاقًا.")
   200	    else:
   201	        msg = f"فشل عزل PersistentPromotionStore.get: وجد {len(promo_gets)} موقعًا."
   202	        print(f"  ✗ {msg}")
   203	        failures.append(msg)
   204	
   205	    # التحقق من إجمالي مواقع persistent.py عبر collect
   206	    all_sites = tool.collect(REPO_ROOT)
   207	    p_sites = [s for s in all_sites if "persistent.py" in s.path and not s.function.startswith("_")]
   208	    print(f"  إجمالي المواقع العامة في persistent.py: {len(p_sites)} (المتوقع 13 بعد إسقاط 7)")
   209	    if len(p_sites) == 13:
   210	        print("  ✓ ثبتت الخاصية: عدد المواقع العامة في persistent.py هو 13 تمامًا.")
   211	    else:
   212	        msg = f"العدد العام في persistent.py هو {len(p_sites)} وليس 13"
   213	        print(f"  ✗ {msg}")
   214	        failures.append(msg)
   215	
   216	    # -------------------------------------------------------------------------
   217	    # الخلاصة
   218	    # -------------------------------------------------------------------------
   219	    print("\n=== ملخص نتائج المسبار ===")
   220	    if failures:
   221	        print(f"✗ انكسرت خصائص مدّعاة ({len(failures)} إخفاقات):")
   222	        for f in failures:
   223	            print(f"  - {f}")
   224	        return 1
   225	
   226	    print("✓ اجتازت جميع الفحوصات (5/5): الخاصيّةُ المُدَّعاةُ صادقةٌ تمامًا على الأداة والمسار الإنتاجي.")
   227	    return 0
   228	
   229	
   230	if __name__ == "__main__":
   231	    sys.exit(run_probe())
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi113/repo && .venv/bin/python /home/user/workspace/council_w673/gemini_3_8_flash/wi113/probe/probe_wi113.py
EXIT: 0
BYTES: 1962
SHA256: 8696eeef133a40bcacdc9d6532353ccde6fda9bbce4a6d9420b2b769e500da00
NO_EOL: 0
--- OUTPUT ---
=== بدء تشغيل مسبار WI-113 لمقعد gemini_3_8_flash ===

[فحص 1] اختبار عزل صنف قارئ يشارك صنفًا كاتبًا اسم التابع والمعاون...
  ✓ ثبتت الخاصية: DBWriter.process محتسَب كتابة، وCacheReader.process لم يُحتسَب.

[فحص 2] اختبار صنف وارث يستدعي معاونًا كاتبًا في الصنف الأساس (منع الإسقاط الكاذب)...
  ✓ ثبتت الخاصية: EntityService.update_record احتُسِب كتابةً بمعاونِه الموروث _persist.

[فحص 3] اختبار صيانة تتبع المستقبل المجهول (obj._step)...
  ✓ ثبتت الخاصية: الدالة العامة run_job احتُسِبت بالحد المتحفظ للمستقبل المجهول.

[فحص 4] اختبار تتبع سلسلة معاونين متعددة المراحل...
  ✓ ثبتت الخاصية: PipelineStore.submit تتبّع السلسلة بنجاح إلى _leaf_write.

[فحص 5] التحقق من ملف الإنتاج persistent.py وسقوط القراءات السبع وبقاء البذر الكسول...
  عدد مواقع 'get' المركبة الناتجة في persistent.py: 1
    - owner=PersistentSystemStateStore, function=get, writes_via=('_row',)
  ✓ ثبتت الخاصية: يوجد موقع 'get' واحد فقط لـ PersistentSystemStateStore.
  ✓ ثبتت الخاصية: قراءات PersistentPromotionStore.get غير محتسبة إطلاقًا.
  إجمالي المواقع العامة في persistent.py: 13 (المتوقع 13 بعد إسقاط 7)
  ✓ ثبتت الخاصية: عدد المواقع العامة في persistent.py هو 13 تمامًا.

=== ملخص نتائج المسبار ===
✓ اجتازت جميع الفحوصات (5/5): الخاصيّةُ المُدَّعاةُ صادقةٌ تمامًا على الأداة والمسار الإنتاجي.
=== RAW [17] END ===
VERDICT_PER_CRITERION: (1) نعم: الفهرسة صارت بالاسم المؤهل Class.method عبر الدالتين qualify وresolve_callees واستخدام visitor.qcalls وvisitor.qnodes في tools/audit/sovereign_write_inventory.py بدلاً من الفهرسة بالاسم المجرد node.name، وإسناد المالك owner إلى صنف التابع الحق من qnodes بدلاً من آخر صنف يعرف الاسم classes[child.name] — مثبت بالدليل في فرق الالتزام 6605fa88e (الأمر 6)، واجتياز فحوص test_wi113_inventory_qualified_index.py (الأمر 7)، ومسبار المقعد المستقل (الأمران 16 و17).
(2) نعم: فحص test_wi113_inventory_qualified_index.py يثبت في test_persistent_py_has_one_synthesized_get_owned_by_system_state أن ملف common/persistent.py يحتوي على موقع get واحد مركب فقط وهو PersistentSystemStateStore.get (writes_via=('_row',)) وهو موضع البذر الكسول الحقيقي (:932 وما حوله في الأمر 12)، وأن القراءات السبع الزائفة لـ PersistentPromotionStore.get (التي كانت تُحتسب كتابات سابقًا) سقطت تمامًا ولم تعد محتسبة (الأمران 7 و9 ومسبار المقعد في الفحص 5 بالأمرين 16 و17).
(3) نعم: طفرة إرجاع الفهرسة بالاسم المجرد يكتشفها الفحص: عند تشغيل الفحص على شجرة العمل القديمة قبل إصلاح W-669 (الأمر 10)، يسقط الفحص فورًا في جميع الاختبارات الأربعة (4 failed برمز خروج 1) لاعتماد الفحص على واجهة الفهرسة المؤهلة؛ وعلى الصعيد الدلالي تثبت الطفرة M1 في سجل الطفرات ومسبار المقعد المستقل (الأمران 16 و17) أن الفهرسة بالاسم المجرد تكسر عزل القارئ عن الكاتب بينما الفهرسة المؤهلة تصونه.
(4) نعم: قياس D-4 بالأمر الخام decision_gate.py --measure أُجري قبل وبعد: قبل الإصلاح (الأمر 11 على الشجرة القديمة) debt = 142، write_sites_total = 239، والموجة W3 = 97؛ وبعد الإصلاح (الأمر 8) debt = 135، write_sites_total = 232، والموجة W3 = 90 (مع ثبات السيادي 46 والمغلق القديم 7). الفرق هو انخفاض D-4 بسبعة مواقع بالضبط (-7)، ومسجل نصًّا «تصحيح قياس لا حرق» تحت نوع الأداة work_drift في decision_gate_ledger.json (الأمران 5 و6) تنفيذًا لأمر التوجيه 22 § 2.
PROBES: مسبار 1: كتلة الشفرة [16] · كتلة التشغيل [17] · الخاصيّة: محاولة كسر عزل القارئ عن الكاتب عند تشارك الأسماء (فحص 1)، وكسر تتبع المعاون في الصنف الوارث عند استدعاء self._helper لمنع الإسقاط الكاذب (فحص 2)، وكسر الحد القديم المتحفظ للمستقبل المجهول obj._step (فحص 3)، وتتبع سلاسل المعاونين العميقة (فحص 4)، وفحص شجرة persistent.py الإنتاجية الحقيقية وسقوط القراءات السبع وبقاء البذر الكسول ومطابقة أرقام المستودع (فحص 5) · انكسرت؟ لا (ثبتت جميع الخصائص 5/5 واجتاز المسبار بنجاح تام برمز خروج 0).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: أقرُّ بأنّني لم أقرأْ ولم أكتبْ خارجَ جذري /home/user/workspace/council_w673/gemini_3_8_flash/wi113/ واستنساخي الداخليِّ وهذه الإحاطة، ولم أطَّلع على عملِ المقاعدِ الأخرى ولا تقاريرِ المنفِّذ.
VERDICT: PASS لكلِّ المعاييرِ
