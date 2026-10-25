# إحاطةُ جولةِ مراجعةِ البندِ: WI-113 (تصحيحُ قياسٍ A1(هـ): أداةُ الجردِ تفهرسُ بالاسمِ المؤهَّلِ) — مقعدُ grok_4_7
> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.

> **بنودٌ مساعدةٌ (ملزمةٌ):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** gemini_3_8_flash · grok_4_7 · kimi_k3 — والمنسِّقُ عندَ الإطلاقِ **Claude Opus 5.5** (لا مقعدَ من عائلةِ Claude) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w673/grok_4_7/wi113` (§ 2.6).
> **سندُ الجولةِ (التوجيهُ 23 § 2):** «WI-113 وWI-115: أدخلهما IN_REVIEW وأطلق لهما جولة مجلس تُجمَع في الجلسة نفسها (Q-72).»
> **تُبصَمُ sha256 في قيدِ W-673 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-673/briefs_wi113/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w673/grok_4_7/wi113/repo`، وأعدَّ بيئتَه بـ`tools/dev/bootstrap.sh` داخلَه، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ في W-673 — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

| WI-113 | tooling-gates | T0 (**تصحيحُ قياسٍ** لا حرقٌ — A1(هـ) بقرارِ المالكِ في التوجيهِ 22 § 1: «(هـ) تصحيح أداة الجرد» · و§ 2: «بند صغير مستقل. سيخفض D-4 بسبعة قياسًا لا حرقًا؛ سجِّله «تصحيح قياس» تحت عنوان منفصل ولا تحتسبه في منحنى الحرق») | Perplexity Computer | مجلسُ المراجعةِ (بروتوكولُ المجلسِ) — ولا VERIFIED بيدِ المنفِّذِ | IN_REVIEW | tools/audit/sovereign_write_inventory.py · tests/governance/test_wi113_inventory_qualified_index.py · docs/audit/evidence/W-666 · docs/audit/evidence/W-669 | 2026-10-25 | 2026-11-22 | لا عائقَ — A1(هـ) محسومٌ | جولةُ مجلسٍ (W-673 · ثلاثةُ مقاعدَ · تُجمَعُ في الجلسةِ نفسِها — Q-72) | — (يُكتَبُ عندَ الإغلاقِ) |

كتلةُ البندِ (كما هي عندَ كتابةِ هذهِ الإحاطةِ):

```text
المعرِّف: WI-113
النطاق: T0 (tooling-gates · tools/audit/sovereign_write_inventory.py وفحصُه — لا مساسَ بشِفرةِ الإنتاجِ)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · بتوجيهِ المستشارِ 22 § 2)
المراجع: مجلسُ المراجعةِ (بروتوكولُ المجلسِ) — ولا VERIFIED بيدِ المنفِّذِ
الحالة: IN_REVIEW   (قيدُ W-673 · IN_PROGRESS→IN_REVIEW بأمرِ التوجيهِ 23 § 2: «WI-113 وWI-115: أدخلهما IN_REVIEW وأطلق لهما جولة مجلس تُجمَع في الجلسة نفسها (Q-72)» — الشِّفرةُ في W-669 · وإحاطاتُ الجولةِ مبصومةٌ في evidence/W-673/briefs_wi113 · ولا VERIFIED بيدِ المنفِّذِ · والسابقُ: W-668 IN_PROGRESS · W-666 RESERVED · W-663 READY)
المسارات: tools/audit/sovereign_write_inventory.py · tests/governance/test_wi113_inventory_qualified_index.py · docs/audit/evidence/W-666 · docs/audit/evidence/W-669 · ولقطاتُ القياسِ المحروسةُ تحتَ docs/audit/measurements/ تُعادُ إن لزمَ (سابقةُ W-531) · ومجلَّداتُ أدلّةِ قيودِه تُضافُ عندَ حجزِه
بدأ: 2026-10-25 · الأفق: 2026-11-22

السبب: A1 § 1.3 قاسَ أنَّ الجردَ يحتسبُ 7 قراءاتٍ في common/persistent.py مواقعَ كتابةٍ لأنَّ `synthesize_public_sites` يفهرسُ النداءاتِ بالاسمِ المجرَّدِ (`get` وأخواتُها) — والمالكُ أمرَ: «سجِّله «تصحيح قياس» تحت عنوان منفصل ولا تحتسبه في منحنى الحرق».

خارج النطاق: أيُّ عبورٍ أو تعديلٍ في persistent.py أو مستدعيه · تخفيفُ أيِّ بوّابةٍ أو عتبةٍ · احتسابُ الفرقِ حرقًا · (ج) و(د) من A1 (للمالكِ سؤالينِ منفصلينِ)

معيار القبول: (1) الفهرسةُ بالاسمِ المؤهَّلِ `Class.method` لا بالاسمِ المجرَّدِ ولا بآخرِ صنفٍ (2) فحصٌ يُثبِتُ أنَّ القراءاتِ السبعَ (A1 § 1.3) لا تُحتسَبُ وأنَّ الكتابةَ الحقيقيّةَ (:932 بذرٌ كسولٌ) تبقى محتسَبةً (3) طفرةُ إرجاعِ الفهرسةِ بالاسمِ المجرَّدِ يكتشفُها الفحصُ (4) D-4 قبلُ وبعدُ خامًا بأمرٍ — والفرقُ يُسجَّلُ «تصحيحَ قياسٍ» تحتَ عنوانٍ منفصلٍ لا حرقًا

الدليل المطلوب: الفرقُ · الفحصُ قبلُ (يسقطُ) وبعدُ (ينجحُ) · سجلُّ الطفرةِ · مخرجُ `decision_gate.py --measure` قبلُ وبعدُ خامًا
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ: (1) الفهرسةُ بالاسمِ المؤهَّلِ `Class.method` لا بالاسمِ المجرَّدِ ولا بآخرِ صنفٍ (2) فحصٌ يُثبِتُ أنَّ القراءاتِ السبعَ (A1 § 1.3) لا تُحتسَبُ وأنَّ الكتابةَ الحقيقيّةَ (بذرٌ كسولٌ) تبقى محتسَبةً (3) طفرةُ إرجاعِ الفهرسةِ بالاسمِ المجرَّدِ يكتشفُها الفحصُ (4) D-4 قبلُ وبعدُ خامًا بأمرٍ — والفرقُ يُسجَّلُ «تصحيحَ قياسٍ» تحتَ عنوانٍ منفصلٍ لا حرقًا.

**إفصاحاتُ المنسِّقِ (تُحكَمُ لا تُسلَّمُ):** (1) الشِّفرةُ في التزامِ `6605fa88e1823cb4450c0762acb7cfe5e89c8ca7` (قيدُ W-669) — والأمرانِ 6 و7 يُريانِكَ الفرقَ والفحصَ. (2) **المعيارُ (3) طفرةٌ:** سجلُّ طفراتِ المنفِّذِ ليسَ من حدودِ قراءتِكَ — أعِدِ الطفرةَ بنفسِكَ: الأمرُ 10 يُرجِعُ الأداةَ إلى ما قبلَ W-669 في شجرةِ عملٍ منفصلةٍ ويُشغِّلُ الفحصَ نفسَه عليها (يُتوقَّعُ سقوطُه) — احكمْ أنتَ هل سقوطُه دلاليٌّ أم خطأُ واجهةٍ (أفصحَ المنفِّذُ أنَّ الفحصَ على الأداةِ القديمةِ يسقطُ بخطأِ واجهةٍ لا بالتأكيد، وأنَّ السقوطَ الدلاليَّ تُثبِتُه طفرتُه M1 — فهذه دعوى تُحكَمُ لا تُسلَّم). (3) **المعيارُ (4):** D-4 = 142 قبلُ (الأمرُ 11 على الشجرةِ القديمةِ) و135 بعدُ (الأمرُ 8) بحسبِ المنفِّذِ — قِسْهما أنتَ. والفرقُ «تصحيحُ قياسٍ» لا حرقٌ بنصِّ التوجيهِ 22 § 2. (4) **حدٌّ مُعلَنٌ:** المُستقبِلُ غيرُ `self`/`cls` (`obj.x()`) يبقى محلولًا إلى كلِّ تعريفٍ بالاسمِ، و`attribute_helper_writes` لم يُمَسّ — هل أحدُهما يُبطِلُ المعيارَ (1)؟ احكمْ. (5) **حدودُ العزلِ المعلَنةُ:** المقاعدُ الثلاثةُ تعملُ في صندوقٍ واحدٍ مشتركٍ بجذورٍ منفصلةٍ (`/home/user/workspace/council_w673/<مقعد>/`) — لا تقرأْ ولا تكتبْ خارجَ جذرِكَ، ولا تقرأْ نسخةَ المنسِّقِ (`/home/user/workspace/amos`) ولا أدلّةَ المنفِّذِ (`docs/audit/evidence/W-66*`/`W-67*` عدا هذه الإحاطةِ).

### ج · أوامرُ المعاييرِ

1. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/`
2. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-673/briefs_wi113/)`
3. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git rev-parse HEAD`
4. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git log --format='%h %cI %s' -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py`
5. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git show --stat 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7`
6. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && git diff 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7 -- tools/audit/sovereign_write_inventory.py tests/governance/test_wi113_inventory_qualified_index.py`
7. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py`
8. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python tools/audit/decision_gate.py --measure`
9. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py`
10. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && rm -rf ../old && git worktree add --detach ../old 6605fa88e1823cb4450c0762acb7cfe5e89c8ca7^ && cp tests/governance/test_wi113_inventory_qualified_index.py ../old/tests/governance/ && cd ../old && /home/user/workspace/council_w673/grok_4_7/wi113/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/governance/test_wi113_inventory_qualified_index.py`
11. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo/../old && /home/user/workspace/council_w673/grok_4_7/wi113/repo/.venv/bin/python tools/audit/decision_gate.py --measure`
12. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && nl -ba federal/executive/services/src/amos_federation/common/persistent.py | sed -n '880,960p'`
13. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && rg -n 'WI-113|A1\(هـ\)|تصحيح قياس' docs/audit/SOVEREIGN_DECISION_REGISTER.md`
14. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && sha256sum docs/audit/evidence/W-673/briefs_wi113/briefing_grok_4_7.md`
15. `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && cat docs/audit/evidence/W-673/briefs_wi113/SHA256SUMS`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- الشِّفرةُ والفحوصُ والوثائقُ التي تُسمّيها أوامرُ (ج) في استنساخِكَ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w673/grok_4_7/wi113/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من الفحصِ القائمِ — يُنادي **الأداةَ نفسَها** (`tools/audit/sovereign_write_inventory.py` — `synthesize_public_sites` أو الجردَ كلَّه على شجرةٍ مصطنعةٍ في دليلِكَ) ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** (مثلًا: صنفانِ يعرِّفانِ الاسمَ نفسَه أحدُهما يكتبُ والآخرُ يقرأُ — هل تُنسَبُ كتابةٌ للقارئِ؟ · `self.x()` في صنفٍ وارثٍ · كتابةٌ حقيقيّةٌ تسقطُ من العدِّ بعدَ الإصلاحِ = كسرٌ أخطرُ من بقاءِ قراءةٍ). احفظْه في دليلِكَ تحتَ `/home/user/workspace/council_w673/grok_4_7/wi113/probe/`، واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.
7. بعدَ كتابةِ حكمِكَ شغِّلِ الفاحصَ عليه: `cd /home/user/workspace/council_w673/grok_4_7/wi113/repo && .venv/bin/python tools/governance/council_verdict_raw_check.py --brief docs/audit/evidence/W-673/briefs_wi113/briefing_grok_4_7.md --repo . /home/user/workspace/council_w673/grok_4_7/wi113/VERDICT.md` وألصقْ مخرجَه ورمزَ خروجِه في ردِّكَ (لا في VERDICT.md).

### و · صيغةُ جوابِكَ (يُكتَبُ في `/home/user/workspace/council_w673/grok_4_7/wi113/VERDICT.md` ويُحفظُ حرفيًّا بلا تحريرٍ)
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
