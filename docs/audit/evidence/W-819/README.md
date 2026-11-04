# evidence/W-819 — قراراتُ Q-98 وتصميمُ الدفعةِ 2 وأدلّةُ شِفرتِها ومسبارُ log_cost (W-819 · W-820 · W-821)

## التعريف
أدلّةُ قيودِ W-819 (توثيق: نصُّ التوجيهِ 43 · Q-98 · تصميمُ § 7 · أحكامُ CI للدفعةِ 1 على main وPR #266 · لقطةُ البوّابةِ على `4e2b676a`) وW-820 (شِفرةُ الدفعةِ 2 من Q-83 (ج): الأسطحُ التسعةُ في `national_economy` تعبرُ `guard_declared` بأفعالِها الجديدةِ في `EXECUTIVE_ACTIONS` · والمسارُ الكاملُ للأسطحِ السبعةَ عشرَ) وW-821 (مسبارُ `log_cost` قراءةً فقط · DISC-160). تصنيفُ W-820 **C4** (يمسُّ `core/`) — لا VERIFIED بغيرِ المراجعِ أو المجلس.

## النطاق
- `OWNER_DIRECTIVE_43.md` — نصُّ التوجيهِ حرفيًّا.
- `decision_gate_measure_4e2b676a.txt` — لقطةُ البوّابةِ على `4e2b676a` (§ 0): الدَّينُ 76 · العابرُ 102 · W1 ‏11 · W2 ‏28 · W3 ‏37 · EXIT=0.
- `ci_w818_main/` · `ci_w818_pr266/` — أحكامُ CI للدفعةِ 1 (N+1): EXIT=0 ×4.
- `q98_engine_probe.py` + `q98_engine_probe_before.txt` (`verbs=9 mismatched=9` · EXIT=1) + `q98_engine_probe_output.txt` (9/9 · EXIT=0) — المسبارُ الخامُ قبلُ وبعد.
- `q98_mutation_probe.py` + `q98_mutation_output.txt` — الطفرات: `total=18 survived=0`.
- `caller_impact_scan.py` + `caller_impact_before/after.txt` — `ENGINE_CALLERS=0` قبلُ وبعد · `r8_r9_before/after.txt` ‏78 ⇒ 78 · `crossing_suites_after.txt` الملفّاتُ الأربعة.
- `d4_before_stdout.txt` · `d4_classification_before.txt` · `d4_after_stdout.txt` · `d4_classification_after.txt` — D-4 ‏69 ⇒ 60 (حرقٌ 9 · تصنيفٌ 0) على أساسِ `4e2b676a`.
- `services_full_suite.txt` — الحزمةُ الكاملة · و`services_full_suite_run1_fk_order.txt` — التشغيلُ الأوّلُ الساقطُ بترتيبِ الملفّاتِ (محفوظٌ لا ممحوّ).
- `postgresql_not_measured.txt` — ما لم يُقَس وسببُه.
- `log_cost_rejection_probe.py` + `log_cost_rejection_probe_output.txt` — مسبارُ Q-98 البند 3: الجوابُ نعم.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · WI-127 · WI-122).

## تاريخ الإنشاء
2026-11-04

## تاريخ آخر تعديل
2026-11-04

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `OWNER_DIRECTIVE_43.md` — وثيقة
- `caller_impact_after.txt` — ملف تابع
- `caller_impact_before.txt` — ملف تابع
- `caller_impact_scan.py` — أداة قياس
- `ci_w818_main` — مجلد فرعي
- `ci_w818_pr266` — مجلد فرعي
- `crossing_suites_after.txt` — ملف تابع
- `d4_after_stdout.txt` — ملف تابع
- `d4_before_stdout.txt` — ملف تابع
- `d4_classification_after.txt` — ملف تابع
- `d4_classification_before.txt` — ملف تابع
- `decision_gate_measure_4e2b676a.txt` — ملف تابع
- `log_cost_rejection_probe.py` — أداة قياس
- `log_cost_rejection_probe_output.txt` — ملف تابع
- `postgresql_not_measured.txt` — ملف تابع
- `q98_engine_probe.py` — أداة قياس
- `q98_engine_probe_before.txt` — ملف تابع
- `q98_engine_probe_output.txt` — ملف تابع
- `q98_mutation_output.txt` — ملف تابع
- `q98_mutation_probe.py` — أداة قياس
- `r8_r9_after.txt` — ملف تابع
- `r8_r9_before.txt` — ملف تابع
- `services_full_suite.txt` — ملف تابع
- `services_full_suite_run1_fk_order.txt` — ملف تابع
