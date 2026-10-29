"""
AMOS-Federation Phase 16 — Production Security
الهدف: أمان الإنتاج — RBAC، Secret Vault، TLS، Rate Limiting، Kill Switch تحقق
النطاق: services/governance/security
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
آخر تعديل: 2026-10-29 (W-728 — عبورُ أربعةِ أسطحٍ الحدَّ السياديَّ · G1 § 9.10)

المتطلبات:
  16.1: RBAC — أدوار وصلاحيات
  16.2: Secret Vault — أسرار مشفرة
  16.3: TLS/mTLS — شهادات
  16.4: Rate Limiting
  16.5: Audit Verification دوري
  16.6: Kill Switch تحقق من السلامة
  16.7: Policy Engine في الإنتاج
  16.8: Health Monitoring دوري
"""

import hashlib
import json
import logging
import os
import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine, inspect, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from amos_federation.common.database import get_database_url
from amos_federation.common.persistent import PersistentAuditStore
from amos_federation.common.principal import DEFAULT_TENANT
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)

_logger = logging.getLogger(__name__)

# ── أفعالُ العبورِ (G1 § 2.2 · تصميمُ § 9.10 · W-728) ─────────────────────────
#: `create_session` — صفُّ جلسةٍ (ممنوعٌ عندَ ≥4 · `execute_task`).
ACTION_CREATE_SESSION = "execute_task"
#: `check_rate` — رصدٌ لا منع: `log_isolated_action` ليسَ في KILL_SWITCH_BLOCKS.
ACTION_CHECK_RATE = "log_isolated_action"
#: `issue_certificate` — منحُ ثقةٍ (ممنوعٌ عندَ ≥3 · إضافةُ G1).
ACTION_ISSUE_CERTIFICATE = "issue_certificate"
#: `verify_certificate` — إقفالُ مسارِ الانتهاءِ رصدًا لا منعًا (مسارُ الكتابةِ وحدَه).
ACTION_VERIFY_CERTIFICATE = "log_isolated_action"
#: `store_secret` لا يُعبَرُ — دَينٌ معلَّقٌ بقرارِ المالكِ (§ 9.1): القبوُ يُحفظُ
#: كما هو ولا يُنزَلُ إلى فعلٍ أخفّ.

SESSION_SCOPE = "security.session"
RATE_SCOPE = "security.rate"
CERT_ISSUE_SCOPE = "security.cert.issue"
CERT_EXPIRE_SCOPE = "security.cert.expire"


class SecurityBase(DeclarativeBase):
    pass


class RoleModel(SecurityBase):
    """16.1: RBAC roles."""

    __tablename__ = "security_roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(String, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    permissions = Column(Text, default="[]")  # JSON array
    level = Column(Integer, default=0)  # 0=public, 1=citizen, 2=agent, 3=official, 4=royal, 5=king
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class UserSessionModel(SecurityBase):
    """جلسات المستخدمين."""

    __tablename__ = "security_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_token = Column(String, nullable=False, unique=True, index=True)
    username = Column(String, nullable=False)
    role_id = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    expires_at = Column(DateTime, nullable=True)
    ip_address = Column(String, nullable=True)
    # R6.1: مستأجر الجلسة. كان الجدول قبله بلا مستأجر إطلاقًا، فكان كل مبدأ
    # مُتحقَّق من جلسة يخرج إلى طبقة التخويل بمستأجر `default` — فلا عزل بين
    # جلستين مهما اختلف مستأجراهما. و`nullable=False` مقصود: جلسة بلا مستأجر
    # تُقرأ لاحقًا على أنها «أيّ مستأجر»، وذلك عكس المراد.
    tenant_id = Column(String, nullable=False, default=DEFAULT_TENANT, index=True)


class SecretVaultModel(SecurityBase):
    """16.2: Secret Vault — أسرار مشفرة."""

    __tablename__ = "security_secrets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    secret_key = Column(String, nullable=False, unique=True, index=True)
    encrypted_value = Column(Text, nullable=False)
    scope = Column(String, default="global")  # global, state-specific, agent-specific
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    rotated_at = Column(DateTime, nullable=True)


class RateLimitModel(SecurityBase):
    """16.4: Rate Limiting."""

    __tablename__ = "security_rate_limits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    identifier = Column(String, nullable=False, index=True)  # ip or agent_id
    endpoint = Column(String, nullable=False)
    request_count = Column(Integer, default=1)
    window_start = Column(DateTime, default=lambda: datetime.now(UTC))
    last_request = Column(DateTime, default=lambda: datetime.now(UTC))


class TLSCertificateModel(SecurityBase):
    """16.3: TLS Certificates."""

    __tablename__ = "security_certificates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cert_id = Column(String, nullable=False, unique=True, index=True)
    common_name = Column(String, nullable=False)
    cert_hash = Column(String, nullable=False)
    issuer = Column(String, default="AMOS-CA")
    valid_from = Column(DateTime, default=lambda: datetime.now(UTC))
    valid_until = Column(DateTime, nullable=True)
    status = Column(String, default="active")  # active, expired, revoked


# الأدوار الافتراضية
DEFAULT_ROLES = [
    {"role_id": "public", "name": "عام", "permissions": ["read:public"], "level": 0},
    {
        "role_id": "citizen",
        "name": "مواطن",
        "permissions": ["read:public", "write:feedback"],
        "level": 1,
    },
    {
        "role_id": "agent",
        "name": "وكيل",
        "permissions": ["read:public", "write:tasks", "execute:tools"],
        "level": 2,
    },
    {
        "role_id": "official",
        "name": "مسؤول",
        "permissions": ["read:all", "write:tasks", "execute:tools", "manage:agents"],
        "level": 3,
    },
    {
        "role_id": "royal",
        "name": "ملكي",
        "permissions": ["read:all", "write:all", "execute:all", "manage:all"],
        "level": 4,
    },
    {"role_id": "king", "name": "المالك", "permissions": ["*"], "level": 5},
]


class RBACSystem:
    """16.1: Role-Based Access Control."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        SecurityBase.metadata.create_all(self._engine)
        self._migrate_session_tenant()
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)
        self._init_roles()
        self._authorizer = authorizer

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """المُصرِّحُ السياديُّ بالفاعلِ التنفيذيِّ الافتراضيّ — يُبنى عندَ أوّلِ حاجة (G1)."""
        if self._authorizer is None:
            self._authorizer = ConstitutionalAuthorizer()
        return self._authorizer

    def _migrate_session_tenant(self) -> None:
        """R6.1: أضف `security_sessions.tenant_id` إلى جدول قائم إن غاب.

        `create_all` تُنشئ الجداول المفقودة و**لا تُضيف أعمدة إلى جدول موجود**.
        ولا نطام هجرة (alembic) في المستودع، فقاعدة قائمة من قبل R6.1 كانت
        ستكسر كل استعلام جلسة بـ`OperationalError: no such column`. وهذا ليس
        توسيع نطاق بل شرط لأن تعمل الميزة على قاعدة قائمة.

        إضافية وحدها: `ADD COLUMN` لا تُسقط شيئًا ولا تُعيد بناء جدول، والصفوف
        القائمة تأخذ `default` — وهو وصفٌ صادق لها: أُنشئت حين لم يكن للنشر
        إلا مستأجر واحد.
        """
        try:
            inspector = inspect(self._engine)
            if "security_sessions" not in inspector.get_table_names():
                return
            columns = {column["name"] for column in inspector.get_columns("security_sessions")}
            if "tenant_id" in columns:
                return
            with self._engine.begin() as connection:
                connection.execute(
                    text(
                        "ALTER TABLE security_sessions "
                        f"ADD COLUMN tenant_id VARCHAR DEFAULT '{DEFAULT_TENANT}'"
                    )
                )
                connection.execute(
                    text(
                        "UPDATE security_sessions "
                        f"SET tenant_id = '{DEFAULT_TENANT}' WHERE tenant_id IS NULL"
                    )
                )
        except SQLAlchemyError as exc:
            # الهجرة محاولة حسنة النيّة: فشلها يظهر فورًا عند أول استعلام جلسة
            # بخطأ واضح، ولا يُسكَت عنه بإدراج مستأجر وهمي. وإسقاط النظام كلّه
            # عند الإنشاء لأجل قاعدة لا تدعم ALTER أقسى من اللازم.
            # لكنه يُسجَّل: الفشلُ الصامت مخالفةٌ في ذاته.
            _logger.warning("تعذّرت هجرةُ tenant_id لجداول الأمن — %s", exc)

    def _init_roles(self) -> None:
        session = self._Session()
        try:
            for role in DEFAULT_ROLES:
                existing = (
                    session.query(RoleModel).filter(RoleModel.role_id == role["role_id"]).first()
                )
                if not existing:
                    session.add(
                        RoleModel(
                            role_id=role["role_id"],
                            name=role["name"],
                            permissions=json.dumps(role["permissions"]),
                            level=role["level"],
                        )
                    )
            session.commit()
        finally:
            session.close()

    def create_session(
        self,
        username: str,
        role_id: str,
        ip: str = "",
        *,
        tenant_id: str | None = None,
        operation_id: str | None = None,
    ) -> dict[str, Any]:
        """إنشاء جلسة مستخدم.

        Args:
            tenant_id: مستأجر الجلسة. يُملأ عند المصادقة من مصدر موثوق
                (سجلّ المستخدمين أو مُوفّر الهوية)، لا من جسم طلب تسجيل الدخول.
                وغيابه يعني `default` تحديدًا، لا «أيّ مستأجر».
            operation_id: معرِّفُ العمليةِ عندَ الإرسالِ المتكرَّر (G1 § 9.10 · W-728).

        عبورٌ سياديٌّ (G1 § 9.10 · W-728): `execute_task` ممنوعٌ عندَ ≥4.
        بصمةُ الجلسةِ (أولُ 16 حرفًا من SHA-256 للرمز) هي الهدفَ والمفتاح —
        والرمزُ نفسُه لا يدخلُ الهدفَ ولا الأثرَ ولا المفتاحَ ولا سجلَّ الذرّيّة.
        """
        session = self._Session()
        try:
            role = session.query(RoleModel).filter(RoleModel.role_id == role_id).first()
            if not role:
                return {"error": "role_not_found"}
            role_level = role.level
        finally:
            session.close()

        token = hashlib.sha256(f"{username}:{role_id}:{uuid.uuid4().hex}".encode()).hexdigest()
        from datetime import timedelta

        expires_at = datetime.now(UTC) + timedelta(hours=24)
        fingerprint = hashlib.sha256(token.encode()).hexdigest()[:16]
        effect = declared_effect("CREATE", f"session:{fingerprint}", f"{username}:{role_id}")

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                session.add(
                    UserSessionModel(
                        session_token=token,
                        username=username,
                        role_id=role_id,
                        ip_address=ip,
                        tenant_id=(tenant_id or DEFAULT_TENANT),
                        expires_at=expires_at,
                    )
                )
                session.commit()
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(UserSessionModel)
                    .filter(UserSessionModel.session_token == token)
                    .first()
                )
                if row:
                    session.delete(row)
                    session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_CREATE_SESSION,
            f"session:{fingerprint}",
            declared_effects=(effect,),
            operation_key=operation_key(SESSION_SCOPE, fingerprint),
            compensators=(compensator(effect.signature, _undo, "حذفُ صفِّ الجلسة"),),
            applier=_apply,
        )
        if guarded.is_replay:
            return {
                "session_token": token,
                "username": username,
                "role_id": role_id,
                "level": role_level,
                "tenant_id": (tenant_id or DEFAULT_TENANT),
                "replayed": True,
            }

        return {
            "session_token": token,
            "username": username,
            "role_id": role_id,
            "level": role_level,
            "tenant_id": (tenant_id or DEFAULT_TENANT),
        }

    def check_permission(self, session_token: str, permission: str) -> bool:
        """فحص صلاحية — والجلسة المنتهية لا صلاحية لها.

        كانت هذه الدالّة قبل R6 لا تنظر إلى `expires_at` إطلاقًا، فجلسة انتهت
        منذ شهر تمرّ كأنها حيّة. أُضيف الفحص: انتهاء الجلسة رفضٌ لا تحذير.
        """
        session = self._Session()
        try:
            user_session = (
                session.query(UserSessionModel)
                .filter(UserSessionModel.session_token == session_token)
                .first()
            )
            if not user_session:
                return False
            expires_at = user_session.expires_at
            if expires_at is not None:
                if expires_at.tzinfo is None:
                    expires_at = expires_at.replace(tzinfo=UTC)
                if expires_at <= datetime.now(UTC):
                    return False
            role = (
                session.query(RoleModel).filter(RoleModel.role_id == user_session.role_id).first()
            )
            if not role:
                return False
            permissions = json.loads(role.permissions or "[]")
            if "*" in permissions:
                return True
            return permission in permissions
        finally:
            session.close()

    def get_role_level(self, role_id: str) -> int:
        """مستوى الدور."""
        session = self._Session()
        try:
            role = session.query(RoleModel).filter(RoleModel.role_id == role_id).first()
            return role.level if role else 0
        finally:
            session.close()

    def list_roles(self) -> list[dict[str, Any]]:
        session = self._Session()
        try:
            roles = session.query(RoleModel).all()
            return [
                {
                    "role_id": r.role_id,
                    "name": r.name,
                    "permissions": json.loads(r.permissions or "[]"),
                    "level": r.level,
                }
                for r in roles
            ]
        finally:
            session.close()


class SecretVault:
    """16.2: Secret Vault — أسرار مشفرة بـ SHA-256."""

    def __init__(self) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        SecurityBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)

    def _encrypt(self, value: str) -> str:
        """تشفير بسيط — SHA-256 hash (في الإنتاج: AES-256)."""
        salt = os.environ.get("AMOS_VAULT_SALT", "amos-federation-salt")
        return hashlib.sha256(f"{salt}:{value}".encode()).hexdigest()

    def store_secret(self, key: str, value: str, scope: str = "global") -> dict[str, Any]:
        session = self._Session()
        try:
            existing = (
                session.query(SecretVaultModel).filter(SecretVaultModel.secret_key == key).first()
            )
            if existing:
                existing.encrypted_value = self._encrypt(value)
                existing.scope = scope
                existing.rotated_at = datetime.now(UTC)
            else:
                session.add(
                    SecretVaultModel(
                        secret_key=key,
                        encrypted_value=self._encrypt(value),
                        scope=scope,
                    )
                )
            session.commit()
            audit = PersistentAuditStore()
            audit.append("security.secret_stored", "system", {"key": key, "scope": scope})
            return {"key": key, "scope": scope, "stored": True}
        finally:
            session.close()

    def verify_secret(self, key: str, value: str) -> bool:
        session = self._Session()
        try:
            secret = (
                session.query(SecretVaultModel).filter(SecretVaultModel.secret_key == key).first()
            )
            if not secret:
                return False
            return secret.encrypted_value == self._encrypt(value)
        finally:
            session.close()

    def list_secrets(self) -> list[dict[str, Any]]:
        session = self._Session()
        try:
            secrets = session.query(SecretVaultModel).all()
            return [{"key": s.secret_key, "scope": s.scope} for s in secrets]
        finally:
            session.close()


class RateLimiter:
    """16.4: Rate Limiting — منع الإفراط في الطلبات."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        SecurityBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)
        self._authorizer = authorizer

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """المُصرِّحُ السياديُّ بالفاعلِ التنفيذيِّ الافتراضيّ — يُبنى عندَ أوّلِ حاجة (G1)."""
        if self._authorizer is None:
            self._authorizer = ConstitutionalAuthorizer()
        return self._authorizer

    def check_rate(
        self,
        identifier: str,
        endpoint: str,
        max_requests: int = 100,
        window_minutes: int = 1,
        operation_id: str | None = None,
    ) -> dict[str, Any]:
        """فحص معدل الطلبات.

        عبورٌ سياديٌّ (G1 § 9.10 · W-728): `log_isolated_action` رصدٌ لا منع —
        يكتبُ في مسارَي الكتابةِ (الزيادةُ · إنشاءُ الصفِّ) وحدَهما، ورفضُ
        تجاوُزِ السقفِ يقرأُ ويعودُ **بلا عبورٍ ولا كتابةٍ**. فحصُ الحدِّ ثمَّ
        الزيادةُ غيرُ ذرّيٍّ تحتَ التزامنِ كما اليوم — الحدُّ لا يغيِّرُ ذلك.
        """
        session = self._Session()
        try:
            from datetime import timedelta

            window_start = datetime.now(UTC) - timedelta(minutes=window_minutes)
            record = (
                session.query(RateLimitModel)
                .filter(
                    RateLimitModel.identifier == identifier,
                    RateLimitModel.endpoint == endpoint,
                    RateLimitModel.window_start >= window_start,
                )
                .first()
            )
            if record is not None and record.request_count >= max_requests:
                return {"allowed": False, "count": record.request_count, "max": max_requests}
            existed = record is not None
            previous_count = record.request_count if record is not None else 0
        finally:
            session.close()

        op = operation_id or uuid.uuid4().hex[:8]
        effect = declared_effect(
            "WRITE",
            f"rate:{identifier}/{endpoint}/count@{op}",
            "زيادةُ العدّادِ أو إنشاءُ صفِّ النافذة",
        )
        captured: list[int] = []

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                from datetime import timedelta

                window_start = datetime.now(UTC) - timedelta(minutes=window_minutes)
                row = (
                    session.query(RateLimitModel)
                    .filter(
                        RateLimitModel.identifier == identifier,
                        RateLimitModel.endpoint == endpoint,
                        RateLimitModel.window_start >= window_start,
                    )
                    .first()
                )
                if row is not None:
                    row.request_count += 1
                    row.last_request = datetime.now(UTC)
                    session.commit()
                    captured.append(row.request_count)
                else:
                    session.add(
                        RateLimitModel(
                            identifier=identifier,
                            endpoint=endpoint,
                            request_count=1,
                            window_start=datetime.now(UTC),
                        )
                    )
                    session.commit()
                    captured.append(1)
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(RateLimitModel)
                    .filter(
                        RateLimitModel.identifier == identifier,
                        RateLimitModel.endpoint == endpoint,
                    )
                    .first()
                )
                if row is None:
                    return
                if existed:
                    row.request_count = previous_count
                    session.commit()
                else:
                    session.delete(row)
                    session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_CHECK_RATE,
            f"rate:{identifier}/{endpoint}",
            declared_effects=(effect,),
            operation_key=operation_key(RATE_SCOPE, f"{identifier}/{endpoint}.{op}"),
            compensators=(compensator(effect.signature, _undo, "إعادةُ العدّادِ إلى لقطتِه"),),
            applier=_apply,
        )
        if guarded.is_replay:
            return {
                "allowed": True,
                "count": captured[0] if captured else 1,
                "max": max_requests,
                "replayed": True,
            }

        return {
            "allowed": True,
            "count": captured[0] if captured else 1,
            "max": max_requests,
        }


class TLSCertManager:
    """16.3: TLS Certificate Management."""

    def __init__(self, authorizer: ConstitutionalAuthorizer | None = None) -> None:
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        SecurityBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)
        self._authorizer = authorizer

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """المُصرِّحُ السياديُّ بالفاعلِ التنفيذيِّ الافتراضيّ — يُبنى عندَ أوّلِ حاجة (G1)."""
        if self._authorizer is None:
            self._authorizer = ConstitutionalAuthorizer()
        return self._authorizer

    def issue_certificate(
        self, common_name: str, validity_days: int = 365, operation_id: str | None = None
    ) -> dict[str, Any]:
        """إصدارُ شهادةٍ — عبورٌ سياديٌّ (G1 § 9.10 · W-728): `issue_certificate`
        منحُ ثقةٍ ممنوعٌ عندَ ≥3، ومعرِّفُ الشهادةِ يُشتقُّ من `operation_id`
        إن جاء (سابقةُ assign_agent) ليكونَ الإصدارُ المكرَّرُ إعادةً لا صفًّا ثانيًا.
        """
        from datetime import timedelta

        cert_id = operation_id or f"cert-{uuid.uuid4().hex[:10]}"
        cert_hash = hashlib.sha256(f"{common_name}:{cert_id}".encode()).hexdigest()
        valid_until = datetime.now(UTC) + timedelta(days=validity_days)
        effect = declared_effect("CREATE", f"cert:{cert_id}", f"cn: {common_name}")

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                cert = TLSCertificateModel(
                    cert_id=cert_id,
                    common_name=common_name,
                    cert_hash=cert_hash,
                    valid_until=valid_until,
                )
                session.add(cert)
                session.commit()
                audit = PersistentAuditStore()
                audit.append(
                    "security.cert_issued", "system", {"cert_id": cert_id, "cn": common_name}
                )
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(TLSCertificateModel)
                    .filter(TLSCertificateModel.cert_id == cert_id)
                    .first()
                )
                if row:
                    session.delete(row)
                    session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_ISSUE_CERTIFICATE,
            f"cert:{cert_id}",
            declared_effects=(effect,),
            operation_key=operation_key(CERT_ISSUE_SCOPE, cert_id),
            compensators=(compensator(effect.signature, _undo, "حذفُ صفِّ الشهادة"),),
            applier=_apply,
        )
        if guarded.is_replay:
            return {
                "cert_id": cert_id,
                "common_name": common_name,
                "valid_until": str(valid_until),
                "replayed": True,
            }

        return {
            "cert_id": cert_id,
            "common_name": common_name,
            "valid_until": str(valid_until),
        }

    def verify_certificate(self, cert_id: str) -> dict[str, Any]:
        """تحقُّقُ شهادةٍ — مساراتُ القراءةِ (سليمة · منتهيةٌ سلفًا · مجهولة)
        لا تعبرُ؛ ومسارُ الانتهاءِ وحدَهُ يعبُرُ بأثرٍ معلنٍ ومعوِّضٍ يعيدُ
        الحالةَ إلى «active» (G1 § 9.10 · W-728).
        """
        session = self._Session()
        try:
            cert = (
                session.query(TLSCertificateModel)
                .filter(TLSCertificateModel.cert_id == cert_id)
                .first()
            )
            if not cert:
                return {"valid": False, "reason": "not_found"}
            if cert.status != "active":
                return {"valid": False, "reason": cert.status}
            common_name = cert.common_name
            if cert.valid_until:
                valid_until = cert.valid_until
                if valid_until.tzinfo is None:
                    valid_until = valid_until.replace(tzinfo=UTC)
                expired = datetime.now(UTC) > valid_until
            else:
                expired = False
        finally:
            session.close()
        if not expired:
            return {"valid": True, "cert_id": cert_id, "common_name": common_name}

        effect = declared_effect("WRITE", f"cert:{cert_id}", "status.active->expired")

        def _apply(_effect: Any) -> None:
            session = self._Session()
            try:
                row = (
                    session.query(TLSCertificateModel)
                    .filter(TLSCertificateModel.cert_id == cert_id)
                    .first()
                )
                if row is None or row.status != "active":
                    raise RuntimeError("انكسارٌ داخلَ المُطبِّق — تبدَّلَ ما بُنيَ عليه الأثر")
                row.status = "expired"
                session.commit()
            finally:
                session.close()

        def _undo() -> None:
            session = self._Session()
            try:
                row = (
                    session.query(TLSCertificateModel)
                    .filter(TLSCertificateModel.cert_id == cert_id)
                    .first()
                )
                if row is not None:
                    row.status = "active"
                    session.commit()
            finally:
                session.close()

        guarded = self.authorizer.guard_declared(
            ACTION_VERIFY_CERTIFICATE,
            f"cert:{cert_id}",
            declared_effects=(effect,),
            operation_key=operation_key(CERT_EXPIRE_SCOPE, cert_id),
            compensators=(compensator(effect.signature, _undo, "إرجاعُ حالةِ الشهادةِ إلى active"),),
            applier=_apply,
        )
        if guarded.is_replay:
            return {"valid": False, "reason": "expired", "replayed": True}

        return {"valid": False, "reason": "expired"}


# Singletons
_rbac: RBACSystem | None = None
_vault: SecretVault | None = None
_limiter: RateLimiter | None = None
_tls: TLSCertManager | None = None


def get_rbac() -> RBACSystem:
    global _rbac
    if _rbac is None:
        _rbac = RBACSystem()
    return _rbac


def get_secret_vault() -> SecretVault:
    global _vault
    if _vault is None:
        _vault = SecretVault()
    return _vault


def get_rate_limiter() -> RateLimiter:
    global _limiter
    if _limiter is None:
        _limiter = RateLimiter()
    return _limiter


def get_tls_manager() -> TLSCertManager:
    global _tls
    if _tls is None:
        _tls = TLSCertManager()
    return _tls
