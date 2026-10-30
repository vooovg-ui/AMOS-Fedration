# إحاطةُ جولةِ مراجعةِ البندِ: WI-123 (Q-81(ب): تحويلُ update_state عبورًا واحدًا بأثرين) — مقعدُ gemini_4_argon

> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.
> **بنودٌ مساعدةٌ (ملزمة):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** claude_opus_5_5 (عائلةُ Anthropic · Claude) · gemini_4_argon (عائلةُ Google · Gemini) · grok_4_7 (عائلةُ xAI · Grok) — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (عائلةُ GLM — فلا مقعدَ من عائلتِها · § 1.1/Q-60) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w744/gemini_4_argon/wi123` (§ 2.6).
> **سندُ الجولةِ (توجيهُ المستشارِ 31 § 1 · 2026-10-30):** «أطلق جولة المجلس الواحدة الآن على: WI-114 · WI-116 · WI-120 · WI-123 (وما يلزم من WI-115 إن بقي شقٌّ)، على عقدة مختومة جديدة، وتُجمَع أحكامها في الجلسة نفسها (Q-72).»
> **هذه جولةٌ واحدةٌ** بأربعةِ نطاقاتٍ (WI-114 · WI-116 · WI-120 · WI-123) تُجمَعُ أحكامُها في الجلسةِ نفسِها (Q-72) — وهذه إحاطةُ نطاقِكَ فيها لا جولةً مستقلةً (تسلسلُ الجولاتِ § 8 بندُ 5: جولةٌ واحدةٌ في آنٍ واحدٍ).
> **تشكيلةُ المقاعدِ بقياسِ التوفرِ (§ 1.3):** أولُ ثلاثٍ في الترتيبِ المكتوبِ استجابتْ فعلًا في كتالوجِ المنصةِ عندَ الإطلاقِ (claude_opus_5_5 ثمَّ عائلةُ Gemini ثمَّ grok_4_7) — وانحرافٌ مُقيَّدٌ بسببُهِ: `gemini_3_8_flash` لم يعدْ معروضًا في كتالوجِ المنصةِ اليومَ فمقعدُ عائلةِ Google·Gemini هو `gemini_4_argon` (نفسُ العائلةِ · § 1.3: يُقيَّدُ أيُّ انحرافٍ بسببِهِ) — و`kimi_k3` (الرابعُ في الترتيبِ) لم يُلزَمْ لأنَّ أولَ ثلاثةٍ استجابتْ (سابقةُ تشكيلةِ GLM-المنسِّقِ بمقعدِ Claude: W-521/W-526/W-550/W-732).
> **تُبصَمُ sha256 في قيدِ W-744 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-744/council_briefs/wi123/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُّ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2). وهي **عقدةٌ واحدةٌ مشتركةٌ للنطاقاتِ الأربعةِ** (WI-114 · WI-116 · WI-120 · WI-123).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w744/gemini_4_argon/wi123/repo`، وأعدَّ بيئتَهُ بـ`tools/dev/bootstrap.sh` داخلَهُ، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)
صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):
- **النطاقُ:** T1 (federal-executive · شِفرةُ agent_runtime/population.py: عبورٌ واحدٌ بأثرينِ (الكانونُ والمرآةُ) بنمطِ § 9.9.8 · وفحوصُ test_w699_agent_runtime_crossing.py)
- **السندُ (قرارُ المالكِ Q-81(ب) حرفيًّا):** «بند فوري يجعل update_state عبورًا واحدًا بأثرين (نمط § 9.9.8)» — سدًّا لنافذةِ DISC-142 (الرفضُ المتأخِّرُ لعبورِ المرآةِ بعدَ نجاحِ العبورِ الكانونيِّ يتركُ الكانونَ منتقلًا).
- **التنفيذُ (W-741):** التصميمُ وُضِعَ في التزامٍ (`E1_UPDATE_STATE_ONE_CROSSING_DESIGN.md` · READY→RESERVED) ثمَّ الشِّفرةُ في التزامٍ: `update_state` عبورٌ واحدٌ بأثرينِ (كانونٌ + مرآةٌ) بمعوِّضٍ لكلِّ أثرٍ وحارسِ استرجاعٍ سطحيٍّ في `except Exception` يعيدُ القيمَ السابقةَ نفسَها ثمَّ يعيدُ رفعَ الانكسار.

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في كتلةِ البندِ):

> معيار القبول: مسبارُ C2 (النصُّ المودَعُ حرفيًّا) قبلَ/بعد — يجب أن يصيرَ broken=0 · طفرةٌ تُسقطُ معوِّضَ الأثرِ الأول فتُثبتُ الحراسةَ · الحزمةُ الكاملةُ خضراءُ · لا واجهةً عامّةً تعبرُ من نوًى خاصّة (فحصُ الأسطحِ)

خارج النطاق (منعٌ صريح):

> K1 (core/) لا يُمَسُّ · معجمُ الدستورِ · سطوحٌ أخرى في population.py · دفعةُ الأسماءِ (Q-77/Q-78/Q-80 — لاحقةً) · M1 · WI-085

والبندُ الآنَ IN_REVIEW (قيدُ W-743 · H3) والجولةُ مأذونةٌ بتوجيهِ المستشارِ 31.

### ج · أوامرُ المعاييرِ (منَ البندِ نفسِهِ)
1. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/`
2. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/) && git rev-parse HEAD`
3. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && git log --format='%h %cI %s' -5 -- docs/audit/E1_UPDATE_STATE_ONE_CROSSING_DESIGN.md federal/executive/services/src/amos_federation/services/agent_runtime/population.py`
4. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && ls docs/audit/E1_UPDATE_STATE_ONE_CROSSING_DESIGN.md && rg -n 'عبور|معوّض|استرجاع' docs/audit/E1_UPDATE_STATE_ONE_CROSSING_DESIGN.md | head -8`
5. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w699_agent_runtime_crossing.py`
6. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && mkdir -p ../c2probe && cp docs/audit/evidence/W-741/raw/g1_probe.py ../c2probe/g1_probe.py && ln -sfn $(pwd) ../c2probe/repo && .venv/bin/python ../c2probe/g1_probe.py`
7. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py`
8. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && sed -i 's/_compensate_canonical_transition(agent_id, str(canonical_previous))/pass  # mutation/' federal/executive/services/src/amos_federation/services/agent_runtime/population.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w699_agent_runtime_crossing.py -k w741`
9. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && git checkout -- federal/executive/services/src/amos_federation/services/agent_runtime/population.py && git status --porcelain && git diff --stat`
10. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && rg -n 'Q-81' docs/audit/SOVEREIGN_DECISION_REGISTER.md | head -6`
11. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && sha256sum docs/audit/evidence/W-744/council_briefs/wi123/briefing_gemini_4_argon.md`
12. `cd /home/user/workspace/council_w744/gemini_4_argon/wi123/repo && cat docs/audit/evidence/W-744/council_briefs/wi123/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-81 · DISC-142 · Q-26)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w744/gemini_4_argon/wi123/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **المسارَ الإنتاجيَّ** ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** في (ب). احفظْه في دليلِكَ تحتَ `/home/user/workspace/council_w744/gemini_4_argon/wi123/probe/`، واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.

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
