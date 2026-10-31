# evidence/W-765 — شِفرةُ DISC-148 «ربما طُبِّق» وDISC-149 (الخزانة): المسبارانِ بعدَها والطفراتُ وD-4

## التعريف
أدلّةُ القيدِ W-765: تنفيذُ `Q-88` القرار 1 بالتصميمِ `docs/audit/DISC148_MAYBE_APPLIED_DESIGN.md`، وإصلاحُ مُطبِّقاتِ الخزانةِ الستّةِ غيرِ الذرّيّة (القرار 2 · `DISC-149`). المسبارانِ هما مسبارا W-764 بحرفِهما، شُغِّلا بعدَ الشِّفرة.

## النطاق
`core/sovereignty/enforcement_boundary.py` · `core/sovereignty/compensation.py` · `executive_core/sovereignty_bridge.py` · `executive_core/money_authority.py` · `state_treasury/service.py` · `agent_runtime/population.py` (معوِّضُ المرآة) · وفحوصُها. البندُ `WI-125`.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-765).

## تاريخ الإنشاء
2026-10-31

## تاريخ آخر تعديل
2026-10-31 (W-765 — الإنشاء)

## المحتويات
- `disc148_probe_after.txt` — `docs/audit/evidence/W-764/disc148_probe.py` بعدَ الشِّفرة. يُقارَنُ بـ`W-764/disc148_probe_before.txt` سطرًا بسطر.
- `treasury_atomicity_probe_after.txt` — `W-764/treasury_atomicity_probe.py` بعدَ الشِّفرة. يُقارَنُ بـ`W-764/treasury_atomicity_probe_before.txt`. ووسمُ «ذرّيّ/غيرُ ذرّيّ» فيه يَعُدُّ الصفوف: الحركتانِ تُعوَّضانِ بقيدٍ عكسيٍّ (صفٌّ جديدٌ لا حذف)، فيبقى وسمُهما «غيرُ ذرّيّ» والرصيدُ راجع.
- `mutations.txt` — ثلاثُ طفراتٍ على `enforcement_boundary.py`، كلٌّ منها على نسخةٍ نظيفةٍ ثمّ تُرَدّ: M1 حذفُ «ربما طبَّق» ⇐ 6 + 3 فشل · M2 إسقاطُ المعوِّضِ عن الأثرِ قيدَ التطبيق ⇐ 3 + 3 · M3 وسمُ «لا معوِّضَ قابلٌ للتشغيل» FAILED_RETRYABLE ⇐ 2.
- `d4_inventory_before_614b5233.txt` · `d4_inventory_after.txt` — `tools/audit/sovereign_write_inventory.py` قبلُ (worktree عندَ 614b5233) وبعدُ: **86 ← 86**. الدفعةُ لا تُهاجرُ كتابة.

## ما لم يُقَس
- ذرّيّةُ أيِّ مُطبِّقٍ خارجَ الخزانة. والمُطبِّقاتُ الأخرى لم تُصرِّح، فرفعُها يُغلِقُ المفتاحَ FAILED_FINAL ما لم يكن معوِّضُها مُصرَّحًا بثباتِه. والمقيسُ في المجموعتين: فحصٌ واحدٌ في الإنتاجِ احتاجَ تصريحًا (`_restore_mirror`)، وفحصانِ بنيويّانِ حُدِّثا.
- الفشلُ داخلَ `record_domain_trace` بعدَ كتابةِ التدقيقِ وقبلَ الحدث.
- إعادةُ الحركةِ بالمفتاحِ نفسِه بعدَ التعويضِ تُرفَضُ `EntityStateError` (حركةُ المفتاحِ معكوسة). هذا قِيسَ ولم يُغيَّر.
