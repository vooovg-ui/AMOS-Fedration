# حكمُ مقعدِ المجلسِ — grok_4_7 (عائلةُ xAI · Grok) · جولةُ الدفعةِ على WI-105 بعدَ وصلِ التعويضِ (W-606)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في الجولةِ الواحدةِ على الدفعةِ (إحاطاتُ W-605 المبصومةُ · العقدةُ `175054b` · بندُ WI-105 · المعاييرُ 1–7 · المسبارُ الإلزاميُّ § 4.9) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `/home/user/workspace/council_w605/grok_4_7/VERDICT.md` منسوخًا بعدَ هذا الفاصلِ بايتًا ببايتٍ.

---

MODEL: grok_4_7 (الإصدارُ التفصيليُّ غيرُ معروضٍ من المنصةِ)
FAMILY: xAI
RUN_DATE: 2026-10-22 06:49 +00:00
NODE: 175054b7d34987a7552512bbe4ba25f2c9a0e927
CLONE_PATH: /home/user/workspace/council_w605/grok_4_7/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w605/grok_4_7/repo && git rev-parse HEAD
 2. cd /home/user/workspace/council_w605/grok_4_7/repo && bash tools/dev/bootstrap.sh
 3. cd /home/user/workspace/council_w605/grok_4_7/repo && git log --format='%h %cI %s' 8c98ca5..HEAD
 4. cd /home/user/workspace/council_w605/grok_4_7/repo && git diff --stat 8c98ca5 HEAD
 5. cd /home/user/workspace/council_w605/grok_4_7/repo && git log --format='%h %cI %s' -3 -- docs/audit/J1_ISSUE_RULING_DESIGN.md core/sovereignty/enforcement_boundary.py
 6. cd /home/user/workspace/council_w605/grok_4_7/repo && git diff d0932c51 HEAD -- federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py federal/executive/services/tests/test_2b_government_services_sovereign.py tests/sovereignty
 7. cd /home/user/workspace/council_w605/grok_4_7/repo && git diff 8c98ca5 HEAD -- core/sovereignty/enforcement_boundary.py
 8. cd /home/user/workspace/council_w605/grok_4_7/repo && git diff 8c98ca5 HEAD -- federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
 9. cd /home/user/workspace/council_w605/grok_4_7/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 10. cd /home/user/workspace/council_w605/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py -q
 11. cd /home/user/workspace/council_w605/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
 12. cd /home/user/workspace/council_w605/grok_4_7/repo && .venv/bin/python -m pytest tests/sovereignty -q
 13. cd /home/user/workspace/council_w605/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
 14. cd /home/user/workspace/council_w605/grok_4_7/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
 15. cd /home/user/workspace/council_w605/grok_4_7/repo && cat docs/audit/evidence/W-601/test_w601_gap_probe.py docs/audit/evidence/W-601/probe_output_before_fix.txt
 16. cd /home/user/workspace/council_w605/grok_4_7/repo && cat docs/audit/evidence/W-603/mutations_M5_M8_output.txt docs/audit/evidence/W-603/probe_output_after_fix.txt docs/audit/evidence/W-603/measurements.txt
 17. cd /home/user/workspace/council_w605/grok_4_7/repo && rg -n "Q-70" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 18. cd /home/user/workspace/council_w605/grok_4_7/repo && rg -n "DISC-129" docs/governance/work/DISCOVERIES.md
 19. cd /home/user/workspace/council_w605/grok_4_7/repo && .venv/bin/python -m pytest tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q
 20. cd /home/user/workspace/council_w605/grok_4_7/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
 21. find /home/user/workspace/council_w605/grok_4_7 -maxdepth 1
 22. nl -ba /home/user/workspace/council_w605/grok_4_7/probe/probe_partial_restore_after_inner_failure.py
 23. cd /home/user/workspace/council_w605/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_probe.db .venv/bin/python -m pytest federal/executive/services/tests/test_grok_4_7_w605_probe.py -q -s
 24. python3 /home/user/workspace/council_w605/grok_4_7/probe/rerun_mutations.py
 25. cd /home/user/workspace/council_w605/grok_4_7/repo && cp docs/audit/evidence/W-601/test_w601_gap_probe.py federal/executive/services/tests/test_w601_gap_probe.py && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_w601.db .venv/bin/python -m pytest federal/executive/services/tests/test_w601_gap_probe.py -s -q -p no:cacheprovider ; ec=$? ; rm -f federal/executive/services/tests/test_w601_gap_probe.py ; exit $ec
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: b3691418708bcd80f2f538592d095c396c6bcd11c975f5862d7a725c95bba6a5
NO_EOL: 0
--- OUTPUT ---
175054b7d34987a7552512bbe4ba25f2c9a0e927
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && bash tools/dev/bootstrap.sh
EXIT: 0
BYTES: 1287
SHA256: 8bbaf7273f42d0efd8e5c28773c526dfd845213e1aa7922845e153a5c3518973
NO_EOL: 0
--- OUTPUT ---
• الجذر: /home/user/workspace/council_w605/grok_4_7/repo
• ثُبِّتَ خُطّافُ pre-push (يُشغِّلُ حرسَ ما قبلَ الدفعِ على كلِّ دفعٍ — WI-078)
• إنشاءُ بيئةٍ معزولةٍ في .venv
• تركيبُ تبعيّاتِ الجذر (requirements-dev.txt)
• تركيبُ حزمةِ الخدماتِ (قد تطولُ: تبعيّاتٌ كثيرة)
• تركيبُ ruff==0.6.9 (‏المُثبَّتُ في .github/workflows/ci.yml)
✓ البيئةُ جاهزة. للتنشيطِ في جلسةٍ جديدة: source .venv/bin/activate

الأوامرُ الواجبةُ قبلَ أيِّ دفع (دليلُ المشروع § 8 و§ 9):
  python -m pytest tests/ -q
  AMOS_DATABASE_URL="sqlite:////tmp/amos_test.db" \
    python -m pytest federal/executive/services/tests -q
  python tools/governance/truth_audit.py .
  python tools/governance/check_repository_identity.py .
  python tools/governance/check_completion_ledger.py --commit HEAD
  python tests/smoke/run_smoke_tests.py
  ruff check . && ruff format --check \
    federal/executive/services/src federal/executive/services/tests

وتذكّرْ: آخرُ أمرٍ يُغيِّرُ بايتًا من الكودِ يسبقُ آخرَ توليدٍ للمصفوفة.
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && git log --format='%h %cI %s' 8c98ca5..HEAD
EXIT: 0
BYTES: 2232
SHA256: 4b240322ef1c2e95e609a2423c6e11d8faa9d0ba5db719015ee9f82c30e3d2ed
NO_EOL: 0
--- OUTPUT ---
175054b 2026-10-22T05:48:35Z W-604: WI-105 IN_PROGRESS→IN_REVIEW قيدًا مستقلًّا (H3 · سابقة W-597) بعد وصل التعويض (W-603) — لا شفرة · الجولة الواحدة على الدفعة بالمسبار الإلزامي (COUNCIL_PROTOCOL § 4.9) على عقدة main بعد الدمج — المنسق Claude Opus 5.5
968e5ba 2026-10-22T05:38:45Z W-603: وصل التعويض الآلي في الحد (core/sovereignty/enforcement_boundary.py وحده · قرار المالك Q-70 · ملحق التصميم § 7) — تتبع الأثر · لف run_once ⇒ CompensationGuard.compensate بمفتاح الحلقة ثم CompensationRequired · FAILED_RETRYABLE/FAILED_FINAL · T6p/T8/T9/T10 · الطفرات M5–M8 كل أسقط فحصه · مسبار W-601 بعد الوصل: المعوض 1 في السطحين · DISC-129 · D-4 181←181 · نص المسبار الإلزامي في COUNCIL_PROTOCOL § 4.9 والقالب (التوجيه 18 § 3)
e13fe2f 2026-10-22T05:04:50Z W-602: WI-105 IN_REVIEW→IN_PROGRESS قيدًا مستقلًّا (H3) بقرار المالك Q-70 — توسيع النطاق بملف الحد core/sovereignty/enforcement_boundary.py وحده (الفرع الأول من القرار بقياس W-601) · ملحق التصميم § 7 ملتزم قبل الشفرة: الموضع · نص الوصل · فشل المعوِّض ⇒ FAILED_FINAL · ما يُحفظ · مفتاح الحلقة · ومعيار القبول (7) T6p/T8/T9/T10 وM5–M8 — لا شفرة — المنسق Claude Opus 5.5
07ea0d9 2026-10-22T05:01:23Z W-601: قرار المالك Q-70 (توجيه المستشار 18 § 1 · نصّه حرفيًّا): الخيار (1) مشروطًا بقياس موضع الفجوة — والقياس على المسار الإنتاجي بلا تغيير (evidence/W-601): issue_ruling وregister_identity (WI-082) كلاهما RuntimeError خام · الصفوف ملتزمة · نداءات المعوِّض 0 · سجل الذرّية RUNNING ⇒ الفجوة في الحد نفسه · تصحيح مؤرَّخ لعبارة D17 في D18 · حكم CI على 8c98ca5 (N+1) أخضر مقروء 13/13 — لا شفرة — المنسق Claude Opus 5.5
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && git diff --stat 8c98ca5 HEAD
EXIT: 0
BYTES: 1621
SHA256: 737e33f98fd058854aa62b6c7544b658844dee858ed17d9d406df40f5bd8e992
NO_EOL: 0
--- OUTPUT ---
 PROJECT_STATE.md                                   |   8 +-
 core/sovereignty/enforcement_boundary.py           | 161 +++++++++--
 docs/PROJECT_HANDBOOK.md                           |   6 +-
 docs/audit/ACTIVE_EXECUTION_STATE.md               |   2 +-
 docs/audit/COMPLETION_LEDGER.md                    |   8 +
 docs/audit/J1_ISSUE_RULING_DESIGN.md               |  54 +++-
 docs/audit/SOVEREIGN_DECISION_REGISTER.md          |  10 +-
 docs/audit/TRUTH_MATRIX.md                         |   6 +-
 docs/audit/evidence/W-601/README.md                |  43 +++
 .../evidence/W-601/ci_jobs_39720098200.api.txt     |   1 +
 .../W-601/ci_verdict_39720098200_green.txt         |   6 +
 docs/audit/evidence/W-601/directive_18_verbatim.md |  34 +++
 .../evidence/W-601/probe_output_before_fix.txt     |  32 +++
 docs/audit/evidence/W-601/test_w601_gap_probe.py   | 160 +++++++++++
 docs/audit/evidence/W-603/README.md                |  26 ++
 docs/audit/evidence/W-603/measurements.txt         |  22 ++
 .../evidence/W-603/mutations_M5_M8_output.txt      |  39 +++
 .../evidence/W-603/probe_output_after_fix.txt      |  34 +++
 docs/audit/truth_matrix.json                       |  26 +-
 docs/governance/COUNCIL_BRIEF_TEMPLATE.md          |   6 +-
 docs/governance/COUNCIL_PROTOCOL.md                |   3 +-
 docs/governance/work/ACTIVE_WORK.md                |  18 +-
 docs/governance/work/DISCOVERIES.md                |   5 +-
 .../work/HANDOFFS/OWNER-DECISIONS-D18.md           |   5 +-
 .../tests/test_wi105_issue_ruling_sovereign.py     | 310 ++++++++++++++-------
 25 files changed, 873 insertions(+), 152 deletions(-)
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && git log --format='%h %cI %s' -3 -- docs/audit/J1_ISSUE_RULING_DESIGN.md core/sovereignty/enforcement_boundary.py
EXIT: 0
BYTES: 2508
SHA256: 72bf37dbf351c1ea14e6303be9e30374597460e81ad4a1a40fa74e41dccc05bf
NO_EOL: 0
--- OUTPUT ---
968e5ba 2026-10-22T05:38:45Z W-603: وصل التعويض الآلي في الحد (core/sovereignty/enforcement_boundary.py وحده · قرار المالك Q-70 · ملحق التصميم § 7) — تتبع الأثر · لف run_once ⇒ CompensationGuard.compensate بمفتاح الحلقة ثم CompensationRequired · FAILED_RETRYABLE/FAILED_FINAL · T6p/T8/T9/T10 · الطفرات M5–M8 كل أسقط فحصه · مسبار W-601 بعد الوصل: المعوض 1 في السطحين · DISC-129 · D-4 181←181 · نص المسبار الإلزامي في COUNCIL_PROTOCOL § 4.9 والقالب (التوجيه 18 § 3)
e13fe2f 2026-10-22T05:04:50Z W-602: WI-105 IN_REVIEW→IN_PROGRESS قيدًا مستقلًّا (H3) بقرار المالك Q-70 — توسيع النطاق بملف الحد core/sovereignty/enforcement_boundary.py وحده (الفرع الأول من القرار بقياس W-601) · ملحق التصميم § 7 ملتزم قبل الشفرة: الموضع · نص الوصل · فشل المعوِّض ⇒ FAILED_FINAL · ما يُحفظ · مفتاح الحلقة · ومعيار القبول (7) T6p/T8/T9/T10 وM5–M8 — لا شفرة — المنسق Claude Opus 5.5
529cc39 2026-10-21T19:46:27Z W-593: شِفرة J1 — عبور issue_ruling الحدَّ السياديَّ بفاعلٍ قضائيٍّ ثابت (WI-105 · قرار المالك Q-69/D17-6): D1 ثابت JUDICIARY_ACTOR ومُفوِّض كسول في الوحدة · D2 الجسر يمرّر judicial_action كما هو · D3 طلب الاختصاص من البيانات الحيّة + حقل position_scope في JudicialAuthority · D4 المُطبِّق المتداخل يلتزم الصفوف الثلاثة في معاملة واحدة والخدمة فقدت commit · D6 مفتاح بجيل الإلغاء والمكرَّر قبل الحد · D7-أ مُعوِّض تقني (حذف الصفّين وإرجاع حالة القضيّة) — الجرد: الدَّين 183←181 · السيادي 17←18 · الأسطح 220←220 · فحوص T1–T7 خضراء (ملف جديد) وM1–M4 كلٌّ يُسقِط فحصه · r7d وWI-082 بلا تعديل · حزمة services 1482+53 · اكتشافان مؤرَّخان في التصميم: الجيل في هدف العبور (تصادم أذون الثانية) وقياس T6 عبر حارس 1I (مسار run_once لا يُعوِّض آليًّا) · حكم CI على d0932c51 (N+1): مقروء أخضر 13/13 — المنسِّق GLM-5.3
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && git diff d0932c51 HEAD -- federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py federal/executive/services/tests/test_2b_government_services_sovereign.py tests/sovereignty
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && git diff 8c98ca5 HEAD -- core/sovereignty/enforcement_boundary.py
EXIT: 0
BYTES: 12097
SHA256: 71a19b7f62ab786cd312184c49a861aa3b8e1c09d25fa047c2b4634ff6dced45
NO_EOL: 0
--- OUTPUT ---
diff --git a/core/sovereignty/enforcement_boundary.py b/core/sovereignty/enforcement_boundary.py
index a544671..5ac88c2 100644
--- a/core/sovereignty/enforcement_boundary.py
+++ b/core/sovereignty/enforcement_boundary.py
@@ -3,7 +3,7 @@
 النطاق: مرحلةُ ربطٍ وإنفاذٍ فقط. لا إعادةَ بناءٍ لأيِّ مرحلةٍ سابقة.
 المالك: core/sovereignty/ — التاج
 تاريخ الإنشاء: 2026-08-18
-تاريخ آخر تعديل: 2026-08-18
+تاريخ آخر تعديل: 2026-10-22 (W-603 · قرارُ المالكِ Q-70: وصلُ التعويضِ الآليِّ في الحدِّ)
 
 # المشكلةُ المقيسة — لا المُفترَضة
 
@@ -43,6 +43,14 @@
 توقيعٍ (يملكُ مفتاحَ تحقّقٍ عامًّا فقط)؛ ولا يُعيدُ اختراعَ PDP؛ ولا يبني جدولةً
 للصادر؛ ولا يبني استعادةً ولا تعويضًا تشغيليًّا — يفرضُ **ربطَ** الخطّةِ فقط.
 
+> **[إضافةٌ مؤرَّخةٌ · 2026-10-22 · W-603 · قرارُ المالكِ Q-70]** الجملةُ أعلاه
+> تاريخٌ لا يُمحى، وقد قِيسَ أثرُها (W-601): إسقاطُ تثبيتِ النجاحِ بعدَ التزامِ
+> المُطبِّقِ تركَ الصفوفَ قائمةً والذرّيّةَ عالقةً `RUNNING` ونداءاتِ المُعوِّضِ 0.
+> فالحدُّ **صارَ يُنادي `CompensationGuard` نفسَه** (1I — لا مُعوِّضًا جديدًا): إن رفعَ
+> مسارُ الذرّيّةِ بعدَ أن طُبِّقَ أثرٌ داخليٌّ عكسَه بالخطّةِ المربوطةِ ورفعَ
+> `CompensationRequired` (الأصلُ في `__cause__`) — ولا يبتلعُ شيئًا. وما لم يُطبَّقْ
+> فيه أثرٌ يُرفَعُ استثناؤه كما هو. التصميمُ: `docs/audit/J1_ISSUE_RULING_DESIGN.md § 7`.
+
 # الحرسُ الساكن
 
 الفرضُ الزمنيُّ لا يكفي وحدَه: لغةُ بايثون لا تملكُ عزلَ قدرات، ومَن استوردَ
@@ -64,7 +72,10 @@ from cryptography.hazmat.primitives.asymmetric import ed25519
 
 from core.constitutional_engine.model import ActionRequest
 from core.sovereignty.compensation import (
+    CompensationGuard,
+    CompensationJournal,
     CompensationPlan,
+    CompensationRequired,
     Compensator,
     bind_compensation_plan,
 )
@@ -85,6 +96,7 @@ from core.sovereignty.idempotency import (
     IdempotencyKey,
     IdempotencyLedger,
     OperationResult,
+    OperationStatus,
     compute_fingerprint,
 )
 from core.sovereignty.jurisdiction import (
@@ -248,6 +260,9 @@ class SovereignExecutionBoundary:
     outbox: SovereignOutbox | None = None
     wall: JurisdictionWall = field(default_factory=lambda: WALL)
     consumed_permits: ConsumedPermitLedger = field(default_factory=ConsumedPermitLedger)
+    # [W-603 · Q-70] دفترُ التعويضِ (1I). إن لم يُمرَّرْ اشتُقَّ بجانبِ سجلِّ الذرّيّةِ
+    # (`<stem>.compensation.json`) — فلا يتغيّرُ مُنشِئٌ قائمٌ ولا الجسر.
+    compensation_journal: CompensationJournal | None = None
     _pep: PolicyEnforcementPoint | None = field(default=None, init=False, repr=False)
     _executions: int = field(default=0, init=False, repr=False)
     _rejections: dict[str, int] = field(default_factory=dict, init=False, repr=False)
@@ -265,6 +280,11 @@ class SovereignExecutionBoundary:
         self._pep = PolicyEnforcementPoint(
             verifying_key=verifying, consumed=self.consumed_permits
         )
+        if self.compensation_journal is None:
+            ledger_path = Path(self.idempotency_ledger.path)
+            self.compensation_journal = CompensationJournal(
+                path=ledger_path.with_name(ledger_path.stem + ".compensation.json")
+            )
 
     # ── الفحصُ الذاتي ──────────────────────────────────────────────────────
     @property
@@ -346,6 +366,26 @@ class SovereignExecutionBoundary:
         # ⑦ 1H — الذرّيّةُ تلفُّ التطبيق
         enqueued: list[str] = []
         applied_holder: list[tuple[SovereignEffect, ...]] = []
+        # [W-603 · Q-70] ما طبّقه مُطبِّقُ المُنادي **وعادَ** بنجاحٍ — بترتيبِ التطبيق.
+        applied_internal: list[str] = []
+        routed = self._route_effect(
+            permit=permit,
+            operation_key=operation_key,
+            applier=applier,
+            provider=provider,
+            payload_of=payload_of,
+            correlation_id=correlation_id,
+            enqueued=enqueued,
+        )
+
+        def _tracked(effect: SovereignEffect) -> None:
+            routed(effect)
+            if (
+                plan is not None
+                and effect.kind is not EffectKind.EXTERNAL
+                and plan.covers(effect.signature)
+            ):
+                applied_internal.append(effect.signature)
 
         def _under_permit() -> tuple[str, ...]:
             """ما يُرجَعُ للحارسِ بصماتٌ نصّيّةٌ لا كائنات.
@@ -357,15 +397,7 @@ class SovereignExecutionBoundary:
             produced = self.policy_enforcement_point.enforce(
                 permit,
                 planner=planner,
-                applier=self._route_effect(
-                    permit=permit,
-                    operation_key=operation_key,
-                    applier=applier,
-                    provider=provider,
-                    payload_of=payload_of,
-                    correlation_id=correlation_id,
-                    enqueued=enqueued,
-                ),
+                applier=_tracked,
             )
             applied_holder.append(produced)
             return tuple(e.signature for e in produced)
@@ -378,17 +410,30 @@ class SovereignExecutionBoundary:
             actor=request.actor,
         )
         external_prefix = EffectKind.EXTERNAL.value + ":"
-        result: OperationResult[tuple[str, ...]] = IdempotencyGuard(
-            ledger=self.idempotency_ledger
-        ).run_once(
-            key=operation_key,
-            fingerprint=fingerprint,
-            execute=_under_permit,
-            extract_effect_signatures=lambda sigs: tuple(sigs or ()),
-            detect_external=lambda sigs: any(
-                s.startswith(external_prefix) for s in (sigs or ())
-            ),
-        )
+        try:
+            result: OperationResult[tuple[str, ...]] = IdempotencyGuard(
+                ledger=self.idempotency_ledger
+            ).run_once(
+                key=operation_key,
+                fingerprint=fingerprint,
+                execute=_under_permit,
+                extract_effect_signatures=lambda sigs: tuple(sigs or ()),
+                detect_external=lambda sigs: any(
+                    s.startswith(external_prefix) for s in (sigs or ())
+                ),
+            )
+        except Exception as exc:
+            if plan is None or not applied_internal:
+                # لا أثرَ طُبِّقَ: الاستثناءُ يُرفَعُ كما هو (لا لفَّ ولا تغييرَ نوعٍ).
+                raise
+            self._compensate_applied(
+                exc,
+                contract=contract,
+                plan=plan,
+                operation_key=operation_key,
+                applied=tuple(applied_internal),
+            )
+            raise  # pragma: no cover — `_compensate_applied` يرفعُ دائمًا
         stages.append(BoundaryStage.IDEMPOTENCY)
         if enqueued:
             stages.append(BoundaryStage.EXTERNAL_OUTBOX)
@@ -406,6 +451,80 @@ class SovereignExecutionBoundary:
             compensation_plan=plan,
         )
 
+    # ── التعويضُ الآليُّ بعدَ الالتزام (W-603 · Q-70) ─────────────────────────
+    def _compensate_applied(
+        self,
+        exc: BaseException,
+        *,
+        contract: ExecutionContract,
+        plan: CompensationPlan,
+        operation_key: IdempotencyKey,
+        applied: tuple[str, ...],
+    ) -> None:
+        """اعكسْ ما طُبِّقَ بالخطّةِ المربوطةِ ثمَّ ارفعْ `CompensationRequired` — دائمًا.
+
+        مفتاحُ الحلقةِ: معرِّفُ التعويضِ مُشتقٌّ من مضمونِه، فلو مُرِّرَ مفتاحُ الذرّيّةِ
+        نفسُه لأرجعَ الحارسُ في الفشلِ الثاني سجلًّا مُغلَقًا قديمًا **بلا عكسٍ**.
+        فيُشتقُّ مفتاحٌ للحلقةِ من عددِ محاولاتِ السجلِّ — ومفتاحُ الذرّيّةِ لا يتغيّر.
+        """
+        ledger = self.idempotency_ledger
+        record = ledger.get(operation_key)
+        attempt_no = len(record.attempts) if record is not None else 0
+        episode_key = IdempotencyKey(
+            scope=operation_key.scope,
+            value=f"{operation_key.value}@attempt{attempt_no}",
+        )
+        journal = self.compensation_journal
+        if journal is None:  # pragma: no cover — يُبنى في __post_init__ دائمًا
+            raise BoundaryConfigurationError("دفترُ التعويضِ لم يُبنَ.")
+        reason = f"{type(exc).__name__}: {exc}"
+        outcome = CompensationGuard(
+            journal=journal, idempotency=IdempotencyGuard(ledger=ledger)
+        ).compensate(
+            contract=contract,
+            plan=plan,
+            operation_key=episode_key,
+            applied_signatures=applied,
+            reason=reason,
+        )
+        required = CompensationRequired(outcome)
+        try:
+            if outcome.state_is_clean:
+                ledger.transition(
+                    key=operation_key,
+                    new_status=OperationStatus.FAILED_RETRYABLE,
+                    applied_effect_signatures=(),
+                    failure_reason=(
+                        f"{reason} — عُوِّضَ آليًّا في الحدّ "
+                        f"({outcome.record.compensation_id})"
+                    ),
+                    attempt={
+                        "compensated": True,
+                        "compensation_id": outcome.record.compensation_id,
+                    },
+                )
+            else:
+                # إغلاقٌ عندَ الفشل: لا إعادةَ فوقَ أثرٍ باقٍ — الحسمُ بيدِ إنسان.
+                ledger.transition(
+                    key=operation_key,
+                    new_status=OperationStatus.FAILED_FINAL,
+                    applied_effect_signatures=tuple(outcome.residual_signatures),
+                    failure_reason=(
+                        f"{reason} — تعويضٌ غيرُ نظيفٍ ({outcome.record.compensation_id}) "
+                        "يلزمُ قرارٌ بشريّ"
+                    ),
+                    attempt={
+                        "compensated": False,
+                        "compensation_id": outcome.record.compensation_id,
+                    },
+                )
+        except Exception as transition_exc:  # noqa: BLE001 — يُلحَقُ لا يُبتلَع
+            required.add_note(
+                f"تعذّرَ نقلُ سجلِّ الذرّيّةِ بعدَ التعويض: "
+                f"{type(transition_exc).__name__}: {transition_exc}"
+            )
+        raise required from exc
+
     # ── الحرسُ واحدًا واحدًا ───────────────────────────────────────────────
     def _record_rejection(self, stage: BoundaryStage) -> None:
         self._rejections[stage.value] = self._rejections.get(stage.value, 0) + 1
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && git diff 8c98ca5 HEAD -- federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
EXIT: 0
BYTES: 19327
SHA256: 13b10628afd8d0644757039001dc201bb9a0f10ca9b66baee4051b831ca41fa4
NO_EOL: 0
--- OUTPUT ---
diff --git a/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py b/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
index 4dbac9f..c1092a4 100644
--- a/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
+++ b/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
@@ -24,8 +24,16 @@ WI-105 · J1 — عبورُ `issue_ruling` الحدَّ السياديَّ بف
   ولا قرارَ جديدٌ في سجلِّ البوابةِ.
 - T6 · المُعوِّض: إسقاطُ تثبيتِ النجاحِ بعدَ الالتزامِ ⇒ `CompensationRequired`
   و`state_is_clean` والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ.
+  [W-603 · 2026-10-22 · Q-70] كُتِبَ إنتاجيًّا (T6p): النداءُ الإنتاجيُّ وحدَه بلا تعويضٍ يدويٍّ.
 - T7 · التفرُّق: إعادةٌ وصفُّ الحكمِ غائبٌ ⇒ `RulingLedgerDivergenceError`.
 
+[إضافةٌ مؤرَّخةٌ · 2026-10-22 · W-603 · قرارُ المالكِ Q-70 · ملحقُ التصميمِ § 7.6]:
+- T8 · نظيرُ T6p لـWI-082: `register_identity` وحدَه مع الإسقاطِ ⇒ `CompensationRequired`
+  نظيفًا والصفُّ غائبٌ والذرّيّةُ `FAILED_RETRYABLE` والإعادةُ تنجح.
+- T9 · فشلُ المُعوِّضِ نفسِه ⇒ `state_is_clean is False` · `requires_human` · الباقي مُسمًّى ·
+  الذرّيّةُ `FAILED_FINAL` · والإعادةُ مرفوضةٌ.
+- T10 · الحلقةُ الثانيةُ: فشلانِ متتاليانِ بعدَ الالتزامِ ⇒ كلٌّ يعكسُ صفوفَه فعلًا.
+
 الحدُّ المُعلَنُ في هذا الفحصِ:
 - تبديلُ الفاعلِ في T2 بـ`monkeypatch` على ثابتِ الوحدةِ وإفراغِ المُفوِّضِ
   المحفوظِ — لا معاملَ إنتاجيًّا (D1: الفاعلُ ثابتٌ في الوحدةِ).
@@ -39,6 +47,8 @@ WI-105 · J1 — عبورُ `issue_ruling` الحدَّ السياديَّ بف
 
 from __future__ import annotations
 
+import math
+import time
 import uuid
 from typing import Any
 
@@ -614,125 +624,109 @@ def test_wi105_t5_duplicate_rejected_before_boundary(
     assert len(authorizer.gateway.records) == decisions_before
 
 
-# ── T6 · المُعوِّضُ — استعادةٌ تقنيّةٌ دقيقةٌ ────────────────────────────────
+# ── T6p · المُعوِّضُ على المسارِ الإنتاجيِّ — الحدُّ يُعوِّضُ آليًّا (W-603 · Q-70) ──
+#
+# [إضافةٌ مؤرَّخةٌ · 2026-10-22 · W-603] T6 القديمُ (W-593) كانَ يتوقّعُ `RuntimeError`
+# خامًا من النداءِ الإنتاجيِّ ثمَّ يُعوِّضُ يدويًّا بحارسِ 1I. وقرارُ المالكِ Q-70 وصلَ
+# التعويضَ في الحدِّ نفسِه، فصارَ النداءُ الإنتاجيُّ وحدَه يرفعُ `CompensationRequired`
+# بعدَ العكسِ — فيُكتَبُ الفحصُ إنتاجيًّا (تشديدٌ لا تخفيفٌ: لا تعويضَ يدويًّا هنا).
 
 
-def test_wi105_t6_compensator_restores_state_after_failed_settle(
-    registry: StateRegistry,
-    national: NationalRegistry,
-    judiciary: FederalJudiciary,
-    crown: AuthorizationContext,
-    monkeypatch: pytest.MonkeyPatch,
-    tmp_path: Any,
-) -> None:
-    """T6 · المُعوِّضُ — استعادةٌ تقنيّةٌ دقيقةٌ عبرَ حارسِ 1I بالخطةِ المربوطةِ.
-
-    اكتشافُ تنفيذٍ مُعلَنٌ في وثيقةِ التصميمِ (إضافةٌ مؤرَّخةٌ): مسارُ الحدِّ
-    أحاديَّ الأثرِ ينفّذُ عبرَ `run_once` لا عبرَ معاملةِ 1I المُعوَّضةَ، فالتعويضُ
-    الآليُّ غيرُ موصولٍ هناك. فيُقاسُ المُعوِّضُ هنا كما تقيسُهُ حوكمةُ 1I: بإسقاطِ
-    تثبيتِ النجاحِ بعدَ الالتزامِ (الصفوفُ مُلتزَمةٌ والسجلُّ RUNNING) ثمّ
-    التعويضِ بحارسِ 1I بالعقدِ والخطةِ والمفتاحِ الحقيقيّةِ المُلتقَطةِ من
-    العبورِ نفسِهِ.
-    """
-    from core.sovereignty.compensation import (
-        CompensationGuard,
-        CompensationJournal,
-        bind_compensation_plan,
-    )
-    from core.sovereignty.contract import bind_contract
-    from core.sovereignty.idempotency import IdempotencyGuard
+def _drop_settle(monkeypatch: pytest.MonkeyPatch, ledger: Any, label: str) -> Any:
+    """إسقاطُ تثبيتِ النجاحِ بعدَ التزامِ المُطبِّقِ — يُرجِعُ الأصلَ لرفعِ الإسقاط."""
+    original = type(ledger).mark_succeeded
 
-    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t6")
-    authorizer = rulings_module._judiciary_authorizer()
+    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
+        raise RuntimeError(f"تثبيتُ النجاحِ مُسقَطٌ — {label}")
 
-    # جاسوسٌ على العبورِ: يلتقطُ العقدَ (الآثارَ) والمعوّضاتِ والمفتاحَ كما
-    # تُمرَّرُ إلى الحدِّ — فالخطةُ تُبنى بها كما يربطُها الحدُّ نفسُهُ.
-    crossing: dict[str, Any] = {}
-    original_guard = rulings_module.ConstitutionalAuthorizer.guard_declared
+    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)
+    return original
 
-    def spying_guard(self: Any, *args: Any, **kwargs: Any) -> Any:
-        crossing["action"], crossing["target"] = args[0], args[1]
-        crossing.update(kwargs)
-        return original_guard(self, *args, **kwargs)
 
-    monkeypatch.setattr(rulings_module.ConstitutionalAuthorizer, "guard_declared", spying_guard)
+def _next_second() -> None:
+    """حدٌّ معلنٌ مقيسٌ (W-603): معرِّفُ الإذنِ `EP-<العقد>-<الثانية>` (enforcement.py خارجَ
+    النطاقِ) فإعادةُ العقدِ نفسِه في الثانيةِ نفسِها تُرفَضُ `PermitReplayError` — إغلاقًا لا
+    فتحًا. فالإعادةُ في الفحصِ تعبرُ إلى الثانيةِ التاليةِ ولا تُزوِّرُ الزمن."""
+    now = time.time()
+    time.sleep(math.ceil(now) - now + 0.05)
 
-    # إسقاطُ تثبيتِ النجاحِ بعدَ الالتزامِ: المُطبِّقُ يلتزمُ الصفوفَ ثمّ يفشلُ
-    # الختامُ — فهذا موضعُ المُعوِّضِ (تصميمُ D7-أ).
-    ledger = authorizer.boundary.idempotency_ledger
 
-    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
-        raise RuntimeError("تثبيتُ النجاحِ مُسقَطٌ — فحصُ المُعوِّضِ (T6)")
+def _ruling_key(case_id: str) -> Any:
+    from core.sovereignty.idempotency import IdempotencyKey
 
-    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)
+    return IdempotencyKey(scope="judiciary.ruling.issue", value=f"{case_id}:FIRST_INSTANCE:g0")
 
-    with pytest.raises(RuntimeError):
-        judiciary.issue_ruling(
-            context=judge_ctx,
-            case_id=case_id,
-            stage="FIRST_INSTANCE",
-            decision="GRANTED",
-            disposition="قضاءُ الفحصِ — إثباتُ المُعوِّضِ",
-        )
-    monkeypatch.setattr(
-        type(ledger),
-        "mark_succeeded",
-        ledger.mark_succeeded.__func__
-        if hasattr(ledger.mark_succeeded, "__func__")
-        else type(ledger).mark_succeeded,
-    )  # type: ignore[arg-type]
-
-    # والصفوفُ مُلتزَمةٌ فعلًا (الفشلُ بعدَ الالتزامِ لا قبلهُ) — وهذا موضعُ
-    # الاستعادةِ لا قبلَهُ.
-    session = _session()
-    try:
-        assert session.query(RulingModel).filter(RulingModel.case_id == case_id).count() == 1
-    finally:
-        session.close()
-
-    # التعويضُ بحارسِ 1I: العقدُ والخطةُ والمفتاحُ من العبورِ الحقيقيِّ نفسِهِ.
-    effects = crossing["declared_effects"]
-    contract = bind_contract(
-        actor="judicial",
-        action="issue_ruling",
-        target=crossing["target"],
-        declared_effects=effects,
-    )
-    plan = bind_compensation_plan(contract=contract, compensators=crossing["compensators"])
-    guard = CompensationGuard(
-        journal=CompensationJournal(path=tmp_path / "wi105_t6_compensation.json"),
-        idempotency=IdempotencyGuard(ledger=ledger),
-    )
-    outcome = guard.compensate(
-        contract=contract,
-        plan=plan,
-        operation_key=crossing["operation_key"],
-        applied_signatures=tuple(e.signature for e in effects),
-        reason="فشلُ تثبيتِ النجاحِ بعدَ الالتزامِ (T6)",
-    )
-
-    # الحصيلةُ صادقةٌ: الدولةُ رجعتْ كما كانت بالضبطِ.
-    assert outcome.state_is_clean is True
 
-    # والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ إلى ما قبلَ العمليّةِ.
+def _ruling_rows(case_id: str) -> tuple[int, int, str]:
     session = _session()
     try:
-        assert session.query(RulingModel).filter(RulingModel.case_id == case_id).count() == 0
-        assert (
+        rulings = session.query(RulingModel).filter(RulingModel.case_id == case_id).count()
+        procs = (
             session.query(CaseProceedingModel)
             .filter(
                 CaseProceedingModel.case_id == case_id,
                 CaseProceedingModel.proceeding_type == "RULING",
             )
             .count()
-            == 0
         )
         case = session.get(LegalCaseModel, case_id)
-        assert case is not None and case.status != "decided"
+        assert case is not None
+        return rulings, procs, case.status
     finally:
         session.close()
 
 
+def _issue(judiciary: FederalJudiciary, judge_ctx: AuthorizationContext, case_id: str) -> Any:
+    return judiciary.issue_ruling(
+        context=judge_ctx,
+        case_id=case_id,
+        stage="FIRST_INSTANCE",
+        decision="GRANTED",
+        disposition="قضاءُ الفحصِ — إثباتُ المُعوِّضِ",
+    )
+
+
+def test_wi105_t6p_boundary_compensates_failed_settle_on_production_path(
+    registry: StateRegistry,
+    national: NationalRegistry,
+    judiciary: FederalJudiciary,
+    crown: AuthorizationContext,
+    monkeypatch: pytest.MonkeyPatch,
+) -> None:
+    """T6p · نداءُ `issue_ruling` وحدَه مع إسقاطِ التثبيتِ ⇒ الحدُّ يعكسُ ويرفعُ — لا يدويَّ."""
+    from core.sovereignty.compensation import CompensationRequired
+    from core.sovereignty.idempotency import OperationStatus
+
+    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t6p")
+    status_before = _ruling_rows(case_id)[2]
+    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
+    original = _drop_settle(monkeypatch, ledger, "T6p")
+
+    with pytest.raises(CompensationRequired) as caught:
+        _issue(judiciary, judge_ctx, case_id)
+    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
+
+    outcome = caught.value.outcome
+    assert outcome.state_is_clean is True
+    assert outcome.requires_human is False
+    assert isinstance(caught.value.__cause__, Exception)  # الأصلُ محفوظٌ لا مُبتلَع
+    # الصفوفُ غائبةٌ والقضيّةُ بحالتِها السابقةِ (مُعوِّضُ D7-أ نفسُه)
+    assert _ruling_rows(case_id) == (0, 0, status_before)
+    # والذرّيّةُ قابلةٌ للإعادةِ بآثارٍ مطبَّقةٍ لا شيءَ
+    record = ledger.get(_ruling_key(case_id))
+    assert record is not None
+    assert record.status is OperationStatus.FAILED_RETRYABLE
+    assert tuple(record.applied_effect_signatures) == ()
+
+    # الإعادةُ بعدَ رفعِ الإسقاطِ تنجحُ بحكمٍ واحدٍ
+    _next_second()
+    issued = _issue(judiciary, judge_ctx, case_id)
+    assert issued["id"]
+    rulings, procs, status_after = _ruling_rows(case_id)
+    assert (rulings, procs) == (1, 1)
+    assert status_after == "decided"
+
+
 # ── T7 · التفرُّقُ — إعادةٌ بلا صفٍّ لا تُسكَتُ ──────────────────────────────
 
 
@@ -772,3 +766,131 @@ def test_wi105_t7_replay_with_missing_row_raises_divergence(
             decision="GRANTED",
             disposition="قضاءُ الفحصِ — إثباتُ العبورِ المحروسِ",
         )
+
+
+# ── T8 · نظيرُ T6p لـWI-082 — الوصلُ في الحدِّ مرّةً لكلِّ سطحٍ مُهجَّرٍ ──────────
+
+
+def test_wi105_t8_boundary_compensates_register_identity_on_production_path(
+    monkeypatch: pytest.MonkeyPatch,
+) -> None:
+    from core.sovereignty.compensation import CompensationRequired
+    from core.sovereignty.idempotency import IdempotencyKey, OperationStatus
+
+    from amos_federation.services.executive_core import agent_identity as agent_identity_module
+    from amos_federation.services.executive_core.agent_identity import get_identity
+    from amos_federation.services.executive_core.sovereignty_bridge import (
+        ConstitutionalAuthorizer,
+    )
+
+    agent_id = _code("wi105-t8")
+    authorizer = ConstitutionalAuthorizer(actor=agent_identity_module.AGENT_IDENTITY_ACTOR)
+    ledger = authorizer.boundary.idempotency_ledger
+    original = _drop_settle(monkeypatch, ledger, "T8")
+    try:
+        with pytest.raises(CompensationRequired) as caught:
+            register_identity(agent_id, "فحص T8", "probe", authorizer=authorizer)
+        monkeypatch.setattr(type(ledger), "mark_succeeded", original)
+
+        assert caught.value.outcome.state_is_clean is True
+        assert get_identity(agent_id) is None
+        record = ledger.get(
+            IdempotencyKey(scope=agent_identity_module.IDENTITY_SPAWN_SCOPE, value=agent_id)
+        )
+        assert record is not None
+        assert record.status is OperationStatus.FAILED_RETRYABLE
+
+        _next_second()
+        register_identity(agent_id, "فحص T8", "probe", authorizer=authorizer)
+        assert get_identity(agent_id) is not None
+    finally:
+        agent_identity_module._delete_identity_row(agent_id)
+
+
+# ── T9 · فشلُ المُعوِّضِ نفسِه — إغلاقٌ عندَ الفشلِ والحسمُ بيدِ إنسانٍ ─────────────
+
+
+def test_wi105_t9_failing_compensator_closes_operation_final(
+    registry: StateRegistry,
+    national: NationalRegistry,
+    judiciary: FederalJudiciary,
+    crown: AuthorizationContext,
+    monkeypatch: pytest.MonkeyPatch,
+) -> None:
+    from core.sovereignty.compensation import CompensationRequired, Compensator
+    from core.sovereignty.idempotency import IdempotencyError, OperationStatus
+
+    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t9")
+    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
+
+    # المُعوِّضاتُ المُعلَنةُ نفسُها بأسمائِها — لكنَّ عكسَها يرفع (عطبُ القاعدةِ مثلًا).
+    original_guard = rulings_module.ConstitutionalAuthorizer.guard_declared
+
+    def _raiser() -> None:
+        raise RuntimeError("المُعوِّضُ مُعطَّلٌ — فحصُ T9")
+
+    def breaking_guard(self: Any, *args: Any, **kwargs: Any) -> Any:
+        kwargs["compensators"] = tuple(
+            Compensator(effect_signature=c.effect_signature, apply=_raiser, description="T9")
+            for c in kwargs.get("compensators", ())
+        )
+        return original_guard(self, *args, **kwargs)
+
+    monkeypatch.setattr(rulings_module.ConstitutionalAuthorizer, "guard_declared", breaking_guard)
+    original = _drop_settle(monkeypatch, ledger, "T9")
+
+    with pytest.raises(CompensationRequired) as caught:
+        _issue(judiciary, judge_ctx, case_id)
+    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
+    monkeypatch.setattr(rulings_module.ConstitutionalAuthorizer, "guard_declared", original_guard)
+
+    outcome = caught.value.outcome
+    assert outcome.state_is_clean is False
+    assert outcome.requires_human is True
+    assert outcome.residual_signatures  # الباقي مُسمًّى لا مطويٌّ
+    assert "يلزمُ قرارٌ بشريّ" in str(caught.value)
+    # الحالةُ النصفيّةُ مُعلَنةٌ لا مُخفاةٌ: الصفُّ باقٍ والذرّيّةُ مُغلَقةٌ نهائيًّا
+    assert _ruling_rows(case_id)[0] == 1
+    record = ledger.get(_ruling_key(case_id))
+    assert record is not None
+    assert record.status is OperationStatus.FAILED_FINAL
+    assert tuple(record.applied_effect_signatures) == tuple(outcome.residual_signatures)
+
+    # والإعادةُ مرفوضةٌ: لا أثرَ فوقَ أثرٍ باقٍ (لا تُطبَّقُ الصفوفُ مرّتين)
+    _next_second()
+    with pytest.raises((IdempotencyError, DuplicateRulingError)):
+        _issue(judiciary, judge_ctx, case_id)
+    assert _ruling_rows(case_id)[0] == 1
+
+
+# ── T10 · الحلقةُ الثانيةُ — لا يُعادُ سجلُّ تعويضٍ مُغلَقٌ بلا عكسٍ ─────────────
+
+
+def test_wi105_t10_second_failed_episode_compensates_again(
+    registry: StateRegistry,
+    national: NationalRegistry,
+    judiciary: FederalJudiciary,
+    crown: AuthorizationContext,
+    monkeypatch: pytest.MonkeyPatch,
+) -> None:
+    from core.sovereignty.compensation import CompensationRequired
+
+    _bench_unused, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "t10")
+    status_before = _ruling_rows(case_id)[2]
+    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
+    original = _drop_settle(monkeypatch, ledger, "T10")
+
+    ids: list[str] = []
+    for _episode in range(2):
+        with pytest.raises(CompensationRequired) as caught:
+            _issue(judiciary, judge_ctx, case_id)
+        assert caught.value.outcome.state_is_clean is True
+        # كلُّ حلقةٍ تعكسُ صفوفَها فعلًا — القياسُ على القاعدةِ لا على الادّعاء
+        assert _ruling_rows(case_id) == (0, 0, status_before)
+        ids.append(caught.value.outcome.record.compensation_id)
+        _next_second()
+    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
+
+    assert ids[0] != ids[1]  # حلقتانِ بسجلَّينِ لا سجلٌّ مُعادٌ
+    _issue(judiciary, judge_ctx, case_id)
+    assert _ruling_rows(case_id)[:2] == (1, 1)
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3407
SHA256: 3e48e106984387db93ba65d96f685637b02f531b3db76f216bbf4a6bfce3d4ab
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 220
  عمليّاتٌ عامّةٌ مُغيِّرة   : 201
  منها تعبرُ الحدَّ        : 18
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 181
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          171 /  18 /  152
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      17  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
      15  federal/executive/services/src/amos_federation/services/governance/federation.py
      10  federal/executive/services/src/amos_federation/services/federal_state/service.py
       9  federal/executive/services/src/amos_federation/services/governance/treasury.py
       9  federal/executive/services/src/amos_federation/services/national_registry/service.py
       9  federal/executive/services/src/amos_federation/services/royal/main.py
       8  federal/executive/services/src/amos_federation/services/governance/expansion.py
       7  federal/executive/services/src/amos_federation/services/governance/learning_cycle.py
       7  federal/executive/services/src/amos_federation/services/governance/system_life.py
       7  federal/executive/services/src/amos_federation/services/state_treasury/service.py
       5  federal/executive/services/src/amos_federation/services/agent_runtime/health.py
       5  federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
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
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py
       1  federal/executive/services/src/amos_federation/services/government_services/service.py
       1  tools/migrations/r4_unify_agent_identity.py
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py -q
EXIT: 0
BYTES: 706
SHA256: dbad178a109f71fef27c702be7348d95eb207b5733fd2e6ed144cc09634b6122
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py .. [ 20%]
........                                                                 [100%]

============================== 10 passed in 5.74s ==============================
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
EXIT: 1
BYTES: 19029
SHA256: 000e60ce41ebe0915b3de76456ef69e4778cd9daecb62ea8d7c051ad9f3374f9
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 35 items

federal/executive/services/tests/test_r7d_federal_judiciary.py ......... [ 25%]
..................                                                       [ 77%]
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py E [ 80%]
EEEEEEE                                                                  [100%]

==================================== ERRORS ====================================
_ ERROR at setup of test_wi082_1_register_crosses_boundary_and_returns_same_contract _
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: FOREIGN KEY constraint failed

The above exception was the direct cause of the following exception:
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:99: in _fresh_agents
    purge_agents(session)
federal/executive/services/tests/conftest.py:201: in purge_agents
    session.execute(sa_text("DELETE FROM agents"))
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2473: in execute
    return self._execute_internal(
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2373: in _execute_internal
    result = conn.execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1463: in execute
    return meth(
.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:533: in _execute_on_connection
    return connection._execute_clauseelement(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1683: in _execute_clauseelement
    ret = self._execute_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1837: in _execute_context
    return self._exec_single_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1977: in _exec_single_context
    self._handle_dbapi_exception(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:2347: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
E   [SQL: DELETE FROM agents]
E   (Background on this error at: https://sqlalche.me/e/21/gkpj)
______ ERROR at setup of test_wi082_2_duplicate_rejected_before_boundary _______
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: FOREIGN KEY constraint failed

The above exception was the direct cause of the following exception:
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:99: in _fresh_agents
    purge_agents(session)
federal/executive/services/tests/conftest.py:201: in purge_agents
    session.execute(sa_text("DELETE FROM agents"))
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2473: in execute
    return self._execute_internal(
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2373: in _execute_internal
    result = conn.execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1463: in execute
    return meth(
.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:533: in _execute_on_connection
    return connection._execute_clauseelement(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1683: in _execute_clauseelement
    ret = self._execute_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1837: in _execute_context
    return self._exec_single_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1977: in _exec_single_context
    self._handle_dbapi_exception(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:2347: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
E   [SQL: DELETE FROM agents]
E   (Background on this error at: https://sqlalche.me/e/21/gkpj)
____ ERROR at setup of test_wi082_3_kill_switch_level_3_blocks_spawn_agent _____
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: FOREIGN KEY constraint failed

The above exception was the direct cause of the following exception:
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:99: in _fresh_agents
    purge_agents(session)
federal/executive/services/tests/conftest.py:201: in purge_agents
    session.execute(sa_text("DELETE FROM agents"))
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2473: in execute
    return self._execute_internal(
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2373: in _execute_internal
    result = conn.execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1463: in execute
    return meth(
.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:533: in _execute_on_connection
    return connection._execute_clauseelement(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1683: in _execute_clauseelement
    ret = self._execute_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1837: in _execute_context
    return self._exec_single_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1977: in _exec_single_context
    self._handle_dbapi_exception(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:2347: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
E   [SQL: DELETE FROM agents]
E   (Background on this error at: https://sqlalche.me/e/21/gkpj)
_________ ERROR at setup of test_wi082_4_level_below_3_does_not_block __________
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: FOREIGN KEY constraint failed

The above exception was the direct cause of the following exception:
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:99: in _fresh_agents
    purge_agents(session)
federal/executive/services/tests/conftest.py:201: in purge_agents
    session.execute(sa_text("DELETE FROM agents"))
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2473: in execute
    return self._execute_internal(
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2373: in _execute_internal
    result = conn.execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1463: in execute
    return meth(
.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:533: in _execute_on_connection
    return connection._execute_clauseelement(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1683: in _execute_clauseelement
    ret = self._execute_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1837: in _execute_context
    return self._exec_single_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1977: in _exec_single_context
    self._handle_dbapi_exception(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:2347: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
E   [SQL: DELETE FROM agents]
E   (Background on this error at: https://sqlalche.me/e/21/gkpj)
_________ ERROR at setup of test_wi082_5_compensator_reverses_real_row _________
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: FOREIGN KEY constraint failed

The above exception was the direct cause of the following exception:
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:99: in _fresh_agents
    purge_agents(session)
federal/executive/services/tests/conftest.py:201: in purge_agents
    session.execute(sa_text("DELETE FROM agents"))
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2473: in execute
    return self._execute_internal(
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2373: in _execute_internal
    result = conn.execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1463: in execute
    return meth(
.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:533: in _execute_on_connection
    return connection._execute_clauseelement(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1683: in _execute_clauseelement
    ret = self._execute_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1837: in _execute_context
    return self._exec_single_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1977: in _exec_single_context
    self._handle_dbapi_exception(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:2347: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
E   [SQL: DELETE FROM agents]
E   (Background on this error at: https://sqlalche.me/e/21/gkpj)
___ ERROR at setup of test_wi082_6_replay_with_missing_row_raises_divergence ___
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: FOREIGN KEY constraint failed

The above exception was the direct cause of the following exception:
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:99: in _fresh_agents
    purge_agents(session)
federal/executive/services/tests/conftest.py:201: in purge_agents
    session.execute(sa_text("DELETE FROM agents"))
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2473: in execute
    return self._execute_internal(
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2373: in _execute_internal
    result = conn.execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1463: in execute
    return meth(
.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:533: in _execute_on_connection
    return connection._execute_clauseelement(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1683: in _execute_clauseelement
    ret = self._execute_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1837: in _execute_context
    return self._exec_single_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1977: in _exec_single_context
    self._handle_dbapi_exception(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:2347: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
E   [SQL: DELETE FROM agents]
E   (Background on this error at: https://sqlalche.me/e/21/gkpj)
_______ ERROR at setup of test_wi082_7_default_authorizer_path_unchanged _______
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: FOREIGN KEY constraint failed

The above exception was the direct cause of the following exception:
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:99: in _fresh_agents
    purge_agents(session)
federal/executive/services/tests/conftest.py:201: in purge_agents
    session.execute(sa_text("DELETE FROM agents"))
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2473: in execute
    return self._execute_internal(
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2373: in _execute_internal
    result = conn.execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1463: in execute
    return meth(
.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:533: in _execute_on_connection
    return connection._execute_clauseelement(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1683: in _execute_clauseelement
    ret = self._execute_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1837: in _execute_context
    return self._exec_single_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1977: in _exec_single_context
    self._handle_dbapi_exception(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:2347: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
E   [SQL: DELETE FROM agents]
E   (Background on this error at: https://sqlalche.me/e/21/gkpj)
_____ ERROR at setup of test_wi082_8_default_authorizer_is_one_per_module ______
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlite3.IntegrityError: FOREIGN KEY constraint failed

The above exception was the direct cause of the following exception:
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:99: in _fresh_agents
    purge_agents(session)
federal/executive/services/tests/conftest.py:201: in purge_agents
    session.execute(sa_text("DELETE FROM agents"))
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2473: in execute
    return self._execute_internal(
.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2373: in _execute_internal
    result = conn.execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1463: in execute
    return meth(
.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:533: in _execute_on_connection
    return connection._execute_clauseelement(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1683: in _execute_clauseelement
    ret = self._execute_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1837: in _execute_context
    return self._exec_single_context(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1977: in _exec_single_context
    self._handle_dbapi_exception(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:2347: in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1958: in _exec_single_context
    self.dialect.do_execute(
.venv/lib/python3.12/site-packages/sqlalchemy/engine/default.py:1192: in do_execute
    cursor.execute(statement, parameters)
E   sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
E   [SQL: DELETE FROM agents]
E   (Background on this error at: https://sqlalche.me/e/21/gkpj)
=========================== short test summary info ============================
ERROR federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_1_register_crosses_boundary_and_returns_same_contract
ERROR federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_2_duplicate_rejected_before_boundary
ERROR federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_3_kill_switch_level_3_blocks_spawn_agent
ERROR federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_4_level_below_3_does_not_block
ERROR federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_5_compensator_reverses_real_row
ERROR federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_6_replay_with_missing_row_raises_divergence
ERROR federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_7_default_authorizer_path_unchanged
ERROR federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_8_default_authorizer_is_one_per_module
========================= 27 passed, 8 errors in 6.63s =========================
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && .venv/bin/python -m pytest tests/sovereignty -q
EXIT: 0
BYTES: 991
SHA256: 66d637fa06520348c3e982acd8574a4de5783a183322306262ddf468e280d1fa
NO_EOL: 0
--- OUTPUT ---
........................................................................ [  8%]
.............................s.......................................... [ 17%]
........................................................................ [ 26%]
........................................................................ [ 35%]
........................................................................ [ 43%]
........................................................................ [ 52%]
........................................................................ [ 61%]
........................................................................ [ 70%]
........................................................................ [ 79%]
........................................................................ [ 87%]
........................................................................ [ 96%]
...........................                                              [100%]
818 passed, 1 skipped in 4.64s
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
EXIT: 0
BYTES: 13324
SHA256: 15cfa58e686a3e490b5726fc7b20605fb7df2128f3ba6d0a6934da60f0ee1309
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1538 items

federal/executive/services/tests/test_1n_boundary_integration.py ....... [  0%]
...                                                                      [  0%]
federal/executive/services/tests/test_2a_precedent_correction.py ....... [  1%]
....                                                                     [  1%]
federal/executive/services/tests/test_2a_sovereign_runtime_integration.py . [  1%]
............                                                             [  2%]
federal/executive/services/tests/test_2b_government_services_sovereign.py . [  2%]
......................................                                   [  4%]
federal/executive/services/tests/test_2b_state_registry_sovereign.py ... [  4%]
..................................................                       [  8%]
federal/executive/services/tests/test_agent_runtime.py ......            [  8%]
federal/executive/services/tests/test_api_gateway.py ...                 [  8%]
federal/executive/services/tests/test_audit_canonical_record.py ........ [  9%]
..........                                                               [  9%]
federal/executive/services/tests/test_auth.py ...                        [ 10%]
federal/executive/services/tests/test_benchmark.py ..........            [ 10%]
federal/executive/services/tests/test_common_branches.py ............... [ 11%]
................................                                         [ 13%]
federal/executive/services/tests/test_config.py ...                      [ 14%]
federal/executive/services/tests/test_control_console.py ............... [ 15%]
..........                                                               [ 15%]
federal/executive/services/tests/test_critic.py ...........              [ 16%]
federal/executive/services/tests/test_durable_bus_branches.py .......... [ 17%]
.                                                                        [ 17%]
federal/executive/services/tests/test_e2e.py ...                         [ 17%]
federal/executive/services/tests/test_edge_branches.py .........         [ 17%]
federal/executive/services/tests/test_event_bus.py ..............        [ 18%]
federal/executive/services/tests/test_event_schemas.py .....             [ 19%]
federal/executive/services/tests/test_executive_core.py ................ [ 20%]
..............                                                           [ 21%]
federal/executive/services/tests/test_expansion.py ..................... [ 22%]
................                                                         [ 23%]
federal/executive/services/tests/test_experience.py ...........          [ 24%]
federal/executive/services/tests/test_federation.py .................... [ 25%]
.......................                                                  [ 26%]
federal/executive/services/tests/test_governance.py .................... [ 28%]
.......                                                                  [ 28%]
federal/executive/services/tests/test_governance_phase3.py ............. [ 29%]
............                                                             [ 30%]
federal/executive/services/tests/test_hash_chain.py ......               [ 30%]
federal/executive/services/tests/test_health.py ..............           [ 31%]
federal/executive/services/tests/test_health_system.py ................. [ 32%]
...............                                                          [ 33%]
federal/executive/services/tests/test_inmemory_stores.py ............... [ 34%]
.................                                                        [ 35%]
federal/executive/services/tests/test_king_login_boundary.py ........... [ 36%]
...........                                                              [ 37%]
federal/executive/services/tests/test_memory_service.py ........         [ 37%]
federal/executive/services/tests/test_model_gateway.py ....              [ 38%]
federal/executive/services/tests/test_model_layer.py ..............      [ 38%]
federal/executive/services/tests/test_models.py ...                      [ 39%]
federal/executive/services/tests/test_orchestrator.py .......            [ 39%]
federal/executive/services/tests/test_p13_factories_sovereign.py ....... [ 40%]
...............                                                          [ 41%]
federal/executive/services/tests/test_persistence.py ........            [ 41%]
federal/executive/services/tests/test_phase12_states.py ................ [ 42%]
.                                                                        [ 42%]
federal/executive/services/tests/test_phase13_factories.py ............. [ 43%]
                                                                         [ 43%]
federal/executive/services/tests/test_phase14_15_learning.py ........... [ 44%]
...                                                                      [ 44%]
federal/executive/services/tests/test_phase16_security.py .............. [ 45%]
..                                                                       [ 45%]
federal/executive/services/tests/test_phase17_system_life.py ........... [ 46%]
.                                                                        [ 46%]
federal/executive/services/tests/test_phase1_postgres.py ssssssss        [ 46%]
federal/executive/services/tests/test_phase1_postgres_events.py ssssssss [ 47%]
sssssssss                                                                [ 47%]
federal/executive/services/tests/test_phase2_events.py ................. [ 48%]
..........                                                               [ 49%]
federal/executive/services/tests/test_phase3_governance.py ............. [ 50%]
...........                                                              [ 51%]
federal/executive/services/tests/test_phase4_tools.py .................. [ 52%]
                                                                         [ 52%]
federal/executive/services/tests/test_phase5_models.py ...........       [ 53%]
federal/executive/services/tests/test_phase6_population.py ............. [ 53%]
..                                                                       [ 54%]
federal/executive/services/tests/test_phase7_health.py .........         [ 54%]
federal/executive/services/tests/test_population.py ..................   [ 55%]
federal/executive/services/tests/test_q19_money_delegation.py .......... [ 56%]
..................                                                       [ 57%]
federal/executive/services/tests/test_q20_money_representation.py ...... [ 57%]
.ss..................                                                    [ 59%]
federal/executive/services/tests/test_q31_money_engine_wiring.py ....... [ 59%]
.....                                                                    [ 60%]
federal/executive/services/tests/test_q32_money_enforcement_surface.py . [ 60%]
..............                                                           [ 61%]
federal/executive/services/tests/test_r1_canonical_execution_path.py ... [ 61%]
..............                                                           [ 62%]
federal/executive/services/tests/test_r2_task_execution_integration.py . [ 62%]
........................                                                 [ 63%]
federal/executive/services/tests/test_r3_agent_runtime_integration.py .. [ 63%]
...........                                                              [ 64%]
federal/executive/services/tests/test_r4_agent_identity_and_population.py . [ 64%]
...............                                                          [ 65%]
federal/executive/services/tests/test_r5_multi_provider_sandbox.py ..... [ 66%]
..............                                                           [ 66%]
federal/executive/services/tests/test_r6_1_authorization_closure.py .... [ 67%]
..............                                                           [ 68%]
federal/executive/services/tests/test_r6_identity_authorization_root.py . [ 68%]
................                                                         [ 69%]
federal/executive/services/tests/test_r7_government_services.py ........ [ 69%]
........................                                                 [ 71%]
federal/executive/services/tests/test_r7_state_registry.py ............. [ 72%]
.............                                                            [ 73%]
federal/executive/services/tests/test_r7b_state_treasury.py ............ [ 73%]
........................                                                 [ 75%]
federal/executive/services/tests/test_r7c_national_registry.py ......... [ 75%]
..........................                                               [ 77%]
federal/executive/services/tests/test_r7d_federal_judiciary.py ......... [ 78%]
..................                                                       [ 79%]
federal/executive/services/tests/test_r8_federal_state_integration.py .. [ 79%]
...............................                                          [ 81%]
federal/executive/services/tests/test_r9_national_economic_state.py .... [ 81%]
.........................................                                [ 84%]
federal/executive/services/tests/test_real_tools.py .................... [ 85%]
                                                                         [ 85%]
federal/executive/services/tests/test_shadow.py ..........               [ 86%]
federal/executive/services/tests/test_step19_durable_governance_state.py . [ 86%]
.......                                                                  [ 86%]
federal/executive/services/tests/test_step7_gate_denial.py .....         [ 87%]
federal/executive/services/tests/test_tool_registry.py .......           [ 87%]
federal/executive/services/tests/test_training.py ...............        [ 88%]
federal/executive/services/tests/test_treasury.py ...................... [ 90%]
..........                                                               [ 90%]
federal/executive/services/tests/test_w032_registry_ownership.py ....... [ 91%]
......                                                                   [ 91%]
federal/executive/services/tests/test_w033_cost_record_durability.py ... [ 91%]
......                                                                   [ 92%]
federal/executive/services/tests/test_w036_cost_precision.py ........... [ 92%]
                                                                         [ 92%]
federal/executive/services/tests/test_w166_postgres_driver_declared.py . [ 92%]
...............                                                          [ 93%]
federal/executive/services/tests/test_w190_durable_model_registry.py ..  [ 94%]
federal/executive/services/tests/test_w308_test_ledger_is_per_session.py . [ 94%]
..                                                                       [ 94%]
federal/executive/services/tests/test_wi062_migrations_cover_orm_tables.py . [ 94%]
.s                                                                       [ 94%]
federal/executive/services/tests/test_wi063_tenant_isolation_http.py ..s [ 94%]
s..ss.s..ss.s.s.s..s.s.                                                  [ 96%]
federal/executive/services/tests/test_wi064_migrations_follow_orm.py .s  [ 96%]
federal/executive/services/tests/test_wi065_orm_declares_jsonb_timestamptz.py . [ 96%]
.s                                                                       [ 96%]
federal/executive/services/tests/test_wi066_convert_create_all_databases.py . [ 96%]
sssss                                                                    [ 96%]
federal/executive/services/tests/test_wi066_pg_session_isolation.py .ss  [ 97%]
federal/executive/services/tests/test_wi067_legal_search_isolated.py ... [ 97%]
....................                                                     [ 98%]
federal/executive/services/tests/test_wi076_pg_backup_restore.py ssss    [ 98%]
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 98%]
.......                                                                  [ 99%]
federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py .. [ 99%]
........                                                                 [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w605/grok_4_7/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========== 1485 passed, 53 skipped, 1 warning in 263.24s (0:04:23) ============
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
EXIT: 0
BYTES: 34186
SHA256: 28a9182240a7c4ea2c62b488735d939b40568f314f323dce63a0f382d0fe779d
NO_EOL: 0
--- OUTPUT ---
# J1 · WI-105 — تصميمُ عبورِ `issue_ruling` الحدَّ السياديَّ بفاعلٍ قضائيٍّ مُعلَنٍ (Q-6 ①)

<!--
الهدف: وثيقةُ تصميمِ الدفعةِ J1 من خطّةِ حرقِ D-4 — عبورُ إصدارِ الحكمِ الحدَّ السياديَّ بفاعلٍ قضائيٍّ مُعلَنٍ، تُلتزَمُ قبلَ أيِّ شِفرةٍ
النطاق: بندُ WI-105 (federal-executive · services/federal_judiciary + جسرُ executive_core) — فئةُ التغييرِ C3 (حسّاسٌ: سيادةٌ بقائمةِ Q-H)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — بتوجيهِ المالكِ 17 § 3 المرحلةُ 1 — لا شِفرةَ قبلَ اعتمادِ هذه الوثيقةِ
تاريخ الإنشاء: 2026-10-21
<!-- آخر تعديل: 2026-10-22 (W-602 — ملحقُ تصميمٍ مؤرَّخٌ § 7: وصلُ التعويضِ الآليِّ في الحدِّ بقرارِ المالكِ Q-70) · ووقبله 2026-10-21 (W-593 — إضافتان مؤرَّختان: الجيلُ في هدفِ العبورِ · وقياسُ T6 عبرَ حارسِ 1I) -->
-->

> **السند:** قرارُ المالكِ **Q-6 ①** (W-363): «قضاءٌ مستقلٌّ بفاعلٍ قضائيٍّ مُعلَنٍ ← لا يخلطُ السلطاتِ ولا يحتاجُ تفويضًا لكلِّ فعلٍ» — ويفتحُ هجرةَ `federal_judiciary` «في T1 بعدَ هجرةِ Q-15» · وهجرةُ Q-15 (`WI-082`) صارت `VERIFIED` بإجماعِ المجلسِ في `W-576` · والدفعةُ في `HANDOFFS/D4-BURN-PLAN.md` باسمِ **J1**.
> **البروتوكولُ (C3):** هذه الوثيقةُ في التزامٍ يسبقُ الشِفرةَ · ثمَّ جولةُ مجلسٍ على الوثيقةِ · ثمَّ عرضُها على المالكِ · **ولا شِفرةَ قبلَ الموافقةِ** (التوجيهُ 17 § 3 · المرحلةُ 1 · البندُ 4).
> **كلُّ رقمٍ هنا مقيسٌ في W-581 على العقدةِ `2694796`** بالأمرِ المذكورِ بجانبِه — ويُعادُ قياسُه في الدفعةِ التي تُنفِّذُ.

## 1. الوضعُ المقيسُ

### 1.1 الموضعانِ في الجرد

`sovereign_write_inventory.py --service …/federal_judiciary --json` (27 موضعًا في الوحدةِ · كلُّها غيرُ محروسةٍ):

| الموضع | الكتابة | الحالة |
|---|---|---|
| `rulings.py::issue_ruling` | `add()` (صفُّ الحكمِ) ثمَّ `flush` ثمَّ `docket.record_proceeding` ثمَّ `docket.advance_case` | دَينٌ |
| `service.py::FederalJudiciary.issue_ruling` | `commit()` | دَينٌ |

قاعدةُ الأداةِ (رأسُ `sovereign_write_inventory.py`): **الموضعُ محروسٌ إن ظهرَ `guard_declared(` في جسمِ الدالّةِ العامّةِ نفسِها** — لا يكفي أن يعبرَ معاونٌ · ومعاونٌ خاصٌّ يكتبُ ولا تصلُ إليه عمليّةٌ عامّةٌ في وحدتِه يُحصى موضعًا مستقلًّا (فإعادةُ التسميةِ إلى `_` لا تُخفي شيئًا).

### 1.2 النداءات

- إنتاجيًّا: **1** — `service.py:672` يُنادي `rulings.issue_ruling` · ولا مُنادٍ آخرَ (`rg 'rulings\.issue_ruling|issue_ruling\('`).
- الاختباراتُ: **18** نداءً لـ`judiciary.issue_ruling` (الخدمة) في `tests/test_r7d_federal_judiciary.py` — منها مسارُ «الحكمُ البديلُ بعدَ الإلغاءِ» (السطورُ 1049–1075).
  - **[W-584 · 2026-10-21 · تصحيحٌ بالإضافةِ لا بالمحوِ — `DISC-124`]** المقيسُ **15** لا 18: `rg -c "judiciary\.issue_ruling\(" federal/executive/services/tests/test_r7d_federal_judiciary.py` ⇒ `15` · و`rg -c "\.issue_ruling\("` على `federal/executive/services/tests` كلِّها ⇒ ملفٌّ واحدٌ · 15 — فلا نداءَ في غيرِه. والرقمُ 18 أعلاه باقٍ تاريخًا بنِسبتِه (W-581) · ولا أثرَ له في التصميمِ: المعيارُ «test_r7d كاملًا بلا تعديلٍ» لا يتوقّفُ على العدِّ.

### 1.3 الحدُّ اليومَ — ثلاثُ حقائقَ مقيسةٍ تُغيِّرُ التصميمَ عن WI-082

مقيسةٌ بـ`docs/audit/evidence/W-581/probe_issue_ruling_actors.py` (المخرجُ كاملًا بجانبِه):

1. **الجسرُ لا يحملُ طلبَ الاختصاصِ:** `ConstitutionalAuthorizer.guard_declared` (`sovereignty_bridge.py:355`) لا يقبلُ `judicial_action` ولا يُمرِّرُه، والحدُّ الجوهريُّ `EnforcementBoundary.execute` يقبلُه (`enforcement_boundary.py:300`) ويرفضُ كلَّ فعلٍ في `JUDICIAL_ACTIONS` بلا طلبٍ (`_guard_jurisdiction` · `JurisdictionNotDeclaredError`) ⇒ **عبرَ الجسرِ اليومَ يُرفَضُ `issue_ruling` لكلِّ فاعلٍ بلا استثناءٍ (6/6)** — فلا تُهاجَرُ الدفعةُ بلا توسيعِ الجسرِ.
2. **الحكمُ عبرَ الحدِّ الجوهريِّ بطلبِ اختصاصٍ ومُعوِّضٍ:** `JUDICIAL` ⇒ تنفيذٌ · `EXECUTIVE` و`LEGISLATIVE` و`TREASURY` ⇒ `SovereigntyViolation` (A003 · الفصلُ بينَ السلطاتِ) · **و`AGENT` و`SYSTEM` ⇒ تنفيذٌ** (يُراجَعانِ في طبقةِ `AGENT` وقاعدةُ الحصرِ `_BRANCH_EXCLUSIVE` في `rules.py:272` تخصُّ الفروعَ وحدَها) — **اكتشافُ `DISC-121`** وسؤالُ `Q-68` للمالكِ · خارجَ J1 ولا تحسمُه J1.
3. **الجدارُ يعملُ:** نطاقُ محكمةٍ ≠ نطاقِ قضيّةٍ ⇒ `JurisdictionError` · ونطاقُ منصبٍ `DEPARTMENT` ⇒ `JurisdictionError` · وأثرٌ مُغيِّرٌ بلا مُعوِّضٍ ⇒ `CompensationNotDeclaredError`.

وحقيقتانِ أُخرَيانِ: `issue_ruling` **غيرُ مُدرَجٍ في أيِّ مستوًى** من `KILL_SWITCH_BLOCKS` (`rules.py:141`) · و`JUDICIAL_EFFECT_KINDS` = {CREATE · WRITE · READ} و`DELETE` في `NON_JUDICIAL_EFFECT_KINDS` («الحذفُ شأنٌ تنفيذيّ» — `jurisdiction.py:152–167`).

## 2. التصميم

### D1 · الفاعلُ القضائيُّ المُعلَنُ — ثابتٌ في الوحدةِ لا معاملٌ للمُنادي

- `federal_judiciary/rulings.py`: `JUDICIARY_ACTOR = "JUDICIAL"` ومُفوِّضٌ افتراضيٌّ كسولٌ `_judiciary_authorizer()` على مثالِ `agent_identity._default_authorizer` (WI-082).
- **فرقٌ مقصودٌ عن WI-082:** لا يُضافُ معاملٌ عامٌّ `authorizer=` إلى `rulings.issue_ruling` ولا إلى الخدمة. السببُ مقيسٌ (§ 1.3 · 2): من يملكُ أن يُمرِّرَ مُفوِّضًا بفاعلِ `AGENT` يُصدِرُ حكمًا اليومَ. فاختيارُ الفاعلِ يبقى في الوحدةِ وحدَها (نصُّ Q-6: «فاعلٌ قضائيٌّ مُعلَنٌ»).
- الاختبارُ يُبدِّلُ الفاعلَ بـ`monkeypatch` على ثابتِ الوحدةِ (ويُفرِغُ المُفوِّضَ المحفوظَ) لا بمعاملٍ إنتاجيٍّ.
- البديلُ المرفوضُ: معاملٌ اختياريٌّ كـWI-082 — يُبقي ثغرةَ `DISC-121` مفتوحةً لكلِّ مُنادٍ.

### D2 · توسيعُ الجسرِ — `judicial_action` اختياريٌّ يُمرَّرُ كما هو

- `sovereignty_bridge.py`: `guard_declared(..., judicial_action: Any | None = None)` في البروتوكولِ (`:128`) والتنفيذِ (`:355`) — ويُمرَّرُ إلى `self.boundary.execute(..., judicial_action=judicial_action)`.
- **بلا أثرٍ على غيرِ القضائيِّ:** القيمةُ الافتراضيّةُ `None` هي افتراضُ `execute` نفسِه، فكلُّ نداءٍ قائمٍ يبقى بايتًا ببايتٍ في سلوكِه — ويُثبَتُ ذلك بتشغيلِ فحوصِ WI-082 وحزمةِ الجسرِ كاملةً بلا تعديلٍ.
- لا يُخفَّفُ شيءٌ: الجسرُ لا يقرِّرُ الاختصاصَ، الجدارُ (`JudicialJurisdictionWall.evaluate`) يقرِّرُه.

### D3 · طلبُ الاختصاصِ منَ البياناتِ الحيّةِ لا من ثوابتَ

`JudicialAction(action="issue_ruling", court_scope=…, case_scope=…, actor_scope=…, target=…, institution_id=…, case_institution_id=…)`:

| الحقل | المصدر | ملاحظة |
|---|---|---|
| `court_scope` | `authority.jurisdiction` (= `court.jurisdiction`) | موجودٌ اليومَ |
| `case_scope` | `case.jurisdiction` | موجودٌ اليومَ |
| `actor_scope` | `holding.authority_scope` | **حقلٌ جديدٌ `position_scope` في `JudicialAuthority`** (إضافةٌ لا تغييرٌ — يُملأُ في `require_judicial_authority`) |
| `institution_id` | `authority.institution_id` (= `court.institution_id`) | موجودٌ |
| `case_institution_id` | `court.institution_id` | القضيّةُ بلا عمودِ مؤسّسةٍ؛ مؤسّستُها مؤسّسةُ محكمتِها (`models.py` · `LegalCaseModel`) — مُعلَنٌ لا مُخمَّنٌ |
| `is_royal_decree_target` | `False` | إصدارُ الحكمِ هنا على قضيّةٍ لا على مرسومٍ · والجدارُ يقبلُ `issue_ruling` على المرسومِ أصلًا (`jurisdiction.py:341`) |

فالفحصُ المكرَّرُ اليومَ في `authority.py` (`assert_scope_covers_court` · `assert_jurisdiction_match`) يُفحَصُ ثانيةً في الحدِّ نفسِه — ازدواجٌ مقصودٌ: الأوّلُ قاعدةُ نطاقٍ قبلَ الحدِّ، والثاني قرارُ الحدِّ.
ملاحظةٌ مقيسةٌ عرَضًا (لا تُصلَحُ في J1): `authority.py:281` يمرِّرُ `case_institution_id=court.institution_id` لا مؤسّسةَ القضيّةِ — وهو مسارٌ `pragma: no cover` ولا عمودَ للقضيّةِ أصلًا؛ يُذكَرُ ولا يُغيَّرُ.

### D4 · موضعُ العبورِ ومِلكيّةُ المعاملةِ — العبورُ حيث الكتابةُ

- **العبورُ في `rulings.issue_ruling`** (حيث يُكتَبُ الصفُّ): جسمُها يحملُ `guard_declared(` والمُطبِّقُ يُنفِّذُ `add` + `flush` + `record_proceeding` + `advance_case` **+ `session.commit()`** في معاملةٍ واحدةٍ.
- **`service.issue_ruling` يفقدُ `session.commit()`** (الالتزامُ صارَ داخلَ العبورِ) ويبقى مالكَ الجلسةِ (`session.close()` في `finally`) والنشرِ والأثرِ.
- **أثرُه في الجردِ (يُعلَنُ قبلَ القياسِ):** `rulings.issue_ruling` محروسٌ (sovereign 17 ← 18) · و`service.issue_ruling` **يخرجُ من الجردِ لأنّه لم يعدْ يكتبُ** (أسطحٌ 220 ← 219) · **D-4: 183 ← 181**. وهذا ليس تجميلًا للعدِّ: الكتابةُ الوحيدةُ للحكمِ صارت خلفَ الحدِّ، والخدمةُ مُنسِّقٌ لا كاتبٌ. **نقطةُ حكمٍ للمجلسِ.**
  - **[W-588 · 2026-10-21 · تصحيحٌ بالإضافةِ لا بالمحوِ — `DISC-126` · وجدَه مقعدُ grok_4_7 في جولةِ W-585]** «أسطحٌ 220 ← 219» **غلطٌ**: المُطبِّقُ (`_apply`) دالّةٌ متداخلةٌ خاصّةٌ داخلَ `rulings.issue_ruling` على نمطِ WI-082 (`agent_identity._apply`)، وهي تحملُ `add` + `session.commit()` فتُحصى موضعَ كتابةٍ مستقلًّا (public=False) ⇒ **أسطحٌ 220 ← 220** (‏−1 بخروجِ `service.issue_ruling` · +1 بالمُطبِّقِ) · والدَّينُ **183 ← 181** والسياديُّ **17 ← 18** على حالِهما (المُطبِّقُ غيرُ عامٍّ فلا يدخلُ مقامَ الدَّينِ) · الدليلُ `evidence/W-587/coordinator_check_grok_d4.txt`. **وشكلُ المُطبِّقِ يصيرُ جزءًا من التصميمِ لا تفصيلَ تنفيذٍ**: دالّةٌ متداخلةٌ خاصّةٌ واحدةٌ — فإن نفّذَها المنفِّذُ بغيرِ هذا الشكلِ تغيّرَ عدُّ الأسطحِ ووجبَ إعلانُه قبلَ القياسِ.
- البديلُ A2: العبورُ في الخدمةِ ويبقى `rulings.issue_ruling` عامًّا بلا عبورٍ ⇒ مدخلٌ عامٌّ يكتبُ حكمًا متجاوزًا الحدَّ (183 ← 182) — **مرفوضٌ**: الثغرةُ تبقى.
- البديلُ A3: عبورانِ متداخلانِ (الخدمةُ ثمَّ `rulings`) ⇒ قراران في سجلِّ البوابةِ ومفتاحا ذرّيّةٍ لحكمٍ واحدٍ — **مرفوضٌ**: سجلٌّ مُضلِّلٌ.

### D5 · الأثرُ المُعلَنُ — أثرٌ واحدٌ لمعاملةٍ واحدةٍ

`declared_effect("CREATE", f"judiciary/rulings/{case_id}/{stage}", "حكمٌ في المرحلة … وإجراؤه وانتقالُ القضيّةِ إلى decided")` — `CREATE` ∈ `JUDICIAL_EFFECT_KINDS` فيمرُّ `assert_effect_judicial`. الصفوفُ الثلاثةُ (الحكمُ · الإجراءُ · حالةُ القضيّةِ) تُلتزَمُ معًا أو لا يُلتزَمُ شيءٌ، فإعلانُها ثلاثةَ آثارٍ يَعِدُ بتطبيقٍ جزئيٍّ لا يقعُ.

**[إضافةٌ مؤرَّخةٌ (2026-10-21 · `W-593` · اكتشافُ تنفيذٍ أُثبِتَ بالفحصِ قبلَ الدفعِ):]** هدفُ العبورِ وموردُ الأثرِ يحملانِ الجيلَ أيضًا: `judiciary/rulings/{case_id}/{stage}/g{n}` — لا `f"{case_id}/{stage}"` وحده. السببُ مقيسٌ: بصمةُ العقدِ تُشتقُّ من (الفاعلِ · الفعلِ · الهدفِ · الآثارِ) فقط، ومعرِّفُ الإذنِ `EP-{contract}-{ثانيةٌ}` بدقّةِ الثانيةِ، فحكمانِ للمرحلةِ نفسِها في الثانيةِ نفسِها يتصادمانِ في الإذنِ نفسِهِ ويُرفضُ البديلُ بعدَ الإلغاءِ رفضَ إعادةِ إذنٍ (`PermitReplayError` — قِيسَ في T4 قبلَ التصحيحِ). والجيلُ جزءُ هويةِ العمليّةِ في المفتاحِ والهدفِ معًا، فالدلالةُ كما هي: أثرٌ واحدٌ لمعاملةٍ واحدةٍ (D5).

### D6 · مفتاحُ الذرّيّةِ — بجيلِ الإلغاءِ لا بالمرحلةِ وحدَها

- `operation_key("judiciary.ruling.issue", f"{case_id}:{stage}:g{n}")` و`n` = عددُ الأحكامِ المُلغاةِ (`vacated`) للقضيّةِ في المرحلةِ — يُقرأُ قبلَ الحدِّ.
- **لماذا لا `case_id:stage`:** بعدَ الإلغاءِ يُسمَحُ حكمٌ بديلٌ للمرحلةِ نفسِها (الاختبارُ القائمُ 1069) — فمفتاحٌ بلا جيلٍ يُعيدُ الحكمَ الأوّلَ «إعادةً» ولا يكتبُ البديلَ.
- **ترتيبٌ ملزِمٌ:** فحصُ «حكمٌ قائمٌ للمرحلةِ» (`DuplicateRulingError`) يبقى **قبلَ** الحدِّ — وإلّا عادَ الطلبُ الثاني إعادةً صامتةً للأوّلِ (المفتاحُ نفسُه `g0`) بدلَ الرفضِ الذي يفرضُه الاختبارُ القائمُ (السطورُ 1055–1061).
- **الإعادةُ:** إن رجعَ الحدُّ `is_replay` يُقرأُ الحكمُ القائمُ للمرحلةِ؛ فإن غابَ رُفِعَ `RulingLedgerDivergenceError` (على مثالِ `IdentityLedgerDivergenceError` في WI-082) — لا كتابةَ ثانيةً خارجَ الحدِّ.

### D7 · المُعوِّضُ — استعادةٌ تقنيّةٌ دقيقةٌ أم إلغاءٌ قضائيٌّ؟ (نقطةُ حكمٍ)

متى يعملُ (مقيسٌ في `compensation.py:797–808`): بعدَ تسجيلِ الأثرِ «مُطبَّقًا» وفشلِ خطوةٍ لاحقةٍ (مثلًا تثبيتُ النجاحِ في سجلِّ الذرّيّةِ) — أي والصفوفُ مُلتزَمةٌ.

| الخيار | ما يفعل | له | عليه |
|---|---|---|---|
| **(أ) الاستعادةُ التقنيّةُ — التوصية** | في جلسةٍ جديدةٍ: حذفُ صفِّ الإجراءِ (آخرُ تسلسلٍ للقضيّةِ) وصفِّ الحكمِ بمعرِّفَيهما، وإرجاعُ حالةِ القضيّةِ إلى ما كانت قبلَ العمليّةِ (تُحفَظُ قبلَ الحدِّ) | الحالةُ ترجعُ كما كانت بالضبطِ (`state_is_clean`) · والعمليّةُ لم تثبتْ فلا حكمَ قانونيًّا وُجِدَ | «الحذفُ شأنٌ تنفيذيّ» — والمُعوِّضُ ليس أثرًا مُعلَنًا ولا تراجعُه البوابةُ، فيُكتَبُ ذلك في شِفرتِه صريحًا |
| (ب) الإلغاءُ القضائيُّ | `status="vacated"` بسببٍ «تعويضٌ: لم يثبتْ نجاحُ العمليّةِ» | لا حذفَ | القضيّةُ تبقى `decided` بلا حكمٍ قائمٍ — حالةٌ متناقضةٌ · ويرفعُ جيلَ المفتاحِ (D6) بحكمٍ لم يصدرْ |

### D8 · ما يبقى قبلَ الحدِّ (قراءاتٌ لا كتابات)

`require_domain_permission` · `require_tenant` · `require_judicial_authority` (PROVEN) · فحوصُ المدخلِ (المرحلة · القرار · المنطوق) · فحصُ الحكمِ القائمِ · قراءةُ جيلِ الإلغاءِ وحالةِ القضيّةِ السابقةِ. ترتيبُ الأخطاءِ المرئيُّ للمُنادي لا يتغيّرُ.

### D9 · ما لا يتغيّرُ ويُعلَنُ

- زرُّ الإيقافِ: `issue_ruling` غيرُ مُدرَجٍ في أيِّ مستوًى — لا تُضيفُه J1 (مستويات الإيقافِ قرارُ مالكٍ).
- `rules.py` و`jurisdiction.py` و`royal/`: لا مساسَ · وثغرةُ `DISC-121` لا تُصلَحُ هنا (`Q-68`).
- `vacate_ruling` (J2) · `record_proceeding` العامُّ (J3) · وبقيّةُ الوحدةِ: خارجَ J1.

## 3. الفحوصُ والطفراتُ (تُكتَبُ في الدفعةِ المنفِّذةِ)

ملفٌّ جديدٌ `federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py`:

| الفحص | يُثبِت |
|---|---|
| T1 · ALLOW للقضائيّ | الحكمُ يصدرُ عبرَ الخدمةِ · وآخرُ قرارٍ في سجلِّ البوابةِ `issue_ruling` بفاعلِ `judicial` · والصفوفُ الثلاثةُ مُلتزَمةٌ |
| T2 · DENY للتنفيذيّ | `JUDICIARY_ACTOR="EXECUTIVE"` ⇒ `SovereigntyViolation` · لا صفَّ حكمٍ · لا إجراءَ · حالةُ القضيّةِ كما كانت |
| T3 · الاختصاصُ منَ البيانات | الطلبُ المُمرَّرُ يحملُ `case.jurisdiction` و`position_scope` الحقيقيَّينِ (جاسوسٌ على `boundary.execute`) |
| T4 · البديلُ بعدَ الإلغاء | حكمٌ ← إلغاءٌ ← بديلٌ = صفّانِ بمفتاحَي `g0` و`g1` |
| T5 · المكرَّرُ قبلَ الحدّ | الطلبُ الثاني للمرحلةِ ⇒ `DuplicateRulingError` ولا قرارَ جديدٌ في سجلِّ البوابةِ |
| T6 · المُعوِّض | إسقاطُ تثبيتِ النجاحِ بعدَ الالتزامِ ⇒ `CompensationRequired` و`state_is_clean` والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ |
  **[إضافةٌ مؤرَّخةٌ (2026-10-21 · `W-593` · اكتشافُ تنفيذٍ):]** مسارُ الحدِّ أحاديَّ الأثرِ ينفّذُ عبرَ `IdempotencyGuard.run_once` لا عبرَ معاملةِ 1I المُعوَّضةَ (`run_compensated_transaction` موجودةٌ في `compensation.py` ولا مُناديَ إنتاجيًّا لها)، فالتعويضُ الآليُّ غيرُ موصولٍ في هذا المسارِ. فيُقاسُ T6 كما تقيسُهُ حوكمةُ 1I: بإسقاطِ تثبيتِ النجاحِ بعدَ الالتزامِ (الصفوفُ مُلتزَمةٌ والسجلُّ RUNNING) ثمّ التعويضِ بحارسِ 1I (`CompensationGuard.compensate`) بالعقدِ والخطةِ المربوطتينِ منَ العبورِ الحقيقيِّ نفسِهِ — والحصيلةُ `state_is_clean` والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ. ووصلُ التعويضِ الآليِّ في `enforcement_boundary.py` خارجَ ملفّاتِ J1 (§ 5) فيُترَكُ قرينةً للمجلسِ لا يقرّرُهُ المنفِّذُ. |
| T7 · التفرُّق | إعادةٌ وصفُّ الحكمِ غائبٌ ⇒ `RulingLedgerDivergenceError` |

الطفراتُ (تُشغَّلُ على نسخةٍ مؤقّتةٍ وتُقيَّدُ مخرجاتُها):
- **M1 · حذفُ العبورِ** (المُطبِّقُ يُنادى مباشرةً بلا `guard_declared`) ⇒ يسقطُ T1 وT2 (شرطُ التوجيهِ 17).
- M2 · مفتاحٌ بلا جيلٍ ⇒ يسقطُ T4.
- M3 · فحصُ المكرَّرِ بعدَ الحدِّ ⇒ يسقطُ T5.
- M4 · `judicial_action=None` في `rulings` ⇒ يسقطُ T1 (`JurisdictionNotDeclaredError`).

## 4. معيارُ القبولِ الرقميُّ

1. `sovereign_write_inventory.py`: **debt 183 ← 181** · sovereign 17 ← 18 · أسطحٌ 220 ← 219 (**[W-588] الصحيحُ 220 ← 220** — المُطبِّقُ المتداخلُ الخاصُّ يُحصى موضعًا · `DISC-126`) · بلا نموٍّ في غيرِ الوحدةِ.
2. T1–T7 ناجحةٌ · M1–M4 كلٌّ يُسقِطُ فحصَه.
3. `test_r7d_federal_judiciary.py` كاملًا بلا تعديلٍ (18 نداءً — **[W-584] المقيسُ 15** · `DISC-124`) · وفحوصُ WI-082 والجسرِ بلا تعديلٍ.
4. حزمُ services كاملةً خضراءَ في CI مقروءًا على العقدةِ نفسِها.
5. مراجعةٌ تُعيدُ التشغيلَ (Q-H) — ولا VERIFIED بيدِ المنفِّذِ.

## 5. الملفّاتُ التي ستُمَسُّ (ولا غيرُها)

`executive_core/sovereignty_bridge.py` · `federal_judiciary/rulings.py` · `federal_judiciary/service.py` · `federal_judiciary/authority.py` · `tests/test_wi105_issue_ruling_sovereign.py` (جديد) · دعاوى عددِ الحزمةِ في `docs/PROJECT_HANDBOOK.md`.

## 6. نقاطُ الحكمِ المطلوبةُ (للمجلسِ ثمَّ للمالكِ)

| النقطة | السؤال | التوصية |
|---|---|---|
| D1 | الفاعلُ ثابتٌ في الوحدةِ بلا معاملٍ عامٍّ؟ | نعم |
| D4 | العبورُ في `rulings` والالتزامُ داخلَه فتخرجُ الخدمةُ منَ الجردِ (183 ← 181)؟ | نعم |
| D6 | المفتاحُ بجيلِ الإلغاءِ والمكرَّرُ قبلَ الحدِّ؟ | نعم |
| D7 | المُعوِّضُ (أ) الاستعادةُ التقنيّةُ أم (ب) الإلغاءُ؟ | (أ) |

لا نقطةَ منها تمسُّ سؤالًا سياديًّا غيرَ محسومٍ: الفاعلُ محسومٌ بـQ-6 ① · وثغرةُ AGENT/SYSTEM منفصلةٌ في `Q-68` ولا تعتمدُ J1 عليها.

---

## 7. ملحقُ التصميمِ — وصلُ التعويضِ الآليِّ في الحدِّ (إضافةٌ مؤرَّخةٌ · 2026-10-22 · `W-602` · قرارُ المالكِ Q-70)

> **السند:** قرارُ المالكِ **Q-70** (التوجيهُ 18 § 1 · [السجلُّ السياديُّ](SOVEREIGN_DECISION_REGISTER.md)): «خيار (1) مشروطًا. يُوصَل التعويض الآلي بعد قياس موضع الفجوة … في الحالتين: لا خيار (2) (الحالة النصفية لا تُقبل في القضاء).» · والقياسُ الشرطيُّ في `W-601` ([`evidence/W-601/probe_output_before_fix.txt`](evidence/W-601/probe_output_before_fix.txt)). **هذا الملحقُ يُلتزَمُ قبلَ الشِّفرةِ** (التوجيهُ 18 § 2) ولا يمسُّ النصَّ أعلاه: § 5 («الملفّاتُ التي ستُمَسُّ») يُوسَّعُ بملفٍّ واحدٍ هو `core/sovereignty/enforcement_boundary.py` بالفرعِ الأولِ من القرارِ.

### 7.1 الموضعُ — مقيسًا لا مُفترَضًا
- **السطحانِ المُهجَّرانِ يتصرّفانِ تصرُّفًا واحدًا** عندَ إسقاطِ `IdempotencyLedger.mark_succeeded` بعدَ التزامِ المُطبِّقِ: `issue_ruling` (J1) و`register_identity` (WI-082) كلاهما `RuntimeError` خامٌ · الصفوفُ مُلتزَمةٌ · نداءاتُ `CompensationGuard.compensate` **0** · سجلُّ الذرّيّةِ عالقٌ `RUNNING` · الإعادةُ تُرفَضُ بخطأِ التكرارِ.
- **الجذرُ:** `SovereignExecutionBoundary.execute` يربطُ خطّةَ 1I (الخطوةُ ③) ثمَّ يُنفِّذُ عبرَ `IdempotencyGuard.run_once` (الخطوةُ ⑦) ولا يُنادي `CompensationGuard` في أيِّ مسارٍ — وترويسةُ الملفِّ تُعلِنُه قرارًا: «ولا يبني استعادةً ولا تعويضًا تشغيليًّا — يفرضُ **ربطَ** الخطّةِ فقط». و`run_compensated_transaction` في `compensation.py` بلا مُنادٍ إنتاجيٍّ (إضافةُ W-593 في § 3).
- **فالوصلُ في الحدِّ مرّةً واحدةً** يشملُ كلَّ سطحٍ مُهجَّرٍ يعبرُ `guard_declared` (J1 · WI-082 · وما يليهما) — لا في ملفّاتِ J1.

### 7.2 النصُّ المقترحُ للوصلِ (`enforcement_boundary.py` وحدَه)
1. **حقلٌ اختياريٌّ في الحدِّ:** `compensation_journal: CompensationJournal | None = None`. فإن لم يُمرَّرْ اشتُقَّ مسارُه بجانبِ سجلِّ الذرّيّةِ: `<ledger.stem>.compensation.json` في الدليلِ نفسِه — فلا يتغيّرُ الجسرُ (`sovereignty_bridge.py`) ولا أيُّ مُنشِئٍ قائمٍ.
2. **تتبُّعُ ما طُبِّقَ فعلًا:** المُطبِّقُ المُوجَّهُ (`_route_effect`) يُلَفُّ بمُتتبِّعٍ يُضيفُ بصمةَ الأثرِ الداخليِّ **بعدَ** عودةِ مُطبِّقِ المُنادي بنجاحٍ (دلالةُ 1H نفسُها في `run_effects_once`). الأثرُ الخارجيُّ يُدرَجُ في الصادرِ (1K) ولا يُعوَّضُ هنا.
3. **اللفُّ:** نداءُ `run_once` يُلَفُّ؛ فإن رفعَ استثناءً:
   - **ولم يُطبَّقْ أثرٌ** (الخطّةُ `None` أو المُتتبِّعُ فارغٌ) ⇒ يُعادُ رفعُ الاستثناءِ **كما هو** بلا لفٍّ — فاستثناءاتُ الحرسِ (الإذنُ · الاختصاصُ · التكرارُ · الإيقافُ) وفشلُ المُطبِّقِ قبلَ أيِّ أثرٍ لا تتغيّرُ أنواعُها (يحرسُه `test_2b_government_services_sovereign.py::test_09` بلا تعديلٍ).
   - **وطُبِّقَ أثرٌ أو أكثرُ** ⇒ `CompensationGuard(journal, IdempotencyGuard(ledger)).compensate(contract=…, plan=…, operation_key=<مفتاحُ الحلقةِ>, applied_signatures=<المُتتبَّعُ>, reason=<نوعُ الاستثناءِ ونصُّه>)` بترتيبٍ عكسيٍّ (LIFO)، ثمَّ `raise CompensationRequired(outcome) from exc` — **دائمًا يُرفَعُ ولا يُبتلَعُ**؛ والأصلُ محفوظٌ في `__cause__`.
4. **مفتاحُ الحلقةِ (اكتشافُ تصميمٍ):** معرِّفُ التعويضِ مُشتقٌّ من مضمونِ العقدِ والمفتاحِ والآثارِ (`compute_compensation_id`) والعقدُ مُشتقٌّ من مضمونِه ⇒ لو عُوِّضَت محاولةٌ ثمَّ فشلت إعادتُها بالطريقةِ نفسِها لأرجعَ الحارسُ السجلَّ المُغلَقَ القديمَ **بلا عكسٍ** ولادّعى النظافةَ والصفوفُ قائمةٌ. فيُمرَّرُ إلى `compensate` مفتاحٌ مشتقٌّ للحلقةِ: `IdempotencyKey(scope, f"{value}@attempt{n}")` حيثُ `n` عددُ محاولاتِ السجلِّ — ومفتاحُ الذرّيّةِ نفسُه لا يتغيّرُ.

### 7.3 ما يُحفَظُ — حالةُ القضيّةِ ومفتاحُ الذرّيّةِ
- **حالةُ الدولةِ:** يعكسُها مُعوِّضُ السطحِ المُعلَنُ (J1: حذفُ صفِّ الحكمِ وإجراءِ RULING وإعادةُ حالةِ القضيّةِ السابقةِ — D7-أ · WI-082: حذفُ صفِّ الهويّةِ). لا يُضيفُ الحدُّ مُعوِّضًا ولا يُغيّرُ مُعوِّضًا.
- **مفتاحُ الذرّيّةِ عندَ النظافةِ** (`state_is_clean`): يُنقَلُ السجلُّ إلى `FAILED_RETRYABLE` بآثارٍ مطبَّقةٍ `()` وسببٍ يحملُ معرِّفَ التعويضِ — **الدلالةُ نفسُها التي تكتبُها `run_compensated_transaction`** — فالإعادةُ بالمفتاحِ نفسِه جائزةٌ (الحالةُ رجعت والفحصُ النطاقيُّ للتكرارِ لا يجدُ صفًّا).
- **سجلُّ التعويضِ:** دفترُ 1I يحفظُ الحلقةَ كاملةً (فتحٌ · كلُّ أثرٍ قبلَ عكسِه · الحصيلةُ).

### 7.4 سلوكُ التعويضِ عندَ فشلِه هو نفسُه
- مُعوِّضٌ يرفعُ ⇒ `CompensationGuard` يسجّلُه ولا يبتلعُه: الحصيلةُ `COMPENSATION_FAILED`/`PARTIALLY_COMPENSATED` · `state_is_clean = False` · `requires_human = True` · والباقي نافذًا مُسمًّى في `residual_signatures`.
- الحدُّ يرفعُ `CompensationRequired` بهذه الحصيلةِ (نصُّه يُسمّي الباقي ويقولُ «يلزمُ قرارٌ بشريّ») · وينقلُ سجلَّ الذرّيّةِ إلى **`FAILED_FINAL`** بالباقي في `applied_effect_signatures` ⇒ **إغلاقٌ عندَ الفشلِ**: أيُّ إعادةٍ بالمفتاحِ نفسِه تُرفَضُ (لا انتقالَ من النهائيِّ) فلا يُطبَّقُ أثرٌ فوقَ أثرٍ باقٍ — والحسمُ بيدِ إنسانٍ (الدَّينُ معلَنٌ في دفترِ التعويضِ).
- **وإن فشلَ نقلُ سجلِّ الذرّيّةِ نفسُه** (كأن يكونَ السجلُّ هو المعطوبَ): يبقى `CompensationRequired` هو المرفوعَ (حالةُ الدولةِ هي الحقيقةُ المقيسةُ) ويُلحَقُ به نصُّ عطبِ النقلِ (`add_note`) · ويبقى السجلُّ على حالِه (`RUNNING`) فتُرفَضُ الإعادةُ بتعارضٍ — إغلاقٌ لا فتحٌ.

### 7.5 الحدودُ المعلنةُ (لا تُطوى)
- مُطبِّقٌ يلتزمُ ثمَّ يرفعُ **قبلَ أن يعودَ** لا يُتتبَّعُ أثرُه (لم يُعلِنْ نجاحَه) — والسطحانِ يلتزمانِ في آخرِ سطرٍ من مُطبِّقَيهما. هذا حدٌّ معلنٌ لا مُعالَجٌ.
- الأثرُ الخارجيُّ (1K) خارجُ هذا الوصلِ: عقدٌ يخلطُ الداخليَّ بالخارجيِّ مرفوضٌ أصلًا (`MixedEffectContractError`).
- لا يملكُ الحدُّ بهذا الوصلِ `force` ولا `bypass` ولا معاملَ تجاوزٍ جديدًا (يحرسُه `self_check` و`bypass_parameters_of`).

### 7.6 الفحوصُ والطفراتُ المُلزِمةُ (معيارُ القبولِ (7) في البندِ — مكتوبةٌ قبلَ الشِّفرةِ)
| الفحص | ما يُثبتُه |
|---|---|
| **T6p** · J1 الإنتاجيُّ | نداءُ `issue_ruling` وحدَه مع إسقاطِ `mark_succeeded` ⇒ `CompensationRequired` · `state_is_clean` · صفُّ الحكمِ وإجراءُ RULING غائبانِ · القضيّةُ بحالتِها السابقةِ · الذرّيّةُ `FAILED_RETRYABLE` · والإعادةُ بعدَ رفعِ الإسقاطِ تنجحُ بحكمٍ واحدٍ |
| **T8** · WI-082 الإنتاجيُّ | نداءُ `register_identity` وحدَه مع الإسقاطِ نفسِه ⇒ `CompensationRequired` · `state_is_clean` · صفُّ الهويّةِ غائبٌ · الذرّيّةُ `FAILED_RETRYABLE` |
| **T9** · فشلُ المُعوِّضِ نفسِه | إسقاطُ التثبيتِ **ومُعوِّضٌ يرفعُ** ⇒ `CompensationRequired` · `state_is_clean is False` · `requires_human` · الباقي مُسمًّى · الذرّيّةُ `FAILED_FINAL` · والإعادةُ مرفوضةٌ |
| **T10** · الحلقةُ الثانيةُ | فشلانِ متتاليانِ بعدَ الالتزامِ على العقدِ نفسِه ⇒ كلٌّ منهما يعكسُ صفوفَه فعلًا (لا يُعادُ سجلُّ تعويضٍ مُغلَقٌ) |

| الطفرة | تُسقِطُ |
|---|---|
| **M5** · حذفُ اللفِّ (نداءُ `compensate`) | T6p · T8 · T9 · T10 |
| **M6** · إخفاءُ فشلِ المُعوِّضِ (إرجاعُ الحصيلةِ نظيفةً) | T9 |
| **M7** · نقلُ الذرّيّةِ إلى `FAILED_RETRYABLE` عندَ عدمِ النظافةِ | T9 |
| **M8** · حذفُ مفتاحِ الحلقةِ (المفتاحُ نفسُه) | T10 |

وفحصا T6 (حارسُ 1I اليدويُّ في W-593) وT1–T5 وT7 تبقى · وT6 القديمُ يُكتَبُ إنتاجيًّا (T6p) لأنَّ النداءَ الإنتاجيَّ صارَ يرفعُ `CompensationRequired` لا `RuntimeError` — والتغييرُ تشديدٌ مؤرَّخٌ لا تخفيفٌ.

=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && cat docs/audit/evidence/W-601/test_w601_gap_probe.py docs/audit/evidence/W-601/probe_output_before_fix.txt
EXIT: 0
BYTES: 9437
SHA256: b63492fbe19af1af01998f1a3156128028b315af8cc5344673999fbbe95351a4
NO_EOL: 0
--- OUTPUT ---
"""
الهدف: قياسُ موضعِ فجوةِ التعويضِ (Q-70 · التوجيهُ 18 § 2) على المسارِ الإنتاجيِّ — بلا تغييرٍ في الشِّفرة
النطاق: docs/audit/evidence/W-601 — مسبارٌ يُنسَخُ مؤقّتًا إلى federal/executive/services/tests/ ثمَّ يُحذَف (سابقةُ مسبارِ مقعدِ claude في W-599) ولا يُلتزَمُ هناك
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — قيدُ W-601
تاريخ الإنشاء: 2026-10-22

السيناريو الواحدُ لكلِّ سطحٍ: يُسقَطُ تثبيتُ النجاحِ (`IdempotencyLedger.mark_succeeded`)
بعدَ أن يلتزمَ المُطبِّقُ صفوفَه، ثمَّ يُنادى السطحُ بنداءِ الخدمةِ الإنتاجيِّ وحدَه
(لا تعويضَ يدويًّا). ويُسجَّلُ: الاستثناءُ الناتجُ · حالةُ الصفوفِ · هل شُغِّلَ المُعوِّضُ
· حالةُ سجلِّ الذرّيّةِ · ونتيجةُ إعادةِ المحاولةِ بعدَ رفعِ الإسقاطِ.

التشغيل (من جذرِ المستودع):
  cp docs/audit/evidence/W-601/test_w601_gap_probe.py federal/executive/services/tests/ && \
  .venv/bin/pytest federal/executive/services/tests/test_w601_gap_probe.py -s -q -p no:cacheprovider ; \
  rm federal/executive/services/tests/test_w601_gap_probe.py
"""

from __future__ import annotations

from typing import Any

import pytest

from amos_federation.services.executive_core import agent_identity as agent_identity_module
from amos_federation.services.executive_core.agent_identity import (
    get_identity,
    register_identity,
)
from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer

# مُثبَّتاتُ فحوصِ J1 نفسُها — لا بيئةَ موازية
from tests.test_wi105_issue_ruling_sovereign import (  # noqa: F401 — مُثبَّتاتٌ تُحقَنُ بالاسم
    _fresh_state,
    _prepared_case,
    _session,
    crown,
    judiciary,
    national,
    registry,
    rulings_module,
)
from tests.test_wi105_issue_ruling_sovereign import (  # noqa: E402
    CaseProceedingModel,
    LegalCaseModel,
    RulingModel,
)


def _spy_compensators(monkeypatch: pytest.MonkeyPatch, calls: list[str]) -> None:
    """جاسوسٌ على `Compensator.apply`: هل نادى أيُّ مسارٍ المُعوِّضَ؟ — لا يغيّرُ سلوكَه."""
    from core.sovereignty import compensation as comp

    original_compensate = comp.CompensationGuard.compensate

    def spy_compensate(self: Any, **kwargs: Any) -> Any:
        calls.append("CompensationGuard.compensate")
        return original_compensate(self, **kwargs)

    monkeypatch.setattr(comp.CompensationGuard, "compensate", spy_compensate)


def _drop_settle(monkeypatch: pytest.MonkeyPatch, ledger: Any) -> None:
    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("تثبيتُ النجاحِ مُسقَطٌ — مسبارُ W-601")

    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)


def _status_of(ledger: Any, scope: str, value: str) -> str:
    from core.sovereignty.idempotency import IdempotencyKey

    rec = ledger.get(IdempotencyKey(scope=scope, value=value)) if hasattr(ledger, "get") else None
    return getattr(getattr(rec, "status", None), "value", str(rec))


def test_probe_a_issue_ruling(registry, national, judiciary, crown, monkeypatch) -> None:  # noqa: ANN001, F811 — مُثبَّتاتٌ تُحقَنُ بالاسمِ (W-603)
    print("\n## (أ) issue_ruling — J1 · WI-105")
    _b, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "w601a")
    s = _session()
    try:
        before = s.get(LegalCaseModel, case_id).status
    finally:
        s.close()
    print(f"حالةُ القضيّةِ قبلَ النداء: {before}")

    calls: list[str] = []
    _spy_compensators(monkeypatch, calls)
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
    original = type(ledger).mark_succeeded
    _drop_settle(monkeypatch, ledger)

    exc_repr = "لا استثناء"
    try:
        judiciary.issue_ruling(
            context=judge_ctx, case_id=case_id, stage="FIRST_INSTANCE",
            decision="GRANTED", disposition="مسبارُ W-601",
        )
    except Exception as exc:  # noqa: BLE001 — يُقاسُ لا يُبتلَع
        exc_repr = f"{type(exc).__module__}.{type(exc).__name__}: {exc}"
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    s = _session()
    try:
        rulings = s.query(RulingModel).filter(RulingModel.case_id == case_id).count()
        procs = (
            s.query(CaseProceedingModel)
            .filter(CaseProceedingModel.case_id == case_id,
                    CaseProceedingModel.proceeding_type == "RULING")
            .count()
        )
        after = s.get(LegalCaseModel, case_id).status
    finally:
        s.close()
    print(f"الاستثناءُ الناتج: {exc_repr}")
    print(f"صفوفُ الحكمِ: {rulings} · إجراءاتُ RULING: {procs} · حالةُ القضيّة: {after}")
    print(f"هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: {len(calls)}")
    print(f"سجلُّ الذرّيّة: {_status_of(ledger, 'judiciary.ruling.issue', f'{case_id}:FIRST_INSTANCE:g0')}")

    retry = "لا استثناء"
    try:
        judiciary.issue_ruling(
            context=judge_ctx, case_id=case_id, stage="FIRST_INSTANCE",
            decision="GRANTED", disposition="مسبارُ W-601 — إعادة",
        )
    except Exception as exc:  # noqa: BLE001
        retry = f"{type(exc).__module__}.{type(exc).__name__}"
    print(f"إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: {retry}")


def test_probe_b_register_identity(monkeypatch) -> None:  # noqa: ANN001
    print("\n## (ب) register_identity — WI-082")
    agent_id = "w601-probe-agent"
    agent_identity_module._delete_identity_row(agent_id)
    authorizer = ConstitutionalAuthorizer(actor=agent_identity_module.AGENT_IDENTITY_ACTOR)
    calls: list[str] = []
    _spy_compensators(monkeypatch, calls)
    ledger = authorizer.boundary.idempotency_ledger
    original = type(ledger).mark_succeeded
    _drop_settle(monkeypatch, ledger)

    exc_repr = "لا استثناء"
    try:
        register_identity(agent_id, "مسبار", "probe", authorizer=authorizer)
    except Exception as exc:  # noqa: BLE001
        exc_repr = f"{type(exc).__module__}.{type(exc).__name__}: {exc}"
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    row = get_identity(agent_id)
    print(f"الاستثناءُ الناتج: {exc_repr}")
    print(f"صفُّ الهويّة: {'موجود' if row is not None else 'غائب'}")
    print(f"هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: {len(calls)}")
    print(f"سجلُّ الذرّيّة: {_status_of(ledger, agent_identity_module.IDENTITY_SPAWN_SCOPE, agent_id)}")

    retry = "لا استثناء"
    try:
        register_identity(agent_id, "مسبار", "probe", authorizer=authorizer)
    except Exception as exc:  # noqa: BLE001
        retry = f"{type(exc).__module__}.{type(exc).__name__}"
    print(f"إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: {retry}")
    agent_identity_module._delete_identity_row(agent_id)
$ date -u
Thu Oct 22 04:58:17 UTC 2026
$ git rev-parse HEAD
8c98ca54e5b89758673da0df880343d3f552c43e
$ .venv/bin/pytest federal/executive/services/tests/test_w601_gap_probe.py -s -q -p no:cacheprovider
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/AMOS-Fedration/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 2 items

federal/executive/services/tests/test_w601_gap_probe.py 
## (أ) issue_ruling — J1 · WI-105
حالةُ القضيّةِ قبلَ النداء: assigned
الاستثناءُ الناتج: builtins.RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — مسبارُ W-601
صفوفُ الحكمِ: 1 · إجراءاتُ RULING: 1 · حالةُ القضيّة: decided
هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: 0
سجلُّ الذرّيّة: RUNNING
إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: amos_federation.services.federal_judiciary.rulings.DuplicateRulingError
.
## (ب) register_identity — WI-082
الاستثناءُ الناتج: builtins.RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — مسبارُ W-601
صفُّ الهويّة: موجود
هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: 0
سجلُّ الذرّيّة: RUNNING
إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: amos_federation.services.executive_core.agent_identity.DuplicateAgentIdentityError
.

============================== 2 passed in 0.87s ===============================
EXIT 0
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && cat docs/audit/evidence/W-603/mutations_M5_M8_output.txt docs/audit/evidence/W-603/probe_output_after_fix.txt docs/audit/evidence/W-603/measurements.txt
EXIT: 0
BYTES: 6663
SHA256: 11996c4b0f14b6593e8b1d57d403b4cf7bdda09c6a04f5b012e347a6403b7a73
NO_EOL: 0
--- OUTPUT ---
## M5 · حذفُ اللفِّ (نداءُ compensate) — الاستثناءُ يُرفَعُ كما هو دائمًا
- السطرُ الأصلُ: if plan is None or not applied_internal:
- السطرُ المُطفَّر: if True:
- رمزُ الخروج: 1
```
FAILED tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t6p_boundary_compensates_failed_settle_on_production_path
FAILED tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t8_boundary_compensates_register_identity_on_production_path
FAILED tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t9_failing_compensator_closes_operation_final
FAILED tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t10_second_failed_episode_compensates_again
======================= 4 failed, 6 deselected in 1.41s ========================
```

## M6 · إخفاءُ فشلِ المُعوِّضِ — الحصيلةُ تُعامَلُ نظيفةً
- السطرُ الأصلُ: if outcome.state_is_clean:
- السطرُ المُطفَّر: if True:
- رمزُ الخروج: 1
```
FAILED tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t9_failing_compensator_closes_operation_final
================== 1 failed, 3 passed, 6 deselected in 4.62s ===================
```

## M7 · نقلُ الذرّيّةِ إلى FAILED_RETRYABLE عندَ عدمِ النظافة
- السطرُ الأصلُ: new_status=OperationStatus.FAILED_FINAL,
- السطرُ المُطفَّر: new_status=OperationStatus.FAILED_RETRYABLE,
- رمزُ الخروج: 1
```
FAILED tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t9_failing_compensator_closes_operation_final
================== 1 failed, 3 passed, 6 deselected in 4.44s ===================
```

## M8 · حذفُ مفتاحِ الحلقةِ — المفتاحُ نفسُه يُمرَّرُ إلى compensate
- السطرُ الأصلُ: operation_key=episode_key,
- السطرُ المُطفَّر: operation_key=operation_key,
- رمزُ الخروج: 1
```
FAILED tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t10_second_failed_episode_compensates_again
================== 1 failed, 3 passed, 6 deselected in 4.49s ===================
```

$ date -u
Thu Oct 22 05:12:57 UTC 2026
$ git rev-parse HEAD  (+ شِفرةُ W-603 غيرُ مُلتزَمةٍ بعدُ في الشجرةِ العاملة)
e13fe2fed552273e013732bbb4b6344df07f6d31
$ git diff --stat core/
 core/sovereignty/enforcement_boundary.py | 161 +++++++++++++++++++++++++++----
 1 file changed, 140 insertions(+), 21 deletions(-)
$ .venv/bin/pytest federal/executive/services/tests/test_w601_gap_probe.py -s -q -p no:cacheprovider   (المسبارُ بلا تعديلٍ)
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/AMOS-Fedration/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 2 items

tests/test_w601_gap_probe.py 
## (أ) issue_ruling — J1 · WI-105
حالةُ القضيّةِ قبلَ النداء: assigned
الاستثناءُ الناتج: core.sovereignty.compensation.CompensationRequired: العمليّةُ «judiciary.ruling.issue:lcs-d474ad25-0bcc-4d15-aed2-80c5f4d94822:FIRST_INSTANCE:g0@attempt1» على العقد «EC-cb4e8c2c13213988» فشلت (RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — مسبارُ W-601) وعُوِّضَ أثرُها كاملًا فرجعتِ الحالة. الحالة: COMPENSATED.
صفوفُ الحكمِ: 0 · إجراءاتُ RULING: 0 · حالةُ القضيّة: assigned
هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: 1
سجلُّ الذرّيّة: FAILED_RETRYABLE
إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: core.sovereignty.idempotency.IdempotencyError
.
## (ب) register_identity — WI-082
الاستثناءُ الناتج: core.sovereignty.compensation.CompensationRequired: العمليّةُ «agents.identity.spawn:w601-probe-agent@attempt1» على العقد «EC-430477290d128166» فشلت (RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — مسبارُ W-601) وعُوِّضَ أثرُها كاملًا فرجعتِ الحالة. الحالة: COMPENSATED.
صفُّ الهويّة: غائب
هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: 1
سجلُّ الذرّيّة: FAILED_RETRYABLE
إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: core.sovereignty.idempotency.IdempotencyError
.

============================== 2 passed in 0.98s ===============================
# قياساتُ دفعةِ W-603 (2026-10-22) — كلُّ رقمٍ هنا مقيسٌ بأمرِهِ

== D-4 · الجردُ السياديُّ (.venv/bin/python tools/audit/sovereign_write_inventory.py) ==
قبل (main 8c98ca5 · worktree منفصلٌ):
  مواضعُ كتابةٍ (كلُّها)   : 220
  عمليّاتٌ عامّةٌ مُغيِّرة   : 201
  منها تعبرُ الحدَّ        : 18
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 181
بعد (شجرةُ العملِ بشِفرةِ W-603 قبلَ الالتزامِ):
  مواضعُ كتابةٍ (كلُّها)   : 220
  عمليّاتٌ عامّةٌ مُغيِّرة   : 201
  منها تعبرُ الحدَّ        : 18
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 181
⇒ الدَّينُ 181←181 بلا تغيُّرٍ: الوصلُ داخلَ الحدِّ لا يُضيفُ موضعَ كتابةٍ ولا يُخرِجُ واحدًا (المتوقَّعُ في الملحقِ)

== الحزمُ ==
federal/executive/services (AMOS_DATABASE_URL=sqlite:////tmp/amos_w603.db .venv/bin/pytest federal/executive/services/ -q): 1485 passed, 53 skipped, 0 failed = 1538
  (قبلَ كتابةِ T6p: 1 failed (T6 القديمُ يتوقّعُ RuntimeError) · 1481 passed · 53 skipped — المتوقَّعُ في الملحقِ § 7.6)
tests/sovereignty (.venv/bin/pytest tests/sovereignty -q): 818 passed, 1 skipped
tests/ (.venv/bin/pytest tests/ -q قبلَ الختمِ والتوليد): 2703 passed · 1 skipped · 5 failed — كلُّها حرسُ الهويّةِ/الطزاجةِ/رقمِ الحزمةِ قبلَ إنشاءِ README وختمِه وتوليدِ المصفوفةِ وتصحيحِ رقمِ الحزمة؛ يُعادُ بعدَ الالتزامِ في الحرسِ
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && rg -n "Q-70" docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 0
BYTES: 9469
SHA256: 275d231c858d9132357ad21c56c8e8e1ad7fdffbd3815f3fe25fdd83318df637
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-22 (`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`)))
2289:## Q-70 · تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` الإنتاجيّ: تعويضٌ آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ يُستدعى يدويًّا؟ — DECIDED (2026-10-22 · W-601 · توجيهُ المستشارِ 18 § 1) · وكانَ PENDING_OWNER (2026-10-22 · W-599)
2291:**الحالة: DECIDED — نصُّ المالكِ الحرفيُّ** (توجيهُ المستشارِ 18 § 1 · سلَّمَه المالكُ إلى المنفِّذِ 2026-10-22 · «تسليمُ المالك هذا التوجيه إلى الوكيل هو الذي يُصدره، وبتاريخ تسليمه» · النصُّ الكاملُ في [`evidence/W-601/directive_18_verbatim.md`](evidence/W-601/directive_18_verbatim.md)): «Q-70: خيار (1) مشروطًا. يُوصَل التعويض الآلي بعد قياس موضع الفجوة: إن كانت الفجوة في الحد نفسه (enforcement_boundary.py أو ما يستدعيه) أي أن أي سطح مهجَّر يتصرف هكذا (قِس WI-082 على المسار الإنتاجي نفسه): يُوسَّع نطاق WI-105 بهذا القرار ليشمل ملف الحد، فيُوصَل مرة واحدة لكل الدفعات. إن كانت الفجوة في مسار J1 وحده: أصلحها داخل ملفات J1 الخمسة، ولا حاجة لتوسيع نطاق. في الحالتين: لا خيار (2) (الحالة النصفية لا تُقبل في القضاء).»
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && rg -n "DISC-129" docs/governance/work/DISCOVERIES.md
EXIT: 0
BYTES: 24389
SHA256: da66f95d2c25a0e2fed7d9f356c73f5dce10b3da4bb6063a4683f4ac0a9be42c
NO_EOL: 0
--- OUTPUT ---
7:## تاريخ آخر تعديل: 2026-10-22 (`W-603` — قُيِّدَ **DISC-129** (P3): إعادةُ العقدِ نفسِه في الثانيةِ نفسِها تُرفَضُ بمعرِّفِ الإذنِ المُشتقِّ من الثانيةِ — مقيسٌ بعدَ وصلِ التعويضِ) · ووقبله (`W-601` — حُسِمَت وجهةُ **DISC-128**: Q-70 DECIDED بالخيارِ (1) مشروطًا وقياسُ الموضعِ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **DISC-128** (P1): حاجبُ جولةِ مجلسِ دفعةِ J1 — انقسامُ تأويلِ نصِّ T6/D7-أ المعتمدِ (تعويضٌ آليٌّ أم مُعوِّضٌ مسجَّلٌ) · وجهتُه Q-70 (PENDING_OWNER · D18)) · وكانَ قبلَه: 2026-10-21 (`W-592` — حُسِمَت وجهةُ **DISC-127** (Q-69 DECIDED: اعتمادُ الجولةِ الثانيةِ · لا إعادة · ملاحظةُ إجراءٍ) وصُدِّقَت تجديداتُ DISC-087/088/089 (D17-5)) · وكانَ قبلَه: 2026-10-21 (`W-591` — قُيِّدَ **DISC-127** (P2: انحرافُ اختيارِ مقاعدِ الجولةِ الثانيةِ عندَ الإطلاقِ عن § 1.3/§ 1.5 — المنسِّقُ GLM-5.3 والإحاطاتُ المختومةُ تستبعدُ Claude · وجهتُه Q-69)) · وكانَ قبلَه: 2026-10-21 (`W-587` — قُيِّدَ **DISC-126** (P2: أثرُ الأسطحِ في D4 من تصميمِ J1 «220 ← 219» غلطٌ — المُطبِّقُ المتداخلُ يُحصى فيبقى 220 · وجدَه مقعدُ grok_4_7)) · وكانَ قبلَه: 2026-10-21 (`W-586` — قُيِّدَ **DISC-125** (P3: البوابةُ المحلّيّةُ لا تُشغِّلُ ruff ووظيفةُ Lint في CI تُشغِّلُه)) · وكانَ قبلَه: 2026-10-21 (`W-584` — قُيِّدَ **DISC-124** (P2: «18 نداءً» في تصميمِ J1 والبندِ — المقيسُ 15)) · وكانَ قبلَه: 2026-10-21 (`W-582` — قُيِّدَ **DISC-122** (P2: القسمُ د من مخرجِ W-581 لا يُنتِجُه سكربتُه المُلتزَمُ — أُعيدَ إنتاجُه) و**DISC-123** (P2: D-5 بلا أمرٍ واحدٍ · 5/9/15)) · وكانَ قبلَه: 2026-10-21 (`W-581` — قُيِّدَ **DISC-121** (P1): AGENT/SYSTEM يُمارسانِ أفعالَ الفروعِ الحصريّةَ · 54/54 في المراجعةِ) · وكانَ قبلَه: 2026-10-21 (`W-561` — قُيِّدَ **DISC-119** (P1): حارسُ الأسرارِ E2.2 ينهارُ بانهيارِ فكِّ ترميزٍ أمامَ بايتٍ تالفٍ واحدٍ في التاريخِ المدفوعِ (0xd8 في evidence/W-560) فيُسقِطُ Crown وCross-System من CI ⇒ وُجِّهَ إلى بندِ `WI-103`) · ووقبله ((`W-553` — قُيِّدَ **DISC-118** (P1) بأمرِ المالكِ Q-64: طوابعُ التزامٍ كُتِبَت يدويًّا أحدثَ منَ الساعةِ الفعليةِ بنمطٍ متكرِّرٍ (W-442…W-454 ثمَّ W-547…W-549) وتأخيرٌ لينجحَ حارسُ الرتابةِ (W-550) ⇒ وُجِّهَ إلى بندِ الحارسِ `WI-102`) · ووقبله (`W-551` — عُزَّزَت مرساتُ DISC117 بإعلانِ الحرسِ القائمِ بعدَ حمرةِ `OPEN_RECORD_WITHOUT_ANCHOR` في CI) · ووقبله (`W-550` — قُيِّدَ **DISC-117** (P2): منتزعُ أحكامِ الجولاتِ في فاحصِ W-542 يلتقطُ إحاطةَ جولةٍ كمثالِ صيغةِ حكمٍ ⇒ وُجِّهَ إلى بندِ `WI-101` المُسجَّلِ) · ووقبله (`W-546` — `DISC-116` أُغلِقَ بشرطِهِ المكتوبِ: جولةُ W-545 على `WI-094` اجتازَ كلُّ حكمٍ فيها الفاحصَ (3/3 PASS خامًّا كاملًا · الأحكامُ في evidence/W-545)) · ووقبله (`W-545` — جولةُ إعادةِ `WI-094` انعقدت: 3/3 PASS · الأحكامُ حرفيًّا في evidence/W-545) · ووقبله (`W-540` — وجهةُ DISC-116 حُسِمَت: Q-63 DECIDED (إعادةُ جولةِ WI-094 بخامٍ كاملٍ · منعُ الاقتطاعِ نصًّا وفحصًا)) · ووقبله (`W-538` — `DISC-116` (P2) مفتوحٌ: نصُّ تكليفِ المنسِّقِ رخَّصَ في اقتطاعِ المخرجاتِ الخامِ (انحرافٌ عن § 4.1) في جولةِ WI-094) · ووقبله (`W-529` — وجهةُ DISC-115 حُسِمَت: Q-62 DECIDED (الخيارُ 2 · استعادةُ `1c52572` تحتَ WI-082)) · ووقبله (`W-526` — قُيِّدَ **DISC-115** (P1): ملاحظةٌ حاجبةٌ من مقعدِ Claude في جولةِ المجلسِ على WI-082 — الشِفرةُ عندَ عقدةِ المراجعةِ (`83c31a2` = نسخةُ `wi-082-stage3` البايتية) ليست الشِفرةَ التي يصفُها سجلُّ البندِ وأدلّتُهُ (نسخةُ main المُرتدّة في W-425) — وجهتُهُ `Q-62` · البندُ باقٍ IN_REVIEW) · ووقبله (`W-521` — قُيِّدَ **DISC-112** (P1): ملاحظةٌ حاجبةٌ من مقعدِ Claude في جولةِ المجلسِ على WI-096 — معيارُ «الوثيقةُ قبلَ الشِفرةِ» لا يملكُ دليلًا في التاريخِ (وجهتُهُ `Q-61`) · و**DISC-113** (P3): عتبةُ RATIO المعلنةُ في وثيقةِ التصميمِ § 4 بلا حارس · و**DISC-114** (P3): حاصدُ الطفراتِ يكتبُ فوقَ أدلّةٍ متعقّبةٍ) · ووقبله (`W-516` — تصحيحٌ مؤرَّخٌ: مرساةُ استحقاقٍ لصفِّ DISC-111 أُسقطَتْ بوابةَ الحوكمةِ في جولةِ CI لدفعةِ W-515) · ووقبله `W-515` — `DISC-111`: عناوينُ كتلتَي §3 لـWI-094/WI-095 متأخرةٌ عن حقولِ الحالةِ + صفُّ W-452 لا يذكرُ السلوكَ الأشدّ — ملاحظاتُ مقعدِ Claude غيرُ الحاجبةِ في جولةِ WI-095 · عُولِجَ العنوانانِ في الدفعةِ نفسِها) · ووقبله `W-511` — `DISC-110`: حمرةُ Coverage المتقطّعةُ بـ`UnknownAgentIdentityError` في تجهيزِ `test_treasury` على تغييرٍ وثائقيٍّ محضٍ) · ووقبله 2026-10-18 (`W-417` — تجديدُ استحقاقِ 11 اكتشافًا بندًا بندًا بقرارِ المالكِ `Q-53`، كلٌّ بسببِه) · ووقبله (`W-415` — `DISC-102` جذرُ حمرةِ Coverage مقيسًا · `DISC-103` تصادمُ أرقامِ القيودِ بين مكدَّسَين) · ووقبله (`W-360` — سطرُ المولداتِ حُدِّثَ: 12 مولدًا (انضمَّ `prepush_gate` بوجهِ --merge) · تحتَ دعوى `WI-068` القائمِ) · ووقبله (`W-348` — `DISC-098` قُيِّدَ: عقدتانِ حمراوانِ بلغتا `main` قبلَ خضرةِ CI (70441f8 · 597d8bb) — دفعٌ مباشرٌ وحرسُ ما قبلَ الدفعِ لم يكنْ مبنيًّا (تكرارُ جنسِ `DISC-096` مرتينِ) · الحرسُ نُزِلَ في `WI-077` (W-348) · ومسلكُ الدمجِ بيدِ المالكِ (`Q-F`)) · وقبله 2026-10-14 (`W-320` — `DISC-097`: خطأُ المنفِّذِ (صفّا `WI-054`/`WI-061` قُلِبا عرضًا) شُخِّصَ خطأً كتعارضٍ تاريخيٍّ ثم صُحِّحَ وسُحِبَ التشخيصُ بوصفِهِ) · وقبله (`W-316` — `DISC-096`: فُتِحَ `WI-073` وصُحِّحَت فرضيّةُ الخيار) · وقبله 2026-10-13 (`W-315` — `DISC-096` قُيِّدَ: تقديمُ `main` قبلَ قراءةِ حكمِ المقروئيّة) · وقبله 2026-10-13 (`W-312` — `DISC-093` أُصلِحَ بـ`WI-072` بانتظارِ المراجعة) · وقبله 2026-10-13 (`W-308` — `DISC-093` شُخِّصَ بقياسٍ (سجلُّ ذرّيّةِ الاختباراتِ المشترك · الإصلاحُ `WI-072`) · `DISC-095` قُيِّدَ (سجلُّ الذرّيّةِ الإنتاجيُّ بلا قفلِ عمليّة · كامنٌ · `RK-023`)) · وقبله 2026-10-13 (`W-302` — `DISC-094` قُيِّدَ: عملٌ نُفِّذَ على بندٍ `PROPOSED` وعلى مسارٍ غير محجوزٍ (`PHASE_E_ROADMAP.md`) — قيدُ `W-301` · توجيهُ المستشارِ 1 · D1) · وقبله `W-299`/`W-295` (2026-10-12) — `DISC-093` قُيِّدَ قُيِّدَ: إخفاقٌ متقطعٌ غيرُ محسومٍ في حزمةِ الخدماتِ الكاملةِ (W-295 · M1) · ولا شِفرةَ ولا حلٌّ في M1 · مفتوحٌ لوجهةٍ) · وقبله `W-294` (2026-10-12) — `DISC-090`/`DISC-091`/`DISC-092` قُيِّدَت · وقبله `W-252` (2026-10-09) — `DISC-085` وُجِّهَ إلى `WI-060` (`PROPOSED`) بإذنِ المالك · باقٍ مفتوحًا حتى إغلاقِه) · وقبلَه (`W-251` — `DISC-082` (أ)–(ج) أُغلِقَت بإغلاقِ `WI-059` · (د) باقٍ فالاكتشافُ مفتوح) · وقبلَه (`W-250` — `DISC-086` قُيِّدَ: عيبُ `P2` للمراجعِ ب في الجولةِ الأولى على `WI-059` · `DISC-082` باقٍ مفتوحًا حتى إغلاقِ `WI-059`) · وقبلَه 2026-10-08 (`W-248` — `DISC-082` (أ)–(ج) نُفِّذَت في `WI-059` · باقٍ مفتوحًا حتى إغلاقِه) · وقبلَه (`W-247` — `DISC-083` مُغلَقٌ بحجزِ `WI-059`) · وقبلَه (`W-246` — `DISC-083`: `WI-052` أُغلِقَ فارتفعَ سببُ التقاطعِ المقيسُ · باقٍ مفتوحًا حتى حجزِ `WI-059` · `DISC-085` قُيِّدَ) · وقبلَه (`W-243` — `DISC-083`: قرارُ المالكِ الانتظار · الشرطُ غيرُ متحقّق) · وقبلَه 2026-10-07 (`W-242` — `DISC-083` قُيِّدَ: حجزُ `WI-059` يُسقِطُه `CLAIM_CONFLICT` مع `WI-052` · قرارُ مالك) · وقبلَه (`W-240` — `DISC-082` (أ)–(ج) وُجِّهَ إلى `WI-059` بإذنِ المالك · (د)–(و) باقيةٌ) · وقبلَه (`W-239` — `WI-023`/`WI-024` أُغلِقا بإذنِ المالك · `DISC-082` باقٍ مفتوحًا قرارَ مالك) · وقبلَه (`W-237` — الجولةُ التاسعةُ من مجلسِ المراجعةِ (`Q-43`) على `25f7833` بإجماعٍ: `WI-023` و`WI-024` `IN_REVIEW → VERIFIED` · `DISC-081` أُغلِقَ بشرطِه المكتوبِ (‏حكمُ الجولةِ التاسعة) · `DISC-082` قُيِّدَ) · وقبلَه (`W-232` — `DISC-080` (ب)–(هـ) عُولِجَ و`DISC-079` عُولِجَ · و(أ) قبلَ الجولةِ التاسعةِ · `DISC-078` باقٍ مفتوحًا بقرارِ المالك) · وقبلَه (`W-231` — `DISC-080` قُيِّدَ: حكمُ الجولةِ الثامنةِ انقسامٌ على `WI-038`/`WI-041` · وبيئةُ الجولةِ تُعيدُ `DISC-064`) · وقبلَه (`W-229` — `DISC-071` (ج) عُولِجَ في `WI-038` · و(هـ) باقٍ في `WI-040`) · وقبلَه (`W-227` — `DISC-071` (د) عُولِجَ شِقُّه القابلُ للعلاجِ في `WI-041` · `DISC-079` قُيِّدَ: ترويسةُ `test_w041_pushed_head_stamp.py` مُشوَّهةٌ · `DISC-078` مفتوحٌ بيدِ المالك) · وقبلَه (`W-226` — إذنُ المالكِ الصريحُ: `WI-058` `VERIFIED → CLOSED` · و`DISC-077` يُغلَقُ بإغلاقِه · § 7/6 على `W-225` أخضرُ 14/14 · `DISC-078` مفتوحٌ بيدِ المالك) · وقبلَه (`W-225` — الجولةُ الحاديةَ عشرةَ من مجلسِ المراجعةِ (`Q-43`) على `746d9e7` بإجماعِ GPT 5.6 Terra وGrok 4.7: `WI-058` `IN_REVIEW → VERIFIED` · لا `CLOSED` · `DISC-078` قُيِّدَ · `DISC-077` مفتوحٌ حتى الإغلاق) · وقبلَه (`W-224` — `WI-058` `IN_PROGRESS → IN_REVIEW` بقرارِ مجلسِ المراجعةِ · تنفيذُ إصلاحاتِ `P3` · الخطوةُ التاليةُ: قراءةُ حكمِ CI § 7/6 · `DISC-077` مفتوحٌ) · وقبلَه (`W-223` — § 7/6 على W-222 أخضرُ) · وقبلَه (`W-219` — `WI-058` `PROPOSED → READY`) · وقبلَه (`W-212` — `DISC-077` قُيِّدَ: ملاحظاتُ `P3` من المراجعِ ب في الجولةِ العاشرةِ على `WI-057`) · وقبلَه (`W-209` — `DISC-076` قُيِّدَ) · وقبلَه (`W-196` — `DISC-075` قُيِّدَ: ملاحظتا `P3` من المراجعِ ب في الجولةِ التاسعةِ على `WI-025` · و`DISC-074` (د) أُعيدَ قياسُه قائمًا) · وقبلَه (`W-193` — علاجُ `DISC-073` نُفِّذَ في `WI-056`) · وقبلَه (`W-192` — `DISC-074` (ب) عُولِج · و`DISC-073` وُجِّهَ إلى `WI-056`) · وقبلَه 2026-10-03 (`W-191` — `DISC-074` قُيِّدَ: الجولةُ الثامنةُ من المجلسِ على `WI-025` انقسمَت) · وقبلَه 2026-10-03 (`W-190` — `DISC-072` و`DISC-073` قُيِّدا: إدامةُ E4 مُسلسَلةٌ خلفَ حجزِ `WI-025` على قياسِ مواضعِ الكتابة · وruff المحلّيُّ غيرُ المُثبَّتِ يُخالِفُ CI) · وقبلَه 2026-10-03 (`W-181` — `DISC-070` قُيِّدَ: صفُّ قيدٍ خارجَ § 8 بخلايا ناقصةٍ يُقرأُ سليمًا، وصُحِّحَ أثرُه بنقلٍ حرفيٍّ) · وقبلَه 2026-10-02 (`W-176` — `DISC-069` و`DISC-052` عُولِجا في بنودِهما بانتظارِ الجولةِ السابعةِ · وقبلَه `W-175` — `DISC-069` حكمُ الجولةِ السادسةِ مُقيَّدٌ: ثلاثةٌ `VERIFIED` وثلاثةٌ مردودةٌ · وقبلَه `W-166` — `DISC-067` مُعالَجٌ في مصدرِه و`DISC-068` بقاياه مُقيَّدةٌ باستحقاق · وقبلَه `W-165` — الاستحقاقاتُ الفائتةُ الثلاثَ عشرةَ جُدِّدَت وقنبلةُ زمنِ حرسِ WI-029 (`DISC-066`) عولِجَت من مصدرِها إلى 2026-10-17 بسببٍ مكتوبٍ في صفِّ كلٍّ منها بلا محوِ الأوّلِ: الأفقُ السابقُ مضى بلا جولةِ مراجعةٍ تاليةٍ — المراجعةُ فعلُ المجلسِ (`Q-43`) — فالتجديدُ رفعُ حاجزٍ زمنيٍّ لا إنجازٌ، ولا بوّابةَ خُفِّفَت ولا فحصَ أُسكِتَ · حارسُ القاعدةِ `open_record_accountability.py` صادقٌ في حمرتِه) · وقبلَه 2026-09-14 (`W-162` — استحقاقا `DISC-055` و`DISC-056` مضَيا بمُضِيِّ اليومِ فأسقطا بوّابةَ «Work Governance» على عقدةِ `main` نفسِها بعدَ خُضرتِها قبلَ منتصفِ الليلِ — دليلٌ حيٌّ آخرُ على `DISC-062`: الحكمُ دالّةٌ في الزمنِ. فجُدِّدا إلى 2026-09-30 بسببٍ مكتوبٍ بلا محوِ الأوّلِ) · وقبلَه 2026-09-13 (‏`W-161` — **الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ ردَّت البنودَ الستَّةَ كلَّها**: أربعةٌ بإجماعٍ (`WI-023` · `WI-024` · `WI-032` · `WI-038`) واثنانِ بانقسامٍ (`WI-035` · `WI-037` — المراجعُ أ `VERIFIED` والمراجعُ ب `REJECTED`)، فلا `VERIFIED` لبندٍ واحدٍ والإجماعُ شرطُ `Q-43`؛ فقُيِّدَ `DISC-063` باتّحادِ العيوبِ، و`DISC-064` بهُويّةِ الأثرِ المولَّدِ المقروءةِ من `origin` — وبنودُ `READY` الخمسةُ تبقى محجوبةً) · وقبلَه 2026-09-13 (‏`W-160` — **حكمُ CI قِيسَ دالّةً في الزمنِ لا في الشجرةِ وحدَها**: عقدةُ `97e9acd` قُرِئَت خضراءَ 14/14 يومَ 2026-09-11 وصارَت حمراءَ بستِّ مخالفاتِ `DUE_DATE_PASSED` يومَ 2026-09-13 بلا تغييرِ حرفٍ فيها، فقُيِّدَ `DISC-062` ووُجِّهَ إلى حرسٍ يقيسُ عددَ التجديداتِ · **وستُّ استحقاقاتٍ مضَت جُدِّدَت إلى 2026-09-30 بسببٍ مكتوبٍ في صفِّ كلٍّ منها ولم يُمحَ استحقاقُها الأوّلُ** — والتجديدُ رفعُ حاجزٍ زمنيٍّ لا إنجازٌ) · وقبلَه 2026-09-06 (‏`W-138` — السببُ الجذريُّ لعودةِ `DISC-006` صارَ مقيسًا من سجلِّ استهلاكِ الحسابِ ‏2674 دقيقةً مقابلَ مُعلَنٍ منشورٍ 2000، وعبورُ الحدِّ خلالَ 2026-09-03 وهو عينُ حدِّ العَطبِ الزمنيِّ — فرُفِعَ حدُّ القياسِ المُعلَنُ في `W-137` بلا محوِ نصِّه، وقُيِّدَ `DISC-057`، وصارت إشارةُ `RK-011` المبكِّرةُ رقمًا يُقاسُ قبلَ سقوطِ وظيفةٍ. **والحاجزُ باقٍ بيدِ المالكِ ولم تُرقَّ حالةٌ**) · وقبلَه 2026-09-05 (`DISC-006` — **عادَ مقيسًا** بـ`W-137`: صفرُ عاملٍ وصفرُ خطوةٍ في وِردَي عقدةِ `febb558` (‏تشغيلا **95** و**96**)، فحالتُه `مفتوحٌ` لا `مُعالَجٌ` و`RK-011` `مرتفعٌ` — والوجهةُ بيدِ المالكِ) · وقبلَه 2026-09-05 (`DISC-056` — قُيِّدَ بـ`W-136`: قارئُ حكمِ CI يستدعي `/runs/{id}/jobs` بلا تثبيتِ محاولةٍ والواجهةُ تُرجِعُ آخرَها وحدَها، فحكمُ التشغيلِ **94** انقلبَ من `READABLE · 13/13` إلى `UNREADABLE · 0/10` بإعادةِ تشغيلٍ بنيويّةٍ **بلا تغييرِ حرفٍ في الشجرةِ ولا في الرقمِ المُحالِ إليه** · وحرسُه في `WI-048` · والخطرُ `RK-022`) · وقبلَه 2026-09-03 (`DISC-052` — قُيِّدَ بـ`W-129`: بوّابةُ أحجامِ الحزمِ تُعلِنُ حكمًا أوسعَ مِمّا قاسَت — رقمُ حزمةِ الجذرِ مكتوبٌ بصيغةٍ لا يقرؤها قارئُها فتقادَمَ **2398 مقابلَ 2421** بلا حمرةٍ، فصُحِّحَ الرقمُ ووُجِّهَ الحدُّ إلى `WI-044`) · وقبلَه 2026-09-03 (`DISC-051` — قُيِّدَ بـ`W-129`: رباطُ وجهِ `--check` بالمستودعِ الحقيقيِّ قائمةٌ بخطِّ اليدِ، فسبعةُ مُولِّداتٍ من إحدى عشرةَ بلا رباطٍ مقيسٍ · وحرسُه في `WI-043`) · وقبلَه 2026-09-03 (`DISC-050` — قُيِّدَ بـ`W-128`: بوّابةُ سرِّ الملكِ في CI غيَّرَت حكمَها على العقدةِ نفسِها بلا تغييرِ حرفٍ، وسببُها لم يُقرَأْ لأنَّ سجلَّ الوظيفةِ يُحوَّلُ إلى مُضيفٍ محجوبٍ · وحرسُه في `WI-042`) · وقبلَه 2026-09-03 (`DISC-049` — قُيِّدَ بـ`W-127`: طابعُ الالتزامِ المُنشَأِ بواجهةِ Git Data يرثُ إزاحةَ الدافعِ المحلّيّةَ ووجهُ القراءةِ يعرضُها `Z`، فسقطَ فحصانِ في تشغيلِ CI **84** وصُحِّحَ الأثرُ بإعادةِ إنشاءِ الالتزامِ · وحرسُه في `WI-041`) · وقبلَه 2026-09-03 (`DISC-048` — قُيِّدَ وأُصلِحَ موضعُه بـ`W-126`: قاسمُ الخلايا كانَ يرفضُ النقصَ ويُمَرِّرُ الزيادةَ، فصفّانِ بتسعِ خلايا يُحكَمُ عليهما بعمودٍ مُزاحٍ بلا مخالفةٍ — فصارَ العددُ مُلزَمًا في الجهتَينِ و`\|` محتوًى لا حدًّا) · وقبلَه 2026-09-03 (`DISC-047` — قُيِّدَ وأُغلِقَ بـ`W-122`: الإعفاءُ البيئيُّ كانَ يُقاسُ باستيرادِ حزمةِ المستودعِ و`conftest.py` يُضيفُ مسارَ مصدرِها، فسقطَ CI 79 بنقصِ تبعيّاتٍ لا برقمٍ ميّتٍ — فصارَ السببُ يُقرأُ من خرجِ الجمعِ بأسمائِه) · وقبلَه 2026-09-03 (`DISC-046` — نزلَ حرسُه بـ`W-121`: عددُ الجمعِ صارَ مقيسًا حيًّا يُقارَنُ بكلِّ رقمٍ مكتوبٍ، والتاريخيُّ يُعفى بإعلانٍ منسوبٍ إلى قيدٍ لا بصمتٍ) · وقبلَه 2026-09-03 (`DISC-046` — أرقامُ حجمِ الحزمِ في «الحالةُ المقيسةُ الآن» مقيسةٌ متقادمةٌ بلا حرسٍ: المكتوبُ 1748 والمقيسُ 2351) · وقبلَه 2026-09-03 (`DISC-042` — نزلَ حرسُه بـ`W-118`: نثرٌ في خليّةِ المساراتِ يُرفَضُ صراحةً ولا يُقرأُ دعوى · 8 ← 0 والتغطيةُ لم تتبدَّلْ) · وقبلَه 2026-09-03 (`WI-036` — نزلَ حرسُ `W-115` فصارَ التباسُ ترقيمِ § 10 **رقمًا يُقاسُ لا يعلو**، ومِرساةُ `DISC-045` مسارَ حرسٍ قائمًا لا وعدًا) · وقبلَه 2026-09-03 (`WI-036` — `DISC-045`: الرقمُ 9 في § 10 من سجلِّ الإكمالِ مكتوبٌ **مرّتَينِ** لحدَّينِ مختلفَينِ فصارَت **7 إحالاتٍ** إلى «الحدِّ 9» لا تُحَلُّ إلى حدٍّ واحدٍ — مقيسٌ ووُجِّهَ إلى حرسٍ يمنعُ نموَّه، ولا يُعادُ الترقيمُ لأنَّه يكسِرُ إحالاتٍ في قيودٍ مدفوعةٍ) · وقبلَه 2026-08-31 (`WI-023` — دعوى «يُشغَّلُ في كلِّ دفعةٍ» صارت مقيسةً في بوّابةٍ فقُيِّدَ `DISC-037` وأُقِرَّ حدُّ `DISC-032`؛ وقبلَه `WI-022` — القياسُ الأوّلُ للفرعِ كانَ أضيقَ من الواقعِ فصُحِّحَ في `DISC-034`، وتصادمُ معرِّفاتِ السجلِّ بينَ الفرعَينِ قُيِّدَ `DISC-036`) · وقبلَه 2026-08-30 (`WI-021` — فرعٌ لم يُدمَجْ حملَ إصلاحًا لم يبلُغِ الفرعَ الحاكمَ `DISC-034`، وحالةُ بندٍ مكتوبةٌ مرّتَينِ متناقضتَينِ `DISC-035`) · وقبلَه 2026-08-29 (`WI-019` — قراءةُ الحكمِ كشفَت ثلاثةَ عُيوبٍ كانت مستورةً: سطرُ اختبارٍ `DISC-024`، وحرسٌ لا يُقاسُ على طلبِ دمجٍ `DISC-025`، وثلاثةُ فحوصٍ لم تُنفَّذْ `DISC-026`)))
141:| DISC-129 | P3 | `core/sovereignty/enforcement.py:256` (معرِّفُ الإذنِ) — مقيسٌ في `W-603` (2026-10-22) بعدَ وصلِ التعويضِ في الحدِّ | **إعادةُ العقدِ نفسِه في الثانيةِ نفسِها تُرفَضُ:** معرِّفُ الإذنِ `EP-<العقد>-<int(الثانية)>` فبعدَ حلقةٍ عُوِّضَت آليًّا (الذرّيّةُ `FAILED_RETRYABLE` والحالةُ نظيفةٌ) تُرفَضُ الإعادةُ الفوريّةُ `PermitReplayError` (يُرفَعُ `IdempotencyError` بلا أثرٍ مطبَّقٍ) وتنجحُ في الثانيةِ التاليةِ — إغلاقٌ لا فتحٌ | `evidence/W-603/probe_output_after_fix.txt` (مسبارُ W-601 بلا تعديلٍ: «إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: IdempotencyError» · والسببُ المقيسُ `PermitReplayError('الإذنُ «EP-430477290d128166-…» استُهلِك من قبل.')`) · وT6p/T8/T10 تعبرُ إلى الثانيةِ التاليةِ فتنجحُ الإعادةُ | إعادةٌ فوريّةٌ آليّةٌ بعدَ تعويضٍ تفشلُ مرّةً بلا ضررٍ في الحالةِ (لا صفَّ ولا أثرَ) | الملفُّ خارجَ نطاقِ `WI-105` (التوسيعُ بقرارِ Q-70 لملفِّ الحدِّ وحدَه) فلا يُعدَّلُ هنا · يُعرَضُ على المالكِ إن شاءَ بندًا مستقلًّا · استحقاق: 2026-11-20 (أفقُ حجزِ `WI-105`) | مفتوحٌ (مُسجَّلٌ في `W-603`) |
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && .venv/bin/python -m pytest tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q
EXIT: 0
BYTES: 100
SHA256: 53aaf3b4ad93df8bb5726fc36258a103ae31f788f28e64f25992d6cc0f32bde3
NO_EOL: 0
--- OUTPUT ---
....................................................                     [100%]
52 passed in 29.26s
=== RAW [19] END ===
=== RAW [20] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
EXIT: 0
BYTES: 319
SHA256: e237b66d4e4686ec1d76c273157268e76598e93fa5418cfa9090f52a8c38efd9
NO_EOL: 0
--- OUTPUT ---
عقدُ نَسَبِ القياساتِ مستقيمٌ: 11 قياسًا مقيَّدًا · 8 محروسًا (‏منها 1 برباطٍ مقيسٍ نصًّا) · 3 مُعلَنًا بسببٍ مكتوبٍ. ومُؤَجَّلٌ إلى الشطرِ الآخرِ: 2 (‏من 2 يحتاجُ حزمًا خارجيّةً).
=== RAW [20] END ===
=== RAW [21] BEGIN ===
CMD: find /home/user/workspace/council_w605/grok_4_7 -maxdepth 1
EXIT: 0
BYTES: 351
SHA256: f237915f080441e9030b92231cac5fa85a8395ba3ddca7931ef0c5e1c1422229
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w605/grok_4_7
/home/user/workspace/council_w605/grok_4_7/repo
/home/user/workspace/council_w605/grok_4_7/tmp
/home/user/workspace/council_w605/grok_4_7/briefing.md
/home/user/workspace/council_w605/grok_4_7/launch_message.txt
/home/user/workspace/council_w605/grok_4_7/probe
/home/user/workspace/council_w605/grok_4_7/raw
=== RAW [21] END ===
=== RAW [22] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w605/grok_4_7/probe/probe_partial_restore_after_inner_failure.py
EXIT: 0
BYTES: 11863
SHA256: eeb418dc6f8999d9b8003b48bd5f4e1d3fafe8de67f7a5cb0b080d9761f09929
NO_EOL: 0
--- OUTPUT ---
     1	"""مسبارُ مقعدِ grok_4_7 — ليس أمرًا من القسمِ ج ولا نسخةً من T6p/T8/T9/T10.
     2	
     3	يحاولُ كسرَ خاصيّةِ المعيارِ (7) / الملحقِ § 7.4 على المسارِ الإنتاجيِّ
     4	``FederalJudiciary.issue_ruling`` بسيناريو لا يغطّيه الفحصُ القائمُ:
     5	
     6	1. الفشلُ بعدَ التزامِ المُطبِّقِ وعودتِه، لكن داخلَ ``execute()``: لفُّ
     7	   ``PolicyEnforcementPoint.enforce`` يرفعُ بعدَ الأصلِ. فلا يُسقَطُ
     8	   ``mark_succeeded``. فيُنادى ``IdempotencyGuard`` ``mark_failed``
     9	   (FAILED_RETRYABLE) قبلَ أن يرى الحدُّ الاستثناءَ.
    10	2. المُعوِّضُ الإنتاجيُّ ``_restore`` يُلتزَمُ حذفُ صفِّ الحكمِ ثمَّ يرفعُ
    11	   قبلَ حذفِ إجراءِ RULING وإرجاعِ حالةِ القضيّةِ — فشلٌ جزئيٌّ مُلتزَمٌ
    12	   لا استبدالُ المُعوِّضِ برافعٍ كما في T9.
    13	
    14	الخاصيّةُ المُدَّعاةُ التي يُحاوَلُ كسرُها: بعدَ هذا الفشلِ يبقى
    15	``CompensationRequired`` مرفوعًا · ``state_is_clean`` كاذبة ·
    16	``requires_human`` · الباقي مُسمًّى · سجلُّ الذرّيّةِ ``FAILED_FINAL``
    17	(إغلاقٌ لا إعادةٌ فوقَ أثرٍ باقٍ) رغمَ ``mark_failed`` السابق · والإعادةُ
    18	مرفوضةٌ ولا يُكتَبُ حكمٌ ثانٍ.
    19	"""
    20	
    21	from __future__ import annotations
    22	
    23	import math
    24	import time
    25	from typing import Any
    26	
    27	import pytest
    28	from sqlalchemy.orm import Session
    29	
    30	from amos_federation.services.federal_judiciary.models import (
    31	    CaseProceedingModel,
    32	    RulingModel,
    33	)
    34	from core.sovereignty.enforcement import PolicyEnforcementPoint
    35	from tests.test_wi105_issue_ruling_sovereign import (
    36	    _fresh_state,
    37	    _prepared_case,
    38	    _ruling_key,
    39	    _ruling_rows,
    40	    crown,
    41	    judiciary,
    42	    national,
    43	    registry,
    44	)
    45	
    46	
    47	def _next_second() -> None:
    48	    now = time.time()
    49	    time.sleep(math.ceil(now) - now + 0.05)
    50	
    51	
    52	def test_grok_4_7_partial_restore_after_inner_execute_failure() -> None:
    53	    from core.sovereignty.compensation import CompensationRequired
    54	    from core.sovereignty.idempotency import IdempotencyError, OperationStatus
    55	
    56	    # الدوالُّ مثبّتاتُ pytest — تُستدعى النسخةُ الأصليّةُ لا الغلافُ الذي يرفضُ النداءَ.
    57	    _fresh_state.__wrapped__()
    58	    reg = registry.__wrapped__()
    59	    nat = national.__wrapped__()
    60	    jud = judiciary.__wrapped__()
    61	    cr = crown.__wrapped__(nat)
    62	    _bench_unused, case_id, judge_ctx = _prepared_case(reg, nat, jud, cr, "grok47-probe")
    63	    del _bench_unused
    64	    status_before = _ruling_rows(case_id)[2]
    65	    rulings_before, procs_before, _status = _ruling_rows(case_id)
    66	    print(
    67	        f"PROBE_BEFORE rulings={rulings_before} ruling_procs={procs_before} "
    68	        f"case_status={status_before}"
    69	    )
    70	
    71	    original_enforce = PolicyEnforcementPoint.enforce
    72	    original_get = Session.get
    73	    state: dict[str, Any] = {"seen_ruling": False, "partial_committed": False}
    74	
    75	    def exploding_enforce(
    76	        self: PolicyEnforcementPoint,
    77	        permit: Any,
    78	        *,
    79	        planner: Any,
    80	        applier: Any,
    81	        now: Any = None,
    82	    ) -> Any:
    83	        produced = original_enforce(self, permit, planner=planner, applier=applier, now=now)
    84	        raise RuntimeError(
    85	            "فشلٌ بعدَ عودةِ المُطبِّقِ داخلَ execute — لا إسقاطَ mark_succeeded — مسبارُ grok_4_7"
    86	        )
    87	
    88	    def probing_get(self: Session, entity: Any, ident: Any, **kwargs: Any) -> Any:
    89	        obj = original_get(self, entity, ident, **kwargs)
    90	        if entity is RulingModel and obj is not None:
    91	            state["seen_ruling"] = True
    92	        if (
    93	            entity is CaseProceedingModel
    94	            and state["seen_ruling"]
    95	            and not state["partial_committed"]
    96	        ):
    97	            # حذفُ الحكمِ معلَّقٌ في الجلسةِ: التزمْه ثمَّ ارفعْ قبلَ بقيةِ العكس.
    98	            self.commit()
    99	            state["partial_committed"] = True
   100	            raise RuntimeError(
   101	                "المُعوِّضُ الإنتاجيُّ التزمَ حذفَ الحكمِ ثمَّ رفعَ قبلَ حذفِ الإجراءِ "
   102	                "وإرجاعِ الحالة — مسبارُ grok_4_7"
   103	            )
   104	        return obj
   105	
   106	    PolicyEnforcementPoint.enforce = exploding_enforce  # type: ignore[method-assign]
   107	    Session.get = probing_get  # type: ignore[method-assign]
   108	    caught: pytest.ExceptionInfo[Any] | None = None
   109	    try:
   110	        with pytest.raises(Exception) as caught:
   111	            jud.issue_ruling(
   112	                context=judge_ctx,
   113	                case_id=case_id,
   114	                stage="FIRST_INSTANCE",
   115	                decision="GRANTED",
   116	                disposition="مسبارُ grok_4_7 — كسرُ التعويضِ الجزئيِّ",
   117	            )
   118	    finally:
   119	        PolicyEnforcementPoint.enforce = original_enforce  # type: ignore[method-assign]
   120	        Session.get = original_get  # type: ignore[method-assign]
   121	
   122	    assert caught is not None
   123	    exc = caught.value
   124	    print(f"PROBE_EXC type={type(exc).__module__}.{type(exc).__name__}")
   125	    print(f"PROBE_EXC text={exc}")
   126	    print(f"PROBE_PARTIAL_COMMITTED={state['partial_committed']}")
   127	    cause = exc.__cause__
   128	    print(
   129	        "PROBE_CAUSE "
   130	        + (
   131	            f"type={type(cause).__module__}.{type(cause).__name__} text={cause}"
   132	            if cause is not None
   133	            else "none"
   134	        )
   135	    )
   136	
   137	    rulings_after, procs_after, status_after = _ruling_rows(case_id)
   138	    print(
   139	        f"PROBE_AFTER rulings={rulings_after} ruling_procs={procs_after} "
   140	        f"case_status={status_after} status_before={status_before}"
   141	    )
   142	
   143	    from amos_federation.services.federal_judiciary import rulings as rulings_module
   144	
   145	    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
   146	    record = ledger.get(_ruling_key(case_id))
   147	    print(
   148	        "PROBE_LEDGER "
   149	        + (
   150	            f"status={record.status.value} applied={tuple(record.applied_effect_signatures)} "
   151	            f"reason={record.failure_reason}"
   152	            if record is not None
   153	            else "missing"
   154	        )
   155	    )
   156	
   157	    broken: list[str] = []
   158	    if not isinstance(exc, CompensationRequired):
   159	        broken.append(f"الاستثناءُ ليس CompensationRequired بل {type(exc).__name__}")
   160	    outcome = exc.outcome if isinstance(exc, CompensationRequired) else None
   161	    if outcome is None:
   162	        broken.append("لا حصيلةَ تعويضٍ")
   163	    else:
   164	        print(
   165	            f"PROBE_OUTCOME status={outcome.record.status.value} "
   166	            f"state_is_clean={outcome.state_is_clean} requires_human={outcome.requires_human} "
   167	            f"residual={tuple(outcome.residual_signatures)}"
   168	        )
   169	        if outcome.state_is_clean is not False:
   170	            broken.append("state_is_clean ليست False والباقي الجزئيُّ قائمٌ")
   171	        if outcome.requires_human is not True:
   172	            broken.append("requires_human ليست True")
   173	        if not outcome.residual_signatures:
   174	            broken.append("الباقي غيرُ مُسمًّى")
   175	        if "يلزمُ قرارٌ بشريّ" not in str(exc):
   176	            broken.append("النصُّ لا يسمّي لزومَ القرارِ البشريِّ")
   177	    if not state["partial_committed"]:
   178	        broken.append("لم يُلتزَم الحذفُ الجزئيُّ — المسبارُ لم يصبِ المُعوِّضَ الإنتاجيَّ")
   179	    if rulings_after != 0:
   180	        broken.append(f"صفُّ الحكمِ لم يُحذَف بعدَ الالتزامِ الجزئيِّ ({rulings_after})")
   181	    if procs_after != 1:
   182	        broken.append(f"إجراءُ RULING لم يبقَ كما يُتوقَّعُ من الفشلِ الجزئيِّ ({procs_after})")
   183	    if status_after == status_before:
   184	        broken.append("حالةُ القضيّةِ رُدَّت رغمَ فشلِ المُعوِّضِ قبلَ الإرجاعِ — ادّعاءُ نظافةٍ")
   185	    if record is None:
   186	        broken.append("سجلُّ الذرّيّةِ غائبٌ")
   187	    elif record.status is not OperationStatus.FAILED_FINAL:
   188	        broken.append(
   189	            f"الذرّيّةُ {record.status.value} لا FAILED_FINAL — الإغلاقُ عندَ الفشلِ انكسرَ "
   190	            "(mark_failed السابقُ قد يُبقي الإعادةَ مفتوحةً فوقَ أثرٍ باقٍ)"
   191	        )
   192	
   193	    _next_second()
   194	    retry_exc: BaseException | None = None
   195	    try:
   196	        jud.issue_ruling(
   197	            context=judge_ctx,
   198	            case_id=case_id,
   199	            stage="FIRST_INSTANCE",
   200	            decision="GRANTED",
   201	            disposition="مسبارُ grok_4_7 — الإعادةُ بعدَ التعويضِ الجزئيِّ",
   202	        )
   203	    except Exception as retry_error:  # noqa: BLE001 — القياسُ على نوعِ الرفضِ
   204	        retry_exc = retry_error
   205	    rulings_retry, procs_retry, status_retry = _ruling_rows(case_id)
   206	    print(
   207	        "PROBE_RETRY "
   208	        + (
   209	            f"type={type(retry_exc).__module__}.{type(retry_exc).__name__} text={retry_exc}"
   210	            if retry_exc is not None
   211	            else "SUCCEEDED"
   212	        )
   213	    )
   214	    print(
   215	        f"PROBE_RETRY_ROWS rulings={rulings_retry} ruling_procs={procs_retry} "
   216	        f"case_status={status_retry}"
   217	    )
   218	    if retry_exc is None:
   219	        broken.append("الإعادةُ نَجحتْ فوقَ أثرٍ باقٍ")
   220	    elif not isinstance(retry_exc, (IdempotencyError, Exception)):
   221	        broken.append(f"الإعادةُ رُفضت بنوعٍ غيرِ متوقَّعٍ {type(retry_exc).__name__}")
   222	    if rulings_retry != rulings_after:
   223	        broken.append(
   224	            f"الإعادةُ غيّرت صفوفَ الحكمِ {rulings_after} → {rulings_retry} فوقَ أثرٍ باقٍ"
   225	        )
   226	
   227	    if broken:
   228	        print("PROBE_BROKEN " + " | ".join(broken))
   229	        pytest.fail("الخاصيّةُ انكسرت: " + " | ".join(broken))
   230	    print("PROBE_HELD الخاصيّةُ لم تنكسر")
=== RAW [22] END ===
=== RAW [23] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_probe.db .venv/bin/python -m pytest federal/executive/services/tests/test_grok_4_7_w605_probe.py -q -s
EXIT: 0
BYTES: 2879
SHA256: 0c0face4866c4fbe33cefb759af1e3f7a6a821891063de8ceda9a8f76dae6f69
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

federal/executive/services/tests/test_grok_4_7_w605_probe.py PROBE_BEFORE rulings=0 ruling_procs=0 case_status=assigned
PROBE_EXC type=core.sovereignty.compensation.CompensationRequired
PROBE_EXC text=العمليّةُ «judiciary.ruling.issue:lcs-e6565b8e-c542-46cb-898c-40934919e212:FIRST_INSTANCE:g0@attempt2» على العقد «EC-6202847ef5276862» فشلت (IdempotencyError: العمليّةُ «judiciary.ruling.issue:lcs-e6565b8e-c542-46cb-898c-40934919e212:FIRST_INSTANCE:g0» فشلت: فشلٌ بعدَ عودةِ المُطبِّقِ داخلَ execute — لا إسقاطَ mark_succeeded — مسبارُ grok_4_7) ولم يُعوَّض كلُّ أثرِها. الباقي نافذًا: CREATE:judiciary/rulings/lcs-e6565b8e-c542-46cb-898c-40934919e212/FIRST_INSTANCE/g0. يلزمُ قرارٌ بشريّ. الحالة: COMPENSATION_FAILED.
PROBE_PARTIAL_COMMITTED=True
PROBE_CAUSE type=core.sovereignty.idempotency.IdempotencyError text=العمليّةُ «judiciary.ruling.issue:lcs-e6565b8e-c542-46cb-898c-40934919e212:FIRST_INSTANCE:g0» فشلت: فشلٌ بعدَ عودةِ المُطبِّقِ داخلَ execute — لا إسقاطَ mark_succeeded — مسبارُ grok_4_7
PROBE_AFTER rulings=0 ruling_procs=1 case_status=decided status_before=assigned
PROBE_LEDGER status=FAILED_FINAL applied=('CREATE:judiciary/rulings/lcs-e6565b8e-c542-46cb-898c-40934919e212/FIRST_INSTANCE/g0',) reason=IdempotencyError: العمليّةُ «judiciary.ruling.issue:lcs-e6565b8e-c542-46cb-898c-40934919e212:FIRST_INSTANCE:g0» فشلت: فشلٌ بعدَ عودةِ المُطبِّقِ داخلَ execute — لا إسقاطَ mark_succeeded — مسبارُ grok_4_7 — تعويضٌ غيرُ نظيفٍ (CMP-69870fdb3a1d66d4a82a) يلزمُ قرارٌ بشريّ
PROBE_OUTCOME status=COMPENSATION_FAILED state_is_clean=False requires_human=True residual=('CREATE:judiciary/rulings/lcs-e6565b8e-c542-46cb-898c-40934919e212/FIRST_INSTANCE/g0',)
PROBE_RETRY type=core.sovereignty.idempotency.IdempotencyError text=العمليّةُ «judiciary.ruling.issue:lcs-e6565b8e-c542-46cb-898c-40934919e212:FIRST_INSTANCE:g0» في حالةٍ نهائيّة «FAILED_FINAL». لا انتقالَ من النهائي.
PROBE_RETRY_ROWS rulings=0 ruling_procs=1 case_status=decided
PROBE_HELD الخاصيّةُ لم تنكسر
.

============================== 1 passed in 1.72s ===============================
=== RAW [23] END ===
=== RAW [24] BEGIN ===
CMD: python3 /home/user/workspace/council_w605/grok_4_7/probe/rerun_mutations.py
EXIT: 0
BYTES: 15330
SHA256: 254b633d0934689154cc982181c32cb4ce545040e9b0863d97583fcb0cee80f1
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w605/grok_4_7/probe/rerun_mutations.py:171: SyntaxWarning: 'return' in a 'finally' block
  return 2
===== M1 BEGIN k=t1 or t2 =====
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items / 7 deselected / 3 selected

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py FF [ 66%]
F                                                                        [100%]

=================================== FAILURES ===================================
E   assert 0 == 1
     +  where 0 = len([])
     +    where [] = <tests.test_wi105_issue_ruling_sovereign.RecordingJudiciaryAuthorizer object at 0x7f2e99fcd010>.results
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:402: assert 0 == 1
E   Failed: DID NOT RAISE SovereigntyViolation
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:452: Failed: DID NOT RAISE SovereigntyViolation
E   Failed: DID NOT RAISE CompensationRequired
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:885: Failed: DID NOT RAISE CompensationRequired
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t1_issue_ruling_crosses_boundary_as_judicial
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t2_executive_actor_is_denied
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t10_second_failed_episode_compensates_again
======================= 3 failed, 7 deselected in 1.26s ========================
===== M1 EXIT=1 =====
===== M2 BEGIN k=t4 =====
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items / 9 deselected / 1 selected

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py F  [100%]

=================================== FAILURES ===================================
E   core.sovereignty.idempotency.IdempotencyKeyReuseError: المفتاحُ «judiciary.ruling.issue:lcs-bc826097-a358-4aaf-a3b8-b41b4604cded:FIRST_INSTANCE» مُستعمَلٌ ببصمةٍ مختلفة.
/home/user/workspace/council_w605/grok_4_7/repo/core/sovereignty/idempotency.py:846: core.sovereignty.idempotency.IdempotencyKeyReuseError: المفتاحُ «judiciary.ruling.issue:lcs-bc826097-a358-4aaf-a3b8-b41b4604cded:FIRST_INSTANCE» مُستعمَلٌ ببصمةٍ مختلفة.
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t4_replacement_after_vacation_uses_new_generation
======================= 1 failed, 9 deselected in 0.95s ========================
===== M2 EXIT=1 =====
===== M3 BEGIN k=t5 =====
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items / 9 deselected / 1 selected

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py F  [100%]

=================================== FAILURES ===================================
E   AttributeError: 'NoneType' object has no attribute 'id'
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py:182: AttributeError: 'NoneType' object has no attribute 'id'
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t5_duplicate_rejected_before_boundary
======================= 1 failed, 9 deselected in 0.92s ========================
===== M3 EXIT=1 =====
===== M4 BEGIN k=t1 =====
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items / 8 deselected / 2 selected

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py FF [100%]

=================================== FAILURES ===================================
E   core.sovereignty.enforcement_boundary.JurisdictionNotDeclaredError: الفعلُ «issue_ruling» قضائيٌّ ولم يُقدَّم له طلبُ اختصاصٍ مُعلَن. الجدارُ لا يُفحَصُ بالنيّة، ولا يعبرُ فعلٌ قضائيٌّ بلا نطاقِ محكمةٍ ونطاقِ قضيّةٍ ونطاقِ منصبٍ مُصرَّحٍ بها.
/home/user/workspace/council_w605/grok_4_7/repo/core/sovereignty/enforcement_boundary.py:546: core.sovereignty.enforcement_boundary.JurisdictionNotDeclaredError: الفعلُ «issue_ruling» قضائيٌّ ولم يُقدَّم له طلبُ اختصاصٍ مُعلَن. الجدارُ لا يُفحَصُ بالنيّة، ولا يعبرُ فعلٌ قضائيٌّ بلا نطاقِ محكمةٍ ونطاقِ قضيّةٍ ونطاقِ منصبٍ مُصرَّحٍ بها.
E   core.sovereignty.enforcement_boundary.JurisdictionNotDeclaredError: الفعلُ «issue_ruling» قضائيٌّ ولم يُقدَّم له طلبُ اختصاصٍ مُعلَن. الجدارُ لا يُفحَصُ بالنيّة، ولا يعبرُ فعلٌ قضائيٌّ بلا نطاقِ محكمةٍ ونطاقِ قضيّةٍ ونطاقِ منصبٍ مُصرَّحٍ بها.
/home/user/workspace/council_w605/grok_4_7/repo/core/sovereignty/enforcement_boundary.py:546: core.sovereignty.enforcement_boundary.JurisdictionNotDeclaredError: الفعلُ «issue_ruling» قضائيٌّ ولم يُقدَّم له طلبُ اختصاصٍ مُعلَن. الجدارُ لا يُفحَصُ بالنيّة، ولا يعبرُ فعلٌ قضائيٌّ بلا نطاقِ محكمةٍ ونطاقِ قضيّةٍ ونطاقِ منصبٍ مُصرَّحٍ بها.
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t1_issue_ruling_crosses_boundary_as_judicial
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t10_second_failed_episode_compensates_again
======================= 2 failed, 8 deselected in 1.10s ========================
===== M4 EXIT=1 =====
===== M5 BEGIN k=t6p or t8 or t9 or t10 =====
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items / 6 deselected / 4 selected

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py FF [ 50%]
FF                                                                       [100%]

=================================== FAILURES ===================================
E   RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — T6p
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:640: RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — T6p
E   RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — T8
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:640: RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — T8
E   RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — T9
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:640: RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — T9
E   RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — T10
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:640: RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — T10
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t6p_boundary_compensates_failed_settle_on_production_path
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t8_boundary_compensates_register_identity_on_production_path
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t9_failing_compensator_closes_operation_final
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t10_second_failed_episode_compensates_again
======================= 4 failed, 6 deselected in 1.25s ========================
===== M5 EXIT=1 =====
===== M6 BEGIN k=t9 =====
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items / 9 deselected / 1 selected

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py F  [100%]

=================================== FAILURES ===================================
E   AssertionError: assert <OperationStatus.FAILED_RETRYABLE: 'FAILED_RETRYABLE'> is <OperationStatus.FAILED_FINAL: 'FAILED_FINAL'>
     +  where <OperationStatus.FAILED_RETRYABLE: 'FAILED_RETRYABLE'> = IdempotencyRecord(key=IdempotencyKey(scope='judiciary.ruling.issue', value='lcs-8ae5aad4-d347-4772-b4df-bac2809e66d3:F...— عُوِّضَ آليًّا في الحدّ (CMP-02fafc9fd11be6df7e94)', recovered_at=None, succeeded_at=None, has_external_effect=False).status
     +  and   <OperationStatus.FAILED_FINAL: 'FAILED_FINAL'> = <enum 'OperationStatus'>.FAILED_FINAL
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:856: AssertionError: assert <OperationStatus.FAILED_RETRYABLE: 'FAILED_RETRYABLE'> is <OperationStatus.FAILED_FINAL: 'FAILED_FINAL'>
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t9_failing_compensator_closes_operation_final
======================= 1 failed, 9 deselected in 0.93s ========================
===== M6 EXIT=1 =====
===== M7 BEGIN k=t9 =====
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items / 9 deselected / 1 selected

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py F  [100%]

=================================== FAILURES ===================================
E   AssertionError: assert <OperationStatus.FAILED_RETRYABLE: 'FAILED_RETRYABLE'> is <OperationStatus.FAILED_FINAL: 'FAILED_FINAL'>
     +  where <OperationStatus.FAILED_RETRYABLE: 'FAILED_RETRYABLE'> = IdempotencyRecord(key=IdempotencyKey(scope='judiciary.ruling.issue', value='lcs-c220fe30-2e36-41ab-8e34-e255d1e6494c:F...ُ نظيفٍ (CMP-72ab95598e9c9afd34f4) يلزمُ قرارٌ بشريّ', recovered_at=None, succeeded_at=None, has_external_effect=False).status
     +  and   <OperationStatus.FAILED_FINAL: 'FAILED_FINAL'> = <enum 'OperationStatus'>.FAILED_FINAL
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:856: AssertionError: assert <OperationStatus.FAILED_RETRYABLE: 'FAILED_RETRYABLE'> is <OperationStatus.FAILED_FINAL: 'FAILED_FINAL'>
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t9_failing_compensator_closes_operation_final
======================= 1 failed, 9 deselected in 0.94s ========================
===== M7 EXIT=1 =====
===== M8 BEGIN k=t10 =====
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items / 9 deselected / 1 selected

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py F  [100%]

=================================== FAILURES ===================================
E   AssertionError: assert (1, 1, 'decided') == (0, 0, 'assigned')
      
      At index 0 diff: 1 != 0
      Use -v to get more diff
/home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py:889: AssertionError: assert (1, 1, 'decided') == (0, 0, 'assigned')
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t10_second_failed_episode_compensates_again
======================= 1 failed, 9 deselected in 1.06s ========================
===== M8 EXIT=1 =====
===== RESTORED DIFF STAT =====
(empty)
=== RAW [24] END ===
=== RAW [25] BEGIN ===
CMD: cd /home/user/workspace/council_w605/grok_4_7/repo && cp docs/audit/evidence/W-601/test_w601_gap_probe.py federal/executive/services/tests/test_w601_gap_probe.py && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/grok_4_7/tmp/amos_w601.db .venv/bin/python -m pytest federal/executive/services/tests/test_w601_gap_probe.py -s -q -p no:cacheprovider ; ec=$? ; rm -f federal/executive/services/tests/test_w601_gap_probe.py ; exit $ec
EXIT: 0
BYTES: 2182
SHA256: ba3f6acc7b4894619f25f2274699a99864bba0e87835d055f071e1f06cffa1e0
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w605/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 2 items

federal/executive/services/tests/test_w601_gap_probe.py 
## (أ) issue_ruling — J1 · WI-105
حالةُ القضيّةِ قبلَ النداء: assigned
الاستثناءُ الناتج: core.sovereignty.compensation.CompensationRequired: العمليّةُ «judiciary.ruling.issue:lcs-7f7529a3-6190-467b-a7cf-69bb5dacceec:FIRST_INSTANCE:g0@attempt1» على العقد «EC-ba4d2c6bfb50c4ef» فشلت (RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — مسبارُ W-601) وعُوِّضَ أثرُها كاملًا فرجعتِ الحالة. الحالة: COMPENSATED.
صفوفُ الحكمِ: 0 · إجراءاتُ RULING: 0 · حالةُ القضيّة: assigned
هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: 1
سجلُّ الذرّيّة: FAILED_RETRYABLE
إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: core.sovereignty.idempotency.IdempotencyError
.
## (ب) register_identity — WI-082
الاستثناءُ الناتج: core.sovereignty.compensation.CompensationRequired: العمليّةُ «agents.identity.spawn:w601-probe-agent@attempt1» على العقد «EC-430477290d128166» فشلت (RuntimeError: تثبيتُ النجاحِ مُسقَطٌ — مسبارُ W-601) وعُوِّضَ أثرُها كاملًا فرجعتِ الحالة. الحالة: COMPENSATED.
صفُّ الهويّة: غائب
هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: 1
سجلُّ الذرّيّة: FAILED_RETRYABLE
إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: core.sovereignty.idempotency.IdempotencyError
.

============================== 2 passed in 1.02s ===============================
=== RAW [25] END ===
VERDICT_PER_CRITERION: (1) نعم لشقِّ التزامِ الملحقِ قبلَ الشِّفرةِ — كتلةُ 5: e13fe2f (W-602 · ملحقُ § 7 · لا شفرة) يسبقُ 968e5ba (W-603 · شِفرةُ الحدِّ). موافقةُ المالكِ على D1/D4/D6/D7: صدرتْ (Q-69) ولا تُحاكَمْ هنا. (2) نعم — كتلةُ 10: 10 passed (T1–T5 تُثبِتُ guard_declared وطلبَ الاختصاصِ منَ البياناتِ الحيّةِ والمُعوِّضَ الحقيقيَّ ومفتاحَ الجيلِ والمكرَّرَ قبلَ الحدِّ). (3) نعم — كتلةُ 9: مواضعُ 220 · تعبرُ 18 · لا تعبرُ 181. كتلةُ 16: قبلَ الوصلِ وبعدَه 181←181 و18 و220←220 بلا نموٍّ (تصحيحُ W-588: 220 لا 219). (4) نعم — كتلةُ 10: T1–T7 ناجحةٌ ضمنَ العشرةِ. كتلةُ 24: M1 أسقطَ T1 وT2 (EXIT=1) · M2 أسقطَ T4 · M3 أسقطَ T5 · M4 أسقطَ T1. (5) نعم — كتلةُ 6: فرقُ الفحوصِ القائمةِ فارغٌ (BYTES 0). كتلةُ 13: حزمةُ services 1485 passed و53 skipped وEXIT 0 وتشملُ WI-082 وWI-105. كتلةُ 12: tests/sovereignty 818 passed. شِقُّ CI يقرؤُه المنسِّقُ. كتلةُ 11 خرجتْ 1 لأنَّ WI-082 أخطأَ في الإعدادِ (DELETE FROM agents / FOREIGN KEY) على ملفِّ sqlite المشتركِ معَ الأمرِ 10؛ الفحوصُ نفسُها خضراءُ في كتلةِ 13 فليست عيبَ دفعةٍ. (6) نعم — إعادةُ التشغيلِ هي هذا الحكمُ (كتلُ 1–25). (7) نعم — (أ) الموضعُ مقيسٌ قبلَ التغييرِ: كتلُ 3 و15 (W-601 قبلَ W-603 · RuntimeError · نداءاتُ المُعوِّضِ 0) والوصلُ في ملفِّ الحدِّ وحدَه: كتلةُ 4 (core/sovereignty/enforcement_boundary.py وحده منَ النواةِ) وكتلةُ 7. (ب) الملحقُ § 7 قبلَ الشِّفرةِ: كتلةُ 5. (ج) T6p/T8/T9/T10 ناجحةٌ: كتلةُ 10. M5–M8 كلٌّ أسقطَ فحصَه: كتلةُ 16 وكتلةُ 24 (M5 أسقطَ الأربعةَ · M6 وM7 أسقطا T9 · M8 أسقطَ T10) والشجرةُ استُعيدتْ (DIFF STAT فارغٌ). فحوصُ tests/sovereignty وtest_2b وWI-082 القائمةُ بلا تعديلٍ: كتلةُ 6. مسبارُ W-601 بعدَ الوصلِ: كتلةُ 25 — compensate نداءٌ واحدٌ في السطحَينِ · الصفوفُ نظيفةٌ · FAILED_RETRYABLE. (د) الحدودُ المعلنةُ صادقةٌ: كتلةُ 18 (DISC-129) تطابقُ كتلةَ 25 (إعادةٌ فوريّةٌ IdempotencyError بلا صفٍّ) و§ 7.5 في كتلةِ 14.
PROBES: كتلةُ الشِّفرةِ 22 · كتلةُ التشغيلِ 23 · الخاصيّةُ: إغلاقُ التعويضِ على المسارِ الإنتاجيِّ FederalJudiciary.issue_ruling عندَ فشلٍ بعدَ عودةِ المُطبِّقِ داخلَ execute (لا إسقاطَ mark_succeeded، فيُنادى mark_failed أوّلًا) معَ مُعوِّضٍ إنتاجيٍّ يلتزمُ حذفَ صفِّ الحكمِ ثمَّ يرفعُ قبلَ حذفِ إجراءِ RULING وإرجاعِ حالةِ القضيّةِ — المطلوبُ CompensationRequired وstate_is_clean False وrequires_human والباقي مُسمًّى وFAILED_FINAL ورفضُ الإعادةِ بلا حكمٍ ثانٍ. انكسرت؟ لا (PROBE_HELD · EXIT 0 · rulings بقيت 0 · الإعادةُ IdempotencyError على FAILED_FINAL).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — لم أقرأْ تقريرَ منفِّذٍ ولا دليلَ مقعدٍ آخرَ ولا سجلَّ إكمالٍ للحكمِ. الاستثناءُ: بحثٌ عن تعريفِ الطفراتِ داخلَ docs/audit/evidence في الاستنساخِ أظهرَ أسماءَ ملفّاتِ جولاتٍ سابقةٍ في قائمةِ النتائجِ ولم تُفتحْ ولم يُبنَ عليها الحكمُ. القراءةُ الحكميّةُ منَ الإحاطةِ والاستنساخِ ودليلي وحدَها.
VERDICT: PASS لكلِّ المعاييرِ
