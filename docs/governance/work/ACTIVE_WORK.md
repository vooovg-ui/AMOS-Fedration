# سجلُّ العملِ المفتوح — ACTIVE WORK

## الهدف: إعلانُ ما يُعملُ عليه **الآن**، ومَن يعملُ عليه، وفي أيِّ مساراتٍ بالضبط، وإلى متى — حتى لا يبدأَ أحدٌ عملًا بدأَه غيرُه، ولا ينتظرَ نطاقًا لا يعملُ فيه أحد
## النطاق: البنودُ المفتوحةُ وحدَها (`PROPOSED` → `VERIFIED`) والمُغلَقةُ حديثًا. **لا يُسجَّلُ هنا تاريخُ ما أُنجِز** — ذاك في [`COMPLETION_LEDGER.md`](../../audit/COMPLETION_LEDGER.md)، ولا حالةُ القدرةِ — تلك في [`TRUTH_MATRIX.md`](../../audit/TRUTH_MATRIX.md)
## المالك: قائدُ التنفيذِ، بتفويضٍ من المجلس التأسيسي
## تاريخ الإنشاء: 2026-08-25
## تاريخ آخر تعديل: 2026-08-25

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
| WI-002 | audit-truth | T0 / T2 | Driving H | المجلس التأسيسي | CLOSED | docs/audit/COMPLETION_LEDGER.md · EXECUTION_PLAN.md · docs/governance/work/DISCOVERIES.md · docs/governance/work/THE_ROADMAP.md · PROJECT_STATE.md · docs/audit/ACTIVE_EXECUTION_STATE.md · docs/governance/work/ACTIVE_WORK.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَق) | W-047 |

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

## 4 · كيفَ يُقرأُ هذا السجلُّ قبلَ أيِّ عمل

1. هل مسارُك مذكورٌ في عمودِ `المسارات` لبندٍ نشِط؟ → **لا تبدأْ**؛ راجعْ مالكَه (§ 6.1 من الخارطة).
2. هل عملُك مُقيَّدٌ منجَزًا في `COMPLETION_LEDGER.md § 8`؟ → **لا يُعاد** (§ 6.5).
3. هل نطاقُك مُسجَّلٌ في [`OWNERSHIP.md`](OWNERSHIP.md)؟ → إن لا، فأوّلُ عملِك تسجيلُه.
4. هل تخدمُ الخطوةَ التاليةَ غيرَ المحجوبةِ في `COMPLETION_LEDGER.md § 7`؟ → إن لا، فبندُك `PROPOSED` حتى يُعتمَد.
