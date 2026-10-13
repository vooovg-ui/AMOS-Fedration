# أدلّةُ تشخيصِ DISC-093 — سجلُّ ذرّيّةِ الاختباراتِ المشتركُ (W-308)

## التعريف
أدلّةُ تشخيصِ الإخفاقِ المتقطّعِ في `federal/executive/services/tests/test_r7d_federal_judiciary.py`
(`IdempotencyError: المفتاحُ «state_registry.institution.register:default:JUD-…» غيرُ محجوز`) —
بندُ `WI-071` · قيدُ `W-308`. تشخيصٌ بتجربةٍ تفاضليّةٍ، **لا إصلاح**.

## النطاق
audit-truth · T0 (قابليّةُ القياسِ: إخفاقٌ متقطّعٌ يُفسَّرُ بسببٍ مقيسٍ لا بإعادةِ تشغيل).
ملفّاتُ هذا المجلّدِ وحدَها. **لا يدخل:** أيُّ تعديلٍ في `conftest.py` أو في `core/sovereignty/idempotency.py`.

## المالك
Perplexity Computer (مالكُ `WI-071`) · المراجع: مجلسُ المراجعة (GPT 5.6 + Grok 4.6 · `Q-43`).

## تاريخ الإنشاء
2026-10-13

## تاريخ آخر تعديل
2026-10-13 (W-308 · المرّةُ الأولى)

## المحتويات
| الملفّ | ما فيه |
|---|---|
| `results.tsv` | سطرُ النتيجةِ لكلِّ تشغيلٍ (11 تشغيلًا) وعددُ أخطاءِ `IdempotencyError` فيه |
| `failure_signatures.txt` | كلُّ سطرِ `IdempotencyError` وكلُّ سطرِ `FAILED` مستخرجًا من سجلّاتِ التشغيلِ كما خرجَت |

- **البيئة:** استنساخٌ من `52093ba` (`origin/main` · قيدُ `W-307`) · Python 3.12.13 (`.venv` من `tools/dev/bootstrap.sh --with-tools`) · SQLite · لا PostgreSQL مُعلَن · معالِجان (`nproc` = 2).

## السببُ المقيس
1. `federal/executive/services/tests/conftest.py` السطر 41 يكتبُ `AMOS_DATABASE_URL` **دونَ شرط**
   إلى قاعدةٍ في `tempfile.mkdtemp(prefix="amos-services-tests-")` (السطر 38) — **فريدةٍ لكلِّ عمليّة**.
   فالفرضيّةُ المكتوبةُ في `DISC-093` (قاعدةُ SQLite مشتركةٌ `/tmp/amos_svc.db`) **منقوضةٌ**:
   المتغيّرُ المُصدَّرُ في أمرِ `W-295` يُكتَبُ فوقَه عندَ الاستيراد.
2. سجلُّ الذرّيّةِ في الاختباراتِ **مسارٌ ثابتٌ مشترك**: `pytest_sessionstart` (السطر 261) يضعُ
   `AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER` = `federal/executive/services/amos_federation_test_idempotency.json`،
   ويمحوه `_cleanup_test_ledger` عندَ بدءِ كلِّ جلسةٍ وعندَ انتهائها (السطر 248 · و`pytest_sessionfinish` السطر 270).
   ومثلُه ملفُّ التصاريحِ المستهلَكةِ `executive_core_consumed_permits.json` في المجلّدِ نفسِه (يُمحى بالدالّةِ نفسِها) — مشتركٌ كذلك، ولم يُقَسْ له أثرٌ منفصلٌ هنا.
3. `core/sovereignty/idempotency.py` يحفظُ السجلَّ كلَّه بقراءةٍ ثمّ كتابةٍ كاملةٍ (`_load`/`_save`)
   تحتَ قفلِ خيطٍ (`threading.RLock`) **لا قفلِ عمليّة**. فجلستانِ متزامنتانِ: إحداهما تمحو الملفَّ
   أو تكتبُ نسختَها فوقَ حجزِ الأخرى، فيصلُ `transition` إلى مفتاحٍ لم يَعُدْ في الملفّ ⇒ «غيرُ محجوز».

## التجربةُ التفاضليّة — الأوامر (تُعادُ كما هي)
```bash
source .venv/bin/activate
cd federal/executive/services
T=tests/test_r7d_federal_judiciary.py
# R4: أربعُ عمليّاتٍ متزامنةٍ · سجلٌّ مشترك · الملفُّ كاملًا (27 اختبارًا)
for i in 1 2 3 4; do (python -m pytest $T -q -p no:cacheprovider > /tmp/R4_p$i.log 2>&1) & done; wait
# اختباران يقرآنِ مصدرَ الحزمةِ بمسارٍ نسبيٍّ فيُخفقانِ في النسخةِ المعزولةِ وحدَها — يُستبعَدانِ من A وB وC معًا
DS="--deselect $T::test_07_case_lifecycle_is_ordered_with_no_force_transition --deselect $T::test_19_static_guards_forbid_parallel_executors_and_schema_rewrites"
# A: عمليّتانِ متزامنتانِ · سجلٌّ مشترك
(python -m pytest $T -q -p no:cacheprovider $DS > /tmp/A1.log 2>&1) & (python -m pytest $T -q -p no:cacheprovider $DS > /tmp/A2.log 2>&1) & wait
# B: عمليّتانِ متزامنتانِ · سجلٌّ منفصلٌ لكلٍّ (نسخةُ tests/ في مجلّدٍ مستقلٍّ ⇒ conftest يضعُ السجلَّ هناك)
for i in 1 2; do mkdir -p /tmp/isoB$i/svc && cp -r tests /tmp/isoB$i/svc/; done
(cd /tmp/isoB1/svc && python -m pytest $T -q -p no:cacheprovider $DS > /tmp/B1.log 2>&1) & (cd /tmp/isoB2/svc && python -m pytest $T -q -p no:cacheprovider $DS > /tmp/B2.log 2>&1) & wait
# C: ثلاثُ جلساتٍ متتاليةٍ · سجلٌّ مشترك
for i in 1 2 3; do python -m pytest $T -q -p no:cacheprovider $DS > /tmp/C$i.log 2>&1; done
grep -c "IdempotencyError: المفتاح" /tmp/{R4_p1,R4_p2,R4_p3,R4_p4,A1,A2,B1,B2,C1,C2,C3}.log
```

## النتيجةُ المقيسة (`results.tsv`)
| التجربة | الإعداد | الإخفاقات | منها `IdempotencyError` |
|---|---|---|---|
| R4 | سجلٌّ مشتركٌ · 4 متزامنة | 28 (5 · 10 · 5 · 8) من 108 | **28** |
| A | سجلٌّ مشتركٌ · 2 متزامنتان | 3 (2 · 1) من 50 | **3** |
| B | سجلٌّ منفصلٌ · 2 متزامنتان | **0** من 50 | 0 |
| C | سجلٌّ مشتركٌ · 3 متتالية | **0** من 75 | 0 |

كلُّ إخفاقٍ في R4 وA هو `IdempotencyError` «غيرُ محجوز» (31 من 31)، والاختبارُ المُخفِقُ يتغيّرُ
من تشغيلٍ لآخر (سباقٌ لا عيبٌ في اختبارٍ بعينه). الفارقُ الوحيدُ بينَ A وB هو موضعُ ملفِّ السجلّ.

## حدودُ هذا الدليل
- قيسَ على معالِجَينِ؛ الأزمنةُ تتأثّرُ بالحِمل ولا يُبنى عليها حكم.
- لم يُقَسْ في CI: وظائفُ CI تُشغِّلُ الحزمةَ بعمليّةٍ واحدةٍ (لا `pytest-xdist` في `requirements-dev.txt`
  ولا في `ci.yml`)، فالسباقُ لا يظهرُ إلّا بتشغيلٍ محلّيٍّ متوازٍ — كما حدثَ في `W-295`.
- لا إصلاحَ هنا: `federal/executive/services/tests/conftest.py` محجوزٌ لـ`WI-026` (`IN_REVIEW`)؛ والإصلاحُ بندُ `WI-072` (`PROPOSED`).
