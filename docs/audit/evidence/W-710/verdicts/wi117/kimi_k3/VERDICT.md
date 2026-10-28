# حكمُ مقعدِ المجلسِ — kimi_k3 · جولةُ WI-117 (W-710)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في الجولةِ الواحدةِ (قرارُ المالكِ D27) على WI-117 — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w701/kimi_k3/wi117) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `305283d7c8677230663cfbb8735ecba94759b087da2d3b42543c6f45c30bc395`).

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
MODEL: Kimi (moonshotai) — مقعدُ kimi_k3 كما أسمتهُ المنصةُ في الإحاطة
FAMILY: Moonshot AI Kimi
RUN_DATE: 2026-10-28 06:17 +00:00
NODE: 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
CLONE_PATH: /home/user/workspace/council_w701/kimi_k3/wi117/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/
 2. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/)
 3. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
 5. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git show --stat f8d33807
 6. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git diff f8d33807^ f8d33807 -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
 7. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rg -n "require_king" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py
 8. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 9. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py
 10. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rm -rf ../old && git worktree add --detach ../old f8d33807^ && cp federal/executive/services/tests/test_wi117_king_guard_routes.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 11. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && sed -i "s/Depends(require_king)/Depends(require_auth)/g" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
 12. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && git status --short && git diff --stat
 13. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rg -n "D25-2|require_king" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 14. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && sha256sum docs/audit/evidence/W-701/briefs_wi117/briefing_kimi_k3.md
 15. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && cat docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS
 16. nl -ba /home/user/workspace/council_w701/kimi_k3/wi117/probe/probe_wi117_kimi_k3.py
 17. cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && PROBE_NODE=$(git rev-parse HEAD) .venv/bin/python /home/user/workspace/council_w701/kimi_k3/wi117/probe/probe_wi117_kimi_k3.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/)
EXIT: 0
BYTES: 1025
SHA256: 2cc661a1add06f3fab16140029ff6f753ea8cffd16df1fa15f04397d19e82a87
NO_EOL: 0
--- OUTPUT ---
HEAD is now at 147a0c6b W-701: توجيهُ المستشارِ 25 — قراراتُ المالكِ D27 بنصّها (إغلاقُ WI-113/WI-117/WI-119 بعدَ VERIFIED بإجماعٍ دونَ سؤالٍ جديدٍ · الجولةُ الآنَ لا بعدَ G1 — جولةٌ واحدةٌ بثلاثةِ نطاقاتٍ تُجمَعُ في الجلسةِ نفسِها Q-72) + واجبُ N+1 لـPR #168 (قراءةُ التشغيلِ 40478049851 بالفاحصِ فعلًا: مقروءٌ أخضرُ 13/13 على 129bed06 · EXIT 0) + انتقالٌ واحدٌ: WI-119 IN_PROGRESS→IN_REVIEW + إحاطاتُ الجولةِ التسعُ مبصومةً (3 مقاعدٍ × WI-117/WI-119/الكاشفُ من WI-115 · gemini · grok · kimi) ونصوصُ الإطلاقِ حرفيًّا وقياساتُ الجلسةِ خامًا (حوكمةُ الأعمالِ ✓ · راتشيتٌ 61 · حزمةُ الحوكمةِ 1394 خضراءَ) · لا شِّفرةَ سلوكيّةً · المنسِّقُ GLM-5.3 (Perplexity Computer)
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 1bacee57227e4261e1673f1ddaeefa87699b523ee2391c4837661e2e182c6d3c
NO_EOL: 0
--- OUTPUT ---
147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
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
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git show --stat f8d33807
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
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git diff f8d33807^ f8d33807 -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py
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
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rg -n "require_king" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py
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
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 0
BYTES: 2381
SHA256: c4b335c20474ddb97a1748bdc684264056cb7359d6fa62608495e0b002021928
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/kimi_k3/wi117/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, cov-7.1.0, anyio-4.15.1, platformdirs-4.13.7
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items

federal/executive/services/tests/test_wi117_king_guard_routes.py ....... [ 70%]
...                                                                      [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 10 passed, 1 warning in 1.23s =========================
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 0.98s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py
EXIT: 0
BYTES: 3024
SHA256: 96a847bd0215e0f10aebb2547f932782a9c9cc1d5e0f8fff47d58c64adf4b9c5
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/kimi_k3/wi117/repo/federal/executive/services
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
  /home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 55 passed, 1 warning in 6.96s =========================
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 0.83s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 1.61s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rm -rf ../old && git worktree add --detach ../old f8d33807^ && cp federal/executive/services/tests/test_wi117_king_guard_routes.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 2
BYTES: 3013
SHA256: f3aad4b654335ec1729eb1a4ea5f4ebdeaf01d117e53303eaaac59022fcfa7ef
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD b7bb6aa6)
HEAD is now at b7bb6aa6 W-688: انتقالُ WI-117 إلى IN_PROGRESS (دفعةٌ ورقيّةٌ تسبقُ دفعةَ الشِّفرةِ مباشرةً · إجراءُ DISC-137) + واجبُ N+1 لدفعةِ W-687 (حكما CI على 735b7631 مقروءانِ أخضرانِ 13/13) + إصلاحُ رابطَي WI-115 المؤجَّلُ (الإفصاحُ (ب) للتوجيهِ 24) · لا شِّفرةَ) · المنسِّقُ GLM-5.3 (Perplexity Computer)
/home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/kimi_k3/wi117/old/federal/executive/services
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
  /home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
ERROR federal/executive/services/tests/test_wi117_king_guard_routes.py - Type...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.85s ==========================
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && sed -i "s/Depends(require_king)/Depends(require_auth)/g" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py
EXIT: 1
BYTES: 4886
SHA256: 112d556deae2a92105ef32c35a17b8f22a45021ada26d71e573629c0f15273a9
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w701/kimi_k3/wi117/repo/federal/executive/services
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
  /home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_reset_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_promotions_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_governance_gates_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_console_reset_citizen_forbidden
FAILED federal/executive/services/tests/test_wi117_king_guard_routes.py::test_console_approval_citizen_forbidden
==================== 5 failed, 5 passed, 1 warning in 1.18s ====================
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 1.11s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 3.50s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && git status --short && git diff --stat
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rg -n "D25-2|require_king" docs/audit/SOVEREIGN_DECISION_REGISTER.md
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
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && sha256sum docs/audit/evidence/W-701/briefs_wi117/briefing_kimi_k3.md
EXIT: 0
BYTES: 125
SHA256: 8d8ad24a5de078875841801e12cc747b6b02abe5f42f90d87fa96eb9ce24d7dc
NO_EOL: 0
--- OUTPUT ---
980e4e5bc8432d8df99e02d5abda8fb7e531d65879de66c4705ba608041036db  docs/audit/evidence/W-701/briefs_wi117/briefing_kimi_k3.md
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && cat docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w701/kimi_k3/wi117/probe/probe_wi117_kimi_k3.py
EXIT: 0
BYTES: 14582
SHA256: dc366e011c20370a2cb4d1811f8c9492f129eee6e1795526c40f918631570f46
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""
     3	مسبارُ WI-117 الخاصُّ بمقعدِ kimi_k3 (البروتوكولُ § 4.9 — إلزاميٌّ)
     4	
     5	الهدف: إثباتُ أنَّ المساراتِ المحروسةَ بـ`require_king` ترفضُ رمزَ مواطنٍ (403)
     6	        دونَ أن يتغيّرَ مستوى مفتاحِ الإيقافِ، وأنَّ رمزَ الملكِ يمرُّ — عبرَ
     7	        **طلباتِ HTTP حقيقيّةٍ** على خدمتَينِ حيّتينِ مُقلِعتَينِ بـuvicorn
     8	        (governance على 9911 · control_console على 9912).
     9	النطاق: المساراتُ المحروسةُ الخمسةُ (الأربعةُ بنصِّ D25-2 + توقيعُ الموافقةِ
    10	        الذي حُصِّنَ بإلحاقِ قرارِ التوجيهِ 24 § 1):
    11	          governance      POST /v1/system/kill-switch/reset
    12	          governance      POST /v1/promotions
    13	          governance      POST /v1/promotions/{id}/gates
    14	          control_console POST /v1/kill-switch/reset
    15	          control_console POST /v1/approval
    16	        وتفعيلُ الزرِّ (activate) يُقاسُ فقط لإثباتِ أنّه تُرِكَ على حالِه بنصِّ
    17	        D25-2 — لا جزءًا من التحصينِ المحكومِ.
    18	المالك: مقعدُ kimi_k3 في مجلسِ المراجعةِ (جولةُ W-701 · نطاقُ WI-117)
    19	تاريخ الإنشاء: 2026-10-28
    20	الخاصيّةُ المستهدفَةُ: كسرُ «لا يصدُّ الحارسُ المواطنَ» — إن مرَّ طلبُ مواطنٍ
    21	        بغيرِ 403 فالمسبارُ يخرجُ رمزًا غيرَ صفريّ.
    22	"""
    23	
    24	from __future__ import annotations
    25	
    26	import json
    27	import os
    28	import socket
    29	import subprocess
    30	import sys
    31	import time
    32	import urllib.request
    33	from pathlib import Path
    34	
    35	REPO = Path("/home/user/workspace/council_w701/kimi_k3/wi117/repo")
    36	PY = REPO / ".venv" / "bin" / "python"
    37	PROOF_DIR = Path("/home/user/workspace/council_w701/kimi_k3/wi117/probe")
    38	GOV_PORT = 9911
    39	CONSOLE_PORT = 9912
    40	JWT_SECRET = "kimi_k3_probe_secret_at_least_32_characters_long"
    41	AMOS_DB = str(PROOF_DIR / "probe_wi117_kimi_k3.db")
    42	
    43	
    44	def wait_port(port: int, proc: subprocess.Popen, name: str, timeout: float = 45.0) -> None:
    45	    deadline = time.time() + timeout
    46	    while time.time() < deadline:
    47	        if proc.poll() is not None:
    48	            raise RuntimeError(f"{name} ماتَ مبكرًا برمزِ خروجٍ {proc.returncode}")
    49	        try:
    50	            with socket.create_connection(("127.0.0.1", port), timeout=1.0):
    51	                return
    52	        except OSError:
    53	            time.sleep(0.4)
    54	    raise RuntimeError(f"{name} لم يسمع على المنفذِ {port} خلال {timeout}s")
    55	
    56	
    57	def http_request(
    58	    method: str,
    59	    url: str,
    60	    token: str,
    61	    body: dict | None = None,
    62	) -> tuple[int, dict]:
    63	    data = None if body is None else json.dumps(body).encode("utf-8")
    64	    req = urllib.request.Request(url, data=data, method=method)
    65	    req.add_header("Authorization", f"Bearer {token}")
    66	    if data is not None:
    67	        req.add_header("Content-Type", "application/json")
    68	    try:
    69	        with urllib.request.urlopen(req, timeout=10) as resp:
    70	            payload = resp.read().decode("utf-8")
    71	            return resp.status, (json.loads(payload) if payload else {})
    72	    except urllib.error.HTTPError as err:
    73	        payload = err.read().decode("utf-8")
    74	        try:
    75	            parsed = json.loads(payload)
    76	        except ValueError:
    77	            parsed = {"raw": payload}
    78	        return err.code, parsed
    79	
    80	
    81	def expect(cond: bool, label: str, results: list[str]) -> bool:
    82	    results.append(f"{'PASS' if cond else 'FAIL'} · {label}")
    83	    return cond
    84	
    85	
    86	def main() -> int:
    87	    env = dict(
    88	        os.environ,
    89	        AMOS_JWT_SECRET=JWT_SECRET,
    90	        AMOS_ENVIRONMENT="test",
    91	        AMOS_DATABASE_URL=f"sqlite:///{AMOS_DB}",
    92	    )
    93	    # أسكِّ رموزًا من سرِّ الخدمةِ نفسِه قبلَ الإقلاع (النظامُ يصدِّقُ ما يوقَّع بسرِّه).
    94	    sys.path.insert(0, str(REPO / "federal" / "executive" / "services" / "src"))
    95	    for key in ("AMOS_JWT_SECRET", "AMOS_ENVIRONMENT", "AMOS_DATABASE_URL"):
    96	        os.environ[key] = env[key]
    97	    from amos_federation.common.auth import create_access_token
    98	
    99	    citizen_token = create_access_token(
   100	        "kimi_k3-citizen", ["governance:read", "governance:write"], role="citizen"
   101	    )
   102	    king_token = create_access_token("king", ["*"], role="king")
   103	
   104	    gov_proc = subprocess.Popen(
   105	        [str(PY), "-m", "uvicorn",
   106	         "amos_federation.services.governance.main:app",
   107	         "--host", "127.0.0.1", "--port", str(GOV_PORT)],
   108	        env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
   109	    )
   110	    console_proc = subprocess.Popen(
   111	        [str(PY), "-m", "uvicorn",
   112	         "amos_federation.services.control_console.main:app",
   113	         "--host", "127.0.0.1", "--port", str(CONSOLE_PORT)],
   114	        env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
   115	    )
   116	
   117	    results: list[str] = []
   118	    ok = True
   119	    try:
   120	        wait_port(GOV_PORT, gov_proc, "governance")
   121	        wait_port(CONSOLE_PORT, console_proc, "control_console")
   122	        time.sleep(1.0)  # اكتمالُ تهيئةِ التطبيق بعدَ فتحِ المقبس
   123	
   124	        gov = f"http://127.0.0.1:{GOV_PORT}"
   125	        con = f"http://127.0.0.1:{CONSOLE_PORT}"
   126	
   127	        # ── تهيئةٌ: ارفعِ الزرَّ إلى halt برمزِ مواطنٍ (مسارُ التفعيلِ يبقى على حالِه · D25-2) ──
   128	        st, body = http_request("POST", f"{gov}/v1/system/kill-switch", citizen_token,
   129	                                {"level": "halt", "reason": "kimi_k3 probe setup",
   130	                                 "activated_by": "kimi_k3"})
   131	        ok &= expect(st == 200 and body.get("level") == "halt",
   132	                     f"setup: activate(halt) برمزِ مواطنٍ على governance ⇒ {st} level={body.get('level')}",
   133	                     results)
   134	
   135	        # ── 1 · governance reset برمزِ مواطنٍ ⇒ 403 والمستوىُ لا يتغيّر ──
   136	        before = http_request("GET", f"{gov}/v1/system/status", citizen_token)[1].get("level")
   137	        st, body = http_request("POST", f"{gov}/v1/system/kill-switch/reset", citizen_token)
   138	        after = http_request("GET", f"{gov}/v1/system/status", citizen_token)[1].get("level")
   139	        ok &= expect(st == 403 and before == "halt" and after == "halt",
   140	                     f"POST /v1/system/kill-switch/reset (governance) برمزِ مواطنٍ ⇒ {st} · level قبل={before} بعد={after}",
   141	                     results)
   142	
   143	        # ── 2 · إنشاءُ ترقيةٍ برمزِ مواطنٍ ⇒ 403 ──
   144	        st, _ = http_request("POST", f"{gov}/v1/promotions", citizen_token,
   145	                             {"model_id": "kimi_k3-probe-model"})
   146	        ok &= expect(st == 403, f"POST /v1/promotions برمزِ مواطنٍ ⇒ {st}", results)
   147	
   148	        # ── 3 · فحصُ بوّابةٍ برمزِ مواطنٍ ⇒ 403 (والترقيةُ نفسُها أنشأها الملك) ──
   149	        st_create, created = http_request("POST", f"{gov}/v1/promotions", king_token,
   150	                                          {"model_id": "kimi_k3-probe-gates"})
   151	        promo_id = created.get("promotion_id", "missing")
   152	        ok &= expect(st_create == 201,
   153	                     f"setup: POST /v1/promotions برمزِ الملكِ ⇒ {st_create} id={promo_id}", results)
   154	        st, _ = http_request("POST", f"{gov}/v1/promotions/{promo_id}/gates", citizen_token,
   155	                             {"gate_name": "evaluation", "passed": True})
   156	        ok &= expect(st == 403,
   157	                     f"POST /v1/promotions/{promo_id}/gates برمزِ مواطنٍ ⇒ {st}", results)
   158	
   159	        # ── 4 · control_console reset برمزِ مواطنٍ ⇒ 403 والمستوىُ لا يتغيّر ──
   160	        before = http_request("GET", f"{gov}/v1/system/status", citizen_token)[1].get("level")
   161	        st, _ = http_request("POST", f"{con}/v1/kill-switch/reset", citizen_token)
   162	        after = http_request("GET", f"{gov}/v1/system/status", citizen_token)[1].get("level")
   163	        ok &= expect(st == 403 and before == "halt" and after == "halt",
   164	                     f"POST /v1/kill-switch/reset (control_console) برمزِ مواطنٍ ⇒ {st} · level قبل={before} بعد={after}",
   165	                     results)
   166	
   167	        # ── 5 · توقيعُ الموافقةِ برمزِ مواطنٍ ⇒ 403 ──
   168	        st, _ = http_request("POST", f"{con}/v1/approval", citizen_token,
   169	                             {"decision": "approve", "signed_by": "kimi_k3-spoof"})
   170	        ok &= expect(st == 403, f"POST /v1/approval برمزِ مواطنٍ ⇒ {st}", results)
   171	
   172	        # ── 6 · خارجَ النطاق: تفعيلُ الزرِّ يبقى على حالِه (رفعٌ صافٍ normal⇒halt برمزِ مواطنٍ) ──
   173	        # (الخفضُ المُقنَّعُ halt⇒alert عبرَ التفعيلِ يرفضُه الحدُّ السياديُّ بـ403 —
   174	        #  DISC-138 وcanary.py:lower_kill_switch — فالقياسُ هنا على رفعٍ صافٍ فقط)
   175	        http_request("POST", f"{gov}/v1/system/kill-switch/reset", king_token)  # مستوىٌ normal
   176	        st, body = http_request("POST", f"{con}/v1/kill-switch", citizen_token,
   177	                                {"level": "halt", "reason": "kimi_k3 scope check",
   178	                                 "activated_by": "kimi_k3"})
   179	        ok &= expect(st == 200 and body.get("level") == "halt",
   180	                     f"scope: POST /v1/kill-switch (activate · رفعٌ صافٍ) برمزِ مواطنٍ تُرِكَ على حالِه ⇒ {st} level={body.get('level')}",
   181	                     results)
   182	        # أعِدِ المستوىَ إلى halt لقياسِ الرفعِ الملكيِّ التالي
   183	        http_request("POST", f"{gov}/v1/system/kill-switch", citizen_token,
   184	                     {"level": "halt", "reason": "kimi_k3 restore halt", "activated_by": "kimi_k3"})
   185	
   186	        # ── 7 · رمزُ الملكِ يمرُّ على المساراتِ الأربعةِ ──
   187	        st, body = http_request("POST", f"{gov}/v1/system/kill-switch/reset", king_token)
   188	        lvl = http_request("GET", f"{gov}/v1/system/status", king_token)[1].get("level")
   189	        ok &= expect(st == 200 and lvl == "normal",
   190	                     f"king: POST /v1/system/kill-switch/reset (governance) ⇒ {st} · level={lvl}",
   191	                     results)
   192	
   193	        st, body = http_request("POST", f"{con}/v1/kill-switch", citizen_token,
   194	                                {"level": "halt", "reason": "kimi_k3 king-console setup",
   195	                                 "activated_by": "kimi_k3"})
   196	        st2, body2 = http_request("POST", f"{con}/v1/kill-switch/reset", king_token)
   197	        ok &= expect(st == 200 and st2 == 200 and body2.get("level") == "normal",
   198	                     f"king: POST /v1/kill-switch/reset (control_console) ⇒ {st2} · level={body2.get('level')}",
   199	                     results)
   200	
   201	        st, created = http_request("POST", f"{gov}/v1/promotions", king_token,
   202	                                   {"model_id": "kimi_k3-probe-king"})
   203	        promo_id = created.get("promotion_id", "missing")
   204	        ok &= expect(st == 201,
   205	                     f"king: POST /v1/promotions ⇒ {st} id={promo_id}", results)
   206	        st, body = http_request("POST", f"{gov}/v1/promotions/{promo_id}/gates", king_token,
   207	                                {"gate_name": "evaluation", "passed": True})
   208	        ok &= expect(st == 200,
   209	                     f"king: POST /v1/promotions/{promo_id}/gates ⇒ {st}", results)
   210	
   211	        st, body = http_request("POST", f"{con}/v1/approval", king_token,
   212	                                {"decision": "approve", "signed_by": "kimi_k3-spoof"})
   213	        ok &= expect(st == 200 and body.get("signed_by") == "king",
   214	                     f"king: POST /v1/approval ⇒ {st} · signed_by={body.get('signed_by')} (هويةُ الرمزِ لا جسمَ الطلبِ)",
   215	                     results)
   216	    finally:
   217	        for proc in (gov_proc, console_proc):
   218	            proc.terminate()
   219	        for proc in (gov_proc, console_proc):
   220	            try:
   221	                proc.wait(timeout=10)
   222	            except subprocess.TimeoutExpired:
   223	                proc.kill()
   224	
   225	    print("=== مسبارُ WI-117 (kimi_k3) — طلباتُ HTTP حقيقيّةٌ عبرَ uvicorn ===")
   226	    print(f"NODE: {os.environ.get('PROBE_NODE', '147a0c6b1357ddf0a93ba1c4d16e82e8648cb247')}")
   227	    print(f"PORT: governance={GOV_PORT} control_console={CONSOLE_PORT}")
   228	    print(f"DB: {AMOS_DB}")
   229	    print("--- النتائج ---")
   230	    for line in results:
   231	        print(line)
   232	    print("--- الحكم ---")
   233	    print("PROBE: PASS" if ok else "PROBE: FAIL")
   234	    return 0 if ok else 1
   235	
   236	
   237	if __name__ == "__main__":
   238	    sys.exit(main())
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && PROBE_NODE=$(git rev-parse HEAD) .venv/bin/python /home/user/workspace/council_w701/kimi_k3/wi117/probe/probe_wi117_kimi_k3.py
EXIT: 0
BYTES: 1588
SHA256: 5ac71c7599e1e403dcf4b65297600d374930ed7f88a419aed4da46ca84055d14
NO_EOL: 0
--- OUTPUT ---
=== مسبارُ WI-117 (kimi_k3) — طلباتُ HTTP حقيقيّةٌ عبرَ uvicorn ===
NODE: 147a0c6b1357ddf0a93ba1c4d16e82e8648cb247
PORT: governance=9911 control_console=9912
DB: /home/user/workspace/council_w701/kimi_k3/wi117/probe/probe_wi117_kimi_k3.db
--- النتائج ---
PASS · setup: activate(halt) برمزِ مواطنٍ على governance ⇒ 200 level=halt
PASS · POST /v1/system/kill-switch/reset (governance) برمزِ مواطنٍ ⇒ 403 · level قبل=halt بعد=halt
PASS · POST /v1/promotions برمزِ مواطنٍ ⇒ 403
PASS · setup: POST /v1/promotions برمزِ الملكِ ⇒ 201 id=promo-ae9890e5-b7a5-4249-981b-6da2e0404abb
PASS · POST /v1/promotions/promo-ae9890e5-b7a5-4249-981b-6da2e0404abb/gates برمزِ مواطنٍ ⇒ 403
PASS · POST /v1/kill-switch/reset (control_console) برمزِ مواطنٍ ⇒ 403 · level قبل=halt بعد=halt
PASS · POST /v1/approval برمزِ مواطنٍ ⇒ 403
PASS · scope: POST /v1/kill-switch (activate · رفعٌ صافٍ) برمزِ مواطنٍ تُرِكَ على حالِه ⇒ 200 level=halt
PASS · king: POST /v1/system/kill-switch/reset (governance) ⇒ 200 · level=normal
PASS · king: POST /v1/kill-switch/reset (control_console) ⇒ 200 · level=normal
PASS · king: POST /v1/promotions ⇒ 201 id=promo-1cfa0c75-c8f0-4cae-b014-4269e5944de7
PASS · king: POST /v1/promotions/promo-1cfa0c75-c8f0-4cae-b014-4269e5944de7/gates ⇒ 200
PASS · king: POST /v1/approval ⇒ 200 · signed_by=king (هويةُ الرمزِ لا جسمَ الطلبِ)
--- الحكم ---
PROBE: PASS
=== RAW [17] END ===
VERDICT_PER_CRITERION:
 1. المساراتُ الأربعةُ محروسةٌ بـrequire_king: نعم — RAW [7] يُظهرُ Depends(require_king) في governance/main.py:149 (reset) و:170 (promotions) و:203 (gates) وcontrol_console/main.py:211 (reset) و:233 (approval بالإلحاقِ)، وRAW [6] يُظهرُ الفرقَ من require_auth إلى require_king في التزامِ f8d33807، ونشأَ require_king نفسُه في auth.py قبلَ البندِ (يُصدُّ غيرَ الملكِ 403 كما في RAW [17]).
 2. مسبارٌ يشغّلُ طلبَ HTTP حقيقيًّا برمزِ مواطنٍ ويُثبتُ الرفضَ (403) وعدمَ تغييرِ المستوى: نعم — مسباري RAW [16]/RAW [17]: uvicorn حيٌّ على منفذين (governance:9911 · control_console:9912)، ورمزُ مواطنٍ على الأربعة+الموافقة ⇒ 403 ×5 ومستوى الزرِّ halt قبلًا وبعدًا في reset كلتيهما (level قبل=halt بعد=halt)، ولم يُنشأ promotion برمزِ مواطنٍ.
 3. رمزُ الملكِ يمرُّ: نعم — RAW [17]: الملكُ reset (governance) ⇒ 200 level=normal · reset (control_console) ⇒ 200 level=normal · promotions ⇒ 201 · gates ⇒ 200 · approval ⇒ 200 وsigned_by=king (هويةُ الرمزِ لا جسمَ الطلبِ)، وRAW [8] فحوصُ king_allowed الخمسةُ خضراءُ ضمنَ 10/10.
 4. مطفرةٌ تُسقِطُ القيدَ فيكتشفُها فحصٌ: نعم — أعدتُها بنفسي (RAW [11]): إسقاطُ Depends(require_king)→Depends(require_auth) من الملفَّينِ أسقطَ الفحوصَ الخمسةَ citizen_forbidden بتأكيدٍ دلاليٍّ (assert 200==403 و201==403) لا بخطأِ واجهةٍ، EXIT 1؛ وخطُّ الأساسِ أخضرُ قبلَها (RAW [8]: 10 passed) والشجرةُ نُظِّفَت بعدَها (RAW [12]: مخرجٌ فارغٌ تمامًا). والأمرُ 10 (RAW [10]) سقطَ بخطأِ استيرادٍ (PerTestAuthHeaders بلا وسيطِ role على الشجرةِ القديمةِ) فهو دليلُ تاريخٍ مكمّلٌ لا كافٍ وحدَه كما أُفصِح — والطفرةُ المعادَةُ هي الدليلُ الحاسمُ.
 5. الفحوصُ الستُّ التي مرتْ برمزِ مواطنٍ حُدِّثَت إلى رمزِ ملكٍ بلا إضعاف: نعم — RAW [9]: 55 passed (test_governance 27 + test_control_console 28) بلا سقوطٍ ولا skip؛ وفي الشجرةِ تُستعمَلُ KING_HEADERS بـrole="king" في مساراتِ reset/promotions/gates/approval (test_governance.py:18 · test_control_console.py:24-31) وفحصُ test_approval_ignores_spoofed_signer يؤكّدُ أنّ signed_by=king رغمَ انتحالِ الجسمِ — أي تشديدٌ لا إضعاف.
 6. مسبارٌ لكلِّ مقعدٍ: نعم — مسباري الخاصُّ محفوظٌ في probe/probe_wi117_kimi_k3.py ومُلتقَطٌ شِفرةً وتشغيلًا (RAW [16] · RAW [17]) وحُكمُه PROBE: PASS برمزِ خروجٍ 0.
PROBES: مسبارٌ واحدٌ: شِفرتُه كتلةُ RAW [16] · تشغيلُه كتلةُ RAW [17] · الخاصيّةُ التي حاولَ كسرَها: أن لا يصدَّ require_king رمزَ مواطنٍ على المساراتِ الخمسةِ المحروسةِ عبرَ HTTP حقيقيٍّ (وأن يتغيّرَ مستوى الزرِّ رغمَ الرفضِ) وأن لا يمرَّ رمزُ الملكِ — انكسرت؟ لا (كلُّ طلبِ مواطنٍ ⇒ 403 والمستوىُ ثابتٌ halt، وكلُّ طلبِ ملكٍ ⇒ مرورٌ سليمٌ، وactivate تُرِكَ على حالِه كما نصَّ D25-2).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: أقرُّ أنّي لم أقرأْ ولم أكتبْ خارجَ جذري /home/user/workspace/council_w701/kimi_k3/wi117/ إلّا كما يلي: استنسختُ المستودعَ بنفسي من GitHub (git clone https://github.com/vooovg-ui/AMOS-Fedration repo داخلَ جذري) وأعددتُ بيئتَه بـtools/dev/bootstrap.sh داخلَه؛ لم أقرأْ نسخةَ المنسِّقِ /home/user/workspace/amos ولا أدلّةَ المنفِّذِ docs/audit/evidence/W-68*/W-69*/W-70* (عدا ملفِّ الإحاطةِ وSHA256SUMS اللذين أمرتْ بهما الإحاطةُ في الأمرين 14 و15)، ولم أقرأْ مخرجاتِ مقعدٍ آخرَ ولا ذاكرةَ جلسةٍ أخرى.
VERDICT: PASS
