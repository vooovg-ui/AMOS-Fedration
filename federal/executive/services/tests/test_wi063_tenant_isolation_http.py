"""
AMOS-Federation — عزلُ المستأجرينَ عندَ نقاطِ HTTP في المخازنِ الدائمة (WI-063 · DISC-089)
الهدف: أن يُثبَتَ **بالنداءِ لا بالتصريحِ** أنَّ رمزًا موقَّعًا لمستأجرٍ لا يقرأُ وكلاءَ
       مستأجرٍ آخرَ ولا خبراتِه ولا ذاكرتَه، ولا يكتبُ فوقَها — على SQLite دائمًا،
       وعلى PostgreSQL الحقيقيِّ حينَ يُفعَّلُ صراحةً.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-10 (WI-063)
تاريخ آخر تعديل: 2026-10-10 (WI-063)

## ما قِيسَ قبلَ هذا الملفّ (‏DISC-089 · PostgreSQL 18.6 محلّيّ)

رمزٌ لـ`tenant-b` قرأَ عبرَ التطبيقاتِ نفسِها: وكلاءَ `tenant-a` من `api_gateway` و
`tool_registry` و`control_console`، وخبراتِه قائمةً وبالمعرّفِ مع `outcome`، وذاكرتَه
بالمفتاح؛ وكانَ `POST /v1/memory/store` بمفتاحِ غيرِه يكتبُ فوقَه وينقلُ ملكيّتَه.

## القاعدةُ المُختبَرة — وليست جديدة

`tenant_matches` في `common/principal.py`: `federal` يعبرُ الحدود، والسياقُ بلا مستأجرٍ
نطاقُه `default` لا «الكلّ». ومورِدُ مستأجرٍ آخرَ يُقرَأُ `404` لا `403` فلا يُكشَفُ
وجودُه، ويُكتَبُ فوقَه `409` بلا ذِكرِ مالكِه.

## الاستثناءُ المقصود

`control_console` `GET /v1/agents` **فدراليٌّ بقرارِ المالك** (‏2026-10-10: «مع استثناء
control_console ليبقى فدراليًا»)، فاختبارُه هنا يُثبِتُ أنّه **لم يُقيَّد** — حتى لا يُقيِّدَه
تعديلٌ لاحقٌ بلا قرار، ولا يُقرَأَ هذا الملفُّ دعوى عزلٍ له.
"""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass
from typing import TYPE_CHECKING

import pytest
from fastapi.testclient import TestClient

from amos_federation.common.auth import create_access_token
from amos_federation.common.database import (
    AgentModel,
    ExperienceModel,
    MemoryModel,
    get_session_factory,
    init_db,
)
from amos_federation.common.persistent import (
    PersistentExperienceStore,
    PersistentMemoryStore,
)
from amos_federation.common.principal import (
    TenantIsolationError,
    tenant_scope,
)

if TYPE_CHECKING:
    from collections.abc import Iterator


@dataclass(frozen=True)
class Seed:
    a: str  # لاحقةُ صفوفِ tenant-a
    b: str  # لاحقةُ صفوفِ tenant-b
    tenant_a: str
    tenant_b: str


@pytest.fixture(params=["sqlite", "postgres"])
def database(request: pytest.FixtureRequest) -> Iterator[str]:
    """كلُّ اختبارٍ مرّتين: SQLite دائمًا، وPostgreSQL إن فُعِّلَ (‏وإلّا يُتخطّى بسببِه)."""
    yield request.getfixturevalue("sqlite_url" if request.param == "sqlite" else "postgres_url")


@pytest.fixture
def seed(database: str) -> Iterator[Seed]:
    init_db()
    run = uuid.uuid4().hex[:8]
    s = Seed(a=f"a-{run}", b=f"b-{run}", tenant_a=f"tenant-a-{run}", tenant_b=f"tenant-b-{run}")
    session = get_session_factory()()
    try:
        for suffix, tenant in ((s.a, s.tenant_a), (s.b, s.tenant_b)):
            session.add(
                AgentModel(
                    id=f"agent-{suffix}",
                    name=f"agent of {tenant}",
                    role="worker",
                    tenant_id=tenant,
                )
            )
            session.add(
                ExperienceModel(
                    id=f"exp-{suffix}",
                    type="success",
                    agent_id=f"agent-{suffix}",
                    outcome={"secret": f"outcome of {tenant}"},
                    tenant_id=tenant,
                )
            )
            session.add(
                MemoryModel(
                    key=f"mem-{suffix}",
                    value=json.dumps({"content": f"memory of {tenant}"}),
                    tenant_id=tenant,
                )
            )
        session.commit()
    finally:
        session.close()
    yield s
    # حذفُ ما أنشأَه هذا الاختبارُ وحدَه بمعرّفاتِه — لا مسحَ لجدول.
    session = get_session_factory()()
    try:
        agent_ids = [f"agent-{s.a}", f"agent-{s.b}", f"agent-new-{s.b}"]
        session.query(ExperienceModel).filter(
            ExperienceModel.id.in_([f"exp-{s.a}", f"exp-{s.b}"])
        ).delete(synchronize_session=False)
        session.query(MemoryModel).filter(MemoryModel.key.in_([f"mem-{s.a}", f"mem-{s.b}"])).delete(
            synchronize_session=False
        )
        session.query(AgentModel).filter(AgentModel.id.in_(agent_ids)).delete(
            synchronize_session=False
        )
        session.commit()
    finally:
        session.close()


def _headers(tenant: str | None) -> dict[str, str]:
    token = create_access_token(f"user-{uuid.uuid4().hex[:6]}", ["*"], tenant_id=tenant)
    return {"Authorization": f"Bearer {token}"}


def _client(service: str) -> TestClient:
    from importlib import import_module

    return TestClient(import_module(f"amos_federation.services.{service}.main").app)


def _agent_ids(body: list[dict]) -> set[str]:
    return {item["agent_id"] for item in body}


# ── الوكلاء ──────────────────────────────────────────────────────────────


@pytest.mark.parametrize("service", ["api_gateway", "tool_registry"])
def test_agent_list_is_scoped_to_the_caller_tenant(service: str, seed: Seed) -> None:
    r = _client(service).get("/v1/agents", headers=_headers(seed.tenant_b))
    assert r.status_code == 200
    ids = _agent_ids(r.json())
    assert f"agent-{seed.b}" in ids
    assert f"agent-{seed.a}" not in ids


@pytest.mark.parametrize("service", ["api_gateway", "tool_registry"])
def test_federal_context_still_crosses_tenants(service: str, seed: Seed) -> None:
    r = _client(service).get("/v1/agents", headers=_headers("federal"))
    assert r.status_code == 200
    assert {f"agent-{seed.a}", f"agent-{seed.b}"} <= _agent_ids(r.json())


def test_agent_of_another_tenant_reads_as_not_found(seed: Seed) -> None:
    client = _client("tool_registry")
    assert (
        client.get(f"/v1/agents/agent-{seed.a}", headers=_headers(seed.tenant_b)).status_code == 404
    )
    assert (
        client.get(f"/v1/agents/agent-{seed.b}", headers=_headers(seed.tenant_b)).status_code == 200
    )


@pytest.mark.parametrize("service", ["api_gateway", "tool_registry"])
def test_register_cannot_overwrite_another_tenants_agent(service: str, seed: Seed) -> None:
    manifest = {"agent_id": f"agent-{seed.a}", "agent_type": "worker", "name": "hijacked"}
    r = _client(service).post("/v1/agents", json=manifest, headers=_headers(seed.tenant_b))
    assert r.status_code == 409
    assert seed.tenant_a not in r.text  # لا يُكشَفُ المالك
    session = get_session_factory()()
    try:
        row = session.get(AgentModel, f"agent-{seed.a}")
        assert row.name == f"agent of {seed.tenant_a}"
        assert row.tenant_id == seed.tenant_a
    finally:
        session.close()


def test_new_agent_lands_in_the_caller_tenant(seed: Seed) -> None:
    manifest = {"agent_id": f"agent-new-{seed.b}", "agent_type": "worker", "name": "new"}
    r = _client("tool_registry").post("/v1/agents", json=manifest, headers=_headers(seed.tenant_b))
    assert r.status_code == 201
    session = get_session_factory()()
    try:
        assert session.get(AgentModel, f"agent-new-{seed.b}").tenant_id == seed.tenant_b
    finally:
        session.close()


def test_control_console_remains_federal_by_owner_decision(seed: Seed) -> None:
    """استثناءٌ مقصودٌ بقرارِ المالك — يُثبَتُ أنّه **لم يُقيَّد**، لا أنّه معزول."""
    r = _client("control_console").get("/v1/agents", headers=_headers(seed.tenant_b))
    assert r.status_code == 200
    assert {f"agent-{seed.a}", f"agent-{seed.b}"} <= {item["agent_id"] for item in r.json()}


# ── الخبرات ─────────────────────────────────────────────────────────────


def test_experiences_list_get_and_stats_are_scoped(seed: Seed) -> None:
    client = _client("evaluation")
    h = _headers(seed.tenant_b)
    listed = {e["experience_id"] for e in client.get("/v1/experiences", headers=h).json()}
    assert f"exp-{seed.b}" in listed and f"exp-{seed.a}" not in listed
    assert client.get(f"/v1/experiences/exp-{seed.a}", headers=h).status_code == 404
    mine = client.get(f"/v1/experiences/exp-{seed.b}", headers=h)
    assert mine.status_code == 200 and mine.json()["outcome"]["secret"].endswith(seed.tenant_b)
    stats = client.get("/v1/experiences/stats/summary", headers=h).json()
    assert stats["total"] == 1
    run = client.post("/v1/evaluations/run", headers=h).json()
    assert run["total_experiences"] == 1


def test_experience_record_lands_in_the_caller_tenant_and_cannot_overwrite() -> None:
    """طبقةُ المخزنِ مباشرةً — وهي التي تُنادى من `POST /v1/experiences`."""
    init_db()
    store = PersistentExperienceStore()
    run = uuid.uuid4().hex[:8]
    exp_id = f"exp-rec-{run}"
    store.record({"experience_id": exp_id, "type": "success"}, tenant_id=f"t1-{run}")
    try:
        assert store.get(exp_id, tenant_id=f"t1-{run}") is not None
        assert store.get(exp_id, tenant_id=f"t2-{run}") is None
        with pytest.raises(TenantIsolationError):
            store.record({"experience_id": exp_id, "type": "failure"}, tenant_id=f"t2-{run}")
        assert store.get(exp_id, tenant_id=f"t1-{run}")["type"] == "success"
    finally:
        session = get_session_factory()()
        try:
            session.query(ExperienceModel).filter(ExperienceModel.id == exp_id).delete()
            session.commit()
        finally:
            session.close()


# ── الذاكرة ─────────────────────────────────────────────────────────────


def test_memory_get_and_stats_are_scoped(seed: Seed) -> None:
    client = _client("memory_service")
    h = _headers(seed.tenant_b)
    assert client.get(f"/v1/memory/mem-{seed.a}", headers=h).status_code == 404
    assert client.get(f"/v1/memory/mem-{seed.b}", headers=h).status_code == 200
    assert client.get("/v1/memory/stats/summary", headers=h).json()["total_items"] == 1


def test_memory_store_cannot_overwrite_another_tenants_key(seed: Seed) -> None:
    client = _client("memory_service")
    r = client.post(
        "/v1/memory/store",
        json={"key": f"mem-{seed.a}", "value": {"content": "hijacked"}},
        headers=_headers(seed.tenant_b),
    )
    assert r.status_code == 409
    assert seed.tenant_a not in r.text
    row = PersistentMemoryStore().get(f"mem-{seed.a}", tenant_id=seed.tenant_a)
    assert row is not None and "hijacked" not in row["value"]


# ── القاعدة ─────────────────────────────────────────────────────────────


def test_tenant_scope_is_tenant_matches_as_a_predicate() -> None:
    class _Ctx:
        def __init__(self, tenant: str | None, trusted: bool) -> None:
            self.tenant_id = tenant
            self.is_trusted = trusted

    assert tenant_scope(_Ctx("tenant-x", True)) == "tenant-x"
    assert tenant_scope(_Ctx(None, True)) == "default"
    assert tenant_scope(_Ctx("federal", True)) is None
    with pytest.raises(TenantIsolationError):
        tenant_scope(_Ctx("tenant-x", False))
