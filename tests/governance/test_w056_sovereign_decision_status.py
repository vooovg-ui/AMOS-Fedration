#!/usr/bin/env python3
"""حرسُ قياسِ حالةِ القراراتِ السياديّةِ — يُثبِتُ أنَّ الحكمَ يتبعُ الجدولَ (W-056).

الهدف:
    أن يكونَ معيارُ `sovereign_decision_status.py` محروسًا لا موصوفًا: كلُّ
    مخالفةٍ يُعلِنُها الملفُّ لها فحصٌ يُثبِتُ أنَّها تُشتعِلُ حينَ يقعُ سببُها
    و**تسكتُ حينَ لا يقعُ**، وكلُّ رفضٍ مُصنَّفٍ له فحصٌ يُثبِتُ أنَّه رفضٌ لا
    نتيجةٌ خالية.
النطاق:
    فحوصٌ على شجرةٍ مؤقّتةٍ تُبنى في كلِّ حالةٍ، وفحصٌ واحدٌ على المستودعِ
    الحقيقيِّ يُثبِتُ أنَّ الجدولَ الحاضرَ يُقرَأُ فعلًا. لا شبكةَ ولا قاعدةَ.
المالك: tests/governance — ديوانُ التدقيق
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-08-27
"""

from __future__ import annotations

import importlib.util
import json
import sys
from datetime import date
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "sovereign_decision_status.py"


def _load():
    spec = importlib.util.spec_from_file_location(
        "sovereign_decision_status", TOOL_PATH
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    # لا بدَّ من تسجيلِ الوحدةِ قبلَ تنفيذِها: `dataclass` يقرأُ `sys.modules`.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SDS = _load()


ROADMAP_HEAD = """# خارطةُ العمل

> **الحالة:** `{state} — نصٌّ لا يُقاسُ هنا`

## 15 · قسمٌ سابقٌ

لا شيءَ يُقاسُ هنا.

## 16 · اعتمادُ هذه الوثيقةِ وتعديلُها

4. ما دامت `PROPOSED`، تعملُ البوّابةُ في وضعِ **الإبلاغِ** (`--advisory`) لا الإسقاط.

| # | القرار | المالك | التاريخ | الحالة |
|---|---|---|---|---|
{rows}

## 17 · قسمٌ لاحقٌ
"""

ROW_A1 = "| A-1 | اعتمادُ الخارطةِ | المالك | 2026-08-26 | `APPROVED` (نافذة) |"
ROW_A2 = "| A-2 | تعيينُ المراجعِ المستقلّ | المالك | — | `PENDING` |"
ROW_A3 = "| A-3 | تفعيلُ بوّابةِ الإسقاط | المالك | — | `PENDING` |"


def build_tree(
    tmp_path: Path,
    *,
    state: str = "ACTIVE",
    rows: list[str] | None = None,
    roadmap_text: str | None = None,
    active_work: str | None = None,
    extra_docs: dict[str, str] | None = None,
) -> Path:
    """شجرةٌ مؤقّتةٌ أصغرُ ما يُقاسُ عليه — لا نسخةَ من المستودعِ الحقيقيّ."""
    work = tmp_path / "docs" / "governance" / "work"
    work.mkdir(parents=True)
    text = (
        roadmap_text
        if roadmap_text is not None
        else ROADMAP_HEAD.format(
            state=state, rows="\n".join(rows or [ROW_A1, ROW_A2, ROW_A3])
        )
    )
    (tmp_path / SDS.ROADMAP).write_text(text, encoding="utf-8")
    if active_work is not None:
        (tmp_path / SDS.ACTIVE_WORK).write_text(active_work, encoding="utf-8")
    for rel, body in (extra_docs or {}).items():
        target = tmp_path / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
    return tmp_path


def kinds(report) -> set[str]:
    return {v["kind"] for v in report.violations}


# ─────────────────────────── قراءةُ الجدولِ كما هو ───────────────────────────


def test_reads_every_decision_row(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path))
    assert [d.ident for d in report.decisions] == ["A-1", "A-2", "A-3"]


def test_reads_status_and_date_from_cells(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path))
    by_id = {d.ident: d for d in report.decisions}
    assert by_id["A-1"].status == "APPROVED"
    assert by_id["A-1"].on_date == "2026-08-26"
    assert by_id["A-2"].status == "PENDING"
    assert by_id["A-2"].on_date is None


def test_pending_decisions_are_blocking(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path))
    by_id = {d.ident: d for d in report.decisions}
    assert by_id["A-2"].is_blocking and by_id["A-3"].is_blocking
    assert not by_id["A-1"].is_blocking


def test_reads_declared_document_state(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path, state="ACTIVE"))
    assert report.doc_state == "ACTIVE"


def test_reads_advisory_basis_from_section(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path))
    assert report.advisory_basis_state == "PROPOSED"


# ───────────────────── سندُ الإبلاغِ: انقضى أم ما زالَ قائمًا ─────────────────────


def test_expired_advisory_basis_is_reported(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path, state="ACTIVE"))
    assert "ADVISORY_BASIS_EXPIRED" in kinds(report)


def test_advisory_basis_intact_is_silent(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path, state="PROPOSED"))
    assert "ADVISORY_BASIS_EXPIRED" not in kinds(report)


def test_expired_basis_alone_does_not_fail_the_run(tmp_path: Path) -> None:
    tree = build_tree(tmp_path, state="ACTIVE")
    assert SDS.main(["--root", str(tree)]) == 0


def test_expired_basis_fails_only_when_enforced(tmp_path: Path) -> None:
    tree = build_tree(tmp_path, state="ACTIVE")
    assert SDS.main(["--root", str(tree), "--enforce-basis"]) == 1


# ──────────────────────── مخالفاتٌ تُصلَحُ بيدِ من يُحرِّرُ ────────────────────────


def test_unknown_status_is_a_violation(tmp_path: Path) -> None:
    row = "| A-4 | قرارٌ بحالةٍ مبتكَرةٍ | المالك | — | `MAYBE_LATER` |"
    report = SDS.measure(build_tree(tmp_path, rows=[ROW_A1, row]))
    assert "UNKNOWN_DECISION_STATUS" in kinds(report)


def test_approved_without_date_is_a_violation(tmp_path: Path) -> None:
    row = "| A-1 | اعتمادٌ بلا تاريخٍ | المالك | — | `APPROVED` |"
    report = SDS.measure(build_tree(tmp_path, rows=[row]))
    assert "APPROVED_WITHOUT_DATE" in kinds(report)


def test_pending_with_date_is_a_violation(tmp_path: Path) -> None:
    row = "| A-2 | مُعلَّقٌ ومؤرَّخٌ معًا | المالك | 2026-08-20 | `PENDING` |"
    report = SDS.measure(build_tree(tmp_path, rows=[ROW_A1, row]))
    assert "PENDING_WITH_DATE" in kinds(report)


def test_future_decision_date_is_a_violation(tmp_path: Path) -> None:
    row = "| A-5 | قرارٌ لم يقعْ | المالك | 2099-01-01 | `APPROVED` |"
    report = SDS.measure(build_tree(tmp_path, rows=[ROW_A1, row]))
    assert "DECISION_DATE_IN_FUTURE" in kinds(report)


def test_past_dates_are_not_flagged_as_future(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path), today=date(2026, 8, 27))
    assert "DECISION_DATE_IN_FUTURE" not in kinds(report)


def test_reference_to_missing_decision_is_a_violation(tmp_path: Path) -> None:
    tree = build_tree(
        tmp_path,
        extra_docs={"docs/note.md": "هذا العملُ موقوفٌ على A-9 بنصِّ سجلِّه."},
    )
    report = SDS.measure(tree)
    assert "DANGLING_DECISION_REF" in kinds(report)


def test_reference_to_existing_decision_is_not_flagged(tmp_path: Path) -> None:
    tree = build_tree(
        tmp_path,
        extra_docs={"docs/note.md": "هذا العملُ موقوفٌ على A-2 بنصِّ سجلِّه."},
    )
    report = SDS.measure(tree)
    assert "DANGLING_DECISION_REF" not in kinds(report)
    assert any(r.endswith("docs/note.md:1") for r in report.references["A-2"])


def test_clean_table_has_no_hard_violation(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path, state="PROPOSED"))
    assert report.violations == []


# ───────────────────────── عدُّ الإشاراتِ: ما يُعَدُّ وما يُستثنى ─────────────────────────


def test_roadmap_table_is_not_counted_as_a_reference(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path))
    assert report.references["A-2"] == []


def test_measuring_tool_and_its_test_are_excluded(tmp_path: Path) -> None:
    tree = build_tree(
        tmp_path,
        extra_docs={
            "tools/governance/sovereign_decision_status.py": "# A-2 A-3 وصفٌ لا حجبٌ\n",
            "tests/governance/test_w056_sovereign_decision_status.py": "# A-2\n",
            "docs/other.md": "A-2\n",
        },
    )
    report = SDS.measure(tree)
    assert report.references["A-2"] == ["docs/other.md:1"]


def test_frozen_items_are_measured_from_active_work(tmp_path: Path) -> None:
    rows = (
        "| WI-006 | tooling | IN_REVIEW | الإغلاقُ موقوفٌ على A-2 |\n"
        "| WI-011 | audit | IN_PROGRESS | لا عائقَ |\n"
    )
    report = SDS.measure(build_tree(tmp_path, active_work=rows))
    assert report.frozen_items["A-2"] == ["WI-006"]
    assert "A-3" not in report.frozen_items


def test_missing_active_work_is_not_an_invented_zero(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path))
    assert report.frozen_items == {}


def test_pending_age_is_declared_a_lower_bound(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path), today=date(2026, 9, 5))
    note = next(n for n in report.notes if n["kind"] == "PENDING_SINCE_AT_LEAST")
    assert "حدٌّ أدنى" in note["detail"]
    assert "10 يومًا" in note["detail"]


# ──────────────────────────── الرفضُ المُصنَّفُ لا الصمتُ ────────────────────────────


def test_missing_roadmap_is_a_classified_refusal(tmp_path: Path) -> None:
    with pytest.raises(SDS.MeasurementRefused) as err:
        SDS.measure(tmp_path)
    assert err.value.kind == "SOURCE_MISSING"


def test_missing_section_is_a_classified_refusal(tmp_path: Path) -> None:
    tree = build_tree(
        tmp_path, roadmap_text="> **الحالة:** `ACTIVE`\n\n## 15 · لا اعتمادَ هنا\n"
    )
    with pytest.raises(SDS.MeasurementRefused) as err:
        SDS.measure(tree)
    assert err.value.kind == "SECTION_MISSING"


def test_section_without_rows_is_a_classified_refusal(tmp_path: Path) -> None:
    tree = build_tree(tmp_path, rows=["| لا معرِّفَ | نصٌّ | المالك | — | `PENDING` |"])
    with pytest.raises(SDS.MeasurementRefused) as err:
        SDS.measure(tree)
    assert err.value.kind == "NO_DECISION_ROWS"


def test_missing_document_state_is_a_classified_refusal(tmp_path: Path) -> None:
    body = ROADMAP_HEAD.format(state="ACTIVE", rows=ROW_A2).replace(
        "> **الحالة:** `ACTIVE — نصٌّ لا يُقاسُ هنا`", "لا حالةَ مُعلَنةً"
    )
    tree = build_tree(tmp_path, roadmap_text=body)
    with pytest.raises(SDS.MeasurementRefused) as err:
        SDS.measure(tree)
    assert err.value.kind == "DOC_STATE_MISSING"


def test_refusal_exits_with_two_not_one(tmp_path: Path) -> None:
    assert SDS.main(["--root", str(tmp_path)]) == 2


def test_hard_violation_exits_with_one(tmp_path: Path) -> None:
    row = "| A-4 | حالةٌ مبتكَرةٌ | المالك | — | `MAYBE_LATER` |"
    tree = build_tree(tmp_path, state="PROPOSED", rows=[ROW_A1, row])
    assert SDS.main(["--root", str(tree)]) == 1


def test_json_mode_emits_parsable_payload(tmp_path: Path, capsys) -> None:
    tree = build_tree(tmp_path, state="PROPOSED")
    assert SDS.main(["--root", str(tree), "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert [d["ident"] for d in payload["decisions"]] == ["A-1", "A-2", "A-3"]
    assert payload["doc_state"] == "PROPOSED"


# ─────────────────── لا تُصلِحُ ما تحكمُ عليه · والجدولُ الحاضرُ يُقرَأُ ───────────────────


def test_run_does_not_rewrite_the_roadmap(tmp_path: Path) -> None:
    tree = build_tree(tmp_path)
    before = (tree / SDS.ROADMAP).read_bytes()
    SDS.main(["--root", str(tree)])
    assert (tree / SDS.ROADMAP).read_bytes() == before


def test_live_repository_table_is_readable(tmp_path: Path) -> None:
    report = SDS.measure(REPO_ROOT)
    idents = {d.ident for d in report.decisions}
    assert {"A-1", "A-2", "A-3"} <= idents


def test_unreadable_file_is_named_not_swallowed(tmp_path: Path) -> None:
    tree = build_tree(tmp_path)
    (tree / "docs" / "broken.md").write_bytes(b"\xff\xfe A-2 \x00")
    report = SDS.measure(tree)
    note = next(n for n in report.notes if n["kind"] == "UNREADABLE_SOURCE")
    assert "docs/broken.md" in note["detail"]
    assert "ناقصٌ" in note["detail"]


def test_readable_tree_has_no_unreadable_note(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path))
    assert all(n["kind"] != "UNREADABLE_SOURCE" for n in report.notes)


def test_missing_work_register_is_declared_unmeasured(tmp_path: Path) -> None:
    report = SDS.measure(build_tree(tmp_path))
    note = next(n for n in report.notes if n["kind"] == "WORK_REGISTER_UNREAD")
    assert "لم تُقَسْ" in note["detail"]


def test_present_work_register_has_no_unread_note(tmp_path: Path) -> None:
    tree = build_tree(tmp_path, active_work="| WI-006 | tooling | موقوفٌ على A-2 |\n")
    report = SDS.measure(tree)
    assert all(n["kind"] != "WORK_REGISTER_UNREAD" for n in report.notes)
