# حكمُ مقعدِ المجلسِ — grok_4_7 (عائلةُ xAI · Grok) · جولةُ WI-095

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-095 (بروتوكولُ Q-59 · بندُ WI-100) — لا تحريرَ ولا تلخيصَ.

## النطاق
حكمُ مقعدٍ واحدٍ على البندِ WI-095 بإحاطةِ W-514 (sha256 `37c65c3d2281d9c46974b6f32ee48fdda9883e1929cd182cd68d41a09a5850d1`) عندَ العقدةِ `b68d3b2b4f969b3e7eb57032afd7b24fae7bd8dc`.

## المالك
بندُ WI-100 (المنسِّقُ: Perplexity Computer · النموذجُ المنسِّقُ الحاضرُ GLM-5.3 كما أعلنتْهُ المنصةُ — منسِّقٌ لا مُصوِّتٌ).

## تاريخ الإنشاء
2026-10-19

## تاريخ آخر تعديل
2026-10-19 (W-515 — حُفظَ بعدَ اكتمالِ الأحكامِ الثلاثةِ كلِّها · § 2.3)

## المحتويات

- **النموذجُ كما أطلقتْهُ المنصةُ:** `grok_4_7` (عائلةُ xAI · Grok) · معرِّفُ الجلسةِ `wi_095_grok_mvf7cf5m`.
- **دليلُ الاستنساخِ:** `/home/user/workspace/council-wi095-grok` (يُزالُ بعدَ الحفظِ).

نصُّ الحكمِ كما وردَ (حرفيًّا):

````
MODEL: Grok 4.7
NODE: b68d3b2b4f969b3e7eb57032afd7b24fae7bd8dc

بيئة التشغيل (تجهيز، ليس معيارًا): `bash tools/dev/bootstrap.sh` في استنساخ العقدة أعلاه ⇒ EXIT:0. لم يُقرأ سجل قياس في evidence/W-447 ولا evidence/W-452. لم يُعدَّل المستودع (لا commit ولا push)؛ `git status --short` فارغ بعد الأوامر التي تكتب مؤقتًا.

## 1
VERDICT: PASS

السؤال: هل يقرأ المحرك التحقق الكامل مرة واحدة لكل مسار عند التمهيد لا في كل إلحاق؟ (معيار البند 1)

نص المعيار في البند: `append()` لا يقرأ ولا يحلّل السلسلة كاملة إلا أول مرة للمسار في العملية؛ وبعدها تطابق sha256 لبايتات [0, verified_size) في كل إلحاق + تحقق الذيل الجديد وحده + (dev, ino)، والحالة على مستوى الوحدة بمفتاح realpath.

لا أمر معيار لهذا البند في الإحاطة. أُعيد الإنتاج بمسبار خارج الشجرة (`council-wi095-grok/probe_criterion1.py`) يستورد `core.constitutional_engine.ledger` من عقدة المراجعة ويعدّ نداءات `_verify` الكاملة مقابل الذيل.

مخرجات خام (EXIT:0):

```
after ConstitutionalLedger.__init__: full_verify=0 tail_verify=0 parses=0 byte_reads=0 module_keys=0
after ConstitutionalEngine.__init__ (injected ledger): full_verify=0 tail_verify=0 parses=0 byte_reads=0 module_keys=0
after ConstitutionalEngine.__init__ (own path, no append): full_verify=0 tail_verify=0 parses=0 byte_reads=0 module_keys=0
after append #1 on object A: full_verify=1 tail_verify=0 parses=1 byte_reads=1 module_keys=1 last_full={'n': 0, 'start_index': 0, 'prev_is_genesis': True}
after append #2 on object A: full_verify=1 tail_verify=1 parses=2 byte_reads=2 module_keys=1 last_tail={'n': 0, 'start_index': 1, 'prev_is_genesis': False} last_parse_chars=0
after append #5 on object A: full_verify=1 tail_verify=4 parses=5 byte_reads=5 module_keys=1
after second object __init__ same path: full_verify=1 tail_verify=4
after append on object B (same path): full_verify=1 tail_verify=5 last_tail={'n': 0, 'start_index': 5, 'prev_is_genesis': False}
after append via symlink alias: full_verify=1 tail_verify=6
full_verifies_added_by_symlink_append=0
module_state_keys=['/tmp/wi095_c1_s3rbokb0/ledger.jsonl']
state dev=65024 ino=131123 size=2255 count=7 prefix_sha256_len=32
inode_replace_rejected=YES
prefix_tamper_rejected=YES
prime_full_verifies=1 full_added_when_tail_expected=0 tail_added=1 last_tail={'n': 1, 'start_index': 2, 'prev_is_genesis': False}
PROBE_DONE
PROBE_EXIT:0
```

سلسلة مسبقة من 30 قيدًا (عملية جديدة: `_VERIFIED` مفرغة)، EXIT:0:

```
seeded_entries 30 file_bytes 9180
init_of_preseeded full 0 parses 0
first_append_preseeded full [(30, 0, True)] tails [] parse_chars [9180]
second_append_preseeded full_count 1 tail_count 1 last_tail (0, 31, False) parse_chars [9180, 0]
third_object full_count 1 tail_count 2
SEEDED_PROBE_OK
```

القراءة: التحقق الهيكلي الكامل مرة واحدة لكل realpath عند أول `append` في العملية (هذا تمهيد الحالة، لا `__init__`)، لا في كل إلحاق. الإلحاق التالي يحلّل الذيل وحده (0 محرفًا إن لم يُضِف غيرنا) بعد مطابقة بصمة البادئة. كائن ثانٍ ورابط رمزي لا يعيدان التحقق الكامل. استبدال inode وعبث البادئة يُرفضان. ذيل خارجي سليم يُتحقَّق منه كذيل (start_index=2, n=1) بلا تحقق كامل ثانٍ.

BLOCKING_REMARKS: لا ملاحظات حاجبة. ملاحظة غير حاجبة: «عند التمهيد» في سؤال الإحاطة ليس `ConstitutionalLedger.__init__` ولا `ConstitutionalEngine.__init__` (كلاهما لا يتحقق؛ المسبار: full_verify=0). نص معيار البند 1 هو «أول مرة للمسار في العملية»، وهو ما أُعيد إنتاجه. قراءة بايتات الملف تتكرر في كل إلحاق لأن مطابقة sha256 للبادئة تشترطها؛ تحليل السلسلة والتحقق الهيكلي لا يتكرران.

## 2
VERDICT: PASS

الأمر (من جذر عقدة المراجعة):

```
.venv/bin/python docs/audit/evidence/W-452/mutation_kills.py
```

EXIT:0

مخرجات خام:

```
الهدف: core/constitutional_engine/ledger.py · sha256 4458577e96391f9a02db1ce33cf9f8238643e082e6b7786e54d854172dd04fd1

[K1] تعطيلُ مطابقةِ بصمةِ البادئة
  ⇒ قُتِل · 1 failed, 95 passed in 0.34s
    FAILED tests/constitutional/test_constitutional_engine.py::TestLedger::test_cannot_append_onto_broken_chain

[K2] تعطيلُ التحقّقِ من الذيل
  ⇒ قُتِل · 1 failed, 116 passed in 2.82s
    FAILED tests/constitutional/test_ledger_verified_state.py::TestTailWrittenByOthers::test_M8_legitimate_appends_by_another_process_are_accepted

[K3] تعطيلُ فحصِ (dev, ino)
  ⇒ قُتِل · 1 failed, 113 passed in 2.68s
    FAILED tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_M7_replacing_the_file_even_with_identical_bytes

[K4] تخطّي التحقّقِ الكاملِ الأوّلِ حينَ لا حالة
  ⇒ قُتِل · 1 failed, 105 passed in 2.37s
    FAILED tests/constitutional/test_ledger_verified_state.py::TestFullVerificationOncePerPath::test_first_append_in_a_fresh_process_verifies_the_whole_chain

[K5] مفتاحُ الحالةِ بالكائنِ لا بالمسارِ الحقيقيّ (في القراءةِ والكتابة)
  ⇒ قُتِل · 1 failed, 24 passed in 0.18s
    FAILED tests/constitutional/test_constitutional_engine.py::TestArticle001::test_system_cannot_amend_its_own_governance

[K6] تعطيلُ فحصِ اختفاءِ الملف
  ⇒ قُتِل · 1 failed, 114 passed in 2.56s
    FAILED tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_deleting_the_whole_ledger_after_verification

[K7] عدمُ تحديثِ الحالةِ بعدَ الإلحاق (كلُّ إلحاقٍ تحقّقٌ كامل — انحدارُ الأداء)
  ⇒ قُتِل · 1 failed, 99 passed in 1.47s
    FAILED tests/constitutional/test_ledger_append_performance.py::test_append_costs_a_small_fraction_of_a_full_chain_verification

[K8] بدءُ الذيلِ من موضعٍ خاطئ (index الذيلِ يبدأ بصفر)
  ⇒ قُتِل · 1 failed, 100 passed in 1.47s
    FAILED tests/constitutional/test_ledger_concurrency.py::Testالإلحاقالمتزامن::test_ستُّ_عمليّاتٍ_متزامنةٍ_تُنتِج_سلسلةً_سليمةً_كاملة

أُعيدَ الملفُّ بايتًا ببايت: نعم
الحصيلة: 8/8 قُتِلت · الناجية: لا شيء
EXIT:0
```

sha256 لـ `core/constitutional_engine/ledger.py` قبل الأمر وبعده: `4458577e96391f9a02db1ce33cf9f8238643e082e6b7786e54d854172dd04fd1` (متطابق). `git status --short` فارغ.

BLOCKING_REMARKS: لا ملاحظات حاجبة.

## 3
VERDICT: PASS

الأمر نفسه على الجانبين:

```
.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400
```

بصمة السكربت متطابقة على العقدتين: `sha256 9fc136c90b41b9f8f5fd26852eee847b05469dcf9bf24f116dafc37ff9c311ae`. الأب المباشر لعقدة التنفيذ `228d7a9` هو `a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8` (`git rev-parse 228d7a9^`). مفسّر القياس: Python 3.12.13 من `.venv` عقدة المراجعة (على جانب «قبل» وُصل `.venv` بالرابط الرمزي نفسه حتى يبقى الأمر حرفيًا؛ السكربت يدرج جذر نسخته في `sys.path` ويطبع `git HEAD`).

قبل — العقدة `a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8` — EXIT:0

`ledger.py` هناك بلا `_verified_snapshot` (sha256 `a049a82ad17b02dc710b990f5ca9a6c9da4a7da870be228c6326e624dc366981`).

```
# commit: a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200, 6400] · appends/N: 20 · verify reps: 5

     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
   200 |            4.439 |            4.116 |          0.109 |        0.481
   400 |            7.921 |            7.841 |          0.113 |        1.694
   800 |           16.568 |           16.115 |          0.123 |        6.563
  1600 |           32.541 |           31.764 |          0.101 |       26.841
  3200 |           68.429 |           70.050 |          0.122 |      110.026
  6400 |          136.807 |          134.231 |          0.109 |      478.776

  200→400    |      1.78 |      1.90 |         3.52
  400→800    |      2.09 |      2.06 |         3.88
  800→1600   |      1.96 |      1.97 |         4.09
 1600→3200   |      2.10 |      2.21 |         4.10
 3200→6400   |      2.00 |      1.92 |         4.35

# ملاءمةٌ خطّيّة: append_ms(N) ≈ -0.612 + 21.458·N/1000   (R² = 0.9998)
# سلامةُ السلسلةِ بعدَ القياس: سليمة
EXIT:0
```

بعد — العقدة `b68d3b2b4f969b3e7eb57032afd7b24fae7bd8dc` — EXIT:0

```
# commit: b68d3b2b4f969b3e7eb57032afd7b24fae7bd8dc
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200, 6400] · appends/N: 20 · verify reps: 5

     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
   200 |            0.432 |            4.205 |          0.114 |        0.110
   400 |            0.668 |            8.196 |          0.127 |        0.217
   800 |            1.025 |           15.624 |          0.119 |        0.572
  1600 |            1.824 |           34.429 |          0.115 |        1.713
  3200 |            3.206 |           68.121 |          0.117 |        5.798
  6400 |            6.667 |          138.959 |          0.110 |       21.967

  200→400    |      1.55 |      1.95 |         1.98
  400→800    |      1.53 |      1.91 |         2.63
  800→1600   |      1.78 |      2.20 |         3.00
 1600→3200   |      1.76 |      1.98 |         3.38
 3200→6400   |      2.08 |      2.04 |         3.79

# ملاءمةٌ خطّيّة: append_ms(N) ≈ 0.215 + 0.995·N/1000   (R² = 0.9983)
#   ⇒ كلفةُ القيدِ الواحدِ في كلِّ إلحاقٍ ≈ 1.0 µs
# سلامةُ السلسلةِ بعدَ القياس: سليمة
EXIT:0
```

تسريع append_median عند N=3200: 68.429 / 3.206 = 21.344× (≥ 10). عند N=6400: 20.520×. جانب «بعد»: زمن الإلحاق خطّي في N (تعريف السكربت: تضاعف N ⇒ ~2 لا ~4؛ 3200→6400 = 2.08؛ R²=0.9983). النسب تحت 2 عند N الصغير ثابت الكلفة (0.215 ms + fsync ≈ 0.11 ms) لا انحناء تربيعي. `verify_median_ms` يبقى O(N) كاملًا لأن السكربت يقيس `_verify(entries())` منفصلًا عن مسار الإلحاق؛ معيار التسريع على عمود append.

BLOCKING_REMARKS: لا ملاحظات حاجبة.

## 4
VERDICT: PASS

الأمر:

```
.venv/bin/python -m pytest tests/constitutional/ tests/sovereignty/ tests/crown/ -q
```

EXIT:0

```
1349 passed, 1 skipped in 17.36s
EXIT:0
```

الفحصان الجديدان داخل الأمر (جُمعا مع الحزمة، ولا علامة skip في ملفيهما): 18 اختبارًا، منها `test_first_append_in_a_fresh_process_verifies_the_whole_chain` و`test_append_costs_a_small_fraction_of_a_full_chain_verification`. التخطي الوحيد ليس فيهما. فشل أي منهما كان يسقط رمز الخروج. الحزمة القائمة خضراء وهما معها.

BLOCKING_REMARKS: لا ملاحظات حاجبة.

## 5
VERDICT: PASS

الأمر كما في الإحاطة (مفسّر النظام، لا `.venv`):

```
python tools/governance/truth_audit.py --ratchet
```

`which python` ⇒ `/usr/local/bin/python` · 3.14.3

EXIT:0

```
[TRUTH AUDIT] أقاليم: 12 | مُثبَتة: 0 | مخالفات: 61
  - IN_MEMORY_STORE: 59
  - HARDCODED_TRUTH: 2
[TRUTH AUDIT] كُتبت: /home/user/workspace/council-wi095-grok/repo/docs/audit/TRUTH_MATRIX.md
[RATCHET] ثابت عند 61 مخالفة.
TRUTH_EXIT:0
```

خط الأساس المقروء قبل التشغيل من `docs/audit/truth_baseline.json`: `findings_total 61` · `by_kind {'HARDCODED_TRUTH': 2, 'IN_MEMORY_STORE': 59}`. لم يرتفع. بعد الكتابة: `git status --short` فارغ و`git diff --stat` فارغ — المصفوفة المكتوبة يولّدها الوسيط وتطابق الشجرة.

`find . -name '*suite_4000*' -o -name '*tool_environment_preview*' -o -name '*suite_4000_lockdown*'` ⇒ FIND_EXIT:0 ولا ملف. الشرط «إن وُجدت» لا يضيف أثرًا.

BLOCKING_REMARKS: لا ملاحظات حاجبة.

## 6
VERDICT: PASS

الأمر:

```
git log --oneline --grep="W-45[12]" -- docs/audit/COMPLETION_LEDGER.md core/constitutional_engine/ledger.py
```

EXIT:0

```
228d7a9 W-452: WI-095 — تنفيذُ البديلِ أ-2 في ConstitutionalLedger.append() (نقلٌ من W-426 · قياساتٌ معادَةٌ: ×20.8 · 8/8 تحويراتٍ)
a2bbb18 W-451: WI-095 RESERVED → IN_PROGRESS (H3)
EXIT:0
```

قيدان مستقلان:

- `a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8` أبوه `b729272dd719d3373ec98cd6110080d8e2e99604` · `W-451: WI-095 RESERVED → IN_PROGRESS (H3)` · الملفات: `docs/audit/COMPLETION_LEDGER.md` و`docs/governance/work/ACTIVE_WORK.md` فقط.
- `228d7a9d010fc86b364d69dbc1428687b523a322` أبوه `a2bbb186…` · دفعة الشِّفرة · تشمل `core/constitutional_engine/ledger.py` و`docs/audit/COMPLETION_LEDGER.md`.

وصف أثر الحفظ في قيد الدفعة المستقل W-452، لا في قيد الانتقال W-451. من `git show 228d7a9:core/constitutional_engine/ledger.py`:

```
33:والآن: تحقّقٌ كاملٌ **أوّلَ مرّةٍ** يُلحَقُ فيها بالمسارِ في العمليّة، ثمَّ حالةٌ مُتحقَّقٌ منها
35:`(st_dev, st_ino)` + طولُ الجزءِ المُتحقَّقِ منه + عددُ قيودِه + آخرُ بصمة + sha256 لبايتاتِه.
41:تغييرُ سلوكٍ مُعلَنٌ (أشدّ): إعادةُ كتابةٍ **متّسقةٍ** للسلسلةِ (بصماتٌ مُعادٌ حسابُها) بعدَ أن
```

BLOCKING_REMARKS: لا ملاحظات حاجبة. ملاحظة غير حاجبة: `02ddf15 W-453: WI-095 IN_PROGRESS → IN_REVIEW (H3)` قيد انتقال مستقل ثالث، خارج نمط الأمر `W-45[12]`، ولا ينقض استقلال W-451 عن W-452.

الحكم الكامل محفوظ في `council-wi095-grok/VERDICT.md`.
````
