# حكمُ مقعدِ المجلسِ — grok_4_7 (عائلةُ grok) · جولةُ WI-084 (W-647)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-084 (الطابورُ الواحدُ · التوجيهُ 19 § 2 · بروتوكولُ Q-59) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذورِهِ الخاصّةِ (council_w641/grok_4_7/wi084) — منسوخٌ آليًّا، وما بعدَ الفاصلِ بايتًا ببايتٍ (sha256 `d01e2696583ac3f6c56b3fa675dab565df6cf14aa2b9ae4c79ef21321fef55a8`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-084 عندَ العقدةِ `4b5b2be5` — إحاطةٌ مبصومةٌ ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-647) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-24

---
MODEL: grok_4_7
FAMILY: grok
RUN_DATE: 2026-10-24 06:56 +00:00
NODE: 4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
CLONE_PATH: /home/user/workspace/council_w641/grok_4_7/wi084/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi084/
 2. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi084/)
 3. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git log --format='%h %cI %s' -- docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
 5. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && cat docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
 6. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git diff --stat 5caeac5bdf9ea446163c40c0a11147fa1e1a9cec HEAD -- core/sovereignty/ federal/executive/services/src/amos_federation/services/government_services/ federal/executive/services/src/amos_federation/services/executive_core/
 7. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "EXTERNAL" core/sovereignty/*.py
 8. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "EffectKind.EXTERNAL" --type py
 9. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "def advance|def run|is_terminal|max_attempts" federal/executive/services/src/amos_federation/services/executive_core/engine.py
 10. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "def process_case" -A 60 federal/executive/services/src/amos_federation/services/government_services/service.py
 11. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 12. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "Q-16" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 13. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && sha256sum docs/audit/evidence/W-641/briefs_wi084/briefing_grok_4_7.md
 14. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && cat docs/audit/evidence/W-641/briefs_wi084/SHA256SUMS
 15. nl -ba /home/user/workspace/council_w641/grok_4_7/wi084/probe/wi084_break_execution_claims.py
 16. cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && .venv/bin/python /home/user/workspace/council_w641/grok_4_7/wi084/probe/wi084_break_execution_claims.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi084/
EXIT: 0
BYTES: 41
SHA256: a3e2f8d92a955524b52c488f6eab3a10df32c172749d966186bbfc125cdea034
NO_EOL: 0
--- OUTPUT ---
4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi084/)
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
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: a3e2f8d92a955524b52c488f6eab3a10df32c172749d966186bbfc125cdea034
NO_EOL: 0
--- OUTPUT ---
4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git log --format='%h %cI %s' -- docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
EXIT: 0
BYTES: 252
SHA256: 38d929e32dd28bb5f280e4bec872d5debe92eda25f894a5dcdf8c1a8f7ac31c0
NO_EOL: 0
--- OUTPUT ---
5caeac5b 2026-10-16T08:56:27Z W-398: WI-084 — وثيقةُ تصميمِ نوعِ الأثرِ EXECUTION (Q-16 ③): 8 مواضعِ قرارٍ في 6 ملفّات · ثلاثةُ عقودٍ لـprocess_case · خطّةُ رجوع · بلا شِفرة
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && cat docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
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
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && git diff --stat 5caeac5bdf9ea446163c40c0a11147fa1e1a9cec HEAD -- core/sovereignty/ federal/executive/services/src/amos_federation/services/government_services/ federal/executive/services/src/amos_federation/services/executive_core/
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
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "EXTERNAL" core/sovereignty/*.py
EXIT: 0
BYTES: 3954
SHA256: 42467056eb4e995a93edd9f9d8498f215afe9757ad530afa3be059dff75c2a91
NO_EOL: 0
--- OUTPUT ---
core/sovereignty/cli.py:27:    ROOT_EXTERNAL_HUMAN,
core/sovereignty/cli.py:134:        if crown.root_origin != ROOT_EXTERNAL_HUMAN:
core/sovereignty/cli.py:137:                f"«{ROOT_EXTERNAL_HUMAN}»: الدولةُ ولّدت مفتاحَ الملك فرأتْه. "
core/sovereignty/contract.py:72:    EXTERNAL = "EXTERNAL"
core/sovereignty/contract.py:89:    EffectKind.EXTERNAL: "نداءٌ خارجيّ",
core/sovereignty/__init__.py:122:    "ROOT_EXTERNAL_HUMAN": "crown",
core/sovereignty/__init__.py:165:    "MANDATORY_EXTERNAL_STAGES": "enforcement_boundary",
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
core/sovereignty/idempotency.py:34:- **الأثرُ الخارجيُّ لا يُلغى.** `EffectKind.EXTERNAL` لا يمكنُ التراجعُ عنه
core/sovereignty/idempotency.py:85:    EXTERNAL_PENDING = "EXTERNAL_PENDING"
core/sovereignty/idempotency.py:117:    OperationStatus.EXTERNAL_PENDING: "أثرٌ خارجيٌّ معلّق",
core/sovereignty/idempotency.py:977:        لا تقبلُ آثارًا خارجيّة (`EXTERNAL`): الأثرُ الخارجيُّ يحتاجُ outbox
core/sovereignty/idempotency.py:983:            if sig.startswith(EffectKind.EXTERNAL.value + ":"):
core/sovereignty/compensation.py:49:`EffectKind.EXTERNAL` **لا يُقبَلُ معوّضًا**. نداءٌ خارجيٌّ وقع لا يُسحَب،
core/sovereignty/compensation.py:103:    {EffectKind.EXTERNAL}
core/sovereignty/compensation.py:173:    """محاولةُ تسجيلِ معوّضٍ لأثرٍ لا يُعكَس (`EXTERNAL`).
core/sovereignty/compensation.py:321:    1. **أثرٌ لا يُعكَس** (`EXTERNAL`) مُعلَنٌ في العقد -> `IrreversibleEffectError`.
core/sovereignty/crown.py:37:ROOT_EXTERNAL_HUMAN = "EXTERNAL_HUMAN_ROOT"   # وُلِّد خارج الدولة — الملكُ وحده رآه
core/sovereignty/crown.py:86:        return self.root_origin == ROOT_EXTERNAL_HUMAN
core/sovereignty/crown.py:438:        "root_origin": ROOT_EXTERNAL_HUMAN,
core/sovereignty/crown.py:448:                "root_origin": ROOT_EXTERNAL_HUMAN,
core/sovereignty/crown.py:451:                    "ceremony_kind": "GENESIS_EXTERNAL_HUMAN_ROOT",
core/sovereignty/outbox.py:973:    if effect.kind is not EffectKind.EXTERNAL:
core/sovereignty/outbox.py:1360:        kind=EffectKind.EXTERNAL,
core/sovereignty/jurisdiction.py:170:        EffectKind.EXTERNAL,   # التأثيرُ الخارجيُّ شأنٌ تنفيذيّ
core/sovereignty/jurisdiction.py:322:        وأمّا `DELETE` و`TRANSFER` و`EXTERNAL` فخارجةٌ عن السلطةِ القضائيّة:
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "EffectKind.EXTERNAL" --type py
EXIT: 0
BYTES: 2714
SHA256: 1ee1b9d686518586155d68db110529c86ff2179df3ce85c8e2f2d8eccf89f7c0
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
core/sovereignty/outbox.py:973:    if effect.kind is not EffectKind.EXTERNAL:
core/sovereignty/outbox.py:1360:        kind=EffectKind.EXTERNAL,
core/sovereignty/idempotency.py:34:- **الأثرُ الخارجيُّ لا يُلغى.** `EffectKind.EXTERNAL` لا يمكنُ التراجعُ عنه
core/sovereignty/idempotency.py:983:            if sig.startswith(EffectKind.EXTERNAL.value + ":"):
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "def advance|def run|is_terminal|max_attempts" federal/executive/services/src/amos_federation/services/executive_core/engine.py
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
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "def process_case" -A 60 federal/executive/services/src/amos_federation/services/government_services/service.py
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
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
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
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && rg -n "Q-16" docs/audit/SOVEREIGN_DECISION_REGISTER.md
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
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && sha256sum docs/audit/evidence/W-641/briefs_wi084/briefing_grok_4_7.md
EXIT: 0
BYTES: 126
SHA256: e7e8ff94102d50c623e25967fc641c78c241f76d23a57dc6f0252fcd703e7da1
NO_EOL: 0
--- OUTPUT ---
aade023781b0e7a49cbcb6012f8ab899e4d7f75c58c2a852fdbaff73ffef1710  docs/audit/evidence/W-641/briefs_wi084/briefing_grok_4_7.md
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && cat docs/audit/evidence/W-641/briefs_wi084/SHA256SUMS
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
CMD: nl -ba /home/user/workspace/council_w641/grok_4_7/wi084/probe/wi084_break_execution_claims.py
EXIT: 0
BYTES: 7873
SHA256: aebbc81c15566a40e5e9ff28a678e9c38fb898a9c9b59939969e7bef7207931c
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ مقعدِ grok_4_7 لـWI-084 — يحاولُ كسرَ ادّعاءاتِ سلوكِ اليومِ في الوثيقةِ.
     3	
     4	ليس فحصًا قائمًا ولا أمرًا من القسمِ ج. ينادي:
     5	  bind_compensation_plan · SovereignOutbox.enqueue · حدَّ التنفيذِ · ExecutiveCore.run
     6	"""
     7	from __future__ import annotations
     8	
     9	import sys
    10	from pathlib import Path
    11	
    12	REPO = Path("/home/user/workspace/council_w641/grok_4_7/wi084/repo")
    13	TMP = Path("/home/user/workspace/council_w641/grok_4_7/wi084/tmp")
    14	sys.path.insert(0, str(REPO))
    15	sys.path.insert(0, str(REPO / "federal/executive/services/src"))
    16	
    17	from cryptography.hazmat.primitives.asymmetric import ed25519
    18	
    19	from amos_federation.services.executive_core.engine import ExecutiveCore
    20	from core.sovereignty.compensation import (
    21	    Compensator,
    22	    IrreversibleEffectError,
    23	    bind_compensation_plan,
    24	)
    25	from core.sovereignty.contract import EffectKind, SovereignEffect, bind_contract
    26	from core.sovereignty.enforcement import EnforcementPermit
    27	from core.sovereignty.enforcement_boundary import (
    28	    MixedEffectContractError,
    29	    SovereignExecutionBoundary,
    30	)
    31	from core.sovereignty.gateway import SovereignGateway
    32	from core.sovereignty.idempotency import IdempotencyLedger
    33	from core.sovereignty.outbox import EffectPayload, OutboxError, SovereignOutbox
    34	
    35	
    36	class _Provider:
    37	    name = "probe-provider"
    38	    supports_idempotency = True
    39	
    40	    def deliver(self, envelope):  # pragma: no cover — يجب ألا يُنادى
    41	        raise AssertionError("التسليمُ وُصِلَ والمُفتَرَضُ الرفضُ قبلَه")
    42	
    43	
    44	class _Repo:
    45	    def __init__(self) -> None:
    46	        self.task = {"id": "task-probe", "status": "completed"}
    47	
    48	    def state_of(self, task_id: str) -> str:
    49	        return self.task["status"]
    50	
    51	    def require(self, task_id: str) -> dict:
    52	        return dict(self.task)
    53	
    54	
    55	def _effect(kind: EffectKind, resource: str) -> SovereignEffect:
    56	    return SovereignEffect(kind=kind, resource=resource, detail="probe")
    57	
    58	
    59	def _contract(*effects: SovereignEffect):
    60	    return bind_contract(
    61	        actor="EXECUTIVE",
    62	        action="gov.case.process",
    63	        target="gov.case",
    64	        declared_effects=effects,
    65	    )
    66	
    67	
    68	def main() -> int:
    69	    held: list[str] = []
    70	    broken: list[str] = []
    71	
    72	    external = _effect(EffectKind.EXTERNAL, "gov.case/notice")
    73	    write = _effect(EffectKind.WRITE, "gov.case/status")
    74	    sneaked: list[str] = []
    75	    try:
    76	        bind_compensation_plan(
    77	            contract=_contract(external),
    78	            compensators=(
    79	                Compensator(
    80	                    effect_signature=external.signature,
    81	                    apply=lambda: sneaked.append("applied"),
    82	                    description="محاولةُ عكسِ أثرٍ خارجيٍّ",
    83	                ),
    84	            ),
    85	        )
    86	    except IrreversibleEffectError as exc:
    87	        if sneaked:
    88	            broken.append("compensation: رُفِضَ العقدُ بعدَ تنفيذِ المعوِّض")
    89	        else:
    90	            held.append(f"compensation: IrreversibleEffectError قبلَ أيِّ عكس ({exc.__class__.__name__})")
    91	    except Exception as exc:
    92	        broken.append(f"compensation: استثناءٌ غيرُ المُدَّعى {type(exc).__name__}: {exc}")
    93	    else:
    94	        broken.append("compensation: قُبِلَ معوِّضٌ لأثرٍ EXTERNAL")
    95	
    96	    key = ed25519.Ed25519PrivateKey.generate().public_key()
    97	    box = SovereignOutbox(ledger=object(), verifying_key=key)
    98	    permit = EnforcementPermit(
    99	        permit_id="permit-probe",
   100	        actor="EXECUTIVE",
   101	        action="gov.case.process",
   102	        target="gov.case",
   103	        contract_id="contract-probe",
   104	        effect_signatures=(write.signature,),
   105	        decision="ALLOW",
   106	        authority_layer="EXECUTIVE",
   107	        decision_kind="ALLOW",
   108	        request_fingerprint="probe",
   109	        ledger_entry_hash=None,
   110	        issued_at="2026-10-24T00:00:00+00:00",
   111	        expires_at="2026-10-25T00:00:00+00:00",
   112	        signature_hex="00",
   113	    )
   114	    try:
   115	        box.enqueue(
   116	            permit=permit,
   117	            effect=write,
   118	            operation_key="op-probe",
   119	            provider=_Provider(),
   120	            payload=EffectPayload(data={"attempt": "non-external"}),
   121	        )
   122	    except OutboxError as exc:
   123	        text = str(exc)
   124	        if "ليس خارجيًّا" in text:
   125	            held.append("outbox: رفضَ أثرَ WRITE قبلَ الإدراج")
   126	        else:
   127	            broken.append(f"outbox: OutboxError بغيرِ سببِ النوع: {text}")
   128	    except Exception as exc:
   129	        broken.append(f"outbox: استثناءٌ غيرُ المُدَّعى {type(exc).__name__}: {exc}")
   130	    else:
   131	        broken.append("outbox: قَبِلَ أثرًا غيرَ EXTERNAL")
   132	
   133	    ledger = IdempotencyLedger(path=TMP / "wi084_probe_idempotency.jsonl")
   134	    boundary = SovereignExecutionBoundary(
   135	        gateway=SovereignGateway(),
   136	        idempotency_ledger=ledger,
   137	    )
   138	    mixed = _contract(external, write)
   139	    try:
   140	        boundary._guard_compensation(mixed, ())
   141	    except MixedEffectContractError:
   142	        held.append("boundary: رفضَ عقدًا يخلطُ EXTERNAL بكتابةٍ داخليّة")
   143	    except Exception as exc:
   144	        broken.append(f"boundary: استثناءٌ غيرُ MixedEffectContractError {type(exc).__name__}: {exc}")
   145	    else:
   146	        broken.append("boundary: قَبِلَ عقدًا مختلطًا")
   147	
   148	    advances = {"n": 0}
   149	
   150	    def _advance(task_id: str):
   151	        advances["n"] += 1
   152	        raise AssertionError(f"أُعيدَ تنفيذُ مهمّةٍ منتهية: {task_id}")
   153	
   154	    core = ExecutiveCore(
   155	        authorizer=object(),
   156	        repository=_Repo(),
   157	        dispatcher=object(),
   158	        audit_store=object(),
   159	        event_bus=object(),
   160	        runtime=object(),
   161	    )
   162	    core.advance = _advance
   163	    outcome = core.run("task-probe", max_steps=8)
   164	    if advances["n"] == 0 and outcome["terminal"] is True and outcome["final_state"] == "completed":
   165	        held.append("run: مهمّةٌ منتهيةٌ لم تُعَدْ خطواتُها")
   166	    else:
   167	        broken.append(
   168	            f"run: advances={advances['n']} terminal={outcome.get('terminal')} state={outcome.get('final_state')}"
   169	        )
   170	
   171	    print(f"HELD={len(held)} BROKEN={len(broken)}")
   172	    for item in held:
   173	        print(f"HELD {item}")
   174	    for item in broken:
   175	        print(f"BROKEN {item}")
   176	    if broken:
   177	        print("PROPERTY_BROKEN")
   178	        return 1
   179	    print("PROPERTY_HELD")
   180	    return 0
   181	
   182	
   183	if __name__ == "__main__":
   184	    raise SystemExit(main())
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w641/grok_4_7/wi084/repo && .venv/bin/python /home/user/workspace/council_w641/grok_4_7/wi084/probe/wi084_break_execution_claims.py
EXIT: 0
BYTES: 343
SHA256: 2ec883e3ca84152d6abeb544c0c0d68be9079c3e625fae2b62c98e7a5861f1cf
NO_EOL: 0
--- OUTPUT ---
HELD=4 BROKEN=0
HELD compensation: IrreversibleEffectError قبلَ أيِّ عكس (IrreversibleEffectError)
HELD outbox: رفضَ أثرَ WRITE قبلَ الإدراج
HELD boundary: رفضَ عقدًا يخلطُ EXTERNAL بكتابةٍ داخليّة
HELD run: مهمّةٌ منتهيةٌ لم تُعَدْ خطواتُها
PROPERTY_HELD
=== RAW [16] END ===
VERDICT_PER_CRITERION: (1) لا — الوثيقةُ تسمّي ثمانيةَ مواضعِ قرارٍ بأسطرٍ لم تعُدْ صادقةً على هذهِ العقدةِ، وتغفلُ موضعَ قرارٍ تاسعًا. الكتلة 8: EffectKind.EXTERNAL في enforcement_boundary.py عندَ 385 و412 و579 و582 و667، وفي idempotency.py:983، وفي jurisdiction.py:170 — والوثيقةُ قالت 380 و460 و463 و548 و716 و165. والكتلة 7 تؤكّدُ الموضعَ 385 (تتبعُ التعويضِ: kind is not EXTERNAL) وهو فرعُ سلوكٍ غيرُ مُسمًّى، أُضيفَ بعدَ الإيداعِ (تعليقُ W-603 في الملفِّ نفسِه). ما بقيَ صادقًا لا يُرفَض: process_case ما زالَ عندَ 1041 و1058–1060 و1064 و1071–1074 (الكتلة 10)، وrun عندَ 561 (الكتلة 9)، وcompensation.py:103 وoutbox.py:973 وcontract.py:72 و:89 (الكتلتان 7 و8). (2) نعم — الأقسامُ 3-أ/3-ب/3-ج تصفُ إضافةَ EXECUTION وقراءةَ المجموعةِ وتوسيعَ الصادر، وسلوكُ اليومِ الذي تبني عليهِ ثبتَ بالمسبارِ (الكتلة 16). سطرُ sovereignty_bridge من 498 إلى 501 انحرافُ سطرٍ لا يُغيّرُ وصفَ التغيير. (3) نعم — القسمُ 4 يصفُ ثلاثةَ عقودٍ وفصلَ التشغيلِ عن كتابةِ القضيّة، وشكلُ اليومِ ما زالَ كما قاستْه (الكتلة 10). (4) نعم — القسمُ 6 خطّةُ رجوعٍ مرتّبةٌ (ر1 ثمّ ر2 ثمّ ر3) بشرطِ صفرِ سجلّاتِ EXECUTION غيرِ النهائيّةِ ثمَّ git revert بلا دفعٍ بالقوّة. (5) نعم — R-1 وR-2 وR-3 وO-1 وO-2 مكتوبةٌ لا مُخمَّنة. جوابُ R-1 من الكتلتين 7 و8: ليست ثمانيةً، وما خارجَ core/sovereignty/ من EffectKind.EXTERNAL اختباراتٌ لا قراراتُ إنتاج. جوابُ R-2 من الكتلة 9 ومن قراءةِ advance و_execute_step في الاستنساخ: advance تتوقّفُ عندَ النهائيّة، لكنَّ _execute_step تنادي runtime.dispatch قبلَ تثبيتِ الانتقالِ بلا مفتاحِ خطوة — فالسقوطُ بينَ التنفيذِ والتثبيتِ يُعيدُ الخطوة. الوثيقةُ سألت ولم تدّعِ العكس. جوابُ R-3: فحصُ الخلطِ القائمُ يرفضُ EXTERNAL مع كتابةٍ (الكتلة 16) ولا يعرفُ EXECUTION، فلا يكفي وحدَه لجمعِ C1 وC2 حتى يُنفَّذَ الموضعُ 5 كما خطّطت. (6) لا — رقمُ «8» والأسطرُ 165 و380 و460 و463 و548 و716 لا تطابقُ إعادةَ التشغيلِ على هذهِ العقدةِ (الكتل 7 و8 و9). الأوامرُ موجودةٌ لكنَّ هذهِ الأرقامَ كاذبةٌ اليوم. أرقامُ process_case وrun وoutbox.py:973 وcompensation.py:103 ما زالت صادقة. (7) نعم لهذا المقعد — أعدتُ التشغيلَ قبلَ أيِّ شِفرة. لا أحكمُ على المقعدِ الآخرِ (عزلٌ). إفصاحُ تعارضِ § 7 مع توجيهِ 21 لا يُسقطُ الحكمَ؛ حُكِمَ البند.
PROBES: مسبارُ wi084_break_execution_claims.py · كتلةُ الشِّفرةِ 15 · كتلةُ التشغيلِ 16 · الخاصيّةُ: ادّعاءاتُ سلوكِ اليومِ في § 1 و§ 2 — bind_compensation_plan يرفضُ EXTERNAL ولو بمُعوِّضٍ يزعمُ عكسَه، والصادرُ يرفضُ غيرَ EXTERNAL، وحدُّ التنفيذِ يرفضُ عقدًا يخلطُ EXTERNAL بكتابةٍ، وExecutiveCore.run لا يُعيدُ تنفيذَ مهمّةٍ منتهية · انكسرت؟ لا
BLOCKING_REMARKS: معيارُ (1) ومعيارُ (6). خريطةُ التغييرِ ليست صادقةً على العقدةِ 4b5b2be58dd708f1b3e4f5005ed0ed03c2e072e2: موضعُ قرارٍ تاسعٌ غيرُ مُسمًّى في enforcement_boundary.py:385 يفرّعُ على EffectKind.EXTERNAL (تتبعُ ما يُعوَّض)، والأسطرُ المُسمّاةُ 380 و460 و463 و548 و716 لم تعُدْ تشيرُ إلى السلوكِ الموصوفِ (صارت 412 و579 و582 و667 و983 — الكتلة 8). تنفيذُ الشِّفرةِ من هذهِ الوثيقةِ كما هي على هذهِ العقدةِ يعدّلُ أسطرًا خاطئةً ويتركُ فرعًا.
ISOLATION_DECLARATION: نعم — لم أقرأْ للحكمِ شيئًا خارجَ استنساخِي /home/user/workspace/council_w641/grok_4_7/wi084/repo وهذهِ الإحاطةِ. استثناءٌ: أثناءَ انتظارِ الأمرِ 8 ظهرَ في قائمةِ عمليّاتِ النظامِ سطرُ أمرِ مقعدِ kimi_k3 على الأمرِ نفسِه؛ لم أفتحْ ملفّاتِه ولا حكمَه ولم أستعملْ مخرجَه.
VERDICT: FAIL
