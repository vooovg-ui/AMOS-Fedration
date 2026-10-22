"""
الهدف: قياسُ موضعِ فجوةِ التعويضِ (Q-70 · التوجيهُ 18 § 2) على المسارِ الإنتاجيِّ — بلا تغييرٍ في الشِّفرة
النطاق: docs/audit/evidence/W-601 — مسبارٌ يُنسَخُ مؤقّتًا إلى federal/executive/services/tests/ ثمَّ يُحذَف (سابقةُ مسبارِ مقعدِ claude في W-599) ولا يُلتزَمُ هناك
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — قيدُ W-601
تاريخ الإنشاء: 2026-10-22

السيناريو الواحدُ لكلِّ سطحٍ: يُسقَطُ تثبيتُ النجاحِ (`IdempotencyLedger.mark_succeeded`)
بعدَ أن يلتزمَ المُطبِّقُ صفوفَه، ثمَّ يُنادى السطحُ بنداءِ الخدمةِ الإنتاجيِّ وحدَه
(لا تعويضَ يدويًّا). ويُسجَّلُ: الاستثناءُ الناتجُ · حالةُ الصفوفِ · هل شُغِّلَ المُعوِّضُ
· حالةُ سجلِّ الذرّيّةِ · ونتيجةُ إعادةِ المحاولةِ بعدَ رفعِ الإسقاطِ.

التشغيل (من جذرِ المستودع):
  cp docs/audit/evidence/W-601/test_w601_gap_probe.py federal/executive/services/tests/ && \
  .venv/bin/pytest federal/executive/services/tests/test_w601_gap_probe.py -s -q -p no:cacheprovider ; \
  rm federal/executive/services/tests/test_w601_gap_probe.py
"""

from __future__ import annotations

from typing import Any

import pytest

from amos_federation.services.executive_core import agent_identity as agent_identity_module
from amos_federation.services.executive_core.agent_identity import (
    get_identity,
    register_identity,
)
from amos_federation.services.executive_core.sovereignty_bridge import ConstitutionalAuthorizer

# مُثبَّتاتُ فحوصِ J1 نفسُها — لا بيئةَ موازية
from tests.test_wi105_issue_ruling_sovereign import (  # noqa: F401 — مُثبَّتاتٌ تُحقَنُ بالاسم
    _fresh_state,
    _prepared_case,
    _session,
    crown,
    judiciary,
    national,
    registry,
    rulings_module,
)
from tests.test_wi105_issue_ruling_sovereign import (  # noqa: E402
    CaseProceedingModel,
    LegalCaseModel,
    RulingModel,
)


def _spy_compensators(monkeypatch: pytest.MonkeyPatch, calls: list[str]) -> None:
    """جاسوسٌ على `Compensator.apply`: هل نادى أيُّ مسارٍ المُعوِّضَ؟ — لا يغيّرُ سلوكَه."""
    from core.sovereignty import compensation as comp

    original_compensate = comp.CompensationGuard.compensate

    def spy_compensate(self: Any, **kwargs: Any) -> Any:
        calls.append("CompensationGuard.compensate")
        return original_compensate(self, **kwargs)

    monkeypatch.setattr(comp.CompensationGuard, "compensate", spy_compensate)


def _drop_settle(monkeypatch: pytest.MonkeyPatch, ledger: Any) -> None:
    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("تثبيتُ النجاحِ مُسقَطٌ — مسبارُ W-601")

    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)


def _status_of(ledger: Any, scope: str, value: str) -> str:
    from core.sovereignty.idempotency import IdempotencyKey

    rec = ledger.get(IdempotencyKey(scope=scope, value=value)) if hasattr(ledger, "get") else None
    return getattr(getattr(rec, "status", None), "value", str(rec))


def test_probe_a_issue_ruling(registry, national, judiciary, crown, monkeypatch) -> None:  # noqa: ANN001
    print("\n## (أ) issue_ruling — J1 · WI-105")
    _b, case_id, judge_ctx = _prepared_case(registry, national, judiciary, crown, "w601a")
    s = _session()
    try:
        before = s.get(LegalCaseModel, case_id).status
    finally:
        s.close()
    print(f"حالةُ القضيّةِ قبلَ النداء: {before}")

    calls: list[str] = []
    _spy_compensators(monkeypatch, calls)
    ledger = rulings_module._judiciary_authorizer().boundary.idempotency_ledger
    original = type(ledger).mark_succeeded
    _drop_settle(monkeypatch, ledger)

    exc_repr = "لا استثناء"
    try:
        judiciary.issue_ruling(
            context=judge_ctx, case_id=case_id, stage="FIRST_INSTANCE",
            decision="GRANTED", disposition="مسبارُ W-601",
        )
    except Exception as exc:  # noqa: BLE001 — يُقاسُ لا يُبتلَع
        exc_repr = f"{type(exc).__module__}.{type(exc).__name__}: {exc}"
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    s = _session()
    try:
        rulings = s.query(RulingModel).filter(RulingModel.case_id == case_id).count()
        procs = (
            s.query(CaseProceedingModel)
            .filter(CaseProceedingModel.case_id == case_id,
                    CaseProceedingModel.proceeding_type == "RULING")
            .count()
        )
        after = s.get(LegalCaseModel, case_id).status
    finally:
        s.close()
    print(f"الاستثناءُ الناتج: {exc_repr}")
    print(f"صفوفُ الحكمِ: {rulings} · إجراءاتُ RULING: {procs} · حالةُ القضيّة: {after}")
    print(f"هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: {len(calls)}")
    print(f"سجلُّ الذرّيّة: {_status_of(ledger, 'judiciary.ruling.issue', f'{case_id}:FIRST_INSTANCE:g0')}")

    retry = "لا استثناء"
    try:
        judiciary.issue_ruling(
            context=judge_ctx, case_id=case_id, stage="FIRST_INSTANCE",
            decision="GRANTED", disposition="مسبارُ W-601 — إعادة",
        )
    except Exception as exc:  # noqa: BLE001
        retry = f"{type(exc).__module__}.{type(exc).__name__}"
    print(f"إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: {retry}")


def test_probe_b_register_identity(monkeypatch) -> None:  # noqa: ANN001
    print("\n## (ب) register_identity — WI-082")
    agent_id = "w601-probe-agent"
    agent_identity_module._delete_identity_row(agent_id)
    authorizer = ConstitutionalAuthorizer(actor=agent_identity_module.AGENT_IDENTITY_ACTOR)
    calls: list[str] = []
    _spy_compensators(monkeypatch, calls)
    ledger = authorizer.boundary.idempotency_ledger
    original = type(ledger).mark_succeeded
    _drop_settle(monkeypatch, ledger)

    exc_repr = "لا استثناء"
    try:
        register_identity(agent_id, "مسبار", "probe", authorizer=authorizer)
    except Exception as exc:  # noqa: BLE001
        exc_repr = f"{type(exc).__module__}.{type(exc).__name__}: {exc}"
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    row = get_identity(agent_id)
    print(f"الاستثناءُ الناتج: {exc_repr}")
    print(f"صفُّ الهويّة: {'موجود' if row is not None else 'غائب'}")
    print(f"هل شُغِّلَ المُعوِّض؟ نداءاتُ CompensationGuard.compensate: {len(calls)}")
    print(f"سجلُّ الذرّيّة: {_status_of(ledger, agent_identity_module.IDENTITY_SPAWN_SCOPE, agent_id)}")

    retry = "لا استثناء"
    try:
        register_identity(agent_id, "مسبار", "probe", authorizer=authorizer)
    except Exception as exc:  # noqa: BLE001
        retry = f"{type(exc).__module__}.{type(exc).__name__}"
    print(f"إعادةُ المحاولةِ بعدَ رفعِ الإسقاط: {retry}")
    agent_identity_module._delete_identity_row(agent_id)
