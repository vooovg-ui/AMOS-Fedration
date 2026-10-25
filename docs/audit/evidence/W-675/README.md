# دليلُ قيدِ W-675 — WI-114 السطحانِ 1 و3: `governance/canary.py` يعبرُ الحدَّ السياديّ

## التعريف
دليلُ قيدِ `W-675`: شِفرةُ السطحَينِ 1 (`activate_kill_switch`) و3 (`create_promotion`) من WI-114 بأمرِ التوجيهِ 23 § 2 نصًّا: «WI-114 (السطحان 1 و3): الشفرة الآن (التصميم موجود). السطحان 2 و4 بعد قرار 1 بشروطه». التصميمُ: `docs/audit/A1A_CANARY_CROSSING_DESIGN.md` § 3 (W-664).

## النطاق
- **السطح 1:** الرفعُ يعبرُ `guard_declared` بفعلِ `activate_kill_switch` (ALLOW اليومَ للفاعلِ التنفيذيّ)، و**المستوى الأدنى من القائمِ يُوجَّهُ إلى `lower_kill_switch`** (§ 3.3) فيرفضُه R-008-3 (لا قناةَ لموافقةٍ بشريّةٍ عبرَ الجسر · § 3.2) ⇒ `KillSwitchRefusedError` (403) ولا كتابة — علاجُ DISC-138. أثرٌ مُعلَنٌ `WRITE:governance/system_state/<nonce>` ومُعوِّضٌ يستعيدُ اللقطةَ السابقة.
- **السطح 3:** طلبُ الترقيةِ يعبرُ بفعلِ `request_promotion` (فعلٌ حرٌّ ALLOW · مقيسٌ أدناه) **لا** `promote_model` (DENY · يبقى للانتقالِ إلى `promoted` في السطحِ 4). أثرٌ `CREATE:governance/promotions/<id>` ومُعوِّضٌ **يُبطِلُ** (`cancelled`) لا يحذف.
- لا مساسَ بـ`persistent.py` ولا بالمعجمِ ولا بـR008 ولا بأيِّ حارس.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) · البندُ WI-114.

## تاريخ الإنشاء
2026-10-25

## القياس
- مسبارُ الأفعالِ (`review_only` بفاعلِ EXECUTIVE · قبلَ الشِّفرة): `activate_kill_switch` ALLOW · `lower_kill_switch` DENY · `request_promotion` ALLOW · `create_promotion` ALLOW · `register` ALLOW · `promote_model` DENY (على `governance/system_state` و`governance/promotions/x`).
- كلُّ عبورٍ يتركُ أثرَينِ في سجلِّ البوّابة: `PERMIT_ISSUED · AUTHORIZED` ثمَّ `PERMIT_ISSUED · COMPLETED`.
- **D-4 قبلُ/بعدُ: 135 → 135** (W1 11 · W2 34 · W3 90 · مواقعُ الكتابةِ 232) — **حرقٌ 0 وتصحيحٌ 0**: أداةُ الجردِ تعدُّ مواقعَ الكتابةِ في `common/persistent.py` (`PersistentSystemStateStore.set_level` وأخواتِها) لا مستدعيها، فعبورُ المستدعي لا يُرى فيها. (`d4_before.txt` · `d4_after.txt`)
- حزمةُ الخدماتِ: **1539 نجحَت · 53 مُتخطّاة · 0 فشل = 1592** (+14 فحصًا · 224.29 ثانيةً · تشغيلٌ نظيف) — `services_suite.txt`.

## حدُّ الصدق
- **«الفاعلُ من الرمزِ لا من الجسم» (§ 3.3) لم يُنفَّذ**: يتطلّبُ تعديلَ `governance/main.py` و`control_console/main.py` وهما خارجَ مساراتِ WI-114 (`PATH_UNCLAIMED` مقيسًا)، وإضافتُهما تمنعُ حجزَ WI-117 — DISC-139 · `claim_measure.txt`. فالمسارُ ما زالَ يُمرِّرُ `activated_by` من جسمِ الطلب، و`requested_by` لطلبِ الترقيةِ `None`. والفاعلُ الدستوريُّ للعبورِ `EXECUTIVE` ثابتٌ في الوحدةِ (سابقةُ D1) لأنَّ الجسرَ لا يقبلُ إلّا `Branch`.
- `KillSwitchRefusedError` صنفُه `HTTPException` (سابقةُ `enforce_kill_switch` في الوحدةِ نفسِها) ليُجيبَ المسارُ 403 بلا مسٍّ لملفِّ المسار — فالوحدةُ تعرفُ HTTP.
- المُعوِّضُ يعيدُ ختمَ `activated_at` ولا يستعيدُه؛ ومُعوِّضُ الترقيةِ يتركُ صفًّا مُبطَلًا.
- المُعرِّفُ في الهدفِ (`<nonce>`) لأنَّ معرِّفَ الإذنِ `EP-<العقد>-<الثانية>` (DISC-129): بدونِه يُرفَضُ رفعانِ مشروعانِ في ثانيةٍ واحدة (`PermitReplayError` مقيسًا قبلَ الإصلاح) — تحرسُه M6.
- reset والترقيةُ وبوّابةُ `human_approval` ما زالت تقبلُ رمزَ مواطنٍ (`http_probe_after.txt`) — ذلك WI-117 (D25-2) والسطحُ 4، لا هذه الشِّفرة.
- المسبارُ على SQLite مؤقّتةٍ بخدمتَينِ محلّيّتَين؛ لم يُقَسْ في بيئةِ إنتاج.

## تاريخ آخر تعديل
2026-10-25

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `d4_before.txt` · `d4_after.txt` — `python tools/audit/decision_gate.py --measure` قبلَ الشِّفرةِ وبعدَها
- `review_verbs.txt` — مسبارُ الأفعالِ بـ`review_only`
- `mutations.sh` · `mutations.txt` — ستُّ طفراتٍ (M1 توجيهُ الخفض · M2/M3 تجاوزُ الحدّ · M4/M5 المُعوِّضان · M6 المُعرِّفُ في الهدف) كلُّها تُكتشَف، والأصلُ مُستعادٌ بـ`cmp`
- `old_code_vs_new_tests.txt` — الفحوصُ الجديدةُ على `canary.py` كما في `984a6d9f`
- `http_probe_after.txt` — مسبارُ W-672 (`uvicorn` + `urllib` برمزِ مواطن) بعدَ الشِّفرة
- `claim_measure.txt` — قياسُ تقاطعِ الملكيّةِ (DISC-139)
- `services_suite.txt` — ذيلُ حزمةِ الخدماتِ الكاملة
- `ci_verdict_pr152.txt` — حكمُ N+1 لـPR #152 بالفاحصِ والدفعُ السريع
