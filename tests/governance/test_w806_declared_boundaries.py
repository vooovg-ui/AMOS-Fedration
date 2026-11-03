"""الهدف: حرسُ الحدودِ المُعلَنةِ في `common/` — القائمةُ المغلقةُ لا تُوسَّعُ ولا
تُقادَمُ ولا تُسقِطُ صامتًا (قرارا المالكِ ج-1(أ) و(د-1) · Q-87 · W-806).

النطاق: `DECLARED_BOUNDARIES` في `tools/audit/sovereign_write_inventory.py`
وقسمُ «حدودٌ مُعلَنةٌ في common/» في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`
والمواضعُ السبعةُ الحيّةُ في `federal/executive/services/src/amos_federation/common/`
— لا غيرَ: لا يُثبِتُ هذا الحرسُ وجاهةَ الحدودِ (ذاك حكمُ مالكٍ مسجَّلٌ) بل
يبقيها مطبوعةً ومطابقةً لبعضِها بعضًا.

المالك: governance/
تاريخ الإنشاء: 2026-11-03
تاريخ آخر تعديل: 2026-11-03

## لماذا هذا الحرسُ موجود

قرارُ المالكِ في Q-87 قال: هذهِ السبعةُ **حدودٌ لا دَينًا** — تُعَدُّ في حقلٍ
مستقلٍّ مطبوعٍ (`declared_boundary_operations`) وتخرجُ من `non_sovereign_write_operations`.
وبلا حرسٍ تتحوّلُ القائمةُ إلى أداةِ إخفاءٍ: يُضافُ مدخلٌ فلا موقعَ له، أو يُحذفُ
موضعٌ من الشِّفرةِ ويبقى مدخلُه قائمًا، أو يُزاحُ الاستثناءُ من `summarize` فيعودُ
الدَّينُ يحسبُها والرقمُ يكذِبُ. فثلاثةُ أضلاعٍ يطابقُ بعضُها بعضًا: القائمةُ في
الأداةِ · الجدولُ في السجلِّ السياديّ · المواضعُ الحيّةُ في الشجرة.

## حدُّ صدقِ هذا الحرس

بنيويٌّ بالكاملِ: `collect` على الشجرةِ الحيّةِ + `validate_declared_boundaries`
على السجلِّ نصًّا + معادلةُ الهويّةِ من `summarize` نفسِها — لا رقمَ منسوخًا في
هذا الملفِ ولا قراءةَ قياسٍ منشورًا. والمضاعفُ الحيُّ مقيسٌ في `evidence/W-806/mutations/`.
"""

from __future__ import annotations

import importlib.util
import sys
from types import ModuleType

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
INVENTORY_TOOL = REPO_ROOT / "tools" / "audit" / "sovereign_write_inventory.py"
REGISTER = REPO_ROOT / "docs" / "audit" / "SOVEREIGN_DECISION_REGISTER.md"

#: المواضعُ السبعةُ بأسمائِها الكاملةِ — (الملفُّ داخلَ common/ · المالك · الدالّة)
#: ومرجعُ قرارِ كلٍّ منها. هذا هو التعريفُ المرجعيُّ للقائمةِ المغلقةِ (§ 2).
EXPECTED_BOUNDARIES: dict[tuple[str, str, str], str] = {
    ("persistent.py", "PersistentAuditStore", "append"): "ج-1(أ)",
    ("durable_event_bus.py", "DurableEventBus", "publish"): "ج-1(أ)",
    ("event_bus.py", "EventBus", "publish"): "ج-1(أ)",
    ("events.py", "EventPublisher", "publish"): "ج-1(أ)",
    ("database.py", "-", "ensure_added_columns"): "د-1",
    ("persistent.py", "PersistentSystemStateStore", "get"): "د-1",
    ("database.py", "-", "db_cursor"): "د-1",
}


def _load_inventory_tool() -> ModuleType:
    """تحميلُ أداةِ الجردِ بمسارِها مع تسجيلِها في `sys.modules` (سابقةُ step7)."""
    spec = importlib.util.spec_from_file_location(
        "sovereign_write_inventory", INVENTORY_TOOL
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["sovereign_write_inventory"] = module
    spec.loader.exec_module(module)
    return module


def test_القائمةُ_المغلقةُ_سبعةٌ_بأسمائِها_الكاملةِ() -> None:
    tool = _load_inventory_tool()
    assert dict(tool.DECLARED_BOUNDARIES) == EXPECTED_BOUNDARIES, (
        "القائمةُ المغلقةُ تغيَّرَت: المدخلُ أو المرجعُ — القرارُ للسجلِّ السياديّ "
        "لا للشِّفرةِ الصامتة."
    )
    assert tool.DECLARED_BOUNDARY_ROOT.endswith("common/")


def test_كلُّ_مدخلٍ_يطابقُ_موضعًا_حيًّا_موسومًا() -> None:
    tool = _load_inventory_tool()
    sites = tool.collect(REPO_ROOT)
    tagged = [s for s in sites if s.declared_boundary is not None]
    assert len(tagged) == len(EXPECTED_BOUNDARIES), (
        f"الموسومُ {len(tagged)} والقائمةُ {len(EXPECTED_BOUNDARIES)} — "
        "مدخلٌ بلا موضعٍ حيٍّ أو موضعٌ بلا مدخل."
    )
    for site in tagged:
        key = (site.path[len(tool.DECLARED_BOUNDARY_ROOT):], site.owner, site.function)
        assert key in EXPECTED_BOUNDARIES, f"موضعٌ موسومٌ خارجَ القائمة: {key}"
        assert site.declared_boundary == EXPECTED_BOUNDARIES[key]


def test_حدودٌ_خارجَ_common_مرفوضةٌ_بنيةِ_الأداةِ() -> None:
    tool = _load_inventory_tool()
    sites = tool.collect(REPO_ROOT)
    # لا موضعٍ خارجَ جذرِ الحدودِ يُوسَمُ — المفتاحُ يُبنى من الجذرِ أو لا يُبنى.
    for site in sites:
        if not site.path.startswith(tool.DECLARED_BOUNDARY_ROOT):
            assert site.declared_boundary is None, (
                f"موضعٌ خارجَ common/ موسومٌ حدًّا: {site.path} — القرارُ لم يأذنْ به."
            )
    # والمدخلُ الذي ملفُّه خارجَ common/ لا يجدُ موضعًا حيًّا فيُفشِلُ التحققَ نفسَه.
    breaches = tool.validate_declared_boundaries([], "")
    assert len(breaches) == 2 * len(EXPECTED_BOUNDARIES), (
        "شجرةٌ فارغةٌ يجبُ أن تُفشِلَ كلَّ مدخلٍ مرتينِ: تقادمًا ومرجعًا."
    )
    assert any("متقادمٌ أو خارجَ" in b for b in breaches)


def test_مراجعُ_القراراتِ_مسجَّلةٌ_في_السجلِّ_السياديّ() -> None:
    tool = _load_inventory_tool()
    register_text = REGISTER.read_text(encoding="utf-8")
    breaches = tool.validate_declared_boundaries(tool.collect(REPO_ROOT), register_text)
    assert breaches == [], f"انتهاكاتُ القائمةِ المغلقةِ: {breaches}"
    for reference in set(EXPECTED_BOUNDARIES.values()):
        assert reference in register_text, (
            f"مرجعُ قرارٍ {reference} ليسَ في السجلِّ السياديّ — الحدُّ بلا سندٍ."
        )


def test_معادلةُ_الهويّةِ_الرقمُ_العامُّ_يُفسَّرُ_كاملًا() -> None:
    """الرقمُ العامُّ لا يتغيّرُ بسَببِ الحدودِ — والفئاتُ الأربعُ تُفسِّرُه كلَّه.

    لو رُدَّ إسقاطُ الحدودِ من `summarize` عادَ الموسومُ إلى الدَّينِ فاختلَّ
    الجمعُ (public ≠ sovereign + closed + declared + non_sovereign) فسقطَ الفحصُ.
    """
    tool = _load_inventory_tool()
    sites = tool.collect(REPO_ROOT)
    summary = tool.summarize(sites)
    public = summary["public_write_operations"]
    sovereign = summary["sovereign_write_operations"]
    declared = summary["declared_boundary_operations"]
    non_sovereign = summary["non_sovereign_write_operations"]
    public_closed = sum(
        1 for s in sites if s.public and s.closed_legacy
    )
    assert public == sovereign + public_closed + declared + non_sovereign, (
        f"معادلةُ الهويّةِ مكسورة: {public} ≠ {sovereign} + {public_closed} "
        f"+ {declared} + {non_sovereign} — فئةٌ تُحسَبُ مرتينِ أو تُسقَط."
    )
    assert declared == len(EXPECTED_BOUNDARIES)
