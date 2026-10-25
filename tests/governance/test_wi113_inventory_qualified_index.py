"""الهدف: إثباتُ أنَّ جردَ الكتاباتِ يتتبّعُ المعاونينَ بالاسمِ المؤهَّلِ لا بالاسمِ المجرَّد.

النطاق: `tools/audit/sovereign_write_inventory.py` — `synthesize_public_sites` و`resolve_callees`.
المالك: governance/
تاريخ الإنشاء: 2026-10-25
تاريخ آخر تعديل: 2026-10-25

## ما يحرسُه هذا الملفّ (WI-113 · تصحيحُ قياسٍ A1(هـ) · التوجيهُ 22)

قاسَ تحليلُ A1 (§ 1.3) أنَّ الجردَ يحتسبُ 7 قراءاتٍ في `common/persistent.py` مواقعَ
كتابة: الفهرسُ بالاسمِ المجرَّدِ يدمجُ كلَّ `get` في الوحدةِ في مدخلٍ واحد، فيصلُ كلٌّ
منها إلى `_row` الكاتبِ في `PersistentSystemStateStore` (بذرٌ كسولٌ حقيقيّ)، ويُنسَبُ
المالكُ إلى آخرِ صنفٍ يُعرِّفُ `get`. فكانَ الجردُ يُركِّبُ 8 مواقعَ كلُّها بهويّةِ
`PersistentPromotionStore.get`، والحقُّ موقعٌ واحدٌ بهويّةِ `PersistentSystemStateStore.get`.

والحرسُ يقيسُ الشِقَّين: لا يُحسَبُ ما لا يكتب (الإصلاح)، ولا يُسقَطُ ما يكتب (لا إسكات).
"""

from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _repo_root() -> Path:
    """الجذرُ بعلامةٍ لا بعُمقٍ ثابت (DISC-041): صعودٌ حتّى `THE_ROADMAP.md`."""
    here = Path(__file__).resolve()
    for candidate in here.parents:
        if (candidate / "docs" / "governance" / "work" / "THE_ROADMAP.md").is_file():
            return candidate
    raise AssertionError(f"لا جذرَ فوقَ {here} يحملُ THE_ROADMAP.md")


REPO_ROOT = _repo_root()
TOOL_PATH = REPO_ROOT / "tools" / "audit" / "sovereign_write_inventory.py"
PERSISTENT = Path("federal/executive/services/src/amos_federation/common/persistent.py")

#: صنفانِ يُعرِّفانِ `get` و`_row`: الأوّلُ يكتبُ في معاونِه، والثاني يقرأُ فقط.
TWO_STORES = '''"""وحدةٌ للاختبار."""


class SeedingStore:
    def _row(self, session):
        session.add(object())
        session.commit()

    def get(self, session):
        return self._row(session)


class ReadingStore:
    def _row(self, session):
        return session.query(object).first()

    def get(self, session):
        return self._row(session)
'''


def _load_tool() -> ModuleType:
    """حمِّلِ الأداةَ من مسارِها — بلا اعتمادٍ على `sys.path`."""
    name = "amos_write_inventory_qualified_under_test"
    spec = importlib.util.spec_from_file_location(name, TOOL_PATH)
    assert spec is not None and spec.loader is not None, f"لا يُحمَّلُ: {TOOL_PATH}"
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(name, None)
        raise
    return module


def _synthesized(tool: ModuleType, source: str, path: str = "svc/stores.py") -> list:
    tree = ast.parse(source)
    visitor = tool._WriteVisitor(path, source)
    visitor.visit(tree)
    return tool.synthesize_public_sites(
        visitor.sites, visitor.qcalls, visitor.qnodes, path, source
    )


def test_reader_sharing_a_name_with_a_writer_is_not_a_write_site() -> None:
    """`ReadingStore.get` لا يُحسَبُ كتابةً لأنَّ `SeedingStore._row` يكتب."""
    tool = _load_tool()
    added = _synthesized(tool, TWO_STORES)
    identities = [(site.owner, site.function, site.writes_via) for site in added]
    assert identities == [("SeedingStore", "get", ("_row",))], identities


def test_real_writer_through_helper_is_still_counted() -> None:
    """لا إسكات: العمليّةُ العامّةُ التي تكتبُ بمعاونِها تبقى موضعًا بمالكِها الحقّ."""
    tool = _load_tool()
    added = _synthesized(tool, TWO_STORES)
    assert any(site.owner == "SeedingStore" and site.public for site in added)


def test_unknown_receiver_keeps_the_declared_conservative_limit() -> None:
    """نداءٌ على مُستقبِلٍ غيرِ `self` يبقى بالاسمِ: الحدُّ القديمُ لا يُخفَّفُ حيثُ لا يُعرَفُ النوع."""
    tool = _load_tool()
    source = (
        TWO_STORES
        + """

def flush(store, session):
    return store._row(session)
"""
    )
    added = _synthesized(tool, source)
    assert ("-", "flush") in {(site.owner, site.function) for site in added}


def test_persistent_py_has_one_synthesized_get_owned_by_system_state() -> None:
    """الشجرةُ الحاضرة: 8 مواقعَ كاذبةُ الهويّةِ صارت موقعًا واحدًا بهويّتِه الحقّ."""
    tool = _load_tool()
    source = (REPO_ROOT / PERSISTENT).read_text(encoding="utf-8")
    added = _synthesized(tool, source, str(PERSISTENT))
    gets = [
        (site.owner, site.function, site.writes_via)
        for site in added
        if site.function == "get"
    ]
    assert gets == [("PersistentSystemStateStore", "get", ("_row",))], gets
