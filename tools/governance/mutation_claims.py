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
تاريخ آخر تعديل: 2026-08-29

الحدُّ المُعلَنُ — لا مطويٌّ:
    هذا المِلَفُّ **لا يُثبِتُ أنَّ كلَّ دعوى حرسٍ في المستودعِ مُجرَّبةٌ**؛ يُثبِتُ
    أنَّ الدعاوى **المُسجَّلةَ فيه** مُجرَّبةٌ بأمرٍ يُعادُ. والدعاوى المكتوبةُ في
    قيودٍ سابقةٍ (`W-060` وما قبلَه) قِيسَت بيدٍ ولم تُسجَّلْ هنا بعدُ — وذاك
    نقصٌ **مُعلَنٌ** يُسَدُّ قيدًا بعدَ قيدٍ، لا صمتٌ يُقرأُ اكتمالًا.
"""

from __future__ import annotations

from dataclasses import dataclass, field

#: أقلُّ ما يجوزُ أن تُسقِطَهُ طفرةٌ حتى تُقبَلَ دعوى الحرسِ.
MINIMUM_FAILURES = 1


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


#: كلُّ الدعاوى المُسجَّلةِ — بالترتيبِ الذي سُجِّلَت به.
CLAIMS: tuple[Claim, ...] = (W061, W062)


def claims_for(work: str | None = None) -> tuple[Claim, ...]:
    """الدعاوى كلُّها، أو دعوى قيدٍ بعينِه — ولا يُخترَعُ قيدٌ غيرُ مُسجَّلٍ."""
    if work is None:
        return CLAIMS
    picked = tuple(claim for claim in CLAIMS if claim.work == work)
    if not picked:
        known = " · ".join(claim.work for claim in CLAIMS)
        raise KeyError(f"لا دعوى مُسجَّلةً للقيدِ «{work}» — المُسجَّلُ: {known}")
    return picked
