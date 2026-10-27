# -*- coding: utf-8 -*-
"""مولّد إحاطات جولة W-701 — ثلاثة بنود × ثلاثة مقاعد (توجيه المستشار 25 § 1).

الهدف:
    توليدُ إحاطاتِ جولةِ مجلسِ المراجعةِ التسعِ (3 بنودٍ × 3 مقاعدٍ) من صفوفِ وكتلِ
    ACTIVE_WORK.md كما هي عندَ الكتابةِ، وبصماتُها في SHA256SUMS لكلِّ مجلَّدِ إحاطاتٍ.
    المالك: Perplexity Computer (المنسِّقُ GLM-5.3) · تاريخُ الإنشاءِ: 2026-10-27 (قيدُ W-701).
"""

import io
import os
import re
import subprocess  # SHA256SUMS per briefs dir

REPO = "/home/user/workspace/amos"
EVID = os.path.join(REPO, "docs/audit/evidence/W-701")
SEATS = ["gemini_3_8_flash", "grok_4_7", "kimi_k3"]

aw = io.open(
    os.path.join(REPO, "docs/governance/work/ACTIVE_WORK.md"), encoding="utf-8"
).read()


def row_of(wi):
    for line in aw.splitlines():
        if line.startswith("| %s |" % wi):
            return line
    raise KeyError(wi)


def block_of(wi):
    m = re.search(r"```text\nالمعرِّف: %s\n(.*?)```" % wi, aw, re.S)
    if not m:
        m = re.search(r"```\nالمعرِّف: %s\n(.*?)```" % wi, aw, re.S)
    return "المعرِّف: %s\n%s" % (wi, m.group(1))


SANDAD_25 = "«جولة المجلس تُطلَق الآن ولا تنتظر G1: E1 اكتمل 14/14، فلا موجب للتأجيل. تشمل WI-117 وWI-119 وما صار منفَّذًا من WI-115 (الكاشف)، وتُجمَع أحكامها في الجلسة نفسها (Q-72) بمسبار لكل مقعد وأدلة منفصلة.»"

HEAD = """# إحاطةُ جولةِ مراجعةِ البندِ: {TITLE} — مقعدُ {SEAT}
> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.

> **بنودٌ مساعدةٌ (ملزمةٌ):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** gemini_3_8_flash · grok_4_7 · kimi_k3 — والمنسِّقُ عندَ الإطلاقِ **GLM-5.3** (لا مقعدَ من عائلةِ GLM) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w701/{SEAT}/{WIDIR}` (§ 2.6).
> **سندُ الجولةِ (توجيهُ المستشارِ 25 § 1 · قرارُ المالكِ D27):** {SANDAD}
> **هذه جولةٌ واحدةٌ** بثلاثةِ نطاقاتٍ (WI-117 · WI-119 · الكاشفُ المنفَّذُ من WI-115) تُجمَعُ أحكامُها في الجلسةِ نفسِها — وهذه إحاطةُ نطاقِكَ فيها لا جولةً مستقلةً (تسلسلُ الجولاتِ § 8 بندُ 5 محفوظٌ: جولةٌ واحدةٌ في آنٍ واحدٍ).
> **تُبصَمُ sha256 في قيدِ W-701 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-701/{BRIEFDIR}/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-701/{BRIEFDIR}/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2).
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w701/{SEAT}/{WIDIR}/repo`، وأعدَّ بيئتَه بـ`tools/dev/bootstrap.sh` داخلَه، واعملْ داخلَ جذرِكَ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذهِ الإحاطةِ في W-701 — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

{ROW}

كتلةُ البندِ (كما هي عندَ كتابةِ هذهِ الإحاطةِ):

```text
{BLOCK}
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ: {CRITERIA}

**إفصاحاتُ المنسِّقِ (تُحكَمُ لا تُسلَّمُ):** {DISCLOSURES}

### ج · أوامرُ المعاييرِ

{COMMANDS}

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- الشِّفرةُ والفحوصُ والوثائقُ التي تُسمّيها أوامرُ (ج) في استنساخِكَ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out /home/user/workspace/council_w701/{SEAT}/{WIDIR}/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** {PROBE}
7. بعدَ كتابةِ حكمِكَ شغِّلِ الفاحصَ عليه: `cd /home/user/workspace/council_w701/{SEAT}/{WIDIR}/repo && .venv/bin/python tools/governance/council_verdict_raw_check.py --brief docs/audit/evidence/W-701/{BRIEFDIR}/briefing_{SEAT}.md --repo . /home/user/workspace/council_w701/{SEAT}/{WIDIR}/VERDICT.md` وألصقْ مخرجَه ورمزَ خروجِه في ردِّكَ (لا في VERDICT.md).

### و · صيغةُ جوابِكَ (يُكتَبُ في `/home/user/workspace/council_w701/{SEAT}/{WIDIR}/VERDICT.md` ويُحفظُ حرفيًّا بلا تحريرٍ)
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
"""

ISOLATION = (
    "(5) **حدودُ العزلِ المعلَنةُ:** المقاعدُ الثلاثةُ تعملُ في صندوقٍ واحدٍ مشتركٍ بجذورٍ منفصلةٍ "
    "(`/home/user/workspace/council_w701/<مقعد>/`) — لا تقرأْ ولا تكتبْ خارجَ جذرِكَ، ولا تقرأْ نسخةَ المنسِّقِ "
    "(`/home/user/workspace/amos`) ولا أدلّةَ المنفِّذِ (`docs/audit/evidence/W-68*`/`W-69*`/`W-70*` عدا هذه الإحاطةِ)."
)


def cmds_wi117(seat, w):
    P = "/home/user/workspace/council_w701/%s/wi117/repo" % seat
    return "\n".join(
        [
            "1. `cd %s && git log -1 --format=%%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/`"
            % P,
            "2. `cd %s && git checkout $(git log -1 --format=%%H origin/main -- docs/audit/evidence/W-701/briefs_wi117/)`"
            % P,
            "3. `cd %s && git rev-parse HEAD`" % P,
            "4. `cd %s && git log --format='%%h %%cI %%s' -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py`"
            % P,
            "5. `cd %s && git show --stat f8d33807`" % P,
            "6. `cd %s && git diff f8d33807^ f8d33807 -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py federal/executive/services/tests/test_wi117_king_guard_routes.py`"
            % P,
            '7. `cd %s && rg -n "require_king" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py`'
            % P,
            "8. `cd %s && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py`"
            % P,
            "9. `cd %s && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_governance.py federal/executive/services/tests/test_control_console.py`"
            % P,
            "10. `cd %s && rm -rf ../old && git worktree add --detach ../old f8d33807^ && cp federal/executive/services/tests/test_wi117_king_guard_routes.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/%s/wi117/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py`"
            % (P, seat),
            '11. `cd %s && sed -i "s/Depends(require_king)/Depends(require_auth)/g" federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi117_king_guard_routes.py`'
            % P,
            "12. `cd %s && git checkout -- federal/executive/services/src/amos_federation/services/governance/main.py federal/executive/services/src/amos_federation/services/control_console/main.py && git status --short && git diff --stat`"
            % P,
            '13. `cd %s && rg -n "D25-2|require_king" docs/audit/SOVEREIGN_DECISION_REGISTER.md`'
            % P,
            "14. `cd %s && sha256sum docs/audit/evidence/W-701/briefs_wi117/briefing_%s.md`"
            % (P, seat),
            "15. `cd %s && cat docs/audit/evidence/W-701/briefs_wi117/SHA256SUMS`" % P,
        ]
    )


def cmds_wi119(seat, item_key=None):
    P = "/home/user/workspace/council_w701/%s/wi119/repo" % seat
    return "\n".join(
        [
            "1. `cd %s && git log -1 --format=%%H origin/main -- docs/audit/evidence/W-701/briefs_wi119/`"
            % P,
            "2. `cd %s && git checkout $(git log -1 --format=%%H origin/main -- docs/audit/evidence/W-701/briefs_wi119/)`"
            % P,
            "3. `cd %s && git rev-parse HEAD`" % P,
            "4. `cd %s && git log --format='%%h %%cI %%s' -- federal/executive/services/src/amos_federation/services/agent_runtime federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py federal/executive/services/tests/test_e1_executive_identity_crossing.py federal/executive/services/tests/test_w699_agent_runtime_crossing.py`"
            % P,
            "5. `cd %s && git show --stat 153109cf`" % P,
            "6. `cd %s && git show --stat 5f644d88`" % P,
            "7. `cd %s && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_e1_executive_identity_crossing.py`"
            % P,
            "8. `cd %s && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w699_agent_runtime_crossing.py`"
            % P,
            "9. `cd %s && .venv/bin/python tools/audit/sovereign_write_inventory.py`"
            % P,
            "10. `cd %s && .venv/bin/python tools/audit/sovereign_write_inventory.py --json`"
            % P,
            "11. `cd %s && rm -rf ../old && git worktree add --detach ../old 5f644d88^ && cp federal/executive/services/tests/test_w699_agent_runtime_crossing.py ../old/federal/executive/services/tests/ && cd ../old && /home/user/workspace/council_w701/%s/wi119/repo/.venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_w699_agent_runtime_crossing.py`"
            % (P, seat),
            '12. `cd %s && rg -n "Q-73|Q-74" docs/audit/SOVEREIGN_DECISION_REGISTER.md`'
            % P,
            "13. `cd %s && sha256sum docs/audit/evidence/W-701/briefs_wi119/briefing_%s.md`"
            % (P, seat),
            "14. `cd %s && cat docs/audit/evidence/W-701/briefs_wi119/SHA256SUMS`" % P,
        ]
    )


def cmds_wi115(seat, item_key=None):
    P = "/home/user/workspace/council_w701/%s/wi115/repo" % seat
    return "\n".join(
        [
            "1. `cd %s && git log -1 --format=%%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/`"
            % P,
            "2. `cd %s && git checkout $(git log -1 --format=%%H origin/main -- docs/audit/evidence/W-701/briefs_wi115/)`"
            % P,
            "3. `cd %s && git rev-parse HEAD`" % P,
            "4. `cd %s && git log --format='%%h %%cI %%s' -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py`"
            % P,
            "5. `cd %s && git show --stat 2b814b34`" % P,
            "6. `cd %s && git diff 2b814b34^ 2b814b34 -- core/sovereignty/enforcement_boundary.py tests/sovereignty/test_wi115_nesting_detector.py`"
            % P,
            "7. `cd %s && .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py`"
            % P,
            "8. `cd %s && .venv/bin/python -m pytest -q -p no:cacheprovider federal/executive/services/tests/test_wi115_reversed_replay.py federal/executive/services/tests/test_wi115_nesting_compensator_frame.py`"
            % P,
            '9. `cd %s && rg -n "NESTED_SOVEREIGN_EXEMPTIONS|NestedSovereignCallError|open_case" core/sovereignty/enforcement_boundary.py`'
            % P,
            "10. `cd %s && rm -rf ../old && git worktree add --detach ../old 2b814b34^ && cp tests/sovereignty/test_wi115_nesting_detector.py ../old/tests/sovereignty/ && cd ../old && /home/user/workspace/council_w701/%s/wi115/repo/.venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_wi115_nesting_detector.py`"
            % (P, seat),
            "11. `cd %s && sha256sum docs/audit/evidence/W-701/briefs_wi115/briefing_%s.md`"
            % (P, seat),
            "12. `cd %s && cat docs/audit/evidence/W-701/briefs_wi115/SHA256SUMS`" % P,
        ]
    )


ITEMS = {
    "wi117": dict(
        TITLE="WI-117 (تحصينُ مساراتِ الخفضِ وإنشاءِ الترقيةِ وفحصِ البوّابةِ بـrequire_king — D25-2)",
        WIDIR="wi117",
        BRIEFDIR="briefs_wi117",
        CRITERIA="(1) `POST /v1/system/kill-switch/reset` (governance) و`POST /v1/kill-switch/reset` (control_console) و`POST /v1/promotions` و`POST /v1/promotions/{id}/gates` محروسةٌ بـ`require_king` (2) مسبارٌ يشغّلُ طلبَ HTTP حقيقيًّا برمزِ مواطنٍ على كلٍّ منها ويُثبِتُ الرفضَ (403) وأنَّ المستوى لم يتغيّرْ — مخرجٌ حرفيٌّ (3) رمزُ الملكِ يمرُّ (4) مطفرةٌ تُسقِطُ القيدَ عن كلِّ مسارٍ فيكتشفُها فحصٌ (5) الفحوصُ الستُّ التي تمرُّ اليومَ برمزِ مواطنٍ تُحدَّثُ إلى رمزِ ملكٍ بلا إضعافِ ما تفحصُه (6) مسبارٌ لكلِّ مقعدٍ.",
        DISCLOSURES=(
            "(1) الشِّفرةُ في التزامِ `f8d33807` (قيدُ W-689) — والأمرانِ 6 و7 يُريانِكَ الفرقَ والحُرّاسَ. "
            "(2) **المعيارُ (4) طفرةٌ:** سجلُّ طفراتِ المنفِّذِ ليسَ من حدودِ قراءتِكَ — أعِدِ الطفرةَ بنفسِكَ: **خطُّ الأساسِ أولًا** (الأمرُ 8 أخضرُ) ثمَّ الأمرُ 11 يُسقِطُ الحرسَ كلَّهُ (المعاملُ `Depends(require_king)` في توقيعِ كلِّ مسارٍ — لا ديكوريتور) من الملفَّينِ معًا ويُشغِّلُ الفحصَ نفسَه (يُتوقَّعُ سقوطُه على تأكيدِ الحارسِ لا على خطأِ واجهةٍ — احكمْ من مخرجِ pytest أيُّ الفحوصِ سقطت ولماذا) ثمَّ الأمرُ 12 يسترجعُ الملفَّينِ ويُثبِتُ نظافةَ الشجرةِ. ولمجرّكَ في مسبارِكَ (السؤالُ 6) أن يُسقِطَ حارسَ مسارٍ واحدٍ وحدَه من الأربعةِ ويُشغِّلَ الفحوصَ — كلُّ مسارٍ على حدةٍ. والأمرُ 10 (فحوصٌ جديدةٌ على شجرةٍ قديمةٍ) دليلُ تاريخٍ مكمِّلٌ لا كافٍ وحدَه: إن كانَ سقوطُه بخطأِ استيرادٍ لا بتأكيدٍ دلاليٍّ فلا يُثبِتُ المعيارَ وحدَه. "
            "(3) **المعيارُ (2) مسبارُ HTTP:** مسبارُ المنفِّذِ الخامُّ ليسَ من حدودِ قراءتِكَ — **مسبارُكَ الخاصُّ (السؤالُ 6) هو الدليلُ**: شغِّلِ الخدمةَ عبرَ uvicorn برمزِ مواطنٍ (`role=citizen`) واطلبِ المساراتِ الأربعةَ — الرفضُ 403 دونَ تغييرِ المستوى، وبرمزِ الملكِ تمرُّ (المعيارُ 3). "
            "(4) **فحوصُ § 2 (المعيارُ 5):** الأمرُ 9 يُشغِّلُ حزمتَي الحوكمةِ والوحدةِ الكاملتَينِ — عُدَّ الفحوصَ التي تمرُّ برمزِ ملكٍ. "
        )
        + ISOLATION,
        PROBE=(
            "اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُشغِّلُ **طلبَ HTTP حقيقيًّا** عبرَ uvicorn (أو ما يصلُهُ من الشفرةِ الإنتاجيّةِ) برمزِ مواطنٍ على المساراتِ الأربعةِ المحروسةِ ويُثبِتُ الرفضَ (403) وعدمَ تغييرِ المستوى، ثمَّ يُثبِتُ المرورَ برمزِ الملكِ. احفظْه في دليلِكَ تحتَ `/home/user/workspace/council_w701/{SEAT}/wi117/probe/`، واعرضْ شِفرتَهُ بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْهُ بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ أثبتَ مرورًا برمزِ مواطنٍ ملاحظةٌ حاجبةٌ."
        ),
    ),
    "wi119": dict(
        TITLE="WI-119 (عبورُ الأسطحِ الـ14 المباشرةِ تحتَ D-4 للحدِّ السياديِّ — E1 · حرقٌ حقيقيٌّ)",
        WIDIR="wi119",
        BRIEFDIR="briefs_wi119",
        CRITERIA="قياسُ sovereign_write_inventory.py بعدَ دفعةِ الشِّفرةِ (خطُّ الأساسِ 135 مقيسًا · الإسقاطُ 121) + فحوصُ الأصنافِ الخمسةِ خضراءُ وطفرةٌ لكلِّ سطحٍ — **قِسْهُ بنفسِكَ**: الدَّينُ 121 والسياديّةُ 59.",
        DISCLOSURES=(
            "(1) الشِّفرةُ في التزامَينِ: `153109cf` (W-696 · أسطحُ executive_core الستةُ) و`5f644d88` (W-699 · أسطحُ agent_runtime الثمانيةُ · مفتاحُ § 2.4 بمعاملِ operation_id باعتمادِ Q-74) — والأمرانِ 5 و6 يُريانِكَ إحصاءَيهما. "
            "(2) **القبولُ:** الدَّينُ 121 (الأمرُ 9) والسياديّةُ 59 — قِسْهما أنتَ خامًا؛ الإسقاطُ تحقَّقَ كاملًا (135←129←121) والسياديّةُ 46←51←59. "
            "(3) **الطفراتُ وتغطيةُ الأسطحِ الـ14:** سجلُّ محرّكِ طفراتِ المنفِّذِ (15 حالةً) ليسَ من حدودِ قراءتِكَ — أعِدِ الطفرةَ بنفسِكَ: الأمرُ 11 يُنشئُ شجرةَ عملٍ عندَ ما قبلَ W-699 وينسخُ فحوصَهُ إليها (يُتوقَّعُ سقوطُها لأنَّ العبورَ لم يكنْ — واحكمْ هل السقوطُ على تأكيدِ الدليلِ لا على خطأِ استيرادٍ) — ولمجرّكَ أن تُسقِطَ حارسَ سطحٍ واحدٍ في شجرتِكَ وتُشغِّلَ فحوصَه. **وتحقَّقْ من التغطيةِ**: فحوصُ الأمرينِ 7 و8 (الأصنافُ الخمسةُ) يجبُ أن تُغطّيَ كلَّ سطحٍ من الـ14 (6 executive_core + 8 agent_runtime) — عُدَّ الأسطحَ المغطّاةَ في تشغيلِكَ وأعلِنْ أيَّ سطحٍ بلا فحصٍ. "
            "(4) سجلُّ قراراتِ المالكِ: Q-73 (اعتمادُ تصميمِ E1) وQ-74 (معاملُ operation_id) — الأمرُ 12. "
        )
        + ISOLATION,
        PROBE=(
            "اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **مسارًا إنتاجيًّا واحدًا على الأقلِّ من الأسطحِ الـ14** (مثلًا `population.register_agent` أو `health.run_health_check`) من خارجِ العبورِ النشطِ ويُثبِتُ أنَّ الكتابةَ تُصرَّحُ وتُوثَّقُ بأثرِها (المفتاحُ `agent:<id>/lifecycle.<prev>-><target>@<operation_id>` أو نحوَهُ من تصميمِ E1) وأنَّ استدعاءً ثانيًا بنفسِ المفتاحِ لا يُنشئُ عبورًا معشّقًا (قارنْ بسلوكِ الكاشفِ WI-115). احفظْهُ في دليلِكَ تحتَ `/home/user/workspace/council_w701/{SEAT}/wi119/probe/`، واعرضْ شِفرتَهُ بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْهُ بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ أثبتَ كتابةً بلا أثرٍ أو تعشيشًا ملاحظةٌ حاجبةٌ."
        ),
    ),
    "wi115": dict(
        TITLE="WI-115 (Q-9 · الخيارُ 4): جولةُ الكاشفِ المنفَّذِ وحدَه — النطاقُ المعلَنُ لا البندُ كلُّه",
        WIDIR="wi115",
        BRIEFDIR="briefs_wi115",
        CRITERIA="**نطاقُ هذهِ الجولةِ:** المعيارُ (3) (الكاشفُ يرفضُ عبورًا سياديًّا داخلَ عبورٍ نشطٍ قبلَ decide · وopen_case مستثنًى باسمِه استثناءً مسجَّلًا) وشقُّ الكاشفِ من المعيارِ (5) (طفرةُ حذفِ الكاشفِ تُكتشَفُ) — **فلا VERIFIED للبندِ كلِّهِ بهذهِ الجولةِ** (المعيارُ (4) مؤجَّلٌ بعرضٍ على المالكِ: الاستخراجُ `_disburse_core` يكسرُ حرسَ Q-32 القائمَ مقيسًا).",
        DISCLOSURES=(
            "(1) **حدُّ النطاقِ:** الشِّفرةُ في التزامِ `2b814b34` (قيدُ W-685) للكاشفِ وحدَهُ — والمعيارانِ (1) و(2) وشقُّ § 3.5 من (5) عولجتا في جولةٍ سابقةٍ (W-673/W-683) فليستا من نطاقِ حكمِكَ. "
            "(2) الشِّفرةُ: `NESTED_SOVEREIGN_EXEMPTIONS` بأزواجٍ مُجمَّدةٍ · `NestedSovereignCallError` يُرمى قبلَ أيِّ حارسٍ وأيِّ decide · استثناءُ open_case باسمِه. "
            "(3) **الطفرةُ:** سجلُّ طفراتِ المنفِّذِ ليسَ من حدودِ قراءتِكَ — أعِدِ الطفرةَ بنفسِكَ: الأمرُ 10 (شجرةُ عملٍ عندَ ما قبلَ W-685 + نسخُ فحصِ الكاشفِ — يُتوقَّعُ سقوطُه: احكمْ هل السقوطُ على تأكيدِ الكاشفِ لا على خطأِ استيرادٍ — دليلُ تاريخٍ مكمِّلٌ لا كافٍ وحدَه) — ولمجرّكَ في مسبارِكَ أن تُسقِطَ الكاشفَ في شجرتِكَ وتُشغِّلَ الفحوصَ. "
        )
        + ISOLATION,
        PROBE=(
            "اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **الكاشفَ نفسَهُ** (`core/sovereignty/enforcement_boundary.py`) ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** (مثلًا: استدعاءٌ سياديٌّ داخلَ عبورٍ نشطٍ بفعلٍ غيرُ مستثنًى — هل يُرمى `NestedSovereignCallError`؟ · استدعاءٌ باسمِ open_case داخلَ عبورٍ — هل يمرُّ بالاستثناءِ المسجَّلِ لا بالرفضِ؟ · زوجٌ مجمَّدٌ في `NESTED_SOVEREIGN_EXEMPTIONS` — هل يمرُّ كما هو؟). احفظْهُ في دليلِكَ تحتَ `/home/user/workspace/council_w701/{SEAT}/wi115/probe/`، واعرضْ شِفرتَهُ بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْهُ بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ أثبتَ مرورَ تعشيشٍ غيرُ مستثنًى ملاحظةٌ حاجبةٌ."
        ),
    ),
}

CMD_BUILDERS = {"wi117": cmds_wi117, "wi119": cmds_wi119, "wi115": cmds_wi115}

for item_key, item in ITEMS.items():
    d = os.path.join(EVID, item["BRIEFDIR"])
    os.makedirs(d, exist_ok=True)
    for seat in SEATS:
        body = HEAD.format(
            TITLE=item["TITLE"],
            SEAT=seat,
            WIDIR=item["WIDIR"],
            BRIEFDIR=item["BRIEFDIR"],
            SANDAD=SANDAD_25,
            ROW=row_of("WI-" + item_key[2:]),
            BLOCK=block_of("WI-" + item_key[2:]).rstrip(),
            CRITERIA=item["CRITERIA"],
            DISCLOSURES=item["DISCLOSURES"].replace("{SEAT}", seat),
            COMMANDS=CMD_BUILDERS[item_key](seat, item_key).replace("{SEAT}", seat),
            PROBE=item["PROBE"].replace("{SEAT}", seat),
        )
        fp = os.path.join(d, "briefing_%s.md" % seat)
        io.open(fp, "w", encoding="utf-8").write(body)
        print("written", fp)

for item in ITEMS.values():
    d = os.path.join(EVID, item["BRIEFDIR"])
    out = subprocess.run(
        ["sha256sum"] + ["briefing_%s.md" % s for s in SEATS],
        cwd=d,
        capture_output=True,
        text=True,
    ).stdout
    io.open(os.path.join(d, "SHA256SUMS"), "w", encoding="utf-8").write(out)
    print("sums", item["BRIEFDIR"])
print("ALL DONE")
