# حكمُ مقعدِ المجلسِ — gemini_3_8_flash · جولةُ WI-115 (W-683)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-115 (النطاقُ المنفَّذُ: إصلاحُ § 3.5 وحدَه) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w673/gemini_3_8_flash/wi115) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `4b87769f1a98d2a7793991fbdec498c6a371537c12460c54af76b6f2b1fbe943`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-115 عندَ العقدةِ `79abc6a2` — إحاطةٌ مبصومةٌ (W-673) ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9) · ومخرجاتُ الفاحصِ المصلَحِ (W-680 · main `76a0e5e4`) مقروءةٌ مقبولةً EXIT 0 (raw_check_outputs.txt في قيدِ W-683).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-683) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5) · والانتقالُ المقرَّرُ حتى معَ النصابِ: IN_REVIEW→IN_PROGRESS لكاشفِ التعشيشِ (D25-3 — كما قُيِّدَ في W-681).

## تاريخ الإنشاء
2026-10-26

## تاريخ آخر تعديل
2026-10-26 (W-683 — القيدُ نفسُه)

---
MODEL: gemini_3_8_flash
FAMILY: Google · Gemini
RUN_DATE: 2026-10-26 04:05 +00:00
NODE: 79abc6a206000e162689d642d1ebc42af36f445a
CLONE_PATH: /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/
 2. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/)
 3. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
 5. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && cat docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
 6. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git diff 9343479073d65f4ceb61d5ba9ba273452651987c^ 9343479073d65f4ceb61d5ba9ba273452651987c -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py
 7. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
 8. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && nl -ba federal/executive/services/src/amos_federation/services/state_treasury/service.py | sed -n '820,880p'
 9. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rm -rf ../old && git worktree add --detach ../old 9343479073d65f4ceb61d5ba9ba273452651987c^ && cp federal/executive/services/tests/test_wi115_reversed_replay.py ../old/federal/executive/services/tests/ && cd ../old/federal/executive/services && PYTHONPATH=src /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
 10. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rg -n 'def disburse|def reverse|def execute_transfer|_existing_idempotent\(' federal/executive/services/src/amos_federation/services/state_treasury/service.py
 11. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rg -n 'WI-110|WI-115|D25-3|§ ?3.5' docs/audit/SOVEREIGN_DECISION_REGISTER.md
 12. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && sha256sum docs/audit/evidence/W-673/briefs_wi115/briefing_gemini_3_8_flash.md
 13. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && cat docs/audit/evidence/W-673/briefs_wi115/SHA256SUMS
 14. nl -ba /home/user/workspace/council_w673/gemini_3_8_flash/wi115/probe/test_wi115_probe.py
 15. cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider /home/user/workspace/council_w673/gemini_3_8_flash/wi115/probe/test_wi115_probe.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/)
EXIT: 0
BYTES: 909
SHA256: 80d4668520ca97765df3907220e9090940b4f3313f8ede7312822f1be48a7bb1
NO_EOL: 0
--- OUTPUT ---
Note: switching to '79abc6a206000e162689d642d1ebc42af36f445a'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 79abc6a2 W-673: WI-113 وWI-115 IN_PROGRESS→IN_REVIEW · ستُّ إحاطاتٍ مبصومةٍ لجولةِ المجلسِ (gemini_3_8_flash · grok_4_7 · kimi_k3) ونصوصُ الإطلاقِ حرفيًّا · WI-115 بنطاقِ § 3.5 وحدَه · لا شِفرةَ — المنسِّقُ Claude Opus 5.5
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
EXIT: 0
BYTES: 1409
SHA256: 9b19025f4e0310bf7c5091949e3e3551708fdead5a6ecd29808df45c7880cc27
NO_EOL: 0
--- OUTPUT ---
93434790 2026-10-25T08:45:43Z W-670: WI-115 — إصلاحُ § 3.5: إعادةُ صرفٍ بمفتاحِ حركةٍ معكوسةٍ تُرفَضُ (EntityStateError) · فحصانِ وطفرةٌ · وثائقُ الحالةِ وأرقامُ الحزمِ (2727 · 1525+53) — المنسِّقُ Claude Opus 5.5
5086fb4e 2026-10-25T08:00:16Z W-665: WI-115 READY→RESERVED · وثيقةُ تصميمِ Q-9 (إصلاحُ § 3.5 · كاشفُ التعشيشِ · _disburse_core) بقياساتِها · لا شِفرةَ — المنسِّقُ Claude Opus 5.5
f1290238 2026-08-21T16:30:48Z W-015 · تنفيذُ Q-31: وصلُ المُحرِّكِ الدستوريِّ في طبقةِ تخويلِ المال
fe83e085 2026-08-21T14:53:47Z Q-19: فاعلُ الخزانةِ لكلِّ عمليّةٍ بتفويضٍ مُعلَن (W-013)
e594d4bd 2026-08-17T14:23:21Z R9E-CI3: إصلاح بوابة الفحص (ruff) — تناقضٌ حقيقيّ في إعادة التصدير وتنسيقٌ متروك
5f161f88 2026-08-17T08:45:08Z R7-C3: إغلاق دَين الخزانة بمِنحة منصب لا بتوسيع صلاحية
8dac58c5 2026-08-17T07:15:22Z R7-B.1: قفل الصفوف — تسلسلٌ عند التنافس بترتيبٍ قانوني ومهلةٍ محدودة
72f81ab0 2026-08-17T06:53:42Z R7-B: نواة الخزانة الفدرالية — دفترٌ بطرفين ومجاميع مشتقّة
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && cat docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
EXIT: 0
BYTES: 10263
SHA256: 41a4dc7591d8a35c5736107e6fa8159722944f0eb6494b3ffc5250f3d14a97bc
NO_EOL: 0
--- OUTPUT ---
# Q-9 (الخيارُ 4) — تصميمُ كاشفِ التعشيشِ عندَ الحدِّ، وإصلاحُ § 3.5، وهيكلةُ مركَّباتِ المالِ الثلاثة (WI-115)

## الهدف: تصميمُ ما قرّرَه المالكُ في Q-9 قبلَ أيِّ شِفرةٍ وقبلَ أيِّ تصميمٍ لـM1
## النطاق: وثيقةُ تصميمٍ — لا شِفرةَ فيها · لا مساسَ بـK1 · لا تخفيفَ لحارس
## المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) · بقرارِ المالكِ Q-9 في التوجيهِ 22 § 1
## تاريخ الإنشاء: 2026-10-25
## تاريخ آخر تعديل: 2026-10-25 (W-665 — الإنشاءُ)

---

## 0. السندُ والانضباط

- نصُّ القرارِ حرفيًّا (التوجيهُ 22 § 1): «يُمنع التعشيش السيادي بكاشف عند الحد، ويُعاد هيكلة مركّبات المال الثلاثة على نمط «الخارجي يُعلن الآثار وينادي نوًى خاصة»، ويُستثنى open_case باسمه استثناءً مسجَّلًا، ويُعالَج خطر إعادة disburse لحركة معكوسة (§3.5) قبل M1».
- ونصُّ الأمرِ (§ 2): «كاشف التعشيش + إصلاح §3.5 قبل أي تصميم لـM1».
- **كلُّ «ملف:سطر» هنا مولَّدٌ بأمرٍ، ومخرجُه ملصقٌ خامًا** في `docs/audit/evidence/W-665/wi115_design_measurements.txt` (DISC-136). والقياسُ على `cb728386`.

## 1. ما قِيسَ اليومَ (ويُغيِّرُ ترتيبَ العمل)

1. **مركَّباتُ المالِ الثلاثةُ ونواتُها غيرُ محروسةٍ أصلًا.** `rg -c 'guard_declared\('` على شِفرةِ الإنتاجِ يُعيدُ 12 ملفًّا، ليسَ منها `state_treasury/service.py` ولا `national_economy/service.py` ولا `federal_state/service.py`. والمركَّباتُ تُنادي `treasury.disburse` مباشرةً:
   - `national_economy/service.py:1382` `execute_expenditure`، ويُنادي عندَ `:1442`.
   - `national_economy/service.py:1710` `execute_transfer`، ويُنادي عندَ `:1759`.
   - `federal_state/service.py:1053` `execute_scoped_disbursement`، ويُنادي عندَ `:1099`.
   
   **فلا تعشيشَ ماليًّا اليوم**، ويقعُ التعشيشُ بمجرّدِ أن يُحرَسَ المالُ (M1). لذلك يمنعُه الكاشفُ مسبقًا ولا يكسرُ شيئًا قائمًا في المال.
2. **التعشيشُ القائمُ الوحيدُ** هو `open_case`: `government_services/service.py:735`. يعبرُ بـ`ACTION_CASE_OPEN = "gov.case.open"` (`:118`، والنداءُ `:902`)، ومُطبِّقُه يُنادي `self._core.submit` (`:834`). وتلكَ تعبرُ بـ`"task.submit"` (`engine.py:274/:307`). ومعوِّضُه `_cancel_case_task` (`:309`) يُنادي `self._core.cancel` (`:316`)، وهي تعبرُ بـ`"task.cancel"` (`engine.py:608/:619`).
3. **الحدُّ**: `SovereignExecutionBoundary.execute` (`enforcement_boundary.py:311`)، ويقرِّرُ فيه `self.gateway.decide` عندَ `:357`. والجسرُ يُناديه عندَ `sovereignty_bridge.py:386`. والحدُّ لا يحملُ اليومَ أيَّ `contextvars` (rg بلا نتيجةٍ لـ`ContextVar|contextvars|Nested`).
4. **§ 3.5 مقيسًا**: `_existing_idempotent` (`state_treasury/service.py:835–847`) يُرشِّحُ بالمستأجرِ والمفتاحِ وحدَهما، بلا حالة. وتُناديه ثلاثُ عمليّات: `:1233` (`post_funding`)، و`:1337` (`disburse`)، و`:1479` (`execute_decision_disbursement`). وكلُّها تُعيدُ ما وجدَتْه بـ`"idempotent": True`. أمّا `reverse_transaction` فيُعلِّمُ الأصلَ `original.status = "reversed"` (`:1603`) ولا يحذفُه. والحالةُ الافتراضيّةُ `"posted"` (`models.py:285`). **فإعادةُ صرفٍ بمفتاحِ حركةٍ معكوسةٍ تُعيدُ الحركةَ المعكوسةَ «نجاحًا متطابقًا»**، فيحسبُ المركَّبُ مالًا صُرِفَ وهو مردود.

## 2. التصميم

### 2.1 إصلاحُ § 3.5 (أوّلًا — لا يتوقّفُ على شيء)
في `_existing_idempotent`: إن وُجدَت الحركةُ وحالتُها `reversed`، يُرفَعُ `EntityStateError` بنصٍّ صريح: «الحركةُ بهذا المفتاحِ معكوسةٌ — لا تُعادُ نجاحًا ولا صرفًا؛ صرفٌ جديدٌ يلزمُه مفتاحٌ جديد».
- لماذا الرفعُ لا الصرفُ من جديد؟ لأنَّ الصرفَ من جديدٍ بالمفتاحِ نفسِه يكسرُ معنى الذرّيّة. والمفتاحُ الجديدُ قرارُ المُنادي لا قرارُ الخزانة.
- يشملُ العمليّاتِ الثلاثَ لأنَّها تمرُّ بالدالّةِ نفسِها.
- **الفحص**: صرفٌ ← عكسٌ ← إعادةُ الصرفِ بالمفتاحِ نفسِه. قبلَ الإصلاحِ يُعادُ `idempotent=True` بحالةِ `reversed` (يسقطُ الفحص)، وبعدَه يُرفَعُ الخطأ (ينجح).
- **الطفرة**: حذفُ الشرطِ يكتشفُه الفحص.

### 2.2 الكاشفُ عندَ الحدّ
- `ContextVar` خاصٌّ بالوحدة في `enforcement_boundary.py`، يحملُ إطارَ العبورِ النشط `(action, target)`. يُضبَطُ عندَ دخولِ `execute` **قبلَ `decide`** (`:357`)، ويُستعادُ في `finally`.
- إن دخلَ `execute` وفي السياقِ عبورٌ نشطٌ، يُرفَعُ `NestedSovereignCallError` قبلَ `decide`، فلا إذنَ ولا قيدَ دفترٍ ولا أثر. والخطأُ استثناءٌ صريحٌ لا يُبتلَع، مثلَ بقيّةِ استثناءاتِ الحدِّ.
- **الاستثناءُ المسجَّلُ باسمِه** ثابتٌ مُجمَّدٌ في الوحدةِ نفسِها:
  `{("gov.case.open", "task.submit"), ("gov.case.open", "task.cancel")}`.
  وهو أزواجٌ (خارجيٌّ، داخليٌّ) لا أسماءٌ مفردة، فلا يصيرُ `open_case` بابًا لأيِّ عبورٍ داخلَه. ويُعلَنُ في رأسِ الوحدةِ بسندِه (Q-9 · التوجيهُ 22 § 1).
- **الفحوص**:
  - عبورٌ داخلَ عبورٍ يُرفَضُ قبلَ `decide`: لا قيدَ في الدفترِ ولا أثرَ مُطبَّق.
  - `open_case` ينجحُ كما هو، ومعوِّضُه كذلك.
  - زوجٌ غيرُ مُستثنًى خارجيُّه `gov.case.open` يُرفَض.
  - السياقُ يُستعادُ بعدَ الرفضِ وبعدَ استثناءٍ في المُطبِّق.
- **الطفرات**: حذفُ الفحصِ، وتوسيعُ الاستثناءِ إلى الاسمِ المفرد، وحذفُ الاستعادةِ في `finally`.

### 2.3 هيكلةُ المركَّباتِ الثلاثة («الخارجيُّ يُعلِنُ الآثارَ ويُنادي نوًى خاصّة»)
- **ما يُفعَلُ الآن**: تُستخرَجُ من `StateTreasury.disburse` نواةٌ خاصّةٌ `_disburse_core` بلا تغييرِ سلوك. ويبقى `disburse` العامُّ غلافًا يُنادي النواة، وتُنادي المركَّباتُ الثلاثةُ النواةَ مباشرة. والفحوصُ القائمةُ للمركَّباتِ تبقى خضراءَ بلا تعديل، وهي الدليلُ على «بلا تغيير سلوك».
- **ما لا يُفعَلُ الآن**: «الخارجيُّ يُعلِنُ الآثار» يعني أنَّ المركَّبَ يعبرُ الحدَّ بآثارٍ مُعلَنة. وهذا عبورٌ للمالِ، أي هو **M1 نفسُه**، والمالكُ أمرَ بالكاشفِ والإصلاحِ «قبل أي تصميم لـM1». فإعلانُ الآثارِ يقعُ مع M1، والنواةُ الخاصّةُ تُهيِّئُه، فلا يحتاجُ M1 إلى إعادةِ فتحِ هذه الملفّات. **وهذا تفسيرٌ للترتيبِ يُعرَضُ على المستشارِ صراحةً، لا قرارٌ بيدِ المنفِّذ.** فإن رأى المالكُ أنَّ الهيكلةَ كاملةً شرطٌ قبلَ M1، فهي مع M1 بالضرورة، لأنَّ إعلانَ الآثارِ لا يكونُ بلا عبور.
- والمفوِّضانِ الإضافيّان، `execute_decision_disbursement` (`state_treasury/service.py:1448`) و`enforce_ruling_via_treasury` (`federal_judiciary/service.py:1012`، ويُنادي عندَ `:1046`)، خارجَ «المركَّباتِ الثلاثة» نصًّا، ويُعرَضانِ مع M1.

### 2.4 ترتيبُ الالتزامات
1. هذه الوثيقة (W-665).
2. بعدَ الحجزِ والانتقالِ إلى IN_PROGRESS: إصلاحُ § 3.5 وفحصُه وطفرتُه.
3. الكاشفُ والاستثناءُ وفحوصُه وطفراتُه، وتشغيلُ المجموعةِ كاملةً لقياسِ أيِّ تعشيشٍ لم يرصدْه التحليلُ نصًّا.
4. استخراجُ `_disburse_core`.
5. مسبارٌ لكلِّ مقعدٍ عندَ IN_REVIEW.

## 3. خارجَ النطاق
- أيُّ تصميمٍ لـM1 أو عبورٍ للمال.
- K1.
- تفكيكُ `ExecutiveCore.submit/run` (2B).
- أيُّ استثناءٍ غيرِ زوجَي `open_case`.
- تخفيفُ أيِّ حارس.

## 4. ما لم يُقَس
- لم تُشغَّل المجموعةُ بالكاشف، فقد يوجدُ تعشيشٌ ديناميكيٌّ لم يرصدْه التحليلُ النصّيّ (Q-9 § 8). يُقاسُ في الخطوة 3، وأيُّ تعشيشٍ جديدٍ يُعرَضُ على المالكِ ولا يُستثنى بيدِ المنفِّذ.
- لم يُقَس أنَّ معوِّضَ `open_case` يجري **داخلَ** إطارِ الحدِّ لا بعدَه. فإن جرى بعدَه، سقطَ الزوجُ `("gov.case.open", "task.cancel")` من الاستثناء، ويُعلَنُ ذلك.
- لم يُقَس سلوكُ `ContextVar` عبرَ الخيوطِ في عمّالِ الصادر.
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git diff 9343479073d65f4ceb61d5ba9ba273452651987c^ 9343479073d65f4ceb61d5ba9ba273452651987c -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py
EXIT: 0
BYTES: 6593
SHA256: 6391cddcd4aba7e38513558549f3bbb0d55217b091efbd66ce837de147f0233e
NO_EOL: 0
--- OUTPUT ---
diff --git a/federal/executive/services/src/amos_federation/services/state_treasury/service.py b/federal/executive/services/src/amos_federation/services/state_treasury/service.py
index e78cade2..c87ec5c0 100644
--- a/federal/executive/services/src/amos_federation/services/state_treasury/service.py
+++ b/federal/executive/services/src/amos_federation/services/state_treasury/service.py
@@ -835,9 +835,15 @@ class StateTreasury:
     def _existing_idempotent(
         self, session, context: AuthorizationContext, idempotency_key: str | None
     ) -> TransactionModel | None:
+        """الحركةُ السابقةُ بالمفتاحِ نفسِه — أو لا شيء.
+
+        WI-115 (Q-9 § 3.5): حركةٌ معكوسةٌ لا تُعادُ «نجاحًا متطابقًا». كانت تُعادُ بـ
+        `idempotent=True` وحالتُها `reversed`، فيحسبُ المُنادي مالًا صُرِفَ وهو مردود.
+        والصرفُ الجديدُ يلزمُه مفتاحٌ جديد — فلا تُنشأُ هنا حركةٌ ولا تُبتلَعُ الإعادة.
+        """
         if not idempotency_key:
             return None
-        return (
+        existing = (
             session.query(TransactionModel)
             .filter(
                 TransactionModel.tenant_id == self._tenant_of(context),
@@ -845,6 +851,12 @@ class StateTreasury:
             )
             .first()
         )
+        if existing is not None and existing.status == "reversed":
+            raise EntityStateError(
+                f"الحركةُ بالمفتاحِ '{idempotency_key}' معكوسةٌ — لا تُعادُ نجاحًا ولا صرفًا؛"
+                " صرفٌ جديدٌ يلزمُه مفتاحٌ جديد"
+            )
+        return existing
 
     # ── 1. تأسيس خزانة ────────────────────────────────────────────────────
 
diff --git a/federal/executive/services/tests/test_wi115_reversed_replay.py b/federal/executive/services/tests/test_wi115_reversed_replay.py
new file mode 100644
index 00000000..f581a817
--- /dev/null
+++ b/federal/executive/services/tests/test_wi115_reversed_replay.py
@@ -0,0 +1,86 @@
+"""
+الهدف: إثباتُ أنَّ إعادةَ صرفٍ بمفتاحِ حركةٍ معكوسةٍ تُرفَضُ ولا تُعادُ «نجاحًا متطابقًا» (WI-115 · Q-9 § 3.5)
+النطاق: federal/executive/services — `StateTreasury._existing_idempotent` ومُناديه `disburse`
+المالك: federal/executive/services
+تاريخ الإنشاء: 2026-10-25 (WI-115)
+تاريخ آخر تعديل: 2026-10-25
+
+قاسَت وثيقةُ التصميمِ (`docs/audit/Q9_NESTING_DETECTOR_DESIGN.md` § 1 بند 4) أنَّ
+`_existing_idempotent` يُرشِّحُ بالمستأجرِ والمفتاحِ وحدَهما، فإعادةُ الصرفِ بمفتاحِ حركةٍ
+عكسَها `reverse_transaction` كانت تُعيدُ الحركةَ المعكوسةَ بـ`idempotent=True`.
+
+ويُفحَصُ الشِّقّان: الرفضُ (الإصلاح)، وبقاءُ الإعادةِ المتطابقةِ لحركةٍ قائمةٍ (لا كسرَ
+لعقدِ عدمِ التكرار). وما **لا** يُفحَصُ هنا: `post_funding` و`execute_decision_disbursement`
+— يشتركانِ في الدالّةِ نفسِها ولم يُمارَسا في هذا الملفّ (حدٌّ مُعلَن).
+"""
+
+from __future__ import annotations
+
+import uuid
+
+import pytest
+
+from amos_federation.common.database import get_session_factory
+from amos_federation.services.state_treasury.models import TransactionModel
+from amos_federation.services.state_treasury.service import EntityStateError
+from tests.test_r7b_state_treasury import (  # noqa: F401 — مثبِّتاتُ pytest تُستورَدُ بأسمائها
+    _allocate,
+    _fiscal,
+    _fresh_state,
+    crown,
+    registry,
+    treasury,
+)
+
+
+def _disburse(store, context, fiscal, allocation, key: str, purpose: str) -> dict:
+    return store.disburse(
+        context=context,
+        allocation_id=allocation["id"],
+        expense_account_code=fiscal.expense["code"],
+        amount="1500",
+        purpose=purpose,
+        official_id=fiscal.official["id"],
+        idempotency_key=key,
+    )
+
+
+def _transactions() -> int:
+    session = get_session_factory()()
+    try:
+        return session.query(TransactionModel).count()
+    finally:
+        session.close()
+
+
+def test_replay_of_reversed_disbursement_is_refused(treasury, registry, crown) -> None:  # noqa: F811
+    """صرفٌ ← عكسٌ ← إعادةُ الصرفِ بالمفتاحِ نفسِه: خطأٌ صريحٌ، لا نجاحٌ ولا حركةٌ جديدة."""
+    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
+    allocation = _allocate(treasury, crown, fiscal, amount="10000")
+    key = f"wi115-{uuid.uuid4().hex[:8]}"
+    posted = _disburse(treasury, crown, fiscal, allocation, key, "صرفٌ سيُعكَس")
+    treasury.reverse_transaction(
+        context=crown,
+        reference=posted["reference"],
+        reason="خطأٌ في المستند",
+        official_id=fiscal.official["id"],
+    )
+    before = _transactions()
+
+    with pytest.raises(EntityStateError, match="معكوسةٌ"):
+        _disburse(treasury, crown, fiscal, allocation, key, "إعادةُ الطلبِ نفسِه")
+
+    assert _transactions() == before, "الرفضُ لا يُنشئُ حركةً"
+    budget = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])
+    assert budget["spent"] == "0.0000", "المصروفُ بعدَ العكسِ صفرٌ ولم يتغيّرْ بالإعادة"
+
+
+def test_replay_of_live_disbursement_stays_idempotent(treasury, registry, crown) -> None:  # noqa: F811
+    """لا كسرَ لعقدِ عدمِ التكرار: الحركةُ القائمةُ تُعادُ بعينِها كما كانت."""
+    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
+    allocation = _allocate(treasury, crown, fiscal, amount="10000")
+    key = f"wi115-{uuid.uuid4().hex[:8]}"
+    first = _disburse(treasury, crown, fiscal, allocation, key, "صرفٌ مرّةً واحدة")
+    second = _disburse(treasury, crown, fiscal, allocation, key, "الطلبُ نفسُه مُعادًا")
+    assert second["id"] == first["id"]
+    assert second.get("idempotent") is True
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
EXIT: 0
BYTES: 639
SHA256: e48b06aa538cd48d2273f3f3b1f9d973c63e5c10d0cd7ab393187485f81dab25
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 2 items

tests/test_wi115_reversed_replay.py ..                                   [100%]

============================== 2 passed in 1.32s ===============================
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && nl -ba federal/executive/services/src/amos_federation/services/state_treasury/service.py | sed -n '820,880p'
EXIT: 0
BYTES: 3479
SHA256: f6bab3e128332730c67aebe39fe47b7c7144a6ec9770bfd984c78e9caad5e54c
NO_EOL: 0
--- OUTPUT ---
   820	            # فيُفرض الترتيب صراحةً بدل الاعتماد على استنتاج المُخطِّط.
   821	            session.add(tx)
   822	            session.flush()
   823	            for entry in entries:
   824	                session.add(entry)
   825	            session.flush()
   826	            # إسناد السلطة يُكتب في **نفس** المعاملة — فلا حركة ملتزمة بلا من أجازها.
   827	            self._record_transaction_authority(session, context, transaction=tx, decision=authority)
   828	            session.flush()
   829	            session.commit()
   830	        except IntegrityError as exc:
   831	            session.rollback()
   832	            raise TreasuryError(f"تعذّر إدخال الحركة '{tx_reference}': {exc.orig}") from exc
   833	        return tx, entries
   834	
   835	    def _existing_idempotent(
   836	        self, session, context: AuthorizationContext, idempotency_key: str | None
   837	    ) -> TransactionModel | None:
   838	        """الحركةُ السابقةُ بالمفتاحِ نفسِه — أو لا شيء.
   839	
   840	        WI-115 (Q-9 § 3.5): حركةٌ معكوسةٌ لا تُعادُ «نجاحًا متطابقًا». كانت تُعادُ بـ
   841	        `idempotent=True` وحالتُها `reversed`، فيحسبُ المُنادي مالًا صُرِفَ وهو مردود.
   842	        والصرفُ الجديدُ يلزمُه مفتاحٌ جديد — فلا تُنشأُ هنا حركةٌ ولا تُبتلَعُ الإعادة.
   843	        """
   844	        if not idempotency_key:
   845	            return None
   846	        existing = (
   847	            session.query(TransactionModel)
   848	            .filter(
   849	                TransactionModel.tenant_id == self._tenant_of(context),
   850	                TransactionModel.idempotency_key == idempotency_key,
   851	            )
   852	            .first()
   853	        )
   854	        if existing is not None and existing.status == "reversed":
   855	            raise EntityStateError(
   856	                f"الحركةُ بالمفتاحِ '{idempotency_key}' معكوسةٌ — لا تُعادُ نجاحًا ولا صرفًا؛"
   857	                " صرفٌ جديدٌ يلزمُه مفتاحٌ جديد"
   858	            )
   859	        return existing
   860	
   861	    # ── 1. تأسيس خزانة ────────────────────────────────────────────────────
   862	
   863	    def establish_treasury(
   864	        self,
   865	        *,
   866	        context: AuthorizationContext,
   867	        code: str,
   868	        name: str,
   869	        currency: str,
   870	        institution_code: str | None = None,
   871	    ) -> dict[str, Any]:
   872	        """أسِّس خزانة بعملة واحدة، تابعةً لمؤسسة أو مركزية."""
   873	        resolve_money_delegation("treasury.establish", entrypoint="establish_treasury")
   874	        require_domain_permission(context, "treasury.establish", PERMISSIONS_TREASURY_ESTABLISH)
   875	        currency_code = normalize_currency(currency)
   876	        if not name.strip():
   877	            raise TreasuryError("الخزانة تلزمها تسمية")
   878	
   879	        session = self._session()
   880	        try:
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rm -rf ../old && git worktree add --detach ../old 9343479073d65f4ceb61d5ba9ba273452651987c^ && cp federal/executive/services/tests/test_wi115_reversed_replay.py ../old/federal/executive/services/tests/ && cd ../old/federal/executive/services && PYTHONPATH=src /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
EXIT: 1
BYTES: 1583
SHA256: ade9f4ee37ffc4fc7680178e39b7873026493c973efae7d750012ec4688e9bde
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD 6605fa88)
HEAD is now at 6605fa88 W-669: WI-113 — أداةُ الجردِ تفهرسُ بالاسمِ المؤهَّلِ · تصحيحُ قياسٍ لا حرقٌ: D-4 142→135 (W3 97→90) · فحصٌ (4) وطفرتانِ · اللقطاتُ المحروسةُ مُعادةٌ — المنسِّقُ Claude Opus 5.5
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w673/gemini_3_8_flash/wi115/old/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 2 items

tests/test_wi115_reversed_replay.py F.                                   [100%]

=================================== FAILURES ===================================
_______________ test_replay_of_reversed_disbursement_is_refused ________________
tests/test_wi115_reversed_replay.py:70: in test_replay_of_reversed_disbursement_is_refused
    with pytest.raises(EntityStateError, match="معكوسةٌ"):
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: DID NOT RAISE EntityStateError
=========================== short test summary info ============================
FAILED tests/test_wi115_reversed_replay.py::test_replay_of_reversed_disbursement_is_refused
========================= 1 failed, 1 passed in 1.37s ==========================
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rg -n 'def disburse|def reverse|def execute_transfer|_existing_idempotent\(' federal/executive/services/src/amos_federation/services/state_treasury/service.py
EXIT: 0
BYTES: 358
SHA256: a6b95a497ac6e4d82cac41a3b3558f764dd4865e42e98055ec3e68a816066493
NO_EOL: 0
--- OUTPUT ---
835:    def _existing_idempotent(
1245:            existing = self._existing_idempotent(session, context, idempotency_key)
1321:    def disburse(
1349:            existing = self._existing_idempotent(session, context, idempotency_key)
1491:            existing = self._existing_idempotent(session, context, idempotency_key)
1529:    def reverse_transaction(
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rg -n 'WI-110|WI-115|D25-3|§ ?3.5' docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 0
BYTES: 11994
SHA256: 0d44cc1d78d54899dc57881dbe1abe5900fe8ecb1dd784447cd63807f3a5c332
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-25 (`W-671` — **قراراتُ التوجيهِ 23 DECIDED** بنصوصِها الحرفيّةِ في قيدٍ واحدٍ: D25-1 (canary § 5 الخيارُ 1 `require_king` بشروطِ أ/ب/ج) · D25-2 (تحصينُ مساراتِ الخفضِ والترقيةِ بـ`require_king` — بندُ C3 مستقلٌّ) · D25-3 (ترتيبُ Q-9: الكاشفُ ثمَّ M1) · وWI-112 قيسَ بلا سرٍّ) · ووقبله 2026-10-25 (`W-660` — **قراراتُ التوجيهِ 22 DECIDED** بنصوصِها الحرفيّةِ في قيدٍ واحدٍ: D24-1 (إغلاقُ WI-084) · D24-R2 (الخيارُ 1 بمعيارِ الاستردادِ) · Q-72 (الخيارُ 1) · WI-109 (A1: الخيارُ 4 — أ · ب · هـ · وج ود سؤالانِ) · WI-110 (Q-9: الخيارُ 4) · WI-112 (السرُّ للمالكِ)) · ووقبله ((`W-649` — **D23 DECIDED**: إغلاقُ WI-106 · WI-107 · WI-111 وتصحيحُ خريطةِ أسطرِ WI-084 ثمَّ جولةٌ جديدةٌ (نصُّ المالكِ حرفيًّا)) · ووقبله ((`W-636/W-637` — تسجيلُ WI-109 (تحليلُ A1) · WI-110 (تحليلُ Q-9) · WI-111 (J2+J3 · 15 سطحًا محسومًا مقيسًا) READY · حرسُ D21-د تحتَ WI-040 (`NEW_ITEM_CLAIMING_ENTRY`) · N+1 لـW-631…W-635 أخضرُ (40030379965) · تصحيحُ تاريخِ الرياضِ في D21-هـ) · ووقبله ((`W-632…W-635` — قراراتُ المالكِ بتوجيهِ المستشارِ 21 على ورقةِ D20 بنصوصِها الحرفيّةِ: Q-7 · Q-8 · Q-13 · Q-14 · Q-23 · Q-26 · Q-28 · Q-29 · Q-30 · Q-32 · Q-33 · Q-34 · Q-36 · Q-37 · Q-41 · E1 DECIDED · وA1 وQ-9 وQ-10 تحليلٌ/قياسٌ أوّلًا) · ووقبله (`W-625` — **Q-71 DECIDED** بأمرِ المالكِ الصريحِ: «أذن بـconftest.py تحت WI-107» — قسمةُ نطاقِ مسارِ conftest.py من WI-072 إلى WI-107) · ووقبله (`W-612` — **D17-2** الأربعةُ مؤجَّلةٌ ولا تعطّلُ J2/J3 · **إبلاغُ ما بعدَ الدمجِ** يبقى إبلاغًا (توجيهُ المستشارِ 19 § 1)) · ووقبله ((`W-611` — **Q-61 DECIDED** بالخيارِ (3) بتطبيقٍ صريحٍ على WI-096 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-610` — **D19 DECIDED**: إذنُ المالكِ بإغلاقِ WI-105 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`))))
2358:**السند:** توجيهُ المستشارِ 23 § 1 — «تسليمُ المالك هذا التوجيه إلى الوكيل هو الذي يُصدرها، وبتاريخ تسليمه» · سلَّمَه المالكُ إلى الوكيلِ 2026-10-25 · النصُّ الكاملُ حرفيًّا في [`evidence/W-671/ADVISOR_DIRECTIVE_23.md`](evidence/W-671/ADVISOR_DIRECTIVE_23.md) · والمعرِّفاتُ D25-1…D25-3 تسميةُ المنفِّذِ للفهرسةِ لا نصُّ المالكِ.
2366:### D25-3 · ترتيبُ Q-9 — DECIDED (W-671)
2367:«ترتيب Q-9: قراءتُك صحيحة. المال غير محروس اليوم، فإعلان الآثار يأتي مع M1. الكاشف أولًا، ثم M1.» ⇒ كاشفُ التعشيشِ (WI-115 الشقُّ الثاني) أولًا ثمَّ M1 · وإعلانُ الآثارِ مع M1 لا قبلَه.
2388:### WI-110 (Q-9) · الخيارُ 4 — DECIDED (W-660)
2389:«WI-110 (Q-9): أقبل الخيار 4: يُمنع التعشيش السيادي بكاشف عند الحد، ويُعاد هيكلة مركّبات المال الثلاثة على نمط «الخارجي يُعلن الآثار وينادي نوًى خاصة»، ويُستثنى open_case باسمه استثناءً مسجَّلًا، ويُعالَج خطر إعادة disburse لحركة معكوسة (§3.5) قبل M1.» ⇒ الكاشفُ وإصلاحُ § 3.5 بندٌ قبلَ أيِّ تصميمٍ لـM1 (W-663) · وWI-110 يبقى `IN_REVIEW`.
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && sha256sum docs/audit/evidence/W-673/briefs_wi115/briefing_gemini_3_8_flash.md
EXIT: 0
BYTES: 134
SHA256: ce4f36c0ac9b28073fac1757c2fbf415d40806be321b7d1ee99ac9a4fcec3d80
NO_EOL: 0
--- OUTPUT ---
ebffbff8383f5217c1aef463e4bcc14f232c0e8efbb6bd99b80a51b9225c69f0  docs/audit/evidence/W-673/briefs_wi115/briefing_gemini_3_8_flash.md
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && cat docs/audit/evidence/W-673/briefs_wi115/SHA256SUMS
EXIT: 0
BYTES: 268
SHA256: 696f6d5a31a4498b98b50da63c80abfdd17864b190e99a83ff59919c4b8d2fb4
NO_EOL: 0
--- OUTPUT ---
ebffbff8383f5217c1aef463e4bcc14f232c0e8efbb6bd99b80a51b9225c69f0  briefing_gemini_3_8_flash.md
d1f550231cf27baa0f6a85de3a6eb664dc587dc7c6623a6f9dc5755848046c0c  briefing_grok_4_7.md
efc856e68db9cc688d8980209976c6ea478ffdc52be66625447f38c97fc75eb0  briefing_kimi_k3.md
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w673/gemini_3_8_flash/wi115/probe/test_wi115_probe.py
EXIT: 0
BYTES: 12321
SHA256: 0471af7b52ed1b55d0f9dd0ba6138829984dadcc181ddc4d876a4d37f91cdebc
NO_EOL: 0
--- OUTPUT ---
     1	"""
     2	الهدف: مسبار مجلس المراجعة (gemini_3_8_flash) لبند WI-115 (Q-9 § 3.5).
     3	النطاق: federal/executive/services — اختبار المسار الإنتاجي لـ StateTreasury._existing_idempotent وdisburse ومحاولة كسر الخاصية المدعاة.
     4	المالك: مجلس المراجعة — مقعد gemini_3_8_flash
     5	تاريخ الإنشاء: 2026-10-26
     6	
     7	الخواص المفحوصة في هذا المسبار لمحاولة كسر السلوك:
     8	1. محاولة كسر خاصية المنع: هل تمر إعادة الصرف لحركة معكوسة صامتة؟ هل تُنشأ حركة جديدة؟ هل يتغيّر الرصيد أو المصروف؟
     9	2. محاولة كسر خاصية عدم التكرار المشروعة: هل يؤثر الإصلاح على إعادة صرف حركة قائمة (posted) فيمنعها أو يُسقط idempotent=True؟
    10	3. محاولة كسر استئناف الصرف: هل يمنع حظر المفتاح المعكوس إجراء صرف جديد شرعي بمفتاح جديد لنفس التخصيص والغرض؟
    11	4. فحص نمط مفتاح execute_transfer (`trf-{reference}`): هل يُرفض استخدام المفتاح المعكوس بصيغة التحويل الاقتصادي؟
    12	5. فحص التعامل مع المفتاح الفارغ (None): هل يبقى سلوك المفاتيح غير المعرفة سليمًا دون رفع أخطاء غير مبررة؟
    13	"""
    14	
    15	from __future__ import annotations
    16	
    17	import uuid
    18	from decimal import Decimal
    19	
    20	import pytest
    21	
    22	from amos_federation.common.database import get_session_factory
    23	from amos_federation.services.state_treasury.models import TransactionModel
    24	from amos_federation.services.state_treasury.service import EntityStateError
    25	from tests.test_r7b_state_treasury import (  # noqa: F401 — fixtures
    26	    _allocate,
    27	    _fiscal,
    28	    _fresh_state,
    29	    crown,
    30	    registry,
    31	    treasury,
    32	)
    33	
    34	
    35	def _count_transactions() -> int:
    36	    session = get_session_factory()()
    37	    try:
    38	        return session.query(TransactionModel).count()
    39	    finally:
    40	        session.close()
    41	
    42	
    43	def test_probe_break_attempt_reversed_replay(treasury, registry, crown) -> None:  # noqa: F811
    44	    """محاولة كسر 1: إعادة الصرف بعد العكس بالمفتاح نفسه يجب أن تُرفض ولا تُغيّر الأرصدة ولا تُنشئ صفوفًا."""
    45	    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
    46	    allocation = _allocate(treasury, crown, fiscal, amount="20000")
    47	    key = f"probe-wi115-{uuid.uuid4().hex[:8]}"
    48	
    49	    # صرف أولي شرعي
    50	    first = treasury.disburse(
    51	        context=crown,
    52	        allocation_id=allocation["id"],
    53	        expense_account_code=fiscal.expense["code"],
    54	        amount="2500",
    55	        purpose="صرف أولي للاختبار",
    56	        official_id=fiscal.official["id"],
    57	        idempotency_key=key,
    58	    )
    59	    assert first["status"] == "posted"
    60	    assert first.get("idempotent") is False or first.get("idempotent") is None
    61	
    62	    # التحقق من رصيد المصروف
    63	    bal_after_first = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])
    64	    assert bal_after_first["spent"] == "2500.0000"
    65	
    66	    # عكس الحركة
    67	    treasury.reverse_transaction(
    68	        context=crown,
    69	        reference=first["reference"],
    70	        reason="عكس لاختبار المسبار",
    71	        official_id=fiscal.official["id"],
    72	    )
    73	
    74	    bal_after_rev = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])
    75	    assert bal_after_rev["spent"] == "0.0000", "العكس يعيد المصروف إلى الصفر"
    76	    tx_count_after_rev = _count_transactions()
    77	
    78	    # محاولة كسر: إعادة الطلب بنفس المفتاح
    79	    with pytest.raises(EntityStateError, match="معكوسةٌ"):
    80	        treasury.disburse(
    81	            context=crown,
    82	            allocation_id=allocation["id"],
    83	            expense_account_code=fiscal.expense["code"],
    84	            amount="2500",
    85	            purpose="إعادة صرف بنفس المفتاح بعد العكس",
    86	            official_id=fiscal.official["id"],
    87	            idempotency_key=key,
    88	        )
    89	
    90	    # التحقق من عدم كسر الحصانة: لا حركة جديدة ولا تغيّر في الرصيد
    91	    assert _count_transactions() == tx_count_after_rev, "فشل الإعادة لا يُنشئ أي صف جديد في الدفتر"
    92	    bal_after_failed_replay = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])
    93	    assert bal_after_failed_replay["spent"] == "0.0000", "رصيد المصروف يبقى صفرًا ولا يتغيّر بإعادة الطلب المرفوض"
    94	
    95	
    96	def test_probe_break_attempt_live_replay_unaffected(treasury, registry, crown) -> None:  # noqa: F811
    97	    """محاولة كسر 2: التحقق أن الإصلاح لم يكسر إعادة الصرف المشروع لحركة قائمة (posted)."""
    98	    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
    99	    allocation = _allocate(treasury, crown, fiscal, amount="20000")
   100	    key = f"probe-live-{uuid.uuid4().hex[:8]}"
   101	
   102	    # صرف أول
   103	    initial = treasury.disburse(
   104	        context=crown,
   105	        allocation_id=allocation["id"],
   106	        expense_account_code=fiscal.expense["code"],
   107	        amount="1800",
   108	        purpose="صرف قائم شرعي",
   109	        official_id=fiscal.official["id"],
   110	        idempotency_key=key,
   111	    )
   112	
   113	    tx_count_before = _count_transactions()
   114	
   115	    # إعادة نفس الطلب لحركة قائمة — يجب أن تنجح ويعود idempotent=True
   116	    replay = treasury.disburse(
   117	        context=crown,
   118	        allocation_id=allocation["id"],
   119	        expense_account_code=fiscal.expense["code"],
   120	        amount="1800",
   121	        purpose="إعادة طلب الصرف القائم",
   122	        official_id=fiscal.official["id"],
   123	        idempotency_key=key,
   124	    )
   125	
   126	    assert replay["id"] == initial["id"], "الإعادة المتطابقة تعيد نفس المعاملة"
   127	    assert replay.get("idempotent") is True, "الإعادة تعلن idempotent=True"
   128	    assert _count_transactions() == tx_count_before, "لا حركة جديدة تُنشأ"
   129	
   130	    bal = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])
   131	    assert bal["spent"] == "1800.0000", "المصروف لا يتضاعف مع الإعادة المتطابقة"
   132	
   133	
   134	def test_probe_break_attempt_legitimate_new_key_after_reversal(treasury, registry, crown) -> None:  # noqa: F811
   135	    """محاولة كسر 3: التحقق أن رفض المفتاح المعكوس لا يحظر صرفًا جديدًا بمفتاح جديد على نفس التخصيص."""
   136	    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
   137	    allocation = _allocate(treasury, crown, fiscal, amount="20000")
   138	    key_old = f"probe-rev-{uuid.uuid4().hex[:8]}"
   139	    key_new = f"probe-new-{uuid.uuid4().hex[:8]}"
   140	
   141	    orig = treasury.disburse(
   142	        context=crown,
   143	        allocation_id=allocation["id"],
   144	        expense_account_code=fiscal.expense["code"],
   145	        amount="1200",
   146	        purpose="صرف أولي سيعكس",
   147	        official_id=fiscal.official["id"],
   148	        idempotency_key=key_old,
   149	    )
   150	    treasury.reverse_transaction(
   151	        context=crown,
   152	        reference=orig["reference"],
   153	        reason="عكس نظامي",
   154	        official_id=fiscal.official["id"],
   155	    )
   156	
   157	    # صرف جديد بمفتاح جديد
   158	    new_tx = treasury.disburse(
   159	        context=crown,
   160	        allocation_id=allocation["id"],
   161	        expense_account_code=fiscal.expense["code"],
   162	        amount="1200",
   163	        purpose="صرف بديل بمفتاح جديد",
   164	        official_id=fiscal.official["id"],
   165	        idempotency_key=key_new,
   166	    )
   167	
   168	    assert new_tx["id"] != orig["id"]
   169	    assert new_tx["status"] == "posted"
   170	    bal = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])
   171	    assert bal["spent"] == "1200.0000"
   172	
   173	
   174	def test_probe_break_attempt_transfer_reference_key_pattern(treasury, registry, crown) -> None:  # noqa: F811
   175	    """محاولة كسر 4: التحقق من نمط مفاتيح التحويل execute_transfer (trf-{reference}) عند العكس والإعادة."""
   176	    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
   177	    allocation = _allocate(treasury, crown, fiscal, amount="20000")
   178	    trf_ref = f"TRF-EXP-{uuid.uuid4().hex[:8]}"
   179	    trf_key = f"trf-{trf_ref}"
   180	
   181	    posted = treasury.disburse(
   182	        context=crown,
   183	        allocation_id=allocation["id"],
   184	        expense_account_code=fiscal.expense["code"],
   185	        amount="3400",
   186	        purpose="صرف تحويل اقتصادي",
   187	        official_id=fiscal.official["id"],
   188	        idempotency_key=trf_key,
   189	    )
   190	
   191	    treasury.reverse_transaction(
   192	        context=crown,
   193	        reference=posted["reference"],
   194	        reason="عكس تحويل ملغى",
   195	        official_id=fiscal.official["id"],
   196	    )
   197	
   198	    # محاولة إعادة الصرف بمفتاح التحويل trf-{reference}
   199	    with pytest.raises(EntityStateError, match="معكوسةٌ"):
   200	        treasury.disburse(
   201	            context=crown,
   202	            allocation_id=allocation["id"],
   203	            expense_account_code=fiscal.expense["code"],
   204	            amount="3400",
   205	            purpose="إعادة صرف التحويل المعكوس",
   206	            official_id=fiscal.official["id"],
   207	            idempotency_key=trf_key,
   208	        )
   209	
   210	
   211	def test_probe_none_idempotency_key_remains_functional(treasury, registry, crown) -> None:  # noqa: F811
   212	    """محاولة كسر 5: التأكد من أن عدم تمرير مفتاح عدم تكرار (None) لا يتأثر بفحص الحالة المعكوسة."""
   213	    fiscal = _fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
   214	    allocation = _allocate(treasury, crown, fiscal, amount="20000")
   215	
   216	    tx1 = treasury.disburse(
   217	        context=crown,
   218	        allocation_id=allocation["id"],
   219	        expense_account_code=fiscal.expense["code"],
   220	        amount="500",
   221	        purpose="صرف بلا مفتاح 1",
   222	        official_id=fiscal.official["id"],
   223	        idempotency_key=None,
   224	    )
   225	    tx2 = treasury.disburse(
   226	        context=crown,
   227	        allocation_id=allocation["id"],
   228	        expense_account_code=fiscal.expense["code"],
   229	        amount="500",
   230	        purpose="صرف بلا مفتاح 2",
   231	        official_id=fiscal.official["id"],
   232	        idempotency_key=None,
   233	    )
   234	
   235	    assert tx1["id"] != tx2["id"]
   236	    assert tx1["status"] == "posted"
   237	    assert tx2["status"] == "posted"
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider /home/user/workspace/council_w673/gemini_3_8_flash/wi115/probe/test_wi115_probe.py
EXIT: 0
BYTES: 98
SHA256: e7481acd2034e7c1f5456e576ef094e80e72ae4ee4ac2c1825a98f7552554a86
NO_EOL: 0
--- OUTPUT ---
.....                                                                    [100%]
5 passed in 1.29s
=== RAW [15] END ===
VERDICT_PER_CRITERION:
- المعيار (1) قبل الشفرة: وثيقة التصميم بقياسات مولدة بأوامر (DISC-136): نعم. وثيقة التصميم `docs/audit/Q9_NESTING_DETECTOR_DESIGN.md` أُودعت في الالتزام 5086fb4e (قيد W-665 بتاريخ 2026-10-25T08:00:16Z) سابقًا لالتزام الشفرة 93434790 (قيد W-670 بتاريخ 2026-10-25T08:45:43Z) كما يثبت سجل git (الكتلة [4])، وتحمل وثيقة التصميم القياسات والتحليلات المطلوبة (الكتلة [5]).
- المعيار (2) إصلاح § 3.5: إعادة صرف لحركة reversed لا تعيدها صامتة — فحص يسقط قبل وينجح بعد: نعم. التحقق بالشفرة المطبقة في `StateTreasury._existing_idempotent` حيث ترفع `EntityStateError` صراحة عند مصادفة حركة معكوسة بالمفتاح نفسه (الكتلتان [6] و[8]). والفحص `test_wi115_reversed_replay.py` ينجح على شجرة العمل الحالية 2 passed (الكتلة [7])، ويسقط على الشجرة السابقة للالتزام W-670 بـ `Failed: DID NOT RAISE EntityStateError` في شجرة عمل منفصلة (الكتلة [9]).
- المعيار (3) الكاشف يرفض عبورًا سياديًا داخل عبور نشط قبل decide · وopen_case مستثنى باسمه استثناءً مسجلًا: لا · لم يُنفَّذْ (خارج نطاق هذه الجولة الجزئية المعلنة بقرار التوجيه 23 § 2 وقرار D25-3، حيث ينحصر نطاق هذه الجولة في شق إصلاح § 3.5 وحده، ويعود البند بعد الجولة IN_PROGRESS لكاشف التعشيش).
- المعيار (4) المركبات الثلاثة تعلن الآثار وتنادي نوى خاصة فلا تُرفض بالكاشف: لا · لم يُنفَّذْ (خارج نطاق هذه الجولة الجزئية المعلنة — يأتي مع إعلان الآثار في M1 بحسب قرار D25-3).
- المعيار (5) طفرات حذف الكاشف وحذف إصلاح § 3.5 تُكتشف: نعم لشق إصلاح § 3.5 (الأمر 9 أعاد تشغيل الفحص على شجرة الشفرة بدون الإصلاح وأسقط الفحص صراحة وهو ما يثبت كشف طفرة حذف الإصلاح)؛ وشق الكاشف لم يُنفّذ لكون الكاشف خارج نطاق هذه الجولة.
- المعيار (6) مسبار لكل مقعد: نعم (الكتلتان [14] و[15]).
PROBES:
- مسبار 1: شفرته [14] · تشغيله [15] · الخاصية التي حاول كسرها: محاولة كسر منع إعادة الصرف لحركة معكوسة (هل تمر صامتة؟ هل يتغير رصيد المصروف؟ هل يُنشأ صف حركة جديد؟)، ومحاولة كسر عدم التكرار لحركة قائمة (posted)، ومحاولة كسر استئناف الصرف بمفتاح جديد، ومحاولة كسر نمط مفتاح execute_transfer (`trf-{reference}`)، وفحص تمرير مفتاح فارغ (None) · انكسرت؟ لا (رُفِضت إعادة الصرف المعكوس بـ EntityStateError وثبتت الأرصدة وعدد الصفوف، وظلت الإعادة القائمة idempotent=True، ونجح الصرف بمفتاح جديد، ومفتاح التحويل رُفِض عند العكس، والمفتاح الفارغ لم يرفع خطأً).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: أقرُّ بأنّني لم أقرأْ شيئًا خارجَ استنساخي وهذهِ الإحاطةِ، وأنّ جميعَ الأوامرِ جرى تشغيلُها فعليًّا داخلَ جذري الخاصِّ /home/user/workspace/council_w673/gemini_3_8_flash/wi115، والمخرجاتُ ملتقطةٌ خامًا بأداةِ الالتقاطِ بلا أيِّ اقتطاعٍ أو تحريرٍ أو تدخّلٍ يدويٍّ.
VERDICT: PASS
