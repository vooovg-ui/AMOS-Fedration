# حكمُ مقعدِ المجلسِ — grok_4_7 (عائلةُ xAI · Grok) · جولةُ WI-096 (W-521)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-096 (بروتوكولُ Q-59 · بندُ WI-100) — لا تحريرَ ولا تلخيصَ.

## النطاق
حكمُ مقعدٍ واحدٍ على البندِ WI-096 بإحاطةِ W-520 المصحّحةِ (sha256 `09b9383791a2e430f362d53ae73767e5a56449bcbe35cd214505d09df41744b9`) عندَ العقدةِ `c7d1436a14088465e79131599cb4e3f36f62520a`.

## المالك
بندُ WI-100 (المنسِّقُ: Perplexity Computer · النموذجُ المنسِّقُ الحاضرُ GLM-5.3 كما أعلنتْهُ المنصةُ — منسِّقٌ لا مُصوِّتٌ).

## تاريخ الإنشاء
2026-10-19

## تاريخ آخر تعديل
2026-10-19 (W-521 — حُفظَ بعدَ اكتمالِ الأحكامِ الثلاثةِ كلِّها · § 2.3)

## المحتويات

- **النموذجُ كما أطلقتْهُ المنصةُ:** `grok_4_7` (عائلةُ xAI · Grok) · الإصدارُ التفصيليُّ غيرُ معروضٍ من المنصةِ.
- **دليلُ الاستنساخِ:** خارجَ المستودعِ عندَ المنسِّقِ (حُفظَتِ الأحكامُ منه إلى هنا).

نصُّ الحكمِ كما وردَ (حرفيًّا):

````
MODEL: grok_4_7
FAMILY: xAI · Grok
RUN_DATE: 2026-10-19 18:42 +00:00
NODE: c7d1436a14088465e79131599cb4e3f36f62520a
CLONE_PATH: /home/user/workspace/council-w521/grok/AMOS-Fedration
COMMANDS_RUN: |
  1) git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council-w521/grok/AMOS-Fedration
     && git checkout c7d1436a14088465e79131599cb4e3f36f62520a
     && git rev-parse HEAD
  2) bash tools/dev/bootstrap.sh
  3) .venv/bin/python -m pytest tests/sovereignty/test_idempotency.py tests/sovereignty/test_idempotency_append_log.py tests/governance/test_w034_runtime_state_identity.py -q
  4) .venv/bin/python docs/audit/evidence/W-471/mutation_harness.py
  5) git log --oneline --follow docs/audit/DISC105_IDEMPOTENCY_APPEND_DESIGN.md
  6) git log --oneline --follow core/sovereignty/idempotency.py
  7) git log --oneline --follow docs/audit/evidence/W-492/review.txt
  8) git rev-parse 1f4a649
     && git merge-base --is-ancestor 1f4a64978d68d8f2405564062bdf851b37844f1b c7d1436a14088465e79131599cb4e3f36f62520a && echo ANCESTOR_OK
  9) بعد (عقدة المراجعة كما هي):
     cp docs/audit/evidence/W-472/bench_curve.py federal/executive/services/tests/test_zz_bench_curve.py
     && .venv/bin/python -m pytest federal/executive/services/tests/test_zz_bench_curve.py -q -s
     && rm federal/executive/services/tests/test_zz_bench_curve.py
  10) تفكيك cProfile على عقدة المراجعة (الأمر كما كُتب — مرة واحدة على «بعد»):
      cp docs/audit/evidence/W-472/bench_profile.py federal/executive/services/tests/test_zz_bench_profile.py
      && .venv/bin/python -m pytest federal/executive/services/tests/test_zz_bench_profile.py -q -s
      && rm federal/executive/services/tests/test_zz_bench_profile.py
  11) قبل (الشجرة نفسها):
      git checkout f4902232e902cd6a28b5b68b5594c2a796eb04b4 -- core/sovereignty/idempotency.py
      ثم إعادة أمر المنحنى أعلاه
      ثم git checkout HEAD -- core/sovereignty/idempotency.py
  أوامر إضافية (ليست بديلاً عن أوامر الإحاطة — وُسمت ADDITIONAL في المخرجات):
  A) على checkout «قبل» نفسه وقبل الاستعادة: أمر bench_profile.py (لقياس هيمنة _atomic_write وزوالها على الجهاز نفسه)
  B) بعد الاستعادة: إعادة منحنى «بعد» مرة ثانية لقياس ضوضاء النسبة
  C) git cat-file -e cacd1a7^:docs/audit/DISC105_IDEMPOTENCY_APPEND_DESIGN.md
     && git merge-base --is-ancestor 1f4a64978d68d8f2405564062bdf851b37844f1b 63b1a3f052e769a5be8e164f85382e38c26ecdb0
RAW_OUTPUTS: |
  --- 1 clone+checkout ---
  EXIT: 0
  date -u at start: 2026-10-19 18:34 +0000
  git rev-parse HEAD:
  c7d1436a14088465e79131599cb4e3f36f62520a
  HEAD detached at c7d1436
  nothing to commit, working tree clean
  c7d1436 W-518: قيدُ جسرٍ (واجبُ N+1) — § 7/6 على عقدةِ دفعةِ W-515/W-516 (f85de5f): التشغيلُ 39257606426 ⇒ مقروءٌ أخضرُ 13/13 · exit 0 — لا شِفرةَ ولا عملَ · توثيقٌ وحدَه (سابقةُ W-495)

  --- 2 bootstrap ---
  EXIT: 0
  • الجذر: /home/user/workspace/council-w521/grok/AMOS-Fedration
  • ثُبِّتَ خُطّافُ pre-push (يُشغِّلُ حرسَ ما قبلَ الدفعِ على كلِّ دفعٍ — WI-078)
  • إنشاءُ بيئةٍ معزولةٍ في .venv
  • تركيبُ تبعيّاتِ الجذر (requirements-dev.txt)
  • تركيبُ حزمةِ الخدماتِ (قد تطولُ: تبعيّاتٌ كثيرة)
  • تركيبُ ruff==0.6.9 (‏المُثبَّتُ في .github/workflows/ci.yml)
  ✓ البيئةُ جاهزة. للتنشيطِ في جلسةٍ جديدة: source .venv/bin/activate
  BOOTSTRAP_EXIT:0

  --- 3 pytest حرس الذرّيّة ---
  EXIT: 0
  ........................................................................ [ 73%]
  ..........................                                               [100%]
  98 passed in 2.53s
  PYTEST_EXIT:0

  --- 4 mutation_harness.py ---
  EXIT: 0
  خطُ الأساسِ أخضرُ ({'failures': 0, 'errors': 0, 'killed': False}) — الحصادُ يبدأُ
  قتلتها  — M1_حذف_flock: failures=1 errors=0 القاتلُ=tests/sovereignty/test_idempotency_append_log.py::TestProcessLock::test_concurrent_processes_lose_no_event
  قتلتها  — M2_فتح_بوضع_w_يمحو: failures=21 errors=0 القاتلُ=tests/sovereignty/test_idempotency_append_log.py::TestAppendLogShape::test_each_event_is_one_line
  قتلتها  — M3_قراءة_الذيل_الممزق_كاملًا: failures=3 errors=0 القاتلُ=tests/sovereignty/test_idempotency_append_log.py::TestCrashSafety::test_torn_tail_is_ignored_and_retried
  قتلتها  — M4_حذف_فحص_البصمة: failures=2 errors=0 القاتلُ=tests/sovereignty/test_idempotency_append_log.py::TestMigration::test_reuse_with_different_fingerprint_still_refused
  قتلتها  — M5_تعطيل_الضغط: failures=1 errors=0 القاتلُ=tests/sovereignty/test_idempotency_append_log.py::TestCompaction::test_log_grows_asymptotically_not_linearly
  قتلتها  — M6_الضغط_يُسقِط_المفاتيح: failures=3 errors=0 القاتلُ=tests/sovereignty/test_idempotency_append_log.py::TestAppendLogShape::test_replacement_rebuilds_state_regardless_of_size
  قتلتها  — M7_الترحيل_يُفرِغُ_المحتوى_القديم: failures=1 errors=0 القاتلُ=tests/sovereignty/test_idempotency_append_log.py::TestMigration::test_legacy_json_object_is_migrated_once
  قتلتها  — M8_إلحاق_بلا_تحديثِ_الذاكرةِ: failures=53 errors=0 القاتلُ=tests/sovereignty/test_idempotency_append_log.py::TestAppendLogShape::test_each_event_is_one_line
  بعدَ الاستعادةِ: أخضرُ ({'failures': 0, 'errors': 0, 'killed': False})
  ALL_KILLED = True
  MUTATION_EXIT:0
  أثر جانبي: الحاصد أعاد كتابة ملفات متتبَّعة تحت docs/audit/evidence/W-471/mutation_runs/ (M1..M8 وbaseline وrestored و_junit_0.xml). لم أُعدِّل الشفرة يدويًا. blob ملف idempotency.py بعد الحاصد = blob العقدة (7ff2c5c5e7c5e93e38cdb74f58a3590c09b420b1).

  --- 5 git log --follow design doc ---
  EXIT: 0
  3c263e3 W-477: تصحيحاتُ مراجعةِ المستشارِ — هويّةُ الملفِّ · قفلُ القراءةِ · ردُّ حارسِ التلفِ · حاصدٌ في المستودعِ · معيارٌ لا يقبلُ التدهورَ
  cacd1a7 W-471: WI-096 — الوثيقةُ ثمَّ الشِفرةُ: سجلٌّ إلحاقيٌّ JSONL لملفِ الذرّيّةِ (flock + ضغطٌ دوريٌّ) + فحوصٌ وطفراتٌ 8/8 + إصلاحُ رأسِ السجلِّ
  DESIGN_LOG_EXIT:0

  --- 6 git log --follow idempotency.py ---
  EXIT: 0
  a8b8118 W-490: تصحيحاتُ المراجعةِ الثالثةِ — كشفُ الترحيلِ من البايتاتِ · عقدُ السجلِّ · فحصُ الساعةِ الحقيقيُّ · حاصدُ JUnit
  6e5fe92 W-489: تصحيحاتُ المراجعةِ الثانيةِ — الفحوصُ الفعليةُ · record=null · الحاصدُ بخطِّ أساسٍ · فحصُ عمرِ الرمزِ · سحبُ تمديدِ DISC-094 غيرِ المأذونِ
  3c263e3 W-477: تصحيحاتُ مراجعةِ المستشارِ — هويّةُ الملفِّ · قفلُ القراءةِ · ردُّ حارسِ التلفِ · حاصدٌ في المستودعِ · معيارٌ لا يقبلُ التدهورَ
  cacd1a7 W-471: WI-096 — الوثيقةُ ثمَّ الشِفرةُ: سجلٌّ إلحاقيٌّ JSONL لملفِ الذرّيّةِ (flock + ضغطٌ دوريٌّ) + فحوصٌ وطفراتٌ 8/8 + إصلاحُ رأسِ السجلِّ
  78f0d9f W-034 · Q-40 (ج): بطاقةُ هويّةٍ لأثرِ التشغيلِ في موضعِ الكتابةِ لا في الكاشف
  b97f0cb STAGE 1H — الذرّيّةُ ومنعُ تكرارِ الأثر
  IDEM_LOG_EXIT:0

  --- 7 git log --follow review.txt ---
  EXIT: 0
  1f4a649 W-492: قيدُ مراجعةِ المستشارِ التي أعادتِ التشغيلَ (نصٌّ حرفيٌّ) + DISC-106/107 + WI-098
  REVIEW_LOG_EXIT:0

  --- 8 merge-base --is-ancestor review commit vs review node ---
  EXIT: 0
  git rev-parse 1f4a649:
  1f4a64978d68d8f2405564062bdf851b37844f1b
  ANCESTOR_OK
  ANCESTOR_EXIT:0

  --- 9 bench curve AFTER (review node, specified command) ---
  EXIT: 0
  CURVE_TIMES: [0.196, 0.131, 0.131, 0.134, 0.133, 0.136, 0.138, 0.138, 0.139, 0.146, 0.147, 0.212]
  FILE_SIZES: [39981, 79061, 118141, 157221, 196301, 235381, 274461, 313541, 352621, 391701, 430781, 469861]
  RATIO: 1.62
  JSON: {"times": [0.196, 0.131, 0.131, 0.134, 0.133, 0.136, 0.138, 0.138, 0.139, 0.146, 0.147, 0.212], "sizes": [39981, 79061, 118141, 157221, 196301, 235381, 274461, 313541, 352621, 391701, 430781, 469861]}
  1 passed in 2.17s
  BENCH_AFTER_EXIT:0
  BENCH_COPY_REMOVED

  --- 10 cProfile AFTER (specified command, review node) ---
  EXIT: 0
  PROFILE_OUTPUT:
           307973 function calls (304160 primitive calls) in 0.271 seconds

     Ordered by: cumulative time
     List reduced from 1120 to 30 due to restriction <30>

     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
          1    0.000    0.000    0.271    0.271 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/agent_runtime/population.py:214(seed_initial_population)
         20    0.000    0.000    0.271    0.014 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/agent_runtime/population.py:170(register_agent)
         20    0.000    0.000    0.218    0.011 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py:269(register_identity)
         20    0.000    0.000    0.142    0.007 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:355(guard_declared)
         20    0.000    0.000    0.128    0.006 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement_boundary.py:291(execute)
         20    0.000    0.000    0.099    0.005 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:866(run_once)
         20    0.000    0.000    0.099    0.005 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:894(_run_once_inner)
         20    0.000    0.000    0.074    0.004 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement_boundary.py:350(_under_permit)
         20    0.000    0.000    0.074    0.004 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement.py:345(enforce)
         80    0.000    0.000    0.058    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:208(_ensure_core_importable)
         80    0.002    0.000    0.058    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:148(locate_repo_root)
    680/200    0.001    0.000    0.056    0.000 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/state_changes.py:93(_go)
         40    0.000    0.000    0.049    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2059(commit)
      80/40    0.000    0.000    0.049    0.001 <sqlalchemy generated _go() wrapper for sqlalchemy.orm.session.SessionTransaction.commit>:1(commit)
      80/40    0.001    0.000    0.049    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:1323(commit)
         60    0.000    0.000    0.046    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:481(_core_sovereignty)
         20    0.000    0.000    0.038    0.002 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement.py:292(consume)
         80    0.001    0.000    0.038    0.000 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/query.py:2795(first)
         20    0.000    0.000    0.036    0.002 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement.py:146(_atomic_write)
         40    0.000    0.000    0.031    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py:186(get_identity)
         80    0.000    0.000    0.030    0.000 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/query.py:2916(_iter)
         20    0.000    0.000    0.029    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement_boundary.py:547(route)
         20    0.000    0.000    0.029    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:381(_apply)
         20    0.000    0.000    0.029    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py:323(<lambda>)
         20    0.000    0.000    0.029    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py:225(_write_identity_row)
         80    0.000    0.000    0.028    0.000 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2406(execute)
         80    0.001    0.000    0.028    0.000 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2201(_execute_internal)
         20    0.000    0.000    0.027    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/agent_runtime/population.py:241(get_agent)
         20    0.000    0.000    0.027    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/gateway.py:439(decide)
        100    0.026    0.000    0.026    0.000 {built-in method posix.fsync}
  1 passed in 2.70s
  PROFILE_AFTER_EXIT:0
  PROFILE_COPY_REMOVED
  ملاحظة قراءة للمخرج لا للمخرج نفسه: idempotency.py:_atomic_write غير ظاهرة في أعلى 30. الظاهرة باسم _atomic_write هي enforcement.py:146 (cumtime 0.036 من 0.271).

  --- 11 bench curve BEFORE (checkout f4902232 idempotency.py, same tree, specified rerun) ---
  EXIT checkout: 0
  EXIT bench: 0
  EXIT restore: 0
  BLOB_HEAD_BEFORE_SWAP:7ff2c5c5e7c5e93e38cdb74f58a3590c09b420b1
  BLOB_WORKTREE after checkout:5e1b4a5233f142849999f99859d5f2abfdd5b56c
  BLOB_OLD_COMMIT f4902232:core/sovereignty/idempotency.py:5e1b4a5233f142849999f99859d5f2abfdd5b56c
  CURVE_TIMES: [0.264, 0.238, 0.306, 0.352, 0.44, 0.461, 0.57, 0.57, 0.615, 0.708, 0.835, 0.799]
  FILE_SIZES: [21065, 41225, 61385, 81545, 101705, 121865, 142025, 162185, 182345, 202505, 222665, 242825]
  RATIO: 3.36
  JSON: {"times": [0.264, 0.238, 0.306, 0.352, 0.44, 0.461, 0.57, 0.57, 0.615, 0.708, 0.835, 0.799], "sizes": [21065, 41225, 61385, 81545, 101705, 121865, 142025, 162185, 182345, 202505, 222665, 242825]}
  1 passed in 6.52s
  BENCH_BEFORE_EXIT:0
  BENCH_BEFORE_COPY_REMOVED
  BLOB_RESTORED:7ff2c5c5e7c5e93e38cdb74f58a3590c09b420b1
  BLOB_HEAD:7ff2c5c5e7c5e93e38cdb74f58a3590c09b420b1
  RESTORE_EXIT:0

  --- A ADDITIONAL cProfile BEFORE (same checkout, before restore) ---
  EXIT: 0
  PROFILE_OUTPUT:
           10483433 function calls (8461660 primitive calls) in 2.880 seconds

     Ordered by: cumulative time
     List reduced from 1113 to 30 due to restriction <30>

     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
          1    0.000    0.000    2.881    2.881 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/agent_runtime/population.py:214(seed_initial_population)
         20    0.001    0.000    2.880    0.144 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/agent_runtime/population.py:170(register_agent)
         20    0.001    0.000    2.806    0.140 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py:269(register_identity)
         20    0.000    0.000    2.718    0.136 /home/user/workspace/council-w521/grok/AMOS-Fedration/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:355(guard_declared)
         20    0.001    0.000    2.704    0.135 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement_boundary.py:291(execute)
         20    0.000    0.000    2.666    0.133 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:599(run_once)
         20    0.000    0.000    2.666    0.133 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:627(_run_once_inner)
         60    0.000    0.000    2.467    0.041 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:316(_save)
         60    0.001    0.000    2.466    0.041 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:161(_atomic_write)
         80    0.500    0.006    2.430    0.030 /opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/json/__init__.py:120(dump)
         40    0.001    0.000    1.716    0.043 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:366(transition)
    1455820    0.252    0.000    1.500    0.000 /opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/json/encoder.py:414(_iterencode)
  3473780/1455820    0.799    0.000    1.248    0.000 /opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/json/encoder.py:334(_iterencode_dict)
         20    0.002    0.000    0.880    0.044 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:437(mark_succeeded)
         20    0.003    0.000    0.868    0.043 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:569(_reserve_or_replay)
         20    0.002    0.000    0.841    0.042 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:426(mark_running)
         20    0.000    0.000    0.836    0.042 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:328(reserve)
     731060    0.200    0.000    0.477    0.000 /opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/json/encoder.py:278(_iterencode_list)
    1455980    0.257    0.000    0.428    0.000 /opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/tempfile.py:497(func_wrapper)
    1455820    0.171    0.000    0.171    0.000 {method 'write' of '_io.TextIOWrapper' objects}
    1001167    0.113    0.000    0.113    0.000 {built-in method builtins.isinstance}
         80    0.001    0.000    0.111    0.001 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/idempotency.py:305(_load)
        200    0.000    0.000    0.100    0.000 /opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/json/__init__.py:299(loads)
        200    0.001    0.000    0.099    0.000 /opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/json/decoder.py:333(decode)
        200    0.098    0.000    0.098    0.000 /opt/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/json/decoder.py:344(raw_decode)
     513200    0.097    0.000    0.097    0.000 {built-in method _json.encode_basestring}
         20    0.000    0.000    0.075    0.004 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement_boundary.py:350(_under_permit)
         20    0.000    0.000    0.075    0.004 /home/user/workspace/council-w521/grok/AMOS-Fedration/core/sovereignty/enforcement.py:345(enforce)
    680/200    0.002    0.000    0.074    0.000 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/state_changes.py:93(_go)
         40    0.000    0.000    0.065    0.002 /home/user/workspace/council-w521/grok/AMOS-Fedration/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2059(commit)
  1 passed in 7.82s
  PROFILE_BEFORE_EXIT:0
  PROFILE_BEFORE_COPY_REMOVED
  حساب من المخرج: idempotency.py:161(_atomic_write) cumtime 2.466 / seed 2.881 = 85.6% (60 نداءً).

  --- B ADDITIONAL bench curve AFTER rerun (after restore; blob matched HEAD) ---
  EXIT: 0
  CURVE_TIMES: [0.228, 0.142, 0.141, 0.145, 0.162, 0.222, 0.15, 0.148, 0.15, 0.151, 0.154, 0.187]
  FILE_SIZES: [39981, 79061, 118141, 157221, 196301, 235381, 274461, 313541, 352621, 391701, 430781, 469861]
  RATIO: 1.32
  JSON: {"times": [0.228, 0.142, 0.141, 0.145, 0.162, 0.222, 0.15, 0.148, 0.15, 0.151, 0.154, 0.187], "sizes": [39981, 79061, 118141, 157221, 196301, 235381, 274461, 313541, 352621, 391701, 430781, 469861]}
  1 passed in 2.33s
  BENCH_AFTER_RERUN_EXIT:0
  RESTORED_BLOB:7ff2c5c5e7c5e93e38cdb74f58a3590c09b420b1
  HEAD_BLOB:7ff2c5c5e7c5e93e38cdb74f58a3590c09b420b1

  --- C ADDITIONAL order checks ---
  EXIT parent-has-design: غير صفر (fatal: path exists on disk, but not in 'cacd1a7^') → PARENT_NO_DESIGN
  cacd1a793889324a6bf0b057f6cf19d1102c4279 2026-10-19 01:13:09 +0000 introduces both docs/audit/DISC105_IDEMPOTENCY_APPEND_DESIGN.md (84 lines added) and core/sovereignty/idempotency.py (+305/−56) in one commit.
  REVIEW_ANCESTOR_OF_MERGE: yes (1f4a64978d68d8f2405564062bdf851b37844f1b ancestor of 63b1a3f052e769a5be8e164f85382e38c26ecdb0)
  EXIT_MERGE_BEFORE_REVIEW: 1 (merge is not an ancestor of the review commit)
  review commit date: 2026-10-19 04:24:16 +0000
  merge commit 63b1a3f date: 2026-10-19 04:49:56 +0000
  merge parents: 838d68c4d78186bc5ee0d0660aba848b4fde5f93 7b294946350bd64827bff990ca0924fede073b78
  merge subject: W-494: دمجُ main المعالَجةِ (PR #77 · 7b29494) إلى فرعِ wi-082-restore
  REVIEW_IN_PR77_HEAD: yes (1f4a649 ancestor of 7b29494)
VERDICT_PER_CRITERION: |
  (1) وثيقةُ تصميمٍ تُعرَضُ قبلَ الشِفرةِ → نعم.
  الدليل: الوثيقة موجودة عند العقدة في docs/audit/DISC105_IDEMPOTENCY_APPEND_DESIGN.md وهي تصميم (وضع قائم / JSONL+flock+ضغط / طفرات ثمان / منحنى / حدود) لا ملاحظةً لاحقةً فقط. git log --follow يُظهر أول ظهور لها في cacd1a7 (W-471، 2026-10-19 01:13:09 +0000) وهو نفس الالتزام الذي أدخل تغيير شفرة WI-096 على core/sovereignty/idempotency.py. الأب cacd1a7^ لا يحتوي الوثيقة (PARENT_NO_DESIGN). لا التزام شفرة لـWI-096 يسبق الوثيقة: تاريخ الملف قبل cacd1a7 هو W-034 وSTAGE 1H فقط. رسالة الالتزام تنص «الوثيقةُ ثمَّ الشِفرةُ». لا التزام منفصل أسبق للوثيقة في كل المراجع المحلية. هذا لا يثبت عرضًا مراجَعًا في التزام سابق، ويثبت أن الشفرة لم تُدمَج في التاريخ قبل الوثيقة. لا أعدّ التزامًا واحدًا مشتركًا خرقًا لـ«لا شفرة قبل الوثيقة» لأن الخرق المشاهَد كان سيكون التزام شفرة يخلو أبوه من الوثيقة، وذلك لم يقع.
  (2) فحوصُ طفراتٍ تحرسُ خصائصَ الذرّةِ → نعم.
  الدليل: pytest المسارات الثلاثة EXIT 0، 98 passed in 2.53s. الحاصد EXIT 0، خط أساس أخضر، M1..M8 كلها failures>0 وerrors=0، بعد الاستعادة أخضر، ALL_KILLED = True. القتلة مسمّاة في المخرج الخام وتطابق الطفرات الثماني في وثيقة التصميم § 3.
  (3) منحنى قبل/بعد على الجهازِ نفسِهِ يُثبتُ زوالَ الهيمنةَ (إعادةُ الكتابةِ الكاملةِ) → نعم.
  الدليل من تشغيلي على الشجرة نفسها:
  قبل (blob 5e1b4a52 = f4902232:idempotency.py) RATIO 3.36، الأزمنة تنمو مع التراكم 0.238→0.799 بينما الملف 41225→242825 بايت، EXIT 0.
  بعد (blob 7ff2c5c5 = HEAD عند عقدة المراجعة) التشغيل الرسمي RATIO 1.62، الأزمنة 0.131 ثم هضبة 0.131–0.147 ثم 0.212، والملف ينمو 79061→469861 بايت (نحو 6×) بلا نموٍّ مطّردٍ للزمن، EXIT 0.
  cProfile قبل (ADDITIONAL على checkout قبل نفسه): idempotency.py:161(_atomic_write) 60 نداءً، cumtime 2.466 من 2.881 = 85.6% من جولة البذر المفكَّكة، وjson.dump يهيمن. EXIT 0.
  cProfile بعد (الأمر المكتوب): جولة البذر 0.271 ث (مقابل 2.881 قبل، نحو 10.6×). idempotency.py:_atomic_write غائبة عن أعلى 30. run_once cumtime 0.099. _atomic_write الظاهرة هي enforcement.py:146 بـ0.036 وليست كتابة ملف الذرّيّة. EXIT 0.
  الهيمنة زالت: إعادة الكتابة الكاملة لم تعد تتبع نمو الملف ولم تعد أغلب الزمن.
  ملاحظة غير حاجبة: وثيقة التصميم § 4 (تصحيح W-477، ليست في نص معيار القبول المقفول عند f4902232 كما نقلته الإحاطة) تضع النسبة ≤ 1.15. التشغيل الرسمي طبع RATIO 1.62 وإعادة التأكيد ADDITIONAL طبعت 1.32. العتبة الرقمية تلك لم تتحقق في عيّنتي النقطتين. لا أُسقط المعيار المقفول بها: المعيار المقفول هو زوال هيمنة إعادة الكتابة الكاملة، والمخرجان (شكل المنحنى + cProfile) يثبتانه. النسبة نقطتان فقط وتتأثران بشوكة واحدة (0.212 و0.222) على أساس نحو 0.14 ث، وأداة القياس نفسها لا تفشل pytest عند تجاوز 1.15 (الاختبار يطبع النسبة ويمرّ).
  (4) مراجعةٌ تُعيدُ التشغيلَ فعلًا محفوظةً نصًّا قبلَ الدمجِ → نعم.
  الدليل: docs/audit/evidence/W-492/review.txt التزامها الوحيد 1f4a64978d68d8f2405564062bdf851b37844f1b (2026-10-19 04:24:16 +0000). merge-base --is-ancestor مقابل عقدة المراجعة طبع ANCESTOR_OK وEXIT 0. الالتزام نفسه سلف لالتزام الدمج 63b1a3f (2026-10-19 04:49:56 +0000، PR #77 · 7b29494) وسلف لرأس PR #77. النص المحفوظ يوثّق إعادة تشغيل فعلية (فحوص سيادة + حاصد الطفرات 8/8 ALL_KILLED = True) لا مراجعة ورقية. حدّ صريح في النص نفسه، غير حاجب لهذا المعيار: المراجع المحفوظ لم يشغّل منحنى bench_curve (بيئته بلا sqlalchemy) ونقل أرقام المنحنى لا قاسها. المعيار يطلب حفظ مراجعة أعادت التشغيل نصًا قبل الدمج، وذلك متحقّق. قياسي أنا للمنحنى مستقل عن ذلك النص.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — لم أقرأ شيئًا خارج استنساخي /home/user/workspace/council-w521/grok/AMOS-Fedration وهذه الإحاطة. لم أفتح /home/user/workspace/amos ولا أدلة مقاعد أخرى. داخل الاستنساخ قرأت مصادر الحكم اللازمة للمعايير لا حزم أدلة المنفّذ كبديل عن التشغيل: كتلة WI-096 في docs/governance/work/ACTIVE_WORK.md، وثيقة التصميم (معيار 1)، review.txt (معيار 4)، إشارات Q-59 في docs/audit/SOVEREIGN_DECISION_REGISTER.md، ونص بروتوكول المجلس لمعنى الملاحظة الحاجبة، ونصوص أدوات القياس التي شغّلتها. الأرقام في الحكم من إعادة تشغيلي. حدّ العزل الإجرائي المعلن (صندوق ملفات مشترك) قائم كما في البروتوكول § 2.4 — لم أستثمره للقراءة خارج الاستنساخ.
VERDICT: PASS لكلِّ المعاييرِ
````
