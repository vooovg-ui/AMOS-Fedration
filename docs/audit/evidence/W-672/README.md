# دليلُ قيدِ W-672 — قياسُ ما قبلَ تحصينِ زرِّ التوقّفِ بطلباتِ HTTP حقيقيّةٍ · تسجيلُ WI-117 READY · WI-114 RESERVED→IN_PROGRESS

## التعريف
دليلُ قيدِ `W-672` (التوجيهُ 23 § 2: «اقرأ مسارات HTTP الستة من جديد قبل التصميم، وقِس كم اختبارًا يمرّ برمز غير ملك» · و§ 0: «قياس نصي لم يُشغَّل فيه طلب HTTP، ويجب تشغيله»):

1. `routes_read.txt` — المساراتُ الستّةُ والحرّاسُ مقروءةٌ بـ`rg -n`/`nl -ba` ومخرجُها ملصقٌ: الحارسُ `Depends(require_auth)` في `governance/main.py:139` (activate · `@router.post` `:136`) · `:149` (reset · `:147`) · `:170` (promotions · `:167`) · `:203` (gates · `:199`) و`control_console/main.py:198` (activate · `:195`) · `:211` (reset · `:209`) · و`require_king` في `common/auth.py:120`.
2. `http_probe.py` + `http_probe_before.txt` — **طلباتُ HTTP حقيقيّةٌ** (خدمتا governance وcontrol_console بـuvicorn على منفذَينِ محلّيَّين · `urllib` لا `TestClient`) برمزٍ `role=citizen`: كلُّ مسارٍ قبِلَ — reset ⇒ 200 و`level`=normal (الوحدتانِ) · activate بـ`level=normal` بعدَ halt ⇒ 200 و`level`=normal (الوحدتانِ · DISC-138) والفاعلُ المكتوبُ «king» من جسمِ الطلبِ · إنشاءُ الترقيةِ ⇒ 201 · `human_approval` passed ⇒ 200.
3. `sim_require_king.sh` + `sim_require_king.txt` — تبديلُ الحارسِ مؤقّتًا إلى `require_king` ثمَّ الإعادةُ: خطُّ الأساسِ 77 passed · بنطاقِ D25-2 (4 مساراتٍ) **6 فحوصٍ تسقطُ** — أي 6 تمرُّ اليومَ برمزٍ غيرِ ملكٍ · ومعَ activate (للقياسِ فقط) 11.

## النطاق
قياسٌ وتسجيلٌ — لا شِفرةَ إنتاجيّةً (الملفّانِ أُعيدا بـ`git checkout` · السطرُ الأخيرُ في `sim_require_king.txt`).

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5).

## تاريخ الإنشاء
2026-10-25

## حدُّ الصدق
المسبارُ على قاعدةِ SQLite مؤقّتةٍ وسرِّ توقيعٍ للاختبارِ في البيئةِ المحوطةِ — لا على نشرٍ إنتاجيٍّ. ورمزُ المواطنِ صُكَّ بـ`create_access_token(…, role=ROLE_CITIZEN)` بالسرِّ نفسِه؛ فالمقيسُ: «أيُّ حاملٍ لرمزٍ صالحِ التوقيعِ بدورِ مواطنٍ» — لا كيفَ يحصلُ مواطنٌ على رمزٍ في الإنتاج. وأرقامُ الأسطرِ في مسمَّياتِ الخطواتِ مأخوذةٌ من `routes_read.txt` على العقدةِ نفسِها.

## تاريخ آخر تعديل
2026-10-25

## المحتويات
- `README.md` — بطاقةُ هويّةِ هذا المجلد
- `routes_read.txt` — قراءةُ المساراتِ والحرّاسِ (أوامرُ ومخرجٌ ورمزُ خروج)
- `http_probe.py` · `http_probe_before.txt` — مسبارُ HTTP ومخرجُه حرفيًّا
- `sim_require_king.sh` · `sim_require_king.txt` — عدُّ الفحوصِ التي تمرُّ برمزٍ غيرِ ملكٍ
