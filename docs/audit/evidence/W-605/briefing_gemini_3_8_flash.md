# إحاطةُ جولةِ مراجعةِ البندِ WI-105 — جولةُ الدفعةِ بعدَ وصلِ التعويضِ (قرارُ Q-70) — المقعدُ `gemini_3_8_flash`

## الهدف: إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ
## النطاق: جولةُ مراجعةٍ واحدةٌ للبندِ WI-105 (J1 · `issue_ruling` · C3) **على الدفعةِ كلِّها: التصميمُ (وملحقُه § 7) والشِّفرةُ والأدلةُ** (التوجيهُ 18 § 2) · نسخةٌ لكلِّ مقعدٍ لا تختلفُ إلّا في جذرِ الدليلِ واسمِ المقعدِ (§ 2.6) · تُبصَمُ sha256 في قيدِ W-605 قبلَ الإطلاقِ · **المنسِّقُ الحاضرُ عندَ الإطلاقِ Claude Opus 5.5 (عائلةُ Anthropic · Claude)** ⇒ لا مقعدَ من عائلةِ Claude (§ 1.5/§ 1.6) والمقاعدُ بترتيبِ § 1.3: gemini_3_8_flash · grok_4_7 · kimi_k3 · أدلّةُ المقاعدِ `council_w605`
## المالك: بندُ WI-105 (المنسِّقُ لا يُصوِّتُ)
## تاريخ الإنشاء: 2026-10-22
## تاريخ آخر تعديل: 2026-10-22 (W-605)

> معبَّأةٌ منَ البندِ نفسِهِ لا منَ تقريرِ منفِّذٍ · مُبصَمةٌ قبلَ إطلاقِ المقاعدِ · لا تُعدَّلُ بعدَ الإطلاقِ.
> **المخرجاتُ خامٌ كاملةٌ — ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ، مهما طالَ المخرجُ** (البروتوكولُ § 4.5). وحكمُكَ يُفحَصُ آليًّا ولا يُحتسَبُ إن رُفِضَ (§ 4.7). **وحكمُ PASS بلا مسبارٍ خاصٍّ بكَ على المسارِ الإنتاجيِّ لا يُحتسَبُ (§ 4.9).**

## أ · العقدةُ والمستودعُ

- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُّ مراجعتُها: `175054b7d34987a7552512bbe4ba25f2c9a0e927`** — رأسُ main بعدَ دمجِ W-601…W-604 (قياسُ الفجوةِ · ملحقُ التصميمِ § 7 · شِفرةُ الوصلِ وفحوصُها وطفراتُها · الانتقالُ إلى IN_REVIEW). ويُثبِتُها الأمرُ 1.
- **دليلُكَ الخاصُّ (§ 2.6 · لا مسارَ مشتركٌ):** `/home/user/workspace/council_w605/gemini_3_8_flash` — كلُّ ما تكتبُهُ (الاستنساخُ · الملفّاتُ المؤقّتةُ · قاعدةُ البياناتِ · كتلُ RAW · مسبارُكَ · ملفُّ حكمِكَ) داخلَهُ وحدَهُ، **لا تحتَ /tmp** ولا في دليلِ مقعدٍ آخرَ.
- التهيئةُ (قبلَ أوامرِ المعاييرِ · لا تُلتقَطُ):

```text
mkdir -p /home/user/workspace/council_w605/gemini_3_8_flash/tmp /home/user/workspace/council_w605/gemini_3_8_flash/raw /home/user/workspace/council_w605/gemini_3_8_flash/probe
git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w605/gemini_3_8_flash/repo
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && git checkout 175054b7d34987a7552512bbe4ba25f2c9a0e927
```

## ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

المعاييرُ (1)–(6) قُيِّدَت في W-579 قبلَ J1 · والمعيارُ (7) قُيِّدَ في W-602 قبلَ شِفرةِ الوصلِ (الأمرُ 5 يُخرِجُ ترتيبَ الالتزامِ):

```text
معيار القبول: (1) **قبلَ الشِّفرة**: وثيقةُ التصميمِ docs/audit/J1_ISSUE_RULING_DESIGN.md مُلتزَمةٌ في قيدٍ يسبقُ الشِّفرةَ ثمَّ جولةُ مجلسٍ عليها
  ثمَّ موافقةُ المالكِ بنصِّه على نقاطِ الحكمِ D1 · D4 · D6 · D7 (2) rulings.issue_ruling يحملُ guard_declared( بالفعلِ issue_ruling
  وطلبِ اختصاصٍ منَ البياناتِ الحيّةِ ومُعوِّضٍ حقيقيٍّ ومفتاحٍ بجيلِ الإلغاءِ (3) D-4: 183 ← 181 · sovereign 17 ← 18 · أسطحٌ 220 ← 219 [W-588: الصحيحُ 220 ← 220 · DISC-126]
  بالأداةِ نفسِها بلا نموٍّ في غيرِه (4) T1–T7 ناجحةٌ · وطفرةُ حذفِ العبورِ (M1) تُسقِطُ T1 وT2 · وM2–M4 كلٌّ يُسقِطُ فحصَهُ
  (5) test_r7d_federal_judiciary.py وفحوصُ WI-082 بلا تعديلٍ · وحزمُ services خضراءُ في CI مقروءًا (6) مراجعةٌ تُعيدُ التشغيلَ (Q-H)
  (7) [W-602 · قرارُ Q-70 · مكتوبٌ قبلَ الشِّفرةِ · ملحقُ التصميمِ § 7]: التعويضُ الآليُّ موصولٌ في الحدِّ — T6p (J1 الإنتاجيُّ: إسقاطُ mark_succeeded ⇒
  CompensationRequired · state_is_clean · الصفوفُ غائبةٌ · القضيّةُ بحالتِها · الذرّيّةُ FAILED_RETRYABLE · الإعادةُ تنجحُ) · T8 (نظيرُه لـWI-082) ·
  T9 (فشلُ المُعوِّضِ نفسِه ⇒ state_is_clean False · requires_human · FAILED_FINAL · الإعادةُ مرفوضةٌ) · T10 (الحلقةُ الثانيةُ تعكسُ فعلًا) ·
  والطفراتُ M5–M8 كلٌّ يُسقِطُ فحصَه · وفحوصُ tests/sovereignty وtest_2b وWI-082 القائمةُ بلا تعديلٍ · ومسبارُ W-601 بعدَ الوصلِ: المُعوِّضُ يُنادى في السطحَينِ
```

**نطاقُ هذه الجولةِ:** الدفعةُ كلُّها والمعاييرُ (1)–(7). وقرارُ المالكِ **Q-70** (الأمرُ 17 يُخرِجُ نصَّه): الفرعُ الأولُ — إن كانتِ الفجوةُ في الحدِّ نفسِه يُوصَلُ التعويضُ فيه مرّةً لكلِّ الدفعاتِ — والقياسُ قبلَ الوصلِ (الأمرُ 15) وضعَها في الحدِّ. فالمطلوبُ منكَ أن تحكمَ بنفسِكَ على: (أ) هل الموضعُ مقيسٌ قبلَ أيِّ تغييرٍ وهل الوصلُ في ملفِّ الحدِّ وحدَه (الأمرانِ 4 و7)؛ (ب) هل الملحقُ § 7 مُلتزَمٌ قبلَ الشِّفرةِ (الأمرُ 5)؛ (ج) هل T6p/T8/T9/T10 تُثبِتُ الخاصيّةَ على المسارِ الإنتاجيِّ وهل M5–M8 تُسقِطُها (الأمرانِ 10 و16 — ولكَ إعادةُ الطفراتِ بنفسِكَ)؛ (د) هل الحدودُ المعلنةُ (الملحقُ § 7.5 · DISC-129 · الأمرُ 18) صادقةٌ. وموافقةُ المالكِ على D1/D4/D6/D7 صدرتْ (Q-69) فلا تُحاكَمْ هنا. والمعيارُ (5) في شِقِّ CI: حكمُ CI على العقدةِ يقرؤه المنسِّقُ ويُقيِّدُه — احكمْ على شِقِّ «بلا تعديلٍ» بالأمرِ 6 والحزمِ بالأمرِ 13.

## ج · أوامرُ المعاييرِ (كلُّ سطرٍ أمرٌ مكتفٍ بنفسِهِ يُلتقَطُ وحدَهُ)

**طريقةُ التشغيلِ (إلزاميّةٌ · § 4.6):** شغِّلْ كلَّ سطرٍ أدناهُ برقمِهِ n (بترتيبِهِ منَ 1 إلى 21) عبرَ أداةِ الالتقاطِ هكذا — والأمرُ بينَ علامتَي الاقتباسِ **حرفيًّا كما هو في السطرِ نفسِهِ**:

```text
python3 /home/user/workspace/council_w605/gemini_3_8_flash/repo/tools/governance/council_raw_capture.py --n <n> --out /home/user/workspace/council_w605/gemini_3_8_flash/raw/<n بخانتين: 01 02 …>.txt '<الأمرُ>'
```

```bash
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && git rev-parse HEAD
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && bash tools/dev/bootstrap.sh
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && git log --format='%h %cI %s' 8c98ca5..HEAD
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && git diff --stat 8c98ca5 HEAD
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && git log --format='%h %cI %s' -3 -- docs/audit/J1_ISSUE_RULING_DESIGN.md core/sovereignty/enforcement_boundary.py
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && git diff d0932c51 HEAD -- federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py federal/executive/services/tests/test_2b_government_services_sovereign.py tests/sovereignty
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && git diff 8c98ca5 HEAD -- core/sovereignty/enforcement_boundary.py
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && git diff 8c98ca5 HEAD -- federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py -q
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && .venv/bin/python -m pytest tests/sovereignty -q
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w605/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && cat docs/audit/evidence/W-601/test_w601_gap_probe.py docs/audit/evidence/W-601/probe_output_before_fix.txt
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && cat docs/audit/evidence/W-603/mutations_M5_M8_output.txt docs/audit/evidence/W-603/probe_output_after_fix.txt docs/audit/evidence/W-603/measurements.txt
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && rg -n "Q-70" docs/audit/SOVEREIGN_DECISION_REGISTER.md
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && rg -n "DISC-129" docs/governance/work/DISCOVERIES.md
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && .venv/bin/python -m pytest tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q
cd /home/user/workspace/council_w605/gemini_3_8_flash/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
find /home/user/workspace/council_w605/gemini_3_8_flash -maxdepth 1
```

## د · مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9 · التوجيهُ 18 § 3)

اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **المسارَ الإنتاجيَّ** (`FederalJudiciary.issue_ruling` أو `register_identity` بسلطةِ الجسرِ كما في الخدمةِ) ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** في المعيارِ (7): مثلًا فشلٌ بعدَ الالتزامِ في موضعٍ آخرَ · أو فشلٌ بعدَ أثرٍ داخليٍّ ثانٍ · أو إعادةٌ بعدَ تعويضٍ · أو سباقٌ · أو مُعوِّضٌ يفشلُ جزئيًّا — أنتَ تختارُ. احفظْه تحتَ `/home/user/workspace/council_w605/gemini_3_8_flash/probe/` (ولكَ نسخُه مؤقّتًا إلى `/home/user/workspace/council_w605/gemini_3_8_flash/repo/federal/executive/services/tests/` لاستعمالِ المُثبَّتاتِ ثمَّ تشغيلُه من هناك). **واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ** (`nl -ba <المسار>` — الرقمُ التالي بعدَ 21) **وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ** عبرَ الأداةِ نفسِها، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.

## هـ · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)

- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّ WI-105 وكتلتُهُ) · هذهِ الإحاطةُ
- وثيقةُ التصميمِ وملحقُها § 7 · شِفرةُ الحدِّ `core/sovereignty/` · شِفرةُ العبورِ (`federal_judiciary/` · `executive_core/sovereignty_bridge.py` · `executive_core/agent_identity.py`) · الفحوصُ · أدلّةُ `W-601` و`W-603` في استنساخِكَ
- القراراتُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-70 · Q-69) · `docs/governance/COUNCIL_PROTOCOL.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ جولاتٍ سابقةٍ ولا سجلِّ الإكمالِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

## و · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامٍ كاملةٍ ورموزِ خروجٍ)

1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ المعلنةِ؟ أعدِدْ مسارَ استنساخِكَ (والأمرُ 1 يُثبِتُ العقدةَ).
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ**، وضَعْ كتلتَهُ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ** (§ 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ (رقمُ الكتلةِ). وأمامَ موافقةِ المالكِ في (1) اكتبْ «صدرتْ (Q-69) ولا تُحاكَمْ هنا».
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (د):** رقما كتلتَي شِفرتِه وتشغيلِه · الخاصيّةُ التي حاولتَ كسرَها · هل انكسرت؟

## ز · صيغةُ جوابِكَ (ملفُّ الحكمِ يُحفظُ حرفيًّا بلا تحريرٍ · § 4.8)

اكتبْ ملفَّ حكمِكَ في `/home/user/workspace/council_w605/gemini_3_8_flash/VERDICT.md` بهذهِ الصيغةِ — وقسمُ `RAW_OUTPUTS` يُركَّبُ **آليًّا** منْ ملفّاتِ `/home/user/workspace/council_w605/gemini_3_8_flash/raw/*.txt` بترتيبِها (`cat /home/user/workspace/council_w605/gemini_3_8_flash/raw/*.txt`) بلا أيِّ نصٍّ بينها:

```
MODEL: <اسمُ النموذجِ كما أعلنتْهُ المنصةُ>
FAMILY: <العائلةُ>
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: <العقدةُ — منَ الأمرِ 1>
CLONE_PATH: /home/user/workspace/council_w605/gemini_3_8_flash/repo
COMMANDS_RUN:
 1. <الأمرُ 1 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 2. <الأمرُ 2 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 3. <الأمرُ 3 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 4. <الأمرُ 4 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 5. <الأمرُ 5 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 6. <الأمرُ 6 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 7. <الأمرُ 7 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 8. <الأمرُ 8 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 9. <الأمرُ 9 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 10. <الأمرُ 10 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 11. <الأمرُ 11 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 12. <الأمرُ 12 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 13. <الأمرُ 13 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 14. <الأمرُ 14 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 15. <الأمرُ 15 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 16. <الأمرُ 16 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 17. <الأمرُ 17 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 18. <الأمرُ 18 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 19. <الأمرُ 19 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 20. <الأمرُ 20 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 21. <الأمرُ 21 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 22. <أمرُ عرضِ شِفرةِ مسبارِكَ حرفيًّا كما في سطرِ CMD>
 23. <أمرُ تشغيلِ مسبارِكَ حرفيًّا كما في سطرِ CMD>
RAW_OUTPUTS:
<كتلُ RAW كما كتبتْها الأداةُ>
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ برقمِ الكتلةِ — (1) إلى (7)>
PROBES: <لكلِّ مسبارٍ: رقمُ كتلةِ شِفرتِه · رقمُ كتلةِ تشغيلِه · الخاصيّةُ التي حاولَ كسرَها · انكسرت؟ نعم/لا>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرارُ>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

ثمَّ افحصْ ملفَّكَ بنفسِكَ قبلَ التسليمِ (الفاحصُ نفسُهُ الذي يُحتسَبُ بهِ الحكمُ · § 4.7):

```text
python3 /home/user/workspace/council_w605/gemini_3_8_flash/repo/tools/governance/council_verdict_raw_check.py /home/user/workspace/council_w605/gemini_3_8_flash/VERDICT.md --brief /home/user/workspace/council_w605/gemini_3_8_flash/briefing.md --repo /home/user/workspace/council_w605/gemini_3_8_flash/repo
```

(الإحاطةُ نفسُها منسوخةٌ إلى `/home/user/workspace/council_w605/gemini_3_8_flash/briefing.md` قبلَ إطلاقِكَ.) فإن رُفِضَ فأصلحِ **التركيبَ** (لا المخرجَ) وأعِدِ الفحصَ — ولا تُحرِّرْ مخرجًا بيدِكَ أبدًا؛ وإن احتجتَ أعِدِ التقاطَ الأمرِ.

> **تذكيرٌ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · المخرجاتُ خامٌ **كاملةٌ** برموزِ خروجِها (§ 4.5) · الفحصُ الآليُّ (§ 4.7) · الحفظُ الحرفيُّ (§ 4.8) · **وPASS بلا مسبارٍ لا يُحتسَبُ (§ 4.9).**
