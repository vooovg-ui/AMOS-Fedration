"""حرسُ W-312 — سجلُّ ذرّيّةِ الاختباراتِ لكلِّ جلسةٍ لا مشتركٌ بينَ الجلسات

الهدف: إسقاطُ أيِّ رجوعٍ إلى مسارٍ ثابتٍ مشتركٍ لسجلِّ الذرّيّةِ في الاختبارات
النطاق: federal/executive/services/tests/conftest.py (‏`WI-072` · `DISC-093`)
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-13 (W-312)

سببُ وجودِه (‏`W-308`): سجلُّ الذرّيّةِ في الاختباراتِ كانَ ملفًّا بمسارٍ ثابتٍ في
مجلَّدِ الخدمات، تمحوه كلُّ جلسةٍ عندَ بدئها وانتهائها وتكتبُه كاملًا. فجلستانِ
متزامنتانِ تفقدُ إحداهما حجزَ الأخرى ⇒ ``IdempotencyError: … غيرُ محجوز``. قِيسَ:
مشتركٌ متوازٍ ⇒ 31 إخفاقًا · منفصلٌ ⇒ 0 · تسلسليٌّ ⇒ 0
(``docs/audit/evidence/W-308/``).

ما يُثبِتُه هذا الملفّ:
1. الجلسةُ الجاريةُ تكتبُ سجلَّها داخلَ مجلَّدِ أثرِها (‏``TEST_ARTIFACT_DIR`` الفريد).
2. التنظيفُ يمسُّ مجلَّدَه وحدَه ولا يمسُّ سجلَّ جلسةٍ أخرى.
3. سباقُ جلستَينِ حقيقيّتَينِ متزامنتَينِ لا يُنتِجُ ``IdempotencyError``.
"""

from __future__ import annotations

import os
import subprocess
import sys
import textwrap
import time
from pathlib import Path

from tests.conftest import (
    TEST_ARTIFACT_DIR,
    TEST_CONSUMED_PERMITS_FILE,
    TEST_IDEMPOTENCY_LEDGER_FILE,
    _cleanup_test_ledger,
)

SERVICES_DIR = Path(__file__).resolve().parent.parent


def test_session_ledger_lives_inside_this_sessions_artifact_dir() -> None:
    """المسارُ المُعلَنُ للجلسةِ داخلَ مجلَّدِها الفريد — لا في مجلَّدِ الخدمات."""
    chosen = Path(os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"]).resolve()
    assert chosen.parent == TEST_ARTIFACT_DIR.resolve(), (
        f"سجلُّ الذرّيّةِ في {chosen} — خارجَ مجلَّدِ أثرِ الجلسة {TEST_ARTIFACT_DIR}: "
        "مسارٌ مشتركٌ بينَ الجلساتِ يُعيدُ سباقَ DISC-093"
    )
    assert chosen.parent != SERVICES_DIR.resolve()
    assert chosen.name == TEST_IDEMPOTENCY_LEDGER_FILE


def test_cleanup_touches_only_its_own_artifact_dir(tmp_path: Path) -> None:
    """تنظيفُ جلسةٍ لا يمحو سجلَّ جلسةٍ أخرى — عينُ ما كانَ يُسقِطُ الحجز."""
    mine = tmp_path / "session-a"
    other = tmp_path / "session-b"
    for folder in (mine, other):
        folder.mkdir()
        (folder / TEST_IDEMPOTENCY_LEDGER_FILE).write_text("{}", encoding="utf-8")
        (folder / TEST_CONSUMED_PERMITS_FILE).write_text("[]", encoding="utf-8")

    returned = _cleanup_test_ledger(mine)

    assert returned == mine / TEST_IDEMPOTENCY_LEDGER_FILE
    assert not (mine / TEST_IDEMPOTENCY_LEDGER_FILE).exists()
    assert not (mine / TEST_CONSUMED_PERMITS_FILE).exists()
    # الجلسةُ الأخرى سليمة.
    assert (other / TEST_IDEMPOTENCY_LEDGER_FILE).read_text(encoding="utf-8") == "{}"
    assert (other / TEST_CONSUMED_PERMITS_FILE).read_text(encoding="utf-8") == "[]"


_RACE_TEST = textwrap.dedent(
    '''
    """اختبارٌ مؤقّتٌ تكتبُه حالةُ السباقِ في W-312 ثمّ تمحوه."""
    import os
    import time
    from pathlib import Path


    def test_ledger_survives_a_concurrent_session():
        ledger = Path(os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"])
        ledger.write_text("mine", encoding="utf-8")
        # الجلسةُ الأخرى تبدأُ وتنتهي في هذه النافذة — فتمحو المشتركَ إن كانَ مشتركًا.
        time.sleep(4)
        assert ledger.exists() and ledger.read_text(encoding="utf-8") == "mine"
    '''
)


def test_two_concurrent_sessions_do_not_erase_each_others_ledger() -> None:
    """جلستانِ حقيقيّتانِ متزامنتانِ (عمليّتانِ) لا تمحو إحداهما سجلَّ الأخرى.

    مع المسارِ الثابتِ القديمِ تمحو بدايةُ الجلسةِ الثانيةِ ونهايتُها ملفَّ الأولى
    فيسقطُ هذا الاختبار — وهو تحوّرُ «إعادةِ المسارِ القديم» الذي يقتلُه.
    """
    probe = SERVICES_DIR / "tests" / "test_zz_wi072_race_probe_tmp.py"
    probe.write_text(_RACE_TEST, encoding="utf-8")
    try:
        cmd = [
            sys.executable,
            "-m",
            "pytest",
            "-q",
            "-p",
            "no:cacheprovider",
            "tests/test_zz_wi072_race_probe_tmp.py",
        ]
        env = {k: v for k, v in os.environ.items() if k != "AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"}
        first = subprocess.Popen(
            cmd, cwd=SERVICES_DIR, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        # الثانيةُ تبدأُ والأولى في نافذةِ نومِها.
        time.sleep(1.5)
        second = subprocess.run(
            cmd, cwd=SERVICES_DIR, env=env, capture_output=True, text=True, timeout=180
        )
        out_first, _ = first.communicate(timeout=180)
    finally:
        probe.unlink(missing_ok=True)

    text_first = out_first.decode("utf-8", errors="replace")
    assert second.returncode == 0, second.stdout[-2000:]
    assert first.returncode == 0, (
        "الجلسةُ الأولى فقدَت سجلَّها أثناءَ جلسةٍ متزامنة — السجلُّ مشتركٌ (DISC-093):\n"
        + text_first[-2000:]
    )
