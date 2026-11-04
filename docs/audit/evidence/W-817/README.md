# evidence/W-817 — قراراتُ Q-97 وتصميمُ الدفعةِ 1 وأدلّةُ شِفرتِها (W-817 · W-818)

## التعريف
أدلّةُ قيدَي W-817 (توثيق: نصُّ التوجيهِ 42 · Q-97 · تصميمُ § 6 · قياسُ `log_cost` · بندُ فكِّ `enforce_ruling_via_treasury` · أحكامُ CI لـW-816 وmain) وW-818 (شِفرةُ الدفعةِ 1 من Q-83 (ج): الأسطحُ الثمانيةُ في `federal_state` تعبرُ `guard_declared` بأفعالِها الجديدةِ في `EXECUTIVE_ACTIONS`). تصنيفُ W-818 **C4** (يمسُّ `core/`) — لا VERIFIED بغيرِ المراجعِ أو المجلس.

## النطاق
- `OWNER_DIRECTIVE_42.md` — نصُّ التوجيهِ حرفيًّا.
- `q97_engine_probe.py` + `q97_engine_probe_output.txt` — المسبارُ الخامُ (القيد ج): يقرأُ `rules.py` من القرص · لكلِّ فعلٍ EXECUTIVE وحدَه ALLOW والتسعةُ DENY (`R-003-1`) ⇒ `verbs=8 mismatched=0` · EXIT=0 · وبمفتاحِ الإيقافِ L0–L5 = ALLOW للتنفيذيِّ (الأفعالُ ليست في `KILL_SWITCH_BLOCKS` — مُعلَن).
- `q97_mutation_probe.py` + `q97_mutation_output.txt` — الطفراتُ (القيد هـ): 8 حذفٍ من الحصرِ ⇒ المسبارُ يخرجُ 1 · 8 رفعٍ لـ`guard_declared` ⇒ اختبارُ العبورِ يفشل · `total=16 survived=0` · الملفُّ أُعيدَ مطابقًا بالبصمة.
- `caller_impact_scan.py` + `caller_impact_before.txt`/`caller_impact_after.txt` — أثرُ الحصرِ على المنادين (القيد د): `ENGINE_CALLERS=0` قبلُ وبعد (لا منادٍ يمرّرُ الأسماءَ الثمانيةَ إلى المحرّكِ خارجَ هذه الدفعة) · و`r8_r9_before.txt`/`r8_r9_after.txt`: 78 ناجحًا قبلُ و78 بعد.
- `d4_before_stdout.txt`/`d4_after_stdout.txt` + `d4_classification_before.txt`/`d4_classification_after.txt` — D-4 بالأداةِ نفسِها: **77 ⇒ 69** (العابرُ 94 ⇒ 102 · العامُّ 180 ⇒ 180 · الكلُّ 269 ⇒ 269) ⇒ **حرقٌ 8 · إعادةُ تصنيفٍ 0**.
- `log_cost_caller_scan.py` + `log_cost_caller_output.txt` — قياسُ مُنادي `log_cost` (Q-97 السؤال 5) قراءةً فقط.
- `ci_w816/` — حكما CI لـW-816 (PR #265 · `dcea5efe`) · `ci_w815_main/` — حكما CI على main بعدَ W-815 (`3d907a2d`): EXIT=0 ×4 (قاعدةُ N+1).

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · WI-127 · قيدا W-817/W-818)

## تاريخ الإنشاء
2026-11-04

## تاريخ آخر تعديل
2026-11-04

## المحتويات
- `services_full_suite.txt`: الحزمةُ الكاملةُ للخدمات بعدَ الدفعة — 1913 نجحَت · 53 مُتخطّاة · 0 فشل = 1966 (892.73 ثانيةً · SQLite · `OTEL_SDK_DISABLED=true`).
- المقيس: ما في النطاقِ أعلاه بأرقامِه.
- **لم يُقَس:** حكمُ CI على هذه الدفعةِ نفسِها (يُقيَّدُ في N+1) · سلوكُ الأسطحِ تحتَ PostgreSQL (القياسُ على SQLite) · التزامنُ الفعليُّ لمنادِيَينِ معًا (الإعادةُ تُحاكى بحذفِ الصفِّ يدويًّا) · أثرُ إدخالِ الأفعالِ في `KILL_SWITCH_BLOCKS` (لم يُقرَّر) · المعنى الدستوريُّ لتسجيلِ الحكومة (سؤالٌ للمالك) · أثرُ تحويلِ الأسطحِ 15–17 إلى الخزانة (Q-97 السؤال 4).

## قانون الوكالة
لا VERIFIED ولا CLOSED بيدِ المنفِّذ · K1 لم يُمَسّ · لا `gh pr merge` ولا دفعٌ قسريّ.
