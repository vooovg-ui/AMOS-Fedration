# قيدُ W-742 — انتقالُ WI-120 إلى المراجعةِ (H3) + واجبُ N+1 لدفعةِ W-741

## التعريف
الأدلّةُ الخامُّ لقيدِ انتقالٍ ورقيٍّ واحدٍ: `WI-120` `IN_PROGRESS → IN_REVIEW` (قيدٌ مستقلٌّ H3 · § 7.4 من بروتوكولِ المجلسِ) تمهيدًا لجولةِ المجلسِ الواحدةِ المأذونةِ بتوجيهِ المستشارِ 31 § 1 (WI-114 · WI-116 · WI-120 · WI-123 — الجمعُ في الجلسةِ نفسِها Q-72)، وواجبُ N+1 لأحكامِ CI الخاصّةِ بدفعةِ W-741.

## النطاق
البندُ WI-120 (G1 · الدفعاتُ 1–4 + إصلاحُ Q-26 في retire_agent مكتملةً شِفرةً عندَ `97a294c`) · توجيهُ المستشارِ 31 § 1 (إطلاقُ الجولةِ الآن).

## المالك
Perplexity Computer (المنسِّقُ GLM-5.3 · قيدُ W-742 · البندُ WI-120).

## تاريخ الإنشاء
2026-10-30

## الملفّاتُ وأوامرُها

| الملفّ | ما هو | الأمرُ المولِّد |
|---|---|---|
| `ci/prA_7c615969_ci.jobs.json` | حِملُ وظائفِ تشغيلِ CI الكاملِ للعقدةِ 7c615969 (التزامِ 1/3 من W-741) | `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/40979885755/jobs` |
| `ci/prA_7c615969_matrix.jobs.json` | حِملُ وظائفِ تشغيلِ المصفوفةِ على 7c615969 | `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/40979881702/jobs` |
| `ci/prB_f76d7241_ci.jobs.json` | حِملُ وظائفِ تشغيلِ CI الكاملِ للعقدةِ f76d7241 (التزامِ 2/3) | `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/40982137131/jobs` |
| `ci/prB_f76d7241_matrix.jobs.json` | حِملُ وظائفِ تشغيلِ المصفوفةِ على f76d7241 | `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/40982125362/jobs` |
| `ci/prC_97a294c_ci.jobs.json` | حِملُ وظائفِ تشغيلِ CI الكاملِ للعقدةِ 97a294c (التزامِ 3/3) | `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/40984407501/jobs` |
| `ci/prC_97a294c_matrix.jobs.json` | حِملُ وظائفِ تشغيلِ المصفوفةِ على 97a294c | `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/40984401037/jobs` |
| `ci/main_97a294c_ci.jobs.json` | حِملُ وظائفِ تشغيلِ CI الكاملِ على main بعدَ الدمجِ (97a294c) | `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/40987223590/jobs` |
| `ci/main_97a294c_matrix.jobs.json` | حِملُ وظائفِ تشغيلِ المصفوفةِ على main بعدَ الدمجِ | `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/40987223588/jobs` |
| `ci/*.checker.txt` | مخرجاتُ فاحصِ المقروئيّةِ الثمانيةُ حرفيًّا (EXIT 0 ×8 · مقروءٌ أخضرُ على العقدةِ نفسِها) | `ci_verdict_readability.py --from-json <payload> --require-readable --expect-sha <العقدة>` |

## ما لم يُقَس
- لا شيءَ جديدًا لم يُقَسْ — انتقالٌ ورقيٌّ بلا شِفرةٍ: القياساتُ المقيسةُ (فحوصُ الدفعاتِ 1–4 · إصلاحُ Q-26 · الطفرةُ · D-4 95) مقيدةٌ في W-722/W-723/W-724/W-728/W-735/W-736 ولم تتغيّرْ.

## تاريخ آخر تعديل
2026-10-30 (W-742 — القيدُ نفسُه)

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `ci/` — واجبُ N+1 لدفعةِ W-741 (حمولاتٌ ×8 + مخرجاتُ الفاحصِ ×8)
