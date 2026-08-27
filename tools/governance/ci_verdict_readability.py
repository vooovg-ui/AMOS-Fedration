#!/usr/bin/env python3
"""مقروئيّةُ حكمِ CI — هل نُفِّذَت خطوةٌ أصلًا قبلَ أن يُقرأَ الحكم؟ (W-051).

الهدف:
    إنفاذُ التخفيفِ المُعلَنِ في `RK-011` أداةً لها رمزُ خروجٍ، بدلَ أن يبقى
    إجراءً يدويًّا يعتمدُ على حسنِ نيّةِ من يقرأُ صفحةَ الوقائع. القاعدةُ
    المُعلَنةُ في سجلِّ المخاطرِ نصًّا: «يُقاسُ بالواجهةِ لا بالعينِ: يُطلَبُ
    `jobs` ويُعَدُّ `steps`؛ فإن كان صفرًا يُعلَنُ الحكمُ **غيرَ مقروءٍ** ولا
    يُنسَبُ إلى الشجرة». وهذا الملفُّ هو تلك القاعدةُ منفَّذةً.

النطاق:
    قراءةُ حِملِ `GET /repos/{owner}/{repo}/actions/runs/{id}/jobs` وحدَه —
    حِملًا محفوظًا على القرصِ (`--from-json`) أو مطلوبًا حيًّا (`--run`).
    ولا تُصلِحُ هذه الأداةُ شيئًا ولا تُغيِّرُ إعدادَ حسابٍ ولا تُطلِقُ تشغيلًا:
    تُقيسُ فقط. وإصلاحُ حسابِ `Actions` (‏دقائقُ · حدُّ إنفاقٍ · طريقةُ دفعٍ)
    **بيدِ المالكِ وحدَه** بنصِّ `DISC-006` — فلا سلطانَ لأداةٍ على فاتورة.

المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-08-27

لماذا أداةٌ لا فقرةٌ في وثيقة
-----------------------------
`DISC-006` رصدَ أنَّ كلَّ وظائفِ CI تسقُطُ في ثانيتَينِ أو ثلاثٍ بلا تنفيذِ خطوةٍ
واحدةٍ (`steps=[]` و`runner_id=0`)، فصارَ `conclusion=failure` رقمًا **لا يحملُ
حكمًا**: لم يُسنَدْ للوظيفةِ عاملٌ قطُّ، فما سقطَ شيءٌ لتُقرأَ نتيجتُه. والخطرُ
المُقيَّدُ في `RK-011` ليس العطبَ نفسَه — بل **أن يُقرأَ حكمٌ غيرُ مقروءٍ حكمًا**،
فيُقالَ «CI أحمرُ» عن شجرةٍ لم تُفحَصْ، أو «أخضرُ» عن شجرةٍ لم تُختبَرْ.

وقد قِيسَ هذا العطبُ ثلاثَ مرّاتٍ بيدٍ (‏`W-049` · `W-050` · وهذا القيدُ)، وفي
كلِّ مرّةٍ بنصٍّ عارضٍ يُكتَبُ ثمَّ يُرمى. فالقياسُ الذي لا أداةَ له قياسٌ لا
يُعادُ، والقاعدةُ التي لا رمزَ خروجٍ لها قاعدةٌ **غيرُ منفَذة** — وهي عينُ
العلّةِ التي بُنِيَت لها بوّابتا `check_completion_ledger.py`
و`check_work_governance.py`. فصارَ للقاعدةِ أداةٌ تُشغَّلُ وتُختبَرُ وتُقيَّدُ.

الحدُّ المُعلَنُ ولا يُزعَمُ أكثرُ منه
------------------------------------
* تحكمُ هذه الأداةُ على **مقروئيّةِ** الحكمِ لا على **صوابِ** الشجرة. تشغيلٌ
  `READABLE` يعني أنَّ الخطواتِ نُفِّذَت فيُقرأُ `conclusion`، لا أنَّه أخضر.
* لا تُنشِئُ تشغيلًا ولا تُعيدُ محاولةً: قراءةٌ محضة.
* وضعُ `--run` يلزمُه توكنٌ في البيئةِ (`AMOS_GITHUB_TOKEN` أو `GITHUB_TOKEN`)
  ووصولٌ شبكيٌّ إلى `api.github.com`. فإن غابَ أحدُهما **تُعلِنُ الأداةُ عجزَها
  وتسقُط**، ولا تُرجِعُ حكمًا مُخترَعًا (‏القاعدة 12: حارسٌ يُتخطَّى بصمتٍ ليس
  حارسًا).
* وضعُ `--from-json` هو الوضعُ الذي يُعادُ به القياسُ بلا شبكةٍ ولا سرٍّ: يقرأُ
  الحِملَ كما ردَّته الواجهةُ حرفًا بحرفٍ. وبه تُختبَرُ الأداةُ نفسُها.

الاستعمالُ
---------
    python tools/governance/ci_verdict_readability.py --from-json jobs.json
    python tools/governance/ci_verdict_readability.py \
        --repo zoorooz/AMOS-Fedration --run 33021924845 --run 33021974329
    python tools/governance/ci_verdict_readability.py --from-json a.json \
        --json docs/audit/measurements/ci_verdict_readability.json

يخرجُ بصفرٍ إن كانَ حكمُ **كلِّ** تشغيلٍ مقروءًا، وبواحدٍ إن كانَ واحدٌ منها
غيرَ مقروءٍ أو مقروءًا جزئيًّا — لأنَّ الشكَّ في مقروئيّةِ الحكمِ يُعلَنُ ولا
يُبتلَع.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path

#: إصدارُ مخطَّطِ القياسِ المنشور — يُرفَعُ حينَ يتغيَّرُ شكلُ الحِملِ لا مضمونُه.
SCHEMA_VERSION = 1

#: ترويسةُ المادّةِ التاسعةِ داخلَ الحِملِ المنشور — تُسمّي مُولِّدَها نصًّا
#: لأنَّ `measurement_provenance.py` يُسقِطُ ما افترقَ فيه القيدُ والنصُّ.
IDENTITY_HEADER = (
    "الهدف: قياسُ مقروئيّةِ حكمِ CI بالخطواتِ المنفَّذةِ لا بالنتيجةِ المُعلَنةِ: "
    "لا يُقرَأُ `conclusion` حكمًا على الشجرةِ ما لم تُنفَّذْ خطوةٌ فعلًا "
    "(‏`RK-011` · `DISC-006`). النطاق: وقائعُ تشغيلاتِ GitHub Actions في هذا "
    "المستودعِ وحدَه — لا حكمَ على صحّةِ الشجرةِ ولا دعوى خُضرةٍ أو حُمرةٍ. "
    "المالك: tools/governance. تاريخ الإنشاء: 2026-08-27. تاريخ آخر تعديل: 2026-08-27. "
    "المُولِّد: tools/governance/ci_verdict_readability.py."
)

#: أسماءُ متغيّراتِ البيئةِ التي يُقرأُ منها التوكنُ، بالترتيب. ولا يُطبَعُ
#: أيٌّ منها ولا قيمتُه في أيِّ مُخرَجٍ — يُقرأُ ويُستَعمَلُ ويُنسى.
TOKEN_ENV_VARS = ("AMOS_GITHUB_TOKEN", "GITHUB_TOKEN")

API_ROOT = "https://api.github.com"

# ── تصنيفُ الوظيفةِ الواحدة ──────────────────────────────────────────────────
#
# `EXECUTED`       : خطوةٌ واحدةٌ على الأقلِّ لها `started_at` — فقد شُغِّلَ شيءٌ.
# `NOT_DISPATCHED` : لا خطوةَ أصلًا و`runner_id` صِفرٌ أو غائبٌ — لم يُسنَدْ عاملٌ.
# `SKIPPED`        : `conclusion == "skipped"` — غيابُ الخطواتِ هنا مشروعٌ فلا
#                    يُحسَبُ عطبًا ولا يُحسَبُ تنفيذًا؛ يُخرَجُ من المقام.
# `AMBIGUOUS`      : ما لا ينطبقُ عليه ما سبقَ — يُعلَنُ ولا يُصنَّفُ بالظنّ.
JOB_EXECUTED = "EXECUTED"
JOB_NOT_DISPATCHED = "NOT_DISPATCHED"
JOB_SKIPPED = "SKIPPED"
JOB_AMBIGUOUS = "AMBIGUOUS"

# ── حكمُ التشغيلِ الواحد ─────────────────────────────────────────────────────
RUN_READABLE = "READABLE"
RUN_UNREADABLE = "UNREADABLE"
RUN_PARTIAL = "PARTIALLY_READABLE"
RUN_UNDETERMINED = "UNDETERMINED"


class MeasurementRefused(RuntimeError):
    """تُرفَعُ حينَ يتعذَّرُ القياسُ — لا يُرجَعُ حكمٌ مُخترَعٌ بدلًا منه."""


@dataclass(frozen=True)
class JobReading:
    """قراءةُ وظيفةٍ واحدةٍ كما ردَّتها الواجهةُ، مصنَّفةً بمعيارٍ مُعلَن."""

    name: str
    job_id: int | None
    conclusion: str | None
    status: str | None
    runner_id: int | None
    steps_total: int
    steps_started: int
    classification: str


@dataclass
class RunReading:
    """حكمُ مقروئيّةِ تشغيلٍ واحدٍ وأرقامُه التي أنتجَته."""

    run_id: str
    jobs_total: int
    jobs_considered: int
    jobs_executed: int
    jobs_not_dispatched: int
    jobs_skipped: int
    jobs_ambiguous: int
    verdict: str
    #: هل يجوزُ الاحتجاجُ بـ`conclusion` حكمًا على الشجرة؟
    conclusion_quotable: bool
    jobs: list[JobReading] = field(default_factory=list)


def classify_job(job: dict[str, object]) -> JobReading:
    """تصنيفُ وظيفةٍ واحدةٍ بمعيارِ التنفيذِ لا بمعيارِ النتيجة."""
    steps = job.get("steps")
    if steps is None:
        steps_list: list[dict[str, object]] = []
    elif isinstance(steps, list):
        steps_list = [s for s in steps if isinstance(s, dict)]
    else:
        raise MeasurementRefused(
            f"حِملٌ غيرُ متوقَّعٍ: حقلُ steps في الوظيفةِ «{job.get('name')}» "
            f"من نوعٍ {type(steps).__name__} لا قائمةً — لا يُخمَّنُ حِملٌ لا يُفهَم."
        )

    started = [s for s in steps_list if s.get("started_at")]
    runner_id = job.get("runner_id")
    conclusion = job.get("conclusion")

    if conclusion == "skipped":
        classification = JOB_SKIPPED
    elif started:
        classification = JOB_EXECUTED
    elif not steps_list and (runner_id in (0, None)):
        classification = JOB_NOT_DISPATCHED
    else:
        classification = JOB_AMBIGUOUS

    return JobReading(
        name=str(job.get("name", "—")),
        job_id=job.get("id") if isinstance(job.get("id"), int) else None,
        conclusion=conclusion if isinstance(conclusion, str) else None,
        status=job.get("status") if isinstance(job.get("status"), str) else None,
        runner_id=runner_id if isinstance(runner_id, int) else None,
        steps_total=len(steps_list),
        steps_started=len(started),
        classification=classification,
    )


def read_run(run_id: str, payload: dict[str, object]) -> RunReading:
    """قراءةُ حِملِ `.../runs/{id}/jobs` وإصدارُ حكمِ مقروئيّتِه."""
    jobs = payload.get("jobs")
    if not isinstance(jobs, list):
        raise MeasurementRefused(
            f"حِملُ التشغيلِ {run_id} لا يحملُ قائمةَ `jobs` — "
            "أهو حِملُ الواجهةِ نفسُه أم ملفٌّ آخر؟ لا يُقاسُ ما لا يُعرَف."
        )

    readings = [classify_job(j) for j in jobs if isinstance(j, dict)]
    if len(readings) != len(jobs):
        raise MeasurementRefused(
            f"حِملُ التشغيلِ {run_id}: عنصرٌ في `jobs` ليس كائنًا — الحِملُ مشكوكٌ فيه."
        )

    executed = sum(r.classification == JOB_EXECUTED for r in readings)
    not_dispatched = sum(r.classification == JOB_NOT_DISPATCHED for r in readings)
    skipped = sum(r.classification == JOB_SKIPPED for r in readings)
    ambiguous = sum(r.classification == JOB_AMBIGUOUS for r in readings)
    considered = len(readings) - skipped

    if considered == 0:
        verdict = RUN_UNDETERMINED
    elif executed == considered:
        verdict = RUN_READABLE
    elif executed == 0:
        verdict = RUN_UNREADABLE
    else:
        verdict = RUN_PARTIAL

    return RunReading(
        run_id=str(run_id),
        jobs_total=len(readings),
        jobs_considered=considered,
        jobs_executed=executed,
        jobs_not_dispatched=not_dispatched,
        jobs_skipped=skipped,
        jobs_ambiguous=ambiguous,
        verdict=verdict,
        conclusion_quotable=verdict == RUN_READABLE,
        jobs=readings,
    )


def _token() -> str:
    """التوكنُ من البيئةِ حصرًا. لا سرَّ في شِفرةٍ ولا في مُخرَج."""
    for name in TOKEN_ENV_VARS:
        value = os.environ.get(name)
        if value:
            return value
    raise MeasurementRefused(
        "لا توكنَ في البيئةِ: يُقرأُ من "
        + " أو ".join(TOKEN_ENV_VARS)
        + " — ولا يُقاسُ حكمٌ بلا وصولٍ إلى الواجهة. "
          "وللقياسِ بلا شبكةٍ استُعمِلَ `--from-json` على حِملٍ محفوظ."
    )


def fetch_jobs(repo: str, run_id: str) -> dict[str, object]:
    """طلبُ حِملِ الوظائفِ حيًّا. يسقُطُ مُعلِنًا سببَه، ولا يُبدِلُه بحكمٍ."""
    if "/" not in repo:
        raise MeasurementRefused(f"`--repo` يُكتَبُ `owner/name` لا «{repo}».")
    url = f"{API_ROOT}/repos/{repo}/actions/runs/{run_id}/jobs?per_page=100"
    request = urllib.request.Request(  # noqa: S310 — عنوانٌ ثابتُ المخطَّطِ أعلاه
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {_token()}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "amos-ci-verdict-readability",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310
            body = response.read()
    except (urllib.error.URLError, TimeoutError) as exc:
        raise MeasurementRefused(
            f"تعذَّرَ الوصولُ إلى الواجهةِ للتشغيلِ {run_id}: {exc} — "
            "يُعلَنُ العجزُ ولا يُقالُ «الحكمُ مقروءٌ» ولا «غيرُ مقروءٍ»."
        ) from exc
    return json.loads(body.decode("utf-8"))


def _load_payload(path: Path) -> tuple[str, dict[str, object]]:
    """قراءةُ حِملٍ محفوظٍ. معرِّفُ التشغيلِ من داخلِ الحِملِ أو من اسمِ الملفّ."""
    if not path.is_file():
        raise MeasurementRefused(
            f"{path}: لا حِملَ في هذا المسارِ — يُعلَنُ الغيابُ ولا يُتخطَّى بصمتٍ."
        )
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise MeasurementRefused(f"{path}: الحِملُ ليس كائنَ JSON.")
    jobs = payload.get("jobs")
    run_id = ""
    if isinstance(jobs, list):
        for job in jobs:
            if isinstance(job, dict) and job.get("run_id") is not None:
                run_id = str(job["run_id"])
                break
    return run_id or path.stem, payload


def measure(readings: list[RunReading], repo: str = "") -> dict[str, object]:
    """حِملُ القياسِ المنشورُ — أرقامُه هي التي يُعادُ بها الحكمُ.

    يحملُ هذا الحِملُ `measured_at` لأنَّ وضعَ نَسَبِه `declared`: لا يُعادُ
    قياسُه في بوّابةٍ (‏يلزمُه شبكةٌ وتوكنٌ)، فطزاجتُه تاريخٌ مُعلَنٌ
    لا بوّابةٌ — على سابقةِ `domain_truth_snapshot.json` في `W-025`.
    """
    return {
        "$comment": IDENTITY_HEADER,
        "schema_version": SCHEMA_VERSION,
        "measurement": "ci_verdict_readability",
        "repository": repo,
        "measured_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "measured_by": "tools/governance/ci_verdict_readability.py",
        "rule": (
            "لا يُقرأُ conclusion حكمًا إلّا إذا نُفِّذَت خطوةٌ فعلًا — "
            "RK-011 · DISC-006"
        ),
        "runs_total": len(readings),
        "runs_readable": sum(r.verdict == RUN_READABLE for r in readings),
        "runs_unreadable": sum(r.verdict == RUN_UNREADABLE for r in readings),
        "runs_partially_readable": sum(r.verdict == RUN_PARTIAL for r in readings),
        "runs_undetermined": sum(r.verdict == RUN_UNDETERMINED for r in readings),
        "runs": [asdict(r) for r in readings],
    }


def render(readings: list[RunReading]) -> str:
    """تقريرٌ بشريٌّ قصيرٌ — الأرقامُ نفسُها التي في الحِمل."""
    lines: list[str] = ["[CI VERDICT] مقروئيّةُ الحكمِ تُقاسُ بالخطواتِ لا بالنتيجة"]
    for r in readings:
        lines.append(
            f"  تشغيلٌ {r.run_id}: {r.verdict} · "
            f"نُفِّذَت {r.jobs_executed}/{r.jobs_considered} وظيفةً "
            f"(لم يُسنَدْ عاملٌ لـ{r.jobs_not_dispatched} · "
            f"مُتخطًّى {r.jobs_skipped} · مشكوكٌ {r.jobs_ambiguous})"
        )
        if r.verdict == RUN_UNREADABLE:
            lines.append(
                "    ⇒ لا يُحتَجُّ بـ`conclusion` هنا حكمًا على الشجرةِ: "
                "لم تُنفَّذْ خطوةٌ واحدةٌ، فالحكمُ غيرُ مقروءٍ ولا يُنسَبُ إليها."
            )
        elif r.verdict == RUN_PARTIAL:
            lines.append(
                "    ⇒ حكمٌ مقروءٌ **جزئيًّا** فلا يُقرأُ حكمًا على التشغيلِ كلِّه: "
                f"{r.jobs_not_dispatched + r.jobs_ambiguous} وظيفةً لم يُقرأْ لها "
                "سجلُّ خطوةٍ، ونتيجةُ التشغيلِ مجموعُ وظائفِه."
            )
        elif r.verdict == RUN_UNDETERMINED:
            lines.append(
                "    ⇒ لا وظيفةَ تُقاسُ في هذا التشغيلِ (‏كلُّها مُتخطًّى) — "
                "لا يُقالُ مقروءٌ ولا غيرُ مقروءٍ."
            )
    unreadable = [r for r in readings if not r.conclusion_quotable]
    if unreadable:
        lines.append(
            f"[CI VERDICT] ✗ {len(unreadable)} من {len(readings)} تشغيلًا حكمُه غيرُ "
            "مقروءٍ — العطبُ في بنيةِ التشغيلِ لا في الشجرةِ (DISC-006 · RK-011)، "
            "وإصلاحُه بيدِ المالكِ في حسابِ Actions."
        )
    else:
        lines.append(
            f"[CI VERDICT] ✓ كلُّ التشغيلاتِ ({len(readings)}) نُفِّذَت خطواتُها — "
            "فـ`conclusion` يُقرأُ حكمًا."
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="مقروئيّةُ حكمِ CI: تُعَدُّ الخطواتُ المنفَّذةُ لا النتيجةُ المُعلَنة."
    )
    parser.add_argument(
        "--repo",
        default="",
        help="owner/name — يلزمُ `--run`، ويُقَيَّدُ في الحِملِ المنشورِ مع `--from-json`",
    )
    parser.add_argument(
        "--run", action="append", default=[], help="معرِّفُ تشغيلٍ يُطلَبُ حيًّا (يُعاد)"
    )
    parser.add_argument(
        "--from-json",
        action="append",
        default=[],
        help="حِملُ `.../jobs` محفوظًا على القرصِ (يُعاد) — قياسٌ بلا شبكةٍ ولا سرّ",
    )
    parser.add_argument("--json", default="", help="مسارُ كتابةِ حِملِ القياس")
    args = parser.parse_args(argv)

    if not args.run and not args.from_json:
        parser.error("لا مُدخَلَ: يلزمُ `--run` أو `--from-json`.")
    if args.run and not args.repo:
        parser.error("`--run` يلزمُه `--repo owner/name`.")

    readings: list[RunReading] = []
    try:
        for path in args.from_json:
            run_id, payload = _load_payload(Path(path))
            readings.append(read_run(run_id, payload))
        for run_id in args.run:
            readings.append(read_run(run_id, fetch_jobs(args.repo, run_id)))
    except MeasurementRefused as exc:
        print(f"[CI VERDICT] ✗ القياسُ مرفوضٌ: {exc}", file=sys.stderr)
        return 2

    print(render(readings))

    if args.json:
        out = Path(args.json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(measure(readings, args.repo), ensure_ascii=False, indent=2)
            + "\n",
            encoding="utf-8",
        )
        print(f"[CI VERDICT] كُتبت: {out}")

    return 0 if all(r.conclusion_quotable for r in readings) else 1


if __name__ == "__main__":
    sys.exit(main())
