# قيدُ W-736 — شِفرةُ إصلاحِ Q-26: `retire_agent` عبورٌ واحدٌ يعلنُ آثارَ التقاعدِ الثلاثة (G1 § 9.9.8 · DISC-141)

## التعريف
الأدلّةُ الخامُّ لدفعةِ الشِّفرةِ التي تنفّذُ تصميمَ W-735 (§ 9.9.8) بعدَه لا قبلَه (التوجيهُ 29 § 2).

## النطاق
`federal/executive/services/src/amos_federation/services/governance/expansion.py` (`RetirementSystem.retire_agent` وحدَه) ·
فحصٌ جديدٌ `federal/executive/services/tests/test_w736_q26_retire_single_crossing.py` (22 فحصًا) · طفرةٌ داخلَ هذا المجلد.
خارجَ النطاق: `PopulationRegistry.update_state` (E1 · فحصُ C2 من المسبار) — DISC-142 · Q-81 (ب) PENDING_OWNER.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-736 · البندُ WI-120).

## تاريخ الإنشاء
2026-10-29

## الشِّفرة (ما تغيّر)
- طلبا إذنٍ مسبقانِ (`contain_agent` ثمَّ `update_population_state`) يحفظانِ رفضَ القاطعِ ≥3 نظيفًا قبلَ أيِّ أثر (سلوكُ W-724 المقيس).
- **عبورٌ واحدٌ** `guard_declared(contain_agent)` يعلنُ: الكانونَ (`lifecycle.<prev>->retired` · يُحذَفُ إن لم تكن هويّةٌ أو كانت retired) · المرآةَ (`population.state.<prev>->retired`) · السجلَّ (`retirement.<id>`).
- المُطبِّقُ يستدعي نوًى خاصّةً لا تعبرُ بنفسها: `_set_lifecycle_state_core` · `_update_population_row_core` · `_create_record`.
- لكلِّ أثرٍ معوِّضُه؛ فشلُ أثرٍ بعدَ سابقِه يُعيدُ ما طُبِّقَ بترتيبٍ عكسيّ (`CompensationRequired` من الحدّ).

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | النتيجة المقيسة |
|---|---|---|
| `probe_after.txt` | مسبارُ المقعدِ نفسُه (sha256 `5583d191…`) بعدَ الإصلاح — الأمرُ في رأسِه | `checks=30 broken=1` (قبلَ: 3 في W-735) · C.k=2 وC.k=3 صارا OK · الباقي C2 `update_state` خارجَ النطاق |
| `surface_scan_after.txt` | أداةُ W-735 نفسُها على فحوصِ W-723/W-724/W-728/W-699/W-736 | 30 سطحًا · `retire_agent` **3 → 1** · المتعاقبةُ 4 → 3 (graduate_batch 112 · employ_batch 31 · update_state 2) |
| `d4_before.txt` / `d4_after.txt` | `tools/audit/sovereign_write_inventory.py` على main `73379d69` ثمَّ على الشجرة | «لا تعبرُ الحدَّ» **95 → 95** · مواضعُ الكتابة 261 → 260 · تعبرُ 85 → 85 |
| `mutation_canonical_compensator.py` | طفرةٌ تُسقِطُ معوِّضَ الكانون (سطرٌ واحد · يُعادُ الأصلُ وتُقاسُ البصمة) | — |
| `mutation_results.txt` | مخرجُها | خطُّ الأساسِ أخضر · `killed=2/2` (3أ و3ب) · البصمةُ مطابقة · EXIT=0 |
| `tests_g1.txt` | فحوصُ G1 الخمسةُ معًا | 216 passed |
| `ci/` | واجبُ N+1 لدفعةِ PR #197 (W-733/W-734/W-735): ستُّ حمولاتٍ ومخرجاتُ الفاحص | المحاولةُ الأولى ساقطةٌ (EXIT=1 · صُحِّحَت بالإضافةِ في `830293cd`) · الأربعُ بعدَها EXIT=0 |
| `services_suite.txt` | حزمةُ الخدماتِ كاملة | 1790 passed · 53 skipped (قبلَ: 1768 + 53) |

القياساتُ المنشورةُ أُعيدَ توليدُها بأوامرِها المقيَّدة (عقدُ النَّسَب W-037): `docs/audit/measurements/write_inventory_p13.json` (‏`write_sites_total` 261→260 — زالَ موضعُ `RetirementSystem._apply` الكاتبُ مباشرةً، وصارَ `_create_record` نواةً عبرَ الحدّ) و`final_audit_p14.json` (‏`total_sites` 261→260) · ومصفوفةُ الحقيقةِ (‏`truth_audit.py --ratchet` ثابتٌ عندَ 61).

قياسٌ إضافيٌّ (مذكورٌ هنا لا ملفًّا): فحوصُ W-736 الـ22 على شِفرةِ ما قبلَ الإصلاح (`git show HEAD:…/expansion.py`) → **7 failed, 15 passed** (k=2,3 لمستويَي 3 و5 · العبورُ الواحد · 3أ · 3ب) — فالفحوصُ تلتقطُ الثغرةَ نفسَها.

## ما لم يُقَس
- `update_state` (C2): لم يُصلَح — ينتظرُ Q-81 (ب).
- حقنُ مستوى القاطعِ في الإنتاج: الفحوصُ تحاكيه بمُصرِّحٍ معلَن (DISC-099 · WI-085)؛ لا دليلَ تشغيليّ.
- مساراتٌ لا تمرُّ بها الفحوص: الفحصُ الديناميكيُّ لا يدّعي «نظيف» لما لم يُستدعَ.
- لا نصابَ مجلس: WI-120 يبقى IN_PROGRESS؛ لا VERIFIED ذاتيّ.

## تاريخ آخر تعديل
2026-10-29 (W-736 — القيدُ نفسُه)

## المحتويات
- `README.md` — بطاقةُ هويّةِ هذا المجلد (المادةُ التاسعة)
- `probe_after.txt` · `surface_scan_after.txt` · `d4_before.txt` · `d4_after.txt`
- `mutation_canonical_compensator.py` · `mutation_results.txt` · `tests_g1.txt` · `services_suite.txt`
- `ci/` — حمولاتُ CI لـPR #197 (مجلدٌ ببطاقتِه)
