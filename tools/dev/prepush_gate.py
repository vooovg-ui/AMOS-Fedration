"""مُشغّلُ حرسِ ما قبلَ الدفعِ — أمرٌ واحدٌ يُشغّلُ البواباتِ كلَّها ويمنعُ الدفعَ عندَ أيِّ فشلٍ.

طريقُ الإنفاذ: PENDING_GATE_ITEM · مؤجَّلٌ ببندِ WI-077 — ربطُه خطوةَ CI أو فحصًا يشملُهُ ينتظرُ إغلاقَ البندِ وقرارَ المالكِ في مسلكِ الدمجِ (`Q-F`)؛ ودليلُ تشغيلِهِ المباشرِ قيَّدهُ W-348 · ورُبِطَ بمسارِ الدفعِ خُطّافَ `pre-push` محليًّا (دليلُ W-349).

التعريف:
    مُشغّلُ البواباتِ المحليةِ قبلَ أيِّ دفعٍ إلى `main`: يُشغّلُ الحرسَ القائمَ كلَّهُ
    بأمرٍ واحدٍ ويخرجُ برمزٍ غيرِ صفريٍّ إن فشلَتْ أيُّ بوابةٍ — فلا يُدفَعُ إلا
    بعدَ خُضرتِه. **لا يُخفَّفُ أيُّ حرسٍ ولا يُضيفُ حكمًا جديدًا** — تنسيقٌ لا
    استبدال.

النطاق:
    بندُ WI-077 (توجيهُ المستشارِ 5 · G3 · DISC-098): الحرسُ السبعةُ المُلزِمةُ
    قبلَ الدفعِ — عقدتا 70441f8 و597d8bb بلغتا `main` حمراوَينِ لأنّ هذه
    البواباتِ لم تكنْ تُشغَّلُ معًا محليًّا قبلَ الدفعِ.

المالك:
    Perplexity Computer (WI-077 · بإذنِ المالكِ العامِّ وتوجيهِ المستشارِ 5).

تاريخ الإنشاء: 2026-10-16 (WI-077 · W-348)
تاريخ آخر تعديل: 2026-10-15 (WI-077 · المرّةُ الأولى)

المحتويات (الحرسُ السبعةُ — بترتيبٍ ثابتٍ):
    1. `check_work_governance.py --commit HEAD` — كلُّ عملٍ مُسجَّلٌ ومملوكٌ
       ومساراتُهُ مُعلنةٌ (عيبُ 70441f8: `PATH_UNCLAIMED`).
    2. `check_work_governance.py --self-check --today <اليوم+4>` — الخارطةُ
       سليمةٌ والحجوزُ لا تنقضي خلالَ أربعةِ أيامٍ.
    3. `commit_timestamp_integrity.py --check` — طوابعُ الالتزامِ UTC صادقة.
    4. `check_completion_ledger.py --commit HEAD` — التوثيقُ مقيَّدٌ معَ العمل.
    5. `truth_audit.py <الجذر> --ratchet` — مصفوفةُ الحقيقةِ لا تنحدر.
    6. `state_document_drift.py` — وثائقُ الحالةِ تذكرُ أحدثَ قيدٍ.
    7. فحوصُ الهويةِ واتساقِ المراجعِ: `pytest` على
       `tests/governance/test_w154_reviewer_consistency.py` وفحوصِ قانونِ
       الهويةِ (عيبُ 597d8bb: `REVIEWER_ROW_BLOCK_MISMATCH`).

الاستعمال:
    .venv/bin/python tools/dev/prepush_gate.py            # على الشجرةِ الحاضرةِ
    .venv/bin/python tools/dev/prepush_gate.py --repo-root /مسار   # لقياسِ شجرةٍ أخرى

الخرجُ: رمزُ خروجٍ **0** فقط إن نجحَ الحرسُ كلُّهُ — وأيُّ فشلٍ يمنعُ الدفعَ.
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

#: الجذرُ يُعرَفُ بعلامةٍ لا بعُمقٍ (نمطُ `repo_root.py` · سابقةُ W-336) —
#: فلا يُحتسَبُ هذا الاشتقاقُ في دَينِ الجذرِ الثابتِ، ولا يُقاسُ على شجرةٍ غيرِ مقصودةٍ.
_ROOT_FINDER_PATH = Path(__file__).resolve().with_name("..").resolve() / "governance" / "repo_root.py"
_ROOT_FINDER_SPEC = importlib.util.spec_from_file_location(
    "amos_repo_root_finder", _ROOT_FINDER_PATH
)
if _ROOT_FINDER_SPEC is None or _ROOT_FINDER_SPEC.loader is None:
    raise ImportError(f"repo_root.py not loadable from {_ROOT_FINDER_PATH}")
_ROOT_FINDER = importlib.util.module_from_spec(_ROOT_FINDER_SPEC)
_ROOT_FINDER_SPEC.loader.exec_module(_ROOT_FINDER)

REPO_ROOT = _ROOT_FINDER.discover_repo_root(__file__)
PY = sys.executable
GOVERNANCE = REPO_ROOT / "tools" / "governance"

#: الحرسُ السبعةُ: (الاسمُ، الأمرُ) — الأمرُ يُبنى بدالّةٍ لأنّ بعضَهُ يحتاجُ الجذرَ.
def _gates(repo_root: Path, today_plus_4: str) -> list[tuple[str, list[str], Path | None]]:
    return [
        (
            "1· حوكمةُ العملِ (--commit HEAD)",
            [
                str(GOVERNANCE / "check_work_governance.py"),
                "--commit",
                "HEAD",
                "--repo-root",
                str(repo_root),
            ],
            repo_root,
        ),
        (
            "2· حوكمةُ العملِ (--self-check --today +4)",
            [
                str(GOVERNANCE / "check_work_governance.py"),
                "--self-check",
                "--today",
                today_plus_4,
                "--repo-root",
                str(repo_root),
            ],
            repo_root,
        ),
        (
            "3· صدقُ طوابعِ الالتزامِ (UTC)",
            [str(GOVERNANCE / "commit_timestamp_integrity.py"), "--check"],
            repo_root,
        ),
        (
            "4· سجلُّ الإكمالِ (--commit HEAD)",
            [str(GOVERNANCE / "check_completion_ledger.py"), "--commit", "HEAD"],
            repo_root,
        ),
        (
            "5· راتشيتُ مصفوفةِ الحقيقةِ",
            [str(GOVERNANCE / "truth_audit.py"), str(repo_root), "--ratchet"],
            repo_root,
        ),
        (
            "6· انحرافُ وثائقِ الحالةِ",
            [str(GOVERNANCE / "state_document_drift.py"), "--root", str(repo_root)],
            repo_root,
        ),
        (
            "7· فحوصُ الهويةِ واتساقِ المراجعِ (test_w154 + قانونُ الهويةِ)",
            [
                "-m",
                "pytest",
                "tests/governance/test_w154_reviewer_consistency.py",
                "tests/governance/test_identity_law.py",
                "-q",
            ],
            repo_root,
        ),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="جذرُ الشجرةِ المقيسةِ (الافتراضيُّ: جذرُ هذا المستودعِ)",
    )
    args = parser.parse_args()
    repo_root = (args.repo_root or REPO_ROOT).resolve()
    today_plus_4 = (date.today() + timedelta(days=4)).isoformat()

    failures: list[str] = []
    print(f"[PREPUSH] الجذرُ المقيسُ: {repo_root}")
    for name, cmd, cwd in _gates(repo_root, today_plus_4):
        run_cmd = [PY, *cmd]
        print(f"\n[PREPUSH] ▶ {name}")
        result = subprocess.run(
            run_cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            failures.append(name)
            print(result.stdout[-2000:] if result.stdout else "", end="")
            if result.stderr:
                print(result.stderr[-1000:], end="")
            print(f"[PREPUSH] ✗ فشلَ: {name}")
        else:
            tail = (result.stdout or "").strip().splitlines()
            print(tail[-1] if tail else "✓")

    print("\n" + "=" * 60)
    if failures:
        for name in failures:
            print(f"[PREPUSH] ✗ {name}")
        print("[PREPUSH] ممنوعٌ الدفعُ — الحرسُ لم يخضرَّ كلُّه.")
        return 1
    print("[PREPUSH] جائزٌ الدفعُ — الحرسُ أخضرُ كلُّه.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
