# إحاطةُ جولةِ مراجعةِ البندِ: WI-115 (Q-9 الخيارُ 4 — **نطاقُ هذه الجولةِ: إصلاحُ § 3.5 وحدَه**) — مقعدُ gemini_3_8_flash
> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.

> **بنودٌ مساعدةٌ (ملزمةٌ):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** gemini_3_8_flash · grok_4_7 · kimi_k3 — والمنسِّقُ عندَ الإطلاقِ **Claude Opus 5.5** (لا مقعدَ من عائلةِ Claude) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w673/gemini_3_8_flash/wi115` (§ 2.6).
> **سندُ الجولةِ (التوجيهُ 23 § 2):** «WI-113 وWI-115: أدخلهما IN_REVIEW وأطلق لهما جولة مجلس تُجمَع في الجلسة نفسها (Q-72).»
> **تُبصَمُ sha256 في قيدِ W-673 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-673/briefs_wi115/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo`، وأعدَّ بيئتَه بـ`tools/dev/bootstrap.sh` داخلَه، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ في W-673 — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

| WI-115 | federal-executive | T1 (Q-9 بقرارِ المالكِ في التوجيهِ 22 § 1: «يُمنع التعشيش السيادي بكاشف عند الحد، ويُعاد هيكلة مركّبات المال الثلاثة على نمط «الخارجي يُعلن الآثار وينادي نوًى خاصة»، ويُستثنى open_case باسمه استثناءً مسجَّلًا، ويُعالَج خطر إعادة disburse لحركة معكوسة (§3.5) قبل M1» · و§ 2: «كاشف التعشيش + إصلاح §3.5 قبل أي تصميم لـM1») | Perplexity Computer | مجلسُ المراجعةِ (بروتوكولُ المجلسِ · C3 لمساسِه `core/sovereignty`) — ولا VERIFIED بيدِ المنفِّذِ | IN_REVIEW | core/sovereignty/enforcement_boundary.py · federal/executive/services/src/amos_federation/services/state_treasury/service.py · federal/executive/services/src/amos_federation/services/national_economy/service.py · federal/executive/services/src/amos_federation/services/federal_state/service.py · tests/sovereignty/test_wi115_nesting_detector.py · federal/executive/services/tests/test_wi115_reversed_replay.py · docs/audit/Q9_NESTING_DETECTOR_DESIGN.md · docs/audit/evidence/W-665 · docs/audit/evidence/W-670 | 2026-10-25 | 2026-11-22 | لا عائقَ — Q-9 محسومٌ (الخيارُ 4) | جولةُ مجلسٍ على ما نُفِّذَ (§ 3.5 · W-670) ثمَّ IN_REVIEW→IN_PROGRESS لكاشفِ التعشيشِ (D25-3: الكاشفُ أولًا ثمَّ M1) | — (يُكتَبُ عندَ الإغلاقِ) |

كتلةُ البندِ (كما هي عندَ كتابةِ هذهِ الإحاطةِ):

```text
المعرِّف: WI-115
النطاق: T1 (federal-executive + core/sovereignty — C3)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · بتوجيهِ المستشارِ 22 § 2)
المراجع: مجلسُ المراجعةِ (بروتوكولُ المجلسِ · C3) — ولا VERIFIED بيدِ المنفِّذِ
الحالة: IN_REVIEW   (قيدُ W-673 · IN_PROGRESS→IN_REVIEW بأمرِ التوجيهِ 23 § 2 نصًّا: «WI-113 وWI-115: أدخلهما IN_REVIEW وأطلق لهما جولة مجلس» · **نطاقُ الجولةِ ما نُفِّذَ وحدَه**: المعيارانِ (1) و(2) وشقُّ § 3.5 من (5) (W-665 · W-670) — والمعاييرُ (3) و(4) وشقُّ الكاشفِ من (5) لم تُنفَّذْ فلا VERIFIED للبندِ كلِّه بهذه الجولةِ · وبعدَها IN_REVIEW→IN_PROGRESS للكاشفِ («كاشف التعشيش … بعد الجولة») · والإحاطاتُ في evidence/W-673/briefs_wi115 · والسابقُ: W-668 IN_PROGRESS · W-665 RESERVED · W-663 READY)
المسارات: core/sovereignty/enforcement_boundary.py · federal/executive/services/src/amos_federation/services/state_treasury/service.py · federal/executive/services/src/amos_federation/services/national_economy/service.py · federal/executive/services/src/amos_federation/services/federal_state/service.py · tests/sovereignty/test_wi115_nesting_detector.py · federal/executive/services/tests/test_wi115_reversed_replay.py · docs/audit/Q9_NESTING_DETECTOR_DESIGN.md (تسبقُ الشِّفرةَ) · docs/audit/evidence/W-665 · docs/audit/evidence/W-670 · ومجلَّداتُ أدلّةِ قيودِه تُضافُ عندَ حجزِه
بدأ: 2026-10-25 · الأفق: 2026-11-22

السبب: Q9_NESTED_SOVEREIGN_CALL_ANALYSIS: التعشيشُ تقبلُه الآليّةُ اليومَ بلا اعتراضٍ (S7b) · والمركَّباتُ الثلاثةُ (execute_expenditure · execute_transfer · execute_scoped_disbursement) مالٌ ← مالٌ · و`_existing_idempotent` يُعيدُ الحركةَ المطابقةَ أيًّا كانت حالتُها (§ 3.5). والمالكُ: «قبل M1».

خارج النطاق: أيُّ تصميمٍ لـM1 · K1 · تفكيكُ ExecutiveCore.submit/run (2B) · استثناءٌ غيرُ open_case · تخفيفُ أيِّ حارسٍ

معيار القبول: (1) **قبلَ الشِّفرةِ**: وثيقةُ التصميمِ بقياساتٍ مولَّدةٍ بأوامرَ (DISC-136) (2) إصلاحُ § 3.5: إعادةُ صرفٍ لحركةٍ `reversed` لا تُعيدُها صامتةً — فحصٌ يسقطُ قبلُ وينجحُ بعدُ (3) الكاشفُ يرفضُ عبورًا سياديًّا داخلَ عبورٍ نشطٍ قبلَ `decide` · و`open_case` مستثنًى باسمِه استثناءً مسجَّلًا (4) المركَّباتُ الثلاثةُ تُعلِنُ الآثارَ وتُنادي نوًى خاصّةً فلا تُرفَضُ بالكاشفِ (5) طفراتُ حذفِ الكاشفِ وحذفِ إصلاحِ § 3.5 تُكتشَفُ (6) مسبارٌ لكلِّ مقعدٍ

الدليل المطلوب: الوثيقةُ · الفروقُ · الفحوصُ قبلُ/بعدُ · سجلُّ الطفراتِ
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ: (1) **قبلَ الشِّفرةِ**: وثيقةُ التصميمِ بقياساتٍ مولَّدةٍ بأوامرَ (DISC-136) (2) إصلاحُ § 3.5: إعادةُ صرفٍ لحركةٍ `reversed` لا تُعيدُها صامتةً — فحصٌ يسقطُ قبلُ وينجحُ بعدُ (3) الكاشفُ يرفضُ عبورًا سياديًّا داخلَ عبورٍ نشطٍ قبلَ `decide` · و`open_case` مستثنًى باسمِه استثناءً مسجَّلًا (4) المركَّباتُ الثلاثةُ تُعلِنُ الآثارَ وتُنادي نوًى خاصّةً فلا تُرفَضُ بالكاشفِ (5) طفراتُ حذفِ الكاشفِ وحذفِ إصلاحِ § 3.5 تُكتشَفُ (6) مسبارٌ لكلِّ مقعدٍ.

**إفصاحاتُ المنسِّقِ (تُحكَمُ لا تُسلَّمُ):** (1) **نطاقُ الجولةِ جزئيٌّ ومُعلَنٌ:** أُنفِّذَ المعيارانِ (1) و(2) وشقُّ § 3.5 من (5) فقط (W-665 الوثيقةُ · W-670 الشِّفرةُ `9343479073d65f4ceb61d5ba9ba273452651987c`). المعياران (3) و(4) وشقُّ الكاشفِ من (5) **لم تُنفَّذْ** — احكمْ عليها «لا · لم يُنفَّذْ» ولا تُعِدَّها ملاحظةً حاجبةً لهذا النطاقِ؛ وحكمُكَ PASS يعني «النطاقُ المنفَّذُ صادقٌ» لا «البندُ كلُّه» — فلا VERIFIED للبندِ بهذه الجولةِ (يعودُ IN_PROGRESS للكاشفِ). (2) الإصلاحُ: `StateTreasury._existing_idempotent` يرفعُ `EntityStateError` إن كانت الحركةُ بالمفتاحِ نفسِه `reversed` — الأمرانِ 6 و8. (3) **المعيارُ (2) «يسقطُ قبلُ»:** الأمرُ 9 يُشغِّلُ الفحصَ على الخدمةِ قبلَ W-670 في شجرةِ عملٍ منفصلةٍ — يُتوقَّعُ سقوطُه. وطفرةُ حذفِ الإصلاحِ (5) أعِدْها أنتَ (سجلُّ المنفِّذِ ليسَ من حدودِ قراءتِكَ) — والأمرُ 9 هو هذه الطفرةُ عمليًّا (الشِّفرةُ بلا الإصلاحِ). (4) **ما لم يقِسْه المنفِّذُ:** أثرُ `execute_transfer` (مُنادٍ يُعيدُ بـ`trf-{reference}`) على حركةٍ معكوسةٍ بعدَ الإصلاحِ — هل يُعلِّمُ التحويلَ منفَّذًا أم يرفضُ؟ مسبارُكَ مدعوٌّ إليه. (5) **حدودُ العزلِ المعلَنةُ:** المقاعدُ الثلاثةُ تعملُ في صندوقٍ واحدٍ مشتركٍ بجذورٍ منفصلةٍ (`/home/user/workspace/council_w673/<مقعد>/`) — لا تقرأْ ولا تكتبْ خارجَ جذرِكَ، ولا تقرأْ نسخةَ المنسِّقِ (`/home/user/workspace/amos`) ولا أدلّةَ المنفِّذِ (`docs/audit/evidence/W-66*`/`W-67*` عدا هذه الإحاطةِ).

### ج · أوامرُ المعاييرِ

1. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/`
2. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi115/)`
3. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git rev-parse HEAD`
4. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py docs/audit/Q9_NESTING_DETECTOR_DESIGN.md`
5. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && cat docs/audit/Q9_NESTING_DETECTOR_DESIGN.md`
6. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && git diff 9343479073d65f4ceb61d5ba9ba273452651987c^ 9343479073d65f4ceb61d5ba9ba273452651987c -- federal/executive/services/src/amos_federation/services/state_treasury/service.py federal/executive/services/tests/test_wi115_reversed_replay.py`
7. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/federal/executive/services && /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py`
8. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && nl -ba federal/executive/services/src/amos_federation/services/state_treasury/service.py | sed -n '820,880p'`
9. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rm -rf ../old && git worktree add --detach ../old 9343479073d65f4ceb61d5ba9ba273452651987c^ && cp federal/executive/services/tests/test_wi115_reversed_replay.py ../old/federal/executive/services/tests/ && cd ../old/federal/executive/services && PYTHONPATH=src /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_wi115_reversed_replay.py`
10. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rg -n 'def disburse|def reverse|def execute_transfer|_existing_idempotent\(' federal/executive/services/src/amos_federation/services/state_treasury/service.py`
11. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && rg -n 'WI-110|WI-115|D25-3|§ ?3.5' docs/audit/SOVEREIGN_DECISION_REGISTER.md`
12. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && sha256sum docs/audit/evidence/W-673/briefs_wi115/briefing_gemini_3_8_flash.md`
13. `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && cat docs/audit/evidence/W-673/briefs_wi115/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- الشِّفرةُ والفحوصُ والوثائقُ التي تُسمّيها أوامرُ (ج) في استنساخِكَ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w673/gemini_3_8_flash/wi115/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من الفحصِ القائمِ — يُنادي **المسارَ الإنتاجيَّ** (`StateTreasury` في `state_treasury/service.py`: `disburse` ثمَّ عكسُ الحركةِ ثمَّ إعادةُ `disburse` بالمفتاحِ نفسِه، أو `execute_transfer` بـ`reference` نفسِه بعدَ العكسِ، أو إعادةٌ متطابقةٌ لحركةٍ قائمةٍ يجبُ أن تبقى `idempotent=True`) ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** (إعادةٌ تمرُّ صامتةً · رفضٌ يمسُّ الإعادةَ المشروعةَ · حركةٌ جديدةٌ تُنشأُ · رصيدٌ يتغيّرُ). احفظْه في دليلِكَ تحتَ `/home/user/workspace/council_w673/gemini_3_8_flash/wi115/probe/`، واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.
7. بعدَ كتابةِ حكمِكَ شغِّلِ الفاحصَ عليه: `cd /home/user/workspace/council_w673/gemini_3_8_flash/wi115/repo && .venv/bin/python tools/governance/council_verdict_raw_check.py --brief docs/audit/evidence/W-673/briefs_wi115/briefing_gemini_3_8_flash.md --repo . /home/user/workspace/council_w673/gemini_3_8_flash/wi115/VERDICT.md` وألصقْ مخرجَه ورمزَ خروجِه في ردِّكَ (لا في VERDICT.md).

### و · صيغةُ جوابِكَ (يُكتَبُ في `/home/user/workspace/council_w673/gemini_3_8_flash/wi115/VERDICT.md` ويُحفظُ حرفيًّا بلا تحريرٍ)
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
