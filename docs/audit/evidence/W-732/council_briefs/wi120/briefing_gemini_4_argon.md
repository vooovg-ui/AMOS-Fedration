# إحاطةُ جولةِ مراجعةِ البندِ: WI-120 (عبورُ أسطحِ G1 الحاكمةِ — الدفعاتُ 1–4 · Q-13/Q-14/Q-26/Q-23) — مقعدُ gemini_4_argon

> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.
> **بنودٌ مساعدةٌ (ملزمة):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** claude_opus_5_5 (عائلةُ Anthropic · Claude) · gemini_4_argon (عائلةُ Google · Gemini) · grok_4_7 (عائلةُ xAI · Grok) — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (عائلةُ GLM — فلا مقعدَ من عائلتِها · § 1.1/Q-60) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w732/gemini_4_argon/wi120` (§ 2.6).
> **سندُ الجولةِ (قرارُ المالكِ D28 · التوجيهُ 27 § 1):** «جولة المجلس: أذن بجولة واحدة على دفعات G1 (1–4) وWI-116، بعد اكتمال دفعات الشفرة، تُجمَع أحكامها في الجلسة نفسها (Q-72).» — وأكَّدَ المالكُ الإطلاقَ في الجلسةِ (2026-10-29 · 15:00 +03): «أطلق الجولة الآن».
> **هذه جولةٌ واحدةٌ** بنطاقَينِ (WI-120 · WI-116) تُجمَعُ أحكامُها في الجلسةِ نفسِها (Q-72) — وهذه إحاطةُ نطاقِكَ فيها لا جولةً مستقلةً (تسلسلُ الجولاتِ § 8 بندُ 5: جولةٌ واحدةٌ في آنٍ واحدٍ).
> **تشكيلةُ المقاعدِ بقياسِ التوفرِ (§ 1.3):** أولُ ثلاثٍ في الترتيبِ المكتوبِ استجابتْ فعلًا في كتالوجِ المنصةِ عندَ الإطلاقِ (claude_opus_5_5 ثمَّ عائلةُ Gemini ثمَّ grok_4_7) — وانحرافٌ مُقيَّدٌ بسببِهِ: `gemini_3_8_flash` لم يعدْ معروضًا في كتالوجِ المنصةِ اليومَ فمقعدُ عائلةِ Google·Gemini هو `gemini_4_argon` (نفسُ العائلةِ · § 1.3: يُقيَّدُ أيُّ انحرافٍ بسببِهِ) — و`kimi_k3` (الرابعُ في الترتيبِ) لم يُلزَمْ لأنَّ أولَ ثلاثةٍ استجابتْ.
> **تُبصَمُ sha256 في قيدِ W-732 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-732/council_briefs/wi120/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-732/council_briefs/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2). وهي **عقدةٌ واحدةٌ مشتركةٌ للنطاقَينِ** (WI-120 وWI-116).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w732/gemini_4_argon/wi120/repo`، وأعدَّ بيئتَهُ بـ`tools/dev/bootstrap.sh` داخلَهُ، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)
صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

- **النطاقُ:** T1 (federal-executive · تصميمٌ مودَعٌ ثمَّ شِفرةٌ لاحقةٌ · services/governance/ · 41 سطحًا: expansion (8) · learning_cycle (7) · security (5) · state_runtime (5) · system_life (7) · treasury (9)) — **[تعديلُ المالكِ D28 (W-721): اعتمادُ التصميمِ بتعديلاتٍ ثلاثة: (أ) store_secret/restore_backup دَينٌ · (ب) الخزانةُ التسعةُ وreward_agent إلى M1 (النطاقُ 30 سطحًا: 11 · 8 · 11) · (ج) «المستوى N» = منعٌ عندَ ≥N · جولةٌ واحدةٌ بعدَ دفعاتِ الشِّفرة]**
- **الدفعاتُ الأربعُ المنفَّذةُ:** المعجمُ (W-722) · state_runtime وsystem_life (W-723) · expansion (W-724) · learning_cycle وsecurity (W-728).
- **ملاحظةٌ (Q-80 باقٍ PENDING_OWNER):** الأسطحُ المحتجزةُ (start_training · evaluate_model · store_secret) غيرُ محروسةٍ بقرارِ التصميمِ (D28 (أ)) — احتجازُها مقصودٌ بقرارِ المالكِ لا عيبُ تنفيذٍ، وحكمُها عندَ المالكِ.

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في كتلةِ البندِ · سابقةُ قيدِ W-715):

> معيار القبول: وثيقةُ التصميمِ (G1_GOVERNANCE_CROSSING_DESIGN.md) تُودَعُ في الدفعةِ الورقيّةِ ثمَّ قياسُ sovereign_write_inventory.py بعدَ كلِّ دفعةِ شِفرةٍ (خطُّ الأساسِ 121 · الإسقاطُ 80 — الفرقُ بينَ الإسقاطِ والقياسِ يُقيَّدُ) + فحوصُ الأصنافِ الخمسةِ + طفرةٌ لكلِّ سطحٍ منَ الـ41 + فحوصٌ خاصةٌ بالقراراتِ الأربعةِ (Q-13: مرسومٌ ملكيٌّ · Q-14: أثرٌ مُعلَنٌ + قاطعٌ + self_heal لا يُعيدُ ولايةً عُلِّقَت بقرارٍ · Q-26: معوّضٌ يعيدُ الوكيلَ · Q-23: المعجمُ التشريعيُّ)

خارج النطاق (منعٌ صريح):

> K1 (royal/main.py · restore_agent الملكيُّ · الصفّانِ 24–25) لا يُمَسُّ · لا تعديلَ لمعجمِ الدستورِ في دفعةِ التصميمِ · لا مساسَ بـpersistent.py ولا بتعريفِ D-4 ولا بمعيارِ WI-115 (4) · لا جولةَ مجلسٍ قبلَ قرارِ المالكِ

وقد صدرَ قرارُ المالكِ D28 (التوجيهُ 27 § 1) بالجولةِ بعدَ اكتمالِ الدفعاتِ — فالبندُ الآنَ IN_REVIEW (قيدُ W-730 · H3) والجولةُ مأذونةٌ.

### ج · أوامرُ المعاييرِ (منَ البندِ نفسِهِ)
1. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-732/council_briefs/`
2. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-732/council_briefs/) && git rev-parse HEAD`
3. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && git log --format='%h %cI %s' -8 -- core/constitutional_engine/rules.py federal/executive/services/src/amos_federation/services/governance/ tests/constitutional/test_g1_vocabulary.py`
4. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && ls docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md && rg -n 'Q-13|Q-14|Q-26|Q-23' docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md | head -12`
5. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/constitutional/test_g1_vocabulary.py`
6. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w723_g1_state_runtime_system_life.py`
7. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w724_g1_expansion.py`
8. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w728_g1_learning_security.py`
9. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_q3_branch_declaration_surface.py`
10. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py`
11. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && sed -i 's/"issue_certificate"/"issue_certificate_mutated"/' core/constitutional_engine/rules.py && .venv/bin/python -m pytest -q -p no:cacheprovider tests/constitutional/test_g1_vocabulary.py`
12. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && git checkout -- core/constitutional_engine/rules.py && git status --porcelain && git diff --stat`
13. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && sed -i 's/guard_declared(/guard_declared_mutated(/' federal/executive/services/src/amos_federation/services/governance/learning_cycle.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w728_g1_learning_security.py`
14. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/learning_cycle.py && git status --porcelain`
15. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && rg -n 'Q-13|Q-14|Q-26|Q-23' docs/audit/SOVEREIGN_DECISION_REGISTER.md | head -12`
16. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && sha256sum docs/audit/evidence/W-732/council_briefs/wi120/briefing_gemini_4_argon.md`
17. `cd /home/user/workspace/council_w732/gemini_4_argon/wi120/repo && cat docs/audit/evidence/W-732/council_briefs/wi120/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-13 · Q-14 · Q-26 · Q-23 · D28 لـWI-120 · وD24-R2 لـWI-116)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w732/gemini_4_argon/wi120/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **المسارَ الإنتاجيَّ** ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** في (ب). احفظْه في دليلِكَ تحتَ `/home/user/workspace/council_w732/gemini_4_argon/wi120/probe/`، واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.

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

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وحكمُ PASS بلا مسبارٍ خاصٍّ على المسارِ الإنتاجيِّ لا يُحتسَبُ (§ 4.9) · وملفُّ حكمِكَ في دليلِكَ يُحفظُ حرفيًّا في المستودعِ (§ 4.8).
