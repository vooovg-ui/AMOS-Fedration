# حكمُ مقعدِ المجلسِ — grok_4_7 (عائلةُ xAI · Grok) · جولةُ دفعةِ J1 على WI-105 (W-599)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ مجلسِ المراجعةِ على دفعةِ J1 (إحاطاتُ W-598 · العقدةُ `03a6c62` · بندُ WI-105 · المعاييرُ 1–6) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في دليلِهِ الخاصِّ `council_w598/grok_4_7` (§ 4.8: ملفُّ الحكمِ هو الحكمُ) — منسوخٌ آليًّا، وما بعدَ الفاصلِ بايتًا ببايتٍ (sha256 `8e91f0335d6a89a5e749bd35712644804ec6142bfb7ea81420a89ceb0af6e820`).

---

MODEL: grok_4_7
FAMILY: grok
RUN_DATE: 2026-10-22 02:43 +00:00
NODE: 03a6c625b79002c519a54bc1f27fddd6e99500dc
CLONE_PATH: /home/user/workspace/council_w598/grok_4_7/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w598/grok_4_7/repo && git rev-parse HEAD
 2. cd /home/user/workspace/council_w598/grok_4_7/repo && bash tools/dev/bootstrap.sh
 3. cd /home/user/workspace/council_w598/grok_4_7/repo && git log --format='%h %cI %s' d0932c51..HEAD
 4. cd /home/user/workspace/council_w598/grok_4_7/repo && git diff --stat d0932c51 HEAD
 5. cd /home/user/workspace/council_w598/grok_4_7/repo && git log --format='%h %cI %s' -- docs/audit/J1_ISSUE_RULING_DESIGN.md
 6. cd /home/user/workspace/council_w598/grok_4_7/repo && git diff d0932c51 HEAD -- federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py
 7. cd /home/user/workspace/council_w598/grok_4_7/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 8. cd /home/user/workspace/council_w598/grok_4_7/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/federal_judiciary --json /home/user/workspace/council_w598/grok_4_7/tmp/judiciary.json
 9. cd /home/user/workspace/council_w598/grok_4_7/repo && rg -n "issue_ruling|guarded|public" /home/user/workspace/council_w598/grok_4_7/tmp/judiciary.json
 10. cd /home/user/workspace/council_w598/grok_4_7/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/executive_core --json /home/user/workspace/council_w598/grok_4_7/tmp/executive_core.json
 11. cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py -q
 12. cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py -q
 13. cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
 14. cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
 15. cd /home/user/workspace/council_w598/grok_4_7/repo && rg -n "JUDICIARY_ACTOR|judicial_action|position_scope|guard_declared\(" federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py federal/executive/services/src/amos_federation/services/federal_judiciary/service.py federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py
 16. cd /home/user/workspace/council_w598/grok_4_7/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
 17. cd /home/user/workspace/council_w598/grok_4_7/repo && cat docs/audit/evidence/W-593/mutation_m1.txt docs/audit/evidence/W-593/mutation_m2.txt docs/audit/evidence/W-593/mutation_m3.txt docs/audit/evidence/W-593/mutation_m4.txt
 18. cd /home/user/workspace/council_w598/grok_4_7/repo && cat docs/audit/evidence/W-593/measurements.txt
 19. cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_step7_factory_surfaces.py -q
 20. cd /home/user/workspace/council_w598/grok_4_7/repo && git diff d0932c51 HEAD -- tests/governance docs/audit/measurements
 21. cd /home/user/workspace/council_w598/grok_4_7/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
 22. find /home/user/workspace/council_w598/grok_4_7 -maxdepth 1
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 303bbf3988d611edb9f006de9dfd72594820a357981b3f7347811f35727ff259
NO_EOL: 0
--- OUTPUT ---
03a6c625b79002c519a54bc1f27fddd6e99500dc
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && bash tools/dev/bootstrap.sh
EXIT: 0
BYTES: 1287
SHA256: 628cb594dfd18c9f7b8e122708255e1a86024d4759ec63cea7f8b9f71f922efa
NO_EOL: 0
--- OUTPUT ---
• الجذر: /home/user/workspace/council_w598/grok_4_7/repo
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
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && git log --format='%h %cI %s' d0932c51..HEAD
EXIT: 0
BYTES: 4457
SHA256: caa8413d01adad4785256310161a4b76ae5b6da283d18ee50c4cb339a5fc6894
NO_EOL: 0
--- OUTPUT ---
03a6c62 2026-10-22T01:10:42Z W-597: WI-105 IN_PROGRESS → IN_REVIEW (قيد مستقل H3 · § 7.4 من بروتوكول المجلس) تمهيدًا لإطلاق جولة مجلس المراجعة على دفعة J1 كلها — استدراك على ذيل W-596: المجلس لا يعرض إلا بند IN_REVIEW · قياسات افتتاح الجلسة (حوكمة ✓ · راتشيت 61 ثابتًا · انحراف 0 · جرد فروع: لا تعارض) · حكم CI على 90cae46 (N+1 · دفعة W-596 · التشغيل 39679264001): مقروء أخضر 13/13 على العقدة نفسها — لا شِفرة — المنسق GLM-5.3
90cae46 2026-10-21T21:08:10Z W-596: تعديل إحاطات الجولة قبل الإطلاق (لم تُطلق بعد) وفق مراجعة المستشار — تصحيح العقدة إلى رأس w-594-v2 الشامل لتصحيح W-595 (كانت تشير إلى 529cc391 الناقصة الإصلاح) + الأوامر 19–21 (فحوص المُثبَّتات وفرقها وعقد نَسَب القياسات) وتعميم فرق الملفّات + تحديد سؤال T6 للجولة (التعويض الآلي أم المُعوِّض المسجَّل — من النص المعتمد لا من تقرير المنفِّذ) وإباحة إعادة الطفرات في نسخة معزولة + تصحيح مؤرَّخ في قياسات W-593 (عامّة قبل = 202 لا 201) + فرق المواضع بين العقدتين مسجَّلًا + إعادة ختم البصمات — المنسِّق GLM-5.3
ff53c07 2026-10-21T21:02:29Z W-594 (تصحيح مؤرَّخ): إصلاح حمرة CI على العقدة c225a9e — الفاشلات الست كلها تعليل لقطات قياس وجّهها حرق D-4 نفسه: لقطة الدَّين 183←181 (decision_gate.py --record-work W-593) وخريطة الموجات 50+34+97=181 وجرد الكتابات وfinal_audit_p14 ومصفوفة الحقيقة أعيد توليدها بأوامرها المقيَّدة · ومُثبَّتات الحارس في test_q3 حُدِّثت بالمقيس الجديد (43/41/0 · 50 · 27-4-19 · 6 مُعلِنًا) مع إضافات مؤرَّخة (سابقة W-402/W-535 — تحديث المُثبَّت بالمقيس لا تخفيف فحص) · tests/ كاملة 2705 ناجحًا · الدليل في evidence/W-594 — لا force-push: التزام فوق c225a9e في فرع جديد — المنسِّق GLM-5.3
c225a9e 2026-10-21T19:50:18Z W-594: إحاطات جولة دفعة J1 (تصميمًا وشِفرةً وأدلةً — § 7 المعدَّل بأمر المالك) — ثلاث نسخ مُبصَمة للمقاعد الثلاثة بحسب المنسِّق الفعلي GLM-5.3 (claude_opus_5_5 · gemini_3_8_flash · grok_4_7 · لا مقعد من عائلة GLM) عند العقدة 529cc391 · الجولة تحاكم المعيار (1) شِقَّ الترتيب والإضافتين المؤرَّختين والمعايير (2)–(6) · حكم CI على رأس W-593 (N+1): التشغيل 39664576857 مقروء أخضر 13/13 — إحاطات لا شِفرة — المنسِّق GLM-5.3
529cc39 2026-10-21T19:46:27Z W-593: شِفرة J1 — عبور issue_ruling الحدَّ السياديَّ بفاعلٍ قضائيٍّ ثابت (WI-105 · قرار المالك Q-69/D17-6): D1 ثابت JUDICIARY_ACTOR ومُفوِّض كسول في الوحدة · D2 الجسر يمرّر judicial_action كما هو · D3 طلب الاختصاص من البيانات الحيّة + حقل position_scope في JudicialAuthority · D4 المُطبِّق المتداخل يلتزم الصفوف الثلاثة في معاملة واحدة والخدمة فقدت commit · D6 مفتاح بجيل الإلغاء والمكرَّر قبل الحد · D7-أ مُعوِّض تقني (حذف الصفّين وإرجاع حالة القضيّة) — الجرد: الدَّين 183←181 · السيادي 17←18 · الأسطح 220←220 · فحوص T1–T7 خضراء (ملف جديد) وM1–M4 كلٌّ يُسقِط فحصه · r7d وWI-082 بلا تعديل · حزمة services 1482+53 · اكتشافان مؤرَّخان في التصميم: الجيل في هدف العبور (تصادم أذون الثانية) وقياس T6 عبر حارس 1I (مسار run_once لا يُعوِّض آليًّا) · حكم CI على d0932c51 (N+1): مقروء أخضر 13/13 — المنسِّق GLM-5.3
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && git diff --stat d0932c51 HEAD
EXIT: 0
BYTES: 2601
SHA256: b2060bed4c874e53725f03a62f39c83a9e78555816a2e71b72b1e967bf195895
NO_EOL: 0
--- OUTPUT ---
 PROJECT_STATE.md                                   |    4 +-
 docs/PROJECT_HANDBOOK.md                           |    7 +-
 docs/audit/ACTIVE_EXECUTION_STATE.md               |    2 +-
 docs/audit/COMPLETION_LEDGER.md                    |   18 +
 docs/audit/J1_ISSUE_RULING_DESIGN.md               |    4 +
 docs/audit/TRUTH_MATRIX.md                         |    6 +-
 docs/audit/evidence/W-593/README.md                |   22 +
 .../evidence/W-593/ci_verdict_39661440605.txt      |   11 +
 .../W-593/ci_verdict_39661440605_jobs.json         | 1666 ++++++++++++++++++++
 docs/audit/evidence/W-593/measurements.txt         |   44 +
 docs/audit/evidence/W-593/mutation_m1.txt          |    5 +
 docs/audit/evidence/W-593/mutation_m2.txt          |    7 +
 docs/audit/evidence/W-593/mutation_m3.txt          |    5 +
 docs/audit/evidence/W-593/mutation_m4.txt          |    6 +
 docs/audit/evidence/W-594/README.md                |   22 +
 docs/audit/evidence/W-594/briefs/README.md         |   31 +
 docs/audit/evidence/W-594/briefs/SHA256SUMS        |    3 +
 .../W-594/briefs/briefing_claude_opus_5_5.md       |  145 ++
 .../W-594/briefs/briefing_gemini_3_8_flash.md      |  145 ++
 .../evidence/W-594/briefs/briefing_grok_4_7.md     |  145 ++
 .../evidence/W-594/ci_verdict_39664576857.txt      |   11 +
 .../W-594/ci_verdict_39664576857_jobs.json         |   98 ++
 .../evidence/W-594/ci_verdict_39665131672_red.txt  |   18 +
 docs/audit/evidence/W-596/README.md                |   20 +
 docs/audit/evidence/W-596/sites_diff.txt           |    6 +
 docs/audit/evidence/W-597/README.md                |   22 +
 .../evidence/W-597/ci_jobs_39679264001.api.txt     |    1 +
 .../evidence/W-597/ci_verdict_39679264001.txt      |    6 +
 docs/audit/evidence/W-597/session_measurements.txt |   37 +
 docs/audit/measurements/decision_gate_ledger.json  |   16 +
 docs/audit/measurements/decision_wave_map.json     |    6 +-
 docs/audit/measurements/final_audit_p14.json       |    9 +-
 docs/audit/measurements/write_inventory_p13.json   |   47 +-
 docs/audit/truth_matrix.json                       |   24 +-
 docs/governance/work/ACTIVE_WORK.md                |   30 +-
 .../services/executive_core/sovereignty_bridge.py  |    3 +
 .../services/federal_judiciary/authority.py        |    3 +
 .../services/federal_judiciary/rulings.py          |  223 ++-
 .../services/federal_judiciary/service.py          |    4 +-
 .../tests/test_wi105_issue_ruling_sovereign.py     |  774 +++++++++
 .../test_q3_branch_declaration_surface.py          |   42 +-
 41 files changed, 3593 insertions(+), 105 deletions(-)
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && git log --format='%h %cI %s' -- docs/audit/J1_ISSUE_RULING_DESIGN.md
EXIT: 0
BYTES: 2108
SHA256: bd283becdbe67f51fc2f6dc1dc8fe2ff5f1501b5847ede4be0b1081a98ed0697
NO_EOL: 0
--- OUTPUT ---
529cc39 2026-10-21T19:46:27Z W-593: شِفرة J1 — عبور issue_ruling الحدَّ السياديَّ بفاعلٍ قضائيٍّ ثابت (WI-105 · قرار المالك Q-69/D17-6): D1 ثابت JUDICIARY_ACTOR ومُفوِّض كسول في الوحدة · D2 الجسر يمرّر judicial_action كما هو · D3 طلب الاختصاص من البيانات الحيّة + حقل position_scope في JudicialAuthority · D4 المُطبِّق المتداخل يلتزم الصفوف الثلاثة في معاملة واحدة والخدمة فقدت commit · D6 مفتاح بجيل الإلغاء والمكرَّر قبل الحد · D7-أ مُعوِّض تقني (حذف الصفّين وإرجاع حالة القضيّة) — الجرد: الدَّين 183←181 · السيادي 17←18 · الأسطح 220←220 · فحوص T1–T7 خضراء (ملف جديد) وM1–M4 كلٌّ يُسقِط فحصه · r7d وWI-082 بلا تعديل · حزمة services 1482+53 · اكتشافان مؤرَّخان في التصميم: الجيل في هدف العبور (تصادم أذون الثانية) وقياس T6 عبر حارس 1I (مسار run_once لا يُعوِّض آليًّا) · حكم CI على d0932c51 (N+1): مقروء أخضر 13/13 — المنسِّق GLM-5.3
4f357aa 2026-10-21T13:53:07Z W-588: تصحيح أثر الأسطح في تصميم J1 بالإضافة (DISC-126 · وجده مقعد grok_4_7): 220 ← 219 ⇒ 220 ← 220 في D4 و§ 4 والمعيار (3) — الدين 183 ← 181 بلا تغيير — لا شِفرة — المنسِّق Claude Opus 5.5
d6dfaee 2026-10-21T12:42:51Z W-584: تصحيح بالإضافة قبل جولة تصميم J1 — «18 نداءً» ← 15 مقيسًا (DISC-124) في الوثيقة وكتلة WI-105 — لا شِفرة — المنسِّق Claude Opus 5.5
ce4b917 2026-10-21T10:26:52Z W-581: WI-105 RESERVED → IN_PROGRESS — وثيقة تصميم J1 قبل الشِّفرة + DISC-121 (AGENT/SYSTEM 54/54) + Q-68 + ورقة D17 + حكم CI على 2694796 — لا شِفرة — المنسِّق Claude Opus 5.5
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && git diff d0932c51 HEAD -- federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3407
SHA256: 3e48e106984387db93ba65d96f685637b02f531b3db76f216bbf4a6bfce3d4ab
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 220
  عمليّاتٌ عامّةٌ مُغيِّرة   : 201
  منها تعبرُ الحدَّ        : 18
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 181
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          171 /  18 /  152
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      17  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
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
       1  federal/executive/services/src/amos_federation/services/government_services/service.py
       1  tools/migrations/r4_unify_agent_identity.py
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/federal_judiciary --json /home/user/workspace/council_w598/grok_4_7/tmp/judiciary.json
EXIT: 0
BYTES: 1072
SHA256: 0b5623be111198a749e93e0509c48ed194b52bc13c2176cbc2d78e21075225ba
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : federal/executive/services/src/amos_federation/services/federal_judiciary
  مواضعُ كتابةٍ (كلُّها)   : 27
  عمليّاتٌ عامّةٌ مُغيِّرة   : 26
  منها تعبرُ الحدَّ        : 1
  مساراتٌ قديمةٌ مُغلَقة    : 0
  **لا تعبرُ الحدَّ**       : 25
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    services           26 /   1 /   25
  التوزيعُ على الملفّات:
      17  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
       5  federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
       2  federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py
  التفصيلُ محفوظٌ في: /home/user/workspace/council_w598/grok_4_7/tmp/judiciary.json
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && rg -n "issue_ruling|guarded|public" /home/user/workspace/council_w598/grok_4_7/tmp/judiciary.json
EXIT: 0
BYTES: 1375
SHA256: fa5665b1aae0a2ea5bc2227f0fa4deff1278f4595d75872ed88e994609e5d15a
NO_EOL: 0
--- OUTPUT ---
7:    "public": 26,
12:  "public_write_operations": 26,
29:   "public": true,
33:   "guarded": false,
42:   "public": true,
46:   "guarded": false,
55:   "public": true,
59:   "guarded": false,
68:   "public": true,
72:   "guarded": false,
81:   "public": true,
85:   "guarded": false,
94:   "public": true,
98:   "guarded": false,
107:   "public": true,
111:   "guarded": false,
120:   "public": true,
124:   "guarded": false,
133:   "public": false,
138:   "guarded": false,
145:   "function": "issue_ruling",
147:   "public": true,
152:   "guarded": true,
161:   "public": true,
165:   "guarded": false,
174:   "public": true,
178:   "guarded": false,
187:   "public": true,
191:   "guarded": false,
200:   "public": true,
204:   "guarded": false,
213:   "public": true,
217:   "guarded": false,
226:   "public": true,
230:   "guarded": false,
239:   "public": true,
243:   "guarded": false,
252:   "public": true,
256:   "guarded": false,
265:   "public": true,
269:   "guarded": false,
278:   "public": true,
282:   "guarded": false,
291:   "public": true,
295:   "guarded": false,
304:   "public": true,
308:   "guarded": false,
317:   "public": true,
321:   "guarded": false,
330:   "public": true,
334:   "guarded": false,
343:   "public": true,
347:   "guarded": false,
356:   "public": true,
360:   "guarded": false,
369:   "public": true,
373:   "guarded": false,
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/executive_core --json /home/user/workspace/council_w598/grok_4_7/tmp/executive_core.json
EXIT: 0
BYTES: 977
SHA256: 76d5857eaae6ac775d030e9d98feb43ab8311df548cfc2bad89b459472b8f3e4
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : federal/executive/services/src/amos_federation/services/executive_core
  مواضعُ كتابةٍ (كلُّها)   : 11
  عمليّاتٌ عامّةٌ مُغيِّرة   : 9
  منها تعبرُ الحدَّ        : 2
  مساراتٌ قديمةٌ مُغلَقة    : 1
  **لا تعبرُ الحدَّ**       : 6
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    services            9 /   2 /    6
  التوزيعُ على الملفّات:
       3  federal/executive/services/src/amos_federation/services/executive_core/repository.py
       2  federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
       1  federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py
  التفصيلُ محفوظٌ في: /home/user/workspace/council_w598/grok_4_7/tmp/executive_core.json
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py -q
EXIT: 0
BYTES: 705
SHA256: 098c4d2c8fc4573495180c4675cd17b66744a28601a567bce6f412f5a71276cc
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w598/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 7 items

federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py .. [ 28%]
.....                                                                    [100%]

============================== 7 passed in 1.65s ===============================
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py -q
EXIT: 0
BYTES: 706
SHA256: bae7c3d65529343a77ef24df81aca30728a689bafe1a05a932685d312fbd13e1
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w598/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 27 items

federal/executive/services/tests/test_r7d_federal_judiciary.py ......... [ 33%]
..................                                                       [100%]

============================== 27 passed in 4.37s ==============================
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
EXIT: 0
BYTES: 706
SHA256: 810ca86910a2cd77c739df95d1fd1d77436a9ab6bdbe1fd6e30907f33ed23d24
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w598/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 8 items

federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 12%]
.......                                                                  [100%]

============================== 8 passed in 0.56s ===============================
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
EXIT: 0
BYTES: 13549
SHA256: 7e213fac4cc70230a2b072a9db099a47d95b5a9daafa801196493290da390606
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w598/grok_4_7/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1535 items

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
.................                                                        [ 35%]
federal/executive/services/tests/test_king_login_boundary.py ........... [ 36%]
...........                                                              [ 37%]
federal/executive/services/tests/test_memory_service.py ........         [ 37%]
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
federal/executive/services/tests/test_phase1_postgres.py ssssssss        [ 46%]
federal/executive/services/tests/test_phase1_postgres_events.py ssssssss [ 47%]
sssssssss                                                                [ 47%]
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
federal/executive/services/tests/test_population.py ..................   [ 55%]
federal/executive/services/tests/test_q19_money_delegation.py .......... [ 56%]
..................                                                       [ 57%]
federal/executive/services/tests/test_q20_money_representation.py ...... [ 58%]
.ss..................                                                    [ 59%]
federal/executive/services/tests/test_q31_money_engine_wiring.py ....... [ 59%]
.....                                                                    [ 60%]
federal/executive/services/tests/test_q32_money_enforcement_surface.py . [ 60%]
..............                                                           [ 61%]
federal/executive/services/tests/test_r1_canonical_execution_path.py ... [ 61%]
..............                                                           [ 62%]
federal/executive/services/tests/test_r2_task_execution_integration.py . [ 62%]
........................                                                 [ 63%]
federal/executive/services/tests/test_r3_agent_runtime_integration.py .. [ 64%]
...........                                                              [ 64%]
federal/executive/services/tests/test_r4_agent_identity_and_population.py . [ 64%]
...............                                                          [ 65%]
federal/executive/services/tests/test_r5_multi_provider_sandbox.py ..... [ 66%]
..............                                                           [ 67%]
federal/executive/services/tests/test_r6_1_authorization_closure.py .... [ 67%]
..............                                                           [ 68%]
federal/executive/services/tests/test_r6_identity_authorization_root.py . [ 68%]
................                                                         [ 69%]
federal/executive/services/tests/test_r7_government_services.py ........ [ 69%]
........................                                                 [ 71%]
federal/executive/services/tests/test_r7_state_registry.py ............. [ 72%]
.............                                                            [ 73%]
federal/executive/services/tests/test_r7b_state_treasury.py ............ [ 73%]
........................                                                 [ 75%]
federal/executive/services/tests/test_r7c_national_registry.py ......... [ 76%]
..........................                                               [ 77%]
federal/executive/services/tests/test_r7d_federal_judiciary.py ......... [ 78%]
..................                                                       [ 79%]
federal/executive/services/tests/test_r8_federal_state_integration.py .. [ 79%]
...............................                                          [ 81%]
federal/executive/services/tests/test_r9_national_economic_state.py .... [ 81%]
.........................................                                [ 84%]
federal/executive/services/tests/test_real_tools.py .................... [ 85%]
                                                                         [ 85%]
federal/executive/services/tests/test_shadow.py ..........               [ 86%]
federal/executive/services/tests/test_step19_durable_governance_state.py . [ 86%]
.......                                                                  [ 87%]
federal/executive/services/tests/test_step7_gate_denial.py .....         [ 87%]
federal/executive/services/tests/test_tool_registry.py .......           [ 87%]
federal/executive/services/tests/test_training.py ...............        [ 88%]
federal/executive/services/tests/test_treasury.py ...................... [ 90%]
..........                                                               [ 90%]
federal/executive/services/tests/test_w032_registry_ownership.py ....... [ 91%]
......                                                                   [ 91%]
federal/executive/services/tests/test_w033_cost_record_durability.py ... [ 91%]
......                                                                   [ 92%]
federal/executive/services/tests/test_w036_cost_precision.py ........... [ 93%]
                                                                         [ 93%]
federal/executive/services/tests/test_w166_postgres_driver_declared.py . [ 93%]
...............                                                          [ 94%]
federal/executive/services/tests/test_w190_durable_model_registry.py ..  [ 94%]
federal/executive/services/tests/test_w308_test_ledger_is_per_session.py . [ 94%]
..                                                                       [ 94%]
federal/executive/services/tests/test_wi062_migrations_cover_orm_tables.py . [ 94%]
.s                                                                       [ 94%]
federal/executive/services/tests/test_wi063_tenant_isolation_http.py ..s [ 94%]
s..ss.s..ss.s.s.s..s.s.                                                  [ 96%]
federal/executive/services/tests/test_wi064_migrations_follow_orm.py .s  [ 96%]
federal/executive/services/tests/test_wi065_orm_declares_jsonb_timestamptz.py . [ 96%]
.s                                                                       [ 96%]
federal/executive/services/tests/test_wi066_convert_create_all_databases.py . [ 96%]
sssss                                                                    [ 97%]
federal/executive/services/tests/test_wi066_pg_session_isolation.py .ss  [ 97%]
federal/executive/services/tests/test_wi067_legal_search_isolated.py ... [ 97%]
....................                                                     [ 98%]
federal/executive/services/tests/test_wi076_pg_backup_restore.py ssss    [ 99%]
federal/executive/services/tests/test_wi082_agent_identity_sovereign.py . [ 99%]
.......                                                                  [ 99%]
federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py .. [ 99%]
.....                                                                    [100%]

=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w598/grok_4_7/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========== 1482 passed, 53 skipped, 1 warning in 248.69s (0:04:08) ============
Failed to export traces to localhost:4317, error code: StatusCode.UNAVAILABLE, error details: failed to connect to all addresses; last error: UNKNOWN: ipv6:%5B::1%5D:4317: Failed to connect to remote host: Connection refused
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && rg -n "JUDICIARY_ACTOR|judicial_action|position_scope|guard_declared\(" federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py federal/executive/services/src/amos_federation/services/federal_judiciary/service.py federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py
EXIT: 0
BYTES: 2098
SHA256: a7e12b09057f81d76ef586a84acb99fb9cf84e416f4000b14ca8560a1c37c359
NO_EOL: 0
--- OUTPUT ---
federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py:76:JUDICIARY_ACTOR = "JUDICIAL"
federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py:85:        _DEFAULT_JUDICIARY_AUTHORIZER = ConstitutionalAuthorizer(actor=JUDICIARY_ACTOR)
federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py:218:    def _judicial_action() -> Any:
federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py:235:            actor_scope=authority.position_scope or "",
federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py:324:    guarded = _judiciary_authorizer().guard_declared(
federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py:343:        judicial_action=_judicial_action(),
federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:128:    def guard_declared(
federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:138:        judicial_action: Any | None = None,
federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:356:    def guard_declared(
federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:366:        judicial_action: Any | None = None,
federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:393:            judicial_action=judicial_action,
federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py:103:    position_scope: str | None = None
federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py:120:            "position_scope": self.position_scope,
federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py:231:            position_scope=holding.authority_scope, court_jurisdiction=court.jurisdiction
federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py:250:        "position_scope": holding.authority_scope,
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
EXIT: 0
BYTES: 23426
SHA256: 4a672ea52a35556d1c558fc8cf3ea5e4d8c5de1d8f2f162f77a2f3f9e475c55f
NO_EOL: 0
--- OUTPUT ---
# J1 · WI-105 — تصميمُ عبورِ `issue_ruling` الحدَّ السياديَّ بفاعلٍ قضائيٍّ مُعلَنٍ (Q-6 ①)

<!--
الهدف: وثيقةُ تصميمِ الدفعةِ J1 من خطّةِ حرقِ D-4 — عبورُ إصدارِ الحكمِ الحدَّ السياديَّ بفاعلٍ قضائيٍّ مُعلَنٍ، تُلتزَمُ قبلَ أيِّ شِفرةٍ
النطاق: بندُ WI-105 (federal-executive · services/federal_judiciary + جسرُ executive_core) — فئةُ التغييرِ C3 (حسّاسٌ: سيادةٌ بقائمةِ Q-H)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — بتوجيهِ المالكِ 17 § 3 المرحلةُ 1 — لا شِفرةَ قبلَ اعتمادِ هذه الوثيقةِ
تاريخ الإنشاء: 2026-10-21
<!-- آخر تعديل: 2026-10-21 (W-593 — إضافتان مؤرَّختان: الجيلُ في هدفِ العبورِ · وقياسُ T6 عبرَ حارسِ 1I) -->
-->

> **السند:** قرارُ المالكِ **Q-6 ①** (W-363): «قضاءٌ مستقلٌّ بفاعلٍ قضائيٍّ مُعلَنٍ ← لا يخلطُ السلطاتِ ولا يحتاجُ تفويضًا لكلِّ فعلٍ» — ويفتحُ هجرةَ `federal_judiciary` «في T1 بعدَ هجرةِ Q-15» · وهجرةُ Q-15 (`WI-082`) صارت `VERIFIED` بإجماعِ المجلسِ في `W-576` · والدفعةُ في `HANDOFFS/D4-BURN-PLAN.md` باسمِ **J1**.
> **البروتوكولُ (C3):** هذه الوثيقةُ في التزامٍ يسبقُ الشِفرةَ · ثمَّ جولةُ مجلسٍ على الوثيقةِ · ثمَّ عرضُها على المالكِ · **ولا شِفرةَ قبلَ الموافقةِ** (التوجيهُ 17 § 3 · المرحلةُ 1 · البندُ 4).
> **كلُّ رقمٍ هنا مقيسٌ في W-581 على العقدةِ `2694796`** بالأمرِ المذكورِ بجانبِه — ويُعادُ قياسُه في الدفعةِ التي تُنفِّذُ.

## 1. الوضعُ المقيسُ

### 1.1 الموضعانِ في الجرد

`sovereign_write_inventory.py --service …/federal_judiciary --json` (27 موضعًا في الوحدةِ · كلُّها غيرُ محروسةٍ):

| الموضع | الكتابة | الحالة |
|---|---|---|
| `rulings.py::issue_ruling` | `add()` (صفُّ الحكمِ) ثمَّ `flush` ثمَّ `docket.record_proceeding` ثمَّ `docket.advance_case` | دَينٌ |
| `service.py::FederalJudiciary.issue_ruling` | `commit()` | دَينٌ |

قاعدةُ الأداةِ (رأسُ `sovereign_write_inventory.py`): **الموضعُ محروسٌ إن ظهرَ `guard_declared(` في جسمِ الدالّةِ العامّةِ نفسِها** — لا يكفي أن يعبرَ معاونٌ · ومعاونٌ خاصٌّ يكتبُ ولا تصلُ إليه عمليّةٌ عامّةٌ في وحدتِه يُحصى موضعًا مستقلًّا (فإعادةُ التسميةِ إلى `_` لا تُخفي شيئًا).

### 1.2 النداءات

- إنتاجيًّا: **1** — `service.py:672` يُنادي `rulings.issue_ruling` · ولا مُنادٍ آخرَ (`rg 'rulings\.issue_ruling|issue_ruling\('`).
- الاختباراتُ: **18** نداءً لـ`judiciary.issue_ruling` (الخدمة) في `tests/test_r7d_federal_judiciary.py` — منها مسارُ «الحكمُ البديلُ بعدَ الإلغاءِ» (السطورُ 1049–1075).
  - **[W-584 · 2026-10-21 · تصحيحٌ بالإضافةِ لا بالمحوِ — `DISC-124`]** المقيسُ **15** لا 18: `rg -c "judiciary\.issue_ruling\(" federal/executive/services/tests/test_r7d_federal_judiciary.py` ⇒ `15` · و`rg -c "\.issue_ruling\("` على `federal/executive/services/tests` كلِّها ⇒ ملفٌّ واحدٌ · 15 — فلا نداءَ في غيرِه. والرقمُ 18 أعلاه باقٍ تاريخًا بنِسبتِه (W-581) · ولا أثرَ له في التصميمِ: المعيارُ «test_r7d كاملًا بلا تعديلٍ» لا يتوقّفُ على العدِّ.

### 1.3 الحدُّ اليومَ — ثلاثُ حقائقَ مقيسةٍ تُغيِّرُ التصميمَ عن WI-082

مقيسةٌ بـ`docs/audit/evidence/W-581/probe_issue_ruling_actors.py` (المخرجُ كاملًا بجانبِه):

1. **الجسرُ لا يحملُ طلبَ الاختصاصِ:** `ConstitutionalAuthorizer.guard_declared` (`sovereignty_bridge.py:355`) لا يقبلُ `judicial_action` ولا يُمرِّرُه، والحدُّ الجوهريُّ `EnforcementBoundary.execute` يقبلُه (`enforcement_boundary.py:300`) ويرفضُ كلَّ فعلٍ في `JUDICIAL_ACTIONS` بلا طلبٍ (`_guard_jurisdiction` · `JurisdictionNotDeclaredError`) ⇒ **عبرَ الجسرِ اليومَ يُرفَضُ `issue_ruling` لكلِّ فاعلٍ بلا استثناءٍ (6/6)** — فلا تُهاجَرُ الدفعةُ بلا توسيعِ الجسرِ.
2. **الحكمُ عبرَ الحدِّ الجوهريِّ بطلبِ اختصاصٍ ومُعوِّضٍ:** `JUDICIAL` ⇒ تنفيذٌ · `EXECUTIVE` و`LEGISLATIVE` و`TREASURY` ⇒ `SovereigntyViolation` (A003 · الفصلُ بينَ السلطاتِ) · **و`AGENT` و`SYSTEM` ⇒ تنفيذٌ** (يُراجَعانِ في طبقةِ `AGENT` وقاعدةُ الحصرِ `_BRANCH_EXCLUSIVE` في `rules.py:272` تخصُّ الفروعَ وحدَها) — **اكتشافُ `DISC-121`** وسؤالُ `Q-68` للمالكِ · خارجَ J1 ولا تحسمُه J1.
3. **الجدارُ يعملُ:** نطاقُ محكمةٍ ≠ نطاقِ قضيّةٍ ⇒ `JurisdictionError` · ونطاقُ منصبٍ `DEPARTMENT` ⇒ `JurisdictionError` · وأثرٌ مُغيِّرٌ بلا مُعوِّضٍ ⇒ `CompensationNotDeclaredError`.

وحقيقتانِ أُخرَيانِ: `issue_ruling` **غيرُ مُدرَجٍ في أيِّ مستوًى** من `KILL_SWITCH_BLOCKS` (`rules.py:141`) · و`JUDICIAL_EFFECT_KINDS` = {CREATE · WRITE · READ} و`DELETE` في `NON_JUDICIAL_EFFECT_KINDS` («الحذفُ شأنٌ تنفيذيّ» — `jurisdiction.py:152–167`).

## 2. التصميم

### D1 · الفاعلُ القضائيُّ المُعلَنُ — ثابتٌ في الوحدةِ لا معاملٌ للمُنادي

- `federal_judiciary/rulings.py`: `JUDICIARY_ACTOR = "JUDICIAL"` ومُفوِّضٌ افتراضيٌّ كسولٌ `_judiciary_authorizer()` على مثالِ `agent_identity._default_authorizer` (WI-082).
- **فرقٌ مقصودٌ عن WI-082:** لا يُضافُ معاملٌ عامٌّ `authorizer=` إلى `rulings.issue_ruling` ولا إلى الخدمة. السببُ مقيسٌ (§ 1.3 · 2): من يملكُ أن يُمرِّرَ مُفوِّضًا بفاعلِ `AGENT` يُصدِرُ حكمًا اليومَ. فاختيارُ الفاعلِ يبقى في الوحدةِ وحدَها (نصُّ Q-6: «فاعلٌ قضائيٌّ مُعلَنٌ»).
- الاختبارُ يُبدِّلُ الفاعلَ بـ`monkeypatch` على ثابتِ الوحدةِ (ويُفرِغُ المُفوِّضَ المحفوظَ) لا بمعاملٍ إنتاجيٍّ.
- البديلُ المرفوضُ: معاملٌ اختياريٌّ كـWI-082 — يُبقي ثغرةَ `DISC-121` مفتوحةً لكلِّ مُنادٍ.

### D2 · توسيعُ الجسرِ — `judicial_action` اختياريٌّ يُمرَّرُ كما هو

- `sovereignty_bridge.py`: `guard_declared(..., judicial_action: Any | None = None)` في البروتوكولِ (`:128`) والتنفيذِ (`:355`) — ويُمرَّرُ إلى `self.boundary.execute(..., judicial_action=judicial_action)`.
- **بلا أثرٍ على غيرِ القضائيِّ:** القيمةُ الافتراضيّةُ `None` هي افتراضُ `execute` نفسِه، فكلُّ نداءٍ قائمٍ يبقى بايتًا ببايتٍ في سلوكِه — ويُثبَتُ ذلك بتشغيلِ فحوصِ WI-082 وحزمةِ الجسرِ كاملةً بلا تعديلٍ.
- لا يُخفَّفُ شيءٌ: الجسرُ لا يقرِّرُ الاختصاصَ، الجدارُ (`JudicialJurisdictionWall.evaluate`) يقرِّرُه.

### D3 · طلبُ الاختصاصِ منَ البياناتِ الحيّةِ لا من ثوابتَ

`JudicialAction(action="issue_ruling", court_scope=…, case_scope=…, actor_scope=…, target=…, institution_id=…, case_institution_id=…)`:

| الحقل | المصدر | ملاحظة |
|---|---|---|
| `court_scope` | `authority.jurisdiction` (= `court.jurisdiction`) | موجودٌ اليومَ |
| `case_scope` | `case.jurisdiction` | موجودٌ اليومَ |
| `actor_scope` | `holding.authority_scope` | **حقلٌ جديدٌ `position_scope` في `JudicialAuthority`** (إضافةٌ لا تغييرٌ — يُملأُ في `require_judicial_authority`) |
| `institution_id` | `authority.institution_id` (= `court.institution_id`) | موجودٌ |
| `case_institution_id` | `court.institution_id` | القضيّةُ بلا عمودِ مؤسّسةٍ؛ مؤسّستُها مؤسّسةُ محكمتِها (`models.py` · `LegalCaseModel`) — مُعلَنٌ لا مُخمَّنٌ |
| `is_royal_decree_target` | `False` | إصدارُ الحكمِ هنا على قضيّةٍ لا على مرسومٍ · والجدارُ يقبلُ `issue_ruling` على المرسومِ أصلًا (`jurisdiction.py:341`) |

فالفحصُ المكرَّرُ اليومَ في `authority.py` (`assert_scope_covers_court` · `assert_jurisdiction_match`) يُفحَصُ ثانيةً في الحدِّ نفسِه — ازدواجٌ مقصودٌ: الأوّلُ قاعدةُ نطاقٍ قبلَ الحدِّ، والثاني قرارُ الحدِّ.
ملاحظةٌ مقيسةٌ عرَضًا (لا تُصلَحُ في J1): `authority.py:281` يمرِّرُ `case_institution_id=court.institution_id` لا مؤسّسةَ القضيّةِ — وهو مسارٌ `pragma: no cover` ولا عمودَ للقضيّةِ أصلًا؛ يُذكَرُ ولا يُغيَّرُ.

### D4 · موضعُ العبورِ ومِلكيّةُ المعاملةِ — العبورُ حيث الكتابةُ

- **العبورُ في `rulings.issue_ruling`** (حيث يُكتَبُ الصفُّ): جسمُها يحملُ `guard_declared(` والمُطبِّقُ يُنفِّذُ `add` + `flush` + `record_proceeding` + `advance_case` **+ `session.commit()`** في معاملةٍ واحدةٍ.
- **`service.issue_ruling` يفقدُ `session.commit()`** (الالتزامُ صارَ داخلَ العبورِ) ويبقى مالكَ الجلسةِ (`session.close()` في `finally`) والنشرِ والأثرِ.
- **أثرُه في الجردِ (يُعلَنُ قبلَ القياسِ):** `rulings.issue_ruling` محروسٌ (sovereign 17 ← 18) · و`service.issue_ruling` **يخرجُ من الجردِ لأنّه لم يعدْ يكتبُ** (أسطحٌ 220 ← 219) · **D-4: 183 ← 181**. وهذا ليس تجميلًا للعدِّ: الكتابةُ الوحيدةُ للحكمِ صارت خلفَ الحدِّ، والخدمةُ مُنسِّقٌ لا كاتبٌ. **نقطةُ حكمٍ للمجلسِ.**
  - **[W-588 · 2026-10-21 · تصحيحٌ بالإضافةِ لا بالمحوِ — `DISC-126` · وجدَه مقعدُ grok_4_7 في جولةِ W-585]** «أسطحٌ 220 ← 219» **غلطٌ**: المُطبِّقُ (`_apply`) دالّةٌ متداخلةٌ خاصّةٌ داخلَ `rulings.issue_ruling` على نمطِ WI-082 (`agent_identity._apply`)، وهي تحملُ `add` + `session.commit()` فتُحصى موضعَ كتابةٍ مستقلًّا (public=False) ⇒ **أسطحٌ 220 ← 220** (‏−1 بخروجِ `service.issue_ruling` · +1 بالمُطبِّقِ) · والدَّينُ **183 ← 181** والسياديُّ **17 ← 18** على حالِهما (المُطبِّقُ غيرُ عامٍّ فلا يدخلُ مقامَ الدَّينِ) · الدليلُ `evidence/W-587/coordinator_check_grok_d4.txt`. **وشكلُ المُطبِّقِ يصيرُ جزءًا من التصميمِ لا تفصيلَ تنفيذٍ**: دالّةٌ متداخلةٌ خاصّةٌ واحدةٌ — فإن نفّذَها المنفِّذُ بغيرِ هذا الشكلِ تغيّرَ عدُّ الأسطحِ ووجبَ إعلانُه قبلَ القياسِ.
- البديلُ A2: العبورُ في الخدمةِ ويبقى `rulings.issue_ruling` عامًّا بلا عبورٍ ⇒ مدخلٌ عامٌّ يكتبُ حكمًا متجاوزًا الحدَّ (183 ← 182) — **مرفوضٌ**: الثغرةُ تبقى.
- البديلُ A3: عبورانِ متداخلانِ (الخدمةُ ثمَّ `rulings`) ⇒ قراران في سجلِّ البوابةِ ومفتاحا ذرّيّةٍ لحكمٍ واحدٍ — **مرفوضٌ**: سجلٌّ مُضلِّلٌ.

### D5 · الأثرُ المُعلَنُ — أثرٌ واحدٌ لمعاملةٍ واحدةٍ

`declared_effect("CREATE", f"judiciary/rulings/{case_id}/{stage}", "حكمٌ في المرحلة … وإجراؤه وانتقالُ القضيّةِ إلى decided")` — `CREATE` ∈ `JUDICIAL_EFFECT_KINDS` فيمرُّ `assert_effect_judicial`. الصفوفُ الثلاثةُ (الحكمُ · الإجراءُ · حالةُ القضيّةِ) تُلتزَمُ معًا أو لا يُلتزَمُ شيءٌ، فإعلانُها ثلاثةَ آثارٍ يَعِدُ بتطبيقٍ جزئيٍّ لا يقعُ.

**[إضافةٌ مؤرَّخةٌ (2026-10-21 · `W-593` · اكتشافُ تنفيذٍ أُثبِتَ بالفحصِ قبلَ الدفعِ):]** هدفُ العبورِ وموردُ الأثرِ يحملانِ الجيلَ أيضًا: `judiciary/rulings/{case_id}/{stage}/g{n}` — لا `f"{case_id}/{stage}"` وحده. السببُ مقيسٌ: بصمةُ العقدِ تُشتقُّ من (الفاعلِ · الفعلِ · الهدفِ · الآثارِ) فقط، ومعرِّفُ الإذنِ `EP-{contract}-{ثانيةٌ}` بدقّةِ الثانيةِ، فحكمانِ للمرحلةِ نفسِها في الثانيةِ نفسِها يتصادمانِ في الإذنِ نفسِهِ ويُرفضُ البديلُ بعدَ الإلغاءِ رفضَ إعادةِ إذنٍ (`PermitReplayError` — قِيسَ في T4 قبلَ التصحيحِ). والجيلُ جزءُ هويةِ العمليّةِ في المفتاحِ والهدفِ معًا، فالدلالةُ كما هي: أثرٌ واحدٌ لمعاملةٍ واحدةٍ (D5).

### D6 · مفتاحُ الذرّيّةِ — بجيلِ الإلغاءِ لا بالمرحلةِ وحدَها

- `operation_key("judiciary.ruling.issue", f"{case_id}:{stage}:g{n}")` و`n` = عددُ الأحكامِ المُلغاةِ (`vacated`) للقضيّةِ في المرحلةِ — يُقرأُ قبلَ الحدِّ.
- **لماذا لا `case_id:stage`:** بعدَ الإلغاءِ يُسمَحُ حكمٌ بديلٌ للمرحلةِ نفسِها (الاختبارُ القائمُ 1069) — فمفتاحٌ بلا جيلٍ يُعيدُ الحكمَ الأوّلَ «إعادةً» ولا يكتبُ البديلَ.
- **ترتيبٌ ملزِمٌ:** فحصُ «حكمٌ قائمٌ للمرحلةِ» (`DuplicateRulingError`) يبقى **قبلَ** الحدِّ — وإلّا عادَ الطلبُ الثاني إعادةً صامتةً للأوّلِ (المفتاحُ نفسُه `g0`) بدلَ الرفضِ الذي يفرضُه الاختبارُ القائمُ (السطورُ 1055–1061).
- **الإعادةُ:** إن رجعَ الحدُّ `is_replay` يُقرأُ الحكمُ القائمُ للمرحلةِ؛ فإن غابَ رُفِعَ `RulingLedgerDivergenceError` (على مثالِ `IdentityLedgerDivergenceError` في WI-082) — لا كتابةَ ثانيةً خارجَ الحدِّ.

### D7 · المُعوِّضُ — استعادةٌ تقنيّةٌ دقيقةٌ أم إلغاءٌ قضائيٌّ؟ (نقطةُ حكمٍ)

متى يعملُ (مقيسٌ في `compensation.py:797–808`): بعدَ تسجيلِ الأثرِ «مُطبَّقًا» وفشلِ خطوةٍ لاحقةٍ (مثلًا تثبيتُ النجاحِ في سجلِّ الذرّيّةِ) — أي والصفوفُ مُلتزَمةٌ.

| الخيار | ما يفعل | له | عليه |
|---|---|---|---|
| **(أ) الاستعادةُ التقنيّةُ — التوصية** | في جلسةٍ جديدةٍ: حذفُ صفِّ الإجراءِ (آخرُ تسلسلٍ للقضيّةِ) وصفِّ الحكمِ بمعرِّفَيهما، وإرجاعُ حالةِ القضيّةِ إلى ما كانت قبلَ العمليّةِ (تُحفَظُ قبلَ الحدِّ) | الحالةُ ترجعُ كما كانت بالضبطِ (`state_is_clean`) · والعمليّةُ لم تثبتْ فلا حكمَ قانونيًّا وُجِدَ | «الحذفُ شأنٌ تنفيذيّ» — والمُعوِّضُ ليس أثرًا مُعلَنًا ولا تراجعُه البوابةُ، فيُكتَبُ ذلك في شِفرتِه صريحًا |
| (ب) الإلغاءُ القضائيُّ | `status="vacated"` بسببٍ «تعويضٌ: لم يثبتْ نجاحُ العمليّةِ» | لا حذفَ | القضيّةُ تبقى `decided` بلا حكمٍ قائمٍ — حالةٌ متناقضةٌ · ويرفعُ جيلَ المفتاحِ (D6) بحكمٍ لم يصدرْ |

### D8 · ما يبقى قبلَ الحدِّ (قراءاتٌ لا كتابات)

`require_domain_permission` · `require_tenant` · `require_judicial_authority` (PROVEN) · فحوصُ المدخلِ (المرحلة · القرار · المنطوق) · فحصُ الحكمِ القائمِ · قراءةُ جيلِ الإلغاءِ وحالةِ القضيّةِ السابقةِ. ترتيبُ الأخطاءِ المرئيُّ للمُنادي لا يتغيّرُ.

### D9 · ما لا يتغيّرُ ويُعلَنُ

- زرُّ الإيقافِ: `issue_ruling` غيرُ مُدرَجٍ في أيِّ مستوًى — لا تُضيفُه J1 (مستويات الإيقافِ قرارُ مالكٍ).
- `rules.py` و`jurisdiction.py` و`royal/`: لا مساسَ · وثغرةُ `DISC-121` لا تُصلَحُ هنا (`Q-68`).
- `vacate_ruling` (J2) · `record_proceeding` العامُّ (J3) · وبقيّةُ الوحدةِ: خارجَ J1.

## 3. الفحوصُ والطفراتُ (تُكتَبُ في الدفعةِ المنفِّذةِ)

ملفٌّ جديدٌ `federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py`:

| الفحص | يُثبِت |
|---|---|
| T1 · ALLOW للقضائيّ | الحكمُ يصدرُ عبرَ الخدمةِ · وآخرُ قرارٍ في سجلِّ البوابةِ `issue_ruling` بفاعلِ `judicial` · والصفوفُ الثلاثةُ مُلتزَمةٌ |
| T2 · DENY للتنفيذيّ | `JUDICIARY_ACTOR="EXECUTIVE"` ⇒ `SovereigntyViolation` · لا صفَّ حكمٍ · لا إجراءَ · حالةُ القضيّةِ كما كانت |
| T3 · الاختصاصُ منَ البيانات | الطلبُ المُمرَّرُ يحملُ `case.jurisdiction` و`position_scope` الحقيقيَّينِ (جاسوسٌ على `boundary.execute`) |
| T4 · البديلُ بعدَ الإلغاء | حكمٌ ← إلغاءٌ ← بديلٌ = صفّانِ بمفتاحَي `g0` و`g1` |
| T5 · المكرَّرُ قبلَ الحدّ | الطلبُ الثاني للمرحلةِ ⇒ `DuplicateRulingError` ولا قرارَ جديدٌ في سجلِّ البوابةِ |
| T6 · المُعوِّض | إسقاطُ تثبيتِ النجاحِ بعدَ الالتزامِ ⇒ `CompensationRequired` و`state_is_clean` والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ |
  **[إضافةٌ مؤرَّخةٌ (2026-10-21 · `W-593` · اكتشافُ تنفيذٍ):]** مسارُ الحدِّ أحاديَّ الأثرِ ينفّذُ عبرَ `IdempotencyGuard.run_once` لا عبرَ معاملةِ 1I المُعوَّضةَ (`run_compensated_transaction` موجودةٌ في `compensation.py` ولا مُناديَ إنتاجيًّا لها)، فالتعويضُ الآليُّ غيرُ موصولٍ في هذا المسارِ. فيُقاسُ T6 كما تقيسُهُ حوكمةُ 1I: بإسقاطِ تثبيتِ النجاحِ بعدَ الالتزامِ (الصفوفُ مُلتزَمةٌ والسجلُّ RUNNING) ثمّ التعويضِ بحارسِ 1I (`CompensationGuard.compensate`) بالعقدِ والخطةِ المربوطتينِ منَ العبورِ الحقيقيِّ نفسِهِ — والحصيلةُ `state_is_clean` والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ. ووصلُ التعويضِ الآليِّ في `enforcement_boundary.py` خارجَ ملفّاتِ J1 (§ 5) فيُترَكُ قرينةً للمجلسِ لا يقرّرُهُ المنفِّذُ. |
| T7 · التفرُّق | إعادةٌ وصفُّ الحكمِ غائبٌ ⇒ `RulingLedgerDivergenceError` |

الطفراتُ (تُشغَّلُ على نسخةٍ مؤقّتةٍ وتُقيَّدُ مخرجاتُها):
- **M1 · حذفُ العبورِ** (المُطبِّقُ يُنادى مباشرةً بلا `guard_declared`) ⇒ يسقطُ T1 وT2 (شرطُ التوجيهِ 17).
- M2 · مفتاحٌ بلا جيلٍ ⇒ يسقطُ T4.
- M3 · فحصُ المكرَّرِ بعدَ الحدِّ ⇒ يسقطُ T5.
- M4 · `judicial_action=None` في `rulings` ⇒ يسقطُ T1 (`JurisdictionNotDeclaredError`).

## 4. معيارُ القبولِ الرقميُّ

1. `sovereign_write_inventory.py`: **debt 183 ← 181** · sovereign 17 ← 18 · أسطحٌ 220 ← 219 (**[W-588] الصحيحُ 220 ← 220** — المُطبِّقُ المتداخلُ الخاصُّ يُحصى موضعًا · `DISC-126`) · بلا نموٍّ في غيرِ الوحدةِ.
2. T1–T7 ناجحةٌ · M1–M4 كلٌّ يُسقِطُ فحصَه.
3. `test_r7d_federal_judiciary.py` كاملًا بلا تعديلٍ (18 نداءً — **[W-584] المقيسُ 15** · `DISC-124`) · وفحوصُ WI-082 والجسرِ بلا تعديلٍ.
4. حزمُ services كاملةً خضراءَ في CI مقروءًا على العقدةِ نفسِها.
5. مراجعةٌ تُعيدُ التشغيلَ (Q-H) — ولا VERIFIED بيدِ المنفِّذِ.

## 5. الملفّاتُ التي ستُمَسُّ (ولا غيرُها)

`executive_core/sovereignty_bridge.py` · `federal_judiciary/rulings.py` · `federal_judiciary/service.py` · `federal_judiciary/authority.py` · `tests/test_wi105_issue_ruling_sovereign.py` (جديد) · دعاوى عددِ الحزمةِ في `docs/PROJECT_HANDBOOK.md`.

## 6. نقاطُ الحكمِ المطلوبةُ (للمجلسِ ثمَّ للمالكِ)

| النقطة | السؤال | التوصية |
|---|---|---|
| D1 | الفاعلُ ثابتٌ في الوحدةِ بلا معاملٍ عامٍّ؟ | نعم |
| D4 | العبورُ في `rulings` والالتزامُ داخلَه فتخرجُ الخدمةُ منَ الجردِ (183 ← 181)؟ | نعم |
| D6 | المفتاحُ بجيلِ الإلغاءِ والمكرَّرُ قبلَ الحدِّ؟ | نعم |
| D7 | المُعوِّضُ (أ) الاستعادةُ التقنيّةُ أم (ب) الإلغاءُ؟ | (أ) |

لا نقطةَ منها تمسُّ سؤالًا سياديًّا غيرَ محسومٍ: الفاعلُ محسومٌ بـQ-6 ① · وثغرةُ AGENT/SYSTEM منفصلةٌ في `Q-68` ولا تعتمدُ J1 عليها.
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && cat docs/audit/evidence/W-593/mutation_m1.txt docs/audit/evidence/W-593/mutation_m2.txt docs/audit/evidence/W-593/mutation_m3.txt docs/audit/evidence/W-593/mutation_m4.txt
EXIT: 0
BYTES: 2464
SHA256: a914c5a29605c919408927bd73ce8f68d33cdcfc9795f64edd5ccb395a7a1a56
NO_EOL: 0
--- OUTPUT ---
== M1: حذف العبور (المطبق ينادى مباشرة بلا guard_declared) ==
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t1_issue_ruling_crosses_boundary_as_judicial
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t2_executive_actor_is_denied
============================== 2 failed in 1.22s ===============================
== M2: مفتاح بلا جيل الإلغاء (أُعيد تطبيقُها بعد اكتشافِ عدم انطباقِ النسخةِ الأولى) ==
core/sovereignty/idempotency.py:846: in _reserve_or_replay
    raise IdempotencyKeyReuseError(
E   core.sovereignty.idempotency.IdempotencyKeyReuseError: المفتاحُ «judiciary.ruling.issue:lcs-ac21cfcd-2ae4-4f8c-b56c-27d395fa1613:FIRST_INSTANCE» مُستعمَلٌ ببصمةٍ مختلفة.
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t4_replacement_after_vacation_uses_new_generation
============================== 1 failed in 1.11s ===============================
== M3: فحص المكرر بعد الحد (حذف الفحص القائم قبل الحد) ==
E   AttributeError: 'NoneType' object has no attribute 'id'
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t5_duplicate_rejected_before_boundary
============================== 1 failed in 1.10s ===============================
== M4: judicial_action=None في rulings ==
    raise JurisdictionNotDeclaredError(
E   core.sovereignty.enforcement_boundary.JurisdictionNotDeclaredError: الفعلُ «issue_ruling» قضائيٌّ ولم يُقدَّم له طلبُ اختصاصٍ مُعلَن. الجدارُ لا يُفحَصُ بالنيّة، ولا يعبرُ فعلٌ قضائيٌّ بلا نطاقِ محكمةٍ ونطاقِ قضيّةٍ ونطاقِ منصبٍ مُصرَّحٍ بها.
=========================== short test summary info ============================
FAILED federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py::test_wi105_t1_issue_ruling_crosses_boundary_as_judicial
============================== 1 failed in 1.02s ===============================
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && cat docs/audit/evidence/W-593/measurements.txt
EXIT: 0
BYTES: 4025
SHA256: fd5e9f7faef4eba157904e7d08c753e3ef3406c904636adc52d1a976ec5c25f7
NO_EOL: 0
--- OUTPUT ---
# قياساتُ دفعةِ W-593 (2026-10-21) — كلُّ رقمٍ هنا مقيسٌ بأمرِهِ

== الجردُ السياديُّ (tools/audit/sovereign_write_inventory.py) ==
قبل (رأسُ main = d0932c51 · وقياسُ W-581 أساسُ التصميمِ):
  مواضعُ كتابةٍ (كلُّها): 220 · عمليّاتٌ عامّةٌ: 202 · تعبرُ الحدَّ: 17 · لا تعبرُ (الدَّينُ): 183
  [تصحيحٌ مؤرَّخٌ (2026-10-21 · W-596): كانَ مكتوبًا هنا «عامّةٌ: 201» وهو خطأٌ — قيمةُ «قبل» هي 202 كما نشرَها final_audit_p14 قبلَ تجديدِه (قِيسَت النسبُ: منشورٌ 202 · مقيسٌ 201) — خدمةُ issue_ruling خرجَت منَ العامةِ (202←201) والمُطبِّقُ المتداخلُ خاصٌّ لا عامٌّ]
  الوحدةُ (federal_judiciary): 27 موضعًا · كلُّها عامّةٌ · 0 تعبرُ
بعد (شجرةُ العملِ قبلَ الالتزامِ):
  مواضعُ كتابةٍ (كلُّها): 220 · عمليّاتٌ عامّةٌ: 201 · تعبرُ الحدَّ: 18 · لا تعبرُ (الدَّينُ): 181
  الوحدةُ: 27 موضعًا (−1 خروجُ service.issue_ruling منَ الكتابةِ · +1 المُطبِّقُ المتداخلُ) · عامّةٌ 26 · تعبرُ 1
⇒ الدَّينُ 183←181 · السياديُّ 17←18 · الأسطحُ 220←220 (تنبّأَ بهِ تصحيحُ W-588/DISC-126)

== فحوصُ T1–T7 (ملفٌّ جديدٌ: federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py) ==
الأمرُ: AMOS_DATABASE_URL="sqlite:////tmp/amos_w593.db" .venv/bin/python -m pytest federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py -q
المخرجُ: 7 passed in 1.63s

== الطفراتُ M1–M4 (على نسخةٍ مؤقّتةٍ ثمّ استعادةُ الأصلِ — diff فارغٌ بعدَها) ==
M1 حذفُ العبورِ (المُطبِّقُ يُنادى مباشرةً): T1 وT2 سقطَا (2 failed)
M2 مفتاحٌ بلا جيلٍ: T4 سقطَ (IdempotencyKeyReuseError) — أُعيدَ تطبيقُها يدويًّا بعدَ اكتشافِ عدمِ انطباقِ النسخةِ الأولى (التنسيقُ أحاديُّ السطرِ)
M3 فحصُ المكرَّرِ بعدَ الحدِّ (حذفُ الفحصِ القائمِ): T5 سقطَ
M4 judicial_action=None: T1 سقطَ (JurisdictionNotDeclaredError)

== الفحوصُ القائمةُ بلا تعديلٍ ==
test_r7d_federal_judiciary.py: 27 passed (git diff فارغٌ على الملفِّ)
test_wi082_agent_identity_sovereign.py: 8 passed (بلا تعديلٍ)

== حزمةُ services كاملةً ==
الأمرُ: AMOS_DATABASE_URL="sqlite:////tmp/amos_w593.db" .venv/bin/python -m pytest federal/executive/services/tests -q
المخرجُ: 1482 passed, 53 skipped in 261.63s (كانَتْ 1475+53 · الزيادةُ 7 فحوصِ T1–T7)

== حزمةُ الجذرِ ==
pytest tests/ -q --collect-only ⇒ 2706 tests collected (بلا تغييرٍ)

== الملفّاتُ الممسوسةُ ==
federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py (D2)
federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py (العبورُ)
federal/executive/services/src/amos_federation/services/federal_judiciary/service.py (فقدَ commit)
federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py (position_scope)
federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py (جديد · T1–T7)
docs/audit/J1_ISSUE_RULING_DESIGN.md (إضافتانِ مؤرَّختانِ) · docs/PROJECT_HANDBOOK.md (دعاوى الحزمةِ) · وثائقُ الحالةِ
(ولا غيرُها — § 5 من التصميمِ)

== حكمُ CI على رأسِ W-592 (N+1) ==
التشغيلُ 39661440605 · مقروءٌ أخضرُ 13/13 على العقدةِ d0932c51 — الدليلُ: ci_verdict_39661440605.txt
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/grok_4_7/tmp/amos_seat.db .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_step7_factory_surfaces.py -q
EXIT: 0
BYTES: 100
SHA256: eb5d5ea3076f9d03e1d580213d4bf1ae8b9d3c2c0f37224dcd67a937ec749451
NO_EOL: 0
--- OUTPUT ---
....................                                                     [100%]
20 passed in 27.78s
=== RAW [19] END ===
=== RAW [20] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && git diff d0932c51 HEAD -- tests/governance docs/audit/measurements
EXIT: 0
BYTES: 14789
SHA256: b3fd10af46eb214911ac22d0d4944a5b8d51d02538544a385cd02be905d04bfd
NO_EOL: 0
--- OUTPUT ---
diff --git a/docs/audit/measurements/decision_gate_ledger.json b/docs/audit/measurements/decision_gate_ledger.json
index f0f8951..1d7200a 100644
--- a/docs/audit/measurements/decision_gate_ledger.json
+++ b/docs/audit/measurements/decision_gate_ledger.json
@@ -157,6 +157,22 @@
    "kind": "work_drift",
    "reason": "استعادةُ شِفرةِ WI-082 فوقَ المعالجةِ (W-465 · قرارُ المالكِ Q-51 ③): يعودُ الدَّينُ 184 ← 183 — نقضُ ارتدادِ W-427 عينِهِ (موقعُ كتابةٍ واحدٍ في agent_identity عادَ محروسًا · sovereign 16 ← 17 · write_sites 219 ثابتةٌ) — استرجاعُ قيمةِ ما قبلَ الارتدادِ لا خفضٌ جديدٌ لخطِّ الأساسِ",
    "recorded_at": "2026-10-18T20:28:21+00:00"
+  },
+  {
+   "debt": 181,
+   "sovereign": 18,
+   "closed_legacy": 7,
+   "write_sites_total": 220,
+   "git_head": "c225a9e",
+   "waves": {
+    "W1": 50,
+    "W2": 34,
+    "W3": 97
+   },
+   "decision": "W-593",
+   "kind": "work_drift",
+   "reason": "تنفيذُ J1 (بندُ WI-105 · بقرارِ المالكِ Q-69/D17-6): عبورُ issue_ruling الحدَّ السياديَّ — دَينٌ 183←181 (الوحدةُ: −1 خروجُ service.issue_ruling منَ الكتابةِ · +1 المُطبِّقُ المتداخلُ · sovereign 17←18) · W1: 52←50 · write_sites 220←220 (تنبّأَ بهِ تصحيحُ W-588/DISC-126)",
+   "recorded_at": "2026-10-21T20:10:56+00:00"
   }
  ]
 }
diff --git a/docs/audit/measurements/decision_wave_map.json b/docs/audit/measurements/decision_wave_map.json
index 8c18df6..cc1f16c 100644
--- a/docs/audit/measurements/decision_wave_map.json
+++ b/docs/audit/measurements/decision_wave_map.json
@@ -1,11 +1,11 @@
 {
  "$comment": "الهدف: خريطةُ توزيعِ دَينِ الهجرةِ على موجاتِ القرارِ البشريّ — مُخرَجُ tools/audit/decision_gate.py --map. المادةُ التاسعةُ · 2.",
  "note": "تقسيمُ الدَّينِ على موجاتِ القرارِ — مجموعُه الدَّينُ كلُّه بلا تكرار.",
- "debt": 183,
+ "debt": 181,
  "waves": {
-  "W1": 52,
+  "W1": 50,
   "W2": 34,
   "W3": 97
  },
- "git_head": "0332aa2"
+ "git_head": "c225a9e"
 }
diff --git a/docs/audit/measurements/final_audit_p14.json b/docs/audit/measurements/final_audit_p14.json
index 2a028f7..6962895 100644
--- a/docs/audit/measurements/final_audit_p14.json
+++ b/docs/audit/measurements/final_audit_p14.json
@@ -1,10 +1,10 @@
 {
   "$comment": "الهدف: 21 قياسَ مطابقةٍ بينَ ما يقولُه المستودعُ وما تقولُه الوثيقةُ — مُخرَجُ tools/audit/final_audit.py (P14). يقيسُ ولا يُصلِح، ولا يُقرَأُ شهادةَ نجاح. المادةُ التاسعةُ · 2.",
-  "debt_summary_field": 183,
-  "debt_recount": 183,
-  "sovereign": 17,
+  "debt_summary_field": 181,
+  "debt_recount": 181,
+  "sovereign": 18,
   "closed_legacy": 7,
-  "public": 202,
+  "public": 201,
   "total_sites": 220,
   "program_mentions_168": 73,
   "program_placeholders": 0,
@@ -148,6 +148,7 @@
     "factories.py::assign_manager",
     "factories.py::complete_step",
     "factories.py::start_production",
+    "rulings.py::issue_ruling",
     "service.py::appoint_official",
     "service.py::assign_case",
     "service.py::close_case",
diff --git a/docs/audit/measurements/write_inventory_p13.json b/docs/audit/measurements/write_inventory_p13.json
index ad1d959..5082425 100644
--- a/docs/audit/measurements/write_inventory_p13.json
+++ b/docs/audit/measurements/write_inventory_p13.json
@@ -14,9 +14,9 @@
     "non_sovereign": 28
    },
    "services": {
-    "public": 172,
-    "sovereign": 17,
-    "non_sovereign": 154
+    "public": 171,
+    "sovereign": 18,
+    "non_sovereign": 152
    },
    "tools": {
     "public": 1,
@@ -24,13 +24,13 @@
     "non_sovereign": 1
    }
   },
-  "public_write_operations": 202,
-  "sovereign_write_operations": 17,
+  "public_write_operations": 201,
+  "sovereign_write_operations": 18,
   "closed_legacy_paths": 7,
-  "non_sovereign_write_operations": 183,
+  "non_sovereign_write_operations": 181,
   "non_sovereign_by_file": {
    "federal/executive/services/src/amos_federation/common/persistent.py": 20,
-   "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py": 18,
+   "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py": 17,
    "federal/executive/services/src/amos_federation/services/national_economy/service.py": 16,
    "federal/executive/services/src/amos_federation/services/governance/federation.py": 15,
    "federal/executive/services/src/amos_federation/services/federal_state/service.py": 10,
@@ -58,7 +58,6 @@
    "federal/executive/services/src/amos_federation/services/api_gateway/store.py": 1,
    "federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py": 1,
    "federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py": 1,
-   "federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py": 1,
    "federal/executive/services/src/amos_federation/services/government_services/service.py": 1,
    "tools/migrations/r4_unify_agent_identity.py": 1
   }
@@ -846,33 +845,35 @@
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py",
    "owner": "-",
-   "function": "issue_ruling",
+   "function": "_apply",
    "ordinal": 0,
-   "public": true,
+   "public": false,
    "writes": [
-    "add()"
+    "add()",
+    "commit()"
    ],
    "guarded": false,
    "closed_legacy": false,
    "writes_via": []
   },
   {
-   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
-   "owner": "FederalJudiciary",
-   "function": "add_claim",
+   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py",
+   "owner": "-",
+   "function": "issue_ruling",
    "ordinal": 0,
    "public": true,
    "writes": [
+    "add()",
     "commit()"
    ],
-   "guarded": false,
+   "guarded": true,
    "closed_legacy": false,
    "writes_via": []
   },
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
    "owner": "FederalJudiciary",
-   "function": "add_party",
+   "function": "add_claim",
    "ordinal": 0,
    "public": true,
    "writes": [
@@ -885,7 +886,7 @@
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
    "owner": "FederalJudiciary",
-   "function": "appoint_judge",
+   "function": "add_party",
    "ordinal": 0,
    "public": true,
    "writes": [
@@ -898,7 +899,7 @@
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
    "owner": "FederalJudiciary",
-   "function": "assign_case",
+   "function": "appoint_judge",
    "ordinal": 0,
    "public": true,
    "writes": [
@@ -911,7 +912,7 @@
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
    "owner": "FederalJudiciary",
-   "function": "close_case",
+   "function": "assign_case",
    "ordinal": 0,
    "public": true,
    "writes": [
@@ -924,7 +925,7 @@
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
    "owner": "FederalJudiciary",
-   "function": "enforce_ruling_via_task",
+   "function": "close_case",
    "ordinal": 0,
    "public": true,
    "writes": [
@@ -937,7 +938,7 @@
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
    "owner": "FederalJudiciary",
-   "function": "enforce_ruling_via_treasury",
+   "function": "enforce_ruling_via_task",
    "ordinal": 0,
    "public": true,
    "writes": [
@@ -950,7 +951,7 @@
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
    "owner": "FederalJudiciary",
-   "function": "file_case",
+   "function": "enforce_ruling_via_treasury",
    "ordinal": 0,
    "public": true,
    "writes": [
@@ -963,7 +964,7 @@
   {
    "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
    "owner": "FederalJudiciary",
-   "function": "issue_ruling",
+   "function": "file_case",
    "ordinal": 0,
    "public": true,
    "writes": [
diff --git a/tests/governance/test_q3_branch_declaration_surface.py b/tests/governance/test_q3_branch_declaration_surface.py
index 7e54694..8705386 100644
--- a/tests/governance/test_q3_branch_declaration_surface.py
+++ b/tests/governance/test_q3_branch_declaration_surface.py
@@ -272,13 +272,14 @@ def test_bridge_actor_is_declared_parameter_defaulting_to_executive() -> None:
     assert isinstance(default, ast.Name) and default.id == "DEFAULT_ACTOR"
 
 
-# ── 4. مواضعُ بناءِ المُصرِّحِ: أربعةٌ تُعلِنُ فاعلَها وأربعةٌ تتَّكِلُ على الافتراض ──
-def test_production_authorizer_sites_split_five_declared_four_defaulted() -> None:
-    """(محدّثة في W-402 · WI-082): المُصرِّحُ الخامسُ المُعلِنُ فاعلَهُ — إنشاءُ
-    الهويّةِ بقرارِ المالكِ Q-15 ① — على سابقةِ factories.py نفسِها، لا هروبًا
-    من الإعلانِ. والافتراضيّةُ الأربعُ كما هي."""
+# ── 4. مواضعُ بناءِ المُصرِّحِ: ستةٌ تُعلِنُ فاعلَها وأربعةٌ تتَّكِلُ على الافتراض ──
+def test_production_authorizer_sites_split_six_declared_four_defaulted() -> None:
+    """(محدّثة في W-593 · WI-105/J1): المُصرِّحُ السادسُ المُعلِنُ فاعلَهُ — المُفوِّضُ القضائيُّ
+    الكسولُ في rulings.py (JUDICIARY_ACTOR · D1 من تصميمِ J1 المعتمدِ بقرارِ المالكِ
+    Q-69/D17-6) — على سابقةِ factories.py نفسِها، لا هروبًا من الإعلانِ. والافتراضيّةُ
+    الأربعُ كما هي. (وكانت خمسةً بعدَ WI-082 · W-402.)"""
     sites = _authorizer_construction_sites()
-    assert len(sites["declared"]) == 5, sites["declared"]
+    assert len(sites["declared"]) == 6, sites["declared"]
     assert len(sites["defaulted"]) == 4, sites["defaulted"]
     assert sorted(Path(p.split(":")[0]).name for p in sites["declared"]) == [
         "agent_identity.py",
@@ -286,6 +287,7 @@ def test_production_authorizer_sites_split_five_declared_four_defaulted() -> Non
         "factories.py",
         "money_authority.py",
         "money_authority.py",
+        "rulings.py",
     ], sites["declared"]
     assert sorted(Path(p.split(":")[0]).name for p in sites["defaulted"]) == [
         "engine.py",
@@ -296,25 +298,28 @@ def test_production_authorizer_sites_split_five_declared_four_defaulted() -> Non
 
 
 # ── 5. دَينُ W1 وتواقيعُه ─────────────────────────────────────────────────────
-def test_w1_debt_is_fifty_two_sites() -> None:
-    assert len(_w1_debt()) == 52
+def test_w1_debt_is_fifty_sites() -> None:
+    """(محدّثة في W-593 · J1): 52 ← 50 — issue_ruling عبرَ الحدَّ السياديَّ فخرجَ منَ
+    دَينِ W1. (سابقةُ WI-082 · W-402.)"""
+    assert len(_w1_debt()) == 50
 
 
-def test_w1_signature_buckets_are_twenty_eight_four_twenty() -> None:
-    """الدعوى المحروسة: 28 سياقًا وحدَه · 4 فاعلًا مُسمّىً · 20 بلا فاعلٍ بأيِّ صورةٍ · 0 كِلاهما."""
+def test_w1_signature_buckets_are_twenty_seven_four_nineteen() -> None:
+    """الدعوى المحروسة (محدّثة في W-593 · J1: 28/20 ← 27/19): 27 سياقًا وحدَه ·
+    4 فاعلًا مُسمّىً · 19 بلا فاعلٍ بأيِّ صورةٍ · 0 كِلاهما."""
     buckets = _signature_buckets()
     counts = {key: len(value) for key, value in buckets.items()}
     assert counts == {
-        "context_only": 28,
+        "context_only": 27,
         "actor_named": 4,
-        "neither": 20,
+        "neither": 19,
         "both": 0,
     }, counts
-    assert sum(counts.values()) == 52
+    assert sum(counts.values()) == 50
 
 
 def test_no_w1_debt_site_declares_a_branch_today() -> None:
-    """لا موضعَ واحدًا من الـ52 يُمرِّرُ فرعًا — فالفرعُ اليومَ لا يُعلَنُ في التوقيعِ أصلًا."""
+    """لا موضعَ واحدًا منَ الـ50 (كانت 52 قبلَ J1 · W-593) يُمرِّرُ فرعًا — فالفرعُ اليومَ لا يُعلَنُ في التوقيعِ أصلًا."""
     for site in _w1_debt():
         source = (REPO_ROOT / site.path).read_text(encoding="utf-8")
         node = _function_node(ast.parse(source), site.function)
@@ -326,10 +331,11 @@ def test_no_w1_debt_site_declares_a_branch_today() -> None:
 
 
 # ── 6. أثرُ الإعلانِ على الحكم — من المُحرِّكِ نفسِه ──────────────────────────
-def test_only_one_debt_action_is_branch_sensitive_today() -> None:
-    """الدعوى المحروسة: من 44 اسمَ فعلٍ في دَينِ W1 — 41 خارجَ المعجمِ · 1 حسّاسٌ للفرعِ · 2 ممنوعانِ لكلِّ فاعل."""
+def test_no_debt_action_is_branch_sensitive_today() -> None:
+    """الدعوى المحروسة (محدّثة في W-593 · J1: 44/41/1 ← 43/41/0 — issue_ruling كانَ الحسّاسَ الوحيدَ فخرجَ منَ الدَّينِ كلِّهِ فلم يبقَ حسّاسٌ فيه): من 43 اسمَ فعلٍ في دَينِ W1 —
+    41 خارجَ المعجمِ · 0 حسّاسٌ للفرعِ · 2 ممنوعانِ لكلِّ فاعل."""
     actions = sorted({site.function.split(".")[-1] for site in _w1_debt()})
-    assert len(actions) == 44, actions
+    assert len(actions) == 43, actions
     actors = ["EXECUTIVE", "JUDICIAL", "LEGISLATIVE", "TREASURY", "ROYAL"]
     verdicts = _engine_verdicts(actions, actors)
 
@@ -344,7 +350,7 @@ def test_only_one_debt_action_is_branch_sensitive_today() -> None:
             sensitive.append(action)
 
     assert len(outside) == 41, sorted(outside)
-    assert sensitive == ["issue_ruling"], sensitive
+    assert sensitive == [], sensitive
     assert sorted(denied) == ["grant_authority", "revoke_authority"], sorted(denied)
 
 
=== RAW [20] END ===
=== RAW [21] BEGIN ===
CMD: cd /home/user/workspace/council_w598/grok_4_7/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
EXIT: 0
BYTES: 319
SHA256: e237b66d4e4686ec1d76c273157268e76598e93fa5418cfa9090f52a8c38efd9
NO_EOL: 0
--- OUTPUT ---
عقدُ نَسَبِ القياساتِ مستقيمٌ: 11 قياسًا مقيَّدًا · 8 محروسًا (‏منها 1 برباطٍ مقيسٍ نصًّا) · 3 مُعلَنًا بسببٍ مكتوبٍ. ومُؤَجَّلٌ إلى الشطرِ الآخرِ: 2 (‏من 2 يحتاجُ حزمًا خارجيّةً).
=== RAW [21] END ===
=== RAW [22] BEGIN ===
CMD: find /home/user/workspace/council_w598/grok_4_7 -maxdepth 1
EXIT: 0
BYTES: 370
SHA256: 6a81a3fe864d1eb2bfc63f6e8aad9f0ee7c96da2b15e8b8be12ab750b8e7145c
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w598/grok_4_7
/home/user/workspace/council_w598/grok_4_7/repo
/home/user/workspace/council_w598/grok_4_7/tmp
/home/user/workspace/council_w598/grok_4_7/capture_progress.log
/home/user/workspace/council_w598/grok_4_7/capture_stdout.log
/home/user/workspace/council_w598/grok_4_7/run_captures.py
/home/user/workspace/council_w598/grok_4_7/raw
=== RAW [22] END ===
VERDICT_PER_CRITERION: (1) الترتيبُ والإضافتانِ: نعم. موافقةُ المالكِ على نقاطِ الحكمِ صدرتْ بتوجيهِ المستشارِ 17 ولا تُحاكَمُ هنا.
الترتيبُ (درسُ Q-61): الكتلةُ 5 تُخرِجُ أوّلَ التزامٍ لوثيقةِ التصميمِ ce4b917 في 2026-10-21T10:26:52Z (W-581 · لا شِفرةَ) قبلَ التزامِ الشِّفرةِ 529cc39 في 2026-10-21T19:46:27Z (W-593). الالتزاماتُ d6dfaee و4f357aa بينهما تصحيحاتٌ بلا شِفرة. الكتلةُ 3 تُثبِتُ أنّ 529cc39 هو التزامُ الشِّفرةِ وأنّ 03a6c62 فوقَه توثيقٌ لا شِفرة.
الإضافةُ (أ) الجيلُ في هدفِ العبورِ: سليمةٌ ومُنفَّذة. الكتلةُ 16 (§ D5) تُعلِنُ الهدفَ judiciary/rulings/{case_id}/{stage}/g{n} لتجنُّبِ تصادمِ إذنِ الثانية. الشِّفرةُ في rulings.py تبني target وoperation_key بالجيلِ معًا، والكتلةُ 11 (7 passed) تشملُ T4.
الإضافةُ (ب) قياسُ T6 عبرَ حارسِ 1I: إفصاحٌ صادقٌ عن مسارِ الإنتاجِ لا حسمٌ للمعيارِ — الحسمُ في (2) و(4) أدناهُ. الكتلةُ 16 تُثبِتُ أنّ الإضافةَ تقولُ إنّ التعويضَ الآليَّ غيرُ موصولٍ في مسارِ run_once، وهذا مطابقٌ لما في enforcement_boundary.execute (يستدعي IdempotencyGuard.run_once لا run_compensated_transaction).
(2) guard_declared بالفعلِ issue_ruling وطلبِ اختصاصٍ حيٍّ ومُعوِّضٍ حقيقيٍّ ومفتاحٍ بجيلِ الإلغاء: نعم.
الكتلةُ 15: rulings.py:324 guard_declared( · rulings.py:76 JUDICIARY_ACTOR = JUDICIAL · rulings.py:235 actor_scope=authority.position_scope · sovereignty_bridge.py يمرِّرُ judicial_action. الشِّفرةُ: guard_declared(\"issue_ruling\", target, ..., operation_key=op_key حيث op_key = judiciary.ruling.issue:{case}:{stage}:g{generation} والجيلُ عددُ vacated قبلَ الحدِّ، وjudicial_action=_judicial_action() من authority.jurisdiction وcase.jurisdiction وposition_scope لا من ثوابت. الخدمةُ فقدَتْ session.commit() (service.py بعدَ السطرِ 672).
المُعوِّضُ الحقيقيُّ / T6 — الحكمُ منَ النصِّ المعتمدِ لا منَ الإضافةِ المؤرَّخة: النصُّ الذي وافقَ عليه المالكُ (D17-6 في سجلِّ القراراتِ داخلَ الاستنساخ: «D7 (أ) الاستعادة التقنية للمُعوِّض») هو اختيارُ جوهرِ المُعوِّضِ: استعادةٌ تقنيّةٌ (حذفُ صفَّي الحكمِ والإجراءِ وإرجاعُ حالةِ القضيّةِ) لا إلغاءٌ قضائيٌّ (ب). نقطةُ الحكمِ في § 6 منَ الكتلةِ 16 هي هذا الاختيارُ وحدَه. § 5 منَ الوثيقةِ المعتمدةِ لا يشملُ enforcement_boundary.py، وحارسُ الحدِّ نفسُه يصفُ دورَ 1I عندَ العبورِ بأنّه «ربطًا لا استعادة». فالنصُّ المعتمدُ لا يقتضي إعادةَ وصلِ التعويضِ الآليِّ في مسارِ الإنتاجِ أحاديِّ الأثر. يقتضي مُعوِّضًا مسجَّلًا صالحًا: الدالّةُ _restore تُمرَّرُ في compensators= إلى guard_declared وهي تحذفُ الصفَّينِ وتُرجِعُ الحالةَ في جلسةٍ جديدة — لا دالّةٌ فارغةٌ ولا vacate. الكتلةُ 11 تُثبِتُ أنّ T6 نجحَ: إسقاطُ تثبيتِ النجاحِ بعدَ الالتزامِ (الصفُّ حاضرٌ) ثمَّ CompensationGuard.compensate بالعقدِ والخطّةِ الملتقَطينِ منَ العبورِ الحقيقيِّ ⇒ state_is_clean والصفوفُ غائبةٌ والحالةُ مُستعادة. صفُّ T6 الأصليُّ الذي يسمّي CompensationRequired يصفُ استثناءَ run_compensated_transaction (compensation.py:829) وهو خارجَ ملفّاتِ الدفعةِ المعتمدة؛ لا أجعلُ الإضافةَ المؤرَّخةَ حسمًا، وأحكمُ بأنّ المعتمدَ هو المُعوِّضُ المسجَّلُ الصالحُ لا الاستدعاءُ الآليُّ في مسارِ الإنتاج.
(3) D-4: 183 ← 181 · sovereign 17 ← 18 · أسطحٌ 220 ← 220 بلا نموٍّ في غيرِه: نعم. الكتلةُ 7 (قياسي على العقدة): مواضعُ 220 · تعبرُ 18 · لا تعبرُ 181 · عامّةٌ 201. الكتلةُ 8: الوحدةُ 27 موضعًا · عامّةٌ 26 · تعبرُ 1 · لا تعبرُ 25. الكتلةُ 9: issue_ruling وحدَها public=true وguarded=true. أعدتُ قياسَ الأساسِ d0932c51 بالأداةِ نفسِها في نسخةٍ داخلَ دليلي (ليس من أوامرِ الإحاطةِ الـ22): مواضعُ 220 · عامّةٌ 202 · تعبرُ 17 · لا تعبرُ 183 · الوحدةُ 27 عامّةً و0 تعبرُ وservice.py 18 وrulings.py 1. الفرقُ: الأسطحُ ثابتةٌ 220 · السياديُّ +1 (عبورُ issue_ruling) · الدَّينُ −2 (خروجُ service.issue_ruling منَ الكتابةِ وانتقالُ issue_ruling منَ الدَّينِ إلى المحروس · والمُطبِّقُ المتداخلُ خاصٌّ فلا يدخلُ الدَّين) · منطقةُ services 172/17/154 ← 171/18/152 ومناطقُ core وservice_common وtools بلا تغيير. الكتلةُ 18 توافقُ هذا الفرقَ (وتصحيحَ «عامّةٌ قبل = 202»). بلا نموٍّ في غيرِ الوحدة.
(4) T1–T7 ناجحةٌ وM1 تُسقِطُ T1 وT2 وM2–M4 كلٌّ يُسقِطُ فحصَه: نعم.
الكتلةُ 11: 7 passed in 1.65s (EXIT 0) — وهي T1–T7 كما تسمّيها الكتلةُ 16.
الطفراتُ: مخرجاتُ الكتلةِ 17 ملخّصاتٌ بلا الرقعة، فأعَدتُ إجرائَها بنفسي في نسخةٍ معزولةٍ mutation_copy داخلَ دليلي (الأصلُ استُعيدَ وgit diff فارغٌ بعدَها). الضابطُ بلا طفرة: 7 passed. M1 (نداءُ المُطبِّقِ مباشرةً بلا guard_declared): T1 وT2 سقطَا (EXIT 1 · T1: لا عبورَ في السجلِّ · T2: لم يُرفَع SovereigntyViolation). M2 (مفتاحٌ بلا جيل): T4 سقطَ (EXIT 1 · IdempotencyKeyReuseError على مفتاحٍ بلا g{n}). M3 (حذفُ فحصِ المكرَّرِ قبلَ الحدِّ): T5 سقطَ (EXIT 1 · AttributeError لأنّ الطلبَ الثاني صارَ إعادةً وproceeding=None بدلَ DuplicateRulingError قبلَ الحدِّ — وهو الضررُ الذي يصِفُه D6). M4 (judicial_action=None): T1 سقطَ (EXIT 1 · JurisdictionNotDeclaredError). المخرجُ الخامُّ في tmp/mutations/.
(5) test_r7d وفحوصُ WI-082 بلا تعديلٍ وحزمُ services خضراءُ في CI مقروءًا: نعم.
الكتلةُ 6: فرقٌ فارغٌ (BYTES 0 · EXIT 0) على الملفَّين. الكتلةُ 12: 27 passed. الكتلةُ 13: 8 passed. الكتلةُ 14: 1482 passed, 53 skipped · EXIT 0 (التخطّي اختباراتُ postgres بلا خادم · والتحذيرُ ورفضُ تصديرِ الأثرِ إلى localhost:4317 بعدَ الخلاصةِ لا يُسقِطانِ الحزمة). CI: دليلُ الاستنساخِ docs/audit/evidence/W-597/ci_verdict_39679264001.txt يقرأُ التشغيلَ 39679264001 مقروءًا وأخضرَ 13/13 وعلى العقدةِ نفسِها، وREADME يربطُه بـ90cae46. قستُ فرقَ مساراتِ الشِّفرةِ 90cae46..HEAD (federal · core · tools · tests) فكانَ فارغًا، فالكتلةُ 3 (حكمُ CI على 90cae46 أخضرُ 13/13) تنطبقُ على شِفرةِ هذه العقدة.
(6) مراجعةٌ تُعيدُ التشغيلَ (Q-H): نعم. الأوامرُ 1–22 شُغِّلَت عبرَ أداةِ الالتقاطِ على استنساخٍ أنشأتُه أنا عندَ 03a6c625b79002c519a54bc1f27fddd6e99500dc، وأُعيدَتِ الطفراتُ وقياسُ الأساسِ في دليلِ المقعد.
سؤالُ 1: نعم استنسختُ المستودعَ بنفسي. المسارُ /home/user/workspace/council_w598/grok_4_7/repo. الكتلةُ 1: HEAD = 03a6c625b79002c519a54bc1f27fddd6e99500dc وهو رأسُ رسالةِ الإطلاق.
حرسُ W-595 (ليس معيارَ قبولٍ مستقلًّا ويُقاسُ بالأوامرِ 19–21): الكتلةُ 19: 20 passed. الكتلةُ 21: عقدُ النَّسَبِ مستقيمٌ (EXIT 0). الكتلةُ 20: تحديثُ المُثبَّتاتِ إلى المقيسِ (دَينُ W1 52←50 · المُعلِنون 5←6 بإضافةِ rulings.py · الحسّاسُ في الدَّينِ issue_ruling خرجَ فصارَ sensitive فارغًا) لا تخفيفًا صامتًا.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً. ملاحظةٌ غيرُ حاجبة: التعويضُ الآليُّ غيرُ موصولٍ في مسارِ الإنتاجِ أحاديِّ الأثرِ (run_once). فشلُ تثبيتِ النجاحِ بعدَ الالتزامِ يُبقي الصفوفَ حتى يُستدعى CompensationGuard.compensate. هذا لا يُسقِطُ المعيارَ لأنّ النصَّ المعتمدَ (D17-6 · D7-أ) و§ 5 يطلبانِ مُعوِّضًا تقنيًّا مسجَّلًا صالحًا لا تعديلَ enforcement_boundary.py، والكتلةُ 11 تُثبِتُ صلاحَه. الإضافةُ المؤرَّخةُ قرينةٌ لا حسم، والحكمُ منَ النصِّ المعتمد.
ISOLATION_DECLARATION: نعم. لم أقرأْ تقاريرَ المنفِّذِ ولا أدلّةَ المقاعدِ الأخرى ولا سجلَّ الإكمالِ خارجَ الاستنساخِ ولا أدلّةَ الجولاتِ W-581…W-590 ولا ورقةَ D17. قرأتُ الإحاطةَ المأمورَ بها، ومصادرَ القسمِ د داخلَ الاستنساخِ (صفُّ WI-105 وكتلتُه · وثيقةُ التصميمِ · شِفرةُ العبورِ وcore/sovereignty · سجلُّ القراراتِ في مواضعِ Q-6 وQ-69/D17-6 وQ-68 · دليلُ CI في evidence/W-597 لأنّ المعيارَ 5 يطلبُ CI مقروءًا). كلُّ الكتابةِ وإعادةِ الطفراتِ وقياسِ الأساسِ داخلَ /home/user/workspace/council_w598/grok_4_7. الاستنساخُ عندَ رأسِ رسالةِ الإطلاقِ كما تُثبِتُه الكتلةُ 1. الكتلةُ 22 تُدرِجُ محتوياتِ دليلِ المقعدِ عندَ الالتقاطِ وحدَها.
VERDICT: PASS لكلِّ المعاييرِ
