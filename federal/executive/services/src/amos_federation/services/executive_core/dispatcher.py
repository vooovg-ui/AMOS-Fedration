"""الهدف: توزيع المهمّة على وكيل مؤهَّل فعلًا — من سجل الوكلاء في القاعدة.

النطاق: federal/executive/services — النواة التنفيذية
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-16
تاريخ آخر تعديل: 2026-08-16

حقيقة مقيسة قبل هذه الوحدة: جدول `agents` مُعرَّف في `common/database.py` ولم
يكن **أي** ملف في الخدمات يقرأ منه أو يكتب فيه (`grep AgentModel` = تعريفه
وحده). في المقابل كان المنسّق يضع في خطته أسماء وكلاء نصيّة ثابتة
(`worker-researcher`, `critic-001`) لا وجود لها في أي سجل. أي أن «تعيين وكيل»
كان سلسلة نصّية، لا قرارًا مبنيًّا على قدرة مُسجَّلة.

فهذه الوحدة أول مستهلك حقيقي لسجل الوكلاء:

- الاختيار بالقدرة: أدوات الخطة ⊆ أدوات الوكيل المسموحة (أو `*`).
- الاختيار بالحالة: الوكلاء المعزولون/المسحوبون لا يُختارون.
- عند عدم وجود وكيل مؤهَّل: `NoEligibleAgentError` — والمهمّة تسقط صريحًا. لا يُخترَع
  وكيل، ولا يُنفَّذ بوكيل وهمي، ولا تُخفَّض متطلّبات الأداة لتناسب الموجود.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from amos_federation.common.database import AgentModel, get_session_factory
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)

#: الحالات التي يُقبل معها ترشيح الوكيل للعمل.
#: `employed` أُضيفت في R4: كانت حالة تخرّج في `agent_population` وحده، فكان
#: الوكيل المتخرِّج يسقط من الترشيح بعد توحيد دورة الحياة في `agents.status`.
EMPLOYABLE_STATUSES = frozenset({"registered", "active", "promoted", "ready", "employed"})

#: صلاحية شاملة — يستخدمها التاج والوكلاء العامّون في هذا المستودع.
WILDCARD = "*"


class NoEligibleAgentError(RuntimeError):
    """لا وكيل مُسجَّل يملك القدرة المطلوبة — فلا توزيع ولا تنفيذ."""


@dataclass(frozen=True)
class AgentAssignment:
    """قرار توزيع: من، وبأي صلاحيات، ولماذا هو مؤهَّل."""

    agent_id: str
    agent_role: str
    permissions: tuple[str, ...]
    allowed_tools: tuple[str, ...]
    required_tools: tuple[str, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "agent_role": self.agent_role,
            "permissions": list(self.permissions),
            "allowed_tools": list(self.allowed_tools),
            "required_tools": list(self.required_tools),
        }


def required_tools_of(plan: list[dict[str, Any]]) -> tuple[str, ...]:
    """أدوات الخطة بالترتيب وبلا تكرار."""
    seen: list[str] = []
    for step in plan:
        tool = str(step.get("tool", "")).strip()
        if tool and tool not in seen:
            seen.append(tool)
    return tuple(seen)


#: الفعلُ السياديُّ لتسجيلِ الوكيلِ في الموزِّعِ (E1 · WI-119 · تصميمُ W-694 ·
#: اعتمادُ المالكِ 2026-10-26): يعيدُ استعمالَ «spawn_agent» القائمِ (المستوى 3
#: من زرِّ الإيقافِ) لأنَّهُ إنشاءُ صفِّ وكيلٍ في السجلِّ الكانونيِّ — نفسُ صنفِ
#: `register_identity` المحروسِ بـWI-082.
ACTION_SPAWN_AGENT = "spawn_agent"

#: نطاقُ مفتاحِ الذرّيّةِ لتسجيلِ الوكيلِ في الموزِّعِ: القيمةُ هي `agent_id`.
DISPATCHER_SPAWN_SCOPE = "dispatcher.agent.spawn"


#: المُصرِّحُ الافتراضيُّ لتسجيلِ الوكيلِ — كائنٌ واحدٌ للوحدةِ (نمطُ W-532).
_DEFAULT_AUTHORIZER: ConstitutionalAuthorizer | None = None


def _default_authorizer() -> ConstitutionalAuthorizer:
    global _DEFAULT_AUTHORIZER
    if _DEFAULT_AUTHORIZER is None:
        _DEFAULT_AUTHORIZER = ConstitutionalAuthorizer(actor="EXECUTIVE")
    return _DEFAULT_AUTHORIZER


def register_agent(
    agent_id: str,
    name: str,
    role: str,
    *,
    permissions: list[str] | None = None,
    allowed_tools: list[str] | None = None,
    status: str = "registered",
    token_budget: int = 10_000,
    tenant_id: str = "default",
    authorizer: ConstitutionalAuthorizer | None = None,
) -> dict[str, Any]:
    """تسجيل وكيل في القاعدة — الطريق الوحيد ليصبح قابلًا للتوزيع — عبر الحدّ السياديّ (E1).

    الكتابةُ (CREATE/MERGE لصفِّ الوكيلِ في `agents`) لا تقعُ إلّا بإذنٍ دستوريٍّ
    بالفعلِ «spawn_agent» القائمِ (المستوى 3 · صنفُ register_identity المحروسِ
    بـWI-082 · تصميمُ E1 § 2.2) — فالفاعلُ تنفيذيٌّ والمعوِّضُ يحذفُ الصفَّ.
    """
    actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
    target = f"agent:{agent_id}"
    effect = declared_effect("CREATE", target, f"صفُّ وكيلٍ «{name}» في السجلِّ الكانونيِّ للموزِّعِ")

    def _apply(_effect: Any) -> None:
        session = get_session_factory()()
        try:
            session.merge(
                AgentModel(
                    id=agent_id,
                    name=name,
                    role=role,
                    status=status,
                    permissions=permissions or [],
                    allowed_tools=allowed_tools or [],
                    token_budget=token_budget,
                    tenant_id=tenant_id,
                )
            )
            session.commit()
        finally:
            session.close()

    def _delete_row() -> bool:
        session = get_session_factory()()
        try:
            row = session.get(AgentModel, agent_id)
            if row is None:
                return False
            session.delete(row)
            session.commit()
            return True
        finally:
            session.close()

    actor_authorizer.guard_declared(
        ACTION_SPAWN_AGENT,
        target,
        declared_effects=(effect,),
        applier=_apply,
        operation_key=operation_key(DISPATCHER_SPAWN_SCOPE, agent_id),
        compensators=(
            compensator(
                effect.signature,
                _delete_row,
                "حذفُ صفِّ الوكيلِ المُنشَأ — عكسٌ حقيقيٌّ للتسجيلِ",
            ),
        ),
    )
    return {
        "agent_id": agent_id,
        "name": name,
        "role": role,
        "status": status,
        "permissions": permissions or [],
        "allowed_tools": allowed_tools or [],
        "tenant_id": tenant_id,
    }


def _covers(allowed: list[str], required: tuple[str, ...]) -> bool:
    if WILDCARD in allowed:
        return True
    return set(required).issubset(set(allowed))


class CapabilityDispatcher:
    """يختار وكيلًا من سجل الوكلاء بناءً على أدوات الخطة."""

    def __init__(self, employable_statuses: frozenset[str] = EMPLOYABLE_STATUSES) -> None:
        self._statuses = employable_statuses

    def candidates(self, tenant_id: str = "default") -> list[AgentModel]:
        session = get_session_factory()()
        try:
            return (
                session.query(AgentModel)
                .filter(
                    AgentModel.tenant_id == tenant_id,
                    AgentModel.status.in_(sorted(self._statuses)),
                )
                .order_by(AgentModel.created_at.asc())
                .all()
            )
        finally:
            session.close()

    def available_agents(self, tenant_id: str = "default") -> list[dict[str, Any]]:
        """الوكلاء القابلون للتوزيع فعلًا — نفس مصدر `select` لا قائمة موازية.

        أُضيفت في R1 لتعرض `agent-runtime` ما يمكن توزيعه حقًّا، بدل القائمة
        النصّية الثابتة التي كانت تعرضها ولا علاقة لها بسجل الوكلاء.
        """
        return [
            {
                "id": row.id,
                "role": row.role,
                "status": row.status,
                "allowed_tools": list(row.allowed_tools or []),
            }
            for row in self.candidates(tenant_id)
        ]

    def assignment_for(
        self,
        agent_id: str,
        plan: list[dict[str, Any]],
        *,
        tenant_id: str = "default",
    ) -> AgentAssignment:
        """إعادة قراءة تعيين وكيل **مُسمّى** من السجل لحظة التنفيذ.

        أُضيفت في R3 لأن مسار التنفيذ كان يُلفّق تعيينًا من أدوات الخطة نفسها بعد
        أن يُلقي تعيين التوزيع الحقيقي. هنا تُقرأ صلاحيات الوكيل وأدواته المسموحة
        **كما هي في القاعدة الآن**، لا كما كانت لحظة التوزيع ولا كما تشتهي الخطة.

        لا يُخفَّض المتطلَّب ولا يُستبدَل الوكيل: هذه الدالة لا تختار بديلًا. إن لم
        يكن الوكيل مُسجَّلًا أو خرج من حالات التشغيل (عزل، تقاعد) فالتنفيذ يسقط.

        Raises:
            NoEligibleAgentError: الوكيل غير موجود في السجل أو حالته غير قابلة
                للتشغيل. تغطية الأدوات تُفحَص عند حدّ بيئة التشغيل fail-closed.
        """
        session = get_session_factory()()
        try:
            row = (
                session.query(AgentModel)
                .filter(AgentModel.id == agent_id, AgentModel.tenant_id == tenant_id)
                .first()
            )
        finally:
            session.close()
        if row is None:
            raise NoEligibleAgentError(f"الوكيل غير مُسجَّل في السجل: {agent_id}")
        if row.status not in self._statuses:
            raise NoEligibleAgentError(f"حالة الوكيل {agent_id} غير قابلة للتشغيل: {row.status}")
        return AgentAssignment(
            agent_id=row.id,
            agent_role=row.role,
            permissions=tuple(row.permissions or []),
            allowed_tools=tuple(row.allowed_tools or []),
            required_tools=required_tools_of(plan),
        )

    def select(
        self,
        plan: list[dict[str, Any]],
        *,
        tenant_id: str = "default",
        preferred_agent: str | None = None,
    ) -> AgentAssignment:
        """اختيار وكيل مؤهَّل، أو رفع `NoEligibleAgentError` صريحًا.

        `preferred_agent` تفضيل لا أمر: إن كان الوكيل المفضَّل غير مؤهَّل للأدوات
        المطلوبة فلا يُختار — التفضيل لا يلغي القدرة.
        """
        required = required_tools_of(plan)
        rows = self.candidates(tenant_id)
        eligible = [row for row in rows if _covers(list(row.allowed_tools or []), required)]
        if not eligible:
            registered = len(rows)
            raise NoEligibleAgentError(
                "لا وكيل مؤهَّل للأدوات المطلوبة "
                f"({', '.join(required) or 'بلا أدوات'}) — "
                f"وكلاء مرشَّحون في السجل: {registered}"
            )
        chosen = next((row for row in eligible if row.id == preferred_agent), eligible[0])
        return AgentAssignment(
            agent_id=chosen.id,
            agent_role=chosen.role,
            permissions=tuple(chosen.permissions or []),
            allowed_tools=tuple(chosen.allowed_tools or []),
            required_tools=required,
        )
