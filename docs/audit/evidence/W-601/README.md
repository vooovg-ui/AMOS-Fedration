# دليلُ قيدِ W-601 — قرارُ المالكِ Q-70 وقياسُ موضعِ فجوةِ التعويضِ

## التعريف
دليلُ قيدِ `W-601`: تسجيلُ قرارِ المالكِ **Q-70** بنصِّه الحرفيِّ (توجيهُ المستشارِ 18 § 1 · سلَّمَه المالكُ 2026-10-22) وتنفيذُ شرطِه الأولِ — **قياسُ موضعِ الفجوةِ بلا تغييرٍ في الشِّفرةِ** على المسارِ الإنتاجيِّ لسطحَينِ مُهجَّرَينِ: (أ) `issue_ruling` (J1 · WI-105) و(ب) `register_identity` (WI-082). وحكمُ CI على رأسِ دفعةِ W-600 (N+1).

## النطاق
أدلةُ القيدِ وحدَها — لا شِفرةَ تُمسُّ في هذا القيدِ (بندُ WI-105). المسبارُ يُنسَخُ مؤقّتًا إلى مجلدِ فحوصِ الخدماتِ ثمَّ يُحذَفُ (سابقةُ مسبارِ مقعدِ claude في W-599) ولا يُلتزَمُ هناك.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 — منسِّقٌ لا مُصوِّتٌ).

## تاريخ آخر تعديل
2026-10-22

## تاريخ الإنشاء
2026-10-22

## المحتويات

- `directive_18_verbatim.md` — نصُّ التوجيهِ 18 حرفيًّا كما سلَّمَه المالكُ (سندُ Q-70).
- `test_w601_gap_probe.py` — المسبارُ: يُسقِطُ `IdempotencyLedger.mark_succeeded` بعدَ التزامِ المُطبِّقِ، ويُنادي السطحَ بنداءِ الخدمةِ وحدَه، ويسجِّلُ الاستثناءَ وحالةَ الصفوفِ ونداءاتِ `CompensationGuard.compensate` (جاسوسٌ لا يغيّرُ السلوكَ) وحالةَ سجلِّ الذرّيّةِ ونتيجةَ الإعادةِ.
- `probe_output_before_fix.txt` — مخرجُه الخامُ كاملًا برمزِ خروجِه على العقدةِ `8c98ca5` (قبلَ أيِّ تغييرٍ).
- `ci_jobs_39720098200.api.txt` · `ci_verdict_39720098200_green.txt` — حكمُ CI على رأسِ دفعةِ W-600 (`8c98ca54e5b89758673da0df880343d3f552c43e` · PR #117): READABLE · 13/13 · أخضرُ على العقدةِ نفسِها (حِملُ `gh api` + `--from-json` · سابقةُ W-574).

## النتيجةُ المقيسةُ (من `probe_output_before_fix.txt` حرفيًّا)

| | (أ) `issue_ruling` | (ب) `register_identity` |
|---|---|---|
| الاستثناءُ | `builtins.RuntimeError` | `builtins.RuntimeError` |
| الصفوفُ بعدَ الفشلِ | حكمٌ 1 · إجراءُ RULING 1 · القضيّةُ `decided` | صفُّ الهويّةِ موجودٌ |
| نداءاتُ المُعوِّضِ | 0 | 0 |
| سجلُّ الذرّيّةِ | `RUNNING` | `RUNNING` |
| الإعادةُ | `DuplicateRulingError` | `DuplicateAgentIdentityError` |

⇒ السطحانِ يتصرّفانِ تصرُّفًا واحدًا: **الفجوةُ في الحدِّ نفسِه** (`core/sovereignty/enforcement_boundary.py` · `SovereignExecutionBoundary.execute`) — الفرعُ الأولُ من قرارِ Q-70.

## إعادةُ التشغيل

```
cp docs/audit/evidence/W-601/test_w601_gap_probe.py federal/executive/services/tests/ && \
.venv/bin/pytest federal/executive/services/tests/test_w601_gap_probe.py -s -q -p no:cacheprovider ; \
rm federal/executive/services/tests/test_w601_gap_probe.py
```
