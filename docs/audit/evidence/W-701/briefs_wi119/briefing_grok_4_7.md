# إحاطةُ جولةِ مراجعةِ البندِ: WI-119 (عبورُ الأسطحِ الـ14 المباشرةِ تحتَ D-4 للحدِّ السياديِّ — E1 · حرقٌ حقيقيٌّ) — مقعدُ grok_4_7
> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.

> **بنودٌ مساعدةٌ (ملزمةٌ):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** gemini_3_8_flash · grok_4_7 · kimi_k3 — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (لا مقعدَ من عائلةِ GLM) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w701/grok_4_7/wi119` (§ 2.6).
> **سندُ الجولةِ (توجيهُ المستشارِ 25 § 1 · قرارُ المالكِ D27):** «جولة المجلس تُطلَق الآن ولا تنتظر G1: E1 اكتمل 14/14، فلا موجب للتأجيل. تشمل WI-117 وWI-119 وما صار منفَّذًا من WI-115 (الكاشف)، وتُجمَع أحكامها في الجلسة نفسها (Q-72) بمسبار لكل مقعد وأدلة منفصلة.»
> **هذه جولةٌ واحدةٌ** بثلاثةِ نطاقاتٍ (WI-117 · WI-119 · الكاشفُ المنفَّذُ من WI-115) تُجمَعُ أحكامُها في الجلسةِ نفسِها — وهذه إحاطةُ نطاقِكَ فيها لا جولةً مستقلةً (تسلسلُ الجولاتِ § 8 بندُ 5 محفوظٌ: جولةٌ واحدةٌ في آنٍ واحدٍ).
> **تُبصَمُ sha256 في قيدِ W-701 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-701/briefs_wi119/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi119/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w701/grok_4_7/wi119/repo`، وأعدَّ بيئتَه بـ`tools/dev/bootstrap.sh` داخلَه، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ في W-701 — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

| WI-119 | federal-executive | T1 (**C3 · حرقٌ حقيقيٌّ** — عبورُ الأسطحِ الـ14 المباشرةِ تحتَ D-4 للحدِّ السياديِّ بنمطِ WI-082 وتصحيحِه (مفاتيحُ الإعادةِ · نوى خاصّةٌ بلا تعشيشٍ) وفقَ خطةِ حرقِ D-4 وتوجيهِ المستشارِ 24 § 2 حرفيًّا) | Perplexity Computer | جولةُ مجلسٍ واحدةٌ (بعدَ E1 وG1 وتحليلِ D-4/المستدعين وتصميمِ WI-116 · § 2) | IN_REVIEW | docs/audit/E1_EXECUTIVE_IDENTITY_CROSSING_DESIGN.md · docs/audit/evidence/W-693 · docs/audit/evidence/W-695 · docs/audit/evidence/W-696 · docs/audit/evidence/W-697 · docs/audit/evidence/W-698 · docs/audit/evidence/W-699 · docs/audit/evidence/W-700 · core/constitutional_engine/rules.py · federal/executive/services/src/amos_federation/services/agent_runtime · federal/executive/services/src/amos_federation/services/executive_core · federal/executive/services/tests/test_executive_core.py · federal/executive/services/tests/test_e1_executive_identity_crossing.py · federal/executive/services/tests/test_phase7_health.py · federal/executive/services/tests/test_w699_agent_runtime_crossing.py | 2026-10-26 | 2026-11-22 | قرارُ المالكِ على توسيعِ معجمِ EXECUTIVE_ACTIONS (§ 5 من التصميمِ — توسيعٌ مضيِّقٌ على سابقةِ Q-18) | التصميمُ مودَعٌ في W-694 (docs/audit/E1_EXECUTIVE_IDENTITY_CROSSING_DESIGN.md) — نموذجُ الصلاحياتِ وجدولُ الأسطحِ والأفعالُ ومستوياتُ الإيقافِ وخطةُ الفحوصِ · القياسُ بعدَ الشِّفرةِ هو القبولُ | قيدُ W-701 — IN_PROGRESS→IN_REVIEW بأمرِ المالكِ في التوجيهِ 25 § 1: الجولةُ الآنَ لا بعدَ G1 (الإغلاقُ بعدَ VERIFIED بإجماعٍ بإذنِ D27) · والشِّفرةُ 14/14 في W-696+W-699 (الدَّينُ 121 · السياديّةُ 59) · جولةُ المجلسِ (W-701) |

كتلةُ البندِ (كما هي عندَ كتابةِ هذهِ الإحاطةِ):

```text
المعرِّف: WI-119
النطاق: T1 (federal-executive · تصميمٌ مودَعٌ ثمَّ شِفرةٌ لاحقةٌ · agent_runtime (8 أسطحٍ) وexecutive_core (6 أسطحٍ))
المالك: Perplexity Computer (بتوجيهِ المستشارِ 24 § 2)
المراجع: جولةُ مجلسٍ واحدةٌ — **تعديلٌ مؤرَّخٌ (قيدُ W-701 · قرارُ المالكِ D27): الجولةُ تُطلَقُ الآنَ ولا تنتظرُ G1 وتشملُ WI-117 وWI-119 والكاشفَ المنفَّذَ من WI-115** · والنصُّ الأصليُّ (تاريخٌ لا يُمحى): جولةُ مجلسٍ واحدةٌ بعدَ E1 وG1 وتحليلِ D-4/المستدعين وتصميمِ WI-116 (§ 2)
الحالة: IN_REVIEW   (قيدُ W-701 — IN_PROGRESS→IN_REVIEW بأمرِ المالكِ في التوجيهِ 25 § 1: «جولة المجلس تُطلَق الآن ولا تنتظر G1: E1 اكتمل 14/14» · الشِّفرةُ نُفِّذَت كاملةً: W-696 (أسطحُ executive_core الستةُ · D-4 135←129) + W-699 (أسطحُ agent_runtime الثمانيةُ · D-4 129←121 · السياديّةُ 51←59 · القبولُ الكاملُ 14/14) + W-700 (تصويبُ CI) · قيسَ المالكُ بنفسِهِ (التوجيهُ 25 § 0): D-4 = 121 — وقالَ حرفيًّا عن الباقي: «الباقي من تقريرك الأخير غير مقيس عندي» · بانتظارِ جولةِ المجلسِ المأمورةِ الآنَ · والسابقُ (تاريخٌ لا يُمحى): W-697 صَحَّحَ حُمرةَ CI الأولى على PR #167: قياساتٌ متقادمةٌ وفحوصُ حوكمةٍ حُدِّثت بالمقيسِ (الجردُ 235 · الدَّينُ 129 = 11+34+84 · المُصرِّحُونَ 11 · حزمةُ الخدماتِ 1620) · والشِّفرةُ نُفِّذَت في W-696 — أسطحُ executive_core الستةُ تعبرُ بالقاموسِ الموسَّعِ (13 اسمًا باعتمادِ Q-73) · قياسُ القبولِ: D-4 135←129 (−6 أسطحٍ) والسياديّةُ 46←51 · فحوصُ الأصنافِ الخمسةِ (14 فحصًا) خضراءُ · المتبقّي: أسطحُ agent_runtime الثمانيةُ (W-697) ثمَّ جولةُ المجلسِ · والسابقُ (تاريخٌ لا يُمحى): قيدُ W-695 — انتقلَ RESERVED→IN_PROGRESS بدفعةٍ ورقيّةٍ تسبقُ دفعةَ الشِّفرةِ مباشرةً · سابقةُ W-688 · إجراءُ DISC-137 · التصميمُ مودَعٌ في W-694)
المسارات: docs/audit/E1_EXECUTIVE_IDENTITY_CROSSING_DESIGN.md · docs/audit/evidence/W-693 · docs/audit/evidence/W-695 · docs/audit/evidence/W-696 · docs/audit/evidence/W-697 · docs/audit/evidence/W-698 · docs/audit/evidence/W-699 · core/constitutional_engine/rules.py · federal/executive/services/src/amos_federation/services/agent_runtime · federal/executive/services/src/amos_federation/services/executive_core · federal/executive/services/tests/test_executive_core.py · federal/executive/services/tests/test_e1_executive_identity_crossing.py
بدأ: 2026-10-26 · الأفق: 2026-11-22

السبب: نصُّ التوجيهِ 24 § 2: «E1 (14 سطحًا مباشرة تحت D-4): تصميم يعرض نموذج الصلاحيات، ثم الشفرة. هذا حرق حقيقي» + صفُّ E1 من خطةِ حرقِ D-4 (نمطُ WI-082 وطفرتُهُ)

فكُّ تقاطعِ المطالباتِ (§ 6.1): مسارُ `agent_identity.py` نُقِلَ من WI-082 (VERIFIED) إلى WI-119 بقيدِ W-693 — سابقةُ نقلِ ملفَّي الفحصِ من WI-097 إلى WI-117 في W-687

خارج النطاق (منعٌ صريح): K1 (الصفّانِ 24–25) لا يُمَسُّ · لا تعديلَ لمعجمِ الدستورِ ولا لـKILL_SWITCH_BLOCKS في دفعةِ التصميمِ · لا مساسَ بـpersistent.py ولا بتعريفِ D-4 ولا بمعيارِ WI-115 (4)

معيار القبول: قياسُ sovereign_write_inventory.py بعدَ دفعةِ الشِّفرةِ (خطُّ الأساسِ 135 مقيسًا ومودَعًا في evidence/W-693 · الإسقاطُ 121 مشروطًا — الفرقُ بينَ الإسقاطِ والقياسِ يُقيَّدُ) + فحوصُ الأصنافِ الخمسةِ خضراءُ وطفرةٌ لكلِّ سطحٍ — **قُيسَ في W-696**: الدَّينُ 135←129 (−6 أسطحِ executive_core · الحمولتانِ في evidence/W-693 وevidence/W-696) والسياديّةُ 46←51 معَ قيدِ انحرافِ القياسِ على engine.submit (حارسُهُ قائمٌ والأداةُ لم تعد ترى كتابتَهُ الخامَّ في `_create_core`) · أسطحُ agent_runtime الثمانيةُ تُقاسُ في W-697

الدليل المطلوب: وثيقةُ التصميمِ (مودَعةٌ في W-694 · evidence/W-693 لخطِّ الأساسِ) · الحمولاتُ الخامُّ للقياسِ قبلَ وبعدَ · فحوصُ الأصنافِ الخمسةِ والطفراتُ في دفعةِ الشِّفرةِ
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ: قياسُ sovereign_write_inventory.py بعدَ دفعةِ الشِّفرةِ (خطُّ الأساسِ 135 مقيسًا · الإسقاطُ 121) + فحوصُ الأصنافِ الخمسةِ خضراءُ وطفرةٌ لكلِّ سطحٍ — **قِسْهُ بنفسِكَ**: الدَّينُ 121 والسياديّةُ 59.

**إفصاحاتُ المنسِّقِ (تُحكَمُ لا تُسلَّمُ):** (1) الشِّفرةُ في التزامَينِ: `153109cf` (W-696 · أسطحُ executive_core الستةُ) و`5f644d88` (W-699 · أسطحُ agent_runtime الثمانيةُ · مفتاحُ § 2.4 بمعاملِ operation_id باعتمادِ Q-74) — والأمرانِ 5 و6 يُريانِكَ إحصاءَيهما. (2) **القبولُ:** الدَّينُ 121 (الأمرُ 9) والسياديّةُ 59 — قِسْهما أنتَ خامًا؛ الإسقاطُ تحقَّقَ كاملًا (135←129←121) والسياديّةُ 46←51←59. (3) **الطفراتُ وتغطيةُ الأسطحِ الـ14:** سجلُّ محرّكِ طفراتِ المنفِّذِ (15 حالةً) ليسَ من حدودِ قراءتِكَ — أعِدِ الطفرةَ بنفسِكَ: الأمرُ 11 يُنشئُ شجرةَ عملٍ عندَ ما قبلَ W-699 وينسخُ فحوصَهُ إليها (يُتوقَّعُ سقوطُها لأنَّ العبورَ لم يكنْ — واحكمْ هل السقوطُ على تأكيدِ الدليلِ لا على خطأِ استيرادٍ) — ولمجرّكَ أن تُسقِطَ حارسَ سطحٍ واحدٍ في شجرتِكَ وتُشغِّلَ فحوصَه. **وتحقَّقْ من التغطيةِ**: فحوصُ الأمرينِ 7 و8 (الأصنافُ الخمسةُ) يجبُ أن تُغطّيَ كلَّ سطحٍ من الـ14 (6 executive_core + 8 agent_runtime) — عُدَّ الأسطحَ المغطّاةَ في تشغيلِكَ وأعلِنْ أيَّ سطحٍ بلا فحصٍ. (4) سجلُّ قراراتِ المالكِ: Q-73 (اعتمادُ تصميمِ E1) وQ-74 (معاملُ operation_id) — الأمرُ 12. (5) **حدودُ العزلِ المعلَنةُ:** المقاعدُ الثلاثةُ تعملُ في صندوقٍ واحدٍ مشتركٍ بجذورٍ منفصلةٍ (`/home/user/workspace/council_w701/<مقعد>/`) — لا تقرأْ ولا تكتبْ خارجَ جذرِكَ، ولا تقرأْ نسخةَ المنسِّقِ (`/home/user/workspace/amos`) ولا أدلّةَ المنفِّذِ (`docs/audit/evidence/W-68*`/`W-69*`/`W-70*` عدا هذه الإحاطةِ).

### ج · أوامرُ المعاييرِ

1. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi119/`
2. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/briefs_wi119/)`
3. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && git rev-parse HEAD`
4. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && git log --format='%h %cI %s' -- federal/executive/services/src/amos_federation/services/agent_runtime federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py federal/executive/services/tests/test_e1_executive_identity_crossing.py federal/executive/services/tests/test_w699_agent_runtime_crossing.py`
5. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && git show --stat 153109cf`
6. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && git show --stat 5f644d88`
7. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_e1_executive_identity_crossing.py`
8. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w699_agent_runtime_crossing.py`
9. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py`
10. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --json`
11. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && rm -rf ../old && git worktree add --detach ../old 5f644d88^ && cp federal/executive/services/tests/test_w699_agent_runtime_crossing.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/grok_4_7/wi119/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w699_agent_runtime_crossing.py`
12. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && rg -n "Q-73|Q-74" docs/audit/SOVEREIGN_DECISION_REGISTER.md`
13. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && sha256sum docs/audit/evidence/W-701/briefs_wi119/briefing_grok_4_7.md`
14. `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && cat docs/audit/evidence/W-701/briefs_wi119/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- الشِّفرةُ والفحوصُ والوثائقُ التي تُسمّيها أوامرُ (ج) في استنساخِكَ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w701/grok_4_7/wi119/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **مسارًا إنتاجيًّا واحدًا على الأقلِّ من الأسطحِ الـ14** (مثلًا `population.register_agent` أو `health.run_health_check`) من خارجِ العبورِ النشطِ ويُثبِتُ أنَّ الكتابةَ تُصرَّحُ وتُوثَّقُ بأثرِها (المفتاحُ `agent:<id>/lifecycle.<prev>-><target>@<operation_id>` أو نحوَهُ من تصميمِ E1) وأنَّ استدعاءً ثانيًا بنفسِ المفتاحِ لا يُنشئُ عبورًا معشّقًا (قارنْ بسلوكِ الكاشفِ WI-115). احفظْهُ في دليلِكَ تحتَ `/home/user/workspace/council_w701/grok_4_7/wi119/probe/`، واعرضْ شِفرتَهُ بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْهُ بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ أثبتَ كتابةً بلا أثرٍ أو تعشيشًا ملاحظةٌ حاجبةٌ.
7. بعدَ كتابةِ حكمِكَ شغِّلِ الفاحصَ عليه: `cd /home/user/workspace/council_w701/grok_4_7/wi119/repo && .venv/bin/python tools/governance/council_verdict_raw_check.py --brief docs/audit/evidence/W-701/briefs_wi119/briefing_grok_4_7.md --repo . /home/user/workspace/council_w701/grok_4_7/wi119/VERDICT.md` وألصقْ مخرجَه ورمزَ خروجِه في ردِّكَ (لا في VERDICT.md).

### و · صيغةُ جوابِكَ (يُكتَبُ في `/home/user/workspace/council_w701/grok_4_7/wi119/VERDICT.md` ويُحفظُ حرفيًّا بلا تحريرٍ)
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
