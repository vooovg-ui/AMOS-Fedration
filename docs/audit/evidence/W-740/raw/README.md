# خاماتُ قياسِ دفعةِ W-740 — السطحانِ 2 و4 لـWI-114

## التعريف
مخرجاتٌ خامٌ مقيسةٌ لا يُعدَّلُ محتواها بعدَ القياسِ: الحزمةُ الكاملةُ، الطفراتُ الأربعُ، وفحصُ الكياناتِ.

## النطاق
- `full_services_suite.txt` — 1802 نجحَت · 53 متخطاة · 0 فشل (بلا PostgreSQL · بلا --cov).
- `mutation_a..d_*.txt` — الطفراتُ أ/ب/ج/د: فشلُ الفحوصِ الحارسةِ عندَ إفسادِ كلِّ آليةٍ (لا ناجحًا بلا حارسٍ).
- `scan_canary_crossings.json` — لكلِّ نداءٍ عبورٌ واحدٌ على الأكثرِ (لا تعاقبَ داخلَ النداءِ الواحدِ).

## المالك
المنسِّقُ (قيدُ W-740).

## تاريخ الإنشاء
2026-10-29

## تاريخ آخر تعديل
2026-10-29 (W-740 — القيدُ نفسُه)

## المحتويات
- `full_services_suite.txt` — تشغيلُ `pytest tests/ -q` للحزمةِ الكاملةِ.
- `mutation_a_drop_human_approval_passing.txt` · `mutation_b_unconditional_approved.txt` · `mutation_c_drop_issued_for_check.txt` · `mutation_d_drop_surface4_compensator.txt` — خرجاتُ الطفراتِ.
- `scan_canary_crossings.json` — خرجُ الفحصِ.
