"""WI-082 — هجرة `register_identity` عبرَ الحدِّ السياديِّ بفعلِ «spawn_agent».

الهدف: إثباتُ أنَّ إنشاءَ الهويّةِ يعبرُ الحدَّ السياديَّ بالفعلِ «spawn_agent» (قرارُ
       المالكِ Q-15 ① · القيدُ W-385) فيقفُ عندَ المستوى الثالثِ من زرِّ الإيقافِ
       (المادةُ الثامنة · R-008-2)، وأنّ عقدَ المُنادي القائمَ لم يتغيّرْ: نفسُ
       الإرجاعِ للناجحِ ونفسُ الرفضِ للمكررِ، وأنّ الطفرةَ (تبديلُ الفعلِ إلى
       register_agent) تُسقِطُ الفحصَ لا تصمتُ عنه.
النطاق: قياسُ سلوكِ `register_identity` عبرَ الحدِّ وحدَه — لا تعديلَ للبوابةِ ولا
        للقواعدِ الدستوريّةِ. وحقنُ مستوى زرِّ الإيقافِ في الطلبِ محاكاةٌ لحالةِ الزرِّ
        معلَنةٌ هنا لا تجاوزٌ للبوّابةِ.
المالك: federal/executive/services — WI-082 (بقرارِ المالكِ Q-15 · وتوجيهِ المستشارِ 8)
تاريخ الإنشاء: 2026-10-17 (W-402 · WI-082)

قرارُ المالكِ Q-15 ① (2026-10-15 · القيدُ W-385): إنشاءُ الهويّةِ يُعلَنُ بالفعلِ
`spawn_agent` — فيقفُ عندَ المستوى الثالثِ من زرِّ الإيقافِ (المادةُ الثامنة،
R-008-2: `KILL_SWITCH_BLOCKS[3]`). والسابقةُ المعماريّةُ `governance/factories.py`
(P13): معاملٌ مسمّىً اختياريٌّ `authorizer` لا يغيّرُ سلوكَ مُنادٍ قائم.

الحدُّ المُعلَنُ في هذا الفحصِ:
- اختبارُ المستوى 3 يحقنُ `kill_switch_level=3` في الطلبِ عبرَ مصدّ مُصرِّحٍ
  محليٍّ (محاكاةُ حالةِ الزرِّ في الطلبِ لا تعديلٌ للفعلِ) — لأنَّ لا مسارَ
  إنتاجيًّا اليومَ يضخُّ المستوى في الطلبِ، وتلك مسجّلةٌ اكتشافًا مستقلًّا
  (DISC-099 · WI-085).
- لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذِ (§ 4.3) — هذا ملفُّ قياسٍ لا حُكمِ مراجعة.

الدليلُ المُعادُ تشغيلُه:
    .venv/bin/python -m pytest federal/executive/services/tests/test_wi082_agent_identity_sovereign.py -q
"""

from __future__ import annotations

import dataclasses
from typing import Any

import pytest
from core.sovereignty.gateway import SovereigntyViolation

from amos_federation.services.executive_core.agent_identity import (
    ACTION_SPAWN_AGENT,
    AGENT_IDENTITY_ACTOR,
    DuplicateAgentIdentityError,
    IdentityLedgerDivergenceError,
    _delete_identity_row,
    register_identity,
)
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from tests.conftest import purge_agents

#: الوكيلُ الذي يُبنى افتراضيًّا بلا مُصرِّحٍ مُمرَّر — القيمةُ المقيسةُ من الطلبِ
#: المُصنَّعِ للحدِّ لا تخمينًا.
EXPECTED_DEFAULT_ACTOR = "EXECUTIVE"


class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجل كل نتيجة محروسة — لأجل قياس الاعتمادية، لا لاتخاذ قرار."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.results.append(guarded)
        return guarded


class KillSwitchLevelAuthorizer(ConstitutionalAuthorizer):
    """المُصرِّحُ نفسُهُ وطلبُهُ يحملُ مستوى زرِّ الإيقافِ.

    محاكاةُ **حالةِ الزرِّ** في الطلبِ لا تعديلٌ للفعلِ ولا تجاوزٌ للبوّابةِ:
    الطلبُ يمرُّ في المسارِ السياديِّ كاملًا، والقاعدةُ R-008-2 هي التي تنطقُ.
    """

    def __init__(self, level: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._kill_switch_level = level

    def _request(
        self,
        action: str,
        target: str,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        request = super()._request(action, target, metadata)
        return dataclasses.replace(request, kill_switch_level=self._kill_switch_level)


@pytest.fixture(autouse=True)
def _fresh_agents() -> None:
    """قاعدة نظيفة — القياس على سجل حقيقي لا على بقايا (نمط test_r4)."""
    from amos_federation.common.database import get_session_factory, init_db
    from tests.conftest import purge_tasks

    init_db()
    session = get_session_factory()()
    try:
        purge_tasks(session)
        purge_agents(session)
        session.commit()
    finally:
        session.close()


# ── 1. النجاح عبرَ الحدِّ — نفسُ الإرجاعِ، والكتابةُ بإذنٍ ─────────────────────


def test_wi082_1_register_crosses_boundary_and_returns_same_contract() -> None:
    authorizer = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    identity = register_identity(
        "wi082-success",
        "وكيل WI-082",
        "worker",
        permissions=["task:execute"],
        allowed_tools=["python_execute"],
        authorizer=authorizer,
    )

    # نفسُ عقدِ الإرجاعِ القائمِ: هويةٌ كانونيّةٌ كاملةٌ لا بنيةٌ جديدة.
    assert identity.agent_id == "wi082-success"
    assert identity.name == "وكيل WI-082"
    assert identity.role == "worker"

    # والصكُّ المُلزِمُ مُسجَّلٌ: عبورٌ واحدٌ بدليلِهِ الحرفيِّ — الفعلُ والهدفُ
    # والقرارُ وبصمةُ السجلِّ، لا وعدٌ بأنَّ «الحدَّ عُبر».
    assert len(authorizer.results) == 1
    evidence = authorizer.results[0].evidence.as_dict()
    assert evidence["action"] == "spawn_agent"
    assert evidence["target"] == "agents/wi082-success"
    assert evidence["decision"] == "ALLOW"
    assert evidence["ledger_entry_hash"]
    assert evidence["request_fingerprint"]

    from amos_federation.services.executive_core.agent_identity import require_identity

    stored = require_identity("wi082-success")
    assert stored.agent_id == identity.agent_id


# ── 2. المكررُ يُرفضُ قبلَ الحدِّ — لا عبورَ ولا كتابةً ───────────────────────


def test_wi082_2_duplicate_rejected_before_boundary() -> None:
    authorizer = RecordingAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    register_identity("wi082-dup", "وكيل أول", "worker", authorizer=authorizer)

    with pytest.raises(DuplicateAgentIdentityError):
        register_identity("wi082-dup", "وكيل ثانٍ", "worker", authorizer=authorizer)

    # العقدُ القائمُ: المكررُ لا يعبُرُ الحدَّ أصلًا (رفضٌ مبكّرٌ صريحٌ).
    assert len(authorizer.results) == 1


# ── 3. المستوى 3 من زرِّ الإيقافِ يجمّدُ الإنشاءَ — وهذا مضمونُ الفحصِ ──────


def test_wi082_3_kill_switch_level_3_blocks_spawn_agent() -> None:
    authorizer = KillSwitchLevelAuthorizer(level=3, actor=AGENT_IDENTITY_ACTOR)
    with pytest.raises(SovereigntyViolation) as excinfo:
        register_identity(
            "wi082-halted",
            "وكيل مُجمَّد",
            "worker",
            authorizer=authorizer,
        )

    # القاعدةُ R-008-2 تنطقُ باسمِ الفعلِ نفسِهِ: «spawn_agent» مُجمَّدٌ من
    # المستوى الثالثِ. وهذا هو القيدُ الذي تُسقِطُهُ طفرةُ تغييرِ الاسمِ.
    message = str(excinfo.value)
    assert "spawn_agent" in message
    assert "المستوى 3" in message

    # والرفضُ منعٌ حقيقيٌّ لا شكليٌّ: لا صفَّ هويةٍ كُتِبَ.
    from amos_federation.services.executive_core.agent_identity import get_identity

    assert get_identity("wi082-halted") is None


def test_wi082_4_level_below_3_does_not_block() -> None:
    """المستويانِ 1 و2 لا يجمّدانِ spawn_agent — التجميدُ من الثالثِ حصرًا.

    هذا هو الوجهُ الآخرُ للطفرةِ: لو عُدِّلَ القيدُ في `rules.py` (مجموعةُ
    المستوى الثالثِ) فسيُسقِطُ هذا الفحصُ — فلا يُزعَمُ تجميدٌ لا تُقيسُهُ بوّابةٌ.
    """
    authorizer = KillSwitchLevelAuthorizer(level=2, actor=AGENT_IDENTITY_ACTOR)
    identity = register_identity(
        "wi082-level2",
        "وكيل تحت المستوى الثاني",
        "worker",
        authorizer=authorizer,
    )
    assert identity.agent_id == "wi082-level2"


# ── 4. المعوّضُ عكسٌ حقيقيٌّ لا زعمٌ ─────────────────────────────────────────


def test_wi082_5_compensator_reverses_real_row() -> None:
    register_identity(
        "wi082-compensate",
        "وكيل المعوّض",
        "worker",
        authorizer=ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR),
    )

    # عكسٌ لأثرٍ موجودٍ: حذفٌ حقيقيٌّ وإعادةُ True.
    assert _delete_identity_row("wi082-compensate") is True
    from amos_federation.services.executive_core.agent_identity import get_identity

    assert get_identity("wi082-compensate") is None

    # ولا يُزعَمُ عكسُ أثرٍ لا وجودَ لهُ: الصفُّ غائبٌ فالعودةُ False.
    assert _delete_identity_row("wi082-compensate") is False


# ── 5. الإعادةُ بعدَ حذفِ الصفِّ: تفرُّقٌ صريحٌ لا إنشاءٌ يُزعَم ──────────────


def test_wi082_6_replay_with_missing_row_raises_divergence() -> None:
    authorizer = ConstitutionalAuthorizer(actor=AGENT_IDENTITY_ACTOR)
    register_identity(
        "wi082-replay",
        "وكيل الإعادة",
        "worker",
        authorizer=authorizer,
    )

    # حذفُ الصفِّ خارجَ العمليّةِ (كما يفعلُ تفريغُ الاختباراتِ): سجلُّ الذرّيّةِ
    # يُثبِتُ النجاحَ والصفُّ غائبٌ — تفرُّقٌ لا يُسكَتُ عنهُ ولا يُعادُ الإنشاءُ
    # خارجَ الحدِّ ولا يُزعَمُ نجاحٌ لم يقعْ.
    _delete_identity_row("wi082-replay")

    with pytest.raises(IdentityLedgerDivergenceError):
        register_identity(
            "wi082-replay",
            "وكيل الإعادة",
            "worker",
            authorizer=authorizer,
        )


# ── 6. المسارُ الافتراضيُّ بلا مُصرِّحٍ مُمرَّرٍ: يعملُ كالمُنادي القائمِ ─────


def test_wi082_7_default_authorizer_path_unchanged() -> None:
    """بلا `authorizer` يُبنى المبدئيُّ بفاعلٍ مسمّى — لا جسرٌ ثانٍ ولا سلوكٌ جديد.

    (يستعملُ سجلَّ الذرّيّةِ المُتاحَ في بيئةِ الاختبارِ — انظر `conftest.py`.)
    """
    identity = register_identity(
        "wi082-default-path",
        "وكيل المسار الافتراضي",
        "worker",
    )
    assert identity.agent_id == "wi082-default-path"
    assert AGENT_IDENTITY_ACTOR == EXPECTED_DEFAULT_ACTOR
    assert ACTION_SPAWN_AGENT == "spawn_agent"
