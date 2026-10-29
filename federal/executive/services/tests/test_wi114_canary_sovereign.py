"""
فحوصُ WI-114 — عبورُ `governance/canary.py` الحدَّ السياديَّ: الأسطحُ الأربعةُ (W-675 · W-740)
الهدف: إثباتُ أنَّ زرَّ التوقّفِ والترقيةَ يمرّانِ بالبوّابةِ الحقيقيّةِ بأفعالِ المعجم، وأنَّ
    «التفعيلَ» بمستوى أدنى من القائمِ خفضٌ يرفضُه الحدُّ فلا يُكتَبُ شيءٌ (DISC-138) — برفضٍ حقيقيٍّ
    من محرّكِ القواعدِ لا ببوّابةٍ مُستبدَلة.
النطاق: الأسطحُ الأربعةُ: `activate_kill_switch` (1 · W-675) و`reset_kill_switch` (2 · W-740)
    و`create_promotion` (3 · W-675) و`check_gate` (4 · W-740) — بمعاييرِ القبولِ في A1A § 7.5:
    المواطنُ يُصدُّ (403)، والملكُ يعبرُ بدليلِه من `require_king`، والخالي والمزوَّرُ يُرفَضانِ
    (R-008-3 · R-001-1) والرفضُ ذرّيٌّ.
المالك: Perplexity Computer (WI-114 · المنسِّقُ الحاضرُ Claude Opus 5.5)
تاريخ الإنشاء: 2026-10-25
تاريخ آخر تعديل: 2026-10-29 (W-740 — السطحانِ 2 و4 بفحوصِ A1A § 7.5)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest
from fastapi.testclient import TestClient

from amos_federation.common.auth import create_access_token
from amos_federation.common.persistent import PersistentPromotionStore
from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    KingApproval,
)
from amos_federation.services.governance import canary
from amos_federation.services.governance.main import app
from tests.conftest import king_approval

from .per_test_auth import PerTestAuthHeaders

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


# ── السطحان 2 و4 (W-740 · A1A § 7.3/§ 7.4 · معاييرُ القبولِ § 7.5) ────────────

KING = PerTestAuthHeaders("wi114-king", ["governance:read", "governance:write"], role="king")
CITIZEN = PerTestAuthHeaders("wi114-citizen2", ["governance:read", "governance:write"])


def _capture_requests(monkeypatch: pytest.MonkeyPatch) -> list[Any]:
    """التقطِ طلباتِ العبورِ كما بناها الجسرُ (`ActionRequest`) — لا كما تُخمَّن.

    `ExecutionRecord` لا يحملُ البياناتِ الوصفيةَ، فالوسمانِ (`human_approval_source`
    و`human_approval_subject`) يُقاسانِ هنا على الطلبِ نفسِه الذي عبرَ الحدَّ.
    """
    box: list[Any] = []
    original = ConstitutionalAuthorizer._request

    def _spy(self: Any, action: str, target: str, metadata: Any, human_approval: Any = None) -> Any:
        request = original(self, action, target, metadata, human_approval)
        box.append(request)
        return request

    monkeypatch.setattr(ConstitutionalAuthorizer, "_request", _spy)
    return box


def _requests_for(box: list[Any], action: str) -> list[Any]:
    return [r for r in box if r.action == action]


# 1 · مسبارُ HTTP: المواطنُ يُصدُّ والملكُ يعبرُ بدليلِه (§ 7.5/1)


def test_http_citizen_cannot_reset_kill_switch() -> None:
    """رمزُ مواطنٍ على مسارِ الخفضِ ⇒ 403 من `require_king` — يُعادُ قياسُه لا يُفترَض."""
    resp = client.post("/v1/system/kill-switch/reset", headers=CITIZEN)
    assert resp.status_code == 403


def test_http_citizen_cannot_check_gate() -> None:
    """رمزُ مواطنٍ على مسارِ البوّابةِ ⇒ 403 من `require_king`."""
    create = client.post("/v1/promotions", headers=KING, json={"model_id": "wi114-http-c"})
    promo_id = create.json()["promotion_id"]
    resp = client.post(
        f"/v1/promotions/{promo_id}/gates",
        headers=CITIZEN,
        json={"gate_name": "evaluation", "passed": True},
    )
    assert resp.status_code == 403


def test_http_king_reset_crosses_with_evidence_tags(monkeypatch: pytest.MonkeyPatch) -> None:
    """رمزُ ملكٍ ⇒ عبورٌ ALLOW والوسمانِ في الطلبِ: المصدرُ `require_king` وصاحبُه من الرمزِ."""
    canary.activate_kill_switch("halt", "wi114 http king", "wi114-actor")
    box = _capture_requests(monkeypatch)
    resp = client.post("/v1/system/kill-switch/reset", headers=KING)
    assert resp.status_code == 200, resp.text
    assert resp.json()["level"] == "normal"
    assert canary.get_system_status()["level"] == "normal"
    requests = _requests_for(box, canary.ACTION_LOWER_KILL_SWITCH)
    assert len(requests) == 1
    assert requests[0].human_approved is True
    assert requests[0].metadata["human_approval_source"] == "require_king"
    assert requests[0].metadata["human_approval_subject"] == "wi114-king"
    new = _records()[-2:]
    assert {r.decision for r in new} == {"ALLOW"}
    assert _completions(new)[-1] == "COMPLETED"


def test_http_king_final_gate_promotes_with_evidence_tags(monkeypatch: pytest.MonkeyPatch) -> None:
    """البوّابةُ الأخيرةُ برمزِ ملكٍ ⇒ `promote_model` يعبرُ بدليلِه والترقيةُ `promoted`."""
    create = client.post("/v1/promotions", headers=KING, json={"model_id": "wi114-http-king"})
    promo_id = create.json()["promotion_id"]
    box = _capture_requests(monkeypatch)
    for gate in ["evaluation", "shadow", "canary", "human_approval"]:
        resp = client.post(
            f"/v1/promotions/{promo_id}/gates",
            headers=KING,
            json={"gate_name": gate, "passed": True},
        )
        assert resp.status_code == 200, resp.text
    resp = client.post(
        f"/v1/promotions/{promo_id}/gates",
        headers=KING,
        json={"gate_name": "activation", "passed": True},
    )
    assert resp.status_code == 200, resp.text
    assert resp.json()["status"] == "promoted"
    # البواباتُ غيرُ الأخيرةِ فعلٌ حرٌّ بلا دليلٍ؛ والأخيرةُ وحدَها تحملُه
    free = _requests_for(box, canary.ACTION_RECORD_PROMOTION_GATE)
    assert free and all(r.human_approved is False for r in free)
    promoted = _requests_for(box, canary.ACTION_PROMOTE_MODEL)
    assert len(promoted) == 1
    assert promoted[0].human_approved is True
    assert promoted[0].metadata["human_approval_source"] == "require_king"
    assert promoted[0].metadata["human_approval_subject"] == "wi114-king"


# 2 · النداءُ المباشرُ بلا دليلٍ ⇒ رفضٌ ذرّيٌّ (§ 7.5/2)


def test_direct_bare_reset_refused_r008_3_writes_nothing() -> None:
    canary.activate_kill_switch("halt", "wi114 bare", "wi114-actor")
    before = len(_records())
    with pytest.raises(canary.KillSwitchRefusedError) as info:
        canary.reset_kill_switch(None)
    assert info.value.status_code == 403
    assert info.value.verb == canary.ACTION_LOWER_KILL_SWITCH
    assert "R-008-3" in str(info.value)
    status = canary.get_system_status()
    assert (status["level"], status["reason"]) == ("halt", "wi114 bare")
    new = _records()[before:]
    assert _actions(new) == [canary.ACTION_LOWER_KILL_SWITCH]
    assert "ALLOW" not in {r.decision for r in new}
    assert "COMPLETED" not in _completions(new)


def test_direct_final_gate_without_approval_refused_r001_1_row_unchanged() -> None:
    promo = canary.create_promotion("wi114-bare-final")
    pid = promo["promotion_id"]
    for gate in ["evaluation", "shadow", "canary", "human_approval"]:
        canary.check_gate(pid, gate, True, "wi114")
    before = len(_records())
    with pytest.raises(canary.PromotionRefusedError) as info:
        canary.check_gate(pid, "activation", True, "wi114")
    assert info.value.status_code == 403
    assert info.value.verb == canary.ACTION_PROMOTE_MODEL
    assert "R-001-1" in str(info.value)
    # ذرّيّةُ الرفضِ: البوّابةُ الأخيرةُ لم تُكتبْ والحالةُ كما كانت
    row = canary.get_promotion(pid)
    assert row is not None
    assert row["gates"]["activation"]["status"] == "pending"
    assert row["status"] == "in_progress"
    new = _records()[before:]
    assert "COMPLETED" not in _completions(new)


def test_direct_nonfinal_gate_is_free_action_without_evidence() -> None:
    """اجتيازُ بوّابةٍ غيرِ أخيرةٍ فعلٌ حرٌّ (`record_promotion_gate`) — ALLOW بلا دليلٍ (مسبارُ W-737)."""
    promo = canary.create_promotion("wi114-free")
    pid = promo["promotion_id"]
    before = len(_records())
    row = canary.check_gate(pid, "evaluation", True, "wi114")
    assert row["gates"]["evaluation"]["status"] == "passed"
    new = _records()[before:]
    assert _actions(new) == [canary.ACTION_RECORD_PROMOTION_GATE]
    assert {r.decision for r in new} == {"ALLOW"}
    assert _completions(new)[-1] == "COMPLETED"


def test_direct_king_approval_crosses_both_surfaces() -> None:
    """الدليلُ الصحيحُ يعبرُ: الخفضُ والبوّابةُ الأخيرةُ — والنداءُ بعدَ الرفضِ مشروعٌ لا إعادةً."""
    canary.activate_kill_switch("degraded", "wi114 before lower", "wi114-actor")
    state = canary.reset_kill_switch(king_approval(canary.ACTION_LOWER_KILL_SWITCH))
    assert state["level"] == "normal"

    promo = canary.create_promotion("wi114-king-final")
    pid = promo["promotion_id"]
    for gate in ["evaluation", "shadow", "canary", "human_approval"]:
        canary.check_gate(pid, gate, True, "wi114")
    row = canary.check_gate(
        pid, "activation", True, "wi114", approval=king_approval(canary.ACTION_PROMOTE_MODEL)
    )
    assert row["status"] == "promoted"


# 3 · الدليلُ المزوَّرُ ⇒ رفضٌ (§ 7.5/3)


class _DuckTypedApproval:
    """كائنٌ له حقولُ `KingApproval` نفسُها من غيرِ النوعِ — تشابهُ الشكلِ لا أصالةَ."""

    source = "require_king"
    subject = "forged"
    role = "king"
    issued_for = "lower_kill_switch"


def test_duck_typed_evidence_refused_like_bare() -> None:
    canary.activate_kill_switch("halt", "wi114 forged", "wi114-actor")
    with pytest.raises(canary.KillSwitchRefusedError) as info:
        canary.reset_kill_switch(_DuckTypedApproval())  # type: ignore[arg-type]
    assert "R-008-3" in str(info.value)
    assert canary.get_system_status()["level"] == "halt"


def test_evidence_issued_for_another_action_refused() -> None:
    """دليلٌ صحيحُ النوعِ صُدِرَ لفعلٍ آخرَ يُعامَلُ كالخالي: لا موافقةَ لغيرِ فعلِها."""
    canary.activate_kill_switch("halt", "wi114 other-action", "wi114-actor")
    with pytest.raises(canary.KillSwitchRefusedError):
        canary.reset_kill_switch(king_approval(canary.ACTION_PROMOTE_MODEL))
    assert canary.get_system_status()["level"] == "halt"


def test_from_verified_claims_rejects_non_king_role() -> None:
    """الدفاعُ الثاني: بناءُ الدليلِ من مطالباتٍ غيرِ ملكيّةٍ يرفعُ لا يُصحِّح."""
    with pytest.raises(Exception) as info:
        KingApproval.from_verified_claims({"role": "citizen", "sub": "x"}, "lower_kill_switch")
    assert type(info.value).__name__ == "SovereigntyUnavailableError"


def test_surface4_compensator_restores_gates_and_status(monkeypatch: pytest.MonkeyPatch) -> None:
    """فشلُ تثبيتِ نجاحِ البوّابةِ الأخيرةِ ⇒ المعوِّضُ يعيدُ البوّاباتِ والحالةَ كما كانتا (A1A § 7.4)."""
    from core.sovereignty.compensation import CompensationRequired

    promo = canary.create_promotion("wi114-comp-final")
    pid = promo["promotion_id"]
    for gate in ["evaluation", "shadow", "canary", "human_approval"]:
        canary.check_gate(pid, gate, True, "wi114")
    ledger, original = _drop_settle(monkeypatch)
    with pytest.raises(CompensationRequired) as caught:
        canary.check_gate(
            pid, "activation", True, "wi114", approval=king_approval(canary.ACTION_PROMOTE_MODEL)
        )
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    assert caught.value.outcome.state_is_clean is True
    # المعوِّضُ أعادَ البوّاباتِ والحالةَ: الأخيرةُ لم تُثبَّتْ والترقيةُ كما كانت
    row = canary.get_promotion(pid)
    assert row is not None
    assert row["gates"]["activation"]["status"] == "pending"
    assert row["status"] == "in_progress"
