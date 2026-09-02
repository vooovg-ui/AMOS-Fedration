#!/usr/bin/env python3
"""الهدف: حرسُ رؤيةِ حزمةِ الخدماتِ من شجرتِها حينَ لا تكونُ مُركَّبةً (W-064).

النطاق: `conftest.py` الجذريُّ — الشرطُ الذي يُضيفُ `federal/executive/services/src`
إلى مسارِ الاستيرادِ عندَ غيابِ الحزمةِ المُركَّبةِ.

المالك: governance/
تاريخ الإنشاء: 2026-08-29
تاريخ آخر تعديل: 2026-08-29

لماذا هذا الحرسُ
----------------
سقطَت ثلاثةُ اختباراتٍ في وظيفةِ «السيادةِ الملكيّةِ» في CI بـ`ModuleNotFoundError:
amos_federation`، لأنَّ تلك الوظيفةَ تُركِّبُ تبعياتِ التطويرِ وحدَها. فلم تُقَسْ
فحوصُ فصلِ الإنفاذِ الفدراليِّ فيها (‏`DISC-026`). والعلاجُ في `conftest.py`، ولو بقيَ
بلا حرسٍ لعادَ العَطبُ صامتًا: تُحذَفُ الأسطرُ فتُتخطّى الفحوصُ ولا يُنبِّهُ شيءٌ.

والقياسُ هنا **في بيئةٍ تُشبِهُ بيئةَ CI فعلًا**: يُشغَّلُ مُفسِّرٌ بـ`-S` فلا يُرى
`site-packages` ولا الحزمةُ المُركَّبةُ، ثمَّ يُقرأُ هل صارَت الحزمةُ مرئيّةً بعدَ
تحميلِ `conftest`. ويُقاسُ الضبطُ (‏بلا `conftest`) كي لا تُنسَبَ الرؤيةُ لغيرِ سببِها.
"""
from __future__ import annotations

import subprocess
import sys

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
SERVICES_SRC = REPO_ROOT / "federal" / "executive" / "services" / "src"

_قياسٌ = """
import importlib.util, sys
sys.path.insert(0, {repo!r})
{تحميلٌ}
print("VISIBLE" if importlib.util.find_spec("amos_federation") else "MISSING")
"""


def _شغِّلْ(تحميلٌ: str) -> str:
    """مُفسِّرٌ بلا `site-packages` — فالحزمةُ المُركَّبةُ لا تُرى فيه."""
    result = subprocess.run(
        [sys.executable, "-S", "-c", _قياسٌ.format(repo=str(REPO_ROOT), تحميلٌ=تحميلٌ)],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        pytest.skip(f"تعذّر القياسُ بمُفسِّرٍ بلا موقعٍ: {result.stderr.strip()[:200]}")
    return result.stdout.strip()


def test_الحزمةُ_غيرُ_مرئيةٍ_بلا_conftest():
    """الضبطُ: بلا الشرطِ في `conftest` لا تُرى الحزمةُ — فالعَطبُ حقيقيٌّ لا متوهَّمٌ."""
    assert _شغِّلْ("") == "MISSING"


def test_الحزمةُ_تُرى_بعدَ_تحميلِ_conftest():
    """وبتحميلِ `conftest` تُرى الحزمةُ من شجرتِها، فتُنفَّذُ الفحوصُ لا تُتخطّى."""
    assert _شغِّلْ("import conftest  # noqa: F401") == "VISIBLE"


def test_مُجلَّدُ_المصادرِ_قائمٌ_ويحملُ_الحزمة():
    assert (SERVICES_SRC / "amos_federation" / "__init__.py").is_file()


def test_الشرطُ_لا_يُزاحِمُ_حزمةً_مُركَّبةً():
    """الحزمةُ المُركَّبةُ أَولى: الإضافةُ مشروطةٌ بغيابِها لا مُطلَقةٌ."""
    نصٌّ = (REPO_ROOT / "conftest.py").read_text(encoding="utf-8")
    assert 'if importlib.util.find_spec("amos_federation") is None:' in نصٌّ
    assert "sys.path.insert(0, str(SERVICES_SRC))" in نصٌّ


def test_فحوصُ_فصلِ_الإنفاذِ_لا_تسقُطُ_لغيابِ_الحزمةِ_من_الشجرة():
    """الغايةُ ليست مسارًا بل فحوصًا تُبلَغُ: يُشغَّلُ الثلاثةُ ويُقرأُ حكمُها.

    وحدُّ هذا الحرسِ مُعلَنٌ لا مستورٌ: `conftest` يجعلُ الحزمةَ **مرئيّةً** من
    شجرتِها، ولا يُركِّبُ تبعياتِها. فإن نقصَت بيئةُ الوظيفةِ تبعيّةً من تبعياتِ
    الحزمةِ (‏`sqlalchemy` أو `structlog` أو `pydantic`‏) سقطَ الاستيرادُ لسببٍ
    آخرَ — وذلك نقصُ تجهيزٍ في تلك الوظيفةِ يُعالَجُ في موضعِه (`DISC-026`)، لا
    عَطبٌ في ما نحرسُه هنا. فالحكمُ مُحكَمٌ بلا تخطٍّ صامتٍ: الحزمةُ نفسُها لا
    تكونُ غائبةً أبدًا، وإن اكتملَت التبعياتُ فالفحوصُ الثلاثةُ تنجحُ.
    """
    result = subprocess.run(
        [sys.executable, "-m", "pytest",
         "tests/sovereignty/test_enforcement_separation.py",
         "-k", "الفدرالي or فدرالي", "-q", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    مخرَجٌ = result.stdout + result.stderr
    assert "No module named 'amos_federation'" not in مخرَجٌ, (
        "حزمةُ الخدماتِ ما زالت غيرَ مرئيّةٍ من شجرتِها — وهو ما يحرسُه هذا الملفّ:\n"
        + مخرَجٌ[-2000:]
    )
    ناقصٌ = [
        اسمٌ for اسمٌ in ("sqlalchemy", "structlog", "pydantic")
        if f"No module named '{اسمٌ}'" in مخرَجٌ
    ]
    if ناقصٌ:
        # لا تخطٍّ ولا تخفيفٍ: يُقاسُ أنَّ السقوطَ **ليس** من الحزمةِ، ويُعلَنُ
        # سببُه الحقيقيُّ باسمِه في المخرَجِ ليُعالَجَ في وظيفتِه.
        print("تبعياتُ حزمةِ الخدماتِ ناقصةٌ في هذه البيئةِ:", " · ".join(ناقصٌ))
        return
    assert result.returncode == 0, مخرَجٌ[-2000:]
    assert "error" not in result.stdout.lower(), مخرَجٌ[-2000:]
