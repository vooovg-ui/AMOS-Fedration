# Q-87 (ج): الفاعلون الأربعة على الأفعالِ الحصريّة (تصميم · WI-126)

> **التعريف:** تصميمُ تنفيذِ القرارِ 5 من `Q-87`: «يُمنَع STATE وINSTITUTION بـR-003-1 كما أُضيف AGENT وSYSTEM في Q-68؛ ويُشترَط لـHUMAN موافقة بشرية موسومة (قناة human_approval المستعملة في W-740) على الأفعال الحصرية وعلى أفعال المال؛ ويُوحَّد حكم review مع execute لـROYAL بلا مرسوم (كلاهما رفض)».
> **النطاق:** `core/constitutional_engine/rules.py` (`_r003_1` وحدَها) · الفحوصُ الستّةُ التي قاسَها W-763 · ملفُّ فحوصٍ جديد. **لا شِفرةَ في هذا القيد.** ولا مساسَ بـ`gateway.py` (WI-085) ولا بـK1.
> **المالك:** Perplexity Computer (منسِّقٌ لا مصوِّت) · البندُ `WI-126` · القيدُ `W-766`.
> **تاريخ الإنشاء:** 2026-10-31 · **تاريخ آخر تعديل:** 2026-10-31.
> **الدليل:** `docs/audit/evidence/W-763/` (`four_actor_usage.txt` · `experiment_rules.patch` · `experiment_root_suite.txt` · `experiment_services_suite.txt`).
> **المحتويات:** § 1 الحالُ المقيس · § 2 القاعدة · § 3 ما ينكسرُ وكيفَ يُعالَج · § 4 القسمة · § 5 الفحوص · § 6 ما لا يفعلُه.

---

## 1. الحالُ المقيس (W-763)

- `_r003_1` اليومَ: الفروعُ الأربعةُ لا يمارسُ أحدُها حصريَّ غيرِه، و`AGENT`/`SYSTEM` (Q-68) لا يمارسانِ أيَّ حصريّ. أمّا `HUMAN` و`STATE` و`INSTITUTION` و`ROYAL` فتعودُ `None`: لا رفض.
- لا مُنادٍ إنتاجيٌّ يبني `Branch.STATE` أو `Branch.INSTITUTION`. و`Branch.HUMAN` في ثلاثةِ مواضع، والمداخلُ الديناميكيّةُ ثلاثة (`cli.py` ×2 · `sovereignty_bridge.py:360`).
- `ROYAL` بلا مرسوم: `classify` يرفعُ `RoyalAuthenticityError`، فـ`gateway.review` يُقيِّمُه طرفًا تابعًا (غيرَ سياديّ) فيُرجِعُ **ALLOW** لـ`issue_ruling`، بينما `execute` يرفضُه. هذا التفاوتُ هو ما يُوحِّدُه القرار.
- الرقعةُ التجريبيّة: الخدماتُ 1871/53/0 · الجذرُ 6 فشل (4 أمثلةٌ بـSTATE · 1 يتوقّعُ ROYAL بلا مرسوم ALLOW لـ`issue_ruling` · 1 طزاجةُ أثرٍ مُولَّدٍ لا تُنسَبُ للرقعة).

## 2. القاعدة (في `_r003_1` · والأثرُ للتاجِ يبقى ADVISORY)

`EXCLUSIVE = اتّحادُ _BRANCH_EXCLUSIVE`:

| الفاعل | الشرط | الحكم |
|---|---|---|
| `STATE` · `INSTITUTION` | الفعلُ في `EXCLUSIVE` | رفضٌ بنصِّ Q-68 نفسِه (يُضافانِ إلى `_NON_BRANCH_EXCLUDED`) |
| `HUMAN` | الفعلُ في `EXCLUSIVE ∪ NON_CONSTITUTIONAL_MONEY_ACTIONS` **و** لا (`human_approved` **و** `metadata["human_approval_source"]` غيرُ فارغ) | رفض |
| `ROYAL` | `royal_decree is None` **و** الفعلُ في `EXCLUSIVE` | رفض |

- **الوسمُ** هو ما تكتبُه قناةُ W-740 (`sovereignty_bridge.guard_declared(human_approval=…)` تُثري `metadata["human_approval_source"] = human_approval.source`). فـ`human_approved=True` وحدَه بلا مصدرٍ لا يكفي، وهذا مقصودُ «موسومة».
- **ROYAL بمرسوم** لا يمسُّه التغيير: يُصنَّفُ سياديًّا، وأثرُ R-003-1 للتاجِ ADVISORY (رأيٌ لا منع).
- **التوحيد:** `review` يُقيِّمُ ROYAL بلا مرسومٍ طرفًا تابعًا، و`R-003-1` مُلزِمةٌ للتابع، فيصيرُ `review` رفضًا كـ`execute`. ولا تُمَسُّ `gateway.py`.
- أفعالُ المالِ لـSTATE وINSTITUTION وROYAL خارجَ نصِّ القرار (النصُّ قيَّدَ المالَ بـHUMAN وحدَه) فلا تُضاف.

## 3. ما ينكسرُ وكيفَ يُعالَج (بأمرِ التوجيهِ 36 § 2 بند 4)

| الفحص | سببُ الكسر | المعالجة |
|---|---|---|
| `test_enforcement_integration.py` ×3 (`Branch.STATE` مثالًا لتابعٍ يُنفِّذُ `execute_task`) | `execute_task` حصريٌّ للتنفيذيّ | **يُحدَّثُ لا يُحذَف:** المثالُ يصيرُ `Branch.EXECUTIVE` (تابعٌ يملكُ الفعل)، والتأكيداتُ نفسُها بلا تخفيف |
| `test_supreme_authority.py::…سلسلة_القرار_التابع…` (`STATE` مثالًا) | كالسابق | **يُحدَّثُ لا يُحذَف** بالطريقةِ نفسِها؛ وحالةُ `opt_out_constitution` تبقى رفضًا كما هي |
| `test_q3_branch_declaration_surface.py::test_issue_ruling_is_denied_for_the_default_actor_and_allowed_for_judicial` (`verdicts["ROYAL"][0] == "ALLOW"`) | يتوقّعُ ALLOW لـROYAL بلا مرسوم | **يُعدَّلُ إلى DENY لأنه نقيضُ القرار** (التوجيه 36 § 2 بند 4)، ويُكتَبُ هذا في القيدِ وفي سطرِ الفحص |
| `test_w099_generated_artifact_freshness` | أثرٌ مُولَّدٌ متقادمٌ، لا يُنسَبُ للرقعة | يُعادُ توليدُ الأثرِ في القيدِ نفسِه إن ظهر |

ولا يُحذَفُ فحصٌ ولا يُضعَّفُ تأكيد.

## 4. القسمة (مُعلَنة)

`core/constitutional_engine/rules.py` في `WI-124` و`WI-120` (IN_REVIEW)، و`test_enforcement_integration.py` في `WI-033` (IN_REVIEW)، و`test_q3_branch_declaration_surface.py` في `WI-120` (IN_REVIEW). تُقسَمُ إلى `WI-126` عندَ انتقالِه إلى `IN_PROGRESS` (قيدُ الشِّفرة)، بسطرٍ مؤرَّخٍ في كلِّ بند، كسابقةِ W-756. وشِفرةُ تلك البنودِ في هذه الملفّاتِ تبقى تحتَ مراجعتِها، والتغييرُ يمسُّ `_r003_1` والفحوصَ المذكورةَ وحدَها.

## 5. الفحوص (في قيدِ الشِّفرة)

- `tests/constitutional/test_q87_four_actors.py`: لكلِّ فاعلٍ من الأربعة × فعلٌ حصريٌّ من كلِّ فرع ⇐ DENY بـR-003-1 · HUMAN مع `human_approved` بلا مصدر ⇐ DENY · HUMAN بموافقةٍ موسومة ⇐ لا يرفضُه R-003-1 · HUMAN على فعلِ مالٍ بلا وسم ⇐ DENY · ROYAL بمرسومٍ ⇐ لا منعَ (رأيٌ ADVISORY) · `review` و`execute` لـROYAL بلا مرسومٍ كلاهما رفض.
- طفرتان: حذفُ STATE/INSTITUTION من المجموعة ⇐ فحصٌ يسقط · قبولُ `human_approved` بلا مصدر ⇐ فحصٌ يسقط.
- المجموعتان كاملتين.

## 6. ما لا يفعلُه

- لا يمسُّ `gateway.py` ولا `authority.py` ولا K1 (`royal/main.py`).
- لا يُغيِّرُ أثرَ R-003-1 للتاج (ADVISORY).
- لا يُضيفُ مُنادِيًا لـSTATE أو INSTITUTION في الإنتاج، ولا يُعيِّنُ مراجعًا.
