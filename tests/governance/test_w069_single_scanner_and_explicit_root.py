"""الهدف: حرسُ ما استُنقِذَ من فرعٍ لم يُدمَج — مصدرُ حقيقةٍ واحدٌ لحدِّ مادةِ
المفتاحِ الخاصِّ في شجرةِ العملِ، ومحلُّ قياسٍ يُمَرَّرُ صراحةً لا يُخمَّنُ.

الحدُّ المحروسُ هنا حدَّانِ مقيسانِ لا مُدَّعيانِ:

  أ · بوّابةُ السيادةِ 6 في `.github/workflows/ci.yml` لا تُعيدُ كتابةَ ماسحِ
    الأسرارِ بيدٍ، بل تُنادي الماسحَ المرجعيَّ وحدَه. ومصدرا حقيقةٍ لحدٍّ واحدٍ
    بابُ افتراقٍ: أحدُهما يُخفَّفُ ولا يُلاحَظُ، والآخرُ يُبلِّغُ أحمرًا كاذبًا
    فيُقالُ «عطبُ قياسٍ» ويُطوى. وكانَ ذلك مقيسًا في `DISC-021`.

  ب · بوّابةُ حوكمةِ العملِ تقبَلُ `--repo-root` فتقيسُ الشجرةَ المُمَرَّرةَ لا
    الشجرةَ التي فيها ملفُّها. وليسَ ذاك رايةَ تخطٍّ: الفحوصُ عينُها تُجرَى
    كاملةً — وإنما يُعلَنُ محلُّ القياسِ. وكانَ ذلك مقيسًا في `DISC-022`.

وكِلا الحدَّينِ كانَ قد صُلِحَ على فرعٍ لم يُدمَجْ قطُّ إلى `main` (`DISC-034`)،
فبقيَ العطبُ قائمًا في الفرعِ المنشورِ وحُلَّ مرّتَينِ حلًّا مختلفًا. فهذا
الحرسُ يمنعُ رجوعَ الحدَّينِ إلى ما كانا عليه.

حدُّ هذا الحرسِ — مُعلَنٌ لا مطويٌّ: يقيسُ نصَّ `ci.yml` وسلوكَ الأداتَينِ، ولا
يقيسُ أنَّ الفرعَ `develop` صارَ مدموجًا — ذاك قرارُ مستودعٍ لا يملكُه اختبارٌ.

النطاق: حرسُ حوكمة
المالك: التنفيذ (بتفويضِ المالك)
تاريخ الإنشاء: 2026-08-30
تاريخ آخر تعديل: 2026-08-30
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
CI_PATH = REPO_ROOT / ".github" / "workflows" / "ci.yml"
SECRET_TOOL = REPO_ROOT / "tools" / "crown" / "verify_secret_boundaries.py"
WORK_TOOL = REPO_ROOT / "tools" / "governance" / "check_work_governance.py"

# النمطُ مُركَّبٌ من أجزاءَ كي لا يحملَ هذا الملفُّ نفسُه مادةَ مفتاحٍ.
_DASHES = "-" * 5
_PEM_HEAD = "BEGIN " + "PRIVATE KEY"

GATE6_NAME = "بوابة 6 — لا مفتاح خاص للملك في المستودع"


def _gate6_block() -> str:
    """نصُّ خطوةِ البوّابةِ السادسةِ وحدَها، من عنوانِها إلى عنوانِ ما بعدَها."""
    text = CI_PATH.read_text(encoding="utf-8")
    start = text.index(GATE6_NAME)
    nxt = text.index("- name:", start + len(GATE6_NAME))
    return text[start:nxt]


# ── أ · مصدرُ حقيقةٍ واحدٌ لحدِّ مادةِ المفتاحِ ───────────────────────────────


def test_بوابةُ_السيادةِ_السادسةُ_تُنادي_الماسحَ_المرجعيَّ_لا_ماسحًا_ثانيًا() -> None:
    block = _gate6_block()
    assert "verify_secret_boundaries.py --tree-pem-only" in block, (
        "البوّابةُ 6 لا تُنادي الماسحَ المرجعيَّ — عادَ لحدٍّ واحدٍ مصدرا حقيقةٍ"
    )


def test_لا_ماسحَ_مكتوبًا_بيدٍ_في_خطوةِ_البوابةِ_السادسة() -> None:
    """الحدُّ ليسَ «وُجِدَ النداءُ» بل «لا ماسحَ ثانيًا معَه»."""
    block = _gate6_block()
    assert not re.search(r"\bgrep\b", block), (
        f"ماسحٌ مكتوبٌ بيدٍ في خطوةِ البوّابةِ 6:\n{block}"
    )
    assert _PEM_HEAD not in block, "نمطُ كتلةِ PEM مكتوبٌ في مِلفِّ التكاملِ من جديدٍ"


def test_الرايةُ_تُشغِّلُ_البوابةَ_ولا_تُسقِطُها(tmp_path: Path) -> None:
    """راية النطاقِ ليست تخطِّيًا: تُشغِّلُ الفحصَ، وتَحمَرُّ على مادةِ مفتاحٍ حقيقيّةٍ."""
    out = subprocess.run(
        [sys.executable, str(SECRET_TOOL), "--tree-pem-only"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    assert out.returncode == 0, out.stdout + out.stderr
    assert "لا مادة مفتاح خاص في شجرة العمل" in out.stdout, (
        "الرايةُ مرَّت بلا أن تُعلِنَ أنَّ الفحصَ أُجرِيَ — نجاحٌ بلا بيانٍ لا يُثبِتُ فحصًا"
    )
    assert "PASS: 1/1" in out.stdout, "نطاقُ الرايةِ غيرُ مُعلَنٍ في المَخرَجِ"


def test_الرايةُ_تحمَرُّ_على_مادةِ_مفتاحٍ_مزروعةٍ(tmp_path: Path) -> None:
    """أجدى برهانٍ على أنَّ البوّابةَ تعملُ: مُحاولةُ نقضِها بمادةٍ مزروعةٍ."""
    planted = REPO_ROOT / "tmp_planted_key_probe.txt"
    assert not planted.exists(), "مِسبارٌ سابقٌ لم يُنظَّف"
    planted.write_text(f"{_DASHES}{_PEM_HEAD}{_DASHES}\n", encoding="utf-8")
    try:
        out = subprocess.run(
            [sys.executable, str(SECRET_TOOL), "--tree-pem-only"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=False,
        )
    finally:
        planted.unlink()
    assert out.returncode == 1, "مادةُ مفتاحٍ مزروعةٌ لم تُحمِّرِ البوّابةَ — البوّابةُ دعوى"
    assert "tmp_planted_key_probe.txt" in out.stdout


def test_رايةٌ_غيرُ_معروفةٍ_تُرفَضُ_ولا_تُطوى() -> None:
    out = subprocess.run(
        [sys.executable, str(SECRET_TOOL), "--no-such-flag"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    assert out.returncode == 2, out.stdout + out.stderr


# ── ب · محلُّ القياسِ يُمَرَّرُ صراحةً ───────────────────────────────────────


def test_بوابةُ_العملِ_تقبَلُ_جذرًا_مُمَرَّرًا() -> None:
    out = subprocess.run(
        [sys.executable, str(WORK_TOOL), "--help"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    assert out.returncode == 0, out.stdout + out.stderr
    assert "--repo-root" in out.stdout, "محلُّ القياسِ لا يُمَرَّرُ صراحةً — عادَ يُخمَّنُ"


def test_جذرٌ_ليسَ_مجلَّدًا_يُرفَضُ_رفضًا_مُعلَنًا(tmp_path: Path) -> None:
    ghost = tmp_path / "لا-وجودَ-له"
    out = subprocess.run(
        [sys.executable, str(WORK_TOOL), "--self-check", "--repo-root", str(ghost)],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    assert out.returncode == 2, out.stdout + out.stderr
    assert "--repo-root" in out.stderr


def test_الجذرُ_المُمَرَّرُ_هو_المقيسُ_فعلًا(tmp_path: Path) -> None:
    """شجرةٌ خاليةٌ من السجلّاتِ تُحمِّرُ بغيابِها، فيُعلَمُ أنَّها هي المقيسةُ."""
    empty = tmp_path / "شجرةٌ-خاليةٌ"
    empty.mkdir()
    out = subprocess.run(
        [sys.executable, str(WORK_TOOL), "--self-check", "--repo-root", str(empty)],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    assert out.returncode != 0, (
        "شجرةٌ بلا سجلّاتٍ مرَّت — فالمقيسُ كانَ المستودعَ الحقيقيَّ لا الجذرَ المُمَرَّرَ"
    )


def test_تعيينُ_الجذرِ_ليسَ_رايةَ_تخطٍّ() -> None:
    """الحدُّ الأخلاقيُّ مقروءٌ في المصدرِ: الدالّةُ تُعلِنُ أنّها لا تُسقِطُ فحصًا."""
    src = WORK_TOOL.read_text(encoding="utf-8")
    assert "def set_repo_root" in src
    body = src[src.index("def set_repo_root") : src.index("def resolve_merge_base")]
    assert "تخط" in body, "تعيينُ الجذرِ بلا إعلانِ حدِّه يُقرأُ رايةَ تخطٍّ"


@pytest.mark.parametrize("flag", ["--force", "--skip", "--no-verify", "--bypass"])
def test_لا_رايةَ_تخطٍّ_في_الأداتَينِ(flag: str) -> None:
    for tool in (SECRET_TOOL, WORK_TOOL):
        assert flag not in tool.read_text(encoding="utf-8"), f"{flag} في {tool.name}"
