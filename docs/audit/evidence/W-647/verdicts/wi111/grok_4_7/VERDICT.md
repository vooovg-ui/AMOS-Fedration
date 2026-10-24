# حكمُ مقعدِ المجلسِ — grok_4_7 (عائلةُ grok) · جولةُ WI-111 (J2+J3) (W-647)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-111 (J2+J3) (الطابورُ الواحدُ · التوجيهُ 19 § 2 · بروتوكولُ Q-59) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذورِهِ الخاصّةِ (council_w641/grok_4_7/wi111) — منسوخٌ آليًّا، وما بعدَ الفاصلِ بايتًا ببايتٍ (sha256 `dd5a4ece9e020e75887ebeb962cc1517c2e69a8c07a89a2135a0469fd8cc443b`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-111 (J2+J3) عندَ العقدةِ `4b5b2be5` — إحاطةٌ مبصومةٌ ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-647) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-24

---
MODEL: grok_4_7
FAMILY: grok
RUN_DATE: 2026-10-24 07:12 +00:00
NODE: 4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
CLONE_PATH: /home/user/workspace/council_w641/grok_4_7/wi111/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi111/
 2. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi111/)
 3. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff --stat 4247c68fea97c3bdba583f590ed5f3bda679d12e HEAD -- federal/ tools/ tests/ agents/ core/ src/
 5. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && bash tools/dev/bootstrap.sh --verify
 6. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log --format='%h %cI %s' 83994514d831d184c5fc1855ef5edc0bf777b0ad..HEAD --max-count=30
 7. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log --format='%h %cI %s' -4 -- docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
 8. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff 83994514d831d184c5fc1855ef5edc0bf777b0ad 4247c68fea97c3bdba583f590ed5f3bda679d12e -- federal/executive/services/src/amos_federation/services/federal_judiciary/ core/constitutional_engine/rules.py core/sovereignty/jurisdiction.py
 9. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff 83994514d831d184c5fc1855ef5edc0bf777b0ad 4247c68fea97c3bdba583f590ed5f3bda679d12e -- federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py federal/executive/services/tests/test_r7d_federal_judiciary.py
 10. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat federal/executive/services/tests/test_wi111_judiciary_docket_sovereign.py
 11. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 12. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi111_judiciary_docket_sovereign.py -q
 13. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi105_issue_ruling_sovereign.py tests/test_r7d_federal_judiciary.py -q
 14. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests -q
 15. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/audit/judicial_gate_probe.py
 16. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md
 17. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-638/inventory_before_wi111.txt docs/audit/evidence/W-640/inventory_after_wi111.txt
 18. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-641/mutation_probe_wi111.py.txt
 19. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python docs/audit/evidence/W-641/mutation_probe_wi111.py.txt
 20. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && rg -n "D17-2|Q-61" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 21. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && sha256sum docs/audit/evidence/W-641/briefs_wi111/briefing_grok_4_7.md
 22. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-641/briefs_wi111/SHA256SUMS
 23. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py tests/governance/test_step7_factory_surfaces.py -q
 24. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
 25. nl -ba /home/user/workspace/council_w641/grok_4_7/wi111/probe/wi111_break_judiciary.py
 26. cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python /home/user/workspace/council_w641/grok_4_7/wi111/probe/wi111_break_judiciary.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi111/
EXIT: 0
BYTES: 41
SHA256: a3e2f8d92a955524b52c488f6eab3a10df32c172749d966186bbfc125cdea034
NO_EOL: 0
--- OUTPUT ---
4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi111/)
EXIT: 0
BYTES: 788
SHA256: 345a4d3f8be8230bc5fb5e31c5c1574e05df03df3e258e80bbb9ea33dba1ab4a
NO_EOL: 0
--- OUTPUT ---
Note: switching to '4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 4b5b2be5 W-641: WI-111/WI-109/WI-110 IN_PROGRESS→IN_REVIEW · إحاطاتُ جولتَي WI-111 وWI-084 مبصومةٌ (الطابورُ الواحدُ) · مسبارُ طفراتِ WI-111
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: a3e2f8d92a955524b52c488f6eab3a10df32c172749d966186bbfc125cdea034
NO_EOL: 0
--- OUTPUT ---
4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff --stat 4247c68fea97c3bdba583f590ed5f3bda679d12e HEAD -- federal/ tools/ tests/ agents/ core/ src/
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && bash tools/dev/bootstrap.sh --verify
EXIT: 0
BYTES: 7017
SHA256: 07580a200541555cd624ea2d621a763f098a06b3579a107d478fa1488ef567a4
NO_EOL: 0
--- OUTPUT ---
• الجذر: /home/user/workspace/council_w641/grok_4_7/wi111/repo
• ثُبِّتَ خُطّافُ pre-push (يُشغِّلُ حرسَ ما قبلَ الدفعِ على كلِّ دفعٍ — WI-078)
• إنشاءُ بيئةٍ معزولةٍ في .venv
• تركيبُ تبعيّاتِ الجذر (requirements-dev.txt)
• تركيبُ حزمةِ الخدماتِ (قد تطولُ: تبعيّاتٌ كثيرة)
• تركيبُ ruff==0.6.9 (‏المُثبَّتُ في .github/workflows/ci.yml)
✓ البيئةُ جاهزة. للتنشيطِ في جلسةٍ جديدة: source .venv/bin/activate
── حزمةُ الجذر ──
........................................................................ [  2%]
........................................................................ [  5%]
........................................................................ [  7%]
........................................................................ [ 10%]
........................................................................ [ 13%]
........................................................................ [ 15%]
........................................................................ [ 18%]
........................................................................ [ 21%]
........................................................................ [ 23%]
........................................................................ [ 26%]
........................................................................ [ 29%]
........................................................................ [ 31%]
........................................................................ [ 34%]
........................................................................ [ 37%]
........................................................................ [ 39%]
........................................................................ [ 42%]
........................................................................ [ 44%]
........................................................................ [ 47%]
........................................................................ [ 50%]
........................................................................ [ 52%]
........................................................................ [ 55%]
........................................................................ [ 58%]
........................................................................ [ 60%]
........................................................................ [ 63%]
........................................................................ [ 66%]
........................................................................ [ 68%]
........................................................................ [ 71%]
.........................................................s.............. [ 74%]
........................................................................ [ 76%]
........................................................................ [ 79%]
........................................................................ [ 81%]
........................................................................ [ 84%]
........................................................................ [ 87%]
........................................................................ [ 89%]
........................................................................ [ 92%]
........................................................................ [ 95%]
........................................................................ [ 97%]
...........................................................              [100%]
2722 passed, 1 skipped in 463.07s (0:07:43)
── بوّاباتُ الحوكمة ──
[TRUTH AUDIT] أقاليم: 12 | مُثبَتة: 0 | مخالفات: 61
  - IN_MEMORY_STORE: 59
  - HARDCODED_TRUTH: 2
[TRUTH AUDIT] كُتبت: /home/user/workspace/council_w641/grok_4_7/wi111/repo/docs/audit/TRUTH_MATRIX.md
فحص هوية المستودع (المادة التاسعة): .
==============================================================

نجح: كل مجلد يحمل بطاقة هوية كاملة، وكل ملف يُعلن هدفه.

================================================================
  AMOS-Federation P3 Smoke Tests — Summary
================================================================
Domain           Status   Detail
--------------------------------
tools            UNMEASURED   count=10, source=snapshot:2026-08-22T18:45:00+00:00
agents           UNMEASURED   count=5116, source=snapshot:2026-08-22T18:45:00+00:00
institutions     UNMEASURED   count=8, source=snapshot:2026-08-22T18:45:00+00:00
royal            UNMEASURED   guards=7, decrees=1, source=snapshot:2026-08-22T18:45:00+00:00
ops              UNMEASURED   count=71, source=snapshot:2026-08-22T18:45:00+00:00
federal          UNMEASURED   transactions=0, budgets=0, executive_roles=5, source=snapshot:2026-08-22T18:45:00+00:00
core             UNMEASURED   memories=3, experiences=11, source=snapshot:2026-08-22T18:45:00+00:00
runtime          UNMEASURED   tasks=28, events=1027, source=snapshot:2026-08-22T18:45:00+00:00
interfaces       UNMEASURED   count=0, source=snapshot:2026-08-22T18:45:00+00:00
states           UNMEASURED   legislations=0, compliance_reports=0, source=snapshot:2026-08-22T18:45:00+00:00
docs             PASS         nucleus_files=106, schemas=13, registries=12, source=filesystem
tests            PASS         nucleus_files=5, source=filesystem
--------------------------------
  2/12 أقاليمُ قِيسَت ونجحت | 10 غيرُ مقيسة | 0 فاشلة
  تنبيه: «غير مقيس» ليس نجاحًا — الأرقامُ أعلاه مُقتبَسةٌ من لَقطةٍ مُؤرَّخة،
  ولا تُقبَلُ دليلًا في بوّابةٍ تشترطُ إثباتًا. هيِّئ AMOS_TRUTH_DB_URL،
  أو شغِّلْ بـ --require-measured لتفشلَ البوّابةُ عندَ غيابِ القياس.
================================================================

لا إقليمَ فاشلًا — وبقيَ 10 إقليمًا غيرَ مقيس.
── نظافةُ الشجرةِ بعدَ التشغيل (O-1N-1) ──
✓ الشجرةُ نظيفةٌ بعدَ حزمةٍ كاملة.

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
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log --format='%h %cI %s' 83994514d831d184c5fc1855ef5edc0bf777b0ad..HEAD --max-count=30
EXIT: 0
BYTES: 404
SHA256: 90154b772801a5b57b5871845c205ed03c2e9126c9bc5d3bdfad83fb7466dcf5
NO_EOL: 0
--- OUTPUT ---
4b5b2be5 2026-10-24T00:00:44Z W-641: WI-111/WI-109/WI-110 IN_PROGRESS→IN_REVIEW · إحاطاتُ جولتَي WI-111 وWI-084 مبصومةٌ (الطابورُ الواحدُ) · مسبارُ طفراتِ WI-111
4247c68f 2026-10-23T23:56:33Z W-640: WI-111 (J2+J3) — 15 سطحًا قضائيًّا تعبرُ بفاعلِ الوحدةِ وأفعالِ D17-2 · D-4 157←142 · M1–M5 مقتولةٌ
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log --format='%h %cI %s' -4 -- docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
EXIT: 0
BYTES: 801
SHA256: a5c71818c8d524975773d5768cfa63380b5d5807a1fbca12693ddfeaa3eba62c
NO_EOL: 0
--- OUTPUT ---
4247c68f 2026-10-23T23:56:33Z W-640: WI-111 (J2+J3) — 15 سطحًا قضائيًّا تعبرُ بفاعلِ الوحدةِ وأفعالِ D17-2 · D-4 157←142 · M1–M5 مقتولةٌ
d6963e68 2026-10-23T22:59:40Z W-638: WI-109/WI-110/WI-111 READY→RESERVED (H3) · ملحقُ تصميمِ J2+J3 مُودَعٌ قبلَ الشِّفرةِ (15 سطحًا · D-4 متوقَّعٌ 157←142) · قياسُ ما قبلُ — لا شِفرةَ — المنسِّق Claude Opus 5.5
e594d4bd 2026-08-17T14:23:21Z R9E-CI3: إصلاح بوابة الفحص (ruff) — تناقضٌ حقيقيّ في إعادة التصدير وتنسيقٌ متروك
5220b666 2026-08-17T09:54:48Z R7-D2: القضية والأطراف والأدلّة والإجراءات — دورةُ حياةٍ لا نصٌّ حرّ
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff 83994514d831d184c5fc1855ef5edc0bf777b0ad 4247c68fea97c3bdba583f590ed5f3bda679d12e -- federal/executive/services/src/amos_federation/services/federal_judiciary/ core/constitutional_engine/rules.py core/sovereignty/jurisdiction.py
EXIT: 0
BYTES: 51370
SHA256: 72cf4f19fb435b7b8db999ec82a0302c1bd0bbd54a00c02ec935fedfb7d8d69a
NO_EOL: 0
--- OUTPUT ---
diff --git a/core/constitutional_engine/rules.py b/core/constitutional_engine/rules.py
index 1aca12a8..18b9c904 100644
--- a/core/constitutional_engine/rules.py
+++ b/core/constitutional_engine/rules.py
@@ -30,7 +30,21 @@ from .model import ActionRequest, Branch, CrownEffect, Severity
 # ---------------------------------------------------------------------------
 
 LEGISLATIVE_ACTIONS = frozenset({"legislate", "enact_policy", "amend_policy", "repeal_policy"})
-JUDICIAL_ACTIONS = frozenset({"adjudicate", "arbitrate", "interpret_constitution", "issue_ruling"})
+# معجمُ القضاءِ — قرارُ المالكِ D17-2 (خيارُ 1 · W-592) وتنفيذُه في الدفعةِ J2+J3 (WI-111).
+# كانَ أربعةَ أفعالٍ، وجدارُ الاختصاصِ (`core/sovereignty/jurisdiction.py`) يعرفُ ستّةً
+# أخرى غائبةً هنا، فمرَّت `ALLOW` لكلِّ فرعٍ (مقيسًا: `judicial_gate_probe.py` · W-638).
+# والتوسيعُ تضييقٌ لا توسيعٌ (سابقةُ Q-18): كلُّ فعلٍ يُضافُ يصيرُ حصرًا قضائيًّا يُرفَضُ
+# للفروعِ الأخرى بـ`R-003-1`. والأفعالُ الأربعةُ المؤجَّلةُ (establish_court ·
+# set_court_status · appoint_judge · submit_evidence) **غائبةٌ عمدًا** (D17-2 · D21-أ بند 9).
+JUDICIAL_ACTIONS = frozenset({
+    # المعجمُ الأصليُّ (قبلَ D17-2)
+    "adjudicate", "arbitrate", "interpret_constitution", "issue_ruling",
+    # الستّةُ القائمةُ في جدارِ الاختصاصِ (D17-2 · نعم في الجدار)
+    "refer_case", "admit_case", "vacate_ruling", "admit_evidence", "recuse_judge",
+    "register_judgment",
+    # الأربعةُ الجديدةُ في المعجمَينِ (D17-2 · لا — جديد)
+    "assign_case", "record_proceeding", "join_party", "admit_claim",
+})
 EXECUTIVE_ACTIONS = frozenset({"execute_task", "dispatch_agent", "orchestrate", "coordinate"})
 # معجمُ المالِ الدستوريّ — القرارُ السياديُّ Q-18 · الخيارُ 2 (2026-08-21).
 # كانَ المعجمُ أربعةَ أفعالٍ، فمرَّ ستةَ عشرَ فعلًا ماليًّا آخرَ `ALLOW` للتنفيذِ
diff --git a/core/sovereignty/jurisdiction.py b/core/sovereignty/jurisdiction.py
index 3a9ae87a..c9409bee 100644
--- a/core/sovereignty/jurisdiction.py
+++ b/core/sovereignty/jurisdiction.py
@@ -91,6 +91,11 @@ JUDICIAL_ACTIONS: Final[frozenset[str]] = frozenset(
         "admit_evidence",      # قبولُ دليل
         "recuse_judge",        # تنحيةُ قاضٍ (إجراءٌ داخليٌّ قضائيّ)
         "register_judgment",   # تسجيلُ الحكمِ في السجلّ
+        # الأربعةُ الجديدةُ — قرارُ المالكِ D17-2 (خيارُ 1) · الدفعةُ J2+J3 (WI-111):
+        "assign_case",         # إسنادُ القضيّةِ إلى قاضٍ في محكمتِها
+        "record_proceeding",   # قيدُ إجراءٍ في سجلِّ القضيّة
+        "join_party",          # ضمُّ طرفٍ إلى الدعوى
+        "admit_claim",         # قبولُ مطالبةٍ في الدعوى
     }
 )
 
diff --git a/federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py b/federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
index c6d9452c..4284fc34 100644
--- a/federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
+++ b/federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
@@ -48,7 +48,14 @@ from datetime import UTC, datetime
 from typing import TYPE_CHECKING, Any
 
 from sqlalchemy import func, select
+from sqlalchemy import inspect as sa_inspect
 
+from amos_federation.common.database import get_session_factory
+from amos_federation.services.executive_core.sovereignty_bridge import (
+    compensator,
+    declared_effect,
+    operation_key,
+)
 from amos_federation.services.federal_judiciary.jurisdiction import assert_jurisdiction_match
 from amos_federation.services.federal_judiciary.models import (
     CASE_TYPES,
@@ -193,6 +200,167 @@ def proceeding_dict(row: CaseProceedingModel) -> dict[str, Any]:
     }
 
 
+# ── العبورُ السياديُّ (WI-111 · الدفعةُ J2+J3 · ملحقُ التصميمِ D1–D8) ─────────────
+#
+# الفاعلُ واحدٌ للوحدةِ: مُصرِّحُ J1 نفسُه (`rulings._judiciary_authorizer` · D1) —
+# يُستورَدُ كسولًا لأنَّ `rulings` يستوردُ هذه الوحدةَ. وكلُّ عمليّةٍ عامّةٍ تعبرُ
+# تحملُ نداءَ الحدِّ **في جسدِها** (هكذا يقيسُ الجردُ)، والمُساعداتُ هنا تبني
+# المعاملاتِ فقط: الأثرَ والمفتاحَ والمُطبِّقَ والمُعوِّضَ وطلبَ الاختصاصِ.
+
+
+class JudicialLedgerDivergenceError(JudiciaryError):
+    """سجلُّ الذرّيّةِ يُثبِتُ العمليّةَ والصفُّ غائبٌ — استعادةٌ لا نجاحٌ يُزعَم (D6)."""
+
+
+def _authorizer() -> Any:
+    """مُصرِّحُ الوحدةِ القضائيّةِ الواحدُ (D1) — لا مُصرِّحَ ثانٍ."""
+    from amos_federation.services.federal_judiciary.rulings import _judiciary_authorizer
+
+    return _judiciary_authorizer()
+
+
+def judicial_request(
+    action: str,
+    *,
+    court: Any,
+    case_scope: str,
+    target: str,
+    actor_scope: str | None = None,
+    institution_id: str | None = None,
+) -> Any:
+    """طلبُ الاختصاصِ منَ البياناتِ الحيّةِ (D4) — نطاقُ المحكمةِ ونطاقُ القضيّةِ منَ الصفوفِ.
+
+    `actor_scope` منصبُ القاضي المُثبَتُ حيثُ يُثبَتُ (`vacate_ruling`)؛ وإلّا فنطاقُ
+    المحكمةِ **مُعلَنًا** — حدٌّ معلَنٌ في الملحقِ (D4): هذه الأسطحُ لا تُثبِتُ منصبًا
+    اليومَ، فيصيرُ فحصُ المنصبِ عندَها تحصيلَ حاصلٍ لا ادّعاءَ إثباتٍ.
+    """
+    import sys as _sys
+
+    from amos_federation.services.executive_core.sovereignty_bridge import locate_repo_root
+
+    root = locate_repo_root()
+    if str(root) not in _sys.path:
+        _sys.path.insert(0, str(root))
+    from core.sovereignty.jurisdiction import JudicialAction
+
+    return JudicialAction(
+        action=action,
+        court_scope=court.jurisdiction,
+        case_scope=case_scope,
+        actor_scope=court.jurisdiction if actor_scope is None else actor_scope,
+        target=target,
+        institution_id=institution_id or court.institution_id,
+        case_institution_id=court.institution_id,
+        is_royal_decree_target=False,
+    )
+
+
+def _snapshot(row: Any) -> dict[str, Any]:
+    """قيمُ الأعمدةِ كلِّها قبلَ العمليّةِ — يستعيدُها المُعوِّضُ حرفيًّا (D7)."""
+    return {attr.key: getattr(row, attr.key) for attr in sa_inspect(row).mapper.column_attrs}
+
+
+class Crossing:
+    """معاملاتُ عبورٍ واحدٍ — يبنيها `_plan_crossing` ويُمرِّرُها النداءُ إلى الحدِّ."""
+
+    def __init__(self, action: str, target: str, kwargs: dict[str, Any]) -> None:
+        self.action = action
+        self.target = target
+        self.kwargs = kwargs
+
+
+def _plan_crossing(
+    session: Session,
+    *,
+    action: str,
+    court: Any,
+    case_scope: str,
+    namespace: str,
+    key: str,
+    kind: str,
+    description: str,
+    mutate: Any,
+    snapshots: tuple[Any, ...] = (),
+    actor_scope: str | None = None,
+    institution_id: str | None = None,
+    metadata: dict[str, Any] | None = None,
+) -> Crossing:
+    """ابنِ عبورًا: أثرٌ واحدٌ مُعلَنٌ · مفتاحٌ · مُطبِّقٌ يكتبُ ويلتزمُ · مُعوِّضٌ تقنيٌّ.
+
+    `mutate(created)` يكتبُ في `session` ويُلحِقُ بـ`created` كلَّ صفٍّ يُدرِجُه
+    (`(النموذج, المعرِّف)`)؛ و`snapshots` صفوفٌ قائمةٌ يُغيِّرُها — تُلتقَطُ قيمُها قبلَ
+    الحدِّ ويُعيدُها المُعوِّضُ. والهدفُ يحملُ المفتاحَ (درسُ J1 D5: بصمةُ الإذنِ منَ
+    الفاعلِ والفعلِ والهدفِ والآثارِ، فهدفٌ بلا هويّةِ العمليّةِ يتصادمُ في الثانيةِ نفسِها).
+    """
+    target = f"judiciary/{action}/{key}"
+    effect = declared_effect(kind, target, description)
+    before = [(type(row), row.id, _snapshot(row)) for row in snapshots]
+    created: list[tuple[Any, str]] = []
+
+    def _apply(_effect: Any) -> Any:
+        """المُطبِّقُ — الكتابةُ والالتزامُ في معاملةٍ واحدةٍ خلفَ الحدِّ."""
+        value = mutate(created)
+        session.commit()
+        return value
+
+    def _restore() -> None:
+        """المُعوِّضُ (D7): استعادةٌ تقنيّةٌ في جلسةٍ جديدةٍ — حذفُ المُدرَجِ وإرجاعُ المنقولِ.
+
+        العمليّةُ لم تثبتْ (فشلٌ بعدَ الالتزامِ) فلا أثرَ قضائيًّا وُجِدَ؛ «الحذفُ شأنٌ
+        تنفيذيّ» — والمُعوِّضُ ليس أثرًا مُعلَنًا، فيُكتَبُ ذلك صريحًا هنا كما في J1.
+        """
+        restore = get_session_factory()()
+        try:
+            for model, row_id in reversed(created):
+                row = restore.get(model, row_id)
+                if row is not None:
+                    restore.delete(row)
+            for model, row_id, values in before:
+                row = restore.get(model, row_id)
+                if row is not None:
+                    for name, value in values.items():
+                        setattr(row, name, value)
+            restore.commit()
+        finally:
+            restore.close()
+
+    kwargs: dict[str, Any] = {
+        "declared_effects": (effect,),
+        "applier": _apply,
+        "operation_key": operation_key(namespace, key),
+        "compensators": (
+            compensator(
+                effect.signature,
+                _restore,
+                "استعادةٌ تقنيّةٌ: حذفُ الصفوفِ المُدرَجةِ وإرجاعُ الحقولِ المنقولةِ "
+                "إلى قيمِها قبلَ العمليّةِ — العمليّةُ لم تثبتْ",
+            ),
+        ),
+        "metadata": {"key": key, **(metadata or {})},
+        "judicial_action": judicial_request(
+            action,
+            court=court,
+            case_scope=case_scope,
+            target=target,
+            actor_scope=actor_scope,
+            institution_id=institution_id,
+        ),
+    }
+    return Crossing(action, target, kwargs)
+
+
+def crossed_value(guarded: Any, *, replay: Any, what: str) -> Any:
+    """قيمةُ العبورِ — والإعادةُ تُقرأُ ولا تُكتَبُ (D6): إن غابَ الصفُّ فتفرُّقٌ صريحٌ."""
+    if not guarded.is_replay:
+        return guarded.value
+    value = replay()
+    if value is None:
+        raise JudicialLedgerDivergenceError(
+            f"سجلُّ الذرّيّةِ يُثبِتُ {what} ولا صفَّ قائمًا — استعادةٌ مطلوبةٌ لا نجاحٌ يُزعَم"
+        )
+    return value
+
+
 def load_case(session: Session, case_id: str, *, tenant_id: str) -> LegalCaseModel:
     row = session.get(LegalCaseModel, case_id)
     if row is None or row.tenant_id != tenant_id:
@@ -275,9 +443,35 @@ def open_case(
         opened_by_identity_id=opened_by_identity_id,
         tenant_id=tenant_id,
     )
-    session.add(row)
-    session.flush()
-    return row
+
+    def _insert(created: list[tuple[Any, str]]) -> LegalCaseModel:
+        session.add(row)
+        session.flush()
+        created.append((LegalCaseModel, row.id))
+        return row
+
+    # `admit_case` (D17-2) · المفتاحُ (المستأجرُ · المرجعُ) — فريدٌ بقيدِ القاعدةِ (D6).
+    plan = _plan_crossing(
+        session,
+        action="admit_case",
+        court=court,
+        case_scope=court.jurisdiction,
+        namespace="judiciary.case.open",
+        key=f"{tenant_id}:{reference}",
+        kind="CREATE",
+        description=f"قبولُ قضيّةٍ بالمرجعِ '{reference}' في المحكمةِ '{court.code}'",
+        mutate=_insert,
+    )
+    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)
+    return crossed_value(
+        guarded,
+        replay=lambda: session.execute(
+            select(LegalCaseModel).where(
+                LegalCaseModel.reference == reference, LegalCaseModel.tenant_id == tenant_id
+            )
+        ).scalar_one_or_none(),
+        what=f"قبولَ القضيّةِ '{reference}'",
+    )
 
 
 def file_case(session: Session, *, case_id: str, tenant_id: str) -> LegalCaseModel:
@@ -289,8 +483,10 @@ def file_case(session: Session, *, case_id: str, tenant_id: str) -> LegalCaseMod
     return row
 
 
-def assign_case(session: Session, *, case_id: str, judge_id: str, tenant_id: str) -> LegalCaseModel:
-    """`filed → assigned` بقاضٍ مُقلَّدٍ نشطٍ في محكمة القضية بالذات."""
+def check_assign(
+    session: Session, *, case_id: str, judge_id: str, tenant_id: str
+) -> tuple[LegalCaseModel, CourtJudgeModel]:
+    """فحوصُ الإسنادِ كلُّها — تُنادى قبلَ الحدِّ وفي الكاتبِ نفسِه (مصدرٌ واحدٌ)."""
     row = load_case(session, case_id, tenant_id=tenant_id)
     assert_transition(row.status, "assigned")
     judge = session.get(CourtJudgeModel, judge_id)
@@ -300,6 +496,12 @@ def assign_case(session: Session, *, case_id: str, judge_id: str, tenant_id: str
         raise JudiciaryError(f"القاضي حالتُه '{judge.status}' لا 'active' — لا إسنادَ إليه")
     if judge.court_id != row.court_id:
         raise JudiciaryError("القاضي مُقلَّدٌ في محكمةٍ أخرى — لا إسنادَ عبر المحاكم")
+    return row, judge
+
+
+def assign_case(session: Session, *, case_id: str, judge_id: str, tenant_id: str) -> LegalCaseModel:
+    """`filed → assigned` بقاضٍ مُقلَّدٍ نشطٍ في محكمة القضية بالذات."""
+    row, judge = check_assign(session, case_id=case_id, judge_id=judge_id, tenant_id=tenant_id)
     row.assigned_judge_id = judge.id
     row.assigned_at = _now()
     row.status = "assigned"
@@ -331,15 +533,21 @@ def advance_case(session: Session, *, case_id: str, target: str, tenant_id: str)
     return row
 
 
+def check_close(session: Session, *, case_id: str, reason: str, tenant_id: str) -> LegalCaseModel:
+    """فحوصُ الإغلاقِ — قبلَ الحدِّ وفي الكاتبِ نفسِه (مصدرٌ واحدٌ)."""
+    if not reason.strip():
+        raise JudiciaryError("إغلاقُ القضية يلزمه سببٌ مكتوب")
+    row = load_case(session, case_id, tenant_id=tenant_id)
+    assert_transition(row.status, "closed")
+    return row
+
+
 def close_case(
     session: Session, *, case_id: str, reason: str, tenant_id: str
 ) -> tuple[LegalCaseModel, str]:
     """`decided|enforcement → closed` بسببٍ مكتوبٍ وطابعِ إغلاق."""
-    if not reason.strip():
-        raise JudiciaryError("إغلاقُ القضية يلزمه سببٌ مكتوب")
-    row = load_case(session, case_id, tenant_id=tenant_id)
+    row = check_close(session, case_id=case_id, reason=reason, tenant_id=tenant_id)
     previous = row.status
-    assert_transition(previous, "closed")
     row.status = "closed"
     row.closed_at = _now()
     row.closure_reason = reason
@@ -388,9 +596,37 @@ def add_party(
         added_by=added_by,
         tenant_id=tenant_id,
     )
-    session.add(row)
-    session.flush()
-    return row
+
+    def _insert(created: list[tuple[Any, str]]) -> CasePartyModel:
+        session.add(row)
+        session.flush()
+        created.append((CasePartyModel, row.id))
+        return row
+
+    # `join_party` (D17-2) · المفتاحُ (القضيّةُ · الهويّةُ · الدورُ) — والمكرَّرُ رُفِضَ قبلَ الحدِّ.
+    plan = _plan_crossing(
+        session,
+        action="join_party",
+        court=load_court(session, case.court_id, tenant_id=tenant_id),
+        case_scope=case.jurisdiction,
+        namespace="judiciary.party.add",
+        key=f"{case.id}:{identity.id}:{party_role}",
+        kind="CREATE",
+        description=f"ضمُّ طرفٍ بدورِ '{party_role}' إلى القضيّةِ '{case.reference}'",
+        mutate=_insert,
+    )
+    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)
+    return crossed_value(
+        guarded,
+        replay=lambda: session.execute(
+            select(CasePartyModel).where(
+                CasePartyModel.case_id == case.id,
+                CasePartyModel.identity_id == identity.id,
+                CasePartyModel.party_role == party_role,
+            )
+        ).scalar_one_or_none(),
+        what=f"ضمَّ الطرفِ إلى القضيّةِ '{case.reference}'",
+    )
 
 
 def add_claim(
@@ -441,9 +677,32 @@ def add_claim(
         filed_by=filed_by,
         tenant_id=tenant_id,
     )
-    session.add(row)
-    session.flush()
-    return row
+
+    def _insert(created: list[tuple[Any, str]]) -> CaseClaimModel:
+        session.add(row)
+        session.flush()
+        created.append((CaseClaimModel, row.id))
+        return row
+
+    # `admit_claim` (D17-2) · لا مفتاحَ طبيعيًّا: المفتاحُ معرِّفُ الصفِّ نفسُه — حدٌّ معلَنٌ
+    # (D6): لا ذرّيّةَ عبرَ إعادةِ المُنادي، والإعادةُ داخلَ النداءِ الواحدِ وحدَها.
+    plan = _plan_crossing(
+        session,
+        action="admit_claim",
+        court=load_court(session, case.court_id, tenant_id=tenant_id),
+        case_scope=case.jurisdiction,
+        namespace="judiciary.claim.add",
+        key=row.id,
+        kind="CREATE",
+        description=f"قبولُ مطالبةٍ من نوعِ '{claim_type}' في القضيّةِ '{case.reference}'",
+        mutate=_insert,
+    )
+    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)
+    return crossed_value(
+        guarded,
+        replay=lambda: session.get(CaseClaimModel, row.id),
+        what=f"قبولَ المطالبةِ في القضيّةِ '{case.reference}'",
+    )
 
 
 def submit_evidence(
@@ -495,10 +754,10 @@ def submit_evidence(
     return row
 
 
-def set_evidence_status(
+def check_evidence_status(
     session: Session, *, evidence_id: str, status: str, reason: str, tenant_id: str
-) -> tuple[CaseEvidenceModel, str]:
-    """اقبل الدليل أو استبعِده أو اسحبه — بأثرٍ مكتوبٍ لا بحذف صفّ."""
+) -> CaseEvidenceModel:
+    """فحوصُ تغييرِ حالةِ الدليلِ — قبلَ الحدِّ وفي الكاتبِ نفسِه (مصدرٌ واحدٌ)."""
     if status not in ("admitted", "excluded", "withdrawn"):
         raise EvidenceError(f"حالةُ دليلٍ غير مسموحة '{status}'")
     if not reason.strip():
@@ -506,6 +765,16 @@ def set_evidence_status(
     row = session.get(CaseEvidenceModel, evidence_id)
     if row is None or row.tenant_id != tenant_id:
         raise EvidenceError(f"لا دليل بالمعرّف '{evidence_id}' في مستأجر '{tenant_id}'")
+    return row
+
+
+def set_evidence_status(
+    session: Session, *, evidence_id: str, status: str, reason: str, tenant_id: str
+) -> tuple[CaseEvidenceModel, str]:
+    """اقبل الدليل أو استبعِده أو اسحبه — بأثرٍ مكتوبٍ لا بحذف صفّ."""
+    row = check_evidence_status(
+        session, evidence_id=evidence_id, status=status, reason=reason, tenant_id=tenant_id
+    )
     previous = row.status
     row.status = status
     row.status_reason = reason
@@ -513,25 +782,50 @@ def set_evidence_status(
     return row, previous
 
 
-def record_proceeding(
+def _check_proceeding(
     session: Session,
     *,
     case_id: str,
     proceeding_type: str,
-    actor_principal: str,
     actor_identity_id: str,
     summary: str,
     tenant_id: str,
-    record: dict[str, Any] | None = None,
-) -> CaseProceedingModel:
-    """قيِّد إجراءً بترتيبٍ مفروضٍ في القاعدة — بديلُ النصّ الحرّ."""
+) -> LegalCaseModel:
+    """فحوصُ الإجراءِ كلُّها قبلَ الحدِّ — مصدرٌ واحدٌ للكاتبِ الخاصِّ وللعمليّةِ العامّةِ."""
     if proceeding_type not in PROCEEDING_TYPES:
         raise JudiciaryError(f"نوعُ إجراءٍ غير معروف '{proceeding_type}'")
     if not summary.strip():
         raise JudiciaryError("خلاصةُ الإجراء لا تكون فارغة")
     case = load_case(session, case_id, tenant_id=tenant_id)
     _load_identity(session, actor_identity_id, tenant_id=tenant_id)
+    return case
+
 
+def _insert_proceeding(
+    session: Session,
+    *,
+    case_id: str,
+    proceeding_type: str,
+    actor_principal: str,
+    actor_identity_id: str,
+    summary: str,
+    tenant_id: str,
+    record: dict[str, Any] | None = None,
+    created: list[tuple[Any, str]] | None = None,
+) -> CaseProceedingModel:
+    """الكاتبُ الخامُ للإجراءِ — **خاصٌّ** يُنادى من داخلِ مُطبِّقاتٍ عابرةٍ فقط (D3).
+
+    يُناديه مُطبِّقُ `record_proceeding` ومُطبِّقاتُ `file_case`/`open_hearing` في الخدمةِ
+    و`rulings.issue_ruling`؛ فلا يقعُ عبورٌ داخلَ عبورٍ (Q-9 لم يُحسَمْ — WI-110).
+    """
+    case = _check_proceeding(
+        session,
+        case_id=case_id,
+        proceeding_type=proceeding_type,
+        actor_identity_id=actor_identity_id,
+        summary=summary,
+        tenant_id=tenant_id,
+    )
     current_max = session.execute(
         select(func.max(CaseProceedingModel.sequence)).where(CaseProceedingModel.case_id == case.id)
     ).scalar()
@@ -549,9 +843,66 @@ def record_proceeding(
     )
     session.add(row)
     session.flush()
+    if created is not None:
+        created.append((CaseProceedingModel, row.id))
     return row
 
 
+def record_proceeding(
+    session: Session,
+    *,
+    case_id: str,
+    proceeding_type: str,
+    actor_principal: str,
+    actor_identity_id: str,
+    summary: str,
+    tenant_id: str,
+    record: dict[str, Any] | None = None,
+) -> CaseProceedingModel:
+    """قيِّد إجراءً بترتيبٍ مفروضٍ في القاعدة — بديلُ النصّ الحرّ — عابرًا الحدَّ (`record_proceeding`)."""
+    case = _check_proceeding(
+        session,
+        case_id=case_id,
+        proceeding_type=proceeding_type,
+        actor_identity_id=actor_identity_id,
+        summary=summary,
+        tenant_id=tenant_id,
+    )
+    # لا مفتاحَ طبيعيًّا قبلَ الحدِّ (التسلسلُ يُحسَبُ داخلَه): مفتاحٌ فريدٌ لكلِّ نداءٍ (D6).
+    key = f"{case.id}:{uuid.uuid4()}"
+
+    def _insert(created: list[tuple[Any, str]]) -> CaseProceedingModel:
+        return _insert_proceeding(
+            session,
+            case_id=case.id,
+            proceeding_type=proceeding_type,
+            actor_principal=actor_principal,
+            actor_identity_id=actor_identity_id,
+            summary=summary,
+            tenant_id=tenant_id,
+            record=record,
+            created=created,
+        )
+
+    plan = _plan_crossing(
+        session,
+        action="record_proceeding",
+        court=load_court(session, case.court_id, tenant_id=tenant_id),
+        case_scope=case.jurisdiction,
+        namespace="judiciary.proceeding.record",
+        key=key,
+        kind="CREATE",
+        description=f"قيدُ إجراءٍ من نوعِ '{proceeding_type}' في القضيّةِ '{case.reference}'",
+        mutate=_insert,
+    )
+    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)
+    return crossed_value(
+        guarded,
+        replay=lambda: None,
+        what=f"قيدَ الإجراءِ في القضيّةِ '{case.reference}'",
+    )
+
+
 def list_proceedings(
     session: Session, *, case_id: str, tenant_id: str
 ) -> list[CaseProceedingModel]:
@@ -570,6 +921,8 @@ def list_proceedings(
 __all__ = [
     "ALLOWED_TRANSITIONS",
     "CaseNotFoundError",
+    "Crossing",
+    "JudicialLedgerDivergenceError",
     "CaseTransitionError",
     "EvidenceError",
     "PartyIdentityError",
@@ -579,6 +932,10 @@ __all__ = [
     "assert_transition",
     "assign_case",
     "case_dict",
+    "check_assign",
+    "check_close",
+    "check_evidence_status",
+    "crossed_value",
     "claim_dict",
     "close_case",
     "evidence_dict",
@@ -587,6 +944,7 @@ __all__ = [
     "load_case",
     "open_case",
     "open_hearing",
+    "judicial_request",
     "party_dict",
     "proceeding_dict",
     "record_proceeding",
diff --git a/federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py b/federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py
index 24ba81d6..228579be 100644
--- a/federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py
+++ b/federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py
@@ -47,9 +47,9 @@ from amos_federation.services.executive_core.sovereignty_bridge import (
     operation_key,
 )
 from amos_federation.services.federal_judiciary.docket import (
+    _insert_proceeding,
     advance_case,
     load_case,
-    record_proceeding,
 )
 from amos_federation.services.federal_judiciary.models import (
     RULING_DECISIONS,
@@ -281,7 +281,8 @@ def issue_ruling(
         )
         session.add(row)
         session.flush()
-        proceeding = record_proceeding(
+        # الكاتبُ الخاصُّ لا العمليّةُ العامّةُ العابرةُ (WI-111 · D3): لا عبورَ داخلَ عبورٍ.
+        proceeding = _insert_proceeding(
             session,
             case_id=case.id,
             proceeding_type="RULING",
@@ -358,6 +359,18 @@ def issue_ruling(
     return row, proceeding
 
 
+def check_vacate(session: Session, *, ruling_id: str, reason: str, tenant_id: str) -> RulingModel:
+    """فحوصُ الإلغاءِ — قبلَ الحدِّ وفي الكاتبِ نفسِه (مصدرٌ واحدٌ · WI-111)."""
+    if not reason.strip():
+        raise RulingError("إلغاءُ حكمٍ يلزمه سببٌ مكتوب")
+    row = load_ruling(session, ruling_id, tenant_id=tenant_id)
+    if row.status == "vacated":
+        raise RulingError(f"الحكم '{ruling_id}' مُلغىً أصلًا")
+    if row.status == "enforced":
+        raise RulingError(f"الحكم '{ruling_id}' نُفِّذ — عكسُ أثرٍ تنفيذيّ ليس مبنيًّا في هذه الوحدة")
+    return row
+
+
 def vacate_ruling(
     session: Session, *, ruling_id: str, reason: str, tenant_id: str
 ) -> tuple[RulingModel, str]:
@@ -366,13 +379,7 @@ def vacate_ruling(
     والحكمُ المُنفَّذ (`enforced`) لا يُلغى في هذه الوحدة: إلغاءُ أثرٍ تنفيذيّ جرى
     يحتاج عكسَ حركةٍ أو إبطالَ مهمّة، وذاك مسارٌ **غير مبنيّ** ويُقال ولا يُموَّه.
     """
-    if not reason.strip():
-        raise RulingError("إلغاءُ حكمٍ يلزمه سببٌ مكتوب")
-    row = load_ruling(session, ruling_id, tenant_id=tenant_id)
-    if row.status == "vacated":
-        raise RulingError(f"الحكم '{ruling_id}' مُلغىً أصلًا")
-    if row.status == "enforced":
-        raise RulingError(f"الحكم '{ruling_id}' نُفِّذ — عكسُ أثرٍ تنفيذيّ ليس مبنيًّا في هذه الوحدة")
+    row = check_vacate(session, ruling_id=ruling_id, reason=reason, tenant_id=tenant_id)
     previous = row.status
     row.status = "vacated"
     row.vacated_at = _now()
diff --git a/federal/executive/services/src/amos_federation/services/federal_judiciary/service.py b/federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
index 766aa6ad..279821cd 100644
--- a/federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
+++ b/federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
@@ -49,6 +49,7 @@ AMOS-Federation Federal Judiciary — Service Facade
 
 from __future__ import annotations
 
+import uuid
 from typing import TYPE_CHECKING, Any
 
 from amos_federation.common.database import get_session_factory, init_db
@@ -74,6 +75,7 @@ from amos_federation.services.federal_judiciary.enforcement import EnforcementEr
 from amos_federation.services.federal_judiciary.models import (
     FEDERAL_JUDICIARY_TABLES,
     CaseEvidenceModel,
+    CaseProceedingModel,
     CourtJudgeModel,
     CourtModel,
     LegalCaseModel,
@@ -93,6 +95,25 @@ RULING_TASK_TYPE = "judiciary.ruling.enforce"
 RULING_TASK_DOMAIN = "judiciary"
 
 
+def _replayed_transition(
+    session: Session, case_id: str, tenant_id: str, proceeding_type: str
+) -> tuple[LegalCaseModel, CaseProceedingModel] | None:
+    """الإعادةُ تُقرأُ (D6): القضيّةُ وآخرُ إجراءٍ من النوعِ — وغيابُ الإجراءِ تفرُّقٌ لا نجاح."""
+    case = docket.load_case(session, case_id, tenant_id=tenant_id)
+    proceeding = (
+        session.query(CaseProceedingModel)
+        .filter(
+            CaseProceedingModel.case_id == case.id,
+            CaseProceedingModel.proceeding_type == proceeding_type,
+        )
+        .order_by(CaseProceedingModel.sequence.desc())
+        .first()
+    )
+    if proceeding is None:
+        return None
+    return case, proceeding
+
+
 class FederalJudiciary:
     """القضاء الفدرالي: محاكمُ وقضاةٌ وقضايا وأحكامٌ وتنفيذُها — بحدٍّ واحد لكلٍّ."""
 
@@ -254,18 +275,45 @@ class FederalJudiciary:
     ) -> dict[str, Any]:
         """علِّق قاضيًا أو اعزله — وأثرُه أن سلطته القضائية تسقط آليًّا."""
         require_domain_permission(context, "judiciary.judge.status", PERMISSIONS_JUDGE_WRITE)
+        tenant = self._tenant_of(context)
         session = self._session()
         try:
-            row, previous = registry.set_judge_status(
+            # فحوصُ `registry.set_judge_status` قبلَ الحدِّ (WI-111 · D8 · `registry.py` خارجَ
+            # النطاقِ فتُعادُ هنا مُطابِقةً — والكاتبُ يُعيدُها داخلَ المُطبِّقِ بلا تغيير).
+            if status not in ("active", "suspended", "revoked"):
+                raise registry.JudiciaryError(f"حالةُ تقليدٍ غير معروفة '{status}'")
+            if not reason.strip():
+                raise registry.JudiciaryError("تغييرُ حالة تقليدٍ قضائيّ يلزمه سببٌ مكتوب")
+            judge = session.get(CourtJudgeModel, judge_id)
+            if judge is None or judge.tenant_id != tenant:
+                raise registry.JudiciaryError(
+                    f"لا تقليدَ قضاءٍ بالمعرّف '{judge_id}' في مستأجر '{tenant}'"
+                )
+            require_tenant(context, judge.tenant_id)
+            court = registry.load_court(session, judge.court_id, tenant_id=tenant)
+            # `recuse_judge` (D17-2 · ونقطةُ D8-أ المعلَنةُ: الدالّةُ تُعلِّقُ وتعزلُ) · الحالةُ
+            # قد تتكرّرُ (active↔suspended) فالمفتاحُ فريدٌ لكلِّ نداءٍ (D6).
+            plan = docket._plan_crossing(
                 session,
-                judge_id=judge_id,
-                status=status,
-                reason=reason,
-                tenant_id=self._tenant_of(context),
+                action="recuse_judge",
+                court=court,
+                case_scope=court.jurisdiction,
+                namespace="judiciary.judge.status",
+                key=f"{judge.id}:{judge.status}->{status}:{uuid.uuid4()}",
+                kind="WRITE",
+                description=f"تغييرُ حالةِ تقليدِ القاضي إلى '{status}' في المحكمةِ '{court.code}'",
+                mutate=lambda _created: registry.set_judge_status(
+                    session, judge_id=judge.id, status=status, reason=reason, tenant_id=tenant
+                ),
+                snapshots=(judge,),
+            )
+            guarded = rulings._judiciary_authorizer().guard_declared(
+                plan.action, plan.target, **plan.kwargs
+            )
+            row, previous = docket.crossed_value(
+                guarded, replay=lambda: None, what="تغييرَ حالةِ التقليدِ"
             )
-            require_tenant(context, row.tenant_id)
             payload = registry.judge_dict(row)
-            session.commit()
         finally:
             session.close()
         trace = self._record(
@@ -311,8 +359,8 @@ class FederalJudiciary:
                 opened_by_identity_id=identity_id,
                 tenant_id=self._tenant_of(context),
             )
+            # `docket.open_case` يعبرُ الحدَّ ويلتزمُ داخلَه (WI-111 · D3) — الخدمةُ مُنسِّقٌ.
             payload = docket.case_dict(row)
-            session.commit()
         finally:
             session.close()
         trace = self._record(
@@ -338,20 +386,49 @@ class FederalJudiciary:
         session = self._session()
         try:
             identity_id = self._identity_of(session, context)
-            row = docket.file_case(session, case_id=case_id, tenant_id=self._tenant_of(context))
-            require_tenant(context, row.tenant_id)
-            proceeding = docket.record_proceeding(
+            tenant = self._tenant_of(context)
+            case = docket.load_case(session, case_id, tenant_id=tenant)
+            require_tenant(context, case.tenant_id)
+            docket.assert_transition(case.status, "filed")
+            summary = f"قيدُ القضية '{case.reference}' رسميًّا"
+
+            def _mutate(created: list[Any]) -> tuple[Any, Any]:
+                moved = docket.file_case(session, case_id=case.id, tenant_id=tenant)
+                proceeding = docket._insert_proceeding(
+                    session,
+                    case_id=case.id,
+                    proceeding_type="FILING",
+                    actor_principal=context.principal_id,
+                    actor_identity_id=identity_id,
+                    summary=summary,
+                    tenant_id=tenant,
+                    created=created,
+                )
+                return moved, proceeding
+
+            # `refer_case` (D17-2) · الخريطةُ لا دوائرَ فيها: (القضيّةُ · السابقةُ→اللاحقةُ) فريدٌ (D6).
+            plan = docket._plan_crossing(
                 session,
-                case_id=row.id,
-                proceeding_type="FILING",
-                actor_principal=context.principal_id,
-                actor_identity_id=identity_id,
-                summary=f"قيدُ القضية '{row.reference}' رسميًّا",
-                tenant_id=self._tenant_of(context),
+                action="refer_case",
+                court=registry.load_court(session, case.court_id, tenant_id=tenant),
+                case_scope=case.jurisdiction,
+                namespace="judiciary.case.file",
+                key=f"{case.id}:{case.status}->filed",
+                kind="WRITE",
+                description=f"انتقالُ القضيّةِ '{case.reference}' إلى 'filed' وقيدُ إجراءِ FILING",
+                mutate=_mutate,
+                snapshots=(case,),
+            )
+            guarded = rulings._judiciary_authorizer().guard_declared(
+                plan.action, plan.target, **plan.kwargs
+            )
+            row, proceeding = docket.crossed_value(
+                guarded,
+                replay=lambda: _replayed_transition(session, case.id, tenant, "FILING"),
+                what=f"انتقالَ القضيّةِ '{case.reference}' إلى 'filed'",
             )
             payload = docket.case_dict(row)
             proceeding_payload = docket.proceeding_dict(proceeding)
-            session.commit()
         finally:
             session.close()
         self._publish_proceeding(context, proceeding_payload)
@@ -362,14 +439,37 @@ class FederalJudiciary:
     ) -> dict[str, Any]:
         """`filed → assigned` بقاضٍ نشطٍ في محكمة القضية بالذات."""
         require_domain_permission(context, "judiciary.case.assign", PERMISSIONS_DOCKET_WRITE)
+        tenant = self._tenant_of(context)
         session = self._session()
         try:
-            row = docket.assign_case(
-                session, case_id=case_id, judge_id=judge_id, tenant_id=self._tenant_of(context)
+            case, judge = docket.check_assign(
+                session, case_id=case_id, judge_id=judge_id, tenant_id=tenant
+            )
+            require_tenant(context, case.tenant_id)
+            # `assign_case` (D17-2 · جديدٌ في المعجمَينِ) · (القضيّةُ · filed→assigned) فريدٌ (D6).
+            plan = docket._plan_crossing(
+                session,
+                action="assign_case",
+                court=registry.load_court(session, case.court_id, tenant_id=tenant),
+                case_scope=case.jurisdiction,
+                namespace="judiciary.case.assign",
+                key=f"{case.id}:{case.status}->assigned",
+                kind="WRITE",
+                description=f"إسنادُ القضيّةِ '{case.reference}' إلى قاضٍ في محكمتِها",
+                mutate=lambda _created: docket.assign_case(
+                    session, case_id=case.id, judge_id=judge.id, tenant_id=tenant
+                ),
+                snapshots=(case,),
+            )
+            guarded = rulings._judiciary_authorizer().guard_declared(
+                plan.action, plan.target, **plan.kwargs
+            )
+            row = docket.crossed_value(
+                guarded,
+                replay=lambda: docket.load_case(session, case.id, tenant_id=tenant),
+                what=f"إسنادَ القضيّةِ '{case.reference}'",
             )
-            require_tenant(context, row.tenant_id)
             payload = docket.case_dict(row)
-            session.commit()
         finally:
             session.close()
         trace = self._record(
@@ -393,20 +493,49 @@ class FederalJudiciary:
         session = self._session()
         try:
             identity_id = self._identity_of(session, context)
-            row = docket.open_hearing(session, case_id=case_id, tenant_id=self._tenant_of(context))
-            require_tenant(context, row.tenant_id)
-            proceeding = docket.record_proceeding(
+            tenant = self._tenant_of(context)
+            case = docket.load_case(session, case_id, tenant_id=tenant)
+            require_tenant(context, case.tenant_id)
+            docket.assert_transition(case.status, "hearing")
+            summary = f"افتتاحُ جلسةٍ في القضية '{case.reference}'"
+
+            def _mutate(created: list[Any]) -> tuple[Any, Any]:
+                moved = docket.open_hearing(session, case_id=case.id, tenant_id=tenant)
+                proceeding = docket._insert_proceeding(
+                    session,
+                    case_id=case.id,
+                    proceeding_type="HEARING",
+                    actor_principal=context.principal_id,
+                    actor_identity_id=identity_id,
+                    summary=summary,
+                    tenant_id=tenant,
+                    created=created,
+                )
+                return moved, proceeding
+
+            # `adjudicate` (D17-2) · الخريطةُ لا دوائرَ فيها: (القضيّةُ · السابقةُ→اللاحقةُ) فريدٌ (D6).
+            plan = docket._plan_crossing(
                 session,
-                case_id=row.id,
-                proceeding_type="HEARING",
-                actor_principal=context.principal_id,
-                actor_identity_id=identity_id,
-                summary=f"افتتاحُ جلسةٍ في القضية '{row.reference}'",
-                tenant_id=self._tenant_of(context),
+                action="adjudicate",
+                court=registry.load_court(session, case.court_id, tenant_id=tenant),
+                case_scope=case.jurisdiction,
+                namespace="judiciary.case.hearing",
+                key=f"{case.id}:{case.status}->hearing",
+                kind="WRITE",
+                description=f"انتقالُ القضيّةِ '{case.reference}' إلى 'hearing' وقيدُ إجراءِ HEARING",
+                mutate=_mutate,
+                snapshots=(case,),
+            )
+            guarded = rulings._judiciary_authorizer().guard_declared(
+                plan.action, plan.target, **plan.kwargs
+            )
+            row, proceeding = docket.crossed_value(
+                guarded,
+                replay=lambda: _replayed_transition(session, case.id, tenant, "HEARING"),
+                what=f"انتقالَ القضيّةِ '{case.reference}' إلى 'hearing'",
             )
             payload = docket.case_dict(row)
             proceeding_payload = docket.proceeding_dict(proceeding)
-            session.commit()
         finally:
             session.close()
         self._publish_proceeding(context, proceeding_payload)
@@ -417,14 +546,39 @@ class FederalJudiciary:
     ) -> dict[str, Any]:
         """`decided|enforcement → closed` بسببٍ مكتوب."""
         require_domain_permission(context, "judiciary.case.close", PERMISSIONS_DOCKET_WRITE)
+        tenant = self._tenant_of(context)
         session = self._session()
         try:
-            row, previous = docket.close_case(
-                session, case_id=case_id, reason=reason, tenant_id=self._tenant_of(context)
+            case = docket.check_close(session, case_id=case_id, reason=reason, tenant_id=tenant)
+            require_tenant(context, case.tenant_id)
+            previous_status = case.status
+            # `register_judgment` (D17-2) · (القضيّةُ · السابقةُ→closed) فريدٌ — الإغلاقُ نهائيٌّ (D6).
+            plan = docket._plan_crossing(
+                session,
+                action="register_judgment",
+                court=registry.load_court(session, case.court_id, tenant_id=tenant),
+                case_scope=case.jurisdiction,
+                namespace="judiciary.case.close",
+                key=f"{case.id}:{case.status}->closed",
+                kind="WRITE",
+                description=f"إغلاقُ القضيّةِ '{case.reference}' بسببٍ مكتوبٍ",
+                mutate=lambda _created: docket.close_case(
+                    session, case_id=case.id, reason=reason, tenant_id=tenant
+                ),
+                snapshots=(case,),
+            )
+            guarded = rulings._judiciary_authorizer().guard_declared(
+                plan.action, plan.target, **plan.kwargs
+            )
+            row, previous = docket.crossed_value(
+                guarded,
+                replay=lambda: (
+                    docket.load_case(session, case.id, tenant_id=tenant),
+                    previous_status,
+                ),
+                what=f"إغلاقَ القضيّةِ '{case.reference}'",
             )
-            require_tenant(context, row.tenant_id)
             payload = docket.case_dict(row)
-            session.commit()
         finally:
             session.close()
         trace = self._record(
@@ -474,8 +628,7 @@ class FederalJudiciary:
                 institution_id=institution_id,
                 display_label=display_label,
             )
-            payload = docket.party_dict(row)
-            session.commit()
+            payload = docket.party_dict(row)  # `docket.add_party` يعبرُ ويلتزمُ (WI-111)
         finally:
             session.close()
         return payload
@@ -509,8 +662,7 @@ class FederalJudiciary:
                 legal_basis_ref=legal_basis_ref,
                 amount=amount,
             )
-            payload = docket.claim_dict(row)
-            session.commit()
+            payload = docket.claim_dict(row)  # `docket.add_claim` يعبرُ ويلتزمُ (WI-111)
         finally:
             session.close()
         return payload
@@ -569,18 +721,36 @@ class FederalJudiciary:
     ) -> dict[str, Any]:
         """اقبل الدليل أو استبعِده أو اسحبه — بأثرٍ مكتوبٍ لا بحذف."""
         require_domain_permission(context, "judiciary.evidence.status", PERMISSIONS_DOCKET_WRITE)
+        tenant = self._tenant_of(context)
         session = self._session()
         try:
-            row, previous = docket.set_evidence_status(
+            evidence = docket.check_evidence_status(
+                session, evidence_id=evidence_id, status=status, reason=reason, tenant_id=tenant
+            )
+            require_tenant(context, evidence.tenant_id)
+            case = docket.load_case(session, evidence.case_id, tenant_id=tenant)
+            # `admit_evidence` (D17-2) · الحالةُ قد تتكرّرُ فالمفتاحُ فريدٌ لكلِّ نداءٍ (D6).
+            plan = docket._plan_crossing(
                 session,
-                evidence_id=evidence_id,
-                status=status,
-                reason=reason,
-                tenant_id=self._tenant_of(context),
+                action="admit_evidence",
+                court=registry.load_court(session, case.court_id, tenant_id=tenant),
+                case_scope=case.jurisdiction,
+                namespace="judiciary.evidence.status",
+                key=f"{evidence.id}:{evidence.status}->{status}:{uuid.uuid4()}",
+                kind="WRITE",
+                description=f"تغييرُ حالةِ دليلٍ إلى '{status}' في القضيّةِ '{case.reference}'",
+                mutate=lambda _created: docket.set_evidence_status(
+                    session, evidence_id=evidence.id, status=status, reason=reason, tenant_id=tenant
+                ),
+                snapshots=(evidence,),
+            )
+            guarded = rulings._judiciary_authorizer().guard_declared(
+                plan.action, plan.target, **plan.kwargs
+            )
+            row, previous = docket.crossed_value(
+                guarded, replay=lambda: None, what="تغييرَ حالةِ الدليلِ"
             )
-            require_tenant(context, row.tenant_id)
             payload = docket.evidence_dict(row)
-            session.commit()
         finally:
             session.close()
         return {**payload, "previous_status": previous}
@@ -617,8 +787,7 @@ class FederalJudiciary:
                 tenant_id=self._tenant_of(context),
                 record=record,
             )
-            payload = docket.proceeding_dict(row)
-            session.commit()
+            payload = docket.proceeding_dict(row)  # `docket.record_proceeding` يعبرُ ويلتزمُ (WI-111)
         finally:
             session.close()
         trace = self._publish_proceeding(context, payload)
@@ -709,18 +878,47 @@ class FederalJudiciary:
     ) -> dict[str, Any]:
         """ألغِ حكمًا غير مُنفَّذ بسلطةٍ قضائية في محكمته — تغييرُ حالةٍ لا حذف."""
         require_domain_permission(context, "judiciary.ruling.vacate", PERMISSIONS_RULING_WRITE)
+        tenant = self._tenant_of(context)
         session = self._session()
         try:
-            ruling = rulings.load_ruling(session, ruling_id, tenant_id=self._tenant_of(context))
+            ruling = rulings.load_ruling(session, ruling_id, tenant_id=tenant)
             require_tenant(context, ruling.tenant_id)
-            require_judicial_authority(
+            authority = require_judicial_authority(
                 session, context, court_id=ruling.court_id, case_id=ruling.case_id
             )
-            row, previous = rulings.vacate_ruling(
-                session, ruling_id=ruling_id, reason=reason, tenant_id=self._tenant_of(context)
+            rulings.check_vacate(session, ruling_id=ruling.id, reason=reason, tenant_id=tenant)
+            case = docket.load_case(session, ruling.case_id, tenant_id=tenant)
+            # `vacate_ruling` (J2 · D17-2) · المنصبُ مُثبَتٌ هنا فنطاقُ الفاعلِ منه (D4 كـJ1) ·
+            # الإلغاءُ مرّةً واحدةً للحكمِ (D6).
+            plan = docket._plan_crossing(
+                session,
+                action="vacate_ruling",
+                court=registry.load_court(session, ruling.court_id, tenant_id=tenant),
+                case_scope=case.jurisdiction,
+                namespace="judiciary.ruling.vacate",
+                key=f"{ruling.id}:{ruling.status}->vacated",
+                kind="WRITE",
+                description=f"إلغاءُ حكمِ المرحلةِ '{ruling.stage}' في القضيّةِ '{case.reference}'",
+                mutate=lambda _created: rulings.vacate_ruling(
+                    session, ruling_id=ruling.id, reason=reason, tenant_id=tenant
+                ),
+                snapshots=(ruling,),
+                actor_scope=authority.position_scope or "",
+                institution_id=authority.institution_id,
+            )
+            previous_status = ruling.status
+            guarded = rulings._judiciary_authorizer().guard_declared(
+                plan.action, plan.target, **plan.kwargs
+            )
+            row, previous = docket.crossed_value(
+                guarded,
+                replay=lambda: (
+                    rulings.load_ruling(session, ruling.id, tenant_id=tenant),
+                    previous_status,
+                ),
+                what="إلغاءَ الحكمِ",
             )
             payload = rulings.ruling_dict(row)
-            session.commit()
         finally:
             session.close()
         return {**payload, "previous_status": previous}
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff 83994514d831d184c5fc1855ef5edc0bf777b0ad 4247c68fea97c3bdba583f590ed5f3bda679d12e -- federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py federal/executive/services/tests/test_r7d_federal_judiciary.py
EXIT: 0
BYTES: 3081
SHA256: d7538d9ff8c722db0ed0c7a61f2e8faea9d00660d947206b9fd73df16992e05f
NO_EOL: 0
--- OUTPUT ---
diff --git a/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py b/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
index c1092a4e..0376a945 100644
--- a/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
+++ b/federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
@@ -378,6 +378,17 @@ def _prepared_case(
 # ── T1 · ALLOW للقضائيّ — العبورُ والصفوفُ الثلاثةُ ──────────────────────────
 
 
+
+def _ruling_results(authorizer: Any) -> list[Any]:
+    """عبوراتُ `issue_ruling` وحدَها منَ المُصرِّحِ المشتركِ.
+
+    مُضافٌ في WI-111 (J2+J3 · W-640): المُصرِّحُ نفسُه صارَ يعبرُ به تجهيزُ الفحصِ أيضًا
+    (فتحُ القضيّةِ وقيدُها وإسنادُها وإلغاءُ الحكمِ) — فعدُّ `authorizer.results` كلِّها
+    لم يعُدْ يقيسُ `issue_ruling`. والتصفيةُ بالفعلِ تُبقي قصدَ الفحصِ كما هو: عددُ
+    عبوراتِ إصدارِ الحكمِ بعينِه (لا تخفيفَ — والقيدُ الثاني في T5 على سجلِّ البوابةِ باقٍ).
+    """
+    return [r for r in authorizer.results if r.evidence.as_dict()["action"] == "issue_ruling"]
+
 def test_wi105_t1_issue_ruling_crosses_boundary_as_judicial(
     registry: StateRegistry,
     national: NationalRegistry,
@@ -399,8 +410,8 @@ def test_wi105_t1_issue_ruling_crosses_boundary_as_judicial(
     assert payload["status"] == "issued"
 
     # عبورٌ واحدٌ بدليلِهِ الحرفيِّ: الفعلُ والقرارُ والهدفُ بجيلِهِ.
-    assert len(authorizer.results) == 1
-    evidence = authorizer.results[0].evidence.as_dict()
+    assert len(_ruling_results(authorizer)) == 1
+    evidence = _ruling_results(authorizer)[0].evidence.as_dict()
     assert evidence["action"] == "issue_ruling"
     assert evidence["decision"] == "ALLOW"
     assert evidence["target"] == f"judiciary/rulings/{case_id}/FIRST_INSTANCE/g0"
@@ -583,8 +594,8 @@ def test_wi105_t4_replacement_after_vacation_uses_new_generation(
     finally:
         session.close()
 
-    assert len(authorizer.results) == 2
-    targets = [r.evidence.as_dict()["target"] for r in authorizer.results]
+    assert len(_ruling_results(authorizer)) == 2
+    targets = [r.evidence.as_dict()["target"] for r in _ruling_results(authorizer)]
     assert targets[0] == f"judiciary/rulings/{case_id}/FIRST_INSTANCE/g0"
     assert targets[1] == f"judiciary/rulings/{case_id}/FIRST_INSTANCE/g1"
 
@@ -620,7 +631,7 @@ def test_wi105_t5_duplicate_rejected_before_boundary(
         )
 
     # المكرَّرُ لم يعبُرِ الحدَّ أصلًا: لا عبورَ جديدَ ولا قرارَ في البوابةِ.
-    assert len(authorizer.results) == 1
+    assert len(_ruling_results(authorizer)) == 1
     assert len(authorizer.gateway.records) == decisions_before
 
 
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat federal/executive/services/tests/test_wi111_judiciary_docket_sovereign.py
EXIT: 0
BYTES: 23411
SHA256: 5b3f64e2b147036b03c2de47519d0cac1a4c24fd6f753e9de1c8bd027ceaa292
NO_EOL: 0
--- OUTPUT ---
"""
الهدف: إثباتُ الدفعةِ J2+J3 (WI-111) — الأسطحُ القضائيّةُ الخمسةَ عشرَ المحسومةُ تعبرُ
       الحدَّ بفاعلِ الوحدةِ القضائيِّ وبأفعالِ D17-2، ولا عبورَ داخلَ عبورٍ.
النطاق: `federal_judiciary/{service,docket,rulings}.py` ومعجمُ المُحرِّكِ وجدارُ الاختصاصِ —
        على ملحقِ التصميمِ `docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md` (T1–T8 · M1–M5).
المالك: federal/executive/services/tests
تاريخ الإنشاء: 2026-10-23
تاريخ آخر تعديل: 2026-10-23

لماذا
-----
D17-2 (خيارُ 1): «تُنفَّذ الأسطح الأخرى بالأفعال المعتمدة في D17-2». فكلُّ فعلٍ منَ العشرةِ
يُثبَتُ هنا حصرًا قضائيًّا في المُحرِّكِ (T1)، ويُثبَتُ عبورُه على المسارِ الإنتاجيِّ نفسِه
بالفعلِ المعتمدِ (T2) وبأثرٍ مُعلَنٍ ومُعوِّضٍ (T3)، ورفضُه لفاعلٍ تنفيذيٍّ منعًا حقيقيًّا (T2b)،
والإعادةُ بلا صفٍّ تفرُّقًا (T4)، والمُعوِّضُ استعادةً حقيقيّةً (T5)، والجردُ بلا دَينٍ في
الأسطحِ الخمسةَ عشرَ (T6)، و`issue_ruling` بلا عبورٍ متداخلٍ (T7).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

import tests.test_wi105_issue_ruling_sovereign as j1
from amos_federation.services.federal_judiciary import FederalJudiciary
from amos_federation.services.federal_judiciary import docket as docket_module
from amos_federation.services.federal_judiciary import rulings as rulings_module
from amos_federation.services.federal_judiciary.models import (
    CaseClaimModel,
    CaseEvidenceModel,
    CasePartyModel,
    CaseProceedingModel,
    CourtJudgeModel,
    LegalCaseModel,
)

if TYPE_CHECKING:
    from amos_federation.common.principal import AuthorizationContext
    from amos_federation.services.national_registry.service import NationalRegistry
    from amos_federation.services.state_registry.service import StateRegistry

# التجهيزاتُ نفسُها منَ J1 (لا نسخَ): السجلّاتُ والتاجُ.
registry = j1.registry
national = j1.national
judiciary = j1.judiciary
crown = j1.crown


@pytest.fixture(autouse=True)
def _fresh_state() -> None:
    """قاعدةٌ نظيفةٌ قبلَ كلِّ فحصٍ: أبناءُ القضيّةِ أوّلًا (مطالبةٌ · دليلٌ · طرفٌ) ثمَّ ترتيبُ J1.

    تجهيزُ J1 لا يحذفُ المطالباتِ والأدلّةَ والأطرافَ لأنَّ فحوصَه لا تُنشئُها؛ وهذه
    الفحوصُ تُنشئُها، فقيدُ المفتاحِ الأجنبيِّ يمنعُ حذفَ القضيّةِ قبلَها. والباقي حرفيًّا
    ترتيبُ `j1._fresh_state` بأسمائه في وحدتِه (لا نسخَ للنماذج).
    """
    j1.init_db()
    session = j1.get_session_factory()()
    try:
        session.query(CaseClaimModel).delete()
        session.query(CaseEvidenceModel).delete()
        session.query(CasePartyModel).delete()
        for model in (
            j1.RulingModel,
            CaseProceedingModel,
            LegalCaseModel,
            CourtJudgeModel,
            j1.CourtModel,
            j1.AuthorityGrantModel,
            j1.DecisionProvenanceModel,
            j1.LedgerEntryModel,
            j1.TransactionModel,
            j1.AllocationModel,
            j1.BudgetModel,
            j1.TreasuryAccountModel,
            j1.TreasuryModel,
            j1.OfficialPositionModel,
            j1.PositionModel,
            j1.IdentityAgentModel,
            j1.IdentityPrincipalModel,
            j1.IdentityModel,
        ):
            session.query(model).delete()
        j1.purge_tasks(session)
        j1.purge_agents(session)
        session.commit()
    finally:
        session.close()
    j1.reset_executive_core()
    j1.reset_state_registry()
    j1.reset_government_services()
    j1.reset_state_treasury()
    j1.reset_national_registry()
    j1.reset_federal_judiciary()
    rulings_module.reset_judiciary_authorizer()


#: الأفعالُ العشرةُ المضافةُ إلى معجمِ المُحرِّكِ (D17-2 · ملحقُ التصميمِ D2).
NEW_ENGINE_VERBS = (
    "refer_case",
    "admit_case",
    "vacate_ruling",
    "admit_evidence",
    "recuse_judge",
    "register_judgment",
    "assign_case",
    "record_proceeding",
    "join_party",
    "admit_claim",
)

#: الأسطحُ الخمسةَ عشرَ المحسومةُ (قيسَت عندَ 6f3fba2 · W-636).
SETTLED_SURFACES = {
    ("service.py", "vacate_ruling"),
    ("service.py", "file_case"),
    ("service.py", "open_case"),
    ("docket.py", "open_case"),
    ("service.py", "set_evidence_status"),
    ("service.py", "set_judge_status"),
    ("service.py", "close_case"),
    ("service.py", "assign_case"),
    ("service.py", "open_hearing"),
    ("service.py", "record_proceeding"),
    ("docket.py", "record_proceeding"),
    ("service.py", "add_party"),
    ("docket.py", "add_party"),
    ("service.py", "add_claim"),
    ("docket.py", "add_claim"),
}


class SpyingAuthorizer(rulings_module.ConstitutionalAuthorizer):
    """يسجّلُ كلَّ نداءٍ محروسٍ بمعاملاتِه وعمقِ تداخلِه — قياسٌ لا قرار."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.calls: list[dict[str, Any]] = []
        self.depth = 0
        self.max_depth = 0

    def guard_declared(self, action: str, target: str, **kwargs: Any) -> Any:
        self.depth += 1
        self.max_depth = max(self.max_depth, self.depth)
        try:
            guarded = super().guard_declared(action, target, **kwargs)
        finally:
            self.depth -= 1
        self.calls.append(
            {"action": action, "target": target, "kwargs": kwargs, "guarded": guarded}
        )
        return guarded

    def actions(self) -> list[str]:
        return [c["action"] for c in self.calls]


def _install_spy() -> SpyingAuthorizer:
    spy = SpyingAuthorizer(actor=rulings_module.JUDICIARY_ACTOR)
    rulings_module._DEFAULT_JUDICIARY_AUTHORIZER = spy
    return spy


def _world(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    username: str,
) -> tuple[Any, AuthorizationContext, AuthorizationContext, dict[str, Any]]:
    judge_ctx = j1._context("official", username=username)
    bench = j1._bench(registry, national, judiciary, crown, judge_ctx)
    filer = j1._context("official", username=f"filer-{username}")
    identity = j1._party_identity(national, crown, filer)
    return bench, judge_ctx, filer, identity


def _open(judiciary: FederalJudiciary, filer: AuthorizationContext, bench: Any) -> dict[str, Any]:
    return judiciary.open_case(
        context=filer,
        court_id=bench.court["id"],
        case_type="CIVIL",
        subject="نزاعٌ لفحصِ WI-111",
        reference=j1._code("W111"),
    )


# ── T1 · المعجمُ: الأفعالُ العشرةُ حصرٌ قضائيٌّ ─────────────────────────────────


@pytest.mark.parametrize("verb", NEW_ENGINE_VERBS)
def test_wi111_t1_engine_denies_non_judicial_and_allows_judicial(verb: str) -> None:
    from core.constitutional_engine.engine import ConstitutionalEngine
    from core.constitutional_engine.model import ActionRequest, Branch

    engine = ConstitutionalEngine()

    def decide(actor: str) -> tuple[str, list[str]]:
        verdict = engine.evaluate(
            ActionRequest(actor=Branch[actor], action=verb, target="wi111/probe")
        )
        decision = getattr(verdict, "decision", verdict)
        rules = [str(getattr(v, "rule_id", v)) for v in getattr(verdict, "violations", []) or []]
        return str(getattr(decision, "name", decision)), rules

    for actor in ("EXECUTIVE", "LEGISLATIVE"):
        decision, rules = decide(actor)
        assert decision == "DENY", (verb, actor, decision)
        assert "R-003-1" in rules, (verb, actor, rules)
    assert decide("JUDICIAL")[0] == "ALLOW"


def test_wi111_t1b_wall_knows_the_four_new_verbs_and_not_the_deferred() -> None:
    from core.constitutional_engine.rules import JUDICIAL_ACTIONS as ENGINE_VERBS
    from core.sovereignty.jurisdiction import JUDICIAL_ACTIONS as WALL_VERBS

    for verb in ("assign_case", "record_proceeding", "join_party", "admit_claim"):
        assert verb in WALL_VERBS
    for verb in NEW_ENGINE_VERBS:
        assert verb in ENGINE_VERBS
    # الأفعالُ الأربعةُ المؤجَّلةُ (D17-2 · D21-أ بند 9) غائبةٌ عمدًا منَ المعجمِ.
    for verb in ("establish_court", "set_court_status", "appoint_judge", "submit_evidence"):
        assert verb not in ENGINE_VERBS


# ── T2 · المسارُ الإنتاجيُّ: كلُّ سطحٍ يعبرُ بفعلِه المعتمدِ ─────────────────────


def _full_flow(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    username: str,
) -> dict[str, Any]:
    bench, judge_ctx, filer, identity = _world(registry, national, judiciary, crown, username)
    spy = _install_spy()
    case = _open(judiciary, filer, bench)
    party = judiciary.add_party(
        context=filer, case_id=case["id"], party_role="PLAINTIFF", identity_id=identity["id"]
    )
    judiciary.add_claim(
        context=filer,
        case_id=case["id"],
        claimant_party_id=party["id"],
        claim_type="DECLARATORY",
        statement="مطالبةُ فحصِ WI-111",
    )
    judiciary.record_proceeding(
        context=filer, case_id=case["id"], proceeding_type="MOTION", summary="طلبٌ إجرائيٌّ"
    )
    judiciary.file_case(context=filer, case_id=case["id"])
    judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
    judiciary.open_hearing(context=judge_ctx, case_id=case["id"])
    evidence = judiciary.submit_evidence(
        context=filer, case_id=case["id"], evidence_type="DOCUMENT", source="فحصُ WI-111"
    )
    judiciary.set_evidence_status(
        context=judge_ctx, evidence_id=evidence["id"], status="admitted", reason="مقبولٌ للفحص"
    )
    ruling = judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case["id"],
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ فحصِ WI-111",
    )
    judiciary.vacate_ruling(context=judge_ctx, ruling_id=ruling["id"], reason="إلغاءٌ للفحص")
    judiciary.close_case(context=judge_ctx, case_id=case["id"], reason="إغلاقٌ للفحص")
    judiciary.set_judge_status(
        context=crown, judge_id=bench.judge["id"], status="suspended", reason="تعليقٌ للفحص"
    )
    return {"spy": spy, "case": case, "bench": bench, "evidence": evidence}


def test_wi111_t2_production_path_crosses_with_d17_2_verbs(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    flow = _full_flow(registry, national, judiciary, crown, "t2")
    spy: SpyingAuthorizer = flow["spy"]
    assert spy.actions() == [
        "admit_case",
        "join_party",
        "admit_claim",
        "record_proceeding",
        "refer_case",
        "assign_case",
        "adjudicate",
        "admit_evidence",
        "issue_ruling",
        "vacate_ruling",
        "register_judgment",
        "recuse_judge",
    ]
    for call in spy.calls:
        evidence = call["guarded"].evidence.as_dict()
        assert evidence["decision"] == "ALLOW", call["action"]
        assert evidence["action"] == call["action"]
    records = [r for r in spy.gateway.records if r.action in set(spy.actions())]
    assert records and all(r.actor == "judicial" and r.decision == "ALLOW" for r in records)


@pytest.mark.parametrize("surface", ["open_case", "assign_case", "add_party"])
def test_wi111_t2b_executive_actor_is_denied_and_nothing_is_written(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
    surface: str,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    bench, _judge_ctx, filer, identity = _world(
        registry, national, judiciary, crown, f"t2b{surface}"
    )
    case = _open(judiciary, filer, bench)
    judiciary.file_case(context=filer, case_id=case["id"])
    monkeypatch.setattr(rulings_module, "JUDICIARY_ACTOR", "EXECUTIVE")
    rulings_module.reset_judiciary_authorizer()

    session = j1._session()
    try:
        cases_before = session.query(LegalCaseModel).count()
        parties_before = session.query(CasePartyModel).count()
    finally:
        session.close()

    with pytest.raises(SovereigntyViolation):
        if surface == "open_case":
            _open(judiciary, filer, bench)
        elif surface == "assign_case":
            judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
        else:
            judiciary.add_party(
                context=filer,
                case_id=case["id"],
                party_role="PLAINTIFF",
                identity_id=identity["id"],
            )

    session = j1._session()
    try:
        assert session.query(LegalCaseModel).count() == cases_before
        assert session.query(CasePartyModel).count() == parties_before
        row = session.get(LegalCaseModel, case["id"])
        assert row is not None and row.status == "filed" and row.assigned_judge_id is None
    finally:
        session.close()


# ── T3 · الأثرُ المُعلَنُ ونوعُه ومُعوِّضُه وطلبُ الاختصاصِ ─────────────────────────


def test_wi111_t3_each_crossing_declares_effect_compensator_and_jurisdiction(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    flow = _full_flow(registry, national, judiciary, crown, "t3")
    spy: SpyingAuthorizer = flow["spy"]
    creates = {"admit_case", "join_party", "admit_claim", "record_proceeding", "issue_ruling"}
    for call in spy.calls:
        kwargs = call["kwargs"]
        (effect,) = kwargs["declared_effects"]
        expected = "CREATE" if call["action"] in creates else "WRITE"
        assert effect.kind.name == expected, call["action"]
        assert len(kwargs["compensators"]) == 1, call["action"]
        request = kwargs["judicial_action"]
        assert request.action == call["action"]
        assert request.court_scope == flow["bench"].court["jurisdiction"]
        if call["action"] != "issue_ruling":  # J1 يجعلُ هدفَ طلبِه القضيّةَ (فحوصُه في wi105)
            assert request.target == call["target"]
        assert request.is_royal_decree_target is False


# ── T4 · الإعادةُ بلا صفٍّ تفرُّقٌ لا نجاحٌ ──────────────────────────────────────


def test_wi111_t4_replay_with_missing_case_raises_divergence(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    bench, _judge_ctx, filer, _identity = _world(registry, national, judiciary, crown, "t4")
    reference = j1._code("W111R")
    first = judiciary.open_case(
        context=filer,
        court_id=bench.court["id"],
        case_type="CIVIL",
        subject="فحص",
        reference=reference,
    )
    session = j1._session()
    try:
        row = session.get(LegalCaseModel, first["id"])
        assert row is not None
        session.delete(row)
        session.commit()
    finally:
        session.close()
    with pytest.raises(docket_module.JudicialLedgerDivergenceError):
        judiciary.open_case(
            context=filer,
            court_id=bench.court["id"],
            case_type="CIVIL",
            subject="فحص",
            reference=reference,
        )


# ── T5 · المُعوِّضُ على المسارِ الإنتاجيِّ: فشلُ التثبيتِ ⇒ استعادةٌ حقيقيّةٌ ──────────


def test_wi111_t5_failed_settle_restores_assignment_and_closure(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired

    bench, judge_ctx, filer, _identity = _world(registry, national, judiciary, crown, "t5")
    case = _open(judiciary, filer, bench)
    judiciary.file_case(context=filer, case_id=case["id"])
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger

    original = j1._drop_settle(monkeypatch, ledger, "WI-111 T5 assign")
    with pytest.raises(CompensationRequired) as caught:
        judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    assert caught.value.outcome.state_is_clean is True
    session = j1._session()
    try:
        row = session.get(LegalCaseModel, case["id"])
        assert row is not None and row.status == "filed" and row.assigned_judge_id is None
    finally:
        session.close()

    j1._next_second()
    judiciary.assign_case(context=crown, case_id=case["id"], judge_id=bench.judge["id"])
    judiciary.open_hearing(context=judge_ctx, case_id=case["id"])
    judiciary.issue_ruling(
        context=judge_ctx,
        case_id=case["id"],
        stage="FIRST_INSTANCE",
        decision="GRANTED",
        disposition="قضاءُ فحصِ WI-111 T5",
    )

    original = j1._drop_settle(monkeypatch, ledger, "WI-111 T5 close")
    with pytest.raises(CompensationRequired):
        judiciary.close_case(context=judge_ctx, case_id=case["id"], reason="إغلاقٌ للفحص")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    session = j1._session()
    try:
        row = session.get(LegalCaseModel, case["id"])
        assert row is not None and row.status == "decided" and row.closed_at is None
    finally:
        session.close()


def test_wi111_t5b_failed_settle_removes_inserted_party_and_proceeding(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired

    bench, _judge_ctx, filer, identity = _world(registry, national, judiciary, crown, "t5b")
    case = _open(judiciary, filer, bench)
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger

    original = j1._drop_settle(monkeypatch, ledger, "WI-111 T5b party")
    with pytest.raises(CompensationRequired):
        judiciary.add_party(
            context=filer, case_id=case["id"], party_role="PLAINTIFF", identity_id=identity["id"]
        )
    with pytest.raises(CompensationRequired):
        judiciary.file_case(context=filer, case_id=case["id"])
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    session = j1._session()
    try:
        assert (
            session.query(CasePartyModel).filter(CasePartyModel.case_id == case["id"]).count() == 0
        )
        assert (
            session.query(CaseProceedingModel)
            .filter(CaseProceedingModel.case_id == case["id"])
            .count()
            == 0
        )
        row = session.get(LegalCaseModel, case["id"])
        assert row is not None and row.status == "opened"
    finally:
        session.close()


# ── T6 · الجردُ: الأسطحُ الخمسةَ عشرَ بلا دَينٍ ──────────────────────────────────


def _inventory() -> Any:
    root = next(
        p
        for p in Path(__file__).resolve().parents
        if (p / "tools" / "audit" / "sovereign_write_inventory.py").is_file()
    )
    tool = root / "tools" / "audit" / "sovereign_write_inventory.py"
    spec = importlib.util.spec_from_file_location("_wi111_inventory", tool)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.collect(root)


def test_wi111_t6_inventory_has_no_debt_on_settled_surfaces() -> None:
    sites = [s for s in _inventory() if "/federal_judiciary/" in s.path and s.public]
    debt = {(Path(s.path).name, s.function) for s in sites if not s.guarded and not s.closed_legacy}
    assert not (debt & SETTLED_SURFACES), sorted(debt & SETTLED_SURFACES)
    guarded = {(Path(s.path).name, s.function) for s in sites if s.guarded}
    for surface in (
        ("docket.py", "open_case"),
        ("docket.py", "add_party"),
        ("docket.py", "add_claim"),
        ("docket.py", "record_proceeding"),
    ):
        assert surface in guarded, surface
    # والمؤجَّلُ وJ4 دَينٌ باقٍ كما هو (لا مساسَ — D21-أ بند 9).
    for surface in (("service.py", "submit_evidence"), ("service.py", "appoint_judge")):
        assert surface in debt, surface


# ── T7 · لا عبورَ داخلَ عبورٍ ────────────────────────────────────────────────────


def test_wi111_t7_no_nested_crossing_on_any_surface(
    registry: StateRegistry,
    national: NationalRegistry,
    judiciary: FederalJudiciary,
    crown: AuthorizationContext,
) -> None:
    flow = _full_flow(registry, national, judiciary, crown, "t7")
    spy: SpyingAuthorizer = flow["spy"]
    assert spy.max_depth == 1
    session = j1._session()
    try:
        # إجراءُ الحكمِ قُيِّدَ بالكاتبِ الخاصِّ داخلَ مُطبِّقِ `issue_ruling` (لا `record_proceeding` عابرًا).
        assert (
            session.query(CaseProceedingModel)
            .filter(
                CaseProceedingModel.case_id == flow["case"]["id"],
                CaseProceedingModel.proceeding_type == "RULING",
            )
            .count()
            == 1
        )
        assert spy.actions().count("record_proceeding") == 1
        assert (
            session.query(CaseClaimModel)
            .filter(CaseClaimModel.case_id == flow["case"]["id"])
            .count()
            == 1
        )
        evidence = session.get(CaseEvidenceModel, flow["evidence"]["id"])
        assert evidence is not None and evidence.status == "admitted"
        judge = session.get(CourtJudgeModel, flow["bench"].judge["id"])
        assert judge is not None and judge.status == "suspended"
    finally:
        session.close()
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3221
SHA256: 45204a1ce3bf8c187a5cabc3d4c0e40243e36778eaa3d8810b6097ebe52906ed
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 239
  عمليّاتٌ عامّةٌ مُغيِّرة   : 190
  منها تعبرُ الحدَّ        : 46
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 142
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          160 /  46 /  113
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
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
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi111_judiciary_docket_sovereign.py -q
EXIT: 0
BYTES: 632
SHA256: e34a5a1acadd315ec6a85f9accf14f1e04f60705a8e4482e5a9852d3aa62df26
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 21 items

tests/test_wi111_judiciary_docket_sovereign.py .....................     [100%]

============================== 21 passed in 5.82s ==============================
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi105_issue_ruling_sovereign.py tests/test_r7d_federal_judiciary.py -q
EXIT: 0
BYTES: 712
SHA256: 7e653a14372d1ff5d055e5d82c3a088001da48e5ef22aff995d46fb6a02e6205
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 37 items

tests/test_wi105_issue_ruling_sovereign.py ..........                    [ 27%]
tests/test_r7d_federal_judiciary.py ...........................          [100%]

============================= 37 passed in 11.35s ==============================
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests -q
EXIT: 0
BYTES: 9074
SHA256: 629172d57981de7265658dad4d75b3af833e7cf8317acaf8b1a300cff74c5d8f
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1576 items

tests/test_1n_boundary_integration.py ..........                         [  0%]
tests/test_2a_precedent_correction.py ...........                        [  1%]
tests/test_2a_sovereign_runtime_integration.py .............             [  2%]
tests/test_2b_government_services_sovereign.py ......................... [  3%]
..............                                                           [  4%]
tests/test_2b_state_registry_sovereign.py .............................. [  6%]
.......................                                                  [  7%]
tests/test_agent_runtime.py ......                                       [  8%]
tests/test_api_gateway.py ...                                            [  8%]
tests/test_audit_canonical_record.py ..................                  [  9%]
tests/test_auth.py ...                                                   [  9%]
tests/test_benchmark.py ..........                                       [ 10%]
tests/test_common_branches.py .......................................... [ 13%]
.....                                                                    [ 13%]
tests/test_config.py ...                                                 [ 13%]
tests/test_control_console.py .........................                  [ 15%]
tests/test_critic.py ...........                                         [ 15%]
tests/test_durable_bus_branches.py ...........                           [ 16%]
tests/test_e2e.py ...                                                    [ 16%]
tests/test_edge_branches.py .........                                    [ 17%]
tests/test_event_bus.py ..............                                   [ 18%]
tests/test_event_schemas.py .....                                        [ 18%]
tests/test_executive_core.py ..............................              [ 20%]
tests/test_expansion.py .....................................            [ 22%]
tests/test_experience.py ...........                                     [ 23%]
tests/test_federation.py ...........................................     [ 26%]
tests/test_governance.py ...........................                     [ 28%]
tests/test_governance_phase3.py .........................                [ 29%]
tests/test_hash_chain.py ......                                          [ 30%]
tests/test_health.py ..............                                      [ 30%]
tests/test_health_system.py ................................             [ 32%]
tests/test_inmemory_stores.py ................................           [ 34%]
tests/test_king_login_boundary.py ......................                 [ 36%]
tests/test_memory_service.py ........                                    [ 36%]
tests/test_model_gateway.py ....                                         [ 37%]
tests/test_model_layer.py ..............                                 [ 38%]
tests/test_models.py ...                                                 [ 38%]
tests/test_orchestrator.py .......                                       [ 38%]
tests/test_p13_factories_sovereign.py ......................             [ 40%]
tests/test_persistence.py ........                                       [ 40%]
tests/test_phase12_states.py .................                           [ 41%]
tests/test_phase13_factories.py .............                            [ 42%]
tests/test_phase14_15_learning.py ..............                         [ 43%]
tests/test_phase16_security.py ................                          [ 44%]
tests/test_phase17_system_life.py ............                           [ 45%]
tests/test_phase1_postgres.py ssssssss                                   [ 45%]
tests/test_phase1_postgres_events.py sssssssssssssssss                   [ 46%]
tests/test_phase2_events.py ...........................                  [ 48%]
tests/test_phase3_governance.py ........................                 [ 49%]
tests/test_phase4_tools.py ..................                            [ 51%]
tests/test_phase5_models.py ...........                                  [ 51%]
tests/test_phase6_population.py ...............                          [ 52%]
tests/test_phase7_health.py .........                                    [ 53%]
tests/test_population.py ..................                              [ 54%]
tests/test_q19_money_delegation.py ............................          [ 56%]
tests/test_q20_money_representation.py .......ss..................       [ 57%]
tests/test_q31_money_engine_wiring.py ............                       [ 58%]
tests/test_q32_money_enforcement_surface.py ...............              [ 59%]
tests/test_r1_canonical_execution_path.py .................              [ 60%]
tests/test_r2_task_execution_integration.py .........................    [ 62%]
tests/test_r3_agent_runtime_integration.py .............                 [ 63%]
tests/test_r4_agent_identity_and_population.py ................          [ 64%]
tests/test_r5_multi_provider_sandbox.py ...................              [ 65%]
tests/test_r6_1_authorization_closure.py ..................              [ 66%]
tests/test_r6_identity_authorization_root.py .................           [ 67%]
tests/test_r7_government_services.py ................................    [ 69%]
tests/test_r7_state_registry.py ..........................               [ 71%]
tests/test_r7b_state_treasury.py ....................................    [ 73%]
tests/test_r7c_national_registry.py ...................................  [ 75%]
tests/test_r7d_federal_judiciary.py ...........................          [ 77%]
tests/test_r8_federal_state_integration.py ............................. [ 79%]
....                                                                     [ 79%]
tests/test_r9_national_economic_state.py ............................... [ 81%]
..............                                                           [ 82%]
tests/test_real_tools.py ....................                            [ 83%]
tests/test_shadow.py ..........                                          [ 84%]
tests/test_step19_durable_governance_state.py ........                   [ 84%]
tests/test_step7_gate_denial.py .....                                    [ 85%]
tests/test_tool_registry.py .......                                      [ 85%]
tests/test_training.py ...............                                   [ 86%]
tests/test_treasury.py ................................                  [ 88%]
tests/test_w032_registry_ownership.py .............                      [ 89%]
tests/test_w033_cost_record_durability.py .........                      [ 89%]
tests/test_w036_cost_precision.py ...........                            [ 90%]
tests/test_w166_postgres_driver_declared.py ................             [ 91%]
tests/test_w190_durable_model_registry.py ..                             [ 91%]
tests/test_w308_test_ledger_is_per_session.py ...                        [ 92%]
tests/test_wi062_migrations_cover_orm_tables.py ..s                      [ 92%]
tests/test_wi063_tenant_isolation_http.py ..ss..ss.s..ss.s.s.s..s.s.     [ 93%]
tests/test_wi064_migrations_follow_orm.py .s                             [ 93%]
tests/test_wi065_orm_declares_jsonb_timestamptz.py ..s                   [ 94%]
tests/test_wi066_convert_create_all_databases.py .sssss                  [ 94%]
tests/test_wi066_pg_session_isolation.py .ss                             [ 94%]
tests/test_wi067_legal_search_isolated.py .......................        [ 96%]
tests/test_wi076_pg_backup_restore.py ssss                               [ 96%]
tests/test_wi082_agent_identity_sovereign.py ........                    [ 96%]
tests/test_wi105_issue_ruling_sovereign.py ..........                    [ 97%]
tests/test_wi106_federation_coordinate_sovereign.py ........             [ 98%]
tests/test_wi107_national_registry_register_sovereign.py .........       [ 98%]
tests/test_wi111_judiciary_docket_sovereign.py .....................     [100%]

=============================== warnings summary ===============================
../../../.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w641/grok_4_7/wi111/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========== 1523 passed, 53 skipped, 1 warning in 229.73s (0:03:49) ============
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/audit/judicial_gate_probe.py
EXIT: 0
BYTES: 8412
SHA256: 9ffefb7fb6d5655d8d03a157b09211be642769cc306f93d8a38d94a024d6bc98
NO_EOL: 0
--- OUTPUT ---
*DENY* EXECUTIVE  adjudicate                       DENY       R-003-1
ALLOW  JUDICIAL   adjudicate                       ALLOW      
*DENY* LEGISLATIVE adjudicate                       DENY       R-003-1
ALLOW  ROYAL      adjudicate                       ALLOW      
*DENY* EXECUTIVE  issue_ruling                     DENY       R-003-1
ALLOW  JUDICIAL   issue_ruling                     ALLOW      
*DENY* LEGISLATIVE issue_ruling                     DENY       R-003-1
ALLOW  ROYAL      issue_ruling                     ALLOW      
*DENY* EXECUTIVE  vacate_ruling                    DENY       R-003-1
ALLOW  JUDICIAL   vacate_ruling                    ALLOW      
*DENY* LEGISLATIVE vacate_ruling                    DENY       R-003-1
ALLOW  ROYAL      vacate_ruling                    ALLOW      
*DENY* EXECUTIVE  admit_evidence                   DENY       R-003-1
ALLOW  JUDICIAL   admit_evidence                   ALLOW      
*DENY* LEGISLATIVE admit_evidence                   DENY       R-003-1
ALLOW  ROYAL      admit_evidence                   ALLOW      
*DENY* EXECUTIVE  register_judgment                DENY       R-003-1
ALLOW  JUDICIAL   register_judgment                ALLOW      
*DENY* LEGISLATIVE register_judgment                DENY       R-003-1
ALLOW  ROYAL      register_judgment                ALLOW      
*DENY* EXECUTIVE  refer_case                       DENY       R-003-1
ALLOW  JUDICIAL   refer_case                       ALLOW      
*DENY* LEGISLATIVE refer_case                       DENY       R-003-1
ALLOW  ROYAL      refer_case                       ALLOW      
*DENY* EXECUTIVE  admit_case                       DENY       R-003-1
ALLOW  JUDICIAL   admit_case                       ALLOW      
*DENY* LEGISLATIVE admit_case                       DENY       R-003-1
ALLOW  ROYAL      admit_case                       ALLOW      
*DENY* EXECUTIVE  recuse_judge                     DENY       R-003-1
ALLOW  JUDICIAL   recuse_judge                     ALLOW      
*DENY* LEGISLATIVE recuse_judge                     DENY       R-003-1
ALLOW  ROYAL      recuse_judge                     ALLOW      
ALLOW  EXECUTIVE  create_court                     ALLOW      
ALLOW  JUDICIAL   create_court                     ALLOW      
ALLOW  LEGISLATIVE create_court                     ALLOW      
ALLOW  ROYAL      create_court                     ALLOW      
ALLOW  EXECUTIVE  appoint_judge                    ALLOW      
ALLOW  JUDICIAL   appoint_judge                    ALLOW      
ALLOW  LEGISLATIVE appoint_judge                    ALLOW      
ALLOW  ROYAL      appoint_judge                    ALLOW      
ALLOW  EXECUTIVE  register_court                   ALLOW      
ALLOW  JUDICIAL   register_court                   ALLOW      
ALLOW  LEGISLATIVE register_court                   ALLOW      
ALLOW  ROYAL      register_court                   ALLOW      
ALLOW  EXECUTIVE  set_court_status                 ALLOW      
ALLOW  JUDICIAL   set_court_status                 ALLOW      
ALLOW  LEGISLATIVE set_court_status                 ALLOW      
ALLOW  ROYAL      set_court_status                 ALLOW      
ALLOW  EXECUTIVE  set_judge_status                 ALLOW      
ALLOW  JUDICIAL   set_judge_status                 ALLOW      
ALLOW  LEGISLATIVE set_judge_status                 ALLOW      
ALLOW  ROYAL      set_judge_status                 ALLOW      
ALLOW  EXECUTIVE  file_case                        ALLOW      
ALLOW  JUDICIAL   file_case                        ALLOW      
ALLOW  LEGISLATIVE file_case                        ALLOW      
ALLOW  ROYAL      file_case                        ALLOW      
*DENY* EXECUTIVE  assign_case                      DENY       R-003-1
ALLOW  JUDICIAL   assign_case                      ALLOW      
*DENY* LEGISLATIVE assign_case                      DENY       R-003-1
ALLOW  ROYAL      assign_case                      ALLOW      
ALLOW  EXECUTIVE  open_hearing                     ALLOW      
ALLOW  JUDICIAL   open_hearing                     ALLOW      
ALLOW  LEGISLATIVE open_hearing                     ALLOW      
ALLOW  ROYAL      open_hearing                     ALLOW      
ALLOW  EXECUTIVE  close_case                       ALLOW      
ALLOW  JUDICIAL   close_case                       ALLOW      
ALLOW  LEGISLATIVE close_case                       ALLOW      
ALLOW  ROYAL      close_case                       ALLOW      
ALLOW  EXECUTIVE  add_party                        ALLOW      
ALLOW  JUDICIAL   add_party                        ALLOW      
ALLOW  LEGISLATIVE add_party                        ALLOW      
ALLOW  ROYAL      add_party                        ALLOW      
ALLOW  EXECUTIVE  add_claim                        ALLOW      
ALLOW  JUDICIAL   add_claim                        ALLOW      
ALLOW  LEGISLATIVE add_claim                        ALLOW      
ALLOW  ROYAL      add_claim                        ALLOW      
ALLOW  EXECUTIVE  submit_evidence                  ALLOW      
ALLOW  JUDICIAL   submit_evidence                  ALLOW      
ALLOW  LEGISLATIVE submit_evidence                  ALLOW      
ALLOW  ROYAL      submit_evidence                  ALLOW      
ALLOW  EXECUTIVE  set_evidence_status              ALLOW      
ALLOW  JUDICIAL   set_evidence_status              ALLOW      
ALLOW  LEGISLATIVE set_evidence_status              ALLOW      
ALLOW  ROYAL      set_evidence_status              ALLOW      
*DENY* EXECUTIVE  record_proceeding                DENY       R-003-1
ALLOW  JUDICIAL   record_proceeding                ALLOW      
*DENY* LEGISLATIVE record_proceeding                DENY       R-003-1
ALLOW  ROYAL      record_proceeding                ALLOW      
ALLOW  EXECUTIVE  record_enforcement               ALLOW      
ALLOW  JUDICIAL   record_enforcement               ALLOW      
ALLOW  LEGISLATIVE record_enforcement               ALLOW      
ALLOW  ROYAL      record_enforcement               ALLOW      
ALLOW  EXECUTIVE  enforce_ruling                   ALLOW      
ALLOW  JUDICIAL   enforce_ruling                   ALLOW      
ALLOW  LEGISLATIVE enforce_ruling                   ALLOW      
ALLOW  ROYAL      enforce_ruling                   ALLOW      
*DENY* EXECUTIVE  pardon                           DENY       R-010-1,R-010-5
*DENY* JUDICIAL   pardon                           DENY       R-010-1,R-010-5
*DENY* LEGISLATIVE pardon                           DENY       R-010-1,R-010-5
*DENY* ROYAL      pardon                           DENY       R-010-3,R-010-5
*DENY* EXECUTIVE  overturn_judicial_ruling         DENY       R-010-1,R-010-5
*DENY* JUDICIAL   overturn_judicial_ruling         DENY       R-010-1,R-010-5
*DENY* LEGISLATIVE overturn_judicial_ruling         DENY       R-010-1,R-010-5
*DENY* ROYAL      overturn_judicial_ruling         DENY       R-010-3,R-010-5
*DENY* EXECUTIVE  legislate                        DENY       R-003-1
*DENY* JUDICIAL   legislate                        DENY       R-003-1
ALLOW  LEGISLATIVE legislate                        ALLOW      
ALLOW  ROYAL      legislate                        ALLOW      
*DENY* EXECUTIVE  enact_policy                     DENY       R-003-1
*DENY* JUDICIAL   enact_policy                     DENY       R-003-1
ALLOW  LEGISLATIVE enact_policy                     ALLOW      
ALLOW  ROYAL      enact_policy                     ALLOW      
*DENY* EXECUTIVE  amend_policy                     DENY       R-003-1
*DENY* JUDICIAL   amend_policy                     DENY       R-003-1
ALLOW  LEGISLATIVE amend_policy                     ALLOW      
ALLOW  ROYAL      amend_policy                     ALLOW      
*DENY* EXECUTIVE  repeal_policy                    DENY       R-003-1
*DENY* JUDICIAL   repeal_policy                    DENY       R-003-1
ALLOW  LEGISLATIVE repeal_policy                    ALLOW      
ALLOW  ROYAL      repeal_policy                    ALLOW      
ALLOW  EXECUTIVE  suspend_policy                   ALLOW      
ALLOW  JUDICIAL   suspend_policy                   ALLOW      
ALLOW  LEGISLATIVE suspend_policy                   ALLOW      
ALLOW  ROYAL      suspend_policy                   ALLOW      
ALLOW  EXECUTIVE  vote                             ALLOW      
ALLOW  JUDICIAL   vote                             ALLOW      
ALLOW  LEGISLATIVE vote                             ALLOW      
ALLOW  ROYAL      vote                             ALLOW      
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md
EXIT: 0
BYTES: 16752
SHA256: 5191864775be28601661e6ce38584edf9d360a073cf4a7975e2cdc69c9b2d516
NO_EOL: 0
--- OUTPUT ---
# ملحقُ تصميمِ الدفعةِ J2+J3 (الجزءُ المحسومُ) — خمسةَ عشرَ سطحًا قضائيًّا تعبرُ الحدَّ بفاعلِ الوحدةِ القضائيِّ وبأفعالِ D17-2 المعتمدةِ

## التعريف
ملحقُ تصميمٍ قصيرٌ للدفعةِ **J2+J3** (بندُ `WI-111`) يُودَعُ **في التزامٍ مستقلٍّ يسبقُ أيَّ شِفرةٍ** (قرارُ المالكِ Q-61 · «تُعرَضُ قبلَ الشِّفرةِ») بتوجيهِ المستشارِ 21 § 2: «J2 + J3 (الجزء المحسوم) بنمط J1 مع ملحق تصميم قصير يسبق الشفرة». يحدِّدُ الأسطحَ مقيسةً، والأفعالَ، وموضعَ العبورِ، ونطاقاتِ الجدارِ، والآثارَ، والمفاتيحَ، والمُعوِّضاتِ، والفحوصَ والطفراتِ، والأرقامَ المتوقَّعةَ قبلَ الشِّفرةِ.

## النطاق
الإنتاجُ: `federal/executive/services/src/amos_federation/services/federal_judiciary/{service.py,docket.py,rulings.py}` · ومعجمُ المُحرِّكِ `core/constitutional_engine/rules.py` (`JUDICIAL_ACTIONS`) · وجدارُ الاختصاصِ `core/sovereignty/jurisdiction.py` (`JUDICIAL_ACTIONS`). والفحوصُ: `federal/executive/services/tests/test_wi111_judiciary_docket_sovereign.py`. **لا يمسُّ** أسطحَ الأفعالِ الأربعةِ المؤجَّلةِ (D17-2 · D21-أ بند 9) ولا أسطحَ J4 الثلاثةَ ولا `registry.py` ولا `models.py` ولا `authority.py`.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 — منسِّقٌ لا مُصوِّتٌ) — بندُ `WI-111`.

## تاريخ الإنشاء
2026-10-23

## تاريخ آخر تعديل
2026-10-23 (النسخةُ الأولى — قبلَ الشِّفرةِ)

---

## 0. السندُ (لا اختراعَ)

- **قرارُ المالكِ D17-2** (خيارُ 1 · W-592) وجدولُ أفعالِه اسمًا اسمًا في [`HANDOFFS/OWNER-DECISIONS-D17.md`](../governance/work/HANDOFFS/OWNER-DECISIONS-D17.md) § البندُ 2 · و**D17-2 (الأربعةُ)** (W-612): «تُنفَّذ الأسطح الأخرى بالأفعال المعتمدة في D17-2» · و**D21-أ بند 9**: «تبقى الأفعال الأربعة مؤجَّلة».
- **قرارُ المالكِ D21-هـ** (W-631): «أطلقْ بعدَ J2/J3» — فجولةُ هذه الدفعةِ في الإطلاقِ الواحدِ معَ F1 وR1 وWI-084.
- **سابقةُ J1** ([`J1_ISSUE_RULING_DESIGN.md`](J1_ISSUE_RULING_DESIGN.md) · WI-105 CLOSED): فاعلُ الوحدةِ `JUDICIARY_ACTOR = "JUDICIAL"` بمُصرِّحٍ واحدٍ (`rulings._judiciary_authorizer` · D1) · طلبُ اختصاصٍ منَ البياناتِ الحيّةِ (D3) · مُطبِّقٌ متداخلٌ واحدٌ يحملُ الكتابةَ والالتزامَ (D4) · مُعوِّضٌ تقنيٌّ بجلسةٍ جديدةٍ (D7-أ) · إعادةٌ تُقرأُ ولا تُكتَبُ (D6).

## 1. الأسطحُ (مقيسةً · `sovereign_write_inventory.py --json` عندَ `7a547fa`)

جردُ `federal_judiciary` عندَ `7a547fa` (ومثلُه عندَ `6f3fba2` — لا شِفرةَ بينهما): **25 سطحًا عامًّا دَينًا** (عدا `issue_ruling` المحروسِ). منها **3 لـJ4** (`enforce_ruling_via_task` · `enforce_ruling_via_treasury` · `enforcement.record_enforcement`) و**7 للأفعالِ الأربعةِ المؤجَّلةِ** (`service/docket.submit_evidence` · `service/registry.appoint_judge` · `service.register_court` · `registry.create_court` · `service.set_court_status`) — **فالمحسومُ 15 سطحًا لا 22** (رقمُ الـ22 في الخطّةِ يضمُّ المؤجَّلَ؛ قياسٌ لا إسقاطٌ):

| # | السطح | الفعلُ (D17-2) | جديدٌ في المعجمِ؟ | موضعُ العبورِ |
|---|---|---|---|---|
| 1 | `service.vacate_ruling` | `vacate_ruling` (J2) | المُحرِّكُ: نعم · الجدارُ: قائمٌ | الخدمة |
| 2 | `service.file_case` | `refer_case` | المُحرِّكُ: نعم · الجدارُ: قائمٌ | الخدمة |
| 3–4 | `service.open_case` + `docket.open_case` | `admit_case` | المُحرِّكُ: نعم · الجدارُ: قائمٌ | `docket` (والخدمةُ مُنسِّقٌ بلا التزامٍ) |
| 5 | `service.set_evidence_status` | `admit_evidence` | المُحرِّكُ: نعم · الجدارُ: قائمٌ | الخدمة |
| 6 | `service.set_judge_status` | `recuse_judge` | المُحرِّكُ: نعم · الجدارُ: قائمٌ | الخدمة |
| 7 | `service.close_case` | `register_judgment` | المُحرِّكُ: نعم · الجدارُ: قائمٌ | الخدمة |
| 8 | `service.assign_case` | `assign_case` | **كلاهما جديدٌ** | الخدمة |
| 9 | `service.open_hearing` | `adjudicate` | قائمٌ في كليهما | الخدمة |
| 10–11 | `service.record_proceeding` + `docket.record_proceeding` | `record_proceeding` | **كلاهما جديدٌ** | `docket` |
| 12–13 | `service.add_party` + `docket.add_party` | `join_party` | **كلاهما جديدٌ** | `docket` |
| 14–15 | `service.add_claim` + `docket.add_claim` | `admit_claim` | **كلاهما جديدٌ** | `docket` |

## 2. نقاطُ التصميم

- **D1 · الفاعلُ:** فاعلُ الوحدةِ الواحدُ نفسُه منَ J1 — `rulings._judiciary_authorizer()` (`JUDICIAL`) — لا مُصرِّحَ ثانٍ. والإعلانُ لا يأذنُ: البوابةُ تُقيِّمُ الفعلَ للفاعلِ.
- **D2 · المعجمانِ:** يُضافُ إلى `rules.JUDICIAL_ACTIONS` عشرةُ أفعالٍ (`refer_case` · `admit_case` · `vacate_ruling` · `admit_evidence` · `recuse_judge` · `register_judgment` · `assign_case` · `record_proceeding` · `join_party` · `admit_claim`) فيصيرُ كلٌّ منها **حصرًا قضائيًّا يُرفَضُ لغيرِ القضاءِ بـR-003-1** (تضييقٌ لا توسيعٌ — على سابقةِ معجمِ المالِ Q-18) · ويُضافُ إلى `jurisdiction.JUDICIAL_ACTIONS` الأربعةُ الجديدةُ (`assign_case` · `record_proceeding` · `join_party` · `admit_claim`) ليُفحَصَ كلُّ عبورٍ بها بالجدارِ (`_guard_jurisdiction` يُلزِمُ طلبَ اختصاصٍ لكلِّ فعلٍ في الجدارِ). **وقياسُ ما قبلُ** (`judicial_gate_probe.py --json`): الأفعالُ الستّةُ القائمةُ في الجدارِ و`assign_case`/`record_proceeding` كلُّها `ALLOW` لـ`EXECUTIVE` و`LEGISLATIVE` اليومَ.
- **D3 · موضعُ العبورِ ولا تعشيشَ:** حيثُ يُدرِجُ `docket` صفًّا (`open_case` · `add_party` · `add_claim` · `record_proceeding`) يعبرُ **`docket` نفسُه** الحدَّ (على سابقةِ `rulings.issue_ruling`) وتصيرُ الخدمةُ مُنسِّقًا بلا التزامٍ؛ وحيثُ لا يُدرِجُ (`file_case` · `assign_case` · `open_hearing` · `close_case` · `set_evidence_status` · `set_judge_status` · `vacate_ruling`) تعبرُ **الخدمةُ**. والكاتبُ الخامُ للإجراءِ يصيرُ خاصًّا `docket._insert_proceeding` يُنادى من داخلِ المُطبِّقاتِ (`file_case` · `open_hearing` · `rulings.issue_ruling`) — **فلا عبورَ داخلَ عبورٍ** (Q-9 لم يُحسَمْ: تحليلُه بندُ `WI-110`).
- **D4 · طلبُ الاختصاصِ:** `court_scope` = نطاقُ المحكمةِ و`case_scope` = نطاقُ القضيّةِ منَ الصفوفِ الحيّةِ. و`actor_scope`: في `vacate_ruling` منصبُ القاضي المُثبَتُ (`require_judicial_authority` قائمٌ اليومَ) كـJ1؛ **وفي البقيةِ نطاقُ المحكمةِ مُعلَنًا** لأنَّ هذه الأسطحَ لا تُثبِتُ منصبًا اليومَ (`require_domain_permission` وحدَه). **حدٌّ معلَنٌ:** فحصُ «المنصبِ في نطاقِ المحكمةِ» عندَها تحصيلُ حاصلٍ — وإلزامُها بإثباتِ منصبٍ تغييرٌ لمن يحقُّ له النداءُ، وهو خارجُ هذه الدفعةِ (لا توسيعَ ولا تضييقَ لمن ينادي).
- **D5 · الآثارُ:** `CREATE` للإدراجِ و`WRITE` للانتقالِ — وكلاهما قضائيٌّ في الجدارِ (`assert_effect_judicial`) · لا `DELETE` ولا `TRANSFER` ولا `EXTERNAL`.
- **D6 · مفاتيحُ الذرّيّةِ والإعادةِ:** انتقالٌ ⇒ `(المعرِّفُ · الحالةُ السابقةُ → اللاحقةُ)` · `open_case` ⇒ `(المستأجرُ · المرجعُ)` · `add_party` ⇒ `(القضيّةُ · الهويّةُ · الدورُ)` — وكلُّها فريدةٌ بقيدٍ أو بفحصٍ قائمٍ؛ **و`add_claim`/`record_proceeding` بلا مفتاحٍ طبيعيٍّ** فمفتاحُهما فريدٌ لكلِّ نداءٍ (حدٌّ معلَنٌ: لا ذرّيّةَ عبرَ إعادةِ المُنادي). والفحوصُ الموجودةُ (انتقالٌ مسموحٌ · مرجعٌ غيرُ مستعمَلٍ · طرفٌ غيرُ مكرَّرٍ) تجري **قبلَ** الحدِّ. والإعادةُ (`is_replay`) تقرأُ الصفَّ القائمَ ولا تكتبُ.
- **D7 · المُعوِّضاتُ:** استعادةٌ تقنيّةٌ في جلسةٍ جديدةٍ على نمطِ J1 D7-أ: حذفُ الصفِّ المُدرَجِ بمعرِّفِه، وإرجاعُ الحقولِ المنقولةِ إلى قيمِها قبلَ العمليّةِ (الحالةُ وما يرافقُها) وحذفُ صفِّ الإجراءِ المُرافقِ.
- **D8 · نقطتانِ معلَنتانِ للمجلسِ والمالكِ (لا تُحسَمانِ هنا):** (أ) **`set_judge_status` ⇐ `recuse_judge`** كما في الجدولِ المعتمدِ، لكنَّ الدالّةَ تُعلِّقُ وتعزلُ (`suspended` · `revoked`) — والعزلُ أقربُ إلى عكسِ `appoint_judge` المؤجَّلِ فرعُه · (ب) **`assign_case`** يصيرُ حصرًا قضائيًّا في المُحرِّكِ، و`government_services.assign_case` (سطحُ X1 تنفيذيٌّ) لا يعبرُ اليومَ فلا ينكسرُ — لكنَّه حينَ يُهاجَرُ يلزمُه فعلٌ آخرُ.

## 3. الأرقامُ المتوقَّعةُ (مكتوبةٌ قبلَ الشِّفرةِ · بالأداةِ نفسِها)

- **D-4: 157 ← 142** (الأسطحُ الخمسةَ عشرَ: 11 تعبرُ و4 خدماتٍ تخرجُ منَ العدِّ لأنَّها لا تكتبُ — نمطُ J1 الذي أنقصَ اثنينِ بعبورٍ واحدٍ).
- السياديُّ: **42 ← 53** (11 عابرةً).
- `judicial_gate_probe`: الأفعالُ العشرةُ `DENY · R-003-1` لـ`EXECUTIVE` و`LEGISLATIVE` · `ALLOW` لـ`JUDICIAL` و`ROYAL`.

## 4. الفحوصُ (`test_wi111_judiciary_docket_sovereign.py`)

لكلِّ فعلٍ منَ العشرةِ: T1 فاعلٌ تنفيذيٌّ ⇒ `DENY` (R-003-1) · T2 فاعلُ الوحدةِ ⇒ عبورٌ وقيدٌ في سجلِّ الحدِّ بالفعلِ المعتمدِ · T3 الأثرُ المُعلَنُ ونوعُه ومُعوِّضُه · T4 الإعادةُ لا تكتبُ صفًّا ثانيًا (للمفاتيحِ الطبيعيّةِ) · T5 فشلٌ بعدَ الالتزامِ ⇒ المُعوِّضُ يُعيدُ الحالةَ · T6 الجردُ: الأسطحُ الخمسةَ عشرَ عابرةٌ أو خارجةٌ منَ العدِّ · T7 `issue_ruling` لا يُعشِّشُ عبورًا (مُطبِّقُه يستعملُ الكاتبَ الخاصَّ) · T8 الحزمةُ الكاملةُ خضراءُ.

## 5. الطفراتُ (كلٌّ يجبُ أن يُسقِطَ فحصَه)

- **M1** حذفُ `guard_declared(` من سطحٍ في مجموعةِ الانتقالاتِ (`assign_case`) ⇒ T6 يسقطُ.
- **M2** حذفُه من سطحٍ في مجموعةِ الإدراجِ (`docket.add_party`) ⇒ T2/T6 يسقطانِ.
- **M3** حذفُ فعلٍ جديدٍ منَ المعجمِ (`join_party`) ⇒ T1 يسقطُ.
- **M4** المُعوِّضُ لا يُعيدُ الحالةَ (`close_case`) ⇒ T5 يسقطُ.
- **M5** مُطبِّقُ `issue_ruling` ينادي `record_proceeding` العامَّ ⇒ T7 يسقطُ.

## 6. ما لا يُنجَزُ في J2+J3 ولماذا

الأفعالُ الأربعةُ المؤجَّلةُ (7 أسطحٍ · D21-أ بند 9) · J4 (3 · جولةُ WI-084 في الطابورِ) · إثباتُ منصبِ الفاعلِ في الأسطحِ الإداريّةِ (D4 · تغييرٌ لمن ينادي) · ذرّيّةُ `add_claim`/`record_proceeding` عبرَ الإعادةِ (D6).

## 7. ما قيسَ بعدَ الشِّفرةِ (W-640 · مُلحَقٌ مؤرَّخٌ — ما فوقَه لم يُمَسَّ)

> الأقسامُ 1–6 كُتِبَت قبلَ الشِّفرةِ وتبقى كما هي. وهذا ما خالفَ المتوقَّعَ أو أُضيفَ عندَ التنفيذِ — مقيسًا بالأدواتِ نفسِها (`evidence/W-640/`).

- **D-4: 157 ← 142 — كما تُوُقِّعَ.** **والسياديُّ: 42 ← 46 لا 53.** العابرُ المعدودُ الأسطحُ الأربعةُ في `docket` وحدَها؛ والخدماتُ السبعُ (`vacate_ruling` · `file_case` · `set_evidence_status` · `set_judge_status` · `close_case` · `assign_case` · `open_hearing`) تحملُ النداءَ في جسدِها لكنَّ كتابتَها صارت في مُطبِّقٍ يبنيه `docket._plan_crossing` فلا يراها الجردُ موضعَ كتابةٍ أصلًا — فتخرجُ منَ العدِّ ولا تدخلُ «العابرَ». التوقُّعُ (53) افترضَ أنَّ الخدمةَ تبقى موضعَ كتابةٍ؛ وهذا **عمىً في الأداةِ** مُقيَّدٌ في DISC-132 (2) لا تُعادُ صياغةُ الشِّفرةِ لتضخيمِ الرقمِ.
- **M1 قتلَه T2 وT2b وT5 لا T6** (خلافَ § 5): لنفسِ العمى — حذفُ النداءِ من خدمةٍ مُفوِّضةٍ لا يُعيدُها دَينًا. فالشاهدُ على عبورِ الخدماتِ السبعِ **فحصُ المسارِ الإنتاجيِّ** (T2: تسلسلُ الأفعالِ الاثني عشرَ حرفيًّا) لا الجردُ.
- **`_plan_crossing` خاصٌّ:** كانَ عامًّا في المسوّدةِ فعدَّه الجردُ عمليّةً عامّةً مُغيِّرةً بلا عبورٍ (143) — وهو بانٍ لا عمليّةٌ، فصارَ خاصًّا (142). وتنادي الخدمةُ `docket._plan_crossing` عبرَ الوحدةِ — مُعلَنٌ.
- **فحوصٌ قبلَ الحدِّ بمصدرٍ واحدٍ:** أُضيفَت `docket.check_assign` · `check_close` · `check_evidence_status` و`rulings.check_vacate` ويناديها الكاتبُ نفسُه — فلا تكرارَ. **إلّا `set_judge_status`:** `registry.py` خارجَ النطاقِ فأُعيدَت فحوصُه الثلاثةُ في الخدمةِ مطابِقةً (الحالةُ · السببُ · وجودُ التقليدِ في المستأجرِ) — تكرارٌ معلَنٌ يُزالُ حينَ يُهاجَرُ `appoint_judge` (D21-أ بند 9).
- **فحصُ J1 كُيِّفَ لا خُفِّفَ:** `test_wi105_issue_ruling_sovereign.py` كانَ يعدُّ `authorizer.results` كلَّها (1 · 2 · 1) فصارَ يجدُ معها عبوراتِ التجهيزِ (4 · 6 · 4). أُضيفَ `_ruling_results` يُصفّي بالفعلِ `issue_ruling` فيبقى القيدُ نفسُه على إصدارِ الحكمِ (عددًا وهدفًا وجيلًا)، وقيدُ T5 على سجلِّ البوابةِ باقٍ بلا تغيير. يُعرَضُ على المجلسِ نصًّا.
- **فحوصُ WI-111 21 خضراءَ** · طفراتٌ خمسٌ مقتولةٌ (`evidence/W-640/mutations.txt` بأسماءِ الفحوصِ الساقطةِ) · والمسبارُ القضائيُّ بعدَ الشِّفرةِ `evidence/W-640/judicial_gate_probe_after.{json,txt}`.
- **حدٌّ معلَنٌ إضافيٌّ:** تعطيلُ معجمِ المُحرِّكِ وحدَه (M3) يُمرِّرُ فاعلًا تنفيذيًّا على `add_party` (T2b) — جدارُ الاختصاصِ لا يمنعُ الفاعلَ بل الأثرَ والنطاقَ، فالمنعُ الفرعيُّ منَ المعجمِ وحدَه.
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-638/inventory_before_wi111.txt docs/audit/evidence/W-640/inventory_after_wi111.txt
EXIT: 0
BYTES: 6625
SHA256: 7eaf9c4f3f90b8bc6effac93db19d24624f032bfbb04bcd5c04170d4ca292fcd
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 246
  عمليّاتٌ عامّةٌ مُغيِّرة   : 201
  منها تعبرُ الحدَّ        : 42
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 157
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          171 /  42 /  128
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      17  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
      10  federal/executive/services/src/amos_federation/services/federal_state/service.py
       9  federal/executive/services/src/amos_federation/services/governance/treasury.py
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
  التفصيلُ محفوظٌ في: docs/audit/evidence/W-638/inventory_before_wi111.json
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 239
  عمليّاتٌ عامّةٌ مُغيِّرة   : 190
  منها تعبرُ الحدَّ        : 46
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 142
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          160 /  46 /  113
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
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
  التفصيلُ محفوظٌ في: docs/audit/evidence/W-640/inventory_after_wi111.json
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-641/mutation_probe_wi111.py.txt
EXIT: 0
BYTES: 5067
SHA256: 0654890d03f8be1165a5bde3729bd8321b31d9220bd6289376673fd5e9c2c583
NO_EOL: 0
--- OUTPUT ---
"""الهدف: مسبارُ طفراتِ WI-111 (J2+J3) الآليُّ — يُطبِّقُ كلَّ طفرةٍ منَ الخمسِ المُعلَنةِ في ملحقِ
J2J3_JUDICIARY_DOCKET_DESIGN.md § 5 على حدةٍ، ويُشغِّلُ ملفَّي الفحوصِ، ثمَّ يُعيدُ الأصلَ ويتحقَّقُ أنّه
مستعادٌ بايتًا ببايتٍ (sha256). نمطُ mutation_probe_wi107 (W-628). يُحفَظُ بلاحقةِ .py.txt كي لا
يُعَدَّ شِفرةً إنتاجيّةً في الجردِ (درسُ W-639 · DISC-132) ويُشغَّلُ بـ`.venv/bin/python <المسار>`
منْ جذرِ الاستنساخِ. القيدُ W-641.
"""
import hashlib
import subprocess, sys, shutil, pathlib
ROOT = pathlib.Path.cwd()
assert (ROOT / "core/constitutional_engine/rules.py").is_file(), "شغِّلْه منْ جذرِ الاستنساخِ"
J = ROOT / "federal/executive/services/src/amos_federation/services/federal_judiciary"
MUT = {
 "M1": (J/"service.py", "            guarded = rulings._judiciary_authorizer().guard_declared(\n                plan.action, plan.target, **plan.kwargs\n            )\n            row = docket.crossed_value(\n                guarded,\n                replay=lambda: docket.load_case(session, case.id, tenant_id=tenant),\n                what=f\"إسنادَ",
        "            guarded = docket._Unguarded(plan.kwargs[\"applier\"](None))\n            row = docket.crossed_value(\n                guarded,\n                replay=lambda: docket.load_case(session, case.id, tenant_id=tenant),\n                what=f\"إسنادَ"),
 "M2": (J/"docket.py", "        namespace=\"judiciary.party.add\",", "        namespace=\"judiciary.party.add\",  # M2"),
 "M3": (ROOT/"core/constitutional_engine/rules.py", "\"assign_case\", \"record_proceeding\", \"join_party\", \"admit_claim\",", "\"assign_case\", \"record_proceeding\", \"admit_claim\","),
 "M4": (J/"docket.py", "            for model, row_id, values in before:\n                row = restore.get(model, row_id)\n                if row is not None:\n                    for name, value in values.items():\n                        setattr(row, name, value)", "            for model, row_id, values in before:\n                row = restore.get(model, row_id)\n                if row is not None and False:\n                    for name, value in values.items():\n                        setattr(row, name, value)"),
 "M5": (J/"rulings.py", "        proceeding = _insert_proceeding(\n            session,\n            case_id=case.id,\n            proceeding_type=\"RULING\",", "        from amos_federation.services.federal_judiciary.docket import record_proceeding as _rp\n\n        proceeding = _rp(\n            session,\n            case_id=case.id,\n            proceeding_type=\"RULING\","),
}
EXTRA = {"M1": ("docket.py", "\n\nclass _Unguarded:\n    is_replay = False\n\n    def __init__(self, value):\n        self.value = value\n")}
TESTS = ["tests/test_wi111_judiciary_docket_sovereign.py"]
FILES = sorted({p for p, _, _ in MUT.values()} | {J / "docket.py"})
def digest():
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in FILES}
BASE = digest()
killed = 0
for name in sys.argv[1:] or sorted(MUT):
    tests = TESTS
    path, old, new = MUT[name]
    backup = path.read_text()
    assert backup.count(old) == 1, (name, backup.count(old))
    mut = backup.replace(old, new)
    extra_backup = None
    if name == "M2":
        # remove the guard call in docket.add_party: replace its guard line with a direct apply
        o = "    guarded = _authorizer().guard_declared(plan.action, plan.target, **plan.kwargs)\n    return crossed_value(\n        guarded,\n        replay=lambda: session.execute(\n            select(CasePartyModel)"
        assert mut.count(o) == 1
        mut = mut.replace(o, "    guarded = _Unguarded(plan.kwargs[\"applier\"](None))\n    return crossed_value(\n        guarded,\n        replay=lambda: session.execute(\n            select(CasePartyModel)")
        mut += EXTRA["M1"][1]
    path.write_text(mut)
    if name == "M1":
        d = J/"docket.py"; extra_backup = d.read_text(); d.write_text(extra_backup + EXTRA["M1"][1])
    try:
        r = subprocess.run([str(ROOT/".venv/bin/python"), "-m", "pytest", "-q", "-p", "no:cacheprovider", *tests],
                           cwd=ROOT/"federal/executive/services", capture_output=True, text=True, timeout=600)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:]
        failed = [l.split("::")[-1].split(" ")[0] for l in r.stdout.splitlines() if l.startswith("FAILED")]
        print(f"{name}: {'KILLED' if r.returncode != 0 else 'SURVIVED'} · {last} · failed={failed}")
    finally:
        path.write_text(backup)
        if extra_backup is not None:
            (J/"docket.py").write_text(extra_backup)
    restored = digest() == BASE
    print(f"{name}: restored_bytes={restored}")
    assert restored, name

print("BASELINE_RESTORED:", digest() == BASE)
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python docs/audit/evidence/W-641/mutation_probe_wi111.py.txt
EXIT: 0
BYTES: 1605
SHA256: 31db8b153310da841e7bd1ba550afdf217d0cfe184bfd7155aeb548d9eba2291
NO_EOL: 0
--- OUTPUT ---
M1: KILLED · ========================= 3 failed, 18 passed in 7.77s ========================= · failed=['test_wi111_t2_production_path_crosses_with_d17_2_verbs', 'test_wi111_t2b_executive_actor_is_denied_and_nothing_is_written[assign_case]', 'test_wi111_t5_failed_settle_restores_assignment_and_closure']
M1: restored_bytes=True
M2: KILLED · ========================= 4 failed, 17 passed in 9.04s ========================= · failed=['test_wi111_t2_production_path_crosses_with_d17_2_verbs', 'test_wi111_t2b_executive_actor_is_denied_and_nothing_is_written[add_party]', 'test_wi111_t5b_failed_settle_removes_inserted_party_and_proceeding', 'test_wi111_t6_inventory_has_no_debt_on_settled_surfaces']
M2: restored_bytes=True
M3: KILLED · ======================== 3 failed, 18 passed in 12.15s ========================= · failed=['test_wi111_t1_engine_denies_non_judicial_and_allows_judicial[join_party]', 'test_wi111_t1b_wall_knows_the_four_new_verbs_and_not_the_deferred', 'test_wi111_t2b_executive_actor_is_denied_and_nothing_is_written[add_party]']
M3: restored_bytes=True
M4: KILLED · ========================= 2 failed, 19 passed in 7.83s ========================= · failed=['test_wi111_t5_failed_settle_restores_assignment_and_closure', 'test_wi111_t5b_failed_settle_removes_inserted_party_and_proceeding']
M4: restored_bytes=True
M5: KILLED · ========================= 2 failed, 19 passed in 7.66s ========================= · failed=['test_wi111_t2_production_path_crosses_with_d17_2_verbs', 'test_wi111_t7_no_nested_crossing_on_any_surface']
M5: restored_bytes=True
BASELINE_RESTORED: True
=== RAW [19] END ===
=== RAW [20] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && rg -n "D17-2|Q-61" docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 0
BYTES: 13341
SHA256: 3ea1a00415ee9635feebdfeb18ea6dd097f93243af8d2cf538f291f1ec36203f
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-23 (`W-636/W-637` — تسجيلُ WI-109 (تحليلُ A1) · WI-110 (تحليلُ Q-9) · WI-111 (J2+J3 · 15 سطحًا محسومًا مقيسًا) READY · حرسُ D21-د تحتَ WI-040 (`NEW_ITEM_CLAIMING_ENTRY`) · N+1 لـW-631…W-635 أخضرُ (40030379965) · تصحيحُ تاريخِ الرياضِ في D21-هـ) · ووقبله ((`W-632…W-635` — قراراتُ المالكِ بتوجيهِ المستشارِ 21 على ورقةِ D20 بنصوصِها الحرفيّةِ: Q-7 · Q-8 · Q-13 · Q-14 · Q-23 · Q-26 · Q-28 · Q-29 · Q-30 · Q-32 · Q-33 · Q-34 · Q-36 · Q-37 · Q-41 · E1 DECIDED · وA1 وQ-9 وQ-10 تحليلٌ/قياسٌ أوّلًا) · ووقبله (`W-625` — **Q-71 DECIDED** بأمرِ المالكِ الصريحِ: «أذن بـconftest.py تحت WI-107» — قسمةُ نطاقِ مسارِ conftest.py من WI-072 إلى WI-107) · ووقبله (`W-612` — **D17-2** الأربعةُ مؤجَّلةٌ ولا تعطّلُ J2/J3 · **إبلاغُ ما بعدَ الدمجِ** يبقى إبلاغًا (توجيهُ المستشارِ 19 § 1)) · ووقبله ((`W-611` — **Q-61 DECIDED** بالخيارِ (3) بتطبيقٍ صريحٍ على WI-096 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-610` — **D19 DECIDED**: إذنُ المالكِ بإغلاقِ WI-105 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`))))
2335:- «9: تبقى الأفعال الأربعة مؤجَّلة.» ⇒ `establish_court` · `set_court_status` · `appoint_judge` · `submit_evidence` مؤجَّلةٌ (تأكيدُ D17-2).
2363:### Q-61 · عرضُ التصميمِ قبلَ الشِّفرةِ في WI-096 — DECIDED (W-611)
2364:«Q-61: خيار (3) مع تطبيق صريح على WI-096. أقرّ أن شرط عرض التصميم قبل الشفرة لم يتحقق إجرائيًّا في WI-096 وأتجاوزه لهذا البند وحده لأن المعايير 2 و3 و4 تحققت بإجماع المقاعد، ويُقيَّد الإخلال كما هو. وللبنود القادمة يُودَع التصميم في التزام مستقل يسبق الشفرة. ثم تُعاد جولة WI-096 بمسبار كل مقعد.» ⇒ تفصيلُه تحتَ `## Q-61`.
2366:### D17-2 (الأفعالُ الأربعةُ المستثناةُ) — DECIDED بالتأجيلِ (W-612)
2367:«D17-2 (الأفعال الأربعة): تُؤجَّل establish_court وset_court_status وappoint_judge وsubmit_evidence إلى قرار لاحق، ولا تعطّل بقية J2/J3: تُنفَّذ الأسطح الأخرى بالأفعال المعتمدة في D17-2.» ⇒ الأربعةُ باقيةٌ سؤالًا مفتوحًا (لا تُنفَّذُ أسطحُها) · وما عداها من J2/J3 مفتوحٌ بأفعالِ D17-2 المعتمدةِ.
2433:### D17-2 · أفعالُ القضاءِ والولاياتِ في معجمِ المُحرِّكِ — DECIDED (باستثناءاتٍ)
2447:«لا جولات مجلس على تصميم منفرد من الآن. الجولة الواحدة لكل دفعة تغطي التصميم والشفرة والأدلة معًا بعد التنفيذ. شرط الترتيب باقٍ: التزام وثيقة التصميم يسبق التزام الشفرة في التاريخ (يتحقق منه الفاحص)، وهذا هو درس Q-61. … حجم الدفعة: كل دفعة تقدَّم إلى main تنقص D-4 بما لا يقل عن عشرة أسطح حيث يسمح النمط، إلا ما فرضه التصميم (J1 = 2 لأنه يُرسي النمط).» — نُفِّذَ تعديلُ البروتوكولِ مؤرَّخًا (W-592).
2604:## Q-61 · هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — DECIDED (2026-10-22 · W-611 · توجيهُ المستشارِ 19 § 1 · الخيارُ 3 بتطبيقٍ صريحٍ على WI-096) · وكانَ PENDING_OWNER (2026-10-19 · W-521)
2606:> **[إضافةٌ مؤرَّخةٌ · 2026-10-22 · W-611] DECIDED — نصُّ المالكِ حرفيًّا:** «Q-61: خيار (3) مع تطبيق صريح على WI-096. أقرّ أن شرط عرض التصميم قبل الشفرة لم يتحقق إجرائيًّا في WI-096 وأتجاوزه لهذا البند وحده لأن المعايير 2 و3 و4 تحققت بإجماع المقاعد، ويُقيَّد الإخلال كما هو. وللبنود القادمة يُودَع التصميم في التزام مستقل يسبق الشفرة. ثم تُعاد جولة WI-096 بمسبار كل مقعد.» (النصُّ الكاملُ للتوجيهِ في [`evidence/W-610/ADVISOR_DIRECTIVE_19.md`](evidence/W-610/ADVISOR_DIRECTIVE_19.md)) ⇒ (أ) **الإخلالُ مُقيَّدٌ كما هو**: وثيقةُ التصميمِ وشِفرتُه في الالتزامِ نفسِه `cacd1a7` (W-471) — والمعيارُ (1) لم يتحقق إجرائيًّا · (ب) تجاوزُه **لـWI-096 وحدَه** · (ج) **للبنودِ القادمةِ**: التصميمُ في التزامٍ مستقلٍّ يسبقُ الشِّفرةَ · (د) تُعادُ جولةُ WI-096 بمسبارِ كلِّ مقعدٍ (§ 4.9) — لا VERIFIED قبلَها.
=== RAW [20] END ===
=== RAW [21] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && sha256sum docs/audit/evidence/W-641/briefs_wi111/briefing_grok_4_7.md
EXIT: 0
BYTES: 126
SHA256: c5eb2c4fe773a210740e8e66577a5f1e4503df50f4b4a9cdf013e4e8098aa8a8
NO_EOL: 0
--- OUTPUT ---
c9fd7e1bba984b8d0b38db1e2d2a8bc460bf0616c26814cc311858b719c4d873  docs/audit/evidence/W-641/briefs_wi111/briefing_grok_4_7.md
=== RAW [21] END ===
=== RAW [22] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-641/briefs_wi111/SHA256SUMS
EXIT: 0
BYTES: 268
SHA256: 585da634b1b55765e4adf708233a64597da9c4b56bc7dcba43b36d917cc8166b
NO_EOL: 0
--- OUTPUT ---
6ea96c050cf50154b87c488e47355daa736ca3bf19c27bec5c10cebff5b28700  briefing_gemini_3_8_flash.md
c9fd7e1bba984b8d0b38db1e2d2a8bc460bf0616c26814cc311858b719c4d873  briefing_grok_4_7.md
7b8c6b3eb272823cdf61e41bf86f3f9291787ab18823823b7cf825e219241129  briefing_kimi_k3.md
=== RAW [22] END ===
=== RAW [23] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py tests/governance/test_step7_factory_surfaces.py -q
EXIT: 0
BYTES: 110
SHA256: 6eb26269770bc40e2cad8e85188fe801e3e6488f0644e95e5dad124400f31896
NO_EOL: 0
--- OUTPUT ---
........................................................................ [100%]
72 passed in 93.54s (0:01:33)
=== RAW [23] END ===
=== RAW [24] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
EXIT: 0
BYTES: 319
SHA256: e237b66d4e4686ec1d76c273157268e76598e93fa5418cfa9090f52a8c38efd9
NO_EOL: 0
--- OUTPUT ---
عقدُ نَسَبِ القياساتِ مستقيمٌ: 11 قياسًا مقيَّدًا · 8 محروسًا (‏منها 1 برباطٍ مقيسٍ نصًّا) · 3 مُعلَنًا بسببٍ مكتوبٍ. ومُؤَجَّلٌ إلى الشطرِ الآخرِ: 2 (‏من 2 يحتاجُ حزمًا خارجيّةً).
=== RAW [24] END ===
=== RAW [25] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w641/grok_4_7/wi111/probe/wi111_break_judiciary.py
EXIT: 0
BYTES: 12259
SHA256: e1406f55d906833e4408c2da7230d7ee693d652a47e3d1629a38ba35f9882bff
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ مقعدِ grok_4_7 لـWI-111 — يحاولُ كسرَ حصرِ الأفعالِ العشرةِ وعبورِ الأسطحِ.
     3	
     4	ليس فحصًا قائمًا ولا أمرًا من القسمِ ج. ينادي FederalJudiciary وأسطحَ docket/rulings.
     5	"""
     6	from __future__ import annotations
     7	
     8	import os
     9	import sys
    10	from pathlib import Path
    11	
    12	ROOT = Path("/home/user/workspace/council_w641/grok_4_7/wi111")
    13	REPO = ROOT / "repo"
    14	SERVICES = REPO / "federal/executive/services"
    15	os.environ["AMOS_DATABASE_URL"] = f"sqlite:////{ROOT / 'tmp' / 'amos_probe_wi111.db'}"
    16	os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = str(ROOT / "tmp" / "wi111_probe_idempotency.json")
    17	sys.path.insert(0, str(REPO))
    18	sys.path.insert(0, str(SERVICES / "src"))
    19	sys.path.insert(0, str(SERVICES))
    20	
    21	from core.constitutional_engine.engine import ConstitutionalEngine
    22	from core.constitutional_engine.model import ActionRequest, Branch
    23	from core.constitutional_engine.rules import JUDICIAL_ACTIONS as ENGINE_VERBS
    24	from core.sovereignty.compensation import CompensationRequired
    25	from core.sovereignty.gateway import SovereigntyViolation
    26	from core.sovereignty.jurisdiction import JUDICIAL_ACTIONS as WALL_VERBS
    27	from amos_federation.services.federal_judiciary import docket as docket_module
    28	from amos_federation.services.federal_judiciary import rulings as rulings_module
    29	from amos_federation.services.federal_judiciary.models import CasePartyModel, LegalCaseModel
    30	import tests.test_wi105_issue_ruling_sovereign as j1
    31	
    32	TEN = (
    33	    "refer_case",
    34	    "admit_case",
    35	    "vacate_ruling",
    36	    "admit_evidence",
    37	    "recuse_judge",
    38	    "register_judgment",
    39	    "assign_case",
    40	    "record_proceeding",
    41	    "join_party",
    42	    "admit_claim",
    43	)
    44	DEFERRED = ("establish_court", "set_court_status", "appoint_judge", "submit_evidence")
    45	
    46	
    47	def main() -> int:
    48	    held: list[str] = []
    49	    broken: list[str] = []
    50	    engine = ConstitutionalEngine()
    51	
    52	    def decide(actor: str, verb: str) -> tuple[str, list[str]]:
    53	        verdict = engine.evaluate(ActionRequest(actor=Branch[actor], action=verb, target="wi111/seat-probe"))
    54	        decision = getattr(verdict, "decision", verdict)
    55	        rules = [str(getattr(v, "rule_id", v)) for v in getattr(verdict, "violations", []) or []]
    56	        return str(getattr(decision, "name", decision)), rules
    57	
    58	    denied = 0
    59	    for verb in TEN:
    60	        for actor in ("EXECUTIVE", "LEGISLATIVE"):
    61	            decision, rules = decide(actor, verb)
    62	            if decision == "DENY" and "R-003-1" in rules:
    63	                denied += 1
    64	            else:
    65	                broken.append(f"engine: {actor} {verb} → {decision} {rules}")
    66	        if decide("JUDICIAL", verb)[0] != "ALLOW":
    67	            broken.append(f"engine: JUDICIAL {verb} ليس ALLOW")
    68	    if denied == 20:
    69	        held.append("engine: العشرةُ DENY لغيرِ القضاءِ بـR-003-1 ومنها join_party وadmit_claim")
    70	
    71	    leaked = [verb for verb in DEFERRED if verb in ENGINE_VERBS or verb in WALL_VERBS]
    72	    if leaked:
    73	        broken.append(f"lexicon: فعلٌ مؤجَّلٌ دخلَ المعجمَ {leaked}")
    74	    else:
    75	        held.append("lexicon: الأفعالُ الأربعةُ المؤجَّلةُ غائبةٌ عن معجمِ المُحرِّكِ والجدار")
    76	
    77	    fresh = getattr(j1._fresh_state, "__wrapped__", None)
    78	    if fresh is None:
    79	        raise RuntimeError("تعذّرَ نزعُ غلافِ تجهيزِ القاعدة")
    80	    fresh()
    81	    rulings_module.reset_judiciary_authorizer()
    82	    registry = j1.get_state_registry()
    83	    national = j1.get_national_registry()
    84	    judiciary = j1.get_federal_judiciary()
    85	    crown = j1._context("king", username="crown-probe")
    86	    crown_identity = national.create_identity(context=crown, identity_type="PERSON", label="التاج")
    87	    national.link_principal(context=crown, principal_id=crown.principal_id, identity_id=crown_identity["id"])
    88	    judge_ctx = j1._context("official", username="judge-probe")
    89	    bench = j1._bench(registry, national, judiciary, crown, judge_ctx)
    90	    filer = j1._context("official", username="filer-probe")
    91	    party = j1._party_identity(national, crown, filer)
    92	
    93	    opened = judiciary.open_case(
    94	        context=filer,
    95	        court_id=bench.court["id"],
    96	        case_type="CIVIL",
    97	        subject="مسبارُ مقعدٍ",
    98	        reference=j1._code("P111"),
    99	    )
   100	    filed = judiciary.file_case(context=filer, case_id=opened["id"])
   101	    if filed.get("status") != "filed":
   102	        broken.append(f"file_case: الحالةُ {filed.get('status')} لا filed")
   103	    else:
   104	        held.append("file_case: عبورٌ إنتاجيٌّ إلى filed")
   105	
   106	    rulings_module.JUDICIARY_ACTOR = "LEGISLATIVE"
   107	    rulings_module.reset_judiciary_authorizer()
   108	    session = j1._session()
   109	    try:
   110	        parties_before = session.query(CasePartyModel).count()
   111	    finally:
   112	        session.close()
   113	    try:
   114	        judiciary.add_party(
   115	            context=filer,
   116	            case_id=opened["id"],
   117	            party_role="PLAINTIFF",
   118	            identity_id=party["id"],
   119	        )
   120	    except SovereigntyViolation:
   121	        session = j1._session()
   122	        try:
   123	            parties_after = session.query(CasePartyModel).count()
   124	        finally:
   125	            session.close()
   126	        if parties_after == parties_before:
   127	            held.append("add_party: فاعلٌ تشريعيٌّ رُفِضَ ولم يُكتَب طرفٌ")
   128	        else:
   129	            broken.append("add_party: رُفِضَ التشريعيُّ لكنَّ صفَّ الطرفِ كُتِب")
   130	    except Exception as exc:
   131	        broken.append(f"add_party: استثناءٌ غيرُ SovereigntyViolation {type(exc).__name__}: {exc}")
   132	    else:
   133	        broken.append("add_party: فاعلٌ تشريعيٌّ مرَّ بـjoin_party")
   134	
   135	    rulings_module.JUDICIARY_ACTOR = "EXECUTIVE"
   136	    rulings_module.reset_judiciary_authorizer()
   137	    try:
   138	        judiciary.assign_case(context=crown, case_id=opened["id"], judge_id=bench.judge["id"])
   139	    except SovereigntyViolation:
   140	        session = j1._session()
   141	        try:
   142	            row = session.get(LegalCaseModel, opened["id"])
   143	            still_filed = row is not None and row.status == "filed" and row.assigned_judge_id is None
   144	        finally:
   145	            session.close()
   146	        if still_filed:
   147	            held.append("assign_case: فاعلٌ تنفيذيٌّ رُفِضَ والحالةُ filed")
   148	        else:
   149	            broken.append("assign_case: رُفِضَ التنفيذيُّ لكنَّ الإسنادَ كُتِب")
   150	    except Exception as exc:
   151	        broken.append(f"assign_case: استثناءٌ غيرُ SovereigntyViolation {type(exc).__name__}: {exc}")
   152	    else:
   153	        broken.append("assign_case: فاعلٌ تنفيذيٌّ مرَّ")
   154	
   155	    rulings_module.JUDICIARY_ACTOR = "JUDICIAL"
   156	    rulings_module.reset_judiciary_authorizer()
   157	    auth = rulings_module._judiciary_authorizer()
   158	    depth = {"n": 0, "max": 0}
   159	    original_guard = auth.guard_declared
   160	
   161	    def _counting_guard(action: str, target: str, **kwargs):
   162	        depth["n"] += 1
   163	        depth["max"] = max(depth["max"], depth["n"])
   164	        try:
   165	            return original_guard(action, target, **kwargs)
   166	        finally:
   167	            depth["n"] -= 1
   168	
   169	    auth.guard_declared = _counting_guard
   170	    second = judiciary.open_case(
   171	        context=filer,
   172	        court_id=bench.court["id"],
   173	        case_type="CIVIL",
   174	        subject="عمقُ العبور",
   175	        reference=j1._code("P111N"),
   176	    )
   177	    judiciary.file_case(context=filer, case_id=second["id"])
   178	    if depth["max"] == 1 and depth["n"] == 0:
   179	        held.append("nested: file_case عبرَ مرّةً واحدةً لا داخلَ عبورٍ")
   180	    else:
   181	        broken.append(f"nested: max_depth={depth['max']} leftover={depth['n']}")
   182	    auth.guard_declared = original_guard
   183	
   184	    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
   185	    original_mark = type(ledger).mark_succeeded
   186	
   187	    def _failing_mark(*args, **kwargs):
   188	        raise RuntimeError("تثبيتُ النجاحِ مُسقَطٌ — مسبارُ WI-111")
   189	
   190	    type(ledger).mark_succeeded = _failing_mark
   191	    try:
   192	        judiciary.assign_case(context=crown, case_id=opened["id"], judge_id=bench.judge["id"])
   193	    except CompensationRequired as exc:
   194	        clean = exc.outcome.state_is_clean
   195	        session = j1._session()
   196	        try:
   197	            row = session.get(LegalCaseModel, opened["id"])
   198	            restored = row is not None and row.status == "filed" and row.assigned_judge_id is None
   199	        finally:
   200	            session.close()
   201	        if clean and restored:
   202	            held.append("compensate: فشلُ التثبيتِ بعدَ assign_case استعادَ filed بلا قاضٍ")
   203	        else:
   204	            broken.append(f"compensate: clean={clean} restored={restored}")
   205	    except Exception as exc:
   206	        broken.append(f"compensate: استثناءٌ غيرُ CompensationRequired {type(exc).__name__}: {exc}")
   207	    else:
   208	        broken.append("compensate: assign_case نجحَ رغمَ إسقاطِ التثبيت")
   209	    finally:
   210	        type(ledger).mark_succeeded = original_mark
   211	
   212	    reference = j1._code("P111D")
   213	    wiped = judiciary.open_case(
   214	        context=filer,
   215	        court_id=bench.court["id"],
   216	        case_type="CIVIL",
   217	        subject="حذفٌ خارجَ الواجهة",
   218	        reference=reference,
   219	    )
   220	    session = j1._session()
   221	    try:
   222	        row = session.get(LegalCaseModel, wiped["id"])
   223	        session.delete(row)
   224	        session.commit()
   225	    finally:
   226	        session.close()
   227	    try:
   228	        judiciary.open_case(
   229	            context=filer,
   230	            court_id=bench.court["id"],
   231	            case_type="CIVIL",
   232	            subject="حذفٌ خارجَ الواجهة",
   233	            reference=reference,
   234	        )
   235	    except docket_module.JudicialLedgerDivergenceError:
   236	        held.append("replay: إعادةُ قضيّةٍ محذوفةٍ تفرُّقٌ لا نجاح")
   237	    except Exception as exc:
   238	        broken.append(f"replay: استثناءٌ غيرُ التفرُّق {type(exc).__name__}: {exc}")
   239	    else:
   240	        broken.append("replay: إعادةٌ نجحت لقضيّةٍ محذوفة")
   241	
   242	    print(f"HELD={len(held)} BROKEN={len(broken)}")
   243	    for item in held:
   244	        print(f"HELD {item}")
   245	    for item in broken:
   246	        print(f"BROKEN {item}")
   247	    if broken:
   248	        print("PROPERTY_BROKEN")
   249	        return 1
   250	    print("PROPERTY_HELD")
   251	    return 0
   252	
   253	
   254	if __name__ == "__main__":
   255	    raise SystemExit(main())
=== RAW [25] END ===
=== RAW [26] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python /home/user/workspace/council_w641/grok_4_7/wi111/probe/wi111_break_judiciary.py
EXIT: 0
BYTES: 763
SHA256: b5cd38a13b059519e692cf5e972ddeecdf90f645d4eff13fa571e5666fcfda16
NO_EOL: 0
--- OUTPUT ---
HELD=8 BROKEN=0
HELD engine: العشرةُ DENY لغيرِ القضاءِ بـR-003-1 ومنها join_party وadmit_claim
HELD lexicon: الأفعالُ الأربعةُ المؤجَّلةُ غائبةٌ عن معجمِ المُحرِّكِ والجدار
HELD file_case: عبورٌ إنتاجيٌّ إلى filed
HELD add_party: فاعلٌ تشريعيٌّ رُفِضَ ولم يُكتَب طرفٌ
HELD assign_case: فاعلٌ تنفيذيٌّ رُفِضَ والحالةُ filed
HELD nested: file_case عبرَ مرّةً واحدةً لا داخلَ عبورٍ
HELD compensate: فشلُ التثبيتِ بعدَ assign_case استعادَ filed بلا قاضٍ
HELD replay: إعادةُ قضيّةٍ محذوفةٍ تفرُّقٌ لا نجاح
PROPERTY_HELD
=== RAW [26] END ===
VERDICT_PER_CRITERION: (1) نعم — الكتلة 7: ملحقُ التصميمِ في d6963e68 (W-638 · 2026-10-23T22:59:40Z) قبلَ شِفرةِ 4247c68f (W-640 · 2026-10-23T23:56:33Z). والكتلة 4: فرقُ الشِّفرةِ بينَ 4247c68 وHEAD فارغٌ. والكتلة 6: ما بعدَ الشِّفرةِ قيدُ توثيقِ W-641 وحدَه. (2) نعم — الكتلة 17: الدَّينُ 157←142 والسياديُّ 42←46 والمواضعُ 246←239، والكتلة 11 تطابقُ البعدَ حيًّا (142 / 46 / 239). وservice.py خرجَ من قائمةِ الدَّينِ (كانَ 17) وdocket.py من 5 إلى 1. والكتلة 12: 21 passed ومنها جردُ الأسطحِ المحسومةِ بلا دَين. والسياديُّ 46 لا 53 إفصاحٌ مقيسٌ لا كسرٌ (الجردُ أعمى عنِ التفويض). (3) نعم — الكتلة 15: التنفيذيُّ والتشريعيُّ DENY بـR-003-1 على ثمانيةٍ منَ العشرةِ التي يحملُها مسبارُ البوّابة، والكتلة 12 تغطّي العشرةَ كلَّها في T1 (21 passed)، والكتلة 26 تؤكّدُ join_party وadmit_claim معَ الثمانية. وALLOW للتاجِ أثرُ تاجٍ استشاريٌّ على R-003-1 لا مرورُ فرعٍ. (4) نعم — الكتلة 12 خضراءُ وفيها منعُ العبورِ المتداخل، والكتلة 19: M5 قُتِلَ بفحصِ التداخل، والكتلة 26: file_case عبرَ مرّةً واحدةً (max_depth=1). (5) نعم — الكتلة 19: M1–M5 KILLED والأصلُ مستعادٌ (BASELINE_RESTORED). (6) نعم — الكتلة 14: 1523 passed و53 skipped وexit 0. والكتلة 5: جذرٌ 2722 passed و1 skipped. والكتلة 13: 37 passed. وتعديلُ test_wi105 في الكتلة 9 يرشّحُ عبوراتِ issue_ruling وحدَها ويبقي قيدَ سجلِّ البوّابةِ في T5 — لم يُضعِفِ الفحصَ.
PROBES: مسبارُ wi111_break_judiciary.py · كتلةُ الشِّفرةِ 25 · كتلةُ التشغيلِ 26 · الخاصيّةُ: الأسطحُ الإنتاجيّةُ تعبرُ بفاعلِ الوحدةِ القضائيِّ، والعشرةُ DENY لغيرِ القضاءِ بـR-003-1 ومنها join_party وadmit_claim، ولا عبورَ داخلَ عبورٍ، وفشلُ التثبيتِ يُعوَّض، وإعادةُ قضيّةٍ محذوفةٍ تفرُّقٌ لا نجاح، والفعلُ المؤجَّلُ لم يدخلِ المعجمَ — حاولَ كسرَها بفاعلٍ تشريعيٍّ على add_party وتنفيذيٍّ على assign_case وبإسقاطِ التثبيتِ وبحذفِ الصفِّ خارجَ الواجهة · انكسرت؟ لا
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — لم أقرأْ للحكمِ شيئًا خارجَ استنساخِي /home/user/workspace/council_w641/grok_4_7/wi111/repo وهذهِ الإحاطةِ. استثناءٌ: أثناءَ انتظارِ الأوامرِ الطويلةِ ظهرَ في قائمةِ عمليّاتِ النظامِ سطرُ أمرِ مقاعدَ أخرى؛ لم أفتحْ ملفّاتِها ولا أحكامَها ولم أستعملْ مخرجَها.
VERDICT: PASS
