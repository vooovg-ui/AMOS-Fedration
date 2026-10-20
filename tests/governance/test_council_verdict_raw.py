"""فحوصُ خامِ أحكامِ المجلسِ (قرارُ المالكِ Q-63 · قيدُ W-542).

الغرض:
    أن يُقاسَ `tools/governance/council_verdict_raw_check.py` و`council_raw_capture.py`
    مرّتَينِ: على أحكامٍ مصنوعةٍ يُرى فيها كلُّ رفضٍ (اقتطاعٌ · وصفٌ نثريٌّ · أمرٌ
    بلا كتلةٍ · بصمةٌ لا تطابقُ · أمرٌ منَ الإحاطةِ لم يُشغَّلْ · «cat» يخالفُ الملفَّ
    عندَ العقدةِ)، وعلى **الشجرةِ الحاضرةِ**: كلُّ حكمِ مقعدٍ محفوظٍ في جولةٍ بعدَ
    القانونِ (قيدٌ رقمُه أكبرُ من `RAW_RULE_AFTER`) يجتازُ الفاحصَ — وإلا سقطَ CI.
    والأحكامُ السابقةُ للقانونِ لا يُطبَّقُ عليها بأثرٍ رجعيٍّ، لكنَّ رفضَها مقيسٌ
    هنا (جولةُ W-538 · DISC-116) فلا يُدَّعى لها خامٌ لم يُثبَت.
المالك: tests/governance — ديوانُ التدقيق (بندُ WI-100 · قرارُ المالكِ Q-63)
تاريخ الإنشاء: 2026-10-20
تاريخ آخر تعديل: 2026-10-20
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools" / "governance"))

import council_raw_capture as cap  # noqa: E402
import council_verdict_raw_check as chk  # noqa: E402

# آخرُ قيدٍ قبلَ أوّلِ جولةٍ تحتَ القانون (W-544 إحاطاتُ الإعادة) — أحكامُ ما بعدَه تُفحَصُ إلزامًا
RAW_RULE_AFTER = 544
NODE = "a" * 40


def _verdict(cmds: list[str], blocks: list[str], *, raw_extra: str = "") -> str:
    listed = "\n".join(f" {i}. {c}" for i, c in enumerate(cmds, 1))
    return (
        "MODEL: m\nFAMILY: f\nRUN_DATE: 2026-10-20 00:00 +00:00\n"
        f"NODE: {NODE}\nCLONE_PATH: /x/repo\n"
        f"COMMANDS_RUN:\n{listed}\n"
        f"RAW_OUTPUTS:\n{raw_extra}{''.join(blocks)}"
        "VERDICT_PER_CRITERION: (1) نعم\n"
        "BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً\n"
        "ISOLATION_DECLARATION: نعم\n"
        "VERDICT: PASS\n"
    )


def _good() -> str:
    cmds = ["printf 'a\\nb\\n'", "printf 'no-eol'", "echo err 1>&2; exit 3"]
    return _verdict(cmds, [cap.capture(i, c) for i, c in enumerate(cmds, 1)])


def test_captured_verdict_is_accepted() -> None:
    rep = chk.check_text(_good())
    assert rep.ok, rep.problems
    assert rep.commands == 3 and rep.blocks == 3


def test_capture_records_exit_and_stderr() -> None:
    block = cap.capture(1, "echo out; echo err 1>&2; exit 7")
    assert "EXIT: 7\n" in block
    assert "out\nerr\n" in block


def test_excerpt_instead_of_blocks_is_rejected() -> None:
    # نمطُ W-538 (kimi_k3): مقاطعُ مفتاحيّةٌ بدلَ المخرج
    text = _verdict(["python m.py"], [], raw_extra=" [1] N=200 append=0.43 ms … EXIT=0\n")
    rep = chk.check_text(text)
    assert not rep.ok
    assert any(p.startswith("R6") for p in rep.problems)
    assert any(p.startswith("R4") and "بلا كتلةِ RAW" in p for p in rep.problems)


def test_prose_description_beside_blocks_is_rejected() -> None:
    # نمطُ W-538 (grok_4_7): وصفُ مخرجِ cat نثرًا
    cmds = ["printf x"]
    text = _verdict(cmds, [cap.capture(1, cmds[0])], raw_extra="--- cat MAPPING.md ---\nجدولٌ يُحيلُ …\n")
    assert any(p.startswith("R6") for p in chk.check_text(text).problems)


def test_truncated_output_fails_the_hash() -> None:
    cmds = ["seq 1 50"]
    block = cap.capture(1, cmds[0]).replace("25\n26\n27\n", "")
    rep = chk.check_text(_verdict(cmds, [block]))
    assert any(p.startswith("R5") and "SHA256" in p for p in rep.problems)
    assert any(p.startswith("R5") and "BYTES" in p for p in rep.problems)


def test_edited_cell_fails_the_hash() -> None:
    # نمطُ W-538 (gemini_3_8_flash): خليّةٌ أُعيدَت كتابتُها
    cmds = ["printf 'قياسُ الجذرِ + وثيقةُ التصميم\\n'"]
    block = cap.capture(1, cmds[0]).replace("قياسُ الجذرِ", "قياسُ جذرِ DISC-100")
    assert any(p.startswith("R5") for p in chk.check_text(_verdict(cmds, [block])).problems)


def test_listed_command_without_block_and_mismatched_cmd_are_rejected() -> None:
    cmds = ["printf a", "printf b"]
    text = _verdict(cmds, [cap.capture(1, "printf DIFFERENT")])
    probs = chk.check_text(text).problems
    assert any("يخالفُ المُعلَن" in p for p in probs)
    assert any("[2] بلا كتلةِ RAW" in p for p in probs)


@pytest.mark.parametrize("field", chk.REQUIRED_FIELDS)
def test_each_required_field_is_required(field: str) -> None:
    text = re.sub(rf"^{field}:", "X_REMOVED:", _good(), count=1, flags=re.M)
    assert any(p.startswith("R1") and field in p for p in chk.check_text(text).problems)


def test_field_inside_raw_output_does_not_count() -> None:
    # حقلٌ داخلَ مخرجٍ خامٍ (cat لقالبٍ) لا يسدُّ حقلًا غائبًا
    cmds = ["printf 'VERDICT: PASS\\n'"]
    text = _verdict(cmds, [cap.capture(1, cmds[0])]).replace("\nVERDICT: PASS\n", "\n")
    assert any(p == "R1 حقلٌ إلزاميٌّ غائبٌ: VERDICT" for p in chk.check_text(text).problems)


def test_short_node_is_rejected() -> None:
    text = _good().replace(NODE, "311d9be")
    assert any(p.startswith("R2") for p in chk.check_text(text).problems)


def test_brief_command_not_run_is_rejected() -> None:
    brief = "## ج · أوامر\n```bash\nprintf 'a\\nb\\n'\nseq 1 3; echo \"EXIT=$?\"\n```\n## د · حدود\n"
    assert chk.brief_commands(brief) == ["printf 'a\\nb\\n'", "seq 1 3"]
    probs = chk.check_text(_good(), brief_text=brief).problems
    assert probs == ["R7 أمرٌ منَ الإحاطةِ بلا كتلةِ RAW: 'seq 1 3'"]


def test_cat_output_is_compared_with_the_file_at_node(tmp_path: Path) -> None:
    repo = tmp_path / "r"
    repo.mkdir()
    (repo / "M.md").write_text("سطرٌ أصليٌّ\n", encoding="utf-8")
    run = lambda *a: subprocess.run(["git", "-C", str(repo), *a], check=True, capture_output=True)  # noqa: E731
    run("init", "-q")
    run("-c", "user.name=t", "-c", "user.email=t@t", "add", "M.md")
    run("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "m")
    node = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    good_cmd = f"cd {repo} && cat M.md"
    text = _verdict([good_cmd], [cap.capture(1, good_cmd)]).replace(NODE, node)
    assert chk.check_text(text, repo=repo).ok
    (repo / "M.md").write_text("سطرٌ مُحرَّرٌ\n", encoding="utf-8")  # الشجرةُ تغيّرت والعقدةُ لا
    text = _verdict([good_cmd], [cap.capture(1, good_cmd)]).replace(NODE, node)
    assert any(p.startswith("R8") for p in chk.check_text(text, repo=repo).problems)


def test_cli_exit_codes(tmp_path: Path) -> None:
    good = tmp_path / "good.md"
    good.write_text(_good(), encoding="utf-8")
    bad = tmp_path / "bad.md"
    bad.write_text(_verdict(["x"], [], raw_extra="مقاطع\n"), encoding="utf-8")
    tool = REPO_ROOT / "tools" / "governance" / "council_verdict_raw_check.py"
    assert subprocess.run([sys.executable, str(tool), str(good)], capture_output=True).returncode == 0
    assert subprocess.run([sys.executable, str(tool), str(bad)], capture_output=True).returncode == 1


def test_capture_cli_writes_block(tmp_path: Path) -> None:
    out = tmp_path / "raw_01.txt"
    tool = REPO_ROOT / "tools" / "governance" / "council_raw_capture.py"
    r = subprocess.run([sys.executable, str(tool), "--n", "1", "--out", str(out), "echo hi"], capture_output=True)
    assert r.returncode == 0
    assert out.read_text(encoding="utf-8").startswith("=== RAW [1] BEGIN ===\nCMD: echo hi\nEXIT: 0\n")


def _round_verdicts() -> list[Path]:
    found = []
    for d in sorted((REPO_ROOT / "docs" / "audit" / "evidence").glob("W-*")):
        m = re.fullmatch(r"W-(\d+)", d.name)
        if not m or int(m.group(1)) <= RAW_RULE_AFTER:
            continue
        for f in sorted(d.glob("*.md")):
            t = f.read_text(encoding="utf-8")
            if re.search(r"^MODEL:", t, re.M) and re.search(r"^VERDICT:", t, re.M):
                found.append(f)
    return found


@pytest.mark.parametrize("verdict", _round_verdicts() or [None], ids=lambda p: p.parent.name + "/" + p.name if p else "none-yet")
def test_repository_round_verdicts_carry_raw_outputs(verdict: Path | None) -> None:
    if verdict is None:
        pytest.skip("لا جولةَ محفوظةٌ بعدَ القانونِ بعدُ")
    rep = chk.check_file(verdict)
    assert rep.ok, rep.problems


def test_pre_rule_round_w538_is_measured_as_rejected() -> None:
    # لا أثرَ رجعيٌّ — لكنَّ الرفضَ مقيسٌ فلا يُدَّعى خامٌ لجولةِ W-538
    d = REPO_ROOT / "docs" / "audit" / "evidence" / "W-538"
    for name in ("gemini_3_8_flash.md", "grok_4_7.md", "kimi_k3.md"):
        assert not chk.check_file(d / name).ok, name
