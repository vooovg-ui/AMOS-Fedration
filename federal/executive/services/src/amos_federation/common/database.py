"""
AMOS-Federation Database Layer
الهدف: طبقة تخزين دائمة بـ SQLAlchemy (SQLite للبيئة الحالية، PostgreSQL للإنتاج)
النطاق: common/database
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
"""

import contextlib
import os
import uuid
from collections.abc import Generator
from datetime import UTC, datetime

from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
    create_engine,
    event,
)
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    """القاعدة لكل النماذج."""

    pass


# === النماذج ===


class AgentModel(Base):
    """جدول الوكلاء — السجلُّ الكانونيُّ الواحدُ لهويّةِ الوكيل.

    W-032 (قرارُ المالكِ في Q-39 (ب) بتاريخ 2026-08-23): كانَ `api-gateway` يكتبُ
    بيانَ الوكيلِ في **قاموسِ ذاكرةٍ** بينما هذا الجدولُ موجودٌ — أي كاتبانِ على
    حقيقةٍ واحدةٍ، أحدُهما يتبخّرُ بإعادةِ التشغيل. فحُوِّلَتِ الكتابةُ إلى هنا،
    وأُضيفَتِ الأعمدةُ الثلاثةُ أدناه لأنَّ البيانَ المنشورَ يحملُها: لو كُتِبَ
    الوكيلُ بلا `agent_type` و`domain` و`description` لصارَ الجدولُ يُعيدُ **أقلَّ**
    مِمّا أعلنَه العقدُ، وذاك نقصُ حقيقةٍ لا إدامةٌ لها.
    """

    __tablename__ = "agents"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    #: نوعُ الوكيلِ كما أعلنَه بيانُ التسجيلِ (`AgentManifestModel.agent_type`).
    #: و`role` يبقى حقلَ القدرةِ الذي يقرأُه الموزِّعُ — لا يُدمَجانِ في عمودٍ واحد.
    agent_type = Column(String, default="worker")
    #: مجالُ الوكيلِ المُعلَنُ في البيان — `None` تعني «لم يُعلَنْ» لا «عامّ».
    domain = Column(String, nullable=True)
    description = Column(Text, default="")
    status = Column(String, default="registered")
    permissions = Column(JSON, default=list)
    allowed_tools = Column(JSON, default=list)
    token_budget = Column(Integer, default=10000)
    tenant_id = Column(String, default="default")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    updated_at = Column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )


class ToolModel(Base):
    """جدول الأدوات — مالكُ سجلِّ الأدواتِ الواحدُ (Q-39 (ب) · W-032).

    الأعمدةُ الأربعةُ المُضافةُ في W-032 (`version` · `risk_level` ·
    `input_schema` · `output_schema`) ليست ترفًا: قبلَها كانَ `PersistentToolStore`
    يكتبُ الأداةَ ويُعيدُ قراءتَها بقيمٍ **ثابتةٍ مُختلَقةٍ** (`1.0.0` و`low`
    وقاموسَينِ فارغَينِ)، فأداةٌ تُسجَّلُ بخطورةِ `critical` تُقرأُ `low`. وحينَ صارَ
    هذا الجدولُ المصدرَ الوحيدَ للحقيقةِ لم يَجُزْ أن يُخفِّضَ خطورةَ أداةٍ بالسكوت.
    """

    __tablename__ = "tools"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text, default="")
    category = Column(String, default="general")
    keywords = Column(JSON, default=list)
    endpoint = Column(String, default="")
    permissions_required = Column(JSON, default=list)
    version = Column(String, default="1.0.0")
    risk_level = Column(String, default="low")
    input_schema = Column(JSON, default=dict)
    output_schema = Column(JSON, default=dict)
    sandbox_required = Column(Boolean, default=False)
    tenant_id = Column(String, default="default")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class TaskModel(Base):
    """جدول المهام."""

    __tablename__ = "tasks"

    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String, default="created")
    priority = Column(String, default="normal")
    domain = Column(String, default="general")
    assigned_agent = Column(String, nullable=True)
    plan = Column(JSON, default=list)
    result = Column(JSON, default=dict)
    tenant_id = Column(String, default="default")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    updated_at = Column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )


class MemoryModel(Base):
    """جدول الذاكرة التشغيلية."""

    __tablename__ = "memories"

    key = Column(String, primary_key=True)
    value = Column(Text, nullable=False)
    keywords = Column(JSON, default=list)
    tenant_id = Column(String, default="default")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class ExperienceModel(Base):
    """جدول الخبرات."""

    __tablename__ = "experiences"

    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    task_id = Column(String, nullable=True)
    agent_id = Column(String, nullable=True)
    model_used = Column(String, nullable=True)
    outcome = Column(JSON, default=dict)
    quality_score = Column(Float, nullable=True)
    provenance = Column(JSON, default=dict)
    tenant_id = Column(String, default="default")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class ReviewModel(Base):
    """جدول مراجعات الناقد."""

    __tablename__ = "reviews"

    id = Column(String, primary_key=True)
    task_id = Column(String, nullable=True)
    agent_id = Column(String, nullable=True)
    quality_score = Column(Float, nullable=False)
    feedback = Column(Text, default="")
    approved = Column(Boolean, default=False)
    criteria = Column(JSON, default=dict)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class AuditEntryModel(Base):
    """جدول سجل التدقيق."""

    __tablename__ = "audit_entries"

    id = Column(String, primary_key=True)
    action = Column(String, nullable=False)
    actor = Column(String, nullable=False)
    details = Column(JSON, default=dict)
    prev_hash = Column(String, nullable=False, default="0" * 64)
    hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class SystemStateModel(Base):
    """جدولُ حالةِ النظامِ — صفٌّ واحدٌ يحملُ مستوى مفتاحِ الإيقاف.

    أُنشئَ في W-031 تنفيذًا لقرارِ المالكِ في Q-39 (أ) بتاريخ 2026-08-23: إدامةُ
    مفتاحِ الإيقافِ **أوّلًا** قبلَ باقي الأسطح. وقبلَه كان المستوى قاموسًا في
    ذاكرةِ العمليّةِ، فقِيسَ في W-030 أنَّ نظامًا أُوقِفَ بمستوى `halt` يعودُ
    `normal` بإعادةِ التشغيلِ — أي أنَّ الدولةَ تُلغي إيقافَ نفسِها.

    والصفُّ واحدٌ بمعرّفٍ ثابتٍ (`system`) لأنَّ الحالةَ حالةُ الدولةِ لا حالةُ
    عمليّةٍ: كلُّ عاملٍ يقرأُ الصفَّ نفسَه، فلا يبقى لكلِّ عمليّةٍ مستوًى خاصٌّ.
    """

    __tablename__ = "system_state"

    id = Column(String, primary_key=True, default="system")
    level = Column(String, nullable=False, default="normal")
    reason = Column(Text, default="")
    #: نصٌّ ISO لا `DateTime`: هذه القيمةُ تُعادُ حرفيًّا في جسمِ الواجهةِ، وتحويلُها
    #: إلى وقتٍ ثمّ تنسيقُها من جديدٍ يُغيِّرُ عقدَ الواجهةِ بلا سبب.
    activated_at = Column(String, nullable=True, default=None)
    activated_by = Column(String, default="")
    updated_at = Column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )


class PromotionModel(Base):
    """جدولُ طلباتِ ترقيةِ النماذجِ وبوّاباتِها الخمس.

    أُنشئَ في W-031 بقرارِ المالكِ في Q-39 (أ). وقبلَه كانت الطلباتُ قائمةً في
    الذاكرةِ، فكانت **موافقةُ الإنسانِ على ترقيةٍ** (`human_approval`) تزولُ
    بإعادةِ التشغيلِ ولا يبقى لها أثرٌ يُقاس (W-029 · W-030).
    """

    __tablename__ = "promotions"

    id = Column(String, primary_key=True)
    model_id = Column(String, nullable=False)
    gates = Column(JSON, default=dict)
    status = Column(String, default="in_progress")
    #: نصوصُ ISO حفظًا لعقدِ الواجهةِ كما كانَ قبلَ الإدامةِ — لا تغييرَ في الشكل.
    created_at = Column(String, default="")
    updated_at = Column(String, default="")


# === إدارة الاتصال ===


def get_database_url() -> str:
    """الحصول على رابط قاعدة البيانات."""
    return os.environ.get(
        "AMOS_DATABASE_URL",
        f"sqlite:///{os.path.join(os.getcwd(), 'amos_federation.db')}",
    )


# === لهجة قاعدة البيانات ===

DIALECT_POSTGRES = "postgresql"
DIALECT_SQLITE = "sqlite"


def db_dialect(url: str | None = None) -> str:
    """المصدر الوحيد لتحديد لهجة قاعدة البيانات الحالية.

    يعيد DIALECT_POSTGRES أو DIALECT_SQLITE. كل قرار يعتمد على اللهجة
    في هذه الطبقة يجب أن يمرّ من هنا، لا من مقارنات نصية متفرقة.
    """
    effective = url if url is not None else get_database_url()
    if effective.startswith("postgresql"):
        return DIALECT_POSTGRES
    return DIALECT_SQLITE


def _is_postgres(url: str | None = None) -> bool:
    return db_dialect(url) == DIALECT_POSTGRES


def _pg_connect_args(url: str | None = None) -> dict:
    """معاملات الاتصال المعتمدة على اللهجة (Supabase يتطلب SSL).

    هذه الدالة هي المصدر الوحيد لمعاملات الاتصال؛ get_engine() يستدعيها
    ولا يكرّر المنطق.
    """
    if not _is_postgres(url):
        return {"check_same_thread": False}
    return {
        "sslmode": os.environ.get("AMOS_DB_SSLMODE", "require"),
        "connect_timeout": int(os.environ.get("AMOS_DB_CONNECT_TIMEOUT", "15")),
    }


def connect_args(url: str | None = None) -> dict:
    """معاملاتُ الاتّصال لكلّ مُنشِئِ محرّكٍ في المشروع — الواجهةُ المُعلنة.

    `_pg_connect_args` تقول عن نفسها إنّها «المصدرُ الوحيد»، وكانت ثلاثةُ
    مواضعٍ تكتب `sslmode: require` بيدها فتُكذّب الدّعوى. فهذه دالةٌ عامّةٌ
    تُستورَد من خارج الوحدة، ليبقى المصدرُ واحدًا فعلًا لا قولًا.

    والمستودع يطلب SSL افتراضًا لأنّ الإنتاج على Supabase يوجبه، وُيخفَّض
    بمتغيّر `AMOS_DB_SSLMODE` وحده — للحاويات المحليّة التي لا TLS لها.
    """
    return _pg_connect_args(url)


def _pool_settings() -> dict:
    """حدود تجمّع الاتصالات — قابلة للضبط لأن الوسطاء المُجمّعين محدودون.

    Supabase session-mode pooler يرفض ما يزيد على 15 عميلًا، فلا يجوز تثبيت
    حجم التجمّع في الكود.
    """
    return {
        "pool_size": int(os.environ.get("AMOS_DB_POOL_SIZE", "5")),
        "max_overflow": int(os.environ.get("AMOS_DB_MAX_OVERFLOW", "10")),
    }


_engine = None
_SessionLocal = None


def _enforce_sqlite_foreign_keys(engine) -> None:
    """شغِّل فرض المفاتيح الأجنبية على SQLite — وإلا كان القيد زخرفة.

    SQLite يقبل `REFERENCES` في المخطَّط ثم **لا يفرضه** إلا إذا رُفع
    `PRAGMA foreign_keys` لكل اتصال. وحتى R6 لم يكن في المستودع أي
    `ForeignKey` في طبقة ORM (`grep` = صفر)، فلم يظهر الفرق. وR7 أدخلت أول
    روابط مرجعية حقيقية (`state_officials.agent_id → agents.id`)، فلو بقي
    الفرض مُطفأً لكان الادّعاء بوجود قيود مرجعية كذبًا: الصفوف اليتيمة تُكتب
    بنجاح.

    والفرض هنا على محرك `common/database` وحده. الوحدات التي تُنشئ محركًا
    خاصًّا بها (`treasury`, `RBACSystem`, `DurableEventBus`) لا يشملها هذا،
    وهو دَينٌ قائم مُسجَّل — لكن جداول R7 كلها على هذا المحرك.
    """
    if db_dialect(str(engine.url)) != DIALECT_SQLITE:
        return

    @event.listens_for(engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, _connection_record):  # pragma: no cover - callback
        cursor = dbapi_connection.cursor()
        try:
            cursor.execute("PRAGMA foreign_keys=ON")
        finally:
            cursor.close()


def get_engine():
    """الحصول على محرك قاعدة البيانات (Singleton)."""
    global _engine
    if _engine is None:
        url = get_database_url()
        _engine = create_engine(
            url,
            connect_args=_pg_connect_args(url),
            echo=False,
            pool_pre_ping=True,
            **_pool_settings(),
        )
        _enforce_sqlite_foreign_keys(_engine)
    return _engine


def reset_engine() -> None:
    """إعادة تعيين المحرك — للاختبارات والتغيير بين SQLite و PostgreSQL."""
    global _engine, _SessionLocal
    if _engine is not None:
        _engine.dispose()
    _engine = None
    _SessionLocal = None


def get_session_factory():
    """الحصول على مصنع الجلسات (Singleton)."""
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=get_engine(), autoflush=False, expire_on_commit=False)
    return _SessionLocal


#: الأعمدةُ التي أُضيفَتْ إلى جداولَ **قائمةٍ** في W-032. و`create_all` لا يُعدِّلُ
#: جدولًا موجودًا: يُنشئُ الغائبَ ويسكتُ عن الناقص. فقاعدةُ بياناتٍ أُنشئَتْ قبلَ
#: W-032 كانت ستُسقِطُ كلَّ نداءٍ بـ`no such column` — وهو سقوطٌ صامتُ السببِ عندَ
#: من يُشغِّلُ النظامَ على قاعدتِه القديمة. فالإضافةُ تُطبَّقُ هنا **مرّةً واحدةً
#: وبأمانٍ**: تُقرأُ الأعمدةُ الموجودةُ فعلًا ثمَّ يُضافُ الناقصُ فقط، ولا يُحذَفُ
#: عمودٌ ولا يُغيَّرُ نوعُه ولا تُمَسُّ بياناتٌ. ونصُّ الترحيلِ نفسُه مُقيَّدٌ في
#: `migrations/015_registry_ownership_w032.sql` لمن يُرحِّلُ بالـSQL لا بالمحرّك.
_W032_ADDED_COLUMNS: dict[str, dict[str, str]] = {
    "agents": {
        "agent_type": "VARCHAR",
        "domain": "VARCHAR",
        "description": "TEXT",
    },
    "tools": {
        "version": "VARCHAR",
        "risk_level": "VARCHAR",
        "input_schema": "JSON",
        "output_schema": "JSON",
    },
}


def ensure_added_columns() -> list[str]:
    """أضِفِ الأعمدةَ الناقصةَ في جداولَ قائمةٍ — وأعِدْ ما أُضيفَ فعلًا.

    الإرجاعُ ليس زينةً: بلا قائمةٍ مُعادةٍ لا يستطيعُ اختبارٌ أن يُثبِتَ أنَّ
    الإضافةَ جرَتْ ولا أنَّ إعادةَ النداءِ لا تُضيفُ شيئًا (idempotent).
    """
    from sqlalchemy import inspect as sa_inspect
    from sqlalchemy import text as sa_text

    engine = get_engine()
    inspector = sa_inspect(engine)
    added: list[str] = []
    existing_tables = set(inspector.get_table_names())
    for table, columns in _W032_ADDED_COLUMNS.items():
        if table not in existing_tables:
            continue
        present = {col["name"] for col in inspector.get_columns(table)}
        for column, sql_type in columns.items():
            if column in present:
                continue
            with engine.begin() as connection:
                connection.execute(sa_text(f"ALTER TABLE {table} ADD COLUMN {column} {sql_type}"))
            added.append(f"{table}.{column}")
    return added


def init_db() -> None:
    """إنشاء كل الجداول عند الإقلاع، وإتمامُ أعمدةِ W-032 في القائمِ منها."""
    Base.metadata.create_all(get_engine())
    ensure_added_columns()


def get_db() -> Generator[Session, None, None]:
    """Dependency للحصول على جلسة قاعدة بيانات."""
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()


def with_db(func):
    """Decorator لتوفير جلسة DB تلقائيًا."""

    def wrapper(*args, **kwargs):
        session = get_session_factory()()
        try:
            result = func(*args, session=session, **kwargs)
            session.commit()
            return result
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    return wrapper


# === توافق عكسي مع الوحدات القديمة ===


def generate_uuid() -> uuid.UUID:
    """توليد معرّف فريد (توافق عكسي)."""
    return uuid.uuid4()


# === طبقة SQL محايدة اللهجة ===
#
# قاعدة واحدة لكل الكود الذي يستخدم db_cursor():
#   اكتب المحاجيز بالشكل القانوني "?" فقط.
# المغلّف أدناه يترجمها إلى "%s" عند استخدام psycopg2. لا يجوز كتابة
# SQL خاص بلهجة واحدة داخل مسار الإنتاج.

PARAM_PLACEHOLDER = "?"


def translate_placeholders(sql: str, dialect: str) -> str:
    """تحويل المحاجيز القانونية "?" إلى ما تفهمه اللهجة المستهدفة.

    يتجاهل المحاجيز داخل السلاسل النصية المفردة حتى لا يُفسِد القيم الحرفية،
    ويضاعف '%' في PostgreSQL لأن psycopg2 يعتبره حرف تنسيق.
    """
    if dialect != DIALECT_POSTGRES:
        return sql
    out: list[str] = []
    in_string = False
    for char in sql:
        if char == "'":
            in_string = not in_string
            out.append(char)
        elif in_string:
            out.append(char)
        elif char == PARAM_PLACEHOLDER:
            out.append("%s")
        elif char == "%":
            out.append("%%")
        else:
            out.append(char)
    return "".join(out)


def _as_mapping(row):
    """توحيد شكل السجلّ: قاموس في اللهجتين معًا."""
    if row is None:
        return None
    if isinstance(row, dict):
        return row
    return dict(row)


class PortableCursor:
    """مغلّف مؤشر يخفي اختلافات اللهجة عن مستدعيه.

    يقبل محاجيز "?" دائمًا، ويعيد السجلات كقواميس دائمًا.
    """

    def __init__(self, cursor, dialect: str) -> None:
        self._cursor = cursor
        self.dialect = dialect

    def execute(self, sql: str, params=None):
        translated = translate_placeholders(sql, self.dialect)
        if params is None:
            return self._cursor.execute(translated)
        return self._cursor.execute(translated, params)

    def executemany(self, sql: str, seq_of_params):
        translated = translate_placeholders(sql, self.dialect)
        return self._cursor.executemany(translated, seq_of_params)

    def fetchone(self):
        return _as_mapping(self._cursor.fetchone())

    def fetchall(self):
        return [_as_mapping(row) for row in self._cursor.fetchall()]

    def __getattr__(self, name):
        return getattr(self._cursor, name)


@contextlib.contextmanager
def db_cursor():
    """مؤشر محايد اللهجة يعمل على SQLite و PostgreSQL بنفس الـ SQL."""
    db_url = get_database_url()
    dialect = db_dialect(db_url)

    if dialect == DIALECT_POSTGRES:
        import psycopg2
        from psycopg2.extras import RealDictCursor

        pg_args = _pg_connect_args(db_url)
        conn = psycopg2.connect(db_url, **pg_args)
        try:
            yield PortableCursor(conn.cursor(cursor_factory=RealDictCursor), dialect)
            conn.commit()
        finally:
            conn.close()
    else:
        import sqlite3

        db_path = db_url.replace("sqlite:///", "")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield PortableCursor(conn.cursor(), dialect)
            conn.commit()
        finally:
            conn.close()


# === سجل التدقيق (audit_log) — تعريف واحد لللهجتين ===
#
# عمود seq متزايد رتيب وهو الأساس الوحيد لترتيب السلسلة.
# لا يجوز الترتيب بـ id لأنه UUID في PostgreSQL فيُعطي ترتيبًا عشوائيًا.

_AUDIT_LOG_DDL = {
    DIALECT_SQLITE: """
        CREATE TABLE IF NOT EXISTS audit_log (
            seq        INTEGER PRIMARY KEY AUTOINCREMENT,
            id         TEXT,
            event_id   TEXT,
            timestamp  TEXT,
            event_type TEXT,
            actor_type TEXT,
            actor_id   TEXT,
            action     TEXT,
            chain_hash TEXT,
            prev_hash  TEXT,
            metadata   TEXT
        )
    """,
    DIALECT_POSTGRES: """
        CREATE TABLE IF NOT EXISTS audit_log (
            seq        BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            id         UUID DEFAULT gen_random_uuid(),
            event_id   VARCHAR(255),
            timestamp  TEXT,
            event_type VARCHAR(100),
            actor_type VARCHAR(20),
            actor_id   VARCHAR(255),
            action     VARCHAR(255),
            chain_hash VARCHAR(255),
            prev_hash  VARCHAR(255),
            metadata   JSONB
        )
    """,
}


def audit_log_ddl(dialect: str | None = None) -> str:
    """تعريف جدول audit_log المناسب لللهجة الحالية."""
    return _AUDIT_LOG_DDL[dialect or db_dialect()]


def ensure_audit_log_table() -> None:
    """إنشاء جدول audit_log إن لم يوجد — بنفس العقد في اللهجتين."""
    with db_cursor() as cur:
        cur.execute(audit_log_ddl(cur.dialect))


def drop_audit_log_table() -> None:
    """إزالة جدول audit_log — للاختبارات فقط."""
    with db_cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS audit_log")
