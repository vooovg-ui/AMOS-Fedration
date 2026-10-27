# إحاطةُ جولةِ مراجعةِ البندِ: WI-117 (تحصينُ مساراتِ الخفضِ وإنشاءِ الترقيةِ وفحصِ البوّابةِ بـrequire_king — D25-2) — مقعدُ kimi_k3
> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.

> **بنودٌ مساعدةٌ (ملزمةٌ):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** gemini_3_8_flash · grok_4_7 · kimi_k3 — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (لا مقعدَ من عائلةِ GLM) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w701/kimi_k3/wi117` (§ 2.6).
> **سندُ الجولةِ (توجيهُ المستشارِ 25 § 1 · قرارُ المالكِ D27):** «جولة المجلس تُطلَق الآن ولا تنتظر G1: E1 اكتمل 14/14، فلا موجب للتأجيل. تشمل WI-117 وWI-119 وما صار منفَّذًا من WI-115 (الكاشف)، وتُجمَع أحكامها في الجلسة نفسها (Q-72) بمسبار لكل مقعد وأدلة منفصلة.»
> **هذه جولةٌ واحدةٌ** بثلاثةِ نطاقاتٍ (WI-117 · WI-119 · الكاشفُ المنفَّذُ من WI-115) تُجمَعُ أحكامُها في الجلسةِ نفسِها — وهذه إحاطةُ نطاقِكَ فيها لا جولةً مستقلةً (تسلسلُ الجولاتِ § 8 بندُ 5 محفوظٌ: جولةٌ واحدةٌ في آنٍ واحدٍ).
> **تُبصَمُ sha256 في قيدِ W-701 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w701/kimi_k3/wi117/repo`، وأعدَّ بيئتَه بـ`tools/dev/bootstrap.sh` داخلَه، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ في W-701 — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

| WI-117 | federal-executive | T1 (**C3** · تحصينٌ فوريٌّ بقرارِ المالكِ D25-2 حرفيًّا: «تحصين فوري للمسارات (مستقل عن العبور): تُقيَّد مسارات الخفض (reset) وإنشاء الترقية وفحص البوابة بـrequire_king (الموجود في auth.py:120) دون انتظار تصميم العبور. تُترك مسارات الرفع (activate) على حالها لأن الرفع هو الاتجاه الآمن. هذا بند C3 مستقل بتصميم قصير ومسبار يشغّل طلب HTTP حقيقيًّا برمز مواطن ويُثبت الرفض، ومطفرة تُسقط القيد.») | Perplexity Computer | مجلسُ المراجعةِ (بروتوكولُ المجلسِ · C3 · مسبارٌ لكلِّ مقعدٍ) — ولا VERIFIED بيدِ المنفِّذِ | IN_REVIEW | federal/executive/services/src/amos_federation/services/governance/main.py · federal/executive/services/src/amos_federation/services/control_console/main.py · federal/executive/services/tests/test_wi117_king_guard_routes.py · federal/executive/services/tests/test_governance.py · federal/executive/services/tests/test_control_console.py · docs/audit/WI117_KING_GUARD_DESIGN.md · docs/audit/evidence/W-687 · docs/audit/evidence/W-688 · docs/audit/evidence/W-689 · docs/audit/evidence/W-690 · docs/audit/evidence/W-692 · federal/executive/services/tests/per_test_auth.py | 2026-10-25 | 2026-11-22 | لا عائقَ — وخفضُ activate (DISC-138) وجهتُه WI-114 السطحُ 1 | التصميمُ القصيرُ مودَعٌ في W-687 (معيارُ النجاحِ: مسبارُ HTTP حقيقيٌّ برمزِ مواطنٍ ⇒ 403 + طفرةٌ · وإلحاقُ sign_approval بقرارِ التوجيهِ 24 § 1) · ثمَّ IN_PROGRESS في دفعةٍ تسبقُ دفعةَ الشِّفرةِ مباشرةً (DISC-137) — نُقِلَ إليها في W-688 · **أولويةٌ مطلقةٌ (التوجيهُ 24 § 1)** · **الشِّفرةُ نُفِّذَت في W-689** (require_king ×4 + sign_approval منَ الرمزِ + 13 فحصًا + طفرةٌ + مسبارُ HTTP) — بانتظارِ جولةِ المجلسِ (مسبارٌ لكلِّ مقعدٍ) | قيدُ W-701 — إذنُ الإغلاقِ بعدَ VERIFIED بإجماعِ المجلسِ صدرَ بقرارِ D27 (لا سؤالَ جديدًا) · جولةُ المجلسِ (W-701) |

كتلةُ البندِ (كما هي عندَ كتابةِ هذهِ الإحاطةِ):

```text
المعرِّف: WI-117
النطاق: T1 (federal-executive · C3 — governance/main.py وcontrol_console/main.py وفحوصُهما · مستقلٌّ عن تصميمِ العبورِ WI-114)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · بقرارِ المالكِ D25-2 في التوجيهِ 23 § 1)
المراجع: مجلسُ المراجعةِ (بروتوكولُ المجلسِ · C3 · مسبارٌ لكلِّ مقعدٍ) — ولا VERIFIED بيدِ المنفِّذِ
الحالة: IN_REVIEW   (قيدُ W-689 — IN_PROGRESS→IN_REVIEW: الشِّفرةُ نُفِّذَت كاملةً وفقَ تصميمِ W-687 § 2 (require_king ×4 + sign_approval + 13 فحصًا + طفرةٌ مقتولةٌ + مسبارُ HTTP حقيقيٌّ) والحزمُ خضراءُ (الجذرُ 2758 · الخدماتُ 1606) · بانتظارِ جولةِ المجلسِ · والسابقُ: قيدُ W-688 — RESERVED→IN_PROGRESS تنفيذًا لإجراءِ DISC-137)
المسارات: federal/executive/services/src/amos_federation/services/governance/main.py · federal/executive/services/src/amos_federation/services/control_console/main.py · federal/executive/services/tests/test_wi117_king_guard_routes.py · federal/executive/services/tests/test_governance.py · federal/executive/services/tests/test_control_console.py · docs/audit/WI117_KING_GUARD_DESIGN.md (تصميمٌ قصيرٌ يسبقُ الشِّفرةَ) · docs/audit/evidence/W-687 (قيدُ W-687) · docs/audit/evidence/W-688 (قيدُ W-688 — انتقالُ الحالةِ وحكمُ N+1 وواجبُ ما بعدَ الدمجِ)
بدأ: 2026-10-25 · الأفق: 2026-11-22

السبب: D25-2 حرفيًّا: «تحصين فوري للمسارات (مستقل عن العبور): تُقيَّد مسارات الخفض (reset) وإنشاء الترقية وفحص البوابة بـrequire_king (الموجود في auth.py:120) دون انتظار تصميم العبور. تُترك مسارات الرفع (activate) على حالها لأن الرفع هو الاتجاه الآمن. هذا بند C3 مستقل بتصميم قصير ومسبار يشغّل طلب HTTP حقيقيًّا برمز مواطن ويُثبت الرفض، ومطفرة تُسقط القيد.» · وقياسُ ما قبلُ (evidence/W-672/http_probe_before.txt · طلباتُ HTTP حقيقيّةٌ عبرَ uvicorn برمزٍ `role=citizen`): reset في الوحدتَينِ ⇒ 200 و`level`=normal · إنشاءُ الترقيةِ ⇒ 201 · `human_approval` passed ⇒ 200 · وفحوصٌ تمرُّ اليومَ برمزٍ غيرِ ملكٍ في نطاقِ القرارِ: 6 (evidence/W-672/sim_require_king.txt)

خارج النطاق: عبورُ canary.py (WI-114) · تمثيلُ الموافقةِ عبرَ الجسرِ (D25-1 · WI-114 السطحانِ 2 و4) · مساراتُ activate بنصِّ D25-2 «تُترك … على حالها» — وخفضُها المُقنَّعُ (DISC-138) يُسَدُّ في canary.py بـWI-114 السطحِ 1 (تصميمُه § 3.3) · مساراتُ canary (`POST /v1/canary` و`/rollback`) · تغييرُ `require_king` نفسِه

معيار القبول: (1) `POST /v1/system/kill-switch/reset` (governance) و`POST /v1/kill-switch/reset` (control_console) و`POST /v1/promotions` و`POST /v1/promotions/{id}/gates` محروسةٌ بـ`require_king` (2) مسبارٌ يشغّلُ **طلبَ HTTP حقيقيًّا** برمزِ مواطنٍ على كلٍّ منها ويُثبِتُ الرفضَ (403) وأنَّ المستوى لم يتغيّرْ — مخرجٌ حرفيٌّ (3) رمزُ الملكِ يمرُّ (4) مطفرةٌ تُسقِطُ القيدَ عن كلِّ مسارٍ فيكتشفُها فحصٌ (5) الفحوصُ الستُّ التي تمرُّ اليومَ برمزِ مواطنٍ تُحدَّثُ إلى رمزِ ملكٍ بلا إضعافِ ما تفحصُه (6) مسبارٌ لكلِّ مقعدٍ

الدليل المطلوب: التصميمُ القصيرُ · الفرقُ · مسبارُ HTTP قبلُ/بعدُ خامًا · سجلُّ الطفراتِ · الحزمُ قبلُ/بعدُ
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ: (1) `POST /v1/system/kill-switch/reset` (governance) و`POST /v1/kill-switch/reset` (control_console) و`POST /v1/promotions` و`POST /v1/promotions/{id}/gates` محروسةٌ بـ`require_king` (2) مسبارٌ يشغّلُ طلبَ HTTP حقيقيًّا برمزِ مواطنٍ على كلٍّ منها ويُثبِتُ الرفضَ (403) وأنَّ المستوى لم يتغيّرْ — مخرجٌ حرفيٌّ (3) رمزُ الملكِ يمرُّ (4) مطفرةٌ تُسقِطُ القيدَ عن كلِّ مسارٍ فيكتشفُها فحصٌ (5) الفحوصُ الستُّ التي تمرُّ اليومَ برمزِ مواطنٍ تُحدَّثُ إلى رمزِ ملكٍ بلا إضعافِ ما تفحصُه (6) مسبارٌ لكلِّ مقعدٍ.

**إفصاحاتُ المنسِّقِ (تُحكَمُ لا تُسلَّمُ):** (1) الشِّفرةُ في التزامِ `f8d33807` (قيدُ W-689) — والأمرانِ 6 و7 يُريانِكَ الفرقَ والحُرّاسَ. (2) **المعيارُ (4) طفرةٌ:** سجلُّ طفراتِ المنفِّذِ ليسَ من حدودِ قراءتِكَ — أعِدِ الطفرةَ بنفسِكَ: **خطُّ الأساسِ أولًا** (الأمرُ 8 أخضرُ) ثمَّ الأمرُ 11 يُسقِطُ الحرسَ كلَّهُ (المعاملُ `Depends(require_king)` في توقيعِ كلِّ مسارٍ — لا ديكوريتور) من الملفَّينِ معًا ويُشغِّلُ الفحصَ نفسَه (يُتوقَّعُ سقوطُه على تأكيدِ الحارسِ لا على خطأِ واجهةٍ — احكمْ من مخرجِ pytest أيُّ الفحوصِ سقطت ولماذا) ثمَّ الأمرُ 12 يسترجعُ الملفَّينِ ويُثبِتُ نظافةَ الشجرةِ. ولمجرّكَ في مسبارِكَ (السؤالُ 6) أن يُسقِطَ حارسَ مسارٍ واحدٍ وحدَه من الأربعةِ ويُشغِّلَ الفحوصَ — كلُّ مسارٍ على حدةٍ. والأمرُ 10 (فحوصٌ جديدةٌ على شجرةٍ قديمةٍ) دليلُ تاريخٍ مكمِّلٌ لا كافٍ وحدَه: إن كانَ سقوطُه بخطأِ استيرادٍ لا بتأكيدٍ دلاليٍّ فلا يُثبِتُ المعيارَ وحدَه. (3) **المعيارُ (2) مسبارُ HTTP:** مسبارُ المنفِّذِ الخامُّ ليسَ من حدودِ قراءتِكَ — **مسبارُكَ الخاصُّ (السؤالُ 6) هو الدليلُ**: شغِّلِ الخدمةَ عبرَ uvicorn برمزِ مواطنٍ (`role=citizen`) واطلبِ المساراتِ الأربعةَ — الرفضُ 403 دونَ تغييرِ المستوى، وبرمزِ الملكِ تمرُّ (المعيارُ 3). (4) **فحوصُ § 2 (المعيارُ 5):** الأمرُ 9 يُشغِّلُ حزمتَي الحوكمةِ والوحدةِ الكاملتَينِ — عُدَّ الفحوصَ التي تمرُّ برمزِ ملكٍ. (5) **حدودُ العزلِ المعلَنةُ:** المقاعدُ الثلاثةُ تعملُ في صندوقٍ واحدٍ مشتركٍ بجذورٍ منفصلةٍ (`/home/user/workspace/council_w701/<مقعد>/`) — لا تقرأْ ولا تكتبْ خارجَ جذرِكَ، ولا تقرأْ نسخةَ المنسِّقِ (`/home/user/workspace/amos`) ولا أدلّةَ المنفِّذِ (`docs/audit/evidence/W-68*`/`W-69*`/`W-70*` عدا هذه الإحاطةِ).

### ج · أوامرُ المعاييرِ

1. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/`
2. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/)`
3. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git rev-parse HEAD`
4. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py`
5. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git show --stat f8d33807`
6. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git diff f8d33807^ f8d33807 -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py`
7. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rg -n "require_king" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py`
8. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py`
9. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py`
10. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rm -rf ../old && git worktree add --detach ../old f8d33807^ && cp federal/executive/services/tests/test_wi117_king_guard_routes.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/kimi_k3/wi117/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py`
11. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && sed -i "s/Depends(require_king)/Depends(require_auth)/g" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py`
12. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && git checkout -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && git status --short && git diff --stat`
13. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && rg -n "D25-2|require_king" docs/audit/SOVEREIGN_DECISION_REGISTER.md`
14. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && sha256sum docs/audit/evidence/W-701/briefs_wi117/briefing_kimi_k3.md`
15. `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && cat docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- الشِّفرةُ والفحوصُ والوثائقُ التي تُسمّيها أوامرُ (ج) في استنساخِكَ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w701/kimi_k3/wi117/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُشغِّلُ **طلبَ HTTP حقيقيًّا** عبرَ uvicorn (أو ما يصلُهُ من الشفرةِ الإنتاجيّةِ) برمزِ مواطنٍ على المساراتِ الأربعةِ المحروسةِ ويُثبِتُ الرفضَ (403) وعدمَ تغييرِ المستوى، ثمَّ يُثبِتُ المرورَ برمزِ الملكِ. احفظْه في دليلِكَ تحتَ `/home/user/workspace/council_w701/kimi_k3/wi117/probe/`، واعرضْ شِفرتَهُ بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْهُ بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ أثبتَ مرورًا برمزِ مواطنٍ ملاحظةٌ حاجبةٌ.
7. بعدَ كتابةِ حكمِكَ شغِّلِ الفاحصَ عليه: `cd /home/user/workspace/council_w701/kimi_k3/wi117/repo && .venv/bin/python tools/governance/council_verdict_raw_check.py --brief docs/audit/evidence/W-701/briefs_wi117/briefing_kimi_k3.md --repo . /home/user/workspace/council_w701/kimi_k3/wi117/VERDICT.md` وألصقْ مخرجَه ورمزَ خروجِه في ردِّكَ (لا في VERDICT.md).

### و · صيغةُ جوابِكَ (يُكتَبُ في `/home/user/workspace/council_w701/kimi_k3/wi117/VERDICT.md` ويُحفظُ حرفيًّا بلا تحريرٍ)
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

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتُه (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وحكمُ PASS بلا مسبارٍ خاصٍّ لا يُحتسَبُ (§ 4.9) · وملفُّ حكمِكَ في دليلِكَ يُحفَظُ حرفيًّا في المستودعِ (§ 4.8).
