# evidence/W-759 — ورقةُ المالكِ A1 (ج)/(د) بالقياس + سؤالُ الفاعلينَ خارجَ الفروع

## التعريف
أدلّةُ القيدِ W-759 (2/3 من دفعةِ W-758..W-760 · التوجيهُ 33 § 1 البندان 3 و4): إعادةُ قياسِ مواضعِ A1 للفئتين (ج) و(د) على الشجرةِ الحاليّة، وقياسُ الفاعلين HUMAN/STATE/INSTITUTION/ROYAL على الأفعالِ الحصريّةِ في المحرّكِ **والبوّابة**. الورقةُ: `docs/audit/A1_CD_OWNER_PAPER.md`.

## النطاق
قراءةٌ وقياسٌ فقط — لا شِفرةَ إنتاج، ولا مساسَ بـ`rules.py`. البندُ `WI-109`.

## المالك
Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-759 · WI-109).

## تاريخ الإنشاء
2026-10-31

## تاريخ آخر تعديل
2026-10-31 (W-759 — الإنشاء)

## المحتويات
- `a1_common_sites.py` + `a1_common_sites.out.txt` — الجردُ الحيُّ لمواضعِ `common/`: **22** (21 عامّةٌ غيرُ محروسة + 1 خاصّ) مقابلَ 28 في W-639.
- `a1cd_remeasure.py` + `a1cd_remeasure.out.txt` — مستدعو (ج) بأداةِ W-639 ومرشِّحِها نفسِه: append 21 (11 داخلَ `_apply`) · الأحداثُ 25+27 ‏43 · EventPublisher 2 · Memory 2 · Experience 2. ومعه إفصاحٌ بـ12 سطرًا متشظّيًا و38 مرشَّحًا جديدًا لم يُعَدّ.
- `a1d_rg_callers.txt` — rg لمستدعي (د) و`record_domain_trace` (27 في 7 ملفّات).
- `engine_probe_exclusive_actors_rerun.txt` — إعادةُ تشغيلِ `W-747/engine_probe_exclusive_actors.py` حرفيًّا؛ مطابقٌ لـ`W-747/probe_after.txt` (HUMAN/STATE/INSTITUTION/ROYAL ‏56/56 ALLOW).
- `gateway_probe_exclusive_actors.py` + `.full.txt` — مسبارٌ جديدٌ على `SovereignGateway`: `review` ‏56/56 allowed للأربعة · `execute` يستدعي المُنفِّذَ 56/56 لـHUMAN وSTATE وINSTITUTION، و0/56 لـROYAL (`RoyalImpersonation`) · AGENT ‏0/56. التشغيل: `PYTHONPATH=. .venv/bin/python docs/audit/evidence/W-759/gateway_probe_exclusive_actors.py`.
