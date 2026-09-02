"""الهدف: حرسُ إغلاقِ تبعيّاتِ البوّاباتِ في `tools/governance/gate_dependency_closure.py` (W-053).

المالك · Owner: — (غيرُ معيَّن) · تُسنَدُ إلى نطاقِ `tooling-gates`.
النطاق: الأداةُ وحدَها — تفكيكُ مسارِ CI نصًّا، وحصرُ ما تُثبِّتُه وظيفةٌ، وتتبُّعُ
الاستيراداتِ عبورًا، وتصنيفُ الوحداتِ، والرفضُ المُصنَّفُ برمزِ 2، والأساسُ
`KNOWN_OPEN` بشرطَيه (‏لا يُزادُ بلا مُوجِّهٍ، ولا يبقى بعدَ إصلاحٍ).

لماذا هذا الحرس
---------------
`RK-010` كانَ تخفيفُه نصًّا في سجلِّ المخاطرِ: «كلُّ بوّابةٍ بالمكتبةِ القياسيّةِ
وحدَها أو تُعلَنُ تبعيّتُها» — ولا شيءَ في الشجرةِ يقيسُه. والحرسُ القائمُ
`test_root_dependencies_declared.py` يقيسُ الاتِّجاهَ الواحدَ (‏الإعلاناتُ قائمةٌ
ولا اسمَ حزمةٍ عاريًا في CI) ولا يقيسُ المقابلَ: **أنَّ ما تستوردُه بوّابةٌ
مُثبَّتٌ في الوظيفةِ التي تُشغِّلُها**. وقد تحقَّقَ الخطرُ مرّتَينِ في هذه الشجرةِ:
سقوطٌ بـ`ModuleNotFoundError: sqlalchemy` مكتوبٌ في
`tests/governance/test_w036_pricing_divergence.py`، وسقوطٌ قائمٌ اليومَ بـ
`ModuleNotFoundError: amos_federation` في `sovereignty-kernel` (`DISC-009`).

وكلُّ فحصٍ هنا يبني **مستودعًا مُصطنَعًا في دليلٍ موقوتٍ** — لا شبكةَ، ولا تركيبَ
حزمةٍ، ولا اعتمادَ على شجرةِ هذا المستودعِ إلّا في فحوصِ الواقعِ المُعلَنةِ.

وحدُّ صدقِ هذا الحرس: يُثبِتُ أنَّ الأداةَ تقيسُ ما تدَّعي قياسَه وترفضُ حينَ لا
تقدرُ، **ولا** يُثبِتُ أنَّ CI أخضرُ ولا أنَّ العطبَ المقيسَ أُصلِحَ — إصلاحُه قرارُ
المالكِ، والأداةُ تكشِفُ ولا تُصلِحُ.
"""

from __future__ import annotations

import ast
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

ROOT = discover_repo_root(__file__)
TOOL = ROOT / "tools/governance/gate_dependency_closure.py"
SOURCE = TOOL.read_text(encoding="utf-8")

sys.path.insert(0, str(ROOT / "tools" / "governance"))
import gate_dependency_closure as gdc  # noqa: E402


# ═══════════════════════════════════════════════════════════════════════════
# ٠ — تجهيزاتٌ محكمةٌ: مستودعٌ مُصطنَعٌ يُبنى في الفحصِ
# ═══════════════════════════════════════════════════════════════════════════
def _write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip("\n"), encoding="utf-8")
    return path


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """شجرةٌ صغيرةٌ تكفي للقياسِ: إعلانٌ واحدٌ ومسارٌ واحدٌ."""
    _write(tmp_path / "requirements-dev.txt", "pytest>=8.3.3\ncryptography>=43.0.1\n")
    return tmp_path


@pytest.fixture(autouse=True)
def _isolate_search_roots():
    """أدلّةُ البحثِ حالةٌ عامّةٌ في الأداةِ — تُنظَّفُ كي لا يُلوِّثَ فحصٌ فحصًا."""
    before = set(gdc._SEARCH_ROOTS)
    yield
    gdc._SEARCH_ROOTS.clear()
    gdc._SEARCH_ROOTS.update(before)


def _measure(repo_root: Path) -> dict[str, object]:
    return gdc.measure(repo_root)


def _job(payload: dict[str, object], name: str) -> dict[str, object]:
    for row in payload["detail"]:  # type: ignore[index]
        if row["job"] == name:
            return row  # type: ignore[return-value]
    raise AssertionError(f"وظيفةٌ لم تُقَسْ: {name}")


# ═══════════════════════════════════════════════════════════════════════════
# ١ — الحكمُ الأساسيُّ: نقصٌ يُكشَفُ، وإغلاقٌ يُشهَدُ به
# ═══════════════════════════════════════════════════════════════════════════
def test_missing_dependency_is_detected(repo: Path) -> None:
    """بوّابةٌ تستوردُ حزمةً لا تُثبِّتُها وظيفتُها = نقصٌ مكشوفٌ لا خُضرةٌ."""
    _write(repo / "requirements-tools.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import yaml\nprint(yaml)\n")
    row = _job(_measure(repo), "g")
    assert row["missing"] == ["pyyaml"], row
    assert row["verdict"] == "OPEN"


def test_declared_dependency_is_closed(repo: Path) -> None:
    """وحينَ تُثبِّتُ الوظيفةُ ما تستوردُه البوّابةُ يُشهَدُ بالإغلاقِ."""
    _write(repo / "requirements-tools.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: pip install -r requirements-tools.txt
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import yaml\nprint(yaml)\n")
    row = _job(_measure(repo), "g")
    assert row["missing"] == []
    assert row["verdict"] == "CLOSED"
    assert "pyyaml" in row["needed"]  # type: ignore[operator]


def test_stdlib_only_gate_needs_nothing(repo: Path) -> None:
    """بوّابةٌ بالمكتبةِ القياسيّةِ وحدَها لا تحتاجُ إعلانًا — وهذا نصُّ التخفيفِ."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import ast\nimport json\nimport tomllib\nprint(ast, json, tomllib)\n")
    row = _job(_measure(repo), "g")
    assert row["needed"] == []
    assert row["installed_count"] == 0
    assert row["verdict"] == "CLOSED"


# ═══════════════════════════════════════════════════════════════════════════
# ٢ — العبورُ: الاستيرادُ غيرُ المباشرِ يُحسَبُ
# ═══════════════════════════════════════════════════════════════════════════
def test_transitive_import_is_counted(repo: Path) -> None:
    """حزمةٌ يستوردُها ملفٌّ **يستوردُه** المدخلُ تلزمُ الوظيفةَ كما لو استوردَها."""
    _write(repo / "requirements-tools.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/entry.py
        """,
    )
    _write(repo / "tools/entry.py", "import helper\nprint(helper)\n")
    _write(repo / "tools/helper.py", "import yaml\nprint(yaml)\n")
    row = _job(_measure(repo), "g")
    assert row["missing"] == ["pyyaml"], "لم يُتبَّعْ الاستيرادُ عبورًا"


def test_sys_path_insert_resolves_local_module(repo: Path) -> None:
    """وحدةٌ بلغَها الفحصُ بـ`sys.path.insert` محليّةٌ لا طرفٌ ثالثٌ."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python -m pytest tests/
        """,
    )
    _write(repo / "tools/governance/mygate.py", "import json\nprint(json)\n")
    _write(
        repo / "tests/test_a.py",
        """
        import sys
        from pathlib import Path

        REPO = Path(__file__).resolve().parents[1]
        sys.path.insert(0, str(REPO / "tools" / "governance"))
        import mygate
        """,
    )
    row = _job(_measure(repo), "g")
    assert row["missing"] == [], row
    assert row["verdict"] == "CLOSED"


def test_string_constants_follow_source_order() -> None:
    """ترتيبُ الحروفِ الثابتةِ ترتيبُ المصدرِ — والعرضُ يقلِبُه فيَكذبُ القياسُ.

    عيبٌ وقعَ فعلًا في بناءِ هذه الأداةِ: `ast.walk` أعادَ `governance` قبلَ
    `tools`، فبُنيَ دليلٌ لا وجودَ له، فعُدَّت وحدةٌ محليّةٌ طرفًا ثالثًا.
    """
    tree = ast.parse('import sys\nsys.path.insert(0, str(R / "tools" / "governance"))\n')
    call = next(
        n for n in ast.walk(tree) if isinstance(n, ast.Call) and getattr(n.func, "attr", "") == "insert"
    )
    assert gdc._string_constants(call) == ["tools", "governance"]


# ═══════════════════════════════════════════════════════════════════════════
# ٣ — الاستيرادُ المحروسُ ليسَ نقصًا
# ═══════════════════════════════════════════════════════════════════════════
@pytest.mark.parametrize(
    "handler",
    ["ImportError", "ModuleNotFoundError", "Exception", "BaseException"],
)
def test_guarded_import_is_not_missing(repo: Path, handler: str) -> None:
    """فقدانٌ يُمسَكُ ويُترجَمُ إلى تخطٍّ مُعلَنٍ ليسَ تبعيّةً لازمةً للوظيفةِ."""
    _write(repo / "requirements-tools.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/g.py
        """,
    )
    _write(
        repo / "tools/g.py",
        f"""
        def f():
            try:
                import yaml
            except {handler}:
                return None
            return yaml
        """,
    )
    row = _job(_measure(repo), "g")
    assert row["missing"] == [], f"استيرادٌ محروسٌ بـ{handler} عُدَّ نقصًا — حُمرةٌ بلا سببٍ"


def test_unguarded_import_in_function_is_missing(repo: Path) -> None:
    """وبلا حراسةٍ يُعَدُّ نقصًا وإن كانَ داخلَ دالّةٍ: يُنفَّذُ حينَ تُنادى."""
    _write(repo / "requirements-tools.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "def f():\n    import yaml\n    return yaml\n")
    assert _job(_measure(repo), "g")["missing"] == ["pyyaml"]


def test_guard_requires_import_error_family(repo: Path) -> None:
    """و`try` يمسِكُ `ValueError` وحدَه لا يحرسُ شيئًا — فالنقصُ يبقى نقصًا."""
    _write(repo / "requirements-tools.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/g.py
        """,
    )
    _write(
        repo / "tools/g.py",
        """
        try:
            import yaml
        except ValueError:
            yaml = None
        """,
    )
    assert _job(_measure(repo), "g")["missing"] == ["pyyaml"]


# ═══════════════════════════════════════════════════════════════════════════
# ٤ — الرفضُ المُصنَّفُ: خروجٌ 2 لا حكمٌ
# ═══════════════════════════════════════════════════════════════════════════
def _run(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL), str(repo_root), *args],
        capture_output=True,
        text=True,
        check=False,
        timeout=600,
    )


def test_refuses_when_no_workflows(tmp_path: Path) -> None:
    """لا دليلَ مساراتٍ = لا شيءَ يُقاسُ: رفضٌ برمزِ 2 لا خُضرةٌ برمزِ 0."""
    out = _run(tmp_path, "--check")
    assert out.returncode == 2, out
    assert out.stderr.startswith("REFUSED:")


def test_refuses_on_unknown_module(repo: Path) -> None:
    """وحدةٌ لا يُعرَفُ اسمُ توزيعِها: رفضٌ — وتخمينُها يُنتِجُ نقصًا كاذبًا."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import zzz_not_declared_anywhere\n")
    out = _run(repo, "--check")
    assert out.returncode == 2, out
    assert "لا تُصنَّفُ" in out.stderr


def test_refuses_on_unparseable_python(repo: Path) -> None:
    """ملفٌّ يُبلَغُ من بوّابةٍ ولا يُفكَّكُ: رفضٌ — لا يُمَرُّ عليه صامتًا."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "def (:\n")
    out = _run(repo, "--check")
    assert out.returncode == 2
    assert "لا يُفكَّكُ" in out.stderr


def test_refuses_on_missing_requirements_file(repo: Path) -> None:
    """ملفُّ متطلّباتٍ مذكورٌ في مسارٍ وغيرُ موجودٍ: رفضٌ لا تجاهلٌ."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-ghost.txt
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import json\n")
    out = _run(repo, "--check")
    assert out.returncode == 2
    assert "غيرُ موجودٍ" in out.stderr


def test_refuses_on_unresolvable_pip_argument(repo: Path) -> None:
    """وسيطُ `pip install` لا يُحسَمُ إلى إعلانٍ: رفضٌ — والتخمينُ يُخضِّرُ بلا قياسٍ."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install ${{ env.SOMETHING }}
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import json\n")
    out = _run(repo, "--check")
    assert out.returncode == 2
    assert "لا يُحسَمُ" in out.stderr


def test_refuses_on_workflow_without_jobs(repo: Path) -> None:
    """ملفُّ مسارٍ بلا `jobs`: بنيةٌ لا تُفكَّكُ نصًّا — رفضٌ لا صفرُ وظائفَ."""
    _write(repo / ".github/workflows/ci.yml", "name: t\non: [push]\n")
    out = _run(repo, "--check")
    assert out.returncode == 2
    assert "jobs" in out.stderr


def test_exit_one_on_unexpected_open(repo: Path) -> None:
    """نقصٌ حقيقيٌّ غيرُ مُقيَّدٍ = حكمٌ سلبيٌّ (1) — يُميَّزُ عن الرفضِ (2)."""
    _write(repo / "requirements-tools.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import yaml\n")
    out = _run(repo, "--check")
    assert out.returncode == 1, out
    assert "pyyaml" in out.stderr


# ═══════════════════════════════════════════════════════════════════════════
# ٥ — الأداةُ تقيسُ ولا تكتبُ · وبالمكتبةِ القياسيّةِ وحدَها
# ═══════════════════════════════════════════════════════════════════════════
def test_tool_imports_stdlib_only() -> None:
    """أداةٌ تحرسُ إعلانَ التبعيّاتِ ثمَّ تلزمُها تبعيّةٌ = مثالُ العطبِ الذي تحرسُ منه."""
    tree = ast.parse(SOURCE)
    tops: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            tops |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            tops.add(node.module.split(".")[0])
    third_party = sorted(t for t in tops if t not in gdc.STDLIB)
    assert third_party == [], f"الأداةُ تستوردُ طرفًا ثالثًا: {third_party}"


def test_tool_does_not_write(repo: Path) -> None:
    """لا كتابةَ ولا تركيبَ: بصمةُ الشجرةِ قبلَ التشغيلِ وبعدَه واحدةٌ."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import json\n")

    def snapshot() -> list[tuple[str, int]]:
        return sorted(
            (str(p.relative_to(repo)), p.stat().st_size)
            for p in repo.rglob("*")
            if p.is_file()
        )

    before = snapshot()
    assert _run(repo, "--check").returncode == 0
    assert snapshot() == before, "الأداةُ غيَّرَت الشجرةَ — والقياسُ لا يكتبُ"


def test_source_has_no_installer_call() -> None:
    """ولا تُثبِّتُ حزمةً ولا تُصلِحُ مسارًا: لا `pip install` مُنفَّذًا في الشِفرةِ."""
    code = "\n".join(
        ln for ln in SOURCE.splitlines() if not ln.lstrip().startswith("#")
    )
    body = ast.parse(code)
    calls = [
        n
        for n in ast.walk(body)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr in {"run", "check_output", "check_call", "Popen", "system"}
    ]
    assert calls == [], "الأداةُ تُشغِّلُ عمليّةً — والقياسُ لا يُنفِّذُ ولا يُثبِّتُ"


# ═══════════════════════════════════════════════════════════════════════════
# ٦ — الأساسُ ترباسٌ لا رخصةٌ
# ═══════════════════════════════════════════════════════════════════════════
def test_every_baseline_entry_is_routed() -> None:
    """كلُّ عطبٍ مُقيَّدٍ في الأساسِ له مُوجِّهٌ وسببٌ — وإلّا فهو عطبٌ مطويٌّ."""
    assert gdc.KNOWN_OPEN, "أساسٌ فارغٌ: إن أُصلِحَ العطبُ فليُحذَفْ من الشِفرةِ لا يُفرَّغْ"
    for key, entry in gdc.KNOWN_OPEN.items():
        assert entry.get("missing"), f"{key}: مدخلٌ بلا نقصٍ مُسمًّى"
        routed = str(entry.get("routed", ""))
        assert routed.startswith(("DISC-", "RK-")), f"{key}: بلا مُوجِّهٍ — عطبٌ مطويٌّ"
        assert len(str(entry.get("why", ""))) > 60, f"{key}: بلا سببٍ مكتوبٍ"


def test_stale_baseline_fails(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """وإن أُصلِحَ العطبُ وبقيَ اسمُه في الأساسِ سقطَتِ الأداةُ — لا تُخضِّرُ على قِدَمٍ."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import json\n")
    monkeypatch.setitem(
        gdc.KNOWN_OPEN,
        ("ci.yml", "g"),
        {"missing": ["pyyaml"], "routed": "DISC-999", "why": "x" * 61},
    )
    assert gdc.main([str(repo), "--check"]) == 1


def test_baseline_only_absolves_its_own_job(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """والأساسُ يُبرِّئُ وظيفتَه وحدَها: نقصُ وظيفةٍ أخرى يبقى حكمًا سلبيًّا."""
    _write(repo / "requirements-tools.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import yaml\n")
    monkeypatch.setitem(
        gdc.KNOWN_OPEN,
        ("ci.yml", "other"),
        {"missing": ["pyyaml"], "routed": "DISC-999", "why": "x" * 61},
    )
    assert gdc.main([str(repo), "--check"]) == 1


# ═══════════════════════════════════════════════════════════════════════════
# ٧ — أدلّةُ العملِ الحقيقيّةِ: دليلٌ ومشروعٌ قابلٌ للتحريرِ
# ═══════════════════════════════════════════════════════════════════════════
def test_working_directory_is_honoured(repo: Path) -> None:
    """`working-directory` يُغيِّرُ موضِعَ الملفِّ المُشغَّلِ وموضِعَ الإعلانِ معًا."""
    _write(repo / "svc/requirements-dev.txt", "PyYAML>=6.0.3\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            defaults:
              run:
                working-directory: svc
            steps:
              - run: pip install -r requirements-dev.txt
              - run: python tools/g.py
        """,
    )
    _write(repo / "svc/tools/g.py", "import yaml\n")
    row = _job(_measure(repo), "g")
    assert row["working_directory"] == "svc"
    assert row["missing"] == [], row


def test_editable_install_provides_its_own_modules(repo: Path) -> None:
    """مشروعٌ محليٌّ رُكِّبَ قابلًا للتحريرِ يُوفِّرُ وحداتِه — فليست طرفًا ثالثًا."""
    _write(
        repo / "svc/pyproject.toml",
        """
        [project]
        name = "mypkg"
        version = "0.1.0"
        dependencies = ["cryptography>=43"]

        [tool.setuptools.packages.find]
        where = ["src"]
        """,
    )
    _write(repo / "svc/src/mypkg/__init__.py", "")
    _write(repo / "svc/src/mypkg/thing.py", "import json\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -e svc
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "from mypkg.thing import json\n")
    row = _job(_measure(repo), "g")
    assert row["missing"] == [], row
    assert "mypkg" in row["needed"] or row["needed"] == []


def test_no_deps_editable_does_not_grant_dependencies(repo: Path) -> None:
    """و`--no-deps` لا يُثبِّتُ تبعيّاتِ المشروعِ: نقصُها نقصٌ حقيقيٌّ."""
    _write(
        repo / "svc/pyproject.toml",
        """
        [project]
        name = "mypkg"
        version = "0.1.0"
        dependencies = ["PyYAML>=6.0.3"]

        [tool.setuptools.packages.find]
        where = ["src"]
        """,
    )
    _write(repo / "svc/src/mypkg/__init__.py", "import yaml\n")
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: pip install -e svc --no-deps
              - run: python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import mypkg\n")
    assert _job(_measure(repo), "g")["missing"] == ["pyyaml"]


def test_comments_are_not_commands(repo: Path) -> None:
    """سطرٌ مُعلَّقٌ لا يُنفِّذُ شيئًا — فلا يُقرأُ تركيبًا ولا تشغيلًا."""
    _write(
        repo / ".github/workflows/ci.yml",
        """
        name: t
        on: [push]
        jobs:
          g:
            runs-on: ubuntu-latest
            steps:
              - run: |
                  # pip install ${{ env.X }}
                  python tools/g.py
        """,
    )
    _write(repo / "tools/g.py", "import json\n")
    out = _run(repo, "--check")
    assert out.returncode == 0, out.stderr


# ═══════════════════════════════════════════════════════════════════════════
# ٨ — على الواقعِ: هذه الشجرةُ نفسُها
# ═══════════════════════════════════════════════════════════════════════════
def test_real_tree_is_measured_and_open_defect_is_the_known_one() -> None:
    """على الشجرةِ الحقيقيّةِ: القياسُ يقعُ، والمفتوحُ هو المُقيَّدُ وحدَه.

    والعددُ مُعلَنٌ لا مُدَّعًى: 15 وظيفةً في المساراتِ الثلاثةِ، تُقاسُ منها
    التي تُشغِّلُ مدخلَ بايثونَ — و`lint` و`lockfile-check` لا تُشغِّلانِ.
    """
    payload = gdc.measure(ROOT)
    assert payload["jobs_measured"] >= 13
    assert payload["unexpected_open"] == {}
    assert payload["stale_baseline"] == []
    assert _job(payload, "sovereignty-kernel")["missing"] == ["amos-federation"]


def test_real_tree_verdict_is_zero() -> None:
    """وحكمُها صفرٌ: مفتوحٌ واحدٌ مُقيَّدٌ مُوجَّهٌ، لا نقصٌ مُفلِتٌ."""
    assert gdc.main([str(ROOT), "--check"]) == 0
