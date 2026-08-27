# سجلُّ العملِ المفتوح — ACTIVE WORK

## الهدف: إعلانُ ما يُعملُ عليه **الآن**، ومَن يعملُ عليه، وفي أيِّ مساراتٍ بالضبط، وإلى متى — حتى لا يبدأَ أحدٌ عملًا بدأَه غيرُه، ولا ينتظرَ نطاقًا لا يعملُ فيه أحد
## النطاق: البنودُ المفتوحةُ وحدَها (`PROPOSED` → `VERIFIED`) والمُغلَقةُ حديثًا. **لا يُسجَّلُ هنا تاريخُ ما أُنجِز** — ذاك في [`COMPLETION_LEDGER.md`](../../audit/COMPLETION_LEDGER.md)، ولا حالةُ القدرةِ — تلك في [`TRUTH_MATRIX.md`](../../audit/TRUTH_MATRIX.md)
## المالك: قائدُ التنفيذِ، بتفويضٍ من المجلس التأسيسي
## تاريخ الإنشاء: 2026-08-25
## تاريخ آخر تعديل: 2026-08-27

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
| WI-006 | tooling-gates | T0 / T2 | Driving H | المجلس التأسيسي | IN_REVIEW | tools/governance/ci_verdict_readability.py · tests/governance/test_w051_ci_verdict_readability.py · tools/governance/measurement_provenance.py · tests/governance/test_w038_probe_measure_mode.py · tests/governance/test_w048_bound_provenance.py · docs/audit/measurements/ci_verdict_readability.json · docs/audit/measurements/README.md · docs/governance/work/ACTIVE_WORK.md · docs/governance/work/DISCOVERIES.md · docs/governance/work/RISK_REGISTER.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-27 | 2026-09-03 | — (لا عائقَ على البندِ نفسِه؛ والعطبُ المقيسُ عائقٌ على `T0.4ب` لا عليه) | يُنقَلُ إلى `CLOSED` بقيدِ `W-051` ورقمِ الدمجِ بعدَ أن يدمجَ المالكُ — § 7 | — (يُكتَبُ بعدَ دمجِ المالك) |
| WI-007 | tooling-gates | T0 | Driving H | المجلس التأسيسي | IN_REVIEW | tools/audit/final_audit.py · tests/governance/test_w052_history_hash_probe.py · docs/governance/work/OWNERSHIP.md | 2026-08-27 | 2026-09-03 | — (لا عائقَ على البندِ نفسِه) | يُنقَلُ إلى `CLOSED` بقيدِ `W-052` ورقمِ الدمجِ بعدَ أن يدمجَ المالكُ — § 7 | — (يُكتَبُ بعدَ دمجِ المالك) |

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

## 4 · كيفَ يُقرأُ هذا السجلُّ قبلَ أيِّ عمل

1. هل مسارُك مذكورٌ في عمودِ `المسارات` لبندٍ نشِط؟ → **لا تبدأْ**؛ راجعْ مالكَه (§ 6.1 من الخارطة).
2. هل عملُك مُقيَّدٌ منجَزًا في `COMPLETION_LEDGER.md § 8`؟ → **لا يُعاد** (§ 6.5).
3. هل نطاقُك مُسجَّلٌ في [`OWNERSHIP.md`](OWNERSHIP.md)؟ → إن لا، فأوّلُ عملِك تسجيلُه.
4. هل تخدمُ الخطوةَ التاليةَ غيرَ المحجوبةِ في `COMPLETION_LEDGER.md § 7`؟ → إن لا، فبندُك `PROPOSED` حتى يُعتمَد.
