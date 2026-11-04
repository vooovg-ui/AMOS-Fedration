# evidence/W-823 — أدلّةُ شِفرةِ الدفعةِ 3 من Q-83 (ج): أسطحُ الخزانةِ الثلاثة (W-823 · Q-99)

## التعريف
أدلّةُ قيدِ W-823: أسطحُ الخزانةِ الثلاثةُ في `national_economy` (`authorize_expenditure` · `authorize_procurement` ⇒ `award_procurement` · `authorize_transfer` فعلٌ جديد) تعبرُ عقدَ الخزانةِ `money_crossing_contract` بفاعلِ TREASURY، بتصميمِ `Q83C_LEXICON_TABLE_DESIGN.md` § 8 قبلَ الشِّفرة. **C4** — لا VERIFIED بلا مراجعٍ مستقلّ.

## النطاق
- `q99_engine_probe.py` + `q99_engine_probe_before.txt` (`verbs=3 mismatched=1` · `authorize_transfer` 10/10 ALLOW · EXIT=1) + `q99_engine_probe_after.txt` (3/3: TREASURY وحدَه ALLOW والتسعةُ DENY `R-003-1` · EXIT=0) — المسبارُ الخام.
- `q99_mutation_probe.py` + `q99_mutation_probe.txt` — `total=6 survived=0` (3 حذفُ قاعدة · 3 حذفُ عبور) · الملفُّ أُعيدَ مطابقًا بالبايت.
- `caller_impact_scan.py` + `caller_impact_before/after.txt` — `ENGINE_CALLERS=0` قبلُ وبعد.
- `affected_suites_before.txt` · `affected_suites_after.txt` — الحزمُ المتأثّرة (139 ⇒ 169 · q18 ‏111 ⇒ 117).
- `guards_raw_diff.txt` — الفرقُ الخامُ للحرّاسِ الأربعةِ مقابلَ `ba1cac8f` (Q-99 البند 3 · سابقةُ DISC-155).
- `d4_after_stdout.txt` · `d4_classification_after.txt` — D-4 ‏60 ⇒ 57 (حرقٌ 3 · تصنيفٌ 0) · و«قبل» في `evidence/W-822/`.
- `root_collect_diff.txt` — مُجمَّعُ الجذرِ 3614 ⇒ 3639 بالملفّ.
- `services_full_suite.txt` — حزمةُ الخدماتِ الكاملة بعدَ الشِّفرة.
- `postgresql_not_measured.txt` — ما لم يُقَس وسببُه.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · WI-127).

## تاريخ الإنشاء
2026-11-04

## تاريخ آخر تعديل
2026-11-04

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `affected_suites_after.txt` — ملف تابع
- `affected_suites_before.txt` — ملف تابع
- `caller_impact_after.txt` — ملف تابع
- `caller_impact_before.txt` — ملف تابع
- `caller_impact_scan.py` — أداة قياس
- `d4_after_stdout.txt` — ملف تابع
- `d4_classification_after.txt` — ملف تابع
- `guards_raw_diff.txt` — ملف تابع
- `postgresql_not_measured.txt` — ملف تابع
- `q99_engine_probe.py` — أداة قياس
- `q99_engine_probe_after.txt` — ملف تابع
- `q99_engine_probe_before.txt` — ملف تابع
- `q99_mutation_probe.py` — أداة قياس
- `q99_mutation_probe.txt` — ملف تابع
- `root_collect_diff.txt` — ملف تابع
- `services_full_suite.txt` — ملف تابع
