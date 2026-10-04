"""حرسُ `WI-056` — بيئةُ `bootstrap.sh` تحملُ ruff الذي يحكمُ به CI لا أحدثَ إصدار.

الهدف:
    كانَ `pyproject.toml` يُعلِنُ `ruff>=0.6.9` حدًّا أدنى وCI يُركِّبُ إصدارًا مُثبَّتًا،
    فحملَت بيئةُ `bootstrap.sh` ruff 0.16.10 ورأت `ruff check .` أحمرَ بـ505 تشخيصًا
    لا يراها CI (‏`DISC-073`) — وأسقطَ ذلك حكمَ مراجعٍ في الجولةِ الثامنةِ (`DISC-074` (أ)).
    فالإصدارُ يُقرأُ من `.github/workflows/ci.yml` في موضعٍ واحدٍ ولا يُكتَبُ في السكربت.

النطاق:
    `tools/dev/bootstrap.sh` (‏`ruff_ci_pin` · `--print-ruff-pin` · الخطوة 5ب) — قراءةً
    وتشغيلًا للاستخراجِ وحدَه، لا تركيبًا لبيئة.

المالك: governance/
تاريخ الإنشاء: 2026-10-04
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOTSTRAP = REPO_ROOT / "tools" / "dev" / "bootstrap.sh"
CI_WORKFLOW = REPO_ROOT / ".github" / "workflows" / "ci.yml"

#: صيغةُ التثبيتِ في CI كما يقرؤها السكربت — سطرُ `- run: pip install ruff==X`.
PIN_RE = re.compile(r"^\s*-\s*run:\s*pip install ruff==([0-9][0-9A-Za-z.]*)\s*$", re.MULTILINE)

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="bash غيرُ متاح")


def _ci_pins(text: str) -> set[str]:
    return set(PIN_RE.findall(text))


def _print_pin(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["bash", str(root / "tools" / "dev" / "bootstrap.sh"), "--print-ruff-pin"],
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )


def _fake_root(tmp_path: Path, ci_text: str) -> Path:
    """شجرةٌ دنيا تجتازُ فحصَ الجذرِ في السكربت — والمتغيِّرُ فيها `ci.yml` وحدَه."""
    (tmp_path / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
    (tmp_path / "core" / "constitution").mkdir(parents=True)
    (tmp_path / "requirements-dev.txt").write_text("", encoding="utf-8")
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    (tmp_path / ".github" / "workflows" / "ci.yml").write_text(ci_text, encoding="utf-8")
    (tmp_path / "tools" / "dev").mkdir(parents=True)
    shutil.copy2(BOOTSTRAP, tmp_path / "tools" / "dev" / "bootstrap.sh")
    return tmp_path


def test_ci_pins_ruff_exactly_once() -> None:
    """CI يُثبِّتُ ruff بإصدارٍ واحدٍ — وإلّا فلا «إصدارُ CI» يُقرأ."""
    pins = _ci_pins(CI_WORKFLOW.read_text(encoding="utf-8"))
    assert len(pins) == 1, f"تثبيتاتُ ruff في ci.yml: {sorted(pins)}"


def test_bootstrap_reads_the_pin_and_does_not_hardcode_it() -> None:
    """لا رقمَ إصدارٍ لـruff مكتوبًا في السكربت — المصدرُ واحدٌ هو ci.yml."""
    text = BOOTSTRAP.read_text(encoding="utf-8")
    assert not re.search(r"ruff==[0-9]", text), "إصدارُ ruff مكتوبٌ رقمًا في bootstrap.sh"
    assert ".github/workflows/ci.yml" in text
    assert 'pip install --quiet "ruff==$RUFF_PIN"' in text, "السكربتُ لا يُركِّبُ المُثبَّتَ المقروء"


def test_bootstrap_installs_the_pin_after_the_services_package() -> None:
    """التركيبُ بعدَ `[dev]` — وإلّا أعادَ `ruff>=0.6.9` في `[dev]` أحدثَ إصدارٍ فوقَه."""
    text = BOOTSTRAP.read_text(encoding="utf-8")
    services = text.index('pip install --quiet -e "federal/executive/services[dev]"')
    pinned = text.index('pip install --quiet "ruff==$RUFF_PIN"')
    assert pinned > services


def test_print_ruff_pin_equals_the_ci_pin() -> None:
    """ما يستخرجُه السكربتُ من الشجرةِ الحقيقيّةِ يساوي ما يُركِّبُه CI."""
    (expected,) = _ci_pins(CI_WORKFLOW.read_text(encoding="utf-8"))
    proc = _print_pin(REPO_ROOT)
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == expected


def test_print_ruff_pin_follows_a_changed_pin(tmp_path: Path) -> None:
    """تغييرُ التثبيتِ في ci.yml يتبعُه السكربتُ بلا مسّ — فلا نسختانِ تفترقان."""
    root = _fake_root(tmp_path, "jobs:\n  lint:\n    steps:\n      - run: pip install ruff==9.8.7\n")
    proc = _print_pin(root)
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == "9.8.7"


@pytest.mark.parametrize(
    "ci_text",
    [
        "jobs:\n  lint:\n    steps:\n      - run: pip install ruff\n",
        "jobs:\n  a:\n    steps:\n      - run: pip install ruff==0.6.9\n"
        "  b:\n    steps:\n      - run: pip install ruff==0.7.0\n",
    ],
    ids=["no-pin", "two-different-pins"],
)
def test_missing_or_conflicting_pin_fails_closed(tmp_path: Path, ci_text: str) -> None:
    """غيابُ التثبيتِ أو تعدُّدُه خطأٌ مُعلَنٌ لا تخمينٌ لإصدار."""
    proc = _print_pin(_fake_root(tmp_path, ci_text))
    assert proc.returncode != 0
    assert proc.stdout.strip() == ""
