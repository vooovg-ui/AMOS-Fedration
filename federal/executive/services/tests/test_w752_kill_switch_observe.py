"""
فحوصُ W-752 — WI-085 المرحلةُ الأولى: مصدرُ مستوى زرِّ التوقّفِ الفدراليُّ ومراقبتُه بلا منع (Q-79 · ب · م2 · غ1)
الهدف: إثباتُ معيارِ القبولِ § 10.6 (2) و(3) من `docs/audit/WI085_KILL_SWITCH_INJECTION_DESIGN.md`: الأشكالُ الخمسةُ للقراءة،
    وأنَّ غيابَ الصفِّ لا يُنشئُه، وأنَّ البوّابةَ التي يبنيها الجسرُ تُسجِّلُ «ما كانَ سيمنعُه» **ولا تمنع** — بطلبِ HTTP حقيقيٍّ
    على تطبيقِ واجهةِ التحكّمِ وقاعدتِه.
النطاق: `kill_switch_level_source.py` وتسجيلُه في `ConstitutionalAuthorizer._build_gateway` — لا منعَ ولا تغييرَ حكم.
المالك: Perplexity Computer (قيدُ W-752 · البندُ WI-085)
تاريخ الإنشاء: 2026-10-30
تاريخ آخر تعديل: 2026-10-30
"""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING, Any

import pytest
from fastapi.testclient import TestClient

from amos_federation.common.database import SystemStateModel, get_session_factory
from amos_federation.common.persistent import PersistentSystemStateStore
from amos_federation.services.control_console.main import app
from amos_federation.services.executive_core.kill_switch_level_source import (
    LEGACY_NAME_LEVEL,
    OBSERVATION_LOGGER,
    PersistentKillSwitchLevelSource,
    level_from_stored,
)
from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer

from .per_test_auth import PerTestAuthHeaders

if TYPE_CHECKING:
    from collections.abc import Iterator

AUTH_HEADERS = PerTestAuthHeaders("w752-operator", ["read", "write"])
client = TestClient(app)


def _delete_state_row() -> None:
    session = get_session_factory()()
    try:
        session.query(SystemStateModel).filter(SystemStateModel.id == "system").delete()
        session.commit()
    finally:
        session.close()


def _state_rows() -> int:
    session = get_session_factory()()
    try:
        return session.query(SystemStateModel).filter(SystemStateModel.id == "system").count()
    finally:
        session.close()


def _write_raw_level(value: str) -> None:
    PersistentSystemStateStore().get()  # يضمنُ الصفَّ
    session = get_session_factory()()
    try:
        row = session.query(SystemStateModel).filter(SystemStateModel.id == "system").first()
        row.level = value
        session.commit()
    finally:
        session.close()


@pytest.fixture(autouse=True)
def _normal_after() -> Iterator[None]:
    yield
    PersistentSystemStateStore().reset()


def _observations(caplog: pytest.LogCaptureFixture) -> list[dict[str, Any]]:
    out = []
    for rec in caplog.records:
        if rec.name == OBSERVATION_LOGGER and rec.getMessage().startswith(
            "kill_switch_would_block "
        ):
            out.append(json.loads(rec.getMessage().split(" ", 1)[1]))
    return out


# ── القراءةُ: الأشكالُ الخمسة (§ 10.4) ─────────────────────────────────────


@pytest.mark.parametrize(
    ("stored", "expected"),
    [
        ("0", (0, "constitutional")),
        ("3", (3, "constitutional")),
        ("5", (5, "constitutional")),
        ("normal", (0, "legacy_name")),
        ("alert", (1, "legacy_name")),
        ("degraded", (3, "legacy_name")),
        ("halt", (4, "legacy_name")),
        ("6", (5, "unknown")),
        ("-1", (5, "unknown")),
        ("HALT", (5, "unknown")),
        ("", (5, "unknown")),
        (None, (5, "unknown")),
    ],
)
def test_level_from_stored_forms(stored: Any, expected: tuple[int, str]) -> None:
    assert level_from_stored(stored) == expected


def test_legacy_names_follow_m2_derivation_lowest() -> None:
    """الاسمُ القديمُ ⇐ أدنى مستوًى يوافقُ اشتقاقَ م2 (§ 3): 1–2 alert · 3 degraded · 4–5 halt."""
    assert LEGACY_NAME_LEVEL == {"normal": 0, "alert": 1, "degraded": 3, "halt": 4}


def test_absent_row_reads_five_and_is_not_created() -> None:
    """غ1: الصفُّ الغائبُ يُقرأُ 5 — ولا يُنشئُه المصدرُ (خلافَ `get()` المقيسِ في W-751)."""
    _delete_state_row()
    assert _state_rows() == 0
    reading = PersistentKillSwitchLevelSource().read()
    assert (reading.level, reading.form) == (5, "absent")
    assert _state_rows() == 0


def test_source_reads_each_call_without_cache() -> None:
    src = PersistentKillSwitchLevelSource()
    PersistentSystemStateStore().set_level("degraded", "w752", "test")
    assert src.read().level == 3
    PersistentSystemStateStore().set_level("halt", "w752", "test")
    assert src.read().level == 4
    _write_raw_level("2")
    assert (src.read().level, src.read().form) == (2, "constitutional")


# ── التسجيلُ في البوّابةِ المبنيّة ──────────────────────────────────────────


def test_built_gateway_has_persistent_source_registered() -> None:
    gw = ConstitutionalAuthorizer().gateway
    assert isinstance(gw._kill_switch_source, PersistentKillSwitchLevelSource)
    assert gw._kill_switch_sink is not None


def test_guard_at_halt_allows_and_logs_would_block(caplog: pytest.LogCaptureFixture) -> None:
    """عبورٌ فدراليٌّ والزرُّ halt: يمرُّ (لا منع) وتُسجَّلُ ملاحظةٌ بالمستوى 4."""
    auth = ConstitutionalAuthorizer()
    PersistentSystemStateStore().set_level("halt", "w752", "test")
    caplog.set_level(logging.WARNING, logger=OBSERVATION_LOGGER)
    verdict = auth.gateway.review(auth._request("create_task", "w752:target", {}, None))
    assert verdict.allowed
    obs = _observations(caplog)
    assert len(obs) == 1
    assert obs[0]["action"] == "create_task"
    assert obs[0]["effective_level"] == 4
    assert obs[0]["source_form"] == "legacy_name"
    assert obs[0]["mode"] == "OBSERVE"


def test_containment_action_at_halt_not_logged(caplog: pytest.LogCaptureFixture) -> None:
    auth = ConstitutionalAuthorizer()
    PersistentSystemStateStore().set_level("halt", "w752", "test")
    caplog.set_level(logging.WARNING, logger=OBSERVATION_LOGGER)
    auth.gateway.review(auth._request("run_health_check", "w752:target", {}, None))
    assert _observations(caplog) == []


def test_normal_level_not_logged(caplog: pytest.LogCaptureFixture) -> None:
    auth = ConstitutionalAuthorizer()
    PersistentSystemStateStore().reset()
    caplog.set_level(logging.WARNING, logger=OBSERVATION_LOGGER)
    auth.gateway.review(auth._request("create_task", "w752:target", {}, None))
    assert _observations(caplog) == []


# ── المسبارُ الحيُّ بطلباتِ HTTP (§ 10.6 (3)) ──────────────────────────────


def test_live_http_halt_take_exam_passes_and_logs(caplog: pytest.LogCaptureFixture) -> None:
    """`POST /v1/kill-switch` halt ⇐ `POST /v1/specialization/exam` يمرُّ (200) ويُسجَّلُ «ما كانَ سيُمنَع» بالمستوى 4."""
    r = client.post(
        "/v1/kill-switch",
        json={"level": "halt", "reason": "مسبارُ W-752", "activated_by": "w752"},
        headers=AUTH_HEADERS,
    )
    assert r.status_code == 200, r.text
    assert PersistentSystemStateStore().get()["level"] == "halt"
    caplog.set_level(logging.WARNING, logger=OBSERVATION_LOGGER)
    r = client.post(
        "/v1/specialization/exam",
        params={"agent_id": "w752-agent", "track": "finance", "score": 90.0},
        headers=AUTH_HEADERS,
    )
    assert r.status_code == 200, r.text
    assert "error" not in r.json()
    obs = [o for o in _observations(caplog) if o["action"] == "record_curriculum_step"]
    assert obs, "لم تُسجَّلْ ملاحظةٌ لـrecord_curriculum_step والزرُّ halt"
    assert obs[0]["effective_level"] == 4
    assert obs[0]["request_level"] == 0
    assert "المستوى 4" in obs[0]["would_block_reason"]
