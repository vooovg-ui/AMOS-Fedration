# أدلّةُ W-381 — استثناءُ الدمجِ اليدويِّ الواحدِ لطلبِ الدمجِ #64 (توجيهُ المستشارِ 9 § 1)

## التعريف
أدلّةُ الاستثناءِ المُقيَّدِ الذي أذِنَ به المالكُ عبرَ توجيهِ المستشارِ 9 لعقدةٍ واحدةٍ هي
`81b0071ff6655a3982119ba7f0fde10ed239869e` (رأسُ #64 · W-363…W-380)، ورفضا وجهِ الدمجِ السابقانِ بالرمزِ 2.

## النطاق
عقدةٌ واحدةٌ فقط — **لا يتكرّرُ الاستثناءُ لأيِّ عقدةٍ أخرى** · والإصلاحُ نفسُه بندٌ مستقلٌّ (`WI-083`).

## المالك
Perplexity Computer — بقرارِ المالكِ الواردِ في توجيهِ المستشارِ 9.

## تاريخ الإنشاء
2026-10-16 (W-381)

## التسلسلُ كما وقع (بتوقيتِ الرياض 2026-10-16)

1. **أوّلُ `--merge` حيٍّ (بعدَ إذنِ المالكِ «نعم، ادمجه» 11:18):** `python tools/dev/prepush_gate.py --merge 81b0071…` —
   الحرسُ السبعةُ خضراءُ ثمَّ **رفضٌ مُصنَّفٌ بالرمزِ 2**: «عنوانُ origin غيرُ مفهومٍ لاستخراجِ owner/name منه:
   'https://git-agent-proxy.perplexity.ai/vooovg-ui/AMOS-Fedration.git'» ⇒ `merge_refused_exit2_first.log`.
2. **محاولةٌ ثانيةٌ بإعدادٍ محلّيٍّ مؤقَّت** (عنوانُ origin إلى github.com مع `pushInsteadOf` إلى الوسيط) — فشلت
   بالرمزِ نفسِه لأنَّ إعدادَ البيئةِ العامَّ (`url.….insteadof` في `~/.gitconfig-proxy`) يُعيدُ كتابةَ العنوانِ —
   وأُعيدَ الإعدادُ كما كان ⇒ `merge_refused_exit2_second.log`. **لم يُدفَعْ شيءٌ ولم يتغيّرْ main** (بقيَ `19eab59`).
3. **الاستثناءُ (توجيهُ المستشارِ 9 § 1) بثلاثِ خطواتٍ مستقلّة:**
   - (أ) الحكمُ بأداةِ الحكمِ: `gh api repos/vooovg-ui/AMOS-Fedration/actions/runs/38869869886/jobs` ثمَّ
     `python tools/governance/ci_verdict_readability.py --from-json … --repo vooovg-ui/AMOS-Fedration --require-readable --expect-sha 81b0071ff6655a3982119ba7f0fde10ed239869e`
     ⇒ **`EXIT=0`** · **13 وظيفةً من 13 `success`** · كلُّها على العقدةِ نفسِها ⇒ `verdict_pr64_81b0071.log` · `jobs_38869869886.json`.
   - (ب) الحرسُ السبعةُ محلّيًّا: `python tools/dev/prepush_gate.py` (بلا `--merge`) ⇒ **`EXIT=0`** ⇒ `prepush_gate_local.log`.
   - (ج) `git merge-base --is-ancestor origin/main 81b0071…` صادقٌ (تقديمٌ سريعٌ) ثمَّ
     `TZ=UTC git push origin 81b0071ff6655a3982119ba7f0fde10ed239869e:main` ⇒ **`19eab59..81b0071`** · **`EXIT=0`** ⇒ `push_ff_main.log`.

## الحدودُ المُعلنة
- **حكمُ تشغيلِ `push` على main للعقدةِ `81b0071`** *(أُضيفَ في `W-393`)*: التشغيلُ **38873871966** (AMOS-Federation CI) —
  `ci_verdict_readability.py --require-readable --expect-sha 81b0071…` ⇒ **EXIT=0 · 13/13 success** على العقدةِ نفسِها ⇒
  `verdict_main_push_81b0071.log` · `jobs_main_38873871966.json` · ومصفوفةُ الحقيقةِ (38873871812) success.
- الخُطّافُ (`pre-push`) شغّلَ الحرسَ السبعةَ مرّةً أخرى عندَ الدفعِ وخرجَ أخضرَ (ذيلُ `push_ff_main.log`).

## تاريخ آخر تعديل
2026-10-16

## المحتويات
- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `jobs_38869869886.json` — بيانات مهيكلة
- `merge_refused_exit2_first.log` — ملف تابع
- `merge_refused_exit2_second.log` — ملف تابع
- `prepush_gate_local.log` — ملف تابع
- `push_ff_main.log` — ملف تابع
- `verdict_pr64_81b0071.log` — ملف تابع
