"""الهدف: حرسُ مِسبارِ بصماتِ التاريخِ في `tools/audit/final_audit.py` (W-052).

المالك · Owner: — (غيرُ معيَّن) · تُسنَدُ إلى نطاقِ `audit-truth`.
النطاق: القسمُ السادسُ وحدَه من `final_audit.py` — استخراجُ البصماتِ من الوثيقةِ،
وقراءةُ السجلِّ، والحكمُ بالبادئةِ، ورفضُ القياسِ حينَ لا سجلَّ يُحكَمُ به.

لماذا هذا الحرس
---------------
قِيسَ في W-052 أنَّ المِسبارَ كانَ يكذبُ بثلاثةِ أوجهٍ (نافذةُ 400 · طولُ الاختصارِ
`%h` · قاعدةُ السبعةِ محارفَ بالضبط)، وأنَّ الوجهَ الرابعَ — سجلٌّ غائبٌ أو مبتورٌ —
كانَ يُنتِجُ **قائمةً فارغةً** تُقرَأُ شهادةَ براءةٍ. والإصلاحُ بلا حرسٍ يرتدُّ في أوّلِ
تحريرٍ، فهذه الفحوصُ تُشغِّلُ الأداةَ **على مستودعاتِ git حقيقيّةٍ مؤقّتةٍ** تُبنى
في الفحصِ نفسِه: لا شبكةَ، ولا اعتمادَ على تاريخِ هذا المستودعِ، ولا لمسَ شجرتِه.

وحدُّ صدقِ هذا الحرس: يُثبِتُ أنَّ الحكمَ على بصمةٍ يتبعُ السجلَّ الحقيقيَّ في كلِّ
الحالاتِ المقيسةِ أعلاه، **ولا** يُثبِتُ أنَّ كلَّ بصمةٍ في الوثيقةِ تدلُّ على العملِ
الذي تُنسَبُ إليه — ذاك حكمٌ على معنًى لا تقيسُه أداة.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root  # noqa: E402

ROOT = discover_repo_root(__file__)
TOOL = ROOT / "tools/audit/final_audit.py"
SOURCE = TOOL.read_text(encoding="utf-8")

# نافذةُ القياسِ: القسمُ السادسُ وحدَه — لا يُقرَأُ الملفُّ كلُّه كي لا يخضرَّ الفحصُ
# بذكرِ الرمزِ في موضعٍ آخر.
SECTION_SIX = SOURCE.split("# 6)", 1)[-1].split("# 7)", 1)[0]


def _code_only(text: str) -> str:
    """شِفرةُ القسمِ بلا شرحٍ ولا سلسلةِ توثيق.

    الحكمُ على الشرحِ خطأُ قياسٍ: الشرحُ هنا **يذكرُ** القاعدةَ القديمةَ (`-n 400`)
    ليُبيِّنَ ما أُصلِحَ، فقياسُ النصِّ كلِّه يجعلُ التوثيقَ الصادقَ مخالفةً.
    """
    stripped = re.sub(r'""".*?"""', "", text, flags=re.DOTALL)
    return "\n".join(
        line for line in stripped.splitlines() if not line.lstrip().startswith("#")
    )


SECTION_SIX_CODE = _code_only(SECTION_SIX)


# ── ١ · عقدُ المصدر: ما لا يجوزُ أن يرتدَّ ────────────────────────────────────


def test_tool_exists_and_declares_its_purpose() -> None:
    assert TOOL.is_file(), "الأداةُ المحكومُ عليها غيرُ موجودة"
    assert "الهدف:" in SOURCE.splitlines()[0]


def test_history_window_is_not_truncated_by_a_number() -> None:
    """`-n 400` أو أيُّ عددٍ: نافذةٌ مقطوعةٌ تُؤجِّلُ الكذبَ ولا تمنعُه."""
    assert '"-n"' not in SECTION_SIX_CODE, "عادت نافذةٌ مقطوعةٌ إلى قراءةِ السجلّ"
    assert not re.search(r"-n\s*\d", SECTION_SIX_CODE)
    assert "--max-count" not in SECTION_SIX_CODE
    # والشرحُ يبقى ذاكرًا للقاعدةِ المرفوعة؛ فحذفُ التاريخِ ليس إصلاحًا.
    assert "-n 400" in SECTION_SIX, "أُزيلَ إعلانُ ما كانَ عليه الحكمُ قبلَ W-052"


def test_history_is_read_by_full_hash_not_abbreviation() -> None:
    """`%h` طولُه متغيّرٌ بنموِّ المستودعِ، فالمطابقةُ به عقدٌ غيرُ مضمون."""
    assert "--format=%H" in SECTION_SIX_CODE
    assert "--format=%h" not in SECTION_SIX_CODE


def test_doc_extraction_accepts_seven_to_forty_hex_chars() -> None:
    assert "[0-9a-f]{7,40}" in SECTION_SIX_CODE
    assert "[0-9a-f]{7}`" not in SECTION_SIX_CODE


def test_judgement_is_by_prefix_not_string_equality() -> None:
    assert "startswith" in SECTION_SIX_CODE
    assert "h not in log" not in SECTION_SIX_CODE


def test_shallow_clone_is_detected_before_judging() -> None:
    assert "--is-shallow-repository" in SECTION_SIX_CODE


def test_every_git_call_in_the_probe_reads_its_return_code() -> None:
    """أمرٌ لا يُقرَأُ رمزُ خروجِه هو ابتلاعٌ صامتٌ (القاعدةُ 2 · W-027)."""
    assert SECTION_SIX_CODE.count("subprocess.run") == 2
    assert SECTION_SIX_CODE.count("returncode != 0") == 2


def test_refusal_is_declared_and_exits_with_two() -> None:
    assert "REFUSED" in SOURCE
    assert "SystemExit(2)" in SOURCE
    assert "file=sys.stderr" in SOURCE


# ── ٢ · قياسٌ حيٌّ على مستودعاتِ git مؤقّتة ──────────────────────────────────


def _git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    done = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    assert done.returncode == 0, f"git {' '.join(args)} سقطَ: {done.stderr}"
    return done


def _plant(
    tmp: Path,
    *,
    commits: int,
    hashes_doc: list[str] | None = None,
    commit_doc: bool = True,
) -> Path:
    """يبني مستودعًا حقيقيًّا بالعددِ المطلوبِ من الالتزاماتِ، ويُعيدُ جذرَه.

    الشجرةُ تحملُ ما تقرأُه الأداةُ فقط (المُدخَلاتُ التي تلمسُها الأقسامُ 1…9)،
    فالفحصُ يقيسُ القسمَ السادسَ ولا يُعيدُ بناءَ المستودعِ كلِّه.
    """
    root = tmp / "repo"
    (root / "docs/audit/measurements").mkdir(parents=True)
    (root / "docs/audit/evidence").mkdir(parents=True)
    (root / "tools/audit").mkdir(parents=True)
    (root / "tools/governance").mkdir(parents=True)

    inv = {
        "summary": {
            "non_sovereign_write_operations": 0,
            "sovereign_write_operations": 0,
            "closed_legacy_paths": 0,
            "public_write_operations": 0,
            "write_sites_total": 0,
        },
        "sites": [],
    }
    (root / "docs/audit/measurements/write_inventory_p13.json").write_text(
        json.dumps(inv), encoding="utf-8"
    )
    (root / "docs/audit/evidence/evidence_registry.jsonl").write_text("", encoding="utf-8")
    (root / "docs/audit/SOVEREIGN_DECISION_REGISTER.md").write_text(
        "## Q-1\n", encoding="utf-8"
    )
    # الأداةُ نفسُها تُنسَخُ كما هي — الحكمُ على شِفرةِ الإنتاجِ لا على نسخةٍ ألطف.
    (root / "tools/audit/final_audit.py").write_text(SOURCE, encoding="utf-8")

    # الأقسامُ 4 و 5 و 8 تقرأُ ملفّاتٍ مُسمَّاةً بأسمائِها في الأداةِ نفسِها،
    # فتُقرَأُ قائماتُها من مصدرِها ولا تُكتَبُ مرّةً ثانيةً هنا: نسخةٌ مكرّرةٌ
    # تتقادمُ بلا أن تُعلِنَ.
    for match in re.findall(r'"(federal/[^"]+\.py)"', SOURCE):
        target = root / match
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# الهدف: مدخَلٌ مؤقّتٌ للحرس.\n", encoding="utf-8")
    for match in re.findall(r'"(docs/audit/(?:measurements|evidence)/[^"]+)"', SOURCE):
        target = root / match
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            target.write_text("{}\n", encoding="utf-8")
    for name in (
        "SOVEREIGN_MIGRATION_PROGRAM.md", "SOVEREIGN_DECISION_REGISTER.md",
        "MIGRATION_DEBT_INVENTORY.md", "STATE_RUNTIME_MIGRATION_ANALYSIS.md",
        "AGENT_IDENTITY_MIGRATION_ANALYSIS.md", "TREASURY_MIGRATION_ANALYSIS.md",
        "JUDICIARY_LEGISLATIVE_MIGRATION_ANALYSIS.md",
        "GOVERNANCE_NESTING_MIGRATION_ANALYSIS.md",
        "ROYAL_SYSTEM_LIFE_MIGRATION_ANALYSIS.md",
        "REMAINING_SURFACES_INVENTORY.md", "STAGE_2B_HANDOFF.md",
    ):
        path = root / "docs/audit" / name
        if not path.exists():
            path.write_text(f"# {name}\n", encoding="utf-8")
    (root / "docs/audit/measurements/README.md").write_text("# قياسات\n", encoding="utf-8")
    (root / "docs/audit/evidence/README.md").write_text("# أدلّة\n", encoding="utf-8")
    for tool in re.findall(r'"(tools/[^"]+\.py)"', SOURCE):
        target = root / tool
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            target.write_text("# الهدف: مدخَلٌ مؤقّتٌ للحرس.\n", encoding="utf-8")

    _git(root, "init", "-q", "-b", "main")
    _git(root, "config", "user.email", "guard@example.invalid")
    _git(root, "config", "user.name", "W-052 Guard")

    shas: list[str] = []
    for i in range(commits):
        (root / "docs/audit/step.txt").write_text(f"{i}\n", encoding="utf-8")
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", f"c{i}")
        shas.append(_git(root, "rev-parse", "HEAD").stdout.strip())

    cited = hashes_doc if hashes_doc is not None else []
    body = "# برنامج\n\n" + "\n".join(f"| خطوة | `{h}` |" for h in cited) + "\n"
    (root / "docs/audit/SOVEREIGN_MIGRATION_PROGRAM.md").write_text(body, encoding="utf-8")
    if commit_doc:
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", "doc")
        shas.append(_git(root, "rev-parse", "HEAD").stdout.strip())
    # خارجَ الشجرةِ المحكومِ عليها: ملفُّ مساعدةٍ داخلَها يُلوّثُ `git status`.
    (root.parent / "shas.json").write_text(json.dumps(shas), encoding="utf-8")
    return root


def _run(root: Path) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run(
        [sys.executable, "tools/audit/final_audit.py"],
        cwd=root, capture_output=True, text=True, env=env,
    )


def _payload(done: subprocess.CompletedProcess[str]) -> dict[str, object]:
    assert done.returncode == 0, f"الأداةُ سقطَت: {done.stderr}"
    return json.loads(done.stdout)


@pytest.fixture(scope="module")
def deep_repo(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """مستودعٌ بـ405 التزامٍ — أوّلُ عمقٍ تكذبُ عندَه نافذةُ 400 القديمة."""
    tmp = tmp_path_factory.mktemp("w052-deep")
    return _plant(tmp, commits=405)


def _shas(root: Path) -> list[str]:
    return json.loads((root.parent / "shas.json").read_text(encoding="utf-8"))


def test_a_hash_older_than_four_hundred_commits_is_found(deep_repo: Path) -> None:
    """البصمةُ الأولى على عمقِ 404: النافذةُ القديمةُ كانت تُنكِرُها."""
    oldest = _shas(deep_repo)[0]
    doc = (deep_repo / "docs/audit/SOVEREIGN_MIGRATION_PROGRAM.md")
    doc.write_text(f"# برنامج\n\n| P0 | `{oldest[:7]}` |\n", encoding="utf-8")
    payload = _payload(_run(deep_repo))
    assert payload["hashes_in_doc"] == [oldest[:7]]
    assert payload["hashes_not_in_history"] == []


def test_the_old_window_would_have_lied_on_the_same_repository(deep_repo: Path) -> None:
    """القياسُ المضادُّ: القاعدةُ القديمةُ تُنفَّذُ هنا فتُنكِرُ بصمةً موجودة.

    بلا هذا الفحصِ يبقى الفحصُ السابقُ دعوى: قد يمرُّ لأنَّ العمقَ لم يُبلَغْ.
    """
    oldest = _shas(deep_repo)[0][:7]
    old_window = subprocess.run(
        ["git", "log", "--format=%h", "-n", "400"],
        cwd=deep_repo, capture_output=True, text=True,
    ).stdout.split()
    assert oldest not in old_window, "لم يُبلَغِ العمقُ الذي تكذبُ عندَه النافذة"


def test_a_fabricated_hash_is_still_reported_missing(deep_repo: Path) -> None:
    """الإصلاحُ لا يُخضِّرُ الحكمَ: بصمةٌ ملفَّقةٌ تبقى مُعلَنةً مفقودة."""
    doc = (deep_repo / "docs/audit/SOVEREIGN_MIGRATION_PROGRAM.md")
    doc.write_text("# برنامج\n\n| X | `0badbad` |\n", encoding="utf-8")
    payload = _payload(_run(deep_repo))
    assert payload["hashes_not_in_history"] == ["0badbad"]


def test_a_forty_char_hash_in_the_doc_is_measured_not_skipped(deep_repo: Path) -> None:
    """قاعدةُ السبعةِ بالضبطِ كانت تتخطّى البصمةَ التامّةَ فلا تُفحَصُ أصلًا."""
    head = _shas(deep_repo)[-1]
    doc = (deep_repo / "docs/audit/SOVEREIGN_MIGRATION_PROGRAM.md")
    doc.write_text(f"# برنامج\n\n| HEAD | `{head}` |\n", encoding="utf-8")
    payload = _payload(_run(deep_repo))
    assert payload["hashes_in_doc"] == [head], "البصمةُ التامّةُ خارجَ القياس"
    assert payload["hashes_not_in_history"] == []
    assert not re.findall(r"`([0-9a-f]{7})`", f"`{head}`"), \
        "القاعدةُ القديمةُ كانت تُهمِلُ هذه البصمةَ فعلًا"


def test_a_forty_char_fabrication_is_reported_missing(deep_repo: Path) -> None:
    fake = "0" * 40
    doc = (deep_repo / "docs/audit/SOVEREIGN_MIGRATION_PROGRAM.md")
    doc.write_text(f"# برنامج\n\n| X | `{fake}` |\n", encoding="utf-8")
    payload = _payload(_run(deep_repo))
    assert payload["hashes_not_in_history"] == [fake]


def test_prefix_judgement_survives_a_longer_abbreviation(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    """`core.abbrev=12`: المطابقةُ النصّيّةُ التامّةُ كانت تُنكِرُ كلَّ بصمة."""
    root = _plant(tmp_path_factory.mktemp("w052-abbrev"), commits=3)
    _git(root, "config", "core.abbrev", "12")
    head = _shas(root)[-1]
    (root / "docs/audit/SOVEREIGN_MIGRATION_PROGRAM.md").write_text(
        f"# برنامج\n\n| HEAD | `{head[:7]}` |\n", encoding="utf-8"
    )
    payload = _payload(_run(root))
    assert payload["hashes_not_in_history"] == []

    abbrev = subprocess.run(
        ["git", "log", "--format=%h", "-n", "400"],
        cwd=root, capture_output=True, text=True,
    ).stdout.split()
    assert all(len(a) >= 12 for a in abbrev), "لم يتغيّرْ طولُ الاختصار"
    assert head[:7] not in abbrev, "القاعدةُ القديمةُ كانت تُنكِرُ بصمةً موجودة"


# ── ٣ · الرفضُ: ما لا سجلَّ له لا يُحكَمُ فيه ────────────────────────────────


def test_a_shallow_clone_is_refused_not_declared_clean(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    """الاستنساخُ الضحلُ كانَ يُنتِجُ «لا بصمةَ مفقودةً» بلا قياس."""
    tmp = tmp_path_factory.mktemp("w052-shallow")
    origin = _plant(tmp, commits=5)
    head = _shas(origin)[-1]
    shallow = tmp / "shallow"
    subprocess.run(
        ["git", "clone", "-q", "--depth", "1", f"file://{origin}", str(shallow)],
        capture_output=True, text=True, check=True,
    )
    assert (shallow / ".git/shallow").exists(), "الاستنساخُ لم يكنْ ضحلًا"
    assert head  # البصمةُ مقروءةٌ من الأصلِ لا من الضحل

    done = _run(shallow)
    assert done.returncode == 2, f"لم يُرفَضْ: {done.returncode} · {done.stdout[:200]}"
    assert "REFUSED" in done.stderr
    assert "مبتورٌ" in done.stderr
    assert done.stdout.strip() == "", "طُبِعَ قياسٌ لم يُقَسْ"


def test_a_tree_without_git_is_refused(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    """شجرةٌ بلا سجلٍّ: الغيابُ يُعلَنُ ولا يُقرَأُ براءةً."""
    tmp = tmp_path_factory.mktemp("w052-nogit")
    root = _plant(tmp, commits=2)
    (root / "docs/audit/SOVEREIGN_MIGRATION_PROGRAM.md").write_text(
        "# برنامج\n\n| X | `0badbad` |\n", encoding="utf-8"
    )
    subprocess.run(["rm", "-rf", str(root / ".git")], check=True)
    env = dict(os.environ, PYTHONIOENCODING="utf-8", GIT_CEILING_DIRECTORIES=str(tmp))
    done = subprocess.run(
        [sys.executable, "tools/audit/final_audit.py"],
        cwd=root, capture_output=True, text=True, env=env,
    )
    assert done.returncode == 2, f"لم يُرفَضْ: {done.returncode} · {done.stdout[:200]}"
    assert "REFUSED" in done.stderr
    assert done.stdout.strip() == ""


def test_a_repository_without_a_single_commit_is_refused(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    """مستودعٌ بلا التزامٍ: يُقاسُ أنَّ `git log` هو من يرفضُ، فلا يُزادُ حرسٌ زينة.

    الشرحُ في `final_audit.py` يدّعي أنَّ فرعَ «سجلٍّ فارغٍ» لا يُبلَغُ؛
    والدعوى بلا قياسٍ وثيقةٌ لا حرسٌ — فهذا قياسُها.
    """
    tmp = tmp_path_factory.mktemp("w052-empty")
    root = _plant(tmp, commits=0, commit_doc=False)
    log = subprocess.run(
        ["git", "log", "--format=%H"], cwd=root, capture_output=True, text=True
    )
    assert log.returncode != 0, "لو نجحَ `git log` هنا للزِمَ حرسُ سجلٍّ فارغٍ"
    done = _run(root)
    assert done.returncode == 2, f"لم يُرفَضْ: {done.returncode} · {done.stdout[:200]}"
    assert "REFUSED" in done.stderr
    assert done.stdout.strip() == ""


def test_refusal_message_names_the_remedy(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    """رسالةُ رفضٍ لا تدلُّ على العلاجِ تُترَكُ فتُتجاوَز."""
    tmp = tmp_path_factory.mktemp("w052-remedy")
    origin = _plant(tmp, commits=3)
    shallow = tmp / "s"
    subprocess.run(
        ["git", "clone", "-q", "--depth", "1", f"file://{origin}", str(shallow)],
        capture_output=True, text=True, check=True,
    )
    done = _run(shallow)
    assert "fetch-depth: 0" in done.stderr


# ── ٤ · بقيّةُ القياساتِ لم تُمَسّ ────────────────────────────────────────────


def test_the_payload_key_set_did_not_change(deep_repo: Path) -> None:
    """عقدُ المُخرَجِ ثابتٌ: أُصلِحَ حكمٌ ولم يُزَدْ حقلٌ ولا حُذِف.

    الرقمُ المُعلَنُ في ترويسةِ المُخرَجِ وفي `measurements/README.md` هو «21 قياسًا»،
    فزيادةُ مفتاحٍ هنا تُكذِّبُ وثيقتَينِ في مسارَينِ لا يملكُهما هذا البند.
    """
    payload = _payload(_run(deep_repo))
    assert set(payload) == {
        "$comment", "debt_summary_field", "debt_recount", "sovereign",
        "closed_legacy", "public", "total_sites", "program_mentions_168",
        "program_placeholders", "program_todo_markers", "questions_headed",
        "questions_count", "questions_missing_1_to_max", "missing_docs",
        "missing_tools", "hashes_in_doc", "hashes_not_in_history",
        "evidence_entries", "evidence_chain_consistent",
        "bypass_params_in_migrated", "closed_legacy_functions",
        "sovereign_sites",
    }


def test_the_tool_still_measures_and_does_not_write(deep_repo: Path) -> None:
    """«يقيسُ ولا يُصلِحُ»: لا أثرَ في الشجرةِ بعدَ التشغيل."""
    before = _git(deep_repo, "status", "--porcelain").stdout
    _payload(_run(deep_repo))
    after = _git(deep_repo, "status", "--porcelain").stdout
    assert before == after, "الأداةُ كتبَت في الشجرةِ التي تحكمُ عليها"
