# جدولُ معجمِ Q-83 (ج) المقترح — الأسطحُ الأربعةُ والعشرون (وثيقةُ تصميمٍ فقط · بلا شِفرة)

## الهدف
عرضُ فعلٍ دستوريٍّ مقترحٍ لكلِّ سطحٍ من الأسطحِ الأربعةِ والعشرين المحجوبةِ بقرارِ Q-83 (ج)، ومعه الفاعلُ والآثارُ والمعوِّضُ ومسبارُ المحرّكِ مقيسًا قبلَ الاقتراح — بنصِّ قرارِ المالكِ Q-96 القرار 6: «يُؤذَن بإعداد جدول معجم مقترح (وثيقة تصميم فقط: لكل سطح من الأربعة والعشرين الفعل المقترح والفاعل والآثار والمعوِّض ومسبار المحرك). يُعرَض عليّ وعلى المالك فيُقَرّ أو يُعدَّل قبل أي شفرة. لا يخترع المنفِّذ أفعالًا خارج هذا الجدول.»

## النطاق
عرضٌ لا قرار. لا يُضافُ فعلٌ إلى `core/constitutional_engine/rules.py` ولا مدخلٌ إلى `MONEY_OPERATION_LEXICON` ولا `guard_declared` إلى سطحٍ قبلَ أن يُقِرَّ المستشارُ والمالكُ هذا الجدولَ أو يُعدِّلاه بنصٍّ مؤرَّخٍ يُقيَّدُ في `SOVEREIGN_DECISION_REGISTER.md`. وبعدَ الإقرار: شِفرةٌ في دفعاتٍ صغيرة، لكلٍّ مسبارُ محرّكٍ وطفرات (التوجيهُ 41 § 2 بند 4). وإضافةُ فعلٍ إلى حصرِ فرعٍ في `rules.py` مسٌّ لـ`core/` يحتاجُ قرارَه المستقلَّ — K1 لا يُمَسّ.

## المالك
قيدُ W-816 · WI-122 · Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5). والإقرارُ للمستشارِ والمالك.

## تاريخ الإنشاء
2026-11-04

## تاريخ آخر تعديل
2026-11-04 (W-819 — § 7 تصميمُ الدفعةِ 2 بقرارِ Q-98 · قبلَ الشِّفرة) · 2026-11-04 (W-817 — § 6 تصميمُ الدفعةِ 1 بقرارِ Q-97 · قبلَ الشِّفرة) · 2026-11-04 (W-816 — النسخةُ الأولى)

---

## 1 · مصدرُ القائمةِ وطريقةُ القياس

- **الأسطحُ الأربعةُ والعشرون** من `docs/audit/evidence/W-813/d4_classification.txt`: الصنفُ [20] «Q-83 (ج) — معجمُ الأسطحِ العشرين» (‏`federal_state` ‏8 + ‏`national_economy` ‏12) · الصنفُ [3] «Q-83 (أ)① + (ج) — مركَّبُ النواة» · الصنفُ [1] «مشتقُّ مالٍ» (`ModelLayer.log_cost`). والمجموعُ 24 من الـ77.
- **الآثار** قراءةٌ ساكنة: `evidence/W-816/surface_effects_scan.py` ⇒ `surface_effects_scan_output.txt` (‏SCANNED=24 · لكلِّ سطحٍ عمليّةُ نطاقِه والنموذجُ المُنشأُ والمقروء).
- **مسبارُ المحرّك**: `evidence/W-816/lexicon_engine_probe.py` ⇒ `lexicon_engine_probe_output.txt`. يُنادي `ConstitutionalEngine.evaluate` (النواةُ الحقيقيّة · سجلٌّ مؤقّت) لكلِّ مرشَّحٍ (38 فعلًا: المقترحُ والقائمُ القريبُ منه) ولكلِّ فاعلٍ من العشرة، في وضعين: «الآن» (المعجمُ كما هو) و«مقترح» (ترقيعٌ في الذاكرةِ لـ`rules._BRANCH_EXCLUSIVE` داخلَ التشغيلِ وحدَه — لا يُكتَبُ في `core/`). النتيجة: `surfaces=24 candidates=38 actor_denied=0` · وتصادمُ الأفعالِ الجديدةِ مع المجموعاتِ القائمة = `[]` (الحصرُ الفرعيّ · الحسّاسُ بشريًّا · الذاكرة · الحوكمةُ الذاتيّة · مفتاحُ الإيقاف).

## 2 · ثلاثُ حقائقَ مقيسةٍ تحكمُ الجدول

1. **الفعلُ المجهولُ يمرُّ للجميع.** كلُّ فعلٍ جديدٍ في الجدولِ اليومَ: `owner=— allow=10/10` — حتى `HUMAN` و`AGENT`. فاسمُ فعلٍ لا يدخلُ حصرَ فرعٍ ليس حمايةً، والعبورُ به عبورٌ شكليّ. لذلك يقترحُ الجدولُ لكلِّ فعلٍ جديدٍ حصرَه في فرعٍ، وتحتَ «مقترح» صار كلٌّ منها `allow=[فاعلِه وحدَه]`.
2. **الأفعالُ القائمةُ القريبةُ تُغيِّرُ المعنى أو تُحجَب.** `create_state`/`dissolve_state`/`create_institution`/`grant_authority`/`revoke_authority` للتنفيذيّ ⇒ `DENY['R-010-1','R-010-5']` (امتيازٌ ملكيّ) و`create_state` ⇒ ‏+`R-004-1` (75٪ وتوقيعٌ بشريّ) · `assign_case` ⇒ `DENY['R-003-1']` (قضائيّ) · `enact_policy` ⇒ `DENY['R-003-1']` (تشريعيّ) · `create_budget`/`open_account`/`book_expense` ⇒ `DENY['R-003-1']` (خزانة). فإعادةُ استعمالِها إمّا تعطيلٌ للسطحِ أو ادّعاءُ معنًى ليس فيه — وكلاهما «اختراعٌ لإنجاحِ عبور» بنصِّ Q-83 (ج).
3. **ما يحملُ اسمًا قائمًا بمعناه نفسِه يُعادُ ولا يُخترَع.** `authorize_expenditure` و`award_procurement` في `TREASURY_ACTIONS` اليوم (`owner=TREASURY allow=1/10`) ومعناهما معنى سطحَيهما.

## 3 · الجدول

القاعدةُ في التسمية: الفعلُ الجديدُ **اسمُ السطحِ نفسُه** — لا اسمَ مُبتدَعًا خارجَ الشِّفرة — إلا حيث فعلٌ قائمٌ بمعناه. والفاعلُ **التنفيذيُّ** افتراضُ `ConstitutionalAuthorizer()` القائم (`sovereignty_bridge.py`) فلا فاعلَ جديد، و**الخزانةُ** حيث التفويضُ الماليُّ بسندِ Q-19. والمعوِّضُ مُعلَنٌ قبلَ التنفيذ (`compensator(...)` · 1I).

| # | السطح | الفعلُ المقترح | الفاعل | الآثار (عمليّةُ النطاق ⇒ النموذج) | المعوِّض المقترح | مسبارُ المحرّك (الآن ⇒ مقترح · البديلُ المقيس) |
|---|---|---|---|---|---|---|
| 1 | `federal_state.register_government` | `register_government` — جديد ⇒ `EXECUTIVE_ACTIONS` | EXECUTIVE | `federation.government.register` ⇒ CREATE `GovernmentModel` | حذفُ الصفِّ المُنشأ بمعرّفِه | 10/10 ⇒ EXECUTIVE وحدَه · `create_state` ⇒ DENY R-004-1/R-010-1/R-010-5 · `admit_state` ⇒ DENY R-004-1 |
| 2 | `federal_state.set_government_status` | `set_government_status` — جديد ⇒ EXECUTIVE | EXECUTIVE | `federation.government.status` ⇒ WRITE `GovernmentModel.status` | إعادةُ الحالةِ السابقةِ المقروءةِ قبلَ الكتابة | 10/10 ⇒ EXECUTIVE · `dissolve_state` ⇒ DENY R-010-1/R-010-5 |
| 3 | `federal_state.bind_institution` | `bind_institution` — جديد ⇒ EXECUTIVE | EXECUTIVE | `federation.institution.bind` ⇒ CREATE `InstitutionGovernmentModel` | حذفُ الربطِ المُنشأ | 10/10 ⇒ EXECUTIVE · `create_institution` ⇒ DENY R-010-1/R-010-5 |
| 4 | `federal_state.record_relation` | `record_relation` — جديد ⇒ EXECUTIVE | EXECUTIVE | `federation.relation.record` ⇒ CREATE `GovernmentRelationModel` | حذفُ العلاقةِ المُنشأة | 10/10 ⇒ EXECUTIVE · لا بديلَ قائم |
| 5 | `federal_state.grant_delegation` | `grant_delegation` — جديد ⇒ EXECUTIVE | EXECUTIVE | `federation.delegation.grant` ⇒ CREATE `GovernmentDelegationModel` | حذفُ التفويضِ المُنشأ | 10/10 ⇒ EXECUTIVE · `grant_authority` ⇒ DENY R-010-1/R-010-5 |
| 6 | `federal_state.revoke_delegation` | `revoke_delegation` — جديد ⇒ EXECUTIVE | EXECUTIVE | `federation.delegation.revoke` ⇒ WRITE `GovernmentDelegationModel` (يُقرأُ أوّلًا) | إعادةُ الحالةِ المقروءة | 10/10 ⇒ EXECUTIVE · `revoke_authority` ⇒ DENY R-010-1/R-010-5 |
| 7 | `federal_state.scope_service` | `scope_service` — جديد ⇒ EXECUTIVE | EXECUTIVE | `federation.service.scope` ⇒ CREATE `ServiceScopeModel` (يقرأ `GovernmentModel`/`DepartmentModel`) | حذفُ النطاقِ المُنشأ | 10/10 ⇒ EXECUTIVE · `deploy_service` ⇒ ALLOW لكنَّه فعلُ نشرٍ لا نطاق (معنًى آخر) |
| 8 | `federal_state.scope_case` | `scope_case` — جديد ⇒ EXECUTIVE | EXECUTIVE | `federation.case.scope` ⇒ CREATE `CaseScopeModel` (يقرأ `OfficialModel`) | حذفُ النطاقِ المُنشأ | 10/10 ⇒ EXECUTIVE · `assign_case` ⇒ DENY R-003-1 (قضائيّ) |
| 9 | `national_economy.register_sector` | `register_sector` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.sector.register` ⇒ CREATE `EconomicSectorModel` | حذفُ القطاعِ المُنشأ | 10/10 ⇒ EXECUTIVE · لا بديل |
| 10 | `national_economy.register_category` | `register_category` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.category.register` ⇒ CREATE `EconomicCategoryModel` | حذفُ الفئة | 10/10 ⇒ EXECUTIVE · لا بديل |
| 11 | `national_economy.define_indicator` | `define_indicator` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.indicator.define` ⇒ CREATE `EconomicIndicatorDefinitionModel` | حذفُ التعريف | 10/10 ⇒ EXECUTIVE · لا بديل |
| 12 | `national_economy.register_public_entity` | `register_public_entity` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.entity.register` ⇒ CREATE `PublicEconomicEntityModel` + CREATE `EconomicDecisionModel` | حذفُ الكيانِ ثمَّ قرارِه (أثران · معوِّضان) | 10/10 ⇒ EXECUTIVE · `create_institution` ⇒ DENY R-010-1/R-010-5 |
| 13 | `national_economy.create_program` | `create_program` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.program.create` ⇒ CREATE `EconomicProgramModel` + `EconomicDecisionModel` | حذفُ البرنامجِ وقرارِه | 10/10 ⇒ EXECUTIVE · `create_budget` ⇒ DENY R-003-1 (خزانة) |
| 14 | `national_economy.issue_policy` | `issue_policy` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.policy.issue` ⇒ CREATE `EconomicPolicyModel` (مسوَّدة) + `EconomicDecisionModel` | حذفُ المسوَّدةِ وقرارِها | 10/10 ⇒ EXECUTIVE · `enact_policy` ⇒ DENY R-003-1 (تشريعيّ) |
| 15 | `national_economy.register_revenue_source` | `register_revenue_source` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.revenue.register` ⇒ CREATE `RevenueSourceModel` + `EconomicDecisionModel` | حذفُ المصدرِ وقرارِه | 10/10 ⇒ EXECUTIVE · `open_account` ⇒ DENY R-003-1 |
| 16 | `national_economy.register_public_asset` | `register_public_asset` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.asset.register` ⇒ CREATE `PublicAssetModel` + `EconomicDecisionModel` | حذفُ الأصلِ وقرارِه | 10/10 ⇒ EXECUTIVE · `book_expense` ⇒ DENY R-003-1 |
| 17 | `national_economy.register_public_liability` | `register_public_liability` — جديد ⇒ EXECUTIVE | EXECUTIVE | `economy.liability.register` ⇒ CREATE `PublicLiabilityModel` + `EconomicDecisionModel` | حذفُ الالتزامِ وقرارِه | 10/10 ⇒ EXECUTIVE · `book_expense` ⇒ DENY R-003-1 |
| 18 | `national_economy.authorize_expenditure` | `authorize_expenditure` — **قائم** في `TREASURY_ACTIONS` · ومدخلُ `economy.expenditure.authorize` قائمٌ في المعجمِ وفي `money_delegation.py` | TREASURY | `economy.expenditure.authorize` ⇒ CREATE `ExpenditureAuthorizationModel` + `EconomicDecisionModel` | حذفُ الإجازةِ وقرارِها | 1/10 (TREASURY) ⇒ بلا تغيير |
| 19 | `national_economy.authorize_procurement` | `award_procurement` — **قائم** في `TREASURY_ACTIONS` · ويلزمُ مدخلُ معجمٍ `economy.procurement.authorize` ⇒ `award_procurement` ومدخلُ تفويضٍ في `money_delegation.py` (الثاني عشر) | TREASURY | `economy.procurement.authorize` ⇒ CREATE `ProcurementModel` + `EconomicDecisionModel` | حذفُ المشترياتِ وقرارِها | 1/10 (TREASURY) ⇒ بلا تغيير |
| 20 | `national_economy.authorize_transfer` | `authorize_transfer` — جديد ⇒ `TREASURY_ACTIONS` · ومدخلا معجمٍ `economy.transfer.grant`/`economy.transfer.subsidy` ومدخلا تفويض | TREASURY | `economy.transfer.{grant,subsidy}` ⇒ CREATE `EconomicTransferModel` + `EconomicDecisionModel` | حذفُ التحويلِ وقرارِه | 10/10 ⇒ TREASURY وحدَه · `authorize_expenditure` ⇒ ALLOW للخزانة (بديلٌ قائم — انظر § 4 السؤال 3) |
| 21 | `federal_state.execute_scoped_operation` | `execute_scoped_operation` — جديد ⇒ EXECUTIVE · بعدَ عبورِ النواةِ `ExecutiveCore.run` (تسلسلُ Q-83 (أ)①) | EXECUTIVE | `federation.operation.execute` ⇒ CREATE `GovernmentOperationModel` | حذفُ قيدِ العمليّة (ولا يُعوِّضُ ما عبرَ النواة — له عبورُه) | 10/10 ⇒ EXECUTIVE · `execute_task` ⇒ ALLOW لكنَّه فعلُ النواةِ نفسِها (العبورُ الأوّل) |
| 22 | `national_economy.activate_policy` | `activate_policy` — جديد ⇒ EXECUTIVE · بعدَ عبورِ النواة | EXECUTIVE | `economy.policy.activate` ⇒ WRITE `EconomicPolicyModel.status` + CREATE `EconomicDecisionModel` | إعادةُ الحالةِ المقروءةِ وحذفُ القرار | 10/10 ⇒ EXECUTIVE · `enact_policy` ⇒ DENY R-003-1 |
| 23 | `national_economy.execute_economic_decision` | `execute_economic_decision` — جديد ⇒ EXECUTIVE · بعدَ عبورِ النواة | EXECUTIVE | `economy.decision.execute` ⇒ WRITE `EconomicDecisionModel.status` | إعادةُ الحالةِ المقروءة | 10/10 ⇒ EXECUTIVE · `execute_task` ⇒ ALLOW (فعلُ النواة) |
| 24 | `model_gateway.log_cost` | `log_cost` — جديد ⇒ `NON_CONSTITUTIONAL_MONEY_ACTIONS` (بسندِ Q-17: وحدةُ تشغيلٍ لا مالٌ دستوريّ) · بعدَ أصلِه `charge_model_invoke` | EXECUTIVE | CREATE `CostLogModel` | حذفُ قيدِ التكلفة | 10/10 ⇒ تسعةٌ ALLOW و`HUMAN` DENY R-003-1 بلا وسمِ موافقة (حكمُ المجموعةِ القائم) · `charge_model_invoke` كذلك |

## 4 · أسئلةٌ للمستشارِ والمالك قبلَ الإقرار

1. **`register_government` (البند 1):** هل تسجيلُ حكومةٍ «إنشاءُ ولايةٍ» بالمعنى الدستوريّ؟ إن كان، فالفعلُ `create_state` وسطحُه يُحجَبُ اليومَ للتنفيذيّ (R-004-1 75٪ وتوقيعٌ بشريّ · R-010 امتيازٌ ملكيّ) — والجدولُ لا يقترحُه لأنّه يُغيِّرُ سلوكَ السطحِ لا يُعبِرُه. وكذا `grant_delegation`/`revoke_delegation` إزاءَ `grant_authority`/`revoke_authority`.
2. **الحصرُ في `EXECUTIVE_ACTIONS`:** إضافةُ عشرينَ فعلًا إلى حصرِ التنفيذيِّ تمسُّ `core/constitutional_engine/rules.py` — والمقترحُ تحتَ «مقترح» مقيسٌ بترقيعٍ في الذاكرةِ لا بملفّ. والبديلُ عن الحصرِ (تركُها مجهولةً للمحرّك) مقيسٌ: 10/10 يمرّ — عبورٌ بلا حماية.
3. **`authorize_transfer` (البند 20):** فعلٌ جديدٌ للخزانةِ في مقابلِ `execute_transfer` القائم (زوجُ «إجازة ⇒ تنفيذ» كـ`authorize_expenditure`/`execute_expenditure`)، أم إعادةُ `authorize_expenditure` لأنَّ التحويلَ يُجازُ على إجازةِ إنفاقٍ قائمة؟ المنفِّذُ يقترحُ الأوّلَ لأنَّ الثانيَ يُسوّي بين أثرَين مختلفَين في التدقيق.
4. **الأصولُ والالتزاماتُ ومصادرُ الإيراد (15–17):** اقتُرِحَت تنفيذيّةً لأنّها تسجيلٌ بلا حركةِ مال؛ فإن رأى المالكُ أنّها من شأنِ الخزانةِ فكلٌّ منها يحتاجُ مدخلَ تفويضٍ ماليٍّ بسندِ Q-19.
5. **`log_cost` (24):** يُقاسُ فاعلُه التنفيذيُّ ولم يُقَس مُنادِيه في `model_gateway/main.py:230` (مسارُ واجهةٍ لا كائنُ مُصرِّحٍ اليوم).

## 5 · ما يقيسُه الجدولُ وما لا يقيسُه

- **مقيس:** حكمُ المحرّكِ لثمانيةٍ وثلاثينَ فعلًا × عشرةِ فاعلين في الوضعين · وأثرُ كلِّ سطحٍ قراءةً ساكنة.
- **لم يُقَس:** المسارُ الكاملُ `guard_declared` ⇒ الجسرُ ⇒ النواةُ لأيِّ سطح (لا شِفرةَ قبلَ الإقرار) · سلوكُ المعوِّضاتِ المقترحة · أثرُ الحصرِ الجديدِ على مُنادينَ قائمينَ يمرّونَ اليومَ بالاسمِ المجهول (يُقاسُ في دفعةِ كلِّ فعل) · تفاعلُ الأفعالِ الجديدةِ مع مستوياتِ مفتاحِ الإيقاف (ليست في `KILL_SWITCH_BLOCKS` — مقيسٌ عدمُ التصادمِ فقط).
- **أثرُ الجدولِ على D-4:** صفر — وثيقةٌ لا شِفرة. وإن أُقِرَّ ونُفِّذَ كاملًا فالـ24 عبورٌ يُقاسُ في دفعتِه (المتوقَّعُ رقمٌ لا يُكتَبُ مقيسًا قبلَ قياسِه).

## 6 · الدفعةُ 1 — الأسطحُ الثمانيةُ في `federal_state` (W-817 · قرارُ Q-97 · قبلَ الشِّفرة)

**السند:** قرارُ المالكِ Q-97 (التوجيهُ 42 § 1) — السؤالُ 1: «فعلٌ جديدٌ باسمِ السطح» لا ربطٌ بـ`create_state`/`grant_authority`/`revoke_authority` · السؤالُ 2: الإضافةُ إلى `EXECUTIVE_ACTIONS` تضييقٌ على سابقةِ Q-18 بقيودِه (أ)–(هـ) · ترتيبُ الدفعات: هذه الأولى. **التصنيف: C4** (تمسُّ `core/constitutional_engine/rules.py`) — فلا يُسمّى شيءٌ فيها VERIFIED بغيرِ المراجعِ أو المجلس، والدمجُ بالمسارِ المعتادِ لا يمنحُ حالة.

### 6.1 الجدول (لكلِّ سطحٍ: الفعلُ · الفاعلُ · الأثرُ المعلَن · المعوِّض · مفتاحُ الذرّيّة)

| # | السطح | الفعل | الفاعل | الأثرُ المعلَن (`declared_effect`) | المعوِّض (`idempotent=True`) | مفتاحُ الذرّيّة (النطاق = الفعل) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `register_government` | `register_government` | EXECUTIVE | CREATE `federation/{tenant}/governments/{code}` | حذفُ صفِّ `GovernmentModel` بمعرّفِه المولَّدِ قبلَ العبور (لا أثرَ إن غاب) | `{tenant}:{code}` — الرمزُ فريدٌ أبدًا (الحلُّ حالةٌ لا حذف) |
| 2 | `set_government_status` | `set_government_status` | EXECUTIVE | WRITE `federation/{tenant}/governments/{code}/status` | إعادةُ `status`/`status_reason`/`updated_at` المقروءةِ قبلَ العبور | `{tenant}:{gov_id}:{prev_status}->{status}@{prev_updated_at}` — نسخةٌ لا محتوى، فالعمليّةُ المشروعةُ اللاحقةُ ليست إعادة |
| 3 | `bind_institution` | `bind_institution` | EXECUTIVE | CREATE (ربطٌ جديد) أو WRITE (إعادةُ ربطٍ قائم) `federation/{tenant}/institutions/{code}/government` | جديد ⇒ حذفُ صفِّ الربط · قائم ⇒ إعادةُ `government_id`/`relation`/`assigned_by`/`assigned_by_identity_id`/`updated_at` | `{tenant}:{institution_id}:{row_version\|new}:{government_id}:{relation}` |
| 4 | `record_relation` | `record_relation` | EXECUTIVE | CREATE `federation/{tenant}/relations/{id}` | حذفُ صفِّ العلاقة | `{tenant}:{id}` — المعرّفُ مولَّدٌ قبلَ العبور؛ **العلاقةُ ليست ذرّيّةً بالمحتوى** (علاقتانِ متطابقتانِ مسموحتانِ اليوم) فالمفتاحُ يحمي من تكرارِ أثرٍ واحدٍ لا من تكرارِ الطلب — انحرافٌ معلَن |
| 5 | `grant_delegation` | `grant_delegation` | EXECUTIVE | CREATE `federation/{tenant}/delegations/{id}` | حذفُ صفِّ التفويض | `{tenant}:{id}` (مولَّدٌ بـ`new_delegation_id()` قبلَ العبور) — الانحرافُ نفسُه |
| 6 | `revoke_delegation` | `revoke_delegation` | EXECUTIVE | WRITE `federation/{tenant}/delegations/{id}/status` | إعادةُ `status`/`revoked_at`/`revoked_reason`/`updated_at` | `{tenant}:{id}` — النقضُ مرّةً واحدة (والثانيةُ مرفوضةٌ قبلَ العبورِ كما هي اليوم) |
| 7 | `scope_service` | `scope_service` | EXECUTIVE | CREATE أو WRITE `federation/{tenant}/services/{service_id}/scope` | جديد ⇒ حذف · قائم ⇒ إعادةُ `level`/`government_id`/`department_id`/`updated_at` | `{tenant}:{service_id}:{row_version\|new}:{level}:{department_id}` |
| 8 | `scope_case` | `scope_case` | EXECUTIVE | CREATE `federation/{tenant}/cases/{case_id}/scope` | حذفُ صفِّ الإسناد | `{tenant}:{case_id}` — إسنادٌ واحدٌ للقضيّة (الثاني مرفوضٌ قبلَ العبور) |

### 6.2 شكلُ العبور (نقطةٌ واحدةٌ للسطح · نمطُ `government_services.publish_service`)

1. **الفحوصُ القائمةُ كلُّها قبلَ العبورِ ولا تُضعَّف:** `require_domain_permission` · المفرداتُ المقيَّدة · السببُ المكتوب · المستأجر · وجودُ الصفوف · `require_government_authority` في `scope_case` · ورفضُ التكرار. تُقرأُ في جلسةٍ تُغلَقُ قبلَ العبور.
2. `self.authorizer.guard_declared(<الفعل>, target, declared_effects=(effect,), applier=_apply, operation_key=..., compensators=(...), metadata={tenant_id + رموزٌ لا مال})` — **مرّةً واحدةً في جسمِ كلِّ سطح** (فيعدُّها الجردُ `sovereign_write_inventory.py` عبورًا).
3. `_apply` يفتحُ جلسةَ كتابةٍ جديدةً ويكتبُ ويُثبِّتُ ثمّ يُسجِّلُ `record_domain_trace` **داخلَه** (فالإعادةُ لا تُنتِجُ حدثًا ثانيًا لأثرٍ واحد). ولا تحقّقَ في المُطبِّق — كلُّ رفضٍ قبلَه، فلا يُغلَقُ سجلُّ الذرّيّةِ «غيرَ محسومٍ» بخطأِ تحقّق.
4. **الإعادة:** `{…المعرّفات، "replayed": True, "operation_key": …}` · وغيرُها `{**guarded.value, "replayed": False}` — مفتاحٌ مضافٌ لا مفتاحٌ محذوف، فالمنادونَ القائمونَ لا ينكسرون.
5. المُصرِّحُ معامَلٌ اختياريٌّ أخيرٌ في `FederalStateGovernment.__init__(executive_core=None, authorizer=None)` والافتراضُ `get_authorizer()` (الفاعلُ EXECUTIVE) بالاستيرادِ المؤجَّل.

### 6.3 القيودُ (أ)–(هـ) من Q-97 وكيف تُقاسُ في W-818

- **(أ)** قرارٌ سياديٌّ مستقلٌّ: Q-97 نفسُه للدفعةِ 1؛ ولكلِّ دفعةٍ لاحقةٍ تمسُّ `core/` قرارُها.
- **(ب)** هذا القسمُ — مُدوَّنٌ قبلَ الشِّفرةِ في قيدِ W-817 السابقِ لقيدِ W-818 في الدفعةِ نفسِها.
- **(ج)** مسبارٌ خامٌ بملفّ: `docs/audit/evidence/W-817/q97_engine_probe.py` يقرأُ `core/constitutional_engine/rules.py` **من القرص** (لا ترقيعَ في الذاكرة) ويُقيِّمُ كلَّ فعلٍ لعشرةِ فاعلين: المقبولُ EXECUTIVE وحدَه والتسعةُ مرفوضون، ومعه مستوياتُ مفتاحِ الإيقافِ 0–5.
- **(د)** أثرُ الحصرِ على المنادين: مسحٌ ساكنٌ محفوظٌ لكلِّ نصٍّ حرفيٍّ للأفعالِ الثمانيةِ في الشِّفرةِ خارجَ هذه الدفعة + عددُ اجتيازِ `test_r8`/`test_r9` قبلُ وبعد. فإن ظهرَ منادٍ يمرُّ اليومَ بالاسمِ المجهولِ وسيُحجَبُ فلا دمج.
- **(هـ)** طفرة: حذفُ كلِّ فعلٍ من `EXECUTIVE_ACTIONS` على نسخةٍ مؤقّتةٍ ⇒ المسبارُ يجبُ أن يفشل (8 طفرات) · ورفعُ `guard_declared` من كلِّ سطحٍ ⇒ اختبارُ العبورِ يجبُ أن يفشل (8 طفرات).

### 6.4 ما لا تفعلُه الدفعة

لا تُدخِلُ الأفعالَ الثمانيةَ في `KILL_SWITCH_BLOCKS` (لم يُقرَّر ذلك — سابقةُ `graceful_shutdown`: اسمٌ جديدٌ بلا منعٍ حتى يُقرَّر) ويُقاسُ أثرُ المستوياتِ كما هو · لا تمسُّ `execute_scoped_operation` ولا `execute_scoped_disbursement` (الدفعتانِ 3 و4) · لا تُغيِّرُ المعنى الدستوريَّ لتسجيلِ الحكومة (سؤالٌ مفتوحٌ للمالكِ في Q-97).

## 7 · الدفعةُ 2 — الأسطحُ التسعةُ في `national_economy` (W-819 · قرارُ Q-98 · قبلَ الشِّفرة)

**السند:** قرارُ المالكِ Q-98 (التوجيهُ 43 § 1): «أسطح national_economy التسعة، بنهج Q-97 نفسه (فعل جديد باسم السطح، تضييق على سابقة Q-18، قرار سيادي مستقل، تصميم قبل الشفرة، مسبار خام، قياس المنادين، طفرات). الأسطح 15–17 تبقى تنفيذية افتراضًا مؤقتًا كما في Q-97». **التصنيف: C4** (تمسُّ `core/constitutional_engine/rules.py`) — فلا VERIFIED بغيرِ المراجعِ أو المجلس، وتُدرَجُ في قائمةِ غيرِ المراجَعِ مع الدفعةِ 1 وWI-114 (RK-024).

### 7.1 الجدول (الأسطحُ 9–17 من § 3 · كلُّها CREATE)

| # | السطح | الفعل | الفاعل | الأثرُ المعلَن (`declared_effect`) | المعوِّض (`idempotent=True`) | مفتاحُ الذرّيّة |
| --- | --- | --- | --- | --- | --- | --- |
| 9 | `register_sector` | `register_sector` | EXECUTIVE | CREATE `economy/{tenant}/sectors/{code}` | حذفُ صفِّ `EconomicSectorModel` بمعرّفِه المولَّدِ قبلَ العبور | `{tenant}:{code}` |
| 10 | `register_category` | `register_category` | EXECUTIVE | CREATE `economy/{tenant}/sectors/{sector_code}/categories/{code}` | حذفُ صفِّ `EconomicCategoryModel` | `{tenant}:{sector_id}:{code}` — الفئةُ فريدةٌ في قطاعِها لا في المستأجر |
| 11 | `define_indicator` | `define_indicator` | EXECUTIVE | CREATE `economy/{tenant}/indicators/{code}` | حذفُ صفِّ `EconomicIndicatorDefinitionModel` | `{tenant}:{code}` |
| 12 | `register_public_entity` | `register_public_entity` | EXECUTIVE | CREATE `economy/{tenant}/entities/{code}` | حذفُ القرارِ ثمّ الكيان | `{tenant}:{code}` |
| 13 | `create_program` | `create_program` | EXECUTIVE | CREATE `economy/{tenant}/programs/{code}` | حذفُ القرارِ ثمّ البرنامج | `{tenant}:{code}` |
| 14 | `issue_policy` | `issue_policy` | EXECUTIVE | CREATE `economy/{tenant}/policies/{code}` (مسوَّدة) | حذفُ السياسةِ ثمّ قرارِها (`decision_id` مفتاحٌ أجنبيٌّ من السياسةِ إلى القرار) | `{tenant}:{code}` |
| 15 | `register_revenue_source` | `register_revenue_source` | EXECUTIVE (افتراضٌ مؤقّت) | CREATE `economy/{tenant}/revenue_sources/{code}` | حذفُ القرارِ ثمّ المصدر | `{tenant}:{code}` |
| 16 | `register_public_asset` | `register_public_asset` | EXECUTIVE (افتراضٌ مؤقّت) | CREATE `economy/{tenant}/assets/{code}` | حذفُ القرارِ ثمّ الأصل | `{tenant}:{code}` |
| 17 | `register_public_liability` | `register_public_liability` | EXECUTIVE (افتراضٌ مؤقّت) | CREATE `economy/{tenant}/liabilities/{code}` | حذفُ القرارِ ثمّ الالتزام | `{tenant}:{code}` |

**انحرافٌ معلَنٌ عن § 3 الصفّ 12** («أثران · معوِّضان»): الأسطحُ 12–17 تكتبُ صفَّها وقرارَها الاقتصاديَّ **في معاملةٍ واحدة** اليوم. فإعلانُ أثرَين يقسمُ المطبِّقَ نداءَين بتثبيتَين ويُضعِفُ الذرّيّةَ القائمةَ في القاعدة. فالمعلَنُ أثرٌ واحدٌ يشملُ الصفَّين، ومعوِّضٌ واحدٌ يحذفُهما بترتيبِ مفاتيحِهما الأجنبيّة. ولا يُقاسُ أنّ هذا أقوى؛ هو حفظٌ لما هو قائم.

### 7.2 شكلُ العبور (نمطُ § 6.2 نفسُه · أصغرُ فرقٍ في الشِّفرة)

1. **الفحوصُ القائمةُ كلُّها قبلَ العبورِ ولا تُضعَّف:** `require_domain_permission` · المفرداتُ المقيَّدة (المستوى · الحالة · النوع) · المستأجر · وجودُ الصفوف · `_authorize` (حلُّ السلطةِ قراءةً: `require_government_authority` لا يكتب) · `_target_government` · رفضُ التكرار. تُقرأُ في جلسةٍ تُغلَقُ قبلَ العبور، **ويُبنى الصفُّ فيها كائنًا عابرًا لا يُضاف** (`session.add` لا يُنادى في جلسةِ القراءة).
2. `self.authorizer.guard_declared(<الفعل>, target, declared_effects=(effect,), applier=_apply, operation_key=..., compensators=(...), metadata={tenant_id + الرمز})` مرّةً واحدةً في جسمِ كلِّ سطح.
3. `_apply` يفتحُ جلسةَ كتابةٍ جديدة: يُضيفُ الصفَّ، ويُصدِرُ القرارَ بـ`_issue_decision` **فيها** (12–17)، ويُثبِّت، ثمّ `_announce` داخلَه. والأسطحُ 9–11 لا حدثَ لها اليومَ ولا يُضافُ لها حدث.
4. **الإعادة:** `{…الرمز، "replayed": True, "operation_key": …}` · وغيرُها `{**guarded.value, "replayed": False}` — مفتاحٌ مضافٌ لا محذوف.
5. المُصرِّحُ معامَلٌ اختياريٌّ أخيرٌ: `NationalEconomy.__init__(executive_core=None, federation=None, authorizer=None)` والافتراضُ `get_authorizer()` بالاستيرادِ المؤجَّل.

### 7.3 القياس (Q-98 · ومعه ما طلبَه التوجيهُ 43 § 2)

- **مسبارٌ خام** `evidence/W-819/q98_engine_probe.py`: يقرأُ `rules.py` من القرص · لكلِّ فعلٍ من التسعة عشرةُ فاعلين: المقبولُ EXECUTIVE وحدَه · ومستوياتُ مفتاحِ الإيقافِ 0–5.
- **أثرُ الحصرِ على المنادين:** مسحٌ ساكنٌ لكلِّ نصٍّ حرفيٍّ للأفعالِ التسعةِ قبلُ وبعد + اجتيازُ `test_r8`/`test_r9` قبلُ وبعد.
- **الطفرات:** حذفُ كلِّ فعلٍ من `EXECUTIVE_ACTIONS` ⇒ المسبارُ يفشل (9) · ورفعُ `guard_declared` من كلِّ سطح ⇒ اختبارُ العبورِ يفشل (9).
- **المسارُ كاملًا إعلانًا ⇒ جسرًا ⇒ نواة** — لم يُقَس صراحةً في الدفعةِ 1 (اختبارُها حقنَ مُصرِّحًا وقرأَ `ledger_entry_hash` من الدليلِ لا من سجلِّ النواة). يُقاسُ الآنَ للأسطحِ السبعةَ عشرَ (8 + 9) بتوصيلِ الإنتاجِ الافتراضيّ (`authorizer=None` ⇒ `get_authorizer()`): بعدَ كلِّ نداءٍ يُقرأُ سجلُّ النواةِ `ConstitutionalLedger` نفسُه فيُوجَدُ قيدُ `CONSTITUTIONAL_VERDICT` بالفعلِ والفاعلِ EXECUTIVE وALLOW، وتُطابِقُ بصمتُه `ledger_entry_hash` في سجلِّ البوّابة، و`verify_chain()` فارغ.
- **PostgreSQL:** وظيفةُ CI «Cross-System Suites (SQLite + PostgreSQL)» تُشغِّلُ حزمًا مسمّاة؛ يُقاسُ هل تشملُ ملفّاتِ العبور، وإلّا يُكتَبُ «لم يُقَس».

### 7.4 ما لا تفعلُه الدفعة

لا `KILL_SWITCH_BLOCKS` (كما في § 6.4) · لا تمسُّ أسطحَ الخزانةِ 18–20 (الدفعةُ 3) ولا المركَّبةَ 21–23 (الدفعةُ 4) ولا `log_cost` (لا شِفرةَ قبلَ القياس) · لا تُقرِّرُ أنّ 15–17 تنفيذيّةٌ نهائيًّا.
