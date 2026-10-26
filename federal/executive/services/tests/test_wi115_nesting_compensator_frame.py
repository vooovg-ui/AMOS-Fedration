"""
الهدف: قياسُ عبورِ معوِّضِ فتحِ القضيّةِ — هل يجري داخلَ إطارِ العبورِ النشطِ أم بعدَه؟
النطاق: federal/executive/services — WI-115 (الكاشفُ · قياسُ § 4 من تصميمِ W-665)
تاريخ الإنشاء: 2026-10-26 (`W-685`)

سندُ القياسِ: وثيقةُ `docs/audit/Q9_NESTING_DETECTOR_DESIGN.md` § 4 قالت إنَّ
«لم يُقَس أنَّ معوِّضَ open_case يجري داخلَ إطارِ الحدِّ لا بعدَه. فإن جرى بعدَه،
سقطَ الزوجُ ("gov.case.open", "task.cancel") من الاستثناءِ ويُعلَن ذلك». هذا
الفحصُ يقيسُه فعلًا: فتحُ قضيّةٍ يفشلُ إدخالُ صفِّها بعدَ نجاحِ مهمّتِها فيُعوَّضُ
تلقائيًّا (W-603) داخلَ الحدِّ، والمقيسُ إطارُ العبورِ لحظةَ عبورِ الإلغاءِ.

فإن غيَّرَ أحدٌ المسارَ فأصبحَ التعويضُ خارجَ الإطارِ، فشلَ هذا الفحصُ — فيُعلَن
الأمرُ ويُنظَرُ في سقوطِ الزوجِ منَ الاستثناءِ، لا أن يبقى صامتًا.
"""

from __future__ import annotations

import sys
import uuid
from pathlib import Path
from types import SimpleNamespace

import pytest

import amos_federation.services.state_treasury.models  # noqa: F401 — مفتاحٌ أجنبيٌّ يفرضُ الاستيرادَ
from amos_federation.common.database import TaskModel, get_session_factory, init_db
from amos_federation.common.principal import DEFAULT_TENANT, AuthorizationContext
from amos_federation.services.executive_core.agent_identity import register_identity
from amos_federation.services.executive_core.engine import reset_executive_core
from amos_federation.services.government_services.models import CaseModel, ServiceModel
from amos_federation.services.government_services.service import (
    ACTION_CASE_OPEN,
    CASE_TASK_TYPE,
    GovernmentServices,
    reset_government_services,
)
from amos_federation.services.state_registry.service import StateRegistry, reset_state_registry

from tests.conftest import purge_agents, purge_tasks
from tests.test_2b_government_services_sovereign import (  # noqa: F401 — تجهيزاتٌ قائمةٌ
    RecordingAuthorizer,
    _code,
    _context,
    _open,
)

# الاستيرادُ من `core` على نمطِ الجسرِ نفسِه (`_ensure_core_importable` —
# sovereignty_bridge.py:210): جذرُ المستودعِ في sys.path ثمَّ استيرادٌ معتادٌ،
# فالوحدةُ المحمَّلةُ هي نفسُها التي تحملُها الحدودُ العاملةُ (لا نسختان).
_REPO_ROOT = Path(__file__).resolve().parents[4]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
from core.sovereignty.compensation import CompensationRequired
from core.sovereignty.enforcement_boundary import _active_crossing


@pytest.fixture(autouse=True)
def _fresh_state() -> None:
    init_db()
    session = get_session_factory()()
    try:
        session.query(CaseModel).delete()
        session.query(ServiceModel).delete()
        purge_tasks(session)
        purge_agents(session)
        session.commit()
    finally:
        session.close()
    reset_executive_core()
    reset_state_registry()
    reset_government_services()


@pytest.fixture
def authorizer(tmp_path):
    return RecordingAuthorizer(idempotency_ledger_path=tmp_path / "W685-IDEM.json")


@pytest.fixture
def crown() -> AuthorizationContext:
    return _context("king")


@pytest.fixture
def gov(authorizer) -> GovernmentServices:
    return GovernmentServices(authorizer=authorizer)


@pytest.fixture
def published(gov: GovernmentServices, crown: AuthorizationContext) -> dict:
    registry = StateRegistry()
    institution = registry.register_institution(
        context=crown,
        code=_code("INST"),
        name="وزارة الخدمات",
        kind="ministry",
        branch="executive",
    )
    service = gov.publish_service(
        context=crown,
        institution_code=institution["code"],
        code=_code("SVC"),
        name="إصدار وثيقة",
    )
    return {"institution_code": institution["code"], "service": service}


@pytest.fixture
def applicant() -> str:
    agent_id = f"agent-w685-{uuid.uuid4().hex[:10]}"
    register_identity(agent_id, f"وكيل {agent_id}", "executor", tenant_id=DEFAULT_TENANT)
    return agent_id


def test_معوض_فتح_القضية_يعبر_داخل_الإطار_النشط(
    gov: GovernmentServices,
    crown: AuthorizationContext,
    published: dict,
    applicant: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """فتحُ قضيّةٍ يفشلُ صفُّها بعدَ نجاحِ مهمّتِها ⇒ تعويضٌ تلقائيٌّ والقياسُ: الإطارُ لحظةَ الإلغاءِ.

    والمقيسُ ثلاثةٌ لا واحدٌ: (أ) الإطارُ النشطُ لحظةَ عبورِ الإلغاءِ إطارُ فتحِ
    القضيّةِ؛ (ب) والإلغاءُ أصابَ المهمّةَ **الجديدةَ** التي أنشأها الفتحُ لا صفًّا
    احتياطيًّا؛ (جـ) وسببُ الفشلِ هو تصادمُ صفِّ القضيّةِ المقصودُ (سلسلةُ السببِ
    تصلُ إلى `DuplicateReferenceError`) بلا صفٍّ قضيّةٍ مكتوبٍ بعدَ الفشلِ.
    """
    fixed = uuid.UUID("68500685-0685-4685-8685-685068506850")

    # (1) مهمّةٌ احتياطيّةٌ حقيقيّةٌ يُشيرُ إليها المفتاحُ الأجنبيُّ للصفِّ الاحتياطيِّ
    reserve_task = gov._core.submit(  # type: ignore[union-attr]
        CASE_TASK_TYPE,
        "مهمة المسبار الاحتياطية",
        priority="normal",
        tenant_id=DEFAULT_TENANT,
    )

    # (2) صفٌّ احتياطيٌّ يشغلُ معرِّفَ القضيّةِ الآتي (تصادمُ مفتاحٍ أساسيٍّ) بمرجعٍ
    # مختلفٍ فلا يصدُّهُ حارسُ تكرارِ المرجعِ القائمُ قبلَ الحدِّ
    session = get_session_factory()()
    service_row = (
        session.query(ServiceModel)
        .filter(ServiceModel.code == published["service"]["code"])
        .first()
    )
    assert service_row is not None
    try:
        session.add(
            CaseModel(
                id=f"case-{fixed}",
                reference="CASE-W685-RESERVED",
                service_id=service_row.id,
                institution_id=service_row.institution_id,
                applicant_agent_id=applicant,
                task_id=reserve_task["id"],
                subject="صفٌّ احتياطيٌّ للقياس",
                payload={},
                status="submitted",
                priority="normal",
                tenant_id=DEFAULT_TENANT,
                opened_by=crown.principal_id,
            )
        )
        session.commit()
    finally:
        session.close()

    # (3) تثبيتُ uuid4 في وحدةِ الخدماتِ الحكوميّةِ وحدَها (لا عالميًّا فلا يصطدمُ
    # مولِّدُ سجلّاتِ التدقيقِ ولا مولِّدُ معرِّفاتِ المهامِّ في النواةِ) — فتصطدمُ
    # القضيّةُ الجديدةُ بالمفتاحِ الأساسيِّ المحجوزِ
    import amos_federation.services.government_services.service as gov_service_module

    monkeypatch.setattr(
        gov_service_module,
        "uuid",
        SimpleNamespace(uuid4=lambda: fixed),
    )

    # (4) تسجيلُ الإطارِ ومعرِّفِ المهمّةِ المُلغاةِ لحظةَ عبورِ الإلغاءِ
    frames: list[tuple[str, str] | None] = []
    cancelled_task_ids: list[str] = []
    original_cancel = gov._core.cancel  # type: ignore[union-attr]

    def _recording_cancel(*args: object, **kwargs: object):
        frames.append(_active_crossing.get())
        if args:
            cancelled_task_ids.append(str(args[0]))
        return original_cancel(*args, **kwargs)

    monkeypatch.setattr(gov._core, "cancel", _recording_cancel)  # type: ignore[union-attr]

    # (5) الفتحُ يفشلُ بعدَ التطبيقِ ⇒ تعويضٌ تلقائيٌّ (W-603) داخلَ الحدِّ
    with pytest.raises(CompensationRequired) as excinfo:
        _open(
            gov,
            crown,
            published["institution_code"],
            published["service"]["code"],
            applicant,
            reference="CASE-W685-NEW",
        )

    # (أ) القياسُ نفسُه: الإلغاءُ عبَرَ والإطارُ النشطُ إطارُ فتحِ القضيّةِ
    assert frames, "لم يُستدعَ الإلغاءُ أصلًا — القياسُ لم يجرِ."
    assert frames[-1] is not None, (
        "الإلغاءُ عبَرَ خارجَ الإطارِ النشطِ — يُعلَن سقوطُ الزوجِ من الاستثناءِ."
    )
    assert frames[-1][0] == ACTION_CASE_OPEN, frames[-1]

    # (ب) الإلغاءُ أصابَ المهمّةَ الجديدةَ التي أنشأها الفتحُ (لا الاحتياطيّةَ)
    assert cancelled_task_ids, "الإلغاءُ مرَّ دونَ معرِّفِ مهمّةٍ — القياسُ ناقصٌ."
    cancelled_id = cancelled_task_ids[-1]
    assert cancelled_id != reserve_task["id"], "الإلغاءُ أصابَ المهمّةَ الاحتياطيّةَ — الفحصُ يقيسُ غيرَ المقصودِ."
    session = get_session_factory()()
    try:
        rows = session.query(CaseModel).count()
        task_row = session.get(TaskModel, cancelled_id)
    finally:
        session.close()
    assert task_row is not None, f"المهمّةُ المُلغاةُ {cancelled_id} ليست صفًّا حقيقيًّا في `tasks`."
    assert task_row.status == "cancelled", (
        f"المهمّةُ الجديدةُ لم تُلغَ بعدَ التعويضِ: {task_row.status}"
    )
    assert rows == 1, f"صفوفُ القضايا {rows} — القضيّةُ الجديدةُ كُتِبَت رغمَ فشلِها."

    # (جـ) سببُ الفشلِ المقصودُ: تصادمُ صفِّ القضيّةِ (لا خللُ تدقيقٍ ولا غيرُه)
    cause = excinfo.value.__cause__
    assert cause is not None, "التعويضُ بلا سببٍ موصولٍ — سلسلةُ السببِ مكسورةٌ."
    chain: list[str] = []
    node: object | None = cause
    while node is not None:
        chain.append(type(node).__name__)
        node = getattr(node, "__cause__", None)
    assert "DuplicateReferenceError" in chain, (
        f"سببُ الفشلِ ليسَ تصادمَ صفِّ القضيّةِ: {chain}"
    )
