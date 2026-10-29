# أدلّةُ أحكامِ CI — دفعةُ W-727 (واجبُ N+1 لدفعةِ W-726)

## التعريف

حمولاتُ وظائفِ التشغيلاتِ الأربعةِ المقروءةِ بالفاحصِ
(`ci_verdict_readability.py --from-json --require-readable --expect-sha bb7eeb316e5bdd87e2a891742f63c6030a823027`)
على رأسِ دفعةِ W-726 قبلَ الدمجِ وبعدَه. تُقيَّدُ في دفعةِ العملِ هذه لا في دفعةٍ خاصّة (التوجيهُ 28 § 2 بند 1).

## النطاق

| الملفّ | التشغيل | العقدة | الحكم |
|---|---|---|---|
| `pr192_ci_jobs.json` | `40829188714` (AMOS-Federation CI · PR #192) | `bb7eeb31` | مقروءٌ وأخضرُ 13/13 |
| `pr192_truth_matrix_jobs.json` | `40829184424` (مصفوفةُ الحقيقةِ · PR #192) | `bb7eeb31` | مقروءٌ وأخضرُ 1/1 |
| `main_bb7eeb31_ci_jobs.json` | `40831369041` (AMOS-Federation CI · main) | `bb7eeb31` | مقروءٌ وأخضرُ 13/13 |
| `main_bb7eeb31_truth_matrix_jobs.json` | `40831369076` (مصفوفةُ الحقيقةِ · main) | `bb7eeb31` | مقروءٌ وأخضرُ 1/1 |

## المالك

Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-727).

## تاريخ الإنشاء

2026-10-29

## تاريخ آخر تعديل

2026-10-29

## المحتويات

- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `main_bb7eeb31_ci_jobs.json` — ملف تابع
- `main_bb7eeb31_truth_matrix_jobs.json` — ملف تابع
- `pr192_ci_jobs.json` — ملف تابع
- `pr192_truth_matrix_jobs.json` — ملف تابع
