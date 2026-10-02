"""
حرسُ مُشغِّلِ PostgreSQL المُعلَن — الرابطُ بلا مُشغِّلٍ لا يُسلَّمُ لافتراضِ SQLAlchemy
الهدف: أن يُحمِّلَ كلُّ محرّكِ PostgreSQL في المستودعِ المُشغِّلَ المُعلَنَ اعتمادًا
        (`psycopg2-binary` في `pyproject.toml`) لا ما يفترضُه إصدارُ SQLAlchemy المُركَّب
النطاق: common/database — `get_database_url` · `with_declared_driver` · `libpq_dsn` · مواضعُ
        `create_engine` و`psycopg2.connect`
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-02

قِيسَ لا افتُرِض (`DISC-067` · `W-166`): SQLAlchemy 2.1.0 (2026-09-24) غيَّرَ مُشغِّلَ
`postgresql://` الافتراضيَّ من psycopg2 إلى psycopg 3، والاعتمادُ لا يُقيِّدُ سقفَ
الإصدار، فركَّبَ تشغيلُ CI رقمِ 35 (`pull_request` · 36925379905) SQLAlchemy 2.1.1 وسقطَت
حزمةُ `services-postgres` بـ8 فاشلةٍ و8 أخطاءٍ كلُّها `No module named 'psycopg'` —
والعقدةُ نفسُها كانت خضراءَ في التشغيلِ 34 بـSQLAlchemy 2.0.52. فالعطبُ في الاعتمادِ
على افتراضٍ خارجيٍّ متحرّكٍ، لا في الشجرة؛ وعلاجُه تسميةُ المُشغِّلِ في الموضعِ الواحدِ
الذي تمرُّ منه كلُّ روابطِ القاعدة.
"""

from __future__ import annotations

import ast
import pathlib
import re

import pytest
from sqlalchemy import create_engine

from amos_federation.common import database
from amos_federation.common.database import (
    DIALECT_POSTGRES,
    POSTGRES_DRIVER,
    db_dialect,
    get_database_url,
    libpq_dsn,
    with_declared_driver,
)

SERVICES_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_ROOT = SERVICES_ROOT / "src"
PYPROJECT = SERVICES_ROOT / "pyproject.toml"


# ── التحويلُ نفسُه ────────────────────────────────────────────────────────────


def test_driverless_url_gets_declared_driver() -> None:
    """الرابطُ بلا مُشغِّلٍ يُسنَدُ إلى المُشغِّلِ المُعلَن."""
    assert (
        with_declared_driver("postgresql://u:p@h:5432/d")
        == f"postgresql+{POSTGRES_DRIVER}://u:p@h:5432/d"
    )


@pytest.mark.parametrize(
    "url",
    [
        "postgresql+psycopg://u:p@h/d",
        "postgresql+psycopg2://u:p@h/d",
        "postgresql+asyncpg://u:p@h/d",
        "sqlite:///tmp/x.db",
        "sqlite://",
    ],
)
def test_named_driver_or_non_postgres_url_is_untouched(url: str) -> None:
    """الرابطُ الذي يُسمّي مُشغِّلَه أو ليس PostgreSQL لا يُنقَض."""
    assert with_declared_driver(url) == url


def test_rewrite_keeps_dialect_and_connect_args(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("AMOS_DATABASE_URL", "postgresql://u:p@h:5432/d")
    url = get_database_url()
    assert url.startswith(f"postgresql+{POSTGRES_DRIVER}://")
    assert db_dialect(url) == DIALECT_POSTGRES
    assert "sslmode" in database.connect_args(url), "معاملاتُ PostgreSQL تبقى كما كانت"


# ── المحرّكُ يُحمِّلُ المُشغِّلَ المُعلَنَ فعلًا — عينُ ما سقطَ في CI ────────────


def test_engine_loads_declared_driver_whatever_sqlalchemy_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """`create_engine` يستوردُ المُشغِّلَ عندَ الإنشاءِ بلا اتصال — فيُقاسُ هنا بلا قاعدة."""
    monkeypatch.setenv("AMOS_DATABASE_URL", "postgresql://u:p@127.0.0.1:1/d")
    engine = create_engine(get_database_url())
    try:
        assert engine.dialect.driver == POSTGRES_DRIVER
    finally:
        engine.dispose()


def test_code_driver_matches_pyproject_dependency() -> None:
    """مصدرانِ لا يفترقانِ صامتًا: اسمُ المُشغِّلِ في الكودِ يطابقُ اعتمادًا مُعلَنًا."""
    text = PYPROJECT.read_text(encoding="utf-8")
    deps = re.findall(r'^\s*"([A-Za-z0-9_.\-]+)\s*(?:[<>=!~;\[]|")', text, re.M)
    names = {d.lower().replace("_", "-") for d in deps}
    assert (
        f"{POSTGRES_DRIVER}-binary" in names or POSTGRES_DRIVER in names
    ), f"المُشغِّلُ `{POSTGRES_DRIVER}` غيرُ مُعلَنٍ اعتمادًا في {PYPROJECT.name}: {sorted(names)}"


# ── الموضعُ الواحدُ: كلُّ `create_engine` في الشجرةِ يأخذُ رابطَه من `get_database_url` ─


def _is_get_database_url(node: ast.AST) -> bool:
    if not isinstance(node, ast.Call):
        return False
    func = node.func
    return getattr(func, "id", getattr(func, "attr", None)) == "get_database_url"


def _engine_sites() -> tuple[int, list[str]]:
    routed = 0
    stray: list[str] = []
    for path in sorted(SRC_ROOT.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for fn in ast.walk(tree):
            if not isinstance(fn, ast.FunctionDef | ast.AsyncFunctionDef):
                continue
            assigned: dict[str, list[ast.AST]] = {}
            for node in ast.walk(fn):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            assigned.setdefault(target.id, []).append(node.value)
            for node in ast.walk(fn):
                if not (
                    isinstance(node, ast.Call)
                    and getattr(node.func, "id", getattr(node.func, "attr", None))
                    == "create_engine"
                ):
                    continue
                first = node.args[0] if node.args else None
                if first is not None and (
                    _is_get_database_url(first)
                    or (
                        isinstance(first, ast.Name)
                        and assigned.get(first.id)
                        and all(_is_get_database_url(v) for v in assigned[first.id])
                    )
                ):
                    routed += 1
                else:
                    rel = path.relative_to(SERVICES_ROOT)
                    stray.append(f"{rel}:{node.lineno}")
    return routed, stray


def test_every_engine_site_routes_through_get_database_url() -> None:
    """محرّكٌ يُنشَأُ من رابطٍ لم يمرَّ بـ`get_database_url` يعودُ إلى افتراضِ SQLAlchemy."""
    routed, stray = _engine_sites()
    assert routed > 0, "لا موضعَ `create_engine` واحدًا مقيسًا — القياسُ بلا مادّة"
    assert stray == [], (
        "مواضعُ `create_engine` لا تأخذُ رابطَها من `get_database_url` "
        f"فيفوتُها المُشغِّلُ المُعلَن: {stray}"
    )


# ── الاتصالُ المباشرُ بالمُشغِّلِ يأخذُ صيغةَ libpq لا صيغةَ SQLAlchemy ─────────
#
# قِيسَ في `W-166` على PostgreSQL 18 محلّيٍّ: لمّا سُمِّيَ المُشغِّلُ في الرابطِ وحدَه سقطَ
# `db_cursor` بـ`psycopg2.ProgrammingError: invalid dsn` في خمسةَ عشرَ موضعًا — فالرابطُ
# له مستهلِكانِ بعقدينِ مختلفين، وكلٌّ يأخذُ صيغتَه من دالّةٍ واحدةٍ مُسمّاة.


@pytest.mark.parametrize(
    ("url", "dsn"),
    [
        ("postgresql+psycopg2://u:p@h:5432/d", "postgresql://u:p@h:5432/d"),
        ("postgresql+psycopg://u:p@h/d?sslmode=disable", "postgresql://u:p@h/d?sslmode=disable"),
        ("postgresql://u:p@h/d", "postgresql://u:p@h/d"),
        ("sqlite:///tmp/x.db", "sqlite:///tmp/x.db"),
    ],
)
def test_libpq_dsn_drops_driver_name(url: str, dsn: str) -> None:
    """صيغةُ libpq بلا اسمِ مُشغِّل."""
    assert libpq_dsn(url) == dsn


def test_db_cursor_connects_with_libpq_dsn(monkeypatch: pytest.MonkeyPatch) -> None:
    """يُقاسُ ما يتسلَّمُه `psycopg2.connect` فعلًا — بلا قاعدةٍ ولا شبكة."""
    psycopg2 = pytest.importorskip("psycopg2")
    received: list[str] = []

    class _StopError(Exception):
        pass

    def _connect(dsn: str, **_kwargs: object) -> object:
        received.append(dsn)
        raise _StopError

    monkeypatch.setenv("AMOS_DATABASE_URL", "postgresql://u:p@127.0.0.1:1/d")
    monkeypatch.setattr(psycopg2, "connect", _connect)
    with pytest.raises(_StopError), database.db_cursor():
        pass  # pragma: no cover - الاتصالُ يُوقَفُ قبلَه
    assert received == ["postgresql://u:p@127.0.0.1:1/d"]


def _connect_sites() -> tuple[int, list[str]]:
    """كلُّ `psycopg2.connect` في الشجرةِ يأخذُ وسيطَه الأوّلَ من `libpq_dsn(...)`."""
    routed = 0
    stray: list[str] = []
    for path in sorted(SRC_ROOT.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "connect"
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "psycopg2"
            ):
                continue
            first = node.args[0] if node.args else None
            if (
                isinstance(first, ast.Call)
                and getattr(first.func, "id", getattr(first.func, "attr", None)) == "libpq_dsn"
            ):
                routed += 1
            else:
                stray.append(f"{path.relative_to(SERVICES_ROOT)}:{node.lineno}")
    return routed, stray


def test_every_direct_connect_routes_through_libpq_dsn() -> None:
    routed, stray = _connect_sites()
    assert routed > 0, "لا موضعَ `psycopg2.connect` واحدًا مقيسًا — القياسُ بلا مادّة"
    assert stray == [], f"اتصالٌ مباشرٌ برابطٍ بصيغةِ SQLAlchemy يرفضُه libpq: {stray}"
