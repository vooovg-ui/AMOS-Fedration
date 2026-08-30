"""
الهدف: إثباتُ أنّ بوابةَ حوكمةِ العملِ تُنفِذُ الخارطةَ الحاكمةَ فعلًا — تسقطُ عند
       عملٍ بلا قيد، وعند تقاطعِ بندَينِ في مسار، وعند حجزٍ منتهٍ، وعند إغلاقٍ بلا
       قيدِ سجلّ، وعند انتقالِ حالةٍ ممنوع؛ وتمرُّ على السجلّاتِ السليمة.
النطاق: سلوكُ `tools/governance/check_work_governance.py` وحدَه. لا يُقاسُ هنا
        مضمونُ البنود — البوّابةُ تُقاسُ بسلوكِها لا بما تُنتِجُه من نصوص.
المالك: tests/governance
تاريخ الإنشاء: 2026-08-25
تاريخ آخر تعديل: 2026-08-25

لماذا تُختبَرُ البوابةُ لا نتيجتُها
-----------------------------------
بوابةٌ تمرُّ دائمًا ليست بوابة. فيُثبَّتُ هنا أنَّ كلَّ مخالفةٍ مُعلَنةٍ في
`THE_ROADMAP § 13` تسقطُ فعلًا، وأنَّ إعفاءَ سجلّاتِ الطبقةِ من الحجزِ لا يتوسَّعُ
إلى الكود، وأنَّ حدَّ البوّابةِ المُعلَنَ (الشكلُ والتقاطعُ لا صدقُ المضمون) محفوظ.
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
    spec = importlib.util.spec_from_file_location("check_work_governance", TOOL_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gate = _load_tool()

TODAY = date(2026, 8, 25)

ACTIVE_ROW = (
    "| WI-001 | tooling-gates | T2 | فلان | فلانٌ آخر | IN_PROGRESS "
    "| tools/governance · src | 2026-08-20 | 2026-09-30 | — | خطوةٌ واحدة | — |"
)

DETAIL_BLOCK = """### WI-001 — بندٌ تجريبيّ

```text
النطاق: tooling-gates
الحالة: IN_PROGRESS
خارجَ النطاق: لا شيء
معيارُ القبول: شرطٌ يُقاس
الدليلُ المطلوب: أمرٌ يُعادُ تشغيلُه
```
"""

#: حالةُ الكتلةِ يجبُ أن تُطابِقَ حالةَ الصفِّ (`STATUS_CONTRADICTION` · W-069)، فتُولَّدُ
#: الكتلةُ الافتراضيّةُ من صفِّ التجهيزِ نفسِه لا تُثبَّتُ على حالةٍ واحدة.
def _detail_for(rows: str) -> str:
    """كتلةُ تفصيلٍ حالتُها حالةُ أوّلِ صفٍّ في `rows` — تجهيزٌ لا تخفيفُ حرسٍ."""
    for line in rows.splitlines():
        cells = line.split("|")
        if len(cells) >= 14 and cells[1].strip().startswith("WI-"):
            status = cells[6].strip()
            return DETAIL_BLOCK.replace(
                "الحالة: IN_PROGRESS", f"الحالة: {status}"
            ).replace("### WI-001", f"### {cells[1].strip()}")
    return DETAIL_BLOCK

OWNERSHIP_ROW = "| tooling-gates | tools/governance · src | فلان | فلانٌ آخر | — | C1 |"
DISCOVERY_ROW = (
    "| DISC-001 | P2 | موضع | ما اكتُشِف | دليل | أثر | بندٌ في ACTIVE_WORK | مفتوح |"
)
RISK_ROW = "| RK-001 | خطر | مرتفع | أثر | إشارة | تصرُّف | مالك | مصدر |"


def _register(path: str, *extra: str) -> str:
    """نصُّ سجلٍّ أدنى: أقسامُه الإلزاميّةُ ثمَّ صفوفُه."""
    return "\n".join([*gate.REQUIRED_SECTIONS.get(path, ()), *extra, ""])


def _write_registers(
    repo: Path,
    *,
    active_rows: str = ACTIVE_ROW,
    details: str | None = None,
    ownership_rows: str = OWNERSHIP_ROW,
    discovery_rows: str = DISCOVERY_ROW,
) -> None:
    files = {
        gate.ROADMAP_PATH: _register(gate.ROADMAP_PATH),
        gate.ACTIVE_PATH: _register(
            gate.ACTIVE_PATH,
            active_rows,
            _detail_for(active_rows) if details is None else details,
        ),
        gate.OWNERSHIP_PATH: _register(gate.OWNERSHIP_PATH, ownership_rows),
        gate.RISK_PATH: _register(gate.RISK_PATH, RISK_ROW),
        gate.DISCOVERIES_PATH: _register(gate.DISCOVERIES_PATH, discovery_rows),
        gate.HANDOFF_TEMPLATE_PATH: "# قالبٌ\n",
        gate.LEDGER_PATH: "| W-000 | تأسيس |\n",
    }
    for rel, body in files.items():
        target = repo / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")


def _mkrepo(tmp_path: Path, **kwargs: str) -> Path:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t.t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    _write_registers(tmp_path, **kwargs)
    (tmp_path / "src").mkdir(exist_ok=True)
    (tmp_path / "src" / "a.py").write_text("x = 1\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "base"], cwd=tmp_path, check=True)
    return tmp_path


def _stage(repo: Path, rel: str, content: str) -> None:
    target = repo / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    subprocess.run(["git", "add", rel], cwd=repo, check=True)


def _kinds(mode: str = "staged", ref: str | None = None, shape_only: bool = False) -> set[str]:
    return {v["kind"] for v in gate.run(mode, ref, shape_only=shape_only, today=TODAY)}


# ── المستودعُ الحقيقيّ ────────────────────────────────────────────────────────


def test_الأداةُ_وسجلّاتُ_الطبقةِ_موجودة() -> None:
    assert TOOL_PATH.is_file(), "بوابةُ حوكمةِ العملِ غيرُ موجودة"
    for rel in gate.REQUIRED_REGISTERS:
        assert (REPO_ROOT / rel).is_file(), f"{rel} غيرُ موجود"


def test_الاستدعاءُ_الذاتيُّ_يمرُّ_على_المستودع() -> None:
    """سجلّاتُ المستودعِ الحقيقيّةُ سليمةُ الشكلِ ولا تقاطعَ فيها."""
    out = subprocess.run(
        [sys.executable, str(TOOL_PATH), "--self-check"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert out.returncode == 0, out.stdout + out.stderr


def test_كلُّ_نطاقِ_بندٍ_مُسجَّلٌ_في_سجلِّ_الملكيّة() -> None:
    items, malformed = gate.parse_items(
        (REPO_ROOT / gate.ACTIVE_PATH).read_text(encoding="utf-8")
    )
    scopes = gate.parse_scopes((REPO_ROOT / gate.OWNERSHIP_PATH).read_text(encoding="utf-8"))
    assert malformed == []
    assert items, "لا بندَ واحدًا في سجلِّ العملِ المفتوح"
    for item in items:
        assert item["scope"] in scopes, f"{item['id']}: نطاقٌ غيرُ مُسجَّل"


# ── الشكلُ والاتّساق ──────────────────────────────────────────────────────────


def test_غيابُ_سجلٍّ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    (repo / gate.OWNERSHIP_PATH).unlink()
    assert _kinds(shape_only=True) == {"REGISTER_MISSING"}


def test_غيابُ_قسمٍ_إلزاميٍّ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    (repo / gate.ACTIVE_PATH).write_text("# بلا أقسام\n", encoding="utf-8")
    assert "REGISTER_SECTION_MISSING" in _kinds(shape_only=True)


def test_التشكيلُ_لا_يكسِرُ_مطابقةَ_الأقسام(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """العناوينُ تُطابَقُ منزوعةَ التشكيل — فتحةٌ تُضافُ لا تُسقِطُ البوّابة."""
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    body = (repo / gate.ACTIVE_PATH).read_text(encoding="utf-8")
    (repo / gate.ACTIVE_PATH).write_text(
        body.replace("## 1 · البنود النشطة", "## 1 · البنودُ النشِطة"), encoding="utf-8"
    )
    assert "REGISTER_SECTION_MISSING" not in _kinds(shape_only=True)


def test_تكرارُ_معرِّفِ_بندٍ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path, active_rows=f"{ACTIVE_ROW}\n{ACTIVE_ROW}")
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "DUPLICATE_ITEM_ID" in _kinds(shape_only=True)


def test_حالةٌ_خارجَ_آلةِ_الحالاتِ_تُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path, active_rows=ACTIVE_ROW.replace("IN_PROGRESS", "شغّالٌ تقريبًا"))
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "ILLEGAL_STATUS" in _kinds(shape_only=True)


def test_نطاقٌ_غيرُ_مُسجَّلٍ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path, active_rows=ACTIVE_ROW.replace("tooling-gates |", "نطاقٌ مُختلَق |", 1))
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "SCOPE_UNOWNED" in _kinds(shape_only=True)


def test_بندٌ_نشِطٌ_بلا_مالكٍ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path, active_rows=ACTIVE_ROW.replace("| فلان |", "| — |", 1))
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "OWNERLESS_ITEM" in _kinds(shape_only=True)


def test_تاريخٌ_بغيرِ_الصيغةِ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path, active_rows=ACTIVE_ROW.replace("2026-08-20", "قريبًا"))
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "MALFORMED_ITEM" in _kinds(shape_only=True)


def test_بندٌ_نشِطٌ_بلا_كتلةِ_تفاصيلَ_يُرصَد(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = _mkrepo(tmp_path, details="")
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "MALFORMED_ITEM" in _kinds(shape_only=True)


def test_كتلةُ_تفاصيلَ_ناقصةُ_حقلٍ_تُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path, details=DETAIL_BLOCK.replace("معيارُ القبول: شرطٌ يُقاس", ""))
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "MALFORMED_ITEM" in _kinds(shape_only=True)


def test_إغلاقٌ_بلا_قيدِ_سجلٍّ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path, active_rows=ACTIVE_ROW.replace("IN_PROGRESS", "CLOSED"))
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "MISSING_LEDGER_LINK" in _kinds(shape_only=True)


def test_اكتشافٌ_بلا_وجهةٍ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(
        tmp_path, discovery_rows=DISCOVERY_ROW.replace("بندٌ في ACTIVE_WORK", "—")
    )
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "UNROUTED_DISCOVERY" in _kinds(shape_only=True)


# ── منعُ التكرار: التقاطعُ والحجز ────────────────────────────────────────────


def test_تقاطعُ_بندَينِ_في_مسارٍ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """جوهرُ الطبقة: نطاقٌ واحدٌ لجهتَينِ يسقطُ قبلَ أن يصيرَ عملًا مُكرَّرًا."""
    second = (
        "| WI-002 | tooling-gates | T2 | آخر | مراجع | RESERVED "
        "| tools/governance/x.py | 2026-08-24 | 2026-09-30 | — | خطوة | — |"
    )
    details = DETAIL_BLOCK + DETAIL_BLOCK.replace("WI-001", "WI-002")
    repo = _mkrepo(tmp_path, active_rows=f"{ACTIVE_ROW}\n{second}", details=details)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "CLAIM_CONFLICT" in _kinds(shape_only=True)


def test_مساراتٌ_متجاورةٌ_لا_تُعَدُّ_تقاطعًا() -> None:
    assert gate._paths_overlap("tools/governance", "tools/governance/a.py") is True
    assert gate._paths_overlap("tools/governance", "tools/dev") is False
    assert gate._paths_overlap("tools/gov", "tools/governance") is False


def test_حجزٌ_منتهٍ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path, active_rows=ACTIVE_ROW.replace("2026-09-30", "2026-08-01"))
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert "RESERVATION_EXPIRED" in _kinds(shape_only=True)


def test_حجزٌ_سارٍ_لا_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    assert _kinds(shape_only=True) == set()


# ── مجموعةُ التغيير ──────────────────────────────────────────────────────────


def test_تغييرٌ_في_مسارٍ_محجوزٍ_يمرُّ(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    _stage(repo, "src/a.py", "x = 2\n")
    assert _kinds() == set()


def test_تغييرٌ_في_مسارٍ_غيرِ_محجوزٍ_يسقط(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    _stage(repo, "core/other.py", "y = 1\n")
    assert _kinds() == {"PATH_UNCLAIMED"}


@pytest.mark.parametrize(
    "path",
    [
        gate.ACTIVE_PATH,
        gate.OWNERSHIP_PATH,
        gate.LEDGER_PATH,
        "docs/audit/TRUTH_MATRIX.md",
        "docs/governance/work/HANDOFFS/WI-001.md",
        "federal/executive/services/requirements.lock",
    ],
)
def test_سجلّاتُ_الطبقةِ_والمخرجاتُ_المولَّدةُ_معفاةٌ_من_الحجز(path: str) -> None:
    assert gate.requires_claim(path) is False


@pytest.mark.parametrize(
    "path",
    [
        "core/constitutional_engine/engine.py",
        "tools/governance/check_work_governance.py",
        ".github/workflows/ci.yml",
        "docs/audit/PHASE_E_ROADMAP.md",
    ],
)
def test_الإعفاءُ_لا_يتوسَّعُ_إلى_العملِ_الحقيقيّ(path: str) -> None:
    assert gate.requires_claim(path) is True


def test_قيدُ_سجلٍّ_مع_بندٍ_مفتوحٍ_يسقط(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """واجبُ ما بعدَ الدمج: من قيَّدَ عملَه أغلقَ بندَه في الالتزامِ نفسِه."""
    row = ACTIVE_ROW.replace("| — | خطوةٌ واحدة | — |", "| — | خطوةٌ واحدة | W-001 |")
    repo = _mkrepo(tmp_path, active_rows=row)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    _stage(repo, gate.LEDGER_PATH, "| W-000 | تأسيس |\n| W-001 | عملٌ مُقيَّد |\n")
    assert "POST_MERGE_NOT_CLOSED" in _kinds()


def test_قيدُ_سجلٍّ_مع_بندٍ_مُغلَقٍ_يمرُّ(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    row = ACTIVE_ROW.replace("IN_PROGRESS", "CLOSED").replace(
        "| — | خطوةٌ واحدة | — |", "| — | خطوةٌ واحدة | W-001 |"
    )
    repo = _mkrepo(tmp_path, active_rows=row)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    _stage(repo, gate.LEDGER_PATH, "| W-000 | تأسيس |\n| W-001 | عملٌ مُقيَّد |\n")
    assert "POST_MERGE_NOT_CLOSED" not in _kinds()


def test_انتقالُ_حالةٍ_ممنوعٌ_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """`IN_PROGRESS → CLOSED` يتجاوزُ المراجعةَ فيسقط."""
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    body = (repo / gate.ACTIVE_PATH).read_text(encoding="utf-8")
    _stage(
        repo,
        gate.ACTIVE_PATH,
        body.replace("IN_PROGRESS", "CLOSED").replace(
            "| — | خطوةٌ واحدة | — |", "| — | خطوةٌ واحدة | W-001 |"
        ),
    )
    assert "ILLEGAL_TRANSITION" in _kinds()


def test_انتقالٌ_مشروعٌ_لا_يُرصَد(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    body = (repo / gate.ACTIVE_PATH).read_text(encoding="utf-8")
    _stage(repo, gate.ACTIVE_PATH, body.replace("IN_PROGRESS", "IN_REVIEW"))
    assert "ILLEGAL_TRANSITION" not in _kinds()


def test_آلةُ_الحالاتِ_مُغلَقةٌ_على_نفسِها() -> None:
    """كلُّ حالةٍ في الرسمِ معروفةٌ، وكلُّ وجهةٍ حالةٌ معروفة — لا حالةَ يتيمة."""
    assert set(gate.LEGAL_TRANSITIONS) == set(gate.ALL_STATUSES)
    for source, targets in gate.LEGAL_TRANSITIONS.items():
        assert targets <= gate.ALL_STATUSES, source
    assert gate.LEGAL_TRANSITIONS["CLOSED"] == frozenset()
    assert gate.LEGAL_TRANSITIONS["CANCELLED"] == frozenset()


# ── وضعُ الإبلاغ ─────────────────────────────────────────────────────────────


def test_وضعُ_الإبلاغِ_يُعلِنُ_ولا_يُسقِط(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """قبلَ اعتمادِ الخارطةِ تُبلِغُ البوّابةُ ولا تُوقِفُ عملًا (§ 16)."""
    repo = _mkrepo(tmp_path)
    monkeypatch.setattr(gate, "REPO_ROOT", repo)
    _stage(repo, "core/other.py", "y = 1\n")
    monkeypatch.setattr(sys, "argv", ["gate", "--staged", "--advisory"])
    assert gate.main() == 0
    monkeypatch.setattr(sys, "argv", ["gate", "--staged"])
    assert gate.main() == 1
