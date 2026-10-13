# أدلّةُ إصلاحِ DISC-093 — سجلُّ ذرّيّةِ الاختباراتِ لكلِّ جلسة (WI-072 · W-312)

## التعريف
أدلّةُ البندِ `WI-072` (قيدُ `W-312`): نقلُ سجلِّ الذرّيّةِ والتصاريحِ المستهلَكةِ في
اختباراتِ `federal/executive/services` من مسارٍ ثابتٍ مشتركٍ إلى مجلّدِ أثرِ الجلسةِ الفريد
(`TEST_ARTIFACT_DIR`) — بعدَ قسمةِ نطاقِ `WI-026` بقرارِ المالكِ `Q-45`.

## النطاق
federal-executive · T0 (قابليّةُ القياس). ملفّاتُ هذا المجلّدِ وحدَها.
**لا يدخل:** `core/sovereignty/` ولا الإنتاج (`DISC-095`/`RK-023`).

## المالك
Perplexity Computer (مالكُ `WI-072`) · المراجع: مجلسُ المراجعة (GPT 5.6 + Grok 4.6 · `Q-43`).

## تاريخ الإنشاء
2026-10-13

## تاريخ آخر تعديل
2026-10-13 (W-312 · المرّةُ الأولى)

## المحتويات
| الملفّ | ما فيه |
|---|---|
| `results.tsv` | سطرُ النتيجةِ لكلِّ تشغيلٍ متزامنٍ بعدَ الإصلاحِ (8 تشغيلات) وعددُ `IdempotencyError` فيه |

- **البيئة:** فرعُ `wi-072-test-ledger-per-session` (قِيسَ على `8de0fed` في جلسةِ W-310 ثمّ حُفِظَ حتى دفعةِ IN_PROGRESS) · Python 3.12.13 · SQLite · معالِجان.

## الأوامر (تُعادُ كما هي)
```bash
source .venv/bin/activate
cd federal/executive/services
T=tests/test_r7d_federal_judiciary.py
# A بعدَ الإصلاح: عمليّتانِ متزامنتانِ في المجلّدِ نفسِه (مرّتان) — الملفُّ كاملًا (27)
for r in 1 2; do (python -m pytest $T -q -p no:cacheprovider > /tmp/A${r}a.log 2>&1) & (python -m pytest $T -q -p no:cacheprovider > /tmp/A${r}b.log 2>&1) & wait; done
# R4 بعدَ الإصلاح: أربعُ عمليّاتٍ متزامنةٍ في المجلّدِ نفسِه
for i in 1 2 3 4; do (python -m pytest $T -q -p no:cacheprovider > /tmp/R4_p$i.log 2>&1) & done; wait
grep -c "IdempotencyError: المفتاح" /tmp/A*.log /tmp/R4_p*.log
# الحرسُ وتحوّرُه
python -m pytest tests/test_w308_test_ledger_is_per_session.py -q -p no:cacheprovider
```

## النتيجةُ المقيسة — قبلُ (`W-308`) وبعدُ (`W-312`)
| التجربة | قبلَ الإصلاح (`docs/audit/evidence/W-308/`) | بعدَ الإصلاح (`results.tsv`) |
|---|---|---|
| A · عمليّتانِ متزامنتانِ في المجلّدِ نفسِه | 3 إخفاقاتٍ من 50 · كلُّها `IdempotencyError` | **0 من 108** (4 تشغيلات × 27) |
| R4 · أربعُ عمليّاتٍ متزامنة | 28 إخفاقًا من 108 · كلُّها `IdempotencyError` | **0 من 108** |

(في `W-308` استُبعِدَ اختباران من A لأنَّ النسخةَ المعزولةَ في B تُسقِطُهما؛ وهنا لا نسخةَ معزولةً فشُغِّلَ الملفُّ كاملًا.)

## الحرسُ وتحوّرُه
- `tests/test_w308_test_ledger_is_per_session.py` ⇒ **3 passed**.
- التحوّر: إعادةُ `_cleanup_test_ledger(workspace)` (المسارِ القديم) في `pytest_sessionstart`
  و`pytest_sessionfinish` ⇒ **2 failed, 1 passed** — يسقطُ اختبارُ موضعِ السجلِّ واختبارُ سباقِ
  الجلستَينِ الحقيقيّتَين؛ ويبقى اختبارُ التنظيفِ ناجحًا لأنّه يفحصُ الدالّةَ لا موضعَ النداء.

## حدودُ هذا الدليل
- الأزمنةُ تتأثّرُ بحِملِ معالِجَين ولا يُبنى عليها حكم.
- اختبارُ السباقِ يكتبُ ملفًّا مؤقّتًا `tests/test_zz_wi072_race_probe_tmp.py` ويمحوه في `finally`.
- لا يُغيِّرُ هذا الإصلاحُ شيئًا في الإنتاج: سجلُّ الإنتاجِ في `.runtime/sovereignty/` كما كان.
