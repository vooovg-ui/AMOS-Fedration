# حكمُ مقعدِ المجلسِ — grok_4_7 (عائلةُ xAI · Grok) · جولةُ WI-082 (W-526)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-082 (بروتوكولُ Q-59 · بندُ WI-100) — لا تحريرَ ولا تلخيصَ.

## النطاق
حكمُ مقعدٍ واحدٍ على البندِ WI-082 بإحاطةِ W-525 المبصومةِ (sha256 `37865b4358af96a8afbd2bdb27f601fe396817f0fb08ba992af652111841bdcd`) عندَ العقدةِ `83c31a2697d6e3a8b834b2963037d018492c648c`.

## المالك
بندُ WI-100 (المنسِّقُ: Perplexity Computer · النموذجُ المنسِّقُ الحاضرُ GLM-5.3 كما أعلنتْهُ المنصةُ — منسِّقٌ لا مُصوِّتٌ).

## تاريخ الإنشاء
2026-10-19

## تاريخ آخر تعديل
2026-10-19 (W-526 — حفظُ الحكمِ بعدَ اكتمالِ المقاعدِ كلِّها · § 2.3)

---

MODEL: grok_4_7
FAMILY: Grok
RUN_DATE: 2026-10-19 23:19 +00:00
NODE: 83c31a2697d6e3a8b834b2963037d018492c648c
CLONE_PATH: /home/user/workspace/seat_grok_4_7_wi082
COMMANDS_RUN: git clone --no-checkout https://git-agent-proxy.perplexity.ai/vooovg-ui/AMOS-Fedration.git /home/user/workspace/seat_grok_4_7_wi082 ; git checkout 83c31a2697d6e3a8b834b2963037d018492c648c ; bash tools/dev/bootstrap.sh ; .venv/bin/python tools/audit/sovereign_write_inventory.py --json /tmp/inv_seat.json ; rg -n "register_identity\(|update_identity\(|set_lifecycle_state\(" --type py federal core tools | rg -v /tests/ | rg -v "def " ; rg -c "register_identity\(|spawn_agent\(|update_identity\(|set_lifecycle_state\(" federal/executive/services/tests ; rg -n "spawn_agent" core/constitutional_engine/rules.py ; AMOS_DATABASE_URL=sqlite:////tmp/amos_seat_$$.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q ; sed mutation ACTION_SPAWN_AGENT spawn_agent→register_agent then same pytest ; echo EXIT ; git checkout -- agent_identity.py ; AMOS_DATABASE_URL=sqlite:////tmp/amos_seat_$$.db .venv/bin/python -m pytest federal/executive/services/tests/ -q
RAW_OUTPUTS:
[clone] exit=0
HEAD=83c31a2697d6e3a8b834b2963037d018492c648c
log -1: 83c31a2 W-524: WI-082 IN_PROGRESS → IN_REVIEW (قيدٌ مستقلٌّ H3) تمهيدًا لجولةِ مجلسِ المراجعةِ — لا شِفرةَ — توثيقٌ وحدَه
status: ## HEAD (no branch)

[bash tools/dev/bootstrap.sh] BOOTSTRAP_EXIT=0
• الجذر: /home/user/workspace/seat_grok_4_7_wi082
• ثُبِّتَ خُطّافُ pre-push
• إنشاءُ بيئةٍ معزولةٍ في .venv
• تركيبُ تبعيّاتِ الجذر (requirements-dev.txt)
• تركيبُ حزمةِ الخدماتِ
• تركيبُ ruff==0.6.9
✓ البيئةُ جاهزة.
(venv pytest later reported Python 3.12.13)

[.venv/bin/python tools/audit/sovereign_write_inventory.py --json /tmp/inv_seat.json] INVENTORY_EXIT=0
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 219
  عمليّاتٌ عامّةٌ مُغيِّرة   : 202
  منها تعبرُ الحدَّ        : 17
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 183
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          172 /  17 /  154
    tools               1 /   0 /    1
  ...
       2  federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
  التفصيلُ محفوظٌ في: /tmp/inv_seat.json

[read of /tmp/inv_seat.json as the command's own output, per briefing]
summary.non_sovereign_write_operations = 183   # D-4
summary.sovereign_write_operations = 17
summary.write_sites_total = 219
summary.public_write_operations = 202
non_sovereign_by_file[.../executive_core/agent_identity.py] = 2
sites:
  register_identity public=true guarded=true closed_legacy=false writes=[] writes_via=[_delete_identity_row, _write_identity_row]
  set_lifecycle_state public=true guarded=false closed_legacy=false writes=["commit()"]
  update_identity public=true guarded=false closed_legacy=false writes=["commit()"]

[rg call sites] RG1_EXIT=0 PIPE=0 0 0
federal/executive/services/src/amos_federation/services/agent_runtime/population.py:187:        identity = register_identity(
federal/executive/services/src/amos_federation/services/agent_runtime/population.py:273:        canonical_updated = set_lifecycle_state(agent_id, new_state)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:373:            set_lifecycle_state(agent_id, AgentLifecycleState.TRAINING.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:403:        set_lifecycle_state(agent_id, AgentLifecycleState.ACTIVE.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:514:            set_lifecycle_state(agent_id, AgentLifecycleState.PAUSED.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:593:            set_lifecycle_state(agent_id, AgentLifecycleState.RETIRED.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:595:            set_lifecycle_state(agent_id, AgentLifecycleState.ACTIVE.value)
tools/migrations/r4_unify_agent_identity.py:322:                register_identity(
(8 lines; update_identity production calls = 0)

[rg -c tests] RG2_EXIT=0
federal/executive/services/tests/test_r5_multi_provider_sandbox.py:1
federal/executive/services/tests/test_r7d_federal_judiciary.py:1
federal/executive/services/tests/test_r7_state_registry.py:1
federal/executive/services/tests/test_r4_agent_identity_and_population.py:11
federal/executive/services/tests/test_r6_1_authorization_closure.py:1
federal/executive/services/tests/test_r7_government_services.py:1
federal/executive/services/tests/test_2b_state_registry_sovereign.py:2
federal/executive/services/tests/test_r8_federal_state_integration.py:2
federal/executive/services/tests/test_r7c_national_registry.py:1
federal/executive/services/tests/test_2b_government_services_sovereign.py:3
federal/executive/services/tests/test_r9_national_economic_state.py:1
federal/executive/services/tests/test_r6_identity_authorization_root.py:2
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:7
federal/executive/services/tests/test_r7b_state_treasury.py:1
(14 files; counts sum = 35 = 28 historical + 7 in the new WI-082 file)

[rg spawn_agent rules.py] RG3_EXIT=0
144:    3: frozenset({"dispatch_agent", "spawn_agent", "expand_state"}),

[pytest test_wi082_agent_identity_sovereign.py -q] WI082_TEST_EXIT=0
collected 7 items
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 14%]
......                                                                   [100%]
============================== 7 passed in 1.07s ===============================

[mutation] SED_EXIT=0
mutated line 81: ACTION_SPAWN_AGENT = "register_agent"
pytest: collected 7 items
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 14%]
FF....                                                                   [100%]
FAILED test_register_identity_declares_effect_under_target
  AssertionError: assert 'register_agent' == 'spawn_agent'
FAILED test_register_identity_refused_at_kill_switch_level_3
  Failed: DID NOT RAISE SovereigntyViolation
========================= 2 failed, 5 passed in 0.82s ==========================
EXIT=1
git checkout -- agent_identity.py CHECKOUT_EXIT=0
restored line 81: ACTION_SPAWN_AGENT = "spawn_agent"
git diff --stat empty DIFF_STAT_EXIT=0
post-run git status --porcelain empty

[pytest federal/executive/services/tests/ -q] SERVICES_TEST_EXIT=0
platform linux -- Python 3.12.13, pytest-9.1.1
collected 1527 items
(progress body: dots and skips only; no F and no E in the progress)
test_wi082_agent_identity_sovereign.py . ...... [100%]
=========== 1474 passed, 53 skipped, 1 warning in 315.96s (0:05:15) ============
stderr: Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:4317: Failed to connect to remote host: Connection refused
warning: StarletteDeprecationWarning from fastapi/testclient.py (httpx/starlette.testclient)
1474+53=1527

VERDICT_PER_CRITERION:
(1) نعم — عرضُ الأثرِ قبلَ الشِّفرة موجودٌ في كتلةِ البندِ المسموحِ قراءتُها (ACTIVE_WORK.md «#### WI-082 · عرضُ الأثرِ قبلَ الشِّفرة» · التزامُ W-390 = 8a10950eb20f7727a5cd71fcaba77220a3700a9f بتاريخ 2026-10-16 08:46:32 +0000، وعنوانُه «قبلَ أيِّ شِفرة»). شِفرةُ الهجرةِ دخلت لاحقًا في W-402 = 14c43a28976e2f6970acd06b3dc9fe87c74373b0 بتاريخ 2026-10-17 21:37:19 +0000، ثمّ ارتدّت (W-425) واستُعيدت (W-465). إعادةُ أوامرِ القياسِ أنتجت المواضعَ الثمانيةَ نفسَها وبالأسطرِ نفسِها، وupdate_identity ×0، وspawn_agent في rules.py:144 داخل KILL_SWITCH_BLOCKS[3]. العقدُ العامُّ لم يُلزَم بـAuthorizationContext: register_identity يضيف authorizer اختياريًّا بالاسمِ وافتراضُه None (السطران 273 و279)، والفحصُ 7 نجح. سؤالُ التسميةِ كُتِب PENDING_OWNER في الكتلةِ ولم يُخمَّن؛ وقرارُ W-446 أبقى الاثنينِ دَينًا بلا هجرةٍ في هذه الجولة. لم أفتح محتوياتِ evidence/W-390/.
(2) نعم — في التشغيلِ السليمِ 7 passed EXIT=0. register_identity ينادي guard_declared(ACTION_SPAWN_AGENT, ...) والثابتُ "spawn_agent". عند المستوى 3 يُرفضُ الإنشاءُ (الفحصُ test_register_identity_refused_at_kill_switch_level_3 نجح قبلَ الطفرة). الطفرةُ spawn_agent→register_agent: EXIT=1 وليست صامتةً. سقط فحصان لا ثلاثة: test_register_identity_declares_effect_under_target (الفعلُ صار register_agent) وtest_register_identity_refused_at_kill_switch_level_3 (لم يُرفع SovereigntyViolation). ترتيبُ الجمعِ .FF.... أي الفحصان 2 و3، لا 1 و3 و7. الفحصُ 1 (مراحلُ الحدِّ) والفحصُ 7 (توقيعٌ بلا كسر) لا يثبتانِ اسمَ الفعلِ فبقيا أخضرين. الخاصيةُ التي يسمّيها المعيارُ (إسقاطُ الفحصِ عند تبديلِ الفعل، ورفضُ المستوى 3 مربوطٌ بـspawn_agent) تحقّقت. فرقُ العدِّ عن «3 فحوص · 1 و3 و7» المُقيَّد في الإحاطةِ مُعلَنٌ هنا وغيرُ حاجبٍ لأنَّ الفحصينِ اللذينِ يحكمانِ اسمَ الفعلِ وزرَّ الإيقافِ هما اللذانِ سقطا.
(3) نعم بالقراءةِ المعدَّلةِ (W-390 ج + قرارُ W-446) لا بالصيغةِ التاريخيةِ 3→0. قياسي على هذه العقدة: دَينُ agent_identity.py = 2؛ register_identity guarded=true؛ update_identity وset_lifecycle_state guarded=false وwrites=["commit()"]؛ D-4 = 183؛ sovereign = 17؛ write_sites_total = 219. قياسُ ما قبلُ في كتلةِ البندِ المسموحة: دَينٌ 3 وD-4 184. الفرقُ −1 في الملفِّ و−1 في D-4 و+1 في السياديِّ مع ثباتِ المجموعِ 219 يطابقُ هجرةَ register_identity وحدَه بلا نموٍّ في غيرِه. الصيغةُ الأولى (بعدُ = 0 وD-4 ينقصُ 3) لم تتحقّق وهي باقيةٌ للتاريخِ لا للقراءةِ العاملة. الاثنانِ دَينٌ مُعلَنٌ ولا هجرةَ لهما في هذه الجولةِ بنصِّ نقلِ W-446.
(4) نعم في التشغيلِ المحليِّ المأمورِ به: EXIT=0 · 1474 passed · 53 skipped · 0 failed · 1527 collected. الملفاتُ الـ13 التي تنادي الدوالَّ في قياسِ ما قبلُ ما زالت في خرجِ rg -c وبالعدِّ نفسِه (28)، ويُضافُ إليها test_wi082_agent_identity_sovereign.py:7، والمجموعُ 35، وكلُّها داخلَ الحزمةِ الخضراء. الـ53 تخطيًا في فحوصِ Postgres الحيّةِ ونحوِها لا فشلًا (1474+53=1527). CI على هذه العقدة: gh commit status state=pending total=0؛ check-runs total=0. لا أزعمُ أنَّ CI أخضر. الإحاطةُ والبندُ يحيلانِ حكمَ CI إلى واجبِ N+1، فلم أعدَّ غيابه إخفاقًا لهذه الجولة.
(5) نعم — هذه الجولةُ أعادت تشغيلَ أوامرِ (ج) وحفظت الخرجَ الخامَّ ورموزَ الخروج، ولم تحكم من أدلّةِ المنفِّذِ وحدَها. لا VERIFIED من هذا المقعد؛ الإجماعُ خارجُ تشغيلِ مقعدٍ واحد.

BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم، نظامُ الملفّاتِ مشتركٌ وأُقِرُّ بذلك. الاستنساخُ خاصٌّ بهذا المقعدِ في /home/user/workspace/seat_grok_4_7_wi082 عند العقدةِ أعلاه، ولم أعمل داخل /home/user/workspace/amos ولم أقرأ أدلّةَ المنفِّذِ ولا عملَ المقاعدِ الأخرى. القراءةُ داخلَ الاستنساخِ اقتصرت على كتلةِ WI-082 وعرضِ أثرِها في ACTIVE_WORK.md، وQ-15 وQ-51 ونقلِ W-446 في SOVEREIGN_DECISION_REGISTER.md، والشِفرةِ والفحوصِ قيدَ المراجعةِ لتفسيرِ الخرج. استثناءٌ ضيّق: سردتُ أسماءَ ملفاتِ docs/audit/evidence/W-390/ فقط (لم أقرأ محتوياتِها ولم أدخلها في الحكم)، واستعلمتُ gh عن حالةِ CI لهذه العقدةِ (pending · 0) ولم أقرأ سجلاتِ تشغيل.
VERDICT: PASS لكلِّ المعاييرِ
