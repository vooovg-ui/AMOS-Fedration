#!/usr/bin/env python3
"""حرسُ سجلِّ دعاوى الطفرةِ: ما سُجِّلَ مقيسٌ، وما لم يُسجَّلْ مُسمّى (W-063).

الهدف:
    أن يبقى مِلَفُّ `tools/governance/mutation_claims.py` **صادقًا في طرفَيه**:
    الأرقامُ المُسجَّلةُ هي المقيسةُ بالمِسبارِ لا المنقولةُ من نصٍّ، وقائمةُ
    القيودِ التي لم تُسجَّلْ بعدُ **مُعلَنةٌ ومحروسةٌ** فلا يُقرأُ نقصُها
    اكتمالًا يومَ يَنسى كاتبٌ أن يُنقِصَها أو يزيدَها.
النطاق:
    قراءةُ بياناتٍ فقط: لا تشغيلَ طفرةٍ ولا `git` ولا شبكةَ ولا كتابةَ ملفٍّ —
    فتشغيلُ الطفراتِ نفسُه في `tools/governance/mutation_probe.py`.
المالك: tests/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-29
تاريخ آخر تعديل: 2026-09-01 (W-093 — الدعوى تُقرأُ بإعلانٍ صريحٍ · `DISC-033`)

الحدُّ المُعلَنُ — لا مطويٌّ:
    هذا الملفُّ **لا يُثبِتُ أنَّ الطفرةَ تُمسَكُ**؛ المِسبارُ وحدَه يُثبِتُ ذلك
    بتشغيلٍ. وهذا يُثبِتُ أنَّ السجلَّ لا يكذِبُ على قارئِه: لا قيدَ يُذكَرُ
    مُسجَّلًا وغيرَ مُسجَّلٍ في وقتٍ واحدٍ، ولا رقمَ يُدَّعى بلا موضِعٍ في الشجرةِ.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
CLAIMS_SOURCE = ROOT / "tools" / "governance" / "mutation_claims.py"
LEDGER = ROOT / "docs" / "audit" / "COMPLETION_LEDGER.md"
ACTIVE_WORK = ROOT / "docs" / "governance" / "work" / "ACTIVE_WORK.md"


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


claims = _load(CLAIMS_SOURCE, "mutation_claims_w063")


#: ما قِيسَ بالمِسبارِ في `W-063` لهذه القيودِ الثلاثةِ — مقيسٌ لا مُقدَّرٌ.
MEASURED = {
    "W-055": {
        "SUM_CHECK_DISABLED": 1,
        "REFUSAL_CODE_FLIPPED": 1,
        "DRIFT_READ_AS_MATCH": 4,
        "FUTURE_DATE_UNCHECKED": 1,
    },
    "W-056": {
        "EXPIRY_UNDETECTED": 2,
        "REFUSAL_CODE_FLIPPED": 1,
        "SELF_COUNTED": 1,
        "PENDING_NOT_BLOCKING": 4,
        "EMPTY_TABLE_ACCEPTED": 1,
        "UNREADABLE_SWALLOWED": 1,
        "WORK_REGISTER_ASSUMED_READ": 1,
    },
    "W-059": {
        "DIACRITIC_RANGE_TOO_WIDE": 11,
        "ANCHOR_FROM_WHOLE_ROW": 1,
    },
    "W-063": {
        "GAP_LIST_SHRUNK": 2,
        "NUMBER_NOT_MEASURED": 2,
        "ITEM_ID_INVENTED": 2,
    },
}


def test_the_new_claims_are_registered_with_their_measured_numbers():
    """`W-055` و`W-056` و`W-059` و`W-063` مُسجَّلةٌ بأرقامِ المِسبارِ لا بأرقامِ النصِّ."""
    for work, expected in MEASURED.items():
        (claim,) = claims.claims_for(work)
        declared = {m.kind: m.expected_failures for m in claim.mutations}
        assert declared == expected, work


def test_items_match_the_work_register():
    """كلُّ دعوى تُنسَبُ إلى بندٍ **موجودٍ** في سجلِّ العملِ لا إلى معرِّفٍ مُخترَعٍ."""
    register = ACTIVE_WORK.read_text(encoding="utf-8")
    known = set(re.findall(r"\bWI-\d{3}\b", register))
    assert known, "سجلُّ العملِ لا يُقرَأُ فيه بندٌ"
    for claim in claims.CLAIMS:
        assert claim.item in known, f"{claim.work}: {claim.item}"


def test_unregistered_list_and_registered_list_never_overlap():
    """لا قيدَ يُقالُ عنه مُسجَّلٌ وغيرُ مُسجَّلٍ في وقتٍ واحدٍ."""
    registered = {claim.work for claim in claims.CLAIMS}
    remaining = set(claims.UNREGISTERED_WORK)
    assert not (registered & remaining), sorted(registered & remaining)


def test_declared_gap_covers_every_ledger_entry_that_claims_a_mutation():
    """كلُّ قيدٍ **مُدَّعٍ** في السجلِّ: إمّا مُسجَّلٌ هنا وإمّا مُسمّى في النقصِ.

    هذا هو الحرسُ الذي يمنعُ قراءةَ النقصِ اكتمالًا: يومَ يُقيَّدُ قيدٌ جديدٌ
    يُعلِنُ دعوى مِسبارٍ ولا يُسجِّلُها ولا يُعلِنُها ناقصةً، يسقُطُ هذا الفحصُ.

    وقراءةُ «مَن هو المُدَّعي» صارت في `mutation_claims.rows_claiming_a_probe`
    بإعلانٍ صريحٍ لا بجذرِ كلمةٍ (`DISC-033` · `W-093`).
    """
    text = LEDGER.read_text(encoding="utf-8")
    claiming = claims.rows_claiming_a_probe(text)
    assert claiming, "لا قيدَ مُدَّعٍ يُقرَأُ — القياسُ لم يقرأِ السجلَّ"
    accounted = {c.work for c in claims.CLAIMS} | set(claims.UNREGISTERED_WORK)
    unaccounted = sorted(work for work in claiming if work not in accounted)
    assert not unaccounted, f"قيودٌ مُدَّعيةٌ ولا تُعلَنُ حالتُها: {unaccounted}"


def test_every_registered_mutation_still_has_one_place_in_the_tree():
    """نصُّ كلِّ طفرةٍ موجودٌ مرّةً واحدةً في هدفِه — دعوى بلا موضِعٍ غيرُ مُجرَّبةٍ."""
    for claim in claims.CLAIMS:
        for mutation in claim.mutations:
            target = ROOT / mutation.target
            assert target.is_file(), f"{claim.work}: {mutation.target}"
            found = target.read_text(encoding="utf-8").count(mutation.old)
            assert found == 1, f"{claim.work} · {mutation.kind}: وُجِدَ {found}"


def test_no_mutation_targets_a_test_file():
    """الطفرةُ تُعادُ في **الحرسِ المقيسِ** لا في الفحصِ الذي يقيسُه.

    فمن طفَرَ الفحصَ ليُسقِطَه أثبتَ أنَّ الفحصَ يسقُطُ بنفسِه لا أنَّ الحرسَ يعَضُّ.
    """
    for claim in claims.CLAIMS:
        for mutation in claim.mutations:
            assert not mutation.target.startswith("tests/"), (
                f"{claim.work} · {mutation.kind}: هدفُ الطفرةِ فحصٌ لا حرسٌ"
            )


@pytest.mark.parametrize("work", sorted(MEASURED))
def test_each_new_claim_names_its_own_living_test_file(work):
    """كلُّ دعوى تُشغِّلُ فحوصَ قيدِها الموجودةَ في الشجرةِ لا فحوصًا مُتخيَّلةً."""
    (claim,) = claims.claims_for(work)
    assert claim.tests, work
    for relative in claim.tests:
        assert (ROOT / relative).is_file(), relative


# ——— قراءةُ الدعوى: إعلانٌ صريحٌ لا جذرُ كلمةٍ (`DISC-033` · W-093) ———


def _row(work: str, body: str) -> str:
    """صفُّ § 8 مُصطَنَعٌ — يُقاسُ عليه القارئُ بلا مسِّ السجلِّ الحقيقيِّ."""
    return f"| {work} | 2026-09-01 | خطوة | {body} | بقي | دليل |\n"


def test_the_reserved_phrase_marks_a_claim():
    assert claims.rows_claiming_a_probe(
        _row("W-500", f"هذا القيدُ فيه {claims.CLAIM_MARKER} بأرقامٍ مقيسةٍ")
    ) == {"W-500"}


def test_a_word_root_alone_is_not_a_claim():
    """شكلُ `DISC-033` بعينِه: لفظُ القفزِ في عبارةِ حالةٍ لا يُقرَأُ دعوى."""
    text = _row("W-501", "§ 4.3 لا يُجيزُ الطفرَ من IN_REVIEW إلى CLOSED")
    text += _row("W-502", "ولا الوثبَ ولا التحوّرَ في حالةِ بندٍ")
    assert claims.rows_claiming_a_probe(text) == set()


def test_prose_outside_a_row_is_not_a_claim():
    assert claims.rows_claiming_a_probe(
        f"نصٌّ حرٌّ يذكرُ W-503 و{claims.CLAIM_MARKER} في فقرةٍ لا في صفٍّ.\n"
    ) == set()


def test_legacy_rows_are_still_read_as_claims():
    """ما قرأَهُ الجذرُ قبلَ حجزِ العبارةِ مُجمَّدٌ: لا يُفلِتُ بصياغةٍ جديدةٍ."""
    legacy = sorted(claims.LEGACY_CLAIM_ROWS)[0]
    assert claims.rows_claiming_a_probe(_row(legacy, "بلا لفظٍ ولا عبارةٍ")) == {legacy}


def test_legacy_roster_is_not_empty_and_is_frozen():
    assert len(claims.LEGACY_CLAIM_ROWS) == 13
    assert isinstance(claims.LEGACY_CLAIM_ROWS, frozenset)


def test_every_legacy_row_still_has_a_row_in_the_ledger():
    """معرِّفٌ مُجمَّدٌ بلا صفٍّ في § 8 دعوى بلا موضِعٍ — يُسقِطُ."""
    text = LEDGER.read_text(encoding="utf-8")
    present = set(re.findall(r"\|\s*(W-\d{3})\s*\|", text))
    missing = sorted(claims.LEGACY_CLAIM_ROWS - present)
    assert not missing, missing


def test_every_legacy_row_declares_its_state():
    accounted = {c.work for c in claims.CLAIMS} | set(claims.UNREGISTERED_WORK)
    assert not sorted(claims.LEGACY_CLAIM_ROWS - accounted)


def test_a_new_declared_claim_that_is_not_accounted_would_fail_the_guard():
    """الحرسُ ما زالَ يعَضُّ: صفٌّ يُعلِنُ دعوى ولا يُعلِنُ حالتَه غيرُ محسوبٍ."""
    claiming = claims.rows_claiming_a_probe(
        _row("W-504", f"{claims.CLAIM_MARKER} بلا تسجيلٍ ولا إعلانِ نقصٍ")
    )
    accounted = {c.work for c in claims.CLAIMS} | set(claims.UNREGISTERED_WORK)
    assert sorted(work for work in claiming if work not in accounted) == ["W-504"]


def test_the_real_ledger_has_no_unaccounted_declared_claim():
    text = LEDGER.read_text(encoding="utf-8")
    accounted = {c.work for c in claims.CLAIMS} | set(claims.UNREGISTERED_WORK)
    assert sorted(claims.rows_claiming_a_probe(text) - accounted) == []


def test_reading_the_ledger_writes_nothing():
    before = LEDGER.read_bytes()
    claims.rows_claiming_a_probe(before.decode("utf-8"))
    assert LEDGER.read_bytes() == before
