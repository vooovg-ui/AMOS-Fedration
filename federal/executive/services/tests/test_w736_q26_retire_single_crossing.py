"""W-736 · Q-26 — retire_agent عبورٌ واحدٌ يعلنُ آثارَ التقاعدِ الثلاثة (G1 § 9.9.8 · DISC-141).

الهدف: إثباتُ أنَّ ثغرةَ Q-26 التي كشفَها مسبارُ مقعدِ المجلسِ (رفضٌ متأخِّرٌ لعبورِ المرآةِ بعدَ نجاحِ
       العبورِ الكانونيِّ يتركُ الكانونَ retired والمرآةَ employed بلا سجلّ) قد سُدَّت: عبورٌ واحدٌ
       (`contain_agent`) يعلنُ الكانونَ والمرآةَ والسجلَّ، ولكلِّ أثرٍ معوِّضُه، وفشلُ أيِّ أثرٍ بعدَ
       سابقِه يُعيدُ الوكيلَ إلى حالتِه السابقةِ كانونًا ومرآةً ولا يتركُ سجلًّا.
النطاق: retire_agent وحدَه. `update_state` نفسُه (سطحُ E1 · فحصُ C2 من المسبار) خارجَ النطاق —
        DISC-142 · Q-81 (ب). حقنُ مستوى القاطعِ في الطلبِ محاكاةٌ معلَنةٌ (نمطُ WI-082 · E1)، لأنَّ
        الجسرَ لا يحقنُه في الإنتاج (DISC-099 · WI-085).
المالك: federal/executive/services — WI-120 (G1 · تصميمُ W-735 § 9.9.8).
تاريخ الإنشاء: 2026-10-29 (W-736)

الفحوصُ الخمسةُ (§ 9.9.8 (7)): (1) سيناريو المقعدِ لكلِّ k · (2) عبورٌ واحدٌ في المستوى الأعلى ·
(3أ) فشلُ المرآةِ بعدَ الكانون · (3ب) فشلُ السجلِّ بعدَ الكانونِ والمرآة · (4) تحقّقٌ مسبقٌ يحفظُ رفضَ ≥3.
والطفرةُ التي تُسقِطُ معوِّضَ الكانونِ تُسقِطُ (3أ) و(3ب): `docs/audit/evidence/W-736/mutation_canonical_compensator.py`.

الدليلُ المُعادُ تشغيلُه (من federal/executive/services):
    ../../../.venv/bin/python -m pytest tests/test_w736_q26_retire_single_crossing.py -q
"""

from __future__ import annotations

import dataclasses
import uuid
from typing import Any

import pytest

from amos_federation.services.agent_runtime import population as pop
from amos_federation.services.agent_runtime.population import get_population_registry
from amos_federation.services.executive_core.agent_identity import get_identity
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
)
from amos_federation.services.governance import expansion as ex
from amos_federation.services.governance.expansion import RetirementRecordModel, RetirementSystem


# ── مُصرِّحاتُ القياس ─────────────────────────────────────────────────────────
class RecordingAuthorizer(ConstitutionalAuthorizer):
    """يسجِّلُ كلَّ نتيجةٍ محروسةٍ وكلَّ طلبِ إذن — للقياسِ لا للقرار (نمطُ WI-082)."""

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


class LateLevelAuthorizer(ConstitutionalAuthorizer):
    """مستوى القاطعِ يرتفعُ بعدَ `after` طلبًا — سيناريو مسبارِ المقعدِ حرفيًّا (القسمُ C)."""

    def __init__(self, level: int, after: int = 0, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.level, self.after, self.n = level, after, 0

    def _request(self, action: str, target: str, metadata: dict[str, Any] | None = None) -> Any:
        request = super()._request(action, target, metadata)
        self.n += 1
        level = self.level if self.n > self.after else 0
        return dataclasses.replace(request, kill_switch_level=level)


def _violation() -> type[Exception]:
    from core.sovereignty.gateway import SovereigntyViolation

    return SovereigntyViolation


def _seed_employed() -> str:
    """وكيلٌ «employed» عبرَ المسارِ المحروس — تجهيزٌ لا سطحٌ مَقيس (نمطُ W-724 والمسبار)."""
    registry = get_population_registry()
    agent_id = f"w736-{uuid.uuid4().hex[:8]}"
    registry.register_agent(
        name=agent_id, role="reserve", category="reserve", permissions=[], agent_id=agent_id
    )
    registry.update_state(agent_id, "employed")
    return agent_id


def _states(agent_id: str) -> tuple[str, str | None, str | None]:
    """(get_agent · الهويةُ الكانونيّة · صفُّ المرآةِ نفسُه) — ثلاثيّةُ المسبار."""
    registry = get_population_registry()
    identity = get_identity(agent_id)
    profile = registry._profile(agent_id)
    return (
        registry.get_agent(agent_id)["state"],
        identity.lifecycle_state if identity is not None else None,
        profile.state if profile is not None else None,
    )


def _records(agent_id: str) -> int:
    rs = RetirementSystem()
    session = rs._Session()
    try:
        return int(session.query(RetirementRecordModel).filter_by(agent_id=agent_id).count())
    finally:
        session.close()


# ═════════════════════════════════════════════════════════════════════════════
# (1) سيناريو المقعد: ارتفاعُ القاطعِ بعدَ k طلبًا — الحالتانِ إمّا الهدفُ كاملًا أو السابقُ كاملًا
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.parametrize("level", [3, 5])
@pytest.mark.parametrize("k", range(0, 9))
def test_1_late_level_rise_never_leaves_half_state(k: int, level: int) -> None:
    agent_id = _seed_employed()
    before = _states(agent_id)
    assert before == ("employed",) * 3
    rs = RetirementSystem(authorizer=LateLevelAuthorizer(level, after=k))
    try:
        rs.retire_agent(agent_id)
        err: Exception | None = None
    except Exception as exc:  # noqa: BLE001 — يُقاسُ نوعُه أدناه
        err = exc
    after, n = _states(agent_id), _records(agent_id)
    full = err is None and n == 1 and after == ("retired",) * 3
    clean = err is not None and n == 0 and after == before
    assert full or clean, f"k={k} level={level} exc={err!r} records={n} after={after}"
    if err is not None:
        assert isinstance(err, _violation())


# ═════════════════════════════════════════════════════════════════════════════
# (2) عبورٌ واحدٌ في المستوى الأعلى يعلنُ الآثارَ الثلاثة
# ═════════════════════════════════════════════════════════════════════════════
def test_2_single_top_level_crossing_with_three_effects() -> None:
    agent_id = _seed_employed()
    rec = RecordingAuthorizer()
    RetirementSystem(authorizer=rec).retire_agent(agent_id)
    assert len(rec.results) == 1, [r.evidence.as_dict()["action"] for r in rec.results]
    assert rec.results[0].evidence.as_dict()["action"] == "contain_agent"
    assert rec.permits == ["contain_agent", "update_population_state"]
    applied = [str(e.signature) for e in rec.results[0].outcome.applied_effects]
    assert len(applied) == 3, applied
    resources = " ".join(applied)
    assert "lifecycle.employed->retired" in resources
    assert "population.state.employed->retired" in resources
    assert "retirement." in resources
    assert _states(agent_id) == ("retired",) * 3 and _records(agent_id) == 1


# ═════════════════════════════════════════════════════════════════════════════
# (3) ترتيبُ الفشلِ المقيس — فشلُ أثرٍ بعدَ سابقِه يُعيدُ الوكيلَ كانونًا ومرآةً
# ═════════════════════════════════════════════════════════════════════════════
def test_3a_mirror_failure_after_canonical_restores_canonical(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired

    agent_id = _seed_employed()
    before = _states(agent_id)

    def _broken_mirror(*_a: Any, **_kw: Any) -> None:
        raise RuntimeError("انكسارُ كتابةِ المرآة")

    monkeypatch.setattr(pop, "_update_population_row_core", _broken_mirror)
    with pytest.raises(CompensationRequired, match="انكسارُ كتابةِ المرآة"):
        RetirementSystem().retire_agent(agent_id)
    monkeypatch.undo()
    assert _states(agent_id) == before
    assert _records(agent_id) == 0


def test_3b_record_failure_after_canonical_and_mirror_restores_both(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired

    agent_id = _seed_employed()
    before = _states(agent_id)

    class _Exploding:
        id = RetirementRecordModel.id
        agent_id = RetirementRecordModel.agent_id

        def __init__(self, **_kw: Any) -> None:
            raise RuntimeError("انكسارُ سجلِّ التقاعد")

    monkeypatch.setattr(ex, "RetirementRecordModel", _Exploding)
    with pytest.raises(CompensationRequired, match="انكسارُ سجلِّ التقاعد"):
        RetirementSystem().retire_agent(agent_id)
    monkeypatch.undo()
    assert _states(agent_id) == before
    assert _records(agent_id) == 0


# ═════════════════════════════════════════════════════════════════════════════
# (4) التحقّقُ المسبقُ يحفظُ رفضَ ≥3 المقيسَ في W-724 — نظيفًا قبلَ أيِّ أثرٍ ولا عبور
# ═════════════════════════════════════════════════════════════════════════════
def test_4_precheck_refuses_at_level3_before_any_crossing() -> None:
    agent_id = _seed_employed()
    before = _states(agent_id)
    auth = LateLevelAuthorizer(3, after=0)
    rec_results: list[Any] = []
    original = auth.guard_declared

    def _spy(*a: Any, **kw: Any) -> Any:
        rec_results.append(a[0] if a else kw.get("action"))
        return original(*a, **kw)

    auth.guard_declared = _spy  # type: ignore[method-assign]
    with pytest.raises(_violation()):
        RetirementSystem(authorizer=auth).retire_agent(agent_id)
    assert rec_results == []
    assert _states(agent_id) == before and _records(agent_id) == 0
