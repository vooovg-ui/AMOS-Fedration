"""
الهدف: إثباتُ أنَّ الجردَ المُعلَنَ في `ARCHITECTURE.md` صارَ **مقيسًا** لا مقروءًا:
       تُقرأُ أرقامُه من الوثيقةِ نفسِها، ويُرصَدُ تناقضُ المجموعِ مع تفصيلِه،
       ويُرصَدُ افتراقُه عن قياسٍ حيٍّ، ويُرفَضُ الحكمُ عندَ غيابِ مصدرِ القياسِ
       رفضًا مُصنَّفًا برمزٍ يُميِّزُه من الافتراق.
النطاق: `tools/governance/schema_inventory_drift.py` وحدَه — قراءةُ المُعلَنِ
        ومقابلتُه بحِملٍ محفوظٍ. ولا يُقاسُ هنا شكلُ مخطَّطٍ ولا عمودٌ ولا فهرسٌ:
        الحدُّ مُعلَنٌ في ترويسةِ الأداةِ وفي قسمِ الجردِ من `ARCHITECTURE.md`.
المالك: tests/governance
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-08-27

لماذا هذا الاختبار
------------------
كانَ في `ARCHITECTURE.md` جردٌ مقيسٌ بتاريخِه وحدُّ صدقٍ مكتوبٌ يقولُ: «لا بوّابةَ
في CI تحرسُ هذا القسم». فما كانَ في الشجرةِ شيءٌ يقرأُ تلك الأرقامَ أصلًا: لو
تناقضَ المجموعُ مع تفصيلِه، أو صارَ تاريخُ القياسِ في المستقبلِ، أو افترقَ الجردُ
عن القاعدةِ — لبقيَ النصُّ مُطمئنًّا. ويُثبَّتُ هنا أنَّ الأداةَ تسقُطُ في كلٍّ من
هذه، وأنَّها **لا تدَّعي مطابقةً** حينَ لا مصدرَ قياسٍ لها.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "governance" / "schema_inventory_drift.py"


def _load_tool():
    spec = importlib.util.spec_from_file_location(
        "schema_inventory_drift_w055", TOOL_PATH
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    # يُسجَّلُ قبلَ التنفيذِ لأنَّ `dataclasses` تقرأُ وحدةَ الصنفِ من `sys.modules`.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


tool = _load_tool()


DOC = """# عمارةٌ

المشروع متصل بقاعدة بيانات Supabase (PostgreSQL **17.6**).

### المقيسُ في 2026-08-21

| المقياس | القيمة المقيسة |
|---|---|
| جداولُ `public` | **86** |
| جداولُ المخطَّطاتِ غيرِ النظاميّةِ كلِّها | **122** (`public` 86 · `auth` 23 · `storage` 8 · `realtime` 3 · `supabase_migrations` 1 · `vault` 1) |
| صفوفُ `agent_population` | **5,116** |
| صفوفُ `event_store` | **1,027** |
| صفوفُ `audit_entries` | **71** |
"""

LIVE = {
    "measured_at": "2026-08-27T15:12:52Z",
    "server_version": "17.6",
    "schemas": [
        {"table_schema": "public", "tables": 86},
        {"table_schema": "auth", "tables": 23},
        {"table_schema": "storage", "tables": 8},
        {"table_schema": "realtime", "tables": 3},
        {"table_schema": "supabase_migrations", "tables": 1},
        {"table_schema": "vault", "tables": 1},
    ],
    "rows": {"agent_population": 5116, "event_store": 1027, "audit_entries": 71},
}


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    (tmp_path / "ARCHITECTURE.md").write_text(DOC, encoding="utf-8")
    return tmp_path


# ---------------------------------------------------------------------------
# قراءةُ المُعلَنِ — من الوثيقةِ لا من الذاكرة
# ---------------------------------------------------------------------------


def test_الجردُ_المُعلَنُ_يُقرأُ_رقمًا_لا_نصًّا(repo: Path) -> None:
    declared = tool.read_declared(repo)
    assert declared.measured_on == date(2026, 8, 21)
    assert declared.version == "17.6"
    assert declared.schemas["public"] == 86
    assert declared.schemas["supabase_migrations"] == 1
    assert declared.breakdown_total == 122
    assert declared.breakdown_sum == 122
    assert declared.rows == {
        "agent_population": 5116,
        "event_store": 1027,
        "audit_entries": 71,
    }


def test_غيابُ_قسمِ_الجردِ_رفضٌ_لا_نجاحٌ(tmp_path: Path) -> None:
    (tmp_path / "ARCHITECTURE.md").write_text("# عمارةٌ بلا جرد\n", encoding="utf-8")
    with pytest.raises(tool.MeasurementRefused):
        tool.read_declared(tmp_path)


def test_غيابُ_الوثيقةِ_نفسِها_رفضٌ_مُعلَن(tmp_path: Path) -> None:
    with pytest.raises(tool.MeasurementRefused):
        tool.read_declared(tmp_path)


def test_قسمٌ_بلا_صفِّ_مخطَّطٍ_يُرفَضُ_ولا_يُحكَمُ_على_فراغ(tmp_path: Path) -> None:
    (tmp_path / "ARCHITECTURE.md").write_text(
        "# عمارةٌ\n\n### المقيسُ في 2026-08-21\n\nلا جدولَ هنا.\n", encoding="utf-8"
    )
    with pytest.raises(tool.MeasurementRefused):
        tool.read_declared(tmp_path)


# ---------------------------------------------------------------------------
# استقامةُ المُعلَنِ في نفسِه — تُقاسُ بلا قاعدةٍ ولا سرّ
# ---------------------------------------------------------------------------


def test_الجردُ_المستقيمُ_لا_مخالفةَ_فيه(repo: Path) -> None:
    contract = tool.check_contract(tool.read_declared(repo), date(2026, 8, 27), 30)
    assert contract.violations == []


def test_مجموعٌ_يُخالِفُ_تفصيلَه_يُرصَد(tmp_path: Path) -> None:
    (tmp_path / "ARCHITECTURE.md").write_text(
        DOC.replace("**122**", "**130**"), encoding="utf-8"
    )
    contract = tool.check_contract(tool.read_declared(tmp_path), date(2026, 8, 27), 30)
    assert any(v.startswith("INVENTORY_SUM_MISMATCH") for v in contract.violations)


def test_تاريخُ_قياسٍ_في_المستقبلِ_يُرصَد(repo: Path) -> None:
    contract = tool.check_contract(tool.read_declared(repo), date(2026, 8, 20), 30)
    assert any(v.startswith("INVENTORY_DATE_IN_FUTURE") for v in contract.violations)


def test_جردٌ_بلا_عدَّادِ_صفوفٍ_يُرصَد(tmp_path: Path) -> None:
    trimmed = "\n".join(line for line in DOC.splitlines() if "صفوفُ" not in line)
    (tmp_path / "ARCHITECTURE.md").write_text(trimmed + "\n", encoding="utf-8")
    contract = tool.check_contract(tool.read_declared(tmp_path), date(2026, 8, 27), 30)
    assert any(v.startswith("INVENTORY_NO_ROW_METRIC") for v in contract.violations)


def test_التقادُمُ_يُعلَنُ_ملاحظةً_ولا_يُسقِطُ_بنفسِه(repo: Path) -> None:
    contract = tool.check_contract(tool.read_declared(repo), date(2026, 12, 31), 30)
    assert any(n.startswith("INVENTORY_STALE") for n in contract.notes)
    assert contract.violations == []


# ---------------------------------------------------------------------------
# المطابقةُ بالمقيسِ — والافتراقُ يُسمّى
# ---------------------------------------------------------------------------


def test_مطابقةٌ_تامّةٌ_بلا_افتراق(repo: Path) -> None:
    verdicts = tool.compare(tool.read_declared(repo), LIVE)
    assert verdicts
    assert [v for v in verdicts if v.is_drift] == []


def test_جدولٌ_زائدٌ_في_القاعدةِ_افتراقٌ_في_المخطَّطِ_والمجموع(repo: Path) -> None:
    live = json.loads(json.dumps(LIVE))
    live["schemas"][0]["tables"] = 87
    drifted = {
        v.metric for v in tool.compare(tool.read_declared(repo), live) if v.is_drift
    }
    assert "schema:public" in drifted
    assert "schemas:total" in drifted


def test_مخطَّطٌ_غيرُ_مُعلَنٍ_يُسمّى_UNDECLARED(repo: Path) -> None:
    live = json.loads(json.dumps(LIVE))
    live["schemas"].append({"table_schema": "graphql", "tables": 2})
    states = {v.metric: v.state for v in tool.compare(tool.read_declared(repo), live)}
    assert states["schema:graphql"] == "UNDECLARED"


def test_مخطَّطٌ_مُعلَنٌ_غائبٌ_عن_القاعدةِ_يُسمّى_MISSING_LIVE(repo: Path) -> None:
    live = json.loads(json.dumps(LIVE))
    live["schemas"] = [s for s in live["schemas"] if s["table_schema"] != "vault"]
    states = {v.metric: v.state for v in tool.compare(tool.read_declared(repo), live)}
    assert states["schema:vault"] == "MISSING_LIVE"


def test_عددُ_صفوفٍ_مفترِقٌ_يُرصَد(repo: Path) -> None:
    live = json.loads(json.dumps(LIVE))
    live["rows"]["event_store"] = 2048
    drifted = {
        v.metric for v in tool.compare(tool.read_declared(repo), live) if v.is_drift
    }
    assert "rows:event_store" in drifted


def test_إصدارُ_محرِّكٍ_مفترِقٌ_يُرصَد(repo: Path) -> None:
    live = json.loads(json.dumps(LIVE))
    live["server_version"] = "16.4"
    drifted = {
        v.metric for v in tool.compare(tool.read_declared(repo), live) if v.is_drift
    }
    assert "server_version" in drifted


@pytest.mark.parametrize(
    "payload",
    [
        "ليس كائنًا",
        {},
        {"schemas": []},
        {"schemas": [{"table_schema": "public"}]},
    ],
)
def test_حِملٌ_ناقصٌ_يُرفَضُ_ولا_يُقرأُ_مطابقةً(repo: Path, payload: object) -> None:
    with pytest.raises(tool.MeasurementRefused):
        tool.compare(tool.read_declared(repo), payload)


def test_القياسُ_الحيُّ_بلا_وصلِ_قاعدةٍ_رفضٌ_لا_صفرُ_افتراق() -> None:
    with pytest.raises(tool.MeasurementRefused):
        tool.measure_live("")


# ---------------------------------------------------------------------------
# رموزُ الخروجِ — الرفضُ يُميَّزُ من الافتراقِ ومن الاستقامة
# ---------------------------------------------------------------------------


def _run(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL_PATH), *args],
        capture_output=True,
        text=True,
        cwd=str(cwd or REPO_ROOT),
        check=False,
    )


def test_الفحصُ_على_المستودعِ_نفسِه_يمرُّ() -> None:
    done = _run(["--check"])
    assert done.returncode == 0, done.stdout + done.stderr


def test_المطابقةُ_على_حِملٍ_محفوظٍ_تمرُّ(tmp_path: Path) -> None:
    payload = tmp_path / "live.json"
    payload.write_text(json.dumps(LIVE, ensure_ascii=False), encoding="utf-8")
    done = _run(["--from-json", str(payload)])
    assert done.returncode == 0, done.stdout + done.stderr


def test_افتراقٌ_يُخرِجُ_بواحدٍ(tmp_path: Path) -> None:
    live = json.loads(json.dumps(LIVE))
    live["rows"]["audit_entries"] = 99
    payload = tmp_path / "live.json"
    payload.write_text(json.dumps(live, ensure_ascii=False), encoding="utf-8")
    done = _run(["--from-json", str(payload)])
    assert done.returncode == 1
    assert "rows:audit_entries" in done.stdout


def test_حِملٌ_غائبٌ_يُخرِجُ_باثنَينِ_لا_بواحد(tmp_path: Path) -> None:
    done = _run(["--from-json", str(tmp_path / "لا-وجود-له.json")])
    assert done.returncode == 2
    assert "مرفوض" in done.stderr


def test_بلا_وضعٍ_يُرفَضُ_الاستدعاء() -> None:
    done = _run([])
    assert done.returncode == 2 or "لا وضعَ" in (done.stderr + done.stdout)


def test_حِملُ_القياسِ_المكتوبُ_يحملُ_المُعلَنَ_والأحكامَ(tmp_path: Path) -> None:
    payload = tmp_path / "live.json"
    payload.write_text(json.dumps(LIVE, ensure_ascii=False), encoding="utf-8")
    out = tmp_path / "published.json"
    done = _run(["--from-json", str(payload), "--json", str(out)])
    assert done.returncode == 0, done.stdout + done.stderr
    written = json.loads(out.read_text(encoding="utf-8"))
    assert written["drift_count"] == 0
    assert written["declared"]["schemas"]["public"] == 86
    assert {v["metric"] for v in written["verdicts"]} >= {
        "schema:public",
        "schemas:total",
    }
