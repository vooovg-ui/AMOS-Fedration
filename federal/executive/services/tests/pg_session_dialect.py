# الهدف: مُلحَقُ pytest يحوّلُ جلسةَ حزمةِ `services-postgres` كلَّها إلى PostgreSQL ويُسقِطُ أيَّ اختبارٍ يجري على غيرِه
# النطاق: federal/executive/services/tests — يُحمَّلُ بـ`-p tests.pg_session_dialect` في حزمةِ PostgreSQL وحدَها (Q-99 البند 6)
# المالك: federal/executive/services (WI-127 · W-825)
# تاريخ الإنشاء: 2026-11-05
# تاريخ آخر تعديل: 2026-11-05 (`W-825` — الإنشاء بتصميمِ `docs/audit/Q99_6_POSTGRES_CROSSING_SUITE_DESIGN.md` § 2.1)

"""مُلحَقُ لهجةِ الجلسة: PostgreSQL أو السقوط — لا تخطّي ولا عودةٌ صامتةٌ إلى SQLite.

`conftest.py` يفرضُ SQLite للحزمةِ كلِّها (قرارُ E2.2-G)، فملفُّ عبورٍ يُضافُ إلى حزمةِ
PostgreSQL بلا هذا المُلحَقِ يجري على SQLite وهو في حزمةٍ اسمُها POSTGRES — خضرةٌ
كاذبة. والمُلحَقُ لا يمسُّ ذلك القرار: لا يُحمَّلُ إلّا حيثُ تُعلِنُه الأداة.

1. `pytest_configure`: بيئةُ PostgreSQL غائبة ⇒ `pytest.UsageError` (سقوطٌ لا تخطٍّ).
2. `pytest_collection_finish`: بعدَ `conftest.py` والجمع ⇒ `AMOS_DATABASE_URL` يصيرُ رابطَ
   PostgreSQL ويُعادُ بناءُ المحرّك.
3. `pytest_runtest_call`: بعدَ مثبِّتاتِ كلِّ اختبارٍ وقبلَ جسمِه ⇒ لهجةٌ غيرُ PostgreSQL
   تُسقِطُ الاختبارَ باسمِه.
"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Mapping

PG_FLAG_ENV = "AMOS_RUN_POSTGRES_TESTS"
PG_URL_ENV = "AMOS_TEST_DATABASE_URL"
REQUIRED_DIALECT = "postgresql"

#: عددُ الاختباراتِ التي فُحِصَت لهجتُها فعلًا في هذه الجلسة — يُطبَعُ في الملخَّص.
_CHECKED: list[str] = []


def postgres_env_violation(env: Mapping[str, str]) -> str | None:
    """سببُ رفضِ البيئة، أو `None` إن كانت بيئةَ PostgreSQL صريحةً كاملة."""
    if env.get(PG_FLAG_ENV) != "1":
        return f"{PG_FLAG_ENV}=1 غائب — حزمةُ PostgreSQL لا تجري بلا PostgreSQL"
    if not env.get(PG_URL_ENV, "").startswith("postgresql"):
        return f"{PG_URL_ENV} لا يبدأُ بـpostgresql — حزمةُ PostgreSQL لا تجري بلا PostgreSQL"
    return None


def dialect_violation(dialect: str) -> str | None:
    """سببُ رفضِ اللهجةِ الفعليّة لحظةَ الاختبار، أو `None` إن كانت PostgreSQL."""
    if dialect != REQUIRED_DIALECT:
        return (
            f"اللهجةُ الفعليّة «{dialect}» لا «{REQUIRED_DIALECT}» — الاختبارُ لم يجرِ على PostgreSQL"
        )
    return None


def pytest_configure(config: pytest.Config) -> None:
    reason = postgres_env_violation(os.environ)
    if reason is not None:
        raise pytest.UsageError(f"[pg-session] {reason}")


@pytest.hookimpl(tryfirst=True)
def pytest_collection_finish(session: pytest.Session) -> None:
    from amos_federation.common import database

    os.environ["AMOS_DATABASE_URL"] = os.environ[PG_URL_ENV]
    database.reset_engine()


@pytest.hookimpl(wrapper=True)
def pytest_runtest_call(item: pytest.Item):
    from amos_federation.common import database

    reason = dialect_violation(database.db_dialect())
    if reason is not None:
        pytest.fail(f"[pg-session] {item.nodeid}: {reason}", pytrace=False)
    _CHECKED.append(item.nodeid)
    return (yield)


def pytest_terminal_summary(terminalreporter) -> None:  # noqa: ANN001 — TerminalReporter
    terminalreporter.write_line(
        f"[pg-session] اختباراتٌ فُحِصَت لهجتُها قبلَ جسمِها: {len(_CHECKED)} · "
        f"اللهجة المطلوبة: {REQUIRED_DIALECT}"
    )
