"""
AMOS-Federation — الهجرة 019: تحويلُ قواعدِ create_all إلى jsonb وtimestamptz بعدَ التحقّقِ من UTC (WI-066)
الهدف: أن يُثبَتَ على PostgreSQL الحقيقيِّ أنَّ 019 (1) تُحوِّلُ الأعمدةَ الـ22 في قاعدةٍ بنَاها
       create_all قبلَ WI-065 **واللحظةُ نفسُها**، (2) ترفضُ — ولا تُغيِّرُ شيئًا — حينَ لا تكونُ
       منطقةُ الجلسةِ UTC، أو حينَ تشهدُ البياناتُ نفسُها أنَّها كُتِبَت بمنطقةٍ أخرى، أو حينَ يتجاوزُ
       دورٌ المنطقة، و(3) لا تفعلُ شيئًا في قاعدةٍ بنَتْها الهجرات.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-10 (WI-066)
تاريخ آخر تعديل: 2026-10-10 (WI-066)

## كيف تُحاكى «قاعدةٌ قديمة»

يُبنى المخطّطُ بـ`create_all` للنموذجِ الحاليِّ ثمَّ تُعادُ الأعمدةُ الـ22 إلى `json` و`timestamp`
بلا منطقة — وهو بالضبطِ ما كانَ `create_all` يبنيه قبلَ WI-065 (‏`JSON` و`DateTime` بلا منطقة).
وتُكتَبُ الأوقاتُ بقيمٍ UTC بلا منطقةٍ كما كانَ PostgreSQL يخزّنُها بجلسةِ UTC.
"""

from __future__ import annotations

import os
import re
import uuid
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from tests.pg_session import session_engine

MIGRATIONS_DIR = Path(__file__).resolve().parents[1] / "migrations"
MIGRATION_019 = MIGRATIONS_DIR / "019_convert_create_all_databases_to_jsonb_timestamptz.sql"

JSON_COLS = (
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
)
TS_COLS = (
    "agents.created_at",
    "agents.updated_at",
    "tools.created_at",
    "tasks.created_at",
    "tasks.updated_at",
    "memories.created_at",
    "experiences.created_at",
    "reviews.created_at",
    "audit_entries.created_at",
)


def test_migration_019_names_exactly_the_22_columns_and_never_drops() -> None:
    sql = MIGRATION_019.read_text(encoding="utf-8")
    code = "\n".join(line for line in sql.splitlines() if not line.lstrip().startswith("--"))
    named = set(re.findall(r"\['(\w+)', '(\w+)', '(?:json|ts)'\]", code))
    assert {f"{t}.{c}" for t, c in named} == set(JSON_COLS) | set(TS_COLS)
    upper = code.upper()
    for forbidden in ("DROP COLUMN", "DROP TABLE", "DELETE ", "TRUNCATE", "UPDATE ", "INSERT "):
        assert forbidden not in upper, forbidden
    assert "AT TIME ZONE %L" in code and "'UTC'" in code


def _pg_enabled() -> bool:
    return os.environ.get("AMOS_RUN_POSTGRES_TESTS") == "1" and os.environ.get(
        "AMOS_TEST_DATABASE_URL", ""
    ).startswith("postgresql")


pg = pytest.mark.skipif(
    not _pg_enabled(),
    reason="Set AMOS_RUN_POSTGRES_TESTS=1 and AMOS_TEST_DATABASE_URL=postgresql://... to run",
)

WRITTEN = datetime(2026, 10, 10, 9, 0, 0)  # UTC بلا منطقة — كما خزّنَته جلسةُ UTC


@pytest.fixture
def legacy_schema():
    """مخطّطٌ مؤقّتٌ كقاعدةِ create_all قبلَ WI-065، فيه صفٌّ في كلِّ جدولٍ من السبعة."""
    from sqlalchemy import create_engine, text

    from amos_federation.common.database import (
        AgentModel,
        AuditEntryModel,
        Base,
        ExperienceModel,
        MemoryModel,
        ReviewModel,
        TaskModel,
        ToolModel,
        with_declared_driver,
    )

    url = with_declared_driver(os.environ["AMOS_TEST_DATABASE_URL"])
    schema = f"wi066_{uuid.uuid4().hex[:10]}"
    admin = create_engine(url, isolation_level="AUTOCOMMIT")
    with admin.connect() as conn:
        conn.execute(text(f'CREATE SCHEMA "{schema}"'))
    utc = session_engine(url, search_path=schema, timezone="UTC", isolation_level="AUTOCOMMIT")
    models = (
        AgentModel,
        ToolModel,
        TaskModel,
        MemoryModel,
        ExperienceModel,
        ReviewModel,
        AuditEntryModel,
    )
    Base.metadata.create_all(utc, tables=[m.__table__ for m in models])
    with utc.connect() as conn:
        for item in JSON_COLS:
            t, c = item.split(".")
            conn.execute(text(f"ALTER TABLE {t} ALTER COLUMN {c} TYPE json USING {c}::json"))
        for item in TS_COLS:
            t, c = item.split(".")
            conn.execute(
                text(
                    f"ALTER TABLE {t} ALTER COLUMN {c} TYPE timestamp USING {c} AT TIME ZONE 'UTC'"
                )
            )
        ts = {"ts": WRITTEN}
        conn.execute(
            text(
                "INSERT INTO agents (id, name, role, permissions, allowed_tools, created_at, "
                "updated_at, tenant_id) VALUES ('a1', 'n', 'worker', CAST('[\"write\"]' AS json), "
                "CAST('[]' AS json), :ts, :ts, 'default')"
            ),
            ts,
        )
        conn.execute(
            text(
                "INSERT INTO experiences (id, type, outcome, provenance, created_at, tenant_id) "
                "VALUES ('e1', 'success', CAST('{\"k\": 1}' AS json), CAST('{}' AS json), :ts, "
                "'default')"
            ),
            ts,
        )
    yield {"url": url, "schema": schema, "admin": admin, "utc": utc}
    utc.dispose()
    with admin.connect() as conn:
        conn.execute(text(f'DROP SCHEMA IF EXISTS "{schema}" CASCADE'))
    admin.dispose()


def _types(admin, schema: str) -> dict[str, str]:
    from sqlalchemy import text

    with admin.connect() as conn:
        rows = conn.execute(
            text(
                "SELECT table_name || '.' || column_name, data_type FROM information_schema.columns "
                "WHERE table_schema = :s"
            ),
            {"s": schema},
        )
        return dict(rows.all())


def _run_019(url: str, schema: str, tz: str) -> None:
    engine = session_engine(url, search_path=schema, timezone=tz, isolation_level="AUTOCOMMIT")
    raw = engine.raw_connection()
    try:
        cur = raw.cursor()
        cur.execute(MIGRATION_019.read_text(encoding="utf-8"))
        cur.close()
    finally:
        raw.close()
        engine.dispose()


def _assert_untouched(types: dict[str, str]) -> None:
    assert {types[c] for c in JSON_COLS} == {"json"}
    assert {types[c] for c in TS_COLS} == {"timestamp without time zone"}


@pg
def test_converts_all_22_columns_and_keeps_the_instant(legacy_schema) -> None:
    from sqlalchemy import text

    s = legacy_schema
    _assert_untouched(_types(s["admin"], s["schema"]))
    _run_019(s["url"], s["schema"], "UTC")
    types = _types(s["admin"], s["schema"])
    assert {types[c] for c in JSON_COLS} == {"jsonb"}
    assert {types[c] for c in TS_COLS} == {"timestamp with time zone"}
    with s["utc"].connect() as conn:
        got = conn.execute(text("SELECT created_at FROM agents WHERE id = 'a1'")).scalar_one()
        assert got == WRITTEN.replace(tzinfo=UTC)
        hits = conn.execute(
            text("SELECT count(*) FROM agents WHERE permissions @> CAST('[\"write\"]' AS jsonb)")
        ).scalar_one()
        assert hits == 1
    _run_019(s["url"], s["schema"], "UTC")  # التكرارُ لا يفعلُ شيئًا ولا يتكسّر
    assert _types(s["admin"], s["schema"]) == types


@pg
def test_refuses_when_the_session_is_not_utc_and_changes_nothing(legacy_schema) -> None:
    s = legacy_schema
    with pytest.raises(Exception, match="WI-066"):
        _run_019(s["url"], s["schema"], "Asia/Riyadh")
    _assert_untouched(_types(s["admin"], s["schema"]))


@pg
def test_refuses_when_the_data_was_written_in_another_zone(legacy_schema) -> None:
    """صفٌّ كُتِبَ بجلسةِ +03 يبدو بعدَ «الآنِ» بساعاتٍ إن قُرِئَ UTC — والبياناتُ تشهد."""
    from sqlalchemy import text

    s = legacy_schema
    riyadh_wall_clock = datetime.now(UTC).replace(tzinfo=None) + timedelta(hours=3)
    with s["utc"].connect() as conn:
        conn.execute(
            text(
                "INSERT INTO memories (key, value, keywords, created_at, tenant_id) "
                "VALUES ('m1', 'v', CAST('[]' AS json), :ts, 'default')"
            ),
            {"ts": riyadh_wall_clock},
        )
    with pytest.raises(Exception, match="WI-066"):
        _run_019(s["url"], s["schema"], "UTC")
    _assert_untouched(_types(s["admin"], s["schema"]))


@pg
def test_refuses_when_a_role_overrides_the_zone(legacy_schema) -> None:
    from sqlalchemy import text

    s = legacy_schema
    role = f"wi066_role_{uuid.uuid4().hex[:8]}"
    with s["admin"].connect() as conn:
        db = conn.execute(text("SELECT current_database()")).scalar_one()
        conn.execute(text(f'CREATE ROLE "{role}"'))
        conn.execute(text(f'ALTER ROLE "{role}" IN DATABASE "{db}" SET TimeZone = \'Asia/Riyadh\''))
    try:
        with pytest.raises(Exception, match="WI-066"):
            _run_019(s["url"], s["schema"], "UTC")
        _assert_untouched(_types(s["admin"], s["schema"]))
    finally:
        with s["admin"].connect() as conn:
            conn.execute(text(f'ALTER ROLE "{role}" IN DATABASE "{db}" RESET TimeZone'))
            conn.execute(text(f'DROP ROLE "{role}"'))


@pg
def test_a_migration_built_database_is_left_as_is() -> None:
    from sqlalchemy import create_engine, text

    from amos_federation.common.database import with_declared_driver

    url = with_declared_driver(os.environ["AMOS_TEST_DATABASE_URL"])
    schema = f"wi066m_{uuid.uuid4().hex[:10]}"
    admin = create_engine(url, isolation_level="AUTOCOMMIT")
    with admin.connect() as conn:
        conn.execute(text(f'CREATE SCHEMA "{schema}"'))
    try:
        engine = session_engine(
            url, search_path=schema, timezone="UTC", isolation_level="AUTOCOMMIT"
        )
        raw = engine.raw_connection()
        try:
            cur = raw.cursor()
            for f in sorted(MIGRATIONS_DIR.glob("[0-9][0-9][0-9]_*.sql")):
                if f.name[:3] < "019":
                    cur.execute(f.read_text(encoding="utf-8"))
            cur.close()
        finally:
            raw.close()
        before = _types(admin, schema)
        assert {before[c] for c in JSON_COLS} == {"jsonb"}
        _run_019(url, schema, "Asia/Riyadh")  # لا عمودَ قديمٌ ⇒ لا تحقّقَ يلزمُ ولا تغيير
        assert _types(admin, schema) == before
        engine.dispose()
    finally:
        with admin.connect() as conn:
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{schema}" CASCADE'))
        admin.dispose()
