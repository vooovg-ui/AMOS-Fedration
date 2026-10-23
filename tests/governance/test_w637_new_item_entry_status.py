"""
الهدف: إثباتُ حرسِ D21-د — بندٌ جديدٌ لا يدخلُ سجلَّ العملِ بحالةٍ تحجزُ مساراتٍ
       (RESERVED/IN_PROGRESS/…)؛ يُسجَّلُ PROPOSED أو READY ثمَّ ينتقلُ قيدًا مستقلًّا (H3).
النطاق: فرعُ «البندِ الجديدِ» في فحصِ الانتقالاتِ بـ`tools/governance/check_work_governance.py`
        وحدَه (بندُ WI-040 القائمُ · W-637 · قرارُ المالكِ D21-د: «يُستكمل الحرس الذي يمنع
        تكراره في بند قائم لا جديد»).
المالك: tests/governance
تاريخ الإنشاء: 2026-10-23
تاريخ آخر تعديل: 2026-10-23

لماذا
-----
مرَّ تسجيلُ WI-108 مباشرةً IN_PROGRESS في W-629 لأنَّ البوّابةَ كانت تتخطّى كلَّ
بندٍ لا سابقَ له («old is None ⇒ continue»). فيُثبَّتُ هنا أنَّ الدخولَ الحاجزَ
يسقطُ، وأنَّ الدخولَ المشروعَ (PROPOSED · READY) والبندَ القائمَ لا يتأثَّران.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_HELPERS_PATH = Path(__file__).with_name("test_work_governance_gate.py")
_spec = importlib.util.spec_from_file_location("_wg_helpers_w637", _HELPERS_PATH)
assert _spec is not None and _spec.loader is not None
h = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(h)
gate = h.gate

NEW_ROW = (
    "| WI-002 | tooling-gates | T2 | فلان | فلانٌ آخر | {status} "
    "| tools/governance/new_tool.py | 2026-08-20 | 2026-09-30 | — | خطوةٌ واحدة | — |"
)


def _add_new_item(repo: Path, status: str) -> None:
    body = (repo / gate.ACTIVE_PATH).read_text(encoding="utf-8")
    row = NEW_ROW.format(status=status)
    block = h.DETAIL_BLOCK.replace("### WI-001", "### WI-002").replace(
        "الحالة: IN_PROGRESS", f"الحالة: {status}"
    )
    body = body.replace(h.ACTIVE_ROW, f"{h.ACTIVE_ROW}\n{row}") + "\n" + block
    h._stage(repo, gate.ACTIVE_PATH, body)


@pytest.mark.parametrize("status", ["RESERVED", "IN_PROGRESS", "IN_REVIEW", "VERIFIED"])
def test_بندٌ_جديدٌ_بحالةٍ_حاجزةٍ_يسقط(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, status: str
) -> None:
    repo = h._mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    _add_new_item(repo, status)
    assert "NEW_ITEM_CLAIMING_ENTRY" in h._kinds()


@pytest.mark.parametrize("status", ["PROPOSED", "READY"])
def test_بندٌ_جديدٌ_بحالةٍ_غيرِ_حاجزةٍ_يمرّ(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, status: str
) -> None:
    repo = h._mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    _add_new_item(repo, status)
    assert "NEW_ITEM_CLAIMING_ENTRY" not in h._kinds()


def test_البندُ_القائمُ_لا_يتأثَّرُ_بالحرس(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """WI-001 قائمٌ في الأساسِ IN_PROGRESS — انتقالُه المشروعُ لا يُرصَدُ دخولًا جديدًا."""
    repo = h._mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    body = (repo / gate.ACTIVE_PATH).read_text(encoding="utf-8")
    h._stage(repo, gate.ACTIVE_PATH, body.replace("IN_PROGRESS", "IN_REVIEW"))
    kinds = h._kinds()
    assert "NEW_ITEM_CLAIMING_ENTRY" not in kinds
    assert "ILLEGAL_TRANSITION" not in kinds

