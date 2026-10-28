# حكمُ مقعدِ المجلسِ — grok_4_7 · جولةُ WI-117 (W-710)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في الجولةِ الواحدةِ (قرارُ المالكِ D27) على WI-117 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w701/grok_4_7/wi117) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `20c7cc97cc8aa7094ddae6c915c2d7d734cde75bc2d5cdbf1811b8b1d929e075`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-117 عندَ العقدةِ `147a0c6b1357ddf0a93ba1c4d16e82e8648cb247` — إحاطةٌ مبصومةٌ (W-701) ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9) · ومخرجاتُ الفاحصِ منَ المنسِّقِ مقروءةٌ مقبولةً EXIT 0 (raw_check_outputs.txt في قيدِ W-710). تحصينُ مساراتِ الخفضِ والترقيةِ والبوّابةِ بـrequire_king (D25-2) — البندُ كاملًا.

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
RUN_DATE: 2026-10-28 06:21 +00:00
NODE: 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
CLONE_PATH: /home/user/workspace/council_w701/grok_4_7/wi117/repo — أمرُ الاستنساخِ: git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w701/grok_4_7/wi117/repo ثمَّ bash tools/dev/bootstrap.sh داخلَ المستنسخِ
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/
 2. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/)
 3. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
 5. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git show --stat f8d33807
 6. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git diff f8d33807^ f8d33807 -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
 7. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && rg -n "require_king" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py
 8. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 9. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py
 10. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && rm -rf ../old && git worktree add --detach ../old f8d33807^ && cp federal/executive/services/tests/test_wi117_king_guard_routes.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 11. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && sed -i "s/Depends(require_king)/Depends(require_auth)/g" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 12. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && git status --short && git diff --stat
 13. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && rg -n "D25-2|require_king" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 14. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && sha256sum docs/audit/evidence/W-701/briefs_wi117/briefing_grok_4_7.md
 15. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && cat docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS
 16. nl -ba /home/user/workspace/council_w701/grok_4_7/wi117/probe/wi117_http_probe.py
 17. /home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/bin/python /home/user/workspace/council_w701/grok_4_7/wi117/probe/wi117_http_probe.py
 18. cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && rg -n -A 12 -H "def test_reset_kill_switch|def test_create_promotion|def test_check_gate_passed|def test_check_gate_failed_stops_promotion|def test_all_gates_passed_promotes|def test_kill_switch_reset\(" federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/)
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
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 0
BYTES: 2109
SHA256: 7ce0faf53d4fabe03a3052b77c751ce6991dc9576aa436f7c577f8c2cf5a0ac2
NO_EOL: 0
--- OUTPUT ---
e15e5b82 2026-10-26T10:33:12Z W-690: تصحيحٌ مؤرَّخٌ لحمرةِ lint على رأسِ PR #162 — تنسيقُ 3 ملفاتِ فحصٍ بـruff format (تنسيقٌ لا تغييرَ في المضمونِ · 65 فحصًا خضراءَ بعدَه) · لا انتقالَ حالةٍ · سابقةُ W-676/W-686 · المنسِّقُ GLM-5.3 (Perplexity Computer)
f8d33807 2026-10-26T10:15:25Z W-689: شِفرةُ تحصينِ WI-117 — require_king على المساراتِ الأربعةِ (reset ×2 · promotions · gates) + تحصينُ sign_approval (الموقِّعُ هويةُ الرمزِ لا جسمَ الطلبِ) + 13 فحصًا + طفرةٌ مقتولةٌ + مسبارُ HTTP حقيقيٌّ (مواطنٌ ⇒ 403 ×5 والمستوى halt والملكُ 200) · انتقالٌ واحدٌ: IN_PROGRESS→IN_REVIEW · D-4: تصحيحٌ لا حرقٌ · المنسِّقُ GLM-5.3 (Perplexity Computer)
f4df92e2 2026-08-16T20:50:29Z R4: توحيد هوية الوكيل والسجل والسكّان — مصدر حقيقة واحد وإسقاط سكّاني
93c524db 2026-08-15T07:44:23Z chore: fix CI, identity checks, and code formatting
3f601e7b 2026-08-15T04:46:17Z Phase 11: Full population expansion + universities + retirement (v1.0 roadmap)
08b46ae9 2026-08-15T04:37:44Z Phase 10: Federal Treasury + amos-credit digital currency (v1.0 roadmap)
6c97d476 2026-08-15T04:29:38Z Phase 9: Federal institutions + complete governance (v1.0 roadmap)
f1816aef 2026-08-15T04:20:45Z Phase 8: Agent Health System + PostgreSQL (v1.0 roadmap)
858cc365 2026-08-15T03:49:52Z Phase 7: Control Console — human control surface (v1.0 roadmap)
5bd8f75b 2026-08-15T03:39:44Z Phase 3: Foundational governance (v1.0 roadmap)
bc573e24 2026-08-15T03:37:14Z Phase 2: Event bus / nervous system (v1.0 roadmap)
5597816d 2026-08-15T03:34:39Z Phase 1: Persistent memory (v1.0 roadmap)
5052d4ba 2026-08-15T01:57:01Z Phase 6: Governance + Canary
21bfaecb 2026-08-15T03:39:37+03:00 feat(services): تنفيذ هياكل الخدمات التسعة + مصادقة JWT + بوابة المهام والمنسق
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git show --stat f8d33807
EXIT: 0
BYTES: 2051
SHA256: 6838873fa7af86690eb5a1b8deb32288c24cb6053a43bccc223c96427c8a8b26
NO_EOL: 0
--- OUTPUT ---
commit f8d338077f7450a89dfe01a060dbf0e452dee7e8
Author: vooovg-ui <326082239+vooovg-ui@users.noreply.github.com>
Date:   Mon Oct 26 10:15:25 2026 +0000

    W-689: شِفرةُ تحصينِ WI-117 — require_king على المساراتِ الأربعةِ (reset ×2 · promotions · gates) + تحصينُ sign_approval (الموقِّعُ هويةُ الرمزِ لا جسمَ الطلبِ) + 13 فحصًا + طفرةٌ مقتولةٌ + مسبارُ HTTP حقيقيٌّ (مواطنٌ ⇒ 403 ×5 والمستوى halt والملكُ 200) · انتقالٌ واحدٌ: IN_PROGRESS→IN_REVIEW · D-4: تصحيحٌ لا حرقٌ · المنسِّقُ GLM-5.3 (Perplexity Computer)

 PROJECT_STATE.md                                   |   3 +-
 docs/PROJECT_HANDBOOK.md                           |   7 +-
 docs/audit/ACTIVE_EXECUTION_STATE.md               |   1 +
 docs/audit/COMPLETION_LEDGER.md                    |   3 +
 docs/audit/TRUTH_MATRIX.md                         |   4 +-
 docs/audit/evidence/W-689/README.md                |  45 ++++
 docs/audit/evidence/W-689/http_probe.py            | 247 +++++++++++++++++++++
 docs/audit/evidence/W-689/http_probe_raw.txt       |  56 +++++
 docs/audit/evidence/W-689/mutations/README.md      |  40 ++++
 .../W-689/mutations/after_restore_output.txt       |   2 +
 .../W-689/mutations/m1_guard_dropped_exit.txt      |   1 +
 .../W-689/mutations/m1_guard_dropped_output.txt    |   6 +
 .../evidence/W-689/mutations/mutation_log.txt      |  11 +
 docs/audit/truth_matrix.json                       |  10 +-
 docs/governance/work/ACTIVE_WORK.md                |  12 +-
 .../services/control_console/main.py               |  20 +-
 .../amos_federation/services/governance/main.py    |   8 +-
 federal/executive/services/tests/per_test_auth.py  |  10 +-
 .../services/tests/test_control_console.py         |  61 ++++-
 .../executive/services/tests/test_governance.py    |  42 ++--
 .../services/tests/test_wi117_king_guard_routes.py | 126 +++++++++++
 21 files changed, 656 insertions(+), 59 deletions(-)
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git diff f8d33807^ f8d33807 -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 0
BYTES: 11142
SHA256: 6d6ae188d537f82768f59de885839557d7722b04f8adda376fe0dd7ae12ef707
NO_EOL: 0
--- OUTPUT ---
diff --git a/federal/executive/services/src/amos_federation/services/control_console/main.py b/federal/executive/services/src/amos_federation/services/control_console/main.py
index 275eeceb..fb1dd026 100644
--- a/federal/executive/services/src/amos_federation/services/control_console/main.py
+++ b/federal/executive/services/src/amos_federation/services/control_console/main.py
@@ -12,7 +12,7 @@ from fastapi import APIRouter, Depends, HTTPException, Query
 from fastapi.responses import HTMLResponse
 from pydantic import BaseModel, Field
 
-from amos_federation.common.auth import require_auth
+from amos_federation.common.auth import require_auth, require_king
 from amos_federation.common.registry import SERVICES
 from amos_federation.common.service import create_service_app
 
@@ -208,9 +208,9 @@ async def activate_kill_switch(
 
 @router.post("/kill-switch/reset", response_model=dict)
 async def reset_kill_switch(
-    _: Annotated[dict[str, object], Depends(require_auth)],
+    _: Annotated[dict[str, object], Depends(require_king)],
 ) -> dict[str, Any]:
-    """إعادة ضبط Kill Switch."""
+    """إعادة ضبط Kill Switch (حارسٌ ملكيٌّ — WI-117)."""
     from amos_federation.services.governance.canary import reset_kill_switch
 
     return reset_kill_switch()
@@ -220,10 +220,9 @@ async def reset_kill_switch(
 
 
 class ApprovalRequest(BaseModel):
-    """طلب موافقة/رفض."""
+    """طلب موافقة/رفض — الموقِّعُ هويةُ الرمزِ الملكيِّ لا جسمَ الطلبِ (WI-117)."""
 
     decision: str = Field(pattern="^(approve|reject)$")
-    signed_by: str = Field(min_length=1)
     model_id: str | None = None
     notes: str = ""
 
@@ -231,28 +230,29 @@ class ApprovalRequest(BaseModel):
 @router.post("/approval", response_model=dict)
 async def sign_approval(
     request: ApprovalRequest,
-    _: Annotated[dict[str, object], Depends(require_auth)],
+    token_data: Annotated[dict[str, object], Depends(require_king)],
 ) -> dict[str, Any]:
-    """7.5: زر الموافقة/الرفض — يُفعّل فعليًا في المرحلة 9 مع توقيع Ed25519."""
+    """7.5: زر الموافقة/الرفض — يُفعّل فعليًا في المرحلة 9 مع توقيع Ed25519 (حارسٌ ملكيٌّ — WI-117)."""
     from amos_federation.common.event_bus import get_event_bus
     from amos_federation.common.persistent import PersistentAuditStore
 
+    signer = str(token_data["sub"])
     approval_id = f"approval-{__import__('uuid').uuid4().hex[:8]}"
     result = {
         "approval_id": approval_id,
         "decision": request.decision,
-        "signed_by": request.signed_by,
+        "signed_by": signer,
         "model_id": request.model_id,
         "notes": request.notes,
         "signature_pending": True,  # سيُوقّع بـ Ed25519 في المرحلة 9
     }
-    PersistentAuditStore().append("approval.signed", request.signed_by, result)
+    PersistentAuditStore().append("approval.signed", signer, result)
     get_event_bus().publish(
         "amos_federation.approval.signed",
         {
             "approval_id": approval_id,
             "decision": request.decision,
-            "signed_by": request.signed_by,
+            "signed_by": signer,
         },
     )
     return result
diff --git a/federal/executive/services/src/amos_federation/services/governance/main.py b/federal/executive/services/src/amos_federation/services/governance/main.py
index b9ea1cb0..0e1c453e 100644
--- a/federal/executive/services/src/amos_federation/services/governance/main.py
+++ b/federal/executive/services/src/amos_federation/services/governance/main.py
@@ -11,7 +11,7 @@ from typing import Annotated, Any
 from fastapi import APIRouter, Depends, HTTPException, Query, status
 from pydantic import BaseModel, Field
 
-from amos_federation.common.auth import require_auth
+from amos_federation.common.auth import require_auth, require_king
 from amos_federation.common.persistent import PersistentAuditStore
 from amos_federation.common.registry import SERVICES
 from amos_federation.common.service import create_service_app
@@ -146,7 +146,7 @@ async def activate_kill_switch(
 
 @router.post("/system/kill-switch/reset", response_model=dict)
 async def reset_kill_switch_endpoint(
-    _: Annotated[dict[str, object], Depends(require_auth)],
+    _: Annotated[dict[str, object], Depends(require_king)],
 ) -> dict[str, Any]:
     """إعادة ضبط مفتاح الإيقاف."""
     result = reset_kill_switch()
@@ -167,7 +167,7 @@ def _activate_kill_switch_safe(level: str, reason: str, activated_by: str) -> di
 @router.post("/promotions", response_model=dict, status_code=status.HTTP_201_CREATED)
 async def create_promotion_endpoint(
     request: PromotionCreateRequest,
-    _: Annotated[dict[str, object], Depends(require_auth)],
+    _: Annotated[dict[str, object], Depends(require_king)],
 ) -> dict[str, Any]:
     """إنشاء طلب ترقية نموذج بـ 5 بوابات."""
     promo = create_promotion(request.model_id)
@@ -200,7 +200,7 @@ async def get_promotion_endpoint(
 async def check_gate_endpoint(
     promotion_id: str,
     request: GateCheckRequest,
-    _: Annotated[dict[str, object], Depends(require_auth)],
+    _: Annotated[dict[str, object], Depends(require_king)],
 ) -> dict[str, Any]:
     """فحص بوابة ترقية."""
     try:
diff --git a/federal/executive/services/tests/test_wi117_king_guard_routes.py b/federal/executive/services/tests/test_wi117_king_guard_routes.py
new file mode 100644
index 00000000..fdde0a31
--- /dev/null
+++ b/federal/executive/services/tests/test_wi117_king_guard_routes.py
@@ -0,0 +1,126 @@
+"""
+فحوصُ WI-117 — حارسُ `require_king` على المساراتِ الخمسةِ (W-689)
+الهدف: إثباتُ أنَّ رفعَ زرِّ التوقّفِ (الخدمتَينِ) وإنشاءَ الترقيةِ وفحصَ البوّابةِ وتوقيعَ
+    الموافقةِ لا يعبُرُها إلّا رمزٌ ملكيٌّ — فالمواطنُ يُصدُّ (403) والملكُ يمرُّ، وأنَّ
+    الموقِّعَ في الموافقةِ هويةُ الرمزِ لا جسمَ الطلبِ.
+النطاق: المساراتُ الخمسةُ المحروسةُ حصرًا (governance: reset/promotions/gates ·
+    control_console: reset/approval) — «التفعيلُ» يبقى بنصِّ D25-2 (W-675/WI-114).
+المالك: Perplexity Computer (WI-117 · المنسِّقُ GLM-5.3 · تصميمُ W-687)
+تاريخ الإنشاء: 2026-10-26
+"""
+
+from __future__ import annotations
+
+from fastapi.testclient import TestClient
+
+from amos_federation.services.control_console.main import app as console_app
+from amos_federation.services.governance.main import app as governance_app
+
+from .per_test_auth import PerTestAuthHeaders
+
+governance_client = TestClient(governance_app)
+console_client = TestClient(console_app)
+
+CITIZEN = PerTestAuthHeaders("wi117-citizen", ["governance:read", "governance:write"])
+KING = PerTestAuthHeaders("king", ["governance:read", "governance:write"], role="king")
+
+
+def test_governance_reset_citizen_forbidden() -> None:
+    """مواطنٌ لا يرفعُ زرَّ التوقّفِ من خدمةِ الحوكمةِ (WI-117)."""
+    resp = governance_client.post("/v1/system/kill-switch/reset", headers=CITIZEN)
+    assert resp.status_code == 403
+
+
+def test_governance_reset_king_allowed() -> None:
+    """الملكُ يرفعُ زرَّ التوقّفِ من خدمةِ الحوكمةِ (WI-117)."""
+    governance_client.post(
+        "/v1/system/kill-switch",
+        headers=CITIZEN,
+        json={"level": "alert", "reason": "wi117", "activated_by": "tester"},
+    )
+    resp = governance_client.post("/v1/system/kill-switch/reset", headers=KING)
+    assert resp.status_code == 200
+    assert resp.json()["level"] == "normal"
+
+
+def test_governance_promotions_citizen_forbidden() -> None:
+    """مواطنٌ لا يطلبُ ترقيةً (WI-117)."""
+    resp = governance_client.post(
+        "/v1/promotions", headers=CITIZEN, json={"model_id": "wi117-model"}
+    )
+    assert resp.status_code == 403
+
+
+def test_governance_promotions_king_allowed() -> None:
+    """الملكُ يطلبُ ترقيةً (WI-117)."""
+    resp = governance_client.post(
+        "/v1/promotions", headers=KING, json={"model_id": "wi117-model"}
+    )
+    assert resp.status_code == 201
+    assert resp.json()["status"] == "in_progress"
+
+
+def test_governance_gates_citizen_forbidden() -> None:
+    """مواطنٌ لا يفحصُ بوّابةَ ترقيةٍ (WI-117)."""
+    create = governance_client.post(
+        "/v1/promotions", headers=KING, json={"model_id": "wi117-gates"}
+    )
+    promo_id = create.json()["promotion_id"]
+    resp = governance_client.post(
+        f"/v1/promotions/{promo_id}/gates",
+        headers=CITIZEN,
+        json={"gate_name": "evaluation", "passed": True},
+    )
+    assert resp.status_code == 403
+
+
+def test_governance_gates_king_allowed() -> None:
+    """الملكُ يفحصُ بوّابةَ ترقيةٍ (WI-117)."""
+    create = governance_client.post(
+        "/v1/promotions", headers=KING, json={"model_id": "wi117-gates-king"}
+    )
+    promo_id = create.json()["promotion_id"]
+    resp = governance_client.post(
+        f"/v1/promotions/{promo_id}/gates",
+        headers=KING,
+        json={"gate_name": "evaluation", "passed": True},
+    )
+    assert resp.status_code == 200
+    assert resp.json()["gates"]["evaluation"]["status"] == "passed"
+
+
+def test_console_reset_citizen_forbidden() -> None:
+    """مواطنٌ لا يرفعُ زرَّ التوقّفِ من وحدةِ التحكّمِ (WI-117)."""
+    resp = console_client.post("/v1/kill-switch/reset", headers=CITIZEN)
+    assert resp.status_code == 403
+
+
+def test_console_reset_king_allowed() -> None:
+    """الملكُ يرفعُ زرَّ التوقّفِ من وحدةِ التحكّمِ (WI-117)."""
+    console_client.post(
+        "/v1/kill-switch",
+        headers=CITIZEN,
+        json={"level": "alert", "reason": "wi117", "activated_by": "tester"},
+    )
+    resp = console_client.post("/v1/kill-switch/reset", headers=KING)
+    assert resp.status_code == 200
+    assert resp.json()["level"] == "normal"
+
+
+def test_console_approval_citizen_forbidden() -> None:
+    """مواطنٌ لا يوقِّعُ موافقةً من وحدةِ التحكّمِ (WI-117)."""
+    resp = console_client.post(
+        "/v1/approval", headers=CITIZEN, json={"decision": "approve"}
+    )
+    assert resp.status_code == 403
+
+
+def test_console_approval_king_allowed() -> None:
+    """الملكُ يوقِّعُ موافقةً — والموقِّعُ هويةُ الرمزِ لا جسمَ الطلبِ (WI-117)."""
+    resp = console_client.post(
+        "/v1/approval",
+        headers=KING,
+        json={"decision": "approve", "signed_by": "spoofed-user"},
+    )
+    assert resp.status_code == 200
+    assert resp.json()["signed_by"] == "king"
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && rg -n "require_king" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py
EXIT: 0
BYTES: 1009
SHA256: 04f19c9d5832a734eeb1ae226926fe886b00172353e728b2fdc479143e885d4d
NO_EOL: 0
--- OUTPUT ---
federal/executive/services/src/amos_federation/services/control_console/main.py:15:from amos_federation.common.auth import require_auth, require_king
federal/executive/services/src/amos_federation/services/control_console/main.py:211:    _: Annotated[dict[str, object], Depends(require_king)],
federal/executive/services/src/amos_federation/services/control_console/main.py:233:    token_data: Annotated[dict[str, object], Depends(require_king)],
federal/executive/services/src/amos_federation/services/governance/main.py:14:from amos_federation.common.auth import require_auth, require_king
federal/executive/services/src/amos_federation/services/governance/main.py:149:    _: Annotated[dict[str, object], Depends(require_king)],
federal/executive/services/src/amos_federation/services/governance/main.py:170:    _: Annotated[dict[str, object], Depends(require_king)],
federal/executive/services/src/amos_federation/services/governance/main.py:203:    _: Annotated[dict[str, object], Depends(require_king)],
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 0
BYTES: 2384
SHA256: 65fbbdf4a266ee93a9cd2b624ff29e9e987f06c4e11e04a7e3897c1f3b20a15e
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/grok_4_7/wi117/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items

federal/executive/services/tests/test_wi117_king_guard_routes.py ....... [ 70%]
...                                                                      [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 10 passed, 1 warning in 1.21s =========================
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 0.85s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py
EXIT: 0
BYTES: 3027
SHA256: e0f00644422ce5c98d13629b1a0be565a65c3cec1bf69d4bf159bb7e4e67637d
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/grok_4_7/wi117/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 55 items

federal/executive/services/tests/test_governance.py .................... [ 36%]
.......                                                                  [ 49%]
federal/executive/services/tests/test_control_console.py ............... [ 76%]
.............                                                            [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 55 passed, 1 warning in 6.80s =========================
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 4.15s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 0.86s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && rm -rf ../old && git worktree add --detach ../old f8d33807^ && cp federal/executive/services/tests/test_wi117_king_guard_routes.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 2
BYTES: 3016
SHA256: 87515df8ef06ded577b5bbb3273e6c71e236baa6332d878cb51c14ad8c42e50a
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD b7bb6aa6)
HEAD is now at b7bb6aa6 W-688: انتقالُ WI-117 إلى IN_PROGRESS (دفعةٌ ورقيّةٌ تسبقُ دفعةَ الشِّفرةِ مباشرةً · إجراءُ DISC-137) + واجبُ N+1 لدفعةِ W-687 (حكما CI على 735b7631 مقروءانِ أخضرانِ 13/13) + إصلاحُ رابطَي WI-115 المؤجَّلُ (الإفصاحُ (ب) للتوجيهِ 24) · لا شِّفرةَ) · المنسِّقُ GLM-5.3 (Perplexity Computer)
/home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/grok_4_7/wi117/old/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 0 items / 1 error

==================================== ERRORS ====================================
____________ ERROR collecting tests/test_wi117_king_guard_routes.py ____________
federal/executive/services/tests/test_wi117_king_guard_routes.py:25: in <module>
    KING = PerTestAuthHeaders("king", ["governance:read", "governance:write"], role="king")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   TypeError: PerTestAuthHeaders.__init__() got an unexpected keyword argument 'role'
=============================== warnings summary ===============================
../repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
ERROR federal/executive/services/tests/test_wi117_king_guard_routes.py - Type...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.83s ==========================
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && sed -i "s/Depends(require_king)/Depends(require_auth)/g" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 1
BYTES: 4631
SHA256: b4e6be321893cf6d5f942ff4359d52e6494b8c45fedfe75b3cc470d7988dff3b
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/grok_4_7/wi117/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items

federal/executive/services/tests/test_wi117_king_guard_routes.py F.F.F.F [ 70%]
.F.                                                                      [100%]

=================================== FAILURES ===================================
___________________ test_governance_reset_citizen_forbidden ____________________
federal/executive/services/tests/test_wi117_king_guard_routes.py:31: in test_governance_reset_citizen_forbidden
    assert resp.status_code == 403
E   assert 200 == 403
E    +  where 200 = <Response [200 OK]>.status_code
_________________ test_governance_promotions_citizen_forbidden _________________
federal/executive/services/tests/test_wi117_king_guard_routes.py:51: in test_governance_promotions_citizen_forbidden
    assert resp.status_code == 403
E   assert 201 == 403
E    +  where 201 = <Response [201 Created]>.status_code
___________________ test_governance_gates_citizen_forbidden ____________________
federal/executive/services/tests/test_wi117_king_guard_routes.py:72: in test_governance_gates_citizen_forbidden
    assert resp.status_code == 403
E   assert 200 == 403
E    +  where 200 = <Response [200 OK]>.status_code
_____________________ test_console_reset_citizen_forbidden _____________________
federal/executive/services/tests/test_wi117_king_guard_routes.py:93: in test_console_reset_citizen_forbidden
    assert resp.status_code == 403
E   assert 200 == 403
E    +  where 200 = <Response [200 OK]>.status_code
___________________ test_console_approval_citizen_forbidden ____________________
federal/executive/services/tests/test_wi117_king_guard_routes.py:111: in test_console_approval_citizen_forbidden
    assert resp.status_code == 403
E   assert 200 == 403
E    +  where 200 = <Response [200 OK]>.status_code
=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_reset_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_promotions_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_gates_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_console_reset_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_console_approval_citizen_forbidden
==================== 5 failed, 5 passed, 1 warning in 1.14s ====================
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 0.93s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && git status --short && git diff --stat
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && rg -n "D25-2|require_king" docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 0
BYTES: 13643
SHA256: 328358970ec9b5802e827405e7710139e3817e465696e22e1a719f4ba8583abe
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-27 (`W-696` — **Q-73 DECIDED** بأمرِ المالكِ الصريحِ بنصِّهِ الحرفيِّ: «اعتماد تصميم E1 (13 اسمًا)» — تعديلٌ مؤرَّخٌ على القراءةِ الحرفيّةِ لـD21-أ #10: اعتمادُ تصميمِ W-694 بقاموسِهِ الثالثَ عشرَ المعروضِ على المالكِ · التنفيذُ في دفعةِ W-696 تحتَ WI-119) · ووقبله 2026-10-25 (`W-671` — **قراراتُ التوجيهِ 23 DECIDED** بنصوصِها الحرفيّةِ في قيدٍ واحدٍ: D25-1 (canary § 5 الخيارُ 1 `require_king` بشروطِ أ/ب/ج) · D25-2 (تحصينُ مساراتِ الخفضِ والترقيةِ بـ`require_king` — بندُ C3 مستقلٌّ) · D25-3 (ترتيبُ Q-9: الكاشفُ ثمَّ M1) · وWI-112 قيسَ بلا سرٍّ) · ووقبله 2026-10-25 (`W-660` — **قراراتُ التوجيهِ 22 DECIDED** بنصوصِها الحرفيّةِ في قيدٍ واحدٍ: D24-1 (إغلاقُ WI-084) · D24-R2 (الخيارُ 1 بمعيارِ الاستردادِ) · Q-72 (الخيارُ 1) · WI-109 (A1: الخيارُ 4 — أ · ب · هـ · وج ود سؤالانِ) · WI-110 (Q-9: الخيارُ 4) · WI-112 (السرُّ للمالكِ)) · ووقبله ((`W-649` — **D23 DECIDED**: إغلاقُ WI-106 · WI-107 · WI-111 وتصحيحُ خريطةِ أسطرِ WI-084 ثمَّ جولةٌ جديدةٌ (نصُّ المالكِ حرفيًّا)) · ووقبله ((`W-636/W-637` — تسجيلُ WI-109 (تحليلُ A1) · WI-110 (تحليلُ Q-9) · WI-111 (J2+J3 · 15 سطحًا محسومًا مقيسًا) READY · حرسُ D21-د تحتَ WI-040 (`NEW_ITEM_CLAIMING_ENTRY`) · N+1 لـW-631…W-635 أخضرُ (40030379965) · تصحيحُ تاريخِ الرياضِ في D21-هـ) · ووقبله ((`W-632…W-635` — قراراتُ المالكِ بتوجيهِ المستشارِ 21 على ورقةِ D20 بنصوصِها الحرفيّةِ: Q-7 · Q-8 · Q-13 · Q-14 · Q-23 · Q-26 · Q-28 · Q-29 · Q-30 · Q-32 · Q-33 · Q-34 · Q-36 · Q-37 · Q-41 · E1 DECIDED · وA1 وQ-9 وQ-10 تحليلٌ/قياسٌ أوّلًا) · ووقبله (`W-625` — **Q-71 DECIDED** بأمرِ المالكِ الصريحِ: «أذن بـconftest.py تحت WI-107» — قسمةُ نطاقِ مسارِ conftest.py من WI-072 إلى WI-107) · ووقبله (`W-612` — **D17-2** الأربعةُ مؤجَّلةٌ ولا تعطّلُ J2/J3 · **إبلاغُ ما بعدَ الدمجِ** يبقى إبلاغًا (توجيهُ المستشارِ 19 § 1)) · ووقبله ((`W-611` — **Q-61 DECIDED** بالخيارِ (3) بتطبيقٍ صريحٍ على WI-096 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-610` — **D19 DECIDED**: إذنُ المالكِ بإغلاقِ WI-105 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`))))
2361:«سؤال canary § 5 (تمثيل الموافقة البشرية): الخيار 1، رمز الملك (require_king)، بثلاثة شروط: (أ) يُتحقَّق من دور الملك عند المسار نفسه ويُمرَّر دليلًا موسومًا بالمصدر عبر الجسر، لا يُشتق أبدًا من require_auth وحده · (ب) للأفعال ذات criticality="fateful" يبقى التوقيع (human_signature) مطلوبًا كما في rules.py:323؛ والخيار 2 (Ed25519) بند لاحق مستقل · (ج) لم يُقَس أن رمز الملك يحمله إنسان فعلًا؛ يُسجَّل هذا في "ما لم يُقَس" ويُعرض عليّ لا يُفترض.» ⇒ الخيارُ 1 من `docs/audit/A1A_CANARY_CROSSING_DESIGN.md` § 5 بشروطِه الثلاثةِ · والشرطُ (ج) يُسجَّلُ «ما لم يُقَس» في كلِّ تقريرٍ ويُعرَضُ على المالكِ — لا يُفترَض.
2363:### D25-2 · تحصينٌ فوريٌّ لمساراتِ الخفضِ والترقيةِ بـ`require_king` — DECIDED (W-671 · يُسجَّلُ بندًا WI-117 في W-672)
2364:«تحصين فوري للمسارات (مستقل عن العبور): تُقيَّد مسارات الخفض (reset) وإنشاء الترقية وفحص البوابة بـrequire_king (الموجود في auth.py:120) دون انتظار تصميم العبور. تُترك مسارات الرفع (activate) على حالها لأن الرفع هو الاتجاه الآمن. هذا بند C3 مستقل بتصميم قصير ومسبار يشغّل طلب HTTP حقيقيًّا برمز مواطن ويُثبت الرفض، ومطفرة تُسقط القيد.» ⇒ بندُ C3 مستقلٌّ (WI-117) · **قيدُ البوّابةِ:** «يُحجز في هذه الدفعة» ممتنعٌ بحارسِ الانتقالِ الواحدِ (`NEW_ITEM_CLAIMING_ENTRY` — البندُ الجديدُ لا ينتهي نطاقُه في حالةٍ حاجزةٍ) فيُسجَّلُ `READY` هنا ويُحجَزُ في الدفعةِ التاليةِ · والبوّابةُ لا تُعدَّل (DISC-137) · **وقياسٌ يخالفُ مقدّمةَ القرارِ** (يُعرَضُ ولا يُحسَمُ بيدِ المنفِّذِ): مسارُ «الرفعِ» `POST /v1/system/kill-switch` يقبلُ `level="normal"` فيخفضُ halt→normal برمزِ مواطنٍ (طلبُ HTTP حقيقيٌّ · `evidence/W-672/http_probe_before.txt`) — DISC-138 · ووجهتُه WI-114 السطحُ 1 (`A1A_CANARY_CROSSING_DESIGN.md` § 3.3: الخفضُ المُقنَّعُ برفعٍ يُوجَّهُ إلى `lower_kill_switch`) لا توسيعُ D25-2.
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && sha256sum docs/audit/evidence/W-701/briefs_wi117/briefing_grok_4_7.md
EXIT: 0
BYTES: 126
SHA256: 727ef127fc211ceabf78bbb25756b790c660cdfd688efd2fdd8a4b82ebc2aa9b
NO_EOL: 0
--- OUTPUT ---
9a63d6c5c640500fbfe426616c473b1e60e2ce4d6d4f2a4527e85b820b60c1c6  docs/audit/evidence/W-701/briefs_wi117/briefing_grok_4_7.md
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && cat docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS
EXIT: 0
BYTES: 268
SHA256: 2d7a9945c48520a5eea77718a04ea35982c3929f25568efddb042faf4d7f5a2f
NO_EOL: 0
--- OUTPUT ---
33137ced2663e8e935c71f3a14079089acf5b5083c214663dbfa9ca7bffc899c  briefing_gemini_3_8_flash.md
9a63d6c5c640500fbfe426616c473b1e60e2ce4d6d4f2a4527e85b820b60c1c6  briefing_grok_4_7.md
980e4e5bc8432d8df99e02d5abda8fb7e531d65879de66c4705ba608041036db  briefing_kimi_k3.md
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w701/grok_4_7/wi117/probe/wi117_http_probe.py
EXIT: 0
BYTES: 18523
SHA256: 6257983c04146613065013613d919f7ddaeef54cfee383b6e3664d4990f0280b
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ مقعدِ grok_4_7 لـWI-117 — طلباتُ HTTP حقيقيّةٌ عبرَ uvicorn.
     3	
     4	ليسَ أمرًا من أوامرِ الإحاطةِ ولا نسخةً من فحصِ TestClient القائم.
     5	يُقلعُ خدمتَي الحوكمةِ ووحدةِ التحكّمِ كعمليّتَي uvicorn منفصلتَينِ،
     6	ويسكُّ رمزَ مواطنٍ ورمزَ ملكٍ، ثمَّ يثبتُ:
     7	  - رفضَ المواطنِ (403) على المساراتِ الأربعةِ المحروسةِ
     8	  - بقاءَ مستوى زرِّ التوقّفِ كما كان قبلَ كلِّ رفضٍ
     9	  - مرورَ الملكِ على المساراتِ نفسِها
    10	"""
    11	
    12	from __future__ import annotations
    13	
    14	import json
    15	import os
    16	import socket
    17	import subprocess
    18	import sys
    19	import time
    20	import urllib.error
    21	import urllib.request
    22	from pathlib import Path
    23	
    24	REPO = Path("/home/user/workspace/council_w701/grok_4_7/wi117/repo")
    25	PROBE_DIR = Path("/home/user/workspace/council_w701/grok_4_7/wi117/probe")
    26	PY = REPO / ".venv" / "bin" / "python"
    27	DB_PATH = PROBE_DIR / "wi117_seat_http.db"
    28	JWT_SECRET = "grok47-wi117-seat-probe-secret-32b"
    29	
    30	ENV = os.environ.copy()
    31	ENV["AMOS_ENVIRONMENT"] = "test"
    32	ENV["AMOS_DATABASE_URL"] = f"sqlite:///{DB_PATH}"
    33	ENV["AMOS_JWT_SECRET"] = JWT_SECRET
    34	ENV["AMOS_CLAUDE_API_KEY"] = "probe-not-a-real-key"
    35	ENV["AMOS_DB_POOL_SIZE"] = "1"
    36	ENV["AMOS_DB_MAX_OVERFLOW"] = "0"
    37	ENV["OTEL_SDK_DISABLED"] = "true"
    38	
    39	os.environ.update(
    40	    {
    41	        "AMOS_ENVIRONMENT": ENV["AMOS_ENVIRONMENT"],
    42	        "AMOS_DATABASE_URL": ENV["AMOS_DATABASE_URL"],
    43	        "AMOS_JWT_SECRET": ENV["AMOS_JWT_SECRET"],
    44	        "AMOS_CLAUDE_API_KEY": ENV["AMOS_CLAUDE_API_KEY"],
    45	    }
    46	)
    47	
    48	
    49	def _free_port() -> int:
    50	    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    51	        sock.bind(("127.0.0.1", 0))
    52	        return int(sock.getsockname()[1])
    53	
    54	
    55	def _mint(role: str, subject: str) -> str:
    56	    from amos_federation.common.auth import create_access_token
    57	
    58	    return create_access_token(
    59	        subject,
    60	        ["governance:read", "governance:write"],
    61	        tenant_id="federal",
    62	        role=role,
    63	    )
    64	
    65	
    66	def _prepare_database() -> None:
    67	    if DB_PATH.exists():
    68	        DB_PATH.unlink()
    69	    from amos_federation.common.database import init_db, reset_engine
    70	
    71	    init_db()
    72	    reset_engine()
    73	
    74	
    75	class Server:
    76	    def __init__(self, name: str, target: str, port: int) -> None:
    77	        self.name = name
    78	        self.target = target
    79	        self.port = port
    80	        self.base = f"http://127.0.0.1:{port}"
    81	        self.log_path = PROBE_DIR / f"{name}.log"
    82	        self.proc: subprocess.Popen[bytes] | None = None
    83	        self._log = None
    84	
    85	    def start(self) -> None:
    86	        self._log = self.log_path.open("wb")
    87	        self.proc = subprocess.Popen(
    88	            [
    89	                str(PY),
    90	                "-m",
    91	                "uvicorn",
    92	                self.target,
    93	                "--host",
    94	                "127.0.0.1",
    95	                "--port",
    96	                str(self.port),
    97	                "--log-level",
    98	                "warning",
    99	            ],
   100	            cwd=str(REPO),
   101	            env=ENV,
   102	            stdout=self._log,
   103	            stderr=subprocess.STDOUT,
   104	        )
   105	        deadline = time.monotonic() + 30
   106	        last_error = "no attempt"
   107	        while time.monotonic() < deadline:
   108	            if self.proc.poll() is not None:
   109	                break
   110	            try:
   111	                with urllib.request.urlopen(self.base + "/health", timeout=1) as resp:
   112	                    if resp.status == 200:
   113	                        print(
   114	                            f"SERVER {self.name} pid={self.proc.pid} "
   115	                            f"port={self.port} health=200 target={self.target}"
   116	                        )
   117	                        return
   118	            except Exception as exc:  # noqa: BLE001 — انتظارُ الإقلاعِ
   119	                last_error = f"{type(exc).__name__}: {exc}"
   120	                time.sleep(0.2)
   121	        tail = self.log_path.read_text(encoding="utf-8", errors="replace")[-2000:]
   122	        raise RuntimeError(
   123	            f"تعذّرَ إقلاعُ {self.name} (exit={self.proc.poll()} last={last_error})\n{tail}"
   124	        )
   125	
   126	    def stop(self) -> None:
   127	        if self.proc is None:
   128	            return
   129	        if self.proc.poll() is None:
   130	            self.proc.terminate()
   131	            try:
   132	                self.proc.wait(timeout=5)
   133	            except subprocess.TimeoutExpired:
   134	                self.proc.kill()
   135	                self.proc.wait(timeout=5)
   136	        if self._log is not None:
   137	            self._log.close()
   138	        print(f"SERVER {self.name} stopped exit={self.proc.returncode}")
   139	
   140	
   141	def call(base: str, method: str, path: str, token: str, body: dict | None = None) -> tuple[int, object]:
   142	    data = None if body is None else json.dumps(body).encode("utf-8")
   143	    if method == "POST" and data is None:
   144	        data = b""
   145	    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
   146	    if body is not None:
   147	        headers["Content-Type"] = "application/json"
   148	    req = urllib.request.Request(base + path, data=data, method=method, headers=headers)
   149	    try:
   150	        with urllib.request.urlopen(req, timeout=20) as resp:
   151	            raw = resp.read().decode("utf-8")
   152	            return resp.status, json.loads(raw) if raw else None
   153	    except urllib.error.HTTPError as exc:
   154	        raw = exc.read().decode("utf-8", errors="replace")
   155	        try:
   156	            payload: object = json.loads(raw) if raw else None
   157	        except json.JSONDecodeError:
   158	            payload = raw
   159	        return exc.code, payload
   160	
   161	
   162	def main() -> int:
   163	    failures: list[str] = []
   164	
   165	    def check(name: str, ok: bool, detail: str) -> None:
   166	        mark = "PASS" if ok else "FAIL"
   167	        print(f"CHECK {mark} {name} :: {detail}")
   168	        if not ok:
   169	            failures.append(name)
   170	
   171	    _prepare_database()
   172	    from amos_federation.common.auth import ROLE_CITIZEN, ROLE_KING
   173	
   174	    citizen = _mint(ROLE_CITIZEN, "wi117-probe-citizen")
   175	    king = _mint(ROLE_KING, "king")
   176	    print(f"TOKEN citizen_role={ROLE_CITIZEN} king_role={ROLE_KING} minted=yes")
   177	
   178	    gov = Server(
   179	        "governance",
   180	        "amos_federation.services.governance.main:app",
   181	        _free_port(),
   182	    )
   183	    console = Server(
   184	        "control_console",
   185	        "amos_federation.services.control_console.main:app",
   186	        _free_port(),
   187	    )
   188	    try:
   189	        gov.start()
   190	        console.start()
   191	
   192	        status, payload = call(gov.base, "GET", "/v1/system/status", citizen)
   193	        print(f"HTTP GET governance /v1/system/status citizen -> {status} {payload}")
   194	        check("status_readable_by_citizen", status == 200, f"status={status}")
   195	        level_before_raise = payload.get("level") if isinstance(payload, dict) else None
   196	
   197	        status, payload = call(
   198	            gov.base,
   199	            "POST",
   200	            "/v1/system/kill-switch",
   201	            citizen,
   202	            {"level": "halt", "reason": "wi117-seat-probe", "activated_by": "citizen-probe"},
   203	        )
   204	        print(f"HTTP POST governance /v1/system/kill-switch citizen halt -> {status} {payload}")
   205	        check(
   206	            "activate_remains_open_to_citizen",
   207	            status == 200 and isinstance(payload, dict) and payload.get("level") == "halt",
   208	            f"status={status} body={payload}",
   209	        )
   210	
   211	        status, payload = call(gov.base, "GET", "/v1/system/status", citizen)
   212	        level_halt = payload.get("level") if isinstance(payload, dict) else None
   213	        print(f"HTTP GET governance /v1/system/status after_activate -> {status} level={level_halt}")
   214	        check("level_is_halt_before_resets", level_halt == "halt", f"level={level_halt}")
   215	
   216	        status, payload = call(gov.base, "POST", "/v1/system/kill-switch/reset", citizen)
   217	        print(f"HTTP POST governance /v1/system/kill-switch/reset citizen -> {status} {payload}")
   218	        check("citizen_governance_reset_403", status == 403, f"status={status} body={payload}")
   219	        status, payload = call(gov.base, "GET", "/v1/system/status", citizen)
   220	        level_after = payload.get("level") if isinstance(payload, dict) else None
   221	        print(f"HTTP GET governance /v1/system/status after_citizen_gov_reset -> {status} level={level_after}")
   222	        check(
   223	            "level_unchanged_after_citizen_gov_reset",
   224	            level_after == "halt",
   225	            f"before=halt after={level_after}",
   226	        )
   227	
   228	        status, payload = call(console.base, "POST", "/v1/kill-switch/reset", citizen)
   229	        print(f"HTTP POST control_console /v1/kill-switch/reset citizen -> {status} {payload}")
   230	        check("citizen_console_reset_403", status == 403, f"status={status} body={payload}")
   231	        status, payload = call(gov.base, "GET", "/v1/system/status", citizen)
   232	        level_after = payload.get("level") if isinstance(payload, dict) else None
   233	        print(f"HTTP GET governance /v1/system/status after_citizen_console_reset -> {status} level={level_after}")
   234	        check(
   235	            "level_unchanged_after_citizen_console_reset",
   236	            level_after == "halt",
   237	            f"before=halt after={level_after}",
   238	        )
   239	
   240	        status, listed = call(gov.base, "GET", "/v1/promotions", citizen)
   241	        count_before = len(listed) if isinstance(listed, list) else -1
   242	        print(f"HTTP GET governance /v1/promotions citizen before -> {status} count={count_before}")
   243	        status, payload = call(
   244	            gov.base,
   245	            "POST",
   246	            "/v1/promotions",
   247	            citizen,
   248	            {"model_id": "wi117-citizen-must-not-create"},
   249	        )
   250	        print(f"HTTP POST governance /v1/promotions citizen -> {status} {payload}")
   251	        check("citizen_promotions_403", status == 403, f"status={status} body={payload}")
   252	        status, listed_after = call(gov.base, "GET", "/v1/promotions", citizen)
   253	        count_after = len(listed_after) if isinstance(listed_after, list) else -1
   254	        print(f"HTTP GET governance /v1/promotions citizen after -> {status} count={count_after}")
   255	        check(
   256	            "promotion_count_unchanged_after_citizen_create",
   257	            count_after == count_before and count_before >= 0,
   258	            f"before={count_before} after={count_after}",
   259	        )
   260	        status, state = call(gov.base, "GET", "/v1/system/status", citizen)
   261	        level_after = state.get("level") if isinstance(state, dict) else None
   262	        print(f"HTTP GET governance /v1/system/status after_citizen_promotions -> {status} level={level_after}")
   263	        check(
   264	            "level_unchanged_after_citizen_promotions",
   265	            level_after == "halt",
   266	            f"before=halt after={level_after}",
   267	        )
   268	
   269	        status, created = call(
   270	            gov.base,
   271	            "POST",
   272	            "/v1/promotions",
   273	            king,
   274	            {"model_id": "wi117-king-probe"},
   275	        )
   276	        promo_id = created.get("promotion_id") if isinstance(created, dict) else None
   277	        print(f"HTTP POST governance /v1/promotions king -> {status} id={promo_id} body={created}")
   278	        check(
   279	            "king_promotions_201",
   280	            status == 201 and isinstance(promo_id, str) and bool(promo_id),
   281	            f"status={status} id={promo_id}",
   282	        )
   283	
   284	        gate_path = f"/v1/promotions/{promo_id}/gates"
   285	        status, payload = call(
   286	            gov.base,
   287	            "POST",
   288	            gate_path,
   289	            citizen,
   290	            {"gate_name": "evaluation", "passed": True, "notes": "citizen-must-not"},
   291	        )
   292	        print(f"HTTP POST governance {gate_path} citizen -> {status} {payload}")
   293	        check("citizen_gates_403", status == 403, f"status={status} body={payload}")
   294	        status, promo = call(gov.base, "GET", f"/v1/promotions/{promo_id}", citizen)
   295	        gate_status = None
   296	        if isinstance(promo, dict):
   297	            gate_status = (promo.get("gates") or {}).get("evaluation", {}).get("status")
   298	        print(
   299	            f"HTTP GET governance /v1/promotions/{promo_id} after_citizen_gate -> "
   300	            f"{status} evaluation={gate_status}"
   301	        )
   302	        check(
   303	            "gate_unchanged_after_citizen",
   304	            gate_status == "pending",
   305	            f"evaluation={gate_status}",
   306	        )
   307	        status, state = call(gov.base, "GET", "/v1/system/status", citizen)
   308	        level_after = state.get("level") if isinstance(state, dict) else None
   309	        print(f"HTTP GET governance /v1/system/status after_citizen_gates -> {status} level={level_after}")
   310	        check(
   311	            "level_unchanged_after_citizen_gates",
   312	            level_after == "halt",
   313	            f"before=halt after={level_after}",
   314	        )
   315	
   316	        status, payload = call(
   317	            gov.base,
   318	            "POST",
   319	            gate_path,
   320	            king,
   321	            {"gate_name": "evaluation", "passed": True, "notes": "king-probe"},
   322	        )
   323	        king_gate = None
   324	        if isinstance(payload, dict):
   325	            king_gate = (payload.get("gates") or {}).get("evaluation", {}).get("status")
   326	        print(f"HTTP POST governance {gate_path} king -> {status} evaluation={king_gate}")
   327	        check(
   328	            "king_gates_200",
   329	            status == 200 and king_gate == "passed",
   330	            f"status={status} evaluation={king_gate}",
   331	        )
   332	
   333	        status, payload = call(gov.base, "POST", "/v1/system/kill-switch/reset", king)
   334	        print(f"HTTP POST governance /v1/system/kill-switch/reset king -> {status} {payload}")
   335	        check(
   336	            "king_governance_reset_200",
   337	            status == 200 and isinstance(payload, dict) and payload.get("level") == "normal",
   338	            f"status={status} body={payload}",
   339	        )
   340	        status, state = call(gov.base, "GET", "/v1/system/status", citizen)
   341	        level_after = state.get("level") if isinstance(state, dict) else None
   342	        print(f"HTTP GET governance /v1/system/status after_king_gov_reset -> {status} level={level_after}")
   343	        check("level_normal_after_king_gov_reset", level_after == "normal", f"level={level_after}")
   344	
   345	        status, payload = call(
   346	            console.base,
   347	            "POST",
   348	            "/v1/kill-switch",
   349	            citizen,
   350	            {"level": "halt", "reason": "wi117-seat-probe-console", "activated_by": "citizen-probe"},
   351	        )
   352	        print(f"HTTP POST control_console /v1/kill-switch citizen halt -> {status} {payload}")
   353	        check(
   354	            "console_activate_remains_open_to_citizen",
   355	            status == 200 and isinstance(payload, dict) and payload.get("level") == "halt",
   356	            f"status={status} body={payload}",
   357	        )
   358	        status, payload = call(console.base, "POST", "/v1/kill-switch/reset", king)
   359	        print(f"HTTP POST control_console /v1/kill-switch/reset king -> {status} {payload}")
   360	        check(
   361	            "king_console_reset_200",
   362	            status == 200 and isinstance(payload, dict) and payload.get("level") == "normal",
   363	            f"status={status} body={payload}",
   364	        )
   365	        status, state = call(gov.base, "GET", "/v1/system/status", citizen)
   366	        level_after = state.get("level") if isinstance(state, dict) else None
   367	        print(f"HTTP GET governance /v1/system/status after_king_console_reset -> {status} level={level_after}")
   368	        check("level_normal_after_king_console_reset", level_after == "normal", f"level={level_after}")
   369	
   370	        print(f"BASELINE_LEVEL_BEFORE_RAISE {level_before_raise}")
   371	    finally:
   372	        console.stop()
   373	        gov.stop()
   374	
   375	    if failures:
   376	        print("PROBE_RESULT FAIL " + ",".join(failures))
   377	        return 1
   378	    print("PROBE_RESULT PASS citizen_403_x4 level_unchanged king_passed_x4")
   379	    return 0
   380	
   381	
   382	if __name__ == "__main__":
   383	    try:
   384	        sys.exit(main())
   385	    except Exception as exc:  # noqa: BLE001 — المسبارُ يُعلنُ سقوطَه ولا يبتلعَه
   386	        print(f"PROBE_RESULT FAIL exception={type(exc).__name__}: {exc}")
   387	        raise
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: /home/user/workspace/council_w701/grok_4_7/wi117/repo/.venv/bin/python /home/user/workspace/council_w701/grok_4_7/wi117/probe/wi117_http_probe.py
EXIT: 0
BYTES: 5455
SHA256: 5bdc72f1b5e3ef4fd874891abd11c27da50f83a6e3df84dd0ef43e6f477dea07
NO_EOL: 0
--- OUTPUT ---
TOKEN citizen_role=citizen king_role=king minted=yes
SERVER governance pid=7522 port=47763 health=200 target=amos_federation.services.governance.main:app
SERVER control_console pid=7536 port=42171 health=200 target=amos_federation.services.control_console.main:app
HTTP GET governance /v1/system/status citizen -> 200 {'level': 'normal', 'reason': '', 'activated_at': None, 'activated_by': ''}
CHECK PASS status_readable_by_citizen :: status=200
HTTP POST governance /v1/system/kill-switch citizen halt -> 200 {'level': 'halt', 'reason': 'wi117-seat-probe', 'activated_at': '2026-10-28T06:20:22.057622+00:00', 'activated_by': 'citizen-probe'}
CHECK PASS activate_remains_open_to_citizen :: status=200 body={'level': 'halt', 'reason': 'wi117-seat-probe', 'activated_at': '2026-10-28T06:20:22.057622+00:00', 'activated_by': 'citizen-probe'}
HTTP GET governance /v1/system/status after_activate -> 200 level=halt
CHECK PASS level_is_halt_before_resets :: level=halt
HTTP POST governance /v1/system/kill-switch/reset citizen -> 403 {'detail': 'هذا الإجراء يتطلب صلاحيات المالك/الملك'}
CHECK PASS citizen_governance_reset_403 :: status=403 body={'detail': 'هذا الإجراء يتطلب صلاحيات المالك/الملك'}
HTTP GET governance /v1/system/status after_citizen_gov_reset -> 200 level=halt
CHECK PASS level_unchanged_after_citizen_gov_reset :: before=halt after=halt
HTTP POST control_console /v1/kill-switch/reset citizen -> 403 {'detail': 'هذا الإجراء يتطلب صلاحيات المالك/الملك'}
CHECK PASS citizen_console_reset_403 :: status=403 body={'detail': 'هذا الإجراء يتطلب صلاحيات المالك/الملك'}
HTTP GET governance /v1/system/status after_citizen_console_reset -> 200 level=halt
CHECK PASS level_unchanged_after_citizen_console_reset :: before=halt after=halt
HTTP GET governance /v1/promotions citizen before -> 200 count=0
HTTP POST governance /v1/promotions citizen -> 403 {'detail': 'هذا الإجراء يتطلب صلاحيات المالك/الملك'}
CHECK PASS citizen_promotions_403 :: status=403 body={'detail': 'هذا الإجراء يتطلب صلاحيات المالك/الملك'}
HTTP GET governance /v1/promotions citizen after -> 200 count=0
CHECK PASS promotion_count_unchanged_after_citizen_create :: before=0 after=0
HTTP GET governance /v1/system/status after_citizen_promotions -> 200 level=halt
CHECK PASS level_unchanged_after_citizen_promotions :: before=halt after=halt
HTTP POST governance /v1/promotions king -> 201 id=promo-3a3d18ff-dbf0-45d2-98e3-6704197ee566 body={'promotion_id': 'promo-3a3d18ff-dbf0-45d2-98e3-6704197ee566', 'model_id': 'wi117-king-probe', 'gates': {'evaluation': {'status': 'pending', 'checked_at': None}, 'shadow': {'status': 'pending', 'checked_at': None}, 'canary': {'status': 'pending', 'checked_at': None}, 'human_approval': {'status': 'pending', 'checked_at': None}, 'activation': {'status': 'pending', 'checked_at': None}}, 'status': 'in_progress', 'created_at': '2026-10-28T06:20:22.108295+00:00', 'updated_at': '2026-10-28T06:20:22.108295+00:00'}
CHECK PASS king_promotions_201 :: status=201 id=promo-3a3d18ff-dbf0-45d2-98e3-6704197ee566
HTTP POST governance /v1/promotions/promo-3a3d18ff-dbf0-45d2-98e3-6704197ee566/gates citizen -> 403 {'detail': 'هذا الإجراء يتطلب صلاحيات المالك/الملك'}
CHECK PASS citizen_gates_403 :: status=403 body={'detail': 'هذا الإجراء يتطلب صلاحيات المالك/الملك'}
HTTP GET governance /v1/promotions/promo-3a3d18ff-dbf0-45d2-98e3-6704197ee566 after_citizen_gate -> 200 evaluation=pending
CHECK PASS gate_unchanged_after_citizen :: evaluation=pending
HTTP GET governance /v1/system/status after_citizen_gates -> 200 level=halt
CHECK PASS level_unchanged_after_citizen_gates :: before=halt after=halt
HTTP POST governance /v1/promotions/promo-3a3d18ff-dbf0-45d2-98e3-6704197ee566/gates king -> 200 evaluation=passed
CHECK PASS king_gates_200 :: status=200 evaluation=passed
HTTP POST governance /v1/system/kill-switch/reset king -> 200 {'level': 'normal', 'reason': '', 'activated_at': None, 'activated_by': ''}
CHECK PASS king_governance_reset_200 :: status=200 body={'level': 'normal', 'reason': '', 'activated_at': None, 'activated_by': ''}
HTTP GET governance /v1/system/status after_king_gov_reset -> 200 level=normal
CHECK PASS level_normal_after_king_gov_reset :: level=normal
HTTP POST control_console /v1/kill-switch citizen halt -> 200 {'level': 'halt', 'reason': 'wi117-seat-probe-console', 'activated_at': '2026-10-28T06:20:22.427687+00:00', 'activated_by': 'citizen-probe'}
CHECK PASS console_activate_remains_open_to_citizen :: status=200 body={'level': 'halt', 'reason': 'wi117-seat-probe-console', 'activated_at': '2026-10-28T06:20:22.427687+00:00', 'activated_by': 'citizen-probe'}
HTTP POST control_console /v1/kill-switch/reset king -> 200 {'level': 'normal', 'reason': '', 'activated_at': None, 'activated_by': ''}
CHECK PASS king_console_reset_200 :: status=200 body={'level': 'normal', 'reason': '', 'activated_at': None, 'activated_by': ''}
HTTP GET governance /v1/system/status after_king_console_reset -> 200 level=normal
CHECK PASS level_normal_after_king_console_reset :: level=normal
BASELINE_LEVEL_BEFORE_RAISE normal
SERVER control_console stopped exit=-15
SERVER governance stopped exit=-15
PROBE_RESULT PASS citizen_403_x4 level_unchanged king_passed_x4
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w701/grok_4_7/wi117/repo && rg -n -A 12 -H "def test_reset_kill_switch|def test_create_promotion|def test_check_gate_passed|def test_check_gate_failed_stops_promotion|def test_all_gates_passed_promotes|def test_kill_switch_reset\(" federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py
EXIT: 0
BYTES: 7367
SHA256: e15bdf1231f51b58e1094e4d7c08b70a20511e3dcc2f392e6203f34a9516719b
NO_EOL: 0
--- OUTPUT ---
federal/executive/services/tests/test_control_console.py:196:def test_kill_switch_reset() -> None:
federal/executive/services/tests/test_control_console.py-197-    """إعادة ضبط Kill Switch (حارسٌ ملكيٌّ — WI-117)."""
federal/executive/services/tests/test_control_console.py-198-    client.post(
federal/executive/services/tests/test_control_console.py-199-        "/v1/kill-switch",
federal/executive/services/tests/test_control_console.py-200-        headers=AUTH_HEADERS,
federal/executive/services/tests/test_control_console.py-201-        json={"level": "alert", "reason": "اختبار", "activated_by": "tester"},
federal/executive/services/tests/test_control_console.py-202-    )
federal/executive/services/tests/test_control_console.py-203-    resp = client.post("/v1/kill-switch/reset", headers=KING_HEADERS)
federal/executive/services/tests/test_control_console.py-204-    assert resp.status_code == 200
federal/executive/services/tests/test_control_console.py-205-    assert resp.json()["level"] == "normal"
federal/executive/services/tests/test_control_console.py-206-
federal/executive/services/tests/test_control_console.py-207-
federal/executive/services/tests/test_control_console.py-208-def test_kill_switch_writes_audit() -> None:
--
federal/executive/services/tests/test_governance.py:131:def test_reset_kill_switch() -> None:
federal/executive/services/tests/test_governance.py-132-    """إعادة ضبط مفتاح الإيقاف (حارسٌ ملكيٌّ — WI-117)."""
federal/executive/services/tests/test_governance.py-133-    client.post(
federal/executive/services/tests/test_governance.py-134-        "/v1/system/kill-switch",
federal/executive/services/tests/test_governance.py-135-        headers=AUTH_HEADERS,
federal/executive/services/tests/test_governance.py-136-        json={"level": "alert", "reason": "test", "activated_by": "admin"},
federal/executive/services/tests/test_governance.py-137-    )
federal/executive/services/tests/test_governance.py-138-    resp = client.post("/v1/system/kill-switch/reset", headers=KING_HEADERS)
federal/executive/services/tests/test_governance.py-139-    assert resp.status_code == 200
federal/executive/services/tests/test_governance.py-140-    assert resp.json()["level"] == "normal"
federal/executive/services/tests/test_governance.py-141-
federal/executive/services/tests/test_governance.py-142-
federal/executive/services/tests/test_governance.py-143-def test_kill_switch_rejects_invalid_level() -> None:
--
federal/executive/services/tests/test_governance.py:156:def test_create_promotion() -> None:
federal/executive/services/tests/test_governance.py-157-    """إنشاء طلب ترقية (حارسٌ ملكيٌّ — WI-117)."""
federal/executive/services/tests/test_governance.py-158-    resp = client.post("/v1/promotions", headers=KING_HEADERS, json={"model_id": "model-123"})
federal/executive/services/tests/test_governance.py-159-    assert resp.status_code == 201
federal/executive/services/tests/test_governance.py-160-    data = resp.json()
federal/executive/services/tests/test_governance.py-161-    assert "promotion_id" in data
federal/executive/services/tests/test_governance.py-162-    assert data["status"] == "in_progress"
federal/executive/services/tests/test_governance.py-163-    assert "evaluation" in data["gates"]
federal/executive/services/tests/test_governance.py-164-    assert "human_approval" in data["gates"]
federal/executive/services/tests/test_governance.py-165-
federal/executive/services/tests/test_governance.py-166-
federal/executive/services/tests/test_governance.py:167:def test_check_gate_passed() -> None:
federal/executive/services/tests/test_governance.py-168-    """فحص بوابة ناجحة (حارسٌ ملكيٌّ — WI-117)."""
federal/executive/services/tests/test_governance.py-169-    create = client.post("/v1/promotions", headers=KING_HEADERS, json={"model_id": "model-1"})
federal/executive/services/tests/test_governance.py-170-    promo_id = create.json()["promotion_id"]
federal/executive/services/tests/test_governance.py-171-    resp = client.post(
federal/executive/services/tests/test_governance.py-172-        f"/v1/promotions/{promo_id}/gates",
federal/executive/services/tests/test_governance.py-173-        headers=KING_HEADERS,
federal/executive/services/tests/test_governance.py-174-        json={"gate_name": "evaluation", "passed": True},
federal/executive/services/tests/test_governance.py-175-    )
federal/executive/services/tests/test_governance.py-176-    assert resp.status_code == 200
federal/executive/services/tests/test_governance.py-177-    assert resp.json()["gates"]["evaluation"]["status"] == "passed"
federal/executive/services/tests/test_governance.py-178-
federal/executive/services/tests/test_governance.py-179-
federal/executive/services/tests/test_governance.py:180:def test_check_gate_failed_stops_promotion() -> None:
federal/executive/services/tests/test_governance.py-181-    """فشل بوابة يوقف الترقية (حارسٌ ملكيٌّ — WI-117)."""
federal/executive/services/tests/test_governance.py-182-    create = client.post("/v1/promotions", headers=KING_HEADERS, json={"model_id": "model-2"})
federal/executive/services/tests/test_governance.py-183-    promo_id = create.json()["promotion_id"]
federal/executive/services/tests/test_governance.py-184-    resp = client.post(
federal/executive/services/tests/test_governance.py-185-        f"/v1/promotions/{promo_id}/gates",
federal/executive/services/tests/test_governance.py-186-        headers=KING_HEADERS,
federal/executive/services/tests/test_governance.py-187-        json={"gate_name": "evaluation", "passed": False},
federal/executive/services/tests/test_governance.py-188-    )
federal/executive/services/tests/test_governance.py-189-    assert resp.json()["status"] == "failed"
federal/executive/services/tests/test_governance.py-190-
federal/executive/services/tests/test_governance.py-191-
federal/executive/services/tests/test_governance.py:192:def test_all_gates_passed_promotes() -> None:
federal/executive/services/tests/test_governance.py-193-    """اجتياز كل البوابات يرقى النموذج (حارسٌ ملكيٌّ — WI-117)."""
federal/executive/services/tests/test_governance.py-194-    create = client.post("/v1/promotions", headers=KING_HEADERS, json={"model_id": "model-3"})
federal/executive/services/tests/test_governance.py-195-    promo_id = create.json()["promotion_id"]
federal/executive/services/tests/test_governance.py-196-    for gate in ["evaluation", "shadow", "canary", "human_approval", "activation"]:
federal/executive/services/tests/test_governance.py-197-        client.post(
federal/executive/services/tests/test_governance.py-198-            f"/v1/promotions/{promo_id}/gates",
federal/executive/services/tests/test_governance.py-199-            headers=KING_HEADERS,
federal/executive/services/tests/test_governance.py-200-            json={"gate_name": gate, "passed": True},
federal/executive/services/tests/test_governance.py-201-        )
federal/executive/services/tests/test_governance.py-202-    resp = client.get(f"/v1/promotions/{promo_id}", headers=AUTH_HEADERS)
federal/executive/services/tests/test_governance.py-203-    assert resp.json()["status"] == "promoted"
federal/executive/services/tests/test_governance.py-204-
=== RAW [18] END ===
VERDICT_PER_CRITERION: (1) نعم — RAW [7] EXIT 0: Depends(require_king) على governance/main.py:149 (POST /v1/system/kill-switch/reset) و:170 (POST /v1/promotions) و:203 (POST /v1/promotions/{id}/gates) وعلى control_console/main.py:211 (POST /v1/kill-switch/reset). sign_approval على control_console/main.py:233 محروسٌ أيضًا بإلحاقِ التوجيهِ 24 § 1 وليسَ من المساراتِ الأربعةِ. (2) نعم — RAW [17] EXIT 0: مسبارُ HTTP حقيقيٌّ عبرَ uvicorn برمزِ مواطنٍ ⇒ 403 على المساراتِ الأربعةِ، والمستوى بقي halt بعدَ كلِّ رفضٍ، وعددُ الترقياتِ لم يزدْ، وبوابةُ evaluation بقيت pending. (3) نعم — RAW [17]: رمزُ الملكِ ⇒ 201 على الإنشاءِ و200 evaluation=passed على البوّابةِ و200 level=normal على خفضِ الحوكمةِ و200 level=normal على خفضِ الوحدةِ. RAW [8] EXIT 0: 10 passed. (4) نعم — RAW [11] EXIT 1: إسقاطُ Depends(require_king) إلى Depends(require_auth) في الملفَّينِ معًا أسقطَ فحوصَ المواطنِ الأربعةَ (والخامسَ sign_approval) على التأكيدِ الدلاليِّ لا على خطأِ واجهةٍ: reset 200!=403 وpromotions 201!=403 وgates 200!=403 وconsole reset 200!=403. RAW [12] EXIT 0 أعادَ الملفَّينِ والشجرةَ نظيفةً (مخرجٌ فارغٌ). RAW [10] EXIT 2 خطأُ جمعٍ (role غيرُ متوقَّعٍ في PerTestAuthHeaders القديمة) دليلُ تاريخٍ مكمِّلٌ لا كافٍ وحدَه كما نصّتِ الإحاطةُ، والمعيارُ قائمٌ على RAW [11]. (5) نعم — RAW [18] EXIT 0 يُظهرُ الفحوصَ الستَّ برمزِ ملكٍ بلا إسقاطِ التأكيدِ السلوكيِّ: test_kill_switch_reset (وحدةُ التحكّمِ: 200 وlevel=normal) وtest_reset_kill_switch (200 وlevel=normal) وtest_create_promotion (201 والحالةُ والبوّاباتُ) وtest_check_gate_passed (evaluation passed) وtest_check_gate_failed_stops_promotion (status failed) وtest_all_gates_passed_promotes (status promoted). RAW [9] EXIT 0: 55 passed. مسارُ activate بقي مفتوحًا للمواطنِ (RAW [17] ⇒ 200) وفقَ D25-2 في RAW [13]. (6) نعم — مسبارُ هذا المقعدِ كتلةُ الشِّفرةِ RAW [16] وكتلةُ التشغيلِ RAW [17] EXIT 0 وPROBE_RESULT PASS.
PROBES: مسبارُ HTTP wi117_http_probe.py · كتلةُ الشِّفرةِ [16] · كتلةُ التشغيلِ [17] · الخاصيّةُ التي حاولَ كسرَها: تمريرُ رمزِ مواطنٍ (role=citizen) على المساراتِ الأربعةِ المحروسةِ وتغييرُ مستوى زرِّ التوقّفِ أو إنشاءُ ترقيةٍ أو تمريرُ بوّابةٍ · انكسرت؟ لا
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — لم أقرأْ ولم أكتبْ خارجَ جذرِ /home/user/workspace/council_w701/grok_4_7/wi117. استنسختُ المستودعَ بنفسِي من GitHub إلى CLONE_PATH وأعددتُ بيئتَه بـtools/dev/bootstrap.sh، وشغّلتُ أوامرَ المعاييرِ ومسبارِي داخلَ هذا الجذرِ. لم أقرأْ نسخةَ المنسِّقِ ولا أدلّةَ المنفِّذِ ولا عملَ المقاعدِ الأخرى. لا استثناء.
VERDICT: PASS لكلِّ المعاييرِ
