# قيدُ W-719 — أدلّةُ تصميمِ WI-116 (استردادُ التنفيذِ لنوعِ EXECUTION · D24-R2)

## التعريف
أدلّةُ القياسِ الخامُّ لوثيقةِ [`EXECUTION_RECOVERY_DESIGN.md`](../../EXECUTION_RECOVERY_DESIGN.md) — تصميمُ الخيارِ 1 بقرارِ المالكِ D24-R2 بمعيارِ قبولِه: مسلكُ استردادٍ مُعلَنٌ للمهمّةِ العالقةِ في EXECUTING ومسبارٌ يُسقِطُ العاملَ بينَ dispatch والتثبيت.

## النطاق
رأسُ الشجرةِ · مواضعُ السطورِ مُعادةُ القياسِ بأوامرَ · مسبارُ الجدوى (عمليّةٌ فرعيّةٌ تُنهي نفسَها بـ`os._exit(137)`) ومخرجُه خامًا — لا شِّفرةَ إنتاجٍ ولا جولةَ مجلس.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-719).

## تاريخ الإنشاء
2026-10-28

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | الأمرُ المولِّد (من جذرِ المستودع) |
|---|---|---|
| `session_head.txt` | رأسُ الشجرةِ عندَ القياس | `git rev-parse HEAD > docs/audit/evidence/W-719/session_head.txt` |
| `measurements.txt` | مواضعُ § 1-أ و§ 1-ب بـ`grep -n`/`sed -n` (الأوامرُ مطبوعةٌ قبلَ كلِّ مخرج) | `bash docs/audit/evidence/W-719/measure.sh > docs/audit/evidence/W-719/measurements.txt 2>&1` |
| `measure.sh` | أوامرُ القياس | — |
| `probe_execution_crash.py` | مسبارُ الجدوى (دليلٌ · ليسَ اختبارًا في الحزمة) | — |
| `probe_run.txt` | مخرجُ المسبارِ خامًا (5 passed · أسطرُ `[probe]` بالأرقام) | `cd federal/executive/services && ../../../.venv/bin/python -m pytest -p tests.conftest ../../../docs/audit/evidence/W-719/probe_execution_crash.py -q -s -p no:cacheprovider > ../../../docs/audit/evidence/W-719/probe_run.txt 2>&1` |

## الإعادة
الأوامرُ أعلاه على العقدةِ نفسِها تُعيدُ الأرقامَ نفسَها. المسبارُ يكتبُ في قاعدةِ الاختبارِ التي يُهيِّئُها `tests/conftest.py` وفي مجلّدٍ مؤقّتٍ لـpytest فقط، ولا يُعدِّلُ شِّفرة.

## تاريخ آخر تعديل
2026-10-28

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `measure.sh` — إعادةُ قياسِ مواضعِ § 1 من EXECUTION_RECOVERY_DESIGN.md على العقدةِ الحاليّة (W-719 · WI-116)
- `measurements.txt` — ملف تابع
- `probe_execution_crash.py` — مسبارُ جدوى WI-116: إسقاطُ العاملِ بينَ dispatch وتثبيتِ الحالة
- `probe_run.txt` — ملف تابع
- `session_head.txt` — ملف تابع
