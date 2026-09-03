#!/usr/bin/env python3
"""
حرسُ صدقِ أحجامِ الحزمِ المكتوبةِ — Suite Size Claim Guard

الهدف: إبقاءُ [`tools/governance/suite_size_inventory.py`] مُجرَّبًا بإعادةِ العَطبِ
       لا مُدَّعًى: كلُّ مخالفةٍ يُسمّيها المِقياسُ تُصنَعُ هنا صناعةً ويُثبَتُ أنَّه
       يراها، ثمَّ يُثبَتُ أنَّ المستودعَ نفسَه نظيفٌ بالجمعِ الحيِّ. فحرسٌ لا يُجرَّبُ
       عَطبُه دعوى (`DISC-046` · حُجِزَ في `W-120` · نزلَ في `W-121`).
النطاق: الحكمُ والقراءةُ. أمّا جمعُ الحزمِ حيًّا فيُشغَّلُ مرّةً واحدةً في فحصٍ واحدٍ
        لأنَّه يستدعي `pytest` في عمليّةٍ مستقلّةٍ.
المالك: tests/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-03
تاريخ آخر تعديل: 2026-09-03 (`W-122` — أُضيفَ حرسُ الفرقِ بينَ «تبعيّاتٌ خارجيّةٌ
                غائبةٌ يُسمّيها المُفسِّرُ» و«حزمةٌ معطوبةٌ»، بعدَ حكمِ CI 79 الأحمرِ)
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.governance.suite_size_inventory import (
    CLAIM_PATHS,
    REPO_ROOT,
    SUITES,
    Suite,
    SuiteCollectionFailed,
    SuiteDependenciesMissing,
    ClaimPathMissing,
    claims,
    collect_size,
    judge,
    live_sizes,
    missing_external_modules,
    needed_suites,
    verdict,
)

LIVE_SIZES = {"root": 2352, "services": 1428}


def _repo_with_handbook(tmp_path: Path, body: str) -> Path:
    """مستودعٌ مصنوعٌ لا يحملُ إلّا مسارَ الدعوى — العَطبُ يُصنَعُ ولا يُنتظَرُ."""
    target = tmp_path / CLAIM_PATHS[0]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8")
    return tmp_path


def test_المستودعُ_نفسُه_لا_يحملُ_رقمَ_حزمةٍ_ميّتًا():
    """الحكمُ الحيُّ على المستودعِ: كلُّ رقمٍ مكتوبٍ يُطابِقُ الجمعَ الآنَ."""
    code, problems = verdict(REPO_ROOT)
    assert code == 0, "رقمُ حزمةٍ مكتوبٌ خالفَ الجمعَ الحيَّ: " + " · ".join(problems)


def test_رقمٌ_ميّتٌ_يُرى_مخالفةً_مُسمّاةً(tmp_path):
    """إعادةُ العَطبِ: رقمٌ يُخالِفُ الجمعَ ⇒ `STALE_SUITE_CLAIM`."""
    repo = _repo_with_handbook(
        tmp_path, "| حزمةُ الجذر | **1748 نجحَت · 1 مُتخطّاة** | `pytest tests/ -q` |\n"
    )
    problems = judge(claims(repo), LIVE_SIZES)
    assert any(p.startswith("STALE_SUITE_CLAIM") for p in problems), problems


def test_الرقمُ_المُطابِقُ_للجمعِ_لا_يُشتكى_منه(tmp_path):
    """ولا يُشتكى من صادقٍ: مكتوبٌ = مقيسٌ ⇒ لا مخالفةَ (‏فالحرسُ ليسَ ضجيجًا)."""
    repo = _repo_with_handbook(
        tmp_path, "| حزمةُ الجذر | **2351 نجحَت · 1 مُتخطّاة** | `pytest tests/ -q` |\n"
    )
    assert judge(claims(repo), LIVE_SIZES) == []


def test_دعوى_بلا_متخطّاةٍ_لا_تُقرأُ_فتُعلَنُ(tmp_path):
    """«N نجحَت» بلا «مُتخطّاة» ⇒ `UNREADABLE_CLAIM_SHAPE` لا تخطٍّ صامتٌ."""
    repo = _repo_with_handbook(tmp_path, "| حزمةُ الجذر | **2351 نجحَت** |\n")
    problems = judge(claims(repo), LIVE_SIZES)
    assert any(p.startswith("UNREADABLE_CLAIM_SHAPE") for p in problems), problems


def test_رقمٌ_بلا_حزمةٍ_يُعرَفُ_يُعلَنُ(tmp_path):
    """رقمٌ لا تُقرأُ حزمتُه ⇒ `UNATTRIBUTED_SUITE_CLAIM`، فلا يمرُّ بلا نسَبٍ."""
    repo = _repo_with_handbook(tmp_path, "وقِيسَ أنَّ **900 نجحَت · 2 مُتخطّاة**.\n")
    problems = judge(claims(repo), LIVE_SIZES)
    assert any(p.startswith("UNATTRIBUTED_SUITE_CLAIM") for p in problems), problems


def test_تاريخيٌّ_بلا_قيدٍ_يَنسِبُه_يُعلَنُ(tmp_path):
    """إعفاءُ «كانَ المكتوبُ» مشروطٌ بقيدٍ ⇒ بلا قيدٍ `UNDATED_HISTORICAL_CLAIM`."""
    repo = _repo_with_handbook(
        tmp_path, "| حزمةُ الجذر | وكانَ المكتوبُ **1748 نجحَت · 1 مُتخطّاة** |\n"
    )
    problems = judge(claims(repo), LIVE_SIZES)
    assert any(p.startswith("UNDATED_HISTORICAL_CLAIM") for p in problems), problems


def test_تاريخيٌّ_منسوبٌ_إلى_قيدٍ_يُعفى(tmp_path):
    """ومنسوبٌ إلى قيدٍ يُقرأُ ماضيًا فلا يُقاسُ بالجمعِ الحاضرِ."""
    repo = _repo_with_handbook(
        tmp_path,
        "| حزمةُ الجذر | **2351 نجحَت · 1 مُتخطّاة** · وكانَ المكتوبُ "
        "**1748 نجحَت · 1 مُتخطّاة** (‏قِيسَ W-030) |\n",
    )
    assert judge(claims(repo), LIVE_SIZES) == []


def test_حزمةٌ_لم_تُجمَعْ_لا_تمرُّ_بصمتٍ(tmp_path):
    """غيابُ حجمٍ مقيسٍ ⇒ `SUITE_UNCOLLECTABLE`، لا «لا مخالفةَ» كاذبةٌ."""
    repo = _repo_with_handbook(
        tmp_path, "| حزمةُ الجذر | **2351 نجحَت · 1 مُتخطّاة** |\n"
    )
    problems = judge(claims(repo), {})
    assert any(p.startswith("SUITE_UNCOLLECTABLE") for p in problems), problems


def test_جمعٌ_فاشلٌ_يُرفَعُ_ولا_يُبتلَعُ(tmp_path):
    """هدفٌ لا يُجمَعُ يرفعُ `SuiteCollectionFailed` — الابتلاعُ إخفاءُ فشلٍ."""
    absent = Suite(key="absent", target="tests/لا-وجودَ-له", marker="حزمةُ الجذر")
    with pytest.raises(SuiteCollectionFailed):
        collect_size(absent, REPO_ROOT)


def test_مسارُ_دعوى_غائبٌ_يُرفَعُ(tmp_path):
    """نطاقٌ مُعلَنٌ لا يوجدُ ⇒ رفعٌ لا صمتٌ، فالنطاقُ الناقصُ لا يُقاسُ عليه."""
    with pytest.raises(ClaimPathMissing):
        claims(tmp_path)


def test_حزمةٌ_غيرُ_مُثبَّتةٍ_تُعفى_بسببٍ_مكتوبٍ(tmp_path):
    """الإعفاءُ البيئيُّ مشروطٌ بسببٍ مكتوبٍ، ولا يُصطنَعُ إخفاقٌ سببُه البيئةُ."""
    repo = _repo_with_handbook(
        tmp_path,
        "| حزمةُ الخدماتِ | **1356 نجحَت · 27 مُتخطّاة** |\n",
    )
    assert judge(claims(repo), {}, frozenset({"services"})) == []
    assert judge(claims(repo), {}) != []


def test_كلُّ_حزمةٍ_قابلةٍ_للغيابِ_تحملُ_سببَها_مكتوبًا():
    """حزمةٌ لها `probe` بلا سببٍ مكتوبٍ إعفاءٌ صامتٌ — فيُشتَرَطُ السببُ."""
    silent = [s.key for s in SUITES if s.probe and not s.unmeasured_reason.strip()]
    assert not silent, f"إعفاءٌ بلا سببٍ مكتوبٍ: {silent}"


def test_لا_تُجمَعُ_حزمةٌ_لا_رقمَ_لها(tmp_path):
    """الجمعُ الحيُّ لا يُشغَّلُ إلّا لحزمةٍ نُسِبَ إليها رقمٌ حيٌّ — كلفةٌ تُقاسُ بحاجةٍ."""
    repo = _repo_with_handbook(
        tmp_path, "| حزمةُ الجذر | **2351 نجحَت · 1 مُتخطّاة** |\n"
    )
    assert needed_suites(claims(repo)) == {"root"}


def _suite_in(repo: Path, key: str, body: str) -> Suite:
    """حزمةٌ مصنوعةٌ في مستودعٍ مصنوعٍ — يُصنَعُ سببُ الفشلِ لا يُنتظَرُ."""
    target = repo / key
    target.mkdir(parents=True, exist_ok=True)
    (target / f"test_{key}.py").write_text(body, encoding="utf-8")
    return Suite(
        key=key,
        target=key,
        marker="حزمةُ الجذر",
        probe=None,
        unmeasured_reason="سببٌ مكتوبٌ للتجربةِ",
    )


def test_أسماءُ_الحزمِ_الغائبةِ_تُقرأُ_ولا_تُخمَّنُ():
    """السببُ يُقرأُ من خرجِ المُفسِّرِ، وحزمُ المستودعِ نفسِها ليست نقصَ بيئةٍ."""
    output = (
        "ModuleNotFoundError: No module named 'fastapi'\n"
        "ModuleNotFoundError: No module named 'sqlalchemy.orm'\n"
        "ModuleNotFoundError: No module named 'amos_federation.common'\n"
    )
    assert missing_external_modules(output) == ("fastapi", "sqlalchemy")
    assert missing_external_modules("collected 0 items") == ()


def test_تبعيّةٌ_خارجيّةٌ_غائبةٌ_تُعفي_بإعلانٍ_يُسمّيها(tmp_path):
    """جمعٌ يفشلُ ويُسمّي حزمةً خارجيّةً غائبةً ⇒ إعفاءٌ مُعلَنٌ باسمِها لا صمتٌ."""
    suite = _suite_in(
        tmp_path, "svc", "import حزمة_لا_وجود_لها_في_البيئة  # noqa: F401\n"
    )
    with pytest.raises(SuiteDependenciesMissing) as raised:
        collect_size(suite, tmp_path)
    assert raised.value.modules == ("حزمة_لا_وجود_لها_في_البيئة",)
    assert "حزمة_لا_وجود_لها_في_البيئة" in str(raised.value)


def test_حزمةٌ_معطوبةٌ_لا_تُعفى_بل_تُرفَعُ_إخفاقًا(tmp_path):
    """فشلُ جمعٍ لا يُسمّي حزمةً غائبةً عَطبٌ مُسمًّى — ولا يُبتلَعُ إعفاءً."""
    suite = _suite_in(tmp_path, "broken", "def معطوب(:\n    pass\n")
    with pytest.raises(SuiteCollectionFailed) as raised:
        collect_size(suite, tmp_path)
    assert "SUITE_UNCOLLECTABLE" in str(raised.value)


def test_الإعفاءُ_يُدرَجُ_في_المقيسِ_بسببٍ_يحملُ_الأسماءَ(monkeypatch, tmp_path):
    """`live_sizes` تُعفي ما تعذَّرَ جمعُه لتبعيّةٍ غائبةٍ، وتكتبُ اسمَها في سببِه."""
    repo = _repo_with_handbook(
        tmp_path,
        "| حزمةُ الخدماتِ | **1356 نجحَت · 27 مُتخطّاة** |\n",
    )
    وهمية = Suite(
        key="services",
        target="لا-يوجد",
        marker="حزمةُ الخدمات",
        probe=None,
        unmeasured_reason="سببٌ مكتوبٌ للتجربةِ",
    )

    def _يرفعُ_الغياب(suite, repo=None):
        raise SuiteDependenciesMissing(suite.key, ("fastapi", "sqlalchemy"))

    monkeypatch.setattr(
        "tools.governance.suite_size_inventory.SUITES", (وهمية,), raising=True
    )
    monkeypatch.setattr(
        "tools.governance.suite_size_inventory.collect_size",
        _يرفعُ_الغياب,
        raising=True,
    )
    sizes, unmeasured, reasons = live_sizes(claims(repo), repo)
    assert sizes == {}
    assert unmeasured == frozenset({"services"})
    assert "fastapi" in reasons["services"] and "sqlalchemy" in reasons["services"]
    assert judge(claims(repo), sizes, unmeasured) == []
