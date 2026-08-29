# سجلُّ العملِ المفتوح — ACTIVE WORK

## الهدف: إعلانُ ما يُعملُ عليه **الآن**، ومَن يعملُ عليه، وفي أيِّ مساراتٍ بالضبط، وإلى متى — حتى لا يبدأَ أحدٌ عملًا بدأَه غيرُه، ولا ينتظرَ نطاقًا لا يعملُ فيه أحد
## النطاق: البنودُ المفتوحةُ وحدَها (`PROPOSED` → `VERIFIED`) والمُغلَقةُ حديثًا. **لا يُسجَّلُ هنا تاريخُ ما أُنجِز** — ذاك في [`COMPLETION_LEDGER.md`](../../audit/COMPLETION_LEDGER.md)، ولا حالةُ القدرةِ — تلك في [`TRUTH_MATRIX.md`](../../audit/TRUTH_MATRIX.md)
## المالك: قائدُ التنفيذِ، بتفويضٍ من المجلس التأسيسي
## تاريخ الإنشاء: 2026-08-25
## تاريخ آخر تعديل: 2026-08-29 (`WI-019` — الحكمُ الأحمرُ صارَ مقروءًا ثمَّ صارَ أخضرَ: سببُه سطرُ اختبارٍ لا حرسٌ ضعيفٌ، فأُصلِحَ الفتيلُ ولم يُخفَّفِ الماسحُ)

> يحكمُ هذا السجلَّ [`THE_ROADMAP.md`](THE_ROADMAP.md): الحقولُ في § 4.2، والحالاتُ
> والانتقالاتُ في § 4.3، وقفلُ النطاقِ في § 6، وواجبُ ما بعدَ الدمجِ في § 7.
> وتحرسُه البوّابةُ `tools/governance/check_work_governance.py`.
>
> **قاعدةُ الكتابة:** صفٌّ في الجدولِ **ومعَه** كتلةُ تفاصيلَ في § 3 لكلِّ بندٍ نشِط.
> صفٌّ بلا كتلةٍ = `MALFORMED_ITEM`.

---

## 1 · البنودُ النشِطة

| المعرِّف | النطاق | المسار | المالك | المراجع | الحالة | المسارات | بدأ | ينتهي الحجز | العائق | الخطوةُ التالية | قيدُ السجلّ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WI-001 | governance-docs | T2 | Driving H | المجلس التأسيسي | CLOSED | docs/governance/work · tools/governance/check_work_governance.py · tests/governance/test_work_governance_gate.py · .github/workflows/ci.yml · docs/governance/README.md · docs/index.md · README.md · docs/PROJECT_HANDBOOK.md · docs/audit/COMPLETION_LEDGER.md | 2026-08-25 | 2026-09-01 | — | — (مُغلَق) | W-043 · W-044 · W-045 · W-046 · دمجُ #14 (`2b355ca3`) · #15 (`b4d957fa`) |
| WI-003 | tooling-gates | T0 / T2 | Driving H | المجلس التأسيسي | CLOSED | tools/governance/measurement_provenance.py · tools/governance/restart_survival_probe.py · .github/workflows/measure.yml · tests/governance/test_w048_bound_provenance.py · tests/governance/test_w037_measurement_provenance.py · tests/governance/test_w038_probe_measure_mode.py · docs/audit/measurements/README.md · docs/PROJECT_HANDBOOK.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَقٌ بقيدِ W-048 · وحكمُ CI على دفعتِه يُقيِّدُه أوّلُ عملٍ تالٍ كما فَعلَ W-044 بما قبلَه) | W-048 |
| WI-005 | audit-truth | T0 | Driving H | المجلس التأسيسي | CLOSED | docs/governance/work/ACTIVE_WORK.md · docs/governance/work/DISCOVERIES.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَقٌ بقيدِ W-050 · وDISC-006 ما زالَ مفتوحًا بيدِ المالكِ) | W-050 |
| WI-004 | audit-truth | T0 | Driving H | المجلس التأسيسي | CLOSED | docs/governance/work/DISCOVERIES.md · docs/governance/work/RISK_REGISTER.md · docs/governance/work/ACTIVE_WORK.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَقٌ بقيدِ W-049 · وإصلاحُ حسابِ Actions بيدِ المالكِ — DISC-006 مفتوحٌ عليه) | W-049 |
| WI-002 | audit-truth | T0 / T2 | Driving H | المجلس التأسيسي | CLOSED | docs/audit/COMPLETION_LEDGER.md · EXECUTION_PLAN.md · docs/governance/work/DISCOVERIES.md · docs/governance/work/THE_ROADMAP.md · PROJECT_STATE.md · docs/audit/ACTIVE_EXECUTION_STATE.md · docs/governance/work/ACTIVE_WORK.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَق) | W-047 |
| WI-006 | tooling-gates | T0 / T2 | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/ci_verdict_readability.py · tests/governance/test_w051_ci_verdict_readability.py · tools/governance/measurement_provenance.py · tests/governance/test_w038_probe_measure_mode.py · tests/governance/test_w048_bound_provenance.py · docs/audit/measurements/ci_verdict_readability.json · docs/audit/measurements/README.md · docs/governance/work/ACTIVE_WORK.md · docs/governance/work/DISCOVERIES.md · docs/governance/work/RISK_REGISTER.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-27 | 2026-09-03 | — (لا عائقَ على البندِ نفسِه؛ والعطبُ المقيسُ عائقٌ على `T0.4ب` لا عليه) | **دُمِجَ ولم يُغلَقْ**: قيدُ `W-051` صارَ حالةَ الدولةِ (‏دمجٌ واقعٌ)، والإغلاقُ موقوفٌ على قرارِ `A-2` لأنَّ § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` — `DISC-012` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-007 | tooling-gates | T0 | Driving H | المجلس التأسيسي | IN_REVIEW | tools/audit/final_audit.py · tests/governance/test_w052_history_hash_probe.py · docs/governance/work/OWNERSHIP.md | 2026-08-27 | 2026-09-03 | — (لا عائقَ على البندِ نفسِه) | **دُمِجَ ولم يُغلَقْ**: قيدُ `W-052` صارَ حالةَ الدولةِ (‏دمجٌ واقعٌ)، والإغلاقُ موقوفٌ على قرارِ `A-2` لأنَّ § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` — `DISC-012` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-008 | tooling-gates | T0 | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/gate_dependency_closure.py · tests/governance/test_w053_gate_dependency_closure.py | 2026-08-27 | 2026-09-03 | — (لا عائقَ على البندِ نفسِه؛ والعطبُ المقيسُ عائقٌ على `sovereignty-kernel` لا عليه) | **دُمِجَ ولم يُغلَقْ**: قيدُ `W-053` صارَ حالةَ الدولةِ (‏دمجٌ واقعٌ)، والإغلاقُ موقوفٌ على قرارِ `A-2` لأنَّ § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` — `DISC-012` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-010 | audit-truth | T0 | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/schema_inventory_drift.py · tests/governance/test_w055_schema_inventory_drift.py · ARCHITECTURE.md | 2026-08-27 | 2026-09-03 | — (لا عائقَ على البندِ نفسِه؛ ونشرُ الحِملِ محجوبٌ بحجزِ `WI-006` — `DISC-014`) | يُنقَلُ إلى `CLOSED` بقيدِ `W-055` ورقمِ الدمجِ بعدَ أن يدمجَ المالكُ — § 7، إن فُتِحَ الطريقُ (`DISC-012`) | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-011 | audit-truth | T0 (قابليّةُ القياسِ · شرطُ خروجٍ) | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/sovereign_decision_status.py · tests/governance/test_w056_sovereign_decision_status.py | 2026-08-27 | 2026-09-03 | — | بعدَ دمجِ المالكِ يُنقَلُ إلى `CLOSED` بقيدِ `W-056` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-012 | audit-truth | T0 (قابليّةُ القياسِ · شرطُ خروجٍ) | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/state_document_drift.py · tests/governance/test_w057_state_document_drift.py · PROJECT_STATE.md · docs/PROJECT_HANDBOOK.md | 2026-08-27 | 2026-09-03 | — | بعدَ دمجِ المالكِ يُنقَلُ إلى `CLOSED` بقيدِ `W-057` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-009 | tooling-gates | T0 / T2 | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/check_work_governance.py · tests/governance/test_w054_post_merge_reverse_link.py · docs/governance/work/THE_ROADMAP.md | 2026-08-27 | 2026-09-03 | — (لا عائقَ على البندِ نفسِه؛ والتعارُضُ المقيسُ `DISC-012` عائقٌ على إغلاقِ `WI-006`…`WI-008` لا عليه) | يُنقَلُ إلى `CLOSED` بقيدِ `W-054` ورقمِ الدمجِ بعدَ أن يدمجَ المالكُ — § 7، إن أمكنَ الطريقُ (`DISC-012`) | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-013 | tests-root | T0 (صدقُ الحرسِ · منعُ كذبٍ مُوثَّقٍ معكوسٍ) | Driving H | المجلس التأسيسي | IN_REVIEW | tests/governance/test_step18_restart_survival.py · tests/governance/test_w058_live_stack_precondition.py | 2026-08-27 | 2026-09-03 | — | بعدَ دمجِ المالكِ يُنقَلُ إلى `CLOSED` بقيدِ `W-058` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-015 | governance-docs | T0 (قابليّةُ القياسِ · دعوى الحرسِ تُثبَتُ بطفرةٍ لا تُكتَبُ) | Driving H | المجلس التأسيسي | IN_REVIEW | — (لا مسارَ يُحجَزُ: كلُّ ما يُمَسُّ **مُعفًى من الحجزِ** بنصِّ § 6 — `DISCOVERIES.md` · `RISK_REGISTER.md` · `ACTIVE_WORK.md` · `COMPLETION_LEDGER.md` وسطرُ آخرِ قيدٍ في وثيقتَي الحالةِ؛ ولذلك لا يُزاحَمُ حجزُ `WI-006`) | 2026-08-28 | 2026-09-04 | — | بعدَ دمجِ المالكِ يُنقَلُ إلى `CLOSED` بقيدِ `W-060` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-014 | tooling-gates | T0 (قابليّةُ القياسِ · قاعدةٌ مكتوبةٌ تصيرُ عدَّادًا) | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/open_record_accountability.py · tests/governance/test_w059_open_record_accountability.py | 2026-08-28 | 2026-09-04 | — | بعدَ دمجِ المالكِ يُنقَلُ إلى `CLOSED` بقيدِ `W-059` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-019 | tooling-gates | T0 (قابليّةُ القياسِ · حكمُ CI يُقرأُ ثمَّ يُخضَّرُ من سببِه) | Driving H | المجلس التأسيسي | IN_REVIEW | tools/crown/secret_scan_exceptions.py · tests/crown/test_w064_secret_scan_exceptions.py · tools/crown/verify_secret_boundaries.py · tests/sovereignty/test_outbox.py · docs/security/SECRET_BOUNDARIES.md · conftest.py · tests/governance/test_w064_services_src_fallback.py | 2026-08-29 | 2026-09-06 | — | بعدَ الدمجِ يُنقَلُ إلى `CLOSED` بقيدِ `W-064` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ الدمج) |
| WI-018 | tooling-gates | T0 (قابليّةُ القياسِ · دعاوى القيودِ السابقةِ تصيرُ مُسجَّلةً ومقيسةً) | Driving H | المجلس التأسيسي | IN_REVIEW | tests/governance/test_w063_registered_claims.py | 2026-08-29 | 2026-09-05 | — (‏`mutation_claims.py` محجوزٌ لـ`WI-017` بالمالكِ نفسِه: عملٌ مزدوجٌ بقائدٍ واحدٍ · § 6.1) | بعدَ دمجِ المالكِ يُنقَلُ إلى `CLOSED` بقيدِ `W-063` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-017 | tooling-gates | T0 (قابليّةُ القياسِ · «الحرسُ مُجرَّبٌ بطفرةٍ» يصيرُ أمرًا يُعادُ) | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/mutation_probe.py · tools/governance/mutation_claims.py · tests/governance/test_w062_mutation_probe.py | 2026-08-29 | 2026-09-05 | — | بعدَ دمجِ المالكِ يُنقَلُ إلى `CLOSED` بقيدِ `W-062` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-016 | tooling-gates | T0 (قابليّةُ القياسِ · إشارةُ خطرٍ مكتوبةٌ تصيرُ رقمًا) | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/surface_debt_trend.py · tests/governance/test_w061_surface_debt_trend.py | 2026-08-29 | 2026-09-05 | — | بعدَ دمجِ المالكِ يُنقَلُ إلى `CLOSED` بقيدِ `W-061` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2` | — (يُكتَبُ بعدَ دمجِ المالك) |

---

## 2 · البنودُ المؤجَّلةُ صراحةً

| المعرِّف | النطاق | المالك | الحالة | الـtrigger الذي يُعيدُها | المصدر |
|---|---|---|---|---|---|
| WI-D01 | integrations | — | DEFERRED | دخولُ المسارِ `T5` واعتمادُ مزوِّدٍ خارجيٍّ بقرارٍ سياديّ | THE_ROADMAP § 9.2 |
| WI-D02 | agents | — | DEFERRED | إثباتُ إقليمٍ واحدٍ `PROVEN` قبلَ إضافةِ وكيلٍ جديد | THE_ROADMAP § 9.2 |
| WI-D03 | api-surface | — | DEFERRED | اكتمالُ المسارِ `T3` (هرمُ الاختبارِ والأمن) | THE_ROADMAP § 9.2 |

---

## 3 · تفاصيلُ البنودِ النشِطة

### WI-001 — طبقةُ حوكمةِ العملِ الإلزاميّة

```text
النطاق: governance-docs
المسار/المرحلة: T2 (الحوكمةُ والتوثيقُ المحروس)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: CLOSED
المسارات:
  docs/governance/work/
  tools/governance/check_work_governance.py
  tests/governance/test_work_governance_gate.py
  .github/workflows/ci.yml
  docs/governance/README.md
  docs/index.md            (سطرُ فهرسٍ يُشيرُ إلى الطبقةِ لا أكثر)
  README.md                (سطرُ بوّابةٍ يُشيرُ إلى الخارطةِ لا أكثر)
  docs/PROJECT_HANDBOOK.md (فقرةُ إحالةٍ في § 1 لا حقيقةٌ جديدة — بابُ الدخولِ يُحيلُ إلى الطريق)
  docs/audit/COMPLETION_LEDGER.md § 8  (قيدُ W-043 — واجبُ الدفعِ لا مِلكيّةُ نطاق)
  docs/audit/TRUTH_MATRIX.md · docs/audit/truth_matrix.json  (مُولَّدانِ آليًّا: أُعيدَ توليدُهما لأنَّ الملفّاتِ المُضافةَ تُغيِّرُ عدَّادَ الجردِ — ولم يُمَسَّ عدَّادُ المخالفاتِ: 63 قبلَ العملِ و63 بعدَه)
خارجَ النطاق:
  - لا يُعدَّلُ نصٌّ دستوريٌّ ولا مرسوم
  - لا تُعدَّلُ حالةُ إقليمٍ ولا مصفوفةُ الحقيقةِ ولا عدّادُ المخالفات
  - لا تُنشَأُ خريطةُ مراحلَ ثالثةٌ ولا ترقيمٌ موازٍ
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/
معيارُ القبول:
  1. البوّابةُ تسقُطُ على كلِّ مخالفةٍ في THE_ROADMAP § 13، وتنجحُ على السجلّاتِ الحاليّة
  2. الاختباراتُ تُغطّي كلَّ مخالفةٍ إسقاطًا ونجاحًا (اختبارُ رفضٍ لا نجاحٍ فقط)
  3. بوّاباتُ الهويّةِ والسجلِّ والـlint تبقى خضراءَ كما كانت
  4. لا مصدرَ حقيقةٍ جديدًا: كلُّ ما يملكُه المستودعُ يُحال إليه لا يُنسَخ
الدليلُ المطلوب:
  python tools/governance/check_work_governance.py --self-check
  pytest tests/governance/test_work_governance_gate.py -q
  python tools/governance/check_repository_identity.py .
  python tools/governance/check_completion_ledger.py --self-check
  ruff check .
بدأ: 2026-08-25        ينتهي الحجز: 2026-09-01
العائق: —
الخطوةُ التالية: — (البندُ مُغلَقٌ؛ لا عودةَ إلّا ببندٍ جديدٍ — § 4.3)
قيدُ السجلّ: W-043 · W-044 · W-045 · W-046   |   دمجُ #14 (2b355ca3) · #15 (b4d957fa)
```

### WI-002 — معالجةُ ديونِ التدقيق (DISC-004 و DISC-001) وتحديثُ خطّةِ التنفيذِ والحالة

```text
النطاق: audit-truth
المسار/المرحلة: T0 / T2 (قابليّةُ القياسِ والحوكمةُ المحروسة)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: CLOSED
المسارات:
  docs/audit/COMPLETION_LEDGER.md § 9
  EXECUTION_PLAN.md
  docs/governance/work/DISCOVERIES.md
  docs/governance/work/THE_ROADMAP.md § 16
  PROJECT_STATE.md
  docs/audit/ACTIVE_EXECUTION_STATE.md
  docs/governance/work/ACTIVE_WORK.md
خارجَ النطاق:
  - لا يُعدَّلُ نصٌّ دستوريٌّ ولا مرسومٌ ملكي
  - لا يُختلَقُ رقمٌ غيرُ مقيسٍ لمصفوفةِ الحقيقة
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/
معيارُ القبول:
  1. جدولُ ملخَّصِ § 9 في COMPLETION_LEDGER.md يُطابِقُ المقاسَ الفعليَّ (63 مخالفة: 60 IN_MEMORY_STORE + 2 HARDCODED_TRUTH + 1 SANDBOX_DISABLED)
  2. مفرداتُ EXECUTION_PLAN.md تُحَرَّرُ من الخلطِ بين DONE القديمةِ وحقيقةِ الإثباتِ DoD
  3. إغلاقُ DISC-004 و DISC-001 في DISCOVERIES.md برقمِ هذا البند
  4. تثبيتُ قرارِ الاعتمادِ A-1 في THE_ROADMAP.md بأمرِ المالكِ الصريح
  5. تحديثُ PROJECT_STATE.md و ACTIVE_EXECUTION_STATE.md بالواقعِ المقاس
  6. اجتيازُ كافّةِ بوّاباتِ الحوكمةِ والهويّةِ والسجلِّ ومصفوفةِ الحقيقة
الدليلُ المطلوب:
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_completion_ledger.py --self-check
  python tools/governance/check_repository_identity.py .
  python tools/governance/check_root_file_names.py . --source disk
  python tools/governance/truth_audit.py
بدأ: 2026-08-26        ينتهي الحجز: 2026-09-02
العائق: —
الخطوةُ التالية: — (البندُ مُغلَقٌ بعدَ استيفاءِ معاييرِ القبولِ وقيدِ W-047)
قيدُ السجلّ: W-047
```

---

### WI-003 — رباطُ `restart_survival` يُقاسُ لا يُصدَّقُ (‏وضعُ `bound`)

```text
النطاق: tooling-gates
المسار/المرحلة: T0 / T2 (قابليّةُ القياسِ والحوكمةُ المحروسة)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: CLOSED
المسارات:
  tools/governance/measurement_provenance.py
  tools/governance/restart_survival_probe.py
  .github/workflows/measure.yml
  tests/governance/test_w048_bound_provenance.py
  tests/governance/test_w037_measurement_provenance.py
  tests/governance/test_w038_probe_measure_mode.py
  docs/audit/measurements/README.md
  docs/PROJECT_HANDBOOK.md
  docs/audit/COMPLETION_LEDGER.md
  docs/audit/ACTIVE_EXECUTION_STATE.md
خارجَ النطاق:
  - لا يُمسُّ منطقُ قياسِ المِسبارِ نفسُه (`measure()` · أسطحُه · شاهدا الضبط) — العملُ في الرباطِ لا في المقيس
  - لا يُلمسُ ملفُّ القياسِ المنشورُ `docs/audit/measurements/restart_survival.json` بيدٍ — مولَّدٌ يُعادُ توليدُه لا يُحرَّر
  - لا يُمسُّ `Q-38` ولا `Q-29` ولا `Q-41` ولا أيُّ سؤالٍ سياديٍّ مفتوح
  - لا تُمسُّ البوّابتانِ الحمراوانِ (`B-9` · تدويرُ الأسرار) — بيدِ المالك
  - لا يُنقَصُ فحصٌ قائمٌ ولا يُوسَّعُ إعفاءٌ لتُخضَرَ بوّابةٌ
معيارُ القبول:
  1. وضعٌ رابعٌ `bound` في عقدِ النَّسَبِ يقيسُ الرباطَ نصًّا: ملفُّ الوقائعِ موجودٌ · الأمرُ فيه حرفًا بحرفٍ · غيرُ منزوعِ الأثرِ · مسارُ المُولِّدِ في مُشغِّلاتِ الوظيفة
  2. `measure.yml` يُعيدُ للحكمِ أثرَه: يُنزَعُ `|| true` ويُسمّى الخطوةُ بما تفعلُ لا «عرضًا»
  3. المِسبارُ في وضعِ `--check` لا يكتبُ ملفَ القياسِ المنشورَ — الحرسُ لا يحكمُ على ما يكتبُ (‏سابقةُ W-038)
  4. المحروسُ يصيرُ **8 من 10** والمُعلَنُ بلا حرسٍ **2** — مقيسًا من العقدِ لا منقولًا من نصٍّ
  5. فحصٌ جديدٌ يحرسُ الحرسَ: يصنعُ كلَّ عيبٍ (‏ملفٌ مفقودٌ · أمرٌ غائبٌ · `|| true` · `continue-on-error` · مُشغِّلاتٌ تتجاهلُ المُولِّدَ · حقولُ رباطٍ زينةٌ) وينتظرُ الحُمرةَ
  6. الحدُّ مُعلَنٌ لا مطويٌّ: الرباطُ يحرسُ **القدرةَ** لا **طزاجةَ** المنشورِ، ومضمونُه محروسٌ بـ`test_step18_restart_survival.py`
  7. الفحوصُ القائمةُ التي كانتْ تُثبِتُ الرقمَ القديمَ (7 من 10) تُحدَّرُ بصدقٍ ولا تُحذَفُ ولا تُضَعَف
  8. اجتيازُ بوّاباتِ ما قبلَ الدفعِ كلِّها، وثباتُ مخالفاتِ مصفوفةِ الحقيقةِ عندَ 63 بلا زيادةٍ
الدليلُ المطلوب:
  python tools/governance/measurement_provenance.py . --check --contract-only
  python -m pytest tests/governance/test_w048_bound_provenance.py -q
  python -m pytest tests/governance/test_w037_measurement_provenance.py tests/governance/test_w038_probe_measure_mode.py tests/governance/test_step18_restart_survival.py -q
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_work_governance.py --staged
  python tools/governance/check_completion_ledger.py --staged
  python tools/governance/check_repository_identity.py .
  python tools/governance/check_root_file_names.py . --source disk
  python tools/governance/truth_audit.py
بدأ: 2026-08-26        ينتهي الحجز: 2026-09-02
العائق: —
الخطوةُ التالية: — (البندُ مُغلَقٌ بعدَ استيفاءِ معاييرِ القبولِ وقيدِ W-048)
حدُّ الإغلاقِ — مُعلَنٌ لا مطويٌّ:
  - أُغلِقَ في التغييرِ نفسِه الذي قيَّدَه على سابقةِ `WI-002`/`W-047`، لأنَّ بوّابةَ الحوكمةِ تُلزِمُ بـ`POST_MERGE_NOT_CLOSED`
  - والإغلاقُ يعني أنَّ العملَ تمَّ ووُثِّقَ، **لا** أنَّ مراجعًا مستقلًّا حكمَ عليه — القرارُ `A-2` (‏تسميةُ مراجعٍ) معلَّقٌ بيدِ المالك
  - وحكمُ CI على دفعتِه لا يُمكنُ أن يُقَيَّدَ فيهِ نفسِه — يُقيِّدُه أوّلُ عملٍ تالٍ (‏سابقةُ `W-044`)
قيدُ السجلّ: W-048
```

---

### WI-004 — قيدُ ما بعدَ الدمجِ لـW-048، وقيدُ عطبِ بنيةِ CI الذي يمنعُ قراءةَ أيِّ حكمٍ

```text
النطاق: audit-truth
المسار/المرحلة: T0 (قابليّةُ القياسِ — قيدُ ما بعدَ الدمجِ وصدقُ الشاهد)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: CLOSED
المسارات:
  docs/governance/work/DISCOVERIES.md
  docs/governance/work/RISK_REGISTER.md
  docs/governance/work/ACTIVE_WORK.md
  docs/audit/COMPLETION_LEDGER.md
  docs/audit/ACTIVE_EXECUTION_STATE.md
خارجَ النطاق:
  - لا يُمَسُّ عملُ `W-048` نفسُه — قد دُمِجَ، وهذا قيدُ ما بعدَه لا تعديلٌ له
  - لا تُلمَسُ شِفرةُ أداةٍ ولا وظيفةُ CI: العطبُ في حسابِ `Actions` لا في المستودعِ، وإصلاحُه بيدِ المالكِ
  - لا يُعادُ ترقيمُ ماضٍ ولا يُصحَّحُ رقمٌ قِيسَ في جولةٍ سابقةٍ — الأرقامُ الماضيةُ سجلُّ جولاتِها
  - لا يُدَّعى أنَّ الحمراوَينِ `B-9` ما زالتا الحمراءَ الوحيدتَينِ — لم تُقرَأْ منذ 2026-08-25T22:00Z
معيارُ القبول:
  1. قيدُ الدمجِ: الطلبُ #17 دُمِجَ في `main` عندَ `832b0faa` — بيدِ المالكِ لا بيدي، فيُوثَّقُ لا يُدَّعى
  2. قيدُ العطبِ بشاهدٍ مقيسٍ: `steps=[]` و`runner_id=0` في ثلاثةِ تشغيلاتٍ بأرقامِها، وتحديدُ أوّلِ تشغيلٍ لم يُنفَّذْ وآخرِ تشغيلٍ نُفِّذَ
  3. إثباتُ أنَّ العطبَ **سبقَ** عملَ `W-048` ولم يُحدِثْه — بفارقِ زمنٍ مقيسٍ لا بدعوى
  4. تسجيلُ الاكتشافِ `DISC-006` موجَّهًا إلى المالكِ، والخطرِ `RK-011` بإشارةٍ مبكِّرةٍ **تُقاسُ بالواجهةِ**
  5. إعلانُ الأثرِ صريحًا: كلُّ دعوى «أخضرَ» أو «أحمرَ» في CI بعدَ 2026-08-25T22:00Z دعوى بلا شاهدٍ
الدليلُ المطلوب:
  gh api repos/zoorooz/AMOS-Fedration/actions/runs/32903824510/jobs   # with_steps=12 من 13 — آخرُ تشغيلٍ نُفِّذَ
  gh api repos/zoorooz/AMOS-Fedration/actions/runs/32908448189/jobs   # with_steps=0  من 13 — أوّلُ تشغيلٍ لم يُنفَّذْ
  gh api repos/zoorooz/AMOS-Fedration/actions/runs/32966866314/jobs   # with_steps=0  من 16 — دفعةُ W-048
  gh api repos/zoorooz/AMOS-Fedration/actions/permissions             # enabled: true — فالمنعُ ليس في إعدادِ المستودعِ
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_completion_ledger.py --staged
بدأ: 2026-08-26        ينتهي الحجز: 2026-09-02
العائق: —
الخطوةُ التالية: — (البندُ مُغلَقٌ بقيدِ W-049؛ وإصلاحُ حسابِ Actions بيدِ المالكِ ويبقى DISC-006 مفتوحًا عليه)
حدُّ الإغلاقِ — مُعلَنٌ لا مطويٌّ:
  - أُغلِقَ في التغييرِ نفسِه الذي قيَّدَه على سابقةِ `WI-002`/`W-047`، لأنَّ البوّابةَ تُلزِمُ بـ`POST_MERGE_NOT_CLOSED`
  - والإغلاقُ توثيقٌ لا مراجعةٌ — القرارُ `A-2` معلَّقٌ بيدِ المالك
  - وحكمُ CI على دفعتِه **لن يُقرأَ أيضًا** ما لم يُصلَحْ حسابُ `Actions`
قيدُ السجلّ: W-049
```

---

### WI-005 — قيدُ دمجِ #18 بإذنِ المالكِ صريحًا وبلا شاهدٍ من CI

```text
النطاق: audit-truth
المسار/المرحلة: T0 (صدقُ الشاهدِ — قيدُ ما بعدَ الدمجِ)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: CLOSED
المسارات:
  docs/governance/work/ACTIVE_WORK.md
  docs/governance/work/DISCOVERIES.md
  docs/audit/COMPLETION_LEDGER.md
  docs/audit/ACTIVE_EXECUTION_STATE.md
خارجَ النطاق:
  - لا يُمَسُّ محتوى `W-048` ولا `W-049` — كلاهما في الرأسِ، وهذا قيدُ ما بعدَهما
  - لا تُلمَسُ شِفرةٌ ولا وظيفةُ CI: العطبُ في حسابِ `Actions`، وإصلاحُه بيدِ المالكِ (`DISC-006`)
  - لا يُغلَقُ `DISC-006` — الدمجُ لا يُصلِحُ عطبًا، والقيدُ ليس دواءً
  - لا يُدَّعى أنَّ الشجرةَ خضراءُ في CI، ولا أنَّ `B-9` وحدَهما الحمراءُ
معيارُ القبول:
  1. قيدُ الدمجِ برقمِه وعقدتِه: #18 → `main` عندَ `f91da5d6` · 2026-08-26T22:58:20Z
  2. قيدُ الإذنِ لا كتمانُه: المالكُ اختارَ الدمجَ صريحًا بعدَ إعلامِه أنَّ الحكمَ غيرُ مقروءٍ
  3. قيدُ القياسِ الذي سبقَ الدمجَ لا القياسِ الذي يُرضي: ثلاثُ محاولاتٍ أُعيدَ تشغيلُها وكلُّها `with_steps=0`
  4. إعلانُ أنَّ الدمجَ جرى **بلا شاهدٍ من CI** — واسمُ ذلك في هذا المستودعِ **حلقةٌ مفتوحةٌ** لا خُضرةٌ
  5. بقاءُ `DISC-006` مفتوحًا موجَّهًا إلى المالكِ، وبقاءُ `RK-011` قائمًا
الدليلُ المطلوب:
  gh pr view 18 --json state,mergedAt,mergeCommit   # MERGED · 2026-08-26T22:58:20Z · f91da5d6
  gh api .../actions/runs/32973894416 --jq .run_attempt            # 3 محاولاتٍ
  gh api .../actions/runs/32973894416/attempts/3/jobs              # steps=0 · runner_id=0 في كلِّ وظيفةٍ
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_completion_ledger.py --staged
بدأ: 2026-08-26        ينتهي الحجز: 2026-09-02
العائق: —
الخطوةُ التالية: — (البندُ مُغلَقٌ بقيدِ W-050؛ وأوّلُ عملٍ يُشاهِدُ تشغيلًا نُفِّذَ فعلًا يُقيِّدُ حكمَ W-048 وW-049 وW-050)
حدُّ الإغلاقِ — مُعلَنٌ لا مطويٌّ:
  - أُغلِقَ في التغييرِ نفسِه الذي قيَّدَه لأنَّ البوّابةَ تُلزِمُ بـ`POST_MERGE_NOT_CLOSED` (سابقةُ `WI-002`/`W-047`)
  - والإغلاقُ توثيقٌ لا مراجعةٌ — القرارُ `A-2` معلَّقٌ بيدِ المالك
  - وحكمُ CI على دفعتِه لن يُقرأَ أيضًا ما لم يُصلَحْ حسابُ `Actions`
قيدُ السجلّ: W-050
```

---

### WI-006 — مقروئيّةُ حكمِ CI تُقاسُ بالخطواتِ لا بالنتيجةِ (حرسُ `RK-011` شِفرةً)

```text
النطاق: tooling-gates
المسار/المرحلة: T0 / T2 (صدقُ الشاهدِ · حرسٌ مُنفَّذٌ لا وثيقةٌ)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/ci_verdict_readability.py            (القدرةُ الجديدةُ — أداةٌ بمخرَجِ خروجٍ)
  tests/governance/test_w051_ci_verdict_readability.py  (حرسُ المعيارِ: 24 فحصًا · نجاحٌ ورفضٌ)
  tools/governance/measurement_provenance.py            (قيدُ القياسِ المنشورِ — سطرٌ في `REGISTRY`)
  tests/governance/test_w038_probe_measure_mode.py      (فحصُ عدٍّ حُوِّلَ من مساواةٍ إلى ترباسٍ — مُعلَنٌ في حدِّ البند)
  tests/governance/test_w048_bound_provenance.py        (فحصُ عدٍّ حُوِّلَ من مساواةٍ إلى ترباسٍ — مُعلَنٌ في حدِّ البند)
  docs/audit/measurements/ci_verdict_readability.json   (الحِملُ المنشورُ · وضعُ `declared` بسببٍ مكتوب)
  docs/audit/measurements/README.md                     (صفُّ فهرسٍ وسطرُ محتوياتٍ لا حقيقةٌ جديدة)
  docs/governance/work/DISCOVERIES.md                   (`DISC-006`: قياسٌ ثالثٌ يُضافُ لا استنتاجٌ)
  docs/governance/work/RISK_REGISTER.md                 (`RK-011`: تخفيفُه صارَ محروسًا بشِفرةٍ)
  docs/governance/work/ACTIVE_WORK.md                   (هذا البندُ نفسُه)
  docs/audit/COMPLETION_LEDGER.md § 8                   (قيدُ W-051 — واجبُ الدفعِ لا مِلكيّةُ نطاق)
  docs/audit/ACTIVE_EXECUTION_STATE.md                  (حالةُ اللحظةِ لا تاريخٌ جديد)
  docs/audit/TRUTH_MATRIX.md · docs/audit/truth_matrix.json  (مُولَّدانِ آليًّا: الملفّاتُ المُضافةُ تُغيِّرُ عدَّادَ الجردِ — ولم يُمَسَّ عدَّادُ المخالفات: 63 قبلَ العملِ و63 بعدَه)
خارجَ النطاق:
  - لا وظيفةَ CI جديدةً ولا تعديلَ في `.github/**`: ربطُ حرسٍ بشبكةٍ وتوكنٍ قرارُ تصميمٍ، وقرارُ التصميمِ للمالكِ
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/
  - لا يُمَسُّ عدّادُ المخالفاتِ ولا حالةُ إقليمٍ في مصفوفةِ الحقيقة
  - لا يُدَّعى أنَّ الشجرةَ خضراءُ ولا حمراءُ في CI: الأداةُ تقولُ «غيرُ مقروءٍ» ولا تقولُ أكثر
  - لا يُصلَحُ حسابُ `Actions` (‏دقائقُ · حدُّ إنفاقٍ · وسيلةُ دفعٍ): بيدِ المالكِ وحدَه — `DISC-006`
  - لا يُغلَقُ `DISC-006` ولا `RK-011`: القياسُ ليس دواءً
  - لا يُدمَجُ هذا العملُ بيدِ المنفِّذِ: الدمجُ للمالكِ
معيارُ القبول:
  1. الأداةُ تُصنِّفُ كلَّ وظيفةٍ من حِملِ `runs/{id}/jobs`: `EXECUTED` (بدأت خطوةٌ) · `NOT_DISPATCHED` (لا خطواتٍ ولا عاملٌ) · `SKIPPED` (خارجَ المقامِ) · `AMBIGUOUS`
  2. حكمُ التشغيلِ يُبنى على الخطواتِ لا على `conclusion`، و`conclusion_quotable` لا يصدُقُ إلّا مع `READABLE`
  3. تُعيدُ الأداةُ **رفضًا** (خروجٌ 2 · `MeasurementRefused`) حينَ لا تملكُ ما تقيسُ به — والرفضُ ليس حكمًا
  4. الأداةُ تُعادُ حيًّا (`--repo/--run`) وبلا شبكةٍ (`--from-json`) بالنتيجةِ نفسِها على الحِملِ نفسِه
  5. تُصدِّقُ الأداةُ قياسَ اليدِ في `W-049`: تشغيلُ `32903824510` → 12/13 وظيفةً منفَّذةً حرفًا بحرفٍ
  6. لا `except` صامتٌ ولا سرٌّ في الشِفرةِ: التوكنُ من البيئةِ وحدَها ولا يُطبَعُ ولا يُقيَّدُ
  7. البوّاباتُ الستُّ وعقدُ نسبِ القياساتِ تبقى خضراءَ كما كانت، وعدّادُ المخالفاتِ 63 لم يتغيَّر
الدليلُ المطلوب:
  pytest tests/governance/test_w051_ci_verdict_readability.py -q          # 24 passed
  python tools/governance/ci_verdict_readability.py --repo zoorooz/AMOS-Fedration --run 32903824510
  python tools/governance/measurement_provenance.py . --check --contract-only
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_completion_ledger.py --staged
  python tools/governance/check_repository_identity.py .
  ruff check .
بدأ: 2026-08-27        ينتهي الحجز: 2026-09-03
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` ويُكتَبُ في `قيدُ السجلّ`: `W-051` ورقمُ الدمجِ وعقدتُه — § 7
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - `IN_REVIEW` لا `CLOSED`: لم يُدمَجْ بعدُ، وإغلاقُه قبلَ الدمجِ دعوى لا قيد (‏وهو خلافُ ما فعلَه `WI-003`/`WI-004`/`WI-005` — أُغلِقت في دفعتِها لأنَّ القيدَ كان قيدَ دمجٍ قد وقع)
  - `VERIFIED` غيرُ مُتاحٍ: يلزمُه مراجعٌ مستقلٌّ، وتسميتُه قرارٌ سياديٌّ معلَّقٌ (`A-2`)
  - `الأداةُ تحرسُ **معيارَ** القراءةِ لا **حالةَ** CI: ولا تُنشِئُ شاهدًا، ولا تُغني عن تشغيلٍ يُنفَّذُ فعلًا
  - **فحصانِ قائمانِ حُوِّلا بصدقٍ ولم يُحذَفا ولم يُضعَّفا**: `test_guarded_count_is_eight_of_ten` و`test_guarded_count_matches_the_registry` كانا يُثبِّتانِ «10 مقيَّدًا · 2 مُعلَنًا» **بالمساواةِ**، فكانا يسقُطانِ على إضافةِ قياسٍ مشروعٍ لا على تخفيفِ حرسٍ. فصارا **ترباسًا**: الكلُّ يرتفعُ · والمحروسُ لا ينقُصُ (≥ 8) · والمُعلَنُ بلا حرسٍ لا يتكاثرُ (≤ 3) · وكلُّ مُعلَنٍ له سببٌ مكتوبٌ
  - **والثمنُ يُعلَنُ لا يُطوى**: المُعلَنُ بلا حرسٍ ارتفعَ **من 2 إلى 3** — وذاك ثمنُ قياسٍ يلزمُه واجهةٌ حيّةٌ، لا رخصةٌ لرابعٍ
  - واجبُ ما بعدَ الدمجِ لـ`W-048`/`W-049`/`W-050` **يبقى مفتوحًا**: أوّلُ عملٍ يُشاهِدُ تشغيلًا نُفِّذَ فعلًا يُقيِّدُ حكمَه
قيدُ السجلّ: — (يُكتَبُ بعدَ دمجِ المالك)
```

---

### WI-007 — مِسبرُ بصماتِ السجلِّ يقرأُ التاريخَ كلَّه أو يرفضُ — ولا يقولُ «ليسَ في السجلِّ» بلا حقٍّ

```text
النطاق: tooling-gates
المسار/المرحلة: T0 (صدقُ القياسِ نفسِه · واجبٌ مُعلَنٌ منذُ `W-037` يُوفَّى)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/audit/final_audit.py                             (القسمُ السادسُ — قاعدةُ القياسِ أُصلِحَت وأُضيفَ رفضٌ مُصنَّف)
  tests/governance/test_w052_history_hash_probe.py       (حرسُ المعيارِ: 20 فحصًا على مستودعاتِ git حقيقيّةٍ موقوتةٍ بلا شبكةٍ)
  docs/governance/work/OWNERSHIP.md                      (تسجيلُ `tools/audit` — القاعدةُ 3 تأمرُ به قبلَ العملِ لا بعدَه)
  وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ: ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md · TRUTH_MATRIX.md · truth_matrix.json (‏مُوَلَّدان)
  وسببُ تركِها غيرَ مُعلَنةٍ في عمودِ المساراتِ واحدٌ: البندُ `WI-006` حاجزٌ عليها وهو `IN_REVIEW`، فالدّعوى تُسقِطُ `CLAIM_CONFLICT` بحقٍّ
خارجَ النطاق:
  - لا يُمَسُّ `docs/audit/ACTIVE_EXECUTION_STATE.md`: محجوزٌ لـ`WI-006` وغيرُ مُعفًى — ومسُّه تجاوزُ حاجزٍ لا اجتهادٌ
  - لا يُمَسُّ `tools/governance/measurement_provenance.py`: محجوزٌ لـ`WI-006`؛ ونصُّ السببِ فيه ما زالَ يوصِفُ هشاشةً أُصلِحَت — فقُيِّدَ واجبًا لا يُطوى (`DISC-007`)
  - لا يُعادُ توليدُ `docs/audit/measurements/final_audit_p14.json`: يلزمُه نسخٌ كاملُ العمقِ، وبيئتي مُوَطَّنةٌ من `tarball` بقيدٍ مُصطنَعٍ واحدٍ
  - لا تُوسَّعُ حقولُ الحِملِ ولا يُنقصُ منها: ثلاثةٌ وعشرونَ مفتاحًا كما كانَت — لأنَّ دعوى «21 قياسًا» في الترويسةِ وفي فهرسِ القياساتِ تصدُقُ بها وتكذِبُ بزيادةٍ
  - لا تُسجَّلُ التِّسعُ الباقيةُ تحتَ `tools/`: تعيينُ مالكٍ وحدودِ نطاقٍ قرارٌ للمالكِ — قُيِّدَ ولم يُحسَمْ (`DISC-008` · `RK-012`)
  - لا يُدَّعى أنَّ البصماتِ الثلاثَ والأربعينَ في الواقعِ صحيحةٌ أو فاسدةٌ: المِسبرُ يقيسُ ولا يُفتي
  - ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ: الدمجُ للمالكِ
معيارُ القبول:
  1. يُقرأُ السجلُّ **بكاملِ عمقِه** لا بنافذةٍ مقطوعةٍ: حُذِفَ `-n 400` ولم يُكبَّرْ — ورقمٌ أكبرُ يؤجِّلُ الكذبَ ولا يمنعُه
  2. يُحكَمُ بالسابقةِ (`startswith`) على `%H` الكاملِ، لا بمساواةِ `%h` المختصرِ — فطولُ الاختصارِ ينمو بعددِ الكائناتِ (`core.abbrev=auto`) وليسَ عقدًا
  3. يلتقطُ التعبيرُ البصماتِ من 7 إلى 40 خانةً (`[0-9a-f]{7,40}`)، فقد كانَ يقصِرُ على سبعٍ فيمرُّ بالأربعينَ بلا فحصٍ
  4. حينَ لا يملكُ ما يقيسُ به **يرفضُ ولا يحكُمُ**: خروجٌ 2 و`REFUSED:` في مجرى الخطأِ ولا حِملَ يُطبَعُ — ثلاثُ أبوابٍ: لا git · نسخٌ ضحلٌ (‏ويُسمَّى الدواءُ `fetch-depth: 0`) · `git log` يفشلُ
  5. لا حرسَ لا يُبلَغُ فرعُه: حرسُ «سجلٍّ فارغٍ» **لم يُكتَبْ** لأنَّ git نفسَه يخرجُ بخللٍ قبلَه — مقيسٌ ومكتوبٌ في الشِفرةِ (‏سابقةُ `W-051`)
  6. المِسبرُ يقيسُ ولا يكتبُ: `git status` قبلَه وبعدَه واحدٌ حرفًا بحرفٍ
  7. مجموعةُ مفاتيحِ الحِملِ لم تتغيَّرْ (23)، والبوّاباتُ وعقدُ النَّسبِ خضراءُ، وعدّادُ المخالفاتِ 63 لم يرتفعْ
  8. والفحصُ يُثبِتُ **الكذبَ القديمَ** لا الصدقَ الجديدَ وحدَه: قياسٌ مقابِلٌ على المستودعِ نفسِه يُري أنَّ القاعدةَ القديمةَ كانَت تقولُ «ليسَ في السجلِّ» عن قيدٍ قائمٍ
الدليلُ المطلوب:
  pytest tests/governance/test_w052_history_hash_probe.py -q            # 20 passed
  python tools/audit/final_audit.py                                     # خروجٌ 0 · حِملٌ بـ22 مفتاحًا (‏21 قياسًا)
  خمسُ طفراتٍ مقصودةٍ في الشِفرةِ — وكلُّ واحدةٍ أُمسِكَت
  python tools/governance/check_work_governance.py --self-check · --staged
  python tools/governance/check_completion_ledger.py --self-check · --staged
  python tools/governance/check_repository_identity.py .
  python tools/governance/check_root_file_names.py . --source disk
  python tools/governance/measurement_provenance.py . --check --contract-only
  python tools/governance/truth_audit.py
  ruff check .
بدأ: 2026-08-27        ينتهي الحجز: 2026-09-03
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` ويُكتَبُ في `قيدِ السجلّ`: `W-052` ورقمُ الدمجِ وعقدتُه — § 7؛ ويُصحَّحُ نصُّ السببِ في `measurement_provenance.py` متى انفكَّ حجزُ `WI-006`
حدُّ البندِ — مُعلَنٌ لا مطويّ:
  - **هذا إصلاحُ قاعدةِ قياسٍ لا إصلاحُ دَينٍ**: عدّادُ الدَّينِ 182 كما كانَ، والأسئلةُ 42 كما كانَت — ولا قدرةَ جديدةَ في المنتَجِ
  - **والعطبُ ليسَ مفترَضًا كلُّه**: `main` اليومَ **270 التزامًا** وأعمقُ بصمةٍ مذكورةٍ `0111c95` عندَ العمقِ **135** — فالهامشُ 265 التزامًا قبلَ أن تبدأَ النافذةُ القديمةُ بالكذبِ. **لكنَّ العيبَينِ الآخرَينِ كانا يكذِبانِ اليومَ فعلًا**: بصمتانِ من أربعينَ خانةً (`024f8ab1…` · `6a86205c…`) لم تُفحَصا قطُّ — 43 مذكورةً والمقروءُ 41
  - **ومخرَجُ بيئتي ليسَ حكمًا على المستودعِ**: شجرتي مُوَطَّنةٌ من `tarball` بقيدٍ مُصطنَعٍ واحدٍ، فيقولُ المِسبرُ عندي `43 من 43` ليسَ في السجلِّ — **وذاك صدقٌ عن شجرتي لا عن `main`**؛ والحكمُ الصادقُ يلزمُه نسخٌ كاملُ العمقِ في CI
  - **والقياسُ لم يُقَدْ بـCI**: لا تشغيلَ منفَّذًا في المستودعِ منذُ 2026-08-26T23:05:02Z (`DISC-006` بيدِ المالكِ) — **فلا يُدَّعى أنَّ الشجرةَ خضراءُ**
  - `VERIFIED` غيرُ مُتاحٍ: يلزمُه مراجعٌ مستقلٌّ وتسميتُه قرارٌ سياديٌّ معلَّقٌ (`A-2`)، و`CLOSED` قبلَ الدمجِ دعوى لا قيدٌ
  - **وتسجيلُ `tools/audit` في `OWNERSHIP.md` فعلٌ إداريٌّ تأمرُ به القاعدةُ 3 لا اجتهادٌ منِّي**، وأُلحِقَ بأقربِ نطاقٍ جنسًا لا بنطاقٍ مُبتدَعٍ — **وللمالكِ نقضُه وإعادةُ توزيعِه**
قيدُ السجلّ: — (يُكتَبُ بعدَ دمجِ المالك)
```

---

### WI-019 — الحكمُ الأحمرُ يُقرأُ أوّلًا ثمَّ يُخضَّرُ من سببِه لا من قياسِه

```text
النطاق: tooling-gates
المسار/المرحلة: T0 — قابليّةُ القياسِ: حكمُ CI يصيرُ مقروءًا ومُخضَّرًا بإصلاحِ السببِ
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/crown/secret_scan_exceptions.py          — سجلُّ استثناءاتِ التاريخِ، مسارٌ جديدٌ لم يُحجَزْ
  tests/crown/test_w064_secret_scan_exceptions.py — حرسُ السجلِّ، مسارٌ جديدٌ كذلك
  tools/crown/verify_secret_boundaries.py        — تُوصَلُ بوّابةُ التاريخِ بالسجلِّ وتُزادُ بوّابةُ إعفاءٍ ميتٍ
  tests/sovereignty/test_outbox.py               — الفتيلُ: كتلةُ PEM المكتوبةُ حرفًا تُبنى بالتركيبِ
  docs/security/SECRET_BOUNDARIES.md             — عددُ البوّاباتِ ووصفُ السجلِّ يُطابِقانِ التنفيذَ
  conftest.py                                    — حزمةُ الخدماتِ تُرى من شجرتِها إن لم تُركَّبْ (‏`DISC-026`)
  tests/governance/test_w064_services_src_fallback.py — حرسُ ذلك الشرطِ، مسارٌ جديدٌ
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - أمرُ المالكِ في 2026-08-29 نصًّا: يُدمَجُ المفتوحُ، ثمَّ يُصلَحُ الحكمُ الأحمرُ في CI
    ويُصلَحُ كلُّ خطأٍ قبلَ التقدُّمِ في الخارطةِ
  - و`DISC-006` كانَ يمنعُ قراءةَ الحكمِ أصلًا (‏`steps=[]` · `runner_id=0`): وقد زالَ
    مانعُه بانتقالِ المستودعِ إلى حسابٍ فيه دقائقُ تشغيلٍ، فصارَ الحكمُ **مقروءًا
    مقيسًا** بـ`ci_verdict_readability.py` — انظر `DISC-023`
  - والحمراءُ نفسُها سببُها **سطرُ اختبارٍ سلبيٍّ** يحملُ كتلةَ PEM حرفًا، لا حرسٌ ضعيفٌ
    ولا شِفرةٌ فاسدةٌ — انظر `DISC-024`
خارجَ النطاق:
  - **لا يُوسَّعُ نمطُ الماسحِ ولا يُعفى مجلَّدُ اختباراتٍ**: الإعفاءُ لبصمةِ نصِّ سطرٍ
    رُوجِعَ فردًا فردًا، ومعَه بوّابةٌ تُسقِطُ الإعفاءَ الميتَ
  - لا يُعادُ كتابةُ تاريخِ git: بصماتُ الالتزامِ وأرقامُ الدمجِ مُقيَّدةٌ في السجلِّ،
    فمحوُها لإصلاحِ سطرٍ ليس سرًّا إفسادٌ لسلسلةِ الإثباتِ
  - لا يُمَسُّ `.github/` (‏`DISC-006`): البوّابةُ في ملفِّ سيرٍ محجوزٍ للمالكِ، والإصلاحُ
    في الشجرةِ لا في السيرِ
  - لا تُغلَقُ بنودٌ مدموجةٌ ولا تُنقَلُ حالةٌ إلى `VERIFIED`: طريقُ الإغلاقِ موقوفٌ على `A-2`
معيارُ القبول:
   1. `python tools/crown/verify_secret_boundaries.py` يخرُجُ بصفرٍ من **سببِه** لا بتخفيفٍ
   2. سطرٌ يُشبِهُ المفتاحَ ولا بصمةَ له في السجلِّ يبقى مخالفةً (مُبرهَنٌ بفحصٍ)
   3. إعفاءٌ لا يقابلُه سطرٌ في التاريخِ = مخالفةٌ مُسمّاةٌ لا سكوتٌ
   4. قيمةُ الاختبارِ السلبيِّ تبقى ترويسةَ PEM **تامّةً** عندَ التشغيلِ: الحرسُ لم يَضعُفْ
   5. حكمُ CI مقروءٌ مقيسًا (‏`READABLE`) قبلَ أن يُنسَبَ إليه أخضرُ أو أحمرُ
   6. الانحدارُ كاملًا بلا نقصٍ عن المقيسِ قبلَ البندِ
الدليلُ المطلوب:
  python tools/crown/verify_secret_boundaries.py                          # PASS 12/12 · خروجٌ 0
  pytest tests/crown/test_w064_secret_scan_exceptions.py -q               # 8 فحوصٍ · حرسُ السجلِّ
  pytest tests/sovereignty/test_outbox.py -q                              # 89 فحصًا · الفتيلُ مُصلَحٌ
  python tools/governance/ci_verdict_readability.py --from-json <jobs>    # READABLE · نُفِّذَت 13/13
  pytest tests/ -q                                                        # الانحدارُ كاملًا
بدأ: 2026-08-29        ينتهي الحجز: 2026-09-06
العائق: —
الخطوةُ التالية: بعدَ الدمجِ يُقرأُ حكمُ CI على «main» بالأداةِ، ويُنقَلُ البندُ إلى `CLOSED` إن فُتِحَ طريقُ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  يُخضِّرُ هذا البندُ وظيفتَينِ سقطَتا بسببٍ واحدٍ مقيسٍ، **ولا يَزعُمُ** أنَّ المستودعَ صارَ
  بلا عَطبٍ: الحكمُ صارَ مقروءًا فصارَ ما فيه من حمرةٍ يُقرأُ ويُصلَحُ واحدةً واحدةً.
  والاستثناءُ المُعلَنُ لا يُطهِّرُ التاريخَ، بل يُعلِنُ أنَّ نصًّا بعينِه رُوجِعَ فلم يكنْ سرًّا.
```

---

### WI-018 — دعاوى الطفرةِ في القيودِ السابقةِ تصيرُ مُسجَّلةً ومقيسةً

```text
النطاق: tooling-gates
المسار/المرحلة: T0 — قابليّةُ القياسِ: «هذا الحرسُ مُجرَّبٌ بطفرةٍ» في قيدٍ مُقفَلٍ يصيرُ رقمًا يُعادُ
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tests/governance/test_w063_registered_claims.py    — حرسُ صدقِ السجلِّ، مسارٌ جديدٌ لم يُحجَزْ قبلَ اليومِ
  و`tools/governance/mutation_claims.py` **لا يُدرَجُ في خليّةِ حجزِ هذا البندِ** لأنَّ حجزَه قائمٌ
  لـ`WI-017` (‏`IN_REVIEW`) ولا يُحجَزُ مسارٌ مرّتَينِ: فالطريقُ المُعلَنُ هنا هو الثالثُ من
  § 6.1 — **عملٌ مزدوجٌ بقائدٍ واحدٍ** (المالكُ نفسُه · المراجعُ نفسُه)، وهو مُقيَّدٌ في حقلِ
  العائقِ في صفِّ البندِ لا مطويٌّ. ولولا هذا الإعلانُ لأسقطَتْه البوّابةُ بـ`CLAIM_CONFLICT`
  — وقد أسقطَتْه فعلًا في أوّلِ تشغيلٍ، فصُحِّحَ الإعلانُ ولم يُلمَسِ الحرسُ
  وما سواها مُعفًى من الحجزِ بنصِّ § 6 (سجلّاتُ العملِ والاكتشافِ والقيدِ والمصفوفةُ المُعادَةُ
  التوليدِ وسطرُ «آخرِ قيدٍ» في وثيقتَي الحالةِ وحدَه)
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - «ما بقي» في قيدِ `W-062` وترويسةُ مِلَفِّ الدعاوى نصَّا حرفًا أنَّ دعاوى القيودِ السابقةِ
    **لم تُسجَّلْ بعدُ**، وأنَّ ذاك نقصٌ يُسَدُّ قيدًا بعدَ قيدٍ — فهذا البندُ يسدُّ نقصًا
    أعلنَه القيدُ السابقُ عن نفسِه
  - و§ 7 (البندُ 10) لا يعرِفُ حسمًا سياديًّا محسومًا غيرَ منفَّذٍ اليومَ، وهذا بندٌ من § 6
    **لا يحتاجُ قرارًا سياديًّا** ولا سرًّا ولا شبكةً ولا حسابَ Actions
خارجَ النطاق:
  - **لا تُسجَّلُ التسعةُ الباقيةُ اليومَ**: سُجِّلَ `W-055` و`W-056` و`W-059`، والباقي
    (`W-029` · `W-030` · `W-051` · `W-052` · `W-053` · `W-054` · `W-057` · `W-058` · `W-060`)
    مُعلَنٌ في `UNREGISTERED_WORK` **ومحروسٌ بفحصٍ** فلا يُقرأُ صمتُه اكتمالًا
  - **لا يُوسَّعُ حرسٌ محجوزٌ لبندٍ مفتوحٍ**: نقصُ عضِّ قاعدةِ `SELF_EXCLUDED` (فحصٌ واحدٌ لا اثنانِ)
    يُصلَحُ في `tests/governance/test_w056_sovereign_decision_status.py` وهو محجوزٌ لـ`WI-011`
    وطريقُ إغلاقِه موقوفٌ على `A-2` — فقُيِّدَ `DISC-022` ولم يُمَسَّ الملفُّ
  - **ولا يُخفَّفُ حدُّ المِسبارِ لتخضيرِ رقمٍ**: الرقمُ المُسجَّلُ هو **المقيسُ** (1) لا المنشورُ (2)
  - لا يُمَسُّ نصُّ قيدٍ سابقٍ في `COMPLETION_LEDGER.md`: التاريخُ لا يُعادُ كتابتُه، والفرقُ يُقيَّدُ
  - لا يُنشَرُ حِملُ قياسٍ تحتَ `docs/audit/measurements/` (`DISC-014`)، ولا يُمَسُّ `.github/` (`DISC-006`)
  - لا تُغلَقُ بنودٌ مدموجةٌ ولا تُنقَلُ حالةٌ إلى `VERIFIED`، ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ
معيارُ القبول:
   1. دعاوى `W-055` و`W-056` و`W-059` مُسجَّلةٌ بنصِّ عَطبٍ **موجودٍ مرّةً واحدةً** في هدفِه
   2. كلُّ رقمٍ مُسجَّلٍ **مقيسٌ بالمِسبارِ** لا منقولٌ من نثرٍ، وما اختلفَ عن المنشورِ يُقيَّدُ اكتشافًا
   3. قائمةُ القيودِ غيرِ المُسجَّلةِ **مُعلَنةٌ في الشِفرةِ ومحروسةٌ**: قيدٌ يدَّعي طفرةً ولا هو
      مُسجَّلٌ ولا مُعلَنٌ ناقصًا = فحصٌ ساقطٌ
   4. لا طفرةٌ تستهدفُ ملفَّ فحصٍ: العَطبُ يُعادُ في الحرسِ المقيسِ لا في الفحصِ الذي يقيسُه
   5. دعوى هذا السجلِّ نفسِه مُسجَّلةٌ ومُجرَّبةٌ به: ثلاثُ طفراتٍ على مِلَفِّ الدعاوى تُسقِطُ حرسَه
   6. المِسبارُ كلُّه يخرُجُ بصفرٍ بعدَ التسجيلِ: 31 طفرةً · 31 مُلتقَطةً لستِّ دعاوى
الدليلُ المطلوب:
  python tools/governance/mutation_probe.py --work W-055                  # 4 طفراتٍ · 4 مُلتقَطةٌ
  python tools/governance/mutation_probe.py --work W-056                  # 7 طفراتٍ · 7 مُلتقَطةٌ
  python tools/governance/mutation_probe.py --work W-059                  # 2 طفرتانِ · 2 مُلتقَطةٌ
  python tools/governance/mutation_probe.py --work W-063                  # 3 طفراتٍ · 3 مُلتقَطةٌ
  python tools/governance/mutation_probe.py                               # خروجٌ 0 · 31 · 31
  pytest tests/governance/test_w063_registered_claims.py -q               # 10 فحوصٍ · حرسُ صدقِ السجلِّ
  pytest tests/governance/test_w062_mutation_probe.py -q                  # 24 فحصًا · بلا انحدارٍ
  pytest tests/ -q                                                       # الانحدارُ كاملًا
  python tools/governance/check_work_governance.py --staged               # صفرُ مخالفاتٍ
  python tools/governance/check_completion_ledger.py --staged             # صفرُ مخالفاتٍ
  python tools/governance/state_document_drift.py                        # صفرُ انحرافٍ
بدأ: 2026-08-29        ينتهي الحجز: 2026-09-05
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-063` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  ثلاثةُ قيودٍ سابقةٍ من اثني عشرَ تدَّعي طفرةً صارت مقيسةً (‏وأُضيفَ إليها هذا القيدُ نفسُه)؛
  فمن قرأَ «31 مُلتقَطةً» شهادةَ سلامةٍ
  للمستودعِ كلِّه فقد قرأَ ما لم يُكتَبْ. والمِسبارُ يقيسُ **عَطبًا بعينِه** لا كلَّ عَطبٍ ممكنٍ،
  وصدقُ الأرقامِ التسعةِ الباقيةِ ما زالَ دعوى نثرٍ حتى تُسجَّلَ.
```

---

### WI-017 — «الحرسُ مُجرَّبٌ بطفرةٍ» يصيرُ أمرًا يُعادُ لا عبارةً تُقرأُ

```text
النطاق: tooling-gates
المسار/المرحلة: T0 — قابليّةُ القياسِ: دعوى حرسٍ مكتوبةٌ في سجلٍّ تصيرُ تشغيلًا يُعادُ ويُقاسُ
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/mutation_probe.py            — المُشغِّلُ، مسارٌ جديدٌ لم يُحجَزْ قبلَ اليومِ
  tools/governance/mutation_claims.py           — الدعاوى بياناتٍ، مسارٌ جديدٌ كذلك
  tests/governance/test_w062_mutation_probe.py  — حرسُ الاثنَينِ، مسارٌ جديدٌ كذلك
  وما سواها مُعفًى من الحجزِ بنصِّ § 6 كما في البندِ السابقِ (سجلّاتُ العملِ والقيدِ والمصفوفةُ
  المُعادَةُ التوليدِ وسطرُ «آخرِ قيدٍ» في وثيقتَي الحالةِ وحدَه)
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - «ما بقي» في قيدِ `W-061` نصَّ حرفًا: «**والتحقُّقُ بالطفرةِ ما زالَ بيدٍ** لا أداةً في الشجرةِ» —
    فهذا البندُ يسدُّ نقصًا **أعلنَه القيدُ السابقُ عن نفسِه**، لا نقصًا اكتُشِفَ اليومَ
  - و`RK-019` في جوهرِه هذا: قيدٌ يُقرأُ حرسًا وليس في الشجرةِ ما يقيسُه. وقد صارَ لكلِّ قيدٍ
    مِرساةٌ في `W-061`، لكنَّ **صدقَ المِرساةِ** نفسِه كانَ يُقاسُ بيدٍ في نسخةٍ تُمحى
  - ومن `W-051` إلى `W-061` تكرَّرَت عبارةُ «مُجرَّبٌ بطفرةٍ» أحدَ عشرَ قيدًا: لا يُعادُ تجريبُها بأمرٍ،
    ولا يعترضُ شيءٌ من أضعفَ حرسًا لاحقًا فمرَّت طفرتُه
  - ولا يلزمُه قرارٌ سياديٌّ ولا سرٌّ ولا شبكةٌ ولا حسابُ Actions
خارجَ النطاق:
  - **لا تُسجَّلُ دعاوى القيودِ السابقةِ كلُّها اليومَ**: سُجِّلَ `W-061` و`W-062`، والبقيّةُ نقصٌ
    **مُعلَنٌ** في ترويسةِ مِلَفِّ الدعاوى يُسَدُّ قيدًا بعدَ قيدٍ — ولا يُقرأُ صمتُه اكتمالًا
  - لا يُمَسُّ حرسٌ قائمٌ ولا أداةٌ محجوزةٌ لبندٍ مفتوحٍ: الطفراتُ تُطبَّقُ في **نسخةٍ** لا في الشجرةِ
  - لا يُنشَرُ حِملُ قياسٍ تحتَ `docs/audit/measurements/` (`DISC-014`)، ولا يُمَسُّ `.github/` (`DISC-006`)
  - لا يُعدَّلُ نصُّ الخارطةِ ولا `OWNERSHIP.md` ولا يُضافُ صفُّ قرارٍ `Q-###`
  - لا تُغلَقُ بنودٌ مدموجةٌ ولا تُنقَلُ حالةٌ إلى `VERIFIED`، ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ
  - **ولا يُدَّعى حكمُ CI**: أحكامُ Actions غيرُ مقروءةٍ (`DISC-006`)
معيارُ القبول:
   1. أمرٌ واحدٌ يُعيدُ كلَّ عَطبٍ مُعلَنٍ في نسخةٍ معزولةٍ ويُعلِنُ عددَ الفحوصِ الساقطةِ عندَ كلِّ عَطبٍ
   2. نجاةُ طفرةٍ = مخالفةٌ مُسمّاةٌ (`GUARD_SURVIVED_MUTATION`) لا سطرٌ صامتٌ
   3. رقمٌ مُعلَنٌ في سجلٍّ لا يطابقُ المقيسَ = مخالفةٌ مُسمّاةٌ (`FAILURE_COUNT_MISMATCH`)
   4. دعوى صارَ نصُّها غيرَ موجودٍ أو مُبهَمًا = مخالفةٌ (`MUTATION_PATTERN_STALE`) لا تجاهُلٌ
   5. قاعدةٌ ساقطةٌ قبلَ الطفرةِ = **رفضٌ** لا قياسٌ (`BASELINE_NOT_GREEN`)
   6. المِسبارُ **لا يكتبُ سطرًا** في الشجرةِ التي يحكمُ عليها — ولا بايتكودَ كذلك
   7. دعوى المِسبارِ نفسِه مُسجَّلةٌ ومُجرَّبةٌ به: من يحرسُ الحارسَ سؤالٌ مُجابٌ برقمٍ
   8. الأرقامُ المنشورةُ في `W-061` تُعادُ آليًّا فتُطابِقُ ما نُشِرَ: 2 · 5 · 2 · 1 · 1 · 1 · 1
الدليلُ المطلوب:
  python tools/governance/mutation_probe.py --list                        # سردُ الدعاوى بلا تشغيلٍ
  python tools/governance/mutation_probe.py --work W-061                  # سبعُ طفراتٍ · سبعُ التقاطاتٍ
  python tools/governance/mutation_probe.py --work W-062                  # ثمانِ طفراتٍ · ثمانِ التقاطاتٍ
  python tools/governance/mutation_probe.py                               # خروجٌ 0 · طفراتٌ 15 · مُلتقَطةٌ 15
  pytest tests/governance/test_w062_mutation_probe.py -q                  # 24 فحصًا · حرسُ المِسبارِ
  pytest tests/ -q                                                       # الانحدارُ كاملًا
  python tools/governance/check_work_governance.py --staged               # صفرُ مخالفاتٍ
  python tools/governance/check_completion_ledger.py --staged             # صفرُ مخالفاتٍ
  python tools/governance/state_document_drift.py                        # صفرُ انحرافٍ
بدأ: 2026-08-29        ينتهي الحجز: 2026-09-05
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-062` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  يُثبِتُ هذا البندُ أنَّ الدعاوى **المُسجَّلةَ** مُجرَّبةٌ بأمرٍ يُعادُ، **ولا يُثبِتُ** أنَّ كلَّ حرسٍ
  في المستودعِ مُجرَّبٌ: خمسةَ عشرَ عَطبًا من قيدَينِ سُجِّلَت، وتسعةُ قيودٍ سابقةٍ لم تُسجَّلْ بعدُ.
  والطفرةُ استبدالُ نصٍّ، فهي تُحاكي عَطبًا بعينِه لا كلَّ عَطبٍ ممكنٍ؛ فمن قرأَ «مُلتقَطةٌ 15»
  شهادةَ سلامةٍ عامّةً فقد قرأَ ما لم يُكتَبْ.
```

---

### WI-016 — إشارةُ الخطرِ المكتوبةُ تصيرُ رقمًا: اتِّجاهُ دَينِ الأسطحِ يُقاسُ بينَ قيدَينِ

```text
النطاق: tooling-gates
المسار/المرحلة: T0 — قابليّةُ القياسِ: إشارةٌ مبكِّرةٌ في سجلِّ الخطرِ لا يقيسُها سطرٌ تصيرُ أمرًا يُعادُ
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/surface_debt_trend.py            — أداةٌ جديدةٌ، مسارٌ لم يُحجَزْ قبلَ اليومِ
  tests/governance/test_w061_surface_debt_trend.py  — حرسُها، مسارٌ جديدٌ كذلك
  وما سواهما مُعفًى من الحجزِ بنصِّ § 6: `RISK_REGISTER.md` · `DISCOVERIES.md` · `ACTIVE_WORK.md` ·
  `COMPLETION_LEDGER.md` · `TRUTH_MATRIX.md` و`truth_matrix.json` (مُعادَا التوليدِ) · وسطرُ «آخرِ قيدٍ»
  في `PROJECT_STATE.md` و`docs/PROJECT_HANDBOOK.md` وحدَه — لأنَّ إضافةَ قيدٍ إلى § 8 تُشعِلُ
  `state_document_drift.py` بـ`STATE_DOC_BEHIND`، فتحديثُهما لازمُ القيدِ لا توسيعُ نطاقٍ
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - § 7 من سجلِّ الإكمالِ يقصُرُ العملَ التاليَ على أحدِ اثنَينِ: قرارٌ سياديٌّ (بيدِ المالكِ لا بيدِ
    منفِّذٍ)، أو **بندٌ لا يحتاجُ قرارًا سياديًّا**؛ وهذا الثاني
  - ووجهتُه **مكتوبةٌ قبلَ اليومِ لا مُخترَعةٌ الآنَ**: خليّةُ `RK-003` نفسُها نصَّت على أنَّ بناءَ قياسِ
    اتِّجاهِ العدِّ «**بندٌ تالٍ في `tooling-gates`**»، وحالةُ `DISC-020` نصَّت على أنَّ هذا الصفَّ وحدَه
    بقيَ بلا مِرساةٍ لأنَّ قياسَ إشارتِه غيرُ موجودٍ في الشجرةِ
  - و§ 12 من الخارطةِ يُدرِجُ «اتِّجاهَ الدَّينِ صعودًا أو هبوطًا» مؤشِّرًا دوريًّا — ولم تكن في الشجرةِ
    أداةٌ تُنتِجُه، فكانَ المؤشِّرُ يُقرأُ بالعينِ لا يُقاسُ
  - ولا يلزمُه قرارٌ سياديٌّ ولا سرٌّ ولا شبكةٌ ولا حسابُ Actions — فلا يقعُ تحتَ عائقٍ من العوائقِ المفتوحةِ
خارجَ النطاق:
  - **لا يُخفَّضُ دَينٌ ولا يُصلَحُ سطحٌ**: هذا البندُ يقيسُ الاتِّجاهَ، وتخفيضُ الدَّينِ نفسِه موقوفٌ على
    `Q-33`/`Q-35`/`Q-38`/`Q-39` — قياسُ الاتِّجاهِ ليس ادِّعاءَ إصلاحٍ
  - **لا تُمَسُّ أداةُ الجردِ** `tools/audit/sovereign_write_inventory.py`: تُقرأُ قاعدةً وتُستدعى، ولا
    يُعدَّلُ فيها سطرٌ — والدليلُ `git status`
  - لا يُنشَرُ حِملُ قياسٍ تحتَ `docs/audit/measurements/` (`DISC-014`)، ولا يُمَسُّ `.github/` (`DISC-006`)
  - لا يُعدَّلُ نصُّ الخارطةِ ولا `OWNERSHIP.md` ولا يُضافُ صفُّ قرارٍ `Q-###`
  - لا يُمَسُّ ملفٌّ محجوزٌ لبندٍ مفتوحٍ، ولا يُعدَّلُ `open_record_accountability.py` (محجوزٌ لـ`WI-014`)
  - لا تُغلَقُ بنودٌ مدموجةٌ ولا تُنقَلُ حالةٌ إلى `VERIFIED`، ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ
  - **ولا يُدَّعى حكمُ CI**: أحكامُ Actions غيرُ مقروءةٍ (`DISC-006`) فلا يُقالُ خُضرةً ولا حُمرةً
معيارُ القبول:
   1. أمرٌ واحدٌ يُنتِجُ اتِّجاهَ دَينِ الأسطحِ بينَ أحدثِ قيدَينِ في § 8، ويُعيدُه مرّتَينِ فيُنتِجُ عينَه
   2. اللقطتانِ تُقاسانِ **بقاعدةِ الشجرةِ الحاضرةِ** لا بقاعدةِ كلِّ لقطةٍ في زمنِها — وإلّا كانَ المُعلَنُ
      فارقَ أداتَينِ لا فارقَ دَينٍ، وهذا حدٌّ مكتوبٌ في ترويسةِ الأداةِ ومحروسٌ بفحصٍ
   3. القيدُ يُنسَبُ إلى **أوّلِ** التزامٍ أدخلَ صفَّه في § 8، لا إلى آخرِ من مسَّ معرِّفَه
   4. صعودُ الدَّينِ بينَ قيدَينِ **يُسقِطُ** الأداةَ بمخالفةٍ مُسمّاةٍ، وهبوطُه يمرُّ، وثباتُه يُعلَنُ صافيًا
   5. ما لا يُقاسُ **يُرفَضُ باسمِه**: غيابُ سجلٍّ · غيابُ تاريخٍ · فشلُ `git` · نقطةٌ واحدةٌ · قاعدةٌ لا
      تُحمَّلُ — كلٌّ منها خروجٌ 2 بجنسٍ مُصنَّفٍ، ولا يُقالُ «لا صعودَ» عمّا لم يُقَسْ
   6. الأداةُ **لا تكتبُ سطرًا** في شجرةٍ تحكمُ عليها — والدليلُ فحصٌ يقارنُ `git status` قبلَها وبعدَها
   7. كلُّ دعوى حرسٍ في هذا البندِ **مُجرَّبةٌ بطفرةٍ** في نسخةٍ معزولةٍ، ويُكتَبُ عددُ الفحوصِ الساقطةِ
   8. العدَّادُ `open_record_accountability.py` بعدَ الإرساءِ يُعلِنُ **صِفرَ صفوفٍ بلا مِرساةٍ** ويخرُجُ بـ0
الدليلُ المطلوب:
  python tools/governance/surface_debt_trend.py                          # خروجٌ 0 · نقطتانِ · دَينٌ 182 → 182 · صافي +0
  python tools/governance/surface_debt_trend.py --entries 4              # نافذةٌ أوسعُ · W-057…W-060 · لا صعودَ
  python tools/governance/surface_debt_trend.py --json                   # الحِملُ نفسُه رقمًا رقمًا
  pytest tests/governance/test_w061_surface_debt_trend.py -q             # حرسُ الأداةِ
  python tools/governance/open_record_accountability.py                   # خروجٌ 0 · 40 صفًّا · 30 مفتوحًا · 14 محروسًا · 16 بيدِ المالكِ · 0 بلا مِرساةٍ
  pytest tests/ -q                                                       # الانحدارُ كاملًا
  python tools/governance/check_work_governance.py --staged               # صفرُ مخالفاتٍ
  python tools/governance/check_completion_ledger.py --staged             # صفرُ مخالفاتٍ
  python tools/governance/state_document_drift.py                        # صفرُ انحرافٍ
بدأ: 2026-08-29        ينتهي الحجز: 2026-09-05
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-061` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  هذا البندُ يُثبِتُ أنَّ **اتِّجاهَ** دَينِ الأسطحِ صارَ رقمًا يُعادُ، وأنَّ صعودَه يُسقِطُ. **ولا يُثبِتُ**
  أنَّ العدَّ نفسَه صحيحٌ — صحّةُ الجردِ مسؤوليّةُ `tools/audit/sovereign_write_inventory.py` وحدودُه
  مُعلَنةٌ في ترويستِه. **ولا يُثبِتُ** أنَّ الدَّينَ يهبطُ: القياسُ اليومَ ثابتٌ عندَ 182 موضعًا، والهبوطُ
  عملٌ آخرُ موقوفٌ على قراراتٍ سياديّةٍ مفتوحةٍ. **ولا يقيسُ** ما بينَ القيودِ من التزاماتٍ وسطى، بل
  اتِّجاهًا بينَ نقاطِ القيودِ — وهذا حدٌّ مقصودٌ: القيدُ وحدةُ المساءلةِ في هذا المستودعِ.
```

---

### WI-015 — دعوى الحرسِ تُثبَتُ بطفرةٍ لا تُكتَبُ: إرساءُ القيودِ المفتوحةِ صفًّا صفًّا

```text
النطاق: governance-docs
المسار/المرحلة: T0 — قابليّةُ القياسِ: تحويلُ عدَّادٍ يُشعِلُ (`W-059`) إلى قيودٍ مُرسَاةٍ بأدلّةٍ مُجرَّبةٍ
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات: — لا مسارَ يُحجَزُ في هذا البندِ
  فكلُّ ما يُمَسُّ **مُعفًى من الحجزِ** بنصِّ § 6 من الخارطةِ: يُمَسُّ ولا يُدَّعى مِلكًا، ولا يُقفِلُ نطاقًا
  على غيرِ صاحبِه — ولذلك لا يُزاحَمُ حجزُ `WI-006` على سجلَّي الاكتشافِ والخطرِ (وإعلانُهما مِلكًا كانَ
  سيُشعِلُ `CLAIM_CONFLICT`، وقد قِيسَ ذلك فعلًا في هذه الجلسةِ ثمَّ صُحِّحَ الإعلانُ لا البوّابةُ):
  سجلُّ الخطرِ   — خلايا المِرساةِ لثمانيةِ صفوفٍ: RK-001 · RK-002 · RK-003 · RK-005 · RK-006 · RK-007 · RK-008 · RK-018
  سجلُّ الاكتشافِ — خلايا المِرساةِ لثلاثةِ صفوفٍ: DISC-010 · DISC-015 · DISC-016 · وحالةُ DISC-020 · وقيدُ DISC-021
وملفّاتٌ مُعفاةٌ أخرى تُمَسُّ لأنَّ القيدَ يوجِبُها — مُعلَنٌ لا مطويّ:
  ACTIVE_WORK.md · COMPLETION_LEDGER.md · TRUTH_MATRIX.md و truth_matrix.json (مُعادُ التوليدِ)
  و`PROJECT_STATE.md` · `docs/PROJECT_HANDBOOK.md` — سطرُ «آخرِ قيدٍ» فيهما وحدَه، لأنَّ إضافةَ قيدٍ إلى § 8
  تُشعِلُ `state_document_drift.py` بـ`STATE_DOC_BEHIND`؛ فتحديثُهما لازمُ القيدِ لا توسيعُ نطاقٍ
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - § 7 من سجلِّ الإكمالِ يقصُرُ العملَ التاليَ على أحدِ اثنَينِ: قرارٌ سياديٌّ (بيدِ المالكِ لا بيدِ منفِّذٍ)،
    أو **بندٌ لا يحتاجُ قرارًا سياديًّا**؛ وهذا الثاني، وسببُ اختيارِه **مكتوبٌ قبلَ اليومِ**: وجهةُ
    `DISC-020` و`RK-019` تنُصُّ على أنَّ «إرساءَ الصفوفِ صفًّا صفًّا بندٌ تالٍ في `governance-docs`»
  - والنطاقُ `governance-docs` مُسجَّلٌ في `OWNERSHIP.md`، والملفّانِ المَمسوسانِ **مُعفَيانِ من الحجزِ**
    فلا يزاحِمانِ حجزًا قائمًا ولا يُنتِجانِ `CLAIM_CONFLICT`
  - ولا يلزمُه قرارٌ سياديٌّ ولا سرٌّ ولا شبكةٌ ولا حسابُ Actions — فلا يقعُ تحتَ عائقٍ من العوائقِ المفتوحةِ
  - **وشرطُ الإرساءِ ليس اجتهادًا**: `DISC-020` كتبَ حرفًا أنَّ الحرسَ لا يُذكَرُ إلّا «بعدَ التحقُّقِ من
    أنَّه يسقُطُ فعلًا عندَ عودةِ العَطبِ» — فهذا البندُ يُنفِّذُ شرطَه لا يُخفِّفُه
خارجَ النطاق:
  - **لا يُبنى قياسٌ جديدٌ**: `RK-003` إشارتُه «اتِّجاهُ عدِّ الأسطحِ بينَ قيدَينِ» لا يقيسُها سطرٌ في
    الشجرةِ، وبناءُ ذلك القياسِ بندٌ في `tooling-gates` — فيبقى الصفُّ **مخالفةً ظاهرةً عن قصدٍ**
  - **لا يُخترَعُ تاريخُ استحقاقٍ لقيدٍ بيدِ المالكِ**: `DISC-015` · `DISC-016` · `DISC-021` · `RK-005` ·
    `RK-006` أُرسِيَت بإعلانِ أنَّها بيدِ من يُقرِّرُ، لا بموعدٍ يكتبُه منفِّذٌ عن صاحبِ القرارِ
  - **لا تُعدَّلُ الأداةُ ولا حرسُها**: `open_record_accountability.py` محجوزٌ لـ`WI-014` وهو `IN_REVIEW`،
    فتعديلُه اليومَ `CLAIM_CONFLICT` — ولذلك قُيِّدَ عَطبُه (`DISC-021`) ولم يُصلَحْ
  - لا يُلمَسُ ملفٌّ محجوزٌ لبندٍ مفتوحٍ: البوّاباتُ المذكورةُ مِرساةً **تُقرأُ وتُجرَّبُ في نسخةٍ معزولةٍ**
    تحتَ `/tmp` ولا تُعدَّلُ في الشجرةِ — والدليلُ: `git status` بعدَ التحقُّقِ لا يذكرُ منها ملفًّا
  - لا يُنشَرُ حِملُ قياسٍ تحتَ `docs/audit/measurements/` (`DISC-014`)، ولا يُمَسُّ `.github/` (`DISC-006`)
  - لا يُعدَّلُ نصُّ الخارطةِ ولا `OWNERSHIP.md` ولا يُضافُ صفُّ قرارٍ `Q-###`
  - لا تُغلَقُ بنودٌ مدموجةٌ ولا تُنقَلُ حالةٌ إلى `VERIFIED`، ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ
معيارُ القبول:
   1. كلُّ صفٍّ يُرسَى بحرسٍ **يُذكَرُ مسارُ ملفٍّ موجودٍ** في خلايا مِرساتِه المُعلَنةِ — لا في نثرٍ خارجَها
   2. ولا يُذكَرُ حرسٌ إلّا بعدَ **طفرةٍ مقيسةٍ**: تُعادُ العَطبُ في نسخةٍ معزولةٍ فيسقُطُ فحصٌ واحدٌ على
      الأقلِّ، ويُكتَبُ عددُ الساقطِ في خليّةِ المِرساةِ — دعوى بلا رقمٍ ليست دليلًا
   3. حرسٌ لا تُسقِطُه طفرتُه **لا يُذكَرُ مِرساةً**، ولو حملَ اسمَ العَطبِ في اسمِ ملفِّه
   4. وحدُّ كلِّ حرسٍ جزئيٍّ **مُعلَنٌ في الخليّةِ نفسِها** (ما يحرسُه وما لا يحرسُه)، لا في حاشيةٍ
   5. صفٌّ لا حرسَ له ولا هو بيدِ المالكِ **يبقى مخالفةً** ولا يُلبَسُ مِرساةً بصياغةٍ
   6. صفٌّ بيدِ من يُقرِّرُ يُعلَنُ كذلك **بسببٍ مقيسٍ** (حجزٌ لا يُرفَعُ · حكمٌ غيرُ مقروءٍ · قرارٌ معلَّقٌ)
   7. لا تُمَسُّ خليّةٌ ليست خليّةَ مِرساةٍ: التحريرُ بخليّةٍ مُرقَّمةٍ لا بسطرٍ كاملٍ
   8. العدَّادُ بعدَ الإرساءِ يُعلِنُ **14 محروسًا · 16 بيدِ المالكِ · صفًّا واحدًا بلا مِرساةٍ**، ويخرُجُ بـ1
   9. ولا يُخضَّرُ العدَّادُ بحيلةٍ: أوّلُ صياغةٍ أخضرَتْه كذبًا فقُيِّدَت (`DISC-021`) وصُحِّحَت لا سُتِرَت
  10. الرقمُ يُعادُ بأمرٍ واحدٍ مرّتَينِ فيُنتِجُ عينَه — شرطُ خروجِ T0
الدليلُ المطلوب:
  python tools/governance/open_record_accountability.py                 # خروجٌ 1 · 40 صفًّا · 31 مفتوحًا · 14 محروسًا · 0 باستحقاقٍ · 16 بيدِ المالكِ · 1 بلا مِرساةٍ
  python tools/governance/open_record_accountability.py --json          # الحِملُ نفسُه رقمًا رقمًا
  pytest tests/governance/test_w059_open_record_accountability.py -q    # حرسُ العدَّادِ لم يُمَسَّ
  pytest tests/ -q                                                     # الانحدارُ كاملًا
  python tools/governance/check_work_governance.py --staged             # صفرُ مخالفاتٍ
  python tools/governance/check_completion_ledger.py --staged           # صفرُ مخالفاتٍ
  python tools/governance/state_document_drift.py                       # صفرُ انحرافٍ
بدأ: 2026-08-28        ينتهي الحجز: 2026-09-04
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-060` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  هذا البندُ يُثبِتُ أنَّ عشرةَ قيودٍ صارَت مُرسَاةً بأدلّةٍ **جُرِّبَت** لا بدعوى تُقرأُ. **ولا يُثبِتُ أنَّ
  القيودَ كلَّها مُرسَاةٌ**: العدَّادُ يخرُجُ بـ1 عن حقٍّ (`RK-003`). **ولا يُثبِتُ أنَّ المِرساةَ لا تُكذَبُ**:
  التحقُّقُ بالطفرةِ جرى بيدٍ ولم يُصِرْ أداةً في الشجرةِ، ومُصنِّفُ المِرساةِ نفسُه يُخدَعُ بمسارٍ يُذكَرُ
  دليلَ نفيٍ (`DISC-021`) وإحكامُه محجوزٌ لـ`WI-014` وموقوفٌ على `A-2`. وليس فيه ربطٌ بـCI (`DISC-006`)
  ولا نشرُ حِملٍ (`DISC-014`) ولا دعوى `PROVEN` لأيِّ سطحٍ.
```

---

### WI-014 — القيدُ المفتوحُ يصيرُ مُساءَلًا: لكلِّ قيدٍ حرسٌ أو استحقاقٌ أو إعلانُ يدٍ تُقرِّرُ

```text
النطاق: tooling-gates
المسار/المرحلة: T0 — قابليّةُ القياسِ: تحويلُ قاعدةٍ مكتوبةٍ (`DISC-018`) إلى عدَّادٍ يُشعِلُ حينَ تُخرَقُ
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/open_record_accountability.py            (الأداةُ: تقرأُ `DISCOVERIES.md § 1` و`RISK_REGISTER.md § 1` وتُصنِّفُ مِرساةَ كلِّ صفٍّ مفتوحٍ — حرسٌ قائمٌ أو استحقاقٌ أو يدُ المالكِ — ولا تكتبُ شيئًا)
  tests/governance/test_w059_open_record_accountability.py  (حرسُ الحرسِ: 39 فحصًا · لكلِّ مخالفةٍ اشتعالٌ وسكوتٌ · ولكلِّ رفضٍ مُصنَّفٍ فحصٌ · وطفرتانِ مقصودتانِ تُثبِتانِ أنَّ نزعَ التشكيلِ وحصرَ خلايا المِرساةِ حاملانِ لا زينةٌ)
وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ:
  ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md
  و`PROJECT_STATE.md` · `docs/PROJECT_HANDBOOK.md` — سطرُ «آخرِ قيدٍ» فيهما وحدَه، لأنَّ إضافةَ قيدٍ إلى § 8
  تُشعِلُ `state_document_drift.py` بـ`STATE_DOC_BEHIND`؛ فتحديثُهما لازمُ القيدِ لا توسيعُ نطاقٍ
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - § 7 من سجلِّ الإكمالِ يقصُرُ العملَ التاليَ على أحدِ اثنَينِ: قرارٌ سياديٌّ (وذاك بيدِ المالكِ لا بيدِ
    منفِّذٍ)، أو **بندٌ لا يحتاجُ قرارًا سياديًّا**؛ وهذا الثاني، وسببُ اختيارِه **مكتوبٌ قبلَ اليومِ**:
    وجهةُ `DISC-018` تنُصُّ حرفًا: «وتعميمُ القاعدةِ (لكلِّ قيدٍ حرسٌ أو تاريخُ استحقاقٍ) بندٌ تالٍ»
  - وهو أسبقُ ما بقيَ من الوجهاتِ المكتوبةِ: بقيّةُ الاكتشافاتِ المفتوحةِ إمّا بيدِ المالكِ
    (`DISC-008` · `DISC-009` · `DISC-012` · `DISC-014` · `DISC-017`) وإمّا محلُّها ملفٌّ محجوزٌ لبندٍ
    `IN_REVIEW` (`DISC-015` · `DISC-016`) — فالعملُ فيها إمّا انتحالُ قرارٍ وإمّا `CLAIM_CONFLICT`
  - ولا يلزمُه قرارٌ سياديٌّ ولا سرٌّ ولا شبكةٌ ولا حسابُ Actions — فلا يقعُ تحتَ عائقٍ من العوائقِ المفتوحةِ
  - والنطاقُ `tooling-gates` مُسجَّلٌ في `OWNERSHIP.md`، والملفُّ **جديدٌ** فلا يزاحِمُ حجزًا قائمًا
  - وانحرافٌ مُعلَنٌ لا مطويّ: وجهةُ `DISC-018` تقولُ «في نطاقِ `governance-docs`»، ونُفِّذَ في
    `tooling-gates` عن قصدٍ — لأنَّ § 3 من الخارطةِ يمنعُ القاعدةَ التي لا يقيسُها شيءٌ، فكتابةُ القاعدةِ
    نصًّا في وثيقةٍ تُعيدُ عينَ العطبِ الذي قيَّدَه `DISC-018`. والسجلّاتُ المُعفاةُ وحدَها ما مُسَّ من `governance-docs`
خارجَ النطاق:
  - **لا تُرسَى الصفوفُ صفًّا صفًّا في هذا البندِ**: كتابةُ «حرسُ هذا الصفِّ هو كذا» دعوى تلزمُها
    تجربةٌ لكلِّ صفٍّ على حِدةٍ (أنَّ الحرسَ يسقُطُ فعلًا عندَ عودةِ العطبِ)، فقُيِّدَت بندًا تاليًا في `DISC-020`
  - **لا يُخترَعُ تاريخُ استحقاقٍ لقيدٍ بيدِ المالكِ**: تحديدُ موعدٍ لقرارٍ سياديٍّ فعلُ صاحبِ القرارِ،
    وموقوفٌ على `A-2`/`A-3` (`DISC-012` · `RK-004`) — فالأداةُ تُبلِغُ عن هذه الصفوفِ ولا تُسقِطُ بها
  - لا يُلمَسُ ملفٌّ محجوزٌ لبندٍ مفتوحٍ: لا `check_work_governance.py` ولا `measurement_provenance.py`
    ولا `state_document_drift.py` ولا `sovereign_decision_status.py` ولا فحوصُ `w051`…`w058`
  - لا يُنشَرُ حِملُ قياسٍ تحتَ `docs/audit/measurements/`: ذاك يوجِبُ قيدَ نَسَبٍ في ملفٍّ محجوزٍ (`DISC-014`)
  - لا يُمَسُّ `.github/`: أحكامُ CI غيرُ مقروءةٍ (`DISC-006`)، وربطُ بوّابةٍ جديدةٍ بها دعوى لا تُقاسُ
  - لا يُعدَّلُ نصُّ الخارطةِ ولا `OWNERSHIP.md` ولا يُضافُ صفُّ قرارٍ `Q-###`
  - لا تُغلَقُ بنودٌ مدموجةٌ ولا تُنقَلُ حالةٌ إلى `VERIFIED`، ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ
معيارُ القبول:
   1. الأداةُ تقرأُ السجلَّينِ بعنوانِ القسمِ لا برقمِ سطرٍ، وتُطابِقُ العنوانَ **بلا تشكيلٍ** فلا تنكسِرُ بحركةٍ
   2. مِرساةُ الصفِّ تُقرأُ من **خلاياها المُعلَنةِ** وحدَها: الوجهةُ والحالةُ للاكتشافِ، والإشارةُ والتصرُّفُ
      والمالكُ والمصدرُ للخطرِ — فملفٌّ يُذكَرُ في خليّةِ الدليلِ موضِعَ عطبٍ **ليس حرسًا له**
   3. حرسٌ مذكورٌ لا وجودَ لملفِّه يُسمّى `DEAD_ANCHOR` ولا يُعَدُّ مِرساةً — ويُقاسُ في المُغلَقِ أيضًا
   4. تاريخُ استحقاقٍ مضى يُسمّى `DUE_DATE_PASSED`؛ وتاريخُ اليومِ نفسِه لا يُعَدُّ ماضيًا
   5. صفٌّ مفتوحٌ بلا مِرساةٍ يُسمّى `OPEN_RECORD_WITHOUT_ANCHOR` — وهو ما يُسقِطُ التشغيلَ
   6. صفٌّ مُعلَنٌ بيدِ المالكِ **يُبلَغُ عنه ولا يُسقِطُ**: ملاحظةُ `OWNER_HELD_WITHOUT_GUARD` تُكتَبُ ولا تُبتلَعُ
   7. خطرٌ بلا إشارةٍ مبكِّرةٍ مكتوبةٍ يُسمّى `RISK_SIGNAL_EMPTY` — فلا خطرَ بلا ما يُقاسُ
   8. صفٌّ ناقصُ الخلايا يُسمّى `MALFORMED_ROW` ولا يُبتلَعُ صامتًا
   9. الانفتاحُ يُقرأُ من نصِّ خليّةِ الحالةِ لا من ظنٍّ: «مُعالَجٌ … والشِّقُّ الثاني مفتوحٌ» مفتوحٌ،
      وحالةٌ فارغةٌ أو بمفرداتٍ غيرِ مُعلَنةٍ تُقرأُ **مفتوحةً** — لا يُستنبَطُ إغلاقٌ من نصٍّ حرٍّ
  10. عجزُ القياسِ رفضٌ مُصنَّفٌ لا نتيجةٌ خالية: `SOURCE_MISSING` · `SECTION_MISSING` · `NO_ROWS`، خروجٌ 2
  11. الأداةُ **لا تكتبُ في ما تحكمُ عليه** — مقيسٌ بمقارنةِ بايتاتِ السجلَّينِ قبلَ التشغيلِ وبعدَه
  12. طفرتانِ مقصودتانِ تُقاسُ فرقُهما ولا يُعدَّلُ الحرسُ لإثباتِهما: مدًى واسعٌ لنزعِ التشكيلِ يبتلعُ
      الأبجديّةَ فيُقرأُ المُعالَجُ مفتوحًا؛ وقراءةُ المِرساةِ من الصفِّ كلِّهِ تجعلُ موضِعَ العطبِ حرسَه
  13. الرقمُ يُعادُ بأمرٍ واحدٍ مرّتَينِ فيُنتِجُ عينَه — شرطُ خروجِ T0
الدليلُ المطلوب:
  python tools/governance/open_record_accountability.py                                  # خروجٌ 1 · 39 صفًّا · 30 مفتوحًا · 8 محروسًا · 0 باستحقاقٍ · 11 بيدِ المالكِ · 11 بلا مِرساةٍ
  python tools/governance/open_record_accountability.py --json                           # الحِملُ نفسُه رقمًا رقمًا
  pytest tests/governance/test_w059_open_record_accountability.py -q                     # 39 passed
  pytest tests/ -q                                                                       # الانحدارُ كاملًا
  ruff check tools/governance/open_record_accountability.py tests/governance/test_w059_open_record_accountability.py
بدأ: 2026-08-28        ينتهي الحجز: 2026-09-04
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-059` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  هذا البندُ يُثبِتُ أنَّ قاعدةَ `DISC-018` صارَ لها عدَّادٌ يُشعِلُ حينَ تُخرَقُ، وأنَّ الخرقَ **مقيسٌ الآنَ
  بأحدَ عشرَ صفًّا** لا موصوفٌ. **ولا يُثبِتُ أنَّ القيودَ أُرسِيَت**: الأداةُ تخرُجُ بـ1 على المستودعِ الحاضرِ
  عن حقٍّ، وإرساءُ الصفوفِ صفًّا صفًّا بندٌ تالٍ (`DISC-020` · `RK-019`)، وما كانَ بيدِ المالكِ يبقى بيدِه.
  وليس في هذا البندِ ربطٌ بـCI (‏`DISC-006`) ولا نشرُ حِملٍ (‏`DISC-014`) ولا دعوى `PROVEN` لأيِّ سطحٍ.
```

---

### WI-013 — حرسُ نجاةِ الحالةِ يكفُّ عن الشهادةِ زورًا على الإدامةِ حينَ تنقُصُ البيئةُ

```text
النطاق: tests-root
المسار/المرحلة: T0 — صدقُ الحرسِ: أن لا يُنسَبَ عجزُ بيئةٍ إلى الحالةِ، وأن يبقى القياسُ مقيسًا لا مفترَضًا
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tests/governance/test_step18_restart_survival.py        (الإصلاحُ: شرطٌ مقيسٌ من مُخرَجِ المِسبارِ — `_missing_third_party_module` · `_skip_if_the_environment_is_incomplete` — يُستشارُ في الفحصَينِ الحيَّينِ)
  tests/governance/test_w058_live_stack_precondition.py   (حرسُ الحرسِ: 12 فحصًا · يقيسُ ما يُبتلَعُ وما لا يُبتلَعُ · وطفرةٌ مقصودةٌ تُثبِتُ أنَّ فحصَ الشجرةِ يعضُّ · ودليلٌ أخيرٌ يُشغِّلُ الفحصَينِ في عمليّةٍ)
وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ:
  ACTIVE_WORK.md · DISCOVERIES.md · COMPLETION_LEDGER.md · PROJECT_STATE.md · docs/PROJECT_HANDBOOK.md · docs/audit/ACTIVE_EXECUTION_STATE.md
  و`docs/audit/TRUTH_MATRIX.md` · `docs/audit/truth_matrix.json` — يُعادُ توليدُهما بأمرِ التحقُّقِ نفسِه، لا يُحرَّرانِ بيدٍ
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - لم يُختَرْ هذا البندُ من § 6 اختيارًا: **قِيسَ اليومَ** بتشغيلِ `pytest tests/ -q` على `70a4081`، فسقطَ فحصانِ
    حيّانِ برسالتَينِ تنسِبانِ السقوطَ إلى **إدامةِ الحالةِ** («الكنارُ نجا خلافًا للتصريحِ» · «سجلُّ الذرّيّةِ لم
    يُكتَبْ في موضعِ القياسِ — فالتوجيهُ مُعطَّلٌ»)، والسببُ الحقيقيُّ وحدةٌ غائبةٌ: `No module named 'jwt'`
  - وذاك بعينِه **الكذبُ المُوثَّقُ المعكوسُ** الذي تُعلِنُ ترويسةُ الملفِّ نفسِه (§ الهدف · الصورةُ الثالثةُ)
    أنَّها أُنشِئَت لمنعِه — فالعطبُ في الحرسِ لا في المحروسِ، ومن جنسِ `RK-010` و`RK-013` و`DISC-009`
  - وحكمٌ أحمرُ كاذبٌ يُفسِدُ كلَّ قراءةٍ تالِيَةٍ للحالةِ: يُوهِمُ فقدَ إدامةٍ خِلافَ `Q-39 (أ)` ويُوهِمُ تلويثَ
    الشجرةِ — فتصحيحُه أسبقُ من أيِّ بندٍ جديدٍ في ترتيبِ الأولويّاتِ (صدقُ القياسِ قبلَ توسيعِه)
  - ولا يلزمُه قرارٌ سياديٌّ ولا سرٌّ ولا شبكةٌ ولا حسابُ Actions — فلا يقعُ تحتَ شيءٍ من العوائقِ المفتوحةِ
  - والنطاقُ `tests-root` مُسجَّلٌ في `OWNERSHIP.md` (‏`tests` · `C0`)، والملفُّ **غيرُ محجوزٍ** لأيِّ بندٍ مفتوحٍ:
    `WI-003` الذي حجزَ `restart_survival_probe.py` مُغلَقٌ — فلا `CLAIM_CONFLICT`
خارجَ النطاق:
  - لا يُلمَسُ `tools/governance/restart_survival_probe.py`: المِسبارُ يقيسُ صحيحًا ويُخرِجُ `UNMEASURED` صادقًا،
    والعطبُ في **قراءةِ** مُخرَجِه لا في إنتاجِه — وتغييرُ المقيسِ لإرضاءِ قارئِه عكسُ الترتيبِ
  - لا تُثبَّتُ تبعيّاتُ الطبقةِ الفدراليّةِ ولا يُصلَحُ إعلانُها: ذاك `DISC-009` و`issue #22`، وقرارُه ثلاثيُّ
    الوجهِ ينتظرُ المالكَ — وهذا البندُ يُسمِّي النقصَ ولا يُخفيه ولا يدَّعي إصلاحَه
  - لا يُوسَّعُ `LIVE_STACK_MODULES` بـ`amos_federation`: المِسبارُ يحقِنُ `federal/executive/services/src` في
    `PYTHONPATH` لكلِّ مرحلةٍ ولا يضعُه في `sys.path` للعمليّةِ الأمِّ، فـ`find_spec` يعودُ `None` ولو كانَ
    القياسُ مُستطاعًا — فيصيرُ الفحصانِ متخطَّيَينِ **دائمًا** في كلِّ بيئةٍ، وذاك إخفاءٌ لا إصلاحٌ
  - لا يُحذَفُ فحصٌ ولا يُضعَفُ تأكيدٌ ولا يُبدَّلُ معيارُ قبولٍ: عددُ التأكيداتِ لم ينقُصْ، وإنّما أُضيفَ
    **شرطٌ سابقٌ** يُميِّزُ «لم يُقَسْ» من «قِيسَ فخالفَ»
  - لا يُدَّعى أنَّ الإدامةَ مقيسةٌ في هذه البيئةِ: الفحصانِ **مُتخطَّيانِ** هنا بنصٍّ يُسمِّي الناقصَ، والقياسُ
    الكاملُ محلُّه `.github/workflows/measure.yml` — وأحكامُ CI **غيرُ مقروءةٍ** بقياسِ أداةِ `W-051`
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/ · ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ
معيارُ القبول:
  1. شرطُ القياسِ الحيِّ يُقرَأُ **من مُخرَجِ المِسبارِ** (`verdict` · `detail`) لا من قائمةِ وحداتٍ مكتوبةٍ بيدٍ
  2. نقصُ توزيعٍ خارجيٍّ (‏`jwt` · `structlog` · `pydantic_settings`) **يُتخطَّى باسمِه المقيسِ** ولا يُنسَبُ إلى الحالةِ
  3. نقصُ وحدةٍ من شجرةِ المستودعِ (يُحَلُّ اسمُها الأعلى تحتَ `federal/executive/services/src`) **يبقى أحمرَ**
  4. عجزٌ ليس `No module named` (‏مهلةٌ · رمزُ خروجٍ · قاعدةٌ مقفولةٌ · نصٌّ فارغٌ) **يبقى أحمرَ**
  5. حكمٌ غيرُ `UNMEASURED` لا يُنظَرُ فيه أصلًا — فـ`CONTRADICTS_DECLARATION` لا تُخفى بهذا البابِ ولو حملَ نصُّها ما يُشبِهُ عجزَ بيئةٍ
  6. الشرطُ الرخيصُ اليدويُّ (`_require_live_stack`) يبقى مُقدَّمًا: يوفِّرُ الدقائقَ حينَ تغيبُ الطبقةُ كلُّها
  7. حضورُ الاستدعاءِ في **جسمِ** كلِّ فحصٍ حيٍّ مقيسٌ نصًّا — فحرسٌ يُحذَفُ صامتًا يُسقِطُ حرسَ الحرسِ
  8. الفحصانِ الحيّانِ في هذه البيئةِ **يمرّانِ أو يُتخطَّيانِ ولا يسقُطانِ** — مقيسٌ بتشغيلِهما في عمليّةٍ لا بدعوى
  9. طفرةٌ مقصودةٌ تُثبِتُ أنَّ فحصَ الشجرةِ حاملٌ لا زينةٌ: بإضعافِه يُبتلَعُ نقصُ شِفرةِ المستودعِ — أُعيدَ بناءُ النسخةِ المُضعَفةِ في الفحصِ وقِيسَ فرقُها، ولم يُعدَّلِ الحرسُ ليُثبَتَ ذلك
 10. حالةُ الشجرةِ لم تتغيَّرْ خارجَ المسارَينِ: `ruff check` على الملفَّينِ عندَ خطِّ الأساسِ نفسِه (‏مخالفتانِ قديمتانِ من `PLE2502` لا ثالثةَ لهما)
الدليلُ المطلوب:
  pytest tests/governance/test_w058_live_stack_precondition.py -q                      # 12 passed
  pytest tests/governance/test_step18_restart_survival.py -q -rs                       # 16 passed · 2 skipped — ونصُّ التخطِّي يُسمِّي `jwt`
  pytest tests/ -q                                                                     # الانحدارُ كاملًا · وسقوطُ الحرسَينِ زالَ
  ruff check tests/governance/test_step18_restart_survival.py tests/governance/test_w058_live_stack_precondition.py
بدأ: 2026-08-27        ينتهي الحجز: 2026-09-03
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-058` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  هذا البندُ يُثبِتُ أنَّ سقوطَ الحرسِ لن يُنسَبَ بعدَ اليومِ إلى إدامةِ الحالةِ حينَ يكونُ سببُه وحدةً غائبةً،
  وأنَّ الحدَّ بينَ «بيئةٌ ناقصةٌ» و«شِفرةٌ مفقودةٌ» مقيسٌ ومحروسٌ بطفرةٍ. **ولا يُثبِتُ أنَّ الحالةَ تنجو
  إعادةَ التشغيلِ**: ذاك قياسٌ لم يُجرَ هنا لنقصِ البيئةِ، ويبقى موقوفًا على بيئةٍ كاملةٍ (`bootstrap.sh`)
  أو على حسمِ `DISC-009`، وعلى حسابِ Actions المُعطَّلِ (`DISC-006`) ليُقرأَ حكمُ `measure.yml`. وليس فيه
  إصلاحٌ لتبعيّاتٍ ولا دعوى `PROVEN` لأيِّ سطحٍ. ومحلُّ خطرِه المكتوبُ `DISC-019`.
```

---

### WI-012 — موضعُ المشروعِ في وثائقِ حالتِه يصيرُ مقيسًا مقابلَ سجلِّه، لا محفوظًا بيدٍ

```text
النطاق: audit-truth
المسار/المرحلة: T0 — شرطُ الخروجِ «أن يُنتِجَ أيُّ عاملٍ الرقمَ نفسَه بأمرٍ واحدٍ»، مُنزَّلًا على وثائقِ الحالةِ
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/state_document_drift.py                (الأداةُ: تقرأُ § 8 نصًّا · تقيسُ أحدثَ قيدٍ تذكرُه كلُّ وثيقةِ حالةٍ · تعدُّ التأخُّرَ · ترفضُ مُصنَّفًا)
  tests/governance/test_w057_state_document_drift.py      (حرسُ المعيارِ: 39 فحصًا · سبعُ طفراتٍ مقصودةٍ عضَّت منها ستٌّ ثمَّ رُدَّت · والسابعةُ مكافئةٌ تُعلَنُ لا تُطوى)
  PROJECT_STATE.md                                       (تصحيحُ الانحرافِ المقيسِ: 9 قيودٍ تأخُّرًا → صِفرٌ)
  docs/PROJECT_HANDBOOK.md                               (تصحيحُ الانحرافِ المقيسِ: 8 قيودٍ تأخُّرًا → صِفرٌ)
وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ:
  ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md · THE_ROADMAP.md (سطرُ التاريخِ فقط)
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - § 7 (البندُ 10) يقصُرُ ما يُبدَأُ على حسمٍ سياديٍّ أو «بندٍ من § 6 لا يحتاجُ قرارًا» — وقِيسَ اليومَ أنَّ
    ما بقيَ من T3 محجوبٌ نصًّا: `Q-35` يقولُ حرفًا «العدُّ يبقى 2 كما هو ولا يُمَسّ»، و`Q-33` مثلُه للعزلِ
  - و`DISC-013` مفتوحٌ في نطاقِ `audit-truth` ولم يُفتَحْ له بندٌ، ولا يلزمُه قرارٌ ولا سرٌّ ولا شبكةٌ
  - واتّساعُ فارقِه من ستّةٍ إلى تسعةٍ وهو مفتوحٌ دليلٌ أنَّ القيدَ وحدَه لا يُصلِحُ — قِيدَ في `DISC-018`
خارجَ النطاق:
  - لا يُحكَمُ على صدقِ نصِّ الوثيقةِ: الأداةُ تقيسُ أحدثَ قيدٍ تذكرُه ومدى تأخُّرِه، لا صوابَ ما تقولُه عنه
  - لا تُكتَشَفُ وثائقُ الحالةِ اكتشافًا: القائمةُ مُعلَنةٌ في الشِفرةِ — والخطرُ قِيدَ في `RK-018`
  - لا تُصلِحُ الأداةُ وثيقةً تحكمُ عليها: التصحيحُ عملُ يدٍ مُقيَّدٍ، وبوّابةٌ تُصلِحُ محكومَها لا تُثبِتُ شيئًا (سابقةُ `W-037`/`W-038`)
  - لا تُربَطُ الأداةُ ببوّابةٍ ولا بـ`.github/**`: الربطُ يمسُّ `check_work_governance.py` (محجوزٌ لـ`WI-009`) والتفعيلُ عينُ `A-3`
  - لا يُنشَرُ حِملٌ في `docs/audit/measurements/`: قيدُ النَّسَبِ مقفولٌ (`DISC-014`) — فـ`--json` يطبعُ إلى المُخرَجِ القياسيِّ
  - لا يُلمَسُ `measurement_provenance.py` ولا `ci_verdict_readability.py`: محجوزانِ لـ`WI-006`
  - لا يُغلَقُ `WI-006`…`WI-011`: طريقُ الإغلاقِ مقطوعٌ ما دامَ `A-2` معلَّقًا (`DISC-012`)
  - لا تُمَسُّ المخالفتانِ الباقيتانِ من `HARDCODED_TRUTH` ولا `SANDBOX_DISABLED`: محجوبةٌ بـ`Q-35` و`Q-33` نصًّا
  - لا يُدَّعى أنَّ CI أخضرُ ولا أحمرُ: الأحكامُ **غيرُ مقروءةٍ** بقياسِ أداةِ `W-051` (16/16 تراكُمًا)
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/ · ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ
معيارُ القبول:
  1. أحدثُ قيدٍ في § 8 يُقرَأُ **من صفوفِ الجدولِ** لا من فقرةٍ ولا من ذاكرةٍ، وبالعددِ لا بترتيبِ الظهورِ
  2. تأخُّرُ وثيقةِ حالةٍ يُسقِطُ (رمز 1) **بعددِه** (`STATE_DOC_BEHIND`)، وكذا دعوى قيدٍ لا صفَّ له، ووثيقةٌ لا تذكرُ قيدًا، وتاريخٌ غائبٌ أو في المستقبلِ
  3. عجزُ القياسِ **رفضٌ مُصنَّفٌ برمزِ 2**: مصدرٌ غائبٌ · جدولٌ بلا صفوفٍ — ولا يُقالُ «لا انحراف» عن قياسٍ لم يُجرَ
  4. تاريخٌ أقدمُ من تاريخِ أحدثِ قيدٍ **إبلاغٌ لا إسقاطٌ**: قد يكونُ النصُّ صحيحًا وتاريخُه ناقصًا (§ 13.3)
  5. الوثيقتانِ تُصحَّحانِ **بالمقيسِ**: ما بينَ `W-048` و`W-057` يُلخَّصُ بما في § 8، ولا تُخترَعُ حالةٌ ولا يُدَّعى إغلاقٌ لم يقعْ
  6. الأداةُ لا تكتبُ بايتًا في وثيقةٍ تحكمُ عليها — وفحصٌ يُثبِتُه بمقارنةِ النصِّ قبلَ التشغيلِ وبعدَه
  7. فحصٌ يقرأُ المستودعَ الحقيقيَّ **يسقُطُ** إن تُرِكَتِ الوثيقتانِ متأخِّرتَينِ — فالحرسُ يعضُّ عملَ اليومِ لا عملَ غيرِه
  8. الفحوصُ تسقُطُ إن أُضعِفَ الحرسُ — أُثبِتَ بسبعِ طفراتٍ مقصودةٍ: **ستٌّ عضَّت** (توسيعُ التحمُّلِ إلى قيدٍ · تحويلُ الإسقاطِ إبلاغًا · ابتلاعُ جدولٍ بلا صفوفٍ · ابتلاعُ مصدرٍ غائبٍ · تعطيلُ حرسِ التاريخِ المستقبليِّ · تصعيدُ الإبلاغِ إسقاطًا) ثمَّ رُدَّت، **والسابعةُ لم تعضَّ وتُعلَنُ مكافئةً**: ترتيبُ معرِّفٍ ثابتِ العرضِ (`W-###`) نصًّا يُساوي ترتيبَه عددًا، فالفحصُ لا يُفرِّقُ ما لا يختلفُ — ولم يُخترَعْ فحصٌ يوهِمُ عضًّا
الدليلُ المطلوب:
  pytest tests/governance/test_w057_state_document_drift.py -q   # 39 passed
  python tools/governance/state_document_drift.py                # خروجٌ 0 بعدَ التصحيحِ · وكانَ 1 بمخالفتَينِ قبلَه
  python tools/governance/state_document_drift.py --json         # الحِملُ إلى المُخرَجِ القياسيِّ · لا ملفَّ يُكتَبُ
  bash tools/dev/bootstrap.sh --verify                           # الحرسُ كاملًا · والشجرةُ نظيفةٌ بعدَه
بدأ: 2026-08-27        ينتهي الحجز: 2026-09-03
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-057` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  الأداةُ تُثبِتُ أنَّ وثيقتَي الحالةِ تذكرانِ أحدثَ قيدٍ مكتوبٍ في § 8 وأنَّ تاريخَهما مُعلَنٌ غيرُ مستقبليٍّ.
  ولا تُثبِتُ أنَّ وصفَهما لذلكَ القيدِ صادقٌ، ولا ترى وثيقةً تُعلِنُ حالةً ولم تُدرَجْ في القائمةِ المُعلَنةِ،
  ولا تُحصي دعوى حالةٍ في ملفٍّ غيرِ ماركداونَ. وهذه حدودٌ مكتوبةٌ لا مطويّةٌ، ومحلُّ خطرِها `RK-018`.
```

---

### WI-011 — حالةُ القرارِ السياديِّ تصيرُ رقمًا يُقاسُ، لا فقرةً تُروى في ردٍّ

```text
النطاق: audit-truth
المسار/المرحلة: T0 — شرطُ الخروجِ «أن يُنتِجَ أيُّ عاملٍ الرقمَ نفسَه بأمرٍ واحدٍ»، مُنزَّلًا على جدولِ § 16
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/sovereign_decision_status.py                 (الأداةُ: تقرأُ § 16 نصًّا · تقيسُ استقامتَه · تعدُّ ما يتوقَّفُ عليه · ترفضُ مُصنَّفًا)
  tests/governance/test_w056_sovereign_decision_status.py       (حرسُ المعيارِ: 35 فحصًا · أُثبِتَ عضُّها بسبعِ طفراتٍ مقصودةٍ ثمَّ رُدَّت)
وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ:
  ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md · THE_ROADMAP.md (سطرُ التاريخِ فقط)
  و`docs/audit/TRUTH_MATRIX.md` · `docs/audit/truth_matrix.json` — يُعادُ توليدُهما بأمرِ التحقُّقِ نفسِه، لا يُحرَّرانِ بيدٍ
لماذا هذا البندُ الآنَ — سببٌ مُعلَنٌ لا ترتيبٌ مُخترَعٌ:
  - § 7 من السجلِّ (البندُ 10) يقصُرُ ما يُبدَأُ على «قرارٍ سياديٍّ» أو «بندٍ من § 6 لا يحتاجُ قرارًا» — وهذا الثاني:
    لا يلزمُه سرٌّ ولا صلاحيةٌ ولا شبكةٌ، ولا يُفعِّلُ إسقاطًا (فذاك عينُ `A-3`)
  - وطلبُ التوثيقِ الحاضرُ («بقاءُ `A-2` و`A-3`») لا يُؤدّى بفقرةٍ: فقرةٌ تُصدَّقُ بلا إعادةِ إنتاجٍ،
    وأمرٌ واحدٌ يُعيدُ الرقمَ لأيِّ عاملٍ — فالتوثيقُ هنا أداةٌ، والقيدُ نتيجتُها
خارجَ النطاق:
  - لا يُحكَمُ على صوابِ دعوى الحجبِ: الأداةُ تقيسُ **ما هو مكتوبٌ ومن يتوقَّفُ عليه**، لا هل الحجبُ مُبرَّرٌ
  - لا تُعتمَدُ ولا تُرفَضُ `A-2`/`A-3`: قرارُ المالكِ لا يُنتَحَلُ بأداةٍ
  - لا يُكتَبُ في `THE_ROADMAP.md` غيرُ سطرِ التاريخِ: بوّابةٌ تُصلِحُ ما تحكمُ عليه لا تُثبِتُ شيئًا (سابقةُ `W-037`/`W-038`)
  - لا تُربَطُ الأداةُ ببوّابةٍ ولا بـ`.github/**`: الربطُ يمسُّ `check_work_governance.py` (محجوزٌ لـ`WI-009`)، والتفعيلُ عينُ `A-3` — قِيدَ في `DISC-016`
  - لا يُنشَرُ حِملٌ في `docs/audit/measurements/`: قيدُ النَّسَبِ مقفولٌ بـ`WI-006` (`DISC-014`) — فـ`--json` يطبعُ إلى المُخرَجِ القياسيِّ ولا يكتبُ ملفًّا
  - لا يُلمَسُ `tools/governance/measurement_provenance.py` ولا `ci_verdict_readability.py`: محجوزانِ لـ`WI-006`
  - لا يُصحَّحُ نصُّ § 16 المتنافي: حسمٌ سياديٌّ قِيدَ في `DISC-017`
  - لا يُغلَقُ `WI-006`…`WI-010`: طريقُ الإغلاقِ مقطوعٌ ما دامَ `A-2` معلَّقًا (`DISC-012`)
  - لا يُدَّعى أنَّ CI أخضرُ ولا أحمرُ: أحكامُ التشغيلاتِ **غيرُ مقروءةٍ** بقياسِ أداةِ `W-051` (12/12)
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/ · ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ
معيارُ القبول:
  1. حالةُ كلِّ قرارٍ تُقرأُ من جدولِ § 16 **نصًّا** (المعرِّفُ · العنوانُ · التاريخُ · رمزُ الحالةِ) — لا تُكتَبُ في الشِفرةِ ولا تُحفَظُ نسخةً ثانيةً
  2. يُسقِطُ (رمز 1) على ما يُصلِحُه من يُحرِّرُ: حالةٌ غيرُ معجميّةٍ · اعتمادٌ بلا تاريخٍ · تعليقٌ بتاريخٍ · تاريخٌ في المستقبلِ · إشارةٌ إلى `A-#` لا صفَّ له
  3. عجزُ القياسِ **رفضٌ مُصنَّفٌ برمزِ 2** لا حكمٌ: مصدرٌ غائبٌ · قسمٌ غائبٌ · جدولٌ بلا صفوفٍ · حالةُ وثيقةٍ غيرُ مُعلَنةٍ — ولا يُقالُ «لا مخالفة» عن قياسٍ لم يُجرَ
  4. انقضاءُ سندِ وضعِ الإبلاغِ يُطبَعُ مسموعًا ولا يُسقِطُ إلّا بـ`--enforce-basis` صريحًا: الإسقاطُ على ما لا يملِكُ المنفِّذُ حسمَه عقوبةٌ لا حرسٌ (§ 13.3 · سابقةُ `POST_MERGE_NOT_CLOSED` في `W-054`)
  5. عمرُ التعليقِ يُطبَعُ **حدًّا أدنى مُشتَقًّا** مُعلَنًا بلفظِه، لا عمرًا مقيسًا: الجدولُ لا يحملُ تاريخَ طلبِ القرارِ
  6. الأداةُ وفحصُها مُستثنيانِ من عدِّ الإشاراتِ: وصفُ الحجبِ ليس حجبًا، وعادٌّ يعدُّ نفسَه يُنفِّخُ رقمَه (سابقةُ `W-029`)
  7. لا تكتبُ الأداةُ حرفًا في الخارطةِ التي تحكمُ عليها — وفحصٌ يُثبِتُه بمقارنةِ البايتاتِ قبلَ التشغيلِ وبعدَه
  8. عجزُ القياسِ الجزئيُّ يُسمّى ولا يُبتلَعُ: ملفٌّ لم يُقرَأْ يُعلَنُ (`UNREADABLE_SOURCE`) والعدُّ يُوصَفُ ناقصًا بقدرِه، وغيابُ سجلِّ العملِ يُعلَنُ «لم تُقَسْ» (`WORK_REGISTER_UNREAD`) لا «لا بندَ متوقِّفًا»
  9. الفحوصُ تسقُطُ إن أُضعِفَ الحرسُ — أُثبِتَ بسبعِ طفراتٍ مقصودةٍ ثمَّ رُدَّت
الدليلُ المطلوب:
  pytest tests/governance/test_w056_sovereign_decision_status.py -q     # 35 passed
  python tools/governance/sovereign_decision_status.py                  # خروجٌ 0 · A-1 APPROVED 2026-08-26 · A-2 وA-3 PENDING · وإبلاغُ ADVISORY_BASIS_EXPIRED
  python tools/governance/sovereign_decision_status.py --json           # الحِملُ إلى المُخرَجِ القياسيِّ · لا ملفَّ يُكتَبُ
  python tools/governance/sovereign_decision_status.py --enforce-basis  # خروجٌ 1 · الانقضاءُ يصيرُ مُسقِطًا بطلبٍ صريحٍ
  bash tools/dev/bootstrap.sh --verify                                  # الحرسُ كاملًا · والشجرةُ نظيفةٌ بعدَه
بدأ: 2026-08-27        ينتهي الحجز: 2026-09-03
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-056` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  الأداةُ تُثبِتُ أنَّ `A-2` و`A-3` مكتوبانِ `PENDING` وأنَّ 52 و14 موضعًا تُشيرُ إليهما وأنَّ ثلاثةَ بنودٍ
  (`WI-006` · `WI-007` · `WI-008`) تُعلِنُ توقُّفَها على `A-2`. ولا تُثبِتُ أنَّ التوقُّفَ مُستحَقٌّ، ولا تُحصي
  عملًا توقَّفَ بلا أن يُعلِنَ توقُّفَه في صفِّه — فما لا يُكتَبُ لا يُعَدُّ. وعمرُ التعليقِ حدٌّ أدنى لا قياسٌ.
  وبقاءُ `A-2`/`A-3` معلَّقَينِ ليسَ عيبًا في هذا البندِ ولا يُرفَعُ به: رفعُه فعلُ المالكِ.
```

---

### WI-010 — جردُ القاعدةِ المُعلَنُ في وثيقةٍ يصيرُ رقمًا يُقاسُ، وما لا يُقاسُ يُسمّى

```text
النطاق: audit-truth
المسار/المرحلة: T0.6 (ما بقيَ مفتوحًا من W-017: «الأداةُ المُقارِنةُ آليًّا»)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/schema_inventory_drift.py                    (الأداةُ: تقرأُ المُعلَنَ · تقيسُ استقامتَه · تُقابِلُه بحِملٍ حيٍّ · ترفضُ مُصنَّفًا)
  tests/governance/test_w055_schema_inventory_drift.py          (حرسُ المعيارِ: 26 فحصًا · أُثبِتَ عضُّها بأربعِ طفراتٍ مقصودةٍ)
  ARCHITECTURE.md                                               (قياسُ التصديقِ المؤرَّخُ · وحدُّ الصدقِ أُعيدَ كتابتُه ثلاثةَ أقسامٍ)
وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ:
  ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md · THE_ROADMAP.md
  و`docs/audit/measurements/final_audit_p14.json` — مجلَّدٌ مُعفًى بالبادئةِ، والملفُّ **غيرُ مُدَّعًى في بندٍ مفتوحٍ**،
  وإعادةُ توليدِه بأمرِها المُقيَّدِ هي عينُ ما تأمرُ به رسالةُ البوّابةِ الساقطةِ (تفصيلُه في الحدِّ أدناه)
خارجَ النطاق:
  - لا يُلمَسُ `tools/governance/measurement_provenance.py`: محجوزٌ لـ`WI-006` وهو `IN_REVIEW` — فلم يُقيَّدْ نَسَبُ القياسِ ولم يُنشَرِ الحِملُ (`DISC-014`)
  - ولا `docs/audit/measurements/README.md` بمضمونٍ جديدٍ: صفُّ فهرسٍ لملفٍّ لم يُنشَرْ فهرسٌ يكذِبُ
  - ولا `tools/governance/ci_verdict_readability.py`: عيبُ واجهتِه مقيسٌ ومُقيَّدٌ في `DISC-015`، والملفُّ محجوزٌ لـ`WI-006`
  - لا يُلمَسُ `.github/**`: ربطُ الأداةِ بوظيفةٍ يلزمُه سرُّ قاعدةٍ في CI، وذاك قرارُ المالكِ
  - لا تُعدَّلُ الأرقامُ المُعلَنةُ في `ARCHITECTURE.md`: طابقَها المقيسُ، ولو خالفَته لكانَ التصحيحُ قيدًا لا صمتًا
  - لا تكتبُ الأداةُ في `ARCHITECTURE.md`: بوّابةٌ تُصلِحُ ما تحكمُ عليه لا تُثبِتُ شيئًا (سابقةُ `W-037`/`W-038`)
  - لا يُغلَقُ `WI-006`…`WI-009`: طريقُ الإغلاقِ مقطوعٌ ما دامَ `A-2` معلَّقًا (`DISC-012`)
  - لا يُدَّعى أنَّ CI أخضرُ ولا أحمرُ: حكمُ تشغيلَيِ الدمجِ `#25` **غيرُ مقروءٍ** بقياسِ أداةِ `W-051`
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/
  - لا يُدمَجُ هذا العملُ بيدِ المنفِّذِ: الدمجُ للمالكِ
معيارُ القبول:
  1. الأرقامُ المُعلَنةُ تُقرأُ من `ARCHITECTURE.md` **نصًّا** (عنوانُ القسمِ · صفوفُ المخطَّطاتِ · تفصيلُ المجموعِ · عدَّاداتُ الصفوفِ · إصدارُ المحرِّكِ) — لا تُكتَبُ في الشِفرةِ ولا تُحفَظُ نسخةً ثانيةً
  2. `--check` يُشغَّلُ **بلا قاعدةٍ ولا سرٍّ ولا شبكةٍ** ويُسقِطُ على: غيابِ القسمِ · مجموعٍ يُخالِفُ تفصيلَه · تاريخٍ في المستقبلِ · جردٍ بلا عدَّادِ صفوفٍ
  3. `--from-json` يُقابِلُ حِملًا محفوظًا مقياسًا مقياسًا ويُسمّي كلَّ فارقٍ باسمِه (`DRIFT` · `MISSING_LIVE` · `UNDECLARED`) ويخرجُ بـ1
  4. عجزُ القياسِ **رفضٌ مُصنَّفٌ برمزِ 2** لا حكمٌ: لا وصلَ قاعدةٍ · لا مُحرِّكَ · حِملٌ غائبٌ أو ناقصٌ — ولا يُقالُ «لا افتراق» عن مقارنةٍ لم تُجرَ
  5. التقادُمُ يُحسَبُ ويُطبَعُ ولا يُسقِطُ إلّا بـ`--enforce-staleness` صريحًا — إسقاطٌ على ما لا تملِكُ البوّابةُ أداتَه عقوبةٌ لا حرسٌ (§ 13.3)
  6. الفحوصُ تسقُطُ إن أُضعِفَ الحرسُ — أُثبِتَ بأربعِ طفراتٍ مقصودةٍ ثمَّ رُدَّت
  7. حدُّ الصدقِ في `ARCHITECTURE.md` لم يبقَ جملةً واحدةً تقولُ «لا حرسَ»: صارَ ثلاثةَ أقسامٍ — محروسٌ · محروسٌ · واجبٌ بشريّ
الدليلُ المطلوب:
  pytest tests/governance/test_w055_schema_inventory_drift.py -q                        # 26 passed
  python tools/governance/schema_inventory_drift.py --check                             # خروجٌ 0 · عمرُ الجردِ 6 أيّامٍ
  python tools/governance/schema_inventory_drift.py --from-json <حِملُ القياسِ الحيّ>     # 11 مطابقًا · 0 مفترقًا
  python tools/governance/schema_inventory_drift.py --measure                           # رفضٌ مُصنَّفٌ · رمز 2 (لا سرَّ في البيئة)
  python tools/governance/measurement_provenance.py . --check                           # ✓ 11 مقيَّدًا
  python tools/governance/check_repository_identity.py .
بدأ: 2026-08-27        ينتهي الحجز: 2026-09-03
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-055` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **`T0.6` لم تُغلَقْ بهذا وشرطُ خروجِها لم يُستوفَ كلُّه**: نصُّه «أداةٌ تُقارِنُ الجردَ بالقاعدةِ آليًّا»، والمُنفَّذُ **الحُكمُ** كلُّه
    و**المقارنةُ بحِملٍ**؛ وما بقيَ هو **إعادةُ القياسِ الحيِّ في CI** وتلزمُها سرُّ خدمةٍ لا تملِكُه البوّابةُ — واجبٌ بشريٌّ كما كانَ
  - **العددُ لا المخطَّطُ**: يُقاسُ عددُ جداولٍ وعددُ صفوفٍ وإصدارٌ — لا عمودٌ ولا نوعٌ ولا قيدٌ ولا فهرسٌ ولا سياسةُ `RLS`.
    فمخطَّطٌ يُغيَّرُ بلا تغيُّرِ عددٍ **لا يُرصَدُ**، وذاك مكتوبٌ في ترويسةِ الأداةِ وفي `ARCHITECTURE.md` لا مطويٌّ في نيّةٍ
  - **قياسُ اليومِ لا افتراقَ فيه، وذاك لا يُقرأُ ثباتًا**: صفرُ الافتراقِ يقولُ إنَّ المخطَّطَ لم يتحرَّكْ بينَ 2026-08-21 و2026-08-27
    لا إنَّه لن يتحرَّك. والقياسُ **جرى بيدِ جلسةٍ موصولةٍ بمشروعِ Supabase**، لا بأمرٍ في هذا المستودعِ — فلا يُعادُ توليدُه من الشجرةِ
  - **الحِملُ الحيُّ لم يُنشَرْ ولا لعطبٍ فيه**: `measurement_provenance.py` محجوزٌ لـ`WI-006`، ونشرٌ بلا قيدِ نَسَبٍ يُسقِطُ البوّابةَ بحقٍّ.
    فكُتِبَت **حقولُ القيدِ اللازمةُ** (المُولِّدُ · أمرُ إعادةِ التوليدِ · الوضعُ `declared` · موجَزُ السببِ) في قيدِ `W-055` ليُوضَعَ بلا اجتهادٍ متى انفكَّ الحجزُ (`DISC-014` · `RK-016`)
  - **وأُعيدَ توليدُ `final_audit_p14.json` وهو ليس من عملِ هذا البندِ**: كانت بوّابةُ النَّسَبِ **ساقطةً على `main` قبلَ عملي** (قِيسَ بتنحيةِ تغييراتي)،
    وعِلّتُها أنَّ `W-052` أصلحَ مِسبرَ البصماتِ ولم يُعِدْ توليدَ حِملِه **لأنَّ شجرتَه كانت بلا سجلِّ `git` حقيقيٍّ** وأعلنَ ذلك في حدِّه.
    وشجرةُ هذه الجلسةِ نسخٌ كاملُ العمقِ (`--is-shallow-repository` = `false` · 278 التزامًا)، فأُدِّيَ الواجبُ المُعلَنُ بأمرِه المُقيَّدِ:
    الفارقُ **حقلٌ واحدٌ** (`hashes_in_doc`: 41 ← 43 بصمةً بدخولِ بصمتَيِ الأربعينَ) و**لم يتغيَّرْ عدَّادُ دَينٍ ولا مخالفةٌ**
  - **البندُ يُتركُ `IN_REVIEW` لا `CLOSED`**: لم يُدمَجْ بعدُ، و`VERIFIED` غيرُ مُتاحٍ (`A-2` بيدِ المالكِ) — والإغلاقُ نفسُه محجوبٌ بـ`DISC-012`
  - **ولا يُدَّعى أنَّ هذه الدفعةَ خضراءُ**: حكمُ CI عليها يُقيِّدُه أوّلُ عملٍ يُشاهِدُ تشغيلًا نُفِّذَ فعلًا — و`DISC-006` مفتوحٌ بيدِ المالك
قيدُ السجلّ: — (يُكتَبُ بعدَ دمجِ المالك)
```

---

### WI-009 — حرسُ ما بعدَ الدمجِ يُقاسُ من خارجِ يدِ المحروس، وحدُّه يُكتَبُ حيثُ أُحيلَ إليه

```text
النطاق: tooling-gates
المسار/المرحلة: T0 / T2 (صدقُ الشاهدِ · حرسٌ مُنفَّذٌ لا وثيقةٌ)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/check_work_governance.py                     (القياسُ العكسيُّ: قيدٌ ← بند)
  tests/governance/test_w054_post_merge_reverse_link.py         (حرسُ المعيارِ: 11 فحصًا · نجاحٌ ورفضٌ وإضعافٌ يُسقِط)
  docs/governance/work/THE_ROADMAP.md § 13.3                    (الحدُّ المُعلَنُ — إحالةٌ كانت مُعلَّقةً على قسمٍ غيرِ موجود)
خارجَ النطاق:
  - لا يُلمَسُ `.github/**`: ربطُ الإسقاطِ بالتكاملِ قرارُ تصميمٍ، والقرارُ للمالكِ (`A-3`)
  - لا يُعدَّلُ § 4.3 ولا آلةُ الحالاتِ: تعديلُ القانونِ لِيوافقَ عملًا خُرِقَت فيه ممنوعٌ نصًّا (§ 16.3)
  - لا يُغلَقُ `WI-006`/`WI-007`/`WI-008`: طريقُ الإغلاقِ مقطوعٌ ما دامَ `A-2` معلَّقًا — `DISC-012`
  - لا تُنشَرُ الحِملةُ الجديدةُ في `docs/audit/measurements/ci_verdict_readability.json`: مسارٌ محجوزٌ لـ`WI-006`
    وهو مفتوحٌ — فالقياسُ يُكتَبُ في قيدِ السجلِّ ويُنشَرُ عندَ تحرُّرِ حجزِه
  - لا يُدَّعى أنَّ CI أخضرُ ولا أحمرُ: أحكامُ التشغيلاتِ العشرةِ **غيرُ مقروءةٍ** بقياسِ أداةِ `W-051`
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/
  - لا يُدمَجُ هذا العملُ بيدِ المنفِّذِ: الدمجُ للمالكِ
معيارُ القبول:
  1. يُقرأُ سجلُّ الإكمالِ **من `origin/main`** فيُبنى فهرسُ `W-### → WI-###` من الإعلانِ الصريحِ (رابطٌ إلى ACTIVE_WORK.md)
  2. كلُّ بندٍ يُعلِنُه قيدٌ مدموجٌ وحالتُه ليست `CLOSED` يُرصَدُ `POST_MERGE_NOT_CLOSED`
  3. الدفعُ المشروعُ قبلَ الدمجِ (قيدٌ في الفرعِ لا في `main`) **لا يُحمَّرُ**، والذكرُ العارضُ لا يُحمَّرُ
  4. تعذُّرُ قراءةِ الأساسِ **يُعلَنُ** على stderr، ويُرفَضُ برمزِ 2 مع `--require-merge-base`؛ ومرجعٌ مُمَرَّرٌ صراحةً لا يُتجاوَزُ
  5. الإسقاطُ موقوفٌ على `--enforce-post-merge` حتّى يُعتمَدَ `A-2`/`A-3` — والإبلاغُ لا يُطوى
  6. الفحصُ يسقُطُ إن أُضعِفَ الحرسُ (طُبِّقَ تحويرٌ متعمَّدٌ فسقطَت 3 فحوصٍ ثمَّ رُدَّ)
  7. § 13.3 مكتوبٌ ويُطابِقُ سلوكَ الأداةِ، وإحالةُ § 7 لم تبقَ مُعلَّقةً على قسمٍ غيرِ موجود
الدليلُ المطلوب:
  pytest tests/governance/test_w054_post_merge_reverse_link.py -q                      # 11 passed
  python tools/governance/check_work_governance.py --self-check                        # إبلاغٌ: 3 بنودٍ محبوسة
  python tools/governance/check_work_governance.py --self-check --enforce-post-merge   # إسقاطٌ: رمز 1
  python tools/governance/check_work_governance.py --self-check --merge-base لا-وجود-له --require-merge-base  # رفضٌ: رمز 2
  pytest tests/governance/test_work_governance_gate.py -q
  python tools/governance/check_repository_identity.py .
بدأ: 2026-08-27        ينتهي الحجز: 2026-09-03
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` بقيدِ `W-054` ورقمِ الدمجِ — إن فُتِحَ طريقُ الإغلاقِ بقرارِ `A-2`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الحرسُ يقيسُ حضورَ القيدِ في فرعِ الدولةِ لا واقعةَ الدمجِ**: دمجٌ بلا قيدٍ لا يُدرِكُه هذا الحرسُ (وذاك لـ`ledger-gate`)
  - **القيودُ التي لا تُعلِنُ بندَها رابطًا خارجَ القياسِ**: `W-046`…`W-050` مثلًا. وجعلُ الإعلانِ إلزامًا يلزمُه تصحيحُ قيودٍ ماضيةٍ — قرارُ المالكِ لا فعلُ منفِّذٍ (`DISC-010`)
  - **الإسقاطُ لم يُفعَّلْ**: لأنَّ الواجبَ نفسَه غيرُ مُستطاعٍ الآنَ (`DISC-012`)، وإسقاطٌ على ما لا يُستطاعُ عقوبةٌ لا حرسٌ. والإبلاغُ مسموعٌ في كلِّ تشغيلٍ
  - **إصلاحُ ختمِ `docs/audit/measurements/README.md`** جرى في هذا العملِ (مسارٌ مُعفًى من الحجزِ ومولَّدٌ آليًّا) وهو **مذكورٌ في مساراتِ `WI-006` المحجوزةِ** — فلم يُطلَبْ له حجزٌ ولم يُنقَلْ إلى هذا البندِ: أُصلِحَ ختمٌ ولم يُكتَبْ مضمونٌ (`DISC-011`)
  - **أحكامُ CI على الدمجاتِ لم تُشاهَدْ**: عشرةُ تشغيلاتٍ لدمجاتِ `#20`…`#24` كلُّها `UNREADABLE` بقياسِ `ci_verdict_readability.py` — فواجبُ § 7 (6) يبقى مفتوحًا لا مُؤدًّى، وسببُه `DISC-006` بيدِ المالك
قيدُ السجلّ: — (يُكتَبُ بعدَ دمجِ المالك)
```

---

### WI-008 — بوّابةٌ لا تستوردُ ما لا يُثبَّتُ لها: إغلاقُ التبعيّاتِ يُقاسُ بالوظيفةِ لا بالنيّة

```text
النطاق: tooling-gates
المسار/المرحلة: T0 (صدقُ القياسِ نفسِه · تخفيفُ `RK-010` يُنفَّذُ شِفرةً)
المالك: Driving H            المراجع: المجلس التأسيسي
الحالة: IN_REVIEW
المسارات:
  tools/governance/gate_dependency_closure.py                  (الحرسُ — بالمكتبةِ القياسيّةِ وحدَها ورفضٌ مُصنَّفٌ برمزِ 2)
  tests/governance/test_w053_gate_dependency_closure.py         (حرسُ الحرسِ: تجهيزاتٌ محكمةٌ موقوتةٌ + طفراتٌ تُثبِتُ أنَّه يعضُّ)
  وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ: ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md
  وسببُ تركِها غيرَ مُعلَنةٍ في عمودِ المساراتِ واحدٌ: `WI-006` و`WI-007` حاجزانِ عليها وهما `IN_REVIEW`، فالدّعوى تُسقِطُ `CLAIM_CONFLICT` بحقٍّ
خارجَ النطاق:
  - **لا يُصلَحُ العطبُ المقيسُ في `sovereignty-kernel`**: تركيبُ الحزمةِ في الوظيفةِ أو نقلُ الفحوصِ أو إعلانُ التبعيّةِ ثلاثةُ حلولٍ مختلفةِ الأثرِ على معنى الوظيفةِ — والاختيارُ قرارُ المالكِ (`DISC-009` · `RK-013`)
  - لا يُمَسُّ `.github/workflows/ci.yml`: تعديلُه هو الإصلاحُ نفسُه، وهو قرارٌ لم يُحسَمْ
  - لا يُمَسُّ `docs/audit/ACTIVE_EXECUTION_STATE.md` ولا `tools/governance/measurement_provenance.py`: محجوزانِ لـ`WI-006`
  - لا يُسجَّلُ الحرسُ في `measure.yml` ولا في `ci.yml`: إضافةُ خطوةٍ إلى مسارٍ تعديلُ عقدِ CI — يُقتَرَحُ على المالكِ ولا يُنفَّذُ ذاتيًّا
  - لا تُوسَّعُ الأداةُ إلى وظيفتَي `lint` و`lockfile-check`: لا تُشغِّلانِ مدخلَ بايثونَ يُقاسُ (‏`ruff` و`pip` وحدَهما) — **والعددُ مُعلَنٌ: 13 من 15 مقيسةٌ**، لا «كلُّ الوظائفِ»
  - ولا يُدمَجُ هذا العملُ بيدِ المنفِّذِ: الدمجُ للمالكِ
معيارُ القبول:
  1. يُقاسُ الاتِّجاهُ **المقابلُ** للحرسِ القائمِ: `test_root_dependencies_declared.py` يقيسُ أنَّ الإعلاناتَ قائمةٌ وألّا يُبَثَّ اسمٌ عاريًا؛ وهذا يقيسُ أنَّ **ما تستوردُه بوّابةٌ مُثبَّتٌ في الوظيفةِ التي تُشغِّلُها** — ولا تكرارَ
  2. بالمكتبةِ القياسيّةِ وحدَها (`ast` · `re` · `tomllib` · `json`): أداةٌ تحرسُ إعلانَ التبعيّاتِ ثمَّ تلزمُها تبعيّةٌ غيرُ مُعلَنةٍ هي مثالُ العطبِ الذي تحرسُ منه
  3. الاستيراداتُ تُتبَّعُ **عبورًا** لا في الملفِّ الأوّلِ وحدَه، وتُحَلُّ الوحداتُ المحليّةُ بأبوابِها الحقيقيّةِ الثلاثةِ: جذرُ المستودعِ · دليلُ عملِ الوظيفةِ · دليلُ النَّصِّ المُشغَّلِ و`sys.path.insert` الصريحُ
  4. الاستيرادُ المحروسُ لا يُعَدُّ نقصًا: `try` يمسِكُ `ImportError` أو `Exception` يُترجِمُ الفقدانَ إلى تخطٍّ مُعلَنٍ — وعدُّه نقصًا يُحمِّرُ بوّابةً بسببٍ غيرِ حقيقيٍّ، وذاك عينُ `RK-010`
  5. حينَ لا تملكُ ما تقيسُ به **ترفضُ ولا تحكُمُ**: خروجٌ 2 و`REFUSED:` — ومن أبوابِه **وحدةٌ لا يُعرَفُ اسمُ توزيعِها**، فتخمينُه يُنتِجُ نقصًا كاذبًا
  6. الأساسُ `KNOWN_OPEN` **ترباسٌ لا رخصةٌ**: يلزمُ كلَّ مدخلٍ فيه مُوجِّهٌ (`DISC-009`)، وإن أُصلِحَ العطبُ وبقيَ الاسمُ سقطَتِ الأداةُ بـ`أساسٌ تقادمَ`
  7. الأداةُ تقيسُ ولا تكتبُ: لا تُعدِّلُ ملفًّا ولا تُثبِّتُ حزمةً ولا تُصلِحُ مسارًا
  8. والفحصُ يُثبِتُ **أنَّ الحرسَ يعضُّ**: طفراتٌ مقصودةٌ في الشِفرةِ كلٌّ منها يُمسَكُ، وتجهيزاتٌ محكمةٌ تُبنى في دليلٍ موقوتٍ بلا شبكةٍ
الدليلُ المطلوب:
  python tools/governance/gate_dependency_closure.py . --check      # 12 من 13 مُغلَقةٌ · 1 مفتوحةٌ مُقيَّدةٌ · خروجٌ 0
  pytest tests/governance/test_w053_gate_dependency_closure.py -q
  طفراتٌ مقصودةٌ في الشِفرةِ — وكلُّ واحدةٍ أُمسِكَت
  python tools/governance/check_work_governance.py --self-check · --staged
  python tools/governance/check_completion_ledger.py --self-check · --staged
  python tools/governance/check_repository_identity.py .
  python tools/governance/check_root_file_names.py . --source disk
  python tools/governance/measurement_provenance.py . --check --contract-only
  python tools/governance/truth_audit.py
  ruff check .
بدأ: 2026-08-27        ينتهي الحجز: 2026-09-03
العائق: —
الخطوةُ التالية: بعدَ أن يدمجَ المالكُ، يُنقَلُ البندُ إلى `CLOSED` ويُكتَبُ في `قيدِ السجلّ`: `W-053` ورقمُ الدمجِ وعقدتُه — § 7؛ ويُرفَعُ إلى المالكِ اختيارُ حلٍّ لـ`DISC-009`
حدُّ البندِ — مُعلَنٌ لا مطويّ:
  - **هذا حرسُ قياسٍ لا إصلاحُ عطبٍ**: العطبُ الذي كشفَه ما زالَ قائمًا في `ci.yml` — والأداةُ تُبقي الشجرةَ خضراءَ لأنَّه **مُقيَّدٌ في أساسٍ مُوجَّهٍ**، لا لأنَّه زالَ
  - **والعطبُ مقيسٌ لا مُستنتَجٌ**: `python -m pytest tests/sovereignty/ -q` عندي = `43 passed · 3 errors` بـ`ModuleNotFoundError: amos_federation` في تجهيزِ `مُصرِّح`؛ ووظيفةُ `sovereignty-kernel` تُثبِّتُ `requirements-dev.txt` وحدَه
  - **وقد وقعَ من جنسِه عطبٌ قبلَ اليومِ**: مكتوبٌ في `tests/governance/test_w036_pricing_divergence.py` أنَّ فحصًا سقطَ في وظيفةِ الهويّةِ بـ`ModuleNotFoundError: sqlalchemy` — فالخطرُ `RK-010` **متحقِّقٌ مرّتَينِ** لا مفترَضٌ
  - **وتصحيحٌ لقياسٍ سابقٍ لي في هذه الجلسةِ**: عددُ وظائفِ CI **15** لا 21 (‏`ci.yml` 13 · `measure.yml` 1 · `truth-matrix.yml` 1) — قِيسَ بالأداةِ وبـ`awk` مستقلًّا
  - **ولا قدرةَ جديدةَ في المنتَجِ**: عدّادُ الدَّينِ 182 كما كانَ، والمخالفاتُ 63 كما كانَت
  - **والقياسُ لم يُقَدْ بـCI**: لا تشغيلَ منفَّذًا في المستودعِ منذُ 2026-08-26T23:05:02Z (`DISC-006` بيدِ المالكِ) — فلا يُدَّعى أنَّ الشجرةَ خضراءُ
  - `VERIFIED` غيرُ مُتاحٍ: يلزمُه مراجعٌ مستقلٌّ وتسميتُه قرارٌ سياديٌّ معلَّقٌ (`A-2`)، و`CLOSED` قبلَ الدمجِ دعوى لا قيدٌ
قيدُ السجلّ: — (يُكتَبُ بعدَ دمجِ المالك)
```

---

## 4 · كيفَ يُقرأُ هذا السجلُّ قبلَ أيِّ عمل

1. هل مسارُك مذكورٌ في عمودِ `المسارات` لبندٍ نشِط؟ → **لا تبدأْ**؛ راجعْ مالكَه (§ 6.1 من الخارطة).
2. هل عملُك مُقيَّدٌ منجَزًا في `COMPLETION_LEDGER.md § 8`؟ → **لا يُعاد** (§ 6.5).
3. هل نطاقُك مُسجَّلٌ في [`OWNERSHIP.md`](OWNERSHIP.md)؟ → إن لا، فأوّلُ عملِك تسجيلُه.
4. هل تخدمُ الخطوةَ التاليةَ غيرَ المحجوبةِ في `COMPLETION_LEDGER.md § 7`؟ → إن لا، فبندُك `PROPOSED` حتى يُعتمَد.
