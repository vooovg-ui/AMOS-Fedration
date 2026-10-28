# قيدُ W-722 — أدلّةُ دفعةِ معجمِ G1 (§ 5.1 · § 9.5): خمسةُ أسماءٍ ومستويانِ لزرِّ الإيقاف

## التعريف
الأدلّةُ الخامُّ لدفعةِ المعجم: الفرقُ في `core/constitutional_engine/rules.py`، وفحوصُ المعجمِ قبلَ الشِّفرةِ وبعدَها،
وقياسُ D-4 بعدَها.

## النطاق
المعجمُ وحدَه بقرارِ المالكِ (`docs/governance/work/HANDOFFS/OWNER-DECISIONS-D28.md`):
- `EXECUTIVE_ACTIONS` ⇐ issue_certificate · create_backup · self_heal
- `LEGISLATIVE_ACTIONS` ⇐ suspend_policy · vote
- `KILL_SWITCH_BLOCKS` ⇐ issue_certificate في المستوى 3 · self_heal في المستوى 4

ولا سلوكَ جديدًا ولا عبورَ سطحٍ في هذه الدفعة، فـD-4 لا يتحرَّك. والحرقُ يبدأُ بدفعةِ state_runtime+system_life.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-722 · البندُ WI-120).

## تاريخ الإنشاء
2026-10-28

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | الأمرُ المولِّد |
|---|---|---|
| `rules_diff.txt` | فرقُ `rules.py` على قاعدةِ الفرع | `git diff HEAD -- core/constitutional_engine/rules.py` |
| `vocab_tests_before.txt` | الفحوصُ الجديدةُ على `rules.py` القديم: **8 سقطَت · 7 نجحَت** (السبعةُ الناجحةُ: سماحُ الفرعِ المالكِ والغائبُ عمدًا وcreate_backup بلا منع — تصحُّ قبلُ وبعد) | `git stash -- core/constitutional_engine/rules.py` ثمَّ `pytest tests/constitutional/test_g1_vocabulary.py -q` ثمَّ `git stash pop` |
| `vocab_tests_after.txt` | الفحوصُ نفسُها بعدَ الشِّفرة: **15 نجحَت** | `pytest tests/constitutional/test_g1_vocabulary.py -v` |
| `d4_after.txt` | أداةُ الجردِ بعدَ الشِّفرة: **121** (بلا تغيُّر) | `.venv/bin/python tools/audit/sovereign_write_inventory.py --root .` |

## أثرٌ جانبيٌّ مقيس
`docs/audit/measurements/judicial_gate_matrix.json` أُعيدَ توليدُه (`python tools/audit/judicial_gate_probe.py --json
docs/audit/measurements/judicial_gate_matrix.json`): أربعةُ أحكامٍ صارت **ALLOW → DENY** بـR-003-1، هي
(suspend_policy · vote) × (EXECUTIVE · JUDICIAL). وهذا هو الحصرُ المقصودُ لا خطأٌ.

## ما لم يُقَس
- سلوكُ self_heal وشرطُه (سجلُّ الإيقافِ المحكوم): مكانُه دفعةُ system_life لا هذه.
- حراسةُ أيِّ سطح: لا عبورَ هنا.

## تاريخ آخر تعديل
2026-10-28

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `d4_after.txt` — ملف تابع
- `rules_diff.txt` — ملف تابع
- `vocab_tests_after.txt` — ملف تابع
- `vocab_tests_before.txt` — ملف تابع
