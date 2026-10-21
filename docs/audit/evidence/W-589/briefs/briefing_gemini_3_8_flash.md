# إحاطةُ جولةِ مراجعةِ البندِ WI-105 — جولةُ التصميمِ (المعيارُ 1) — المقعدُ `gemini_3_8_flash`

## الهدف: إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ — معبَّأةٌ منَ القالبِ الثابتِ `COUNCIL_BRIEF_TEMPLATE.md` (sha256 `90465d7ab19345f4b2d74c317277bd7c327521b569a132290d778b2d602773a9`)
## النطاق: جولةُ مراجعةٍ واحدةٌ للبندِ WI-105 (J1 · `issue_ruling` بفاعلٍ قضائيٍّ مُعلَنٍ · C3) **على وثيقةِ التصميمِ قبلَ الشِّفرةِ** — المعيارُ (1) وحدَه · نسخةٌ لكلِّ مقعدٍ لا تختلفُ إلّا في جذرِ الدليلِ واسمِ المقعدِ (§ 2.6) · تُبصَمُ sha256 في قيدِ W-585 قبلَ الإطلاقِ · المنسِّقُ الحاضرُ Claude Opus 5.5 ⇒ يُستبعَدُ مقعدُ عائلةِ Claude (§ 1.5 · Q-60) · أدلّةُ المقاعدِ `council_w589`
## المالك: بندُ WI-105 (المنسِّقُ لا يُصوِّتُ)
## تاريخ الإنشاء: 2026-10-21
## تاريخ آخر تعديل: 2026-10-21 (W-589 — الجولةُ الثانيةُ · العقدةُ عقدةُ قيدِ W-588 بعدَ تصحيحِ DISC-126 · والأمرانِ 9 و10 يقيسانِ سابقةَ WI-082 لأثرِ الأسطحِ)

> معبَّأةٌ منَ البندِ نفسِهِ لا منَ تقريرِ منفِّذٍ · مُبصَمةٌ قبلَ إطلاقِ المقاعدِ · لا تُعدَّلُ بعدَ الإطلاقِ.
> **المخرجاتُ خامٌ كاملةٌ — ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ، مهما طالَ المخرجُ** (البروتوكولُ § 4.5). وحكمُكَ يُفحَصُ آليًّا ولا يُحتسَبُ إن رُفِضَ (§ 4.7).

## أ · العقدةُ والمستودعُ

- المستودعُ: `vooovg-ui/AMOS-Fedration`
- العقدةُ المرادُّ مراجعتُها (كاملةً): `4f357aab60567d3c43d2075d1f30191d74067174`
- **دليلُكَ الخاصُّ (§ 2.6 · لا مسارَ مشتركٌ):** `/home/user/workspace/council_w589/gemini_3_8_flash` — كلُّ ما تكتبُهُ (الاستنساخُ · الملفّاتُ المؤقّتةُ · قاعدةُ البياناتِ · سجلُّ الذرّيّةِ · كتلُ RAW · ملفُّ حكمِكَ) داخلَهُ وحدَهُ، **لا تحتَ `/tmp`** ولا في دليلِ مقعدٍ آخرَ.
- التهيئةُ (قبلَ أوامرِ المعاييرِ · لا تُلتقَطُ لأنَّ أداةَ الالتقاطِ داخلَ الاستنساخِ):

```text
mkdir -p /home/user/workspace/council_w589/gemini_3_8_flash/tmp /home/user/workspace/council_w589/gemini_3_8_flash/raw
git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w589/gemini_3_8_flash/repo
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && git checkout 4f357aab60567d3c43d2075d1f30191d74067174
```

## ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` عندَ العقدةِ (`git show 4f357aa:docs/governance/work/ACTIVE_WORK.md` — حرفيًّا):

```text
| WI-105 | federal-executive | T1 (الدفعةُ **J1** من خطّةِ حرقِ D-4: `issue_ruling` يعبرُ الحدَّ السياديَّ بفاعلٍ قضائيٍّ مُعلَنٍ — سندُ قرارِ المالكِ `Q-6` ① وشرطُه `WI-082` VERIFIED (W-576) · **حسّاسٌ: سيادة بقائمةِ Q-H** · فئةُ C3: وثيقةُ التصميمِ `docs/audit/J1_ISSUE_RULING_DESIGN.md` في التزامٍ يسبقُ الشِفرةَ ثمَّ جولةُ مجلسٍ ثمَّ موافقةُ المالكِ — التوجيهُ 17 § 3) | Perplexity Computer | مجلسُ المراجعةِ (بروتوكولُ المجلسِ · Q-59) — حسّاسٌ: إعادةُ تشغيلٍ وتقريرٌ حرفيٌّ — ولا VERIFIED بيدِ المنفِّذِ (§ 4.3) | IN_REVIEW | federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py · federal/executive/services/src/amos_federation/services/federal_judiciary/service.py · federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py · federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py · federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py · docs/audit/J1_ISSUE_RULING_DESIGN.md · docs/audit/evidence/W-581 · docs/audit/evidence/W-582 · docs/audit/evidence/W-584 · docs/audit/evidence/W-585 · docs/audit/evidence/W-586 · docs/audit/evidence/W-587 · docs/audit/evidence/W-588 | 2026-10-21 | 2026-11-20 | لا عائقَ لجولةِ التصميمِ (W-583: IN_PROGRESS→IN_REVIEW لجولةِ المجلسِ على وثيقةِ التصميمِ وحدَها — المعيارُ (1)) · والشِّفرةُ تنتظرُ حكمَ الجولةِ وموافقةَ المالكِ بنصِّه على D1 · D4 · D6 · D7 ثمَّ العودةَ IN_PROGRESS قيدًا مستقلًّا (سابقةُ W-534/W-571) · وكانَ: لا عائقَ للتصميمِ · والشِّفرةُ تنتظرُ جولةَ المجلسِ على وثيقةِ التصميمِ وموافقةَ المالكِ (التوجيهُ 17 § 3 · المرحلةُ 1 · 3–4) | D-4: 183 ← 181 بالأداةِ نفسِها · T1–T7 ناجحةٌ · الطفرةُ M1 (حذفُ العبورِ) تُسقِطُ T1 وT2 · test_r7d كاملًا بلا تعديلٍ · CI أخضرُ مقروءٌ | — (يُكتَبُ عندَ الإغلاقِ) |
```

كتلةُ البندِ عندَ العقدةِ نفسِها (حرفيًّا):

### WI-105 — T1 · الدفعةُ J1: `issue_ruling` يعبرُ الحدَّ بفاعلٍ قضائيٍّ مُعلَنٍ (Q-6 ①) — `IN_REVIEW` (W-583 · جولةُ التصميمِ)

```
المعرِّف: WI-105
النطاق: T1 (federal-executive · services/federal_judiciary + جسرُ executive_core — حسّاسٌ: سيادة بقائمةِ Q-H · فئةُ C3)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · بتوجيهِ المالكِ 17 § 3 المرحلةُ 1)
المراجع: مجلسُ المراجعةِ (بروتوكولُ المجلسِ · Q-59) — **حسّاسٌ (سيادة · Q-H): يُعيدُ المراجعُ التشغيلَ ويحفظُ تقريرَه حرفيًّا** — ولا VERIFIED بيدِ المنفِّذِ (§ 4.3)
الحالة: IN_REVIEW   (قيدُ W-583: IN_PROGRESS→IN_REVIEW قيدًا مستقلًّا (H3) لجولةِ مجلسِ المراجعةِ على وثيقةِ التصميمِ وحدَها — المعيارُ (1) قبلَ الشِّفرةِ · بروتوكولُ المجلسِ § 7.4 لا يعرضُ إلّا بندًا IN_REVIEW · والعودةُ IN_PROGRESS للشِّفرةِ بعدَ الحكمِ وموافقةِ المالكِ بنصِّه — سابقةُ W-534/W-571 · لا VERIFIED بهذه الجولةِ: المعاييرُ (2)–(6) لا تنطبقُ قبلَ الشِّفرةِ) · والسابقُ (تاريخٌ لا يُمحى): IN_PROGRESS   (قيدُ W-581: RESERVED→IN_PROGRESS بأوّلِ دليلٍ (وثيقةُ التصميمِ · evidence/W-581) — ولا شِفرةَ قبلَ جولةِ المجلسِ وموافقةِ المالكِ) · والسابقُ (تاريخٌ لا يُمحى): RESERVED (قيدُ W-580: READY→RESERVED — الحجزُ حتى الأفقِ 2026-11-20 · ولم تُلمَسْ شِفرةٌ) · والسابقُ (تاريخٌ لا يُمحى): READY (قيدُ W-579 · سُجِّلَ READY مباشرةً بـTHE_ROADMAP § 4 خطوة 2: محدَّدٌ · غيرُ متعارضٍ · تبعيّتُه WI-082 VERIFIED (W-576) — وموافقةُ المالكِ تحجبُ الشِّفرةَ لا الحالةَ)
المسارات: federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py · federal/executive/services/src/amos_federation/services/federal_judiciary/service.py · federal/executive/services/src/amos_federation/services/federal_judiciary/authority.py · federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py · federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py · docs/audit/J1_ISSUE_RULING_DESIGN.md · docs/audit/evidence/W-581 · docs/audit/evidence/W-582 · docs/audit/evidence/W-584 · docs/audit/evidence/W-585 · docs/audit/evidence/W-586 · docs/audit/evidence/W-587 · docs/audit/evidence/W-588
بدأ: 2026-10-21 · الأفق: 2026-11-20

قياسُ ما قبلُ (2026-10-21 · العقدة 2694796 — يُودَعُ دليلُه حينَ يبدأُ العملُ):
  (أ) sovereign_write_inventory.py: debt 183 · sovereign 17 · أسطحٌ 220 — وفي الوحدةِ 27 موضعًا كلُّها دَينٌ،
      منها الموضعانِ rulings.py::issue_ruling (add) وservice.py::issue_ruling (commit)
  (ب) النداءاتُ: إنتاجيٌّ 1 (service.py:672) · اختباراتٌ 18 في test_r7d_federal_judiciary.py
  (ج) probe_issue_ruling_actors.py: عبرَ الجسرِ يُرفَضُ issue_ruling لكلِّ فاعلٍ (JurisdictionNotDeclaredError 6/6)
      لأنَّ guard_declared لا يحملُ judicial_action · وعبرَ الحدِّ الجوهريِّ بطلبِ اختصاصٍ: JUDICIAL ينفذُ · EXECUTIVE/LEGISLATIVE/
      TREASURY ⇒ DENY (A003) · AGENT/SYSTEM ينفذانِ (يُقيَّدُ اكتشافًا حينَ يبدأُ العملُ — خارجَ هذا البندِ)

خارج النطاق: rules.py · jurisdiction.py · royal/ · مستوياتُ زرِّ الإيقافِ · vacate_ruling (J2) · record_proceeding (J3) · ثغرةُ AGENT/SYSTEM في قاعدةِ الحصرِ

معيار القبول: (1) **قبلَ الشِّفرة**: وثيقةُ التصميمِ docs/audit/J1_ISSUE_RULING_DESIGN.md مُلتزَمةٌ في قيدٍ يسبقُ الشِّفرةَ ثمَّ جولةُ مجلسٍ عليها
  ثمَّ موافقةُ المالكِ بنصِّه على نقاطِ الحكمِ D1 · D4 · D6 · D7 (2) rulings.issue_ruling يحملُ guard_declared( بالفعلِ issue_ruling
  وطلبِ اختصاصٍ منَ البياناتِ الحيّةِ ومُعوِّضٍ حقيقيٍّ ومفتاحٍ بجيلِ الإلغاءِ (3) D-4: 183 ← 181 · sovereign 17 ← 18 · أسطحٌ 220 ← 219 [W-588: الصحيحُ 220 ← 220 · DISC-126]
  بالأداةِ نفسِها بلا نموٍّ في غيرِه (4) T1–T7 ناجحةٌ · وطفرةُ حذفِ العبورِ (M1) تُسقِطُ T1 وT2 · وM2–M4 كلٌّ يُسقِطُ فحصَه
  (5) test_r7d_federal_judiciary.py وفحوصُ WI-082 بلا تعديلٍ · وحزمُ services خضراءُ في CI مقروءًا (6) مراجعةٌ تُعيدُ التشغيلَ (Q-H)

الدليل المطلوب: docs/audit/J1_ISSUE_RULING_DESIGN.md · docs/audit/evidence/W-581/ (قياسُ ما قبلُ) · ودليلُ الدفعةِ المنفِّذةِ (الجردُ قبلُ/بعدُ · الطفراتُ · CI)

[W-581 · 2026-10-21] بدأَ العملُ بأوّلِ دليلٍ: وثيقةُ التصميمِ docs/audit/J1_ISSUE_RULING_DESIGN.md (مُلتزَمةٌ قبلَ أيِّ شِفرةٍ)
  وقياسُ ما قبلُ evidence/W-581/probe_issue_ruling_actors.py (الأقسامُ أ–د) · والاكتشافُ المذكورُ في (ج) قُيِّدَ DISC-121 وسؤالُه Q-68
  (PENDING_OWNER) · ونقاطُ الحكمِ D1 · D4 · D6 · D7 تُعرَضُ على مجلسِ المراجعةِ ثمَّ على المالكِ (HANDOFFS/OWNER-DECISIONS-D17.md البند 6)
[W-582 · 2026-10-21] استلامٌ معلنٌ بتوجيهِ المالكِ 17 («تسليمٌ كاملٌ بصلاحياتٍ واسعةٍ للوكيلِ الجديدِ» — نصُّه حرفيًّا في
  evidence/W-582/OWNER_DIRECTIVE_17.md): المالكُ في الصفِّ باقٍ Perplexity Computer · والمنسِّقُ الحاضرُ Claude Opus 5.5 ·
  والبناءُ على قيودِ W-579…W-581 لا إعادتُها · وقياسُ المرحلةِ 0 حيًّا في evidence/W-582 · والقسمُ (د) منَ القياسِ
  أُعيدَ إنتاجُه بسكربتٍ مُلتزَمٍ (DISC-122) · وأُضيفَت مساراتُ أدلّةِ W-582/W-584/W-585 إلى الدعوى
[W-584 · 2026-10-21] تصحيحٌ بالإضافةِ (DISC-124): «(ب) … اختباراتٌ 18» في قياسِ ما قبلُ — المقيسُ 15
  (rg -c "judiciary\.issue_ruling\(" على test_r7d_federal_judiciary.py · ولا نداءَ في غيرِه منَ الاختباراتِ) · و18 باقٍ تاريخًا
  · ووثيقةُ التصميمِ صُحِّحَت بالإضافةِ في § 1.2 و§ 4 · ومسارُ evidence/W-586 أُضيفَ إلى الدعوى (قيدُ أحكامِ الجولةِ)
[W-586 · 2026-10-21] تصحيحُ حمرةِ CI (39604470249 · Lint E731 في evidence/W-582/d5_status_probe.py — المخرجُ لم يتغيّرْ) ·
  وقيدُ أحكامِ الجولةِ ينتقلُ إلى W-587 (مسارُه أُضيفَ إلى الدعوى) · DISC-125
[W-587 · 2026-10-21] أحكامُ جولةِ المجلسِ على التصميمِ (evidence/W-587 · حرفيًّا · الفاحصُ يقبلُ الثلاثةَ 17/17):
  gemini_3_8_flash PASS · kimi_k3 PASS · grok_4_7 FAIL حاجبٌ على D4 («أثر الأسطح المعلن (220←219)» غيرُ سليمٍ —
  المُطبِّقُ المتداخلُ يُحصى موضعًا) · المنسِّقُ تحقّقَ فوجدَها صحيحةً بسابقةِ WI-082 (DISC-126) ⇒ لا إجماعَ (§ 5.1)
  ⇒ لا تغييرَ حالةٍ · باقٍ IN_REVIEW · والتصحيحُ بالإضافةِ في W-588 (مسارُه أُضيفَ إلى الدعوى) ثمَّ جولةٌ جديدةٌ
[W-588 · 2026-10-21] تصحيحٌ بالإضافةِ (DISC-126): المعيارُ (3) «أسطحٌ 220 ← 219» — الصحيحُ 220 ← 220 (المُطبِّقُ المتداخلُ
  الخاصُّ يُحصى موضعًا كسابقةِ WI-082) · والدَّينُ 183 ← 181 والسياديُّ 17 ← 18 بلا تغييرٍ · فالتصحيحُ رقمٌ معلنٌ لا تليينُ معيارٍ ·
  ووثيقةُ التصميمِ صُحِّحَت بالإضافةِ في D4 و§ 4 · وشكلُ المُطبِّقِ (دالّةٌ متداخلةٌ خاصّةٌ واحدةٌ) صارَ من التصميمِ ⇒ جولةٌ ثانيةٌ
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في الالتزامِ `fb7dadb` · قيدِ W-579 — والنصُّ عندَ العقدةِ حرفيًّا):

```text
معيار القبول: (1) **قبلَ الشِّفرة**: وثيقةُ التصميمِ docs/audit/J1_ISSUE_RULING_DESIGN.md مُلتزَمةٌ في قيدٍ يسبقُ الشِّفرةَ ثمَّ جولةُ مجلسٍ عليها
  ثمَّ موافقةُ المالكِ بنصِّه على نقاطِ الحكمِ D1 · D4 · D6 · D7 (2) rulings.issue_ruling يحملُ guard_declared( بالفعلِ issue_ruling
  وطلبِ اختصاصٍ منَ البياناتِ الحيّةِ ومُعوِّضٍ حقيقيٍّ ومفتاحٍ بجيلِ الإلغاءِ (3) D-4: 183 ← 181 · sovereign 17 ← 18 · أسطحٌ 220 ← 219 [W-588: الصحيحُ 220 ← 220 · DISC-126]
  بالأداةِ نفسِها بلا نموٍّ في غيرِه (4) T1–T7 ناجحةٌ · وطفرةُ حذفِ العبورِ (M1) تُسقِطُ T1 وT2 · وM2–M4 كلٌّ يُسقِطُ فحصَه
  (5) test_r7d_federal_judiciary.py وفحوصُ WI-082 بلا تعديلٍ · وحزمُ services خضراءُ في CI مقروءًا (6) مراجعةٌ تُعيدُ التشغيلَ (Q-H)
```

**نطاقُ هذه الجولةِ (منَ البندِ نفسِهِ · قيودُ W-583 وW-584 وW-588):** المعيارُ **(1) وحدَه** — شِقُّه الذي يحكمُ عليه المجلسُ: (1-أ) وثيقةُ التصميمِ `docs/audit/J1_ISSUE_RULING_DESIGN.md` مُلتزَمةٌ في قيدٍ يسبقُ الشِّفرةَ (ولا شِفرةَ إنتاجيّةَ تغيّرت منذُ العقدةِ `2694796`) · (1-ب) وقائعُها المقيسةُ في § 1 منها تُعادُ بتشغيلِكَ (الجردُ · النداءاتُ · حدُّ الجسرِ · حكمُ الحدِّ لكلِّ فاعلٍ) · (1-ج) نقاطُ الحكمِ D1 · D4 · D6 · D7 (§ 6 منها) سليمةٌ تقنيًّا ولا تمسُّ سؤالًا سياديًّا غيرَ محسومٍ. وشِقُّه الأخيرُ («موافقةُ المالكِ بنصِّه») **لا ينطبقُ على المقعدِ**: يأتي بعدَ الجولةِ. والمعاييرُ (2)–(6) **لا تنطبقُ**: لا شِفرةَ قبلَ الموافقةِ — فلا `VERIFIED` بهذه الجولةِ.

## ج · أوامرُ المعاييرِ (منَ البندِ نفسِهِ — كلُّ سطرٍ أمرٌ مكتفٍ بنفسِهِ يُلتقَطُ وحدَهُ)

**طريقةُ التشغيلِ (إلزاميّةٌ · § 4.6):** شغِّلْ كلَّ سطرٍ أدناهُ برقمِهِ n (بترتيبِهِ منَ 1 إلى 19) عبرَ أداةِ الالتقاطِ هكذا — والأمرُ بينَ علامتَي الاقتباسِ **حرفيًّا كما هو في السطرِ نفسِهِ** (بلا رقمِهِ):

```text
python3 /home/user/workspace/council_w589/gemini_3_8_flash/repo/tools/governance/council_raw_capture.py --n <n> --out /home/user/workspace/council_w589/gemini_3_8_flash/raw/<n بخانتين: 01 02 …>.txt '<الأمرُ>'
```

(إن احتوى الأمرُ علامةَ اقتباسٍ مفردةً فمرِّرْهُ بحيثُ يصلُ الأداةَ حرفيًّا — مثلًا بـ`"$(cat <<'EOF' … EOF)"`؛ والمعيارُ أن يطابقَ سطرُ `CMD:` في الكتلةِ السطرَ أدناهُ حرفًا بحرفٍ.)

الأوامرُ (19 أمرًا — منَ البندِ وقياساتِهِ المُعلنةِ في «قياسُ ما قبلُ»: البيئةُ أولًا · ثمَّ ترتيبُ الوثيقةِ قبلَ الشِّفرةِ · ثمَّ جردُ الدَّينِ السياديِّ (كلُّه ثمَّ الوحدةُ) · ثمَّ النداءاتُ وحدُّ الجسرِ وزرُّ الإيقافِ · ثمَّ قياسا حكمِ الحدِّ لكلِّ فاعلٍ (المذكورانِ في البندِ) · ثمَّ الحزمةُ القضائيّةُ القائمةُ · ثمَّ وثيقةُ التصميمِ كاملةً · ثمَّ فحصُ العزلِ § 2.6):

```bash
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && git rev-parse HEAD
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && bash tools/dev/bootstrap.sh
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && git log --format='%h %cI %s' 26947961f61d9d54439569d9d005cace589a762c..HEAD
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && git diff --stat 26947961f61d9d54439569d9d005cace589a762c HEAD -- federal core tools/audit
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && git log --format='%h %cI %s' -- docs/audit/J1_ISSUE_RULING_DESIGN.md
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/federal_judiciary --json /home/user/workspace/council_w589/gemini_3_8_flash/tmp/judiciary.json
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && rg -n "issue_ruling" /home/user/workspace/council_w589/gemini_3_8_flash/tmp/judiciary.json
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/executive_core --json /home/user/workspace/council_w589/gemini_3_8_flash/tmp/executive_core.json
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && rg -n -A8 "agent_identity.py" /home/user/workspace/council_w589/gemini_3_8_flash/tmp/executive_core.json
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && rg -n "rulings\.issue_ruling|issue_ruling\(" --type py federal/executive/services/src | rg -v "def "
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && rg -c "judiciary\.issue_ruling\(" federal/executive/services/tests/test_r7d_federal_judiciary.py
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && rg -n "def guard_declared|judicial_action" federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py core/sovereignty/enforcement_boundary.py
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && rg -n "issue_ruling|KILL_SWITCH_BLOCKS" core/constitutional_engine/rules.py
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER=/home/user/workspace/council_w589/gemini_3_8_flash/tmp/probe_ledger.json PYTHONPATH=federal/executive/services/src:. .venv/bin/python docs/audit/evidence/W-581/probe_issue_ruling_actors.py
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && PYTHONPATH=federal/executive/services/src:. .venv/bin/python docs/audit/evidence/W-582/probe_branch_exclusive_agent_system.py
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w589/gemini_3_8_flash/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py -q
cd /home/user/workspace/council_w589/gemini_3_8_flash/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
find /home/user/workspace/council_w589/gemini_3_8_flash -maxdepth 1
```

## د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)

- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- مُخرَجُ البندِ موضوعُ المراجعةِ: `docs/audit/J1_ISSUE_RULING_DESIGN.md` (الأمرُ 18 يُخرِجُهُ كاملًا) — وما تُحيلُ إليهِ من شِفرةٍ في استنساخِكَ (`federal/executive/services/src/amos_federation/services/federal_judiciary/` · `federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py` · `core/sovereignty/` · `core/constitutional_engine/rules.py`) لتتحقّقَ من وقائعِها
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-6 · Q-68)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ (ملفّاتُ `*.out.txt` و`README.md` في `evidence/W-581/` و`evidence/W-582/` · وورقةُ `HANDOFFS/OWNER-DECISIONS-D17.md`) ولا أدلّةِ أيِّ جولةٍ سابقةٍ — احكمْ من إعادةِ تشغيلِكَ أنتَ.** (السكربتانِ في الأمرَينِ 13 و14 أداتا قياسٍ تُشغِّلُهما لا تقريرانِ تقرؤُهما.)

## هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامٍ كاملةٍ ورموزِ خروجٍ)

1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ (والأمرُ 1 يُثبِتُ العقدةَ).
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ**، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (§ 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ (أشِرْ إلى رقمِ الكتلةِ). (هنا: (1-أ) · (1-ب) · (1-ج) — وما لا ينطبقُ اكتبْ أمامَه «لا ينطبقُ».)
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».

## و · صيغةُ جوابِكَ (ملفُّ الحكمِ يُحفظُ حرفيًّا بلا تحريرٍ · § 4.8)

اكتبْ ملفَّ حكمِكَ في `/home/user/workspace/council_w589/gemini_3_8_flash/VERDICT.md` بهذهِ الصيغةِ — وقسمُ `RAW_OUTPUTS` يُركَّبُ **آليًّا** منْ ملفّاتِ `/home/user/workspace/council_w589/gemini_3_8_flash/raw/*.txt` بترتيبِها (مثلًا `cat /home/user/workspace/council_w589/gemini_3_8_flash/raw/*.txt`) بلا أيِّ نصٍّ بينها:

```
MODEL: <اسمُ النموذجِ كما أعلنتْهُ المنصةُ>
FAMILY: <العائلةُ>
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: 4f357aab60567d3c43d2075d1f30191d74067174
CLONE_PATH: /home/user/workspace/council_w589/gemini_3_8_flash/repo
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
RAW_OUTPUTS:
<كتلُ RAW كما كتبتْها الأداةُ>
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ برقمِ الكتلةِ>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرارُ>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

ثمَّ افحصْ ملفَّكَ بنفسِكَ قبلَ التسليمِ (الفاحصُ نفسُهُ الذي يُحتسَبُ بهِ الحكمُ · § 4.7):

```text
python3 /home/user/workspace/council_w589/gemini_3_8_flash/repo/tools/governance/council_verdict_raw_check.py /home/user/workspace/council_w589/gemini_3_8_flash/VERDICT.md --repo /home/user/workspace/council_w589/gemini_3_8_flash/repo
```

فإن رُفِضَ فأصلحِ **التركيبَ** (لا المخرجَ) وأعِدِ الفحصَ — ولا تُحرِّرْ مخرجًا بيدِكَ أبدًا؛ وإن احتجتَ أعِدِ التقاطَ الأمرِ.

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وملفُّ حكمِكَ في دليلِكَ يُحفظُ حرفيًّا في المستودعِ (§ 4.8).
