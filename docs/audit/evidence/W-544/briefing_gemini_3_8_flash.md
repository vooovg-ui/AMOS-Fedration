# إحاطةُ جولةِ مراجعةِ البندِ: WI-094 — الإعادةُ بمخرجاتٍ خامٍ كاملةٍ (بأمرِ المالكِ Q-63) — نسخةُ المقعدِ `gemini_3_8_flash`

## الهدف: إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ — معبَّأةٌ منَ القالبِ الثابتِ `COUNCIL_BRIEF_TEMPLATE.md` بنسختِهِ المعدَّلةِ في W-542 (sha256 `90465d7ab19345f4b2d74c317277bd7c327521b569a132290d778b2d602773a9`)
## النطاق: جولةُ مراجعةٍ واحدةٌ للبندِ WI-094 تُعيدُ جولةَ W-538 (Q-63 · DISC-116) · نسخةٌ لكلِّ مقعدٍ لا تختلفُ إلّا في جذرِ الدليلِ واسمِ المقعدِ (§ 2.6) · تُبصَمُ sha256 في قيدِ W-544 قبلَ الإطلاقِ
## المالك: بندُ WI-100 (بروتوكولُ المجلسِ · § 3.2)
## تاريخ الإنشاء: 2026-10-20
## تاريخ آخر تعديل: 2026-10-20 (W-544 — التعبئةُ منَ القالبِ المعدَّلِ)

> معبَّأةٌ منَ البندِ نفسِهِ لا منَ تقريرِ منفِّذٍ · مُبصَمةٌ قبلَ إطلاقِ المقاعدِ · لا تُعدَّلُ بعدَ الإطلاقِ.
> **المخرجاتُ خامٌ كاملةٌ — ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ، مهما طالَ المخرجُ** (البروتوكولُ § 4.5). وحكمُكَ يُفحَصُ آليًّا ولا يُحتسَبُ إن رُفِضَ (§ 4.7).

## أ · العقدةُ والمستودعُ

- المستودعُ: `vooovg-ui/AMOS-Fedration`
- العقدةُ المرادُّ مراجعتُها (كاملةً): `be05b45b22c4bf90e7cdbe60724fa439abc7700f`
- **دليلُكَ الخاصُّ (§ 2.6 · لا مسارَ مشتركٌ):** `/home/user/workspace/council_w545/gemini_3_8_flash` — كلُّ ما تكتبُهُ (الاستنساخُ · شجرةُ «قبلُ» · الملفّاتُ المؤقّتةُ · كتلُ RAW · ملفُّ حكمِكَ) داخلَهُ وحدَهُ، **لا تحتَ `/tmp`** ولا في دليلِ مقعدٍ آخرَ.
- التهيئةُ (قبلَ أوامرِ المعاييرِ · لا تُلتقَطُ لأنَّ أداةَ الالتقاطِ داخلَ الاستنساخِ):

```text
mkdir -p /home/user/workspace/council_w545/gemini_3_8_flash/tmp /home/user/workspace/council_w545/gemini_3_8_flash/raw
git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w545/gemini_3_8_flash/repo
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && git checkout be05b45b22c4bf90e7cdbe60724fa439abc7700f
```

## ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` عندَ العقدةِ — حرفيًّا:

```text
| WI-094 | audit-truth | T1 (‏إعادةُ بناءِ مكدَّسِ DISC-100 فوقَ main — سندُ `Q-52`/`Q-56`: قياسُ الجذرِ ووثيقةُ تصميمِ المسارِ (أ) بلا شِفرةٍ في النواة · الأصلُ على المكدَّسِ كانَ `WI-085`/`W-407…W-412` وترقيمُه تصادمَ معَ بندِ `main` فأُعِيدَ بترقيمٍ تالٍ) | Perplexity Computer (بقرارِ المالكِ: «كلاهما معًا (بندان منفصلان)» · 2026-10-18) | مجلسُ المراجعةِ (Q-48) — **حسّاسٌ (نواةُ السيادةِ موضوعًا · Q-H: يُعيدُ المراجعُ تشغيلَ القياسِ ويحفظُ تقريرَه حرفيًّا)** — ولا VERIFIED بيدِ المنفِّذِ (§ 4.3) | IN_REVIEW | docs/audit/DISC100_LEDGER_APPEND_DESIGN.md · docs/audit/evidence/W-447/ | 2026-10-18 | 2026-11-30 | — | مراجعةٌ مستقلّةٌ تُعيدُ تشغيلَ القياسِ (Q-48 · Q-H) — ولا VERIFIED بيدِ المنفِّذِ | — (يُكتَبُ عندَ الإغلاقِ) |
```

كتلةُ البندِ عندَ العقدةِ — حرفيًّا:

```text
المعرِّف: WI-094
النطاق: T1 (audit-truth · سكربتُ قياسٍ في docs/audit/evidence/ ووثيقةٌ في docs/audit/ — وموضوعُهما حسّاسٌ: نواةُ السجلِّ الدستوريِّ)
المالك: Perplexity Computer (بقرارِ المالكِ في تعارضِ النطاقِ: «كلاهما معًا (بندان منفصلان)» · 2026-10-18 18:11 +03)
المراجع: مجلسُ المراجعةِ (Q-48) — **حسّاسٌ (نواةُ السيادةِ موضوعًا · Q-H): يُعيدُ المراجعُ تشغيلَ القياسِ ويحكمُ على نقاطِ الضعفِ المُعلنةِ ويحفظُ تقريرَه حرفيًّا** — ولا VERIFIED بيدِ المنفِّذِ (§ 4.3)
الحالة: IN_REVIEW   (قيدُ W-543: IN_PROGRESS→IN_REVIEW تمهيدًا لإعادةِ الجولةِ بمخرجاتٍ خامٍ كاملةٍ (Q-63) بالقالبِ المعدَّلِ والفاحصِ (W-542) · والسابقُ (تاريخٌ لا يُمحى): VERIFIED→IN_PROGRESS في W-541 · VERIFIED في W-539 · وكلُّ انتقالٍ قيدٌ مستقلٌّ — H3)
المسارات: docs/audit/DISC100_LEDGER_APPEND_DESIGN.md · docs/audit/evidence/W-447/
بدأ: 2026-10-18 · ينتهي الحجز: 2026-11-30

السبب: إعادةُ بناءِ المكدَّسِ الموازيِ (PR #69→#70→#71) فوقَ main بقرارِ المالكِ Q-52/Q-56 —
  وهذا البندُ هو نظيرُ «WI-085/W-407…W-412» على المكدَّسِ: قياسُ الجذرِ بالأدلّة (بلا كودٍ في النواة)
  ووثيقةُ تصميمِ المسارِ (أ). **وترقيمُ البندِ جديدٌ لا تصادمٌ**: رقمُ WI-085 على main مأخوذٌ ببندٍ آخر
  (زرُّ الإيقافِ · DISC-099) فلا يُعادُ استعمالُه — وجدولُ المقابلةِ (القديمُ ↔ الجديد) في أدلّةِ W-447.

خارج النطاق (منعٌ صريح): لا تعديلَ في core/ ولا في أيِّ ملفِّ شِفرةٍ إنتاجيّةٍ أو اختبار · لا رفعَ لـjwt_expire_minutes ·
  لا نقلَ لتجديداتِ الحجوزِ من المكدَّسِ (W-418/W-419 — حجوزُ main القانونيّةُ هي الحاكمة) ·
  ولا فتحَ بندِ الشِّفرةِ (C3) قبلَ READY → RESERVED → IN_PROGRESS بقيودٍ مستقلّةٍ — فهو بندُ WI-095 التابعُ لاحقًا

معيار القبول: (1) سكربتٌ يُعادُ تشغيلُه بأمرٍ واحدٍ يستعملُ الصنفَ الإنتاجيَّ نفسَه على سجلٍّ مؤقّت (2) منحنى
  مقيسٌ قبلُ/بعدُ على الجهازِ نفسِهِ وبالأمرِ نفسِهِ في أدلّةِ WI-095 (3) وثيقةُ تصميمٍ بثلاثةِ بدائلَ
  ونقاطِ ضعفِها (4) جدولُ مقابلةٍ مكتوبٌ (القديمُ ↔ الجديد) يُحيلُ كلَّ قيدٍ قديمٍ إلى مصيرِه

الدليل المطلوب: .venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py (والممتدُّ وبصمةُ البادئة)
قيد السجلّ: — (يُكتَبُ عندَ الإغلاقِ)

[W-539 · 2026-10-20] VERIFIED بإجماعِ مجلسِ المراجعةِ (Q-59 · جولةُ W-538 · المقاعدُ بـ§ 1.5 · المنسِّقُ Claude Opus 5.5): gemini_3_8_flash · grok_4_7 · kimi_k3
  — كلٌّ استنسخَ عندَ 311d9be وأعادَ تشغيلَ القياسِ بنفسِه (قبلُ a2bbb18 وبعدُ 311d9be على الجهازِ نفسِه وبالأمرِ نفسِه) · الأحكامُ الأصليّةُ وحدَها:
  docs/audit/evidence/W-538/README.md (لا تلخيصَ) · ولا CLOSED إلا بإذنِ المالكِ الصريحِ (§ 4.3) · وحقلُ «المراجع» أعلاهُ يبقى كما كُتِبَ (تعيينُ المراجعينَ قرارُ مالكٍ) — والمسلكُ المعتمدُ لـVERIFIED هو المجلسُ بقرارِ Q-59
Q-H-STATUS: MET docs/audit/evidence/W-538/README.md

[W-541 · 2026-10-20] تصحيحٌ مؤرَّخٌ بأمرِ المالكِ Q-63 (نصُّهُ في SOVEREIGN_DECISION_REGISTER.md): ختمُ «Q-H-STATUS: MET» أعلاهُ
  مبنيٌّ على جولةِ W-538 التي صدرت بتكليفٍ يُرخِّصُ في اقتطاعِ المخرجاتِ (خلافَ § 4.1 · DISC-116) — فلا يُعتدُّ به
  حتى تُعادَ الجولةُ بمخرجاتٍ خامٍ كاملةٍ يجتازُ كلُّ حكمٍ فيها council_verdict_raw_check.py. والتصحيحُ بالإضافةِ لا بالمحوِ:
  السطرُ التالي هو الحاكمُ (آخرُ سطرٍ) · والبندُ VERIFIED→IN_PROGRESS في هذا القيدِ · ولا CLOSED قبلَ الإعادةِ (نصُّ Q-63)
Q-H-STATUS: UNMET — جولةُ W-538 لا يُعتدُّ بها (Q-63 · DISC-116) · تُعادُ الجولةُ بمخرجاتٍ خامٍ كاملة
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في تسجيلِ البندِ W-442 ثمَّ حجزِهِ W-444 · قبلَ أوّلِ دليلٍ W-446/W-447): الفقرةُ «معيار القبول» أعلاهُ بنصِّها. (والحالةُ والتصحيحُ المؤرَّخُ في الكتلةِ تاريخُ البندِ — لا يُغيِّرانِ المعاييرَ.)

## ج · أوامرُ المعاييرِ (منَ البندِ نفسِهِ — كلُّ سطرٍ أمرٌ مكتفٍ بنفسِهِ يُلتقَطُ وحدَهُ)

**طريقةُ التشغيلِ (إلزاميّةٌ · § 4.6):** شغِّلْ كلَّ سطرٍ أدناهُ برقمِهِ n (بترتيبِهِ منَ 1) عبرَ أداةِ الالتقاطِ هكذا — والأمرُ بينَ علامتَي الاقتباسِ **حرفيًّا كما هو**:

```text
python3 /home/user/workspace/council_w545/gemini_3_8_flash/repo/tools/governance/council_raw_capture.py --n <n> --out /home/user/workspace/council_w545/gemini_3_8_flash/raw/<n بخانتين: 01 02 …>.txt '<الأمرُ>'
```

(إن احتوى الأمرُ علامةَ اقتباسٍ مفردةً فمرِّرْهُ بحيثُ يصلُ الأداةَ حرفيًّا — مثلًا بـ`"$(cat <<'EOF' … EOF)"`؛ والمعيارُ أن يطابقَ سطرُ `CMD:` في الكتلةِ السطرَ أدناهُ حرفًا بحرفٍ.)

المعيارُ (1) والشطرُ «بعدُ» من (2) — الدليلُ المطلوبُ في البندِ بأمرِهِ (والممتدُّ وبصمةُ البادئةِ) · ومعها البيئةُ:

```bash
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && git rev-parse HEAD
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && bash tools/dev/bootstrap.sh
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && TMPDIR=/home/user/workspace/council_w545/gemini_3_8_flash/tmp .venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && TMPDIR=/home/user/workspace/council_w545/gemini_3_8_flash/tmp .venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && TMPDIR=/home/user/workspace/council_w545/gemini_3_8_flash/tmp .venv/bin/python docs/audit/evidence/W-447/measure_prefix_digest.py
```

الشطرُ «قبلُ» من (2) — الأمرُ نفسُهُ على الجهازِ نفسِهِ على النواةِ قبلَ تنفيذِ أ-2 (العقدةُ `a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8` = الأبُ المباشرُ لالتزامِ تنفيذِ WI-095 · والسكربتُ يُضيفُ جذرَ شجرتِهِ إلى `sys.path` فيقيسُ نواةَ تلكَ الشجرةِ) · ثمَّ ما تغيّرَ في النواةِ بينَ العقدتينِ · ثمَّ وجودُ ملفّاتِ القياسِ «في أدلّةِ WI-095»:

```bash
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && git worktree add /home/user/workspace/council_w545/gemini_3_8_flash/before a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8
cd /home/user/workspace/council_w545/gemini_3_8_flash/before && TMPDIR=/home/user/workspace/council_w545/gemini_3_8_flash/tmp /home/user/workspace/council_w545/gemini_3_8_flash/repo/.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py
cd /home/user/workspace/council_w545/gemini_3_8_flash/before && TMPDIR=/home/user/workspace/council_w545/gemini_3_8_flash/tmp /home/user/workspace/council_w545/gemini_3_8_flash/repo/.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && git diff --stat a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8 be05b45b22c4bf90e7cdbe60724fa439abc7700f -- core/constitutional_engine/ledger.py
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && ls docs/audit/evidence/W-452/
```

(والشطرُ «في أدلّةِ WI-095» من (2) يُتحقَّقُ منه بوجودِ ملفّاتِ القياسِ بالأمرِ `ls` وحدَهُ — **والحكمُ على المنحنى من تشغيلِكَ أنتَ** لا من تلكَ الملفّاتِ.)

المعياران (3) و(4) — الوثيقةُ وجدولُ المقابلةِ هما مُخرَجا البندِ نفسِهِ (موضوعُ المراجعةِ) · كاملَينِ:

```bash
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && rg -n '^## |^### |^#### ' docs/audit/DISC100_LEDGER_APPEND_DESIGN.md
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && cat docs/audit/DISC100_LEDGER_APPEND_DESIGN.md
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && cat docs/audit/evidence/W-447/MAPPING.md
```

ومنعُ «خارج النطاق» (لا تعديلَ في `core/` ولا في شِفرةٍ إنتاجيّةٍ أو اختبارٍ في التزامِ البندِ):

```bash
cd /home/user/workspace/council_w545/gemini_3_8_flash/repo && git show --stat --format='%H %s' ddcd21746e8f1c4726f7cb7052f45d95edf9631e
```

بعدَ الانتهاءِ (فحصُ § 2.6 · يُعيدُ قائمةَ ما كتبتَهُ):

```bash
find /home/user/workspace/council_w545/gemini_3_8_flash -maxdepth 1
```

## د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)

- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- مُخرَجا البندِ موضوعا المراجعةِ: `docs/audit/DISC100_LEDGER_APPEND_DESIGN.md` · وسكربتا القياسِ و`MAPPING.md` في `docs/audit/evidence/W-447/`
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-52 · Q-56 · Q-48)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ (ملفّاتُ `*.log` و`README.md` في `W-447/` و`W-452/`) ولا أدلّةِ أيِّ جولةٍ سابقةٍ (`evidence/W-538/` وما بعدَها) — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

## هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامٍ كاملةٍ ورموزِ خروجٍ)

1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ (والأمرُ 1 يُثبِتُ العقدةَ).
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ**، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (§ 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ (أشِرْ إلى رقمِ الكتلةِ).
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».

## و · صيغةُ جوابِكَ (ملفُّ الحكمِ يُحفظُ حرفيًّا بلا تحريرٍ · § 4.8)

اكتبْ ملفَّ حكمِكَ في `/home/user/workspace/council_w545/gemini_3_8_flash/VERDICT.md` بهذهِ الصيغةِ — وقسمُ `RAW_OUTPUTS` يُركَّبُ **آليًّا** منْ ملفّاتِ `/home/user/workspace/council_w545/gemini_3_8_flash/raw/*.txt` بترتيبِها (مثلًا `cat /home/user/workspace/council_w545/gemini_3_8_flash/raw/*.txt`) بلا أيِّ نصٍّ بينها:

```
MODEL: <اسمُ النموذجِ كما أعلنتْهُ المنصةُ>
FAMILY: <العائلةُ>
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: be05b45b22c4bf90e7cdbe60724fa439abc7700f
CLONE_PATH: /home/user/workspace/council_w545/gemini_3_8_flash/repo
COMMANDS_RUN:
 1. <الأمرُ 1 حرفيًّا>
 …
 15. <الأمرُ 15 حرفيًّا>
RAW_OUTPUTS:
<كتلُ RAW الخمسَ عشرةَ كما كتبتْها الأداةُ>
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ برقمِ الكتلةِ>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرارُ>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

ثمَّ افحصْ ملفَّكَ بنفسِكَ قبلَ التسليمِ (الفاحصُ نفسُهُ الذي يُحتسَبُ بهِ الحكمُ · § 4.7):

```text
python3 /home/user/workspace/council_w545/gemini_3_8_flash/repo/tools/governance/council_verdict_raw_check.py /home/user/workspace/council_w545/gemini_3_8_flash/VERDICT.md --repo /home/user/workspace/council_w545/gemini_3_8_flash/repo
```

فإن رُفِضَ فأصلحِ **التركيبَ** (لا المخرجَ) وأعِدِ الفحصَ — ولا تُحرِّرْ مخرجًا بيدِكَ أبدًا؛ وإن احتجتَ أعِدِ التقاطَ الأمرِ.

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتِهِ (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وملفُّ حكمِكَ في دليلِكَ يُحفظُ حرفيًّا في المستودعِ (§ 4.8).
