# ملحقُ تصميمِ الدفعةِ F1 — أسطحُ `governance/federation.py` تعبرُ الحدَّ بفاعلٍ تنفيذيٍّ مُعلَنٍ بالفعلِ `coordinate`

## التعريف
ملحقُ تصميمٍ قصيرٌ للدفعةِ **F1** (بندُ `WI-106`) يُودَعُ **في التزامٍ مستقلٍّ يسبقُ أيَّ شِفرةٍ** (قرارُ المالكِ Q-61 للبنودِ القادمةِ · توجيهُ المستشارِ 19 § 2). يحدِّدُ نقاطَ التصميمِ D1–D8 والأرقامَ المتوقَّعةَ قبلَ الكتابةِ والفحوصَ والطفراتِ، على نمطِ J1 ([`J1_ISSUE_RULING_DESIGN.md`](J1_ISSUE_RULING_DESIGN.md)).

## النطاق
`federal/executive/services/src/amos_federation/services/governance/federation.py` وحدَه في الإنتاجِ · وملفُّ الفحوصِ `federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py`. لا يمسُّ `core/` ولا الجسرَ ولا `royal/` (K1 لا يُمَسُّ).

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — بندُ `WI-106`.

## تاريخ الإنشاء
2026-10-22

## تاريخ آخر تعديل
2026-10-22

---

## 0. السندُ (لا اختراعَ)

- **D17-1** (نصُّ المالكِ · السجلُّ السياديُّ): «خيار (1): فاعل تنفيذي معلن للوحدة بالفعل coordinate (نص Q-24 نفسه) → يفتح دفعة F1.»
- **Q-24** (نصُّه): الوحدةُ «تنسيق لا سلطة» — فالفرعُ التشريعيُّ والقضائيُّ في هذه الوحدةِ **سجلّاتُ تنسيقٍ** لا سلطةٌ تشريعيّةٌ ولا قضائيّةٌ حقيقيّةٌ. القضاءُ الحقيقيُّ هو `federal_judiciary` بفاعلِه القضائيِّ (J1). هذا التصميمُ لا يمنحُ `JudicialBranch.rule` ولا `LegislativeBranch.enact` أيَّ سلطةٍ؛ يُخضِعُهما للحدِّ بالفعلِ الذي قرَّرَه المالكُ.
- **قياسُ ما قبلُ** (`evidence/W-615/`): مسبارُ البوابةِ على `coordinate` ⇒ `EXECUTIVE` ALLOW · `LEGISLATIVE`/`JUDICIAL`/`TREASURY` DENY · `AGENT`/`SYSTEM` ALLOW (ثغرةُ Q-68 — خارجَ البندِ).

## 1. الأسطحُ الخمسةَ عشرَ (مقيسةً · `sovereign_write_inventory.py`)

| الصنف | السطح | الأثرُ المُعلَن | الهدفُ (= قيمةُ المفتاحِ) |
|---|---|---|---|
| ApprovalSystem | `request_approval` | CREATE | `federation/approvals/{approval_id}/request` |
| ApprovalSystem | `decide_approval` | UPDATE | `federation/approvals/{approval_id}/decide` |
| PromotionSystem | `start_promotion` | CREATE | `federation/promotions/{promotion_id}/start` |
| PromotionSystem | `pass_gate` | UPDATE | `federation/promotions/{target_type}:{target_id}/{gate}/pass/{nonce}` |
| PromotionSystem | `fail_gate` | UPDATE | `federation/promotions/{target_type}:{target_id}/{gate}/fail/{nonce}` |
| ExecutiveBranch | `appoint` | UPDATE | `federation/executive_roles/{role_name}/appoint/{nonce}` |
| LegislativeBranch | `propose` | CREATE | `federation/legislations/{leg_id}/propose` |
| LegislativeBranch | `open_debate` | UPDATE | `federation/legislations/{id}/debate/{nonce}` |
| LegislativeBranch | `open_voting` | UPDATE | `federation/legislations/{id}/voting/{nonce}` |
| LegislativeBranch | `vote` | UPDATE | `federation/legislations/{id}/votes/{agent_id}` |
| LegislativeBranch | `enact` | UPDATE | `federation/legislations/{id}/enact` |
| JudicialBranch | `file_case` | CREATE | `federation/court_cases/{case_id}/file` |
| JudicialBranch | `add_argument` | UPDATE | `federation/court_cases/{id}/arguments/{nonce}` |
| JudicialBranch | `rule` | UPDATE | `federation/court_cases/{id}/ruling/{nonce}` |
| SupremeOversight | `generate_compliance_report` | CREATE | `federation/compliance_reports/{report_id}/generate` |

## 2. نقاطُ التصميم

**D1 · الفاعلُ:** ثابتُ وحدةٍ `FEDERATION_ACTOR = "EXECUTIVE"` ومُفوِّضٌ كسولٌ واحدٌ للوحدةِ `_federation_authorizer()` (+ `reset_federation_authorizer()` للفحوصِ) — نمطُ `rulings._judiciary_authorizer` نفسُه (D1 في J1). لا معامَلَ `authorizer` في توقيعاتِ الأسطحِ (لا تغييرَ في واجهتِها).

**D2 · الفعلُ:** `FEDERATION_VERB = "coordinate"` للأسطحِ الخمسةَ عشرَ كلِّها (D17-1 حرفيًّا). اسمُ العمليّةِ يُحمَلُ في `metadata["operation"]` (`"<Class>.<method>"`) وفي نطاقِ المفتاحِ — لا يُخترَعُ فعلٌ لكلِّ سطحٍ (ذلك سؤالُ Q-2 المعلَّقُ).

**D3 · الهدفُ والمفتاحُ:** الهدفُ بالجدولِ أعلاه، والمفتاحُ `operation_key("federation.<op>", <لاحقةِ الهدفِ>)` — الهويّةُ نفسُها في الاثنينِ (نمطُ J1 D5/D6). السببُ مقيسٌ في J1: بصمةُ العقدِ تُشتقُّ من (الفاعلِ · الفعلِ · الهدفِ · الآثارِ)، ومعرِّفُ الإذنِ `EP-<العقد>-<الثانية>` يرفضُ عقدًا مكرَّرًا في الثانيةِ نفسِها — فالعمليّاتُ المشروعُ تكرارُها على الكيانِ نفسِه (حجّتانِ في قضيّةٍ · فتحُ مناقشةٍ ثانٍ) تحملُ في هدفِها **مُعرِّفَ استدعاءٍ** (`nonce = uuid4().hex`) وإلّا رُفِضَ الاستدعاءُ الثاني المشروعُ.

**D4 · موضعُ العبورِ:** في **جسدِ كلِّ سطحٍ عامٍّ** (`guard_declared(` نصًّا فيه — قاعدةُ الجردِ)، والكتابةُ كلُّها في **مُطبِّقٍ متداخلٍ خاصٍّ** `_apply` يفتحُ الجلسةَ ويكتبُ ويلتزمُ (نمطُ `agent_identity._apply` في WI-082 و`rulings._apply` في J1). لا كتابةَ خارجَ المُطبِّقِ في أيِّ سطحٍ.

**D5 · التحقُّقُ قبلَ العبورِ:** فحوصُ المُدخَلِ والحالةِ القائمةُ اليومَ (مثلًا «الوكيل صوّت بالفعل» · «الموافقة تم البت فيها» · «بوابة سابقة لم تُجتز») تُنفَّذُ **قبلَ العبورِ** بجلسةِ قراءةٍ ولا تتغيّرُ رسائلُها ولا أنواعُها (`ValueError`) — فلا يتحوّلُ رفضُ مُدخَلٍ إلى `CompensationRequired` ولا يُسجَّلُ في الذرّيّةِ عمليّةً فاشلةً. ويُعيدُ المُطبِّقُ تحميلَ الصفِّ داخلَ معاملتِه.

**D6 · الإعادةُ:** المفتاحُ طبيعيٌّ حيثُ لا يتكرّرُ الفعلُ في المجالِ: الإنشاءُ بمعرِّفٍ جديدٍ · `decide_approval` (يُبَتُّ مرّةً) · `vote` (صوتٌ لكلِّ وكيلٍ) · `enact` (إقرارٌ مرّةً). وحيثُ يُشرَعُ التكرارُ فالمفتاحُ يحملُ مُعرِّفَ الاستدعاءِ (D3) — **فلا يتغيّرُ سلوكُ اليومِ**. وإن عادَ مفتاحٌ طبيعيٌّ ناجحٌ (`is_replay`) رُفِعَ `FederationReplayError` صريحًا بلا كتابةٍ ثانيةٍ (والمقيسُ: `decide_approval`/`vote` يرفضُهما D5 قبلَ ذلك؛ و`enact` الثاني هو الحالةُ الوحيدةُ التي تبلغُ الإعادةَ — **تغييرُ سلوكٍ مُعلَنٌ**: كانَ يُعيدُ الإقرارَ صامتًا).

**D7 · المُعوِّضُ (نمطُ J1 D7-أ):** استعادةٌ تقنيّةٌ دقيقةٌ في جلسةٍ جديدةٍ عبرَ سجلِّ تراجعٍ لكلِّ عبورٍ `_FederationUndo`: المُطبِّقُ يُسجِّلُ قبلَ الكتابةِ (أ) كلَّ صفٍّ أنشأَه (`created(model, pk)`) و(ب) القيمَ السابقةَ لكلِّ عمودٍ يغيّرُه (`prior(row, *columns)` بنسخةٍ عميقةٍ للأعمدةِ JSON). ومُعوِّضُ الأثرِ يحذفُ المُنشَأَ ويُعيدُ السابقَ ويلتزمُ. الحدُّ يُنادي المُعوِّضَ آليًّا عندَ فشلِ تثبيتِ النجاحِ بعدَ الالتزامِ (قرارُ المالكِ Q-70 · W-603) — «الحذفُ شأنٌ تنفيذيٌّ» والمُعوِّضُ ليس أثرًا مُعلَنًا.

**D8 · ما يبقى خارجَ العبورِ (مُعلَنٌ لا مسكوتٌ عنه):** (أ) نشرُ ناقلِ الأحداثِ بعدَ الالتزامِ كما هو اليومَ — أثرٌ للبنيةِ التحتيّةِ، سؤالُ A1 · (ب) `ExecutiveBranch._init_roles` — بذرُ الأدوارِ الشاغرةِ في المُنشئِ، معاونٌ خاصٌّ لا تصلُه عمليّةٌ عامّةٌ، فلا يُحصى دَينًا (قاعدةُ الجردِ) ويبقى كتابةً بلا عبورٍ تُعلَنُ هنا · (ج) `PolicyEngine.add_rule` في `enact` يكتبُ في ذاكرةِ نسخةٍ جديدةٍ لا تخزينَ (مقيسٌ: `self._rules` قاموسٌ) — يبقى داخلَ المُطبِّقِ كما هو · (د) `Ed25519Signer` (Q-37) لا يُمَسُّ.

## 3. الأرقامُ المتوقَّعةُ (مكتوبةٌ قبلَ الشِّفرةِ · بالأداةِ نفسِها)

- **الدَّينُ (D-4):** 181 ← **166** (الخمسةَ عشرَ تعبرُ).
- **السياديُّ:** 18 ← **33**.
- **الأسطحُ:** 220 ← **236** متوقَّعًا — كلُّ مُطبِّقٍ متداخلٍ خاصٍّ يُحصى موضعًا مستقلًّا (سابقةُ DISC-126 في J1/WI-082) فيزيدُ 15، ومُعوِّضُ `_FederationUndo._restore` موضعٌ خاصٌّ واحدٌ. ليست دَينًا (الدَّينُ عامٌّ غيرُ عابرٍ وحدَه). **إن خالفَ المقيسُ هذا الرقمَ أُعلِنَ الفرقُ بسببِه ولا يُعدَّلُ المتوقَّعُ بأثرٍ رجعيٍّ.**
- **بلا نموٍّ في غيرِ الوحدةِ:** دَينُ كلِّ ملفٍّ آخرَ كما هو.

## 4. الفحوصُ (`test_wi106_federation_coordinate_sovereign.py`)

- **T1 · العبورُ:** مُصرِّحٌ مُسجِّلٌ بالثابتِ نفسِه؛ استدعاءُ الأسطحِ الخمسةَ عشرَ كلِّها ⇒ 15 عمليّةً متمايزةً في `metadata["operation"]`، الفعلُ `coordinate` في كلِّها، والقرارُ ALLOW.
- **T2 · الفاعلُ مُعلَنٌ لا مُثبَّتٌ:** تبديلُ `FEDERATION_ACTOR` إلى `JUDICIAL` ⇒ `propose` و`request_approval` يُرفَضانِ في البوابةِ ولا صفَّ يُكتَبُ.
- **T3 · لا كتابةَ خارجَ المُطبِّقِ:** مُصرِّحٌ يرفضُ قبلَ المُطبِّقِ ⇒ لكلِّ سطحٍ: الصفوفُ والأعمدةُ كما كانت.
- **T4 · المُعوِّضُ على الإنشاءِ (`propose`):** إسقاطُ تثبيتِ النجاحِ ⇒ `CompensationRequired` · `state_is_clean` · الصفُّ غائبٌ · الذرّيّةُ `FAILED_RETRYABLE` · والإعادةُ (الثانيةُ التاليةُ) تنجح.
- **T5 · المُعوِّضُ على التحديثِ (`vote`):** الإسقاطُ نفسُه ⇒ العدّادُ والمصوِّتونَ يعودانِ إلى ما قبلُ.
- **T6 · الإعادةُ الطبيعيّةُ (`enact`):** الإقرارُ الثاني ⇒ `FederationReplayError` ولا كتابةَ ثانيةً.
- **T7 · الجردُ:** الأداةُ على الوحدةِ ⇒ 15 عامًّا كلُّها عابرةٌ (0 دَينٌ).
- **T8 · ثوابتُ D1/D2:** الفاعلُ الافتراضيُّ `EXECUTIVE` والفعلُ `coordinate`.
- **بلا تعديلٍ:** `test_federation.py` كاملًا.

## 5. الطفراتُ (كلٌّ يجبُ أن يُسقِطَ فحصَه)

- **M1:** `propose` يُنادي `_apply` مباشرةً بلا عبورٍ ⇒ يسقطُ T1 وT3.
- **M2:** `FEDERATION_ACTOR = "JUDICIAL"` ⇒ يسقطُ T1 وT8.
- **M3:** مُعوِّضُ `_restore` لا يفعلُ شيئًا ⇒ يسقطُ T4 وT5.
- **M4:** حذفُ `undo.prior(...)` من `vote` ⇒ يسقطُ T5.
- **M5:** مفتاحُ `enact` يحملُ مُعرِّفَ استدعاءٍ ⇒ يسقطُ T6.

## 6. ما لا يُنجَزُ في F1 ولماذا

R1 (السجلُّ الوطنيُّ) دفعةٌ تاليةٌ بندًا مستقلًّا (ملفّاتُه منفصلةٌ — ولا يُجمَعُ معَ F1 كي تبقى جولةُ المجلسِ على دفعةٍ واحدةٍ مقروءةٍ). وJ2/J3 بأفعالِ D17-2 المعتمدةِ بعدَها.
