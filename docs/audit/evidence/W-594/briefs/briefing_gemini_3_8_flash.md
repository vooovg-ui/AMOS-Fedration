# إحاطةُ جولةِ مراجعةِ البندِ WI-105 — جولةُ الدفعةِ (تصميمًا وشِفرةً وأدلةً) — المقعدُ `gemini_3_8_flash`

## الهدف: إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ
## النطاق: جولةُ مراجعةٍ واحدةٌ للبندِ WI-105 (J1 · `issue_ruling` بفاعلٍ قضائيٍّ مُعلَنٍ · C3) **على الدفعةِ كلِّها بعدَ التنفيذِ: التصميمُ والشِّفرةُ والأدلةُ معًا** (بروتوكولُ المجلسِ § 7 كما عُدِّلَ بأمرِ المالكِ في توجيهِ المستشارِ 17 § 2 — لا جولاتِ مجلسٍ على تصميمٍ منفردٍ) · نسخةٌ لكلِّ مقعدٍ لا تختلفُ إلّا في جذرِ الدليلِ واسمِ المقعدِ (§ 2.6) · تُبصَمُ sha256 في قيدِ W-598 قبلَ الإطلاقِ · **المنسِّقُ الحاضرُ عندَ الإطلاقِ GLM-5.3 (عائلةُ GLM)** ⇒ الاستبعادُ عندَ الإطلاقِ على المنسِّقِ الفعليِّ (§ 1.5 المعدَّلُ) فلا مقعدَ من عائلةِ GLM · ومقعدُ claude_opus_5_5 متاحٌ الآنَ · أدلّةُ المقاعدِ `council_w598` · **[عُدِّلَتْ مؤرَّخًا في W-596 قبلَ الإطلاقِ (لم تُطلَقْ بعدُ): العقدةُ صُحِّحَت إلى رأسِ هذا الفرعِ ليشملَ تصحيحَ لقطاتِ القياسِ ومُثبَّتاتِ الحارسِ (W-595) · وأُضيفَتِ الأوامرُ 19–21 · وحُدِّدَت أسئلةُ الحكمِ في T6 والطفراتِ]** **[عُدِّلَتْ مؤرَّخًا في W-598 قبلَ الإطلاقِ (لم تُطلَقْ بعدُ · سابقةُ W-596): العقدةُ صُحِّحَت إلى `03a6c62` — رأسِ main بعدَ الانتقالِ التوثيقيِّ W-597 (IN_PROGRESS → IN_REVIEW · § 7.4 · لا شِفرةَ زائدةً — فرقُ مساراتِ الشِّفرةِ بينَ 90cae46 و03a6c62 فارغٌ مقيسًا) · وأدلّةُ المقاعدِ تغيَّرتْ إلى `council_w598`]**
## المالك: بندُ WI-105 (المنسِّقُ لا يُصوِّتُ)
## تاريخ الإنشاء: 2026-10-21
## تاريخ آخر تعديل: 2026-10-22 (W-598 — تعديلٌ مؤرَّخٌ قبلَ الإطلاقِ · والسابقُ: W-596 2026-10-21)

> معبَّأةٌ منَ البندِ نفسِهِ لا منَ تقريرِ منفِّذٍ · مُبصَمةٌ قبلَ إطلاقِ المقاعدِ · لا تُعدَّلُ بعدَ الإطلاقِ.
> **المخرجاتُ خامٌ كاملةٌ — ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ، مهما طالَ المخرجُ** (البروتوكولُ § 4.5). وحكمُكَ يُفحَصُ آليًّا ولا يُحتسَبُ إن رُفِضَ (§ 4.7).

## أ · العقدةُ والمستودعُ

- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُّ مراجعتُها: رأسُ فرعِ `w-594-v2-j1-batch-briefs` (آخرُ التزامٍ فيه — ويُثبِتُهُ منسِّقُ الإطلاقِ في رسالةِ الإطلاقِ، ويُثبِتُهُ المقعدُ بالأمرِ 1)** **[إضافةٌ مؤرَّخةٌ (2026-10-22 · W-598): العقدةُ الآنَ `03a6c62` — رأسُ main بعدَ الانتقالِ التوثيقيِّ W-597 فوقَ رأسِ الفرعِ · شِفرةُ البندِ وتصحيحُ القياساتِ (W-593/W-595) لم يتغيرْ بايتًا بينَ العقدتَينِ (فرقُ مساراتِ الشِّفرةِ فارغٌ مقيسًا) · والأمرُ 1 يُثبِتُ العقدةَ كما في رسالةِ الإطلاقِ]** — وتشملُ شِفرةَ J1 (التزامُ W-593) **وتصحيحَ لقطاتِ القياسِ ومُثبَّتاتِ الحارسِ (التزامُ W-595)** — فلا تُراجَعْ عقدةً ناقصةَ الإصلاحِ.
- **دليلُكَ الخاصُّ (§ 2.6 · لا مسارَ مشتركٌ):** `/home/user/workspace/council_w598/gemini_3_8_flash` — كلُّ ما تكتبُهُ (الاستنساخُ · الملفّاتُ المؤقّتةُ · قاعدةُ البياناتِ · سجلُّ الذرّيّةِ · كتلُ RAW · ملفُّ حكمِكَ) داخلَهُ وحدَهُ، **لا تحتَ /tmp** ولا في دليلِ مقعدٍ آخرَ.
- التهيئةُ (قبلَ أوامرِ المعاييرِ · لا تُلتقَطُ لأنَّ أداةَ الالتقاطِ داخلَ الاستنساخِ):

```text
mkdir -p /home/user/workspace/council_w598/gemini_3_8_flash/tmp /home/user/workspace/council_w598/gemini_3_8_flash/raw
git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w598/gemini_3_8_flash/repo
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && git checkout <الرأسُ من رسالةِ الإطلاقِ>
```

## ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في قيدِ W-579 الالتزامِ `fb7dadb` · وعلى العقدةِ حرفيًّا — والأمرُ 5 يُخرِجُ تاريخَ التزامِها):

```text
معيار القبول: (1) **قبلَ الشِّفرة**: وثيقةُ التصميمِ docs/audit/J1_ISSUE_RULING_DESIGN.md مُلتزَمةٌ في قيدٍ يسبقُ الشِّفرةَ ثمَّ جولةُ مجلسٍ عليها
  ثمَّ موافقةُ المالكِ بنصِّه على نقاطِ الحكمِ D1 · D4 · D6 · D7 (2) rulings.issue_ruling يحملُ guard_declared( بالفعلِ issue_ruling
  وطلبِ اختصاصٍ منَ البياناتِ الحيّةِ ومُعوِّضٍ حقيقيٍّ ومفتاحٍ بجيلِ الإلغاءِ (3) D-4: 183 ← 181 · sovereign 17 ← 18 · أسطحٌ 220 ← 219 [W-588: الصحيحُ 220 ← 220 · DISC-126]
  بالأداةِ نفسِها بلا نموٍّ في غيرِه (4) T1–T7 ناجحةٌ · وطفرةُ حذفِ العبورِ (M1) تُسقِطُ T1 وT2 · وM2–M4 كلٌّ يُسقِطُ فحصَهُ
  (5) test_r7d_federal_judiciary.py وفحوصُ WI-082 بلا تعديلٍ · وحزمُ services خضراءُ في CI مقروءًا (6) مراجعةٌ تُعيدُ التشغيلَ (Q-H)
```

**نطاقُ هذه الجولةِ:** الدفعةُ كلُّها — المعاييرُ (2)–(6) (الشِّفرةُ موجودةٌ) **والمعيارُ (1)** في شِقِّهِ المتبقّي: التزامُ وثيقةِ التصميمِ يسبقُ التزامَ الشِّفرةِ في التاريخِ (الأمرُ 5 — درسُ Q-61) وسلامةُ **الإضافتينِ المؤرَّختينِ** (الأمرُ 16):
- **(أ) الجيلُ في هدفِ العبورِ:** بصمةُ العقدِ تُشتقُّ من (الفاعلِ · الفعلِ · الهدفِ · الآثارِ) ومعرِّفُ الإذنِ بدقّةِ الثانيةِ، فحكمانِ للمرحلةِ نفسِها في الثانيةِ نفسِها يتصادمانِ في الإذنِ — فحُمِّلَ الهدفُ الجيلَ `g{n}`.
- **(ب) قياسُ T6 عبرَ حارسِ 1I:** مسارُ الحدِّ أحاديَّ الأثرِ ينفّذُ عبرَ `run_once` لا عبرَ معاملةِ 1I المُعوَّضةَ، فالتعويضُ الآليُّ غيرُ موصولٍ — فيُقاسُ المُعوِّضُ بحارسِ 1I بالعقدِ والخطةِ منَ العبورِ الحقيقيِّ.
- وموافقةُ المالكِ على نقاطِ الحكمِ **صدرتْ فعلًا** (توجيهُ المستشارِ 17 § 1: Q-69 DECIDED · D17-6) فلا تُحاكَمْ هنا — تُقاسُ الشِّفرةُ على المعاييرِ.

## ج · أوامرُ المعاييرِ (كلُّ سطرٍ أمرٌ مكتفٍ بنفسِهِ يُلتقَطُ وحدَهُ)

**طريقةُ التشغيلِ (إلزاميّةٌ · § 4.6):** شغِّلْ كلَّ سطرٍ أدناهُ برقمِهِ n (بترتيبِهِ منَ 1 إلى 22) عبرَ أداةِ الالتقاطِ هكذا — والأمرُ بينَ علامتَي الاقتباسِ **حرفيًّا كما هو في السطرِ نفسِهِ** (بلا رقمِهِ):

```text
python3 /home/user/workspace/council_w598/gemini_3_8_flash/repo/tools/governance/council_raw_capture.py --n <n> --out /home/user/workspace/council_w598/gemini_3_8_flash/raw/<n بخانتين: 01 02 …>.txt '<الأمرُ>'
```

الأوامرُ (22 أمرًا — البيئةُ أولًا · ثمَّ ترتيبُ الوثيقةِ قبلَ الشِّفرةِ (Q-61) · ثمَّ جردُ الدَّينِ السياديِّ (كلُّه ثمَّ الوحدةُ ثمَّ الجسرُ) · ثمَّ فحوصُ T1–T7 والفحوصُ القائمةُ والحزمةُ كاملةً · ثمَّ شِفرةُ العبورِ ووثيقةُ التصميمِ ومخرجاتُ الطفراتِ وقياساتُ الدفعةِ · ثمَّ حرسُ الحوكمةِ (فحوصُ المُثبَّتاتِ وفرقُها وعقدُ نَسَبِ القياساتِ — تصحيحُ W-595) · ثمَّ فحصُ العزلِ § 2.6):

```bash
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && git rev-parse HEAD
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && bash tools/dev/bootstrap.sh
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && git log --format='%h %cI %s' d0932c51..HEAD
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && git diff --stat d0932c51 HEAD
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && git log --format='%h %cI %s' -- docs/audit/J1_ISSUE_RULING_DESIGN.md
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && git diff d0932c51 HEAD -- federal/executive/services/tests/test_r7d_federal_judiciary.py federal/executive/services/tests/test_wi082_agent_identity_sovereign.py
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/federal_judiciary --json /home/user/workspace/council_w598/gemini_3_8_flash/tmp/judiciary.json
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && rg -n "issue_ruling|guarded|public" /home/user/workspace/council_w598/gemini_3_8_flash/tmp/judiciary.json
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/executive_core --json /home/user/workspace/council_w598/gemini_3_8_flash/tmp/executive_core.json
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py -q
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py -q
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests -q
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && rg -n "JUDICIARY_ACTOR|judicial_action|position_scope|guard_declared\(" federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py federal/executive/services/src/amos_federation/services/federal_judiciary/service.py federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && cat docs/audit/evidence/W-593/mutation_m1.txt docs/audit/evidence/W-593/mutation_m2.txt docs/audit/evidence/W-593/mutation_m3.txt docs/audit/evidence/W-593/mutation_m4.txt
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && cat docs/audit/evidence/W-593/measurements.txt
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite://///home/user/workspace/council_w598/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_step7_factory_surfaces.py -q
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && git diff d0932c51 HEAD -- tests/governance docs/audit/measurements
cd /home/user/workspace/council_w598/gemini_3_8_flash/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
find /home/user/workspace/council_w598/gemini_3_8_flash -maxdepth 1
```

## د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)

- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- مُخرَجُ البندِ موضوعُ المراجعةِ: وثيقةُ التصميمِ `docs/audit/J1_ISSUE_RULING_DESIGN.md` (الأمرُ 16 يُخرِجُهُ كاملًا) وشِفرةُ العبورِ في استنساخِكَ (`federal_judiciary/rulings.py` · `service.py` · `authority.py` · `executive_core/sovereignty_bridge.py` · `core/sovereignty/`) · ومخرجاتُ الطفراتِ وقياساتُ الدفعةِ (الأمرانِ 17 و18 — مخرجاتٌ خامٌ مُلتزَمةٌ في الدليلِ تحكمُ عليها بإعادةِ تشغيلِكَ أنتَ للأوامرِ 11–14)
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-6 · Q-69 · Q-68)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ جولاتٍ سابقةٍ (W-581…W-590) ولا ورقةُ D17 — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

## هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامٍ كاملةٍ ورموزِ خروجٍ)

1. هل استنسختَ المستودعَ بنفسِكَ عندَ رأسِ الفرعِ المعلَنِ في رسالةِ الإطلاقِ؟ أعدِدْ مسارَ استنساخِكَ (والأمرُ 1 يُثبِتُ العقدةَ).
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ**، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (§ 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ (أشِرْ إلى رقمِ الكتلةِ). (هنا: (1) شِقُّ الترتيبِ والإضافتينِ · (2) · (3) · (4) · (5) · (6) — وموافقةُ المالكِ في (1) صدرتْ فاكتبْ أمامَها «صدرتْ بتوجيهِ المستشارِ 17 ولا تُحاكَمْ هنا».)
   **وفي المعيارِ (4) تحديدًا حاكِمْ هذينِ بنفسِكَ منَ النصِّ المعتمدِ (الأمرُ 16) لا من تقريرِ المنفِّذِ:**
   - **T6/المعيارُ «مُعوِّضٍ حقيقيٍّ»:** هل يقتضي النصُّ المعتمدُ (D7-أ كما وافقَ عليها المالكُ) تعويضًا **آليًّا يُستدعى عندَ فشلِ التثبيتِ في مسارِ الإنتاجِ**، أم **مُعوِّضًا مسجَّلًا صالحًا** يُثبِتُ صلاحيّتَهُ قياسُ حارسِ 1I؟ فإن رأيتَ الأولَ وهو غيرُ موصولٍ في المسارِ أحاديِّ الأثرِ (كما تقولُ الإضافةُ المؤرَّخةُ) فاحكمْ على المعيارِ بما تراهُ منَ النصِّ — الإضافةُ المؤرَّخةُ والقياسُ عبرَ الحارسِ **قرينةٌ معروضةٌ عليكَ لا حسمٌ**.
   - **الطفراتُ M1–M4:** مخرجاتُها المُلتزَمةُ أمامَكَ (الأمرُ 17) وإجراءُ إجرائِها موصوفٌ فيها. فإن رأيتَ قراءتَها لا تكفي لإثباتِ أنّ كلَّ طفرةٍ تُسقِطُ فحصَها **فأعِدْ إجرائَها بنفسِكَ في نسخةٍ معزولةٍ** ووثِّقْ مخرجَكَ الخامَ — لكَ ذلكَ ولستَ مُلزَمًا بالاكتفاءِ بقراءةِ مخرجاتِ المنفِّذِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».

## و · صيغةُ جوابِكَ (ملفُّ الحكمِ يُحفظُ حرفيًّا بلا تحريرٍ · § 4.8)

اكتبْ ملفَّ حكمِكَ في `/home/user/workspace/council_w598/gemini_3_8_flash/VERDICT.md` بهذهِ الصيغةِ — وقسمُ `RAW_OUTPUTS` يُركَّبُ **آليًّا** منْ ملفّاتِ `/home/user/workspace/council_w598/gemini_3_8_flash/raw/*.txt` بترتيبِها (مثلًا `cat /home/user/workspace/council_w598/gemini_3_8_flash/raw/*.txt`) بلا أيِّ نصٍّ بينها:

```
MODEL: <اسمُ النموذجِ كما أعلنتْهُ المنصةُ>
FAMILY: <العائلةُ>
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: <رأسُ الفرعِ الذي استنسختَهُ — منَ الأمرِ 1>
CLONE_PATH: /home/user/workspace/council_w598/gemini_3_8_flash/repo
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
 22. <الأمرُ 22 حرفيًّا كما في سطرِ CMD من كتلتِهِ>
RAW_OUTPUTS:
<كتلُ RAW كما كتبتْها الأداةُ>
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ برقمِ الكتلةِ>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرارُ>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

ثمَّ افحصْ ملفَّكَ بنفسِكَ قبلَ التسليمِ (الفاحصُ نفسُهُ الذي يُحتسَبُ بهِ الحكمُ · § 4.7):

```text
python3 /home/user/workspace/council_w598/gemini_3_8_flash/repo/tools/governance/council_verdict_raw_check.py /home/user/workspace/council_w598/gemini_3_8_flash/VERDICT.md --repo /home/user/workspace/council_w598/gemini_3_8_flash/repo
```

فإن رُفِضَ فأصلحِ **التركيبَ** (لا المخرجَ) وأعِدِ الفحصَ — ولا تُحرِّرْ مخرجًا بيدِكَ أبدًا؛ وإن احتجتَ أعِدِ التقاطَ الأمرِ.

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وملفُّ حكمِكَ في دليلِكَ يُحفظُ حرفيًّا في المستودعِ (§ 4.8).
