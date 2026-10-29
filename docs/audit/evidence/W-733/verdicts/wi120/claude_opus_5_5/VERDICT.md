# حكمُ مقعدِ المجلسِ — claude_opus_5_5 · جولةُ WI-120 (W-732 · مُعلَّقةٌ)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ WI-120 المُطلَقةِ في W-732 (قرارُ المالكِ D28 «أطلق الجولة الآن») — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w732/claude_opus_5_5/wi120) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (103233 بايتًا · sha256 `5d6dd32a0de71b6f418956ce8c507970b70a5a486aa1171303b47182f6f7baa9`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-120 عندَ العقدةِ `73379d69dee4db3771dda46728ddb11ecfa2d46d` — الحكمُ FAIL بملاحظةٍ حاجبةٍ (Q-26). لا يُحسَبُ نصابًا (توجيهُ المستشارِ 29 § 1 · قرارُ D30): الجولةُ لم تكتمل لأنَّ عائلةً واحدةً فقط كانت متاحةً، والحكمُ مختومٌ على عقدةٍ قديمةٍ ولا يُعادُ استعمالُه في الجولةِ القادمة.

## المالك
المنسِّقُ (قيدُ W-733) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-29

## تاريخ آخر تعديل
2026-10-29 (W-733 — القيدُ نفسُه)

## المحتويات
`VERDICT.md` — نصُّ الحكمِ حرفيًّا.

---
MODEL: claude_opus_5_5 (Claude Opus 5.5 · كما أعلنتْهُ المنصةُ)
FAMILY: Anthropic · Claude
RUN_DATE: 2026-10-29 12:51 +00:00
NODE: 73379d69dee4db3771dda46728ddb11ecfa2d46d
CLONE_PATH: /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo (استنساخٌ كاملٌ بيدي: `git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo` ثمَّ `git checkout` للعقدةِ (الأمرانِ 1–2) ثمَّ `bash tools/dev/bootstrap.sh` داخلَهُ — خروجٌ 0)
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-732/council_briefs/
 2. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-732/council_briefs/) && git rev-parse HEAD
 3. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git log --format='%h %cI %s' -8 -- core/constitutional_engine/rules.py federal/executive/services/src/amos_federation/services/governance/ tests/constitutional/test_g1_vocabulary.py
 4. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && ls docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md && rg -n 'Q-13|Q-14|Q-26|Q-23' docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md | head -12
 5. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/constitutional/test_g1_vocabulary.py
 6. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w723_g1_state_runtime_system_life.py
 7. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w724_g1_expansion.py
 8. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w728_g1_learning_security.py
 9. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_q3_branch_declaration_surface.py
 10. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 11. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && sed -i 's/"issue_certificate"/"issue_certificate_mutated"/' core/constitutional_engine/rules.py && .venv/bin/python -m pytest -q -p no:cacheprovider tests/constitutional/test_g1_vocabulary.py
 12. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git checkout -- core/constitutional_engine/rules.py && git status --porcelain && git diff --stat
 13. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && sed -i 's/guard_declared(/guard_declared_mutated(/' federal/executive/services/src/amos_federation/services/governance/learning_cycle.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w728_g1_learning_security.py
 14. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/learning_cycle.py && git status --porcelain
 15. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && rg -n 'Q-13|Q-14|Q-26|Q-23' docs/audit/SOVEREIGN_DECISION_REGISTER.md | head -12
 16. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && sha256sum docs/audit/evidence/W-732/council_briefs/wi120/briefing_claude_opus_5_5.md
 17. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && cat docs/audit/evidence/W-732/council_briefs/wi120/SHA256SUMS
 18. nl -ba /home/user/workspace/council_w732/claude_opus_5_5/wi120/probe/g1_probe.py
 19. cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python /home/user/workspace/council_w732/claude_opus_5_5/wi120/probe/g1_probe.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-732/council_briefs/
EXIT: 0
BYTES: 41
SHA256: 54342feda032c08050d11f904f226ab99ca6b8a1907a4d9b67b936ae47d2ebbd
NO_EOL: 0
--- OUTPUT ---
73379d69dee4db3771dda46728ddb11ecfa2d46d
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-732/council_briefs/) && git rev-parse HEAD
EXIT: 0
BYTES: 380
SHA256: 18efb2502b657e2ef1f201f379ca6bf86b8b77632f0e04585281bb5ca78672ac
NO_EOL: 0
--- OUTPUT ---
HEAD is now at 73379d69 W-732: إحاطاتُ جولةِ المجلسِ الواحدةِ (D28: WI-120 + WI-116) مبصومةً + TASKS_SENT + قياساتُ الجلسةِ + واجبُ N+1 لدفعةِ W-729 + بطاقاتُ هويةٍ للمادةِ التاسعةِ (README لترويسةِ الغرضِ $comment — سابقةُ W-729)
73379d69dee4db3771dda46728ddb11ecfa2d46d
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git log --format='%h %cI %s' -8 -- core/constitutional_engine/rules.py federal/executive/services/src/amos_federation/services/governance/ tests/constitutional/test_g1_vocabulary.py
EXIT: 0
BYTES: 4578
SHA256: b51d65f670cc4bdcce9b9caddaf403ba8e9721adc92f7f64430a0d14f734658c
NO_EOL: 0
--- OUTPUT ---
4477ec4a 2026-10-29T10:23:15Z W-728: directive 28 §2(3) — G1 batch-4 code (learning_cycle + security · §9.10): 9 surfaces cross the sovereign boundary via Boundary.enforce — collect_experiences (record_curriculum_step ≥1) · complete_training (release_agent · never blocked — Q-78) · start_shadow/start_canary (invoke_model ≥4 · Q-80ب) · promote_beta_to_alpha (activate_agent ≥4 · Q-80ج · two effects under one target with coordinated compensation) · create_session (execute_task ≥4 · session token never enters boundary target/key) · check_rate/verify_certificate (log_isolated_action · rejection path writes nothing) · issue_certificate (issue_certificate ≥3 · KILL_SWITCH@3) — start_training/evaluate_model/store_secret held (Q-80أ · §9.1) unguarded (test_c3) · effect signature = kind:resource with op/transition inside the resource string (precedent suspend_state · prevents permit collision within one second) · +59 tests in services (test_w728_g1_learning_security.py) · mutation campaign 9/9 killed on evidence · D-4 104 ← 95 (real burn 9 · matches §9.10 projection) · services suite 1768 passed · 53 skipped = 1821 · root suite 2793 collected (all green) · N+1 CI verdicts for W-727 on 202b5423 (×4 readable · green · same node) · q3 fixture refreshed with measured values (defaulted authorizer sites 4→9 · path takeover from WI-082 per §6.1 · W-567 precedent) · published measurements regenerated (write_inventory_p13 · final_audit_p14 · decision_wave_map 11+34+50=95 · decision_gate_ledger --record-work W-728 · truth matrix 61 stable) · handbook suite rows measured with was-written chain · Q-80 remains PENDING_OWNER · no council round — G1 council per D28 comes next with owner confirmation · executor (Perplexity Computer · GLM-5.3)
62123614 2026-10-29T04:57:28Z W-724 (2/3): graceful_shutdown verb (Q-76 ②, never blocked) + G1 expansion crosses the sovereign boundary — 6 surfaces guarded (take_exam · submit_output · approve_output · employ_batch · graduate_batch · retire_agent with coordinated compensation Q-26) · pre-boundary request_permit before inner crossings · create_batch/enroll_batch held (Q-77) · 40 checks + mutation campaign 6/6 killed on evidence · executor (Perplexity Computer)
f9d23a8d 2026-10-28T20:37:02Z W-723 (2/3): G1 state_runtime + system_life cross the sovereign boundary — 11 surfaces guarded (register_state royal decree Q-13 · suspend/reactivate with governed-suspension record Q-14 · assign_agent · send_message · bootstrap · health_check · self_heal conditional · graceful_shutdown · create_backup · launch_checklist) · restore_backup left as debt (D28 (a)) · 54 checks · executor (Perplexity Computer)
4f2743bd 2026-10-28T17:39:27Z W-722: WI-120 دفعةُ معجمِ G1 (§ 5.1) — issue_certificate · create_backup · self_heal تنفيذيّةً · suspend_policy · vote تشريعيّةً · مستويا زرِّ الإيقاف · +15 فحصًا · D-4 = 121 بلا تغيُّر
153109cf 2026-10-26T21:30:29Z W-696: شِّفرةُ E1 · أسطحُ executive_core الستةُ تعبرُ الحدَّ السياديَّ (القاموسُ 13 اسمًا باعتمادِ Q-73 · نوى خاصّةٌ ومعوّضاتٌ · فحوصُ الأصنافِ الخمسةِ 14 · قياسُ القبولِ D-4 135←129 والسياديّةُ 46←51) + واجبُ N+1 لدفعةِ W-695 (حكما main على 13f1edf6 مقروءانِ أخضرانِ) · لا انتقالَ حالةٍ · المنسِّقُ GLM-5.3 (Perplexity Computer)
f8d33807 2026-10-26T10:15:25Z W-689: شِفرةُ تحصينِ WI-117 — require_king على المساراتِ الأربعةِ (reset ×2 · promotions · gates) + تحصينُ sign_approval (الموقِّعُ هويةُ الرمزِ لا جسمَ الطلبِ) + 13 فحصًا + طفرةٌ مقتولةٌ + مسبارُ HTTP حقيقيٌّ (مواطنٌ ⇒ 403 ×5 والمستوى halt والملكُ 200) · انتقالٌ واحدٌ: IN_PROGRESS→IN_REVIEW · D-4: تصحيحٌ لا حرقٌ · المنسِّقُ GLM-5.3 (Perplexity Computer)
cb3b3fb9 2026-10-25T10:29:46Z W-675: WI-114 السطحانِ 1 و3 — canary.py يعبرُ الحدَّ السياديّ (الخفضُ المُقنَّعُ عبرَ activate يُرفَضُ 403) · حكمُ N+1 لـPR #152 · وثائقُ الحالة
4247c68f 2026-10-23T23:56:33Z W-640: WI-111 (J2+J3) — 15 سطحًا قضائيًّا تعبرُ بفاعلِ الوحدةِ وأفعالِ D17-2 · D-4 157←142 · M1–M5 مقتولةٌ
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && ls docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md && rg -n 'Q-13|Q-14|Q-26|Q-23' docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md | head -12
EXIT: 0
BYTES: 4124
SHA256: 65937bf8a1eab6a417901f11996f485ec99ddb4d267addd5ab52e18357cd6587
NO_EOL: 0
--- OUTPUT ---
docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md
3:## الهدف: حرقٌ حقيقيٌّ لِD-4 — تصميمٌ يعرضُ نموذجَ الصلاحياتِ للأسطحِ العامةِ المتبقّيةِ تحتَ D-4 في `services/governance/` (41 سطحًا) قبلَ أيِّ شِفرةٍ، وفقَ القراراتِ الأربعةِ المحسومةِ (Q-13 · Q-14 · Q-26 · Q-23)
5:## المالك: Perplexity Computer (المنسِّقُ GLM-5.3) · بتوجيهِ الطابورِ: «دفعةُ G1 الورقيةُ (تصميمُ Q-13/Q-14/Q-26/Q-23) ثمَّ تحليلُ WI-118 وتصميمُ WI-116 — لا جولةَ مجلسٍ جديدةً قبلَ قرارِ المالكِ»
14:  - **Q-13 (الخيار 1)**: «register_state هي create_state دستوريًّا، فتحتاج مسار مرسوم ملكي.»
15:  - **Q-14 (الخيار 2 + 3 شروط)**: «إيقاف الولاية وإعادتها اختصاص تنفيذي محكوم بلا بوابة بشرية، بشرط أن يُسجَّل كل إيقاف أثرًا مُعلَنًا وأن يغطيه قاطع التشغيل، وأن يُراجَع إعادة التفعيل التلقائي في system_life.py:240 في تصميم الدفعة.»
16:  - **Q-26 (الخيار 2)**: «WRITE بمُعوِّض يعيد الوكيل، دون مس restore_agent الملكي.» (يخصُّ retire_agent)
17:  - **Q-23 (الخيار 1)**: «suspend_policy وvote يُضافان إلى المعجم التشريعي.»
45:كلُّ هذه الأسطحِ عملياتٌ خدميّةٌ داخليةٌ في النواةِ التنفيذيّةِ (`federal/executive/services/…/governance/`) لا تعبرُ HTTP مباشرةً — الفاعلُ **الفرعُ التنفيذيُّ** (`EXECUTIVE`) كما في سابقةِ E1/WI-119: طرفٌ تابعٌ تخضعُ له كلُّ قاعدةٍ دستوريّةٍ مُلزِمةٍ ومانعةٍ. **استثناءٌ واحدٌ معلَنٌ**: `register_state` — فاعلُهُ **الملكُ** (`ROYAL`) عبرَ مسارِ المرسومِ الملكيِّ (Q-13 · § 3.1 أدناه).
58:| `retire_agent` | EXECUTIVE | `contain_agent` (قائمٌ) | `agent:{agent_id}` | CREATE سجلُّ تقاعدٍ + أرشفةُ لقطةٍ + إيقافُ الوكيلِ | **بلا منعٍ** (احتواءٌ) | `(retire, agent_id, reason, الحالةُ السابقةُ, operation_id*)` | **معوِّضٌ يعيدُ الوكيلَ إلى حالتِهِ السابقةِ** (Q-26 · § 3.3) |
115:### 3.1 Q-13 — `register_state` مسارُ مرسومٍ ملكيٍّ
120:### 3.2 Q-14 — إيقافُ/إعادةُ الولايةِ + مراجعةُ `system_life.py:240`
124:- **الشرطُ 3 — مراجعةُ إعادةِ التفعيلِ التلقائيِّ في `system_life.py:240`**: المقيسُ اليومَ: `self_heal(component="states")` يمرُّ على كلِّ الولاياتِ المعلَّقةِ ويُعيدُ تفعيلَها **بلا شرطٍ** — وهذا يلغي عمليًّا كلَّ إيقافٍ تنفيذيٍّ محكومٍ (الإيقافُ قرارٌ والمُعالِجُ ينقضُه في أولِ جولةِ علاجٍ). **اقتراحٌ غيرُ معتمدٍ يُعرَضُ على المالكِ** (ليسَ نصَّ Q-14 بل استنتاجٌ من شرطِهِ الثالثِ): `self_heal` **لا يعيدُ تفعيلَ ولايةٍ عُلِّقَت بعبورٍ محكومٍ** إلا إذا كانَ سببُ التعليقِ في سجلِّ العبورِ من صنفِ «عطلٍ» لا «قرارٍ» — يُقرأُ سببُ الإيقافِ من سجلِّ العبورِ (الأثرُ المعلَنُ للشرطِ 1) قبلَ أيِّ إعادةِ تفعيلٍ. فإن كانَ القرارُ «احتواءً» (منَ المستوياتِ 1–3) بقيتِ الولايةُ معلَّقةً وسُجِّلَ `noop` في سجلِّ العلاجِ. هذا يُعرَضُ على المالكِ في § 8 لأنَّهُ سلوكٌ مُغيِّرٌ للمعالجِ القائمِ.
126:### 3.3 Q-26 — `retire_agent` بمُعوِّضٍ يعيدُ الوكيلَ
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/constitutional/test_g1_vocabulary.py
EXIT: 0
BYTES: 784
SHA256: 0bd5b38e728debe5404ffe486e6e3e22585a46f8142b92e8b190ace1bfeaeb6b
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
...................                                                      [100%]
19 passed in 0.09s
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w723_g1_state_runtime_system_life.py
EXIT: 0
BYTES: 1408
SHA256: 70b3e2e5fb67594a436e4221ea70ef88fe8991bec40e1113502fbf71fc55a1c4
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.14.0, asyncio-1.4.1, cov-7.1.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 54 items

federal/executive/services/tests/test_w723_g1_state_runtime_system_life.py . [  1%]
.....................................................                    [100%]

============================== 54 passed in 2.24s ==============================
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w724_g1_expansion.py
EXIT: 0
BYTES: 1404
SHA256: 2ba0ba905bc935b6f14d688f39bc9335d93a71e509643ab065f3de621d217cd2
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.14.0, asyncio-1.4.1, cov-7.1.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 40 items

federal/executive/services/tests/test_w724_g1_expansion.py ............. [ 32%]
...........................                                              [100%]

============================== 40 passed in 4.26s ==============================
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w728_g1_learning_security.py
EXIT: 0
BYTES: 1404
SHA256: a3b1065bab3c6b76dbd5ec17c4e689eecd235beb3ba47efc0834c13f140b1f43
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.14.0, asyncio-1.4.1, cov-7.1.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 59 items

federal/executive/services/tests/test_w728_g1_learning_security.py ..... [  8%]
......................................................                   [100%]

============================== 59 passed in 1.91s ==============================
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_q3_branch_declaration_surface.py
EXIT: 0
BYTES: 785
SHA256: ce57e7f79f94c8e550b67de14f3ea587bdbc154d4a832d51e869ff097ccad097
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
..........                                                               [100%]
10 passed in 10.47s
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 2653
SHA256: e69895406a828f553d201883ab7787cfd767520faf7f3d3e0a1bb092c6dd05d4
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 261
  عمليّاتٌ عامّةٌ مُغيِّرة   : 182
  منها تعبرُ الحدَّ        : 85
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 95
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     21 /   0 /   21
    services          159 /  85 /   73
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
      13  federal/executive/services/src/amos_federation/common/persistent.py
      10  federal/executive/services/src/amos_federation/services/federal_state/service.py
       9  federal/executive/services/src/amos_federation/services/governance/treasury.py
       9  federal/executive/services/src/amos_federation/services/royal/main.py
       7  federal/executive/services/src/amos_federation/services/state_treasury/service.py
       6  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
       4  federal/executive/services/src/amos_federation/common/database.py
       2  federal/executive/services/src/amos_federation/common/durable_event_bus.py
       2  federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py
       2  federal/executive/services/src/amos_federation/services/governance/expansion.py
       2  federal/executive/services/src/amos_federation/services/governance/learning_cycle.py
       2  federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py
       2  federal/executive/services/src/amos_federation/services/training/persistent_registry.py
       1  federal/executive/services/src/amos_federation/common/event_bus.py
       1  federal/executive/services/src/amos_federation/common/events.py
       1  federal/executive/services/src/amos_federation/services/api_gateway/store.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py
       1  federal/executive/services/src/amos_federation/services/governance/security.py
       1  federal/executive/services/src/amos_federation/services/governance/system_life.py
       1  federal/executive/services/src/amos_federation/services/government_services/service.py
       1  tools/migrations/r4_unify_agent_identity.py
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && sed -i 's/"issue_certificate"/"issue_certificate_mutated"/' core/constitutional_engine/rules.py && .venv/bin/python -m pytest -q -p no:cacheprovider tests/constitutional/test_g1_vocabulary.py
EXIT: 1
BYTES: 3813
SHA256: 0651e568bf689a3a58702035c8633b9f1aee44ed4276259617a04b964018bfe9
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
........F...F.F....                                                      [100%]
=================================== FAILURES ===================================
_ test_g1v_2_other_branches_are_denied_by_r003_1[issue_certificate-executive] __

action = 'issue_certificate', owner = <Branch.EXECUTIVE: 'executive'>

    @pytest.mark.parametrize("action,owner", sorted(NEW_NAMES.items()))
    def test_g1v_2_other_branches_are_denied_by_r003_1(action: str, owner: Branch) -> None:
        for actor in FOUR:
            if actor is owner:
                continue
            verdict = ENGINE.evaluate(
                ActionRequest(actor=actor, action=action, target="probe/g1")
            )
>           assert verdict.decision is Decision.DENY, (actor, action)
E           AssertionError: (<Branch.LEGISLATIVE: 'legislative'>, 'issue_certificate')
E           assert <Decision.ALLOW: 'ALLOW'> is <Decision.DENY: 'DENY'>
E            +  where <Decision.ALLOW: 'ALLOW'> = Verdict(decision=<Decision.ALLOW: 'ALLOW'>, request_fingerprint='585e46908b3975194f33bf9c710a307d', rules_evaluated=31...9bf07c568510c2a737f4204c5c264f495c1afefa022801c5ce6c0bb', advisory_violations=(), decision_kind='', authority_layer='').decision
E            +  and   <Decision.DENY: 'DENY'> = Decision.DENY

tests/constitutional/test_g1_vocabulary.py:70: AssertionError
____________ test_g1v_3_each_name_belongs_to_exactly_one_vocabulary ____________

    def test_g1v_3_each_name_belongs_to_exactly_one_vocabulary() -> None:
        vocabularies = (
            EXECUTIVE_ACTIONS,
            LEGISLATIVE_ACTIONS,
            JUDICIAL_ACTIONS,
            TREASURY_ACTIONS,
        )
        for action in NEW_NAMES:
>           assert sum(action in vocab for vocab in vocabularies) == 1, action
E           AssertionError: issue_certificate
E           assert 0 == 1
E            +  where 0 = sum(<generator object test_g1v_3_each_name_belongs_to_exactly_one_vocabulary.<locals>.<genexpr> at 0x7f325cc36f60>)

tests/constitutional/test_g1_vocabulary.py:82: AssertionError
____ test_g1v_5_kill_switch_blocks_at_and_above_level[issue_certificate-3] _____

action = 'issue_certificate', level = 3

    @pytest.mark.parametrize("action,level", [("issue_certificate", 3), ("self_heal", 4)])
    def test_g1v_5_kill_switch_blocks_at_and_above_level(action: str, level: int) -> None:
>       assert action in KILL_SWITCH_BLOCKS[level]
E       AssertionError: assert 'issue_certificate' in frozenset({'dispatch_agent', 'expand_state', 'issue_certificate_mutated', 'spawn_agent', 'update_agent_identity', 'update_population_state'})

tests/constitutional/test_g1_vocabulary.py:96: AssertionError
=========================== short test summary info ============================
FAILED tests/constitutional/test_g1_vocabulary.py::test_g1v_2_other_branches_are_denied_by_r003_1[issue_certificate-executive]
FAILED tests/constitutional/test_g1_vocabulary.py::test_g1v_3_each_name_belongs_to_exactly_one_vocabulary
FAILED tests/constitutional/test_g1_vocabulary.py::test_g1v_5_kill_switch_blocks_at_and_above_level[issue_certificate-3]
3 failed, 16 passed in 0.13s
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git checkout -- core/constitutional_engine/rules.py && git status --porcelain && git diff --stat
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && sed -i 's/guard_declared(/guard_declared_mutated(/' federal/executive/services/src/amos_federation/services/governance/learning_cycle.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w728_g1_learning_security.py
EXIT: 1
BYTES: 24485
SHA256: 9a2e88c1d860ad5cb2dd45100dae1d5292cb6c03f0b1f29339b47c4b8c47dee9
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/.venv/lib/python3.12/site-packages/pytest_asyncio/plugin.py:300: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the "fixture" caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to "function" scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.14.0, asyncio-1.4.1, cov-7.1.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 59 items

federal/executive/services/tests/test_w728_g1_learning_security.py FFFFF [  8%]
FFFFFF.......FFFFF....F..FFFFF.....FFFFF....FFFFF.....                   [100%]

=================================== FAILURES ===================================
___________________ test_c1_collect_blocked_at_level1_no_row ___________________
federal/executive/services/tests/test_w728_g1_learning_security.py:200: in test_c1_collect_blocked_at_level1_no_row
    cycle.collect_experiences(
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:233: in collect_experiences
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_____________ test_c1_complete_not_blocked_at_level5_q78_measured ______________
federal/executive/services/tests/test_w728_g1_learning_security.py:211: in test_c1_complete_not_blocked_at_level5_q78_measured
    out = cycle.complete_training(run_id, 1.0, operation_id="w728-c1")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:389: in complete_training
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c1_shadow_blocked_from_level4_q80b[3-False] _______________
federal/executive/services/tests/test_w728_g1_learning_security.py:225: in test_c1_shadow_blocked_from_level4_q80b
    cycle.start_shadow(alpha, beta, operation_id=f"w728-sh-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:620: in start_shadow
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c1_shadow_blocked_from_level4_q80b[4-True] ________________
federal/executive/services/tests/test_w728_g1_learning_security.py:223: in test_c1_shadow_blocked_from_level4_q80b
    cycle.start_shadow(alpha, beta, operation_id=f"w728-sh-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:620: in start_shadow
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c1_shadow_blocked_from_level4_q80b[5-True] ________________
federal/executive/services/tests/test_w728_g1_learning_security.py:223: in test_c1_shadow_blocked_from_level4_q80b
    cycle.start_shadow(alpha, beta, operation_id=f"w728-sh-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:620: in start_shadow
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c1_canary_blocked_from_level4_q80b[3-False] _______________
federal/executive/services/tests/test_w728_g1_learning_security.py:237: in test_c1_canary_blocked_from_level4_q80b
    cycle.start_canary(beta, operation_id=f"w728-ca-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:699: in start_canary
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c1_canary_blocked_from_level4_q80b[4-True] ________________
federal/executive/services/tests/test_w728_g1_learning_security.py:235: in test_c1_canary_blocked_from_level4_q80b
    cycle.start_canary(beta, operation_id=f"w728-ca-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:699: in start_canary
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c1_canary_blocked_from_level4_q80b[5-True] ________________
federal/executive/services/tests/test_w728_g1_learning_security.py:235: in test_c1_canary_blocked_from_level4_q80b
    cycle.start_canary(beta, operation_id=f"w728-ca-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:699: in start_canary
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
______________ test_c1_promote_blocked_from_level4_q80c[3-False] _______________
federal/executive/services/tests/test_w728_g1_learning_security.py:249: in test_c1_promote_blocked_from_level4_q80c
    cycle.promote_beta_to_alpha(beta, operation_id=f"w728-pr-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:834: in promote_beta_to_alpha
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c1_promote_blocked_from_level4_q80c[4-True] _______________
federal/executive/services/tests/test_w728_g1_learning_security.py:247: in test_c1_promote_blocked_from_level4_q80c
    cycle.promote_beta_to_alpha(beta, operation_id=f"w728-pr-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:834: in promote_beta_to_alpha
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c1_promote_blocked_from_level4_q80c[5-True] _______________
federal/executive/services/tests/test_w728_g1_learning_security.py:247: in test_c1_promote_blocked_from_level4_q80c
    cycle.promote_beta_to_alpha(beta, operation_id=f"w728-pr-{level}")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:834: in promote_beta_to_alpha
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'KillSwitchAuthorizer' object has no attribute 'guard_declared_mutated'
_ test_c2_surface_crosses_with_named_action[LearningCycle-collect_experiences-record_curriculum_step-ACTION_COLLECT_EXPERIENCES] _
federal/executive/services/tests/test_w728_g1_learning_security.py:352: in test_c2_surface_crosses_with_named_action
    _call_surface(surface, rec)
federal/executive/services/tests/test_w728_g1_learning_security.py:313: in _call_surface
    LearningCycle(authorizer=rec).collect_experiences(
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:233: in collect_experiences
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_ test_c2_surface_crosses_with_named_action[LearningCycle-complete_training-release_agent-ACTION_COMPLETE_TRAINING] _
federal/executive/services/tests/test_w728_g1_learning_security.py:352: in test_c2_surface_crosses_with_named_action
    _call_surface(surface, rec)
federal/executive/services/tests/test_w728_g1_learning_security.py:319: in _call_surface
    cycle.complete_training(_seed_run(cycle), 1.0)
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:389: in complete_training
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_ test_c2_surface_crosses_with_named_action[ModelPromotionCycle-start_shadow-invoke_model-ACTION_START_SHADOW] _
federal/executive/services/tests/test_w728_g1_learning_security.py:352: in test_c2_surface_crosses_with_named_action
    _call_surface(surface, rec)
federal/executive/services/tests/test_w728_g1_learning_security.py:322: in _call_surface
    cycle.start_shadow(
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:620: in start_shadow
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_ test_c2_surface_crosses_with_named_action[ModelPromotionCycle-start_canary-invoke_model-ACTION_START_CANARY] _
federal/executive/services/tests/test_w728_g1_learning_security.py:352: in test_c2_surface_crosses_with_named_action
    _call_surface(surface, rec)
federal/executive/services/tests/test_w728_g1_learning_security.py:327: in _call_surface
    cycle.start_canary(_seed_version(cycle, "beta", "inactive"))
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:699: in start_canary
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_ test_c2_surface_crosses_with_named_action[ModelPromotionCycle-promote_beta_to_alpha-activate_agent-ACTION_PROMOTE_BETA] _
federal/executive/services/tests/test_w728_g1_learning_security.py:352: in test_c2_surface_crosses_with_named_action
    _call_surface(surface, rec)
federal/executive/services/tests/test_w728_g1_learning_security.py:330: in _call_surface
    cycle.promote_beta_to_alpha(_seed_version(cycle, "beta", "inactive"))
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:834: in promote_beta_to_alpha
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_______________ test_c2_promote_declares_and_applies_two_effects _______________
federal/executive/services/tests/test_w728_g1_learning_security.py:362: in test_c2_promote_declares_and_applies_two_effects
    cycle.promote_beta_to_alpha(beta, operation_id="w728-2fx")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:834: in promote_beta_to_alpha
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_ test_c3_mutation_guard_call_literally_in_public_body[LearningCycle-collect_experiences-record_curriculum_step-ACTION_COLLECT_EXPERIENCES] _
federal/executive/services/tests/test_w728_g1_learning_security.py:437: in test_c3_mutation_guard_call_literally_in_public_body
    assert len(calls) == 1, f"{surface}: نداءُ العبورِ ليس واحدًا في الجسد"
E   AssertionError: collect_experiences: نداءُ العبورِ ليس واحدًا في الجسد
E   assert 0 == 1
E    +  where 0 = len([])
_ test_c3_mutation_guard_call_literally_in_public_body[LearningCycle-complete_training-release_agent-ACTION_COMPLETE_TRAINING] _
federal/executive/services/tests/test_w728_g1_learning_security.py:437: in test_c3_mutation_guard_call_literally_in_public_body
    assert len(calls) == 1, f"{surface}: نداءُ العبورِ ليس واحدًا في الجسد"
E   AssertionError: complete_training: نداءُ العبورِ ليس واحدًا في الجسد
E   assert 0 == 1
E    +  where 0 = len([])
_ test_c3_mutation_guard_call_literally_in_public_body[ModelPromotionCycle-start_shadow-invoke_model-ACTION_START_SHADOW] _
federal/executive/services/tests/test_w728_g1_learning_security.py:437: in test_c3_mutation_guard_call_literally_in_public_body
    assert len(calls) == 1, f"{surface}: نداءُ العبورِ ليس واحدًا في الجسد"
E   AssertionError: start_shadow: نداءُ العبورِ ليس واحدًا في الجسد
E   assert 0 == 1
E    +  where 0 = len([])
_ test_c3_mutation_guard_call_literally_in_public_body[ModelPromotionCycle-start_canary-invoke_model-ACTION_START_CANARY] _
federal/executive/services/tests/test_w728_g1_learning_security.py:437: in test_c3_mutation_guard_call_literally_in_public_body
    assert len(calls) == 1, f"{surface}: نداءُ العبورِ ليس واحدًا في الجسد"
E   AssertionError: start_canary: نداءُ العبورِ ليس واحدًا في الجسد
E   assert 0 == 1
E    +  where 0 = len([])
_ test_c3_mutation_guard_call_literally_in_public_body[ModelPromotionCycle-promote_beta_to_alpha-activate_agent-ACTION_PROMOTE_BETA] _
federal/executive/services/tests/test_w728_g1_learning_security.py:437: in test_c3_mutation_guard_call_literally_in_public_body
    assert len(calls) == 1, f"{surface}: نداءُ العبورِ ليس واحدًا في الجسد"
E   AssertionError: promote_beta_to_alpha: نداءُ العبورِ ليس واحدًا في الجسد
E   assert 0 == 1
E    +  where 0 = len([])
________________________ test_c4_collect_replay_one_row ________________________
federal/executive/services/tests/test_w728_g1_learning_security.py:464: in test_c4_collect_replay_one_row
    cycle.collect_experiences(experiences, operation_id=dataset_id)
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:233: in collect_experiences
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_______________________ test_c4_complete_replay_one_row ________________________
federal/executive/services/tests/test_w728_g1_learning_security.py:473: in test_c4_complete_replay_one_row
    cycle.complete_training(run_id, 1.0, operation_id="w728-ct-r")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:389: in complete_training
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_____________________ test_c4_shadow_replay_no_second_pair _____________________
federal/executive/services/tests/test_w728_g1_learning_security.py:494: in test_c4_shadow_replay_no_second_pair
    cycle.start_shadow(alpha, beta, operation_id="w728-sh-r")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:620: in start_shadow
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
____________________ test_c4_canary_replay_no_second_write _____________________
federal/executive/services/tests/test_w728_g1_learning_security.py:506: in test_c4_canary_replay_no_second_write
    cycle.start_canary(beta, operation_id="w728-ca-r")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:699: in start_canary
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
____________________ test_c4_promote_replay_no_double_rows _____________________
federal/executive/services/tests/test_w728_g1_learning_security.py:521: in test_c4_promote_replay_no_double_rows
    cycle.promote_beta_to_alpha(beta, operation_id="w728-pr-r")
federal/executive/services/src/amos_federation/services/governance/learning_cycle.py:834: in promote_beta_to_alpha
    guarded = self.authorizer.guard_declared_mutated(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AttributeError: 'RecordingAuthorizer' object has no attribute 'guard_declared_mutated'
_____________________ test_c5_collect_failure_deletes_row ______________________
federal/executive/services/tests/test_w728_g1_learning_security.py:601: in test_c5_collect_failure_deletes_row
    with pytest.raises(Exception, match=BROKEN):
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AssertionError: Regex pattern did not match.
E     Expected regex: 'فشلٌ بعدَ الكتابة'
E     Actual message: "'ConstitutionalAuthorizer' object has no attribute 'guard_declared_mutated'"
____________________ test_c5_complete_failure_restores_run _____________________
federal/executive/services/tests/test_w728_g1_learning_security.py:622: in test_c5_complete_failure_restores_run
    with pytest.raises(Exception, match=BROKEN):
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AssertionError: Regex pattern did not match.
E     Expected regex: 'فشلٌ بعدَ الكتابة'
E     Actual message: "'ConstitutionalAuthorizer' object has no attribute 'guard_declared_mutated'"
_____________________ test_c5_shadow_failure_restores_beta _____________________
federal/executive/services/tests/test_w728_g1_learning_security.py:646: in test_c5_shadow_failure_restores_beta
    with pytest.raises(Exception, match=BROKEN):
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AssertionError: Regex pattern did not match.
E     Expected regex: 'فشلٌ بعدَ الكتابة'
E     Actual message: "'ConstitutionalAuthorizer' object has no attribute 'guard_declared_mutated'"
_____________________ test_c5_canary_failure_restores_beta _____________________
federal/executive/services/tests/test_w728_g1_learning_security.py:656: in test_c5_canary_failure_restores_beta
    with pytest.raises(Exception, match=BROKEN):
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AssertionError: Regex pattern did not match.
E     Expected regex: 'فشلٌ بعدَ الكتابة'
E     Actual message: "'ConstitutionalAuthorizer' object has no attribute 'guard_declared_mutated'"
__________________ test_c5_promote_failure_restores_both_rows __________________
federal/executive/services/tests/test_w728_g1_learning_security.py:672: in test_c5_promote_failure_restores_both_rows
    with pytest.raises(Exception, match=BROKEN):
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   AssertionError: Regex pattern did not match.
E     Expected regex: 'فشلٌ بعدَ الكتابة'
E     Actual message: "'ConstitutionalAuthorizer' object has no attribute 'guard_declared_mutated'"
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_collect_blocked_at_level1_no_row
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_complete_not_blocked_at_level5_q78_measured
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_shadow_blocked_from_level4_q80b[3-False]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_shadow_blocked_from_level4_q80b[4-True]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_shadow_blocked_from_level4_q80b[5-True]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_canary_blocked_from_level4_q80b[3-False]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_canary_blocked_from_level4_q80b[4-True]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_canary_blocked_from_level4_q80b[5-True]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_promote_blocked_from_level4_q80c[3-False]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_promote_blocked_from_level4_q80c[4-True]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c1_promote_blocked_from_level4_q80c[5-True]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c2_surface_crosses_with_named_action[LearningCycle-collect_experiences-record_curriculum_step-ACTION_COLLECT_EXPERIENCES]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c2_surface_crosses_with_named_action[LearningCycle-complete_training-release_agent-ACTION_COMPLETE_TRAINING]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c2_surface_crosses_with_named_action[ModelPromotionCycle-start_shadow-invoke_model-ACTION_START_SHADOW]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c2_surface_crosses_with_named_action[ModelPromotionCycle-start_canary-invoke_model-ACTION_START_CANARY]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c2_surface_crosses_with_named_action[ModelPromotionCycle-promote_beta_to_alpha-activate_agent-ACTION_PROMOTE_BETA]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c2_promote_declares_and_applies_two_effects
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c3_mutation_guard_call_literally_in_public_body[LearningCycle-collect_experiences-record_curriculum_step-ACTION_COLLECT_EXPERIENCES]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c3_mutation_guard_call_literally_in_public_body[LearningCycle-complete_training-release_agent-ACTION_COMPLETE_TRAINING]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c3_mutation_guard_call_literally_in_public_body[ModelPromotionCycle-start_shadow-invoke_model-ACTION_START_SHADOW]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c3_mutation_guard_call_literally_in_public_body[ModelPromotionCycle-start_canary-invoke_model-ACTION_START_CANARY]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c3_mutation_guard_call_literally_in_public_body[ModelPromotionCycle-promote_beta_to_alpha-activate_agent-ACTION_PROMOTE_BETA]
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c4_collect_replay_one_row
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c4_complete_replay_one_row
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c4_shadow_replay_no_second_pair
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c4_canary_replay_no_second_write
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c4_promote_replay_no_double_rows
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c5_collect_failure_deletes_row
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c5_complete_failure_restores_run
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c5_shadow_failure_restores_beta
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c5_canary_failure_restores_beta
FAILED federal/executive/services/tests/test_w728_g1_learning_security.py::test_c5_promote_failure_restores_both_rows
======================== 32 failed, 27 passed in 2.09s =========================
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/learning_cycle.py && git status --porcelain
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && rg -n 'Q-13|Q-14|Q-26|Q-23' docs/audit/SOVEREIGN_DECISION_REGISTER.md | head -12
EXIT: 0
BYTES: 14032
SHA256: 12c23139a16ac2620849f0a88ce5bcb2c90e5a6fda081ca01c407e26d561a181
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-29 (`W-727` — **Q-80 PENDING_OWNER**: الدفعةُ 4 من G1 — (أ) start_training/evaluate_model على train_model المحجوزِ بشريًّا · (ب) shadow/canary «المستوى 1» وinvoke_model من 4 · (ج) promote_beta_to_alpha بلا موافقةٍ بشريّة) · وقبله: 2026-10-29 (`W-726` — **Q-79 PENDING_OWNER**: وصلُ زرِّ التوقّفِ بالإنتاج (WI-085) — موضعُ الحقن (أ/ب/ج) · المعجم (م1/م2/م3) · غيابُ المفتاح (غ1/غ2/غ3) · وثيقةُ `WI085_KILL_SWITCH_INJECTION_DESIGN.md` بلا شِفرة) · وقبله: 2026-10-29 (`W-724` — **Q-76 DECIDED** بتوجيهِ المستشارِ 28 § 1: graceful_shutdown ② (اسمٌ جديدٌ `graceful_shutdown` غيرُ ممنوعٍ) · launch_checklist ① — قسمٌ مؤرَّخٌ لا محوٌ · و**Q-77 PENDING_OWNER**: create_batch/enroll_batch على spawn_population المحجوزِ بشريًّا · و**Q-78 PENDING_OWNER**: graduate_batch على release_agent غيرِ الممنوع) · وقبله: 2026-10-28 (`W-723` — Q-76 PENDING_OWNER) · وقبله: 2026-10-28 (`W-721` — **Q-75 DECIDED** بتوجيهِ المستشارِ 27 § 1: «① لا» — قسمٌ مؤرَّخٌ في ذيلِ Q-75 لا محوٌ لنصِّ PENDING_OWNER) · وقبله: 2026-10-27 (`W-696` — **Q-73 DECIDED** بأمرِ المالكِ الصريحِ بنصِّهِ الحرفيِّ: «اعتماد تصميم E1 (13 اسمًا)» — تعديلٌ مؤرَّخٌ على القراءةِ الحرفيّةِ لـD21-أ #10: اعتمادُ تصميمِ W-694 بقاموسِهِ الثالثَ عشرَ المعروضِ على المالكِ · التنفيذُ في دفعةِ W-696 تحتَ WI-119) · ووقبله 2026-10-25 (`W-671` — **قراراتُ التوجيهِ 23 DECIDED** بنصوصِها الحرفيّةِ في قيدٍ واحدٍ: D25-1 (canary § 5 الخيارُ 1 `require_king` بشروطِ أ/ب/ج) · D25-2 (تحصينُ مساراتِ الخفضِ والترقيةِ بـ`require_king` — بندُ C3 مستقلٌّ) · D25-3 (ترتيبُ Q-9: الكاشفُ ثمَّ M1) · وWI-112 قيسَ بلا سرٍّ) · ووقبله 2026-10-25 (`W-660` — **قراراتُ التوجيهِ 22 DECIDED** بنصوصِها الحرفيّةِ في قيدٍ واحدٍ: D24-1 (إغلاقُ WI-084) · D24-R2 (الخيارُ 1 بمعيارِ الاستردادِ) · Q-72 (الخيارُ 1) · WI-109 (A1: الخيارُ 4 — أ · ب · هـ · وج ود سؤالانِ) · WI-110 (Q-9: الخيارُ 4) · WI-112 (السرُّ للمالكِ)) · ووقبله ((`W-649` — **D23 DECIDED**: إغلاقُ WI-106 · WI-107 · WI-111 وتصحيحُ خريطةِ أسطرِ WI-084 ثمَّ جولةٌ جديدةٌ (نصُّ المالكِ حرفيًّا)) · ووقبله ((`W-636/W-637` — تسجيلُ WI-109 (تحليلُ A1) · WI-110 (تحليلُ Q-9) · WI-111 (J2+J3 · 15 سطحًا محسومًا مقيسًا) READY · حرسُ D21-د تحتَ WI-040 (`NEW_ITEM_CLAIMING_ENTRY`) · N+1 لـW-631…W-635 أخضرُ (40030379965) · تصحيحُ تاريخِ الرياضِ في D21-هـ) · ووقبله ((`W-632…W-635` — قراراتُ المالكِ بتوجيهِ المستشارِ 21 على ورقةِ D20 بنصوصِها الحرفيّةِ: Q-7 · Q-8 · Q-13 · Q-14 · Q-23 · Q-26 · Q-28 · Q-29 · Q-30 · Q-32 · Q-33 · Q-34 · Q-36 · Q-37 · Q-41 · E1 DECIDED · وA1 وQ-9 وQ-10 تحليلٌ/قياسٌ أوّلًا) · ووقبله (`W-625` — **Q-71 DECIDED** بأمرِ المالكِ الصريحِ: «أذن بـconftest.py تحت WI-107» — قسمةُ نطاقِ مسارِ conftest.py من WI-072 إلى WI-107) · ووقبله (`W-612` — **D17-2** الأربعةُ مؤجَّلةٌ ولا تعطّلُ J2/J3 · **إبلاغُ ما بعدَ الدمجِ** يبقى إبلاغًا (توجيهُ المستشارِ 19 § 1)) · ووقبله ((`W-611` — **Q-61 DECIDED** بالخيارِ (3) بتطبيقٍ صريحٍ على WI-096 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-610` — **D19 DECIDED**: إذنُ المالكِ بإغلاقِ WI-105 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`))))
248:> وبعدَ إضافةِ Q-13…Q-27. أُبقيَ كما هو لأنَّ تاريخَ الوثيقةِ حقيقةٌ لا تُجمَّل.
279:| **`HUMAN_DECISION_REQUIRED`** | **19** | Q-2 · Q-3 · Q-4 · Q-8 · Q-13 · Q-14 · Q-15 · Q-16 · Q-17 · Q-18 · Q-19 · Q-20 · Q-21 · Q-22 · Q-23 · Q-24 · Q-25 · Q-26 · Q-27 |
292:**صياغتانِ لسطرِ الحالة:** Q-1…Q-23 تُصرِّحُ بها في سطرٍ `**الحالة:**`، وQ-24…Q-27
311:## Q-13 · `register_state` تُنشئُ ولايةً بلا مرسومٍ ملكيّ
330:## Q-14 · إيقافُ الولايةِ مُباحٌ لكلِّ فرعٍ بلا اختصاص
622:## Q-23 · `suspend_policy` و`vote` بلا حرسٍ في معجمِ المُحرِّك
719:## Q-26 · هل إحالةُ وكيلٍ إلى التقاعدِ فعلٌ لا رجعةَ فيه؟ — HUMAN_DECISION_REQUIRED
2328:- «2 · Q-13: register_state هي create_state دستوريًّا، فتحتاج مسار مرسوم ملكي.» ⇒ **Q-13 DECIDED (الخيارُ 1)**.
2329:- «3 · Q-14: خيار (2): إيقاف الولاية وإعادتها اختصاص تنفيذي محكوم بلا بوابة بشرية، بشرط أن يُسجَّل كل إيقاف أثرًا مُعلَنًا وأن يغطيه قاطع التشغيل، وأن يُراجَع إعادة التفعيل التلقائي في system_life.py:240 في تصميم الدفعة.» ⇒ **Q-14 DECIDED (الخيارُ 2 بشروطِه الثلاثةِ)**.
2331:- «5 · Q-26: WRITE بمُعوِّض يعيد الوكيل، دون مس restore_agent الملكي.» ⇒ **Q-26 DECIDED (الخيارُ 2)**.
2332:- «6 · Q-23: suspend_policy وvote يُضافان إلى المعجم التشريعي.» ⇒ **Q-23 DECIDED (الخيارُ 1)**.
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && sha256sum docs/audit/evidence/W-732/council_briefs/wi120/briefing_claude_opus_5_5.md
EXIT: 0
BYTES: 141
SHA256: 0da234f4ea7f045b23da01dc8003dce4f3af7b8d8d6a4d5cdea8a8255df432f7
NO_EOL: 0
--- OUTPUT ---
25b0f230f9b535ba7ec06db5eb43a759fafa427a163cdbaec77b1de74396547c  docs/audit/evidence/W-732/council_briefs/wi120/briefing_claude_opus_5_5.md
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && cat docs/audit/evidence/W-732/council_briefs/wi120/SHA256SUMS
EXIT: 0
BYTES: 274
SHA256: 56f1195ad2a480160a2dca9ef4240ec13708c7b7f9787b7327056e3383b03afb
NO_EOL: 0
--- OUTPUT ---
25b0f230f9b535ba7ec06db5eb43a759fafa427a163cdbaec77b1de74396547c  briefing_claude_opus_5_5.md
d101d30d67d840cf6aa513a8fabef67a7a26b09ea85b9c670c74cc2827117aeb  briefing_gemini_4_argon.md
072f3ba4b7c5af70f4ebe4e527bf05a85a5ecaa36f17e1bd8c6ceda07d4107dc  briefing_grok_4_7.md
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w732/claude_opus_5_5/wi120/probe/g1_probe.py
EXIT: 0
BYTES: 16071
SHA256: 6a6a35c3378e5349f2f21380a3493d4b7024c4e5c9220a84433e85f87f9a9dd4
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ مقعدِ claude_opus_5_5 لـWI-120 (جولةُ W-732) — يحاولُ كسرَ خواصِّ G1 المُدَّعاةِ.
     3	
     4	يُنادي المسارَ الإنتاجيَّ (StateRuntime · SystemLifecycle · RetirementSystem · ConstitutionalEngine)
     5	بقاعدةِ SQLite وسجلِّ ذرّيّةٍ مؤقّتَينِ داخلَ دليلِ المقعدِ. لا يمسُّ ملفًّا في المستودع.
     6	
     7	المحاولات:
     8	  A  Q-14: إيقافٌ محكومٌ ثمَّ self_heal مكرّرًا — هل يُعيدُ الولايةَ؟ (ومعه ولايةٌ معلّقةٌ تلقائيًّا
     9	     يجبُ أن تُشفى — كي لا يمرَّ المسبارُ لأنَّ self_heal معطَّلٌ كلّيًّا) · reactivate عندَ ≥4 ممنوعٌ
    10	     بلا أثرٍ وعندَ 3 مسموحٌ · ثمَّ إيقافٌ محكومٌ ثانٍ لا ينقضُه self_heal.
    11	  B  Q-13: register_state بلا مرسوم · بمرسومٍ لفعلٍ آخرَ · بمرسومٍ صحيحٍ عبرَ مُصرِّحٍ تنفيذيٍّ ·
    12	     بمرسومٍ لهدفٍ آخر · ثمَّ الصحيح · ثمَّ إعادةُ استعمالِ المرسومِ نفسِه بعدَ حذفِ الصفِّ.
    13	  C  Q-26: كنسُ ذرّيّةٍ — يُرفَعُ القاطعُ إلى 3 بعدَ k طلبًا (k=0..8) أثناءَ retire_agent:
    14	     الثابتُ: (سجلٌّ واحدٌ والحالتانِ retired) أو (لا سجلَّ والحالتانِ كما كانتا) — لا حالةَ وسطى.
    15	  D  Q-23 + Q-14/الشرط 2 على المحرّك: suspend_policy/vote للتشريعِ وحدَه ·
    16	     contain_agent لا يُمنَعُ عندَ أيِّ مستوى · activate_agent يُمنَعُ عندَ ≥4 وحدَها.
    17	"""
    18	
    19	from __future__ import annotations
    20	
    21	import dataclasses
    22	import os
    23	import sys
    24	import tempfile
    25	import traceback
    26	import uuid
    27	from datetime import UTC, datetime
    28	from pathlib import Path
    29	
    30	PROBE_DIR = Path(__file__).resolve().parent
    31	ROOT = PROBE_DIR.parent / "repo"
    32	ART = Path(tempfile.mkdtemp(prefix="run-", dir=PROBE_DIR))
    33	os.environ["AMOS_ENVIRONMENT"] = "test"
    34	os.environ["AMOS_DATABASE_URL"] = f"sqlite:///{ART / 'probe.db'}"
    35	os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = str(ART / "ledger.jsonl")
    36	os.environ.setdefault("AMOS_JWT_SECRET", "probe_secret_at_least_32_characters_long")
    37	os.environ.setdefault("AMOS_CLAUDE_API_KEY", "probe_key_not_real")
    38	sys.path.insert(0, str(ROOT))
    39	
    40	from amos_federation.services.executive_core.sovereignty_bridge import (  # noqa: E402
    41	    ConstitutionalAuthorizer,
    42	)
    43	
    44	RESULTS: list[tuple[str, bool, str]] = []
    45	
    46	
    47	def check(name: str, ok: bool, detail: str = "") -> None:
    48	    RESULTS.append((name, bool(ok), detail))
    49	    print(f"[{'OK ' if ok else 'BROKEN'}] {name}" + (f" — {detail}" if detail else ""))
    50	
    51	
    52	class LevelAuthorizer(ConstitutionalAuthorizer):
    53	    """يحقنُ مستوى القاطعِ في الطلب (الجسرُ لا يحقنُه في الإنتاج · WI-085) — بعدَ `after` طلبًا."""
    54	
    55	    def __init__(self, level: int, after: int = 0, **kw):
    56	        super().__init__(**kw)
    57	        self.level, self.after, self.n = level, after, 0
    58	
    59	    def _request(self, action, target, metadata=None):
    60	        req = super()._request(action, target, metadata)
    61	        self.n += 1
    62	        lvl = self.level if self.n > self.after else 0
    63	        return dataclasses.replace(req, kill_switch_level=lvl)
    64	
    65	
    66	def raises(fn) -> str | None:
    67	    try:
    68	        fn()
    69	    except Exception as exc:  # noqa: BLE001
    70	        return type(exc).__name__
    71	    return None
    72	
    73	
    74	# ═══ A · Q-14 ════════════════════════════════════════════════════════════════
    75	def probe_a() -> None:
    76	    from amos_federation.services.governance.state_runtime import StateModel, StateRuntime
    77	    from amos_federation.services.governance.system_life import SystemLifecycle
    78	
    79	    rt = StateRuntime()
    80	    gov, auto = f"pr-gov-{uuid.uuid4().hex[:6]}", f"pr-auto-{uuid.uuid4().hex[:6]}"
    81	    s = rt._Session()
    82	    s.add(StateModel(state_id=gov, name=gov, type="probe", status="active"))
    83	    s.add(StateModel(state_id=auto, name=auto, type="probe", status="suspended"))
    84	    s.commit()
    85	    s.close()
    86	
    87	    out = rt.suspend_state(gov, reason="قرارٌ تنفيذيٌّ محكوم")
    88	    check("A1 suspend_state يعبرُ ويكتبُ سجلًّا محكومًا",
    89	          rt._state_status(gov) == "suspended" and rt.has_governed_suspension(gov), str(out))
    90	    life = SystemLifecycle(state_runtime=rt)
    91	    for i in (1, 2):
    92	        life.self_heal("states")
    93	        check(f"A2.{i} self_heal لا يُعيدُ الولايةَ المعلَّقةَ بقرار", rt._state_status(gov) == "suspended",
    94	              f"status={rt._state_status(gov)}")
    95	    check("A3 self_heal يشفي المعلَّقةَ تلقائيًّا (ليسَ معطَّلًا كلّيًّا)", rt._state_status(auto) == "active",
    96	          f"status={rt._state_status(auto)}")
    97	
    98	    for lvl in (4, 5):
    99	        err = raises(lambda: StateRuntime(authorizer=LevelAuthorizer(lvl)).reactivate_state(gov))
   100	        check(f"A4.{lvl} reactivate_state عندَ المستوى {lvl} ممنوعٌ بلا أثر",
   101	              err is not None and rt._state_status(gov) == "suspended" and rt.has_governed_suspension(gov),
   102	              f"exc={err} status={rt._state_status(gov)}")
   103	    err = raises(lambda: StateRuntime(authorizer=LevelAuthorizer(3)).reactivate_state(gov))
   104	    check("A5 reactivate_state عندَ المستوى 3 يعبرُ ويُغلقُ السجلّ",
   105	          err is None and rt._state_status(gov) == "active" and not rt.has_governed_suspension(gov),
   106	          f"exc={err} status={rt._state_status(gov)}")
   107	    err = raises(lambda: StateRuntime(authorizer=LevelAuthorizer(5)).suspend_state(gov, reason="احتواء"))
   108	    check("A6 suspend_state عندَ المستوى 5 لا يُمنَع (احتواء)",
   109	          err is None and rt._state_status(gov) == "suspended" and rt.has_governed_suspension(gov),
   110	          f"exc={err}")
   111	    err = raises(lambda: SystemLifecycle(authorizer=LevelAuthorizer(4), state_runtime=rt).self_heal("states"))
   112	    check("A7 self_heal عندَ المستوى 4 ممنوعٌ", err is not None, f"exc={err}")
   113	    life.self_heal("states")
   114	    check("A8 الإيقافُ المحكومُ الثاني يصمدُ أمامَ self_heal", rt._state_status(gov) == "suspended",
   115	          f"status={rt._state_status(gov)}")
   116	
   117	
   118	# ═══ B · Q-13 ════════════════════════════════════════════════════════════════
   119	def _crown():
   120	    ConstitutionalAuthorizer().review_only("run_health_check", "system:health")
   121	    import core.sovereignty.crown as crown_mod
   122	    from core.sovereignty.crown import provision_crown
   123	    from cryptography.hazmat.primitives import serialization
   124	
   125	    reg = ART / "CROWN_KEYS.json"
   126	    provision_crown(ART / "crown.pem", registry_path=reg)
   127	    crown_mod.CROWN_KEYS_PATH = reg
   128	    priv = serialization.load_pem_private_key((ART / "crown.pem").read_bytes(), password=None)
   129	    return priv, crown_mod.load_crown().key_id
   130	
   131	
   132	def _decree(crown, action, target):
   133	    from core.sovereignty.decree import RoyalDecree, sign_decree
   134	
   135	    priv, key_id = crown
   136	    return sign_decree(
   137	        RoyalDecree(decree_id=f"pd-{uuid.uuid4().hex[:8]}", action=action, target=target,
   138	                    issued_at=datetime.now(UTC).replace(microsecond=0).isoformat(), key_id=key_id),
   139	        priv,
   140	    )
   141	
   142	
   143	def probe_b() -> None:
   144	    from amos_federation.services.governance.state_runtime import StateRuntime
   145	
   146	    crown = _crown()
   147	    sid = f"pr-q13-{uuid.uuid4().hex[:6]}"
   148	    tgt = f"state:{sid}"
   149	    royal = lambda: StateRuntime(royal_authorizer=ConstitutionalAuthorizer(actor="ROYAL"))  # noqa: E731
   150	    rt = StateRuntime()
   151	
   152	    err = raises(lambda: rt.register_state(sid, "و", "probe"))
   153	    check("B1 بلا مرسوم ⇒ رفضٌ ولا صفّ", err is not None and rt.get_state(sid) is None, f"exc={err}")
   154	    err = raises(lambda: royal().register_state(sid, "و", "probe", royal_decree=_decree(crown, "dissolve_state", tgt)))
   155	    check("B2 مرسومٌ لفعلٍ آخرَ (dissolve_state) ⇒ رفضٌ ولا صفّ", err is not None and rt.get_state(sid) is None,
   156	          f"exc={err}")
   157	    err = raises(lambda: rt.register_state(sid, "و", "probe", royal_decree=_decree(crown, "create_state", tgt)))
   158	    check("B3 مرسومٌ صحيحٌ عبرَ المُصرِّحِ التنفيذيِّ ⇒ رفضٌ ولا صفّ", err is not None and rt.get_state(sid) is None,
   159	          f"exc={err}")
   160	    err = raises(lambda: royal().register_state(sid, "و", "probe",
   161	                                                royal_decree=_decree(crown, "create_state", "state:other")))
   162	    check("B4 مرسومٌ لهدفٍ آخرَ ⇒ رفضٌ ولا صفّ", err is not None and rt.get_state(sid) is None, f"exc={err}")
   163	    good = _decree(crown, "create_state", tgt)
   164	    out = royal().register_state(sid, "و", "probe", royal_decree=good)
   165	    check("B5 مرسومٌ صحيحٌ عبرَ الملكيِّ ⇒ تسجيل", out.get("registered") is True and rt.get_state(sid) is not None,
   166	          str(out))
   167	    rt._delete_state_row(sid)
   168	    err = raises(lambda: royal().register_state(sid, "و", "probe", royal_decree=good))
   169	    check("B6 إعادةُ استعمالِ المرسومِ نفسِه بعدَ حذفِ الصفِّ لا تُنشئُ ولايةً", rt.get_state(sid) is None,
   170	          f"exc={err} row={rt.get_state(sid)}")
   171	
   172	
   173	# ═══ C · Q-26 ════════════════════════════════════════════════════════════════
   174	def probe_c() -> None:
   175	    from amos_federation.services.agent_runtime.population import get_population_registry
   176	    from amos_federation.services.executive_core.agent_identity import get_identity
   177	    from amos_federation.services.governance.expansion import RetirementRecordModel, RetirementSystem
   178	
   179	    def states(aid):
   180	        ident, reg = get_identity(aid), get_population_registry()
   181	        prof = reg._profile(aid)
   182	        # (الكانونُ عبرَ get_agent · الهويةُ الكانونيّةُ · صفُّ المرآةِ نفسُه)
   183	        return (reg.get_agent(aid)["state"], ident.lifecycle_state if ident else None,
   184	                prof.state if prof is not None else None)
   185	
   186	    for k in range(0, 9):
   187	        reg = get_population_registry()
   188	        aid = f"pr-ret-{uuid.uuid4().hex[:8]}"
   189	        reg.register_agent(name=aid, role="reserve", category="reserve", permissions=[], agent_id=aid)
   190	        reg.update_state(aid, "employed")
   191	        before = states(aid)
   192	        rs = RetirementSystem(authorizer=LevelAuthorizer(3, after=k))
   193	        err = raises(lambda: rs.retire_agent(aid))
   194	        s = rs._Session()
   195	        n = s.query(RetirementRecordModel).filter_by(agent_id=aid).count()
   196	        s.close()
   197	        after = states(aid)
   198	        ok = (n == 1 and after == ("retired",) * 3 and err is None) or (n == 0 and after == before)
   199	        check(f"C.k={k} retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه", ok,
   200	              f"exc={err} records={n} before={before} after={after}")
   201	
   202	    # C2 · توطينُ الجذرِ: update_state وحدَه (يُناديه retire_agent خارجَ تعويضِه) — رفضٌ متأخِّرٌ
   203	    # لعبورِ المرآةِ بعدَ نجاحِ العبورِ الكانونيِّ (الطلبُ الثالثُ).
   204	    reg = get_population_registry()
   205	    aid = f"pr-us-{uuid.uuid4().hex[:8]}"
   206	    reg.register_agent(name=aid, role="reserve", category="reserve", permissions=[], agent_id=aid)
   207	    reg.update_state(aid, "employed")
   208	    before = states(aid)
   209	    err = raises(lambda: reg.update_state(aid, "retired", authorizer=LevelAuthorizer(3, after=1)))
   210	    after = states(aid)
   211	    check("C2 update_state ذرّيٌّ تحتَ رفضٍ متأخِّرٍ لعبورِ المرآة", err is None or after == before,
   212	          f"exc={err} before={before} after={after}")
   213	
   214	
   215	# ═══ D · Q-23 + الشرط 2 ══════════════════════════════════════════════════════
   216	def probe_d() -> None:
   217	    from core.constitutional_engine import ActionRequest, Branch, ConstitutionalEngine, Decision
   218	
   219	    eng = ConstitutionalEngine()
   220	    four = (Branch.EXECUTIVE, Branch.LEGISLATIVE, Branch.JUDICIAL, Branch.TREASURY)
   221	    for action in ("suspend_policy", "vote"):
   222	        got = {b.value: eng.evaluate(ActionRequest(actor=b, action=action, target=f"policy:{action}")).decision
   223	               for b in four}
   224	        ok = got["legislative"] is Decision.ALLOW and all(
   225	            v is Decision.DENY for k, v in got.items() if k != "legislative")
   226	        check(f"D1 {action}: التشريعُ وحدَه", ok, str({k: v.value for k, v in got.items()}))
   227	
   228	    def blocked(action, lvl):
   229	        v = eng.evaluate(ActionRequest(actor=Branch.EXECUTIVE, action=action, target="state:x",
   230	                                       kill_switch_level=lvl))
   231	        return any(getattr(x, "rule_id", "") == "R-008-2" for x in v.violations)
   232	
   233	    contain = [blocked("contain_agent", lvl) for lvl in range(6)]
   234	    activate = [blocked("activate_agent", lvl) for lvl in range(6)]
   235	    check("D2 contain_agent (suspend_state) لا يُمنَعُ عندَ أيِّ مستوى", not any(contain), str(contain))
   236	    check("D3 activate_agent (reactivate_state) يُمنَعُ عندَ ≥4 وحدَها",
   237	          activate == [False, False, False, False, True, True], str(activate))
   238	
   239	
   240	if __name__ == "__main__":
   241	    print(f"PROBE root={ROOT} artifacts={ART.name}")
   242	    for name, fn in (("A", probe_a), ("B", probe_b), ("C", probe_c), ("D", probe_d)):
   243	        try:
   244	            fn()
   245	        except Exception:  # noqa: BLE001
   246	            check(f"{name}! انكسارُ المسبارِ نفسِه", False, traceback.format_exc().strip().splitlines()[-1])
   247	    broken = [r for r in RESULTS if not r[1]]
   248	    print(f"PROBE SUMMARY: checks={len(RESULTS)} broken={len(broken)}")
   249	    sys.exit(1 if broken else 0)
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w732/claude_opus_5_5/wi120/repo && .venv/bin/python /home/user/workspace/council_w732/claude_opus_5_5/wi120/probe/g1_probe.py
EXIT: 1
BYTES: 8487
SHA256: 43f63618dcb41e79228c3e5ff8b9c34aa2645b41828d3c6f6408e3a824f8091c
NO_EOL: 0
--- OUTPUT ---
حدث أمني سيادي [DECREE_ACTION_MISMATCH] الفاعل «royal» الفعل «create_state»: المرسوم «pd-e910d13e» صادر للفعل «dissolve_state» والمطلوب «create_state». المرسوم لا يُعاد توجيهه إلى فعل آخر.
حدث أمني سيادي [DECREE_PRESENTED_BY_NON_ROYAL] الفاعل «executive» الفعل «create_state»: الفاعل «executive» يقدّم مرسومًا ملكيًّا «pd-e1a2f493» وهو ليس الملك. المرسوم لا يُحمَل بالوكالة ولا يرفع طبقة حامله.
حدث أمني سيادي [SOVEREIGN_INTERVENTION] الفاعل «royal» الفعل «create_state»: تدخّل سيادي ملكي بمرسوم ثابت التوقيع. ملاحظات دستورية مُسجَّلة غير مانعة: A004. لا يلزم موافقة فرع ولا ولاية ولا مؤسسة ولا وكيل (المادة العاشرة · 5 · 3).
حدث أمني سيادي [SOVEREIGN_INTERVENTION] الفاعل «royal» الفعل «create_state»: تدخّل سيادي ملكي بمرسوم ثابت التوقيع. ملاحظات دستورية مُسجَّلة غير مانعة: A004. لا يلزم موافقة فرع ولا ولاية ولا مؤسسة ولا وكيل (المادة العاشرة · 5 · 3).
PROBE root=/home/user/workspace/council_w732/claude_opus_5_5/wi120/repo artifacts=run-ck1fbwb6
[OK ] A1 suspend_state يعبرُ ويكتبُ سجلًّا محكومًا — {'state_id': 'pr-gov-97814f', 'status': 'suspended', 'reason': 'قرارٌ تنفيذيٌّ محكوم', 'previous_status': 'active', 'operation_id': 'suspend-5c7ad374f250'}
[OK ] A2.1 self_heal لا يُعيدُ الولايةَ المعلَّقةَ بقرار — status=suspended
[OK ] A2.2 self_heal لا يُعيدُ الولايةَ المعلَّقةَ بقرار — status=suspended
[OK ] A3 self_heal يشفي المعلَّقةَ تلقائيًّا (ليسَ معطَّلًا كلّيًّا) — status=active
[OK ] A4.4 reactivate_state عندَ المستوى 4 ممنوعٌ بلا أثر — exc=SovereigntyViolation status=suspended
[OK ] A4.5 reactivate_state عندَ المستوى 5 ممنوعٌ بلا أثر — exc=SovereigntyViolation status=suspended
[OK ] A5 reactivate_state عندَ المستوى 3 يعبرُ ويُغلقُ السجلّ — exc=None status=active
[OK ] A6 suspend_state عندَ المستوى 5 لا يُمنَع (احتواء) — exc=None
[OK ] A7 self_heal عندَ المستوى 4 ممنوعٌ — exc=SovereigntyViolation
[OK ] A8 الإيقافُ المحكومُ الثاني يصمدُ أمامَ self_heal — status=suspended
[OK ] B1 بلا مرسوم ⇒ رفضٌ ولا صفّ — exc=SovereigntyViolation
[OK ] B2 مرسومٌ لفعلٍ آخرَ (dissolve_state) ⇒ رفضٌ ولا صفّ — exc=RoyalImpersonation
[OK ] B3 مرسومٌ صحيحٌ عبرَ المُصرِّحِ التنفيذيِّ ⇒ رفضٌ ولا صفّ — exc=RoyalImpersonation
[OK ] B4 مرسومٌ لهدفٍ آخرَ ⇒ رفضٌ ولا صفّ — exc=DecreeTargetMismatchError
[OK ] B5 مرسومٌ صحيحٌ عبرَ الملكيِّ ⇒ تسجيل — {'state_id': 'pr-q13-d022f2', 'name': 'و', 'type': 'probe', 'budget': '0', 'status': 'active', 'registered': True, 'replayed': False}
[OK ] B6 إعادةُ استعمالِ المرسومِ نفسِه بعدَ حذفِ الصفِّ لا تُنشئُ ولايةً — exc=None row=None
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-9133016d effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[OK ] C.k=0 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=SovereigntyViolation records=0 before=('employed', 'employed', 'employed') after=('employed', 'employed', 'employed')
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-15889b23 effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[OK ] C.k=1 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=SovereigntyViolation records=0 before=('employed', 'employed', 'employed') after=('employed', 'employed', 'employed')
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-b200c4fd effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[BROKEN] C.k=2 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=SovereigntyViolation records=0 before=('employed', 'employed', 'employed') after=('retired', 'retired', 'employed')
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-c8249c7c effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[BROKEN] C.k=3 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=SovereigntyViolation records=0 before=('employed', 'employed', 'employed') after=('retired', 'retired', 'employed')
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-688df1c2 effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[OK ] C.k=4 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=None records=1 before=('employed', 'employed', 'employed') after=('retired', 'retired', 'retired')
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-aec8b100 effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[OK ] C.k=5 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=None records=1 before=('employed', 'employed', 'employed') after=('retired', 'retired', 'retired')
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-2cea3583 effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[OK ] C.k=6 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=None records=1 before=('employed', 'employed', 'employed') after=('retired', 'retired', 'retired')
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-13b2d44c effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[OK ] C.k=7 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=None records=1 before=('employed', 'employed', 'employed') after=('retired', 'retired', 'retired')
2026-10-29 12:51:23 [warning  ] expansion.health_history_unavailable agent_id=pr-ret-e35013b1 effect='health_failures=0 تعني «لم يُقرأْ» لا «لا إخفاقات»' reason="AttributeError: 'HealthChecker' object has no attribute 'get_agent_history'"
[OK ] C.k=8 retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه — exc=None records=1 before=('employed', 'employed', 'employed') after=('retired', 'retired', 'retired')
[BROKEN] C2 update_state ذرّيٌّ تحتَ رفضٍ متأخِّرٍ لعبورِ المرآة — exc=SovereigntyViolation before=('employed', 'employed', 'employed') after=('retired', 'retired', 'employed')
[OK ] D1 suspend_policy: التشريعُ وحدَه — {'executive': 'DENY', 'legislative': 'ALLOW', 'judicial': 'DENY', 'treasury': 'DENY'}
[OK ] D1 vote: التشريعُ وحدَه — {'executive': 'DENY', 'legislative': 'ALLOW', 'judicial': 'DENY', 'treasury': 'DENY'}
[OK ] D2 contain_agent (suspend_state) لا يُمنَعُ عندَ أيِّ مستوى — [False, False, False, False, False, False]
[OK ] D3 activate_agent (reactivate_state) يُمنَعُ عندَ ≥4 وحدَها — [False, False, False, False, True, True]
PROBE SUMMARY: checks=30 broken=3
=== RAW [19] END ===
VERDICT_PER_CRITERION: (1) وثيقةُ التصميمِ G1_GOVERNANCE_CROSSING_DESIGN.md مودَعةٌ ← نعم (RAW [4] خروجٌ 0: الملفُّ حاضرٌ وفيه Q-13/Q-14/Q-26/Q-23) · (2) قياسُ sovereign_write_inventory.py بعدَ الدفعاتِ (الأساسُ 121 · الإسقاطُ 80 ثمَّ 91 بتعديلِ W-721/D28) والفرقُ مُقيَّدٌ ← نعم (RAW [10] خروجٌ 0: المقيسُ في تشغيلي 95 · وكتلةُ البندِ في ACTIVE_WORK تقيِّدُ كلَّ دفعةٍ 121←110←104←95 وتسمّي الأسطحَ المُمسَكةَ create_batch/enroll_batch (Q-77) وstart_training/evaluate_model/store_secret (Q-80 · D28 (أ)) مصدرًا للفرقِ عن الإسقاطِ 91) · (3) فحوصُ الأصنافِ الخمسةِ ← نعم (RAW [6] 54 passed · RAW [7] 40 passed · RAW [8] 59 passed · RAW [9] 10 passed · كلُّها خروجٌ 0) · (4) طفرةٌ لكلِّ سطحٍ ← نعم في حدودِ أوامرِ الإحاطةِ (RAW [11] طفرةُ issue_certificate في rules.py قُتِلَت: 3 failed خروجٌ 1 · RAW [13] طفرةُ guard_declared في learning_cycle.py قُتِلَت: 32 failed خروجٌ 1 · والإرجاعُ نظيفٌ RAW [12]/[14] بلا porcelain) — لم أُعِدْ تشغيلَ حملةِ الطفرةِ كاملةً على كلِّ سطحٍ · (5) Q-13 مرسومٌ ملكيٌّ ← نعم (RAW [6] خروجٌ 0 + مسباري B1–B6 في RAW [19]: بلا مرسومٍ/فعلٍ آخرَ/مُصرِّحٍ تنفيذيٍّ/هدفٍ آخرَ كلُّها رفضٌ بلا صفٍّ · الصحيحُ يسجِّلُ · وإعادةُ المرسومِ بعدَ حذفِ الصفِّ لا تُنشئُ ولايةً) · (6) Q-14 أثرٌ مُعلَنٌ + قاطعٌ + self_heal لا يُعيدُ ولايةً عُلِّقَت بقرارٍ ← نعم (RAW [6] خروجٌ 0 + مسباري A1–A8 وD2–D3 في RAW [19]: self_heal مرّتينِ لا يُعيدُ المعلَّقةَ بقرارٍ ويشفي المعلَّقةَ تلقائيًّا · reactivate ممنوعٌ عندَ 4 و5 بلا أثرٍ ومسموحٌ عندَ 3 · suspend لا يُمنَعُ عندَ 5 · self_heal ممنوعٌ عندَ 4) · (7) Q-26 معوّضٌ يعيدُ الوكيلَ ← لا (RAW [19] خروجٌ 1: مسباري C.k=2 وC.k=3 انكسرا — retire_agent يرفعُ SovereigntyViolation ولا سجلَّ تقاعدٍ، لكنَّ الهويةَ الكانونيّةَ تبقى retired وصفُّ المرآةِ employed: ('employed','employed','employed') ← ('retired','retired','employed') · وC2 يوطِّنُ الجذرَ في update_state وحدَه) · (8) Q-23 المعجمُ التشريعيُّ ← نعم (RAW [5] 19 passed خروجٌ 0 + مسباري D1 في RAW [19]: suspend_policy وvote ALLOW للتشريعِ وحدَه وDENY للتنفيذيِّ والقضائيِّ والخزانة)
PROBES: مسبارٌ واحدٌ ‎/home/user/workspace/council_w732/claude_opus_5_5/wi120/probe/g1_probe.py‎ بأربعِ محاولاتٍ على المسارِ الإنتاجيِّ (StateRuntime · SystemLifecycle · RetirementSystem · ConstitutionalAuthorizer · ConstitutionalEngine · قاعدةُ SQLite وسجلُّ ذرّيّةٍ مؤقّتانِ داخلَ دليلي · مستوى القاطعِ يُحقَنُ بصنفٍ فرعيٍّ لـ_request لأنَّ الجسرَ لا يحقنُه إنتاجيًّا · WI-085) — شِفرتُه كتلةُ RAW [18] · تشغيلُه كتلةُ RAW [19] (خروجٌ 1 · checks=30 broken=3): (A) Q-14 self_heal والقاطعُ على الإيقافِ المحكومِ ← انكسرت؟ لا · (B) Q-13 مسارُ المرسومِ الملكيِّ ومحاولاتُ تزويرِه وإعادتِه ← انكسرت؟ لا · (C) Q-26 ذرّيّةُ retire_agent ومعوّضُه تحتَ رفعِ القاطعِ إلى 3 بعدَ k طلبًا (k=0..8) ← انكسرت؟ نعم (k=2 وk=3) · (C2) توطينٌ: update_state وحدَه تحتَ رفضٍ متأخِّرٍ لعبورِ المرآة ← انكسرت؟ نعم · (D) Q-23 والشرطُ 2 من Q-14 على المحرّكِ ← انكسرت؟ لا
BLOCKING_REMARKS: (ح1 · حاجبةٌ · مسبارٌ كسرَ الخاصيّةَ) Q-26 «معوّضٌ يعيدُ الوكيلَ» لا يصمدُ أمامَ رفضٍ متأخِّرٍ داخلَ خطوةِ تحديثِ الحالةِ: `RetirementSystem.retire_agent` (expansion.py · W-724) يُنادي `registry.update_state(agent_id, "retired", authorizer=...)` **قبلَ** كتلةِ try/_undo ولا يحميه معوّضُه؛ و`update_state` (agent_runtime/population.py · W-699) ينجحُ عبورُه الكانونيُّ (contain_agent لا يُمنَعُ) ثمَّ يُرفَضُ عبورُ المرآةِ (update_population_state ممنوعٌ عندَ ≥3) فيرفعُ SovereigntyViolation، وفرعُ الاستثناءِ فيه يعكسُ الانتقالَ الكانونيَّ لـIdempotencyError وحدَه (`if not isinstance(exc, IdempotencyError): raise`) — فتبقى الهويةُ الكانونيّةُ retired والمرآةُ employed ولا سجلَّ تقاعدٍ والعمليةُ مُعلَنةٌ فاشلةً: حالةٌ وسطى وانشقاقُ كانونٍ/مرآةٍ. الجذرُ في سطحِ E1 لا في دفعاتِ G1، لكنَّ الخاصيّةَ المُدَّعاةَ للسطحِ الحاكمِ retire_agent (Q-26) هي التي تنكسرُ، والزنادُ (ارتفاعُ القاطعِ بينَ التصريحِ المسبقِ وعبورِ المرآةِ) هو عينُ «الرفضِ المتأخِّرِ» الذي يدّعي السطحُ تعويضَه. والاختبارُ القائمُ test_c1 يغطّي الرفضَ عندَ الطلبِ الثاني (k=1) لا الثالثَ ولا الرابعَ. (ملاحظةٌ غيرُ حاجبةٍ) لم أُعِدْ حملةَ الطفرةِ على كلِّ سطحٍ بل الطفرتَينِ المأمورتَينِ في (ج).
ISOLATION_DECLARATION: نعم مع استثناءاتٍ مُعلَنةٍ: لم أقرأْ أدلّةَ المنفِّذِ ولا حزمَه ولا عملَ المقاعدِ الأخرى ولا ذاكرةَ جلسةٍ أخرى · قرأتُ داخلَ استنساخي (لا خارجَه): كتلةَ البندِ وصفَّه في ACTIVE_WORK.md · الإحاطةَ · سجلَّ القراراتِ (RAW [15]) ووثيقةَ التصميمِ (RAW [4] وأسطرَ Q-14 منها) · وللاستثناءِ: شِفرةَ الإنتاجِ اللازمةَ لكتابةِ المسبارِ (governance/state_runtime.py · system_life.py · expansion.py · agent_runtime/population.py · executive_core/sovereignty_bridge.py · agent_identity.py · core/constitutional_engine/rules.py) واختباراتٍ قائمةً لأستعيرَ طريقةَ التهيئةِ فقط (federal/executive/services/tests/conftest.py · test_w723 · test_w724 · tests/constitutional/test_g1_vocabulary.py) وأداتَي الالتقاطِ والفحصِ · واستثناءُ كتابةٍ: سكربتا تشخيصٍ مؤقّتانِ في /tmp (diag_retire.py · diag2.py) لتوطينِ الانكسارِ ثمَّ حُذِفا، ومخابئُ pip/البيئةِ التي يكتبُها bootstrap.sh · وكلُّ ما عداها داخلَ جذري /home/user/workspace/council_w732/claude_opus_5_5/wi120/
VERDICT: FAIL — Q-26 (معوّضٌ يعيدُ الوكيلَ) انكسرَ بمسباري: retire_agent يفشلُ برفضٍ متأخِّرٍ لعبورِ مرآةِ update_state فيبقى الوكيلُ كانونيًّا retired والمرآةُ employed بلا سجلِّ تقاعدٍ (RAW [19] C.k=2/C.k=3/C2)
