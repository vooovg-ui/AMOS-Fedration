# evidence/W-815 — شِفرةُ DISC-155 (أ) وDISC-153 بقرارِ المالكِ Q-96 بعدَ تصميمِهما

## التعريف
أدلّةُ قيدِ الشِّفرةِ W-815: المدخلُ الحادي عشر لـ`enforce_ruling_via_treasury` وتحديثُ عددِ الحرّاسِ الثلاثةِ 10 → 11 (M1 § 2.12)، والخطوةُ 34 في حرسِ ما قبلَ الدفع (`DISC153_PREPUSH_ONLY_DEPS_DESIGN.md`) — بطفراتِها وقياسِ D-4 بعدَها.

## النطاق
- `guards_raw_diff.txt`: `git diff d1ac08bd -- <الحرّاس الثلاثة>` خامًا. القراءة: سبعةُ أسطرٍ محذوفة كلُّها أعدادٌ أو أسماءُ فحوصٍ أُعيدَت بعددٍ أكبر — `treasury + economy == 6` ⇒ `treasury + economy + judiciary == 7` مع `judiciary == 1` جديد · `== 10` ⇒ `== 11` (ثلاثُ مرّات) · `four_of_ten` ⇒ `four_of_eleven` · `six_are_six` ⇒ `seven_are_seven` (و`len(WRAPPER_ENTRYPOINTS) == 3` جديد) · `ten_…_four_and_six` ⇒ `eleven_…_four_and_seven`. والمضافُ: فحصُ ترتيبِ الاستخراجِ قبلَ أيِّ عمل · امتدادُ «لا وسمَ جملةٍ» إلى القضاء · فحصا المُغلِّفِ القضائيّ (لا يعبرُ طبقةَ التخويلِ بنفسِه · يُسنِدُ إلى `treasury.disburse` ولا `_post`). لا فحصَ حُذِف.
- `mutation_probe.py` + `mutation_probe_output.txt`: تسعُ طفراتٍ (DISC-155 ①–⑤ · DISC-153 ①–④) ⇒ **9/9 مقتولة** (EXIT=0) · وتكميلُ ① على سلوكِ القضاءِ وحدَه: `UndeclaredMoneyDelegationError` قبلَ أيِّ كتابة.
- `d4_after_stdout.txt` + `d4_before_after_compare.txt`: D-4 ‏77 → 77 · الملخّصُ متطابق · صفرُ موضعٍ زائدٍ أو ناقصٍ موضعًا موضعًا ⇒ **حرقٌ 0 · إعادةُ تصنيفٍ 0**.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · قيدُ W-815 · WI-127 وWI-077)

## تاريخ الإنشاء
2026-11-04

## تاريخ آخر تعديل
2026-11-04

## المحتويات
- الحزمُ المقيسة: `test_q19`/`test_q31`/`test_q32`/`test_r7d_federal_judiciary`/`test_w792_m1_batch2_composites` ‏96 ناجحًا · `tests/governance/test_wi077_prepush_ci_parity.py` ‏22 ناجحًا · `prepush_gate.py --internal provenance-only-deps` EXIT=0 (`cryptography` حاضرة).
- ما لم يُقَس: عبورُ `enforce_ruling_via_treasury` نفسِه (قيدٌ تالٍ) · سلوكُ الخطوةِ 34 على آلةٍ بلا `cryptography` غيرُ الفحصِ المُحاكي.

## قانون الوكالة
لا VERIFIED ولا IN_REVIEW بيدِ المنفِّذ (RK-024). DISC-153 وDISC-155 «نُفِّذا بانتظارِ المراجعة» لا مُغلَقان.
