# إحاطةُ جولةِ مراجعةِ البندِ: WI-107 (الدفعةُ R1 — أسطحُ السجلِّ الوطنيِّ) — مقعدُ kimi_k3
> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.

> **بنودٌ مساعدةٌ (ملزمةٌ):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — التوجيهُ 18 § 3 · وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** gemini_3_8_flash · grok_4_7 · kimi_k3 — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (لا مقعدَ من عائلةِ GLM) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w628/kimi_k3` (§ 2.6).
> **تُبصَمُ sha256 في قيدِ W-628 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-628/briefs/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُّ مراجعتُها (كاملةً):** رأسُ قيدِ **W-628** — التزامِ هذهِ الإحاطةِ نفسِهِ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-628/briefs/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2). وهي فوقَ عقدةِ شِفرةِ R1 النهائيةِ `a458db66299602154f585590fe058aa343f86bed` برِفقِ قيودٍ توثيقيّةٍ وحدَها — **وفرقُ الشِّفرةِ بينَ العقدتَينِ فارغٌ مقيسًا** (الأمرُ 4: `git diff --stat a458db6 <العقدةُ> -- federal/ tools/ tests/ agents/ core/ src/` ⇒ صفرُ ملفاتٍ) — فالشِّفرةُ المحكومةُ هي شِفرةُ R1 نفسُها. والإحاطاتُ والبصماتُ موجودةٌ في الشجرةِ عندَ هذهِ العقدةِ (لا عندَ `a458db6`) فتحققُ البصمةِ يتمُّ عندَها (الأوامرُ 22–23).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `council_w628/kimi_k3/repo`، واعملْ داخلَهُ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ عقدةِ المراجعةِ):

| WI-107 | federal-executive | T1 (الدفعةُ **R1** من خطّةِ حرقِ D-4: أسطحُ `national_registry/service.py` التسعةُ تعبرُ الحدَّ السياديَّ بفاعلٍ تنفيذيٍّ مُعلَنٍ بالفعلِ `register` — سندُ قرارِ المالكِ **D17-3** (خيارُ 1: إعلانٌ ساكنٌ بفاعلِ وحدةٍ ثابتٍ على سابقةِ FACTORY_ACTOR) وتوجيهِ المستشارِ 20 § 2 · **حسّاسٌ: سيادة بقائمةِ Q-H** · فئةُ C3: ملحقُ تصميمٍ في التزامٍ مستقلٍّ يسبقُ الشِّفرةَ ثمَّ الشِّفرةُ بفحوصِها وطفراتِها ثمَّ جولةُ مجلسٍ — **طابورٌ واحدٌ مع F1** (توجيهٌ 20 § 1)) | Perplexity Computer | مجلسُ المراجعةِ (بروتوكولُ المجلسِ · Q-59) — حسّاسٌ: إعادةُ تشغيلٍ وتقريرٌ حرفيٌّ — ولا VERIFIED بيدِ المنفِّذِ (§ 4.3) | IN_REVIEW | federal/executive/services/src/amos_federation/services/national_registry/service.py · federal/executive/services/tests/test_wi107_national_registry_register_sovereign.py · docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md · docs/audit/evidence/W-623 · docs/audit/evidence/W-624 · docs/audit/evidence/W-625 · federal/executive/services/tests/conftest.py · docs/audit/evidence/W-626 · docs/audit/evidence/W-627 · docs/audit/evidence/W-628 | 2026-10-23 | 2026-11-21 | لا عائقَ — D17-3 محسومٌ (خيارُ 1) | D-4: 166 ← 157 · السياديُّ 33 ← 42 · المواضعُ 236 ← 246 مقيسًا (W-625) · T1–T8 (+T6-ج) · M1–M5 قُتِلَت سلوكيًّا (M5 بطفرةٍ مصحّحةٍ — قتلُهُ عبرَ مسارِ الإعادةِ) · أربعةُ ملفّاتٍ خضراءُ (105: r7c 35 · 2b 53 · wi106 8 · wi107 9) و**الحزمةُ الكاملةُ خضراءُ مقيسةً: 1502 ناجحًا · 53 متخطًّى · exit=0** بعدَ إصلاحِ conftest.py بقرارِ المالكِ Q-71 · حكمُ CI يُقرأُ بالفاحصِ | — (يُكتَبُ عندَ الإغلاقِ) |

كتلةُ البندِ (كما هي عندَ عقدةِ المراجعةِ):

```text
المعرِّف: WI-107
النطاق: T1 (federal-executive · services/national_registry/service.py — حسّاسٌ: سيادة بقائمةِ Q-H · فئةُ C3)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ GLM-5.3 · بتوجيهِ المستشارِ 20 § 2)
المراجع: مجلسُ المراجعةِ (بروتوكولُ المجلسِ · Q-59) — **حسّاسٌ (سيادة · Q-H): يُعيدُ المراجعُ التشغيلَ ويحفظُ تقريرَهُ حرفيًّا ويكتبُ مسبارَهُ الخاصَّ (§ 4.9)** — ولا VERIFIED بيدِ المنفِّذِ (§ 4.3)
الحالة: IN_REVIEW   (قيدُ W-628: IN_PROGRESS→IN_REVIEW قيدًا مستقلًّا (H3 · سابقةُ W-618) — الجولةُ في الطابورِ الواحدِ مع F1 وإحاطاتُها في evidence/W-628/briefs/) · والسابقُ (تاريخٌ لا يُمحى): IN_PROGRESS   (قيدُ W-624: RESERVED→IN_PROGRESS قيدًا مستقلًّا (H3 · سابقةُ W-615) — الملحقُ والقياسُ مُودَعانِ في قيدِ W-623) · والسابقُ (تاريخٌ لا يُمحى): RESERVED   (قيدُ W-623: READY→RESERVED قيدًا مستقلًّا (H3 · سابقةُ W-614) حتى 2026-11-21 · المالكُ Perplexity Computer) · والسابقُ (تاريخٌ لا يُمحى): READY   (قيدُ W-622 · سُجِّلَ READY مباشرةً بـTHE_ROADMAP § 4 خطوة 2: محدَّدٌ · غيرُ متعارضٍ · سندُه D17-3 المحسومُ — خيارُ (1): إعلانٌ ساكنٌ بفاعلِ وحدةٍ ثابتٍ)
المسارات: federal/executive/services/src/amos_federation/services/national_registry/service.py · federal/executive/services/tests/test_wi107_national_registry_register_sovereign.py (أُنشئَ معَ شِفرةِ W-625) · docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md (ملحقُ التصميمِ — التزامٌ مستقلٌّ يسبقُ الشِّفرةَ · وتصحيحاتُه المؤرَّخةُ § 7) · docs/audit/evidence/W-623 · docs/audit/evidence/W-624 · docs/audit/evidence/W-625 (الجردُ بعدُ · الطفراتُ) · docs/audit/evidence/W-626 (تصحيحُ حمرتِ CI الأولى على عقدةِ W-625) · docs/audit/evidence/W-628 (حكمُ CI على العقدةِ المدموجةِ · إحاطاتُ الجولةِ · مسبارُ الطفراتِ)
بدأ: 2026-10-23 · الأفق: 2026-11-21

قياسُ ما قبلُ (2026-10-23 · main = b043411 — الدليلُ evidence/W-622/inventory_before_wi107.json):
  (أ) sovereign_write_inventory.py: debt 166 · sovereign 33 · المواضعُ 236 — وفي الوحدةِ 9 أسطحٍ كلُّها دَينٌ: assign_position · create_identity · create_position · grant_authority · link_agent · link_principal · revoke_assignment · revoke_authority · set_identity_status
  (ب) حيادُ الفعلِ «register» مقيسًا: ليس في الاختصاصِ الملكيِّ الحصريِّ (20 اسمًا) ولا في أفعالِ التآكلِ (16 اسمًا) — واسمَا grant_authority/revoke_authority يبقيانِ محجوبَينِ للاسمِ في البوابةِ (قرارُ التصميمِ يُوثَّقُ في الملحقِ)

خارج النطاق: نشرُ الأحداثِ بعدَ الالتزامِ (يُحسَمُ بقرارِ المالكِ) · التعديلُ على جداولِ النماذجِ أو authorization.py · أيُّ تغييرٍ على معاجمِ التاجِ في core/sovereignty

معيار القبول: (1) **قبلَ الشِّفرة**: ملحقُ التصميمِ docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md في التزامٍ مستقلٍّ يسبقُ الشِّفرةَ (Q-61) (2) الأسطحُ التسعةُ كلُّها يحملُ guard_declared( بالفعلِ register وفاعلٍ تنفيذيٍّ مُعلَنٍ ومُعوِّضٍ حقيقيٍّ ومفتاحِ عمليّةٍ (3) D-4: 166 ← 157 بالأداةِ نفسِها بلا نموٍّ في غيرِ الوحدةِ (4) فحوصُ البندِ ناجحةٌ وكلُّ طفرةٍ مُعلَنةٍ في التصميمِ تُسقِطُ فحصَها (5) فحوصُ السجلِ القائمةُ بلا تعديلٍ وحزمُ services خضراءُ في CI مقروءٍ (6) مراجعةٌ تُعيدُ التشغيلَ بمسبارِ كلِّ مقعدٍ (Q-H · § 4.9) — في طابورٍ واحدٍ مع F1 (توجيهٌ 20 § 1)

الدليل المطلوب: docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md (الملحقُ) · docs/audit/evidence/W-623/ (مسبارُ الفعلِ · جردُ الأسطحِ · حكمُ N+1) · ودليلُ الدفعةِ المنفِّذةِ (الجردُ قبلُ/بعدُ · الطفراتُ) في قيدِ الشِّفرةِ
[W-623 · 2026-10-23] READY→RESERVED (H3) — والملحقُ والأدلةُ في هذا القيدِ: مسبارُ `register` (EXECUTIVE ALLOW · والفعلُ محايدٌ) · جردُ الأسطحِ التسعةِ · حكمُ تشغيلِ main على 0129b6b (39887371108) مقروءٌ أخضرُ (واجبُ N+1 لقيدِ W-622) — لا شِفرةَ
[W-624 · 2026-10-23] RESERVED→IN_PROGRESS (H3 · سابقةُ W-615) — البوابةُ تقيسُ انتقالَ الحالةِ من قاعدةِ مدى الدمجِ إلى رأسِهِ فيقتضي التزامَي دمجٍ لانتقالَينِ (لا قفزًا READY→IN_PROGRESS) — لا شِفرةَ · والخطوةُ التاليةُ: شِفرةُ R1 (نمطُ W-617)
[W-624 · الالتزامُ الثاني] واجبُ N+1 لقيدِ W-623: حكمُ تشغيلِ main على `c6b5c2c` (39895711116) مقروءٌ أخضرُ بالفاحصِ — الدليلُ evidence/W-624
[W-625 · 2026-10-23] شِفرةُ R1 (سابقةُ W-617): الأسطحُ التسعةُ تعبرُ بالفعلِ `register` بفاعلٍ تنفيذيٍّ مُعلَنٍ ومُعوِّضٍ حقيقيٍّ ومفتاحِ عمليّةٍ — الإنشاءُ بمعرّفاتِ استدعاءٍ والربطُ والعزلُ والسحبُ بمفاتيحَ طبيعيّةٍ (وربطُ المبدأِ بالمستأجرِ) · والتحقّقُ قبلَ العبورِ (D5) والكتابةُ الوحيدةُ داخلَهُ (D4) · وقياسُ ما بعدُ (evidence/W-625/inventory_after_wi107.json): **D-4: 166 ← 157 · السياديُّ 33 ← 42 · المواضعُ 236 ← 246** — وفي الوحدةِ 19 موضعًا: 9 عامًّا كلُّها عابرةٌ و10 خاصّةً (المُطبّقاتُ المتداخلةُ) · وفحوصٌ T1–T8 (+T6-ج: الاسمُ نفسُهُ في مستأجرينِ مختلفَينِ ليسَ إعادةً) ناجحةٌ (105 لأربعةِ ملفّاتٍ بلا تعديلٍ: test_r7c 35 · test_2b 53 · test_wi106 8 · wi107 9 — والحزمةُ الكاملةُ ليست خضراءَ) · والطفراتُ M1–M4 قُتِلَ فحصُ كلٍّ سلوكيًّا وM5 أُعيدَ حصادُه بطفرةٍ مصحّحةٍ (قتلُهُ الأولى كانَ برفعِ IdentityConflictError لا بمسارِ الإعادةِ — توجيهُ المستشارِ) (evidence/W-625/mutation_M*.out.txt · وخطُّ الأساسِ أخضرُ بعدَ الاستعادةِ) · وتصحيحاتٌ مؤرَّخةٌ أربعةٌ في الملحقِ § 7 (UPDATE←WRITE · آليّةُ رفضِ T2: `register` مُنطَّقٌ فالمقيسُ سريانُ الفاعلِ المُعلَنِ والرفضُ بحكمِ محرّكٍ حقيقيٍّ في gateway.decide · مفتاحُ link_principal بالمستأجرِ · عزلُ سجلِّ الذرّيّةِ في الفحوصِ بتوجيهِ المستشارِ) · **وحاجبٌ قُطعَ بقرارِ المالكِ Q-71** («أذن بـconftest.py تحت WI-107» · قسمةُ نطاقٍ كسابقةِ Q-45): تشغيلُ الحزمةِ الكاملةِ قاسَ 115 خطأَ تهيئةٍ كلُّها سببٌ واحدٌ (إعادةُ ربطِ «crown» عبرَ سجلِّ الجلسةِ — الأدلةُ repro_r7d_crown_pair.out.txt وservices_suite_before_conftest_fix.out.txt) · 9 منها في ملفِّ الفحوصِ أُصلحت بمسحٍ شاملٍ من فاحصِ القاعدةِ (جداولُ الخدماتِ على عدةِّ `Base` فالترتيبُ من نماذجِ ORM ناقصٌ) · والباقي (106) أُصلحَ بقرارِ Q-71: مسارُ conftest.py إلى هذا البندِ (WI-072 يُضيَّقُ بقيدٍ مؤرَّخٍ) والإصلاحُ الضيّقُ نُفِّذَ فيه — سجلُّ ذرّيّةٍ **جديدٌ سليمُ الترويسةِ** لكلِّ فحصٍ (استبدالٌ بـ`os.replace` لا مسحًا: المسحُ تحتَ مصرِّحٍ حيٍّ يُنشئُ سجلًّا بلا ترويسةٍ فقِيسَ أنّ فحوصَ federation (30) وwi106 (5) وr7c (1) تُرفَضُ «سجلٌّ تالفٌ») + `reset_registry_authorizer()` قبلَ وبعدَ كلِّ فحصٍ للمصرِّحِ الوطنيِّ وحدَه · **والحزمةُ الكاملةُ خضراءُ مقيسةً: 1502 ناجحًا · 53 متخطًّى · exit=0** (evidence/W-625/services_suite_after_conftest_fix.out.txt) — حكمُ CI يُقرأُ بالفاحصِ بعدَ الدفعِ (واجبُ N+1)
[W-626 · 2026-10-23] تصحيحُ حمرةِ CI الأولى على عقدةِ W-625 (`f65ae2d` · التشغيلُ 39927107532 · سابقةُ W-594/W-600): Identity Law وTruth Audit وLint — لقطاتُ القياسِ أُعيدَ توليدُها (الدَّينُ 166 ← 157 مسجَّلةً بـ`--record-work W-625` · الموجاتُ 26+34+97=157 · الأسئلةُ 70 ← 71) ومُثبَّتاتُ test_q3 بالمقيسِ الجديدِ (8 · 26 · 18-4-4-0 · الأفعالُ 20/20/0 — سابقةُ W-402/W-535) ورقمُ حزمةِ services 1546 ← 1555 وlint أُصلحَ · الحزمةُ الكاملةُ 1502 · 53 · exit=0 والطفراتُ M1–M5 أُعيدَ حصادُها كلُّها مقتولةً · لا force-push: التزامٌ فوقَ f65ae2d · الدليلُ في evidence/W-626.
[W-627 · 2026-10-23] تصحيحُ حمرةِ CI الثانية على عقدةِ W-626 (`4b3b210` · التشغيلُ 39934595079 · سابقةُ W-626): فشلُ Lint وحده — `ruff format --check` على ملفِّ فحوصِ WI-107 · أُصلحَ بالتنسيقِ وحده (ruff format · لا دلالةَ سلوكيةَ) وملفُّ الفحوصِ أُعيدَ تشغيلُه أخضرَ (9/9) و`ruff format --check` أخضرُ على 241 ملفًا · لا تغييرَ في الإنتاجِ ولا القياساتِ · لا force-push: التزامٌ فوقَ 4b3b210 · الدليلُ في evidence/W-627.
[W-628 · 2026-10-23] IN_PROGRESS→IN_REVIEW (H3 · سابقةُ W-618 · البوابةُ تقيسُ انتقالًا واحدًا لكلِّ مدى دمجٍ) — لا شِفرةَ · وواجبُ N+1 لدفعةِ W-625/626/627: التقديمُ السريعُ لـmain إلى `a458db6` (e7609e1 ← a458db6 · الحرسُ السبعةُ أخضرُ ثمَّ قراءةُ الحكمِ في خطوةٍ مستقلةٍ) وحكمُ تشغيلِ main على العقدةِ نفسِها (39960113632) مقروءٌ أخضرُ بالفاحصِ — الدليلُ evidence/W-628/ci_verdict_39960113632_green.txt · وإحاطاتُ جولةِ R1 الثلاثةُ (gemini_3_8_flash · grok_4_7 · kimi_k3 — المنسِّقُ GLM-5.3 فلا مقعدَ من عائلتهِ) مبصَمةٌ في evidence/W-628/briefs/ في الطابورِ الواحدِ مع F1 (توجيهٌ 20 § 1 · العقدةُ المعلنةُ: رأسُ قيدِ W-628 حيثُ الإحاطاتُ وبصماتُها وفرقُ الشِّفرةِ بينَه وبينَ `a458db6` فارغٌ مقيسًا — سابقةُ W-620/W-621) · ومسبارُ طفراتٍ آليٌّ (نمطُ mutation_probe_wi106 · سابقةُ W-617): M1–M5 كلُّها مقتولةٌ سلوكيًّا والأصلُ مستعادٌ بايتًا ببايتٍ (evidence/W-628/mutation_probe_wi107.py)
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في التزاماتِ التسجيلِ W-622/W-623 والملحقِ): الملحقُ قبلَ الشِّفرةِ (Q-61) · الأسطحُ التسعةُ بفاعلٍ تنفيذيٍّ مُعلَنٍ ومُعوِّضٍ حقيقيٍّ ومفتاحِ عمليّةٍ · D-4: 166 ← 157 بالأداةِ نفسِها · فحوصُ T1–T8 ناجحةٌ وكلُّ طفرةٍ M1–M5 تُسقِطُ فحصَها · فحوصُ السجلِ القائمةُ بلا تعديلٍ وحزمُ services خضراءُ في CI مقروءٍ · مراجعةٌ تُعيدُ التشغيلَ بمسبارِ كلِّ مقعدٍ (Q-H · § 4.9) في طابورٍ واحدٍ مع F1.

### ج · أوامرُ المعاييرِ (منَ البندِ نفسِهِ)

1. `cd /home/user/workspace/council_w628/kimi_k3/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-628/briefs/`
2. `cd /home/user/workspace/council_w628/kimi_k3/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-628/briefs/)`
3. `cd /home/user/workspace/council_w628/kimi_k3/repo && git rev-parse HEAD`
4. `cd /home/user/workspace/council_w628/kimi_k3/repo && git diff --stat a458db66299602154f585590fe058aa343f86bed HEAD -- federal/ tools/ tests/ agents/ core/ src/`
5. `cd /home/user/workspace/council_w628/kimi_k3/repo && bash tools/dev/bootstrap.sh --verify`
6. `cd /home/user/workspace/council_w628/kimi_k3/repo && git log --format='%h %cI %s' e7609e1..HEAD --max-count=30`
7. `cd /home/user/workspace/council_w628/kimi_k3/repo && git diff --stat e7609e1 HEAD`
8. `cd /home/user/workspace/council_w628/kimi_k3/repo && git log --format='%h %cI %s' -3 -- docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md federal/executive/services/src/amos_federation/services/national_registry/service.py`
9. `cd /home/user/workspace/council_w628/kimi_k3/repo && git diff e7609e1 HEAD -- federal/executive/services/tests/test_r7c_national_registry.py federal/executive/services/tests/test_2b_state_registry_sovereign.py federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py`
10. `cd /home/user/workspace/council_w628/kimi_k3/repo && git diff e7609e1 HEAD -- federal/executive/services/src/amos_federation/services/national_registry/service.py`
11. `cd /home/user/workspace/council_w628/kimi_k3/repo && cat federal/executive/services/tests/test_wi107_national_registry_register_sovereign.py`
12. `cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py`
13. `cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi107_national_registry_register_sovereign.py -q`
14. `cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_r7c_national_registry.py -q`
15. `cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_2b_state_registry_sovereign.py -q`
16. `cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests -q`
17. `cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md`
18. `cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-622/inventory_before_wi107.json docs/audit/evidence/W-625/inventory_after_wi107.json`
19. `cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-628/mutation_probe_wi107.py`
20. `cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python docs/audit/evidence/W-628/mutation_probe_wi107.py`
21. `cd /home/user/workspace/council_w628/kimi_k3/repo && rg -n "D17-3|Q-61|Q-71" docs/audit/SOVEREIGN_DECISION_REGISTER.md`
22. `cd /home/user/workspace/council_w628/kimi_k3/repo && sha256sum docs/audit/evidence/W-628/briefs/briefing_kimi_k3.md`
23. `cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-628/briefs/SHA256SUMS`
24. `cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q`
25. `cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-###)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out <دليلُك>/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ في جولاتِ C3 · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **المسارَ الإنتاجيَّ** (`NationalRegistry`) ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** في (ب) (مثلًا: سطحٌ يكتبُ بلا عبورٍ للحدِّ · فاعلٌ غيرُ تنفيذيٍّ يمرُّ · كتابةٌ فاشلةٌ بلا تعويضٍ · مفتاحٌ طبيعيٌّ بلا مستأجرٍ يسمحُ إعادةً · ربطُ مبدأٍ بقائمةِ انتظارٍ). احفظْه في دليلِكَ تحتَ `probe/`، واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.

### و · صيغةُ جوابِكَ (يُحفظُ حرفيًّا بلا تحريرٍ)
```
MODEL: <اسمُ النموذجِ كما أعلنتْهُ المنصةُ>
FAMILY: <العائلةُ>
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: <sha>
CLONE_PATH: <المسارُ>
COMMANDS_RUN:
 1. <الأمرُ حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 2. …
RAW_OUTPUTS:
<كتلُ RAW كما كتبتْها أداةُ الالتقاطِ — متتاليةً بلا أيِّ نصٍّ بينها:>
=== RAW [1] BEGIN ===
CMD: <الأمر>
EXIT: <رمزُ الخروج>
BYTES: <عدد>
SHA256: <بصمة>
NO_EOL: <0|1>
--- OUTPUT ---
<المخرجُ كلُّهُ>
=== RAW [1] END ===
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ>
PROBES: <لكلِّ مسبارٍ: رقمُ كتلةِ شِفرتِه · رقمُ كتلةِ تشغيلِه · الخاصيّةُ التي حاولَ كسرَها · انكسرت؟ نعم/لا>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرار>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتُه (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وحكمُ PASS بلا مسبارٍ خاصٍّ على المسارِ الإنتاجيِّ لا يُحتسَبُ (§ 4.9) · وملفُّ حكمِكَ في دليلِكَ يُحفَظُ حرفيًّا في المستودعِ (§ 4.8).
