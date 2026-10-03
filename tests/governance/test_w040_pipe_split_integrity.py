#!/usr/bin/env python3
"""حرسُ قاسمِ الخلايا — أنبوبٌ مهروبٌ محتوًى لا حدٌّ (WI-040 · DISC-048).

الهدف:
    أن يكونَ العَطبُ المُقيَّدُ في `DISC-048` محروسًا في قارئِ
    `check_work_governance.py._cells` و`check_discoveries`. كانَ يقسِمُ على
    `split("|")` فيمرُّ الأنبوبُ المهروبُ `\\|` حدًّا، فتزحفُ الأعمدةُ ويُحكَمُ
    على صفٍّ لم يُقرَأْ. فصارَ يُقسَمُ على أنبوبٍ غيرِ مهروبٍ، ويُزالُ هربُه
    في نصِّ الخليّةِ، وعددُ الأعمدةِ مُلزَمٌ في الجهتَينِ.

    أمّا `guard_enforcement_closure.py.table_rows` فمسارُه مقفولٌ بـ`WI-023`
    (`IN_REVIEW`) فلا يُمَسُّ في هذا البندِ — يُؤجَّلُ إلى تحرُّرِه.
النطاق:
    فحوصٌ مباشرةٌ على الدالةِ بشجرةٍ مؤقّتةٍ. لا شبكةَ ولا قاعدةَ بيانات.
المالك: tests/governance — ديوانُ التدقيق
تاريخ الإنشاء: 2026-10-03
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CWG_PATH = REPO_ROOT / "tools" / "governance" / "check_work_governance.py"


def _load_cwg():
    spec = importlib.util.spec_from_file_location("cwg_w040", CWG_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CWG = _load_cwg()


# ── بياناتُ الاختبارِ ──────────────────────────────────────────────────────

#: صفٌّ سليمٌ بثمانِ خلايا — بدون أنبوبٍ مهروبٍ.
_GOOD_DISC_ROW = (
    "| DISC-201 | P2 | موضع | ما اكتُشِف | دليل | أثر | الوجهةُ `WI-001` | مفتوحٌ |"
)

#: صفٌّ فيه أنبوبٌ غيرُ مهروبٍ داخلَ خليّةِ الوجهة: تسعُ خلايا.
_OVERFLOWING_DISC_ROW = (
    "| DISC-203 | P2 | موضع | ما اكتُشِف | دليل | أثر | "
    "الوجهةُ `grep tests/ | wc -l` | مفتوحٌ |"
)

#: الصفُّ نفسُه بعدَ الهربِ: ثمانِ خلايا، والأنبوبُ محتوًى.
_ESCAPED_DISC_ROW = _OVERFLOWING_DISC_ROW.replace("| wc -l", r"\| wc -l")

#: صفٌّ ناقصٌ: سبعُ خلايا.
_TOO_FEW_ROW = "| DISC-204 | P2 | موضع | ما اكتُشِف | دليل | أثر | مفتوحٌ |"


# ── فحوصُ `check_work_governance._cells` ──────────────────────────────────────


class TestCellsSplit:
    """القاسمُ يفرِّقُ بينَ الأنبوبِ الحدِّ والأنبوبِ المحتوى."""

    def test_escaped_pipe_is_content_not_a_delimiter(self) -> None:
        """`\\|` محتوًى لا حدٌّ — فالصفُّ ثمانِ خلايا لا تسعٌ."""
        cells = CWG._cells(_ESCAPED_DISC_ROW)
        assert len(cells) == 8

    def test_escaped_pipe_is_unescaped_in_cell_text(self) -> None:
        """الهربُ يُزالُ عندَ القراءةِ، فلا يتغيَّرُ النصُّ."""
        cells = CWG._cells(_ESCAPED_DISC_ROW)
        assert "| wc -l" in cells[6]
        assert r"\|" not in cells[6]

    def test_unescaped_pipe_overflows_to_nine_cells(self) -> None:
        """الأنبوبُ غيرُ المهروبِ حدٌّ — فالصفُّ تسعُ خلايا."""
        cells = CWG._cells(_OVERFLOWING_DISC_ROW)
        assert len(cells) == 9

    def test_good_row_reads_eight_cells(self) -> None:
        """صفٌّ سليمٌ بلا أنبوبٍ مهروبٍ — ثمانِ خلايا."""
        cells = CWG._cells(_GOOD_DISC_ROW)
        assert len(cells) == 8


# ── فحوصُ `check_work_governance.check_discoveries` ───────────────────────────


class TestDiscoveriesColumnCount:
    """عددُ الأعمدةِ مُلزَمٌ في الجهتَينِ، والرسالةُ تُسمّي السببَ."""

    def test_overflowing_row_is_refused(self) -> None:
        """الزيادةُ تُرفَضُ كما يُرفَضُ النقصُ."""
        text = f"# سجل\n\n## 1\n\n| أ | ب | ج | د | هـ | و | ز | ح |\n|---|---|---|---|---|---|---|---|\n{_OVERFLOWING_DISC_ROW}\n"
        violations = CWG.check_discoveries(text)
        kinds = [v["kind"] for v in violations]
        assert "MALFORMED_ITEM" in kinds

    def test_too_few_row_is_refused(self) -> None:
        """النقصُ يُرفَضُ."""
        text = f"# سجل\n\n## 1\n\n| أ | ب | ج | د | هـ | و | ز | ح |\n|---|---|---|---|---|---|---|---|\n{_TOO_FEW_ROW}\n"
        violations = CWG.check_discoveries(text)
        kinds = [v["kind"] for v in violations]
        assert "MALFORMED_ITEM" in kinds

    def test_escaped_pipe_row_is_accepted(self) -> None:
        """الصفُّ المهروبُ يُقرأُ ثمانيًا — فلا مخالفةَ."""
        text = f"# سجل\n\n## 1\n\n| أ | ب | ج | د | هـ | و | ز | ح |\n|---|---|---|---|---|---|---|---|\n{_ESCAPED_DISC_ROW}\n"
        violations = CWG.check_discoveries(text)
        kinds = [v["kind"] for v in violations]
        assert "MALFORMED_ITEM" not in kinds

    def test_overflow_message_names_unescaped_pipe_as_cause(self) -> None:
        """رسالةُ الزيادةِ تُسمّي الأنبوبَ غيرَ المهروبِ سببًا."""
        text = f"# سجل\n\n## 1\n\n| أ | ب | ج | د | هـ | و | ز | ح |\n|---|---|---|---|---|---|---|---|\n{_OVERFLOWING_DISC_ROW}\n"
        violations = CWG.check_discoveries(text)
        detail = next(v["detail"] for v in violations if v["kind"] == "MALFORMED_ITEM")
        assert "مهروب" in detail


# ── فحوصُ الطفراتِ — تُثبِتُ أنَّ الحرسَ يعملُ لا أنَّه موجودٌ ────────────────────


class TestMutations:
    """إعادةُ القسمِ الساذجِ تُسقِطُ فحصًا مُسمًّى، ورفعُ حدِّ العددِ يُسقِطُ فحصًا."""

    def test_naive_split_would_accept_overflowing_row(self) -> None:
        """طفرةٌ: لو عادَ القسمُ الساذجُ `split("|")` لمرَّ الصفُّ ذو التسعِ خلايا."""
        import re as _re

        original = CWG._CELL_SPLIT_RE
        try:
            CWG._CELL_SPLIT_RE = _re.compile(r"\|")
            cells = CWG._cells(_ESCAPED_DISC_ROW)
            # مع القسمِ الساذجِ، `\\|` يُنتِجُ خليّةً فارغةً + 8 خلايا = 9
            assert len(cells) != 8, "القسمُ الساذجُ لا يُنتِجُ ثمانيًا"
        finally:
            CWG._CELL_SPLIT_RE = original

    def test_relaxing_column_limit_would_accept_overflow(self) -> None:
        """طفرةٌ: لو رُفِعَ حدُّ العددِ لمرَّ الصفُّ ذو التسعِ خلايا."""
        text = f"# سجل\n\n## 1\n\n| أ | ب | ج | د | هـ | و | ز | ح |\n|---|---|---|---|---|---|---|---|\n{_OVERFLOWING_DISC_ROW}\n"
        original_check = CWG.check_discoveries
        try:

            def _relaxed(text: str):
                violations = []
                for line in text.splitlines():
                    import re

                    m = re.match(r"\|\s*(DISC-\d+)", line)
                    if not m:
                        continue
                    cells = CWG._cells(line)
                    if len(cells) < 8:
                        violations.append(
                            {"kind": "MALFORMED_ITEM", "detail": "too few"}
                        )
                return violations

            CWG.check_discoveries = _relaxed
            violations = CWG.check_discoveries(text)
            assert "MALFORMED_ITEM" not in [v["kind"] for v in violations]
        finally:
            CWG.check_discoveries = original_check
