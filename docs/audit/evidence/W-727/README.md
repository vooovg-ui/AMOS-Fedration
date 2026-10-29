# أدلّةُ دفعةِ W-727 — ملحقُ تصميمِ الدفعةِ 4 من G1 (learning_cycle + security) · دفعةٌ ورقيّة

## التعريف

أدلّةُ الملحقِ § 9.10 من [`../../G1_GOVERNANCE_CROSSING_DESIGN.md`](../../G1_GOVERNANCE_CROSSING_DESIGN.md) قبلَ أيِّ شِفرة
(التوجيهُ 28 § 2 بند 3: «ملحقُ تصميمٍ ← شِفرة»)، وسؤالُ المالكِ **Q-80 (PENDING_OWNER)** في
[`../../SOVEREIGN_DECISION_REGISTER.md`](../../SOVEREIGN_DECISION_REGISTER.md)، وأحكامُ CI لدفعةِ W-726 (واجبُ N+1).

## النطاق

- **لا شِفرة.** لا مساسَ بـ`learning_cycle.py` ولا `security.py` ولا `rules.py` ولا K1.
- المسبارُ يعملُ على قاعدةٍ ودفترِ تكرارٍ مؤقّتَين في `/tmp` ولا يُنشئُ `.runtime/` (قِيسَ بعدَ التشغيل).

## المالك

Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-727 · البندُ WI-120).

## تاريخ الإنشاء

2026-10-29

## تاريخ آخر تعديل

2026-10-29

## النتيجةُ المقيسة

- إعادةُ العدِّ على `bb7eeb31`: الدفعةُ 4 = **11** سطحًا (learning_cycle 7 · security 4 بعدَ خروجِ store_secret).
- مسبارُ الأفعال: **9 PERMIT · 2 DENY R-001-1** — `start_training` و`evaluate_model` على `train_model` المحجوزِ بشريًّا (Q-80 أ).
- تعارضُ مستوى: `start_shadow`/`start_canary` § 2.2 يقول 1 والفعلُ `invoke_model` يُمنَعُ من 4 (Q-80 ب).

**التشغيل** (من `federal/executive/services`):

```
../../../.venv/bin/python ../../../docs/audit/evidence/W-727/probe_batch4_actions.py
```

## ما لم يُقَس

- كلفةُ عبورِ `check_rate` لكلِّ طلب (لا مناديَ إنتاجيًّا اليوم).
- أنَّ رمزَ الملكِ يحملُه إنسانٌ فعلًا (D25-1 (ج)).

## المحتويات

- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `probe_batch4_actions.py` — مسبارُ أفعالِ الدفعة (قياسٌ لا إصلاح)
- `probe_batch4_actions.txt` — مخرجُه الحرفيّ
- `surface_recount_bb7eeb31.txt` — مخرجُ `evidence/W-721/surface_recount.py` على `bb7eeb31`
- `ci/` — أحكامُ CI لدفعةِ W-726 (واجبُ N+1)
