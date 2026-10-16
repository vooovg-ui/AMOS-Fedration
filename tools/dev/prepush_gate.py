"""مُشغّلُ حرسِ ما قبلَ الدفعِ — أمرٌ واحدٌ يُشغّلُ البواباتِ كلَّها ويمنعُ الدفعَ عندَ أيِّ فشلٍ.

طريقُ الإنفاذ: PENDING_GATE_ITEM · مؤجَّلٌ ببندِ WI-077 — ربطُه خطوةَ CI أو فحصًا يشملُهُ ينتظرُ إغلاقَ البندِ وقرارَ المالكِ في مسلكِ الدمجِ (`Q-F`)؛ ودليلُ تشغيلِهِ المباشرِ قيَّدهُ W-348 · ورُبِطَ بمسارِ الدفعِ خُطّافَ `pre-push` محليًّا (دليلُ W-349).

التعريف:
    مُشغّلُ البواباتِ المحليةِ قبلَ أيِّ دفعٍ إلى `main`: يُشغّلُ الحرسَ القائمَ كلَّهُ
    بأمرٍ واحدٍ ويخرجُ برمزٍ غيرِ صفريٍّ إن فشلَتْ أيُّ بوابةٍ — فلا يُدفَعُ إلا
    بعدَ خُضرتِه. **لا يُخفَّفُ أيُّ حرسٍ ولا يُضيفُ حكمًا جديدًا** — تنسيقٌ لا
    استبدال.

    [إضافةٌ مؤرَّخةٌ (W-360 · WI-078 · توجيهُ المستشارِ 6 · H2 · 2026-10-16)]:
    وضْعُ `--merge <sha>` — **المسلكُ الوحيدُ الموثَّقُ إلى main**: يُشغّلُ الحرسَ
    السبعةَ أوّلًا، ثمَّ يقرأُ حكمَ CI على العقدةِ نفسِها بأداةِ الحكمِ القائمةِ
    (`ci_verdict_readability.py --require-readable --expect-sha <sha>`) منَ
    البياناتِ الحيّةِ (عبرَ `gh`)، فإن خرجَ صفرًا قدَّمَ `main` تقديمًا سريعًا
    لنفسِ العقدةِ وحدَهَا (`git push origin <sha>:main` بتوقيتِ UTC) — وإلا
    امتنعَ برمزٍ غيرِ صفريٍّ ولم يدفعْ شيئًا. «غيرُ مقروءٍ» ليسَ أخضرَ ولا
    أحمرَ فلا دمجَ. ولا يُستعمَلُ `gh pr merge` ولا force-push ولا يُخفَّفُ
    حرسٌ ولا يُغيَّرُ سلوكُ أداةِ الحكمِ.

    [إضافةٌ مؤرَّخةٌ (W-387 · WI-083 · توجيهُ المستشارِ 9 § 2 · 2026-10-16)]:
    أوّلُ `--merge` حيٍّ رُفِضَ بالرمزِ 2 (W-381) لأنَّ origin في بيئةِ العاملِ
    وسيطٌ (`https://git-agent-proxy.perplexity.ai/…`). فصارت الصيغُ المقبولةُ ثلاثًا
    لا رابعَ لها (`ACCEPTED_ORIGIN_PREFIXES`)، **وشُرِطَ** أن يُطابِقَ owner/repo
    المستخرَجُ `CANONICAL_SLUG` (`vooovg-ui/AMOS-Fedration`) **مطابقةً تامّةً** قبلَ
    أيِّ قراءةِ حكمٍ أو دفعٍ — وإلّا الرمزُ 2 كما كان. ولا تغيّرَ في أداةِ الحكمِ
    ولا في الرموزِ الأخرى.

النطاق:
    بندُ WI-077 (توجيهُ المستشارِ 5 · G3 · DISC-098): الحرسُ السبعةُ المُلزِمةُ
    قبلَ الدفعِ — عقدتا 70441f8 و597d8bb بلغتا `main` حمراوَينِ لأنّ هذه
    البواباتِ لم تكنْ تُشغَّلُ معًا محليًّا قبلَ الدفعِ.

المالك:
    Perplexity Computer (WI-077 · بإذنِ المالكِ العامِّ وتوجيهِ المستشارِ 5).

تاريخ الإنشاء: 2026-10-16 (WI-077 · W-348)
تاريخ آخر تعديل: 2026-10-16 (W-387 · WI-083 — صيغةُ الوسيطِ والمطابقةُ التامّةُ لاسمِ المستودع) · ووقبله 2026-10-15 (WI-077 · المرّةُ الأولى)

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
    .venv/bin/python tools/dev/prepush_gate.py --merge <sha>
        # وجهُ الدمجِ (WI-078): الحرسُ ثمَّ حكمُ CI مقروءًا أخضرَ على العقدةِ
        # نفسِها ثمَّ التقديمُ السريعُ إلى main — لا دفعَ عندَ أيِّ فشلٍ

الخرجُ: رمزُ خروجٍ **0** فقط إن نجحَ الحرسُ كلُّهُ — وأيُّ فشلٍ يمنعُ الدفعَ.
وفي وجهِ `--merge`: **0** فقط إن قُدِّمَ التقديمُ السريعُ فعلًا بعدَ حكمٍ مقروءٍ
أخضرَ — وكلُّ امتناعٍ يُعلِنُ سببَهُ ولا يدفعُ شيئًا.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

#: الجذرُ يُعرَفُ بعلامةٍ لا بعُمقٍ (نمطُ `repo_root.py` · سابقةُ W-336) —
#: فلا يُحتسَبُ هذا الاشتقاقُ في دَينِ الجذرِ الثابتِ، ولا يُقاسُ على شجرةٍ غيرِ مقصودةٍ.
_ROOT_FINDER_PATH = (
    Path(__file__).resolve().with_name("..").resolve() / "governance" / "repo_root.py"
)
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
def _gates(
    repo_root: Path, today_plus_4: str
) -> list[tuple[str, list[str], Path | None]]:
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


# ── وجهُ الدمجِ `--merge <sha>` (WI-078 · توجيهُ المستشارِ 6 · H2) ───────────
#
# القاعدةُ: لا تقديمَ إلى `main` إلا بعدَ (1) خُضرةِ الحرسِ السبعةِ على الشجرةِ
# الحاضرةِ، و(2) حكمِ CI مقروءٍ أخضرَ على العقدةِ نفسِها — ثمَّ التقديمُ السريعُ
# وحدَهُ (`git push origin <sha>:main` بتوقيتِ UTC). كلُّ عطبٍ أو غيابِ حكمٍ
# امتناعٌ مُعلَّنٌ برمزٍ غيرِ صفريٍّ — ولا بديلَ صامتًا.


#: الصيغُ المقبولةُ لعنوانِ origin — ثلاثٌ لا رابعَ لها (WI-083 · توجيهُ المستشارِ 9 § 2):
#: مباشرةٌ بـhttps أو ssh، أو وسيطُ بيئةِ العاملِ الذي يُعيدُ كتابةَ github.com بإعدادٍ
#: مفروضٍ (`url.….insteadof`). والبادئةُ تنتهي بـ`/` أو `:` فلا يمرُّ مضيفٌ مخادعٌ
#: يحملُ الاسمَ بادئةً (مثلَ `github.com.evil/…`).
ACCEPTED_ORIGIN_PREFIXES = (
    "https://github.com/",
    "git@github.com:",
    "https://git-agent-proxy.perplexity.ai/",
)

#: المستودعُ الوحيدُ الذي يُقدِّمُ إليه الوجهُ main — مطابقةٌ تامّةٌ لا بادئةٌ (WI-083):
#: لا مالكَ آخرَ ولا لاحقةَ (`…-fork`) ولا اختلافَ حرف.
CANONICAL_SLUG = "vooovg-ui/AMOS-Fedration"


def _slug_from_url(url: str) -> str:
    """`owner/name` من عنوانِ origin — بعلامةٍ لا بافتراضٍ ولا شبكةٍ.

    يقبلُ الصيغَ الثلاثَ في `ACCEPTED_ORIGIN_PREFIXES`، بلاحقةِ `.git` وبها. ما لم
    يُفهَمْ يُرفَضُ نصًّا (رفضٌ مُصنَّفٌ لا تسامحُ تحليلٍ).
    """
    cleaned = url.strip()
    for prefix in ACCEPTED_ORIGIN_PREFIXES:
        if cleaned.startswith(prefix):
            path = cleaned[len(prefix) :]
            break
    else:
        raise ValueError(
            f"عنوانُ origin غيرُ مفهومٍ لاستخراجِ owner/name منه: {cleaned!r} — "
            "يُرفَضُ ولا يُخمَّنُ مالكٌ."
        )
    path = path.removesuffix(".git").strip("/")
    if path.count("/") != 1 or not path:
        raise ValueError(f"عنوانُ origin لا يحملُ owner/name واحدًا: {cleaned!r} — يُرفَضُ.")
    return path


def _canonical_slug(url: str) -> str:
    """`owner/name` المستخرَجُ **مطابقًا تمامًا** لـ`CANONICAL_SLUG` — وإلّا رفض (WI-083).

    المطابقةُ مساواةٌ لا `startswith` ولا تطبيعُ حالةِ أحرف: مستودعٌ مخادعٌ أو فرعٌ
    منسوخٌ يُرفَضُ قبلَ أيِّ قراءةِ حكمٍ أو دفعٍ.
    """
    slug = _slug_from_url(url)
    if slug != CANONICAL_SLUG:
        raise ValueError(
            f"المستودعُ المُستخرَجُ {slug!r} ليسَ {CANONICAL_SLUG!r} مطابقةً تامّةً — "
            "يُرفَضُ ولا يُقدَّمُ إلى main مستودعٌ آخر."
        )
    return slug


def _origin_url(repo_root: Path) -> str:
    """عنوانُ remote الأصلِ من git نفسِه — لا افتراضَ مالكٍ."""
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    if result.returncode != 0 or not result.stdout.strip():
        raise RuntimeError(
            "تعذَّرَ قراءةُ `git remote get-url origin` — لا يُقاسُ حكمٌ بلا "
            "مالكٍ معروفٍ للمستودعِ."
        )
    return result.stdout.strip()


#: حكمُ الدمجِ حكمُ وظائفِ CI نفسِها — لا يُستبدَلُ بتشغيلٍ أخضرَ منَ
#: مصفوفةِ الحقيقةِ وحدَه: مصفوفةٌ خضراءُ وتشغيلُ CI جارٍ أو غائبٌ يعني
#: «لا حكمَ بعدُ» لا «أخضرُ» (W-362 · عيبٌ رصدهُ مراجعُ التسليمِ: الوجهُ
#: كانَ يقبلُ المصفوفةَ وحدها حكمًا فيُقدِّمُ بلا انتظارِ CI).
CI_WORKFLOW_NAME = "AMOS-Federation CI"


def _select_completed_runs(runs: list, sha: str) -> list:
    """تشغيلاتُ **CI** المكتملةُ على العقدةِ نفسِها — المعلَّقُ لا يُحتسَبُ
    حكمًا · وتشغيلُ المصفوفةِ وحدَهُ ليسَ حكمَ CI فلا يُقدَّمُ بهِ شيءٌ."""
    selected: list = []
    for run in runs:
        if not isinstance(run, dict):
            continue
        if run.get("headSha") != sha or run.get("status") != "completed":
            continue
        if run.get("workflowName") != CI_WORKFLOW_NAME:
            continue
        selected.append(run)
    return selected


def _fetch_jobs_payload(repo_root: Path, slug: str, run_id: str) -> dict:
    """حِملُ وظائفِ تشغيلٍ واحدٍ حيًّا عبرَ `gh api` — بلا توكنٍ في البيئةِ.

    غيابُ `gh` أو فشلُ النداءِ رفضٌ مُصنَّفٌ: يُعلَنُ العجزُ ولا يُقالُ «الحكمُ
    مقروءٌ» ولا «غيرُ مقروءٍ» عن قياسٍ لم يجرِ.
    """
    import json

    result = subprocess.run(
        ["gh", "api", f"repos/{slug}/actions/runs/{run_id}/jobs?per_page=100"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
        timeout=120,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"تعذَّرَ جلبُ وظائفِ التشغيلِ {run_id}: "
            f"{result.stderr.strip()[-500:]} — يُعلَنُ العجزُ ولا يُستبدَلُ بحكمٍ."
        )
    payload = json.loads(result.stdout)
    if not isinstance(payload, dict):
        raise RuntimeError(f"حِملُ التشغيلِ {run_id} ليسَ كائنَ JSON — لا يُقاسُ ما لا يُعرَف.")
    return payload


def _read_verdict(repo_root: Path, slug: str, sha: str, payload_paths: list) -> tuple:
    """قراءةُ الحكمِ بأداةِ الحكمِ نفسِها (`ci_verdict_readability.py`) — لا إعادةَ كتابةٍ.

    يُستدعى كما هو بـ`--from-json` لكلِّ تشغيلٍ مكتملٍ معَ `--require-readable
    --expect-sha <sha>` — فالرمزُ 0 وحدهُ هو الخُضرةَ المقروءةَ على العقدةِ نفسِها.
    """
    cmd = [PY, str(GOVERNANCE / "ci_verdict_readability.py")]
    for path in payload_paths:
        cmd.extend(["--from-json", str(path)])
    cmd.extend(["--repo", slug, "--require-readable", "--expect-sha", sha])
    result = subprocess.run(
        cmd,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
        timeout=120,
    )
    return result.returncode, (result.stdout or "") + (result.stderr or "")


def _merge_flow(sha: str, repo_root: Path, failures: list) -> int:
    """وجهُ الدمجِ: حرسٌ ثمَّ حكمٌ مقروءٌ أخضرُ ثمَّ تقديمٌ سريعٌ — أو امتناعٌ."""
    if failures:
        for name in failures:
            print(f"[PREPUSH] ✗ {name}")
        print(
            "[PREPUSH] ✗ ممنوعٌ الدفعُ — الحرسُ لم يخضرَّ كلَّهُ، فلا يُقرأُ حكمُ "
            "الدمجِ أصلًا ولا يُقدَّمُ شيءٌ (WI-078)."
        )
        return 1

    # العقدةُ المقيسةُ هيَ العقدةُ المدموجةُ — لا يُقاسُ غيرُها ويُدفَعُ هذهِ.
    head_result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    head_sha = head_result.stdout.strip() if head_result.returncode == 0 else ""
    if head_sha != sha:
        print(
            f"[PREPUSH] ✗ رفضٌ: HEAD هو {head_sha[:12] or 'غيرُ معروفٍ'} "
            f"والعقدةُ المطلوبُ دمجُها {sha[:12]} — الحرسُ يقيسُ الشجرةَ الحاضرةَ "
            "فلا يُقدَّمُ إلى main عقدةً لم تُقَسْ شجرتُها (WI-078)."
        )
        return 2

    try:
        slug = _canonical_slug(_origin_url(repo_root))
    except (RuntimeError, ValueError) as exc:
        print(f"[PREPUSH] ✗ رفضٌ مُصنَّفٌ: {exc}")
        return 2

    import json

    result = subprocess.run(
        [
            "gh",
            "run",
            "list",
            "--repo",
            slug,
            "--json",
            "databaseId,headSha,status,conclusion,event,workflowName",
            "--limit",
            "100",
        ],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
        timeout=120,
    )
    if result.returncode != 0:
        print(
            "[PREPUSH] ✗ رفضٌ مُصنَّفٌ: تعذَّرَ `gh run list` — لا يُقرأُ حكمُ CI "
            f"بلا وصولٍ حيٍّ ({result.stderr.strip()[-300:]})."
        )
        return 2
    runs = json.loads(result.stdout)
    if not isinstance(runs, list):
        print("[PREPUSH] ✗ رفضٌ: خرجُ `gh run list` ليسَ قائمةً — لا يُخمَّنُ حكمٌ.")
        return 2

    completed = _select_completed_runs(runs, sha)
    if not completed:
        print(
            f"[PREPUSH] ✗ رفضٌ: لا تشغيلَ مكتملًا لوظائفِ CI "
            f"(‎{CI_WORKFLOW_NAME}‎) على العقدةِ {sha[:12]} — لا حكمَ بعدُ فلا "
            "دمجَ: «غيرُ مقروءٍ» ليسَ أخضرَ ولا أحمرَ · وتشغيلُ المصفوفةِ وحدَهُ "
            "ليسَ حكمَ CI (WI-078 · W-362)."
        )
        return 3

    payload_paths: list = []
    for run in completed:
        run_id = str(run.get("databaseId"))
        try:
            payload = _fetch_jobs_payload(repo_root, slug, run_id)
        except RuntimeError as exc:
            print(f"[PREPUSH] ✗ رفضٌ مُصنَّفٌ (تشغيلُ {run_id}): {exc}")
            return 3
        import tempfile

        payload_path = Path(tempfile.gettempdir()) / f"amos_prepush_merge_{run_id}.json"
        payload_path.write_text(
            json.dumps(payload, ensure_ascii=False), encoding="utf-8"
        )
        payload_paths.append(payload_path)
        print(
            f"[PREPUSH] • حِملُ التشغيلِ {run_id} "
            f"({run.get('workflowName', '—')}) جُلِبَ حيًّا"
        )

    verdict_exit, verdict_text = _read_verdict(repo_root, slug, sha, payload_paths)
    print(verdict_text.rstrip())
    if verdict_exit != 0:
        print(
            f"[PREPUSH] ✗ رفضٌ: بوّابةُ الدمجِ خرجَتْ برمزِ {verdict_exit} — "
            "لا تقديمَ إلى main إلا بحكمٍ مقروءٍ أخضرَ على العقدةِ نفسِها (WI-078)."
        )
        return 4

    push_env = {**os.environ, "TZ": "UTC"}
    push_result = subprocess.run(
        ["git", "push", "origin", f"{sha}:main"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=False,
        timeout=300,
        env=push_env,
    )
    if push_result.stdout:
        print(push_result.stdout, end="")
    if push_result.stderr:
        print(push_result.stderr, end="")
    if push_result.returncode != 0:
        print(
            f"[PREPUSH] ✗ رفضُ التقديمِ السريعِ برمزِ {push_result.returncode} — "
            "لا force-push ولا بديلَ: العطبُ يُصلَحُ في مصدرِهِ ثمَّ تُعادُ "
            "المحاولةُ بالعقدةِ المصحَّحةِ (WI-078)."
        )
        return 5
    print(
        "[PREPUSH] ✓ قُدِّمَ main تقديمًا سريعًا إلى العقدةِ نفسِها بعدَ حكمٍ "
        "مقروءٍ أخضرَ — مسلكُ --merge (WI-078)."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="جذرُ الشجرةِ المقيسةِ (الافتراضيُّ: جذرُ هذا المستودعِ)",
    )
    parser.add_argument(
        "--merge",
        metavar="SHA",
        default="",
        help=(
            "وجهُ الدمجِ (WI-078): الحرسُ ثمَّ قراءةُ حكمِ CI مقروءًا أخضرَ على "
            "العقدةِ نفسِها ثمَّ تقديمٌ سريعٌ إلى main — لا دفعَ عندَ أيِّ فشلٍ."
        ),
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
    if args.merge:
        return _merge_flow(args.merge.strip(), repo_root, failures)
    if failures:
        for name in failures:
            print(f"[PREPUSH] ✗ {name}")
        print("[PREPUSH] ممنوعٌ الدفعُ — الحرسُ لم يخضرَّ كلُّه.")
        return 1
    print("[PREPUSH] جائزٌ الدفعُ — الحرسُ أخضرُ كلُّه.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
