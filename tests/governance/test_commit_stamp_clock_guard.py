"""
فحوصُ حارسِ ساعةِ طوابعِ الالتزامِ — WI-102 · DISC-118 · Q-64

الهدف: إثباتُ أنَّ `tools/governance/commit_stamp_clock_guard.py` يرفضُ ختمًا أحدثَ منَ
       الساعةِ الفعليةِ، وختمَ مؤلفٍ أحدثَ من ختمِ الالتزامِ، وختمًا أقدمَ من أبيه — وأنَّه
       يُجيزُ السلسلةَ الصادقةَ. وفحصٌ حيٌّ يُشغِّلُ الحارسَ على مدى الالتزاماتِ الجديدةِ
       فوقَ main بالساعةِ الفعليةِ (فيُنفَّذُ في CI ضمنَ «بوابة 5 — pytest tests/governance»).
النطاق: الحارسُ وحدَه. المستودعاتُ التركيبيةُ تُبنى في دليلٍ مؤقّتٍ بطوابعَ مضبوطةٍ عمدًا
        (مدخلاتُ اختبارٍ لا قيودٌ).
المالك: tests/governance — بندُ WI-102 (Perplexity Computer · قيدُ W-554)
تاريخ الإنشاء: 2026-10-20
تاريخ آخر تعديل: 2026-10-20 (W-554)
"""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

# الجذرُ بعلامةٍ لا بعُمقٍ ثابتٍ (حرسُ W-102 · test_w102_measurement_root_provenance)
REPO_ROOT = discover_repo_root(__file__)
TOOL = REPO_ROOT / "tools" / "governance" / "commit_stamp_clock_guard.py"
_SPEC = importlib.util.spec_from_file_location("commit_stamp_clock_guard", TOOL)
assert _SPEC is not None and _SPEC.loader is not None
guard = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = guard  # dataclasses تقرأُ الوحدةَ من sys.modules
_SPEC.loader.exec_module(guard)

T0 = datetime(2026, 10, 20, 8, 0, 0, tzinfo=timezone.utc)


def _run(repo: Path, *args: str, env: dict[str, str] | None = None) -> str:
    out = subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, check=True,
        env={**os.environ, **(env or {})},
    )
    return out.stdout.strip()


def _commit(repo: Path, msg: str, committer: datetime, author: datetime | None = None) -> str:
    (repo / "f.txt").write_text(msg, encoding="utf-8")
    _run(repo, "add", "f.txt")
    env = {
        "GIT_AUTHOR_DATE": (author or committer).isoformat(),
        "GIT_COMMITTER_DATE": committer.isoformat(),
        "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t",
    }
    _run(repo, "commit", "-q", "-m", msg, env=env)
    return _run(repo, "rev-parse", "HEAD")


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    _run(tmp_path, "init", "-q", "-b", "main")
    _commit(tmp_path, "base", T0)
    _run(tmp_path, "branch", "base-ref")
    return tmp_path


def _codes(repo: Path, now: datetime, rng: str = "base-ref..HEAD") -> list[str]:
    commits = guard.commits_in_range(repo, rng)
    return [v.code for v in guard.check_commits(commits, repo, now, timedelta(seconds=120))]


def test_honest_chain_passes(repo: Path) -> None:
    _commit(repo, "a", T0 + timedelta(minutes=1))
    _commit(repo, "b", T0 + timedelta(minutes=2))
    assert _codes(repo, T0 + timedelta(minutes=3)) == []


def test_future_committer_stamp_rejected(repo: Path) -> None:
    # نمطُ W-549: الختمُ 08:55 والفحصُ 08:10
    _commit(repo, "w549", T0 + timedelta(minutes=55))
    codes = _codes(repo, T0 + timedelta(minutes=10, seconds=41))
    assert "FUTURE_STAMP" in codes


def test_future_within_tolerance_is_declared_limit(repo: Path) -> None:
    # الحدُّ المُعلَنُ: 103 ثوانٍ (مثلُ W-452) داخلَ هامشِ 120 — يمرُّ ولا يُخفى
    _commit(repo, "w452", T0 + timedelta(seconds=103))
    assert _codes(repo, T0) == []


def test_author_after_committer_rejected(repo: Path) -> None:
    _commit(repo, "a", T0 + timedelta(minutes=1), author=T0 + timedelta(minutes=30))
    codes = _codes(repo, T0 + timedelta(hours=1))
    assert "AUTHOR_AFTER_COMMIT" in codes


def test_stamp_before_parent_rejected(repo: Path) -> None:
    _commit(repo, "a", T0 + timedelta(minutes=10))
    _commit(repo, "b", T0 + timedelta(minutes=5))
    codes = _codes(repo, T0 + timedelta(hours=1))
    assert codes == ["BEFORE_PARENT"]


def test_before_parent_checked_against_base_commit(repo: Path) -> None:
    # الأبُ خارجَ المدى (الأساسُ نفسُه) يُقرأُ ويُقارَنُ
    _commit(repo, "a", T0 - timedelta(minutes=1))
    assert _codes(repo, T0 + timedelta(hours=1)) == ["BEFORE_PARENT"]


def test_equal_to_parent_allowed(repo: Path) -> None:
    _commit(repo, "a", T0)
    assert _codes(repo, T0 + timedelta(minutes=1)) == []


def test_cli_exit_codes(repo: Path) -> None:
    _commit(repo, "a", T0 + timedelta(minutes=55))
    base = ["python", str(TOOL), "--repo-root", str(repo), "--range", "base-ref..HEAD"]
    bad = subprocess.run([*base, "--now", (T0 + timedelta(minutes=10)).isoformat()],
                         capture_output=True, text=True)
    ok = subprocess.run([*base, "--now", (T0 + timedelta(hours=1)).isoformat()],
                        capture_output=True, text=True)
    unreadable = subprocess.run([*base[:-1], "nope..HEAD"], capture_output=True, text=True)
    assert (bad.returncode, ok.returncode, unreadable.returncode) == (1, 0, 2)
    assert "FUTURE_STAMP" in bad.stdout


def _has(rev: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{rev}^{{commit}}"], cwd=REPO_ROOT,
                          capture_output=True).returncode == 0


@pytest.mark.skipif(not (_has("122b00f") and _has("7a44582")),
                    reason="السجلُّ ضحلٌ — عقدُ W-546/W-549 غيرُ مرئيةٍ (تُعلَنُ ولا تُطوى)")
def test_real_history_w549_caught_at_its_run_start() -> None:
    """نمطُ DISC-118 مقيسًا على التاريخِ الحقيقيِّ: W-549 عندَ بدءِ سيرِ دفعِها 08:10:41Z."""
    commits = guard.commits_in_range(REPO_ROOT, "122b00f..7a44582")
    now = datetime(2026, 10, 20, 8, 10, 41, tzinfo=timezone.utc)
    found = guard.check_commits(commits, REPO_ROOT, now, timedelta(seconds=120))
    assert {v.sha[:7] for v in found if v.code == "FUTURE_STAMP"} == {"7a44582"}


def test_live_new_commits_stamped_by_real_clock() -> None:
    """الفحصُ الحيُّ: كلُّ التزامٍ جديدٍ فوقَ main مختومٌ منَ الساعةِ الفعليةِ (Q-64)."""
    if guard.default_base(REPO_ROOT) is None:
        pytest.skip("لا origin/main ولا main — لا مدى يُقاسُ (يُعلَنُ)")
    ranges, _foreign, _label = guard.resolve_range(REPO_ROOT, None)
    commits: dict[str, object] = {}
    for r in ranges:
        for c in guard.commits_in_range(REPO_ROOT, r):
            commits.setdefault(c.sha, c)
    found = guard.check_commits(list(commits.values()), REPO_ROOT,  # type: ignore[arg-type]
                                datetime.now(timezone.utc), timedelta(seconds=120))
    assert found == [], "\n".join(f"{v.code} {v.sha[:7]} {v.detail}" for v in found)
