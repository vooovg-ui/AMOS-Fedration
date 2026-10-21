# قياسُ ما قبلَ J1 — حكمُ الحدِّ على `issue_ruling` لكلِّ فاعلٍ (W-581)

## التعريف

دليلُ قيدِ `W-581`: قياسٌ مُعادُ التشغيلِ بأمرٍ واحدٍ لحكمِ الحدِّ السياديِّ على الفعلِ `issue_ruling` (ولكلِّ فعلٍ حصريٍّ في القسمِ د) — سندُ وثيقةِ تصميمِ J1 (`docs/audit/J1_ISSUE_RULING_DESIGN.md` § 1.3) والاكتشافِ `DISC-121`.

## النطاق

بندُ `WI-105` (PROPOSED) · قياسٌ لا شِفرةَ إنتاجيّةَ: السكربتُ لا يكتبُ في قاعدةِ بياناتٍ (المُطبِّقُ يُسجِّلُ نداءَه في قائمةٍ) · وسجلُّ الذرّيّةِ ملفٌّ مؤقّتٌ بـ`mktemp -u`.

## المالك

Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5).

## تاريخ الإنشاء

2026-10-21

## النتيجةُ (من المخرجِ)

- (أ) المراجعةُ: JUDICIAL `ALLOW` · EXECUTIVE/LEGISLATIVE/TREASURY `DENY` · AGENT/SYSTEM `ALLOW` (طبقةُ AGENT).
- (ب) عبرَ الجسرِ `guard_declared`: **6/6 مرفوضٌ** بـ`JurisdictionNotDeclaredError` — الجسرُ لا يحملُ طلبَ الاختصاصِ.
- (ج) عبرَ الحدِّ الجوهريِّ بطلبِ اختصاصٍ ومُعوِّضٍ: JUDICIAL يُنفِّذُ · الفروعُ الثلاثةُ الأخرى `SovereigntyViolation` · **AGENT/SYSTEM يُنفِّذانِ**.
- (د) المراجعةُ لكلِّ فعلٍ حصريٍّ في `_BRANCH_EXCLUSIVE`: **ALLOW 54/54** لـAGENT وSYSTEM.

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `ci_jobs_39573575374.api.txt` — ملف تابع
- `ci_verdict_2694796.txt` — ملف تابع
- `probe_issue_ruling_actors.out.txt` — مخرجُ probe_issue_ruling_actors.py — W-581 · 2026-10-21 · العقدة 2694796 (سطورُ «حدث أمني» في …
- `probe_issue_ruling_actors.py` — قياسُ حكمِ الحدِّ السياديِّ على الفعلِ issue_ruling لكلِّ فاعلٍ — مسارُ التنفيذِ الكاملُ لا ال…

## تاريخ آخر تعديل
2026-10-21
