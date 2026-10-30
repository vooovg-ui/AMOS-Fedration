# evidence/W-750 — شِفرةُ دفعةِ المعجم (Q-77 ② · Q-78 ③ · Q-80 ②) بعدَ تصميمِ W-749

## التعريف
أدلّةُ القيدِ W-750: تنفيذُ تصميمِ `docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md` § 9.11 (قيدُ W-749) بأمرِ التوجيهِ 32 § 1
(«دفعة المعجم: graceful_shutdown + تحويلات Q-77 وQ-78 وQ-80 — تفتح أسطح expansion/learning الموقوفة وتُنقص D-4»).

## النطاق
شِفرةٌ في `governance/expansion.py` و`governance/learning_cycle.py` وفحوصُها. البندُ `WI-120` يبقى `IN_PROGRESS` (انتقالُه في W-749) —
ولا VERIFIED بلا نصابٍ مستقلّ (التوجيهُ 32).

## المالك
المنسِّقُ (Perplexity Computer) — قيدُ W-750 (بندُ WI-120).

## تاريخ الإنشاء
2026-10-30

## تاريخ آخر تعديل
2026-10-30 (W-750 — الإنشاء)

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `d4_after.txt` — ملف تابع
- `d4_after_surfaces.txt` — ملف تابع
- `mutate.sh` — ملف تابع
- `mutations.txt` — ملف تابع
- `services_suite.txt` — ملف تابع
- `root_suite.txt` — ملف تابع

## الأوامر (تُعادُ حرفيًّا)
- الجرد (من الجذر): `.venv/bin/python tools/audit/sovereign_write_inventory.py --root .` (و`--json <ملف>` للأسطح)
- الطفرات (من الجذر): `bash docs/audit/evidence/W-750/mutate.sh` — كلُّ طفرةٍ تُعكَسُ بعدَ قياسِها والشجرةُ تعودُ كما كانت
- الحزمة (من `federal/executive/services`): `../../../.venv/bin/python -m pytest -q -p no:cacheprovider`
- الجذر: `.venv/bin/python -m pytest tests/ -q -p no:cacheprovider`

## ما نُفِّذ
| السطح | الفعلُ قبل | الفعلُ بعد | المنعُ بالقاطع | القرار |
|---|---|---|---|---|
| `PopulationExpansion.create_batch` | لا عبور | `create_task` (CREATE صفّ · معوِّضٌ حذف) | ≥4 | Q-77 ② |
| `PopulationExpansion.enroll_batch` | لا عبور | `spawn_agent` (تحقّقٌ مسبق ⇒ register_agent متعاقبة ⇒ عبورُ العدّاد · معوِّضٌ يُعيدُ العدّاد) | ≥3 | Q-77 ② |
| `EvaluationSystem.evaluate_model` | لا عبور | `record_curriculum_step` (CREATE صفّ · معوِّضٌ حذف · مُصرِّحٌ محقونٌ أو المشتركُ `get_authorizer()` — لا موضعَ بناءٍ جديد) | ≥1 | Q-80 ② |
| `PopulationExpansion.graduate_batch` | `release_agent` (لا منعَ عندَ أيِّ مستوى) | `activate_agent` | ≥4 | Q-78 ③ |
| `LearningCycle.complete_training` | `release_agent` | `activate_agent` | ≥4 | Q-78 ③ |
| `SystemLifecycle.graceful_shutdown` | `graceful_shutdown` (W-724) | لا تغيير — يُقاسُ فقط | لا منع | Q-76 ② |

`spawn_population` و`train_model` باقيانِ في `HUMAN_GATED_ACTIONS` لم يُمَسّا ولم يُنزَلا (فحصُ `test_c3_spawn_population_not_lowered_q77`).

## المقيس
- **D-4 قبل (W-749): 95 · بعد: 92** (`d4_after.txt`). والمتبقّي في الملفَّين سطحٌ واحد: `LearningCycle.start_training` — دَينٌ بنصِّ Q-80 ① (`d4_after_surfaces.txt`).
- **الطفرات:** ستٌّ كلُّها مقتولة (`mutations.txt`): M1 (7 فشل) · M2 (5) · M3 (1) · M4 (7) · M5 (1) · M6 (1) · وبلا طفرةٍ 130 ناجحًا.
  M3 (حذفُ التحقّقِ المسبقِ في enroll_batch) يقتلُه فحصٌ واحد لأنَّ register_agent الداخليَّ يمنعُ عندَ ≥3 أيضًا — حدٌّ معلَن.
- **حزمةُ الخدمات:** 1835 ناجحًا · 53 تخطّيًا · 0 فشل = 1888 (`services_suite.txt` · كانَ 1804/53/0).
- **الجذر:** 3076 ناجحًا · 1 تخطّيًا · 0 فشل (`root_suite.txt`). وكشفَ تشغيلٌ سابقٌ حمرتَين صُحِّحتا قبلَ الالتزام: لقطةُ الدَّينِ (`decision_gate.py --record-work W-750` ⇒ 92) وموضعُ بناءِ مُصرِّحٍ جديدٍ (أُزيلَ باستعمالِ `get_authorizer()` — لا تحديثَ لفحصِ q3).
- **لقطةُ الدَّين:** `docs/audit/measurements/decision_gate_ledger.json` — debt 92 · sovereign 88 · W3 50→47.

## تصحيحٌ مؤرَّخ
- (2026-10-30 · W-750) مسبارُ W-749 `probe_lexicon_actions.py` سمّى ثابتَه `ROWS` فطابقَ كاشفَ HARDCODED_TRUTH في `truth_audit.py` (الراتشيت 2→3) — أُعيدَت تسميتُه `PROBE_CASES` بلا تغييرِ سلوك، وأُعيدَ تشغيلُه فطابقَ مخرجُه `probe_before.txt` سطرًا بسطر. لا تخفيفَ للكاشفِ ولا تحريكَ لخطِّ الأساس.

## ما لم يُقَس
- حقنُ مستوى القاطعِ في الإنتاج — محاكاةٌ في الطلبِ فقط (DISC-099/WI-085): الفحوصُ لا تُثبِتُ منعًا في الإنتاج.
- `run_full_expansion` لم يُشغَّلْ كاملًا في الفحوص (خطٌّ قصيرٌ بدفعةٍ واحدةٍ فقط).
- `enroll_batch` ليست ذرّيّةً كلُّها: انكسارُ عبورِ العدّادِ يُعيدُ العدّادَ ولا يحذفُ الوكلاءَ المسجَّلين بعبورِهم (§ 9.9.6 (1)).

## تصحيح مؤرَّخ 2026-10-30 — خريطة الموجات
- أُعيدَ توليدُ `docs/audit/measurements/decision_wave_map.json` بـ`decision_gate.py --map` في الدفعةِ نفسِها (11 + 34 + 47 = 92) بعدما كشفَ CI على PR #220 أنها بقيت على 95؛ والأصلُ أن تُولَّدَ مع الالتزامِ المُقاس لا بعده.
