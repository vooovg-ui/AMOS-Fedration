# حكمُ مقعدِ المجلسِ — gemini_3_8_flash (عائلةُ Google · Gemini) · جولةُ WI-082 (W-526)

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

MODEL: gemini_3_8_flash
FAMILY: Gemini
RUN_DATE: 2026-10-19 23:14 +00:00
NODE: 83c31a2697d6e3a8b834b2963037d018492c648c
CLONE_PATH: /home/user/workspace/seat_gemini_3_8_flash_wi082/repo
COMMANDS_RUN:
  1. git clone https://git-agent-proxy.perplexity.ai/vooovg-ui/AMOS-Fedration.git repo && cd repo && git checkout 83c31a2697d6e3a8b834b2963037d018492c648c
  2. bash tools/dev/bootstrap.sh
  3. .venv/bin/python tools/audit/sovereign_write_inventory.py --json /tmp/inv_seat.json
  4. rg -n "register_identity\(|update_identity\(|set_lifecycle_state\(" --type py federal core tools | rg -v /tests/ | rg -v "def "
  5. rg -c "register_identity\(|spawn_agent\(|update_identity\(|set_lifecycle_state\(" federal/executive/services/tests
  6. rg -n "spawn_agent" core/constitutional_engine/rules.py
  7. AMOS_DATABASE_URL=sqlite:////tmp/amos_seat_$$.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
  8. sed -i 's/ACTION_SPAWN_AGENT = "spawn_agent"/ACTION_SPAWN_AGENT = "register_agent"/' federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py && AMOS_DATABASE_URL=sqlite:////tmp/amos_seat_$$.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q; echo "EXIT=$?" && git checkout -- federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
  9. AMOS_DATABASE_URL=sqlite:////tmp/amos_seat_$$.db .venv/bin/python -m pytest federal/executive/services/tests/ -q
RAW_OUTPUTS:
--- Command 1: bash tools/dev/bootstrap.sh ---
[EXIT=0]
• الجذر: /home/user/workspace/seat_gemini_3_8_flash_wi082/repo
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

--- Command 2: .venv/bin/python tools/audit/sovereign_write_inventory.py --json /tmp/inv_seat.json ---
[EXIT=0]
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
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      18  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
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
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py
       1  federal/executive/services/src/amos_federation/services/government_services/service.py
       1  tools/migrations/r4_unify_agent_identity.py
  التفصيلُ محفوظٌ في: /tmp/inv_seat.json

--- Command 3a: rg -n "register_identity\(|update_identity\(|set_lifecycle_state\(" --type py federal core tools | rg -v /tests/ | rg -v "def " ---
[EXIT=0]
federal/executive/services/src/amos_federation/services/agent_runtime/population.py:187:        identity = register_identity(
federal/executive/services/src/amos_federation/services/agent_runtime/population.py:273:        canonical_updated = set_lifecycle_state(agent_id, new_state)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:373:            set_lifecycle_state(agent_id, AgentLifecycleState.TRAINING.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:403:        set_lifecycle_state(agent_id, AgentLifecycleState.ACTIVE.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:514:            set_lifecycle_state(agent_id, AgentLifecycleState.PAUSED.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:593:            set_lifecycle_state(agent_id, AgentLifecycleState.RETIRED.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:595:            set_lifecycle_state(agent_id, AgentLifecycleState.ACTIVE.value)
tools/migrations/r4_unify_agent_identity.py:322:                register_identity(

--- Command 3b: rg -c "register_identity\(|spawn_agent\(|update_identity\(|set_lifecycle_state\(" federal/executive/services/tests ---
[EXIT=0]
federal/executive/services/tests/test_r5_multi_provider_sandbox.py:1
federal/executive/services/tests/test_r7d_federal_judiciary.py:1
federal/executive/services/tests/test_2b_state_registry_sovereign.py:2
federal/executive/services/tests/test_r8_federal_state_integration.py:2
federal/executive/services/tests/test_r7_state_registry.py:1
federal/executive/services/tests/test_r4_agent_identity_and_population.py:11
federal/executive/services/tests/test_r6_1_authorization_closure.py:1
federal/executive/services/tests/test_r7_government_services.py:1
federal/executive/services/tests/test_r6_identity_authorization_root.py:2
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:7
federal/executive/services/tests/test_r7c_national_registry.py:1
federal/executive/services/tests/test_r7b_state_treasury.py:1
federal/executive/services/tests/test_2b_government_services_sovereign.py:3
federal/executive/services/tests/test_r9_national_economic_state.py:1

--- Command 3c: rg -n "spawn_agent" core/constitutional_engine/rules.py ---
[EXIT=0]
144:    3: frozenset({"dispatch_agent", "spawn_agent", "expand_state"}),

--- Command 4: AMOS_DATABASE_URL=sqlite:////tmp/amos_seat_$$.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q ---
[EXIT=0]
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/seat_gemini_3_8_flash_wi082/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 7 items

federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 14%]
......                                                                   [100%]

============================== 7 passed in 0.71s ===============================

--- Command 5: Mutation test (sed replace ACTION_SPAWN_AGENT -> register_agent) ---
[EXIT=1]
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/seat_gemini_3_8_flash_wi082/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 7 items

federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 14%]
FF....                                                                   [100%]

=================================== FAILURES ===================================
_____________ test_register_identity_declares_effect_under_target ______________
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:131: in test_register_identity_declares_effect_under_target
    assert call["action"] == "spawn_agent"
E   AssertionError: assert 'register_agent' == 'spawn_agent'
E     
E     - spawn_agent
E     + register_agent
____________ test_register_identity_refused_at_kill_switch_level_3 _____________
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:143: in test_register_identity_refused_at_kill_switch_level_3
    with pytest.raises(SovereigntyViolation) as excinfo:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: DID NOT RAISE SovereigntyViolation
=========================== short test summary info ===========================
FAILED federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_register_identity_declares_effect_under_target
FAILED federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_register_identity_refused_at_kill_switch_level_3
========================= 2 failed, 5 passed in 0.59s ==========================
EXIT=1

--- Command 6: AMOS_DATABASE_URL=sqlite:////tmp/amos_seat_$$.db .venv/bin/python -m pytest federal/executive/services/tests/ -q ---
[EXIT=0]
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/seat_gemini_3_8_flash_wi082/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1527 items

[... 1527 items collected across services tests ...]
=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/seat_gemini_3_8_flash_wi082/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========== 1474 passed, 53 skipped, 1 warning in 313.81s (0:05:13) ============

VERDICT_PER_CRITERION:
  - معيار القبول (1): نعم.
    الدليل: عُرض أثر إلزام الدوال الثلاث على المواضع الثمانية في كتلة البند بـ ACTIVE_WORK.md (قسم «WI-082 · عرضُ الأثرِ قبلَ الشِّفرة») قبل كتابة الشفرة. والمواضع الثمانية تم التحقق منها بالأمر rg (موضعان لـ register_identity، و6 مواضع لـ set_lifecycle_state، وصفر لـ update_identity). ولم يُمس العقد العام القائم حيث جاء المعامل اختياريًا authorizer=None (مُثبت في test_register_identity_signature_breaks_nothing_and_has_no_bypass). وسُجل سؤال PENDING_OWNER بشأن تسمية فعلي update_identity وset_lifecycle_state، ثم صدر قرار المالك في W-446 («فعلا WI-082 ③ الإيقاف المؤقت والتقاعد مسموحان دائمًا، والتفعيل والتدريب تحت spawn_agent») مع بقائهما دينًا معلنًا في هذه الدفعة دون فتح هجرة جديدة لهما.
  - معيار القبول (2): نعم.
    الدليل: الدالة register_identity تعبر الحد السيادي بالفعل spawn_agent وتُرفض عند المستوى الثالث من زر الإيقاف (R-008-2 في rules.py:144). الاختبارات السبعة في test_wi082_agent_identity_sovereign.py نجحت جميعها (7 passed). وعند إجراء طفرة تغيير الفعل ACTION_SPAWN_AGENT من spawn_agent إلى register_agent سقط الفحص وقتل الطفرة بـ EXIT=1 مع فشل فحصين صراحةً (test_register_identity_declares_effect_under_target و test_register_identity_refused_at_kill_switch_level_3).
  - معيار القبول (3): نعم.
    الدليل: بأداة sovereign_write_inventory.py، دين الملف agent_identity.py أصبح 2 (register_identity أصبح guarded=True، وبقي set_lifecycle_state و update_identity غير معبوري الحد دينًا معلنًا)، و D-4 نقص من 184 إلى 183، والسيادي نما من 16 إلى 17، مع ثبات بقية الملفات بلا أي نمو في غيره.
  - معيار القبول (4): نعم.
    الدليل: حزمة الخدمات الفدرالية كاملة خضراء برمز خروج 0 (1474 passed, 53 skipped, 0 failed)، وتتضمن الاختبارات الـ 13 ملف اختبار التي تنادي الدوال وتعمل دون انكسار.
  - معيار القبول (5): نعم.
    الدليل: تمت إعادة تشغيل جميع أوامر المعايير كاملةً بشكل مستقل وفعلي في استنساخ مستقل وبقاعدة بيانات مستقلة، والتحقق المباشر من المخرجات ورموز الخروج.

BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً

ISOLATION_DECLARATION: أُقرُّ بأنني استنسختُ المستودعَ في دليلٍ خاصٍّ بي مستقلٍّ (/home/user/workspace/seat_gemini_3_8_flash_wi082/repo)، وعملتُ داخله منفردًا، ولم أقرأ شيئًا من أدلّة المنفِّذ أو عمل المقاعد الأخرى، ولم أقرأ خارج استنساخي وهذه الإحاطة ومصادر المعايير المعلنة حصرًا في البند (د). كما أُقرُّ بأن البيئة ذات نظام ملفات مشترك.

VERDICT: PASS لكلِّ المعاييرِ
