# A1 — تحليلٌ مسجَّلٌ لعبورِ البنيةِ التحتيّةِ الحدَّ السياديّ (دَينُ D-4 في `common/`)

> **الهدف:** قياسُ مواقعِ الكتابةِ العامّةِ غيرِ العابرةِ في ملفّاتِ البنيةِ الخمسة موقعًا موقعًا (المستدعون · الفرع · التعشيش · الأثر · التعويض) ثمّ عرضُ الخياراتِ وتوصيةِ المنفِّذ على المالك، تنفيذًا لـ D21-أ البند 1، بلا أيِّ تنفيذ.

> **الإيداعُ (W-639 · بندُ `WI-109` · D21-أ بند 1):** تحليلٌ فقط بلا شِفرةٍ إنتاجيّةٍ — **توصيةُ منفِّذٍ للمالكِ لا قرارٌ**. أعدَّت المسوّدةَ مهمّةٌ مُفوَّضةٌ منَ المنسِّقِ (نموذجُه نفسُه · لا مقعدَ مجلسٍ) في نسخةٍ مستقلّةٍ عندَ `7a547fa`؛ وما تحقَّقَ منه المنسِّقُ بنفسِه وما لم يتحقَّقْ مُعلَنٌ في [`evidence/W-639/README.md`](evidence/W-639/README.md). والمساراتُ المذكورةُ للأدواتِ ومخرجاتِها صارت في `docs/audit/evidence/W-639/` (نُقِلَت منَ المجلَّدِ المؤقَّتِ عندَ الإيداعِ — لا تغييرَ في القيمِ).

---

## 0. النطاقُ والالتزام

- **قرارُ المالك (D21-أ · 1) حرفيًّا:** «A1: يُجرى التحليل المسجَّل أولًا (بند مستقل لفحص المستدعين والفرع والتعشيش والأثر والتعويض)، ثم تُعرض عليّ توصيتك. لا تنفيذ قبله.»
- **مكانُ العمل:** نسخةٌ مستقلّة `/home/user/workspace/a1_clone` عند الالتزام `7a547fa`، وأُنشئت هكذا:
  ```
  git clone -q /home/user/workspace/amos /home/user/workspace/a1_clone && cd a1_clone && git checkout -q 7a547fa
  ```
- **لا تعديلَ لأيِّ شيفرة.** المستودعُ الأصليّ `/home/user/workspace/amos` لم يُعدَّل. للإفصاح: نفّذتُ داخلَه أمرًا واحدًا للقراءةِ فقط هو `git -C /home/user/workspace/amos status --short`، لأتأكّدَ أنّه نظيف، وجاءَ بلا مخرجات. الأثرُ الوحيدُ الممكنُ لهذا الأمر تحديثُ ذاكرةِ الفهرسِ المؤقّتة لـgit، ولا يمسُّ أيَّ ملفٍّ متتبَّع. الأمرُ يخالفُ حرفَ التعليمات «لا عمليات git هناك»، ولذلك أذكرُه.
- **الأدواتُ المساعدة** كتبتُها خارجَ المستودع في `docs/audit/evidence/W-639/`، وهي قراءةٌ بشجرةِ الصياغة (AST) فقط:
  - `a1_callers.py.txt`: يعدُّ نداءاتِ الإنتاجِ لأسماءِ الأفعال، مع المستقبِلِ والنطاقِ المحيط.
  - `a1_nesting.py.txt`: يتتبّعُ الدوالَّ الممرَّرةَ بـ`applier=` إلى `guard_declared(` تتبُّعًا انتقاليًّا.
  - المخرجاتُ الخام: `a1_sites_measured.txt` و`a1_all_attr_calls_raw.txt` و`a1_callers_filtered.txt` و`a1_caller_classification.txt` و`a1_nesting_raw.txt`.
- **تعريفُ «الإنتاج»:** يُستبعَدُ كلُّ ما تحتَ `tests/` أو `test/`، وكلُّ ملفٍّ اسمُه `test_*.py`، وكذلك `docs/`، و`core/` حين يكونُ المستقبِلُ من نوعٍ آخر.

---

## 1. القياس: كم موقعًا؟

### 1.1 الأمرُ والملخّص

```
$ python3 tools/audit/sovereign_write_inventory.py --json /home/user/workspace/a1_clone/inv.json
```
مقتطفٌ من ملخّصِ الملفّ (`summary`):
```
write_sites_total: 246 · public_write_operations: 201 · sovereign_write_operations: 42
closed_legacy_paths: 7 · non_sovereign_write_operations: 157
by_area.service_common: {public: 28, sovereign: 0, non_sovereign: 28}
non_sovereign_by_file[…/common/persistent.py]: 20
```

### 1.2 التصفية: المسارُ أحدُ الملفّاتِ الخمسة، و`public=true`، و`guarded=false`، و`closed_legacy=false`

```
$ python3 -c "import json;d=json.load(open('inv.json')); P='federal/executive/services/src/amos_federation/'
F=['common/persistent.py','common/database.py','common/durable_event_bus.py','common/event_bus.py','common/events.py']
allin=[s for s in d['sites'] if s['path'] in [P+f for f in F]]
sel=[s for s in allin if s['public'] and not s['guarded'] and not s['closed_legacy']] ..."
all sites in files 28      ← لا موقعَ مستبعَدًا: كلُّ مواقعِ الملفّاتِ الخمسةِ دَين
selected 28
{persistent.py: 20, database.py: 4, durable_event_bus.py: 2, event_bus.py: 1, events.py: 1}
```

**العددُ المقيس 28**، وتوزيعُه على الملفّات كما هو متوقَّع: 20 + 4 + 2 + 1 + 1.

ولأنّ مفتاحَ السجلِّ في JSON لا يحملُ رقمَ سطر (DISC-039)، استخرجتُ الأسطرَ من دالّةِ الأداةِ نفسها `collect()`:
```
$ python3 -c "import sys;sys.path.insert(0,'tools/audit'); import sovereign_write_inventory as m; s=m.collect(m.REPO_ROOT) …"
database.py:422 - ensure_added_columns ('raw-sql-write',)
database.py:463 - with_db ('commit()',)
database.py:466 - wrapper ('commit()',)
database.py:564 - db_cursor ('commit()',)
durable_event_bus.py:92  DurableEventBus publish ('add()','commit()')
durable_event_bus.py:220 DurableEventBus ack ('add()','commit()')
event_bus.py:63          EventBus publish ('add()','commit()')
events.py:214            EventPublisher publish ('raw-sql-write',)
persistent.py:97   PersistentAgentStore register
persistent.py:220  PersistentToolStore register
persistent.py:294  PersistentTaskStore create
persistent.py:365  PersistentTaskStore update_status
persistent.py:380  PersistentMemoryStore store
persistent.py:492  PersistentExperienceStore record
persistent.py:617  PersistentCriticStore review
persistent.py:742  PersistentAuditStore append ('add()','commit()','raw-sql-write')
persistent.py:941  PersistentSystemStateStore set_level  via ('_row',)
persistent.py:956  PersistentSystemStateStore reset      via ('_row',)
persistent.py:990  PersistentPromotionStore create
persistent.py:1029 PersistentPromotionStore save_gates
persistent.py:144,258,330,413,526,646,932,1009  «PersistentPromotionStore get»  () via ('_row',)   ← 8 مواقع
```

### 1.3 اكتشافٌ قياسيّ: 7 من مواقعِ `get` الثمانية أثرٌ جانبيٌّ لأداةِ الجرد، لا كتابات

يَنسبُ الجردُ ثمانيةَ مواقع إلى «`PersistentPromotionStore.get`». والواقعُ أنّ في `persistent.py` ثماني دوالَّ مختلفةً اسمُها `get`، واحدةٌ في كلِّ صنف:
```
$ python3 - <<EOF  (ast: لكلِّ ClassDef، اطبع أسطرَ دوالِّ get)
PersistentAgentStore 144 · PersistentToolStore 258 · PersistentTaskStore 330 · PersistentMemoryStore 413
PersistentExperienceStore 526 · PersistentCriticStore 646 · PersistentSystemStateStore 932 · PersistentPromotionStore 1009
$ rg -n "self\._row\(" common/persistent.py   → فقط داخل PersistentSystemStateStore (get/set_level/reset)
```
والسببُ في `tools/audit/sovereign_write_inventory.py`، في الدالّة `synthesize_public_sites` (الأسطر 318–372):
- جدولُ النداءاتِ مفهرَسٌ **باسمِ الدالّة** (`calls.get(node.name)`)، فتتشاركُ دوالُّ `get` الثماني مجموعةَ نداءاتٍ واحدة، وفيها `_row` القادمُ من `PersistentSystemStateStore.get`.
- والمالكُ يُؤخَذُ من `classes.get(node.name)`، أي من **آخرِ صنفٍ** عرّفَ `get`، وهو `PersistentPromotionStore`.

**النتيجة:**
- `persistent.py:932` (`PersistentSystemStateStore.get`) **كتابةٌ حقيقيّة**: `_row()` يُدرِجُ الصفَّ `system` بالمستوى `normal` إن لم يكن موجودًا، ثمّ يُثبِّت (السطرُ 919).
- المواقعُ السبعةُ الأخرى (144، 258، 330، 413، 526، 646، 1009) **قراءةٌ خالصة**، واحتسابُها إيجابيّاتٌ كاذبة.
- **الدَّينُ الجوهريّ = 21 موقعًا** (28 − 7). لا أقترحُ هنا تصحيحَ الأداة (لا تنفيذ)، وأسجّلُه بندًا للمالك في §7.

ملاحظةٌ جانبيّة: نصُّ Q-25 في السجلّ يقولُ إنّ 8 من المواقعِ «مُفوَّضةٌ» (writes_via). المقيسُ أنّ للحقلِ `writes_via` قيمةً غيرَ فارغةٍ في **10** مواقع: ثمانيةُ `get` إضافةً إلى `set_level` و`reset`.

---

## 2. الآليّة: كيف يعملُ `guard_declared` والأثرُ المُعلَن والمعوِّض

مصادري: `services/executive_core/sovereignty_bridge.py` و`core/sovereignty/{contract,compensation,enforcement_boundary}.py` و`core/constitutional_engine/rules.py`.

1. **`guard_declared(actor, action, target, declared_effects, applier, compensators, …)`** يبني عقدًا (`ExecutionContract`) بالآثارِ المُعلَنة، ويطلبُ قرارَ البوّابةِ الدستوريّة (`ActionRequest`: الفاعل/الفرع، الفعل، الهدف). بعدَ ذلك يربطُ خطّةَ التعويض، ثمّ يُنفِّذُ `applier` داخلَ حدِّ الإنفاذ (`EnforcementBoundary.execute`)، ويُعيدُ دليلًا (`evidence`).
2. **أنواعُ الأثر** (`EffectKind`): `READ` و`CREATE` و`WRITE` و`DELETE` و`TRANSFER` و`EXTERNAL`. كلُّها مُغيِّرةٌ إلا `READ`.
3. **`bind_compensation_plan`** (`compensation.py:311`) يرفضُ **قبلَ التنفيذ** ثلاثَ حالات:
   - أثرٌ من نوعِ `EXTERNAL` يُعلَنُ في العقد يُطلِقُ `IrreversibleEffectError`، ويلزمُه outbox وقرارٌ بشريّ.
   - أثرٌ مُغيِّرٌ بلا معوِّضٍ يُطلِقُ `UncompensatableEffectError`.
   - معوِّضٌ لأثرٍ خارجَ العقد يُطلِقُ `CompensationScopeError`.
4. **لا يوجدُ في المعجمِ نوعُ أثرٍ «إلحاقٍ فقط/شاهد»:**
   ```
   $ rg -n "APPEND|append_only|إلحاق|witness" core/sovereignty/contract.py compensation.py outbox.py   → لا شيء
   ```
   النتيجة: كلُّ كتابةٍ تُعلَنُ عبرَ `guard_declared` تحتاجُ معوِّضًا يعكسُها.
5. **المعجمُ الدستوريّ** (`rules.py:117–140`) يحظرُ نصًّا عكسَ بعضِ هذه الكتابات:
   - `MEMORY_DESTRUCTIVE_ACTIONS` تضمُّ `delete_memory` و`delete_audit_log` و`truncate_audit_log` و`rewrite_history` و`delete_experience` و`purge_ledger`.
   - `HUMAN_GATED_ACTIONS` تضمُّ `promote_model`.
   - `KILL_SWITCH_TAMPER_ACTIONS` تضمُّ `downgrade_kill_switch`.
   - وتشترطُ القاعدةُ R008 (السطور 421–434) أن يكونَ `lower_kill_switch` بموافقةٍ بشريّة (`human_approved`).
6. **مستوى زرِّ التوقّفِ في طلبِ البوّابة:** الحقلُ `kill_switch_level` في `ActionRequest` قيمتُه الافتراضيّةُ 0، ولا يُمرِّرُه الجسرُ أبدًا:
   ```
   rg -n kill_switch_level core/   → model.py:84 (default 0) · rules.py:418 · engine.py · cli.py
   ```
   لا يمرُّ في `sovereignty_bridge.py`، فقاعدةُ «ما يمنعُه كلُّ مستوى» خاملةٌ في كلِّ عبورٍ عبرَ الجسر. (هذا خارجَ A1، لكنّه يمسُّ الخيار 1؛ انظر §5.)
7. **سابقةُ F1** (`docs/audit/F1_FEDERATION_COORDINATE_DESIGN.md`):
   - الفاعلُ وحدةٌ ثابتةٌ مُعلَنة، والفعلُ `coordinate`.
   - القرارُ D8 هناك تركَ صراحةً `bus.publish` بعدَ الالتزام **خارجَ العبور** بوصفِه «سؤالَ A1».
   - وتسجّلُ الوثيقةُ في Q-68 أنّ `AGENT` و`SYSTEM` يحصلان على `ALLOW` في `coordinate`، وهي ثغرةٌ قائمة.
8. **سابقةُ R1** (`docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md`): فاعلُ وحدةٍ ثابتٌ للسجلِّ الوطنيّ، وفعلٌ واحدٌ مُعلَن، ومعوِّضٌ صادقٌ يحذفُ الصفَّ المُنشأ.
9. **السابقةُ الجاريةُ للأثر داخلَ المطبِّقات** (المُقاسة في §4):
   - العمليّاتُ المحروسةُ تُعلِنُ **أثرَ النطاقِ وحدَه**، مثلُ صفِّ المؤسّسة. أمّا أثرُ الأثر (`record_domain_trace`، أي كتابةُ التدقيقِ ونشرُ الحدث) فيقعُ **داخلَ المطبِّق دونَ أن يُعلَنَ ودونَ معوِّض**.
   - المعوِّضُ يحذفُ صفَّ النطاق، ويبقى سطرُ التدقيقِ شاهدًا تاريخيًّا.

---

## 3. الجدولُ موقعًا موقعًا (28 موقعًا)

### 3.0 أوامرُ القياسِ المشتركة

```
# المستدعون (إنتاج فقط): كلُّ نداءٍ لصفةٍ باسمِ الفعل مع المستقبِل والنطاق
$ python3 docs/audit/evidence/W-639/a1_callers.py.txt . register,create,update_status,store,record,review,set_level,reset,save_gates,ack,publish,append,get \
     > docs/audit/evidence/W-639/a1_all_attr_calls_raw.txt          → 1730 سطرًا خامًا
# ثمّ التصفيةُ بالمستقبِلاتِ المعروفةِ الأنواع (audit/_audit/self._audit/_audit_store/PersistentAuditStore()/_AUDIT ·
#   get_event_bus()/get_durable_event_bus()/self._bus/bus/self._local_bus/event_publisher · agent_store/tool_store · …)
                                                       → a1_callers_filtered.txt = 83 نداءً
# أوامرُ rg المكمِّلة:
$ RG='rg -n --type py -g !**/tests/** -g !**/test/** -g !**/test_*.py'
$ $RG "Persistent(Agent|Tool|Task|Memory|Experience|Critic|Audit|SystemState|Promotion)Store\b" | rg -v common/persistent.py
$ $RG "get_event_bus\(\)" ; $RG "get_durable_event_bus\(\)|DurableEventBus\("
$ $RG "EventPublisher\(|event_publisher" -l ; $RG "with_db|db_cursor\(|ensure_added_columns|init_db\(|\.ack\(|TaskStore"
$ rg -n "init_event_consumers|from amos_federation.common.event_wiring|publish_task_created|…" --type py | awk -F: '{print $1}' | sort | uniq -c
      1 common/event_wiring.py · 4 tests/test_edge_branches.py · 15 tests/test_phase2_events.py · 4 tests/test_r2_task_execution_integration.py
```
**النتيجة:** وحدة `common/event_wiring.py` لا يستوردُها أيُّ ملفِّ إنتاج، ولا يبلغُها إلا الاختبارات. المستدعون من داخلِها مذكورون أدناه، ومعلَّمون بأنّهم «اختباريّون فعلًا».

**تصنيفُ موضعِ كلِّ نداء** (`a1_caller_classification.txt`):
```
Counter({'UNGUARDED_FN': 69, 'POST_GUARD_SAME_FN': 11, 'INSIDE_APPLIER': 3})
```
- `INSIDE_APPLIER`: النداءُ يقعُ نصًّا داخلَ `_apply` ممرَّرٍ إلى `guard_declared`.
- `POST_GUARD_SAME_FN`: النداءُ في دالّةٍ عامّةٍ تستدعي `guard_declared`، لكنّه بعدَها لا داخلَ المطبِّق.
- `UNGUARDED_FN`: كلُّ ما سوى ذلك.
- البلوغُ الانتقاليّ (عبرَ `record_domain_trace` و`engine._record`) مُقاسٌ وحدَه في §4.

**مفتاحُ الفروع:**
- **تنفيذيّ:** خدمات `api_gateway` و`tool_registry` و`memory_service` و`evaluation` و`critic` و`orchestrator` و`agent_runtime` و`executive_core` و`control_console` و`government_services` و`state_registry`، ومعها `governance/{canary,main,learning_cycle,security,system_life,expansion,state_runtime,factories}`.
- **اتّحاديّ متعدّدُ الفروع (F1):** `governance/federation.py`، وفيه أصنافُ `LegislativeBranch` و`JudicialBranch` و`ExecutiveBranch` و`SupremeOversight`.
- **قضائيّ:** `federal_judiciary/rulings.py`.
- **خزانة:** `governance/treasury.py`.
- **ملكيّ:** لا مستدعيَ ملكيًّا لأيِّ موقع. التاجُ يكتبُ `audit_entries` بإدراجٍ SQL خامٍ مباشر، خارجَ A1 (انظر §5.6).
- **بنيةٌ داخليّة:** `common/*` و`tools/ops/*`.

### 3.1 `persistent.py` (20 موقعًا: 13 حقيقيّة و7 إيجابيّات كاذبة)

| # | الموقع | المستدعون (إنتاج) file:line | الفرع | التعشيش | الأثر | التعويضُ الصادق |
|---|---|---|---|---|---|---|
| 1 | `:97 PersistentAgentStore.register` | `services/tool_registry/main.py:112` register_agent (HTTP)؛ `services/api_gateway/main.py:171` register_agent | تنفيذيّ (السجلّ) | لا | جدول `agents`: إنشاءٌ أو تحديثٌ للصفِّ القائم (`session.add` أو تعديلُ الحقول) مع فحصِ عزلِ المستأجر؛ يُعكَس | **ممكن**: لقطةٌ سابقة، فإن كانَ إنشاءً حُذفَ الصفّ، وإن كانَ تحديثًا استُعيدَت الحقول |
| 2 | `:220 PersistentToolStore.register` | `tool_registry/main.py:81` register_tool؛ `api_gateway/main.py:182` register_tool | تنفيذيّ | لا | جدول `tools`: إنشاءٌ أو تحديث، ويشملُ **`risk_level`**؛ يُعكَس | **ممكن** كالسابق. تنبيه: خفضُ `risk_level` أثرٌ أمنيّ (§5.3) |
| 3 | `:294 PersistentTaskStore.create` | **0** (لا مستدعيَ في الإنتاج؛ `TaskStore` لا يظهرُ إلا في تعليقات) | — | — | جدول `tasks`: `merge` (إنشاءٌ أو كتابةٌ فوقَ القائم) | ممكن، لكنّه بلا مستدعٍ |
| 4 | `:365 PersistentTaskStore.update_status` | **0** | — | — | تحديثُ `tasks.status` | ممكن (استعادةُ الحالةِ السابقة)، بلا مستدعٍ |
| 5 | `:380 PersistentMemoryStore.store` | `memory_service/main.py:53` store_memory (HTTP)؛ `agent_runtime/health.py:464` TreatmentSystem._execute_treatment | تنفيذيّ | لا | جدول `memories`: `merge` بالمفتاح (إنشاءٌ أو كتابةٌ فوقَ القائم) | **تقنيًّا ممكن، دستوريًّا ممنوع**: عكسُ الإنشاءِ هو `delete_memory`، وعكسُ الكتابةِ فوقَ القائمِ قريبٌ من `rewrite_history`، وكلاهما في `MEMORY_DESTRUCTIVE` |
| 6 | `:492 PersistentExperienceStore.record` | `evaluation/main.py:95` record_experience (بعدَ مراجعةِ `SubsystemBoundary.authorize`، أي `review_only`)؛ `common/event_wiring.py:255` (اختباريٌّ فعلًا، وبتوقيعٍ خاطئ؛ §5.4) | تنفيذيّ | لا | جدول `experiences`: `merge` | **ممنوعٌ دستوريًّا**: العكسُ هو `delete_experience` |
| 7 | `:617 PersistentCriticStore.review` | `critic/main.py:171` review_task (بعدَ `boundary`) | تنفيذيّ | لا | جدول `reviews`: `merge` | **ممكن**: حذفُ المراجعةِ أو استعادتُها؛ الفعلُ ليس في قائمةِ الحظر |
| 8 | `:742 PersistentAuditStore.append` | **23 نداءً**، تفصيلُها: | متعدّد | **نعم**: 3 مباشرةً + 12 انتقاليًّا (§4) | جدول `audit_entries`: إلحاقٌ بسلسلةٍ مُجزَّأة، **لا يُعكَس بطبيعته** | **مستحيلٌ صادقًا**: الحذفُ `delete_audit_log`، ويكسرُ السلسلة؛ و«قيدٌ عاكس» ليس عكسًا |
|   |   | `executive_core/engine.py:175` _record · `executive_core/agent_runtime_gateway.py:286` record_lifecycle · `executive_core/subsystem_boundary.py:207` record · `state_registry/trace.py:61` record_domain_trace · `control_console/main.py:205` activate_kill_switch · `control_console/main.py:249` sign_approval · `governance/main.py:43` _append_audit · `governance/learning_cycle.py:164,198,401,454` · `governance/security.py:360,469` · `governance/state_runtime.py:247,308,446(applier),546` · `governance/system_life.py:143,251,282` · `governance/factories.py:286(applier),623(applier)` · `common/event_wiring.py:233` (اختباريّ) | | | | |
| 9 | `:932 PersistentSystemStateStore.get` (حقيقيّ) | `governance/canary.py:47` get_system_status؛ `tools/ops/pg_backup_restore.py:295` | تنفيذيّ/حوكمة + أداةُ تشغيل | لا | جدول `system_state`: **بذرٌ كسول**؛ يُدرَجُ صفُّ `system` بالمستوى `normal` عندَ أوّلِ قراءة، وهو متطابقُ النتيجةِ عندَ التكرار | معوِّضٌ صادقٌ ممكن (حذفُ البذر) لكنّه بلا معنى؛ الأصدقُ نقلُ البذرِ إلى الإقلاع |
| 10 | `:941 PersistentSystemStateStore.set_level` | `governance/canary.py:54` activate_kill_switch (HTTP، `require_auth`)؛ `tools/ops/pg_backup_restore.py:268` | **حوكمة/زرُّ التوقّف** (المادة الثامنة) | لا | تحديثُ `system_state.level` (رفعُ زرِّ التوقّف) | العكسُ استعادةُ المستوى السابق، **لكنّه خفضٌ لزرِّ التوقّف**، أي `lower_kill_switch` الذي يتطلّبُ موافقةً بشريّة (R008)؛ فالمعوِّضُ نفسُه فعلٌ سياديّ |
| 11 | `:956 PersistentSystemStateStore.reset` | `governance/canary.py:73` reset_kill_switch (HTTP، **`require_auth` فقط**) | **حوكمة/زرُّ التوقّف** | لا | تحديثُ `system_state` إلى `normal` (**خفضُ زرِّ التوقّف**) | ممكن (إعادةُ المستوى السابق). **الخطرُ هنا في الفعلِ نفسِه لا في التعويض** (§5.1) |
| 12 | `:990 PersistentPromotionStore.create` | `governance/canary.py:157` create_promotion؛ `tools/ops/pg_backup_restore.py:272` | حوكمة/ترقيةُ النموذج (`promote_model` بوّابةٌ بشريّة) | لا | جدول `promotions`: `merge` | **ممكن**: حذفُ الصفّ إن كانَ جديدًا، أو استعادةُ اللقطة |
| 13 | `:1029 PersistentPromotionStore.save_gates` | `governance/canary.py:182` check_gate | حوكمة/ترقية | لا | تحديثُ `promotions.gates` و`status` | **ممكن**: استعادةُ البوّاباتِ والحالةِ السابقة |
| 14–20 | `:144` Agent.get · `:258` Tool.get · `:330` Task.get · `:413` Memory.get · `:526` Experience.get · `:646` Critic.get · `:1009` Promotion.get | (قراءات) | — | — | **لا كتابة**: إيجابيٌّ كاذبٌ من الجرد (§1.3) | لا ينطبق |

### 3.2 `database.py` (4 مواقع)

| # | الموقع | المستدعون | الفرع | التعشيش | الأثر | التعويض |
|---|---|---|---|---|---|---|
| 21 | `:422 ensure_added_columns` | `init_db()` وحدَها (داخل `database.py`)، و`init_db` يُستدعى عندَ تحميلِ الخدمات (rg `init_db\(`) | بنيةٌ داخليّة (ترحيلُ مخطَّطٍ عندَ الإقلاع) | لا | DDL: `ALTER TABLE … ADD COLUMN`، متطابقُ النتيجةِ عندَ التكرار؛ لا يُعكَسُ عمليًّا | لا معوِّضَ صادق (إسقاطُ عمودٍ ترحيلٌ عكسيّ لا تعويض). **ليس فعلًا سياديًّا بل تهيئة** |
| 22 | `:463 with_db` | **0** | — | — | ديكوريتر يُثبِّتُ جلسةً عامّة | لا ينطبق (شيفرةٌ ميّتة) |
| 23 | `:466 wrapper` (داخل with_db) | **0** | — | — | كالسابق | لا ينطبق |
| 24 | `:564 db_cursor` | `common/events.py:168,265,330` (EventPublisher: قراءة، ثمّ `INSERT INTO audit_log`، ثمّ قراءةُ التحقّق) | بنيةٌ داخليّة | لا | مديرُ سياقٍ **عامّ**: أثرُه ما يكتبُه المستدعي | **لا يمكنُ إعلانُه في هذا المستوى**؛ الأثرُ يُعرَفُ عندَ المستدعي فقط |

### 3.3 `durable_event_bus.py` (موقعان)

| # | الموقع | المستدعون | الفرع | التعشيش | الأثر | التعويض |
|---|---|---|---|---|---|---|
| 25 | `:92 DurableEventBus.publish` | `executive_core/engine.py:186` _record · `executive_core/agent_runtime_gateway.py:295` record_lifecycle · `executive_core/subsystem_boundary.py:221` record · `state_registry/trace.py:69` record_domain_trace · `common/event_wiring.py:70,85,102,123,144,171` (اختباريّةٌ فعلًا) | تنفيذيّ، ومنه القضائيّ عبرَ trace | **نعم: 12 مطبِّقًا عبرَ trace، و1 عبرَ engine._record** (§4) | جدول `durable_events`: **إنشاءٌ**، ثمّ تسليمٌ داخلَ العمليّةِ للمشتركين؛ أثرٌ متسلسلٌ لا يُستردّ | **لا معوِّضَ صادق**: حذفُ الحدثِ إعادةُ كتابةٍ للتاريخ، ولا يستردُّ ما فعلَه المشتركون؛ «حدثُ سحب» ليس عكسًا |
| 26 | `:220 DurableEventBus.ack` | **0** | — | — | `event_consumer_offsets`: إنشاءٌ أو تحديث | ممكن (استعادةُ الإزاحة)، بلا مستدعٍ |

### 3.4 `event_bus.py` (موقعٌ واحد)

| # | الموقع | المستدعون | الفرع | التعشيش | الأثر | التعويض |
|---|---|---|---|---|---|---|
| 27 | `:63 EventBus.publish` | **31 نداءً خارجيًّا + 1 داخليّ**: `governance/federation.py:510,588,698,774,829,956,1059,1251,1368,1462,1580` (11، **كلُّها بعدَ الحارس**: POST_GUARD) · `governance/expansion.py:386,510,639,679,805,842,981` (7) · `agent_runtime/health.py:256,408,523,600` (4) · `agent_runtime/population.py:584` · `control_console/main.py:149,250` · `governance/canary.py:58` · `governance/treasury.py:187,522` (خزانة) · `tool_registry/authorized_execution.py:419` · `tool_registry/providers/selection.py:231` · `tool_registry/sandbox.py:429` · داخليّ: `common/events.py:317` (`_local_bus`) | تنفيذيّ، واتّحاديّ (F1)، وخزانة | **لا** (0 من 43 مطبِّقًا) | جدول `event_store`: إنشاءٌ ثمّ تسليمٌ للمشتركين | **لا معوِّضَ صادق** (كالبند 25) |

### 3.5 `events.py` (موقعٌ واحد)

| # | الموقع | المستدعون | الفرع | التعشيش | الأثر | التعويض |
|---|---|---|---|---|---|---|
| 28 | `:214 EventPublisher.publish` | `api_gateway/main.py:115` create_task · `orchestrator/main.py:140` notify_plan | تنفيذيّ | لا | `INSERT INTO audit_log` (سلسلةٌ **ثانية** غيرُ `audit_entries`؛ انظر Q-27)، ثمّ نشرٌ إلى **NATS** (أثرٌ `EXTERNAL`) أو إلى الحافلةِ المحلّيّة | **لا معوِّضَ صادق**: التدقيقُ إلحاقٌ، وNATS أثرٌ خارجيٌّ لا يُسحَب، فيُرفَضُ عندَ الربطِ أصلًا (`IrreversibleEffectError`) ويلزمُه outbox |

**إجماليُّ المستدعين المقيسين:** 83 نداءً إنتاجيًّا في `a1_callers_filtered.txt`، منها 10 في `event_wiring.py` يبلغُها الاختبارُ وحدَه. **8 مواقع بلا أيِّ مستدعٍ إنتاجيّ:** TaskStore.create وTaskStore.update_status وwith_db وwrapper وack، ومعها ensure_added_columns الذي لا يبلغُه إلا `init_db`. هذه 6 بلا مستدعٍ خارجيّ.

---

## 4. التعشيش: ما يُستدعى من داخلِ مطبِّقٍ سياديّ قائم

```
$ python3 docs/audit/evidence/W-639/a1_nesting.py.txt . > docs/audit/evidence/W-639/a1_nesting_raw.txt
$ rg -c "^APPLIER" a1_nesting_raw.txt                → 43   (كلُّ guard_declared( بمعامل applier= في الإنتاج)
$ rg "^APPLIER" a1_nesting_raw.txt | rg -vc "> 0 A1" → 15   (مطبِّقاتٌ تبلغُ موقعًا من A1)
```
المطبِّقاتُ الخمسة عشر، وكلُّها تبلغُ **موقعين اثنين لا غير**: `persistent.py:742 append` و`durable_event_bus.py:92 publish`.

| المطبِّق (guard_declared في) | الفرع | المسار إلى A1 |
|---|---|---|
| `federal_judiciary/rulings.py:324` issue_ruling | **قضائيّ** | `trace.py:61 _AUDIT.append` + `trace.py:69 durable.publish` |
| `governance/factories.py:304` start_production | تنفيذيّ | `factories.py:286 audit.append` (مباشر) |
| `governance/factories.py:635` assign_manager | تنفيذيّ | `factories.py:623 audit.append` (مباشر) |
| `governance/state_runtime.py:463` allocate_budget | تنفيذيّ (ميزانيّة) | `state_runtime.py:446 PersistentAuditStore().append` (مباشر) |
| `government_services/service.py:595` publish_service · `:698` set_service_status · `:1008` assign_case · `:1277` decide_case · `:1437` close_case | تنفيذيّ (خدماتٌ حكوميّة) | trace (append + publish) |
| `government_services/service.py:901` open_case | تنفيذيّ | trace، **ومعه** `self._core.submit()` الذي يحوي `guard_declared` **متداخلًا**، ثمّ `engine.py:175 append` و`engine.py:186 publish` عبرَ `_record` |
| `state_registry/service.py:637` register_institution · `:767` set_institution_status · `:902` create_department · `:1083` appoint_official · `:1173` revoke_official | تنفيذيّ (سجلُّ الدولة) | trace (append + publish) |

**ملاحظاتُ القياس:**
- **2 من 28 موقعًا** تُبلَغُ من داخلِ مطبِّقاتٍ محروسة، عبرَ 15 مطبِّقًا. لا موقعَ آخرَ من A1 يُبلَغُ من داخلِ أيِّ مطبِّق.
- `federation.py` (F1) ينشرُ إلى `EventBus` في 11 موضعًا **بعدَ** عودةِ `guard_declared` لا داخلَه. هذا هو القرارُ D8 في F1 نفسه، وهو من صنف POST_GUARD.
- `engine._record` يُستدعى بعدَ الحارس في `engine.submit` و`engine.py:271,319`. لكنّه حين يُبلَغُ عبرَ `open_case` يقعُ داخلَ مطبِّقِ العمليّةِ الخارجيّة، ومعه **حارسٌ متداخل**. هذه حالةٌ قائمةٌ اليوم وتعمل، فالحدُّ يقبلُ التداخلَ في حالةٍ واحدةٍ مقيسة على الأقلّ.
- **المطبِّقاتُ الخمسة عشر لا تُعلِنُ أثرَ التدقيقِ ولا أثرَ الحدث.** كلٌّ منها يُعلِنُ أثرَ النطاقِ وحدَه، ومعوِّضُه يحذفُ صفَّ النطاق ويتركُ سطرَ التدقيق. مثالٌ من `state_registry/service.py:600–665`: `declared_effects=(_effect(INSTITUTIONS_TABLE, CREATE),)` مع معوِّضٍ يحذفُ الصفّ.
- **حدودُ الأداة:** التتبّعُ الانتقاليّ بالاسم، وبعمقٍ أقصاه 6، ويعبرُ الملفّاتِ حين يكونُ للاسمِ ثلاثةُ تعريفاتٍ أو أقلّ. قد يفوتُه مسارٌ يمرُّ عبرَ اسمٍ شائع (§8).

---

## 5. اكتشافاتٌ تمسُّ قرارَ العبور

1. **زرُّ التوقّفِ والترقيةُ ليسا «بنية».** مواقعُ `set_level` و`reset` و`Promotion.create/save_gates` (البنود 10–13) يبلغُها `governance/canary.py`، بمسارات HTTP لا يحميها إلا `require_auth`:
   ```
   rg -n "def |set_level|reset|create\(|save_gates" governance/canary.py
   ```
   وهذه الأفعالُ أفعالٌ دستوريّةٌ مُسمّاةٌ في المعجم: `lower_kill_switch` يتطلّبُ موافقةً بشريّة (R008)، و`downgrade_kill_switch` عبثٌ بالزرّ، و`promote_model` بوّابةٌ بشريّة.
   - دوالُّ `canary.py` لا تكتبُ مباشرة، فلا يحتسبُها الجردُ موقعًا. دَينُها **مُسجَّلٌ على البنية** في `persistent.py`.
   - **عبورُها بفعلِ بنيةٍ عامّ يجعلُها «محروسةً» في الجرد، وهي في الحقيقةِ تتجاوزُ قاعدةَ الموافقةِ البشريّة.** هذا هو الغسلُ عينُه.
2. **لا يمكنُ عبورُ التدقيقِ والذاكرةِ والخبرةِ والأحداثِ صادقًا بـ`guard_declared` كما هو اليوم.** كلُّ كتابةٍ مُعلَنةٍ تحتاجُ معوِّضًا (§2.3)، ومعوِّضاتُها إمّا محظورةٌ دستوريًّا (البنود 5 و6 و8) أو غيرُ موجودة (البنود 25 و27 و28). فإن عبرَت كما هي، فلا بدّ من واحدٍ من ثلاثة:
   - معوِّضٌ كاذب، وهذا يكسرُ صدقَ الحارس.
   - إعلانُ الأثرِ `EXTERNAL`، فيُرفَضُ ويحتاجُ outbox.
   - نوعُ أثرٍ جديدٌ مثلُ «إلحاق/شاهد»، وهذا يحتاجُ قرارَ عقدٍ في `core/sovereignty`.
3. **`tools.risk_level` قابلٌ للخفضِ عبرَ register** من مسارين HTTP (`tool_registry/main.py:81` و`api_gateway/main.py:182`). إن عبرَ بفعلِ بنيةٍ عامّ صارَ خفضُ المخاطرِ عبورًا «سياديًّا» لا يتمايزُ عن إنشاءِ أداة.
4. **`event_wiring.py` لا يبلغُه الإنتاج**، وفيه علّةٌ صامتة: `MemoryConsumer._handle_experience` (السطر 255) يستدعي `_exp_store.record(experience_id=…, exp_type=…)` بمعاملاتٍ مُسمّاة، والتوقيعُ `record(data, *, tenant_id)`. فيقعُ `TypeError` يبتلعُه `contextlib.suppress(Exception)`، ولا يُكتَبُ شيءٌ أبدًا. (رصدٌ فقط، خارجَ نطاقِ التنفيذ.)
5. **6 مواقع بلا مستدعٍ خارجيّ** (TaskStore×2، with_db، wrapper، ack، ensure_added_columns). عبورُها يعني إضافةَ حارسٍ إلى شيفرةٍ لا تُستدعى، والقرارُ فيها حذفٌ أو إعلانُ حدٍّ، لا عبور.
6. **ثلاثةُ كتّابٍ لسجلّاتِ التدقيق:**
   - `audit_entries` عبرَ `PersistentAuditStore`.
   - `audit_log` عبرَ `events.py:265` بـSQL خام.
   - إدراجُ التاجِ الخامُ في `audit_entries`.
   وهذه مادّةُ Q-27، وأيُّ «فعلِ تدقيقٍ» موحَّدٍ يجبُ أن يحسمَ هذا أوّلًا.
7. **`db_cursor` و`with_db` عامّان:** أثرُهما يحدّدُه المستدعي، فلا يُعلَنان في مستواهما. العبورُ الصادقُ مكانُه المستدعي، أي `events.py:214`.

---

## 6. الخيارات

### الخيار 1: فاعلُ وحدةٍ مُعلَنٌ واحد، وفعلٌ آليٌّ مُعلَنٌ واحد، لكلِّ الملفّات
(مثلًا فاعلٌ ثابتٌ «بنيةٌ» من فرع `SYSTEM` بفعلٍ واحد، على نمطِ F1 وR1.)
- **ما يفتحُه في السطوح:**
  - يُغلقُ الـ28 دفعةً واحدةً في الجرد.
  - يتطلّبُ فعلًا جديدًا في `rules.py` (أو استعارةَ `coordinate`)، وعقدًا لكلِّ موقع، ومعوِّضاتٍ لكلِّ كتابةٍ مُغيِّرة.
- **المخاطر:**
  - **غسلٌ عامّ.** أيُّ مستدعٍ (canary و`control_console` وHTTP) يكتبُ عبرَ البنية فيُحسَبُ عبورُه «سياديًّا» بهويّةِ البنيةِ لا بهويّته، فيمرُّ `reset` (خفضُ زرِّ التوقّف) دونَ موافقةٍ بشريّة، ويمرُّ خفضُ `risk_level`، وتمرُّ الترقية (§5.1 و§5.3). الفاعلُ الثابتُ يمحو الفاعلَ الحقيقيّ من الدليل.
  - **سلطةٌ حصريّة.** إن كانَ الفعلُ في مجموعةٍ حصريّة صارَ للبنيةِ سلطةٌ لا يملكُها غيرُها. وإن لم يكن حصريًّا (كـ`coordinate`) فـQ-68 قائمة: `AGENT` و`SYSTEM` يحصلان على `ALLOW`، فالحارسُ لا يمنعُ أحدًا.
  - **استحالةُ الصدق:** التدقيقُ والذاكرةُ والخبرةُ والأحداثُ بلا معوِّضٍ صادق (§5.2).
  - **تعشيشٌ مزدوج:** 15 مطبِّقًا ستستدعي حارسًا داخلَ حارس عندَ كلِّ سطرِ تدقيق، فيُضاعَفُ الدفترُ والذرّيّة، وقد يُحتمَلُ الارتدادُ الذاتيّ إن سُجِّلَ الدليلُ نفسُه عبرَ `append`.
- **الاختباراتُ والطفرات اللازمة:**
  - اختبارُ أنّ كلَّ موقعٍ يمرُّ بالحارس.
  - طفرةُ «إزالة الحارس» لكلِّ موقع (28).
  - طفرةُ «خفضُ زرِّ التوقّفِ عبرَ البنية يجبُ أن يُرفَض»، وهذه **ستفشلُ في هذا التصميم**.
  - اختبارٌ ضدّ إعادةِ الدخولِ في التعشيش.

### الخيار 2: أفعالٌ لكلِّ موقعٍ من المعجم
- **ما يفتحُه:**
  - `set_level` بفعل `activate_kill_switch`، و`reset` بفعل `lower_kill_switch` (`human_approved` إلزاميّ).
  - `Promotion.create/save_gates` بفعل `promote_model` أو أفعالٍ ترقويّة.
  - `register` (agent/tool) بأفعالِ تسجيل، و`critic.review` بفعلِ مراجعة.
- **المخاطر:**
  - يتّسعُ المعجم، وكلُّ فعلٍ جديدٍ تضييق (سابقةُ Q-18)، والأفعالُ الجديدةُ تحتاجُ قرارَ مالكٍ لكلٍّ منها.
  - **الفاعلُ يجبُ أن يكونَ المستدعي الحقيقيّ** لا وحدةً ثابتة، وإلّا عادَ غسلُ الخيار 1.
  - لا يحلُّ مشكلةَ التدقيق/الذاكرة/الخبرة/الأحداث (بلا معوِّضٍ صادق)، ولا شيفرةَ ميّتة.
  - الحارسُ في مستوى المخزن لا يعرفُ هويّةَ المستدعي إلا إذا مُرِّرت، فتُغيَّرُ تواقيعُ المخازن وكلُّ مستدعيها (83 نداءً).
- **الاختبارات:**
  - لكلِّ فعل: `ALLOW` للفرعِ الصحيح و`DENY` لغيره.
  - `lower_kill_switch` دونَ `human_approved` يُرفَض.
  - طفرةُ «تبديلُ الفعلِ إلى فعلٍ أعمّ» يجبُ أن تُكتشَف.
  - معوِّضٌ لكلِّ موقعٍ يُطفَّرُ إلى معوِّضٍ فارغٍ فيُكتشَف.

### الخيار 3: حدٌّ مُعلَن (يبقى الدَّين مُعلَنًا)
- **ما يفتحُه:** لا سطوحَ جديدة. يُسجَّلُ في `SOVEREIGN_DECISION_REGISTER` أنّ `common/*` بنيةٌ تحتَ الحدّ، وأنّ العبورَ مسؤوليّةُ المستدعي.
- **المخاطر:**
  - يبقى زرُّ التوقّفِ والترقيةُ والتسجيلُ بلا حارس، وهي أخطرُ ما في الدفعة.
  - يبقى الرقمُ 28 في الجرد، ومعه 7 إيجابيّاتٍ كاذبة.
  - الإعلانُ قد يصيرُ غطاءً دائمًا.
- **الاختبارات:** اختبارٌ أنّ الحدَّ المُعلَنَ مطابقٌ للجردِ (عددٌ وأسماء)، وطفرةٌ تضيفُ موقعَ كتابةٍ جديدًا في `common/` فيجبُ أن يفشلَ اختبارُ الحدّ.

### الخيار 4 (هجين تبرّرُه القياسات): تقسيمٌ بحسبِ طبيعةِ الأثرِ والمستدعي

| الفئة | المواقع | المعاملةُ المقترحة |
|---|---|---|
| **أ: أفعالٌ دستوريّةٌ مُقنَّعةٌ بالبنية** | 10، 11، 12، 13 (زرُّ التوقّف والترقية) | **لا تعبرُ في البنية.** تعبرُ عندَ المستدعي (`governance/canary.py`) بأفعالِ المعجمِ نفسِه (`activate_kill_switch`/`lower_kill_switch` مع `human_approved`، و`promote_model`)، والفاعلُ هو المستدعي. ومعوِّضاتُها صادقة (§3.1). ويُعلَّمُ موقعُ المخزنِ «مُفوَّضًا» لا مُغلقًا |
| **ب: سجلّاتُ نطاقٍ قابلةٌ للعكس** | 1، 2، 7 (agent/tool register، critic review) | تعبرُ **عندَ المستدعي** بفعلِ المستدعي، كما فعلت F1 وR1، مع معوِّضِ لقطة. ولا فاعلَ ثابتَ في البنية |
| **ج: شهودُ إلحاقٍ لا يُعكَسون** | 8، 25، 27، 28، و5 و6 (التدقيق، الأحداث، الذاكرة، الخبرة) | **حدٌّ مُعلَنٌ مُقيَّد**: تُعلَنُ «شاهدَ إلحاق» تابعًا لعمليّةِ مستدعيه. داخلَ المطبِّقاتِ الخمسة عشر هي تابعةٌ لعمليّةٍ محروسةٍ أصلًا، والسابقةُ الجاريةُ أنّها غيرُ معلنةٍ ولا مُعوَّضة. وخارجَها يُسجَّلُ أنّ عبورَها يتطلّبُ قرارًا في العقد (نوعُ أثرِ «إلحاق»، أو outbox لـNATS) |
| **د: بنيةٌ حقيقيّةٌ أو ميّتة** | 9، 21، 22، 23، 24، 26، 3، 4 | **حدٌّ مُعلَنٌ أو حذف**: البذرُ والترحيلُ تهيئةُ إقلاع؛ `db_cursor`/`with_db` عامّان لا يُعلَنان في مستواهما؛ وTaskStore وack وwith_db بلا مستدعٍ |
| **هـ: إيجابيّاتٌ كاذبة** | 14–20 | إصلاحُ القياسِ في `sovereign_write_inventory.py` (الفهرسةُ بالمؤهَّل `Class.method` لا بالاسم)، بقرارٍ منفصل |

- **ما يفتحُه:** 4 سطوحٍ في `canary.py` بأفعالٍ موجودةٍ أصلًا في المعجم، و4 سطوحٍ للتسجيل/المراجعة عندَ المستدعين. **لا فعلَ جديدٌ للبنية، ولا فاعلٌ ثابت.**
- **المخاطر:**
  - الفئةُ ج تبقى دَينًا مُعلَنًا، لكنّها لا تمنحُ أحدًا سلطة: الكتابةُ إلحاقٌ لا تُغيِّرُ حالةً سياديّة.
  - يجبُ ضمانُ ألّا يُستعمَلَ «شاهدُ الإلحاق» لكتابةِ حالة. والمخزنان 5 و6 (الذاكرة والخبرة) يستعملان `merge`، فيكتبان فوقَ القائم، فليسا إلحاقًا خالصًا. **إدراجُهما في ج يحتاجُ قرارًا صريحًا** أو تحويلَهما إلى إلحاقٍ فقط.
- **الاختباراتُ والطفرات:**
  - (أ) `reset_kill_switch` دونَ موافقةٍ بشريّةٍ يُرفَض، وطفرةُ حذفِ الحارسِ من `canary.reset_kill_switch` تُكتشَف.
  - (ب) لكلِّ مسار: فرعٌ خاطئٌ يُرفَض، والمعوِّضُ يعيدُ اللقطة، وطفرةُ المعوِّضِ الفارغ تُكتشَف.
  - (ج) اختبارُ الحدّ: قائمةُ الشهودِ المُعلَنة = الجرد، وطفرةٌ تجعلُ شاهدًا يكتبُ عمودَ حالةٍ تُكتشَف.
  - (هـ) اختبارٌ يُثبتُ أنّ `Agent.get` وأخواتِها لا تُحتسَبُ كتابات.

---

## 7. توصيةُ المنفِّذ (للمالك، لا قرار)

> **توصيةُ المنفِّذ:** رفضُ الخيار 1 (الفاعل الثابت الواحد). سببُه المقيس: 4 من المواقع أفعالٌ دستوريّةٌ مسمّاة؛ إذ إنّ `reset` هو `lower_kill_switch` ويتطلّبُ موافقةً بشريّة، و`promotions` هي `promote_model`. وفاعلُ بنيةٍ ثابتٌ يغسلُها، ويغسلُ معها خفضَ `risk_level`. كما يستحيلُ تعويضُ التدقيقِ والأحداثِ صادقًا. **والمقترحُ الهجينُ (الخيار 4):**
> - (أ) يعبرُ زرُّ التوقّفِ والترقيةُ عندَ المستدعي (`governance/canary.py`) بأفعالِ المعجمِ القائمةِ وبفاعلِ المستدعي، **أوّلًا** لأنّها الأخطر.
> - (ب) يعبرُ التسجيلُ والمراجعةُ عندَ مستدعيها على نمطِ F1 وR1، بمعوِّضِ لقطة.
> - (ج) تُعلَنُ شهودُ الإلحاق (التدقيق والأحداث) حدًّا مُقيَّدًا تابعًا لعمليّةِ المستدعي، ويُطرَحُ سؤالُ «نوعُ أثرِ إلحاق/outbox» على المالكِ منفصلًا. وتُطرَحُ الذاكرةُ والخبرةُ سؤالًا صريحًا لأنّهما تكتبان فوقَ القائم.
> - (د) يُعلَنُ حدٌّ للتهيئة، ويُقرَّرُ حذفُ الشيفرةِ الميّتة.
> - (هـ) تُصحَّحُ أداةُ الجرد لأنّها تحتسبُ 7 قراءاتٍ كتابات.
> لا تنفيذَ قبلَ قرارِ المالك.

---

## 8. ما لم يُقَس

- **البلوغُ الديناميكيّ:** المستدعون مُقاسون نصًّا (AST) بالمستقبِل. لم تُقَس النداءاتُ عبرَ `getattr` أو الحقنِ أو المستقبِلاتِ بأسماءٍ غيرِ مدرجة. القائمةُ الخامُ (1730 سطرًا) محفوظةٌ لمن يريدُ توسيعَ المرشِّح.
- **المسارُ الانتقاليّ للتعشيش** بالاسم وبعمقٍ ≤ 6؛ لم يُقَس بتتبّعِ أنواعٍ حقيقيّ ولا بتشغيل. قد يُفوِّتُ مسارًا عبرَ اسمٍ شائعٍ له أكثرُ من 3 تعريفات.
- **سلوكُ الحدِّ عندَ تعشيشٍ عامّ:** إعادةُ الدخول وتداخلُ الذرّيّة والدفتر. المقيسُ حالةٌ واحدةٌ قائمة (`open_case` ثمّ `engine.submit`) ولم تُشغَّل اختباراتُها.
- **ما إذا كانَ `audit.append` يُستدعى من داخلِ مسارِ تسجيلِ دليلِ الحارسِ نفسِه** (خطرُ الارتداد): قِيسَ أنّ `core/sovereignty` والجسرَ لا يستوردان `persistent` أو `event_bus` (rg بلا نتائج)، ولم يُقَس ما بعدَ ذلك.
- **مشتركو الحافلتين** وما يكتبونه عندَ التسليم (أثرٌ متسلسل) لم يُحصَوا في الإنتاج، عدا أنّ `event_wiring` لا يبلغُه الإنتاج.
- **مسارُ NATS الحقيقيّ** في `events.py` (يتطلّبُ اتّصالًا حيًّا).
- **المصادقةُ الفعليّة على مسارات `canary.py` HTTP** (ما تفعلُه `require_auth` بالتفصيل، ومن يملكُ الرمز) لم تُقَس. المقيسُ أنّها الحمايةُ الوحيدةُ الظاهرةُ في التوقيع.
- **لم تُشغَّل أيُّ اختباراتٍ ولا طفرات**، ولم يُنشأ venv.
- **مكانُ التصحيحِ الدقيق في أداةِ الجرد** لم يُختبَر. المقيسُ فقط أنّ الفهرسةَ بالاسم تُنتجُ الإيجابيّاتِ السبعة.
- **أحكامُ «الفرع»** مبنيّةٌ على موقعِ الملفّ والصنف، لا على هويّةِ فاعلٍ وقتَ التشغيل.
