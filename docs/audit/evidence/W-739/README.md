# قيدُ W-739 — تصميمُ M1 (عبورُ المالِ · WI-122) ورقًا · لا شِفرة

## التعريف
أدلّةُ تصميمِ عبورِ الأسطحِ العامّةِ الـ33 في `national_economy` و`federal_state` و`state_treasury` — `docs/audit/M1_MONEY_CROSSING_DESIGN.md` — بأمرِ التوجيهِ 29 (D30): «WI-085 تصميم (طلبته في 28) وM1 تصميم. كلاهما بلا شفرة، وكلاهما لا يتوقف على المجلس».

## النطاق
قراءةٌ ساكنةٌ للشِّفرةِ ومسبارٌ للمحرّكِ الدستوريِّ وحدَه على سجلٍّ مؤقّت. لا تغييرَ في الشِّفرةِ ولا في `core/` (K1). السؤالُ Q-83 مقيَّدٌ في القيدِ نفسِه، وWI-122 READY → RESERVED.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-739 · البندُ WI-122).

## تاريخ الإنشاء
2026-10-29

## المحتويات

| الملفّ | ما هو | النتيجة المقيسة |
|---|---|---|
| `m1_surface_scan.py` | مسحٌ بالـAST للأسطحِ الـ33 من `write_inventory_p13.json` | — |
| `m1_surface_scan_output.txt` | مخرجُه (`python3 docs/audit/evidence/W-739/m1_surface_scan.py` · EXIT 0) | `surfaces=33` · `disburse` 3 · `core` 3 · `delegation` 9 · `guard` 0 |
| `engine_probe_money_actor.py` | مسبارُ `ConstitutionalEngine.evaluate` لـ15 فعلًا ماليًّا × 10 فاعلين | — |
| `engine_probe_output.txt` | مخرجُه (`.venv/bin/python docs/audit/evidence/W-739/engine_probe_money_actor.py` · EXIT 0) | 150 صفًّا · EXECUTIVE/LEGISLATIVE/JUDICIAL ⇒ DENY `R-003-1` على الـ15 · TREASURY ⇒ ALLOW 15 · AGENT/SYSTEM/STATE/INSTITUTION ⇒ ALLOW 15 (Q-68 غيرُ مُنفَّذ) |
| `design_measurements.txt` | 9 أوامرَ ومخرجُها خامًا | المفوِّضانِ (l.1460→1514 · l.1012→1046) · § 3.5 مُصلَحٌ (l.854) · الاستثناءُ زوجا `gov.case.open` · `guard_declared` صفرٌ في الملفّاتِ الثلاثة |
| `ci/` | واجبُ N+1 لدفعةِ W-737/W-738 (PR #199) | حمولاتُ CI والمصفوفةِ على `62f8a897` وأحكامُ الفاحصِ EXIT=0 — التفصيلُ في `ci/README.md` |

## ما لم يُقَس
- لا سطحَ ماليٌّ شُغِّلَ محروسًا؛ المسبارُ لا يمرُّ بالجسرِ ولا بالحدّ.
- نافذةُ التسلسلِ لمركَّباتِ النواةِ الثلاثة (Q-83 (أ)) غيرُ مقيسةٍ بمسبار.
- المسحُ اسميٌّ بعمقٍ واحد؛ نقاطُ HTTP والإرسالُ الديناميكيُّ غيرُ محلولة.

## تاريخ آخر تعديل
2026-10-29 (W-739 — القيدُ نفسُه)
