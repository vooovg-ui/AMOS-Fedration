# حكمُ مقعدِ المجلسِ — gemini_3_8_flash (عائلةُ Google · Gemini) · جولةُ WI-082 المستعادةُ بالإحاطاتِ v5 (W-575)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-082 (بروتوكولُ Q-59 · بندُ WI-100) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في دليلِهِ الخاصِّ `council_w574/gemini_3_8_flash` (§ 4.8: ملفُّ الحكمِ هو الحكمُ) — منسوخٌ آليًّا، وما بعدَ الفاصلِ بايتًا ببايتٍ (sha256 `cbe093eef333f0a106b42f42388e93fe1cc25112fe1ae9d567fabfe47a191524`).

## النطاق
حكمُ مقعدٍ واحدٍ على البندِ WI-082 بإحاطتِهِ المبصومةِ في W-574 عندَ العقدةِ `42e1c17a253629808d9fa7c267ab6238b26b7d68` (15 أمرًا مُلتقَطًا بـ`council_raw_capture.py`).

## المالك
بندُ WI-100 (المنسِّقُ: Perplexity Computer · النموذجُ المنسِّقُ الحاضرُ Claude Opus 5.5 (عائلةُ Anthropic · Claude) كما تعرضُه المنصةُ — منسِّقٌ لا مُصوِّتٌ).

## تاريخ الإنشاء
2026-10-21

## تاريخ آخر تعديل
2026-10-21 (W-575 — حفظُ الحكمِ بعدَ اكتمالِ المقاعدِ كلِّها · § 2.3)

---

MODEL: gemini_3_8_flash
FAMILY: Google · Gemini
RUN_DATE: 2026-10-21 08:08 +00:00
NODE: 42e1c17a253629808d9fa7c267ab6238b26b7d68
CLONE_PATH: /home/user/workspace/council_w574/gemini_3_8_flash/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && git rev-parse HEAD
 2. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && bash tools/dev/bootstrap.sh
 3. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 4. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && rg -n "register_identity\(|update_identity\(|set_lifecycle_state\(" --type py federal core tools | rg -v /tests/ | rg -v "def "
 5. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && rg -c "register_identity\(|spawn_agent\(|update_identity\(|set_lifecycle_state\(" federal/executive/services/tests
 6. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && rg -n "spawn_agent" core/constitutional_engine/rules.py
 7. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w574/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
 8. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && sed -i 's/ACTION_SPAWN_AGENT = "spawn_agent"/ACTION_SPAWN_AGENT = "register_agent"/' federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
 9. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w574/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
 10. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && git checkout -- federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
 11. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w574/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/ -q
 12. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py -q
 13. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && cat federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
 14. cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && cat federal/executive/services/tests/test_wi082_agent_identity_sovereign.py
 15. find /home/user/workspace/council_w574/gemini_3_8_flash -maxdepth 1
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 39aa3b5eb96abab7d106ecffc22d30f81149828c2a56fc2b9b36496c56c16336
NO_EOL: 0
--- OUTPUT ---
42e1c17a253629808d9fa7c267ab6238b26b7d68
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && bash tools/dev/bootstrap.sh
EXIT: 0
BYTES: 1295
SHA256: e82a0c8c6b81abe058b103143a9beb5db823ebc07afda061590fbf67347517b5
NO_EOL: 0
--- OUTPUT ---
• الجذر: /home/user/workspace/council_w574/gemini_3_8_flash/repo
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
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3502
SHA256: 484053ff6f3f42fe5738e5c6e778996bd38ae55a9dbaa867ea42d35c5b244ea7
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 220
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
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && rg -n "register_identity\(|update_identity\(|set_lifecycle_state\(" --type py federal core tools | rg -v /tests/ | rg -v "def "
EXIT: 0
BYTES: 1165
SHA256: 4333af72d38061d93bca53d662d90ec8b446e068a76044b45d731e4b81419d10
NO_EOL: 0
--- OUTPUT ---
federal/executive/services/src/amos_federation/services/agent_runtime/population.py:187:        identity = register_identity(
federal/executive/services/src/amos_federation/services/agent_runtime/population.py:273:        canonical_updated = set_lifecycle_state(agent_id, new_state)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:373:            set_lifecycle_state(agent_id, AgentLifecycleState.TRAINING.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:403:        set_lifecycle_state(agent_id, AgentLifecycleState.ACTIVE.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:514:            set_lifecycle_state(agent_id, AgentLifecycleState.PAUSED.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:593:            set_lifecycle_state(agent_id, AgentLifecycleState.RETIRED.value)
federal/executive/services/src/amos_federation/services/agent_runtime/health.py:595:            set_lifecycle_state(agent_id, AgentLifecycleState.ACTIVE.value)
tools/migrations/r4_unify_agent_identity.py:322:                register_identity(
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && rg -c "register_identity\(|spawn_agent\(|update_identity\(|set_lifecycle_state\(" federal/executive/services/tests
EXIT: 0
BYTES: 973
SHA256: bbaacb776c3b6e284fa12d8a221b5ae83a7adbcfada6e46117aaa49b2076eb31
NO_EOL: 0
--- OUTPUT ---
federal/executive/services/tests/test_r5_multi_provider_sandbox.py:1
federal/executive/services/tests/test_r7d_federal_judiciary.py:1
federal/executive/services/tests/test_r7_state_registry.py:1
federal/executive/services/tests/test_r4_agent_identity_and_population.py:11
federal/executive/services/tests/test_r6_1_authorization_closure.py:1
federal/executive/services/tests/test_r7_government_services.py:1
federal/executive/services/tests/test_r7c_national_registry.py:1
federal/executive/services/tests/test_2b_government_services_sovereign.py:3
federal/executive/services/tests/test_r9_national_economic_state.py:1
federal/executive/services/tests/test_2b_state_registry_sovereign.py:2
federal/executive/services/tests/test_r8_federal_state_integration.py:2
federal/executive/services/tests/test_r6_identity_authorization_root.py:2
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:12
federal/executive/services/tests/test_r7b_state_treasury.py:1
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && rg -n "spawn_agent" core/constitutional_engine/rules.py
EXIT: 0
BYTES: 73
SHA256: a657e56bdf6e7b43546703c322df012e798cb218549707ce0406a92fb0183619
NO_EOL: 0
--- OUTPUT ---
144:    3: frozenset({"dispatch_agent", "spawn_agent", "expand_state"}),
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w574/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
EXIT: 0
BYTES: 714
SHA256: fb4c22fb6105a66d04ef5e4e9fd7bbeccc8450f7c45e0dd4a3f0322f4f497be6
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w574/gemini_3_8_flash/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 8 items

federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 12%]
.......                                                                  [100%]

============================== 8 passed in 0.62s ===============================
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && sed -i 's/ACTION_SPAWN_AGENT = "spawn_agent"/ACTION_SPAWN_AGENT = "register_agent"/' federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w574/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
EXIT: 1
BYTES: 2392
SHA256: 62b05e3b6e7693a68977647c9f9246f04c5cfe1ea6ebe9a5229b66ad6d51484c
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w574/gemini_3_8_flash/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 8 items

federal/executive/services/tests/test_wi082_agent_identity_sovereign.py F [ 12%]
.F...F.                                                                  [100%]

=================================== FAILURES ===================================
_______ test_wi082_1_register_crosses_boundary_and_returns_same_contract _______
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:128: in test_wi082_1_register_crosses_boundary_and_returns_same_contract
    assert evidence["action"] == "spawn_agent"
E   AssertionError: assert 'register_agent' == 'spawn_agent'
E     
E     - spawn_agent
E     + register_agent
_____________ test_wi082_3_kill_switch_level_3_blocks_spawn_agent ______________
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:161: in test_wi082_3_kill_switch_level_3_blocks_spawn_agent
    with pytest.raises(SovereigntyViolation) as excinfo:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: DID NOT RAISE SovereigntyViolation
________________ test_wi082_7_default_authorizer_path_unchanged ________________
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py:259: in test_wi082_7_default_authorizer_path_unchanged
    assert ACTION_SPAWN_AGENT == "spawn_agent"
E   AssertionError: assert 'register_agent' == 'spawn_agent'
E     
E     - spawn_agent
E     + register_agent
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_1_register_crosses_boundary_and_returns_same_contract
FAILED federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_3_kill_switch_level_3_blocks_spawn_agent
FAILED federal/executive/services/tests/test_wi082_agent_identity_sovereign.py::test_wi082_7_default_authorizer_path_unchanged
========================= 3 failed, 5 passed in 0.92s ==========================
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && git checkout -- federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w574/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/ -q
EXIT: 0
BYTES: 13405
SHA256: af147b8488c674d511a5b9000047ea67a187ca1c081f6f533ed8a786dc621830
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w574/gemini_3_8_flash/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1528 items

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
..........                                                               [ 10%]
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
.......................                                                  [ 27%]
federal/executive/services/tests/test_governance.py .................... [ 28%]
.......                                                                  [ 28%]
federal/executive/services/tests/test_governance_phase3.py ............. [ 29%]
............                                                             [ 30%]
federal/executive/services/tests/test_hash_chain.py ......               [ 30%]
federal/executive/services/tests/test_health.py ..............           [ 31%]
federal/executive/services/tests/test_health_system.py ................. [ 32%]
...............                                                          [ 33%]
federal/executive/services/tests/test_inmemory_stores.py ............... [ 34%]
.................                                                        [ 36%]
federal/executive/services/tests/test_king_login_boundary.py ........... [ 36%]
...........                                                              [ 37%]
federal/executive/services/tests/test_memory_service.py ........         [ 38%]
federal/executive/services/tests/test_model_gateway.py ....              [ 38%]
federal/executive/services/tests/test_model_layer.py ..............      [ 39%]
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
federal/executive/services/tests/test_phase1_postgres.py ssssssss        [ 47%]
federal/executive/services/tests/test_phase1_postgres_events.py ssssssss [ 47%]
sssssssss                                                                [ 48%]
federal/executive/services/tests/test_phase2_events.py ................. [ 49%]
..........                                                               [ 49%]
federal/executive/services/tests/test_phase3_governance.py ............. [ 50%]
...........                                                              [ 51%]
federal/executive/services/tests/test_phase4_tools.py .................. [ 52%]
                                                                         [ 52%]
federal/executive/services/tests/test_phase5_models.py ...........       [ 53%]
federal/executive/services/tests/test_phase6_population.py ............. [ 54%]
..                                                                       [ 54%]
federal/executive/services/tests/test_phase7_health.py .........         [ 54%]
federal/executive/services/tests/test_population.py ..................   [ 56%]
federal/executive/services/tests/test_q19_money_delegation.py .......... [ 56%]
..................                                                       [ 57%]
federal/executive/services/tests/test_q20_money_representation.py ...... [ 58%]
.ss..................                                                    [ 59%]
federal/executive/services/tests/test_q31_money_engine_wiring.py ....... [ 60%]
.....                                                                    [ 60%]
federal/executive/services/tests/test_q32_money_enforcement_surface.py . [ 60%]
..............                                                           [ 61%]
federal/executive/services/tests/test_r1_canonical_execution_path.py ... [ 61%]
..............                                                           [ 62%]
federal/executive/services/tests/test_r2_task_execution_integration.py . [ 62%]
........................                                                 [ 64%]
federal/executive/services/tests/test_r3_agent_runtime_integration.py .. [ 64%]
...........                                                              [ 65%]
federal/executive/services/tests/test_r4_agent_identity_and_population.py . [ 65%]
...............                                                          [ 66%]
federal/executive/services/tests/test_r5_multi_provider_sandbox.py ..... [ 66%]
..............                                                           [ 67%]
federal/executive/services/tests/test_r6_1_authorization_closure.py .... [ 67%]
..............                                                           [ 68%]
federal/executive/services/tests/test_r6_identity_authorization_root.py . [ 68%]
................                                                         [ 69%]
federal/executive/services/tests/test_r7_government_services.py ........ [ 70%]
........................                                                 [ 71%]
federal/executive/services/tests/test_r7_state_registry.py ............. [ 72%]
.............                                                            [ 73%]
federal/executive/services/tests/test_r7b_state_treasury.py ............ [ 74%]
........................                                                 [ 75%]
federal/executive/services/tests/test_r7c_national_registry.py ......... [ 76%]
..........................                                               [ 78%]
federal/executive/services/tests/test_r7d_federal_judiciary.py ......... [ 78%]
..................                                                       [ 79%]
federal/executive/services/tests/test_r8_federal_state_integration.py .. [ 80%]
...............................                                          [ 82%]
federal/executive/services/tests/test_r9_national_economic_state.py .... [ 82%]
.........................................                                [ 85%]
federal/executive/services/tests/test_real_tools.py .................... [ 86%]
                                                                         [ 86%]
federal/executive/services/tests/test_shadow.py ..........               [ 86%]
federal/executive/services/tests/test_step19_durable_governance_state.py . [ 87%]
.......                                                                  [ 87%]
federal/executive/services/tests/test_step7_gate_denial.py .....         [ 87%]
federal/executive/services/tests/test_tool_registry.py .......           [ 88%]
federal/executive/services/tests/test_training.py ...............        [ 89%]
federal/executive/services/tests/test_treasury.py ...................... [ 90%]
..........                                                               [ 91%]
federal/executive/services/tests/test_w032_registry_ownership.py ....... [ 91%]
......                                                                   [ 92%]
federal/executive/services/tests/test_w033_cost_record_durability.py ... [ 92%]
......                                                                   [ 92%]
federal/executive/services/tests/test_w036_cost_precision.py ........... [ 93%]
                                                                         [ 93%]
federal/executive/services/tests/test_w166_postgres_driver_declared.py . [ 93%]
...............                                                          [ 94%]
federal/executive/services/tests/test_w190_durable_model_registry.py ..  [ 94%]
federal/executive/services/tests/test_w308_test_ledger_is_per_session.py . [ 94%]
..                                                                       [ 94%]
federal/executive/services/tests/test_wi062_migrations_cover_orm_tables.py . [ 94%]
.s                                                                       [ 95%]
federal/executive/services/tests/test_wi063_tenant_isolation_http.py ..s [ 95%]
s..ss.s..ss.s.s.s..s.s.                                                  [ 96%]
federal/executive/services/tests/test_wi064_migrations_follow_orm.py .s  [ 96%]
federal/executive/services/tests/test_wi065_orm_declares_jsonb_timestamptz.py . [ 96%]
.s                                                                       [ 97%]
federal/executive/services/tests/test_wi066_convert_create_all_databases.py . [ 97%]
sssss                                                                    [ 97%]
federal/executive/services/tests/test_wi066_pg_session_isolation.py .ss  [ 97%]
federal/executive/services/tests/test_wi067_legal_search_isolated.py ... [ 97%]
....................                                                     [ 99%]
federal/executive/services/tests/test_wi076_pg_backup_restore.py ssss    [ 99%]
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 99%]
.......                                                                  [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w574/gemini_3_8_flash/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========== 1475 passed, 53 skipped, 1 warning in 308.02s (0:05:08) ============
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py -q
EXIT: 0
BYTES: 100
SHA256: 805b9b880e763deb91d663e4a1ec2d56134b1fdfc3a48a8f3c6862394e63b1a5
NO_EOL: 0
--- OUTPUT ---
..........                                                               [100%]
10 passed in 12.14s
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && cat federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
EXIT: 0
BYTES: 26367
SHA256: 17bf4917c87f66f71e4643e200241649ffb44be5e94778c4b357d7b8ed017020
NO_EOL: 0
--- OUTPUT ---
"""الهدف: مصدر حقيقة واحد لهوية الوكيل — وسكّان النظام كإسقاط عنه.

النطاق: federal/executive/services — النواة التنفيذية
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-16
تاريخ آخر تعديل: 2026-10-20 (W-532 — المُصرِّحُ الافتراضيُّ كائنٌ واحدٌ للوحدةِ بالقياسِ ·
قرارُ المالكِ Q-62 ② · فوقَ استعادةِ 1c52572 في W-531) · ووقبله 2026-10-17 (W-402 — WI-082: هجرةُ register_identity عبرَ الحدِّ
السياديِّ بالفعلِ «spawn_agent» بقرارِ المالكِ Q-15 ① · بلا مساسٍ بالاثنَينِ
الباقيَينِ المعلَّقَينِ على حسمِ التسميةِ عندَ المالكِ)

حقائق مقيسة قبل هذه الوحدة (R4-A):

- كان هناك **سجلّان** يُنشئان هوية وكيل ويحفظانها:
  1. جدول `agents` عبر `AgentModel` في `common/database.py`، يُكتب فقط من
     `dispatcher.register_agent`، ويُقرأ من `CapabilityDispatcher.candidates /
     available_agents / select / assignment_for` — أي أن مسار التنفيذ الفعلي
     (Dispatcher → Runtime Gateway، R1–R3) لا يعرف غيره.
  2. جدول `agent_population` في `agent_runtime/population.py`، بمحرِّك
     SQLAlchemy وقاعدة تعريف (`PopulationBase`) خاصّين به، يولّد `agent_id`
     بنفسه ولا يشارك المعرّف مع `agents`. ويُقرأ من: `health.py`،
     `control_console/main.py`، `governance/expansion.py`،
     `governance/federation.py`، `governance/treasury.py`، و SQL خام في
     `royal/main.py`.
- النتيجة المقيسة: هويّتان لنفس الوكيل، دورتا حياة مختلفتان (`agents.status`
  مقابل `agent_population.state`)، وعدّادان مختلفان للسكّان.
- لا توجد أي `ForeignKey` في المستودع تشير إلى أيّ من الجدولين (`grep
  "ForeignKey(" federal/` = صفر نتائج)، فالتوحيد لا يكسر قيودًا مرجعية.

**القرار (R4-B) مبنيّ على البنية الموجودة لا على تفضيل شكلي:** الجدول
`agents` هو المصدر الكانوني لهوية الوكيل، لأنه:

1. الجدول الوحيد الذي يقرأه مسار التنفيذ المعتمد (توزيع → تعيين → تشغيل).
2. يسكن نفس `get_session_factory()` الذي تسكنه `tasks`، فقراءة الهوية لحظة
   التنفيذ تجري على نفس المحرِّك لا على محرِّك ثانٍ.
3. يحفظ الصلاحيات والأدوات في أعمدة `JSON` مكتوبة، لا نصًّا يُفكّ يدويًّا.

و`agent_population` **ليس** سجل هوية ثانيًا بعد R4: صار جدول **ملفّ تدريبي
وإسقاط للقراءة** (category، school_score، specialization، tokens_used،
graduated_at) مفتاحه هو نفس `agent_id` الكانوني. أعمدته المكرّرة (name، role،
permissions، allowed_tools، state) تبقى مكتوبة كـ **مرآة توافُقية مهجورة
(deprecated mirror)** لقرّاء خارج هذا المستودع، ولا يُقرأ منها شيء هنا.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from amos_federation.common.database import AgentModel, get_session_factory
from amos_federation.services.executive_core.dispatcher import EMPLOYABLE_STATUSES
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)

#: اسم الجدول الكانوني للهوية.
CANONICAL_IDENTITY_TABLE = "agents"

#: جدول صار إسقاطًا وملفًّا تدريبيًّا — ليس مصدر هوية.
PROJECTION_TABLE = "agent_population"

#: قيمة تُكتب حين لا تتوفّر المعلومة — لا تُختلق.
UNKNOWN = "UNKNOWN"

#: تصنيف أمانة الإسقاط السكّاني: مبنيّ على السجل الكانوني فعلًا.
POPULATION_FIDELITY = "REAL"

#: نشاط التشغيل (executing/failed) يُقرأ من أحداث دورة الحياة المسجَّلة في R3.
RUNTIME_ACTIVITY_SUBJECT = "amos_federation.executive.agent_lifecycle"

#: فاعلُ إنشاءِ الهويّة (WI-082 · قرارُ المالكِ Q-15 ①): إنشاءُ هويةِ وكيلٍ في
#: السجلِّ الكانونيِّ عملُ السلطةِ التنفيذيّةِ، فالفاعلُ يُعلَنُ تنفيذيًّا ولا يُثبَّتُ —
#: المُصرِّحُ يبقى قابلاً للتمريرِ صراحةً (`authorizer`) والافتراضُ لا يوسِّعُ شيئًا.
AGENT_IDENTITY_ACTOR = "EXECUTIVE"

#: الفعلُ السياديُّ لإنشاءِ الهويّة — قرارُ المالكِ Q-15 ①: يُعلَنُ إنشاءُ الهويّةِ
#: بالفعلِ «spawn_agent» فيقفُ عندَ المستوى الثالثِ من زرِّ الإيقافِ (المادةُ الثامنة).
#: ولا يُسمَّى باسمٍ نطاقيٍّ هروبًا من الدستورِ: البوابةُ تعرفُ هذا الاسمَ فعلًا.
ACTION_SPAWN_AGENT = "spawn_agent"

#: نطاقُ مفتاحِ الذرّيّةِ لإنشاءِ الهويّةِ (1H): القيمةُ هي `agent_id` الكانونيُّ —
#: الهويةُ الواحدةُ لا تُنشأُ مرتَينِ لمفتاحٍ واحد.
IDENTITY_SPAWN_SCOPE = "agents.identity.spawn"


class AgentLifecycleState(StrEnum):
    """دورة حياة الوكيل — حقل واحد كانوني: `agents.status`.

    القيم تجمع ما كان موزَّعًا بين `agents.status` و`agent_population.state`
    قبل R4، حتى لا تبقى دورتا حياة لنفس الوكيل.
    """

    #: أُضيفَتْ في W-032 (Q-39 (ب)): وكيلٌ وصلَ بيانُه من الواجهةِ العامّةِ
    #: (`POST /v1/agents`) وصارَ يُحفَظُ في جدولِ `agents` بدلًا من قاموسٍ
    #: متطاير. وهي **خارجَ** `EMPLOYABLE_STATUSES` بقصدٍ: إدامةُ البيانِ ليست
    #: توزيعًا، ومنحُ نادِي الواجهةِ قدرةَ إدخالِ وكيلٍ إلى مُرشَّحي الموزِّعِ
    #: سلطةٌ لم يمنَحْها قرارٌ (السؤالُ مفتوحٌ · Q-41).
    DECLARED = "declared"
    REGISTERED = "registered"
    TRAINING = "training"
    TESTING = "testing"
    SPECIALIZED = "specialized"
    EMPLOYED = "employed"
    ACTIVE = "active"
    PROMOTED = "promoted"
    READY = "ready"
    PAUSED = "paused"
    RETIRED = "retired"


#: الحالات التي تُحتسب «خارج الخدمة» في الإسقاط السكّاني.
#: و`declared` فيها بحكمِ أنَّها لا تُوزَّعُ: وكيلٌ مُعلَنٌ ولمّا يُوظَّفْ ليس في
#: الخدمةِ، وعدُّه في الخدمةِ يُعطي رقمًا سكّانيًّا أكبرَ ممّا يملِكُه الموزِّعُ فعلًا.
OUT_OF_SERVICE_STATES = frozenset(
    {
        AgentLifecycleState.DECLARED.value,
        AgentLifecycleState.PAUSED.value,
        AgentLifecycleState.RETIRED.value,
    }
)


class DuplicateAgentIdentityError(RuntimeError):
    """محاولة إنشاء هوية بمعرّف موجود — الهوية لا تُنشأ مرّتين."""


class UnknownAgentIdentityError(RuntimeError):
    """لا هوية كانونية بهذا المعرّف — لا يُخترَع وكيل."""


class IdentityLedgerDivergenceError(RuntimeError):
    """سجلُّ الذرّيّةِ يقولُ «نجحت» وصفُّ الهويّةِ غائبٌ — تفرُّقٌ يُرفَعُ لا يُسكَتُ عنه.

    لا يُزعَمُ إنشاءٌ لم يقعْ، ولا يُعادُ الإنشاءُ خارجَ الحدِّ: الحالةُ تحتاجُ
    استعادةً (1H) لا تجاهلًا. وهو مُعلَنٌ حدٌّ لا يُبتلَعُ استثناءً عامًّا.
    """


@dataclass(frozen=True)
class AgentIdentity:
    """الهوية الكانونية كما هي في `agents` الآن."""

    agent_id: str
    name: str
    role: str
    lifecycle_state: str
    permissions: tuple[str, ...]
    allowed_tools: tuple[str, ...]
    token_budget: int
    tenant_id: str
    created_at: str | None = None

    @property
    def employable(self) -> bool:
        """هل الحالة تسمح بالتوزيع فعلًا؟ نفس مجموعة الموزِّع لا مجموعة موازية."""
        return self.lifecycle_state in EMPLOYABLE_STATUSES

    def as_dict(self) -> dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "role": self.role,
            "lifecycle_state": self.lifecycle_state,
            "permissions": list(self.permissions),
            "allowed_tools": list(self.allowed_tools),
            "token_budget": self.token_budget,
            "tenant_id": self.tenant_id,
            "created_at": self.created_at,
            "identity_source": CANONICAL_IDENTITY_TABLE,
        }


def new_agent_id() -> str:
    """معرّف مستقرّ لا يُشتقّ من الاسم — الاسم ليس هوية."""
    return f"agent-{uuid.uuid4().hex[:8]}"


def _to_identity(row: AgentModel) -> AgentIdentity:
    return AgentIdentity(
        agent_id=row.id,
        name=row.name,
        role=row.role,
        lifecycle_state=row.status or AgentLifecycleState.REGISTERED.value,
        permissions=tuple(row.permissions or []),
        allowed_tools=tuple(row.allowed_tools or []),
        token_budget=int(row.token_budget or 0),
        tenant_id=row.tenant_id or "default",
        created_at=row.created_at.isoformat() if row.created_at else None,
    )


def get_identity(agent_id: str, *, tenant_id: str | None = None) -> AgentIdentity | None:
    """قراءة الهوية الكانونية — `None` إن لم تكن مُسجَّلة."""
    session = get_session_factory()()
    try:
        query = session.query(AgentModel).filter(AgentModel.id == agent_id)
        if tenant_id is not None:
            query = query.filter(AgentModel.tenant_id == tenant_id)
        row = query.first()
        return _to_identity(row) if row else None
    finally:
        session.close()


def require_identity(agent_id: str, *, tenant_id: str | None = None) -> AgentIdentity:
    """قراءة الهوية أو سقوط صريح — لا وكيل مُختلَق."""
    identity = get_identity(agent_id, tenant_id=tenant_id)
    if identity is None:
        raise UnknownAgentIdentityError(f"لا هوية كانونية بهذا المعرّف: {agent_id}")
    return identity


def list_identities(
    *,
    lifecycle_state: str | None = None,
    tenant_id: str | None = None,
) -> list[AgentIdentity]:
    """كل الهويات الكانونية (بترتيب الإنشاء)."""
    session = get_session_factory()()
    try:
        query = session.query(AgentModel)
        if lifecycle_state:
            query = query.filter(AgentModel.status == lifecycle_state)
        if tenant_id is not None:
            query = query.filter(AgentModel.tenant_id == tenant_id)
        return [_to_identity(row) for row in query.order_by(AgentModel.created_at.asc()).all()]
    finally:
        session.close()


def _delete_identity_row(agent_id: str) -> bool:
    """حذفُ صفِّ هويةٍ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإنشاءِ (معوّضُ 1I).

    يعيدُ `False` إن لم يكنِ الصفُّ موجودًا: لا يُزعَمُ عكسُ أثرٍ لا وجودَ له.
    وهذا نطاقُهُ محصورٌ في صفِّ هذهِ العمليّةِ (مفتاحُ الذرّيّةِ من `agent_id`)،
    والقيدُ الأوليُّ في الجدولِ يمنعُ أن يكونَ الصفُّ لغيرِها أصلًا.
    """
    session = get_session_factory()()
    try:
        row = session.get(AgentModel, agent_id)
        if row is None:
            return False
        session.delete(row)
        session.commit()
        return True
    finally:
        session.close()


#: المُصرِّحُ الافتراضيُّ لإنشاءِ الهويّةِ — كائنٌ واحدٌ للوحدةِ يُبنى عندَ أوّلِ حاجةٍ
#: (W-532 · قرارُ المالكِ Q-62 ②: «يقارن الوكيل الكلفة … ويتبنى ما هو أسلم» — قِيسَ
#: أنَّ بناءَ المُصرِّحِ لكلِّ نداءٍ يبني حدًّا وسجلَّي ذرّيّةٍ وأذونٍ جديدةً فتنمو كلفةُ
#: النداءِ مع تراكمِ السجلِّ: 12.9 ← 19.6 ← 28.2 ms/op، والكائنُ الواحدُ ثابتٌ 9.5–11.4
#: · evidence/W-532). الفاعلُ مُسمّى صراحةً كما كان، والتمريرُ الصريحُ لـ`authorizer` باقٍ.
_DEFAULT_AUTHORIZER: ConstitutionalAuthorizer | None = None


def _default_authorizer() -> ConstitutionalAuthorizer:
    """المُصرِّحُ الافتراضيُّ بفاعلِ إنشاءِ الهويّةِ المُسمّى — واحدٌ للوحدةِ."""
    global _DEFAULT_AUTHORIZER
    if _DEFAULT_AUTHORIZER is None:
        _DEFAULT_AUTHORIZER = ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    return _DEFAULT_AUTHORIZER


def register_identity(
    agent_id: str,
    name: str,
    role: str,
    *,
    permissions: list[str] | None = None,
    allowed_tools: list[str] | None = None,
    lifecycle_state: str = AgentLifecycleState.REGISTERED.value,
    token_budget: int = 10_000,
    tenant_id: str = "default",
    authorizer: ConstitutionalAuthorizer | None = None,
) -> AgentIdentity:
    """إنشاء هوية كانونية جديدة — ترفض التكرار — عبر الحد السيادي منذ WI-082.

    الكتابةُ في `agents` لا تقعُ إلّا بإذنٍ دستوريٍّ بالفعلِ «spawn_agent» (قرارُ
    المالكِ Q-15 ①)، فيقفُ الإنشاءُ عندَ المستوى الثالثِ من زرِّ الإيقافِ (المادةُ
    الثامنة) ويعلنُ أثرَهُ ويحملُ معوّضًا حقيقيًّا ومفتاحَ ذرّيّةٍ من المعرِّفِ نفسِه.

    `authorizer` اختياريٌّ Named كما في `governance/factories.py` (السابقةِ P13):
    لا يغيّرُ سلوكَ مُنادٍ قائمٍ — من لا يمرّرُ مُصرِّحًا يُبنى له المبدئيُّ بفاعلٍ
    مسمّى، ولا يُبنى جسرٌ ثانٍ ولا بدائيّةٌ سياديّةٌ جديدة.

    Raises:
        DuplicateAgentIdentityError: المعرّف مُستخدَم فعلًا. التحديث يجري عبر
            `update_identity` صراحةً، لا عبر «تسجيل» صامت يمسح ما قبله.
        IdentityLedgerDivergenceError: سجلُّ الذرّيّةِ يُثبِتُ نجاحَ العمليّةِ
            وصفُّ الهويّةِ غائبٌ — استعادةٌ مطلوبةٌ لا إنشاءٌ يُزعَم.
    """
    actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
    # قاعدةُ نطاقٍ **قبلَ** الحدِّ (قراءةٌ لا كتابةٌ): رفضٌ مبكّرٌ صريحٌ للتكرارِ.
    # وهو ليس حمايةَ التزامنِ — ذاك قيدُ المفتاحِ الأوليُّ في الجدولِ — بل إبقاءُ
    # العقدِ القائمِ: المكرّرُ يُرفضُ قبلَ عبورِ الحدِّ لا بعده.
    session = get_session_factory()()
    try:
        existing = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        if existing is not None:
            raise DuplicateAgentIdentityError(f"هوية موجودة فعلًا بهذا المعرّف: {agent_id}")
    finally:
        session.close()

    target = f"agents/{agent_id}"
    effect = declared_effect("CREATE", target, f"هويةُ وكيلٍ «{name}» في السجلِّ الكانونيِّ الواحد")

    def _apply(_effect: Any) -> None:
        write_session = get_session_factory()()
        try:
            write_session.add(
                AgentModel(
                    id=agent_id,
                    name=name,
                    role=role,
                    status=lifecycle_state,
                    permissions=permissions or [],
                    allowed_tools=allowed_tools or [],
                    token_budget=token_budget,
                    tenant_id=tenant_id,
                )
            )
            write_session.commit()
        finally:
            write_session.close()

    guarded = actor_authorizer.guard_declared(
        ACTION_SPAWN_AGENT,
        target,
        declared_effects=(effect,),
        applier=_apply,
        operation_key=operation_key(IDENTITY_SPAWN_SCOPE, agent_id),
        compensators=(
            compensator(
                effect.signature,
                lambda: _delete_identity_row(agent_id),
                "حذفُ صفِّ الهويّةِ المُنشَأ — عكسٌ حقيقيٌّ للإنشاءِ",
            ),
        ),
    )
    if guarded.is_replay and get_identity(agent_id, tenant_id=tenant_id) is None:
        # العمليّةُ مُثبَتةٌ ناجحةٌ لهذا المفتاحِ: لا كتابةً ثانيةً ولا يُزعَمُ إنشاءٌ
        # جديدٌ. والصدقُ أن يُتحقَّقَ من أثرِها: الهويّةُ موجودةٌ فعلًا، أو الحالةُ
        # متفرّقةٌ فتُرفَعُ صريحةً ولا يُعادُ الإنشاءُ خارجَ الحدّ.
        raise IdentityLedgerDivergenceError(
            f"سجلُّ الذرّيّةِ يُثبِتُ إنشاءَ «{agent_id}» وصفُّ الهويّةِ غائبٌ — "
            "استعادةٌ مطلوبةٌ (1H) لا إنشاءٌ يُزعَم"
        )
    return require_identity(agent_id, tenant_id=tenant_id)


def update_identity(
    agent_id: str,
    *,
    name: str | None = None,
    role: str | None = None,
    permissions: list[str] | None = None,
    allowed_tools: list[str] | None = None,
    token_budget: int | None = None,
) -> AgentIdentity:
    """تعديل صريح لهوية قائمة — لا يُنشئ هوية جديدة."""
    session = get_session_factory()()
    try:
        row = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        if row is None:
            raise UnknownAgentIdentityError(f"لا هوية كانونية بهذا المعرّف: {agent_id}")
        if name is not None:
            row.name = name
        if role is not None:
            row.role = role
        if permissions is not None:
            row.permissions = permissions
        if allowed_tools is not None:
            row.allowed_tools = allowed_tools
        if token_budget is not None:
            row.token_budget = token_budget
        session.commit()
    finally:
        session.close()
    return require_identity(agent_id)


def set_lifecycle_state(agent_id: str, lifecycle_state: str) -> bool:
    """تغيير دورة الحياة في الحقل الكانوني الوحيد.

    Returns:
        False إن لم تكن هناك هوية كانونية بهذا المعرّف — بلا إنشاء ضمني.
    """
    session = get_session_factory()()
    try:
        row = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        if row is None:
            return False
        row.status = lifecycle_state
        session.commit()
        return True
    finally:
        session.close()


def _runtime_activity(limit: int = 500) -> dict[str, Any]:
    """آخر طور تشغيل لكل وكيل من أحداث دورة الحياة (R3) — لا تخمين.

    إن لم تُرصَد أحداث بعد فالحقول تُعلَن `observed=False` بدل تصفيرها كأنها
    قياس. `executing`/`failed` لا تُشتقّ من `agents.status` لأن الحالة هناك
    حالة تعيين لا حالة تنفيذ لحظي.
    """
    from amos_federation.common.event_bus import get_event_bus

    events = get_event_bus().get_events(subject=RUNTIME_ACTIVITY_SUBJECT, limit=limit)
    latest: dict[str, str] = {}
    for event in events:  # الأحداث تعود من الأحدث إلى الأقدم
        data = event.get("data") or {}
        agent_id = str(data.get("agent_id", ""))
        phase = str(data.get("phase", ""))
        if agent_id and agent_id not in latest:
            latest[agent_id] = phase
    phases: dict[str, int] = {}
    for phase in latest.values():
        phases[phase] = phases.get(phase, 0) + 1
    return {
        "observed": bool(events),
        "events_scanned": len(events),
        "agents_with_activity": len(latest),
        "by_phase": phases,
        "source": RUNTIME_ACTIVITY_SUBJECT,
    }


def population_projection(*, tenant_id: str | None = None) -> dict[str, Any]:
    """سكّان النظام كإسقاط للسجل الكانوني — لا سجل هوية ثانٍ.

    ما هو مقيس فعلًا: `total` وتوزيع دورة الحياة (منها active وretired وidle
    = مُعيَّن ولا نشاط تشغيل مرصود). ما ليس مقيسًا من الهوية: `executing` و
    `failed` — يُقرآن من أحداث دورة الحياة، ويُعلَن `observed=False` إن لم
    تُسجَّل أحداث بعد. لا يُختلق رقم غير متوفّر.
    """
    identities = list_identities(tenant_id=tenant_id)
    by_state: dict[str, int] = {}
    for identity in identities:
        by_state[identity.lifecycle_state] = by_state.get(identity.lifecycle_state, 0) + 1
    activity = _runtime_activity()
    executing = activity["by_phase"].get("executing", 0)
    failed = activity["by_phase"].get("failed", 0)
    employable = sum(1 for identity in identities if identity.employable)
    return {
        "total": len(identities),
        "by_lifecycle_state": by_state,
        "active": by_state.get(AgentLifecycleState.ACTIVE.value, 0),
        "retired": by_state.get(AgentLifecycleState.RETIRED.value, 0),
        "paused": by_state.get(AgentLifecycleState.PAUSED.value, 0),
        "employable": employable,
        "idle": max(employable - executing, 0),
        "executing": executing if activity["observed"] else None,
        "failed": failed if activity["observed"] else None,
        "runtime_activity": activity,
        "identity_source": CANONICAL_IDENTITY_TABLE,
        "projection_of": CANONICAL_IDENTITY_TABLE,
        "fidelity": POPULATION_FIDELITY,
    }


def identity_health(*, tenant_id: str | None = None) -> dict[str, Any]:
    """صحّة طبقة الهوية والسكّان — مبنيّة على مكوّنات حقيقية لا على «العملية تعمل».

    تُفحَص ثلاثة مكوّنات فعليًّا: قابلية قراءة السجل الكانوني، وناقل الأحداث،
    وتناسق الإسقاط (صفوف `agent_population` بلا هوية كانونية = دَين توفيق).
    أي مكوّن غير متوفّر يُعلَن `unavailable`، ولا تُعلَن الطبقة `healthy` إلا
    إذا نجحت الفحوص الحقيقية كلها.
    """
    components: dict[str, dict[str, Any]] = {}

    try:
        identities = list_identities(tenant_id=tenant_id)
        components["canonical_registry"] = {
            "status": "available",
            "agents": len(identities),
            "table": CANONICAL_IDENTITY_TABLE,
        }
    except Exception as exc:  # noqa: BLE001 — تُعلَن كغير متوفّرة لا تُخفى
        components["canonical_registry"] = {"status": "unavailable", "error": str(exc)}

    try:
        from amos_federation.common.event_bus import get_event_bus

        components["event_bus"] = {
            "status": "available",
            "lifecycle_events": len(
                get_event_bus().get_events(subject=RUNTIME_ACTIVITY_SUBJECT, limit=1)
            ),
        }
    except Exception as exc:  # noqa: BLE001
        components["event_bus"] = {"status": "unavailable", "error": str(exc)}

    try:
        # R4 (OPTION 2): «بلا هوية كانونية» ليس خللًا بحدّ ذاته. القاعدة الحقيقية
        # تحمل 5116 صفًّا سكّانيًّا بـ24 اسمًا متميزًا، أي بذر مكرّر لا هويّات. عدّها
        # دَين توفيق كان يُثبِّت `degraded` إلى الأبد فيفقد المقياس معناه. الخلل
        # الحقيقي: صفّ **ذو دليل تاريخي** لا يراه مسار التنفيذ. والعدد الكلّي
        # يُعلَن معه ولا يُخفَى.
        from amos_federation.services.agent_runtime.population import (
            legacy_seed_profiles,
            reconciliation_debt,
            unmigrated_profiles,
        )

        orphans = unmigrated_profiles()
        debt = reconciliation_debt()
        components["population_projection"] = {
            "status": "available" if not debt else "degraded",
            "unmigrated_profile_rows": len(orphans),
            "reconciliation_debt_rows": len(debt),
            "legacy_seed_rows": len(legacy_seed_profiles()),
            "table": PROJECTION_TABLE,
        }
    except Exception as exc:  # noqa: BLE001
        components["population_projection"] = {"status": "unavailable", "error": str(exc)}

    statuses = {component["status"] for component in components.values()}
    if "unavailable" in statuses:
        overall = "unavailable"
    elif "degraded" in statuses:
        overall = "degraded"
    else:
        overall = "healthy"
    return {
        "status": overall,
        "components": components,
        "basis": "component_checks",
        "fidelity": POPULATION_FIDELITY,
    }
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w574/gemini_3_8_flash/repo && cat federal/executive/services/tests/test_wi082_agent_identity_sovereign.py
EXIT: 0
BYTES: 13510
SHA256: 42b5eb60ef647f549b29c4383ef3cb52bc30214be70e404ec429b0261bdc7121
NO_EOL: 0
--- OUTPUT ---
"""WI-082 — هجرة `register_identity` عبرَ الحدِّ السياديِّ بفعلِ «spawn_agent».

الهدف: إثباتُ أنَّ إنشاءَ الهويّةِ يعبرُ الحدَّ السياديَّ بالفعلِ «spawn_agent» (قرارُ
       المالكِ Q-15 ① · القيدُ W-385) فيقفُ عندَ المستوى الثالثِ من زرِّ الإيقافِ
       (المادةُ الثامنة · R-008-2)، وأنّ عقدَ المُنادي القائمَ لم يتغيّرْ: نفسُ
       الإرجاعِ للناجحِ ونفسُ الرفضِ للمكررِ، وأنّ الطفرةَ (تبديلُ الفعلِ إلى
       register_agent) تُسقِطُ الفحصَ لا تصمتُ عنه.
النطاق: قياسُ سلوكِ `register_identity` عبرَ الحدِّ وحدَه — لا تعديلَ للبوابةِ ولا
        للقواعدِ الدستوريّةِ. وحقنُ مستوى زرِّ الإيقافِ في الطلبِ محاكاةٌ لحالةِ الزرِّ
        معلَنةٌ هنا لا تجاوزٌ للبوّابةِ.
المالك: federal/executive/services — WI-082 (بقرارِ المالكِ Q-15 · وتوجيهِ المستشارِ 8)
تاريخ الإنشاء: 2026-10-17 (W-402 · WI-082)

قرارُ المالكِ Q-15 ① (2026-10-15 · القيدُ W-385): إنشاءُ الهويّةِ يُعلَنُ بالفعلِ
`spawn_agent` — فيقفُ عندَ المستوى الثالثِ من زرِّ الإيقافِ (المادةُ الثامنة،
R-008-2: `KILL_SWITCH_BLOCKS[3]`). والسابقةُ المعماريّةُ `governance/factories.py`
(P13): معاملٌ مسمّىً اختياريٌّ `authorizer` لا يغيّرُ سلوكَ مُنادٍ قائم.

الحدُّ المُعلَنُ في هذا الفحصِ:
- اختبارُ المستوى 3 يحقنُ `kill_switch_level=3` في الطلبِ عبرَ مصدّ مُصرِّحٍ
  محليٍّ (محاكاةُ حالةِ الزرِّ في الطلبِ لا تعديلٌ للفعلِ) — لأنَّ لا مسارَ
  إنتاجيًّا اليومَ يضخُّ المستوى في الطلبِ، وتلك مسجّلةٌ اكتشافًا مستقلًّا
  (DISC-099 · WI-085).
- لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذِ (§ 4.3) — هذا ملفُّ قياسٍ لا حُكمِ مراجعة.

الدليلُ المُعادُ تشغيلُه:
    .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
"""

from __future__ import annotations

import dataclasses
from typing import Any

import pytest

from amos_federation.services.executive_core.agent_identity import (
    ACTION_SPAWN_AGENT,
    AGENT_IDENTITY_ACTOR,
    DuplicateAgentIdentityError,
    IdentityLedgerDivergenceError,
    _delete_identity_row,
    register_identity,
)
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from tests.conftest import purge_agents

#: الوكيلُ الذي يُبنى افتراضيًّا بلا مُصرِّحٍ مُمرَّر — القيمةُ المقيسةُ من الطلبِ
#: المُصنَّعِ للحدِّ لا تخمينًا.
EXPECTED_DEFAULT_ACTOR = "EXECUTIVE"


class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجل كل نتيجة محروسة — لأجل قياس الاعتمادية، لا لاتخاذ قرار."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.results.append(guarded)
        return guarded


class KillSwitchLevelAuthorizer(ConstitutionalAuthorizer):
    """المُصرِّحُ نفسُهُ وطلبُهُ يحملُ مستوى زرِّ الإيقافِ.

    محاكاةُ **حالةِ الزرِّ** في الطلبِ لا تعديلٌ للفعلِ ولا تجاوزٌ للبوّابةِ:
    الطلبُ يمرُّ في المسارِ السياديِّ كاملًا، والقاعدةُ R-008-2 هي التي تنطقُ.
    """

    def __init__(self, level: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._kill_switch_level = level

    def _request(
        self,
        action: str,
        target: str,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        request = super()._request(action, target, metadata)
        return dataclasses.replace(request, kill_switch_level=self._kill_switch_level)


@pytest.fixture(autouse=True)
def _fresh_agents() -> None:
    """قاعدة نظيفة — القياس على سجل حقيقي لا على بقايا (نمط test_r4)."""
    from amos_federation.common.database import get_session_factory, init_db
    from tests.conftest import purge_tasks

    init_db()
    session = get_session_factory()()
    try:
        purge_tasks(session)
        purge_agents(session)
        session.commit()
    finally:
        session.close()


# ── 1. النجاح عبرَ الحدِّ — نفسُ الإرجاعِ، والكتابةُ بإذنٍ ─────────────────────


def test_wi082_1_register_crosses_boundary_and_returns_same_contract() -> None:
    authorizer = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    identity = register_identity(
        "wi082-success",
        "وكيل WI-082",
        "worker",
        permissions=["task:execute"],
        allowed_tools=["python_execute"],
        authorizer=authorizer,
    )

    # نفسُ عقدِ الإرجاعِ القائمِ: هويةٌ كانونيّةٌ كاملةٌ لا بنيةٌ جديدة.
    assert identity.agent_id == "wi082-success"
    assert identity.name == "وكيل WI-082"
    assert identity.role == "worker"

    # والصكُّ المُلزِمُ مُسجَّلٌ: عبورٌ واحدٌ بدليلِهِ الحرفيِّ — الفعلُ والهدفُ
    # والقرارُ وبصمةُ السجلِّ، لا وعدٌ بأنَّ «الحدَّ عُبر».
    assert len(authorizer.results) == 1
    evidence = authorizer.results[0].evidence.as_dict()
    assert evidence["action"] == "spawn_agent"
    assert evidence["target"] == "agents/wi082-success"
    assert evidence["decision"] == "ALLOW"
    assert evidence["ledger_entry_hash"]
    assert evidence["request_fingerprint"]

    from amos_federation.services.executive_core.agent_identity import require_identity

    stored = require_identity("wi082-success")
    assert stored.agent_id == identity.agent_id


# ── 2. المكررُ يُرفضُ قبلَ الحدِّ — لا عبورَ ولا كتابةً ───────────────────────


def test_wi082_2_duplicate_rejected_before_boundary() -> None:
    authorizer = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    register_identity("wi082-dup", "وكيل أول", "worker", authorizer=authorizer)

    with pytest.raises(DuplicateAgentIdentityError):
        register_identity("wi082-dup", "وكيل ثانٍ", "worker", authorizer=authorizer)

    # العقدُ القائمُ: المكررُ لا يعبُرُ الحدَّ أصلًا (رفضٌ مبكّرٌ صريحٌ).
    assert len(authorizer.results) == 1


# ── 3. المستوى 3 من زرِّ الإيقافِ يجمّدُ الإنشاءَ — وهذا مضمونُ الفحصِ ──────


def test_wi082_3_kill_switch_level_3_blocks_spawn_agent() -> None:
    authorizer = KillSwitchLevelAuthorizer(level=3, actor=AGENT_IDENTITY_ACTOR)
    from core.sovereignty.gateway import SovereigntyViolation  # داخل الفحص: الجسرُ يُتاحُ أولًا

    with pytest.raises(SovereigntyViolation) as excinfo:
        register_identity(
            "wi082-halted",
            "وكيل مُجمَّد",
            "worker",
            authorizer=authorizer,
        )

    # القاعدةُ R-008-2 تنطقُ باسمِ الفعلِ نفسِهِ: «spawn_agent» مُجمَّدٌ من
    # المستوى الثالثِ. وهذا هو القيدُ الذي تُسقِطُهُ طفرةُ تغييرِ الاسمِ.
    message = str(excinfo.value)
    assert "spawn_agent" in message
    assert "المستوى 3" in message

    # والرفضُ منعٌ حقيقيٌّ لا شكليٌّ: لا صفَّ هويةٍ كُتِبَ.
    from amos_federation.services.executive_core.agent_identity import get_identity

    assert get_identity("wi082-halted") is None


def test_wi082_4_level_below_3_does_not_block() -> None:
    """المستويانِ 1 و2 لا يجمّدانِ spawn_agent — التجميدُ من الثالثِ حصرًا.

    هذا هو الوجهُ الآخرُ للطفرةِ: لو عُدِّلَ القيدُ في `rules.py` (مجموعةُ
    المستوى الثالثِ) فسيُسقِطُ هذا الفحصُ — فلا يُزعَمُ تجميدٌ لا تُقيسُهُ بوّابةٌ.
    """
    authorizer = KillSwitchLevelAuthorizer(level=2, actor=AGENT_IDENTITY_ACTOR)
    identity = register_identity(
        "wi082-level2",
        "وكيل تحت المستوى الثاني",
        "worker",
        authorizer=authorizer,
    )
    assert identity.agent_id == "wi082-level2"


# ── 4. المعوّضُ عكسٌ حقيقيٌّ لا زعمٌ ─────────────────────────────────────────


def test_wi082_5_compensator_reverses_real_row() -> None:
    register_identity(
        "wi082-compensate",
        "وكيل المعوّض",
        "worker",
        authorizer=ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR),
    )

    # عكسٌ لأثرٍ موجودٍ: حذفٌ حقيقيٌّ وإعادةُ True.
    assert _delete_identity_row("wi082-compensate") is True
    from amos_federation.services.executive_core.agent_identity import get_identity

    assert get_identity("wi082-compensate") is None

    # ولا يُزعَمُ عكسُ أثرٍ لا وجودَ لهُ: الصفُّ غائبٌ فالعودةُ False.
    assert _delete_identity_row("wi082-compensate") is False


# ── 5. الإعادةُ بعدَ حذفِ الصفِّ: تفرُّقٌ صريحٌ لا إنشاءٌ يُزعَم ──────────────


def test_wi082_6_replay_with_missing_row_raises_divergence() -> None:
    authorizer = ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    register_identity(
        "wi082-replay",
        "وكيل الإعادة",
        "worker",
        authorizer=authorizer,
    )

    # حذفُ الصفِّ خارجَ العمليّةِ (كما يفعلُ تفريغُ الاختباراتِ): سجلُّ الذرّيّةِ
    # يُثبِتُ النجاحَ والصفُّ غائبٌ — تفرُّقٌ لا يُسكَتُ عنهُ ولا يُعادُ الإنشاءُ
    # خارجَ الحدِّ ولا يُزعَمُ نجاحٌ لم يقعْ.
    _delete_identity_row("wi082-replay")

    with pytest.raises(IdentityLedgerDivergenceError):
        register_identity(
            "wi082-replay",
            "وكيل الإعادة",
            "worker",
            authorizer=authorizer,
        )


# ── 6. المسارُ الافتراضيُّ بلا مُصرِّحٍ مُمرَّرٍ: يعملُ كالمُنادي القائمِ ─────


def test_wi082_7_default_authorizer_path_unchanged() -> None:
    """بلا `authorizer` يُبنى المبدئيُّ بفاعلٍ مسمّى — لا جسرٌ ثانٍ ولا سلوكٌ جديد.

    (يستعملُ سجلَّ الذرّيّةِ المُتاحَ في بيئةِ الاختبارِ — انظر `conftest.py`.)
    """
    identity = register_identity(
        "wi082-default-path",
        "وكيل المسار الافتراضي",
        "worker",
    )
    assert identity.agent_id == "wi082-default-path"
    assert AGENT_IDENTITY_ACTOR == EXPECTED_DEFAULT_ACTOR
    assert ACTION_SPAWN_AGENT == "spawn_agent"


def test_wi082_8_default_authorizer_is_one_per_module() -> None:
    """بلا `authorizer` يُستعمَلُ كائنٌ واحدٌ للوحدةِ لا كائنٌ لكلِّ نداءٍ (W-532 · Q-62 ②).

    القياسُ (evidence/W-532): البناءُ لكلِّ نداءٍ تنمو كلفتُهُ مع تراكمِ السجلِّ — فالاختيارُ
    يُحرَسُ هنا: نداءانِ بلا مُصرِّحٍ يمرّانِ بالكائنِ نفسِهِ، وفاعلُهُ هو المُسمّى.
    """
    from amos_federation.services.executive_core import agent_identity as module

    seen: list[int] = []
    original = ConstitutionalAuthorizer.guard_declared

    def spy(self: ConstitutionalAuthorizer, *args: Any, **kwargs: Any) -> Any:
        seen.append(id(self))
        return original(self, *args, **kwargs)

    ConstitutionalAuthorizer.guard_declared = spy  # type: ignore[method-assign]
    try:
        register_identity("wi082-one-auth-a", "وكيل أ", "worker")
        register_identity("wi082-one-auth-b", "وكيل ب", "worker")
    finally:
        ConstitutionalAuthorizer.guard_declared = original  # type: ignore[method-assign]
    assert len(seen) == 2
    assert seen[0] == seen[1], "المُصرِّحُ الافتراضيُّ بُنيَ لكلِّ نداءٍ"
    assert module._default_authorizer()._actor == EXPECTED_DEFAULT_ACTOR
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: find /home/user/workspace/council_w574/gemini_3_8_flash -maxdepth 1
EXIT: 0
BYTES: 277
SHA256: d4baa6514fe3197c879e4f8fc3bc09119e0a410a119a20c093b29d377e00369a
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w574/gemini_3_8_flash
/home/user/workspace/council_w574/gemini_3_8_flash/repo
/home/user/workspace/council_w574/gemini_3_8_flash/BRIEF.md
/home/user/workspace/council_w574/gemini_3_8_flash/tmp
/home/user/workspace/council_w574/gemini_3_8_flash/raw
=== RAW [15] END ===
VERDICT_PER_CRITERION:
- المعيار (1) قبل الشفرة: أثر إلزام الدوال الثلاث بـ AuthorizationContext مقيس في evidence/W-390/ مع عقد بلا كسر، وتسمية الدالتين الأخريين معلقة كـ PENDING_OWNER: نعم (الكتل [4] و[5] و[6] و[13]).
- المعيار (2) register_identity يعبر الحد السيادي بالفعل spawn_agent ويرفض عند المستوى 3، وطفرة تبديل الفعل إلى register_agent تسقط الفحص برمز خروج EXIT: 1 وسقوط 3 فحوص: نعم (الكتل [6] و[7] و[8] و[9] و[10]).
- المعيار (3) دين agent_identity.py انخفض من 3 إلى 2 (register_identity وحده) ودين D-4 انخفض من 184 إلى 183 بلا نمو في غيره: نعم (الكتلة [3]).
- المعيار (4) حزمة services كاملة خضراء (1475 passed و 53 skipped) وملف test_q3_branch_declaration_surface.py ناجح (10 passed): نعم (الكتلتان [11] و[12]).
- المعيار (5) مراجعة مستقلة تعيد التشغيل حرفياً بكل الأوامر الملتقطة خاماً: نعم (الكتل [1] إلى [15]).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: أقرُّ بأنّني لم أقرأْ شيئًا خارجَ استنساخي وهذهِ الإحاطةِ، وأنّ جميعَ الأوامرِ جرى تشغيلُها فعليًّا داخلَ دليلي الخاصِّ /home/user/workspace/council_w574/gemini_3_8_flash، والمخرجاتُ التُقِطَت خامًا كاملةً بلا أيِّ تحريرٍ أو تدخّلٍ يدويٍّ، وقاعدةُ البياناتِ والملفّاتُ المؤقّتةُ كلُّها داخلَ الدليلِ لا تحتَ /tmp.
VERDICT: PASS
