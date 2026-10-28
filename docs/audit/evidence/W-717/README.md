# قيدُ W-717 — أدلّةُ تحليلِ WI-118 (تغطيةُ المُنادين لكتاباتِ persistent.py)

## التعريف
أدلّةُ القياسِ الخامُّ لوثيقةِ [`D4_CALLERS_COVERAGE_ANALYSIS.md`](../../D4_CALLERS_COVERAGE_ANALYSIS.md) — تحليلٌ قياسيٌّ بلا شِّفرةٍ بأمرِ المالكِ في التوجيهِ 24 § 1. النتيجةُ سؤالٌ للمالكِ (Q-75) ولا يُغيَّرُ مقياسُ D-4.

## النطاق
مخرجاتُ جردِ D-4 الخامُّ على العقدةِ المقيسة · أداةُ قياسِ المُنادين (دليلٌ لا بوّابة) ومخرجُها نصًّا وحِملًا · رأسُ الشجرةِ — لا شِّفرةَ إنتاجٍ ولا جولةَ مجلسٍ.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-717).

## تاريخ الإنشاء
2026-10-28

## العقدةُ المقيسة
`e8624c2c076d6cdac139df4edc451e00fe6066d3` (main بعدَ W-716 · انظر `session_head.txt`).

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | الأمرُ المولِّد | الخروج |
|---|---|---|---|
| `session_head.txt` | رأسُ الشجرةِ عندَ القياس | `git rev-parse HEAD > session_head.txt` | 0 |
| `d4_inventory_raw.txt` | مخرجُ جردِ D-4 الخامُّ (121) | `.venv/bin/python tools/audit/sovereign_write_inventory.py > d4_inventory_raw.txt 2>&1; echo "exit=$?" >> d4_inventory_raw.txt` | 0 (مسجَّلٌ في آخرِ الملفّ) |
| `d4_inventory.json` | حِملُ الجردِ كاملًا | `.venv/bin/python tools/audit/sovereign_write_inventory.py --json d4_inventory.json` | 0 |
| `d4_callers_coverage.py` | أداةُ قياسِ المُنادين (دليلٌ · ليست بوّابة) | — | — |
| `callers_coverage.txt` | الجدولُ والسلاسلُ كاملةً لكلِّ مسار | `.venv/bin/python docs/audit/evidence/W-717/d4_callers_coverage.py --json docs/audit/evidence/W-717/callers_coverage.json > docs/audit/evidence/W-717/callers_coverage.txt 2>&1` | 0 |
| `callers_coverage.json` | الحِملُ نفسُه منظَّمًا (لكلِّ مسار: المدخلُ · نوعُه · المصادقةُ · السلسلةُ · (ت) · (ل)) | (الأمرُ السابق) | 0 |

## الإعادة
 الأوامرُ أعلاهُ من جذرِ المستودعِ على العقدةِ نفسِها تُعيدُ الأرقامَ نفسَها (الأداةُ حتميّةٌ:
لا شبكةَ ولا قاعدةَ ولا وقت). لا أنابيبَ (`|`) في أيِّ أمرٍ أُودِعَ مخرجُه — المخرجُ يُكتَبُ إلى الملفِّ مباشرةً
(درسُ W-716 في `session_measurements.txt`).

## ملاحظةُ تطويرِ الأداة
 المسودّةُ الأولى نسبَت `self.audit.append` في `core/crown/sovereign_session.py`
(صنفُه `CrownAudit`) إلى `PersistentAuditStore` لتطابقِ الاسم، وفاتَها `store.set_level` في `canary.py`
(اسمٌ محلّيٌّ يُسنَدُ من مُعيدٍ داخلَ الدالّة) واستيرادٌ محلّيٌّ يحجبُ دالّةً بالاسمِ نفسِه
(`governance/main.py::_activate_kill_switch_safe`). صُحِّحَت الثلاثةُ (نطاقُ الأسماءِ لكلِّ دالّة · سماتُ
`self` بصنفِها · تقديمُ الاستيرادِ المحلّيّ) قبلَ الإيداع — والمودَعُ هو المخرجُ المصحَّحُ وحدَه.

## ما لا تفعلُه هذه الدفعة
 لا شِّفرةَ إنتاجٍ · لا تعديلَ لأداةِ D-4 · لا جولةَ مجلسٍ.

## تاريخ آخر تعديل
2026-10-28

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `callers_coverage.json` — بيانات مهيكلة
- `callers_coverage.txt` — ملف تابع
- `d4_callers_coverage.py` — تحليلٌ قياسيٌّ لمساراتِ الاستدعاءِ العامةِ لمواقعِ كتابةِ persistent.py (WI-118) — قياسٌ لا حك…
- `d4_inventory.json` — بيانات مهيكلة
- `d4_inventory_raw.txt` — ملف تابع
- `session_head.txt` — ملف تابع
