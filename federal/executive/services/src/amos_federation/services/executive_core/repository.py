"""الهدف: مستودع المهام للنواة التنفيذية — انتقال حالة ذرّي على مصدر الحقيقة.

النطاق: federal/executive/services — النواة التنفيذية
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-16
تاريخ آخر تعديل: 2026-08-18

`PersistentTaskStore.update_status` القائم يكتب الحالة الجديدة بلا شرط: يقرأ
الصفّ ثم يكتب. وذلك كافٍ لواجهة إدارية، وغير كافٍ لمحرّك تنفيذ: مُنفِّذان
يقرآن `dispatched` في اللحظة نفسها فيكتبان `executing` كلاهما، وتُنفَّذ المهمّة
مرتين — وهذا هو بالضبط ما يجعل «التنفيذ مرة واحدة» ادّعاءً لا خاصيّة.

فهذا المستودع يضيف ما تحتاجه النواة ولا يملكه المخزن العام:

1. `compare_and_set` — تحديث مشروط بـ`WHERE status = expected`، ويُرجع عدد
   الصفوف المتأثّرة. صفر يعني «سبقك غيرك»، لا يعني «نجح».
2. `claim_next` — التقاط مهمّة غير منتهية للتقدّم بها.
3. `list_unfinished` — أساس الاسترداد بعد إعادة التشغيل.
4. `delete` — معكوسُ `create` (أضافته 1N). ليس مرفقًا إداريًّا: خطّةُ التعويض
   (1I) لا تُربَط بأثرِ إنشاءٍ لا يملكُ معكوسًا، والدولةُ لا تدخلُ فعلًا لا تعرفُ
   كيف تخرجُ منه. فبلا هذه الدالّة كان إعلانُ `CREATE` سيُرفَض قبلَ التنفيذ.

ولا يُنشئ نموذجًا ثانيًا لجدول `tasks`: يستخدم `TaskModel` نفسه، احترامًا لقرار
الهجرة 004 (نموذج واحد مرجعي لهذا الجدول).
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from sqlalchemy import delete, update

from amos_federation.common.database import TaskModel, get_session_factory
from amos_federation.services.executive_core.sovereignty_bridge import (
    compensator,
    declared_effect,
    operation_key,
)
from amos_federation.services.executive_core.states import (
    TaskState,
    assert_transition,
    parse_state,
)

# ── E1 · أفعالُ عبورِ أسطحِ المستودعِ (WI-119 · تصميمُ W-694 · اعتمادُ المالكِ
# 2026-10-26) — الثلاثةُ محجوزةٌ منَ المستوىِ الرابعِ (صنفُ execute_task). ──────

ACTION_CREATE_TASK = "create_task"
ACTION_DELETE_TASK = "delete_task"
ACTION_TRANSITION_TASK_STATE = "transition_task_state"

TASK_CREATE_SCOPE = "tasks.create"
TASK_DELETE_SCOPE = "tasks.delete"
TASK_TRANSITION_SCOPE = "tasks.transition"

#: حاملُ المُصرِّحِ الافتراضيِّ للوحدةِ (نمطُ W-532).
_DEFAULT_AUTHORIZER = None


class TaskLedgerDivergenceError(RuntimeError):
    """سجلُّ الذرّيّةِ يقولُ «نجحت» والحقلُ الكانونيُّ مخالفٌ — تفرُّقٌ يُرفَعُ لا يُسكَتُ عنهُ.

    لا يُزعَمُ نجاحٌ لم يقعْ ولا يُعادُ التنفيذُ خارجَ الحدِّ: الحالةُ تحتاجُ
    استعادةً (1H) لا تجاهلًا. نمطُ `IdentityLedgerDivergenceError` (WI-082).
    """


class TaskNotFoundError(LookupError):
    """لا صفّ لهذه المهمّة في مصدر الحقيقة."""


def _row_as_dict(row: TaskModel) -> dict[str, Any]:
    return {
        "id": row.id,
        "type": row.type,
        "description": row.description,
        "status": row.status,
        "priority": row.priority,
        "domain": row.domain,
        "assigned_agent": row.assigned_agent,
        "plan": row.plan or [],
        "result": row.result or {},
        "tenant_id": row.tenant_id,
        "created_at": row.created_at.isoformat() if row.created_at else None,
        "updated_at": row.updated_at.isoformat() if row.updated_at else None,
    }


class ExecutiveTaskRepository:
    """قراءة وكتابة المهام لأجل النواة التنفيذية — على القاعدة لا على الذاكرة."""

    def _authorizer(self):
        """المُصرِّحُ الافتراضيُّ لأسطحِ الكتابةِ — كائنٌ واحدٌ للوحدةِ (نمطُ W-532)."""
        global _DEFAULT_AUTHORIZER
        if _DEFAULT_AUTHORIZER is None:
            from amos_federation.services.executive_core.sovereignty_bridge import (
                ConstitutionalAuthorizer,
            )

            _DEFAULT_AUTHORIZER = ConstitutionalAuthorizer(actor="EXECUTIVE")
        return _DEFAULT_AUTHORIZER

    def create(
        self,
        task_id: str,
        task_type: str,
        description: str,
        *,
        priority: str = "normal",
        domain: str = "general",
        tenant_id: str = "default",
        state: TaskState = TaskState.CREATED,
    ) -> dict[str, Any]:
        """إدراج مهمّة جديدة في القاعدة وإرجاع صفّها كما خُزِّن — عبر الحدّ السياديّ (E1).

        الفعلُ «create_task» (المستوى 4 من زرّ الإيقافِ · صنفُ execute_task) —
        والمعوّضُ يحذفُ الصفَّ المُنشَأ (معكوسُ الإنشاءِ الحقيقيِّ لا وعظٌ).
        """
        target = f"task:{task_id}"
        effect = declared_effect("CREATE", target, f"صفُّ مهمّةٍ «{task_type}» في مصدرِ الحقيقةِ الواحدِ")

        def _apply(_effect: Any) -> None:
            self._create_core(
                task_id,
                task_type,
                description,
                priority=priority,
                domain=domain,
                tenant_id=tenant_id,
                state=state,
            )

        def _delete_row() -> bool:
            session = get_session_factory()()
            try:
                result = session.execute(delete(TaskModel).where(TaskModel.id == task_id))
                session.commit()
                return bool(result.rowcount)
            finally:
                session.close()

        self._authorizer().guard_declared(
            ACTION_CREATE_TASK,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(TASK_CREATE_SCOPE, task_id),
            compensators=(
                compensator(
                    effect.signature,
                    _delete_row,
                    "حذفُ صفِّ المهمّةِ المُنشَأ — عكسٌ حقيقيٌّ للإنشاءِ",
                ),
            ),
        )
        return self.require(task_id)

    def _create_core(
        self,
        task_id: str,
        task_type: str,
        description: str,
        *,
        priority: str = "normal",
        domain: str = "general",
        tenant_id: str = "default",
        state: TaskState = TaskState.CREATED,
    ) -> None:
        """النواةُ الخاصةُ للإنشاءِ (تصميمُ E1 § 2.3): الكتابةُ الخامُ بلا عبورٍ.

        يستدعيها مَن عبرَ الحدَّ السياديَّ بمفعولِهِ المُعلَنِ (نمطُ «الأخيرُ
        تعلنُ كلَّ شيءٍ وتعبرُ مرةً واحدةً») — فلا عبورَ متعشِّقَ (WI-115 · Q-9).
        """
        session = get_session_factory()()
        try:
            session.add(
                TaskModel(
                    id=task_id,
                    type=task_type,
                    description=description,
                    status=state.value,
                    priority=priority,
                    domain=domain,
                    tenant_id=tenant_id,
                    plan=[],
                    result={},
                )
            )
            session.commit()
        finally:
            session.close()

    def get(self, task_id: str) -> dict[str, Any] | None:
        session = get_session_factory()()
        try:
            row = session.query(TaskModel).filter(TaskModel.id == task_id).first()
            return None if row is None else _row_as_dict(row)
        finally:
            session.close()

    def require(self, task_id: str) -> dict[str, Any]:
        """قراءة مهمّة أو رفع `TaskNotFoundError` — لا إرجاع صفّ فارغ يُقرأ كأنه مهمّة."""
        task = self.get(task_id)
        if task is None:
            raise TaskNotFoundError(f"لا مهمّة بالمعرّف: {task_id}")
        return task

    def state_of(self, task_id: str) -> TaskState:
        return parse_state(self.require(task_id)["status"])

    def compare_and_set(
        self,
        task_id: str,
        expected: TaskState,
        target: TaskState,
        **fields: Any,
    ) -> bool:
        """انتقال حالة ذرّي: ينجح مرّة واحدة فقط لكل حالة متوقَّعة.

        يتحقّق من مشروعية الانتقال أولًا (آلة الحالات)، ثم ينفّذ `UPDATE` مشروطًا
        بالحالة المتوقَّعة. الإرجاع `False` معناه أن أحدًا غيّر الحالة قبلنا —
        وليس معناه فشل الكتابة.
        """
        assert_transition(expected, target)
        values: dict[str, Any] = {
            "status": target.value,
            "updated_at": datetime.now(UTC),
        }
        values.update(fields)
        target_id = f"task:{task_id}"
        # موردُ الأثرِ يحملُ الاتجاهَ (موردٌ فرعيٌّ داخلَ نطاقِ الهدفِ — `in_scope`):
        # به تتميّزُ العقودُ بينَ انتقالينِ مختلفينِ للمهمّةِ نفسِها فلا يُرفَض
        # انتقالٌ مشروعٌ كإعادةِ إذنٍ في الثانيةِ نفسِها.
        effect = declared_effect(
            "WRITE",
            f"{target_id}/state.{expected.value}->{target.value}",
            f"انتقالٌ مشروطٌ {expected.value} → {target.value} في الحقلِ الكانونيِّ للحالةِ",
        )

        def _apply(_effect: Any) -> bool:
            return self._transition_core(task_id, expected, target, dict(fields or {}))

        def _reverse() -> bool:
            """انتقالٌ عكسيٌّ إلى الحالةِ المتوقَّعةِ — معوّضُ 1I الحقيقيُّ."""
            session = get_session_factory()()
            try:
                result = session.execute(
                    update(TaskModel)
                    .where(TaskModel.id == task_id, TaskModel.status == target.value)
                    .values(status=expected.value, updated_at=datetime.now(UTC))
                )
                session.commit()
                return bool(result.rowcount)
            finally:
                session.close()

        guarded = self._authorizer().guard_declared(
            ACTION_TRANSITION_TASK_STATE,
            target_id,
            declared_effects=(effect,),
            applier=_apply,
            # النطاقُ يحملُ الاتجاهَ (مفتاحُ التصميمِ § 2.2: انتقالُ المهمّةِ +
            # المعرِّفُ + المتوقَّعةُ + الهدفُ) — فالبصمةُ السياديّةُ تفرّقُ بينَ
            # اتجاهاتٍ مختلفةٍ للمهمّةِ نفسِها ولا يُرفَض عبورٌ مشروعٌ كإعادةِ إذنٍ.
            operation_key=operation_key(
                f"{TASK_TRANSITION_SCOPE}.{expected.value}->{target.value}", task_id
            ),
            compensators=(
                compensator(
                    effect.signature,
                    _reverse,
                    "انتقالٌ عكسيٌّ إلى الحالةِ المتوقَّعةِ — عكسٌ حقيقيٌّ للانتقالِ",
                ),
            ),
        )
        if guarded.is_replay:
            # الإعادةُ (تصميمُ E1 § 2.4): السجلُّ يُثبِتُ نجاحَ هذا الانتقالِ بهذا
            # المفتاحِ فلا يُطبَّقُ الأثرُ مرتينِ — لكنْ **شرطُ المقارنةِ لا تبتلعُهُ
            # الإعادةُ**: `compare_and_set` حارسُ التزامنِ الحقيقيُّ، فالحالةُ
            # المتوقَّعةُ إن لم تعدْ واقعةً فشرطُ الانتقالِ فشلَ ويُرجَعُ False
            # لا replay («يُرجَعُ False لا replay» — حرفُّ التصميمِ). وإن عادتِ
            # الحالةُ المتوقَّعةُ واقعةً معَ سجلٍّ ناجحٍ فهوَ تباعدٌ لا يُسكَتُ عنهُ.
            if self.state_of(task_id) is not expected:
                return False
            raise TaskLedgerDivergenceError(
                f"السجلُّ يُثبِتُ انتقالَ «{task_id}» إلى «{target.value}» "
                "والحقلُ الكانونيُّ عادَ إلى المتوقَّعةِ — تباعدٌ لا يُسكَتُ عنهُ (1H)"
            )
        return bool(guarded.value)

    def _transition_core(
        self,
        task_id: str,
        expected: TaskState,
        target: TaskState,
        fields: dict[str, Any] | None = None,
    ) -> bool:
        """النواةُ الخاصةُ للانتقالِ المشروطِ (تصميمُ E1 § 2.3): الكتابةُ الخامُ بلا عبورٍ.

        تبني قيمَ التحديثِ (الحالةُ + الختمُ الزمنيُّ + الحقولُ الإضافيّةُ) كما
        كان يفعلُ `compare_and_set` العلنيُّ — فدلالةُ المستدعي لا تتغيّرُ.
        """
        values: dict[str, Any] = {
            "status": target.value,
            "updated_at": datetime.now(UTC),
        }
        values.update(fields or {})
        session = get_session_factory()()
        try:
            result = session.execute(
                update(TaskModel)
                .where(TaskModel.id == task_id, TaskModel.status == expected.value)
                .values(**values)
            )
            session.commit()
            return bool(result.rowcount)
        finally:
            session.close()

    def delete(self, task_id: str) -> bool:
        """امحُ صفَّ مهمّةٍ — معكوسُ `create` وحدَه، لا أداةَ تنظيفٍ عامّة.

        يُستدعى من معوّضِ 1I عندَ فشلِ عمليّةٍ أعلنت أثرَ `CREATE`. الإرجاع
        `False` معناه لا صفَّ لِيُمحى (سبقَنا غيرُنا أو لم يُنشَأ قطُّ) — لا
        يعني فشلًا يُبتلَع، والمُنادي يقرؤه.
        """
        # قاعدةُ نطاقٍ **قبلَ الحدِّ (قراءةٌ لا كتابةٌ — نمطُ `register_identity`):
        # محوُ ما لا وجودَ لهُ ليس عمليّةً سياديّةً أصلًا — بل لا-عملٍ يُعادُ
        # بصمتٍ كما كان العقدُ العلنيُّ للدالةِ قبلَ E1، فلا يُستهلَك إذنٌ ولا
        # يُثبَّت مفتاحُ ذرّيّةٍ لما لم يقع.
        snapshot = self.get(task_id)
        if snapshot is None:
            return False

        target = f"task:{task_id}"
        effect = declared_effect("DELETE", target, "حذفُ صفِّ المهمّةِ من مصدرِ الحقيقةِ")

        def _apply(_effect: Any) -> bool:
            return self._delete_core(task_id)

        def _reinsert() -> bool:
            """إعادةُ إدراجِ لقطةِ الصفِّ المحذوفِ — عكسٌ حقيقيٌّ للحذفِ."""
            if snapshot is None:
                return False
            session = get_session_factory()()
            try:
                session.add(
                    TaskModel(
                        id=snapshot["id"],
                        type=snapshot["type"],
                        description=snapshot["description"],
                        status=snapshot["status"],
                        priority=snapshot["priority"],
                        domain=snapshot["domain"],
                        assigned_agent=snapshot["assigned_agent"],
                        plan=snapshot["plan"],
                        result=snapshot["result"],
                        tenant_id=snapshot["tenant_id"],
                    )
                )
                session.commit()
                return True
            finally:
                session.close()

        guarded = self._authorizer().guard_declared(
            ACTION_DELETE_TASK,
            target,
            declared_effects=(effect,),
            applier=_apply,
            operation_key=operation_key(TASK_DELETE_SCOPE, f"{task_id}:{snapshot['status']}"),
            compensators=(
                compensator(
                    effect.signature,
                    _reinsert,
                    "إعادةُ إدراجِ لقطةِ الصفِّ المحذوفِ — عكسٌ حقيقيٌّ للحذفِ",
                ),
            ),
        )
        if guarded.is_replay:
            # الإعادةُ (تصميمُ E1 § 2.4): السجلُّ يُثبِتُ حذفَ هذا الصفِّ فتُعادُ
            # نتيجتُهُ المسجَّلةُ (True) — والقيمةُ لا تُقرأُ منَ المُطبِّقِ (لم
            # يُشغَّلْ عندَ الإعادةِ) بل منَ السجلِّ المُثبِتِ.
            if self.get(task_id) is not None:
                raise TaskLedgerDivergenceError(
                    f"السجلُّ يُثبِتُ حذفَ «{task_id}» والصفُّ موجودٌ — تباعدٌ " "لا يُسكَتُ عنهُ (1H)"
                )
            return True
        return bool(guarded.value)

    def _delete_core(self, task_id: str) -> bool:
        """النواةُ الخاصةُ للحذفِ (تصميمُ E1 § 2.3): الكتابةُ الخامُ بلا عبورٍ."""
        session = get_session_factory()()
        try:
            result = session.execute(delete(TaskModel).where(TaskModel.id == task_id))
            session.commit()
            return bool(result.rowcount)
        finally:
            session.close()

    def list_unfinished(self, limit: int = 100) -> list[dict[str, Any]]:
        """المهام في حالة غير نهائية — أساس الاسترداد بعد إعادة التشغيل."""
        active = [
            TaskState.CREATED.value,
            TaskState.AUTHORIZED.value,
            TaskState.PLANNED.value,
            TaskState.DISPATCHED.value,
            TaskState.EXECUTING.value,
        ]
        session = get_session_factory()()
        try:
            rows = (
                session.query(TaskModel)
                .filter(TaskModel.status.in_(active))
                .order_by(TaskModel.created_at.asc())
                .limit(limit)
                .all()
            )
            return [_row_as_dict(row) for row in rows]
        finally:
            session.close()

    def list_by_state(self, state: TaskState, limit: int = 100) -> list[dict[str, Any]]:
        session = get_session_factory()()
        try:
            rows = (
                session.query(TaskModel).filter(TaskModel.status == state.value).limit(limit).all()
            )
            return [_row_as_dict(row) for row in rows]
        finally:
            session.close()
