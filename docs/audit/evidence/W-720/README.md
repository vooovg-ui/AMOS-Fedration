# قيدُ W-720 — أدلّةُ بندِ شِفرةِ WI-116 (استردادُ التنفيذِ لنوعِ EXECUTION · D24-R2)

## التعريف
مخرجاتُ التشغيلِ الخامُّ لبندِ الشِّفرةِ وفقَ [`EXECUTION_RECOVERY_DESIGN.md`](../../EXECUTION_RECOVERY_DESIGN.md): الأجزاءُ الأربعةُ (أ) سقفٌ 1 لـEXECUTION من التوقيع (ب) مُزوّدُ EXECUTION لا يُقِرُّ بالتفرّد (ج) علامةُ «بدأ التنفيذ» ذرّيّةٌ قبلَ dispatch (د) `recover()` بشرطِ عمرِ العلامةِ > 30 ث.

## النطاق
مسبارُ القبولِ الدائمُ (`federal/executive/services/tests/test_execution_recovery.py` — سقوطٌ حقيقيٌّ بـ`os._exit(137)`) · فحوصُ الصادرِ (`tests/sovereignty/test_outbox_execution_attempts.py`) · وإعادةُ تشغيلِ مسبارِ W-719 على الشِّفرةِ الجديدة. لا جولةَ مجلس.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-720).

## تاريخ الإنشاء
2026-10-28

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | الأمرُ المولِّد |
|---|---|---|
| `session_head.txt` | قاعدةُ الفرعِ (main) عندَ التشغيل — والشِّفرةُ في شجرةِ العملِ قبلَ الإيداع | `git rev-parse HEAD > docs/audit/evidence/W-720/session_head.txt` |
| `recovery_probe_run.txt` | مسبارُ القبول: 7 passed | `cd federal/executive/services && ../../../.venv/bin/python -m pytest tests/test_execution_recovery.py -v -p no:cacheprovider > ../../../docs/audit/evidence/W-720/recovery_probe_run.txt 2>&1` |
| `outbox_attempts_run.txt` | فحوصُ سقفِ الصادر: 7 passed | `.venv/bin/python -m pytest tests/sovereignty/test_outbox_execution_attempts.py -v -p no:cacheprovider > docs/audit/evidence/W-720/outbox_attempts_run.txt 2>&1` |
| `w719_probe_rerun.txt` | مسبارُ W-719 (الذي قاسَ الثغراتِ قبلَ الشِّفرة) مُعادٌ على الشِّفرةِ الجديدة: 5 failed — كلٌّ عندَ بوّابتِه | `cd federal/executive/services && ../../../.venv/bin/python -m pytest -p tests.conftest ../../../docs/audit/evidence/W-719/probe_execution_crash.py -q -s -p no:cacheprovider > ../../../docs/audit/evidence/W-720/w719_probe_rerun.txt 2>&1` |

## قراءةُ إعادةِ مسبارِ W-719
مسبارُ W-719 يُثبِتُ سلوكَ ما **قبلَ** الشِّفرة، ففشلُه الآنَ هو المقصود — ولكلِّ حالةٍ بوّابتُها:

- **P1 غيرُ المتفرِّد**: dispatch_count=1 كما كان، لكنَّ `recover()` بلا `now` يُؤجِّلُ المهمّةَ (عمرُ العلامةِ < 30 ث) فتبقى `executing` ⇒ تأكيدُه `failed` يسقط — الجزءُ (د).
- **P1 المتفرِّد** و**P3** (يُدرِجُ بـ`provider_supports_idempotency=True`): `OutboxError` عندَ الإدراج — الجزءُ (ب).
- **P2** `advance` المباشر: `ExecutionRefusedError` — لا dispatch ثانٍ — الجزءُ (ج).

## الإعادة
الأوامرُ أعلاه على العقدةِ نفسِها. المسابرُ تكتبُ في قاعدةِ الاختبارِ التي يُهيِّئُها `tests/conftest.py` وفي مجلّدِ pytest المؤقّتِ فقط.

## تاريخ آخر تعديل
2026-10-28

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `outbox_attempts_run.txt` — ملف تابع
- `recovery_probe_run.txt` — ملف تابع
- `session_head.txt` — ملف تابع
- `w719_probe_rerun.txt` — ملف تابع
