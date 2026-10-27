# إحاطةُ جولةِ مراجعةِ البندِ: WI-115 (Q-9 · الخيارُ 4): جولةُ الكاشفِ المنفَّذِ وحدَه — النطاقُ المعلَنُ لا البندُ كلُّه — مقعدُ gemini_3_8_flash
> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.

> **بنودٌ مساعدةٌ (ملزمةٌ):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** gemini_3_8_flash · grok_4_7 · kimi_k3 — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (لا مقعدَ من عائلةِ GLM) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w701/gemini_3_8_flash/wi115` (§ 2.6).
> **سندُ الجولةِ (توجيهُ المستشارِ 25 § 1 · قرارُ المالكِ D27):** «جولة المجلس تُطلَق الآن ولا تنتظر G1: E1 اكتمل 14/14، فلا موجب للتأجيل. تشمل WI-117 وWI-119 وما صار منفَّذًا من WI-115 (الكاشف)، وتُجمَع أحكامها في الجلسة نفسها (Q-72) بمسبار لكل مقعد وأدلة منفصلة.»
> **هذه جولةٌ واحدةٌ** بثلاثةِ نطاقاتٍ (WI-117 · WI-119 · الكاشفُ المنفَّذُ من WI-115) تُجمَعُ أحكامُها في الجلسةِ نفسِها — وهذه إحاطةُ نطاقِكَ فيها لا جولةً مستقلةً (تسلسلُ الجولاتِ § 8 بندُ 5 محفوظٌ: جولةٌ واحدةٌ في آنٍ واحدٍ).
> **تُبصَمُ sha256 في قيدِ W-701 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo`، وأعدَّ بيئتَه بـ`tools/dev/bootstrap.sh` داخلَه، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ في W-701 — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

| WI-115 | federal-executive | T1 (Q-9 بقرارِ المالكِ في التوجيهِ 22 § 1: «يُمنع التعشيش السيادي بكاشف عند الحد، ويُعاد هيكلة مركّبات المال الثلاثة على نمط «الخارجي يُعلن الآثار وينادي نوًى خاصة»، ويُستثنى open_case باسمه استثناءً مسجَّلًا، ويُعالَج خطر إعادة disburse لحركة معكوسة (§3.5) قبل M1» · و§ 2: «كاشف التعشيش + إصلاح §3.5 قبل أي تصميم لـM1») | Perplexity Computer | مجلسُ المراجعةِ (بروتوكولُ المجلسِ · C3 لمساسِه `core/sovereignty`) — ولا VERIFIED بيدِ المنفِّذِ | IN_PROGRESS | core/sovereignty/enforcement_boundary.py · federal/executive/services/src/amos_federation/services/state_treasury/service.py · federal/executive/services/src/amos_federation/services/national_economy/service.py · federal/executive/services/src/amos_federation/services/federal_state/service.py · tests/sovereignty/test_wi115_nesting_detector.py · federal/executive/services/tests/test_wi115_reversed_replay.py · federal/executive/services/tests/test_wi115_nesting_compensator_frame.py · docs/audit/Q9_NESTING_DETECTOR_DESIGN.md · docs/audit/evidence/W-665 · docs/audit/evidence/W-670 · docs/audit/evidence/W-684 · docs/audit/evidence/W-685 · docs/audit/evidence/W-686 | 2026-10-25 | 2026-11-22 | لا عائقَ — Q-9 محسومٌ (الخيارُ 4) | جولةُ المجلسِ على النطاقِ المنفَّذِ (§ 3.5 · W-670) اكتملَت ومعالجتُها في W-684: النصابُ 3/3 PASS ⇒ IN_REVIEW→IN_PROGRESS للكاشفِ (D25-3) لا VERIFIED · والكاشفُ نُفِّذَ في W-685 (المعيارُ (3) وشقُّ الكاشفِ من (5) · 3 طفراتٍ مقتولةٍ · المعوِّضُ داخلَ الإطارِ مقيسًا) · وإصلاحُ lint في CI للمسبارِ في W-686 · والمعيارُ (4) مؤجَّلٌ (تعارضٌ مقيسٌ مع حرسِ Q-32 — عرضٌ على المالكِ/المجلسِ) · وباقي البندِ: جولةُ مجلسٍ جديدةٌ على النطاقِ الجديدِ | قيدُ W-701 — جولةُ المجلسِ على الكاشفِ المنفَّذِ (W-685) فلا VERIFIED للبندِ كلِّهِ بها (المعيارُ (4) مؤجَّلٌ بعرضٍ على المالكِ) |

كتلةُ البندِ (كما هي عندَ كتابةِ هذهِ الإحاطةِ):

```text
المعرِّف: WI-115
النطاق: T1 (federal-executive + core/sovereignty — C3)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ GLM-5.3 — قيدُ W-682 · استلامٌ بالأمرِ الدائمِ)
المراجع: مجلسُ المراجعةِ (بروتوكولُ المجلسِ · C3) — ولا VERIFIED بيدِ المنفِّذِ
الحالة: IN_PROGRESS   (قيدُ W-685 · تنفيذُ الكاشفِ: المعيارُ (3) مُنفَّذٌ (`NESTED_SOVEREIGN_EXEMPTIONS` بأزواجٍ مُجمَّدةٍ · `NestedSovereignCallError` قبلَ أيِّ حارسٍ وأيِّ `decide` وأيِّ قيدٍ · استعادةٌ بالرمزِ في `finally`) وشقُّ الكاشفِ من المعيارِ (5) (3 طفراتٍ مقتولةٍ في قياسٍ خامٍّ) وقياسُ § 4 منَ التصميمِ (المعوِّضُ `task.cancel` يعبرُ داخلَ الإطارِ النشطِ — فحصٌ دائمٌ `test_wi115_nesting_compensator_frame.py`) · **المعيارُ (4) مؤجَّلٌ**: الاستخراجُ `_disburse_core` يكسرُ حرسَ Q-32 القائمَ (مقيسًا) وحسمُ تكييفِ الحرسِ عرضٌ على المالكِ/المجلسِ لا قرارُ منفِّذٍ · والسابقُ: قيدُ W-684 · IN_REVIEW→IN_PROGRESS بمعالجةِ تقريرِ جولةِ المجلسِ المدموجِ: النصابُ 3/3 PASS بلا ملاحظةٍ حاجبةٍ (gemini · grok · kimi — أحكامُها حرفيًّا في قيدِ W-683 · مسبارٌ خاصٌّ لكلِّ مقعدٍ) على **النطاقِ المنفَّذِ وحدَه** (§ 3.5: المعيارانِ (1) و(2) وشقُّ § 3.5 من (5) — W-665 · W-670) — فلا VERIFIED للبندِ كلِّه بهذهِ الجولةِ (المعاييرُ (3) و(4) وشقُّ الكاشفِ من (5) لم تُنفَّذْ) والعودةُ IN_PROGRESS لتنفيذِ الكاشفِ (D25-3: الكاشفُ أولًا ثمَّ M1) · والجولةُ أُطلِقَت في W-682 بالإحاطاتِ المبصومةِ (evidence/W-673/briefs_wi115 · توجيهُ التسلسلِ W-678) · والسابقُ: W-673 IN_REVIEW · W-668 IN_PROGRESS · W-665 RESERVED · W-663 READY)
المسارات: core/sovereignty/enforcement_boundary.py · federal/executive/services/src/amos_federation/services/state_treasury/service.py · federal/executive/services/src/amos_federation/services/national_economy/service.py · federal/executive/services/src/amos_federation/services/federal_state/service.py · tests/sovereignty/test_wi115_nesting_detector.py · federal/executive/services/tests/test_wi115_reversed_replay.py · federal/executive/services/tests/test_wi115_nesting_compensator_frame.py · docs/audit/Q9_NESTING_DETECTOR_DESIGN.md (تسبقُ الشِّفرةَ) · docs/audit/evidence/W-665 · docs/audit/evidence/W-670 · docs/audit/evidence/W-685 · docs/audit/evidence/W-686 · ومجلَّداتُ أدلّةِ قيودِه تُضافُ عندَ حجزِه
بدأ: 2026-10-25 · الأفق: 2026-11-22

السبب: Q9_NESTED_SOVEREIGN_CALL_ANALYSIS: التعشيشُ تقبلُه الآليّةُ اليومَ بلا اعتراضٍ (S7b) · والمركَّباتُ الثلاثةُ (execute_expenditure · execute_transfer · execute_scoped_disbursement) مالٌ ← مالٌ · و`_existing_idempotent` يُعيدُ الحركةَ المطابقةَ أيًّا كانت حالتُها (§ 3.5). والمالكُ: «قبل M1».

خارج النطاق: أيُّ تصميمٍ لـM1 · K1 · تفكيكُ ExecutiveCore.submit/run (2B) · استثناءٌ غيرُ open_case · تخفيفُ أيِّ حارسٍ

معيار القبول: (1) **قبلَ الشِّفرةِ**: وثيقةُ التصميمِ بقياساتٍ مولَّدةٍ بأوامرَ (DISC-136) (2) إصلاحُ § 3.5: إعادةُ صرفٍ لحركةٍ `reversed` لا تُعيدُها صامتةً — فحصٌ يسقطُ قبلُ وينجحُ بعدُ (3) الكاشفُ يرفضُ عبورًا سياديًّا داخلَ عبورٍ نشطٍ قبلَ `decide` · و`open_case` مستثنًى باسمِه استثناءً مسجَّلًا (4) المركَّباتُ الثلاثةُ تُعلِنُ الآثارَ وتُنادي نوًى خاصّةً فلا تُرفَضُ بالكاشفِ (5) طفراتُ حذفِ الكاشفِ وحذفِ إصلاحِ § 3.5 تُكتشَفُ (6) مسبارٌ لكلِّ مقعدٍ

الدليل المطلوب: الوثيقةُ · الفروقُ · الفحوصُ قبلُ/بعدُ · سجلُّ الطفراتِ
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ: **نطاقُ هذهِ الجولةِ:** المعيارُ (3) (الكاشفُ يرفضُ عبورًا سياديًّا داخلَ عبورٍ نشطٍ قبلَ decide · وopen_case مستثنًى باسمِه استثناءً مسجَّلًا) وشقُّ الكاشفِ من المعيارِ (5) (طفرةُ حذفِ الكاشفِ تُكتشَفُ) — **فلا VERIFIED للبندِ كلِّهِ بهذهِ الجولةِ** (المعيارُ (4) مؤجَّلٌ بعرضٍ على المالكِ: الاستخراجُ `_disburse_core` يكسرُ حرسَ Q-32 القائمَ مقيسًا).

**إفصاحاتُ المنسِّقِ (تُحكَمُ لا تُسلَّمُ):** (1) **حدُّ النطاقِ:** الشِّفرةُ في التزامِ `2b814b34` (قيدُ W-685) للكاشفِ وحدَهُ — والمعيارانِ (1) و(2) وشقُّ § 3.5 من (5) عولجتا في جولةٍ سابقةٍ (W-673/W-683) فليستا من نطاقِ حكمِكَ. (2) الشِّفرةُ: `NESTED_SOVEREIGN_EXEMPTIONS` بأزواجٍ مُجمَّدةٍ · `NestedSovereignCallError` يُرمى قبلَ أيِّ حارسٍ وأيِّ decide · استثناءُ open_case باسمِه. (3) **الطفرةُ:** سجلُّ طفراتِ المنفِّذِ ليسَ من حدودِ قراءتِكَ — أعِدِ الطفرةَ بنفسِكَ: الأمرُ 10 (شجرةُ عملٍ عندَ ما قبلَ W-685 + نسخُ فحصِ الكاشفِ — يُتوقَّعُ سقوطُه: احكمْ هل السقوطُ على تأكيدِ الكاشفِ لا على خطأِ استيرادٍ — دليلُ تاريخٍ مكمِّلٌ لا كافٍ وحدَه) — ولمجرّكَ في مسبارِكَ أن تُسقِطَ الكاشفَ في شجرتِكَ وتُشغِّلَ الفحوصَ. (5) **حدودُ العزلِ المعلَنةُ:** المقاعدُ الثلاثةُ تعملُ في صندوقٍ واحدٍ مشتركٍ بجذورٍ منفصلةٍ (`/home/user/workspace/council_w701/<مقعد>/`) — لا تقرأْ ولا تكتبْ خارجَ جذرِكَ، ولا تقرأْ نسخةَ المنسِّقِ (`/home/user/workspace/amos`) ولا أدلّةَ المنفِّذِ (`docs/audit/evidence/W-68*`/`W-69*`/`W-70*` عدا هذه الإحاطةِ).

### ج · أوامرُ المعاييرِ

1. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/`
2. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/)`
3. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git rev-parse HEAD`
4. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git log --format='%h %cI %s' -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py`
5. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git show --stat 2b814b34`
6. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && git diff 2b814b34^ 2b814b34 -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py`
7. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py`
8. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py`
9. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && rg -n "NESTED_SOVEREIGN_EXEMPTIONS|NestedSovereignCallError|open_case" core/sovereignty/enforcement_boundary.py`
10. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && rm -rf ../old && git worktree add --detach ../old 2b814b34^ && cp tests/sovereignty/test_wi115_nesting_detector.py ../old/tests/sovereignty/ && cd ../old && /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py`
11. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && sha256sum docs/audit/evidence/W-701/briefs_wi115/briefing_gemini_3_8_flash.md`
12. `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && cat docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- الشِّفرةُ والفحوصُ والوثائقُ التي تُسمّيها أوامرُ (ج) في استنساخِكَ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w701/gemini_3_8_flash/wi115/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **الكاشفَ نفسَهُ** (`core/sovereignty/enforcement_boundary.py`) ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** (مثلًا: استدعاءٌ سياديٌّ داخلَ عبورٍ نشطٍ بفعلٍ غيرُ مستثنًى — هل يُرمى `NestedSovereignCallError`؟ · استدعاءٌ باسمِ open_case داخلَ عبورٍ — هل يمرُّ بالاستثناءِ المسجَّلِ لا بالرفضِ؟ · زوجٌ مجمَّدٌ في `NESTED_SOVEREIGN_EXEMPTIONS` — هل يمرُّ كما هو؟). احفظْهُ في دليلِكَ تحتَ `/home/user/workspace/council_w701/gemini_3_8_flash/wi115/probe/`، واعرضْ شِفرتَهُ بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْهُ بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ أثبتَ مرورَ تعشيشٍ غيرُ مستثنًى ملاحظةٌ حاجبةٌ.
7. بعدَ كتابةِ حكمِكَ شغِّلِ الفاحصَ عليه: `cd /home/user/workspace/council_w701/gemini_3_8_flash/wi115/repo && .venv/bin/python tools/governance/council_verdict_raw_check.py --brief docs/audit/evidence/W-701/briefs_wi115/briefing_gemini_3_8_flash.md --repo . /home/user/workspace/council_w701/gemini_3_8_flash/wi115/VERDICT.md` وألصقْ مخرجَه ورمزَ خروجِه في ردِّكَ (لا في VERDICT.md).

### و · صيغةُ جوابِكَ (يُكتَبُ في `/home/user/workspace/council_w701/gemini_3_8_flash/wi115/VERDICT.md` ويُحفظُ حرفيًّا بلا تحريرٍ)
```
MODEL: <اسمُ النموذجِ كما أعلنتْهُ المنصةُ>
FAMILY: <العائلةُ>
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: <sha>
CLONE_PATH: <المسارُ>
COMMANDS_RUN:
 1. <الأمرُ حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 2. …
RAW_OUTPUTS:
<كتلُ RAW كما كتبتْها أداةُ الالتقاطِ — متتاليةً بلا أيِّ نصٍّ بينها:>
=== RAW [1] BEGIN ===
CMD: <الأمر>
EXIT: <رمزُ الخروج>
BYTES: <عدد>
SHA256: <بصمة>
NO_EOL: <0|1>
--- OUTPUT ---
<المخرجُ كلُّهُ>
=== RAW [1] END ===
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ>
PROBES: <لكلِّ مسبارٍ: رقمُ كتلةِ شِفرتِه · رقمُ كتلةِ تشغيلِه · الخاصيّةُ التي حاولَ كسرَها · انكسرت؟ نعم/لا>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرار>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتُه (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وحكمُ PASS بلا مسبارٍ خاصٍّ لا يُحتسَبُ (§ 4.9) · وملفُّ حكمِكَ في دليلِكَ يُحفَظُ حرفيًّا في المستودعِ (§ 4.8).
