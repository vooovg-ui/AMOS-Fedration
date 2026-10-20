#!/usr/bin/env python3
"""
حارسُ ساعةِ طوابعِ الالتزامِ — Commit Stamp Clock Guard

الهدف: تنفيذُ أمرِ المالكِ (Q-64 · 2026-10-20) نصًّا: «ختمُ الوقتِ في القيودِ منَ
       الساعةِ الفعليةِ فقط، لا يُكتبُ يدويًّا ولا يُؤخَّرُ لينجحَ حارسُ الرتابةِ».
       يرفضُ الحارسُ كلَّ التزامٍ جديدٍ (فوقَ الفرعِ الحاكمِ) ختمُهُ:
         FUTURE_STAMP         أحدثُ منَ الساعةِ الفعليةِ لحظةَ الفحصِ (+ هامشٍ مُعلَنٍ) —
                              فالالتزامُ لا يُولَدُ بعدَ أن يُفحَصَ.
         AUTHOR_AFTER_COMMIT  ختمُ المؤلفِ أحدثُ من ختمِ الالتزامِ الفعليِّ (+ الهامشِ) —
                              تأليفٌ بعدَ إنشاءِ الالتزامِ محالٌ إلّا كتابةً يدويةً.
         BEFORE_PARENT        ختمُ الالتزامِ أقدمُ من ختمِ أبيه (أيِّ أبٍ) — صارمٌ لكلِّ
                              التزامٍ جديدٍ لا دَينًا مجمَّعًا يُسمَحُ بنموِّه.
النطاق: الفحصُ وحدَهُ على مدى الالتزاماتِ الجديدةِ (`<الأساس>..HEAD`). لا يُصحِّحُ
        تاريخًا ماضيًا ولا يُعيدُ كتابةَ التاريخِ — القيودُ السابقةُ لا تُعدَّلُ
        (أمرُ المالكِ نصًّا · § 4.5 منَ الأمرِ الدائمِ). والدَّينُ التاريخيُّ مقيسٌ
        مُعلَنٌ في DISC-118 وفي `commit_timestamp_integrity.py` (المجموعُ لا يعلو).
المالك: tools/governance — بندُ WI-102 (Perplexity Computer · قيدُ W-554)
تاريخ الإنشاء: 2026-10-20
تاريخ آخر تعديل: 2026-10-20 (W-554 · WI-102 · DISC-118)

طريقُ الإنفاذ: COVERED_TEST · tests/governance/test_commit_stamp_clock_guard.py::test_live_new_commits_stamped_by_real_clock يحكُمُ على الشجرةِ الحاضرةِ (origin/main..HEAD بالساعةِ الفعليةِ) ويشملُه استدعاءُ `pytest tests/governance/` في CI

## لماذا لا يكفي حارسُ الرتابةِ القائمُ (DISC-118)
`commit_timestamp_integrity.py` يقيسُ الرتابةَ **مجموعًا لا يعلو** — فختمٌ مستقبليٌّ
يمرُّ ما دامَ أحدثَ من أبيه، والتالي يُضطَرُّ إلى ختمٍ أحدثَ منه أو إلى **انتظارِ**
الساعةِ حتى تتجاوزَه. وقعَ النمطانِ مقيسَينِ: W-442…W-454 (طوابعُ مستديرةٌ بفاصلٍ
ثابتٍ · W-452/W-453/W-454 أحدثُ من بدءِ سيرِ العملِ الذي فحصَها) ثمَّ W-547…W-549
(الثلاثةُ أحدثُ من بدءِ سيرِ دفعِها) ثمَّ W-550 (أُخِّرَ لينجحَ حارسُ الرتابةِ).
فالوجهُ الناقصُ: **مقارنةُ الختمِ بالساعةِ الفعليةِ** — وهو ما يُضيفُه هذا الحارسُ.

## الحدُّ المُعلَنُ في الأداةِ نفسِها
- «الساعةُ الفعليةُ» هي ساعةُ مُشغِّلِ الفحصِ: محليًّا قبلَ الدفعِ، وفي CI لحظةَ
  تشغيلِ الفحصِ الحيِّ (`tests/governance/test_commit_stamp_clock_guard.py`) بعدَ
  الدفعِ — فختمٌ مستقبليٌّ يُرفَضُ ما لم يُفحَصْ بعدَ موعدِه المختومِ. وهذا حدٌّ
  حقيقيٌّ: ختمٌ مستقبليٌّ قصيرُ الإزاحةِ يُدفَعُ ثمَّ يُفحَصُ بعدَ مرورِه يمرُّ.
  فيُكمِّلُه وجهُ AUTHOR_AFTER_COMMIT ووجهُ BEFORE_PARENT على التزامٍ لاحقٍ صادقٍ.
- الهامشُ الافتراضيُّ 120 ثانيةً لاختلافِ الساعاتِ بينَ الأجهزةِ — مُعلَنٌ في كلِّ حكمٍ.
- عقدةُ الدمجِ العارضةُ التي تُولِّدُها المنصّةُ (`refs/pull/<N>/merge` · DISC-065)
  تُستثنى بشرطِ `platform_merge_head` نفسِه ويُعلَنُ استثناؤها في الحكمِ.

الاستخدام:
    python tools/governance/commit_stamp_clock_guard.py
    python tools/governance/commit_stamp_clock_guard.py --range origin/main..HEAD
    python tools/governance/commit_stamp_clock_guard.py --range A..B --now 2026-10-20T08:10:41Z
رموزُ الخروجِ: 0 لا مخالفةَ · 1 مخالفةٌ · 2 تعذَّرَ القياسُ (لا يُخمَّنُ حكمٌ).
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_INTEGRITY_SPEC = importlib.util.spec_from_file_location(
    "commit_timestamp_integrity", _HERE / "commit_timestamp_integrity.py"
)
if _INTEGRITY_SPEC is None or _INTEGRITY_SPEC.loader is None:
    raise ImportError("تعذَّرَ تحميلُ commit_timestamp_integrity.py (شرطُ الدمجِ العارضِ)")
_INTEGRITY = importlib.util.module_from_spec(_INTEGRITY_SPEC)
_INTEGRITY_SPEC.loader.exec_module(_INTEGRITY)

DEFAULT_TOLERANCE_SECONDS = 120
BASE_CANDIDATES = ("origin/main", "main")


class StampUnreadable(RuntimeError):
    """تعذَّرَ قراءةُ سجلِّ git — يُعلَنُ ولا يُخمَّنُ حكمٌ."""


@dataclass(frozen=True)
class Commit:
    sha: str
    parents: tuple[str, ...]
    author: datetime
    committer: datetime
    subject: str


@dataclass(frozen=True)
class Violation:
    code: str
    sha: str
    subject: str
    detail: str


def _git(args: list[str], repo: Path) -> str:
    out = subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, timeout=60, check=False
    )
    if out.returncode != 0:
        raise StampUnreadable(f"فشلَ `git {' '.join(args)}`: {out.stderr.strip()}")
    return out.stdout


def _parse(stamp: str) -> datetime:
    return datetime.fromisoformat(stamp.strip().replace("Z", "+00:00"))


def _rev_exists(repo: Path, rev: str) -> bool:
    out = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}"],
        cwd=repo, capture_output=True, text=True, timeout=30, check=False,
    )
    return out.returncode == 0


def default_base(repo: Path) -> str | None:
    for cand in BASE_CANDIDATES:
        if _rev_exists(repo, cand):
            return cand
    return None


def read_commit(repo: Path, rev: str) -> Commit:
    sep = "\x1f"
    raw = _git(["log", "-1", f"--format=%H{sep}%P{sep}%aI{sep}%cI{sep}%s", rev], repo)
    sha, parents, a, c, subject = raw.rstrip("\n").split(sep, 4)
    return Commit(sha, tuple(parents.split()), _parse(a), _parse(c), subject)


def commits_in_range(repo: Path, rng: str) -> list[Commit]:
    shas = _git(["rev-list", "--reverse", rng], repo).split()
    return [read_commit(repo, s) for s in shas]


def check_commits(
    commits: list[Commit],
    repo: Path,
    now: datetime,
    tolerance: timedelta,
) -> list[Violation]:
    """الأوجهُ الثلاثةُ على كلِّ التزامٍ — لا دَينَ يُسمَحُ به في المدى الجديدِ."""
    found: list[Violation] = []
    limit = now + tolerance
    cache: dict[str, Commit] = {c.sha: c for c in commits}
    for c in commits:
        for label, stamp in (("الالتزام", c.committer), ("المؤلف", c.author)):
            if stamp > limit:
                found.append(Violation(
                    "FUTURE_STAMP", c.sha, c.subject,
                    f"ختمُ {label} {stamp.isoformat()} أحدثُ منَ الساعةِ الفعليةِ "
                    f"{now.isoformat()} بـ{int((stamp - now).total_seconds())} ثانيةً "
                    f"(الهامشُ {int(tolerance.total_seconds())})",
                ))
        if c.author > c.committer + tolerance:
            found.append(Violation(
                "AUTHOR_AFTER_COMMIT", c.sha, c.subject,
                f"ختمُ المؤلفِ {c.author.isoformat()} أحدثُ من ختمِ الالتزامِ "
                f"{c.committer.isoformat()} — تأليفٌ بعدَ الإنشاءِ لا يكونُ إلّا كتابةً",
            ))
        for p in c.parents:
            parent = cache.get(p) or read_commit(repo, p)
            cache[p] = parent
            if c.committer < parent.committer:
                found.append(Violation(
                    "BEFORE_PARENT", c.sha, c.subject,
                    f"ختمُ الالتزامِ {c.committer.isoformat()} أقدمُ من ختمِ أبيه "
                    f"{parent.sha[:7]} ({parent.committer.isoformat()})",
                ))
    return found


def resolve_range(repo: Path, rng: str | None) -> tuple[list[str], str | None, str]:
    """المدى (أو المديانِ عندَ استثناءِ الدمجِ العارضِ) ومن استُثنِيَ ووصفُ الأساسِ."""
    if rng:
        return ([rng], None, rng)
    base = default_base(repo)
    if base is None:
        raise StampUnreadable("لا أساسَ يُقاسُ عليه (origin/main أو main غائبانِ)")
    foreign = _INTEGRITY.platform_merge_head(repo)
    if foreign is None:
        return ([f"{base}..HEAD"], None, f"{base}..HEAD")
    parents = _git(["rev-list", "--parents", "-n", "1", foreign], repo).split()[1:]
    return ([f"{base}..{p}" for p in parents], foreign, f"{base}..(آباءُ {foreign[:7]})")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="حارسُ ساعةِ طوابعِ الالتزامِ (Q-64 · WI-102)")
    ap.add_argument("--range", help="مدى git (الافتراضيُّ: origin/main..HEAD)")
    ap.add_argument("--now", help="الساعةُ المرجعيةُ ISO-8601 (الافتراضيُّ: الساعةُ الفعليةُ)")
    ap.add_argument("--tolerance-seconds", type=int, default=DEFAULT_TOLERANCE_SECONDS)
    ap.add_argument("--repo-root", default=".")
    args = ap.parse_args(argv)
    repo = Path(args.repo_root).resolve()
    now = _parse(args.now) if args.now else datetime.now(timezone.utc)
    tolerance = timedelta(seconds=args.tolerance_seconds)
    try:
        ranges, foreign, label = resolve_range(repo, args.range)
        seen: dict[str, Commit] = {}
        for r in ranges:
            for c in commits_in_range(repo, r):
                seen.setdefault(c.sha, c)
        commits = list(seen.values())
        violations = check_commits(commits, repo, now, tolerance)
    except StampUnreadable as exc:
        print(f"[STAMP CLOCK] ✗ تعذَّرَ القياسُ — {exc}")
        return 2
    print(f"[STAMP CLOCK] المدى: {label} · التزاماتٌ مفحوصةٌ: {len(commits)} · "
          f"الساعةُ: {now.isoformat()} · الهامشُ: {int(tolerance.total_seconds())} ثانيةً")
    if foreign:
        print(f"[STAMP CLOCK] ⊘ استُثنِيَت عقدةُ الدمجِ العارضةُ {foreign[:7]} "
              "(refs/pull/<N>/merge · DISC-065) وفُحِصَ آباؤها")
    for v in violations:
        print(f"  ✗ {v.code} · {v.sha[:7]} «{v.subject[:60]}» — {v.detail}")
    if violations:
        print(f"[STAMP CLOCK] ✗ {len(violations)} مخالفةً — الختمُ منَ الساعةِ الفعليةِ "
              "فقط (`TZ=UTC git commit` بلا GIT_*_DATE) ولا يُؤخَّرُ لينجحَ حارسٌ (Q-64)")
        return 1
    print("[STAMP CLOCK] ✓ لا ختمَ أحدثَ منَ الساعةِ الفعليةِ ولا أقدمَ من أبيه.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
