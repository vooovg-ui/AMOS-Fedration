"""
AMOS-Federation — المخطّطُ المُرحَّلُ يتبعُ النموذج (WI-064 · DISC-088 (ب))
الهدف: أن تبنيَ الهجراتُ 001–018 على PostgreSQL الجداولَ نفسَها التي يبنيها `Base.metadata`
       عمودًا عمودًا — نوعًا وطولًا ودقّةً وقبولًا للفراغ — إلّا ما سُمِّيَ هنا بالاسمِ وسببُه.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-10 (WI-064)
تاريخ آخر تعديل: 2026-10-10 (WI-064)

## القرار

المالكُ في 2026-10-10، جوابًا عن DISC-088 (ب) «أيُّهما مصدرُ المخطّط؟»: **«ORM»**.
فالنموذجُ هو التعريف، والهجرةُ تتبعُه. وقِيسَ قبلَ 018 على PostgreSQL 18.6: 63 عمودًا مشتركًا
يفترقُ؛ و018 تُسوّي منها 41 (‏أطوالٌ ودقّةٌ وقبولُ فراغ — توسيعٌ لا يُفقِدُ قيمة).

## ما يبقى مُسمًّى لا مخفيًّا

- `PENDING_TYPE_DOWNGRADE`: 22 عمودًا تخفيضُها `jsonb ⇒ json` أو `timestamptz ⇒ timestamp`
  ينتظرُ سؤالًا محدَّدًا إلى المالك؛ فليسَ للحرسِ أن يقبلَها بصمتٍ ولا أن يُسقِطَ عليها.
- `MIGRATION_ONLY_*`: أعمدةٌ وجداولُ في الهجراتِ لا يعرفُها النموذج. حذفُها هجرةٌ هدّامة
  يمنعُها الموجِّهُ تلقائيًّا، فهي باقيةٌ ومُعدَّدة.

والمقارنةُ **مساواةُ مجموعات**: افتراقٌ جديدٌ يُسقِطُ الحرس، وكذلك افتراقٌ مُسمًّى زالَ دونَ أن
يُحذَفَ اسمُه من هنا — فلا تبقى القائمةُ أوسعَ من الواقع.
"""

from __future__ import annotations

import importlib
import os
import re
import uuid
from pathlib import Path

import pytest

import amos_federation
from amos_federation.common.database import Base

MIGRATIONS_DIR = Path(__file__).resolve().parents[1] / "migrations"
MIGRATION_018 = MIGRATIONS_DIR / "018_align_migrated_schema_with_orm.sql"

#: (‏نوعُ الهجرة، نوعُ النموذج) — معلَّقٌ لقرارِ المالكِ في التخفيض.
PENDING_TYPE_DOWNGRADE: dict[str, tuple[str, str]] = {
    **dict.fromkeys(
        (
            "agents.allowed_tools",
            "agents.permissions",
            "audit_entries.details",
            "experiences.outcome",
            "experiences.provenance",
            "memories.keywords",
            "reviews.criteria",
            "tasks.plan",
            "tasks.result",
            "tools.input_schema",
            "tools.keywords",
            "tools.output_schema",
            "tools.permissions_required",
        ),
        ("jsonb", "json"),
    ),
    **dict.fromkeys(
        (
            "agents.created_at",
            "agents.updated_at",
            "audit_entries.created_at",
            "experiences.created_at",
            "memories.created_at",
            "reviews.created_at",
            "tasks.created_at",
            "tasks.updated_at",
            "tools.created_at",
        ),
        ("timestamp with time zone", "timestamp without time zone"),
    ),
}

MIGRATION_ONLY_COLUMNS = frozenset(
    {
        "agents.budget",
        "agents.expires_at",
        "agents.manifest",
        "agents.version",
        "tasks.assigned_at",
        "tasks.budget_used",
        "tasks.completed_at",
        "tasks.parent_task_id",
        "tasks.quality_score",
        "tools.status",
        "tools.tool_bom",
    }
)

MIGRATION_ONLY_TABLES = frozenset(
    {
        "approvals",
        "audit_log",
        "budgets",
        "constitution_versions",
        "model_versions",
        "tool_executions",
    }
)


def _import_whole_package() -> None:
    root = Path(amos_federation.__file__).resolve().parent
    for path in sorted(root.rglob("*.py")):
        parts = path.relative_to(root.parent).with_suffix("").parts
        if parts[-1] == "__init__":
            parts = parts[:-1]
        importlib.import_module(".".join(parts))


def test_migration_018_only_widens() -> None:
    """018 لا تحذفُ ولا تكتبُ صفًّا، وكلُّ تعديلٍ فيها توسيعٌ من ثلاثةِ أشكالٍ لا غير."""
    sql = MIGRATION_018.read_text(encoding="utf-8")
    code = "\n".join(line for line in sql.splitlines() if not line.lstrip().startswith("--"))
    upper = code.upper()
    for forbidden in (
        "DROP COLUMN",
        "DROP TABLE",
        "DELETE ",
        "TRUNCATE",
        "UPDATE ",
        "INSERT ",
        "DROP DEFAULT",
        "SET NOT NULL",
        "JSON;",
        "JSON,",
        "WITHOUT TIME ZONE",
    ):
        assert forbidden not in upper, f"018 تحوي «{forbidden.strip()}» خارجَ التعليق"
    clauses = re.findall(r"ALTER COLUMN\s+\w+\s+([^,;]+)", code, re.IGNORECASE)
    assert clauses, "018 بلا تعديل"
    allowed = {"TYPE character varying", "TYPE double precision", "DROP NOT NULL"}
    assert {c.strip() for c in clauses} <= allowed


def _pg_enabled() -> bool:
    return os.environ.get("AMOS_RUN_POSTGRES_TESTS") == "1" and os.environ.get(
        "AMOS_TEST_DATABASE_URL", ""
    ).startswith("postgresql")


@pytest.mark.skipif(
    not _pg_enabled(),
    reason="Set AMOS_RUN_POSTGRES_TESTS=1 and AMOS_TEST_DATABASE_URL=postgresql://... to run",
)
def test_migrated_schema_matches_the_orm_on_postgres() -> None:
    from sqlalchemy import create_engine, text

    from amos_federation.common.database import with_declared_driver

    _import_whole_package()
    url = with_declared_driver(os.environ["AMOS_TEST_DATABASE_URL"])
    suffix = uuid.uuid4().hex[:10]
    mig_schema, orm_schema = f"wi064_mig_{suffix}", f"wi064_orm_{suffix}"
    admin = create_engine(url, isolation_level="AUTOCOMMIT")
    try:
        with admin.connect() as conn:
            conn.execute(text(f'CREATE SCHEMA "{mig_schema}"'))
            conn.execute(text(f'CREATE SCHEMA "{orm_schema}"'))
        mig_engine = create_engine(
            url,
            isolation_level="AUTOCOMMIT",
            connect_args={"options": f"-csearch_path={mig_schema}"},
        )
        raw = mig_engine.raw_connection()
        try:
            cur = raw.cursor()
            for f in sorted(MIGRATIONS_DIR.glob("[0-9][0-9][0-9]_*.sql")):
                cur.execute(f.read_text(encoding="utf-8"))
            cur.execute(MIGRATION_018.read_text(encoding="utf-8"))  # التكرارُ لا يتكسّر
            cur.close()
        finally:
            raw.close()
        mig_engine.dispose()

        orm_engine = create_engine(url, connect_args={"options": f"-csearch_path={orm_schema}"})
        Base.metadata.create_all(orm_engine)
        orm_engine.dispose()

        query = text(
            "SELECT table_name, column_name, data_type, is_nullable, character_maximum_length, "
            "numeric_precision, numeric_scale FROM information_schema.columns "
            "WHERE table_schema = :s"
        )
        with admin.connect() as conn:
            mig = {(r[0], r[1]): tuple(r[2:]) for r in conn.execute(query, {"s": mig_schema})}
            orm = {(r[0], r[1]): tuple(r[2:]) for r in conn.execute(query, {"s": orm_schema})}
    finally:
        with admin.connect() as conn:
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{mig_schema}" CASCADE'))
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{orm_schema}" CASCADE'))
        admin.dispose()

    mig_tables, orm_tables = {t for t, _ in mig}, {t for t, _ in orm}
    assert orm_tables <= mig_tables, f"جداولُ في النموذجِ بلا هجرة: {sorted(orm_tables - mig_tables)}"
    assert mig_tables - orm_tables == MIGRATION_ONLY_TABLES
    only_mig_cols = {f"{t}.{c}" for t, c in mig if t in orm_tables and (t, c) not in orm}
    only_orm_cols = {f"{t}.{c}" for t, c in orm if (t, c) not in mig}
    assert not only_orm_cols, f"أعمدةٌ في النموذجِ بلا هجرة: {sorted(only_orm_cols)}"
    assert only_mig_cols == MIGRATION_ONLY_COLUMNS

    differing: dict[str, tuple[str, str]] = {}
    other: dict[str, tuple] = {}
    for key in sorted(set(mig) & set(orm)):
        a, b = mig[key], orm[key]
        if a == b:
            continue
        name = f"{key[0]}.{key[1]}"
        if a[1:] == b[1:]:
            differing[name] = (a[0], b[0])
        else:
            other[name] = (a, b)
    assert not other, f"افتراقٌ في الطولِ أو الدقّةِ أو قبولِ الفراغ بعدَ 018: {other}"
    assert differing == PENDING_TYPE_DOWNGRADE
