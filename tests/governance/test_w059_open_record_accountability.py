#!/usr/bin/env python3
"""حرسُ قياسِ مساءلةِ القيدِ المفتوحِ — يُثبِتُ أنَّ المِرساةَ تُقاسُ لا تُفترَضُ (W-059).

الهدف:
    أن يكونَ معيارُ `open_record_accountability.py` محروسًا لا موصوفًا: كلُّ
    مخالفةٍ تُعلِنُها الأداةُ لها فحصٌ يُثبِتُ **اشتعالَها عندَ سببِها وسكوتَها
    عندَ غيابِه**، وكلُّ رفضٍ مُصنَّفٍ له فحصٌ يُثبِتُ أنَّه رفضٌ لا نتيجةٌ خالية،
    وكلُّ فئةٍ من فئاتِ المِرساةِ لها فحصٌ يُثبِتُ من أيِّ خليّةٍ قُرِئَت.
النطاق:
    شجرةٌ مؤقّتةٌ تُبنى في كلِّ حالةٍ، وفحصٌ واحدٌ يقرأُ المستودعَ الحقيقيَّ
    ليُثبِتَ أنَّ السجلَّينِ الحاضرَينِ يُقرآنِ فعلًا. لا شبكةَ ولا قاعدةَ ولا
    سرَّ ولا كتابةَ في سجلٍّ محكومٍ عليه.
المالك: tests/governance — ديوانُ التدقيق
تاريخ الإنشاء: 2026-08-28
تاريخ آخر تعديل: 2026-08-28
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from datetime import date
from pathlib import Path

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "open_record_accountability.py"


def _load():
    spec = importlib.util.spec_from_file_location("open_record_accountability", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    # لا بدَّ من تسجيلِ الوحدةِ قبلَ تنفيذِها: `dataclass` يقرأُ `sys.modules`.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ORA = _load()

DISC_HEAD = """# سجلُّ الاكتشافات

## 1 · الاكتشافاتُ المُقيَّدة

| المعرِّف | الخطورة | موضعُ الظهور | ما اكتُشِف | الدليل | الأثر | الوجهة | الحالة |
|---|---|---|---|---|---|---|---|
"""

RISK_HEAD = """# سجلُّ المخاطر

## 1 · المخاطرُ المفتوحة

| المعرِّف | الخطر | الاحتمال | الأثر | الإشارةُ المبكِّرةُ | التصرُّف | المالك | المصدر |
|---|---|---|---|---|---|---|---|
"""

#: صفٌّ سليمٌ افتراضًا: اكتشافٌ مفتوحٌ يذكرُ حرسًا قائمًا في وجهتِه.
DISC_ANCHORED = (
    "| DISC-101 | P2 | موضع | ما اكتُشِف | دليل | أثر | "
    "`tools/governance/probe.py` يحرسُه | مفتوحٌ |"
)
#: صفٌّ سليمٌ افتراضًا: خطرٌ إشارتُه مكتوبةٌ وحرسُه مذكورٌ في تصرُّفِه.
RISK_ANCHORED = (
    "| RK-101 | خطرٌ مقيسٌ | مرتفع | أثر | عدَّادٌ يصعدُ | "
    "`tests/governance/test_probe.py` يسقُطُ | مالكُ النطاقِ | قيدُ W-001 |"
)


def _write(root: Path, rel: str, text: str) -> None:
    target = root / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def _tree(
    root: Path,
    *,
    disc_rows: tuple[str, ...] = (DISC_ANCHORED,),
    risk_rows: tuple[str, ...] = (RISK_ANCHORED,),
    guards: tuple[str, ...] = (
        "tools/governance/probe.py",
        "tests/governance/test_probe.py",
    ),
    disc_head: str = DISC_HEAD,
    risk_head: str = RISK_HEAD,
    drop: tuple[str, ...] = (),
) -> None:
    """شجرةٌ صغيرةٌ صالحةٌ افتراضًا، تُعطَبُ في كلِّ فحصٍ من موضعٍ واحدٍ."""
    for guard in guards:
        _write(root, guard, "# حرسٌ قائمٌ في الشجرةِ\n")
    if "DISCOVERIES" not in drop:
        _write(
            root,
            "docs/governance/work/DISCOVERIES.md",
            disc_head + "".join(f"{row}\n" for row in disc_rows),
        )
    if "RISK_REGISTER" not in drop:
        _write(
            root,
            "docs/governance/work/RISK_REGISTER.md",
            risk_head + "".join(f"{row}\n" for row in risk_rows),
        )


def _kinds(report) -> set[str]:
    return {v["kind"] for v in report.violations}


def _note_kinds(report) -> set[str]:
    return {n["kind"] for n in report.notes}


def _record(report, record_id: str):
    matches = [r for r in report.records if r.record_id == record_id]
    assert len(matches) == 1, f"صفٌّ واحدٌ متوقَّعٌ لـ{record_id}، وقُرِئَ {len(matches)}"
    return matches[0]


TODAY = date(2026, 8, 28)


# ——— الحالةُ السليمةُ: الحرسُ يسكتُ حينَ لا سببَ ———


def test_anchored_tree_has_no_violations(tmp_path: Path) -> None:
    _tree(tmp_path)
    assert ORA.measure(tmp_path, today=TODAY).violations == []


def test_anchored_tree_exits_zero(tmp_path: Path, capsys) -> None:
    _tree(tmp_path)
    assert ORA.main(["--root", str(tmp_path)]) == 0
    assert "لا مخالفةَ مقيسةً" in capsys.readouterr().out


def test_both_registers_are_read(tmp_path: Path) -> None:
    _tree(tmp_path)
    registers = {r.register for r in ORA.measure(tmp_path, today=TODAY).records}
    assert registers == {
        "docs/governance/work/DISCOVERIES.md",
        "docs/governance/work/RISK_REGISTER.md",
    }


# ——— فئاتُ المِرساةِ: كلُّ فئةٍ تُقرأُ من خليّتِها المُعلَنةِ ———


def test_guard_anchor_is_read_from_the_destination_cell(tmp_path: Path) -> None:
    _tree(tmp_path)
    record = _record(ORA.measure(tmp_path, today=TODAY), "DISC-101")
    assert record.anchor == ORA.ANCHOR_GUARD
    assert record.guard_paths == ("tools/governance/probe.py",)


def test_guard_in_the_evidence_cell_is_not_an_anchor(tmp_path: Path) -> None:
    """ملفٌّ يُذكَرُ موضِعَ عَطبٍ في خليّةِ الدليلِ ليس حارسًا له."""
    row = (
        "| DISC-102 | P2 | موضع | ما اكتُشِف | `tools/governance/probe.py:12` | "
        "أثر | يُفتَحُ له بندٌ | مفتوحٌ |"
    )
    _tree(tmp_path, disc_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert _record(report, "DISC-102").anchor == ORA.ANCHOR_NONE
    assert "OPEN_RECORD_WITHOUT_ANCHOR" in _kinds(report)


def test_due_date_is_an_anchor_when_no_guard(tmp_path: Path) -> None:
    row = (
        "| DISC-103 | P3 | موضع | ما اكتُشِف | دليل | أثر | "
        "يُعالَجُ · استحقاق: 2026-09-30 | مفتوحٌ |"
    )
    _tree(tmp_path, disc_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    record = _record(report, "DISC-103")
    assert record.anchor == ORA.ANCHOR_DUE
    assert record.due == "2026-09-30"
    assert report.violations == []


def test_passed_due_date_is_not_an_anchor(tmp_path: Path) -> None:
    row = (
        "| DISC-104 | P3 | موضع | ما اكتُشِف | دليل | أثر | "
        "يُعالَجُ · استحقاق: 2026-08-01 | مفتوحٌ |"
    )
    _tree(tmp_path, disc_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert "DUE_DATE_PASSED" in _kinds(report)


def test_due_date_on_the_day_itself_still_holds(tmp_path: Path) -> None:
    row = (
        "| DISC-105 | P3 | موضع | ما اكتُشِف | دليل | أثر | "
        "يُعالَجُ · استحقاق: 2026-08-28 | مفتوحٌ |"
    )
    _tree(tmp_path, disc_rows=(row,))
    assert ORA.measure(tmp_path, today=TODAY).violations == []


def test_owner_held_is_reported_not_dropped(tmp_path: Path) -> None:
    row = (
        "| DISC-106 | P1 | موضع | ما اكتُشِف | دليل | أثر | "
        "قرارُ المالكِ: تعيينُ مراجعٍ | مفتوحٌ بيدِ المالك |"
    )
    _tree(tmp_path, disc_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert _record(report, "DISC-106").anchor == ORA.ANCHOR_OWNER_HELD
    assert report.violations == []
    assert "OWNER_HELD_WITHOUT_GUARD" in _note_kinds(report)


def test_owner_held_with_a_guard_is_counted_guarded(tmp_path: Path) -> None:
    """ترتيبُ الفئاتِ مُعلَنٌ: الحرسُ القائمُ يسبقُ إعلانَ يدِ المالكِ."""
    row = (
        "| DISC-107 | P1 | موضع | ما اكتُشِف | دليل | أثر | "
        "قرارُ المالكِ · وحرسُه `tools/governance/probe.py` | مفتوحٌ |"
    )
    _tree(tmp_path, disc_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert _record(report, "DISC-107").anchor == ORA.ANCHOR_GUARD
    assert _note_kinds(report) == {"ANCHOR_TALLY"}


def test_unanchored_open_record_is_a_violation(tmp_path: Path) -> None:
    row = "| DISC-108 | P2 | موضع | ما اكتُشِف | دليل | أثر | يُنظَرُ فيه | مفتوحٌ |"
    _tree(tmp_path, disc_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert "OPEN_RECORD_WITHOUT_ANCHOR" in _kinds(report)
    assert ORA.main(["--root", str(tmp_path)]) == 1


# ——— مِرساةٌ مكتوبةٌ لا تحمِلُ شيئًا ———


def test_missing_guard_path_is_a_dead_anchor(tmp_path: Path) -> None:
    row = (
        "| DISC-109 | P2 | موضع | ما اكتُشِف | دليل | أثر | "
        "حرسُه `tools/governance/ghost.py` | مفتوحٌ |"
    )
    _tree(tmp_path, disc_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    record = _record(report, "DISC-109")
    assert record.missing_paths == ("tools/governance/ghost.py",)
    assert record.anchor == ORA.ANCHOR_NONE
    assert "DEAD_ANCHOR" in _kinds(report)


def test_dead_anchor_is_reported_on_closed_rows_too(tmp_path: Path) -> None:
    """قيدٌ مُغلَقٌ يُحيلُ إلى ملفٍّ محذوفٍ يبقى إحالةً كاسرةً."""
    row = (
        "| DISC-110 | P3 | موضع | ما اكتُشِف | دليل | أثر | "
        "أُغلِقَ بـ`tests/governance/test_ghost.py` | مُغلَق |"
    )
    _tree(tmp_path, disc_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert _record(report, "DISC-110").is_open is False
    assert "DEAD_ANCHOR" in _kinds(report)


def test_a_directory_is_not_a_guard_file(tmp_path: Path) -> None:
    row = (
        "| DISC-111 | P3 | موضع | ما اكتُشِف | دليل | أثر | "
        "حرسُه `tools/governance/probe.py` | مفتوحٌ |"
    )
    _tree(tmp_path, disc_rows=(row,), guards=())
    (tmp_path / "tools/governance/probe.py").mkdir(parents=True)
    report = ORA.measure(tmp_path, today=TODAY)
    assert "DEAD_ANCHOR" in _kinds(report)


# ——— حالةُ الصفِّ: تُقرأُ من نصٍّ لا من ظنٍّ ———


def test_handled_row_is_not_read_open(tmp_path: Path) -> None:
    row = (
        "| DISC-112 | P2 | موضع | ما اكتُشِف | دليل | أثر | "
        "بندُ عملٍ | مُعالَج بالبندِ `WI-002` |"
    )
    _tree(tmp_path, disc_rows=(row,))
    record = _record(ORA.measure(tmp_path, today=TODAY), "DISC-112")
    assert record.is_open is False
    assert record.open_basis == "STATUS_SAYS_CLOSED"


def test_partly_handled_but_still_open_is_read_open(tmp_path: Path) -> None:
    """«مُعالَجٌ … والشِّقُّ الثاني مفتوحٌ» مفتوحٌ — الانفتاحُ يسبقُ الإغلاقَ."""
    row = (
        "| DISC-113 | P1 | موضع | ما اكتُشِف | دليل | أثر | بندٌ | "
        "مُعالَجٌ بالبندِ `WI-007` — والشِّقُّ الثاني مفتوحٌ |"
    )
    _tree(tmp_path, disc_rows=(row,))
    record = _record(ORA.measure(tmp_path, today=TODAY), "DISC-113")
    assert record.is_open is True
    assert record.open_basis == "STATUS_SAYS_OPEN"


def test_empty_status_is_read_open(tmp_path: Path) -> None:
    row = "| DISC-114 | P2 | موضع | ما اكتُشِف | دليل | أثر | يُنظَرُ فيه | — |"
    _tree(tmp_path, disc_rows=(row,))
    record = _record(ORA.measure(tmp_path, today=TODAY), "DISC-114")
    assert record.is_open is True
    assert record.open_basis == "STATUS_EMPTY_READ_OPEN"
    assert "OPEN_RECORD_WITHOUT_ANCHOR" in _kinds(ORA.measure(tmp_path, today=TODAY))


def test_undeclared_status_is_read_open_not_closed(tmp_path: Path) -> None:
    """حالةٌ بمفرداتٍ غيرِ مُعلَنةٍ تُقرأُ مفتوحةً — لا يُستنبَطُ إغلاقٌ من نصٍّ حرٍّ."""
    row = "| DISC-115 | P2 | موضع | ما اكتُشِف | دليل | أثر | يُنظَرُ فيه | قيدَ الدراسةِ |"
    _tree(tmp_path, disc_rows=(row,))
    record = _record(ORA.measure(tmp_path, today=TODAY), "DISC-115")
    assert record.is_open is True
    assert record.open_basis == "STATUS_UNDECLARED_READ_OPEN"


def test_every_risk_row_is_open_by_the_section_heading(tmp_path: Path) -> None:
    """سجلُّ المخاطرِ لا عمودَ حالةٍ فيه: عنوانُ § 1 يُعلِنُ انفتاحَ صفوفِه."""
    _tree(tmp_path)
    record = _record(ORA.measure(tmp_path, today=TODAY), "RK-101")
    assert record.is_open is True
    assert record.open_basis == "SECTION_DECLARES_OPEN"


# ——— قاعدةُ سجلِّ المخاطرِ: لا خطرَ بلا إشارةٍ تُقاس ———


def test_risk_without_an_early_signal_is_a_violation(tmp_path: Path) -> None:
    row = (
        "| RK-102 | خطرٌ موصوفٌ | مرتفع | أثر | — | "
        "`tests/governance/test_probe.py` | مالكٌ | قيدٌ |"
    )
    _tree(tmp_path, risk_rows=(row,))
    assert "RISK_SIGNAL_EMPTY" in _kinds(ORA.measure(tmp_path, today=TODAY))


def test_risk_signal_check_is_silent_when_the_cell_is_written(tmp_path: Path) -> None:
    _tree(tmp_path)
    assert "RISK_SIGNAL_EMPTY" not in _kinds(ORA.measure(tmp_path, today=TODAY))


def test_risk_owner_cell_can_declare_owner_held(tmp_path: Path) -> None:
    row = (
        "| RK-103 | خطرٌ مقيسٌ | مرتفع | أثر | عدَّادٌ يصعدُ | يُرفَعُ | "
        "**المالك** (فاتورةٌ وحدُّ إنفاقٍ) | قيدٌ |"
    )
    _tree(tmp_path, risk_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert _record(report, "RK-103").anchor == ORA.ANCHOR_OWNER_HELD
    assert report.violations == []


def test_scope_owner_is_not_read_as_the_repository_owner(tmp_path: Path) -> None:
    """«مالكُ النطاقِ» ليس «المالكَ» — واحدٌ يعملُ والآخرُ يُقرِّرُ."""
    row = (
        "| RK-106 | خطرٌ مقيسٌ | مرتفع | أثر | عدَّادٌ يصعدُ | يُرفَعُ | "
        "مالكُ النطاقِ `audit-truth` | قيدٌ |"
    )
    _tree(tmp_path, risk_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert _record(report, "RK-106").anchor == ORA.ANCHOR_NONE


def test_risk_description_cell_is_not_read_as_an_anchor(tmp_path: Path) -> None:
    """وصفُ الخطرِ لو ذكرَ «قرارَ المالكِ» لا يجعلُه مُرسًى — الخلايا مُعلَنةٌ."""
    row = (
        "| RK-104 | تأخُّرُ قرارِ المالكِ يحجبُ عملًا | مرتفع | أثر | "
        "عدَّادٌ يصعدُ | يُرفَعُ | قائدُ التنفيذ | قيدٌ |"
    )
    _tree(tmp_path, risk_rows=(row,))
    report = ORA.measure(tmp_path, today=TODAY)
    assert _record(report, "RK-104").anchor == ORA.ANCHOR_NONE
    assert "OPEN_RECORD_WITHOUT_ANCHOR" in _kinds(report)


# ——— الصفُّ المعطوبُ يُسمَّى ولا يُبتلَعُ ———


def test_short_discovery_row_is_named_malformed(tmp_path: Path) -> None:
    _tree(tmp_path, disc_rows=("| DISC-116 | P2 | موضع | ما اكتُشِف |",))
    report = ORA.measure(tmp_path, today=TODAY)
    assert "MALFORMED_ROW" in _kinds(report)
    assert [r.record_id for r in report.records] == ["RK-101"]


def test_short_risk_row_is_named_malformed(tmp_path: Path) -> None:
    _tree(tmp_path, risk_rows=("| RK-105 | خطر | مرتفع |",))
    report = ORA.measure(tmp_path, today=TODAY)
    assert "MALFORMED_ROW" in _kinds(report)
    assert [r.record_id for r in report.records] == ["DISC-101"]


# ——— الرفضُ المُصنَّفُ: عجزٌ عن القياسِ لا يُقرأُ نظافةً ———


def test_missing_discoveries_register_is_a_refusal(tmp_path: Path) -> None:
    _tree(tmp_path, drop=("DISCOVERIES",))
    try:
        ORA.measure(tmp_path, today=TODAY)
    except ORA.MeasurementRefused as refusal:
        assert refusal.kind == "SOURCE_MISSING"
    else:  # pragma: no cover - يُبلَغُ إن ابتُلِعَ الرفضُ
        raise AssertionError("سجلٌّ غائبٌ قُرِئَ نظافةً — وذاك ما يمنعُه هذا الفحصُ")


def test_missing_risk_register_is_a_refusal(tmp_path: Path) -> None:
    _tree(tmp_path, drop=("RISK_REGISTER",))
    try:
        ORA.measure(tmp_path, today=TODAY)
    except ORA.MeasurementRefused as refusal:
        assert refusal.kind == "SOURCE_MISSING"
    else:  # pragma: no cover
        raise AssertionError("سجلٌّ غائبٌ قُرِئَ نظافةً")


def test_missing_section_heading_is_a_refusal(tmp_path: Path) -> None:
    _tree(tmp_path, disc_head="# سجلٌّ بلا قسمٍ\n\n| المعرِّف |\n|---|\n")
    try:
        ORA.measure(tmp_path, today=TODAY)
    except ORA.MeasurementRefused as refusal:
        assert refusal.kind == "SECTION_MISSING"
    else:  # pragma: no cover
        raise AssertionError("سجلٌّ بلا قسمِ صفوفٍ قُرِئَ نظافةً")


def test_section_heading_is_matched_without_diacritics(tmp_path: Path) -> None:
    """الحركاتُ لا تُعتَمَدُ حدًّا: عنوانٌ غيرُ مشكولٍ يُقبَلُ."""
    _tree(
        tmp_path,
        disc_head=DISC_HEAD.replace("الاكتشافاتُ المُقيَّدة", "الاكتشافات المقيدة"),
    )
    assert ORA.measure(tmp_path, today=TODAY).violations == []


def test_register_without_rows_is_a_refusal(tmp_path: Path) -> None:
    _tree(tmp_path, disc_rows=())
    try:
        ORA.measure(tmp_path, today=TODAY)
    except ORA.MeasurementRefused as refusal:
        assert refusal.kind == "NO_ROWS"
    else:  # pragma: no cover
        raise AssertionError("سجلٌّ بلا صفوفٍ قُرِئَ نظافةً")


def test_refusal_exits_with_two_and_writes_to_stderr(tmp_path: Path, capsys) -> None:
    _tree(tmp_path, drop=("DISCOVERIES",))
    assert ORA.main(["--root", str(tmp_path)]) == 2
    captured = capsys.readouterr()
    assert "رفضٌ · SOURCE_MISSING" in captured.err
    assert captured.out == ""


# ——— الحِملُ والعدُّ: رقمٌ واحدٌ لا يتناقضُ ———


def test_json_payload_is_valid_and_counts_add_up(tmp_path: Path, capsys) -> None:
    rows = (
        DISC_ANCHORED,
        "| DISC-117 | P2 | موضع | ما اكتُشِف | دليل | أثر | يُنظَرُ فيه | مفتوحٌ |",
        "| DISC-118 | P1 | موضع | ما اكتُشِف | دليل | أثر | قرارُ المالكِ | مفتوحٌ |",
        "| DISC-119 | P3 | موضع | ما اكتُشِف | دليل | أثر | بندٌ | مُغلَق |",
    )
    _tree(tmp_path, disc_rows=rows)
    assert ORA.main(["--root", str(tmp_path), "--json"]) == 1
    payload = json.loads(capsys.readouterr().out)
    assert payload["rows_read"] == 5
    assert payload["open_rows"] == 4
    assert sum(payload["by_anchor"].values()) == payload["open_rows"]
    assert payload["by_anchor"] == {
        "GUARD": 2,
        "DUE": 0,
        "OWNER_HELD": 1,
        "NONE": 1,
    }


def test_tally_note_is_always_written(tmp_path: Path) -> None:
    _tree(tmp_path)
    assert "ANCHOR_TALLY" in _note_kinds(ORA.measure(tmp_path, today=TODAY))


def test_the_tool_writes_nothing_into_the_registers(tmp_path: Path) -> None:
    """بوّابةٌ تُصلِحُ ما تحكمُ عليه لا تُثبِتُ شيئًا (سابقةُ `W-037`)."""
    _tree(tmp_path)
    before = {
        path: path.read_bytes()
        for path in (tmp_path / "docs/governance/work").rglob("*.md")
    }
    ORA.main(["--root", str(tmp_path)])
    after = {
        path: path.read_bytes()
        for path in (tmp_path / "docs/governance/work").rglob("*.md")
    }
    assert before == after


# ——— طفرةٌ مقصودةٌ: يُثبَتُ أنَّ نزعَ التشكيلِ حاملٌ لا زينةٌ ———


def test_over_broad_diacritic_range_would_read_a_handled_row_as_open() -> None:
    """لو نُزِعَت الحروفُ العربيّةُ نفسُها لصارَ كلُّ نصٍّ خاليًا فطابقَ كلَّ علامةٍ.

    هذا العطبُ **وقعَ فعلًا** في أوّلِ تشغيلٍ لهذه الأداةِ: مدًى من `0610` إلى
    `065F` يبتلعُ الأبجديّةَ كلَّها، فقرأتِ الأداةُ سبعةً وثلاثينَ صفًّا كلَّها
    «مفتوحةً» وعشرينَ منها «بيدِ المالكِ». فيُبنى هنا البديلُ المُضعَّفُ ويُقاسُ
    فرقُه، ولا يُعدَّلُ الحرسُ ليُثبَتَ ذلك.
    """
    handled = "مُعالَج ببندٍ قائمٍ"

    def weak_norm(text: str) -> str:
        stripped = "".join(ch for ch in text if not ("\u0610" <= ch <= "\u065f"))
        return re.sub(r"\s+", " ", stripped).strip()

    assert weak_norm(handled) == ""
    assert weak_norm("مفتوح") == ""
    # بالبديلِ المُضعَّفِ: «مفتوح» موجودةٌ في كلِّ نصٍّ — فالحالةُ تُقرأُ مفتوحةً.
    assert weak_norm("مفتوح") in weak_norm(handled)
    # وبالحرسِ القائمِ: الحروفُ باقيةٌ، والعلامةُ غيرُ موجودةٍ.
    assert ORA._norm("مفتوح") == "مفتوح"
    assert ORA._norm("مفتوح") not in ORA._norm(handled)
    assert ORA._classify_open(handled) == (False, "STATUS_SAYS_CLOSED")


def test_anchor_cells_mutation_would_swallow_a_dead_anchor() -> None:
    """لو قُرِئَتِ المِرساةُ من الصفِّ كلِّهِ لصارَ موضِعُ العَطبِ حارسَه."""
    evidence_row_cells = [
        "DISC-120",
        "P2",
        "موضع",
        "ما اكتُشِف",
        "`tools/governance/probe.py:12`",
        "أثر",
        "يُنظَرُ فيه",
        "مفتوحٌ",
    ]
    declared = f"{evidence_row_cells[6]} {evidence_row_cells[7]}"
    whole_row = " ".join(evidence_row_cells)
    assert ORA.PATH_RE.findall(declared) == []
    assert ORA.PATH_RE.findall(whole_row) == ["tools/governance/probe.py"]


# ——— دليلٌ أخيرٌ: السجلّانِ الحاضرانِ يُقرآنِ فعلًا ———


def test_the_live_registers_are_measurable() -> None:
    report = ORA.measure(REPO_ROOT)
    assert len(report.records) >= 30
    assert {r.register for r in report.records} == {
        "docs/governance/work/DISCOVERIES.md",
        "docs/governance/work/RISK_REGISTER.md",
    }
    assert "MALFORMED_ROW" not in _kinds(report)
    assert "DEAD_ANCHOR" not in _kinds(report)


def test_the_live_measurement_is_reproducible() -> None:
    """أمرٌ واحدٌ يُنتِجُ الرقمَ نفسَه مرّتَينِ — شرطُ خروجِ T0."""
    first = ORA.measure(REPO_ROOT)
    second = ORA.measure(REPO_ROOT)
    assert first.to_dict()["by_anchor"] == second.to_dict()["by_anchor"]
    assert [r.record_id for r in first.records] == [r.record_id for r in second.records]
