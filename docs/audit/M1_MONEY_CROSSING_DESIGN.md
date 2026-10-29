# M1 — عبورُ المالِ إلى الحدِّ السياديّ: تصميمٌ ورقيٌّ قبلَ أيِّ شِفرة

## الهدف: تصميمُ عبورِ الأسطحِ العامّةِ الـ33 في `national_economy` (16) و`federal_state` (10) و`state_treasury` (7) إلى `guard_declared` تصميمًا يُعرَضُ على المالكِ قبلَ أيِّ شِفرة — بأمرِ التوجيهِ 29 (D30): «WI-085 تصميم (طلبته في 28) وM1 تصميم. كلاهما بلا شفرة، وكلاهما لا يتوقف على المجلس».
## النطاق: وثيقةُ تصميمٍ — لا شِفرةَ إنتاجيّةً · لا مساسَ بـK1 ولا بـ`core/` ولا بالمعجمِ · القياساتُ قراءةٌ ساكنةٌ ومسبارُ محرّكٍ على سجلٍّ مؤقّتٍ في `evidence/W-739/`.
## المالك: docs/audit — البندُ WI-122 (federal-executive) · المنفِّذُ Perplexity Computer (المنسِّقُ Claude Opus 5.5 · قيدُ W-739).
## تاريخ الإنشاء: 2026-10-29
## تاريخ آخر تعديل: 2026-10-29 (W-739 — الإنشاء)

---

## 0. السندُ والشروطُ السابقة

| السند | النصّ | حالتُه المقيسة |
|---|---|---|
| WI-110 (Q-9) · الخيارُ 4 — DECIDED (W-660) | «يُمنع التعشيش السيادي بكاشف عند الحد، ويُعاد هيكلة مركّبات المال الثلاثة على نمط «الخارجي يُعلن الآثار وينادي نوًى خاصة»، ويُستثنى open_case باسمه استثناءً مسجَّلًا، ويُعالَج خطر إعادة disburse لحركة معكوسة (§3.5) قبل M1.» | الكاشفُ قائم: `core/sovereignty/enforcement_boundary.py` (`NESTED_SOVEREIGN_EXEMPTIONS` = زوجا `gov.case.open` فقط · الرفعُ قبلَ أيِّ `decide`) · § 3.5 مُصلَح: `StateTreasury._existing_idempotent` يرفعُ `EntityStateError` لحركةٍ `reversed` |
| D25-3 — DECIDED (W-671) | «الكاشف أولًا، ثم M1.» | الكاشفُ (W-685) قبلَ هذا التصميم |
| Q-19 — الخيارُ 2 (مُنفَّذ · W-013) | «فاعلُ الخزانةِ لكلِّ عمليّةٍ على حِدَةٍ بتفويضٍ مُعلَن» — لا وسمَ لخدمةٍ كاملة | `common/money_delegation.py` (`resolve_money_delegation`) · `executive_core/money_authority.py` عندَ `_authorize_money` (Q-31 ②) |
| Q-68 — DECIDED (W-592) | «الحصر: لا يمارس AGENT ولا SYSTEM أفعال الفروع الحصرية. يُنفَّذ كبند مستقل بدفعة مراجعة C4 بعد J1 لا قبله.» | غيرُ مُنفَّذٍ بعد — والمسبارُ (§ 2.2) يقيسُه ALLOW اليوم |
| درسُ Q-26 (W-736) | عبورٌ واحدٌ لكلِّ سطحٍ يُعلِنُ كلَّ آثارِه بنوًى خاصّةٍ ومعوِّضٍ لكلِّ أثر | مقيسٌ على `retire_agent`: المسبارُ broken 3→1 |

## 1. القياسُ (قبلَ أيِّ شِفرة)

### 1.1 الأسطحُ الـ33 ونداءاتُها — `evidence/W-739/m1_surface_scan_output.txt`

الأمر: `python3 docs/audit/evidence/W-739/m1_surface_scan.py` — الخلاصةُ حرفيًّا: `SCAN SUMMARY: surfaces=33 marks={'disburse': 3, 'core': 3, 'delegation': 9, 'guard': 0}`.

| الصنف | العدد | الأسطح |
|---|---|---|
| مالٌ ← مال (`.disburse(` داخلَ السطح) | 3 | `execute_expenditure` (l.1382) · `execute_transfer` (l.1710) · `execute_scoped_disbursement` (l.1053) |
| مالٌ ← النواةُ التنفيذيّةُ المحروسة (`_execute_via_core`/`submit`/`run`) | 3 | `activate_policy` (l.977) · `execute_economic_decision` (l.2207) · `execute_scoped_operation` (l.974) |
| أسطحُ الخزانةِ الذرّيّة (تفويضٌ مُعلَنٌ قائم) | 7 | `allocate` · `create_budget` · `disburse` · `establish_treasury` · `open_account` · `post_funding` · `reverse_transaction` |
| كتابةٌ مباشرةٌ بلا نداءٍ سياديّ | 20 | 12 في `national_economy` · 8 في `federal_state` |
| **محروسٌ اليوم** | **0 من 33** | — |

مفوِّضانِ خارجَ الجرد (لا كتابةَ مباشرةً لهما) يُناديانِ `disburse`: `StateTreasury.execute_decision_disbursement` (l.1460 → `self.disburse` l.1514) و`FederalJudiciary.enforce_ruling_via_treasury` (l.1012 → `treasury.disburse` l.1046).

### 1.2 حكمُ المحرّكِ على أفعالِ المالِ لكلِّ فاعل — `evidence/W-739/engine_probe_output.txt`

الأمر: `.venv/bin/python docs/audit/evidence/W-739/engine_probe_money_actor.py` — 150 صفًّا (15 فعلًا × 10 فاعلين). الخلاصةُ حرفيًّا:
`ALLOW per actor (of 15): {'EXECUTIVE': 0, 'LEGISLATIVE': 0, 'JUDICIAL': 0, 'TREASURY': 15, 'ROYAL': 15, 'HUMAN': 15, 'STATE': 15, 'INSTITUTION': 15, 'AGENT': 15, 'SYSTEM': 15}`

فالغلافُ بفاعلٍ `EXECUTIVE` يُرَدُّ `DENY ['R-003-1']` على كلِّ فعلٍ ماليّ، فيلزمُ غلافَ M1 فاعلُ `TREASURY` بتفويضٍ مُعلَنٍ لكلِّ عمليّة (Q-19 ②). و`AGENT`/`SYSTEM`/`STATE`/`INSTITUTION` ⇒ ALLOW اليوم — هذا Q-68 غيرُ المُنفَّذ، لا يُصلَحُ في M1 (بندٌ مستقلٌّ بعدَ J1 بنصِّ المالك)، ويُعلَنُ هنا لأنَّ M1 لا يُغلِقُه.

## 2. التصميم

### 2.1 القاعدةُ العامّة — عبورٌ واحدٌ لكلِّ سطح
كلُّ سطحٍ من الـ33 يصيرُ **عبورًا واحدًا** `guard_declared` بفعلِه الدستوريِّ من `MONEY_OPERATION_LEXICON`/`TREASURY_ACTIONS` حيثُ وُجِد، وبفاعلِ `TREASURY` المُستخرَجِ من `resolve_money_delegation` للعمليّةِ بعينِها (لا وسمَ للخدمة)، ويُعلِنُ كلَّ آثارِه ومعوِّضًا لكلِّ أثر. ولا عبورَ سياديًّا داخلَ المُطبِّق — فالكاشفُ يرفعُ `NestedSovereignCallError`، ولا يُوسَّعُ `NESTED_SOVEREIGN_EXEMPTIONS` (مُجمَّدٌ في `core/` · K1).

### 2.2 أسطحُ الخزانةِ الذرّيّةُ السبعة
تُفصَلُ كلٌّ منها إلى **غلافٍ عامٍّ محروس** و**نواةٍ خاصّة** (`_disburse_core` · `_reverse_core` · …) تحملُ الكتابةَ الحاليّةَ بلا تغيير. والمعوِّضُ لكلِّ أثرٍ نواةُ العكسِ الخاصّة (`_reverse_core`) لا الغلافُ المحروس (وإلّا تعشَّشَ المعوِّضُ). والمفتاحُ النطاقيُّ (`idempotency_key`) يبقى، وإصلاحُ § 3.5 يبقى حارسَه.

### 2.3 مركَّباتُ المالِ الثلاثة (مالٌ ← مال)
`execute_expenditure` · `execute_transfer` · `execute_scoped_disbursement`: الغلافُ الخارجيُّ يُعلِنُ آثارَه كلَّها — أثرَ الصرفِ (`TRANSFER:treasury/...`) وأثرَ سجلِّ العمليّة وأثرَ تحديثِ الحالة — وينادي `_disburse_core` داخلَ مُطبِّقِه لا `disburse` العامّ. ومعوِّضُ أثرِ الصرفِ `_reverse_core` على الحركةِ نفسِها. والمفتاحُ النطاقيُّ للصرفِ يُشتقُّ من مفتاحِ المركَّب (اليومَ `exp-{reference}` / `trf-{reference}`) — وحركةٌ معكوسةٌ لا تُعادُ (§ 3.5 · مُصلَح).

### 2.4 المفوِّضانِ
`execute_decision_disbursement` و`enforce_ruling_via_treasury` يُعاملانِ معاملةَ 2.3: عبورٌ واحدٌ ينادي `_disburse_core`. ويبقى قرارُ الفعلِ والفاعلِ في `enforce_ruling_via_treasury` (القضاءُ يأمرُ والخزانةُ تصرف) سؤالًا للمالكِ (Q-83 (ب)).

### 2.5 مركَّباتُ النواةِ التنفيذيّةِ الثلاثة
`activate_policy` · `execute_economic_decision` · `execute_scoped_operation` تُنادي `ExecutiveCore.submit`/`run` المحروسَين سلفًا (`task.submit` …). نصُّ Q-9 الخيارُ 4: «3 مواضعِ ← النواة فتُرتَّبُ تسلسلًا خارجَ المُطبِّق (النواةُ ليست مالًا ولا تُفكَّكُ في M1)». لكنَّ درسَ Q-26 (W-735/W-736) قاسَ أنَّ العبوراتِ المتعاقبةَ تتركُ حالةً وسيطةً بلا دفترٍ مشترك. فالمعروضُ على المالكِ (Q-83 (أ)):
- ① تسلسلٌ خارجَ المُطبِّق كما في نصِّ Q-9 (النواةُ عبورُها أوّلًا ثمَّ عبورُ الاقتصادِ لسجلِّ العمليّة) مع نافذةٍ وسيطةٍ مُعلَنةٍ واختبارِ فشلِ الخطوةِ الثانية؛
- ② زوجٌ استثنائيٌّ مسمًّى ثانٍ في `NESTED_SOVEREIGN_EXEMPTIONS` على سابقةِ `open_case` — يمسُّ `core/` فيحتاجُ قرارًا وطفرات؛
- ③ تأجيلُ الثلاثةِ من M1 إلى بندٍ يلي.
**توصيةُ المنفِّذ (رأيٌ لا قرار): ①** — هو نصُّ القرارِ القائم، ولا يمسُّ K1، والنافذةُ تُقاسُ بالمسبارِ نفسِه قبلَ وبعد.

### 2.6 الأسطحُ العشرون ذاتُ الكتابةِ المباشرة
عبورٌ واحدٌ بأثرٍ واحدٍ أو أكثر ومعوِّضٍ لكلٍّ. أفعالُها ليست كلُّها في معجمِ المال (مثلًا `register_sector`، `bind_institution`)، فلا تحتاجُ فاعلَ الخزانة إلّا ما كانَ فعلُه في `TREASURY_ACTIONS` (`authorize_expenditure` ← `economy.expenditure.authorize` مقيسٌ في المعجم؛ و`economy.procurement.award` في `MONEY_OPERATION_LEXICON` بلا مدخلٍ في الشِّفرةِ ينادي تفويضَه، و`authorize_procurement`/`authorize_transfer` لا يناديانِ `resolve_money_delegation` اليوم — `m1_surface_scan_output.txt` و`engine_probe_output.txt`). والمعجمُ للعشرين سؤالٌ للمالك (Q-83 (ج)) — لا يُخترَعُ اسمُ فعلٍ لإنجاحِ عبور.

### 2.7 دفعاتُ الشِّفرةِ المقترحة (بعدَ قرارِ المالكِ · ثلاثةُ قيودٍ كحدٍّ أقصى لكلِّ دفعة)
1. الخزانةُ السبع + النوى الخاصّة (2.2).
2. المركَّباتُ الثلاثة + المفوِّضان (2.3 · 2.4).
3. `federal_state` الثمانية + `national_economy` الاثنا عشر (2.6) بعدَ المعجم.
4. النواةُ الثلاثة (2.5) بعدَ Q-83 (أ).

### 2.8 جدولُ الأسطحِ الـ33 (الفعل · الفاعل · الآثار · المعوِّض)
مصدرُ الأعمدة: `write_inventory_p13.json` (`writes` · `writes_via`) و`MONEY_OPERATION_LEXICON` والأسماءُ النطاقيّةُ في الشِّفرة (`design_measurements.txt` · `m1_surface_scan_output.txt`). «Q-83» حيثُ لا يُخترَعُ فعلٌ.

| السطح | العمليّةُ النطاقيّة | الفعلُ الدستوريّ | الفاعل | الآثارُ المُعلَنة | المعوِّض |
|---|---|---|---|---|---|
| state_treasury · `establish_treasury` | `treasury.establish` | `establish_treasury` | TREASURY | CREATE خزانة | حذفُ الصفِّ المُنشأ (نواةٌ خاصّة) |
| state_treasury · `open_account` | `treasury.account.open` | `open_account` | TREASURY | CREATE حساب | حذفُ الصفِّ المُنشأ |
| state_treasury · `create_budget` | `treasury.budget.create` | `create_budget` | TREASURY | CREATE ميزانيّة | حذفُ الصفِّ المُنشأ |
| state_treasury · `allocate` | `treasury.allocate` | `allocate_funds` | TREASURY | CREATE تخصيص | حذفُ الصفِّ المُنشأ |
| state_treasury · `post_funding` | `treasury.funding.post` | `post_funding` | TREASURY | TRANSFER حركة (`_post`) + CREATE سندُ التفويض | `_reverse_core` على الحركة |
| state_treasury · `disburse` | `treasury.disburse` | `disburse_funds` | TREASURY | TRANSFER حركة (`_post`) + CREATE سندُ التفويض | `_reverse_core` على الحركة |
| state_treasury · `reverse_transaction` | `treasury.transaction.reverse` | `reverse_transaction` | TREASURY | TRANSFER حركةُ عكس + WRITE حالةُ الأصل `reversed` | لا معوِّضَ آليٌّ للعكس — عكسُ العكسِ ممنوعٌ اليوم؛ يُعلَنُ أثرًا بلا معوِّضٍ ويُسأل عنه في دفعته |
| national_economy · `execute_expenditure` | `economy.expenditure.execute` | Q-83 (ج) — `economy.expenditure.execute` لا مدخلَ له في المعجم؛ الصرفُ الداخليُّ `disburse_funds` | TREASURY | TRANSFER (`_disburse_core`) + WRITE حالةُ الإجازة | `_reverse_core` + إعادةُ الحالة |
| national_economy · `execute_transfer` | `economy.transfer.execute` | `execute_transfer` | TREASURY | TRANSFER (`_disburse_core`) + WRITE حالةُ الإجازة | `_reverse_core` + إعادةُ الحالة |
| federal_state · `execute_scoped_disbursement` | `federation.treasury.execute` → `treasury.disbursement.post` | Q-83 (ج) للخارجيّ؛ الداخليُّ `treasury.disbursement.post` → `disburse_funds` | TREASURY | TRANSFER (`_disburse_core`) + CREATE سجلُّ العمليّة | `_reverse_core` + حذفُ السجلّ |
| national_economy · `activate_policy` | `economy.policy.activate` | Q-83 (ج) | Q-83 (أ) | تسلسل: عبورُ النواة ثمَّ WRITE الحالة + CREATE القرار | بحسب Q-83 (أ) |
| national_economy · `execute_economic_decision` | `economy.decision.execute` | Q-83 (ج) | Q-83 (أ) | تسلسل: عبورُ النواة ثمَّ WRITE الحالة | بحسب Q-83 (أ) |
| federal_state · `execute_scoped_operation` | `federation.operation.execute` | Q-83 (ج) | Q-83 (أ) | تسلسل: عبورُ النواة ثمَّ CREATE سجلُّ العمليّة | بحسب Q-83 (أ) |
| national_economy · `authorize_expenditure` | `economy.expenditure.authorize` | `authorize_expenditure` | TREASURY | CREATE إجازة + CREATE القرار (`_issue_decision`) | حذفُ الصفَّين |
| national_economy · `authorize_procurement` · `authorize_transfer` · `create_program` · `define_indicator` · `issue_policy` · `register_category` · `register_public_asset` · `register_public_entity` · `register_public_liability` · `register_revenue_source` · `register_sector` (11) | اسمُها النطاقيُّ القائم | Q-83 (ج) | بحسبِ الفعل (فاعلُ الخزانةِ إن كانَ الفعلُ في `TREASURY_ACTIONS`) | CREATE صفّ (+ CREATE القرار لمن ينادي `_issue_decision`: 8 منها) | حذفُ الصفِّ المُنشأ |
| federal_state · `bind_institution` · `grant_delegation` · `record_relation` · `register_government` · `revoke_delegation` · `scope_case` · `scope_service` · `set_government_status` (8) | `federation.*` القائم | Q-83 (ج) | EXECUTIVE (أفعالٌ غيرُ ماليّة) | CREATE صفّ (6) · WRITE حالة (`revoke_delegation` · `set_government_status`) | حذفُ الصفّ / إعادةُ القيمةِ السابقة |

والمفوِّضانِ خارجَ الجرد: `execute_decision_disbursement` (`treasury.decision.disburse` → `disburse_funds` · TREASURY · TRANSFER بـ`_disburse_core` · `_reverse_core`) و`enforce_ruling_via_treasury` (Q-83 (ب)). فنقاطُ الدخولِ الخمسُ إلى `disburse` (3 مركَّبات + 2 مفوِّضان) كلُّها تصيرُ نداءً لـ`_disburse_core` داخلَ عبورٍ واحد.

## 3. معاييرُ القبولِ لدفعاتِ الشِّفرة

| # | المعيار | القياس |
|---|---|---|
| 1 | D-4 ينخفضُ بعددِ ما عبرَ فعلًا (من 95) | `tools/audit/sovereign_write_inventory.py` قبلَ وبعد |
| 2 | عبورٌ واحدٌ لكلِّ سطح | فحصُ العبوراتِ المتعاقبة (`evidence/W-735/scan_sequential_crossings.py`) — صفرُ تسلسلٍ جديدٍ إلّا ما قرّرَه Q-83 (أ) |
| 3 | لا تعشيشَ مرفوعٌ في المسارِ الأخضر | الكاشفُ لا يرفعُ في اختباراتِ الخدمات · و`NESTED_SOVEREIGN_EXEMPTIONS` بلا تغيير (فحصُ التساوي) |
| 4 | فاعلُ الخزانةِ لكلِّ عمليّة | كلُّ غلافٍ ماليٍّ يمرُّ بـ`resolve_money_delegation` · فاعلٌ `EXECUTIVE` ⇒ DENY `R-003-1` مقيسًا |
| 5 | صدقُ التعويض | اختبارُ فشلٍ بعدَ الصرفِ يُثبِتُ حركةَ `reversal` في الدفتر · وطفرةُ «حذفُ معوِّضِ أثرِ الصرف» killed |
| 6 | § 3.5 لا يُضعَف | اختبارُ W-670 أخضرُ بلا تعديل |

## 4. أسئلةُ المالك — Q-83 (PENDING_OWNER)
- (أ) مركَّباتُ النواةِ الثلاثة: ① تسلسلٌ مُعلَن · ② استثناءٌ مسمًّى ثانٍ · ③ تأجيل. التوصية ①.
- (ب) `enforce_ruling_via_treasury`: الفاعلُ في العبورِ الواحد `TREASURY` بتفويضٍ مُعلَنٍ يذكرُ الحكمَ القضائيَّ سندًا، أم يبقى خارجَ M1؟ التوصية: `TREASURY` بتفويضٍ مُعلَن.
- (ج) معجمُ الأسطحِ التي لا مدخلَ لعمليّتِها في `MONEY_OPERATION_LEXICON` (العشرون + `execute_expenditure` + `execute_scoped_disbursement` + مركَّباتُ النواةِ الثلاثة — § 2.8): أسماءٌ دستوريّةٌ جديدةٌ بقرارٍ مستقلٍّ قبلَ الدفعة 3. التوصية: قرارٌ مستقلٌّ قبلَ الدفعة 3 لا قبلَ الدفعتين 1 و2.

## 5. ما لم يُقَس
- لم يُشغَّلْ أيُّ سطحٍ ماليٍّ محروسًا — المالُ غيرُ محروسٍ اليوم (0 من 33)، والمسبارُ يمرُّ بالمحرّكِ وحدَه لا بالجسرِ ولا بالحدّ.
- لم تُقَسْ نافذةُ التسلسلِ في 2.5 بمسبار؛ ستُقاسُ في دفعتِها.
- المسحُ الساكنُ اسميٌّ (عمقٌ واحدٌ للنداءاتِ الخاصّة) — الإرسالُ الديناميكيُّ ونقاطُ HTTP في `state_treasury/main.py` غيرُ محلولة.
- PostgreSQL وعزلُ المعاملاتِ للجلساتِ المتعاقبةِ في المركَّبات.
- Q-68 (AGENT/SYSTEM ⇒ ALLOW) مقيسٌ ولا يُصلَحُ هنا.
