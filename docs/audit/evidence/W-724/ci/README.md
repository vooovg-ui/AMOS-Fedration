# أدلّةُ أحكامِ CI — دفعةُ W-724 (واجبُ N+1 لدفعةِ W-723)

## التعريف

حمولاتُ وظائفِ التشغيلاتِ الأربعةِ المقروءةِ بالفاحصِ
(`ci_verdict_readability.py --from-json --require-readable --expect-sha 2dc40c016a08ac1f14f3daac4118b9953b27e63d`)
على رأسِ دفعةِ W-723 قبلَ الدمجِ وبعدَه. تُقيَّدُ في دفعةِ العملِ هذه لا في دفعةٍ خاصّة (التوجيهُ 28 § 2 بند 1).

## النطاق

| الملفّ | التشغيل | العقدة | الحكم |
|---|---|---|---|
| `pr189_ci_jobs.json` | `40765878195` (AMOS-Federation CI · PR #189) | `2dc40c01` | مقروءٌ وأخضرُ 13/13 |
| `pr189_truth_matrix_jobs.json` | `40765870589` (مصفوفةُ الحقيقةِ · PR #189) | `2dc40c01` | مقروءٌ وأخضرُ 1/1 |
| `main_2dc40c01_ci_jobs.json` | `40768067876` (AMOS-Federation CI · main) | `2dc40c01` | مقروءٌ وأخضرُ 13/13 |
| `main_2dc40c01_truth_matrix_jobs.json` | `40768067597` (مصفوفةُ الحقيقةِ · main) | `2dc40c01` | مقروءٌ وأخضرُ 1/1 |

## المالك

Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-724).

## تاريخ الإنشاء

2026-10-29

## تاريخ آخر تعديل

2026-10-29

## المحتويات

- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `main_2dc40c01_ci_jobs.json` — ملف تابع
- `main_2dc40c01_truth_matrix_jobs.json` — ملف تابع
- `pr189_ci_jobs.json` — ملف تابع
- `pr189_truth_matrix_jobs.json` — ملف تابع
