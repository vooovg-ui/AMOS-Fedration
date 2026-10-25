"""
فحوصُ WI-114 — عبورُ `governance/canary.py` الحدَّ السياديَّ: السطحانِ 1 و3 (W-675)
الهدف: إثباتُ أنَّ رفعَ زرِّ التوقّفِ وطلبَ الترقيةِ يمرّانِ بالبوّابةِ الحقيقيّةِ بأفعالِ المعجم، وأنَّ
    «التفعيلَ» بمستوى أدنى من القائمِ خفضٌ يرفضُه الحدُّ فلا يُكتَبُ شيءٌ (DISC-138) — برفضٍ حقيقيٍّ
    من محرّكِ القواعدِ لا ببوّابةٍ مُستبدَلة.
النطاق: `activate_kill_switch` (السطح 1) و`create_promotion` (السطح 3) وحدَهما. السطحانِ 2 و4 بعدَ
    D25-1 بشروطِه — فلا فحصَ لهما هنا.
المالك: Perplexity Computer (WI-114 · المنسِّقُ الحاضرُ Claude Opus 5.5)
تاريخ الإنشاء: 2026-10-25
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest
from fastapi.testclient import TestClient

from amos_federation.common.auth import create_access_token
from amos_federation.common.persistent import PersistentPromotionStore
from amos_federation.services.governance import canary
from amos_federation.services.governance.main import app

if TYPE_CHECKING:
    from collections.abc import Iterator

client = TestClient(app)


def _citizen_headers() -> dict[str, str]:
    # رمزُ مواطنٍ — لا دورَ ملكيٌّ؛ والمسارُ يكتفي اليومَ بـ`require_auth` (W-672).
    token = create_access_token("citizen-wi114", ["read", "write"], role="citizen")
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(autouse=True)
def _fresh_canary_authorizer() -> Iterator[None]:
    canary.reset_canary_authorizer()
    yield
    canary.reset_canary_authorizer()


def _records() -> list[Any]:
    return list(canary._canary_authorizer().gateway.records)


def _actions(records: list[Any]) -> list[str]:
    """كلُّ عبورٍ يتركُ أثرَين: إذنٌ صادرٌ (AUTHORIZED) ثمَّ اكتمالٌ (COMPLETED) — مقيسٌ في W-675."""
    return sorted({r.action for r in records})


def _completions(records: list[Any]) -> list[str]:
    return [str(r.completion.value) for r in records]


def _drop_settle(monkeypatch: pytest.MonkeyPatch) -> Any:
    """إسقاطُ تثبيتِ النجاحِ بعدَ التزامِ المُطبِّق (سابقةُ W-603 · wi106) — فيعملُ المُعوِّض."""
    ledger = canary._canary_authorizer().boundary.idempotency_ledger
    original = type(ledger).mark_succeeded

    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("تثبيتُ النجاحِ مُسقَطٌ — WI-114")

    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)
    return ledger, original


def _promotion_ids() -> set[str]:
    return {p["promotion_id"] for p in PersistentPromotionStore().list_all()}


# ── السطح 1 ───────────────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    ("current", "requested", "verb"),
    [
        ("normal", "halt", canary.ACTION_ACTIVATE_KILL_SWITCH),
        ("alert", "alert", canary.ACTION_ACTIVATE_KILL_SWITCH),
        ("degraded", "halt", canary.ACTION_ACTIVATE_KILL_SWITCH),
        ("halt", "normal", canary.ACTION_LOWER_KILL_SWITCH),
        ("halt", "alert", canary.ACTION_LOWER_KILL_SWITCH),
        ("degraded", "alert", canary.ACTION_LOWER_KILL_SWITCH),
    ],
)
def test_kill_switch_verb_routes_lowering(current: str, requested: str, verb: str) -> None:
    assert canary.kill_switch_verb(current, requested) == verb


def test_raise_crosses_gateway_with_activate_verb() -> None:
    before = len(_records())
    state = canary.activate_kill_switch("halt", "wi114 raise", "wi114-actor")
    assert state["level"] == "halt"
    new = _records()[before:]
    assert _actions(new) == [canary.ACTION_ACTIVATE_KILL_SWITCH]
    assert {r.actor for r in new} == {canary.CANARY_ACTOR.lower()}  # قيمةُ `Branch.EXECUTIVE`
    assert {r.decision for r in new} == {"ALLOW"}
    assert _completions(new)[-1] == "COMPLETED"


def test_two_raises_in_the_same_second_both_cross() -> None:
    """معرِّفُ الإذنِ بالثانية — والمُعرِّفُ في الهدفِ يمنعُ تصادمَ رفعَينِ مشروعَين."""
    canary.activate_kill_switch("alert", "wi114 first", "wi114-a")
    state = canary.activate_kill_switch("halt", "wi114 second", "wi114-b")
    assert (state["level"], state["activated_by"]) == ("halt", "wi114-b")


def test_lowering_via_activate_is_refused_and_writes_nothing() -> None:
    canary.activate_kill_switch("halt", "wi114 halt", "wi114-actor")
    before = len(_records())
    with pytest.raises(canary.KillSwitchRefusedError) as info:
        canary.activate_kill_switch("normal", "disguised lowering", "king")
    assert info.value.status_code == 403
    assert info.value.verb == canary.ACTION_LOWER_KILL_SWITCH
    status = canary.get_system_status()
    assert status["level"] == "halt"
    assert status["reason"] == "wi114 halt"
    assert status["activated_by"] == "wi114-actor"
    new = _records()[before:]
    assert _actions(new) == [canary.ACTION_LOWER_KILL_SWITCH]
    assert "ALLOW" not in {r.decision for r in new}
    assert "COMPLETED" not in _completions(new)


def test_http_citizen_cannot_lower_via_activate() -> None:
    """طلبُ HTTP (TestClient) برمزِ مواطن: halt ثمَّ activate بـnormal ⇒ 403 والمستوى باقٍ halt."""
    raise_resp = client.post(
        "/v1/system/kill-switch",
        headers=_citizen_headers(),
        json={"level": "halt", "reason": "wi114 http", "activated_by": "x"},
    )
    assert raise_resp.status_code == 200
    resp = client.post(
        "/v1/system/kill-switch",
        headers=_citizen_headers(),
        json={"level": "normal", "reason": "citizen lowers", "activated_by": "king"},
    )
    assert resp.status_code == 403, resp.text
    assert resp.json()["detail"]["action"] == canary.ACTION_LOWER_KILL_SWITCH
    assert canary.get_system_status()["level"] == "halt"


def test_kill_switch_compensator_restores_previous_snapshot(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired

    canary.activate_kill_switch("alert", "wi114 before", "wi114-before")
    ledger, original = _drop_settle(monkeypatch)
    with pytest.raises(CompensationRequired) as caught:
        canary.activate_kill_switch("halt", "wi114 failing", "wi114-failing")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    assert caught.value.outcome.state_is_clean is True
    status = canary.get_system_status()
    assert (status["level"], status["reason"], status["activated_by"]) == (
        "alert",
        "wi114 before",
        "wi114-before",
    )


# ── السطح 3 ───────────────────────────────────────────────────────────────────


def test_create_promotion_crosses_with_request_verb_not_promote() -> None:
    before = len(_records())
    promo = canary.create_promotion("model-wi114", requested_by="wi114-requester")
    assert promo["status"] == "in_progress"
    assert promo["promotion_id"] in _promotion_ids()
    new = _records()[before:]
    assert _actions(new) == [canary.ACTION_REQUEST_PROMOTION]
    assert canary.ACTION_REQUEST_PROMOTION != "promote_model"
    assert {r.decision for r in new} == {"ALLOW"}
    assert _completions(new)[-1] == "COMPLETED"


def test_create_promotion_denied_verb_writes_no_row(monkeypatch: pytest.MonkeyPatch) -> None:
    """رفضٌ حقيقيٌّ: `promote_model` DENY للفاعلِ التنفيذيِّ (مسبارُ W-675) ⇒ لا صفّ."""
    monkeypatch.setattr(canary, "ACTION_REQUEST_PROMOTION", "promote_model")
    ids_before = _promotion_ids()
    with pytest.raises(Exception) as info:
        canary.create_promotion("model-wi114-denied", requested_by="wi114")
    assert type(info.value).__name__ == "SovereigntyViolation"
    assert _promotion_ids() == ids_before


def test_create_promotion_compensator_cancels(monkeypatch: pytest.MonkeyPatch) -> None:
    from core.sovereignty.compensation import CompensationRequired

    ids_before = _promotion_ids()
    ledger, original = _drop_settle(monkeypatch)
    with pytest.raises(CompensationRequired) as caught:
        canary.create_promotion("model-wi114-comp", requested_by="wi114")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    assert caught.value.outcome.state_is_clean is True
    created = _promotion_ids() - ids_before
    assert len(created) == 1
    row = PersistentPromotionStore().get(created.pop())
    assert row is not None
    assert row["status"] == "cancelled"
