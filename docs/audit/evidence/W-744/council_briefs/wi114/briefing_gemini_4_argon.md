# إحاطةُ جولةِ مراجعةِ البندِ: WI-114 (A1(أ): عبورُ أسطحِ canary.py الأربعة — زرُّ التوقّفِ والترقيةُ) — مقعدُ gemini_4_argon

> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.
> **بنودٌ مساعدةٌ (ملزمة):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** claude_opus_5_5 (عائلةُ Anthropic · Claude) · gemini_4_argon (عائلةُ Google · Gemini) · grok_4_7 (عائلةُ xAI · Grok) — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (عائلةُ GLM — فلا مقعدَ من عائلتِها · § 1.1/Q-60) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w744/gemini_4_argon/wi114` (§ 2.6).
> **سندُ الجولةِ (توجيهُ المستشارِ 31 § 1 · 2026-10-30):** «أطلق جولة المجلس الواحدة الآن على: WI-114 · WI-116 · WI-120 · WI-123 (وما يلزم من WI-115 إن بقي شقٌّ)، على عقدة مختومة جديدة، وتُجمَع أحكامها في الجلسة نفسها (Q-72).»
> **هذه جولةٌ واحدةٌ** بأربعةِ نطاقاتٍ (WI-114 · WI-116 · WI-120 · WI-123) تُجمَعُ أحكامُها في الجلسةِ نفسِها (Q-72) — وهذه إحاطةُ نطاقِكَ فيها لا جولةً مستقلةً (تسلسلُ الجولاتِ § 8 بندُ 5: جولةٌ واحدةٌ في آنٍ واحدٍ).
> **تشكيلةُ المقاعدِ بقياسِ التوفرِ (§ 1.3):** أولُ ثلاثٍ في الترتيبِ المكتوبِ استجابتْ فعلًا في كتالوجِ المنصةِ عندَ الإطلاقِ (claude_opus_5_5 ثمَّ عائلةُ Gemini ثمَّ grok_4_7) — وانحرافٌ مُقيَّدٌ بسببُهِ: `gemini_3_8_flash` لم يعدْ معروضًا في كتالوجِ المنصةِ اليومَ فمقعدُ عائلةِ Google·Gemini هو `gemini_4_argon` (نفسُ العائلةِ · § 1.3: يُقيَّدُ أيُّ انحرافٍ بسببِهِ) — و`kimi_k3` (الرابعُ في الترتيبِ) لم يُلزَمْ لأنَّ أولَ ثلاثةٍ استجابتْ (سابقةُ تشكيلةِ GLM-المنسِّقِ بمقعدِ Claude: W-521/W-526/W-550/W-732).
> **تُبصَمُ sha256 في قيدِ W-744 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-744/council_briefs/wi114/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُّ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2). وهي **عقدةٌ واحدةٌ مشتركةٌ للنطاقاتِ الأربعةِ** (WI-114 · WI-116 · WI-120 · WI-123).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w744/gemini_4_argon/wi114/repo`، وأعدَّ بيئتَهُ بـ`tools/dev/bootstrap.sh` داخلَهُ، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)
صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):
- **النطاقُ:** T1 (federal-executive · `governance/canary.py` وفحوصُه ووثيقةُ تصميمِه — الأسطحُ الأربعةُ: 1 و3 (W-675) و2 و4 (W-740))
- **السندُ (قرارُ المالكِ في التوجيهِ 22 § 1):** «(أ) المستدعي في governance/canary.py (زر التوقف lower_kill_switch وpromote_model) أولًا» و§ 2: «وثيقة تصميم في التزام، ثم الشفرة في التزام لاحق، بنمط J1/F1 وفحوص وطفرات ومسبار لكل مقعد».
- **تنفيذُ السطحين 2 و4 (W-740 · بقرارِ D25-1):** `reset_kill_switch` (السطح 2 · lower_kill_switch) و`check_gate` (السطح 4 · promote_model عندَ الانتقالِ إلى promoted) بدليلِ ملكٍ من `require_king` يصلُ الطلبَ عبرَ الجسرِ (`sovereignty_bridge.py` · قناةُ human_approval في `_request` و`guard_declared` و`request_permit` و`review_only` · صنفُ KingApproval موسومٌ بالمصدرِ عبرَ `from_verified_claims` ولا توقيعَ ولا حرجيّةَ من الجسرِ).

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في كتلةِ البندِ):

> معيار القبول: (1) **قبلَ الشِّفرةِ**: وثيقةُ التصميمِ في التزامٍ يسبقُها — وفيها قياسُ `require_auth` على مساراتِ HTTP (ما تفعلُه ومن يملكُ الرمزَ · A1 § 8) وكلُّ ملف:سطرٍ مولَّدٌ بأمرٍ ومخرجُه ملصقٌ (DISC-136) (2) الأسطحُ الأربعةُ تعبرُ الحدَّ بفاعلِ المستدعي وأفعالِ المعجمِ القائمةِ (3) `reset_kill_switch` دونَ موافقةٍ بشريّةٍ يُرفَضُ (4) فحوصٌ وطفراتٌ بنمطِ J1/F1 (حذفُ الحارسِ من كلِّ سطحٍ يُكتشَفُ) (5) مسبارٌ لكلِّ مقعدٍ

خارج النطاق (منعٌ صريح):

> العبورُ في البنيةِ (persistent.py) · فاعلُ بنيةٍ ثابتٌ (مرفوضٌ في § 7) · (ب) و(ج) و(د) من A1 · أفعالٌ جديدةٌ في المعجمِ · تخفيفُ R008

ملاحظتانِ معروضتانِ على الجولةِ (منَ القياسِ · لا يُفترضُ جوابُهما):
- **انحرافٌ مُعلَنٌ عن حرفيّةِ § 7.4 (W-740 · Q-84):** هدفُ الطلبِ والأثرِ للسطحِ 4 هوَ **البوّابةُ داخلَ الترقيةِ** (`governance/promotions/<id>/gates/<gate>`) لا الترقيةُ العاريةُ — بصمةُ الطلبِ تُحسَبُ من الفعلِ والهدفِ فبدونَ تمييزِ البوّابةِ تشتركُ بواباتُ الترقيةِ الواحدةِ في بصمةٍ واحدةٍ ويُرفضُ الثاني كإعادةِ تصريحٍ (مقيسٌ: `PermitReplayError`). حكمُ الجولةِ على هذا الانحرافِ يُسجَّلُ حرفيًّا.
- **Q-82 (حرجيّةُ promote_model):** توصيةُ التصميمِ إبقاؤُها `normal` في هذه الدفعةِ (§ 7.7) — قرارُها للمالكِ.

### ج · أوامرُ المعاييرِ (منَ البندِ نفسِهِ)
1. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/`
2. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-744/council_briefs/) && git rev-parse HEAD`
3. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && git log --format='%h %cI %s' -6 -- docs/audit/A1A_CANARY_CROSSING_DESIGN.md federal/executive/services/src/amos_federation/services/governance/canary.py`
4. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && ls docs/audit/A1A_CANARY_CROSSING_DESIGN.md && rg -n 'require_king|human_approval|عبور' docs/audit/A1A_CANARY_CROSSING_DESIGN.md | head -10`
5. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi114_canary_sovereign.py`
6. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && rg -c 'reset_kill_switch\(\)' federal/executive/services/tests; echo "rg_exit=$? (1 = لا مواضع نداءٍ عارية)"`
7. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_q3_branch_declaration_surface.py`
8. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py`
9. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && sed -i 's/human_approval=approval,/human_approval=None,/' federal/executive/services/src/amos_federation/services/governance/canary.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi114_canary_sovereign.py`
10. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/canary.py && git status --porcelain && git diff --stat`
11. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && rg -n 'D25-1|Q-84|Q-82' docs/audit/SOVEREIGN_DECISION_REGISTER.md | head -8`
12. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && sha256sum docs/audit/evidence/W-744/council_briefs/wi114/briefing_gemini_4_argon.md`
13. `cd /home/user/workspace/council_w744/gemini_4_argon/wi114/repo && cat docs/audit/evidence/W-744/council_briefs/wi114/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-15 · D25-1 · D25-2 · Q-82 · Q-84)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w744/gemini_4_argon/wi114/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **المسارَ الإنتاجيَّ** ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** في (ب). احفظْه في دليلِكَ تحتَ `/home/user/workspace/council_w744/gemini_4_argon/wi114/probe/`، واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.

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
