# evidence/W-774 — Q-87 (ج): الفاعلون الأربعة على الأفعالِ الحصريّة (WI-126 · شِفرة)

## التعريف
أدلّةُ قيدِ W-774: شِفرةُ القرارِ 5 من Q-87 في `core/constitutional_engine/rules.py::_r003_1` بنصِّ التصميمِ المودَعِ في W-766 (`docs/audit/Q87_FOUR_ACTORS_DESIGN.md` § 2): STATE وINSTITUTION يُضافانِ إلى `_NON_BRANCH_EXCLUDED` · HUMAN على الأفعالِ الحصريّةِ وأفعالِ المالِ غيرِ الدستوريّةِ يحتاجُ `human_approved=True` ومصدرًا موسومًا غيرَ فارغٍ في `metadata["human_approval_source"]` (قناةُ W-740) · ROYAL بلا مرسومٍ على فعلٍ حصريٍّ رفضٌ في `review` كما في `execute` · ROYAL بمرسومٍ لا يُمنَع · والأثرُ في المسارِ السياديِّ يبقى ADVISORY.

## النطاق
- `probe_before.txt` — مسبارُ W-747 (`evidence/W-747/engine_probe_exclusive_actors.py`) على الشجرةِ بلا الرقعة (main `8e57dd87`): ROYAL وHUMAN وSTATE وINSTITUTION 56/56 ALLOW على الحصريّة.
- `probe_after.txt` — المسبارُ نفسُه بعدَ الشِّفرة: الأربعةُ 0/56 · الفروعُ المالكةُ كما هي (6/6 · 14/14 · 21/21 · 15/15) · AGENT وSYSTEM 0/56 كما كانا.
- `mutations.txt` — طفرتانِ على المصدرِ ثمَّ إعادتُه (مطابقٌ بـ`cmp`): حذفُ STATE/INSTITUTION ⇒ 123 فشلًا · قبولُ `human_approved` بلا مصدر ⇒ 65 فشلًا.
- `d4_before.txt` · `d4_after.txt` — جردُ D-4 (`tools/audit/sovereign_write_inventory.py`): 267 موضعَ كتابة · 182 عمليّةً عامّةً مُغيِّرة · 94 تعبرُ الحدَّ · 7 مساراتٌ قديمةٌ مُغلَقة · 86 لا تعبرُ — قبلَ وبعدَ سواء (القاعدةُ في المحرّكِ لا في مواضعِ الكتابة).
- `root_suite_patch_before_test_updates.txt` — حزمةُ الجذرِ بالرقعةِ قبلَ تحديثِ الفحوص (بـ`python3` النظام): الكسورُ المتوقَّعةُ في § 3 + ما خرجَ عنها (`test_q68_4`) + فشولُ بيئةٍ قائمةٌ على الشجرةِ بلا الرقعةِ أيضًا (secret-scan ×3 · `test_enforcement_separation` ×3 لغيابِ `amos_federation` عن مسارِ النظام).
- `root_suite_after.txt` — حزمةُ الجذرِ بعدَ الشِّفرةِ والوثائق (`.venv/bin/python -m pytest tests/`).
- `services_suite_after.txt` — حزمةُ الخدمات (`federal/executive/services` · `.venv` · `PYTHONPATH=src`): 1875 نجحت · 53 مُتخطّاة · 0 فشل.

## المالك
Perplexity Computer (المنسِّق · WI-126) — والمراجعةُ للمالكِ ومجلسِ المراجعةِ حين تتوفّرُ العوائل (D30).

## تاريخ الإنشاء
2026-11-01

## تاريخ آخر تعديل
2026-11-01 (W-774 — الإنشاء)

## المحتويات
| الملف | الغرض |
|---|---|
| `probe_before.txt` · `probe_after.txt` | المسبارُ قبلَ/بعدَ |
| `mutations.txt` | الطفرتانِ وأثرُهما |
| `d4_before.txt` · `d4_after.txt` | جردُ D-4 قبلَ/بعدَ |
| `root_suite_patch_before_test_updates.txt` · `root_suite_after.txt` | حزمةُ الجذر |
| `services_suite_after.txt` | حزمةُ الخدمات |
