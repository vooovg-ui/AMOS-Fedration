"""
اختبارات W-032: مالكٌ واحدٌ لسجلَّي الأدواتِ والوكلاءِ · والبوّابةُ وسيطٌ
الهدف: إثباتُ أنَّ ما كُتِبَ من البوّابةِ العامّةِ يُقرأُ من الخدمةِ المالكةِ ومن
       قاعدةِ البياناتِ، وأنَّ الإدامةَ لم تُصبح توزيعًا، وأنَّ الحدودَ مُعلَنة.
النطاق: services/api-gateway · services/tool-registry · common/persistent
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-23
بأيِّ سلطةٍ: حسمُ المالكِ Q-39 (ب) بتاريخ 2026-08-23 — «tool-registry يملكُ ·
             api-gateway وسيطٌ · فلا كاتبانِ متنافسانِ».
"""

from __future__ import annotations

import uuid
from pathlib import Path

from fastapi.testclient import TestClient
from sqlalchemy import inspect

from amos_federation.common.auth import create_access_token
from amos_federation.common.database import (
    _W032_ADDED_COLUMNS,
    AgentModel,
    ToolModel,
    ensure_added_columns,
    get_engine,
    get_session_factory,
)
from amos_federation.common.persistent import (
    GATEWAY_DECLARED_AGENT_STATUS,
    PersistentAgentStore,
    PersistentToolStore,
)
from amos_federation.services.api_gateway import main as gateway
from amos_federation.services.executive_core.agent_identity import (
    OUT_OF_SERVICE_STATES,
    AgentLifecycleState,
)
from amos_federation.services.executive_core.dispatcher import EMPLOYABLE_STATUSES
from amos_federation.services.tool_registry import main as owner

_SCOPES = ["agents:read", "agents:write", "tools:read", "tools:write"]
AUTH_HEADERS = {"Authorization": f"Bearer {create_access_token('tester', _SCOPES)}"}

gateway_client = TestClient(gateway.app)
owner_client = TestClient(owner.app)


def _uid(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:10]}"


# ---------------------------------------------------------------------------
# 1) المالِكُ واحدٌ: ما يُكتَبُ من البوّابةِ يُقرأُ من الخدمةِ المالكة
# ---------------------------------------------------------------------------


def test_agent_registered_via_gateway_is_visible_from_owning_service() -> None:
    """بيانُ وكيلٍ سُجِّلَ من البوّابةِ يُقرأُ من `tool-registry` — لا قاموسانِ."""
    agent_id = _uid("agent")
    payload = {
        "agent_id": agent_id,
        "agent_type": "analyst",
        "domain": "finance",
        "name": "محلِّلُ الميزانِ",
        "description": "بيانٌ مُسجَّلٌ في اختبارِ W-032",
        "permissions": ["read:reports"],
    }
    created = gateway_client.post("/v1/agents", json=payload, headers=AUTH_HEADERS)
    assert created.status_code == 201, created.text

    fetched = owner_client.get(f"/v1/agents/{agent_id}", headers=AUTH_HEADERS)
    assert fetched.status_code == 200, fetched.text
    body = fetched.json()
    # أمانةُ البيانِ: كلُّ حقلٍ أُعلِنَ يُقرأُ كما أُعلِن — لا قيمةً مُختلَقة.
    assert body["agent_type"] == "analyst"
    assert body["domain"] == "finance"
    assert body["name"] == "محلِّلُ الميزانِ"
    assert body["description"] == "بيانٌ مُسجَّلٌ في اختبارِ W-032"
    assert body["permissions"] == ["read:reports"]

    listed = owner_client.get("/v1/agents", headers=AUTH_HEADERS)
    assert listed.status_code == 200
    assert agent_id in {item["agent_id"] for item in listed.json()}


def test_tool_registered_via_gateway_is_visible_from_owning_service() -> None:
    """بيانُ أداةٍ سُجِّلَ من البوّابةِ يُقرأُ من المالكِ بكلِّ حقولِه."""
    tool_id = _uid("tool")
    payload = {
        "tool_id": tool_id,
        "name": f"name-{tool_id}",
        "version": "3.1.4",
        "risk_level": "critical",
        "input_schema": {"type": "object", "required": ["q"]},
        "output_schema": {"type": "array"},
    }
    created = gateway_client.post("/v1/tools", json=payload, headers=AUTH_HEADERS)
    assert created.status_code == 201, created.text

    fetched = owner_client.get(f"/v1/tools/{tool_id}", headers=AUTH_HEADERS)
    assert fetched.status_code == 200, fetched.text
    body = fetched.json()
    # قبلَ W-032 كانت القراءةُ تُعيدُ `1.0.0` و`low` وقاموسَينِ فارغَينِ دائمًا:
    # أي أداةٌ خطرةٌ تُقرأُ آمنةً. هذا الحرسُ يُسقِطُ رجوعَ ذلك.
    assert body["version"] == "3.1.4"
    assert body["risk_level"] == "critical"
    assert body["input_schema"] == {"type": "object", "required": ["q"]}
    assert body["output_schema"] == {"type": "array"}


def test_gateway_reads_tools_from_owner_including_seeded_ones() -> None:
    """`GET /v1/tools` في البوّابةِ يقرأُ من جدولِ المالكِ لا من فراغ."""
    response = gateway_client.get("/v1/tools", headers=AUTH_HEADERS)
    assert response.status_code == 200
    ids = {item["tool_id"] for item in response.json()}
    assert "sql_query" in ids


def test_registered_manifest_reaches_the_database_row_itself() -> None:
    """الكتابةُ تصلُ الجدولَ نفسَه — لا طبقةَ ذاكرةٍ تُقلِّدُ الإدامة."""
    agent_id = _uid("agent-db")
    tool_id = _uid("tool-db")
    gateway_client.post(
        "/v1/agents",
        json={
            "agent_id": agent_id,
            "agent_type": "worker",
            "domain": "ops",
            "name": "عاملٌ",
            "permissions": [],
        },
        headers=AUTH_HEADERS,
    )
    gateway_client.post(
        "/v1/tools",
        json={
            "tool_id": tool_id,
            "name": f"name-{tool_id}",
            "version": "9.9.9",
            "risk_level": "high",
            "input_schema": {},
            "output_schema": {},
        },
        headers=AUTH_HEADERS,
    )
    session = get_session_factory()()
    try:
        agent_row = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        tool_row = session.query(ToolModel).filter(ToolModel.id == tool_id).first()
        assert agent_row is not None, "بيانُ الوكيلِ لم يصلْ جدولَ `agents`"
        assert tool_row is not None, "بيانُ الأداةِ لم يصلْ جدولَ `tools`"
        assert agent_row.status == GATEWAY_DECLARED_AGENT_STATUS
        assert tool_row.version == "9.9.9"
        assert tool_row.risk_level == "high"
    finally:
        session.close()


# ---------------------------------------------------------------------------
# 2) مُغلَقٌ عندَ الفشل: الإدامةُ ليست توزيعًا
# ---------------------------------------------------------------------------


def test_declared_agent_is_not_employable_by_the_dispatcher() -> None:
    """وكيلٌ سُجِّلَ من الواجهةِ العامّةِ لا يدخلُ مُرشَّحي الموزِّعِ.

    وهذا **قصدٌ** لا نقص: قبلَ W-032 كان البيانُ يقفُ في قاموسٍ لا يقرأُه
    الموزِّع، فلم يكن نادي الواجهةِ يملكُ سلطةَ التوزيع. ولمّا صارَ البيانُ
    دائمًا في جدولِ الهويّةِ نفسِه، كان لا بدَّ من حالةٍ غيرِ قابلةٍ للتوظيفِ
    حتى لا تُمنَحَ تلك السلطةُ ضمنًا. ومن يريدُ منحَها فليَحسِمْ Q-41.
    """
    assert GATEWAY_DECLARED_AGENT_STATUS not in EMPLOYABLE_STATUSES
    assert GATEWAY_DECLARED_AGENT_STATUS in OUT_OF_SERVICE_STATES


def test_declared_state_constant_matches_the_lifecycle_enum() -> None:
    """قيمةُ `common` وقيمةُ دورةِ الحياةِ نصٌّ واحدٌ — لا نسختانِ تفترقان.

    `common/` لا تستوردُ من `services/` (اتّجاهُ الاعتمادِ واحدٌ)، فالنصُّ
    مكتوبٌ مرّتينِ ضرورةً، وهذا الحرسُ هو ما يمنعُ افتراقَهما صامتًا.
    """
    assert AgentLifecycleState.DECLARED.value == GATEWAY_DECLARED_AGENT_STATUS


def test_registering_an_existing_agent_does_not_demote_it() -> None:
    """نداءُ تسجيلٍ لا يُخفِّضُ حالةَ وكيلٍ قائمٍ — فالواجهةُ ليست بابَ عزلٍ."""
    agent_id = _uid("agent-live")
    session = get_session_factory()()
    try:
        session.add(
            AgentModel(
                id=agent_id,
                name="وكيلٌ عاملٌ",
                role="worker",
                status="active",
                permissions=[],
                allowed_tools=[],
            )
        )
        session.commit()
    finally:
        session.close()

    response = gateway_client.post(
        "/v1/agents",
        json={
            "agent_id": agent_id,
            "agent_type": "worker",
            "domain": "ops",
            "name": "اسمٌ مُحدَّثٌ",
            "permissions": ["x"],
        },
        headers=AUTH_HEADERS,
    )
    assert response.status_code == 201

    session = get_session_factory()()
    try:
        row = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        assert row is not None
        assert row.status == "active", "نداءُ التسجيلِ خفَّضَ حالةَ وكيلٍ عاملٍ"
        assert row.name == "اسمٌ مُحدَّثٌ"
    finally:
        session.close()


# ---------------------------------------------------------------------------
# 3) حدودٌ مُعلَنة: لا كاتبَ ثانيًا · وقيدُ الاسمِ الفريدِ يُقالُ بـ409
# ---------------------------------------------------------------------------


def test_gateway_source_declares_no_local_registry_dicts() -> None:
    """لا قاموسَ وكلاءٍ أو أدواتٍ في مصدرِ البوّابةِ — الحرسُ على الشِفرةِ نفسِها."""
    source = Path(gateway.__file__).read_text(encoding="utf-8")
    forbidden = (
        "agents: dict[str, AgentManifestModel] = {}",
        "tools: dict[str, ToolManifestModel] = {}",
    )
    for line in forbidden:
        assert line not in source, f"عادَ كاتبٌ متنافسٌ إلى البوّابةِ: {line}"
    assert not hasattr(gateway, "agents")
    assert not hasattr(gateway, "tools")


def test_gateway_and_owner_share_the_same_store_objects() -> None:
    """الوساطةُ تفويضٌ إلى مخزنِ المالكِ نفسِه لا نسخةٌ موازية."""
    assert isinstance(owner.agent_store, PersistentAgentStore)
    assert isinstance(owner.tool_store, PersistentToolStore)
    assert owner.STORE_DURABILITY == {
        "tool_store": "DURABLE_CONTROL",
        "agent_store": "DURABLE_CONTROL",
    }


def test_duplicate_tool_name_returns_409_not_500() -> None:
    """قيدُ `tools.name` الفريدُ يُترجَمُ إلى `409` معَ ذِكرِ السببِ.

    وهذا تغييرُ عقدٍ مُعلَنٌ: أداتانِ باسمٍ واحدٍ ومعرّفَينِ مختلفَينِ كانتا
    تُقبَلانِ في القاموسِ المتطايرِ، والجدولُ المالكُ لا يقبلُهما.
    """
    shared_name = f"shared-{uuid.uuid4().hex[:8]}"
    first = gateway_client.post(
        "/v1/tools",
        json={
            "tool_id": _uid("tool-a"),
            "name": shared_name,
            "version": "1.0.0",
            "risk_level": "low",
            "input_schema": {},
            "output_schema": {},
        },
        headers=AUTH_HEADERS,
    )
    assert first.status_code == 201, first.text

    second = gateway_client.post(
        "/v1/tools",
        json={
            "tool_id": _uid("tool-b"),
            "name": shared_name,
            "version": "1.0.0",
            "risk_level": "low",
            "input_schema": {},
            "output_schema": {},
        },
        headers=AUTH_HEADERS,
    )
    assert second.status_code == 409, second.text
    assert "tool-registry" in second.json()["detail"]


# ---------------------------------------------------------------------------
# 4) الهجرةُ والدالّةُ تُعلِنانِ نفسَ القائمةِ · والإضافةُ مُتكرِّرةُ الأمانِ
# ---------------------------------------------------------------------------


def test_added_columns_exist_and_function_is_idempotent() -> None:
    """`ensure_added_columns()` لا تُضيفُ شيئًا على قاعدةٍ مُهاجَرةٍ بالفعل."""
    inspector = inspect(get_engine())
    for table, columns in _W032_ADDED_COLUMNS.items():
        present = {column["name"] for column in inspector.get_columns(table)}
        for column_name in columns:
            assert column_name in present, f"عمودُ {table}.{column_name} غائبٌ"
    assert ensure_added_columns() == [], "الدالّةُ أضافت عمودًا على قاعدةٍ مُهاجَرةٍ"


def test_migration_file_declares_the_same_columns_as_the_function() -> None:
    """هجرةُ 015 والدالّةُ لا تفترقانِ — وإلّا هاجرَ PostgreSQL دونَ SQLite."""
    migration = (
        Path(__file__).resolve().parents[1] / "migrations" / "015_registry_ownership_w032.sql"
    )
    text = migration.read_text(encoding="utf-8")
    for table, columns in _W032_ADDED_COLUMNS.items():
        for column_name in columns:
            assert (
                f"ALTER TABLE {table} ADD COLUMN IF NOT EXISTS {column_name}" in text
            ), f"هجرةُ 015 لا تُعلِنُ {table}.{column_name}"


def test_pre_w032_rows_read_as_declared_contract_defaults() -> None:
    """صفٌّ بأعمدةٍ `NULL` (كُتِبَ قبلَ 015) يُقرأُ بقيمةِ العقدِ لا بانفجار."""
    tool_id = _uid("tool-legacy")
    session = get_session_factory()()
    try:
        session.add(
            ToolModel(
                id=tool_id,
                name=f"legacy-{tool_id}",
                description="",
                category="general",
                keywords=[],
                permissions_required=[],
            )
        )
        session.commit()
    finally:
        session.close()

    manifest = owner.tool_store.get(tool_id)
    assert manifest is not None
    assert manifest.version == "1.0.0"
    assert manifest.risk_level == "low"
    assert manifest.input_schema == {}
