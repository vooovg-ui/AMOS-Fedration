#!/usr/bin/env python3
"""حرسُ إزاحةِ الالتزامِ قبلَ الدفعِ — لا التزامَ دمجٍ بإزاحةٍ غير UTC (`Q-E` · `WI-074`).

طريقُ الإنفاذ: CI_STEP · خطوةُ «بوابة 7» في `.github/workflows/ci.yml` (وظيفةُ
`work-governance-gate`) تُشغِّلُ الأداةَ على المدى الصريحِ `origin/main..HEAD` مع
`--exclude-ephemeral` على حدثَي `pull_request` و`push` — لا انفصالَ بينَ حكمٍ
وتوصيلِهِ. وحارسُ الأداةِ في `tests/governance/test_w074_pre_push_merge_guard.py`
(7 فحوصٍ) يُشغِّلُهُ استدعاءُ `pytest tests/governance/` في CI.

الهدف:
    سدُّ ثغرةِ `W-293`/`W-329` من مصدرِها: التزامُ الدمجِ الذي يُنشِئُهُ الخادمُ
    (`gh pr merge` أو زرُّ الدمجِ في الواجهةِ) بالإزاحةِ المحلّيّةِ لِحسابِ
    المالكِ (مثلُ `+03:00`) كانَ يُدفَعُ إلى `main` **قبلَ** أن ترفضَهُ بوّابةُ
    `Identity Law` الحاليةُ (`test_w110`/`test_w113` · `DISC-044`/`DISC-049`)، لأنّ
    البوّابةَ هناك تُقاسُ بعدَ الدفعِ لا قبلهُ. فالوجهُ هنا **قبلَ الدفعِ**:
    يُفحَصُ التزاماتِ الدمجِ الموجودةُ فعليًّا في المدى `base..head` قبلَ أن
    يُدفَعَ إلى `main`.

الحدُّ المُعلَنُ ولا يُزعَمُ أكثرُ منه:
    * تُقاسُ التزاماتِ الدمجِ **الواقعيّةِ** التي يملكُها المستودعُ: كلُّ التزامٍ
      دمجٍ (أبوانِ أو أكثرُ) في المدى `base..head` ما لم يكن استثناءً مشروطًا.
    * **الاستثناءُ الوحيدُ** هو عقدةُ الدمجِ العارضةُ التي وَلَّدَتها المنصّةُ
      (`refs/pull/<N>/merge`) بشرطٍ ثلاثيٍّ مُقيَّسٍ: دمجٌ · لا يحويه مرجعٌ من
      المستودعِ (لا فرعٌ ولا وسمٌ) · آباؤُهُ مرئيّونَ — فتُستثنى هيَ وحدَها عندَ
      طلبِ الاستثناءِ صراحةً (`--exclude-ephemeral`)، ولا يُقاسُ عليها خرقُ
      الإزاحةِ لأنّها عقدةٌ لا يملكُها المستودعُ وستُولَّدُ من جديدٍ عندَ كلِّ
      تشغيلٍ بلا سلطةٍ للمستودعِ على إزاحتِهَا ولا على إنشائِهَا (`DISC-065`).
    * **المسموحُ صراحةً**: `TZ=UTC git merge --no-ff` والتقديمُ السريعُ
      (`git push origin <sha>:main`) — لأنّ الإزاحةَ عالميّةٌ.
    * **الممنوعُ**: `gh pr merge` وزرُّ الدمجِ في الواجهةِ (`W-293`) — لأنّهُما
      يُنشِئانِ التزامًا بإزاحةِ ساعةِ حسابِ المالكِ (مثلُ `+03:00`) ولن يرفضَهُ
      هذا الحرسُ **قبلَ إنشاءِهِ** (القدرةُ أضيقُ من المنعِ الشاملِ).
    * **القدرةُ المثبتةُ**: رفضُ التزامِ الدمجِ **الموجودِ فعليًّا** قبلَ دفعهِ.
      لا منعُ التزامٍ سيُنشِئُهُ الخادمُ لاحقًا — فذلكَ يبقى ممنوعًا نصًّا
      (`W-293`) لا حرسًا. والحرسُ البَعديُّ القائمُ (`test_w110`/`test_w113` على
      حدثِ `push`) باقٍ كما هو.
    * فحصُ `pull_request` **لا يمنعُ التزامًا سيُنشِئُهُ `gh pr merge` لاحقًا**:
      الحرسُ يُعطي حكمًا على ما دخلَ المدى فعليًّا، والدمجُ الخادميُّ يُنشِئُ
      التزامًا بعدَ الحُكمِ لا قبلهُ — فالحظرُ المطلقُ لتلكَ الوسيلةِ (نصُّ
      `W-293`) **باقٍ** ولا تُكمِلُهُ هذه الأداةُ ولا تُزعمُهُ.
    * غيابُ المرجعِ أو نقصُ التاريخِ = خرجٌ **2** لا صفرًا يوهمُ تمامَ القياسِ
      (القاعدة 12: حارسٌ يُتخطَّى بصمتٍ ليس حارسًا).

النطاق:
    `.github/workflows/ci.yml` (على حدثَي `pull_request` و`push`) وحدَه — لا
    تُغيِّرُ الأداةُ إعدادَ حسابٍ ولا تُنشِئُ تشغيلًا ولا تُعيدُ كتابةَ تاريخٍ
    (لا `force-push`) ولا ترفعُ رقمًا مُعلَنًا في `DISCOVERIES.md` ولا تُغيِّرُ
    `baseline_node`. مكتبةٌ قياسيّةٌ وحدَها (RK-010) وتستوردُ تعريفَ الإزاحةِ
    العالميّةِ من `commit_timestamp_integrity` (مصدرٌ واحدٌ لا نسختانِ).

الملك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المالكِ (`Q-E` · `W-334` ·
تَفويضٌ عامٌّ 2026-10-15)
تاريخ الإنشاء: 2026-10-15 (W-335 · WI-074 · القرارُ `Q-E`)
تاريخ آخر تعديل: 2026-10-15 (W-335 · المرّةُ الأولى)

الاستخدام:
    python tools/governance/pre_push_merge_guard.py --base-ref refs/heads/main --head HEAD
    python tools/governance/pre_push_merge_guard.py --base-ref origin/main --head HEAD --exclude-ephemeral
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import importlib.util

# مصدرٌ واحدٌ للإزاحةِ العالميّةِ: من قِياسِ قانونِ الهُويّةِ لا نسخةٌ ثانيةٌ
_CTI_PATH = Path(__file__).resolve().with_name("commit_timestamp_integrity.py")
_CTI_SPEC = importlib.util.spec_from_file_location(
    "amos_commit_timestamp_integrity", _CTI_PATH
)
if _CTI_SPEC is None or _CTI_SPEC.loader is None:
    raise ImportError(f"commit_timestamp_integrity.py not loadable from {_CTI_PATH}")
_CTI = importlib.util.module_from_spec(_CTI_SPEC)
_CTI_SPEC.loader.exec_module(_CTI)

GENERATED_MERGE_REF = _CTI.GENERATED_MERGE_REF
UTC_SUFFIXES = _CTI.UTC_SUFFIXES

_ROOT_FINDER_PATH = Path(__file__).resolve().with_name("repo_root.py")
_ROOT_FINDER_SPEC = importlib.util.spec_from_file_location(
    "amos_repo_root_finder", _ROOT_FINDER_PATH
)
if _ROOT_FINDER_SPEC is None or _ROOT_FINDER_SPEC.loader is None:
    raise ImportError(f"repo_root.py not loadable from {_ROOT_FINDER_PATH}")
_ROOT_FINDER = importlib.util.module_from_spec(_ROOT_FINDER_SPEC)
_ROOT_FINDER_SPEC.loader.exec_module(_ROOT_FINDER)
REPO_ROOT = _ROOT_FINDER.discover_repo_root(__file__)


class GuardRefUnreachable(RuntimeError):
    """يُرفَعُ حينَ لا يُرى مرجعٌ لازمٌ — فلا يُقاسُ ولا يُطوى ولا يُقالَ «أخضرُ»."""


def _git(args: list[str], repo: Path) -> str:
    out = subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, timeout=60, check=False
    )
    if out.returncode != 0:
        raise GuardRefUnreachable(
            f"فشلَ `git {' '.join(args)}` في {repo}: {out.stderr.strip()}"
        )
    return out.stdout


def _rev_exists(repo: Path, rev: str) -> bool:
    out = subprocess.run(
        ["git", "cat-file", "-e", f"{rev}^{{commit}}"],
        cwd=repo, capture_output=True, text=True, timeout=60, check=False,
    )
    return out.returncode == 0


def _is_utc_stamp(stamp: str) -> bool:
    return stamp.endswith(UTC_SUFFIXES)


def _resolve_ref(repo: Path, ref: str) -> str:
    """يُعيدُ SHA الالتزامِ لمرجعٍ أو لأمرٍ — غيابُه خرجٌ 2 لا تخمينٌ."""
    return _git(["rev-parse", "--verify", ref], repo).strip()


def platform_merge_head(repo: Path, head_rev: str = "HEAD") -> str | None:
    """عقدةُ الدمجِ العارضةُ التي وَلَّدَتها المنصّةُ — نفسُ شرطِ `DISC-065`.

    ثلاثيّةٌ مُقيَّسةٌ: رأسٌ التزامُ دمجٍ · لا يحويه إلّا مرجعُ دمجٍ عارضٌ ·
    آباؤُهُ مرئيّونَ. فما لا يستوفيها **يُقاسُ** — الاستثناءُ أضيقُ من أن يُفلِتَ
    منه خرقٌ.
    """
    try:
        head_line = _git(["rev-list", "--parents", "-n", "1", head_rev], repo).split()
    except GuardRefUnreachable as unreachable:
        # الغيابُ مُعلَنٌ لا مَطويٌّ: عقدةٌ لا تُقَرأُ لا تُخمَّنُ «عارضةً» ولا «حقيقيةً»
        print(
            f"[MERGE GUARD] △ لم يُقَس رأسُ HEAD للاستثناءِ: {unreachable}",
            file=sys.stderr,
        )
        return None
    if len(head_line) < 3:  # الأوّلُ الابنُ وما بعدَه آباؤُه
        return None
    head, parents = head_line[0], head_line[1:]
    refs = _git(
        ["for-each-ref", "--contains", head, "--format=%(refname)"], repo
    ).split()
    # قائمةٌ فارغةٌ ليست «كلُّها عارضةٌ»: رأسٌ على detached HEAD لا يحويه مرجعٌ
    # أصلًا ليس عقدةَ منصةٍ — فلا يُستثنى التزامٌ حقيقيٌّ بغيابِ مرجعٍ (ثغرةُ W-336)
    if not refs or any(GENERATED_MERGE_REF.match(ref) is None for ref in refs):
        return None
    if any(not _rev_exists(repo, parent) for parent in parents):
        return None
    return head


def _is_shallow(repo: Path) -> bool:
    """أسجلٌّ ضحلٌ بعَلَمِ git؟ — يُعلَنُ ولا يُطوى (لا حكمَ «أخضرُ» على جزءٍ)."""
    return _git(["rev-parse", "--is-shallow-repository"], repo).strip() == "true"


def _merge_commits_in_range(repo: Path, base: str, head: str) -> dict[str, str]:
    """كلُّ التزاماتِ الدمجِ في المدى `base..head` — SHA ↦ طابع `%cI`."""
    raw = _git(
        ["log", "--format=%H %cI", "--merges", f"{base}..{head}"], repo
    ).strip()
    stamps: dict[str, str] = {}
    if not raw:
        return stamps
    for line in raw.splitlines():
        parts = line.split()
        if len(parts) < 2:
            continue
        stamps[parts[0]] = parts[1]
    return stamps


def guard_report(
    repo: Path | None = None,
    base_ref: str = "refs/heads/main",
    head_ref: str = "HEAD",
    exclude_ephemeral: bool = False,
) -> tuple[str, int]:
    """حكمُ الحرسِ على المدى `base..head`: رسالةٌ ورمزُ خروجٍ.

    الرسالةُ تُسمّي التصريحَ الغائبَ سببًا (الإزاحةَ المحلّيّةَ للعقدةِ
    المَدروسةِ) لا تُسمّي الدمجَ الخادميَّ حصرًا. ولا يُقالَ «أخضرُ» على غيابِ
    مرجعٍ — الغيابُ خرجٌ 2 مُعلَنٌ لا صفرٌ صامتٌ.
    """
    repo = Path(repo) if repo is not None else REPO_ROOT
    try:
        base_sha = _resolve_ref(repo, base_ref)
    except GuardRefUnreachable as unreachable:
        return (
            f"[MERGE GUARD] ✗ لم يُقَس: المرجعُ الأساسُ `{base_ref}` غيرُ مرئيٍّ في "
            f"{repo} ({unreachable}) — فشرطُ «كلُّ التزامِ دمجٍ في المدى بإزاحةٍ "
            "عالميّةٍ» لم يُقَس هنا ولا يُدَّعى خُضرةً"
        ), 2
    try:
        head_sha = _resolve_ref(repo, head_ref)
    except GuardRefUnreachable as unreachable:
        return (
            f"[MERGE GUARD] ✗ لم يُقَس: رأسُ المدى `{head_ref}` غيرُ مرئيٍّ في "
            f"{repo} ({unreachable}) — فشرطُ «كلُّ التزامِ دمجٍ في المدى بإزاحةٍ "
            "عالميّةٍ» لم يُقَس هنا ولا يُدَّعى خُضرةً"
        ), 2

    # سجلٌّ ضحلٌ = قياسٌ على جزءٍ: لا يُقالَ «أخضرُ» على مدىً قد يكونُ أبواهُ خارجَ
    # المرآةِ — يُعلَنُ عجزُ القياسِ (خرجٌ 2) لا يُطوى ولا يُخمَّنُ (ثغرةُ W-336)
    if _is_shallow(repo):
        return (
            "[MERGE GUARD] ✗ لم يُقَس: سجلٌّ ضحلٌ (استنساخٌ بعمقٍ محدودٍ) — "
            "آباءُ التزاماتِ الدمجِ قد يكونونَ خارجَ المرآةِ فلا يُقاسُ المدى كاملًا "
            "ولا يُدَّعى خُضرةً"
        ), 2

    merges = _merge_commits_in_range(repo, base_sha, head_sha)
    ephemeral: str | None = None
    if exclude_ephemeral:
        ephemeral = platform_merge_head(repo, head_sha)
    if ephemeral is not None and ephemeral in merges:
        merges = {k: v for k, v in merges.items() if k != ephemeral}
        print(
            f"[MERGE GUARD] △ استُثنِيَ من النطاقِ `{ephemeral[:10]}` — عقدةُ دمجٍ "
            "وَلَّدَتها منصّةُ الاستضافةِ في `refs/pull/*/merge` ولا يحويها فرعٌ "
            "فليست من تاريخِ المستودعِ (`DISC-065`)، وقِيسَ كلُّ التزاماتِ الدمجِ "
            "الأخرى في المدى فلا يُفلِتُ خرقٌ",
            file=sys.stderr,
        )

    violations = {k: v for k, v in merges.items() if not _is_utc_stamp(v)}
    if violations:
        cause = (
            "السببُ: غيابُ التصريحِ بإزاحةِ `+00:00` عندَ إنشاءِ الالتزامِ "
            "(TZ=UTC أو GIT_COMMITTER_DATE بإزاحةِ +00:00)، فوُرِثَت إزاحةُ "
            "بيئةِ المُنشِئِ"
        )
        return (
            "[MERGE GUARD] ✗ التزامُ دمجٍ بإزاحةٍ محلّيّةٍ: "
            + " · ".join(f"{sha[:10]}={stamp}" for sha, stamp in violations.items())
            + f" — {cause} · ولا يُرفَعُ الرقمُ المُعلَنُ ولا يُخفَّفُ حرسٌ قائمٌ"
        ), 1

    if not merges and ephemeral is None:
        return (
            f"[MERGE GUARD] ✓ المدى `{base_sha[:10]}..{head_sha[:10]}` لا يحتوي "
            "على التزامِ دمجٍ — فلا خرقَ يُقاسُ على التزاماتِ الدمجِ (وليسَ هذا "
            "إثباتًا للتقديمِ السريعِ: انعدامُ الدمجِ شرطٌ لا برهانُ ff)"
        ), 0
    return (
        f"[MERGE GUARD] ✓ كلُّ التزامِ دمجٍ ({len(merges)}) في المدى "
        f"`{base_sha[:10]}..{head_sha[:10]}` إزاحتُه عالميّةٌ"
    ), 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="حرسُ إزاحةِ التزامِ الدمجِ قبلَ الدفعِ (Q-E · WI-074)"
    )
    parser.add_argument(
        "--repo", default="", help="مسارُ المستودعِ (افتراضيًّا: جذرُ المستودعِ المكتشَف)"
    )
    parser.add_argument(
        "--base-ref",
        default="refs/heads/main",
        help=(
            "المرجعُ الأساسُ (افتراضيًّا: refs/heads/main — في CI على pull_request "
            "يُمرَّر origin/main أو github.event.pull_request.base.sha)"
        ),
    )
    parser.add_argument(
        "--head",
        default="HEAD",
        help="رأسُ المدى (افتراضيًّا: HEAD)",
    )
    parser.add_argument(
        "--exclude-ephemeral",
        action="store_true",
        help=(
            "استثناءُ عقدةِ الدمجِ العارضةِ (refs/pull/N/merge) وحدها — شرطٌ "
            "ثلاثيٌّ مُقيَّسٌ: دمجٌ · لا يحويه فرعٌ · آباؤُهُ مرئيّونَ (`DISC-065`)"
        ),
    )
    args = parser.parse_args(argv)

    repo = Path(args.repo) if args.repo else REPO_ROOT
    if not (repo / ".git").exists():
        print(f"[MERGE GUARD] ✗ ليسَ مستودعَ git: {repo}", file=sys.stderr)
        return 2

    report, code = guard_report(
        repo=repo,
        base_ref=args.base_ref,
        head_ref=args.head,
        exclude_ephemeral=args.exclude_ephemeral,
    )
    if code == 0:
        print(report)
    else:
        print(report, file=sys.stderr)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
