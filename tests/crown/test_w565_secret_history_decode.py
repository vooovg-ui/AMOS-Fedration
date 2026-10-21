#!/usr/bin/env python3
"""
حرسُ صمودِ حارسِ الأسرارِ أمامَ بايتٍ تالفٍ واحدٍ في التاريخِ — W-565

الهدف: إثباتٌ مُعادُ التشغيلِ أنَّ الإصلاحَ (فكُّ خرجِ `git log --all -p`
       بالاستبدالِ لا بالانهيارِ) لم يُعمِ الحارسَ ولم يُخفِّفْه: بايتٌ تالفٌ
       واحدٌ في التاريخِ (بايتٌ لا يُمحى لأنَّ التزامَه مدفوعٌ — عينُ DISC-119)
       لا يُسقِطُ الحارسَ، وكتلةُ PEM زُرِعَت ثم حُذِفَت منَ الشجرةِ ما زالت
       تُلتقَطُ منَ التاريخِ رغمَ وجودِ البايتِ التالفِ في الجمعِ نفسِهِ.
       فلا انهيارَ ولا عمى — حُكْمٌ كاملُ التغطيةِ.

النطاق: التاريخِ المنشورِ في `tools/crown/verify_secret_boundaries.py`
        (`_added_key_lines` · بوّابةُ «لا مادة مفتاح خاص في التاريخ المنشور»).
        أمّا شجرةُ العملِ فتُفحَصُ بنمطٍ آخرَ (errors="ignore") ولا يشملُها هذا الحرسُ.

المالك: tests/crown — المجلس التأسيسي
تاريخ الإنشاء: 2026-10-21 (`W-565` · `WI-103` · سندُ `DISC-119`)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

# الجذرُ بعَلَمٍ صريحٍ لا بعُمقٍ: «git rev-parse» — لا اشتقاقًا من موقعِ الملفِ
REPO_ROOT = Path(subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True, check=True,
).stdout.strip())
GUARD_REL = "tools/crown/verify_secret_boundaries.py"


def _clone(tmp_path: Path) -> Path:
    """استنساخٌ كاملُ العمقِ منَ المستودعِ الحقيقيِّ — التاريخُ هو موضوعُ الفحصِ."""
    target = tmp_path / "repo"
    result = subprocess.run(
        ["git", "clone", "--quiet", f"file://{REPO_ROOT}", str(target)],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        pytest.skip(f"تعذّر الاستنساخُ في هذه البيئةِ: {result.stderr.strip()[:120]}")
    return target


def _commit(clone: Path, files: dict[str, bytes], message: str) -> None:
    for rel, content in files.items():
        (clone / rel).write_bytes(content)
    subprocess.run(["git", "-C", str(clone), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(clone), "-c", "user.name=w565", "-c", "user.email=w565@local",
         "commit", "--quiet", "-m", message],
        check=True, capture_output=True,
    )


def _run_gate(clone: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, GUARD_REL],
        cwd=clone, capture_output=True, check=False,
        encoding="utf-8", errors="replace",
    )


def _bad_byte_line() -> bytes:
    """حرفٌ عربيٌّ مبتورٌ كما وقعَ فعلًا: آخرُ بايتٍ ناقصٌ من حرفٍ ثنائيِّ البايتات."""
    return "ت".encode("utf-8") + b"\xd8"


def test_البايتُ_التالفُ_وحدَهُ_لا_يُسقِطُ_الحارسَ(tmp_path):
    """بايتٌ غيرُ صالحٍ في UTF-8 داخلَ التاريخِ لا يُمحى — الحارسُ يحكُمُ ولا ينهارُ.

    عينُ العطبِ الحقيقيِّ (DISC-119): قبلَ W-565 كانَ هذا الفحصُ ينهارُ
    UnicodeDecodeError فتُسقَطُ الوظيفةُ كلُّها من CI.
    """
    clone = _clone(tmp_path)
    _commit(clone, {"w565_bad_byte.log": b"measurement\n" + _bad_byte_line() + b"\n"},
            "w565: بايتٌ تالفٌ واحدٌ في التاريخ")
    result = _run_gate(clone)
    assert result.returncode == 0, (result.stdout or "")[-1500:] + (result.stderr or "")[-500:]
    assert "PASS: 12/12" in result.stdout, result.stdout[-1500:]
    assert "لا مادة مفتاح خاص في التاريخ المنشور" in result.stdout


def test_المسحُ_ما_زالَ_يلتقطُ_المفتاحَ_في_التاريخِ_رغمَ_البايتِ_التالفِ(tmp_path):
    """الاستبدالُ لا يُعمي: كتلةُ PEM زُرِعَت ثم حُذِفَت منَ الشجرةِ — تُلتقَطُ منَ التاريخِ.

    كتلةُ المفتاحِ لا تُكتَبُ في هذا الملفِ قطعًا مُركَّبًا حتى لا يُسقِطَ
    ماسحُ الأسرارِ بفحصِ نفسِه (سابقةُ `test_w064_secret_scan_exceptions.py`).
    """
    clone = _clone(tmp_path)
    _commit(clone, {"w565_bad_byte.log": b"measurement\n" + _bad_byte_line() + b"\n"},
            "w565: بايتٌ تالفٌ واحدٌ في التاريخ")
    # تركيبٌ لا يُطوى مترجمًا: القيمُ منفصلةٌ في الثوابتِ فلا يحملُ «.pyc» الترويسةَ أبدًا
    head = ("-" * 5) + "".join(("BEGIN ", "PRIV", "ATE KEY")) + ("-" * 5)
    tail = ("-" * 5) + "".join(("END ", "PRIV", "ATE KEY")) + ("-" * 5)
    _commit(clone, {"w565_planted.txt": (head + "\nbody\n" + tail + "\n").encode("ascii")},
            "w565: زرعُ كتلةٍ ثم حذفُها منَ الشجرةِ")
    (clone / "w565_planted.txt").unlink()
    subprocess.run(["git", "-C", str(clone), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(clone), "-c", "user.name=w565", "-c", "user.email=w565@local",
         "commit", "--quiet", "-m", "w565: الحذفُ منَ الشجرةِ — التاريخُ يحتفظُ بالسطرِ"],
        check=True, capture_output=True,
    )
    result = _run_gate(clone)
    assert result.returncode == 1, result.stdout[-1500:]
    assert "لا مادة مفتاح خاص في التاريخ المنشور" in result.stdout
    assert "بلا مراجعة معلنة" in result.stdout, result.stdout[-1500:]
