# حكمُ مقعدِ المجلسِ — gemini_3_8_flash · جولةُ WI-115 (W-710)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في الجولةِ الواحدةِ (قرارُ المالكِ D27) على WI-115 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w701/gemini_3_8_flash/wi115) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `aec737a4ce295a4ecdb16bff95b6c94596b67fcc1ff926933ba1f787e2118926`).

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
MODEL: gemini_3_8_flash
FAMILY: gemini
RUN_DATE: 2026-10-28 06:46 +00:00
NODE: 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
CLONE_PATH: /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/
 2. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/)
 3. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git log --format='%h %cI %s' -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
 5. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git show --stat 2b814b34
 6. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git diff 2b814b34^ 2b814b34 -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py
 7. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
 8. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
 9. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && rg -n "NESTED_SOVEREIGN_EXEMPTIONS|NestedSovereignCallError|open_case" core/sovereignty/enforcement_boundary.py
 10. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && rm -rf ../old && git worktree add --detach ../old 2b814b34^ && cp tests/sovereignty/test_wi115_nesting_detector.py ../old/tests/sovereignty/ && cd ../old && /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
 11. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && sha256sum docs/audit/evidence/W-701/briefs_wi115/briefing_gemini_3_8_flash.md
 12. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && cat docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS
 13. nl -ba /home/user/workspace/council_w701/gemini_3_8_flash/wi115/probe/test_custom_probe.py
 14. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider /home/user/workspace/council_w701/gemini_3_8_flash/wi115/probe/test_custom_probe.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/)
EXIT: 0
BYTES: 1605
SHA256: 56806346d0784c228cd8e79471ae3c3c5e404b3571c756489ea1594c171bb5df
NO_EOL: 0
--- OUTPUT ---
Note: switching to '147a0c6b1357ddf0a93ba1c4d16e82e8648cb247'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 147a0c6b W-701: توجيهُ المستشارِ 25 — قراراتُ المالكِ D27 بنصّها (إغلاقُ WI-113/WI-117/WI-119 بعدَ VERIFIED بإجماعٍ دونَ سؤالٍ جديدٍ · الجولةُ الآنَ لا بعدَ G1 — جولةٌ واحدةٌ بثلاثةِ نطاقاتٍ تُجمَعُ في الجلسةِ نفسِها Q-72) + واجبُ N+1 لـPR #168 (قراءةُ التشغيلِ 40478049851 بالفاحصِ فعلًا: مقروءٌ أخضرُ 13/13 على 129bed06 · EXIT 0) + انتقالٌ واحدٌ: WI-119 IN_PROGRESS→IN_REVIEW + إحاطاتُ الجولةِ التسعُ مبصومةً (3 مقاعدٍ × WI-117/WI-119/الكاشفُ من WI-115 · gemini · grok · kimi) ونصوصُ الإطلاقِ حرفيًّا وقياساتُ الجلسةِ خامًا (حوكمةُ الأعمالِ ✓ · راتشيتٌ 61 · حزمةُ الحوكمةِ 1394 خضراءَ) · لا شِّفرةَ سلوكيّةً · المنسِّقُ GLM-5.3 (Perplexity Computer)
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git log --format='%h %cI %s' -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git show --stat 2b814b34
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git diff 2b814b34^ 2b814b34 -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
EXIT: 0
BYTES: 784
SHA256: 96e522b58ac135d4be459f1aa1e6842448ca1cc1a67d982f452a6ce0f55ad8d1
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
.......                                                                  [100%]
7 passed in 0.13s
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py
EXIT: 0
BYTES: 1407
SHA256: 1a1f91f4ade68c774731a18289ad9f34ebced4a7ea3e4da330591cf1a3c06ea4
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 3 items

federal/executive/services/tests/test_wi115_reversed_replay.py ..        [ 66%]
federal/executive/services/tests/test_wi115_nesting_compensator_frame.py . [100%]

============================== 3 passed in 1.60s ===============================
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && rg -n "NESTED_SOVEREIGN_EXEMPTIONS|NestedSovereignCallError|open_case" core/sovereignty/enforcement_boundary.py
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && rm -rf ../old && git worktree add --detach ../old 2b814b34^ && cp tests/sovereignty/test_wi115_nesting_detector.py ../old/tests/sovereignty/ && cd ../old && /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py
EXIT: 2
BYTES: 2060
SHA256: ef2956114ff5abd550d57dccbd2c073f156930f8407775ab52e87193ca0e37d9
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD bd1dc84b)
HEAD is now at bd1dc84b W-684: إعادةُ توليدِ مصفوفةِ الحقيقةِ (ملفّاتٌ مُعفاةٌ وحدَها)
/home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))

==================================== ERRORS ====================================
______ ERROR collecting tests/sovereignty/test_wi115_nesting_detector.py _______
ImportError while importing test module '/home/user/workspace/council_w701/gemini_3_8_flash/wi115/old/tests/sovereignty/test_wi115_nesting_detector.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/uv/python/cpython-3.12.15-linux-x86_64-gnu/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/sovereignty/test_wi115_nesting_detector.py:35: in <module>
    from core.sovereignty.enforcement_boundary import (
E   ImportError: cannot import name 'NestedSovereignCallError' from 'core.sovereignty.enforcement_boundary' (/home/user/workspace/council_w701/gemini_3_8_flash/wi115/old/core/sovereignty/enforcement_boundary.py)
=========================== short test summary info ============================
ERROR tests/sovereignty/test_wi115_nesting_detector.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.18s
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && sha256sum docs/audit/evidence/W-701/briefs_wi115/briefing_gemini_3_8_flash.md
EXIT: 0
BYTES: 134
SHA256: e0bf415765de67d03dba24627ebfde9526f0dd97efae24424aca602093860914
NO_EOL: 0
--- OUTPUT ---
59c601126c30585d32790210c831dc953ab8516e89c8211838819313edf91e1c  docs/audit/evidence/W-701/briefs_wi115/briefing_gemini_3_8_flash.md
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && cat docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w701/gemini_3_8_flash/wi115/probe/test_custom_probe.py
EXIT: 0
BYTES: 10724
SHA256: 0beded53c4fcdff531f5a5fb1a4d089e3260bb3cbd3a9821b592d0f89a15c497
NO_EOL: 0
--- OUTPUT ---
     1	"""مسبار مقعد gemini_3_8_flash المستقل لكاشف التعشيش السيادي (WI-115 · Q-9).
     2	يحاول المسبار كسر الخواص المدعاة لكاشف التعشيش في core/sovereignty/enforcement_boundary.py:
     3	1. محاولة كسر التناظر: هل يُسمح بالعكس (task.submit كأب وgov.case.open كابن)؟ يُتوقع الرفض.
     4	2. محاولة تعشيش الفعل مع نفسه: gov.case.open داخل gov.case.open. يُتوقع الرفض.
     5	3. اختبار الزوج الثاني المستثنى: (gov.case.open, task.cancel) - هل يعبر بسلام؟
     6	4. اختبار عبر نسختين مختلفتين من SovereignExecutionBoundary في نفس السياق (cross-instance nesting).
     7	5. اختبار ثبات NESTED_SOVEREIGN_EXEMPTIONS ضد التعديل (frozenset immutability).
     8	"""
     9	
    10	from __future__ import annotations
    11	
    12	from pathlib import Path
    13	import pytest
    14	from cryptography.hazmat.primitives.asymmetric import ed25519
    15	
    16	from core.constitutional_engine.engine import ConstitutionalEngine
    17	from core.constitutional_engine.ledger import ConstitutionalLedger
    18	from core.constitutional_engine.model import ActionRequest, Branch
    19	from core.sovereignty.compensation import Compensator
    20	from core.sovereignty.contract import EffectKind, SovereignEffect
    21	from core.sovereignty.enforcement import ConsumedPermitLedger
    22	from core.sovereignty.enforcement_boundary import (
    23	    NESTED_SOVEREIGN_EXEMPTIONS,
    24	    NestedSovereignCallError,
    25	    SovereignExecutionBoundary,
    26	    _active_crossing,
    27	)
    28	from core.sovereignty.gateway import SovereignGateway
    29	from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger
    30	from core.sovereignty.outbox import OutboxLedger, SovereignOutbox
    31	
    32	
    33	def _make_boundary(tmp_path: Path, name: str = "b") -> tuple[SovereignExecutionBoundary, SovereignGateway, IdempotencyLedger]:
    34	    sub = tmp_path / name
    35	    sub.mkdir(parents=True, exist_ok=True)
    36	    gateway = SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(sub / "l.jsonl")))
    37	    idempotency = IdempotencyLedger(sub / "IDEMPOTENCY.json")
    38	    outbox = SovereignOutbox(
    39	        ledger=OutboxLedger(sub / "OUTBOX.json"),
    40	        verifying_key=ed25519.Ed25519PublicKey.from_public_bytes(bytes.fromhex(gateway.verifying_key_hex)),
    41	    )
    42	    bnd = SovereignExecutionBoundary(
    43	        gateway=gateway,
    44	        idempotency_ledger=idempotency,
    45	        outbox=outbox,
    46	        consumed_permits=ConsumedPermitLedger(sub / "CONSUMED.json"),
    47	    )
    48	    return bnd, gateway, idempotency
    49	
    50	
    51	def _req(action: str, target: str) -> ActionRequest:
    52	    return ActionRequest(actor=Branch.EXECUTIVE, action=action, target=target, channel="official")
    53	
    54	
    55	def _eff(resource: str) -> SovereignEffect:
    56	    return SovereignEffect(kind=EffectKind.WRITE, resource=resource, detail="probe")
    57	
    58	
    59	def _comp(state: dict[str, str], eff: SovereignEffect) -> Compensator:
    60	    return Compensator(
    61	        effect_signature=eff.signature,
    62	        apply=lambda: state.update({eff.resource: "RESTORED"}),
    63	        description="probe compensation",
    64	    )
    65	
    66	
    67	def test_probe_1_reversed_pair_rejected(tmp_path: Path):
    68	    """محاولة كسر الاستثناء بعكس الزوج: task.submit كأب وgov.case.open كابن - يجب أن يُرفض."""
    69	    bnd, gw, idemp = _make_boundary(tmp_path, "p1")
    70	    state = {"tasks/task-1": "0", "gov/case-1": "0"}
    71	    eff_outer = _eff("tasks/task-1")
    72	    eff_inner = _eff("gov/case-1")
    73	
    74	    def applier_outer(e: SovereignEffect):
    75	        with pytest.raises(NestedSovereignCallError) as exc_info:
    76	            bnd.execute(
    77	                _req("gov.case.open", "gov/case-1"),
    78	                declared_effects=(eff_inner,),
    79	                planner=lambda _: (eff_inner,),
    80	                applier=lambda inner_e: state.__setitem__(inner_e.resource, "INNER_DONE"),
    81	                operation_key=IdempotencyKey("scope", "inner-p1"),
    82	                compensators=(_comp(state, eff_inner),),
    83	            )
    84	        assert "التعشيشُ السياديُّ ممنوعٌ" in str(exc_info.value)
    85	        state[e.resource] = "OUTER_DONE"
    86	
    87	    bnd.execute(
    88	        _req("task.submit", "tasks/task-1"),
    89	        declared_effects=(eff_outer,),
    90	        planner=lambda _: (eff_outer,),
    91	        applier=applier_outer,
    92	        operation_key=IdempotencyKey("scope", "outer-p1"),
    93	        compensators=(_comp(state, eff_outer),),
    94	    )
    95	    assert state["tasks/task-1"] == "OUTER_DONE"
    96	    assert state["gov/case-1"] == "0"
    97	    assert _active_crossing.get() is None
    98	
    99	
   100	def test_probe_2_self_nesting_open_case_rejected(tmp_path: Path):
   101	    """محاولة استدعاء gov.case.open داخل gov.case.open - يجب أن يُرفض لأن الزوج ليس في الاستثناء."""
   102	    bnd, gw, idemp = _make_boundary(tmp_path, "p2")
   103	    state = {"gov/case-parent": "0", "gov/case-child": "0"}
   104	    eff_outer = _eff("gov/case-parent")
   105	    eff_inner = _eff("gov/case-child")
   106	
   107	    def applier_outer(e: SovereignEffect):
   108	        with pytest.raises(NestedSovereignCallError) as exc_info:
   109	            bnd.execute(
   110	                _req("gov.case.open", "gov/case-child"),
   111	                declared_effects=(eff_inner,),
   112	                planner=lambda _: (eff_inner,),
   113	                applier=lambda inner_e: state.__setitem__(inner_e.resource, "CHILD_DONE"),
   114	                operation_key=IdempotencyKey("scope", "inner-p2"),
   115	                compensators=(_comp(state, eff_inner),),
   116	            )
   117	        assert "التعشيشُ السياديُّ ممنوعٌ" in str(exc_info.value)
   118	        state[e.resource] = "PARENT_DONE"
   119	
   120	    bnd.execute(
   121	        _req("gov.case.open", "gov/case-parent"),
   122	        declared_effects=(eff_outer,),
   123	        planner=lambda _: (eff_outer,),
   124	        applier=applier_outer,
   125	        operation_key=IdempotencyKey("scope", "outer-p2"),
   126	        compensators=(_comp(state, eff_outer),),
   127	    )
   128	    assert state["gov/case-parent"] == "PARENT_DONE"
   129	    assert state["gov/case-child"] == "0"
   130	    assert _active_crossing.get() is None
   131	
   132	
   133	def test_probe_3_exempt_pair_task_cancel_succeeds(tmp_path: Path):
   134	    """التحقق من الزوج المستثنى الثاني: gov.case.open -> task.cancel يعبر بنجاح وينفذ."""
   135	    bnd, gw, idemp = _make_boundary(tmp_path, "p3")
   136	    state = {"gov/case-A": "0", "tasks/task-cancel-A": "0"}
   137	    eff_outer = _eff("gov/case-A")
   138	    eff_inner = _eff("tasks/task-cancel-A")
   139	
   140	    def applier_outer(e: SovereignEffect):
   141	        outcome_inner = bnd.execute(
   142	            _req("task.cancel", "tasks/task-cancel-A"),
   143	            declared_effects=(eff_inner,),
   144	            planner=lambda _: (eff_inner,),
   145	            applier=lambda inner_e: state.__setitem__(inner_e.resource, "CANCELED"),
   146	            operation_key=IdempotencyKey("scope", "inner-p3"),
   147	            compensators=(_comp(state, eff_inner),),
   148	        )
   149	        assert outcome_inner.is_replay is False
   150	        state[e.resource] = "CASE_OPENED"
   151	
   152	    bnd.execute(
   153	        _req("gov.case.open", "gov/case-A"),
   154	        declared_effects=(eff_outer,),
   155	        planner=lambda _: (eff_outer,),
   156	        applier=applier_outer,
   157	        operation_key=IdempotencyKey("scope", "outer-p3"),
   158	        compensators=(_comp(state, eff_outer),),
   159	    )
   160	    assert state["gov/case-A"] == "CASE_OPENED"
   161	    assert state["tasks/task-cancel-A"] == "CANCELED"
   162	    assert _active_crossing.get() is None
   163	
   164	
   165	def test_probe_4_cross_instance_nesting_detection(tmp_path: Path):
   166	    """التحقق من كشف التعشيش عبر نسختين منفصلتين من SovereignExecutionBoundary."""
   167	    bnd1, gw1, idemp1 = _make_boundary(tmp_path, "p4_b1")
   168	    bnd2, gw2, idemp2 = _make_boundary(tmp_path, "p4_b2")
   169	    state = {"acc-1": "0", "acc-2": "0"}
   170	    eff1 = _eff("acc-1")
   171	    eff2 = _eff("acc-2")
   172	
   173	    def applier_bnd1(e: SovereignEffect):
   174	        with pytest.raises(NestedSovereignCallError) as exc_info:
   175	            bnd2.execute(
   176	                _req("credit_account", "acc-2"),
   177	                declared_effects=(eff2,),
   178	                planner=lambda _: (eff2,),
   179	                applier=lambda inner_e: state.__setitem__(inner_e.resource, "INNER_DONE"),
   180	                operation_key=IdempotencyKey("scope", "inner-p4"),
   181	                compensators=(_comp(state, eff2),),
   182	            )
   183	        assert "التعشيشُ السياديُّ ممنوعٌ" in str(exc_info.value)
   184	        state[e.resource] = "OUTER_DONE"
   185	
   186	    bnd1.execute(
   187	        _req("credit_account", "acc-1"),
   188	        declared_effects=(eff1,),
   189	        planner=lambda _: (eff1,),
   190	        applier=applier_bnd1,
   191	        operation_key=IdempotencyKey("scope", "outer-p4"),
   192	        compensators=(_comp(state, eff1),),
   193	    )
   194	    assert state["acc-1"] == "OUTER_DONE"
   195	    assert state["acc-2"] == "0"
   196	    assert _active_crossing.get() is None
   197	
   198	
   199	def test_probe_5_exemptions_frozenset_immutability():
   200	    """التحقق من تجميد مجموعة الاستثناءات NESTED_SOVEREIGN_EXEMPTIONS وعدم إمكانية تعديلها."""
   201	    assert isinstance(NESTED_SOVEREIGN_EXEMPTIONS, frozenset)
   202	    assert NESTED_SOVEREIGN_EXEMPTIONS == frozenset({
   203	        ("gov.case.open", "task.submit"),
   204	        ("gov.case.open", "task.cancel"),
   205	    })
   206	    with pytest.raises(AttributeError):
   207	        NESTED_SOVEREIGN_EXEMPTIONS.add(("any", "any"))  # type: ignore[attr-defined]
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider /home/user/workspace/council_w701/gemini_3_8_flash/wi115/probe/test_custom_probe.py
EXIT: 0
BYTES: 784
SHA256: ef97a68c94ce09835d91d8d13d25fedf74eec30606d1ae2fd89392ff7567bfe6
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
.....                                                                    [100%]
5 passed in 0.08s
=== RAW [14] END ===
VERDICT_PER_CRITERION:
- المعيار (1) [خارج نطاق هذه الجولة / عولج سابقًا في W-673/W-683]: وثيقة التصميم بقياسات مولدة بأوامر (DISC-136) — ليس من نطاق هذه الجولة.
- المعيار (2) [خارج نطاق هذه الجولة / عولج سابقًا في W-673/W-683]: إصلاح § 3.5 (إعادة صرف لحركة reversed لا تعيدها صامتة) — ليس من نطاق هذه الجولة.
- المعيار (3) [داخل نطاق هذه الجولة]: الكاشف يرفض عبورًا سياديًّا داخل عبور نشط قبل decide · وopen_case مستثنًى باسمه استثناءً مسجلًا: نعم (متحقق بالكامل). الدليل: تطبيق الكاشف عند الخطوة ⓪ في SovereignExecutionBoundary.execute ورفع NestedSovereignCallError قبل أي حارس وأي decide وأي قيد (الكتلة [9])، وحصر الاستثناء في NESTED_SOVEREIGN_EXEMPTIONS بأزواج مجمدة frozenset للزوجين (gov.case.open, task.submit) و(gov.case.open, task.cancel) فقط (الكتلة [9])، ونجاح جميع فحوصات الكاشف 6/6 PASS في الكتلة [7] وفحوصات الحرس والمعوض 7/7 PASS في الكتلة [8]، بالإضافة إلى نتائج المسبار المستقل (الكتلتان [13] و[14]).
- المعيار (4) [مؤجل بعرض على المالك/المجلس]: المركبات الثلاثة تعلن الآثار وتنادي نوى خاصة فلا ترفض بالكاشف — مؤجل بقرار المالك وتوجيه المستشار 25 § 1 (الاستخراج _disburse_core يكسر حرس Q-32 القائم مقيسًا) وليس من نطاق هذه الجولة.
- المعيار (5) [شق الكاشف - داخل نطاق هذه الجولة]: طفرة حذف الكاشف تكتشف: نعم (متحقق). الدليل: سقوط فحص الكاشف عند تشغيله على شجرة العمل القديمة قبل W-685 بخطأ استيراد صريح ImportError: cannot import name NestedSovereignCallError (الكتلة [10] برمز خروج 2)، ومقتل طفرة الحذف بفحص test_التعشيشغيرالمستثنىيرفضقبلأيحارسوقبلأيإذن في الكتلة [7]، وإثبات المنع الحاسم في المسبار المستقل (الكتلتان [13] و[14]).
- المعيار (6) [مسبار لكل مقعد - إلزامي]: نعم (متحقق). الدليل: كتابة وتنفيذ مسبار مستقل خاص بمقعد gemini_3_8_flash في /home/user/workspace/council_w701/gemini_3_8_flash/wi115/probe/test_custom_probe.py عُرضت شفرته في الكتلة [13] ونُفّذ بنجاح 5/5 PASS في الكتلة [14].
PROBES:
- مسبار مقعد gemini_3_8_flash المستقل: كتلة الشفرة [13] · كتلة التشغيل [14] · الخواص التي حاول كسرها: (1) محاولة كسر التناظر بعكس الزوج task.submit كأب وgov.case.open كابن (انكسرت؟ لا - رُفض برفع NestedSovereignCallError) · (2) محاولة تعشيش الفعل داخل نفسه gov.case.open في gov.case.open (انكسرت؟ لا - رُفض برفع NestedSovereignCallError) · (3) اختبار عبور الزوج الثاني المستثنى مسجلًا gov.case.open -> task.cancel (انكسرت؟ لا - عبر بنجاح ونُفّذ) · (4) كشف التعشيش عبر نسختين منفصلتين من SovereignExecutionBoundary في نفس السياق cross-instance (انكسرت؟ لا - تم اكتشاف التعشيش ورفع NestedSovereignCallError) · (5) محاولة تعديل مجموعة الاستثناءات NESTED_SOVEREIGN_EXEMPTIONS (انكسرت؟ لا - frozenset غير قابلة للتعديل وتثير AttributeError).
BLOCKING_REMARKS:
لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION:
نعم، أقر بأنني لم أقرأ أو أكتب أي شيء خارج استنساخي الخاص /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo وهذه الإحاطة في /home/user/workspace/council_w701/gemini_3_8_flash/wi115/briefing.md، ملتزمًا بالعزل التام بالجذر.
VERDICT:
PASS لكلِّ المعاييرِ المنفَّذةِ في النطاقِ المعلَنِ (المعيارُ (3) وشقُّ الكاشفِ من (5) والمسبارُ (6)) — فلا VERIFIED للبندِ كلِّهِ بهذهِ الجولةِ
