"""
فحوصُ WI-117 — حارسُ `require_king` على المساراتِ الخمسةِ (W-689)
الهدف: إثباتُ أنَّ رفعَ زرِّ التوقّفِ (الخدمتَينِ) وإنشاءَ الترقيةِ وفحصَ البوّابةِ وتوقيعَ
    الموافقةِ لا يعبُرُها إلّا رمزٌ ملكيٌّ — فالمواطنُ يُصدُّ (403) والملكُ يمرُّ، وأنَّ
    الموقِّعَ في الموافقةِ هويةُ الرمزِ لا جسمَ الطلبِ.
النطاق: المساراتُ الخمسةُ المحروسةُ حصرًا (governance: reset/promotions/gates ·
    control_console: reset/approval) — «التفعيلُ» يبقى بنصِّ D25-2 (W-675/WI-114).
المالك: Perplexity Computer (WI-117 · المنسِّقُ GLM-5.3 · تصميمُ W-687)
تاريخ الإنشاء: 2026-10-26
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from amos_federation.services.control_console.main import app as console_app
from amos_federation.services.governance.main import app as governance_app

from .per_test_auth import PerTestAuthHeaders

governance_client = TestClient(governance_app)
console_client = TestClient(console_app)

CITIZEN = PerTestAuthHeaders("wi117-citizen", ["governance:read", "governance:write"])
KING = PerTestAuthHeaders("king", ["governance:read", "governance:write"], role="king")


def test_governance_reset_citizen_forbidden() -> None:
    """مواطنٌ لا يرفعُ زرَّ التوقّفِ من خدمةِ الحوكمةِ (WI-117)."""
    resp = governance_client.post("/v1/system/kill-switch/reset", headers=CITIZEN)
    assert resp.status_code == 403


def test_governance_reset_king_allowed() -> None:
    """الملكُ يرفعُ زرَّ التوقّفِ من خدمةِ الحوكمةِ (WI-117)."""
    governance_client.post(
        "/v1/system/kill-switch",
        headers=CITIZEN,
        json={"level": "alert", "reason": "wi117", "activated_by": "tester"},
    )
    resp = governance_client.post("/v1/system/kill-switch/reset", headers=KING)
    assert resp.status_code == 200
    assert resp.json()["level"] == "normal"


def test_governance_promotions_citizen_forbidden() -> None:
    """مواطنٌ لا يطلبُ ترقيةً (WI-117)."""
    resp = governance_client.post(
        "/v1/promotions", headers=CITIZEN, json={"model_id": "wi117-model"}
    )
    assert resp.status_code == 403


def test_governance_promotions_king_allowed() -> None:
    """الملكُ يطلبُ ترقيةً (WI-117)."""
    resp = governance_client.post("/v1/promotions", headers=KING, json={"model_id": "wi117-model"})
    assert resp.status_code == 201
    assert resp.json()["status"] == "in_progress"


def test_governance_gates_citizen_forbidden() -> None:
    """مواطنٌ لا يفحصُ بوّابةَ ترقيةٍ (WI-117)."""
    create = governance_client.post(
        "/v1/promotions", headers=KING, json={"model_id": "wi117-gates"}
    )
    promo_id = create.json()["promotion_id"]
    resp = governance_client.post(
        f"/v1/promotions/{promo_id}/gates",
        headers=CITIZEN,
        json={"gate_name": "evaluation", "passed": True},
    )
    assert resp.status_code == 403


def test_governance_gates_king_allowed() -> None:
    """الملكُ يفحصُ بوّابةَ ترقيةٍ (WI-117)."""
    create = governance_client.post(
        "/v1/promotions", headers=KING, json={"model_id": "wi117-gates-king"}
    )
    promo_id = create.json()["promotion_id"]
    resp = governance_client.post(
        f"/v1/promotions/{promo_id}/gates",
        headers=KING,
        json={"gate_name": "evaluation", "passed": True},
    )
    assert resp.status_code == 200
    assert resp.json()["gates"]["evaluation"]["status"] == "passed"


def test_console_reset_citizen_forbidden() -> None:
    """مواطنٌ لا يرفعُ زرَّ التوقّفِ من وحدةِ التحكّمِ (WI-117)."""
    resp = console_client.post("/v1/kill-switch/reset", headers=CITIZEN)
    assert resp.status_code == 403


def test_console_reset_king_allowed() -> None:
    """الملكُ يرفعُ زرَّ التوقّفِ من وحدةِ التحكّمِ (WI-117)."""
    console_client.post(
        "/v1/kill-switch",
        headers=CITIZEN,
        json={"level": "alert", "reason": "wi117", "activated_by": "tester"},
    )
    resp = console_client.post("/v1/kill-switch/reset", headers=KING)
    assert resp.status_code == 200
    assert resp.json()["level"] == "normal"


def test_console_approval_citizen_forbidden() -> None:
    """مواطنٌ لا يوقِّعُ موافقةً من وحدةِ التحكّمِ (WI-117)."""
    resp = console_client.post("/v1/approval", headers=CITIZEN, json={"decision": "approve"})
    assert resp.status_code == 403


def test_console_approval_king_allowed() -> None:
    """الملكُ يوقِّعُ موافقةً — والموقِّعُ هويةُ الرمزِ لا جسمَ الطلبِ (WI-117)."""
    resp = console_client.post(
        "/v1/approval",
        headers=KING,
        json={"decision": "approve", "signed_by": "spoofed-user"},
    )
    assert resp.status_code == 200
    assert resp.json()["signed_by"] == "king"
