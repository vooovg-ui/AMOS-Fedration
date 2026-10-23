# إحاطةُ جولةِ مراجعةِ البندِ WI-106 — الدفعةُ F1 (`governance/federation.py` بالفعلِ `coordinate`) — المقعدُ `gemini_3_8_flash`

## الهدف: إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ
## النطاق: جولةُ مراجعةٍ واحدةٌ للبندِ WI-106 (F1 · D17-1 · التوجيهُ 19 § 2) **على الدفعةِ كلِّها: ملحقُ التصميمِ والشِّفرةُ والفحوصُ والطفراتُ والقياسُ** · نسخةٌ لكلِّ مقعدٍ لا تختلفُ إلّا في جذرِ الدليلِ واسمِ المقعدِ (§ 2.6) · تُبصَمُ sha256 في قيدَي W-618/W-620 قبلَ الإطلاقِ · **المنسِّقُ الحاضرُ عندَ الإطلاقِ GLM-5.3** ⇒ لا مقعدَ من عائلةِ GLM (§ 1.5/§ 1.6) — والمقاعدُ الثلاثةُ لا تضمُّ GLM ولا Claude والمقاعدُ بترتيبِ § 1.3: gemini_3_8_flash · grok_4_7 · kimi_k3 · أدلّةُ المقاعدِ `council_w620`
## المالك: بندُ WI-106 (المنسِّقُ لا يُصوِّتُ)
## تاريخ الإنشاء: 2026-10-22
## تاريخ آخر تعديل: 2026-10-23 (W-621 — تصحيحٌ ثانٍ مؤرَّخٌ قبلَ الإطلاقِ: العقدةُ `8cd2f56` حيثُ الإحاطاتُ المُصحَّحةُ وبصماتُها · وتصحيحُ «W-15» إلى «W-615» · ووقبله W-620 ثم W-618)

> معبَّأةٌ منَ البندِ نفسِهِ لا منَ تقريرِ منفِّذٍ · مُبصَمةٌ قبلَ إطلاقِ المقاعدِ · لا تُعدَّلُ بعدَ الإطلاقِ.
> **إضافةٌ مؤرَّخةٌ (W-620 · 2026-10-22 · قبلَ الإطلاقِ — لم تُطلَقِ الجولةُ بعدُ · سابقةُ W-596/W-598):**
> (1) **تصحيحُ العقدةِ**: العقدةُ المُعتمدةُ للمراجعةِ صارت `8cd2f56d181648dad6f2d7ac6191536ae64bdf12` — رأسِ main بعدَ التقديمِ السريعِ للدفعةِ (296a276 → 80e4394 · مقيسًا بـ`git ls-remote`) — وهي تشملُ فوقَ `fd6c1af` قيدَ W-618 (إحاطاتٌ لا شِفرةَ) وقيدَ W-619 (تصحيحُ lint في مسبارِ W-615 · لا شِفرةَ إنتاجيّةً) **وفرقُ الشِفرةِ بينَ العقدتَينِ فارغٌ مقيسًا** (`git diff --stat fd6c1af 80e4394 -- federal/ tools/ tests/ agents/ core/ src/` ⇒ صفرُ ملفاتٍ · والفرقُ الكاملُ 20 ملفًا توثيقًا وحدَها · الدليلُ في `evidence/W-620`) — فالشِّفرةُ المحكومةُ لم تتغير.
> (2) **جذرُ الدليلِ**: تغيَّرَ إلى `council_w620/<seat>` (جذورٌ فريدةٌ § 2.6) والبصمةُ تُعادُ في قيدِ W-620 (البصمةُ القديمةُ في تاريخِ الملفِّ لا تُمحى).
> (3) **المنسِّقُ عندَ الإطلاقِ GLM-5.3** ⇒ لا مقعدَ من عائلةِ GLM — والمقاعدُ الثلاثةُ (gemini_3_8_flash · grok_4_7 · kimi_k3) لا تضمُّ GLM ولا Claude فتبقى سليمةً تحتَ أيٍّ منَ المنسِّقَينِ.
> **إضافةٌ مؤرَّخةٌ ثانيةٌ (W-621 · 2026-10-23 · قبلَ الإطلاقِ — الجولةُ لم تُطلَقْ بعدُ):**
> (1) **تصحيحُ عقدةِ الإحاطةِ المُصحَّحةِ نفسِها**: الإحاطاتُ المُصحَّحةُ وبصماتُها الجديدةُ موجودةٌ في الشجرةِ عندَ `8cd2f56` (رأسِ main بعدَ دمجِ قيدِ W-620) لا عندَ `80e4394` — فالمقعدُ الذي يستنسخُ `80e4394` يجدُ الإحاطاتِ القديمةَ (نسخةَ W-618) وبصماتِها القديمةَ فيفشلُ تحققُ البصمةِ. **فالعقدةُ المعيَّنةُ لهذهِ الجولةِ هي `8cd2f56`** — وفرقُ الشِّفرةِ بينَ `80e4394` و`8cd2f56` فارغٌ مقيسًا على مساراتِ الشِّفرةِ الستِّ (`git diff --stat 80e4394 8cd2f56 -- federal/ tools/ tests/ agents/ core/ src/` ⇒ صفرُ ملفاتٍ · الكاملُ 17 ملفًا توثيقًا وحدَه: قيدُ W-620) — فالشِّفرةُ المحكومةُ لم تتغير.
> (2) **تصحيحُ خطأٍ مطبعيٍّ** في الإضافةِ الأولى: «مسبارِ W-15» صوابُه «مسبارِ W-615».

> **المخرجاتُ خامٌ كاملةٌ — ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ، مهما طالَ المخرجُ** (البروتوكولُ § 4.5). وحكمُكَ يُفحَصُ آليًّا ولا يُحتسَبُ إن رُفِضَ (§ 4.7). **وحكمُ PASS بلا مسبارٍ خاصٍّ بكَ على المسارِ الإنتاجيِّ لا يُحتسَبُ (§ 4.9).**

## أ · العقدةُ والمستودعُ

- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُّ مراجعتُها: `8cd2f56d181648dad6f2d7ac6191536ae64bdf12`** — رأسُ `main` بعدَ التقديمِ السريعِ للدفعةِ (يشملُ فوقَ `fd6c1af` قيدَي W-618 وW-619 — توثيقٌ وتصحيحُ lint لا شِفرةَ · فرقُ الشِفرةِ فارغٌ مقيسًا). ويُثبِتُها الأمرُ 1.
- **دليلُكَ الخاصُّ (§ 2.6 · لا مسارَ مشتركٌ):** `/home/user/workspace/council_w620/gemini_3_8_flash` — كلُّ ما تكتبُهُ (الاستنساخُ · الملفّاتُ المؤقّتةُ · قاعدةُ البياناتِ · كتلُ RAW · مسبارُكَ · ملفُّ حكمِكَ) داخلَهُ وحدَهُ، **لا تحتَ /tmp** ولا في دليلِ مقعدٍ آخرَ.
- التهيئةُ (قبلَ أوامرِ المعاييرِ · لا تُلتقَطُ):

```text
mkdir -p /home/user/workspace/council_w620/gemini_3_8_flash/tmp /home/user/workspace/council_w620/gemini_3_8_flash/raw /home/user/workspace/council_w620/gemini_3_8_flash/probe
git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w620/gemini_3_8_flash/repo
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && git checkout 8cd2f56d181648dad6f2d7ac6191536ae64bdf12
```

## ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ · قيدُ W-613)

```text
معيار القبول: (1) **قبلَ الشِّفرة**: ملحقُ التصميمِ docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md في التزامٍ مستقلٍّ يسبقُ الشِّفرةَ (Q-61)
  (2) الأسطحُ الخمسةَ عشرَ كلٌّ يحملُ guard_declared( بالفعلِ coordinate وفاعلٍ تنفيذيٍّ مُعلَنٍ ومُعوِّضٍ حقيقيٍّ ومفتاحِ عمليّةٍ
  (3) D-4: 181 ← 166 · sovereign 18 ← 33 بالأداةِ نفسِها بلا نموٍّ في غيرِ الوحدةِ (والأسطحُ تُعلَنُ قبلُ/بعدُ بسببِها)
  (4) فحوصُ البندِ ناجحةٌ وكلُّ طفرةٍ مُعلَنةٍ في التصميمِ تُسقِطُ فحصَها (5) test_federation.py بلا تعديلٍ وحزمُ services خضراءُ في CI مقروءًا
  (6) مراجعةٌ تُعيدُ التشغيلَ بمسبارِ كلِّ مقعدٍ (Q-H · § 4.9)
```

**نطاقُ هذه الجولةِ:** الدفعةُ كلُّها والمعاييرُ (1)–(6). المطلوبُ أن تحكمَ بنفسِكَ على: (أ) هل الملحقُ مُلتزَمٌ قبلَ الشِّفرةِ (الأمرُ 5)؛ (ب) هل كلُّ سطحٍ عامٍّ منَ الخمسةَ عشرَ يعبرُ الحدَّ بالفعلِ `coordinate` والفاعلِ `EXECUTIVE` بمُعوِّضٍ يعكسُ فعلًا ومفتاحِ إعادةٍ (الأوامرُ 7 و8 و15)؛ (ج) هل الدَّينُ 181 ← 166 والعابرةُ 18 ← 33 مقيسانِ بالأداةِ وأنَّ نموَّ المواضعِ 220 ← 236 داخلَ الوحدةِ وحدَها (الأمرانِ 9 و15)؛ (د) هل الطفراتُ M1–M5 تُسقِطُ فحوصَها (الأمرانِ 16 و17 — ولكَ إعادتُها بنفسِكَ)؛ (هـ) هل الحدودُ المعلنةُ صادقةٌ: الملحقُ كتبَ نوعَ الأثرِ UPDATE والمعجمُ لا يعرفُه فاستُعمِلَ WRITE · ونداءُ `enact` الثاني يُرفَضُ بـ`FederationReplayError` تغيُّرًا معلنًا. والمعيارُ (5) في شِقِّ CI: حكمُ CI على العقدةِ يقرؤه المنسِّقُ ويُقيِّدُه — احكمْ على شِقِّ «بلا تعديلٍ» بالأمرِ 6 والحزمِ بالأمرِ 13.

## ج · أوامرُ المعاييرِ (كلُّ سطرٍ أمرٌ مكتفٍ بنفسِهِ يُلتقَطُ وحدَهُ)

**طريقةُ التشغيلِ (إلزاميّةٌ · § 4.6):** شغِّلْ كلَّ سطرٍ أدناهُ برقمِهِ n (بترتيبِهِ منَ 1 إلى 21) عبرَ أداةِ الالتقاطِ هكذا — والأمرُ بينَ علامتَي الاقتباسِ **حرفيًّا كما هو في السطرِ نفسِهِ**:

```text
python3 /home/user/workspace/council_w620/gemini_3_8_flash/repo/tools/governance/council_raw_capture.py --n <n> --out /home/user/workspace/council_w620/gemini_3_8_flash/raw/<n بخانتين: 01 02 …>.txt '<الأمرُ>'
```

```bash
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && git rev-parse HEAD
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && bash tools/dev/bootstrap.sh
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && git log --format='%h %cI %s' 5a7520c..HEAD
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && git diff --stat 5a7520c HEAD
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && git log --format='%h %cI %s' -3 -- docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md federal/executive/services/src/amos_federation/services/governance/federation.py
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && git diff 5a7520c HEAD -- federal/executive/services/tests/test_federation.py tests/sovereignty core/sovereignty
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && git diff 5a7520c HEAD -- federal/executive/services/src/amos_federation/services/governance/federation.py
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && cat federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py -q
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_federation.py -q
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && .venv/bin/python -m pytest tests/sovereignty -q
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && cat docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && cat docs/audit/evidence/W-615/federation_sites_before.txt docs/audit/evidence/W-617/federation_sites_after.txt
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && cat docs/audit/evidence/W-617/mutation_probe_wi106.py docs/audit/evidence/W-617/mutation_probe_wi106.out.txt
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w620/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python docs/audit/evidence/W-617/mutation_probe_wi106.py
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && rg -n "D17-1|Q-61" docs/audit/SOVEREIGN_DECISION_REGISTER.md
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q
cd /home/user/workspace/council_w620/gemini_3_8_flash/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
find /home/user/workspace/council_w620/gemini_3_8_flash -maxdepth 1
```

## د · مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9 · التوجيهُ 19 § 2)

اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **المسارَ الإنتاجيَّ** (أسطحُ `governance/federation.py` العامّةُ كما تُنادى في الخدمةِ) ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** في المعيارِ (2): مثلًا سطحٌ يكتبُ بلا عبورٍ · أو فاعلٌ غيرُ تنفيذيٍّ يمرُّ · أو فشلٌ بعدَ الأثرِ لا يُعوَّضُ كاملًا · أو إعادةٌ بالمفتاحِ نفسِه تُكرِّرُ الأثرَ · أو تسلسلٌ (propose ⇒ vote ⇒ enact) يتركُ حالًا وسطًا — أنتَ تختارُ. احفظْه تحتَ `/home/user/workspace/council_w620/gemini_3_8_flash/probe/` (ولكَ نسخُه مؤقّتًا إلى `/home/user/workspace/council_w620/gemini_3_8_flash/repo/federal/executive/services/tests/` لاستعمالِ المُثبَّتاتِ ثمَّ تشغيلُه من هناك). **واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ** (`nl -ba <المسار>` — الرقمُ التالي بعدَ 21) **وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ** عبرَ الأداةِ نفسِها، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.

## هـ · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)

- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّ WI-106 وكتلتُهُ) · هذهِ الإحاطةُ
- ملحقُ التصميمِ · شِفرةُ `governance/federation.py` · شِفرةُ الحدِّ `core/sovereignty/` · الفحوصُ · أدلّةُ `W-615` و`W-617` في استنساخِكَ
- القراراتُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (D17-1 · Q-61) · `docs/governance/COUNCIL_PROTOCOL.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ جولاتٍ سابقةٍ ولا سجلِّ الإكمالِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

## و · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامٍ كاملةٍ ورموزِ خروجٍ)

1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ المعلنةِ؟ أعدِدْ مسارَ استنساخِكَ (والأمرُ 1 يُثبِتُ العقدةَ).
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ**، وضَعْ كتلتَهُ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ** (§ 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ (رقمُ الكتلةِ). وأمامَ شِقِّ CI في (5) اكتبْ «يقرؤه المنسِّقُ ويُقيِّدُه».
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (د):** رقما كتلتَي شِفرتِه وتشغيلِه · الخاصيّةُ التي حاولتَ كسرَها · هل انكسرت؟

## ز · صيغةُ جوابِكَ (ملفُّ الحكمِ يُحفظُ حرفيًّا بلا تحريرٍ · § 4.8)

اكتبْ ملفَّ حكمِكَ في `/home/user/workspace/council_w620/gemini_3_8_flash/VERDICT.md` بهذهِ الصيغةِ — وقسمُ `RAW_OUTPUTS` يُركَّبُ **آليًّا** منْ ملفّاتِ `/home/user/workspace/council_w620/gemini_3_8_flash/raw/*.txt` بترتيبِها (`cat /home/user/workspace/council_w620/gemini_3_8_flash/raw/*.txt`) بلا أيِّ نصٍّ بينها:

```
MODEL: <اسمُ النموذجِ كما أعلنتْهُ المنصةُ>
FAMILY: <العائلةُ>
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: <العقدةُ — منَ الأمرِ 1>
CLONE_PATH: /home/user/workspace/council_w620/gemini_3_8_flash/repo
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
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ برقمِ الكتلةِ — (1) إلى (6)>
PROBES: <لكلِّ مسبارٍ: رقمُ كتلةِ شِفرتِه · رقمُ كتلةِ تشغيلِه · الخاصيّةُ التي حاولَ كسرَها · انكسرت؟ نعم/لا>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرارُ>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

ثمَّ افحصْ ملفَّكَ بنفسِكَ قبلَ التسليمِ (الفاحصُ نفسُهُ الذي يُحتسَبُ بهِ الحكمُ · § 4.7):

```text
python3 /home/user/workspace/council_w620/gemini_3_8_flash/repo/tools/governance/council_verdict_raw_check.py /home/user/workspace/council_w620/gemini_3_8_flash/VERDICT.md --brief /home/user/workspace/council_w620/gemini_3_8_flash/briefing.md --repo /home/user/workspace/council_w620/gemini_3_8_flash/repo
```

(الإحاطةُ نفسُها منسوخةٌ إلى `/home/user/workspace/council_w620/gemini_3_8_flash/briefing.md` قبلَ إطلاقِكَ.) فإن رُفِضَ فأصلحِ **التركيبَ** (لا المخرجَ) وأعِدِ الفحصَ — ولا تُحرِّرْ مخرجًا بيدِكَ أبدًا؛ وإن احتجتَ أعِدِ التقاطَ الأمرِ.

> **تذكيرٌ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · المخرجاتُ خامٌ **كاملةٌ** برموزِ خروجِها (§ 4.5) · الفحصُ الآليُّ (§ 4.7) · الحفظُ الحرفيُّ (§ 4.8) · **وPASS بلا مسبارٍ لا يُحتسَبُ (§ 4.9).**
