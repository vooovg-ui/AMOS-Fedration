# evidence/W-764/ci — أحكامُ CI لدفعةِ W-761..W-763 (واجبُ N+1)

## التعريف
حمولاتُ وظائفِ CI الخامّةُ ومخرجاتُ الفاحصِ الحرفيّةُ للطلبَين #232 (أحمرُ · أُغلِق) و#233 (أخضرُ · دُمِجَ بالتقديمِ السريعِ إلى `614b5233`).

## النطاق
قراءةُ حكمٍ لا دفعُ عمل. الحمولاتُ مُستجلَبةٌ بـgh api فقط، ولا توكنَ فيها.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-764 · WI-100).

## تاريخ الإنشاء
2026-10-31

## تاريخ آخر تعديل
2026-10-31 (W-764 — الإنشاء)

## المحتويات
- `pr232_red_jobs.json` — تشغيلُ 41208615476 على `938e23cc`: `Lint (ruff)` فشلَ (`ruff format --check` على `tests/test_2b_state_registry_sovereign.py`)، و`Tests` و`Cross-System Suites` تُخُطِّيَتا. الفاحص: EXIT=1.
- `pr232_matrix_jobs.json` — تشغيلُ 41208613428: 1/1 أخضر. الفاحص: EXIT=0. ولا يُغني عن الأحمر.
- `pr233_jobs.json` — تشغيلُ 41209262463: 13/13 أخضرُ على العقدةِ نفسِها. الفاحص: EXIT=0.
- `pr233_matrix_jobs.json` — المصفوفة: أخضر. الفاحص: EXIT=0.
- لكلِّ حمولةٍ `.checker.txt` بمخرجِ `ci_verdict_readability.py --from-json … --require-readable --expect-sha …` وسطرِ EXIT.
