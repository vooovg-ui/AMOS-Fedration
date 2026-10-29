# حمولاتُ CI لدفعةِ W-736 (PR #198) — واجبُ N+1 في W-737

## التعريف
حمولاتُ وظائفِ تشغيلاتِ PR #198 ولـmain بعدَ دمجِه، ومخرجاتُ الفاحصِ عليها.

## النطاق
- على `ad67494c15207423a4e5227c9b81003a850d24ec` (PR #198): CI `40901720835` · المصفوفةُ `40901707593` — EXIT=0 كلاهما ⇒ `TZ=UTC git push origin ad67494c…:main`.
- على main بعدَ الدمج (`ad67494c`): CI `40905380698` · المصفوفةُ `40905380729` — EXIT=0 كلاهما.

## المالك
المنسِّقُ (قيدُ W-737).

## تاريخ الإنشاء
2026-10-29

## تاريخ آخر تعديل
2026-10-29 (W-737 — القيدُ نفسُه)

## المحتويات
- `*_jobs.json` — حمولةُ `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/<id>/jobs` مع مفتاحِ `$comment` للغاية.
- `checker_*.txt` — `ci_verdict_readability.py --from-json … --require-readable --expect-sha <sha>` ومخرجُه وEXIT.
