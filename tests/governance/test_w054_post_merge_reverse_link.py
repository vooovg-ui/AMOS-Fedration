"""
الهدف: إثباتُ أنَّ حرسَ ما بعدَ الدمجِ يُقاسُ **بالاتِّجاهِ العكسيّ** — من قيدِ
       سجلِّ الإكمالِ المدموجِ في فرعِ الدولةِ إلى بندِه في `ACTIVE_WORK.md` — فلا
       يبقى صامتًا في عينِ الحالةِ التي بُنِيَ لها: بندٌ دُمِجَ عملُه وقُيِّدَ،
       وخليّةُ «قيدُ السجلّ» فيه فارغةٌ لأنَّ من يجبُ عليه الإغلاقُ لم يُغلِق.
النطاق: `ledger_reverse_links` و`resolve_merge_base` و`check_post_merge_closure`
        ووصلُها في `run`/`main` من `tools/governance/check_work_governance.py`.
        لا يُقاسُ هنا صدقُ مضمونِ القيدِ — الحدُّ مُعلَنٌ في THE_ROADMAP § 13.3.
المالك: tests/governance
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-08-27

لماذا هذا الاختبار
------------------
القياسُ القائمُ قبلَ `W-054` كان يقرأُ الرابطَ من **البندِ إلى القيدِ**: خليّةُ
«قيدُ السجلّ» في صفِّ البند. وتلك الخليّةُ يكتبُها **من يجبُ عليه الإغلاق**، فهي
فارغةٌ بالضرورةِ ما دامَ الواجبُ مُهمَلًا — فكانَ الحرسُ يصمُتُ عن الحالةِ الوحيدةِ
التي أُنشئَ لأجلِها. ويُثبَّتُ هنا الاتِّجاهُ المقابلُ، ويُثبَّتُ معَه أنَّ الدفعَ
المشروعَ قبلَ الدمجِ (‏قيدٌ في الفرعِ لا في `main`) لا يُحمَّرُ، وأنَّ تعذُّرَ قراءةِ
الأساسِ يُعلَنُ ولا يُطوى.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "check_work_governance.py"


def _load_tool():
    spec = importlib.util.spec_from_file_location("check_work_governance_w054", TOOL_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gate = _load_tool()
TODAY = date(2026, 8, 27)

ACTIVE_ROW = (
    "| WI-006 | tooling-gates | T0 | فلان | فلانٌ آخر | {status} "
    "| tools/governance/ci_verdict_readability.py | 2026-08-27 | 2026-09-30 | — "
    "| خطوةٌ واحدة | {ledger} |"
)

DETAIL_BLOCK = """### WI-006 — بندٌ تجريبيّ

```text
النطاق: tooling-gates
خارجَ النطاق: لا شيء
معيارُ القبول: شرطٌ يُقاس
الدليلُ المطلوب: أمرٌ يُعادُ تشغيلُه
```
"""

OWNERSHIP_ROW = "| tooling-gates | tools/governance | فلان | فلانٌ آخر | — | C1 |"
DISCOVERY_ROW = (
    "| DISC-001 | P2 | موضع | ما اكتُشِف | دليل | أثر | بندٌ في ACTIVE_WORK | مفتوح |"
)
RISK_ROW = "| RK-001 | خطر | مرتفع | أثر | إشارة | تصرُّف | مالك | مصدر |"

# صفُّ قيدٍ يُعلِنُ بندَه رابطًا — وهو وحدَه ما يُقاس (‏الذكرُ العارضُ لا يُقاس).
LEDGER_LINKED = (
    "| W-051 | 2026-08-27 | عملٌ مُقيَّد | في البندِ "
    "[`WI-006`](../governance/work/ACTIVE_WORK.md) قُيِّدَ ما تمَّ | حدٌّ مُعلَن | دليل |"
)
LEDGER_BARE_MENTION = (
    "| W-052 | 2026-08-27 | عملٌ آخر | لم يُمَسَّ محجوزٌ لغيرِه: WI-006 محجوزٌ له "
    "| حدٌّ مُعلَن | دليل |"
)


def _register(path: str, *extra: str) -> str:
    return "\n".join([*gate.REQUIRED_SECTIONS.get(path, ()), *extra, ""])


def _write_registers(repo: Path, *, status: str, ledger_cell: str, ledger_rows: str) -> None:
    files = {
        gate.ROADMAP_PATH: _register(gate.ROADMAP_PATH),
        gate.ACTIVE_PATH: _register(
            gate.ACTIVE_PATH,
            ACTIVE_ROW.format(status=status, ledger=ledger_cell),
            DETAIL_BLOCK,
        ),
        gate.OWNERSHIP_PATH: _register(gate.OWNERSHIP_PATH, OWNERSHIP_ROW),
        gate.RISK_PATH: _register(gate.RISK_PATH, RISK_ROW),
        gate.DISCOVERIES_PATH: _register(gate.DISCOVERIES_PATH, DISCOVERY_ROW),
        gate.HANDOFF_TEMPLATE_PATH: "# قالبٌ\n",
        gate.LEDGER_PATH: f"{ledger_rows}\n",
    }
    for rel, body in files.items():
        target = repo / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")


def _mkrepo(
    tmp_path: Path,
    *,
    merged_ledger: str = "| W-000 | تأسيس |",
    status: str = "IN_REVIEW",
    ledger_cell: str = "—",
) -> Path:
    """مستودعٌ فيه فرعُ دولةٍ (`main`) قيدُه المدموجُ هو `merged_ledger`."""
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t.t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    _write_registers(tmp_path, status=status, ledger_cell=ledger_cell, ledger_rows=merged_ledger)
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "أساسُ الدمج"], cwd=tmp_path, check=True)
    return tmp_path


def _kinds(**kw) -> set[str]:
    return {v["kind"] for v in gate.run("staged", None, shape_only=True, today=TODAY, **kw)}


# ── القياسُ العكسيُّ نفسُه ────────────────────────────────────────────────────


def test_قراءةُ_الروابطِ_تقتصرُ_على_الإعلانِ_الصريح() -> None:
    links = gate.ledger_reverse_links(f"{LEDGER_LINKED}\n{LEDGER_BARE_MENTION}\n")
    assert links == {"W-051": {"WI-006"}}, "الذكرُ العارضُ لا يُقاسُ، والإعلانُ الصريحُ يُقاس"


def test_بندٌ_قيدُه_مدموجٌ_وحالتُه_ليست_مُغلَقةً_يُرصَد(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """عينُ الحالةِ التي صمَتَ عنها الحرسُ الأوّل: القيدُ مدموجٌ والخليّةُ فارغة."""
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_LINKED)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "POST_MERGE_NOT_CLOSED" in _kinds(merge_base="main", enforce_post_merge=True)


def test_الإغلاقُ_يُسكِتُ_الحرس(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(
        tmp_path, merged_ledger=LEDGER_LINKED, status="CLOSED", ledger_cell="W-051 · دمج #20"
    )
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "POST_MERGE_NOT_CLOSED" not in _kinds(merge_base="main", enforce_post_merge=True)


def test_دفعٌ_قبلَ_الدمجِ_لا_يُحمَّر(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """قيدٌ في الفرعِ ولم يُدمَجْ بعد: `IN_REVIEW` حقٌّ لا مخالفة."""
    repo = _mkrepo(tmp_path)  # فرعُ الدولةِ بلا قيدٍ يُعلِنُ البند
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    (repo / gate.LEDGER_PATH).write_text(f"{LEDGER_LINKED}\n", encoding="utf-8")
    assert "POST_MERGE_NOT_CLOSED" not in _kinds(merge_base="main", enforce_post_merge=True)


def test_الذكرُ_العارضُ_في_قيدٍ_مدموجٍ_لا_يُحمَّر(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_BARE_MENTION)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "POST_MERGE_NOT_CLOSED" not in _kinds(merge_base="main", enforce_post_merge=True)


# ── الإسقاطُ والإبلاغُ وحدُّ القياس ───────────────────────────────────────────


def test_الافتراضيُّ_إبلاغٌ_لا_إسقاطٌ_ما_دامَ_A2_معلَّقًا(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """طريقُ `IN_REVIEW → VERIFIED → CLOSED` يلزمُه مراجعٌ لم يُعيَّنْ (`A-2`)."""
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_LINKED)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    notes: list[str] = []
    kinds = {
        v["kind"]
        for v in gate.run(
            "staged", None, shape_only=True, today=TODAY, merge_base="main", notes=notes
        )
    }
    assert "POST_MERGE_NOT_CLOSED" not in kinds, "الإسقاطُ لا يكونُ افتراضًا"
    assert any("POST_MERGE_NOT_CLOSED" in n for n in notes), "ولا يُطوى: يُعلَنُ في الملاحظات"


def test_تعذُّرُ_قراءةِ_الأساسِ_يُعلَنُ_ولا_يُطوى(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_LINKED)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    notes: list[str] = []
    gate.run(
        "staged", None, shape_only=True, today=TODAY, merge_base="لا-وجود-له", notes=notes
    )
    assert notes and "لم يُقَسْ" in notes[0]


def test_أساسٌ_مُمَرَّرٌ_صراحةً_لا_يُتجاوَزُ_إلى_غيرِه(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_LINKED)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert gate.resolve_merge_base("main") == "main"
    assert gate.resolve_merge_base("لا-وجود-له") is None, "لا قياسٌ عن أساسٍ في زيِّ آخر"


def _run_tool(repo: Path, *extra: str, cwd: Path | None = None):
    """تشغيلُ الأداةِ على شجرةِ الاختبارِ وحدها (DISC-022).

    الجذرُ يُمَرَّرُ صراحةً، فلا تقعُ العمليةُ الفرعيةُ على المستودعِ الحقيقيِّ: ترقيعُ
    `gate.REPO_ROOT` لا يبلغُ عمليةً أخرى، وكانت الأداةُ تشتقُّ جذرَها من موقعِ ملفِّها.
    """
    return subprocess.run(
        [sys.executable, str(TOOL_PATH), "--repo-root", str(repo), *extra],
        cwd=cwd or repo,
        capture_output=True,
        text=True,
        check=False,
    )


def test_رفضٌ_مُعلَنٌ_حينَ_يُطلَبُ_الأساسُ_ولا_يُقرَأ(tmp_path: Path) -> None:
    """`--require-merge-base` يرفضُ (رمز 2) ولا يمرُّ مرورًا صامتًا."""
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_LINKED)
    out = _run_tool(
        repo, "--self-check", "--merge-base", "لا-وجود-له", "--require-merge-base"
    )
    assert out.returncode == 2, out.stdout + out.stderr


# ── W-054 · أ) الإسقاطُ يُطلَبُ فيسقُط ───────────────────────────────────


def test_الإسقاطُ_يُطلَبُ_فيسقُط(tmp_path: Path) -> None:
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_LINKED)
    out = _run_tool(repo, "--self-check", "--merge-base", "main", "--enforce-post-merge")
    assert out.returncode == 1, out.stdout + out.stderr
    assert "POST_MERGE_NOT_CLOSED" in out.stdout
    assert "WI-006" in out.stdout, "المخالفةُ تُسمّي بندَ الشجرةِ المقيسةِ"
    assert "لم يُقَسْ" not in out.stderr, "الأساسُ مقروءٌ من شجرةِ الاختبارِ"


# ── W-054 · ب) الإغلاقُ الحقيقيُّ يُمرِّرُ البوّابة ───────────────────────────


def test_الإغلاقُ_الحقيقيُّ_يُمرِّرُ_الإسقاطَ(tmp_path: Path) -> None:
    """لا تُقاسُ الحمرةُ وحدها: إغلاقٌ معَ قيدٍ يُسكِتُ الحرسَ برمزِ صفرٍ."""
    repo = _mkrepo(
        tmp_path,
        merged_ledger=LEDGER_LINKED,
        status="CLOSED",
        ledger_cell="W-051 · دمج #20",
    )
    out = _run_tool(repo, "--self-check", "--merge-base", "main", "--enforce-post-merge")
    assert out.returncode == 0, out.stdout + out.stderr
    assert "POST_MERGE_NOT_CLOSED" not in out.stdout


# ── W-054 · ج) لا يعتمدُ على حالةِ المستودعِ الحقيقيِّ ───────────────────────


def test_الحكمُ_يتبعُ_شجرةَ_الاختبارِ_لا_المستودعَ(tmp_path: Path) -> None:
    """شجرتانِ لا تختلفانِ إلّا في الإغلاقِ تُعطيانِ حكمَينِ مختلفَينِ.

    والمستودعُ الحقيقيُّ لم يُمَسّ، فلو كانَ هو المقروءَ لما اختلفَ الحكمان.
    """
    for اسم in ("مفتوح", "مغلق"):
        (tmp_path / اسم).mkdir()
    مفتوح = _mkrepo(tmp_path / "مفتوح", merged_ledger=LEDGER_LINKED)
    مغلق = _mkrepo(
        tmp_path / "مغلق",
        merged_ledger=LEDGER_LINKED,
        status="CLOSED",
        ledger_cell="W-051 · دمج #20",
    )
    حجة = ("--self-check", "--merge-base", "main", "--enforce-post-merge")
    assert _run_tool(مفتوح, *حجة).returncode == 1
    assert _run_tool(مغلق, *حجة).returncode == 0


def test_القياسُ_لا_يتغيرُ_بموضعِ_التشغيلِ(tmp_path: Path) -> None:
    """جذرٌ مُمَرَّرٌ يُقاسُ منهُ وإن كانَ موضعُ التشغيلِ جوفَ المستودعِ الحقيقيِّ."""
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_LINKED)
    حجة = ("--self-check", "--merge-base", "main", "--enforce-post-merge")
    من_الشجرة = _run_tool(repo, *حجة)
    من_المستودع = _run_tool(repo, *حجة, cwd=REPO_ROOT)
    assert من_الشجرة.returncode == من_المستودع.returncode == 1
    assert "WI-006" in من_المستودع.stdout


def test_أساسٌ_محليٌّ_غائبٌ_يُعلَنُ_ولا_يُطوَى(tmp_path: Path) -> None:
    """علّةُ الحُمرةِ في التكاملِ تُقاسُ لا تُحكى: شجرةٌ بلا `main` تُعلِنُ أنّه لم يُقَس.

    فبـ`--repo-root` يصيرُ الحدُّ مقيسًا في اختبارٍ، لا مفاجأةً تقعُ في عاملِ التكامل.
    """
    repo = _mkrepo(tmp_path, merged_ledger=LEDGER_LINKED)
    subprocess.run(["git", "branch", "-m", "main", "فرع"], cwd=repo, check=True)
    out = _run_tool(repo, "--self-check", "--merge-base", "main", "--enforce-post-merge")
    assert out.returncode == 0
    assert "لم يُقَسْ" in out.stderr, "حدُّ القياسِ يُعلَنُ على كلِّ حال"


# ── المستودعُ الحقيقيُّ: الواجبُ المُهمَلُ يُقاسُ فعلًا ─────────────────────────


def test_واجبُ_ما_بعدَ_الدمجِ_في_المستودعِ_يُقاسُ_لا_يُخمَّن() -> None:
    """قياسٌ على السجلِّ الحقيقيّ: كلُّ قيدٍ يُعلِنُ بندَه رابطًا يُقرأُ إعلانُه."""
    text = (REPO_ROOT / gate.LEDGER_PATH).read_text(encoding="utf-8")
    links = gate.ledger_reverse_links(text)
    assert links, "لا قيدَ واحدًا يُعلِنُ بندَه رابطًا — القياسُ العكسيُّ بلا مادّة"
    items, malformed = gate.parse_items(
        (REPO_ROOT / gate.ACTIVE_PATH).read_text(encoding="utf-8")
    )
    assert malformed == []
    known = {str(it["id"]) for it in items}
    for work_id, declared in links.items():
        for item_id in declared:
            assert item_id in known, f"{work_id} يُعلِنُ بندًا غيرَ موجودٍ: {item_id}"
