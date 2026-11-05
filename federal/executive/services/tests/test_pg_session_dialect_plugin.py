"""الهدف: فحصُ مُلحَقِ لهجةِ الجلسة `tests/pg_session_dialect.py` بلا خادمِ PostgreSQL (Q-99 البند 6 · W-825).

التعريف: المُلحَقُ يُحمَّلُ في حزمةِ `services-postgres` وحدَها ويُسقِطُ الجلسةَ بلا بيئةِ
PostgreSQL ويُسقِطُ كلَّ اختبارٍ يجري على غيرِه. وهذا الملفُّ يفحصُ دالّتَيه الحاكمتَين
النقيّتَين وخُطّافَ الإعداد — فيجري في حزمةِ SQLite العاديّة بلا تخطٍّ.
النطاق: federal/executive/services/tests
المالك: federal/executive/services (WI-127 · W-825)
تاريخ الإنشاء: 2026-11-05
تاريخ آخر تعديل: 2026-11-05 (`W-825` — الإنشاء)
"""

from __future__ import annotations

import pytest

from tests import pg_session_dialect as plugin

PG_URL = "postgresql://postgres:x@localhost:5432/db"


class TestEnvironmentGate:
    def test_full_postgres_env_is_accepted(self) -> None:
        env = {plugin.PG_FLAG_ENV: "1", plugin.PG_URL_ENV: PG_URL}
        assert plugin.postgres_env_violation(env) is None

    @pytest.mark.parametrize(
        "env",
        [
            {},
            {plugin.PG_URL_ENV: PG_URL},
            {plugin.PG_FLAG_ENV: "0", plugin.PG_URL_ENV: PG_URL},
            {plugin.PG_FLAG_ENV: "1"},
            {plugin.PG_FLAG_ENV: "1", plugin.PG_URL_ENV: "sqlite:///x.db"},
        ],
    )
    def test_incomplete_env_is_refused(self, env: dict) -> None:
        assert plugin.postgres_env_violation(env) is not None

    def test_configure_raises_usage_error_not_skip(self, monkeypatch) -> None:
        monkeypatch.delenv(plugin.PG_FLAG_ENV, raising=False)
        monkeypatch.delenv(plugin.PG_URL_ENV, raising=False)
        with pytest.raises(pytest.UsageError, match="pg-session"):
            plugin.pytest_configure(None)  # type: ignore[arg-type]


class TestDialectGate:
    def test_postgresql_passes(self) -> None:
        assert plugin.dialect_violation("postgresql") is None

    @pytest.mark.parametrize("dialect", ["sqlite", "", "postgres", "mysql"])
    def test_anything_else_fails(self, dialect: str) -> None:
        reason = plugin.dialect_violation(dialect)
        assert reason is not None and "postgresql" in reason

    def test_this_session_is_not_postgres_so_the_gate_would_fail_it(self) -> None:
        """في حزمةِ SQLite: لهجةُ الجلسةِ sqlite — فلو حُمِّلَ المُلحَقُ هنا لأسقطَها."""
        from amos_federation.common import database

        assert database.db_dialect() == "sqlite"
        assert plugin.dialect_violation(database.db_dialect()) is not None


class TestRuntestCallHook:
    def test_hook_fails_a_test_running_on_sqlite_before_its_body(self) -> None:
        """الخُطّافُ نفسُه — لا الدالّةُ وحدَها — يُسقِطُ اختبارًا على SQLite قبلَ جسمِه."""

        class _Item:
            nodeid = "tests/x.py::test_y"

        gen = plugin.pytest_runtest_call(_Item())  # type: ignore[arg-type]
        with pytest.raises(pytest.fail.Exception, match="pg-session"):
            next(gen)
