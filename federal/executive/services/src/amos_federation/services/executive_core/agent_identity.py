"""الهدف: مصدر حقيقة واحد لهوية الوكيل — وسكّان النظام كإسقاط عنه.

النطاق: federal/executive/services — النواة التنفيذية
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-16
تاريخ آخر تعديل: 2026-10-20 (W-532 — المُصرِّحُ الافتراضيُّ كائنٌ واحدٌ للوحدةِ بالقياسِ ·
قرارُ المالكِ Q-62 ② · فوقَ استعادةِ 1c52572 في W-531) · ووقبله 2026-10-17 (W-402 — WI-082: هجرةُ register_identity عبرَ الحدِّ
السياديِّ بالفعلِ «spawn_agent» بقرارِ المالكِ Q-15 ① · بلا مساسٍ بالاثنَينِ
الباقيَينِ المعلَّقَينِ على حسمِ التسميةِ عندَ المالكِ)

حقائق مقيسة قبل هذه الوحدة (R4-A):

- كان هناك **سجلّان** يُنشئان هوية وكيل ويحفظانها:
  1. جدول `agents` عبر `AgentModel` في `common/database.py`، يُكتب فقط من
     `dispatcher.register_agent`، ويُقرأ من `CapabilityDispatcher.candidates /
     available_agents / select / assignment_for` — أي أن مسار التنفيذ الفعلي
     (Dispatcher → Runtime Gateway، R1–R3) لا يعرف غيره.
  2. جدول `agent_population` في `agent_runtime/population.py`، بمحرِّك
     SQLAlchemy وقاعدة تعريف (`PopulationBase`) خاصّين به، يولّد `agent_id`
     بنفسه ولا يشارك المعرّف مع `agents`. ويُقرأ من: `health.py`،
     `control_console/main.py`، `governance/expansion.py`،
     `governance/federation.py`، `governance/treasury.py`، و SQL خام في
     `royal/main.py`.
- النتيجة المقيسة: هويّتان لنفس الوكيل، دورتا حياة مختلفتان (`agents.status`
  مقابل `agent_population.state`)، وعدّادان مختلفان للسكّان.
- لا توجد أي `ForeignKey` في المستودع تشير إلى أيّ من الجدولين (`grep
  "ForeignKey(" federal/` = صفر نتائج)، فالتوحيد لا يكسر قيودًا مرجعية.

**القرار (R4-B) مبنيّ على البنية الموجودة لا على تفضيل شكلي:** الجدول
`agents` هو المصدر الكانوني لهوية الوكيل، لأنه:

1. الجدول الوحيد الذي يقرأه مسار التنفيذ المعتمد (توزيع → تعيين → تشغيل).
2. يسكن نفس `get_session_factory()` الذي تسكنه `tasks`، فقراءة الهوية لحظة
   التنفيذ تجري على نفس المحرِّك لا على محرِّك ثانٍ.
3. يحفظ الصلاحيات والأدوات في أعمدة `JSON` مكتوبة، لا نصًّا يُفكّ يدويًّا.

و`agent_population` **ليس** سجل هوية ثانيًا بعد R4: صار جدول **ملفّ تدريبي
وإسقاط للقراءة** (category، school_score، specialization، tokens_used،
graduated_at) مفتاحه هو نفس `agent_id` الكانوني. أعمدته المكرّرة (name، role،
permissions، allowed_tools، state) تبقى مكتوبة كـ **مرآة توافُقية مهجورة
(deprecated mirror)** لقرّاء خارج هذا المستودع، ولا يُقرأ منها شيء هنا.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from amos_federation.common.database import AgentModel, get_session_factory
from amos_federation.services.executive_core.dispatcher import EMPLOYABLE_STATUSES
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)

#: اسم الجدول الكانوني للهوية.
CANONICAL_IDENTITY_TABLE = "agents"

#: جدول صار إسقاطًا وملفًّا تدريبيًّا — ليس مصدر هوية.
PROJECTION_TABLE = "agent_population"

#: قيمة تُكتب حين لا تتوفّر المعلومة — لا تُختلق.
UNKNOWN = "UNKNOWN"

#: تصنيف أمانة الإسقاط السكّاني: مبنيّ على السجل الكانوني فعلًا.
POPULATION_FIDELITY = "REAL"

#: نشاط التشغيل (executing/failed) يُقرأ من أحداث دورة الحياة المسجَّلة في R3.
RUNTIME_ACTIVITY_SUBJECT = "amos_federation.executive.agent_lifecycle"

#: فاعلُ إنشاءِ الهويّة (WI-082 · قرارُ المالكِ Q-15 ①): إنشاءُ هويةِ وكيلٍ في
#: السجلِّ الكانونيِّ عملُ السلطةِ التنفيذيّةِ، فالفاعلُ يُعلَنُ تنفيذيًّا ولا يُثبَّتُ —
#: المُصرِّحُ يبقى قابلاً للتمريرِ صراحةً (`authorizer`) والافتراضُ لا يوسِّعُ شيئًا.
AGENT_IDENTITY_ACTOR = "EXECUTIVE"

#: الفعلُ السياديُّ لإنشاءِ الهويّة — قرارُ المالكِ Q-15 ①: يُعلَنُ إنشاءُ الهويّةِ
#: بالفعلِ «spawn_agent» فيقفُ عندَ المستوى الثالثِ من زرِّ الإيقافِ (المادةُ الثامنة).
#: ولا يُسمَّى باسمٍ نطاقيٍّ هروبًا من الدستورِ: البوابةُ تعرفُ هذا الاسمَ فعلًا.
ACTION_SPAWN_AGENT = "spawn_agent"

#: نطاقُ مفتاحِ الذرّيّةِ لإنشاءِ الهويّةِ (1H): القيمةُ هي `agent_id` الكانونيُّ —
#: الهويةُ الواحدةُ لا تُنشأُ مرتَينِ لمفتاحٍ واحد.
IDENTITY_SPAWN_SCOPE = "agents.identity.spawn"


# ── E1 · أفعالُ عبورِ الأسطحِ المباشرةِ تحتَ D-4 (WI-119 · تصميمُ W-694 ·
# اعتمادُ المالكِ 2026-10-26: «اعتمادُ تصميمِ E1 (13 اسمًا)») ──────────────────────

#: تحديثُ الهويّةِ (الحقولُ المصرَّحَةُ) — المستوى 3 (صنفُ spawn_agent).
ACTION_UPDATE_AGENT_IDENTITY = "update_agent_identity"

#: نطاقُ مفتاحِ الذرّيّةِ لتحديثِ الهويّةِ: القيمةُ بصمةُ الحقولِ المطلوبةِ —
#: فإعادةُ الإرسالِ إعادةٌ واحدةٌ والتحديثُ المختلفُ عمليّةٌ لاحقةٌ مشروعةٌ.
IDENTITY_UPDATE_SCOPE = "agents.identity.update"

#: احتواءُ الوكيلِ (PAUSED/RETIRED/TRAINING وبقيّةُ الحالاتِ غيرِ الاستعاديّةِ) —
#: أداةُ الإيقافِ نفسُها لا تُمنَعُ عندَ أيِّ مستوىً (التصميمُ § 2.2 قاعدةٌ 3).
ACTION_CONTAIN_AGENT = "contain_agent"

#: استعادةُ قدرةٍ أوقفها النظامُ (الانتقالُ إلى ACTIVE) — المحجوزُ منَ المستوى 4
#: (صنفُ execute_task · التصميمُ § 2.2 قاعدةٌ 2).
ACTION_ACTIVATE_AGENT = "activate_agent"

#: نطاقُ مفتاحِ الذرّيّةِ لانتقالِ دورةِ الحياةِ: القيمةُ (الوكيلِ، الحالةِ الهدفِ).
LIFECYCLE_SCOPE = "agents.lifecycle"


class AgentLifecycleState(StrEnum):
    """دورة حياة الوكيل — حقل واحد كانوني: `agents.status`.

    القيم تجمع ما كان موزَّعًا بين `agents.status` و`agent_population.state`
    قبل R4، حتى لا تبقى دورتا حياة لنفس الوكيل.
    """

    #: أُضيفَتْ في W-032 (Q-39 (ب)): وكيلٌ وصلَ بيانُه من الواجهةِ العامّةِ
    #: (`POST /v1/agents`) وصارَ يُحفَظُ في جدولِ `agents` بدلًا من قاموسٍ
    #: متطاير. وهي **خارجَ** `EMPLOYABLE_STATUSES` بقصدٍ: إدامةُ البيانِ ليست
    #: توزيعًا، ومنحُ نادِي الواجهةِ قدرةَ إدخالِ وكيلٍ إلى مُرشَّحي الموزِّعِ
    #: سلطةٌ لم يمنَحْها قرارٌ (السؤالُ مفتوحٌ · Q-41).
    DECLARED = "declared"
    REGISTERED = "registered"
    TRAINING = "training"
    TESTING = "testing"
    SPECIALIZED = "specialized"
    EMPLOYED = "employed"
    ACTIVE = "active"
    PROMOTED = "promoted"
    READY = "ready"
    PAUSED = "paused"
    RETIRED = "retired"


#: الحالات التي تُحتسب «خارج الخدمة» في الإسقاط السكّاني.
#: و`declared` فيها بحكمِ أنَّها لا تُوزَّعُ: وكيلٌ مُعلَنٌ ولمّا يُوظَّفْ ليس في
#: الخدمةِ، وعدُّه في الخدمةِ يُعطي رقمًا سكّانيًّا أكبرَ ممّا يملِكُه الموزِّعُ فعلًا.
OUT_OF_SERVICE_STATES = frozenset(
    {
        AgentLifecycleState.DECLARED.value,
        AgentLifecycleState.PAUSED.value,
        AgentLifecycleState.RETIRED.value,
    }
)


class DuplicateAgentIdentityError(RuntimeError):
    """محاولة إنشاء هوية بمعرّف موجود — الهوية لا تُنشأ مرّتين."""


class UnknownAgentIdentityError(RuntimeError):
    """لا هوية كانونية بهذا المعرّف — لا يُخترَع وكيل."""


class IdentityLedgerDivergenceError(RuntimeError):
    """سجلُّ الذرّيّةِ يقولُ «نجحت» وصفُّ الهويّةِ غائبٌ — تفرُّقٌ يُرفَعُ لا يُسكَتُ عنه.

    لا يُزعَمُ إنشاءٌ لم يقعْ، ولا يُعادُ الإنشاءُ خارجَ الحدِّ: الحالةُ تحتاجُ
    استعادةً (1H) لا تجاهلًا. وهو مُعلَنٌ حدٌّ لا يُبتلَعُ استثناءً عامًّا.
    """


@dataclass(frozen=True)
class AgentIdentity:
    """الهوية الكانونية كما هي في `agents` الآن."""

    agent_id: str
    name: str
    role: str
    lifecycle_state: str
    permissions: tuple[str, ...]
    allowed_tools: tuple[str, ...]
    token_budget: int
    tenant_id: str
    created_at: str | None = None

    @property
    def employable(self) -> bool:
        """هل الحالة تسمح بالتوزيع فعلًا؟ نفس مجموعة الموزِّع لا مجموعة موازية."""
        return self.lifecycle_state in EMPLOYABLE_STATUSES

    def as_dict(self) -> dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "role": self.role,
            "lifecycle_state": self.lifecycle_state,
            "permissions": list(self.permissions),
            "allowed_tools": list(self.allowed_tools),
            "token_budget": self.token_budget,
            "tenant_id": self.tenant_id,
            "created_at": self.created_at,
            "identity_source": CANONICAL_IDENTITY_TABLE,
        }


def new_agent_id() -> str:
    """معرّف مستقرّ لا يُشتقّ من الاسم — الاسم ليس هوية."""
    return f"agent-{uuid.uuid4().hex[:8]}"


def _to_identity(row: AgentModel) -> AgentIdentity:
    return AgentIdentity(
        agent_id=row.id,
        name=row.name,
        role=row.role,
        lifecycle_state=row.status or AgentLifecycleState.REGISTERED.value,
        permissions=tuple(row.permissions or []),
        allowed_tools=tuple(row.allowed_tools or []),
        token_budget=int(row.token_budget or 0),
        tenant_id=row.tenant_id or "default",
        created_at=row.created_at.isoformat() if row.created_at else None,
    )


def get_identity(agent_id: str, *, tenant_id: str | None = None) -> AgentIdentity | None:
    """قراءة الهوية الكانونية — `None` إن لم تكن مُسجَّلة."""
    session = get_session_factory()()
    try:
        query = session.query(AgentModel).filter(AgentModel.id == agent_id)
        if tenant_id is not None:
            query = query.filter(AgentModel.tenant_id == tenant_id)
        row = query.first()
        return _to_identity(row) if row else None
    finally:
        session.close()


def require_identity(agent_id: str, *, tenant_id: str | None = None) -> AgentIdentity:
    """قراءة الهوية أو سقوط صريح — لا وكيل مُختلَق."""
    identity = get_identity(agent_id, tenant_id=tenant_id)
    if identity is None:
        raise UnknownAgentIdentityError(f"لا هوية كانونية بهذا المعرّف: {agent_id}")
    return identity


def list_identities(
    *,
    lifecycle_state: str | None = None,
    tenant_id: str | None = None,
) -> list[AgentIdentity]:
    """كل الهويات الكانونية (بترتيب الإنشاء)."""
    session = get_session_factory()()
    try:
        query = session.query(AgentModel)
        if lifecycle_state:
            query = query.filter(AgentModel.status == lifecycle_state)
        if tenant_id is not None:
            query = query.filter(AgentModel.tenant_id == tenant_id)
        return [_to_identity(row) for row in query.order_by(AgentModel.created_at.asc()).all()]
    finally:
        session.close()


def _delete_identity_row(agent_id: str) -> bool:
    """حذفُ صفِّ هويةٍ موجودٍ فعلًا — عكسٌ حقيقيٌّ للإنشاءِ (معوّضُ 1I).

    يعيدُ `False` إن لم يكنِ الصفُّ موجودًا: لا يُزعَمُ عكسُ أثرٍ لا وجودَ له.
    وهذا نطاقُهُ محصورٌ في صفِّ هذهِ العمليّةِ (مفتاحُ الذرّيّةِ من `agent_id`)،
    والقيدُ الأوليُّ في الجدولِ يمنعُ أن يكونَ الصفُّ لغيرِها أصلًا.
    """
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


#: المُصرِّحُ الافتراضيُّ لإنشاءِ الهويّةِ — كائنٌ واحدٌ للوحدةِ يُبنى عندَ أوّلِ حاجةٍ
#: (W-532 · قرارُ المالكِ Q-62 ②: «يقارن الوكيل الكلفة … ويتبنى ما هو أسلم» — قِيسَ
#: أنَّ بناءَ المُصرِّحِ لكلِّ نداءٍ يبني حدًّا وسجلَّي ذرّيّةٍ وأذونٍ جديدةً فتنمو كلفةُ
#: النداءِ مع تراكمِ السجلِّ: 12.9 ← 19.6 ← 28.2 ms/op، والكائنُ الواحدُ ثابتٌ 9.5–11.4
#: · evidence/W-532). الفاعلُ مُسمّى صراحةً كما كان، والتمريرُ الصريحُ لـ`authorizer` باقٍ.
_DEFAULT_AUTHORIZER: ConstitutionalAuthorizer | None = None


def _default_authorizer() -> ConstitutionalAuthorizer:
    """المُصرِّحُ الافتراضيُّ بفاعلِ إنشاءِ الهويّةِ المُسمّى — واحدٌ للوحدةِ."""
    global _DEFAULT_AUTHORIZER
    if _DEFAULT_AUTHORIZER is None:
        _DEFAULT_AUTHORIZER = ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    return _DEFAULT_AUTHORIZER


def register_identity(
    agent_id: str,
    name: str,
    role: str,
    *,
    permissions: list[str] | None = None,
    allowed_tools: list[str] | None = None,
    lifecycle_state: str = AgentLifecycleState.REGISTERED.value,
    token_budget: int = 10_000,
    tenant_id: str = "default",
    authorizer: ConstitutionalAuthorizer | None = None,
) -> AgentIdentity:
    """إنشاء هوية كانونية جديدة — ترفض التكرار — عبر الحد السيادي منذ WI-082.

    الكتابةُ في `agents` لا تقعُ إلّا بإذنٍ دستوريٍّ بالفعلِ «spawn_agent» (قرارُ
    المالكِ Q-15 ①)، فيقفُ الإنشاءُ عندَ المستوى الثالثِ من زرِّ الإيقافِ (المادةُ
    الثامنة) ويعلنُ أثرَهُ ويحملُ معوّضًا حقيقيًّا ومفتاحَ ذرّيّةٍ من المعرِّفِ نفسِه.

    `authorizer` اختياريٌّ Named كما في `governance/factories.py` (السابقةِ P13):
    لا يغيّرُ سلوكَ مُنادٍ قائمٍ — من لا يمرّرُ مُصرِّحًا يُبنى له المبدئيُّ بفاعلٍ
    مسمّى، ولا يُبنى جسرٌ ثانٍ ولا بدائيّةٌ سياديّةٌ جديدة.

    Raises:
        DuplicateAgentIdentityError: المعرّف مُستخدَم فعلًا. التحديث يجري عبر
            `update_identity` صراحةً، لا عبر «تسجيل» صامت يمسح ما قبله.
        IdentityLedgerDivergenceError: سجلُّ الذرّيّةِ يُثبِتُ نجاحَ العمليّةِ
            وصفُّ الهويّةِ غائبٌ — استعادةٌ مطلوبةٌ لا إنشاءٌ يُزعَم.
    """
    actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
    # قاعدةُ نطاقٍ **قبلَ** الحدِّ (قراءةٌ لا كتابةٌ): رفضٌ مبكّرٌ صريحٌ للتكرارِ.
    # وهو ليس حمايةَ التزامنِ — ذاك قيدُ المفتاحِ الأوليُّ في الجدولِ — بل إبقاءُ
    # العقدِ القائمِ: المكرّرُ يُرفضُ قبلَ عبورِ الحدِّ لا بعده.
    session = get_session_factory()()
    try:
        existing = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        if existing is not None:
            raise DuplicateAgentIdentityError(f"هوية موجودة فعلًا بهذا المعرّف: {agent_id}")
    finally:
        session.close()

    target = f"agents/{agent_id}"
    effect = declared_effect("CREATE", target, f"هويةُ وكيلٍ «{name}» في السجلِّ الكانونيِّ الواحد")

    def _apply(_effect: Any) -> None:
        write_session = get_session_factory()()
        try:
            write_session.add(
                AgentModel(
                    id=agent_id,
                    name=name,
                    role=role,
                    status=lifecycle_state,
                    permissions=permissions or [],
                    allowed_tools=allowed_tools or [],
                    token_budget=token_budget,
                    tenant_id=tenant_id,
                )
            )
            write_session.commit()
        finally:
            write_session.close()

    guarded = actor_authorizer.guard_declared(
        ACTION_SPAWN_AGENT,
        target,
        declared_effects=(effect,),
        applier=_apply,
        operation_key=operation_key(IDENTITY_SPAWN_SCOPE, agent_id),
        compensators=(
            compensator(
                effect.signature,
                lambda: _delete_identity_row(agent_id),
                "حذفُ صفِّ الهويّةِ المُنشَأ — عكسٌ حقيقيٌّ للإنشاءِ",
            ),
        ),
    )
    if guarded.is_replay and get_identity(agent_id, tenant_id=tenant_id) is None:
        # العمليّةُ مُثبَتةٌ ناجحةٌ لهذا المفتاحِ: لا كتابةً ثانيةً ولا يُزعَمُ إنشاءٌ
        # جديدٌ. والصدقُ أن يُتحقَّقَ من أثرِها: الهويّةُ موجودةٌ فعلًا، أو الحالةُ
        # متفرّقةٌ فتُرفَعُ صريحةً ولا يُعادُ الإنشاءُ خارجَ الحدّ.
        raise IdentityLedgerDivergenceError(
            f"سجلُّ الذرّيّةِ يُثبِتُ إنشاءَ «{agent_id}» وصفُّ الهويّةِ غائبٌ — "
            "استعادةٌ مطلوبةٌ (1H) لا إنشاءٌ يُزعَم"
        )
    return require_identity(agent_id, tenant_id=tenant_id)


def update_identity(
    agent_id: str,
    *,
    name: str | None = None,
    role: str | None = None,
    permissions: list[str] | None = None,
    allowed_tools: list[str] | None = None,
    token_budget: int | None = None,
    authorizer: ConstitutionalAuthorizer | None = None,
) -> AgentIdentity:
    """تعديل صريح لهوية قائمة — لا يُنشئ هوية جديدة — عبر الحد السيادي (E1 · WI-119).

    كتابةُ `agents` (الحقولُ المصرَّحَةُ: name/role/permissions/allowed_tools/
    token_budget) لا تقعُ إلّا بإذنٍ دستوريٍّ بالفعلِ «update_agent_identity»
    (تصميمُ W-694 § 2.2 · اعتمادُ المالكِ 2026-10-26) فيقفُ عندَ المستوىِ الثالثِ
    من زرِّ الإيقافِ (صنفُ spawn_agent — منحُ صلاحيّاتٍ) ويُعلنُ أثرَهُ ويحملُ
    معوّضًا يُرجِعُ لقطةَ الحقولِ السابقةِ ومفتاحَ ذرّيّةٍ من بصمةِ الحقولِ المطلوبةِ.
    فبصمةُ الحقولِ في المفتاحِ تجعلُ إعادةَ الإرسالِ إعادةً واحدةً والتحديثَ
    المختلفَ عمليّةً لاحقةً مشروعةً (تصميمُ E1 § 3 الصنفُ 4).

    Raises:
        UnknownAgentIdentityError: لا هوية كانونية بهذا المعرّف.
    """
    actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
    # قاعدةُ نطاقٍ **قبلَ** الحدِّ (قراءةٌ لا كتابةٌ): رفضٌ مبكّرٌ لما لا وجودَ له.
    existing = get_identity(agent_id)
    if existing is None:
        raise UnknownAgentIdentityError(f"لا هوية كانونية بهذا المعرّف: {agent_id}")

    changes: dict[str, Any] = {}
    if name is not None:
        changes["name"] = name
    if role is not None:
        changes["role"] = role
    if permissions is not None:
        changes["permissions"] = list(permissions)
    if allowed_tools is not None:
        changes["allowed_tools"] = list(allowed_tools)
    if token_budget is not None:
        changes["token_budget"] = int(token_budget)
    if not changes:
        # لا حقولُ مطلوبةٌ: لا عبورَ ولا كتابةً — العمليّةُ فارغةٌ فلا تُقاس.
        return require_identity(agent_id)

    target = f"agent:{agent_id}"
    fingerprint = hashlib.sha256(
        json.dumps(changes, sort_keys=True, ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    # موردُ الأثرِ يحملُ بصمةَ التغييراتِ (موردٌ فرعيٌّ داخلَ نطاقِ الهدفِ —
    # `in_scope`): به تتميّزُ العقودُ بينَ تحديثينِ مختلفينِ للوكيلِ نفسِهِ
    # فلا يُرفَض تحديثٌ مشروعٌ كإعادةِ إذنٍ في الثانيةِ نفسِها.
    effect = declared_effect(
        "WRITE",
        f"{target}/fields.{fingerprint[:16]}",
        f"تحديثُ الحقولِ المصرَّحَةِ {sorted(changes)} للهويّةِ الكانونيّةِ",
    )

    def _apply(_effect: Any) -> None:
        _update_identity_core(agent_id, changes)

    # المعوّضُ الحقيقيّ: لقطةُ الحقولِ السابقةِ (تصميمُ E1 § 2.2 — إرجاعُ لقطةِ
    # الحقولِ السابقةِ) — يُبنى **قبلَ** التنفيذِ من الهويّةِ المقروءةِ فوقَ لا من
    # قراءةٍ لاحقةٍ تسبقُ الكتابةَ المتزامنةَ.
    previous = {
        "name": existing.name,
        "role": existing.role,
        "permissions": list(existing.permissions),
        "allowed_tools": list(existing.allowed_tools),
        "token_budget": existing.token_budget,
    }

    actor_authorizer.guard_declared(
        ACTION_UPDATE_AGENT_IDENTITY,
        target,
        declared_effects=(effect,),
        applier=_apply,
        # النطاقُ يحملُ بصمةَ الحمولةِ (مفتاحُ التصميمِ § 2.2: هويةُ التحديثِ +
        # المعرِّفُ + بصمةُ التغييراتِ) — فالبصمةُ السياديّةُ (الطلبُ) تتغيّرُ معَ
        # كلِّ تحديثٍ مختلفٍ ولا يُرفَض التحديثُ الثاني كإعادةِ إذنٍ في الثانيةِ نفسِها.
        operation_key=operation_key(f"{IDENTITY_UPDATE_SCOPE}.{fingerprint[:16]}", agent_id),
        compensators=(
            compensator(
                effect.signature,
                lambda: _update_identity_core(agent_id, previous),
                "إرجاعُ لقطةِ الحقولِ السابقةِ للهويّةِ — عكسٌ حقيقيٌّ للتحديثِ",
            ),
        ),
    )
    return require_identity(agent_id)


def _update_identity_core(agent_id: str, changes: dict[str, Any]) -> None:
    """نواةُ كتابةِ تحديثِ الهويّةِ — كاتبٌ صافٍ بلا عبورٍ (Q-9 § 2.3 · تصميمُ E1).

    تستعملُها العباراتُ العلنيّةُ المحروسةُ (كتحديثِ الهويّةِ هذا) وكلُّ سطحٍ
    أعلنَ أثرَ تحديثِ الهويّةِ في عبورِهِ الأعلى (فلا تعشيشَ) — ولا تُستعملُ
    مباشرةً من خارجِ الوحدةِ: المرجعُ العلنيُّ هو `update_identity` المحروس.
    """
    session = get_session_factory()()
    try:
        row = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        if row is None:
            raise UnknownAgentIdentityError(f"لا هوية كانونية بهذا المعرّف: {agent_id}")
        if "name" in changes:
            row.name = changes["name"]
        if "role" in changes:
            row.role = changes["role"]
        if "permissions" in changes:
            row.permissions = changes["permissions"]
        if "allowed_tools" in changes:
            row.allowed_tools = changes["allowed_tools"]
        if "token_budget" in changes:
            row.token_budget = changes["token_budget"]
        session.commit()
    finally:
        session.close()


def set_lifecycle_state(
    agent_id: str, lifecycle_state: str, authorizer: ConstitutionalAuthorizer | None = None
) -> bool:
    """تغيير دورة الحياة في الحقل الكانوني الوحيد — عبر الحد السيادي (E1 · WI-119).

    الفعلُ بالوجهةِ (تصميمُ W-694 § 2.2): الانتقالُ إلى حالةِ احتواءٍ
    (PAUSED/RETIRED/TRAINING) يعبرُ بالفعلِ «contain_agent» بلا منعٍ — أداةُ
    الاحتواءِ نفسُها لا تُمنَعُ عندَ الإيقافِ — والانتقالُ إلى ACTIVE يعبرُ
    بالفعلِ «activate_agent» المحجوزِ منَ المستوىِ الرابعِ (استعادةُ قدرةٍ
    أوقفها النظامُ · صنفُ execute_task) · وبقيّةُ الحالاتِ (تسجيلٌ وإدارةٌ لا
    احتواءَ ولا استعادةَ) تعبرُ بـcontain_agent أيضًا لأنَّ أعمالَ التسجيلِ تبقى
    ممكنةً في كلِّ المستوياتِ (التصميمُ § 2.2 قاعدةٌ 3).

    مفتاحُ الذرّيّةِ من (الوكيلِ، الحالةِ السابقةِ، الحالةِ الهدفِ) وموردُ الأثرِ
    يحملُ الاتجاهَ (تصميمُ E1 § 2.2): فالانتقالانِ المتعاقبانِ (ACTIVE→PAUSED→ACTIVE)
    عمليّتانِ (تصميمُ E1 § 3 الصنفُ 4) وإعادةُ الإرسالِ بعدَ النجاحِ عمليةٌ فارغةٌ
    تعودُ بلا أثرٍ. والمعوّضُ يُرجِعُ الحالةَ السابقةَ.

    Returns:
        False إن لم تكن هناك هوية كانونية بهذا المعرّف — بلا إنشاء ضمني.
    """
    actor_authorizer = authorizer if authorizer is not None else _default_authorizer()
    # قاعدةُ نطاقٍ **قبلَ** الحدِّ (قراءةٌ لا كتابةٌ): لا إنشاءً ضمنيًّا.
    existing = get_identity(agent_id)
    if existing is None:
        return False

    previous_state = existing.lifecycle_state
    if previous_state == lifecycle_state:
        # العمليّةُ الفارغةُ لا تُقاسُ (سابقةُ `update_identity` بلا حقولٍ): الحالةُ
        # الهدفُ هي الواقعةُ فعلًا — فلا عبورَ ولا كتابةً ولا مفتاحُ ذرّيّةٍ
        # لما لم يقعْ. وبه لا تبتلعُ «إعادةُ الإرسالِ» انتقالًا جديدًا (active→active)
        # بل تعودُ بلا أثرٍ — «عدمُ تكرارِ الأثرِ عندَ الإعادةِ» (تصميمُ E1 § 3 · 4).
        return True
    action = (
        ACTION_ACTIVATE_AGENT
        if lifecycle_state == AgentLifecycleState.ACTIVE.value
        else ACTION_CONTAIN_AGENT
    )
    target = f"agent:{agent_id}"
    # موردُ الأثرِ يحملُ الاتجاهَ (موردٌ فرعيٌّ داخلَ نطاقِ الهدفِ — `in_scope`):
    # به تتميّزُ العقودُ بينَ انتقالينِ مختلفينِ للوكيلِ نفسِهِ فلا يُرفَض انتقالٌ
    # مشروعٌ كإعادةِ إذنٍ في الثانيةِ نفسِها.
    effect = declared_effect(
        "WRITE",
        f"{target}/lifecycle.{previous_state}->{lifecycle_state}",
        f"انتقالُ دورةِ الحياةِ {previous_state} → {lifecycle_state} في الحقلِ الكانونيِّ الوحيدِ",
    )

    def _apply(_effect: Any) -> None:
        _set_lifecycle_state_core(agent_id, lifecycle_state)

    guarded = actor_authorizer.guard_declared(
        action,
        target,
        declared_effects=(effect,),
        applier=_apply,
        # النطاقُ يحملُ الاتجاهَ (مفتاحُ التصميمِ § 2.2: دورةُ الحياةِ + المعرِّفُ +
        # الحالةُ السابقةُ + الحالةُ الهدفُ) — فالبصمةُ السياديّةُ تفرّقُ بينَ
        # اتجاهاتٍ مختلفةٍ ولا يُرفَض عبورٌ مشروعٌ كإعادةِ إذنٍ في الثانيةِ نفسِها.
        operation_key=operation_key(
            f"{LIFECYCLE_SCOPE}.{previous_state}->{lifecycle_state}", agent_id
        ),
        compensators=(
            compensator(
                effect.signature,
                lambda: _set_lifecycle_state_core(agent_id, previous_state),
                "إرجاعُ حالةِ دورةِ الحياةِ السابقةِ — عكسٌ حقيقيٌّ للانتقالِ",
            ),
        ),
    )
    if guarded.is_replay:
        # العمليّةُ مُثبَتةٌ لهذا المفتاحِ: أثرُها إمّا واقعٌ فعلًا (الحالةُ الهدفُ) أو
        # متفرّقٌ فتُرفَعُ صريحةً ولا يُعادُ التنفيذُ خارجَ الحدّ (نمطُ register_identity).
        current = get_identity(agent_id)
        if current is None or current.lifecycle_state != lifecycle_state:
            raise IdentityLedgerDivergenceError(
                f"سجلُّ الذرّيّةِ يُثبِتُ انتقالَ «{agent_id}» إلى «{lifecycle_state}» "
                "والحقلُ الكانونيُّ مخالفٌ — استعادةٌ مطلوبةٌ (1H) لا تنفيذٌ يُزعَم"
            )
    return True


def _set_lifecycle_state_core(agent_id: str, lifecycle_state: str) -> bool:
    """نواةُ كتابةِ دورةِ الحياةِ — كاتبٌ صافٍ بلا عبورٍ (Q-9 § 2.3 · تصميمُ E1).

    تستعملُها الأسطحُ التي أعلنت أثرَ انتقالِ دورةِ الحياةِ في عبورِها الأعلى
    (health.isolate · health.start_treatment · health.release …) فلا تعشيشَ،
    ويستعملُها العبورُ العلنيُّ `set_lifecycle_state` نفسُه. ولا تُستعملُ مباشرةً
    من خارجِ الوحدةِ: المرجعُ العلنيُّ هو `set_lifecycle_state` المحروس.
    """
    session = get_session_factory()()
    try:
        row = session.query(AgentModel).filter(AgentModel.id == agent_id).first()
        if row is None:
            return False
        row.status = lifecycle_state
        session.commit()
        return True
    finally:
        session.close()


def _runtime_activity(limit: int = 500) -> dict[str, Any]:
    """آخر طور تشغيل لكل وكيل من أحداث دورة الحياة (R3) — لا تخمين.

    إن لم تُرصَد أحداث بعد فالحقول تُعلَن `observed=False` بدل تصفيرها كأنها
    قياس. `executing`/`failed` لا تُشتقّ من `agents.status` لأن الحالة هناك
    حالة تعيين لا حالة تنفيذ لحظي.
    """
    from amos_federation.common.event_bus import get_event_bus

    events = get_event_bus().get_events(subject=RUNTIME_ACTIVITY_SUBJECT, limit=limit)
    latest: dict[str, str] = {}
    for event in events:  # الأحداث تعود من الأحدث إلى الأقدم
        data = event.get("data") or {}
        agent_id = str(data.get("agent_id", ""))
        phase = str(data.get("phase", ""))
        if agent_id and agent_id not in latest:
            latest[agent_id] = phase
    phases: dict[str, int] = {}
    for phase in latest.values():
        phases[phase] = phases.get(phase, 0) + 1
    return {
        "observed": bool(events),
        "events_scanned": len(events),
        "agents_with_activity": len(latest),
        "by_phase": phases,
        "source": RUNTIME_ACTIVITY_SUBJECT,
    }


def population_projection(*, tenant_id: str | None = None) -> dict[str, Any]:
    """سكّان النظام كإسقاط للسجل الكانوني — لا سجل هوية ثانٍ.

    ما هو مقيس فعلًا: `total` وتوزيع دورة الحياة (منها active وretired وidle
    = مُعيَّن ولا نشاط تشغيل مرصود). ما ليس مقيسًا من الهوية: `executing` و
    `failed` — يُقرآن من أحداث دورة الحياة، ويُعلَن `observed=False` إن لم
    تُسجَّل أحداث بعد. لا يُختلق رقم غير متوفّر.
    """
    identities = list_identities(tenant_id=tenant_id)
    by_state: dict[str, int] = {}
    for identity in identities:
        by_state[identity.lifecycle_state] = by_state.get(identity.lifecycle_state, 0) + 1
    activity = _runtime_activity()
    executing = activity["by_phase"].get("executing", 0)
    failed = activity["by_phase"].get("failed", 0)
    employable = sum(1 for identity in identities if identity.employable)
    return {
        "total": len(identities),
        "by_lifecycle_state": by_state,
        "active": by_state.get(AgentLifecycleState.ACTIVE.value, 0),
        "retired": by_state.get(AgentLifecycleState.RETIRED.value, 0),
        "paused": by_state.get(AgentLifecycleState.PAUSED.value, 0),
        "employable": employable,
        "idle": max(employable - executing, 0),
        "executing": executing if activity["observed"] else None,
        "failed": failed if activity["observed"] else None,
        "runtime_activity": activity,
        "identity_source": CANONICAL_IDENTITY_TABLE,
        "projection_of": CANONICAL_IDENTITY_TABLE,
        "fidelity": POPULATION_FIDELITY,
    }


def identity_health(*, tenant_id: str | None = None) -> dict[str, Any]:
    """صحّة طبقة الهوية والسكّان — مبنيّة على مكوّنات حقيقية لا على «العملية تعمل».

    تُفحَص ثلاثة مكوّنات فعليًّا: قابلية قراءة السجل الكانوني، وناقل الأحداث،
    وتناسق الإسقاط (صفوف `agent_population` بلا هوية كانونية = دَين توفيق).
    أي مكوّن غير متوفّر يُعلَن `unavailable`، ولا تُعلَن الطبقة `healthy` إلا
    إذا نجحت الفحوص الحقيقية كلها.
    """
    components: dict[str, dict[str, Any]] = {}

    try:
        identities = list_identities(tenant_id=tenant_id)
        components["canonical_registry"] = {
            "status": "available",
            "agents": len(identities),
            "table": CANONICAL_IDENTITY_TABLE,
        }
    except Exception as exc:  # noqa: BLE001 — تُعلَن كغير متوفّرة لا تُخفى
        components["canonical_registry"] = {"status": "unavailable", "error": str(exc)}

    try:
        from amos_federation.common.event_bus import get_event_bus

        components["event_bus"] = {
            "status": "available",
            "lifecycle_events": len(
                get_event_bus().get_events(subject=RUNTIME_ACTIVITY_SUBJECT, limit=1)
            ),
        }
    except Exception as exc:  # noqa: BLE001
        components["event_bus"] = {"status": "unavailable", "error": str(exc)}

    try:
        # R4 (OPTION 2): «بلا هوية كانونية» ليس خللًا بحدّ ذاته. القاعدة الحقيقية
        # تحمل 5116 صفًّا سكّانيًّا بـ24 اسمًا متميزًا، أي بذر مكرّر لا هويّات. عدّها
        # دَين توفيق كان يُثبِّت `degraded` إلى الأبد فيفقد المقياس معناه. الخلل
        # الحقيقي: صفّ **ذو دليل تاريخي** لا يراه مسار التنفيذ. والعدد الكلّي
        # يُعلَن معه ولا يُخفَى.
        from amos_federation.services.agent_runtime.population import (
            legacy_seed_profiles,
            reconciliation_debt,
            unmigrated_profiles,
        )

        orphans = unmigrated_profiles()
        debt = reconciliation_debt()
        components["population_projection"] = {
            "status": "available" if not debt else "degraded",
            "unmigrated_profile_rows": len(orphans),
            "reconciliation_debt_rows": len(debt),
            "legacy_seed_rows": len(legacy_seed_profiles()),
            "table": PROJECTION_TABLE,
        }
    except Exception as exc:  # noqa: BLE001
        components["population_projection"] = {"status": "unavailable", "error": str(exc)}

    statuses = {component["status"] for component in components.values()}
    if "unavailable" in statuses:
        overall = "unavailable"
    elif "degraded" in statuses:
        overall = "degraded"
    else:
        overall = "healthy"
    return {
        "status": overall,
        "components": components,
        "basis": "component_checks",
        "fidelity": POPULATION_FIDELITY,
    }
