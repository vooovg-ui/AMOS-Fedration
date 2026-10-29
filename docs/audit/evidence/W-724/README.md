# قيدُ W-724 — أدلّةُ دفعةِ G1 الثالثة: expansion والمعجمُ الصغير (Q-76)

## التعريف
الأدلّةُ الخامُّ لدفعةِ expansion: مسبارُ الأفعالِ قبلَ الشِّفرة، وأحكامُ CI لدفعةِ W-723 (واجبُ N+1)، وقياساتُ D-4 بعدَ الشِّفرة.

## النطاق
تصميمُ G1 § 9.9 · قرارُ المالكِ D29 (Q-76) · السؤالانِ Q-77 وQ-78.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-724 · البندُ WI-120).

## تاريخ الإنشاء
2026-10-29

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | الأمرُ المولِّد |
|---|---|---|
| `probe_expansion_actions.py` | مسبارُ `request_permit` بفاعلِ EXECUTIVE لأفعالِ الجدول — بلا كتابةٍ في المشروع | يُشغَّلُ من `federal/executive/services` |
| `probe_expansion_actions.txt` | مخرجُه: `spawn_population` ⇐ DENY بـR-001-1 · الستّةُ الأخرى ⇐ PERMIT | المسبارُ أعلاه |
| `ci/` | أحكامُ CI الأربعةُ على `2dc40c01` (PR #189 وmain) مقروءةً خضراء — واجبُ N+1 لـW-723 | `ci_verdict_readability.py --from-json` |
| `vocab_tests_before_code.txt` | فحوصُ المعجمِ قبلَ إضافةِ `graceful_shutdown`: **2 فشلا · 17 نجحَت** (الحمرةُ قبلَ الشِّفرة) | `pytest tests/constitutional/test_g1_vocabulary.py -q` من الجذر |
| `vocab_tests_after_code.txt` | بعدَها: **19 نجحَت** | الأمرُ نفسُه |
| `d4_before.txt` | الجردُ على main `2dc40c01` (قاعدةُ الفرع): **110** · مواضعُ 240 · سياديٌّ 70 | `git worktree add /tmp/wt_base 2dc40c01` ثمَّ `sovereign_write_inventory.py` فيه |
| `d4_after.txt` | الجردُ بعدَ الشِّفرة: **104** · مواضعُ 243 · سياديٌّ 76 · العامُّ 182 كما هو | `.venv/bin/python tools/audit/sovereign_write_inventory.py` |
| `inventory_after_w724.json` | حمولةُ الجردِ كاملةً بعدَ الشِّفرة | `sovereign_write_inventory.py --json docs/audit/evidence/W-724/inventory_after_w724.json` |
| `surfaces_after.txt` | الأسطحُ العامّةُ في expansion وgraceful_shutdown من الحمولةِ نفسِها: 6 محروسةٌ جديدةٌ · create_batch وenroll_batch `guarded=False` (Q-77) | قراءةُ `sites` من الحمولة |
| `w724_tests.txt` | فحوصُ الدفعة: **40 نجحَت** | `pytest tests/test_w724_g1_expansion.py -v` من `federal/executive/services` |
| `services_suite.txt` | حزمةُ الخدماتِ كاملةً: **1709 نجحَت · 53 تخطّيًا = 1762** | `pytest tests/ -q` من `federal/executive/services` |
| `mutation_campaign.py` · `mutation_results.json` | نزعُ نداءِ الحدِّ من كلِّ سطحٍ: خطُّ الأساسِ ناجحٌ ثمَّ **6/6 قُتِلَت على تأكيدِ الدليل** | `.venv/bin/python docs/audit/evidence/W-724/mutation_campaign.py` |

## الحرقُ والتصحيح
D-4: 110 ← 104 — **حرقٌ حقيقيٌّ 6 · تصحيحٌ 0**. والمواضعُ الثلاثةُ الزائدةُ (240 ← 243) مُطبِّقاتٌ وكُتّابٌ خاصّةٌ لا تُحصى في الدَّين.
و`graceful_shutdown` لم يتغيّرْ حرسُه (محروسٌ منذُ W-723)؛ تغيّرَ فعلُه وحدَه (Q-76 ②).

## ما لم يُقَس
- **زرُّ الإيقافِ غيرُ محقونٍ في الإنتاج** (DISC-099 · WI-085): كلُّ فحصٍ للمنعِ هنا يحقنُ المستوى في الطلبِ محاكاةً، فلا يُثبِتُ منعًا عندَ أيِّ مستوى في الإنتاج.
- **employ_batch وgraduate_batch ليستا ذرّيّتَينِ كلَّهما** (§ 9.9.6 (1)): فشلُ عبورِ صفِّ الدفعةِ الأخيرِ يعكسُ العددَ وحدَه، لا فحوصَ الصحّةِ ولا خطواتِ المنهجِ ولا تحديثاتِ الحالةِ التي ثبتت قبلَه.
- **فشلٌ داخلَ مُطبِّقٍ وحيدِ الأثرِ** في الأسطحِ الخمسةِ غيرِ retire_agent لا يُعوَّضُ آليًّا — دَينُ 2A (G-7) كما هو. وretire_agent وحدَه يُعوِّضُ الأثرينِ بنفسِه (مقيسٌ بفحص).
- قيمةُ الفحصِ الصحّيِّ في `test_c2_employ_activates_through_inner_crossings` مُتجاوَزةٌ إلى «healthy» بعدَ عبورِه الحقيقيّ: وكيلٌ جديدٌ بلا خبراتٍ يُقاسُ «monitor» فلا يُوظَّف.
- **Q-77** (create_batch/enroll_batch) و**Q-78** (release_agent) معلَّقانِ للمالك — لم يُنزَلْ أيٌّ منهما إلى فعلٍ أخفّ.
- لا جولةَ مجلسٍ ولا نصاب — والدفعةُ لا تُوسَمُ VERIFIED.

## تاريخ آخر تعديل
2026-10-29

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `ci/` — مجلد تابع
- `d4_after.txt` — ملف تابع
- `d4_before.txt` — ملف تابع
- `inventory_after_w724.json` — ملف تابع
- `mutation_campaign.py` — ملف تابع
- `mutation_results.json` — ملف تابع
- `probe_expansion_actions.py` — ملف تابع
- `probe_expansion_actions.txt` — ملف تابع
- `services_suite.txt` — ملف تابع
- `surfaces_after.txt` — ملف تابع
- `vocab_tests_after_code.txt` — ملف تابع
- `vocab_tests_before_code.txt` — ملف تابع
- `w724_tests.txt` — ملف تابع
