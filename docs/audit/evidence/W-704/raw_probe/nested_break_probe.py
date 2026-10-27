"""مسبارُ المقعدِ kimi_k3 (WI-115 · جولةُ W-701) — كسرُ الكاشفِ النافيُّ للتعشيشِ.

يحاولُ المسبارُ استدعاءً سياديًّا داخلَ عبورٍ نشطٍ بفعلٍ غيرُ مستثنًى (`credit_account`
على نمطِ فحوصِ الكاشفِ نفسِها) فيتوقَّعُ أنْ يُرمى `NestedSovereignCallError` قبلَ
أيِّ `decide` وأيِّ قيدٍ في دفترِ الذرّيّةِ — هذا مسبارٌ من عندِ المقعدِ لا من أوامرِ (ج)
(البروتوكولُ § 4.9).
"""

الهدف: مسبارُ المنسِّقِ — كسرُ كاشفِ التعشيشِ عندَ الحدِّ (WI-115) بمحاولةِ عبورٍ معشّقٍ (جولةُ W-704).


from __future__ import annotations

from pathlib import Path
import sys
import tempfile

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "repo"))
sys.path.insert(0, str(BASE / "repo" / "federal" / "executive" / "services" / "src"))

from cryptography.hazmat.primitives.asymmetric import ed25519  # noqa: E402

from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.ledger import ConstitutionalLedger  # noqa: E402
from core.sovereignty.enforcement_boundary import (  # noqa: E402
    NestedSovereignCallError,
    SovereignExecutionBoundary,
    _active_crossing,
)
from core.sovereignty.gateway import SovereignGateway  # noqa: E402
from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger  # noqa: E402
from core.sovereignty.outbox import OutboxLedger, SovereignOutbox  # noqa: E402
from core.constitutional_engine.model import ActionRequest, Branch  # noqa: E402


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="probe_wi115_kimi_"))

    gateway = SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(tmp / "l.jsonl")))
    idempotency = IdempotencyLedger(tmp / "IDEMPOTENCY.json")
    outbox = SovereignOutbox(
        ledger=OutboxLedger(tmp / "OUTBOX.json"),
        verifying_key=ed25519.Ed25519PublicKey.from_public_bytes(
            bytes.fromhex(gateway.verifying_key_hex)
        ),
    )
    boundary = SovereignExecutionBoundary(
        gateway=gateway,
        idempotency_ledger=idempotency,
        outbox=outbox,
    )

    state = {"treasury/account-A": "1000", "gov/case-A/row": "NONE"}

    # فعلٌ سياديٌّ غيرُ مستثنًى (credit_account) داخلَ إطارِ gov.case.open النشطِ —
    # يُتوقَّعُ رفضُهُ قبلَ أيِّ decide وأيِّ قيدٍ.
    # مسبارٌ مباشرٌ: الإطارُ النشطُ يُثبَتُ بالمدخلِ العموميِّ (`_active_crossing`)
    # لا بعبورٍ خارجيٍّ — فالكاشفُ يُقاسُ على المنعِ قبلَ أيِّ حارسٍ وأيِّ قيدٍ.
    outer_token = None
    try:
        outer_token = _active_crossing.set(("gov.case.open", "gov/case-A"))

        boundary.execute(
            ActionRequest(actor=Branch.EXECUTIVE, action="credit_account", target="treasury/account-A", channel="official"),
            declared_effects=(),
            planner=lambda _: (),
            applier=lambda e: state.__setitem__(e.resource, "MUTATED"),
            operation_key=IdempotencyKey(scope="probe", value="inner"),
        )
    except NestedSovereignCallError:
        print("PASS: NestedSovereignCallError raised for non-exempt 'credit_account' inside active crossing")
    else:
        print("FAIL: nesting silently allowed — no NestedSovereignCallError raised")
    finally:
        if outer_token is not None:
            _active_crossing.reset(outer_token)

    # (3) السياقُ مستعادٌ — لا إطارَ معلَّقًا.
    if _active_crossing.get() is None:
        print("PASS: context restored (no dangling crossing frame)")
    else:
        print("FAIL: context NOT restored — dangling frame")


if __name__ == "__main__":
    main()
