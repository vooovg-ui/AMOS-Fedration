"""الهدف: إثباتُ مرحلةِ المراقبةِ لـWI-085 في النواة (Q-79 · ب · م2 · غ1): البوّابةُ تقرأُ المستوى من مصدرٍ مُسجَّلٍ وتأخذُ الأعلى
وتُسجِّلُ «ما كانَ سيمنعُه» — **ولا تمنع**: الحكمُ والتنفيذُ كما كانا (معيارُ § 10.6 (1) من `docs/audit/WI085_KILL_SWITCH_INJECTION_DESIGN.md`).

المالك: tests/sovereignty/ — البندُ WI-085 (قيدُ W-752 · وسقفُ الذاكرةِ بقيدِ W-779)
تاريخ الإنشاء: 2026-10-30
تاريخ آخر تعديل: 2026-11-01 (W-779 — اختباراتُ سقفِ الملاحظات · § 5 من WI085_MONITORING_EXIT_CRITERION) · وقبله: 2026-10-30
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
import core.sovereignty.crown as crown_mod
import core.sovereignty.gateway as gateway_mod
from core.constitutional_engine.engine import ConstitutionalEngine
from core.constitutional_engine.ledger import ConstitutionalLedger
from core.constitutional_engine.model import ActionRequest, Branch
from core.sovereignty.crown import provision_crown
from core.sovereignty.decree import RoyalDecree, sign_decree
from core.sovereignty.gateway import SovereignGateway, SovereigntyViolation
from core.sovereignty.kill_switch_source import (
    FAIL_CLOSED_LEVEL,
    KILL_SWITCH_INJECTION_MODE,
    KillSwitchLevelSource,
    LevelReading,
    resolve_reading,
)
from cryptography.hazmat.primitives import serialization


class _Fixed:
    def __init__(self, level: int, form: str = "constitutional") -> None:
        self.level = level
        self.form = form
        self.reads = 0

    def read(self) -> LevelReading:
        self.reads += 1
        return LevelReading(self.level, self.form)


class _Raises:
    def read(self) -> LevelReading:
        raise RuntimeError("المصدرُ معطوب")


class _Bad:
    def __init__(self, value: object) -> None:
        self.value = value

    def read(self) -> object:
        return type("R", (), {"level": self.value, "form": "constitutional"})()


@pytest.fixture
def gw(tmp_path) -> SovereignGateway:
    return SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(tmp_path / "ledger.jsonl")))


def _req(action: str, actor: Branch = Branch.EXECUTIVE, **kw) -> ActionRequest:
    return ActionRequest(actor=actor, action=action, target="w752", **kw)


# ── القراءةُ بغ1 ──────────────────────────────────────────────────────────


def test_mode_is_observe_only() -> None:
    assert KILL_SWITCH_INJECTION_MODE == "OBSERVE"


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        (None, (FAIL_CLOSED_LEVEL, "no_source")),
        (_Raises(), (FAIL_CLOSED_LEVEL, "error")),
        (_Bad(6), (FAIL_CLOSED_LEVEL, "unknown")),
        (_Bad(-1), (FAIL_CLOSED_LEVEL, "unknown")),
        (_Bad("4"), (FAIL_CLOSED_LEVEL, "unknown")),
        (_Bad(True), (FAIL_CLOSED_LEVEL, "unknown")),
        (_Fixed(3), (3, "constitutional")),
        (_Fixed(0), (0, "constitutional")),
    ],
)
def test_resolve_reading_g1(source, expected) -> None:
    r = resolve_reading(source)
    assert (r.level, r.form) == expected


def test_fixed_source_is_protocol() -> None:
    assert isinstance(_Fixed(1), KillSwitchLevelSource)


# ── المراقبةُ بلا منع: المسارُ التابع ───────────────────────────────────────


def test_subordinate_at_level4_allows_executes_and_observes(gw) -> None:
    gw.register_kill_switch_source(_Fixed(4))
    done: list[str] = []
    gw.execute(_req("create_task"), lambda: done.append("تم"))
    assert done == ["تم"], "المراقبةُ منعت — والقرارُ «بلا منع»"
    obs = gw.kill_switch_observations
    assert len(obs) == 1
    o = obs[0]
    assert (o.action, o.path, o.request_level, o.source_level, o.effective_level) == (
        "create_task",
        "subordinate",
        0,
        4,
        4,
    )
    assert o.verdict_decision == "ALLOW"
    assert "المستوى 4" in o.would_block_reason
    assert o.mode == "OBSERVE"


def test_subordinate_below_threshold_not_observed(gw) -> None:
    gw.register_kill_switch_source(_Fixed(3))
    gw.execute(_req("create_task"), lambda: None)
    assert gw.kill_switch_observations == ()


def test_level0_not_observed(gw) -> None:
    gw.register_kill_switch_source(_Fixed(0))
    gw.execute(_req("record_curriculum_step"), lambda: None)
    assert gw.kill_switch_observations == ()


def test_containment_never_observed(gw) -> None:
    gw.register_kill_switch_source(_Fixed(5))
    for action in ("run_health_check", "contain_agent", "release_agent", "graceful_shutdown", "create_backup"):
        gw.review(_req(action))
    assert gw.kill_switch_observations == ()


def test_request_level_already_blocking_is_denied_as_today_and_not_observed(gw) -> None:
    """طلبٌ يحملُ 4 بنفسِه ⇐ DENY كما اليوم — ممنوعٌ فعلًا فليسَ «ما كانَ سيُمنَع»."""
    gw.register_kill_switch_source(_Fixed(0))
    with pytest.raises(SovereigntyViolation):
        gw.execute(_req("create_task", kill_switch_level=4), lambda: None)
    assert gw.kill_switch_observations == ()


def test_effective_is_max_requester_cannot_lower(gw) -> None:
    """الأعلى: الطلبُ يحملُ 1 والمصدرُ 4 ⇐ الفعّالُ 4 (الطالبُ لا يُخفِّضُ)."""
    gw.register_kill_switch_source(_Fixed(4))
    gw.review(_req("create_task", kill_switch_level=1))
    (o,) = gw.kill_switch_observations
    assert (o.request_level, o.source_level, o.effective_level) == (1, 4, 4)


def test_effective_takes_request_when_higher(gw) -> None:
    """والعكسُ: الطلبُ يحملُ 2 والمصدرُ 0 ⇐ الفعّالُ 2 — `spawn_population` ممنوعٌ اليومَ بالطلبِ نفسِه فلا ملاحظة،
    و`spawn_agent` (≥3) لا يُمنَعُ عندَ 2 فلا ملاحظةَ أيضًا."""
    gw.register_kill_switch_source(_Fixed(0))
    gw.review(_req("spawn_agent", kill_switch_level=2))
    assert gw.kill_switch_observations == ()


def test_review_path_observes(gw) -> None:
    gw.register_kill_switch_source(_Fixed(1))
    verdict = gw.review(_req("record_curriculum_step"))
    assert verdict.allowed
    (o,) = gw.kill_switch_observations
    assert o.path == "review"


def test_no_source_reads_five_and_observes_without_blocking(gw) -> None:
    done: list[str] = []
    gw.execute(_req("spawn_agent"), lambda: done.append("تم"))
    assert done == ["تم"]
    (o,) = gw.kill_switch_observations
    assert (o.source_level, o.source_form) == (5, "no_source")


def test_source_error_reads_five_and_crossing_passes(gw) -> None:
    gw.register_kill_switch_source(_Raises())
    done: list[str] = []
    gw.execute(_req("create_task"), lambda: done.append("تم"))
    assert done == ["تم"]
    (o,) = gw.kill_switch_observations
    assert (o.source_level, o.source_form) == (5, "error")


def test_sink_failure_counted_and_crossing_passes(gw) -> None:
    def broken_sink(_o) -> None:
        raise RuntimeError("المُصرِّفُ معطوب")

    gw.register_kill_switch_source(_Fixed(4), broken_sink)
    done: list[str] = []
    gw.execute(_req("create_task"), lambda: done.append("تم"))
    assert done == ["تم"], "عطلُ المراقبةِ أسقطَ العبور"
    assert gw.kill_switch_observation_errors == 1


def test_sink_receives_observation(gw) -> None:
    got: list[object] = []
    gw.register_kill_switch_source(_Fixed(4), got.append)
    gw.execute(_req("activate_agent"), lambda: None)
    assert len(got) == 1 and got[0] is gw.kill_switch_observations[0]


def test_source_read_once_per_crossing_no_cache(gw) -> None:
    src = _Fixed(4)
    gw.register_kill_switch_source(src)
    gw.review(_req("create_task"))
    gw.review(_req("create_task"))
    assert src.reads == 2


def test_observation_does_not_write_extra_ledger_entries(tmp_path) -> None:
    """الملاحظةُ لا تكتبُ في السجلِّ الدستوريّ: عددُ القيودِ بمصدرٍ وبغيرِه سواء."""
    a = SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(tmp_path / "a.jsonl")))
    b = SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(tmp_path / "b.jsonl")))
    b.register_kill_switch_source(_Fixed(5))
    for g in (a, b):
        g.execute(_req("create_task"), lambda: None)
    assert len(a.engine.ledger) == len(b.engine.ledger)
    assert len(b.kill_switch_observations) == 1


# ── المسارُ الملكيُّ: مُلاحَظٌ لا ممنوع ──────────────────────────────────────


@pytest.fixture
def crown(monkeypatch, tmp_path):
    key_path = tmp_path / "crown.pem"
    registry = tmp_path / "CROWN_KEYS.json"
    provision_crown(key_path, registry_path=registry)
    monkeypatch.setattr(crown_mod, "CROWN_KEYS_PATH", registry)
    priv = serialization.load_pem_private_key(key_path.read_bytes(), password=None)
    return priv, crown_mod.load_crown().key_id


def test_sovereign_path_observed_not_blocked(crown, gw) -> None:
    key, key_id = crown
    decree = sign_decree(
        RoyalDecree(
            decree_id="w752-royal",
            action="self_modify",
            issued_at=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            key_id=key_id,
        ),
        key,
    )
    gw.register_kill_switch_source(_Fixed(5))
    done: list[str] = []
    gw.execute(ActionRequest(actor=Branch.ROYAL, action="self_modify", royal_decree=decree), lambda: done.append("تم"))
    assert done == ["تم"]
    (o,) = gw.kill_switch_observations
    assert o.path == "sovereign" and o.effective_level == 5


# ── سقفُ الذاكرة (W-779 · § 5 من `docs/audit/WI085_MONITORING_EXIT_CRITERION.md`) ──────────


def test_cap_constant_is_design_value(gw) -> None:
    assert gateway_mod.KILL_SWITCH_OBSERVATIONS_CAP == 10_000
    assert gw._kill_switch_observations.maxlen == 10_000
    assert gw.kill_switch_observations_total == 0
    assert gw.kill_switch_observations_dropped == 0


@pytest.mark.parametrize("cap", [1, 7])
def test_cap_plus_five_bounds_memory_counts_dropped_and_exports_all(
    monkeypatch, tmp_path, cap
) -> None:
    """‏CAP+5 ⇒ الطولُ CAP · المُسقَطُ 5 · الكلُّ CAP+5 · المُصرِّفُ CAP+5 — والعبورُ كلُّه نافذ."""
    monkeypatch.setattr(gateway_mod, "KILL_SWITCH_OBSERVATIONS_CAP", cap)
    ledger = ConstitutionalLedger(tmp_path / "cap.jsonl")
    g = SovereignGateway(ConstitutionalEngine(ledger=ledger))
    exported: list[object] = []
    g.register_kill_switch_source(_Fixed(4), exported.append)
    done: list[int] = []
    for i in range(cap + 5):
        g.execute(_req("create_task"), lambda i=i: done.append(i))
    assert done == list(range(cap + 5)), "السقفُ منعَ عبورًا — والقرارُ «بلا منع»"
    assert len(g.kill_switch_observations) == cap
    assert g.kill_switch_observations_dropped == 5
    assert g.kill_switch_observations_total == cap + 5
    # المُصرِّفُ لكلِّ ملاحظة: السقفُ يحدُّ الذاكرةَ لا الدليل
    assert len(exported) == cap + 5
    # المحفوظُ هو الأحدث: آخرُ CAP ملاحظةً مُصرَّفةً بعينِها
    assert list(g.kill_switch_observations) == exported[-cap:]
    assert g.kill_switch_observation_errors == 0


def test_below_cap_nothing_dropped(gw) -> None:
    gw.register_kill_switch_source(_Fixed(4))
    for _ in range(3):
        gw.review(_req("create_task"))
    assert len(gw.kill_switch_observations) == 3
    assert gw.kill_switch_observations_total == 3
    assert gw.kill_switch_observations_dropped == 0


def test_unobserved_crossings_not_counted_in_total(gw) -> None:
    gw.register_kill_switch_source(_Fixed(0))
    gw.review(_req("create_task"))
    assert gw.kill_switch_observations_total == 0
    assert gw.kill_switch_observations_dropped == 0
