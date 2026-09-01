#!/usr/bin/env python3
"""دعاوى الطفرةِ المُعلَنةُ — مصدرُ حقيقةٍ واحدٌ لكلِّ «حرسٌ مُثبَتٌ بطفرةٍ» (W-062).

الهدف:
    أن تكونَ كلُّ دعوى «هذا الحرسُ يسقُطُ عندَ عودةِ العَطبِ» **مُعلَنةً في مِلَفٍّ
    واحدٍ قابلٍ للتشغيلِ**، لا مكتوبةً في خليّةِ سجلٍّ يقرؤها إنسانٌ ويصدِّقُها.
    فالدعوى هنا صيغةٌ تنفيذيّةٌ: أيُّ عَطبٍ يُعادُ · وأيُّ فحوصٍ تُشغَّلُ · وكم
    فحصًا يجبُ أن يسقُطَ. ومن ادَّعى ولم يُسجِّلْ هنا، دعواهُ غيرُ مقيسةٍ.
النطاق:
    بياناتٌ فقط: لا شبكةَ ولا قاعدةَ بياناتٍ ولا سرَّ ولا كتابةَ ملفٍّ. والتشغيلُ
    في `tools/governance/mutation_probe.py`، وحرسُ الاثنَينِ في
    `tests/governance/test_w062_mutation_probe.py`.
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-29
تاريخ آخر تعديل: 2026-09-01 (W-093 — الدعوى تُقرأُ بإعلانٍ صريحٍ · `DISC-033`)

الحدُّ المُعلَنُ — لا مطويٌّ:
    هذا المِلَفُّ **لا يُثبِتُ أنَّ كلَّ دعوى حرسٍ في المستودعِ مُجرَّبةٌ**؛ يُثبِتُ
    أنَّ الدعاوى **المُسجَّلةَ فيه** مُجرَّبةٌ بأمرٍ يُعادُ.
    والمُسجَّلُ اليومَ ستّةُ قيودٍ: `W-055` · `W-056` · `W-059` · `W-061` · `W-062` · `W-063`
    (وفيها دعوى هذا المِلَفِّ نفسِه: من يحرسُ السجلَّ سؤالٌ مُجابٌ برقمٍ لا بثقةٍ).
    **والباقي غيرُ مُسجَّلٍ ومُسمّى لا مسكوتٌ عنه**: `W-029` · `W-030` · `W-051` ·
    `W-052` · `W-053` · `W-054` · `W-057` · `W-058` · `W-060` — وقِيدَ أنَّ
    `W-029` و`W-030` كشفَهما حرسُ هذا القيدِ لا ذاكرةُ كاتبِه (كانا خارجَ
    القائمةِ الأولى فأسقطَ الفحصُ الدعوى) — دعاويها قِيسَت بيدٍ في قيودِها ولم
    تُصِرْ بعدُ أمرًا يُعادُ، وذاك نقصٌ **مُعلَنٌ** يُسَدُّ قيدًا بعدَ قيدٍ، لا
    صمتٌ يُقرأُ اكتمالًا. وقائمةُ الباقي محروسةٌ في
    `tests/governance/test_w063_registered_claims.py` فلا تُقرأُ اكتمالًا بالنسيانِ.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

#: رأسُ صفِّ قيدٍ في § 8 — المعرِّفُ في أوّلِ خليّةٍ.
_ROW_HEAD_RE = re.compile(r"\|\s*(W-\d{3})\s*\|")

#: أقلُّ ما يجوزُ أن تُسقِطَهُ طفرةٌ حتى تُقبَلَ دعوى الحرسِ.
MINIMUM_FAILURES = 1

#: العبارةُ المحجوزةُ التي **يُعلِنُ** بها صفُّ سجلٍّ أنَّه يَدَّعي قياسَ مِسبارٍ.
#:
#: قِيدَ في `DISC-033` أنَّ قراءةَ الدعوى بجذرِ كلمةٍ سالبةٌ لا موجبةٌ: الجذرُ
#: مشتركٌ بينَ العَطبِ المُعادِ في المِسبارِ وبينَ القفزِ، فأحمَرَّ الحرسُ على
#: صفٍّ صادقٍ وقيَّدَ لغةَ السجلِّ بكلمةٍ. فصارَ الإعلانُ **صريحًا**: من ادَّعى
#: قياسًا بالمِسبارِ كتبَ هذه العبارةَ، ومن لم يكتُبْها لم يَدَّعِ — فتُقرأُ
#: الدعوى بقصدِ كاتبِها لا بصرفِ لفظٍ.
CLAIM_MARKER = "دعوى مِسبارٍ مُعلَنةٌ"

#: الصفوفُ التي أصابَتها قراءةُ الجذرِ قبلَ `W-093` — **مُجمَّدةٌ كما قِيسَت**.
#:
#: التاريخُ لا يُعادُ كتابتُه: هذه الصفوفُ كُتِبَت قبلَ أن تُحجَزَ عبارةٌ، فلا
#: تُصاغُ من جديدٍ لِتُوافِقَ قارئًا جديدًا. وكلُّ معرِّفٍ هنا **يجبُ أن يبقى
#: مُعلَنَ الحالةِ** — مُسجَّلًا في `CLAIMS` أو مُسمًّى في `UNREGISTERED_WORK` —
#: وذاك محروسٌ في `tests/governance/test_w063_registered_claims.py`.
LEGACY_CLAIM_ROWS: frozenset[str] = frozenset(
    #: مكتوبةٌ في سطرٍ واحدٍ بقصدٍ: صيغةُ السطرِ الواحدِ لكلِّ معرِّفٍ تُطابِقُ نصَّ
    #: طفرةٍ مُسجَّلةٍ في `W-063` فتصيرُ دعوى بلا موضِعٍ واحدٍ — قِيسَ ذلك فسقَطَ الفحصُ.
    "W-029 W-030 W-052 W-053 W-055 W-056 W-057 W-058 W-059 W-060 W-061 W-062"
    " W-063".split()
)

#: قيودٌ دعاويها مكتوبةٌ في السجلِّ ولم تُسجَّلْ هنا بعدُ — نقصٌ مُعلَنٌ يُقاسُ.
UNREGISTERED_WORK: tuple[str, ...] = (
    "W-029",
    "W-030",
    "W-051",
    "W-052",
    "W-053",
    "W-054",
    "W-057",
    "W-058",
    "W-060",
)


@dataclass(frozen=True)
class Mutation:
    """عَطبٌ يُعادُ نصًّا، وعددُ الفحوصِ الذي يجبُ أن يسقُطَ عندَه."""

    kind: str
    target: str
    old: str
    new: str
    expected_failures: int
    note: str = ""


@dataclass(frozen=True)
class Claim:
    """دعوى حرسٍ واحدةٌ: قيدُها · فحوصُها · وطفراتُها."""

    work: str
    item: str
    tests: tuple[str, ...]
    mutations: tuple[Mutation, ...] = field(default_factory=tuple)


#: دعوى `W-061`: حرسُ اتِّجاهِ دَينِ الأسطحِ. الأرقامُ مقيسةٌ لا مُقدَّرةٌ.
W061 = Claim(
    work="W-061",
    item="WI-016",
    tests=("tests/governance/test_w061_surface_debt_trend.py",),
    mutations=(
        Mutation(
            kind="RISE_NEVER_FIRES",
            target="tools/governance/surface_debt_trend.py",
            old="if delta > 0:",
            new="if delta > 999:",
            expected_failures=2,
            note="شرطُ الصعودِ يُعطَّلُ فلا يُشعِلُ صعودٌ.",
        ),
        Mutation(
            kind="BLIND_COUNT",
            target="tools/governance/surface_debt_trend.py",
            old="return int(summary[TOTAL_KEY]), int(summary[DEBT_KEY])",
            new="return 0, 0",
            expected_failures=5,
            note="العدُّ يُصفَّرُ فيصيرُ كلُّ فارقٍ صِفرًا.",
        ),
        Mutation(
            kind="INVERTED_PUBLISHED",
            target="tools/governance/surface_debt_trend.py",
            old="elif declared != newest_point.debt_sites:",
            new="elif declared == newest_point.debt_sites:",
            expected_failures=2,
            note="فحصُ مطابقةِ الحِملِ المنشورِ يُقلَبُ.",
        ),
        Mutation(
            kind="LAST_COMMIT_NOT_FIRST",
            target="tools/governance/surface_debt_trend.py",
            old="return commits[0]",
            new="return commits[-1]",
            expected_failures=1,
            note="القيدُ يُنسَبُ إلى آخرِ من مسَّ معرِّفَه لا أوّلِ من أدخلَه.",
        ),
        Mutation(
            kind="NO_MINIMUM_POINTS",
            target="tools/governance/surface_debt_trend.py",
            old="if count < 2:",
            new="if count < 0:",
            expected_failures=1,
            note="حدُّ النقطتَينِ يُلغى فيُدَّعى اتِّجاهٌ بنقطةٍ.",
        ),
        Mutation(
            kind="SWALLOW_GIT_FAILURE",
            target="tools/governance/surface_debt_trend.py",
            old="if done.returncode != 0:",
            new="if False:",
            expected_failures=1,
            note="فشلُ `git` يُبتلَعُ فيُقرأَ «لا صفَّ في التاريخِ».",
        ),
        Mutation(
            kind="WRITES_INTO_TREE",
            target="tools/governance/surface_debt_trend.py",
            old="def measure(root: Path | None = None, entries: int = 2) -> Report:",
            new=(
                "def measure(root: Path | None = None, entries: int = 2) -> Report:\n"
                '    (Path(root or Path.cwd()) / "_probe.txt").write_text('
                '"x", encoding="utf-8")'
            ),
            expected_failures=1,
            note="الأداةُ تكتبُ سطرًا في الشجرةِ التي تحكمُ عليها.",
        ),
    ),
)

#: دعوى `W-062`: المِسبارُ يُجرِّبُ نفسَه — من يحرسُ الحارسَ.
W062 = Claim(
    work="W-062",
    item="WI-017",
    tests=("tests/governance/test_w062_mutation_probe.py",),
    mutations=(
        Mutation(
            kind="SURVIVAL_READ_AS_CATCH",
            target="tools/governance/mutation_probe.py",
            old="if observed < minimum:",
            new="if False:",
            expected_failures=2,
            note="نجاةُ الطفرةِ تُقرأُ التقاطًا فلا تُعلَنُ مخالفةً.",
        ),
        Mutation(
            kind="COUNT_MISMATCH_IGNORED",
            target="tools/governance/mutation_probe.py",
            old="elif observed != mutation.expected_failures:",
            new="elif False:",
            expected_failures=3,
            note="رقمٌ مُعلَنٌ مخالفٌ للمقيسِ يمرُّ صامتًا.",
        ),
        Mutation(
            kind="STALE_CLAIM_SKIPPED",
            target="tools/governance/mutation_probe.py",
            old="if occurrences != 1:",
            new="if occurrences > 99:",
            expected_failures=3,
            note="دعوى صارَ نصُّها غيرَ موجودٍ أو مُبهَمًا تُتجاهَلُ.",
        ),
        Mutation(
            kind="RED_BASELINE_ACCEPTED",
            target="tools/governance/mutation_probe.py",
            old="if baseline_failed:",
            new="if False:",
            expected_failures=2,
            note="يُقاسُ الالتقاطُ على قاعدةٍ ساقطةٍ أصلًا.",
        ),
        Mutation(
            kind="TREE_WRITE_UNCHECKED",
            target="tools/governance/mutation_probe.py",
            old="if git_status(root) != before:",
            new="if False:",
            expected_failures=2,
            note="كتابةُ المِسبارِ في الشجرةِ الحاكمةِ لا تُعلَنُ.",
        ),
        Mutation(
            kind="NO_RESTORE_BETWEEN_MUTATIONS",
            target="tools/governance/mutation_probe.py",
            old='                    target.write_text(pristine, encoding="utf-8")',
            new="                    pass",
            expected_failures=1,
            note="لا تُستعادُ الشجرةُ بينَ طفرتَينِ فتُقاسُ الثانيةُ على الأولى.",
        ),
        Mutation(
            kind="UNREADABLE_OUTPUT_AS_ZERO",
            target="tools/governance/mutation_probe.py",
            old='        raise ProbeRefused(\n            "PYTEST_OUTPUT_UNREADABLE"',
            new='        return (0, 0)\n        raise ProbeRefused(\n            "PYTEST_OUTPUT_UNREADABLE"',
            expected_failures=1,
            note="خلاصةٌ لا تُقرأُ تُقرأُ صِفرَ سقوطٍ.",
        ),
        Mutation(
            kind="UNREGISTERED_WORK_SILENT",
            target="tools/governance/mutation_probe.py",
            old='        raise ProbeRefused("WORK_NOT_REGISTERED", str(exc)) from exc',
            new="        return ()",
            expected_failures=2,
            note="قيدٌ غيرُ مُسجَّلٍ يُقرأُ «لا شيءَ لِيُقاسَ».",
        ),
    ),
)

#: دعوى `W-055`: حرسُ افتراقِ جردِ المخطَّطِ. أرقامُها المنشورةُ في القيدِ 1·1·4·1.
W055 = Claim(
    work="W-055",
    item="WI-010",
    tests=("tests/governance/test_w055_schema_inventory_drift.py",),
    mutations=(
        Mutation(
            kind="SUM_CHECK_DISABLED",
            target="tools/governance/schema_inventory_drift.py",
            old="if declared.breakdown_total and declared.breakdown_total != declared.breakdown_sum:",
            new="if False:",
            expected_failures=1,
            note="فحصُ مطابقةِ المجموعِ لتفصيلِه يُعطَّلُ.",
        ),
        Mutation(
            kind="REFUSAL_CODE_FLIPPED",
            target="tools/governance/schema_inventory_drift.py",
            old="return 2",
            new="return 1",
            expected_failures=1,
            note="رمزُ الرفضِ المُصنَّفِ يصيرُ رمزَ مخالفةٍ فيُقرأُ الرفضُ حكمًا.",
        ),
        Mutation(
            kind="DRIFT_READ_AS_MATCH",
            target="tools/governance/schema_inventory_drift.py",
            old='return self.state != "MATCH"',
            new="return False",
            expected_failures=4,
            note="الافتراقُ يُقرأُ مطابقةً فلا يُشعِلُ.",
        ),
        Mutation(
            kind="FUTURE_DATE_UNCHECKED",
            target="tools/governance/schema_inventory_drift.py",
            old="if declared.measured_on > today:",
            new="if False:",
            expected_failures=1,
            note="قياسٌ مؤرَّخٌ في المستقبلِ يُقبَلُ حاصلًا.",
        ),
    ),
)


#: دعوى `W-056`: حرسُ حالةِ القراراتِ السياديّةِ. أرقامُها المنشورةُ 2·1·2·4·1·1·1.
W056 = Claim(
    work="W-056",
    item="WI-011",
    tests=("tests/governance/test_w056_sovereign_decision_status.py",),
    mutations=(
        Mutation(
            kind="EXPIRY_UNDETECTED",
            target="tools/governance/sovereign_decision_status.py",
            old="if basis and state != basis:",
            new="if False:",
            expected_failures=2,
            note="انقضاءُ سندِ وضعِ الإبلاغِ لا يُرصَدُ.",
        ),
        Mutation(
            kind="REFUSAL_CODE_FLIPPED",
            target="tools/governance/sovereign_decision_status.py",
            old="return 2",
            new="return 1",
            expected_failures=1,
            note="رمزُ الرفضِ 2 يصيرُ 1.",
        ),
        Mutation(
            kind="SELF_COUNTED",
            target="tools/governance/sovereign_decision_status.py",
            old="""    "tools/governance/sovereign_decision_status.py",
    "tests/governance/test_w056_sovereign_decision_status.py",""",
            new='    "tools/governance/__never_excluded__.py",',
            expected_failures=1,
            note=(
                "الأداةُ تعُدُّ إشاراتِ نفسِها فتُنفِّخُ الرقمَ الذي تقيسُه. "
                "وقيدُ `W-056` نشرَ «فحصانِ» والمقيسُ اليومَ **فحصٌ واحدٌ** "
                "بالطفرتَينِ المُجرَّبتَينِ (استثناءُ الأداةِ وحدَها · واستثناؤها "
                "مع فحصِها) — والرقمُ هنا مقيسٌ لا منقولٌ، والفرقُ مقيَّدٌ في "
                "`DISC-022` ولم يُوسَّعْ حرسٌ ولا خُفِّفَ حدٌّ لتسويتِه."
            ),
        ),
        Mutation(
            kind="PENDING_NOT_BLOCKING",
            target="tools/governance/sovereign_decision_status.py",
            old='BLOCKING_STATUSES = frozenset({"PENDING", "DEFERRED"})',
            new="BLOCKING_STATUSES = frozenset()",
            expected_failures=4,
            note="«المعلَّقُ ليس حاجبًا» فيُقرأُ الحجبُ طريقًا.",
        ),
        Mutation(
            kind="EMPTY_TABLE_ACCEPTED",
            target="tools/governance/sovereign_decision_status.py",
            old="    if not out:",
            new="    if False:",
            expected_failures=1,
            note="جدولٌ لا يُقرَأُ فيه صفٌّ يُقالُ عنه «لا مخالفة».",
        ),
        Mutation(
            kind="UNREADABLE_SWALLOWED",
            target="tools/governance/sovereign_decision_status.py",
            old="    if unreadable:",
            new="    if False:",
            expected_failures=1,
            note="ملفٌّ لم يُقرَأْ يُبتلَعُ فيُقرأُ النقصُ اكتمالًا.",
        ),
        Mutation(
            kind="WORK_REGISTER_ASSUMED_READ",
            target="tools/governance/sovereign_decision_status.py",
            old="    if not work_read:",
            new="    if False:",
            expected_failures=1,
            note="غيابُ سجلِّ العملِ يُقرأُ صفرًا مقيسًا.",
        ),
    ),
)


#: دعوى `W-059`: حرسُ إرساءِ القيودِ المفتوحةِ. أرقامُها **لم تُنشَرْ** في قيدِها،
#: فقِيسَت هنا بالمِسبارِ وسُجِّلَت بالمقيسِ لا بالمُقدَّرِ.
W059 = Claim(
    work="W-059",
    item="WI-014",
    tests=("tests/governance/test_w059_open_record_accountability.py",),
    mutations=(
        Mutation(
            kind="DIACRITIC_RANGE_TOO_WIDE",
            target="tools/governance/open_record_accountability.py",
            old="[*range(0x064B, 0x0653), 0x0640, 0x0670, 0x06D6, 0x0653, 0x0654, 0x0655]",
            new="[*range(0x0600, 0x0700)]",
            expected_failures=11,
            note="مدًى واسعٌ لنزعِ التشكيلِ يبتلعُ الأبجديّةَ فيُقرأُ المُعالَجُ مفتوحًا.",
        ),
        Mutation(
            kind="ANCHOR_FROM_WHOLE_ROW",
            target="tools/governance/open_record_accountability.py",
            old='anchor_text = f"{cells[6]} {cells[7]}"',
            new='anchor_text = " ".join(cells)',
            expected_failures=1,
            note="المِرساةُ تُقرأُ من الصفِّ كلِّهِ فيصيرُ موضِعُ العَطبِ حرسَه.",
        ),
    ),
)

#: دعوى `W-063`: حرسُ صدقِ هذا السجلِّ نفسِه — من يحرسُ السجلَّ سؤالٌ يُجابُ برقمٍ.
W063 = Claim(
    work="W-063",
    item="WI-018",
    tests=("tests/governance/test_w063_registered_claims.py",),
    mutations=(
        Mutation(
            kind="GAP_LIST_SHRUNK",
            target="tools/governance/mutation_claims.py",
            old='    "W-030",\n',
            new="",
            expected_failures=2,
            note="قيدٌ يدَّعي طفرةً يُحذَفُ من قائمةِ النقصِ فيُقرأُ صمتُه اكتمالًا.",
        ),
        Mutation(
            kind="NUMBER_NOT_MEASURED",
            target="tools/governance/mutation_claims.py",
            old="            expected_failures=1,\n            note=(\n",
            new="            expected_failures=2,\n            note=(\n",
            expected_failures=2,
            note="رقمٌ منشورٌ يُعادُ نقلُه مكانَ المقيسِ فيصيرُ السجلُّ ناقلًا لا قائسًا.",
        ),
        Mutation(
            kind="ITEM_ID_INVENTED",
            target="tools/governance/mutation_claims.py",
            old='    work="W-059",\n    item="WI-014",',
            new='    work="W-059",\n    item="WI-999",',
            expected_failures=2,
            note="دعوى تُنسَبُ إلى بندٍ لا وجودَ له في سجلِّ العملِ.",
        ),
    ),
)


#: كلُّ الدعاوى المُسجَّلةِ — بالترتيبِ الذي سُجِّلَت به.
CLAIMS: tuple[Claim, ...] = (W055, W056, W059, W061, W062, W063)


def claims_for(work: str | None = None) -> tuple[Claim, ...]:
    """الدعاوى كلُّها، أو دعوى قيدٍ بعينِه — ولا يُخترَعُ قيدٌ غيرُ مُسجَّلٍ."""
    if work is None:
        return CLAIMS
    picked = tuple(claim for claim in CLAIMS if claim.work == work)
    if not picked:
        known = " · ".join(claim.work for claim in CLAIMS)
        raise KeyError(f"لا دعوى مُسجَّلةً للقيدِ «{work}» — المُسجَّلُ: {known}")
    return picked


def rows_claiming_a_probe(ledger_text: str) -> set[str]:
    """معرِّفاتُ صفوفِ § 8 التي **تُعلِنُ** أنَّها تَدَّعي قياسًا بالمِسبارِ.

    القراءةُ في طريقَينِ مُعلَنَينِ لا في جذرِ كلمةٍ (`DISC-033`):
      * صفٌّ يحملُ `CLAIM_MARKER` — إعلانٌ صريحٌ من كاتبِ الصفِّ.
      * صفٌّ معرِّفُه في `LEGACY_CLAIM_ROWS` — ما قرأَهُ الجذرُ قبلَ حجزِ العبارةِ،
        مُجمَّدًا كما قِيسَ لأنَّ التاريخَ لا يُعادُ كتابتُه.

    الحدُّ المُعلَنُ: صفٌّ يَدَّعي قياسًا بلغةٍ أخرى ولا يحملُ العبارةَ **لا يراهُ
    هذا القارئُ** — وهو حدُّ كلِّ قائمةٍ مكتوبةٍ في الشِفرةِ، لا سكوتٌ مطويٌّ.

    Args:
        ledger_text: نصُّ `docs/audit/COMPLETION_LEDGER.md` كما هو.

    Returns:
        مجموعةُ معرِّفاتِ القيودِ المُدَّعيةِ التي **لها صفٌّ** في النصِّ المقروءِ.
    """
    claiming: set[str] = set()
    for line in ledger_text.splitlines():
        head = _ROW_HEAD_RE.match(line)
        if head is None:
            continue
        work = head.group(1)
        if CLAIM_MARKER in line or work in LEGACY_CLAIM_ROWS:
            claiming.add(work)
    return claiming
