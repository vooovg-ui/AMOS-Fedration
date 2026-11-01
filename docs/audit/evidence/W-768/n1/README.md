# README — حكما CI للطلب #237 (واجبُ N+1 · W-768)

## التعريف
حمولتا وظائفِ CI الخامّتانِ للطلب #237 على `53bb0cc5`، ومخرجُ الفاحصِ الحرفيُّ لكلٍّ منهما.

## النطاق
- `pr237_ci_jobs.json`: تشغيلُ 41238284440 · 13 وظيفةً `success` على العقدةِ نفسِها · `pr237_ci_jobs.checker.txt`: EXIT=0.
- `pr237_matrix_jobs.json`: تشغيلُ 41238279767 · وظيفةٌ واحدة `success` · `pr237_matrix_jobs.checker.txt`: EXIT=0.
- مُستجلَبةٌ بـgh api، ولا توكنَ فيها. والفاحص: `ci_verdict_readability.py --from-json … --require-readable --expect-sha 53bb0cc5…`.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-768 · WI-100)

## تاريخ الإنشاء
2026-11-01

## تاريخ آخر تعديل
2026-11-01

## المحتويات
- `pr237_ci_jobs.json` · `pr237_ci_jobs.checker.txt` · `pr237_matrix_jobs.json` · `pr237_matrix_jobs.checker.txt`
