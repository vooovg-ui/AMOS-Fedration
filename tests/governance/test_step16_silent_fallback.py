# =============================================================================
# File:        tests/governance/test_step16_silent_fallback.py
# الهدف · Purpose: حرسُ الخطوةِ 16 (T3.5) — الارتداداتُ الصامتةُ صِفرٌ ولا ترتدّ،
#             وكلُّ موضعٍ أُصلِحَ يُعلِنُ فشلَه بصيغةٍ تُقاسُ من المصدر
# النطاق:     قراءةٌ وفحصٌ فقط: قاعدةُ المدقّقِ تُستورَدُ ولا تُعادُ كتابتُها،
#             والمواضعُ الـ26 تُقاسُ في مِلفّاتِها على القُرص.
# المالك · Owner: tests/governance
# Created:     2026-08-22
# Phase:       T3.5 · W-027
# Article 009: هذا الملف يلتزم بالمادة 009 — الشفافية والمراجعة المستمرة.
# =============================================================================
"""حرسُ الخطوةِ 16 — الارتدادُ الصامت (المادة 002: إعلانُ الحقيقة).

الهدف: تثبيتُ نتيجةِ W-027 إلى موضعِها: **صِفرُ `SILENT_FALLBACK`** بقاعدةِ
       المدقّقِ نفسِها، وامتناعُ الارتدادِ إلى الشكلِ الذي كان يُخفي الفشلَ
       (‏`except X: pass` · بديلٌ بلا إعلانٍ · نصُّ خطأٍ عامٌّ يُبدِلُ الخطأَ الحقيقيّ).

النطاق: لا شبكةَ ولا قاعدةَ بياناتٍ. المكتبةُ القياسيّةُ و`pytest` فقط.
المالك: tests/governance
تاريخ الإنشاء: 2026-08-22

حدُّ صدقِ هذا الحرس: يُثبِتُ **أنَّ كلَّ مِعالِجِ استثناءٍ في نطاقِ المدقّقِ يُعلِنُ
شيئًا يُقاسُ** (رفعٌ · تسجيلٌ · استخدامُ الاستثناءِ)، وأنَّ المواضعَ الـ26 المُصلَحةَ
في W-027 لا تزالُ تُعلِنُ، وأنَّ المدقِّقَ نفسَه لم يعُدْ يُخطّي ملفًّا بصمتٍ.
ولا يُثبِتُ أنَّ نصَّ كلِّ إعلانٍ كافٍ لتشخيصِ العلّةِ عمليًّا — ذاك حكمٌ على جودةِ
رسالةٍ لا يُقاسُ بأداة. ولا يُثبِتُ أنَّ البديلَ في `federation.py` صارَ آمنًا:
البديلُ باقٍ مكسورًا وقابلًا للتلفيقِ بحكمِ Q-37، وهذا الحرسُ يُثبِتُ فقط أنّه
**يَصرُخُ** بحالِه.
"""

from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
AUDIT_TOOL = REPO_ROOT / "tools" / "governance" / "truth_audit.py"
SERVICES_SRC = REPO_ROOT / "federal" / "executive" / "services" / "src" / "amos_federation"
SERVICES_TESTS = REPO_ROOT / "federal" / "executive" / "services" / "tests"


def _load_audit_module():
    """استوردْ قاعدةَ المدقّقِ نفسَها — لا تُعَدْ كتابتُها في الحرس.

    إعادةُ تنفيذِ القاعدةِ هنا تُنتِجُ حرسًا يُصادِقُ على فهمِه لا على الأداة،
    فيبقى أخضرَ بعدَ أن يُضعَّفَ المدقِّقُ الحقيقيّ.
    """
    spec = importlib.util.spec_from_file_location("_truth_audit_step16", AUDIT_TOOL)
    assert spec and spec.loader, "تعذَّرَ تحميلُ قاعدةِ المدقّق."
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def audit_module():
    return _load_audit_module()


@pytest.fixture(scope="module")
def audit_result(audit_module):
    """شغِّلِ المدقِّقَ مرّةً على المستودعِ كلِّه، واقرأِ الخرجَ لا الادّعاء."""
    audit = audit_module.TruthAudit(REPO_ROOT)
    audit.scan()
    return audit


# ═══════════════════════════════════════════════════════════════════════════
# 1 · الحُكمُ المقيس: صِفرُ ارتدادٍ صامتٍ في نطاقِ المدقّق
# ═══════════════════════════════════════════════════════════════════════════


def test_silent_fallback_count_is_zero(audit_result):
    """المدقِّقُ لا يجدُ ارتدادًا صامتًا واحدًا — يُقاسُ لا يُنقَل."""
    offenders = [f for f in audit_result.global_findings if f.kind == "SILENT_FALLBACK"]
    rendered = "\n".join(f"  - {f.path}:{f.line} — {f.detail}" for f in offenders)
    assert not offenders, (
        f"عادَ الارتدادُ الصامتُ: {len(offenders)} موضعًا. W-027 أنزلَها من 26 إلى 0، "
        f"والسَّقَّاطةُ لا تصعدُ.\n{rendered}"
    )


def test_ratchet_does_not_regress_above_w027_baseline(audit_result):
    """إجماليُّ المخالفاتِ لا يتجاوزُ خطَّ W-027 — 63 بعدَ إسقاطِ الـ26."""
    total = audit_result.summary()["findings_total"]
    assert total <= 63, (
        f"إجماليُّ المخالفاتِ {total} > 63 (خطُّ W-027). "
        "السَّقَّاطةُ تنزلُ ولا تصعد: أُضيفَ دَينٌ جديدٌ أو أُضعِفَ كاشف."
    )


# ═══════════════════════════════════════════════════════════════════════════
# 2 · صدقُ المدقّقِ على نفسِه: لا ملفَّ يُخطَّى بصمت
# ═══════════════════════════════════════════════════════════════════════════


def test_auditor_publishes_skipped_file_counts(audit_result):
    """الموجزُ يُعلِنُ ما لم يُقَسْ — لا يُخفي عجزَه تحتَ «لا مخالفة»."""
    summary = audit_result.summary()
    for key in ("unreadable_files", "unparsable_files"):
        assert key in summary, (
            f"الموجزُ لا يُعلِنُ `{key}`. مدقِّقٌ يعجزُ عن قياسِ ملفٍّ ثمَّ يسكتُ "
            "يُظهِرُ نظافةً لم يقِسْها."
        )
        assert isinstance(summary[key], int)


def test_auditor_records_unreadable_file_instead_of_empty_text(audit_module, tmp_path):
    """ملفٌّ لا يُقرأُ يُقيَّدُ في السجلِّ ولا يُسلَّمُ نصًّا فارغًا صامتًا."""
    audit = audit_module.TruthAudit(tmp_path)
    missing = tmp_path / "لا-وجودَ-له.py"
    text = audit._read(missing)
    assert text == "", "العقدُ أن يُعادَ نصٌّ فارغٌ — لكن مع تقييدِ السبب."
    assert audit.unreadable_files, (
        "قُرِئَ ملفٌّ غيرُ موجودٍ فأُعيدَ فراغٌ **بلا تقييد**: "
        "النصُّ الفارغُ يمرُّ في كلِّ الفحوصِ فيُقرأُ العجزُ نظافةً."
    )
    recorded_path, reason = audit.unreadable_files[0]
    assert "لا-وجودَ-له.py" in recorded_path
    assert reason.strip(), "قُيِّدَ الملفُّ بلا سببٍ — التقييدُ بلا سببٍ نصفُ إعلان."


def test_auditor_records_unparsable_file(audit_module, tmp_path):
    """ملفٌّ لا يُحلَّلُ نحويًّا يُعلَنُ — تخطّيه يُلغي كلَّ الفحوصِ النحويّة."""
    (tmp_path / "core").mkdir()
    broken = tmp_path / "core" / "معطوب.py"
    broken.write_text("def خطأ(:\n    pass\n", encoding="utf-8")
    audit = audit_module.TruthAudit(tmp_path)
    audit.scan()
    recorded = [p for p, _ in audit.unparsable_files]
    assert any("معطوب.py" in p for p in recorded), (
        "ملفٌّ لا يُحلَّلُ نحويًّا مرَّ بلا تقييد: أسرارُه وثوابتُه وارتداداتُه "
        f"لم تُفحَصْ، والصمتُ يُقرأُ براءةً. المُقيَّد: {recorded}"
    )


def test_domain_of_returns_none_for_outside_path_without_swallowing(audit_module, tmp_path):
    """المسارُ خارجَ الجذرِ يُسأَلُ صراحةً لا يُبتلَعُ استثناءً."""
    audit = audit_module.TruthAudit(tmp_path)
    assert audit._domain_of(Path("/tmp/خارج-الجذر/ملف.py")) is None
    source = Path(audit_module.__file__).read_text(encoding="utf-8")
    fn_start = source.index("def _domain_of")
    fn_end = source.index("\n    def ", fn_start + 10)
    body = source[fn_start:fn_end]
    assert "except ValueError" not in body, (
        "عادَ `except ValueError` إلى `_domain_of`: الحالةُ المتوقَّعةُ تُسأَلُ "
        "بـ`is_relative_to` ولا تُلبَسُ لباسَ الخطأِ المُبتلَع."
    )


# ═══════════════════════════════════════════════════════════════════════════
# 3 · المواضعُ المُصلَحةُ تُعلِنُ — تُقاسُ من المصدرِ موضعًا موضعًا
# ═══════════════════════════════════════════════════════════════════════════

#: (المِلفّ، مِفتاحُ الإعلانِ الذي يجبُ أن يبقى) — أُصلِحَت في W-027.
DECLARED_SITES: tuple[tuple[Path, str], ...] = (
    (SERVICES_SRC / "common/events.py", "events.transport_unavailable"),
    (SERVICES_SRC / "common/events.py", "audit.timestamp_unparsable"),
    (SERVICES_SRC / "common/events.py", "audit.metadata_malformed_json"),
    (SERVICES_SRC / "common/persistent.py", "tool_store.seed_failed"),
    (SERVICES_SRC / "common/persistent.py", "memory.value_malformed_json"),
    (SERVICES_SRC / "common/persistent.py", "audit.chain_verification_failed_on_init"),
    (SERVICES_SRC / "common/persistent.py", "audit.hash_recompute_attempt_failed"),
    (SERVICES_SRC / "common/service.py", "service.instrumentation_unavailable"),
    (SERVICES_SRC / "common/tracing.py", "tracing.unavailable"),
    (SERVICES_SRC / "services/evaluation/benchmark.py", "benchmark.task_execution_failed"),
    (SERVICES_SRC / "services/governance/expansion.py", "expansion.health_history_unavailable"),
    (
        SERVICES_SRC / "services/governance/federation.py",
        "federation.signing_downgraded_to_forgeable_fallback",
    ),
    (SERVICES_SRC / "services/governance/federation.py", "federation.signature_rejected"),
    (SERVICES_SRC / "services/governance/policy_engine.py", "policy.non_numeric_comparison"),
    (SERVICES_SRC / "services/tool_registry/store.py", "tool_registry.seed_from_yaml_failed"),
)


@pytest.mark.parametrize(
    ("path", "marker"),
    DECLARED_SITES,
    ids=[f"{p.name}::{m}" for p, m in DECLARED_SITES],
)
def test_repaired_site_still_declares(path: Path, marker: str):
    """كلُّ موضعٍ أُصلِحَ في W-027 لا يزالُ يُعلِنُ فشلَه باسمِ حدثٍ مقروء."""
    assert path.exists(), f"غابَ المِلفُّ {path}"
    text = path.read_text(encoding="utf-8")
    assert marker in text, (
        f"سقطَ الإعلانُ `{marker}` من {path.relative_to(REPO_ROOT)}. "
        "W-027 استبدلَ الصمتَ بالإعلانِ، وحذفُ الإعلانِ يعيدُ الصمت."
    )


def test_no_bare_pass_only_handler_in_services_source():
    """لا مِعالِجَ استثناءٍ جسمُه `pass` وحدَه في مصدرِ الخدمات."""
    offenders: list[str] = []
    for path in sorted(SERVICES_SRC.rglob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc:  # pragma: no cover - يسقطُ الحرسُ صريحًا
            pytest.fail(f"تعذَّرَ تحليلُ {path}: {exc}")
        for node in ast.walk(tree):
            if not isinstance(node, ast.ExceptHandler):
                continue
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                offenders.append(f"{path.relative_to(REPO_ROOT)}:{node.lineno}")
    assert not offenders, (
        "عادَ `except …: pass` إلى مصدرِ الخدمات — وهو أصفى صورةِ ارتدادٍ صامت:\n  "
        + "\n  ".join(offenders)
    )


def test_benchmark_error_carries_real_exception():
    """تقريرُ القياسِ يحملُ نوعَ الخطأِ ونصَّه لا `execution_failed` وحدَه."""
    text = (SERVICES_SRC / "services/evaluation/benchmark.py").read_text(encoding="utf-8")
    for key in ('"error_type"', '"error_detail"'):
        assert key in text, (
            f"غابَ {key} من تقريرِ القياس: نصٌّ عامٌّ واحدٌ لكلِّ الأعطالِ "
            "لا يُفرِّقُ أداةً مفقودةً من مهلةٍ منتهيةٍ من خللٍ في المِعيار."
        )


def test_federation_fallback_is_declared_not_silently_repaired():
    """البديلُ المكسورُ باقٍ بحكمِ Q-37 — لكنّه يَصرُخُ بحالِه."""
    text = (SERVICES_SRC / "services/governance/federation.py").read_text(encoding="utf-8")
    assert "Q-37" in text, (
        "سقطَت الإحالةُ إلى Q-37: بقاءُ بديلٍ قابلٍ للتلفيقِ بلا إحالةٍ إلى "
        "قرارٍ سياديٍّ مُعلَّقٍ يُحوِّلُ الدَّينَ المُعلَنَ إلى دَينٍ مخفيّ."
    )
    assert "critical(" in text, (
        "خُفِّضَ مستوى الإعلانِ عن انحدارِ التوقيع: هذا أخطرُ من ارتدادٍ صامتٍ "
        "عاديٍّ فلا يُعلَنُ بأقلَّ من `critical`."
    )


@pytest.mark.parametrize(
    "path",
    (
        SERVICES_TESTS / "test_2a_sovereign_runtime_integration.py",
        SERVICES_TESTS / "test_2b_state_registry_sovereign.py",
    ),
    ids=["test_2a", "test_2b"],
)
def test_idempotency_branches_surface_the_exception(path: Path):
    """فرعُ `IdempotencyError` في الاختبارَينِ يحملُ سببَ الرفضِ في رسالتِه."""
    text = path.read_text(encoding="utf-8")
    assert "except IdempotencyError as exc" in text, (
        f"عادَ ابتلاعُ الاستثناءِ في {path.name}: اختبارٌ يسقطُ بلا سببِ الرفضِ "
        "يُجبِرُ قارئَه على التخمين."
    )


def test_sovereign_inventory_declares_skipped_files():
    """جردُ الأسطحِ يُعلِنُ ملفَّ الإنتاجِ الذي تعذَّرَ تحليلُه — الدَّينُ لا يُنقَصُ بصمت."""
    text = (REPO_ROOT / "tools/audit/sovereign_write_inventory.py").read_text(encoding="utf-8")
    assert "SOVEREIGN INVENTORY" in text and "stderr" in text, (
        "عادَ الجردُ يتخطّى ملفَّ إنتاجٍ بصمتٍ: أسطحُه لا تُعَدُّ فيظهرُ الدَّينُ "
        "أقلَّ مما هو، وهذا كذبٌ في الاتّجاهِ المُطمئِن."
    )
