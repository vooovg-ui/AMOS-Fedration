# قيدُ W-723 — أدلّةُ دفعةِ G1 الثانية: state_runtime وsystem_life تعبرانِ الحدَّ السياديّ

## التعريف
الأدلّةُ الخامُّ لدفعةِ الشِّفرةِ الأولى من أسطحِ G1: قياسُ D-4 قبلَ الدفعةِ وبعدَها، وحراسةُ كلِّ سطحٍ من الجرد،
وفحوصُ الدفعةِ، وحزمةُ الخدمات.

## النطاق
بقرارِ المالكِ (`docs/governance/work/HANDOFFS/OWNER-DECISIONS-D28.md`) وتصميمِ G1 § 3 و§ 9.8:
- `state_runtime.py` (5): register_state بمرسومٍ ملكيٍّ وربطِ الهدف (Q-13) · suspend_state · reactivate_state بسجلِّ
  إيقافٍ محكوم (Q-14) · assign_agent · FederalMessageBus.send_message
- `system_life.py` (6): bootstrap · health_check · self_heal بشرطِه · graceful_shutdown · create_backup · launch_checklist
- `restore_backup` غيرُ محروسٍ عمدًا (دَينٌ · D28 (أ))

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-723 · البندُ WI-120).

## تاريخ الإنشاء
2026-10-28

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | الأمرُ المولِّد |
|---|---|---|
| `d4_before.txt` | الجردُ على `4f2743bd` (قاعدةُ الفرع): **121** · مواضعُ 235 · سياديٌّ 59 | `git worktree add /tmp/wt_base 4f2743bd` ثمَّ `sovereign_write_inventory.py --root .` فيه |
| `d4_after.txt` | الجردُ بعدَ الشِّفرة: **110** · مواضعُ 240 · سياديٌّ 70 | `.venv/bin/python tools/audit/sovereign_write_inventory.py --root .` |
| `inventory_after_w723.json` | حمولةُ الجردِ كاملةً بعدَ الشِّفرة | `sovereign_write_inventory.py --root . --json docs/audit/evidence/W-723/inventory_after_w723.json` |
| `surfaces_after.txt` | الأسطحُ العامّةُ في الملفَّينِ وحراستُها من الحمولةِ نفسِها: 12 محروسًا (منها allocate_budget القديم) · restore_backup وحدَه `guarded=False` | قراءةُ `sites` من الحمولةِ وتصفيتُها بالمسارَين و`public` |
| `w723_tests.txt` | فحوصُ الدفعةِ: **54 نجحَت** | `pytest tests/test_w723_g1_state_runtime_system_life.py -v` من `federal/executive/services` |
| `services_suite.txt` | حزمةُ الخدماتِ كاملةً: **1669 نجحَت · 53 تخطّيًا** | `pytest tests/ -q` من `federal/executive/services` |

## الحرقُ والتصحيح
D-4: 121 ← 110 — **حرقٌ حقيقيٌّ 11 · تصحيحٌ 0**. والمواضعُ الخمسةُ الزائدةُ (235 ← 240) نوىً خاصّةٌ لا تُحصى في الدَّين.

## ما لم يُقَس
- زرُّ الإيقافِ غيرُ محقونٍ في الإنتاج (DISC-099): منعُ orchestrate/self_heal عندَ ≥4 مقيسٌ بفحصٍ يحقنُ المستوى لا بتشغيل.
- فشلٌ **داخلَ** مُطبِّقٍ وحيدِ الأثرِ (كتابةٌ ثمَّ سقوطٌ قبلَ العودة) لا يُعوَّضُ آليًّا — دَينُ 2A (test_2a G-7) كما هو.
  والصنفُ 5 قِيسَ بانكسارِ التثبيتِ بعدَ المُطبِّقِ (نمطُ E1) وبفشلِ الأثرِ الثاني في self_heal.
- الإيقافُ «التلقائيُّ» (بلا قرار): لا مسارَ في الشِّفرةِ اليومَ يُنشئُه، فقِيسَ بصفٍّ معلَّقٍ بلا سجلٍّ نشط.
- Q-76 (graceful_shutdown وlaunch_checklist على orchestrate) معلَّقٌ للمالك — نُفِّذَ عمودُ الفعلِ كما هو.
- لا جولةَ مجلسٍ ولا نصاب — والدفعةُ لا تُوسَمُ VERIFIED.

## تاريخ آخر تعديل
2026-10-28

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `d4_after.txt` — ملف تابع
- `d4_before.txt` — ملف تابع
- `inventory_after_w723.json` — ملف تابع
- `services_suite.txt` — ملف تابع
- `surfaces_after.txt` — ملف تابع
- `w723_tests.txt` — ملف تابع
