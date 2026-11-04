# دليلُ حمولاتِ CI لدفعتَي W-812 وW-813 — مقيَّدةٌ في W-814 بحكمِ Q-95 القرار 2

## التعريف

حِمَلُ وظائفِ ستّةِ تشغيلاتٍ أُحمِلَت بـ`gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/<id>/jobs`
وقُرِئَ حكمُ كلٍّ بالفاحصِ `ci_verdict_readability.py --from-json <ملف> --require-readable --expect-sha <sha>`
في خطوةٍ منفصلة: **EXIT=0 ستَّ مرّات** (`verdicts_readability.txt`).

## النطاق

- W-812 على `ede2e8db`: ‏41759791838 (PR #262 · 13/13) · 41759768479 (push · 1/1) · 41763182430 (main · 13/13) · 41763182423 (main · 1/1).
- W-813 على `d1ac08bd`: ‏41789383465 (PR #263 · 13/13) · 41789376894 (push · 1/1).

## المالك

Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · قيدُ W-814 · WI-128).

## تاريخ الإنشاء

2026-11-04

## تاريخ آخر تعديل
2026-11-04

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `run_41759768479_jobs.json` — بيانات مهيكلة
- `run_41759791838_jobs.json` — بيانات مهيكلة
- `run_41763182423_jobs.json` — بيانات مهيكلة
- `run_41763182430_jobs.json` — بيانات مهيكلة
- `run_41789376894_jobs.json` — بيانات مهيكلة
- `run_41789383465_jobs.json` — بيانات مهيكلة
- `verdicts_readability.txt` — ملف تابع
