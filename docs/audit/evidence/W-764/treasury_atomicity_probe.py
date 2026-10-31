"""مسبارُ ذرّيّةِ مُطبِّقاتِ الخزانةِ الستّة (W-764 · التوجيهُ 36 § 1 القرار 2 · DISC-148).

الهدف: الإجابةُ بالقياسِ لا بالقراءة عن سؤالِ المالك «هل هي ذرّيّةٌ فعلًا (معاملةُ قاعدةٍ واحدة)؟»:
       يُحقَنُ فشلٌ واحدٌ في `record_domain_trace` — وهي تُنادى في كلِّ `_apply` **بعدَ** `session.commit()` —
       ثمَّ يُقاسُ: هل بقيَ الصفُّ/المالُ؟ بأيِّ حالةٍ وُسِمَت العمليّةُ في سجلِّ الذرّيّة؟ وماذا تفعلُ
       إعادةُ النداءِ نفسِه بحرفِه؟
النطاق: `StateTreasury` الستُّ (establish_treasury · open_account · create_budget · allocate · post_funding ·
        disburse) على SQLite الاختبار · قراءةٌ وحقنٌ مؤقّتٌ بـmonkeypatch · لا تعديلَ لشِفرةِ الإنتاج.
المالك: Perplexity Computer (قيدُ W-764 · البندُ WI-125).
التشغيل (من federal/executive/services):
    ../../../.venv/bin/python -m pytest -q -s -p no:cacheprovider -p tests.conftest \
        ../../../docs/audit/evidence/W-764/treasury_atomicity_probe.py
"""

from __future__ import annotations

import json
import uuid
from pathlib import Path
from typing import Any, Callable

import pytest

from amos_federation.common.database import get_session_factory
from amos_federation.services.state_registry.service import get_state_registry
from amos_federation.services.state_treasury import service as treasury_module
from amos_federation.services.state_treasury.models import (
    AccountModel,
    AllocationModel,
    BudgetModel,
    TransactionModel,
    TreasuryModel,
)
from amos_federation.services.state_treasury.service import StateTreasury
from tests.test_r7b_state_treasury import (  # noqa: F401 — المُثبِّتُ التلقائيُّ نفسُه
    _allocate,
    _code,
    _context,
    _fiscal,
    _fresh_state,
)
from tests.test_w755_m1_treasury_single_crossing import Factory

OUT: list[str] = []


def _count(model: Any) -> int:
    s = get_session_factory()()
    try:
        return s.query(model).count()
    finally:
        s.close()


def _ledger_statuses(tmp_path: Path) -> list[str]:
    """آخرُ حالةٍ لكلِّ مفتاحٍ في سجلّاتِ الذرّيّة (JSON أو JSONL — يُقرأُ سطرًا سطرًا)."""
    latest: dict[str, str] = {}
    for f in sorted(tmp_path.glob("M1-*-IDEM.json*")):
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise AssertionError(f"سطرٌ غيرُ مقروءٍ في {f.name}: {exc}") from exc
            stack = [item]
            while stack:
                cur = stack.pop()
                if isinstance(cur, dict):
                    if "status" in cur and "value" in cur:
                        latest[f"{cur.get('scope')}:{cur['value']}"] = str(
                            cur["status"]
                        )
                    stack.extend(cur.values())
                elif isinstance(cur, list):
                    stack.extend(cur)
    return [latest[k] for k in sorted(latest)]


def _new_statuses(before: list[str], after: list[str]) -> list[str]:
    """الحالاتُ التي ظهرَت أو تغيّرَت بعدَ نقطةِ القياس (عدٌّ لا هويّة — يكفي لعمليّةٍ واحدة)."""
    rest = list(before)
    out = []
    for s in after:
        if s in rest:
            rest.remove(s)
        else:
            out.append(s)
    return out


def _balance(treasury: StateTreasury, crown: Any, fiscal: Any) -> str:
    return str(
        treasury.account_balance(
            context=crown,
            treasury_code=fiscal.treasury["code"],
            account_code=fiscal.cash["code"],
        )["balance"]
    )


class FailTraceOnce:
    """يرفعُ في النداءِ الأوّلِ بعدَ تسليحِه فقط — ما بعدَ commit المُطبِّق."""

    def __init__(self, real: Callable[..., Any]) -> None:
        self.real = real
        self.armed = False
        self.fired = 0

    def __call__(self, *a: Any, **k: Any) -> Any:
        if self.armed:
            self.armed = False
            self.fired += 1
            raise RuntimeError("حقنُ W-764: فشلُ التتبّعِ بعدَ الالتزام")
        return self.real(*a, **k)


def _attempt(fn: Callable[[], Any]) -> str:
    try:
        r = fn()
        return "OK" + (
            " idempotent" if isinstance(r, dict) and r.get("idempotent") else ""
        )
    except Exception as exc:  # noqa: BLE001 — القياسُ يسجّلُ النوعَ لا يبتلعُه
        return type(exc).__name__


@pytest.mark.parametrize(
    "op",
    [
        "establish_treasury",
        "open_account",
        "create_budget",
        "allocate",
        "post_funding",
        "disburse",
        "post_funding/بلا-مفتاح",
        "disburse/بلا-مفتاح",
    ],
)
def test_probe(op: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    crown = _context("king")
    registry = get_state_registry()
    factory = Factory(tmp_path)
    treasury = StateTreasury(money_authorizer_factory=factory)
    fiscal = _fiscal(treasury, registry, crown)
    allocation = (
        _allocate(treasury, crown, fiscal) if op.startswith("disburse") else None
    )
    keyless = op.endswith("/بلا-مفتاح")
    key = None if keyless else f"W764-{uuid.uuid4().hex[:6]}"
    calls: dict[str, tuple[Callable[[], Any], Any]] = {
        "establish_treasury": (
            lambda c=_code("TRS"): treasury.establish_treasury(
                context=crown, code=c, name="مسبار", currency="SAR"
            ),
            TreasuryModel,
        ),
        "open_account": (
            lambda c=_code("ACC"): treasury.open_account(
                context=crown,
                treasury_code=fiscal.treasury["code"],
                code=c,
                name="مسبار",
                kind="cash",
            ),
            AccountModel,
        ),
        "create_budget": (
            lambda c=_code("BUD"): treasury.create_budget(
                context=crown,
                treasury_code=fiscal.treasury["code"],
                institution_code=fiscal.institution["code"],
                code=c,
                period="2026",
                limit_amount="10.0000",
            ),
            BudgetModel,
        ),
        "allocate": (
            lambda: _allocate(treasury, crown, fiscal, amount="100.0000"),
            AllocationModel,
        ),
        "post_funding": (
            lambda: treasury.post_funding(
                context=crown,
                treasury_code=fiscal.treasury["code"],
                cash_account_code=fiscal.cash["code"],
                revenue_account_code=fiscal.revenue["code"],
                amount="100.0000",
                purpose="مسبار",
                official_id=fiscal.official["id"],
                idempotency_key=key,
            ),
            TransactionModel,
        ),
        "disburse": (
            lambda: treasury.disburse(
                context=crown,
                allocation_id=allocation["id"],
                expense_account_code=fiscal.expense["code"],
                amount="100.0000",
                purpose="مسبار",
                official_id=fiscal.official["id"],
                idempotency_key=key,
            ),
            TransactionModel,
        ),
    }
    calls["post_funding/بلا-مفتاح"] = calls["post_funding"]
    calls["disburse/بلا-مفتاح"] = calls["disburse"]
    call, model = calls[op]
    injector = FailTraceOnce(treasury_module.record_domain_trace)
    monkeypatch.setattr(treasury_module, "record_domain_trace", injector)
    rows0, bal0 = _count(model), _balance(treasury, crown, fiscal)
    led_before = _ledger_statuses(tmp_path)
    injector.armed = True
    first = _attempt(call)
    rows1, bal1 = _count(model), _balance(treasury, crown, fiscal)
    status1 = _new_statuses(led_before, _ledger_statuses(tmp_path))
    second = _attempt(call)
    rows2, bal2 = _count(model), _balance(treasury, crown, fiscal)
    status2 = _new_statuses(led_before, _ledger_statuses(tmp_path))
    atomic = (
        "ذرّيٌّ (لا أثرَ بعدَ الفشل)"
        if rows1 == rows0 and bal1 == bal0
        else "**غيرُ ذرّيّ** (أثرٌ باقٍ بعدَ الفشل)"
    )
    OUT.append(
        f"{op}: حُقِنَ={injector.fired} · محاولة1={first} · صفوف {model.__tablename__} {rows0}→{rows1} · "
        f"رصيدُ النقد {bal0}→{bal1} · سجلُّ الذرّيّة {status1} · {atomic} || "
        f"إعادةٌ بالنداءِ نفسِه: {second} · صفوف→{rows2} · الرصيد→{bal2} · سجلُّ الذرّيّة {status2}"
    )
    assert injector.fired == 1


def teardown_module() -> None:
    print("\n=== مسبارُ ذرّيّةِ مُطبِّقاتِ الخزانةِ الستّة (W-764) ===")
    for line in OUT:
        print(line)
