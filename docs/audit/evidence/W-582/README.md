# استلامُ WI-105 بتوجيهِ المالكِ 17 وقياسُ المرحلةِ 0 (W-582)

## التعريف

دليلُ قيدِ `W-582`: نصُّ توجيهِ المالكِ 17 حرفيًّا · قياساتُ المرحلةِ 0 حيّةً (D-4 · D-5 · D-6 ① · WI-082 · الحوكمة) · وإعادةُ إنتاجِ القسمِ (د) من قياسِ W-581 بسكربتٍ مُلتزَمٍ (`DISC-122`) · وقياسُ D-5 بأمرٍ واحدٍ وفرقُه عن العدِّ اليدويِّ (`DISC-123`).

## النطاق

بندُ `WI-105` (IN_PROGRESS) · قياسٌ لا شِفرةَ إنتاجيّةَ · السكربتانِ يقرآنِ ولا يكتبانِ.

## المالك

Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5).

## تاريخ الإنشاء

2026-10-21

## إعادةُ التشغيل

```
PYTHONPATH=federal/executive/services/src:. .venv/bin/python docs/audit/evidence/W-582/probe_branch_exclusive_agent_system.py
.venv/bin/python docs/audit/evidence/W-582/d5_status_probe.py
```

## المحتويات

- `OWNER_DIRECTIVE_17.md` — حفظُ نصِّ توجيهِ المالكِ 17 حرفيًّا كما وصلَ المنفِّذَ — سندُ الاستلامِ المعلنِ لـWI-105 وكلِّ…
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `ci_jobs_39573575374.api.txt` — ملف تابع
- `d5_status_probe.out.txt` — ملف تابع
- `d5_status_probe.py` — قياسُ D-5 (Q-1…Q-27) بأمرٍ واحدٍ من نصِّ السجلِّ السياديِّ — أوّلُ حالةٍ في قسمِ كلِّ سؤالٍ وآ…
- `phase0_measurements.txt` — W-582 · قياساتُ المرحلةِ 0 (التوجيه 17 § 3) — بيئةُ المنفِّذِ · Python 3.12.15 · 2026-10-21T12…
- `probe_branch_exclusive_agent_system.out.txt` — ملف تابع
- `probe_branch_exclusive_agent_system.py` — إعادةُ إنتاجِ القسمِ (د) من مخرجِ W-581 (ALLOW 54/54 لـAGENT وSYSTEM على أفعالِ _BRANCH_EXCLUS…

## تاريخ آخر تعديل
2026-10-21
