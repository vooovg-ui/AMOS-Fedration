# حكمُ مقعدِ المجلسِ — kimi_k3 · جولةُ WI-113 (W-679)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-113 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w673/kimi_k3/wi113) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `b3e813678fb709f12ecb199a4ef3edc9b243806c76a48c3243c7108a6ba971c5`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-113 عندَ العقدةِ `79abc6a2` — إحاطةٌ مبصومةٌ (W-673) ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9) · والفحصُ النهائيُّ للنصابِ معلَّقٌ على شرائطِ § 4.7 (قياسُ عيبَي الفاحصِ في W-679).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-679) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-25

## تاريخ آخر تعديل
2026-10-25

---
MODEL: kimi_k3 (Kimi — Moonshot AI)
FAMILY: Kimi (Moonshot AI)
RUN_DATE: 2026-10-25 23:38 +00:00
NODE: 79abc6a206000e162689d642d1ebc42af36f445a
CLONE_PATH: /home/user/workspace/council_w673/kimi_k3/wi113/repo
CLONE_CMD: git clone https://github.com/vooovg-ui/AMOS-Fedration repo (استنساخٌ كاملٌ في جذر المقعد) — وأُعِدَّتِ البيئةُ بـ tools/dev/bootstrap.sh ثم git checkout للعقدة بالأمرين 1 و2
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/
 2. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/)
 3. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git log --format='%h %cI %s' -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
 5. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git show --stat 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7
 6. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git diff 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7 -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
 7. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
 8. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python tools/audit/decision_gate.py --measure
 9. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 10. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && rm -rf ../old && git worktree add --detach ../old 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ && cp tests/governance/test_wi113_inventory_qualified_index.py ../old/tests/governance/ && cd ../old && /home/user/workspace/council_w673/kimi_k3/wi113/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
 11. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo/../old && /home/user/workspace/council_w673/kimi_k3/wi113/repo/.venv/bin/python tools/audit/decision_gate.py --measure
 12. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && nl -ba federal/executive/services/src/amos_federation/common/persistent.py | sed -n '880,960p'
 13. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && rg -n 'WI-113|A1\(هـ\)|تصحيح قياس' docs/audit/SOVEREIGN_DECISION_REGISTER.md
 14. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && sha256sum docs/audit/evidence/W-673/briefs_wi113/briefing_kimi_k3.md
 15. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && cat docs/audit/evidence/W-673/briefs_wi113/SHA256SUMS
 16. nl -ba /home/user/workspace/council_w673/kimi_k3/wi113/probe/probe_qualified_attribution.py
 17. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python /home/user/workspace/council_w673/kimi_k3/wi113/probe/probe_qualified_attribution.py
 18. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && cp tools/audit/sovereign_write_inventory.py ../probe/sovereign_write_inventory.orig.py && .venv/bin/python ../probe/apply_mutation_m1.py
 19. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
 20. cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git checkout -- tools/audit/sovereign_write_inventory.py && git status --porcelain -- tools/audit/sovereign_write_inventory.py; echo RESTORED
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/)
EXIT: 0
BYTES: 329
SHA256: 820b1154c5055620984fd0bba0e902931b07c236382c0e2d712be5b3ef5bcc27
NO_EOL: 0
--- OUTPUT ---
HEAD is now at 79abc6a2 W-673: WI-113 وWI-115 IN_PROGRESS→IN_REVIEW · ستُّ إحاطاتٍ مبصومةٍ لجولةِ المجلسِ (gemini_3_8_flash · grok_4_7 · kimi_k3) ونصوصُ الإطلاقِ حرفيًّا · WI-115 بنطاقِ § 3.5 وحدَه · لا شِفرةَ — المنسِّقُ Claude Opus 5.5
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git log --format='%h %cI %s' -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git show --stat 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git diff 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7 -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 0
BYTES: 98
SHA256: f87e1ec159e73ceaff96b34a3bc29b017111816d05b56b64e23a829128ce891b
NO_EOL: 0
--- OUTPUT ---
....                                                                     [100%]
4 passed in 0.08s
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python tools/audit/decision_gate.py --measure
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && rm -rf ../old && git worktree add --detach ../old 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ && cp tests/governance/test_wi113_inventory_qualified_index.py ../old/tests/governance/ && cd ../old && /home/user/workspace/council_w673/kimi_k3/wi113/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 1
BYTES: 7670
SHA256: 9b47529c0583eb0b1b61830ca450420b0bfcd60a6204b70f71ba078a57503106
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

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/kimi_k3/wi113/old/tools/audit/sovereign_write_inventory.py'>
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

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/kimi_k3/wi113/old/tools/audit/sovereign_write_inventory.py'>
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

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/kimi_k3/wi113/old/tools/audit/sovereign_write_inventory.py'>
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

tool = <module 'amos_write_inventory_qualified_under_test' from '/home/user/workspace/council_w673/kimi_k3/wi113/old/tools/audit/sovereign_write_inventory.py'>
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo/../old && /home/user/workspace/council_w673/kimi_k3/wi113/repo/.venv/bin/python tools/audit/decision_gate.py --measure
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && nl -ba federal/executive/services/src/amos_federation/common/persistent.py | sed -n '880,960p'
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && rg -n 'WI-113|A1\(هـ\)|تصحيح قياس' docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 1
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && sha256sum docs/audit/evidence/W-673/briefs_wi113/briefing_kimi_k3.md
EXIT: 0
BYTES: 125
SHA256: b04071eb9debf16e9c5f4505639d63cb8088130f7d4f8bf537a418dc6e1f22db
NO_EOL: 0
--- OUTPUT ---
4ca60bb75474edcab8de7a3dc6ac8c30a7174fb9aa23af965671d84af125509f  docs/audit/evidence/W-673/briefs_wi113/briefing_kimi_k3.md
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && cat docs/audit/evidence/W-673/briefs_wi113/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w673/kimi_k3/wi113/probe/probe_qualified_attribution.py
EXIT: 0
BYTES: 7467
SHA256: 8f8dae0616f9c51141ef04446ad2ee71eeddf4123127dbbb5853912bf08564d9
NO_EOL: 0
--- OUTPUT ---
     1	"""مسبارُ مقعدِ kimi_k3 — WI-113 (البروتوكولُ § 4.9): كسرُ خاصيّةِ الفهرسةِ بالاسمِ المؤهَّل.
     2	
     3	ينادي الأداةَ نفسَها (`tools/audit/sovereign_write_inventory.py`: `synthesize_public_sites`)
     4	على أشجارٍ مصطنعةٍ من عندي — لا نسخًا عن فحصِ WI-113 القائم، ويحاولُ كسرَ المُدَّعى:
     5	
     6	أ) تضليلُ النسبةِ: صنفانِ يعرِّفانِ الدالّةَ والمعاونَ بالاسمينِ نفسِهما (`load`/`_store_row`)،
     7	   أحدُهما كاتبٌ والآخرُ قارئٌ — هل تُنسَبُ كتابةٌ للقارئِ أو يُنسَبُ المالكُ لآخرِ مُعرِّف؟
     8	ب) إسقاطُ كاتبٍ حقيقيّ (أخطرُ من بقاءِ قراءةٍ): كاتبُ الوحيدُ في صنفٍ أساسٍ والعموميّةُ
     9	   في وارثٍ تُنادي `self` — هل بقي محسوبًا؟
    10	ج) سلسلةُ معاونَين داخلَ الصنفِ (`apply → self._stage → self._flush` كاتب) — هل تُسقَط؟
    11	د) الطفرةُ دلاليًّا: إرجاعُ الحلِّ بالاسمِ المجرَّدِ (سلوكُ ما قبلَ W-669) — هل تنكسرُ
    12	   دعوى (أ) — أي إنَّ الحرسَ يكشفُ الطفرةَ بالتأكيدِ لا بخطأِ واجهة؟
    13	"""
    14	
    15	from __future__ import annotations
    16	
    17	import ast
    18	import importlib.util
    19	import sys
    20	from pathlib import Path
    21	from types import ModuleType
    22	
    23	REPO = Path("/home/user/workspace/council_w673/kimi_k3/wi113/repo")
    24	TOOL_PATH = REPO / "tools" / "audit" / "sovereign_write_inventory.py"
    25	
    26	
    27	def load_tool() -> ModuleType:
    28	    spec = importlib.util.spec_from_file_location("kimi_k3_probe_inventory", TOOL_PATH)
    29	    assert spec is not None and spec.loader is not None
    30	    module = importlib.util.module_from_spec(spec)
    31	    sys.modules["kimi_k3_probe_inventory"] = module
    32	    spec.loader.exec_module(module)
    33	    return module
    34	
    35	
    36	def synth(tool: ModuleType, source: str) -> list:
    37	    tree = ast.parse(source)
    38	    visitor = tool._WriteVisitor("probe/stores.py", source)
    39	    visitor.visit(tree)
    40	    return tool.synthesize_public_sites(
    41	        visitor.sites, visitor.qcalls, visitor.qnodes, "probe/stores.py", source
    42	    )
    43	
    44	
    45	# أ) كاتبٌ وقارئٌ بالاسمينِ نفسِهما في الدالّةِ والمعاون
    46	CASE_A = '''
    47	class VaultWriter:
    48	    def _store_row(self, session):
    49	        session.add(object())
    50	        session.commit()
    51	
    52	    def load(self, session):
    53	        return self._store_row(session)
    54	
    55	
    56	class CacheReader:
    57	    def _store_row(self, session):
    58	        return session.query(object).first()
    59	
    60	    def load(self, session):
    61	        return self._store_row(session)
    62	'''
    63	
    64	# ب) الكاتبُ في الأساسِ والعموميّةُ في الوارثِ — إسقاطُها إسكاتٌ لكتابةٍ حقيقيّة
    65	CASE_B = '''
    66	class BaseStore:
    67	    def _persist(self, session):
    68	        session.add(object())
    69	        session.commit()
    70	
    71	
    72	class ChildStore(BaseStore):
    73	    def save(self, session):
    74	        return self._persist(session)
    75	'''
    76	
    77	# ج) سلسلةُ معاونَينِ داخلَ الصنفِ نفسِه
    78	CASE_C = '''
    79	class Ledger:
    80	    def _flush(self, session):
    81	        session.add(object())
    82	        session.commit()
    83	
    84	    def _stage(self, session):
    85	        return self._flush(session)
    86	
    87	    def apply(self, session):
    88	        return self._stage(session)
    89	'''
    90	
    91	
    92	def resolve_bare_all(caller, qcalls):
    93	    """طفرةٌ: حلٌّ بالاسمِ المجرَّدِ لكلِّ نداءٍ — سلوكُ ما قبلَ W-669 عمدًا."""
    94	    by_bare: dict[str, set[str]] = {}
    95	    for name in qcalls:
    96	        by_bare.setdefault(name.rsplit(".", 1)[-1], set()).add(name)
    97	    resolved: set[str] = set()
    98	    for _kind, name in qcalls.get(caller, ()):
    99	        resolved.update(by_bare.get(name, ()))
   100	    return resolved
   101	
   102	
   103	def main() -> int:
   104	    tool = load_tool()
   105	    failures: list[str] = []
   106	
   107	    # أ) لا كتابةَ تُنسَبُ للقارئِ ومالكُ الموقعِ الوحيدِ كاتبُه الحقّ
   108	    added_a = synth(tool, CASE_A)
   109	    ids_a = [(s.owner, s.function, s.writes_via) for s in added_a]
   110	    exp_a = [("VaultWriter", "load", ("_store_row",))]
   111	    print(f"[أ] مواقعُ CASE_A المركَّبة: {ids_a}")
   112	    if ids_a != exp_a:
   113	        failures.append(f"أ: توقَّع {exp_a} فوجد {ids_a}")
   114	
   115	    # ب) كاتبٌ حقيقيٌّ وراثيٌّ لا يُسقَط
   116	    ids_b = [(s.owner, s.function, s.writes_via) for s in synth(tool, CASE_B)]
   117	    print(f"[ب] مواقعُ CASE_B المركَّبة: {ids_b}")
   118	    if ("ChildStore", "save", ("_persist",)) not in ids_b:
   119	        failures.append(f"ب: سقط كاتبُ الوارثِ الحقيقيّ — {ids_b}")
   120	
   121	    # ج) سلسلةُ المعاونَينِ لا تُسقِطُ الكاتب
   122	    ids_c = [(s.owner, s.function, s.writes_via) for s in synth(tool, CASE_C)]
   123	    print(f"[ج] مواقعُ CASE_C المركَّبة: {ids_c}")
   124	    if ("Ledger", "apply", ("_flush",)) not in ids_c:
   125	        failures.append(f"ج: سقطت كتابةُ السلسلةِ — {ids_c}")
   126	
   127	    # د) طفرةٌ دلالية: إرجاعُ الحلِّ بالاسمِ المجرَّدِ يكسرُ دعوى (أ)
   128	    original = tool.resolve_callees
   129	    tool.resolve_callees = resolve_bare_all
   130	    try:
   131	        ids_mut = [(s.owner, s.function, s.writes_via) for s in synth(tool, CASE_A)]
   132	    finally:
   133	        tool.resolve_callees = original
   134	    print(f"[د] مواقعُ CASE_A تحتَ الطفرةِ (حلٌّ مجرَّد): {ids_mut}")
   135	    if ids_mut == exp_a:
   136	        failures.append(
   137	            "د: الطفرةُ (فهرسةٌ/حلٌّ بالاسمِ المجرَّد) لم يكشفْها الحرسُ — نفسُ النتيجة"
   138	        )
   139	    elif not any(owner == "CacheReader" for owner, _f, _v in ids_mut):
   140	        failures.append(
   141	            f"د: الطفرةُ غيّرتِ النتيجةَ لكن ليس بدمجِ القارئِ كما قبلَ W-669 — {ids_mut}"
   142	        )
   143	
   144	    if failures:
   145	        print("PROBE FAIL:")
   146	        for f in failures:
   147	            print(f"  - {f}")
   148	        return 1
   149	    print("PROBE PASS: الخاصيّةُ صامدةٌ في الأحوالِ الأربعةِ والطفرةُ مكشوفةٌ دلاليًّا")
   150	    return 0
   151	
   152	
   153	if __name__ == "__main__":
   154	    raise SystemExit(main())
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python /home/user/workspace/council_w673/kimi_k3/wi113/probe/probe_qualified_attribution.py
EXIT: 0
BYTES: 544
SHA256: 9f04ee708ce31b8460d55f95b8425f485cb62eeaf69632769d3a5cef98a46e22
NO_EOL: 0
--- OUTPUT ---
[أ] مواقعُ CASE_A المركَّبة: [('VaultWriter', 'load', ('_store_row',))]
[ب] مواقعُ CASE_B المركَّبة: [('ChildStore', 'save', ('_persist',))]
[ج] مواقعُ CASE_C المركَّبة: [('Ledger', 'apply', ('_flush',))]
[د] مواقعُ CASE_A تحتَ الطفرةِ (حلٌّ مجرَّد): [('VaultWriter', 'load', ('_store_row',)), ('CacheReader', 'load', ('_store_row',))]
PROBE PASS: الخاصيّةُ صامدةٌ في الأحوالِ الأربعةِ والطفرةُ مكشوفةٌ دلاليًّا
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && cp tools/audit/sovereign_write_inventory.py ../probe/sovereign_write_inventory.orig.py && .venv/bin/python ../probe/apply_mutation_m1.py
EXIT: 0
BYTES: 108
SHA256: 673aedab637991118b68382f68c4a2a7644bca8b43e934cf42800114759a0538
NO_EOL: 0
--- OUTPUT ---
M1 applied: نداءاتُ self تُحَلُّ بالاسمِ المجرد (سلوكُ ما قبلَ W-669)
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py
EXIT: 1
BYTES: 1277
SHA256: dc56b7c97cab5e4e43b1b32bafb5f1af6cd21b9bffe6a59cc52c0dd591f82776
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
=== RAW [19] END ===
=== RAW [20] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi113/repo && git checkout -- tools/audit/sovereign_write_inventory.py && git status --porcelain -- tools/audit/sovereign_write_inventory.py; echo RESTORED
EXIT: 0
BYTES: 9
SHA256: d76c795987205b838ac2d149a962ce5506c7a1f6da940d73c5b67a3ad69b2dd8
NO_EOL: 0
--- OUTPUT ---
RESTORED
=== RAW [20] END ===
VERDICT_PER_CRITERION:
 المعيار (1) الفهرسة بالاسم المؤهل ← نعم: الفرق (الكتلة 6) يُدخِل qcalls/qnodes وqualify وresolve_callees ويجعل synthesize_public_sites يركِّب المواقعَ بالمفتاحِ «Class.method» وبمالكِها الحق (owner من _classes لا «آخر صنف يعرِّف الاسم»)؛ والفحص ينجح (الكتلة 7: 4 passed)؛ ومسباري (الكتلة 17) يُثبِت أن قارئًا شارك كاتبًا الاسمَ نفسَه لا يُنسَب إليه شيء ومالك الموقع كاتبه الحق. وحدَّ المنسِّق المعلَن (المستقبِل غير self/cls يُحَلُّ لكل تعريف بالاسم، وattribute_helper_writes لم يُمَسَّ) لا يُبطِل المعيار: هو حدٌّ تحفُّظيٌّ مُعلَنٌ باقٍ كما كان قبل الإصلاح (يقع في فرع else في resolve_callees) ويحرُسُه test_unknown_receiver_keeps_the_declared_conservative_limit — وهو يزيد العدّ ولا يُسقِط كاتبًا، فليس تخفيفَ بوابة.
 المعيار (2) القراءات السبع لا تُحتسَب والكتابة الحقيقية (:932 بذر كسول) تبقى ← نعم: test_persistent_py_has_one_synthesized_get_owned_by_system_state ضمن 4 passed (الكتلة 7) يُثبِت أن المواقع الثمانية كاذبة الهوية صارت موقعًا واحدًا (PersistentSystemStateStore.get عبر _row)؛ وD-4 قِستُه بنفسي 142 قبل (الكتلة 11 على شجرة 6605fa88^) و135 بعد (الكتلة 8) — فرقٌ = 7 بعينها؛ وwrite_sites_total نزل 239→232؛ والكتلة 12 تُرِي أن get عند :932 ينادي self._row و_row يفعل session.add+session.commit (الكتابة الحقيقية)، و الجردُ ما زال يحتسب 13 موقعًا في persistent.py (الكتلة 9)؛ ومسباري ب/ج (الكتلة 17) يُثبِت عدم إسقاط كاتب حقيقي وراثي ولا كاتب سلسلة معاونَين.
 المعيار (3) طفرة إرجاع الفهرسة بالاسم المجرد يكتشفها الفحص ← نعم (بإثباتٍ دلاليّ من يدي لا تسليمًا): الأمر 10 (الكتلة 10) سقطت فيه فحوص WI-113 على الأداة القديمة بخطأ واجهة AttributeError ('_WriteVisitor' has no attribute 'qcalls') لا بتأكيد — كما أفصح المنفذ — فلم أقبله وحده؛ فأعدتُ الطفرة بنفسي على الأداة الحاضرة (M1: قلبُ فرعِ الحلِّ المؤهَّلِ لنداءات self في resolve_callees — الكتلتان 18 وتطبيقها) وشغَّلتُ الفحصَ نفسَه فسقط بدلالة AssertionError دلالية: ظهر ('ReadingStore','get',('_row',)) زائدًا (الكتلة 19: 1 failed 3 passed) ثم استُعيد الملف (الكتلة 20). ومسباري المستقل (د) يكشف الطفرةَ نفسَها: تحت الحل المجرَّد ظهر CacheReader.load كموقع كتابة (الكتلة 17). ملاحظة غير حاجبة: الطفرة M1 يكشفها من الفحص اختبارٌ واحدٌ (test_reader...) والثلاثة الباقية صمدت تحتها — تغطيةٌ كافية للمعيار كما كُتِب.
 المعيار (4) D-4 قبل وبعد خامًا بأمر والفرق يُسجَّل «تصحيح قياس» تحت عنوان منفصل لا حرقًا ← نعم: القياسان خامان بأمرين — 142 (الكتلة 11) و135 (الكتلة 8)؛ والتسجيل تحت العنوان المنفصل «تصحيحُ قياسٍ لا حرقٌ: D-4 142→135 (W3 97→90)» في رسالة التزام الشفرة 6605fa88 نفسِها (الكتلة 5) وفي صف البند وكتلته T0 «تصحيح قياس لا حرق». ملاحظةٌ غيرُ حاجبة: الأمر 13 (الكتلة 13، EXIT 1) لا يجِد WI-113 في SOVEREIGN_DECISION_REGISTER.md عند هذه العقدة — وصف البند يقول «— (يُكتب عند الإغلاق)» فالتسجيل في السجل يأتي عند الإغلاق بعد نصاب المجلس، فليس نقصًا في إثبات «تصحيح القياس» الآن، وأُثبِتُه ليعلم به المنسق عند الإغلاق.
PROBES: مسبار واحد من عندي — probe/probe_qualified_attribution.py: كتلة الشفرة [16] (nl -ba) وكتلة التشغيل [17] (EXIT 0) ؛ حاول كسر: (أ) نسبة كتابة لقارئ يشارك كاتبًا الاسمَ في الدالة والمعاون معًا — صمدت (VaultWriter.load وحده) · (ب) إسقاط كاتب حقيقي معرَّف في صنف أساس يُنادى self من وارث — صمدت (ChildStore.save محسوب) · (ج) إسقاط كاتب عبر سلسلة معاونَين داخل الصنف — صمدت (Ledger.apply عبر _flush) · (د) طفرة الحل بالاسم المجرد — انكسرت الدعوى تحتها كما يجب (ظهر CacheReader.load) أي الطفرة مكشوفة دلاليًّا. انكسرت الخاصية؟ لا. وإضافةً لذلك طفرة M1 على ملف الأداة نفسه مع الفحص القائم: كتلتا التطبيق [18] والتشغيل [19] (سقوط دلالي 1 failed) والاستعادة [20].
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً (ملاحظتان غير حاجبتين: سقوطُ الأمرِ 10 بخطأ واجهة لا بتأكيد — وقد أثبتُّ الكشفَ الدلاليَّ بنفسي في [19] و[17]؛ وغيابُ قيدِ WI-113 عن سجل القرارات عند العقدة وهو موكولٌ للإغلاق بنص الصف)
ISOLATION_DECLARATION: أقرُّ أني لم أقرأ ولم أكتب خارج جذري /home/user/workspace/council_w673/kimi_k3/wi113 ومستنسخَه وشجرةَ العملِ ../old التي أنشأتُها داخله بالأمر 10: نعم — لم أقرأ نسخة المنسق ولا أدلة المنفذ (evidence/W-66*/W-67* غير المبصومة لي) ولا عملَ مقعدٍ آخر؛ وقرأتُ فقط الإحاطةَ والعقدةَ وما تسمّيه أوامر (ج) في استنساخي (بما فيه صف البند وكتلته في ACTIVE_WORK.md للمطابقة، وأداة الفاحص tools/governance/council_verdict_raw_check.py التي أمرتني الإحاطة بتشغيلها) — بلا استثناء آخر.
VERDICT: PASS — المعايير الأربعة كلها تحققت في تشغيلي أنا: (1) فهرسة مؤهلة بالمالك الحق، (2) سقوط القراءات السبع وبقاء البذر الكسول :932 محسوبًا، (3) طفرة الفهرسة المجردة مكشوفة دلاليًّا بإثباتي لا تسليمًا، (4) D-4 142→135 مقيسان خامًا ومسجَّلان «تصحيح قياس» لا حرقًا.
