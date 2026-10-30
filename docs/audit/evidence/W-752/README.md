# evidence/W-752 — WI-085 المرحلةُ الأولى: مراقبةُ زرِّ التوقّفِ بلا منع (Q-79 · تصميمُ § 10)

## التعريف
أدلّةُ القيدِ W-752: شِفرةُ المرحلةِ الأولى لـWI-085 بقرارِ المالكِ Q-79 («أوافق على توصيتك (ب · م2 · غ1) بشرط مرحلة مراقبة»)
وبنصِّ التوجيهِ 32 § 1: «حقن المستوى يسجّل ما كان سيمنعه، بلا منع». والتصميمُ مودَعٌ قبلَها في W-751 (`WI085_KILL_SWITCH_INJECTION_DESIGN.md` § 10).

## النطاق
البوّابةُ تقرأُ مستوى المادةِ الثامنةِ من مصدرٍ مُسجَّلٍ وتُسجِّلُ «ما كانَ سيمنعُه» — **ولا تمنع**. لا تغييرَ في `rules.py`
ولا في `KILL_SWITCH_BLOCKS` ولا في `persistent.py` ولا في K1. ولا VERIFIED: البندُ حسّاسٌ سياديًّا والمراجعةُ المستقلّةُ معلَّقة (D30 · DISC-144).

## المالك
المنسِّقُ (Perplexity Computer) — قيدُ W-752 (البندُ WI-085).

## تاريخ الإنشاء
2026-10-30

## تاريخ آخر تعديل
2026-10-30 (W-752 — الإنشاء)

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `mutate.sh` — طفراتُ المرحلة (كلٌّ يُعكَسُ بعدَ قياسِه)
- `mutations.txt` — مخرجُها الحرفيّ
- `probe_read_cost.py` — مسبارُ كلفةِ القراءةِ التقريبيّ (بطاقتُه في رأسِه)
- `probe_read_cost.txt` — مخرجُه
- `services_suite.txt` — سطرُ خلاصةِ حزمةِ الخدمات
- `root_suite.txt` — سطرُ خلاصةِ حزمةِ الجذر

## ما نُفِّذ
| الموضع | التغيير |
|---|---|
| `core/sovereignty/kill_switch_source.py` (جديد) | `KillSwitchLevelSource` · `LevelReading` · `resolve_reading` بغ1 (no_source/error/unknown ⇐ 5 · والعطلُ يُسجَّلُ) · `KillSwitchObservation` · `observe` (الأعلى · الحكمُ من `_r008_2` على نسخة) · `KILL_SWITCH_INJECTION_MODE = "OBSERVE"` |
| `core/sovereignty/gateway.py` | `register_kill_switch_source` · `kill_switch_observations` · `kill_switch_observation_errors` · الملاحظةُ بعدَ `evaluate` في review/sovereign/subordinate — الحكمُ يعودُ كما هو |
| `executive_core/kill_switch_level_source.py` (جديد) | `PersistentKillSwitchLevelSource` يقرأُ `system_state` بلا إنشاء · `level_from_stored` (constitutional/legacy_name/unknown) · المُصرِّفُ `amos.kill_switch.observe` (WARNING · JSON) |
| `executive_core/sovereignty_bridge.py` | `_build_gateway` يُسجِّلُ المصدرَ والمُصرِّف |

## المقيس
- **الفحوص:** `tests/sovereignty/test_w752_kill_switch_observe.py` 25 ✓ · `federal/.../tests/test_w752_kill_switch_observe.py` 20 ✓
  — منها **مسبارُ HTTP**: `POST /v1/kill-switch` halt ⇐ `POST /v1/specialization/exam` يعودُ 200 (لا منع) وتُسجَّلُ ملاحظةُ
  `record_curriculum_step` بـ`request_level=0` و`effective_level=4`.
- **الطفراتُ 8/8 مقتولة** (`mutations.txt`): نزعُ الملاحظةِ من المسارِ التابع · المستوى = مستوى الطلبِ وحدَه · غيابُ المصدرِ يُقرأُ 0 ·
  المراقبةُ تمنع · عطلُ المُصرِّفِ بلا عدّ · القراءةُ بـ`get()` · الجسرُ لا يُسجِّل · halt ⇐ 3.
- **الكلفةُ (تقريبيّة · SQLite):** قراءةٌ ≈0.35 ms · `review` ≈0.62 ⇐ ≈1.16 ms (فرقٌ ≈0.55 ms/عبور).
- **D-4 = 92** بلا تغيير (`decision_gate.py --measure`): لا سطحَ عامًّا جديدًا يكتب.
- **الحزم:** انظرِ `services_suite.txt` و`root_suite.txt`.

## ما لم يُقَس
- **المنعُ لم يُفعَّل** — بقرارِ المالك؛ يُفعَّلُ بعدَ مراجعةِ سجلِّ `amos.kill_switch.observe`.
- **م2 فجوةٌ معلَنة:** الكاتبُ يقبلُ الأسماءَ الأربعةَ وحدَها، فالمستوى المقروءُ اليومَ `legacy_name` مترجَمٌ لا مخزَّن (§ 10.4).
- `kill_switch_observations` في الذاكرةِ بلا سقف: عندَ halt طويلٍ يزيدُ بكلِّ عبورٍ ممنوعٍ نظريًّا (1000 من 1000 في المسبار) — يُعالَجُ في دفعةِ المنعِ أو بقرار.
- الصفُّ الغائبُ يُقرأُ 5 فيُسجِّلُ كلَّ عبورٍ في جدولِ التجميدِ حتى يُنشأَ الصفّ — سلوكٌ مقصودٌ بغ1 لكنَّ حجمَه في الإنتاجِ غيرُ مقيس.
- PostgreSQL وحملٌ حقيقيّ — لم يُشغَّلا هنا.
- المسارُ الملكيُّ مُلاحَظٌ في الفحصِ لا في الإنتاج (لا مرسومَ حيًّا).

## مسُّ ملفٍّ تحتَ مُطالَبةِ بندٍ آخر

`sovereignty_bridge.py` مُطالَبٌ به في `WI-114` (IN_REVIEW). هَنْكُ W-752 فيه سطرانِ في `_build_gateway`
(تسجيلُ `PersistentKillSwitchLevelSource()` و`log_observation`). أُسقِطَ المسارُ من `WI-085` تفاديًا لـ`CLAIM_CONFLICT`
(THE_ROADMAP § 6.1)، والمراجعةُ المستقلّةُ لـ`WI-085` يجبُ أن تشملَ هذا الهَنْكَ.
