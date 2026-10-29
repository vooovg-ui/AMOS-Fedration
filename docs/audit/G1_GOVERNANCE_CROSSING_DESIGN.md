# G1 — تصميمُ عبورِ أسطحِ الحوكمةِ المتبقّيةِ الحدَّ السياديَّ (41 سطحًا · WI-120 · توجيهُ الطابورِ W-712/W-713)

## الهدف: حرقٌ حقيقيٌّ لِD-4 — تصميمٌ يعرضُ نموذجَ الصلاحياتِ للأسطحِ العامةِ المتبقّيةِ تحتَ D-4 في `services/governance/` (41 سطحًا) قبلَ أيِّ شِفرةٍ، وفقَ القراراتِ الأربعةِ المحسومةِ (Q-13 · Q-14 · Q-26 · Q-23)
## النطاق: وثيقةُ تصميمٍ — لا شِّفرةَ فيها · لا مساسَ بـK1 (الملكيِّ) ولا بمعجمِ الدستورِ في هذه الدفعةِ ولا بـ`persistent.py` ولا بحارسٍ قائمٍ (التنفيذُ في دفعةِ الشِّفرةِ اللاحقةِ)
## المالك: Perplexity Computer (المنسِّقُ GLM-5.3) · بتوجيهِ الطابورِ: «دفعةُ G1 الورقيةُ (تصميمُ Q-13/Q-14/Q-26/Q-23) ثمَّ تحليلُ WI-118 وتصميمُ WI-116 — لا جولةَ مجلسٍ جديدةً قبلَ قرارِ المالكِ»
## تاريخ الإنشاء: 2026-10-28 (W-715)
## تاريخ آخر تعديل: 2026-10-29 (W-724 — § 9.9 ملحقُ تصميمِ دفعةِ expansion والمعجمِ الصغيرِ قبلَ الشِّفرة: graceful_shutdown بقرارِ Q-76 · ستّةُ أسطحٍ بنمطِ E1 § 2.2 · Q-77 يوقفُ create_batch/enroll_batch · Q-78) · وقبله: 2026-10-28 (W-723 — § 9.8 ملحقُ تصميمِ الدفعةِ 2 قبلَ الشِّفرة: قناةُ المرسومِ · نطاقُ self_heal · تعارضُ Q-76 · ثمَّ § 9.8.4 الشِّفرةُ مقيسةً) · وقبله: 2026-10-28 (W-722 — دفعةُ المعجمِ § 9.5 مُشفَّرةٌ) · وقبله: 2026-10-28 (W-721 — **اعتمادُ المالكِ بتعديلاتٍ ثلاثة** بالتوجيهِ 27 § 1: (أ) store_secret وrestore_backup دَينٌ · (ب) الخزانةُ التسعةُ وreward_agent إلى M1 · (ج) «المستوى N» = منعٌ عندَ ≥N مقيسًا · وself_heal معتمَدٌ بشرطِه — § 9 تعديلٌ مؤرَّخٌ لا محوٌ) · وقبله: 2026-10-28 (W-715 — الإنشاءُ)

---

## 0. السندُ والانضباط

- **سندُ القراراتِ المحسومةِ** (`docs/audit/SOVEREIGN_DECISION_REGISTER.md` · توجيهُ المستشارِ 21 · D21-أ · 2026-10-23):
  - **Q-13 (الخيار 1)**: «register_state هي create_state دستوريًّا، فتحتاج مسار مرسوم ملكي.»
  - **Q-14 (الخيار 2 + 3 شروط)**: «إيقاف الولاية وإعادتها اختصاص تنفيذي محكوم بلا بوابة بشرية، بشرط أن يُسجَّل كل إيقاف أثرًا مُعلَنًا وأن يغطيه قاطع التشغيل، وأن يُراجَع إعادة التفعيل التلقائي في system_life.py:240 في تصميم الدفعة.»
  - **Q-26 (الخيار 2)**: «WRITE بمُعوِّض يعيد الوكيل، دون مس restore_agent الملكي.» (يخصُّ retire_agent)
  - **Q-23 (الخيار 1)**: «suspend_policy وvote يُضافان إلى المعجم التشريعي.»
- **سندُ الخطةِ الأمّ** (`docs/governance/work/HANDOFFS/D4-BURN-PLAN.md` · صفُّ G1): «الأسطحُ العامةُ المتبقّيةُ في governance/ · 41 سطحًا · C3 (سيادة/أمن) · الإسقاطُ D-4 118←77».
- **مسارُ التنفيذِ (إجراءُ DISC-137)**: هذه الدفعةُ الورقيّةُ تحملُ التصميمَ وتنقلُ البندَ `READY → RESERVED` (WI-120) · ثمَّ دفعةٌ تنقلُهُ `RESERVED → IN_PROGRESS` · ثمَّ دفعاتُ الشِّفرةِ والفحوصِ والطفراتِ.
- **الخطُّ الأساسُ المقيسُ** (أداةُ الجردِ نفسُها · الحمولةُ الخامُّ في `evidence/W-714/d4_baseline_inventory.{txt,json}`): **D-4 = 121** على `8dbe0cf7` (main بعدَ دمجِ W-713) · **G1 = 41 سطحًا عامًّا مفتوحًا في `services/governance/`**. الإسقاطُ في الخطةِ الأمّ (118←77) كانَ إسقاطًا مشروطًا من حالٍ سابقةٍ — القياسُ الفعليُّ اليومَ 121، فالإسقاطُ بعدَ حرقِ G1 هو **80** إسقاطًا مشروطًا لا نتيجةً موعودةً.
- **محظوراتٌ ساريةٌ**: لا شِّفرةَ قبلَ التصميمِ · لا `gh pr merge` · لا VERIFIED/CLOSED بيدِ المنفِّذِ · K1 (الملكيُّ) لا يُمَسُّ · لا تعديلَ لتعريفِ D-4 · لا جولةَ مجلسٍ جديدةً قبلَ قرارِ المالكِ.

---

## 1. المقيسُ الآنَ (على `8dbe0cf7` · مخرجُ `sovereign_write_inventory.py`)

**41 سطحًا عامًّا غيرَ سياديٍّ مفتوحًا** في `services/governance/` حصرًا (لا يشملُ الخاصَّ `_log_event`/`_apply` ولا المحروسَ):

| # | الملفُّ | عددُ الأسطحِ | الأسطحُ |
|---|---|---|---|
| 1 | `expansion.py` | 8 | create_batch · employ_batch · enroll_batch · graduate_batch · retire_agent · take_exam · approve_output · submit_output |
| 2 | `learning_cycle.py` | 7 | evaluate_model · collect_experiences · complete_training · start_training · promote_beta_to_alpha · start_canary · start_shadow |
| 3 | `security.py` | 5 | create_session · check_rate · store_secret · issue_certificate · verify_certificate |
| 4 | `state_runtime.py` | 5 | send_message · assign_agent · reactivate_state · register_state · suspend_state |
| 5 | `system_life.py` | 7 | bootstrap · create_backup · graceful_shutdown · health_check · launch_checklist · restore_backup · self_heal |
| 6 | `treasury.py` | 9 | allocate_budget · charge_model_invoke · charge_retraining · charge_storage · generate_financial_report · process_real_costs · reward_quality_report · reward_successful_training · reward_task_completion |

**ملاحظةٌ على الكتابةِ عبرَ التفويضِ**: اثنا عشرَ سطحًا منَ الـ41 لا تحملُ كتاباتٍ مباشرةً في جسدِها بل تكتبُ عبرَ `_log_event` أو عبرَ مناديها الداخليِّ (`writes_via`): `bootstrap · graceful_shutdown · health_check · launch_checklist · self_heal` (في system_life · 5) و`charge_model_invoke · charge_retraining · charge_storage · process_real_costs · reward_quality_report · reward_successful_training · reward_task_completion` (في treasury · 7 · بعضُها يكتبُ عبرَ `allocate_budget` أو `reward_*` الداخليِّ). **فالجردُ الرسميُّ يعدُّها أسطحَ كتابةٍ عامّةً غيرَ سياديّةٍ** — والتصميمُ أدناه يعبرُها جميعًا لأنَّ المقياسَ الرسميَّ هو الحكمُ.

---

## 2. نموذجُ الصلاحياتِ (جوهرُ التصميمِ)

### 2.1 الفاعلُ ومصدرُه
كلُّ هذه الأسطحِ عملياتٌ خدميّةٌ داخليةٌ في النواةِ التنفيذيّةِ (`federal/executive/services/…/governance/`) لا تعبرُ HTTP مباشرةً — الفاعلُ **الفرعُ التنفيذيُّ** (`EXECUTIVE`) كما في سابقةِ E1/WI-119: طرفٌ تابعٌ تخضعُ له كلُّ قاعدةٍ دستوريّةٍ مُلزِمةٍ ومانعةٍ. **استثناءٌ واحدٌ معلَنٌ**: `register_state` — فاعلُهُ **الملكُ** (`ROYAL`) عبرَ مسارِ المرسومِ الملكيِّ (Q-13 · § 3.1 أدناه).

### 2.2 الأفعالُ وتسميتُها (قرارُ التصميمِ — يُعرَضُ صراحةً)
**إضافةُ أسماءٍ جديدةٍ إلى `EXECUTIVE_ACTIONS` في `core/constitutional_engine/rules.py`** — في دفعةِ الشِّفرةِ لا في هذه الدفعةِ. السندُ: سابقةُ Q-18 (توسيعُ المعجمِ **تضييقٌ لا توسيعٌ** — كلُّ فعلٍ يُضافُ يصيرُ حصرًا للفرعِ التنفيذيِّ فيُمنعُ على الفروعِ الأخرى بـR-003-1). حيثُ يغطّي فعلٌ قائمٌ المعنى يُعادُ استعمالُهُ ولا يُخترَعُ اسمٌ موازٍ يلوّثُ دلالتَهُ.

**الجدولُ الحاكمُ — تعيينٌ صريحٌ لكلِّ سطحٍ منَ الـ41**:

| السطحُ | الفاعلُ | الفعلُ | الهدفُ | الأثرُ المعلَنُ | زرُّ الإيقافِ | مفتاحُ العمليّةِ | المعوِّضُ |
|---|---|---|---|---|---|---|---|
| `create_batch` | EXECUTIVE | `spawn_population` (قائمٌ) | `batch:{batch_id}` | CREATE صفُّ دفعةٍ | **المستوى 2** (صنفُ replicate) | `(batch, batch_id)` | حذفُ الصفِّ |
| `employ_batch` | EXECUTIVE | `dispatch_agent` (قائمٌ) | `batch:{batch_id}` | UPDATE حالةِ الدفعةِ | **المستوى 3** | `(batch_employ, batch_id, الحالةُ السابقةُ)` | إرجاعُ الحالةِ |
| `enroll_batch` | EXECUTIVE | `spawn_population` (قائمٌ) | `batch:{batch_id}` | CREATE صفُّ تسجيلٍ | **المستوى 2** | `(enroll, batch_id, agent_id, uuid)` | حذفُ الصفِّ |
| `graduate_batch` | EXECUTIVE | `release_agent` (قائمٌ) | `batch:{batch_id}` | UPDATE حالةِ الدفعةِ | **المستوى 4** (استعادةُ قدرةٍ) | `(graduate, batch_id, الحالةُ السابقةُ)` | إرجاعُ الحالةِ |
| `retire_agent` | EXECUTIVE | `contain_agent` (قائمٌ) | `agent:{agent_id}` | CREATE سجلُّ تقاعدٍ + أرشفةُ لقطةٍ + إيقافُ الوكيلِ | **بلا منعٍ** (احتواءٌ) | `(retire, agent_id, reason, الحالةُ السابقةُ, operation_id*)` | **معوِّضٌ يعيدُ الوكيلَ إلى حالتِهِ السابقةِ** (Q-26 · § 3.3) |
| `take_exam` | EXECUTIVE | `record_curriculum_step` (قائمٌ) | `exam:{exam_id}` | APPEND نتيجةِ امتحانٍ | **المستوى 1** (منهجُ تدريبٍ) | `(exam, exam_id, agent_id, uuid)` | حذفُ الإدخالِ |
| `approve_output` | EXECUTIVE | `activate_agent` (قائمٌ) | `output:{output_id}` | UPDATE حالةِ إخراجٍ | **المستوى 4** | `(approve, output_id, الحالةُ السابقةُ)` | إرجاعُ الحالةِ |
| `submit_output` | EXECUTIVE | `create_task` (قائمٌ) | `output:{output_id}` | CREATE/UPDATE صفُّ إخراجٍ | **المستوى 4** | `(submit, output_id, uuid)` | حذفُ الصفِّ |
| `evaluate_model` | EXECUTIVE | `train_model` (قائمٌ · المستوى 1) | `model:{model_id}` | APPEND نتيجةِ تقييمٍ | **المستوى 1** | `(eval, model_id, uuid)` | حذفُ الإدخالِ |
| `collect_experiences` | EXECUTIVE | `record_curriculum_step` (قائمٌ) | `exp:{exp_id}` | APPEND صفُّ تجربةٍ | **المستوى 1** | `(exp, exp_id, uuid)` | حذفُ الصفِّ |
| `complete_training` | EXECUTIVE | `release_agent` (قائمٌ) | `training:{training_id}` | UPDATE حالةِ تدريبٍ | **المستوى 4** | `(complete, training_id, الحالةُ السابقةُ)` | إرجاعُ الحالةِ |
| `start_training` | EXECUTIVE | `train_model` (قائمٌ · المستوى 1) | `training:{training_id}` | CREATE صفُّ تدريبٍ | **المستوى 1** | `(train, training_id, uuid)` | حذفُ الصفِّ |
| `promote_beta_to_alpha` | EXECUTIVE | `activate_agent` (قائمٌ) | `model:{model_id}` | UPDATE نسخةِ الإنتاجِ | **المستوى 4** (استعادةُ قدرةٍ) | `(promote, model_id, النسخةُ السابقةُ)` | إرجاعُ النسخةِ |
| `start_canary` | EXECUTIVE | `invoke_model` (قائمٌ) | `canary:{canary_id}` | CREATE صفُّ كنارٍ | **المستوى 1** (تجربةُ نموذجٍ) | `(canary, canary_id, uuid)` | حذفُ الصفِّ |
| `start_shadow` | EXECUTIVE | `invoke_model` (قائمٌ) | `shadow:{shadow_id}` | CREATE صفُّ ظلٍّ | **المستوى 1** | `(shadow, shadow_id, uuid)` | حذفُ الصفِّ |
| `create_session` | EXECUTIVE | `execute_task` (قائمٌ) | `session:{session_id}` | CREATE صفُّ جلسةٍ | **المستوى 4** | `(session, session_id, uuid)` | حذفُ الصفِّ |
| `check_rate` | EXECUTIVE | `log_isolated_action` (قائمٌ) | `rate:{key}` | APPEND عدّادِ معدّلٍ | — (رصدٌ) | `(rate, key, uuid)` | حذفُ الإدخالِ |
| `store_secret` | EXECUTIVE | **`store_secret`** (جديدٌ) | `secret:{key}` | CREATE/UPDATE صفُّ سرٍّ | **المستوى 5** (سرٌّ = أعلى حساسيةٍ) | `(secret, key, بصمةُ القيمةِ)` | إرجاعُ لقطةِ القيمةِ السابقةِ (أو حذفُ الصفِّ إن كانَ إنشاءً) |
| `issue_certificate` | EXECUTIVE | **`issue_certificate`** (جديدٌ) | `cert:{cert_id}` | CREATE صفُّ شهادةٍ | **المستوى 3** (منحُ ثقةٍ) | `(cert, cert_id, uuid)` | حذفُ الصفِّ |
| `verify_certificate` | EXECUTIVE | `log_isolated_action` (قائمٌ) | `cert:{cert_id}` | APPEND سجلُّ تحقّقٍ | — (رصدٌ) | `(verify, cert_id, uuid)` | حذفُ الإدخالِ |
| `send_message` | EXECUTIVE | `coordinate` (قائمٌ) | `msg:{message_id}` | CREATE صفُّ رسالةٍ | **المستوى 4** | `(msg, message_id, uuid)` | حذفُ الصفِّ |
| `assign_agent` | EXECUTIVE | `dispatch_agent` (قائمٌ) | `state:{state_id}/agent:{agent_id}` | CREATE صفُّ تعيينٍ | **المستوى 3** | `(assign, state_id, agent_id, uuid)` | حذفُ الصفِّ |
| `reactivate_state` | EXECUTIVE | `activate_agent` (قائمٌ) | `state:{state_id}` | UPDATE حالةِ الولايةِ (suspended→active) | **المستوى 4** (استعادةُ قدرةٍ أوقفها النظامُ) | `(reactivate, state_id, الحالةُ السابقةُ, operation_id*)` | إرجاعُ الحالةِ السابقةِ |
| `register_state` | **ROYAL** | `create_state` (قائمٌ · ملكيٌّ) | `state:{state_id}` | CREATE صفُّ ولايةٍ | **المستوى 5** (مرسومٌ ملكيٌّ) | `(create_state, state_id, decree_id)` | حذفُ الصفِّ |
| `suspend_state` | EXECUTIVE | `contain_agent` (قائمٌ) | `state:{state_id}` | UPDATE حالةِ الولايةِ (active→suspended) + **أثرٌ مُعلَنٌ** | **بلا منعٍ** (احتواءٌ = أداةُ الإيقافِ نفسُها) | `(suspend, state_id, الحالةُ السابقةُ, operation_id*)` | إرجاعُ الحالةِ السابقةِ |
| `bootstrap` | EXECUTIVE | `orchestrate` (قائمٌ) | `system:bootstrap` | APPEND سجلِّ حدثٍ (عبرَ `_log_event`) | **المستوى 4** | `(bootstrap, uuid)` | حذفُ الإدخالِ |
| `create_backup` | EXECUTIVE | **`create_backup`** (جديدٌ) | `backup:{backup_id}` | CREATE ملفُّ نسخةٍ احتياطيّةٍ | — (أداةُ استردادٍ لا تُمنَعُ) | `(backup, backup_id, uuid)` | حذفُ الملفِّ |
| `graceful_shutdown` | EXECUTIVE | `orchestrate` (قائمٌ) | `system:shutdown` | APPEND سجلِّ حدثٍ | **بلا منعٍ** (إيقافٌ نظاميٌّ) | `(shutdown, uuid)` | حذفُ الإدخالِ |
| `health_check` | EXECUTIVE | `run_health_check` (قائمٌ) | `system:health` | APPEND سجلِّ فحصٍ | — (رصدٌ) | `(health, uuid)` | حذفُ الإدخالِ |
| `launch_checklist` | EXECUTIVE | `orchestrate` (قائمٌ) | `system:launch` | APPEND سجلِّ حدثٍ | — (رصدٌ) | `(launch, uuid)` | حذفُ الإدخالِ |
| `restore_backup` | EXECUTIVE | **`restore_backup`** (جديدٌ) | `backup:{backup_id}` | استبدالُ حالةِ النظامِ من نسخةٍ | **المستوى 5** (استبدالُ حالةٍ) | `(restore, backup_id, بصمةُ الحالةِ الحاليّةِ)` | استعادةُ الحالةِ السابقةِ من لقطةٍ |
| `self_heal` | EXECUTIVE | **`self_heal`** (جديدٌ) | `system:heal:{component}` | APPEND سجلِّ علاجٍ + كتاباتُ المعالجةِ | **المستوى 4** | `(heal, component, uuid)` | إرجاعُ الحالاتِ المعالجةِ |
| `allocate_budget` | EXECUTIVE | `allocate_budget` (قائمٌ) | `state:{state_id}/budget` | UPDATE ميزانيّةِ ولايةٍ | **المستوى 3** | `(alloc, state_id, المبلغُ السابقُ)` | إرجاعُ المبلغِ السابقِ |
| `charge_model_invoke` | EXECUTIVE | `invoke_model` (قائمٌ) | `ledger:{entry_id}` | APPEND قيدُ محاسبةٍ | — (تدقيقٌ) | `(charge, entry_id, uuid)` | حذفُ القيدِ |
| `charge_retraining` | EXECUTIVE | `train_model` (قائمٌ) | `ledger:{entry_id}` | APPEND قيدُ محاسبةٍ | — | `(charge, entry_id, uuid)` | حذفُ القيدِ |
| `charge_storage` | EXECUTIVE | `invoke_tool` (قائمٌ) | `ledger:{entry_id}` | APPEND قيدُ محاسبةٍ | — | `(charge, entry_id, uuid)` | حذفُ القيدِ |
| `generate_financial_report` | EXECUTIVE | `orchestrate` (قائمٌ) | `report:{report_id}` | CREATE صفُّ تقريرٍ | — (رصدٌ) | `(report, report_id, uuid)` | حذفُ الصفِّ |
| `process_real_costs` | EXECUTIVE | `orchestrate` (قائمٌ) | `ledger:{batch}` | APPEND قيودُ تكاليفَ | — | `(costs, batch, uuid)` | حذفُ القيودِ |
| `reward_quality_report` | EXECUTIVE | **`reward_agent`** (جديدٌ) | `reward:{reward_id}` | APPEND قيدُ مكافأةٍ | **المستوى 4** (صرفٌ ماليٌّ) | `(reward, reward_id, uuid)` | حذفُ القيدِ |
| `reward_successful_training` | EXECUTIVE | `reward_agent` (جديدٌ) | `reward:{reward_id}` | APPEND قيدُ مكافأةٍ | **المستوى 4** | `(reward, reward_id, uuid)` | حذفُ القيدِ |
| `reward_task_completion` | EXECUTIVE | `reward_agent` (جديدٌ) | `reward:{reward_id}` | APPEND قيدُ مكافأةٍ | **المستوى 4** | `(reward, reward_id, uuid)` | حذفُ القيدِ |

**قواعدُ التسميةِ الملزمةُ في الشِّفرةِ**:
1. الاسمُ نتيجةُ المعنى لا مصدرُ الإذنِ — لا رفعَ صلاحيّاتٍ خارجَ العبورِ المُعلَنِ.
2. أعمالُ الاحتواءِ والرصدِ (`suspend_state` · `retire_agent` · `check_rate` · `verify_certificate` · `health_check` · `create_backup`) تبقى ممكنةً في كلِّ مستوياتِ الإيقافِ — منعُ أداةِ الاحتواءِ عندَ الإيقافِ نقضٌ لغايةِ الإيقافِ نفسِهِ (سابقةُ E1 قاعدة 3).
3. الأسماءُ الجديدةُ الثلاثةُ عشرَ (المعلَّمةُ «جديدٌ») تُعرَضُ على المالكِ في § 8 — إن اعترضَ فوُقِّفَت شفرةُ الأفعالِ الجديدةِ حتى الحسمِ (سابقةُ E1 § 5).

### 2.3 معالجةُ التعشيشِ (النمطُ: «الخارجيُّ يُعلنُ الآثارَ ويُنادي نوًى خاصّةً» — Q-9 § 2.3)
- **عبورٌ واحدٌ لكلِّ عمليّةِ**: السطحُ الخارجيُّ يعلنُ **جميعَ** آثارِ العمليّةِ في `declared_effects` ويعبرُ مرةً واحدةً. الكتاباتُ الداخليّةُ (`_log_event` · `_insert_*` · `allocate_budget` الداخليُّ في treasury) تُستخرَجُ نوىً خاصّةً بلا عبورٍ (سابقةُ J2/J3 `docket._insert_proceeding`).
- الكاشفُ المنفَّذُ في الحدِّ (`NestedSovereignCallError` في `enforcement_boundary.py`) يظلُّ حارسَ النمطِ — لا يُمَسُّ ولا يُوسَّعُ استثناءُهُ المسجَّلُ.
- **مواضعُ التعشيشِ المتوقَّعةُ**: `treasury.charge_*` ينادي `allocate_budget` داخليًّا (نواةٌ خاصّةٌ لا عبورانِ) · `system_life.self_heal` ينادي `reactivate_state` (انظر § 3.2) · `expansion.retire_agent` ينادي `set_lifecycle_state` عبرَ health (نواةٌ خاصّةٌ).

### 2.4 مفاتيحُ العمليّاتِ (سابقةُ WI-082/Q-74)
- **إعادةُ المحاولةِ للعمليّةِ نفسِها** ⇒ المفتاحُ نفسُهُ ⇒ إعادةٌ (replay) لا يُطبَّقُ الأثرُ مرتَينِ.
- **عمليّةٌ جديدةٌ على الكيانِ نفسِهِ** ⇒ مفتاحٌ جديدٌ يحملُ الحالةَ السابقةَ وبصمةَ القيمِ (المعلَّمُ بـ`operation_id*` يتبعُ سابقةَ Q-74 المعتَمَدةَ في E1).
- `retire_agent` يحملُ `reason` في المفتاحِ لأنَّ التقاعدَ مرتَينِ بسببينِ مختلفَينِ عمليّتانِ.

---

## 3. القراراتُ الأربعةُ المحسومةُ — تطبيقُها في التصميمِ

### 3.1 Q-13 — `register_state` مسارُ مرسومٍ ملكيٍّ
- `register_state` (state_runtime.py:228) هوَ دستوريًّا **`create_state`** — والفعلُ موجودٌ أصلًا في المعجمِ الملكيِّ (`core/sovereignty/prerogatives.py:33`) ومقيدٌ بـR-004-1 (75% موافقةَ مجلسٍ + توقيعٌ بشريٌّ).
- **التصميمُ**: العبورُ بفاعلِ `ROYAL` معَ `royal_decree` مُوقَّعٍ يخصُّ الفعلَ `create_state` والهدفَ `state:{state_id}` (المدققُ في `core/constitutional_engine/rules.py:572-581` يرفضُ مرسومًا لا يطابقُ الفعلَ). لا بوّابةَ بشريّةً إضافيّةً — المرسومُ المُوقَّعُ هوَ البوّابةُ.
- **حدودٌ**: لا يُمَسُّ `royal/main.py` (K1) · لا يُعدَّلُ المعجمُ الملكيُّ (الفعلُ موجودٌ) · المُطبِّقُ الداخليُّ يبقى نواةً خاصّةً.

### 3.2 Q-14 — إيقافُ/إعادةُ الولايةِ + مراجعةُ `system_life.py:240`
- `suspend_state` و`reactivate_state` اختصاصٌ تنفيذيٌّ محكومٌ **بلا بوابةٍ بشريّةٍ** — عبورٌ بفاعلِ `EXECUTIVE` عبرَ الحدِّ.
- **الشرطُ 1 — أثرٌ مُعلَنٌ لكلِّ إيقافٍ**: `declared_effects` في عبورِ `suspend_state` يحملُ `state:{state_id}` والحالةَ السابقةَ والسببَ — ويُسجَّلُ في سجلِّ العبورِ (المرآة).
- **الشرطُ 2 — تغطيةُ قاطعِ التشغيلِ**: `suspend_state` بلا منعٍ (احتواءٌ) و`reactivate_state` محجوزٌ بالمستوى 4 (استعادةُ قدرةٍ أوقفها النظامُ) — فالقاطعُ يمنعُ إعادةَ التفعيلِ في المستوياتِ 5 ولا يمنعُ الإيقافَ أبدًا. **[تصحيحٌ مؤرَّخٌ · W-721 · 2026-10-28]: «في المستوياتِ 5» خطأٌ — المقيسُ حرفيًّا أنَّ المنعَ عندَ المستويينِ 4 و5 (≥ 4) · انظر § 9.3.**
- **الشرطُ 3 — مراجعةُ إعادةِ التفعيلِ التلقائيِّ في `system_life.py:240`**: المقيسُ اليومَ: `self_heal(component="states")` يمرُّ على كلِّ الولاياتِ المعلَّقةِ ويُعيدُ تفعيلَها **بلا شرطٍ** — وهذا يلغي عمليًّا كلَّ إيقافٍ تنفيذيٍّ محكومٍ (الإيقافُ قرارٌ والمُعالِجُ ينقضُه في أولِ جولةِ علاجٍ). **اقتراحٌ غيرُ معتمدٍ يُعرَضُ على المالكِ** (ليسَ نصَّ Q-14 بل استنتاجٌ من شرطِهِ الثالثِ): `self_heal` **لا يعيدُ تفعيلَ ولايةٍ عُلِّقَت بعبورٍ محكومٍ** إلا إذا كانَ سببُ التعليقِ في سجلِّ العبورِ من صنفِ «عطلٍ» لا «قرارٍ» — يُقرأُ سببُ الإيقافِ من سجلِّ العبورِ (الأثرُ المعلَنُ للشرطِ 1) قبلَ أيِّ إعادةِ تفعيلٍ. فإن كانَ القرارُ «احتواءً» (منَ المستوياتِ 1–3) بقيتِ الولايةُ معلَّقةً وسُجِّلَ `noop` في سجلِّ العلاجِ. هذا يُعرَضُ على المالكِ في § 8 لأنَّهُ سلوكٌ مُغيِّرٌ للمعالجِ القائمِ.

### 3.3 Q-26 — `retire_agent` بمُعوِّضٍ يعيدُ الوكيلَ
- المقيسُ اليومَ: `retire_agent` (expansion.py:935) يؤرشفُ لقطةَ الوكيلِ (`archived_data`) ويُنشئُ سجلَّ تقاعدٍ ويُوقفُ الوكيلَ — ولا مسارَ عودةٍ.
- **التصميمُ**: المعوِّضُ في عبورِ `retire_agent` **يعيدُ الوكيلَ**: يحذفُ سجلَّ التقاعدِ ويُعيدُ الوكيلَ منَ اللقطةِ المؤرشفةِ إلى **حالتِهِ السابقةِ قبلَ التقاعدِ** (لا إلى ACTIVE افتراضًا · نواةٌ خاصّةٌ لا تمسُّ `royal/main.py:restore_agent` الملكيَّ — K1). القيدُ: إن فشلَ استردادُ اللقطةِ فالمعوِّضُ يُسجِّلُ الفشلَ ولا يدَّعي الإعادةَ (سابقةُ `health_failures=0` في expansion.py — لا دعوى صحّةٍ لم تُقَسْ).
- **حدودٌ**: `royal/main.py` (K1) لا يُمَسُّ · `restore_agent` الملكيُّ يبقى مسارَ الملكِ الوحيدَ للوكيلِ الممسوحِ.

### 3.4 Q-23 — `suspend_policy` و`vote` في المعجمِ التشريعيِّ
- **التنفيذُ** (في دفعةِ الشِّفرةِ): إضافةُ `suspend_policy` و`vote` إلى `LEGISLATIVE_ACTIONS` في `core/constitutional_engine/rules.py:32` (القائمُ: legislate · enact_policy · amend_policy · repeal_policy).
- `suspend_policy` موجودٌ أصلًا في `FORBIDDEN_JUDICIAL_ACTIONS` (jurisdiction.py:114) — فإضافتُهُ إلى المعجمِ التشريعيِّ **يكمِّلُ الحصرَ** (القضاءُ ممنوعٌ والتنفيذُ ممنوعٌ بـR-003-1 والتشريعُ هو المالك). `vote` جديدٌ على المعجمِ كاملًا (لا يظهرُ في أيِّ معجمٍ اليومَ) — يُعرَضُ على المالكِ في § 8.
- **حدودٌ**: لا مساسَ بمعجمِ القضاءِ ولا التنفيذِ · لا سلوكَ جديدًا في هذه الدفعةِ — المعجمُ وحدهُ (السلوكُ في بنودٍ لاحقةٍ).

---

## 4. خطةُ الفحوصِ (تُنفَّذُ في دفعاتِ الشِّفرةِ — خمسةُ أصنافٍ)
1. **الرفضُ قبلَ أيِّ كتابةٍ مُلتزَمَةٍ**: منعُ الفعلِ (زرُّ إيقافٍ بالمستوى المانعِ · فاعلٌ لا يملكُه) ⇒ لا `add` ولا `commit` ولا قيدٌ في دفترِ الذرّيّةِ.
2. **نجاحُ الفاعلِ الصحيحِ بالأثرِ المقصودِ**: كلُّ سطحٍ يكتبُ عبرَ العبورِ ويُعيدُ نتيجتَهُ.
3. **الطفرةُ (سابقةُ WI-082/WI-111)**: نزعُ الحارسِ عن كلِّ سطحٍ يُسقِطُ فحصَهُ — طفرةٌ لكلِّ سطحٍ منَ الـ41.
4. **عدمُ تكرارِ الأثرِ عندَ الإعادةِ**: إعادةُ الإرسالِ إعادةٌ واحدةٌ · `active→suspended→active` عمليّتانِ.
5. **التعويضُ على المسارِ الحقيقيّ**: فشلٌ بعدَ الحارسِ ⇒ المعوِّضُ يُرجعُ الحالةَ بلا محوِ تحديثٍ أحدثَ · ومعوِّضُ `retire_agent` **يعيدُ الوكيلَ** (Q-26) ومعوِّضُ `register_state` يحذفُ صفَّ الولايةِ.

**فحوصٌ خاصةٌ بالقراراتِ الأربعةِ**:
- **Q-13**: `register_state` بلا مرسومٍ ⇒ رفضٌ · بمرسومٍ لا يخصُّ `create_state` ⇒ رفضٌ (المدققُ rules.py:578) · بمرسومٍ صحيحٍ ⇒ قبولٌ.
- **Q-14**: `suspend_state` يسجِّلُ أثرًا مُعلَنًا · `self_heal` لا يُعيدُ ولايةً عُلِّقَت بقرارٍ (§ 3.2) · القاطعُ بالمستوى 5 يمنعُ `reactivate_state` ولا يمنعُ `suspend_state`.
- **Q-26**: فشلٌ بعدَ حارسِ `retire_agent` ⇒ الوكيلُ يعودُ منَ اللقطةِ · `royal/main.py` لم يُمَسَّ (فحصُ فرقِ الملفّاتِ).
- **Q-23**: `suspend_policy` و`vote` ALLOW لـLEGISLATIVE وDENY لـEXECUTIVE/JUDICIAL/ROYAL (مسبارُ جدارِ الاختصاصِ).

---

## 5. شطرُ الدفعاتِ (تُقترحُ للدمجِ الصغيرِ السريعِ)
1. **المعجمُ والأثرُ المعلَنُ**: الأفعالُ الجديدةُ في `EXECUTIVE_ACTIONS` + `LEGISLATIVE_ACTIONS` (+Q-23) + مستوياتُ الإيقافِ الجديدةُ في `KILL_SWITCH_BLOCKS`.
2. **state_runtime + system_life** (12 سطحًا · **[W-721]: 11 بعدَ خروجِ restore_backup** — § 9.4): Q-13 + Q-14 + مراجعةُ `self_heal:240`.
3. **expansion** (8 أسطح): Q-26 (retire_agent).
4. **learning_cycle + security** (12 سطحًا · **[W-721]: 11 بعدَ خروجِ store_secret** — § 9.4).
5. **treasury** (9 أسطح · **[W-721]: خرجت إلى M1** بالتعديلِ (ب) — § 9.2).
6. القياسُ بعدَ كلِّ دفعةٍ (القبولُ: `sovereign_write_inventory.py` — الفرقُ بينَ 121 والقياسِ الجديدِ يُقيَّدُ · الإسقاطُ 80 بعدَ G1 كاملةً).

---

## 6. ما لا يُفعَلُ في هذا التصميمِ (حدودٌ صريحةٌ)
- **لا شِّفرةَ في هذه الدفعةِ** — التصميمُ وحدَهُ (DISC-137).
- **K1 لا يُمَسُّ**: `royal/main.py` وكلُّ صفٍّ منَ الصفَّينِ 24–25 (الملكيُّ) · لا مساسَ بـ`restore_agent` الملكيِّ.
- **لا تعديلَ لمعجمِ الدستورِ في هذه الدفعةِ** — التسميةُ قرارُ تصميمٍ يُعرَضُ، والتنفيذُ في دفعةِ الشِّفرةِ.
- **لا مساسَ بـ`persistent.py` ولا بتعريفِ D-4 ولا بمعيارِ WI-115 (4)**.
- **لا جولةَ مجلسٍ جديدةً** قبلَ قرارِ المالكِ (توجيهُ الطابورِ W-712/W-713).
- **لا حرقَ موعودًا**: 80 إسقاطٌ مشروطٌ — القياسُ بعدَ الشِّفرةِ هو الحكمُ.
- **لا VERIFIED ولا CLOSED** — البندُ ينتقلُ READY→RESERVED في هذه الدفعةِ فقط.

---

## 7. ترتيبُ الالتزاماتِ (ما بعدَ هذه الدفعةِ — تسلسلُ الطابورِ W-712/W-713)
1. هذه الوثيقةُ (W-715) + حجزُ WI-120 (READY→RESERVED).
2. **تحليلُ WI-118** (تحليلٌ قياسيٌّ بلا شِّفرةٍ — قرارُ المالكِ في التوجيهِ 24 § 1) ثمَّ **تصميمُ WI-116** — تسلسلُ الطابورِ لا ينتظرُ قرارَ المالكِ على تصميمِ G1.
3. **قرارُ المالكِ على تصميمِ G1** (§ 8) — وبعدهُ: دفعةٌ ورقيّةٌ تنقلُ WI-120 إلى IN_PROGRESS (DISC-137) ثمَّ دفعاتُ الشِّفرةِ (الشطرُ المقترحُ في § 5) معَ فحوصِ الأصنافِ الخمسةِ وطفراتِ الـ41.
4. القياسُ بعدَ كلِّ دفعةٍ (القبولُ بقياسِ الأداةِ).
5. جولةُ مجلسٍ واحدةٌ (بعدَ قرارِ المالكِ لا قبلهُ) على الدفعةِ كلِّها.

---

## 8. القرارُ المعروضُ على المالكِ (صريحٌ)
**أربعةُ قراراتٍ** معروضةٌ على المالكِ في تقريرِ هذه الجلسةِ (لا تُنفَّذُ شفرةٌ قبلَ الحسمِ):

1. **اعتمادُ التصميمِ** (أو تعديلُهُ): نموذجُ الصلاحياتِ في § 2 للأسطحِ الـ41 — خاصةً مستوياتُ الإيقافِ والمعوّضاتِ.
2. **الأسماءُ الجديدةُ الثمانيةُ** (ستةٌ تنفيذيةٌ في `EXECUTIVE_ACTIONS`: `store_secret · issue_certificate · create_backup · restore_backup · self_heal · reward_agent` + اسمانِ تشريعيانِ في `LEGISLATIVE_ACTIONS`: `suspend_policy · vote` — **وكلاهما محسومانِ أصلًا بقرارِ Q-23** ولا يُعادُ عرضُهُما كسؤالٍ جديدٍ): توسيعٌ **مضيِّقٌ** على سابقةِ Q-18. **إن اعترضَ المالكُ فوُقِّفَت شفرةُ الأفعالِ الجديدةِ حتى الحسمِ** — ولا يُتجاوَزُ الاعتراضُ باختيارِ أسماءٍ بديلةٍ هاربةٍ.
3. **سلوكُ `self_heal` المُعدَّلُ** (§ 3.2): عدمُ إعادةِ تفعيلِ ولايةٍ عُلِّقَت بقرارٍ محكومٍ — تغييرٌ لسلوكِ المعالجِ القائمِ (اليومَ يُعيدُ الكلَّ بلا شرطٍ).
4. **الإذنُ بفتحِ جولةِ مجلسٍ** على دفعةِ G1 كاملةً (تصميمًا وشِّفرةً وأدلةً) بعدَ اكتمالِ دفعاتِ الشِّفرةِ — فلا جولةَ قبلَ هذا القرارِ.

**ما يتعطَّلُ حتى الحسمِ**: دفعةُ الشِّفرةِ الأولى (المعجمُ) وجميعُ ما بعدها منَ الشطرِ المقترحِ في § 5.
**ما يُنفَّذُ بعدَ القرارِ مباشرةً**: انتقالُ WI-120 إلى IN_PROGRESS ثمَّ دفعةُ المعجمِ (§ 5.1).

---

## 9. اعتمادُ المالكِ بتعديلاتٍ ثلاثة — تعديلٌ مؤرَّخٌ (2026-10-28 · W-721 · التوجيهُ 27 § 1)

النصُّ الحرفيُّ في [`OWNER-DECISIONS-D28.md`](../governance/work/HANDOFFS/OWNER-DECISIONS-D28.md). وما فوقَ هذا القسمِ باقٍ
بنصِّه، والتصحيحاتُ عليه بعلاماتٍ مؤرَّخةٍ تُحيلُ إلى هنا.

### 9.1 (أ) خارجَ G1 — دَينٌ إلى تصميمٍ مستقلّ
- **`store_secret`**: معوِّضُه في § 2.2 («إرجاعُ لقطةِ القيمةِ السابقة») يضعُ سرًّا في سجلِّ العبور، وهذا ممنوعٌ:
  «لا تُخزَّن قيمة سر في أي أثر أو معوِّض، بصمة فقط». ويبقى الاسمُ خارجَ المعجمِ حتى يصدرَ تصميمُه.
- **`restore_backup`**: يستبدلُ حالةَ النظام، ويحتاجُ تصميمًا يقرِّرُ هل تلزمُه موافقةٌ بشريّة، وليسَ له مسارُ HTTP يحملُها.
  ويبقى الاسمُ كذلكَ خارجَ المعجم.

### 9.2 (ب) إلى M1 — الخزانةُ التسعةُ وreward_agent
الأسطحُ التسعةُ في `treasury.py` (allocate_budget · charge_model_invoke · charge_retraining · charge_storage ·
generate_financial_report · process_real_costs · reward_quality_report · reward_successful_training · reward_task_completion)
تحملُ المالَ المتعشِّشَ الذي قرَّرَه Q-9. فلا تُعبَرُ إلّا بعدَ كاشفِ التعشيشِ وتصميمِ M1، وتحتَ جولةٍ بأعلى فئة.
والاسمُ `reward_agent` يتبعُها، فلا يدخلُ المعجمَ في دفعةِ G1.

### 9.3 (ج) دلالةُ «المستوى N» — مقيسةٌ حرفيًّا
القاعدةُ `_r008_2` في `core/constitutional_engine/rules.py:485-498` تمرُّ على `range(1, min(level, 5) + 1)` وتمنعُ
إن وُجِدَ الفعلُ في أيٍّ منها. **فـ«المستوى N» يعني المنعَ عندَ كلِّ مستوًى ≥ N، تراكميًّا.** والمسبارُ في
`docs/audit/evidence/W-721/killswitch_probe.py`، ومخرجُه الحرفيُّ في `evidence/W-721/measure.txt`:

```
activate_agent @ level 3: ALLOW
activate_agent @ level 4: BLOCK — زر التوقف عند المستوى 4، والفعل «activate_agent» مُجمَّد ابتداءً من المستوى 4.
activate_agent @ level 5: BLOCK — زر التوقف عند المستوى 5، والفعل «activate_agent» مُجمَّد ابتداءً من المستوى 4.
```

فـ`reactivate_state` (الفعلُ `activate_agent`) يُمنَعُ في المستويينِ 4 و5، وعبارةُ «في المستوياتِ 5» في § 3.2 خطأٌ
صُحِّحَ هناكَ بعلامة. وبهذه الدلالةِ نفسِها تُقرأُ كلُّ خانةِ «زرُّ الإيقافِ» في جدولِ § 2.2.

### 9.4 إعادةُ العدِّ — مقيسةٌ لا معدودةٌ باليد
الأمرُ `.venv/bin/python docs/audit/evidence/W-721/surface_recount.py` (المصدرُ `write_inventory_p13.json`):

| الدفعة | الأسطح | المستثنى |
|---|---|---|
| 2 · state_runtime + system_life | **11** (5 + 6) | restore_backup ⇒ دَين |
| 3 · expansion | **8** | — |
| 4 · learning_cycle + security | **11** (7 + 4) | store_secret ⇒ دَين |
| المجموعُ لـ G1 | **30** = 41 − 9 (M1) − 2 (دَين) | — |

والإسقاطُ بعدَ G1 كاملةً يصيرُ **91** لا 80 (121 − 30)، وهو إسقاطٌ لا وعد: يُقاسُ D-4 بأداةِ الجردِ بعدَ كلِّ دفعة.

### 9.5 المعجمُ في دفعةِ W-722 (§ 5.1) بعدَ التعديل
- `EXECUTIVE_ACTIONS` ⇐ `issue_certificate` · `create_backup` · `self_heal` (ثلاثةٌ لا ستّة).
- `LEGISLATIVE_ACTIONS` ⇐ `suspend_policy` · `vote` (محسومانِ بـQ-23).
- `KILL_SWITCH_BLOCKS` ⇐ `issue_certificate` في المستوى 3 · `self_heal` في المستوى 4 · و`create_backup` بلا منع.
- **[W-722 · 2026-10-28] شُفِّرَ** في `rules.py` بفحوصِ `tests/constitutional/test_g1_vocabulary.py` (15) — الأدلّةُ `evidence/W-722/`.

### 9.6 self_heal — معتمَدٌ بشرط
«لا يُعيد تفعيل ولاية عُلِّقت بقرار محكوم.» وشرطُ القبولِ في الدفعةِ 2 ثلاثةُ أمور: سجلٌّ صريحٌ يميِّزُ الإيقافَ المحكوم ·
وما عُلِّقَ تلقائيًّا (بلا قرار) يُعادُ تفعيلُه كما كان · وفحصٌ يُثبتُ الحالتين.

### 9.7 المجلس
جولةٌ واحدةٌ على دفعاتِ G1 (1–4) وWI-116 بعدَ اكتمالِ دفعاتِ الشِّفرة، تُجمَعُ أحكامُها في الجلسةِ نفسِها (Q-72).
فالبندُ 4 في § 8 حُسِم، والحدُّ «لا جولةَ مجلسٍ جديدةً قبلَ قرارِ المالك» في § 6 زالَ موجبُه بالقرار.

### 9.8 ملحقُ تصميمِ الدفعةِ 2 — قبلَ الشِّفرة (مؤرَّخ · W-723 · 2026-10-28)
ثلاثُ فجواتٍ قِيسَت عندَ بدءِ الدفعةِ 2 ولم يغطِّها نصُّ § 3 و§ 5، فتُسَدُّ هنا ورقًا قبلَ أيِّ شِفرةٍ («لا شفرة قبل التصميم»):

**9.8.1 قناةُ المرسومِ في الجسر (Q-13).** § 3.1 يشترطُ عبورَ `register_state` بفاعلِ `ROYAL` ومرسومٍ موقَّع، والمقيسُ أنَّ
`ConstitutionalAuthorizer._request` (`sovereignty_bridge.py`) يبني `ActionRequest` بلا `royal_decree`، وأنَّ `classify`
(`core/sovereignty/authority.py`) يرفعُ `ROYAL_COMMAND_UNSIGNED` لكلِّ أمرٍ ملكيٍّ بلا مرسوم — فلا مسارَ ملكيًّا عبرَ الجسرِ اليوم.
- **التصميم**: وسيطٌ اختياريٌّ واحدٌ `royal_decree=None` في `guard_declared` يُركَّبُ على الطلبِ **بعدَ** `_request` بـ`dataclasses.replace`،
  فتوقيعُ `_request` لا يتغيّرُ (المُصرِّحاتُ الفرعيّةُ في الاختبارات تتجاوزُه بثلاثةِ وسائط).
- **الجسرُ لا يتحقّقُ ولا يُقرِّر**: التحقّقُ كلُّه في `classify` (الفعلُ يطابقُ · التاجُ منصَّبٌ · التوقيعُ يثبت) — فالوسيطُ نقلٌ لا سلطة،
  ومرسومٌ في يدِ فاعلٍ غيرِ ملكيٍّ يرفعُ `DECREE_PRESENTED_BY_NON_ROYAL` كما هو.
- **ربطُ الهدف**: `classify` يطابقُ الفعلَ لا الهدف (authority.py — المقيس)، فيرفضُ السطحُ قبلَ العبورِ مرسومًا هدفُه غيرُ `state:{state_id}`.
- `register_state` يعبرُ بمُصرِّحٍ بفاعلِ `ROYAL` **يُمرَّرُ صريحًا** إلى `StateRuntime(royal_authorizer=…)` ولا يُبنى داخلَ الخدمة
  (سابقةُ Q-19 مفحوصةً في `test_2a_precedent_correction.py::TestN2ActorIsTruthful`) · وبلا تمريرٍ يعبرُ بالمُصرِّحِ التنفيذيِّ
  فيرفضُه الدستورُ (المقيسُ: `create_state` لـ`EXECUTIVE` ⇒ DENY بـR-004-1 · R-010-1 · R-010-5) · لا يُمَسُّ `royal/main.py` (K1) ولا المعجمُ الملكيّ.
- R-004-1 (75% + توقيعٌ بشريّ) في المسارِ السياديِّ **مُخبِرٌ لا مانع** (gateway.py: «لا فرعَ في هذا المسارِ يرفعُ») — فالمرسومُ هوَ البوّابةُ كما قرَّرَ § 3.1.

**9.8.2 نطاقُ آثارِ self_heal.** الهدفُ في جدولِ § 2 `system:heal:{component}` والمعالجةُ تمسُّ `state:{id}` — و`in_scope` (contract.py)
يرفضُ أثرًا خارجَ الهدفِ (`EffectOutOfScopeError`). **التصميم**: كلُّ إعادةِ تفعيلٍ أثرٌ مُعلَنٌ موردُه `system:heal:states/state:{id}` (داخلَ الهدف)
ووصفُه يُسمّي الصفَّ والانتقالَ، ومعوِّضٌ لكلٍّ يُرجعُ الحالةَ السابقة · وسجلُّ الحدثِ أثرٌ `CREATE` (صفٌّ جديدٌ — `EffectKind` بلا `APPEND`، المقيسُ في contract.py) موردُه `system:heal:{component}/event:{id}`.
والمعالجةُ تمرُّ بنواةٍ خاصّةٍ في `StateRuntime` لا بـ`reactivate_state` المحروسِ (`NestedSovereignCallError` — § 5.3).
والسجلُّ الصريحُ (§ 9.6) جدولٌ جديدٌ `state_suspension_records` يُنشئُه `create_all` — لا عمودَ يُضافُ إلى `federal_states` فتنكسرَ قاعدةٌ قائمة.
«المحكومُ» = إيقافٌ عبرَ `suspend_state` المحروسِ (سجلٌّ نشطٌ) · «التلقائيُّ» = ولايةٌ معلَّقةٌ بلا سجلٍّ نشط (المقيسُ: لا مسارَ تعليقٍ آخرَ في الشِّفرةِ اليوم).

**9.8.3 تعارضٌ مقيسٌ في جدولِ § 2 — يُرفَعُ للمالك (Q-76) ولا يُحسَمُ هنا.** `graceful_shutdown` («بلا منعٍ») و`launch_checklist` («رصدٌ»)
مسنَدانِ إلى `orchestrate`، و`orchestrate` في `KILL_SWITCH_BLOCKS[4]` — فالمقيسُ أنّهما يُمنَعانِ عندَ ≥4، خلافًا لعمودِ القاطعِ ولـ§ 5 بند 2.
تُنفَّذُ الدفعةُ بعمودِ الفعلِ كما هو (لا اسمَ معجمٍ جديدًا بلا قرار) ويُثبَّتُ السلوكُ المقيسُ بفحصٍ يُسمّي Q-76،
والأثرُ التشغيليُّ اليومَ صفرٌ لأنَّ الجسرَ لا يحقنُ `kill_switch_level` (DISC-099/WI-085).

**9.8.4 [W-723 · 2026-10-28] شُفِّرَ** بالتصميمِ أعلاه في `state_runtime.py` و`system_life.py` و`sovereignty_bridge.py` (وسيطُ `royal_decree`)،
بفحوصِ `federal/executive/services/tests/test_w723_g1_state_runtime_system_life.py` (54). المقيسُ: أحدَ عشرَ سطحًا محروسًا و`restore_backup`
وحدَه غيرُ محروسٍ (دَينُ § 9.1) · D-4 121 ← 110 (`evidence/W-723/`). وانحرافانِ مُعلَنانِ عن نصِّ الملحقِ لا عن معناه:
- المُصرِّحُ التنفيذيُّ الافتراضيُّ لـ`FederalMessageBus` و`SystemLifecycle` يُؤخَذُ من `get_authorizer()` في الجسرِ (موضعُ بناءٍ قائمٌ معدودٌ) لا بموضعِ بناءٍ
  جديد — فعدُّ المواضعِ الافتراضيّةِ في `tests/governance/test_q3_branch_declaration_surface.py` يبقى 4 كما هو.
- الصنفُ 5 (المعوِّض) يُقاسُ بانكسارِ مرحلةِ التثبيتِ **بعدَ** عودةِ المُطبِّقِ (نمطُ E1 · test_e1_13) وبفشلِ الأثرِ الثاني في self_heal المتعدّدِ الآثار.
  أمّا فشلٌ **داخلَ** مُطبِّقٍ وحيدِ الأثرِ (كتابةٌ ثمَّ سقوطٌ قبلَ العودة) فلا يُعوَّضُ آليًّا — دَينُ 2A (test_2a G-7) كما هو، لا يُزعَمُ هنا سدُّه.

### 9.9 ملحقُ تصميمِ الدفعةِ 3 (expansion) والمعجمِ الصغير — قبلَ الشِّفرة (مؤرَّخ · W-724 · 2026-10-29)

**9.9.1 المعجمُ بقرارِ Q-76 (D29).** يدخلُ `graceful_shutdown` في `EXECUTIVE_ACTIONS` ولا يدخلُ `KILL_SWITCH_BLOCKS` عندَ أيِّ
مستوى (توسيعٌ مضيِّقٌ على سابقةِ Q-18: يصيرُ حصرًا للتنفيذِ فيُمنَعُ على غيرِه بـR-003-1). ويتحوّلُ إليه
`SystemLifecycle.graceful_shutdown`؛ و`launch_checklist` باقٍ على `orchestrate` (①). والفحصُ: المستوى 5 لا يمنعُ الإيقافَ
النظاميَّ، ويمنعُ `launch_checklist` عندَ 4 و5، وفرعٌ تشريعيٌّ يطلبُ `graceful_shutdown` يُرفَض.

**9.9.2 تعارضٌ مقيسٌ يوقفُ سطحين (Q-77 · PENDING_OWNER).** `create_batch` و`enroll_batch` مُسنَدانِ في § 2.2 إلى
`spawn_population`، وهو في `HUMAN_GATED_ACTIONS` فيمنعُه R-001-1 بلا موافقةٍ بشريّة، ولا قناةَ في الجسرِ تضعُها
(`evidence/W-724/probe_expansion_actions.py`). فلا يُعبَرانِ في هذه الدفعة ولا يُنزَلانِ إلى فعلٍ أخفَّ بيدِ المنفِّذ — يبقيانِ
دَينًا معلَّقًا بالقرار. فالدفعةُ **ستّةُ أسطحٍ لا ثمانية**.

**9.9.3 تعارضٌ مقيسٌ ثانٍ لا يوقفُ (Q-78 · PENDING_OWNER).** § 2.2 يعطي `graduate_batch` (`release_agent`) «المستوى 4»، و`release_agent`
ليسَ في `KILL_SWITCH_BLOCKS` عندَ أيِّ مستوى (فعلُ إطلاقٍ من العزلِ في E1 · أداةُ احتواء). يُنفَّذُ عمودُ الفعلِ كما هو (سابقةُ
Q-76 في W-723) فلا يُمنَعُ التخريجُ عندَ أيِّ مستوى، ويُعرَضُ السؤال. ونفسُه يخصُّ `complete_training` في دفعةِ learning_cycle.

**9.9.4 النمطُ: سابقةُ E1 § 2.2–2.3 (`PopulationRegistry.update_state` · W-699).** أربعةٌ من الستّةِ تنادي أسطحًا محروسةً أصلًا
(`register_agent` · `AgentSchool.take_step` عبرَ `run_full_curriculum` · `HealthChecker.check_agent` · `update_state`). ومناداتُها
داخلَ مُطبِّقٍ تعشيشٌ يرفضُه الكاشف (`NestedSovereignCallError`). فالنمطُ:
1. **تحقّقٌ مسبقٌ** بـ`request_permit` على فعلِ السطحِ وهدفِه **قبلَ أيِّ كتابة** — فالرفضُ (قاطعٌ · فاعلٌ لا يملك) نظيفٌ بلا أثرٍ داخليّ.
2. **العبوراتُ الداخليّةُ متعاقبةٌ لا متداخلة** — كلٌّ يعبرُ بسطحِه ومعوِّضِه.
3. **عبورُ السطحِ نفسِه أخيرًا** بأثرِه المُعلَنِ في § 2.2 (صفُّه هو) ومعوِّضِه.
4. **التعويضُ المنسَّق** حيثُ يجبُ أن يعكسَ عبورُ السطحِ ما ثبَّتَه عبورٌ قبلَه في العمليّةِ الواحدة (retire_agent وحدَه · Q-26).

| السطح | الفعل | الهدف | الأثرُ المُعلَن | المعوِّض | المفتاح |
|---|---|---|---|---|---|
| `take_exam` | `record_curriculum_step` (≥1) | `exam:{exam_id}` | CREATE صفُّ نتيجة | حذفُ الصفِّ بمعرِّفِه | `expansion.exam` · `{exam_id}` (`operation_id` أو uuid) |
| `submit_output` | `create_task` (≥4) | `output:{output_id}` | CREATE صفُّ مخرج | حذفُ الصفّ | `expansion.output.submit` · `{output_id}` |
| `approve_output` | `activate_agent` (≥4) | `output:{output_id}` | UPDATE approved/quality | إرجاعُ اللقطةِ السابقة | `expansion.output.approve` · `{output_id}/{السابق}->{بصمةُ الجديد}` |
| `employ_batch` | `dispatch_agent` (≥3) | `batch:{batch_id}` | UPDATE `employed` | إرجاعُ العددِ السابق | `expansion.batch.employ` · `{batch_id}/{السابق}->{الجديد}.{op}` |
| `graduate_batch` | `release_agent` (لا منع · Q-78) | `batch:{batch_id}` | UPDATE `graduated` | إرجاعُ العددِ السابق | `expansion.batch.graduate` · `{batch_id}/{السابق}->{الجديد}.{op}` |
| `retire_agent` | `contain_agent` (لا منع · احتواء) | `agent:{agent_id}` | CREATE سجلُّ تقاعد | حذفُ السجلِّ **وإعادةُ الوكيلِ إلى حالتِه السابقة** (Q-26) | `expansion.retire` · `{agent_id}/{reason}/{السابق}.{op}` |

**9.9.5 retire_agent (Q-26).** يُقرأُ الوكيلُ (اللقطةُ المؤرشفةُ وحالتُه السابقةُ في الكانونِ والمرآة) قبلَ الحدّ، ثمَّ التحقّقُ
المسبق، ثمَّ `update_state(agent, "retired")` بعبورَيه، ثمَّ عبورُ السجلّ. معوِّضُ السجلِّ يحذفُه ويعيدُ لقطةَ صفِّ السكّانِ
(`_restore_population_snapshot_core`) والحالةَ الكانونيّةَ (`_set_lifecycle_state_core`) — نوًى خاصّةٌ في `agent_runtime` و`executive_core`،
لا `royal/main.py:restore_agent` (K1). وإن فشلَ عبورُ السجلِّ بلا تشغيلِ المعوِّض (فشلٌ داخلَ المُطبِّق) يُعوِّضُ السطحُ بنفسِه
الأثرينِ ثمَّ يُعيدُ رفعَ الانكسار (سابقةُ `update_state`). وإن فشلَ الاسترجاعُ نفسُه يُسجَّلُ الفشلُ ويُرفَعُ ولا تُدَّعى الإعادة.

**9.9.6 حدودٌ مُعلَنة.** (1) العمليّاتُ المركّبةُ في employ/graduate ليست ذرّيّةً كلُّها: فشلُ عبورِ الدفعةِ الأخيرِ لا يعكسُ
فحوصَ الصحّةِ ولا خطواتِ المنهجِ ولا تحديثاتِ الحالةِ التي ثبتت قبلَه — كلٌّ منها محكومٌ بعبورِه ومعوِّضِه، والجدولُ
§ 2.2 حصرَ أثرَ السطحِ في صفِّ الدفعة. (2) `run_full_expansion` و`produce_first_output` منادِيانِ بلا كتابةٍ مباشرةٍ لا يُعبَران.
(3) الطفرات: لكلِّ سطحٍ نزعُ نداءِ الحدِّ يُسقِطُ فحصَ دليلِه تحديدًا (سابقةُ W-699 `mutation_results.json`).

**9.9.7 [W-724 · 2026-10-29] شُفِّرَ** بالتصميمِ أعلاه في `rules.py` (`graceful_shutdown` في EXECUTIVE_ACTIONS وخارجَ KILL_SWITCH_BLOCKS) و`system_life.py` (`ACTION_GRACEFUL_SHUTDOWN`) و`expansion.py` (الأسطحُ الستّة)،
وفحوصُه في `federal/executive/services/tests/test_w724_g1_expansion.py` (40) و`tests/constitutional/test_g1_vocabulary.py` (+4)، وحملةُ الطفرةِ 6/6 في `evidence/W-724/mutation_results.json`.
**تعديلٌ واحدٌ معلَنٌ على عمودِ «المفتاح»** (لا على الفعلِ ولا الأثرِ ولا المعوِّض): أُسقِطَ `{السابق}` و`{الجديد}` من مفاتيحِ approve_output وemploy_batch
وgraduate_batch وretire_agent، فصارت `{المعرِّف}.{op}` (وapprove_output `{output_id}/q={الجودة}.{op}`)؛ لأنَّ «السابقَ» يتبدّلُ بعدَ التطبيقِ الأوّلِ فتصيرُ الإعادةُ
بالمعرِّفِ نفسِه مفتاحًا جديدًا فتُكرِّرُ الأثرَ — وهذا يُسقِطُ الصنفَ 4. و`op` من `operation_id` أو uuid، فلا يتصادمُ استدعاءانِ مستقلّان. وفي الأسطحِ المركّبةِ الثلاثةِ
يُقرأُ سجلُّ الذرّيّةِ قبلَ الحدِّ (`_already_succeeded`) فلا تُعادُ العبوراتُ الداخليّةُ عندَ الإعادة. والمقيسُ عندَ حقنِ القاطعِ: retire_agent عندَ ≥3 يُرفَضُ
بالعبورِ الداخليِّ `update_population_state` لا بفعلِه (`contain_agent`)، فلا سجلَّ ولا انتقالَ يبقى — وهذا سلوكُ النمطِ لا قرارٌ جديد، ويُعرَضُ مع Q-78.
