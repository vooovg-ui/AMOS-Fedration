MODEL: grok_4_7
FAMILY: grok
RUN_DATE: 2026-10-24 17:56 +00:00
NODE: aba3cb45254ffbef101000ab9d13798b4a46717f
CLONE_PATH: /home/user/workspace/council_w652/grok_4_7/wi084/repo
CLONE_COMMAND: git clone https://github.com/vooovg-ui/AMOS-Fedration.git /home/user/workspace/council_w652/grok_4_7/wi084/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-652/briefs_wi084/
 2. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-652/briefs_wi084/)
 3. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git log --format='%h %cI %s' -- docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
 5. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && cat docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
 6. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git diff --stat 5caeac5bdf9ea446163c40c0a11147fa1e1a9cec HEAD -- docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md core/sovereignty/ federal/executive/services/src/amos_federation/services/government_services/ federal/executive/services/src/amos_federation/services/executive_core/
 7. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "EXTERNAL" core/sovereignty/*.py
 8. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "EffectKind.EXTERNAL" --type py .
 9. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && nl -ba core/sovereignty/enforcement_boundary.py | sed -n '375,425p;570,590p;660,672p'
 10. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n -c "EXTERNAL" tests/sovereignty/
 11. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && nl -ba federal/executive/services/src/amos_federation/services/executive_core/engine.py | sed -n '205,260p;331,350p;424,440p;476,486p;540,570p'
 12. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "def process_case" -A 60 federal/executive/services/src/amos_federation/services/government_services/service.py
 13. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "EffectKind\(|EXTERNAL" federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py
 14. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "DEFAULT_MAX_DELIVERY_ATTEMPTS: Final|^def enqueue_write_ahead|^class OutboxWorker|claims_exactly_once|\"guarantee\"" core/sovereignty/outbox.py
 15. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 16. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "Q-16|D23" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 17. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && sha256sum docs/audit/evidence/W-652/briefs_wi084/briefing_grok_4_7.md
 18. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && cat docs/audit/evidence/W-652/briefs_wi084/SHA256SUMS
 19. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && nl -ba /home/user/workspace/council_w652/grok_4_7/wi084/probe/break_claimed_properties.py
 20. cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && PYTHONPATH=. .venv/bin/python /home/user/workspace/council_w652/grok_4_7/wi084/probe/break_claimed_properties.py
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-652/briefs_wi084/
EXIT: 0
BYTES: 41
SHA256: 6ddb44ad1c484a9a4174b53165abe4bf805eba4edf5a56f0587d35e3690b11c0
NO_EOL: 0
--- OUTPUT ---
aba3cb45254ffbef101000ab9d13798b4a46717f
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-652/briefs_wi084/)
EXIT: 0
BYTES: 875
SHA256: 1a72abd2ee99d5024be73c8bb4384a56fec1cb258b88dad4efdde1383ff63851
NO_EOL: 0
--- OUTPUT ---
Note: switching to 'aba3cb45254ffbef101000ab9d13798b4a46717f'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at aba3cb45 W-652: إحاطاتُ جولةِ WI-084 المُعادةِ (D23 (2)) — gemini_3_8_flash · grok_4_7 · kimi_k3 مبصومةٌ قبلَ الإطلاقِ (SHA256SUMS) ونصوصُ الإطلاقِ حرفيًّا · لا شِفرةَ · المنسِّقُ Claude Opus 5.5
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 6ddb44ad1c484a9a4174b53165abe4bf805eba4edf5a56f0587d35e3690b11c0
NO_EOL: 0
--- OUTPUT ---
aba3cb45254ffbef101000ab9d13798b4a46717f
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git log --format='%h %cI %s' -- docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
EXIT: 0
BYTES: 706
SHA256: 4d5f4a3cd73249e809c014e8bcbae0811c849d04f9798a4eff535c141c5e8444
NO_EOL: 0
--- OUTPUT ---
5592f88f 2026-10-24T13:48:34Z W-650: WI-084 — تصحيحُ خريطةِ أسطرِ وثيقةِ تصميمِ EXECUTION بقياسٍ مُعادٍ على 1489efde (قرارُ المالكِ D23 (2)): 9 مواضعِ قرارٍ في 5 ملفّاتٍ · التاسعُ enforcement_boundary.py:385 مُسمًّى · R-2 بالقراءةِ سؤالٌ مفتوحٌ · تصحيحٌ بالإضافةِ — لا شِفرةَ · المنسِّقُ Claude Opus 5.5
5caeac5b 2026-10-16T08:56:27Z W-398: WI-084 — وثيقةُ تصميمِ نوعِ الأثرِ EXECUTION (Q-16 ③): 8 مواضعِ قرارٍ في 6 ملفّات · ثلاثةُ عقودٍ لـprocess_case · خطّةُ رجوع · بلا شِفرة
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && cat docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
EXIT: 0
BYTES: 23361
SHA256: 23aa03882d9af9b6a11498375a4fa289a894569cd5adb9047e6f7b6377ee2dd4
NO_EOL: 0
--- OUTPUT ---
# Q16_EXECUTION_EFFECT_DESIGN.md — وثيقةُ تصميمِ نوعِ الأثرِ `EXECUTION` (قرارُ المالكِ Q-16 ③)

<!--
الهدف: وصفٌ دقيقٌ لتعديلِ الأوّليّاتِ السياديّةِ الذي يقتضيه قرارُ المالكِ في Q-16 ③ — قبلَ أيِّ شِفرة
النطاق: تصميمٌ فقط · لا شِفرةَ ولا اختبارَ ولا تعديلَ في core/sovereignty/ ولا في process_case · كلُّ رقمٍ بأمرٍ يُعادُ تشغيلُه
المالك: docs/audit/ — ديوانُ التدقيق · البندُ WI-084 (Perplexity Computer)
تاريخ الإنشاء: 2026-10-16
تاريخ آخر تعديل: 2026-10-24 (W-650 — تصحيحُ خريطةِ الأسطرِ بقياسٍ مُعادٍ على `1489efde` وتسميةُ الموضعِ التاسعِ · بقرارِ المالكِ D23 (2) · تصحيحٌ بالإضافةِ لا محوٌ)
-->

**البند:** `WI-084` · **القيد:** `W-398` · **نقطةُ القياس:** فرعُ `w-381-merge-exception-d9` فوقَ main `81b0071`
**الحالة:** تصميمٌ للمراجعة — **لا يُكتَبُ سطرُ شِفرةٍ قبلَ مراجعةِ مقعدينِ يُعيدانِ التشغيلَ (Q-H)** ثمَّ بندِ شِفرةٍ مستقلٍّ يُسجَّلُ بعدَها.

> **[إضافةٌ مؤرَّخةٌ · 2026-10-24 · W-650] نقطةُ قياسٍ جديدةٌ: main `1489efde`** (والشِّفرةُ المقيسةُ لم تتغيّرْ منذُ آخرِ التزامٍ مسَّ `core/sovereignty/`: `4247c68f` · W-640). جولةُ W-647 حكمَ فيها مقعدُ `grok_4_7` بـFAIL للمعيارَينِ (1) و(6): خريطةُ أسطرِ § 2 متقادمةٌ على العقدةِ المراجَعةِ وموضعُ قرارٍ تاسعٌ غيرُ مسمًّى (الحكمُ حرفيًّا في [`evidence/W-647/verdicts/wi084/grok_4_7/VERDICT.md`](evidence/W-647/verdicts/wi084/grok_4_7/VERDICT.md)). وقرارُ المالكِ D23 (2): «صحّح خريطة أسطر WI-084 وأعد جولة المجلس». فأُعيدَ قياسُ **كلِّ** رقمِ سطرٍ في هذه الوثيقةِ بأمرِه — والخامُ في [`evidence/W-650/measurements.txt`](evidence/W-650/measurements.txt). **الخريطةُ النافذةُ هي § 2-ب**؛ وجدولُ § 2 الأصليُّ باقٍ كما كُتِبَ في W-398 شاهدًا لا مرجعًا للتنفيذ. ولا تغييرَ في أيِّ قرارِ تصميمٍ: التصحيحُ أرقامٌ وموضعٌ واحدٌ مُسمًّى.

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

> **[إضافةٌ مؤرَّخةٌ · 2026-10-24 · W-650]** أُعيدَ قياسُ أسطرِ هذا القسمِ على `1489efde`: `service.py:1041` · 1058–1060 · 1064 · 1071–1074 · و`engine.py:561` — **كلُّها كما هي** (الخامُ في `evidence/W-650/measurements.txt`).

## 2 · مواضعُ القرارِ بـ`EXTERNAL` اليومَ (ما سيتغيّر)

**الأمر:** `rg -n "EXTERNAL" core/sovereignty/*.py | rg -v "ROOT_EXTERNAL_HUMAN|MANDATORY_EXTERNAL_STAGES|EXTERNAL_OUTBOX"`

**8 مواضعِ قرارِ سلوكٍ في 6 ملفّات** [W-650: **متقادمٌ — النافذُ 9 مواضعَ في 5 ملفّاتٍ (§ 2-ب)**؛ وكانَ العدُّ على `81b0071` نفسِها 8 في **5** ملفّاتٍ لا 6 — مقيسًا بالأمرِ نفسِه] — غيرَ التعريفِ (`contract.py:72` و`:89`) والبنّاءِ (`outbox.py:1360`) والشروح:

(الجدولُ التالي خريطةُ W-398 على `81b0071` كما كُتِبَت — **لا يُنفَّذُ بها**؛ النافذةُ § 2-ب.)

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

### 2-ب · الخريطةُ النافذةُ — مُعادةُ القياسِ (إضافةٌ مؤرَّخةٌ · 2026-10-24 · W-650 · العقدةُ `1489efde`)

**الأمرُ نفسُه** (`rg -n "EXTERNAL" core/sovereignty/*.py | rg -v "ROOT_EXTERNAL_HUMAN|MANDATORY_EXTERNAL_STAGES|EXTERNAL_OUTBOX"`) ⇒ **9 مواضعِ قرارِ سلوكٍ في 5 ملفّاتٍ** (compensation 1 · jurisdiction 1 · enforcement_boundary 5 · idempotency 1 · outbox 1):

| # | الموضع (`1489efde`) | وكانَ (`81b0071`) | السلوكُ اليوم | بعدَ التصميم |
|---|---|---|---|---|
| 1 | `compensation.py:103` | :103 | `IRREVERSIBLE_EFFECT_KINDS = {EXTERNAL}` ⇒ `bind_compensation_plan` يقرأُ المجموعةَ (:331) ويرفعُ `IrreversibleEffectError` (:334) | `{EXTERNAL, EXECUTION}` |
| 2 | `jurisdiction.py:170` (المجموعةُ تبدأُ :166) | :165 | `NON_JUDICIAL_EFFECT_KINDS` تمنعُ القضاءَ من DELETE/TRANSFER/EXTERNAL | يُضافُ `EXECUTION` |
| 3 | `enforcement_boundary.py:412` (تُستعمَلُ في `detect_external` :421–423) | :380 | بادئةُ `"EXTERNAL:"` لتمييزِ النتيجةِ في سجلِّ الأحاديّة | كلُّ بادئةٍ من `IRREVERSIBLE_EFFECT_KINDS` |
| 4 | `enforcement_boundary.py:579` | :460 | جمعُ الآثارِ الخارجيّةِ لفحصِ الخلط | `e.kind in IRREVERSIBLE_EFFECT_KINDS` |
| 5 | `enforcement_boundary.py:582` (والرفضُ :584–586) | :463 | جمعُ الآثارِ المغيِّرةِ الداخليّة ⇒ `MixedEffectContractError` إن اجتمعا | `e.kind not in IRREVERSIBLE_EFFECT_KINDS` |
| 6 | `enforcement_boundary.py:667` | :548 | `route`: غيرُ الخارجيِّ إلى المُطبِّق، والخارجيُّ إلى الصادر | غيرُ اللّامعكوسِ إلى المُطبِّق، واللّامعكوسُ إلى الصادر |
| 7 | `idempotency.py:983` | :716 | المسارُ الذرّيُّ المباشرُ يرفضُ بادئةَ `"EXTERNAL:"` | يرفضُ كلَّ بادئةٍ لامعكوسة |
| 8 | `outbox.py:973` | :973 | الصادرُ لا يقبلُ إلّا `EXTERNAL` (`OutboxError`) | يقبلُ `IRREVERSIBLE_EFFECT_KINDS` |
| **9** | **`enforcement_boundary.py:385`** (داخلَ `_tracked` :381–388) | **لم يكنْ** — أدخلَه `968e5ba4` (W-603: وصلُ التعويضِ الآليِّ في الحدِّ · Q-70) | يُلحِقُ بـ`applied_internal` (قائمةِ ما يُعوَّضُ آليًّا) كلَّ أثرٍ **غيرِ `EXTERNAL`** تغطّيه خطّةُ التعويض | `effect.kind not in IRREVERSIBLE_EFFECT_KINDS` — فلا يُعَدُّ أثرُ `EXECUTION` «داخليًّا مُطبَّقًا» يُعوَّضُ |

**عن الموضعِ التاسع (قراءةُ شِفرةٍ لا تشغيلٌ):** الفرعُ يقعُ بعدَ `plan is not None`، وخطّةُ التعويضِ لا تُربَطُ أصلًا لعقدٍ فيه أثرٌ لامعكوسٌ (الموضعُ 1 · :331–334) — فاليومَ لا يبلغُه أثرٌ `EXTERNAL` بخطّةٍ. لكنَّه **موضعُ قرارٍ بالاسم** فتسري عليه قاعدةُ التصميمِ: يقرأُ المجموعةَ لا النوعَ — وإلّا بقيَ فرعٌ يُسمّي `EXTERNAL` وحدَه، وهو عينُ ما حذَّرَ منه حكمُ grok (W-647).

**غيرُ مواضعِ القرار (مقيسةً · مستبعَدةً بسببٍ مُسمًّى):** التعريفُ `contract.py:72` و`:89` · البنّاءُ `outbox.py:1360` · الشروحُ `compensation.py:49/173/321` · `jurisdiction.py:322` · `idempotency.py:34/977` · `idempotency.py:85/117` (`OperationStatus.EXTERNAL_PENDING` — اسمُ حالةِ عمليّةٍ لا قرارٌ على نوعِ أثرٍ) · `crown.py:451` (نصُّ `"GENESIS_EXTERNAL_HUMAN_ROOT"` — نوعُ مراسمٍ لا نوعُ أثرٍ).

**خارجَ `core/sovereignty/`:** `rg -n "EffectKind\.EXTERNAL" --type py` مستثنيًا الاختباراتِ و`core/sovereignty/` ⇒ **لا نتيجةَ** (رمزُ 1) — فلا قرارَ إنتاجيًّا بالاسمِ خارجَه.

**أرقامٌ أخرى في الوثيقةِ أُعيدَ قياسُها:** `sovereignty_bridge.py:498` ← **:501** (§ 3-أ) · و`outbox.py:1055` · `:1351` · `:86` · `:1211` · `:1360` و`contract.py:72/89` و`compensation.py:331` **كما هي** · وعدُّ `rg -c EXTERNAL tests/sovereignty/*.py` (§ 5) **كما هو**: compensation 4 · crown_human_root 4 · enforcement_boundary 10 · enforcement_integration 5 · idempotency 1 · outbox 3.

## 3 · تغييرُ العقود

### 3-أ · أنواعُ الأثر (1E · `contract.py`)

- يُضافُ `EXECUTION = "EXECUTION"` إلى `EffectKind`، و`is_mutating` صحيحٌ له تلقائيًّا (كلُّ ما ليس `READ`).
- الوسمُ العربيّ: «تشغيلُ مهمّة».
- `sovereignty_bridge.py:498` [W-650: **:501** على `1489efde`] يبني النوعَ بـ`contract.EffectKind(kind)` من نصّ — فيقبلُ `"EXECUTION"` بلا تعديل.

### 3-ب · التعويض (1I · `compensation.py`)

- لا معوّضَ يُقبَلُ لـ`EXECUTION` (`UncompensatableEffectError`) ولا خطّةَ تعويضٍ لعقدٍ فيه تشغيل (`IrreversibleEffectError`) — **بالمجموعةِ نفسِها، لا بقاعدةٍ جديدة**.
- **ما لا يتغيّر:** خطّةُ التعويضِ لعقدٍ لا تشغيلَ فيه تبقى كما هي حرفيًّا.

### 3-ج · الصادر (1K · `outbox.py` · `enforcement_boundary.py`)

- `enqueue_write_ahead` (`outbox.py:1055`) يبقى كما هو: الإدراجُ **قبلَ** تثبيتِ نجاحِ العمليّة، ورفضُه بعدَه (`OutboxOrderingError`).
- **مسألةٌ مقيسةٌ لا تُخفى:** الصادرُ يُعلِنُ `AT_LEAST_ONCE_WITH_STABLE_IDEMPOTENCY_IDENTITY` و`claims_exactly_once: False` (`outbox.py:1351`) ويُعيدُ حتى `DEFAULT_MAX_DELIVERY_ATTEMPTS = 3` (`:86`). فالتشغيلُ قد يُسلَّمُ أكثرَ من مرّة.
- **الحلُّ المقترح:** المُزوّدُ (`ProviderAdapter`) لـ`EXECUTION` يُنادي `ExecutiveCore.run(task_id)` **ومفتاحُ أحاديّتِه `task_id`**. وبما قيسَ في § 1 (`run` يتوقّفُ عندَ الحالةِ النهائيّة ويُكمِلُ من حيثُ وقف) فالتسليمُ المكرَّرُ لا يُعيدُ خطوةً تمَّت — **بشرطِ** أن تكونَ `advance` نفسُها أحاديّةً لكلِّ خطوة. وهذا الشرطُ **غيرُ مقيسٍ بعدُ** (سؤالُ المراجعةِ R-2).
  - **[إضافةٌ مؤرَّخةٌ · 2026-10-24 · W-650] قراءةُ شِفرةٍ على `1489efde` (لا تشغيلٌ ولا مسبارٌ):** `advance` (`engine.py:331`) تُوجِّهُ المهمّةَ التي حالتُها `EXECUTING` إلى `_execute_step` (:347) · و`_execute_step` يُنادي `self._runtime.dispatch(…)` (:478) **قبلَ** الانتقالِ المحروسِ `EXECUTING → COMPLETED` (:542) · ومفتاحُ الذرّيّةِ للانتقالِ لا للخطوة (`_guarded_transition` · :250–252). فإن سقطَ العاملُ بينَ :478 و:542 بقيتِ المهمّةُ `EXECUTING` وتسليمٌ ثانٍ يُنادي `dispatch` مرّةً أخرى. **الشرطُ أعلاه غيرُ متحقِّقٍ اليومَ بالقراءة** — وهذا ما قرأه مقعدُ grok في W-647 أيضًا (وقالَ: «الوثيقةُ سألت ولم تدّعِ العكس»). لا يُغيِّرُ هذا القيدُ الحلَّ المقترحَ: يبقى R-2 سؤالًا مفتوحًا بخيارَيه المذكورَينِ في § 7 (`max_attempts = 1` لـ`EXECUTION` أو مفتاحٌ لكلِّ خطوة)، وحسمُه قبلَ بندِ الشِّفرة.
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
| اختباراتٌ جديدة | لكلِّ موضعٍ من الثمانيةِ [W-650: **التسعةِ** · § 2-ب] فحصٌ لـ`EXECUTION` · وطفرةٌ لكلٍّ (إرجاعُ `is EXTERNAL` بدلَ المجموعةِ يُسقِطُ فحصًا) | سجلُّ الطفرات |
| `process_case` | دَينٌ يخرجُ من D-4 (`public · commit · unguarded`) | `sovereign_write_inventory.py` قبلُ/بعدُ |
| بياناتٌ قائمة | لا سجلّاتِ صادرٍ من نوعِ `EXECUTION` اليومَ — النوعُ غيرُ موجود | عدُّ السجلّاتِ قبلَ الدمج |
| أوّليّاتُ Q-16 الأخرى | `build_compensation_plan` لا يتغيّرُ توقيعُه ولا قواعدُه الثلاث | فحصُ التوقيع |

## 6 · خطّةُ الرجوع

1. **الشِّفرةُ في قيودٍ مستقلّةٍ مرتّبة:** (ر1) النوعُ والمجموعةُ والمواضعُ الثمانية [W-650: **التسعة** · § 2-ب] · (ر2) مُزوّدُ التشغيل · (ر3) هجرةُ `process_case`. فالرجوعُ عن (ر3) وحدَه يُعيدُ `process_case` إلى سلوكِها اليومَ ويُبقي البنيةَ خامدةً بلا مُستعمِل.
2. **قبلَ أيِّ رجوعٍ عن (ر1) أو (ر2):** يُعَدُّ في الصادرِ كلُّ سجلٍّ نوعُه `EXECUTION` وحالتُه ليست نهائيّة. يجبُ أن يكونَ **صفرًا** — وإلّا يُصرَفُ (يُسلَّمُ أو يُحسَمُ بشريًّا) أوّلًا. لأنَّ الرجوعَ يحذفُ النوعَ فلا يُقرأُ السجلُّ.
3. **الرجوعُ بـ`git revert`** على فرعٍ ودمجٍ تقدُّميٍّ كأيِّ عمل — لا دفعَ بالقوّة.
4. **ما لا رجوعَ فيه بطبيعتِه:** مهمّةٌ شُغِّلَت لا تُعادُ إلى ما قبلَها — وهذا هو سببُ القرارِ ③ نفسِه، لا عيبٌ في الخطّة.

## 7 · أسئلةٌ مفتوحة

### للمراجعين (يُعادُ تشغيلُها)

- **R-1:** أعيدوا أمرَ § 2 وتأكّدوا أنَّ المواضعَ ثمانيةٌ لا غير [W-650: **تسعةٌ** في 5 ملفّاتٍ على `1489efde` — § 2-ب]، ولا موضعَ آخرَ يقرأُ `EXTERNAL` بالاسمِ خارجَ `core/sovereignty/` يتخذُ قرارًا (`rg -n "EffectKind.EXTERNAL" --type py`).
- **R-2:** هل `ExecutiveCore.advance` أحاديّةٌ لكلِّ خطوةٍ إن سقطَ العاملُ بينَ تنفيذِ الخطوةِ وتثبيتِ الحالة؟ إن لم تكن، فالتسليمُ المكرَّرُ قد يُعيدُ خطوة — ويلزمُ `max_attempts = 1` لـ`EXECUTION` أو مفتاحٌ لكلِّ خطوة.
- **R-3:** هل يكفي فحصُ الخلطِ القائمُ ليمنعَ عقدًا واحدًا يجمعُ C1 وC2؟

### للمالك

- **O-1:** قضيّةٌ بقيَ تشغيلُها `DEAD` أو `INDETERMINATE`: تبقى `processing` حتى قرارٍ بشريّ (توصيتي) — أم تُعلَّمُ بحالةٍ جديدةٍ مثلَ «تنتظرُ حسمًا»؟ الثانيةُ تُغيِّرُ مفرداتِ حالةِ القضيّة.
- **O-2:** تسليمٌ متزامنٌ (س) أم لا (ع)؟ — التوصية: (س).

## 8 · ما لم يُفعَلْ — صراحةً

- لم يُكتَبْ سطرُ شِفرةٍ ولا اختبار، ولم يُمَسَّ `core/sovereignty/` ولا `service.py`.
- لم يُسجَّلْ بندُ الشِّفرةِ بعدُ: يُسجَّلُ بعدَ المراجعةِ وجوابِ O-1 وO-2.
- لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذ.
- **[إضافةٌ مؤرَّخةٌ · 2026-10-24 · W-650]** تصحيحُ W-650 أرقامٌ وموضعٌ مُسمًّى وقراءةُ R-2 فقط: لا شِفرةَ ولا اختبارَ ولا تغييرَ في قرارِ تصميمٍ · ولا يُغني عن جولةِ المجلسِ الجديدةِ (D23 (2)).
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && git diff --stat 5caeac5bdf9ea446163c40c0a11147fa1e1a9cec HEAD -- docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md core/sovereignty/ federal/executive/services/src/amos_federation/services/government_services/ federal/executive/services/src/amos_federation/services/executive_core/
EXIT: 0
BYTES: 450
SHA256: 6fd2d879770fbbdb9483c666305a3d371fbaf5e99526580390065e5a12707820
NO_EOL: 0
--- OUTPUT ---
 core/sovereignty/enforcement_boundary.py           | 161 +++++++--
 core/sovereignty/idempotency.py                    | 377 ++++++++++++++++++---
 core/sovereignty/jurisdiction.py                   |   5 +
 docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md          |  43 ++-
 .../services/executive_core/agent_identity.py      | 143 +++++++-
 .../services/executive_core/sovereignty_bridge.py  |   3 +
 6 files changed, 636 insertions(+), 96 deletions(-)
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "EXTERNAL" core/sovereignty/*.py
EXIT: 0
BYTES: 3954
SHA256: ab7ae6cebbc65682522c814645f9d108a5906ff4eaae9a97ce8680bdc141b726
NO_EOL: 0
--- OUTPUT ---
core/sovereignty/__init__.py:122:    "ROOT_EXTERNAL_HUMAN": "crown",
core/sovereignty/__init__.py:165:    "MANDATORY_EXTERNAL_STAGES": "enforcement_boundary",
core/sovereignty/compensation.py:49:`EffectKind.EXTERNAL` **لا يُقبَلُ معوّضًا**. نداءٌ خارجيٌّ وقع لا يُسحَب،
core/sovereignty/compensation.py:103:    {EffectKind.EXTERNAL}
core/sovereignty/compensation.py:173:    """محاولةُ تسجيلِ معوّضٍ لأثرٍ لا يُعكَس (`EXTERNAL`).
core/sovereignty/compensation.py:321:    1. **أثرٌ لا يُعكَس** (`EXTERNAL`) مُعلَنٌ في العقد -> `IrreversibleEffectError`.
core/sovereignty/crown.py:37:ROOT_EXTERNAL_HUMAN = "EXTERNAL_HUMAN_ROOT"   # وُلِّد خارج الدولة — الملكُ وحده رآه
core/sovereignty/crown.py:86:        return self.root_origin == ROOT_EXTERNAL_HUMAN
core/sovereignty/crown.py:438:        "root_origin": ROOT_EXTERNAL_HUMAN,
core/sovereignty/crown.py:448:                "root_origin": ROOT_EXTERNAL_HUMAN,
core/sovereignty/crown.py:451:                    "ceremony_kind": "GENESIS_EXTERNAL_HUMAN_ROOT",
core/sovereignty/jurisdiction.py:170:        EffectKind.EXTERNAL,   # التأثيرُ الخارجيُّ شأنٌ تنفيذيّ
core/sovereignty/jurisdiction.py:322:        وأمّا `DELETE` و`TRANSFER` و`EXTERNAL` فخارجةٌ عن السلطةِ القضائيّة:
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
core/sovereignty/outbox.py:973:    if effect.kind is not EffectKind.EXTERNAL:
core/sovereignty/outbox.py:1360:        kind=EffectKind.EXTERNAL,
core/sovereignty/contract.py:72:    EXTERNAL = "EXTERNAL"
core/sovereignty/contract.py:89:    EffectKind.EXTERNAL: "نداءٌ خارجيّ",
core/sovereignty/cli.py:27:    ROOT_EXTERNAL_HUMAN,
core/sovereignty/cli.py:134:        if crown.root_origin != ROOT_EXTERNAL_HUMAN:
core/sovereignty/cli.py:137:                f"«{ROOT_EXTERNAL_HUMAN}»: الدولةُ ولّدت مفتاحَ الملك فرأتْه. "
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "EffectKind.EXTERNAL" --type py .
EXIT: 0
BYTES: 2764
SHA256: 63a9b46d65e0660036072b7bdec3432cf00368ecddc75a5ba6444ab9b810041b
NO_EOL: 0
--- OUTPUT ---
./tests/sovereignty/test_enforcement_integration.py:369:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
./tests/sovereignty/test_enforcement_integration.py:393:                declared_effects=(_أثر(EffectKind.EXTERNAL, NOTICE),),
./tests/sovereignty/test_compensation.py:230:                SovereignEffect(kind=EffectKind.EXTERNAL, resource=f"{TARGET}/swift"),
./tests/sovereignty/test_compensation.py:246:        assert EffectKind.EXTERNAL in IRREVERSIBLE_EFFECT_KINDS
./tests/sovereignty/test_enforcement_boundary.py:273:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
./tests/sovereignty/test_enforcement_boundary.py:575:        خارجيّ = _أثر(EffectKind.EXTERNAL, TARGET)
./tests/sovereignty/test_enforcement_boundary.py:591:        خارجيّ = _أثر(EffectKind.EXTERNAL, TARGET)
./tests/sovereignty/test_enforcement_boundary.py:617:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
./tests/sovereignty/test_enforcement_boundary.py:637:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
./tests/sovereignty/test_enforcement_boundary.py:653:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
./tests/sovereignty/test_enforcement_boundary.py:669:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
./tests/sovereignty/test_enforcement_boundary.py:957:        أثر = _أثر(EffectKind.EXTERNAL, NOTICE)
./core/sovereignty/enforcement_boundary.py:385:                and effect.kind is not EffectKind.EXTERNAL
./core/sovereignty/enforcement_boundary.py:412:        external_prefix = EffectKind.EXTERNAL.value + ":"
./core/sovereignty/enforcement_boundary.py:579:            e for e in contract.declared_effects if e.kind is EffectKind.EXTERNAL
./core/sovereignty/enforcement_boundary.py:582:            e for e in contract.mutating_effects if e.kind is not EffectKind.EXTERNAL
./core/sovereignty/enforcement_boundary.py:667:            if effect.kind is not EffectKind.EXTERNAL:
./core/sovereignty/compensation.py:49:`EffectKind.EXTERNAL` **لا يُقبَلُ معوّضًا**. نداءٌ خارجيٌّ وقع لا يُسحَب،
./core/sovereignty/compensation.py:103:    {EffectKind.EXTERNAL}
./core/sovereignty/contract.py:89:    EffectKind.EXTERNAL: "نداءٌ خارجيّ",
./core/sovereignty/jurisdiction.py:170:        EffectKind.EXTERNAL,   # التأثيرُ الخارجيُّ شأنٌ تنفيذيّ
./core/sovereignty/outbox.py:973:    if effect.kind is not EffectKind.EXTERNAL:
./core/sovereignty/outbox.py:1360:        kind=EffectKind.EXTERNAL,
./core/sovereignty/idempotency.py:34:- **الأثرُ الخارجيُّ لا يُلغى.** `EffectKind.EXTERNAL` لا يمكنُ التراجعُ عنه
./core/sovereignty/idempotency.py:983:            if sig.startswith(EffectKind.EXTERNAL.value + ":"):
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && nl -ba core/sovereignty/enforcement_boundary.py | sed -n '375,425p;570,590p;660,672p'
EXIT: 0
BYTES: 4880
SHA256: 7eb039a45dc218fa03a073a12a9bc1971e4f85128ec48985d189d9c1ab0f3bc8
NO_EOL: 0
--- OUTPUT ---
   375	            provider=provider,
   376	            payload_of=payload_of,
   377	            correlation_id=correlation_id,
   378	            enqueued=enqueued,
   379	        )
   380	
   381	        def _tracked(effect: SovereignEffect) -> None:
   382	            routed(effect)
   383	            if (
   384	                plan is not None
   385	                and effect.kind is not EffectKind.EXTERNAL
   386	                and plan.covers(effect.signature)
   387	            ):
   388	                applied_internal.append(effect.signature)
   389	
   390	        def _under_permit() -> tuple[str, ...]:
   391	            """ما يُرجَعُ للحارسِ بصماتٌ نصّيّةٌ لا كائنات.
   392	
   393	            سجلُّ 1H يُثبِّتُ بصمةَ النتيجةِ بـ`json`، والكائنُ غيرُ القابلِ
   394	            للتمثيلِ يُفشِلُ التثبيت. والبصماتُ هي ما يُقارَنُ عندَ الإعادةِ
   395	            أصلًا، فلا يُفقَدُ شيءٌ بإرجاعِها.
   396	            """
   397	            produced = self.policy_enforcement_point.enforce(
   398	                permit,
   399	                planner=planner,
   400	                applier=_tracked,
   401	            )
   402	            applied_holder.append(produced)
   403	            return tuple(e.signature for e in produced)
   404	
   405	        fingerprint = compute_fingerprint(
   406	            scope=operation_key.scope,
   407	            action=request.action,
   408	            target=request.target,
   409	            effect_signatures=tuple(sorted(contract.declared_signatures)),
   410	            actor=request.actor,
   411	        )
   412	        external_prefix = EffectKind.EXTERNAL.value + ":"
   413	        try:
   414	            result: OperationResult[tuple[str, ...]] = IdempotencyGuard(
   415	                ledger=self.idempotency_ledger
   416	            ).run_once(
   417	                key=operation_key,
   418	                fingerprint=fingerprint,
   419	                execute=_under_permit,
   420	                extract_effect_signatures=lambda sigs: tuple(sigs or ()),
   421	                detect_external=lambda sigs: any(
   422	                    s.startswith(external_prefix) for s in (sigs or ())
   423	                ),
   424	            )
   425	        except Exception as exc:
   570	        self, contract: ExecutionContract, compensators: tuple[Compensator, ...]
   571	    ) -> tuple[CompensationPlan | None, tuple[SovereignEffect, ...]]:
   572	        """1I: ما لا تعرفُ الدولةُ كيفَ تخرجُ منه لا تدخلُه — ربطًا لا استعادة.
   573	
   574	        الخلطُ مرفوض: خطّةُ 1I ترفضُ العقدَ الذي فيه أثرٌ خارجيّ، وترتيبُ 1K لا
   575	        يُغطّي أثرًا داخليًّا. فعقدٌ يجمعُهما لا ضمانَ له، والرفضُ قبلَ التنفيذِ
   576	        أصدقُ من ادّعاءٍ بعدَه.
   577	        """
   578	        external = tuple(
   579	            e for e in contract.declared_effects if e.kind is EffectKind.EXTERNAL
   580	        )
   581	        reversible_mutating = tuple(
   582	            e for e in contract.mutating_effects if e.kind is not EffectKind.EXTERNAL
   583	        )
   584	        if external and reversible_mutating:
   585	            self._record_rejection(BoundaryStage.COMPENSATION_PLAN)
   586	            raise MixedEffectContractError(
   587	                "العقدُ يخلطُ أثرًا خارجيًّا ("
   588	                + " · ".join(e.signature for e in external)
   589	                + ") بأثرٍ مُغيِّرٍ داخليّ ("
   590	                + " · ".join(e.signature for e in reversible_mutating)
   660	
   661	        مُطبِّقُ المُنادي **لا يُنادى قطُّ** على أثرٍ خارجيّ: لا فحصًا بعدَه ولا
   662	        تحذيرًا، بل لا يُمرَّرُ إليه. والأثرُ الخارجيُّ يُدرَجُ في الصادرِ قبلَ
   663	        تثبيتِ نجاحِ العمليّة (`enqueue_write_ahead`)، فالترتيبُ مفروضٌ من 1K.
   664	        """
   665	
   666	        def route(effect: SovereignEffect) -> None:
   667	            if effect.kind is not EffectKind.EXTERNAL:
   668	                applier(effect)
   669	                return
   670	            if self.outbox is None or provider is None or payload_of is None:
   671	                # لا يُبلَغُ هذا الموضعُ عبرَ `execute` — الفحصُ سابقٌ للإذن.
   672	                # ويبقى مغلقًا لأنّ التوزيعَ قد يُستدعى من مسارٍ آخرَ لاحقًا.
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n -c "EXTERNAL" tests/sovereignty/
EXIT: 0
BYTES: 263
SHA256: f857f149db82de3924609479c9c4d5beb226fe515935cf3c966e93eb1a4b6e38
NO_EOL: 0
--- OUTPUT ---
tests/sovereignty/test_outbox.py:3
tests/sovereignty/test_enforcement_integration.py:5
tests/sovereignty/test_idempotency.py:1
tests/sovereignty/test_crown_human_root.py:4
tests/sovereignty/test_compensation.py:4
tests/sovereignty/test_enforcement_boundary.py:10
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && nl -ba federal/executive/services/src/amos_federation/services/executive_core/engine.py | sed -n '205,260p;331,350p;424,440p;476,486p;540,570p'
EXIT: 0
BYTES: 7561
SHA256: 6aafff571e57310512ebacb6ca2551d0f57d3edddf396d84e6143ec864321ddc
NO_EOL: 0
--- OUTPUT ---
   205	            audit_hash=entry["hash"],
   206	            event_id=event["event_id"],
   207	            detail=detail,
   208	        )
   209	
   210	    def _guarded_transition(
   211	        self,
   212	        task_id: str,
   213	        expected: TaskState,
   214	        target: TaskState,
   215	        action: str,
   216	        *,
   217	        fields: dict[str, Any] | None = None,
   218	        detail: dict[str, Any] | None = None,
   219	    ) -> TransitionOutcome:
   220	        """انتقال محكوم: حدُّ التنفيذ السياديّ → كتابة ذرّية → تدقيق → حدث.
   221	
   222	        الكتابة تحدث **داخل** مُطبِّقِ الحدّ، فلا تقع خارج الإذن. وإن سبقنا
   223	        مُنفِّذ آخر إلى الحالة نفسها، يُرفع `ExecutionRefusedError` — ولا يُدّعى نجاح.
   224	
   225	        ما أضافته 1N فوقَ ما كان: أثرٌ مُعلَنٌ واحدٌ (`WRITE` على المهمّة) يُقاسُ
   226	        عليه العقد، ومفتاحُ ذرّيّةٍ يجعلُ الانتقالَ الواحدَ غيرَ قابلٍ للتكرار،
   227	        ومعوّضٌ يُعيدُ الحالةَ إلى `expected` إن فشلت العمليّة بعدَ الكتابة.
   228	        والإعادةُ (`is_replay`) تُرفَض هنا كما يُرفَض السَّبْق: الانتقالُ الواحدُ
   229	        لا يقعُ مرّتين، وإرجاعُ نجاحٍ ثانٍ كان سيكون ادّعاءً.
   230	        """
   231	        # مشروعيّةُ الانتقال تُفحَص **قبل** الحدّ: آلةُ الحالاتِ ليست سؤالَ سلطةٍ،
   232	        # وانتقالٌ مستحيلٌ لا يُصدَر له إذنٌ ولا يُحجَز له مفتاحُ ذرّيّة. وبهذا يبقى
   233	        # `IllegalTransitionError` كما كان يراه المُنادي، لا ملفوفًا في خطأِ سجلّ.
   234	        assert_transition(expected, target)
   235	        payload = dict(fields or {})
   236	        resource = f"task:{task_id}"
   237	
   238	        def _write(_effect: Any) -> bool:
   239	            return self._repo.compare_and_set(task_id, expected, target, **payload)
   240	
   241	        def _revert() -> None:
   242	            self._repo.compare_and_set(task_id, target, expected)
   243	
   244	        effect = declared_effect("WRITE", resource, f"{expected.value} → {target.value}")
   245	        guarded: GuardedResult = self._authorizer.guard_declared(
   246	            action,
   247	            resource,
   248	            declared_effects=(effect,),
   249	            applier=_write,
   250	            operation_key=operation_key(
   251	                TRANSITION_KEY_SCOPE, f"{task_id}:{expected.value}->{target.value}"
   252	            ),
   253	            compensators=(
   254	                compensator(
   255	                    effect.signature,
   256	                    _revert,
   257	                    f"إرجاع {task_id} إلى {expected.value}",
   258	                ),
   259	            ),
   260	            metadata={"from_state": expected.value, "to_state": target.value},
   331	    def advance(self, task_id: str) -> TransitionOutcome:
   332	        """خطوة واحدة حتمية في دورة حياة المهمّة، حسب حالتها الحالية."""
   333	        task = self._repo.require(task_id)
   334	        state = parse_state(task["status"])
   335	        if is_terminal(state):
   336	            raise ExecutionRefusedError(
   337	                f"المهمّة {task_id} في حالة نهائية ({state.value}) — لا تقدُّم بعدها"
   338	            )
   339	        if state is TaskState.CREATED:
   340	            return self._authorize_step(task)
   341	        if state is TaskState.AUTHORIZED:
   342	            return self._plan_step(task)
   343	        if state is TaskState.PLANNED:
   344	            return self._dispatch_step(task)
   345	        if state is TaskState.DISPATCHED:
   346	            return self._start_step(task)
   347	        return self._execute_step(task)
   348	
   349	    def _authorize_step(self, task: dict[str, Any]) -> TransitionOutcome:
   350	        """التقييم الدستوري للمهمّة نفسها: تُأذَن أو تُرفَض — والرفض قرار مُسجَّل."""
   424	    def _start_step(self, task: dict[str, Any]) -> TransitionOutcome:
   425	        """تثبيت بداية التنفيذ في القاعدة **قبل** تشغيل الوكيل.
   426	
   427	        الترتيب مقصود: مهمّة انقطع تنفيذها تُقرأ `executing` بعد إعادة التشغيل،
   428	        فيعرف الاسترداد أنها بدأت ولا يُعيد تشغيلها كأنها لم تبدأ.
   429	        """
   430	        return self._guarded_transition(
   431	            task["id"],
   432	            TaskState.DISPATCHED,
   433	            TaskState.EXECUTING,
   434	            "task.start",
   435	            detail={"agent_id": task["assigned_agent"], "started_at": _now()},
   436	        )
   437	
   438	    def _execute_step(self, task: dict[str, Any]) -> TransitionOutcome:
   439	        """التنفيذ الفعلي عبر حدّ بيئة التشغيل — لا مسار تنفيذ ثانٍ.
   440	
   476	            )
   477	        try:
   478	            outcome = self._runtime.dispatch(
   479	                task,
   480	                assignment,
   481	                authorization={
   482	                    "authorized_action": f"task.authorize.{task['type']}",
   483	                    "authorized_by": AUDIT_ACTOR,
   484	                },
   485	            )
   486	        except CapabilityDeniedError as exc:
   540	                },
   541	            )
   542	        return self._guarded_transition(
   543	            task_id,
   544	            TaskState.EXECUTING,
   545	            TaskState.COMPLETED,
   546	            "task.complete",
   547	            fields={"result": payload},
   548	            detail={
   549	                "agent_id": agent_id,
   550	                "agent_role": payload["agent_role"],
   551	                "execution_id": payload["execution_id"],
   552	                "agent_status": payload["status"],
   553	                "steps": len(payload.get("steps", []) or []),
   554	                "execution_fidelity": EXECUTION_FIDELITY,
   555	                "runtime_fidelity": payload["runtime_fidelity"],
   556	                "tool_execution_fidelity": payload["tool_execution_fidelity"],
   557	            },
   558	        )
   559	
   560	    # ── التشغيل حتى النهاية ───────────────────────────────────────────────
   561	    def run(self, task_id: str, max_steps: int = 8) -> dict[str, Any]:
   562	        """تقديم المهمّة حتى حالة نهائية أو حتى نفاد الخطوات المسموحة."""
   563	        outcomes: list[TransitionOutcome] = []
   564	        for _ in range(max_steps):
   565	            state = self._repo.state_of(task_id)
   566	            if is_terminal(state):
   567	                break
   568	            outcomes.append(self.advance(task_id))
   569	        task = self._repo.require(task_id)
   570	        return {
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "def process_case" -A 60 federal/executive/services/src/amos_federation/services/government_services/service.py
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
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "EffectKind\(|EXTERNAL" federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py
EXIT: 0
BYTES: 77
SHA256: cc4863a195a87f8823f6bca1ad23259ebb9c038a5d1dfdcfdfcdee2de68eda36
NO_EOL: 0
--- OUTPUT ---
501:        kind=contract.EffectKind(kind), resource=resource, detail=detail
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "DEFAULT_MAX_DELIVERY_ATTEMPTS: Final|^def enqueue_write_ahead|^class OutboxWorker|claims_exactly_once|\"guarantee\"" core/sovereignty/outbox.py
EXIT: 0
BYTES: 231
SHA256: ebeb60c61df7e324be1a7891aa4b56d61c10d09c1051bf705f1f66698349c2b2
NO_EOL: 0
--- OUTPUT ---
86:DEFAULT_MAX_DELIVERY_ATTEMPTS: Final[int] = 3
1055:def enqueue_write_ahead(
1211:class OutboxWorker:
1350:            "claims_exactly_once": False,
1351:            "guarantee": "AT_LEAST_ONCE_WITH_STABLE_IDEMPOTENCY_IDENTITY",
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
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
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && rg -n "Q-16|D23" docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 0
BYTES: 11781
SHA256: 781b64669c14f5b1930b543a2bd2164f0e1642c4d08730094216f56f8ddf8f77
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-24 (`W-649` — **D23 DECIDED**: إغلاقُ WI-106 · WI-107 · WI-111 وتصحيحُ خريطةِ أسطرِ WI-084 ثمَّ جولةٌ جديدةٌ (نصُّ المالكِ حرفيًّا)) · ووقبله ((`W-636/W-637` — تسجيلُ WI-109 (تحليلُ A1) · WI-110 (تحليلُ Q-9) · WI-111 (J2+J3 · 15 سطحًا محسومًا مقيسًا) READY · حرسُ D21-د تحتَ WI-040 (`NEW_ITEM_CLAIMING_ENTRY`) · N+1 لـW-631…W-635 أخضرُ (40030379965) · تصحيحُ تاريخِ الرياضِ في D21-هـ) · ووقبله ((`W-632…W-635` — قراراتُ المالكِ بتوجيهِ المستشارِ 21 على ورقةِ D20 بنصوصِها الحرفيّةِ: Q-7 · Q-8 · Q-13 · Q-14 · Q-23 · Q-26 · Q-28 · Q-29 · Q-30 · Q-32 · Q-33 · Q-34 · Q-36 · Q-37 · Q-41 · E1 DECIDED · وA1 وQ-9 وQ-10 تحليلٌ/قياسٌ أوّلًا) · ووقبله (`W-625` — **Q-71 DECIDED** بأمرِ المالكِ الصريحِ: «أذن بـconftest.py تحت WI-107» — قسمةُ نطاقِ مسارِ conftest.py من WI-072 إلى WI-107) · ووقبله (`W-612` — **D17-2** الأربعةُ مؤجَّلةٌ ولا تعطّلُ J2/J3 · **إبلاغُ ما بعدَ الدمجِ** يبقى إبلاغًا (توجيهُ المستشارِ 19 § 1)) · ووقبله ((`W-611` — **Q-61 DECIDED** بالخيارِ (3) بتطبيقٍ صريحٍ على WI-096 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-610` — **D19 DECIDED**: إذنُ المالكِ بإغلاقِ WI-105 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`))))
279:| **`HUMAN_DECISION_REQUIRED`** | **19** | Q-2 · Q-3 · Q-4 · Q-8 · Q-13 · Q-14 · Q-15 · Q-16 · Q-17 · Q-18 · Q-19 · Q-20 · Q-21 · Q-22 · Q-23 · Q-24 · Q-25 · Q-26 · Q-27 |
281:**Q-16 حاضرٌ ولم يُسقَطْ:** فعلُ `process_case` قضائيٌّ حصريٌّ بفاعلٍ تنفيذيّ · يُوقِفُ P5ز.
394:## Q-16 · هل يُعلَنُ تشغيلُ المهمّةِ أثرًا، وبأيِّ معكوسٍ صادق؟
426:### إضافةٌ مؤرَّخةٌ — قرارُ المالكِ في Q-16 (2026-10-16 · الرياض 10:00 · `W-363`)
604:تحتَ فاعلٍ قضائيٍّ يخالفُ حدَّ الاختصاصِ نصًّا، وتشغيلُ المهمّةِ هو عينُ **Q-16**.
616:- **ما يُفتَحُ بعدَه:** هجرةُ عمليّتَي `federal_judiciary/service.py` (‏`:728` و`:812` في نصِّ السؤال) **بعدَ هجرةِ Q-6** في T1. **وشقُّ تشغيلِ المهمّةِ فيه معلَّقٌ على تنفيذِ Q-16** (نوعُ الأثرِ `EXECUTION`) — فلا يُهاجَرُ ذلك الشقُّ قبلَ استيفاءِ شرطَي Q-16.
2356:## قراراتُ المالكِ — ورقةُ D23 (2026-10-24 · W-649 · نصُّ المالكِ الحرفيُّ · سابقةُ D19/W-610)
2358:**السند:** رسالةُ المالكِ إلى المنفِّذِ في الجلسةِ 2026-10-24 جوابًا على [`HANDOFFS/OWNER-DECISIONS-D23.md`](../governance/work/HANDOFFS/OWNER-DECISIONS-D23.md) · النصُّ الكاملُ حرفيًّا في [`evidence/W-649/owner_decision_D23_verbatim.md`](evidence/W-649/owner_decision_D23_verbatim.md).
2360:### D23 (1) · إغلاقُ WI-106 · WI-107 · WI-111 — DECIDED (W-649)
2363:### D23 (2) · مسارُ WI-084 — DECIDED (W-649)
3080:| Q-16 | ③ نوعُ أثرٍ جديدٌ `EXECUTION` | DECIDED في الاختيار · التنفيذُ مشروط | إضافةٌ في § Q-16 |
3091:- **الأثر:** شرطُ Q-16 (ب) · و`CLOSED` لـ`WI-076` · وكلُّ `VERIFIED` لبندٍ حسّاسٍ بعدَ قانونِ `Q-H` — **كلُّها تنتظرُ قناةَ المقعدِ الثاني**.
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && sha256sum docs/audit/evidence/W-652/briefs_wi084/briefing_grok_4_7.md
EXIT: 0
BYTES: 126
SHA256: c536106a0dadb4ddd98a8ac2c8f8c2ac91cb84676f5820ff3007abe2eb2336e2
NO_EOL: 0
--- OUTPUT ---
5036baa47e2388ecd994703ff00046d650f495f326c2fede442db2d5d4b26eeb  docs/audit/evidence/W-652/briefs_wi084/briefing_grok_4_7.md
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && cat docs/audit/evidence/W-652/briefs_wi084/SHA256SUMS
EXIT: 0
BYTES: 268
SHA256: 5b72e6e4be7fc5ff0370567deea34fcdd153a9641a0bef9187f0b0253604fe05
NO_EOL: 0
--- OUTPUT ---
34765148a7dbda4ae3a9d590a381b8ba718ff37b6fc26da4b25a45ad529ee3bc  briefing_gemini_3_8_flash.md
5036baa47e2388ecd994703ff00046d650f495f326c2fede442db2d5d4b26eeb  briefing_grok_4_7.md
74a0e240e6a4fb5eddd9c39b9e01536e86f90f563a7c04e3d694b408bcba66da  briefing_kimi_k3.md
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && nl -ba /home/user/workspace/council_w652/grok_4_7/wi084/probe/break_claimed_properties.py
EXIT: 0
BYTES: 17409
SHA256: 33df3f044e4dcfec3be7e1722affc40206300373723932853e0907d73310f16f
NO_EOL: 0
--- OUTPUT ---
     1	#!/usr/bin/env python3
     2	"""مسبارُ مقعدِ grok_4_7 لبندِ WI-084 — ليس أمرًا من إحاطةِ (ج) ولا نسخةً من فحصٍ قائم.
     3	
     4	ينادي المسارَ الإنتاجيَّ ويحاولُ كسرَ خواصَّ تدّعيها وثيقةُ
     5	docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md عن سلوكِ اليوم:
     6	
     7	  (أ) bind_compensation_plan يرفضُ عقدًا فيه أثرٌ EXTERNAL (IrreversibleEffectError)
     8	      فلا تُربَطُ خطّةٌ تبلغُ فرعَ _tracked (:385).
     9	  (ب) SovereignExecutionBoundary.execute يرفضُ عقدًا يخلطُ EXTERNAL بكتابةٍ
    10	      (MixedEffectContractError) قبلَ أن يُنادى مُطبِّقُ المُنادي.
    11	  (ج) عقدٌ EXTERNAL فقط — ولو مُرِّرَ معوّضٌ — لا يُنتِجُ compensation_plan،
    12	      ومُطبِّقُ المُنادي لا يستقبلُ الأثرَ الخارجيَّ.
    13	  (د) خطّةٌ مربوطةٌ لعقدِ WRITE ثمَّ planner يُهرِّبُ أثرَ EXTERNAL: لا يبلغُ
    14	      _tracked (فحصُ نطاقِ الإذنِ قبلَ التطبيق).
    15	  (هـ) الصادرُ (SovereignOutbox.enqueue) يرفضُ أثرًا غيرَ EXTERNAL.
    16	  (و) ExecutiveCore.run لا يُعيدُ تنفيذَ مهمّةٍ حالتُها نهائيّة (§ 1).
    17	  (ز) قراءةُ R-2: سقوطٌ بينَ dispatch (:478) وتثبيتِ EXECUTING→COMPLETED (:542)
    18	      يُبقي المهمّةَ EXECUTING فنداءٌ ثانٍ لـadvance يُنادي dispatch مرّةً أخرى.
    19	      الوثيقةُ تدّعي أنّ الشرطَ غيرُ متحقّقٍ اليوم. إن لم يُعِدِ النداءُ الثاني
    20	      dispatch فالقراءةُ مكسورة.
    21	
    22	خروجٌ 0 = لم تنكسرْ خاصيّةٌ مدّعاةٌ. خروجٌ 1 = انكسرت.
    23	"""
    24	
    25	from __future__ import annotations
    26	
    27	import tempfile
    28	from pathlib import Path
    29	
    30	from cryptography.hazmat.primitives.asymmetric import ed25519
    31	
    32	from core.constitutional_engine.engine import ConstitutionalEngine
    33	from core.constitutional_engine.ledger import ConstitutionalLedger
    34	from core.constitutional_engine.model import ActionRequest, Branch
    35	from core.sovereignty.compensation import (
    36	    Compensator,
    37	    IrreversibleEffectError,
    38	    bind_compensation_plan,
    39	)
    40	from core.sovereignty.contract import (
    41	    EffectKind,
    42	    SovereignEffect,
    43	    bind_contract,
    44	)
    45	from core.sovereignty.enforcement import ConsumedPermitLedger
    46	from core.sovereignty.enforcement_boundary import (
    47	    MixedEffectContractError,
    48	    SovereignExecutionBoundary,
    49	)
    50	from core.sovereignty.gateway import SovereignGateway
    51	from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger
    52	from core.sovereignty.outbox import (
    53	    EffectPayload,
    54	    OutboxError,
    55	    OutboxLedger,
    56	    SovereignOutbox,
    57	)
    58	from amos_federation.services.executive_core.engine import ExecutiveCore
    59	from amos_federation.services.executive_core.states import TaskState
    60	
    61	
    62	BROKEN: list[str] = []
    63	
    64	
    65	def note(held: bool, name: str, detail: str) -> None:
    66	    mark = "HELD" if held else "BROKEN"
    67	    print(f"[{mark}] {name}: {detail}")
    68	    if not held:
    69	        BROKEN.append(name)
    70	
    71	
    72	class _Provider:
    73	    name = "probe-provider"
    74	    supports_idempotency = True
    75	
    76	    def deliver(self, envelope: object) -> None:
    77	        raise AssertionError("المزوّدُ لا يُنادى من هذا المسبار")
    78	
    79	
    80	class _PermitStub:
    81	    signature_hex = ""
    82	    permit_id = "probe-permit"
    83	    decision = "ALLOW"
    84	
    85	
    86	def attack_bind_plan_for_external() -> None:
    87	    effect = SovereignEffect(
    88	        kind=EffectKind.EXTERNAL, resource="notice/probe", detail="probe"
    89	    )
    90	    contract = bind_contract(
    91	        actor=Branch.EXECUTIVE.value,
    92	        action="notify_citizen",
    93	        target="notice/probe",
    94	        declared_effects=(effect,),
    95	    )
    96	    try:
    97	        plan = bind_compensation_plan(
    98	            contract=contract,
    99	            compensators=(
   100	                Compensator(
   101	                    effect_signature=effect.signature,
   102	                    apply=lambda: None,
   103	                    description="محاولةُ عكسِ أثرٍ خارجيّ",
   104	                ),
   105	            ),
   106	        )
   107	    except IrreversibleEffectError as exc:
   108	        note(True, "bind_compensation_plan-rejects-EXTERNAL", type(exc).__name__)
   109	        return
   110	    note(
   111	        False,
   112	        "bind_compensation_plan-rejects-EXTERNAL",
   113	        f"أُعيدَت خطّةٌ {plan!r} لعقدٍ فيه EXTERNAL",
   114	    )
   115	
   116	
   117	def _boundary(tmp: Path) -> SovereignExecutionBoundary:
   118	    gateway = SovereignGateway(
   119	        ConstitutionalEngine(ledger=ConstitutionalLedger(tmp / "ledger.jsonl"))
   120	    )
   121	    outbox = SovereignOutbox(
   122	        ledger=OutboxLedger(tmp / "OUTBOX.json"),
   123	        verifying_key=ed25519.Ed25519PublicKey.from_public_bytes(
   124	            bytes.fromhex(gateway.verifying_key_hex)
   125	        ),
   126	    )
   127	    return SovereignExecutionBoundary(
   128	        gateway=gateway,
   129	        idempotency_ledger=IdempotencyLedger(tmp / "IDEMPOTENCY.json"),
   130	        outbox=outbox,
   131	        consumed_permits=ConsumedPermitLedger(tmp / "CONSUMED.json"),
   132	    )
   133	
   134	
   135	def _request(action: str, target: str) -> ActionRequest:
   136	    return ActionRequest(
   137	        actor=Branch.EXECUTIVE, action=action, target=target, channel="official"
   138	    )
   139	
   140	
   141	def attack_mixed_and_tracked(tmp: Path) -> None:
   142	    boundary = _boundary(tmp)
   143	    write = SovereignEffect(kind=EffectKind.WRITE, resource="account/probe", detail="w")
   144	    external = SovereignEffect(
   145	        kind=EffectKind.EXTERNAL, resource="account/probe", detail="x"
   146	    )
   147	    seen: list[str] = []
   148	
   149	    def applier(effect: SovereignEffect) -> None:
   150	        seen.append(effect.signature)
   151	
   152	    compensator = Compensator(
   153	        effect_signature=write.signature,
   154	        apply=lambda: None,
   155	        description="إرجاع",
   156	    )
   157	    try:
   158	        outcome = boundary.execute(
   159	            _request("credit_account", "account/probe"),
   160	            declared_effects=(write, external),
   161	            planner=lambda _permit: (write, external),
   162	            applier=applier,
   163	            operation_key=IdempotencyKey(scope="probe", value="mixed"),
   164	            compensators=(compensator,),
   165	            provider=_Provider(),
   166	            payload_of=lambda _effect: EffectPayload(data={"n": 1}),
   167	        )
   168	    except MixedEffectContractError as exc:
   169	        note(
   170	            seen == [],
   171	            "mixed-contract-rejected-before-applier",
   172	            f"{type(exc).__name__} seen={seen}",
   173	        )
   174	    else:
   175	        note(
   176	            False,
   177	            "mixed-contract-rejected-before-applier",
   178	            f"عبرَ التنفيذُ plan={outcome.compensation_plan!r} seen={seen}",
   179	        )
   180	
   181	    # عقدٌ خارجيٌّ فقط + معوّضٌ يحاولُ ربطَ خطّةٍ تبلغُ _tracked
   182	    seen.clear()
   183	    ext_only = SovereignEffect(
   184	        kind=EffectKind.EXTERNAL, resource="notice/probe", detail="only"
   185	    )
   186	    ext_comp = Compensator(
   187	        effect_signature=ext_only.signature,
   188	        apply=lambda: None,
   189	        description="لا ينبغي أن يُربَط",
   190	    )
   191	    try:
   192	        outcome = boundary.execute(
   193	            _request("notify_citizen", "notice/probe"),
   194	            declared_effects=(ext_only,),
   195	            planner=lambda _permit: (ext_only,),
   196	            applier=applier,
   197	            operation_key=IdempotencyKey(scope="probe", value="ext-only"),
   198	            compensators=(ext_comp,),
   199	            provider=_Provider(),
   200	            payload_of=lambda _effect: EffectPayload(data={"to": "citizen"}),
   201	        )
   202	    except Exception as exc:  # noqa: BLE001 — أيُّ عبورٍ أو رفضٍ غيرِ المتوقَّعِ يُعلَن
   203	        note(
   204	            False,
   205	            "external-only-plan-never-bound",
   206	            f"استثناءٌ غيرُ متوقَّع: {type(exc).__name__}: {exc}",
   207	        )
   208	    else:
   209	        plan_bound = outcome.compensation_plan is not None
   210	        caller_saw_external = any(s.startswith("EXTERNAL:") for s in seen)
   211	        note(
   212	            (not plan_bound) and (not caller_saw_external),
   213	            "external-only-plan-never-bound",
   214	            f"plan_bound={plan_bound} caller_saw={seen} enqueued={outcome.enqueued_effect_ids}",
   215	        )
   216	
   217	    # خطّةٌ مربوطةٌ (عقدُ WRITE) ثمَّ planner يُهرِّبُ EXTERNAL نحوَ _tracked
   218	    seen.clear()
   219	    sneaky = SovereignEffect(
   220	        kind=EffectKind.EXTERNAL, resource="account/probe", detail="sneak"
   221	    )
   222	
   223	    def sneak(permit: object) -> tuple[SovereignEffect, ...]:
   224	        return (write, sneaky)
   225	
   226	    try:
   227	        outcome = boundary.execute(
   228	            _request("credit_account", "account/probe"),
   229	            declared_effects=(write,),
   230	            planner=sneak,
   231	            applier=applier,
   232	            operation_key=IdempotencyKey(scope="probe", value="sneak"),
   233	            compensators=(compensator,),
   234	        )
   235	    except Exception as exc:  # noqa: BLE001
   236	        reached = any(s.startswith("EXTERNAL:") for s in seen)
   237	        note(
   238	            not reached,
   239	            "sneaked-EXTERNAL-does-not-reach-tracked-applier",
   240	            f"{type(exc).__name__}: {exc} seen={seen}",
   241	        )
   242	    else:
   243	        reached = any(s.startswith("EXTERNAL:") for s in seen)
   244	        note(
   245	            False,
   246	            "sneaked-EXTERNAL-does-not-reach-tracked-applier",
   247	            f"عبرَ التنفيذُ plan={outcome.compensation_plan is not None} seen={seen}",
   248	        )
   249	
   250	
   251	def attack_outbox_rejects_non_external(tmp: Path) -> None:
   252	    key = ed25519.Ed25519PrivateKey.generate()
   253	    outbox = SovereignOutbox(
   254	        ledger=OutboxLedger(tmp / "OUTBOX-direct.json"),
   255	        verifying_key=key.public_key(),
   256	    )
   257	    write = SovereignEffect(kind=EffectKind.WRITE, resource="account/probe", detail="w")
   258	    try:
   259	        record = outbox.enqueue(
   260	            permit=_PermitStub(),  # type: ignore[arg-type]
   261	            effect=write,
   262	            operation_key="probe-write",
   263	            provider=_Provider(),
   264	            payload=EffectPayload(data={"n": 1}),
   265	        )
   266	    except OutboxError as exc:
   267	        text = str(exc)
   268	        note(
   269	            "WRITE:account/probe" in text,
   270	            "outbox-rejects-non-EXTERNAL",
   271	            type(exc).__name__ + ": " + text.splitlines()[0],
   272	        )
   273	    else:
   274	        note(False, "outbox-rejects-non-EXTERNAL", f"قُبِلَ سجلٌّ {record.effect_id}")
   275	
   276	
   277	class _TerminalRepo:
   278	    def state_of(self, task_id: str) -> TaskState:
   279	        return TaskState.COMPLETED
   280	
   281	    def require(self, task_id: str) -> dict[str, object]:
   282	        return {"id": task_id, "status": "completed"}
   283	
   284	
   285	class _BoomRuntime:
   286	    def __init__(self) -> None:
   287	        self.calls = 0
   288	
   289	    def dispatch(self, *args: object, **kwargs: object) -> object:
   290	        self.calls += 1
   291	        raise AssertionError("أُعيدَ تنفيذُ مهمّةٍ نهائيّة")
   292	
   293	
   294	def attack_run_does_not_reexecute() -> None:
   295	    runtime = _BoomRuntime()
   296	    core = ExecutiveCore(
   297	        authorizer=object(),
   298	        repository=_TerminalRepo(),
   299	        dispatcher=object(),
   300	        audit_store=object(),
   301	        event_bus=object(),
   302	        planner=lambda _task: [],
   303	        runtime=runtime,
   304	    )
   305	    result = core.run("task-finished")
   306	    note(
   307	        runtime.calls == 0 and result["final_state"] == "completed" and result["terminal"] is True,
   308	        "run-skips-finished-task",
   309	        f"dispatch_calls={runtime.calls} final={result['final_state']} terminal={result['terminal']} transitions={result['transitions']}",
   310	    )
   311	
   312	
   313	class _ExecutingRepo:
   314	    def require(self, task_id: str) -> dict[str, object]:
   315	        return {
   316	            "id": task_id,
   317	            "status": "executing",
   318	            "assigned_agent": "agent-probe",
   319	            "plan": [{"step": 1}],
   320	            "tenant_id": "tenant-probe",
   321	            "type": "generic",
   322	            "result": {},
   323	        }
   324	
   325	    def state_of(self, task_id: str) -> TaskState:
   326	        return TaskState.EXECUTING
   327	
   328	
   329	class _Assignment:
   330	    agent_role = "probe-role"
   331	    allowed_tools = ("tool",)
   332	    required_tools = ("tool",)
   333	
   334	    def as_dict(self) -> dict[str, object]:
   335	        return {"agent_role": self.agent_role}
   336	
   337	
   338	class _Dispatcher:
   339	    def assignment_for(self, agent_id: str, plan: object, tenant_id: str | None = None) -> _Assignment:
   340	        return _Assignment()
   341	
   342	
   343	class _DispatchOutcome:
   344	    def as_dict(self) -> dict[str, object]:
   345	        return {
   346	            "status": "completed",
   347	            "execution_id": "exec-probe",
   348	            "agent_role": "probe-role",
   349	            "runtime_fidelity": "probe",
   350	            "tool_execution_fidelity": "probe",
   351	            "steps": [],
   352	        }
   353	
   354	
   355	class _CountingRuntime:
   356	    def __init__(self) -> None:
   357	        self.calls = 0
   358	
   359	    def dispatch(self, *args: object, **kwargs: object) -> _DispatchOutcome:
   360	        self.calls += 1
   361	        return _DispatchOutcome()
   362	
   363	
   364	class _AuthorizerThatDoesNotCommit:
   365	    def guard_declared(self, *args: object, **kwargs: object) -> object:
   366	        raise RuntimeError("سقطَ العاملُ قبلَ تثبيتِ EXECUTING→COMPLETED")
   367	
   368	
   369	def attack_r2_second_delivery_redispatches() -> None:
   370	    runtime = _CountingRuntime()
   371	    core = ExecutiveCore(
   372	        authorizer=_AuthorizerThatDoesNotCommit(),
   373	        repository=_ExecutingRepo(),
   374	        dispatcher=_Dispatcher(),
   375	        audit_store=object(),
   376	        event_bus=object(),
   377	        planner=lambda _task: [],
   378	        runtime=runtime,
   379	    )
   380	    errors: list[str] = []
   381	    for _ in range(2):
   382	        try:
   383	            core.advance("task-executing")
   384	        except Exception as exc:  # noqa: BLE001
   385	            errors.append(type(exc).__name__ + ": " + str(exc).splitlines()[0])
   386	    # الوثيقةُ تدّعي أنّ الشرطَ غيرُ متحقّق: النداءُ الثاني يُعيدُ dispatch.
   387	    # انكسارُ القراءةِ = النداءُ الثاني لم يُعِدِ dispatch.
   388	    note(
   389	        runtime.calls == 2,
   390	        "R2-reading-second-advance-redispatches",
   391	        f"dispatch_calls={runtime.calls} errors={errors}",
   392	    )
   393	
   394	
   395	def main() -> int:
   396	    attack_bind_plan_for_external()
   397	    with tempfile.TemporaryDirectory(prefix="wi084-probe-") as raw:
   398	        tmp = Path(raw)
   399	        attack_mixed_and_tracked(tmp)
   400	        attack_outbox_rejects_non_external(tmp)
   401	    attack_run_does_not_reexecute()
   402	    attack_r2_second_delivery_redispatches()
   403	    print(f"BROKEN_COUNT={len(BROKEN)}")
   404	    if BROKEN:
   405	        print("BROKEN_NAMES=" + ",".join(BROKEN))
   406	        return 1
   407	    print("PROBE_RESULT=no-claimed-property-broken")
   408	    return 0
   409	
   410	
   411	if __name__ == "__main__":
   412	    raise SystemExit(main())
=== RAW [19] END ===
=== RAW [20] BEGIN ===
CMD: cd /home/user/workspace/council_w652/grok_4_7/wi084/repo && PYTHONPATH=. .venv/bin/python /home/user/workspace/council_w652/grok_4_7/wi084/probe/break_claimed_properties.py
EXIT: 0
BYTES: 1219
SHA256: ea508f7a764eee2f1378faf68869cc65ed99251021abe60439bf4d588bdb9d1b
NO_EOL: 0
--- OUTPUT ---
[HELD] bind_compensation_plan-rejects-EXTERNAL: IrreversibleEffectError
[HELD] mixed-contract-rejected-before-applier: MixedEffectContractError seen=[]
[HELD] external-only-plan-never-bound: plan_bound=False caller_saw=[] enqueued=('OB-4c1958ed93293c90617a3484',)
[HELD] sneaked-EXTERNAL-does-not-reach-tracked-applier: IdempotencyError: العمليّةُ «probe:sneak» فشلت: الإذنُ «EP-9584f864efe7fa7c-1792864561» يأذن بـWRITE:account/probe، وحاول المُنفِّذُ: EXTERNAL:account/probe. لم يُطبَّق شيء. seen=[]
[HELD] outbox-rejects-non-EXTERNAL: OutboxError: الأثرُ «WRITE:account/probe» ليس خارجيًّا. صندوقُ الصادرِ للأثرِ الخارجيِّ وحدَه، ولا يُستعمَلُ مسارًا موازيًا للأثرِ المحلّيّ.
[HELD] run-skips-finished-task: dispatch_calls=0 final=completed terminal=True transitions=[]
[HELD] R2-reading-second-advance-redispatches: dispatch_calls=2 errors=['RuntimeError: سقطَ العاملُ قبلَ تثبيتِ EXECUTING→COMPLETED', 'RuntimeError: سقطَ العاملُ قبلَ تثبيتِ EXECUTING→COMPLETED']
BROKEN_COUNT=0
PROBE_RESULT=no-claimed-property-broken
=== RAW [20] END ===
VERDICT_PER_CRITERION: (1) نعم — الخريطةُ النافذةُ § 2-ب صادقةٌ على العقدةِ المراجَعةِ aba3cb45254ffbef101000ab9d13798b4a46717f. الأمرُ 7 يُسمّي EffectKind.EXTERNAL في مواضعِ القرارِ التسعة: compensation.py:103 · jurisdiction.py:170 · enforcement_boundary.py:385 و412 و579 و582 و667 · idempotency.py:983 · outbox.py:973. الأمرُ 9 يثبتُ السياق: 385 داخلَ _tracked (381–388) بعدَ plan is not None · 412 تُستعمَلُ في detect_external (421–423) · الرفضُ عندَ 584–586 · التوجيهُ عندَ 667. الأمرُ 8 لا يُظهرُ EffectKind.EXTERNAL إنتاجيًّا خارجَ core/sovereignty/ والاختبارات. المستبعَدُ في الأمرِ 7 (تعريفُ contract.py:72 و:89 · بنّاءُ outbox.py:1360 · الشروحُ · OperationStatus.EXTERNAL_PENDING عندَ 85/117 · GENESIS_EXTERNAL_HUMAN_ROOT عندَ crown.py:451 · ROOT_EXTERNAL_HUMAN · EXTERNAL_OUTBOX · MANDATORY_EXTERNAL_STAGES) ليس قرارَ سلوكٍ على نوعِ الأثر. سلوكُ قبلُ/بعدُ مكتوبٌ لكلِّ موضعٍ من التسعة. جدولُ § 2 الأصليُّ موسومٌ في الوثيقةِ نفسِها «متقادمٌ» و«لا يُنفَّذُ بها» والنافذُ § 2-ب — إبقاءُه شاهدًا لا يُلبِسُ على منفِّذٍ يتّبعُ التوسيمَ الصريحَ (ملاحظةٌ غيرُ حاجبة). (2) نعم — § 3-أ يضيفُ EXECUTION إلى EffectKind ويسمّي sovereignty_bridge.py:501 (الأمرُ 13: EffectKind(kind) من نصّ). § 3-ب يصفُ رفضَ المعوّضِ والخطّةِ عبرَ المجموعةِ نفسِها لا بقاعدةٍ جديدة. § 3-ج يصفُ 1K: enqueue_write_ahead عندَ 1055 · الضمانُ at-least-once · DEFAULT_MAX_DELIVERY_ATTEMPTS = 3 عندَ 86 · OutboxWorker عندَ 1211 (الأمرُ 14). المسبارُ (الأمرُ 20) نادى bind_compensation_plan وSovereignOutbox.enqueue وأثبتَ الرفضَين. (3) نعم — § 4 يفصلُ ثلاثةَ عقودٍ (C1 كتابةُ الحالة · C2 EXECUTION عبرَ الصادرِ بلا معوّض · C3 قيدُ النتيجة) مع ترتيبِ الفشلِ وخيارِ التسليمِ المتزامنِ (س). الأمرُ 12 يثبتُ شكلَ اليوم: process_case عندَ 1041 · 1058–1060 ثمَّ commit · 1064 run · 1071–1074 ثمَّ commit. (4) نعم — § 6 خطّةٌ مرتّبةٌ قابلةٌ للتنفيذِ كتصميم: (ر1) النوعُ والمجموعةُ والمواضعُ التسعة · (ر2) المزوّد · (ر3) هجرةُ process_case · وشرطُ صفرِ سجلّاتِ EXECUTION غيرِ النهائيّةِ قبلَ الرجوعِ عن ر1/ر2 · وgit revert بلا دفعٍ بالقوّة · مع إقرارِ أنَّ مهمّةً شُغِّلَت لا تُعاد. (5) نعم — R-1 وR-2 وR-3 وO-1 وO-2 مكتوبةٌ لا مُخمَّنة. إبقاءُ R-2 مفتوحًا يُلبّي (5) ولا ينقضُه: الخيارانِ (max_attempts = 1 أو مفتاحٌ لكلِّ خطوة) محسمانِ قبلَ بندِ الشِّفرةِ لا داخلَ وثيقةِ التصميم. قراءةُ W-650 (dispatch عندَ engine.py:478 يسبقُ تثبيتَ EXECUTING→COMPLETED عندَ :542 ومفتاحُ الذرّيّةِ للانتقالِ لا للخطوةِ عندَ :250–252) طابقتِ الأمرَ 11، والمسبارُ (الأمرُ 20) لم يستطعْ تكذيبَها: advanceٌ ثانٍ بعدَ سقوطٍ قبلَ التثبيتِ أعادَ dispatch (dispatch_calls=2). (6) نعم — أرقامُ الخريطةِ النافذةِ أُعيدَ تشغيلُها بالأوامرِ 7 و8 و9 و10 و11 و12 و13 و14 وطابقتِ العقدة. عدُّ الاختباراتِ في § 5 طابقَ الأمرَ 10: compensation 4 · enforcement_boundary 10 · idempotency 1 · outbox 3 · crown_human_root 4 · enforcement_integration 5 (ستّةُ ملفّات). أسطرُ process_case وengine.py:561 طابقتِ الأمرينِ 11 و12. ملاحظةٌ غيرُ حاجبة: § 3-ج ينسبُ claims_exactly_once: False إلى outbox.py:1351 والأمرُ 14 يضعُه في 1350 وعبارةَ الضمانِ في 1351. الحقيقةُ (False وعبارةُ الضمان) صحيحةٌ والموضعُ ليس موقعَ قرارٍ يُنفَّذُ من § 2-ب. (7) نعم — لا التزامَ تنفيذٍ لـWI-084 (الأمرُ 4: الوثيقةُ وحدَها في 5caeac5b ثمَّ 5592f88f). الوثيقةُ تشترطُ مراجعةَ مقعدينِ قبلَ الشِّفرة. هذا المقعدُ أعادَ تشغيلَ قياساتِ التصميمِ وحفظَها خامًا. نصابُ المقعدِ الثاني خارجَ عزلِ هذا المقعدِ وليس عيبًا في الوثيقة.
PROBES: كتلةُ الشِّفرةِ 19 · كتلةُ التشغيلِ 20 · المسارُ الإنتاجيُّ: bind_compensation_plan · SovereignExecutionBoundary.execute · SovereignOutbox.enqueue · ExecutiveCore.run · ExecutiveCore.advance. (أ) ادّعاءُ أنَّ bind_compensation_plan يرفضُ EXTERNAL — انكسرت؟ لا (IrreversibleEffectError). (ب) ادّعاءُ رفضِ العقدِ المختلطِ قبلَ المُطبِّق — انكسرت؟ لا (MixedEffectContractError · seen=[]). (ج) ادّعاءُ أنَّ خطّةً لا تُربَطُ لعقدٍ EXTERNAL فلا تبلغُ _tracked — انكسرت؟ لا (plan_bound=False · caller_saw=[]). (د) محاولةُ تهريبِ EXTERNAL من planner بينما خطّةُ WRITE مربوطةٌ ليبلغَ _tracked — انكسرت؟ لا (IdempotencyError يلفُّ رفضَ نطاقِ الإذن: يأذن بـWRITE:account/probe وحاول EXTERNAL:account/probe · لم يُطبَّق شيء · seen=[]). (هـ) ادّعاءُ أنَّ الصادرَ يرفضُ غيرَ EXTERNAL — انكسرت؟ لا (OutboxError على WRITE:account/probe). (و) ادّعاءُ § 1 أنَّ ExecutiveCore.run لا يُعيدُ تنفيذَ مهمّةٍ نهائيّة — انكسرت؟ لا (dispatch_calls=0). (ز) محاولةُ تكذيبِ قراءةِ R-2 — انكسرت؟ لا (dispatch_calls=2). EXIT الأمرِ 20 = 0 · BROKEN_COUNT=0. مسبارٌ لم يكسرْ خاصيّةً مُدَّعاة.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — لم أقرأْ شيئًا خارجَ استنساخِي /home/user/workspace/council_w652/grok_4_7/wi084/repo وهذهِ الإحاطةِ /home/user/workspace/council_w652/grok_4_7/wi084/briefing.md. بصمةُ الإحاطةِ المحلّيّةِ تطابقُ الأمرَ 17 وSHA256SUMS (5036baa47e2388ecd994703ff00046d650f495f326c2fede442db2d5d4b26eeb). لم أقرأْ أحكامَ W-647 ولا evidence/W-650/measurements.txt ولا نسخةَ المنسِّقِ ولا جذورَ المقاعدِ الأخرى. الاستنساخُ كاملٌ بالأمرِ git clone https://github.com/vooovg-ui/AMOS-Fedration.git إلى CLONE_PATH، ثمَّ tools/dev/bootstrap.sh داخلَ الاستنساخ، ثمَّ الأمرُ 2 للانتقالِ إلى العقدة. أدواتُ الالتقاطِ والفاحصِ قُرئت من الاستنساخِ لأنّها طريقُ التنفيذِ المفروض.
VERDICT: PASS
