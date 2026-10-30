# إحاطةُ جولةِ مراجعةِ البندِ: WI-116 (EXECUTION: استردادُ العالقِ في EXECUTING · D24-R2) — مقعدُ claude_opus_5_5

> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.
> **بنودٌ مساعدةٌ (ملزمة):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** claude_opus_5_5 (عائلةُ Anthropic · Claude) · gemini_4_argon (عائلةُ Google · Gemini) · grok_4_7 (عائلةُ xAI · Grok) — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (عائلةُ GLM — فلا مقعدَ من عائلتِها · § 1.1/Q-60) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w744/claude_opus_5_5/wi116` (§ 2.6).
> **سندُ الجولةِ (توجيهُ المستشارِ 31 § 1 · 2026-10-30):** «أطلق جولة المجلس الواحدة الآن على: WI-114 · WI-116 · WI-120 · WI-123 (وما يلزم من WI-115 إن بقي شقٌّ)، على عقدة مختومة جديدة، وتُجمَع أحكامها في الجلسة نفسها (Q-72).»
> **هذه جولةٌ واحدةٌ** بأربعةِ نطاقاتٍ (WI-114 · WI-116 · WI-120 · WI-123) تُجمَعُ أحكامُها في الجلسةِ نفسِها (Q-72) — وهذه إحاطةُ نطاقِكَ فيها لا جولةً مستقلةً (تسلسلُ الجولاتِ § 8 بندُ 5: جولةٌ واحدةٌ في آنٍ واحدٍ).
> **تشكيلةُ المقاعدِ بقياسِ التوفرِ (§ 1.3):** أولُ ثلاثٍ في الترتيبِ المكتوبِ استجابتْ فعلًا في كتالوجِ المنصةِ عندَ الإطلاقِ (claude_opus_5_5 ثمَّ عائلةُ Gemini ثمَّ grok_4_7) — وانحرافٌ مُقيَّدٌ بسببُهِ: `gemini_3_8_flash` لم يعدْ معروضًا في كتالوجِ المنصةِ اليومَ فمقعدُ عائلةِ Google·Gemini هو `gemini_4_argon` (نفسُ العائلةِ · § 1.3: يُقيَّدُ أيُّ انحرافٍ بسببِهِ) — و`kimi_k3` (الرابعُ في الترتيبِ) لم يُلزَمْ لأنَّ أولَ ثلاثةٍ استجابتْ (سابقةُ تشكيلةِ GLM-المنسِّقِ بمقعدِ Claude: W-521/W-526/W-550/W-732).
> **تُبصَمُ sha256 في قيدِ W-744 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-744/council_briefs/wi116/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُّ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2). وهي **عقدةٌ واحدةٌ مشتركةٌ للنطاقاتِ الأربعةِ** (WI-114 · WI-116 · WI-120 · WI-123).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w744/claude_opus_5_5/wi116/repo`، وأعدَّ بيئتَهُ بـ`tools/dev/bootstrap.sh` داخلَهُ، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)
صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):
- **النطاقُ:** T1 (federal-executive · executive_core — المساراتُ بالتصميمِ)
- **السندُ (D24-R2 حرفيًّا):** «الخيار 1 (max_attempts=1 للنوع EXECUTION) بمعيار قبول صريح: مسلكُ استرداد معلَن للمهمة العالقة في EXECUTING بعد سقوط العامل بين dispatch والتثبيت، ومسبارٌ يُسقط العاملَ هناك. إن تعذّر المعيار عند التصميم يعود السؤال للمالك ولا يُنزَل إلى الخيار 2 بيدك».
- **التنفيذُ (W-718/W-719/W-720):** الأجزاءُ الأربعةُ — (أ) `EXECUTION_MAX_DELIVERY_ATTEMPTS=1` يُحسَبُ من التوقيعِ في `record_result` و`is_claimable` (ب) رفضُ إدراجِ EXECUTION بإقرارِ التفرّدِ وغموضُه بشريٌّ دائمًا (ج) علامةُ `execution_begin` محروسةٌ بمفتاحِ `<id>:execution-begin` قبلَ dispatch وdispatch ثانٍ مرفوضٌ من كلِّ طريقٍ (د) `recover(now=)` يُؤجِّلُ ما عمرُ علامتِه ≤ 30 ث ويُعلِنُ بعدَها `failed · interrupted_execution · dispatched` — ومسبارُ القبولِ الدائمُ 7 passed.

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في كتلةِ البندِ):

> معيار القبول: (1) `max_attempts=1` لنوعِ EXECUTION (2) مسلكُ استردادٍ مُعلَنٌ للمهمّةِ العالقةِ في EXECUTING بعدَ سقوطِ العاملِ بينَ dispatch والتثبيتِ (3) مسبارٌ يُسقِطُ العاملَ هناك ويُثبِتُ المسلكَ (4) إن تعذَّرَ المعيارُ عندَ التصميمِ يعودُ السؤالُ للمالكِ ولا يُنزَلُ إلى الخيارِ 2

خارج النطاق (منعٌ صريح):

> الخيارُ 2 أو أيُّ نزولٍ إليه بيدِ المنفِّذِ · WI-084 (مغلقٌ) · تغييرُ max_attempts لغيرِ EXECUTION

وقد صدرَ قرارُ المالكُ D28 بالجولةِ على الدفعاتِ — والبندُ IN_REVIEW (قيدُ W-731 · H3) والجولةُ مأذونةٌ بتوجيهِ المستشارِ 31.

### ج · أوامرُ المعاييرِ (منَ البندِ نفسِهِ)
1. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/`
2. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/) && git rev-parse HEAD`
3. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && git log --format='%h %cI %s' -6 -- docs/audit/EXECUTION_RECOVERY_DESIGN.md core/sovereignty/outbox.py federal/executive/services/tests/test_execution_recovery.py`
4. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && rg -n 'EXECUTION_MAX_DELIVERY_ATTEMPTS' core/sovereignty/outbox.py`
5. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_execution_recovery.py`
6. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_outbox_execution_attempts.py`
7. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && sed -i 's/EXECUTION_MAX_DELIVERY_ATTEMPTS: Final\[int\] = 1/EXECUTION_MAX_DELIVERY_ATTEMPTS: Final[int] = 2/' core/sovereignty/outbox.py && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_outbox_execution_attempts.py`
8. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && git checkout -- core/sovereignty/outbox.py && git status --porcelain && git diff --stat`
9. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && rg -n 'D24-R2' docs/audit/SOVEREIGN_DECISION_REGISTER.md | head -5`
10. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && sha256sum docs/audit/evidence/W-744/council_briefs/wi116/briefing_claude_opus_5_5.md`
11. `cd /home/user/workspace/council_w744/claude_opus_5_5/wi116/repo && cat docs/audit/evidence/W-744/council_briefs/wi116/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (D24-R2 · Q-16 · D28)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w744/claude_opus_5_5/wi116/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **المسارَ الإنتاجيَّ** ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** في (ب). احفظْه في دليلِكَ تحتَ `/home/user/workspace/council_w744/claude_opus_5_5/wi116/probe/`، واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.

### و · صيغةُ جوابِكَ (يُحفظُ حرفيًّا بلا تحريرٍ)
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
ISOLATION_DECLARATION: <الإقرارُ>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِه (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وحكمُ PASS بلا مسبارٍ خاصٍّ على المسارِ الإنتاجيِّ لا يُحتسَبُ (§ 4.9) · وملفُّ حكمِكَ في دليلِكَ يُحفظُ حرفيًّا في المستودعِ (§ 4.8).
