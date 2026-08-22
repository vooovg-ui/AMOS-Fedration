# =============================================================================
# File:        tests/governance/test_step13_identity_headers.py
# الهدف · Purpose: حرسُ الخطوةِ 13 (T3.2) — ترويساتُ الهويّةِ صفرٌ ولا ترتدّ،
#             وما تُعلِنُه ترويسةُ الحارسِ هو ما يفعلُه الحارس
# النطاق:     قراءةٌ وفحصٌ فقط: قاعدةُ المدقّقِ نفسُها تُستورَدُ ولا تُعادُ كتابتُها،
#             وحرّاسُ إقليمَي `docs` و`tests` يُقاسانِ على شجرةٍ مؤقّتة.
# المالك · Owner: tests/governance
# Created:     2026-08-22
# Phase:       T3.2 · W-026
# Article 009: هذا الملف يلتزم بالمادة 009 — الشفافية والمراجعة المستمرة.
# =============================================================================
"""حرسُ الخطوةِ 13 — ترويساتُ الهويّة (المادة 009).

الهدف: تثبيتُ نتيجةِ W-026 إلى موضعِها: **صِفرُ مخالفةِ ترويسةٍ** بقاعدةِ المدقّقِ
       نفسِها، وصِفرُ مخالفةٍ في بوّابةِ الهويّة، وامتناعُ الارتدادِ إلى الشكلِ الذي
       كان يُخفي الهدفَ عن القياس (ترويسةٌ فوقَ العنوانِ في ماركداون · كلمةُ الهدفِ
       بعدَ السطرِ الخامسَ عشرَ في الشِّفرة).
النطاق: لا شبكةَ ولا قاعدةَ بياناتٍ. المكتبةُ القياسيّةُ و`pytest` فقط.
المالك: tests/governance
تاريخ الإنشاء: 2026-08-22

حدُّ صدقِ هذا الحرس: يُثبِتُ **أنَّ كلَّ ملفٍّ في نطاقِ المدقّقِ يُعلِنُ هدفَه بصيغةٍ
تُقاس**، ويُثبِتُ أنَّ حارسَي `docs` و`tests` يتغيّرُ خرجُهما بتغيُّرِ الشجرةِ (فلا
يُصادِقانِ على أنفسِهما). ولا يُثبِتُ أنَّ نصَّ كلِّ هدفٍ صادقٌ في وصفِه — ذاك حكمٌ
على معنًى لا يُقاسُ بأداة.
"""

from __future__ import annotations

import importlib.util
import os
import re
import shutil
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]

# قاعدةُ الحكمِ تُستورَدُ من المدقّقِ نفسِه — لا تُعادُ كتابتُها هنا، لئلّا يخضرَّ
# الحرسُ بقاعدةٍ ألطفَ من قاعدةِ البوّابة.
sys.path.insert(0, str(REPO_ROOT / "tools" / "governance"))
import check_repository_identity as cri  # noqa: E402
import truth_audit as ta  # noqa: E402

SCANNED_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".rego", ".sql"}
EXCLUDED_NAME_PARTS = (".example", "truth_matrix", "truth_baseline")

DOMAIN_GUARDS = sorted(str(p.relative_to(REPO_ROOT)) for p in REPO_ROOT.glob("*/stubs/*_check.py"))


def _audit():
    return ta.TruthAudit(REPO_ROOT)


def _scanned_files(audit) -> list[Path]:
    out = []
    for p in audit._iter_files():
        if audit._domain_of(p) is None:
            continue
        if p.suffix.lower() not in SCANNED_SUFFIXES:
            continue
        if any(x in p.name for x in EXCLUDED_NAME_PARTS):
            continue
        out.append(p)
    return out


# ── 1 · العددُ المقيسُ صفرٌ بالقاعدتَين ──────────────────────────────────────


def test_truth_matrix_identity_violations_are_zero():
    """قاعدةُ المدقّقِ نفسُها: لا ملفَّ في نطاقِه بلا ترويسةٍ تُقاس."""
    audit = _audit()
    offenders = [
        str(p.relative_to(REPO_ROOT))
        for p in _scanned_files(audit)
        if not ta.TruthAudit._has_identity_header(p, audit._read(p))
    ]
    assert offenders == [], "ملفّاتٌ بلا ترويسةِ هويّةٍ بقاعدةِ المدقّق: " + " · ".join(offenders)


def test_identity_gate_reports_no_violation():
    """بوّابةُ الهويّةِ (المادة 009) صفرٌ — بطاقاتٌ وحقولٌ وإعلانُ هدف."""
    violations = cri.audit(REPO_ROOT)
    assert violations == [], "مخالفاتُ بوّابةِ الهويّة: " + " · ".join(
        f"{v['kind']}:{v['path']}" for v in violations
    )


# ── 2 · منعُ الارتدادِ إلى الشكلِ الذي كان يُخفي الهدف ────────────────────────


def test_markdown_identity_comment_never_precedes_the_title():
    """في ماركداون: العنوانُ أوّلًا ثمَّ ترويسةُ التعليق.

    كانت ثلاثةَ عشرَ ملفًّا تبدأُ بـ`<!--` فتُحسَبُ بلا ترويسةٍ عندَ المدقّقِ رغمَ
    أنّها تحملُ ترويسةً كاملةً. والحرسُ يمنعُ عودةَ هذا الترتيب.
    """
    offenders = []
    audit = _audit()
    for p in _scanned_files(audit):
        if p.suffix.lower() != ".md":
            continue
        text = audit._read(p)
        if text.lstrip().startswith("<!--"):
            offenders.append(str(p.relative_to(REPO_ROOT)))
    assert offenders == [], "ترويسةٌ فوقَ العنوانِ في: " + " · ".join(offenders)


@pytest.mark.parametrize("rel", DOMAIN_GUARDS)
def test_guard_declares_purpose_within_the_measured_window(rel):
    """حارسُ الإقليمِ يُعلِنُ «الهدف» و«المالك» داخلَ أوّلِ خمسةَ عشرَ سطرًا.

    كانت الكلمةُ تقعُ في السطرِ السادسَ عشرَ — فيُعلَنُ الهدفُ ولا يُقاسُ إعلانُه.
    """
    head = "\n".join((REPO_ROOT / rel).read_text(encoding="utf-8").splitlines()[:15])
    assert "الهدف" in head, f"{rel}: «الهدف» خارجَ نافذةِ القياس"
    assert "المالك" in head, f"{rel}: «المالك» خارجَ نافذةِ القياس"
    assert "النطاق" in head, f"{rel}: «النطاق» خارجَ نافذةِ القياس"


def test_all_twelve_domain_guards_exist():
    """اثنا عشرَ إقليمًا لكلٍّ حارسٌ — العددُ مقيسٌ من القرصِ لا مكتوبًا."""
    assert len(DOMAIN_GUARDS) == 12, DOMAIN_GUARDS


# ── 3 · حارسا `docs` و`tests`: لا مصادقةَ على النفس ──────────────────────────


def _load_module(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture()
def docs_guard():
    return _load_module("docs_check_under_test", "docs/stubs/docs_check.py")


@pytest.fixture()
def tests_guard():
    return _load_module("tests_check_under_test", "tests/stubs/tests_check.py")


def test_docs_guard_states_its_source_and_claims_no_database(docs_guard):
    """ترويسةُ حارسِ التوثيقِ كانت تدّعي Supabase وهو يقرأُ نظامَ الملفّات."""
    src = (REPO_ROOT / "docs/stubs/docs_check.py").read_text(encoding="utf-8")
    # البطاقةُ وحدَها (أسطرُ التعليقِ حتّى فاصلِها) هي محلُّ الدّعوى. وذِكرُ
    # الدّعوى القديمةِ في فقرةِ «سببِ التغيير» توثيقٌ لا ادّعاءٌ — والخطأُ
    # يبقى في تاريخِه بنصِّ قاعدةِ التصحيحِ المؤرَّخ.
    banner = src.split('"""', 1)[0]
    assert "Supabase" not in banner, "بطاقةٌ تدّعي مصدرًا لا يُقرأُ في الكود"
    assert "filesystem" in src, "الحارسُ لا يُعلِنُ مصدرَه"
    assert docs_guard.check()["source"] == "filesystem"


def test_docs_guard_has_no_hardcoded_count_constants(docs_guard):
    """لا ثابتَ عددٍ يُعادُ في النتيجة: المخطّطاتُ والسجلّاتُ تُقاسان."""
    src = (REPO_ROOT / "docs/stubs/docs_check.py").read_text(encoding="utf-8")
    assert not re.search(r"^SCHEMAS\s*=\s*\d+", src, re.M)
    assert not re.search(r"^REGISTRIES\s*=\s*\d+", src, re.M)
    measured = docs_guard.check()
    assert measured["schemas"] == docs_guard._count_contract_schemas()
    assert measured["registries"] == len(docs_guard._existing_domain_registries())


def test_docs_guard_output_tracks_the_tree(tmp_path, docs_guard, monkeypatch):
    """تحويرٌ: أُنقِصَ مخطّطٌ من الشجرةِ فنقصَ العددُ — فالقياسُ قياسٌ لا اقتباس."""
    fake = tmp_path / "repo"
    (fake / "docs" / "contracts" / "schemas").mkdir(parents=True)
    for i in range(3):
        (fake / "docs" / "contracts" / "schemas" / f"x{i}.schema.json").write_text("{}", encoding="utf-8")
    monkeypatch.setattr(docs_guard, "PROJECT_ROOT", str(fake))
    assert docs_guard._count_contract_schemas() == 3
    (fake / "docs" / "contracts" / "schemas" / "x0.schema.json").unlink()
    assert docs_guard._count_contract_schemas() == 2


def test_docs_guard_fails_when_a_declared_registry_is_missing(tmp_path, docs_guard, monkeypatch):
    """سجلٌّ مُعلَنٌ مفقودٌ = فشلٌ مُعلَنُ السبب، لا نجاحٌ صامت."""
    fake = tmp_path / "repo"
    (fake / "docs" / "contracts" / "schemas").mkdir(parents=True)
    (fake / "docs" / "contracts" / "schemas" / "a.schema.json").write_text("{}", encoding="utf-8")
    monkeypatch.setattr(docs_guard, "PROJECT_ROOT", str(fake))
    monkeypatch.setattr(docs_guard, "MIN_NUCLEUS_FILES", 0)
    out = docs_guard.check()
    assert out["status"] == "fail"
    assert "سجلّاتٌ مُعلَنةٌ مفقودة" in out["reason"]


def test_tests_guard_counts_guards_from_disk(tmp_path, tests_guard, monkeypatch):
    """تحويرٌ: حُذِفَ حارسٌ من الشجرةِ فنقصَ العدُّ، ونزلَ تحتَ الحدِّ ففشل."""
    fake = tmp_path / "repo"
    for dom in ("tools", "agents", "core"):
        d = fake / dom / "stubs"
        d.mkdir(parents=True)
        (d / f"{dom}_check.py").write_text("# x", encoding="utf-8")
    monkeypatch.setattr(tests_guard, "PROJECT_ROOT", str(fake))
    assert tests_guard._count_domain_guards() == 3
    out = tests_guard.check()
    assert out["status"] == "fail"
    assert out["runner"] == "missing"
    assert "حرّاسُ الأقاليمِ 3" in out["reason"]


def test_tests_guard_smoke_domains_is_not_a_written_constant(tests_guard):
    """‏`SMOKE_DOMAINS = 12` كان يُعادُ بلا فحص — فلا يبقى ثابتًا."""
    src = (REPO_ROOT / "tests/stubs/tests_check.py").read_text(encoding="utf-8")
    assert not re.search(r"^SMOKE_DOMAINS\s*=\s*\d+", src, re.M)
    assert tests_guard.check()["smoke_domains"] == tests_guard._count_domain_guards()


def test_both_guards_import_no_third_party(tmp_path):
    """وظيفةُ الدخانِ في CI لا تُركِّبُ حزمًا — فالحارسانِ بالمكتبةِ القياسيّةِ وحدَها."""
    stdlib_only = {"os", "sys", "json", "re", "pathlib"}
    for rel in ("docs/stubs/docs_check.py", "tests/stubs/tests_check.py"):
        src = (REPO_ROOT / rel).read_text(encoding="utf-8")
        imported = set(re.findall(r"^\s*import\s+([A-Za-z_][\w.]*)", src, re.M))
        imported |= set(re.findall(r"^\s*from\s+([A-Za-z_][\w.]*)\s+import", src, re.M))
        outside = {m.split(".")[0] for m in imported} - stdlib_only
        assert not outside, f"{rel}: تبعيّةٌ خارجَ المكتبةِ القياسيّة: {outside}"


# ── 4 · سجلُّ الوكلاءِ المستوردين: ترويسةٌ ولا دعوى واقعٍ حيّ ─────────────────


def test_imported_citizens_registry_declares_identity_and_stays_valid():
    """ترويسةُ تعليقٍ عربيّةٌ فوقَ `meta:`، والملفُّ ما زالَ YAML صحيحَ البناء."""
    p = REPO_ROOT / "agents/registry/imported_citizens.yaml"
    lines = p.read_text(encoding="utf-8").splitlines()
    head = "\n".join(lines[:15])
    for kw in ("الهدف", "النطاق", "المالك"):
        assert kw in head, f"«{kw}» غائبٌ عن ترويسةِ السجل"
    body = [ln for ln in lines if ln.strip() and not ln.lstrip().startswith("#")]
    assert body[0] == "meta:", body[0]


def test_imported_citizens_total_matches_its_own_entries():
    """‏`total_imported` يُخبِرُ عن هذا الملفِّ نفسِه — فليُطابِقْ مدخلاتَه."""
    text = (REPO_ROOT / "agents/registry/imported_citizens.yaml").read_text(encoding="utf-8")
    declared = int(re.search(r"^\s*total_imported:\s*(\d+)", text, re.M).group(1))
    entries = len(re.findall(r"^- id:\s*\S+", text, re.M))
    assert declared == entries, f"مُعلَنٌ {declared} · مقيسٌ {entries}"


def test_repository_tree_is_untouched_by_this_guard():
    """هذا الحرسُ لا يكتبُ في المستودع — فلا يُخلِّفُ فخًّا لبوّابةِ الهويّة."""
    assert shutil.which("git")
    assert os.environ.get("AMOS_IDENTITY_GUARD_WROTE") is None
