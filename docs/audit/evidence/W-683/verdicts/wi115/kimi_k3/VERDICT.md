# حكمُ مقعدِ المجلسِ — kimi_k3 · جولةُ WI-115 (W-683)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-115 (النطاقُ المنفَّذُ: إصلاحُ § 3.5 وحدَه) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w673/kimi_k3/wi115) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `4f0d56f8154c21e461837ccc7fb16388e6cc4a74b34f907c4c08dd0d1b8323d2`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-115 عندَ العقدةِ `79abc6a2` — إحاطةٌ مبصومةٌ (W-673) ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9) · ومخرجاتُ الفاحصِ المصلَحِ (W-680 · main `76a0e5e4`) مقروءةٌ مقبولةً EXIT 0 (raw_check_outputs.txt في قيدِ W-683).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-683) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5) · والانتقالُ المقرَّرُ حتى معَ النصابِ: IN_REVIEW→IN_PROGRESS لكاشفِ التعشيشِ (D25-3 — كما قُيِّدَ في W-681).

## تاريخ الإنشاء
2026-10-26

## تاريخ آخر تعديل
2026-10-26 (W-683 — القيدُ نفسُه)

---
MODEL: Kimi K3
FAMILY: Moonshot AI (Kimi)
RUN_DATE: 2026-10-26 04:03 +00:00
NODE: 79abc6a206000e162689d642d1ebc42af36f445a
CLONE_PATH: /home/user/workspace/council_w673/kimi_k3/wi115/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/
 2. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/)
 3. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
 5. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && cat docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
 6. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git diff 9343479073d65f4ceb61d5ba9ba273452651987c^ 9343479073d65f4ceb61d5ba9ba273452651987c -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py
 7. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
 8. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && nl -ba federal/executive/services/src/amos_federation/services/state_treasury/service.py | sed -n '820,880p'
 9. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && rm -rf ../old && git worktree add --detach ../old 9343479073d65f4ceb61d5ba9ba273452651987c^ && cp federal/executive/services/tests/test_wi115_reversed_replay.py ../old/federal/executive/services/tests/ && cd ../old/federal/executive/services && PYTHONPATH=src /home/user/workspace/council_w673/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
 10. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && rg -n 'def disburse|def reverse|def execute_transfer|_existing_idempotent\(' federal/executive/services/src/amos_federation/services/state_treasury/service.py
 11. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && rg -n 'WI-110|WI-115|D25-3|§ ?3.5' docs/audit/SOVEREIGN_DECISION_REGISTER.md
 12. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && sha256sum docs/audit/evidence/W-673/briefs_wi115/briefing_kimi_k3.md
 13. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && cat docs/audit/evidence/W-673/briefs_wi115/SHA256SUMS
 14. nl -ba /home/user/workspace/council_w673/kimi_k3/wi115/probe/probe_wi115_reversed_replay_kimi.py
 15. cd /home/user/workspace/council_w673/kimi_k3/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider -p tests.conftest /home/user/workspace/council_w673/kimi_k3/wi115/probe/probe_wi115_reversed_replay_kimi.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/)
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && cat docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && git diff 9343479073d65f4ceb61d5ba9ba273452651987c^ 9343479073d65f4ceb61d5ba9ba273452651987c -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
EXIT: 0
BYTES: 630
SHA256: 77c4cf0fe88c409bdbc77234d085524df0ebc4171bbe95ed673d17b6c8e1428d
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w673/kimi_k3/wi115/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 2 items

tests/test_wi115_reversed_replay.py ..                                   [100%]

============================== 2 passed in 2.78s ===============================
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && nl -ba federal/executive/services/src/amos_federation/services/state_treasury/service.py | sed -n '820,880p'
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && rm -rf ../old && git worktree add --detach ../old 9343479073d65f4ceb61d5ba9ba273452651987c^ && cp federal/executive/services/tests/test_wi115_reversed_replay.py ../old/federal/executive/services/tests/ && cd ../old/federal/executive/services && PYTHONPATH=src /home/user/workspace/council_w673/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
EXIT: 1
BYTES: 1574
SHA256: 5834e0d46200abbda00f1ea63112d14c11b2a3aa1affe453c6a45175f6c8b3e1
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD 6605fa88)
HEAD is now at 6605fa88 W-669: WI-113 — أداةُ الجردِ تفهرسُ بالاسمِ المؤهَّلِ · تصحيحُ قياسٍ لا حرقٌ: D-4 142→135 (W3 97→90) · فحصٌ (4) وطفرتانِ · اللقطاتُ المحروسةُ مُعادةٌ — المنسِّقُ Claude Opus 5.5
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w673/kimi_k3/wi115/old/federal/executive/services
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
========================= 1 failed, 1 passed in 1.43s ==========================
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && rg -n 'def disburse|def reverse|def execute_transfer|_existing_idempotent\(' federal/executive/services/src/amos_federation/services/state_treasury/service.py
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && rg -n 'WI-110|WI-115|D25-3|§ ?3.5' docs/audit/SOVEREIGN_DECISION_REGISTER.md
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
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && sha256sum docs/audit/evidence/W-673/briefs_wi115/briefing_kimi_k3.md
EXIT: 0
BYTES: 125
SHA256: 15016c45584cf406a0f4e032896a487dcdf43609cb3aa8121376ebbe2f4e07ed
NO_EOL: 0
--- OUTPUT ---
efc856e68db9cc688d8980209976c6ea478ffdc52be66625447f38c97fc75eb0  docs/audit/evidence/W-673/briefs_wi115/briefing_kimi_k3.md
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo && cat docs/audit/evidence/W-673/briefs_wi115/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w673/kimi_k3/wi115/probe/probe_wi115_reversed_replay_kimi.py
EXIT: 0
BYTES: 9134
SHA256: c35f7173b18a8be51e509ae6aca434fbe6f68e63899ba383954ad370c5f2581c
NO_EOL: 0
--- OUTPUT ---
     1	"""
     2	مسبارُ مقعدِ kimi_k3 — WI-115 (Q-9 § 3.5) — كتابةٌ مستقلّةٌ لا نسخةَ من الفحصِ القائم.
     3	الهدف: كسرُ الخاصيّةِ المُدَّعاةِ على المسارِ الإنتاجيِّ StateTreasury.disburse /
     4	reverse_transaction في federal/executive/services/.../state_treasury/service.py:
     5	
     6	  أ) هجومٌ غاشم: صرفٌ بمفتاح K ← عكسٌ ← إعادةُ الصرفِ بـK لكنَّ **بمبلغٍ وغرضٍ
     7	     وتخصيصٍ مختلفين** (متغيّراتٌ مسمومة). يجبُ رفضُها بـEntityStateError، وبلا
     8	     حركةٍ جديدة، وبلا تغيّرِ رصيد، والأصلُ يبقى `reversed`.
     9	  ب) العقدُ القائم: إعادةٌ متطابقةٌ لحركةٍ حيّةٍ (لم تُعكَس) بالمفتاحِ نفسِه
    10	     يجبُ أن تبقى `idempotent=True` بالمعرِّفِ نفسِه، مرّتين متتاليتين.
    11	
    12	إن نجحَت الإعادةُ في (أ) (رُجِعَت الحركةُ المعكوسةُ نجاحًا أو أُنشئَت حركةٌ
    13	جديدة أو تغيّرَ المصروف) فالخاصيّةُ منكسرةٌ ويُسقِطُ assert المسبارَ.
    14	وما لا يقيسُه هذا المسبار: execute_transfer على مستوى الخدمةِ الاقتصاديّةِ
    15	(حدٌّ مُعلَن — نطاقُ الجولةِ هو § 3.5 في الخزانة).
    16	"""
    17	
    18	from __future__ import annotations
    19	
    20	import os
    21	import uuid
    22	
    23	os.environ["AMOS_ENVIRONMENT"] = "test"
    24	
    25	import pytest
    26	
    27	from amos_federation.common.database import get_session_factory
    28	from amos_federation.services.state_treasury.models import TransactionModel
    29	from amos_federation.services.state_treasury.service import EntityStateError
    30	from tests.test_r7b_state_treasury import (  # noqa: F401 — المثبِّتاتُ تُستورَدُ بأسمائها
    31	    _allocate,
    32	    _fiscal,
    33	    _fresh_state,
    34	    crown,
    35	    registry,
    36	    treasury,
    37	)
    38	
    39	KEY_PREFIX = "kimi-probe"
    40	
    41	
    42	def _keys_count(key: str) -> int:
    43	    session = get_session_factory()()
    44	    try:
    45	        return (
    46	            session.query(TransactionModel)
    47	            .filter(TransactionModel.idempotency_key == key)
    48	            .count()
    49	        )
    50	    finally:
    51	        session.close()
    52	
    53	
    54	def _row_by_key(key: str):
    55	    session = get_session_factory()()
    56	    try:
    57	        return (
    58	            session.query(TransactionModel)
    59	            .filter(TransactionModel.idempotency_key == key)
    60	            .one()
    61	        )
    62	    finally:
    63	        session.close()
    64	
    65	
    66	def _spent(treasury, crown, budget_code: str) -> str:
    67	    return treasury.budget_balance(context=crown, budget_code=budget_code)["spent"]
    68	
    69	
    70	def test_poisoned_replay_after_reversal_must_not_pass(treasury, registry, crown) -> None:  # noqa: F811
    71	    """صرف ← عكس ← إعادةٌ بمتغيّراتٍ مسمومة: رفضٌ صريح ولا أثرَ ولا رصيدَ."""
    72	    fiscal = _fiscal(treasury, registry, crown, limit_amount="200000", funding="90000")
    73	    alloc_a = _allocate(treasury, crown, fiscal, amount="30000")
    74	    alloc_b = _allocate(treasury, crown, fiscal, amount="30000")
    75	    key = f"{KEY_PREFIX}-atk-{uuid.uuid4().hex[:10]}"
    76	
    77	    posted = treasury.disburse(
    78	        context=crown,
    79	        allocation_id=alloc_a["id"],
    80	        expense_account_code=fiscal.expense["code"],
    81	        amount="1200.50",
    82	        purpose="صرف تشغيلي أصلي",
    83	        official_id=fiscal.official["id"],
    84	        idempotency_key=key,
    85	    )
    86	    assert _keys_count(key) == 1
    87	    assert _spent(treasury, crown, fiscal.budget["code"]) == "1200.5000"
    88	
    89	    treasury.reverse_transaction(
    90	        context=crown,
    91	        reference=posted["reference"],
    92	        reason="مستند باطل — يُعكَس",
    93	        official_id=fiscal.official["id"],
    94	    )
    95	    assert _row_by_key(key).status == "reversed"
    96	    spent_after_reversal = _spent(treasury, crown, fiscal.budget["code"])
    97	    assert spent_after_reversal == "0.0000"
    98	    total_before = _keys_count(key)
    99	
   100	    # الهجوم: المفتاحُ نفسُه لكنَّ المبلغَ والغرضَ والتخصيصَ مغايرةٌ كلُّها.
   101	    with pytest.raises(EntityStateError, match="معكوسةٌ"):
   102	        treasury.disburse(
   103	            context=crown,
   104	            allocation_id=alloc_b["id"],
   105	            expense_account_code=fiscal.expense["code"],
   106	            amount="9999.99",
   107	            purpose="محاولة التفاف على مفتاح معكوس",
   108	            official_id=fiscal.official["id"],
   109	            idempotency_key=key,
   110	        )
   111	
   112	    assert _keys_count(key) == total_before == 1, "الرفضُ لا يُنشئُ حركةً بديلةً"
   113	    assert _row_by_key(key).id == posted["id"], "لم تُكتَبْ حركةٌ فوقَ الأصل"
   114	    assert _row_by_key(key).status == "reversed", "الأصلُ يبقى معكوسًا"
   115	    assert _spent(treasury, crown, fiscal.budget["code"]) == spent_after_reversal, (
   116	        "لا رصيدَ تغيّرَ بالهجوم"
   117	    )
   118	
   119	
   120	def test_mutated_replay_after_reversal_same_allocation_refused_too(treasury, registry, crown) -> None:  # noqa: F811
   121	    """نسخةٌ أضعفُ من الهجوم: المبلغُ وحده مغايرٌ والتخصيصُ نفسُه — يُرفَضُ أيضًا."""
   122	    fiscal = _fiscal(treasury, registry, crown, limit_amount="200000", funding="90000")
   123	    alloc = _allocate(treasury, crown, fiscal, amount="30000")
   124	    key = f"{KEY_PREFIX}-mut-{uuid.uuid4().hex[:10]}"
   125	
   126	    posted = treasury.disburse(
   127	        context=crown,
   128	        allocation_id=alloc["id"],
   129	        expense_account_code=fiscal.expense["code"],
   130	        amount="800",
   131	        purpose="صرف سيُعكس ثم تُعاد محاكاته",
   132	        official_id=fiscal.official["id"],
   133	        idempotency_key=key,
   134	    )
   135	    treasury.reverse_transaction(
   136	        context=crown,
   137	        reference=posted["reference"],
   138	        reason="خطأ محاسبي",
   139	        official_id=fiscal.official["id"],
   140	    )
   141	    with pytest.raises(EntityStateError, match="معكوسةٌ"):
   142	        treasury.disburse(
   143	            context=crown,
   144	            allocation_id=alloc["id"],
   145	            expense_account_code=fiscal.expense["code"],
   146	            amount="799.99",
   147	            purpose="صرف سيُعكس ثم تُعاد محاكاته",
   148	            official_id=fiscal.official["id"],
   149	            idempotency_key=key,
   150	        )
   151	    assert _keys_count(key) == 1
   152	    assert _spent(treasury, crown, fiscal.budget["code"]) == "0.0000"
   153	
   154	
   155	def test_honest_replay_of_live_disbursement_stays_idempotent(treasury, registry, crown) -> None:  # noqa: F811
   156	    """الإصلاحُ لا يكسرُ عقدَ عدمِ التكرار: إعادةٌ أمينةٌ لحركةٍ حيّةٍ تعودُ بعينِها."""
   157	    fiscal = _fiscal(treasury, registry, crown, limit_amount="200000", funding="90000")
   158	    alloc = _allocate(treasury, crown, fiscal, amount="30000")
   159	    key = f"{KEY_PREFIX}-ok-{uuid.uuid4().hex[:10]}"
   160	
   161	    def do_disburse() -> dict:
   162	        return treasury.disburse(
   163	            context=crown,
   164	            allocation_id=alloc["id"],
   165	            expense_account_code=fiscal.expense["code"],
   166	            amount="777.25",
   167	            purpose="إعادة أمينة مكررة",
   168	            official_id=fiscal.official["id"],
   169	            idempotency_key=key,
   170	        )
   171	
   172	    first = do_disburse()
   173	    second = do_disburse()
   174	    third = do_disburse()
   175	    assert second["id"] == first["id"] and second.get("idempotent") is True
   176	    assert third["id"] == first["id"] and third.get("idempotent") is True
   177	    assert second["status"] == "posted" and third["status"] == "posted"
   178	    assert _keys_count(key) == 1, "ثلاثُ محاولاتٍ أمينةٍ = حركةٌ واحدة"
   179	    assert _spent(treasury, crown, fiscal.budget["code"]) == "777.2500", (
   180	        "الإعاداتُ لا تضاعفُ المصروف"
   181	    )
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w673/kimi_k3/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/kimi_k3/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider -p tests.conftest /home/user/workspace/council_w673/kimi_k3/wi115/probe/probe_wi115_reversed_replay_kimi.py
EXIT: 0
BYTES: 98
SHA256: 20362a81bf4105ac9b50b20bf0a2d76c76b81572886928ac3f09de5e8026048a
NO_EOL: 0
--- OUTPUT ---
...                                                                      [100%]
3 passed in 1.17s
=== RAW [15] END ===
VERDICT_PER_CRITERION:
 (1) وثيقةُ التصميمِ قبلَ الشِّفرةِ بقياساتٍ مولَّدةٍ بأوامرَ (DISC-136): نعم — RAW [4] يُثبِتُ أنَّ W-665 (5086fb4e · وثيقةُ تصميمِ Q-9 · «لا شِفرةَ») سبقَ W-670 (93434790 · إصلاحُ § 3.5)، وRAW [5] يُظهِرُ الوثيقةَ كاملةً وفي رأسِها: «كلُّ «ملف:سطر» هنا مولَّدٌ بأمرٍ، ومخرجُه ملصقٌ خامًا في docs/audit/evidence/W-665/wi115_design_measurements.txt (DISC-136). والقياسُ على cb728386» — والقياساتُ الملصقةُ في § 1 مقروءةٌ في المخرجِ.
 (2) إصلاحُ § 3.5 — إعادةُ صرفٍ لحركةٍ reversed لا تُعيدُها صامتةً، فحصٌ يسقطُ قبلُ وينجحُ بعدُ: نعم — RAW [6] يُظهِرُ الفرقَ: _existing_idempotent يرفعُ EntityStateError إن كانت الحركةُ بالمفتاحِ نفسِه بحالةِ «reversed»، وRAW [8] يُظهِرُ الشِّفرةَ مثبَّتةً في السطورِ 835–859، وRAW [7] (EXIT 0 · «2 passed») ينجحُ بعدَ الإصلاحِ، وRAW [9] (EXIT 1 · «1 failed, 1 passed» · «DID NOT RAISE EntityStateError») يسقطُ على شجرةِ W-670^ (6605fa88) بالفحصِ نفسِه — سقطَ قبلَ ونجحَ بعدَ.
 (3) الكاشفُ يرفضُ التعشيشَ قبلَ decide وopen_case مستثنًى باسمِه: لا · لم يُنفَّذْ — إفصاحُ المنسِّقِ (1) في الإحاطةِ يُعلِنُ أنَّه لم يُنفَّذْ، وتاريخُ الملفِّ في RAW [4] لا يُظهِرُ أيَّ تسليمٍ للكاشفِ، ووثيقةُ التصميمِ في RAW [5] تضعُه في § 2.2 تصميمًا — ويُحكَمُ عليه «لا · لم يُنفَّذْ» دونَ أن يكونَ ملاحظةً حاجبةً لنطاقِ هذه الجولةِ (§ 3.5 وحدَه).
 (4) المركَّباتُ الثلاثةُ تُعلِنُ الآثارَ وتُنادي نوًى خاصّةً: لا · لم يُنفَّذْ — الإفصاحُ نفسُه (1)، والوثيقةُ في RAW [5] § 2.3 تضعُ الهيكلةَ تصميمًا وتقولُ إنَّ إعلانَ الآثارِ يقعُ مع M1 (D25-3 في RAW [11]: «الكاشف أولًا، ثم M1») — ويُحكَمُ «لا · لم يُنفَّذْ» بلا حجبٍ لهذا النطاقِ.
 (5) طفراتُ حذفِ الكاشفِ وحذفِ إصلاحِ § 3.5 تُكتشَفُ: شقُّ إصلاحِ § 3.5 نعم — أعدتُ الطفرةَ بنفسي في RAW [9] (شجرةُ عملٍ على W-670^ بلا الإصلاحِ: الفحصُ يسقطُ بـ«DID NOT RAISE EntityStateError»، EXIT 1)؛ وشقُّ حذفِ الكاشفِ: لا · لم يُنفَّذْ (لا كاشفَ أصلًا ليُحذَفَ في هذه الجولةِ).
 (6) مسبارٌ لكلِّ مقعدٍ: نعم — مسباري الخاصُّ في RAW [14] (الشِّفرة) وRAW [15] (التشغيل: EXIT 0 · «3 passed»).
PROBES:
 مسبارٌ واحد: probe/probe_wi115_reversed_replay_kimi.py (ثلاثةُ سيناريوهات) — كتلةُ شِفرتِه RAW [14] · كتلةُ تشغيلِه RAW [15] (EXIT 0 · 3 passed) · الخواصُّ التي حاولَ كسرَها: (أ) إعادةٌ مسمومةٌ بمفتاحِ حركةٍ معكوسةٍ بمبلغٍ وغرضٍ وتخصيصٍ مغايرين — يجبُ رفضُها بـEntityStateError بلا حركةٍ جديدةٍ وبلا تغيّرِ رصيدٍ وبقاءِ الأصلِ reversed · (ب) إعادةٌ مغايرةٌ في المبلغِ وحدَه — تُرفَضُ كذلك · (ج) الإعادةُ الأمينةُ المتطابقةُ لحركةٍ حيّةٍ تبقى idempotent=True بالمعرِّفِ نفسِه ولا تُضاعِفُ المصروفَ · انكسرت الخاصيّةُ؟ لا (3 passed على شِفرةِ ما بعدَ W-670) — وتأكيدًا لعدمِ خواءِ المسبارِ شغَّلتُه (تشغيلًا استقصائيًّا غيرَ ملتقَط) على شجرةِ ../old (W-670^) فسقطَ سيناريوها (أ) و(ب) بـ«DID NOT RAISE EntityStateError» ونجحَ (ج) — أي إنَّ المسبارَ يكشفُ طفرةَ حذفِ الإصلاحِ.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — أقرُّ أنّي لم أقرأْ ولم أكتبْ خارجَ جذري /home/user/workspace/council_w673/kimi_k3/wi115/؛ استنسختُ المستودعَ بنفسي إلى repo/ (git clone https://github.com/vooovg-ui/AMOS-Fedration repo) وأعددتُ بيئتَه بـtools/dev/bootstrap.sh وأعدتُ تشغيلَ أوامرِ المعاييرِ كلِّها بنفسي عبرَ أداةِ الالتقاطِ، ولم أقرأْ نسخةَ المنسِّقِ ولا أدلّةَ المنفِّذِ (docs/audit/evidence/W-66*/W-67* عدا هذه الإحاطةِ نفسِها — بصمتُها تحقَّقتُ منها في RAW [12] مقابلَ RAW [13]: efc856e68db9cc688d8980209976c6ea478ffdc52be66625447f38c97fc75eb0 مطابقةٌ لسطر briefing_kimi_k3.md في SHA256SUMS)، واستثناءٌ وحيدٌ تقنيٌّ: مجلَّداتُ temp مؤقَّتةٌ أنشأها حزامُ فحوصِ المستودعِ نفسِه (tests/conftest.py عبرَ tempfile.mkdtemp في /tmp) حينَ شغَّلتُ الفحوصَ والمسبارَ — وهو أثرُ تنفيذِ الأوامرِ المفروضةِ ذاتِها لا قراءةٌ ولا كتابةٌ منّي لملفّاتِ مقعدٍ آخر.
VERDICT: PASS — للنطاقِ المنفَّذِ في هذه الجولةِ وحدَه (§ 3.5: المعيارانِ (1) و(2) وشقُّ § 3.5 من (5) ومسبارُ المقعدِ (6) صادقةٌ مُعادَةُ التشغيلِ بيدي)؛ والمعاييرُ (3) و(4) وشقُّ الكاشفِ من (5) محكومٌ عليها «لا · لم يُنفَّذْ» — فلا VERIFIED للبندِ كلِّه بهذه الجولةِ ويعودُ IN_PROGRESS للكاشفِ.
