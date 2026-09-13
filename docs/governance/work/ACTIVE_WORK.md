# سجلُّ العملِ المفتوح — ACTIVE WORK

## الهدف: إعلانُ ما يُعملُ عليه **الآن**، ومَن يعملُ عليه، وفي أيِّ مساراتٍ بالضبط، وإلى متى — حتى لا يبدأَ أحدٌ عملًا بدأَه غيرُه، ولا ينتظرَ نطاقًا لا يعملُ فيه أحد
## النطاق: البنودُ المفتوحةُ وحدَها (`PROPOSED` → `VERIFIED`) والمُغلَقةُ حديثًا. **لا يُسجَّلُ هنا تاريخُ ما أُنجِز** — ذاك في [`COMPLETION_LEDGER.md`](../../audit/COMPLETION_LEDGER.md)، ولا حالةُ القدرةِ — تلك في [`TRUTH_MATRIX.md`](../../audit/TRUTH_MATRIX.md)
## المالك: قائدُ التنفيذِ، بتفويضٍ من المجلس التأسيسي
## تاريخ الإنشاء: 2026-08-25
## تاريخ آخر تعديل: 2026-09-13 (W-161 — الدمجُ إلى main تمَّ تقديمًا سريعًا، وحكمُ CI على العقدةِ المدموجةِ b951dca قُرِئَ أخضرَ 14/14 (تشغيلُ 34784013601 · 13/13 · ومصفوفةُ الحقيقةِ 34784013651 · 1/1) بساعةِ قراءةٍ مُقيَّدةٍ؛ ثمَّ شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ فردَّت البنودَ الستَّةَ كلَّها — أربعةٌ بإجماعٍ واثنانِ بانقسامٍ — فصفرُ VERIFIED بقاعدةِ Q-43، ونُقِلَت الستّةُ IN_REVIEW → IN_PROGRESS، وقُيِّدَ DISC-063 وDISC-064؛ ولم يُصلَحْ عيبٌ في قيدِ تقييدِه ولم يُرفَعْ الحاجزُ عن بنودِ READY الخمسةِ) · وقبلَه 2026-09-13 (`W-160` — حكمُ CI على عقدةِ `W-159` قُرِئَ فسقطَ في وظيفةِ «Work Governance» وحدَها بستِّ مخالفاتِ `DUE_DATE_PASSED`، والسببُ مقيسٌ على عينِ عقدةِ `97e9acd`: **الحكمُ دالّةٌ في الزمنِ لا في الشجرةِ وحدَها** — فجُدِّدَت الاستحقاقاتُ الستُّ إلى 2026-09-30 بسببٍ مكتوبٍ بلا محوِ الأوّلِ، وقُيِّدَ `DISC-062` ووُجِّهَ إلى حرسٍ يقيسُ عددَ التجديداتِ · ولا حرسَ خُفِّفَ ولا اختبارَ سُكِّتَ ولا حالةَ بندٍ نُقِلَت) · وقبلَه 2026-09-13 (`W-159` — واجبُ § 7 السادسُ أُدِّيَ على عقدةِ `W-158` (`97e9acd`) بعدَ **يومَينِ من التأخُّرِ** — والتأخُّرُ مُقَيَّدٌ دينًا في الواجبِ لا ممحُوٌ: التشغيلُ [34564791386](https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34564791386) ⇒ `success` · **14 خضراءَ · 0 حمراءَ · 0 متخطّاةٍ** · وسُجِّلَ البندُ `WI-052` (`IN_PROGRESS`) لتشغيلِ الجولةِ الخامسةِ من مجلسِ المراجعةِ المستقلِّ على البنودِ الستّةِ التي قِيسَ أنَّها تقفلُ مساراتِ بنودِ `READY` الخمسةِ) · والقيدُ السابقُ: 2026-09-11 (`W-158` — `WI-051` أُغلِقَ `VERIFIED → CLOSED` في التزامٍ منفصلٍ بعدَ قراءةِ حكمِ CI على عقدةِ الاعتمادِ `W-157` (‏التشغيلُ 34562272448 ⇒ **أخضرُ 14/14 · 0 حمراءَ · 0 متخطّاةٍ**) — فحدُّ التسلسلِ `DISC-060` أُدِّيَ · ومعاييرُ القبولِ التسعةُ مُستوفاةٌ · ومجلسُ المراجعةِ المستقلِّ صارَ مُجرَّبًا أربعَ جولاتٍ: رفضَ بإجماعٍ مرّتَينِ وانقسمَ مرّةً وأجمعَ `VERIFIED` في الرابعةِ)

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
| WI-001 | governance-docs | T2 | Driving H | المجلس التأسيسي | CLOSED | docs/governance/work · tools/governance/check_work_governance.py · tests/governance/test_work_governance_gate.py · .github/workflows/ci.yml · docs/governance/README.md · docs/index.md · README.md · docs/PROJECT_HANDBOOK.md · docs/audit/COMPLETION_LEDGER.md | 2026-08-25 | 2026-08-31 | — | — (مُغلَق) | W-043 · W-044 · W-045 · W-046 · دمجُ #14 (`2b355ca3`) · #15 (`b4d957fa`) |
| WI-003 | tooling-gates | T0 / T2 | Driving H | المجلس التأسيسي | CLOSED | tools/governance/measurement_provenance.py · tools/governance/restart_survival_probe.py · .github/workflows/measure.yml · tests/governance/test_w048_bound_provenance.py · tests/governance/test_w037_measurement_provenance.py · tests/governance/test_w038_probe_measure_mode.py · docs/audit/measurements/README.md · docs/PROJECT_HANDBOOK.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَقٌ بقيدِ W-048 · وحكمُ CI على دفعتِه يُقيِّدُه أوّلُ عملٍ تالٍ كما فَعلَ W-044 بما قبلَه) | W-048 |
| WI-005 | audit-truth | T0 | Driving H | المجلس التأسيسي | CLOSED | docs/governance/work/ACTIVE_WORK.md · docs/governance/work/DISCOVERIES.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَقٌ بقيدِ W-050 · وDISC-006 ما زالَ مفتوحًا بيدِ المالكِ) | W-050 |
| WI-004 | audit-truth | T0 | Driving H | المجلس التأسيسي | CLOSED | docs/governance/work/DISCOVERIES.md · docs/governance/work/RISK_REGISTER.md · docs/governance/work/ACTIVE_WORK.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَقٌ بقيدِ W-049 · وإصلاحُ حسابِ Actions بيدِ المالكِ — DISC-006 مفتوحٌ عليه) | W-049 |
| WI-002 | audit-truth | T0 / T2 | Driving H | المجلس التأسيسي | CLOSED | docs/audit/COMPLETION_LEDGER.md · EXECUTION_PLAN.md · docs/governance/work/DISCOVERIES.md · docs/governance/work/THE_ROADMAP.md · PROJECT_STATE.md · docs/audit/ACTIVE_EXECUTION_STATE.md · docs/governance/work/ACTIVE_WORK.md | 2026-08-26 | 2026-09-02 | — | — (مُغلَق) | W-047 |
| WI-006 | tooling-gates | T0 / T2 | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/governance/ci_verdict_readability.py · tests/governance/test_w051_ci_verdict_readability.py · tools/governance/measurement_provenance.py · tests/governance/test_w038_probe_measure_mode.py · tests/governance/test_w048_bound_provenance.py · docs/audit/measurements/ci_verdict_readability.json · docs/audit/measurements/README.md · docs/governance/work/ACTIVE_WORK.md · docs/governance/work/DISCOVERIES.md · docs/governance/work/RISK_REGISTER.md · docs/audit/COMPLETION_LEDGER.md · docs/audit/ACTIVE_EXECUTION_STATE.md | 2026-08-27 | 2026-09-03 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-051 · دفعٌ مباشرٌ إلى main (`9561d9a`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-007 | tooling-gates | T0 | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/audit/final_audit.py · tests/governance/test_w052_history_hash_probe.py · docs/governance/work/OWNERSHIP.md | 2026-08-27 | 2026-09-03 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-052 · دفعٌ مباشرٌ إلى main (`3cea7f3`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-008 | tooling-gates | T0 | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/governance/gate_dependency_closure.py · tests/governance/test_w053_gate_dependency_closure.py | 2026-08-27 | 2026-09-03 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-053 · دفعٌ مباشرٌ إلى main (`84969a9`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-010 | audit-truth | T0 | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/governance/schema_inventory_drift.py · tests/governance/test_w055_schema_inventory_drift.py · ARCHITECTURE.md | 2026-08-27 | 2026-09-03 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-055 · دفعٌ مباشرٌ إلى main (`978638f`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-011 | audit-truth | T0 (قابليّةُ القياسِ · شرطُ خروجٍ) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/governance/sovereign_decision_status.py · tests/governance/test_w056_sovereign_decision_status.py | 2026-08-27 | 2026-09-03 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-056 · دفعٌ مباشرٌ إلى main (`3e9ee6a`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-012 | audit-truth | T0 (قابليّةُ القياسِ · شرطُ خروجٍ) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/governance/state_document_drift.py · tests/governance/test_w057_state_document_drift.py | 2026-08-27 | 2026-09-03 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-057 · دفعٌ مباشرٌ إلى main (`9c05ed8`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-009 | tooling-gates | T0 / T2 | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | — (المسارُ سُلِّمَ · § 6.4) | 2026-08-27 | 2026-09-03 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-054 · دفعٌ مباشرٌ إلى main (`aedd379`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-013 | tests-root | T0 (صدقُ الحرسِ · منعُ كذبٍ مُوثَّقٍ معكوسٍ) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tests/governance/test_step18_restart_survival.py · tests/governance/test_w058_live_stack_precondition.py | 2026-08-27 | 2026-09-03 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-058 · دفعٌ مباشرٌ إلى main (`eafc38e`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-015 | governance-docs | T0 (قابليّةُ القياسِ · دعوى الحرسِ تُثبَتُ بطفرةٍ لا تُكتَبُ) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | — (لا مسارَ يُحجَزُ: كلُّ ما يُمَسُّ **مُعفًى من الحجزِ** بنصِّ § 6 — `DISCOVERIES.md` · `RISK_REGISTER.md` · `ACTIVE_WORK.md` · `COMPLETION_LEDGER.md` وسطرُ آخرِ قيدٍ في وثيقتَي الحالةِ؛ ولذلك لا يُزاحَمُ حجزُ `WI-006`) | 2026-08-28 | 2026-09-04 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-060 · دمجُ #2 (`6a7e571`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33219913887 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-014 | tooling-gates | T0 (قابليّةُ القياسِ · قاعدةٌ مكتوبةٌ تصيرُ عدَّادًا) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/governance/open_record_accountability.py · tests/governance/test_w059_open_record_accountability.py | 2026-08-28 | 2026-09-04 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-059 · دمجُ #1 (`764a3dc`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33217559878 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-019 | tooling-gates | T0 (قابليّةُ القياسِ · حكمُ CI يُقرأُ ثمَّ يُخضَّرُ من سببِه) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/crown/secret_scan_exceptions.py · tests/crown/test_w064_secret_scan_exceptions.py · tools/crown/verify_secret_boundaries.py · tests/sovereignty/test_outbox.py · docs/security/SECRET_BOUNDARIES.md · conftest.py · tests/governance/test_w064_services_src_fallback.py · .github/workflows/ci.yml | 2026-08-29 | 2026-09-06 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-064 · دمجُ #6 (`17ab3c4`) · حكمُ CI: أخضرُ 13/13 (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-018 | tooling-gates | T0 (قابليّةُ القياسِ · دعاوى القيودِ السابقةِ تصيرُ مُسجَّلةً ومقيسةً) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tests/governance/test_w063_registered_claims.py | 2026-08-29 | 2026-09-05 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-063 · دمجُ #5 (`0803ae2`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33278721516 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-017 | tooling-gates | T0 (قابليّةُ القياسِ · «الحرسُ مُجرَّبٌ بطفرةٍ» يصيرُ أمرًا يُعادُ) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/governance/mutation_probe.py · tools/governance/mutation_claims.py · tests/governance/test_w062_mutation_probe.py | 2026-08-29 | 2026-09-05 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-062 · دمجُ #4 (`3356d71`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33278679341 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-016 | tooling-gates | T0 (قابليّةُ القياسِ · إشارةُ خطرٍ مكتوبةٌ تصيرُ رقمًا) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | tools/governance/surface_debt_trend.py · tests/governance/test_w061_surface_debt_trend.py | 2026-08-29 | 2026-09-05 | — | يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ — § 4.3 لا يُجيزُ `IN_REVIEW → CLOSED` وثبًا | W-061 · دمجُ #3 (`7f6ccf1`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33251600117 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633) |
| WI-020 | governance-docs | T0 / T2 (قرارٌ سياديٌّ يُقيَّدُ · وواجبُ § 7 يُوفَّى بعدَه) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | docs/governance/work/THE_ROADMAP.md · tools/governance/check_work_governance.py · PROJECT_STATE.md · docs/PROJECT_HANDBOOK.md · tests/governance/test_w054_post_merge_reverse_link.py | 2026-08-30 | 2026-09-06 | — | مُنجَزٌ · واجبُ § 7 وُفِّيَ كاملًا و`--enforce-post-merge` ⇒ 0 | W-065 · دفعٌ مباشرٌ إلى main (`bdfc1db`) وإتمامٌ في `04415f4` و`12a3df7` · حكمُ CI على عقدةِ القيدِ: **أحمرُ** 12/13 (تشغيلُ 33312805372) بعَطبِ قياسٍ قُيِّدَ `DISC-033` وأُصلِحَ في `W-066`، ثمَّ **أخضرُ 13/13** على `04415f4` (تشغيلُ 33315225633) وعلى عقدةِ وفاءِ الواجبِ `12a3df7` (تشغيلُ 33316791473) · مُراجَعٌ ومُغلَقٌ 2026-08-30 بـ`W-068` |

---
| WI-021 | tooling-gates | T0 / T0.4ب (إرجاعُ `main` أخضرَ · واحديّةُ الماسحِ ومحلُّ القياسِ الصريحُ) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | .github/workflows/ci.yml · tools/crown/verify_secret_boundaries.py · tools/governance/check_work_governance.py · tests/governance/test_w054_post_merge_reverse_link.py · tests/governance/test_w069_single_scanner_and_explicit_root.py · tests/governance/test_w069_status_contradiction.py · tests/governance/test_work_governance_gate.py · PROJECT_STATE.md · docs/PROJECT_HANDBOOK.md | 2026-08-30 | 2026-09-06 | — | مُنجَزٌ · مساراتُه الثمانيةُ انفكَّت (§ 6.1) · وقرارُ `origin/develop` بيدِ المالكِ | W-069 · دفعٌ مباشرٌ إلى main (`ed9e5c5`) · حكمُ CI على عقدةِ القيدِ **قُرِئَ أخضرَ 13/13** (تشغيلُ 33342938099 · `completed success` · و`ci_verdict_readability.py --from-json` ⇒ `READABLE · 13/13`) · مُراجَعٌ 2026-08-31 (`A-2` · غيرُ مستقلٍّ) · **مُغلَقٌ 2026-08-31 بـ`W-071`** بعدَ خُضرةٍ مقروءةٍ ثانيةٍ 13/13 على `0ce4d5d` (تشغيلُ 33345147799 · `READABLE`) |
| WI-022 | docs-general | T0 / T0.4ب (صدقُ السجلِّ في موضعِه · إعادةُ تقييمِ `DISC-034` بقياسٍ صحيحٍ) | Driving H | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | PROJECT_STATE.md · docs/PROJECT_HANDBOOK.md | 2026-08-31 | 2026-09-07 | — | مُنجَزٌ · مساراهُ انفكّا (§ 6.1) · وقرارُ `origin/develop` بيدِ المالكِ بثلاثةِ خياراتٍ | W-072 · دفعٌ مباشرٌ إلى main (`fb70f47`) · حكمُ CI على عقدةِ القيدِ **قُرِئَ أخضرَ 13/13** (تشغيلُ 33348727892 · `completed success` · و`ci_verdict_readability.py --from-json` ⇒ `READABLE · 13/13`) · مُسلَّمٌ للمراجعةِ 2026-08-31 · مُراجَعٌ 2026-08-31 (`A-2` · غيرُ مستقلٍّ) بعدَ خُضرةٍ مقروءةٍ ثانيةٍ 13/13 على `afae5e0` (تشغيلُ 33350334816 · `READABLE`) · **مُغلَقٌ 2026-08-31 بـ`W-075`** بعدَ خُضرةٍ مقروءةٍ ثالثةٍ 13/13 على `2a5c1f6` (تشغيلُ 33351966117 · `READABLE`) |
| WI-023 | tooling-gates | T0 / T0.4ب (قابليّةُ القياسِ — دعوى «يُشغَّلُ في كلِّ دفعةٍ» تُقاسُ قبلَ أن تُقبَلَ سندًا) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_PROGRESS | tools/governance/guard_enforcement_closure.py · tests/governance/test_w077_guard_enforcement_closure.py | 2026-08-31 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، فبطلَ مضمونُ العبارةِ السابقةِ «لم يُشغَّلْ له مراجعٌ بعدُ» — وتبقى مكتوبةً شاهدةً على تاريخِها لا تُمحى.** والحكمُ: **`REJECTED` بإجماعِ المراجعَينِ** (أ `P1=4` · ب `P1=3` و`P2=2`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ عيوبِ الجولةِ الخامسةِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ. | معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`) | W-078 · حكمُ عقدةِ `4764a12` مقروءٌ **13/13 · READABLE** (تشغيلُ 33391458311) |
| WI-024 | tooling-gates | T0 / T0.4ب (قابليّةُ القياسِ — «أداةٌ حاكمةٌ لا تُشغَّلُ» تُقاسُ وتُعلِنُ سببَها) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_PROGRESS | tools/governance/enforcement_path_ledger.py · tests/governance/test_w079_enforcement_path_ledger.py · tools/audit/final_audit.py · tools/audit/judicial_gate_probe.py · tools/audit/treasury_gate_probe.py · tools/governance/ci_verdict_readability.py · tools/governance/constitutional_reconciliation.py · tools/governance/evidence_registry.py · tools/governance/gate_dependency_closure.py · tools/governance/schema_inventory_drift.py · tools/governance/sovereign_decision_status.py · tools/migrations/r4_unify_agent_identity.py · tools/stubs/registry_check.py | 2026-08-31 | 2026-09-30 | انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (`Q-43`) — **والحجزُ جُدِّدَ إلى 2026-09-15 في `W-152`** بنصِّ § 6.3 (‏انقضى 2026-09-08 فحمَّرَ `RESERVATION_EXPIRED` وأسقطَ «Cross-System Suites») · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، فبطلَ مضمونُ العبارةِ السابقةِ «لم يُشغَّلْ له مراجعٌ بعدُ» — وتبقى مكتوبةً شاهدةً على تاريخِها لا تُمحى.** والحكمُ: **`REJECTED` بإجماعِ المراجعَينِ** (أ `P1=3` · ب `P1=4`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ عيوبِ الجولةِ الخامسةِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ. | معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`) | W-079 · الحجزُ وقياسُ خطِّ الأساسِ |
| WI-025 | audit-truth | T0 / T0.4ب (‏صدقُ القياسِ — القياسُ المنشورُ يُفتَّحُ بما يُقاسُ لا بإحداثيٍّ في المصدرِ) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/audit/sovereign_write_inventory.py · tests/governance/test_w083_measurement_site_key.py · docs/audit/measurements/write_inventory_p13.json · docs/audit/measurements/README.md | 2026-08-31 | 2026-09-30 | انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (`Q-43`) — **والحجزُ جُدِّدَ إلى 2026-09-15 في `W-152`** بنصِّ § 6.3 (‏انقضى 2026-09-08 فحمَّرَ `RESERVATION_EXPIRED` وأسقطَ «Cross-System Suites») · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ ثمَّ `VERIFIED` — بيدِ المراجعِ لا بيدِ صاحبِ التغييرِ (§ 4.3) | W-085 · حكمُ عقدةِ `W-084` أخضرُ 13/13 · READABLE |
| WI-026 | tooling-gates | T0 (قابليّةُ القياسِ · حالةُ تشغيلٍ تُكتَبُ في الشجرةِ فتُحمِّرُ بوّابةً على أثرٍ غيرِ مُفهرَسٍ) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | conftest.py · tests/governance/test_runtime_state_stays_outside_the_tree.py · federal/executive/services/tests/conftest.py | 2026-09-01 | 2026-09-30 | انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (`Q-43`) — **والحجزُ جُدِّدَ إلى 2026-09-15 في `W-152`** بنصِّ § 6.3 (‏انقضى 2026-09-08 فحمَّرَ `RESERVATION_EXPIRED` وأسقطَ «Cross-System Suites») · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ ثمَّ `VERIFIED` — بيدِ المراجعِ لا بيدِ صاحبِ التغييرِ (§ 4.3) | W-088 · حكمُ عقدةِ `W-087` أخضرُ 13/13 · READABLE |
| WI-027 | audit-truth | T0 (قابليّةُ القياسِ · حرسُ انحرافٍ يقيسُ أقصى ذكرٍ في النصِّ لا الحقلَ الذي تُعلِنُه الوثيقةُ حالةً) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/state_document_drift.py · tests/governance/test_w057_state_document_drift.py | 2026-09-01 | 2026-09-30 | انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (`Q-43`) — **والحجزُ جُدِّدَ إلى 2026-09-15 في `W-152`** بنصِّ § 6.3 (‏انقضى 2026-09-08 فحمَّرَ `RESERVATION_EXPIRED` وأسقطَ «Cross-System Suites») · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ ثمَّ `VERIFIED` — بيدِ المراجعِ لا بيدِ صاحبِ التغييرِ (§ 4.3) | W-091 · حكمُ عقدةِ `W-090` أخضرُ 13/13 · READABLE |
| WI-028 | tooling-gates | T0 (قابليّةُ القياسِ · حرسٌ يقرأُ الدعوى بجذرِ كلمةٍ فيُحمِّرُ على قيدٍ صادقٍ) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/mutation_claims.py · tests/governance/test_w063_registered_claims.py | 2026-09-01 | 2026-09-30 | انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (`Q-43`) — **والحجزُ جُدِّدَ إلى 2026-09-15 في `W-152`** بنصِّ § 6.3 (‏انقضى 2026-09-08 فحمَّرَ `RESERVATION_EXPIRED` وأسقطَ «Cross-System Suites») · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةُ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) (§ 4.3) — الكاتبُ لا يُصدِّقُ نفسَه | W-095 |
| WI-029 | tests-root | T0 (قابليّةُ القياسِ · فحصٌ يُشغِّلُ أداةً في عمليّةٍ فرعيّةٍ ويحكُمُ على شجرةٍ **لا يقرؤها** · `DISC-032`) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tests/governance/test_w096_subprocess_measurement_site.py · tests/governance/test_w054_post_merge_reverse_link.py | 2026-09-01 | 2026-09-30 | انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (`Q-43`) — **والحجزُ جُدِّدَ إلى 2026-09-15 في `W-152`** بنصِّ § 6.3 (‏انقضى 2026-09-08 فحمَّرَ `RESERVATION_EXPIRED` وأسقطَ «Cross-System Suites») · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مُسلَّمٌ للمراجعةِ · حكمُ CI قُرِئَ أخضرَ 13/13 · والنقلُ إلى `VERIFIED` فعلُ المراجعِ لا فعلُ الكاتبِ (§ 4.3 — والمراجعُ مستقلٌّ بـ`Q-43` · `DISC-027`) | W-097 · دفعٌ مباشرٌ إلى main (`9bf0b00`) · **حكمُ عقدةِ القيدِ نفسِها قُرِئَ أحمرَ** (تشغيلُ 33570417864 · رقمُ 55 · `READABLE` · 12/13) **بسببٍ خارجَ نطاقِ البندِ**: خطوةُ «المصفوفةُ المدفوعةُ محدَّثةٌ» في وظيفةِ `Truth Audit` — ووظيفةُ `Tests` نفسُها **خضِرَت**، فالحرسُ نُفِّذَ وسكتَ على شجرةٍ صادقةٍ. وقُطِعَ السببُ في مصدرِه بـ`W-098`، فقُرِئَ الحكمُ على العقدةِ التاليةِ `815d707` **أخضرَ 13/13** (تشغيلُ [33572642082](https://github.com/xoos-beep/AMOS-Fedration/actions/runs/33572642082) · رقمُ 56 · `completed success` · و`ci_verdict_readability.py --from-json` ⇒ `READABLE · 13/13`) وهي تحملُ مساراتِ البندِ بلا تغيُّرٍ · مُسلَّمٌ للمراجعةِ 2026-09-01 · **وقيدُ التسليمِ لا يُسمّى في هذه الخليّةِ** بالسابقةِ المقيسةِ نفسِها (`DISC-010` · `DISC-030`): البوّابةُ تقرأُ الرابطَ العكسيَّ فتُشعِلُ `POST_MERGE_NOT_CLOSED` على بندٍ حالتُه `IN_REVIEW`، والرابطُ يكتبُه مَن يُغلِقُ. والدليلُ لم يُخفَ: قيدُ التسليمِ يُسمّي هذا البندَ نصًّا |
| WI-030 | tooling-gates | T0 (قابليّةُ القياسِ · أثرٌ مُولَّدٌ يتقادمُ فتخضَرُّ كلُّ بوّابةٍ محلّيّةٍ ويحمَرُّ CI وحدَه · `DISC-040`) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/truth_audit.py · tests/governance/test_w099_generated_artifact_freshness.py | 2026-09-01 | 2026-09-30 | انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (`Q-43`) — **والحجزُ جُدِّدَ إلى 2026-09-15 في `W-152`** بنصِّ § 6.3 (‏انقضى 2026-09-08 فحمَّرَ `RESERVATION_EXPIRED` وأسقطَ «Cross-System Suites») · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ ثمَّ `VERIFIED` — بيدِ المراجعِ لا بيدِ صاحبِ التغييرِ (§ 4.3) | — |
| WI-031 | tooling-gates | T0 (قابليّةُ القياسِ · جذرُ القياسِ مُثبَّتٌ بعُمقٍ مكتوبٍ فيُقرأُ أخضرُ عن شجرةٍ غيرِ مقصودةٍ · `DISC-041` · سببُ `DISC-032` الأعمقُ) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tests/governance/test_w102_measurement_root_provenance.py | 2026-09-02 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةُ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — ولا يضعُ الكاتبُ `VERIFIED` (§ 4.3) | — |
| WI-032 | tooling-gates | T0 (خفضُ دَينِ `DISC-041` المقيسِ: جذرٌ يُعرَفُ بعلامةٍ لا بعُمقٍ مكتوبٍ — في المواضعِ **الحرّةِ** وحدَها) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_PROGRESS | tools/governance/repo_root.py · tests/governance/test_w106_repo_root_discovery.py · tests/governance/test_completion_ledger_gate.py · tests/governance/test_constitutional_reconciliation.py · tests/governance/test_cross_system_suites.py · tests/governance/test_identity_law.py · tests/governance/test_measurement_ignores_environments.py · tests/governance/test_q3_branch_declaration_surface.py · tests/governance/test_root_dependencies_declared.py · tests/governance/test_step12_live_truth_guards.py · tests/governance/test_step13_identity_headers.py · tests/governance/test_step16_silent_fallback.py · tests/governance/test_step17_in_memory_stores.py · tests/governance/test_step18_restart_survival.py · tests/governance/test_step20_debt_drift_snapshot.py · tests/governance/test_step7_factory_surfaces.py · tests/governance/test_truth_matrix_identity.py · tests/governance/test_w034_runtime_state_identity.py · tests/governance/test_w036_pricing_divergence.py · tests/governance/test_w037_measurement_provenance.py · tests/governance/test_w038_probe_measure_mode.py · tests/governance/test_w042_root_name_guard.py · tests/governance/test_w048_bound_provenance.py · tests/governance/test_w051_ci_verdict_readability.py · tests/governance/test_w052_history_hash_probe.py · tests/governance/test_w053_gate_dependency_closure.py · tests/governance/test_w055_schema_inventory_drift.py · tests/governance/test_w056_sovereign_decision_status.py · tests/governance/test_w058_live_stack_precondition.py · tests/governance/test_w059_open_record_accountability.py · tests/governance/test_w061_surface_debt_trend.py · tests/governance/test_w062_mutation_probe.py · tests/governance/test_w064_services_src_fallback.py · tests/governance/test_w069_single_scanner_and_explicit_root.py · tests/governance/test_w069_status_contradiction.py · tests/governance/test_work_governance_gate.py | 2026-09-02 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، فبطلَ مضمونُ العبارةِ السابقةِ «لم يُشغَّلْ له مراجعٌ بعدُ» — وتبقى مكتوبةً شاهدةً على تاريخِها لا تُمحى.** والحكمُ: **`REJECTED` بإجماعِ المراجعَينِ** (أ `P1=1` · ب `P1=2`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ عيوبِ الجولةِ الخامسةِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ. | معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`) | — |
| WI-033 | tests-root | T0 (تتمّةُ خفضِ دَينِ `DISC-041`: المواضعُ الحرّةُ الباقيةُ تحتَ `tests/` خارجَ `tests/governance/`) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tests/constitutional/test_constitutional_cli.py · tests/constitutional/test_constitutional_engine.py · tests/crown/test_crown_truth_matrix.py · tests/crown/test_w064_secret_scan_exceptions.py · tests/sovereignty/test_crown_human_root.py · tests/sovereignty/test_enforcement_boundary.py · tests/sovereignty/test_enforcement_integration.py · tests/sovereignty/test_sovereignty_cli.py · tests/sovereignty/test_sovereignty_kernel.py | 2026-09-02 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةُ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — مراجعُ النطاقِ `tests-root` (‏`C0`) بنصِّ `OWNERSHIP.md` و`Q-43`، فلا `VERIFIED` بيدِ الكاتبِ | — |
| WI-035 | tooling-gates | T0 (‏حدُّ الصدقِ 9 في [`COMPLETION_LEDGER.md § 10`](../../audit/COMPLETION_LEDGER.md): صدقُ طوابعِ الالتزامِ يصيرُ رقمًا مقيسًا محروسًا من النموِّ · `DISC-043`) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_PROGRESS | tools/governance/commit_timestamp_integrity.py · tests/governance/test_w110_commit_stamp_integrity.py · tests/governance/test_w113_new_commit_stamp_utc.py | 2026-09-02 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، فبطلَ مضمونُ العبارةِ السابقةِ «لم يُشغَّلْ له مراجعٌ بعدُ» — وتبقى مكتوبةً شاهدةً على تاريخِها لا تُمحى.** والحكمُ: **`REJECTED` بانقسامٍ لا يُجمَعُ جمعًا حسابيًّا** (أ `VERIFIED` `P1=0` · ب `REJECTED` `P1=2`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ عيوبِ الجولةِ الخامسةِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ. | معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`) | — |
| WI-037 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-042`: خليّةُ المساراتِ تُشطَرُ على «·» فيُقرأُ الجزءُ النثريُّ دعوى، ونثرٌ يذكرُ مجلَّدًا يُغطّيه كلَّه · **استحقاق 2026-09-09**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_PROGRESS | tools/governance/check_work_governance.py · tests/governance/test_w117_claim_cell_shape.py | 2026-09-03 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، فبطلَ مضمونُ العبارةِ السابقةِ «لم يُشغَّلْ له مراجعٌ بعدُ» — وتبقى مكتوبةً شاهدةً على تاريخِها لا تُمحى.** والحكمُ: **`REJECTED` بانقسامٍ لا يُجمَعُ جمعًا حسابيًّا** (أ `VERIFIED` `P1=0` · ب `REJECTED` `P1=2` و`P3=1`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ عيوبِ الجولةِ الخامسةِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ. | معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`) | — |
| WI-036 | tooling-gates | T0 (قابليّةُ القياسِ · `DISC-045`: أرقامُ حدودِ § 10 في [`COMPLETION_LEDGER.md`](../../audit/COMPLETION_LEDGER.md) لا يُقاسُ تفرُّدُها فـ«الحدُّ 9» إحالةٌ لا تُحَلُّ) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/truth_limit_integrity.py · tests/governance/test_w115_truth_limit_integrity.py | 2026-09-03 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ مستقلّةٌ بـمجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) (‏`Q-43`) — و`VERIFIED` فعلُ المراجعِ لا الكاتبِ | — |
| WI-034 | tooling-gates | T0 (‏حدُّ الصدقِ 8 في [`COMPLETION_LEDGER.md § 10`](../../audit/COMPLETION_LEDGER.md): فخُّ منطقةِ زمنِ الالتزامِ صارَ محروسًا لا مُعلَنًا وحدَه) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/stamp_readme_identity.py · tests/governance/test_w109_commit_timestamp_timezone.py | 2026-09-02 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ — والمراجعُ مجلسُ المراجعةِ بـ`Q-43` فلا `VERIFIED` بيدِ الكاتبِ (§ 4.3 · `DISC-027` مُغلَقٌ) | — |
| WI-038 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-046`: «الحالةُ المقيسةُ الآن» تُعلِنُ حجمَ حزمةٍ متقادمًا — المكتوبُ 1748 والمقيسُ 2351 — ولا بوّابةَ تقرأُ رقمًا في نثرٍ · **استحقاق 2026-09-10**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_PROGRESS | tools/governance/suite_size_inventory.py · tests/governance/test_w120_suite_size_claims.py | 2026-09-03 | 2026-09-30 | **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، فبطلَ مضمونُ العبارةِ السابقةِ «لم يُشغَّلْ له مراجعٌ بعدُ» — وتبقى مكتوبةً شاهدةً على تاريخِها لا تُمحى.** والحكمُ: **`REJECTED` بإجماعِ المراجعَينِ** (أ `P1=3` · ب `P1=4` و`P2=1`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ عيوبِ الجولةِ الخامسةِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ. | معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`) | — |
| WI-039 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-021`: مُصنِّفُ مِرساةِ المساءلةِ يقرأُ **مسارًا مذكورًا في نثرٍ** حرسًا قائمًا، فمن كتبَ «لا حرسَ وهذانِ الملفّانِ لا يقيسانِ هذا» نالَ خُضرةً كاذبةً · **استحقاق 2026-09-11**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_PROGRESS | tools/governance/open_record_accountability.py · tests/governance/test_w124_anchor_declaration.py | 2026-09-03 | 2026-09-30 | قلبُ حقلِ `anchor` نفسِه يمسُّ `tests/governance/test_w059_open_record_accountability.py` وهو مُدَّعًى لـ`WI-033` (`IN_REVIEW`) — فنزلَت طبقةُ الإعلانِ وسقّاطتُها بلا مسِّ مُدَّعًى · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | قلبُ حقلِ `anchor` نفسِه متى تحرَّرَ حرسُ الأداةِ من دعوى `WI-033` (‏وترقيةُ الصفوفِ تمَّت في `W-126`: 25 ← 2) | — |
| WI-040 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-048`: قارئاتُ صفوفِ الجداولِ في أدواتِ الحوكمةِ تقسِمُ على محرفِ الأنبوبِ بلا تمييزِ المهروبِ، فخليّةٌ تحملُه تُزيحُ الأعمدةَ فيُحكَمُ على صفٍّ لم يُقرَأْ — أُصلِحَ موضعُ أداةِ المساءلةِ في `W-126` وبقيَ موضعانِ مقيسانِ · **استحقاق 2026-09-11**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | READY | tools/governance/check_work_governance.py · tools/governance/guard_enforcement_closure.py | 2026-09-03 | 2026-09-11 | لا عائقَ فنيًّا — ولا يُحجَزُ ما دامَ `check_work_governance.py` مُدَّعًى لـ`WI-037` (`IN_REVIEW`) · و`READY` لا تقفلُ مسارًا (§ 6.1) | حجزُ البندِ متى تحرَّرَ المسارُ الأوّلُ، ثمَّ إحكامُ القاسمَينِ المقيسَينِ بحرسٍ يُثبِتُ الفرقَ بطفرةٍ | — |
| WI-041 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-049`: إنشاءُ الالتزامِ بواجهةِ Git Data بلا تصريحِ إزاحةٍ يكتُبُ إزاحةَ المُنشِئِ المحلّيّةَ، ووجهُ القراءةِ يعرضُها `Z` فيُقرأُ سليمًا وهو ليسَ كذلك — قِيسَ في تشغيلِ CI **84** وصُحِّحَ أثرُه في `W-127` · **استحقاق 2026-09-11**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | READY | tools/governance/commit_timestamp_integrity.py · docs/PROJECT_HANDBOOK.md | 2026-09-03 | 2026-09-11 | لا عائقَ فنيًّا — والمسارانِ مُدَّعيانِ لبندَينِ `IN_REVIEW` (`WI-035` · `WI-023`) فلا يُحجَزُ قبلَ تحرُّرِهما · و`READY` لا تقفلُ مسارًا (§ 6.1) | حجزُ البندِ متى تحرَّرَ المسارانِ، ثمَّ إنزالُ وجهٍ يقيسُ إزاحةَ رأسِ الفرعِ المدفوعِ قبلَ الاعتمادِ عليه، وكتابةُ التصريحِ بالإزاحةِ في قائمةِ ما قبلَ الدفعِ | — |
| WI-042 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-050`: بوّابةُ «حدِّ سرِّ الملكِ» غيَّرَت حكمَها على العقدةِ نفسِها بلا تغييرِ حرفٍ، وسببُها لم يُقرَأْ — قِيسَ في تشغيلِ CI **86** بمحاولتَينِ · **استحقاق 2026-09-11**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | READY | .github/workflows/ci.yml · federal/executive/services/pyproject.toml | 2026-09-03 | 2026-09-11 | **`ci.yml` مقفولٌ بـ`WI-023` (`IN_REVIEW`)** فلا يُمَسُّ قبلَ تحرُّرِه · و`READY` لا تقفلُ مسارًا (§ 6.1) | عزلُ السببِ أوّلًا بقراءةِ سجلِّ الوظيفةِ من طريقٍ لا يمرُّ بمُضيفٍ محجوبٍ، ثمَّ تثبيتُ تبعيّاتِ الخطوةِ من قفلٍ لا من محيطٍ متغيِّرٍ | — |
| WI-043 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-051`: الفحصُ الذي يُثبِتُ استقرارَ الأثرِ المُولَّدِ يُسمّي ثلاثةَ مُولِّداتٍ نصًّا، فمُولِّدٌ جديدٌ لا يدخُلُ الحرسَ **ولا يُبلَّغُ عن غيابِه** — والمقيسُ 11 مُولِّدًا و4 مربوطةٌ فقط · **استحقاق 2026-09-11**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/generator_settlement_closure.py · tests/governance/test_w129_generator_settlement_closure.py | 2026-09-03 | 2026-09-30 | قُرِئَ حكمُ تشغيلِ **88** (`33778908328`) على عقدةِ الدفعِ `936f5e15` ⇒ `completed success` · **13/13** · `ci_verdict_readability` ⇒ خروجٌ 0 · `READABLE`. فلا عائقَ — والبندُ في يدِ المراجعِ · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ مستقلّةٌ ثمَّ `VERIFIED` — وذاكَ فعلُ المراجعِ لا الكاتبِ (§ 4.3 — والمراجعُ مستقلٌّ بـ`Q-43`) | — |
| WI-044 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-052`: بوّابةُ أحجامِ الحزمِ تُعلِنُ «كلُّ رقمِ حزمةٍ مكتوبٍ يُطابِقُ الجمعَ الحيَّ» ولا تقرأُ رقمَ حزمةِ الجذرِ أصلًا — فتقادَمَ **2398 مقابلَ 2421** برمزِ خروجٍ 0 · **استحقاق 2026-09-11**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | READY | tools/governance/suite_size_inventory.py · tests/governance/test_w120_suite_size_claims.py | 2026-09-03 | 2026-09-11 | المسارانِ **مُدَّعيانِ لـ`WI-038`** وحالتُه `IN_REVIEW` فلا يُحجَزانِ قبلَ تحرُّرِهما · و`READY` لا تقفلُ مسارًا (§ 6.1) | حجزُ البندِ متى تحرَّرَ المسارانِ، ثمَّ إمّا قراءةُ صيغةِ «المُجمَّعُ حيًّا» وقياسُها بـ`--collect-only`، وإمّا تضييقُ نصِّ الحكمِ فلا يُعلِنُ ما لم يُقَسْ | — |
| WI-047 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-055`: بوّابةٌ تطبعُ «ملاحظة ·» بعددٍ مقيسٍ ثمَّ تخرجُ برمزِ **0** — فالدَّينُ يُعَدُّ ولا يُرتَّجُ، وقد صعِدَ جردُ `UNWIRED_TOOL_INVENTORY` **20 ← 21** بينَ `W-130` و`W-131` بلا بوّابةٍ تُسمّيه · والمقيسُ **18 ملاحظةً عادّةً · صفرٌ محبوسةٌ · 18 بلا سقفٍ** · **استحقاق 2026-09-13**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/report_note_ratchet.py · tests/governance/test_w132_report_note_ratchet.py | 2026-09-03 | 2026-09-30 | المراجعةُ بيدِ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43`: `VERIFIED` قرارُه لا قرارُ منفِّذٍ (‏و`CLOSED` بعدَه · § 4.3) — و`DISC-027` و`RK-020` أُغلِقا بـ`Q-43` · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ مستقلّةٌ ثمَّ `VERIFIED` — وذاكَ فعلُ المراجعِ لا الكاتبِ (§ 4.3 — والمراجعُ مستقلٌّ بـ`Q-43`، و`DISC-027` و`RK-020` أُغلِقا به) | W-132 · دفعٌ مباشرٌ إلى main (`575b911`) · حكمُ تشغيلِ **91** (`33798360474`) على عقدةِ `575b911` ⇒ `completed success` · **13/13** · `READABLE` (و`ci_verdict_readability.py --from-json` ⇒ خروجٌ 0) · مُسلَّمٌ للمراجعةِ 2026-09-04 |
| WI-048 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-056`: قارئُ حكمِ CI يستدعي `/runs/{id}/jobs` **بلا تثبيتِ محاولةٍ** والواجهةُ تُرجِعُ آخرَها وحدَها ولا يكتُبُ الخرجُ أيَّ محاولةٍ قرأَ — فالتشغيلُ **94** انقلبَ `READABLE · 13/13` ← `UNREADABLE · 0/10` بإعادةِ تشغيلٍ بنيويّةٍ بلا تغييرِ حرفٍ في الشجرةِ · **استحقاق 2026-09-13**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | READY | tools/governance/ci_verdict_readability.py · tests/governance/test_w051_ci_verdict_readability.py | 2026-09-05 | 2026-09-13 | **المسارانِ مقفولانِ**: `ci_verdict_readability.py` مُدَّعًى لـ`WI-024` و`test_w051_…` مُدَّعًى لـ`WI-032` وكلاهما `IN_REVIEW` — فلا يُحجَزانِ قبلَ تحرُّرِهما، و`READY` لا تقفلُ مسارًا (§ 6.1) فلا `CLAIM_CONFLICT` | حجزُ البندِ متى تحرَّرَ المسارانِ، ثمَّ تثبيتُ رقمِ المحاولةِ في القراءةِ وكتابتُه في الخرجِ، وحرسٌ يُثبِتُ الفرقَ بطفرةٍ | — |
| WI-046 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-054`: أثرٌ مُولَّدٌ يشهدُ في متنِه أنَّ قياسَه جرى في بيئةٍ **ناقصةٍ** ولا يقرأُ تلكَ الشهادةَ حرسٌ — فوثيقةٌ معطوبةٌ تمرُّ بكلِّ بوّابةٍ برمزِ خروجٍ 0 · والمقيسُ **وثيقتانِ شاهدتانِ · صفرُ مُعلِنٍ نقصًا · صفرُ قارئٍ** · **استحقاق 2026-09-12**) | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/artifact_witness_integrity.py · tests/governance/test_w131_artifact_witness_integrity.py | 2026-09-03 | 2026-09-30 | لا عائقَ تنفيذيًّا — **الحكمُ مقروءٌ**: تشغيلُ CI **90** (`33790942381`) على عقدةِ `9da40866` ⇒ `completed success` · **13/13** · `READABLE`. والعائقُ الباقي **دورُ المراجعةِ**: المراجعُ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43` (‏`A-2` `APPROVED`) ولم يُشغَّلْ بعدُ لهذا البندِ، فلا يُكتَبُ `VERIFIED` · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ مستقلّةٌ تقرأُ الحرسَ وحدودَه المُعلَنةَ ثمَّ `VERIFIED` — والكاتبُ لا يكتبُها (§ 4.3) | — |
| WI-045 | tooling-gates | T0 (‏قابليّةُ القياسِ · `DISC-053`: السطرُ الناجحُ لوجهِ `--check` يُعلِنُ حكمًا **كلّيًّا** ولا يقولُ **كم قرأَ**، فلا يُميَّزُ «قِيسَ ألفٌ» من «قِيسَ صفرٌ» — والمقيسُ **20** جملةً كلّيّةً منها **17** بلا مقامٍ · **استحقاق 2026-09-11") | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_REVIEW | tools/governance/green_denominator_closure.py · tests/governance/test_w130_green_denominator_closure.py | 2026-09-03 | 2026-09-30 | لا عائقَ تنفيذيًّا — **الحكمُ مقروءٌ**: تشغيلُ CI **89** (`33785332367`) على عقدةِ `93db6855` ⇒ `completed success` · **13/13** · `READABLE`. والعائقُ الباقي **دورُ المراجعةِ**: المراجعُ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43` (‏`A-2` `APPROVED`) ولم يُشغَّلْ بعدُ لهذا البندِ، فلا يُكتَبُ `VERIFIED` · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | مراجعةٌ مستقلّةٌ تقرأُ الحرسَ وحدودَه المُعلَنةَ ثمَّ `VERIFIED` — والكاتبُ لا يكتبُها (§ 4.3) | — |
| WI-050 | governance-docs | T0 (قابليّةُ القياسِ — تفعيلُ A-3 + إصلاحُ إخفاقاتِ Identity Law: مزامنةُ وثائقِ الحالةِ وتصحيحُ حدِّ الصدق) | Perplexity Computer | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | docs/governance/work/THE_ROADMAP.md · docs/governance/work/DISCOVERIES.md | 2026-09-07 | 2026-09-14 | لا عائقَ فنيًّا — THE_ROADMAP.md غيرُ مُدَّعًى وDISCOVERIES.md معفيةٌ بنصِّ § 6 | تفعيلُ A-3 + تصحيحُ TRUTH_LIMIT_BASELINE + مزامنةُ PROJECT_HANDBOOK.md (واجبُ § 7) | دفعٌ مباشرٌ إلى main (`08251f8`) · حكمُ CI: **أخضرُ 13/13 success** (تشغيلُ 34159148045) · مُراجَعٌ بـ`W-143` · **مُغلَقٌ بـ`W-144`** |
| WI-051 | governance-docs | T2 | Driving H | مجلس المراجعة (GPT 5.6 + Grok 4.6) — والشقُّ `C3` (`decisions`) يحسمُه المالك | CLOSED | docs/audit/SOVEREIGN_DECISION_REGISTER.md · docs/governance/work/THE_ROADMAP.md · docs/governance/work/OWNERSHIP.md · docs/governance/work/ACTIVE_WORK.md · docs/governance/work/RISK_REGISTER.md · docs/governance/work/DISCOVERIES.md · .github/workflows/ci.yml · PROJECT_STATE.md · docs/PROJECT_HANDBOOK.md · tests/governance/test_w150_gate_enforcement_in_ci.py · tests/governance/test_w154_reviewer_consistency.py | 2026-09-08 | 2026-09-30 | — (‏فُضَّ قفلُ `WI-023` بقرارِ المالكِ `Q-44`). والباقي **حكمُ المجلسِ**: الجولتانِ الأولى والثانيةُ رُفِضَتا بإجماعٍ، والثالثةُ انقسمَت (‏المراجعُ ب `VERIFIED` · المراجعُ أ `REJECTED` بعيبٍ `P1`)، فعُولِجَ اتّحادُ عيوبِها في `W-154` · **وجُدِّدَ الحجزُ إلى 2026-09-30 بنصِّ § 6.3** — والسببُ مكتوبٌ لا مطويٌّ: البندُ لم يُسلَّمْ ولم يُشغَّلْ له مراجعٌ بعدُ، والتجديدُ **رفعُ حاجزٍ زمنيٍّ** لا إنجازٌ ولا مراجعةٌ | — (‏أُغلِقَ). ولا عملَ باقيًا في هذا البندِ: قرارُ `Q-43` مُسجَّلٌ ومُنزَلٌ في `A-2` و`OWNERSHIP.md`، و`RK-020` و`DISC-027` مُغلَقانِ، ومجلسُ المراجعةِ المستقلِّ **مُجرَّبٌ أربعَ جولاتٍ** لا مُدَّعًى. | دفعٌ مباشرٌ إلى `main` · **مُراجَعٌ بإجماعِ مجلسٍ مستقلٍّ في الجولةِ الرابعةِ** على عقدةِ `W-156` (`408e772c`) — `GPT 5.6 Sol` ⇒ `VERIFIED` `P1=0` و`Grok 4.6` ⇒ `VERIFIED` `P1=0` — و**مُعتمَدٌ `VERIFIED` بـ`W-157`** بيدِ المجلسِ لا بيدِ المؤلِّفِ (§ 4.3) · حكمُ CI على عقدةِ `W-156`: **أخضرُ 14/14 · 0 حمراءَ · 0 متخطّاةٍ** (‏التشغيلُ [`34559801140`](https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34559801140)) · وحكمُ CI على عقدةِ الاعتمادِ `W-157` (`df32bd8f`): **أخضرُ 14/14 · 0 حمراءَ · 0 متخطّاةٍ** (‏التشغيلُ [`34562272448`](https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34562272448)) · **مُغلَقٌ بـ`W-158`** |
| WI-052 | audit-truth | T0 (‏قابليّةُ القياسِ · أداءُ واجبِ § 7/6 على عقدةِ `W-158` ثمَّ تشغيلُ الجولةِ الخامسةِ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على البنودِ الستّةِ التي تقفلُ مساراتِ بنودِ `READY` الخمسةِ) | Perplexity Computer | مجلس المراجعة (GPT 5.6 + Grok 4.6) | IN_PROGRESS | docs/audit/COMPLETION_LEDGER.md · docs/governance/work/ACTIVE_WORK.md | 2026-09-13 | 2026-09-30 | لا عائقَ فنيًّا على هذا البندِ — ولا مسارَ مقفولًا يُمَسُّ. **والعائقُ البنيويُّ المقيسُ الذي أنشأَ هذا البندَ**: عشرونَ بندًا `IN_REVIEW` تقفلُ مساراتِها (§ 6.1) فتحجُبُ بنودَ `READY` الخمسةَ، والمراجعةُ فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3) **والجولةُ الخامسةُ شُغِّلَت وقُيِّدَ حكمُها في `W-161`: صفرُ بندٍ مُجمَعٌ عليه ⇒ صفرُ `VERIFIED`، فنُقِلَت الستّةُ `IN_REVIEW → IN_PROGRESS` — والعائقُ البنيويُّ المقيسُ لم يُرفَعْ: المساراتُ تبقى مقفولةً في `IN_PROGRESS` كما في `IN_REVIEW` (§ 6.1)، وبنودُ `READY` الخمسةُ تبقى محجوبةً.** | قراءةُ حكمِ CI على عقدةِ قيدِ `W-161` بالعدِّ الثلاثيِّ وبساعةِ قراءتِه، ثمَّ نقلُ البندِ `IN_PROGRESS → IN_REVIEW` في قيدٍ لاحقٍ (‏معيارُ القبولِ 9 · `DISC-060` — لا نقلَ حالةٍ قبلَ قراءةِ حكمِ عقدةِ القيدِ) | — (‏يكتبُها مَن يجبُ عليه الإغلاقُ · `DISC-010` · `DISC-030`: ذِكرُ قيدٍ أُضيفَ في مجموعةِ التغييرِ نفسِها يُشعِلُ `POST_MERGE_NOT_CLOSED` على بندٍ غيرِ مُغلَقٍ — والدليلُ لم يُخفَ: القيدُ مُسمًّى بعينِه ورقمِه في كتلةِ التفاصيلِ أدناه، وصفُّه في § 8 يُسمّي هذا البندَ نصًّا) |
| WI-049 | audit-truth | T0 (قابليّةُ القياسِ · خطُّ أساسِ المستودعِ الجديدِ: قياسُ حالةِ CI على `vooovg-ui/AMOS-Fedration` · المستودعُ نُسِخَ من `xoos-beep` وحسابُ `Actions` فيه جديدٌ · `DISC-006` كانَ على حسابِ المالكِ القديمِ) | Perplexity Computer | المالك (`A-2` · غيرُ مستقلٍّ) | CLOSED | docs/governance/work/ACTIVE_WORK.md · docs/audit/COMPLETION_LEDGER.md | 2026-09-07 | 2026-09-14 | لا عائقَ فنيًّا — ولا مسارَ مقفولًا يُمَسُّ — ووثيقتا الحالةِ تُمَسّانِ بسطرِ قيدٍ معفىٍ بنصِّ § 6 | دفعُ التسجيلِ إلى main لإحراكِ CI ثمَّ قراءةُ الحكمِ وتقييدُه | دفعٌ مباشرٌ إلى main (`95f0fc3`) · حكمُ CI: **أوّلُ تشغيلٍ READABLE · 13/13** (تشغيلُ 34148407884) · مُراجَعٌ بـ`W-143` · **مُغلَقٌ بـ`W-144`** |

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
بدأ: 2026-08-25        ينتهي الحجز: 2026-08-31
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
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-051 · دفعٌ مباشرٌ إلى main (`9561d9a`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
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
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-052 · دفعٌ مباشرٌ إلى main (`3cea7f3`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
قيدُ السجلّ: W-050
```

---

### WI-006 — مقروئيّةُ حكمِ CI تُقاسُ بالخطواتِ لا بالنتيجةِ (حرسُ `RK-011` شِفرةً)

```text
النطاق: tooling-gates
المسار/المرحلة: T0 / T2 (صدقُ الشاهدِ · حرسٌ مُنفَّذٌ لا وثيقةٌ)
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه غائبٌ ولا يُطوى**: لا تشغيلَ واحدًا على `9561d9a` (‏`DISC-006` · دقائقُ الحسابِ السابقِ)، فلم يُشاهَدْ حكمٌ يومَ الدمجِ. والحكمُ المقروءُ اليومَ **أخضرُ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
  - `IN_REVIEW` لا `CLOSED`: لم يُدمَجْ بعدُ، وإغلاقُه قبلَ الدمجِ دعوى لا قيد (‏وهو خلافُ ما فعلَه `WI-003`/`WI-004`/`WI-005` — أُغلِقت في دفعتِها لأنَّ القيدَ كان قيدَ دمجٍ قد وقع)
  - `VERIFIED` غيرُ مُتاحٍ: يلزمُه مراجعٌ مستقلٌّ، وتسميتُه قرارٌ سياديٌّ معلَّقٌ (`A-2`)
  - `الأداةُ تحرسُ **معيارَ** القراءةِ لا **حالةَ** CI: ولا تُنشِئُ شاهدًا، ولا تُغني عن تشغيلٍ يُنفَّذُ فعلًا
  - **فحصانِ قائمانِ حُوِّلا بصدقٍ ولم يُحذَفا ولم يُضعَّفا**: `test_guarded_count_is_eight_of_ten` و`test_guarded_count_matches_the_registry` كانا يُثبِّتانِ «10 مقيَّدًا · 2 مُعلَنًا» **بالمساواةِ**، فكانا يسقُطانِ على إضافةِ قياسٍ مشروعٍ لا على تخفيفِ حرسٍ. فصارا **ترباسًا**: الكلُّ يرتفعُ · والمحروسُ لا ينقُصُ (≥ 8) · والمُعلَنُ بلا حرسٍ لا يتكاثرُ (≤ 3) · وكلُّ مُعلَنٍ له سببٌ مكتوبٌ
  - **والثمنُ يُعلَنُ لا يُطوى**: المُعلَنُ بلا حرسٍ ارتفعَ **من 2 إلى 3** — وذاك ثمنُ قياسٍ يلزمُه واجهةٌ حيّةٌ، لا رخصةٌ لرابعٍ
  - واجبُ ما بعدَ الدمجِ لـ`W-048`/`W-049`/`W-050` **يبقى مفتوحًا**: أوّلُ عملٍ يُشاهِدُ تشغيلًا نُفِّذَ فعلًا يُقيِّدُ حكمَه
قيدُ السجلّ: W-051 · دفعٌ مباشرٌ إلى main (`9561d9a`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
```

---

### WI-007 — مِسبرُ بصماتِ السجلِّ يقرأُ التاريخَ كلَّه أو يرفضُ — ولا يقولُ «ليسَ في السجلِّ» بلا حقٍّ

```text
النطاق: tooling-gates
المسار/المرحلة: T0 (صدقُ القياسِ نفسِه · واجبٌ مُعلَنٌ منذُ `W-037` يُوفَّى)
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه غائبٌ ولا يُطوى**: لا تشغيلَ واحدًا على `3cea7f3` (‏`DISC-006` · دقائقُ الحسابِ السابقِ)، فلم يُشاهَدْ حكمٌ يومَ الدمجِ. والحكمُ المقروءُ اليومَ **أخضرُ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
  - **هذا إصلاحُ قاعدةِ قياسٍ لا إصلاحُ دَينٍ**: عدّادُ الدَّينِ 182 كما كانَ، والأسئلةُ 42 كما كانَت — ولا قدرةَ جديدةَ في المنتَجِ
  - **والعطبُ ليسَ مفترَضًا كلُّه**: `main` اليومَ **270 التزامًا** وأعمقُ بصمةٍ مذكورةٍ `0111c95` عندَ العمقِ **135** — فالهامشُ 265 التزامًا قبلَ أن تبدأَ النافذةُ القديمةُ بالكذبِ. **لكنَّ العيبَينِ الآخرَينِ كانا يكذِبانِ اليومَ فعلًا**: بصمتانِ من أربعينَ خانةً (`024f8ab1…` · `6a86205c…`) لم تُفحَصا قطُّ — 43 مذكورةً والمقروءُ 41
  - **ومخرَجُ بيئتي ليسَ حكمًا على المستودعِ**: شجرتي مُوَطَّنةٌ من `tarball` بقيدٍ مُصطنَعٍ واحدٍ، فيقولُ المِسبرُ عندي `43 من 43` ليسَ في السجلِّ — **وذاك صدقٌ عن شجرتي لا عن `main`**؛ والحكمُ الصادقُ يلزمُه نسخٌ كاملُ العمقِ في CI
  - **والقياسُ لم يُقَدْ بـCI**: لا تشغيلَ منفَّذًا في المستودعِ منذُ 2026-08-26T23:05:02Z (`DISC-006` بيدِ المالكِ) — **فلا يُدَّعى أنَّ الشجرةَ خضراءُ**
  - `VERIFIED` غيرُ مُتاحٍ: يلزمُه مراجعٌ مستقلٌّ وتسميتُه قرارٌ سياديٌّ معلَّقٌ (`A-2`)، و`CLOSED` قبلَ الدمجِ دعوى لا قيدٌ
  - **وتسجيلُ `tools/audit` في `OWNERSHIP.md` فعلٌ إداريٌّ تأمرُ به القاعدةُ 3 لا اجتهادٌ منِّي**، وأُلحِقَ بأقربِ نطاقٍ جنسًا لا بنطاقٍ مُبتدَعٍ — **وللمالكِ نقضُه وإعادةُ توزيعِه**
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-064 · دمجُ #6 (`17ab3c4`) · حكمُ CI: أخضرُ 13/13 (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-063 · دمجُ #5 (`0803ae2`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33278721516 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-062 · دمجُ #4 (`3356d71`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33278679341 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-061 · دمجُ #3 (`7f6ccf1`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33251600117 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-060 · دمجُ #2 (`6a7e571`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33219913887 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-059 · دمجُ #1 (`764a3dc`) · حكمُ CI على عقدتِه: **أحمرُ** (تشغيلُ 33217559878 · سببُه `DISC-024` عُولِجَ في `W-064`) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-058 · دفعٌ مباشرٌ إلى main (`eafc38e`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-057 · دفعٌ مباشرٌ إلى main (`9c05ed8`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-056 · دفعٌ مباشرٌ إلى main (`3e9ee6a`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-055 · دفعٌ مباشرٌ إلى main (`978638f`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
قيدُ السجلّ: W-052 · دفعٌ مباشرٌ إلى main (`3cea7f3`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
```

---

### WI-020 — قرارُ `A-2` يُقيَّدُ في § 16 بحدِّه، ثمَّ يُوفَّى واجبُ § 7 لأربعةَ عشرَ بندًا

```text
النطاق: governance-docs
المسار/المرحلة: T0 / T2 (قرارٌ سياديٌّ يُقيَّدُ لا يُصنَعُ · وواجبٌ مُعلَّقٌ يُوفَّى بعدَه)
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
المسارات:
  docs/governance/work/THE_ROADMAP.md              (§ 16: صفُّ `A-2` وتاريخُه، و§ 16.5 نصُّ القرارِ وحدُّه)
  tools/governance/check_work_governance.py        (نصُّ سببِ الإبلاغِ وحدَه — لا حكمٌ ولا حدٌّ يُمَسّ)
  PROJECT_STATE.md                                 (موضعُ الحالةِ من السجلِّ § 7 واجب 4 · وتصحيحُ عنوانِ المستودعِ المُعلَنِ)
  docs/PROJECT_HANDBOOK.md                         (تاريخُ آخرِ تعديلٍ وأحدثُ قيدٍ — § 7 واجب 4)
  tests/governance/test_w054_post_merge_reverse_link.py (فحصٌ كانَ يقرأُ المستودعَ الحقيقيَّ فاحمَرَّ من الإصلاحِ — `DISC-032`: يُصلَحُ ليقرأَ شجرتَه، ولا يُخفَّفُ ولا يُحذَفُ)
  وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ: ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md
  وترتيبُ الالتزامِ مُعلَنٌ لا مستورٌ: قيدُ `A-2` وإغلاقُ الأربعةَ عشرَ في **الالتزامِ نفسِه**، لأنَّ `WI-009` كان حاجزًا على المسارَينِ أعلاه وهو `IN_REVIEW`؛ فلو سُجِّلَ هذا البندُ قبلَ إغلاقِه أسقطَتِ البوّابةُ `CLAIM_CONFLICT` بحقٍّ، ولو أُغلِقَ قبلَ قيدِ `A-2` أُغلِقَ بمعرفةٍ في رأسِ شخصٍ (§ 2 حكم 14)
خارجَ النطاق:
  - لا يُصنَعُ قرارٌ سياديٌّ ولا يُؤوَّلُ: نصُّ المالكِ يُنقَلُ إلى § 16.5 كما وردَ، ولا يُزادُ عليه تفويضٌ لم يُنطَقْ (§ 2 حكم 12)
  - لا يُعتمَدُ `A-3` ولا يُستنتَجُ من `A-2`: بوّابةُ الإسقاطِ تبقى إبلاغًا، والقرارُ للمالكِ
  - لا يُحَلُّ `ADVISORY_BASIS_EXPIRED` (`DISC-017`): سندُ § 16.4 معلَّقٌ على «PROPOSED» والوثيقةُ `ACTIVE` — نصُّ § 16.4 قرارُ المالكِ لا تصحيحُ منفِّذٍ
  - لا يُغيَّرُ حكمُ بوّابةٍ ولا حدُّها ولا عتبتُها: المُمَسُّ في `check_work_governance.py` **نصُّ سببٍ يُطبَعُ** لا شرطُ إسقاطٍ
  - لا يُغلَقُ `DISC-027` ولا `RK-020` باعتمادِ القرارِ: الاستقلالُ المنتفي حقيقةٌ قائمةٌ حتّى يُعَيَّنَ مراجعٌ ليسَ هو المالكَ
  - لا يُنقَلُ بندٌ إلى `CLOSED` لخُضرةِ CI وحدَها: الخُضرةُ شرطٌ من شروطٍ لا دليلُ إغلاقٍ
  - ولا يُغلَقُ هذا البندُ في دفعتِه: حكمُ CI عليه لم يُقرَأْ بعد (§ 7 واجب 6 · سابقةُ `W-040`)
معيارُ القبول:
  1. `A-2` يُقرأُ من الجدولِ `APPROVED` بتاريخٍ غيرِ مستقبليٍّ، بلا `APPROVED_WITHOUT_DATE` ولا `DECISION_DATE_IN_FUTURE` ولا `UNKNOWN_DECISION_STATUS` ولا `DANGLING_DECISION_REF`
  2. حدُّ القرارِ مكتوبٌ في الوثيقةِ الحاكمةِ نفسِها (§ 16.5) نصًّا يقولُ إنَّ المراجعةَ **ليست مستقلَّةً**، لا في قيدٍ عارضٍ
  3. أربعةَ عشرَ بندًا كانت `IN_REVIEW` وقيودُها مدموجةٌ تمرُّ بـ`VERIFIED` في الدفعةِ الأولى ثمَّ إلى `CLOSED` في الدفعةِ التاليةِ (§ 4.3 لا يُجيزُ الوثبَ)، ولكلٍّ عندَ الإغلاقِ في «قيدِ السجلّ» ثلاثةٌ: `W-###` · عقدةُ الدمجِ · **حكمُ CI على عقدتِه كما كانَ** (غائبًا أو أحمرَ أو أخضرَ) لا كما يُرجى
  4. لكلِّ بندٍ مُغلَقٍ سطرُ مراجعةٍ يذكرُ أنَّ الدليلَ **أُعيدَ تشغيلُه** عندَ الرأسِ ورمزَ خروجِه، وأنَّ الأرقامَ المُعلَنةَ لقطاتٌ زمنيّةٌ لا عقدٌ
  5. `check_work_governance.py --self-check --enforce-post-merge` يخرُجُ **بصفرٍ بعدَ دفعةِ الإغلاقِ** لا قبلَها: الرقمُ كان 14 قبلَ العملِ، ويبقى 14 في دفعةِ `VERIFIED` **وذلك صحيحٌ يُعلَنُ لا يُخفى**، ثمَّ يصيرُ صفرًا حينَ يُغلَقُ الأربعةَ عشرَ
  6. نصُّ سببِ الإبلاغِ في الأداةِ لا يقولُ «`A-2` معلَّقٌ» بعدَ اعتمادِه: يُقاسُ بأنَّ العبارةَ لم تبقَ في الشِفرةِ
  7. البوّاباتُ كلُّها خضراءُ كما كانت، وعدّادُ المخالفاتِ 63 لم يرتفعْ، والانحدارُ كاملًا بلا نقصٍ
الدليلُ المطلوب:
  python tools/governance/sovereign_decision_status.py                                  # A-2 · APPROVED · 2026-08-30 · خروجٌ 0
  python tools/governance/check_work_governance.py --self-check                         # صفرُ مخالفاتٍ · ولا ملاحظةَ POST_MERGE_NOT_CLOSED
  python tools/governance/check_work_governance.py --self-check --enforce-post-merge    # 1 بـ14 في دفعةِ VERIFIED · 0 بعدَ دفعةِ الإغلاقِ
  python tools/governance/check_completion_ledger.py --staged                           # صفرُ مخالفاتٍ
  python tools/governance/state_document_drift.py                                       # صفرُ انحرافٍ
  python tools/governance/open_record_accountability.py                                 # كلُّ قيدٍ مفتوحٍ له مِرساةٌ
  pytest tests/governance -q                                                            # حرسُ الحوكمةِ كاملًا
  pytest tests/ -q                                                                      # الانحدارُ كاملًا
  python tools/governance/truth_audit.py . --ratchet                                    # 63 لم يرتفعْ
  ruff check .
بدأ: 2026-08-30        ينتهي الحجز: 2026-09-06
العائق: —
الخطوةُ التالية: — (مُغلَقٌ · § 7 وُفِّيَ)
حدُّ البندِ — مُعلَنٌ لا مطويّ:
  - **هذا قيدُ قرارٍ لا صناعتُه**: القرارُ حسمَه المالكُ نصًّا في 2026-08-30، وعملُ هذا البندِ نقلُه إلى السجلِّ الحاكمِ بحدِّه (§ 2 حكم 14: ما لم يُكتَبْ فليس حالةَ المشروعِ)
  - **والاستقلالُ منتفٍ لا مُدَّعًى**: أربعةَ عشرَ بندًا تمرُّ `IN_REVIEW → VERIFIED → CLOSED` بمراجعٍ هو المالكُ نفسُه، فقيمةُ `VERIFIED` هنا **إعادةُ تشغيلِ دليلٍ ومطابقةُ معيارٍ** لا شهادةُ عينٍ ثانيةٍ (`DISC-027` · `RK-020`)
  - **وحكمُ CI على عقدِ دمجِ ثلاثةَ عشرَ منها لم يكنْ أخضرَ**: ثمانيةٌ بلا تشغيلٍ أصلًا (`DISC-006`)، وخمسةٌ بتشغيلٍ **أحمرَ** لسببٍ واحدٍ مُقيَّدٍ عُولِجَ في `W-064`. والإغلاقُ يستندُ إلى خُضرةِ **حالةِ الدولةِ** (`17ab3c4` ⇒ 13/13) لا إلى خُضرةِ عقدِها، وهذا **حدٌّ مُعلَنٌ ومقيسٌ** لا مطويٌّ (`DISC-028`)
  - **ولم يُفعَّلْ إسقاطٌ**: `--enforce-post-merge` يصيرُ صفرًا يومَ يُوفَّى الواجبُ (دفعةُ الإغلاقِ) **لا** لأنَّ الحرسَ صارَ مُسقِطًا افتراضًا؛ وجعلُه افتراضًا يُحمِّرُ نافذةَ التزامٍ واحدٍ بينَ الدمجِ والإغلاقِ، وذاك قرارُ `A-3` لا اجتهادُ منفِّذٍ (`DISC-030`)
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ أعلاه عندَ الرأسِ بمُفسِّرِ 3.12 ذاتِه، والمعاييرُ السبعةُ طُوبِقَت واحدًا واحدًا — ومنها المعيارُ الخامسُ: `--enforce-post-merge` كانَ **1 بـ14 مخالفةً** في دفعةِ `VERIFIED` (`W-065`) وصارَ **0** بعدَ إغلاقِ الأربعةَ عشرَ في `W-067`، فالواجبُ وُفِّيَ ولم يُخفَّفْ حرسٌ.
  - **وحكمُ CI على عقدةِ دفعِ هذا البندِ قُرِئَ ولم يُطوَ**: `bdfc1db` ⇒ **أحمرُ** (تشغيلُ 33312805372 · 12/13) بعَطبِ قياسٍ قُيِّدَ `DISC-033`، ثمَّ `04415f4` ⇒ **أخضرُ 13/13** (تشغيلُ 33315225633) بعدَ إصلاحِ سببِه. فالحمرةُ مُقيَّدةٌ كما تُقيَّدُ الخُضرةُ.
  - `VERIFIED` لا `CLOSED`: § 4.3 لا يُجيزُ الوثبَ، وحكمُ CI على عقدةِ `W-067` — وهي الدفعةُ التي أوفَتِ الواجبَ — لم يُقرَأْ بعدُ (§ 7 واجب 6 · سابقةُ `W-040`).
  - **مُغلَقٌ 2026-08-30 بـ`W-068`**: حكمُ CI على عقدةِ وفاءِ الواجبِ `12a3df7` قُرِئَ **أخضرَ 13/13** (تشغيلُ 33316791473)، فتحقَّقَ المعيارُ السادسُ والسابعُ معًا. **وسلسلةُ الأحكامِ الثلاثةِ مُقيَّدةٌ كما كانت لا كما يُرجى**: `bdfc1db` أحمرُ 12/13 · `04415f4` أخضرُ 13/13 · `12a3df7` أخضرُ 13/13.
  - **وإغلاقُ أربعةَ عشرَ بندًا لا يعني أنَّ ما فيها من عَطبٍ زالَ**: `DISC-021` و`DISC-022` و`DISC-014` وغيرُها تبقى مفتوحةً بمالكيها، وإغلاقُ البندِ إغلاقُ **عملِه** لا إغلاقُ اكتشافاتِه
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-054 · دفعٌ مباشرٌ إلى main (`aedd379`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
قيدُ السجلّ: W-065 · دفعٌ مباشرٌ إلى main (`bdfc1db`) وإتمامٌ في `04415f4` و`12a3df7` · حكمُ CI على عقدةِ القيدِ: **أحمرُ** 12/13 (تشغيلُ 33312805372) بعَطبِ قياسٍ قُيِّدَ `DISC-033` وأُصلِحَ في `W-066`، ثمَّ **أخضرُ 13/13** على `04415f4` (تشغيلُ 33315225633) وعلى عقدةِ وفاءِ الواجبِ `12a3df7` (تشغيلُ 33316791473) · مُراجَعٌ ومُغلَقٌ 2026-08-30 بـ`W-068`
```

---

### WI-019 — الحكمُ الأحمرُ يُقرأُ أوّلًا ثمَّ يُخضَّرُ من سببِه لا من قياسِه

```text
النطاق: tooling-gates
المسار/المرحلة: T0 — قابليّةُ القياسِ: حكمُ CI يصيرُ مقروءًا ومُخضَّرًا بإصلاحِ السببِ
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
المسارات:
  tools/crown/secret_scan_exceptions.py          — سجلُّ استثناءاتِ التاريخِ، مسارٌ جديدٌ لم يُحجَزْ
  tests/crown/test_w064_secret_scan_exceptions.py — حرسُ السجلِّ، مسارٌ جديدٌ كذلك
  tools/crown/verify_secret_boundaries.py        — تُوصَلُ بوّابةُ التاريخِ بالسجلِّ وتُزادُ بوّابةُ إعفاءٍ ميتٍ
  tests/sovereignty/test_outbox.py               — الفتيلُ: كتلةُ PEM المكتوبةُ حرفًا تُبنى بالتركيبِ
  docs/security/SECRET_BOUNDARIES.md             — عددُ البوّاباتِ ووصفُ السجلِّ يُطابِقانِ التنفيذَ
  conftest.py                                    — حزمةُ الخدماتِ تُرى من شجرتِها إن لم تُركَّبْ (‏`DISC-026`)
  tests/governance/test_w064_services_src_fallback.py — حرسُ ذلك الشرطِ، مسارٌ جديدٌ
  .github/workflows/ci.yml                       — تجهيزُ بيئةِ القياسِ من سببِها: تبعياتُ
    حزمةِ الخدماتِ في وظيفةِ السيادةِ (`DISC-026`) · تاريخٌ كاملٌ في وظيفةِ التاجِ لتُقاسَ
    بوّابةُ الاستثناءِ الميتِ · مرجعٌ محليٌّ لـ«main» في وظيفتَي الهُويّةِ والحزمِ العابرةِ
    (`DISC-025`). **مسارٌ كان محجوزًا** (`DISC-006`) ومُسَّ بأمرِ المالكِ الصريحِ، ولا
    يحملُ تخفيفَ حارسٍ ولا رفعَ بوّابةٍ — والتغييرُ كلُّه تجهيزُ بيئةٍ
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI مُشاهَدٌ على عقدةِ دمجِه نفسِها**: تشغيلُ `33306534739` على `17ab3c4` ⇒ **13/13 ناجحةً وكلُّها بخطواتٍ** (`READABLE`)، وتشغيلُ `33308285078` على `3e10398` ⇒ 13/13 كذلك.
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
  يُخضِّرُ هذا البندُ وظيفتَينِ سقطَتا بسببٍ واحدٍ مقيسٍ، **ولا يَزعُمُ** أنَّ المستودعَ صارَ
  بلا عَطبٍ: الحكمُ صارَ مقروءًا فصارَ ما فيه من حمرةٍ يُقرأُ ويُصلَحُ واحدةً واحدةً.
  والاستثناءُ المُعلَنُ لا يُطهِّرُ التاريخَ، بل يُعلِنُ أنَّ نصًّا بعينِه رُوجِعَ فلم يكنْ سرًّا.
```

---

### WI-018 — دعاوى الطفرةِ في القيودِ السابقةِ تصيرُ مُسجَّلةً ومقيسةً

```text
النطاق: tooling-gates
المسار/المرحلة: T0 — قابليّةُ القياسِ: «هذا الحرسُ مُجرَّبٌ بطفرةٍ» في قيدٍ مُقفَلٍ يصيرُ رقمًا يُعادُ
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه كانَ أحمرَ ولا يُطوى**: تشغيلُ `33278721516` على `0803ae2` سقطَ بوظيفتَي الأسرارِ لسببٍ مُقيَّدٍ لا يخصُّ عملَ البندِ (`DISC-024`: كتلةُ `PRIVATE KEY` حرفًا في فحصٍ سالبٍ)، وعُولِجَ سببُه في `W-064`؛ ثمَّ قُرِئَ الحكمُ **أخضرَ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
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
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه كانَ أحمرَ ولا يُطوى**: تشغيلُ `33278679341` على `3356d71` سقطَ بوظيفتَي الأسرارِ لسببٍ مُقيَّدٍ لا يخصُّ عملَ البندِ (`DISC-024`: كتلةُ `PRIVATE KEY` حرفًا في فحصٍ سالبٍ)، وعُولِجَ سببُه في `W-064`؛ ثمَّ قُرِئَ الحكمُ **أخضرَ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
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
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه كانَ أحمرَ ولا يُطوى**: تشغيلُ `33251600117` على `7f6ccf1` سقطَ بوظيفتَي الأسرارِ لسببٍ مُقيَّدٍ لا يخصُّ عملَ البندِ (`DISC-024`: كتلةُ `PRIVATE KEY` حرفًا في فحصٍ سالبٍ)، وعُولِجَ سببُه في `W-064`؛ ثمَّ قُرِئَ الحكمُ **أخضرَ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
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
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه كانَ أحمرَ ولا يُطوى**: تشغيلُ `33219913887` على `6a7e571` سقطَ بوظيفتَي الأسرارِ لسببٍ مُقيَّدٍ لا يخصُّ عملَ البندِ (`DISC-024`: كتلةُ `PRIVATE KEY` حرفًا في فحصٍ سالبٍ)، وعُولِجَ سببُه في `W-064`؛ ثمَّ قُرِئَ الحكمُ **أخضرَ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
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
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه كانَ أحمرَ ولا يُطوى**: تشغيلُ `33217559878` على `764a3dc` سقطَ بوظيفتَي الأسرارِ لسببٍ مُقيَّدٍ لا يخصُّ عملَ البندِ (`DISC-024`: كتلةُ `PRIVATE KEY` حرفًا في فحصٍ سالبٍ)، وعُولِجَ سببُه في `W-064`؛ ثمَّ قُرِئَ الحكمُ **أخضرَ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
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
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه غائبٌ ولا يُطوى**: لا تشغيلَ واحدًا على `eafc38e` (‏`DISC-006` · دقائقُ الحسابِ السابقِ)، فلم يُشاهَدْ حكمٌ يومَ الدمجِ. والحكمُ المقروءُ اليومَ **أخضرُ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
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
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **تسليمُ مسارٍ مُعلَنٌ (§ 6.4) بتاريخِ 2026-08-30**: `PROJECT_STATE.md` · `docs/PROJECT_HANDBOOK.md` سُلِّمَت إلى `WI-020`، لأنَّ عملَ هذا البندِ مدموجٌ وحجزُه صارَ **قُفلًا قائمًا على عملٍ منتهٍ** يمنعُ تحديثَ وثائقِ الحالةِ الواجبَ في § 7 واجب 4 وتصحيحَ عنوانِ مستودعٍ مُعلَنٍ خطأً. والتسليمُ طريقٌ مُعلَنٌ في § 6.1 («يُقسَمُ البندُ أو يُستلَم») لا تجاوزٌ للحجزِ، ولا يُنقَصُ به شيءٌ من دليلِ هذا البندِ ولا من حدِّه.
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه غائبٌ ولا يُطوى**: لا تشغيلَ واحدًا على `9c05ed8` (‏`DISC-006` · دقائقُ الحسابِ السابقِ)، فلم يُشاهَدْ حكمٌ يومَ الدمجِ. والحكمُ المقروءُ اليومَ **أخضرُ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
  الأداةُ تُثبِتُ أنَّ وثيقتَي الحالةِ تذكرانِ أحدثَ قيدٍ مكتوبٍ في § 8 وأنَّ تاريخَهما مُعلَنٌ غيرُ مستقبليٍّ.
  ولا تُثبِتُ أنَّ وصفَهما لذلكَ القيدِ صادقٌ، ولا ترى وثيقةً تُعلِنُ حالةً ولم تُدرَجْ في القائمةِ المُعلَنةِ،
  ولا تُحصي دعوى حالةٍ في ملفٍّ غيرِ ماركداونَ. وهذه حدودٌ مكتوبةٌ لا مطويّةٌ، ومحلُّ خطرِها `RK-018`.
```

---

### WI-011 — حالةُ القرارِ السياديِّ تصيرُ رقمًا يُقاسُ، لا فقرةً تُروى في ردٍّ

```text
النطاق: audit-truth
المسار/المرحلة: T0 — شرطُ الخروجِ «أن يُنتِجَ أيُّ عاملٍ الرقمَ نفسَه بأمرٍ واحدٍ»، مُنزَّلًا على جدولِ § 16
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه غائبٌ ولا يُطوى**: لا تشغيلَ واحدًا على `3e9ee6a` (‏`DISC-006` · دقائقُ الحسابِ السابقِ)، فلم يُشاهَدْ حكمٌ يومَ الدمجِ. والحكمُ المقروءُ اليومَ **أخضرُ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
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
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه غائبٌ ولا يُطوى**: لا تشغيلَ واحدًا على `978638f` (‏`DISC-006` · دقائقُ الحسابِ السابقِ)، فلم يُشاهَدْ حكمٌ يومَ الدمجِ. والحكمُ المقروءُ اليومَ **أخضرُ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
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
  - **مُغلَقٌ 2026-08-30 بـ`W-067`، وحالةُ هذه الكتلةِ صُحِّحَت في `W-069`**: كانَ الصفُّ يقولُ `CLOSED` وهذه الكتلةُ تقولُ `VERIFIED` — حالتانِ مكتوبتانِ لبندٍ واحدٍ إحداهما كاذبةٌ، ومرَّتا لأنَّ الحرسَ كانَ يقرأُ الصفَّ وحدَه (`DISC-035`؛ والحرسُ صارَ يقيسُ الاتفاقَ بـ`STATUS_CONTRADICTION`). ودليلُ الإغلاقِ كما هو مُقيَّدٌ في الصفِّ: W-053 · دفعٌ مباشرٌ إلى main (`84969a9`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
قيدُ السجلّ: W-055 · دفعٌ مباشرٌ إلى main (`978638f`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
```

---

### WI-009 — حرسُ ما بعدَ الدمجِ يُقاسُ من خارجِ يدِ المحروس، وحدُّه يُكتَبُ حيثُ أُحيلَ إليه

```text
النطاق: tooling-gates
المسار/المرحلة: T0 / T2 (صدقُ الشاهدِ · حرسٌ مُنفَّذٌ لا وثيقةٌ)
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **تسليمُ مسارٍ مُعلَنٌ (§ 6.4) بتاريخِ 2026-08-30**: `tools/governance/check_work_governance.py` · `tests/governance/test_w054_post_merge_reverse_link.py` · `docs/governance/work/THE_ROADMAP.md` سُلِّمَت إلى `WI-020`، لأنَّ عملَ هذا البندِ مدموجٌ وحجزُه صارَ **قُفلًا قائمًا على عملٍ منتهٍ** يمنعُ قيدَ قرارِ `A-2` في الخارطةِ وإصلاحَ نصِّ سببٍ صارَ كاذبًا بعدَ اعتمادِه. والتسليمُ طريقٌ مُعلَنٌ في § 6.1 («يُقسَمُ البندُ أو يُستلَم») لا تجاوزٌ للحجزِ، ولا يُنقَصُ به شيءٌ من دليلِ هذا البندِ ولا من حدِّه.
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه غائبٌ ولا يُطوى**: لا تشغيلَ واحدًا على `aedd379` (‏`DISC-006` · دقائقُ الحسابِ السابقِ)، فلم يُشاهَدْ حكمٌ يومَ الدمجِ. والحكمُ المقروءُ اليومَ **أخضرُ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
  - **الحرسُ يقيسُ حضورَ القيدِ في فرعِ الدولةِ لا واقعةَ الدمجِ**: دمجٌ بلا قيدٍ لا يُدرِكُه هذا الحرسُ (وذاك لـ`ledger-gate`)
  - **القيودُ التي لا تُعلِنُ بندَها رابطًا خارجَ القياسِ**: `W-046`…`W-050` مثلًا. وجعلُ الإعلانِ إلزامًا يلزمُه تصحيحُ قيودٍ ماضيةٍ — قرارُ المالكِ لا فعلُ منفِّذٍ (`DISC-010`)
  - **الإسقاطُ لم يُفعَّلْ**: لأنَّ الواجبَ نفسَه غيرُ مُستطاعٍ الآنَ (`DISC-012`)، وإسقاطٌ على ما لا يُستطاعُ عقوبةٌ لا حرسٌ. والإبلاغُ مسموعٌ في كلِّ تشغيلٍ
  - **إصلاحُ ختمِ `docs/audit/measurements/README.md`** جرى في هذا العملِ (مسارٌ مُعفًى من الحجزِ ومولَّدٌ آليًّا) وهو **مذكورٌ في مساراتِ `WI-006` المحجوزةِ** — فلم يُطلَبْ له حجزٌ ولم يُنقَلْ إلى هذا البندِ: أُصلِحَ ختمٌ ولم يُكتَبْ مضمونٌ (`DISC-011`)
  - **أحكامُ CI على الدمجاتِ لم تُشاهَدْ**: عشرةُ تشغيلاتٍ لدمجاتِ `#20`…`#24` كلُّها `UNREADABLE` بقياسِ `ci_verdict_readability.py` — فواجبُ § 7 (6) يبقى مفتوحًا لا مُؤدًّى، وسببُه `DISC-006` بيدِ المالك
قيدُ السجلّ: W-054 · دفعٌ مباشرٌ إلى main (`aedd379`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
```

---

### WI-008 — بوّابةٌ لا تستوردُ ما لا يُثبَّتُ لها: إغلاقُ التبعيّاتِ يُقاسُ بالوظيفةِ لا بالنيّة

```text
النطاق: tooling-gates
المسار/المرحلة: T0 (صدقُ القياسِ نفسِه · تخفيفُ `RK-010` يُنفَّذُ شِفرةً)
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
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
الخطوةُ التالية: يُنقَلُ إلى `CLOSED` في الالتزامِ التاليِ بعدَ قراءةِ حكمِ CI — § 4.3 لا يُجيزُ الوثبَ من `IN_REVIEW`
حدُّ البندِ — مُعلَنٌ لا مطويّ:
  - **مُراجَعٌ 2026-08-30 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ في هذا البندِ عندَ الرأسِ `3e10398` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ بمعيارِ القبولِ لا بكتابةِ صاحبِه. **والأرقامُ المُعلَنةُ في «الدليلُ المطلوب» لقطاتٌ زمنيّةٌ**: ما تغيَّرَ منها بنموِّ السجلّاتِ قُيِّدَ في `W-065` رقمًا رقمًا، والمعيارُ المحقَّقُ هو القدرةُ ورمزُ الخروجِ لا مساواةُ اللقطةِ.
  - **حكمُ CI على عقدةِ دمجِه غائبٌ ولا يُطوى**: لا تشغيلَ واحدًا على `84969a9` (‏`DISC-006` · دقائقُ الحسابِ السابقِ)، فلم يُشاهَدْ حكمٌ يومَ الدمجِ. والحكمُ المقروءُ اليومَ **أخضرُ 13/13** على `17ab3c4` الحاملِ لشِفرةِ البندِ كلِّها. فالإغلاقُ يستندُ إلى خُضرةِ حالةِ الدولةِ لا إلى خُضرةِ عقدتِه — وذاك **حدٌّ مُعلَنٌ** (`DISC-028`).
  - **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ **مُنتفٍ ومُسجَّلٌ** لا مُدَّعًى (`DISC-027`).
  - **هذا حرسُ قياسٍ لا إصلاحُ عطبٍ**: العطبُ الذي كشفَه ما زالَ قائمًا في `ci.yml` — والأداةُ تُبقي الشجرةَ خضراءَ لأنَّه **مُقيَّدٌ في أساسٍ مُوجَّهٍ**، لا لأنَّه زالَ
  - **والعطبُ مقيسٌ لا مُستنتَجٌ**: `python -m pytest tests/sovereignty/ -q` عندي = `43 passed · 3 errors` بـ`ModuleNotFoundError: amos_federation` في تجهيزِ `مُصرِّح`؛ ووظيفةُ `sovereignty-kernel` تُثبِّتُ `requirements-dev.txt` وحدَه
  - **وقد وقعَ من جنسِه عطبٌ قبلَ اليومِ**: مكتوبٌ في `tests/governance/test_w036_pricing_divergence.py` أنَّ فحصًا سقطَ في وظيفةِ الهويّةِ بـ`ModuleNotFoundError: sqlalchemy` — فالخطرُ `RK-010` **متحقِّقٌ مرّتَينِ** لا مفترَضٌ
  - **وتصحيحٌ لقياسٍ سابقٍ لي في هذه الجلسةِ**: عددُ وظائفِ CI **15** لا 21 (‏`ci.yml` 13 · `measure.yml` 1 · `truth-matrix.yml` 1) — قِيسَ بالأداةِ وبـ`awk` مستقلًّا
  - **ولا قدرةَ جديدةَ في المنتَجِ**: عدّادُ الدَّينِ 182 كما كانَ، والمخالفاتُ 63 كما كانَت
  - **والقياسُ لم يُقَدْ بـCI**: لا تشغيلَ منفَّذًا في المستودعِ منذُ 2026-08-26T23:05:02Z (`DISC-006` بيدِ المالكِ) — فلا يُدَّعى أنَّ الشجرةَ خضراءُ
  - `VERIFIED` غيرُ مُتاحٍ: يلزمُه مراجعٌ مستقلٌّ وتسميتُه قرارٌ سياديٌّ معلَّقٌ (`A-2`)، و`CLOSED` قبلَ الدمجِ دعوى لا قيدٌ
قيدُ السجلّ: W-053 · دفعٌ مباشرٌ إلى main (`84969a9`) · حكمُ CI على عقدتِه: **غائبٌ** (`DISC-006` · لا تشغيلَ) ثمَّ أخضرُ 13/13 على `17ab3c4` (تشغيلُ 33306534739) · مُراجَعٌ 2026-08-30 بـ`W-065` · **مُغلَقٌ 2026-08-30 بـ`W-067`** بعدَ خُضرةٍ مقروءةٍ 13/13 على `04415f4` (تشغيلُ 33315225633)
```

---
---

### WI-021 — ماسحٌ واحدٌ مرجعيٌّ لبوّابةِ السيادةِ 6، ومحلُّ قياسٍ صريحٌ لبوّابةِ حوكمةِ العملِ، وحالةٌ لا تُكتَبُ مرّتَينِ متناقضتَينِ

```text
النطاق: tooling-gates
المسار/المرحلة: T0 / T0.4ب (إرجاعُ `main` أخضرَ · وتصحيحُ صدقِ السجلِّ في موضعِه)
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
المسارات:
  .github/workflows/ci.yml                                       (بوّابةُ 6 تُنادي الماسحَ المرجعيَّ — والملفُّ يُمَسُّ بإعلانٍ لا استخفاءً)
  tools/crown/verify_secret_boundaries.py                        (رايةُ `--tree-pem-only` ومدخلٌ يرفضُ رايةً مجهولةً برمزِ 2)
  tools/governance/check_work_governance.py                      (`--repo-root` صريحٌ · و`check_block_status_agrees` بمخالفةِ `STATUS_CONTRADICTION`)
  tests/governance/test_w054_post_merge_reverse_link.py           (يُقاسُ على الأداةِ المنشورةِ بمحلٍّ مُمَرَّرٍ لا على نُسخةٍ)
  tests/governance/test_w069_single_scanner_and_explicit_root.py  (حرسُ واحديّةِ الماسحِ وصراحةِ محلِّ القياسِ — بطفرةِ مفتاحٍ مزروعٍ)
  tests/governance/test_w069_status_contradiction.py              (حرسُ اتفاقِ حالةِ الصفِّ وحالةِ الكتلةِ — بزرعِ تناقضٍ ورفعِه)
  tests/governance/test_work_governance_gate.py                   (تجهيزُ الكتلةِ يُولَّدُ من صفِّه فتُطابِقُ الحالةُ الحالةَ — تجهيزٌ صُحِّحَ لا حرسٌ خُفِّفَ)
  PROJECT_STATE.md · docs/PROJECT_HANDBOOK.md                    (واجبُ § 7 (4): وثائقُ الحالةِ تُحدَّثُ في دفعةِ العملِ نفسِها)
  وملفّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ: ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md · TRUTH_MATRIX.md المولَّدة
خارجَ النطاق:
  - **لا يُدمَجُ `origin/develop` ولا يُحذَفُ ولا يُعلَنُ إسقاطُه**: ذاك قرارُ مستودعٍ للمالكِ، والخارطةُ لا تمنحُ التنفيذَ سلطتَه — يُقيَّدُ في `DISC-034` و`RK-021` ويُتركُ
  - لا يُخفَّفُ ماسحُ الأسرارِ ولا تُنقَصُ بوّابةٌ: البوّاباتُ اثنتا عشرةَ قبلَ العملِ واثنتا عشرةَ بعدَه، والرايةُ تُشغِّلُ واحدةً منها للتكاملِ لا تُلغي البقيّةَ
  - لا يُفعَّلُ إسقاطُ `POST_MERGE_NOT_CLOSED` افتراضًا: ذاك قرارُ `A-3` وهو معلَّقٌ (`DISC-030`)
  - لا يُعالَجُ `DISC-029` (أثرُ الانحدارِ في الجذرِ) ولا `DISC-031` (مِرساةُ حرسِ الانحرافِ): بندانِ مستقلّانِ في `tooling-gates`، وتوسيعُ النطاقِ الصامتُ ممنوعٌ (§ 5.2)
  - لا تُعادُ كتابةُ تاريخٍ: كتلُ § 3 تُصحَّحُ بسطرِ إقرارٍ يُعلِنُ التناقضَ الذي كانَ، ولا يُمحى
  - لا يُلمَسُ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/
معيارُ القبول:
  1. بوّابةُ السيادةِ 6 في CI تُنادي `tools/crown/verify_secret_boundaries.py` وحدَه، ولا يبقى في خطوتِها ماسحٌ ثانٍ مكتوبٌ بيدٍ ولا نمطُ PEM حرًّا
  2. `--tree-pem-only` يُشغِّلُ بوّابةَ «لا مفتاحَ خاصًّا في الشجرةِ» فعلًا: تُطبَعُ `PASS: 1/1`، ويحمَرُّ الأمرُ عندَ زرعِ مفتاحٍ ثمَّ يعودُ أخضرَ عندَ رفعِه
  3. رايةٌ مجهولةٌ تُرفَضُ برمزِ 2 — لا تُتجاوَزُ صامتةً، ولا رايةَ تخطٍّ في الأداةِ
  4. `--repo-root PATH` يُغيِّرُ محلَّ القياسِ حقًّا (يُقاسُ بشجرةٍ موقوتةٍ)، ويُرفَضُ برمزِ 2 إن لم يكن دليلًا
  5. فحصُ `W-054` يُقاسُ على الأداةِ **المنشورةِ** بمحلٍّ مُمَرَّرٍ لا بنُسخةٍ في شجرةٍ مؤقَّتةٍ (‏عَطبُ `DISC-032` من جنسِه)
  6. `check_block_status_agrees` يرصُدُ `STATUS_CONTRADICTION` عندَ اختلافِ حالةِ الصفِّ عن حالةِ الكتلةِ، و`MALFORMED_ITEM` عندَ كتلةِ بندٍ نشِطٍ بلا سطرِ حالةٍ، وهو موصولٌ في `run()`
  7. لا كتلةَ في `ACTIVE_WORK.md` تُخالِفُ صفَّها: `--self-check` كانَ **14 مخالفةً** فصارَ **صفرًا**
  8. حكمُ CI على عقدةِ الدفعِ يُقرأُ رقمًا ويُقيَّدُ — والتشغيلُ `in_progress` ليسَ حكمًا
الدليلُ المطلوب:
  pytest tests/governance/test_w069_single_scanner_and_explicit_root.py tests/governance/test_w069_status_contradiction.py tests/governance/test_w054_post_merge_reverse_link.py -q
  python tools/crown/verify_secret_boundaries.py                       # PASS: 12/12
  python tools/crown/verify_secret_boundaries.py --tree-pem-only        # PASS: 1/1
  python tools/crown/verify_secret_boundaries.py --لا-وجود-لها          # رمزُ الخروجِ 2
  python tools/governance/check_work_governance.py --self-check         # 0 مخالفة (كانَ 14 `STATUS_CONTRADICTION`)
  python tools/governance/check_work_governance.py --repo-root /لا-دليلَ  # رمزُ الخروجِ 2
  python tools/governance/check_work_governance.py --enforce-post-merge  # خروجٌ 0
  python tools/governance/open_record_accountability.py · state_document_drift.py · truth_audit.py . --ratchet
  pytest tests/ -q                                                     # 2216 passed · 1 skipped
  وحكمُ CI على عقدةِ الدفعِ يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ في خليّةِ «قيدُ السجلّ»
بدأ: 2026-08-30        ينتهي الحجز: 2026-09-06
العائق: —
الخطوةُ التالية: مُنجَزٌ · ولا خطوةَ باقيةً في هذا البندِ — وما بقيَ قرارُ فرعٍ بيدِ المالكِ (`DISC-034`)
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **العملُ سبقَ قيدَه في الشجرةِ المحليّةِ، وذاك خرقٌ لقاعدةِ «الدفعُ = العملُ وقيدُه معًا» صُحِّحَ قبلَ أيِّ دفعةٍ**: كُتِبَ التغييرُ ثمَّ سُجِّلَ البندُ وحُجِزَت مساراتُه ثمَّ قُيِّدَ الاكتشافانِ — فلا دفعةَ خرجَت بلا قيدٍ، والخرقُ **مُعلَنٌ هنا لا مستورٌ** (§ 6.2 تُوجِبُ الحجزَ قبلَ لمسِ العملِ)
  - **الملفُّ `.github/workflows/ci.yml` كانَ محجوزًا بنصِّ `DISC-006`** وتُمَسُّ خطوةٌ واحدةٌ فيه بحدٍّ مُعلَنٍ: استبدالُ ماسحٍ مكتوبٍ بيدٍ بنداءِ الماسحِ المرجعيِّ — لا حرسٌ خُفِّفَ ولا بوّابةٌ رُفِعَت ولا قياسٌ زُيِّفَ
  - **ما استُنقِذَ من `origin/develop` محتوًى لا نسبٌ**: أُعيدَ كتابةُ الإصلاحِ في `main` ولم يُدمَجِ الالتزامُ `37156e6`، فالفرعُ ما زالَ مفترقًا وفيه ملفُّ حرسٍ لم يُقَسْ هنا — والقرارُ للمالكِ (`DISC-034`)
  - **حرسُ الاتفاقِ يقيسُ الحرفَ لا الصدقَ**: يُثبِتُ أنَّ الصفَّ والكتلةَ يقولانِ الشيءَ نفسَه، ولا يقيسُ أنَّ ما يقولانِه حقٌّ — وصدقُ الحالةِ يبقى على الدليلِ المُعلَنِ في البندِ
  - **و`VERIFIED` — متى وُضِعَت — ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2`، فالاستقلالُ مُنتفٍ ومُسجَّلٌ لا مُدَّعًى (`DISC-027` · `RK-020`)
  - **الحرسُ الجديدُ زادَ شرطًا على شكلِ الكتلةِ فصُحِّحَ تجهيزُ فحصٍ قائمٍ**: كانَ تجهيزُ `test_work_governance_gate.py` يبني كتلةً بلا سطرِ حالةٍ — وهو شكلٌ لا يقعُ في السجلِّ الحقيقيِّ (‏عشرونَ كتلةً كلُّها تُعلِنُ حالتَها) — فصارَ التجهيزُ يُولِّدُ سطرَ الحالةِ **من صفِّه نفسِه**. فالمُصحَّحُ تجهيزٌ لا معيارٌ، ولم تُنقَصْ دعوى فحصٍ واحدةٌ: 37 فحصًا تمرُّ كما كانَت
  - **ولا قدرةَ جديدةَ في المنتَجِ**: مخالفاتُ مصفوفةِ الحقيقةِ ثابتةٌ عندَ 63، ولا سطحَ صارَ `PROVEN`
  - **مُراجَعٌ 2026-08-31 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الدليلِ المُعلَنِ عندَ الرأسِ `ed9e5c5` بمُفسِّرِ 3.12 ذاتِه الذي تُشغِّلُه CI، وطُوبِقَت رموزُ الخروجِ والأرقامُ بمعيارِ القبولِ الثمانيةِ بندًا بندًا: البوّاباتُ 12/12 والرايةُ 1/1 ورمزُ 2 لرايةٍ مجهولةٍ ولمحلٍّ ليسَ دليلًا، و`--self-check` صفرٌ بعدَ أربعةَ عشرَ، و`pytest tests/ -q` ⇒ 2216 passed · 1 skipped. **و`VERIFIED` هنا ليست شهادةَ عينٍ ثانيةٍ** — الاستقلالُ مُنتفٍ ومُسجَّلٌ (`DISC-027`)
  - **وحكمُ CI على عقدةِ الدفعِ مُشاهَدٌ لا مُدَّعًى**: تشغيلُ 33342938099 على `ed9e5c5` ⇒ `completed success` · **13/13** وكلُّها بخطواتٍ منفَّذةٍ بقياسِ `ci_verdict_readability.py` (`READABLE`) — فالخُضرةُ **مقروءةٌ** لا مُستنتَجةً من عدمِ الحمرةِ
  - **مُغلَقٌ 2026-08-31 بـ`W-071`**: قُرِئَ حكمُ CI على عقدةِ قيدِ المراجعةِ `0ce4d5d` كذلك — تشغيلُ 33345147799 ⇒ `completed success` · **13/13** · `READABLE` — فالإغلاقُ يستندُ إلى حكمَينِ مقروءَينِ متَّصلَينِ لا إلى واحدٍ
قيدُ السجلّ: W-069 · دفعٌ مباشرٌ إلى main (`ed9e5c5`) · حكمُ CI على عقدةِ القيدِ **قُرِئَ أخضرَ 13/13** (تشغيلُ 33342938099 · `completed success` · و`ci_verdict_readability.py --from-json` ⇒ `READABLE · 13/13`) · مُراجَعٌ 2026-08-31 (`A-2` · غيرُ مستقلٍّ) · **مُغلَقٌ 2026-08-31 بـ`W-071`** بعدَ خُضرةٍ مقروءةٍ ثانيةٍ 13/13 على `0ce4d5d` (تشغيلُ 33345147799 · `READABLE`)
```


### WI-048 — الحكمُ يُقرأُ بمحاولةٍ مسمّاةٍ، لا بآخرِ ما كتبَته الواجهة

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-056` قُيِّدَ في `W-136` · الخطرُ `RK-022`)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: READY   (‏`PROPOSED` ← `READY` بلا قفزٍ · § 4.3 · ولا تقفلُ مسارًا § 6.1)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ — أمرُ القياسِ في «الدليلُ المطلوب» أدناه):
  tools/governance/ci_verdict_readability.py                       (‏السطرُ 249 — الاستدعاءُ بلا `attempts/` · ولا حقلَ محاولةٍ في الحِملِ المكتوبِ)
  tests/governance/test_w051_ci_verdict_readability.py             (‏24 فحصًا قائمًا · يُزادُ عليها حرسُ المحاولةِ ولا يُحذَفُ منها فحصٌ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `ci_verdict_readability.py` **مُدَّعًى لـ`WI-024` وحالتُه `IN_REVIEW`** — مقفولٌ فلا يُمَسُّ اليومَ، و`READY` لا تقفلُ مسارًا فلا `CLAIM_CONFLICT`
  - `test_w051_ci_verdict_readability.py` **مُدَّعًى لـ`WI-032` وحالتُه `IN_REVIEW`** — مقفولٌ كذلك
  - ولا يُمَسُّ `docs/audit/measurements/ci_verdict_readability.json` (‏بادئةٌ معفاةٌ من الحجزِ § 6 · ومُولِّدُها هو المسارُ الأوّلُ نفسُه فيتبعُه)
  - ولا `.github/workflows/ci.yml` (‏مقفولٌ بـ`WI-023`)
خارج النطاق:
  - **لا يُعادُ تشغيلُ تشغيلٍ ولا تُحذَفُ محاولةٌ**: إعادةُ التشغيلِ عينُ العَطبِ المُقيَّدِ فلا تُستعمَلُ دواءً له، وحذفُ محاولةٍ محوٌ لحمرةٍ تُحرِّمُه § 2 حكم 5
  - **ولا يُصلَحُ سببُ سقوطِ المحاولةِ 2**: بنيةُ حسابِ `Actions` بيدِ المالكِ (`RK-011` · `DISC-006`) — يُقاسُ ويُقيَّدُ ولا يُدَّعى إصلاحُه
  - **ولا تُعادُ كتابةُ القيودِ الماضيةِ**: قيدٌ مضى يُحيلُ إلى رقمِ تشغيلٍ بلا رقمِ محاولةٍ يبقى كما كُتِبَ، ويُستدرَكُ بقيدٍ جديدٍ إن لزمَ (§ 2 حكم 7) — لا يُمحى
  - ولا يُضافُ سرٌّ ولا شبكةٌ إلى بوّابةٍ: وجهُ `--from-json` يبقى قياسًا بلا شبكةٍ
معيار القبول:
  1. القراءةُ الحيّةُ تُثبِّتُ محاولةً مسمّاةً: الاستدعاءُ `.../runs/{id}/attempts/{n}/jobs` بمحاولةٍ مُعلَنةٍ، و`n` الافتراضيُّ يُشتَقُّ من `GET /runs/{id}` لا يُفترَضُ
  2. الحِملُ المكتوبُ والحكمُ المطبوعُ **يحمِلانِ رقمَ المحاولةِ** وعددَ المحاولاتِ القائمةَ — فلا يُقرأُ حكمٌ بلا محاولةٍ مسمّاةٍ
  3. حِملٌ محفوظٌ لا يُصرِّحُ بمحاولتِه **لا يُقرأُ حكمًا صامتًا**: يُعلَنُ نقصُه في الخرجِ ولا يُنسَبُ إلى الشجرةِ
  4. الحرسُ **مُجرَّبٌ بطفرةٍ**: إعادةُ الاستدعاءِ إلى `/jobs` بلا محاولةٍ تُسقِطُ فحصًا مُسمًّى، وحذفُ حقلِ المحاولةِ من الخرجِ يُسقِطُ فحصًا مُسمًّى
  5. لا يُخفَّفُ فحصٌ ولا يُحذَفُ من الـ24 القائمةِ فحصٌ · و§ 5.4 كلُّها رمزُها 0 · و`truth_audit` لا يرتفعُ
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ **ورقمِ محاولةٍ** ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب (‏والقياسُ الأوّلُ جرى في `W-136` على التشغيلِ 94):
  grep -n 'actions/runs' tools/governance/ci_verdict_readability.py   # السطرُ 249 — لا `attempts/`
  gh api "repos/xoos-beep/AMOS-Fedration/actions/runs/33818260611" --jq '{a:.run_attempt,c:.conclusion}'   # {"a":2,"c":"failure"}
  gh api ".../runs/33818260611/jobs?per_page=100" --jq '[.jobs[].run_attempt]|unique'                      # [2] — المحاولةُ 1 لا تُرى
  gh api ".../runs/33818260611/attempts/1/jobs?per_page=100"                                               # 13 وظيفةً success بخطواتٍ منفَّذةٍ
  python tools/governance/ci_verdict_readability.py --from-json <حِملُ المحاولةِ 1>   # 0 · READABLE · 13/13
  python tools/governance/ci_verdict_readability.py --from-json <حِملُ المحاولةِ 2>   # 1 · UNREADABLE · 0/10
  python -m pytest tests/governance/test_w051_ci_verdict_readability.py -q            # لا فحصَ يسقُطُ
بدأ: 2026-09-05        ينتهي الحجز: 2026-09-13
  (‏نافذةٌ مُعلَنةٌ لا حجزٌ: الحالةُ `READY` فلا تقفلُ مسارًا · § 6.1 — والحجزُ يُعلَنُ بانتقالٍ مُسجَّلٍ إلى `RESERVED`)
العائق: لا عائقَ فنيًّا. والمسارانِ مُدَّعيانِ لبندَينِ في المراجعةِ (`WI-024` · `WI-032`) فلا يُحجَزانِ قبلَ تحرُّرِهما — والانتظارُ مُعلَنٌ لا مطويٌّ. وتحرُّرُهما موقوفٌ على دورِ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) بعدَ `Q-43`، لا على قرارِ مالكٍ (‏فـ`A-2` `APPROVED`).
الخطوةُ التالية: حجزُ البندِ متى تحرَّرَ المسارانِ، ثمَّ تثبيتُ المحاولةِ في القراءةِ وكتابتُها في الخرجِ بحرسٍ يُثبِتُ الفرقَ بطفرةٍ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **المقيسُ تشغيلٌ واحدٌ بمحاولتَينِ**، ولا يُدَّعى مسحُ كلِّ تشغيلاتِ المستودعِ بحثًا عن محاولاتٍ مُعادةٍ — وما لم يُقَسْ لا يُعلَنُ
  - **وتثبيتُ المحاولةِ لا يُعيدُ للدليلِ ثباتَه بأثرٍ رجعيٍّ**: قيودٌ مضَت تُحيلُ إلى أرقامِ تشغيلٍ بلا محاولةٍ، وإحكامُ القارئِ يمنعُ التبدُّلَ من اليومِ ولا يُصحِّحُ ما مضى
  - **ولا يمنعُ البندُ إعادةَ تشغيلٍ**: هي حقُّ المالكِ في حسابِه — البندُ يجعلُ القراءةَ **تُسمّي ما قرأَت** فلا يُقرأُ حِملٌ آخرُ بالرقمِ نفسِه صامتًا
قيدُ السجلّ: — (‏البندُ لم يُنجَزْ بعدُ · والقيدُ الذي فتحَه `W-136`)
```

---

### WI-047 — دَينٌ يُعَدُّ، فيُرتَّجُ عددُ ما لا سقفَ له

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-055` قُيِّدَ بأرقامٍ تُعادُ: **18 ملاحظةً عادّةً · صفرٌ محبوسةٌ · 18 بلا سقفٍ** قبلَ الحرسِ، و**19 · 1 · 18** بعدَه)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW   (‏`PROPOSED` ← `READY` ← `RESERVED` ← `IN_PROGRESS` ← `IN_REVIEW` بلا قفزٍ · § 4.3 — نُقِلَ على حكمِ تشغيلِ **91** (`33798360474` · `575b911`) ⇒ `completed success` · **13/13** · `READABLE`. و`VERIFIED` **لا يُكتَبُ هنا**: فعلُ المراجعِ لا الكاتبِ · والمراجعُ بعدَ `Q-43` مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6) · و`DISC-027` و`RK-020` أُغلِقا به)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ):
  tools/governance/report_note_ratchet.py                          (‏جديدٌ — يُحصي ملاحظاتِ الإبلاغِ الحاملةَ عددًا ويرتِّجُ ما لا سقفَ له)
  tests/governance/test_w132_report_note_ratchet.py                 (‏جديدٌ — يُثبِتُ الفرقَ بشجرةٍ مصنوعةٍ ثمَّ يقيسُ الشجرةَ الحقيقيّةَ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - المسارانِ **غيرُ موجودَينِ قبلَ هذا البندِ** فلا مُدَّعيَ لهما في صفوفِ § 1 — لا `CLAIM_COLLISION`
  - والبوّاباتُ الستُّ المقروءةُ **لا تُمَسُّ**: أكثرُها مُدَّعًى لبنودٍ `IN_REVIEW` (`WI-023`…`WI-046`)، والقراءةُ تركيبيّةٌ لا كتابةٌ
  - ولا `.github/workflows/ci.yml` (‏مقفولٌ بـ`WI-023`) ولا `docs/audit/*` المُولَّدةُ
خارج النطاق:
  - **لا يُنزَلُ سقفٌ لكلِّ رقمٍ على حدةٍ**: تحويلُ ملاحظةٍ إلى مخالفةٍ يمسُّ ستَّ أدواتٍ مُدَّعاةٍ ويُغيِّرُ حكمَ بوّابةٍ قائمةٍ — قرارٌ أعلى من فئةِ هذا البندِ
  - **ولا تُحذَفُ ملاحظةٌ** لتخرُجَ من العدِّ: حذفُ الإبلاغِ إخفاءٌ لا إصلاحٌ، ولذلكَ عددُ العادّاتِ **أرضٌ لا تنزلُ**
  - ولا يُخفَّفُ حرسٌ قائمٌ ولا يُسكَتُ ماسحٌ
معيار القبول:
  1. عددُ الملاحظاتِ العادّةِ **بلا سقفٍ مُعلَنٍ** سقفٌ لا يعلو، والمرتَّجُ منها **أرضٌ لا تنزلُ**
  2. القياسُ من **شجرةِ التحليلِ** لا من نصِّ الملفِّ: لفظُ «ملاحظة» في تعليقٍ أو ترويسةٍ لا يُعَدُّ ملاحظةً
  3. **الرَّتْجُ إعلانٌ مقصودٌ** لا ذِكرٌ عارضٌ: يُقرأُ من سطرِ `REPORT_NOTE_RATCHETED:` وحدَه، فنثرُ القيدِ لا يُخضِرُ رمزًا بضربِ المثلِ به
  4. **والحرسُ يُحصي نفسَه**: ملاحظتُه تُبنى بالشكلِ المقيسِ نفسِه فتدخُلُ العدَّ، وحبسُها مُعلَنٌ لأنَّ عددَها هو ما يحبِسُه أساسُه فعلًا
  5. عَطبُ القياسِ **يُرفَعُ لا يُتخطّى**: ملفٌّ لا يُقرأُ أو لا يُحَلُّ نحوًا يُسقِطُ القياسَ
  6. الرقمُ المُعلَنُ **مصدرٌ واحدٌ** في [`DISCOVERIES.md`](DISCOVERIES.md) لا ثابتٌ مدفونٌ في الأداةِ
  7. **وجملةُ نجاحِ الحرسِ تحمِلُ مقامَها** (`DISC-053`) · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  8. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python tools/governance/report_note_ratchet.py --check
  python -m pytest tests/governance/test_w132_report_note_ratchet.py -q -p no:randomly
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-30
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الرَّتْجُ يُقاسُ إعلانًا لا إنفاذًا**: رمزٌ مُعلَنٌ في `REPORT_NOTE_RATCHETED:` يُعَدُّ محبوسًا ولو لم يُسقِطْ رقمُه بوّابةً بعدُ — فهذا الحرسُ يمنعُ **نموَّ الصمتِ** لا يُنشِئُ سقفًا لكلِّ رقمٍ
  - **والشكلُ مُدرَجٌ**: تُقاسُ الملاحظاتُ المبنيّةُ على شكلِ `‹تقرير›.notes.append(‹بانٍ›("CODE", …))`؛ بوّابةٌ تطبعُ ملاحظةً بشكلٍ آخرَ تُفلِتُ حتّى يُدرَجَ شكلُها — والشكلُ مكتوبٌ في نصِّ الأداةِ
  - **ولا يُقاسُ صدقُ العددِ** في الملاحظةِ: يُقاسُ أنَّ عددًا يُطبَعُ بلا سقفٍ
  - **ولا `VERIFIED` بيدِ الكاتبِ** (§ 4.3) — والمراجعُ بعدَ `Q-43` مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6)، و`DISC-027` و`RK-020` أُغلِقا به
قيدُ السجلّ: W-132 · دفعٌ مباشرٌ إلى main (`575b911`) · حكمُ تشغيلِ **91** (`33798360474`) على عقدةِ `575b911` ⇒ `completed success` · **13/13** · `READABLE` (و`ci_verdict_readability.py --repo xoos-beep/AMOS-Fedration --from-json` ⇒ خروجٌ 0) · مُسلَّمٌ للمراجعةِ 2026-09-04   |   — (البندُ `IN_REVIEW` — `VERIFIED` فعلُ المراجعِ لا الكاتبِ · `A-2` `PENDING` · `DISC-027` · `RK-020`)
```

---


### WI-046 — أثرٌ يشهدُ على نقصِ بيئتِه، فتُقرأُ شهادتُه

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-054` قُيِّدَ بأرقامٍ تُعادُ: **وثيقتانِ شاهدتانِ · صفرُ مُعلِنٍ نقصًا · صفرُ قارئٍ لشهادةٍ**)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW   (‏`PROPOSED` ← `READY` ← `RESERVED` ← `IN_PROGRESS` ← `IN_REVIEW` بلا قفزٍ · § 4.3 — نُقِلَ على حكمِ تشغيلِ **90** (`33790942381` · `9da40866`) ⇒ `completed success` · **13/13** · `READABLE`. و`VERIFIED` **لا يُكتَبُ هنا**: فعلُ المراجعِ لا الكاتبِ · والمراجعُ بعدَ `Q-43` مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6) · و`DISC-027` و`RK-020` أُغلِقا به)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ):
  tools/governance/artifact_witness_integrity.py                   (‏جديدٌ — يقرأُ شهادةَ التوليدِ في الأثرِ المُقيَّدِ ويرفضُ المُعلِنَ نقصَه)
  tests/governance/test_w131_artifact_witness_integrity.py          (‏جديدٌ — يُثبِتُ الفرقَ بأثرٍ مصنوعٍ ثمَّ يقيسُ الأثرَ الحقيقيَّ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - المسارانِ **غيرُ موجودَينِ قبلَ هذا البندِ** فلا مُدَّعيَ لهما في صفوفِ § 1 — لا `CLAIM_COLLISION`
  - و`tools/governance/verify_cross_system_suites.py` **لا يُمَسُّ**: مُدَّعًى لا يُدَّعى هنا، والحرسُ **قارئٌ للأثرِ** لا مُعدِّلٌ للمُولِّدِ
  - و`docs/audit/CROSS_SYSTEM_SUITE_MATRIX.md` و`docs/audit/CROWN_TRUTH_MATRIX.md` **تُقرآنِ ولا تُكتَبانِ** — والأولى استُرجِعَت من الفرعِ في `W-130` فلا تُمَسُّ هنا
خارج النطاق:
  - **لا يُعدَّلُ المُولِّدُ ليرفضَ التوليدَ في بيئةٍ ناقصةٍ**: ذاكَ إصلاحٌ ثانٍ في مسارٍ مُدَّعًى، وهذا البندُ يحرسُ **الأثرَ المُقيَّدَ** — وهو الموضعُ الذي يخدعُ القارئَ
  - **ولا تُحذَفُ شهادةُ التوليدِ من الوثيقةِ** هربًا من قراءتِها: حذفُها إخفاءٌ لا إصلاحٌ، ولذلكَ عددُ الشاهدينَ **أرضٌ لا تنزلُ**
  - ولا تُعادُ الوثيقةُ المعطوبةُ ولا يُخفَّفُ حرسٌ قائمٌ
معيار القبول:
  1. أثرٌ مُقيَّدٌ يُعلِنُ في متنِه **نقصَ بيئةِ قياسِه** أو **سقوطَ حزمةٍ** يُسقِطُ وجهَ `--check` بمخالفةٍ مُسمّاةٍ
  2. عددُ الآثارِ **الشاهدةِ** أرضٌ لا تنزلُ: حذفُ الشهادةِ من وثيقةٍ يُسقِطُ الوجهَ كما يُسقِطُه النقصُ
  3. الفرقُ **مُجرَّبٌ بأثرٍ مصنوعٍ**: وثيقةٌ تُعلِنُ «غائبة» أو خليّةَ `FAIL` تُقاسُ مخالفةً، ونظيرتُها السليمةُ تمرُّ
  4. عَطبُ القياسِ **يُرفَعُ لا يُتخطّى**: أثرٌ لا يُقرأُ يُسقِطُ القياسَ ولا يُقرأُ «سليمًا»
  5. الرقمُ المُعلَنُ **مصدرٌ واحدٌ** في [`DISCOVERIES.md`](DISCOVERIES.md) لا ثابتٌ مدفونٌ في الأداةِ
  6. **وجملةُ نجاحِ الحرسِ تحمِلُ مقامَها** (`DISC-053` · لا يُزادُ الصامتُ)
  7. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  8. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python tools/governance/artifact_witness_integrity.py --check
  python -m pytest tests/governance/test_w131_artifact_witness_integrity.py -q -p no:randomly
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-30
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الشهادةُ تُقرأُ نصًّا**: أثرٌ يُعلِنُ نقصَ بيئتِه بصيغةٍ غيرِ مُدرَجةٍ يُفلِتُ حتّى تُدرَجَ صيغتُه — والصيغُ المُدرَجةُ مكتوبةٌ في نصِّ الأداةِ لا مطويّةٌ
  - **والحرسُ لا يقيسُ صدقَ الأرقامِ** في الأثرِ: يقيسُ أنَّ الأثرَ **لا يشهدُ على نفسِه بالنقصِ** — فأثرٌ وُلِّدَ في بيئةٍ كاملةٍ بأرقامٍ خاطئةٍ يمرُّ
  - **ولا يمنعُ التوليدَ الناقصَ** أصلًا: يمنعُ **قيدَه في الشجرةِ** — والمنعُ في المُولِّدِ بندٌ آخرُ في مسارٍ مُدَّعًى
  - **ولا `VERIFIED` بيدِ الكاتبِ** (§ 4.3) — والمراجعُ بعدَ `Q-43` مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6)، و`DISC-027` و`RK-020` أُغلِقا به
قيدُ السجلّ: — (‏البندُ لم يُغلَقْ بعدُ)
```

---


### WI-045 — خُضرةٌ تقولُ كم قرأَت، أو تُبلَّغُ عن سكوتِها

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-053` قُيِّدَ بأرقامٍ تُعادُ: **49 وحدةً · 36 جملةَ نجاحٍ · 20 كلّيّةً · 3 بمقامٍ · 17 بلا مقامٍ**)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW   (‏`PROPOSED` ← `READY` ← `RESERVED` ← `IN_PROGRESS` ← `IN_REVIEW` بلا قفزٍ · § 4.3 — نُقِلَ على حكمِ تشغيلِ **89** (`33785332367` · `93db6855`) ⇒ `completed success` · **13/13** · `READABLE`. و`VERIFIED` **لا يُكتَبُ هنا**: فعلُ المراجعِ لا الكاتبِ · والمراجعُ بعدَ `Q-43` مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6) · و`DISC-027` و`RK-020` أُغلِقا به)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ):
  tools/governance/green_denominator_closure.py                    (‏جديدٌ — يُحصي جملَ النجاحِ الكلّيّةَ ومقاماتِها ويُسقِطُ نموَّ ما لا مقامَ له)
  tests/governance/test_w130_green_denominator_closure.py          (‏جديدٌ — يُثبِتُ الفرقَ بشجرةٍ مصنوعةٍ ثمَّ يقيسُ المستودعَ الحقيقيَّ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - المسارانِ **غيرُ موجودَينِ قبلَ هذا البندِ** فلا مُدَّعيَ لهما في صفوفِ § 1 — لا `CLAIM_CONFLICT`
  - ولا تُمَسُّ أيُّ أداةٍ من السبعَ عشرةَ المقيسةِ: أكثرُها مُدَّعًى لبنودٍ `IN_REVIEW` (`WI-023` · `WI-030` · `WI-034` · `WI-035` · `WI-036` · `WI-038` · `WI-043`)
  - ولا `tools/governance/suite_size_inventory.py` (‏مُدَّعًى لـ`WI-038` و`WI-044`) ولا `docs/PROJECT_HANDBOOK.md`
خارج النطاق:
  - **لا يُرفَقُ المقامُ بالسبعَ عشرةَ جملةً في هذا البندِ**: تعديلُ خرجِ خمسةَ عشرَ ملفًّا يمسُّ مساراتٍ مُدَّعاةً ويُخرِجُ حجمَ التغييرِ عن حدِّ بندٍ واحدٍ. والمُنجَزُ **منعُ نموِّ ما لا مقامَ له وتسميتُه** لا إغلاقُه
  - **ولا يُرفَعُ الرقمُ المُعلَنُ ليسَعَ جملةً جديدةً بلا مقامٍ**: رفعُه فعلُ إخفاءٍ لا فعلُ قياسٍ
  - ولا يُخفَّفُ حرسٌ قائمٌ ولا تُحذَفُ جملةُ نجاحٍ لتخرُجَ من العدِّ
معيار القبول:
  1. عددُ الجملِ الكلّيّةِ **بلا مقامٍ** سقفٌ لا يعلو، والمُقامُ منها **أرضٌ لا تنزلُ**، وعددُ الجملِ الكلّيّةِ **مُطابِقٌ تمامًا**
  2. القياسُ من **شجرةِ التحليلِ** لا من نصِّ الملفِّ: حرفُ «✓» في تعليقٍ أو في ترويسةٍ **لا يُعَدُّ** جملةَ نجاحٍ
  3. **المقامُ كمٌّ مقيسٌ لا رقمٌ مكتوبٌ**: عددٌ حرفيٌّ مغروسٌ في الجملةِ لا يشتري مقامًا، والمقامُ ما يُحسَبُ من المقروءِ (`len(...)` أو عدّادٌ)
  4. **والحرسُ يُحصي نفسَه**: جملةُ نجاحِ هذه الأداةِ داخلةٌ في العدِّ، فتحمِلُ مقامَها — وقارئٌ يُعفي نفسَه يُعلِّمُ الإعفاءَ
  5. عَطبُ القياسِ **يُرفَعُ لا يُتخطّى**: ملفٌّ لا يُقرأُ أو لا يُحَلُّ نحوًا يُسقِطُ القياسَ، وسطرُ الرقمِ المُعلَنِ الغائبُ أو المكرَّرُ يُرفَضُ
  6. الرقمُ المُعلَنُ **مصدرٌ واحدٌ** في [`DISCOVERIES.md`](DISCOVERIES.md) لا يُخمَّنُ ولا يُنسَخُ
  7. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  8. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python tools/governance/green_denominator_closure.py --check
  python -m pytest tests/governance/test_w130_green_denominator_closure.py -q -p no:randomly
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-30
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **المقامُ يُقاسُ شكلًا لا صدقًا**: جملةٌ تُرفِقُ عددًا محسوبًا من مجموعةٍ **خاطئةٍ** تُقرأُ «بمقامٍ» — فالحرسُ يمنعُ الحكمَ الكلّيَّ الأصمَّ ولا يُصدِّقُ الرقمَ المُرفَقَ
  - **والقراءةُ تركيبيّةٌ (AST)**: أداةٌ تبني سطرَ نجاحِها بطريقةٍ لا يراها القارئُ الساكنُ (‏تجميعٌ في متغيِّرٍ بعيدٍ · قالبٌ يُقرأُ من ملفٍّ) لا تُحصى — حدٌّ مُعلَنٌ في نصِّ الأداةِ وفي نصِّ الفحصِ
  - **والحكمُ «الكلّيُّ» يُعرَفُ بألفاظٍ مُدرَجةٍ**: جملةٌ تُعلِنُ الكُلّيّةَ بلفظٍ غيرِ مُدرَجٍ تُقرأُ غيرَ كلّيّةٍ فتخرُجُ من العدِّ — وهذا **جنسُ العَطبِ الذي يُحرَسُ نفسُه** (`DISC-052`)، فالحدُّ مكتوبٌ صريحًا ويُصحَّحُ بإضافةِ لفظٍ لا بتخفيفٍ
  - **ولا `VERIFIED` بيدِ الكاتبِ** (§ 4.3) — والمراجعُ بعدَ `Q-43` مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6)، و`DISC-027` و`RK-020` أُغلِقا به
قيدُ السجلّ: — (‏البندُ لم يُغلَقْ بعدُ)
```

---


### WI-044 — حكمُ البوّابةِ لا يُعلِنُ أوسعَ مِمّا قاسَ

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-052` قُيِّدَ في `W-129` بفارقٍ مقيسٍ **23**)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: READY   (‏`PROPOSED` ← `READY` بلا قفزٍ · § 4.3 · ولا تقفلُ مسارًا § 6.1)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ):
  tools/governance/suite_size_inventory.py                         (‏قارئُ الدعاوى — صيغةُ «المُجمَّعُ حيًّا N» لا تُصنَّفُ حيّةً · ونصُّ الحكمِ أوسعُ من القياسِ)
  tests/governance/test_w120_suite_size_claims.py                  (‏حرسُ الأداةِ — يُزادُ فحصٌ يُثبِتُ أنَّ رقمَ الجذرِ يُقرأُ ويُقاسُ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - المسارانِ كلاهما **مُدَّعًى لـ`WI-038`** وحالتُه `IN_REVIEW` — فلا يُمَسّانِ اليومَ، و`READY` لا تقفلُ مسارًا فلا `CLAIM_CONFLICT`
  - ولا يُمَسُّ `docs/PROJECT_HANDBOOK.md` في هذا البندِ (‏مُدَّعًى لـ`WI-023`) — والرقمُ نفسُه صُحِّحَ بقياسٍ طازجٍ في `W-129`
خارج النطاق:
  - **لا يُحذَفُ الرقمُ من وثيقةِ الحالةِ هربًا من حرسِه**: حذفُ الدعوى إخفاءٌ لا قياسٌ
  - ولا يُعادُ ترتيبُ صيغِ الأرقامِ في الوثيقةِ كلِّها: المحكومُ به **حدُّ القارئِ ونصُّ حكمِه** لا أسلوبُ الكتابةِ
معيار القبول:
  1. رقمُ حزمةِ الجذرِ **يُقرأُ دعوى حيّةً** ويُقاسُ بجمعٍ حيٍّ، **أو** يُضيَّقُ نصُّ الحكمِ فيُسمّي ما لم يُقَسْ صراحةً
  2. الفرقُ **مُجرَّبٌ بطفرةٍ**: رقمٌ يُزاحُ بواحدٍ يُسقِطُ فحصًا مُسمًّى، والرسالةُ تُسمّي الدعوى وموضعَها
  3. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  4. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python tools/governance/suite_size_inventory.py --json
  python -m pytest tests/ -q -p no:randomly --collect-only
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-11
  (‏نافذةٌ مُعلَنةٌ لا حجزٌ: الحالةُ `READY` فلا تقفلُ مسارًا · § 6.1)
العائق: المسارانِ مُدَّعيانِ لبندٍ `IN_REVIEW` (`WI-038`) — والمراجعةُ بيدِ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43` لا بيدِ المالكِ
الخطوةُ التالية: حجزُ البندِ متى تحرَّرَ المسارانِ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **العَطبُ ليسَ في الرقمِ**: الرقمُ صُحِّحَ في `W-129` بقياسٍ طازجٍ — والباقي أنَّ تقادُمَه لا يُحمَرُّ له
  - **وقارئُ النصِّ يبقى قارئَ نصٍّ**: أيُّ صيغةٍ ثالثةٍ لرقمٍ مكتوبٍ تُفلِتُ حتّى تُقاسَ — حدٌّ من جنسِ كلِّ قارئٍ للنثرِ، لا وعدٌ بإغلاقِ الجنسِ
قيدُ السجلّ: — (‏البندُ لم يُنجَزْ بعدُ · والقيدُ الذي فتحَه `W-129`)
```

---


### WI-043 — مُولِّدٌ يُولَدُ فيدخُلُ الحرسَ، أو يُبلَّغُ عن غيابِه

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-051` قُيِّدَ بأرقامٍ تُعادُ: **11 مُولِّدًا · 4 مربوطةٌ · 7 بلا رباطٍ**)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW   (‏`PROPOSED` ← `READY` ← `RESERVED` ← `IN_PROGRESS` ← `IN_REVIEW` بلا قفزٍ · § 4.3 — و`VERIFIED` فعلُ المراجعِ لا الكاتبِ)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ):
  tools/governance/generator_settlement_closure.py                 (‏جديدٌ — يقيسُ المُولِّداتِ ومواضعَ رباطِها ويُسقِطُ نموَّ الفراغِ)
  tests/governance/test_w129_generator_settlement_closure.py        (‏جديدٌ — يُثبِتُ الفرقَ بشجرةٍ مصنوعةٍ ثمَّ يقيسُ المستودعَ الحقيقيَّ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - المسارانِ **غيرُ موجودَينِ قبلَ هذا البندِ** فلا مُدَّعيَ لهما في صفوفِ § 1 — لا `CLAIM_CONFLICT`
  - ولا يُمَسُّ `tests/governance/test_identity_law.py` (‏موضعُ الرباطِ الثلاثيِّ المقيسُ) — وهو مُدَّعًى لـ`WI-032` (`IN_REVIEW`)
  - ولا `tests/governance/test_w099_generated_artifact_freshness.py` ولا `tools/governance/truth_audit.py`
خارج النطاق:
  - **لا تُربَطُ السبعةُ غيرُ المربوطةِ في هذا البندِ**: ربطُ سبعةِ مُولِّداتٍ بوجهِ `--check` على الجذرِ الحقيقيِّ عملٌ سبعيُّ الحجمِ يمسُّ مساراتٍ مُدَّعاةً، والمُنجَزُ هنا **منعُ نموِّ الفراغِ وتسميتُه** لا إغلاقُه
  - **ولا يُرفَعُ الرقمُ المُعلَنُ ليسَعَ مُولِّدًا جديدًا**: رفعُه فعلُ إخفاءٍ لا فعلُ قياسٍ، والوجهُ يُسقِطُ عندَ النموِّ قصدًا
  - ولا يُخفَّفُ حرسٌ قائمٌ ولا يُحذَفُ موضعُ رباطٍ
معيار القبول:
  1. عددُ المُولِّداتِ بلا رباطٍ مقيسٍ **سقفٌ لا يعلو**، والمربوطُ **أرضٌ لا تنزلُ**، وعددُ المُولِّداتِ **مُطابِقٌ تمامًا**
  2. القياسُ من **شجرةِ التحليلِ** لا من نصِّ الملفِّ: أداةٌ تحكي عن الكتابةِ في ترويستِها ولا تكتُبُ **لا تُعَدُّ** مُولِّدًا
  3. **الرباطُ نداءٌ لا كلمةٌ**: ذِكرُ اسمِ أداةٍ في فحصٍ لا يشتري رباطًا، ووجهٌ يُشغَّلُ على شجرةٍ مؤقَّتةٍ ليسَ رباطًا على المستودعِ
  4. عَطبُ القياسِ **يُرفَعُ لا يُتخطّى**: ملفٌّ لا يُقرأُ أو لا يُحَلُّ نحوًا يُسقِطُ القياسَ، وسطرُ الرقمِ المُعلَنِ الغائبُ أو المكرَّرُ يُرفَضُ
  5. الرقمُ المُعلَنُ **مصدرٌ واحدٌ** في [`DISCOVERIES.md`](DISCOVERIES.md) لا يُخمَّنُ ولا يُنسَخُ
  6. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  7. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python tools/governance/generator_settlement_closure.py --check
  python -m pytest tests/governance/test_w129_generator_settlement_closure.py -q -p no:randomly
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-30
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الحرسُ يقيسُ أنَّ الوجهَ يُشغَّلُ على الشجرةِ الحقيقيّةِ، لا أنَّ ما يقيسُه صادقٌ**: أداةٌ يُشغَّلُ `--check` لها ولا تُسقِطُ بحقٍّ تُقرأُ «مربوطةً» — وهذا حدٌّ من جنسِ كلِّ حرسٍ يقيسُ الرباطَ لا المضمونَ
  - **والقراءةُ تركيبيّةٌ (AST)**: فحصٌ يبني أمرَه بطريقةٍ لا يراها القارئُ الساكنُ لا يُحصى رباطًا — حدٌّ مُعلَنٌ في نصِّ الأداةِ وفي نصِّ الفحصِ
  - **وأوّلُ نسخةٍ من الأداةِ عَدَّت نفسَها مُولِّدًا**: قاسَتِ الكتابةَ نصًّا فحكمَت على ذِكرٍ في ترويستِها، فقِيسَ 12 مُولِّدًا و8 بلا رباطٍ. **أُصلِحَ السببُ** (‏صارَ القياسُ نحويًّا) لا العَرَضُ (‏لم يُستثنَ الملفُّ ولم يُرفَعِ الرقمُ)، والعَطبُ محروسٌ بفحصٍ مُسمًّى
  - **والعملُ سبقَ قيدَ البندِ في الشجرةِ المحليّةِ**: كُتِبَ الحرسُ ثمَّ قُيِّدَ `DISC-051` ثمَّ فُتِحَ هذا البندُ — نافذةُ الالتزامِ الواحدِ (`DISC-030`)، **مُعلَنٌ هنا لا مستورٌ**، ولا دفعةَ خرجَت بلا قيدٍ
  - **ولا `VERIFIED` بيدِ الكاتبِ** (§ 4.3) — والمراجعُ بعدَ `Q-43` مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6)، و`DISC-027` و`RK-020` أُغلِقا به
قيدُ السجلّ: — (‏البندُ لم يُغلَقْ بعدُ)
```

---


### WI-042 — بوّابةٌ يُقرأُ حكمُها ولا يتذبذبُ على شجرةٍ واحدةٍ

```text
النطاق: tooling-gates (‏بوّاباتُ CI — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-050` قُيِّدَ في `W-128` بمحاولتَينِ متناقضتَينِ على عقدةٍ واحدةٍ)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: READY   (‏`PROPOSED` ← `READY` بلا قفزٍ · § 4.3 · ولا تقفلُ مسارًا § 6.1)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ):
  .github/workflows/ci.yml                                         (‏السطرُ 432 — خطوةُ «بوّابة 2ج» تُثبِّتُ بـ`pip install -e . --no-deps` فتُحَلُّ التبعيّاتُ من محيطٍ لا من قفلٍ)
  federal/executive/services/pyproject.toml                        (‏مصدرُ تبعيّاتِ الحزمةِ — إن كانَ العزلُ يوجِبُ تثبيتَ مدًى)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `.github/workflows/ci.yml` **مقفولٌ بـ`WI-023` وحالتُه `IN_REVIEW`** — فلا يُمَسُّ اليومَ، و`READY` لا تقفلُ مسارًا فلا `CLAIM_CONFLICT`
  - `federal/executive/services/pyproject.toml` لا مُدَّعيَ له في صفوفِ § 1
  - ولا يُمَسُّ `federal/executive/services/tests/test_king_login_boundary.py`: **الفحصُ ليس مُتَّهَمًا حتّى يُقرأَ سببُ سقوطِه**
خارج النطاق:
  - **لا يُعادُ تشغيلُ وظيفةٍ علاجًا**: إعادةُ التشغيلِ في `W-128` كانت **قياسَ ثباتِ حكمٍ** وقُيِّدَت نتيجتاها معًا، ولا تصيرُ عادةً تُخضِّرُ حمرةً
  - ولا يُوسَمُ فحصٌ `flaky` ولا يُعلَّمُ `xfail` ولا يُسكَتُ: **الوسمُ إخفاءٌ ما لم يُقرَأِ السببُ**
  - ولا يُقرَّرُ تغييرُ بنيةِ تثبيتِ التبعيّاتِ في المستودعِ كلِّه: هذا عزلُ سببٍ في خطوةٍ واحدةٍ مقيسةٍ
معيار القبول:
  1. **سببُ السقوطِ مقروءٌ ومكتوبٌ** قبلَ أيِّ تغييرٍ: لا يُصلَحُ ما لم يُقَسْ
  2. حكمُ الخطوةِ **دالّةٌ في الشجرةِ**: تشغيلانِ متتاليانِ على عقدةٍ واحدةٍ يُعطيانِ الحكمَ نفسَه
  3. تبعيّاتُ الخطوةِ تُثبَّتُ من مصدرٍ مُثبَتٍ لا من محيطٍ متغيِّرٍ، والفرقُ مكتوبٌ
  4. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  5. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  # القياسُ الذي فتحَ البندَ: تشغيلُ 86 (33767648556 · 8de10b14) — محاولةٌ 1 فشلٌ 12/13 · محاولةٌ 2 نجاحٌ 13/13 بلا تعديلٍ
  python tools/governance/ci_verdict_readability.py --from-json <jobs.json> --repo xoos-beep/AMOS-Fedration
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-11
  (‏نافذةٌ مُعلَنةٌ لا حجزٌ: الحالةُ `READY` فلا تقفلُ مسارًا · § 6.1)
العائق: **قراءةُ سجلِّ الوظيفةِ محجوبةٌ في بيئةِ التنفيذِ**: تنزيلُه يُحوَّلُ إلى مُضيفٍ غيرِ `api.github.com`، وتعليقاتُ الفحصِ
  لم تحمِلْ إلّا «رمزُ الخروجِ 1». فعزلُ السببِ يوجِبُ طريقًا للقراءةِ — أو أثرًا تُصدِّرُه الوظيفةُ نفسُها، وذاكَ يمسُّ مسارًا مقفولًا.
الخطوةُ التالية: إيجادُ طريقٍ لقراءةِ سجلِّ الوظيفةِ (‏أو أثرٍ مُصدَّرٍ)، ثمَّ عزلُ السببِ قبلَ أيِّ تغييرٍ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **لا يُدَّعى تذبذُبٌ محضٌ**: المقيسُ حكمانِ متناقضانِ على شجرةٍ واحدةٍ، وذاكَ يُثبِتُ **عدمَ ثباتِ الحكمِ** لا يُثبِتُ سلامةَ الشجرةِ
  - **والخُضرةُ الثانيةُ لا تُبرِّئُ**: بقيَ احتمالُ عَطبٍ يظهرُ بشرطٍ لم يُعزَلْ، وهو مكتوبٌ هنا لا مطويٌّ
قيدُ السجلّ: — (‏البندُ لم يُنجَزْ بعدُ · والقيدُ الذي فتحَه `W-128`)
```

---

### WI-041 — طابعُ الالتزامِ يُصرَّحُ لا يُورَثُ من بيئةِ الدافعِ

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-049` قُيِّدَ في `W-127` وصُحِّحَ أثرُه ولم يُحرَسْ سببُه)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: READY   (‏`PROPOSED` ← `READY` بلا قفزٍ · § 4.3 · ولا تقفلُ مسارًا § 6.1)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ):
  tools/governance/commit_timestamp_integrity.py                   (‏قائمٌ — يُزادُ له وجهٌ يقيسُ رأسَ الفرعِ المدفوعِ لا التاريخَ المرئيَّ محلّيًّا وحدَه)
  docs/PROJECT_HANDBOOK.md                                         (‏§ 12 — قائمةُ ما قبلَ الدفعِ: التصريحُ بالإزاحةِ يُكتَبُ شرطًا لا عُرفًا)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `commit_timestamp_integrity.py` **مُدَّعًى لـ`WI-035` وحالتُه `IN_REVIEW`** — فلا يُمَسُّ اليومَ، و`READY` لا تقفلُ مسارًا فلا `CLAIM_CONFLICT`
  - `docs/PROJECT_HANDBOOK.md` **مُدَّعًى لـ`WI-023` وحالتُه `IN_REVIEW`** — والحكمُ نفسُه
  - ولا يُمَسُّ `tests/governance/test_w110_commit_stamp_integrity.py` ولا `test_w113_new_commit_stamp_utc.py` (‏مُدَّعيانِ لـ`WI-035`)
  - ولا `.github/workflows/ci.yml` (‏مقفولٌ بـ`WI-023`)
خارج النطاق:
  - **لا يُرفَعُ `COMMIT_STAMP_BASELINE` ولا يُخفَّفُ حرسٌ قائمٌ**: الحرسانِ القائمانِ صَدَقا — وهما من كشفَ العَطبَ، فلا يُمَسّانِ
  - ولا يُعادُ كتابةُ تاريخٍ ماضٍ: التصحيحُ يقعُ على الالتزامِ الجديدِ قبلَ أن يُبنى عليه، لا على قيودٍ مدفوعةٍ (‏حدُّ `DISC-043`)
  - ولا يُقرَّرُ تغييرُ أداةِ الدفعِ نفسِها قرارًا معماريًّا: هذا إحكامُ شرطٍ مكتوبٍ لا اختيارُ وسيلةٍ
معيار القبول:
  1. التصريحُ بإزاحةِ `+00:00` في إنشاءِ الالتزامِ **شرطٌ مكتوبٌ** في قائمةِ ما قبلَ الدفعِ، لا عُرفٌ يُتذكَّرُ
  2. وجهٌ يقيسُ إزاحةَ رأسِ الفرعِ **المدفوعِ** فيُقرأُ العَطبُ من مصدرٍ يراه المُنشِئُ، لا من حكمِ CI بعدَ الحمرةِ وحدَه
  3. الحرسُ **مُجرَّبٌ بطفرةٍ**: طابعٌ بإزاحةٍ محلّيّةٍ يُسقِطُ فحصًا مُسمًّى، والرسالةُ تُسمّي التصريحَ الغائبَ سببًا
  4. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  5. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python tools/governance/commit_timestamp_integrity.py             # المُعلَنُ والمقيسُ قبلَ الإحكامِ وبعدَه
  python -m pytest tests/governance/test_w110_commit_stamp_integrity.py tests/governance/test_w113_new_commit_stamp_utc.py -q
  # والقياسُ الأوّلُ الذي فتحَ البندَ: تشغيلُ CI 84 على العقدةِ `0b907583` — فحصانِ ساقطانِ سببُهما إزاحةُ `+03:00`
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-11
  (‏نافذةٌ مُعلَنةٌ لا حجزٌ: الحالةُ `READY` فلا تقفلُ مسارًا · § 6.1)
العائق: لا عائقَ فنيًّا. والمسارانِ مُدَّعيانِ لبندَينِ `IN_REVIEW` فلا يُحجَزُ قبلَ تحرُّرِهما — والانتظارُ مُعلَنٌ لا مطويٌّ.
الخطوةُ التالية: حجزُ البندِ متى تحرَّرَ المسارانِ، ثمَّ إنزالُ الوجهِ والشرطِ المكتوبِ بحرسٍ يُثبِتُ الفرقَ بطفرةٍ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **العَطبُ في أداةِ الدفعِ لا في محتوى العملِ**، فحرسٌ يقرأُ الشجرةَ وحدَها لا يراه: ما يُقاسُ هنا هو رأسُ الفرعِ بعدَ الدفعِ — وذاكَ حدٌّ مكتوبٌ لا مطويٌّ
  - **ولا يُدَّعى منعُ العَطبِ قبلَ وقوعِه**: أقصى ما يُبنى قياسٌ يكشفُه في اللحظةِ التاليةِ للدفعِ فيُصحَّحُ قبلَ أن يُبنى عليه غيرُه
قيدُ السجلّ: — (‏البندُ لم يُنجَزْ بعدُ · والقيدُ الذي فتحَه `W-127`)
```

---

### WI-040 — صفُّ الجدولِ يُقرأُ كما كُتِبَ، لا كما شطرَه محرفٌ

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-048` قُيِّدَ في `W-126` وأُصلِحَ موضعٌ واحدٌ منه)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: READY   (‏`PROPOSED` ← `READY` بلا قفزٍ · § 4.3 · ولا تقفلُ مسارًا § 6.1)
المسارات (‏مقيسةٌ لا مُقدَّرةٌ — أمرُ القياسِ في «الدليلُ المطلوب» أدناه):
  tools/governance/check_work_governance.py                        (‏السطرُ 215 — قسمٌ ساذجٌ · وحدُّ عددِ الأعمدةِ فيه **ثنائيُّ الجهةِ** أصلًا، فالناقصُ هو تمييزُ المهروبِ وحدَه)
  tools/governance/guard_enforcement_closure.py                    (‏السطرُ 142 — قسمٌ ساذجٌ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `check_work_governance.py` **مُدَّعًى لـ`WI-037` وحالتُه `IN_REVIEW`** — فلا يُمَسُّ اليومَ، و`READY` لا تقفلُ مسارًا فلا `CLAIM_CONFLICT`
  - `guard_enforcement_closure.py` لا مُدَّعيَ له في صفوفِ § 1
  - ولا يُمَسُّ `open_record_accountability.py` (‏مُدَّعًى لـ`WI-039` · وقد أُصلِحَ موضعُه هناكَ)
  - ولا `.github/workflows/ci.yml` (‏مقفولٌ بـ`WI-023`)
خارج النطاق:
  - **لا يُوحَّدُ القارئُ في وحدةٍ مشتركةٍ في هذا البندِ**: توحيدُ قارئٍ لأدواتِ الحوكمةِ كلِّها قرارٌ هندسيٌّ أوسعُ يُرفَعُ `Q-###` إن لزمَ، لا يُقرَّرُ في إحكامِ عَطبٍ
  - ولا يُحذَفُ نصٌّ من سجلٍّ لأنَّه يحملُ محرفَ أنبوبٍ: **يُهرَبُ المحرفُ ولا يُمحى النصُّ**
  - ولا تُخفَّفُ حدودُ عددِ الأعمدةِ القائمةُ ولا يُسكَتُ صنفُ `MALFORMED_ITEM`
معيار القبول:
  1. كلُّ قارئِ صفٍّ من المسارَينِ يقسِمُ على محرفِ أنبوبٍ **غيرِ مهروبٍ** وحدَه، و`\|` يُقرأُ محتوًى فيُزالُ هربُه في نصِّ الخليّةِ
  2. عددُ الأعمدةِ مُلزَمٌ في الجهتَينِ في كلِّ قارئٍ منهما، والرسالةُ تُسمّي الزيادةَ وسببَها لا العددَ وحدَه
  3. الحرسُ **مُجرَّبٌ بطفرةٍ**: إعادةُ القسمِ الساذجِ تُسقِطُ فحصًا مُسمًّى، ورفعُ حدِّ العددِ يُسقِطُ فحصًا مُسمًّى
  4. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  5. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب (‏والقياسُ الأوّلُ للمسارَينِ جرى في `W-126`):
  grep -rn 'split("|")' tools/                                     # الموضعانِ: check_work_governance.py:215 · guard_enforcement_closure.py:142
  python tools/governance/check_work_governance.py --self-check     # خروجٌ 0 قبلَ الإحكامِ وبعدَه
  python tools/governance/guard_enforcement_closure.py              # خروجٌ 0 قبلَ الإحكامِ وبعدَه
  python -m pytest tests/governance/ -q                             # لا فحصَ يسقُطُ
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-11
  (‏نافذةٌ مُعلَنةٌ لا حجزٌ: الحالةُ `READY` فلا تقفلُ مسارًا · § 6.1 — والحجزُ يُعلَنُ بانتقالٍ مُسجَّلٍ إلى `RESERVED`)
العائق: لا عائقَ فنيًّا. والمسارُ الأوّلُ مُدَّعًى لـ`WI-037` (`IN_REVIEW`) فلا يُحجَزُ قبلَ تحرُّرِه — والانتظارُ مُعلَنٌ لا مطويٌّ.
الخطوةُ التالية: حجزُ البندِ متى تحرَّرَ `check_work_governance.py`، ثمَّ إحكامُ القاسمَينِ بحرسٍ يُثبِتُ الفرقَ بطفرةٍ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الموضعانِ مقيسانِ بأمرٍ واحدٍ، ولا يُدَّعى أنَّهما كلُّ قارئاتِ الجداولِ**: أدواتٌ أخرى تكتُبُ جداولَ ولا تقرأُها (`evidence_registry.py` · `truth_audit.py`) فليست في النطاقِ، وما لم يُقَسْ لا يُعلَنُ
  - و`check_work_governance.py` كانَ يرفضُ الزيادةَ والنقصَ أصلًا، فعَطبُه **الهربُ وحدَه** — والفرقُ يُكتَبُ ولا يُعمَّمُ
قيدُ السجلّ: — (‏البندُ لم يُنجَزْ بعدُ · والقيدُ الذي فتحَه `W-126`)
```

---

### WI-039 — المِرساةُ إعلانٌ مُهيكَلٌ يُقرأُ، لا مسارٌ يمرُّ في نثرٍ

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-021` مفتوحٌ منذ `W-060` ولا حرسَ له)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_PROGRESS   (‏`RESERVED` ← `IN_PROGRESS` بلا قفزٍ · § 4.3 · قيدُ `W-125`)
المسارات:
  tools/governance/open_record_accountability.py                   (‏قائمٌ — يُشدَّدُ مُصنِّفُ المِرساةِ فيه)
  tests/governance/test_w124_anchor_declaration.py                 (‏نزلَ في `W-125` — و**صارَ 29 فحصًا في `W-126`**: قراءةُ الإعلانِ · السقّاطةُ · رفضٌ مُصنَّفٌ · طفرتانِ لحدِّ الأعمدةِ · المستودعُ الحقيقيُّ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - المسارُ الأوّلُ كانَ مُدَّعًى لـ`WI-014`، **و`WI-014` مُغلَقٌ** (‏قيدُ `W-067`) — فأُعيدَ قياسُ الدعوى من صفوفِ § 1: **ستّةَ عشرَ بندًا غيرَ مُغلَقٍ ولا واحدٌ منها يُعلِنُ هذا المسارَ**، فالحاجزُ المكتوبُ في `DISC-021` لم يَعُدْ قائمًا ولم يُلغَ نصُّه بل قُيِّدَ إعادةُ قياسِه
  - والملفُّ الثاني لا وجودَ له بعدُ فلا مُدَّعيَ له
  - ولا يُمَسُّ `.github/workflows/ci.yml` (‏مقفولٌ بـ`WI-023`) · ولا `check_completion_ledger.py` (‏مُدَّعًى) · ولا `check_work_governance.py` (‏مُدَّعًى لـ`WI-037`)
  - والفحصُ تحتَ `tests/governance/` فيُنفَّذُ بخطوتَيْ `pytest` القائمتَينِ — إنفاذٌ بلا مسِّ مسارٍ مقفولٍ
خارج النطاق:
  - **لا تُخفَّفُ الأداةُ ولا يُحذَفُ صنفٌ من أصنافِ المِرساةِ**: الشِّدَّةُ تُزادُ ولا تُنقَصُ
  - ولا تُصحَّحُ صفوفُ سجلَّي الاكتشافاتِ والمخاطرِ **بادِّعاءِ حرسٍ لا يوجدُ**: من لا حرسَ له يُعلَنُ بلا حرسٍ
  - ولا يُحسَمُ قرارُ مالكٍ (`A-2` · `A-3`)
معيار القبول (‏عُدِّلَ البندُ 1 في `W-125` بقياسِ ملكيّةٍ لا برغبةٍ — والسببُ في «العائق» أدناه):
  1. مسارٌ لا يقعُ في **إعلانٍ مُهيكَلٍ للحرسِ** لا يُعَدُّ مُعلَنًا، ويُعَدُّ صفُّه في «مسارٍ في نثرٍ» برقمٍ مُعلَنٍ لا يعلو
     (‏والأصلُ المكتوبُ: «لا يُقرأُ مِرساةً» — وقلبُ حقلِ `anchor` نفسِه يمسُّ حرسًا مُدَّعًى لبندٍ `IN_REVIEW` فلا يُمَسُّ اليومَ)
  2. النصُّ الذي أنتجَ الخُضرةَ الكاذبةَ في `W-060` يُعادُ حرفًا في فحصٍ فيُقرأُ **بلا مِرساةٍ** لا `GUARD`
  3. ما بقيَ من مساراتٍ في نثرٍ غيرِ مُعلَنٍ **يُعَدُّ ويُسمَّى برقمٍ لا يعلو** (‏سقّاطةٌ تمنعُ النموَّ ولا تُبيحُ القائمَ)
  4. الحرسُ **مُجرَّبٌ بطفرةٍ**: تعطيلُ شرطِ الإعلانِ يُسقِطُ فحوصًا مُسمّاةً
  5. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب (‏أُعيدَ قياسُه في `W-126` · 2026-09-03 · والسابقُ في `W-125` يبقى مكتوبًا في السجلِّ):
  python tools/governance/open_record_accountability.py                        # خروجٌ 0 · 69 صفًّا · 51 مفتوحًا · 29 محروسًا · باستحقاقٍ 2 · بلا مِرساةٍ 0
  python tools/governance/open_record_accountability.py --declaration-check    # خروجٌ 0 · مُعلَنٌ حرسُها 27 · مسارٌ في نثرٍ 2 = السقّاطةُ 2
  python -m pytest tests/governance/test_w124_anchor_declaration.py -q         # 29 نجحَت (‏21 ← 29)
  # وقِيسَ في `W-125`: خروجٌ 0 · 68 صفًّا · 50 مفتوحًا · مُعلَنٌ حرسُها 4 · نثرٌ 25 · 21 فحصًا
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-30
العائق: **قلبُ التصنيفِ محجوبٌ بملكيّةٍ لا بفنٍّ** — جعلُ صفِّ النثرِ يُقرأُ «بلا مِرساةٍ» يُسقِطُ فحوصًا قائمةً في
  `tests/governance/test_w059_open_record_accountability.py` (‏تُثبِتُ اليومَ أنَّ مسارًا في نثرٍ يُقرأُ `GUARD`)، وذاك الملفُّ
  **مُدَّعًى لـ`WI-033` وحالتُه `IN_REVIEW`** — فتعديلُه خرقُ قفلِ النطاقِ (§ 6). فنزلَ في هذا القيدِ ما لا يمسُّ مُدَّعًى:
  طبقةُ إعلانٍ مقيسةٌ وسقّاطةٌ تمنعُ النموَّ، وحرسُها في ملفٍّ مملوكٍ لهذا البندِ.
الخطوةُ التالية: **قلبُ حقلِ `anchor` نفسِه متى تحرَّرَ `tests/governance/test_w059_open_record_accountability.py` من دعوى `WI-033`** — وهو ما بقيَ من معيارِ القبولِ 1
  (‏وقد تمَّت في `W-126` ترقيةُ الصفوفِ صفًّا صفًّا: **25 ← 2** بمراجعةِ ثلاثةٍ وعشرينَ صفًّا، ولم يُرَقَّ `DISC-007` ولا `DISC-032` لأنَّ مسارَيهما موضعُ عَطبٍ لا حارسُه)
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الإعلانُ لا الكفايةُ**: الأداةُ تقيسُ أنَّ الحرسَ **مُعلَنٌ بشكلٍ يُقرأُ**، ولا تقيسُ أنَّه يحرسُ عينَ العَطبِ المُقيَّدِ — وذاكَ حكمٌ بشريٌّ يبقى على حالِه
  - **والقائمُ لا يُبرَّأُ**: الصفوفُ التي تذكرُ مساراتِها نثرًا اليومَ تُعَدُّ رقمًا مُعلَنًا يُمنَعُ نموُّه، وخفضُه يجري صفًّا صفًّا بمراجعةٍ لا بجملةٍ
  - **وقُيِّدَ في `W-126` عَطبٌ في الأداةِ نفسِها لا في السجلّاتِ** (`DISC-048`): قاسمُ الخلايا كانَ يرفضُ النقصَ ويُمَرِّرُ الزيادةَ،
    فصفّانِ بتسعِ خلايا (`DISC-032` · `RK-013`) حُكِمَ عليهما بعمودٍ مُزاحٍ في كلِّ تشغيلٍ سابقٍ بلا مخالفةٍ — وأُصلِحَ سببُه هنا لأنَّ الملفَّ مُدَّعًى لهذا البندِ،
    **ومسحُ سائرِ قارئاتِ الجداولِ خارجَ هذا البندِ** ووُجِّهَ إلى `WI-040`
قيدُ السجلّ: W-124 (‏الحجزُ) · و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`)
```

---

### WI-038 — حجمُ الحزمةِ رقمٌ يُقاسُ بأمرٍ رخيصٍ لا يُنقَلُ

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-046` · استحقاقُه 2026-09-10 ولا حرسَ له)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_PROGRESS   (‏`IN_REVIEW → IN_PROGRESS` · § 4.3 — انتقالٌ مشروعٌ أوجبَه ردُّ المجلسِ في الجولةِ الخامسةِ)
المسارات:
  tools/governance/suite_size_inventory.py                         (‏جديدٌ — يجمعُ الحزمَ ويُقارِنُ بالمكتوبِ)
  tests/governance/test_w120_suite_size_claims.py                  (‏جديدٌ — يُثبِتُ أنَّ رقمًا ميّتًا يُرَدُّ)
  **ولا يُدَّعى `docs/PROJECT_HANDBOOK.md` مِلكًا**: مقفولٌ بـ`WI-023` وهو `IN_REVIEW`، ونطاقُ بندٍ في المراجعةِ لا يُقسَمُ ولا يُوسَّعُ (§ 6.1).
  فتصحيحُ رقمِه يقعُ تحتَ **واجبِ § 7 (4)** الذي يُلزِمُ بمطابقةِ وثائقِ الحالةِ للواقعِ بعدَ كلِّ دمجٍ — مَسٌّ بواجبٍ مكتوبٍ لا حجزٌ ثانٍ
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - المساراتُ المحجوزةُ **لا يُعلِنُها بندٌ نشِطٌ**: الملفّانِ لا وجودَ لهما بعدُ فلا مُدَّعيَ لهما. و`PROJECT_HANDBOOK.md` **يُعلِنُه `WI-023`** (`IN_REVIEW`) فلم يُحجَزْ هنا — وأوّلُ محاولةٍ لحجزِه أسقطَتِ البوّابةَ بـ`CLAIM_CONFLICT` فصُحِّحَ الحجزُ لا البوّابة
  - ولا `ci.yml` يُمَسُّ (‏مقفولٌ بـ`WI-023`) · ولا `check_completion_ledger.py` (‏مُدَّعًى) · ولا أداةَ قائمةً تُعدَّلُ · ولا جدولَ ولا migration ولا سرَّ
  - والفحصُ تحتَ `tests/governance/` فيُنفَّذُ بخطوتَيْ `pytest` القائمتَينِ (‏وظيفةُ `test` تُشغِّلُ `tests/` كلَّها بتبعيّاتٍ كاملةٍ) — إنفاذٌ بلا مسِّ مسارٍ مقفولٍ
خارج النطاق:
  - **لا تُعدَّلُ قيودُ § 8 التاريخيّةُ ولا أرقامُها**: كانت صادقةً يومَ كُتِبَت، والمُصحَّحُ دعوى «الآنَ» وحدَها
  - ولا يُمَسُّ `measurement_provenance.py` ولا عقدُ ملفّاتِ `docs/audit/measurements/` — هذا الحرسُ يقرأُ **نثرًا** لا ملفَّ قياسٍ، ولا يُنشِئُ ملفَّ قياسٍ جديدًا (‏مصدرُ حقيقةٍ ثانٍ)
  - ولا يُقاسُ **زمنُ** الحزمةِ حرسًا (‏يتبدَّلُ بالعتادِ فيصيرُ حاجزًا كاذبًا) — الزمنُ يبقى مُؤرَّخًا مُعلَنًا
خارج النطاق: لا يُحسَمُ قرارُ مالكٍ (`A-2` · `A-3`)
معيار القبول:
  1. كلُّ حزمةٍ مُعلَنةٍ في الوثيقةِ تحملُ **عددَ جمعٍ** (‏`--collect-only`) مكتوبًا بشكلٍ واحدٍ يقرؤه الحرسُ
  2. الحرسُ يجمعُ الحزمةَ **حيًّا** ويُسقِطُ الاختلافَ بمخالفةٍ مُسمّاةٍ — ولا يُصلِحُ ما يحكمُ عليه
  3. حزمةٌ **يتعذَّرُ جمعُها** (‏تبعيّاتٌ غائبةٌ) تُعلَنُ بسببِها المكتوبِ وتُعَدُّ ظاهرةً — لا تُطوى صامتةً
  4. الرقمُ المكتوبُ يُصحَّحُ **بقياسٍ طازجٍ في هذه العقدةِ** لا بنقلٍ، وأرقامُ النجاحِ/التخطّي تبقى مُؤرَّخةً مُعلَنةَ الحدِّ
  5. الحرسُ **مُجرَّبٌ بطفرةٍ**: يُغيَّرُ الرقمُ المكتوبُ بواحدٍ فيسقطُ، ويُعادُ فيقومُ
  6. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  7. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python tools/governance/suite_size_inventory.py . --check
  python -m pytest tests/governance/test_w120_suite_size_claims.py -q
  python -m pytest tests/ -q
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-30
العائق: — **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، والحكمُ: `REJECTED` بإجماعِ المراجعَينِ** (أ `P1=3` · ب `P1=4` و`P2=1`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ تلكَ العيوبِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ.
الخطوةُ التالية: معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`)
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الجمعُ لا التنفيذُ**: المحروسُ عددُ ما يُجمَعُ (‏رخيصٌ · دون ثانيةٍ)، لا عددُ ما ينجحُ — فحزمةٌ تُجمَعُ ولا تُشغَّلُ لا يكشِفُها هذا الحرسُ، وذاكَ عملُ الحزمةِ نفسِها في CI
  - **وحزمةُ الخدماتِ لا تُجمَعُ في وظيفةِ بوّاباتِ الحوكمةِ** (‏حزمتُها غيرُ مُثبَّتةٍ هناك) — فتُعلَنُ «غيرُ مقيسةٍ هنا» بسببٍ مكتوبٍ، ويبقى إنفاذُها محلّيًّا وفي وظيفةِ `test`
قيدُ السجلّ: W-120 (‏الحجزُ) · W-123 (‏حكمُ تشغيلِ 80 أخضرَ 13/13 `READABLE` فسُلِّمَ للمراجعةِ) · W-121 (‏نزولُ الأداةِ والحرسِ وتصحيحُ الرقمِ: 13 فحصًا · 4 مواضعَ صُحِّحَت · حزمةُ الخدماتِ مُعلَنةٌ «غيرُ مقيسةٍ» في وظيفةِ بوّاباتِ الحوكمةِ بسببٍ مكتوبٍ) · W-122 (‏حكمُ CI 79 الأحمرُ: الإعفاءُ البيئيُّ صارَ يُقرأُ من خرجِ الجمعِ بأسماءِ الحزمِ الغائبةِ · `DISC-047` قُيِّدَ وأُغلِقَ · 17 فحصًا) · و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`)
حكمُ الجولةِ الخامسةِ من مجلسِ المراجعةِ — مُقيَّدٌ كما وردَ لا كما يُشتَهى:
  العقدةُ المُراجَعةُ: `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` · التاريخُ: 2026-09-13
  المراجعُ أ (‏GPT 5.6 Sol) والمراجعُ ب (‏Grok 4.6) في حاويتَينِ منفصلتَينِ، كلٌّ أعادَ
  تشغيلَ الدليلِ بنفسِه وقرأَ حكمَ CI بنفسِه من الواجهةِ — والحكمُ: **`REJECTED` بإجماعِ المراجعَينِ**
  (أ `P1=3` · ب `P1=4` و`P2=1`).
  والعيوبُ باتّحادِها مُقيَّدةٌ في `DISC-063` ولم تُصلَحْ في هذا البندِ ولا في قيدِ التقييدِ
  (§ 5.2 — تقييدُ حكمٍ لا إصلاحُ عيبٍ). ولم يُنقَلْ بندٌ إلى `VERIFIED`: الإجماعُ شرطُ `Q-43`.

```

---

### WI-037 — خليّةُ المساراتِ تُقرأُ مساراتٍ لا نثرًا: دعوى لا تتَّسِعُ بما لم تُكتَبْ

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-042` · استحقاقُه 2026-09-09 ولا حرسَ له)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_PROGRESS   (‏`IN_REVIEW → IN_PROGRESS` · § 4.3 — انتقالٌ مشروعٌ أوجبَه ردُّ المجلسِ في الجولةِ الخامسةِ)
المسارات:
  tools/governance/check_work_governance.py                        (‏تشديدُ قراءةِ خليّةِ المساراتِ في § 1)
  tests/governance/test_w117_claim_cell_shape.py                   (‏جديدٌ — يُثبِتُ أنَّ نثرًا لا يُغطّي ملفًّا)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `check_work_governance.py` **لا يُعلِنُه بندٌ نشِطٌ**: قُرِئَ جدولُ § 1 كلُّه — البنودُ `WI-023`…`WI-036` لا واحدَ منها يُعلِنُه، والبنودُ التي أعلنَته (`WI-001` · `WI-020` · `WI-021`) **مُغلَقةٌ** فلا حجزَ قائمًا (§ 6.1). فالحاجزُ المكتوبُ في `DISC-042` («مُدَّعًى لبندٍ في يدِ المراجعِ») **صَدَقَ يومَ كُتِبَ ولم يَعُدْ قائمًا** — والقياسُ يُعادُ لا يُورَثُ
  - ولا `ci.yml` يُمَسُّ (‏مقفولٌ بـ`WI-023`) · ولا أداةَ أخرى تُعدَّلُ · ولا جدولَ ولا migration ولا سرَّ
  - والفحصُ تحتَ `tests/governance/` فيُنفَّذُ بخطوتَيْ `pytest` القائمتَينِ — إنفاذٌ بلا مسِّ مسارٍ مقفولٍ
خارج النطاق:
  - **لا تُوسَّعُ دعوى بندٍ ولا تُضيَّقُ**: ما تُغطّيه المساراتُ المكتوبةُ اليومَ يبقى كما هو — المُنجَزُ **منعُ قراءةِ نثرٍ دعوى**
  - ولا تُمَسُّ قواعدُ الانتقالِ ولا `CLAIM_CONFLICT` نفسُه ولا أعفاءُ السجلّاتِ (§ 6)
  - ولا يُحسَمُ قرارُ مالكٍ (`A-2` · `A-3` · `origin/develop`)
معيار القبول:
  1. جزءٌ من خليّةِ المساراتِ **لا يُطابِقُ شكلَ مسارٍ يُرفَضُ صراحةً** بمخالفةٍ مُسمّاةٍ، ولا يُقرأُ دعوى تُغطّي شيئًا
  2. خليّةٌ تبدأُ بعلامةِ الفراغِ («—») **تُقرأُ إعلانَ «لا مسارَ يُحجَزُ»**، وما بعدَها تعليلٌ مكتوبٌ لا دعوى — فلا يُكسَرُ صفٌّ صادقٌ قائمٌ
  3. الحرسُ **يُثبِتُ الفخَّ**: نثرٌ يذكرُ مجلَّدًا **لا يُغطّي** ملفًّا تحتَه، **ويُثبِتُ عكسَه**: مسارٌ مكتوبٌ اسمًا يُغطّي ما تحتَه
  4. الشجرةُ الحيّةُ **خاليةٌ** من الأجزاءِ غيرِ المساريّةِ (‏المقيسُ اليومَ **8** أجزاءٍ في 4 بنودٍ)، ونصُّها **يُنقَلُ إلى كتلةِ تفاصيلِ بندِه لا يُحذَفُ**
     (‏**نُفِّذَ ومُقيسٌ**: 8 ← 0 · والنقلُ لم يُغيِّرْ تغطيةً — قُورِنَت التغطيةُ قبلَ التشديدِ وبعدَه على **1855** ملفًّا مُتتبَّعًا فتبدَّلَ **صفرٌ**. وعلامةُ الفراغِ رفعَت 4 منها بلا مسِّ صفٍّ صادقٍ)
  5. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python -m pytest tests/governance/test_w117_claim_cell_shape.py -q
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_work_governance.py --staged
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-30
العائق: — **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، والحكمُ: `REJECTED` بانقسامٍ لا يُجمَعُ جمعًا حسابيًّا** (أ `VERIFIED` `P1=0` · ب `REJECTED` `P1=2` و`P3=1`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ تلكَ العيوبِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ.
الخطوةُ التالية: معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`)
حكمُ CI المقروءُ (‏الأحدثُ): عقدةُ `c5d3798` · تشغيلُ `33707717108` (‏رقمُ **76**) ⇒ `completed success` · **13/13** وظيفةً · `READABLE` رمزُ 0
                            ومصفوفةُ الحقيقةِ `33707717114` (‏رقمُ 77) `success` · وعقدةُ الحجزِ `8df135d` قُرِئَت أيضًا خضراءَ 13/13 (‏تشغيلُ `33706767478`)
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الشكلُ لا الوجودُ**: لا يُشترَطُ أن يوجدَ الملفُّ (‏بندٌ يُعلِنُ ملفًّا سيُنشِئُه) — فمسارٌ مكتوبٌ خطأً ولا يوجدُ يمرُّ، وهذا حدٌّ مُعلَنٌ
  - **ودعوى المجلَّدِ تبقى مشروعةً**: `tests/governance` مكتوبًا مسارًا يُغطّي ما تحتَه — المرفوضُ نثرٌ **حولَه** لا المسارُ نفسُه
قيدُ السجلّ: W-117 (‏الحجزُ) · و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`)
حكمُ الجولةِ الخامسةِ من مجلسِ المراجعةِ — مُقيَّدٌ كما وردَ لا كما يُشتَهى:
  العقدةُ المُراجَعةُ: `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` · التاريخُ: 2026-09-13
  المراجعُ أ (‏GPT 5.6 Sol) والمراجعُ ب (‏Grok 4.6) في حاويتَينِ منفصلتَينِ، كلٌّ أعادَ
  تشغيلَ الدليلِ بنفسِه وقرأَ حكمَ CI بنفسِه من الواجهةِ — والحكمُ: **`REJECTED` بانقسامٍ لا يُجمَعُ جمعًا حسابيًّا**
  (أ `VERIFIED` `P1=0` · ب `REJECTED` `P1=2` و`P3=1`).
  والعيوبُ باتّحادِها مُقيَّدةٌ في `DISC-063` ولم تُصلَحْ في هذا البندِ ولا في قيدِ التقييدِ
  (§ 5.2 — تقييدُ حكمٍ لا إصلاحُ عيبٍ). ولم يُنقَلْ بندٌ إلى `VERIFIED`: الإجماعُ شرطُ `Q-43`.

```

---

### WI-036 — أرقامُ حدودِ الصدقِ: تفرُّدٌ يُقاسُ وإحالةٌ تُحَلُّ

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-045`: § 10 تُعلِنُ 17 حدًّا مرقومةً 1…16 والرقمُ 9 مكتوبٌ مرّتَينِ)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW    (‏حكمٌ أخضرُ مقروءٌ 13/13 على عقدةِ `c817ada` · تشغيلٌ 73 — ولا يضعُ الكاتبُ `VERIFIED` · § 4.3)
المسارات:
  tools/governance/truth_limit_integrity.py                        (‏جديدٌ — يقيسُ ولا يُصحِّحُ)
  tests/governance/test_w115_truth_limit_integrity.py              (‏جديدٌ — حرسُ «لا نموَّ» + إثباتُ الفخِّ على نصٍّ مصنوعٍ)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - الملفّانِ **جديدانِ ومُعدَّدانِ اسمًا** في خليّةِ مساراتِ هذا البندِ لا نثرًا يُقرأُ دعوى مجلَّدٍ (‏درسُ `DISC-042`): قِيسَ على خلايا المساراتِ كلِّها — لا تداخل
  - ولا `ci.yml` يُمَسُّ (‏مقفولٌ بـ`WI-023`) · ولا أداةَ قائمةً تُعدَّلُ · ولا `check_completion_ledger.py` يُمَسُّ (‏مُدَّعًى لبندٍ في يدِ المراجعِ · § 6.1)
  - و**نصُّ § 10 نفسُه لا يُعادُ ترقيمُه** فلا يُمَسُّ سطرٌ مُحالٌ إليه من قيدٍ مدفوعٍ
خارج النطاق:
  - **لا يُعادُ ترقيمُ حدودِ § 10**: الأرقامُ مُحال إليها من قيودٍ مدفوعةٍ لا تُمحى، وترقيمٌ جديدٌ يكسِرُ إحالاتٍ صادقةً
  - ولا يُقاسُ **صدقُ الحدِّ** نفسِه ولا يُغلَقُ حدٌّ: المقيسُ **تفرُّدُ المُعرِّفِ وحلُّ الإحالةِ** لا مضمونُ الحدِّ
  - ولا تُمَسُّ سجلّاتُ الحوكمةِ الأُخرى ولا بوّابةُ السجلِّ القائمةُ
معيار القبول:
  1. الالتباسُ يصيرُ **رقمًا يُعادُ** من نصِّ § 10 لا فقرةً تُروى: عددُ الحدودِ · الأرقامُ المكرَّرةُ · الفجواتُ · والإحالاتُ التي لا تُحَلُّ
  2. نموُّ أيِّ رقمٍ يُسقِطُ الفحصَ · وانخفاضُه يوجبُ خفضَ المُعلَنِ (‏سقّاطةٌ لا تعلو ولا تُترَكُ رخوةً)
  3. الحرسُ **يُثبِتُ أنَّ القياسَ يرى العيبَ** على نصٍّ مصنوعٍ فيه تكرارٌ وفجوةٌ وإحالةٌ ملتبسةٌ، **ويُثبِتُ عكسَه** على نصٍّ سليمٍ فلا تُقاسُ خُضرةٌ بلا فرقٍ
     (‏**تصحيحُ صياغةٍ مقيسٌ لا تخفيفٌ**: كُتِبَ عندَ الحجزِ «إحالةٌ معلَّقةٌ» ثمَّ وقعَ مقيسًا أنَّ الإحالةَ المعلَّقةَ **لا تُفرَّقُ نصًّا** عن رقمٍ أجنبيٍّ عن القسمِ — فالعبارةُ نفسُها تُستعملُ لغيرِ الحدودِ («الحدُّ 80%» عن نسبةٍ) فعَدُّها معلَّقةً حكمٌ كاذبٌ. فالمحكومُ به **الإحالةُ الملتبسةُ**: رقمٌ داخلَ مدى الترقيمِ يحملُه أكثرُ من حدٍّ — وهي **عينُ عَطبِ `DISC-045`**. وما خرجَ عن المدى يُطبَعُ إبلاغًا لا حكمًا (`OUTSIDE_RANGE_REFERENCES`) فلا يُحذَفُ أثرُه ولا يُدَّعى فيه صدقٌ)
  4. الرقمُ المُعلَنُ مصدرُه **سطرٌ واحدٌ** في `DISCOVERIES.md` لا ثابتٌ في فحصٍ (‏مصدرُ حقيقةٍ واحدٌ)
  5. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليل المطلوب:
  python -m pytest tests/governance/test_w115_truth_limit_integrity.py -q        (‏10 نجحَت)
  python tools/governance/truth_limit_integrity.py --check                       (‏رمزُ 0)
  python tools/governance/truth_audit.py . --ratchet                             (‏ثابتٌ عندَ 63 — بعدَ إصلاحِ `SILENT_FALLBACK` أحدثَته النسخةُ الأولى في نفسِها)
بدأ: 2026-09-03        ينتهي الحجز: 2026-09-30
العائق: —
الخطوةُ التالية: مراجعةٌ مستقلّةٌ — والمنفِّذُ لا يملكُ `VERIFIED` (`DISC-027` · `RK-020`)
حكمُ CI المقروءُ (‏الأحدثُ): عقدةُ `c817ada` · تشغيلُ `33704390584` (‏رقمُ **73**) ⇒ `completed success` · **13/13** وظيفةً · `READABLE` رمزُ 0
                            ومصفوفةُ الحقيقةِ `33704390613` (‏رقمُ 74) `success` — قُرِئَ برقمِ تشغيلٍ ولم يُستنتَجْ من خُضرةٍ محلّيّةٍ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الحرسُ يقيسُ شكلَ المُعرِّفِ لا صدقَ الحدِّ**: حدٌّ فريدُ الرقمِ قد يكونُ كاذبَ المضمونِ — وهذا لا يُقاسُ هنا
  - **والالتباسُ القائمُ لا يُرفَعُ**: الرقمُ 9 يبقى مكتوبًا مرّتَينِ مُعلَنًا مقيسًا، والحرسُ يمنعُ زيادتَه فقط
  - وقياسُ الإحالاتِ نصّيٌّ (‏أنماطُ «الحدِّ N» في `.md`/`.py`) فصياغةٌ جديدةٌ للإحالةِ قد لا تُرى — والحدُّ مُعلَنٌ لا مطويٌّ
  - **والإحالةُ المعلَّقةُ خارجَ المدى لا تُحكَمُ بها**: لا يُفرَّقُ نصًّا رقمٌ أجنبيٌّ عن القسمِ عن إحالةٍ إلى حدٍّ غيرِ موجودٍ، فتُطبَعُ إبلاغًا (`OUTSIDE_RANGE_REFERENCES`) ولا تُدخَلُ في السقّاطةِ — إعلانُ حدٍّ لا إسقاطُ أثرٍ
قيدُ السجلّ: W-114 (‏الحجزُ) · و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`)
```

---

### WI-035 — صدقُ طوابعِ الالتزامِ: رقمٌ يُقاسُ ويُحرَسُ من النموِّ

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — حدُّ الصدقِ 9 المُعلَنُ منذُ `W-028` بلا رقمٍ ولا حرسٍ · `DISC-043`)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_PROGRESS   (‏`IN_REVIEW → IN_PROGRESS` · § 4.3 — انتقالٌ مشروعٌ أوجبَه ردُّ المجلسِ في الجولةِ الخامسةِ)
المسارات:
  tools/governance/commit_timestamp_integrity.py                   (‏جديدٌ — يقيسُ ولا يُصحِّحُ)
  tests/governance/test_w110_commit_stamp_integrity.py             (‏جديدٌ — حرسُ «لا نموَّ» + إثباتُ الفخِّ على سجلٍّ مصنوعٍ)
  tests/governance/test_w113_new_commit_stamp_utc.py               (‏جديدٌ `W-113` — حرسٌ **سابقٌ للدفعِ**: ما بعدَ `baseline_node` إزاحتُه `+00:00`)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - الملفّانِ **جديدانِ** ولا يُعلِنُهما بندٌ `RESERVED`/`IN_PROGRESS`/`IN_REVIEW`: قِيسَ على خلايا المساراتِ كلِّها — لا تداخل
  - وملفُّ `test_w113_new_commit_stamp_utc.py` **جديدٌ ومُعدَّدٌ اسمًا** في خليّةِ مساراتِ هذا البندِ لا نثرًا يُقرأُ دعوى مجلَّدٍ (‏درسُ `DISC-042`): قِيسَ على خلايا المساراتِ كلِّها — لا تداخل
  - ولا `ci.yml` يُمَسُّ (‏مقفولٌ بـ`WI-023`) · ولا أداةَ قائمةً تُعدَّلُ · ولا جدولَ ولا migration ولا سرَّ · ولا قرارَ `Q-###` يتوقَّفُ عليه
خارجَ النطاق:
  - **لا يُصحَّحُ ماضٍ ولا يُعادُ كتابةُ تاريخٍ**: العشرةُ الالتزاماتُ ذاتُ الطوابعِ المكرَّرةِ تبقى كما هي — `force-push` يمحو قيودًا مدفوعةً وهو ممنوعٌ
  - ولا يُقاسُ **صدقُ الساعةِ** التي كتبَت الطابعَ: المقيسُ تناسُقُ الطوابعِ لا مطابقتُها لزمنِ العملِ الفعليِّ
  - ولا يُغلَقُ حدُّ الصدقِ 9 ولا `DISC-043`: قياسٌ وحرسٌ من النموِّ لا إبراءٌ
معيارُ القبول:
  1. الدَّينُ يصيرُ **رقمًا يُعادُ** من سجلِّ git لا فقرةً تُروى، ومصدرُه المُعلَنُ سطرٌ واحدٌ في `DISCOVERIES.md` (`COMMIT_STAMP_BASELINE:`)
  2. نموُّ أيِّ حقلٍ يُسقِطُ الفحصَ · وانخفاضُه على سجلٍّ كاملٍ يوجبُ خفضَ المُعلَنِ (‏سقّاطةٌ لا تعلو ولا تُترَكُ رخوةً)
  3. الحرسُ **يُثبِتُ أنَّ القياسَ يرى العيوبَ** على سجلٍّ مصنوعٍ فيه الثلاثةُ، فلا تُقاسُ خُضرةٌ بلا فرقٍ
  4. اكتمالُ السجلِّ يُقاسُ بعددِ الالتزاماتِ لا بعَلَمِ الضحالةِ وحدَه — ومرآةٌ ناقصةٌ **تُعلِنُ نقصَها** ولا تُوهِمُ بخفضٍ
  5. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
  7. (`W-113` · `DISC-044`) **النموُّ يُمنَعُ في مصدرِه لا يُرصَدُ بعدَ وقوعِه**: كلُّ التزامٍ واقعٍ بعدَ العقدةِ المُعلَنةِ (`baseline_node`) إزاحتُه `+00:00` أو يسقُطُ الفحصُ **قبلَ الدفعِ**، والعقدةُ تُقرأُ من السطرِ المُعلَنِ نفسِه لا تُخمَّنُ · وغيابُها عن مرآةٍ ضحلةٍ **يُعلَنُ** ولا يُقرأُ خُضرةً
الدليلُ المطلوب:
  python -m pytest tests/governance/test_w110_commit_stamp_integrity.py tests/governance/test_w113_new_commit_stamp_utc.py -q
  python tools/governance/commit_timestamp_integrity.py --check
  python tools/governance/truth_audit.py . --ratchet
بدأ: 2026-09-02        ينتهي الحجز: 2026-09-30
العائق: — **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، والحكمُ: `REJECTED` بانقسامٍ لا يُجمَعُ جمعًا حسابيًّا** (أ `VERIFIED` `P1=0` · ب `REJECTED` `P1=2`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ تلكَ العيوبِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ.
الخطوةُ التالية: معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`)
حكمُ CI المقروءُ (‏الأحدثُ): عقدةُ `2c59165` · تشغيلٌ **71** (`33697957662`) · **success · 13/13 · `READABLE`**
  ومصفوفةُ الحقيقةِ (`33697957637`) `success` · و`ci_verdict_readability.py --from-json` ⇒ `READABLE · 13/13` رمزُ 0
  فهذا **أوّلُ حكمٍ أخضرَ** بعدَ ثلاثةِ أحكامٍ حمراءَ مقروءةٍ على هذا البندِ، وبه نُقِلَ إلى `IN_REVIEW` بلا قفزٍ
  وقبلَه: عقدةُ `66c217b` · تشغيلٌ (`33621763476`) · **failure · 11/13**
  والوظيفتانِ الساقطتانِ «‏Identity Law · بوّابةُ 5» و«‏Cross-System Suites» · والفحصُ الساقطُ **واحدٌ**:
  `test_w110_commit_stamp_integrity.py::test_دَينُ_طوابعِ_الالتزامِ_لا_يعلو` ⇒ `non_utc: مقيسٌ 135 · المُعلَنُ 134`
  والسببُ **أنَّ العقدةَ التي أعلنَت 134 حملَت نفسُها إزاحةً `+03:00`** فزادَ الدَّينُ بواحدٍ لحظةَ الدفعِ — عَطبٌ بنيويٌّ قُيِّدَ `DISC-044`
  فصُحِّحَ المُعلَنُ **134 ← 135** (‏و`history_commits` 353 ← 356 مقيسًا من `git`)، ولم يُخفَّفْ فحصٌ ولم يُمسَحْ تاريخٌ
  بل **قُوِّيَ الحرسُ بوجهٍ ثانٍ سابقٍ للدفعِ** (`baseline_node` · `W-113`) يمنعُ 136 من أن تُولَدَ
  وأُعيدَ الفشلُ محلّيًّا بعينِه قبلَ الإصلاحِ: `pytest tests/governance/ -q` ⇒ **1 failed · 1014 passed**
  وقبلَه: عقدةُ `1e800dd` · تشغيلٌ **69** (`33614088205`) · **failure · 11/13**
  والسببُ **أنَّ مصدرَ القياسِ يُوحِّدُ الإزاحاتِ**: الواجهةُ البرمجيّةُ تُعيدُ كلَّ طابعٍ بـ`Z` فقاسَت `non_utc=0`
  و`git` في CI يقولُ **134 من 355** — فصارَ المُعلَنُ 134، و**حُذِفَ الفحصُ الذي كانَ يشترطُ صفرًا** لأنَّه دعوى كاذبةٌ (`W-112`)
  وقبلَه: عقدةُ `89efcdec` · تشغيلٌ **68** (`33610766326`) · **failure** — وظيفتانِ: «Identity Law · بوّابةُ 5» و«Cross-System Suites»
  والسببُ **خطأُ منهجٍ في الرقمِ المُعلَنِ**: `non_monotonic` قِيسَ بترتيبِ القائمةِ (3) والحرسُ يَعُدُّ بنسَبِ الأبوَّةِ (4)
  فصُحِّحَ المُعلَنُ **3 ← 4** ولم يُمَسَّ شرطٌ (`W-111`) · وعقدةُ التصحيحِ تُقرأُ في القيدِ التالي
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الرقمُ المُعلَنُ لا يُقاسُ محلّيًّا** بل عبرَ واجهةِ المستودعِ بخوارزميّةِ الأداةِ حرفًا — ومقياسانِ لشيءٍ واحدٍ أسقطا عقدةً فعلًا، والدرسُ مُقيَّدٌ
  - **المرآةُ المحلّيّةُ ناقصةٌ** (‏15 التزامًا مقابلَ 353 مُعلَنًا): فحصُ «الانخفاضُ يوجبُ الخفضَ» **يُتخطّى محلّيًّا بإعلانٍ** ويُقاسُ في CI حيثُ `fetch-depth: 0` — فالخُضرةُ المحلّيّةُ هنا أضعفُ من خُضرةِ CI ولا تُقرأُ بديلًا عنها
  - **والرقمُ المُعلَنُ قِيسَ من الواجهةِ البرمجيّةِ للمستودعِ** (353 التزامًا على `main`) لا من المرآةِ — ومصدرُه مُصرَّحٌ به في `DISC-043`
  - ~~**ولا حرسَ على الطابعِ قبلَ كتابتِه**~~ — **وقعَ هذا الحدُّ مقيسًا لا متوقَّعًا فأسقطَ عقدةً** (`DISC-044`)، فصارَ الحرسُ وجهَينِ: مجموعٌ لا يعلو (‏بَعديٌّ)، و**كلُّ جديدٍ بعدَ `baseline_node` إزاحتُه `+00:00`** يُقاسُ قبلَ الدفعِ · والماضي يبقى مُعلَنًا مقيسًا (135) لا مُبرَأً
  - **وحدُّ الوجهِ الجديدِ مُعلَنٌ**: على مرآةٍ لا ترى العقدةَ المُعلَنةَ يُرفَعُ `BaselineNodeUnreachable` فيُعلَنُ أنَّ الشرطَ **لم يُقَس** ولا يُدَّعى خُضرةً — ويُقاسُ في CI حيثُ `fetch-depth: 0`
قيدُ السجلّ: W-110 ثمَّ W-113 · الحجزُ والعملُ في عقدةٍ واحدةٍ («الدفعُ = العملُ وقيدُه معًا»)
  و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`)
حكمُ الجولةِ الخامسةِ من مجلسِ المراجعةِ — مُقيَّدٌ كما وردَ لا كما يُشتَهى:
  العقدةُ المُراجَعةُ: `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` · التاريخُ: 2026-09-13
  المراجعُ أ (‏GPT 5.6 Sol) والمراجعُ ب (‏Grok 4.6) في حاويتَينِ منفصلتَينِ، كلٌّ أعادَ
  تشغيلَ الدليلِ بنفسِه وقرأَ حكمَ CI بنفسِه من الواجهةِ — والحكمُ: **`REJECTED` بانقسامٍ لا يُجمَعُ جمعًا حسابيًّا**
  (أ `VERIFIED` `P1=0` · ب `REJECTED` `P1=2`).
  والعيوبُ باتّحادِها مُقيَّدةٌ في `DISC-063` ولم تُصلَحْ في هذا البندِ ولا في قيدِ التقييدِ
  (§ 5.2 — تقييدُ حكمٍ لا إصلاحُ عيبٍ). ولم يُنقَلْ بندٌ إلى `VERIFIED`: الإجماعُ شرطُ `Q-43`.

```

---

### WI-034 — فخُّ منطقةِ زمنِ الالتزامِ: يُحرَسُ لا يُعلَنُ وحدَه

```text
النطاق: tooling-gates (‏`tools/governance` — نطاقٌ مُسجَّلٌ · فئةُ التغييرِ `C1`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — حدُّ الصدقِ 8 المُعلَنُ منذُ `W-005` بلا حرسٍ)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW   (‏`RESERVED` ← `IN_PROGRESS` ← `IN_REVIEW` بلا قفزٍ · § 4.3 — والحجزُ كُتِبَ قبلَ مسِّ ملفٍّ)
المسارات:
  tools/governance/stamp_readme_identity.py                        (‏اشتقاقُ التاريخِ يُوحَّدُ على UTC)
  tests/governance/test_w109_commit_timestamp_timezone.py          (‏جديدٌ — حرسٌ يُثبِتُ الفخَّ ثمَّ يقيسُ زوالَه)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `stamp_readme_identity.py` **لا يُعلِنُه بندٌ** `RESERVED`/`IN_PROGRESS`/`IN_REVIEW`: قِيسَ على خلايا المساراتِ كلِّها — لا تداخل
  - وملفُّ الحرسِ جديدٌ · ولا `ci.yml` يُمَسُّ (‏مقفولٌ بـ`WI-023`) · ولا جدولَ ولا migration ولا سرَّ · ولا قرارَ `Q-###` يتوقَّفُ عليه
خارجَ النطاق:
  - **حدُّ الصدقِ 9 لا يُمَسُّ**: صدقُ طابعِ الالتزامِ نفسِه (‏تواريخُ `W-023`…`W-027` الباطلةُ) دَينٌ آخرُ يبقى مُعلَنًا، وتصحيحُه يوجبُ إعادةَ كتابةِ التاريخِ وهي ممنوعةٌ
  - ولا تُمَسُّ أدواتٌ أُخرى تشتقُّ تواريخَ ولو كانَ فيها عينُ النمطِ: هذا بندُ موضعٍ واحدٍ مقيسٍ لا حملةٌ
معيارُ القبول:
  1. اشتقاقُ «اليومِ» لا يتبعُ منطقةَ الجهازِ، واشتقاقُ تاريخِ git لا يتبعُ منطقةَ الالتزامِ — بل UTC في الحالَينِ
  2. الحرسُ **يُثبِتُ أنَّ الفخَّ حقيقيٌّ** أوّلًا (‏التزامٌ بـ+03:00 قربَ منتصفِ الليلِ يُري `--date=short` يومًا والمُوحَّدُ يومًا آخرَ)، فلا تُقاسُ خُضرةٌ بلا فرقٍ
  3. لا يُخفَّفُ فحصٌ ولا يُسكَتُ ماسحٌ · و`--ratchet` لا يرتفعُ · و§ 5.4 كلُّها رمزُها 0
  4. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليلُ المطلوب:
  python -m pytest tests/governance/test_w109_commit_timestamp_timezone.py -q
  python tools/governance/truth_audit.py . --ratchet
بدأ: 2026-09-02        ينتهي الحجز: 2026-09-30
العائق: —
الخطوةُ التالية: مراجعةٌ — والمراجعُ مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43`، ولا يُكتَبُ `VERIFIED` هنا بحالٍ (§ 4.3)
حكمُ CI المقروءُ: عقدةُ `8693658` · تشغيلٌ **67** (`33607123826`) · `completed success` · **13/13** · `READABLE` — قُرِئَ لا استُنتِجَ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الحرسُ يقيسُ أداةً واحدةً**: عودةُ النمطِ في أداةٍ أُخرى لا يُسقِطُه — فالحدُّ 8 صارَ محروسًا **في موضعِه المقيسِ** لا في المستودعِ كلِّه
  - **ولا يُقرأُ إبراءً للحدِّ 9**: صدقُ الطابعِ نفسِه ما زالَ بلا حرسٍ
قيدُ السجلّ: W-109 · الحجزُ والعملُ في عقدةٍ واحدةٍ («الدفعُ = العملُ وقيدُه معًا»)
  و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`)
```

---

### WI-033 — تتمّةُ الخفضِ: المواضعُ الحرّةُ الباقيةُ تحتَ `tests/`

```text
النطاق: tests-root (‏`tests` — نطاقٌ **مُسجَّلٌ** في `OWNERSHIP.md` فئتُه `C0`، فلا نطاقَ يُبتدَعُ هنا)
المسار/المرحلة: T0 (قابليّةُ القياسِ — تتمّةُ `W-106`: ما بقيَ حرًّا من صنفِ «بلا وجهٍ يُمرِّرُ جذرًا صريحًا»)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW   (‏`RESERVED` ← `IN_PROGRESS` ← `IN_REVIEW` بلا قفزٍ · § 4.3)
المسارات (‏كلُّ مسارٍ مُعلَنٌ صراحةً اسمًا — لا بنثرٍ يُقرأُ دعوى واسعةً · `DISC-042`):
  tests/constitutional/test_constitutional_cli.py
  tests/constitutional/test_constitutional_engine.py
  tests/crown/test_crown_truth_matrix.py
  tests/crown/test_w064_secret_scan_exceptions.py
  tests/sovereignty/test_crown_human_root.py
  tests/sovereignty/test_enforcement_boundary.py
  tests/sovereignty/test_enforcement_integration.py
  tests/sovereignty/test_sovereignty_cli.py
  tests/sovereignty/test_sovereignty_kernel.py
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - قِيسَت التسعةُ واحدًا واحدًا على خلايا مساراتِ كلِّ بندٍ `RESERVED`/`IN_PROGRESS`/`IN_REVIEW`: **لا يُدَّعى أيٌّ منها**
  - ولا أداةَ تُمَسُّ · ولا `ci.yml` (‏مقفولٌ بـ`WI-023`) · ولا جدولَ ولا migration ولا سرَّ · ولا قرارَ `Q-###` يتوقَّفُ عليه
خارجَ النطاق:
  - **`tools/crown/` لا يُمَسُّ**: مجلَّدٌ **بلا نطاقٍ مُسجَّلٍ** في `OWNERSHIP.md` (‏`RK-012` · `DISC-008`)، وتسجيلُ نطاقٍ فعلُ مالكٍ لا منفِّذٍ — فموضعاهُ الحرّانِ يبقيانِ مقيسَينِ في الدَّينِ
  - ومواضعُ البنودِ المفتوحةِ لا تُمَسُّ (§ 6.1) · وصنفُ «بوجهٍ يُمرِّرُ جذرًا صريحًا» ليسَ هدفَ هذا البندِ
  - ولا يُغلَقُ `DISC-041` ولا `DISC-032`: خفضٌ لا إبراءٌ
معيارُ القبول:
  1. المواضعُ التسعةُ تصيرُ `discover_repo_root(__file__)` بلا تغييرِ سلوكٍ آخرَ — والجذرُ المُكتشَفُ هو الجذرُ نفسُه (‏الاختباراتُ تمرُّ كما كانت)
  2. الرقمانِ المُعلَنانِ في `ROOT_PROVENANCE_BASELINE:` يُخفَضانِ تبعًا للمقيسِ، وحرسُ `WI-031` يُسقِطُ إن لم يُخفَضا
  3. § 5.4 كلُّها رمزُها 0 · و`--ratchet` لا يرتفعُ · و`ruff` نظيفٌ · والمجموعةُ الكاملةُ أخضرُ بمعناها عدا الإخفاقاتِ المحلّيّةِ المُعلَنةِ
  4. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ (§ 4.3)
الدليلُ المطلوب:
  python -m pytest tests/constitutional tests/crown tests/sovereignty -q
  python -m pytest tests/governance/test_w102_measurement_root_provenance.py -q
  bash tools/dev/bootstrap.sh --verify  &&  python tools/governance/truth_audit.py . --ratchet
بدأ: 2026-09-02        ينتهي الحجز: 2026-09-30
العائق: —
الخطوةُ التالية: مراجعةٌ — والمراجعُ لهذا النطاقِ (`tests-root` · فئةُ `C0` في `OWNERSHIP.md`) مجلسُ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43`، والنقلُ إلى `VERIFIED` فعلُه لا فعلُ الكاتبِ
حكمُ CI المقروءُ: عقدةُ `ceef58e` · تشغيلٌ **65** (`33601053405`) · **success · 13/13 · READABLE** — قُرِئَ بـ`ci_verdict_readability.py --from-json`
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **يبقى بعدَ هذا البندِ موضعانِ حرّانِ من الصنفِ نفسِه** تحتَ `tools/crown/`، وحبسُهما ليسَ تقنيًّا بل **غيابُ نطاقٍ مُسجَّلٍ** — قرارُ مالكٍ
  - وتبقى مواضعُ البنودِ المفتوحةِ وصنفُ «بوجهٍ صريحٍ» مقيسةً في الدَّينِ
قيدُ السجلّ: W-107 · الحجزُ والعملُ في عقدةٍ واحدةٍ («الدفعُ = العملُ وقيدُه معًا»)
  و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`)
```

---

### WI-032 — خفضُ دَينِ `DISC-041`: الجذرُ يُكتشَفُ بعلامةٍ، في المواضعِ الحرّةِ وحدَها

```text
النطاق: tooling-gates (‏النطاقُ المُسجَّلُ في `OWNERSHIP.md` · فئةُ التغييرِ `C0`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — `DISC-041` مقيسٌ ومحروسٌ من النموِّ، وهذا أوّلُ خفضٍ فعليٍّ له)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_PROGRESS   (‏`IN_REVIEW → IN_PROGRESS` · § 4.3 — انتقالٌ مشروعٌ أوجبَه ردُّ المجلسِ في الجولةِ الخامسةِ)
المسارات:
  tools/governance/repo_root.py                                    (‏جديدٌ — مُكتشِفٌ يصعدُ حتّى علامةٍ دالّةٍ ويرفعُ خطأً إن لم يجدْها)
  tests/governance/test_w106_repo_root_discovery.py                (‏جديدٌ — حرسُ المُكتشِفِ نفسِه)
  و34 ملفَّ فحصٍ تُرحَّلُ مواضعُها الحرّةُ (‏كلُّ مسارٍ مُعلَنٌ صراحةً · § 6.2):
  tests/governance/test_completion_ledger_gate.py
  tests/governance/test_constitutional_reconciliation.py
  tests/governance/test_cross_system_suites.py
  tests/governance/test_identity_law.py
  tests/governance/test_measurement_ignores_environments.py
  tests/governance/test_q3_branch_declaration_surface.py
  tests/governance/test_root_dependencies_declared.py
  tests/governance/test_step12_live_truth_guards.py
  tests/governance/test_step13_identity_headers.py
  tests/governance/test_step16_silent_fallback.py
  tests/governance/test_step17_in_memory_stores.py
  tests/governance/test_step18_restart_survival.py
  tests/governance/test_step20_debt_drift_snapshot.py
  tests/governance/test_step7_factory_surfaces.py
  tests/governance/test_truth_matrix_identity.py
  tests/governance/test_w034_runtime_state_identity.py
  tests/governance/test_w036_pricing_divergence.py
  tests/governance/test_w037_measurement_provenance.py
  tests/governance/test_w038_probe_measure_mode.py
  tests/governance/test_w042_root_name_guard.py
  tests/governance/test_w048_bound_provenance.py
  tests/governance/test_w051_ci_verdict_readability.py
  tests/governance/test_w052_history_hash_probe.py
  tests/governance/test_w053_gate_dependency_closure.py
  tests/governance/test_w055_schema_inventory_drift.py
  tests/governance/test_w056_sovereign_decision_status.py
  tests/governance/test_w058_live_stack_precondition.py
  tests/governance/test_w059_open_record_accountability.py
  tests/governance/test_w061_surface_debt_trend.py
  tests/governance/test_w062_mutation_probe.py
  tests/governance/test_w064_services_src_fallback.py
  tests/governance/test_w069_single_scanner_and_explicit_root.py
  tests/governance/test_w069_status_contradiction.py
  tests/governance/test_work_governance_gate.py
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - المسارانِ الجديدانِ لا يُعلِنُهما بندٌ: لا تداخل
  - **والملفّاتُ الأربعةُ والثلاثونَ قِيسَت واحدًا واحدًا**: لا يُدَّعى أيٌّ منها في خليّةِ مساراتِ بندٍ حالتُه `RESERVED` أو `IN_PROGRESS` أو `IN_REVIEW` — والمواضعُ المُدَّعاةُ (37 مسارًا) **تُترَكُ كما هي** ولو كانَ فيها عينُ النمطِ
  - `.github/workflows/ci.yml` **لا يُمَسُّ** (‏مقفولٌ بـ`WI-023`) · ولا أداةَ مُدَّعاةً تُمَسُّ · ولا جدولَ ولا migration ولا سرَّ · ولا قرارَ `Q-###` يتوقَّفُ عليه
خارجَ النطاق:
  - **مواضعُ البنودِ المفتوحةِ لا تُمَسُّ**: خفضُها ينتظرُ انفكاكَ دعواها (§ 6.1)
  - **و`tools/crown/` و`tests/crown/` و`tests/sovereignty/` و`tests/constitutional/` خارجَ النطاقِ**: نطاقاتٌ أُخرى لا يملكُها `tooling-gates`
  - ولا تُعَلَّى سقّاطةٌ ولا يُسكَتُ ماسحٌ · ولا يُغلَقُ `DISC-041` ولا `DISC-032`: خفضٌ لا إبراءٌ
معيارُ القبول:
  1. `repo_root.py` يصعدُ من موضعٍ حتّى ملفٍّ دالٍّ على جذرِ المستودعِ، **ويرفعُ خطأً يُسمّي الموضعَ** إن بلغَ الجذرَ الأعلى بلا علامةٍ — ولا يهبطُ إلى تخمينٍ
  2. حرسُه يُثبِتُ: الاكتشافَ من عُمقٍ مختلفٍ · والرفعَ الصريحَ عندَ الغيابِ · وأنَّ نقلَ ملفٍّ لا يُغيِّرُ الجذرَ المُكتشَفَ (‏وهو عينُ العَطبِ الذي يُعالَج)
  3. المواضعُ الحرّةُ الأربعةُ والثلاثونَ تُرحَّلُ، فينخفضُ الرقمانِ المُعلَنانِ في سطرِ `ROOT_PROVENANCE_BASELINE:` داخلَ `DISC-041` — **والحرسُ يُسقِطُ إن لم يُخفَضِ الرقمُ**، فلا تبقى سقّاطةٌ أرخى من الواقعِ
  4. `bash tools/dev/bootstrap.sh --verify` أخضرُ بمعناهُ (‏وما عدا الإخفاقاتِ المحلّيّةَ المُعلَنةَ التي تخضرُّ في CI) · و`--ratchet` لا يرتفعُ · و`ruff` نظيفٌ · وكلُّ بوّابةِ § 5.4 رمزُها 0
  5. حكمُ CI يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ قبلَ الانتقالِ — ولا يُقرأُ الأخضرُ إغلاقًا (§ 4.3)
الدليلُ المطلوب:
  python -m pytest tests/governance/test_w106_repo_root_discovery.py -q
  python -m pytest tests/governance/test_w102_measurement_root_provenance.py -q -s   # الرقمُ المُخفَّضُ يُطبَعُ
  bash tools/dev/bootstrap.sh --verify  &&  python tools/governance/truth_audit.py . --ratchet
بدأ: 2026-09-02        ينتهي الحجز: 2026-09-30
العائق: — **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، والحكمُ: `REJECTED` بإجماعِ المراجعَينِ** (أ `P1=1` · ب `P1=2`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ تلكَ العيوبِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ.
الخطوةُ التالية: معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`)
حكمُ CI المقروءُ: عقدةُ `9c27533` · تشغيلٌ **64** (`33598194613`) · **success · 13/13 · READABLE** — قُرِئَ بـ`ci_verdict_readability.py --from-json` لا بنظرٍ في الصفحةِ · وأخضرُ مقروءٌ ليسَ إغلاقًا
ما قِيسَ فعلًا:
  - رُحِّلَ **34 موضعًا حرًّا** إلى `discover_repo_root(__file__)`، فانخفضَ المقيسُ:
    `tests` من **53 إلى 19** · ومن صنفِ «بلا وجهٍ» من **37 إلى 12** · و`tools` **25 و2** بلا تغييرٍ
  - وخُفِضَ الرقمُ المُعلَنُ في `ROOT_PROVENANCE_BASELINE:` تبعًا للمقيسِ، فالسقّاطةُ شُدَّت ولم تُرخَ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا خفضٌ جزئيٌّ لا إبراءٌ**: يبقى النمطُ في مواضعِ البنودِ المفتوحةِ وفي نطاقاتٍ أُخرى، و`DISC-041` و`DISC-032` **مفتوحانِ**
  - **ولا يُقرأُ الترحيلُ إصلاحًا لِما لم يُرحَّلْ**: الرقمُ المُعلَنُ بعدَ الخفضِ هو الحقيقةُ المقيسةُ لا الغايةُ
قيدُ السجلّ: W-106 · الحجزُ والعملُ في عقدةٍ واحدةٍ (‏«الدفعُ = العملُ وقيدُه معًا»)
  و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`): ذِكرُ قيدٍ أُضيفَ في مجموعةِ التغييرِ نفسِها يُشعِلُ `POST_MERGE_NOT_CLOSED` على بندٍ حالتُه `RESERVED`
حكمُ الجولةِ الخامسةِ من مجلسِ المراجعةِ — مُقيَّدٌ كما وردَ لا كما يُشتَهى:
  العقدةُ المُراجَعةُ: `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` · التاريخُ: 2026-09-13
  المراجعُ أ (‏GPT 5.6 Sol) والمراجعُ ب (‏Grok 4.6) في حاويتَينِ منفصلتَينِ، كلٌّ أعادَ
  تشغيلَ الدليلِ بنفسِه وقرأَ حكمَ CI بنفسِه من الواجهةِ — والحكمُ: **`REJECTED` بإجماعِ المراجعَينِ**
  (أ `P1=1` · ب `P1=2`).
  والعيوبُ باتّحادِها مُقيَّدةٌ في `DISC-063` ولم تُصلَحْ في هذا البندِ ولا في قيدِ التقييدِ
  (§ 5.2 — تقييدُ حكمٍ لا إصلاحُ عيبٍ). ولم يُنقَلْ بندٌ إلى `VERIFIED`: الإجماعُ شرطُ `Q-43`.

```

---

### WI-031 — نسَبُ محلِّ القياسِ: جذرٌ يُعرَفُ بعلامةٍ أو بعلمٍ، لا بعُمقٍ مكتوبٍ

```text
النطاق: tooling-gates (‏النطاقُ المُسجَّلُ في `OWNERSHIP.md` · فئةُ التغييرِ `C0`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — بوّابةٌ قد تقرأَ شجرةً غيرَ المقصودةِ وتُخرِجَ صفرًا · `DISC-041`)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW   (‏RESERVED `W-102` ← IN_PROGRESS `W-103` ← IN_REVIEW `W-104` بعدَ حكمٍ مقروءٍ · ولا يضعُ الكاتبُ `VERIFIED` · § 4.3)
المسارات:
  tests/governance/test_w102_measurement_root_provenance.py        (‏نزلَ — قارئٌ تركيبيٌّ يُحصي النمطَ ويُعلِنُ رقمَينِ لا يعلوانِ)
  ولا أداةَ تُمَسُّ في هذا البندِ ألبتّةَ: الحرسُ **يقرأُ** ولا يُعدِّلُ
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `tests/governance/test_w102_measurement_root_provenance.py` **ملفٌّ جديدٌ** لا يُعلِنُه بندٌ: لا تداخل
  - **ولهذا لم يُدَّعَ إصلاحُ النمطِ في هذا البندِ**: مواضعُه تسكنُ أدواتٍ **مُدَّعاةً لبنودٍ في يدِ المراجعِ** (`WI-023`…`WI-030` — منها `state_document_drift.py` و`truth_audit.py` و`guard_enforcement_closure.py`)، فمسُّها الآنَ مصادمةُ دعوى (§ 6.1) وتوسيعُ نطاقٍ صامتٌ (§ 5.2)
  - `.github/workflows/ci.yml` **لا يُمَسُّ** (‏مقفولٌ بـ`WI-023`): الفحصُ تحتَ `tests/governance/` فيُنفَّذُ بخطوتَيْ pytest القائمتَينِ (‏السطرُ 117 و579)
  - ولا أداةَ جديدةً في `tools/` · ولا جدولَ ولا migration ولا سرَّ · ولا قرارَ `Q-###` مفتوحًا يتوقَّفُ عليه
خارجَ النطاق:
  - **لا يُصلَحُ النمطُ في هذا البندِ**: السقّاطةُ تمنعُ نموَّه، والخفضُ يجري بندًا بندًا حينَ تنفكُّ الدعاوى — **ولا يُقرأُ الحجزُ إصلاحًا**
  - **ولا تُعَلَّى السقّاطةُ أبدًا**: الرقمانِ يُخفَضانِ ولا يُرفَعانِ؛ ورفعُهما تخفيفُ بوّابةٍ لا إصلاحُ عَطبٍ
  - ولا يُمَسُّ نصُّ § 5.4 ولا § 6 (‏قرارُ مالكٍ) · ولا تُحسَمُ مراجعةُ `WI-023`…`WI-030`
معيارُ القبول:
  1. الحرسُ يُحصي النمطَ تركيبيًّا (‏`ast`) ويُصنِّفُه صنفَينِ: جذرٌ من عُمقٍ ثابتٍ · ومنه ما **لا يقبلُ** جذرًا صريحًا ألبتّةَ
  2. الرقمانِ مُعلَنانِ في الفحصِ نفسِه، ويُسقِطُ الحرسُ إن **نما** أحدُهما — ويُسقِطُ كذلك إن **انخفضَ** بلا خفضِ الرقمِ المُعلَنِ (فلا تبقى سقّاطةٌ أرخى من الواقعِ)
  3. قياسُ القارئِ نفسِه: نصّانِ يُقرآنِ فيُحكَمُ عليهما حكمَينِ مختلفَينِ — ولا يُطمَأنُّ إلى خضرةٍ لم تُختَبَرْ
  4. الإحصاءُ يُقاسُ غيرَ فارغٍ: قارئٌ يُحصي صفرًا يُقرأُ خضرةً وهو أعمى
  5. `pytest tests/governance -q` أخضرُ بمعناهُ · والسقّاطةُ 63 لم ترتفعْ · و`ruff` نظيفٌ · وكلُّ بوّابةٍ محلّيّةٍ رمزُها 0
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ، ولا يُقرأُ الأخضرُ إغلاقًا (§ 4.3)
الدليلُ المطلوب:
  python -m pytest tests/governance/test_w102_measurement_root_provenance.py -q -s   # الرقمانِ يُطبَعانِ
  python -m pytest tests/governance -q  &&  ruff check .
  python tools/governance/truth_audit.py . --check  &&  python tools/governance/truth_audit.py . --ratchet
بدأ: 2026-09-02        ينتهي الحجز: 2026-09-30
العائق: —
الخطوةُ التالية: مراجعةُ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — عُيِّنَ مراجعًا لهذا النطاقِ بقرارِ المالكِ `Q-43` (`A-2` `APPROVED`)، وأُغلِقَ `DISC-027` و`RK-020` بذلك. ولا فعلَ لمنفِّذٍ فيه
حكمُ CI المقروءُ: عقدةُ الحجزِ `9d460b5` ⇒ تشغيلُ 60 ([`33585020251`](https://github.com/xoos-beep/AMOS-Fedration/actions/runs/33585020251)) `success` **13/13** `READABLE` · وعقدةُ النزولِ `061f64c` ⇒ تشغيلُ 61 ([`33586085087`](https://github.com/xoos-beep/AMOS-Fedration/actions/runs/33586085087)) `success` **13/13** `READABLE` — **ولا يُقرأُ الأخضرُ إغلاقًا** (§ 4.3)
تصحيحٌ مقيسٌ لا يُمحى: الرقمُ `tests: 53` في `W-102` قيسَ على شجرةٍ **فيها الحرسُ** قبلَ نزولِه؛ وعلى عقدةِ `W-102` نفسِها كانَ **52**. والرقمُ المُعلَنُ في الحرسِ 53 لأنَّه نزلَ — **والحرسُ يُحصي نفسَه ولا يُعفي**
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا يُوقِفُ النموَّ ولا يُبرِئُ القائمَ**: 25 و53 موضعًا مقيسةٌ تبقى كما هي حتّى تنفكَّ الدعاوى
  - **وتصنيفُ «يقبلُ جذرًا صريحًا» يُقرأُ على مستوى الوحدةِ** لا على موضعِ الإسنادِ — وهو تصنيفٌ **أرخى من الحقيقةِ**، ولهذا يُعلَنُ الرقمُ الأشدُّ (‏بلا وجهٍ ألبتّةَ) رقمًا ثانيًا مستقلًّا
  - **ولا يُقرأُ هذا إغلاقًا لِـ`DISC-041` ولا لِـ`DISC-032`**: الحالةُ تُقرأُ بعدَ حكمٍ مقروءٍ ومراجعةٍ (§ 4.3)
قيدُ السجلّ: W-102 · الحجزُ
  و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ (`DISC-010` · `DISC-030`): ذِكرُ قيدٍ أُضيفَ في مجموعةِ التغييرِ نفسِها يُشعِلُ `POST_MERGE_NOT_CLOSED` على بندٍ حالتُه `RESERVED` — والدليلُ لم يُخفَ إذ القيدُ مُسمًّى هنا
```

---

### WI-030 — «الأثرُ المُولَّدُ مدفوعٌ» يُقاسُ قبلَ الدفعِ لا في CI وحدَها

```text
النطاق: tooling-gates (‏النطاقُ المُسجَّلُ في `OWNERSHIP.md` الذي يحوي `tools/governance` · فئةُ التغييرِ `C0`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — بوّابةٌ لا وجهَ لها محلّيًّا تجعلُ الأخضرَ المحلّيَّ غيرَ دالٍّ · `DISC-040`)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW
المسارات:
  tools/governance/truth_audit.py                                  (‏يُزادُ وجهُ `--check`: يُولِّدُ في الذاكرةِ ويقارِنُ بالمكتوبِ ويُسقِطُ على الفرقِ · **ولا يكتُبُ في الشجرةِ في هذا الوجهِ**)
  tests/governance/test_w099_generated_artifact_freshness.py       (‏جديدٌ — يقيسُ أنَّ الأثرَ المُولَّدَ في الشجرةِ طازجٌ، ويقيسُ أنَّ الوجهَ نفسَه يُسقِطُ فعلًا)
  وسجلّاتُ الحالةِ والحوكمةِ **لا تُدَّعى في مساراتِ هذا البندِ**: تُمَسُّ تحتَ دعوى `WI-023` القائمةِ وبقائدٍ واحدٍ (§ 6.1)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `tools/governance/truth_audit.py` **لا يُدَّعى في مساراتِ أيِّ بندٍ مفتوحٍ**: قُرِئَ جدولُ § 1 كلُّه — البنودُ `WI-023`…`WI-029` تُعلِنُ `guard_enforcement_closure.py` و`enforcement_path_ledger.py` و`measurement_provenance.py` و`state_document_drift.py` و`mutation_probe.py` وفحوصَها، ولا واحدَ منها يُعلِنُ هذا الملفَّ: لا تداخل
  - `tests/governance/test_w099_generated_artifact_freshness.py` **ملفٌّ جديدٌ** لا يُعلِنُه بندٌ: لا تداخل
  - `.github/workflows/ci.yml` **لا يُمَسُّ** وهو مقفولٌ بـ`WI-023`: الفحصُ الجديدُ تحتَ `tests/governance/` فيُنفَّذُ بخطوتَيْ pytest القائمتَينِ (‏السطرُ 117 والسطرُ 579) — فطريقُ الإنفاذِ قائمٌ بلا مسِّ مسارٍ مقفولٍ
  - **ولا أداةَ جديدةً تُزادُ في `tools/`**: الوجهُ يسكنُ الأداةَ التي تُولِّدُ الأثرَ نفسَها — فلا مصدرَ حقيقةٍ مُكرَّرًا، ولا صفَّ جديدًا في `VERDICT_CAPABLE_UNWIRED` (‏10 اليومَ)، ولا نطاقًا ثانيًا يُدَّعى
  - لا جدولَ ولا migration ولا مسارَ API ولا عقدَ ولا سرَّ ولا مورِدَ تشغيلٍ · ولا قرارَ `Q-###` مفتوحًا يتوقَّفُ عليه
خارجَ النطاق:
  - **لا يُمَسُّ نصُّ § 5.4 في [`THE_ROADMAP.md`](THE_ROADMAP.md)**: زيادةُ أمرٍ إلى مجموعةِ ما قبلَ الدفعِ تعديلٌ في وثيقةٍ حاكمةٍ — قرارُ مالكٍ لا فعلُ عاملٍ. ولهذا يسكنُ الإنفاذُ فحصًا تحتَ `tests/`، فمجموعةُ ما قبلَ الدفعِ تُشغِّلُ `pytest tests/ -q` أصلًا: الإنفاذُ يصلُ بلا مسِّ نصٍّ سياديٍّ
  - **ولا تُمَسُّ خطوةُ CI القائمةُ** (`git diff --exit-code` · السطرُ 515): البوّابةُ الأبعدُ تبقى كما هي — يُزادُ وجهٌ أقربُ ولا يُخفَّفُ الأبعدُ
  - **ولا يُعمَّمُ الوجهُ على كلِّ أثرٍ مُولَّدٍ في `docs/audit/` في هذا البندِ**: البقيّةُ مقيسةٌ بـ`measurement_provenance.py --check` أصلًا، وتعميمُ الحرسِ على كلِّ كاتبٍ بندٌ آخرُ إن كشفَه القياسُ
  - **ولا تُحسَمُ قراراتُ المالكِ**: مراجعةُ `WI-023`…`WI-029` · `origin/develop` · سرُّ `T0.6` · `A-3` · استقلالُ المراجعةِ
معيارُ القبول:
  1. **الوجهُ يُقاسُ لا يُدَّعى**: `truth_audit.py . --check` يخرُجُ بـ0 حينَ يطابِقُ المكتوبُ المُولَّدَ، وبرمزٍ غيرِ صفريٍّ حينَ يختلفُ حقلٌ واحدٌ — ويُسمّي الملفَّ والحقلَ
  2. **ولا يكتُبُ في الشجرةِ التي يحكُمُ عليها**: يُقاسُ ببصمةِ الملفَّينِ قبلَ التشغيلِ وبعدَه
  3. **الحرسُ يُسقِطُ فعلًا**: يُقاسُ بشجرةٍ مؤقَّتةٍ أُفسِدَ فيها الأثرُ المُولَّدُ فيُسقِطُ، وبشجرةٍ طازجةٍ فلا يُسقِطُ — ومحلُّ القياسِ مُمرَّرٌ صراحةً (`DISC-032`)
  4. **والشجرةُ الحاضرةُ تُقاسُ**: فحصٌ يُسقِطُ إن كانَ الأثرُ المُولَّدُ في المستودعِ متقادمًا — وهو عينُ ما حمَّرَ التشغيلَ 55
  5. مجموعُ `tests/governance` أخضرُ بمعناهُ · والسقّاطةُ 63 لم ترتفعْ · و`ruff` نظيفٌ · وكلُّ بوّابةٍ محلّيّةٍ رمزُها 0
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ، ولا يُقرأُ الأخضرُ إغلاقًا (§ 4.3)
الدليلُ المطلوب:
  python tools/governance/truth_audit.py . --check
  python -m pytest tests/governance/test_w099_generated_artifact_freshness.py -q
  python -m pytest tests/governance -q  &&  ruff check .
  python tools/governance/truth_audit.py . --ratchet                  # المتوقَّع: ثابتٌ عندَ 63
بدأ: 2026-09-01        ينتهي الحجز: 2026-09-30
العائق: انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — عُيِّنَ مراجعًا لهذا النطاقِ بـ`Q-43`. **والحجزُ جُدِّدَ في `W-152`** بنصِّ § 6.3 (‏الحجزُ ينتهي إن لم يُحدَّثْ): المالكُ نفسُه ولا استلامَ، والسببُ مُعلَنٌ لا مطويٌّ — انقضى 2026-09-08 والبندُ ما زالَ `IN_REVIEW` بلا مراجعٍ مُشغَّلٍ، فحمَّرَ `RESERVATION_EXPIRED` سبعةَ بنودٍ وأسقطَ «Cross-System Suites» في CI.
الخطوةُ التالية: مراجعةٌ ثمَّ `VERIFIED` — بيدِ المراجعِ لا بيدِ الكاتبِ (§ 4.3)
ما نزلَ فعلًا (‏مقيسٌ لا مُدَّعًى):
  - `truth_audit.py` ‏⊕ `--check`: توليدٌ في الذاكرةِ ومقارنةٌ بالمكتوبِ وإسقاطٌ يُسمّي الملفَّ والحقلَ · ولا كتابةَ في هذا الوجهِ
  - `tests/governance/test_w099_generated_artifact_freshness.py`: ستَّةُ فحوصٍ ⇒ **6 مرَّت**
  - عَطبٌ أحدثَه القياسُ في نفسِه: `SILENT_FALLBACK` (‏استثناءٌ مُبتلَعٌ) رفعَ 63 ← 64 — **فأُصلِحَ في مصدرِه** (‏يُسمّى ويُرفَعُ نصُّه) لا بتعليةِ السقّاطةِ · و`--ratchet` ⇒ ثابتٌ عندَ **63**
  - إحصاءُ مواضعِ القياسِ بعدَ إرساءِ الجديدِ: **27 موضعًا · 20 قصدًا · 7 مُرساةٌ · 0 غيرُ مُرساةٍ**
  - وعَطبٌ ثانٍ كشفَه نموُّ السجلِّ: فحصُ `test_w057_state_document_drift.py::test_real_repository_is_measurable` كانَ يقيسُ رأسَ السجلِّ بسقفٍ مُضمَرٍ عندَ `W-099` — فصارَ يقيسُ **شكلَ المعرِّفِ** لا عدَدَه. والمسارُ مُدَّعًى لـ`WI-027` فمُسَّ **تحتَ دعواهُ وبقائدٍ واحدٍ** (§ 6.1) ولا يُدَّعى في مساراتِ هذا البندِ
حكمُ CI المقروءُ: عقدةُ الدفعِ `48082c5` ⇒ تشغيلُ [`33581117015`](https://github.com/xoos-beep/AMOS-Fedration/actions/runs/33581117015) (‏رقمُ 58) `completed success` · **13/13** · `READABLE` — والفحصُ الجديدُ نُفِّذَ في CI بخطوتَيْ pytest القائمتَينِ · وقبلَها عقدةُ الحجزِ `03974135` (‏قيدُ `W-099`) ⇒ تشغيلُ [`33575634587`](https://github.com/xoos-beep/AMOS-Fedration/actions/runs/33575634587) (‏رقمُ 57) `completed success` · **13/13** · `READABLE` — وعقدةُ الدفعِ هذه (`W-100`) تُقرأُ في القيدِ التالي
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا يُطزِّجُ أثرًا واحدًا لا كلَّ أثرٍ**: `docs/audit/TRUTH_MATRIX.md` و`truth_matrix.json` وحدَهما — وكلُّ كاتبٍ آخرَ في `docs/audit/` يبقى محكومًا بحارسِه هو
  - **ولا يُقرأُ هذا إغلاقًا لِـ`DISC-040`**: الحالةُ تُقرأُ بعدَ حكمٍ مقروءٍ ومراجعةٍ (§ 4.3)
قيدُ السجلّ: W-099 · الحجزُ · و`W-100` · الوجهُ والحرسُ · و`W-101` · الحكمُ والمراجعةُ
  و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—`** بالسابقةِ المقيسةِ نفسِها (`DISC-010` · `DISC-030`): البوّابةُ تقرأُ تلك الخليّةَ وحدَها، وذِكرُ قيدٍ أُضيفَ في مجموعةِ التغييرِ نفسِها يُشعِلُ `POST_MERGE_NOT_CLOSED` على بندٍ حالتُه `RESERVED`. والدليلُ لم يُخفَ: القيدُ مُسمًّى هنا
```

---

## 4 · كيفَ يُقرأُ هذا السجلُّ قبلَ أيِّ عمل

1. هل مسارُك مذكورٌ في عمودِ `المسارات` لبندٍ نشِط؟ → **لا تبدأْ**؛ راجعْ مالكَه (§ 6.1 من الخارطة).
2. هل عملُك مُقيَّدٌ منجَزًا في `COMPLETION_LEDGER.md § 8`؟ → **لا يُعاد** (§ 6.5).
3. هل نطاقُك مُسجَّلٌ في [`OWNERSHIP.md`](OWNERSHIP.md)؟ → إن لا، فأوّلُ عملِك تسجيلُه.
4. هل تخدمُ الخطوةَ التاليةَ غيرَ المحجوبةِ في `COMPLETION_LEDGER.md § 7`؟ → إن لا، فبندُك `PROPOSED` حتى يُعتمَد.

### WI-022 — إعادةُ تقييمِ `DISC-034` بقياسٍ صحيحٍ: خمسةُ التزاماتٍ لا واحدٌ، وتصادمُ معرِّفاتٍ في السجلِّ

```text
النطاق: docs-general
المسار/المرحلة: T0 / T0.4ب (صدقُ السجلِّ في موضعِه — لا حالةَ دولةٍ تُبنى على قياسٍ خاطئٍ)
المالك: Driving H            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED
المسارات:
  PROJECT_STATE.md                                               (واجبُ § 7 (4) · وسطرُ عددِ الصفوفِ وصفُّ الخلاصةِ)
  docs/PROJECT_HANDBOOK.md                                       (واجبُ § 7 (4) · تاريخُ آخرِ تعديلٍ)
  وسجلّاتُ الحوكمةِ والتدقيقِ (`ACTIVE_WORK.md` · `DISCOVERIES.md` · `RISK_REGISTER.md` · `COMPLETION_LEDGER.md` · مصفوفةُ الحقيقةِ المولَّدةُ)
  **تُمَسُّ ولا تُدَّعى مِلكًا**: هي **مُعفاةٌ من الحجزِ** بنصِّ § 6. وكانَ هذا النصُّ مكتوبًا في **خليّةِ المساراتِ** في § 1 فنُقِلَ إلى هنا
  بـ`W-118` (`DISC-042`): الخليّةُ تُقرأُ مساراتٍ لا نثرًا — والنقلُ **لا يُغيِّرُ تغطيةً** (‏قِيسَ: صفرُ ملفٍّ تبدَّلَت تغطيتُه)
  وسجلّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ: ACTIVE_WORK.md · DISCOVERIES.md · RISK_REGISTER.md · COMPLETION_LEDGER.md · TRUTH_MATRIX.md المولَّدة
خارجَ النطاق:
  - **لا يُدمَجُ `origin/develop` ولا يُحذَفُ ولا يُعلَنُ إسقاطُه ولا يُرقَّمُ سجلُّه من جديدٍ**: قرارُ مستودعٍ للمالكِ (§ 2 حكم 12) — يُقاسُ ويُقيَّدُ ويُتركُ
  - لا يُلمَسُ كودُ أداةٍ ولا فحصٌ: هذا بندُ سجلٍّ محضٌ، وتوسيعُ النطاقِ الصامتُ ممنوعٌ (§ 5.2)
  - لا يُمحى نصُّ `DISC-034` الأوّلُ: يُصحَّحُ بسطرِ إقرارٍ يُعلِنُ ما قِيسَ خطأً — والتاريخُ لا يُعادُ كتابتُه
  - لا يُحسَبُ صفُّ سجلٍّ في الفرعِ إنجازًا في `main`: ما لم يبلُغِ الفرعَ الحاكمَ لا يُدَّعى محسوبًا
معيارُ القبول:
  1. عددُ التزاماتِ `origin/develop` التي ليست في `main` مقيسٌ بأمرٍ يُعادُ تشغيلُه، ومكتوبٌ رقمًا لا وصفًا
  2. دعوى `DISC-034` الأولى («التزامٌ واحدٌ» · «الرأسُ `37156e6`») مُصحَّحةٌ بسطرِ إقرارٍ يُعلِنُ الخطأَ ولا يمحوه
  3. تصادمُ معرِّفاتِ السجلِّ بينَ الفرعَينِ مقيسٌ بندًا بندًا ومُقيَّدٌ اكتشافًا جديدًا (`DISC-036`)
  4. حكمُ CI على عقدةِ إغلاقِ `WI-021` مقروءٌ ومُقيَّدٌ رقمًا (واجبُ § 7 (6))
  5. القرارُ المطلوبُ من المالكِ مكتوبٌ خياراتٍ محدودةً صريحةً، ولا يُتَّخَذُ في التنفيذِ
  6. البوّاباتُ كلُّها ترجعُ رمزَ صفرٍ، ولا حرسٌ خُفِّفَ ولا مصفوفةٌ تُرَاخى
الدليلُ المطلوب:
  git rev-list --count HEAD..origin/develop                       # 5
  git log --oneline HEAD..origin/develop                          # خمسةُ عناوينَ بأسمائِها
  git merge-base HEAD origin/develop                              # e5efe9c
  git rev-list --count origin/develop..HEAD                       # 28
  git show origin/develop:docs/audit/COMPLETION_LEDGER.md | grep -E '^\| W-06[012] \|'   # عناوينُ تخالفُ عناوينَ `main`
  python tools/governance/check_work_governance.py --self-check · --staged · --enforce-post-merge
  python tools/governance/open_record_accountability.py · state_document_drift.py · truth_audit.py . --ratchet
  وحكمُ CI على عقدةِ الدفعِ يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ في خليّةِ «قيدُ السجلّ»
بدأ: 2026-08-31        ينتهي الحجز: 2026-09-07
العائق: —
الخطوةُ التالية: مُنجَزٌ · ولا خطوةَ باقيةً في هذا البندِ — وما بقيَ قرارُ فرعٍ بيدِ المالكِ (`DISC-034` · `DISC-036`)
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا بندٌ يُصحِّحُ قياسًا لا يبني قدرةً**: لا حرسَ جديدَ ولا سطحَ صارَ `PROVEN`، ومخالفاتُ مصفوفةِ الحقيقةِ تبقى عندَ 63
  - **والقياسُ الأوّلُ في `DISC-034` كانَ خاطئًا خطأً واحدًا محدَّدًا**: قِيسَ الرأسُ `37156e6` فبُنِيَ عليه «التزامٌ واحدٌ»، والرأسُ الحقيقيُّ `e0be191` والالتزاماتُ **خمسةٌ**. والخطأُ من جنسِ ما يُحاسِبُ عليه المشروعُ نفسُه: دعوى قِيسَت مرّةً ولم تُعَدْ عندَ الاستعمالِ
  - **ولا يُقالُ إنَّ الفرعَ أُنقِذَ**: الشِقُّ الهندسيُّ المُستنقَذُ في `W-069` كانَ من التزامٍ واحدٍ من الخمسةِ، وأربعةٌ باقيةٌ لم يُقَسْ محتواها بندًا بندًا في هذا البندِ — وذاك مُعلَنٌ حدًّا لا مطويٌّ
  - **وتصادمُ المعرِّفاتِ عَطبٌ في السجلِّ لا في الفرعِ**: `W-060` و`W-061` و`W-062` تُسمّي في `main` عملًا وفي `develop` عملًا آخرَ، فلا يُدمَجُ الفرعُ بلا ترقيمٍ من جديدٍ — وهو ما يجعلُ القرارَ قرارَ مالكٍ لا خطوةَ تنفيذٍ
  - **و`VERIFIED` — متى وُضِعَت — ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2` (`DISC-027` · `RK-020`)
  - **وحكمُ CI على عقدةِ الدفعِ مُشاهَدٌ لا مُدَّعًى**: تشغيلُ 33348727892 على `fb70f47` ⇒ `completed success` · **13/13** · `READABLE` بقياسِ الخطواتِ
  - **مُراجَعٌ 2026-08-31 بمراجعٍ غيرِ مستقلٍّ** (`A-2` § 16.5 · `RK-020`): أُعيدَ تشغيلُ الأوامرِ السِتّةِ المُعلَنةِ في «الدليلِ المطلوبِ» عندَ الرأسِ `afae5e0` فطُوبِقَت أرقامُها بمعيارِ القبولِ بندًا بندًا — **خمسةٌ** التزاماتٍ و**ثمانيةٌ وعشرونَ** وأساسُ افتراقٍ `e5efe9c` وثلاثةُ معرِّفاتٍ مُتصادمةٍ وأقصى صفٍّ في سجلِّ الفرعِ `W-054`، والبوّاباتُ رمزَ صفرٍ. **ولا شهادةَ عينٍ ثانيةٍ**: الاستقلالُ مُنتفٍ ومُسجَّلٌ (`DISC-027`)
  - **وحكمُ CI على عقدةِ التسليمِ للمراجعةِ مقروءٌ كذلك**: تشغيلُ 33350334816 على `afae5e0` ⇒ `completed success` · **13/13** · `READABLE`
  - **مُغلَقٌ 2026-08-31 بـ`W-075`**: قُرِئَ حكمُ CI على عقدةِ المراجعةِ `2a5c1f6` كذلك — تشغيلُ 33351966117 ⇒ `completed success` · **13/13** · `READABLE` — فالبندُ سلكَ طريقَ § 4.3 كاملًا بأربعِ دفعاتٍ وثلاثةِ أحكامٍ مقروءةٍ متَّصلةٍ
قيدُ السجلّ: W-072 · دفعٌ مباشرٌ إلى main (`fb70f47`) · حكمُ CI على عقدةِ القيدِ **قُرِئَ أخضرَ 13/13** (تشغيلُ 33348727892 · `completed success` · و`ci_verdict_readability.py --from-json` ⇒ `READABLE · 13/13`) · مُسلَّمٌ للمراجعةِ 2026-08-31 · مُراجَعٌ 2026-08-31 (`A-2` · غيرُ مستقلٍّ) بعدَ خُضرةٍ مقروءةٍ ثانيةٍ 13/13 على `afae5e0` (تشغيلُ 33350334816 · `READABLE`) · **مُغلَقٌ 2026-08-31 بـ`W-075`** بعدَ خُضرةٍ مقروءةٍ ثالثةٍ 13/13 على `2a5c1f6` (تشغيلُ 33351966117 · `READABLE`)
```

### WI-023 — دعوى «يُشغَّلُ في كلِّ دفعةٍ» تصيرُ مقيسةً في بوّابةٍ، لا سندًا يُكتَبُ فيُصدَّقُ

```text
النطاق: tooling-gates
المسار/المرحلة: T0 / T0.4ب (قابليّةُ القياسِ — سندُ بقاءِ القيدِ يُقاسُ لا يُقرأُ)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_PROGRESS   (‏`IN_REVIEW → IN_PROGRESS` · § 4.3 — انتقالٌ مشروعٌ أوجبَه ردُّ المجلسِ في الجولةِ الخامسةِ)
المسارات:
  tools/governance/guard_enforcement_closure.py                  (الحرسُ الجديدُ · مكتبةُ قياسٍ وحدَها)
  tests/governance/test_w077_guard_enforcement_closure.py        (الحرسُ مُراقَبٌ بفحوصِه · ومنها فحصانِ على الشجرةِ الحاضرةِ)
  .github/workflows/ci.yml                                       (ربطُ الحرسِ وثلاثِ أدواتٍ بخطواتِ تشغيلٍ)
  PROJECT_STATE.md                                               (واجبُ § 7 (4))
  docs/PROJECT_HANDBOOK.md                                       (واجبُ § 7 (4) · وقائمةُ الأوامرِ المُلزِمةِ)
  وسجلّاتُ الحوكمةِ والتدقيقِ (`ACTIVE_WORK.md` · `DISCOVERIES.md` · `COMPLETION_LEDGER.md` · `docs/audit/TRUTH_MATRIX.md` و`docs/audit/truth_matrix.json` المولَّدتانِ بالأداةِ)
  **تُمَسُّ ولا تُدَّعى مِلكًا**: مُعفاةٌ من الحجزِ بنصِّ § 6. وكانَ هذا النصُّ في **خليّةِ المساراتِ** في § 1 فنُقِلَ إلى هنا بـ`W-118` (`DISC-042`)
  — نقلٌ لا حذفٌ، **ولا تغيُّرَ في التغطيةِ** (‏الجزءُ النثريُّ لم يكنْ يُغطّي ملفًّا أصلًا: قِيسَ صفرًا)
  وسجلّاتٌ مُعفاةٌ من الحجزِ تُمَسُّ ولا تُدَّعى مِلكًا — مُعلَنٌ لا مطويّ: ACTIVE_WORK.md · DISCOVERIES.md · COMPLETION_LEDGER.md · docs/audit/TRUTH_MATRIX.md وdocs/audit/truth_matrix.json (‏مولَّدتانِ بالأداةِ لا تُكتَبانِ بيدٍ)
خارجَ النطاق:
  - **لا يُقرَّرُ `A-3` ولا يُبدَّلُ وضعُ الإبلاغِ إلى إسقاطٍ**: قرارُ المالكِ (§ 16) — والبوّاباتُ الجديدةُ **مُسقِطةٌ بنفسِها** ولا تمسُّ وضعَ بوّابةِ حوكمةِ العملِ
  - **لا يُدمَجُ `origin/develop` ولا يُحذَفُ ولا يُرقَّمُ سجلُّه**: قرارُ مستودعٍ للمالكِ (`DISC-034` · `DISC-036`)
  - لا يُمحى نصُّ `DISC-032` الأوّلُ: يُقرُّ بسطرٍ يُعلِنُ أنَّ دعواهُ كانت غيرَ منفَذةٍ حتّى `W-077` — والتاريخُ لا يُعادُ كتابتُه
  - **لا تُوسَّعُ الأداةُ لتحكُمَ على صدقِ ما يقيسُه الحرسُ**: تقيسُ **وجودَ طريقِ إنفاذٍ** وحدَه، وذاك حدُّها المُعلَنُ
  - لا تُربَطُ الأدواتُ الثلاثةَ عشرَ الباقيةُ غيرُ المربوطةِ: الجردُ يُعلَنُ ملاحظةً، وربطُ ما لا دعوى مكتوبةً له بندٌ تالٍ لا توسيعٌ صامتٌ (§ 5.2)
معيارُ القبول:
  1. كلُّ دعوى «يُشغَّلُ في كلِّ دفعةٍ» في `DISCOVERIES.md` و`RISK_REGISTER.md` تُقابَلُ بطريقِ إنفاذٍ مُسمّى (`CI_STEP` أو `CI_PYTEST` أو `REAL_TREE_TEST`) — وإلّا سقطَ الحرسُ برمزِ 1
  2. الحرسُ يُسقِطُ عندَ سببِه **ويسكتُ عندَ غيابِه**: لكلِّ مخالفةٍ ولكلِّ قاعدةٍ مكتوبةٍ فحصٌ في الشجرةِ المؤقَّتةِ، وفحصانِ يحكُمانِ على الشجرةِ الحاضرةِ
  3. `mutation_probe.py` مربوطٌ بخطوةِ تشغيلٍ في CI فتصيرُ دعوى `DISC-032` **صادقةً بالإنفاذِ**، وكلفتُه مكتوبةٌ رقمًا مقيسًا
  4. الحرسُ نفسُه مربوطٌ في CI ومربوطٌ في قائمةِ الأوامرِ المُلزِمةِ في الدليلِ — فلا حرسٌ يُولَدُ غيرَ مربوطٍ ويُحاسِبُ غيرَه
  5. `gate_dependency_closure.py` يبقى عندَ **12 مُغلَقةً · 1 مفتوحةً** (المفتوحةُ `DISC-009` بيدِ المالكِ): الأدواتُ الثلاثُ مكتبيّةُ قياسٍ فلا تُنشِئُ تبعيّةً غيرَ مُثبَّتةٍ
  6. البوّاباتُ كلُّها ترجعُ رمزَ صفرٍ، ومخالفاتُ مصفوفةِ الحقيقةِ تبقى عندَ 63 ولا حرسٌ خُفِّفَ
الدليلُ المطلوب:
  python tools/governance/guard_enforcement_closure.py            # المتوقَّع: 4 دعاوى · 4 منفَذةٌ · 0 غيرُ منفَذةٍ · رمزُ 0
  python -m pytest tests/governance/test_w077_guard_enforcement_closure.py -q   # المتوقَّع: 19 نجحَت (‏كانَ 17 قبلَ فحصَي الرفضِ المُصنَّفِ)
  python tools/governance/mutation_probe.py                       # المتوقَّع: 31 وثبةً · 31 مُلتقَطةً · رمزُ 0 (‏4م 31ث)
  python tools/governance/gate_dependency_closure.py              # المتوقَّع: 13 وظيفةً · 12 مُغلَقةً · 1 مفتوحةً (`DISC-009`)
  python tools/governance/state_document_drift.py · open_record_accountability.py · check_work_governance.py --self-check
  python tools/governance/truth_audit.py . --ratchet              # المتوقَّع: ثابتٌ عندَ 63
  ruff check . && python -m pytest tests/governance/ -q
  وحكمُ CI على كلِّ عقدةٍ يُقرأُ برقمِ تشغيلٍ ويُقيَّدُ في خليّةِ «قيدُ السجلّ»
بدأ: 2026-08-31        ينتهي الحجز: 2026-09-30
العائق: انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) (`Q-43`). **وتاريخُ الحجزِ ههنا كانَ 2026-09-07 وصفُّ § 1 يقولُ 2026-09-14** — انحرافُ صفٍّ/كتلةٍ أسقطَه المراجعُ ب في الجولةِ الثالثةِ، فزُومِلَ إلى **2026-09-14** في `W-154`: الجدولُ هو ما تقرؤه البوّابةُ، والكتلةُ كانت متخلِّفةً عنه لا مُجدَّدةً بغيرِ سببٍ. **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، والحكمُ: `REJECTED` بإجماعِ المراجعَينِ** (أ `P1=4` · ب `P1=3` و`P2=2`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ تلكَ العيوبِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ.
الخطوةُ التالية: معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`)
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الأداةُ تقيسُ وجودَ طريقِ إنفاذٍ لا صدقَ ما يقيسُه الحرسُ**: فحصٌ يذكرُ `REPO_ROOT` ولا يُؤكِّدُ شيئًا ذا معنًى يمرُّ من هنا — وصدقُ الحكمِ واجبُ من يكتبُ الفحصَ، وحرسُه مراجعةٌ بشريّةٌ ومِسبارُ الوَثبِ
  - **والقاعدتانِ مكتوبتانِ فيهما حدٌّ**: «فحصُ الشجرةِ الحاضرةِ» يُعرَفُ بغيابِ `tmp_path` وذِكرِ `REPO_ROOT` في ملفٍّ يربطُ نفسَه بالأداةِ استيرادًا أو ثابتَ مسارٍ؛ فمن قاسَ الشجرةَ الحاضرةَ باسمٍ آخرَ **لا تراهُ الأداةُ** — نقصٌ يُعلَنُ ولا يُدَّعى تمامًا
  - **والدعوى تُقرأُ في جُملتِها** لا في الخليّةِ كلِّها (حدُّ الجُملةِ فواصلُ مكتوبةٌ): وحملُ ملفّاتِ الخليّةِ كلِّها على عبارةٍ واحدةٍ ادِّعاءٌ عن الكاتبِ لا قياسٌ لِما كتبَ
  - **وثلاثةَ عشرَ أداةً حاكمةً تبقى غيرَ مربوطةٍ بخطوةِ تشغيلٍ**: تُعلَنُ ملاحظةً `UNWIRED_TOOL_INVENTORY` ولا تُسقِطُ — فما لا دعوى مكتوبةً له لا يُحاسَبُ عليه صاحبُه في هذا البندِ، وهذا **نقصٌ مُعلَنٌ** لا اكتمالٌ
  - **ومِسبارُ الوَثبِ يُطيلُ وظيفةَ الهُويّةِ بأربعِ دقائقَ ونصفٍ**: كلفةٌ مُعلَنةٌ مقيسةً لا مطويّةٌ، وهي ثمنُ أن تصيرَ دعوى `DISC-032` مقيسةً
  - **و`VERIFIED` — متى وُضِعَت — ليست شهادةَ عينٍ ثانيةٍ**: المراجعُ هو المالكُ جامعًا الدورَينِ بنصِّ `A-2` (`DISC-027` · `RK-020`)
قيدُ السجلّ: W-078 · حكمُ عقدةِ `4764a12` قُرِئَ **13/13 · READABLE** (تشغيلُ 33391458311) والبندُ سُلِّمَ للمراجعةِ
حكمُ الجولةِ الخامسةِ من مجلسِ المراجعةِ — مُقيَّدٌ كما وردَ لا كما يُشتَهى:
  العقدةُ المُراجَعةُ: `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` · التاريخُ: 2026-09-13
  المراجعُ أ (‏GPT 5.6 Sol) والمراجعُ ب (‏Grok 4.6) في حاويتَينِ منفصلتَينِ، كلٌّ أعادَ
  تشغيلَ الدليلِ بنفسِه وقرأَ حكمَ CI بنفسِه من الواجهةِ — والحكمُ: **`REJECTED` بإجماعِ المراجعَينِ**
  (أ `P1=4` · ب `P1=3` و`P2=2`).
  والعيوبُ باتّحادِها مُقيَّدةٌ في `DISC-063` ولم تُصلَحْ في هذا البندِ ولا في قيدِ التقييدِ
  (§ 5.2 — تقييدُ حكمٍ لا إصلاحُ عيبٍ). ولم يُنقَلْ بندٌ إلى `VERIFIED`: الإجماعُ شرطُ `Q-43`.

```

### WI-024 — «أداةٌ حاكمةٌ لا تُشغِّلُها دفعةٌ» تصيرُ مخالفةً مُسمّاةً أو سببًا مُصنَّفًا، لا صمتًا في جردٍ

```text
النطاق: tooling-gates
المسار/المرحلة: T0 / T0.4ب (قابليّةُ القياسِ — ما لا يُشغَّلُ لا يُقاسُ، وما لا سببَ لِتركِه لا يُقبَل)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_PROGRESS   (‏`IN_REVIEW → IN_PROGRESS` · § 4.3 — انتقالٌ مشروعٌ أوجبَه ردُّ المجلسِ في الجولةِ الخامسةِ)
المسارات:
  tools/governance/enforcement_path_ledger.py                    (الأداةُ الجديدةُ · مكتبةُ قياسٍ وحدَها · لا تكتبُ بايتًا)
  tests/governance/test_w079_enforcement_path_ledger.py          (فحوصٌ في شجرةٍ مؤقَّتةٍ · وفحوصٌ تحكُمُ على الشجرةِ الحاضرةِ)
  والأحدَ عشرَ ملفًّا الذي يُقاسُ أنَّه قابلٌ للتشغيلِ ولا يُشغِّلُه شيءٌ — يُضافُ في ترويسةِ كلٍّ منها سطرُ «طريقُ الإنفاذ» وحدَه، ولا يُمَسُّ منطقُه:
  tools/audit/final_audit.py · tools/audit/judicial_gate_probe.py · tools/audit/treasury_gate_probe.py
  tools/governance/ci_verdict_readability.py · tools/governance/constitutional_reconciliation.py · tools/governance/evidence_registry.py
  tools/governance/gate_dependency_closure.py · tools/governance/schema_inventory_drift.py · tools/governance/sovereign_decision_status.py
  tools/migrations/r4_unify_agent_identity.py · tools/stubs/registry_check.py
  وسجلّاتُ الحالةِ والحوكمةِ (`ACTIVE_WORK.md` · `DISCOVERIES.md` · `COMPLETION_LEDGER.md` · `PROJECT_STATE.md` · `docs/PROJECT_HANDBOOK.md` · مصفوفةُ الحقيقةِ المولَّدةُ) **لا تُدَّعى في مساراتِ هذا البندِ**: هي مُعلَنةٌ في مساراتِ `WI-023` وتُمَسُّ بحكمِ واجبِ § 7 — فالتسميةُ مرّتَينِ تقاطعٌ مقيسٌ لا حِرصٌ (`CLAIM_CONFLICT` § 6.1)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `.github/workflows/ci.yml` **مقفولٌ** بـ`WI-023` وهو `IN_REVIEW` (§ 6.1) — فلا خطوةَ تشغيلٍ جديدةٌ تُضافُ في هذا البندِ، والإنفاذُ يمرُّ من استدعاءِ `pytest` القائمِ في CI (‏`CI_PYTEST`) لا من بوّابةٍ جديدةٍ
  - `tools/governance/guard_enforcement_closure.py` **مقفولٌ** بـ`WI-023` — فنقصُ جردِه (`UNWIRED_TOOL_INVENTORY`) يُقاسُ ويُقيَّدُ اكتشافًا هنا، **ولا يُصلَحُ في مسارِه** قبلَ إغلاقِ `WI-023`
  - لا بندَ مفتوحًا آخرَ يلامسُ `tools/governance/enforcement_path_ledger.py` ولا `tests/governance/test_w079_*` ولا ترويساتِ الأدواتِ: **لا تداخل**
  - لا جدولَ قاعدةِ بياناتٍ ولا migration ولا مسارَ API ولا عقدَ ولا schema ولا سرَّ ولا مورِدَ تشغيلٍ · ولا قرارَ `Q-###` مفتوحًا يتوقَّفُ عليه هذا البندُ
خارجَ النطاق:
  - **لا تُضافُ خطوةُ تشغيلٍ في `ci.yml`**: المسارُ مقفولٌ (§ 6.1) — وربطُ الأدواتِ التي يُثبِتُ القياسُ أنَّها تصلحُ بوّابةً مُسقِطةً بندٌ تالٍ يُحجَزُ بعدَ إغلاقِ `WI-023`، لا توسيعٌ صامتٌ الآنَ (§ 5.2)
  - **لا يُقرَّرُ أنَّ أداةً يجبُ أن تُشغَّلَ في كلِّ دفعةٍ**: الأداةُ تُلزِمُ **إعلانَ** طريقِ إنفاذٍ أو سببٍ مُصنَّفٍ، ولا تُنشئُ واجبَ تشغيلٍ لم يكتبْه أحدٌ
  - **لا يُمَسُّ منطقُ أيِّ أداةٍ**: يُضافُ سطرُ ترويسةٍ واحدٌ لا أكثرَ — فإصلاحُ سلوكِ أداةٍ (‏`final_audit.py` يرفعُ استثناءً حينَ يُعطى وسيطًا ليسَ مسارًا) اكتشافٌ يُقيَّدُ لا عملٌ يُدَسُّ
  - **لا تُحسَمُ قراراتُ المالكِ**: `A-3` · `origin/develop` · سرُّ `T0.6` · استقلالُ المراجعةِ · أسئلةُ `T2` — ولا يُغلَقُ `WI-023` ولا يُنقَلُ إلى `VERIFIED`
معيارُ القبول:
  1. كلُّ ملفٍّ في `tools/**` يُصنَّفُ بقياسٍ من مصدرِه: **يُشغَّلُ بحرسِ `__main__`** أو **يعملُ عندَ الاستيرادِ** أو **مكتبةٌ لا مدخلَ لها** — فلا يُحمَلُ ملفٌّ لا يُشغَّلُ على أنَّه أداةٌ مهجورةٌ
  2. كلُّ أداةٍ **قابلةٍ للتشغيلِ وغيرِ مربوطةٍ** يلزمُها سطرُ ترويسةٍ `طريقُ الإنفاذ: <رمزٌ مُصنَّفٌ> · <نصٌّ>` من مفرداتٍ **مغلقةٍ** — وغيابُه مخالفةُ `ENFORCEMENT_PATH_UNDECLARED`، ورمزٌ خارجَ المفرداتِ `ENFORCEMENT_PATH_UNKNOWN_REASON`
  3. **الإعلانُ يُكذَّبُ بالواقعِ لا يُصدَّقُ بنفسِه**: ادِّعاءُ خطوةِ تشغيلٍ لا تُسمّي المسارَ `ENFORCEMENT_PATH_FALSE`، وادِّعاءُ سببٍ لِتركِ الربطِ لأداةٍ **صارت مربوطةً** `ENFORCEMENT_PATH_STALE`
  4. الأداةُ تُعلِنُ ملاحظةً بعددِ الأدواتِ **القادرةِ على الحكمِ** (‏تخرجُ برمزٍ غيرِ صفرٍ في شِفرتِها) وهي غيرُ مربوطةٍ — رقمٌ يُقرأُ لا انطباعٌ
  5. الأداةُ تسكتُ عندَ غيابِ سببِها وتسقُطُ عندَ حضورِه: لكلِّ مخالفةٍ ولكلِّ قاعدةٍ فحصٌ في شجرةٍ مؤقَّتةٍ، وفحوصٌ تحكُمُ على الشجرةِ الحاضرةِ وتربطُ نفسَها بالأداةِ (‏فيصيرُ إنفاذُها `CI_PYTEST` بالاستدعاءِ القائمِ)
  6. الرفضُ مُصنَّفٌ لا صامتٌ: غيابُ `tools/` أو `.github/workflows/` أو عَطبٌ نحويٌّ في مصدرٍ ⇒ رمزُ الخروجِ 2 لا حكمٌ مبنيٌّ على قراءةٍ فاشلةٍ
  7. البوّاباتُ كلُّها ترجعُ رمزَ صفرٍ · ومخالفاتُ مصفوفةِ الحقيقةِ تبقى عندَ 63 ولا حرسٌ يُخفَّفُ · وحكمُ CI يُقرأُ برقمِ تشغيلٍ لكلِّ عقدةِ دفعٍ
الدليلُ المطلوب:
  python tools/governance/enforcement_path_ledger.py               # المتوقَّع: تصنيفُ كلِّ أداةٍ · مخالفاتٌ صفرٌ بعدَ الإعلانِ · رمزُ 0
  python -m pytest tests/governance/test_w079_enforcement_path_ledger.py -q
  python tools/governance/guard_enforcement_closure.py             # المتوقَّع: 4 دعاوى · 4 منفَذةٌ · 0 غيرُ منفَذةٍ
  python tools/governance/state_document_drift.py · open_record_accountability.py · check_work_governance.py --self-check
  python tools/governance/truth_audit.py . --ratchet               # المتوقَّع: ثابتٌ عندَ 63
  ruff check . && python -m pytest tests/governance/ -q
بدأ: 2026-08-31        ينتهي الحجز: 2026-09-30
العائق: انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — عُيِّنَ مراجعًا لهذا النطاقِ بـ`Q-43`. **والحجزُ جُدِّدَ في `W-152`** بنصِّ § 6.3 (‏الحجزُ ينتهي إن لم يُحدَّثْ): المالكُ نفسُه ولا استلامَ، والسببُ مُعلَنٌ لا مطويٌّ — انقضى 2026-09-08 والبندُ ما زالَ `IN_REVIEW` بلا مراجعٍ مُشغَّلٍ، فحمَّرَ `RESERVATION_EXPIRED` سبعةَ بنودٍ وأسقطَ «Cross-System Suites» في CI. **وقد شُغِّلَت الجولةُ الخامسةُ من مجلسِ المراجعةِ المستقلِّ (`Q-43`) على عقدةِ `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` يومَ 2026-09-13، والحكمُ: `REJECTED` بإجماعِ المراجعَينِ** (أ `P1=3` · ب `P1=4`) — والعيوبُ مُقيَّدةٌ باتّحادِها في `DISC-063` **ولم تُصلَحْ ههنا** (§ 5.2)، فالعائقُ الآنَ: معالجةُ تلكَ العيوبِ ثمَّ إعادةُ التسليمِ لجولةٍ سادسةٍ.
الخطوةُ التالية: معالجةُ عيوبِ الجولةِ الخامسةِ المُقيَّدةِ في `DISC-063` بيدِ مالكِ البندِ، ثمَّ إعادةُ التسليمِ `IN_PROGRESS → IN_REVIEW` لجولةٍ سادسةٍ — و`VERIFIED` فعلُ المجلسِ لا فعلُ المؤلِّفِ (§ 4.3 · `Q-43`)
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **الأداةُ تُلزِمُ الإعلانَ لا التشغيلَ**: هي تمنعُ **صمتَ** «أداةٌ حاكمةٌ لا تُشغِّلُها دفعةٌ» ولا تمنعُ تركَها بسببٍ مُعلَنٍ — فمن أرادَ ربطًا فبندُ ربطٍ وبوّابةٌ، لا سطرُ ترويسةٍ
  - **قياسُ «قادرةٍ على الحكمِ» ساكنٌ**: يُقرأُ من الشِفرةِ (`sys.exit` برمزٍ غيرِ صفرٍ أو `SystemExit`) لا من تشغيلٍ — فأداةٌ تحكُمُ بطريقٍ آخرَ لا يراها هذا القياسُ: نقصٌ يُعلَنُ
  - **الترويسةُ تُقرأُ في نافذةٍ مُعلَنةٍ** من أوّلِ الملفِّ — وإعلانٌ مكتوبٌ خارجَها لا يُقرأُ، وذاك حدٌّ مكتوبٌ لا عَطبٌ
  - **والعددُ المقيسُ هنا 11 لا 13**: جردُ `W-077` عَدَّ مكتبةً بلا مدخلٍ أداةً (`mutation_claims.py`)، وعَدَّ ثلاثًا يُشغِّلُها فحصٌ يحكُمُ على الشجرةِ الحاضرةِ أدواتٍ غيرَ مربوطةٍ (`live_truth.py` · `sovereign_write_inventory.py` · `surface_debt_trend.py`)، وقصَرَ نظرَه على مجلَّدَينِ من خمسةٍ فغابَ عنه `tools/migrations` و`tools/stubs` — فالتصحيحُ مقيسٌ لا مُقدَّرٌ
  - **ولا يُصلَحُ جردُ `guard_enforcement_closure.py`** في هذا البندِ: مسارُه مقفولٌ (§ 6.1)، ونقصُه مقيسٌ ومُقيَّدٌ اكتشافًا — والتصحيحُ في بندٍ تالٍ بعدَ إغلاقِ `WI-023`
قيدُ السجلّ: W-082 · حكمُ عقدةِ `W-081` قُرِئَ أخضرَ 13/13 · READABLE فسُلِّمَ البندُ للمراجعةِ · وقبلَه W-081 · قُيِّدَ سببُ الحمرةِ (‏`DISC-039`) · وقبلَه W-080 · السجلُّ قائمٌ ويُسقِطُ: 43 ملفًّا مقيسًا · 11 إعلانًا مُصنَّفًا · 22 فحصًا خضراءَ (‏وقبلَه W-079 · الحجزُ وقياسُ خطِّ الأساسِ)
حكمُ الجولةِ الخامسةِ من مجلسِ المراجعةِ — مُقيَّدٌ كما وردَ لا كما يُشتَهى:
  العقدةُ المُراجَعةُ: `b951dcac6cd103d396e8daa4e5b9e4cefb3f9c5a` · التاريخُ: 2026-09-13
  المراجعُ أ (‏GPT 5.6 Sol) والمراجعُ ب (‏Grok 4.6) في حاويتَينِ منفصلتَينِ، كلٌّ أعادَ
  تشغيلَ الدليلِ بنفسِه وقرأَ حكمَ CI بنفسِه من الواجهةِ — والحكمُ: **`REJECTED` بإجماعِ المراجعَينِ**
  (أ `P1=3` · ب `P1=4`).
  والعيوبُ باتّحادِها مُقيَّدةٌ في `DISC-063` ولم تُصلَحْ في هذا البندِ ولا في قيدِ التقييدِ
  (§ 5.2 — تقييدُ حكمٍ لا إصلاحُ عيبٍ). ولم يُنقَلْ بندٌ إلى `VERIFIED`: الإجماعُ شرطُ `Q-43`.

```

### WI-025 — القياسُ المنشورُ يُفتَّحُ بما يُقاسُ لا برقمِ سطرٍ، فلا يتقادمُ من تعديلِ ترويسةٍ ولا يُخفي انتقالَ موقعٍ

```text
النطاق: audit-truth
المسار/المرحلة: T0 / T0.4ب (‏صدقُ القياسِ — بوّابةُ طزاجةٍ تُعاقِبُ ما لا يُقاسُ تُعلِّمُ العاملَ أن يتجنَّبَ الصوابَ)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW
المسارات:
  tools/audit/sovereign_write_inventory.py                       (حِملُ `--json` وحدَه · ولا يُمَسُّ منطقُ الجردِ ولا العدُّ ولا التصنيفُ)
  tests/governance/test_w083_measurement_site_key.py             (فحوصٌ في شجرةٍ مؤقَّتةٍ · تُثبِتُ الطزاجةَ والإنفاذَ معًا)
  docs/audit/measurements/write_inventory_p13.json               (يُعادُ توليدُه بأمرِه المُقيَّدِ لا بيدٍ)
  docs/audit/measurements/README.md                              (‏يُعلَنُ فيه مفتاحُ الموقعِ وحدُّه)
  وسجلّاتُ الحالةِ والحوكمةِ **لا تُدَّعى في مساراتِ هذا البندِ**: هي مُعلَنةٌ في مساراتِ `WI-023` وتُمَسُّ بحكمِ واجبِ § 7 (‏`CLAIM_CONFLICT` § 6.1)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `WI-023` (`IN_REVIEW`) يقفلُ `.github/workflows/ci.yml` و`tools/governance/guard_enforcement_closure.py` — **ولا يلمسُهما هذا البندُ**
  - `WI-024` (`IN_REVIEW`) يقفلُ `tools/governance/enforcement_path_ledger.py` وترويساتِ أحدَ عشرَ ملفًّا ومنها `tools/audit/final_audit.py` — و`final_audit.py` **قارئٌ** لجردِ الكتاباتِ، فقُيسَ من مصدرِه أنَّه لا يقرأُ حقلَ السطرِ، فلا يُمَسُّ ولا يحتاجُ مسًّا: **لا تداخل**
  - `tools/governance/measurement_provenance.py` **غيرُ محجوزٍ** ولا يُمَسُّ عمدًا: المقارنةُ لا تُخفَّفُ ولا يُضافُ لها استثناءٌ — الإصلاحُ في **مصدرِ** القياسِ لا في **حاكمِه** (وإلّا صارَ الحلُّ إسكاتَ بوّابةٍ)
  - قارئا الجردِ الآخرانِ `tools/governance/surface_debt_trend.py` و`tools/audit/decision_gate.py` قِيسَ أنَّهما يقرآنِ `summary` لا `sites`: **لا تداخل**
  - لا جدولَ ولا migration ولا مسارَ API ولا عقدَ ولا سرَّ ولا مورِدَ تشغيلٍ · ولا قرارَ `Q-###` مفتوحًا يتوقَّفُ عليه هذا البندُ · وفئةُ التغييرِ `C0` (‏حِملُ مُخرَجِ تدقيقٍ · بلا تغيُّرِ سلوكٍ مقيسٍ) لا `C3` ولا `C4`
خارجَ النطاق:
  - **لا يُخفَّفُ حاكمُ الطزاجةِ**: لا استثناءَ حقلٍ في `measurement_provenance.py` ولا تسامحَ في المقارنةِ ولا حذفَ قيدٍ من العقدِ
  - **لا يُمَسُّ العدُّ ولا التصنيفُ**: 217 موقعًا تبقى 217، والمجاميعُ في `summary` كما هي — ومن أرادَ تغييرَ ما يُعَدُّ فبندٌ آخرُ وقيدٌ آخرُ
  - **لا يُصلَحُ جردُ `guard_enforcement_closure.py`** (`DISC-038`) ولا تُضافُ خطوةُ تشغيلٍ في `ci.yml`: مساراتٌ مقفولةٌ بـ`WI-023` (§ 6.1)
  - **لا تُحسَمُ قراراتُ المالكِ**: مراجعةُ `WI-023` و`WI-024` · `origin/develop` · سرُّ `T0.6` · `A-3` · استقلالُ المراجعةِ · أسئلةُ `T2`
معيارُ القبول:
  1. مفتاحُ الموقعِ في حِملِ `--json` صارَ (‏مسارٌ · مالكٌ · دالّةٌ · رتبةٌ داخلَ الثلاثةِ) — **ورقمُ السطرِ يُرفَعُ من الحِملِ** ويبقى في بنيةِ الأداةِ لقارئٍ بشريٍّ ولِفحوصٍ قائمةٍ تقرأُه
  2. الحِملُ مرتَّبٌ ترتيبًا قاطعًا لا يتبعُ ترتيبَ الأسطرِ — فنقلُ دالّةٍ في ملفِّها لا يُحرِّكُ حرفًا في القياسِ المنشورِ
  3. **الإنفاذُ لم يُخفَّفْ بقياسٍ لا بدعوى**: إضافةُ موقعِ كتابةٍ · حذفُه · إعادةُ تسميتِه · تغيُّرُ ما يكتبُه · عبورُه الحدَّ أو تركُه — كلٌّ منها يُحرِّكُ الحِملَ فتسقُطُ بوّابةُ الطزاجةِ
  4. إدخالُ سطرِ ترويسةٍ أو تعليقٍ في ملفٍّ إنتاجيٍّ **لا يُحرِّكُ** الحِملَ — وهو عينُ ما أسقطَ CI في `W-080`
  5. موقعانِ يتشاركانِ المسارَ والمالكَ والدالّةَ يبقيانِ متمايزَينِ بالرتبةِ — فلا يُدمَجانِ ولا يُسقَطُ أحدُهما بحجّةِ تكرارٍ
  6. قارئو الجردِ الثلاثةُ يبقونَ عاملينَ بلا مسٍّ: `final_audit.py` · `surface_debt_trend.py` · `decision_gate.py`
  7. `measurement_provenance.py . --check` **كاملًا** رمزُ 0 · والبوّاباتُ كلُّها رمزُ 0 · والسقّاطةُ ثابتةٌ عندَ 63 · وحكمُ CI يُقرأُ برقمِ تشغيلٍ لكلِّ عقدةِ دفعٍ
الدليلُ المطلوب:
  python -m pytest tests/governance/test_w083_measurement_site_key.py -q
  python tools/audit/sovereign_write_inventory.py --json docs/audit/measurements/write_inventory_p13.json
  python tools/governance/measurement_provenance.py . --check      # المتوقَّع: عقدٌ مستقيمٌ · رمزُ 0
  python tools/audit/final_audit.py · surface_debt_trend.py · decision_gate.py --gate W1
  python tools/governance/truth_audit.py . --ratchet               # المتوقَّع: ثابتٌ عندَ 63
  ruff check . && python -m pytest tests/governance/ -q
بدأ: 2026-08-31        ينتهي الحجز: 2026-09-30
العائق: انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — عُيِّنَ مراجعًا لهذا النطاقِ بـ`Q-43`. **والحجزُ جُدِّدَ في `W-152`** بنصِّ § 6.3 (‏الحجزُ ينتهي إن لم يُحدَّثْ): المالكُ نفسُه ولا استلامَ، والسببُ مُعلَنٌ لا مطويٌّ — انقضى 2026-09-08 والبندُ ما زالَ `IN_REVIEW` بلا مراجعٍ مُشغَّلٍ، فحمَّرَ `RESERVATION_EXPIRED` سبعةَ بنودٍ وأسقطَ «Cross-System Suites» في CI.
الخطوةُ التالية: مراجعةُ البندِ ثمَّ `VERIFIED` ثمَّ `CLOSED` — فعلُ المراجعِ لا فعلُ صاحبِ التغييرِ (§ 4.3)، والمراجعُ المُعلَنُ هو مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43` — و`DISC-027` و`RK-020` أُغلِقا به
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا يرفعُ إنذارًا كاذبًا ولا يزيدُ ما يُقاسُ**: القياسُ يبقى ساكنًا من الشِفرةِ، وما لا يراه الجردُ اليومَ لا يراه بعدَ هذا البندِ
  - **الرتبةُ مفتاحٌ نسبيٌّ**: لو أُضيفَ موقعٌ ثانٍ بالاسمِ نفسِه في الدالّةِ نفسِها تنزاحُ رُتَبُ ما بعدَه — وذاك **تغيُّرٌ حقيقيٌّ في الجردِ** يُقصَدُ ظهورُه، لا تقادمًا كاذبًا
  - **حقلُ السطرِ لا يُحذَفُ من الأداةِ**: فحوصٌ قائمةٌ تقرأُه من البنيةِ (`test_measurement_ignores_environments.py` · `test_step7_factory_surfaces.py`)، وحذفُه كسرٌ لا إصلاحٌ
قيدُ السجلّ: W-085 · حكمُ عقدةِ `W-084` قُرِئَ أخضرَ 13/13 · READABLE فسُلِّمَ البندُ للمراجعةِ · وقبلَه W-084 · المفتاحُ نُقِلَ وأُعيدَ توليدُ القياسِ · 11 فحصًا خضراءَ (‏وقبلَه W-083 · الحجزُ وفحصُ التداخلِ)
```

### WI-026 — حالةُ التشغيلِ لا تُكتَبُ في شجرةِ المستودعِ: موضعُ قاعدةِ البياناتِ يُعلَنُ في البيئةِ لمدى التشغيلِ، والعقدُ الافتراضيُّ لا يُنقَل

```text
النطاق: tooling-gates
المسار/المرحلة: T0 (قابليّةُ القياسِ — حمرةٌ محليّةٌ لا تدُلُّ على عَطبٍ في المستودعِ تُعلِّمُ تطبيعَ الحمرةِ · `RK-005`)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW
المسارات:
  conftest.py                                                     (‏إعلانُ موضعٍ في البيئةِ إن لم تُعلِنْه · بنمطِ `AMOS_CONSUMED_PERMITS_PATH` القائمِ)
  tests/governance/test_runtime_state_stays_outside_the_tree.py    (‏تُضافُ أوجهُ حرسٍ · ولا يُمَسُّ ما فيه من أوجهِ سجلِّ الأذونِ)
  federal/executive/services/tests/conftest.py                    (‏**مسارٌ ثالثٌ أُضيفَ في `W-087` وأُعلِنَ قبلَ مسِّه**: رابطُ قاعدةِ الاختبارِ نسبيٌّ فيُكتَبُ حيثُ يُشغَّلُ pytest · والتنظيفُ القائمُ يفتِّشُ مجلَّدَ الخدماتِ فلا يراهُ)
  وسجلّاتُ الحالةِ والحوكمةِ **لا تُدَّعى في مساراتِ هذا البندِ**: مُعلَنةٌ في مساراتِ `WI-023` وتُمَسُّ بحكمِ واجبِ § 7 (‏`CLAIM_CONFLICT` § 6.1)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `WI-023` (`IN_REVIEW`) يقفلُ `.github/workflows/ci.yml` و`tools/governance/guard_enforcement_closure.py` — **ولا يلمسُهما هذا البندُ**
  - `WI-024` (`IN_REVIEW`) يقفلُ `tools/governance/enforcement_path_ledger.py` وترويساتِ أحدَ عشرَ ملفًّا — **ولا يلمسُها هذا البندُ**
  - `WI-025` (`IN_REVIEW`) يقفلُ أداةَ جردِ الكتاباتِ وقياسَها المنشورَ و`README` القياساتِ — **ولا يلمسُها هذا البندُ**
  - `conftest.py` كانَ مُعلَنًا في مساراتِ `WI-019` وهي `CLOSED` منذُ 2026-08-30، و`test_runtime_state_stays_outside_the_tree.py` **غيرُ مُدَّعًى في أيِّ بندٍ غيرِ مُغلَقٍ**: لا تداخل
  - `federal/executive/services/src/amos_federation/common/database.py` **لا يُمَسُّ**: الموضعُ الافتراضيُّ عقدٌ إنتاجيٌّ، ونقلُه تغييرُ عقدٍ لا إصلاحُ أثرٍ
  - `tools/governance/check_root_file_names.py` **لا يُمَسُّ ولا يُخفَّفُ**: البوّابةُ صادقةٌ، والعَطبُ فيما يكتُبُ في الجذرِ لا فيما يقرأُ
  - لا جدولَ ولا migration ولا مسارَ API ولا عقدَ ولا سرَّ ولا مورِدَ تشغيلٍ · ولا قرارَ `Q-###` مفتوحًا يتوقَّفُ عليه · وفئةُ التغييرِ `C0` (‏إعلانُ بيئةٍ لمدى التشغيلِ وفحوصٌ · بلا تغيُّرِ سلوكٍ إنتاجيٍّ)
خارجَ النطاق:
  - **لا يُخفَّفُ حرسٌ**: لا استثناءَ في `check_root_file_names.py` ولا إعلانَ أثرٍ في قائمةِ الجذرِ ولا قصرَ لوضعِ القرصِ على المُفهرَسِ — وهي الطريقانِ الآخرانِ في `DISC-029` ولم يُختارا
  - **لا يُنقَلُ الموضعُ الافتراضيُّ الإنتاجيُّ**: `os.getcwd()/amos_federation.db` يبقى كما هو، ووجهُ حرسٍ عكسيٌّ يُسقِطُ لو نُقِلَ صامتًا
  - **لا تُحسَمُ قراراتُ المالكِ**: مراجعةُ `WI-023` و`WI-024` و`WI-025` · `origin/develop` · سرُّ `T0.6` · `A-3` · استقلالُ المراجعةِ · أسئلةُ `T2`
معيارُ القبول:
  1. كلُّ تشغيلِ اختباراتٍ يُعلِنُ `AMOS_DATABASE_URL` بموضعٍ **خارجَ** شجرةِ المستودعِ إن لم تُعلِنْه البيئةُ سلفًا — والإعلانُ الصريحُ لا يُنقَض
  2. اسمُ مُتغيّرِ البيئةِ المكتوبُ في `conftest.py` مطابقٌ للحرفِ الذي يقرؤه `database.py` — يُقاسُ نصًّا فلا يفترقُ صامتًا
  3. `amos_federation.db` لا يُنشأُ في جذرِ المستودعِ بعدَ تشغيلِ الاختباراتِ · و`check_root_file_names.py --source disk` يخرُجُ بصفرٍ على شجرةٍ نظيفةٍ
  4. **الحدُّ العكسيُّ محروسٌ**: بلا إعلانٍ في البيئةِ يبقى الموضعُ الافتراضيُّ مُشتَقًّا من `cwd` — فنقلُه يُسقِطُ الحرسَ ولا يمرُّ صامتًا
  5. لا فحصَ يُخفَّفُ ولا يُتخطّى: مجموعُ `tests/governance` وفحوصُ الخدماتِ التي تقرأُ المُتغيّرَ تبقى خضراءَ بمعناها
  6. البوّاباتُ كلُّها رمزُ 0 · والسقّاطةُ ثابتةٌ عندَ 63 · وحكمُ CI يُقرأُ برقمِ تشغيلٍ لعقدةِ كلِّ دفعةٍ
  7. **وأثرُ حزمةِ الخدماتِ كذلك** (‏`W-087`): `amos_federation_test.db` صارَ مُعلَنًا بمسارٍ مُطلَقٍ خارجَ الشجرةِ، فلا يعتمدُ موضعُه على مجلَّدِ التشغيلِ، والتنظيفُ القائمُ يفتِّشُ المجلَّدَ الذي كُتِبَ فيه فعلًا لا مجلَّدًا آخرَ
الدليلُ المطلوب:
  python tools/governance/check_root_file_names.py . --source disk   # المتوقَّع: رمزُ 0 بعدَ تشغيلِ الاختباراتِ
  python -m pytest tests/governance/test_runtime_state_stays_outside_the_tree.py -q
  python -m pytest tests/governance -q  &&  ruff check .
  python tools/governance/truth_audit.py . --ratchet                 # المتوقَّع: ثابتٌ عندَ 63
بدأ: 2026-09-01        ينتهي الحجز: 2026-09-30
العائق: انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — عُيِّنَ مراجعًا لهذا النطاقِ بـ`Q-43`. **والحجزُ جُدِّدَ في `W-152`** بنصِّ § 6.3 (‏الحجزُ ينتهي إن لم يُحدَّثْ): المالكُ نفسُه ولا استلامَ، والسببُ مُعلَنٌ لا مطويٌّ — انقضى 2026-09-08 والبندُ ما زالَ `IN_REVIEW` بلا مراجعٍ مُشغَّلٍ، فحمَّرَ `RESERVATION_EXPIRED` سبعةَ بنودٍ وأسقطَ «Cross-System Suites» في CI.
الخطوةُ التالية: مراجعةُ البندِ ثمَّ `VERIFIED` ثمَّ `CLOSED` — فعلُ المراجعِ لا فعلُ صاحبِ التغييرِ (§ 4.3)، والمراجعُ المُعلَنُ هو مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43` — و`DISC-027` و`RK-020` أُغلِقا به
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا يعزلُ أثرَ التشغيلِ ولا يُصلِحُ عقدًا إنتاجيًّا**: خدمةٌ تُشغَّلُ في الإنتاجِ بلا `AMOS_DATABASE_URL` ما زالت تكتبُ في مجلَّدِ عملِها — وذاك قرارُ عقدٍ يُقيَّدُ لا يُطوى هنا
  - **الإعلانُ لمدى التشغيلِ لا يُغيِّرُ ما يُقاسُ**: أيُّ فحصٍ يُعلِنُ موضعَه صريحًا يبقى على موضعِه، فلا يُخطَفُ منه شيءٌ
  - **وضعُ القرصِ يُحمِّرُ على أثرَينِ آخرَينِ قِيسا في `W-087` ولا يُطويانِ**: `.coverage` أثرُ تشغيلِ تغطيةٍ سابقٍ مُستبعَدٌ بـ`.gitignore` — يُمسَحُ ولا يُعلَنُ استثناءً · و`amos_federation_test_idempotency.json` يُكتَبُ في مجلَّدِ الخدماتِ لا في الجذرِ فلا تراهُ بوّابةُ أسماءِ الجذرِ، **ولم يُعالَجْ هنا** ويبقى مُقيَّدًا في `DISC-029`
  - **قسرُ رابطِ الاختبارِ في حزمةِ الخدماتِ لا يُرفَعُ**: الملفُّ يُثبِّتُ لهجةَ SQLite للحزمةِ كلِّها بقرارٍ معماريٍّ (`E2.2-G`) — وما تغيَّرَ **موضعُ** الملفِّ لا سلطةُ الإعلانِ
قيدُ السجلّ: W-088 · حكمُ عقدةِ `W-087` قُرِئَ أخضرَ 13/13 · READABLE فسُلِّمَ البندُ للمراجعةِ (‏وقبلَه W-087 · الأثرُ عُزِلَ في مصدرَيهِ · وW-086 · الحجزُ)
```

### WI-027 — انحرافُ وثائقِ الحالةِ يُقاسُ بالحقلِ الذي تُعلِنُه الوثيقةُ حالةً، بمِرساةٍ مُسمّاةٍ لا بأقصى ذكرٍ في نصٍّ حرٍّ

```text
النطاق: audit-truth
المسار/المرحلة: T0 (قابليّةُ القياسِ — بوّابةٌ خضراءُ على وثيقةٍ متأخِّرةٍ ثمانيةَ قيودٍ · `DISC-031`)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW
المسارات:
  tools/governance/state_document_drift.py                      (‏تُضافُ قراءةُ الحقلِ المُعلَنِ بمِرساةٍ مكتوبةٍ في الشِفرةِ · ولا تُمَسُّ الأنواعُ القائمةُ من المخالفاتِ)
  tests/governance/test_w057_state_document_drift.py             (‏تُضافُ أوجهُ حرسٍ · ولا يُحذَفُ وجهٌ قائمٌ)
  وسجلّاتُ الحالةِ والحوكمةِ **لا تُدَّعى في مساراتِ هذا البندِ**: مُعلَنةٌ في مساراتِ `WI-023` وتُمَسُّ بحكمِ واجبِ § 7 (‏`CLAIM_CONFLICT` § 6.1)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - `WI-023` (`IN_REVIEW`) يقفلُ `.github/workflows/ci.yml` و`tools/governance/guard_enforcement_closure.py` — **ولا يلمسُهما هذا البندُ**
  - `WI-024` (`IN_REVIEW`) يقفلُ `tools/governance/enforcement_path_ledger.py` وترويساتِ أحدَ عشرَ ملفًّا — **ولا يلمسُها هذا البندُ**
  - `WI-025` (`IN_REVIEW`) يقفلُ أداةَ جردِ الكتاباتِ وقياسَها المنشورَ — **ولا يلمسُها هذا البندُ**
  - `WI-026` (`IN_REVIEW`) يقفلُ `conftest.py` وحرسَ حالةِ التشغيلِ وconftest حزمةِ الخدماتِ — **ولا يلمسُها هذا البندُ**
  - `tools/governance/state_document_drift.py` وفحصُه كانا مُعلَنَينِ في مساراتِ `WI-012` وهي `CLOSED` منذُ 2026-08-27: لا تداخل
  - لا جدولَ ولا migration ولا مسارَ API ولا عقدَ ولا سرَّ ولا مورِدَ تشغيلٍ · ولا قرارَ `Q-###` مفتوحًا يتوقَّفُ عليه · وفئةُ التغييرِ `C0` (‏قراءةٌ تُضافُ إلى أداةِ حوكمةٍ وفحوصٌ · بلا سلوكٍ إنتاجيٍّ)
خارجَ النطاق:
  - **لا يُخفَّفُ الحرسُ القائمُ**: `STATE_DOC_BEHIND` و`STATE_DOC_CITES_UNKNOWN_WORK` و`STATE_DOC_UNDECLARED_DATE` و`STATE_DOC_DATE_IN_FUTURE` تبقى كما هي — ما يُضافُ **يشُدُّ** ولا يُرخي
  - **ولا تكتُبُ الأداةُ في وثيقةٍ تحكمُ عليها**: سابقةُ `W-037`/`W-038` قائمةٌ — بوّابةٌ تُصلِحُ ما تحكمُ عليه لا تُثبِتُ شيئًا
  - **ولا تُوسَّعُ قائمةُ وثائقِ الحالةِ**: `STATE_DOCUMENTS` تبقى مُعلَنةً بحدِّها المكتوبِ، وتوسيعُها بندٌ آخرُ لا يُطوى هنا
  - **ولا يُقاسُ صدقُ الوصفِ**: الحدُّ المُعلَنُ في ترويسةِ الأداةِ باقٍ — وثيقةٌ تذكرُ القيدَ وتكذِبُ في وصفِه تمرُّ، وحرسُها مراجعةٌ بشريّةٌ
  - **ولا تُحسَمُ قراراتُ المالكِ**: مراجعةُ `WI-023` · `WI-024` · `WI-025` · `WI-026` · `origin/develop` · سرُّ `T0.6` · `A-3` · استقلالُ المراجعةِ · أسئلةُ `T2`
معيارُ القبول:
  1. لكلِّ وثيقةِ حالةٍ **مِرساةٌ مُسمّاةٌ مكتوبةٌ في الشِفرةِ** تُعلِنُ **أينَ** تُعلِنُ الوثيقةُ حالتَها، فيُقرَأُ القيدُ من موضعِه لا من أقصى ذكرٍ في الملفِّ
  2. غيابُ المِرساةِ **يُعلَنُ مخالفةً مُصنَّفةً** لا يُبتلَعُ فيُقرَأَ نظافةً — حقلٌ يُعادُ تسميتُه يُسقِطُ الحرسَ ولا يُسكِتُه
  3. تأخُّرُ **الحقلِ المُعلَنِ** عن رأسِ § 8 يُسقِطُ برمزِ 1 ويُطبَعُ بعددِ القيودِ — حالةُ `DISC-031` بعينِها (‏حقلٌ عندَ `W-057` وسجلٌّ عندَ `W-064` وترويسةٌ تذكرُ الأحدثَ) تُسقِطُ
  4. الأوجهُ القائمةُ كلُّها تبقى خضراءَ بمعناها لا بتعديلِ توقُّعِها
  5. `state_document_drift.py` على هذا المستودعِ ⇒ رمزُ 0 (‏الوثيقتانِ مُحدَّثتانِ فعلًا) · والسقّاطةُ ثابتةٌ عندَ 63 · و`ruff` نظيفٌ
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ لعقدةِ الدفعةِ، ولا يُقرأُ الأخضرُ إغلاقًا (§ 4.3)
الدليلُ المطلوب:
  python tools/governance/state_document_drift.py                     # المتوقَّع: رمزُ 0
  python -m pytest tests/governance/test_w057_state_document_drift.py -q
  python -m pytest tests/governance -q  &&  ruff check .
  python tools/governance/truth_audit.py . --ratchet                  # المتوقَّع: ثابتٌ عندَ 63
بدأ: 2026-09-01        ينتهي الحجز: 2026-09-30
العائق: انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — عُيِّنَ مراجعًا لهذا النطاقِ بـ`Q-43`. **والحجزُ جُدِّدَ في `W-152`** بنصِّ § 6.3 (‏الحجزُ ينتهي إن لم يُحدَّثْ): المالكُ نفسُه ولا استلامَ، والسببُ مُعلَنٌ لا مطويٌّ — انقضى 2026-09-08 والبندُ ما زالَ `IN_REVIEW` بلا مراجعٍ مُشغَّلٍ، فحمَّرَ `RESERVATION_EXPIRED` سبعةَ بنودٍ وأسقطَ «Cross-System Suites» في CI.
الخطوةُ التالية: مراجعةُ البندِ ثمَّ `VERIFIED` ثمَّ `CLOSED` — فعلُ المراجعِ لا فعلُ صاحبِ التغييرِ (§ 4.3)، والمراجعُ المُعلَنُ هو مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) بنصِّ `Q-43` — و`DISC-027` و`RK-020` أُغلِقا به
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا يقيسُ موضعَ الدعوى لا صدقَها**: حقلٌ يقولُ `W-089` ويكذِبُ في وصفِه يمرُّ — وذاك حدُّ الأداةِ المُعلَنُ منذُ `W-057` ولا يُدَّعى رفعُه
  - **والمِرساةُ مُعلَنةٌ في الشِفرةِ لا مُكتشَفةٌ**: وثيقةٌ تُعلِنُ حالتَها بحقلٍ لم يُسمَّ هنا لا يراها هذا الحرسُ — وهو الحدُّ نفسُه القائمُ في `STATE_DOCUMENTS`
  - **ولا يُقرأُ هذا إغلاقًا لِـ`DISC-031`**: القيدُ يُقرأُ حالتَه بعدَ حكمٍ مقروءٍ ومراجعةٍ، وأثرُ العَطبِ على `PROJECT_STATE.md` صُحِّحَ في `W-065` والعَطبُ في القياسِ هو ما يُعالَجُ هنا
قيدُ السجلّ: W-091 · حكمُ عقدةِ `W-090` قُرِئَ أخضرَ 13/13 · READABLE فسُلِّمَ البندُ للمراجعةِ (‏وقبلَه W-090 · المِرساةُ مكتوبةٌ وأربعةُ أنواعٍ تُسقِطُ · 53 وجهًا في فحصِ الأداةِ · وW-089 · الحجزُ)
```


### WI-028 — دعوى المِسبارِ تُقرأُ بإعلانٍ صريحٍ لا بجذرِ كلمةٍ في نصٍّ حرٍّ

```text
النطاق: tooling-gates (‏`tools/governance` · النطاقُ المُسجَّلُ في `OWNERSHIP.md` الذي يحوي المسارَينِ)
المسار/المرحلة: T0 (قابليّةُ القياسِ — حرسٌ سالبٌ يُحمِّرُ على قيدٍ صادقٍ فيدفعُ إلى كذبٍ أو تخفيفٍ · `DISC-033`)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW
المسارات:
  tools/governance/mutation_claims.py                            (‏تُعلَنُ فيه عبارةٌ محجوزةٌ للدعوى وسجلٌّ مُجمَّدٌ للصفوفِ التاريخيّةِ · ولا تُمَسُّ دعوى مُسجَّلةٌ ولا `UNREGISTERED_WORK`)
  tests/governance/test_w063_registered_claims.py                 (‏يُنقَلُ وجهُ «كلُّ مُدَّعٍ مُعلَنٌ» إلى القراءةِ الصريحةِ · وتُضافُ أوجهٌ)
  وسجلّاتُ الحالةِ والحوكمةِ **لا تُدَّعى في مساراتِ هذا البندِ**: تُمَسُّ بحكمِ واجبِ § 7 (‏`CLAIM_CONFLICT` § 6.1)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - خمسةُ بنودٍ في المراجعةِ (`WI-023` · `WI-024` · `WI-025` · `WI-026` · `WI-027`) تقفلُ مساراتٍ أخرى — **ولا يلمسُها هذا البندُ**
  - `tools/governance/mutation_claims.py` كانَ مُعلَنًا في مساراتِ `WI-017` وهي `CLOSED` منذُ 2026-08-29، و`tests/governance/test_w063_registered_claims.py` في `WI-018` وهي `CLOSED` كذلك: لا تداخل
  - `tools/governance/mutation_probe.py` **لا يُمَسُّ**: التشغيلُ فيه، وما يُصلَحُ هنا **قراءةُ الدعوى** لا إعادةُ العَطبِ
  - لا جدولَ ولا migration ولا مسارَ API ولا عقدَ ولا سرَّ ولا مورِدَ تشغيلٍ · ولا قرارَ `Q-###` مفتوحًا يتوقَّفُ عليه · وفئةُ التغييرِ `C0`
  - **واسمُ النطاقِ قِيسَ لا افتُرِضَ**: `DISC-033` يُسمّي البندَ التاليَ «`tests-integrity`» و**لا صفَّ لهذا النطاقِ في `OWNERSHIP.md`** — فأسقطَ `check_work_governance.py` الحجزَ بـ`SCOPE_UNOWNED` (‏رمزُ 1) قبلَ أيِّ مسٍّ. **ولم يُختَرَعْ نطاقٌ ولا سُجِّلَ صفٌّ جديدٌ**: إنشاءُ نطاقٍ وتعيينُ مالكِه قرارُ سجلِّ مِلكيّةٍ لا فعلُ عاملٍ، فحُجِزَ البندُ في `tooling-gates` — النطاقِ المُسجَّلِ الذي يحوي المسارَينِ فعلًا — وبقيَ اسمُ `DISC-033` كما كُتِبَ (‏التاريخُ لا يُعادُ كتابتُه)
خارجَ النطاق:
  - **لا يُخفَّفُ الحرسُ ولا يُكذَبُ في السجلِّ**: `UNREGISTERED_WORK` لا يُزادُ فيها قيدٌ لم يَدَّعِ دعوى — وهو الطريقُ الضارُّ الذي سمّاهُ `DISC-033` نصًّا
  - **ولا يُحذَفُ وجهٌ قائمٌ**: «كلُّ قيدٍ مُدَّعٍ مُعلَنٌ» يبقى مُسقِطًا — يتغيَّرُ **كيفَ يُعرَفُ المُدَّعي** لا أنَّه يُعرَفُ
  - **ولا يُعادُ كتابةُ التاريخِ**: صفوفُ السجلِّ القديمةُ لا تُصاغُ من جديدٍ لِتُوافِقَ قارئًا جديدًا — تُجمَّدُ كما قِيسَت
  - **ولا تُحسَمُ قراراتُ المالكِ**: مراجعةُ `WI-023`…`WI-027` · `origin/develop` · سرُّ `T0.6` · `A-3` · استقلالُ المراجعةِ · أسئلةُ `T2`
معيارُ القبول:
  1. الدعوى تُقرَأُ **بإعلانٍ صريحٍ**: عبارةٌ محجوزةٌ مُعلَنةٌ في `mutation_claims.py` — لا بجذرِ كلمةٍ في نصٍّ حرٍّ
  2. صفٌّ يستعملُ «الوثبَ» أو «الطفرَ» بمعنى القفزِ **لا يُقرَأُ دعوى** — يُقاسُ بنصٍّ مُصطَنَعٍ فلا يُطمَأنُّ إليه بالظنِّ
  3. صفٌّ يُعلِنُ دعوى بالعبارةِ المحجوزةِ ولا يُسجَّلُ ولا يُسمّى ناقصًا **يُسقِطُ الفحصَ**
  4. الصفوفُ التاريخيّةُ الثلاثةَ عشرَ التي قرأَها الجذرُ **مُجمَّدةٌ مُعلَنةً** وكلٌّ منها مُعلَنُ الحالةِ (‏مُسجَّلٌ أو مُسمًّى في النقصِ)، ومعرِّفٌ مُجمَّدٌ بلا صفٍّ في § 8 يُسقِطُ
  5. مجموعُ `tests/governance` أخضرُ بمعناهُ · والسقّاطةُ 63 · و`ruff` نظيفٌ
  6. حكمُ CI يُقرأُ برقمِ تشغيلٍ، ولا يُقرأُ الأخضرُ إغلاقًا (§ 4.3)
الدليلُ المطلوب:
  python -m pytest tests/governance/test_w063_registered_claims.py -q
  python -m pytest tests/governance -q  &&  ruff check .
  python tools/governance/truth_audit.py . --ratchet                  # المتوقَّع: ثابتٌ عندَ 63
بدأ: 2026-09-01        ينتهي الحجز: 2026-09-30
العائق: انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — عُيِّنَ مراجعًا لهذا النطاقِ بـ`Q-43`. **والحجزُ جُدِّدَ في `W-152`** بنصِّ § 6.3 (‏الحجزُ ينتهي إن لم يُحدَّثْ): المالكُ نفسُه ولا استلامَ، والسببُ مُعلَنٌ لا مطويٌّ — انقضى 2026-09-08 والبندُ ما زالَ `IN_REVIEW` بلا مراجعٍ مُشغَّلٍ، فحمَّرَ `RESERVATION_EXPIRED` سبعةَ بنودٍ وأسقطَ «Cross-System Suites» في CI.
الخطوةُ التالية: مراجعةُ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — والكاتبُ لا يُصدِّقُ نفسَه (§ 4.3)
حكمُ CI المقروءُ: `bf484fe` ⇒ تشغيلُ `33494440719` ⇒ `success` · 13/13 · `READABLE`
  (‏وقبلَه `f69f51c` ⇒ `33490638690` ⇒ `failure` فأُصلِحَ سببُه في `W-094`)
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا يُصلِحُ قراءةَ الدعوى لا اكتمالَها**: تسعةُ قيودٍ دعاويها غيرُ مُسجَّلةٍ تبقى مُسمّاةً في `UNREGISTERED_WORK` — نقصٌ مُعلَنٌ يُسَدُّ قيدًا بعدَ قيدٍ
  - **والعبارةُ المحجوزةُ مُعلَنةٌ لا مُكتشَفةٌ**: صفٌّ يَدَّعي دعوى بلغةٍ أخرى لا يراهُ هذا الحرسُ — وهو الحدُّ نفسُه القائمُ في كلِّ قائمةٍ مكتوبةٍ في الشِفرةِ
  - **ولا يُقرأُ هذا إغلاقًا لِـ`DISC-033`**: الحالةُ تُقرأُ بعدَ حكمٍ مقروءٍ ومراجعةٍ (§ 4.3)
قيدُ السجلّ: W-092 · الحجزُ ⟶ W-093 · التنفيذُ ⟶ W-094 · إصلاحُ سببِ الحمرةِ (‏المِسبارُ 31/31) ⟶ W-095 · حكمٌ مقروءٌ ونقلٌ إلى المراجعةِ
```

### WI-029 — «الفحصُ يقرأُ الشجرةَ التي يُعلِنُها» يُقاسُ بحرسٍ لا بعينٍ

```text
النطاق: tests-root (‏`tests` — النطاقُ المُسجَّلُ في `OWNERSHIP.md` الذي يحوي المسارَينِ · فئةُ التغييرِ `C0`)
المسار/المرحلة: T0 (قابليّةُ القياسِ — فحصٌ يخضَرُّ أو يحمَرُّ من حالِ المستودعِ الحقيقيِّ لا من صدقِ دعواهُ · `DISC-032`)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_REVIEW
المسارات:
  tests/governance/test_w096_subprocess_measurement_site.py       (‏جديدٌ — يُحصي نمطَ `DISC-032` في `tests/` كلِّها ويُسقِطُ على كلِّ موضعٍ غيرِ مُرسًى)
  tests/governance/test_w054_post_merge_reverse_link.py            (‏يُرسى موضعُ القياسِ في الموضعِ الوحيدِ الذي كشفَه القياسُ · السطرُ 216)
  وسجلّاتُ الحالةِ والحوكمةِ **لا تُدَّعى في مساراتِ هذا البندِ**: تُمَسُّ بحكمِ واجبِ § 7 تحتَ دعوى `WI-023` القائمةِ وبقائدٍ واحدٍ (§ 6.1 · `CLAIM_CONFLICT`)
فحصُ التداخلِ (§ 6.2) — نتيجتُه تُقيَّدُ ولو كانت «لا تداخل»:
  - ستَّةُ بنودٍ في المراجعةِ (`WI-023`…`WI-028`) تقفلُ مساراتٍ أخرى — و**لا يلمسُ هذا البندُ واحدًا منها**: `test_w077` · `test_w079` · `test_w083` · `test_runtime_state_stays_outside_the_tree` · `test_w057` · `test_w063` كلُّها خارجَ مسارَيْ هذا البندِ
  - `tests/governance/test_w054_post_merge_reverse_link.py` كانَ مُعلَنًا في مساراتِ `WI-020` و`WI-021` وهما `CLOSED` (‏`W-070` · `W-075`): لا تداخل
  - `.github/workflows/ci.yml` **لا يُمَسُّ** وهو مقفولٌ بـ`WI-023`: الفحصُ الجديدُ تحتَ `tests/governance/` فيُنفَّذُ بخطوتَيْ pytest القائمتَينِ في CI (‏السطرُ 117 `pytest tests/governance/` والسطرُ 579 `pytest tests/ --cov`) — فطريقُ الإنفاذِ قائمٌ بلا مسِّ مسارٍ مقفولٍ
  - **ولا أداةَ جديدةً تُزادُ في `tools/`**: القياسُ يسكنُ الفحصَ نفسَه — فلا مصدرَ حقيقةٍ مُكرَّرًا، ولا صفَّ جديدًا في `VERDICT_CAPABLE_UNWIRED` (‏10 اليومَ)، ولا نطاقًا ثانيًا يُدَّعى
  - **واسمُ النطاقِ قِيسَ لا افتُرِضَ**: `DISC-032` يُسمّي البندَ التاليَ «`tests-integrity`» و**لا صفَّ لهذا النطاقِ في `OWNERSHIP.md`** — وإنشاءُ نطاقٍ وتعيينُ مالكِه قرارُ سجلِّ مِلكيّةٍ لا فعلُ عاملٍ (‏`DISC-008` · `RK-012`)، فحُجِزَ البندُ في `tests-root`، ونصُّ `DISC-032` بقيَ كما كُتِبَ
  - لا جدولَ ولا migration ولا مسارَ API ولا عقدَ ولا سرَّ ولا مورِدَ تشغيلٍ · ولا قرارَ `Q-###` مفتوحًا يتوقَّفُ عليه
خارجَ النطاق:
  - **لا يُخفَّفُ فحصٌ ولا يُسكَتُ**: الموضعُ المكشوفُ يُصلَحُ بإرساءِ محلِّ القياسِ (`--repo-root`) لا بحذفِ تأكيدٍ ولا بـ`xfail` ولا بتليينِ رمزِ الخروجِ
  - **ولا تُمَسُّ الأدواتُ**: `check_work_governance.py` لا يُعادُ تصميمُ `REPO_ROOT` فيها في هذا البندِ — النمطُ في ثلاثين أداةً، وتغييرُ المِرساةِ فيها كلِّها بندٌ آخرُ في `tooling-gates`
  - **ولا تُمَسُّ المواضعُ التي تقصِدُ المستودعَ الحقيقيَّ عن عمدٍ** (19 موضعًا): قصدُها مشروعٌ، والحرسُ يُميِّزُها بمحلِّ القياسِ لا بالحظرِ
  - **ولا تُحسَمُ قراراتُ المالكِ**: مراجعةُ `WI-023`…`WI-028` · `origin/develop` · سرُّ `T0.6` · `A-3` · استقلالُ المراجعةِ · إنشاءُ نطاقِ `tests-integrity` · أسئلةُ `T2`
معيارُ القبول:
  1. **العَطبُ يُحصى لا يُقدَّرُ**: الفحصُ الجديدُ يقرأُ `tests/` كلَّها ويُصنِّفُ كلَّ تشغيلِ أداةٍ في عمليّةٍ فرعيّةٍ إلى: يقصِدُ المستودعَ الحقيقيَّ · مِرساتُه صادقةٌ · **يحكُمُ على شجرةٍ لا يقرؤها** — والثالثُ يُسقِطُ الفحصَ
  2. **الحرسُ يُسقِطُ فعلًا**: يُقاسُ بنصٍّ مُصطَنَعٍ يحملُ النمطَ فيُسقِطُ، وبنصٍّ مُرسًى فلا يُسقِطُ — فلا يُطمَأنُّ إلى خضرةٍ لم تُختَبَرْ
  3. **الموضعُ المكشوفُ يصيرُ صادقًا**: `test_w054...py::test_رفضٌ_مُعلَنٌ_حينَ_يُطلَبُ_الأساسُ_ولا_يُقرَأ` يقيسُ شجرتَه المؤقَّتةَ، ورمزُ خروجِه 2 يأتي من تلك الشجرةِ — ويُثبَتُ بأنَّ إزالةَ الشجرةِ تُغيِّرُ الحكمَ
  4. مجموعُ `tests/governance` أخضرُ بمعناهُ · والسقّاطةُ 63 · و`ruff` نظيفٌ · وكلُّ بوّابةٍ محلّيّةٍ رمزُها 0
  5. حكمُ CI يُقرأُ برقمِ تشغيلٍ، ولا يُقرأُ الأخضرُ إغلاقًا (§ 4.3)
الدليلُ المطلوب:
  python -m pytest tests/governance/test_w096_subprocess_measurement_site.py -q
  python -m pytest tests/governance/test_w054_post_merge_reverse_link.py -q
  python -m pytest tests/governance -q  &&  ruff check .
  python tools/governance/truth_audit.py . --ratchet                  # المتوقَّع: ثابتٌ عندَ 63
بدأ: 2026-09-01        ينتهي الحجز: 2026-09-30
العائق: انتظارُ دورِ المراجعةِ لدى مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — عُيِّنَ مراجعًا لهذا النطاقِ بـ`Q-43`. **والحجزُ جُدِّدَ في `W-152`** بنصِّ § 6.3 (‏الحجزُ ينتهي إن لم يُحدَّثْ): المالكُ نفسُه ولا استلامَ، والسببُ مُعلَنٌ لا مطويٌّ — انقضى 2026-09-08 والبندُ ما زالَ `IN_REVIEW` بلا مراجعٍ مُشغَّلٍ، فحمَّرَ `RESERVATION_EXPIRED` سبعةَ بنودٍ وأسقطَ «Cross-System Suites» في CI.
الخطوةُ التالية: مراجعةُ مجلسِ المراجعةِ (GPT 5.6 + Grok 4.6) — والنقلُ إلى `VERIFIED` فعلُ المراجعِ لا فعلُ الكاتبِ (§ 4.3)
حكمُ CI المقروءُ: عقدةُ البندِ `9bf0b00` ⇒ **أحمرُ** 12/13 (تشغيلُ 33570417864 · رقمُ 55 · `READABLE`) بسببٍ خارجَ نطاقِه (خطوةُ «المصفوفةُ المدفوعةُ محدَّثةٌ») — و**وظيفةُ `Tests` خضِرَت** فالحرسُ نُفِّذَ في CI وسكتَ على شجرةٍ صادقةٍ · ثمَّ العقدةُ التاليةُ `815d707` ⇒ **أخضرُ 13/13** (تشغيلُ 33572642082 · رقمُ 56 · `READABLE`) وهي تحملُ مسارَيِ البندِ بلا تغيُّرٍ
خطُّ الأساسِ المقيسُ قبلَ أيِّ مسٍّ (‏`W-096` · يُعادُ إنتاجُه بالفحصِ الجديدِ):
  تشغيلاتُ أدواتٍ في عمليّاتٍ فرعيّةٍ داخلَ `tests/`      24
  منها تقصِدُ المستودعَ الحقيقيَّ عن عمدٍ                 19
  منها تقصِدُ شجرةً مؤقَّتةً                                5
      مِرساتُها صادقةٌ (‏المُشغَّلُ داخلَ الشجرةِ أو محلُّ القياسِ مُمرَّرٌ)   4
      **تحكُمُ على شجرةٍ لا تقرؤها**                                        1
  والموضعُ: `tests/governance/test_w054_post_merge_reverse_link.py:216`
  وإثباتُه بالتشغيلِ لا بالنظرِ: الأمرُ نفسُه من دليلٍ **فارغٍ** بلا سجلٍّ ولا شجرةٍ يخرُجُ بـ`2` — فالشجرةُ التي يبنيها الفحصُ لا تُقرأُ أصلًا
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **هذا يُحصي النمطَ في `tests/` ولا يُصلِحُ مِرساةَ الأدواتِ**: `REPO_ROOT = Path(__file__).resolve().parents[2]` قائمٌ في نحوِ ثلاثينَ أداةً، وهو أصلُ العَطبِ لا فرعُه — يبقى نقصًا مُعلَنًا يُوجَّهُ بندًا في `tooling-gates`
  - **والحرسُ يقرأُ الشِفرةَ تركيبيًّا (AST) لا سلوكًا**: فحصٌ يُبني أمرَه بطريقةٍ لا يراها القارئُ التركيبيُّ لا يُحصى — حدٌّ من جنسِ كلِّ قارئٍ ساكنٍ، ويُعلَنُ في نصِّ الفحصِ نفسِه
  - **ولا يُقرأُ هذا إغلاقًا لِـ`DISC-032`**: الحالةُ تُقرأُ بعدَ حكمٍ مقروءٍ ومراجعةٍ (§ 4.3)
قيدُ السجلّ: W-096 · الحجزُ وقياسُ خطِّ الأساسِ
  و**خليّةُ «قيدُ السجلّ» في صفِّ § 1 تُكتَبُ `—` بسابقةٍ مقيسةٍ لا بتخفيفٍ**: البوّابةُ تقرأُ تلك الخليّةَ وحدَها، فذِكرُ قيدٍ أُضيفَ في مجموعةِ التغييرِ نفسِها يُشعِلُ `POST_MERGE_NOT_CLOSED` على بندٍ حالتُه `RESERVED` — وذاك تناقضٌ مع § 4.3 لا خرقٌ من العاملِ، مُقيَّدٌ في `DISC-010` (‏«تلك الخليّةُ يكتبُها مَن يجبُ عليه الإغلاقُ، فتكونُ `—`») و`DISC-030` (‏«نافذةُ الالتزامِ الواحدِ» · وتفعيلُ الإسقاطِ افتراضًا قرارُ `A-3` بيدِ المالكِ). والدليلُ لم يُخفَ: القيدُ مُسمًّى هنا، و`W-096` في § 8 يُسمّي `WI-029` نصًّا
```

---


### WI-050 — تفعيلُ A-3 + إصلاحُ إخفاقاتِ Identity Law

```text
النطاق: governance-docs
المسار/المرحلة: T0 (قابليّةُ القياسِ — تفعيلُ بوّابةِ work-governance-gate بوضعِ الإسقاط + إصلاحُ إخفاقاتِ CI)
المالك: Perplexity Computer            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED   (‏`VERIFIED` ← `CLOSED` · § 4.3 — أُغلقَ بـ`W-144` بعدَ اعتمادِ `VERIFIED` بـ`W-143` · المراجعةُ غيرُ مستقلّةٍ (`DISC-027` · `RK-020`) · `A-2`)
المسارات:
  docs/governance/work/THE_ROADMAP.md        (غيرُ مُدَّعًى — متاحٌ)
  docs/governance/work/DISCOVERIES.md         (معفيةٌ من الحجزِ بنصِّ § 6)
خارجَ النطاق:
  - لا يُمَسُّ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/
  - لا تُمَسُّ الأدواتُ في tools/ ولا الفحوصُ في tests/
  - لا يُمَسُّ .github/workflows/ci.yml (مقفولٌ بـWI-023)
  - PROJECT_HANDBOOK.md يُحدَّثُ بواجبِ § 7 (مزامنةُ وثائقِ الحالةِ) لا بادّعاءِ المسارِ
معيارُ القبول:
  1. A-3 يصيرُ `APPROVED` في § 16.4
  2. TRUTH_LIMIT_BASELINE يُصحَّحُ إلى `ambiguous_references=24`
  3. PROJECT_HANDBOOK.md يُشيرُ إلى W-139
  4. CI يصيرُ أخضرَ 13/13
الدليلُ المطلوب:
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_repository_identity.py .
  python tools/governance/truth_audit.py . --ratchet
  python tools/governance/ci_verdict_readability.py --from-json <ci_run_json>
بدأ: 2026-09-07        ينتهي الحجز: 2026-09-14
العائق: —
الخطوةُ التالية: دفعُ التغييراتِ إلى main ثمَّ قراءةُ حكمِ CI
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - A-3 يُفعِّلُ الإسقاطَ لكنَّهُ لا يُعيِّنُ مراجعًا مستقلًا (RK-020 · DISC-027 يبقيانِ مفتوحَينِ)
  - PROJECT_HANDBOOK.md محدَّثٌ بواجبِ § 7 لا بادّعاءِ مسارٍ (مقفولٌ بـWI-023)
  - لا يُمَسُّ .github/workflows/ci.yml (مقفولٌ بـWI-023)
  - ولا يُحلُّ بندٌ IN_REVIEW بيدِ المنفِّذ (§ 4.3)
قيدُ السجلّ: W-140 (يُكتبُ عندَ الإغلاقِ)
```

### WI-049 — خطُّ أساسِ المستودعِ الجديدِ: قياسُ حالةِ CI على `vooovg-ui/AMOS-Fedration`

```text
النطاق: ci-pipeline / audit-truth
المسار/المرحلة: T0 (قابليّةُ القياسِ — خطُّ أساسٍ على مستودعٍ جديدٍ)
المالك: Perplexity Computer            المراجع: المالك (`A-2` · غيرُ مستقلٍّ)
الحالة: CLOSED   (‏`VERIFIED` ← `CLOSED` · § 4.3 — أُغلقَ بـ`W-144` بعدَ اعتمادِ `VERIFIED` بـ`W-143` · المراجعةُ غيرُ مستقلّةٍ (`DISC-027` · `RK-020`) · `A-2`)
المسارات:
  docs/governance/work/ACTIVE_WORK.md        (معفيةٌ من الحجزِ بنصِّ § 6)
  docs/audit/COMPLETION_LEDGER.md             (معفيةٌ من الحجزِ بنصِّ § 6)
  PROJECT_STATE.md                            (سطرُ قيدٍ — معفيةٌ بنصِّ § 6)
  docs/audit/ACTIVE_EXECUTION_STATE.md       (سطرُ قيدٍ — معفيةٌ بنصِّ § 6)
خارجَ النطاق:
  - لا يُمَسُّ كودُ التطبيقِ في core/ federal/ states/ agents/ runtime/
  - لا تُمَسُّ الأدواتُ في tools/ ولا الفحوصُ في tests/
  - لا يُمَسُّ .github/workflows/ci.yml (مقفولٌ بـWI-023)
  - لا يُعدَّلُ نصٌّ دستوريٌّ ولا مرسوم
  - لا تُحلُّ بنودٌ IN_REVIEW بيدِ المنفِّذ (§ 4.3)
  - لا يُغلقُ DISC-006 — يُقىاسُ حالُه على الحسابِ الجديدِ لا يُدَّعى زوالُه
فحصُ التداخلِ (§ 6.2) — نتيجتُه: لا تداخلَ
  - المساراتُ المُعلَنةُ معفاةٌ من الحجزِ بنصِّ § 6 (DISCOVERIES.md · RISK_REGISTER.md ·
    ACTIVE_WORK.md · COMPLETION_LEDGER.md وسطرُ آخرِ قيدٍ في وثيقتَي الحالةِ)
  - لا مسارَ تطبيقيٍّ يُمَسُّ ولا أداةٌ ولا فحصٌ
معيارُ القبول:
  1. CI يُشغَّلُ على هذا المستودعِ لأوّلِ مرّةٍ (التشغيلُ الأوّلُ على vooovg-ui)
  2. حكمُ CI يُقرأُ بـci_verdict_readability.py ويُقيَّدُ برقمِ تشغيلٍ ورابطِه
  3. مصفوفةُ الحقيقةِ ثابتةٌ عندَ 63 (لا زيادة)
  4. هويةُ المستودعِ ناجحةٌ
  5. حوكمةُ العملِ ناجحةٌ (self-check)
  6. يُقيَّدُ ما أعطاهُ التشغيلُ وإن خالفَ المتوقَّعَ — لا يُطوى
الدليلُ المطلوب:
  python tools/governance/check_repository_identity.py .
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/truth_audit.py
  python tools/governance/ci_verdict_readability.py --from-json <ci_run_json>
بدأ: 2026-09-07        ينتهي الحجز: 2026-09-14
العائق: —
الخطوةُ التالية: دفعُ التسجيلِ إلى main لإحراكِ CI ثمَّ قراءةُ الحكمِ
حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - هذا بندُ قياسٍ لا إنجازٌ: يُقياسُ هل CI يعملُ على الحسابِ الجديدِ، ولا يُدَّعى زوالُ DISC-006
  - وDISC-006 كانَ على حسابِ xoos-beep لا vooovg-ui — فالقياسُ هنا جديدٌ لا تحويلٌ
  - ولا يُحلُّ بندٌ IN_REVIEW بيدِ المنفِّذ (§ 4.3) — القرارُ بيدِ المراجعِ
  - والمراجعةُ ليست مستقلَّةً استقلالًا حقيقيًّا (A-2 · DISC-027 · RK-020)
قيدُ السجلّ: — (يُكتَبُ عندَ الإغلاقِ)
```

### WI-051 — تسجيل قرار سيادي Q-43: تعيين مجلس مراجعة مستقل بالنماذج

```text
النطاق: governance-docs / decisions
المسار/المرحلة: T2 (الحوكمة والتوثيق المحروس)
المالك: Driving H            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6) — والشقُّ `C3` (`decisions`) يحسمُه المالك
الحالة: CLOSED   (‏`VERIFIED → CLOSED` · § 4.3 — أُغلِقَ بـ`W-158` **بعدَ قراءةِ حكمِ CI على عقدةِ الاعتمادِ `W-157` (`df32bd8f`)**: التشغيلُ 34562272448 (‏`run_number` 22 · `run_attempt` 1) ⇒ `success` · **14 خضراءَ · 0 حمراءَ · 0 متخطّاةٍ** بالعدِّ الثلاثيِّ — فحدُّ التسلسلِ `DISC-060` أُدِّيَ ولم يُغلَقْ بندٌ على عقدةٍ بلا حكمٍ. و**الاعتمادُ `VERIFIED` وقعَ بـ`W-157` بيدِ مجلسِ المراجعةِ المستقلِّ لا بيدِ المؤلِّفِ**: إجماعُ الجولةِ الرابعةِ على عقدةِ `W-156` (`408e772c`) — المراجعُ «أ» (`GPT 5.6 Sol`) ⇒ `VERIFIED` بـ`P1=0`، والمراجعُ «ب» (`Grok 4.6`) ⇒ `VERIFIED` بـ`P1=0`، كلٌّ في حاويةٍ منفصلةٍ ونسخةٍ مستقلّةٍ وبيئةٍ افتراضيّةٍ خاصّةٍ وتكليفٍ أعمى، وكلٌّ أقرَّ استقلالَه صريحًا. **وثلاثُ الجولاتِ السابقةِ لم تُعطِ إجماعًا وتُقيَّدُ كما وقعت لا تُمحى**: `IN_PROGRESS → IN_REVIEW` بيدِ المالكِ في `W-150` — § 4.3. **وثلاثُ جولاتٍ من المراجعةِ المعزولةِ لم تُعطِ إجماعًا**: الأولى رُفِضَت بإجماعِ النموذجَينِ (‏سبعةُ عيوبٍ · عُولِجَت في `W-150`)، والثانيةُ رُفِضَت بإجماعِهما أيضًا (‏عيبانِ + خمسةٌ · عُولِجَ اتّحادُها في `W-152`)، والثالثةُ **انقسمَت**: المراجعُ ب مَنحَ `VERIFIED` بثلاثةِ عيوبٍ غيرِ `P1`، والمراجعُ أ رفضَ بعيبٍ `P1` (‏إجراءُ `Q-43` غيرُ ذَرِّيٍّ) وثلاثةٍ دونَه — فعُولِجَ اتّحادُ الأربعةِ والثلاثةِ في `W-154`. **ولا يُنقَلُ إلى `VERIFIED` إلّا بمنحِ المراجعَينِ معًا**، ولا يمنحُها صاحبُ التغييرِ . **ودورةُ النقلِ بعدَ كلِّ رفضٍ مُعلَنةٌ**: `IN_REVIEW → IN_PROGRESS` عندَ الرفضِ ثمَّ `IN_PROGRESS → IN_REVIEW` بعدَ الإصلاحِ — ثلاثَ مرَّاتٍ (`W-150` · `W-152` · `W-154`)، وكلُّها نقلاتٌ مشروعةٌ في § 4.3 ولا واحدةَ منها `VERIFIED`)
المسارات:
  docs/audit/SOVEREIGN_DECISION_REGISTER.md
  docs/governance/work/THE_ROADMAP.md
  docs/governance/work/OWNERSHIP.md
  docs/governance/work/ACTIVE_WORK.md
  docs/governance/work/RISK_REGISTER.md
  docs/governance/work/DISCOVERIES.md
  .github/workflows/ci.yml          ← أُفرِجَ عنه من WI-023 بقرارِ Q-44
  PROJECT_STATE.md                  ← أُفرِجَ عنه من WI-023 بقرارِ Q-44
  docs/PROJECT_HANDBOOK.md          ← أُفرِجَ عنه من WI-023 بقرارِ Q-44
  tests/governance/test_w150_gate_enforcement_in_ci.py   ← حارسٌ جديدٌ (‏مسارٌ لا مُدَّعيَ له)
  tests/governance/test_w154_reviewer_consistency.py     ← حارسٌ جديدٌ في `W-154` (‏مسارٌ لا مُدَّعيَ له)
  docs/audit/measurements/final_audit_p14.json           ← قياسٌ أُعيدَ توليدُه في W-151 بعدَ Q-44
خارج النطاق:
  - لا يعدل نص دستوري ولا مرسوم
  - لا يمس كود التطبيق في core/ federal/ states/ agents/ runtime/
  - لا يعدل منطق اي بوابة: `ci.yml` يُمَسُّ في **سطرَي استدعاءٍ** فقط
    (‏رفعُ `--advisory` من بوابة 2 تنفيذًا لـ`A-3`)، ولا تُعدَّلُ أداةٌ
  - لا يرقي WI-023 ولا يغلقه: يبقى `IN_REVIEW` ومراجعتُه مستحقّةٌ
  - لا يمنح المنفذُ نفسَه `VERIFIED` (section 4.3)
فحص التداخل (section 6.2) — نتيجته: لا تداخل **بعدَ قسمةِ Q-44**
  - سجلّاتُ الحوكمةِ الستُّ معفاةٌ من الحجزِ بنصِّ section 6
  - المساراتُ الثلاثةُ المضافةُ كانت مقفولةً بـ`WI-023` (`IN_REVIEW`)،
    وأُفرِجَ عنها بـ**قسمةِ البند** — أوّلِ الطرقِ الثلاثةِ في section 6.1 —
    بقرارِ المالكِ `Q-44`. ولا بندَ نشِطٌ آخرُ يُعلِنُها: قُرِئَ جدولُ § 1 كلُّه،
    و`WI-041`/`WI-042` حالتُهما `READY` و`READY` **لا تقفلُ مسارًا** (section 6.1)
معيار القبول:
  1. قرار Q-43 مسجل في SOVEREIGN_DECISION_REGISTER.md
  2. A-2 محدث في THE_ROADMAP.md section 16.5
  3. OWNERSHIP.md محدث بتعيين المراجع المستقل
  4. RK-020 و DISC-027 يعلنان الاغلاق — و`RK-020` **يُرفَعُ من جدولِ
     «§ 1 · المخاطرُ المفتوحة»** لا تُحرَّرُ خليّتُه وحدَها، لأنَّ
     `open_record_accountability.py` يقرأُ كلَّ سطرٍ `| RK-### |` مفتوحًا بالثابت
  5. check_work_governance.py --self-check ناجح
  6. المراجعة المستقلة بـGPT 5.6 و Grok 4.6 تمنح VERIFIED
  7. **حكمُ CI مُقيَّدٌ برقمِه ورابطِه معًا** (§ 7 واجب 6 · § 16.5 شرط 2) —
     الرقمُ وحدَه لا يكفي، وهو ما أسقطَه المجلسُ بإجماعٍ في الجولةِ الأولى
  8. **`state_document_drift.py` يخرجُ بـ0**، و`test_w057_state_document_drift.py`
     يمرُّ باختبارَيه — وهو السببُ الجذريُّ الوحيدُ لحمرةِ الوظائفِ الثلاثِ
  9. **§ 16.5 والملفُّ يقولان الشيءَ نفسَه**: إن قيلَ إنَّ البوّابةَ نافذةٌ
     إسقاطًا فلا `--advisory` في `ci.yml`
الدليل المطلوب:
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_work_governance.py --commit HEAD
  python tools/governance/truth_audit.py . --ratchet
  python tools/governance/check_repository_identity.py .
  python tools/governance/state_document_drift.py
  python tools/governance/open_record_accountability.py
  python -m pytest tests/governance -q
بدأ: 2026-09-08        ينتهي الحجز: 2026-09-30
حكمُ CI على حالةِ الدولةِ (§ 16.5 شرطُ 2 · § 7 واجب 6 — مقروءٌ ومُقيَّدٌ **برقمِه ورابطِه** لا مطويٌّ):

  · **تشغيلُ عقدةِ `W-152`** (‏وكانَ يُوصَفُ ههنا «الأحدثَ على رأسِ البندِ» حتّى صحَّحَه المراجعانِ معًا في الجولةِ الرابعةِ · `D-2`) — `55bced2`:
    رقمُه **34295388651** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34295388651>
    ⇒ **success** · مقروءٌ بفحوصِ العقدةِ (‏`commits/55bced2/check-runs`) ·
    **14 خضراءَ و0 حمراءَ و0 متخطّاةٍ** — فالخُضرةُ **مقروءةٌ بالعدِّ الثلاثيِّ**
    (‏نصُّ `DISC-060`) لا مُستنتَجةً من غيابِ الحمرةِ، ولا وظيفةَ حُجِبَت خلفَ
    `needs:`. وزالَت حمرةُ «Cross-System Suites» بزوالِ سببِها المقيسِ:
    `RESERVATION_EXPIRED` في `WI-024` … `WI-030`.
    وعلى العقدةِ نفسِها سيرُ عملٍ ثانٍ **أخضرُ**: «مصفوفةُ الحقيقةِ المولَّدة»
    رقمُه **34295388653** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34295388653>.
    **وحدُّ التسلسلِ مُعلَنٌ لا مطويٌّ**: تقييدُ هذا الحكمِ يُنشئُ عقدةً جديدةً
    (`W-153`) لا حكمَ لها بعدُ عندَ لحظةِ الكتابةِ — فحكمُها يُقرأُ ويُقيَّدُ
    بعدَ دفعِها وقبلَ أيِّ `CLOSED`، ولا يُدَّعى أنَّ آخرَ عقدةٍ مقروءةٌ سلفًا.

  · **والعقدةُ التاليةُ قُرِئَ حكمُها أيضًا** — `3fed13f` (‏`W-153`):
    رقمُه **34297000390** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34297000390>
    ⇒ **success** · `commits/3fed13f/check-runs` ⇒ `{total:14, success:14}` ·
    **14 خضراءَ و0 حمراءَ و0 متخطّاةٍ**؛ وسيرُ العملِ الثاني «مصفوفةُ الحقيقةِ
    المولَّدة» رقمُه **34297000416** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34297000416> ⇒ **success**.
    **وحدُّ التسلسلِ يبقى قائمًا**: عقدةُ `W-154` نفسُها لا حكمَ لها عندَ الكتابةِ،
    ويُقرأُ حكمُها بعدَ دفعِها وقبلَ أيِّ نقلٍ إلى `VERIFIED` أو `CLOSED`.

  · **وعقدةُ `W-154` قُرِئَ حكمُها كذلك** — `7ad990c`:
    رقمُه **34301063337** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34301063337>
    ⇒ **success** · `commits/7ad990c/check-runs` ⇒ `{total:14, success:14}` ·
    **14 خضراءَ و0 حمراءَ و0 متخطّاةٍ**؛ وسيرُ «مصفوفةِ الحقيقةِ المولَّدة»
    رقمُه **34301063334** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34301063334> ⇒ **success**.

  · **وعقدةُ `W-155` قُرِئَ حكمُها بالعدِّ الثلاثيِّ** — `5be999f`:
    رقمُه **34303197855** (‏`run_number` 20) · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34303197855>
    ⇒ **success** · `commits/5be999f/check-runs` ⇒
    `{total:14, success:14, failure:0, skipped:0, other:[]}` ·
    **14 خضراءَ و0 حمراءَ و0 متخطّاةٍ** — والعدُّ ثلاثيٌّ بنصِّ `DISC-060`
    لا استنتاجًا من غيابِ الحمرةِ؛ وسيرُ «مصفوفةِ الحقيقةِ المولَّدة»
    رقمُه **34303197937** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34303197937> ⇒ **success**.

  · **وعندَ استئنافِ العملِ كانَ العائقُ المقيسُ الوحيدُ `RESERVATION_EXPIRED` ثمانيَ
    مرّاتٍ** (`WI-031` … `WI-038` — حجوزُها انتهت في 2026-09-09 و2026-09-10
    والتاريخُ اليومَ 2026-09-11) فأسقطَ `check_work_governance.py --self-check`
    بـ`exit=1`، **وهو عينُ العَطبِ `P1` الذي أسقطَه المراجعانِ معًا في الجولةِ الثانيةِ**.
    فجُدِّدَ الحجزُ إلى **2026-09-30** بنصِّ § 6.3 في **22 صفًّا و22 كتلةً**،
    **والسببُ مكتوبٌ في خليّةِ «العائق» من الصفِّ وفي الكتلةِ معًا** — لا في الكتلِ
    وحدَها كما فعلَ `W-152` وأسقطَه المراجعُ في الجولةِ الثالثةِ.
    **ونطاقُ التجديدِ مقيسٌ لا مُختارٌ**: هو عينُ المجموعةِ التي تقرؤها
    `check_work_governance.py:483` (`RESERVED`/`IN_PROGRESS`/`IN_REVIEW`)،
    **وبنودُ `READY` الخمسةُ لم تُمَسَّ** (`WI-040` · `WI-041` · `WI-042` · `WI-044` ·
    `WI-048`) لأنَّ البوّابةَ لا تقرأُ حجزَها. **ولا يُقرأُ التجديدُ إنجازًا ولا مراجعةً**:
    لا بندَ واحدًا من الاثنينِ والعشرينَ رُقِّيَت حالتُه.

  · **والجولةُ الرابعةُ من المراجعةِ المعزولةِ لم تُشغَّلْ — والعائقُ بيئيٌّ مُعلَنٌ لا
    حكمٌ مطويٌّ**: أُنشِئَت الحاويتانِ المعزولتانِ على هذه العقدةِ نفسِها
    (`council_r4/reviewer_a_repo` و`reviewer_b_repo` ببيئتَينِ منفصلتَينِ) وكُتِبَ
    تكليفٌ أعمى لكلٍّ منهما، ثمَّ **توقَّفَ المراجعانِ كلاهما لنفادِ رصيدِ النماذجِ**
    قبلَ إنتاجِ أيِّ تقريرٍ (‏مجلَّدا المخرَجِ فارغانِ). فلا `VERIFIED` ولا `REJECTED`
    في هذه الجولةِ، ويبقى البندُ `IN_REVIEW` حتّى تُشغَّلَ الجولةُ ويُجمِعَ
    المراجعانِ — ولا يجوزُ لصاحبِ التغييرِ أن يسدَّ هذا الفراغَ بحكمٍ من نفسِه (§ 4.3).
    **والحاويتانِ زائلتانِ لا محفوظتانِ**: بيئةُ التنفيذِ عارضةٌ ولم تُدفَعا إلى المستودعِ،
    فلا يجوزُ الإحالةُ إليهما دليلًا. **وفي `W-156` تُشغَّلُ الجولةُ الرابعةُ من جديدٍ**
    على عقدةِ `W-156` نفسِها بحاويتَينِ منفصلتَينِ ونسختَينِ مستقلّتَينِ من المستودعِ
    وبيئتَينِ افتراضيّتَينِ، وبتكليفٍ أعمى لكلٍّ منهما: لا يرى أحدُ المراجعَينِ تقريرَ
    الآخرِ ولا حاويتَه ولا شجرةَ عملِ المؤلِّفِ. **وهذا القيدُ لا يُلغي هذه الفقرةَ**:
    الجولةُ الموقوفةُ وقعت وتُقيَّدُ كما وقعت — الخطأُ يُسمّى ولا يُمحى.

  · **تشغيلُ عقدةِ `W-151`** (‏وكانَ يُوصَفُ ههنا «الأحدثَ» كذلك · `D-2` — واللقبُ يُصحَّحُ ولا يُمحى الحكمُ) — `3e9ca82` (‏وهي العقدةُ
    التي رأتها الجولةُ الثانيةُ من المراجعةِ):
    رقمُه **34292383869** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34292383869>
    ⇒ **failure** · مقروءٌ بفحوصِ العقدةِ · **13 خضراءُ و1 حمراءُ و0 متخطّاةٌ**
    (‏14 فحصًا): زالَت حمرةُ «Lint (ruff)» و«Truth Audit» ولم تبقَ وظيفةٌ
    متخطّاةٌ، والحمراءُ الواحدةُ «Cross-System Suites» (‏وظيفةٌ **102282757108**)
    ⇒ `1 failed, 2488 passed, 1 skipped`. وسببُها **واحدٌ مقيسٌ**:
    `RESERVATION_EXPIRED` في سبعةِ بنودٍ (`WI-024` … `WI-030`) بعدَ انقضاءِ
    منتصفِ ليلِ UTC، فأسقطَ `check_work_governance.py --self-check` و
    `tests/governance/test_work_governance_gate.py::test_الاستدعاءُ_الذاتيُّ_يمرُّ_على_المستودع`.
    **وهذا العَطبُ أسقطَه المراجعانِ معًا `P1`** وعولِجَ في `W-152` بتجديدِ
    الحجزِ بنصِّ § 6.3 مع تسميةِ السببِ لا طيِّه.
    وعلى العقدةِ نفسِها سيرُ عملٍ ثانٍ **أخضرُ**: «مصفوفةُ الحقيقةِ المولَّدة»
    رقمُه **34292383841** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34292383841>.

  · **التشغيلُ الأسبقُ** — `377c6ad` (‏`W-150`):
    رقمُه **34272407985** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34272407985>
    ⇒ **failure** · مقروءٌ بفحوصِ العقدةِ (‏`commits/377c6ad/check-runs`) ·
    **10 خضراءُ و2 حمراءُ و2 متخطّاةٌ** (‏14 فحصًا).
    **وتصحيحٌ مقيسٌ لا يُطوى** (‏أسقطَه المراجعُ ب `P2` في الجولةِ الثانيةِ):
    قُيِّدَ ههنا أوّلًا «**11** خضراءُ و2 حمراءُ و2 متخطّاةٌ»، وذاك خطأُ عدٍّ —
    مجموعُه 15 لا 14، والمقيسُ بإعادةِ القراءةِ **10 خضراءُ**. فالخطأُ يُسمّى
    ويُصحَّحُ ولا يُمحى.
    (أ) «Lint (ruff)» ⇒ **failure**: مخالفتا `F401` في
    `tests/governance/test_w150_gate_enforcement_in_ci.py` — `subprocess`
    و`sys` مستورَدانِ بلا استعمالٍ. والحارسُ الذي نزلَ في `W-150` ليمنعَ
    **دعوى بلا قياسٍ** دُفِعَ نفسُه بلا تشغيلِ `ruff check .` عليه.
    (ب) «Truth Audit (E0 — Ratchet Gate)» ⇒ **failure**: لا في الراتشيت
    (‏ثابتٌ عندَ 63) بل في `measurement_provenance.py --check`:
    `docs/audit/measurements/final_audit_p14.json` متقادمٌ في حقلَينِ —
    `questions_count` منشورٌ **43** والمقيسُ **44** — لأنَّ `Q-44` سُجِّلَ
    في `W-150` ولم يُعَدْ توليدُ القياسِ المربوطِ بعددِ الأسئلةِ السياديّةِ.
    (ج) «Tests» و«Cross-System Suites» ⇒ **skipped** لا خضراءَ: تعتمدانِ
    على `lint`، فحمرةٌ واحدةٌ حجبَت مجموعتَي اختباراتٍ عن القياسِ أصلًا.
    وعلى العقدةِ نفسِها سيرُ عملٍ ثانٍ **أخضرُ**: «مصفوفةُ الحقيقةِ المولَّدة»
    رقمُه **34272408038** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34272408038>.
    وعولِجَ السببانِ في `W-151`.
    **وتصحيحُ حدٍّ أُعلِنَ أوسعَ مِمّا قِيسَ** (‏أسقطَه المراجعُ ب): قِيلَ ههنا إنَّ
    مسلكَ `actions/runs/<id>/jobs` «يُرجِعُ 404»، والصوابُ أنَّه أرجعَ `404`
    **من حاويةِ المؤلِّفِ فقط**؛ وقد قرأَه المراجعُ ب من حاويتِه بنجاحٍ
    وأعطى تفصيلَ الوظائفِ. فالحدُّ حدُّ بيئةٍ لا حدُّ مسلكٍ.

  · **التشغيلُ الأسبقُ** — `a995b00` (‏`W-149`):
    رقمُه **34178124272** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34178124272>
    ⇒ **failure** · مقروءٌ (13 وظيفةً بخطواتٍ) · **10 خضراءُ و3 حمراءُ**:
    «Work Governance» · «Identity Law» · «Cross-System Suites».
    وسجلُّ الوظائفِ الثلاثِ قُرِئَ فأعطى **سببًا جذريًّا واحدًا لا ثلاثةً**:
    `tests/governance/test_w057_state_document_drift.py` يسقطُ باختبارَيه
    (`:431` و`:590`) بنصٍّ واحدٍ: «`PROJECT_STATE.md:24` … يقولُ `W-146`
    وأحدثُ قيدٍ في § 8 `W-149` — **3 قيدًا** تأخُّرًا»، ومثلُها
    `docs/PROJECT_HANDBOOK.md:12`.
    وعلى العقدةِ نفسِها سيرُ عملٍ ثانٍ **أخضرُ**: «مصفوفةُ الحقيقةِ المولَّدة»
    رقمُه **34178124268** · رابطُه
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34178124268>.

  · **وتصحيحُ قيدٍ سابقٍ لا يُطوى** (‏أسقطَه Grok 4.6 عيبًا `P2`):
    التشغيلُ **34175576534** ·
    <https://github.com/vooovg-ui/AMOS-Fedration/actions/runs/34175576534>
    على رأسِ `6785bf1` قُيِّدَ ههنا بأنَّ رأسَ سجلِّ الإكمالِ عندَه **`W-148`**،
    و**هذا خطأٌ**: أعلى صفٍّ في § 8 عندَ تلك العقدةِ **`W-147`**، ولا صفَّ
    `W-148` في السجلِّ أصلًا — `W-148` **رقمُ التزامٍ بلا قيدٍ في § 8**.
    فالانحرافُ يومَها كان `W-146` مقابلَ `W-147` (قيدٌ واحدٌ)، لا مقابلَ `W-148`.

  · **ودعوى «خارجَ نطاقِ WI-051» سُحِبَت** (‏أسقطَها المراجعانِ معًا `P1`):
    الانحرافُ **صنيعُ هذا البندِ نفسِه** — قيداهُ `W-147` و`W-149` رفعا الرأسَ
    من `W-146` إلى `W-149`، ومزامنةُ سطرِ الحالةِ **واجبُ § 7** جرى عليه العملُ
    في `W-140` و`W-141` و`W-146`. وقد كان الحاجزُ الحقيقيُّ قفلَ `WI-023`،
    وقد فُضَّ بقرارِ المالكِ **`Q-44`** (قسمةُ بندٍ · § 6.1)، فصارَ الإصلاحُ
    داخلَ النطاقِ ومُنجَزًا في `W-150`.
العائق: — (‏فُضَّ). كان قفلُ `WI-023` على `ci.yml` ووثيقتَي الحالةِ يمنعُ إصلاحَ السببِ الجذريِّ لحمرةِ CI وإنفاذَ `A-3`؛ وفَضَّه المالكُ بـ`Q-44`.
الخطوة التالية: — (‏أُغلِقَ البندُ بـ`W-158`). ولا عملَ باقيًا فيه: قرارُ `Q-43` مُسجَّلٌ `DECIDED` ومُنزَلٌ في `A-2` و`OWNERSHIP.md`، و`RK-020` و`DISC-027` مُغلَقانِ، **ومجلسُ المراجعةِ المستقلِّ صارَ مُجرَّبًا أربعَ جولاتٍ لا مُدَّعًى**: رُفِضَ بإجماعٍ مرّتَينِ، وانقسمَ مرّةً، وأجمعَ `VERIFIED` في الرابعةِ. **وما بقيَ من عيوبِ `P2`/`P3` صُحِّحَ في `W-157` وسُمِّيَ ولم يُمحَ.**
قيد السجل: — (يكتتب عند الاغلاق)
```

### WI-052 — واجبُ § 7/6 يُؤدَّى على عقدةِ الإغلاقِ، والجولةُ الخامسةُ من مجلسِ المراجعةِ تُشغَّلُ على البنودِ الحاجبةِ

```text
النطاق: audit-truth (‏docs/audit — والسجلُّ رأسُ المُمَسِّ)
المسار/المرحلة: T0 (قابليّةُ القياسِ — حكمُ CI يُقرأُ ويُقيَّدُ · والمراجعةُ تُشغَّلُ)
المالك: Perplexity Computer            المراجع: مجلس المراجعة (GPT 5.6 + Grok 4.6)
الحالة: IN_PROGRESS   (‏`READY → RESERVED → IN_PROGRESS` · § 4.3 — سُجِّلَ ثمَّ حُجِزَ ثمَّ بُدِئَ
  في الالتزامِ نفسِه الذي يحملُ قيدَه `W-159`، ولا حالةَ قُفِزَ فوقَها)
المسارات:
  docs/audit/COMPLETION_LEDGER.md            (معفيةٌ من الحجزِ بنصِّ § 6)
  docs/governance/work/ACTIVE_WORK.md        (معفيةٌ من الحجزِ بنصِّ § 6)
وتُمَسُّ وثيقتا الحالةِ بسطرِ قيدٍ **وحدَه** — وهو معفًى بنصِّ § 6، فلا يُدَّعى مسارًا
  ولا يُكتَبُ في خليّةِ «المسارات» (سابقةُ `WI-049` المقيسةُ):
  PROJECT_STATE.md          — سطرُ «تاريخ آخر تعديل» + صفُّ `Last Completed Work` المُضافُ
  docs/PROJECT_HANDBOOK.md  — سطرُ «تاريخ آخر تعديل» وحدَه
  وحدُّ ذلكَ مُعلَنٌ: `docs/PROJECT_HANDBOOK.md` **مسارٌ مقفولٌ لِـ`WI-023`** (`IN_REVIEW`)،
  ولا يُمَسُّ منه إلّا سطرُ القيدِ المعفيُّ — ولا يُدَّعى ولا يُعدَّلُ متنُه
خارجَ النطاق:
  - لا يُمَسُّ كودٌ تنفيذيٌّ في core/ federal/ states/ agents/ runtime/
  - لا تُمَسُّ أداةٌ في tools/ ولا فحصٌ في tests/ ولا .github/workflows/
  - لا يُعدَّلُ نصٌّ دستوريٌّ ولا مرسومٌ ولا سجلُّ قراراتٍ سياديّةٍ
  - لا يُنقَلُ بندٌ إلى VERIFIED بيدِ المؤلِّفِ (§ 4.3) — النقلُ فعلُ المجلسِ
  - لا يُصلَحُ عيبٌ يُسقِطُه المجلسُ في هذا البندِ نفسِه: يُقيَّدُ أوّلًا ثمَّ يُعالَجُ
    في بندٍ أو قيدٍ لاحقٍ بحسبِ مسارِه ومالكِه
  - لا تُجدَّدُ حجوزٌ ولا تُغيَّرُ تواريخُ بنودٍ أخرى ههنا
فحصُ التداخلِ (§ 6.2) — نتيجتُه: لا تداخلَ
  - المساراتُ الأربعةُ المُعلَنةُ كلُّها **معفاةٌ من الحجزِ** بنصِّ § 6، فلا CLAIM_CONFLICT
  - ولا يُمَسُّ مسارٌ مقفولٌ لبندٍ IN_REVIEW أو IN_PROGRESS: الأدواتُ والاختباراتُ
    المذكورةُ في البنودِ الستّةِ **تُقرَأُ ولا تُكتَبُ** — والمراجعُ حاكمٌ لا عاملٌ
  - و`WI-039` (IN_PROGRESS) يقفلُ open_record_accountability.py ولا يُمَسُّ ههنا
معيارُ القبول:
  1. حكمُ CI على عقدةِ `W-158` (`97e9acd`) مقروءٌ بالعدِّ الثلاثيِّ (‏خضراءُ · حمراءُ ·
     متخطّاةٌ) ومُقيَّدٌ في § 8 برقمِ تشغيلِه ورابطِه و`run_attempt` — واجبُ § 7/6
  2. القراءةُ جرَت بأداةِ المستودعِ `ci_verdict_readability.py` لا بعينٍ، وحدُّ
     الأداةِ مُعلَنٌ إن رفضَت القياسَ الحيَّ
  3. الجولةُ الخامسةُ من المراجعةِ شُغِّلَت في **حاويتَينِ منفصلتَينِ** لكلٍّ نسخةُ
     مستودعٍ مستقلّةٌ وبيئةٌ افتراضيّةٌ خاصّةٌ وتكليفٌ أعمى مكتوبٌ
  4. كلُّ مراجعٍ أعادَ تشغيلَ الدليلِ بنفسِه وقرأَ حكمَ CI بنفسِه، ولم ينقلْه عن وثيقةٍ
  5. حكمُ المجلسِ على كلِّ بندٍ من الستّةِ مُقيَّدٌ **كما وردَ** — رفضًا كانَ أو قبولًا —
     بعددِ عيوبِ `P1`/`P2`/`P3`، ولا يُطوى خلافٌ ولا يُجمَعُ حكمٌ جمعًا حسابيًّا
  6. لا بندَ يُنقَلُ إلى `VERIFIED` إلّا بإجماعِ المراجعَينِ عليه **بحالِه** (`Q-43`)
  7. البوّاباتُ التسعُ تخرجُ بـ0 قبلَ الدفعِ، والراتشيتُ ثابتٌ عندَ 63
  8. `state_document_drift.py` يخرجُ بـ0 (‏وثائقُ الحالةِ تُزامِلُ رأسَ السجلِّ)
  9. حكمُ CI على عقدةِ كلِّ قيدٍ من قيودِ هذا البندِ يُقرأُ بعدَ الدفعِ ويُقيَّدُ
     (‏حدُّ التسلسلِ `DISC-060`) قبلَ أيِّ نقلِ حالةٍ
الدليلُ المطلوب:
  gh api repos/vooovg-ui/AMOS-Fedration/commits/<sha>/check-runs
  gh api "repos/vooovg-ui/AMOS-Fedration/actions/runs?head_sha=<sha>"
  python tools/governance/ci_verdict_readability.py --from-json <jobs_payload.json>
  python tools/governance/check_work_governance.py --self-check
  python tools/governance/check_work_governance.py --staged
  python tools/governance/check_completion_ledger.py --staged
  python tools/governance/check_repository_identity.py .
  python tools/governance/state_document_drift.py
  python tools/governance/open_record_accountability.py
  python tools/governance/measurement_provenance.py . --check --without-deps
  python tools/governance/truth_limit_integrity.py --check
  python tools/governance/truth_audit.py . --ratchet
  ruff check .                                   (‏بـruff 0.6.9 إصدارِ CI)
  python -m pytest tests/governance -q
بدأ: 2026-09-13        ينتهي الحجز: 2026-09-30
العائق: لا عائقَ فنيًّا على هذا البندِ نفسِه. والعائقُ الذي أنشأَه مقيسٌ: عشرونَ بندًا
  حالتُها IN_REVIEW تقفلُ مساراتِها بنصِّ § 6.1، وخمسةُ بنودِ READY (WI-040 · WI-041 ·
  WI-042 · WI-044 · WI-048) كلٌّ منها يُعلِنُ في حقلِ «العائق» أنَّ مسارَه مُدَّعًى
  لبندٍ IN_REVIEW — فلا يُفتَحُ عملٌ تنفيذيٌّ في تلكَ الأدواتِ قبلَ مراجعةٍ
الخطوةُ التالية: قراءةُ حكمِ CI على عقدةِ قيدِ `W-161` بالعدِّ الثلاثيِّ وبساعةِ
  قراءتِه، ثمَّ نقلُ البندِ IN_PROGRESS → IN_REVIEW في قيدٍ لاحقٍ (معيارُ 9 · DISC-060)
ما اكتُشِفَ أثناءَ التنفيذِ — مُقيَّدٌ لا مطويٌّ (§ 5.2):
  حكمُ CI على عقدةِ قيدِ `W-159` سقطَ في وظيفةِ «Work Governance» وحدَها بستِّ
  مخالفاتِ `DUE_DATE_PASSED`، والسببُ **ليسَ عملَ هذا البندِ**: شُغِّلَت الأداةُ على
  عينِ عقدةِ `97e9acd` فأعطَت المخالفاتِ عينَها — فالحكمُ دالّةٌ في الزمنِ لا في
  الشجرةِ وحدَها. فقُيِّدَ `DISC-062` (`P1`) ووُجِّهَ إلى `tooling-gates`، وجُدِّدَت
  الاستحقاقاتُ الستُّ إلى 2026-09-30 بسببٍ مكتوبٍ في صفِّ كلٍّ منها بلا محوِ الأوّلِ.
  ومسَّ ذلكَ `docs/governance/work/DISCOVERIES.md` — **وهي معفاةٌ من الحجزِ بنصِّ § 6**
  فلا تُدَّعى مسارًا، ومسارُ الأداةِ `open_record_accountability.py` **مقفولٌ لِـ`WI-039`**
  فلم يُمَسَّ: قُيِّدَ العَطبُ ووُجِّهَ ولم يُنقَلْ إلى مكانٍ آخرَ. وقيدُه `W-160`.

حدُّ البندِ — مُعلَنٌ لا مطويٌّ:
  - **حكمُ CI يتقادَمُ** (`DISC-062`): كلُّ دعوى خُضرةٍ في هذا البندِ تُقرأُ بتاريخِ
    قراءتِها لا بصفةٍ دائمةٍ للعقدةِ
  - **خُضرةُ CI شرطٌ لا مراجعةٌ**: قراءةُ الحكمِ لا تمنحُ بندًا حالةً ولا تُرقِّيه
  - **العزلُ عزلُ مسارٍ وبيئةٍ ومعرفةٍ لا عزلُ نواةٍ** — قائمةُ العمليّاتِ مشتركةٌ،
    وهذا حدُّ بنيةٍ يُسمّى كما سُمِّيَ في W-157، ومن أرادَ تشديدَه فبقرارٍ لا بدعوى
  - **تقاريرُ المراجعَينِ لا تُدفَعُ إلى الشجرةِ**: بيئةُ التنفيذِ عارضةٌ، والمُقيَّدُ
    في السجلِّ حكمُها وعددُ عيوبِها وأدلّتُها وإقرارُ استقلالِها — وهي سنَّةُ الجولاتِ
    الأربعِ السابقةِ نفسُها ولا يُدَّعى غيرُها
  - **ستّةٌ لا عشرونَ**: البنودُ الأربعةَ عشرَ الأخرى الباقيةُ IN_REVIEW لا يُسحَبُ
    عليها حكمُ هذه الجولةِ، وكلُّ بندٍ يُراجَعُ بحالِه
  - **ولا يُقرَأُ عددُ الجولاتِ حُجّةً**: أربعُ جولاتٍ سابقةٍ على WI-051 وحدَه، ولا
    تُنقَلُ ثقتُها إلى بنودٍ لم تُراجَعْ
قيدُ السجلّ: W-159 (‏قيدُ أداءِ واجبِ § 7/6 وتسجيلِ البندِ) — وقيدُ الإغلاقِ يُكتَبُ عندَ الإغلاقِ
ما اكتُشِفَ في الجولةِ الخامسةِ — مُقيَّدٌ كما وردَ (قيدُه `W-161`):
  الدمجُ إلى main تمَّ تقديمًا سريعًا 97e9acd..b951dca، وأُعيدَت قراءةُ حكمِ CI على
  العقدةِ المدموجةِ نفسِها (واجبُ § 7/6): تشغيلُ 34784013601 (رقمُ 26 · محاولةُ 1 ·
  push) ⇒ success · 13 خضراءَ · 0 حمراءَ · 0 متخطًّى، ومصفوفةُ الحقيقةِ 34784013651
  ⇒ success · 1 خضراءُ — وساعةُ القراءةِ 2026-09-13T22:24:12Z (DISC-062).
  ثمَّ شُغِّلَت الجولةُ في حاويتَينِ منفصلتَينِ: المراجعُ أ ردَّ أربعةً وقبِلَ WI-035
  وWI-037 (جملةُ P1 إحدى عشرةَ)، والمراجعُ ب ردَّ الستَّةَ (سبعةُ عيوبٍ مميَّزةٍ).
  فبقاعدةِ Q-43: صفرُ بندٍ مُجمَعٌ عليه ⇒ **صفرُ VERIFIED**، والانقسامُ لا يُجمَعُ
  جمعًا حسابيًّا. ونُقِلَت الستّةُ IN_REVIEW → IN_PROGRESS (§ 4.3)، وقُيِّدَ DISC-063
  باتّحادِ العيوبِ وDISC-064 بهُويّةِ الأثرِ المولَّدِ المقروءةِ من origin.
  **ولم يُصلَحْ عيبٌ ههنا** (§ 5.2): وجهةُ كلِّ طبقةٍ مكتوبةٌ في DISC-063.

```
