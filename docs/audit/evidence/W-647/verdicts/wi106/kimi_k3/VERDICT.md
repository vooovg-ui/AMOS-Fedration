# حكمُ مقعدِ المجلسِ — kimi_k3 (عائلةُ Moonshot AI Kimi) · جولةُ WI-106 (F1) (W-647)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-106 (F1) (الطابورُ الواحدُ · التوجيهُ 19 § 2 · بروتوكولُ Q-59) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذورِهِ الخاصّةِ (council_w620/kimi_k3) — منسوخٌ آليًّا، وما بعدَ الفاصلِ بايتًا ببايتٍ (sha256 `bb55aaf23a86bbc97745f1347e200803c994c44b3182bdf5becf3fa84609b83a`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-106 (F1) عندَ العقدةِ `8cd2f56d181648dad6f2d7ac6191536ae64bdf12` — إحاطةٌ مبصومةٌ ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-647) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-24

---
MODEL: Kimi (kimi_k3)
FAMILY: Moonshot AI
RUN_DATE: 2026-10-24 06:22 +00:00
NODE: 8cd2f56d181648dad6f2d7ac6191536ae64bdf12
CLONE_PATH: /home/user/workspace/council_w620/kimi_k3/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w620/kimi_k3/repo && git rev-parse HEAD
 2. cd /home/user/workspace/council_w620/kimi_k3/repo && bash tools/dev/bootstrap.sh
 3. cd /home/user/workspace/council_w620/kimi_k3/repo && git log --format='%h %cI %s' 5a7520c..HEAD
 4. cd /home/user/workspace/council_w620/kimi_k3/repo && git diff --stat 5a7520c HEAD
 5. cd /home/user/workspace/council_w620/kimi_k3/repo && git log --format='%h %cI %s' -3 -- docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md federal/executive/services/src/amos_federation/services/governance/federation.py
 6. cd /home/user/workspace/council_w620/kimi_k3/repo && git diff 5a7520c HEAD -- federal/executive/services/tests/test_federation.py tests/sovereignty core/sovereignty
 7. cd /home/user/workspace/council_w620/kimi_k3/repo && git diff 5a7520c HEAD -- federal/executive/services/src/amos_federation/services/governance/federation.py
 8. cd /home/user/workspace/council_w620/kimi_k3/repo && cat federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py
 9. cd /home/user/workspace/council_w620/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 10. cd /home/user/workspace/council_w620/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py -q
 11. cd /home/user/workspace/council_w620/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_federation.py -q
 12. cd /home/user/workspace/council_w620/kimi_k3/repo && .venv/bin/python -m pytest tests/sovereignty -q
 13. cd /home/user/workspace/council_w620/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
 14. cd /home/user/workspace/council_w620/kimi_k3/repo && cat docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md
 15. cd /home/user/workspace/council_w620/kimi_k3/repo && cat docs/audit/evidence/W-615/federation_sites_before.txt docs/audit/evidence/W-617/federation_sites_after.txt
 16. cd /home/user/workspace/council_w620/kimi_k3/repo && cat docs/audit/evidence/W-617/mutation_probe_wi106.py docs/audit/evidence/W-617/mutation_probe_wi106.out.txt
 17. cd /home/user/workspace/council_w620/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_seat.db .venv/bin/python docs/audit/evidence/W-617/mutation_probe_wi106.py
 18. cd /home/user/workspace/council_w620/kimi_k3/repo && rg -n "D17-1|Q-61" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 19. cd /home/user/workspace/council_w620/kimi_k3/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q
 20. cd /home/user/workspace/council_w620/kimi_k3/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
 21. find /home/user/workspace/council_w620/kimi_k3 -maxdepth 1
 22. nl -ba /home/user/workspace/council_w620/kimi_k3/probe/probe_wi106_kimi_k3.py
 23. cd /home/user/workspace/council_w620/kimi_k3/repo && cp /home/user/workspace/council_w620/kimi_k3/probe/probe_wi106_kimi_k3.py federal/executive/services/tests/test_probe_wi106_kimi_k3.py && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_probe.db .venv/bin/python -m pytest federal/executive/services/tests/test_probe_wi106_kimi_k3.py -q
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: a32ca78d353b39f55972190b7d244482c9cd033d9dee7bea557443f2c77f58bb
NO_EOL: 0
--- OUTPUT ---
8cd2f56d181648dad6f2d7ac6191536ae64bdf12
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && bash tools/dev/bootstrap.sh
EXIT: 0
BYTES: 1286
SHA256: 01a6e4aabf6e93d457b26c8d7716cf0b139aadb3313fc149dfac4f6d70f38965
NO_EOL: 0
--- OUTPUT ---
• الجذر: /home/user/workspace/council_w620/kimi_k3/repo
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
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && git log --format='%h %cI %s' 5a7520c..HEAD
EXIT: 0
BYTES: 2568
SHA256: 1821f057405e9321cc0f693055b0a3a04bfe5dd3831d2ee4c3a56a05018f102e
NO_EOL: 0
--- OUTPUT ---
8cd2f56d 2026-10-22T14:29:48Z W-620: حكمُ CI أخضرُ مقروءًا على 80e4394 (39784257293 · 13/13) + التقديمُ السريعُ لـmain بإذنِ المالكِ (296a276 ← 80e4394 · PR #122/#123 MERGED) + تصحيحٌ مؤرَّخٌ لإحاطاتِ جولةِ F1 قبلَ الإطلاقِ إلى 80e4394 (فرقُ شِفرةٍ فارغٌ مقيسًا · سابقةُ W-596/W-598) — لا شِفرةَ · المنسِّقُ GLM-5.3
80e43949 2026-10-22T13:07:27Z W-619: تصحيحُ حمرةِ CI على 07b4dcf (39778902085 · E401 في مسبارِ W-615 — فصلُ استيرادٍ · المخرجُ مقيسًا لم يتغير: طابقَ المسجَّلَ سطرًا بسطرٍ) — لا شِفرةَ إنتاجيّةً · DISC-125 قائمٌ (إحالةٌ مؤرَّخةٌ) · منفِّذٌ جديدٌ يستلمُ الجلسةَ · المنسِّقُ GLM-5.3
07b4dcf5 2026-10-22T12:29:34Z W-618: WI-106 IN_PROGRESS→IN_REVIEW (H3) + إحاطاتُ جولةِ F1 مُبصَمةً على fd6c1af (gemini_3_8_flash · grok_4_7 · kimi_k3 · مسبارٌ لكلِّ مقعدٍ) — لا شِفرةَ · المنسِّقُ Claude Opus 5.5
fd6c1af3 2026-10-22T12:23:36Z W-617: شِفرةُ F1 — سطوحُ federation.py الـ15 تعبرُ الحدَّ السياديَّ (coordinate · EXECUTIVE) · T1–T8 · M1–M5 قُتِلَت · الدَّينُ 181→166 · العابرةُ 18→33 · المواضعُ 220→236 مقيسًا — WI-106 باقٍ IN_PROGRESS · المنسِّقُ Claude Opus 5.5
c4939391 2026-10-22T12:12:14Z W-616: حكمُ CI N+1 (PR #122 · 5a7520c و main 296a276: READABLE 13/13 أخضرُ) + مساراتُ WI-106 تُعلِنُ لقطاتِ القياسِ قبلَ الشِّفرةِ (سابقةُ W-594) — لا شِفرةَ · المنسِّقُ Claude Opus 5.5
e5ce7612 2026-10-22T11:37:56Z W-615: WI-106 RESERVED → IN_PROGRESS + ملحقُ تصميمِ F1 (D1–D8 · متوقَّعٌ D-4 181←166) في التزامٍ مستقلٍّ قبلَ الشِّفرةِ (Q-61) + قياسُ ما قبلُ — لا شِفرةَ · المنسِّقُ Claude Opus 5.5
c6c3f64a 2026-10-22T11:33:09Z W-614: WI-106 READY → RESERVED (حتى 2026-11-21 · H3) — لا شِفرةَ · المنسِّقُ Claude Opus 5.5
6b643a29 2026-10-22T11:32:27Z W-613: تسجيلُ WI-106 (الدفعةُ F1 · governance/federation.py بفاعلٍ تنفيذيٍّ مُعلَنٍ بالفعلِ coordinate · D17-1) READY + قياسُ ما قبلُ (D-4 181) — لا شِفرةَ · المنسِّقُ Claude Opus 5.5
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && git diff --stat 5a7520c HEAD
EXIT: 0
BYTES: 2998
SHA256: d43cac83470c600636f980c26a4db694df952cbb05d34237802d02ff9b7b9860
NO_EOL: 0
--- OUTPUT ---
 PROJECT_STATE.md                                   |   4 +-
 docs/PROJECT_HANDBOOK.md                           |   6 +-
 docs/audit/ACTIVE_EXECUTION_STATE.md               |   2 +-
 docs/audit/COMPLETION_LEDGER.md                    |  16 +
 docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md      |  93 +++
 docs/audit/TRUTH_MATRIX.md                         |   6 +-
 docs/audit/evidence/W-615/README.md                |  22 +
 .../evidence/W-615/federation_sites_before.txt     |  18 +
 docs/audit/evidence/W-615/inventory_before.txt     |  46 ++
 .../evidence/W-615/probe_coordinate_actors.out.txt |   7 +
 .../evidence/W-615/probe_coordinate_actors.py      |  18 +
 docs/audit/evidence/W-616/README.md                |  21 +
 .../evidence/W-616/ci_jobs_39768670038.api.txt     |   1 +
 .../evidence/W-616/ci_jobs_39770632794.api.txt     |   1 +
 .../evidence/W-616/ci_verdict_39768670038.txt      |   7 +
 .../evidence/W-616/ci_verdict_39770632794.txt      |   7 +
 docs/audit/evidence/W-617/README.md                |  39 +
 .../evidence/W-617/federation_sites_after.txt      |  33 +
 docs/audit/evidence/W-617/inventory_after.txt      |  43 ++
 .../evidence/W-617/mutation_probe_wi106.out.txt    |  13 +
 docs/audit/evidence/W-617/mutation_probe_wi106.py  | 100 +++
 docs/audit/evidence/W-617/services_suite_tail.txt  |   3 +
 .../evidence/W-617/t1_t8_and_test_federation.txt   |   1 +
 docs/audit/evidence/W-618/README.md                |  21 +
 docs/audit/evidence/W-618/TASKS_SENT.md            |  35 +
 docs/audit/evidence/W-618/briefs/README.md         |  25 +
 docs/audit/evidence/W-618/briefs/SHA256SUMS        |   4 +
 .../W-618/briefs/briefing_gemini_3_8_flash.md      | 145 ++++
 .../evidence/W-618/briefs/briefing_grok_4_7.md     | 145 ++++
 .../evidence/W-618/briefs/briefing_kimi_k3.md      | 145 ++++
 docs/audit/evidence/W-619/README.md                |  22 +
 .../evidence/W-619/ci_jobs_39778902085.api.txt     |   1 +
 .../evidence/W-619/ci_verdict_39778902085_red.txt  |   9 +
 docs/audit/evidence/W-619/session_measurements.txt |  51 ++
 docs/audit/evidence/W-620/README.md                |  22 +
 .../evidence/W-620/ci_jobs_39784257293.api.txt     |   1 +
 .../W-620/ci_verdict_39784257293_green.txt         |   6 +
 docs/audit/evidence/W-620/session_measurements.txt |  24 +
 docs/audit/measurements/decision_gate_ledger.json  |  16 +
 docs/audit/measurements/decision_wave_map.json     |   6 +-
 docs/audit/measurements/final_audit_p14.json       |  23 +-
 docs/audit/measurements/write_inventory_p13.json   | 259 ++++++-
 docs/audit/truth_matrix.json                       |  34 +-
 docs/governance/work/ACTIVE_WORK.md                |  37 +-
 docs/governance/work/DISCOVERIES.md                |   4 +-
 .../services/governance/federation.py              | 788 ++++++++++++++++-----
 .../test_wi106_federation_coordinate_sovereign.py  | 420 +++++++++++
 .../test_q3_branch_declaration_surface.py          |  41 +-
 48 files changed, 2529 insertions(+), 262 deletions(-)
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && git log --format='%h %cI %s' -3 -- docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md federal/executive/services/src/amos_federation/services/governance/federation.py
EXIT: 0
BYTES: 844
SHA256: 065ea81d01bde30dd6eb36b8baf175202d7132d6c8ab1f243fda6b4bcbec4c1b
NO_EOL: 0
--- OUTPUT ---
fd6c1af3 2026-10-22T12:23:36Z W-617: شِفرةُ F1 — سطوحُ federation.py الـ15 تعبرُ الحدَّ السياديَّ (coordinate · EXECUTIVE) · T1–T8 · M1–M5 قُتِلَت · الدَّينُ 181→166 · العابرةُ 18→33 · المواضعُ 220→236 مقيسًا — WI-106 باقٍ IN_PROGRESS · المنسِّقُ Claude Opus 5.5
e5ce7612 2026-10-22T11:37:56Z W-615: WI-106 RESERVED → IN_PROGRESS + ملحقُ تصميمِ F1 (D1–D8 · متوقَّعٌ D-4 181←166) في التزامٍ مستقلٍّ قبلَ الشِّفرةِ (Q-61) + قياسُ ما قبلُ — لا شِفرةَ · المنسِّقُ Claude Opus 5.5
68a087c9 2026-08-22T09:55:00Z W-027 · T3.5: الارتداداتُ الصامتةُ 26 ← 0 — وأربعةٌ منها كانت في أدواتِ القياسِ نفسِها
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && git diff 5a7520c HEAD -- federal/executive/services/tests/test_federation.py tests/sovereignty core/sovereignty
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && git diff 5a7520c HEAD -- federal/executive/services/src/amos_federation/services/governance/federation.py
EXIT: 0
BYTES: 43792
SHA256: fe1057cf4a497e5c70e92b0c2875ad19abc7815fde0795ed408f00f785870c76
NO_EOL: 0
--- OUTPUT ---
diff --git a/federal/executive/services/src/amos_federation/services/governance/federation.py b/federal/executive/services/src/amos_federation/services/governance/federation.py
index 0f2eaa54..6fec4ce7 100644
--- a/federal/executive/services/src/amos_federation/services/governance/federation.py
+++ b/federal/executive/services/src/amos_federation/services/governance/federation.py
@@ -6,6 +6,7 @@ AMOS-Federation Full Governance + Federal Institutions (Phase 9)
 تاريخ الإنشاء: 2026-08-15
 """
 
+import copy
 import hashlib
 import uuid
 from datetime import UTC, datetime
@@ -25,9 +26,16 @@ from sqlalchemy import (
     desc,
     select,
 )
+from sqlalchemy import inspect as sa_inspect
 from sqlalchemy.orm import DeclarativeBase
 
 from amos_federation.common.database import get_database_url, get_session_factory
+from amos_federation.services.executive_core.sovereignty_bridge import (
+    ConstitutionalAuthorizer,
+    compensator,
+    declared_effect,
+    operation_key,
+)
 
 
 class _GovBase(DeclarativeBase):
@@ -148,6 +156,113 @@ class ComplianceReportModel(_GovBase):
     created_at = Column(DateTime, default=lambda: datetime.now(UTC))
 
 
+# === F1 · العبورُ السياديُّ (WI-106 · قرارُ المالكِ D17-1 · التصميمُ docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md) ===
+
+#: فاعلُ الوحدةِ (D1): «تنسيق لا سلطة» (Q-24) — فاعلٌ تنفيذيٌّ مُعلَنٌ **ثابتًا في الوحدةِ لا
+#: معاملًا للمُنادي**، على سابقةِ `rulings.JUDICIARY_ACTOR` (J1 · D1). والاختبارُ يُبدِّلُه
+#: بـ`monkeypatch` على هذا الثابتِ لا بمعاملٍ إنتاجيّ.
+FEDERATION_ACTOR = "EXECUTIVE"
+
+#: فعلُ الوحدةِ (D2): نصُّ قرارِ المالكِ D17-1 حرفيًّا — فعلٌ واحدٌ للأسطحِ الخمسةَ عشرَ كلِّها،
+#: واسمُ العمليّةِ يُحمَلُ في البياناتِ والنطاقِ لا في فعلٍ مُخترَعٍ (ذلك سؤالُ Q-2).
+FEDERATION_VERB = "coordinate"
+
+_DEFAULT_FEDERATION_AUTHORIZER: ConstitutionalAuthorizer | None = None
+
+
+def _federation_authorizer() -> ConstitutionalAuthorizer:
+    """المُصرِّحُ الافتراضيُّ بفاعلِ الوحدةِ المُسمّى — واحدٌ للوحدةِ (D1)."""
+    global _DEFAULT_FEDERATION_AUTHORIZER
+    if _DEFAULT_FEDERATION_AUTHORIZER is None:
+        _DEFAULT_FEDERATION_AUTHORIZER = ConstitutionalAuthorizer(actor=FEDERATION_ACTOR)
+    return _DEFAULT_FEDERATION_AUTHORIZER
+
+
+def reset_federation_authorizer() -> None:
+    """أفرِغِ المُفوِّضَ المحفوظَ — للاختباراتِ التي تبدّلُ الفاعلَ (D1)."""
+    global _DEFAULT_FEDERATION_AUTHORIZER
+    _DEFAULT_FEDERATION_AUTHORIZER = None
+
+
+class FederationReplayError(ValueError):
+    """مفتاحٌ طبيعيٌّ عبرَ بنجاحٍ من قبلُ — الإعادةُ ليست نجاحًا ثانيًا ولا كتابةً ثانيةً (D6)."""
+
+
+def _nonce() -> str:
+    """مُعرِّفُ استدعاءٍ (D3) حيثُ يُشرَعُ تكرارُ الفعلِ على الكيانِ نفسِه."""
+    return uuid.uuid4().hex
+
+
+class _FederationUndo:
+    """سجلُّ تراجعٍ لعبورٍ واحدٍ (D7): ما أُنشِئَ وما كانَ قبلَ التغييرِ — ومُعوِّضُه.
+
+    المُطبِّقُ يُسجِّلُ قبلَ الكتابةِ؛ والحدُّ يُنادي `_restore` آليًّا إن فشلَ تثبيتُ النجاحِ
+    بعدَ الالتزامِ (قرارُ المالكِ Q-70). استعادةٌ تقنيّةٌ في جلسةٍ جديدةٍ — «الحذفُ شأنٌ
+    تنفيذيٌّ» والمُعوِّضُ ليس أثرًا مُعلَنًا ولا تراجعُه البوابة.
+    """
+
+    def __init__(self) -> None:
+        self._created: list[tuple[type, Any]] = []
+        self._prior: list[tuple[type, Any, dict[str, Any]]] = []
+
+    def created(self, row: Any) -> None:
+        self._created.append((type(row), sa_inspect(row).identity or _row_pk(row)))
+
+    def prior(self, row: Any, *columns: str) -> None:
+        values = {column: copy.deepcopy(getattr(row, column)) for column in columns}
+        self._prior.append((type(row), sa_inspect(row).identity, values))
+
+    def _restore(self) -> None:
+        session = get_session_factory()()
+        try:
+            for model, identity in reversed(self._created):
+                row = session.get(model, identity)
+                if row is not None:
+                    session.delete(row)
+            for model, identity, values in reversed(self._prior):
+                row = session.get(model, identity)
+                if row is not None:
+                    for column, value in values.items():
+                        setattr(row, column, value)
+            session.commit()
+        finally:
+            session.close()
+
+
+def _row_pk(row: Any) -> tuple[Any, ...]:
+    """المفتاحُ الأساسيُّ لصفٍّ لم يُدفَعْ بعدُ — من أعمدتِه المُعلَنةِ لا تخمينًا."""
+    return tuple(getattr(row, column.key) for column in type(row).__mapper__.primary_key)
+
+
+def _crossing(
+    operation: str, kind: str, suffix: str, detail: str, undo: _FederationUndo
+) -> tuple[str, dict[str, Any]]:
+    """عقدُ عبورٍ واحدٍ (D3): الهدفُ = قيمةُ المفتاحِ · أثرٌ مُعلَنٌ · مُعوِّضُه · اسمُ العمليّة."""
+    target = f"federation/{suffix}"
+    effect = declared_effect(kind, target, detail)
+    return target, {
+        "declared_effects": (effect,),
+        "operation_key": operation_key(f"federation.{operation}", suffix),
+        "compensators": (
+            compensator(
+                effect.signature,
+                undo._restore,
+                "استعادةٌ تقنيّةٌ: حذفُ ما أُنشِئَ وإرجاعُ ما تغيَّرَ — العمليّةُ لم تثبتْ",
+            ),
+        ),
+        "metadata": {"operation": operation},
+    }
+
+
+def _refuse_replay(guarded: Any, operation: str, target: str) -> None:
+    """الإعادةُ على مفتاحٍ طبيعيٍّ تُرفَعُ صريحةً بلا كتابةٍ ثانيةٍ (D6)."""
+    if guarded.is_replay:
+        raise FederationReplayError(
+            f"العمليّةُ «{operation}» على «{target}» عبرَت الحدَّ بنجاحٍ من قبلُ — "
+            "الإعادةُ ليست نجاحًا ثانيًا"
+        )
+
+
 # === 9.1: Expanded Policy Engine ===
 
 POLICY_RULES_EXPANDED = [
@@ -356,30 +471,39 @@ class ApprovalSystem:
         public_key_hex: str,
         notes: str = "",
     ) -> dict[str, Any]:
-        """طلب موافقة مع توقيع Ed25519."""
+        """طلب موافقة مع توقيع Ed25519 — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
         approval_id = str(uuid.uuid4())
         message = f"{request_type}:{target_id}:{requester}:{approval_id}"
         signature = self.signer.sign(private_key_hex, message)
         verified = self.signer.verify(public_key_hex, message, signature)
+        undo = _FederationUndo()
 
-        session = get_session_factory()()
-        try:
-            record = ApprovalModel(
-                id=approval_id,
-                request_type=request_type,
-                target_id=target_id,
-                requester=requester,
-                decision="pending",
-                signed_by=requester,
-                signature=signature,
-                public_key=public_key_hex,
-                verified=verified,
-                notes=notes,
-            )
-            session.add(record)
-            session.commit()
-        finally:
-            session.close()
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = ApprovalModel(
+                    id=approval_id,
+                    request_type=request_type,
+                    target_id=target_id,
+                    requester=requester,
+                    decision="pending",
+                    signed_by=requester,
+                    signature=signature,
+                    public_key=public_key_hex,
+                    verified=verified,
+                    notes=notes,
+                )
+                undo.created(record)
+                session.add(record)
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "ApprovalSystem.request_approval"
+        target, crossing = _crossing(
+            operation, "CREATE", f"approvals/{approval_id}/request", "طلبُ موافقةٍ موقَّعٍ", undo
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
 
         from amos_federation.common.event_bus import get_event_bus
 
@@ -409,34 +533,56 @@ class ApprovalSystem:
         approver_public_key: str,
         notes: str = "",
     ) -> dict[str, Any]:
-        """موافقة أو رفض مع توقيع."""
+        """موافقة أو رفض مع توقيع — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
         if decision not in ["approve", "reject"]:
             raise ValueError("القرار يجب أن يكون approve أو reject")
 
+        # D5: التحقُّقُ قبلَ العبورِ — الرسائلُ والأنواعُ كما كانت
         session = get_session_factory()()
         try:
-            record = session.execute(
+            existing = session.execute(
                 select(ApprovalModel).where(ApprovalModel.id == approval_id)
             ).scalar_one_or_none()
-            if not record:
+            if not existing:
                 raise ValueError("الموافقة غير موجودة")
-            if record.decision != "pending":
-                raise ValueError(f"الموافقة已 تم البت فيها: {record.decision}")
-
-            message = f"{approval_id}:{decision}:{approver_public_key}"
-            signature = self.signer.sign(approver_private_key, message)
-            verified = self.signer.verify(approver_public_key, message, signature)
-
-            record.decision = decision
-            record.signed_by = approver_public_key[:16]  # identifier
-            record.signature = signature
-            record.public_key = approver_public_key
-            record.verified = verified
-            record.notes = notes
-            session.commit()
+            if existing.decision != "pending":
+                raise ValueError(f"الموافقة已 تم البت فيها: {existing.decision}")
         finally:
             session.close()
 
+        message = f"{approval_id}:{decision}:{approver_public_key}"
+        signature = self.signer.sign(approver_private_key, message)
+        verified = self.signer.verify(approver_public_key, message, signature)
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(ApprovalModel).where(ApprovalModel.id == approval_id)
+                ).scalar_one()
+                undo.prior(
+                    record, "decision", "signed_by", "signature", "public_key", "verified", "notes"
+                )
+                record.decision = decision
+                record.signed_by = approver_public_key[:16]  # identifier
+                record.signature = signature
+                record.public_key = approver_public_key
+                record.verified = verified
+                record.notes = notes
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "ApprovalSystem.decide_approval"
+        target, crossing = _crossing(
+            operation, "WRITE", f"approvals/{approval_id}/decide", "البتُّ في موافقةٍ", undo
+        )
+        guarded = _federation_authorizer().guard_declared(
+            FEDERATION_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, operation, target)
+
         from amos_federation.common.event_bus import get_event_bus
 
         get_event_bus().publish(
@@ -518,24 +664,34 @@ class PromotionSystem:
         _GovBase.metadata.create_all(engine)
 
     def start_promotion(self, target_type: str, target_id: str, requester: str) -> dict[str, Any]:
-        """بدء عملية ترقية."""
+        """بدء عملية ترقية — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
         promotion_id = str(uuid.uuid4())
         gates: list[dict] = []
-        session = get_session_factory()()
-        try:
-            for gate_name in GATE_ORDER:
-                gate = PromotionGateModel(
-                    id=str(uuid.uuid4()),
-                    target_type=target_type,
-                    target_id=target_id,
-                    gate=gate_name,
-                    status="pending",
-                )
-                session.add(gate)
-                gates.append({"gate": gate_name, "status": "pending"})
-            session.commit()
-        finally:
-            session.close()
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                for gate_name in GATE_ORDER:
+                    gate = PromotionGateModel(
+                        id=str(uuid.uuid4()),
+                        target_type=target_type,
+                        target_id=target_id,
+                        gate=gate_name,
+                        status="pending",
+                    )
+                    undo.created(gate)
+                    session.add(gate)
+                    gates.append({"gate": gate_name, "status": "pending"})
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "PromotionSystem.start_promotion"
+        target, crossing = _crossing(
+            operation, "CREATE", f"promotions/{promotion_id}/start", "بواباتُ الترقيةِ الخمس", undo
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
 
         from amos_federation.common.event_bus import get_event_bus
 
@@ -557,13 +713,13 @@ class PromotionSystem:
     def pass_gate(
         self, target_type: str, target_id: str, gate: str, result: dict
     ) -> dict[str, Any]:
-        """اجتياز بوابة محددة."""
+        """اجتياز بوابة محددة — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
         if gate not in GATE_ORDER:
             raise ValueError(f"بوابة غير معروفة: {gate}")
 
+        # D5: التحقُّقُ قبلَ العبورِ — البواباتُ السابقةُ ووجودُ البوابةِ كما كانا
         session = get_session_factory()()
         try:
-            # التحقق من البوابات السابقة
             for prev_gate in GATE_ORDER:
                 if prev_gate == gate:
                     break
@@ -575,20 +731,44 @@ class PromotionSystem:
                 ).scalar_one_or_none()
                 if not prev or prev.status != "passed":
                     raise ValueError(f"بوابة {prev_gate} لم تُجتز بعد")
-
-            record = session.execute(
+            session.execute(
                 select(PromotionGateModel)
                 .where(PromotionGateModel.target_type == target_type)
                 .where(PromotionGateModel.target_id == target_id)
                 .where(PromotionGateModel.gate == gate)
             ).scalar_one()
-            record.status = "passed"
-            record.result = result
-            record.completed_at = datetime.now(UTC)
-            session.commit()
         finally:
             session.close()
 
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(PromotionGateModel)
+                    .where(PromotionGateModel.target_type == target_type)
+                    .where(PromotionGateModel.target_id == target_id)
+                    .where(PromotionGateModel.gate == gate)
+                ).scalar_one()
+                undo.prior(record, "status", "result", "completed_at")
+                record.status = "passed"
+                record.result = result
+                record.completed_at = datetime.now(UTC)
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "PromotionSystem.pass_gate"
+        target, crossing = _crossing(
+            operation,
+            "WRITE",
+            f"promotions/{target_type}:{target_id}/{gate}/pass/{_nonce()}",
+            "اجتيازُ بوابةِ ترقيةٍ",
+            undo,
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
+
         from amos_federation.common.event_bus import get_event_bus
 
         get_event_bus().publish(
@@ -602,22 +782,48 @@ class PromotionSystem:
         return {"gate": gate, "status": "passed", "result": result}
 
     def fail_gate(self, target_type: str, target_id: str, gate: str, reason: str) -> dict[str, Any]:
-        """رسوب في بوابة."""
+        """رسوب في بوابة — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
+        # D5: وجودُ البوابةِ قبلَ العبورِ — النوعُ كما كانَ (`NoResultFound`)
         session = get_session_factory()()
         try:
-            record = session.execute(
+            session.execute(
                 select(PromotionGateModel)
                 .where(PromotionGateModel.target_type == target_type)
                 .where(PromotionGateModel.target_id == target_id)
                 .where(PromotionGateModel.gate == gate)
             ).scalar_one()
-            record.status = "failed"
-            record.result = {"reason": reason}
-            record.completed_at = datetime.now(UTC)
-            session.commit()
         finally:
             session.close()
 
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(PromotionGateModel)
+                    .where(PromotionGateModel.target_type == target_type)
+                    .where(PromotionGateModel.target_id == target_id)
+                    .where(PromotionGateModel.gate == gate)
+                ).scalar_one()
+                undo.prior(record, "status", "result", "completed_at")
+                record.status = "failed"
+                record.result = {"reason": reason}
+                record.completed_at = datetime.now(UTC)
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "PromotionSystem.fail_gate"
+        target, crossing = _crossing(
+            operation,
+            "WRITE",
+            f"promotions/{target_type}:{target_id}/{gate}/fail/{_nonce()}",
+            "رسوبٌ في بوابةِ ترقيةٍ",
+            undo,
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
+
         from amos_federation.common.event_bus import get_event_bus
 
         get_event_bus().publish(
@@ -700,7 +906,7 @@ class ExecutiveBranch:
             session.close()
 
     def appoint(self, role_name: str, agent_id: str) -> dict[str, Any]:
-        """تعيين وكيل في دور تنفيذي."""
+        """تعيين وكيل في دور تنفيذي — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
         if role_name not in [r["role_name"] for r in EXECUTIVE_ROLES]:
             raise ValueError(f"دور غير معروف: {role_name}")
 
@@ -710,18 +916,41 @@ class ExecutiveBranch:
         if not agent:
             raise ValueError(f"الوكيل {agent_id} غير موجود")
 
+        # D5: وجودُ الدورِ قبلَ العبورِ — النوعُ كما كانَ (`NoResultFound`)
         session = get_session_factory()()
         try:
-            record = session.execute(
+            session.execute(
                 select(ExecutiveRoleModel).where(ExecutiveRoleModel.role_name == role_name)
             ).scalar_one()
-            record.agent_id = agent_id
-            record.status = "filled"
-            record.appointed_at = datetime.now(UTC)
-            session.commit()
         finally:
             session.close()
 
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(ExecutiveRoleModel).where(ExecutiveRoleModel.role_name == role_name)
+                ).scalar_one()
+                undo.prior(record, "agent_id", "status", "appointed_at")
+                record.agent_id = agent_id
+                record.status = "filled"
+                record.appointed_at = datetime.now(UTC)
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "ExecutiveBranch.appoint"
+        target, crossing = _crossing(
+            operation,
+            "WRITE",
+            f"executive_roles/{role_name}/appoint/{_nonce()}",
+            "تعيينُ وكيلٍ في دورٍ تنفيذيٍّ",
+            undo,
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
+
         from amos_federation.common.event_bus import get_event_bus
 
         get_event_bus().publish(
@@ -799,21 +1028,31 @@ class LegislativeBranch:
         _GovBase.metadata.create_all(engine)
 
     def propose(self, title: str, body: str, proposer: str) -> dict[str, Any]:
-        """اقتراح قانون جديد."""
+        """اقتراح قانون جديد — سجلُّ تنسيقٍ لا سلطةٌ (Q-24) · يعبرُ بالفعلِ `coordinate` (F1)."""
         leg_id = str(uuid.uuid4())
-        session = get_session_factory()()
-        try:
-            record = LegislationModel(
-                id=leg_id,
-                title=title,
-                body=body,
-                proposer=proposer,
-                status="proposed",
-            )
-            session.add(record)
-            session.commit()
-        finally:
-            session.close()
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = LegislationModel(
+                    id=leg_id,
+                    title=title,
+                    body=body,
+                    proposer=proposer,
+                    status="proposed",
+                )
+                undo.created(record)
+                session.add(record)
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "LegislativeBranch.propose"
+        target, crossing = _crossing(
+            operation, "CREATE", f"legislations/{leg_id}/propose", "اقتراحُ قانونٍ", undo
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
 
         from amos_federation.common.event_bus import get_event_bus
 
@@ -828,92 +1067,196 @@ class LegislativeBranch:
         return {"legislation_id": leg_id, "title": title, "status": "proposed"}
 
     def open_debate(self, legislation_id: str) -> dict[str, Any]:
-        """فتح المناقشة."""
-        self._update_status(legislation_id, "debate")
+        """فتح المناقشة — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
+        self._require_legislation(legislation_id)
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(LegislationModel).where(LegislationModel.id == legislation_id)
+                ).scalar_one()
+                undo.prior(record, "status")
+                record.status = "debate"
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "LegislativeBranch.open_debate"
+        target, crossing = _crossing(
+            operation,
+            "WRITE",
+            f"legislations/{legislation_id}/debate/{_nonce()}",
+            "فتحُ المناقشةِ",
+            undo,
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
         return {"legislation_id": legislation_id, "status": "debate"}
 
     def vote(self, legislation_id: str, agent_id: str, vote: str) -> dict[str, Any]:
-        """التصويت على قانون."""
+        """التصويت على قانون — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
         if vote not in ["for", "against", "abstain"]:
             raise ValueError("التصويت يجب أن يكون for/against/abstain")
 
+        # D5: التحقُّقُ قبلَ العبورِ — الرسائلُ والأنواعُ كما كانت
         session = get_session_factory()()
         try:
-            record = session.execute(
+            existing = session.execute(
                 select(LegislationModel).where(LegislationModel.id == legislation_id)
             ).scalar_one_or_none()
-            if not record:
+            if not existing:
                 raise ValueError("القانون غير موجود")
-            if record.status != "voting":
-                raise ValueError(f"القانون ليس في مرحلة التصويت (الحالة: {record.status})")
-
-            voters = record.voters or []
-            if agent_id in voters:
+            if existing.status != "voting":
+                raise ValueError(f"القانون ليس في مرحلة التصويت (الحالة: {existing.status})")
+            if agent_id in (existing.voters or []):
                 raise ValueError("الوكيل صوّت بالفعل")
-            voters.append(agent_id)
-            record.voters = voters
-
-            if vote == "for":
-                record.votes_for += 1
-            elif vote == "against":
-                record.votes_against += 1
-            else:
-                record.votes_abstain += 1
-            session.commit()
         finally:
             session.close()
 
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(LegislationModel).where(LegislationModel.id == legislation_id)
+                ).scalar_one()
+                undo.prior(record, "voters", "votes_for", "votes_against", "votes_abstain")
+                record.voters = [*(record.voters or []), agent_id]
+                if vote == "for":
+                    record.votes_for += 1
+                elif vote == "against":
+                    record.votes_against += 1
+                else:
+                    record.votes_abstain += 1
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "LegislativeBranch.vote"
+        target, crossing = _crossing(
+            operation,
+            "WRITE",
+            f"legislations/{legislation_id}/votes/{agent_id}",
+            "صوتُ وكيلٍ على قانونٍ",
+            undo,
+        )
+        guarded = _federation_authorizer().guard_declared(
+            FEDERATION_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, operation, target)
+
         return {"legislation_id": legislation_id, "agent_id": agent_id, "vote": vote}
 
     def open_voting(self, legislation_id: str) -> dict[str, Any]:
-        """فتح التصويت."""
-        self._update_status(legislation_id, "voting")
+        """فتح التصويت — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
+        self._require_legislation(legislation_id)
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(LegislationModel).where(LegislationModel.id == legislation_id)
+                ).scalar_one()
+                undo.prior(record, "status")
+                record.status = "voting"
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "LegislativeBranch.open_voting"
+        target, crossing = _crossing(
+            operation,
+            "WRITE",
+            f"legislations/{legislation_id}/voting/{_nonce()}",
+            "فتحُ التصويتِ",
+            undo,
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
         return {"legislation_id": legislation_id, "status": "voting"}
 
     def enact(self, legislation_id: str) -> dict[str, Any]:
-        """إقرار قانون — يُضاف لـ Policy Engine فعليًا."""
+        """إقرار قانون — يُضاف لـ Policy Engine فعليًا · يعبرُ الحدَّ بالفعلِ `coordinate` (F1).
+
+        تغييرُ سلوكٍ مُعلَنٌ (D6): الإقرارُ الثاني لقانونٍ واحدٍ يُرفَعُ `FederationReplayError`
+        بدلَ إعادةِ الإقرارِ صامتًا.
+        """
         session = get_session_factory()()
         try:
-            record = session.execute(
+            existing = session.execute(
                 select(LegislationModel).where(LegislationModel.id == legislation_id)
             ).scalar_one_or_none()
-            if not record:
+            if not existing:
                 raise ValueError("القانون غير موجود")
-            if record.votes_for <= record.votes_against:
-                record.status = "rejected"
-                session.commit()
-                return {"legislation_id": legislation_id, "status": "rejected"}
-
-            # إضافة القانون لـ Policy Engine
-            from amos_federation.services.governance.policy_engine import PolicyEngine, RegoRule
-
-            pe = PolicyEngine()
-            rule_name = f"legislated_{record.title[:30]}".replace(" ", "_")
-            pe.add_rule(
-                RegoRule(
-                    name=rule_name,
-                    description=record.body,
-                    conditions=[{"field": "legislation.enacted", "op": "eq", "value": True}],
-                    decision="allow",
-                )
-            )
-            record.status = "enacted"
-            record.enacted_rule_name = rule_name
-            session.commit()
         finally:
             session.close()
 
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(LegislationModel).where(LegislationModel.id == legislation_id)
+                ).scalar_one()
+                undo.prior(record, "status", "enacted_rule_name")
+                if record.votes_for <= record.votes_against:
+                    record.status = "rejected"
+                    session.commit()
+                    return {"legislation_id": legislation_id, "status": "rejected"}
+
+                # إضافة القانون لـ Policy Engine (ذاكرةُ نسخةٍ لا تخزين — D8-ج)
+                from amos_federation.services.governance.policy_engine import (
+                    PolicyEngine,
+                    RegoRule,
+                )
+
+                pe = PolicyEngine()
+                rule_name = f"legislated_{record.title[:30]}".replace(" ", "_")
+                pe.add_rule(
+                    RegoRule(
+                        name=rule_name,
+                        description=record.body,
+                        conditions=[{"field": "legislation.enacted", "op": "eq", "value": True}],
+                        decision="allow",
+                    )
+                )
+                record.status = "enacted"
+                record.enacted_rule_name = rule_name
+                session.commit()
+                return {
+                    "legislation_id": legislation_id,
+                    "status": "enacted",
+                    "rule_name": rule_name,
+                }
+            finally:
+                session.close()
+
+        operation = "LegislativeBranch.enact"
+        target, crossing = _crossing(
+            operation, "WRITE", f"legislations/{legislation_id}/enact", "إقرارُ قانونٍ أو رفضُه", undo
+        )
+        guarded = _federation_authorizer().guard_declared(
+            FEDERATION_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, operation, target)
+        outcome: dict[str, Any] = guarded.value
+        if outcome["status"] == "rejected":
+            return outcome
+
         from amos_federation.common.event_bus import get_event_bus
 
         get_event_bus().publish(
             "amos_federation.legislative.enacted",
             {
                 "legislation_id": legislation_id,
-                "rule_name": rule_name,
+                "rule_name": outcome["rule_name"],
             },
         )
 
-        return {"legislation_id": legislation_id, "status": "enacted", "rule_name": rule_name}
+        return outcome
 
     def run_full_legislative_cycle(
         self, title: str, body: str, proposer: str, voters: list[tuple[str, str]]
@@ -964,14 +1307,13 @@ class LegislativeBranch:
         finally:
             session.close()
 
-    def _update_status(self, legislation_id: str, status: str) -> None:
+    def _require_legislation(self, legislation_id: str) -> None:
+        """D5: وجودُ القانونِ قبلَ العبورِ — النوعُ كما كانَ (`NoResultFound`) · قراءةٌ لا كتابة."""
         session = get_session_factory()()
         try:
-            record = session.execute(
+            session.execute(
                 select(LegislationModel).where(LegislationModel.id == legislation_id)
             ).scalar_one()
-            record.status = status
-            session.commit()
         finally:
             session.close()
 
@@ -994,22 +1336,32 @@ class JudicialBranch:
     def file_case(
         self, plaintiff: str, defendant: str, subject: str, evidence: list | None = None
     ) -> dict[str, Any]:
-        """رفع دعوى."""
+        """رفع دعوى — سجلُّ تنسيقٍ لا قضاءٌ (Q-24) · يعبرُ بالفعلِ `coordinate` (F1)."""
         case_id = str(uuid.uuid4())
-        session = get_session_factory()()
-        try:
-            record = CourtCaseModel(
-                id=case_id,
-                plaintiff=plaintiff,
-                defendant=defendant,
-                subject=subject,
-                evidence=evidence or [],
-                status="open",
-            )
-            session.add(record)
-            session.commit()
-        finally:
-            session.close()
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = CourtCaseModel(
+                    id=case_id,
+                    plaintiff=plaintiff,
+                    defendant=defendant,
+                    subject=subject,
+                    evidence=evidence or [],
+                    status="open",
+                )
+                undo.created(record)
+                session.add(record)
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "JudicialBranch.file_case"
+        target, crossing = _crossing(
+            operation, "CREATE", f"court_cases/{case_id}/file", "رفعُ دعوى في سجلِّ التنسيقِ", undo
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
 
         from amos_federation.common.event_bus import get_event_bus
 
@@ -1025,38 +1377,86 @@ class JudicialBranch:
         return {"case_id": case_id, "status": "open"}
 
     def add_argument(self, case_id: str, arg_text: str, by: str) -> dict[str, Any]:
-        """إضافة مرافعة."""
+        """إضافة مرافعة — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
+        # D5: وجودُ القضيّةِ قبلَ العبورِ — النوعُ كما كانَ (`NoResultFound`)
         session = get_session_factory()()
         try:
-            record = session.execute(
-                select(CourtCaseModel).where(CourtCaseModel.id == case_id)
-            ).scalar_one()
-            args = record.arguments or []
-            args.append({"text": arg_text, "by": by, "timestamp": datetime.now(UTC).isoformat()})
-            record.arguments = args
-            record.status = "hearing"
-            session.commit()
+            session.execute(select(CourtCaseModel).where(CourtCaseModel.id == case_id)).scalar_one()
         finally:
             session.close()
+
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(CourtCaseModel).where(CourtCaseModel.id == case_id)
+                ).scalar_one()
+                undo.prior(record, "arguments", "status")
+                record.arguments = [
+                    *(record.arguments or []),
+                    {"text": arg_text, "by": by, "timestamp": datetime.now(UTC).isoformat()},
+                ]
+                record.status = "hearing"
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "JudicialBranch.add_argument"
+        target, crossing = _crossing(
+            operation,
+            "WRITE",
+            f"court_cases/{case_id}/arguments/{_nonce()}",
+            "إضافةُ مرافعةٍ",
+            undo,
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
         return {"case_id": case_id, "argument_added": True}
 
     def rule(self, case_id: str, ruling: str, judge: str) -> dict[str, Any]:
-        """إصدار حكم."""
+        """إصدار حكم في سجلِّ التنسيقِ (Q-24) — يعبرُ الحدَّ بالفعلِ `coordinate` (F1).
+
+        القضاءُ الحقيقيُّ هو `federal_judiciary.rulings.issue_ruling` بفاعلِه القضائيِّ (J1)؛
+        هذا السجلُّ لا يمنحُه العبورُ سلطةً.
+        """
         session = get_session_factory()()
         try:
-            record = session.execute(
+            existing = session.execute(
                 select(CourtCaseModel).where(CourtCaseModel.id == case_id)
             ).scalar_one_or_none()
-            if not record:
+            if not existing:
                 raise ValueError("القضية غير موجودة")
-            record.ruling = ruling
-            record.ruling_judge = judge
-            record.status = "ruled"
-            record.resolved_at = datetime.now(UTC)
-            session.commit()
         finally:
             session.close()
 
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = session.execute(
+                    select(CourtCaseModel).where(CourtCaseModel.id == case_id)
+                ).scalar_one()
+                undo.prior(record, "ruling", "ruling_judge", "status", "resolved_at")
+                record.ruling = ruling
+                record.ruling_judge = judge
+                record.status = "ruled"
+                record.resolved_at = datetime.now(UTC)
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "JudicialBranch.rule"
+        target, crossing = _crossing(
+            operation,
+            "WRITE",
+            f"court_cases/{case_id}/ruling/{_nonce()}",
+            "تسجيلُ حكمٍ في سجلِّ التنسيقِ",
+            undo,
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
+
         from amos_federation.common.event_bus import get_event_bus
 
         get_event_bus().publish(
@@ -1113,7 +1513,7 @@ class SupremeOversight:
         _GovBase.metadata.create_all(engine)
 
     def generate_compliance_report(self, period: str | None = None) -> dict[str, Any]:
-        """تقرير امتثال شهري حقيقي."""
+        """تقرير امتثال شهري حقيقي — يعبرُ الحدَّ بالفعلِ `coordinate` (F1)."""
         if not period:
             period = datetime.now(UTC).strftime("%Y-%m")
 
@@ -1144,22 +1544,36 @@ class SupremeOversight:
             recommendations.append("مراجعة السياسات المُنتَهَكة")
 
         report_id = str(uuid.uuid4())
-        session = get_session_factory()()
-        try:
-            record = ComplianceReportModel(
-                id=report_id,
-                period=period,
-                total_audits=total,
-                violations=violations,
-                compliance_rate=compliance_rate,
-                findings=findings,
-                recommendations=recommendations,
-                chain_verified=chain_verify.get("valid", False),
-            )
-            session.add(record)
-            session.commit()
-        finally:
-            session.close()
+        undo = _FederationUndo()
+
+        def _apply(_effect: Any) -> None:
+            session = get_session_factory()()
+            try:
+                record = ComplianceReportModel(
+                    id=report_id,
+                    period=period,
+                    total_audits=total,
+                    violations=violations,
+                    compliance_rate=compliance_rate,
+                    findings=findings,
+                    recommendations=recommendations,
+                    chain_verified=chain_verify.get("valid", False),
+                )
+                undo.created(record)
+                session.add(record)
+                session.commit()
+            finally:
+                session.close()
+
+        operation = "SupremeOversight.generate_compliance_report"
+        target, crossing = _crossing(
+            operation,
+            "CREATE",
+            f"compliance_reports/{report_id}/generate",
+            "تقريرُ امتثالٍ",
+            undo,
+        )
+        _federation_authorizer().guard_declared(FEDERATION_VERB, target, applier=_apply, **crossing)
 
         from amos_federation.common.event_bus import get_event_bus
 
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && cat federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py
EXIT: 0
BYTES: 18507
SHA256: 07aeff6e6c8b67cdc2a2b3cdca66c6dc6f665f9c6fdf0e7fd6fb559ca68e8552
NO_EOL: 0
--- OUTPUT ---
"""
WI-106 · F1 — أسطحُ `governance/federation.py` الخمسةَ عشرَ تعبرُ الحدَّ السياديَّ بفاعلٍ
تنفيذيٍّ مُعلَنٍ بالفعلِ `coordinate` (قرارُ المالكِ D17-1 · نصُّ Q-24: «تنسيق لا سلطة»).

الهدف: إثباتُ أنَّ كلَّ سطحٍ عامٍّ مُغيِّرٍ في الوحدةِ يعبرُ الحدَّ بالفعلِ نفسِه وبالفاعلِ
       الثابتِ في الوحدةِ، وأنَّ الكتابةَ كلَّها خلفَ الحدِّ (لا صفَّ يُكتَبُ إن رُفِضَ)،
       وأنَّ المُعوِّضَ يستعيدُ الحالةَ كما كانت، وأنَّ الإعادةَ على مفتاحٍ طبيعيٍّ تُرفَعُ صريحةً.
النطاق: قياسُ سلوكِ الوحدةِ عبرَ الحدِّ وحدَه — لا تعديلَ للبوابةِ ولا للقواعدِ ولا لـ
        `test_federation.py` (بلا تعديلٍ).
المالك: federal/executive/services — WI-106 (تصميمُ docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md
        المُلتزَمُ قبلَ الشِّفرةِ في W-615).
تاريخ الإنشاء: 2026-10-22 (WI-106 · الدفعةُ F1)

الفحوصُ كما وردتْ في التصميمِ (§ 4) — T1–T8:
- T1 · العبورُ: الأسطحُ الخمسةَ عشرَ كلُّها ⇒ 15 عمليّةً متمايزةً بالفعلِ `coordinate` وALLOW.
- T2 · الفاعلُ مُعلَنٌ لا مُثبَّتٌ: `FEDERATION_ACTOR="JUDICIAL"` ⇒ رفضٌ ولا صفَّ.
- T3 · لا كتابةَ خارجَ المُطبِّقِ: الرفضُ لكلِّ سطحٍ ⇒ الصفوفُ والأعمدةُ كما كانت.
- T4 · المُعوِّضُ على الإنشاءِ (`propose`) · T5 · على التحديثِ (`vote`).
- T6 · الإعادةُ الطبيعيّةُ (`enact` الثاني) ⇒ `FederationReplayError` بلا كتابةٍ ثانيةٍ.
- T7 · الجردُ: 15 عامًّا في الوحدةِ كلُّها عابرةٌ · T8 · الثابتانِ.

الحدُّ المُعلَنُ: لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذِ (§ 4.3) — ملفُّ قياسٍ لا حُكمِ مراجعةٍ.

الدليلُ المُعادُ تشغيلُه (من federal/executive/services):
    ../../../.venv/bin/python -m pytest tests/test_wi106_federation_coordinate_sovereign.py -q
"""

from __future__ import annotations

import importlib.util
import math
import sys
import time
from pathlib import Path
from typing import Any

import pytest
from sqlalchemy import create_engine, delete, select

from amos_federation.common.database import get_database_url, get_session_factory
from amos_federation.services.agent_runtime.population import get_population_registry
from amos_federation.services.governance import federation as federation_module
from amos_federation.services.governance.federation import (
    ApprovalModel,
    ApprovalSystem,
    ComplianceReportModel,
    CourtCaseModel,
    ExecutiveBranch,
    ExecutiveRoleModel,
    FederationReplayError,
    JudicialBranch,
    LegislationModel,
    LegislativeBranch,
    PromotionGateModel,
    PromotionSystem,
    SupremeOversight,
    _GovBase,
)

#: الأسطحُ الخمسةَ عشرَ المقيسةُ قبلَ الشِّفرةِ (evidence/W-615/federation_sites_before.txt).
EXPECTED_OPERATIONS = frozenset(
    {
        "ApprovalSystem.request_approval",
        "ApprovalSystem.decide_approval",
        "PromotionSystem.start_promotion",
        "PromotionSystem.pass_gate",
        "PromotionSystem.fail_gate",
        "ExecutiveBranch.appoint",
        "LegislativeBranch.propose",
        "LegislativeBranch.open_debate",
        "LegislativeBranch.open_voting",
        "LegislativeBranch.vote",
        "LegislativeBranch.enact",
        "JudicialBranch.file_case",
        "JudicialBranch.add_argument",
        "JudicialBranch.rule",
        "SupremeOversight.generate_compliance_report",
    }
)

_MODELS = (
    ApprovalModel,
    PromotionGateModel,
    LegislationModel,
    CourtCaseModel,
    ComplianceReportModel,
)


@pytest.fixture(autouse=True)
def clean_federation() -> Any:
    """جداولُ الوحدةِ نظيفةٌ قبلَ كلِّ فحصٍ وبعدَه · والمُفوِّضُ المحفوظُ مُفرَغٌ (D1)."""
    url = get_database_url()
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    _GovBase.metadata.create_all(create_engine(url, connect_args=connect_args))
    get_population_registry().seed_initial_population()
    federation_module.reset_federation_authorizer()
    yield
    session = get_session_factory()()
    try:
        for model in _MODELS:
            session.execute(delete(model))
        for role in session.execute(select(ExecutiveRoleModel)).scalars().all():
            role.agent_id = None
            role.status = "vacant"
            role.appointed_at = None
        session.commit()
    finally:
        session.close()
    federation_module.reset_federation_authorizer()


class RecordingFederationAuthorizer(federation_module.ConstitutionalAuthorizer):
    """يسجّلُ كلَّ عبورٍ (اسمَ العمليّةِ والدليلَ) — لقياسِ العبورِ لا لاتخاذِ قرارٍ."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.crossings: list[tuple[str, Any]] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.crossings.append(((kwargs.get("metadata") or {}).get("operation", ""), guarded))
        return guarded


def _install_recording_authorizer() -> RecordingFederationAuthorizer:
    """مُصرِّحٌ مسجِّلٌ بثابتِ الوحدةِ نفسِه — المسارُ الإنتاجيُّ كما هو (D1)."""
    authorizer = RecordingFederationAuthorizer(actor=federation_module.FEDERATION_ACTOR)
    federation_module._DEFAULT_FEDERATION_AUTHORIZER = authorizer
    return authorizer


def _agent_id(index: int = 0) -> str:
    return get_population_registry().list_agents()[index]["agent_id"]


def _keys() -> tuple[str, str]:
    return ApprovalSystem().signer.generate_keypair()


def _legislation(leg_id: str) -> LegislationModel:
    session = get_session_factory()()
    try:
        row = session.get(LegislationModel, leg_id)
        assert row is not None
        session.expunge(row)
        return row
    finally:
        session.close()


def _count(model: type) -> int:
    session = get_session_factory()()
    try:
        return len(session.execute(select(model)).scalars().all())
    finally:
        session.close()


def _snapshot() -> dict[str, list[tuple[Any, ...]]]:
    """لقطةُ كلِّ صفوفِ الوحدةِ بأعمدتِها — للمقارنةِ قبلَ الرفضِ وبعدَه (T3)."""
    session = get_session_factory()()
    try:
        out: dict[str, list[tuple[Any, ...]]] = {}
        for model in (*_MODELS, ExecutiveRoleModel):
            columns = [c.key for c in model.__table__.columns]
            rows = session.execute(select(model)).scalars().all()
            out[model.__name__] = sorted(
                (tuple(repr(getattr(r, c)) for c in columns) for r in rows), key=repr
            )
        return out
    finally:
        session.close()


def _drop_settle(monkeypatch: pytest.MonkeyPatch, ledger: Any, label: str) -> Any:
    """إسقاطُ تثبيتِ النجاحِ بعدَ التزامِ المُطبِّقِ — يُرجِعُ الأصلَ لرفعِ الإسقاط."""
    original = type(ledger).mark_succeeded

    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError(f"تثبيتُ النجاحِ مُسقَطٌ — {label}")

    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)
    return original


def _next_second() -> None:
    """معرِّفُ الإذنِ `EP-<العقد>-<الثانية>` (سابقةُ W-603): الإعادةُ تعبرُ إلى الثانيةِ التاليةِ."""
    now = time.time()
    time.sleep(math.ceil(now) - now + 0.05)


def _voting_legislation(title: str) -> str:
    branch = LegislativeBranch()
    leg_id = branch.propose(title, "نصُّ الفحصِ", "tester")["legislation_id"]
    branch.open_debate(leg_id)
    branch.open_voting(leg_id)
    return leg_id


def _exercise_all_surfaces() -> None:
    """استدعاءُ الأسطحِ الخمسةَ عشرَ كلِّها مرّةً على الأقلِّ — بالواجهةِ العامّةِ كما هي."""
    priv, pub = _keys()
    approvals = ApprovalSystem()
    approval = approvals.request_approval("policy_change", "t1", "tester", priv, pub)
    approvals.decide_approval(approval["approval_id"], "approve", priv, pub)

    promotions = PromotionSystem()
    promotions.start_promotion("model", "t1-model", "tester")
    promotions.pass_gate("model", "t1-model", "evaluation", {"score": 0.9})
    promotions.fail_gate("model", "t1-model", "shadow", "فحصٌ")

    ExecutiveBranch().appoint("coordinator", _agent_id())

    legislative = LegislativeBranch()
    leg_id = _voting_legislation("قانونُ T1")
    legislative.vote(leg_id, _agent_id(0), "for")
    legislative.enact(leg_id)

    judicial = JudicialBranch()
    case_id = judicial.file_case("a", "b", "موضوعُ الفحصِ")["case_id"]
    judicial.add_argument(case_id, "حجّةٌ", "a")
    judicial.rule(case_id, "حكمُ تنسيقٍ", "judge")

    SupremeOversight().generate_compliance_report("2026-10")


# ── T1 · العبورُ: خمسَ عشرةَ عمليّةً بالفعلِ coordinate ─────────────────────────


def test_wi106_t1_every_surface_crosses_as_coordinate() -> None:
    authorizer = _install_recording_authorizer()
    _exercise_all_surfaces()

    operations = {name for name, _ in authorizer.crossings}
    assert operations == EXPECTED_OPERATIONS
    for name, guarded in authorizer.crossings:
        evidence = guarded.evidence.as_dict()
        assert evidence["action"] == "coordinate", name
        assert evidence["decision"] == "ALLOW", name
        assert evidence["target"].startswith("federation/"), name
    record = authorizer.gateway.records[-1]
    assert record.action == "coordinate"
    assert record.actor == "executive"


# ── T2 · الفاعلُ ثابتُ الوحدةِ — تبديلُه يُسقِطُ العبورَ ───────────────────────


def test_wi106_t2_judicial_actor_is_denied_and_nothing_is_written(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation  # يُتاحُ أوّلًا (الجسرُ)

    monkeypatch.setattr(federation_module, "FEDERATION_ACTOR", "JUDICIAL")
    federation_module.reset_federation_authorizer()
    priv, pub = _keys()

    with pytest.raises(SovereigntyViolation):
        LegislativeBranch().propose("مرفوضٌ", "نصٌّ", "tester")
    with pytest.raises(SovereigntyViolation):
        ApprovalSystem().request_approval("policy_change", "t2", "tester", priv, pub)

    assert _count(LegislationModel) == 0
    assert _count(ApprovalModel) == 0


# ── T3 · لا كتابةَ خارجَ المُطبِّقِ — لكلِّ سطحٍ ───────────────────────────────


def test_wi106_t3_denied_crossing_leaves_every_surface_untouched(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    # التحضيرُ بالفاعلِ الصحيحِ: كيانٌ قائمٌ لكلِّ سطحِ تحديثٍ
    priv, pub = _keys()
    approval_id = ApprovalSystem().request_approval("policy_change", "t3", "tester", priv, pub)[
        "approval_id"
    ]
    PromotionSystem().start_promotion("model", "t3-model", "tester")
    leg_debate = LegislativeBranch().propose("قانونُ T3", "نصٌّ", "tester")["legislation_id"]
    leg_vote = _voting_legislation("قانونُ T3-ب")
    case_id = JudicialBranch().file_case("a", "b", "موضوعٌ")["case_id"]
    agent = _agent_id()
    before = _snapshot()

    monkeypatch.setattr(federation_module, "FEDERATION_ACTOR", "JUDICIAL")
    federation_module.reset_federation_authorizer()

    calls = [
        lambda: ApprovalSystem().request_approval("policy_change", "x", "tester", priv, pub),
        lambda: ApprovalSystem().decide_approval(approval_id, "approve", priv, pub),
        lambda: PromotionSystem().start_promotion("model", "t3-other", "tester"),
        lambda: PromotionSystem().pass_gate("model", "t3-model", "evaluation", {}),
        lambda: PromotionSystem().fail_gate("model", "t3-model", "evaluation", "x"),
        lambda: ExecutiveBranch().appoint("coordinator", agent),
        lambda: LegislativeBranch().propose("x", "y", "z"),
        lambda: LegislativeBranch().open_debate(leg_debate),
        lambda: LegislativeBranch().open_voting(leg_debate),
        lambda: LegislativeBranch().vote(leg_vote, agent, "for"),
        lambda: LegislativeBranch().enact(leg_vote),
        lambda: JudicialBranch().file_case("p", "d", "s"),
        lambda: JudicialBranch().add_argument(case_id, "x", "p"),
        lambda: JudicialBranch().rule(case_id, "x", "j"),
        lambda: SupremeOversight().generate_compliance_report("2026-10"),
    ]
    assert len(calls) == len(EXPECTED_OPERATIONS)
    for call in calls:
        with pytest.raises(SovereigntyViolation):
            call()

    assert _snapshot() == before


# ── T4 · المُعوِّضُ على الإنشاءِ ─────────────────────────────────────────────


def test_wi106_t4_compensator_removes_created_row(monkeypatch: pytest.MonkeyPatch) -> None:
    from core.sovereignty.compensation import CompensationRequired

    ledger = federation_module._federation_authorizer().boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T4")
    with pytest.raises(CompensationRequired) as caught:
        LegislativeBranch().propose("قانونُ T4", "نصٌّ", "tester")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    assert caught.value.outcome.state_is_clean is True
    assert caught.value.outcome.requires_human is False
    assert _count(LegislationModel) == 0

    LegislativeBranch().propose("قانونُ T4", "نصٌّ", "tester")
    assert _count(LegislationModel) == 1


# ── T5 · المُعوِّضُ على التحديثِ ─────────────────────────────────────────────


def test_wi106_t5_compensator_restores_vote_counters(monkeypatch: pytest.MonkeyPatch) -> None:
    from core.sovereignty.compensation import CompensationRequired
    from core.sovereignty.idempotency import IdempotencyKey, OperationStatus

    leg_id = _voting_legislation("قانونُ T5")
    agent = _agent_id()
    ledger = federation_module._federation_authorizer().boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T5")
    with pytest.raises(CompensationRequired) as caught:
        LegislativeBranch().vote(leg_id, agent, "for")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    assert caught.value.outcome.state_is_clean is True
    row = _legislation(leg_id)
    assert (row.votes_for, row.votes_against, row.votes_abstain) == (0, 0, 0)
    assert list(row.voters or []) == []
    record = ledger.get(
        IdempotencyKey(
            scope="federation.LegislativeBranch.vote",
            value=f"legislations/{leg_id}/votes/{agent}",
        )
    )
    assert record is not None and record.status is OperationStatus.FAILED_RETRYABLE

    _next_second()
    LegislativeBranch().vote(leg_id, agent, "for")
    row = _legislation(leg_id)
    assert row.votes_for == 1
    assert list(row.voters) == [agent]


# ── T6 · الإعادةُ الطبيعيّةُ مرفوعةٌ صريحةً ─────────────────────────────────


def test_wi106_t6_second_enact_is_refused_without_second_write() -> None:
    leg_id = _voting_legislation("قانونُ T6")
    branch = LegislativeBranch()
    branch.vote(leg_id, _agent_id(), "for")
    first = branch.enact(leg_id)
    assert first["status"] == "enacted"
    updated_before = _legislation(leg_id).updated_at

    _next_second()
    with pytest.raises(FederationReplayError):
        branch.enact(leg_id)
    after = _legislation(leg_id)
    assert after.status == "enacted"
    assert after.updated_at == updated_before


# ── T7 · الجردُ: الوحدةُ بلا دَينٍ ────────────────────────────────────────────


def _repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "audit" / "sovereign_write_inventory.py").is_file():
            return parent
    raise AssertionError("جذرُ المستودعِ غيرُ موجود")


def test_wi106_t7_inventory_counts_fifteen_guarded_and_zero_debt() -> None:
    root = _repo_root()
    tool = root / "tools" / "audit" / "sovereign_write_inventory.py"
    spec = importlib.util.spec_from_file_location("_wi106_inventory", tool)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    sites = [s for s in module.collect(root) if s.path.endswith("governance/federation.py")]
    public = [s for s in sites if s.public]
    assert {f"{s.owner}.{s.function}" for s in public} == EXPECTED_OPERATIONS
    assert all(s.guarded for s in public), [s.function for s in public if not s.guarded]


# ── T8 · الثابتانِ (D1 · D2) ──────────────────────────────────────────────────


def test_wi106_t8_actor_and_verb_constants() -> None:
    assert federation_module.FEDERATION_ACTOR == "EXECUTIVE"
    assert federation_module.FEDERATION_VERB == "coordinate"
    assert federation_module._federation_authorizer()._actor == "EXECUTIVE"
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3316
SHA256: 3393bd24de95851af8b06ffd6b61591f640d5ae38565ba8f258edc4c66b45985
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 236
  عمليّاتٌ عامّةٌ مُغيِّرة   : 201
  منها تعبرُ الحدَّ        : 33
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 166
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          171 /  33 /  137
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      17  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
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
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py -q
EXIT: 0
BYTES: 712
SHA256: 0b74bd343b590231064f4be821046b187915168af97f2381d62f52f61a266cca
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w620/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 8 items

federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py . [ 12%]
.......                                                                  [100%]

============================== 8 passed in 6.68s ===============================
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_federation.py -q
EXIT: 0
BYTES: 1692
SHA256: 228757ccb4708a5afdc77ddbfd47a6d5de5e84e7a10342e545f8611370e5f0ab
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w620/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 43 items

federal/executive/services/tests/test_federation.py .................... [ 46%]
.......................                                                  [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w620/kimi_k3/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 43 passed, 1 warning in 9.65s =========================
Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317, retrying in 0.88s. Error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && .venv/bin/python -m pytest tests/sovereignty -q
EXIT: 0
BYTES: 991
SHA256: bd4074a6c178a1e0d16f16abcda745c809ad10a784995a46ce21e006ea4130fd
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
818 passed, 1 skipped in 4.61s
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
EXIT: 0
BYTES: 13490
SHA256: 7f5cb007a3f5eab980d73f3243d5c4ff8b98a02ec726d857f922040bc764a9c1
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w620/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1546 items

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
federal/executive/services/tests/test_config.py ...                      [ 13%]
federal/executive/services/tests/test_control_console.py ............... [ 14%]
..........                                                               [ 15%]
federal/executive/services/tests/test_critic.py ...........              [ 16%]
federal/executive/services/tests/test_durable_bus_branches.py .......... [ 16%]
.                                                                        [ 17%]
federal/executive/services/tests/test_e2e.py ...                         [ 17%]
federal/executive/services/tests/test_edge_branches.py .........         [ 17%]
federal/executive/services/tests/test_event_bus.py ..............        [ 18%]
federal/executive/services/tests/test_event_schemas.py .....             [ 19%]
federal/executive/services/tests/test_executive_core.py ................ [ 20%]
..............                                                           [ 20%]
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
federal/executive/services/tests/test_model_gateway.py ....              [ 37%]
federal/executive/services/tests/test_model_layer.py ..............      [ 38%]
federal/executive/services/tests/test_models.py ...                      [ 38%]
federal/executive/services/tests/test_orchestrator.py .......            [ 39%]
federal/executive/services/tests/test_p13_factories_sovereign.py ....... [ 39%]
...............                                                          [ 40%]
federal/executive/services/tests/test_persistence.py ........            [ 41%]
federal/executive/services/tests/test_phase12_states.py ................ [ 42%]
.                                                                        [ 42%]
federal/executive/services/tests/test_phase13_factories.py ............. [ 43%]
                                                                         [ 43%]
federal/executive/services/tests/test_phase14_15_learning.py ........... [ 43%]
...                                                                      [ 44%]
federal/executive/services/tests/test_phase16_security.py .............. [ 45%]
..                                                                       [ 45%]
federal/executive/services/tests/test_phase17_system_life.py ........... [ 45%]
.                                                                        [ 45%]
federal/executive/services/tests/test_phase1_postgres.py ssssssss        [ 46%]
federal/executive/services/tests/test_phase1_postgres_events.py ssssssss [ 47%]
sssssssss                                                                [ 47%]
federal/executive/services/tests/test_phase2_events.py ................. [ 48%]
..........                                                               [ 49%]
federal/executive/services/tests/test_phase3_governance.py ............. [ 50%]
...........                                                              [ 50%]
federal/executive/services/tests/test_phase4_tools.py .................. [ 52%]
                                                                         [ 52%]
federal/executive/services/tests/test_phase5_models.py ...........       [ 52%]
federal/executive/services/tests/test_phase6_population.py ............. [ 53%]
..                                                                       [ 53%]
federal/executive/services/tests/test_phase7_health.py .........         [ 54%]
federal/executive/services/tests/test_population.py ..................   [ 55%]
federal/executive/services/tests/test_q19_money_delegation.py .......... [ 56%]
..................                                                       [ 57%]
federal/executive/services/tests/test_q20_money_representation.py ...... [ 57%]
.ss..................                                                    [ 59%]
federal/executive/services/tests/test_q31_money_engine_wiring.py ....... [ 59%]
.....                                                                    [ 59%]
federal/executive/services/tests/test_q32_money_enforcement_surface.py . [ 59%]
..............                                                           [ 60%]
federal/executive/services/tests/test_r1_canonical_execution_path.py ... [ 60%]
..............                                                           [ 61%]
federal/executive/services/tests/test_r2_task_execution_integration.py . [ 61%]
........................                                                 [ 63%]
federal/executive/services/tests/test_r3_agent_runtime_integration.py .. [ 63%]
...........                                                              [ 64%]
federal/executive/services/tests/test_r4_agent_identity_and_population.py . [ 64%]
...............                                                          [ 65%]
federal/executive/services/tests/test_r5_multi_provider_sandbox.py ..... [ 65%]
..............                                                           [ 66%]
federal/executive/services/tests/test_r6_1_authorization_closure.py .... [ 66%]
..............                                                           [ 67%]
federal/executive/services/tests/test_r6_identity_authorization_root.py . [ 67%]
................                                                         [ 68%]
federal/executive/services/tests/test_r7_government_services.py ........ [ 69%]
........................                                                 [ 70%]
federal/executive/services/tests/test_r7_state_registry.py ............. [ 71%]
.............                                                            [ 72%]
federal/executive/services/tests/test_r7b_state_treasury.py ............ [ 73%]
........................                                                 [ 74%]
federal/executive/services/tests/test_r7c_national_registry.py ......... [ 75%]
..........................                                               [ 77%]
federal/executive/services/tests/test_r7d_federal_judiciary.py ......... [ 77%]
..................                                                       [ 78%]
federal/executive/services/tests/test_r8_federal_state_integration.py .. [ 79%]
...............................                                          [ 81%]
federal/executive/services/tests/test_r9_national_economic_state.py .... [ 81%]
.........................................                                [ 84%]
federal/executive/services/tests/test_real_tools.py .................... [ 85%]
                                                                         [ 85%]
federal/executive/services/tests/test_shadow.py ..........               [ 85%]
federal/executive/services/tests/test_step19_durable_governance_state.py . [ 86%]
.......                                                                  [ 86%]
federal/executive/services/tests/test_step7_gate_denial.py .....         [ 86%]
federal/executive/services/tests/test_tool_registry.py .......           [ 87%]
federal/executive/services/tests/test_training.py ...............        [ 88%]
federal/executive/services/tests/test_treasury.py ...................... [ 89%]
..........                                                               [ 90%]
federal/executive/services/tests/test_w032_registry_ownership.py ....... [ 90%]
......                                                                   [ 91%]
federal/executive/services/tests/test_w033_cost_record_durability.py ... [ 91%]
......                                                                   [ 91%]
federal/executive/services/tests/test_w036_cost_precision.py ........... [ 92%]
                                                                         [ 92%]
federal/executive/services/tests/test_w166_postgres_driver_declared.py . [ 92%]
...............                                                          [ 93%]
federal/executive/services/tests/test_w190_durable_model_registry.py ..  [ 93%]
federal/executive/services/tests/test_w308_test_ledger_is_per_session.py . [ 93%]
..                                                                       [ 93%]
federal/executive/services/tests/test_wi062_migrations_cover_orm_tables.py . [ 93%]
.s                                                                       [ 93%]
federal/executive/services/tests/test_wi063_tenant_isolation_http.py ..s [ 94%]
s..ss.s..ss.s.s.s..s.s.                                                  [ 95%]
federal/executive/services/tests/test_wi064_migrations_follow_orm.py .s  [ 95%]
federal/executive/services/tests/test_wi065_orm_declares_jsonb_timestamptz.py . [ 95%]
.s                                                                       [ 95%]
federal/executive/services/tests/test_wi066_convert_create_all_databases.py . [ 96%]
sssss                                                                    [ 96%]
federal/executive/services/tests/test_wi066_pg_session_isolation.py .ss  [ 96%]
federal/executive/services/tests/test_wi067_legal_search_isolated.py ... [ 96%]
....................                                                     [ 98%]
federal/executive/services/tests/test_wi076_pg_backup_restore.py ssss    [ 98%]
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 98%]
.......                                                                  [ 98%]
federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py .. [ 98%]
........                                                                 [ 99%]
federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py . [ 99%]
.......                                                                  [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w620/kimi_k3/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========== 1493 passed, 53 skipped, 1 warning in 367.65s (0:06:07) ============
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && cat docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md
EXIT: 0
BYTES: 12812
SHA256: d50d6afa3f0ce289aa1c50f93c0450feb471a4fa46c6f4398666c9a862df6a4d
NO_EOL: 0
--- OUTPUT ---
# ملحقُ تصميمِ الدفعةِ F1 — أسطحُ `governance/federation.py` تعبرُ الحدَّ بفاعلٍ تنفيذيٍّ مُعلَنٍ بالفعلِ `coordinate`

## التعريف
ملحقُ تصميمٍ قصيرٌ للدفعةِ **F1** (بندُ `WI-106`) يُودَعُ **في التزامٍ مستقلٍّ يسبقُ أيَّ شِفرةٍ** (قرارُ المالكِ Q-61 للبنودِ القادمةِ · توجيهُ المستشارِ 19 § 2). يحدِّدُ نقاطَ التصميمِ D1–D8 والأرقامَ المتوقَّعةَ قبلَ الكتابةِ والفحوصَ والطفراتِ، على نمطِ J1 ([`J1_ISSUE_RULING_DESIGN.md`](J1_ISSUE_RULING_DESIGN.md)).

## النطاق
`federal/executive/services/src/amos_federation/services/governance/federation.py` وحدَه في الإنتاجِ · وملفُّ الفحوصِ `federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py`. لا يمسُّ `core/` ولا الجسرَ ولا `royal/` (K1 لا يُمَسُّ).

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — بندُ `WI-106`.

## تاريخ الإنشاء
2026-10-22

## تاريخ آخر تعديل
2026-10-22

---

## 0. السندُ (لا اختراعَ)

- **D17-1** (نصُّ المالكِ · السجلُّ السياديُّ): «خيار (1): فاعل تنفيذي معلن للوحدة بالفعل coordinate (نص Q-24 نفسه) → يفتح دفعة F1.»
- **Q-24** (نصُّه): الوحدةُ «تنسيق لا سلطة» — فالفرعُ التشريعيُّ والقضائيُّ في هذه الوحدةِ **سجلّاتُ تنسيقٍ** لا سلطةٌ تشريعيّةٌ ولا قضائيّةٌ حقيقيّةٌ. القضاءُ الحقيقيُّ هو `federal_judiciary` بفاعلِه القضائيِّ (J1). هذا التصميمُ لا يمنحُ `JudicialBranch.rule` ولا `LegislativeBranch.enact` أيَّ سلطةٍ؛ يُخضِعُهما للحدِّ بالفعلِ الذي قرَّرَه المالكُ.
- **قياسُ ما قبلُ** (`evidence/W-615/`): مسبارُ البوابةِ على `coordinate` ⇒ `EXECUTIVE` ALLOW · `LEGISLATIVE`/`JUDICIAL`/`TREASURY` DENY · `AGENT`/`SYSTEM` ALLOW (ثغرةُ Q-68 — خارجَ البندِ).

## 1. الأسطحُ الخمسةَ عشرَ (مقيسةً · `sovereign_write_inventory.py`)

| الصنف | السطح | الأثرُ المُعلَن | الهدفُ (= قيمةُ المفتاحِ) |
|---|---|---|---|
| ApprovalSystem | `request_approval` | CREATE | `federation/approvals/{approval_id}/request` |
| ApprovalSystem | `decide_approval` | UPDATE | `federation/approvals/{approval_id}/decide` |
| PromotionSystem | `start_promotion` | CREATE | `federation/promotions/{promotion_id}/start` |
| PromotionSystem | `pass_gate` | UPDATE | `federation/promotions/{target_type}:{target_id}/{gate}/pass/{nonce}` |
| PromotionSystem | `fail_gate` | UPDATE | `federation/promotions/{target_type}:{target_id}/{gate}/fail/{nonce}` |
| ExecutiveBranch | `appoint` | UPDATE | `federation/executive_roles/{role_name}/appoint/{nonce}` |
| LegislativeBranch | `propose` | CREATE | `federation/legislations/{leg_id}/propose` |
| LegislativeBranch | `open_debate` | UPDATE | `federation/legislations/{id}/debate/{nonce}` |
| LegislativeBranch | `open_voting` | UPDATE | `federation/legislations/{id}/voting/{nonce}` |
| LegislativeBranch | `vote` | UPDATE | `federation/legislations/{id}/votes/{agent_id}` |
| LegislativeBranch | `enact` | UPDATE | `federation/legislations/{id}/enact` |
| JudicialBranch | `file_case` | CREATE | `federation/court_cases/{case_id}/file` |
| JudicialBranch | `add_argument` | UPDATE | `federation/court_cases/{id}/arguments/{nonce}` |
| JudicialBranch | `rule` | UPDATE | `federation/court_cases/{id}/ruling/{nonce}` |
| SupremeOversight | `generate_compliance_report` | CREATE | `federation/compliance_reports/{report_id}/generate` |

## 2. نقاطُ التصميم

**D1 · الفاعلُ:** ثابتُ وحدةٍ `FEDERATION_ACTOR = "EXECUTIVE"` ومُفوِّضٌ كسولٌ واحدٌ للوحدةِ `_federation_authorizer()` (+ `reset_federation_authorizer()` للفحوصِ) — نمطُ `rulings._judiciary_authorizer` نفسُه (D1 في J1). لا معامَلَ `authorizer` في توقيعاتِ الأسطحِ (لا تغييرَ في واجهتِها).

**D2 · الفعلُ:** `FEDERATION_VERB = "coordinate"` للأسطحِ الخمسةَ عشرَ كلِّها (D17-1 حرفيًّا). اسمُ العمليّةِ يُحمَلُ في `metadata["operation"]` (`"<Class>.<method>"`) وفي نطاقِ المفتاحِ — لا يُخترَعُ فعلٌ لكلِّ سطحٍ (ذلك سؤالُ Q-2 المعلَّقُ).

**D3 · الهدفُ والمفتاحُ:** الهدفُ بالجدولِ أعلاه، والمفتاحُ `operation_key("federation.<op>", <لاحقةِ الهدفِ>)` — الهويّةُ نفسُها في الاثنينِ (نمطُ J1 D5/D6). السببُ مقيسٌ في J1: بصمةُ العقدِ تُشتقُّ من (الفاعلِ · الفعلِ · الهدفِ · الآثارِ)، ومعرِّفُ الإذنِ `EP-<العقد>-<الثانية>` يرفضُ عقدًا مكرَّرًا في الثانيةِ نفسِها — فالعمليّاتُ المشروعُ تكرارُها على الكيانِ نفسِه (حجّتانِ في قضيّةٍ · فتحُ مناقشةٍ ثانٍ) تحملُ في هدفِها **مُعرِّفَ استدعاءٍ** (`nonce = uuid4().hex`) وإلّا رُفِضَ الاستدعاءُ الثاني المشروعُ.

**D4 · موضعُ العبورِ:** في **جسدِ كلِّ سطحٍ عامٍّ** (`guard_declared(` نصًّا فيه — قاعدةُ الجردِ)، والكتابةُ كلُّها في **مُطبِّقٍ متداخلٍ خاصٍّ** `_apply` يفتحُ الجلسةَ ويكتبُ ويلتزمُ (نمطُ `agent_identity._apply` في WI-082 و`rulings._apply` في J1). لا كتابةَ خارجَ المُطبِّقِ في أيِّ سطحٍ.

**D5 · التحقُّقُ قبلَ العبورِ:** فحوصُ المُدخَلِ والحالةِ القائمةُ اليومَ (مثلًا «الوكيل صوّت بالفعل» · «الموافقة تم البت فيها» · «بوابة سابقة لم تُجتز») تُنفَّذُ **قبلَ العبورِ** بجلسةِ قراءةٍ ولا تتغيّرُ رسائلُها ولا أنواعُها (`ValueError`) — فلا يتحوّلُ رفضُ مُدخَلٍ إلى `CompensationRequired` ولا يُسجَّلُ في الذرّيّةِ عمليّةً فاشلةً. ويُعيدُ المُطبِّقُ تحميلَ الصفِّ داخلَ معاملتِه.

**D6 · الإعادةُ:** المفتاحُ طبيعيٌّ حيثُ لا يتكرّرُ الفعلُ في المجالِ: الإنشاءُ بمعرِّفٍ جديدٍ · `decide_approval` (يُبَتُّ مرّةً) · `vote` (صوتٌ لكلِّ وكيلٍ) · `enact` (إقرارٌ مرّةً). وحيثُ يُشرَعُ التكرارُ فالمفتاحُ يحملُ مُعرِّفَ الاستدعاءِ (D3) — **فلا يتغيّرُ سلوكُ اليومِ**. وإن عادَ مفتاحٌ طبيعيٌّ ناجحٌ (`is_replay`) رُفِعَ `FederationReplayError` صريحًا بلا كتابةٍ ثانيةٍ (والمقيسُ: `decide_approval`/`vote` يرفضُهما D5 قبلَ ذلك؛ و`enact` الثاني هو الحالةُ الوحيدةُ التي تبلغُ الإعادةَ — **تغييرُ سلوكٍ مُعلَنٌ**: كانَ يُعيدُ الإقرارَ صامتًا).

**D7 · المُعوِّضُ (نمطُ J1 D7-أ):** استعادةٌ تقنيّةٌ دقيقةٌ في جلسةٍ جديدةٍ عبرَ سجلِّ تراجعٍ لكلِّ عبورٍ `_FederationUndo`: المُطبِّقُ يُسجِّلُ قبلَ الكتابةِ (أ) كلَّ صفٍّ أنشأَه (`created(model, pk)`) و(ب) القيمَ السابقةَ لكلِّ عمودٍ يغيّرُه (`prior(row, *columns)` بنسخةٍ عميقةٍ للأعمدةِ JSON). ومُعوِّضُ الأثرِ يحذفُ المُنشَأَ ويُعيدُ السابقَ ويلتزمُ. الحدُّ يُنادي المُعوِّضَ آليًّا عندَ فشلِ تثبيتِ النجاحِ بعدَ الالتزامِ (قرارُ المالكِ Q-70 · W-603) — «الحذفُ شأنٌ تنفيذيٌّ» والمُعوِّضُ ليس أثرًا مُعلَنًا.

**D8 · ما يبقى خارجَ العبورِ (مُعلَنٌ لا مسكوتٌ عنه):** (أ) نشرُ ناقلِ الأحداثِ بعدَ الالتزامِ كما هو اليومَ — أثرٌ للبنيةِ التحتيّةِ، سؤالُ A1 · (ب) `ExecutiveBranch._init_roles` — بذرُ الأدوارِ الشاغرةِ في المُنشئِ، معاونٌ خاصٌّ لا تصلُه عمليّةٌ عامّةٌ، فلا يُحصى دَينًا (قاعدةُ الجردِ) ويبقى كتابةً بلا عبورٍ تُعلَنُ هنا · (ج) `PolicyEngine.add_rule` في `enact` يكتبُ في ذاكرةِ نسخةٍ جديدةٍ لا تخزينَ (مقيسٌ: `self._rules` قاموسٌ) — يبقى داخلَ المُطبِّقِ كما هو · (د) `Ed25519Signer` (Q-37) لا يُمَسُّ.

## 3. الأرقامُ المتوقَّعةُ (مكتوبةٌ قبلَ الشِّفرةِ · بالأداةِ نفسِها)

- **الدَّينُ (D-4):** 181 ← **166** (الخمسةَ عشرَ تعبرُ).
- **السياديُّ:** 18 ← **33**.
- **الأسطحُ:** 220 ← **236** متوقَّعًا — كلُّ مُطبِّقٍ متداخلٍ خاصٍّ يُحصى موضعًا مستقلًّا (سابقةُ DISC-126 في J1/WI-082) فيزيدُ 15، ومُعوِّضُ `_FederationUndo._restore` موضعٌ خاصٌّ واحدٌ. ليست دَينًا (الدَّينُ عامٌّ غيرُ عابرٍ وحدَه). **إن خالفَ المقيسُ هذا الرقمَ أُعلِنَ الفرقُ بسببِه ولا يُعدَّلُ المتوقَّعُ بأثرٍ رجعيٍّ.**
- **بلا نموٍّ في غيرِ الوحدةِ:** دَينُ كلِّ ملفٍّ آخرَ كما هو.

## 4. الفحوصُ (`test_wi106_federation_coordinate_sovereign.py`)

- **T1 · العبورُ:** مُصرِّحٌ مُسجِّلٌ بالثابتِ نفسِه؛ استدعاءُ الأسطحِ الخمسةَ عشرَ كلِّها ⇒ 15 عمليّةً متمايزةً في `metadata["operation"]`، الفعلُ `coordinate` في كلِّها، والقرارُ ALLOW.
- **T2 · الفاعلُ مُعلَنٌ لا مُثبَّتٌ:** تبديلُ `FEDERATION_ACTOR` إلى `JUDICIAL` ⇒ `propose` و`request_approval` يُرفَضانِ في البوابةِ ولا صفَّ يُكتَبُ.
- **T3 · لا كتابةَ خارجَ المُطبِّقِ:** مُصرِّحٌ يرفضُ قبلَ المُطبِّقِ ⇒ لكلِّ سطحٍ: الصفوفُ والأعمدةُ كما كانت.
- **T4 · المُعوِّضُ على الإنشاءِ (`propose`):** إسقاطُ تثبيتِ النجاحِ ⇒ `CompensationRequired` · `state_is_clean` · الصفُّ غائبٌ · الذرّيّةُ `FAILED_RETRYABLE` · والإعادةُ (الثانيةُ التاليةُ) تنجح.
- **T5 · المُعوِّضُ على التحديثِ (`vote`):** الإسقاطُ نفسُه ⇒ العدّادُ والمصوِّتونَ يعودانِ إلى ما قبلُ.
- **T6 · الإعادةُ الطبيعيّةُ (`enact`):** الإقرارُ الثاني ⇒ `FederationReplayError` ولا كتابةَ ثانيةً.
- **T7 · الجردُ:** الأداةُ على الوحدةِ ⇒ 15 عامًّا كلُّها عابرةٌ (0 دَينٌ).
- **T8 · ثوابتُ D1/D2:** الفاعلُ الافتراضيُّ `EXECUTIVE` والفعلُ `coordinate`.
- **بلا تعديلٍ:** `test_federation.py` كاملًا.

## 5. الطفراتُ (كلٌّ يجبُ أن يُسقِطَ فحصَه)

- **M1:** `propose` يُنادي `_apply` مباشرةً بلا عبورٍ ⇒ يسقطُ T1 وT3.
- **M2:** `FEDERATION_ACTOR = "JUDICIAL"` ⇒ يسقطُ T1 وT8.
- **M3:** مُعوِّضُ `_restore` لا يفعلُ شيئًا ⇒ يسقطُ T4 وT5.
- **M4:** حذفُ `undo.prior(...)` من `vote` ⇒ يسقطُ T5.
- **M5:** مفتاحُ `enact` يحملُ مُعرِّفَ استدعاءٍ ⇒ يسقطُ T6.

## 6. ما لا يُنجَزُ في F1 ولماذا

R1 (السجلُّ الوطنيُّ) دفعةٌ تاليةٌ بندًا مستقلًّا (ملفّاتُه منفصلةٌ — ولا يُجمَعُ معَ F1 كي تبقى جولةُ المجلسِ على دفعةٍ واحدةٍ مقروءةٍ). وJ2/J3 بأفعالِ D17-2 المعتمدةِ بعدَها.
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && cat docs/audit/evidence/W-615/federation_sites_before.txt docs/audit/evidence/W-617/federation_sites_after.txt
EXIT: 0
BYTES: 2405
SHA256: 646b9238a442ab1cff00c3b4cbe3e5e00cc1a7e744022597192f16428090aede
NO_EOL: 0
--- OUTPUT ---
{"write_sites_total": 220, "by_area": {"core": {"public": 1, "sovereign": 0, "non_sovereign": 0}, "service_common": {"public": 28, "sovereign": 0, "non_sovereign": 28}, "services": {"public": 171, "sovereign": 18, "non_sovereign": 152}, "tools": {"public": 1, "sovereign": 0, "non_sovereign": 1}}, "p
federation sites 16 public 15 guarded 0
  ApprovalSystem decide_approval public debt
  ApprovalSystem request_approval public debt
  ExecutiveBranch _init_roles private debt
  ExecutiveBranch appoint public debt
  JudicialBranch add_argument public debt
  JudicialBranch file_case public debt
  JudicialBranch rule public debt
  LegislativeBranch enact public debt
  LegislativeBranch open_debate public debt
  LegislativeBranch open_voting public debt
  LegislativeBranch propose public debt
  LegislativeBranch vote public debt
  PromotionSystem fail_gate public debt
  PromotionSystem pass_gate public debt
  PromotionSystem start_promotion public debt
  SupremeOversight generate_compliance_report public debt
federation sites 32 public 15 guarded 15 public_debt 0
  ApprovalSystem _apply private debt
  ApprovalSystem _apply private debt
  ApprovalSystem decide_approval public guarded
  ApprovalSystem request_approval public guarded
  ExecutiveBranch _apply private debt
  ExecutiveBranch _init_roles private debt
  ExecutiveBranch appoint public guarded
  JudicialBranch _apply private debt
  JudicialBranch _apply private debt
  JudicialBranch _apply private debt
  JudicialBranch add_argument public guarded
  JudicialBranch file_case public guarded
  JudicialBranch rule public guarded
  LegislativeBranch _apply private debt
  LegislativeBranch _apply private debt
  LegislativeBranch _apply private debt
  LegislativeBranch _apply private debt
  LegislativeBranch _apply private debt
  LegislativeBranch enact public guarded
  LegislativeBranch open_debate public guarded
  LegislativeBranch open_voting public guarded
  LegislativeBranch propose public guarded
  LegislativeBranch vote public guarded
  PromotionSystem _apply private debt
  PromotionSystem _apply private debt
  PromotionSystem _apply private debt
  PromotionSystem fail_gate public guarded
  PromotionSystem pass_gate public guarded
  PromotionSystem start_promotion public guarded
  SupremeOversight _apply private debt
  SupremeOversight generate_compliance_report public guarded
  _FederationUndo _restore private debt
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && cat docs/audit/evidence/W-617/mutation_probe_wi106.py docs/audit/evidence/W-617/mutation_probe_wi106.out.txt
EXIT: 0
BYTES: 5694
SHA256: d7ea38ad7c08a292efc4db1ad4fc9d897b6342df977743460e26531bc3b3ba4e
NO_EOL: 0
--- OUTPUT ---
"""مسبارُ طفراتِ WI-106 (الدفعةُ F1) — دليلُ قيدِ W-617.

الغرض: تطبيقُ كلِّ طفرةٍ مُعلَنةٍ في ملحقِ التصميمِ (§ 5 · M1–M5) على نسخةِ الوحدةِ،
وتشغيلُ فحوصِ البندِ، وإثباتُ أنَّ كلَّ طفرةٍ تُسقِطُ فحصَها المُعلَنَ ثمَّ استعادةُ الأصلِ
بايتًا ببايتٍ (البصمةُ قبلُ وبعدُ).
التشغيل: من جذرِ المستودعِ — `.venv/bin/python docs/audit/evidence/W-617/mutation_probe_wi106.py`
المالك: Perplexity Computer · تاريخ الإنشاء: 2026-10-22
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SERVICES = ROOT / "federal" / "executive" / "services"
TARGET = SERVICES / "src/amos_federation/services/governance/federation.py"
TESTS = "tests/test_wi106_federation_coordinate_sovereign.py"


def _m1(src: str) -> str:
    head, tail = src.split('operation = "LegislativeBranch.propose"', 1)
    guard = re.search(r"_federation_authorizer\(\)\.guard_declared\(.*?\n        \)\n", tail, re.S)
    assert guard
    return head + 'operation = "LegislativeBranch.propose"' + tail.replace(
        guard.group(0), "_apply(None)\n", 1
    )


MUTATIONS = {
    "M1 · propose يكتبُ بلا عبورٍ": (_m1, ["t1", "t3"]),
    "M2 · الفاعلُ JUDICIAL": (
        lambda s: s.replace('FEDERATION_ACTOR = "EXECUTIVE"', 'FEDERATION_ACTOR = "JUDICIAL"', 1),
        ["t1", "t8"],
    ),
    "M3 · المُعوِّضُ لا يفعلُ شيئًا": (
        lambda s: s.replace(
            "    def _restore(self) -> None:\n", "    def _restore(self) -> None:\n        return\n", 1
        ),
        ["t4", "t5"],
    ),
    "M4 · vote بلا تسجيلِ السابقِ": (
        lambda s: re.sub(r"\n *undo\.prior\(record, \"voters\"[^\n]*", "", s, count=1),
        ["t5"],
    ),
    "M5 · مفتاحُ enact بمُعرِّفِ استدعاءٍ": (
        lambda s: s.replace(
            'f"legislations/{legislation_id}/enact"',
            'f"legislations/{legislation_id}/enact/{_nonce()}"',
            1,
        ),
        ["t6"],
    ),
}


def _run(selector: str) -> tuple[int, str]:
    r = subprocess.run(
        [sys.executable, "-m", "pytest", TESTS, "-q", "-p", "no:cacheprovider", "-k", selector],
        cwd=SERVICES,
        capture_output=True,
        text=True,
        timeout=900,
        check=False,
    )
    lines = [ln for ln in r.stdout.splitlines() if "passed" in ln or "failed" in ln]
    return r.returncode, (lines[-1] if lines else r.stdout[-300:])


def main() -> int:
    original = TARGET.read_bytes()
    digest = hashlib.sha256(original).hexdigest()
    print(f"sha256 قبلُ: {digest}")
    rc, line = _run("wi106")
    print(f"الأصلُ: rc={rc} · {line}")
    all_killed = rc == 0
    try:
        for name, (mutate, expected) in MUTATIONS.items():
            mutated = mutate(original.decode("utf-8"))
            assert mutated != original.decode("utf-8"), f"الطفرةُ لم تُطبَّق: {name}"
            TARGET.write_text(mutated, encoding="utf-8")
            for test in expected:
                rc, line = _run(f"wi106_{test}_")
                killed = rc != 0
                all_killed = all_killed and killed
                print(f"{name} ⇒ {test}: {'سقطَ (قُتِلَت)' if killed else 'نجحَ (نجَت!)'} · {line}")
            TARGET.write_bytes(original)
    finally:
        TARGET.write_bytes(original)
    after = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    print(f"sha256 بعدُ: {after} · {'مطابقٌ' if after == digest else 'مختلفٌ!'}")
    print("الحكمُ: كلُّ الطفراتِ قُتِلَت" if all_killed and after == digest else "الحكمُ: فشلٌ")
    return 0 if all_killed and after == digest else 1


if __name__ == "__main__":
    raise SystemExit(main())
sha256 قبلُ: 845f337feb4d5b609511fa60f642cacc4b3f85e85f14e19c009ca20accb874d4
الأصلُ: rc=0 · ============================== 8 passed in 6.52s ===============================
M1 · propose يكتبُ بلا عبورٍ ⇒ t1: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 0.91s ========================
M1 · propose يكتبُ بلا عبورٍ ⇒ t3: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 0.86s ========================
M2 · الفاعلُ JUDICIAL ⇒ t1: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 0.73s ========================
M2 · الفاعلُ JUDICIAL ⇒ t8: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 0.75s ========================
M3 · المُعوِّضُ لا يفعلُ شيئًا ⇒ t4: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 0.76s ========================
M3 · المُعوِّضُ لا يفعلُ شيئًا ⇒ t5: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 0.79s ========================
M4 · vote بلا تسجيلِ السابقِ ⇒ t5: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 0.81s ========================
M5 · مفتاحُ enact بمُعرِّفِ استدعاءٍ ⇒ t6: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.61s ========================
sha256 بعدُ: 845f337feb4d5b609511fa60f642cacc4b3f85e85f14e19c009ca20accb874d4 · مطابقٌ
الحكمُ: كلُّ الطفراتِ قُتِلَت
exit=0
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_seat.db .venv/bin/python docs/audit/evidence/W-617/mutation_probe_wi106.py
EXIT: 0
BYTES: 1643
SHA256: 0423e11235a80653c4bfe976aea96a09cac8757585e63a2d64fcd993e79b5229
NO_EOL: 0
--- OUTPUT ---
sha256 قبلُ: 845f337feb4d5b609511fa60f642cacc4b3f85e85f14e19c009ca20accb874d4
الأصلُ: rc=0 · ============================== 8 passed in 9.48s ===============================
M1 · propose يكتبُ بلا عبورٍ ⇒ t1: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.07s ========================
M1 · propose يكتبُ بلا عبورٍ ⇒ t3: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.05s ========================
M2 · الفاعلُ JUDICIAL ⇒ t1: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.44s ========================
M2 · الفاعلُ JUDICIAL ⇒ t8: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.28s ========================
M3 · المُعوِّضُ لا يفعلُ شيئًا ⇒ t4: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.39s ========================
M3 · المُعوِّضُ لا يفعلُ شيئًا ⇒ t5: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.31s ========================
M4 · vote بلا تسجيلِ السابقِ ⇒ t5: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.32s ========================
M5 · مفتاحُ enact بمُعرِّفِ استدعاءٍ ⇒ t6: سقطَ (قُتِلَت) · ======================= 1 failed, 7 deselected in 1.74s ========================
sha256 بعدُ: 845f337feb4d5b609511fa60f642cacc4b3f85e85f14e19c009ca20accb874d4 · مطابقٌ
الحكمُ: كلُّ الطفراتِ قُتِلَت
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && rg -n "D17-1|Q-61" docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 0
BYTES: 11597
SHA256: cd0d703e04d96167a441696250ac36e7a7af899dba05859c2445e815371543a8
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-22 (`W-612` — **D17-2** الأربعةُ مؤجَّلةٌ ولا تعطّلُ J2/J3 · **إبلاغُ ما بعدَ الدمجِ** يبقى إبلاغًا (توجيهُ المستشارِ 19 § 1)) · ووقبله ((`W-611` — **Q-61 DECIDED** بالخيارِ (3) بتطبيقٍ صريحٍ على WI-096 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-610` — **D19 DECIDED**: إذنُ المالكِ بإغلاقِ WI-105 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`)))
2296:### Q-61 · عرضُ التصميمِ قبلَ الشِّفرةِ في WI-096 — DECIDED (W-611)
2297:«Q-61: خيار (3) مع تطبيق صريح على WI-096. أقرّ أن شرط عرض التصميم قبل الشفرة لم يتحقق إجرائيًّا في WI-096 وأتجاوزه لهذا البند وحده لأن المعايير 2 و3 و4 تحققت بإجماع المقاعد، ويُقيَّد الإخلال كما هو. وللبنود القادمة يُودَع التصميم في التزام مستقل يسبق الشفرة. ثم تُعاد جولة WI-096 بمسبار كل مقعد.» ⇒ تفصيلُه تحتَ `## Q-61`.
2346:### D17-1 · فاعلُ `governance/federation.py` — DECIDED
2363:«لا جولات مجلس على تصميم منفرد من الآن. الجولة الواحدة لكل دفعة تغطي التصميم والشفرة والأدلة معًا بعد التنفيذ. شرط الترتيب باقٍ: التزام وثيقة التصميم يسبق التزام الشفرة في التاريخ (يتحقق منه الفاحص)، وهذا هو درس Q-61. … حجم الدفعة: كل دفعة تقدَّم إلى main تنقص D-4 بما لا يقل عن عشرة أسطح حيث يسمح النمط، إلا ما فرضه التصميم (J1 = 2 لأنه يُرسي النمط).» — نُفِّذَ تعديلُ البروتوكولِ مؤرَّخًا (W-592).
2520:## Q-61 · هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — DECIDED (2026-10-22 · W-611 · توجيهُ المستشارِ 19 § 1 · الخيارُ 3 بتطبيقٍ صريحٍ على WI-096) · وكانَ PENDING_OWNER (2026-10-19 · W-521)
2522:> **[إضافةٌ مؤرَّخةٌ · 2026-10-22 · W-611] DECIDED — نصُّ المالكِ حرفيًّا:** «Q-61: خيار (3) مع تطبيق صريح على WI-096. أقرّ أن شرط عرض التصميم قبل الشفرة لم يتحقق إجرائيًّا في WI-096 وأتجاوزه لهذا البند وحده لأن المعايير 2 و3 و4 تحققت بإجماع المقاعد، ويُقيَّد الإخلال كما هو. وللبنود القادمة يُودَع التصميم في التزام مستقل يسبق الشفرة. ثم تُعاد جولة WI-096 بمسبار كل مقعد.» (النصُّ الكاملُ للتوجيهِ في [`evidence/W-610/ADVISOR_DIRECTIVE_19.md`](evidence/W-610/ADVISOR_DIRECTIVE_19.md)) ⇒ (أ) **الإخلالُ مُقيَّدٌ كما هو**: وثيقةُ التصميمِ وشِفرتُه في الالتزامِ نفسِه `cacd1a7` (W-471) — والمعيارُ (1) لم يتحقق إجرائيًّا · (ب) تجاوزُه **لـWI-096 وحدَه** · (ج) **للبنودِ القادمةِ**: التصميمُ في التزامٍ مستقلٍّ يسبقُ الشِّفرةَ · (د) تُعادُ جولةُ WI-096 بمسبارِ كلِّ مقعدٍ (§ 4.9) — لا VERIFIED قبلَها.
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q
EXIT: 0
BYTES: 110
SHA256: a319349b669ac5c1fc0fc2bb78dce70aad7115f4675ec556a36791daaf91ee01
NO_EOL: 0
--- OUTPUT ---
..............................................................           [100%]
62 passed in 85.60s (0:01:25)
=== RAW [19] END ===
=== RAW [20] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
EXIT: 0
BYTES: 319
SHA256: e237b66d4e4686ec1d76c273157268e76598e93fa5418cfa9090f52a8c38efd9
NO_EOL: 0
--- OUTPUT ---
عقدُ نَسَبِ القياساتِ مستقيمٌ: 11 قياسًا مقيَّدًا · 8 محروسًا (‏منها 1 برباطٍ مقيسٍ نصًّا) · 3 مُعلَنًا بسببٍ مكتوبٍ. ومُؤَجَّلٌ إلى الشطرِ الآخرِ: 2 (‏من 2 يحتاجُ حزمًا خارجيّةً).
=== RAW [20] END ===
=== RAW [21] BEGIN ===
CMD: find /home/user/workspace/council_w620/kimi_k3 -maxdepth 1
EXIT: 0
BYTES: 283
SHA256: a4c3b2e79e620d85bd09588e50d4316fd402d53eb41c29aa3eb9cc259e8b0633
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w620/kimi_k3
/home/user/workspace/council_w620/kimi_k3/repo
/home/user/workspace/council_w620/kimi_k3/tmp
/home/user/workspace/council_w620/kimi_k3/briefing.md
/home/user/workspace/council_w620/kimi_k3/probe
/home/user/workspace/council_w620/kimi_k3/raw
=== RAW [21] END ===
=== RAW [22] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w620/kimi_k3/probe/probe_wi106_kimi_k3.py
EXIT: 0
BYTES: 8317
SHA256: 5396b4e25a7ec98394cbf9a761c7f34ef4dd202244e567eacf472653c1314bab
NO_EOL: 0
--- OUTPUT ---
     1	"""
     2	مسبارُ المقعدِ kimi_k3 الخاصُّ لجولةِ WI-106 (F1 · coordinate) — يُنادي المسارَ
     3	الإنتاجيَّ وحدَه (الأسطحَ العامّةَ في governance/federation.py) ويحاولُ كسرَ ثلاثِ
     4	خواصَّ مُدَّعاةٍ في المعيارِ (2):
     5	
     6	  P1 · إعادةُ الإقرارِ على مسارِ «مرفوضٌ» (rejected): القانونُ الذي تصوُتُ
     7	       الأغلبيّةُ ضدَّه يعبرُ الحدَّ ويُدوَّنُ مفتاحُه — فالإقرارُ الثاني يجبُ أن
     8	       يُرفَعَ FederationReplayError صريحًا لا أن يعودَ «rejected» بنجاحٍ صامتٍ
     9	       (إن رجعَ بنجاحٍ… انكسرتِ الخاصيّةُ: الإعادةُ تُعادُ كأثَرٍ ثانٍ).
    10	  P2 · مُعوِّضُ الإنشاءِ على سطحٍ لم يُغطِّه فحصُ T4 — ApprovalSystem.request_approval:
    11	       إسقاطُ تثبيتِ النجاحِ بعدَ الأثرِ يجبُ أن يُعيدَ الحالةَ نظيفةً كاملةً
    12	       (لا صفَّ Approval يتسرَّب).
    13	  P3 · فاعلٌ بقيمةٍ أخرى من عائلةِ الفروعِ («LEGISLATIVE») يجبُ أن يُرفَضَ على
    14	       سطحينِ لم يختبرْهما T2/T3 بالقيمةِ نفسِها: JudicialBranch.rule و
    15	       SupremeOversight.generate_compliance_report — ولا صفَّ يُكتَبُ.
    16	
    17	الملفّ pytest بحتٌ يُنسَخُ مؤقّتًا إلى federal/executive/services/tests/ (إذنُ الإحاطةِ د)
    18	ويُشغَّلُ من جذرِ المستودعِ بقاعدةِ sqlite خاصّةٍ بالمقعد.
    19	"""
    20	
    21	from __future__ import annotations
    22	
    23	import math
    24	import time
    25	from typing import Any
    26	
    27	import pytest
    28	from sqlalchemy import create_engine, select
    29	
    30	from amos_federation.common.database import get_database_url, get_session_factory
    31	from amos_federation.services.agent_runtime.population import get_population_registry
    32	from amos_federation.services.governance import federation as federation_module
    33	from amos_federation.services.governance.federation import (
    34	    ApprovalModel,
    35	    ApprovalSystem,
    36	    CourtCaseModel,
    37	    FederationReplayError,
    38	    JudicialBranch,
    39	    LegislativeBranch,
    40	    LegislationModel,
    41	    SupremeOversight,
    42	    _GovBase,
    43	)
    44	from core.sovereignty.compensation import CompensationRequired
    45	from core.sovereignty.gateway import SovereigntyViolation
    46	
    47	
    48	@pytest.fixture(autouse=True)
    49	def _clean_tables() -> Any:
    50	    url = get_database_url()
    51	    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    52	    _GovBase.metadata.create_all(create_engine(url, connect_args=connect_args))
    53	    get_population_registry().seed_initial_population()
    54	    federation_module.reset_federation_authorizer()
    55	    yield
    56	    session = get_session_factory()()
    57	    try:
    58	        for model in (ApprovalModel, LegislationModel, CourtCaseModel):
    59	            session.execute(pytest.importorskip("sqlalchemy").delete(model))
    60	        session.commit()
    61	    finally:
    62	        session.close()
    63	    federation_module.reset_federation_authorizer()
    64	
    65	
    66	def _agent() -> str:
    67	    return get_population_registry().list_agents()[0]["agent_id"]
    68	
    69	
    70	def _count(model: type) -> int:
    71	    session = get_session_factory()()
    72	    try:
    73	        return len(session.execute(select(model)).scalars().all())
    74	    finally:
    75	        session.close()
    76	
    77	
    78	def _leg_row(leg_id: str) -> LegislationModel:
    79	    session = get_session_factory()()
    80	    try:
    81	        row = session.get(LegislationModel, leg_id)
    82	        assert row is not None
    83	        session.expunge(row)
    84	        return row
    85	    finally:
    86	        session.close()
    87	
    88	
    89	def _cross_second() -> None:
    90	    now = time.time()
    91	    time.sleep(math.ceil(now) - now + 0.05)
    92	
    93	
    94	def _draft_losing_law() -> str:
    95	    branch = LegislativeBranch()
    96	    leg_id = branch.propose("قانونُ المسبارِ p1", "نصٌّ خاسرٌ", "seat-kimi")["legislation_id"]
    97	    branch.open_debate(leg_id)
    98	    branch.open_voting(leg_id)
    99	    branch.vote(leg_id, _agent(), "against")
   100	    return leg_id
   101	
   102	
   103	def test_p1_replay_refused_even_on_rejected_path() -> None:
   104	    """الإقرارُ الثاني لقانونٍ رُفِضَ في الأولى يجبُ أن يُرفَعَ صريحًا."""
   105	    branch = LegislativeBranch()
   106	    leg_id = _draft_losing_law()
   107	    first = branch.enact(leg_id)
   108	    assert first["status"] == "rejected"
   109	    stamp_before = _leg_row(leg_id).updated_at
   110	
   111	    _cross_second()
   112	    with pytest.raises(FederationReplayError):
   113	        branch.enact(leg_id)
   114	    row = _leg_row(leg_id)
   115	    assert row.status == "rejected"
   116	    assert row.updated_at == stamp_before
   117	
   118	
   119	def test_p2_creation_compensator_on_request_approval(monkeypatch: pytest.MonkeyPatch) -> None:
   120	    """فشلُ التثبيتِ بعدَ إنشاءِ صفِّ الموافقةِ يستعيدِهِ كاملًا (لا صفَّ يتسرَّب)."""
   121	    authorizer = federation_module._federation_authorizer()
   122	    ledger = authorizer.boundary.idempotency_ledger
   123	    original = type(ledger).mark_succeeded
   124	
   125	    def _broken_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
   126	        raise RuntimeError("مسبارُ kimi_k3: تثبيتُ النجاحِ مُسقَطٌ عمدًا")
   127	
   128	    monkeypatch.setattr(type(ledger), "mark_succeeded", _broken_mark_succeeded)
   129	    privately, publicly = ApprovalSystem().signer.generate_keypair()
   130	    with pytest.raises(CompensationRequired) as caught:
   131	        ApprovalSystem().request_approval("budget_shift", "probe-target", "seat-kimi", privately, publicly)
   132	    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
   133	
   134	    assert caught.value.outcome.state_is_clean is True
   135	    assert caught.value.outcome.requires_human is False
   136	    assert _count(ApprovalModel) == 0
   137	
   138	    _cross_second()
   139	    ApprovalSystem().request_approval("budget_shift", "probe-target", "seat-kimi", privately, publicly)
   140	    assert _count(ApprovalModel) == 1
   141	
   142	
   143	def test_p3_legislative_actor_denied_on_rule_and_report() -> None:
   144	    """فاعلٌ «LEGISLATIVE» لا يجوزُ له العبورُ — ولا صفَّ يتغيَّر."""
   145	    judicial = JudicialBranch()
   146	    case_id = judicial.file_case("claimant", "defendant", "موضوعُ مسبارِ p3")["case_id"]
   147	    before_cases = _count(CourtCaseModel)
   148	
   149	    monkey_value = "LEGISLATIVE"
   150	    original_actor = federation_module.FEDERATION_ACTOR
   151	    try:
   152	        federation_module.FEDERATION_ACTOR = monkey_value
   153	        federation_module.reset_federation_authorizer()
   154	        with pytest.raises(SovereigntyViolation):
   155	            judicial.rule(case_id, "حكمٌ بفاعلٍ غيرِ تنفيذيٍّ", "judge")
   156	        with pytest.raises(SovereigntyViolation):
   157	            SupremeOversight().generate_compliance_report("2026-10")
   158	    finally:
   159	        federation_module.FEDERATION_ACTOR = original_actor
   160	        federation_module.reset_federation_authorizer()
   161	
   162	    assert _count(CourtCaseModel) == before_cases
   163	    session = get_session_factory()()
   164	    try:
   165	        row = session.get(CourtCaseModel, case_id)
   166	        assert row is not None and row.status != "ruled"
   167	    finally:
   168	        session.close()
=== RAW [22] END ===
=== RAW [23] BEGIN ===
CMD: cd /home/user/workspace/council_w620/kimi_k3/repo && cp /home/user/workspace/council_w620/kimi_k3/probe/probe_wi106_kimi_k3.py federal/executive/services/tests/test_probe_wi106_kimi_k3.py && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/kimi_k3/tmp/amos_probe.db .venv/bin/python -m pytest federal/executive/services/tests/test_probe_wi106_kimi_k3.py -q
EXIT: 0
BYTES: 624
SHA256: 325fdcf390670a38329b53dd64cbd11c657692a4af4003969d57adc9b338ca71
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w620/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 3 items

federal/executive/services/tests/test_probe_wi106_kimi_k3.py ...         [100%]

============================== 3 passed in 2.39s ===============================
=== RAW [23] END ===
VERDICT_PER_CRITERION:
(1) نعم — الملحقُ قبلَ الشِّفرةِ: كتلة 5 تُظهِرُ أنَّ docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md التُزِمَ في e5ce7612 (قيدُ W-615) قبلَ التزامِ الشِّفرةِ fd6c1af3 (قيدُ W-617)، وكتلة 3 تؤكدُ الترتيبَ كاملًا على المدى 5a7520c..HEAD.
(2) نعم — الأسطحُ الخمسةَ عشرَ كلُّها تعبرُ بالفعلِ coordinate بفاعلٍ EXECUTIVE مُعلَنٍ ومُعوِّضٍ حقيقيٍّ ومفتاحِ عمليّةٍ: كتلة 7 (فرقُ الشِّفرةِ كاملًا: guard_declared في كلِّ سطحٍ عامٍّ بعقدِ عبورٍ واحدٍ D3) وكتلة 10 (فحوصُ T1–T8 الثمانيةُ كلُّها ناجحةٌ: 8 passed، وهي تقيسُ العمليّاتِ الخمسَ عشرةَ والفعلَ والقرارَ والمُعوِّضَ والإعادةَ) وكتلة 17 (الطفراتُ الخمسُ تُسقِطُ هذه الخواصَّ كلَّها فيُقتَلنَ).
(3) نعم — الدَّينُ 181 ← 166 والسياديُّ 18 ← 33 مقيسانِ بالأداةِ نفسِها في تشغيلي: كتلة 9 (مواضعُ كتابةٍ كلُّها 236 · منها تعبرُ الحدَّ 33 · لا تعبرُ 166) وتطابقُ «قبلُ» في كتلة 15 (federation_sites_before.txt: خمسةَ عشرَ سطحًا عامًّا debt) و«بعدُ» في كتلة 15 (federation_sites_after.txt: الخمسةَ عشرةَ public guarded) — والنموُّ 220 ← 236 حصرًا داخلَ الوحدةِ (كتل 7 و15)؛ ولا نموَّ في غيرِ الوحدةِ (كتلة 9: التوزيعُ على الملفّاتِ الأخرى كما هو في قياسِ «قبلُ» الواردِ في كتلة 14).
(4) نعم — فحوصُ البندِ ناجحةٌ (كتلة 10: 8 passed) وكلُّ طفرةٍ مُعلَنةٍ تُسقِطُ فحصَها: كتلتا 16 و17 — أعدتُ تشغيلَ مسبارِ الطفراتِ بنفسي فسقطَت المساراتُ الثمانيةُ كلُّها (M1×t1/t3 · M2×t1/t8 · M3×t4/t5 · M4×t5 · M5×t6) وبصمةُ الأصلِ بعدَ الاستعادةِ مطابقةٌ.
(5) نعم في شقِّ «بلا تعديلٍ» — كتلة 6: فرقُ test_federation.py وtests/sovereignty وcore/sovereignty بينَ 5a7520c وHEAD فارغٌ تمامًا (صفرُ بايت)؛ والحزمُ في تشغيلي كلُّها خضراءُ: test_federation.py ‏43 passed (كتلة 11) · tests/sovereignty ‏818 passed + ‏1 skipped (كتلة 12) · حزمةُ الخدماتِ كاملةً 1493 passed + ‏53 skipped (كتلة 13) · فحوصُ الحوكمةِ 62 passed (كتلة 19) · provenance ‏exit 0 (كتلة 20). وأمامَ شقِّ CI: «يقرؤه المنسِّقُ ويُقيِّدُه».
(6) نعم — مراجعةٌ أعادَتِ التشغيلَ بمسبارِ المقعدِ: هذه الجولةُ نفسُها، ومسباري الخاصُّ على المسارِ الإنتاجيِّ في الكتلتين 22 (الشِّفرة) و23 (التشغيل: 3 passed).
PROBES: مسبارٌ واحدٌ — كتلةُ الشِّفرةِ 22 · كتلةُ التشغيلِ 23 (3 passed · exit 0) · الخواصُّ التي حاولَ كسرَها: (P1) إعادةُ enact على قانونٍ نتيجتُه «rejected» يجبُ أن تُرفَعَ FederationReplayError لا أن تُعادَ بنجاحٍ صامتٍ · (P2) فشلٌ بعدَ أثرِ الإنشاءِ على سطحِ request_approval (غيرِ المُغطَّى في T4/T5) يجبُ أن يُعوَّضَ كاملًا · (P3) فاعلٌ LEGISLATIVE يحاولُ rule وgenerate_compliance_report يجبُ أن يُرفَضَ بلا كتابةٍ — **انكسرت؟ لا**: الثلاثةُ صمدَت فرفضَتِ الإعادةَ صريحةً واستُعيدَ الصفُّ نظيفًا ورُفِضَ الفاعلُ غيرُ التنفيذيِّ بلا أثرٍ.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً.
ISOLATION_DECLARATION: أقرُّ أنّني لم أقرأْ شيئًا خارجَ استنساخي الخاصِّ /home/user/workspace/council_w620/kimi_k3/repo وهذهِ الإحاطةِ المنسوخةِ في دليلي — لا أدلّةَ جولاتٍ سابقةً ولا سجلَّ إكمالٍ ولا عملَ مقاعدَ أخرى ولا تقاريرَ منفِّذٍ: نعم، بلا أيِّ استثناءٍ.
VERDICT: PASS لكلِّ المعاييرِ (1)–(6).
