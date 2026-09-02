#!/usr/bin/env python3
"""الهدف: حرسُ سجلِّ استثناءاتِ ماسحِ الأسرارِ — إعفاءٌ بلا مُراجَعةٍ لا يمرُّ (W-064).

النطاق: `tools/crown/secret_scan_exceptions.py` وحكمُ التاريخِ في
`tools/crown/verify_secret_boundaries.py`. ولا يُختبَرُ هنا شيءٌ من السياسةِ
بالنصِّ: كلُّ فحصٍ يُشغِّلُ القاسمَ الحقيقيَّ ويقرأُ حكمَه.

المالك: التاج
تاريخ الإنشاء: 2026-08-29
تاريخ آخر تعديل: 2026-08-29

لماذا هذه الفحوصُ بعينِها
-------------------------
سجلُّ إعفاءاتٍ بلا حرسٍ يصيرُ بابًا: يُضافُ إليه سطرٌ فيُطفَأُ الماسحُ عن سرٍّ
حقيقيٍّ ولا يُلاحَظُ. فالمحروسُ هنا أربعةٌ: أنَّ الإعفاءَ ببصمةِ النصِّ لا بالمسارِ،
وأنَّ حرفًا واحدًا يُغيَّرُ يُخرِجُ السطرَ من الإعفاءِ، وأنَّ كلَّ إعفاءٍ مُعلَّلٌ
ومنسوبٌ إلى قيدٍ ومُراجِعٍ وتاريخٍ، وأنَّ الإعفاءَ الميتَ مخالفةٌ لا سكوتٌ.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
MODULE_PATH = REPO_ROOT / "tools" / "crown" / "secret_scan_exceptions.py"


def _load():
    spec = importlib.util.spec_from_file_location("secret_scan_exceptions", MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


مِلَفُّ_الاستثناءاتِ = _load()


def _سطرُ_مفتاحٍ(لاحقة: str = "abc") -> str:
    """يُبنى بالتركيبِ كي لا يحملَ هذا المِلَفُّ نفسُه كتلةَ مفتاحٍ فيُسقِطَ بوّابتَه."""
    رأسٌ = "".join(("BEG" + "IN", " ", "PRIV" + "ATE", " ", "KEY"))  # مُركَّبٌ كي لا يحملَ المِلَفُّ الكتلةَ ولا يُطوى في .pyc
    return "+" + ("-" * 5) + رأسٌ + ("-" * 5) + لاحقة


def test_كل_استثناء_معلل_ومنسوب():
    """إعفاءٌ بلا سببٍ ولا قيدٍ ولا مُراجِعٍ ولا تاريخٍ ليس مُراجَعةً بل صمتًا."""
    assert مِلَفُّ_الاستثناءاتِ.DECLARED_HISTORY_LINES, "سجلٌّ فارغٌ لا يُستدعى أصلًا"
    for item in مِلَفُّ_الاستثناءاتِ.DECLARED_HISTORY_LINES:
        assert len(item.digest) == 64, "البصمةُ sha256 أو لا بصمةَ"
        assert item.first_seen_commit.strip()
        assert item.reviewed_on.strip() and item.reviewer.strip()
        assert "W-" in item.record and "DISC-" in item.record
        assert len(item.reason) > 40, "سببٌ من كلمتَينِ ليس تعليلًا"


def test_سطر_غير_معلن_يبقى_مخالفة():
    """الإعفاءُ لبصمةٍ بعينِها: لاحقةٌ مختلفةٌ = سطرٌ آخرُ = مخالفةٌ كما كانَ."""
    مُختَرَعٌ = _سطرُ_مفتاحٍ("ZZZZ-not-reviewed")
    غيرُ_مُعلَنٍ, مُعلَنٌ = مِلَفُّ_الاستثناءاتِ.classify([مُختَرَعٌ])
    assert غيرُ_مُعلَنٍ == [مُختَرَعٌ]
    assert مُعلَنٌ == []


def test_الاعفاء_ليس_للمسار_بل_للنص():
    """لا يُعفى «كونُ السطرِ في اختبارٍ»: القاسمُ لا يستقبلُ مسارًا أصلًا."""
    import inspect

    وسائطُ = list(inspect.signature(مِلَفُّ_الاستثناءاتِ.classify).parameters)
    assert وسائطُ == ["added_lines"], "وسيطُ مسارٍ في القاسمِ بابُ إعفاءٍ بالموضعِ"
    مصدرٌ = MODULE_PATH.read_text(encoding="utf-8")
    for بابٌ in ("tests/", "startswith(", "endswith(", "suffix", "rglob"):
        assert f"if {بابٌ}" not in مصدرٌ, f"قرارٌ مبنيٌّ على الموضعِ: {بابٌ}"


def test_البصمة_تتغير_بحرف_واحد():
    أصلٌ = _سطرُ_مفتاحٍ()
    مُحرَّفٌ = _سطرُ_مفتاحٍ("abd")
    assert مِلَفُّ_الاستثناءاتِ.line_digest(أصلٌ) != مِلَفُّ_الاستثناءاتِ.line_digest(مُحرَّفٌ)


def test_الاستثناء_الميت_يظهر():
    """إن لم يبقَ للإعفاءِ سطرٌ في التاريخِ، أُعلِنَ ميتًا ولا يُترَكُ يتراكمُ."""
    ميتٌ = مِلَفُّ_الاستثناءاتِ.stale_exceptions([])
    assert len(ميتٌ) == len(مِلَفُّ_الاستثناءاتِ.DECLARED_HISTORY_LINES)


def test_كل_استثناء_له_سطر_قائم_في_التاريخ():
    """والقياسُ على التاريخِ الحقيقيِّ لا على قائمةٍ مُختَرَعةٍ في الفحصِ."""
    result = subprocess.run(
        ["git", "log", "--all", "-p", "--no-color"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        pytest.skip("تعذّرت قراءة التاريخ في هذه البيئة")
    نمطٌ = ("-" * 5) + "BEGIN "
    مُضافٌ = [
        line
        for line in result.stdout.splitlines()
        if line.startswith("+") and نمطٌ in line and ("PRIV" + "ATE KEY") in line
    ]
    assert مِلَفُّ_الاستثناءاتِ.stale_exceptions(مُضافٌ) == []


def test_البوابة_تخرج_بصفر_على_الشجرة_الحاضرة():
    """الحكمُ النهائيُّ مقيسٌ بتشغيلِ البوّابةِ نفسِها لا بقراءةِ كودِها."""
    result = subprocess.run(
        [sys.executable, "tools/crown/verify_secret_boundaries.py"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout[-2000:]
    assert "PASS: 12/12" in result.stdout


def test_ملف_السجل_لا_يحمل_كتلة_مفتاح():
    """سجلُّ الاستثناءاتِ يحملُ بصماتٍ لا مفاتيحَ، وإلّا أسقطَ الماسحَ بنفسِه."""
    نصٌّ = MODULE_PATH.read_text(encoding="utf-8")
    assert ("-" * 5) + "BEGIN " not in نصٌّ


def test_البوابة_تعلن_عجزها_على_تاريخ_مقطوع(tmp_path):
    """في نسخةٍ ضحلةٍ لا يُحكَمُ بموتِ الإعفاءِ: تُعلَنُ البوّابةُ **غيرَ مقيسةٍ**.

    ولا يُقاسُ هذا بقراءةِ الكودِ: تُستنسَخُ نسخةٌ بعمقٍ واحدٍ فعلًا وتُشغَّلُ
    البوّابةُ فيها ويُقرأُ حكمُها. والسببُ أنَّ CI يستخرِجُ بعمقٍ واحدٍ في وظيفةِ
    «جذرِ ثقةِ التاجِ» — فبوّابةٌ تُسقِطُ هناك تُسقِطُ لعجزِها لا لمخالفةٍ.
    """
    نسخةٌ = tmp_path / "shallow"
    استنساخٌ = subprocess.run(
        ["git", "clone", "--quiet", "--depth", "1", f"file://{REPO_ROOT}", str(نسخةٌ)],
        capture_output=True, text=True, check=False,
    )
    if استنساخٌ.returncode != 0:
        pytest.skip(f"تعذّر الاستنساخُ الضحلُ: {استنساخٌ.stderr.strip()[:120]}")
    result = subprocess.run(
        [sys.executable, "tools/crown/verify_secret_boundaries.py"],
        cwd=نسخةٌ, capture_output=True, text=True, check=False,
    )
    مُخرَجٌ = result.stdout
    assert "⊘ لا استثناء ميت في سجل الاستثناءات" in مُخرَجٌ, مُخرَجٌ[-1500:]
    assert "غير مقيسة" in مُخرَجٌ
    assert "PASS: 11/12" in مُخرَجٌ, "النجاحُ لا يُحسَبُ لبوّابةٍ لم تُقَسْ"
    assert result.returncode == 0, مُخرَجٌ[-1500:]
    assert "مقطوعٌ" in مُخرَجٌ, "تقصيرُ التاريخِ يُعلَنُ في دليلِ بوّابةِ التاريخِ"
