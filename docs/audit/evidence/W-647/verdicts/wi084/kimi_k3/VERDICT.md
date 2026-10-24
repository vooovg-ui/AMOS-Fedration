# حكمُ مقعدِ المجلسِ — kimi_k3 (عائلةُ Moonshot AI Kimi) · جولةُ WI-084 (W-647)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-084 (الطابورُ الواحدُ · التوجيهُ 19 § 2 · بروتوكولُ Q-59) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذورِهِ الخاصّةِ (council_w641/kimi_k3/wi084) — منسوخٌ آليًّا، وما بعدَ الفاصلِ بايتًا ببايتٍ (sha256 `d4d08a302bd399c5b10c3bfb8257d3d7d8d739ef8cd3dfe0198a3e48f9b7e708`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-084 عندَ العقدةِ `4b5b2be5` — إحاطةٌ مبصومةٌ ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-647) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-24

---
MODEL: Kimi (kimi_k3)
FAMILY: Moonshot AI
RUN_DATE: 2026-10-24 07:08 +00:00
NODE: 4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
CLONE_PATH: /home/user/workspace/council_w641/kimi_k3/wi084/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi084/
 2. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi084/)
 3. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git log --format='%h %cI %s' -- docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
 5. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && cat docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
 6. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git diff --stat 5caeac5bdf9ea446163c40c0a11147fa1e1a9cec HEAD -- core/sovereignty/ federal/executive/services/src/amos_federation/services/government_services/ federal/executive/services/src/amos_federation/services/executive_core/
 7. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "EXTERNAL" core/sovereignty/*.py
 8. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "EffectKind.EXTERNAL" --type py
 9. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "def advance|def run|is_terminal|max_attempts" federal/executive/services/src/amos_federation/services/executive_core/engine.py
 10. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "def process_case" -A 60 federal/executive/services/src/amos_federation/services/government_services/service.py
 11. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 12. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "Q-16" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 13. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && sha256sum docs/audit/evidence/W-641/briefs_wi084/briefing_kimi_k3.md
 14. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && cat docs/audit/evidence/W-641/briefs_wi084/SHA256SUMS
 15. nl -ba /home/user/workspace/council_w641/kimi_k3/wi084/probe/probe_wi084_kimi_k3.py
 16. cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && PYTHONPATH=/home/user/workspace/council_w641/kimi_k3/wi084/repo .venv/bin/python /home/user/workspace/council_w641/kimi_k3/wi084/probe/probe_wi084_kimi_k3.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi084/
EXIT: 0
BYTES: 41
SHA256: a3e2f8d92a955524b52c488f6eab3a10df32c172749d966186bbfc125cdea034
NO_EOL: 0
--- OUTPUT ---
4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi084/)
EXIT: 0
BYTES: 788
SHA256: 345a4d3f8be8230bc5fb5e31c5c1574e05df03df3e258e80bbb9ea33dba1ab4a
NO_EOL: 0
--- OUTPUT ---
Note: switching to '4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 4b5b2be5 W-641: WI-111/WI-109/WI-110 IN_PROGRESS→IN_REVIEW · إحاطاتُ جولتَي WI-111 وWI-084 مبصومةٌ (الطابورُ الواحدُ) · مسبارُ طفراتِ WI-111
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: a3e2f8d92a955524b52c488f6eab3a10df32c172749d966186bbfc125cdea034
NO_EOL: 0
--- OUTPUT ---
4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git log --format='%h %cI %s' -- docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
EXIT: 0
BYTES: 252
SHA256: 38d929e32dd28bb5f280e4bec872d5debe92eda25f894a5dcdf8c1a8f7ac31c0
NO_EOL: 0
--- OUTPUT ---
5caeac5b 2026-10-16T08:56:27Z W-398: WI-084 — وثيقةُ تصميمِ نوعِ الأثرِ EXECUTION (Q-16 ③): 8 مواضعِ قرارٍ في 6 ملفّات · ثلاثةُ عقودٍ لـprocess_case · خطّةُ رجوع · بلا شِفرة
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && cat docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
EXIT: 0
BYTES: 14808
SHA256: 5623749af0abd112c54f2a9bf602870555d39b42346f4d93bb338a32486f3e9e
NO_EOL: 0
--- OUTPUT ---
# Q16_EXECUTION_EFFECT_DESIGN.md — وثيقةُ تصميمِ نوعِ الأثرِ `EXECUTION` (قرارُ المالكِ Q-16 ③)

<!--
الهدف: وصفٌ دقيقٌ لتعديلِ الأوّليّاتِ السياديّةِ الذي يقتضيه قرارُ المالكِ في Q-16 ③ — قبلَ أيِّ شِفرة
النطاق: تصميمٌ فقط · لا شِفرةَ ولا اختبارَ ولا تعديلَ في core/sovereignty/ ولا في process_case · كلُّ رقمٍ بأمرٍ يُعادُ تشغيلُه
المالك: docs/audit/ — ديوانُ التدقيق · البندُ WI-084 (Perplexity Computer)
تاريخ الإنشاء: 2026-10-16
-->

**البند:** `WI-084` · **القيد:** `W-398` · **نقطةُ القياس:** فرعُ `w-381-merge-exception-d9` فوقَ main `81b0071`
**الحالة:** تصميمٌ للمراجعة — **لا يُكتَبُ سطرُ شِفرةٍ قبلَ مراجعةِ مقعدينِ يُعيدانِ التشغيلَ (Q-H)** ثمَّ بندِ شِفرةٍ مستقلٍّ يُسجَّلُ بعدَها.

---

## 0 · القرارُ الذي تُنفِّذُه هذه الوثيقة

- **نصُّ المالكِ في Q-16 (2026-10-16 · قيدُ W-363):** «نوع أثر جديد EXECUTION ← توصية المنفّذ، لكنها تعدّل بنية سيادية وعقودًا».
- **الشرطانِ قبلَ الشِّفرة (توجيهُ المستشارِ 8 § 2):** (أ) بندٌ مُسجَّلٌ يصفُ التعديلَ — العقودُ 1I/1K · أنواعُ الأثر · ما يتأثّر · خطّةُ رجوع — **وثيقةُ تصميمٍ أوّلًا** · (ب) مراجعةُ مقعدينِ يُعيدانِ التشغيل.
- **المرفوضُ بنصِّ القرار:** ① إخراجُ التشغيلِ من الإعلان · ② معوّضٌ يُنادي `cancel` (يفشلُ دائمًا بعدَ بدءِ التنفيذ).

## 1 · المشكلةُ مقيسةً

`process_case` (`federal/executive/services/src/amos_federation/services/government_services/service.py:1041`) تفعلُ ثلاثةَ أشياءَ بلا حدٍّ سياديّ:

| الخطوة | السطر | ما يحدث | يُعكَس؟ |
|---|---|---|---|
| 1 | 1058–1060 | `case.status = "processing"` ثمَّ `commit()` | نعم (كتابةُ صفّ) |
| 2 | 1064 | `self._core.run(task_id, max_steps)` — خطواتٌ تُنفَّذُ وأدواتٌ تُنادى | **لا** |
| 3 | 1071–1074 | `review_state` و`status = reviewed/processing` ثمَّ `commit()` | نعم (كتابةُ صفّ) |

والجردُ يعدُّها دَينًا (`tools/audit/sovereign_write_inventory.py`: `public=True · writes=[commit()] · guarded=False`).

**وقيسَ في `ExecutiveCore.run`** (`executive_core/engine.py:561`): حلقةٌ تقرأُ الحالةَ في كلِّ خطوةٍ وتتوقّفُ عندَ الحالةِ النهائيّة (`is_terminal`) — فإعادةُ النداءِ على مهمّةٍ انتهت **لا تُعيدُ تنفيذَها**، وعلى مهمّةٍ لم تنتهِ **تُكمِلُها من حيثُ وقفت**. وهذه الخاصّيّةُ أساسُ قسمِ 4-ج أدناه.

## 2 · مواضعُ القرارِ بـ`EXTERNAL` اليومَ (ما سيتغيّر)

**الأمر:** `rg -n "EXTERNAL" core/sovereignty/*.py | rg -v "ROOT_EXTERNAL_HUMAN|MANDATORY_EXTERNAL_STAGES|EXTERNAL_OUTBOX"`

**8 مواضعِ قرارِ سلوكٍ في 6 ملفّات** — غيرَ التعريفِ (`contract.py:72` و`:89`) والبنّاءِ (`outbox.py:1360`) والشروح:

| # | الموضع | السلوكُ اليوم | بعدَ التصميم |
|---|---|---|---|
| 1 | `compensation.py:103` | `IRREVERSIBLE_EFFECT_KINDS = {EXTERNAL}` ⇒ `bind_compensation_plan` يرفعُ `IrreversibleEffectError` (:331) | `{EXTERNAL, EXECUTION}` — فلا معوّضَ لتشغيلٍ أبدًا (يُغلِقُ الخيارَ ② بنيويًّا) |
| 2 | `jurisdiction.py:165` | `NON_JUDICIAL_EFFECT_KINDS` تمنعُ القضاءَ من DELETE/TRANSFER/EXTERNAL | يُضافُ `EXECUTION` — تشغيلُ المهامِّ شأنٌ تنفيذيٌّ لا قضائيّ |
| 3 | `enforcement_boundary.py:380` | `detect_external` ببادئةِ `"EXTERNAL:"` لتمييزِ النتيجةِ في سجلِّ الأحاديّة | يُقرأُ من المجموعةِ لا من نوعٍ واحد: كلُّ بادئةٍ من `IRREVERSIBLE_EFFECT_KINDS` |
| 4 | `enforcement_boundary.py:460` | جمعُ الآثارِ الخارجيّةِ لفحصِ الخلط | `e.kind in IRREVERSIBLE_EFFECT_KINDS` |
| 5 | `enforcement_boundary.py:463` | جمعُ الآثارِ المغيِّرةِ الداخليّة ⇒ `MixedEffectContractError` إن اجتمعا | `e.kind not in IRREVERSIBLE_EFFECT_KINDS` — فعقدٌ يخلطُ تشغيلًا بكتابةِ قضيّةٍ **يُرفَض** |
| 6 | `enforcement_boundary.py:548` | `route`: غيرُ الخارجيِّ إلى المُطبِّق، والخارجيُّ إلى الصادر | غيرُ اللّامعكوسِ إلى المُطبِّق، واللّامعكوسُ (ومنه `EXECUTION`) إلى الصادر |
| 7 | `idempotency.py:716` | المسارُ الذرّيُّ المباشرُ يرفضُ بادئةَ `"EXTERNAL:"` | يرفضُ كلَّ بادئةٍ لامعكوسة |
| 8 | `outbox.py:973` | الصادرُ لا يقبلُ إلّا `EXTERNAL` (`OutboxError`) | يقبلُ `IRREVERSIBLE_EFFECT_KINDS` |

**قاعدةُ التصميم:** لا موضعَ يذكرُ `EffectKind.EXECUTION` باسمِه إلّا التعريفُ والمجموعةُ والاختصاصُ القضائيّ — وكلُّ ما سواها يقرأُ **المجموعة**. فلا يُنسى نوعٌ ثالثٌ لامعكوسٌ يُضافُ لاحقًا.

## 3 · تغييرُ العقود

### 3-أ · أنواعُ الأثر (1E · `contract.py`)

- يُضافُ `EXECUTION = "EXECUTION"` إلى `EffectKind`، و`is_mutating` صحيحٌ له تلقائيًّا (كلُّ ما ليس `READ`).
- الوسمُ العربيّ: «تشغيلُ مهمّة».
- `sovereignty_bridge.py:498` يبني النوعَ بـ`contract.EffectKind(kind)` من نصّ — فيقبلُ `"EXECUTION"` بلا تعديل.

### 3-ب · التعويض (1I · `compensation.py`)

- لا معوّضَ يُقبَلُ لـ`EXECUTION` (`UncompensatableEffectError`) ولا خطّةَ تعويضٍ لعقدٍ فيه تشغيل (`IrreversibleEffectError`) — **بالمجموعةِ نفسِها، لا بقاعدةٍ جديدة**.
- **ما لا يتغيّر:** خطّةُ التعويضِ لعقدٍ لا تشغيلَ فيه تبقى كما هي حرفيًّا.

### 3-ج · الصادر (1K · `outbox.py` · `enforcement_boundary.py`)

- `enqueue_write_ahead` (`outbox.py:1055`) يبقى كما هو: الإدراجُ **قبلَ** تثبيتِ نجاحِ العمليّة، ورفضُه بعدَه (`OutboxOrderingError`).
- **مسألةٌ مقيسةٌ لا تُخفى:** الصادرُ يُعلِنُ `AT_LEAST_ONCE_WITH_STABLE_IDEMPOTENCY_IDENTITY` و`claims_exactly_once: False` (`outbox.py:1351`) ويُعيدُ حتى `DEFAULT_MAX_DELIVERY_ATTEMPTS = 3` (`:86`). فالتشغيلُ قد يُسلَّمُ أكثرَ من مرّة.
- **الحلُّ المقترح:** المُزوّدُ (`ProviderAdapter`) لـ`EXECUTION` يُنادي `ExecutiveCore.run(task_id)` **ومفتاحُ أحاديّتِه `task_id`**. وبما قيسَ في § 1 (`run` يتوقّفُ عندَ الحالةِ النهائيّة ويُكمِلُ من حيثُ وقف) فالتسليمُ المكرَّرُ لا يُعيدُ خطوةً تمَّت — **بشرطِ** أن تكونَ `advance` نفسُها أحاديّةً لكلِّ خطوة. وهذا الشرطُ **غيرُ مقيسٍ بعدُ** (سؤالُ المراجعةِ R-2).
- `INDETERMINATE` (سقوطُ العاملِ داخلَ النداء) لا تُقرأُ فشلًا ولا نجاحًا: تُقرأُ حالةُ المهمّةِ من `ExecutiveCore` نفسِه قبلَ أيِّ إعادة.

## 4 · `process_case` بعدَ الهجرة

### 4-أ · ثلاثةُ عقودٍ لا عقدٌ واحد

فحصُ الخلطِ (§ 2 · الموضع 5) يمنعُ جمعَ التشغيلِ وكتابةِ القضيّةِ في عقدٍ واحد — وهذا مقصود:

| العقد | الأثر | المسار | المعوّض |
|---|---|---|---|
| C1 · بدءُ المعالجة | `WRITE:gov.case:<ref>` (الحالةُ ← `processing`) | المُطبِّقُ المحروس | يُعيدُ الحالةَ السابقة |
| C2 · التشغيل | `EXECUTION:executive.task:<task_id>` | الصادرُ (write-ahead) ثمَّ العامل | **لا معوّض** (لامعكوس) |
| C3 · قيدُ النتيجة | `WRITE:gov.case:<ref>` (`review_state` · `reviewed`/`processing`) | المُطبِّقُ المحروس | يُعيدُ القيمتينِ السابقتين |

### 4-ب · الترتيبُ وحالاتُ الفشل

1. **C1** يُنفَّذُ ويُثبَّت. فشلُه ⇒ لا شيءَ وقع.
2. **C2** يُدرَجُ في الصادرِ قبلَ تثبيتِ نجاحِه. فشلُ الإدراجِ ⇒ **يُعوَّضُ C1** (تعودُ القضيّةُ إلى حالتِها) — ولا تشغيلَ وقع.
3. التسليمُ يُنادي `run`. نتيجتُه `DELIVERED` ⇒ **C3** بالحالةِ النهائيّةِ كما قالَها العمودُ التنفيذيّ (نجاحًا أو فشلًا — كما اليوم).
4. `DEAD` أو `INDETERMINATE` ⇒ **لا C3 ولا تعويضَ لـC1**: القضيّةُ تبقى `processing` لأنَّ ذلك صادق — شيءٌ ربّما جرى. وتُعرَضُ في قائمةِ حالاتٍ تنتظرُ قرارًا (سؤالُ المالكِ O-1).

### 4-ج · متزامنٌ أم لا؟

اليومَ `process_case` تُعيدُ النتيجةَ في النداءِ نفسِه. والصادرُ يُسلَّمُ بعاملٍ (`OutboxWorker` · `outbox.py:1211`). خياران:

- **(س) تسليمٌ متزامن:** `process_case` تُدرِجُ C2 ثمَّ تستدعي العاملَ مرّةً واحدةً على هذا الأثرِ وحدَه، وتُعيدُ النتيجةَ كما اليوم. **لا كسرَ في عقدِ الواجهة.**
- **(ع) تسليمٌ غيرُ متزامن:** تُعيدُ `processing` فورًا ويُكمِلُ العاملُ لاحقًا. كسرٌ في الواجهةِ وفي اختباراتِها.

**التوصية: (س)** — لا يتغيّرُ ما يراه المُنادي، ويبقى الترتيبُ مفروضًا بالصادر.

## 5 · ما يتأثّر

| المجال | الأثر | يُقاسُ عندَ الشِّفرةِ بـ |
|---|---|---|
| مسارُ `EXTERNAL` القائم | **لا تغييرَ في سلوكِه** — المجموعةُ تحويه كما تحويه اليوم | الحزمةُ الكاملةُ خضراءُ بلا تعديلِ اختبارٍ قائم |
| اختباراتٌ تذكرُ `EXTERNAL` | 6 ملفّات: compensation 4 · enforcement_boundary 10 · idempotency 1 · outbox 3 · crown_human_root 4 · enforcement_integration 5 (`rg -c EXTERNAL tests/sovereignty/*.py`) — **لا يُعدَّلُ منها شيء** | خضراءُ كما هي |
| اختباراتٌ جديدة | لكلِّ موضعٍ من الثمانيةِ فحصٌ لـ`EXECUTION` · وطفرةٌ لكلٍّ (إرجاعُ `is EXTERNAL` بدلَ المجموعةِ يُسقِطُ فحصًا) | سجلُّ الطفرات |
| `process_case` | دَينٌ يخرجُ من D-4 (`public · commit · unguarded`) | `sovereign_write_inventory.py` قبلُ/بعدُ |
| بياناتٌ قائمة | لا سجلّاتِ صادرٍ من نوعِ `EXECUTION` اليومَ — النوعُ غيرُ موجود | عدُّ السجلّاتِ قبلَ الدمج |
| أوّليّاتُ Q-16 الأخرى | `build_compensation_plan` لا يتغيّرُ توقيعُه ولا قواعدُه الثلاث | فحصُ التوقيع |

## 6 · خطّةُ الرجوع

1. **الشِّفرةُ في قيودٍ مستقلّةٍ مرتّبة:** (ر1) النوعُ والمجموعةُ والمواضعُ الثمانية · (ر2) مُزوّدُ التشغيل · (ر3) هجرةُ `process_case`. فالرجوعُ عن (ر3) وحدَه يُعيدُ `process_case` إلى سلوكِها اليومَ ويُبقي البنيةَ خامدةً بلا مُستعمِل.
2. **قبلَ أيِّ رجوعٍ عن (ر1) أو (ر2):** يُعَدُّ في الصادرِ كلُّ سجلٍّ نوعُه `EXECUTION` وحالتُه ليست نهائيّة. يجبُ أن يكونَ **صفرًا** — وإلّا يُصرَفُ (يُسلَّمُ أو يُحسَمُ بشريًّا) أوّلًا. لأنَّ الرجوعَ يحذفُ النوعَ فلا يُقرأُ السجلُّ.
3. **الرجوعُ بـ`git revert`** على فرعٍ ودمجٍ تقدُّميٍّ كأيِّ عمل — لا دفعَ بالقوّة.
4. **ما لا رجوعَ فيه بطبيعتِه:** مهمّةٌ شُغِّلَت لا تُعادُ إلى ما قبلَها — وهذا هو سببُ القرارِ ③ نفسِه، لا عيبٌ في الخطّة.

## 7 · أسئلةٌ مفتوحة

### للمراجعين (يُعادُ تشغيلُها)

- **R-1:** أعيدوا أمرَ § 2 وتأكّدوا أنَّ المواضعَ ثمانيةٌ لا غير، ولا موضعَ آخرَ يقرأُ `EXTERNAL` بالاسمِ خارجَ `core/sovereignty/` يتخذُ قرارًا (`rg -n "EffectKind.EXTERNAL" --type py`).
- **R-2:** هل `ExecutiveCore.advance` أحاديّةٌ لكلِّ خطوةٍ إن سقطَ العاملُ بينَ تنفيذِ الخطوةِ وتثبيتِ الحالة؟ إن لم تكن، فالتسليمُ المكرَّرُ قد يُعيدُ خطوة — ويلزمُ `max_attempts = 1` لـ`EXECUTION` أو مفتاحٌ لكلِّ خطوة.
- **R-3:** هل يكفي فحصُ الخلطِ القائمُ ليمنعَ عقدًا واحدًا يجمعُ C1 وC2؟

### للمالك

- **O-1:** قضيّةٌ بقيَ تشغيلُها `DEAD` أو `INDETERMINATE`: تبقى `processing` حتى قرارٍ بشريّ (توصيتي) — أم تُعلَّمُ بحالةٍ جديدةٍ مثلَ «تنتظرُ حسمًا»؟ الثانيةُ تُغيِّرُ مفرداتِ حالةِ القضيّة.
- **O-2:** تسليمٌ متزامنٌ (س) أم لا (ع)؟ — التوصية: (س).

## 8 · ما لم يُفعَلْ — صراحةً

- لم يُكتَبْ سطرُ شِفرةٍ ولا اختبار، ولم يُمَسَّ `core/sovereignty/` ولا `service.py`.
- لم يُسجَّلْ بندُ الشِّفرةِ بعدُ: يُسجَّلُ بعدَ المراجعةِ وجوابِ O-1 وO-2.
- لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذ.
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && git diff --stat 5caeac5bdf9ea446163c40c0a11147fa1e1a9cec HEAD -- core/sovereignty/ federal/executive/services/src/amos_federation/services/government_services/ federal/executive/services/src/amos_federation/services/executive_core/
EXIT: 0
BYTES: 388
SHA256: b15493490dd8d4ee8bbe4826380281e527fafbdc77231b42827afc564f94d46d
NO_EOL: 0
--- OUTPUT ---
 core/sovereignty/enforcement_boundary.py           | 161 +++++++--
 core/sovereignty/idempotency.py                    | 377 ++++++++++++++++++---
 core/sovereignty/jurisdiction.py                   |   5 +
 .../services/executive_core/agent_identity.py      | 143 +++++++-
 .../services/executive_core/sovereignty_bridge.py  |   3 +
 5 files changed, 598 insertions(+), 91 deletions(-)
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "EXTERNAL" core/sovereignty/*.py
EXIT: 0
BYTES: 3954
SHA256: a68037a55bf81d50963eb0a5586e2563876ca80e49ab3e22e32cf5638d1ee7b4
NO_EOL: 0
--- OUTPUT ---
core/sovereignty/__init__.py:122:    "ROOT_EXTERNAL_HUMAN": "crown",
core/sovereignty/__init__.py:165:    "MANDATORY_EXTERNAL_STAGES": "enforcement_boundary",
core/sovereignty/cli.py:27:    ROOT_EXTERNAL_HUMAN,
core/sovereignty/cli.py:134:        if crown.root_origin != ROOT_EXTERNAL_HUMAN:
core/sovereignty/cli.py:137:                f"«{ROOT_EXTERNAL_HUMAN}»: الدولةُ ولّدت مفتاحَ الملك فرأتْه. "
core/sovereignty/contract.py:72:    EXTERNAL = "EXTERNAL"
core/sovereignty/contract.py:89:    EffectKind.EXTERNAL: "نداءٌ خارجيّ",
core/sovereignty/compensation.py:49:`EffectKind.EXTERNAL` **لا يُقبَلُ معوّضًا**. نداءٌ خارجيٌّ وقع لا يُسحَب،
core/sovereignty/compensation.py:103:    {EffectKind.EXTERNAL}
core/sovereignty/compensation.py:173:    """محاولةُ تسجيلِ معوّضٍ لأثرٍ لا يُعكَس (`EXTERNAL`).
core/sovereignty/compensation.py:321:    1. **أثرٌ لا يُعكَس** (`EXTERNAL`) مُعلَنٌ في العقد -> `IrreversibleEffectError`.
core/sovereignty/crown.py:37:ROOT_EXTERNAL_HUMAN = "EXTERNAL_HUMAN_ROOT"   # وُلِّد خارج الدولة — الملكُ وحده رآه
core/sovereignty/crown.py:86:        return self.root_origin == ROOT_EXTERNAL_HUMAN
core/sovereignty/crown.py:438:        "root_origin": ROOT_EXTERNAL_HUMAN,
core/sovereignty/crown.py:448:                "root_origin": ROOT_EXTERNAL_HUMAN,
core/sovereignty/crown.py:451:                    "ceremony_kind": "GENESIS_EXTERNAL_HUMAN_ROOT",
core/sovereignty/enforcement_boundary.py:178:    EXTERNAL_OUTBOX = "EXTERNAL_OUTBOX"          # 1K
core/sovereignty/enforcement_boundary.py:192:MANDATORY_EXTERNAL_STAGES: Final[tuple[BoundaryStage, ...]] = (
core/sovereignty/enforcement_boundary.py:198:    BoundaryStage.EXTERNAL_OUTBOX,
core/sovereignty/enforcement_boundary.py:300:            "mandatory_external_stages": [s.value for s in MANDATORY_EXTERNAL_STAGES],
core/sovereignty/enforcement_boundary.py:385:                and effect.kind is not EffectKind.EXTERNAL
core/sovereignty/enforcement_boundary.py:412:        external_prefix = EffectKind.EXTERNAL.value + ":"
core/sovereignty/enforcement_boundary.py:439:            stages.append(BoundaryStage.EXTERNAL_OUTBOX)
core/sovereignty/enforcement_boundary.py:579:            e for e in contract.declared_effects if e.kind is EffectKind.EXTERNAL
core/sovereignty/enforcement_boundary.py:582:            e for e in contract.mutating_effects if e.kind is not EffectKind.EXTERNAL
core/sovereignty/enforcement_boundary.py:624:            self._record_rejection(BoundaryStage.EXTERNAL_OUTBOX)
core/sovereignty/enforcement_boundary.py:667:            if effect.kind is not EffectKind.EXTERNAL:
core/sovereignty/enforcement_boundary.py:673:                self._record_rejection(BoundaryStage.EXTERNAL_OUTBOX)
core/sovereignty/enforcement_boundary.py:1008:    "MANDATORY_EXTERNAL_STAGES",
core/sovereignty/jurisdiction.py:170:        EffectKind.EXTERNAL,   # التأثيرُ الخارجيُّ شأنٌ تنفيذيّ
core/sovereignty/jurisdiction.py:322:        وأمّا `DELETE` و`TRANSFER` و`EXTERNAL` فخارجةٌ عن السلطةِ القضائيّة:
core/sovereignty/idempotency.py:34:- **الأثرُ الخارجيُّ لا يُلغى.** `EffectKind.EXTERNAL` لا يمكنُ التراجعُ عنه
core/sovereignty/idempotency.py:85:    EXTERNAL_PENDING = "EXTERNAL_PENDING"
core/sovereignty/idempotency.py:117:    OperationStatus.EXTERNAL_PENDING: "أثرٌ خارجيٌّ معلّق",
core/sovereignty/idempotency.py:977:        لا تقبلُ آثارًا خارجيّة (`EXTERNAL`): الأثرُ الخارجيُّ يحتاجُ outbox
core/sovereignty/idempotency.py:983:            if sig.startswith(EffectKind.EXTERNAL.value + ":"):
core/sovereignty/outbox.py:973:    if effect.kind is not EffectKind.EXTERNAL:
core/sovereignty/outbox.py:1360:        kind=EffectKind.EXTERNAL,
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "EffectKind.EXTERNAL" --type py
EXIT: 0
BYTES: 2714
SHA256: 5d0211aa6ac9c9566d6140f6eca90a7abd5b081da0b73a56a07cd501c57d88e9
NO_EOL: 0
--- OUTPUT ---
tests/sovereignty/test_enforcement_integration.py:369:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
tests/sovereignty/test_enforcement_integration.py:393:                declared_effects=(_أثر(EffectKind.EXTERNAL, NOTICE),),
tests/sovereignty/test_compensation.py:230:                SovereignEffect(kind=EffectKind.EXTERNAL, resource=f"{TARGET}/swift"),
tests/sovereignty/test_compensation.py:246:        assert EffectKind.EXTERNAL in IRREVERSIBLE_EFFECT_KINDS
tests/sovereignty/test_enforcement_boundary.py:273:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
tests/sovereignty/test_enforcement_boundary.py:575:        خارجيّ = _أثر(EffectKind.EXTERNAL, TARGET)
tests/sovereignty/test_enforcement_boundary.py:591:        خارجيّ = _أثر(EffectKind.EXTERNAL, TARGET)
tests/sovereignty/test_enforcement_boundary.py:617:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
tests/sovereignty/test_enforcement_boundary.py:637:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
tests/sovereignty/test_enforcement_boundary.py:653:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
tests/sovereignty/test_enforcement_boundary.py:669:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
tests/sovereignty/test_enforcement_boundary.py:957:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
core/sovereignty/enforcement_boundary.py:385:                and effect.kind is not EffectKind.EXTERNAL
core/sovereignty/enforcement_boundary.py:412:        external_prefix = EffectKind.EXTERNAL.value + ":"
core/sovereignty/enforcement_boundary.py:579:            e for e in contract.declared_effects if e.kind is EffectKind.EXTERNAL
core/sovereignty/enforcement_boundary.py:582:            e for e in contract.mutating_effects if e.kind is not EffectKind.EXTERNAL
core/sovereignty/enforcement_boundary.py:667:            if effect.kind is not EffectKind.EXTERNAL:
core/sovereignty/compensation.py:49:`EffectKind.EXTERNAL` **لا يُقبَلُ معوّضًا**. نداءٌ خارجيٌّ وقع لا يُسحَب،
core/sovereignty/compensation.py:103:    {EffectKind.EXTERNAL}
core/sovereignty/contract.py:89:    EffectKind.EXTERNAL: "نداءٌ خارجيّ",
core/sovereignty/jurisdiction.py:170:        EffectKind.EXTERNAL,   # التأثيرُ الخارجيُّ شأنٌ تنفيذيّ
core/sovereignty/idempotency.py:34:- **الأثرُ الخارجيُّ لا يُلغى.** `EffectKind.EXTERNAL` لا يمكنُ التراجعُ عنه
core/sovereignty/idempotency.py:983:            if sig.startswith(EffectKind.EXTERNAL.value + ":"):
core/sovereignty/outbox.py:973:    if effect.kind is not EffectKind.EXTERNAL:
core/sovereignty/outbox.py:1360:        kind=EffectKind.EXTERNAL,
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "def advance|def run|is_terminal|max_attempts" federal/executive/services/src/amos_federation/services/executive_core/engine.py
EXIT: 0
BYTES: 552
SHA256: cbe03bdcd9bf5b771a10f08ed636a4f776008f70bc966db1da74c910a6f78bc1
NO_EOL: 0
--- OUTPUT ---
69:    is_terminal,
331:    def advance(self, task_id: str) -> TransitionOutcome:
335:        if is_terminal(state):
561:    def run(self, task_id: str, max_steps: int = 8) -> dict[str, Any]:
566:            if is_terminal(state):
574:            "terminal": is_terminal(task["status"]),
577:    def advance_to(self, task_id: str, target: TaskState, max_steps: int = 8) -> dict[str, Any]:
588:            if state is target or is_terminal(state):
597:            "terminal": is_terminal(task["status"]),
663:            "terminal": is_terminal(state),
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "def process_case" -A 60 federal/executive/services/src/amos_federation/services/government_services/service.py
EXIT: 0
BYTES: 2730
SHA256: 8af0230c33c4dfb7046f54a0beed108fb9909ca71ca2bf6d9b17d56c53aed82d
NO_EOL: 0
--- OUTPUT ---
1041:    def process_case(
1042-        self, *, context: AuthorizationContext, reference: str, max_steps: int = 8
1043-    ) -> dict[str, Any]:
1044-        """شغِّل مهمّة القضية عبر `ExecutiveCore.run` — ولا تلمس حالة المهمّة هنا.
1045-
1046-        الحالة النهائية تُخزَّن كما قالها العمود التنفيذي، نجاحًا أو فشلًا. وإن لم
1047-        يوجد وكيل مؤهَّل فالمهمّة تفشل، ويُخزَّن `failed` ولا يُدَّعى غيره.
1048-        """
1049-        require_domain_permission(context, "gov.case.process", PERMISSIONS_CASE_PROCESS)
1050-        session = self._session()
1051-        try:
1052-            case = self._case_row(session, context, reference)
1053-            if case.status not in {"submitted", "assigned", "processing"}:
1054-                raise CaseStateError(
1055-                    f"القضية '{reference}' حالتها '{case.status}' — لا معالجة بعد المراجعة"
1056-                )
1057-            task_id = case.task_id
1058-            case.status = "processing"
1059-            case.updated_at = _now()
1060-            session.commit()
1061-        finally:
1062-            session.close()
1063-
1064-        outcome = self._core.run(task_id, max_steps=max_steps)
1065-        final_state = str(outcome["final_state"])
1066-        terminal = bool(outcome["terminal"])
1067-
1068-        session = self._session()
1069-        try:
1070-            case = self._case_row(session, context, reference)
1071-            case.review_state = final_state
1072-            case.status = "reviewed" if terminal else "processing"
1073-            case.updated_at = _now()
1074-            session.commit()
1075-            entity = self._case_dict(case)
1076-        finally:
1077-            session.close()
1078-
1079-        trace = record_domain_trace(
1080-            context,
1081-            "gov.case.review",
1082-            EVENT_CASE_REVIEWED,
1083-            {
1084-                "case_id": entity["id"],
1085-                "reference": entity["reference"],
1086-                "task_id": task_id,
1087-                "task_final_state": final_state,
1088-                "terminal": terminal,
1089-                "tenant_id": entity["tenant_id"],
1090-            },
1091-        )
1092-        return {**entity, "task_final_state": final_state, "terminal": terminal, **trace}
1093-
1094-    def decide_case(
1095-        self,
1096-        *,
1097-        context: AuthorizationContext,
1098-        reference: str,
1099-        outcome: str,
1100-        rationale: str,
1101-        official_id: str | None = None,
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3221
SHA256: 45204a1ce3bf8c187a5cabc3d4c0e40243e36778eaa3d8810b6097ebe52906ed
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 239
  عمليّاتٌ عامّةٌ مُغيِّرة   : 190
  منها تعبرُ الحدَّ        : 46
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 142
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          160 /  46 /  113
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
      10  federal/executive/services/src/amos_federation/services/federal_state/service.py
       9  federal/executive/services/src/amos_federation/services/governance/treasury.py
       9  federal/executive/services/src/amos_federation/services/royal/main.py
       8  federal/executive/services/src/amos_federation/services/governance/expansion.py
       7  federal/executive/services/src/amos_federation/services/governance/learning_cycle.py
       7  federal/executive/services/src/amos_federation/services/governance/system_life.py
       7  federal/executive/services/src/amos_federation/services/state_treasury/service.py
       6  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
       5  federal/executive/services/src/amos_federation/services/agent_runtime/health.py
       5  federal/executive/services/src/amos_federation/services/governance/security.py
       5  federal/executive/services/src/amos_federation/services/governance/state_runtime.py
       4  federal/executive/services/src/amos_federation/common/database.py
       3  federal/executive/services/src/amos_federation/services/agent_runtime/population.py
       3  federal/executive/services/src/amos_federation/services/executive_core/repository.py
       2  federal/executive/services/src/amos_federation/common/durable_event_bus.py
       2  federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
       2  federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py
       2  federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py
       2  federal/executive/services/src/amos_federation/services/training/persistent_registry.py
       1  federal/executive/services/src/amos_federation/common/event_bus.py
       1  federal/executive/services/src/amos_federation/common/events.py
       1  federal/executive/services/src/amos_federation/services/api_gateway/store.py
       1  federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py
       1  federal/executive/services/src/amos_federation/services/government_services/service.py
       1  tools/migrations/r4_unify_agent_identity.py
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && rg -n "Q-16" docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 0
BYTES: 10923
SHA256: d627498a47ab671d24bd889c75b907707e39c5d4e12f36dce6d7022ec3606259
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-23 (`W-636/W-637` — تسجيلُ WI-109 (تحليلُ A1) · WI-110 (تحليلُ Q-9) · WI-111 (J2+J3 · 15 سطحًا محسومًا مقيسًا) READY · حرسُ D21-د تحتَ WI-040 (`NEW_ITEM_CLAIMING_ENTRY`) · N+1 لـW-631…W-635 أخضرُ (40030379965) · تصحيحُ تاريخِ الرياضِ في D21-هـ) · ووقبله ((`W-632…W-635` — قراراتُ المالكِ بتوجيهِ المستشارِ 21 على ورقةِ D20 بنصوصِها الحرفيّةِ: Q-7 · Q-8 · Q-13 · Q-14 · Q-23 · Q-26 · Q-28 · Q-29 · Q-30 · Q-32 · Q-33 · Q-34 · Q-36 · Q-37 · Q-41 · E1 DECIDED · وA1 وQ-9 وQ-10 تحليلٌ/قياسٌ أوّلًا) · ووقبله (`W-625` — **Q-71 DECIDED** بأمرِ المالكِ الصريحِ: «أذن بـconftest.py تحت WI-107» — قسمةُ نطاقِ مسارِ conftest.py من WI-072 إلى WI-107) · ووقبله (`W-612` — **D17-2** الأربعةُ مؤجَّلةٌ ولا تعطّلُ J2/J3 · **إبلاغُ ما بعدَ الدمجِ** يبقى إبلاغًا (توجيهُ المستشارِ 19 § 1)) · ووقبله ((`W-611` — **Q-61 DECIDED** بالخيارِ (3) بتطبيقٍ صريحٍ على WI-096 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-610` — **D19 DECIDED**: إذنُ المالكِ بإغلاقِ WI-105 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`))))
279:| **`HUMAN_DECISION_REQUIRED`** | **19** | Q-2 · Q-3 · Q-4 · Q-8 · Q-13 · Q-14 · Q-15 · Q-16 · Q-17 · Q-18 · Q-19 · Q-20 · Q-21 · Q-22 · Q-23 · Q-24 · Q-25 · Q-26 · Q-27 |
281:**Q-16 حاضرٌ ولم يُسقَطْ:** فعلُ `process_case` قضائيٌّ حصريٌّ بفاعلٍ تنفيذيّ · يُوقِفُ P5ز.
394:## Q-16 · هل يُعلَنُ تشغيلُ المهمّةِ أثرًا، وبأيِّ معكوسٍ صادق؟
426:### إضافةٌ مؤرَّخةٌ — قرارُ المالكِ في Q-16 (2026-10-16 · الرياض 10:00 · `W-363`)
604:تحتَ فاعلٍ قضائيٍّ يخالفُ حدَّ الاختصاصِ نصًّا، وتشغيلُ المهمّةِ هو عينُ **Q-16**.
616:- **ما يُفتَحُ بعدَه:** هجرةُ عمليّتَي `federal_judiciary/service.py` (‏`:728` و`:812` في نصِّ السؤال) **بعدَ هجرةِ Q-6** في T1. **وشقُّ تشغيلِ المهمّةِ فيه معلَّقٌ على تنفيذِ Q-16** (نوعُ الأثرِ `EXECUTION`) — فلا يُهاجَرُ ذلك الشقُّ قبلَ استيفاءِ شرطَي Q-16.
3049:| Q-16 | ③ نوعُ أثرٍ جديدٌ `EXECUTION` | DECIDED في الاختيار · التنفيذُ مشروط | إضافةٌ في § Q-16 |
3060:- **الأثر:** شرطُ Q-16 (ب) · و`CLOSED` لـ`WI-076` · وكلُّ `VERIFIED` لبندٍ حسّاسٍ بعدَ قانونِ `Q-H` — **كلُّها تنتظرُ قناةَ المقعدِ الثاني**.
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && sha256sum docs/audit/evidence/W-641/briefs_wi084/briefing_kimi_k3.md
EXIT: 0
BYTES: 125
SHA256: b2a2fac971dae49268f07d58b4f474920d64a65b4321eff09f7ec6ea713b7cc9
NO_EOL: 0
--- OUTPUT ---
efd2a62be97ff5a79e5766452bd74059faa9cc6388fe4b3dd5f2da7e85103711  docs/audit/evidence/W-641/briefs_wi084/briefing_kimi_k3.md
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && cat docs/audit/evidence/W-641/briefs_wi084/SHA256SUMS
EXIT: 0
BYTES: 268
SHA256: d8c440a0fb5fc454195863b7b6e7b550ba7f850a570283b0e860e180a84fc697
NO_EOL: 0
--- OUTPUT ---
3d0e312df55ab0e0c0ce7ca4eafcfd9c585536903ed409c388fbd7c832ef380d  briefing_gemini_3_8_flash.md
aade023781b0e7a49cbcb6012f8ab899e4d7f75c58c2a852fdbaff73ffef1710  briefing_grok_4_7.md
efd2a62be97ff5a79e5766452bd74059faa9cc6388fe4b3dd5f2da7e85103711  briefing_kimi_k3.md
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w641/kimi_k3/wi084/probe/probe_wi084_kimi_k3.py
EXIT: 0
BYTES: 10392
SHA256: 0e7e53853886e26664221dd5c5c57ef3ad6d72a7e23910436d0d4d0a417a8d0b
NO_EOL: 0
--- OUTPUT ---
     1	"""
     2	مسبارُ المقعدِ kimi_k3 الخاصُّ لجولةِ WI-084 (تصميمُ نوعِ الأثرِ EXECUTION) —
     3	يُنادي المسارَ الإنتاجيَّ في core/sovereignty وحدَه، ويحاولُ تكذيبَ ادّعاءاتِ
     4	الوثيقةِ عن سلوكِ «اليوم» (الملحقِ § 1 و§ 2 — Q16_EXECUTION_EFFECT_DESIGN.md):
     5	
     6	  P1 · § 2 الموضعُ 5 (وجوابُ سؤالِ المراجعةِ R-3 بيدِ المقعد): عقدٌ يخلطُ
     7	       كتابةً داخليّةً (WRITE) بأثرٍ خارجيٍّ (EXTERNAL) يجبُ أن يُرفَضَ من
     8	       المسارِ الإنتاجيِّ SovereignExecutionBoundary.execute بـ
     9	       MixedEffectContractError قبلَ أيِّ تطبيق — حتى مع معوّضٍ قانونيٍّ
    10	       يغطّي الكتابة. إن مرَّ العقدُ ووقعَ أيُّ أثرٍ… انكسرتِ الخاصيّةُ.
    11	  P2 · § 2 الموضعُ 1: bind_compensation_plan لعقدٍ يحوي EXTERNAL يجبُ أن
    12	       يرفعَ IrreversibleEffectError ولو أُعطيَ معوّضٌ زائفٌ له — إن رُبِطَت
    13	       الخطّة… انكسرتِ الخاصيّةُ.
    14	  P3 · § 2 الموضعُ 8: صندوقُ الصادرِ يجبُ أن يرفضَ أثرًا غيرَ EXTERNAL
    15	       («ليس خارجيًّا») ولو حملَ إذنًا موقَّعًا صحيحًا لذلك الأثرِ نفسِه —
    16	       إن أُدرِجَ… انكسرتِ الخاصيّةُ.
    17	
    18	يُشغَّلُ بـ .venv من جذرِ المستودعِ مع PYTHONPATH=جذرِ المستودع — بلا نسخٍ داخله.
    19	رمزُ الخروجِ 0 = كلُّ الادّعاءاتِ صمدَت (لم تنكسرْ خاصيّة)، وغيرُ 0 = كسر.
    20	"""
    21	
    22	from __future__ import annotations
    23	
    24	import sys
    25	import tempfile
    26	import traceback
    27	from pathlib import Path
    28	
    29	from cryptography.hazmat.primitives.asymmetric import ed25519
    30	
    31	from core.constitutional_engine.engine import ConstitutionalEngine
    32	from core.constitutional_engine.ledger import ConstitutionalLedger
    33	from core.constitutional_engine.model import ActionRequest, Branch
    34	from core.sovereignty.compensation import (
    35	    Compensator,
    36	    IrreversibleEffectError,
    37	    bind_compensation_plan,
    38	)
    39	from core.sovereignty.contract import EffectKind, SovereignEffect, bind_contract
    40	from core.sovereignty.enforcement import ConsumedPermitLedger, issue_permit, sign_permit
    41	from core.sovereignty.enforcement_boundary import (
    42	    MixedEffectContractError,
    43	    SovereignExecutionBoundary,
    44	)
    45	from core.sovereignty.gateway import SovereignGateway
    46	from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger
    47	from core.sovereignty.outbox import OutboxLedger, SovereignOutbox
    48	
    49	TARGET_TREASURY = "kimi-probe/treasury"
    50	TARGET_NOTICE = "kimi-probe/notice"
    51	
    52	
    53	def _fresh_boundary(workdir: Path) -> tuple[SovereignExecutionBoundary, SovereignGateway]:
    54	    gateway = SovereignGateway(
    55	        ConstitutionalEngine(ledger=ConstitutionalLedger(workdir / "ledger.jsonl"))
    56	    )
    57	    outbox = SovereignOutbox(
    58	        ledger=OutboxLedger(workdir / "outbox.json"),
    59	        verifying_key=ed25519.Ed25519PublicKey.from_public_bytes(
    60	            bytes.fromhex(gateway.verifying_key_hex)
    61	        ),
    62	    )
    63	    boundary = SovereignExecutionBoundary(
    64	        gateway=gateway,
    65	        idempotency_ledger=IdempotencyLedger(workdir / "idem.json"),
    66	        outbox=outbox,
    67	        consumed_permits=ConsumedPermitLedger(workdir / "consumed.json"),
    68	    )
    69	    return boundary, gateway
    70	
    71	
    72	def probe_p1_mix_refused_before_any_effect(workdir: Path) -> str:
    73	    state = {TARGET_TREASURY: "1000", TARGET_NOTICE: "QUEUED"}
    74	    boundary, _ = _fresh_boundary(workdir)
    75	    # نطاقُ العقدِ يفرضُ أن تكونَ الآثارُ على الهدفِ نفسِه — فالخلطُ هنا على موردٍ واحد.
    76	    internal = SovereignEffect(kind=EffectKind.WRITE, resource=TARGET_TREASURY, detail="مسبار p1")
    77	    external = SovereignEffect(kind=EffectKind.EXTERNAL, resource=TARGET_TREASURY, detail="مسبار p1")
    78	
    79	    def _applier(effect: SovereignEffect) -> None:
    80	        state[effect.resource] = "TOUCHED-BY-PROBE"
    81	
    82	    try:
    83	        boundary.execute(
    84	            ActionRequest(
    85	                actor=Branch.EXECUTIVE,
    86	                action="credit_account",
    87	                target=TARGET_TREASURY,
    88	                channel="official",
    89	            ),
    90	            declared_effects=(internal, external),
    91	            planner=lambda _: (internal, external),
    92	            applier=_applier,
    93	            operation_key=IdempotencyKey(scope="kimi-probe", value="mix-1"),
    94	            compensators=(
    95	                Compensator(
    96	                    effect_signature=internal.signature,
    97	                    apply=lambda: state.update({TARGET_TREASURY: "1000"}),
    98	                    description="إرجاعُ القيمةِ الأصليّة",
    99	                ),
   100	            ),
   101	        )
   102	    except MixedEffectContractError:
   103	        pass
   104	    else:
   105	        return "BROKEN: مرَّ عقدٌ يخلطُ الكتابةَ بالخارجيِّ بلا MixedEffectContractError"
   106	
   107	    if state[TARGET_TREASURY] != "1000" or state[TARGET_NOTICE] != "QUEUED":
   108	        return "BROKEN: وقعَ أثرٌ رغمَ الرفضِ: " + repr(state)
   109	    return "OK: رُفِضَ العقدُ المختلطُ بـMixedEffectContractError ولا أثرَ وقع"
   110	
   111	
   112	def probe_p2_irreversible_effect_unbindable() -> str:
   113	    external = SovereignEffect(kind=EffectKind.EXTERNAL, resource=TARGET_NOTICE, detail="مسبار p2")
   114	    contract = bind_contract(
   115	        actor=Branch.EXECUTIVE,
   116	        action="notify",
   117	        target=TARGET_NOTICE,
   118	        declared_effects=(external,),
   119	    )
   120	    fake_compensator = Compensator(
   121	        effect_signature=external.signature,
   122	        apply=lambda: None,
   123	        description="معوّضٌ زائفٌ لأثرٍ خارجيٍّ (محاولةُ كسرٍ)",
   124	    )
   125	    try:
   126	        bind_compensation_plan(contract=contract, compensators=(fake_compensator,))
   127	    except IrreversibleEffectError:
   128	        return "OK: رُفِضَ ربطُ خطّةٍ بعقدٍ خارجيٍّ (IrreversibleEffectError)"
   129	    return "BROKEN: bind_compensation_plan لم يرفضْ أثرَ EXTERNAL"
   130	
   131	
   132	def probe_p3_outbox_rejects_non_external(workdir: Path) -> str:
   133	    private_key = ed25519.Ed25519PrivateKey.generate()
   134	    outbox = SovereignOutbox(
   135	        ledger=OutboxLedger(workdir / "outbox3.json"),
   136	        verifying_key=private_key.public_key(),
   137	    )
   138	    internal = SovereignEffect(kind=EffectKind.WRITE, resource=TARGET_TREASURY, detail="مسبار p3")
   139	    contract = bind_contract(
   140	        actor=Branch.EXECUTIVE,
   141	        action="credit_account",
   142	        target=TARGET_TREASURY,
   143	        declared_effects=(internal,),
   144	    )
   145	    permit = sign_permit(
   146	        issue_permit(
   147	            contract=contract,
   148	            request_fingerprint="RF-KIMI-P3",
   149	            decision="ALLOW",
   150	            ledger_entry_hash="anchor-kimi",
   151	            private_key=private_key,
   152	            authority_layer="EXECUTIVE",
   153	            decision_kind="ORDINARY",
   154	            ttl_seconds=3600,
   155	        ),
   156	        private_key,
   157	    )
   158	    try:
   159	        outbox.enqueue(
   160	            permit=permit,
   161	            effect=internal,
   162	            operation_key="kimi-probe:p3",
   163	            provider=None,  # type: ignore[arg-type] — يسقطُ قبلَ أيِّ مزوّد
   164	            payload=None,  # type: ignore[arg-type]
   165	        )
   166	    except Exception as exc:  # نتوقّع OutboxError «ليس خارجيًّا»
   167	        from core.sovereignty.outbox import OutboxError
   168	
   169	        if isinstance(exc, OutboxError) and "ليس خارجيّا" in str(exc).replace("ً", ""):
   170	            return "OK: رفضَ الصادرُ أثرًا غيرَ خارجيٍّ رغمَ الإذنِ الموقَّع (OutboxError)"
   171	        return f"BROKEN: رُفِضَ لكن بغيرِ العلةِ المُدَّعاة: {type(exc).__name__}: {exc}"
   172	    return "BROKEN: الصادرُ قبِلَ أثرًا غيرَ EXTERNAL"
   173	
   174	
   175	def main() -> int:
   176	    results: list[str] = []
   177	    with tempfile.TemporaryDirectory(prefix="kimi-wi084-p1-") as tmp:
   178	        results.append("P1 ... " + probe_p1_mix_refused_before_any_effect(Path(tmp)))
   179	    results.append("P2 ... " + probe_p2_irreversible_effect_unbindable())
   180	    with tempfile.TemporaryDirectory(prefix="kimi-wi084-p3-") as tmp:
   181	        results.append("P3 ... " + probe_p3_outbox_rejects_non_external(Path(tmp)))
   182	
   183	    broken = [r for r in results if "BROKEN" in r]
   184	    for line in results:
   185	        print(line, flush=True)
   186	    print(
   187	        "الخلاصة: " + ("انكسرت خاصيّةٌ واحدةٌ على الأقلّ — ملاحظةٌ حاجبة" if broken
   188	                         else "صمدَت الادّعاءاتُ الثلاثةُ — لا كسرَ"),
   189	        flush=True,
   190	    )
   191	    return 1 if broken else 0
   192	
   193	
   194	if __name__ == "__main__":
   195	    try:
   196	        sys.exit(main())
   197	    except Exception:
   198	        traceback.print_exc()
   199	        sys.exit(2)
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w641/kimi_k3/wi084/repo && PYTHONPATH=/home/user/workspace/council_w641/kimi_k3/wi084/repo .venv/bin/python /home/user/workspace/council_w641/kimi_k3/wi084/probe/probe_wi084_kimi_k3.py
EXIT: 0
BYTES: 410
SHA256: 12f7c7b0f1675dceeb17e8e65a029ffe731181a2b890b3d9aac5e607225522ef
NO_EOL: 0
--- OUTPUT ---
P1 ... OK: رُفِضَ العقدُ المختلطُ بـMixedEffectContractError ولا أثرَ وقع
P2 ... OK: رُفِضَ ربطُ خطّةٍ بعقدٍ خارجيٍّ (IrreversibleEffectError)
P3 ... OK: رفضَ الصادرُ أثرًا غيرَ خارجيٍّ رغمَ الإذنِ الموقَّع (OutboxError)
الخلاصة: صمدَت الادّعاءاتُ الثلاثةُ — لا كسرَ
=== RAW [16] END ===
VERDICT_PER_CRITERION:
(1) نعم — الوثيقةُ تُسمّي المواضعَ الثمانيةَ بملفّاتِها وأسطرِها وسلوكِها قبلًا/بعدًا (كتلة 5: § 2 بالجدول) — وقِيست على العقدةِ الحاضرةِ بلا تخمينٍ: كتلتا 7 و8 تُظهِرانِ المواضعَ الثمانيةَ قائمةً في الملفّاتِ الستةِ نفسِها (enforcement_boundary · compensation · contract · jurisdiction · idempotency · outbox) — الأولُ ثابتُ السطرِ (outbox.py:973) والباقي أُزيحت أسطرُه بتحرّكِ الشِّفرةِ (كتلة 6: 598 إضافةً/91 حذفًا في خمسةِ ملفّاتٍ منها enforcement_boundary وidempotency) — إزاحةُ أسطرٍ بلا تغييرِ عددٍ ولا ملفٍّ: ملاحظةٌ مُسمّاةٌ غيرُ حاجبة (قرأتُها بالأمرِ كما أمرتِ الإحاطةُ). وكتلة 10 تؤكدُ أنَّ جدولَ § 1 عن process_case ما زال دقيقًا سطرًا بسطرٍ (def في :1041 والخطواتُ في 1058–1074).
(2) نعم — تغييرُ العقودِ 1I (التعويض) و1K (الصادر) وأنواعِ الأثرِ موصوفٌ (كتلة 5: § 3-أ/ب/ج) وسلوكُ «اليوم» المؤسِّسُ عليه أثبتَه مسباري على المسارِ الإنتاجيِّ: bind_compensation_plan يرفضُ الأثرَ الخارجيَّ (كتلتا 15/16 · P2) والصادرُ يرفضُ غيرَ EXTERNAL (P3).
(3) نعم — شكلُ process_case بعدَ الهجرةِ وفصلُ التشغيلِ عن كتاباتِ القضيّةِ موصوفانِ بثلاثةِ عقودٍ C1/C2/C3 وترتيبِ فشلٍ (كتلة 5: § 4) — والوضعُ الراهنُ مقيسٌ بيدي: كتلة 10 (الشِّفرةَ الحاضرةَ: commit قبلَ run وبعدَه) وكتلة 11 (الجردُ بالأداةِ يعدُّها دَينًا: موضعٌ واحدٌ في government_services/service.py لا يعبرُ الحدَّ).
(4) نعم — خطّةُ الرجوعِ قابلةٌ للتنفيذ: قيودٌ مرتّبةٌ (ر1–ر3) وشرطُ الصفرِ قبلَ حذفِ النوعِ ورجوعٌ بـrevert (كتلة 5: § 6).
(5) نعم — أسئلةٌ مفتوحةٌ مكتوبةٌ لا مُخمَّنة: للمراجعينَ R-1/R-2/R-3 وللمالكِ O-1/O-2 (كتلة 5: § 7). وأجبتُ عنها بأوامرَ مُلتقَطةٍ: R-1 بالأمرين 7 و8 (المواضعُ ثمانيةٌ ولا قرارَ بالاسمِ خارجَ core/sovereignty — الكتلةُ 8 لا تُظهِرُ إلّا core/sovereignty واختباراتِه) · R-3 بمسباري P1 (فحصُ الخلطِ كافٍ: العقدُ المختلطُ يُرفَضُ قبلَ أيِّ أثرٍ — كتلتا 15/16) · وR-2 يبقى كما كتبه المؤلفُ «غير مقيسٍ بعد»: الأمرُ 9 يعرضُ بنيةَ run/advance بفحصِ is_terminal لكلِّ خطوةٍ ولا يقيسُ نافذةَ السقوطِ — وهو صراحةُ السؤالِ لا تكذيبًا له.
(6) نعم — كلُّ رقمٍ في الوثيقةِ أُعيدَ قياسُه بأمرٍ مُلتقَطٍ (الأوامرُ 6–11 منها أسطرُ المواضعِ وجردُ الدَّينِ) وبصمةُ الإحاطةِ مطابقةٌ (الأمرانِ 13 و14).
(7) نعم من جهةِ مقعدي — هذه الجولةُ إعادةُ تشغيلٍ فعليّةٌ بمسبارٍ خاصٍّ قبلَ أيِّ شِفرةٍ (المعيارُ يحتاجُ مقعدينِ: حكمُ المقعدِ الآخرِ ليس في يدي).
PROBES: مسبارٌ واحدٌ — كتلةُ الشِّفرةِ 15 · كتلةُ التشغيلِ 16 (exit 0 · الخلاصة: «صمدَت الادّعاءاتُ الثلاثةُ — لا كسرَ») · على المسارِ الإنتاجيِّ (core/sovereignty: SovereignExecutionBoundary.execute · bind_compensation_plan · SovereignOutbox.enqueue): (P1) حاولَ تكذيبَ § 2 الموضعِ 5 وجوابَ R-3: عقدٌ يخلطُ WRITE بـEXTERNAL على موردٍ واحدٍ بمعوّضٍ قانونيٍّ للكتابة — انكسرت؟ لا: رُفِضَ بـMixedEffectContractError قبلَ أيِّ أثر (الحالةُ لم تتغيّر) · (P2) حاولَ تكذيبَ الموضعِ 1: ربطُ خطّةِ تعويضٍ بعقدٍ خارجيٍّ بمعوّضٍ زائفٍ — انكسرت؟ لا: IrreversibleEffectError · (P3) حاولَ تكذيبَ الموضعِ 8: إدراجُ أثرِ WRITE بإذنٍ موقَّعٍ صحيحٍ في الصادر — انكسرت؟ لا: OutboxError «ليس خارجيًّا».
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً. (ملاحظتانِ غيرُ حاجبتَين: (١) أسطرُ جدولِ § 2 أُزيح عنها بتحرّكِ الشِّفرةِ — مقيسةٌ بالأمرين 6 و7 بلا تغييرِ مدلول، كما نصَّ إفصاحُ المنسِّقِ (2)؛ (٢) الأمرُ 8 بالصيغةِ المكتوبةِ (‏rg بلا مسار) يعتمدُ على stdin ويُعلَّقُ تحتَ التقطيعِ الآليِّ بلا مِحطّةٍ طرفيّة — شغّلتُ الالتقاطَ نفسَهُ بالنصِّ الحرفيِّ داخلَ طرفيّةٍ وهميّة (script) فالتُقِطَ بلا تعديلٍ في الأمر.)
ISOLATION_DECLARATION: أقرُّ أنّني لم أقرأْ شيئًا خارجَ استنساخي الخاصِّ /home/user/workspace/council_w641/kimi_k3/wi084/repo وهذهِ الإحاطةِ — لا أحكامَ مقاعدَ ولا حزمَ منفِّذ: نعم، بلا أيِّ استثناءٍ.
VERDICT: PASS لكلِّ المعاييرِ (1)–(7).
