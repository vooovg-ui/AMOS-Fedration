# حكمُ مقعدِ المجلسِ — grok_4_7 · جولةُ WI-115 (W-683)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-115 (النطاقُ المنفَّذُ: إصلاحُ § 3.5 وحدَه) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذرِهِ الخاصِّ (council_w673/grok_4_7/wi115) — وما بعدَ الفاصلِ أدناه بايتًا ببايتٍ (sha256 `b2cba55f12233dd2bfa5ff771ac976577b6befc2359de3c91a5545ef649277e2`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-115 عندَ العقدةِ `79abc6a2` — إحاطةٌ مبصومةٌ (W-673) ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9) · ومخرجاتُ الفاحصِ المصلَحِ (W-680 · main `76a0e5e4`) مقروءةٌ مقبولةً EXIT 0 (raw_check_outputs.txt في قيدِ W-683).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-683) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5) · والانتقالُ المقرَّرُ حتى معَ النصابِ: IN_REVIEW→IN_PROGRESS لكاشفِ التعشيشِ (D25-3 — كما قُيِّدَ في W-681).

## تاريخ الإنشاء
2026-10-26

## تاريخ آخر تعديل
2026-10-26 (W-683 — القيدُ نفسُه)

---
MODEL: grok_4_7
FAMILY: xAI
RUN_DATE: 2026-10-26 04:10 +00:00
NODE: 79abc6a206000e162689d642d1ebc42af36f445a
CLONE_PATH: /home/user/workspace/council_w673/grok_4_7/wi115/repo
CLONE_COMMAND: gh repo clone vooovg-ui/AMOS-Fedration /home/user/workspace/council_w673/grok_4_7/wi115/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/
 2. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/)
 3. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
 5. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && cat docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
 6. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git diff 9343479073d65f4ceb61d5ba9ba273452651987c^ 9343479073d65f4ceb61d5ba9ba273452651987c -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py
 7. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/grok_4_7/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
 8. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && nl -ba federal/executive/services/src/amos_federation/services/state_treasury/service.py | sed -n '820,880p'
 9. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && rm -rf ../old && git worktree add --detach ../old 9343479073d65f4ceb61d5ba9ba273452651987c^ && cp federal/executive/services/tests/test_wi115_reversed_replay.py ../old/federal/executive/services/tests/ && cd ../old/federal/executive/services && PYTHONPATH=src /home/user/workspace/council_w673/grok_4_7/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
 10. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && rg -n 'def disburse|def reverse|def execute_transfer|_existing_idempotent\(' federal/executive/services/src/amos_federation/services/state_treasury/service.py
 11. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && rg -n 'WI-110|WI-115|D25-3|§ ?3.5' docs/audit/SOVEREIGN_DECISION_REGISTER.md
 12. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && sha256sum docs/audit/evidence/W-673/briefs_wi115/briefing_grok_4_7.md
 13. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && cat docs/audit/evidence/W-673/briefs_wi115/SHA256SUMS
 14. nl -ba /home/user/workspace/council_w673/grok_4_7/wi115/probe/probe_wi115_reversed_callers.py
 15. cd /home/user/workspace/council_w673/grok_4_7/wi115/repo/federal/executive/services && PYTHONPATH=src:. /home/user/workspace/council_w673/grok_4_7/wi115/repo/.venv/bin/python /home/user/workspace/council_w673/grok_4_7/wi115/probe/probe_wi115_reversed_callers.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/)
EXIT: 0
BYTES: 329
SHA256: 820b1154c5055620984fd0bba0e902931b07c236382c0e2d712be5b3ef5bcc27
NO_EOL: 0
--- OUTPUT ---
HEAD is now at 79abc6a2 W-673: WI-113 وWI-115 IN_PROGRESS→IN_REVIEW · ستُّ إحاطاتٍ مبصومةٍ لجولةِ المجلسِ (gemini_3_8_flash · grok_4_7 · kimi_k3) ونصوصُ الإطلاقِ حرفيًّا · WI-115 بنطاقِ § 3.5 وحدَه · لا شِفرةَ — المنسِّقُ Claude Opus 5.5
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: b32953241d3c788043a43be218cfd4f560a44249b0775d821d6c3d669366c808
NO_EOL: 0
--- OUTPUT ---
79abc6a206000e162689d642d1ebc42af36f445a
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && cat docs/audit/Q9_NESTING_DETECTOR_DESIGN.md
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && git diff 9343479073d65f4ceb61d5ba9ba273452651987c^ 9343479073d65f4ceb61d5ba9ba273452651987c -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/grok_4_7/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
EXIT: 0
BYTES: 631
SHA256: 25bd7d7074dcf65ae1125d4d15e0bce62fbd7c03b2a456278e0056281df5921e
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w673/grok_4_7/wi115/repo/federal/executive/services
configfile: pyproject.toml
plugins: asyncio-1.4.1, platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 2 items

tests/test_wi115_reversed_replay.py ..                                   [100%]

============================== 2 passed in 1.31s ===============================
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && nl -ba federal/executive/services/src/amos_federation/services/state_treasury/service.py | sed -n '820,880p'
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && rm -rf ../old && git worktree add --detach ../old 9343479073d65f4ceb61d5ba9ba273452651987c^ && cp federal/executive/services/tests/test_wi115_reversed_replay.py ../old/federal/executive/services/tests/ && cd ../old/federal/executive/services && PYTHONPATH=src /home/user/workspace/council_w673/grok_4_7/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py
EXIT: 1
BYTES: 1575
SHA256: 387b6a318c9f67e8cfde088f7c916dac1ad78b80dd87d473d00528b42d5cff6b
NO_EOL: 0
--- OUTPUT ---
Preparing worktree (detached HEAD 6605fa88)
HEAD is now at 6605fa88 W-669: WI-113 — أداةُ الجردِ تفهرسُ بالاسمِ المؤهَّلِ · تصحيحُ قياسٍ لا حرقٌ: D-4 142→135 (W3 97→90) · فحصٌ (4) وطفرتانِ · اللقطاتُ المحروسةُ مُعادةٌ — المنسِّقُ Claude Opus 5.5
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w673/grok_4_7/wi115/old/federal/executive/services
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
========================= 1 failed, 1 passed in 1.42s ==========================
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && rg -n 'def disburse|def reverse|def execute_transfer|_existing_idempotent\(' federal/executive/services/src/amos_federation/services/state_treasury/service.py
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && rg -n 'WI-110|WI-115|D25-3|§ ?3.5' docs/audit/SOVEREIGN_DECISION_REGISTER.md
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
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && sha256sum docs/audit/evidence/W-673/briefs_wi115/briefing_grok_4_7.md
EXIT: 0
BYTES: 126
SHA256: eff2adcbc39815abd0a524700d1c94a57ca0f8193d329ce50b018ad0f3346bf7
NO_EOL: 0
--- OUTPUT ---
d1f550231cf27baa0f6a85de3a6eb664dc587dc7c6623a6f9dc5755848046c0c  docs/audit/evidence/W-673/briefs_wi115/briefing_grok_4_7.md
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo && cat docs/audit/evidence/W-673/briefs_wi115/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w673/grok_4_7/wi115/probe/probe_wi115_reversed_callers.py
EXIT: 0
BYTES: 22714
SHA256: 09cd2b56fa7cdd4e9bafdd42ca3fe7704b2ab9ab097fee2cd6101164146d47e2
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ مقعدِ grok_4_7 لبندِ WI-115 — شقُّ § 3.5 وحدَه.
     3	
     4	ليسَ نسخةً من tests/test_wi115_reversed_replay.py ولا أمرًا من إحاطةِ (ج).
     5	ينادي المسارَ الإنتاجيَّ ويحاولُ كسرَ الادّعاء:
     6	  إعادةُ صرفٍ لحركةٍ reversed لا تعودُ صامتةً (idempotent=True)،
     7	  ولا تُنشئُ حركةً، ولا تُغيّرُ رصيدًا، ولا تُعلِّمُ تحويلًا منفَّذًا،
     8	  ولا يمسُّ الرفضُ إعادةً مشروعةً لحركةٍ قائمة.
     9	
    10	المساراتُ التي لم يغطِّها الفحصُ القائمُ (صرّحَ أنّه لا يمارسُها):
    11	  * post_funding بعدَ عكسِ حركةِ التمويلِ بالمفتاحِ نفسِه
    12	  * مفتاحُ صرفٍ معكوسٍ يُعادُ عبرَ post_funding (عبورُ الأنواع)
    13	  * execute_transfer الذي ينادي treasury.disburse بمفتاحِ trf-{reference}
    14	    بعدَ عكسِ تلكَ الحركةِ والتحويلُ ما زالَ authorized
    15	    (نافذةُ سقوطٍ بينَ التزامِ الصرفِ وتحديثِ حالةِ التحويل)
    16	"""
    17	
    18	from __future__ import annotations
    19	
    20	import os
    21	import sys
    22	import uuid
    23	from decimal import Decimal
    24	from pathlib import Path
    25	
    26	_SERVICES = Path(
    27	    "/home/user/workspace/council_w673/grok_4_7/wi115/repo/federal/executive/services"
    28	)
    29	sys.path.insert(0, str(_SERVICES))
    30	sys.path.insert(0, str(_SERVICES / "src"))
    31	
    32	import tests.conftest as _conftest  # noqa: E402
    33	
    34	os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = str(
    35	    _conftest._cleanup_test_ledger(_conftest.TEST_ARTIFACT_DIR)
    36	)
    37	_conftest._fresh_test_idempotency_ledger()
    38	
    39	from amos_federation.common.database import (  # noqa: E402
    40	    get_session_factory,
    41	    init_db,
    42	    reset_engine,
    43	)
    44	from amos_federation.services.executive_core.engine import reset_executive_core  # noqa: E402
    45	from amos_federation.services.federal_state.service import reset_federal_state  # noqa: E402
    46	from amos_federation.services.government_services.service import (  # noqa: E402
    47	    reset_government_services,
    48	)
    49	from amos_federation.services.national_economy import EconomicTransferModel  # noqa: E402
    50	from amos_federation.services.national_economy.service import (  # noqa: E402
    51	    EconomicStateError,
    52	    reset_national_economy,
    53	)
    54	from amos_federation.services.national_registry.service import (  # noqa: E402
    55	    get_national_registry,
    56	    reset_national_registry,
    57	)
    58	from amos_federation.services.state_registry.service import (  # noqa: E402
    59	    get_state_registry,
    60	    reset_state_registry,
    61	)
    62	from amos_federation.services.state_treasury.models import TransactionModel  # noqa: E402
    63	from amos_federation.services.state_treasury.service import (  # noqa: E402
    64	    EntityStateError,
    65	    get_state_treasury,
    66	    reset_state_treasury,
    67	)
    68	
    69	import tests.test_r7b_state_treasury as r7b  # noqa: E402
    70	import tests.test_r9_national_economic_state as r9  # noqa: E402
    71	
    72	
    73	def _fresh_db(label: str) -> None:
    74	    """قاعدةُ اختبارٍ جديدة — لا استدعاءً لتجهيزةِ pytest."""
    75	    url = f"sqlite:///{_conftest.TEST_ARTIFACT_DIR / label}.db"
    76	    os.environ["AMOS_DATABASE_URL"] = url
    77	    os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = str(
    78	        _conftest._cleanup_test_ledger(_conftest.TEST_ARTIFACT_DIR)
    79	    )
    80	    _conftest._fresh_test_idempotency_ledger()
    81	    reset_engine()
    82	    init_db()
    83	    reset_executive_core()
    84	    reset_state_registry()
    85	    reset_government_services()
    86	    reset_state_treasury()
    87	    reset_national_registry()
    88	    reset_federal_state()
    89	    reset_national_economy()
    90	    from amos_federation.services.national_registry import service as national_service
    91	
    92	    national_service.reset_registry_authorizer()
    93	
    94	
    95	_fresh_db("probe-boot")
    96	
    97	HELD: list[str] = []
    98	BROKEN: list[str] = []
    99	
   100	
   101	def _say(msg: str) -> None:
   102	    print(msg, flush=True)
   103	
   104	
   105	def _tx_count() -> int:
   106	    session = get_session_factory()()
   107	    try:
   108	        return session.query(TransactionModel).count()
   109	    finally:
   110	        session.close()
   111	
   112	
   113	def _tx_status(reference: str) -> str | None:
   114	    session = get_session_factory()()
   115	    try:
   116	        row = (
   117	            session.query(TransactionModel)
   118	            .filter(TransactionModel.reference == reference)
   119	            .one_or_none()
   120	        )
   121	        return None if row is None else row.status
   122	    finally:
   123	        session.close()
   124	
   125	
   126	def _transfer_row(reference: str) -> tuple[str, str | None]:
   127	    session = get_session_factory()()
   128	    try:
   129	        row = (
   130	            session.query(EconomicTransferModel)
   131	            .filter(EconomicTransferModel.reference == reference)
   132	            .one()
   133	        )
   134	        return row.status, row.transaction_reference
   135	    finally:
   136	        session.close()
   137	
   138	
   139	def _hold(name: str, detail: str) -> None:
   140	    HELD.append(name)
   141	    _say(f"ATTACK {name}: HELD — {detail}")
   142	
   143	
   144	def _break(name: str, detail: str) -> None:
   145	    BROKEN.append(name)
   146	    _say(f"ATTACK {name}: BROKEN — {detail}")
   147	
   148	
   149	def attack_post_funding_reversed_replay(treasury, crown, fiscal) -> None:
   150	    """تمويلٌ ← عكسٌ ← إعادةُ التمويلِ بالمفتاحِ نفسِه وبمبلغٍ مختلف."""
   151	    name = "post_funding_reversed_replay"
   152	    key = f"probe-fund-{uuid.uuid4().hex[:8]}"
   153	    posted = treasury.post_funding(
   154	        context=crown,
   155	        treasury_code=fiscal.treasury["code"],
   156	        cash_account_code=fiscal.cash["code"],
   157	        revenue_account_code=fiscal.revenue["code"],
   158	        amount="4000.0000",
   159	        purpose="تمويلٌ سيُعكَس",
   160	        official_id=fiscal.official["id"],
   161	        idempotency_key=key,
   162	    )
   163	    treasury.reverse_transaction(
   164	        context=crown,
   165	        reference=posted["reference"],
   166	        reason="عكسُ تمويلِ المسبار",
   167	        official_id=fiscal.official["id"],
   168	    )
   169	    assert _tx_status(posted["reference"]) == "reversed", _tx_status(posted["reference"])
   170	    before = _tx_count()
   171	    cash_before = treasury.account_balance(
   172	        context=crown,
   173	        treasury_code=fiscal.treasury["code"],
   174	        account_code=fiscal.cash["code"],
   175	    )
   176	    try:
   177	        replay = treasury.post_funding(
   178	            context=crown,
   179	            treasury_code=fiscal.treasury["code"],
   180	            cash_account_code=fiscal.cash["code"],
   181	            revenue_account_code=fiscal.revenue["code"],
   182	            amount="9000.0000",
   183	            purpose="إعادةٌ صامتةٌ بمبلغٍ أكبر",
   184	            official_id=fiscal.official["id"],
   185	            idempotency_key=key,
   186	        )
   187	    except EntityStateError as exc:
   188	        after = _tx_count()
   189	        cash_after = treasury.account_balance(
   190	            context=crown,
   191	            treasury_code=fiscal.treasury["code"],
   192	            account_code=fiscal.cash["code"],
   193	        )
   194	        if after != before or cash_after != cash_before:
   195	            _break(name, f"رُفِضَ لكنّ الأثرَ تغيّرَ count {before}->{after} cash {cash_before}->{cash_after}")
   196	            return
   197	        _hold(name, f"EntityStateError: {exc}; count={after}; cash={cash_after['balance']}")
   198	        return
   199	    _break(
   200	        name,
   201	        "أُعيدَ التمويلُ المعكوسُ صامتًا "
   202	        f"idempotent={replay.get('idempotent')!r} status={replay.get('status')!r} id={replay.get('id')!r}",
   203	    )
   204	
   205	
   206	def attack_cross_kind_reversed_key(treasury, crown, fiscal, allocation) -> None:
   207	    """مفتاحُ صرفٍ معكوسٍ يُقدَّمُ إلى post_funding — لا يُعادُ صرفٌ كتمويلٍ ناجح."""
   208	    name = "cross_kind_reversed_key"
   209	    key = f"probe-xkind-{uuid.uuid4().hex[:8]}"
   210	    posted = treasury.disburse(
   211	        context=crown,
   212	        allocation_id=allocation["id"],
   213	        expense_account_code=fiscal.expense["code"],
   214	        amount="800.0000",
   215	        purpose="صرفٌ سيُعكَس ثم يُعادُ كتمويل",
   216	        official_id=fiscal.official["id"],
   217	        idempotency_key=key,
   218	    )
   219	    treasury.reverse_transaction(
   220	        context=crown,
   221	        reference=posted["reference"],
   222	        reason="عكسٌ قبلَ عبورِ النوع",
   223	        official_id=fiscal.official["id"],
   224	    )
   225	    before = _tx_count()
   226	    try:
   227	        replay = treasury.post_funding(
   228	            context=crown,
   229	            treasury_code=fiscal.treasury["code"],
   230	            cash_account_code=fiscal.cash["code"],
   231	            revenue_account_code=fiscal.revenue["code"],
   232	            amount="800.0000",
   233	            purpose="تمويلٌ بمفتاحِ الصرفِ المعكوس",
   234	            official_id=fiscal.official["id"],
   235	            idempotency_key=key,
   236	        )
   237	    except EntityStateError as exc:
   238	        if _tx_count() != before:
   239	            _break(name, "الرفضُ أنشأَ حركةً")
   240	            return
   241	        _hold(name, f"EntityStateError عبرَ النوع: {exc}")
   242	        return
   243	    _break(
   244	        name,
   245	        "مفتاحُ الصرفِ المعكوسِ عادَ من post_funding "
   246	        f"idempotent={replay.get('idempotent')!r} kind={replay.get('kind')!r} status={replay.get('status')!r}",
   247	    )
   248	
   249	
   250	def attack_live_replay_different_amount(treasury, crown, fiscal, allocation) -> None:
   251	    """إعادةٌ مشروعةٌ بمبلغٍ وغايةٍ مختلفين — الرفضُ لا يجوزُ أن يمسَّها ولا أن يُنشئَ حركة."""
   252	    name = "live_replay_different_amount"
   253	    key = f"probe-live-{uuid.uuid4().hex[:8]}"
   254	    first = treasury.disburse(
   255	        context=crown,
   256	        allocation_id=allocation["id"],
   257	        expense_account_code=fiscal.expense["code"],
   258	        amount="600.0000",
   259	        purpose="صرفٌ قائم",
   260	        official_id=fiscal.official["id"],
   261	        idempotency_key=key,
   262	    )
   263	    spent_before = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])["spent"]
   264	    before = _tx_count()
   265	    try:
   266	        second = treasury.disburse(
   267	            context=crown,
   268	            allocation_id=allocation["id"],
   269	            expense_account_code=fiscal.expense["code"],
   270	            amount="6000.0000",
   271	            purpose="إعادةٌ مشروعةٌ بمبلغٍ مختلف",
   272	            official_id=fiscal.official["id"],
   273	            idempotency_key=key,
   274	        )
   275	    except EntityStateError as exc:
   276	        _break(name, f"الرفضُ مسَّ إعادةً مشروعةً لحركةٍ غيرِ معكوسة: {exc}")
   277	        return
   278	    spent_after = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])["spent"]
   279	    if second.get("id") != first["id"] or second.get("idempotent") is not True:
   280	        _break(name, f"الإعادةُ المشروعةُ لم تُعِد الحركةَ عينَها: {second.get('id')!r} idempotent={second.get('idempotent')!r}")
   281	        return
   282	    if _tx_count() != before or spent_after != spent_before:
   283	        _break(name, f"الإعادةُ المشروعةُ غيّرت الأثر count {before}->{_tx_count()} spent {spent_before}->{spent_after}")
   284	        return
   285	    if second.get("status") == "reversed":
   286	        _break(name, "الإعادةُ المشروعةُ أعادت حركةً معكوسة")
   287	        return
   288	    _hold(name, f"idempotent=True id={second['id']} spent={spent_after} amount_returned={second.get('amount')!r}")
   289	
   290	
   291	def attack_new_key_after_refusal(treasury, crown, fiscal, allocation) -> None:
   292	    """بعدَ رفضِ المفتاحِ المعكوس، مفتاحٌ جديدٌ يجبُ أن يُصرَف — الرفضُ ليسَ حجبًا شاملًا."""
   293	    name = "new_key_after_refusal"
   294	    dead = f"probe-dead-{uuid.uuid4().hex[:8]}"
   295	    posted = treasury.disburse(
   296	        context=crown,
   297	        allocation_id=allocation["id"],
   298	        expense_account_code=fiscal.expense["code"],
   299	        amount="500.0000",
   300	        purpose="صرفٌ سيُعكَس",
   301	        official_id=fiscal.official["id"],
   302	        idempotency_key=dead,
   303	    )
   304	    treasury.reverse_transaction(
   305	        context=crown,
   306	        reference=posted["reference"],
   307	        reason="عكسٌ قبلَ مفتاحٍ جديد",
   308	        official_id=fiscal.official["id"],
   309	    )
   310	    spent_before = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])["spent"]
   311	    before = _tx_count()
   312	    fresh_key = f"probe-fresh-{uuid.uuid4().hex[:8]}"
   313	    try:
   314	        fresh = treasury.disburse(
   315	            context=crown,
   316	            allocation_id=allocation["id"],
   317	            expense_account_code=fiscal.expense["code"],
   318	            amount="500.0000",
   319	            purpose="صرفٌ جديدٌ بمفتاحٍ جديد",
   320	            official_id=fiscal.official["id"],
   321	            idempotency_key=fresh_key,
   322	        )
   323	    except EntityStateError as exc:
   324	        _break(name, f"الرفضُ حجبَ صرفًا جديدًا بمفتاحٍ جديد: {exc}")
   325	        return
   326	    spent_after = treasury.budget_balance(context=crown, budget_code=fiscal.budget["code"])["spent"]
   327	    if fresh.get("idempotent") is True or fresh.get("id") == posted["id"] or fresh.get("status") == "reversed":
   328	        _break(name, f"المفتاحُ الجديدُ أعادَ الحركةَ المعكوسة: {fresh!r}")
   329	        return
   330	    if _tx_count() != before + 1 or spent_after == spent_before:
   331	        _break(name, f"المفتاحُ الجديدُ لم يُنشئ أثرًا مستقلًّا count {before}->{_tx_count()} spent {spent_before}->{spent_after}")
   332	        return
   333	    _hold(name, f"صرفٌ جديدٌ id={fresh['id']} status={fresh.get('status')!r} spent {spent_before}->{spent_after}")
   334	
   335	
   336	def attack_execute_transfer_on_reversed_key() -> None:
   337	    """execute_transfer بعدَ عكسِ حركةِ trf-{reference} والتحويلُ ما زالَ authorized."""
   338	    name = "execute_transfer_reversed_key"
   339	    _fresh_db("probe-transfer")
   340	
   341	    economy = r9.get_national_economy()
   342	    registry = get_state_registry()
   343	    national = get_national_registry()
   344	    federation = r9.get_federal_state()
   345	    treasury = get_state_treasury()
   346	    crown = r9._context("king", username="probe-crown")
   347	    identity = national.create_identity(context=crown, identity_type="PERSON", label="تاجُ المسبار")
   348	    national.link_principal(context=crown, principal_id=crown.principal_id, identity_id=identity["id"])
   349	
   350	    _federal, (state, _other) = r9._federal_and_states(federation, crown)
   351	    officer = r9._context("royal", username="probe-officer")
   352	    chain = r9._authority_chain(
   353	        registry,
   354	        national,
   355	        federation,
   356	        crown,
   357	        officer,
   358	        government_code=state["code"],
   359	        scope="INSTITUTION",
   360	        operations=("economy.program.create", "economy.grant.authorize", "treasury.disbursement.post"),
   361	        max_amount="10000.0000",
   362	    )
   363	    money = r9._treasury_chain(treasury, crown, chain.institution["code"], chain.official["id"])
   364	    program = r9._program(economy, officer, chain, "INSTITUTION")
   365	    beneficiary = national.create_identity(context=crown, identity_type="PERSON", label="مستفيدُ المسبار")
   366	    transfer = economy.authorize_transfer(
   367	        officer,
   368	        transfer_kind="GRANT",
   369	        program_code=program["code"],
   370	        beneficiary_identity_id=beneficiary["id"],
   371	        allocation_id=money["allocation"]["id"],
   372	        institution_code=chain.institution["code"],
   373	        scope_level="INSTITUTION",
   374	        amount=Decimal("750.2500"),
   375	        purpose="تحويلٌ سيُصادمُ حركةً معكوسة",
   376	    )
   377	    reference = transfer["reference"]
   378	    key = f"trf-{reference}"
   379	    _say(f"TRANSFER reference={reference} status={transfer['status']!r} key={key}")
   380	    if transfer["status"] != "authorized":
   381	        _break(name, f"الإجازةُ لم تبدأ authorized: {transfer['status']!r}")
   382	        return
   383	
   384	    seeded = treasury.disburse(
   385	        context=officer,
   386	        allocation_id=money["allocation"]["id"],
   387	        expense_account_code=money["expense"]["code"],
   388	        amount=transfer["amount"],
   389	        purpose=transfer["purpose"],
   390	        official_id=chain.official["id"],
   391	        idempotency_key=key,
   392	    )
   393	    _say(f"SEEDED disburse id={seeded['id']} status={seeded.get('status')!r} key_hit=trf-{{reference}}")
   394	    treasury.reverse_transaction(
   395	        context=crown,
   396	        reference=seeded["reference"],
   397	        reason="عكسٌ قبلَ إعادةِ execute_transfer",
   398	        official_id=chain.official["id"],
   399	    )
   400	    assert _tx_status(seeded["reference"]) == "reversed"
   401	    status_before, txref_before = _transfer_row(reference)
   402	    before = _tx_count()
   403	    spent_before = treasury.budget_balance(context=crown, budget_code=money["budget"]["code"])["spent"]
   404	    try:
   405	        paid = economy.execute_transfer(
   406	            officer,
   407	            treasury=treasury,
   408	            reference=reference,
   409	            expense_account_code=money["expense"]["code"],
   410	        )
   411	    except EntityStateError as exc:
   412	        status_after, txref_after = _transfer_row(reference)
   413	        spent_after = treasury.budget_balance(context=crown, budget_code=money["budget"]["code"])["spent"]
   414	        after = _tx_count()
   415	        if status_after != "authorized" or txref_after != txref_before or after != before or spent_after != spent_before:
   416	            _break(
   417	                name,
   418	                "رُفِضَ الصرفُ لكنّ التحويلَ أو الرصيدَ تغيّرَ "
   419	                f"status {status_before}->{status_after} txref {txref_before}->{txref_after} "
   420	                f"count {before}->{after} spent {spent_before}->{spent_after}",
   421	            )
   422	            return
   423	        _hold(
   424	            name,
   425	            "execute_transfer رفضَ ولم يُعلِّم التحويلَ منفَّذًا "
   426	            f"({type(exc).__name__}: {exc}); status={status_after}; spent={spent_after}",
   427	        )
   428	        return
   429	    except EconomicStateError as exc:
   430	        _break(name, f"رُفِضَ قبلَ الخزانةِ لا بـEntityStateError — لم يُختبَر الادّعاء: {exc}")
   431	        return
   432	    status_after, txref_after = _transfer_row(reference)
   433	    tx = paid.get("transaction") or {}
   434	    _break(
   435	        name,
   436	        "execute_transfer علّمَ التحويلَ أو أعادَ الحركةَ المعكوسةَ "
   437	        f"transfer_status={paid.get('status')!r} row={status_after!r} "
   438	        f"tx_status={tx.get('status')!r} idempotent={tx.get('idempotent')!r} txref={txref_after!r}",
   439	    )
   440	
   441	
   442	def main() -> int:
   443	    _fresh_db("probe-treasury")
   444	    treasury = get_state_treasury()
   445	    registry = get_state_registry()
   446	    crown = r7b._context("king", username="probe-treasury")
   447	    fiscal = r7b._fiscal(treasury, registry, crown, limit_amount="100000", funding="50000")
   448	    allocation = r7b._allocate(treasury, crown, fiscal, amount="20000")
   449	    _say(f"TREASURY ready code={fiscal.treasury['code']} allocation={allocation['id']}")
   450	
   451	    attack_post_funding_reversed_replay(treasury, crown, fiscal)
   452	    attack_cross_kind_reversed_key(treasury, crown, fiscal, allocation)
   453	    attack_live_replay_different_amount(treasury, crown, fiscal, allocation)
   454	    attack_new_key_after_refusal(treasury, crown, fiscal, allocation)
   455	    attack_execute_transfer_on_reversed_key()
   456	
   457	    _say(f"PROBE_HELD: {len(HELD)}")
   458	    _say(f"PROBE_BROKEN: {len(BROKEN)}")
   459	    if BROKEN:
   460	        _say("PROBE_RESULT: BROKEN")
   461	        return 1
   462	    if len(HELD) < 5:
   463	        _say("PROBE_RESULT: INCOMPLETE")
   464	        return 2
   465	    _say("PROBE_RESULT: HELD")
   466	    return 0
   467	
   468	
   469	if __name__ == "__main__":
   470	    sys.exit(main())
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w673/grok_4_7/wi115/repo/federal/executive/services && PYTHONPATH=src:. /home/user/workspace/council_w673/grok_4_7/wi115/repo/.venv/bin/python /home/user/workspace/council_w673/grok_4_7/wi115/probe/probe_wi115_reversed_callers.py
EXIT: 0
BYTES: 1501
SHA256: c1b5ca377525a093f887fbb44ccc0bf61f227e6d27e5e8a217832b2f5d6c1dd4
NO_EOL: 0
--- OUTPUT ---
TREASURY ready code=TRS-EDB40B16 allocation=alc-bca35024-c2be-463c-a24c-738269ab9963
ATTACK post_funding_reversed_replay: HELD — EntityStateError: الحركةُ بالمفتاحِ 'probe-fund-ef6f961c' معكوسةٌ — لا تُعادُ نجاحًا ولا صرفًا؛ صرفٌ جديدٌ يلزمُه مفتاحٌ جديد; count=3; cash=50000.0000
ATTACK cross_kind_reversed_key: HELD — EntityStateError عبرَ النوع: الحركةُ بالمفتاحِ 'probe-xkind-4f11c742' معكوسةٌ — لا تُعادُ نجاحًا ولا صرفًا؛ صرفٌ جديدٌ يلزمُه مفتاحٌ جديد
ATTACK live_replay_different_amount: HELD — idempotent=True id=tx-09663e6e-c1d6-4be5-b7cf-e3ed6cf93d33 spent=600.0000 amount_returned='600.0000'
ATTACK new_key_after_refusal: HELD — صرفٌ جديدٌ id=tx-a6119d21-5d76-4192-9ea5-06940ca6a757 status='posted' spent 600.0000->1100.0000
TRANSFER reference=TRF-73F660AFF981 status='authorized' key=trf-TRF-73F660AFF981
SEEDED disburse id=tx-ed7efdc5-4cf7-4d03-aa9c-a3708f56fe42 status='posted' key_hit=trf-{reference}
ATTACK execute_transfer_reversed_key: HELD — execute_transfer رفضَ ولم يُعلِّم التحويلَ منفَّذًا (EntityStateError: الحركةُ بالمفتاحِ 'trf-TRF-73F660AFF981' معكوسةٌ — لا تُعادُ نجاحًا ولا صرفًا؛ صرفٌ جديدٌ يلزمُه مفتاحٌ جديد); status=authorized; spent=0.0000
PROBE_HELD: 5
PROBE_BROKEN: 0
PROBE_RESULT: HELD
=== RAW [15] END ===
VERDICT_PER_CRITERION: (1) نعم — الوثيقةُ قبلَ الشِّفرةِ حاضرةٌ في تشغيلِي: RAW 4 يُرتِّبُ 5086fb4e (W-665 · 2026-10-25T08:00:16Z) قبلَ 93434790 (W-670 · 2026-10-25T08:45:43Z)، وRAW 5 (EXIT 0) هو نصُّ docs/audit/Q9_NESTING_DETECTOR_DESIGN.md الذي يُعلِنُ قياساتِ DISC-136 مولَّدةً بأوامرَ (ملف:سطر) وملصقةً في دليلِ W-665. طابقتُ من الشجرةِ ما سمّتْهُ الوثيقةُ لـexecute_transfer (:1710 والنداءُ :1759). لم أُعِدْ توليدَ لصقِ W-665 ولم أفتحْه (مستبعَدٌ من حدودِ القراءة) — والحضورُ والسبقُ مقيسانِ هنا. (2) نعم — RAW 6 وRAW 8: _existing_idempotent يرفعُ EntityStateError إن كانت الحركةُ بالمفتاحِ نفسِه reversed (الأسطرُ 854–858) ولا يُنشئُ حركةً. RAW 7 EXIT 0: الفحصانِ ينجحانِ بعدَ الإصلاحِ (2 passed). RAW 9 EXIT 1: على 6605fa88 (أبُ W-670) يسقطُ test_replay_of_reversed_disbursement_is_refused بـDID NOT RAISE EntityStateError بينما الإعادةُ المشروعةُ تبقى ناجحةً (F.). RAW 15: post_funding بعدَ العكسِ يُرفَضُ ولا يتغيّرُ العددُ ولا النقدُ؛ ومفتاحُ صرفٍ معكوسٍ يُرفَضُ من post_funding؛ وexecute_transfer بمفتاحِ trf-{reference} بعدَ العكسِ يرفعُ EntityStateError ولا يُعلِّمُ التحويلَ executed (يبقى authorized والمصروفُ 0.0000). (3) لا · لم يُنفَّذْ — لا NestedSovereignCallError ولا ContextVar في enforcement_boundary.py ولا خدماتِ المالِ الثلاثة. ليسَ ملاحظةً حاجبةً لهذا النطاقِ. (4) لا · لم يُنفَّذْ — لا _disburse_core، وexecute_transfer ما زالَ ينادي treasury.disburse عندَ :1759. ليسَ ملاحظةً حاجبةً لهذا النطاقِ. (5) شقُّ § 3.5: نعم — طفرةُ الحذفِ هي RAW 9 (الشِّفرةُ بلا الإصلاح) وقد اكتشفَها الفحصُ (EXIT 1). شقُّ الكاشفِ: لا · لم يُنفَّذْ · ليسَ حاجبًا لهذا النطاقِ. (6) نعم — مسبارٌ خاصٌّ على المسارِ الإنتاجيِّ: RAW 14 شِفرتُه وRAW 15 تشغيلُه (EXIT 0 · PROBE_BROKEN: 0 · PROBE_RESULT: HELD).
PROBES: مسبارٌ واحدٌ probe/probe_wi115_reversed_callers.py — كتلةُ الشِّفرةِ 14 · كتلةُ التشغيلِ 15 · الخاصيّةُ التي حاولَ كسرَها: إعادةٌ صامتةٌ لحركةٍ معكوسةٍ (post_funding · عبورُ المفتاحِ إلى نوعٍ آخر · execute_transfer بمفتاحِ trf-{reference} يُعلِّمُ التحويلَ منفَّذًا أو يُنشئُ حركةً أو يُغيّرُ الرصيد) ورفضٌ يمسُّ إعادةً مشروعةً بمبلغٍ مختلفٍ وحجبُ مفتاحٍ جديد. انكسرت؟ لا.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — لم أقرأْ خارجَ استنساخي /home/user/workspace/council_w673/grok_4_7/wi115/repo وهذهِ الإحاطةِ في جذرِ المقعد. لا استثناءَ خارجَ الجذر. داخلَ الاستنساخِ قرأتُ ما سمّتْهُ أوامرُ (ج) وأداتي الالتقاطِ والفاحصِ ومسارَ execute_transfer لكتابةِ المسبارِ الإلزاميِّ. لم أقرأْ مقاعدَ أخرى ولا /home/user/workspace/amos ولا أدلّةَ المنفِّذِ W-66*/W-67* عدا الإحاطةَ المبصومةَ عبرَ الأمرينِ 12 و13. أمرُ الاستنساخِ: gh repo clone vooovg-ui/AMOS-Fedration /home/user/workspace/council_w673/grok_4_7/wi115/repo ثمَّ git checkout لعقدةِ الأمرِ 1، ثمَّ bash tools/dev/bootstrap.sh.
VERDICT: PASS — النطاقُ المنفَّذُ (§ 3.5: المعيارانِ 1 و2 وشقُّ § 3.5 من 5 والمسبارُ 6) صادقٌ لا البندُ كلُّه. المعيارانِ 3 و4 وشقُّ الكاشفِ من 5 لم يُنفَّذا وليسا ملاحظتينِ حاجبتينِ لهذهِ الجولةِ، فلا VERIFIED للبندِ كلِّه.
