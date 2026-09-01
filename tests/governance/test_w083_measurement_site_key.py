"""الهدف: إثباتُ أنَّ مفتاحَ الموقعِ في القياسِ المنشورِ يُقاسُ ولا يُنسَبُ إلى سطرٍ.

النطاق: `tools/audit/sovereign_write_inventory.py` — بانيةُ حِملِ `--json` وحدَها.
المالك: governance/
تاريخ الإنشاء: 2026-08-31
تاريخ آخر تعديل: 2026-08-31

## ما يحرسُه هذا الملفّ (W-084 · WI-025 · T0.4ب)

القياسُ المنشورُ `docs/audit/measurements/write_inventory_p13.json` محروسٌ بطزاجتِه
في `tools/governance/measurement_provenance.py`: يُعادُ تشغيلُ الأمرِ ويُقارَنُ
المُخرَجُ بالمنشور. وكانَ حِملُ المواقعِ يحملُ **رقمَ سطرِ** الدالّةِ، فأدخلَ `W-080`
سطرَي إعلانٍ في ترويسةِ `tools/migrations/r4_unify_agent_identity.py` — لا يمسّانِ
سلوكًا ولا عددًا — فانتقلَ موقعٌ من السطرِ 354 إلى 356، فتقادمَ القياسُ وسقطَت
وظيفةُ `Truth Audit` في CI (‏عُقدةُ `1cd662c` · تشغيلُ 33447618294 · `DISC-039`).

وبوّابةٌ تُعاقِبُ تعديلَ الترويسةِ عقابَ تعديلِ السلوكِ **تُعلِّمُ العاملَ أن
يتجنَّبَ الصواب** — وهو ضِدُّ ما تطلبُه بوّاباتُ الهُويّة. فالإصلاحُ في **مصدرِ**
القياسِ لا في **حاكمِه**: لا استثناءَ حقلٍ يُضافُ إلى بوّابةِ الطزاجةِ، بل يُنقَلُ
المفتاحُ إلى (‏مسارٌ · مالكٌ · دالّةٌ · رتبةٌ داخلَ الثلاثةِ).

وأخطرُ ما في إصلاحٍ كهذا أن يصيرَ **إسكاتًا**: مفتاحٌ أفقرُ يُخفي تغيُّرًا حقيقيًّا
كما يُخفي التقادُمَ الكاذب. فهذا الحرسُ يقيسُ الشِقَّينِ معًا:

1. **الطزاجةُ**: إدخالُ سطرِ ترويسةٍ أو تعليقٍ في ملفٍّ إنتاجيٍّ لا يُحرِّكُ حرفًا
   في الحِمل — ولا نقلُ الدالّةِ في ملفِّها.
2. **الإنفاذُ**: إضافةُ موضعِ كتابةٍ · حذفُه · إعادةُ تسميتِه · تغيُّرُ ما يكتبُه ·
   عبورُه الحدَّ السياديَّ — كلٌّ منها يُحرِّكُ الحِملَ فتسقُطُ بوّابةُ الطزاجةِ.
3. **لا دمجَ ولا إسقاطَ عندَ التشارُك**: موضعانِ يتشاركانِ المسارَ والمالكَ والدالّةَ
   يبقيانِ اثنَينِ متمايزَينِ بالرتبةِ.

ولا يقيسُ هذا الحارسُ المستودعَ إلّا في الفحصِ الأخيرِ (ربطُ الأداةِ بالشجرةِ
الحاضرةِ): سائرُ الفحوصِ يبني شجرةً مؤقّتةً في `tmp_path` فلا يعتمدُ على ترتيبِ
الاختباراتِ ولا يُلوِّثُ شجرةَ العمل.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "audit" / "sovereign_write_inventory.py"

#: وحدةٌ إنتاجيّةٌ فيها موضعُ كتابةٍ عامٌّ واحدٌ — أصغرُ ما يُقاس.
BASE_MODULE = '''"""وحدةُ خدمةٍ للاختبار."""


class Registry:
    def save(self, session, row):
        session.add(row)
        session.commit()
'''


def _load_tool() -> ModuleType:
    """حمِّلِ الأداةَ من مسارِها — بلا اعتمادٍ على `sys.path` ولا على وحدةٍ مُثبَّتة."""
    name = "amos_write_inventory_site_key_under_test"
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


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _payload(tool: ModuleType, root: Path) -> str:
    """الحِملُ كما يُكتَبُ في القياسِ المنشورِ — نصًّا لِيُقارَنَ حرفًا بحرفٍ."""
    records = tool.site_records(tool.collect(root))
    return json.dumps(records, ensure_ascii=False, indent=1)


def _project(root: Path, module: str = BASE_MODULE) -> Path:
    target = root / "svc" / "registry.py"
    _write(target, module)
    return target


# ── 1 · الطزاجةُ: ما لا يمسُّ سلوكًا لا يُحرِّكُ القياسَ ────────────────────────


def test_line_number_is_absent_from_the_published_payload(tmp_path: Path) -> None:
    """رقمُ السطرِ لا يخرجُ في الحِملِ، ويبقى في البنيةِ لقارئٍ بشريٍّ وحرسٍ يقرأُه."""
    tool = _load_tool()
    _project(tmp_path)

    sites = tool.collect(tmp_path)
    assert sites, "شجرةُ الاختبارِ فيها موضعٌ واحدٌ على الأقلّ"
    assert all(isinstance(site.line, int) for site in sites), (
        "رقمُ السطرِ حُذِفَ من بنيةِ `WriteSite` — وحرّاسٌ قائمونَ يقرأونَه، "
        "فهذا كسرٌ لا إصلاحٌ"
    )

    for record in tool.site_records(sites):
        assert "line" not in record, (
            "رقمُ السطرِ عادَ إلى الحِملِ المنشورِ — وهو إحداثيٌّ يتحرَّكُ بسطرِ "
            f"تعليقٍ فيُقادِمُ قياسًا لم يتغيَّرْ سلوكُه: {record}"
        )
        for key in ("path", "owner", "function", "ordinal"):
            assert key in record, f"مفتاحُ الموقعِ ناقصٌ حقلَ {key}: {record}"


def test_inserting_a_header_line_does_not_move_the_payload(tmp_path: Path) -> None:
    """عينُ ما أسقطَ CI في `W-080`: سطرا ترويسةٍ فوقَ الملفِّ لا يمسّانِ القياسَ."""
    tool = _load_tool()
    target = _project(tmp_path)
    before = _payload(tool, tmp_path)

    target.write_text(
        '"""وحدةُ خدمةٍ للاختبار."""\n\n'
        "# طريقُ الإنفاذ: CI_PYTEST · سطرٌ لا يمسُّ سلوكًا\n"
        "# ولا يمسُّ عددًا ولا تصنيفًا\n"
        + BASE_MODULE.split('"""وحدةُ خدمةٍ للاختبار."""\n', 1)[1],
        encoding="utf-8",
    )

    assert _payload(tool, tmp_path) == before, (
        "تحرَّكَ القياسُ المنشورُ بإدخالِ سطرَي تعليقٍ — فبوّابةُ الطزاجةِ تُعاقِبُ "
        "تعديلَ الترويسةِ عقابَ تعديلِ السلوكِ (`DISC-039`)"
    )


def test_moving_a_function_within_its_file_does_not_move_the_payload(
    tmp_path: Path,
) -> None:
    """الترتيبُ قاطعٌ لا يتبعُ الأسطرَ: تبديلُ موضعِ صنفَينِ لا يُحرِّكُ حرفًا."""
    tool = _load_tool()
    first = '''"""وحدةٌ فيها صنفانِ يكتبانِ."""


class Alpha:
    def save(self, session, row):
        session.add(row)
        session.commit()


class Beta:
    def store(self, session, row):
        session.merge(row)
        session.commit()
'''
    second = '''"""وحدةٌ فيها صنفانِ يكتبانِ."""


class Beta:
    def store(self, session, row):
        session.merge(row)
        session.commit()


class Alpha:
    def save(self, session, row):
        session.add(row)
        session.commit()
'''
    target = _project(tmp_path, first)
    before = _payload(tool, tmp_path)
    target.write_text(second, encoding="utf-8")

    assert _payload(tool, tmp_path) == before, (
        "تحرَّكَ الحِملُ بمجرَّدِ تبديلِ ترتيبِ صنفَينِ في ملفِّهما — فالترتيبُ "
        "ما زالَ يتبعُ الأسطرَ لا المفتاحَ"
    )


# ── 2 · الإنفاذُ: كلُّ تغيُّرٍ حقيقيٍّ يُحرِّكُ القياسَ فتسقُطُ الطزاجةُ ──────────


def test_adding_a_write_site_moves_the_payload(tmp_path: Path) -> None:
    """موضعُ كتابةٍ جديدٌ يظهرُ في الحِملِ — وإلّا فالمفتاحُ يُخفي دَينًا."""
    tool = _load_tool()
    target = _project(tmp_path)
    before = _payload(tool, tmp_path)

    target.write_text(
        BASE_MODULE
        + """

class Ledger:
    def record(self, session, row):
        session.add(row)
        session.commit()
""",
        encoding="utf-8",
    )
    after = _payload(tool, tmp_path)

    assert after != before, "موضعُ كتابةٍ جديدٌ لم يُحرِّكِ الحِملَ — المفتاحُ يُخفي دَينًا"
    assert len(tool.collect(tmp_path)) == 2


def test_removing_a_write_site_moves_the_payload(tmp_path: Path) -> None:
    """حذفُ موضعٍ يُحرِّكُ الحِملَ — فلا يُدَّعى دَينٌ زالَ ولا دَينٌ بقيَ بلا قياس."""
    tool = _load_tool()
    target = _project(tmp_path)
    before = _payload(tool, tmp_path)

    target.write_text('"""وحدةٌ بلا كتابةٍ."""\n', encoding="utf-8")

    assert _payload(tool, tmp_path) != before, "حذفُ موضعِ كتابةٍ لم يُحرِّكِ الحِملَ"


def test_renaming_the_operation_moves_the_payload(tmp_path: Path) -> None:
    """اسمُ الدالّةِ جزءٌ من المفتاحِ: إعادةُ تسميتِها تغيُّرٌ يُقصَدُ ظهورُه."""
    tool = _load_tool()
    target = _project(tmp_path)
    before = _payload(tool, tmp_path)

    target.write_text(BASE_MODULE.replace("def save(", "def persist("), encoding="utf-8")

    assert _payload(tool, tmp_path) != before, "إعادةُ تسميةِ العمليّةِ لم تُحرِّكِ الحِملَ"


def test_changing_what_is_written_moves_the_payload(tmp_path: Path) -> None:
    """ما تكتبُه العمليّةُ مقيسٌ في الحِملِ لا في السطرِ: تغيُّرُه يُحرِّكُه."""
    tool = _load_tool()
    target = _project(tmp_path)
    before = _payload(tool, tmp_path)

    target.write_text(
        BASE_MODULE.replace("        session.add(row)", "        session.delete(row)"),
        encoding="utf-8",
    )

    assert _payload(tool, tmp_path) != before, (
        "تغيَّرَ ما تكتبُه العمليّةُ ولم يتحرَّكِ الحِملُ — والكتابةُ عينُ ما يُقاسُ"
    )


def test_crossing_the_sovereign_boundary_moves_the_payload(tmp_path: Path) -> None:
    """عبورُ الحدِّ السياديِّ أهمُّ ما يُقاسُ: ظهورُه في الحِملِ شرطُ صدقٍ."""
    tool = _load_tool()
    target = _project(tmp_path)
    before = _payload(tool, tmp_path)

    target.write_text(
        BASE_MODULE.replace(
            "        session.add(row)",
            "        guard_declared(row)\n        session.add(row)",
        ),
        encoding="utf-8",
    )
    after = json.loads(_payload(tool, tmp_path))

    assert json.dumps(after, ensure_ascii=False, indent=1) != before, (
        "عبورُ الحدِّ السياديِّ لم يُحرِّكِ الحِملَ"
    )
    assert [record for record in after if record["guarded"]], (
        "العبورُ لم يُسجَّلْ في الحِملِ حقلًا يُقرأُ"
    )


# ── 3 · التشارُكُ في المفتاحِ: تمايُزٌ بالرتبةِ لا دمجٌ ولا إسقاطٌ ─────────────


def test_sites_sharing_the_key_stay_distinct_by_ordinal(tmp_path: Path) -> None:
    """موضعانِ بالمسارِ والمالكِ والدالّةِ نفسِها يبقيانِ اثنَينِ برتبتَينِ."""
    tool = _load_tool()
    _project(
        tmp_path,
        '''"""وحدةٌ فيها عمليّةٌ واحدةٌ يقعُ فيها إغلاقُ مسارٍ قديمٍ وكتابةٌ معًا."""


class Registry:
    def save(self, session, row):
        if row is None:
            raise UndeclaredExecutionError("مسارٌ قديمٌ مُغلَق")
        session.add(row)
        session.commit()
''',
    )

    records = tool.site_records(tool.collect(tmp_path))
    keys = [(r["path"], r["owner"], r["function"]) for r in records]
    if len(records) > len(set(keys)):
        shared = [
            r
            for r in records
            if keys.count((r["path"], r["owner"], r["function"])) > 1
        ]
        ordinals = sorted(r["ordinal"] for r in shared)
        assert ordinals == list(range(len(shared))), (
            f"مواضعُ تتشاركُ المفتاحَ ورُتَبُها ليست متمايزةً متّصلةً: {ordinals}"
        )
    else:
        # لا تشارُكَ في هذه الشجرةِ — والرتبةُ تبقى صفرًا لكلِّ موضعٍ، وذاك حكمٌ يُقاسُ
        assert all(r["ordinal"] == 0 for r in records), (
            f"لا تشارُكَ في المفتاحِ ومع ذلك ظهرَت رتبةٌ غيرُ صفرٍ: {records}"
        )


def test_the_payload_is_ordered_by_its_key_and_is_repeatable(tmp_path: Path) -> None:
    """الحِملُ مرتَّبٌ بمفتاحِه ولا يتغيَّرُ بين تشغيلَينِ — وإلّا فالطزاجةُ عبثٌ."""
    tool = _load_tool()
    _project(tmp_path)
    _write(tmp_path / "svc" / "alpha.py", BASE_MODULE)
    _write(tmp_path / "core" / "beta.py", BASE_MODULE)

    first = tool.site_records(tool.collect(tmp_path))
    second = tool.site_records(tool.collect(tmp_path))
    assert first == second, "الحِملُ اختلفَ بين تشغيلَينِ على شجرةٍ لم تتغيَّرْ"

    keys = [(r["path"], r["owner"], r["function"], r["ordinal"]) for r in first]
    assert keys == sorted(keys), f"الحِملُ غيرُ مرتَّبٍ بمفتاحِه: {keys}"


# ── 4 · ربطُ الأداةِ بالشجرةِ الحاضرةِ — فيصيرُ إنفاذُها `CI_PYTEST` ───────────


def test_the_present_tree_payload_carries_no_line_numbers() -> None:
    """حكمٌ على المستودعِ الحاضرِ لا على شجرةٍ مؤقّتةٍ: القياسُ المنشورُ بلا إحداثيّ."""
    tool = _load_tool()
    records = tool.site_records(tool.collect(REPO_ROOT))
    assert records, "جردُ المستودعِ الحاضرِ فارغٌ — وذاك قياسٌ لا يُقبَل"
    assert not [r for r in records if "line" in r], (
        "حِملُ المستودعِ الحاضرِ يحملُ رقمَ سطرٍ"
    )

    published = REPO_ROOT / "docs" / "audit" / "measurements" / "write_inventory_p13.json"
    payload = json.loads(published.read_text(encoding="utf-8"))
    assert not [r for r in payload["sites"] if "line" in r], (
        "القياسُ المنشورُ لم يُعَدْ توليدُه بعدَ نقلِ المفتاحِ — فهو متقادمٌ بحقلٍ "
        "يُسقِطُ بوّابةَ الطزاجةِ في CI"
    )
