#!/usr/bin/env python3
"""حرسُ قياسِ انحرافِ وثائقِ الحالةِ — يُثبِتُ أنَّ التأخُّرَ يُشتعِلُ ويسكتُ (W-057).

الهدف:
    أن يكونَ معيارُ `state_document_drift.py` محروسًا لا موصوفًا: كلُّ مخالفةٍ
    تُعلِنُها الأداةُ لها فحصٌ يُثبِتُ اشتعالَها عندَ سببِها **وسكوتَها عندَ
    غيابِه**، وكلُّ رفضٍ مُصنَّفٍ له فحصٌ يُثبِتُ أنَّه رفضٌ لا نتيجةٌ خالية.
النطاق:
    شجرةٌ مؤقّتةٌ تُبنى في كلِّ حالةٍ، وفحصٌ واحدٌ يقرأُ المستودعَ الحقيقيَّ
    ليُثبِتَ أنَّ السجلَّ الحاضرَ يُقرَأُ فعلًا. لا شبكةَ ولا قاعدةَ ولا كتابةَ
    في وثيقةٍ محكومٍ عليها.
المالك: tests/governance — ديوانُ التدقيق
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-08-27
"""

from __future__ import annotations

import importlib.util
import json
import sys
from datetime import UTC, date, datetime
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "state_document_drift.py"


def _load():
    spec = importlib.util.spec_from_file_location("state_document_drift", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    # لا بدَّ من تسجيلِ الوحدةِ قبلَ تنفيذِها: `dataclass` يقرأُ `sys.modules`.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SDD = _load()

LEDGER_HEAD = """# سجلُّ الإكمالِ

## 8 · قيودُ العمل

| القيد | التاريخ | الخطوة | ما أُنجِزَ | ما بقي | الدليل |
|---|---|---|---|---|---|
"""


def _write(root: Path, rel: str, text: str) -> None:
    target = root / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def _tree(
    root: Path,
    *,
    rows: tuple[tuple[str, str], ...] = (
        ("W-003", "2026-08-20"),
        ("W-005", "2026-08-22"),
    ),
    state_doc: str | None = "آخرُ عملٍ W-005.\ntاريخ آخر تعديل: 2026-08-22\n",
    handbook: str | None = "الدليلُ عندَ W-005.\nتاريخ آخر تعديل: 2026-08-22\n",
) -> None:
    """شجرةٌ صغيرةٌ صالحةٌ افتراضًا، تُعطَبُ في كلِّ فحصٍ من موضعٍ واحدٍ."""
    body = LEDGER_HEAD + "".join(
        f"| {work} | {when} | خطوة | أُنجِزَ | بقي | دليل |\n" for work, when in rows
    )
    _write(root, "docs/audit/COMPLETION_LEDGER.md", body)
    if state_doc is not None:
        _write(root, "PROJECT_STATE.md", state_doc.replace("tاريخ", "تاريخ"))
    if handbook is not None:
        _write(root, "docs/PROJECT_HANDBOOK.md", handbook)


def _kinds(report) -> set[str]:
    return {v["kind"] for v in report.violations}


def _note_kinds(report) -> set[str]:
    return {n["kind"] for n in report.notes}


# ——— الحالةُ السليمةُ: الحرسُ يسكتُ حينَ لا سببَ ———


def test_clean_tree_has_no_violations(tmp_path: Path) -> None:
    _tree(tmp_path)
    assert SDD.measure(tmp_path, today=date(2026, 8, 27)).violations == []


def test_clean_tree_exit_zero(tmp_path: Path, capsys) -> None:
    _tree(tmp_path)
    assert SDD.main(["--root", str(tmp_path)]) == 0
    assert "لا انحرافَ مقيسًا" in capsys.readouterr().out


def test_ledger_head_is_read_by_number_not_order(tmp_path: Path) -> None:
    _tree(tmp_path, rows=(("W-009", "2026-08-24"), ("W-002", "2026-08-19")))
    report = SDD.measure(tmp_path, today=date(2026, 8, 27))
    assert report.ledger_newest_work == "W-009"
    assert report.ledger_newest_date == "2026-08-24"


def test_row_count_is_measured(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        rows=(
            ("W-001", "2026-08-18"),
            ("W-002", "2026-08-19"),
            ("W-003", "2026-08-20"),
        ),
    )
    _write(tmp_path, "PROJECT_STATE.md", "W-003\nتاريخ آخر تعديل: 2026-08-20\n")
    _write(tmp_path, "docs/PROJECT_HANDBOOK.md", "W-003\nتاريخ آخر تعديل: 2026-08-20\n")
    assert SDD.measure(tmp_path, today=date(2026, 8, 27)).ledger_rows == 3


def test_declared_documents_are_reported(tmp_path: Path) -> None:
    _tree(tmp_path)
    payload = SDD.measure(tmp_path, today=date(2026, 8, 27)).to_dict()
    assert payload["declared_documents"] == [
        "PROJECT_STATE.md",
        "docs/PROJECT_HANDBOOK.md",
    ]


def test_ledger_head_note_always_present(tmp_path: Path) -> None:
    _tree(tmp_path)
    assert "LEDGER_HEAD" in _note_kinds(SDD.measure(tmp_path, today=date(2026, 8, 27)))


# ——— STATE_DOC_BEHIND ———


def test_behind_fires_when_document_lags(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="آخرُ عملٍ W-003.\nتاريخ آخر تعديل: 2026-08-20\n")
    assert "STATE_DOC_BEHIND" in _kinds(SDD.measure(tmp_path, today=date(2026, 8, 27)))


def test_behind_counts_the_exact_gap(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        rows=(("W-003", "2026-08-20"), ("W-010", "2026-08-25")),
        state_doc="W-003\nتاريخ آخر تعديل: 2026-08-20\n",
        handbook="W-010\nتاريخ آخر تعديل: 2026-08-25\n",
    )
    report = SDD.measure(tmp_path, today=date(2026, 8, 27))
    behind = [v for v in report.violations if v["kind"] == "STATE_DOC_BEHIND"]
    assert len(behind) == 1
    assert "7 قيدًا" in behind[0]["detail"]


def test_behind_fires_on_a_gap_of_one(tmp_path: Path) -> None:
    """قيدٌ واحدٌ تأخُّرًا مخالفةٌ: تحمُّلٌ ولو بواحدٍ يجعلُ الوثيقةَ تكذبُ بإذنٍ."""
    _tree(
        tmp_path,
        rows=(("W-004", "2026-08-21"), ("W-005", "2026-08-22")),
        state_doc="W-004\nتاريخ آخر تعديل: 2026-08-21\n",
    )
    behind = [
        v
        for v in SDD.measure(tmp_path, today=date(2026, 8, 27)).violations
        if v["kind"] == "STATE_DOC_BEHIND"
    ]
    assert len(behind) == 1
    assert "1 قيدًا" in behind[0]["detail"]


def test_behind_names_the_document_and_line(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="سطرٌ أوّلُ\nآخرُ عملٍ W-003\nتاريخ آخر تعديل: 2026-08-20\n")
    behind = [
        v
        for v in SDD.measure(tmp_path, today=date(2026, 8, 27)).violations
        if v["kind"] == "STATE_DOC_BEHIND"
    ]
    assert "PROJECT_STATE.md" in behind[0]["detail"]
    assert "السطرُ 2" in behind[0]["detail"]


def test_behind_silent_when_document_cites_head(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-003 ثمَّ W-005\nتاريخ آخر تعديل: 2026-08-22\n")
    assert "STATE_DOC_BEHIND" not in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_behind_reads_newest_mention_not_first(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-005 قديمًا\nثمَّ W-003\nتاريخ آخر تعديل: 2026-08-22\n")
    assert "STATE_DOC_BEHIND" not in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_behind_fires_for_each_lagging_document(tmp_path: Path) -> None:
    _tree(
        tmp_path,
        state_doc="W-003\nتاريخ آخر تعديل: 2026-08-20\n",
        handbook="W-003\nتاريخ آخر تعديل: 2026-08-20\n",
    )
    report = SDD.measure(tmp_path, today=date(2026, 8, 27))
    assert len([v for v in report.violations if v["kind"] == "STATE_DOC_BEHIND"]) == 2


def test_behind_note_counts_lagging_documents(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-003\nتاريخ آخر تعديل: 2026-08-20\n")
    note = next(
        n
        for n in SDD.measure(tmp_path, today=date(2026, 8, 27)).notes
        if n["kind"] == "LEDGER_HEAD"
    )
    assert "منها 1 متأخِّرةٌ" in note["detail"]


def test_behind_exit_one(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-003\nتاريخ آخر تعديل: 2026-08-20\n")
    assert SDD.main(["--root", str(tmp_path)]) == 1


# ——— STATE_DOC_CITES_UNKNOWN_WORK ———


def test_unknown_work_fires(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="آخرُ عملٍ W-099\nتاريخ آخر تعديل: 2026-08-22\n")
    assert "STATE_DOC_CITES_UNKNOWN_WORK" in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_unknown_work_does_not_also_report_behind(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-099\nتاريخ آخر تعديل: 2026-08-22\n")
    assert "STATE_DOC_BEHIND" not in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_unknown_work_quotes_the_identifier(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-099\nتاريخ آخر تعديل: 2026-08-22\n")
    hit = next(
        v
        for v in SDD.measure(tmp_path, today=date(2026, 8, 27)).violations
        if v["kind"] == "STATE_DOC_CITES_UNKNOWN_WORK"
    )
    assert "W-099" in hit["detail"]


# ——— STATE_DOC_CITES_NO_WORK ———


def test_no_work_mention_fires(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="وثيقةٌ بلا إحالةٍ\nتاريخ آخر تعديل: 2026-08-22\n")
    assert "STATE_DOC_CITES_NO_WORK" in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_no_work_mention_silent_when_cited(tmp_path: Path) -> None:
    _tree(tmp_path)
    assert "STATE_DOC_CITES_NO_WORK" not in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_word_boundary_prevents_false_mention(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="XW-0055\nتاريخ آخر تعديل: 2026-08-22\n")
    assert "STATE_DOC_CITES_NO_WORK" in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


# ——— التواريخُ ———


def test_undeclared_date_fires(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-005 بلا تاريخٍ\n")
    assert "STATE_DOC_UNDECLARED_DATE" in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_undeclared_date_silent_when_declared(tmp_path: Path) -> None:
    _tree(tmp_path)
    assert "STATE_DOC_UNDECLARED_DATE" not in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_future_date_fires(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-005\nتاريخ آخر تعديل: 2026-09-30\n")
    assert "STATE_DOC_DATE_IN_FUTURE" in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_today_is_not_a_future_date(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-005\nتاريخ آخر تعديل: 2026-08-27\n")
    assert "STATE_DOC_DATE_IN_FUTURE" not in _kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


def test_stale_date_is_a_note_not_a_violation(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-005\nتاريخ آخر تعديل: 2026-08-20\n")
    report = SDD.measure(tmp_path, today=date(2026, 8, 27))
    assert "DATE_OLDER_THAN_LATEST_ENTRY" in _note_kinds(report)
    assert report.violations == []


def test_stale_date_note_silent_when_current(tmp_path: Path) -> None:
    _tree(tmp_path)
    assert "DATE_OLDER_THAN_LATEST_ENTRY" not in _note_kinds(
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    )


# ——— الرفضُ المُصنَّفُ: لا يُقرَأُ نظافةً ———


def test_missing_ledger_is_refusal(tmp_path: Path) -> None:
    _tree(tmp_path)
    (tmp_path / "docs/audit/COMPLETION_LEDGER.md").unlink()
    with pytest.raises(SDD.MeasurementRefused) as excinfo:
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    assert excinfo.value.kind == "SOURCE_MISSING"


def test_missing_state_document_is_refusal(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc=None)
    with pytest.raises(SDD.MeasurementRefused) as excinfo:
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    assert excinfo.value.kind == "SOURCE_MISSING"


def test_ledger_without_rows_is_refusal(tmp_path: Path) -> None:
    _tree(tmp_path)
    _write(tmp_path, "docs/audit/COMPLETION_LEDGER.md", LEDGER_HEAD)
    with pytest.raises(SDD.MeasurementRefused) as excinfo:
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    assert excinfo.value.kind == "NO_LEDGER_ROWS"


def test_refusal_exits_two_and_writes_to_stderr(tmp_path: Path, capsys) -> None:
    _tree(tmp_path)
    (tmp_path / "docs/audit/COMPLETION_LEDGER.md").unlink()
    assert SDD.main(["--root", str(tmp_path)]) == 2
    captured = capsys.readouterr()
    assert "رفضٌ · SOURCE_MISSING" in captured.err
    assert captured.out == ""


def test_prose_rows_are_not_read_as_entries(tmp_path: Path) -> None:
    _tree(tmp_path)
    _write(
        tmp_path,
        "docs/audit/COMPLETION_LEDGER.md",
        LEDGER_HEAD + "نصٌّ يذكرُ W-099 في فقرةٍ لا في صفٍّ.\n",
    )
    with pytest.raises(SDD.MeasurementRefused) as excinfo:
        SDD.measure(tmp_path, today=date(2026, 8, 27))
    assert excinfo.value.kind == "NO_LEDGER_ROWS"


# ——— الحِملُ والمخرجُ ———


def test_json_output_is_parsable(tmp_path: Path, capsys) -> None:
    _tree(tmp_path)
    SDD.main(["--root", str(tmp_path), "--json"])
    payload = json.loads(capsys.readouterr().out)
    assert payload["ledger_newest_work"] == "W-005"
    assert len(payload["documents"]) == 2


def test_json_flag_writes_no_file(tmp_path: Path, capsys) -> None:
    _tree(tmp_path)
    before = {p for p in tmp_path.rglob("*") if p.is_file()}
    SDD.main(["--root", str(tmp_path), "--json"])
    capsys.readouterr()
    assert {p for p in tmp_path.rglob("*") if p.is_file()} == before


def test_documents_are_not_rewritten(tmp_path: Path) -> None:
    _tree(tmp_path, state_doc="W-003\nتاريخ آخر تعديل: 2026-08-20\n")
    before = (tmp_path / "PROJECT_STATE.md").read_text(encoding="utf-8")
    SDD.measure(tmp_path, today=date(2026, 8, 27))
    assert (tmp_path / "PROJECT_STATE.md").read_text(encoding="utf-8") == before


def test_render_lists_every_document(tmp_path: Path) -> None:
    _tree(tmp_path)
    text = SDD.render(SDD.measure(tmp_path, today=date(2026, 8, 27)))
    assert "PROJECT_STATE.md" in text
    assert "docs/PROJECT_HANDBOOK.md" in text


def test_newest_returns_none_on_empty() -> None:
    assert SDD.newest([]) is None


# ——— قياسٌ على المستودعِ الحقيقيِّ ———


def test_real_repository_is_measurable() -> None:
    report = SDD.measure(REPO_ROOT, today=datetime.now(UTC).date())
    assert report.ledger_rows > 40
    assert report.ledger_newest_work.startswith("W-0")
    assert len(report.documents) == len(SDD.STATE_DOCUMENTS)


def test_real_state_documents_cite_the_ledger_head() -> None:
    """الحرسُ الذي يُسقِطُ عملَ اليومِ إن تُرِكَتِ الوثيقتانِ متأخِّرتَين."""
    report = SDD.measure(REPO_ROOT, today=datetime.now(UTC).date())
    assert [v for v in report.violations if v["kind"] == "STATE_DOC_BEHIND"] == []
