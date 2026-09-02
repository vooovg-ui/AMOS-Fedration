"""
حرسُ طزاجةِ الأثرِ المُولَّدِ — «الأثرُ المُولَّدُ مدفوعٌ» يُقاسُ قبلَ الدفعِ لا في CI وحدَها
الهدف: إنفاذُ أنَّ `docs/audit/TRUTH_MATRIX.md` و`docs/audit/truth_matrix.json` المكتوبَينِ في الشجرةِ يطابقانِ ما تُولِّدُه الأداةُ الآنَ، وقياسُ أنَّ وجهَ `--check` يُسقِطُ فعلًا ولا يكتُبُ في الشجرةِ التي يحكُمُ عليها.
النطاق: tools/governance/truth_audit.py — وجهُ `--check` وحدَه · والأثرُ المُولَّدُ في `docs/audit/`
المالك: tests/governance/
تاريخ الإنشاء: 2026-09-01
تاريخ آخر تعديل: 2026-09-01

العَطبُ المقيسُ (`DISC-040`):
    مجموعةُ ما قبلَ الدفعِ (§ 5.4) تأمرُ بتشغيلِ `truth_audit.py`، وتشغيلُها **يكتُبُ**
    الأثرَ فيُرضي الأمرَ آمِرَه — ولا يقيسُ أنَّ المكتوبَ **يُدفَعُ**. فالبوّابةُ الوحيدةُ
    التي كانت تلتقطُ التقادُمَ هي `git diff --exit-code` في CI (‏`ci.yml:515`)، فصارَ
    ممكنًا أن تخضَرَّ كلُّ بوّابةٍ محلّيّةٍ ثمَّ يحمَرَّ الحكمُ. وقُرِئَ ذلك حكمًا لا ظنًّا:
    تشغيلُ 33570417864 (‏رقمُ 55) على `9bf0b00` ⇒ `failure` · 12/13 · الوظيفةُ الساقطةُ
    الوحيدةُ `Truth Audit` في خطوةِ «التحقق من أن المصفوفة المدفوعة محدّثة».

لماذا يسكنُ الإنفاذُ فحصًا لا أمرًا جديدًا في § 5.4:
    زيادةُ أمرٍ إلى مجموعةِ ما قبلَ الدفعِ تعديلٌ في وثيقةٍ حاكمةٍ — قرارُ مالكٍ لا فعلُ
    عاملٍ. ومجموعةُ ما قبلَ الدفعِ تُشغِّلُ `pytest tests/ -q` أصلًا، وCI تُشغِّلُ
    `pytest tests/governance/` (‏السطرُ 117) و`pytest tests/ --cov` (‏السطرُ 579) — فطريقُ
    الإنفاذِ قائمٌ بلا مسِّ مسارٍ مقفولٍ ولا نصٍّ سياديٍّ.

حدُّ الحرسِ — مُعلَنٌ لا مطويٌّ:
    - يقيسُ أثرَ هذه الأداةِ وحدَها؛ وكلُّ كاتبٍ آخرَ في `docs/audit/` يبقى محكومًا بحارسِه هو.
    - و«الطزاجةُ» تُقاسُ بمطابقةِ المُولَّدِ للمكتوبِ لا بصحّةِ المُولَّدِ نفسِه.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "truth_audit.py"
ARTIFACTS = ("docs/audit/TRUTH_MATRIX.md", "docs/audit/truth_matrix.json")


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else "—"


def _seed_tree(tmp_path: Path) -> Path:
    """شجرةٌ مؤقَّتةٌ تحملُ نسخةَ الأداةِ نفسِها — فالمقيسُ فيها هي لا المستودعُ الحقيقيُّ.

    وتُعادُ **قيمةً واحدةً** لا زوجًا مُفكَّكًا: الحرسُ في
    `test_w096_subprocess_measurement_site.py` يقتفي اسمَ الشجرةِ المؤقَّتةِ عبرَ
    الإسنادِ إلى **اسمٍ مفردٍ**، والتفكيكُ إلى زوجٍ يُخفي الاسمَ عنه فيُقرأُ موضعُ
    القياسِ «مستودعًا حقيقيًّا» وهو مؤقَّتٌ. فلا يُكتَبُ ما يُعمي حارسًا قائمًا.
    """
    tree = tmp_path / "repo"
    (tree / "tools" / "governance").mkdir(parents=True)
    (tree / "docs" / "audit").mkdir(parents=True)
    shutil.copy2(TOOL_PATH, tree / "tools" / "governance" / "truth_audit.py")
    # الأداةُ تقرأُ سجلَّ الأدلّةِ من جذرِها المُمرَّرِ — فيُنسَخُ معَها لتقرأَ شجرتَها هي.
    shutil.copy2(
        TOOL_PATH.with_name("evidence_registry.py"),
        tree / "tools" / "governance" / "evidence_registry.py",
    )

    domain = tree / "core"
    domain.mkdir()
    (domain / "README.md").write_text("# core\n", encoding="utf-8")
    (domain / "unit.py").write_text("VALUE = 1\n", encoding="utf-8")

    return tree


def _settle(tmp_path: Path) -> None:
    """يُولَّدُ الأثرُ مرَّتَينِ حتّى يستقرَّ.

    الأثرُ المُولَّدُ يسكُنُ الشجرةَ التي يُقاسُ عليها، فأوّلُ توليدٍ في شجرةٍ خاليةٍ
    يزيدُ ملفَّ `TRUTH_MATRIX.md` نفسَه إلى عدَدِ ملفّاتِ `docs` — وهذه **خاصّةُ
    التوليدِ لا عَطبُ الوجهِ**، وهي مُستقرّةٌ بعدَ التوليدِ الثاني. وتُعلَنُ ولا تُطوى:
    في المستودعِ الحقيقيِّ الأثرُ موجودٌ أصلًا فلا تظهرُ.

    واسمُ المُعامِلِ `tmp_path` مقصودٌ: حارسُ مواضعِ القياسِ يقرأُ اسمَ الشجرةِ
    المؤقَّتةِ من الاسمِ نفسِه، فلو سُمِّيَ غيرَ ذلك لقُرِئَ الموضعُ «مستودعًا
    حقيقيًّا» وهو مؤقَّتٌ — وتسميةٌ تُعمي حارسًا أسوأُ من حارسٍ غائبٍ.
    """
    for _ in range(2):
        subprocess.run(
            [
                sys.executable,
                str(tmp_path / "tools/governance/truth_audit.py"),
                str(tmp_path),
            ],
            cwd=str(tmp_path), capture_output=True, text=True, check=True,
        )


def _check(tmp_path: Path) -> subprocess.CompletedProcess[str]:
    """يُشغَّلُ المُشغَّلُ **داخلَ** الشجرةِ المؤقَّتةِ ومحلُّ القياسِ مُمرَّرٌ صريحًا (`DISC-032`)."""
    return subprocess.run(
        [
            sys.executable,
            str(tmp_path / "tools/governance/truth_audit.py"),
            str(tmp_path),
            "--check",
        ],
        cwd=str(tmp_path), capture_output=True, text=True, check=False,
    )


# ── الحرسُ على الشجرةِ الحاضرةِ ───────────────────────────────────────────────


def test_الأثرُ_المُولَّدُ_في_المستودعِ_طازجٌ_لا_متقادمٌ() -> None:
    """عينُ ما حمَّرَ التشغيلَ 55 يُقاسُ هنا قبلَ الدفعِ — REAL_TREE_ON_PURPOSE."""
    before = {rel: _digest(REPO_ROOT / rel) for rel in ARTIFACTS}

    result = subprocess.run(  # noqa: S603 — REAL_TREE_ON_PURPOSE: الحكمُ على المستودعِ الحقيقيِّ مقصودٌ
        [sys.executable, str(TOOL_PATH), str(REPO_ROOT), "--check"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )

    after = {rel: _digest(REPO_ROOT / rel) for rel in ARTIFACTS}
    assert before == after, (
        "وجهُ `--check` كتبَ في الشجرةِ التي يحكُمُ عليها — "
        "وحاكمٌ يكتُبُ ما يقيسُ لا يقيسُ شيئًا"
    )
    assert result.returncode == 0, (
        "الأثرُ المُولَّدُ في الشجرةِ متقادمٌ: أعِدْ توليدَه بـ"
        "`python tools/governance/truth_audit.py` وادفعْه مع عملِك — "
        "ولا يُخفَّفُ هذا الفحصُ ولا يُسكَتُ.\n"
        f"{result.stdout}\n{result.stderr}"
    )


# ── قياسُ الحرسِ نفسِه: لا يُطمَأنُّ إلى خضرةٍ لم تُختَبَرْ ───────────────────


def test_الوجهُ_يسكُتُ_على_أثرٍ_طازجٍ(tmp_path: Path) -> None:
    tree = _seed_tree(tmp_path)
    _settle(tree)

    fresh = _check(tree)
    assert fresh.returncode == 0, f"سقطَ على أثرٍ طازجٍ:\n{fresh.stdout}\n{fresh.stderr}"


def test_الوجهُ_يُسقِطُ_على_أثرٍ_متقادمٍ_ويُسمّي_الملفَّ_والحقلَ(tmp_path: Path) -> None:
    tree = _seed_tree(tmp_path)
    _settle(tree)

    matrix = tree / "docs" / "audit" / "truth_matrix.json"
    payload = json.loads(matrix.read_text(encoding="utf-8"))
    payload["domains"]["core"]["code_lines"] = 999999
    matrix.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    stale = _check(tree)
    assert stale.returncode != 0, "أثرٌ متقادمٌ مرَّ أخضرَ — حرسٌ لا يُسقِطُ ليسَ حرسًا"
    output = stale.stdout + stale.stderr
    assert "truth_matrix.json" in output, "الرسالةُ لا تُسمّي الملفَّ فلا تُصلِحُ"
    assert "code_lines" in output and "999999" in output, "الرسالةُ لا تُسمّي الحقلَ المتقادمَ"


def test_الوجهُ_يُسقِطُ_حينَ_لا_أثرَ_أصلًا(tmp_path: Path) -> None:
    tree = _seed_tree(tmp_path)
    _settle(tree)
    (tree / "docs" / "audit" / "truth_matrix.json").unlink()

    missing = _check(tree)
    assert missing.returncode != 0, "غيابُ الأثرِ المُولَّدِ مرَّ أخضرَ"
    assert "truth_matrix.json" in missing.stdout + missing.stderr


def test_الوجهُ_لا_يكتُبُ_في_الشجرةِ_التي_يحكُمُ_عليها(tmp_path: Path) -> None:
    """يُقاسُ ببصمةِ الملفَّينِ قبلَ التشغيلِ وبعدَه — وبأنَّ الغائبَ يبقى غائبًا."""
    tree = _seed_tree(tmp_path)
    _settle(tree)
    before = {rel: _digest(tree / rel) for rel in ARTIFACTS}

    _check(tree)
    assert {rel: _digest(tree / rel) for rel in ARTIFACTS} == before

    for rel in ARTIFACTS:
        (tree / rel).unlink()
    _check(tree)
    assert not any((tree / rel).exists() for rel in ARTIFACTS), (
        "الوجهُ أنشأَ الأثرَ الذي يحكُمُ على غيابِه — فبوّابةٌ تُصلِحُ ما تقيسُ لا تقيسُ"
    )


def test_التوليدُ_بلا_علمٍ_يبقى_يكتُبُ_فالوجهُ_زيادةٌ_لا_تخفيفٌ(tmp_path: Path) -> None:
    """`--check` لا يُغيِّرُ سلوكَ الأداةِ الأصليَّ: التوليدُ بلا علمٍ ما زالَ يكتُبُ."""
    tree = _seed_tree(tmp_path)
    assert not (tree / "docs" / "audit" / "truth_matrix.json").exists()

    _settle(tree)
    assert all((tree / rel).exists() for rel in ARTIFACTS), "التوليدُ توقَّفَ عن الكتابةِ"
