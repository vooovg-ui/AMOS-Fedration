# evidence/W-763 — قياسُ الفاعلينَ الأربعةِ قبلَ التصميمِ والشِّفرة (بندُ C4)

## التعريف
أدلّةُ القيدِ W-763: تنفيذُ أمرِ المالكِ في التوجيهِ 35 § 1 (`Q-87`، «الفاعلون الأربعة»): «قبل الشفرة قِس استعمال HUMAN وSTATE وINSTITUTION في الإنتاج … واعرض ما قد ينكسر». هذا قياسٌ فقط، ولا تغييرَ في الشِّفرة.

## النطاق
قراءةٌ ساكنةٌ لشِفرةِ الإنتاج، وتجربةٌ مؤقّتةٌ على `core/constitutional_engine/rules.py` أُعيدَ الملفُّ بعدَها بايتًا (لم تُلتزَم). البندُ `WI-109` للقياس، وتُفتَحُ `WI-126` بحالةِ READY للإصلاح (C4).

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-763).

## تاريخ الإنشاء
2026-10-31

## تاريخ آخر تعديل
2026-10-31 (W-763 — الإنشاء)

## المحتويات
- `four_actor_usage.py` + `four_actor_usage.txt` — قياسٌ ساكنٌ على 265 ملفَّ إنتاج. لا مُنادٍ في الإنتاجِ يبني `Branch.STATE` أو `Branch.INSTITUTION`. الموضعُ الوحيدُ لكلٍّ منهما خريطةُ الطبقاتِ في `core/sovereignty/authority.py`. ويرِدُ `Branch.HUMAN` في الموضعِ نفسِه وفي استثناءِ الاستعادةِ في `rules.py:522`. ولا يرِدُ اسمُ أيٍّ منها نصًّا قربَ actor/branch (0). أمّا مداخلُها فديناميكيّةٌ فقط، وهي ثلاثة: `core/sovereignty/cli.py:242`، و`core/constitutional_engine/cli.py:85` (وفيهما `choices` من قِيَمِ `Branch` كلِّها)، و`sovereignty_bridge.py:360` (`Branch[self._actor]`). والمُصرِّحاتُ الأربعةَ عشرَ في الخدماتِ تستعملُ EXECUTIVE وJUDICIAL وTREASURY وROYAL وحدَها، بقراءةِ المنسِّقِ في هذه الجلسة.
- `experiment_rules.patch` — الرقعةُ التجريبيّة: STATE وINSTITUTION يُرفَضانِ بـR-003-1، وHUMAN يحتاجُ `human_approved` مع `human_approval_source` على الأفعالِ الحصريّةِ والماليّة، وROYAL بلا مرسومٍ يُرفَضُ على الحصريّة.
- `experiment_services_suite.txt` — حزمةُ الخدماتِ تحتَ الرقعة: **1871 passed · 53 skipped · 0 failed**، أي لا انكسارَ في الإنتاج.
- `experiment_root_suite.txt` — الجذرُ تحتَ الرقعة: **6 failed · 3095 passed · 1 skipped**. وما ينكسرُ:
  - 4 فحوصٍ (3 في `test_enforcement_integration.py` و1 في `test_supreme_authority.py`) تستعملُ STATE مثالًا لـ«فاعلٍ تابعٍ» ينفّذُ `execute_task`. ستتغيّرُ أمثلتُها بأمرِ المالك، ولا يُضعَفُ تأكيدُها.
  - 1 (`test_q3 … test_issue_ruling_is_denied_for_the_default_actor_and_allowed_for_judicial`) يتوقّعُ أن يُسمَحَ لـROYAL بلا مرسومٍ بـ`issue_ruling`، وهو نقيضُ القرارِ صراحةً.
  - 1 (`test_w099` طزاجةُ الأثرِ المولَّد): **لم يُنسَب** إلى الرقعة، فقد يكونُ تقادُمَ المصفوفةِ في شجرةِ العملِ وقتَ التشغيل. لم يُقَس منفصلًا.

## ما لم يُقَس
- استعمالُ واجهتَي `cli.py` فعلًا من مُشغِّلٍ بشريٍّ أو آليّ (لا سجلَّ تشغيلٍ في المستودع).
- القيمُ التي يمرّرُها مُنادو `SovereigntyBridge` في وقتِ التشغيلِ خارجَ الفحوص.
- فشلُ `test_w099` تحتَ الرقعةِ وحدَها.
