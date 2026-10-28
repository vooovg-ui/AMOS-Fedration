# حكمُ مقعدِ المجلسِ — gemini_3_8_flash · جولةُ WI-117 (W-710)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في الجولةِ الواحدةِ (قرارُ المالكِ D27) على WI-117 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w701/gemini_3_8_flash/wi117) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `2a073a659a597e2e5f0faa4ea6117301a722350bff4981e304b9ffaf63a9b008`).

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
MODEL: gemini_3_8_flash
FAMILY: Google · Gemini
RUN_DATE: 2026-10-28 06:19 +00:00
NODE: 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
CLONE_PATH: /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/
 2. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/)
 3. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
 5. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git show --stat f8d33807
 6. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git diff f8d33807^ f8d33807 -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
 7. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && rg -n "require_king" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py
 8. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 9. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py
 10. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && rm -rf ../old && git worktree add --detach ../old f8d33807^ && cp federal/executive/services/tests/test_wi117_king_guard_routes.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 11. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && sed -i "s/Depends(require_king)/Depends(require_auth)/g" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 12. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && git status --short && git diff --stat
 13. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && rg -n "D25-2|require_king" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 14. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && sha256sum docs/audit/evidence/W-701/briefs_wi117/briefing_gemini_3_8_flash.md
 15. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && cat docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS
 16. nl -ba /home/user/workspace/council_w701/gemini_3_8_flash/wi117/probe/probe_wi117_http_live.py
 17. cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && .venv/bin/python /home/user/workspace/council_w701/gemini_3_8_flash/wi117/probe/probe_wi117_http_live.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/)
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git show --stat f8d33807
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git diff f8d33807^ f8d33807 -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && rg -n "require_king" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py
EXIT: 0
BYTES: 1009
SHA256: 7819eef502b030874641e976ce8b493cb95062624144f0a3c8bb15fd0975eac9
NO_EOL: 0
--- OUTPUT ---
federal/executive/services/src/amos_federation/services/governance/main.py:14:from amos_federation.common.auth import require_auth, require_king
federal/executive/services/src/amos_federation/services/governance/main.py:149:    _: Annotated[dict[str, object], Depends(require_king)],
federal/executive/services/src/amos_federation/services/governance/main.py:170:    _: Annotated[dict[str, object], Depends(require_king)],
federal/executive/services/src/amos_federation/services/governance/main.py:203:    _: Annotated[dict[str, object], Depends(require_king)],
federal/executive/services/src/amos_federation/services/control_console/main.py:15:from amos_federation.common.auth import require_auth, require_king
federal/executive/services/src/amos_federation/services/control_console/main.py:211:    _: Annotated[dict[str, object], Depends(require_king)],
federal/executive/services/src/amos_federation/services/control_console/main.py:233:    token_data: Annotated[dict[str, object], Depends(require_king)],
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 0
BYTES: 2408
SHA256: 5372acb0a4ac9765baabc4bb5c9a75848026196cbc75d6b84adae800229c22e7
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items

federal/executive/services/tests/test_wi117_king_guard_routes.py ....... [ 70%]
...                                                                      [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 10 passed, 1 warning in 1.22s =========================
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 1.00s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py
EXIT: 0
BYTES: 2793
SHA256: 3d27281b609235cfb7012daf6b27953b284720de61eed479ccec7f81fb4aad79
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/federal/executive/services
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
  /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 55 passed, 1 warning in 6.71s =========================
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 1.04s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && rm -rf ../old && git worktree add --detach ../old f8d33807^ && cp federal/executive/services/tests/test_wi117_king_guard_routes.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 2
BYTES: 3040
SHA256: 0a73324e3c1b07197211c13f76007b63d95635b50536d965de8d26f4f818cf02
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD b7bb6aa6)
HEAD is now at b7bb6aa6 W-688: انتقالُ WI-117 إلى IN_PROGRESS (دفعةٌ ورقيّةٌ تسبقُ دفعةَ الشِّفرةِ مباشرةً · إجراءُ DISC-137) + واجبُ N+1 لدفعةِ W-687 (حكما CI على 735b7631 مقروءانِ أخضرانِ 13/13) + إصلاحُ رابطَي WI-115 المؤجَّلُ (الإفصاحُ (ب) للتوجيهِ 24) · لا شِّفرةَ) · المنسِّقُ GLM-5.3 (Perplexity Computer)
/home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/gemini_3_8_flash/wi117/old/federal/executive/services
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
  /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
ERROR federal/executive/services/tests/test_wi117_king_guard_routes.py - Type...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.83s ==========================
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && sed -i "s/Depends(require_king)/Depends(require_auth)/g" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 1
BYTES: 4655
SHA256: 2ac4e9b4576a2574fbaeef4df239838b30d07588e0275016c17976e0b95981bc
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/federal/executive/services
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
  /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_reset_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_promotions_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_gates_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_console_reset_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_console_approval_citizen_forbidden
==================== 5 failed, 5 passed, 1 warning in 1.15s ====================
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 0.82s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && git status --short && git diff --stat
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && rg -n "D25-2|require_king" docs/audit/SOVEREIGN_DECISION_REGISTER.md
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
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && sha256sum docs/audit/evidence/W-701/briefs_wi117/briefing_gemini_3_8_flash.md
EXIT: 0
BYTES: 134
SHA256: 273851b635e6bc98a19fd43fe3378dcfc1ba07881bd4c78fa4822c7f98879d1e
NO_EOL: 0
--- OUTPUT ---
33137ced2663e8e935c71f3a14079089acf5b5083c214663dbfa9ca7bffc899c  docs/audit/evidence/W-701/briefs_wi117/briefing_gemini_3_8_flash.md
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && cat docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w701/gemini_3_8_flash/wi117/probe/probe_wi117_http_live.py
EXIT: 0
BYTES: 14458
SHA256: fb207595cce1399eda0091a2d9e3d8fd802da2482dcafffff74113d3047ec4cb
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""
     3	مسبار WI-117 المستقل — مقعد gemini_3_8_flash
     4	الهدف: اختبار مسارات الخفض والترقية وبوابات الفحص والموافقة عبر طلبات HTTP حقيقية
     5	    باستخدام خادم uvicorn حي، وإثبات صريح بأن:
     6	    1. رمز المواطن (role=citizen) يُرفض بـ 403 Forbidden دون تغيير المستوى.
     7	    2. رمز الملك (role=king) يُقبل بنجاح.
     8	    3. هوية الموقع تُستمد من الرمز الملكي لمنع التزوير.
     9	المسارات الأربعة المحروسة بنص المعايير:
    10	    - POST /v1/system/kill-switch/reset (governance)
    11	    - POST /v1/kill-switch/reset (control_console)
    12	    - POST /v1/promotions (governance)
    13	    - POST /v1/promotions/{id}/gates (governance)
    14	بالإضافة للمسار الخامس المحروس في دفعة W-689:
    15	    - POST /v1/approval (control_console)
    16	"""
    17	
    18	from __future__ import annotations
    19	
    20	import os
    21	import sys
    22	import threading
    23	import time
    24	
    25	# إعداد البيئة قبل استيراد وحدات التطبيق
    26	os.environ["AMOS_ENVIRONMENT"] = "test"
    27	os.environ["AMOS_JWT_SECRET"] = "wi117_probe_gemini_secret_at_least_32_chars_long"
    28	os.environ["AMOS_DATABASE_URL"] = "sqlite:////tmp/amos_probe_wi117_gemini.db"
    29	
    30	import httpx
    31	import uvicorn
    32	from amos_federation.common.auth import create_access_token
    33	from amos_federation.services.control_console.main import app as console_app
    34	from amos_federation.services.governance.main import app as governance_app
    35	
    36	GOV_PORT = 18101
    37	CON_PORT = 18102
    38	GOV_BASE = f"http://127.0.0.1:{GOV_PORT}"
    39	CON_BASE = f"http://127.0.0.1:{CON_PORT}"
    40	
    41	
    42	def main() -> int:
    43	    print("=== بدء مسبار WI-117 الحي (HTTP Probe via Uvicorn) ===")
    44	
    45	    # سك الرموز للاختبار
    46	    citizen_token = create_access_token(
    47	        subject="citizen-tester",
    48	        scopes=["governance:read", "governance:write"],
    49	        role="citizen",
    50	    )
    51	    king_token = create_access_token(
    52	        subject="king",
    53	        scopes=["governance:read", "governance:write", "*"],
    54	        role="king",
    55	    )
    56	    citizen_headers = {"Authorization": f"Bearer {citizen_token}"}
    57	    king_headers = {"Authorization": f"Bearer {king_token}"}
    58	
    59	    print("[1] تشغيل خادمي uvicorn للخدمتين على منافذ محلية منفصلة...")
    60	    gov_cfg = uvicorn.Config(governance_app, host="127.0.0.1", port=GOV_PORT, log_level="error")
    61	    con_cfg = uvicorn.Config(console_app, host="127.0.0.1", port=CON_PORT, log_level="error")
    62	    gov_server = uvicorn.Server(gov_cfg)
    63	    con_server = uvicorn.Server(con_cfg)
    64	
    65	    t_gov = threading.Thread(target=gov_server.run, daemon=True)
    66	    t_con = threading.Thread(target=con_server.run, daemon=True)
    67	    t_gov.start()
    68	    t_con.start()
    69	
    70	    # انتظار جاهزية الخادمين
    71	    time.sleep(1.2)
    72	
    73	    try:
    74	        with httpx.Client(base_url=GOV_BASE, timeout=10.0) as gov_client, \
    75	             httpx.Client(base_url=CON_BASE, timeout=10.0) as con_client:
    76	
    77	            # فحص الصحة المبدئي
    78	            r_health_g = gov_client.get("/health")
    79	            r_health_c = con_client.get("/health")
    80	            assert r_health_g.status_code == 200, f"Governance health failed: {r_health_g.status_code}"
    81	            assert r_health_c.status_code == 200, f"Console health failed: {r_health_c.status_code}"
    82	            print(f"    ✓ خادم الحوكمة جاهز على المنفذ {GOV_PORT}")
    83	            print(f"    ✓ خادم لوحة التحكم جاهز على المنفذ {CON_PORT}")
    84	
    85	            # ── 1. فحص مسار خفض الحوكمة: POST /v1/system/kill-switch/reset ──
    86	            print("\n[2] فحص المسار 1: POST /v1/system/kill-switch/reset (governance)")
    87	            # تفعيل الإيقاف إلى alert
    88	            r_act = gov_client.post(
    89	                "/v1/system/kill-switch",
    90	                headers=citizen_headers,
    91	                json={"level": "alert", "reason": "probe_test", "activated_by": "tester"},
    92	            )
    93	            assert r_act.status_code == 200, f"Activation failed: {r_act.text}"
    94	            r_stat = gov_client.get("/v1/system/status", headers=citizen_headers)
    95	            assert r_stat.json()["level"] == "alert", "Level is not alert after activation"
    96	            print("    - تم تفعيل مفتاح الإيقاف إلى مستوى alert")
    97	
    98	            # محاولة خفض بالمواطن
    99	            r_cit_reset = gov_client.post("/v1/system/kill-switch/reset", headers=citizen_headers)
   100	            print(f"    - طلب مواطن: كود الاستجابة = {r_cit_reset.status_code} (المتوقع 403)")
   101	            assert r_cit_reset.status_code == 403, f"Citizen reset allowed! {r_cit_reset.status_code}"
   102	            assert "هذا الإجراء يتطلب صلاحيات المالك/الملك" in r_cit_reset.json().get("detail", "")
   103	            r_stat_after = gov_client.get("/v1/system/status", headers=citizen_headers)
   104	            assert r_stat_after.json()["level"] == "alert", "Level unexpectedly changed by citizen reset!"
   105	            print(f"    ✓ تم رفض طلب المواطن (403) وثبت بقاء المستوى دون تغيير ({r_stat_after.json()['level']})")
   106	
   107	            # خفض بالملك
   108	            r_king_reset = gov_client.post("/v1/system/kill-switch/reset", headers=king_headers)
   109	            print(f"    - طلب ملك: كود الاستجابة = {r_king_reset.status_code} (المتوقع 200)")
   110	            assert r_king_reset.status_code == 200, f"King reset failed! {r_king_reset.text}"
   111	            assert r_king_reset.json()["level"] == "normal"
   112	            r_stat_normal = gov_client.get("/v1/system/status", headers=citizen_headers)
   113	            assert r_stat_normal.json()["level"] == "normal"
   114	            print(f"    ✓ تم قبول طلب الملك بنجاح وعاد المستوى إلى normal")
   115	
   116	            # ── 2. فحص مسار خفض لوحة التحكم: POST /v1/kill-switch/reset ──
   117	            print("\n[3] فحص المسار 2: POST /v1/kill-switch/reset (control_console)")
   118	            # تفعيل الإيقاف إلى alert عبر الكونسول
   119	            r_act_c = con_client.post(
   120	                "/v1/kill-switch",
   121	                headers=citizen_headers,
   122	                json={"level": "alert", "reason": "probe_console", "activated_by": "tester"},
   123	            )
   124	            assert r_act_c.status_code == 200
   125	            # محاولة خفض بالمواطن
   126	            r_cit_con_reset = con_client.post("/v1/kill-switch/reset", headers=citizen_headers)
   127	            print(f"    - طلب مواطن: كود الاستجابة = {r_cit_con_reset.status_code} (المتوقع 403)")
   128	            assert r_cit_con_reset.status_code == 403
   129	            assert "هذا الإجراء يتطلب صلاحيات المالك/الملك" in r_cit_con_reset.json().get("detail", "")
   130	            # التأكد أن المستوى لا يزال alert عبر مسار الحوكمة
   131	            r_stat_chk = gov_client.get("/v1/system/status", headers=citizen_headers)
   132	            assert r_stat_chk.json()["level"] == "alert"
   133	            print(f"    ✓ تم رفض طلب المواطن (403) وثبت بقاء المستوى دون تغيير ({r_stat_chk.json()['level']})")
   134	
   135	            # خفض بالملك
   136	            r_king_con_reset = con_client.post("/v1/kill-switch/reset", headers=king_headers)
   137	            print(f"    - طلب ملك: كود الاستجابة = {r_king_con_reset.status_code} (المتوقع 200)")
   138	            assert r_king_con_reset.status_code == 200
   139	            assert r_king_con_reset.json()["level"] == "normal"
   140	            print("    ✓ تم قبول خفض الملك عبر لوحة التحكم بنجاح وعاد المستوى إلى normal")
   141	
   142	            # ── 3. فحص مسار إنشاء الترقية: POST /v1/promotions ──
   143	            print("\n[4] فحص المسار 3: POST /v1/promotions (governance)")
   144	            # محاولة إنشاء بالمواطن
   145	            r_cit_promo = gov_client.post(
   146	                "/v1/promotions",
   147	                headers=citizen_headers,
   148	                json={"model_id": "probe-illegal-model"},
   149	            )
   150	            print(f"    - طلب مواطن: كود الاستجابة = {r_cit_promo.status_code} (المتوقع 403)")
   151	            assert r_cit_promo.status_code == 403
   152	            assert "هذا الإجراء يتطلب صلاحيات المالك/الملك" in r_cit_promo.json().get("detail", "")
   153	            print("    ✓ تم رفض إنشاء الترقية للمواطن (403)")
   154	
   155	            # إنشاء بالملك
   156	            r_king_promo = gov_client.post(
   157	                "/v1/promotions",
   158	                headers=king_headers,
   159	                json={"model_id": "probe-king-model"},
   160	            )
   161	            print(f"    - طلب ملك: كود الاستجابة = {r_king_promo.status_code} (المتوقع 201)")
   162	            assert r_king_promo.status_code == 201
   163	            promo_data = r_king_promo.json()
   164	            promo_id = promo_data["promotion_id"]
   165	            assert promo_data["status"] == "in_progress"
   166	            print(f"    ✓ تم إنشاء الترقية بالملك بنجاح: promotion_id={promo_id}")
   167	
   168	            # ── 4. فحص مسار فحص البوابة: POST /v1/promotions/{id}/gates ──
   169	            print(f"\n[5] فحص المسار 4: POST /v1/promotions/{promo_id}/gates (governance)")
   170	            # محاولة فحص البوابة بالمواطن
   171	            r_cit_gate = gov_client.post(
   172	                f"/v1/promotions/{promo_id}/gates",
   173	                headers=citizen_headers,
   174	                json={"gate_name": "evaluation", "passed": True, "notes": "citizen attempt"},
   175	            )
   176	            print(f"    - طلب مواطن: كود الاستجابة = {r_cit_gate.status_code} (المتوقع 403)")
   177	            assert r_cit_gate.status_code == 403
   178	            assert "هذا الإجراء يتطلب صلاحيات المالك/الملك" in r_cit_gate.json().get("detail", "")
   179	            print("    ✓ تم رفض فحص البوابة للمواطن (403)")
   180	
   181	            # فحص البوابة بالملك
   182	            r_king_gate = gov_client.post(
   183	                f"/v1/promotions/{promo_id}/gates",
   184	                headers=king_headers,
   185	                json={"gate_name": "evaluation", "passed": True, "notes": "king check"},
   186	            )
   187	            print(f"    - طلب ملك: كود الاستجابة = {r_king_gate.status_code} (المتوقع 200)")
   188	            assert r_king_gate.status_code == 200
   189	            gate_resp = r_king_gate.json()
   190	            assert gate_resp["gates"]["evaluation"]["status"] == "passed"
   191	            print("    ✓ تم قبول فحص البوابة بالملك بنجاح وحالتها passed")
   192	
   193	            # ── 5. فحص مسار توقيع الموافقة: POST /v1/approval ──
   194	            print("\n[6] فحص المسار 5 الإضافي: POST /v1/approval (control_console)")
   195	            # محاولة موافقة بالمواطن
   196	            r_cit_app = con_client.post(
   197	                "/v1/approval",
   198	                headers=citizen_headers,
   199	                json={"decision": "approve"},
   200	            )
   201	            print(f"    - طلب مواطن: كود الاستجابة = {r_cit_app.status_code} (المتوقع 403)")
   202	            assert r_cit_app.status_code == 403
   203	            print("    ✓ تم رفض طلب توقيع الموافقة للمواطن (403)")
   204	
   205	            # موافقة بالملك مع محاولة تزوير اسم الموقع في الجسم
   206	            r_king_app = con_client.post(
   207	                "/v1/approval",
   208	                headers=king_headers,
   209	                json={"decision": "approve", "signed_by": "spoofed-user-id"},
   210	            )
   211	            print(f"    - طلب ملك: كود الاستجابة = {r_king_app.status_code} (المتوقع 200)")
   212	            assert r_king_app.status_code == 200
   213	            app_resp = r_king_app.json()
   214	            assert app_resp["signed_by"] == "king", f"Signer spoofed! got {app_resp['signed_by']}"
   215	            print(f"    ✓ تم توقيع الموافقة بالملك وفرض signed_by='king' من الرمز ومنع التزوير")
   216	
   217	    finally:
   218	        print("\n[7] إيقاف خوادم uvicorn...")
   219	        gov_server.should_exit = True
   220	        con_server.should_exit = True
   221	        t_gov.join(timeout=2.0)
   222	        t_con.join(timeout=2.0)
   223	        print("    ✓ تم إيقاف الخوادم بنجاح")
   224	
   225	    print("\n=== نتيجة المسبار: كل الفحوص الحية للمسارات المحروسة نجحت بنسبة 100% ===")
   226	    return 0
   227	
   228	
   229	if __name__ == "__main__":
   230	    sys.exit(main())
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w701/gemini_3_8_flash/wi117/repo && .venv/bin/python /home/user/workspace/council_w701/gemini_3_8_flash/wi117/probe/probe_wi117_http_live.py
EXIT: 0
BYTES: 3238
SHA256: f5af8f1de581e8d08c51a87ff7c7553ed03c4be50c6cee160e35ae88baff897f
NO_EOL: 0
--- OUTPUT ---
Overriding of current TracerProvider is not allowed
=== بدء مسبار WI-117 الحي (HTTP Probe via Uvicorn) ===
[1] تشغيل خادمي uvicorn للخدمتين على منافذ محلية منفصلة...
    ✓ خادم الحوكمة جاهز على المنفذ 18101
    ✓ خادم لوحة التحكم جاهز على المنفذ 18102

[2] فحص المسار 1: POST /v1/system/kill-switch/reset (governance)
    - تم تفعيل مفتاح الإيقاف إلى مستوى alert
    - طلب مواطن: كود الاستجابة = 403 (المتوقع 403)
    ✓ تم رفض طلب المواطن (403) وثبت بقاء المستوى دون تغيير (alert)
    - طلب ملك: كود الاستجابة = 200 (المتوقع 200)
    ✓ تم قبول طلب الملك بنجاح وعاد المستوى إلى normal

[3] فحص المسار 2: POST /v1/kill-switch/reset (control_console)
    - طلب مواطن: كود الاستجابة = 403 (المتوقع 403)
    ✓ تم رفض طلب المواطن (403) وثبت بقاء المستوى دون تغيير (alert)
    - طلب ملك: كود الاستجابة = 200 (المتوقع 200)
    ✓ تم قبول خفض الملك عبر لوحة التحكم بنجاح وعاد المستوى إلى normal

[4] فحص المسار 3: POST /v1/promotions (governance)
    - طلب مواطن: كود الاستجابة = 403 (المتوقع 403)
    ✓ تم رفض إنشاء الترقية للمواطن (403)
    - طلب ملك: كود الاستجابة = 201 (المتوقع 201)
    ✓ تم إنشاء الترقية بالملك بنجاح: promotion_id=promo-aeb045ef-a027-4f81-8e12-220edcd64b7b

[5] فحص المسار 4: POST /v1/promotions/promo-aeb045ef-a027-4f81-8e12-220edcd64b7b/gates (governance)
    - طلب مواطن: كود الاستجابة = 403 (المتوقع 403)
    ✓ تم رفض فحص البوابة للمواطن (403)
    - طلب ملك: كود الاستجابة = 200 (المتوقع 200)
    ✓ تم قبول فحص البوابة بالملك بنجاح وحالتها passed

[6] فحص المسار 5 الإضافي: POST /v1/approval (control_console)
    - طلب مواطن: كود الاستجابة = 403 (المتوقع 403)
    ✓ تم رفض طلب توقيع الموافقة للمواطن (403)
    - طلب ملك: كود الاستجابة = 200 (المتوقع 200)
    ✓ تم توقيع الموافقة بالملك وفرض signed_by='king' من الرمز ومنع التزوير

[7] إيقاف خوادم uvicorn...
    ✓ تم إيقاف الخوادم بنجاح

=== نتيجة المسبار: كل الفحوص الحية للمسارات المحروسة نجحت بنسبة 100% ===
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 1.10s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
=== RAW [17] END ===
VERDICT_PER_CRITERION: (1) نعم: المسارات الأربعة المحددة في D25-2 (بالإضافة إلى مسار توقيع الموافقة الخامس POST /v1/approval) جميعها محروسة بتبعية Depends(require_king). الدليل: فحص الكود بالبحث النصي في الأمر 7 (ظهور require_king صراحة في توقيع الدوال كـ Depends(require_king) في كل من governance/main.py و control_console/main.py)، وفرق الالتزام f8d33807 في الأمر 6، واجتياز حزمة الفحوص المخصصة 13/13 في test_wi117_king_guard_routes.py في الأمر 8، ومسبار المقعد الحي عبر طلبات HTTP حقيقية في الأمرين 16 و17.
(2) نعم: مسبار المقعد المستقل probe_wi117_http_live.py (المعروض بشفرته الكاملة في الكتلة 16 والمنفذ في الكتلة 17) أطلق خادمي uvicorn حيّين ونفذ طلبات HTTP حقيقية برمز مواطن (role=citizen) على جميع المسارات المحروسة، وأثبت رفضها جميعاً برمز الحالة 403 Forbidden مع رسالة الخطأ الصريحة "هذا الإجراء يتطلب صلاحيات المالك/الملك"، وأثبت فحص حالة النظام عبر GET /v1/system/status بقاء المستوى على alert دون أي تغيير.
(3) نعم: أثبت تشغيل المسبار الحي في الكتلة 17 أن تقديم رمز ملك صالح (role=king) على المسارات المحروسة يُقبل بنجاح كامل: مسار خفض الحوكمة أعاد 200 وعاد المستوى إلى normal، ومسار خفض لوحة التحكم أعاد 200 وعاد المستوى إلى normal، ومسار إنشاء الترقية أنشأ ترقية جديدة برمز 201، ومسار فحص البوابة اعتمد البوابة بنجاح برمز 200، ومسار توقيع الموافقة نجح برمز 200 وفرض نسبة التوقيع للملك king ومنع التزوير. كما أثبتت فحوص الكتلة 8 مرور رمز الملك في كافة المسارات.
(4) نعم: في الأمر 11 تم تطبيق مطفرة تسقط قيد الملك باستبدال Depends(require_king) بـ Depends(require_auth) في ملفي الحوكمة ولوحة التحكم؛ وعند تشغيل test_wi117_king_guard_routes.py سقطت الفحوص فوراً بخمسة إخفاقات دلالية صريحة (5 failed) برمز خروج 1 حيث فشلت جميع تأكيدات الرفض للمواطن (test_governance_reset_citizen_forbidden, test_governance_promotions_citizen_forbidden, test_governance_gates_citizen_forbidden, test_console_reset_citizen_forbidden, test_console_approval_citizen_forbidden) لأن رمز المواطن مسموح به في require_auth وممنوع في require_king، مما يثبت حساسية الفحوص وقتلها للمطفرة. ثم أعيدت الشجرة نظيفة في الأمر 12.
(5) نعم: تم تحديث الفحوص القائمة في test_governance.py و test_control_console.py لتستخدم ترويسات الملك الموثوقة دون إضعاف منطق الفحص، وأثبت تشغيل الحزمتين الكاملتين في الأمر 9 اجتياز جميع الفحوص بنجاح (55 passed) برمز خروج 0.
(6) نعم: أعد مقعد gemini_3_8_flash مسباره المستقل تماماً probe_wi117_http_live.py في مساره المخصص، ونفذه عبر uvicorn الفعلي ومكتبة httpx، وأدرجت كتلتا شفرته وتشغيله (16 و 17) كاملتين دون أي اقتطاع في هذا الحكم.
PROBES: مسبار 1: كتلة الشفرة [16] · كتلة التشغيل [17] · الخاصيّةُ المستهدفة: محاولة تجاوز قيد require_king برمز مواطن (role=citizen) على مسارات خفض مفتاح الإيقاف في الحوكمة ولوحة التحكم، وإنشاء الترقية، وتجاوز البوابات، وتزوير توقيع الموافقة عبر طلبات HTTP حقيقية وخادم uvicorn حي، ومحاولة تعديل حالة النظام دون صلاحية ملكية · انكسرت؟ لا (رُفضت جميع محاولات المواطن بـ 403 وثبت بقاء المستوى دون تغيير، وقُبلت طلبات رمز الملك بـ 200 و 201 مع فرض هوية الموقع).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: أقرُّ بأنّني لم أقرأْ ولم أكتبْ خارجَ جذري /home/user/workspace/council_w701/gemini_3_8_flash/wi117/ واستنساخي الداخليِّ وهذه الإحاطة، ولم أطَّلع على عملِ المقاعدِ الأخرى ولا تقاريرِ المنفِّذ، واعتمدت كليًّا على إعادة التشغيل الذاتي والمسبار المستقل.
VERDICT: PASS لكلِّ المعاييرِ
