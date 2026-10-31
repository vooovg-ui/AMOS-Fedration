# evidence/W-762 — شِفرةُ إصلاحِ DISC-146: هويّةُ الإذنِ فريدةٌ لا زمنيّة

## التعريف
أدلّةُ القيدِ W-762: إصلاحُ `issue_permit` بأمرِ المالكِ `Q-87` (7) على تصميمِ `DISC146_PERMIT_IDENTITY_DESIGN.md` (W-761)، والمسبارُ نفسُه بعدَ الإصلاح، والطفرات، والحزمتان.

## النطاق
`core/sovereignty/enforcement.py` (سطرُ `permit_id` واستيرادُ `uuid`) · فحصانِ مُعدَّلانِ في `federal/executive/services/tests/test_2b_state_registry_sovereign.py` · ملفُّ فحوصٍ جديد `tests/sovereignty/test_disc146_permit_identity.py`. البندُ `WI-125`.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-762).

## تاريخ الإنشاء
2026-10-31

## تاريخ آخر تعديل
2026-10-31 (W-762 — الإنشاء)

## المحتويات
- `disc146_q12_probe_after.txt` — مسبارُ W-761 حرفيًّا بعدَ الإصلاح (`docs/audit/evidence/W-761/disc146_q12_probe.py`). القبلُ في `../W-761/disc146_q12_probe_before.txt`.
- `disc146_mutations.py` + `disc146_mutations.txt` — أربعُ طفراتٍ تُطبَّقُ نصًّا ويُستعادُ الملفُّ بايتًا: M1 المعرّفُ الزمنيّ (مقتولة) · M2 معرّفٌ ثابت (مقتولة) · M3a تعطيلُ `is_consumed` وحدَه (**حيّة**: `consume` يرفضُ الإعادةَ مستقلًّا فهي دفاعٌ مزدوجٌ لا ثغرة) · M3b تعطيلُ الاثنين (مقتولة). المجموعُ 3/4.
- `root_suite_after.txt` · `services_suite_after.txt` — الحزمتانِ كاملتَين بعدَ الشِّفرة: الخدماتُ 1871/53/0 · الجذرُ 3103 passed · 1 skipped · 4 failed، والأربعةُ فحوصُ وثائقَ على شجرةٍ ناقصةٍ وقتَ التشغيل (المصفوفةُ ورقمُ الحزمةِ وREADME لحظيٌّ وقصُّ ترويسة).
- `root_rerun_after_docs.txt` — الفحوصُ الأربعةُ نفسُها بعدَ إتمامِ الوثائقِ وتوليدِ المصفوفة.

## تعديلُ فحوصٍ قائمةٍ (مُعلَن)
- `test_permit_identity_has_one_second_granularity` ⇐ `test_permit_identity_is_unique_per_issue_not_per_second`: كانَ يُثبِتُ قيدَ Q-11 (إذنانِ في الثانيةِ نفسِها إذنٌ واحد)، ونقضَه المالكُ بـQ-87 (7)، فصارَ يُثبِتُ النقيضَ ويُضيفُ أنَّ الطابعَ الزمنيَّ غائب. تغييرُ عقدٍ بأمرٍ لا إضعاف.
- `test_two_distinct_transitions_on_one_target_show_the_constraint`: كانَ يقبلُ فرعَين بحسبِ التوقيت، وصارَ يشترطُ المرورَ وحدَه. أشدُّ لا أضعف.

## ما لم يُقَس
عددُ المُطبِّقاتِ غيرِ الذرّيّةِ في الإنتاج (P6 يُضاعِفُ الأثرَ فورًا بعدَ الإصلاح كما كانَ يُضاعِفُه بعدَ ثانيةٍ قبلَه · `DISC-148`) · السباقُ بينَ محاولتَين متزامنتَين على PostgreSQL.
