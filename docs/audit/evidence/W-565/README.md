# الدليل — W-565: إصلاحُ حارسِ الأسرارِ أمامَ بايتٍ تالفٍ واحدٍ في التاريخِ

**البندُ:** [`WI-103`](../../governance/work/ACTIVE_WORK.md) · **السندُ:** [`DISC-119`](../../governance/work/DISCOVERIES.md) · **قرارُ المالكِ:** [`Q-66`](../SOVEREIGN_DECISION_REGISTER.md) · **المنسِّقُ الحاضرُ:** GLM-5.3 · **التاريخُ:** 2026-10-21

## 1 · العطبُ المقيسُ (قبل)
- حكمُ CI على `16a99c0` (رأسُ W-560 · التشغيلُ [`39419827128`](https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/39419827128)): مقروءٌ 13/13 · **أحمرُ بوظيفَتَينِ**: Crown Root of Trust (E2.2) · Cross-System Suites (E2.2-G).
- الجذرُ واحدٌ: 3 فحوصٍ فاشلةٍ في `tests/crown/test_w064_secret_scan_exceptions.py` — إنتاجٌ محليٌّ: `3 failed · 2690 passed · 1 skipped`.
- التتبّعُ: `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd8 in position 416700` من `_added_key_lines` في `tools/crown/verify_secret_boundaries.py` — والبايتُ التالفُ (0xd8 منفردٌ · حرفٌ عربيٌّ مبتورٌ) في `evidence/W-560/measurements.log` أُلزِمَ في `16a99c0` فلا يُمحى.

## 2 · الإصلاحُ
1. `tools/crown/verify_secret_boundaries.py` (`_added_key_lines`): فكُّ خرجِ `git log --all -p` بـ`encoding="utf-8", errors="replace"` — الاستبدالُ لا يمسُّ مطابقةَ ASCII لكتلِ PEM فلا خسارةَ في التغطيةِ.
2. `tests/crown/test_w064_secret_scan_exceptions.py`: الفكُّ نفسُه لاستدعاءِ git log في الفحصِ.
3. `evidence/W-560/measurements.log`: إصلاحٌ مؤرَّخٌ للبايتِ بإكمالِ الاقتباسِ من رؤوسِ الإحاطتَينِ المبصومةِ + إفصاحٌ داخلَ الملفِ (الأصلُ التالفُ باقٍ في التاريخِ).
4. فحصُ انحدارٍ جديدٌ: `tests/crown/test_w565_secret_history_decode.py` — (أ) استنساخٌ كاملُ العمقِ + بايتٌ تالفٌ ⇒ الحارسُ يحكُمُ `PASS: 12/12` (كانَ ينهارُ) · (ب) زرعُ كتلةِ PEM ثمَّ حذفُها منَ الشجرةِ ⇒ تُلتقَطُ منَ التاريخِ رغمَ البايتِ (`returncode 1` + رسالةُ المخالفةِ).

## 3 · القياسُ (بعد)
- `pytest tests/crown/test_w064_secret_scan_exceptions.py tests/crown/test_w565_secret_history_decode.py` ⇒ **11 ناجحًا** (كانت 3 فاشلةً من w064 — التفصيلُ في `measurements.log`).
- `pytest tests/ -q --collect-only` ⇒ **2696 مُجمَّعًا** (كانَ 2694 · +2 فحصَيِ الانحدارِ) — حُدِّثَت دعوى الحزمةِ في `PROJECT_HANDBOOK.md`.
- القياساتُ الحرفيّةُ في [`measurements.log`](measurements.log).

## 4 · ما لم يُنجَزْ ولماذا
- لا شيءَ من نطاقِ البندِ. **حدٌّ مُعلَنٌ لا يُطوى:** حكمُ CI على رأسِ هذه الدفعةِ يُقاسُ في قيدٍ لاحقٍ (N+1) لأنَّه لا يوجدُ قبلَ الدفعِ.
