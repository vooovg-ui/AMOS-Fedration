"""
AMOS-Federation — عزلُ جلسةِ PostgreSQL في الاختباراتِ يُطبَّقُ فعلًا أو يسقطُ بصوتٍ عالٍ (WI-066)
الهدف: أن يُثبَتَ أنَّ `tests.pg_session.session_engine` يضعُ `search_path` و`TimeZone` على
       الجلسةِ الحقيقيّة (‏مباشرةً أو خلفَ مُجمِّعٍ بوضعِ الجلسة)، وأنَّ الإعدادَ الذي لا تعكسُه
       الجلسةُ حرفيًّا يُسقِطُ الاتصالَ ولا يمرُّ صامتًا، وأنَّ `connect_args.options` مرفوض.
النطاق: federal/executive/services/tests
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-12 (WI-066 · W-290)
تاريخ آخر تعديل: 2026-10-12 (WI-066 · W-290)
"""

from __future__ import annotations

import os
import uuid

import pytest

from tests.pg_session import SessionSettingNotAppliedError, session_engine

pg = pytest.mark.skipif(
    not (
        os.environ.get("AMOS_RUN_POSTGRES_TESTS") == "1"
        and os.environ.get("AMOS_TEST_DATABASE_URL", "").startswith("postgresql")
    ),
    reason="يحتاجُ AMOS_RUN_POSTGRES_TESTS=1 وAMOS_TEST_DATABASE_URL=postgresql://…",
)


def test_options_in_connect_args_is_refused() -> None:
    with pytest.raises(ValueError, match="options"):
        session_engine(
            "postgresql://u:p@localhost/db",
            search_path="x",
            connect_args={"options": "-csearch_path=x"},
        )


@pg
def test_schema_and_timezone_reach_the_real_session() -> None:
    from sqlalchemy import create_engine, text

    from amos_federation.common.database import with_declared_driver

    url = with_declared_driver(os.environ["AMOS_TEST_DATABASE_URL"])
    schema = f"wi066s_{uuid.uuid4().hex[:10]}"
    admin = create_engine(url, isolation_level="AUTOCOMMIT")
    with admin.connect() as conn:
        conn.execute(text(f'CREATE SCHEMA "{schema}"'))
    try:
        engine = session_engine(url, search_path=schema, timezone="Asia/Riyadh")
        with engine.connect() as conn:
            assert conn.execute(text("SHOW search_path")).scalar_one() == schema
            assert conn.execute(text("SHOW TimeZone")).scalar_one() == "Asia/Riyadh"
            conn.execute(text("CREATE TABLE probe (id int)"))
            conn.commit()
        engine.dispose()
        with admin.connect() as conn:
            where = (
                conn.execute(
                    text(
                        "SELECT table_schema FROM information_schema.tables WHERE table_name='probe'"
                    )
                )
                .scalars()
                .all()
            )
        assert where == [schema]  # الجدولُ في المخطّطِ المعزولِ وحدَه، لا في الافتراضيّ
    finally:
        with admin.connect() as conn:
            conn.execute(text(f'DROP SCHEMA IF EXISTS "{schema}" CASCADE'))
        admin.dispose()


@pg
def test_a_setting_the_session_does_not_echo_fails_loudly() -> None:
    from sqlalchemy import text

    from amos_federation.common.database import with_declared_driver

    url = with_declared_driver(os.environ["AMOS_TEST_DATABASE_URL"])
    # قِيسَ (‏2026-10-12 · PostgreSQL 17): `utc` تُعيدُها الجلسةُ «UTC» — فالمطابقةُ الحرفيّةُ
    # تفشلُ، وهذا هو الرفضُ المطلوب: المقارنةُ حقيقيّةٌ لا شكليّة.
    engine = session_engine(url, timezone="utc")
    with (
        pytest.raises(SessionSettingNotAppliedError, match="TimeZone"),
        engine.connect() as conn,
    ):
        conn.execute(text("SELECT 1"))
    engine.dispose()
