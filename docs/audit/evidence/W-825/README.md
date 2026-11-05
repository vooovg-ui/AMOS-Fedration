# evidence/W-825 — أدلّةُ شِفرةِ Q-99 البند 6: ملفّا عبورِ الأسطحِ السبعةَ عشرَ في حزمةِ PostgreSQL (W-825)

## التعريف
أدلّةُ قيدِ W-825: إدخالُ `tests/test_r8_q97_federal_state_crossing.py` و`tests/test_r9_economy_q98_crossing.py` إلى حزمةِ `services-postgres` في `tools/governance/verify_cross_system_suites.py` مع مُلحَقِ الجلسة `tests.pg_session_dialect` (يفرضُ لهجةَ PostgreSQL على كلِّ اختبار)، بتصميمِ `docs/audit/Q99_6_POSTGRES_CROSSING_SUITE_DESIGN.md` قبلَ الشِّفرة. تشديدُ بوّابةٍ بلا إضعافِ فحص · لا VERIFIED بلا مراجعٍ مستقلّ.

## النطاق
- `run_pg_suite.py` — يستدعي `run_suite` من الأداةِ نفسِها على حزمةِ `services-postgres`.
- `pg_suite_with_postgres.txt` — PostgreSQL 18.6 محلّيّ: **95 passed · 0 skipped** · كلُّ الـ95 مفحوصةُ اللهجة.
- `pg_suite_without_postgres.txt` — بلا بيئةِ PostgreSQL: **رمزُ خروج 4 · سقوطٌ لا تخطٍّ**.
- `postgres_suite_files_raw_diff.txt` — قائمةُ الملفّاتِ قبلُ (3) وبعدُ (5 + المُلحَق) والفرقُ الخام.
- `q99_6_mutation_probe.py` + `q99_6_mutation_probe.txt` — ستُّ طفراتٍ كلُّها مقتولة · الملفّاتُ أُعيدَت مطابقةً بالبايت.
- `d4_after_stdout.txt` — D-4 ‏57 ⇒ 57.
- `root_collect_diff.txt` — مُجمَّعُ الجذرِ 3639 ⇒ 3644 بالملفّ.
- `services_full_suite.txt` — حزمةُ الخدماتِ الكاملة (SQLite) بعدَ الشِّفرة.
- ما لم يُقَس: PostgreSQL 17 (حكمُ وظيفةِ CI وحدَه) · أسطحُ الخزانةِ الثلاثةُ على PostgreSQL · الإنتاج.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · WI-127).

## تاريخ الإنشاء
2026-11-05

## تاريخ آخر تعديل
2026-11-05

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `d4_after_stdout.txt` — ملف تابع
- `pg_suite_with_postgres.txt` — ملف تابع
- `pg_suite_without_postgres.txt` — ملف تابع
- `postgres_suite_files_raw_diff.txt` — ملف تابع
- `q99_6_mutation_probe.py` — أداة قياس
- `q99_6_mutation_probe.txt` — ملف تابع
- `root_collect_diff.txt` — ملف تابع
- `run_pg_suite.py` — أداة قياس
- `services_full_suite.txt` — ملف تابع
