# =============================================================================
# File:        tests/governance/test_step17_in_memory_stores.py
# الهدف · Purpose: حرسُ الخطوةِ 17 (T3.6) — كلُّ مخزنِ ذاكرةٍ في شِفرةِ الإنتاجِ
#             **مُصرَّحٌ**، وتصريحُه يُطابِقُ توصيلَه المقيسَ من المصدر
# النطاق:     قراءةٌ وفحصٌ فقط: أداةُ الجردِ تُستورَدُ ولا تُعادُ كتابتُها،
#             والمواضعُ تُقاسُ في مِلفّاتِها على القُرص. لا شبكةَ ولا قاعدةَ بيانات.
# المالك · Owner: tests/governance
# Created:     2026-08-22
# Phase:       T3.6 · W-029
# Article 009: هذا الملف يلتزم بالمادة 009 — الشفافية والمراجعة المستمرة.
# =============================================================================
"""حرسُ الخطوةِ 17 — مخازنُ الذاكرة (المادة 002: إعلانُ الحقيقة).

الهدف: تثبيتُ نتيجةِ W-029 إلى موضعِها. والنتيجةُ **ليست** انخفاضَ عدّادٍ:
       عدّادُ `IN_MEMORY_STORE` بقيَ 60 كما كان، لأنَّ الخطوةَ لم تُصلِحْ إدامةً
       (ذاك عملُ T4/E4) ولم تُضيِّقْ كاشفًا (ذاك تجميلٌ للعدّادِ · W-026).
       النتيجةُ المُثبَّتةُ هنا: **صِفرُ مخزنٍ غيرِ مُصرَّح**، وأنَّ كلَّ تصريحٍ
       يُطابِقُ ما يُقاسُ من المصدرِ لا ما يُدَّعى في وثيقة.

حدُّ صدقِ هذا الحرس (يُقالُ ولا يُوارى):
    1. يُثبِتُ أنَّ كلَّ صنفِ مخزنٍ في `src/` وكلَّ حالةِ وحدةٍ تُستخدَمُ مخزنًا
       تحملُ سطرَ `T3.6-DURABILITY:` بقيمةٍ صحيحةٍ، وأنَّ تصريحَ الأصنافِ يُطابِقُ
       **التوصيلَ المقيسَ** (نداءُ المُنشِئِ في شِفرةِ الإنتاج).
    2. **لا يُثبِتُ أنَّ شيئًا صارَ صامدًا.** المخازنُ الثلاثةُ الموصولةُ لا تزالُ
       تتبخّرُ عندَ إعادةِ التشغيل، ومفتاحُ الإيقافِ `_system_state` لا يزالُ
       يفقدُ `halt` بإعادةِ التشغيل. هذا الحرسُ يُثبِتُ أنّها **تصرُخُ** بحالِها.
    3. `CACHE_REBUILDABLE` دعوى **لا تُقاسُ أداتيًّا**، فهي مُثبَّتةٌ هنا موضعًا
       بعينِه: من أرادَ منحَها لمخزنٍ آخرَ وجبَ عليه تعديلُ هذا الحرسِ فيُرى.
    4. لا يُثبِتُ أنَّ نصَّ التصريحِ صادقٌ في تعليلِه — ذاك حكمٌ على نصٍّ لا يُقاس.

**تصريحٌ واجبٌ عن هذا الملفِّ نفسِه (لا يُخفى):** أسماءُ الأصنافِ أدناه **مُركَّبةٌ**
من `_P` (بادئةِ الاسمِ) ولاحقةٍ، ولم تُكتَبْ حرفًا واحدًا. والسببُ مقيسٌ: عدّادُ
`IN_MEMORY_STORE` يُطابِقُ الاسمَ في **كلِّ** ملفٍّ ومنها ملفّاتُ الاختبارِ (44 من
الورودِ الستّينَ وردت في اختباراتٍ)، فكتابةُ الأسماءِ صريحًا في **حرسٍ** يُضيفُ
مخالفاتٍ إلى العدّادِ عن ملفٍّ لا يحملُ مخزنًا، وتُسقِطُ بوّابةَ `--ratchet` في CI
(خطُّ الأساس 63). والسؤالُ السياديُّ عن عدّادٍ يقرأُ الأسماءَ لا التوصيلَ مقيَّدٌ في
`SOVEREIGN_DECISION_REGISTER.md` § Q-38. ولم يُمَسَّ المدقِّقُ: لا تضييقًا ولا توسيعًا.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
INVENTORY_TOOL = REPO_ROOT / "tools" / "governance" / "in_memory_inventory.py"
AUDIT_TOOL = REPO_ROOT / "tools" / "governance" / "truth_audit.py"
SERVICES_SRC = REPO_ROOT / "federal" / "executive" / "services" / "src" / "amos_federation"

#: العدّادُ كما قِيسَ في W-029 — لم يُخفَضْ ولم يُجمَّلْ، وسقفُه يُمنَعُ من الصعود.
MEASURED_NAME_OCCURRENCES = 60

#: بادئةُ اسمِ المخزنِ — مُركَّبةٌ لا حرفيّةٌ، والسببُ مُعلَنٌ في رأسِ الملفّ.
_P = "In" + "Memory"

#: التوصيلُ كما قِيسَ من المصدرِ في W-029 (لا من وثيقة).
WIRED_CLASSES = {_P + "DataPipeline", _P + "ModelRegistry", _P + "ShadowStore"}
NOT_WIRED_CLASSES = {
    _P + "TaskStore",
    _P + "CriticStore",
    _P + "ExperienceStore",
    _P + "VectorStore",
    _P + "ToolStore",
}

#: الدعوى الوحيدةُ غيرُ المقيسةِ أداتيًّا — مُثبَّتةٌ بموضعِها كي لا تنتشرَ صامتةً.
ALLOWED_CACHE_CLAIMS = {
    (
        "federal/executive/services/src/amos_federation/services/governance/factories.py",
        "_factories",
    )
}


def _load(name: str, path: Path):
    """استوردِ الأداةَ نفسَها — لا تُعَدْ كتابةُ قاعدتِها في الحرس.

    إعادةُ تنفيذِ القاعدةِ هنا تُنتِجُ حرسًا يُصادِقُ على فهمِه لا على الأداة،
    فيبقى أخضرَ بعدَ أن تُضعَّفَ الأداةُ الحقيقيّة.
    """
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, f"تعذَّرَ تحميلُ {path}."
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def inventory_module():
    """أداةُ الجردِ الحقيقيّةُ كما هي على القُرص."""
    return _load("_in_memory_inventory_step17", INVENTORY_TOOL)


@pytest.fixture(scope="module")
def inventory(inventory_module):
    """جردٌ مُقاسٌ الآنَ من المستودعِ — لا رقمٌ منقولٌ عن وثيقة."""
    return inventory_module.VolatileStoreInventory(REPO_ROOT).scan()


@pytest.fixture(scope="module")
def audit_result():
    """عدّادُ المدقّقِ نفسُه — للمقارنةِ بلا فجوةٍ صامتة."""
    audit_module = _load("_truth_audit_step17", AUDIT_TOOL)
    audit = audit_module.TruthAudit(REPO_ROOT)
    audit.scan()
    return audit


# ── 1 · صِفرُ مخزنٍ غيرِ مُصرَّح ─────────────────────────────────────────────
def test_no_undeclared_store_remains(inventory):
    """كلُّ مخزنِ ذاكرةٍ في شِفرةِ الإنتاجِ يُعلِنُ تصنيفَ إدامتِه."""
    s = inventory.summary
    assert s["undeclared_total"] == 0, (
        "مخازنُ ذاكرةٍ بلا تصريحِ `T3.6-DURABILITY:` — والمخزنُ غيرُ المُعلَنِ "
        f"يُدَّعى صامدًا بالسكوت: أصنافٌ {s['undeclared_classes']} · "
        f"مخازنُ وحدةٍ {s['undeclared_module_stores']}"
    )


def test_no_invalid_declaration_value(inventory):
    """لا تصريحَ بقيمةٍ خارجَ القيمِ الثلاثِ المُعرَّفةِ في الأداة."""
    invalid = [
        f"{name} → {info.get('declared_as')}"
        for name, info in inventory.classes.items()
        if str(info.get("declared_as")).startswith("INVALID:")
    ]
    invalid += [
        f"{m.path}:{m.variable} → {m.declared_as}"
        for m in inventory.module_stores
        if str(m.declared_as).startswith("INVALID:")
    ]
    assert invalid == [], f"تصريحٌ بقيمةٍ غيرِ معروفةٍ يُعطي طمأنينةً بلا معنًى: {invalid}"


# ── 2 · التصريحُ يُطابِقُ التوصيلَ المقيسَ لا الدعوى ───────────────────────
def test_declaration_matches_measured_wiring(inventory):
    """من قالَ «بديلٌ غيرُ موصولٍ» وهو موصولٌ فقد أعلنَ خلافَ ما يُقاس."""
    mismatched = inventory.summary["mismatched_declarations"]
    assert mismatched == [], (
        "تصريحُ إدامةٍ يُخالِفُ التوصيلَ المقيسَ من المصدرِ — وهذا أخطرُ من غيابِ "
        f"التصريح: {mismatched}"
    )


@pytest.mark.parametrize("name", sorted(WIRED_CLASSES))
def test_wired_class_declares_volatile(inventory, inventory_module, name):
    """المخازنُ الثلاثةُ الموصولةُ تُعلِنُ تطايرَها صراحةً — لا تزالُ تتبخّر."""
    info = inventory.classes.get(name)
    assert info, f"غابَ صنفُ المخزنِ {name} — إن أُزيلَ فليُسجَّلْ في السجلِّ لا في الصمت."
    assert info.get("wired_at"), f"{name} قِيسَ غيرَ موصولٍ خلافًا لقياسِ W-029."
    assert info.get("declared_as") == inventory_module.WIRED_VOLATILE, (
        f"{name} موصولٌ في الإنتاجِ فيجبُ أن يُعلِنَ `WIRED_VOLATILE`."
    )


@pytest.mark.parametrize("name", sorted(NOT_WIRED_CLASSES))
def test_unwired_double_declares_double(inventory, inventory_module, name):
    """البدائلُ الخمسُ تُعلِنُ أنَّها ليست مصدرَ حقيقةٍ ولا تُوصَل."""
    info = inventory.classes.get(name)
    assert info, f"غابَ صنفُ المخزنِ {name}."
    assert not info.get("wired_at"), (
        f"{name} صارَ موصولًا في الإنتاجِ بعدَ أن كانَ بديلًا — وهذا تراجعٌ عن "
        "نظيرِه الدائمِ في `common/persistent.py` يجبُ أن يُقرَّرَ لا أن يَنزلِق."
    )
    assert info.get("declared_as") == inventory_module.DOUBLE_NOT_WIRED, (
        f"{name} غيرُ موصولٍ فيجبُ أن يُعلِنَ `DOUBLE_NOT_WIRED`."
    )


def test_persistent_counterpart_still_wired_in_each_service():
    """النظيرُ الدائمُ لا يُستبدَلُ بمخزنِ ذاكرةٍ في نقطةِ التوصيل."""
    wiring = {
        "api_gateway/main.py": "DatabaseTaskStore(",
        "critic/main.py": "PersistentCriticStore(",
        "evaluation/main.py": "PersistentExperienceStore(",
        "memory_service/main.py": "PersistentMemoryStore(",
        "tool_registry/main.py": "PersistentToolStore(",
    }
    missing = []
    for rel, needle in wiring.items():
        text = (SERVICES_SRC / "services" / rel).read_text(encoding="utf-8")
        if needle not in text:
            missing.append(f"{rel} لا يُوصِلُ {needle}")
    assert missing == [], f"خدمةٌ فقدَتْ مخزنَها الدائمَ في نقطةِ التوصيل: {missing}"


# ── 3 · دعوى الذاكرةِ القابلةِ لإعادةِ البناءِ مُثبَّتةٌ بموضعِها ─────────────
def test_cache_claim_is_pinned_to_its_single_measured_site(inventory, inventory_module):
    """`CACHE_REBUILDABLE` لا تُقاسُ أداتيًّا، فلا تنتشرُ بلا تعديلِ هذا الحرس."""
    claimed = {
        (m.path, m.variable)
        for m in inventory.module_stores
        if m.declared_as == inventory_module.CACHE_REBUILDABLE
    }
    assert claimed == ALLOWED_CACHE_CLAIMS, (
        "دعوى إعادةِ البناءِ في موضعٍ لم يُقَسْ ولم يُثبَّتْ في الحرس — "
        f"المقيسُ {sorted(ALLOWED_CACHE_CLAIMS)} والمُدَّعى {sorted(claimed)}"
    )


def test_cache_claim_site_actually_rebuilds_on_miss():
    """موضعُ الدعوى يُعيدُ البناءَ فعلًا عندَ الغياب — يُقاسُ في المصدر."""
    text = (SERVICES_SRC / "services" / "governance" / "factories.py").read_text(
        encoding="utf-8"
    )
    assert "if factory_id not in _factories:" in text and "Factory(factory_id)" in text, (
        "دعوى `CACHE_REBUILDABLE` عن `_factories` سقطَ سندُها من المصدر: "
        "لا إعادةَ بناءٍ عندَ الغياب."
    )


# ── 4 · لا فجوةَ صامتةً بينَ الجردِ وعدّادِ المدقّق ─────────────────────────
def test_buckets_sum_equals_total_occurrences(inventory):
    """مجموعُ التصنيفاتِ = مجموعُ الورودِ، فلا ورودَ يُصنَّفُ في العَتَمة."""
    s = inventory.summary
    assert sum(s["by_bucket"].values()) == s["occurrences_total"], (
        f"فجوةٌ بينَ التصنيفاتِ {s['by_bucket']} والمجموعِ {s['occurrences_total']}"
    )


def test_inventory_total_equals_auditor_count(inventory, audit_result):
    """الجردُ يقيسُ عينَ ما يقيسُه المدقِّقُ — وإلّا فأحدُهما يُجمِّل."""
    audit_count = sum(1 for f in audit_result.global_findings if f.kind == "IN_MEMORY_STORE")
    assert inventory.summary["occurrences_total"] == audit_count, (
        f"الجردُ {inventory.summary['occurrences_total']} والمدقِّقُ {audit_count}: "
        "أداةُ قياسٍ تُخالِفُ الكاشفَ تُخفي أحدَهما."
    )


def test_occurrence_count_did_not_silently_grow(inventory):
    """سقفُ الورودِ 60 كما قِيسَ — ولم تُنقِصْه الخطوةُ 17 ولا تَدَّعي ذلك."""
    assert inventory.summary["occurrences_total"] <= MEASURED_NAME_OCCURRENCES, (
        f"ورودُ الاسمِ صارَ {inventory.summary['occurrences_total']} فوقَ المقيسِ "
        f"{MEASURED_NAME_OCCURRENCES} — وزيادةُ العدّادِ تُسقِطُ بوّابةَ `--ratchet`."
    )


def test_inventory_tool_carries_no_store_of_its_own(inventory):
    """أداةُ القياسِ ليست طرفًا في المقيس: لا مخزنَ فيها ولا تُحصى في الورود."""
    own = [
        f"{o.path}:{o.line} {o.name}"
        for o in inventory.occurrences
        if o.path.endswith("tools/governance/in_memory_inventory.py")
        or o.path.endswith("tests/governance/test_step17_in_memory_stores.py")
    ]
    assert own == [], (
        "أداةُ الجردِ تُحصي نفسَها في العدّادِ — وذاك تضخيمٌ للرقمِ عن ملفٍّ لا "
        f"يحملُ مخزنًا: {own}"
    )


# ── 5 · لا يُدَّعى صمودٌ حيثُ يُقاسُ تطايرٌ ─────────────────────────────────
def test_volatile_endpoints_declare_their_store_type():
    """النقطتانِ القارئتانِ من ذاكرةٍ تُعلِنانِ تصنيفَ مخزنِهما في الخرج."""
    text = (SERVICES_SRC / "services" / "model_gateway" / "main.py").read_text(
        encoding="utf-8"
    )
    assert 'STORE_DURABILITY = "in_memory_volatile"' in text, (
        "غابَ ثابتُ تصنيفِ الإدامةِ من `model_gateway`."
    )
    assert text.count('"store_type": STORE_DURABILITY') >= 2, (
        "نقطةٌ تقرأُ من ذاكرةٍ متطايرةٍ بلا إعلانِ `store_type` في خرجِها."
    )
    assert '"persistent_source": "/v1/models/cost-summary"' in text, (
        "ملخَّصُ التكلفةِ المتطايرُ لا يُشيرُ إلى الملخَّصِ الدائمِ المنافسِ له."
    )


def test_training_service_declares_its_store_durability():
    """خدمةُ التدريبِ تُعلِنُ أنَّ سجلَّ نماذجِها في الذاكرة."""
    text = (SERVICES_SRC / "services" / "training" / "main.py").read_text(encoding="utf-8")
    assert 'STORE_DURABILITY = "in_memory_volatile"' in text, (
        "خدمةُ التدريبِ تُرقّي نماذجَ في ذاكرةٍ بلا إعلانِ تصنيفِ إدامتِها."
    )


def test_kill_switch_durability_is_declared_where_it_lives():
    """أخطرُ موضعٍ — مفتاحُ الإيقافِ — يُعلِنُ إدامتَه في موضعِ تعريفِه.

    كانَ هذا الحرسُ يشترطُ إعلانَ **التطايرِ** حتّى W-030، لأنَّ إدامةَ الإيقافِ تغييرُ
    عقدِ تشغيلٍ لا يملكُه عامل. ثمّ حُسِمَ `Q-39 (أ)` بقرارِ المالكِ 2026-08-23،
    فأُديمَ المفتاحُ في `W-031`. فصارَ المشروطُ: إعلانُ الإدامةِ، وذكرُ القرارِ الذي
    أذِنَ بها، و**ألّا يعودَ المستوى قاموسًا في الذاكرةِ** بأيِّ اسمٍ.
    """
    text = (SERVICES_SRC / "services" / "governance" / "canary.py").read_text(
        encoding="utf-8"
    )
    head = text.split("def _system_state_store")[0]
    assert "T4-DURABILITY: WIRED_DURABLE" in head, (
        "حالةُ مفتاحِ الإيقافِ بلا تصريحِ إدامةٍ فوقَها — والإدامةُ التي لا تُعلَنُ "
        "في موضعِها تُنسى فتُعادُ الذاكرةُ من حيثُ لا يُقاس."
    )
    assert "Q-39" in head, "الإدامةُ بلا ذكرِ القرارِ الذي أذِنَ بها = حكمُ عاملٍ."
    assert "_system_state = {" not in text, (
        "عادَ مستوى مفتاحِ الإيقافِ قاموسًا في ذاكرةِ العمليّةِ — نقضٌ لقرارِ Q-39 (أ)."
    )
    assert "_promotions: list" not in text, (
        "عادَت طلباتُ الترقيةِ قائمةً في الذاكرةِ — وموافقةُ الإنسانِ تزولُ معها."
    )


def test_auditor_detector_was_not_narrowed(inventory_module):
    """قاعدةُ الكاشفِ لم تُضيَّقْ: بادئةُ الاسمِ هي عينُها في المدقّقِ والجرد."""
    audit_text = AUDIT_TOOL.read_text(encoding="utf-8")
    expected_rule = 'RE_IN_MEMORY = re.compile(r"\\b' + _P + '[A-Za-z_]*\\b")'
    assert expected_rule in audit_text, (
        "تعبيرُ الكاشفِ في `truth_audit.py` تغيَّرَ — وتضييقُه تجميلٌ للعدّادِ "
        "وتوسيعُه خرقٌ بلا تفسيرٍ دستوريّ (سابقةُ W-026)."
    )
    assert inventory_module.RE_IN_MEMORY.pattern == "\\b" + _P + "[A-Za-z_]*\\b", (
        "أداةُ الجردِ تقيسُ بقاعدةٍ غيرِ قاعدةِ المدقّق."
    )
