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

    [إضافةٌ مؤرَّخةٌ (W-769 · WI-077 · DISC-150 · قرارُ المالكِ Q-89 · 2026-11-01)]:
    عقدتانِ احمرّتا في CI (#234 بـ`OPEN_RECORD_WITHOUT_ANCHOR` و#235 بمصفوفةٍ متقادمةٍ)
    قبلَهما الحرسُ السبعةُ محلّيًّا (مسبارُ W-768). فأُضيفَت بعدَ السبعِ خطواتُ كلِّ
    وظيفةِ CI لم تكنْ تُشغَّلُ هنا (8–33)، ومنها فحصا المِرساةِ (8) والطزاجةِ (9)
    وruff على المستودعِ كلِّه (29 · 32). والخطوةُ 32 **حكمٌ جديدٌ أشدُّ من CI**
    بنصِّ القرار: `ruff format --check .` بسقفِ قائمةٍ اسميّةٍ (`ruff_format_debt.txt`)
    لا يزيد. ووظائفُ CI التي لا تُشغَّلُ هنا مُسمّاةٌ في `CI_PARITY_NAMED_DIFFERENCES`
    وتُطبَعُ في آخرِ كلِّ تشغيل. وخيارُ `--base` (الافتراضيُّ origin/main) لخطواتِ
    المدى. والسبعُ الأولى باقيةٌ بأوامرِها. التصميم: `docs/audit/DISC150_PREPUSH_PARITY_DESIGN.md`.

النطاق:
    بندُ WI-077 (توجيهُ المستشارِ 5 · G3 · DISC-098): الحرسُ السبعةُ المُلزِمةُ
    قبلَ الدفعِ — عقدتا 70441f8 و597d8bb بلغتا `main` حمراوَينِ لأنّ هذه
    البواباتِ لم تكنْ تُشغَّلُ معًا محليًّا قبلَ الدفعِ.

المالك:
    Perplexity Computer (WI-077 · بإذنِ المالكِ العامِّ وتوجيهِ المستشارِ 5).

تاريخ الإنشاء: 2026-10-16 (WI-077 · W-348)
تاريخ آخر تعديل: 2026-11-01 (W-769 · WI-077 — تكافؤُ CI: الخطواتُ 8–33 · DISC-150 · Q-89) · وقبله 2026-10-16 (W-387 · WI-083 — صيغةُ الوسيطِ والمطابقةُ التامّةُ لاسمِ المستودع) · ووقبله 2026-10-15 (WI-077 · المرّةُ الأولى)

المحتويات (ثلاثٌ وثلاثونَ خطوةً بترتيبٍ ثابتٍ — السبعُ الأولى كما كانت):
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
    8–9. مِرساةُ القيودِ المفتوحة (`open_record_accountability.py`) · طزاجةُ المصفوفة
       (`git diff --exit-code HEAD` على المصفوفتَين بعدَ الخطوة 5) — DISC-150.
    10–13. بقيّةُ Work Governance: `--self-check` · `--range <base>..HEAD` ·
       `guard_enforcement_closure.py` · `pre_push_merge_guard.py`.
    14–15. بقيّةُ Completion Ledger: `--self-check` · `--range <base>..HEAD`.
    16–18. بقيّةُ Truth Audit: جردُ الذاكرة · افتراقُ التسعير · نَسَبُ القياسات.
    19–27. Identity Law: البطاقاتُ والخواتمُ والتفسيرانِ وأسماءُ الجذرِ ومِسبارُ الوَثب
       و`pytest tests/governance/` كلُّه.
    28–32. Lint: إصدارُ ruff · `ruff check .` · ruff في الخدمات · سقفُ دَينِ التنسيق.
    33. Lockfile: الحزمُ الستُّ في `requirements.lock`.

الاستعمال:
    .venv/bin/python tools/dev/prepush_gate.py            # على الشجرةِ الحاضرةِ
    .venv/bin/python tools/dev/prepush_gate.py --repo-root /مسار   # لقياسِ شجرةٍ أخرى
    .venv/bin/python tools/dev/prepush_gate.py --base <ref>        # أساسُ خطواتِ المدى
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


#: الحرسُ السبعةُ الأولى باقيةٌ بأوامرِها (W-348). وما بعدَها خطواتُ وظائفِ CI التي
#: لم تكنْ تُشغَّلُ محلّيًّا (DISC-150 · قرارُ المالكِ Q-89 · W-769). الأمرُ في كلِّ
#: خطوةٍ يحملُ مُفسِّرَه (`PY` أو `git`)، فتُشغَّلُ `git diff` كغيرِها.
#: وكلُّ خطوةٍ تستدعي أدواتِ الشجرةِ المقيسةِ نفسِها (`repo_root/tools/…`) كما يفعلُ CI.
#: وكانت السبعُ تستدعي أدواتِ مستودعِ البوّابة، فكانَ `--repo-root` يقيسُ الخطوتَين 3 و4
#: على شجرةِ البوّابةِ لا الشجرةِ المطلوبة، لأنَّ أداتَيهما تجدانِ الجذرَ من موضعِ ملفِّهما
#: (W-769). وفي التشغيلِ العاديِّ الشجرتانِ واحدة، فلا يتغيّرُ أمرٌ.
def _gates(
    repo_root: Path, today_plus_4: str, base: str = "origin/main"
) -> list[tuple[str, list[str], Path | None]]:
    tools = repo_root / "tools" / "governance"
    services = repo_root / "federal" / "executive" / "services"
    me = str(Path(__file__).resolve())
    return [
        (
            "1· حوكمةُ العملِ (--commit HEAD)",
            [
                PY,
                str(tools / "check_work_governance.py"),
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
                PY,
                str(tools / "check_work_governance.py"),
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
            [PY, str(tools / "commit_timestamp_integrity.py"), "--check"],
            repo_root,
        ),
        (
            "4· سجلُّ الإكمالِ (--commit HEAD)",
            [PY, str(tools / "check_completion_ledger.py"), "--commit", "HEAD"],
            repo_root,
        ),
        (
            "5· راتشيتُ مصفوفةِ الحقيقةِ",
            [PY, str(tools / "truth_audit.py"), str(repo_root), "--ratchet"],
            repo_root,
        ),
        (
            "6· انحرافُ وثائقِ الحالةِ",
            [PY, str(tools / "state_document_drift.py"), "--root", str(repo_root)],
            repo_root,
        ),
        (
            "7· فحوصُ الهويةِ واتساقِ المراجعِ (test_w154 + قانونُ الهويةِ)",
            [
                PY,
                "-m",
                "pytest",
                "tests/governance/test_w154_reviewer_consistency.py",
                "tests/governance/test_identity_law.py",
                "-q",
            ],
            repo_root,
        ),
        # ── DISC-150 · Q-89: الفحصانِ المأمورُ بهما نصًّا ─────────────────────
        (
            "8· مِرساةُ القيودِ المفتوحةِ (open_record_accountability · Work Governance)",
            [PY, str(tools / "open_record_accountability.py")],
            repo_root,
        ),
        (
            "9· طزاجةُ مصفوفةِ الحقيقةِ (git diff بعدَ الخطوة 5 · Truth Audit)",
            [
                "git",
                "diff",
                "--exit-code",
                "HEAD",
                "--",
                "docs/audit/TRUTH_MATRIX.md",
                "docs/audit/truth_matrix.json",
            ],
            repo_root,
        ),
        # ── Work Governance (بقيّةُ خطواتِه) ───────────────────────────────────
        (
            "10· حوكمةُ العملِ (--self-check بلا تاريخٍ · كما في CI)",
            [PY, str(tools / "check_work_governance.py"), "--self-check"],
            repo_root,
        ),
        (
            f"11· حوكمةُ العملِ (--range {base}..HEAD)",
            [PY, str(tools / "check_work_governance.py"), "--range", f"{base}..HEAD"],
            repo_root,
        ),
        (
            "12· إغلاقُ إنفاذِ الحرسِ (guard_enforcement_closure)",
            [PY, str(tools / "guard_enforcement_closure.py")],
            repo_root,
        ),
        (
            "13· حرسُ إزاحةِ التزامِ الدمجِ (pre_push_merge_guard)",
            [
                PY,
                str(tools / "pre_push_merge_guard.py"),
                "--base-ref",
                base,
                "--head",
                "HEAD",
                "--exclude-ephemeral",
            ],
            repo_root,
        ),
        # ── Completion Ledger ─────────────────────────────────────────────────
        (
            "14· سجلُّ الإكمالِ (--self-check)",
            [PY, str(tools / "check_completion_ledger.py"), "--self-check"],
            repo_root,
        ),
        (
            f"15· سجلُّ الإكمالِ (--range {base}..HEAD)",
            [PY, str(tools / "check_completion_ledger.py"), "--range", f"{base}..HEAD"],
            repo_root,
        ),
        # ── Truth Audit (بقيّةُ خطواتِه) ───────────────────────────────────────
        (
            "16· جردُ مخازنِ الذاكرةِ المنشورُ (--check)",
            [PY, str(tools / "in_memory_inventory.py"), ".", "--check"],
            repo_root,
        ),
        (
            "17· افتراقُ التسعيرِ المنشورُ (--check)",
            [PY, str(tools / "pricing_divergence.py"), ".", "--check"],
            repo_root,
        ),
        (
            "18· نَسَبُ القياساتِ وطزاجتُها (--check --without-deps)",
            [
                PY,
                str(tools / "measurement_provenance.py"),
                ".",
                "--check",
                "--without-deps",
            ],
            repo_root,
        ),
        # ── Identity Law ──────────────────────────────────────────────────────
        (
            "19· بطاقاتُ الهويّةِ (check_repository_identity)",
            [PY, str(tools / "check_repository_identity.py"), "."],
            repo_root,
        ),
        (
            "20· بطاقاتُ المواطنينَ المستوردينَ (--check)",
            [PY, str(tools / "generate_identity_cards.py"), "--check"],
            repo_root,
        ),
        (
            "21· بطاقاتُ الأقاليمِ (--check)",
            [PY, str(tools / "write_domain_readmes.py"), "--check"],
            repo_root,
        ),
        (
            "22· الحقولُ المشتقّةُ مختومةٌ (--check)",
            [PY, str(tools / "stamp_readme_identity.py"), "--check"],
            repo_root,
        ),
        (
            "23· تفسيرا INT-001 وINT-002 قائمانِ والمدقّقُ يستندُ إليهما",
            [PY, me, "--internal", "int-files", "--repo-root", str(repo_root)],
            repo_root,
        ),
        (
            "24· الخاتمُ لا يكتبُ حقولَ الحكمِ",
            [PY, me, "--internal", "stamp-fields", "--repo-root", str(repo_root)],
            repo_root,
        ),
        (
            "25· لا اسمَ غريبًا في الجذرِ (check_root_file_names)",
            [PY, str(tools / "check_root_file_names.py"), "."],
            repo_root,
        ),
        (
            "26· مِسبارُ الوَثبِ (mutation_probe)",
            [PY, str(tools / "mutation_probe.py")],
            repo_root,
        ),
        (
            "27· اختباراتُ الحوكمةِ كلُّها (pytest tests/governance/ · ومنها الطزاجة)",
            [PY, "-m", "pytest", "tests/governance/", "-q"],
            repo_root,
        ),
        # ── Lint (ruff) ───────────────────────────────────────────────────────
        (
            f"28· إصدارُ ruff = {RUFF_VERSION} (المثبَّتُ في CI)",
            [PY, me, "--internal", "ruff-version", "--repo-root", str(repo_root)],
            repo_root,
        ),
        (
            "29· ruff check . (المستودعُ كلُّه)",
            [PY, "-m", "ruff", "check", "."],
            repo_root,
        ),
        (
            "30· ruff check src/ tests/ (الخدمات)",
            [PY, "-m", "ruff", "check", "src/", "tests/"],
            services,
        ),
        (
            "31· ruff format --check src/ tests/ (الخدمات)",
            [PY, "-m", "ruff", "format", "--check", "src/", "tests/"],
            services,
        ),
        (
            "32· ruff format --check . بسقفِ قائمةِ الدَّينِ (أشدُّ من CI)",
            [PY, me, "--internal", "format-debt", "--repo-root", str(repo_root)],
            repo_root,
        ),
        # ── Lockfile Consistency ──────────────────────────────────────────────
        (
            "33· الحزمُ الحرجةُ في requirements.lock",
            [PY, me, "--internal", "lockfile", "--repo-root", str(repo_root)],
            repo_root,
        ),
    ]


#: رسائلُ الفحوصِ الداخليّةِ بلا علامةِ «✓» عمدًا: مقامُ الخُضرةِ (DISC-053 · green_denominator_closure)
#: يُعِدُّ كلَّ «✓» تحتَ tools/، والسجلُّ المُعلَنُ 44 لا يُرفَعُ بيدِ المنفِّذ (W-769).
#: إصدارُ ruff المثبَّتُ في وظيفةِ Lint (`pip install ruff==0.6.9` في ci.yml).
RUFF_VERSION = "0.6.9"

#: قائمةُ دَينِ التنسيقِ الاسميّةُ: الملفّاتُ غيرُ المنسَّقةِ كما قِيسَت على `53bb0cc5`
#: (212 ملفًّا · W-768). تنقصُ ولا تزيد: الإضافةُ إليها رفعُ خطٍّ أساسٍ، وهو للمالك.
FORMAT_DEBT_PATH = Path(__file__).resolve().with_name("ruff_format_debt.txt")

#: الحزمُ التي تفحصُها وظيفةُ Lockfile Consistency في ci.yml.
LOCK_PACKAGES = (
    "fastapi",
    "uvicorn",
    "sqlalchemy",
    "anthropic",
    "structlog",
    "pydantic",
)

#: وظائفُ CI التي تُغطّيها خطواتٌ محلّيّة: معرِّفُ الوظيفةِ ← أرقامُ خطواتِها هنا.
CI_PARITY_COVERED: dict[str, tuple[int, ...]] = {
    "work-governance-gate": (1, 2, 6, 8, 10, 11, 12, 13, 27),
    "ledger-gate": (4, 14, 15, 27),
    "truth-audit": (5, 9, 16, 17, 18),
    "identity-check": (19, 20, 21, 22, 23, 24, 25, 26, 27),
    "lint": (28, 29, 30, 31),
    "lockfile-check": (33,),
}

#: وظائفُ CI التي لا تُشغَّلُ محلّيًّا، وسببُ كلٍّ منها. تُطبَعُ في آخرِ كلِّ تشغيل،
#: فخضرتُها تُقرأُ من CI وحدَه (DISC150_PREPUSH_PARITY_DESIGN.md § 7).
CI_PARITY_NAMED_DIFFERENCES: dict[str, str] = {
    "constitutional-kernel": "Constitutional Kernel: تغطيةُ فروعٍ ≥ 90% وسجلٌّ مؤقّت · نطاقُ K1",
    "sovereignty-kernel": "Sovereignty Kernel: تبعيّاتُ الخدماتِ وتغطيةٌ ≥ 90% · نطاقُ C3",
    "crown-root-of-trust": "Crown Root of Trust: تبعيّاتُ الخدماتِ وفحصُ تاريخِ git كلِّه",
    "smoke": "Smoke: اثنا عشرَ مجالًا بتبعيّاتِ الخدماتِ كاملة",
    "test": "Tests: حزمةُ الخدماتِ كاملةً (≈ 23 دقيقةً مقيسة)",
    "coverage": "Coverage: حزمةُ الخدماتِ كاملةً بتغطيةٍ ≥ 80%",
    "cross-system-suites": "Cross-System Suites: خادمُ PostgreSQL 17",
}


def _would_reformat(output: str) -> set[str]:
    """أسماءُ الملفّاتِ التي يقولُ ruff إنّها تحتاجُ تنسيقًا (`Would reformat: …`)."""
    prefix = "Would reformat: "
    return {
        line[len(prefix) :].strip()
        for line in output.splitlines()
        if line.startswith(prefix)
    }


def _format_debt_verdict(
    unformatted: set[str], debt: set[str]
) -> tuple[int, list[str]]:
    """الحكمُ: 0 إن كانَ كلُّ ملفٍّ غيرِ منسَّقٍ في قائمةِ الدَّين، وإلّا 1 بأسماءِ الزائد."""
    extra = sorted(unformatted - debt)
    return (1 if extra else 0), extra


def _read_debt(path: Path) -> set[str]:
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def _internal(check: str, repo_root: Path) -> int:
    """فحوصٌ لا أداةَ لها في المستودع، تُستدعى خطواتٍ بـ`--internal <الاسم>`."""
    if check == "int-files":
        interp = repo_root / "core" / "constitution" / "interpretations"
        needed = [
            interp / "INT-001-article-009-scope.md",
            interp / "INT-002-preamble-sealing.md",
        ]
        absent = [str(p.relative_to(repo_root)) for p in needed if not p.is_file()]
        checker = repo_root / "tools" / "governance" / "check_repository_identity.py"
        if absent:
            print(f"✗ تفسيرٌ غائب: {' · '.join(absent)}")
            return 1
        if "INT-001" not in checker.read_text(encoding="utf-8"):
            print("✗ المدقّقُ لا يستندُ إلى INT-001")
            return 1
        print("[PREPUSH] حُكمُ الفحص: التفسيرانِ قائمانِ والمدقّقُ يستندُ إلى INT-001.")
        return 0
    if check == "stamp-fields":
        stamper = repo_root / "tools" / "governance" / "stamp_readme_identity.py"
        text = stamper.read_text(encoding="utf-8")
        written = [f for f in ("## التعريف", "## النطاق", "## المالك") if f in text]
        if written:
            print(f"✗ الخاتمُ يكتبُ حقلَ حكم: {' · '.join(written)}")
            return 1
        print("[PREPUSH] حُكمُ الفحص: الخاتمُ يشتقُّ ولا يختلق.")
        return 0
    if check == "lockfile":
        lock = repo_root / "federal" / "executive" / "services" / "requirements.lock"
        names = {
            line.split("==", 1)[0].strip().lower()
            for line in lock.read_text(encoding="utf-8").splitlines()
            if "==" in line
        }
        missing = [p for p in LOCK_PACKAGES if p not in names]
        if missing:
            print(f"✗ MISSING في requirements.lock: {' · '.join(missing)}")
            return 1
        print(
            f"[PREPUSH] حُكمُ الفحص: الحزمُ الستُّ في requirements.lock: {' · '.join(LOCK_PACKAGES)}"
        )
        return 0
    if check == "ruff-version":
        result = subprocess.run(
            [PY, "-m", "ruff", "--version"], capture_output=True, text=True, check=False
        )
        found = (result.stdout or result.stderr).strip()
        if result.returncode != 0 or found.split()[-1:] != [RUFF_VERSION]:
            print(f"✗ ruff المطلوب {RUFF_VERSION} والموجود: {found or 'غيرُ مثبَّت'}")
            return 1
        print(f"[PREPUSH] حُكمُ الفحص: {found}")
        return 0
    if check == "format-debt":
        result = subprocess.run(
            [PY, "-m", "ruff", "format", "--check", "."],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=False,
        )
        out = (result.stdout or "") + (result.stderr or "")
        unformatted = _would_reformat(out)
        if result.returncode not in (0, 1) or (
            result.returncode == 1 and not unformatted
        ):
            print(out[-1500:])
            print("✗ ruff format لم يُنتِجْ قائمةً مقروءة")
            return 1
        debt = _read_debt(FORMAT_DEBT_PATH)
        code, extra = _format_debt_verdict(unformatted, debt)
        for name in extra:
            print(f"✗ غيرُ منسَّقٍ وليسَ في قائمةِ الدَّين: {name}")
        print(
            f"غيرُ المنسَّقِ الآن {len(unformatted)} · قائمةُ الدَّين {len(debt)} · "
            f"زائدٌ {len(extra)} · سُدِّدَ {len(debt - unformatted)}"
        )
        return code
    print(f"✗ فحصٌ داخليٌّ غيرُ معروف: {check}")
    return 2


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
    parser.add_argument(
        "--base",
        default="origin/main",
        help="أساسُ خطواتِ المدى (11 · 13 · 15) — الافتراضيُّ origin/main كما في CI",
    )
    parser.add_argument("--internal", default="", help=argparse.SUPPRESS)
    args = parser.parse_args()
    repo_root = (args.repo_root or REPO_ROOT).resolve()
    if args.internal:
        return _internal(args.internal, repo_root)
    today_plus_4 = (date.today() + timedelta(days=4)).isoformat()

    failures: list[str] = []
    print(f"[PREPUSH] الجذرُ المقيسُ: {repo_root} · الأساسُ: {args.base}")
    for name, cmd, cwd in _gates(repo_root, today_plus_4, args.base):
        print(f"\n[PREPUSH] ▶ {name}")
        result = subprocess.run(
            cmd,
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
    print("[PREPUSH] وظائفُ CI التي لا تُقاسُ هنا (خضرتُها من CI وحدَه):")
    for reason in CI_PARITY_NAMED_DIFFERENCES.values():
        print(f"[PREPUSH]   · {reason}")
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
