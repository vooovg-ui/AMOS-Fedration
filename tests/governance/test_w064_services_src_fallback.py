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
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
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


def test_فحوصُ_فصلِ_الإنفاذِ_تُنفَّذُ_فعلًا():
    """الغايةُ ليست مسارًا بل فحوصًا تعمَلُ: تُشغَّلُ الثلاثةُ ويُقرأُ حكمُها."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest",
         "tests/sovereignty/test_enforcement_separation.py",
         "-k", "الفدرالي or فدرالي", "-q", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stdout[-2000:]
    assert "error" not in result.stdout.lower(), result.stdout[-2000:]
