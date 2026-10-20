# حكمُ مقعدِ المجلسِ — grok_4_7 (عائلةُ xAI · Grok) · جولةُ WI-094 (W-538)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-094 (بروتوكولُ Q-59 · بندُ WI-100) — لا تحريرَ ولا تلخيصَ. المصدرُ: آخرُ رسالةٍ للمقعدِ كما حفظَها سجلُّ المنصةِ لجلستِهِ (`subagents/…/turns/turn_0001.md`) — منسوخةٌ آليًّا لا يدويًّا.

## النطاق
حكمُ مقعدٍ واحدٍ على البندِ WI-094 بإحاطتِهِ المبصومةِ في W-537 (sha256 `fffe14545fb7ac5fb5a9d796a830cde5e4984c5c399b0e2e41fa2b018be708e2`) عندَ العقدةِ `311d9be905b6d1d8a61e1a1155bd8bfa86a031e5`.

## المالك
بندُ WI-100 (المنسِّقُ: Perplexity Computer · النموذجُ المنسِّقُ الحاضرُ Claude Opus 5.5 (عائلةُ Anthropic) كما أعلنتْهُ المنصةُ — منسِّقٌ لا مُصوِّتٌ).

## تاريخ الإنشاء
2026-10-20

## تاريخ آخر تعديل
2026-10-20 (W-538 — حفظُ الحكمِ بعدَ اكتمالِ المقاعدِ كلِّها · § 2.3)

---

MODEL: grok_4_7
FAMILY: Grok
RUN_DATE: 2026-10-20 03:34 +00:00
NODE: 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5
CLONE_PATH: /home/user/workspace/council_w538/grok_4_7/repo
COMMANDS_RUN: git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w538/grok_4_7/repo && git checkout 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5; bash tools/dev/bootstrap.sh; TMPDIR=/home/user/workspace/council_w538/grok_4_7/tmp .venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py; TMPDIR=… .venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400; TMPDIR=… .venv/bin/python docs/audit/evidence/W-447/measure_prefix_digest.py; git worktree add /home/user/workspace/council_w538/grok_4_7/before a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8; TMPDIR=… /home/user/workspace/council_w538/grok_4_7/repo/.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py (في before); TMPDIR=… نفسُ المفسّر measure_ledger_append.py --sizes 200,400,800,1600,3200,6400 (في before); git diff --stat a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5 -- core/constitutional_engine/ledger.py; ls docs/audit/evidence/W-452/; rg -n '^## |^### |^#### ' docs/audit/DISC100_LEDGER_APPEND_DESIGN.md; cat docs/audit/evidence/W-447/MAPPING.md; git show --stat --format='%H %s' ddcd21746e8f1c4726f7cb7052f45d95edf9631e; find /home/user/workspace/council_w538/grok_4_7 -maxdepth 1
RAW_OUTPUTS:
--- clone+checkout ---
311d9be905b6d1d8a61e1a1155bd8bfa86a031e5
311d9be W-536: WI-082 IN_PROGRESS → IN_REVIEW (H3) بعدَ إصلاحِ W-535 — لا شِفرةَ
EXIT=0
--- bootstrap ---
• الجذر: /home/user/workspace/council_w538/grok_4_7/repo
• ثُبِّتَ خُطّافُ pre-push
• إنشاءُ بيئةٍ معزولةٍ في .venv
• تركيبُ تبعيّاتِ الجذر (requirements-dev.txt)
• تركيبُ حزمةِ الخدماتِ
• تركيبُ ruff==0.6.9
✓ البيئةُ جاهزة.
EXIT=0
--- measure_ledger_append.py @ 311d9be (TMPDIR=…/grok_4_7/tmp) ---
# commit: 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200] · appends/N: 20 · verify reps: 5
     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
   200 |            0.648 |            7.321 |          0.164 |        0.085
   400 |            0.624 |            8.353 |          0.113 |        0.203
   800 |            0.983 |           15.617 |          0.107 |        0.537
  1600 |            1.741 |           32.520 |          0.110 |        1.716
  3200 |            3.151 |           64.794 |          0.107 |        5.725
  200→400  append ×0.96  verify ×1.14  cumulative ×2.39
  400→800  append ×1.58  verify ×1.87  cumulative ×2.64
  800→1600 append ×1.77  verify ×2.08  cumulative ×3.20
 1600→3200 append ×1.81  verify ×1.99  cumulative ×3.34
# ملاءمةٌ خطّيّة: append_ms(N) ≈ 0.352 + 0.869·N/1000   (R² = 0.9944)
# ⇒ كلفةُ القيدِ الواحدِ ≈ 0.9 µs
# استقراء: N=19119 ≈ 17.0 ms · N=50000 ≈ 43.8 ms
# سلامةُ السلسلةِ بعدَ القياس: سليمة
EXIT=0
--- measure_ledger_append.py --sizes 200,400,800,1600,3200,6400 @ 311d9be ---
# commit: 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5
     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
   200 |            0.448 |            4.058 |          0.110 |        0.113
   400 |            0.657 |            7.808 |          0.113 |        0.233
   800 |            1.009 |           15.804 |          0.115 |        0.576
  1600 |            2.551 |           33.319 |          0.109 |        1.734
  3200 |            3.162 |           63.874 |          0.104 |        5.902
  6400 |            6.019 |          134.678 |          0.109 |       20.927
  200→400  append ×1.46 verify ×1.92 cumulative ×2.06
  400→800  append ×1.54 verify ×2.02 cumulative ×2.47
  800→1600 append ×2.53 verify ×2.11 cumulative ×3.01
 1600→3200 append ×1.24 verify ×1.92 cumulative ×3.40
 3200→6400 append ×1.90 verify ×2.11 cumulative ×3.55
# append_ms(N) ≈ 0.457 + 0.881·N/1000   (R² = 0.9747)
# ⇒ ≈ 0.9 µs/قيد · استقراء N=19119 ≈ 17.3 ms · N=50000 ≈ 44.5 ms
# سلامةُ السلسلةِ: سليمة
EXIT=0
--- measure_prefix_digest.py @ 311d9be ---
# commit: 311d9be905b6d1d8a61e1a1155bd8bfa86a031e5 · reps: 7
     N |      bytes | verify_full_ms | prefix_digest_ms | stat_tail_ms | full/digest
   200 |     210580 |          3.935 |            0.170 |       0.0278 |        23.2
   400 |     421380 |          8.036 |            0.379 |       0.0280 |        21.2
   800 |     842980 |         15.839 |            0.697 |       0.0434 |        22.7
  1600 |    1687380 |         32.925 |            1.501 |       0.0283 |        21.9
  3200 |    3376980 |         69.443 |            2.924 |       0.0278 |        23.8
  6400 |    6756180 |        139.037 |            5.877 |       0.0279 |        23.7
 12800 |   13520180 |        283.132 |           12.080 |       0.0278 |        23.4
EXIT=0
--- git worktree add before a2bbb186 ---
HEAD is now at a2bbb18 W-451: WI-095 RESERVED → IN_PROGRESS (H3)
WORKTREE_EXIT=0
--- measure_ledger_append.py @ a2bbb186 (قبلُ · نفسُ المفسّر · TMPDIR الخاص) ---
# commit: a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8
# sizes: [200, 400, 800, 1600, 3200]
     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
   200 |            4.166 |            4.056 |          0.111 |        0.445
   400 |            7.824 |            7.681 |          0.109 |        1.619
   800 |           15.357 |           15.031 |          0.109 |        6.376
  1600 |           30.623 |           29.942 |          0.151 |       25.170
  3200 |           67.349 |           67.413 |          0.141 |      104.971
  200→400  append ×1.88 verify ×1.89 cumulative ×3.64
  400→800  append ×1.96 verify ×1.96 cumulative ×3.94
  800→1600 append ×1.99 verify ×1.99 cumulative ×3.95
 1600→3200 append ×2.20 verify ×2.25 cumulative ×4.17
# append_ms(N) ≈ -1.054 + 21.063·N/1000   (R² = 0.9975)
# ⇒ ≈ 21.1 µs/قيد · استقراء N=19119 ≈ 401.7 ms · N=50000 ≈ 1052.1 ms
# سلامةُ السلسلةِ: سليمة
EXIT=0
--- measure_ledger_append.py --sizes …6400 @ a2bbb186 ---
# commit: a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8
     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
   200 |            4.227 |            4.057 |          0.114 |        0.430
   400 |            8.198 |            7.723 |          0.113 |        1.702
   800 |           16.513 |           15.936 |          0.122 |        6.861
  1600 |           35.153 |           35.393 |          0.132 |       28.157
  3200 |           63.084 |           61.628 |          0.117 |      105.768
  6400 |          130.367 |          132.202 |          0.121 |      428.234
  200→400  append ×1.94 verify ×1.90 cumulative ×3.95
  400→800  append ×2.01 verify ×2.06 cumulative ×4.03
  800→1600 append ×2.13 verify ×2.22 cumulative ×4.10
 1600→3200 append ×1.79 verify ×1.74 cumulative ×3.76
 3200→6400 append ×2.07 verify ×2.15 cumulative ×4.05
# append_ms(N) ≈ 0.464 + 20.219·N/1000   (R² = 0.9991)
# ⇒ ≈ 20.2 µs/قيد · استقراء N=19119 ≈ 387.0 ms · N=50000 ≈ 1011.4 ms
# سلامةُ السلسلةِ: سليمة
EXIT=0
--- git diff --stat a2bbb186..311d9be -- core/constitutional_engine/ledger.py ---
 core/constitutional_engine/ledger.py | 127 +++++++++++++++++++++++++++++++----
 1 file changed, 113 insertions(+), 14 deletions(-)
EXIT=0
--- ls docs/audit/evidence/W-452/ ---
README.md
measure_after_default.log
measure_after_extended.log
mutation_kills.log
mutation_kills.py
services_tests.log
tests_green.log
EXIT=0
--- rg headings DISC100_LEDGER_APPEND_DESIGN.md ---
17:## 0 · ما تُنفِّذُه هذه الوثيقةُ وما لا تُنفِّذُه
23:## 1 · المشكلةُ مقيسةً
25:### 1.1 الشِّفرةُ اليوم
37:### 1.2 المنحنى (مقيسٌ اليوم)
53:#### 1.2.1 إعادةُ القياسِ عندَ إعادةِ البناءِ (2026-10-18 · جهازُ التنفيذِ · `W-447`)
71:### 1.3 الأثرُ في CI
76:### 1.4 أنَّه عيبُ إنتاجٍ لا عيبُ اختبار
80:## 2 · ما يجبُ أن يبقى
92:## 3 · قيدٌ تصميميٌّ مقيس
104:## 4 · البدائل
115:### 4.1 البديلُ أ-1 — بصمةُ الملفِّ + الذيلُ + تحقّقٌ كاملٌ كلَّ K
133:### 4.2 البديلُ أ-2 — بصمةُ بايتاتِ البادئةِ في كلِّ إلحاق (بلا نافذة)
153:### 4.3 البديلُ أ-3 — أ-1 في كلِّ إلحاقٍ + بصمةُ البادئةِ كلَّ K (هجين)
160:### 4.4 ما رُفِضَ ولماذا
166:## 5 · المقارنة
177:## 6 · فحوصُ قتلِ التحويرات
196:## 7 · قياسُ القبولِ في بندِ C3
203:## 8 · أسئلةٌ مفتوحة
210:## 9 · ما لم أفعلْه (بصدق)
EXIT=0
--- cat MAPPING.md ---
جدولٌ يُحيلُ W-402…W-406 (قانونيٌّ على main · لا يُعاد) · W-407…W-412 (أُعيدَ → WI-094 / W-442…W-448) · W-413 (مؤكَّدٌ بـQ-56) · W-414 (نُقِلَ → W-458) · W-415 (نُقِلَ → W-459 · الكاشفُ لا يُنفَّذُ هنا) · W-416 (نُقِلَ → W-457) · W-417 (نُقِلَ → W-460) · W-418/W-419 (لا يُنقَل · تجديداتُ main حاكمة) · W-420 (نُقِلَ تاريخيًّا) · W-421 (تاريخيٌّ لا يُنقَل) · W-422…W-427 (أُعيدَ → WI-095 / W-449…W-453) · W-428 (تاريخيٌّ لا يُنقَل). وبنود: WI-082 لا بندَ جديد في هذه الدفعة · WI-085 → WI-094 · WI-086 → WI-095. وقسمُ «ما لم يُنقَل عمدًا» يعلنُ الشِّفرةَ وتجديداتِ الحجوزِ وأحكامَ CI وتقاريرَ الاستشارة.
EXIT=0
--- git show --stat ddcd21746e8f1c4726f7cb7052f45d95edf9631e ---
ddcd21746e8f1c4726f7cb7052f45d95edf9631e W-447: WI-094 — وثيقةُ تصميمِ المسارِ (أ) وقياسُ الجذرِ (نقلٌ من W-411 مع إعادةِ قياسٍ) + جدولُ مقابلةِ المكدَّس
 docs/audit/COMPLETION_LEDGER.md                    |   1 +
 docs/audit/DISC100_LEDGER_APPEND_DESIGN.md         | 215 +++++++++++++++++++++
 docs/audit/evidence/W-447/MAPPING.md               |  37 +++
 docs/audit/evidence/W-447/README.md                |  57 +++++
 docs/audit/evidence/W-447/measure_default.log      |  25 +++
 docs/audit/evidence/W-447/measure_extended.log     |  27 +++
 docs/audit/evidence/W-447/measure_ledger_append.py | 204 +++++++++++++++++++
 docs/audit/evidence/W-447/measure_prefix_digest.log|  14 ++
 docs/audit/evidence/W-447/measure_prefix_digest.py | 118 +++++++++++
 docs/governance/work/ACTIVE_WORK.md                |   2 +-
 10 files changed, 699 insertions(+), 1 deletion(-)
EXIT=0
--- find -maxdepth 1 ---
/home/user/workspace/council_w538/grok_4_7
/home/user/workspace/council_w538/grok_4_7/repo
/home/user/workspace/council_w538/grok_4_7/tmp
/home/user/workspace/council_w538/grok_4_7/before
EXIT=0
VERDICT_PER_CRITERION: (1) نعم — أُعيدَ تشغيلُ `.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py` بأمرٍ واحدٍ EXIT=0 على العقدةِ 311d9be، والممتدُّ EXIT=0، و`measure_prefix_digest.py` EXIT=0. السكربتُ (في الاستنساخ) يدرجُ جذرَ الشجرةِ في sys.path ويستوردُ `core.constitutional_engine.ledger.ConstitutionalLedger` ويكتبُ عبرَ `tempfile.TemporaryDirectory` (TMPDIR الخاصُّ بهذا المقعد)، وخرجُ التشغيلِ يعلنُ «سلامةُ السلسلةِ بعدَ القياس: سليمة» على العقدتين. (2) نعم — المنحنى من تشغيلي لا من ملفّاتِ المنفِّذ. قبلُ على a2bbb186 (الأبُ المباشرُ لتنفيذِ WI-095) بالأمرِ نفسِهِ: إلحاقٌ ≈21.1 µs/قيد (R²=0.9975) ونسبُ التراكميِّ ≈3.64–4.17؛ الممتدُّ ≈20.2 µs/قيد (R²=0.9991) وN=6400 إلحاقٌ 130.367 ms وتراكميٌّ 428.234 s. بعدُ على 311d9be بالأمرِ نفسِهِ والجهازِ نفسِهِ: ≈0.9 µs/قيد (R²=0.9944 افتراضيًّا و0.9747 ممتدًّا)؛ N=3200: 3.151 ms مقابلَ 67.349 ms قبلُ (≈21×) و3.162 مقابلَ 63.084 (≈20×)؛ N=6400: 6.019 ms مقابلَ 130.367 ms (≈22×). التحقّقُ الكاملُ يبقى ≈2× عندَ تضاعفِ N. الشطرُ «في أدلّةِ WI-095» تحقّقَ بـ`ls docs/audit/evidence/W-452/` EXIT=0 ووجودِ measure_after_default.log وmeasure_after_extended.log (لم تُقرأ محتوياتُها). `git diff --stat` يُظهرُ أنَّ فرقَ النواةِ بينَ العقدتين حقيقيٌّ: ledger.py ‏113 إدراجًا و14 حذفًا EXIT=0. (3) نعم — `docs/audit/DISC100_LEDGER_APPEND_DESIGN.md` ثلاثةُ بدائلَ بنقاطِ ضعفٍ مصرَّحٍ بها: أ-1 نافذةُ كشفٍ ≤K وإضعافُ P1 بقدرِ K ورفضُ الاعتمادِ على mtime؛ أ-2 يبقى O(N) ولا يزيلُ التربيعَ ويغيّرُ سلوكَ إعادةِ الكتابةِ المتّسقةِ ويثقُ بذاكرةِ العمليّة؛ أ-3 النافذةُ نفسُها مع إلحاقٍ حتى K فوقَ سلسلةٍ معطوبة. و§4.4 يرفضُ نقطةَ التحقّقِ على القرصِ وmtime وإسقاطَ التحقّقِ من الإلحاق. (4) نعم — `MAPPING.md` EXIT=0 يُحيلُ كلَّ قيدٍ من W-402 إلى W-428 إلى مصيرٍ مكتوبٍ (أُعيدَ / نُقِلَ / مؤكَّدٌ / لا يُنقَل / تاريخيٌّ) ويقابلُ WI-085→WI-094 وWI-086→WI-095. منعُ خارجِ النطاقِ في التزامِ البندِ: `git show --stat ddcd217` لا يمسُّ core/ ولا شِفرةً إنتاجيّةً ولا اختبارًا — وثائقُ وأدلّةُ قياسٍ في docs/audit/evidence/W-447/ وACTIVE_WORK فقط · EXIT=0.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — لم أقرأ شيئًا خارجَ استنساخي `/home/user/workspace/council_w538/grok_4_7/repo` وشجرةِ «قبلُ» `/home/user/workspace/council_w538/grok_4_7/before` وهذهِ الإحاطة. لم أقرأ `/home/user/workspace/amos` ولا `verdicts_w538` ولا أيَّ مقعدٍ آخرَ تحتَ `council_w538/` ولا ملفّاتِ `*.log`/`README.md` في W-447 أو W-452. لم أكتب تحتَ `/tmp`؛ TMPDIR كانَ `/home/user/workspace/council_w538/grok_4_7/tmp`. لا استثناء.
VERDICT: PASS لكلِّ المعاييرِ
