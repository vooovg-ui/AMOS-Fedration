#!/usr/bin/env python3
"""
حرسُ صيغِ origin في وجهِ الدمجِ `--merge` — مطابقةٌ تامّةٌ لاسمِ المستودعِ (WI-083)

الهدف: إثباتُ أنَّ وجهَ الدمجِ يقبلُ عنوانَ الوسيطِ في بيئاتِ العمّالِ ولا يُرخي الحرسَ:
       الصيغُ ثلاثٌ لا رابعَ لها، وowner/repo يُطابِقُ `vooovg-ui/AMOS-Fedration` مطابقةً
       تامّةً، وكلُّ مستودعٍ مخادعٍ يُرفَضُ بالرمزِ 2 من `_merge_flow` قبلَ أيِّ حكمٍ أو
       دفعٍ — ويُقتَلُ بالتحويرِ: كلُّ شرطٍ يُحذَفُ أو يُرخى يُسقِطُ فحصًا.
النطاق: منطقُ الاستخراجِ والمطابقةِ وحدَه — لا شبكةَ ولا `gh` ولا دفعَ: `_merge_flow`
        يُشغَّلُ على مستودعٍ مؤقّتٍ HEAD فيه هو العقدةُ المطلوبةُ وorigin مصنوع.
المالك: tests/governance — WI-083 (توجيهُ المستشارِ 9 § 2)
تاريخ الإنشاء: 2026-10-16 (W-387 · WI-083)
تاريخ آخر تعديل: 2026-10-16 (W-387 · المرّةُ الأولى)
"""

from __future__ import annotations

import importlib.util
import os
import subprocess
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[2]
_GATE_PATH = _REPO_ROOT / "tools" / "dev" / "prepush_gate.py"
_README_PATH = _REPO_ROOT / "tools" / "dev" / "README.md"

_SPEC = importlib.util.spec_from_file_location("amos_prepush_gate_wi083", _GATE_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"prepush_gate.py not loadable from {_GATE_PATH}")
gate = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(gate)

CANON = "vooovg-ui/AMOS-Fedration"
ACCEPTED = (
    "https://github.com/vooovg-ui/AMOS-Fedration.git",
    "https://github.com/vooovg-ui/AMOS-Fedration",
    "git@github.com:vooovg-ui/AMOS-Fedration.git",
    "https://git-agent-proxy.perplexity.ai/vooovg-ui/AMOS-Fedration.git",
    "https://git-agent-proxy.perplexity.ai/vooovg-ui/AMOS-Fedration",
)
DECEPTIVE = (
    "https://github.com/evil/AMOS-Fedration.git",
    "https://git-agent-proxy.perplexity.ai/evil/AMOS-Fedration.git",
    "https://github.com/vooovg-ui/AMOS-Fedration-fork.git",
    "https://git-agent-proxy.perplexity.ai/vooovg-ui/AMOS-Fedration-fork",
    "https://github.com/vooovg-ui/amos-fedration.git",
    "https://git-agent-proxy.perplexity.ai/",
    "https://git-agent-proxy.perplexity.ai/vooovg-ui",
    "https://git-agent-proxy.perplexity.ai.evil.com/vooovg-ui/AMOS-Fedration.git",
    "https://github.com.evil/vooovg-ui/AMOS-Fedration.git",
    "https://git-agent-proxy.perplexity.aivooovg-ui/AMOS-Fedration",
    "https://github.comvooovg-ui/AMOS-Fedration",
    "https://gitlab.com/vooovg-ui/AMOS-Fedration.git",
)


def test_constants_are_exactly_declared() -> None:
    assert gate.CANONICAL_SLUG == CANON
    assert gate.ACCEPTED_ORIGIN_PREFIXES == (
        "https://github.com/",
        "git@github.com:",
        "https://git-agent-proxy.perplexity.ai/",
    ), "الصيغُ المقبولةُ ثلاثٌ لا رابعَ لها"


@pytest.mark.parametrize("url", ACCEPTED)
def test_canonical_slug_accepts_direct_and_proxy(url: str) -> None:
    assert gate._canonical_slug(url) == CANON


@pytest.mark.parametrize("url", DECEPTIVE)
def test_canonical_slug_rejects_deceptive(url: str) -> None:
    with pytest.raises(ValueError, match="يُرفَضُ"):
        gate._canonical_slug(url)


def _repo_at_head(tmp_path: Path, origin: str) -> tuple[Path, str]:
    repo = tmp_path / "r"
    repo.mkdir()
    env = {**os.environ, "TZ": "UTC"}
    for cmd in (
        ["git", "init", "-q", "-b", "main", "."],
        ["git", "config", "user.email", "wi083@amos.local"],
        ["git", "config", "user.name", "WI-083 Guard"],
        ["git", "remote", "add", "origin", origin],
    ):
        subprocess.run(cmd, cwd=repo, check=True, env=env)
    (repo / "README.md").write_text("x", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=repo, check=True, env=env)
    subprocess.run(
        ["git", "commit", "-q", "-m", "init", "--date=2026-10-16T00:00:00+00:00"],
        cwd=repo,
        check=True,
        env=env,
    )
    sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return repo, sha


@pytest.mark.parametrize("url", DECEPTIVE)
def test_merge_flow_refuses_deceptive_origin_with_code_2(
    tmp_path: Path, url: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """HEAD يطابقُ العقدةَ وorigin مخادعٌ ⇒ الرمزُ 2 قبلَ أيِّ نداءٍ لـgh أو دفع."""
    repo, sha = _repo_at_head(tmp_path, url)
    monkeypatch.setattr(gate, "_origin_url", lambda _root: url)

    def _no_network(*_a, **_k):  # pragma: no cover — بلوغُه عطب
        raise AssertionError("بلغَ الوجهُ الشبكةَ مع مستودعٍ مخادعٍ")

    monkeypatch.setattr(gate, "_fetch_jobs_payload", _no_network)
    assert gate._merge_flow(sha, repo, []) == 2


# ── قتلُ الفحصِ بالتحويرِ: كلُّ شرطٍ يُرخى يُسقِطُ فحصًا ─────────────────────


def _mutant(old: str, new: str):
    source = _GATE_PATH.read_text(encoding="utf-8")
    assert source.count(old) == 1, f"موضعُ التحويرِ غيرُ فريدٍ: {old!r}"
    spec = importlib.util.spec_from_loader("amos_prepush_gate_mutant", loader=None)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    module.__dict__["__file__"] = str(_GATE_PATH)
    exec(compile(source.replace(old, new), str(_GATE_PATH), "exec"), module.__dict__)  # noqa: S102
    return module


def _refusal(func, url: str) -> str | None:
    """نصُّ الرفضِ إن رُفِضَ العنوانُ، و`None` إن قُبِل — فالاستثناءُ يُنقَلُ لا يُبتلَع."""
    try:
        func(url)
    except ValueError as exc:
        return str(exc) or "رفضٌ بلا نصّ"
    return None


def _rejects_all(module) -> bool:
    return all(_refusal(module._canonical_slug, url) for url in DECEPTIVE)


def _accepts_all(module) -> bool:
    return all(
        _refusal(module._canonical_slug, url) is None for url in ACCEPTED
    ) and all(module._canonical_slug(url) == CANON for url in ACCEPTED)


def test_live_source_passes_both_probes() -> None:
    assert _rejects_all(gate) and _accepts_all(gate)


def test_mutation_drop_exact_match_is_caught() -> None:
    m = _mutant("    if slug != CANONICAL_SLUG:\n", "    if False:\n")
    assert not _rejects_all(m), "حذفُ المطابقةِ التامّةِ لا يُكتشَف"


def test_mutation_startswith_instead_of_equality_is_caught() -> None:
    m = _mutant(
        "    if slug != CANONICAL_SLUG:\n",
        "    if not slug.startswith(CANONICAL_SLUG):\n",
    )
    assert not _rejects_all(m), "startswith بدلَ المساواةِ يُجيزُ …-fork ولا يُكتشَف"


def test_mutation_case_folding_is_caught() -> None:
    m = _mutant(
        "    if slug != CANONICAL_SLUG:\n",
        "    if slug.lower() != CANONICAL_SLUG.lower():\n",
    )
    assert not _rejects_all(m), "تطبيعُ حالةِ الأحرفِ لا يُكتشَف"


def test_mutation_drop_proxy_prefix_is_caught() -> None:
    m = _mutant('    "https://git-agent-proxy.perplexity.ai/",\n', "")
    assert not _accepts_all(m), "حذفُ صيغةِ الوسيطِ لا يُكتشَف — والعطبُ هو عينُ W-381"


def test_mutation_prefix_without_trailing_slash_is_caught() -> None:
    m = _mutant(
        '    "https://git-agent-proxy.perplexity.ai/",\n',
        '    "https://git-agent-proxy.perplexity.ai",\n',
    )
    assert not _rejects_all(m), "بادئةٌ بلا `/` تُجيزُ مضيفًا مخادعًا ولا يُكتشَف"


def _parser_rejects_nameless(module) -> bool:
    for url in (
        "https://git-agent-proxy.perplexity.ai/",
        "https://git-agent-proxy.perplexity.ai/vooovg-ui",
    ):
        if _refusal(module._slug_from_url, url) is None:
            return False
    return True


def test_live_parser_rejects_nameless() -> None:
    assert _parser_rejects_nameless(gate)


def test_mutation_accept_empty_path_is_caught() -> None:
    """عنوانٌ بلا اسمٍ يُرفَضُ في المُحلِّلِ نفسِه لا بالمطابقةِ وحدَها (دفاعٌ بطبقتين)."""
    m = _mutant('    if path.count("/") != 1 or not path:\n', "    if False:\n")
    assert not _parser_rejects_nameless(m), "قبولُ مسارٍ بلا اسمٍ لا يُكتشَف"


def test_merge_flow_uses_canonical_check() -> None:
    source = _GATE_PATH.read_text(encoding="utf-8")
    assert "slug = _canonical_slug(_origin_url(repo_root))" in source
    assert "slug = _slug_from_url(_origin_url(repo_root))" not in source


def test_readme_documents_accepted_forms() -> None:
    text = _README_PATH.read_text(encoding="utf-8")
    for prefix in gate.ACCEPTED_ORIGIN_PREFIXES:
        assert prefix in text, f"الصيغةُ {prefix} غيرُ موثَّقةٍ في tools/dev/README.md"
    assert CANON in text
