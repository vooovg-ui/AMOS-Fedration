# حكمُ مقعدِ المجلسِ — kimi_k3 · جولةُ WI-115 (W-710)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في الجولةِ الواحدةِ (قرارُ المالكِ D27) على WI-115 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w701/kimi_k3/wi115) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `61ef1f10338c0f954b8721afd778b4f6a0d796c7560c19841e3715faa3235112`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-115 عندَ العقدةِ `147a0c6b1357ddf0a93ba1c4d16e82e8648cb247` — إحاطةٌ مبصومةٌ (W-701) ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9) · ومخرجاتُ الفاحصِ منَ المنسِّقِ مقروءةٌ مقبولةً EXIT 0 (raw_check_outputs.txt في قيدِ W-710). الكاشفُ المنفَّذُ وحده (Q-9 · النطاقُ المعلَنُ — المعيارُ (3) وشقُّ الكاشفِ من (5)).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-710) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-28

## تاريخ آخر تعديل
2026-10-28 (W-710 — القيدُ نفسُه)

## المحتويات
`VERDICT.md` — نصُّ الحكمِ حرفيًّا.

---
MODEL: Kimi K3
FAMILY: Moonshot AI (Kimi)
RUN_DATE: 2026-10-28 06:55 +00:00
NODE: 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
CLONE_PATH: /home/user/workspace/council_w701/kimi_k3/wi115/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/
 2. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/)
 3. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git log --format='%h %cI %s' -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
 5. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git show --stat 2b814b34
 6. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git diff 2b814b34^ 2b814b34 -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py
 7. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
 8. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
 9. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && rg -n "NESTED_SOVEREIGN_EXEMPTIONS|NestedSovereignCallError|open_case" core/sovereignty/enforcement_boundary.py
 10. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && rm -rf ../old && git worktree add --detach ../old 2b814b34^ && cp tests/sovereignty/test_wi115_nesting_detector.py ../old/tests/sovereignty/ && cd ../old && /home/user/workspace/council_w701/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
 11. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && sha256sum docs/audit/evidence/W-701/briefs_wi115/briefing_kimi_k3.md
 12. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && cat docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS
 13. nl -ba /home/user/workspace/council_w701/kimi_k3/wi115/probe/probe_kimi_k3_nesting.py
 14. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && PYTHONPATH=/home/user/workspace/council_w701/kimi_k3/wi115/repo .venv/bin/python /home/user/workspace/council_w701/kimi_k3/wi115/probe/probe_kimi_k3_nesting.py
 15. cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && rm -rf ../mutant && git worktree add --detach ../mutant 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247 && sed -i "s/if outer_crossing is not None and/if False and outer_crossing is not None and/" ../mutant/core/sovereignty/enforcement_boundary.py && cd ../mutant && /home/user/workspace/council_w701/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/)
EXIT: 0
BYTES: 1025
SHA256: 2cc661a1add06f3fab16140029ff6f753ea8cffd16df1fa15f04397d19e82a87
NO_EOL: 0
--- OUTPUT ---
HEAD is now at 147a0c6b W-701: توجيهُ المستشارِ 25 — قراراتُ المالكِ D27 بنصّها (إغلاقُ WI-113/WI-117/WI-119 بعدَ VERIFIED بإجماعٍ دونَ سؤالٍ جديدٍ · الجولةُ الآنَ لا بعدَ G1 — جولةٌ واحدةٌ بثلاثةِ نطاقاتٍ تُجمَعُ في الجلسةِ نفسِها Q-72) + واجبُ N+1 لـPR #168 (قراءةُ التشغيلِ 40478049851 بالفاحصِ فعلًا: مقروءٌ أخضرُ 13/13 على 129bed06 · EXIT 0) + انتقالٌ واحدٌ: WI-119 IN_PROGRESS→IN_REVIEW + إحاطاتُ الجولةِ التسعُ مبصومةً (3 مقاعدٍ × WI-117/WI-119/الكاشفُ من WI-115 · gemini · grok · kimi) ونصوصُ الإطلاقِ حرفيًّا وقياساتُ الجلسةِ خامًا (حوكمةُ الأعمالِ ✓ · راتشيتٌ 61 · حزمةُ الحوكمةِ 1394 خضراءَ) · لا شِّفرةَ سلوكيّةً · المنسِّقُ GLM-5.3 (Perplexity Computer)
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git log --format='%h %cI %s' -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
EXIT: 0
BYTES: 2549
SHA256: 1d22d1badaa14b88295b92b6cc2a02e7bd63ea4fbc5d3e10475c4b3a6b6204c8
NO_EOL: 0
--- OUTPUT ---
d9603291 2026-10-26T06:57:24Z W-686: تصحيحٌ مؤرَّخٌ لحمرةِ lint في CI على رأسِ PR #159 (تشغيلٌ 40281491512 · بوّابةُ lint وحْدَها · سابقةُ W-676): علاماتُ noqa: E402 لاستيرادَي core وفقَ عُرفِ الشجرةِ + اسمٌ لاتينيٌّ للمسبارِ (N802) + تنظيمُ استيراداتٍ وتنسيقٌ · القياسُ بعدَ: تسلسلُ lint كاملًا أخضرُ محليًّا بترتيبِ CI نفسِهِ · لا انتقالَ حالةٍ · المنسِّقُ GLM-5.3 (Perplexity Computer)
2b814b34 2026-10-26T06:41:42Z W-685: تنفيذُ كاشفِ التعشيشِ لِـ WI-115 (المعيارُ (3) وشقُّ الكاشفِ من (5)): استثناءُ التعشيشِ بأزواجٍ مُجمَّدةٍ + NestedSovereignCallError يُرمى قبلَ أيِّ حارسٍ + استعادةٌ بالرمزِ عبرَ try/finally · 7 فحوصٍ جذريةٍ + مسبارٌ دائمٌ لقياسِ § 4 (المعوِّضُ داخلَ الإطارِ) · 3 طفراتٍ مقتولةٍ · المعيارُ (4) مؤجَّلٌ بتعارضٍ مقيسٍ معَ حرسِ Q-32 — عرضٌ على المالكِ · المنسِّقُ GLM-5.3 (Perplexity Computer)
93434790 2026-10-25T08:45:43Z W-670: WI-115 — إصلاحُ § 3.5: إعادةُ صرفٍ بمفتاحِ حركةٍ معكوسةٍ تُرفَضُ (EntityStateError) · فحصانِ وطفرةٌ · وثائقُ الحالةِ وأرقامُ الحزمِ (2727 · 1525+53) — المنسِّقُ Claude Opus 5.5
968e5ba4 2026-10-22T05:38:45Z W-603: وصل التعويض الآلي في الحد (core/sovereignty/enforcement_boundary.py وحده · قرار المالك Q-70 · ملحق التصميم § 7) — تتبع الأثر · لف run_once ⇒ CompensationGuard.compensate بمفتاح الحلقة ثم CompensationRequired · FAILED_RETRYABLE/FAILED_FINAL · T6p/T8/T9/T10 · الطفرات M5–M8 كل أسقط فحصه · مسبار W-601 بعد الوصل: المعوض 1 في السطحين · DISC-129 · D-4 181←181 · نص المسبار الإلزامي في COUNCIL_PROTOCOL § 4.9 والقالب (التوجيه 18 § 3)
6ad36aed 2026-08-19T08:43:18Z fix(P22): قصرُ مسحِ الحرسِ الساكنِ على ما يُعلِنُه المشروعُ لا على مبنيّاتِ المفسِّرِ
0a5bc77b 2026-08-18T08:52:52Z 1M: حدُّ التنفيذِ السياديُّ والحرسُ الساكن — فرضُ 1E–1K على مسارِ التنفيذ
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git show --stat 2b814b34
EXIT: 0
BYTES: 2007
SHA256: 9cdf1572424eacdd6528c5c3958a4544784ab3ff5a494b2af73f106cd233509d
NO_EOL: 0
--- OUTPUT ---
commit 2b814b340b4ed36af4d8353073d84ebb81d85587
Author: vooovg-ui <326082239+vooovg-ui@users.noreply.github.com>
Date:   Mon Oct 26 06:41:42 2026 +0000

    W-685: تنفيذُ كاشفِ التعشيشِ لِـ WI-115 (المعيارُ (3) وشقُّ الكاشفِ من (5)): استثناءُ التعشيشِ بأزواجٍ مُجمَّدةٍ + NestedSovereignCallError يُرمى قبلَ أيِّ حارسٍ + استعادةٌ بالرمزِ عبرَ try/finally · 7 فحوصٍ جذريةٍ + مسبارٌ دائمٌ لقياسِ § 4 (المعوِّضُ داخلَ الإطارِ) · 3 طفراتٍ مقتولةٍ · المعيارُ (4) مؤجَّلٌ بتعارضٍ مقيسٍ معَ حرسِ Q-32 — عرضٌ على المالكِ · المنسِّقُ GLM-5.3 (Perplexity Computer)

 PROJECT_STATE.md                                   |   3 +-
 core/sovereignty/enforcement_boundary.py           | 275 ++++++-----
 docs/PROJECT_HANDBOOK.md                           |  10 +-
 docs/audit/ACTIVE_EXECUTION_STATE.md               |   1 +
 docs/audit/COMPLETION_LEDGER.md                    |   3 +
 docs/audit/evidence/W-685/README.md                | 105 ++++
 docs/audit/evidence/W-685/before_measurements.txt  |  25 +
 docs/audit/evidence/W-685/mutations/README.md      |  46 ++
 .../W-685/mutations/after_restore_output.txt       |   3 +
 .../W-685/mutations/m1_delete_check_exit.txt       |   1 +
 .../W-685/mutations/m1_delete_check_output.txt     | 239 +++++++++
 .../W-685/mutations/m2_single_name_exit.txt        |   1 +
 .../W-685/mutations/m2_single_name_output.txt      | 239 +++++++++
 .../W-685/mutations/m3_delete_finally_exit.txt     |   1 +
 .../W-685/mutations/m3_delete_finally_output.txt   | 532 +++++++++++++++++++++
 docs/governance/work/ACTIVE_WORK.md                |  10 +-
 .../tests/test_wi115_nesting_compensator_frame.py  | 237 +++++++++
 tests/sovereignty/test_wi115_nesting_detector.py   | 406 ++++++++++++++++
 18 files changed, 2016 insertions(+), 121 deletions(-)
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && git diff 2b814b34^ 2b814b34 -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py
EXIT: 0
BYTES: 40510
SHA256: 3ade40435f5ff4a719680b9f930e7c25f8c42078b595583f2cda03db48f0e81f
NO_EOL: 0
--- OUTPUT ---
diff --git a/core/sovereignty/enforcement_boundary.py b/core/sovereignty/enforcement_boundary.py
index 5ac88c27..987d67c3 100644
--- a/core/sovereignty/enforcement_boundary.py
+++ b/core/sovereignty/enforcement_boundary.py
@@ -62,6 +62,7 @@
 from __future__ import annotations
 
 import ast
+import contextvars
 from collections.abc import Callable, Iterable, Mapping, Sequence
 from dataclasses import dataclass, field
 from enum import Enum
@@ -112,6 +113,34 @@ from core.sovereignty.outbox import (
     enqueue_write_ahead,
 )
 
+# ─────────────────────────────────────────────────────────────────────────────
+# كاشفُ التعشيشِ عندَ الحدِّ (WI-115 · Q-9 الخيارُ 4 · سندُه التوجيهُ 22 § 1)
+#
+# النصُّ المقيسُ (W-665 § 1): التعشيشُ القائمُ الوحيدُ اليومَ هو `open_case` —
+# يعبرُ بـ`gov.case.open` ومُطبِّقُهُ يُنادي `task.submit` داخلَه، ومعوِّضُهُ
+# `task.cancel`. وكلُّ ما عدا ذلكَ عبورٌ داخلَ عبورٍ نشطٍ يُرفَضُ قبلَ أيِّ حارسٍ
+# وأيِّ إذنٍ وأيِّ قيدٍ في الدفترِ. والاستثناءُ **أزواجٌ (خارجيٌّ، داخليٌّ)**
+# لا أسماءٌ مفردة، فلا يصيرُ `open_case` بابًا لأيِّ عبورٍ داخلَه — وهو
+# مُجمَّدٌ في الوحدةِ نفسِها ويُعلَّلُ عندَه، فلا يُوسَّعُ بيدِ منفِّذٍ.
+# ─────────────────────────────────────────────────────────────────────────────
+
+#: الاستثناءُ المسجَّلُ باسمِه (Q-9): أزواجُ (فعلٌ خارجيٌّ، فعلٌ داخليٌّ).
+NESTED_SOVEREIGN_EXEMPTIONS: Final[frozenset[tuple[str, str]]] = frozenset(
+    {
+        ("gov.case.open", "task.submit"),
+        ("gov.case.open", "task.cancel"),
+    }
+)
+
+#: إطارُ العبورِ النشطِ `(action, target)` — واحدٌ لكلِّ سياقِ تنفيذٍ.
+#: على مستوى الوحدةِ عمدًا كي يشملَ الكشفُ العبورَ عبرَ نسختَينِ مختلفتَينِ
+#: منَ الحدِّ في السياقِ نفسِه. ولا يُدَّعى انتقالُهُ عبرَ الخيوطِ (غيرُ مقيسٍ —
+#: W-665 § 4).
+_active_crossing: contextvars.ContextVar[tuple[str, str] | None] = (
+    contextvars.ContextVar("amos_sovereign_active_crossing", default=None)
+)
+
+
 # ─────────────────────────────────────────────────────────────────────────────
 # الأخطاء — كلُّها رفضٌ صريحٌ يُرفَع، ولا رايةَ منطقيّةً ولا ابتلاع
 # ─────────────────────────────────────────────────────────────────────────────
@@ -154,6 +183,15 @@ class StaticGuardError(EnforcementBoundaryError):
     """خللٌ في تشغيلِ الحرسِ الساكنِ نفسِه — لا في المشروعِ المفحوص."""
 
 
+class NestedSovereignCallError(EnforcementBoundaryError):
+    """عبورٌ سياديٌّ داخلَ عبورٍ نشطٍ (WI-115 · Q-9) — رفضٌ صريحٌ لا إذنَ معه.
+
+    يُرفَعُ قبلَ أيِّ حارسٍ وأيِّ `decide` وأيِّ قيدٍ في دفترِ الذرّيّة، فلا
+    يبقى للرفضِ أثرٌ ولا حجزٌ ولا أثرٌ مُطبَّق. والزوجُ المسجَّلُ الوحيدُ
+    المُعفاةُ أزواجُهُ في `NESTED_SOVEREIGN_EXEMPTIONS` (open_case باسمِه).
+    """
+
+
 # ─────────────────────────────────────────────────────────────────────────────
 # مراحلُ الحرسِ — مُعلَنةٌ ومُرتَّبة، ويُسجَّلُ ما جرى منها فعلًا
 # ─────────────────────────────────────────────────────────────────────────────
@@ -332,124 +370,141 @@ class SovereignExecutionBoundary:
         وترتيبُ الرفعِ مقصود: كلُّ فحصٍ يفشلُ يرفعُ استثناءَ مرحلتِه، ولا يُلتقَطُ
         هنا استثناءُ حرسٍ قطُّ — الابتلاعُ هو التجاوزُ بعينِه.
         """
-        stages: list[BoundaryStage] = []
-
-        # ① 1G — الاختصاص: ما لا يملكُه الفاعلُ لا يُتعاقَدُ عليه
-        stages.extend(self._guard_jurisdiction(request, declared_effects, judicial_action))
-
-        # ② 1E — العقد: آثارٌ مُعلَنةٌ محصورةٌ في الهدف
-        contract = self._guard_contract(request, declared_effects)
-        stages.append(BoundaryStage.CONTRACT)
-
-        # ③ 1I — خطّةُ التعويض: ربطٌ قبلَ التنفيذ، لا استعادةً بعدَه
-        plan, external_effects = self._guard_compensation(contract, compensators)
-        if plan is not None:
-            stages.append(BoundaryStage.COMPENSATION_PLAN)
-
-        # ④ 1K — تهيئةُ الصادرِ تُفحَصُ قبلَ أيِّ إذنٍ أو حجزٍ أو تطبيق
-        if external_effects:
-            self._guard_outbox_configured(external_effects, provider, payload_of)
-
-        # ⑤ 1H — المفتاح: يُفحَصُ قبلَ إصدارِ الإذنِ فلا يُصدَرُ إذنٌ بلا حجز
-        self._guard_operation_key(operation_key)
-
-        # ⑥ 1D + 1F + 1J — السلطةُ والإذنُ والإغلاق: عبرَ البوابةِ نفسِها
-        permit = self.gateway.decide(request, declared_effects=declared_effects)
-        stages.extend(
-            (
-                BoundaryStage.IDENTITY_AUTHORITY,
-                BoundaryStage.FAIL_CLOSED,
-                BoundaryStage.PERMIT,
+        # ⓪ كاشفُ التعشيشِ (WI-115 · Q-9): قبلَ أيِّ حارسٍ وأيِّ decide وأيِّ قيدٍ —
+        # فلا إذنَ ولا حجزَ ولا أثرَ للرفضِ. وعندَ الرفضِ لا يُضبَطُ السياقُ ولا
+        # يُمحى: إطارُ الأبِ يبقى قائمًا.
+        outer_crossing = _active_crossing.get()
+        if outer_crossing is not None and (outer_crossing[0], request.action) not in NESTED_SOVEREIGN_EXEMPTIONS:
+            raise NestedSovereignCallError(
+                f"عبورٌ سياديٌّ داخلَ عبورٍ نشطٍ: الفعلُ '{request.action}' داخلَ إطارِ "
+                f"'{outer_crossing[0]}' — التعشيشُ السياديُّ ممنوعٌ (WI-115 · Q-9) "
+                "والزوجُ ليسَ منَ الاستثناءِ المسجَّلِ (open_case باسمِه وحدَه)."
             )
-        )
 
-        # ⑦ 1H — الذرّيّةُ تلفُّ التطبيق
-        enqueued: list[str] = []
-        applied_holder: list[tuple[SovereignEffect, ...]] = []
-        # [W-603 · Q-70] ما طبّقه مُطبِّقُ المُنادي **وعادَ** بنجاحٍ — بترتيبِ التطبيق.
-        applied_internal: list[str] = []
-        routed = self._route_effect(
-            permit=permit,
-            operation_key=operation_key,
-            applier=applier,
-            provider=provider,
-            payload_of=payload_of,
-            correlation_id=correlation_id,
-            enqueued=enqueued,
-        )
+        token = _active_crossing.set((request.action, request.target))
+        try:
+            stages: list[BoundaryStage] = []
+
+            # ① 1G — الاختصاص: ما لا يملكُه الفاعلُ لا يُتعاقَدُ عليه
+            stages.extend(self._guard_jurisdiction(request, declared_effects, judicial_action))
+
+            # ② 1E — العقد: آثارٌ مُعلَنةٌ محصورةٌ في الهدف
+            contract = self._guard_contract(request, declared_effects)
+            stages.append(BoundaryStage.CONTRACT)
+
+            # ③ 1I — خطّةُ التعويض: ربطٌ قبلَ التنفيذ، لا استعادةً بعدَه
+            plan, external_effects = self._guard_compensation(contract, compensators)
+            if plan is not None:
+                stages.append(BoundaryStage.COMPENSATION_PLAN)
+
+            # ④ 1K — تهيئةُ الصادرِ تُفحَصُ قبلَ أيِّ إذنٍ أو حجزٍ أو تطبيق
+            if external_effects:
+                self._guard_outbox_configured(external_effects, provider, payload_of)
+
+            # ⑤ 1H — المفتاح: يُفحَصُ قبلَ إصدارِ الإذنِ فلا يُصدَرُ إذنٌ بلا حجز
+            self._guard_operation_key(operation_key)
+
+            # ⑥ 1D + 1F + 1J — السلطةُ والإذنُ والإغلاق: عبرَ البوابةِ نفسِها
+            permit = self.gateway.decide(request, declared_effects=declared_effects)
+            stages.extend(
+                (
+                    BoundaryStage.IDENTITY_AUTHORITY,
+                    BoundaryStage.FAIL_CLOSED,
+                    BoundaryStage.PERMIT,
+                )
+            )
 
-        def _tracked(effect: SovereignEffect) -> None:
-            routed(effect)
-            if (
-                plan is not None
-                and effect.kind is not EffectKind.EXTERNAL
-                and plan.covers(effect.signature)
-            ):
-                applied_internal.append(effect.signature)
-
-        def _under_permit() -> tuple[str, ...]:
-            """ما يُرجَعُ للحارسِ بصماتٌ نصّيّةٌ لا كائنات.
-
-            سجلُّ 1H يُثبِّتُ بصمةَ النتيجةِ بـ`json`، والكائنُ غيرُ القابلِ
-            للتمثيلِ يُفشِلُ التثبيت. والبصماتُ هي ما يُقارَنُ عندَ الإعادةِ
-            أصلًا، فلا يُفقَدُ شيءٌ بإرجاعِها.
-            """
-            produced = self.policy_enforcement_point.enforce(
-                permit,
-                planner=planner,
-                applier=_tracked,
+            # ⑦ 1H — الذرّيّةُ تلفُّ التطبيق
+            enqueued: list[str] = []
+            applied_holder: list[tuple[SovereignEffect, ...]] = []
+            # [W-603 · Q-70] ما طبّقه مُطبِّقُ المُنادي **وعادَ** بنجاحٍ — بترتيبِ التطبيق.
+            applied_internal: list[str] = []
+            routed = self._route_effect(
+                permit=permit,
+                operation_key=operation_key,
+                applier=applier,
+                provider=provider,
+                payload_of=payload_of,
+                correlation_id=correlation_id,
+                enqueued=enqueued,
             )
-            applied_holder.append(produced)
-            return tuple(e.signature for e in produced)
 
-        fingerprint = compute_fingerprint(
-            scope=operation_key.scope,
-            action=request.action,
-            target=request.target,
-            effect_signatures=tuple(sorted(contract.declared_signatures)),
-            actor=request.actor,
-        )
-        external_prefix = EffectKind.EXTERNAL.value + ":"
-        try:
-            result: OperationResult[tuple[str, ...]] = IdempotencyGuard(
-                ledger=self.idempotency_ledger
-            ).run_once(
-                key=operation_key,
-                fingerprint=fingerprint,
-                execute=_under_permit,
-                extract_effect_signatures=lambda sigs: tuple(sigs or ()),
-                detect_external=lambda sigs: any(
-                    s.startswith(external_prefix) for s in (sigs or ())
-                ),
+            def _tracked(effect: SovereignEffect) -> None:
+                routed(effect)
+                if (
+                    plan is not None
+                    and effect.kind is not EffectKind.EXTERNAL
+                    and plan.covers(effect.signature)
+                ):
+                    applied_internal.append(effect.signature)
+
+            def _under_permit() -> tuple[str, ...]:
+                """ما يُرجَعُ للحارسِ بصماتٌ نصّيّةٌ لا كائنات.
+
+                سجلُّ 1H يُثبِّتُ بصمةَ النتيجةِ بـ`json`، والكائنُ غيرُ القابلِ
+                للتمثيلِ يُفشِلُ التثبيت. والبصماتُ هي ما يُقارَنُ عندَ الإعادةِ
+                أصلًا، فلا يُفقَدُ شيءٌ بإرجاعِها.
+                """
+                produced = self.policy_enforcement_point.enforce(
+                    permit,
+                    planner=planner,
+                    applier=_tracked,
+                )
+                applied_holder.append(produced)
+                return tuple(e.signature for e in produced)
+
+            fingerprint = compute_fingerprint(
+                scope=operation_key.scope,
+                action=request.action,
+                target=request.target,
+                effect_signatures=tuple(sorted(contract.declared_signatures)),
+                actor=request.actor,
             )
-        except Exception as exc:
-            if plan is None or not applied_internal:
-                # لا أثرَ طُبِّقَ: الاستثناءُ يُرفَعُ كما هو (لا لفَّ ولا تغييرَ نوعٍ).
-                raise
-            self._compensate_applied(
-                exc,
+            external_prefix = EffectKind.EXTERNAL.value + ":"
+            try:
+                result: OperationResult[tuple[str, ...]] = IdempotencyGuard(
+                    ledger=self.idempotency_ledger
+                ).run_once(
+                    key=operation_key,
+                    fingerprint=fingerprint,
+                    execute=_under_permit,
+                    extract_effect_signatures=lambda sigs: tuple(sigs or ()),
+                    detect_external=lambda sigs: any(
+                        s.startswith(external_prefix) for s in (sigs or ())
+                    ),
+                )
+            except Exception as exc:
+                if plan is None or not applied_internal:
+                    # لا أثرَ طُبِّقَ: الاستثناءُ يُرفَعُ كما هو (لا لفَّ ولا تغييرَ نوعٍ).
+                    raise
+                self._compensate_applied(
+                    exc,
+                    contract=contract,
+                    plan=plan,
+                    operation_key=operation_key,
+                    applied=tuple(applied_internal),
+                )
+                raise  # pragma: no cover — `_compensate_applied` يرفعُ دائمًا
+            stages.append(BoundaryStage.IDEMPOTENCY)
+            if enqueued:
+                stages.append(BoundaryStage.EXTERNAL_OUTBOX)
+
+            applied = applied_holder[0] if applied_holder else ()
+            self._executions += 1
+            return BoundaryOutcome(
                 contract=contract,
-                plan=plan,
-                operation_key=operation_key,
-                applied=tuple(applied_internal),
+                permit_id=permit.permit_id,
+                operation_key=operation_key.composite,
+                applied_effects=tuple(applied),
+                enqueued_effect_ids=tuple(enqueued),
+                stages=tuple(stages),
+                is_replay=result.is_replay,
+                compensation_plan=plan,
             )
-            raise  # pragma: no cover — `_compensate_applied` يرفعُ دائمًا
-        stages.append(BoundaryStage.IDEMPOTENCY)
-        if enqueued:
-            stages.append(BoundaryStage.EXTERNAL_OUTBOX)
-
-        applied = applied_holder[0] if applied_holder else ()
-        self._executions += 1
-        return BoundaryOutcome(
-            contract=contract,
-            permit_id=permit.permit_id,
-            operation_key=operation_key.composite,
-            applied_effects=tuple(applied),
-            enqueued_effect_ids=tuple(enqueued),
-            stages=tuple(stages),
-            is_replay=result.is_replay,
-            compensation_plan=plan,
-        )
+        finally:
+            # الاستعادةُ بالرمزِ لا الضبطُ إلى None: قد يكونُ لنا أبٌ خارجيٌّ أعلنَ
+            # إطارَهُ — فالضبطُ إلى None كانَ سيمحو إطارَ الأبِ بعدَ عودةِ عبورٍ مستثنًى.
+            _active_crossing.reset(token)
 
     # ── التعويضُ الآليُّ بعدَ الالتزام (W-603 · Q-70) ─────────────────────────
     def _compensate_applied(
diff --git a/tests/sovereignty/test_wi115_nesting_detector.py b/tests/sovereignty/test_wi115_nesting_detector.py
new file mode 100644
index 00000000..607dc00c
--- /dev/null
+++ b/tests/sovereignty/test_wi115_nesting_detector.py
@@ -0,0 +1,406 @@
+"""الهدف: قياسُ كاشفِ التعشيشِ عندَ الحدِّ السياديّ (WI-115 · Q-9 الخيارُ 4).
+
+النطاق: `core/sovereignty/enforcement_boundary.py` — كاشفُ العبورِ داخلَ
+العبورِ، لا القواعدِ الدستوريةَ ولا التطبيقِ. سندُ التصميمِ: وثيقةُ
+`docs/audit/Q9_NESTING_DETECTOR_DESIGN.md` (W-665 · المالكُ أمرَ بالخيارِ 4).
+
+الدعوى المُقاسة: عبورٌ سياديٌّ داخلَ عبورٍ نشطٍ **يُرفَضُ قبلَ أيِّ حارسٍ وأيِّ
+`decide` وأيِّ قيدٍ في دفترِ الذرّيّة** — فلا إذنَ ولا حجزَ ولا أثرَ للرفضِ.
+والاستثناءُ المسجَّلُ الوحيدُ أزواجٌ (خارجيٌّ، داخليٌّ) باسمِ `open_case`
+وحْده (`gov.case.open` → `task.submit` و`task.cancel`)، لا أسماءٌ مفردة،
+فلا يصيرُ `open_case` بابًا لأيِّ عبورٍ آخرَ داخلَه.
+
+والقاعدةُ 12 تمنعُ اعتبارَ وجودِ الملفِّ دليلًا: فالمنعُ يُثبَتُ هنا بأنّ
+`decide` لم يُستدعَ للداخلِ وبأنَّ الدفترَ لا يحملُ مفتاحَه وبأنَّ الحالةَ
+لم تتغيّر، لا بأنَّ استثناءً ارتفعَ فحسب.
+
+سجلُّ التحولات: فشلُ الفحصِ قبلَ الإصلاحِ ثمَّ نجاحُه بعده لا يُقاسُ هنا —
+هذا كاشفٌ جديدٌ لا إصلاحٌ؛ والمقيسُ رفضُ التعشيشِ وإبقاءُ الاستثناءِ
+المسجَّلِ يعملُ واستعادةُ السياقِ بعدَ كلِّ مسارٍ (نجاحٌ ورفضٌ واستثناءٌ).
+"""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+import pytest
+from cryptography.hazmat.primitives.asymmetric import ed25519
+
+from core.constitutional_engine.engine import ConstitutionalEngine
+from core.constitutional_engine.ledger import ConstitutionalLedger
+from core.constitutional_engine.model import ActionRequest, Branch
+from core.sovereignty.compensation import Compensator
+from core.sovereignty.contract import EffectKind, SovereignEffect
+from core.sovereignty.enforcement import ConsumedPermitLedger
+from core.sovereignty.enforcement_boundary import (
+    NestedSovereignCallError,
+    SovereignExecutionBoundary,
+    _active_crossing,
+)
+from core.sovereignty.gateway import SovereignGateway
+from core.sovereignty.idempotency import IdempotencyError, IdempotencyKey, IdempotencyLedger
+from core.sovereignty.outbox import OutboxLedger, SovereignOutbox
+
+# ═══════════════════════════════════════════════════════════════════════════
+# تجهيزات — حالةٌ حقيقيّةٌ وسجلّاتٌ على القرص، على نمطِ ديوانِ التدقيقِ
+# ═══════════════════════════════════════════════════════════════════════════
+
+
+@pytest.fixture()
+def حالةُ_الدولة() -> dict[str, str]:
+    return {
+        "treasury/account-A": "1000",
+        "gov/case-A/row": "NONE",
+        "tasks/task-A/row": "NONE",
+    }
+
+
+@pytest.fixture()
+def بوابة(tmp_path: Path) -> SovereignGateway:
+    return SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(tmp_path / "l.jsonl")))
+
+
+@pytest.fixture()
+def سجلُّ_الذرّيّة(tmp_path: Path) -> IdempotencyLedger:
+    return IdempotencyLedger(tmp_path / "IDEMPOTENCY.json")
+
+
+@pytest.fixture()
+def صادر(tmp_path: Path, بوابة: SovereignGateway) -> SovereignOutbox:
+    return SovereignOutbox(
+        ledger=OutboxLedger(tmp_path / "OUTBOX.json"),
+        verifying_key=ed25519.Ed25519PublicKey.from_public_bytes(
+            bytes.fromhex(بوابة.verifying_key_hex)
+        ),
+    )
+
+
+@pytest.fixture()
+def حدّ(
+    tmp_path: Path,
+    بوابة: SovereignGateway,
+    سجلُّ_الذرّيّة: IdempotencyLedger,
+    صادر: SovereignOutbox,
+) -> SovereignExecutionBoundary:
+    return SovereignExecutionBoundary(
+        gateway=بوابة,
+        idempotency_ledger=سجلُّ_الذرّيّة,
+        outbox=صادر,
+        consumed_permits=ConsumedPermitLedger(tmp_path / "CONSUMED.json"),
+    )
+
+
+def _طلب(
+    action: str,
+    target: str,
+    actor: Branch = Branch.EXECUTIVE,
+) -> ActionRequest:
+    return ActionRequest(actor=actor, action=action, target=target, channel="official")
+
+
+def _أثر(resource: str) -> SovereignEffect:
+    """أثرٌ داخلَ نطاقِ هدفِهِ — فالعقدُ يرفضُ الأثرَ خارجَ الهدفِ المأذونِ."""
+    return SovereignEffect(kind=EffectKind.WRITE, resource=resource, detail="قياس")
+
+
+def _مفتاح(value: str) -> IdempotencyKey:
+    return IdempotencyKey(scope="treasury", value=value)
+
+
+def _معوّض(state: dict[str, str], effect: SovereignEffect) -> Compensator:
+    return Compensator(
+        effect_signature=effect.signature,
+        apply=lambda: state.update({effect.resource: state.get(f"{effect.resource}#أصل", "1000")}),
+        description="إرجاعُ القيمةِ الأصليّة",
+    )
+
+
+def _تنفيذٌ_كامل(
+    حدّ: SovereignExecutionBoundary,
+    action: str,
+    key: str,
+    state: dict[str, str],
+) -> None:
+    """عبورٌ واحدٌ كاملُ المسارِ — لا يُلمسُ فيه أيُّ تعشيشٍ."""
+    أثر = _أثر(f"gov/case-{key}")
+    حدّ.execute(
+        _طلب(action=action, target=f"gov/case-{key}"),
+        declared_effects=(أثر,),
+        planner=lambda _: (أثر,),
+        applier=lambda effect: state.__setitem__(effect.resource, "MUTATED"),
+        operation_key=_مفتاح(key),
+        compensators=(_معوّض(state, أثر),),
+    )
+
+
+# ═══════════════════════════════════════════════════════════════════════════
+# 1 — التعشيشُ غيرُ المستثنى يُرفَضُ قبلَ decide وقبلَ أيِّ قيدٍ
+# ═══════════════════════════════════════════════════════════════════════════
+
+
+def test_التعشيشغيرالمستثنىيرفضقبلأيحارسوقبلأيإذن(
+    حدّ: SovereignExecutionBoundary,
+    بوابة: SovereignGateway,
+    سجلُّ_الذرّيّة: IdempotencyLedger,
+    حالةُ_الدولة: dict[str, str],
+) -> None:
+    """عبورٌ داخلَ عبورٍ نشطٍ بفعلٍ غيرِ مستثنًى يُرفَضُ — فلا `decide` ولا قيدَ ولا أثرَ.
+
+    والدليلُ مقيسٌ لا مُفترَضٌ: سجلُّ البوابةِ يحملُ حكمَ الخارجيِّ وحدَه،
+    ودفترُ الذرّيّةِ لا يعرفُ مفتاحَ الداخلِ، والحالةُ لم يمسَّها إلا الخارجيُّ.
+    (وهذا الفحصُ نفسُه يقتلُ طفرةَ حذفِ الفحصِ عندَ دخولِ execute.)
+    """
+    مفتاح_الخارجي = _مفتاح("outer-1")
+    مفتاح_الداخل = _مفتاح("inner-1")
+    أثر_الخارجي = _أثر("gov/case-A/row")
+    أثر_الداخل = _أثر("treasury/account-A")
+
+    def مطبِّقٌ_يعشِّش(effect: SovereignEffect) -> None:
+        with pytest.raises(NestedSovereignCallError):
+            حدّ.execute(
+                _طلب(action="credit_account", target="treasury/account-A"),
+                declared_effects=(أثر_الداخل,),
+                planner=lambda _: (أثر_الداخل,),
+                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
+                operation_key=مفتاح_الداخل,
+                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
+            )
+        حالةُ_الدولة[effect.resource] = "MUTATED"
+
+    حصيلة = حدّ.execute(
+        _طلب(action="gov.case.open", target="gov/case-A"),
+        declared_effects=(أثر_الخارجي,),
+        planner=lambda _: (أثر_الخارجي,),
+        applier=مطبِّقٌ_يعشِّش,
+        operation_key=مفتاح_الخارجي,
+        compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
+    )
+    assert حصيلة.is_replay is False
+
+    # الرفضُ صريحٌ وبالصنفِ المُعلَنِ: `pytest.raises` أعلاه ضمنَ المطبِّقِ
+    # (لا إذنَ للداخلِ: سجلُّ البوابةِ لا يحملُ أيَّ حكمٍ بفعلِ الداخلِ (لكلِّ عبورٍ حكمانِ:
+    # قرارٌ وإتمامٌ — فالعَدُّ بفعلِ الطلبِ لا بعددِ السطورِ)
+    قرارات_الداخل = [r for r in بوابة.records if r.action == "credit_account"]
+    assert قرارات_الداخل == [], "دخلَ الداخلُ إلى decide — الكاشفُ فُتحَ."
+    # ولا قيدَ للداخلِ في دفترِ الذرّيّةِ
+    assert سجلُّ_الذرّيّة.get(مفتاح_الداخل) is None, "قُيِّدَ الداخلُ في الدفترِ قبلَ الرفضِ."
+    # ولا أثرَ للداخلِ: الحالةُ مسَّها الخارجيُّ وحدَه
+    assert حالةُ_الدولة["gov/case-A/row"] == "MUTATED"
+    assert حالةُ_الدولة["treasury/account-A"] == "1000"
+
+
+# ═══════════════════════════════════════════════════════════════════════════
+# 2 — الزوجُ المسجَّلُ وحدَه يعبرُ، ولا يصيرُ open_case بابًا لغيرِه
+# ═══════════════════════════════════════════════════════════════════════════
+
+
+def test_الزوجالمسجليعبركاملالمسار(
+    حدّ: SovereignExecutionBoundary,
+    بوابة: SovereignGateway,
+    سجلُّ_الذرّيّة: IdempotencyLedger,
+    حالةُ_الدولة: dict[str, str],
+) -> None:
+    """`gov.case.open` → `task.submit`: الزوجُ المسجَّلُ يعبرُ كاملَ المسارِ — إذنانِ وقيدانِ."""
+    مفتاح_الخارجي = _مفتاح("outer-2")
+    مفتاح_الداخل = _مفتاح("inner-2")
+    أثر_الخارجي = _أثر("gov/case-A/row")
+    أثر_الداخل = _أثر("tasks/task-A/row")
+
+    def مطبِّقٌ_مستثنًى(effect: SovereignEffect) -> None:
+        حصيلة_الداخل = حدّ.execute(
+            _طلب(action="task.submit", target="tasks/task-A"),
+            declared_effects=(أثر_الداخل,),
+            planner=lambda _: (أثر_الداخل,),
+            applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
+            operation_key=مفتاح_الداخل,
+            compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
+        )
+        assert حصيلة_الداخل.is_replay is False
+        حالةُ_الدولة[effect.resource] = "MUTATED"
+
+    حدّ.execute(
+        _طلب(action="gov.case.open", target="gov/case-A"),
+        declared_effects=(أثر_الخارجي,),
+        planner=lambda _: (أثر_الخارجي,),
+        applier=مطبِّقٌ_مستثنًى,
+        operation_key=مفتاح_الخارجي,
+        compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
+    )
+    قرارات_الداخل = [r for r in بوابة.records if r.action == "task.submit"]
+    assert len(قرارات_الداخل) == 2  # حكمٌ وإتمامٌ للعبورِ الداخليِّ المستثنَى
+    assert سجلُّ_الذرّيّة.get(مفتاح_الداخل) is not None
+    assert حالةُ_الدولة["tasks/task-A/row"] == "MUTATED"
+
+
+def test_فتحالقضيةليسبابالكلعبورغيرالمستثن(
+    حدّ: SovereignExecutionBoundary,
+    حالةُ_الدولة: dict[str, str],
+) -> None:
+    """طاردُ طفرةِ توسيعِ الاستثناءِ إلى اسمٍ مفردٍ: `gov.case.open` خارجيٌّ لا يعفي غيرَ زوجِه.
+
+    لو اتُّسِعَ الاستثناءُ إلى اسمِ الفعلِ الخارجيِّ وحدَه لَعبرَ `credit_account`
+    داخلَ إطارِ `open_case` — وهذا الفحصُ يقتلُ تلك الطفرةَ.
+    """
+    أثر_الخارجي = _أثر("gov/case-A/row")
+    أثر_الداخل = _أثر("treasury/account-A")
+
+    def مطبِّقٌ_غيرُ_مستثنًى(effect: SovereignEffect) -> None:
+        with pytest.raises(NestedSovereignCallError):
+            حدّ.execute(
+                _طلب(action="credit_account", target="treasury/account-A"),
+                declared_effects=(أثر_الداخل,),
+                planner=lambda _: (أثر_الداخل,),
+                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
+                operation_key=_مفتاح("inner-3"),
+                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
+            )
+        حالةُ_الدولة[effect.resource] = "MUTATED"
+
+    حدّ.execute(
+        _طلب(action="gov.case.open", target="gov/case-A"),
+        declared_effects=(أثر_الخارجي,),
+        planner=lambda _: (أثر_الخارجي,),
+        applier=مطبِّقٌ_غيرُ_مستثنًى,
+        operation_key=_مفتاح("outer-3"),
+        compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
+    )
+
+def test_إطارالأبالباقيبعدالرفضوبعدالعبورالمستثن(
+    حدّ: SovereignExecutionBoundary,
+    حالةُ_الدولة: dict[str, str],
+) -> None:
+    """إطارُ الأبِ لا يُمحى برفضِ ولدٍ ولا بعودةِ ولدٍ مستثنًى — والحمايةُ باقيةٌ حتى النهاية.
+
+    (يقتلُ طفرةَ الضبطِ إلى None بدلَ الاستعادةِ بالرمزِ: لو مُحِيَ إطارُ الأبِ
+    بعدَ ولدٍ مستثنًى لَما رُفِضَ الثاني.)
+    """
+    أثر_الداخل = _أثر("tasks/task-A/row")
+    أثر_الداخل_المرفوض = _أثر("treasury/account-A")
+    رفضٌ: list[int] = []
+
+    def مطبِّقٌ_مُوالٍ(effect: SovereignEffect) -> None:
+        # (1) ولدٌ غيرُ مستثنًى: يُرفَضُ
+        with pytest.raises(NestedSovereignCallError):
+            حدّ.execute(
+                _طلب(action="credit_account", target="treasury/account-A"),
+                declared_effects=(أثر_الداخل_المرفوض,),
+                planner=lambda _: (أثر_الداخل_المرفوض,),
+                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
+                operation_key=_مفتاح("inner-4a"),
+                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل_المرفوض),),
+            )
+        رفضٌ.append(1)
+        # (2) ولدٌ مستثنًى: يعبرُ ويَعودُ
+        حصيلة_مستثنًى = حدّ.execute(
+            _طلب(action="task.submit", target="tasks/task-A"),
+            declared_effects=(أثر_الداخل,),
+            planner=lambda _: (أثر_الداخل,),
+            applier=lambda e: None,
+            operation_key=_مفتاح("inner-4b"),
+            compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
+        )
+        assert حصيلة_مستثنًى.is_replay is False
+        # (3) بعدَ الولدِ المستثنَّى: الحمايةُ باقيةٌ — ولدٌ غيرُ مستثنًى يُرفَضُ من جديدٍ
+        with pytest.raises(NestedSovereignCallError):
+            حدّ.execute(
+                _طلب(action="credit_account", target="treasury/account-A"),
+                declared_effects=(أثر_الداخل_المرفوض,),
+                planner=lambda _: (أثر_الداخل_المرفوض,),
+                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
+                operation_key=_مفتاح("inner-4c"),
+                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل_المرفوض),),
+            )
+        رفضٌ.append(2)
+        حالةُ_الدولة[effect.resource] = "MUTATED"
+
+    حدّ.execute(
+        _طلب(action="gov.case.open", target="gov/case-A"),
+        declared_effects=(_أثر("gov/case-A/row"),),
+        planner=lambda _: (_أثر("gov/case-A/row"),),
+        applier=مطبِّقٌ_مُوالٍ,
+        operation_key=_مفتاح("outer-4"),
+        compensators=(_معوّض(حالةُ_الدولة, _أثر("gov/case-A/row")),),
+    )
+    assert رفضٌ == [1, 2]
+    # الإطارُ مُستعادٌ بعدَ اكتمالِ الأبِ — لا عبورَ نشطَ باقيًا في السياقِ
+    assert _active_crossing.get() is None
+
+
+# ═══════════════════════════════════════════════════════════════════════════
+# 3 — السياقُ يُستعادُ بعدَ كلِّ مسارٍ: نجاحٌ، ورفضٌ، واستثناءٌ في المطبِّق
+# ═══════════════════════════════════════════════════════════════════════════
+
+
+def test_السياقيستعادبعدنجاحالعبوروالعبورالتالييعمل(
+    حدّ: SovereignExecutionBoundary,
+    حالةُ_الدولة: dict[str, str],
+) -> None:
+    """عبورٌ متتابعٌ (لا متعشِّشٌ) بعدَ اكتمالِ سابقِهِ يعملُ — والإطارُ نظيفٌ بينَهما.
+
+    (يقتلُ طفرةَ حذفِ الاستعادةِ في `finally`: لو بقِيَ الإطارُ معلَّقًا
+    لَرُفِظَ التالي كمتعشِّشٍ وهو ليسَ متعشِّشًا.)
+    """
+    _تنفيذٌ_كامل(حدّ, "credit_account", "seq-1", حالةُ_الدولة)
+    assert _active_crossing.get() is None
+    _تنفيذٌ_كامل(حدّ, "credit_account", "seq-2", حالةُ_الدولة)
+    assert _active_crossing.get() is None
+
+
+def test_السياقيستعادبعدرفضمتعششوالعبورالتالييعمل(
+    حدّ: SovereignExecutionBoundary,
+    حالةُ_الدولة: dict[str, str],
+) -> None:
+    """بعدَ عبورٍ رُفِضَ تعشيشُهُ (ورُدَّ أثرُهُ)، السياقُ نظيفٌ والعبورُ التاليُ يعملُ."""
+    أثر_الخارجي = _أثر("gov/case-A/row")
+    أثر_الداخل = _أثر("treasury/account-A")
+    def مطبِّقٌ_يرفض(effect: SovereignEffect) -> None:
+        with pytest.raises(NestedSovereignCallError):
+            حدّ.execute(
+                _طلب(action="credit_account", target="treasury/account-A"),
+                declared_effects=(أثر_الداخل,),
+                planner=lambda _: (أثر_الداخل,),
+                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
+                operation_key=_مفتاح("inner-5"),
+                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
+            )
+        حالةُ_الدولة[effect.resource] = "MUTATED"
+
+    حدّ.execute(
+        _طلب(action="gov.case.open", target="gov/case-A"),
+        declared_effects=(أثر_الخارجي,),
+        planner=lambda _: (أثر_الخارجي,),
+        applier=مطبِّقٌ_يرفض,
+        operation_key=_مفتاح("outer-5"),
+        compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
+    )
+    assert _active_crossing.get() is None
+    _تنفيذٌ_كامل(حدّ, "credit_account", "seq-after-reject", حالةُ_الدولة)
+    assert _active_crossing.get() is None
+
+
+def test_السياقيستعادبعداستثناءالمطبق(
+    حدّ: SovereignExecutionBoundary,
+    حالةُ_الدولة: dict[str, str],
+) -> None:
+    """استثناءُ المطبِّقِ يُغلَّفُ في `IdempotencyError` بعدَ نقلِ السجلِّ إلى «فاشل» (لا أثرَ مُطبَّقًا فلا تعويضَ)، والسياقُ يُستعادُ في `finally`.
+
+    (يقتلُ طفرةَ حذفِ `finally` في مسارِ الاستثناءِ تحديدًا.)
+    """
+    أثر_الخارجي = _أثر("gov/case-A/row")
+
+    def مطبِّقٌ_يفشل(effect: SovereignEffect) -> None:
+        raise RuntimeError("فشلٌ مقيسٌ في المطبِّق")
+
+    with pytest.raises(IdempotencyError, match="فشلٌ مقيسٌ"):
+        حدّ.execute(
+            _طلب(action="gov.case.open", target="gov/case-A"),
+            declared_effects=(أثر_الخارجي,),
+            planner=lambda _: (أثر_الخارجي,),
+            applier=مطبِّقٌ_يفشل,
+            operation_key=_مفتاح("outer-6"),
+            compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
+        )
+    assert _active_crossing.get() is None, "الإطارُ بقِيَ معلَّقًا بعدَ استثناءِ المطبِّقِ."
+    # والعبورُ التالي (متتابعٌ) يعملُ — فالرفضُ المزعجُ للتعشيشِ لم يعد يصيبُ البريئَ
+    _تنفيذٌ_كامل(حدّ, "credit_account", "seq-after-exc", حالةُ_الدولة)
+    assert _active_crossing.get() is None
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
EXIT: 0
BYTES: 775
SHA256: 204cd4039e46c9203a4b8b8b0e89942cc729b2bb4b62957f36fb3df68f814aac
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/kimi_k3/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
.......                                                                  [100%]
7 passed in 0.21s
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
EXIT: 0
BYTES: 1389
SHA256: 153d0e7e858fb18e61bb8ec08d4c76b58200bf0656a206115c50b8ed1e056323
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/kimi_k3/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/kimi_k3/wi115/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 3 items

federal/executive/services/tests/test_wi115_reversed_replay.py ..        [ 66%]
federal/executive/services/tests/test_wi115_nesting_compensator_frame.py . [100%]

============================== 3 passed in 1.46s ===============================
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && rg -n "NESTED_SOVEREIGN_EXEMPTIONS|NestedSovereignCallError|open_case" core/sovereignty/enforcement_boundary.py
EXIT: 0
BYTES: 796
SHA256: 546f6b1a06a270ecccc25ef587bee4307dfb536676c5b6b035079a9cfaf0da04
NO_EOL: 0
--- OUTPUT ---
119:# النصُّ المقيسُ (W-665 § 1): التعشيشُ القائمُ الوحيدُ اليومَ هو `open_case` —
123:# لا أسماءٌ مفردة، فلا يصيرُ `open_case` بابًا لأيِّ عبورٍ داخلَه — وهو
128:NESTED_SOVEREIGN_EXEMPTIONS: Final[frozenset[tuple[str, str]]] = frozenset(
186:class NestedSovereignCallError(EnforcementBoundaryError):
191:    المُعفاةُ أزواجُهُ في `NESTED_SOVEREIGN_EXEMPTIONS` (open_case باسمِه).
377:        if outer_crossing is not None and (outer_crossing[0], request.action) not in NESTED_SOVEREIGN_EXEMPTIONS:
378:            raise NestedSovereignCallError(
381:                "والزوجُ ليسَ منَ الاستثناءِ المسجَّلِ (open_case باسمِه وحدَه)."
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && rm -rf ../old && git worktree add --detach ../old 2b814b34^ && cp tests/sovereignty/test_wi115_nesting_detector.py ../old/tests/sovereignty/ && cd ../old && /home/user/workspace/council_w701/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
EXIT: 2
BYTES: 2033
SHA256: 1660644a738520eab29e32b8b1f6df4667d8598b2da33d8029f11fe7bf968922
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD bd1dc84b)
HEAD is now at bd1dc84b W-684: إعادةُ توليدِ مصفوفةِ الحقيقةِ (ملفّاتٌ مُعفاةٌ وحدَها)
/home/user/workspace/council_w701/kimi_k3/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

==================================== ERRORS ====================================
______ ERROR collecting tests/sovereignty/test_wi115_nesting_detector.py _______
ImportError while importing test module '/home/user/workspace/council_w701/kimi_k3/wi115/old/tests/sovereignty/test_wi115_nesting_detector.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/uv/python/cpython-3.12.15-linux-x86_64-gnu/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/sovereignty/test_wi115_nesting_detector.py:35: in <module>
    from core.sovereignty.enforcement_boundary import (
E   ImportError: cannot import name 'NestedSovereignCallError' from 'core.sovereignty.enforcement_boundary' (/home/user/workspace/council_w701/kimi_k3/wi115/old/core/sovereignty/enforcement_boundary.py)
=========================== short test summary info ============================
ERROR tests/sovereignty/test_wi115_nesting_detector.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && sha256sum docs/audit/evidence/W-701/briefs_wi115/briefing_kimi_k3.md
EXIT: 0
BYTES: 125
SHA256: 08ee8e0f84ea76634e8f514dc341c4ffecd088f2fe4da03dad883828253ddcca
NO_EOL: 0
--- OUTPUT ---
80ced2213675420a5c50861e1e3ab79e3ad7e680c7161992cb3cdb2e505385aa  docs/audit/evidence/W-701/briefs_wi115/briefing_kimi_k3.md
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && cat docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS
EXIT: 0
BYTES: 268
SHA256: ae7d75f9e11b9351cd3e977e2d0d6932cfdd2f7d09794e030bdbab2ebc399f5f
NO_EOL: 0
--- OUTPUT ---
59c601126c30585d32790210c831dc953ab8516e89c8211838819313edf91e1c  briefing_gemini_3_8_flash.md
5fda37e5742b405f044202c1d1e8b95e113e058c4424bd9b5b68fb76cf0f3f20  briefing_grok_4_7.md
80ced2213675420a5c50861e1e3ab79e3ad7e680c7161992cb3cdb2e505385aa  briefing_kimi_k3.md
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w701/kimi_k3/wi115/probe/probe_kimi_k3_nesting.py
EXIT: 0
BYTES: 13467
SHA256: 2d644553b97f0762b456461b72b063291c624c79e1ec1a2879ff42824cb4c799
NO_EOL: 0
--- OUTPUT ---
     1	"""مسبارُ مقعدِ kimi_k3 الخاصُّ (WI-115 · الكاشف — البروتوكولُ § 4.9).
     2	
     3	يكتبُه المقعدُ من عندِه — ليسَ أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ.
     4	يُنادي الكاشفَ نفسَه (core/sovereignty/enforcement_boundary.py) ويحاولُ
     5	كسرَ الخاصّيّةِ المُدَّعاةِ في خمسةِ مساراتٍ، منها واحدٌ لم يقِسْهُ فحصُ
     6	المنفِّذِ (التعشيشُ عبرَ نسختَينِ مختلفتَينِ منَ الحدِّ في السياقِ نفسِه).
     7	
     8	الخاصّيّةُ المُستهدَفةُ بالكسر: عبورٌ سياديٌّ داخلَ عبورٍ نشطٍ يُرفَضُ
     9	بـNestedSovereignCallError قبلَ any decide وأيِّ قيدٍ، والاستثناءُ المسجَّلُ
    10	أزواجٌ (gov.case.open → task.submit / task.cancel) لا أسماءٌ مفردة.
    11	
    12	الخروج: 0 إن صمدَتِ الخاصّيّةُ كلُّها (لم تنكسر) · 1 إن انكسرتْ ولو في مسارٍ.
    13	كلُّ سيناريو يطبعُ نتيجتَه حرفيًّا: HELD (صمدَ الكاشف) أو BROKEN (انكسر).
    14	"""
    15	
    16	from __future__ import annotations
    17	
    18	import sys
    19	import tempfile
    20	from pathlib import Path
    21	
    22	from core.constitutional_engine.engine import ConstitutionalEngine
    23	from core.constitutional_engine.ledger import ConstitutionalLedger
    24	from core.constitutional_engine.model import ActionRequest, Branch
    25	from core.sovereignty.compensation import Compensator
    26	from core.sovereignty.contract import EffectKind, SovereignEffect
    27	from core.sovereignty.enforcement import ConsumedPermitLedger
    28	from core.sovereignty.enforcement_boundary import (
    29	    NESTED_SOVEREIGN_EXEMPTIONS,
    30	    NestedSovereignCallError,
    31	    SovereignExecutionBoundary,
    32	    _active_crossing,
    33	)
    34	from core.sovereignty.gateway import SovereignGateway
    35	from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger
    36	
    37	failures: list[str] = []
    38	
    39	
    40	def _report(name: str, held: bool, detail: str) -> None:
    41	    print(f"[{'HELD' if held else 'BROKEN'}] {name}: {detail}")
    42	    if not held:
    43	        failures.append(name)
    44	
    45	
    46	def _boundary(base: Path, tag: str) -> tuple[SovereignExecutionBoundary, SovereignGateway, IdempotencyLedger]:
    47	    """حدٌّ حقيقيٌّ بدفاترَ على القرص — بلا حُقَنٍ ولا محاكاة."""
    48	    d = base / tag
    49	    d.mkdir(parents=True, exist_ok=True)
    50	    gateway = SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(d / "ledger.jsonl")))
    51	    ledger = IdempotencyLedger(d / "IDEMPOTENCY.json")
    52	    boundary = SovereignExecutionBoundary(
    53	        gateway=gateway,
    54	        idempotency_ledger=ledger,
    55	        outbox=None,
    56	        consumed_permits=ConsumedPermitLedger(d / "CONSUMED.json"),
    57	    )
    58	    return boundary, gateway, ledger
    59	
    60	
    61	def _req(action: str, target: str) -> ActionRequest:
    62	    return ActionRequest(actor=Branch.EXECUTIVE, action=action, target=target, channel="official")
    63	
    64	
    65	def _fx(resource: str) -> SovereignEffect:
    66	    return SovereignEffect(kind=EffectKind.WRITE, resource=resource, detail="probe-kimi_k3")
    67	
    68	
    69	def _key(v: str) -> IdempotencyKey:
    70	    return IdempotencyKey(scope="kimi_k3-probe", value=v)
    71	
    72	
    73	def _comp(state: dict[str, str], effect: SovereignEffect) -> Compensator:
    74	    return Compensator(
    75	        effect_signature=effect.signature,
    76	        apply=lambda: state.update({effect.resource: state.get(f"{effect.resource}#orig", "ORIG")}),
    77	        description="إرجاع",
    78	    )
    79	
    80	
    81	def _cross(
    82	    boundary: SovereignExecutionBoundary,
    83	    action: str,
    84	    target: str,
    85	    key_value: str,
    86	    state: dict[str, str],
    87	    applier=None,
    88	) -> None:
    89	    effect = _fx(target)
    90	    boundary.execute(
    91	        _req(action, target),
    92	        declared_effects=(effect,),
    93	        planner=lambda _: (effect,),
    94	        applier=applier or (lambda e: state.__setitem__(e.resource, "TOUCHED")),
    95	        operation_key=_key(key_value),
    96	        compensators=(_comp(state, effect),),
    97	    )
    98	
    99	
   100	def main() -> int:
   101	    tmp = Path(tempfile.mkdtemp(prefix="kimi_k3_probe_"))
   102	    state: dict[str, str] = {}
   103	
   104	    # التحقُّقُ الصفري: جدولُ الاستثناءِ مُجمَّدٌ ويحوي الزوجَينِ المُعلَنَين حرفيًّا
   105	    _report(
   106	        "EXEMPTIONS_FROZEN_PAIRS",
   107	        NESTED_SOVEREIGN_EXEMPTIONS == frozenset({("gov.case.open", "task.submit"), ("gov.case.open", "task.cancel")}),
   108	        f"الجدولُ الفعليُّ: {sorted(NESTED_SOVEREIGN_EXEMPTIONS)}",
   109	    )
   110	
   111	    # ── سيناريو 1 — كسرٌ مباشر: تعشيشٌ غيرُ مستثنًى داخلَ إطارٍ نشطٍ ──────────
   112	    b1, g1, l1 = _boundary(tmp, "s1")
   113	    inner_key = _key("s1-inner")
   114	
   115	    def applier_s1(effect: SovereignEffect) -> None:
   116	        try:
   117	            _cross(b1, "payroll.run", "payroll/batch-9", "s1-inner", state)
   118	        except NestedSovereignCallError:
   119	            state["s1_rejected"] = "YES"
   120	        else:
   121	            state["s1_rejected"] = "NO-SLIPPED-THROUGH"  # انكسارٌ إن وصلنا هنا
   122	        state[effect.resource] = "TOUCHED"  # أثرُ الأبِ يُطبَّقُ بعدَ رفضِ الولد
   123	
   124	    _cross(b1, "fx.transfer", "fx/pool-1", "s1-outer", state, applier=applier_s1)
   125	    inner_records = [r for r in g1.records if r.action == "payroll.run"]
   126	    _report(
   127	        "NESTED_NON_EXEMPT_REFUSED",
   128	        state.get("s1_rejected") == "YES",
   129	        f"الرميُ: {state.get('s1_rejected')}",
   130	    )
   131	    _report(
   132	        "NO_DECIDE_NO_LEDGER_FOR_INNER",
   133	        inner_records == [] and l1.get(inner_key) is None,
   134	        f"سجلُّ decide للداخلِ: {len(inner_records)} · قيدُ الدفترِ: {l1.get(inner_key)}",
   135	    )
   136	    _report(
   137	        "OUTER_FRAME_INTACT_AFTER_REFUSAL",
   138	        _active_crossing.get() is None and state.get("fx/pool-1") == "TOUCHED",
   139	        f"الإطارُ بعدَ الأبِ: {_active_crossing.get()} · أثرُ الأبِ: {state.get('fx/pool-1')}",
   140	    )
   141	
   142	    # ── سيناريو 2 — الزوجانِ المُجمَّدانِ وحدَهما يمرّانِ (open_case باسمِه) ────
   143	    b2, g2, l2 = _boundary(tmp, "s2")
   144	
   145	    def applier_s2(effect: SovereignEffect) -> None:
   146	        for act, tgt in (("task.submit", "tasks/task-1"), ("task.cancel", "tasks/task-1")):
   147	            try:
   148	                _cross(b2, act, tgt, f"s2-{act}", state)
   149	                state[f"s2_{act}"] = "PASSED-BY-EXEMPTION"
   150	            except NestedSovereignCallError:
   151	                state[f"s2_{act}"] = "WRONGLY-REFUSED"
   152	
   153	    _cross(b2, "gov.case.open", "gov/case-A", "s2-outer", state, applier=applier_s2)
   154	    _report(
   155	        "REGISTERED_PAIRS_PASS",
   156	        state.get("s2_task.submit") == "PASSED-BY-EXEMPTION" and state.get("s2_task.cancel") == "PASSED-BY-EXEMPTION",
   157	        f"submit: {state.get('s2_task.submit')} · cancel: {state.get('s2_task.cancel')}",
   158	    )
   159	    inner2 = [r for r in g2.records if r.action in ("task.submit", "task.cancel")]
   160	    _report(
   161	        "EXEMPT_INNER_FULLY_DECIDED",
   162	        len(inner2) == 4,
   163	        f"أحكامُ الداخلِ المستثنى في سجلِّ البوابةِ: {len(inner2)} (متوقَّع 4)",
   164	    )
   165	
   166	    # ── سيناريو 3 — الاستثناءُ أزواجٌ لا أسماء: الاتّجاهانِ يُرفَضانِ ──────────
   167	    # (أ) الاسمُ الخارجيُّ الصحيحُ (gov.case.open) بفعلٍ داخليٍّ غيرِ زوجِه
   168	    b3, g3, l3 = _boundary(tmp, "s3")
   169	
   170	    def applier_s3a(effect: SovereignEffect) -> None:
   171	        try:
   172	            _cross(b3, "task.approve", "tasks/task-2", "s3-a", state)
   173	            state["s3_a"] = "SLIPPED-THROUGH"  # انكسارٌ إن وصلنا هنا
   174	        except NestedSovereignCallError:
   175	            state["s3_a"] = "REFUSED"
   176	
   177	    _cross(b3, "gov.case.open", "gov/case-B", "s3-outer-a", state, applier=applier_s3a)
   178	    _report(
   179	        "OUTER_NAME_NOT_A_GATE",
   180	        state.get("s3_a") == "REFUSED",
   181	        f"task.approve داخلَ gov.case.open: {state.get('s3_a')}",
   182	    )
   183	    # (ب) الفعلُ الداخليُّ الصحيحُ (task.submit) تحتَ اسمٍ خارجيٍّ غيرِ زوجِه
   184	    b3b, g3b, l3b = _boundary(tmp, "s3b")
   185	    state["s3_b"] = "UNSET"
   186	
   187	    def applier_s3b(effect: SovereignEffect) -> None:
   188	        try:
   189	            _cross(b3b, "task.submit", "tasks/task-3", "s3-b", state)
   190	            state["s3_b"] = "SLIPPED-THROUGH"  # انكسارٌ إن وصلنا هنا
   191	        except NestedSovereignCallError:
   192	            state["s3_b"] = "REFUSED"
   193	
   194	    _cross(b3b, "fx.transfer", "fx/pool-2", "s3b-outer", state, applier=applier_s3b)
   195	    _report(
   196	        "INNER_NAME_NOT_A_TICKET",
   197	        state.get("s3_b") == "REFUSED",
   198	        f"task.submit داخلَ fx.transfer: {state.get('s3_b')}",
   199	    )
   200	
   201	    # ── سيناريو 4 — التعشيشُ عبرَ نسختَينِ مختلفتَينِ منَ الحدِّ (لم يقِسْهُ الفحص) ──
   202	    bA, gA, lA = _boundary(tmp, "sA")
   203	    bB, gB, lB = _boundary(tmp, "sB")
   204	
   205	    def applier_s4(effect: SovereignEffect) -> None:
   206	        try:
   207	            _cross(bB, "payroll.run", "payroll/batch-7", "s4-inner", state)  # النسخةُ الأخرى!
   208	            state["s4"] = "SLIPPED-THROUGH-CROSS-INSTANCE"
   209	        except NestedSovereignCallError:
   210	            state["s4"] = "REFUSED"
   211	
   212	    _cross(bA, "fx.transfer", "fx/pool-9", "s4-outer", state, applier=applier_s4)
   213	    _report(
   214	        "CROSS_INSTANCE_NESTING_REFUSED",
   215	        state.get("s4") == "REFUSED",
   216	        f"الكشفُ على مستوى الوحدةِ عبرَ نسختَين: {state.get('s4')}",
   217	    )
   218	    _report(
   219	        "CROSS_INSTANCE_INNER_INVISIBLE",
   220	        [r for r in gB.records if r.action == "payroll.run"] == [],
   221	        f"قراراتُ payroll.run في بوابةِ النسخةِ الثانيةِ: {len([r for r in gB.records if r.action == 'payroll.run'])}",
   222	    )
   223	
   224	    # ── سيناريو 5 — استعادةُ السياقِ بالرمز: عبورانِ متعشِّشانِ متتاليانِ ────────
   225	    b5, g5, l5 = _boundary(tmp, "s5")
   226	    hits: list[str] = []
   227	
   228	    def applier_s5(effect: SovereignEffect) -> None:
   229	        # الأولُ زوجٌ مستثنًى فيمرُّ شرعًا · الثاني غيرُ مستثنًى فيجبُ رفضُه بعدَ عودةِ الأول
   230	        for name, act, tgt in (("exempt-first", "task.submit", "tasks/t-5a"), ("nonexempt-second", "payroll.run", "payroll/b-5")):
   231	            try:
   232	                _cross(b5, act, tgt, f"s5-{name}", state)
   233	                hits.append(f"{name}:PASSED")
   234	            except NestedSovereignCallError:
   235	                hits.append(f"{name}:REFUSED")
   236	
   237	    _cross(b5, "gov.case.open", "gov/case-C", "s5-outer", state, applier=applier_s5)
   238	    _report(
   239	        "FRAME_SURVIVES_EXEMPT_CHILD",
   240	        hits == ["exempt-first:PASSED", "nonexempt-second:REFUSED"],
   241	        f"التسلسل: {hits} — لو مُحِيَ إطارُ الأبِ برجوعِ المستثنى لمرَّ الثاني.",
   242	    )
   243	    state_after = _active_crossing.get()
   244	    _report(
   245	        "CONTEXT_RESTORED_AFTER_PARENT",
   246	        state_after is None,
   247	        f"الإطارُ بعدَ اكتمالِ الأبِ: {state_after}",
   248	    )
   249	
   250	    print()
   251	    print("=" * 72)
   252	    if failures:
   253	        print(f"PROBE RESULT: BROKEN — انكسرتِ الخاصّيّةُ في: {failures}")
   254	        return 1
   255	    print("PROBE RESULT: HELD — صمدَ الكاشفُ في كلِّ محاولاتِ الكسرِ (لم تنكسرِ الخاصّيّة).")
   256	    return 0
   257	
   258	
   259	if __name__ == "__main__":
   260	    sys.exit(main())
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && PYTHONPATH=/home/user/workspace/council_w701/kimi_k3/wi115/repo .venv/bin/python /home/user/workspace/council_w701/kimi_k3/wi115/probe/probe_kimi_k3_nesting.py
EXIT: 0
BYTES: 1523
SHA256: 7beb65ac33f89602674a8ac75de3ea0a3cc58d0da2155ecc47a551b9e0a98d7a
NO_EOL: 0
--- OUTPUT ---
[HELD] EXEMPTIONS_FROZEN_PAIRS: الجدولُ الفعليُّ: [('gov.case.open', 'task.cancel'), ('gov.case.open', 'task.submit')]
[HELD] NESTED_NON_EXEMPT_REFUSED: الرميُ: YES
[HELD] NO_DECIDE_NO_LEDGER_FOR_INNER: سجلُّ decide للداخلِ: 0 · قيدُ الدفترِ: None
[HELD] OUTER_FRAME_INTACT_AFTER_REFUSAL: الإطارُ بعدَ الأبِ: None · أثرُ الأبِ: TOUCHED
[HELD] REGISTERED_PAIRS_PASS: submit: PASSED-BY-EXEMPTION · cancel: PASSED-BY-EXEMPTION
[HELD] EXEMPT_INNER_FULLY_DECIDED: أحكامُ الداخلِ المستثنى في سجلِّ البوابةِ: 4 (متوقَّع 4)
[HELD] OUTER_NAME_NOT_A_GATE: task.approve داخلَ gov.case.open: REFUSED
[HELD] INNER_NAME_NOT_A_TICKET: task.submit داخلَ fx.transfer: REFUSED
[HELD] CROSS_INSTANCE_NESTING_REFUSED: الكشفُ على مستوى الوحدةِ عبرَ نسختَين: REFUSED
[HELD] CROSS_INSTANCE_INNER_INVISIBLE: قراراتُ payroll.run في بوابةِ النسخةِ الثانيةِ: 0
[HELD] FRAME_SURVIVES_EXEMPT_CHILD: التسلسل: ['exempt-first:PASSED', 'nonexempt-second:REFUSED'] — لو مُحِيَ إطارُ الأبِ برجوعِ المستثنى لمرَّ الثاني.
[HELD] CONTEXT_RESTORED_AFTER_PARENT: الإطارُ بعدَ اكتمالِ الأبِ: None

========================================================================
PROBE RESULT: HELD — صمدَ الكاشفُ في كلِّ محاولاتِ الكسرِ (لم تنكسرِ الخاصّيّة).
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi115/repo && rm -rf ../mutant && git worktree add --detach ../mutant 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247 && sed -i "s/if outer_crossing is not None and/if False and outer_crossing is not None and/" ../mutant/core/sovereignty/enforcement_boundary.py && cd ../mutant && /home/user/workspace/council_w701/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
EXIT: 1
BYTES: 18970
SHA256: 9034e446ff48c5912c083f659602b96d589149e9bdacbbb4d67acc39d82ea277
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD 147a0c6b)
HEAD is now at 147a0c6b W-701: توجيهُ المستشارِ 25 — قراراتُ المالكِ D27 بنصّها (إغلاقُ WI-113/WI-117/WI-119 بعدَ VERIFIED بإجماعٍ دونَ سؤالٍ جديدٍ · الجولةُ الآنَ لا بعدَ G1 — جولةٌ واحدةٌ بثلاثةِ نطاقاتٍ تُجمَعُ في الجلسةِ نفسِها Q-72) + واجبُ N+1 لـPR #168 (قراءةُ التشغيلِ 40478049851 بالفاحصِ فعلًا: مقروءٌ أخضرُ 13/13 على 129bed06 · EXIT 0) + انتقالٌ واحدٌ: WI-119 IN_PROGRESS→IN_REVIEW + إحاطاتُ الجولةِ التسعُ مبصومةً (3 مقاعدٍ × WI-117/WI-119/الكاشفُ من WI-115 · gemini · grok · kimi) ونصوصُ الإطلاقِ حرفيًّا وقياساتُ الجلسةِ خامًا (حوكمةُ الأعمالِ ✓ · راتشيتٌ 61 · حزمةُ الحوكمةِ 1394 خضراءَ) · لا شِّفرةَ سلوكيّةً · المنسِّقُ GLM-5.3 (Perplexity Computer)
/home/user/workspace/council_w701/kimi_k3/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
F.FF.F.                                                                  [100%]
=================================== FAILURES ===================================
________________ test_التعشيشغيرالمستثنىيرفضقبلأيحارسوقبلأيإذن _________________

حدّ = SovereignExecutionBoundary(gateway=<core.sovereignty.gateway.SovereignGateway object at 0x7f36bc607590>, idempotency_l...Journal(path=PosixPath('/tmp/pytest-of-user/pytest-11/test_التعشيشغيرالمستثنىيرفضقبل0/IDEMPOTENCY.compensation.json')))
بوابة = <core.sovereignty.gateway.SovereignGateway object at 0x7f36bc607590>
سجلُّ_الذرّيّة = IdempotencyLedger(path=PosixPath('/tmp/pytest-of-user/pytest-11/test_التعشيشغيرالمستثنىيرفضقبل0/IDEMPOTENCY.json'))
حالةُ_الدولة = {'treasury/account-A': 'MUTATED', 'gov/case-A/row': 'NONE', 'tasks/task-A/row': 'NONE'}

    def test_التعشيشغيرالمستثنىيرفضقبلأيحارسوقبلأيإذن(
        حدّ: SovereignExecutionBoundary,
        بوابة: SovereignGateway,
        سجلُّ_الذرّيّة: IdempotencyLedger,
        حالةُ_الدولة: dict[str, str],
    ) -> None:
        """عبورٌ داخلَ عبورٍ نشطٍ بفعلٍ غيرِ مستثنًى يُرفَضُ — فلا `decide` ولا قيدَ ولا أثرَ.
    
        والدليلُ مقيسٌ لا مُفترَضٌ: سجلُّ البوابةِ يحملُ حكمَ الخارجيِّ وحدَه،
        ودفترُ الذرّيّةِ لا يعرفُ مفتاحَ الداخلِ، والحالةُ لم يمسَّها إلا الخارجيُّ.
        (وهذا الفحصُ نفسُه يقتلُ طفرةَ حذفِ الفحصِ عندَ دخولِ execute.)
        """
        مفتاح_الخارجي = _مفتاح("outer-1")
        مفتاح_الداخل = _مفتاح("inner-1")
        أثر_الخارجي = _أثر("gov/case-A/row")
        أثر_الداخل = _أثر("treasury/account-A")
    
        def مطبِّقٌ_يعشِّش(effect: SovereignEffect) -> None:
            with pytest.raises(NestedSovereignCallError):
                حدّ.execute(
                    _طلب(action="credit_account", target="treasury/account-A"),
                    declared_effects=(أثر_الداخل,),
                    planner=lambda _: (أثر_الداخل,),
                    applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                    operation_key=مفتاح_الداخل,
                    compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
                )
            حالةُ_الدولة[effect.resource] = "MUTATED"
    
>       حصيلة = حدّ.execute(
            _طلب(action="gov.case.open", target="gov/case-A"),
            declared_effects=(أثر_الخارجي,),
            planner=lambda _: (أثر_الخارجي,),
            applier=مطبِّقٌ_يعشِّش,
            operation_key=مفتاح_الخارجي,
            compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
        )

tests/sovereignty/test_wi115_nesting_detector.py:170: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
core/sovereignty/enforcement_boundary.py:467: in execute
    ).run_once(
core/sovereignty/idempotency.py:886: in run_once
    return self._run_once_inner(
core/sovereignty/idempotency.py:923: in _run_once_inner
    value = execute()
            ^^^^^^^^^
core/sovereignty/enforcement_boundary.py:448: in _under_permit
    produced = self.policy_enforcement_point.enforce(
core/sovereignty/enforcement.py:377: in enforce
    applier(effect)
core/sovereignty/enforcement_boundary.py:433: in _tracked
    routed(effect)
core/sovereignty/enforcement_boundary.py:723: in route
    applier(effect)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

effect = SovereignEffect(kind=<EffectKind.WRITE: 'WRITE'>, resource='gov/case-A/row', detail='قياس', payload_digest=None)

    def مطبِّقٌ_يعشِّش(effect: SovereignEffect) -> None:
>       with pytest.raises(NestedSovereignCallError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE NestedSovereignCallError

tests/sovereignty/test_wi115_nesting_detector.py:159: Failed
____________________ test_فتحالقضيةليسبابالكلعبورغيرالمستثن ____________________

حدّ = SovereignExecutionBoundary(gateway=<core.sovereignty.gateway.SovereignGateway object at 0x7f36bc6f8fe0>, idempotency_l...Journal(path=PosixPath('/tmp/pytest-of-user/pytest-11/test_فتحالقضيةليسبابالكلعبورغي0/IDEMPOTENCY.compensation.json')))
حالةُ_الدولة = {'treasury/account-A': 'MUTATED', 'gov/case-A/row': 'NONE', 'tasks/task-A/row': 'NONE'}

    def test_فتحالقضيةليسبابالكلعبورغيرالمستثن(
        حدّ: SovereignExecutionBoundary,
        حالةُ_الدولة: dict[str, str],
    ) -> None:
        """طاردُ طفرةِ توسيعِ الاستثناءِ إلى اسمٍ مفردٍ: `gov.case.open` خارجيٌّ لا يعفي غيرَ زوجِه.
    
        لو اتُّسِعَ الاستثناءُ إلى اسمِ الفعلِ الخارجيِّ وحدَه لَعبرَ `credit_account`
        داخلَ إطارِ `open_case` — وهذا الفحصُ يقتلُ تلك الطفرةَ.
        """
        أثر_الخارجي = _أثر("gov/case-A/row")
        أثر_الداخل = _أثر("treasury/account-A")
    
        def مطبِّقٌ_غيرُ_مستثنًى(effect: SovereignEffect) -> None:
            with pytest.raises(NestedSovereignCallError):
                حدّ.execute(
                    _طلب(action="credit_account", target="treasury/account-A"),
                    declared_effects=(أثر_الداخل,),
                    planner=lambda _: (أثر_الداخل,),
                    applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                    operation_key=_مفتاح("inner-3"),
                    compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
                )
            حالةُ_الدولة[effect.resource] = "MUTATED"
    
>       حدّ.execute(
            _طلب(action="gov.case.open", target="gov/case-A"),
            declared_effects=(أثر_الخارجي,),
            planner=lambda _: (أثر_الخارجي,),
            applier=مطبِّقٌ_غيرُ_مستثنًى,
            operation_key=_مفتاح("outer-3"),
            compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
        )

tests/sovereignty/test_wi115_nesting_detector.py:259: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
core/sovereignty/enforcement_boundary.py:467: in execute
    ).run_once(
core/sovereignty/idempotency.py:886: in run_once
    return self._run_once_inner(
core/sovereignty/idempotency.py:923: in _run_once_inner
    value = execute()
            ^^^^^^^^^
core/sovereignty/enforcement_boundary.py:448: in _under_permit
    produced = self.policy_enforcement_point.enforce(
core/sovereignty/enforcement.py:377: in enforce
    applier(effect)
core/sovereignty/enforcement_boundary.py:433: in _tracked
    routed(effect)
core/sovereignty/enforcement_boundary.py:723: in route
    applier(effect)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

effect = SovereignEffect(kind=<EffectKind.WRITE: 'WRITE'>, resource='gov/case-A/row', detail='قياس', payload_digest=None)

    def مطبِّقٌ_غيرُ_مستثنًى(effect: SovereignEffect) -> None:
>       with pytest.raises(NestedSovereignCallError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE NestedSovereignCallError

tests/sovereignty/test_wi115_nesting_detector.py:248: Failed
_________________ test_إطارالأبالباقيبعدالرفضوبعدالعبورالمستثن _________________

حدّ = SovereignExecutionBoundary(gateway=<core.sovereignty.gateway.SovereignGateway object at 0x7f36bb924ce0>, idempotency_l...Journal(path=PosixPath('/tmp/pytest-of-user/pytest-11/test_إطارالأبالباقيبعدالرفضوبع0/IDEMPOTENCY.compensation.json')))
حالةُ_الدولة = {'treasury/account-A': 'MUTATED', 'gov/case-A/row': 'NONE', 'tasks/task-A/row': 'NONE'}

    def test_إطارالأبالباقيبعدالرفضوبعدالعبورالمستثن(
        حدّ: SovereignExecutionBoundary,
        حالةُ_الدولة: dict[str, str],
    ) -> None:
        """إطارُ الأبِ لا يُمحى برفضِ ولدٍ ولا بعودةِ ولدٍ مستثنًى — والحمايةُ باقيةٌ حتى النهاية.
    
        (يقتلُ طفرةَ الضبطِ إلى None بدلَ الاستعادةِ بالرمزِ: لو مُحِيَ إطارُ الأبِ
        بعدَ ولدٍ مستثنًى لَما رُفِضَ الثاني.)
        """
        أثر_الداخل = _أثر("tasks/task-A/row")
        أثر_الداخل_المرفوض = _أثر("treasury/account-A")
        رفضٌ: list[int] = []
    
        def مطبِّقٌ_مُوالٍ(effect: SovereignEffect) -> None:
            # (1) ولدٌ غيرُ مستثنًى: يُرفَضُ
            with pytest.raises(NestedSovereignCallError):
                حدّ.execute(
                    _طلب(action="credit_account", target="treasury/account-A"),
                    declared_effects=(أثر_الداخل_المرفوض,),
                    planner=lambda _: (أثر_الداخل_المرفوض,),
                    applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                    operation_key=_مفتاح("inner-4a"),
                    compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل_المرفوض),),
                )
            رفضٌ.append(1)
            # (2) ولدٌ مستثنًى: يعبرُ ويَعودُ
            حصيلة_مستثنًى = حدّ.execute(
                _طلب(action="task.submit", target="tasks/task-A"),
                declared_effects=(أثر_الداخل,),
                planner=lambda _: (أثر_الداخل,),
                applier=lambda e: None,
                operation_key=_مفتاح("inner-4b"),
                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
            )
            assert حصيلة_مستثنًى.is_replay is False
            # (3) بعدَ الولدِ المستثنَّى: الحمايةُ باقيةٌ — ولدٌ غيرُ مستثنًى يُرفَضُ من جديدٍ
            with pytest.raises(NestedSovereignCallError):
                حدّ.execute(
                    _طلب(action="credit_account", target="treasury/account-A"),
                    declared_effects=(أثر_الداخل_المرفوض,),
                    planner=lambda _: (أثر_الداخل_المرفوض,),
                    applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                    operation_key=_مفتاح("inner-4c"),
                    compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل_المرفوض),),
                )
            رفضٌ.append(2)
            حالةُ_الدولة[effect.resource] = "MUTATED"
    
>       حدّ.execute(
            _طلب(action="gov.case.open", target="gov/case-A"),
            declared_effects=(_أثر("gov/case-A/row"),),
            planner=lambda _: (_أثر("gov/case-A/row"),),
            applier=مطبِّقٌ_مُوالٍ,
            operation_key=_مفتاح("outer-4"),
            compensators=(_معوّض(حالةُ_الدولة, _أثر("gov/case-A/row")),),
        )

tests/sovereignty/test_wi115_nesting_detector.py:316: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
core/sovereignty/enforcement_boundary.py:467: in execute
    ).run_once(
core/sovereignty/idempotency.py:886: in run_once
    return self._run_once_inner(
core/sovereignty/idempotency.py:923: in _run_once_inner
    value = execute()
            ^^^^^^^^^
core/sovereignty/enforcement_boundary.py:448: in _under_permit
    produced = self.policy_enforcement_point.enforce(
core/sovereignty/enforcement.py:377: in enforce
    applier(effect)
core/sovereignty/enforcement_boundary.py:433: in _tracked
    routed(effect)
core/sovereignty/enforcement_boundary.py:723: in route
    applier(effect)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

effect = SovereignEffect(kind=<EffectKind.WRITE: 'WRITE'>, resource='gov/case-A/row', detail='قياس', payload_digest=None)

    def مطبِّقٌ_مُوالٍ(effect: SovereignEffect) -> None:
        # (1) ولدٌ غيرُ مستثنًى: يُرفَضُ
>       with pytest.raises(NestedSovereignCallError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE NestedSovereignCallError

tests/sovereignty/test_wi115_nesting_detector.py:283: Failed
________________ test_السياقيستعادبعدرفضمتعششوالعبورالتالييعمل _________________

حدّ = SovereignExecutionBoundary(gateway=<core.sovereignty.gateway.SovereignGateway object at 0x7f36bc7fec60>, idempotency_l...Journal(path=PosixPath('/tmp/pytest-of-user/pytest-11/test_السياقيستعادبعدرفضمتعششوا0/IDEMPOTENCY.compensation.json')))
حالةُ_الدولة = {'treasury/account-A': 'MUTATED', 'gov/case-A/row': 'NONE', 'tasks/task-A/row': 'NONE'}

    def test_السياقيستعادبعدرفضمتعششوالعبورالتالييعمل(
        حدّ: SovereignExecutionBoundary,
        حالةُ_الدولة: dict[str, str],
    ) -> None:
        """بعدَ عبورٍ رُفِضَ تعشيشُهُ (ورُدَّ أثرُهُ)، السياقُ نظيفٌ والعبورُ التاليُ يعملُ."""
        أثر_الخارجي = _أثر("gov/case-A/row")
        أثر_الداخل = _أثر("treasury/account-A")
        def مطبِّقٌ_يرفض(effect: SovereignEffect) -> None:
            with pytest.raises(NestedSovereignCallError):
                حدّ.execute(
                    _طلب(action="credit_account", target="treasury/account-A"),
                    declared_effects=(أثر_الداخل,),
                    planner=lambda _: (أثر_الداخل,),
                    applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                    operation_key=_مفتاح("inner-5"),
                    compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
                )
            حالةُ_الدولة[effect.resource] = "MUTATED"
    
>       حدّ.execute(
            _طلب(action="gov.case.open", target="gov/case-A"),
            declared_effects=(أثر_الخارجي,),
            planner=lambda _: (أثر_الخارجي,),
            applier=مطبِّقٌ_يرفض,
            operation_key=_مفتاح("outer-5"),
            compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
        )

tests/sovereignty/test_wi115_nesting_detector.py:368: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
core/sovereignty/enforcement_boundary.py:467: in execute
    ).run_once(
core/sovereignty/idempotency.py:886: in run_once
    return self._run_once_inner(
core/sovereignty/idempotency.py:923: in _run_once_inner
    value = execute()
            ^^^^^^^^^
core/sovereignty/enforcement_boundary.py:448: in _under_permit
    produced = self.policy_enforcement_point.enforce(
core/sovereignty/enforcement.py:377: in enforce
    applier(effect)
core/sovereignty/enforcement_boundary.py:433: in _tracked
    routed(effect)
core/sovereignty/enforcement_boundary.py:723: in route
    applier(effect)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

effect = SovereignEffect(kind=<EffectKind.WRITE: 'WRITE'>, resource='gov/case-A/row', detail='قياس', payload_digest=None)

    def مطبِّقٌ_يرفض(effect: SovereignEffect) -> None:
>       with pytest.raises(NestedSovereignCallError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE NestedSovereignCallError

tests/sovereignty/test_wi115_nesting_detector.py:357: Failed
=========================== short test summary info ============================
FAILED tests/sovereignty/test_wi115_nesting_detector.py::test_التعشيشغيرالمستثنىيرفضقبلأيحارسوقبلأيإذن
FAILED tests/sovereignty/test_wi115_nesting_detector.py::test_فتحالقضيةليسبابالكلعبورغيرالمستثن
FAILED tests/sovereignty/test_wi115_nesting_detector.py::test_إطارالأبالباقيبعدالرفضوبعدالعبورالمستثن
FAILED tests/sovereignty/test_wi115_nesting_detector.py::test_السياقيستعادبعدرفضمتعششوالعبورالتالييعمل
4 failed, 3 passed in 0.29s
=== RAW [15] END ===
VERDICT_PER_CRITERION: نطاقُ الجولةِ معيارانِ فقط — (3) الكاشفُ وشقُّ الكاشفِ من (5). المعيارُ (3): نعم — في تشغيلي أنا: الكاشفُ يرفضُ العبورَ السياديَّ داخلَ عبورٍ نشطٍ قبلَ decide وأيِّ قيدٍ (كتلة [7]: 7 passed · وكتلة [14] مسباري الخاص: NESTED_NON_EXEMPT_REFUSED=HELD وNO_DECIDE_NO_LEDGER_FOR_INNER=HELD — سجلُّ البوابةِ للداخلِ 0 وقيدُ الدفترِ None · وكتلة [6]: الرفضُ عندَ رأسِ execute قبلَ كلِّ حارسٍ — السطر 377-378). وopen_case مستثنًى باسمِه استثناءً مسجَّلًا بأزواجٍ مُجمَّدةٍ لا أسماءٍ مفردة (كتلة [9]: NESTED_SOVEREIGN_EXEMPTIONS frozenset {(gov.case.open, task.submit), (gov.case.open, task.cancel)} · وكتلة [7] الزوجُ يمرُّ كاملًا · وكتلة [14]: REGISTERED_PAIRS_PASS=HELD وEXEMPT_INNER_FULLY_DECIDED=HELD — 4 أحكامٍ للداخلِ المستثنى — والاتجاهانِ المعاكسانِ مرفوضانِ: OUTER_NAME_NOT_A_GATE=HELD وINNER_NAME_NOT_A_TICKET=HELD). وشقُّ الكاشفِ من المعيارِ (5): نعم — أعدتُ الطفرةَ بنفسي مرتين: (أ) كتلة [10] شجرةُ ما قبلَ W-685 (bd1dc84b) بلا كاشفٍ مع فحصِ الكاشفِ: فشلٌ في الجمعِ ImportError — دليلُ تاريخٍ مكمِّلٌ فالكاشفُ والفحصُ وليدا الالتزامِ نفسِه 2b814b34 (كتلة [4]) لا إصلاحًا سابقًا. (ب) كتلة [15] طفرةُ كسرِ شرطِ الكاشفِ (if False and) في شجرةِ عملٍ عندَ العقدةِ: سقطت 4 فحوصٍ من 7 بالتأكيدِ الدلاليِّ DID NOT RAISE NestedSovereignCallError — لا بخطأِ استيرادٍ (3 فحوصٍ نجحت) — فالطفرةُ تُكتشَفُ على سلوكِ الكاشفِ نفسِه. المعاييرُ (1) و(2) وشقُّ § 3.5 من (5): خارجةٌ عن نطاقِ حكمي بإفصاحِ المنسِّقِ (عولجت في جولةٍ سابقة) — وكتلة [8] (3 passed) توثيقُ تشغيلٍ لا حكمٌ عليها. المعيارُ (4): مؤجَّلٌ بعرضٍ على المالكِ — لا يدخلُ في هذا الحكمِ ولا VERIFIED للبندِ كلِّه بهذه الجولة.
PROBES: مسبارٌ واحدٌ خاصٌّ من عندي (§ 4.9) — شِفرتُه كتلة [13] (nl -ba) وتشغيلُه كتلة [14] (EXIT 0). الخواصُّ التي حاولَ كسرَها: (أ) تعشيشٌ غيرُ مستثنًى داخلَ إطارٍ نشطٍ — هل يمرُّ بلا NestedSovereignCallError؟ (ب) هل يصلُ الداخلُ المرفوضُ إلى decide أو قيدِ الدفتر؟ (ج) الزوجانِ المُجمَّدانِ — هل يُرفَضانِ خطأً؟ (د) الاستثناءُ أزواجٌ لا أسماء — هل يكفي الاسمُ الخارجيُّ أو الداخليُّ وحدَه؟ (هـ) كسرٌ جديدٌ لم يقِسْهُ فحصُ المنفِّذ: تعشيشٌ عبرَ نسختَينِ مختلفتَينِ من الحدِّ في السياقِ نفسِه (الكشفُ على مستوى الوحدة). (و) بقاءُ إطارِ الأبِ بعدَ ولدٍ مستثنًى واستعادةُ السياقِ بعدَ الأب. انكسرتِ الخاصيّة؟ لا — 12/12 HELD وPROBE RESULT: HELD (EXIT 0). ولا مرورَ لأيِّ تعشيشٍ غيرِ مستثنًى.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — لم أقرأْ شيئًا خارجَ استنساخي (/home/user/workspace/council_w701/kimi_k3/wi115/repo) وهذه الإحاطة: استنسختُ المستودعَ بنفسي من GitHub (git clone https://github.com/vooovg-ui/AMOS-Fedration.git repo) وأعددتُ بيئتَه بـtools/dev/bootstrap.sh وعملتُ داخلَ جذري /home/user/workspace/council_w701/kimi_k3/wi115 وحدَه (raw/ · probe/ · old/ · mutant/ · VERDICT.md). لم أقرأْ نسخةَ المنسِّقِ ولا أدلّةَ المنفِّذِ (W-68*/W-69*/W-70*) ولا عملَ المقاعدِ الأخرى ولا ذاكرةَ جلسةٍ أخرى. استثناءٌ مُعلَنٌ واحد: ظهرت أسماءُ ملفّاتِ أدلّةِ W-685 عرضًا في مخرجِ الأمرِ 5 (git show --stat 2b814b34 — أمرُ معيارٍ من الإحاطة) ولم أفتحْها. مصادرُ الحكمِ كلُّها من إعادةِ تشغيلي أنا.
VERDICT: PASS — المعيارُ (3) وشقُّ الكاشفِ من المعيارِ (5) تحقَّقا في تشغيلي أنا عندَ العقدةِ 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247: الكاشفُ يرفضُ قبلَ decide وأيِّ قيدٍ (7/7) وopen_case مستثنًى بأزواجٍ مُجمَّدةٍ وطفرةُ الكاشفِ تُكتشَفُ دلاليًّا (4 فحوصٍ سقطت بـDID NOT RAISE) ومسباري الخاصُّ صمدَ 12/12 — ولا VERIFIED للبندِ كلِّه بهذه الجولة (المعيارُ (4) مؤجَّلٌ بعرضٍ على المالك).
