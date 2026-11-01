"""مسبارُ DISC-150 — هل يرفضُ حرسُ ما قبلَ الدفعِ المحليُّ العقدَ التي احمرَّت في CI؟ (التوجيهُ 37 § 2 · W-768)

الهدف: يُشغِّلُ `tools/dev/prepush_gate.py` **من الشجرةِ المقيسةِ نفسِها** على ثلاثِ عقدٍ تاريخيّةٍ بحكمٍ
       مقروءٍ في CI: `b78bba09` (#234 · أحمر: قيدٌ مفتوحٌ بلا مِرساة) · `6a850f20` (#235 · أحمر: مصفوفةٌ
       متقادمة) · `8ba08561` (#236 · أخضر · ضابط). ويطبعُ حكمَ البوّابةِ المحلّيّةِ وحكمَ CI جنبًا إلى جنب.
النطاق: قراءةٌ فقط · worktree مؤقّتٌ لكلِّ عقدة · لا شبكة · لا دفع.
المالك: Perplexity Computer (قيدُ W-768 · البندُ WI-077).
التشغيل (من جذرِ المستودع): python3 docs/audit/evidence/W-768/prepush_parity_probe.py [--gate-from HEAD]
    بلا `--gate-from`: البوّابةُ من العقدةِ المقيسةِ نفسِها (قبلَ الإصلاح).
    بـ`--gate-from <ref>`: تُنسَخُ أدواتُ `tools/dev` و`tools/governance` من <ref> إلى الشجرةِ المقيسةِ قبلَ التشغيل (بعدَ الإصلاح).
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

NODES = (
    (
        "b78bba09",
        "614b5233",
        "#234",
        "أحمر — Work Governance: OPEN_RECORD_WITHOUT_ANCHOR DISC-149",
    ),
    (
        "6a850f20",
        "614b5233",
        "#235",
        "أحمر — Truth Audit · Identity Law · Cross-System: TRUTH_MATRIX متقادم",
    ),
    ("8ba08561", "614b5233", "#236", "أخضر 13/13 (ضابط)"),
)


SHIM = """import datetime as _dt
_T = _dt.date.fromisoformat("{today}")


class _PinnedDate(_dt.date):
    @classmethod
    def today(cls):
        return cls(_T.year, _T.month, _T.day)


class _PinnedDateTime(_dt.datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(_T.year, _T.month, _T.day, 12, 0, 0, tzinfo=tz)

    @classmethod
    def utcnow(cls):
        return cls(_T.year, _T.month, _T.day, 12, 0, 0)


_dt.date = _PinnedDate
_dt.datetime = _PinnedDateTime
"""


def _run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd, cwd=str(cwd), capture_output=True, text=True, check=False
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate-from", default="")
    ap.add_argument(
        "--pin-today",
        default="",
        help="YYYY-MM-DD: يُثبَّتُ «اليوم» لكلِّ عملياتِ البوّابةِ عبرَ sitecustomize مؤقّتٍ (أداةُ قياسٍ لا تعديلُ بوّابة)",
    )
    a = ap.parse_args()
    root = Path(
        _run(["git", "rev-parse", "--show-toplevel"], Path.cwd()).stdout.strip()
    )
    py = str(root / ".venv" / "bin" / "python")
    print(
        f"البوّابة: {'من ' + a.gate_from if a.gate_from else 'من العقدةِ المقيسةِ نفسِها'}"
    )
    env = dict(os.environ)
    shim_dir = None
    if a.pin_today:
        shim_dir = Path(tempfile.mkdtemp(prefix="p150_shim_"))
        (shim_dir / "sitecustomize.py").write_text(
            SHIM.format(today=a.pin_today), encoding="utf-8"
        )
        env["PYTHONPATH"] = str(shim_dir) + os.pathsep + env.get("PYTHONPATH", "")
        print(
            f"اليومُ مُثبَّتٌ: {a.pin_today} (يومُ تشغيلِ CI على العقد) — لعزلِ DISC-150 عن انقضاءِ الحجوزِ بمرورِ الساعة"
        )
    else:
        print("اليومُ: ساعةُ الآلةِ الفعليّة (غيرُ مُثبَّت)")
    gate_wt = None
    if a.gate_from:
        # البوّابةُ من شجرةٍ نظيفةٍ للمرجعِ خارجَ العقدةِ المقيسة، فلا تُمَسُّ العقدة
        # (W-769: نسخُ الأدواتِ داخلَها كانَ يُغيِّرُ مصفوفتَها فيُسقِطُ الخطوة 9 زورًا).
        gate_wt = Path(tempfile.mkdtemp(prefix="p150_gate_")) / "wt"
        _run(
            ["git", "worktree", "add", "-q", "--detach", str(gate_wt), a.gate_from],
            root,
        )
    for sha, base, pr, ci in NODES:
        tmp = Path(tempfile.mkdtemp(prefix=f"p150_{sha}_"))
        wt = tmp / "wt"
        _run(["git", "worktree", "add", "-q", "--detach", str(wt), sha], root)
        try:
            (wt / ".venv").symlink_to(root / ".venv")
            if gate_wt is not None:
                gate = [
                    py,
                    str(gate_wt / "tools/dev/prepush_gate.py"),
                    "--repo-root",
                    str(wt),
                ]
            else:
                gate = [py, "tools/dev/prepush_gate.py"]
            help_text = _run([*gate[:2], "--help"], wt).stdout
            if "--base" in help_text:
                gate += ["--base", base]
            r = subprocess.run(
                gate, cwd=str(wt), capture_output=True, text=True, check=False, env=env
            )
            failed = [
                m.group(1).strip()
                for m in re.finditer(r"\[PREPUSH\] ✗ فشلَ: (.+)", r.stdout)
            ]
            verdict = "يُرفَضُ (EXIT≠0)" if r.returncode else "يُقبَلُ (EXIT=0)"
            print(f"{pr} {sha} · CI: {ci} · المحلّيّ: {verdict} EXIT={r.returncode}")
            for name in failed:
                print(f"    ✗ {name}")
        finally:
            _run(["git", "worktree", "remove", "--force", str(wt)], root)
            shutil.rmtree(tmp, ignore_errors=True)
    if gate_wt is not None:
        _run(["git", "worktree", "remove", "--force", str(gate_wt)], root)
        shutil.rmtree(gate_wt.parent, ignore_errors=True)
    if shim_dir is not None:
        shutil.rmtree(shim_dir, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
