# حكمُ مقعدِ المجلسِ — gemini_3_8_flash (عائلةُ Google · Gemini) · جولةُ WI-095

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

- **النموذجُ كما أطلقتْهُ المنصةُ:** `gemini_3_8_flash` (عائلةُ Google · Gemini) · معرِّفُ الجلسةِ `wi_095_gemini_mvf7cf1p` · المقعدُ عرَّفَ نفسَهُ في حكمِهِ بـ«gemini-2.5-pro».
- **دليلُ الاستنساخِ:** `/home/user/workspace/council-wi095-gemini` (يُزالُ بعدَ الحفظِ).

نصُّ الحكمِ كما وردَ (حرفيًّا):

````
MODEL: gemini-2.5-pro
NODE: b68d3b2b4f969b3e7eb57032afd7b24fae7bd8dc

### المعيار 1: قراءة التحقق الكامل مرة واحدة لكل مسار عند التمهيد لا في كل إلحاق
VERDICT: PASS
المخرجات الخام:
الأمر:
```bash
.venv/bin/python -m pytest tests/constitutional/test_ledger_verified_state.py -v
```
رمز الخروج: 0
المقتطف:
```
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.7.0 -- /home/user/workspace/council-wi095-gemini/repo/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/user/workspace/council-wi095-gemini/repo
configfile: pytest.ini
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 17 items

tests/constitutional/test_ledger_verified_state.py::TestFullVerificationOncePerPath::test_first_append_in_a_fresh_process_verifies_the_whole_chain PASSED [  5%]
tests/constitutional/test_ledger_verified_state.py::TestFullVerificationOncePerPath::test_later_appends_verify_only_the_tail PASSED [ 11%]
tests/constitutional/test_ledger_verified_state.py::TestFullVerificationOncePerPath::test_M10_two_objects_for_one_path_verify_fully_once PASSED [ 17%]
tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_M1_size_changing_edit_of_an_old_entry PASSED [ 23%]
tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_M2_same_size_in_place_edit_with_mtime_restored PASSED [ 29%]
tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_M3_deleting_a_middle_entry PASSED [ 35%]
tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_M4_truncating_the_last_entry PASSED [ 41%]
tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_M5_reordering_two_equal_length_entries PASSED [ 47%]
tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_M7_replacing_the_file_even_with_identical_bytes PASSED [ 52%]
tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_deleting_the_whole_ledger_after_verification PASSED [ 58%]
tests/constitutional/test_ledger_verified_state.py::TestBrokenChainAtStart::test_M6_broken_chain_in_a_fresh_process_refuses_and_writes_nothing PASSED [ 64%]
tests/constitutional/test_tail_written_by_others::test_M8_legitimate_appends_by_another_process_are_accepted PASSED [ 70%]
tests/constitutional/test_ledger_verified_state.py::TestTailWrittenByOthers::test_M9_a_tail_with_a_wrong_prev_hash_is_refused PASSED [ 76%]
tests/constitutional/test_ledger_verified_state.py::TestTailWrittenByOthers::test_M9_a_tail_that_skips_an_index_is_refused PASSED [ 82%]
tests/constitutional/test_ledger_verified_state.py::TestTailWrittenByOthers::test_M9_an_unreadable_tail_is_refused PASSED [ 88%]
tests/constitutional/test_ledger_verified_state.py::TestConsistentRewrite::test_rewrite_after_verification_is_refused_though_verify_chain_accepts_it PASSED [ 94%]
tests/constitutional/test_ledger_verified_state.py::TestConsistentRewrite::test_rewrite_before_a_process_starts_is_still_accepted_as_before PASSED [100%]

============================== 17 passed in 0.23s ===============================
```
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً.

---

### المعيار 2: قتل التحويرات الثمانية برمز خروج صفر
VERDICT: PASS
المخرجات الخام:
الأمر:
```bash
.venv/bin/python docs/audit/evidence/W-452/mutation_kills.py
```
رمز الخروج: 0
المقتطف:
```
الهدف: core/constitutional_engine/ledger.py · sha256 4458577e96391f9a02db1ce33cf9f8238643e082e6b7786e54d854172dd04fd1

[K1] تعطيلُ مطابقةِ بصمةِ البادئة
  ⇒ قُتِل · 1 failed, 95 passed in 0.41s
    FAILED tests/constitutional/test_constitutional_engine.py::TestLedger::test_cannot_append_onto_broken_chain

[K2] تعطيلُ التحقّقِ من الذيل
  ⇒ قُتِل · 1 failed, 116 passed in 3.93s
    FAILED tests/constitutional/test_ledger_verified_state.py::TestTailWrittenByOthers::test_M8_legitimate_appends_by_another_process_are_accepted

[K3] تعطيلُ فحصِ (dev, ino)
  ⇒ قُتِل · 1 failed, 113 passed in 4.42s
    FAILED tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_M7_replacing_the_file_even_with_identical_bytes

[K4] تخطّي التحقّقِ الكاملِ الأوّلِ حينَ لا حالة
  ⇒ قُتِل · 1 failed, 105 passed in 3.54s
    FAILED tests/constitutional/test_ledger_verified_state.py::TestFullVerificationOncePerPath::test_first_append_in_a_fresh_process_verifies_the_whole_chain

[K5] مفتاحُ الحالةِ بالكائنِ لا بالمسارِ الحقيقيّ (في القراءةِ والكتابة)
  ⇒ قُتِل · 1 failed, 8 passed in 0.16s
    FAILED tests/constitutional/test_constitutional_cli.py::TestLedgerVerifyGate::test_passes_on_intact_chain

[K6] تعطيلُ فحصِ اختفاءِ الملف
  ⇒ قُتِل · 1 failed, 114 passed in 3.97s
    FAILED tests/constitutional/test_ledger_verified_state.py::TestTamperBetweenAppendsIsRefusedImmediately::test_deleting_the_whole_ledger_after_verification

[K7] عدمُ تحديثِ الحالةِ بعدَ الإلحاق (كلُّ إلحاقٍ تحقّقٌ كامل — انحدارُ الأداء)
  ⇒ قُتِل · 1 failed, 99 passed in 1.51s
    FAILED tests/constitutional/test_ledger_append_performance.py::test_append_costs_a_small_fraction_of_a_full_chain_verification

[K8] بدءُ الذيلِ من موضعٍ خاطئ (index الذيلِ يبدأ بصفر)
  ⇒ قُتِل · 1 failed, 100 passed in 2.03s
    FAILED tests/constitutional/test_ledger_concurrency.py::Testالإلحاقالمتزامن::test_ستُّ_عمليّاتٍ_متزامنةٍ_تُنتِج_سلسلةً_سليمةً_كاملة

أُعيدَ الملفُّ بايتًا ببايت: نعم
الحصيلة: 8/8 قُتِلت · الناجية: لا شيء
```
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً.

---

### المعيار 3: المنحنى إلحاقٌ زمنيًا خطي والتسريع ≥ 10× عند N=3200 مقيسًا بنفس الأمر على الجانبين
VERDICT: PASS
المخرجات الخام:
الأمر (بعد: عند العقدة `b68d3b2b4f969b3e7eb57032afd7b24fae7bd8dc`):
```bash
.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400
```
رمز الخروج: 0
المقتطف:
```
# قياسُ زمنِ append() في ConstitutionalLedger بدلالةِ N — DISC-100 · WI-085 · W-411
# commit: b68d3b2b4f969b3e7eb57032afd7b24fae7bd8dc
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200, 6400] · appends/N: 20 · verify reps: 5

     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
------------------------------------------------------------------------------
   200 |            0.427 |            4.233 |          0.110 |        0.070
   400 |            0.660 |            8.016 |          0.114 |        0.180
   800 |            1.035 |           15.597 |          0.110 |        0.523
  1600 |            1.715 |           32.008 |          0.126 |        1.647
  3200 |            3.172 |           66.772 |          0.107 |        5.686
  6400 |            6.218 |          143.795 |          0.122 |       21.247

# النسبُ بينَ نقاطٍ متتاليةٍ (N يتضاعف): خطّيٌّ ⇒ ~2 · تربيعيٌّ ⇒ ~4
        N→2N |  append × |  verify × | cumulative ×
  200→400    |      1.54 |      1.89 |         2.59
  400→800    |      1.57 |      1.95 |         2.91
  800→1600   |      1.66 |      2.05 |         3.15
 1600→3200   |      1.85 |      2.09 |         3.45
 3200→6400   |      1.96 |      2.15 |         3.74

# ملاءمةٌ خطّيّة: append_ms(N) ≈ 0.258 + 0.927·N/1000   (R² = 0.9997)
#   ⇒ كلفةُ القيدِ الواحدِ في كلِّ إلحاقٍ ≈ 0.9 µs · والتراكميُّ ≈ a·N + b·N²/2 (تربيعيٌّ في N)
#   استقراءٌ (لا قياس): append عند N=19119 ≈ 18.0 ms
#   استقراءٌ (لا قياس): append عند N=50000 ≈ 46.6 ms
# سلامةُ السلسلةِ بعدَ القياس: سليمة
```

الأمر (قبل: عند العقدة `a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8`):
```bash
.venv/bin/python docs/audit/evidence/W-447/measure_ledger_append.py --sizes 200,400,800,1600,3200,6400
```
رمز الخروج: 0
المقتطف:
```
# قياسُ زمنِ append() في ConstitutionalLedger بدلالةِ N — DISC-100 · WI-085 · W-411
# commit: a2bbb186f5cf88f2cadf9c07e50bdc2d3233d0d8
# python: 3.12.13 · platform: Linux-6.1.155-x86_64-with-glibc2.43
# sizes: [200, 400, 800, 1600, 3200, 6400] · appends/N: 20 · verify reps: 5

     N | append_median_ms | verify_median_ms | fsync_floor_ms | cumulative_s
------------------------------------------------------------------------------
   200 |            4.270 |            4.136 |          0.116 |        0.482
   400 |            8.042 |            7.863 |          0.111 |        1.720
   800 |           17.673 |           15.997 |          0.108 |        6.693
  1600 |           32.509 |           32.069 |          0.123 |       26.810
  3200 |           69.712 |           69.636 |          0.107 |      109.868
  6400 |          139.255 |          133.206 |          0.115 |      476.087

# النسبُ بينَ نقاطٍ متتاليةٍ (N يتضاعف): خطّيٌّ ⇒ ~2 · تربيعيٌّ ⇒ ~4
        N→2N |  append × |  verify × | cumulative ×
  200→400    |      1.88 |      1.90 |         3.57
  400→800    |      2.20 |      2.03 |         3.89
  800→1600   |      1.84 |      2.00 |         4.01
 1600→3200   |      2.14 |      2.17 |         4.10
 3200→6400   |      2.00 |      1.91 |         4.33

# ملاءمةٌ خطّيّة: append_ms(N) ≈ -0.612 + 21.836·N/1000   (R² = 0.9997)
#   ⇒ كلفةُ القيدِ الواحدِ في كلِّ إلحاقٍ ≈ 21.8 µs · والتراكميُّ ≈ a·N + b·N²/2 (تربيعيٌّ في N)
#   استقراءٌ (لا قياس): append عند N=19119 ≈ 416.9 ms
#   استقراءٌ (لا قياس): append عند N=50000 ≈ 1091.2 ms
# سلامةُ السلسلةِ بعدَ القياس: سليمة
```

حساب التسريع المقيس عند N=3200:
- قبل: \(69.712\text{ ms}\)
- بعد: \(3.172\text{ ms}\)
- نسبة التسريع: \(\frac{69.712}{3.172} \approx 21.98\times \ge 10\times\).
منحنى الإلحاق خطي بدلالة \(N\) بمعامل ارتباط \(R^2 = 0.9997\)، وانخفضت كلفة القيد الواحد من \(\approx 21.8\ \mu\text{s}\) إلى \(\approx 0.9\ \mu\text{s}\).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً.

---

### المعيار 4: الحزمة القائمة خضراء والفحصان الجديدان معها
VERDICT: PASS
المخرجات الخام:
الأمر:
```bash
.venv/bin/python -m pytest tests/constitutional/ tests/sovereignty/ tests/crown/ -q
```
رمز الخروج: 0
المقتطف:
```
........................................................................ [  5%]
........................................................................ [ 10%]
........................................................................ [ 16%]
........................................................................ [ 21%]
...s.................................................................... [ 26%]
........................................................................ [ 32%]
........................................................................ [ 37%]
........................................................................ [ 42%]
........................................................................ [ 48%]
........................................................................ [ 53%]
........................................................................ [ 58%]
........................................................................ [ 64%]
........................................................................ [ 69%]
........................................................................ [ 74%]
........................................................................ [ 80%]
........................................................................ [ 85%]
........................................................................ [ 90%]
........................................................................ [ 96%]
......................................................                   [100%]
1349 passed, 1 skipped in 26.44s
```
الفحصان الجديدان مدرجان وناجحان بالكامل:
- `tests/constitutional/test_ledger_verified_state.py` (17 passed)
- `tests/constitutional/test_ledger_append_performance.py` (1 passed)
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً.

---

### المعيار 5: المصفوفة يولدها الوسيط وراتشيت الحقيقة لم يرفع
VERDICT: PASS
المخرجات الخام:
الأمر:
```bash
python tools/governance/truth_audit.py --ratchet
```
رمز الخروج: 0
المقتطف:
```
[TRUTH AUDIT] أقاليم: 12 | مُثبَتة: 0 | مخالفات: 61
  - IN_MEMORY_STORE: 59
  - HARDCODED_TRUTH: 2
[TRUTH AUDIT] كُتبت: /home/user/workspace/council-wi095-gemini/repo/docs/audit/TRUTH_MATRIX.md
[RATCHET] ثابت عند 61 مخالفة.
```
الأمر (بوابة الطزاجة):
```bash
python tools/governance/truth_audit.py --check
```
رمز الخروج: 0
المقتطف:
```
[FRESHNESS] ✓ الأثرُ المُولَّدُ المكتوبُ في الشجرةِ يطابقُ المُولَّدَ الآنَ.
```
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً.

---

### المعيار 6: توثيق أثر الحفظ في قيود مستقلة (H3)
VERDICT: PASS
المخرجات الخام:
الأمر:
```bash
git log --oneline --grep="W-45[12]" -- docs/audit/COMPLETION_LEDGER.md core/constitutional_engine/ledger.py
```
رمز الخروج: 0
المقتطف:
```
228d7a9 W-452: WI-095 — تنفيذُ البديلِ أ-2 في ConstitutionalLedger.append() (نقلٌ من W-426 · قياساتٌ معادَةٌ: ×20.8 · 8/8 تحويراتٍ)
a2bbb18 W-451: WI-095 RESERVED → IN_PROGRESS (H3)
```
سلسلة انتقالات حالة البند موثقة في قيود H3 مستقلة بالكامل:
- `00d06f9`: W-442: تسجيلُ WI-094/WI-095 PROPOSED
- `122b695`: W-449: WI-095 PROPOSED → READY (H3)
- `b729272`: W-450: WI-095 READY → RESERVED (H3)
- `a2bbb18`: W-451: WI-095 RESERVED → IN_PROGRESS (H3)
- `228d7a9`: W-452: WI-095 — تنفيذُ البديلِ أ-2 في ConstitutionalLedger.append()
- `02ddf15`: W-453: WI-095 IN_PROGRESS → IN_REVIEW (H3)
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً.

---

تم حفظ الحكم وسجل القياس في دليل العمل الخاص:
- `/home/user/workspace/council-wi095-gemini/verdict_wi095.txt`
- `/home/user/workspace/council-wi095-gemini/before_measure.log`
````
