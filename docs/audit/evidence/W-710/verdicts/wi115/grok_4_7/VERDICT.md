# حكمُ مقعدِ المجلسِ — grok_4_7 · جولةُ WI-115 (W-710)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في الجولةِ الواحدةِ (قرارُ المالكِ D27) على WI-115 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w701/grok_4_7/wi115) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `7e7b6fdc387ed2a190f7dd0dd9f4117f62f7f9e4ef1b7af9298ede8e87b97dff`).

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
MODEL: grok_4_7
FAMILY: grok
RUN_DATE: 2026-10-28 06:51 +00:00
NODE: 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
CLONE_PATH: /home/user/workspace/council_w701/grok_4_7/wi115/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/
 2. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/)
 3. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git log --format='%h %cI %s' -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
 5. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git show --stat 2b814b34
 6. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git diff 2b814b34^ 2b814b34 -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py
 7. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
 8. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
 9. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && rg -n "NESTED_SOVEREIGN_EXEMPTIONS|NestedSovereignCallError|open_case" core/sovereignty/enforcement_boundary.py
 10. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && rm -rf ../old && git worktree add --detach ../old 2b814b34^ && cp tests/sovereignty/test_wi115_nesting_detector.py ../old/tests/sovereignty/ && cd ../old && /home/user/workspace/council_w701/grok_4_7/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
 11. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && sha256sum docs/audit/evidence/W-701/briefs_wi115/briefing_grok_4_7.md
 12. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && cat docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS
 13. nl -ba /home/user/workspace/council_w701/grok_4_7/wi115/probe/seat_probe_wi115.py
 14. cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && .venv/bin/python /home/user/workspace/council_w701/grok_4_7/wi115/probe/seat_probe_wi115.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/)
EXIT: 0
BYTES: 1025
SHA256: 2cc661a1add06f3fab16140029ff6f753ea8cffd16df1fa15f04397d19e82a87
NO_EOL: 0
--- OUTPUT ---
HEAD is now at 147a0c6b W-701: توجيهُ المستشارِ 25 — قراراتُ المالكِ D27 بنصّها (إغلاقُ WI-113/WI-117/WI-119 بعدَ VERIFIED بإجماعٍ دونَ سؤالٍ جديدٍ · الجولةُ الآنَ لا بعدَ G1 — جولةٌ واحدةٌ بثلاثةِ نطاقاتٍ تُجمَعُ في الجلسةِ نفسِها Q-72) + واجبُ N+1 لـPR #168 (قراءةُ التشغيلِ 40478049851 بالفاحصِ فعلًا: مقروءٌ أخضرُ 13/13 على 129bed06 · EXIT 0) + انتقالٌ واحدٌ: WI-119 IN_PROGRESS→IN_REVIEW + إحاطاتُ الجولةِ التسعُ مبصومةً (3 مقاعدٍ × WI-117/WI-119/الكاشفُ من WI-115 · gemini · grok · kimi) ونصوصُ الإطلاقِ حرفيًّا وقياساتُ الجلسةِ خامًا (حوكمةُ الأعمالِ ✓ · راتشيتٌ 61 · حزمةُ الحوكمةِ 1394 خضراءَ) · لا شِّفرةَ سلوكيّةً · المنسِّقُ GLM-5.3 (Perplexity Computer)
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git log --format='%h %cI %s' -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
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
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git show --stat 2b814b34
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
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && git diff 2b814b34^ 2b814b34 -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py
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
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
EXIT: 0
BYTES: 776
SHA256: cc930b84f2524b7234ef126075b4f95cef2077c236e6f15426b6cd0bc18f1ebb
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/grok_4_7/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
.......                                                                  [100%]
7 passed in 0.17s
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
EXIT: 0
BYTES: 1391
SHA256: f8d087c62de5607079265cac33981666d2eb20de25290b53309fb1ddd7992298
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/grok_4_7/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/grok_4_7/wi115/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 3 items

federal/executive/services/tests/test_wi115_reversed_replay.py ..        [ 66%]
federal/executive/services/tests/test_wi115_nesting_compensator_frame.py . [100%]

============================== 3 passed in 1.51s ===============================
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && rg -n "NESTED_SOVEREIGN_EXEMPTIONS|NestedSovereignCallError|open_case" core/sovereignty/enforcement_boundary.py
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
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && rm -rf ../old && git worktree add --detach ../old 2b814b34^ && cp tests/sovereignty/test_wi115_nesting_detector.py ../old/tests/sovereignty/ && cd ../old && /home/user/workspace/council_w701/grok_4_7/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
EXIT: 2
BYTES: 2036
SHA256: 7a82b603ad4d28e95c4886797f8089a21e795bc43b5778cf1d33c1af7fe48a3f
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD bd1dc84b)
HEAD is now at bd1dc84b W-684: إعادةُ توليدِ مصفوفةِ الحقيقةِ (ملفّاتٌ مُعفاةٌ وحدَها)
/home/user/workspace/council_w701/grok_4_7/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

==================================== ERRORS ====================================
______ ERROR collecting tests/sovereignty/test_wi115_nesting_detector.py _______
ImportError while importing test module '/home/user/workspace/council_w701/grok_4_7/wi115/old/tests/sovereignty/test_wi115_nesting_detector.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/uv/python/cpython-3.12.15-linux-x86_64-gnu/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/sovereignty/test_wi115_nesting_detector.py:35: in <module>
    from core.sovereignty.enforcement_boundary import (
E   ImportError: cannot import name 'NestedSovereignCallError' from 'core.sovereignty.enforcement_boundary' (/home/user/workspace/council_w701/grok_4_7/wi115/old/core/sovereignty/enforcement_boundary.py)
=========================== short test summary info ============================
ERROR tests/sovereignty/test_wi115_nesting_detector.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && sha256sum docs/audit/evidence/W-701/briefs_wi115/briefing_grok_4_7.md
EXIT: 0
BYTES: 126
SHA256: 5d0185006b2929428d755cbd4ec6f9a4a6746a2dd80d8de66be604c49566548e
NO_EOL: 0
--- OUTPUT ---
5fda37e5742b405f044202c1d1e8b95e113e058c4424bd9b5b68fb76cf0f3f20  docs/audit/evidence/W-701/briefs_wi115/briefing_grok_4_7.md
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && cat docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w701/grok_4_7/wi115/probe/seat_probe_wi115.py
EXIT: 0
BYTES: 19524
SHA256: 1e38358a309316d805745ea9ef0fb4990b3e6ffa3d532deafccf837753e4388d
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ مقعدِ grok_4_7 لـ WI-115 — ليسَ أمرًا من (ج) ولا نسخةً من فحصٍ قائم.
     3	
     4	ينادي حدَّ التنفيذِ الإنتاجيَّ (SovereignExecutionBoundary.execute) ويحاولُ
     5	كسرَ الخاصيّةِ المُدَّعاةِ: رفضُ عبورٍ سياديٍّ غيرِ مستثنًى داخلَ عبورٍ نشطٍ
     6	قبلَ decide، ومرورُ الزوجينِ المجمَّدينِ لـ open_case وحدَهما.
     7	
     8	ثمَّ يُسقِطُ فحصَ الكاشفِ (لا الصنفَ) في شجرةِ عملٍ منفصلةٍ ويُشغِّلُ فحصَ
     9	الشجرةِ ليُحكَمَ هل السقوطُ على تأكيدِ الكاشفِ لا على خطأِ استيراد.
    10	"""
    11	
    12	from __future__ import annotations
    13	
    14	import subprocess
    15	import sys
    16	import textwrap
    17	from pathlib import Path
    18	
    19	REPO = Path("/home/user/workspace/council_w701/grok_4_7/wi115/repo")
    20	PY = REPO / ".venv/bin/python"
    21	MUTANT = Path("/home/user/workspace/council_w701/grok_4_7/wi115/mutant")
    22	sys.path.insert(0, str(REPO))
    23	
    24	from cryptography.hazmat.primitives.asymmetric import ed25519  # noqa: E402
    25	
    26	from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
    27	from core.constitutional_engine.ledger import ConstitutionalLedger  # noqa: E402
    28	from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402
    29	from core.sovereignty.compensation import Compensator  # noqa: E402
    30	from core.sovereignty.contract import EffectKind, SovereignEffect  # noqa: E402
    31	from core.sovereignty.enforcement import ConsumedPermitLedger  # noqa: E402
    32	from core.sovereignty.enforcement_boundary import (  # noqa: E402
    33	    NESTED_SOVEREIGN_EXEMPTIONS,
    34	    NestedSovereignCallError,
    35	    SovereignExecutionBoundary,
    36	    _active_crossing,
    37	)
    38	from core.sovereignty.gateway import SovereignGateway  # noqa: E402
    39	from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger  # noqa: E402
    40	from core.sovereignty.outbox import OutboxLedger, SovereignOutbox  # noqa: E402
    41	
    42	EXPECTED_PAIRS = frozenset(
    43	    {
    44	        ("gov.case.open", "task.submit"),
    45	        ("gov.case.open", "task.cancel"),
    46	    }
    47	)
    48	CHECK_MARKER = (
    49	    "if outer_crossing is not None and "
    50	    "(outer_crossing[0], request.action) not in NESTED_SOVEREIGN_EXEMPTIONS:"
    51	)
    52	
    53	failures: list[str] = []
    54	seq = 0
    55	
    56	
    57	def note(ok: bool, name: str, detail: str) -> None:
    58	    mark = "HOLD" if ok else "BROKEN"
    59	    print(f"[{mark}] {name}: {detail}")
    60	    if not ok:
    61	        failures.append(f"{name}: {detail}")
    62	
    63	
    64	def fresh(tmp: Path, tag: str) -> tuple[SovereignExecutionBoundary, SovereignGateway, IdempotencyLedger, dict[str, int]]:
    65	    gateway = SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(tmp / f"{tag}-l.jsonl")))
    66	    ledger = IdempotencyLedger(tmp / f"{tag}-idem.json")
    67	    outbox = SovereignOutbox(
    68	        ledger=OutboxLedger(tmp / f"{tag}-out.json"),
    69	        verifying_key=ed25519.Ed25519PublicKey.from_public_bytes(bytes.fromhex(gateway.verifying_key_hex)),
    70	    )
    71	    boundary = SovereignExecutionBoundary(
    72	        gateway=gateway,
    73	        idempotency_ledger=ledger,
    74	        outbox=outbox,
    75	        consumed_permits=ConsumedPermitLedger(tmp / f"{tag}-cons.json"),
    76	    )
    77	    seen: dict[str, int] = {}
    78	    original = gateway.decide
    79	
    80	    def counting(request: ActionRequest, **kwargs: object) -> object:
    81	        if seen.get("__explode__"):
    82	            raise RuntimeError("decide-reached")
    83	        seen[request.action] = seen.get(request.action, 0) + 1
    84	        return original(request, declared_effects=kwargs["declared_effects"])
    85	
    86	    gateway.decide = counting  # type: ignore[method-assign]
    87	    return boundary, gateway, ledger, seen
    88	
    89	
    90	def effect(resource: str) -> SovereignEffect:
    91	    return SovereignEffect(kind=EffectKind.WRITE, resource=resource, detail="seat-probe")
    92	
    93	
    94	def compensator(effect_obj: SovereignEffect) -> Compensator:
    95	    return Compensator(
    96	        effect_signature=effect_obj.signature,
    97	        apply=lambda: None,
    98	        description="seat-probe no-op compensator",
    99	    )
   100	
   101	
   102	def key(value: str) -> IdempotencyKey:
   103	    return IdempotencyKey(scope="seat-probe", value=value)
   104	
   105	
   106	def request(action: str, target: str) -> ActionRequest:
   107	    return ActionRequest(actor=Branch.EXECUTIVE, action=action, target=target, channel="official")
   108	
   109	
   110	def run_cross(
   111	    boundary: SovereignExecutionBoundary,
   112	    action: str,
   113	    target: str,
   114	    key_value: str,
   115	    applier,
   116	) -> object:
   117	    written = effect(f"{target}/row")
   118	    return boundary.execute(
   119	        request(action, target),
   120	        declared_effects=(written,),
   121	        planner=lambda _permit: (written,),
   122	        applier=applier,
   123	        operation_key=key(key_value),
   124	        compensators=(compensator(written),),
   125	    )
   126	
   127	
   128	def next_id(prefix: str) -> str:
   129	    global seq
   130	    seq += 1
   131	    return f"{prefix}-{seq}"
   132	
   133	
   134	def attack_live(tmp: Path) -> None:
   135	    print("=== LIVE ATTACKS ===")
   136	    print(f"module={sys.modules['core.sovereignty.enforcement_boundary'].__file__}")
   137	    print(f"pairs={sorted(NESTED_SOVEREIGN_EXEMPTIONS)}")
   138	    note(
   139	        NESTED_SOVEREIGN_EXEMPTIONS == EXPECTED_PAIRS,
   140	        "frozen-pairs-exact",
   141	        f"got={sorted(NESTED_SOVEREIGN_EXEMPTIONS)}",
   142	    )
   143	    note(isinstance(NESTED_SOVEREIGN_EXEMPTIONS, frozenset), "frozen-type", type(NESTED_SOVEREIGN_EXEMPTIONS).__name__)
   144	
   145	    boundary, _gateway, ledger, seen = fresh(tmp, "live")
   146	
   147	    def nest(inner_action: str, inner_target: str, inner_key: str) -> BaseException | None:
   148	        try:
   149	            run_cross(boundary, inner_action, inner_target, inner_key, lambda _e: None)
   150	        except BaseException as exc:  # noqa: BLE001 — المسبارُ يصنّفُ كلَّ رفض
   151	            return exc
   152	        return None
   153	
   154	    # 1) تعشيشٌ غيرُ مستثنًى، وdecide مُفخَّخ: إن وُصلَ decide فالخاصيّةُ انكسرت.
   155	    outer_target = next_id("probe/open")
   156	    inner_target = next_id("probe/credit")
   157	    inner_key = next_id("inner-credit")
   158	    reached = {"applier": False, "exc": None}
   159	
   160	    def applier_explode(_effect: SovereignEffect) -> None:
   161	        reached["applier"] = True
   162	        seen["__explode__"] = 1
   163	        before = seen.get("credit_account", 0)
   164	        reached["exc"] = nest("credit_account", inner_target, inner_key)
   165	        seen["__explode__"] = 0
   166	        reached["decide_delta"] = seen.get("credit_account", 0) - before
   167	
   168	    run_cross(boundary, "gov.case.open", outer_target, next_id("outer-open"), applier_explode)
   169	    exc = reached["exc"]
   170	    note(reached["applier"] is True, "nonexempt-applier-ran", str(reached["applier"]))
   171	    note(
   172	        isinstance(exc, NestedSovereignCallError),
   173	        "nonexempt-rejected",
   174	        f"type={type(exc).__name__} msg={exc}",
   175	    )
   176	    note(
   177	        not isinstance(exc, RuntimeError),
   178	        "nonexempt-before-decide",
   179	        f"decide_delta={reached.get('decide_delta')} exc={type(exc).__name__}",
   180	    )
   181	    note(ledger.get(key(inner_key)) is None, "nonexempt-no-ledger", "inner key absent" if ledger.get(key(inner_key)) is None else "LEDGER WROTE")
   182	    note(_active_crossing.get() is None, "frame-reset-after-outer", repr(_active_crossing.get()))
   183	
   184	    # 2) الزوجانِ المجمَّدانِ يمرّانِ (يبلغانِ decide) ولا يُرفضانِ بالكاشف.
   185	    for inner_action in ("task.submit", "task.cancel"):
   186	        passed = {"exc": None, "decide": 0, "applier": False}
   187	
   188	        def applier_exempt(_effect: SovereignEffect, action: str = inner_action) -> None:
   189	            passed["applier"] = True
   190	            before = seen.get(action, 0)
   191	            target = next_id(f"probe/{action.replace('.', '-')}")
   192	            passed["exc"] = nest(action, target, next_id(f"key-{action}"))
   193	            passed["decide"] = seen.get(action, 0) - before
   194	
   195	        run_cross(
   196	            boundary,
   197	            "gov.case.open",
   198	            next_id("probe/open-exempt"),
   199	            next_id(f"outer-{inner_action}"),
   200	            applier_exempt,
   201	        )
   202	        note(passed["applier"] is True, f"exempt-{inner_action}-attempted", "applier ran")
   203	        note(
   204	            not isinstance(passed["exc"], NestedSovereignCallError) and passed["decide"] >= 1,
   205	            f"exempt-{inner_action}-passed-not-rejected",
   206	            f"exc={type(passed['exc']).__name__ if passed['exc'] else None} decide={passed['decide']}",
   207	        )
   208	
   209	    # 3) انتحالُ الاسمِ وعكسُ الزوجِ واللاحقةِ والحفيدُ ونسختانِ والفعلُ نفسُه.
   210	    attacks = [
   211	        ("name-spoof-open_case", "gov.case.open", "open_case"),
   212	        ("suffix-spoof", "gov.case.open", "task.submit "),
   213	        ("prefix-spoof", "gov.case.open", "xtask.submit"),
   214	        ("case-spoof", "Gov.case.open", "task.submit"),
   215	        ("reverse-pair", "task.submit", "gov.case.open"),
   216	        ("same-action-nest", "credit_account", "credit_account"),
   217	        ("open-inside-credit", "credit_account", "gov.case.open"),
   218	        ("whitespace-outer-pair", "gov.case.open ", "task.submit"),
   219	    ]
   220	    for name, outer_action, inner_action in attacks:
   221	        bag = {"exc": None, "applier": False}
   222	
   223	        def applier_reject(_effect: SovereignEffect, inner: str = inner_action, slot: dict = bag) -> None:
   224	            slot["applier"] = True
   225	            slot["exc"] = nest(inner, next_id("probe/spoof"), next_id("spoof-key"))
   226	
   227	        run_cross(boundary, outer_action, next_id("probe/outer"), next_id("outer-spoof"), applier_reject)
   228	        note(bag["applier"] is True, f"{name}-attempted", "applier ran")
   229	        note(
   230	            isinstance(bag["exc"], NestedSovereignCallError),
   231	            f"{name}-rejected",
   232	            f"type={type(bag['exc']).__name__}",
   233	        )
   234	
   235	    # 4) نسختانِ مختلفتانِ منَ الحدِّ في السياقِ نفسِه — الإطارُ على مستوى الوحدة.
   236	    other, _g2, ledger2, seen2 = fresh(tmp, "other")
   237	    bag2 = {"exc": None}
   238	
   239	    def applier_other(_effect: SovereignEffect) -> None:
   240	        seen2["__explode__"] = 1
   241	        inner_target = next_id("probe/other-credit")
   242	        inner_key = next_id("other-key")
   243	        try:
   244	            run_cross(other, "credit_account", inner_target, inner_key, lambda _e: None)
   245	            bag2["exc"] = None
   246	        except BaseException as exc:  # noqa: BLE001
   247	            bag2["exc"] = exc
   248	        finally:
   249	            seen2["__explode__"] = 0
   250	        bag2["ledger"] = ledger2.get(key(inner_key))
   251	
   252	    run_cross(boundary, "gov.case.open", next_id("probe/open-other"), next_id("outer-other"), applier_other)
   253	    note(
   254	        isinstance(bag2["exc"], NestedSovereignCallError) and bag2.get("ledger") is None,
   255	        "cross-instance-rejected-before-decide",
   256	        f"type={type(bag2['exc']).__name__} ledger={bag2.get('ledger')}",
   257	    )
   258	
   259	    # 5) حفيدٌ غيرُ مستثنًى داخلَ الزوجِ المُعفى، ثمَّ رفضٌ ثانٍ بعدَ عودةِ الولدِ.
   260	    bag3 = {"grand": None, "after": None, "submit_exc": None}
   261	
   262	    def applier_grand(inner_boundary: SovereignExecutionBoundary = boundary) -> None:
   263	        def inner_applier(_effect: SovereignEffect) -> None:
   264	            bag3["grand"] = nest("credit_account", next_id("probe/grand"), next_id("grand-key"))
   265	
   266	        submit_target = next_id("probe/submit")
   267	        try:
   268	            run_cross(inner_boundary, "task.submit", submit_target, next_id("submit-key"), inner_applier)
   269	            bag3["submit_exc"] = None
   270	        except BaseException as exc:  # noqa: BLE001
   271	            bag3["submit_exc"] = exc
   272	        bag3["after"] = nest("credit_account", next_id("probe/after"), next_id("after-key"))
   273	
   274	    run_cross(boundary, "gov.case.open", next_id("probe/open-grand"), next_id("outer-grand"), lambda e: applier_grand())
   275	    note(
   276	        bag3["submit_exc"] is None and isinstance(bag3["grand"], NestedSovereignCallError),
   277	        "grandchild-under-exempt-rejected",
   278	        f"submit={type(bag3['submit_exc']).__name__ if bag3['submit_exc'] else None} grand={type(bag3['grand']).__name__}",
   279	    )
   280	    note(
   281	        isinstance(bag3["after"], NestedSovereignCallError),
   282	        "parent-frame-survives-exempt-child",
   283	        f"after={type(bag3['after']).__name__}",
   284	    )
   285	    note(_active_crossing.get() is None, "frame-clean-at-end", repr(_active_crossing.get()))
   286	
   287	    # 6) عبورٌ تالٍ على الجذرِ (لا تعشيش) يعملُ — الاستعادةُ لم تُسمِّم السياق.
   288	    follow_exc = None
   289	    try:
   290	        run_cross(boundary, "credit_account", next_id("probe/follow"), next_id("follow-key"), lambda _e: None)
   291	    except BaseException as exc:  # noqa: BLE001
   292	        follow_exc = exc
   293	    note(follow_exc is None, "sequential-after-nests-works", f"exc={type(follow_exc).__name__ if follow_exc else None}")
   294	
   295	
   296	def mutate_and_measure() -> None:
   297	    print("=== MUTATION: delete detector check, keep class ===")
   298	    if MUTANT.exists():
   299	        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(MUTANT)], check=False)
   300	        subprocess.run(["rm", "-rf", str(MUTANT)], check=False)
   301	    subprocess.run(["git", "-C", str(REPO), "worktree", "prune"], check=True)
   302	    add = subprocess.run(
   303	        ["git", "-C", str(REPO), "worktree", "add", "--detach", str(MUTANT), "HEAD"],
   304	        check=False,
   305	        text=True,
   306	        capture_output=True,
   307	    )
   308	    print(add.stdout)
   309	    print(add.stderr)
   310	    if add.returncode != 0:
   311	        note(False, "mutant-worktree", add.stderr.strip() or add.stdout.strip())
   312	        return
   313	    target = MUTANT / "core/sovereignty/enforcement_boundary.py"
   314	    source = target.read_text(encoding="utf-8")
   315	    if CHECK_MARKER not in source:
   316	        note(False, "mutant-marker", "detector check marker missing — mutation not applied")
   317	        return
   318	    start = source.index("        outer_crossing = _active_crossing.get()")
   319	    end = source.index("        token = _active_crossing.set", start)
   320	    mutated = (
   321	        source[:start]
   322	        + "        # MUTATION seat grok_4_7: فحصُ الكاشفِ محذوفٌ، والصنفُ والاستثناءُ باقيان.\n"
   323	        + source[end:]
   324	    )
   325	    if CHECK_MARKER in mutated or "raise NestedSovereignCallError(" in mutated:
   326	        note(False, "mutant-patch", "raise or check still present after patch")
   327	        return
   328	    if "class NestedSovereignCallError" not in mutated:
   329	        note(False, "mutant-class-kept", "class was removed — this would be an import error, not a detector assertion")
   330	        return
   331	    target.write_text(mutated, encoding="utf-8")
   332	    print("patched detector check out; class NestedSovereignCallError kept")
   333	
   334	    inline = textwrap.dedent(
   335	        """
   336	        import sys
   337	        from pathlib import Path
   338	        sys.path.insert(0, str(Path(".").resolve()))
   339	        import core.sovereignty.enforcement_boundary as boundary
   340	        print("MUTANT_MODULE", boundary.__file__)
   341	        print("HAS_RAISE", "raise NestedSovereignCallError(" in Path(boundary.__file__).read_text(encoding="utf-8"))
   342	        print("HAS_CLASS", hasattr(boundary, "NestedSovereignCallError"))
   343	        """
   344	    )
   345	    shown = subprocess.run([str(PY), "-c", inline], cwd=MUTANT, text=True, capture_output=True)
   346	    print(shown.stdout)
   347	    print(shown.stderr)
   348	    proc = subprocess.run(
   349	        [
   350	            str(PY),
   351	            "-m",
   352	            "pytest",
   353	            "-q",
   354	            "-p",
   355	            "no:cacheprovider",
   356	            "--tb=line",
   357	            "tests/sovereignty/test_wi115_nesting_detector.py",
   358	        ],
   359	        cwd=MUTANT,
   360	        text=True,
   361	        capture_output=True,
   362	    )
   363	    print("--- MUTANT PYTEST STDOUT ---")
   364	    print(proc.stdout)
   365	    print("--- MUTANT PYTEST STDERR ---")
   366	    print(proc.stderr)
   367	    print(f"MUTANT_PYTEST_EXIT={proc.returncode}")
   368	    combined = proc.stdout + "\n" + proc.stderr
   369	    import_error = "cannot import name 'NestedSovereignCallError'" in combined
   370	    did_not_raise = "DID NOT RAISE" in combined
   371	    failed = proc.returncode != 0 and "failed" in combined and not import_error
   372	    note(not import_error, "mutation-not-import-error", "ImportError" if import_error else "no NestedSovereignCallError import error")
   373	    note(did_not_raise, "mutation-failed-on-detector-assertion", "DID NOT RAISE present" if did_not_raise else "DID NOT RAISE absent")
   374	    note(failed, "mutation-detected-by-existing-tests", f"exit={proc.returncode}")
   375	
   376	
   377	def main() -> int:
   378	    import tempfile
   379	
   380	    with tempfile.TemporaryDirectory(prefix="wi115-seat-") as raw:
   381	        attack_live(Path(raw))
   382	    mutate_and_measure()
   383	    print("=== PROBE SUMMARY ===")
   384	    print(f"BROKEN_COUNT={len(failures)}")
   385	    for item in failures:
   386	        print(f"BROKEN {item}")
   387	    if failures:
   388	        print("PROBE_RESULT=FAIL")
   389	        return 1
   390	    print("PROBE_RESULT=PASS")
   391	    return 0
   392	
   393	
   394	if __name__ == "__main__":
   395	    sys.exit(main())
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi115/repo && .venv/bin/python /home/user/workspace/council_w701/grok_4_7/wi115/probe/seat_probe_wi115.py
EXIT: 0
BYTES: 6308
SHA256: ff3aa79cea9ae23653958e52c051904dc7104f486b6bce0ba2171469de216ea9
NO_EOL: 0
--- OUTPUT ---
=== LIVE ATTACKS ===
module=/home/user/workspace/council_w701/grok_4_7/wi115/repo/core/sovereignty/enforcement_boundary.py
pairs=[('gov.case.open', 'task.cancel'), ('gov.case.open', 'task.submit')]
[HOLD] frozen-pairs-exact: got=[('gov.case.open', 'task.cancel'), ('gov.case.open', 'task.submit')]
[HOLD] frozen-type: frozenset
[HOLD] nonexempt-applier-ran: True
[HOLD] nonexempt-rejected: type=NestedSovereignCallError msg=عبورٌ سياديٌّ داخلَ عبورٍ نشطٍ: الفعلُ 'credit_account' داخلَ إطارِ 'gov.case.open' — التعشيشُ السياديُّ ممنوعٌ (WI-115 · Q-9) والزوجُ ليسَ منَ الاستثناءِ المسجَّلِ (open_case باسمِه وحدَه).
[HOLD] nonexempt-before-decide: decide_delta=0 exc=NestedSovereignCallError
[HOLD] nonexempt-no-ledger: inner key absent
[HOLD] frame-reset-after-outer: None
[HOLD] exempt-task.submit-attempted: applier ran
[HOLD] exempt-task.submit-passed-not-rejected: exc=None decide=1
[HOLD] exempt-task.cancel-attempted: applier ran
[HOLD] exempt-task.cancel-passed-not-rejected: exc=None decide=1
[HOLD] name-spoof-open_case-attempted: applier ran
[HOLD] name-spoof-open_case-rejected: type=NestedSovereignCallError
[HOLD] suffix-spoof-attempted: applier ran
[HOLD] suffix-spoof-rejected: type=NestedSovereignCallError
[HOLD] prefix-spoof-attempted: applier ran
[HOLD] prefix-spoof-rejected: type=NestedSovereignCallError
[HOLD] case-spoof-attempted: applier ran
[HOLD] case-spoof-rejected: type=NestedSovereignCallError
[HOLD] reverse-pair-attempted: applier ran
[HOLD] reverse-pair-rejected: type=NestedSovereignCallError
[HOLD] same-action-nest-attempted: applier ran
[HOLD] same-action-nest-rejected: type=NestedSovereignCallError
[HOLD] open-inside-credit-attempted: applier ran
[HOLD] open-inside-credit-rejected: type=NestedSovereignCallError
[HOLD] whitespace-outer-pair-attempted: applier ran
[HOLD] whitespace-outer-pair-rejected: type=NestedSovereignCallError
[HOLD] cross-instance-rejected-before-decide: type=NestedSovereignCallError ledger=None
[HOLD] grandchild-under-exempt-rejected: submit=None grand=NestedSovereignCallError
[HOLD] parent-frame-survives-exempt-child: after=NestedSovereignCallError
[HOLD] frame-clean-at-end: None
[HOLD] sequential-after-nests-works: exc=None
=== MUTATION: delete detector check, keep class ===
HEAD is now at 147a0c6b W-701: توجيهُ المستشارِ 25 — قراراتُ المالكِ D27 بنصّها (إغلاقُ WI-113/WI-117/WI-119 بعدَ VERIFIED بإجماعٍ دونَ سؤالٍ جديدٍ · الجولةُ الآنَ لا بعدَ G1 — جولةٌ واحدةٌ بثلاثةِ نطاقاتٍ تُجمَعُ في الجلسةِ نفسِها Q-72) + واجبُ N+1 لـPR #168 (قراءةُ التشغيلِ 40478049851 بالفاحصِ فعلًا: مقروءٌ أخضرُ 13/13 على 129bed06 · EXIT 0) + انتقالٌ واحدٌ: WI-119 IN_PROGRESS→IN_REVIEW + إحاطاتُ الجولةِ التسعُ مبصومةً (3 مقاعدٍ × WI-117/WI-119/الكاشفُ من WI-115 · gemini · grok · kimi) ونصوصُ الإطلاقِ حرفيًّا وقياساتُ الجلسةِ خامًا (حوكمةُ الأعمالِ ✓ · راتشيتٌ 61 · حزمةُ الحوكمةِ 1394 خضراءَ) · لا شِّفرةَ سلوكيّةً · المنسِّقُ GLM-5.3 (Perplexity Computer)

Preparing worktree (detached HEAD 147a0c6b)

patched detector check out; class NestedSovereignCallError kept
MUTANT_MODULE /home/user/workspace/council_w701/grok_4_7/wi115/mutant/core/sovereignty/enforcement_boundary.py
HAS_RAISE False
HAS_CLASS True


--- MUTANT PYTEST STDOUT ---
F.FF.F.                                                                  [100%]
=================================== FAILURES ===================================
E   Failed: DID NOT RAISE NestedSovereignCallError
/home/user/workspace/council_w701/grok_4_7/wi115/mutant/tests/sovereignty/test_wi115_nesting_detector.py:159: Failed: DID NOT RAISE NestedSovereignCallError
E   Failed: DID NOT RAISE NestedSovereignCallError
/home/user/workspace/council_w701/grok_4_7/wi115/mutant/tests/sovereignty/test_wi115_nesting_detector.py:248: Failed: DID NOT RAISE NestedSovereignCallError
E   Failed: DID NOT RAISE NestedSovereignCallError
/home/user/workspace/council_w701/grok_4_7/wi115/mutant/tests/sovereignty/test_wi115_nesting_detector.py:283: Failed: DID NOT RAISE NestedSovereignCallError
E   Failed: DID NOT RAISE NestedSovereignCallError
/home/user/workspace/council_w701/grok_4_7/wi115/mutant/tests/sovereignty/test_wi115_nesting_detector.py:357: Failed: DID NOT RAISE NestedSovereignCallError
=========================== short test summary info ============================
FAILED tests/sovereignty/test_wi115_nesting_detector.py::test_التعشيشغيرالمستثنىيرفضقبلأيحارسوقبلأيإذن
FAILED tests/sovereignty/test_wi115_nesting_detector.py::test_فتحالقضيةليسبابالكلعبورغيرالمستثن
FAILED tests/sovereignty/test_wi115_nesting_detector.py::test_إطارالأبالباقيبعدالرفضوبعدالعبورالمستثن
FAILED tests/sovereignty/test_wi115_nesting_detector.py::test_السياقيستعادبعدرفضمتعششوالعبورالتالييعمل
4 failed, 3 passed in 0.13s

--- MUTANT PYTEST STDERR ---
/home/user/workspace/council_w701/grok_4_7/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

MUTANT_PYTEST_EXIT=1
[HOLD] mutation-not-import-error: no NestedSovereignCallError import error
[HOLD] mutation-failed-on-detector-assertion: DID NOT RAISE present
[HOLD] mutation-detected-by-existing-tests: exit=1
=== PROBE SUMMARY ===
BROKEN_COUNT=0
PROBE_RESULT=PASS
=== RAW [14] END ===
VERDICT_PER_CRITERION: (1) خارجُ نطاقِ هذه الجولة — لا يُحكَم ولا يُدَّعى. الإحاطةُ تُخرجُ المعيارين (1) و(2) من حكمِ هذا المقعد (جولةٌ سابقة). لم أُعِد قياسَ وثيقةِ التصميم.
(2) خارجُ نطاقِ هذه الجولة — لا يُحكَم ولا يُدَّعى. الأمرُ 8 EXIT 0 (3 passed) تشغيلٌ مطلوبٌ لا سندُ حكمٍ على إصلاحِ § 3.5 في هذه الجولة.
(3) نعم. الكاشفُ في core/sovereignty/enforcement_boundary.py يرفعُ NestedSovereignCallError قبلَ أيِّ حارسٍ وقبلَ gateway.decide، والاستثناءُ المسجَّلُ زوجانِ مجمَّدان لا اسمٌ مفرد: (gov.case.open, task.submit) و(gov.case.open, task.cancel) — الأمرُ 9 والأمرُ 6. فحصُ الشجرةِ tests/sovereignty/test_wi115_nesting_detector.py: 7 passed EXIT 0 (الأمرُ 7). المسبارُ الخاصُّ (الكتلةُ 14 · EXIT 0 · PROBE_RESULT=PASS · BROKEN_COUNT=0) نادى SovereignExecutionBoundary.execute على الشِّفرةِ الإنتاجيّةِ وحاولَ الكسر: credit_account داخلَ gov.case.open رُفضَ بـNestedSovereignCallError وdecide_delta=0 رغمَ تفخيخِ decide بـRuntimeError("decide-reached") وبلا قيدٍ في الدفتر؛ task.submit وtask.cancel داخلَ gov.case.open بلغا decide (decide=1) ولم يُرفضا؛ وانتحالُ الاسمِ open_case واللاحقةُ والبادئةُ وحالةُ الأحرفِ والمسافةُ وعكسُ الزوجِ وتعشيشُ الفعلِ نفسِه وgov.case.open داخلَ credit_account ونسخةٌ ثانيةٌ منَ الحدِّ في السياقِ نفسِه وحفيدُ credit_account تحتَ task.submit المُعفى رُفضت كلُّها بـNestedSovereignCallError؛ وإطارُ الأبِ بقِيَ بعدَ الولدِ المستثنى ثمَّ استُعيد (_active_crossing is None) وعملَ عبورٌ تالٍ على الجذر. الخاصيّةُ لم تنكسر.
(4) لا — مؤجَّلٌ بعرضٍ على المالكِ (تعارضٌ مقيسٌ مع حرسِ Q-32) وخارجُ نطاقِ هذه الجولة. لا يُدَّعى تحققُه ولا VERIFIED للبندِ كلِّه.
(5) شقُّ الكاشفِ: نعم. الأمرُ 10 (شجرةُ 2b814b34^ مع نسخِ فحصِ الكاشفِ) EXIT 2 على ImportError: cannot import name 'NestedSovereignCallError' — سقوطٌ على الاستيرادِ لا على تأكيدِ الكاشف، فالدليلُ التاريخيُّ مكمِّلٌ لا كافٍ وحدَه كما أعلنتِ الإحاطة. في المسبارِ (الكتلةُ 14) أُسقطَ فحصُ الكاشفِ وحدَه في شجرةِ mutant عندَ العقدةِ (الصنفُ NestedSovereignCallError والاستثناءُ المجمَّدُ باقيان · HAS_RAISE False · HAS_CLASS True · الوحدةُ من mutant لا من الاستنساخ) ثمَّ شُغِّلَ فحصُ الشجرةِ: MUTANT_PYTEST_EXIT=1 · 4 failed, 3 passed · Failed: DID NOT RAISE NestedSovereignCallError في أربعةِ فحوصٍ (حذفُ الفحصِ عندَ دخولِ execute) · لا خطأَ استيراد. طفرةُ حذفِ الكاشفِ اكتُشفت بتأكيدِ الكاشف. شقُّ حذفِ إصلاحِ § 3.5 من (5): خارجُ النطاق — لا يُحكَم.
(6) نعم. مسبارُ المقعدِ مكتوبٌ في probe/seat_probe_wi115.py وليسَ أمرًا من (ج) ولا نسخةً من فحصٍ قائم، وشِفرتُه الكتلةُ 13 وتشغيلُه الكتلةُ 14.
PROBES: 13 · 14 · رفضُ عبورٍ سياديٍّ غيرِ مستثنًى داخلَ عبورٍ نشطٍ قبلَ decide، ومرورُ الزوجينِ المجمَّدينِ لـopen_case لا بالاسمِ المفردِ ولا بالعكسِ ولا عبرَ نسخةٍ ثانيةٍ ولا لحفيدٍ، وكشفُ طفرةِ حذفِ الفحصِ بتأكيدٍ لا باستيراد · انكسرت؟ لا
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم. استنسختُ المستودعَ بنفسي أمرًا كاملًا: gh repo clone vooovg-ui/AMOS-Fedration /home/user/workspace/council_w701/grok_4_7/wi115/repo ثمَّ git checkout لعقدةِ الأمرِ 1 (147a0c6b1357ddf0a93ba1c4d16e82e8648cb247) ثمَّ bash tools/dev/bootstrap.sh داخلَ الاستنساخ. لم أقرأ ولم أكتب خارجَ جذرِ المقعد /home/user/workspace/council_w701/grok_4_7/wi115. لم أقرأ أدلّةَ المنفِّذِ W-68* ولا W-69* ولا W-70* عدا ملفَّي الإحاطةِ اللذينِ سمّاهما الأمرانِ 11 و12، ولم أقرأ نسخةَ المنسِّقِ /home/user/workspace/amos ولا عملَ مقاعدَ أخرى. ما قُرئ داخلَ الاستنساخ: الشِّفرةُ والفحوصُ التي سمّتها أوامرُ (ج)، وصفُّ WI-115 وكتلتُه في ACTIVE_WORK.md، وقراراتُ Q-9/D25-3/WI-110 في SOVEREIGN_DECISION_REGISTER.md، وأداتا الالتقاطِ والفاحصِ اللازمتانِ لتشغيلِ الإحاطة.
VERDICT: PASS لكلِّ معاييرِ نطاقِ هذه الجولة ((3) وشقُّ الكاشفِ من (5) و(6)) — لا VERIFIED للبندِ كلِّه ((4) مؤجَّل · (1) و(2) وشقُّ § 3.5 خارجَ النطاق)
