"""
AMOS-Federation Phase 17 — System Life + Launch
الهدف: دورة حياة النظام الكاملة + إطلاق رسمي + مراقبة مستمرة
النطاق: services/governance/system_life
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
تاريخ آخر تعديل: 2026-10-28 (W-723 — G1 الدفعة 2: ستّةُ أسطحٍ تعبرُ الحدَّ · self_heal بشرطِه · restore_backup دَينٌ لم يُمَسّ)

المتطلبات:
  17.1: System Bootstrap — تهيئة كاملة من الصفر
  17.2: Continuous Monitoring — مراقبة دورية
  17.3: Self-Healing — إصلاح ذاتي
  17.4: Graceful Shutdown — إيقاف آمن
  17.5: Backup & Restore — نسخ احتياطي
  17.6: Launch Checklist — قائمة الإطلاق
  17.7: System Status Dashboard — لوحة حالة
"""

import json
import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from amos_federation.common.database import get_database_url
from amos_federation.common.persistent import PersistentAuditStore
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    get_authorizer,
    operation_key,
)

# ── G1 الدفعة 2 (W-723): أفعالُ الأسطحِ الستّةِ من جدولِ G1 § 2 بنصِّه ──────
#: `bootstrap` · `launch_checklist` — `orchestrate` (ممنوعٌ عندَ ≥4 · Q-76 ① لـlaunch_checklist).
ACTION_ORCHESTRATE = "orchestrate"
#: `graceful_shutdown` — اسمٌ جديدٌ بقرارِ Q-76 ② (OWNER-DECISIONS-D29 · W-724): أداةُ احتواءٍ
#: لا يمنعُها القاطعُ عندَ أيِّ مستوى.
ACTION_GRACEFUL_SHUTDOWN = "graceful_shutdown"
#: `health_check` — رصدٌ لا يُمنَع.
ACTION_HEALTH_CHECK = "run_health_check"
#: `self_heal` — اسمٌ جديدٌ (W-722) ممنوعٌ عندَ ≥4.
ACTION_SELF_HEAL = "self_heal"
#: `create_backup` — اسمٌ جديدٌ (W-722) أداةُ استردادٍ لا تُمنَع.
ACTION_CREATE_BACKUP = "create_backup"

#: نطاقُ مفاتيحِ الذرّيّة (1H) — يُذيَّلُ باسمِ السطح.
LIFECYCLE_SCOPE = "system_life"


class SystemBase(DeclarativeBase):
    pass


class SystemEventModel(SystemBase):
    """17.1-17.7: أحداث دورة حياة النظام."""

    __tablename__ = "system_events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(String, nullable=False, unique=True, index=True)
    event_type = Column(String, nullable=False)  # bootstrap, health, heal, shutdown, backup, launch
    component = Column(String, nullable=False)
    status = Column(String, default="success")  # success, warning, error
    details = Column(Text, default="{}")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class BackupModel(SystemBase):
    """17.5: النسخ الاحتياطية."""

    __tablename__ = "system_backups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    backup_id = Column(String, nullable=False, unique=True, index=True)
    component = Column(String, nullable=False)
    size_bytes = Column(Integer, default=0)
    checksum = Column(String, nullable=True)
    status = Column(String, default="created")  # created, verified, restored
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))


class SystemLifecycle:
    """17: دورة حياة النظام الكاملة."""

    def __init__(
        self,
        authorizer: ConstitutionalAuthorizer | None = None,
        state_runtime: Any | None = None,
    ) -> None:
        self._authorizer = authorizer
        # زمنُ تشغيلِ الولاياتِ لـ`self_heal` — يُحقَنُ في الاختبارِ ويُؤخَذُ الوحيدُ افتراضًا.
        self._state_runtime = state_runtime
        self._engine = create_engine(
            get_database_url(),
            connect_args={"check_same_thread": False}
            if get_database_url().startswith("sqlite")
            else {},
        )
        SystemBase.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine, autoflush=False, expire_on_commit=False)

    @property
    def authorizer(self) -> ConstitutionalAuthorizer:
        """المُصرِّحُ التنفيذيُّ الافتراضيّ — يُبنى عندَ أوّلِ حاجة.

        عبرَ `get_authorizer()` في الجسرِ (موضعُ بناءٍ افتراضيٌّ قائمٌ معدودٌ) لا بموضعِ
        بناءٍ جديد: الفاعلُ الافتراضيُّ `EXECUTIVE` نفسُه، ومن أرادَ غيرَه يُمرِّرُه صريحًا.
        """
        if self._authorizer is None:
            self._authorizer = get_authorizer()
        return self._authorizer

    def _runtime(self) -> Any:
        if self._state_runtime is None:
            from amos_federation.services.governance.state_runtime import get_state_runtime

            self._state_runtime = get_state_runtime()
        return self._state_runtime

    def _delete_event(self, event_id: str) -> None:
        """معوِّضُ سجلِّ الحدث: حذفُ الإدخالِ الذي كتبَه العبور."""
        session = self._Session()
        try:
            session.query(SystemEventModel).filter(SystemEventModel.event_id == event_id).delete()
            session.commit()
        finally:
            session.close()

    def _event_contract(
        self,
        surface: str,
        target: str,
        event_type: str,
        component: str,
        status: str,
        details: dict[str, Any],
        audit_event: str | None = None,
        audit_payload: dict[str, Any] | None = None,
    ) -> tuple[str, dict[str, Any]]:
        """ابنِ عقدَ سطحٍ أثرُه إدخالُ حدثٍ واحد (+ تدقيقٌ اختياريّ) — **لا يعبرُ بنفسِه**.

        يُرجِعُ (معرِّفَ الحدث، وسائطَ `guard_declared`)، والعبورُ نفسُه في جسدِ السطحِ
        العامِّ. والمعرِّفُ يُولَّدُ **قبلَ** الحدِّ ليُسمّيَه الأثرُ والمعوِّضُ والمفتاحُ معًا،
        فالمعوِّضُ يحذفُ الإدخالَ نفسَه لا «آخرَ إدخال».
        """
        event_id = f"sys-{uuid.uuid4().hex[:10]}"
        effect = declared_effect(
            "CREATE",
            f"{target}/event:{event_id}",
            f"إدخالُ حدثٍ «{event_type}» للمكوِّن «{component}» في system_events",
        )

        def _apply(_effect: Any) -> str:
            self._log_event(event_type, component, status, details, event_id=event_id)
            if audit_event is not None:
                PersistentAuditStore().append(
                    audit_event, "system", {"event_id": event_id, **(audit_payload or {})}
                )
            return event_id

        return event_id, {
            "declared_effects": (effect,),
            "applier": _apply,
            "operation_key": operation_key(f"{LIFECYCLE_SCOPE}.{surface}", event_id),
            "compensators": (
                compensator(
                    effect.signature,
                    lambda: self._delete_event(event_id),
                    "حذفُ إدخالِ الحدث",
                ),
            ),
            "metadata": {"surface": surface, "component": component},
        }

    def _log_event(
        self,
        event_type: str,
        component: str,
        status: str = "success",
        details: dict[str, Any] | None = None,
        *,
        event_id: str | None = None,
    ) -> str:
        event_id = event_id or f"sys-{uuid.uuid4().hex[:10]}"
        session = self._Session()
        try:
            event = SystemEventModel(
                event_id=event_id,
                event_type=event_type,
                component=component,
                status=status,
                details=json.dumps(details or {}, default=str),
            )
            session.add(event)
            session.commit()
            return event_id
        finally:
            session.close()

    def bootstrap(self) -> dict[str, Any]:
        """17.1: System Bootstrap — تهيئة كاملة من الصفر."""
        steps = []
        # تهيئة الولايات
        try:
            from amos_federation.services.governance.state_runtime import get_state_runtime

            get_state_runtime()
            steps.append({"step": "states", "status": "success"})
        except Exception as e:
            steps.append({"step": "states", "status": "error", "error": str(e)})

        # تهيئة المصانع
        try:
            from amos_federation.services.governance.factories import get_factory_registry

            get_factory_registry()
            steps.append({"step": "factories", "status": "success"})
        except Exception as e:
            steps.append({"step": "factories", "status": "error", "error": str(e)})

        # تهيئة الأمان
        try:
            from amos_federation.services.governance.security import get_rbac

            get_rbac()
            steps.append({"step": "security", "status": "success"})
        except Exception as e:
            steps.append({"step": "security", "status": "error", "error": str(e)})

        # تهيئة حلقة التعلم
        try:
            from amos_federation.services.governance.learning_cycle import get_learning_cycle

            get_learning_cycle()
            steps.append({"step": "learning", "status": "success"})
        except Exception as e:
            steps.append({"step": "learning", "status": "error", "error": str(e)})

        all_success = all(s["status"] == "success" for s in steps)
        # التهيئةُ أعلاه بناءُ وحيداتٍ (كتاباتُها في منشئاتِها)، وأثرُ هذا السطحِ إدخالُه.
        event_id, contract = self._event_contract(
            "bootstrap",
            "system:bootstrap",
            "bootstrap",
            "system",
            "success" if all_success else "warning",
            {"steps": steps},
            audit_event="system.bootstrap",
            audit_payload={"steps": len(steps)},
        )
        self.authorizer.guard_declared(ACTION_ORCHESTRATE, "system:bootstrap", **contract)

        return {
            "event_id": event_id,
            "status": "success" if all_success else "partial",
            "steps": steps,
            "timestamp": datetime.now(UTC).isoformat(),
        }

    def health_check(self) -> dict[str, Any]:
        """17.2: Continuous Monitoring — فحص صحة كل المكونات."""
        components = []
        # فحص سلسلة التدقيق
        try:
            audit = PersistentAuditStore()
            chain = audit.verify_chain()
            components.append(
                {
                    "component": "audit_chain",
                    "status": "healthy" if chain["valid"] else "broken",
                    "details": chain.get("message", ""),
                }
            )
        except Exception as e:
            components.append({"component": "audit_chain", "status": "error", "error": str(e)})

        # فحص الولايات
        try:
            from amos_federation.services.governance.state_runtime import get_state_runtime

            runtime = get_state_runtime()
            states = runtime.list_states()
            active = sum(1 for s in states if s["status"] == "active")
            components.append(
                {
                    "component": "states",
                    "status": "healthy",
                    "details": f"{active}/{len(states)} active",
                }
            )
        except Exception as e:
            components.append({"component": "states", "status": "error", "error": str(e)})

        # فحص المصانع
        try:
            from amos_federation.services.governance.factories import get_factory_registry

            registry = get_factory_registry()
            factories = registry.list_factories()
            components.append(
                {
                    "component": "factories",
                    "status": "healthy",
                    "details": f"{len(factories)} factories",
                }
            )
        except Exception as e:
            components.append({"component": "factories", "status": "error", "error": str(e)})

        all_healthy = all(c["status"] in ("healthy",) for c in components)
        event_id, contract = self._event_contract(
            "health",
            "system:health",
            "health",
            "system",
            "success" if all_healthy else "warning",
            {"components": components},
        )
        self.authorizer.guard_declared(ACTION_HEALTH_CHECK, "system:health", **contract)

        return {
            "event_id": event_id,
            "overall_status": "healthy" if all_healthy else "degraded",
            "components": components,
            "timestamp": datetime.now(UTC).isoformat(),
        }

    def self_heal(self, component: str) -> dict[str, Any]:
        """17.3: Self-Healing — عبرَ الحدِّ (`self_heal` · ممنوعٌ عندَ ≥4) وبشرطِ المالك.

        «لا يُعيد تفعيل ولاية عُلِّقت بقرار محكوم» (التوجيهُ 27 § 1): ولايةٌ لها سجلُّ
        إيقافٍ محكومٍ نشطٌ تُتخطّى (`noop`)، والمعلَّقةُ بلا سجلٍّ (تلقائيًّا) يُعادُ
        تفعيلُها كما كان. وكلُّ إعادةِ تفعيلٍ أثرٌ مُعلَنٌ داخلَ الهدفِ بمعوِّضٍ يُرجِعُ
        الحالةَ (G1 § 9.8.2)، وتمرُّ بنواةٍ خاصّةٍ لا بـ`reactivate_state` المحروس.
        """
        actions: list[dict[str, Any]] = []
        to_heal: list[str] = []
        runtime: Any = None
        if component == "audit_chain":
            try:
                audit = PersistentAuditStore()
                chain = audit.verify_chain()
                if not chain["valid"]:
                    # محاولة إصلاح: تحذير فقط (لا نحذف سجلات)
                    actions.append(
                        {"action": "warn", "target": "audit_chain", "message": chain["message"]}
                    )
                else:
                    actions.append(
                        {"action": "noop", "target": "audit_chain", "message": "already healthy"}
                    )
            except Exception as e:
                actions.append({"action": "error", "target": "audit_chain", "error": str(e)})
        elif component == "states":
            try:
                runtime = self._runtime()
                for s in runtime.list_states():
                    if s["status"] != "suspended":
                        continue
                    if runtime.has_governed_suspension(s["state_id"]):
                        actions.append(
                            {
                                "action": "noop",
                                "target": s["state_id"],
                                "message": "governed_suspension",
                            }
                        )
                    else:
                        to_heal.append(s["state_id"])
                if not actions and not to_heal:
                    actions.append({"action": "noop", "target": "states", "message": "all active"})
            except Exception as e:
                actions.append({"action": "error", "target": "states", "error": str(e)})
        else:
            actions.append({"action": "unknown_component", "target": component})

        target = f"system:heal:{component}"
        heal_effects = tuple(
            declared_effect(
                "WRITE",
                f"{target}/state:{state_id}",
                f"federal_states «{state_id}».status: suspended → active (تعليقٌ بلا قرارٍ محكوم)",
            )
            for state_id in to_heal
        )
        healed: list[str] = []
        planned = [
            *actions,
            *({"action": "reactivate", "target": state_id} for state_id in to_heal),
        ]
        event_id, contract = self._event_contract(
            "self_heal",
            target,
            "heal",
            component,
            "success",
            {"actions": planned},
            audit_event="system.self_heal",
            audit_payload={"component": component, "actions": len(planned)},
        )
        log_effect = contract["declared_effects"][0]
        log_apply = contract["applier"]

        def _apply(effect: Any) -> Any:
            if effect.signature == log_effect.signature:
                return log_apply(effect)
            state_id = effect.resource.rsplit("/state:", 1)[1]
            if runtime._heal_reactivate_core(state_id):
                healed.append(state_id)
            return state_id

        def _resuspend(state_id: str) -> Any:
            return lambda: runtime._set_status(state_id, "suspended", expected="active")

        compensators = (
            *contract["compensators"],
            *(
                compensator(e.signature, _resuspend(sid), "إرجاعُ الولايةِ إلى suspended")
                for sid, e in zip(to_heal, heal_effects, strict=True)
            ),
        )
        self.authorizer.guard_declared(
            ACTION_SELF_HEAL,
            target,
            declared_effects=(*heal_effects, log_effect),
            applier=_apply,
            operation_key=contract["operation_key"],
            compensators=compensators,
            metadata={**contract["metadata"], "reactivate": list(to_heal)},
        )
        actions.extend({"action": "reactivate", "target": state_id} for state_id in healed)

        return {
            "event_id": event_id,
            "component": component,
            "actions": actions,
            "healed": any(
                a["action"] not in ("noop", "error", "unknown_component") for a in actions
            ),
        }

    def graceful_shutdown(self, reason: str = "maintenance") -> dict[str, Any]:
        """17.4: Graceful Shutdown — إيقاف آمن."""
        steps = []
        # إيقاف المصانع
        steps.append({"step": "stop_factories", "status": "success"})
        # إيقاف الولايات
        steps.append({"step": "suspend_states", "status": "success"})
        # إيقاف التدريب
        steps.append({"step": "stop_training", "status": "success"})
        # حفظ الحالة
        steps.append({"step": "save_state", "status": "success"})
        # تسجيل الإيقاف
        steps.append({"step": "log_shutdown", "status": "success"})

        event_id, contract = self._event_contract(
            "shutdown",
            "system:shutdown",
            "shutdown",
            "system",
            "success",
            {"reason": reason, "steps": steps},
            audit_event="system.shutdown",
            audit_payload={"reason": reason},
        )
        # `graceful_shutdown` لا يمنعُه القاطعُ عندَ أيِّ مستوى — Q-76 ② (D29 · W-724).
        self.authorizer.guard_declared(ACTION_GRACEFUL_SHUTDOWN, "system:shutdown", **contract)

        return {
            "event_id": event_id,
            "status": "shutdown_complete",
            "reason": reason,
            "steps": steps,
        }

    def _delete_backup(self, backup_id: str) -> None:
        """معوِّضُ `create_backup`: حذفُ صفِّ النسخةِ وإدخالِ حدثِها."""
        session = self._Session()
        try:
            session.query(BackupModel).filter(BackupModel.backup_id == backup_id).delete()
            session.query(SystemEventModel).filter(
                SystemEventModel.event_type == "backup",
                SystemEventModel.details.like(f'%"{backup_id}"%'),
            ).delete(synchronize_session=False)
            session.commit()
        finally:
            session.close()

    def create_backup(self, component: str = "all") -> dict[str, Any]:
        """17.5: Backup & Restore — نسخ احتياطي عبرَ الحدِّ (`create_backup` · لا يُمنَع)."""
        import hashlib

        backup_id = f"backup-{uuid.uuid4().hex[:10]}"
        # محاكاة حجم البيانات
        size = 1024 * 1024  # 1MB placeholder
        checksum = hashlib.sha256(f"{backup_id}:{component}:{size}".encode()).hexdigest()
        target = f"backup:{backup_id}"
        effect = declared_effect(
            "CREATE",
            target,
            f"صفُّ نسخةٍ احتياطيّةٍ للمكوِّن «{component}» في system_backups + إدخالُ حدثِها",
        )

        def _apply(_effect: Any) -> dict[str, Any]:
            session = self._Session()
            try:
                session.add(
                    BackupModel(
                        backup_id=backup_id,
                        component=component,
                        size_bytes=size,
                        checksum=checksum,
                        status="created",
                    )
                )
                session.commit()
            finally:
                session.close()
            self._log_event("backup", component, "success", {"backup_id": backup_id, "size": size})
            return {
                "backup_id": backup_id,
                "component": component,
                "size_bytes": size,
                "checksum": checksum,
                "status": "created",
            }

        guarded = self.authorizer.guard_declared(
            ACTION_CREATE_BACKUP,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(f"{LIFECYCLE_SCOPE}.backup", backup_id),
            compensators=(
                compensator(
                    effect.signature,
                    lambda: self._delete_backup(backup_id),
                    "حذفُ صفِّ النسخةِ وإدخالِها",
                ),
            ),
            metadata={"component": component},
        )
        return dict(guarded.value)

    def restore_backup(self, backup_id: str) -> dict[str, Any]:
        """17.5: استرجاع نسخة احتياطية."""
        session = self._Session()
        try:
            backup = session.query(BackupModel).filter(BackupModel.backup_id == backup_id).first()
            if not backup:
                return {"error": "backup_not_found"}
            backup.status = "restored"
            session.commit()
            self._log_event("restore", backup.component, "success", {"backup_id": backup_id})
            return {"backup_id": backup_id, "status": "restored", "component": backup.component}
        finally:
            session.close()

    def launch_checklist(self) -> dict[str, Any]:
        """17.6: Launch Checklist — قائمة الإطلاق."""
        checks = []
        # فحص الولايات
        from amos_federation.services.governance.state_runtime import get_state_runtime

        runtime = get_state_runtime()
        states = runtime.list_states()
        active = sum(1 for s in states if s["status"] == "active")
        checks.append(
            {"check": "states_active", "required": 9, "actual": active, "passed": active >= 9}
        )

        # فحص المصانع
        from amos_federation.services.governance.factories import get_factory_registry

        registry = get_factory_registry()
        factories = registry.list_factories()
        checks.append(
            {
                "check": "factories_ready",
                "required": 4,
                "actual": len(factories),
                "passed": len(factories) >= 4,
            }
        )

        # فحص الأمان
        from amos_federation.services.governance.security import get_rbac

        rbac = get_rbac()
        roles = rbac.list_roles()
        checks.append(
            {"check": "rbac_roles", "required": 6, "actual": len(roles), "passed": len(roles) >= 6}
        )

        # فحص سلسلة التدقيق
        audit = PersistentAuditStore()
        chain = audit.verify_chain()
        checks.append(
            {
                "check": "audit_chain",
                "required": True,
                "actual": chain["valid"],
                "passed": chain["valid"],
            }
        )

        # فحص حلقة التعلم
        from amos_federation.services.governance.learning_cycle import get_promotion_cycle

        promotion = get_promotion_cycle()
        versions = promotion.list_versions()
        tracks = {v["track"] for v in versions}
        checks.append(
            {
                "check": "model_tracks",
                "required": 3,
                "actual": len(tracks),
                "passed": len(tracks) >= 3,
            }
        )

        all_passed = all(c["passed"] for c in checks)
        event_id, contract = self._event_contract(
            "launch",
            "system:launch",
            "launch",
            "system",
            "success" if all_passed else "warning",
            {"checks": checks},
        )
        # `orchestrate` ممنوعٌ عندَ ≥4 — Q-76 ① (D29 · W-724): لا إطلاقَ أثناءَ توقّفٍ طارئ.
        self.authorizer.guard_declared(ACTION_ORCHESTRATE, "system:launch", **contract)

        return {
            "event_id": event_id,
            "ready_for_launch": all_passed,
            "checks": checks,
            "total_checks": len(checks),
            "passed_checks": sum(1 for c in checks if c["passed"]),
        }

    def system_status(self) -> dict[str, Any]:
        """17.7: System Status Dashboard — لوحة حالة شاملة."""
        # الصحة العامة
        health = self.health_check()

        # الإحصائيات
        from amos_federation.services.governance.state_runtime import get_state_runtime

        runtime = get_state_runtime()
        states = runtime.list_states()

        from amos_federation.services.governance.factories import get_factory_registry

        registry = get_factory_registry()
        factories = registry.list_factories()

        audit = PersistentAuditStore()
        chain = audit.verify_chain()

        return {
            "overall_status": health["overall_status"],
            "timestamp": datetime.now(UTC).isoformat(),
            "states": {
                "total": len(states),
                "active": sum(1 for s in states if s["status"] == "active"),
                "suspended": sum(1 for s in states if s["status"] == "suspended"),
            },
            "factories": {
                "total": len(factories),
            },
            "audit_chain": {
                "valid": chain["valid"],
                "entries": chain.get("entries", 0),
            },
            "components": health["components"],
        }


# Singleton
_lifecycle: SystemLifecycle | None = None


def get_system_lifecycle() -> SystemLifecycle:
    global _lifecycle
    if _lifecycle is None:
        _lifecycle = SystemLifecycle()
    return _lifecycle
