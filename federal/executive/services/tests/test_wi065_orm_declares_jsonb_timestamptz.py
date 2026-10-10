"""
AMOS-Federation — النموذجُ يُعلِنُ `jsonb` و`timestamptz` (WI-065 · DISC-088 (ب))
الهدف: أن يُثبَتَ أنَّ الأعمدةَ الـ22 التي كانت `JSON`/`DateTime` بلا منطقةٍ في النموذج
       صارت `jsonb`/`timestamptz` على PostgreSQL، وأنَّ ذلك **يُغيِّرُ السلوكَ** لا الاسمَ وحدَه:
       اللحظةُ المكتوبةُ بـ`datetime.now(UTC)` تُقرَأُ هي نفسُها ولو كانت منطقةُ الجلسةِ غيرَ UTC،
       ووثيقةُ JSON تقبلُ عاملَ الاحتواءِ `@>` الذي لا يقبلُه `json`.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-10 (WI-065)
تاريخ آخر تعديل: 2026-10-10 (WI-065)

## القرار

المالكُ في 2026-10-10: «غيّر نماذج ORM إلى JSONB وDateTime(timezone=True) ثم اختبرها» —
بعدَ أن حسمَ في DISC-088 (ب) أنَّ النموذجَ مصدرُ المخطّط. فالنموذجُ يُعلِنُ ما بنَتْه
الهجرةُ 001، ولا تُخفَّضُ الهجرة.

## لماذا الاختبارُ الحيُّ بمنطقةِ `Asia/Riyadh`

بـ`DateTime` بلا منطقةٍ يُرسَلُ الوقتُ الواعي فيُحوِّلُه PostgreSQL إلى وقتِ الجلسةِ المحلّيِّ
ثمَّ يُسقِطُ المنطقة؛ فيعودُ مُزاحًا ثلاثَ ساعاتٍ وبلا منطقة. فاختبارٌ بجلسةِ UTC لا يرى
الخلل — ولذا تُضبَطُ الجلسةُ هنا عمدًا على غيرِ UTC.
"""

from __future__ import annotations

import os
import uuid
from datetime import UTC, datetime

import pytest
from sqlalchemy.dialects import postgresql, sqlite

from amos_federation.common.database import (
    AgentModel,
    AuditEntryModel,
    Base,
    ExperienceModel,
    MemoryModel,
    ReviewModel,
    TaskModel,
    ToolModel,
)

#: الجداولُ السبعةُ التي بنَتْها 001 بـ`jsonb`/`timestamptz` وكانَ النموذجُ يُعلِنُها أضعف.
CORE_MODELS = (
    AgentModel,
    ToolModel,
    TaskModel,
    MemoryModel,
    ExperienceModel,
    ReviewModel,
    AuditEntryModel,
)

EXPECTED_JSONB = {
    "agents.permissions",
    "agents.allowed_tools",
    "tools.keywords",
    "tools.permissions_required",
    "tools.input_schema",
    "tools.output_schema",
    "tasks.plan",
    "tasks.result",
    "memories.keywords",
    "experiences.outcome",
    "experiences.provenance",
    "reviews.criteria",
    "audit_entries.details",
}
EXPECTED_TIMESTAMPTZ = {
    "agents.created_at",
    "agents.updated_at",
    "tools.created_at",
    "tasks.created_at",
    "tasks.updated_at",
    "memories.created_at",
    "experiences.created_at",
    "reviews.created_at",
    "audit_entries.created_at",
}


def _compiled(dialect) -> dict[str, str]:
    out: dict[str, str] = {}
    for model in CORE_MODELS:
        for col in model.__table__.columns:
            out[f"{model.__tablename__}.{col.name}"] = col.type.compile(dialect=dialect)
    return out


def test_core_columns_compile_to_jsonb_and_timestamptz_on_postgres() -> None:
    types = _compiled(postgresql.dialect())
    assert {k for k, v in types.items() if v == "JSONB"} == EXPECTED_JSONB
    assert {k for k, v in types.items() if v == "TIMESTAMP WITH TIME ZONE"} == EXPECTED_TIMESTAMPTZ
    assert not [k for k, v in types.items() if v in {"JSON", "TIMESTAMP WITHOUT TIME ZONE"}]


def test_the_same_columns_stay_portable_on_sqlite() -> None:
    """الاختبارُ والتطويرُ على SQLite: `JSON` و`DATETIME` كما كانا — لا نوعَ خاصًّا بـPostgreSQL يتسرّب."""
    types = _compiled(sqlite.dialect())
    assert {types[k] for k in EXPECTED_JSONB} == {"JSON"}
    assert {types[k] for k in EXPECTED_TIMESTAMPTZ} == {"DATETIME"}


def _pg_enabled() -> bool:
    return os.environ.get("AMOS_RUN_POSTGRES_TESTS") == "1" and os.environ.get(
        "AMOS_TEST_DATABASE_URL", ""
    ).startswith("postgresql")


@pytest.mark.skipif(
    not _pg_enabled(),
    reason="Set AMOS_RUN_POSTGRES_TESTS=1 and AMOS_TEST_DATABASE_URL=postgresql://... to run",
)
def test_instant_and_containment_survive_a_non_utc_session_on_postgres() -> None:
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import Session

    from amos_federation.common.database import with_declared_driver

    url = with_declared_driver(os.environ["AMOS_TEST_DATABASE_URL"])
    schema = f"wi065_{uuid.uuid4().hex[:10]}"
    admin = create_engine(url, isolation_level="AUTOCOMMIT")
    with admin.connect() as conn:
        conn.execute(text(f'CREATE SCHEMA "{schema}"'))
    try:
        engine = create_engine(
            url, connect_args={"options": f"-csearch_path={schema} -cTimeZone=Asia/Riyadh"}
        )
        Base.metadata.create_all(engine, tables=[m.__table__ for m in CORE_MODELS])
        written = datetime(2026, 10, 10, 12, 0, 0, tzinfo=UTC)
        with Session(engine) as session:
            session.add(
                AgentModel(
                    id="agent-wi065",
                    name="tz probe",
                    role="worker",
                    permissions=["read", "write"],
                    created_at=written,
                    updated_at=written,
                )
            )
            session.commit()
        with Session(engine) as session:
            read = session.get(AgentModel, "agent-wi065").created_at
            assert read.tzinfo is not None, "عادت اللحظةُ بلا منطقة"
            assert read == written, f"انزاحت اللحظة: كُتِبَ {written} وقُرِئَ {read}"
            contained = session.execute(
                text("SELECT count(*) FROM agents WHERE permissions @> CAST(:p AS jsonb)"),
                {"p": '["write"]'},
            ).scalar_one()
            assert contained == 1
        engine.dispose()
    finally:
        with admin.connect() as conn:
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{schema}" CASCADE'))
        admin.dispose()
