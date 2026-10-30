# evidence/W-749 — تصميمُ دفعةِ المعجم (Q-77 ② · Q-78 ③ · Q-80 ②) قبلَ الشِّفرة

## التعريف
أدلّةُ القيدِ W-749: قياساتُ ما قبلَ الشِّفرةِ لدفعةِ المعجمِ بأمرِ التوجيهِ 32 § 1 («دفعة المعجم: graceful_shutdown + تحويلات Q-77 وQ-78 وQ-80»)،
والتصميمُ نفسُه في `docs/audit/G1_GOVERNANCE_CROSSING_DESIGN.md` § 9.11.

## النطاق
قياسٌ وتصميم — لا شِفرة. البندُ `WI-120` ينتقلُ `IN_REVIEW → IN_PROGRESS` (قيدٌ مستقلٌّ · H3) لأنَّ الدفعةَ آخرُ دفعاتِ G1 المعلَّقةِ بالقرارات.

## المالك
المنسِّقُ (Perplexity Computer) — قيدُ W-749 (بندُ WI-120).

## تاريخ الإنشاء
2026-10-30

## تاريخ آخر تعديل
2026-10-30 (W-749 — الإنشاء)

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `probe_lexicon_actions.py` — شفرة مصدرية
- `probe_before.txt` — ملف تابع
- `d4_before.txt` — ملف تابع
- `d4_before_surfaces.txt` — ملف تابع

## الأوامر (تُعادُ حرفيًّا)
- المسبار (من `federal/executive/services`): `../../../.venv/bin/python ../../../docs/audit/evidence/W-749/probe_lexicon_actions.py`
- الجرد (من الجذر): `.venv/bin/python tools/audit/sovereign_write_inventory.py --root .` ثمَّ `--json` لاستخراجِ الأسطح

## المقيس
- **المسبار:** EXECUTIVE يُجازُ على الأفعالِ الأربعةِ الهدف (`create_task` · `spawn_agent` · `activate_agent` · `record_curriculum_step`)، ولا واحدَ منها
  في `HUMAN_GATED_ACTIONS`، ومستوياتُ المنعِ كما في نصوصِ القرارات (≥4 · ≥3 · ≥4 · ≥1). و`release_agent` لا يُمنَعُ عندَ أيِّ مستوى (اليومَ لـgraduate/complete).
  و`graceful_shutdown` PERMIT ولا منعَ عندَ أيِّ مستوى — منفَّذٌ في W-724 (Q-76 ②) فلا يُعاد.
- **D-4 قبل:** 95. والأسطحُ المتجاوزةُ في الملفَّين أربعة: `create_batch` · `enroll_batch` · `evaluate_model` · `start_training` ⇒ المتوقَّعُ بعدَ الشِّفرةِ 92
  (`start_training` دَينٌ بنصِّ Q-80 ①) — يُقاسُ في W-750 ولا يُعَدّ.
