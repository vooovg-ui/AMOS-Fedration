# حمولاتُ CI لدفعةِ W-737/W-738 (PR #199) — واجبُ N+1 في W-739

## التعريف
حمولاتُ وظائفِ تشغيلاتِ PR #199 ولـmain بعدَ دمجِه، ومخرجاتُ الفاحصِ عليها.

## النطاق
- على `62f8a8970ffd964fe960189a75354c3adf16f63e` (PR #199): CI `40909175940` · المصفوفةُ `40909166319` — EXIT=0 كلاهما ⇒ `TZ=UTC git push origin 62f8a897…:main`.
- على main بعدَ الدمج (`62f8a897` · ad67494c..62f8a897): CI `40912818986` · المصفوفةُ `40912819106` — EXIT=0 كلاهما.

## المالك
المنسِّقُ (قيدُ W-739).

## تاريخ الإنشاء
2026-10-29

## تاريخ آخر تعديل
2026-10-29 (W-739 — القيدُ نفسُه)

## المحتويات
- `*_jobs.json` — حمولةُ `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/<id>/jobs` مع مفتاحِ `$comment` للغاية.
- `checker_*.txt` — `ci_verdict_readability.py --from-json … --require-readable --expect-sha <sha>` ومخرجُه وEXIT.
