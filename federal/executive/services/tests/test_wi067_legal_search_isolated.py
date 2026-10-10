"""
AMOS-Federation — `legal_search` داخلَ صندوقٍ معزولٍ فعلًا (WI-067 · قرارُ المالكِ في Q-33)
الهدف: أن يُثبَتَ **بالتشغيلِ لا بالتصريح** أنَّ `legal_search` (1) يبحثُ في نصِّ الدستورِ الحقيقيّ،
       (2) داخلَ صندوقٍ تفرضُ النواةُ عزلَه — لا شبكة، ولا رؤيةَ لنظامِ ملفّاتِ المضيف، ولا كتابةَ
       في المدوَّنة، ولا عمليّاتِ المضيف، ولا صلاحيّات، ولا أسرارَ بيئته، و(3) يرفضُ ولا يُنفِّذُ
       حينَ يغيبُ العزل — لا سقوطَ إلى المضيفِ ولا محاكاة.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-10 (WI-067)
تاريخ آخر تعديل: 2026-10-10 (WI-067)

## متى تُتخطّى الاختباراتُ الحيّة — ولماذا

تلك التي تُشغِّلُ الصندوقَ تحتاجُ bubblewrap ومساحاتِ أسماءِ مستخدمٍ تسمحُ بها النواة.
فإن لم تتوفّرْ تُتخطّى **بسببِ المزوِّدِ نفسِه** (‏`availability().reason`) — لا لتبدوَ خضراء: والاختبارُ
الذي يُثبِتُ الرفضَ عندَ الغيابِ يجري في كلِّ بيئة.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from amos_federation.services.executive_core.fidelity import ExecutionFidelity
from amos_federation.services.tool_registry.legal_search import CORPUS_MOUNT, corpus_dir
from amos_federation.services.tool_registry.providers.contract import (
    ExecutionRequest,
    ProviderAvailability,
    SandboxSpec,
)
from amos_federation.services.tool_registry.providers.isolated_provider import (
    BubblewrapProvider,
)
from amos_federation.services.tool_registry.providers.selection import execute_in_sandbox
from amos_federation.services.tool_registry.sandbox import _execute_isolated


def execute_legal_search(params, *, provider=None):  # noqa: ANN001, ANN201
    """المنفِّذُ المعزولُ بعدَ التخويل — يُستدعى هنا مباشرةً لقياسِ الصندوقِ لا التخويل."""
    return _execute_isolated("legal_search", params, provider=provider)


CORPUS = corpus_dir()
PROVIDER = BubblewrapProvider({CORPUS_MOUNT: str(CORPUS)}) if CORPUS else None
_STATE = PROVIDER.availability() if PROVIDER else None
#: `AMOS_REQUIRE_ISOLATION=1` في بيئةٍ يُعرَفُ أنَّ الصندوقَ فيها متاح: الغيابُ فشلٌ لا تخطٍّ —
#: فلا يختبئُ إضعافٌ للعزلِ يُفشِلُ السبرَ خلفَ التخطّي.
_REQUIRED = os.environ.get("AMOS_REQUIRE_ISOLATION") == "1"
live = pytest.mark.skipif(
    not _REQUIRED and (_STATE is None or not _STATE.available),
    reason=f"الصندوقُ غيرُ متاحٍ في هذه البيئة: {_STATE.reason if _STATE else 'لا مدوَّنة'}",
)

_FACTS = r"""
import json, os, socket
r = {}
try:
    socket.create_connection(("1.1.1.1", 53), timeout=2)
    r["net"] = "OPEN"
except OSError as e:
    r["net"] = e.errno
r["host_home"] = os.path.exists("/home")
r["etc_passwd"] = os.path.exists("/etc/passwd")
r["corpus_md"] = sum(1 for d, _, fs in os.walk("/corpus") for f in fs if f.endswith(".md"))
for target in ("/corpus/x", "/usr/x"):
    try:
        open(target, "w")
        r[target] = "WROTE"
    except OSError:
        r[target] = "DENIED"
r["pids"] = sorted(int(d) for d in os.listdir("/proc") if d.isdigit())
r["cap_eff"] = [l.split()[1] for l in open("/proc/self/status") if l.startswith("CapEff")][0]
r["env"] = sorted(os.environ)
print(json.dumps(r))
"""


@live
def test_the_kernel_enforces_the_isolation(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    # نسخةٌ من المدوَّنة: إن انكسرَ التركيبُ للقراءةِ وحدَها كتبَ الاختبارُ في النسخةِ لا في الدستور.
    import shutil

    copy = tmp_path / "corpus"
    shutil.copytree(CORPUS, copy)
    monkeypatch.setenv("AMOS_WI067_HOST_SECRET", "must-not-cross")
    result = execute_in_sandbox(
        SandboxSpec(tool_id="legal_search"),
        ExecutionRequest(code=_FACTS),
        provider=BubblewrapProvider({CORPUS_MOUNT: str(copy)}),
    )
    assert result.succeeded, result.stderr
    facts = json.loads(result.stdout)
    assert facts["net"] != "OPEN"  # ENETUNREACH من النواة
    assert facts["host_home"] is False
    assert facts["etc_passwd"] is False
    assert facts["corpus_md"] == len(list(CORPUS.rglob("*.md")))
    assert facts["/corpus/x"] == "DENIED"
    assert not (copy / "x").exists()
    assert facts["/usr/x"] == "DENIED"
    assert facts["pids"][0] == 1 and len(facts["pids"]) <= 3
    assert int(facts["cap_eff"], 16) == 0
    assert "AMOS_WI067_HOST_SECRET" not in facts["env"]
    assert result.network_enforcement == "NAMESPACE_ENFORCED"
    assert result.execution_fidelity == ExecutionFidelity.REAL.value


@live
def test_legal_search_finds_real_constitutional_text() -> None:
    article = next(p for p in sorted((CORPUS / "articles").rglob("*.md")) if p.name != "README.md")
    heading = next(
        line.lstrip("#").strip()
        for line in article.read_text(encoding="utf-8").splitlines()
        if line.startswith("#")
    )
    word = max(heading.split(), key=len)
    out = execute_legal_search({"query": word, "max_results": 50})
    assert out["succeeded"] is True, out
    assert out["provider"] == "bwrap"
    assert out["execution_fidelity"] == "REAL"
    assert out["isolation"] == "BWRAP_ALL_NAMESPACES_RO_ROOT"
    assert out["files_scanned"] == len(list(CORPUS.rglob("*.md")))
    assert out["total_matches"] >= 1
    hit = out["results"][0]
    source = CORPUS / hit["source"]
    assert source.is_file()
    # المقتطفُ سطرٌ حقيقيٌّ من الملفِّ المُسمّى بالرقمِ المُسمّى — لا نصٌّ مُصطنَع.
    assert (
        source.read_text(encoding="utf-8").splitlines()[hit["line"] - 1].strip()[:300]
        == hit["snippet"]
    )


@live
def test_arabic_matching_ignores_diacritics() -> None:
    plain = execute_legal_search({"query": "الدستور"})
    voweled = execute_legal_search({"query": "الدُّسْتُور"})
    assert plain["total_matches"] == voweled["total_matches"] > 0


@live
def test_a_term_absent_from_the_constitution_finds_nothing() -> None:
    out = execute_legal_search({"query": "zzqx-no-such-term-wi067"})
    assert out["succeeded"] is True and out["total_matches"] == 0 and out["results"] == []


class _AbsentProvider(BubblewrapProvider):
    def availability(self) -> ProviderAvailability:
        return ProviderAvailability(
            provider=self.name, available=False, fidelity="UNAVAILABLE", reason="محاكاةُ الغياب"
        )


def test_without_isolation_it_refuses_and_runs_nothing(tmp_path: Path) -> None:
    """يجري في كلِّ بيئة: لا صندوقَ ⇒ لا تنفيذ، ولا سقوطَ إلى المضيف."""
    marker = tmp_path / "ran"
    out = execute_legal_search(
        {"query": "الدستور"},
        provider=_AbsentProvider({CORPUS_MOUNT: str(tmp_path)}),
    )
    assert out["error"] == "sandbox_unavailable"
    assert out["execution_fidelity"] == "UNAVAILABLE"
    assert out["results"] == []
    assert not marker.exists()


def test_network_policies_other_than_deny_are_refused() -> None:
    from amos_federation.services.tool_registry.providers.contract import (
        ProviderUnavailableError,
    )

    if PROVIDER is None or not _STATE.available:
        provider = _AbsentProvider({})
        with pytest.raises(ProviderUnavailableError):
            provider.create_sandbox(SandboxSpec(tool_id="legal_search", network_policy="ALLOW_ALL"))
        return
    with pytest.raises(ProviderUnavailableError, match="سياسةُ الشبكة"):
        PROVIDER.create_sandbox(SandboxSpec(tool_id="legal_search", network_policy="ALLOW_ALL"))


def test_empty_query_is_rejected_before_any_sandbox() -> None:
    out = execute_legal_search({"query": "  "}, provider=_AbsentProvider({}))
    assert out["error"] == "invalid_params"


@live
def test_the_governed_path_runs_legal_search_in_the_sandbox() -> None:
    """من `execute_tool_with_governance` — بعدَ التخويل — إلى الصندوق، لا إلى `unknown_tool`."""
    from amos_federation.common.principal import AuthorizationContext, Principal
    from amos_federation.services.tool_registry.sandbox import execute_tool_with_governance

    context = AuthorizationContext.from_principal(
        Principal.from_session_record(
            session_id="wi067-session",
            username="wi067-tester",
            role_id="official",
            permissions=("execute:tools",),
            expires_at=None,
        )
    )
    out = execute_tool_with_governance("legal_search", {"query": "الدستور"}, principal=context)
    assert out.get("error") is None, out
    assert out["provider"] == "bwrap" and out["total_matches"] > 0
    assert out["authorization_stages"]


def test_the_registry_declares_what_the_runtime_now_enforces() -> None:
    # قراءةٌ نصّيّةٌ لا `yaml`: حزمةُ الخدماتِ لا تعتمدُ على pyyaml في CI (‏حارسُ W-053).
    import re

    from amos_federation.services.tool_registry.sandbox import ISOLATED_TOOLS

    index = Path(__file__).resolve().parents[4] / "tools" / "registry" / "tool-index.yaml"
    text = index.read_text(encoding="utf-8")
    entry = re.search(r'- id: "legal_search"\n(?:(?!\s*- id:).*\n)*', text)
    assert entry is not None
    assert re.search(r"^\s*sandbox_required:\s*true\s*$", entry.group(0), re.M)
    assert "legal_search" in ISOLATED_TOOLS


def test_isolation_state_is_measured_and_named() -> None:
    """يجري في كلِّ بيئة: الصندوقُ متاحٌ، أو غيابُه مُسمّى السبب — وإن وُعِدَ به فغيابُه فشل."""
    assert _STATE is not None, "مدوَّنةُ الدستورِ غيرُ موجودة"
    if _REQUIRED:
        assert _STATE.available, _STATE
    if not _STATE.available:
        assert _STATE.reason and _STATE.fidelity == "UNAVAILABLE"
    else:
        assert _STATE.fidelity == "REAL"


def test_the_sandbox_argv_carries_every_isolation_flag(tmp_path: Path) -> None:
    """يجري في كلِّ بيئة: الطبقاتُ التي تُغطّيها طبقةٌ أخرى في التشغيلِ تُثبَتُ هنا نصًّا."""
    provider = BubblewrapProvider({CORPUS_MOUNT: str(tmp_path)})
    argv = provider._base_argv(str(tmp_path / "w"))
    for flag in ("--unshare-all", "--die-with-parent", "--new-session", "--clearenv"):
        assert flag in argv, flag
    assert argv[argv.index("--cap-drop") + 1] == "ALL"
    assert ["--ro-bind", str(tmp_path), CORPUS_MOUNT] == argv[-3:]
    assert argv[argv.index("/usr") - 1 : argv.index("/usr") + 2] == ["--ro-bind", "/usr", "/usr"]
    assert "--bind" in argv and argv[argv.index("--bind") + 2] == "/work"
    assert argv.count("--bind") == 1  # مجلّدُ العملِ وحدَه قابلٌ للكتابة
