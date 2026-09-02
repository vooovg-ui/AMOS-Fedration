#!/usr/bin/env python3
"""
قياسُ صدقِ طوابعِ الالتزامِ — Commit Timestamp Integrity Measure

الهدف: تصييرُ حدِّ الصدقِ 9 في [`COMPLETION_LEDGER.md § 10`] رقمًا يُقاسُ من سجلِّ
       git لا فقرةً تُروى: كم التزامًا إزاحتُه ليست `+00:00`، وكم طابعًا مكرَّرًا
       بينَ التزاماتٍ مختلفةٍ (‏علامةُ طابعٍ محفورٍ نصًّا لا مقروءٍ من ساعةٍ)، وكم
       موضعًا يسبقُ فيه الطفلُ أباهُ زمنًا.
النطاق: القياسُ وحدَه. لا يُصحِّحُ هذا الملفُّ تاريخًا ماضيًا ولا يُعيدُ كتابةَ
        تاريخِ المستودعِ (‏`force-push` يمحو قيودًا مدفوعةً · § 10 حدًّا 9).
المالك: tools/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-09-02
تاريخ آخر تعديل: 2026-09-02

## الحدُّ المُعلَنُ في الأداةِ نفسِها
القياسُ لا يصدُقُ إلّا على سجلٍّ كاملٍ. فعلى مرآةٍ ضحلةٍ (`--depth`) تُرى
التزاماتٌ أقلُّ، فيُقاسُ أقلُّ — ولذلك تُعلِنُ الأداةُ ضحالةَ السجلِّ صراحةً في
حكمِها بدلَ أن تُوهِمَ بنقصانِ الدَّينِ.

الاستخدام:
    python tools/governance/commit_timestamp_integrity.py --check
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

_ROOT_FINDER_PATH = Path(__file__).resolve().with_name("repo_root.py")
_ROOT_FINDER_SPEC = importlib.util.spec_from_file_location(
    "amos_repo_root_finder", _ROOT_FINDER_PATH
)
if _ROOT_FINDER_SPEC is None or _ROOT_FINDER_SPEC.loader is None:
    raise ImportError(f"تعذّرَ تحميلُ مُكتشِفِ الجذرِ من {_ROOT_FINDER_PATH}")
_ROOT_FINDER = importlib.util.module_from_spec(_ROOT_FINDER_SPEC)
_ROOT_FINDER_SPEC.loader.exec_module(_ROOT_FINDER)

REPO_ROOT = _ROOT_FINDER.discover_repo_root(__file__)

BASELINE_RECORD = Path("docs/governance/work/DISCOVERIES.md")
BASELINE_KEY = "COMMIT_STAMP_BASELINE:"
BASELINE_FIELDS = ("non_utc", "duplicate_groups", "duplicate_commits", "non_monotonic")
HISTORY_FIELD = "history_commits"


class CommitHistoryUnreadable(RuntimeError):
    """يُرفَعُ حينَ يتعذَّرُ قراءةُ سجلِّ git — ولا يُبتلَعُ الخطأُ ولا يُخمَّنُ رقمٌ."""


class BaselineRecordMissing(RuntimeError):
    """يُرفَعُ حينَ يغيبُ سطرُ الرقمِ المُعلَنِ أو يتكرَّرُ — فلا مرجعَ يُقاسُ عليه."""


def _git(args: list[str], repo: Path) -> str:
    out = subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, timeout=60, check=False
    )
    if out.returncode != 0:
        raise CommitHistoryUnreadable(
            f"فشلَ `git {' '.join(args)}` في {repo}: {out.stderr.strip()}"
        )
    return out.stdout


def is_shallow(repo: Path) -> bool:
    """أسجلٌّ ضحلٌ بعَلَمِ git؟ — تُعلَنُ الضحالةُ ولا تُطوى."""
    return _git(["rev-parse", "--is-shallow-repository"], repo).strip() == "true"


def has_full_history(repo: Path | None = None, measured: dict[str, int] | None = None) -> bool:
    """أهذا سجلٌّ كاملٌ؟ — يُقاسُ بعددِ الالتزاماتِ لا بعَلَمٍ وحدَه.

    مرآةٌ تُبنى عبرَ الواجهةِ البرمجيّةِ لا تحملُ عَلَمَ الضحالةِ وهي ناقصةٌ فعلًا،
    فالمعيارُ الصادقُ: أن يبلغَ عددُ الالتزاماتِ المرئيّةِ العددَ المُعلَنَ في
    السجلِّ حينَ قِيسَ الدَّينُ. وما دونَه قياسٌ على جزءٍ، فلا يُطلَبُ عليه خفضٌ.
    """
    repo = Path(repo) if repo is not None else REPO_ROOT
    if is_shallow(repo):
        return False
    counts = measured if measured is not None else measure(repo)
    return counts["commits"] >= declared_history_commits(repo)


def measure(repo: Path | None = None) -> dict[str, int]:
    """يقيسُ الحقولَ الأربعةَ من سجلِّ git — أرقامٌ تُعادُ لا تُروى."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    raw = _git(["log", "--format=%H %cI %P"], repo).strip()
    if not raw:
        raise CommitHistoryUnreadable(f"سجلُّ git فارغٌ في {repo} — لا قياسَ بلا سجلٍّ")

    stamps: dict[str, str] = {}
    parents: dict[str, list[str]] = {}
    for line in raw.splitlines():
        parts = line.split()
        sha, stamp = parts[0], parts[1]
        stamps[sha] = stamp
        parents[sha] = parts[2:]

    # git يكتبُ التوقيتَ العالميَّ «Z» ويكتبُ غيرَه إزاحةً صريحةً — والوجهانِ عالميّانِ
    non_utc = sum(
        1 for s in stamps.values() if not (s.endswith("Z") or s.endswith("+00:00"))
    )

    seen: dict[str, list[str]] = {}
    for sha, stamp in stamps.items():
        seen.setdefault(stamp, []).append(sha)
        # تكرارُ الطابعِ بينَ التزامَينِ مختلفَينِ علامةُ حفرِ نصٍّ لا قراءةِ ساعةٍ
    groups = {stamp: shas for stamp, shas in seen.items() if len(shas) > 1}
    duplicate_groups = len(groups)
    duplicate_commits = sum(len(shas) for shas in groups.values())

    non_monotonic = 0
    for sha, stamp in stamps.items():
        child = datetime.fromisoformat(stamp)
        for parent in parents[sha]:
            if parent not in stamps:
                continue  # حدُّ المرآةِ الضحلةِ: أبٌ خارجَ السجلِّ لا يُقاسُ، ويُعلَنُ في الحكمِ
            if child < datetime.fromisoformat(stamps[parent]):
                non_monotonic += 1

    return {
        "non_utc": non_utc,
        "duplicate_groups": duplicate_groups,
        "duplicate_commits": duplicate_commits,
        "non_monotonic": non_monotonic,
        "commits": len(stamps),
    }


def declared_baseline(repo: Path | None = None) -> dict[str, int]:
    """يقرأُ الرقمَ المُعلَنَ من سجلِّ الاكتشافاتِ — مصدرٌ واحدٌ لا يُنازَع."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    text = (repo / BASELINE_RECORD).read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if BASELINE_KEY in ln]
    if len(lines) != 1:
        raise BaselineRecordMissing(
            f"سطرُ `{BASELINE_KEY}` في {BASELINE_RECORD} وُجِدَ {len(lines)} مرّةً "
            "والمطلوبُ مرّةً واحدةً — لا يُخمَّنُ رقمٌ ولا يُتجاوَزُ الحرسُ"
        )
    values: dict[str, int] = {}
    for field in BASELINE_FIELDS:
        match = re.search(rf"{field}=(\d+)", lines[0])
        if match is None:
            raise BaselineRecordMissing(
                f"الحقلُ `{field}` غائبٌ عن سطرِ `{BASELINE_KEY}` — الرقمُ المُعلَنُ ناقصٌ"
            )
        values[field] = int(match.group(1))
    return values


def declared_history_commits(repo: Path | None = None) -> int:
    """عددُ الالتزاماتِ الذي قِيسَ عليه الدَّينُ المُعلَنُ — يُقرأُ من السجلِّ نفسِه."""
    repo = Path(repo) if repo is not None else REPO_ROOT
    text = (repo / BASELINE_RECORD).read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if BASELINE_KEY in ln]
    if len(lines) != 1:
        raise BaselineRecordMissing(
            f"سطرُ `{BASELINE_KEY}` وُجِدَ {len(lines)} مرّةً والمطلوبُ مرّةً واحدةً"
        )
    match = re.search(rf"{HISTORY_FIELD}=(\d+)", lines[0])
    if match is None:
        raise BaselineRecordMissing(
            f"الحقلُ `{HISTORY_FIELD}` غائبٌ عن سطرِ `{BASELINE_KEY}` — "
            "فلا يُعرَفُ أكاملٌ هذا السجلُّ أم جزءٌ منه"
        )
    return int(match.group(1))


def main() -> int:
    parser = argparse.ArgumentParser(description="قياسُ صدقِ طوابعِ الالتزامِ")
    parser.add_argument("--check", action="store_true", help="يقيسُ ويُقارِنُ بالمُعلَنِ")
    args = parser.parse_args()

    measured = measure()
    declared = declared_baseline()
    full = has_full_history(REPO_ROOT, measured)
    print(
        "COMMIT_STAMP: مقيسٌ "
        + " · ".join(f"{k}={measured[k]}" for k in BASELINE_FIELDS)
        + f" (‏من {measured['commits']} التزامًا"
        + (" · سجلٌّ كاملٌ" if full else " · **سجلٌّ ناقصٌ فالقياسُ على جزءٍ**")
        + ") · المُعلَنُ "
        + " · ".join(f"{k}={declared[k]}" for k in BASELINE_FIELDS)
    )
    if not args.check:
        return 0

    grown = {k: (measured[k], declared[k]) for k in BASELINE_FIELDS if measured[k] > declared[k]}
    if grown:
        print(
            "[COMMIT STAMP] ✗ الدَّينُ علا: "
            + " · ".join(f"{k}: مقيسٌ {m} · المُعلَنُ {d}" for k, (m, d) in grown.items()),
            file=sys.stderr,
        )
        return 1
    if full:
        shrunk = {
            k: (measured[k], declared[k]) for k in BASELINE_FIELDS if measured[k] < declared[k]
        }
        if shrunk:
            print(
                "[COMMIT STAMP] ✗ المقيسُ انخفضَ ولم يُخفَضِ المُعلَنُ: "
                + " · ".join(f"{k}: مقيسٌ {m} · المُعلَنُ {d}" for k, (m, d) in shrunk.items()),
                file=sys.stderr,
            )
            return 1
    print("[COMMIT STAMP] ✓ لا نموَّ في دَينِ الطوابعِ.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
