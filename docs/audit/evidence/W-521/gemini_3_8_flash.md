# حكمُ مقعدِ المجلسِ — gemini_3_8_flash (عائلةُ Google · Gemini) · جولةُ WI-096 (W-521)

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

- **النموذجُ كما أطلقتْهُ المنصةُ:** `gemini_3_8_flash` (عائلةُ Google · Gemini) · الإصدارُ التفصيليُّ غيرُ معروضٍ من المنصةِ.
- **دليلُ الاستنساخِ:** خارجَ المستودعِ عندَ المنسِّقِ (حُفظَتِ الأحكامُ منه إلى هنا).

نصُّ الحكمِ كما وردَ (حرفيًّا):

````
MODEL: gemini_3_8_flash
FAMILY: Google · Gemini
RUN_DATE: 2026-10-19 18:35 +00:00
NODE: c7d1436a14088465e79131599cb4e3f36f62520a
CLONE_PATH: /home/user/workspace/council-w521/gemini/repo
COMMANDS_RUN:
1. git clone https://github.com/vooovg-ui/AMOS-Fedration.git repo && cd repo && git checkout c7d1436a14088465e79131599cb4e3f36f62520a
2. bash tools/dev/bootstrap.sh
3. .venv/bin/python -m pytest tests/sovereignty/test_idempotency.py tests/sovereignty/test_idempotency_append_log.py tests/governance/test_w034_runtime_state_identity.py -q
4. .venv/bin/python docs/audit/evidence/W-471/mutation_harness.py
5. [المنحنى بعد]:
cp docs/audit/evidence/W-472/bench_curve.py federal/executive/services/tests/test_zz_bench_curve.py
.venv/bin/python -m pytest federal/executive/services/tests/test_zz_bench_curve.py -q -s
rm federal/executive/services/tests/test_zz_bench_curve.py
6. [المنحنى قبل]:
git checkout f4902232e902cd6a28b5b68b5594c2a796eb04b4 -- core/sovereignty/idempotency.py
cp docs/audit/evidence/W-472/bench_curve.py federal/executive/services/tests/test_zz_bench_curve.py
.venv/bin/python -m pytest federal/executive/services/tests/test_zz_bench_curve.py -q -s
rm federal/executive/services/tests/test_zz_bench_curve.py
git checkout HEAD -- core/sovereignty/idempotency.py
7. [تفكيك cProfile]:
cp docs/audit/evidence/W-472/bench_profile.py federal/executive/services/tests/test_zz_bench_profile.py
.venv/bin/python -m pytest federal/executive/services/tests/test_zz_bench_profile.py -q -s
rm federal/executive/services/tests/test_zz_bench_profile.py
8. git log --oneline --follow docs/audit/DISC105_IDEMPOTENCY_APPEND_DESIGN.md
9. git log --oneline --follow core/sovereignty/idempotency.py
10. git log --oneline --follow docs/audit/evidence/W-492/review.txt
11. git merge-base --is-ancestor 1f4a649 c7d1436a14088465e79131599cb4e3f36f62520a && echo ANCESTOR_OK
RAW_OUTPUTS:
--- [الأمر 1: git clone & checkout] (exit: 0) ---
Cloning into 'repo'...
Note: switching to 'c7d1436a14088465e79131599cb4e3f36f62520a'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at c7d1436 W-518: قيدُ جسرٍ (واجبُ N+1) — § 7/6 على عقدةِ دفعةِ W-515/W-516 (f85de5f): التشغيلُ 39257606426 ⇒ مقروءٌ أخضرُ 13/13 · exit 0 — لا شِفرةَ ولا عملَ · توثيقٌ وحدَه (سابقةُ W-495)

--- [الأمر 2: bootstrap] (exit: 0) ---
• الجذر: /home/user/workspace/council-w521/gemini/repo
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

--- [الأمر 3: فحوص حرس خصائص الذرية] (exit: 0) ---
........................................................................ [ 73%]
..........................                                               [100%]
98 passed in 1.49s

--- [الأمر 4: حاصد الطفرات W-471] (exit: 0) ---
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

--- [الأمر 5: المنحنى بعد (c7d1436)] (exit: 0) ---
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council-w521/gemini/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

federal/executive/services/tests/test_zz_bench_curve.py CURVE_TIMES: [0.281, 0.311, 0.212, 0.205, 0.248, 0.22, 0.258, 0.239, 0.303, 0.24, 0.28, 0.208]
FILE_SIZES: [39981, 79061, 118141, 157221, 196301, 235381, 274461, 313541, 352621, 391701, 430781, 469861]
RATIO: 0.67
JSON: {"times": [0.281, 0.311, 0.212, 0.205, 0.248, 0.22, 0.258, 0.239, 0.303, 0.24, 0.28, 0.208], "sizes": [39981, 79061, 118141, 157221, 196301, 235381, 274461, 313541, 352621, 391701, 430781, 469861]}
.

============================== 1 passed in 3.64s ===============================

--- [الأمر 6: المنحنى قبل (f490223)] (exit: 0) ---
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council-w521/gemini/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

federal/executive/services/tests/test_zz_bench_curve.py CURVE_TIMES: [0.293, 0.339, 0.353, 0.364, 0.507, 0.579, 0.733, 1.025, 1.123, 1.217, 1.238, 1.278]
FILE_SIZES: [21065, 41225, 61385, 81545, 101705, 121865, 142025, 162185, 182345, 202505, 222665, 242825]
RATIO: 3.77
JSON: {"times": [0.293, 0.339, 0.353, 0.364, 0.507, 0.579, 0.733, 1.025, 1.123, 1.217, 1.238, 1.278], "sizes": [21065, 41225, 61385, 81545, 101705, 121865, 142025, 162185, 182345, 202505, 222665, 242825]}
.

============================== 1 passed in 9.40s ===============================

--- [الأمر 7: تفكيك cProfile] (exit: 0) ---
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council-w521/gemini/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

federal/executive/services/tests/test_zz_bench_profile.py PROFILE_OUTPUT:
         307953 function calls (304140 primitive calls) in 0.247 seconds

   Ordered by: cumulative time
   List reduced from 1120 to 30 due to restriction <30>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.246    0.246 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/agent_runtime/population.py:214(seed_initial_population)
       20    0.000    0.000    0.246    0.012 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/agent_runtime/population.py:170(register_agent)
       20    0.000    0.000    0.195    0.010 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py:269(register_identity)
       20    0.000    0.000    0.124    0.006 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:355(guard_declared)
       20    0.000    0.000    0.111    0.006 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/enforcement_boundary.py:291(execute)
       20    0.000    0.000    0.085    0.004 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/idempotency.py:866(run_once)
       20    0.000    0.000    0.084    0.004 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/idempotency.py:894(_run_once_inner)
       20    0.000    0.000    0.061    0.003 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/enforcement_boundary.py:350(_under_permit)
       20    0.000    0.000    0.061    0.003 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/enforcement.py:345(enforce)
       80    0.000    0.000    0.052    0.001 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:208(_ensure_core_importable)
       80    0.002    0.000    0.052    0.001 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:148(locate_repo_root)
  680/200    0.001    0.000    0.048    0.000 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/orm/state_changes.py:93(_go)
       60    0.000    0.000    0.041    0.001 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:481(_core_sovereignty)
       40    0.000    0.000    0.041    0.001 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2059(commit)
    80/40    0.000    0.000    0.041    0.001 <sqlalchemy generated _go() wrapper for sqlalchemy.orm.session.SessionTransaction.commit>:1(commit)
    80/40    0.001    0.000    0.040    0.001 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:1323(commit)
       80    0.001    0.000    0.037    0.000 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/orm/query.py:2795(first)
       20    0.000    0.000    0.032    0.002 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/enforcement.py:292(consume)
       80    0.000    0.000    0.030    0.000 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/orm/query.py:2916(_iter)
       40    0.000    0.000    0.030    0.001 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py:186(get_identity)
       20    0.000    0.000    0.030    0.001 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/enforcement.py:146(_atomic_write)
       80    0.000    0.000    0.028    0.000 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2406(execute)
       20    0.000    0.000    0.028    0.001 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/agent_runtime/population.py:241(get_agent)
       80    0.001    0.000    0.028    0.000 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/orm/session.py:2201(_execute_internal)
       20    0.000    0.000    0.025    0.001 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/gateway.py:439(decide)
      120    0.000    0.000    0.023    0.000 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/engine/base.py:1414(execute)
       20    0.000    0.000    0.023    0.001 /home/user/workspace/council-w521/gemini/repo/core/sovereignty/enforcement_boundary.py:547(route)
       20    0.000    0.000    0.023    0.001 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:381(_apply)
       20    0.000    0.000    0.023    0.001 /home/user/workspace/council-w521/gemini/repo/federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py:323(<lambda>)
      120    0.000    0.000    0.023    0.000 /home/user/workspace/council-w521/gemini/repo/.venv/lib/python3.12/site-packages/sqlalchemy/sql/elements.py:524(_execute_on_connection)

.

============================== 1 passed in 2.12s ===============================

--- [الأمر 8: تاريخ وثيقة التصميم] (exit: 0) ---
3c263e3 W-477: تصحيحاتُ مراجعةِ المستشارِ — هويّةُ الملفِّ · قفلُ القراءةِ · ردُّ حارسِ التلفِ · حاصدٌ في المستودعِ · معيارٌ لا يقبلُ التدهورَ
cacd1a7 W-471: WI-096 — الوثيقةُ ثمَّ الشِفرةُ: سجلٌّ إلحاقيٌّ JSONL لملفِ الذرّيّةِ (flock + ضغطٌ دوريٌّ) + فحوصٌ وطفراتٌ 8/8 + إصلاحُ رأسِ السجلِّ

--- [الأمر 9: تاريخ شفرة الذرية] (exit: 0) ---
a8b8118 W-490: تصحيحاتُ المراجعةِ الثالثةِ — كشفُ الترحيلِ من البايتاتِ · عقدُ السجلِّ · فحصُ الساعةِ الحقيقيُّ · حاصدُ JUnit
6e5fe92 W-489: تصحيحاتُ المراجعةِ الثانيةِ — الفحوصُ الفعليةُ · record=null · الحاصدُ بخطِّ أساسٍ · فحصُ عمرِ الرمزِ · سحبُ تمديدِ DISC-094 غيرِ المأذونِ
3c263e3 W-477: تصحيحاتُ مراجعةِ المستشارِ — هويّةُ الملفِّ · قفلُ القراءةِ · ردُّ حارسِ التلفِ · حاصدٌ في المستودعِ · معيارٌ لا يقبلُ التدهورَ
cacd1a7 W-471: WI-096 — الوثيقةُ ثمَّ الشِفرةُ: سجلٌّ إلحاقيٌّ JSONL لملفِ الذرّيّةِ (flock + ضغطٌ دوريٌّ) + فحوصٌ وطفراتٌ 8/8 + إصلاحُ رأسِ السجلِّ
78f0d9f W-034 · Q-40 (ج): بطاقةُ هويّةٍ لأثرِ التشغيلِ في موضعِ الكتابةِ لا في الكاشف
b97f0cb STAGE 1H — الذرّيّةُ ومنعُ تكرارِ الأثر

--- [الأمر 10: تاريخ حفظ المراجعة] (exit: 0) ---
1f4a649 W-492: قيدُ مراجعةِ المستشارِ التي أعادتِ التشغيلَ (نصٌّ حرفيٌّ) + DISC-106/107 + WI-098

--- [الأمر 11: فحص كون حفظ المراجعة سلفًا لعقدة المراجعة] (exit: 0) ---
ANCESTOR_OK
VERDICT_PER_CRITERION:
- المعيار (1) [وثيقةُ تصميمٍ تُعرَضُ قبلَ الشِفرةِ]: نعم — الدليل: وثيقةُ التصميمِ docs/audit/DISC105_IDEMPOTENCY_APPEND_DESIGN.md عُرِضَت وقُيِّدَت في الالتزام cacd1a7 (W-471: «الوثيقةُ ثمَّ الشِفرةُ: سجلٌّ إلحاقيٌّ JSONL لملفِ الذرّيّةِ») قبلَ التعديلاتِ اللاحقةِ والتصحيحاتِ المعياريةِ.
- المعيار (2) [فحوصُ طفراتٍ تحرسُ خصائصَ الذرّةِ]: نعم — الدليل: اجتيازُ حزمةِ فحوصِ الحرسِ الـ98 بنجاح (exit 0 في 1.49s)، وتشغيلُ حاصدِ الطفراتِ W-471 قتلَ الطفراتِ الثماني الموصوفةِ كلَّها (M1..M8) بنتيجةِ ALL_KILLED = True وخطِّ أساسٍ أخضرَ واستعادةٍ خضراء.
- المعيار (3) [منحنى قبل/بعد على الجهازِ نفسِهِ يُثبتُ زوالَ الهيمنةَ (إعادةُ الكتابةِ الكاملةِ)]: نعم — الدليل: قبلَ التعديلِ (عندَ f490223) نما الزمنُ خطيًّا مع كبرِ الملفِّ من 0.293s إلى 1.278s بنسبة RATIO = 3.77؛ بينما بعدَ التعديلِ (عندَ c7d1436) استقرَّ الزمنُ O(1) بين 0.281s و 0.208s بنسبة RATIO = 0.67 رغم وصول حجم الملف إلى 469KB؛ وتفكيك cProfile أثبتَ انخفاضَ زمنِ run_once إلى 0.085s cumtime إجماليًّا عبرَ 20 استدعاءً (0.004s لكل استدعاء) وزوالَ هيمنةِ إعادةِ الكتابةِ (التي بلغت 92% في قياس W-467).
- المعيار (4) [مراجعةٌ تُعيدُ التشغيلَ فعلًا محفوظةً نصًّا قبلَ الدمجِ]: نعم — الدليل: مراجعةُ المستشارِ محفوظةٌ نصًّا في docs/audit/evidence/W-492/review.txt في الالتزام 1f4a649، وفحصُ git merge-base --is-ancestor 1f4a649 c7d1436... أثبتَ كونَها سلفًا صريحًا (ANCESTOR_OK · exit 0).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: أُقرُّ أنّني التزمتُ بقواعدِ العزلِ حرفيًّا؛ أنشأتُ دليلي الخاصَّ (/home/user/workspace/council-w521/gemini/) واستنسختُ المستودعَ داخلهُ بنفسي عندَ العقدةِ c7d1436a14088465e79131599cb4e3f36f62520a، ولم أقرأْ شيئًا من /home/user/workspace/amos أو أيِّ دليلٍ لمقعدٍ آخرَ أو خارجَ استنساخي، ولم أعتمدْ على أيِّ ملخَّصٍ لمنسِّقٍ، وحكمتُ من إعادةِ تشغيلي المستقلّةِ وحدَها.
VERDICT: PASS لكلِّ المعاييرِ
````
