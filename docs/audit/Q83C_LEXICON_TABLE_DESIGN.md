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
2026-11-04 (W-816 — النسخةُ الأولى)

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
