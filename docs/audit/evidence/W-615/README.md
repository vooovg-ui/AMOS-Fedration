# دليلُ قيدِ W-615 — قياسُ ما قبلَ WI-106 (الدفعةُ F1: `governance/federation.py` بفاعلٍ تنفيذيٍّ مُعلَنٍ بالفعلِ `coordinate`) وملحقُ التصميمِ قبلَ الشِّفرةِ

## التعريف
دليلُ قيدِ `W-615` (WI-106 RESERVED→IN_PROGRESS · ملحقُ التصميمِ قبلَ الشِّفرةِ): قياسُ ما قبلَ بندِ `WI-106` (سُجِّلَ READY في W-613) لدفعةِ **F1** من خطّةِ حرقِ D-4 — سندُها قرارُ المالكِ **D17-1** («خيار (1): فاعل تنفيذي معلن للوحدة بالفعل coordinate (نص Q-24 نفسه) → يفتح دفعة F1.») وأمرُ توجيهِ المستشارِ 19 § 2 · وقياسُ ما قبلَ أيِّ تصميمٍ أو شِفرةٍ بأوامرَ مُلتزَمةٍ.

## النطاق
بندُ WI-106 (قياسُ ما قبلُ + ملحقُ التصميمِ [`F1_FEDERATION_COORDINATE_DESIGN.md`](../../F1_FEDERATION_COORDINATE_DESIGN.md) — لا شِفرةَ).

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5).

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `inventory_before.txt` — مخرجُ `python tools/audit/sovereign_write_inventory.py` عندَ رأسِ الفرعِ (فوقَ main `296a276` + قيودِ W-610…W-614 الوثائقيّةِ): **دَينٌ 181 · سياديٌّ 18 · أسطحٌ 220**
- `federation_sites_before.txt` — مواضعُ `governance/federation.py`: **16 موضعًا · 15 عامًّا كلُّها دَينٌ (0 عابرٌ)** + معاونٌ خاصٌّ واحدٌ (`ExecutiveBranch._init_roles` — بذرُ الأدوارِ الشاغرةِ في المُنشئِ)
- `probe_coordinate_actors.py` · `probe_coordinate_actors.out.txt` — مسبارُ البوابةِ على الفعلِ `coordinate` لكلِّ فاعلٍ عبرَ `ConstitutionalAuthorizer.review_only`: **EXECUTIVE ⇒ ALLOW** · LEGISLATIVE/JUDICIAL/TREASURY ⇒ DENY · AGENT/SYSTEM ⇒ ALLOW (ثغرةُ Q-68 المعروفةُ — خارجَ هذا البندِ)

## تاريخ آخر تعديل
2026-10-22

## تاريخ الإنشاء
2026-10-22
