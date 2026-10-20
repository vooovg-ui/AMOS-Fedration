# حكمُ مقعدِ المجلسِ — gemini_3_8_flash (عائلةُ Google · Gemini) · جولةُ WI-094 (W-538)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-094 (بروتوكولُ Q-59 · بندُ WI-100) — لا تحريرَ ولا تلخيصَ. المصدرُ: آخرُ رسالةٍ للمقعدِ كما حفظَها سجلُّ المنصةِ لجلستِهِ (`subagents/…/turns/turn_0001.md`) — منسوخةٌ آليًّا لا يدويًّا.

## النطاق
حكمُ مقعدٍ واحدٍ على البندِ WI-094 بإحاطتِهِ المبصومةِ في W-537 (sha256 `ce8660e5a1c8260ed8793f376e93c5bec9e2d936602d2fd38ff9f0c02acfdd2f`) عندَ العقدةِ `311d9be905b6d1d8a61e1a1155bd8bfa86a031e5`.

## المالك
بندُ WI-100 (المنسِّقُ: Perplexity Computer · النموذجُ المنسِّقُ الحاضرُ Claude Opus 5.5 (عائلةُ Anthropic) كما أعلنتْهُ المنصةُ — منسِّقٌ لا مُصوِّتٌ).

## تاريخ الإنشاء
2026-10-20

## تاريخ آخر تعديل
2026-10-20 (W-538 — حفظُ الحكمِ بعدَ اكتمالِ المقاعدِ كلِّها · § 2.3)

---

MODEL: gemini_3_8_flash
FAMILY: Gemini
RUN_DATE: 2026-10-20 03:20 +00:00
NODE: 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5
CLONE_PATH: /home/user/workspace/council_w538/gemini_3_8_flash/repo
COMMANDS_RUN:
1. mkdir -p /home/user/workspace/council_w538/gemini_3_8_flash/tmp && git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w538/gemini_3_8_flash/repo && cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && git checkout 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5
2. cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && bash tools/dev/bootstrap.sh
3. export TMPDIR=/home/user/workspace/council_w538/gemini_3_8_flash/tmp && cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && .venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py; echo "EXIT=$?"
4. export TMPDIR=/home/user/workspace/council_w538/gemini_3_8_flash/tmp && cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && .venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400; echo "EXIT=$?"
5. export TMPDIR=/home/user/workspace/council_w538/gemini_3_8_flash/tmp && cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && .venv/bin/python docs/audit/evidence/W-447/measure_prefix_digest.py; echo "EXIT=$?"
6. cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && git worktree add /home/user/workspace/council_w538/gemini_3_8_flash/before a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8
7. export TMPDIR=/home/user/workspace/council_w538/gemini_3_8_flash/tmp && cd /home/user/workspace/council_w538/gemini_3_8_flash/before && /home/user/workspace/council_w538/gemini_3_8_flash/repo/.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py; echo "EXIT=$?"
8. export TMPDIR=/home/user/workspace/council_w538/gemini_3_8_flash/tmp && cd /home/user/workspace/council_w538/gemini_3_8_flash/before && /home/user/workspace/council_w538/gemini_3_8_flash/repo/.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400; echo "EXIT=$?"
9. cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && git diff --stat a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5 -- core/constitutional_engine/ledger.py; echo "EXIT=$?"
10. cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && ls docs/audit/evidence/W-452/; echo "EXIT=$?"
11. cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && rg -n '^## |^### |^#### ' docs/audit/DISC100_LEDGER_APPEND_DESIGN.md; echo "EXIT=$?"
12. cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && cat docs/audit/evidence/W-447/MAPPING.md; echo "EXIT=$?"
13. cd /home/user/workspace/council_w538/gemini_3_8_flash/repo && git show --stat --format='%H %s' ddcd21746e8f1c4726f7cb7052f45d95edf9631e; echo "EXIT=$?"
14. find /home/user/workspace/council_w538/gemini_3_8_flash -maxdepth 1; echo "EXIT=$?"
RAW_OUTPUTS:
--- [1] clone & checkout ---
Cloning into '/home/user/workspace/council_w538/gemini_3_8_flash/repo'...
HEAD is now at 311d9be W-536: WI-082 IN_PROGRESS → IN_REVIEW (H3) بعدَ إصلاحِ W-535 — لا شِفرةَ
EXIT=0

--- [2] bootstrap.sh ---
• الجذر: /home/user/workspace/council_w538/gemini_3_8_flash/repo
• ثُبِّتَ خُطّافُ pre-push (يُشغِّلُ حرسَ ما قبلَ الدفعِ على كلِّ دفعٍ — WI-078)
• إنشاءُ بيئةٍ معزولةٍ في .venv
• تركيبُ تبعيّاتِ الجذر (requirements-dev.txt)
• تركيبُ حزمةِ الخدماتِ (قد تطولُ: تبعيّاتٌ كثيرة)
• تركيبُ ruff==0.6.9 (‏المُثبَّتُ في .github/workflows/ci.yml)
✓ البيئةُ جاهزة. للتنشيطِ في جلسةٍ جديدة: source .venv/bin/activate
EXIT=0

--- [3] measure_ledger_append.py (on 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5 - "after") ---
# قياسُ زمنِ append() في ConstitutionalLedger بدلالةِ N — DISC-100 · WI-085 · W-411
# commit: 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200] · appends/N: 20 · verify reps: 5

     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
------------------------------------------------------------------------------
   200 |            0.444 |            4.180 |          0.109 |        0.075
   400 |            0.654 |            7.732 |          0.116 |        0.199
   800 |            1.048 |           15.423 |          0.120 |        0.613
  1600 |            1.763 |           30.578 |          0.106 |        1.735
  3200 |            3.163 |           63.641 |          0.112 |        5.826

# النسبُ بينَ نقاطٍ متتاليةٍ (N يتضاعف): خطّيٌّ ⇒ ~2 · تربيعيٌّ ⇒ ~4
        N→2N |  append × |  verify × | cumulative ×
  200→400    |      1.47 |      1.85 |         2.64
  400→800    |      1.60 |      1.99 |         3.07
  800→1600   |      1.68 |      1.98 |         2.83
 1600→3200   |      1.79 |      2.08 |         3.36

# ملاءمةٌ خطّيّة: append_ms(N) ≈ 0.297 + 0.901·N/1000   (R² = 0.9994)
#   ⇒ كلفةُ القيدِ الواحدِ في كلِّ إلحاقٍ ≈ 0.9 µs · والتراكميُّ ≈ a·N + b·N²/2 (تربيعيٌّ في N)
#   استقراءٌ (لا قياس): append عند N=19119 ≈ 17.5 ms
#   استقراءٌ (لا قياس): append عند N=50000 ≈ 45.3 ms
# سلامةُ السلسلةِ بعدَ القياس: سليمة
EXIT=0

--- [4] measure_ledger_append.py --sizes 200..6400 (on 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5 - "after") ---
# قياسُ زمنِ append() في ConstitutionalLedger بدلالةِ N — DISC-100 · WI-085 · W-411
# commit: 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200, 6400] · appends/N: 20 · verify reps: 5

     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
------------------------------------------------------------------------------
   200 |            0.431 |            4.110 |          0.108 |        0.073
   400 |            0.649 |            7.920 |          0.113 |        0.180
   800 |            1.008 |           15.038 |          0.108 |        0.514
  1600 |            1.754 |           32.114 |          0.108 |        1.690
  3200 |            3.110 |           68.200 |          0.120 |        5.708
  6400 |            6.061 |          131.632 |          0.109 |       21.021

# النسبُ بينَ نقاطٍ متتاليةٍ (N يتضاعف): خطّيٌّ ⇒ ~2 · تربيعيٌّ ⇒ ~4
        N→2N |  append × |  verify × | cumulative ×
  200→400    |      1.50 |      1.93 |         2.48
  400→800    |      1.55 |      1.90 |         2.85
  800→1600   |      1.74 |      2.14 |         3.28
 1600→3200   |      1.77 |      2.12 |         3.38
 3200→6400   |      1.95 |      1.93 |         3.68

# ملاءمةٌ خطّيّة: append_ms(N) ≈ 0.275 + 0.902·N/1000   (R² = 0.9998)
#   ⇒ كلفةُ القيدِ الواحدِ في كلِّ إلحاقٍ ≈ 0.9 µs · والتراكميُّ ≈ a·N + b·N²/2 (تربيعيٌّ في N)
#   استقراءٌ (لا قياس): append عند N=19119 ≈ 17.5 ms
#   استقراءٌ (لا قياس): append عند N=50000 ≈ 45.4 ms
# سلامةُ السلسلةِ بعدَ القياس: سليمة
EXIT=0

--- [5] measure_prefix_digest.py ---
# كلفةُ مكوّناتِ البديلينِ (محاكاةُ قياسٍ لا تنفيذ) مقابلَ التحقّقِ الكاملِ — DISC-100 · WI-085 · W-411
# commit: 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5 · reps: 7
# البناءُ هنا بكتابةِ أسطرٍ صحيحةِ السلسلةِ مباشرةً (لا بـappend) لتجنّبِ الكلفةِ التربيعيّةِ في التحضير؛
# ثمَّ يُتحقَّقُ من السلسلةِ بالصنفِ الإنتاجيِّ قبلَ القياس.

     N |      bytes | verify_full_ms | prefix_digest_ms | stat_tail_ms | full/digest
--------------------------------------------------------------------------------------
   200 |     210580 |          3.687 |            0.176 |       0.0276 |        20.9
   400 |     421380 |          7.369 |            0.343 |       0.0276 |        21.5
   800 |     842980 |         14.799 |            0.699 |       0.0275 |        21.2
  1600 |    1687380 |         30.646 |            1.422 |       0.0277 |        21.5
  3200 |    3376980 |         65.313 |            2.850 |       0.0279 |        22.9
  6400 |    6756180 |        135.471 |            5.748 |       0.0277 |        23.6
 12800 |   13520180 |        284.961 |           12.403 |       0.0278 |        23.0
EXIT=0

--- [6] git worktree add before a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8 ---
Preparing worktree (detached HEAD a2bbb18)
HEAD is now at a2bbb18 W-451: WI-095 RESERVED → IN_PROGRESS (H3)
EXIT=0

--- [7] measure_ledger_append.py (on a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8 - "before") ---
# قياسُ زمنِ append() في ConstitutionalLedger بدلالةِ N — DISC-100 · WI-085 · W-411
# commit: a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200] · appends/N: 20 · verify reps: 5

     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
------------------------------------------------------------------------------
   200 |            4.116 |            4.053 |          0.106 |        0.425
   400 |            7.907 |            7.689 |          0.124 |        1.670
   800 |           15.569 |           15.472 |          0.150 |        6.441
  1600 |           32.875 |           31.946 |          0.108 |       25.869
  3200 |           64.177 |           63.811 |          0.122 |      104.163

# النسبُ بينَ نقاطٍ متتاليةٍ (N يتضاعف): خطّيٌّ ⇒ ~2 · تربيعيٌّ ⇒ ~4
        N→2N |  append × |  verify × | cumulative ×
  200→400    |      1.92 |      1.90 |         3.93
  400→800    |      1.97 |      2.01 |         3.86
  800→1600   |      2.11 |      2.06 |         4.02
 1600→3200   |      1.95 |      2.00 |         4.03

# ملاءمةٌ خطّيّة: append_ms(N) ≈ -0.040 + 20.136·N/1000   (R² = 0.9997)
#   ⇒ كلفةُ القيدِ الواحدِ في كلِّ إلحاقٍ ≈ 20.1 µs · والتراكميُّ ≈ a·N + b·N²/2 (تربيعيٌّ في N)
#   استقراءٌ (لا قياس): append عند N=19119 ≈ 384.9 ms
#   استقراءٌ (لا قياس): append عند N=50000 ≈ 1006.8 ms
# سلامةُ السلسلةِ بعدَ القياس: سليمة
EXIT=0

--- [8] measure_ledger_append.py --sizes 200..6400 (on a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8 - "before") ---
# قياسُ زمنِ append() في ConstitutionalLedger بدلالةِ N — DISC-100 · WI-085 · W-411
# commit: a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200, 6400] · appends/N: 20 · verify reps: 5

     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
------------------------------------------------------------------------------
   200 |            4.186 |            4.045 |          0.111 |        0.510
   400 |            7.891 |            7.795 |          0.115 |        1.706
   800 |           15.258 |           15.016 |          0.145 |        6.422
  1600 |           30.930 |           30.552 |          0.108 |       25.691
  3200 |           63.666 |           61.480 |          0.105 |      103.528
  6400 |          132.306 |          127.347 |          0.118 |      432.325

# النسبُ بينَ نقاطٍ متتاليةٍ (N يتضاعف): خطّيٌّ ⇒ ~2 · تربيعيٌّ ⇒ ~4
        N→2N |  append × |  verify × | cumulative ×
  200→400    |      1.89 |      1.93 |         3.34
  400→800    |      1.93 |      1.93 |         3.76
  800→1600   |      2.03 |      2.03 |         4.00
 1600→3200   |      2.06 |      2.01 |         4.03
 3200→6400   |      2.08 |      2.07 |         4.18

# ملاءمةٌ خطّيّة: append_ms(N) ≈ -1.081 + 20.692·N/1000   (R² = 0.9995)
#   ⇒ كلفةُ القيدِ الواحدِ في كلِّ إلحاقٍ ≈ 20.7 µs · والتراكميُّ ≈ a·N + b·N²/2 (تربيعيٌّ في N)
#   استقراءٌ (لا قياس): append عند N=19119 ≈ 394.5 ms
#   استقراءٌ (لا قياس): append عند N=50000 ≈ 1033.5 ms
# سلامةُ السلسلةِ بعدَ القياس: سليمة
EXIT=0

--- [9] git diff --stat a2bbb186..311d9be9 -- core/constitutional_engine/ledger.py ---
 core/constitutional_engine/ledger.py | 127 +++++++++++++++++++++++++++++++----
 1 file changed, 113 insertions(+), 14 deletions(-)
EXIT=0

--- [10] ls docs/audit/evidence/W-452/ ---
README.md
measure_after_default.log
measure_after_extended.log
mutation_kills.log
mutation_kills.py
services_tests.log
tests_green.log
EXIT=0

--- [11] rg -n '^## |^### |^#### ' docs/audit/DISC100_LEDGER_APPEND_DESIGN.md ---
17:## 0 · ما تُنفِّذُه هذه الوثيقةُ وما لا تُنفِّذُه
23:## 1 · المشكلةُ مقيسةً
25:### 1.1 الشِّفرةُ اليوم
37:### 1.2 المنحنى (مقيسٌ اليوم)
53:#### 1.2.1 إعادةُ القياسِ عندَ إعادةِ البناءِ (2026-10-18 · جهازُ التنفيذِ · `W-447`)\n71:### 1.3 الأثرُ في CI (مقيسٌ في W-406 · واستنتاجٌ مُعلَن)
76:### 1.4 أنَّه عيبُ إنتاجٍ لا عيبُ اختبار
80:## 2 · ما يجبُ أن يبقى (الخاصّيّاتُ المحفوظة)
92:## 3 · قيدٌ تصميميٌّ مقيس: كائناتُ السجلِّ كثيرةٌ في العمليّةِ الواحدة
104:## 4 · البدائل
115:### 4.1 البديلُ أ-1 — بصمةُ الملفِّ + الذيلُ + تحقّقٌ كاملٌ كلَّ K (اقتراحُ المستشار)
133:### 4.2 البديلُ أ-2 — بصمةُ بايتاتِ البادئةِ المُتحقَّقِ منها في كلِّ إلحاق (بلا نافذة)
153:### 4.3 البديلُ أ-3 — أ-1 في كلِّ إلحاقٍ + بصمةُ البادئةِ كلَّ K (هجين)
160:### 4.4 ما رُفِضَ ولماذا
166:## 5 · المقارنة
177:## 6 · فحوصُ قتلِ التحويرات (تُكتَبُ في بندِ C3 لا هنا)
196:## 7 · قياسُ القبولِ في بندِ C3
203:## 8 · أسئلةٌ مفتوحة
210:## 9 · ما لم أفعلْه (بصدق)
EXIT=0

--- [12] cat docs/audit/evidence/W-447/MAPPING.md ---
# جدولُ مقابلةِ إعادةِ بناءِ المكدَّسِ (سندُ `Q-52`/`Q-56` · `W-447`)

<!--
الهدف: إعلانُ مصيرِ كلِّ قيدٍ وبندٍ من المكدَّسِ الموازي القديمِ في إعادةِ البناءِ فوقَ main — سندُ Q-52/Q-56
النطاق: توثيقُ المصيرِ فقط · لا يُنشئُ حقيقةً تقنيّةً ولا يحكمُ على مضمونِ القيودِ (ذلك للمراجعةِ المستقلّة)
-->

المكدَّسُ القديم: الفروع `wi-082-stage3` → `wi-085-ledger-append-design` → `wi-086-ledger-a2` (رأسُها `1588b44` · عقدةُ القياسِ `6bd591a`) — قيودُه `W-402`…`W-428` لم تكن قانونيّةً على main (القانونيُّ: `W-402…W-406` من PR #72 ثمَّ `W-407…` من PR #74 فما بعدَه · `Q-52`). وهذا الجدولُ يُعلِنُ مصيرَ كلِّ قيدٍ وقديمِ بنودِه في البناءِ الجديدِ فوقَ `main` (`fc59da6` →).

## 1 · قيودُ المكدَّس ← مصيرُها في البناءِ الجديد

| القيدُ القديم | موضوعُه | المصيرُ في البناءِ | السندُ/السبب |
|---|---|---|---|
| `W-402`…`W-406` | `WI-082` مرحلة 3 (هجرةُ `register_identity` عبرَ `spawn_agent`) | **قانونيٌّ أصلًا على main** (PR #72 · سجلُّ الإكمال) — لا يُعاد · **وشِفرةُ البندِ مرتدّةٌ على main بقرارِ `Q-51` ①** وتُعادُ فوقَ العلاجِ في خطوةٍ لاحقةٍ (`Q-51` ③) لا في هذه الدفعة | `Q-52` (القانونيُّ = قيودُ PR #72) · `Q-51` ①③ |
| `W-407`…`W-412` | `WI-085` (قياسُ جذرِ DISC-100 + وثيقةُ التصميم) | **أُعيدَ بناؤُه**: البندُ الجديدُ `WI-094` · قيودُ `W-442`…`W-448` · الوثيقةُ والأدلّةُ منقولةٌ بقياسٍ مُعادٍ (`W-447`) — **ورقمُ `WI-085` نفسُه لا يُعادُ** (مأخوذٌ على main ببندِ زرِّ الإيقافِ · DISC-099) | `Q-52`/`Q-56` · قرارُ المالكِ `Q-58` |
| `W-413` | قرارُ المالكِ في DISC-100: مسارُ (أ) بالبديلِ أ-2 (لا K) | **مؤكَّدٌ أصلًا على main** بـ`Q-56` (W-429) · ونُقِلَ نصُّهُ التاريخيُّ في `W-446` | `Q-56` |
| `W-414` | قرارُ المالكِ في Q-35: ② تبقى المخالفتانِ | **نُقِلَ تاريخيًّا** في `W-446` مجمَّعًا ثمَّ أُفردَ بقيدٍ مستقلٍّ في `W-458` (إضافةٌ مؤرَّخةٌ في § Q-35) | `Q-52`/`Q-56` |
| `W-415` | قرارُ المالكِ في Q-38: (ج) كاشفٌ ثانٍ (+2 خطُّ الأساسِ بسببٍ مُعلَن) | **نُقِلَ تاريخيًّا** في `W-446` مجمَّعًا ثمَّ أُفردَ بقيدٍ مستقلٍّ في `W-459` (إضافةٌ مؤرَّخةٌ في § Q-38) — **ولا يُنفَّذُ الكاشفُ في هذه الدفعةِ** (بندٌ مستقلٌّ لاحقٌ) | `Q-52`/`Q-56` |
| `W-416` | تأكيدُ المالكِ في Q-25: ① يشملُ 29 | **نُقِلَ تاريخيًّا** في `W-446` مجمَّعًا ثمَّ أُفردَ بقيدٍ مستقلٍّ في `W-457` (إضافةٌ مؤرَّخةٌ في § Q-25) | `Q-52`/`Q-56` |
| `W-417` | قرارُ المالكِ في WI-082 ③: الإيقافُ والتقاعدُ مسموحانِ دائمًا | **نُقِلَ تاريخيًّا** في `W-446` مجمَّعًا ثمَّ أُفردَ بقيدٍ مستقلٍّ في `W-460` (قسمُ النقلِ) | `Q-52`/`Q-56` |
| `W-418`/`W-419` | تجديدُ حجوزِ Driving H (17) والمنفِّذِ (24) إلى 2026-11-30 | **لا يُنقَل**: تجديداتُ main القانونيّةُ (التسوياتُ الأولى والثانيةُ · `Q-50`…`Q-54`) هي الحاكمةُ — استحقاقُ بنودِ main المقيسُ اليومَ 2026-10-31 (بنودُ Driving H) و2026-11-15/2026-11-30 (الأحدثُ) — **قيسَ صفًّا صفًّا** عندَ إعدادِ هذا الجدولِ (أوامرُ `grep` على صفوفِ `ACTIVE_WORK.md` في `W-446`) | `Q-52` (القانونيُّ = main+PR #74) |
| `W-420` | إذنُ تعديلِ ترويسةِ PROJECT_HANDBOOK.md وخلايا الحجمِ | **نُقِلَ تاريخيًّا** في `W-446` (قسمُ النقلِ) — ويُعمَلُ به عندَ تحديثِ الترويسةِ | `Q-52`/`Q-56` |
| `W-421` | رأسُ الدفعةِ (10 بنودٍ · كلُّ عملِها وثائقُ) — حكمُ CI على عقدتِه | **تاريخيٌّ على المكدَّسِ لا يُنقَل** (كانَ حكمًا على عقدةِ المكدَّسِ `6bd591a` لا على بناءِ main الجديدِ) — وحكمُ CI على رأسِ البناءِ الجديدِ يُقيَّدُ في القيدِ التالي (مبدأُ «حكمُ الدفعةِ N في الدفعةِ N+1») | حكمُ عقدةٍ لا يُعاد |
| `W-422`…`W-427` | `WI-086` (تنفيذُ أ-2 في `ConstitutionalLedger.append()`) | **أُعيدَ بناؤُه**: البندُ الجديدُ `WI-095` · قيودُ `W-449`…`W-453` · الشِّفرةُ والفحوصانِ منقولانِ **بايتًا ببايت** (sha256 مطابقٌ) وكلُّ قياسٍ أُعيدَ تشغيلُه (`W-452`) — **ورقمُ `WI-086` نفسُه لا يُعادُ** (مأخوذٌ على main ببندِ تجديدِ `AUTH_HEADERS`) | `Q-52`/`Q-56` · قرارُ المالكِ `Q-58` |
| `W-428` | حكمُ CI على رأسِ المكدَّسِ (عقدةُ `1588b44`) | **تاريخيٌّ على المكدَّسِ لا يُنقَل** — وحكمُ CI على رأسِ البناءِ الجديدِ يُقيَّدُ في القيدِ التالي | حكمُ عقدةٍ لا يُعاد |

## 2 · بنودُ المكدَّسِ القديمة ← بنودُ البناءِ الجديد

| البندُ القديمُ (على المكدَّسِ) | نطاقُه | البندُ الجديدُ (على main) | ملاحظةُ الترقيمِ |
|---|---|---|---|
| `WI-082` (مرحلة 3) | هجرةُ `register_identity` عبرَ `spawn_agent` | لا بندًا جديدًا في هذه الدفعةِ (الشِّفرةُ تُعادُ فوقَ العلاجِ · `Q-51` ③) | الرقمُ قانونيٌّ على main |
| `WI-085` | قياسُ جذرِ DISC-100 + وثيقةُ التصميم | `WI-094` | رقمُ `WI-085` مأخوذٌ على main ببندٍ آخرَ (DISC-099) |
| `WI-086` | تنفيذُ أ-2 | `WI-095` | رقمُ `WI-086` مأخوذٌ على main ببندٍ آخرَ (تجديدُ `AUTH_HEADERS` · قرارُ المالكِ `Q-58`: «كلاهما معًا (بندان منفصلان)») |

## 3 · ما لم يُنقَل عمدًا (مُعلَنٌ لا مسكوتٌ عنه)

- **شِفرةُ `WI-082` مرحلة 3** — مرتدّةٌ على main بقرارِ `Q-51` ① وتُعادُ فوقَ العلاجِ (`Q-51` ③) في خطوةٍ لاحقةٍ مستقلّةٍ.
- **تجديداتُ الحجوزِ** (`W-418`/`W-419`) — تجديداتُ main القانونيّةُ هي الحاكمةُ (قيسَت صفًّا صفًّا · انظر § 1).
- **أحكامُ CI على عقدِ المكدَّسِ** (`W-421`/`W-428`) — أحكامٌ على عقدٍ أخرى لا على البناءِ الجديدِ.
- **تقاريرُ جولاتِ قناةِ الاستشارةِ على المكدَّسِ** — كانت أحكامًا على شجرةِ المكدَّسِ؛ والمراجعةُ على البناءِ الجديدِ تُعادُ بقيودِه.

**حدودُ هذا الجدولِ:** يوثِّقُ مصيرَ القيودِ والبنودِ لا صدقَ مضمونِها — والحكمُ على المضمونِ للمراجعةِ المستقلّةِ (`Q-48` · `Q-H`) لا للمنفِّذِ.
EXIT=0

--- [13] git show --stat ddcd21746e8f1c4726f7cb7052f45d95edf9631e ---
ddcd21746e8f1c4726f7cb7052f45d95edf9631e W-447: WI-094 — وثيقةُ تصميمِ المسارِ (أ) وقياسُ الجذرِ (نقلٌ من W-411 مع إعادةِ قياسٍ) + جدولُ مقابلةِ المكدَّس

 docs/audit/COMPLETION_LEDGER.md                    |   1 +
 docs/audit/DISC100_LEDGER_APPEND_DESIGN.md         | 215 +++++++++++++++++++++
 docs/audit/evidence/W-447/MAPPING.md               |  37 ++++
 docs/audit/evidence/W-447/README.md                |  57 ++++++
 docs/audit/evidence/W-447/measure_default.log      |  25 +++
 docs/audit/evidence/W-447/measure_extended.log     |  27 +++
 docs/audit/evidence/W-447/measure_ledger_append.py | 204 +++++++++++++++++++
 docs/audit/evidence/W-447/measure_prefix_digest.log |  14 ++
 docs/audit/evidence/W-447/measure_prefix_digest.py | 118 +++++++++++
 docs/governance/work/ACTIVE_WORK.md                |   2 +-
 10 files changed, 699 insertions(+), 1 deletion(-)
EXIT=0

--- [14] find /home/user/workspace/council_w538/gemini_3_8_flash -maxdepth 1 ---
/home/user/workspace/council_w538/gemini_3_8_flash
/home/user/workspace/council_w538/gemini_3_8_flash/repo
/home/user/workspace/council_w538/gemini_3_8_flash/tmp
/home/user/workspace/council_w538/gemini_3_8_flash/before
EXIT=0
VERDICT_PER_CRITERION:
- معيار القبول (1): نعم — السكربت docs/audit/evidence/W-447/measure_ledger_append.py يُعاد تشغيله بأمر واحد، ويستخدم الصنف الإنتاجي ConstitutionalLedger على سجل مؤقت موجّه عبر TMPDIR، وانتهى بـ EXIT=0 مع تأكيد سلامة السلسلة ("سلامةُ السلسلةِ بعدَ القياس: سليمة"). وكذلك سكربت docs/audit/evidence/W-447/measure_prefix_digest.py نُفِّذ بأمر واحد وانتهى بـ EXIT=0.
- معيار القبول (2): نعم — قيست المنحنيات "قبلُ" و"بعدُ" على الجهاز نفسه وبالأمر نفسه:
  * قبل (العقدة a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8): كلفة القيد append_ms(N) ≈ -1.081 + 20.692·N/1000 وزمن الإلحاق عند N=6400 هو 132.306 ms والزمن التراكمي 432.325 s.
  * بعد (العقدة 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5): كلفة القيد append_ms(N) ≈ 0.275 + 0.902·N/1000 وزمن الإلحاق عند N=6400 هو 6.061 ms (تسريع بمقدار ~22 ضعفاً) والزمن التراكمي 21.021 s.
  * ملفات القياس في أدلة WI-095 متحققة بوجود docs/audit/evidence/W-452/ (شملت measure_after_default.log و measure_after_extended.log و mutation_kills.log وغيرها).
- معيار القبول (3): نعم — وثيقة التصميم docs/audit/DISC100_LEDGER_APPEND_DESIGN.md تتضمن الأقسام 4.1 (البديل أ-1)، 4.2 (البديل أ-2)، 4.3 (البديل أ-3)، ونقاط الضعف والمفاضلة مفصلة في القسمين 4 و 5، وRG أكد وجود الترويسات كاملة.
- معيار القبول (4): نعم — جدول المقابلة docs/audit/evidence/W-447/MAPPING.md مكتوب وموجود ومكتمل، ويحيل كل قيد من قيود المكدس القديم (W-402 إلى W-428) وبنوده (WI-082, WI-085, WI-086) إلى مصيره بوضوح وتفصيل السند.
- شرط خارج النطاق (منع صريح): نعم — الالتزام ddcd21746e8f1c4726f7cb7052f45d95edf9631e اقتصر على وثائق التصميم والأدلة وسجلات الحوكمة دون مساس بـ core/ أو أي كود إنتاجي أو ملفات اختبار، ولم تُرفع مدة jwt_expire_minutes ولم تُنقل تجديدات الحجوز، وبند الشفرة C3 فُصل في WI-095.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: أقر بأنني لم أقرأ شيئاً خارج استنساخي الخاص (/home/user/workspace/council_w538/gemini_3_8_flash) وهذه الإحاطة؛ ولم أطلع على /home/user/workspace/amos أو أي دليل مقعد آخر، واستخدمت TMPDIR الخاص بي حصراً في جميع العمليات المؤقتة.
VERDICT: PASS لكلِّ المعاييرِ
