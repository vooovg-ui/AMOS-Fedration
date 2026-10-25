# حكمُ مقعدِ المجلسِ — grok_4_7 · جولةُ WI-113 (W-679)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-113 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w673/grok_4_7/wi113) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `56e78b701a61a5a5cffd9804db069884efeaf31f9c5b3438db3c82f2c8d0d0a9`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-113 عندَ العقدةِ `79abc6a2` — إحاطةٌ مبصومةٌ (W-673) ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9) · والفحصُ النهائيُّ للنصابِ معلَّقٌ على شرائطِ § 4.7 (قياسُ عيبَي الفاحصِ في W-679).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-679) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-25

## تاريخ آخر تعديل
2026-10-25

---
MODEL: grok_4_7
FAMILY: grok
RUN_DATE: 2026-10-25 23:43 +00:00
NODE: 79abc6a206000e162689d642d1ebc42af36f445a
CLONE_PATH: /home/user/workspace/council_w673/grok_4_7/wi113/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/
 2. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/)
 3. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git log --format='%h %cI %s' -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
 5. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git show --stat 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7
 6. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git diff 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7 -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
 7. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
 8. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python tools/audit/decision_gate.py --measure
 9. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 10. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && rm -rf ../old && git worktree add --detach ../old 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ && cp tests/governance/test_wi113_inventory_qualified_index.py ../old/tests/governance/ && cd ../old && /home/user/workspace/council_w673/grok_4_7/wi113/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
 11. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo/../old && /home/user/workspace/council_w673/grok_4_7/wi113/repo/.venv/bin/python tools/audit/decision_gate.py --measure
 12. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && nl -ba federal/executive/services/src/amos_federation/common/persistent.py | sed -n '880,960p'
 13. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && rg -n 'WI-113|A1\(هـ\)|تصحيح قياس' docs/audit/SOVEREIGN_DECISION_REGISTER.md
 14. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && sha256sum docs/audit/evidence/W-673/briefs_wi113/briefing_grok_4_7.md
 15. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && cat docs/audit/evidence/W-673/briefs_wi113/SHA256SUMS
 16. nl -ba /home/user/workspace/council_w673/grok_4_7/wi113/probe/break_qualified_index.py
 17. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python /home/user/workspace/council_w673/grok_4_7/wi113/probe/break_qualified_index.py
 18. nl -ba /home/user/workspace/council_w673/grok_4_7/wi113/probe/semantic_bare_mutation.py
 19. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python /home/user/workspace/council_w673/grok_4_7/wi113/probe/semantic_bare_mutation.py
 20. cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && rg -n 'تصحيحُ قياسٍ لا حرقٌ|تصحيحُ قياسٍ — لا حرقٌ' docs/audit/measurements/decision_gate_ledger.json docs/audit/COMPLETION_LEDGER.md docs/audit/ACTIVE_EXECUTION_STATE.md
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/)
EXIT: 0
BYTES: 329
SHA256: 820b1154c5055620984fd0bba0e902931b07c236382c0e2d712be5b3ef5bcc27
NO_EOL: 0
--- OUTPUT ---
HEAD is now at 79abc6a2 W-673: WI-113 وWI-115 IN_PROGRESS→IN_REVIEW · ستُّ إحاطاتٍ مبصومةٍ لجولةِ المجلسِ (gemini_3_8_flash · grok_4_7 · kimi_k3) ونصوصُ الإطلاقِ حرفيًّا · WI-115 بنطاقِ § 3.5 وحدَه · لا شِفرةَ — المنسِّقُ Claude Opus 5.5
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git log --format='%h %cI %s' -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git show --stat 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git diff 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7 -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 0
BYTES: 98
SHA256: f87e1ec159e73ceaff96b34a3bc29b017111816d05b56b64e23a829128ce891b
NO_EOL: 0
--- OUTPUT ---
....                                                                     [100%]
4 passed in 0.08s
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python tools/audit/decision_gate.py --measure
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && rm -rf ../old && git worktree add --detach ../old 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ && cp tests/governance/test_wi113_inventory_qualified_index.py ../old/tests/governance/ && cd ../old && /home/user/workspace/council_w673/grok_4_7/wi113/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 1
BYTES: 8044
SHA256: 2431796ab9ea8c99859b596ce9453bf301b106737a9bea4c76a79581bf1c3263
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD 6aacee81)
Updating files:  91% (2409/2628)Updating files:  92% (2418/2628)Updating files:  93% (2445/2628)Updating files:  94% (2471/2628)Updating files:  95% (2497/2628)Updating files:  96% (2523/2628)Updating files:  97% (2550/2628)Updating files:  98% (2576/2628)Updating files:  99% (2602/2628)Updating files: 100% (2628/2628)Updating files: 100% (2628/2628), done.
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

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/grok_4_7/wi113/old/tools/audit/sovereign_write_inventory.py'>
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

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/grok_4_7/wi113/old/tools/audit/sovereign_write_inventory.py'>
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

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/grok_4_7/wi113/old/tools/audit/sovereign_write_inventory.py'>
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

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/grok_4_7/wi113/old/tools/audit/sovereign_write_inventory.py'>
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo/../old && /home/user/workspace/council_w673/grok_4_7/wi113/repo/.venv/bin/python tools/audit/decision_gate.py --measure
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && nl -ba federal/executive/services/src/amos_federation/common/persistent.py | sed -n '880,960p'
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && rg -n 'WI-113|A1\(هـ\)|تصحيح قياس' docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 1
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && sha256sum docs/audit/evidence/W-673/briefs_wi113/briefing_grok_4_7.md
EXIT: 0
BYTES: 126
SHA256: 493b9e8a84297b21ff5820681a8004de2adb8538fb69708382eea2749ad2fa03
NO_EOL: 0
--- OUTPUT ---
f3dbbcb67a9d4ab2c43ca3423343c4107eff1a857a090a76d48aae5a89eb3ffd  docs/audit/evidence/W-673/briefs_wi113/briefing_grok_4_7.md
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && cat docs/audit/evidence/W-673/briefs_wi113/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w673/grok_4_7/wi113/probe/break_qualified_index.py
EXIT: 0
BYTES: 9411
SHA256: 3b196e3f951a6438dfb67f8ae5e71e1eb7ec3f7285686395244909089298727d
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ مقعدِ grok_4_7 لبندِ WI-113.
     3	
     4	ينادي مدخلَ الأداةِ الإنتاجيَّ نفسه
     5	(tools/audit/sovereign_write_inventory.py --root/--service --json)
     6	ويحاولُ كسرَ الخاصيّةِ المُدَّعاة: الفهرسةُ بالاسمِ المؤهَّلِ لا بالمجرَّدِ
     7	ولا بآخرِ صنفٍ، والقارئُ لا يُنسَبُ إليه كتابةُ كاتبٍ يشارُكُه الاسم،
     8	والكتابةُ الحقيقيّةُ لا تسقطُ من العدِّ.
     9	
    10	ليسَ نسخةً من tests/governance/test_wi113_inventory_qualified_index.py
    11	ولا أمرًا من أوامرِ الإحاطة.
    12	"""
    13	
    14	from __future__ import annotations
    15	
    16	import json
    17	import subprocess
    18	import sys
    19	import textwrap
    20	from pathlib import Path
    21	
    22	SEAT = Path("/home/user/workspace/council_w673/grok_4_7/wi113")
    23	REPO = SEAT / "repo"
    24	TOOL = REPO / "tools" / "audit" / "sovereign_write_inventory.py"
    25	PY = REPO / ".venv" / "bin" / "python"
    26	PROBE = SEAT / "probe"
    27	TREE = PROBE / "tree"
    28	SYNTH_JSON = PROBE / "synth_inventory.json"
    29	COMMON_JSON = PROBE / "common_inventory.json"
    30	
    31	SYNTH_SOURCE = textwrap.dedent(
    32	    '''\
    33	    """شجرةٌ مصطنعةٌ لكسرِ الفهرسة: كاتبٌ أوّلُ الملفِّ وقرّاءٌ بعدَه."""
    34	
    35	
    36	    class WriterFirst:
    37	        def _row(self, session):
    38	            session.add(object())
    39	            session.commit()
    40	
    41	        def get(self, session):
    42	            return self._row(session)
    43	
    44	
    45	    class MiddleReader:
    46	        def _row(self, session):
    47	            return session.query(object).first()
    48	
    49	        def get(self, session):
    50	            return self._row(session)
    51	
    52	
    53	    class LastReader:
    54	        def _row(self, session):
    55	            return session.query(object).first()
    56	
    57	        def get(self, session):
    58	            return self._row(session)
    59	
    60	
    61	    class ChildReader(WriterFirst):
    62	        def _row(self, session):
    63	            return session.query(object).first()
    64	
    65	        def fetch(self, session):
    66	            return self._row(session)
    67	
    68	
    69	    class OrphanWriter:
    70	        def _helper(self, session):
    71	            session.add(object())
    72	            session.commit()
    73	
    74	
    75	    class OtherPublic:
    76	        def publish(self, session):
    77	            session.add(object())
    78	            session.commit()
    79	            return self._helper(session)
    80	
    81	        def _helper(self, session):
    82	            return session.query(object).first()
    83	    '''
    84	)
    85	
    86	
    87	def invoke(root: Path, out: Path, service: str | None = None) -> subprocess.CompletedProcess[str]:
    88	    cmd = [str(PY), str(TOOL), "--root", str(root), "--json", str(out)]
    89	    if service:
    90	        cmd.extend(["--service", service])
    91	    print("CLI:", " ".join(cmd))
    92	    proc = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True, check=False)
    93	    print("CLI_EXIT:", proc.returncode)
    94	    if proc.stdout:
    95	        print("CLI_STDOUT:")
    96	        print(proc.stdout, end="" if proc.stdout.endswith("\n") else "\n")
    97	    if proc.stderr:
    98	        print("CLI_STDERR:")
    99	        print(proc.stderr, end="" if proc.stderr.endswith("\n") else "\n")
   100	    return proc
   101	
   102	
   103	def load_sites(path: Path) -> list[dict]:
   104	    payload = json.loads(path.read_text(encoding="utf-8"))
   105	    sites = payload["sites"]
   106	    assert isinstance(sites, list)
   107	    return sites
   108	
   109	
   110	def ident(site: dict) -> str:
   111	    return (
   112	        f"{site.get('owner')}.{site.get('function')} "
   113	        f"public={site.get('public')} writes={site.get('writes')} "
   114	        f"via={site.get('writes_via')} path={site.get('path')}"
   115	    )
   116	
   117	
   118	def main() -> int:
   119	    broken: list[str] = []
   120	    pkg = TREE / "pkg"
   121	    pkg.mkdir(parents=True, exist_ok=True)
   122	    (pkg / "collision.py").write_text(SYNTH_SOURCE, encoding="utf-8")
   123	
   124	    print("== هجمةُ الشجرةِ المصطنعةِ عبرَ المدخلِ الإنتاجيِّ ==")
   125	    synth = invoke(TREE, SYNTH_JSON)
   126	    if synth.returncode != 0 or not SYNTH_JSON.is_file():
   127	        print("BROKEN: المدخلُ الإنتاجيُّ لم يُكمِلْ على الشجرةِ المصطنعةِ")
   128	        return 1
   129	    sites = load_sites(SYNTH_JSON)
   130	    print("SITES:")
   131	    for site in sites:
   132	        print(" ", ident(site))
   133	
   134	    gets = [s for s in sites if s.get("function") == "get"]
   135	    get_owners = [s.get("owner") for s in gets]
   136	    print("GET_OWNERS:", get_owners)
   137	    if get_owners != ["WriterFirst"]:
   138	        broken.append(
   139	            f"نُسبَت كتابةٌ لغيرِ الكاتبِ أو سقطَ الكاتبُ أو فازَ آخرُ صنفٍ: {get_owners}"
   140	        )
   141	    if any(s.get("owner") == "LastReader" and s.get("function") == "get" for s in sites):
   142	        broken.append("آخرُ صنفٍ (LastReader) مُلِّكَ موقعَ get")
   143	    if any(s.get("owner") == "MiddleReader" for s in sites):
   144	        broken.append("قارئٌ أوسطُ نُسبَت إليه كتابةٌ")
   145	    if any(s.get("owner") == "ChildReader" for s in sites):
   146	        broken.append("صنفٌ وارثٌ يعيدُ تعريفَ _row قارئًا ويُنادي self._row حُسبَ كاتبًا")
   147	    writers = [s for s in sites if s.get("owner") == "WriterFirst" and s.get("function") == "get"]
   148	    if not writers:
   149	        broken.append("الكتابةُ الحقيقيّةُ WriterFirst.get سقطَت من العدِّ")
   150	    publishes = [s for s in sites if s.get("owner") == "OtherPublic" and s.get("function") == "publish"]
   151	    if not publishes:
   152	        broken.append("كتابةٌ مباشرةٌ OtherPublic.publish سقطَت من العدِّ")
   153	
   154	    orphan = [s for s in sites if s.get("owner") == "OrphanWriter"]
   155	    print("ORPHAN_PRIVATE_WRITER_SITES:", len(orphan))
   156	    if not orphan:
   157	        print(
   158	            "OBSERVED_LIMIT: OrphanWriter._helper (كتابةٌ خاصّةٌ لا يناديها عامٌّ في صنفِها) "
   159	            "غابَ من عدِّ collect لأنَّ attribute_helper_writes ما زالَ بالاسمِ المجرَّدِ "
   160	            "فيصلُ OtherPublic.publish إلى كلِّ _helper. هذا حدُّ الدالّةِ التي لم يمسَّها "
   161	            "الإصلاحُ، لا إرجاعٌ لفهرسةِ synthesize_public_sites ولا نسبةٌ إلى آخرِ صنفٍ."
   162	        )
   163	    else:
   164	        print("ORPHAN_KEPT:", ident(orphan[0]))
   165	
   166	    print("== هجمةُ persistent.py عبرَ المدخلِ الإنتاجيِّ --service ==")
   167	    common = invoke(
   168	        REPO,
   169	        COMMON_JSON,
   170	        "federal/executive/services/src/amos_federation/common",
   171	    )
   172	    if common.returncode != 0 or not COMMON_JSON.is_file():
   173	        print("BROKEN: المدخلُ الإنتاجيُّ لم يُكمِلْ على common/")
   174	        return 1
   175	    common_sites = load_sites(COMMON_JSON)
   176	    persistent_gets = [
   177	        s
   178	        for s in common_sites
   179	        if str(s.get("path", "")).endswith("common/persistent.py") and s.get("function") == "get"
   180	    ]
   181	    print("PERSISTENT_GETS:", len(persistent_gets))
   182	    for site in persistent_gets:
   183	        print(" ", ident(site))
   184	    if [s.get("owner") for s in persistent_gets] != ["PersistentSystemStateStore"]:
   185	        broken.append(
   186	            "قراءاتُ persistent.py عادت إلى العدِّ أو المالكُ ليس PersistentSystemStateStore: "
   187	            + repr([s.get("owner") for s in persistent_gets])
   188	        )
   189	    state_gets = [
   190	        s for s in persistent_gets if s.get("owner") == "PersistentSystemStateStore"
   191	    ]
   192	    if not state_gets or state_gets[0].get("writes_via") != ["_row"]:
   193	        broken.append("بذرُ PersistentSystemStateStore.get عبرَ _row سقطَ أو تغيّرَ")
   194	
   195	    if broken:
   196	        print("PROPERTY_BROKEN: yes")
   197	        for item in broken:
   198	            print("BREAK:", item)
   199	        return 1
   200	    print("PROPERTY_BROKEN: no")
   201	    print("CLAIMED_PROPERTY_HELD: reader-not-attributed · owner-not-last-class · inherited-override-not-counted · real-public-write-kept · persistent-seven-reads-not-counted")
   202	    return 0
   203	
   204	
   205	if __name__ == "__main__":
   206	    sys.exit(main())
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python /home/user/workspace/council_w673/grok_4_7/wi113/probe/break_qualified_index.py
EXIT: 0
BYTES: 3713
SHA256: c80fbc9fa5d68dc0b4c941d69ee05f92750a98cb4fbc49de6314a950cc5ee70e
NO_EOL: 0
--- OUTPUT ---
== هجمةُ الشجرةِ المصطنعةِ عبرَ المدخلِ الإنتاجيِّ ==
CLI: /home/user/workspace/council_w673/grok_4_7/wi113/repo/.venv/bin/python /home/user/workspace/council_w673/grok_4_7/wi113/repo/tools/audit/sovereign_write_inventory.py --root /home/user/workspace/council_w673/grok_4_7/wi113/probe/tree --json /home/user/workspace/council_w673/grok_4_7/wi113/probe/synth_inventory.json
CLI_EXIT: 0
CLI_STDOUT:
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 2
  عمليّاتٌ عامّةٌ مُغيِّرة   : 2
  منها تعبرُ الحدَّ        : 0
  مساراتٌ قديمةٌ مُغلَقة    : 0
  **لا تعبرُ الحدَّ**       : 2
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    other               2 /   0 /    2
  التوزيعُ على الملفّات:
       2  pkg/collision.py
  التفصيلُ محفوظٌ في: /home/user/workspace/council_w673/grok_4_7/wi113/probe/synth_inventory.json
SITES:
  OtherPublic.publish public=True writes=['add()', 'commit()'] via=['_helper'] path=pkg/collision.py
  WriterFirst.get public=True writes=[] via=['_row'] path=pkg/collision.py
GET_OWNERS: ['WriterFirst']
ORPHAN_PRIVATE_WRITER_SITES: 0
OBSERVED_LIMIT: OrphanWriter._helper (كتابةٌ خاصّةٌ لا يناديها عامٌّ في صنفِها) غابَ من عدِّ collect لأنَّ attribute_helper_writes ما زالَ بالاسمِ المجرَّدِ فيصلُ OtherPublic.publish إلى كلِّ _helper. هذا حدُّ الدالّةِ التي لم يمسَّها الإصلاحُ، لا إرجاعٌ لفهرسةِ synthesize_public_sites ولا نسبةٌ إلى آخرِ صنفٍ.
== هجمةُ persistent.py عبرَ المدخلِ الإنتاجيِّ --service ==
CLI: /home/user/workspace/council_w673/grok_4_7/wi113/repo/.venv/bin/python /home/user/workspace/council_w673/grok_4_7/wi113/repo/tools/audit/sovereign_write_inventory.py --root /home/user/workspace/council_w673/grok_4_7/wi113/repo --json /home/user/workspace/council_w673/grok_4_7/wi113/probe/common_inventory.json --service federal/executive/services/src/amos_federation/common
CLI_EXIT: 0
CLI_STDOUT:
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : federal/executive/services/src/amos_federation/common
  مواضعُ كتابةٍ (كلُّها)   : 22
  عمليّاتٌ عامّةٌ مُغيِّرة   : 21
  منها تعبرُ الحدَّ        : 0
  مساراتٌ قديمةٌ مُغلَقة    : 0
  **لا تعبرُ الحدَّ**       : 21
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    service_common     21 /   0 /   21
  التوزيعُ على الملفّات:
      13  federal/executive/services/src/amos_federation/common/persistent.py
       4  federal/executive/services/src/amos_federation/common/database.py
       2  federal/executive/services/src/amos_federation/common/durable_event_bus.py
       1  federal/executive/services/src/amos_federation/common/event_bus.py
       1  federal/executive/services/src/amos_federation/common/events.py
  التفصيلُ محفوظٌ في: /home/user/workspace/council_w673/grok_4_7/wi113/probe/common_inventory.json
PERSISTENT_GETS: 1
  PersistentSystemStateStore.get public=True writes=[] via=['_row'] path=federal/executive/services/src/amos_federation/common/persistent.py
PROPERTY_BROKEN: no
CLAIMED_PROPERTY_HELD: reader-not-attributed · owner-not-last-class · inherited-override-not-counted · real-public-write-kept · persistent-seven-reads-not-counted
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w673/grok_4_7/wi113/probe/semantic_bare_mutation.py
EXIT: 0
BYTES: 4602
SHA256: a79d528eb1a94838adaa258912c6f37fe6cc176be7994e4bfeccc84fa96c6f52
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""طفرةٌ دلاليّةٌ من عندِ المقعدِ — لا سجلُّ المنفِّذِ.
     3	
     4	تُبقي واجهةَ synthesize_public_sites وqcalls/qnodes، وتُرجِعُ حلَّ النداءاتِ
     5	إلى كلِّ تعريفٍ بالاسمِ المجرَّدِ، ثمَّ تُشغِّلُ فحصَ البندِ نفسَه وتستعيدُ الملفَّ.
     6	الحكمُ: هل يسقطُ الفحصُ بتأكيدٍ (دلاليّ) أم بخطأِ واجهةٍ؟
     7	"""
     8	
     9	from __future__ import annotations
    10	
    11	import shutil
    12	import subprocess
    13	import sys
    14	from pathlib import Path
    15	
    16	SEAT = Path("/home/user/workspace/council_w673/grok_4_7/wi113")
    17	REPO = SEAT / "repo"
    18	TOOL = REPO / "tools" / "audit" / "sovereign_write_inventory.py"
    19	BACKUP = SEAT / "probe" / "inventory_before_semantic_mutation.py"
    20	PY = REPO / ".venv" / "bin" / "python"
    21	
    22	OLD = '''def resolve_callees(
    23	    caller: str, qcalls: dict[str, set[tuple[str, str]]]
    24	) -> set[str]:
    25	    """حُلَّ نداءاتِ `caller` إلى أسماءٍ مؤهَّلةٍ معرَّفةٍ في الوحدة.
    26	
    27	    - `self.x()`/`cls.x()` ← `Owner.x` إن عُرِّفَ في الصنفِ نفسِه؛ وإلّا (موروثٌ أو
    28	      غيرُ معروف) فكلُّ تعريفٍ بالاسم — تحفُّظٌ مُعلَنٌ: الإسقاطُ أخطرُ من الزيادة.
    29	    - `x()` ← دالّةُ الوحدةِ `x` إن وُجدَت؛ وإلّا فكلُّ تعريفٍ بالاسم (دالّةٌ متداخلة).
    30	    - `obj.x()` على مُستقبِلٍ آخر ← كلُّ تعريفٍ بالاسم: أداةٌ ساكنةٌ لا تعرفُ النوع،
    31	      وهذا هو الحدُّ القديمُ نفسُه باقيًا حيثُ لا يُعرَفُ المُستقبِلُ — لا يُخفَّف.
    32	    """
    33	    by_bare: dict[str, set[str]] = {}
    34	    for name in qcalls:
    35	        by_bare.setdefault(_bare(name), set()).add(name)
    36	    owner = caller.rsplit(".", 1)[0] if "." in caller else ""
    37	    resolved: set[str] = set()
    38	    for kind, name in qcalls.get(caller, ()):
    39	        if kind == "self" and owner and f"{owner}.{name}" in qcalls:
    40	            resolved.add(f"{owner}.{name}")
    41	        elif kind == "name" and name in qcalls:
    42	            resolved.add(name)
    43	        else:
    44	            resolved.update(by_bare.get(name, ()))
    45	    return resolved
    46	'''
    47	
    48	NEW = '''def resolve_callees(
    49	    caller: str, qcalls: dict[str, set[tuple[str, str]]]
    50	) -> set[str]:
    51	    """طفرةُ المقعدِ: كلُّ نداءٍ يُحَلُّ إلى كلِّ تعريفٍ بالاسمِ المجرَّدِ."""
    52	    by_bare: dict[str, set[str]] = {}
    53	    for name in qcalls:
    54	        by_bare.setdefault(_bare(name), set()).add(name)
    55	    resolved: set[str] = set()
    56	    for _kind, name in qcalls.get(caller, ()):
    57	        resolved.update(by_bare.get(name, ()))
    58	    return resolved
    59	'''
    60	
    61	
    62	def main() -> int:
    63	    original = TOOL.read_text(encoding="utf-8")
    64	    if OLD not in original:
    65	        print("MUTATION_ANCHOR_MISSING")
    66	        return 2
    67	    BACKUP.write_text(original, encoding="utf-8")
    68	    TOOL.write_text(original.replace(OLD, NEW, 1), encoding="utf-8")
    69	    print("MUTATION_APPLIED: resolve_callees resolves every call to all bare-name definitions; signature kept")
    70	    try:
    71	        proc = subprocess.run(
    72	            [
    73	                str(PY),
    74	                "-m",
    75	                "pytest",
    76	                "-q",
    77	                "-p",
    78	                "no:cacheprovider",
    79	                "tests/governance/test_wi113_inventory_qualified_index.py",
    80	            ],
    81	            cwd=str(REPO),
    82	            check=False,
    83	        )
    84	        print("PYTEST_EXIT:", proc.returncode)
    85	        return proc.returncode
    86	    finally:
    87	        TOOL.write_text(BACKUP.read_text(encoding="utf-8"), encoding="utf-8")
    88	        restored = TOOL.read_text(encoding="utf-8")
    89	        print("RESTORED:", "طفرةُ المقعدِ" not in restored and OLD in restored)
    90	
    91	
    92	if __name__ == "__main__":
    93	    sys.exit(main())
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python /home/user/workspace/council_w673/grok_4_7/wi113/probe/semantic_bare_mutation.py
EXIT: 1
BYTES: 1406
SHA256: 46988a5386d59f9e8840e524c2870dce4effff4479fe4b4f9b8e2693ed8f6b2f
NO_EOL: 0
--- OUTPUT ---
F...                                                                     [100%]
=================================== FAILURES ===================================
_________ test_reader_sharing_a_name_with_a_writer_is_not_a_write_site _________

    def test_reader_sharing_a_name_with_a_writer_is_not_a_write_site() -> None:
        """`ReadingStore.get` لا يُحسَبُ كتابةً لأنَّ `SeedingStore._row` يكتب."""
        tool = _load_tool()
        added = _synthesized(tool, TWO_STORES)
        identities = [(site.owner, site.function, site.writes_via) for site in added]
>       assert identities == [("SeedingStore", "get", ("_row",))], identities
E       AssertionError: [('SeedingStore', 'get', ('_row',)), ('ReadingStore', 'get', ('_row',))]
E       assert [('SeedingSto...', ('_row',))] == [('SeedingSto...', ('_row',))]
E         
E         Left contains one more item: ('ReadingStore', 'get', ('_row',))
E         Use -v to get more diff

tests/governance/test_wi113_inventory_qualified_index.py:92: AssertionError
=========================== short test summary info ============================
FAILED tests/governance/test_wi113_inventory_qualified_index.py::test_reader_sharing_a_name_with_a_writer_is_not_a_write_site
1 failed, 3 passed in 0.09s
MUTATION_APPLIED: resolve_callees resolves every call to all bare-name definitions; signature kept
PYTEST_EXIT: 1
RESTORED: True
=== RAW [19] END ===
=== RAW [20] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && rg -n 'تصحيحُ قياسٍ لا حرقٌ|تصحيحُ قياسٍ — لا حرقٌ' docs/audit/measurements/decision_gate_ledger.json docs/audit/COMPLETION_LEDGER.md docs/audit/ACTIVE_EXECUTION_STATE.md
EXIT: 0
BYTES: 4112
SHA256: bf7129b419a3021d50b1f02fcdde5e0245fca4b4a2e8308b8aa5930f85a9c980
NO_EOL: 0
--- OUTPUT ---
docs/audit/measurements/decision_gate_ledger.json:238:   "reason": "تصحيحُ قياسٍ لا حرقٌ (W-669 · WI-113 · التوجيهُ 22 § 2): أداةُ الجردِ تفهرسُ بالاسمِ المؤهَّلِ فتسقطُ 8 مواقعَ مُركَّبةٍ خاطئةِ الهويّةِ في persistent.py ويبقى واحدٌ حقٌّ — الدَّينُ 142 ← 135 والموجةُ W3: 97 ← 90 · المواضعُ 239 ← 232 · لا سطحَ عبرَ الحدَّ ولا يُحتسَبُ في منحنى الحرق (evidence/W-669/d4_after.txt)",
docs/audit/ACTIVE_EXECUTION_STATE.md:32:2026-10-25 (W-670 — دفعةُ الشِّفرةِ الأولى للتوجيهِ 22: حكمُ N+1 لـPR #150 على `7d3d5b6f` (40176135507 · 13/13) مقروءٌ أخضرَ قبلَ الدفعِ السريعِ (W-668) · WI-113 وWI-115 IN_PROGRESS (W-668) · **تصحيحُ قياسٍ لا حرقٌ**: أداةُ الجردِ بالاسمِ المؤهَّلِ — D-4 142 → 135 (W3 97 → 90 · المواقعُ 239 → 232) بفحصٍ وطفرتَين (W-669) · إصلاحُ § 3.5: إعادةُ صرفٍ بمفتاحِ حركةٍ معكوسةٍ تُرفَضُ `EntityStateError` بفحصٍ وطفرة (W-670) — كاشفُ التعشيشِ لم يُبدَأ — المنسِّقُ Claude Opus 5.5)
docs/audit/COMPLETION_LEDGER.md:802:10ثغ-10. 2026-10-25 (W-669 — WI-113 · **تصحيحُ قياسٍ — لا حرقٌ** (التوجيهُ 22 § 2: «سجِّله «تصحيح قياس» تحت عنوان منفصل ولا تحتسبه في منحنى الحرق») · المنسِّقُ Claude Opus 5.5): `synthesize_public_sites` يفهرسُ النداءاتِ بالاسمِ المؤهَّلِ `Class.method` (`qualify` · `resolve_callees`) ويحلُّ `self.x()` إلى صنفِ المُنادي ويُسنِدُ المالكَ الحقَّ. **مقيسٌ** (`evidence/W-669/d4_after.txt` مقابلَ `evidence/W-666/d4_before.txt`): **D-4 = 142 → 135** · مواقعُ الكتابةِ 239 → 232 · W3: 97 → 90 · السياديُّ 46 والمُغلَقُ القديمُ 7 ثابتانِ — والفرقُ بالهويّةِ: −8 `PersistentPromotionStore.get via _row` و+1 `PersistentSystemStateStore.get via _row` (البذرُ الكسولُ الحقُّ) — فالسبعُ التي قاسَها A1 § 1.3 هي الصافي. **هذا الفرقُ قياسٌ صُحِّحَ لا دَينٌ حُرِقَ**: لا سطحَ عبرَ الحدَّ، ولا يُحتسَبُ في منحنى الحرق؛ ولقطةُ `decision_gate_ledger.json` مسجَّلةٌ بنوعِ الأداةِ الوحيدِ `work_drift` وسببُها يقولُ «تصحيحُ قياسٍ لا حرقٌ» نصًّا. **الفحصُ** `tests/governance/test_wi113_inventory_qualified_index.py` (4): قارئٌ يُشاركُ كاتبًا الاسمَ لا يُحسَب · الكاتبُ بمعاونِه يبقى · المُستقبِلُ المجهولُ يبقى بالحدِّ القديمِ · persistent.py يُركِّبُ `get` واحدًا لـ`PersistentSystemStateStore`؛ والطفرتانِ M1 (فهرسةٌ مجرَّدة) وM2 (إسكاتُ المجهول) يكتشفُهما. **ولقطاتُ القياسِ المحروسةُ** (`write_inventory_p13.json` · `decision_wave_map.json` · `final_audit_p14.json`) أُعيدَ توليدُها بأوامرِها المقيَّدةِ (سابقةُ W-531). **ولم يُقَسْ**: `attribute_helper_writes` ما زالَ بالاسمِ المجرَّدِ.
docs/audit/COMPLETION_LEDGER.md:1487:| W-669 | 2026-10-25 | T0 (بندُ [`WI-113`](../governance/work/ACTIVE_WORK.md) · **تصحيحُ قياسٍ لا حرقٌ**) | أداةُ الجردِ بالاسمِ المؤهَّلِ: D-4 142 → 135 قياسًا (W3 97 → 90 · المواقعُ 239 → 232) · فحصٌ (4) وطفرتانِ يكتشفُهما · واللقطاتُ المحروسةُ مُعادةٌ | `attribute_helper_writes` بالاسمِ المؤهَّلِ (لم يُقَسْ) · وIN_REVIEW بجولةِ مجلس | [`evidence/W-669/`](evidence/W-669/README.md) |
=== RAW [20] END ===
VERDICT_PER_CRITERION: (1) نعم — الفهرسةُ في synthesize_public_sites/resolve_callees بالاسمِ المؤهَّلِ Class.method لا بالمجرَّدِ ولا بآخرِ صنفٍ (الفرقُ في [6]؛ المالكُ من عقدةِ qnodes لا من آخرِ صنفٍ يُعرِّفُ الاسم). المسبارُ [17] على المدخلِ الإنتاجيِّ: GET_OWNERS=['WriterFirst'] لا LastReader ولا MiddleReader، والوارثُ ChildReader الذي يعيدُ تعريفَ _row قارئًا ويُنادي self._row لم يُحسَب، وWriterFirst.get بقيَ. حدُّ obj.x() (كلُّ تعريفٍ بالاسمِ حيثُ لا يُعرَفُ المُستقبِلُ) معلَنٌ في resolve_callees ويحرسُه الفحصُ الثالثُ فلا يُخفَّف — لا يُبطِلُ (1): ليسَ دمجَ نداءاتِ self ولا نسبةً إلى آخرِ صنفٍ. attribute_helper_writes لم يُمَسّ ([6] لا يغيّرُه) وما زالَ بالاسمِ المجرَّدِ؛ المسبارُ رصدَ غيابَ OrphanWriter._helper لأنَّ OtherPublic.publish يصلُ بالاسمِ المجرَّدِ إلى كلِّ _helper. هذا لا يُبطِلُ (1) كما كُتِبَ لهذا البندِ: لا يُعيدُ مواقعَ القراءةِ العامّةَ الكاذبةَ ولا ينسبُ المالكَ إلى آخرِ صنفٍ ولا يُسقِطُ الكتابةَ العامّةَ الحقيقيّةَ، وهو سابقٌ للإصلاحِ (الدالّةُ لم تتغيّر) وخارجَ D-4 (الدَّينُ عامٌّ فقط). (2) نعم — [7] EXIT 0: 4 passed، ومنها أنَّ القارئَ المشاركَ للاسمِ لا يُحتسَبُ وأنَّ الكاتبَ بمعاونِه يبقى وأنَّ persistent.py يُركِّبُ get واحدًا لمالكِ PersistentSystemStateStore. [17] على المدخلِ الإنتاجيِّ --service: PERSISTENT_GETS: 1 والمالكُ PersistentSystemStateStore وvia=['_row']، والبذرُ الكسولُ في [12] عندَ السطرِ 932. (3) نعم بسقوطٍ دلاليٍّ أعدتُه أنا لا بسجلِّ المنفِّذِ — [10] (إرجاعُ الأداةِ كلِّها إلى 6605fa88^) EXIT 1 بـAttributeError: '_WriteVisitor' object has no attribute 'qcalls'، فالسقوطُ خطأُ واجهةٍ لا تأكيدٌ، ويؤكِّدُ إفصاحَ المنفِّذِ ولا يُسلِّمُ دعوى M1. [18]/[19] أبقتِ الواجهةَ وأرجعتْ حلَّ النداءاتِ إلى كلِّ تعريفٍ بالاسمِ المجرَّدِ؛ الفحصُ نفسُه سقطَ بتأكيدٍ (AssertionError: ReadingStore.get عادت إلى العدِّ بجانبِ SeedingStore.get) ثمَّ استُعيدَ الملفُّ (RESTORED: True). فالفحصُ يكتشفُ طفرةَ الإرجاعِ الدلاليّةَ. (4) نعم — قبلُ [11] EXIT 0: debt 142 · W3 97 · write_sites_total 239 · git_head 6aacee81؛ بعدُ [8] EXIT 0: debt 135 · W3 90 · write_sites_total 232 · git_head 79abc6a2؛ الفرقُ 7 والسياديُّ 46 والمُغلَقُ 7 ثابتانِ فلا عبورَ حدٍّ. التسجيلُ تحتَ عنوانٍ منفصلٍ لا حرقًا في [20]: COMPLETION_LEDGER.md قيدُ 10ثغ-10 عنوانُه «تصحيحُ قياسٍ — لا حرقٌ» ونصُّه «لا يُحتسَبُ في منحنى الحرق»، ولقطةُ decision_gate_ledger.json سببُها «تصحيحُ قياسٍ لا حرقٌ» والدَّينُ 142 ← 135. [13] على سجلِّ القراراتِ EXIT 1 ومخرجُه فارغٌ — التسجيلُ ليسَ في السجلِّ السياديِّ، ونصُّ المعيارِ لا يشترطُه. استنساخٌ: نعم، بنفسي، gh repo clone vooovg-ui/AMOS-Fedration /home/user/workspace/council_w673/grok_4_7/wi113/repo ثمَّ bash tools/dev/bootstrap.sh داخلَه؛ العقدةُ من [1] و[3].
PROBES: [16] شِفرةُ المسبارِ · [17] تشغيلُه · الخاصيّةُ: نسبةُ كتابةٍ لقارئٍ يشارُكُ الاسمَ أو لآخرِ صنفٍ، أو احتسابُ self._row في وارثٍ أعادَ تعريفَ المعاونِ قارئًا، أو سقوطُ الكتابةِ العامّةِ الحقيقيّةِ (ومنها get الوحيدُ في persistent.py) · انكسرت؟ لا
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم. لم أقرأْ ولم أكتبْ خارجَ جذرِ المقعدِ /home/user/workspace/council_w673/grok_4_7/wi113. الاستنساخُ وشجرةُ old (أنشأَها الأمرُ 10) داخلَه. لم أفتحْ /home/user/workspace/amos ولا أدلّةَ المنفِّذِ docs/audit/evidence/W-66* وW-67* عدا الإحاطةِ المبصومةِ التي قرأَها الأمرانِ 14 و15، وبصمتُها تطابقُ SHA256SUMS وتطابقُ إحاطةَ الجذرِ. داخلَ الاستنساخِ قرأتُ ما سمّتْهُ الأوامرُ وما لزمَ للحكمِ: الأداةُ والفحصُ وdocs/governance/COUNCIL_PROTOCOL.md ولقطةُ القياسِ وسجلُّ الإكمالِ.
VERDICT: PASS لكلِّ المعاييرِ
