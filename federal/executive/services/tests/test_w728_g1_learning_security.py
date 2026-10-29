"""
اختباراتُ عبورِ أسطحِ learning_cycle وsecurity الحدَّ السياديَّ (G1 § 9.10 · W-728)

الهدف: إثباتٌ مقيسٌ لا ادّعاء: أنَّ كلَّ سطحٍ من التسعةِ يعبرُ بالفعلِ المسمّى،
وأنَّ الرفضَ يقعُ قبلَ أيِّ كتابة، وأنَّ الإعادةَ لا تُكرِّرُ الأثر، وأنَّ المعوِّضَ
عكسٌ حقيقيّ، وأنَّ مساراتِ القراءةِ والرفضِ لا تعبرُ إطلاقًا.

الأصنافُ (نمطُ W-723/W-724):
1 الرفضُ قبلَ الكتابة (مستوى القاطعِ محقونٌ في الطلب) · 2 النجاحُ عبرَ الحدِّ
بالفعلِ المسمّى · 3 طفرةٌ لكلِّ سطح · 4 الإعادةُ لا تُكرِّر · 5 المعوِّضُ على
المسارِ الحقيقيّ.
"""

from __future__ import annotations

import ast
import dataclasses
import inspect
import json
import textwrap
import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

import pytest

from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from amos_federation.services.governance import learning_cycle as lc
from amos_federation.services.governance import security as sec
from amos_federation.services.governance.learning_cycle import (
    LearningCycle,
    ModelPromotionCycle,
)
from amos_federation.services.governance.security import (
    RateLimiter,
    RBACSystem,
    TLSCertManager,
)


# ── مُصرِّحاتُ القياس (نمطُ WI-082 · W-724) ──────────────────────────────────
class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجِّلُ كلَّ نتيجةٍ محروسةٍ وكلَّ طلبِ إذن — للقياسِ لا للقرار."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.results: list[Any] = []
        self.permits: list[str] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.results.append(guarded)
        return guarded

    def request_permit(self, action: str, *args: Any, **kwargs: Any) -> Any:
        permit = super().request_permit(action, *args, **kwargs)
        self.permits.append(action)
        return permit


class KillSwitchAuthorizer(RecordingAuthorizer):
    """الطلبُ يحملُ مستوى القاطع — محاكاةُ حالتِه لا تجاوزٌ (نمطُ WI-082 · E1)."""

    def __init__(self, level: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._level = level

    def _request(
        self,
        action: str,
        target: str,
        metadata: dict[str, Any] | None = None,
        human_approval: Any = None,
    ) -> Any:
        request = super()._request(action, target, metadata, human_approval)
        return dataclasses.replace(request, kill_switch_level=self._level)


def _violation() -> type[Exception]:
    from core.sovereignty.gateway import SovereigntyViolation

    return SovereigntyViolation


def _evidence(r: RecordingAuthorizer) -> dict[str, Any]:
    assert r.results, "لم يُعبَرِ الحدُّ السياديُّ أصلًا"
    return dict(r.results[-1].evidence.as_dict())


def _count(owner: Any, model: Any, **filters: Any) -> int:
    session = owner._Session()
    try:
        q = session.query(model)
        for key, value in filters.items():
            q = q.filter(getattr(model, key) == value)
        return int(q.count())
    finally:
        session.close()


@pytest.fixture
def rec() -> RecordingAuthorizer:
    return RecordingAuthorizer()


# ── تجهيزات ─────────────────────────────────────────────────────────────────
def _seed_run(owner: LearningCycle, status: str = "running") -> str:
    run_id = f"w728-run-{uuid.uuid4().hex[:6]}"
    session = owner._Session()
    try:
        session.add(
            lc.TrainingRunModel(
                run_id=run_id,
                dataset_id="w728-ds",
                model_name="amos-alpha",
                status=status,
                initial_loss="2.5000",
            )
        )
        session.commit()
    finally:
        session.close()
    return run_id


def _seed_version(owner: ModelPromotionCycle, track: str, status: str) -> str:
    version_id = f"w728-{track}-{uuid.uuid4().hex[:6]}"
    session = owner._Session()
    try:
        session.add(
            lc.ModelVersionModel(
                version_id=version_id,
                track=track,
                model_name=f"amos-{track}",
                status=status,
            )
        )
        session.commit()
    finally:
        session.close()
    return version_id


def _seed_rate(owner: RateLimiter, identifier: str, endpoint: str, count: int) -> None:
    session = owner._Session()
    try:
        session.add(
            sec.RateLimitModel(
                identifier=identifier,
                endpoint=endpoint,
                request_count=count,
                window_start=datetime.now(UTC),
            )
        )
        session.commit()
    finally:
        session.close()


def _seed_cert(owner: TLSCertManager, valid_until: datetime) -> str:
    cert_id = f"w728-cert-{uuid.uuid4().hex[:6]}"
    session = owner._Session()
    try:
        session.add(
            sec.TLSCertificateModel(
                cert_id=cert_id,
                common_name="w728.example",
                cert_hash=f"hash-{cert_id}",
                valid_until=valid_until,
            )
        )
        session.commit()
    finally:
        session.close()
    return cert_id


def _version(owner: ModelPromotionCycle, version_id: str) -> lc.ModelVersionModel:
    session = owner._Session()
    try:
        return session.query(lc.ModelVersionModel).filter_by(version_id=version_id).one()
    finally:
        session.close()


def _set_version(owner: ModelPromotionCycle, version_id: str, **fields: Any) -> None:
    session = owner._Session()
    try:
        row = session.query(lc.ModelVersionModel).filter_by(version_id=version_id).one()
        for key, value in fields.items():
            setattr(row, key, value)
        session.commit()
    finally:
        session.close()


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 1 — الرفضُ قبلَ الكتابة (مستوى القاطعِ محقونٌ في الطلب)
# ═════════════════════════════════════════════════════════════════════════════
def test_c1_collect_blocked_at_level1_no_row() -> None:
    dataset_id = f"w728-ds-{uuid.uuid4().hex[:6]}"
    cycle = LearningCycle(authorizer=KillSwitchAuthorizer(1))
    with pytest.raises(_violation()):
        cycle.collect_experiences(
            [{"type": "gap", "outcome": {"success": True}}], operation_id=dataset_id
        )
    assert _count(cycle, lc.ExperienceDatasetModel, dataset_id=dataset_id) == 0


def test_c1_complete_not_blocked_at_level5_q78_measured() -> None:
    """Q-78: `release_agent` ليسَ في KILL_SWITCH_BLOCKS عندَ أيِّ مستوى — المقيسُ
    يُثبَّتُ ويُرفَعُ للمالكِ."""
    cycle = LearningCycle(authorizer=KillSwitchAuthorizer(5))
    run_id = _seed_run(cycle)
    out = cycle.complete_training(run_id, 1.0, operation_id="w728-c1")
    assert "error" not in out and out["status"] == "completed"
    assert _evidence(cycle.authorizer)["action"] == "release_agent"  # type: ignore[union-attr]


@pytest.mark.parametrize(("level", "blocked"), [(3, False), (4, True), (5, True)])
def test_c1_shadow_blocked_from_level4_q80b(level: int, blocked: bool) -> None:
    cycle = ModelPromotionCycle(authorizer=KillSwitchAuthorizer(level))
    alpha = _seed_version(cycle, "alpha", "active")
    beta = _seed_version(cycle, "beta", "inactive")
    if blocked:
        with pytest.raises(_violation()):
            cycle.start_shadow(alpha, beta, operation_id=f"w728-sh-{level}")
    else:
        cycle.start_shadow(alpha, beta, operation_id=f"w728-sh-{level}")
    assert _version(cycle, beta).status == ("inactive" if blocked else "shadow")


@pytest.mark.parametrize(("level", "blocked"), [(3, False), (4, True), (5, True)])
def test_c1_canary_blocked_from_level4_q80b(level: int, blocked: bool) -> None:
    cycle = ModelPromotionCycle(authorizer=KillSwitchAuthorizer(level))
    beta = _seed_version(cycle, "beta", "inactive")
    if blocked:
        with pytest.raises(_violation()):
            cycle.start_canary(beta, operation_id=f"w728-ca-{level}")
    else:
        cycle.start_canary(beta, operation_id=f"w728-ca-{level}")
    assert _version(cycle, beta).status == ("inactive" if blocked else "canary")


@pytest.mark.parametrize(("level", "blocked"), [(3, False), (4, True), (5, True)])
def test_c1_promote_blocked_from_level4_q80c(level: int, blocked: bool) -> None:
    cycle = ModelPromotionCycle(authorizer=KillSwitchAuthorizer(level))
    beta = _seed_version(cycle, "beta", "inactive")
    if blocked:
        with pytest.raises(_violation()):
            cycle.promote_beta_to_alpha(beta, operation_id=f"w728-pr-{level}")
    else:
        cycle.promote_beta_to_alpha(beta, operation_id=f"w728-pr-{level}")
    assert _version(cycle, beta).track == ("beta" if blocked else "alpha")


@pytest.mark.parametrize(("level", "blocked"), [(3, False), (4, True), (5, True)])
def test_c1_create_session_blocked_from_level4(level: int, blocked: bool) -> None:
    rbac = RBACSystem(authorizer=KillSwitchAuthorizer(level))
    username = f"w728-u-{uuid.uuid4().hex[:6]}"
    if blocked:
        with pytest.raises(_violation()):
            rbac.create_session(username, "citizen", operation_id=f"w728-se-{level}")
    else:
        out = rbac.create_session(username, "citizen", operation_id=f"w728-se-{level}")
        assert out["session_token"]
    session = rbac._Session()
    try:
        rows = session.query(sec.UserSessionModel).filter_by(username=username).count()
    finally:
        session.close()
    assert rows == (0 if blocked else 1)


@pytest.mark.parametrize(("level", "blocked"), [(2, False), (3, True), (5, True)])
def test_c1_issue_certificate_blocked_from_level3(level: int, blocked: bool) -> None:
    tls = TLSCertManager(authorizer=KillSwitchAuthorizer(level))
    cert_id = f"w728-cert-{uuid.uuid4().hex[:6]}"
    if blocked:
        with pytest.raises(_violation()):
            tls.issue_certificate("w728.example", operation_id=cert_id)
    else:
        tls.issue_certificate("w728.example", operation_id=cert_id)
    assert _count(tls, sec.TLSCertificateModel, cert_id=cert_id) == (0 if blocked else 1)


def test_c1_check_rate_and_expiry_never_blocked() -> None:
    """`log_isolated_action` ليسَ في KILL_SWITCH_BLOCKS — رصدٌ لا منعٌ حتى عندَ 5."""
    limiter = RateLimiter(authorizer=KillSwitchAuthorizer(5))
    assert limiter.check_rate("w728-ip-c1", "/api/x", operation_id="w728-rt-c1")["allowed"]
    assert _evidence(limiter.authorizer)["action"] == "log_isolated_action"  # type: ignore[union-attr]

    tls = TLSCertManager(authorizer=KillSwitchAuthorizer(5))
    cert_id = _seed_cert(tls, datetime.now(UTC) - timedelta(days=1))
    assert tls.verify_certificate(cert_id) == {"valid": False, "reason": "expired"}
    assert _evidence(tls.authorizer)["action"] == "log_isolated_action"  # type: ignore[union-attr]


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 2 — النجاحُ عبرَ الحدِّ بالفعلِ المسمّى
# ═════════════════════════════════════════════════════════════════════════════
SURFACES = [
    (LearningCycle, "collect_experiences", "record_curriculum_step", "ACTION_COLLECT_EXPERIENCES"),
    (LearningCycle, "complete_training", "release_agent", "ACTION_COMPLETE_TRAINING"),
    (ModelPromotionCycle, "start_shadow", "invoke_model", "ACTION_START_SHADOW"),
    (ModelPromotionCycle, "start_canary", "invoke_model", "ACTION_START_CANARY"),
    (ModelPromotionCycle, "promote_beta_to_alpha", "activate_agent", "ACTION_PROMOTE_BETA"),
    (RBACSystem, "create_session", "execute_task", "ACTION_CREATE_SESSION"),
    (RateLimiter, "check_rate", "log_isolated_action", "ACTION_CHECK_RATE"),
    (TLSCertManager, "issue_certificate", "issue_certificate", "ACTION_ISSUE_CERTIFICATE"),
    (TLSCertManager, "verify_certificate", "log_isolated_action", "ACTION_VERIFY_CERTIFICATE"),
]


def _call_surface(name: str, rec: RecordingAuthorizer) -> None:
    if name == "collect_experiences":
        LearningCycle(authorizer=rec).collect_experiences(
            [{"type": "gap", "outcome": {"success": True}}],
            operation_id=f"w728-ds-{uuid.uuid4().hex[:6]}",
        )
    elif name == "complete_training":
        cycle = LearningCycle(authorizer=rec)
        cycle.complete_training(_seed_run(cycle), 1.0)
    elif name == "start_shadow":
        cycle = ModelPromotionCycle(authorizer=rec)
        cycle.start_shadow(
            _seed_version(cycle, "alpha", "active"), _seed_version(cycle, "beta", "inactive")
        )
    elif name == "start_canary":
        cycle = ModelPromotionCycle(authorizer=rec)
        cycle.start_canary(_seed_version(cycle, "beta", "inactive"))
    elif name == "promote_beta_to_alpha":
        cycle = ModelPromotionCycle(authorizer=rec)
        cycle.promote_beta_to_alpha(_seed_version(cycle, "beta", "inactive"))
    elif name == "create_session":
        RBACSystem(authorizer=rec).create_session(f"w728-u-{uuid.uuid4().hex[:6]}", "citizen")
    elif name == "check_rate":
        RateLimiter(authorizer=rec).check_rate(
            f"w728-ip-{uuid.uuid4().hex[:6]}", "/api/x", operation_id=f"op-{uuid.uuid4().hex[:6]}"
        )
    elif name == "issue_certificate":
        TLSCertManager(authorizer=rec).issue_certificate(
            "w728.example", operation_id=f"w728-cert-{uuid.uuid4().hex[:6]}"
        )
    elif name == "verify_certificate":
        tls = TLSCertManager(authorizer=rec)
        tls.verify_certificate(_seed_cert(tls, datetime.now(UTC) - timedelta(days=1)))
    else:  # pragma: no cover
        raise AssertionError(name)


@pytest.mark.parametrize(("owner", "surface", "action", "const"), SURFACES)
def test_c2_surface_crosses_with_named_action(
    owner: type, surface: str, action: str, const: str, rec: RecordingAuthorizer
) -> None:
    _call_surface(surface, rec)
    evidence = _evidence(rec)
    assert evidence["action"] == action
    assert evidence["decision"] == "ALLOW"


def test_c2_promote_declares_and_applies_two_effects(rec: RecordingAuthorizer) -> None:
    """الترقيةُ تكتبُ صفَّين: أثرانِ معلنانِ يُطبَّقانِ فعلًا (§ 9.10.5)."""
    cycle = ModelPromotionCycle(authorizer=rec)
    beta = _seed_version(cycle, "beta", "inactive")
    cycle.promote_beta_to_alpha(beta, operation_id="w728-2fx")
    assert len(rec.results[-1].outcome.applied_effects) == 2
    assert _version(cycle, beta).track == "alpha"
    retired = [
        v for v in _all_versions(cycle) if v["track"] == "alpha" and v["status"] == "retired"
    ]
    assert retired  # الألفا النشطُ أُحيلَ للتقاعدِ فعلًا


def _all_versions(owner: ModelPromotionCycle) -> list[dict[str, Any]]:
    return owner.list_versions()


def test_c2_read_and_reject_paths_return_without_crossing(rec: RecordingAuthorizer) -> None:
    """مساراتُ الرفضِ القارئُ تعودُ كما اليوم **بلا عبورٍ ولا كتابة** (§ 9.10.5)."""
    cycle = LearningCycle(authorizer=rec)
    assert cycle.complete_training("w728-missing-run", 1.0) == {"error": "run_not_found"}

    promotion = ModelPromotionCycle(authorizer=rec)
    assert promotion.start_shadow("w728-missing", "w728-missing") == {"error": "model_not_found"}
    assert promotion.start_canary("w728-missing") == {"error": "model_not_found"}
    assert promotion.promote_beta_to_alpha("w728-missing") == {"error": "model_not_found"}

    rbac = RBACSystem(authorizer=rec)
    assert rbac.create_session("w728-u-x", "no-such-role") == {"error": "role_not_found"}

    limiter = RateLimiter(authorizer=rec)
    identifier = f"w728-ip-max-{uuid.uuid4().hex[:6]}"
    _seed_rate(limiter, identifier, "/api/x", 100)
    assert limiter.check_rate(identifier, "/api/x", max_requests=100) == {
        "allowed": False,
        "count": 100,
        "max": 100,
    }

    tls = TLSCertManager(authorizer=rec)
    assert tls.verify_certificate("w728-missing-cert") == {"valid": False, "reason": "not_found"}
    assert (
        tls.verify_certificate(_seed_cert(tls, datetime.now(UTC) + timedelta(days=30)))["valid"]
        is True
    )

    assert rec.results == []  # لا عبورَ واحدًا في مساراتِ الرفضِ والقراءةِ كلِّها


def test_c2_create_session_token_never_enters_boundary_metadata(
    rec: RecordingAuthorizer,
) -> None:
    """الرمزُ لا يدخلُ الهدفَ ولا المفتاحَ ولا الأثرَ — بصمةُ 16 حرفًا وحدَها (§ 9.10.5)."""
    rbac = RBACSystem(authorizer=rec)
    out = rbac.create_session("w728-u-secret", "citizen", operation_id="w728-se-sec")
    token = out["session_token"]
    outcome = rec.results[-1].outcome
    key = outcome.operation_key
    assert token not in key and token[:32] not in key
    for effect in outcome.applied_effects:
        assert token not in effect.signature and token not in effect.resource


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 3 — طفرةٌ لكلِّ سطح (والحملةُ السلوكيّةُ في evidence/W-728/mutation_results.json)
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.parametrize(("owner", "surface", "action", "const"), SURFACES)
def test_c3_mutation_guard_call_literally_in_public_body(
    owner: type, surface: str, action: str, const: str
) -> None:
    """نداءُ `guard_declared` بثابتِ الفعلِ في جسدِ السطحِ نفسِه — واحدٌ لا أكثر."""
    tree = ast.parse(textwrap.dedent(inspect.getsource(getattr(owner, surface))))
    calls = [
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr == "guard_declared"
    ]
    assert len(calls) == 1, f"{surface}: نداءُ العبورِ ليس واحدًا في الجسد"
    first = calls[0].args[0]
    assert isinstance(first, ast.Name) and first.id == const
    module = lc if owner.__module__.endswith("learning_cycle") else sec
    assert getattr(module, const) == action


def test_c3_held_surfaces_untouched_q80a() -> None:
    """`start_training` و`evaluate_model` و`store_secret` دَينٌ معلَّقٌ بـQ-80أ
    و§ 9.1 — لم تُمَسَّ ولم تُنزَل إلى فعلٍ أخفّ."""
    held = [
        (lc.LearningCycle, "start_training"),
        (lc.EvaluationSystem, "evaluate_model"),
        (sec.SecretVault, "store_secret"),
    ]
    for owner, name in held:
        src = inspect.getsource(getattr(owner, name))
        assert "guard_declared" not in src and "request_permit" not in src, name


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 4 — الإعادةُ لا تُكرِّرُ الأثر
# ═════════════════════════════════════════════════════════════════════════════
def test_c4_collect_replay_one_row(rec: RecordingAuthorizer) -> None:
    cycle = LearningCycle(authorizer=rec)
    dataset_id = f"w728-ds-r-{uuid.uuid4().hex[:6]}"
    experiences = [{"type": "gap", "outcome": {"success": True}}]
    cycle.collect_experiences(experiences, operation_id=dataset_id)
    out = cycle.collect_experiences(experiences, operation_id=dataset_id)
    assert out.get("replayed") is True and rec.results[-1].is_replay
    assert _count(cycle, lc.ExperienceDatasetModel, dataset_id=dataset_id) == 1


def test_c4_complete_replay_one_row(rec: RecordingAuthorizer) -> None:
    cycle = LearningCycle(authorizer=rec)
    run_id = _seed_run(cycle)
    cycle.complete_training(run_id, 1.0, operation_id="w728-ct-r")
    _reset_run(cycle, run_id, status="running")  # الحالةُ السابقةُ تعودُ فيتطابقُ المفتاح
    out = cycle.complete_training(run_id, 1.0, operation_id="w728-ct-r")
    assert out.get("replayed") is True and rec.results[-1].is_replay
    assert out["status"] == "completed"  # لا كتابةَ ثانيةً بعدَ الاستعادة


def _reset_run(owner: LearningCycle, run_id: str, status: str) -> None:
    session = owner._Session()
    try:
        row = session.query(lc.TrainingRunModel).filter_by(run_id=run_id).one()
        row.status = status
        session.commit()
    finally:
        session.close()


def test_c4_shadow_replay_no_second_pair(rec: RecordingAuthorizer) -> None:
    cycle = ModelPromotionCycle(authorizer=rec)
    alpha = _seed_version(cycle, "alpha", "active")
    beta = _seed_version(cycle, "beta", "inactive")
    cycle.start_shadow(alpha, beta, operation_id="w728-sh-r")
    before = json.loads(_version(cycle, beta).shadow_pairs or "[]")
    _set_version(cycle, beta, status="inactive", shadow_pairs=json.dumps(before[:-1]))
    out = cycle.start_shadow(alpha, beta, operation_id="w728-sh-r")
    assert out.get("replayed") is True and rec.results[-1].is_replay
    # الإعادةُ لا تكتبُ زوجًا ثانيًا: يبقى الحقلُ على حالِهِ بعدَ الاستعادةِ ([] لا [زوج، زوج])
    assert json.loads(_version(cycle, beta).shadow_pairs or "[]") == before[:-1]


def test_c4_canary_replay_no_second_write(rec: RecordingAuthorizer) -> None:
    cycle = ModelPromotionCycle(authorizer=rec)
    beta = _seed_version(cycle, "beta", "inactive")
    cycle.start_canary(beta, operation_id="w728-ca-r")
    _set_version(cycle, beta, status="inactive", canary_percentage=0)
    out = cycle.start_canary(beta, operation_id="w728-ca-r")
    assert out.get("replayed") is True and rec.results[-1].is_replay
    assert _version(cycle, beta).status == "inactive"  # لا أثرَ ثانٍ


def test_c4_promote_replay_no_double_rows(rec: RecordingAuthorizer) -> None:
    cycle = ModelPromotionCycle(authorizer=rec)
    beta = _seed_version(cycle, "beta", "inactive")
    active_before = {
        v["version_id"]
        for v in cycle.list_versions()
        if v["track"] == "alpha" and v["status"] == "active"
    }
    cycle.promote_beta_to_alpha(beta, operation_id="w728-pr-r")
    retired_by_this = [
        v["version_id"]
        for v in cycle.list_versions()
        if v["version_id"] in active_before and v["status"] == "retired"
    ]
    # استعادةُ اللقطتينِ (النسخةُ والألفا الذي أحالَه هو) فيتطابقُ المفتاحُ (سابقةُ W-723)
    _set_version(cycle, beta, track="beta", status="inactive")
    for version_id in retired_by_this:
        _set_version(cycle, version_id, status="active")
    out = cycle.promote_beta_to_alpha(beta, operation_id="w728-pr-r")
    assert out.get("replayed") is True and rec.results[-1].is_replay
    assert _version(cycle, beta).track == "beta"  # لا كتابةَ ثانيةً بعدَ الاستعادة


def test_c4_check_rate_replay_count_unchanged(rec: RecordingAuthorizer) -> None:
    limiter = RateLimiter(authorizer=rec)
    identifier = f"w728-ip-r-{uuid.uuid4().hex[:6]}"
    limiter.check_rate(identifier, "/api/x", operation_id="w728-rt-r")
    out = limiter.check_rate(identifier, "/api/x", operation_id="w728-rt-r")
    assert out.get("replayed") is True and rec.results[-1].is_replay
    assert out["count"] == 1  # الإعادةُ لا تزيدُ العدّادَ


def test_c4_issue_certificate_replay_one_row(rec: RecordingAuthorizer) -> None:
    tls = TLSCertManager(authorizer=rec)
    cert_id = f"w728-cert-r-{uuid.uuid4().hex[:6]}"
    tls.issue_certificate("w728.example", operation_id=cert_id)
    out = tls.issue_certificate("w728.example", operation_id=cert_id)
    assert out.get("replayed") is True and rec.results[-1].is_replay
    assert _count(tls, sec.TLSCertificateModel, cert_id=cert_id) == 1


def test_c4_verify_second_call_reads_without_crossing(rec: RecordingAuthorizer) -> None:
    """بعدَ الإقفالِ يعودُ التحقُّقُ قراءةً صرفةً — لا عبورَ ثانيًا (مسارُ الرفضِ)."""
    tls = TLSCertManager(authorizer=rec)
    cert_id = _seed_cert(tls, datetime.now(UTC) - timedelta(days=1))
    tls.verify_certificate(cert_id)
    crossings = len(rec.results)
    assert tls.verify_certificate(cert_id) == {"valid": False, "reason": "expired"}
    assert len(rec.results) == crossings


def test_c4_create_session_two_calls_two_distinct_sessions() -> None:
    """مفتاحُ الجلسةِ بصمةُ الرمزِ — كلُّ استدعاءٍ جلسةٌ جديدةٌ، لا إعادةَ (§ 9.10.5)."""
    rbac = RBACSystem()
    first = rbac.create_session("w728-u-2x", "citizen")
    second = rbac.create_session("w728-u-2x", "citizen")
    assert first["session_token"] != second["session_token"]
    session = rbac._Session()
    try:
        rows = session.query(sec.UserSessionModel).filter_by(username="w728-u-2x").count()
    finally:
        session.close()
    assert rows == 2


# ═════════════════════════════════════════════════════════════════════════════
# الصنفُ 5 — المعوِّضُ على المسارِ الحقيقيّ
# ═════════════════════════════════════════════════════════════════════════════
BROKEN = "فشلٌ بعدَ الكتابة"


def _break_commit(monkeypatch: pytest.MonkeyPatch, scope: str) -> None:
    """انكسارُ مرحلةِ التثبيتِ لعبورِ السطحِ وحدَه (نطاقُ مفتاحِه) بعدَ عودةِ المُطبِّق."""
    from core.sovereignty.idempotency import IdempotencyLedger

    original = IdempotencyLedger.mark_succeeded

    def _fail(self: Any, *args: Any, **kwargs: Any) -> Any:
        if kwargs["key"].scope == scope:
            raise RuntimeError("فشلٌ بعدَ الكتابة — انكسارُ مرحلةِ التثبيت")
        return original(self, *args, **kwargs)

    monkeypatch.setattr(IdempotencyLedger, "mark_succeeded", _fail)


def test_c5_collect_failure_deletes_row(monkeypatch: pytest.MonkeyPatch) -> None:
    cycle = LearningCycle()
    _break_commit(monkeypatch, lc.DATASET_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        cycle.collect_experiences(
            [{"type": "gap", "outcome": {"success": True}}],
            operation_id=f"w728-ds-c5-{uuid.uuid4().hex[:6]}",
        )
    session = cycle._Session()
    try:
        rows = (
            session.query(lc.ExperienceDatasetModel)
            .filter(lc.ExperienceDatasetModel.dataset_id.startswith("w728-ds-c5"))
            .count()
        )
    finally:
        session.close()
    assert rows == 0


def test_c5_complete_failure_restores_run(monkeypatch: pytest.MonkeyPatch) -> None:
    cycle = LearningCycle()
    run_id = _seed_run(cycle)
    _break_commit(monkeypatch, lc.TRAINING_COMPLETE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        cycle.complete_training(run_id, 1.0)
    run = _run(cycle, run_id)
    assert run["status"] == "running" and run["final_loss"] is None


def _run(owner: LearningCycle, run_id: str) -> dict[str, Any]:
    session = owner._Session()
    try:
        row = session.query(lc.TrainingRunModel).filter_by(run_id=run_id).one()
        return {
            "status": row.status,
            "final_loss": row.final_loss,
            "epochs_completed": row.epochs_completed,
        }
    finally:
        session.close()


def test_c5_shadow_failure_restores_beta(monkeypatch: pytest.MonkeyPatch) -> None:
    cycle = ModelPromotionCycle()
    alpha = _seed_version(cycle, "alpha", "active")
    beta = _seed_version(cycle, "beta", "inactive")
    _break_commit(monkeypatch, lc.SHADOW_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        cycle.start_shadow(alpha, beta)
    version = _version(cycle, beta)
    assert version.status == "inactive" and version.shadow_pairs == "[]"


def test_c5_canary_failure_restores_beta(monkeypatch: pytest.MonkeyPatch) -> None:
    cycle = ModelPromotionCycle()
    beta = _seed_version(cycle, "beta", "inactive")
    _break_commit(monkeypatch, lc.CANARY_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        cycle.start_canary(beta)
    version = _version(cycle, beta)
    assert version.status == "inactive" and version.canary_percentage == 0


def test_c5_promote_failure_restores_both_rows(monkeypatch: pytest.MonkeyPatch) -> None:
    """أثرانِ معلنانِ: فشلُ التثبيتِ يعكسُهما معًا — الترقيةُ والاستيداع (§ 9.10.5)."""
    cycle = ModelPromotionCycle()
    beta = _seed_version(cycle, "beta", "inactive")
    active_before = {
        v["version_id"]
        for v in cycle.list_versions()
        if v["track"] == "alpha" and v["status"] == "active"
    }
    _break_commit(monkeypatch, lc.PROMOTE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        cycle.promote_beta_to_alpha(beta)
    version = _version(cycle, beta)
    assert version.track == "beta" and version.status == "inactive"
    active_after = {
        v["version_id"]
        for v in cycle.list_versions()
        if v["track"] == "alpha" and v["status"] == "active"
    }
    assert active_before <= active_after  # الألفا النشطُ عادَ نشطًا


def test_c5_create_session_failure_deletes_row(monkeypatch: pytest.MonkeyPatch) -> None:
    rbac = RBACSystem()
    username = f"w728-u-c5-{uuid.uuid4().hex[:6]}"
    _break_commit(monkeypatch, sec.SESSION_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        rbac.create_session(username, "citizen")
    session = rbac._Session()
    try:
        rows = session.query(sec.UserSessionModel).filter_by(username=username).count()
    finally:
        session.close()
    assert rows == 0


def test_c5_check_rate_failure_restores_created_row(monkeypatch: pytest.MonkeyPatch) -> None:
    limiter = RateLimiter()
    identifier = f"w728-ip-c5a-{uuid.uuid4().hex[:6]}"
    _break_commit(monkeypatch, sec.RATE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        limiter.check_rate(identifier, "/api/x")
    session = limiter._Session()
    try:
        rows = session.query(sec.RateLimitModel).filter_by(identifier=identifier).count()
    finally:
        session.close()
    assert rows == 0


def test_c5_check_rate_failure_restores_counter(monkeypatch: pytest.MonkeyPatch) -> None:
    limiter = RateLimiter()
    identifier = f"w728-ip-c5b-{uuid.uuid4().hex[:6]}"
    _seed_rate(limiter, identifier, "/api/x", 7)
    _break_commit(monkeypatch, sec.RATE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        limiter.check_rate(identifier, "/api/x")
    session = limiter._Session()
    try:
        row = session.query(sec.RateLimitModel).filter_by(identifier=identifier).one()
    finally:
        session.close()
    assert row.request_count == 7


def test_c5_issue_certificate_failure_deletes_row(monkeypatch: pytest.MonkeyPatch) -> None:
    tls = TLSCertManager()
    cert_id = f"w728-cert-c5-{uuid.uuid4().hex[:6]}"
    _break_commit(monkeypatch, sec.CERT_ISSUE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        tls.issue_certificate("w728.example", operation_id=cert_id)
    assert _count(tls, sec.TLSCertificateModel, cert_id=cert_id) == 0


def test_c5_verify_expiry_failure_restores_active(monkeypatch: pytest.MonkeyPatch) -> None:
    tls = TLSCertManager()
    cert_id = _seed_cert(tls, datetime.now(UTC) - timedelta(days=1))
    _break_commit(monkeypatch, sec.CERT_EXPIRE_SCOPE)
    with pytest.raises(Exception, match=BROKEN):
        tls.verify_certificate(cert_id)
    session = tls._Session()
    try:
        row = session.query(sec.TLSCertificateModel).filter_by(cert_id=cert_id).one()
    finally:
        session.close()
    assert row.status == "active"
