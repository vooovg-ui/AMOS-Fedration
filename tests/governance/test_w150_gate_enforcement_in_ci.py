#!/usr/bin/env python3
"""حارسُ دعوى الإنفاذِ: «بوّابةُ الحوكمةِ نافذةٌ» تُقاسُ ولا تُصدَّقُ (WI-051 · W-150).

الهدف:
    القرارُ `A-3` اعتُمِدَ `APPROVED` في 2026-09-07، وكتبَت § 16.5 من
    `docs/governance/work/THE_ROADMAP.md` أنَّ `work-governance-gate` صارت
    «نافذةً بوضعِ الإسقاطِ». وبقيَ `.github/workflows/ci.yml` يستدعي الفاحصَ
    بـ`--advisory` — أي **إبلاغًا** يُخرِجُ صفرًا مهما كانت المخالفةُ. فبقيَت
    الوثيقةُ تدَّعي إنفاذًا لا يقيسُه شيءٌ **أربعةً وعشرينَ ساعةً**، ولم يكشِفْه
    فحصٌ آليٌّ بل كشفَه **مجلسُ المراجعةِ المستقلُّ** (GPT 5.6 وGrok 4.6) بإجماعٍ
    في جولتِه الأولى على `WI-051`.

    ومراجعةٌ بشريّةٌ (أو نموذجيّةٌ) كشفَت عَطبًا مرّةً لا تضمنُ كشفَه مرّةً
    ثانيةً. فالدرسُ لا يُكتَبُ في سطرٍ يُقرأُ، بل يُنزَلُ حارسًا يُشغَّلُ:
    هذا الملفُّ. وهو يقيسُ **شيئَينِ لا واحدًا**:

    1. **الملفُّ يقولُ ما تقولُه الوثيقةُ** — لا `--advisory` في وظيفةِ
       بوّابةِ الحوكمةِ. وهذا يمنعُ عودةَ التناقضِ نصًّا.
    2. **والفاحصُ نفسُه يُسقِطُ فعلًا** — يُصطنَعُ في شجرةٍ مؤقتةٍ التزامٌ
       يمسُّ مسارًا لا يُعلِنُه بندٌ نشِطٌ، ويُقاسُ رمزُ الخروجِ. فلو صارَ
       الفاحصُ يُخرِجُ صفرًا على مخالفةٍ حقيقيّةٍ لكانَ رفعُ `--advisory`
       زينةً لا إنفاذًا.

    والثاني هو الأهمُّ: الأوّلُ يحرسُ **الاستدعاءَ**، والثاني يحرسُ **الأثرَ**.
النطاق:
    قراءةُ `.github/workflows/ci.yml` نصًّا (كتلةُ وظيفةِ الحوكمةِ وحدَها)،
    وتحميلُ `tools/governance/check_work_governance.py` وحدةً واستدعاءُ دوالِّها
    ببدائلَ مُركَّبةٍ. لا شبكةَ ولا قاعدةَ ولا سرَّ ولا حسابَ Actions، ولا يكتُبُ
    هذا الملفُّ بايتًا في شجرةٍ يحكمُ عليها.
المالك: tests/ — بتفويضٍ من المجلس التأسيسي · البند `WI-051` · القيد `W-150`
تاريخ الإنشاء: 2026-09-08
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

def _discover_root() -> Path:
    """جذرُ المستودعِ **بعلامةٍ لا بعُمقٍ مكتوبٍ** (‏`W-102` · حرسُ نسَبِ محلِّ القياسِ).

    `parents[2]` يصدُقُ ما دامَ الملفُّ في `tests/governance/`، ويكذِبُ صامتًا
    أوّلَ ما يُنقَلُ أو يُعادُ تنظيمُ المجلَّداتِ — فيُقاسُ مستودعٌ آخرُ ويُقرأُ
    الحكمُ صحيحًا. فالصعودُ هنا حتى `.git` أو `PROJECT_STATE.md`.
    """
    here = Path(__file__).resolve()
    for candidate in (here, *here.parents):
        if (candidate / ".git").exists() or (candidate / "PROJECT_STATE.md").is_file():
            return candidate
    raise RuntimeError(  # pragma: no cover - يمنعُ القياسَ ولا يُخمَّنُ عندَه
        "لم يُعرَفْ جذرُ المستودعِ بعلامةٍ (`.git` أو `PROJECT_STATE.md`) — "
        "والقياسُ يقِفُ ولا يُستأنَفُ بعُمقٍ مظنونٍ."
    )


REPO_ROOT = _discover_root()
CI_WORKFLOW = REPO_ROOT / ".github" / "workflows" / "ci.yml"
GATE = REPO_ROOT / "tools" / "governance" / "check_work_governance.py"

#: اسمُ الوظيفةِ التي تستدعي بوّابةَ الحوكمةِ في `ci.yml`.
GATE_JOB_KEY = "work-governance-gate"


def _gate_job_block() -> str:
    """نصُّ وظيفةِ بوّابةِ الحوكمةِ وحدَها — لا كلُّ الملفِّ.

    القياسُ يجبُ أن يكونَ على الوظيفةِ المعنيّةِ لا على الملفِّ كلِّه: وظيفةٌ
    أخرى قد تستدعي أداةً أخرى بـ`--advisory` لسببٍ مشروعٍ، فحُكمٌ على الملفِّ
    كلِّه يُسقِطُ ما لا ذنبَ له ويُعلِّمُ القارئَ أن يتجاهلَ الحارسَ.
    """
    text = CI_WORKFLOW.read_text(encoding="utf-8")
    start = text.find(f"\n  {GATE_JOB_KEY}:")
    assert start != -1, (
        f"وظيفةُ «{GATE_JOB_KEY}» غيرُ موجودةٍ في {CI_WORKFLOW.relative_to(REPO_ROOT)} — "
        "إمّا أُعيدَت تسميتُها فيلزمُ تحديثُ هذا الحارسِ، وإمّا حُذِفَت فالبوّابةُ "
        "لم تَعُدْ تُشغَّلُ أصلًا. وكلاهما يمنعُ القياسَ ويوجِبُ الوقوفَ."
    )
    # حدُّ الوظيفةِ: أوّلُ مفتاحِ وظيفةٍ تالٍ بمسافتَينِ بادئتَينِ.
    nxt = re.search(r"\n  [a-z0-9][a-z0-9\-_]*:\n", text[start + 1 :])
    end = (start + 1 + nxt.start()) if nxt else len(text)
    return text[start:end]


def test_ci_gate_job_does_not_run_the_governance_check_in_advisory_mode() -> None:
    """لا `--advisory` في وظيفةِ بوّابةِ الحوكمةِ — وإلّا فـ§ 16.5 تدّعي."""
    block = _gate_job_block()
    offenders = [
        line.strip()
        for line in block.splitlines()
        if "--advisory" in line and not line.lstrip().startswith("#")
    ]
    assert offenders == [], (
        "وظيفةُ بوّابةِ الحوكمةِ في `ci.yml` تستدعي الفاحصَ بـ`--advisory` — "
        "وهو وضعُ **الإبلاغِ** الذي يُخرِجُ صفرًا مهما كانت المخالفةُ، بينما "
        "`THE_ROADMAP.md § 16.5` الحدُّ 3 يقولُ إنَّ البوّابةَ **نافذةٌ بوضعِ "
        "الإسقاطِ** بعدَ اعتمادِ `A-3`. فإمّا يُرفَعُ `--advisory` وإمّا يُضيَّقُ "
        "نصُّ § 16.5 — ولا يُترَكُ الاثنانِ متناقضَينِ، فذاك عينُ العَطبِ الذي "
        f"أسقطَه المجلسُ المستقلُّ في `W-150`. الأسطرُ المخالفةُ: {offenders}"
    )


def test_ci_gate_job_actually_invokes_the_governance_check() -> None:
    """ورفعُ `--advisory` لا يُقرأُ إنفاذًا إن لم تَعُدِ البوّابةُ تُستدعى أصلًا."""
    block = _gate_job_block()
    assert "tools/governance/check_work_governance.py" in block, (
        "وظيفةُ بوّابةِ الحوكمةِ لا تستدعي `check_work_governance.py` — "
        "فـ«لا `--advisory` فيها» صارَ صادقًا بحذفِ البوّابةِ لا بإنفاذِها، "
        "وهذا أسوأُ من الإبلاغِ."
    )


def _load_gate_module():
    """تحميلُ البوّابةِ وحدةً — لا تُستدعى بعمليّةٍ في شجرةٍ مؤقتةٍ.

    البوّابةُ تحسِمُ جذرَ المستودعِ من **موضعِ ملفِّها** لا من مجلَّدِ العملِ، فلا
    تُوجَّهُ إلى شجرةٍ مصطنَعةٍ بتغييرِ `cwd`. وأوّلُ صياغةٍ لهذا الحارسِ حاولَت
    ذلك فمرَّت خضراءَ وهي لا تقيسُ شيئًا — وهذا نفسُه عَطبٌ يستحقُّ التسميةَ:
    **حارسٌ يظنُّ أنّه قاسَ وقد قاسَ المستودعَ الحقيقيَّ**. فالقياسُ هنا على
    الدالّةِ نفسِها وعلى ربطِ رمزِ الخروجِ، لا على عمليّةٍ في شجرةٍ.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location("_wg_gate_under_test", GATE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_gate_flags_a_changed_path_that_no_active_item_claims(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """مخالفةٌ حقيقيّةٌ تُقاسُ: مسارٌ تنفيذيٌّ مُغيَّرٌ لا يُعلِنُه بندٌ نشِطٌ."""
    gate = _load_gate_module()

    monkeypatch.setattr(gate, "changed_paths", lambda *_: ["core/never_claimed_by_any.py"])
    monkeypatch.setattr(gate, "ledger_diff", lambda *_: "")
    monkeypatch.setattr(gate, "base_items", lambda *_: None)

    items = [
        {
            "id": "WI-999",
            "status": "IN_PROGRESS",
            "paths": ["docs/some/other/place.md"],
            "ledger": "—",
        }
    ]
    violations = gate.check_change_set("commit", "HEAD", items)
    kinds = [v["kind"] for v in violations]
    assert "PATH_UNCLAIMED" in kinds, (
        "البوّابةُ لم تُسقِطْ مسارًا تنفيذيًّا مُغيَّرًا لا يُعلِنُه بندٌ نشِطٌ — "
        "فرفعُ `--advisory` من `ci.yml` زينةٌ لا إنفاذٌ، ودعوى § 16.5 بلا أثرٍ. "
        f"المخالفاتُ المقروءةُ: {kinds}"
    )


def test_governed_application_path_is_not_exempt_from_claiming() -> None:
    """والمخالفةُ أعلاه ليست مصادفةً: المسارُ التنفيذيُّ **يُشترَطُ له حجزٌ**."""
    gate = _load_gate_module()
    assert gate.requires_claim("core/never_claimed_by_any.py") is True
    # وسجلّاتُ الحوكمةِ معفاةٌ بنصِّ § 6 — يُقاسُ الطرفانِ فلا يُقرأُ الإعفاءُ سهوًا.
    assert gate.requires_claim("docs/governance/work/ACTIVE_WORK.md") is False


def test_advisory_flag_is_what_turns_a_failure_into_a_zero_exit() -> None:
    """ربطُ الرمزِ يُقاسُ: مع `--advisory` صفرٌ، وبدونِه غيرُ صفرٍ — للمخالفاتِ عينِها.

    وهذا هو **جوهرُ** العَطبِ الذي أسقطَه المجلسُ: لم يكنِ الخللُ في البوّابةِ
    ولا في الفاحصِ، بل في **راية استدعاءٍ واحدةٍ** تُحوِّلُ كلَّ مخالفةٍ إلى
    نجاحٍ صامتٍ بينما تقولُ الوثيقةُ «نافذةٌ بوضعِ الإسقاطِ».
    """
    gate = _load_gate_module()
    fake = [gate._v("PATH_UNCLAIMED", "مخالفةٌ مصطنَعةٌ لقياسِ ربطِ رمزِ الخروجِ")]

    class _Args:
        advisory = False

    def exit_code(violations: list[dict[str, str]], advisory: bool) -> int:
        # عينُ الفرعِ الأخيرِ في `main()`: مخالفاتٌ ⇒ 1، إلّا مع `--advisory` ⇒ 0.
        if not violations:
            return 0
        return 0 if advisory else 1

    assert exit_code(fake, advisory=True) == 0
    assert exit_code(fake, advisory=False) == 1
    assert _Args.advisory is False

    source = GATE.read_text(encoding="utf-8")
    assert "if args.advisory:" in source and "    return 1" in source, (
        "بنيةُ `main()` تغيَّرت — فربطُ رمزِ الخروجِ الذي يقيسُه هذا الحارسُ "
        "لم يَعُدْ هو المُنفَّذَ، ويلزمُ تحديثُ الحارسِ قبلَ الوثوقِ به."
    )
