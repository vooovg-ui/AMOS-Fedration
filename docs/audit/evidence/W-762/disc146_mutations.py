"""طفراتُ إصلاحِ DISC-146 (W-762 · WI-125) — كلُّ طفرةٍ تُطبَّقُ نصًّا ثمَّ تُشغَّلُ الفحوصُ ثمَّ يُستعادُ الملف.

الهدف: إثباتُ أنَّ فحوصَ W-762 تقتلُ ثلاثَ طفراتٍ مُحدَّدةٍ في التصميم § 5، لا أنّها تمرُّ مع أيِّ شِفرة.
النطاق: `core/sovereignty/enforcement.py` وحدَه · يُستعادُ بايتًا بعدَ كلِّ طفرة · لا دفعَ ولا التزام.
المالك: Perplexity Computer (قيدُ W-762 · البندُ WI-125).
التشغيل (من جذرِ المستودع): .venv/bin/python docs/audit/evidence/W-762/disc146_mutations.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TARGET = ROOT / "core/sovereignty/enforcement.py"
TESTS = ["tests/sovereignty/test_disc146_permit_identity.py"]

NEW_ID = 'permit_id=f"EP-{contract.contract_id[3:]}-{uuid.uuid4().hex}",'
MUTATIONS = {
    "M1 إعادةُ المعرّفِ الزمنيّ": [
        (NEW_ID, 'permit_id=f"EP-{contract.contract_id[3:]}-{int(moment.timestamp())}",')
    ],
    "M2 معرّفٌ ثابتٌ لكلِّ عقد": [(NEW_ID, 'permit_id=f"EP-{contract.contract_id[3:]}-fixed",')],
    # M3a: فحصٌ واحدٌ من اثنَين — `consume` يرفضُ الإعادةَ مستقلًّا، فالمتوقَّعُ أن تبقى حيّة
    # (دفاعٌ مزدوج) وتُسجَّلَ كذلك لا أن تُخفى.
    "M3a تعطيلُ is_consumed وحدَه": [("        return permit_id in self._load()", "        return False")],
    "M3b تعطيلُ is_consumed وconsume معًا": [
        ("        return permit_id in self._load()", "        return False"),
        ("        if permit_id in سجل:\n            raise PermitReplayError(", "        if False:\n            raise PermitReplayError("),
    ],
}


def _pytest(args: list[str], cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [str(ROOT / ".venv/bin/python"), "-m", "pytest", "-q", "-p", "no:cacheprovider", *args],
        cwd=cwd, capture_output=True, text=True,
    )
    tail = [ln for ln in proc.stdout.splitlines() if " passed" in ln or " failed" in ln]
    failed = [ln.split("::")[-1].split(" ")[0] for ln in proc.stdout.splitlines() if ln.startswith("FAILED")]
    return proc.returncode, (tail[-1] if tail else "?") + (" · سقط: " + ", ".join(failed) if failed else "")


original = TARGET.read_bytes()
killed = 0
try:
    for name, pairs in MUTATIONS.items():
        src = original.decode("utf-8")
        for old, new in pairs:
            assert src.count(old) == 1, f"{name}: موضعُ الطفرةِ غيرُ فريد"
            src = src.replace(old, new)
        TARGET.write_text(src, encoding="utf-8")
        rc, line = _pytest(["-rf", *TESTS], ROOT)
        extra = ""
        status = "مقتولة" if rc != 0 else "**حيّة**"
        killed += rc != 0
        print(f"{name}: {status} · {line}{extra}")
        TARGET.write_bytes(original)
finally:
    TARGET.write_bytes(original)
print(f"المجموع: {killed}/{len(MUTATIONS)} مقتولة · الملفُّ مُستعادٌ بايتًا: {TARGET.read_bytes() == original}")
sys.exit(0)
