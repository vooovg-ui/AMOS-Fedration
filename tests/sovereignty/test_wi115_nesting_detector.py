"""الهدف: قياسُ كاشفِ التعشيشِ عندَ الحدِّ السياديّ (WI-115 · Q-9 الخيارُ 4).

النطاق: `core/sovereignty/enforcement_boundary.py` — كاشفُ العبورِ داخلَ
العبورِ، لا القواعدِ الدستوريةَ ولا التطبيقِ. سندُ التصميمِ: وثيقةُ
`docs/audit/Q9_NESTING_DETECTOR_DESIGN.md` (W-665 · المالكُ أمرَ بالخيارِ 4).

الدعوى المُقاسة: عبورٌ سياديٌّ داخلَ عبورٍ نشطٍ **يُرفَضُ قبلَ أيِّ حارسٍ وأيِّ
`decide` وأيِّ قيدٍ في دفترِ الذرّيّة** — فلا إذنَ ولا حجزَ ولا أثرَ للرفضِ.
والاستثناءُ المسجَّلُ الوحيدُ أزواجٌ (خارجيٌّ، داخليٌّ) باسمِ `open_case`
وحْده (`gov.case.open` → `task.submit` و`task.cancel`)، لا أسماءٌ مفردة،
فلا يصيرُ `open_case` بابًا لأيِّ عبورٍ آخرَ داخلَه.

والقاعدةُ 12 تمنعُ اعتبارَ وجودِ الملفِّ دليلًا: فالمنعُ يُثبَتُ هنا بأنّ
`decide` لم يُستدعَ للداخلِ وبأنَّ الدفترَ لا يحملُ مفتاحَه وبأنَّ الحالةَ
لم تتغيّر، لا بأنَّ استثناءً ارتفعَ فحسب.

سجلُّ التحولات: فشلُ الفحصِ قبلَ الإصلاحِ ثمَّ نجاحُه بعده لا يُقاسُ هنا —
هذا كاشفٌ جديدٌ لا إصلاحٌ؛ والمقيسُ رفضُ التعشيشِ وإبقاءُ الاستثناءِ
المسجَّلِ يعملُ واستعادةُ السياقِ بعدَ كلِّ مسارٍ (نجاحٌ ورفضٌ واستثناءٌ).
"""

from __future__ import annotations

from pathlib import Path

import pytest
from cryptography.hazmat.primitives.asymmetric import ed25519

from core.constitutional_engine.engine import ConstitutionalEngine
from core.constitutional_engine.ledger import ConstitutionalLedger
from core.constitutional_engine.model import ActionRequest, Branch
from core.sovereignty.compensation import Compensator
from core.sovereignty.contract import EffectKind, SovereignEffect
from core.sovereignty.enforcement import ConsumedPermitLedger
from core.sovereignty.enforcement_boundary import (
    NestedSovereignCallError,
    SovereignExecutionBoundary,
    _active_crossing,
)
from core.sovereignty.gateway import SovereignGateway
from core.sovereignty.idempotency import IdempotencyError, IdempotencyKey, IdempotencyLedger
from core.sovereignty.outbox import OutboxLedger, SovereignOutbox

# ═══════════════════════════════════════════════════════════════════════════
# تجهيزات — حالةٌ حقيقيّةٌ وسجلّاتٌ على القرص، على نمطِ ديوانِ التدقيقِ
# ═══════════════════════════════════════════════════════════════════════════


@pytest.fixture()
def حالةُ_الدولة() -> dict[str, str]:
    return {
        "treasury/account-A": "1000",
        "gov/case-A/row": "NONE",
        "tasks/task-A/row": "NONE",
    }


@pytest.fixture()
def بوابة(tmp_path: Path) -> SovereignGateway:
    return SovereignGateway(ConstitutionalEngine(ledger=ConstitutionalLedger(tmp_path / "l.jsonl")))


@pytest.fixture()
def سجلُّ_الذرّيّة(tmp_path: Path) -> IdempotencyLedger:
    return IdempotencyLedger(tmp_path / "IDEMPOTENCY.json")


@pytest.fixture()
def صادر(tmp_path: Path, بوابة: SovereignGateway) -> SovereignOutbox:
    return SovereignOutbox(
        ledger=OutboxLedger(tmp_path / "OUTBOX.json"),
        verifying_key=ed25519.Ed25519PublicKey.from_public_bytes(
            bytes.fromhex(بوابة.verifying_key_hex)
        ),
    )


@pytest.fixture()
def حدّ(
    tmp_path: Path,
    بوابة: SovereignGateway,
    سجلُّ_الذرّيّة: IdempotencyLedger,
    صادر: SovereignOutbox,
) -> SovereignExecutionBoundary:
    return SovereignExecutionBoundary(
        gateway=بوابة,
        idempotency_ledger=سجلُّ_الذرّيّة,
        outbox=صادر,
        consumed_permits=ConsumedPermitLedger(tmp_path / "CONSUMED.json"),
    )


def _طلب(
    action: str,
    target: str,
    actor: Branch = Branch.EXECUTIVE,
) -> ActionRequest:
    return ActionRequest(actor=actor, action=action, target=target, channel="official")


def _أثر(resource: str) -> SovereignEffect:
    """أثرٌ داخلَ نطاقِ هدفِهِ — فالعقدُ يرفضُ الأثرَ خارجَ الهدفِ المأذونِ."""
    return SovereignEffect(kind=EffectKind.WRITE, resource=resource, detail="قياس")


def _مفتاح(value: str) -> IdempotencyKey:
    return IdempotencyKey(scope="treasury", value=value)


def _معوّض(state: dict[str, str], effect: SovereignEffect) -> Compensator:
    return Compensator(
        effect_signature=effect.signature,
        apply=lambda: state.update({effect.resource: state.get(f"{effect.resource}#أصل", "1000")}),
        description="إرجاعُ القيمةِ الأصليّة",
    )


def _تنفيذٌ_كامل(
    حدّ: SovereignExecutionBoundary,
    action: str,
    key: str,
    state: dict[str, str],
) -> None:
    """عبورٌ واحدٌ كاملُ المسارِ — لا يُلمسُ فيه أيُّ تعشيشٍ."""
    أثر = _أثر(f"gov/case-{key}")
    حدّ.execute(
        _طلب(action=action, target=f"gov/case-{key}"),
        declared_effects=(أثر,),
        planner=lambda _: (أثر,),
        applier=lambda effect: state.__setitem__(effect.resource, "MUTATED"),
        operation_key=_مفتاح(key),
        compensators=(_معوّض(state, أثر),),
    )


# ═══════════════════════════════════════════════════════════════════════════
# 1 — التعشيشُ غيرُ المستثنى يُرفَضُ قبلَ decide وقبلَ أيِّ قيدٍ
# ═══════════════════════════════════════════════════════════════════════════


def test_التعشيشغيرالمستثنىيرفضقبلأيحارسوقبلأيإذن(
    حدّ: SovereignExecutionBoundary,
    بوابة: SovereignGateway,
    سجلُّ_الذرّيّة: IdempotencyLedger,
    حالةُ_الدولة: dict[str, str],
) -> None:
    """عبورٌ داخلَ عبورٍ نشطٍ بفعلٍ غيرِ مستثنًى يُرفَضُ — فلا `decide` ولا قيدَ ولا أثرَ.

    والدليلُ مقيسٌ لا مُفترَضٌ: سجلُّ البوابةِ يحملُ حكمَ الخارجيِّ وحدَه،
    ودفترُ الذرّيّةِ لا يعرفُ مفتاحَ الداخلِ، والحالةُ لم يمسَّها إلا الخارجيُّ.
    (وهذا الفحصُ نفسُه يقتلُ طفرةَ حذفِ الفحصِ عندَ دخولِ execute.)
    """
    مفتاح_الخارجي = _مفتاح("outer-1")
    مفتاح_الداخل = _مفتاح("inner-1")
    أثر_الخارجي = _أثر("gov/case-A/row")
    أثر_الداخل = _أثر("treasury/account-A")

    def مطبِّقٌ_يعشِّش(effect: SovereignEffect) -> None:
        with pytest.raises(NestedSovereignCallError):
            حدّ.execute(
                _طلب(action="credit_account", target="treasury/account-A"),
                declared_effects=(أثر_الداخل,),
                planner=lambda _: (أثر_الداخل,),
                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                operation_key=مفتاح_الداخل,
                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
            )
        حالةُ_الدولة[effect.resource] = "MUTATED"

    حصيلة = حدّ.execute(
        _طلب(action="gov.case.open", target="gov/case-A"),
        declared_effects=(أثر_الخارجي,),
        planner=lambda _: (أثر_الخارجي,),
        applier=مطبِّقٌ_يعشِّش,
        operation_key=مفتاح_الخارجي,
        compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
    )
    assert حصيلة.is_replay is False

    # الرفضُ صريحٌ وبالصنفِ المُعلَنِ: `pytest.raises` أعلاه ضمنَ المطبِّقِ
    # (لا إذنَ للداخلِ: سجلُّ البوابةِ لا يحملُ أيَّ حكمٍ بفعلِ الداخلِ (لكلِّ عبورٍ حكمانِ:
    # قرارٌ وإتمامٌ — فالعَدُّ بفعلِ الطلبِ لا بعددِ السطورِ)
    قرارات_الداخل = [r for r in بوابة.records if r.action == "credit_account"]
    assert قرارات_الداخل == [], "دخلَ الداخلُ إلى decide — الكاشفُ فُتحَ."
    # ولا قيدَ للداخلِ في دفترِ الذرّيّةِ
    assert سجلُّ_الذرّيّة.get(مفتاح_الداخل) is None, "قُيِّدَ الداخلُ في الدفترِ قبلَ الرفضِ."
    # ولا أثرَ للداخلِ: الحالةُ مسَّها الخارجيُّ وحدَه
    assert حالةُ_الدولة["gov/case-A/row"] == "MUTATED"
    assert حالةُ_الدولة["treasury/account-A"] == "1000"


# ═══════════════════════════════════════════════════════════════════════════
# 2 — الزوجُ المسجَّلُ وحدَه يعبرُ، ولا يصيرُ open_case بابًا لغيرِه
# ═══════════════════════════════════════════════════════════════════════════


def test_الزوجالمسجليعبركاملالمسار(
    حدّ: SovereignExecutionBoundary,
    بوابة: SovereignGateway,
    سجلُّ_الذرّيّة: IdempotencyLedger,
    حالةُ_الدولة: dict[str, str],
) -> None:
    """`gov.case.open` → `task.submit`: الزوجُ المسجَّلُ يعبرُ كاملَ المسارِ — إذنانِ وقيدانِ."""
    مفتاح_الخارجي = _مفتاح("outer-2")
    مفتاح_الداخل = _مفتاح("inner-2")
    أثر_الخارجي = _أثر("gov/case-A/row")
    أثر_الداخل = _أثر("tasks/task-A/row")

    def مطبِّقٌ_مستثنًى(effect: SovereignEffect) -> None:
        حصيلة_الداخل = حدّ.execute(
            _طلب(action="task.submit", target="tasks/task-A"),
            declared_effects=(أثر_الداخل,),
            planner=lambda _: (أثر_الداخل,),
            applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
            operation_key=مفتاح_الداخل,
            compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
        )
        assert حصيلة_الداخل.is_replay is False
        حالةُ_الدولة[effect.resource] = "MUTATED"

    حدّ.execute(
        _طلب(action="gov.case.open", target="gov/case-A"),
        declared_effects=(أثر_الخارجي,),
        planner=lambda _: (أثر_الخارجي,),
        applier=مطبِّقٌ_مستثنًى,
        operation_key=مفتاح_الخارجي,
        compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
    )
    قرارات_الداخل = [r for r in بوابة.records if r.action == "task.submit"]
    assert len(قرارات_الداخل) == 2  # حكمٌ وإتمامٌ للعبورِ الداخليِّ المستثنَى
    assert سجلُّ_الذرّيّة.get(مفتاح_الداخل) is not None
    assert حالةُ_الدولة["tasks/task-A/row"] == "MUTATED"


def test_فتحالقضيةليسبابالكلعبورغيرالمستثن(
    حدّ: SovereignExecutionBoundary,
    حالةُ_الدولة: dict[str, str],
) -> None:
    """طاردُ طفرةِ توسيعِ الاستثناءِ إلى اسمٍ مفردٍ: `gov.case.open` خارجيٌّ لا يعفي غيرَ زوجِه.

    لو اتُّسِعَ الاستثناءُ إلى اسمِ الفعلِ الخارجيِّ وحدَه لَعبرَ `credit_account`
    داخلَ إطارِ `open_case` — وهذا الفحصُ يقتلُ تلك الطفرةَ.
    """
    أثر_الخارجي = _أثر("gov/case-A/row")
    أثر_الداخل = _أثر("treasury/account-A")

    def مطبِّقٌ_غيرُ_مستثنًى(effect: SovereignEffect) -> None:
        with pytest.raises(NestedSovereignCallError):
            حدّ.execute(
                _طلب(action="credit_account", target="treasury/account-A"),
                declared_effects=(أثر_الداخل,),
                planner=lambda _: (أثر_الداخل,),
                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                operation_key=_مفتاح("inner-3"),
                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
            )
        حالةُ_الدولة[effect.resource] = "MUTATED"

    حدّ.execute(
        _طلب(action="gov.case.open", target="gov/case-A"),
        declared_effects=(أثر_الخارجي,),
        planner=lambda _: (أثر_الخارجي,),
        applier=مطبِّقٌ_غيرُ_مستثنًى,
        operation_key=_مفتاح("outer-3"),
        compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
    )

def test_إطارالأبالباقيبعدالرفضوبعدالعبورالمستثن(
    حدّ: SovereignExecutionBoundary,
    حالةُ_الدولة: dict[str, str],
) -> None:
    """إطارُ الأبِ لا يُمحى برفضِ ولدٍ ولا بعودةِ ولدٍ مستثنًى — والحمايةُ باقيةٌ حتى النهاية.

    (يقتلُ طفرةَ الضبطِ إلى None بدلَ الاستعادةِ بالرمزِ: لو مُحِيَ إطارُ الأبِ
    بعدَ ولدٍ مستثنًى لَما رُفِضَ الثاني.)
    """
    أثر_الداخل = _أثر("tasks/task-A/row")
    أثر_الداخل_المرفوض = _أثر("treasury/account-A")
    رفضٌ: list[int] = []

    def مطبِّقٌ_مُوالٍ(effect: SovereignEffect) -> None:
        # (1) ولدٌ غيرُ مستثنًى: يُرفَضُ
        with pytest.raises(NestedSovereignCallError):
            حدّ.execute(
                _طلب(action="credit_account", target="treasury/account-A"),
                declared_effects=(أثر_الداخل_المرفوض,),
                planner=lambda _: (أثر_الداخل_المرفوض,),
                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                operation_key=_مفتاح("inner-4a"),
                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل_المرفوض),),
            )
        رفضٌ.append(1)
        # (2) ولدٌ مستثنًى: يعبرُ ويَعودُ
        حصيلة_مستثنًى = حدّ.execute(
            _طلب(action="task.submit", target="tasks/task-A"),
            declared_effects=(أثر_الداخل,),
            planner=lambda _: (أثر_الداخل,),
            applier=lambda e: None,
            operation_key=_مفتاح("inner-4b"),
            compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
        )
        assert حصيلة_مستثنًى.is_replay is False
        # (3) بعدَ الولدِ المستثنَّى: الحمايةُ باقيةٌ — ولدٌ غيرُ مستثنًى يُرفَضُ من جديدٍ
        with pytest.raises(NestedSovereignCallError):
            حدّ.execute(
                _طلب(action="credit_account", target="treasury/account-A"),
                declared_effects=(أثر_الداخل_المرفوض,),
                planner=lambda _: (أثر_الداخل_المرفوض,),
                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                operation_key=_مفتاح("inner-4c"),
                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل_المرفوض),),
            )
        رفضٌ.append(2)
        حالةُ_الدولة[effect.resource] = "MUTATED"

    حدّ.execute(
        _طلب(action="gov.case.open", target="gov/case-A"),
        declared_effects=(_أثر("gov/case-A/row"),),
        planner=lambda _: (_أثر("gov/case-A/row"),),
        applier=مطبِّقٌ_مُوالٍ,
        operation_key=_مفتاح("outer-4"),
        compensators=(_معوّض(حالةُ_الدولة, _أثر("gov/case-A/row")),),
    )
    assert رفضٌ == [1, 2]
    # الإطارُ مُستعادٌ بعدَ اكتمالِ الأبِ — لا عبورَ نشطَ باقيًا في السياقِ
    assert _active_crossing.get() is None


# ═══════════════════════════════════════════════════════════════════════════
# 3 — السياقُ يُستعادُ بعدَ كلِّ مسارٍ: نجاحٌ، ورفضٌ، واستثناءٌ في المطبِّق
# ═══════════════════════════════════════════════════════════════════════════


def test_السياقيستعادبعدنجاحالعبوروالعبورالتالييعمل(
    حدّ: SovereignExecutionBoundary,
    حالةُ_الدولة: dict[str, str],
) -> None:
    """عبورٌ متتابعٌ (لا متعشِّشٌ) بعدَ اكتمالِ سابقِهِ يعملُ — والإطارُ نظيفٌ بينَهما.

    (يقتلُ طفرةَ حذفِ الاستعادةِ في `finally`: لو بقِيَ الإطارُ معلَّقًا
    لَرُفِظَ التالي كمتعشِّشٍ وهو ليسَ متعشِّشًا.)
    """
    _تنفيذٌ_كامل(حدّ, "credit_account", "seq-1", حالةُ_الدولة)
    assert _active_crossing.get() is None
    _تنفيذٌ_كامل(حدّ, "credit_account", "seq-2", حالةُ_الدولة)
    assert _active_crossing.get() is None


def test_السياقيستعادبعدرفضمتعششوالعبورالتالييعمل(
    حدّ: SovereignExecutionBoundary,
    حالةُ_الدولة: dict[str, str],
) -> None:
    """بعدَ عبورٍ رُفِضَ تعشيشُهُ (ورُدَّ أثرُهُ)، السياقُ نظيفٌ والعبورُ التاليُ يعملُ."""
    أثر_الخارجي = _أثر("gov/case-A/row")
    أثر_الداخل = _أثر("treasury/account-A")
    def مطبِّقٌ_يرفض(effect: SovereignEffect) -> None:
        with pytest.raises(NestedSovereignCallError):
            حدّ.execute(
                _طلب(action="credit_account", target="treasury/account-A"),
                declared_effects=(أثر_الداخل,),
                planner=lambda _: (أثر_الداخل,),
                applier=lambda e: حالةُ_الدولة.__setitem__(e.resource, "MUTATED"),
                operation_key=_مفتاح("inner-5"),
                compensators=(_معوّض(حالةُ_الدولة, أثر_الداخل),),
            )
        حالةُ_الدولة[effect.resource] = "MUTATED"

    حدّ.execute(
        _طلب(action="gov.case.open", target="gov/case-A"),
        declared_effects=(أثر_الخارجي,),
        planner=lambda _: (أثر_الخارجي,),
        applier=مطبِّقٌ_يرفض,
        operation_key=_مفتاح("outer-5"),
        compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
    )
    assert _active_crossing.get() is None
    _تنفيذٌ_كامل(حدّ, "credit_account", "seq-after-reject", حالةُ_الدولة)
    assert _active_crossing.get() is None


def test_السياقيستعادبعداستثناءالمطبق(
    حدّ: SovereignExecutionBoundary,
    حالةُ_الدولة: dict[str, str],
) -> None:
    """استثناءُ المطبِّقِ يُغلَّفُ في `IdempotencyError` بعدَ نقلِ السجلِّ إلى «فاشل» (لا أثرَ مُطبَّقًا فلا تعويضَ)، والسياقُ يُستعادُ في `finally`.

    (يقتلُ طفرةَ حذفِ `finally` في مسارِ الاستثناءِ تحديدًا.)
    """
    أثر_الخارجي = _أثر("gov/case-A/row")

    def مطبِّقٌ_يفشل(effect: SovereignEffect) -> None:
        raise RuntimeError("فشلٌ مقيسٌ في المطبِّق")

    with pytest.raises(IdempotencyError, match="فشلٌ مقيسٌ"):
        حدّ.execute(
            _طلب(action="gov.case.open", target="gov/case-A"),
            declared_effects=(أثر_الخارجي,),
            planner=lambda _: (أثر_الخارجي,),
            applier=مطبِّقٌ_يفشل,
            operation_key=_مفتاح("outer-6"),
            compensators=(_معوّض(حالةُ_الدولة, أثر_الخارجي),),
        )
    assert _active_crossing.get() is None, "الإطارُ بقِيَ معلَّقًا بعدَ استثناءِ المطبِّقِ."
    # والعبورُ التالي (متتابعٌ) يعملُ — فالرفضُ المزعجُ للتعشيشِ لم يعد يصيبُ البريئَ
    _تنفيذٌ_كامل(حدّ, "credit_account", "seq-after-exc", حالةُ_الدولة)
    assert _active_crossing.get() is None
