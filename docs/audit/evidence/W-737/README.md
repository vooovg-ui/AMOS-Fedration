# قيدُ W-737 — تصميمُ WI-114 السطحَين 2 و4 بعدَ D25-1 (ورقٌ · لا شِفرة)

## التعريف
أدلّةُ تصميمِ عبورِ `reset_kill_switch` (السطح 2 · `lower_kill_switch`) و`check_gate` (السطح 4 · `promote_model`) بدليلِ ملكٍ موسومٍ بالمصدرِ عبرَ الجسر — `docs/audit/A1A_CANARY_CROSSING_DESIGN.md` § 7.

## النطاق
قياسٌ نصّيٌّ ومسبارٌ للمحرّكِ وحدَه. لا تغييرَ في الشِّفرةِ ولا في `core/` (K1). السؤالُ Q-82 والاكتشافُ DISC-143 مقيَّدانِ في القيدِ نفسِه.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-737 · البندُ WI-114).

## تاريخ الإنشاء
2026-10-29

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | النتيجة المقيسة |
|---|---|---|
| `design_measurements.txt` | 11 أمرًا ومخرجُها خامًا على HEAD القيد | لا `human_approved`/`criticality` في `federal` إلا تعليقًا · نداءاتُ `reset_kill_switch(` 42 (38 في 11 ملفَّ فحص) · `check_gate(` 4 |
| `engine_probe_surfaces_2_4.py` | مسبارُ `ConstitutionalEngine.evaluate` على سجلٍّ مؤقّت | — |
| `engine_probe_output.txt` | مخرجُه | 108 صفوف · `lower_kill_switch`/`promote_model` بموافقةٍ و`normal` ⇒ ALLOW (المستويات 0 و3 و5) · بلا موافقة ⇒ DENY `R-008-3`/`R-001-1` · `fateful` ⇒ DENY `R-003-3` ولو وُقِّع · توقيعٌ مختلَقٌ يُسقِطُ `R-003-4` (DISC-143) |
| `ci/` | واجبُ N+1 لدفعةِ W-736 (PR #198) | حمولاتُ CI والمصفوفةِ على `ad67494c` وأحكامُ الفاحصِ EXIT=0 — التفصيلُ في `ci/README.md` |

## ما لم يُقَس
- (ج) من D25-1: أنَّ رمزَ الملكِ يحملُه إنسانٌ فعلًا.
- المسبارُ لا يمرُّ بالجسرِ ولا بالحدّ؛ ولا طلبَ HTTP في هذا القيد.
- `kill_switch_level` لا يُحقَنُ في الإنتاج (DISC-099 · WI-085 · Q-79).

## تاريخ آخر تعديل
2026-10-29 (W-737 — القيدُ نفسُه)

## المحتويات
- `README.md` — بطاقةُ هويّةِ هذا المجلد
- `design_measurements.txt` · `engine_probe_surfaces_2_4.py` · `engine_probe_output.txt`
- وأُعيدَ توليدُ `docs/audit/measurements/final_audit_p14.json` بأمرِه (‏Q-82 جعلَ الأسئلةَ 82 — عقدُ النَّسَب)
