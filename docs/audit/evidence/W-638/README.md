# دليل دفعة W-638 — حجزُ WI-109 · WI-110 · WI-111 (READY→RESERVED) وملحقُ تصميمِ J2+J3 قبلَ الشِّفرةِ

## التعريف
دليلُ القيدِ W-638: انتقالُ البنودِ الثلاثةِ READY→RESERVED (H3 · انتقالٌ واحدٌ لكلِّ بندٍ في مدى الدمجِ) وإيداعُ ملحقِ تصميمِ J2+J3 (`docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md`) **في التزامٍ يسبقُ الشِّفرةَ** (Q-61) معَ قياسِ ما قبلُ.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — بندُ WI-111.

## النطاق
T1 (federal_judiciary · المعجمانِ) — قياسٌ وتصميمٌ لا شِفرةَ · التاريخ: 2026-10-23.

## تاريخ الإنشاء
2026-10-23 (W-638).

## تاريخ آخر تعديل
2026-10-23 (W-638).

## المحتويات
- `inventory_before_wi111.json` · `inventory_before_wi111.txt` — `sovereign_write_inventory.py --json` عندَ `6b8d21b` (لا شِفرةَ إنتاجيّةً منذُ `7a547fa`): مواضعُ 246 · عامّةٌ مُغيِّرةٌ 201 · تعبرُ 42 · **لا تعبرُ 157** · وفي federal_judiciary 25 سطحًا عامًّا دَينًا (15 محسومةً · 7 مؤجَّلةً · 3 لـJ4).
- `judicial_gate_probe_before.json` · `judicial_gate_probe_before.txt` — `judicial_gate_probe.py --json` قبلَ تعديلِ المعجمِ: الأفعالُ `vacate_ruling` · `refer_case` · `admit_case` · `admit_evidence` · `recuse_judge` · `register_judgment` · `assign_case` · `record_proceeding` كلُّها `ALLOW` لـ`EXECUTIVE` و`LEGISLATIVE` (و`adjudicate` · `issue_ruling` `DENY · R-003-1` لهما). (`join_party` و`admit_claim` ليسا في قائمةِ المسبارِ؛ يُقاسانِ في فحوصِ الدفعةِ.)
- `ci_jobs_pr135_40034820208.api.json` — حِملُ وظائفِ تشغيلِ PR #135 (حكمُ N+1 لـW-636/W-637: مقروءٌ أخضرُ 13/13 على `6b8d21b`).
