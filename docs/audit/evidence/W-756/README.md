# evidence/W-756 — M1 الدفعة 1: قياساتُ ما قبلَ الشِّفرة (WI-125 READY→RESERVED)

## التعريف
أدلّةُ القيدِ W-756 (2/3 من دفعةِ التوجيهِ 33): مسبارُ المالِ بعدَ Q-68 حرفيًّا · D-4 قبلَ الشِّفرة · حزمةُ الجذرِ قبلَ الشِّفرة. تسبقُ شِفرةَ W-757 («لا شِفرةَ قبلَ التصميم»).

## النطاق
قراءةٌ وقياسٌ فقط — لا يمسُّ شِفرةَ الإنتاج. التصميمُ المضافُ للدفعةِ 1 في `docs/audit/M1_MONEY_CROSSING_DESIGN.md` § 2.9 (بندُ WI-122).

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-756 · WI-125).

## تاريخ الإنشاء
2026-10-31

## تاريخ آخر تعديل
2026-10-31 (W-756 — الإنشاء)

## المحتويات
- `money_probe_after_q68.txt` — مخرجُ `.venv/bin/python docs/audit/evidence/W-739/engine_probe_money_actor.py` حرفيًّا (150 صفًّا = 15 فعلَ مالٍ × 10 فاعلين) على `main` c97b692c: EXECUTIVE وLEGISLATIVE وJUDICIAL وAGENT وSYSTEM ‏0/15 ALLOW (DENY بـR-003-1) · TREASURY ‏15/15 ALLOW · وROYAL وHUMAN وSTATE وINSTITUTION ‏15/15 ALLOW (سؤالُ التوجيهِ 33 § 4 — يُعرَضُ في ورقةِ A1 لا يُقرَّر)
- `d4_before.txt` — `.venv/bin/python tools/audit/sovereign_write_inventory.py` قبلَ الشِّفرة: «لا تعبرُ الحدَّ» = **92**
- `root_suite_baseline.txt` — حزمةُ الجذرِ قبلَ الشِّفرة: 3099 passed · 1 skipped · 2 failed — والفشلانِ كلاهما قانونُ الهويةِ لغيابِ README مجلدِ الأدلّةِ وقتَها (يُسَدُّ بهذا الملفِّ ونظيرِه)، لا فشلٌ وظيفيّ
