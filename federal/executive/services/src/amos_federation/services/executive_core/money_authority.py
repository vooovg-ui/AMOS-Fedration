"""
AMOS-Federation Executive Core — Money Authority
الهدف: لا يتحرّكُ مالٌ عامٌّ حتّى يُسألَ المُحرِّكُ الدستوريُّ ويأذنَ بفاعلِ التفويضِ المُعلَن
النطاق: executive_core — نقطةُ فرضٍ واحدةٌ يستدعيها مسارُ تخويلِ المال
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-21 (Q-31)
تعتمد على: services/executive_core/sovereignty_bridge.py · common/money_delegation.py

## لماذا هنا لا في الخزانة

حُسِمَ **Q-31** بالخيارِ الثاني: «وصلُ المُحرِّكِ عندَ `_authorize_money`». وموضعُ
الوحدةِ اختيارٌ بُنيويٌّ لا ذوقيّ: خزانةُ الدولةِ تستوردُ `executive_core` أصلًا،
و`executive_core` لا تستوردُ الخزانةَ ولا الاقتصادَ. فلو وُضِعَ الوصلُ في الخزانةِ
لصارَ لكلِّ خدمةٍ ماليّةٍ نسختُها من طريقةِ سؤالِ المُحرِّك، ولو وُضِعَ في `common`
لاستوردتْ مفردةٌ مشتركةٌ جسرًا سياديًّا. فهو هنا: نقطةُ فرضٍ **واحدة**.

## لماذا تُحفَظُ البوّابةُ ولا يُحفَظُ الفاعل

هذا هو الحدُّ الفاصلُ بينَ هذه الوحدةِ وسابقةِ **2A**، وهو مقصودٌ حرفيًّا:

- **البوّابةُ** آلةٌ **بلا فاعل**: قواعدُ وسجلٌّ وتحقيقُ سلسلة. بناؤها مُكلِفٌ
  (قِيسَ: ‏50 مللي)، ولا تحملُ هويّةَ فرعٍ، فحفظُها لا يُخوِّلُ أحدًا.
- **المُصرِّحُ** هو الذي يحملُ الفاعلَ (`actor=TREASURY`)، فيُبنى **عندَ كلِّ
  نداءٍ** من `delegation.actor` المُستخرَجِ من جدولِ التفويضِ المُعلَن. وبناؤه
  ببوّابةٍ محفوظةٍ قِيسَ: ‏0.007 مللي — فلا عُذرَ أداءٍ يُبرِّرُ حفظَ فاعل.

وسابقةُ 2A فعلتِ العكسَ: بنَتْ مُصرِّحًا موسومًا بالخزانةِ **مرّةً واحدةً لكائنِ
التشغيلِ كلِّه**، فصارَ كلُّ ما يمرُّ منه خزانةً بحكمِ البناء. فحفظُ مُصرِّحٍ موسومٍ
هنا يُعيدُ إنتاجَ ما مَنَعَه Q-19 نصًّا، ولذلك يمنعُه هذا الملفُّ بُنيةً لا نصيحةً.

## المُحرِّكُ يكتبُ — قِيسَ لا افتُرِض

`review_only` اسمُها «مراجعةٌ فقط» بمعنى **أنّها لا تُنفِّذُ أثرًا ولا تصرفُ
تصريحًا**، لا بمعنى أنّها لا تكتبُ شيئًا. قِياسُ التنميطِ أثبتَ أنَّ
`engine.evaluate` تُلحِقُ قيدًا في السجلِّ الدستوريِّ
(`core/constitution/ledger/constitutional_ledger.jsonl`) وتُعيدُ تحقيقَ السلسلةِ
كلِّها قبلَ الإلحاق. فلهذا الوصلِ نتيجتانِ مُعلَنتان:

1. **مكسبٌ**: صارَ لكلِّ تحريكِ مالٍ يمرُّ من هنا **أثرٌ مُسلسَلٌ مانعُ التلاعب**.
   وحدُّ هذا الأثرِ مقيسٌ لا مُدَّعى: القيدُ يختمُ **الفعلَ الدستوريَّ والفاعلَ
   والمورِدَ والحكمَ وعددَ القواعدِ المُقيَّمةِ وبصمةَ الطلب**، و**لا يختمُ** اسمَ
   العمليّةِ النطاقيَّ ولا المدخل: بِنيةُ القيدِ في النواةِ تُسجِّلُ حكمَها لا
   بياناتِ مَن نادى. فمن أرادَ ختمَ العمليّةِ نفسِها فذاكَ تغييرٌ في النواةِ
   يُقرَّرُ سياديًّا، لا يُدَّعى هنا.
2. **كُلفةٌ**: زمنُ المراجعةِ ينمو خطّيًّا مع طولِ السجلِّ (قِيسَ: ‏153 مللي عندَ
   ‏9633 قيدًا)، فمجموعُ الكلفةِ تربيعيٌّ مع عددِ العمليّات. هذه صفةُ تصميمِ
   السجلِّ في النواةِ، لا صفةُ هذه الوحدةِ، ولا تُعالَجُ هنا بتلطيفٍ ولا بذاكرةٍ
   مؤقّتةٍ للأحكام: فحفظُ حكمٍ سابقٍ يعني أنَّ المُحرِّكَ لم يُسأَلْ، وذاكَ نقضُ
   Q-31 لا تنفيذُه. وقد سُجِّلَت الكُلفةُ حدًّا من حدودِ الصدقِ لا عيبًا مخفيًّا.

## الحدُّ المُعلَنُ لهذا الوصل (لا يُدَّعى ما ليس مفروضًا)

هذه الوحدةُ تُفرَضُ حيثُ تُنادى، وهي تُنادى من `_authorize_money` وحدَها. وقياسُ
Q-19 أثبتَ أنَّ **أربعةً** من عشرةِ مواضعِ تحريكِ المالِ تمرُّ بـ`_authorize_money`،
والستّةَ الباقيةَ لا تمرُّ به. فالمفروضُ دستوريًّا بعدَ هذا العملِ أربعةٌ لا عشرة،
وتوسيعُ النطاقِ إلى الستّةِ مسألةٌ سياديّةٌ مُقيَّدةٌ بـ**Q-32** لا تُحسَمُ اجتهادًا.

ملاحظةٌ مؤرَّخةٌ (W-757 · 2026-10-31 · M1 الدفعة 1): العدُّ أعلاه عدُّ **طبقةِ التخويل**
(`_authorize_money`) وما زالَ أربعةً كما هو. وصارت عمليّاتُ الخزانةِ الستُّ الذرّيّةُ
(التأسيسُ · الحساب · الموازنة · التخصيص · التمويل · الصرف) **تعبرُ الحدَّ السياديَّ**
بالدوالِّ أدناه، فيُسألُ المُحرِّكُ عن كلٍّ منها عندَ العبورِ بفاعلِ التفويض — طبقةٌ ثانيةٌ
لا تُغيِّرُ عدَّ الأولى. و`reverse_transaction` ومُغلِّفا المالِ والمركّباتُ لم تعبُرْ بعد.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from amos_federation.common.money_delegation import resolve_money_delegation

from .sovereignty_bridge import (
    AuthorityEvidence,
    ConstitutionalAuthorizer,
    _core_sovereignty,
    compensator,
    declared_effect,
    operation_key,
)

if TYPE_CHECKING:  # pragma: no cover — للتوثيقِ لا للتشغيل
    from collections.abc import Callable

    from amos_federation.common.money_delegation import MoneyDelegation

ALLOWED_DECISION = "ALLOW"
"""الحكمُ الوحيدُ الذي يُمرِّرُ مالًا. وكلُّ ما سواه رفضٌ — إغلاقٌ لا تفسير."""


class ConstitutionalMoneyDenialError(PermissionError):  # noqa: N818 — رفضُ سلطةٍ لا عطل
    """رفضَ المُحرِّكُ الدستوريُّ تحريكَ هذا المال.

    يُورَثُ من `PermissionError` لا من `TreasuryError`، لأنَّ حالَه حالُ من لا
    صلاحيةَ له (كما `RegistryAuthorizationError`) لا حالَ خلَلٍ في الخزانة: فما
    منعَه الدستورُ ليس عطلًا يُعاد، بل حدًّا يُحترَم.
    """

    def __init__(self, delegation: MoneyDelegation, evidence: AuthorityEvidence) -> None:
        self.delegation = delegation
        self.evidence = evidence
        advisory = "؛ ".join(evidence.advisory_violations) or "لا مخالفةَ استشاريّةً مُبلَّغة"
        super().__init__(
            f"منعَ المُحرِّكُ الدستوريُّ العمليّةَ «{delegation.operation}»: "
            f"الفعلُ «{delegation.constitutional_action}» بفاعلِ «{delegation.actor}» "
            f"حُكِمَ «{evidence.decision}» في طبقةِ «{evidence.authority_layer}» "
            f"({evidence.rules_evaluated} قاعدةً مُقيَّمة · بصمةُ الطلبِ "
            f"{evidence.request_fingerprint}). المخالفاتُ الاستشاريّة: {advisory}."
        )


_SHARED_GATEWAY: Any | None = None
_CROSSING_GATEWAY: Any | None = None
_CROSSING_BOUNDARY: Any | None = None
"""الآلةُ المحفوظةُ بلا فاعل: بوّابةُ المراجعةِ وحدَها (كما كانت) · وبوّابةُ العبورِ وحدُّه (M1).
منفصلتانِ عمدًا — انظرْ ملاحظةَ M1 أدناه."""


def _authorizer_for(actor: str, *, slot: str = "review") -> ConstitutionalAuthorizer:
    """مُصرِّحٌ جديدٌ بفاعلٍ مُعلَنٍ، على آلةٍ واحدةٍ محفوظةٍ بلا فاعلٍ لكلِّ مَصرِف.

    أوّلُ نداءٍ يبني الآلةَ ويحفظُها من المُصرِّحِ نفسِه (فلا جسرَ ثانيًا ولا
    استعمالَ لواجهةٍ خاصّة)، وما بعدَه يبني مُصرِّحًا جديدًا فوقَها. والمُصرِّحُ
    **لا يُحفَظُ أبدًا**: حفظُه هو عينُ سابقةِ 2A. ومَصرِفُ «review» يحفظُ البوّابةَ وحدَها
    (سلوكُه قبلَ M1 حرفًا)؛ ومَصرِفُ «crossing» يحفظُ الحدَّ أيضًا، لأنَّ بناءَه يُعيدُ قراءةَ
    سجلِّ الذرّيّةِ كاملًا عندَ كلِّ نداء. (W-757: موضعا البناءِ هما هما — لا موضعَ ثالث.)
    """
    global _SHARED_GATEWAY, _CROSSING_GATEWAY, _CROSSING_BOUNDARY
    crossing = slot == "crossing"
    gateway = _CROSSING_GATEWAY if crossing else _SHARED_GATEWAY
    if gateway is None:
        first = ConstitutionalAuthorizer(actor=actor)
        if crossing:
            _CROSSING_GATEWAY, _CROSSING_BOUNDARY = first.gateway, first.boundary
        else:
            _SHARED_GATEWAY = first.gateway
        return first
    return ConstitutionalAuthorizer(
        actor=actor, gateway=gateway, boundary=_CROSSING_BOUNDARY if crossing else None
    )


def require_constitutional_money_authority(
    operation: str,
    *,
    entrypoint: str,
    target: str,
    metadata: dict[str, Any] | None = None,
) -> AuthorityEvidence:
    """اسألِ المُحرِّكَ الدستوريَّ قبلَ تحريكِ المال، وأغلِقْ على غيرِ الإذن.

    الترتيبُ مقصود: يُحضَرُ التفويضُ المُعلَنُ أوّلًا، فالفعلُ الدستوريُّ والفاعلُ
    يُؤخَذانِ من الجدولِ المُعلَنِ لا من نصٍّ يُمرِّرُه النداء. فلا يستطيعُ منادٍ أن
    يُسمّيَ فعلًا دستوريًّا من عندِه.

    Args:
        operation: اسمُ العمليّةِ الماليّةِ كما في جدولِ التفويضِ المُعلَن.
        entrypoint: مدخلُ الشِّفرةِ المُعلَنُ لهذه العمليّة.
        target: المورِدُ المقصودُ — يُسجَّلُ في السجلِّ الدستوريِّ مع الحكم.
        metadata: بيانٌ إضافيٌّ يُعرَضُ على المُحرِّكِ في الطلب. **لا يُختَمُ في
            السجلِّ** (قِيسَ)، ولا يُغيِّرُ الفعلَ ولا الفاعل.

    Returns:
        `AuthorityEvidence` بحكمِ `ALLOW` — وأثرُها مُقيَّدٌ في السجلِّ الدستوريّ.

    Raises:
        UndeclaredMoneyDelegationError: عمليّةٌ أو مدخلٌ بلا تفويضٍ مُعلَن (Q-19).
        ConstitutionalMoneyDenialError: المُحرِّكُ حكمَ بغيرِ `ALLOW`.
        SovereigntyUnavailableError: تعذّرَ حضورُ المُحرِّكِ — إغلاقٌ لا تجاوُز.
    """
    delegation = resolve_money_delegation(operation, entrypoint=entrypoint)
    record: dict[str, Any] = {
        "money_operation": delegation.operation,
        "entrypoint": delegation.entrypoint,
        "delegation_basis": delegation.basis,
    }
    if metadata:
        record.update(metadata)

    evidence = _authorizer_for(delegation.actor).review_only(
        delegation.constitutional_action, target, record
    )
    if evidence.decision != ALLOWED_DECISION:
        raise ConstitutionalMoneyDenialError(delegation, evidence)
    return evidence


# ── M1 (W-757 · M1_MONEY_CROSSING_DESIGN.md § 2.7 الدفعة 1 · § 2.9): العبورُ الواحد ──────
#
# النقطةُ الواحدةُ نفسُها (Q-31) تبني عبورَ المالِ أيضًا، فلا تستوردُ الخزانةُ جسرًا ولا تبني
# مُصرِّحًا (حرسُ Q-31/Q-19 قائمٌ كما هو). والقاعدةُ نفسُها: **الآلةُ تُحفَظُ والفاعلُ لا**.
# فللعبورِ بوّابةٌ وحدٌّ محفوظانِ بلا فاعل — **منفصلانِ** عن بوّابةِ المراجعةِ أعلاه، لأنَّ
# `guard_declared` يقرأُ دليلَه من آخرِ سجلٍّ في بوّابتِه، والمراجعةُ داخلَ المُطبِّقِ
# (`_authorize_money`) كانت ستُلحِقُ سجلَّها بعدَ حكمِ العبورِ فيُقرأُ دليلًا له — والمُصرِّحُ
# يُبنى **عندَ كلِّ نداءٍ** من `delegation.actor`. والحدُّ يُحفَظُ لأنَّ بناءَه يُعيدُ قراءةَ
# سجلِّ الذرّيّةِ كاملًا، وهو بلا فاعلٍ كالبوّابة (`SovereignExecutionBoundary(gateway,
# idempotency_ledger, consumed_permits)`). والبناءُ في `_authorizer_for` نفسِه (مَصرِفُ
# «crossing») — فلا موضعَ بناءٍ جديدًا للمُصرِّح (حرسُ Q-3 · 13 مُعلِنًا كما هو).


def _crossing_authorizer_for(actor: str) -> ConstitutionalAuthorizer:
    """مُصرِّحُ عبورٍ جديدٌ بفاعلٍ مُعلَن، على بوّابةٍ وحدٍّ محفوظَينِ بلا فاعلٍ (مَصرِفُ «crossing»)."""
    return _authorizer_for(actor, slot="crossing")


def money_crossing_contract(
    *,
    operation: str,
    entrypoint: str,
    target: str,
    effect_kind: str,
    detail: str,
    key_value: str,
    apply: Callable[[], Any],
    undo: Callable[[Any], None],
    undo_description: str,
    metadata: dict[str, Any],
    authorizer_factory: Callable[[str], Any] | None = None,
    undo_idempotent: bool = False,
) -> dict[str, Any]:
    """عقدُ عبورٍ واحدٍ لعمليّةِ مالٍ ذرّيّة — يُبنى هنا، **ويعبرُ في جسدِ العمليّةِ العامّة**.

    العبورُ نفسُه (`guard_declared(`) يقعُ في المُنادي: الإعلانُ مسؤوليّةُ العمليّة
    (`sovereign_write_inventory.py` § «تعبرُ الحدّ»)، وهذا يجمعُ ما تُعلِنُه.

    - **الفاعلُ والفعلُ من جدولِ التفويض**: لا فاعلَ مُثبَّتًا ولا فعلَ يُخترَع، والجدولُ
      يرفعُ لعمليّةٍ أو مدخلٍ غيرِ مُعلَن (Q-19).
    - **أثرٌ واحدٌ مُعلَنٌ قبلَ وقوعِه** محصورٌ في الهدف، ومعوِّضٌ مُعلَنٌ له (1I). والحركةُ
      وسندُها وأثرُ التدقيقِ والحدثِ تقعُ في **معاملةٍ واحدة**، فإعلانُها أثرَين يجعلُ الثانيَ
      مُطبِّقًا فارغًا يدّعي ما لم يفعل — فأُعلِنَت أثرًا واحدًا (§ 2.9 · انحرافٌ مُعلَنٌ عن § 2.8).
    - `authorizer_factory` مَنفذُ حقنٍ للفحوصِ وحدَها؛ يُعطى الفاعلَ المُعلَنَ لا غيرَه.
    - **[W-765 · Q-88 · DISC-149] تصحيحٌ بالقياس:** الحركةُ وسندُها في معاملةٍ واحدة، لكنَّ أثرَ
      التدقيقِ والحدثِ (`record_domain_trace`) بعدَ الالتزام، فالمُطبِّقُ **غيرُ ذرّيّ**
      (`evidence/W-764/treasury_atomicity_probe_before.txt`). فـ`undo_idempotent=True` تصريحُ
      العمليّةِ بأنَّ `undo` آمنٌ وقعَ الأثرُ أم لم يقع، فيُشغِّلُه الحدُّ على الأثرِ «ربما طُبِّق».
    """
    delegation = resolve_money_delegation(operation, entrypoint=entrypoint)
    effect = declared_effect(effect_kind, target, detail)
    applied: dict[str, Any] = {}

    def _apply(_effect: Any) -> Any:
        result = apply()
        applied["result"] = result
        return result

    build = authorizer_factory if authorizer_factory is not None else _crossing_authorizer_for
    return {
        "authorizer": build(delegation.actor),
        "actor": delegation.actor,
        "action": delegation.constitutional_action,
        "target": target,
        "declared_effects": (effect,),
        "applier": _apply,
        "operation_key": operation_key(f"state_treasury.{entrypoint}", key_value),
        "compensators": (
            compensator(
                effect.signature,
                lambda: undo(applied.get("result")),
                undo_description,
                idempotent=undo_idempotent,
            ),
        ),
        "metadata": {
            **metadata,
            "money_operation": delegation.operation,
            "entrypoint": delegation.entrypoint,
            "delegation_actor": delegation.actor,
            "delegation_basis": delegation.basis,
        },
    }


def money_crossing_kwargs(contract: dict[str, Any]) -> dict[str, Any]:
    """ما يُمرَّرُ إلى `guard_declared` من العقد — بلا المُصرِّحِ والفعلِ والهدف."""
    return {
        key: contract[key]
        for key in ("declared_effects", "applier", "operation_key", "compensators", "metadata")
    }


def settle_money_crossing(cross: Callable[[], Any], contract: dict[str, Any]) -> Any:
    """نفِّذِ العبورَ الذي سمّته العمليّةُ العامّة، وأعِدْ ما يراه المُنادي.

    **الفحوصُ المقفولةُ تبقى داخلَ المُطبِّق**: نقلُها قبلَ العبورِ يفصلُ القراءةَ عن الكتابةِ
    فيفتحُ سباقَ تجاوزِ الحدِّ على PostgreSQL. فخطأُ النطاقِ يقعُ داخلَ المُطبِّقِ قبلَ أيِّ أثر،
    فيلفُّه سجلُّ الذرّيّةِ (1H) في `IdempotencyError` بعدَ أن يُسجِّلَه فشلًا قابلًا للإعادة.
    ويُعادُ رفعُ **السببِ الأصليِّ نفسِه** بسلسلتِه — فلا يتغيّرُ عقدُ الأخطاءِ للمُنادين ولا
    يُبتلَعُ شيء. ولا يُفَكُّ إلّا اللفُّ الدقيقُ (`type is IdempotencyError` ذو سبب)، والسببُ
    يُرفَعُ أيًّا كان: خطأَ نطاقٍ أو رفضًا سياديًّا من داخلِ التنفيذ (مثلُ `PermitReplayError`
    لطلبٍ مُكرَّرٍ في الثانيةِ نفسِها — مقيسٌ في W-757). وأخطاءُ الذرّيّةِ بلا سبب (تعارضُ
    مفتاح · قيدُ التنفيذ) تمرُّ كما هي.
    """
    idempotency_error = _core_sovereignty("idempotency").IdempotencyError
    compensation_required = _core_sovereignty("compensation").CompensationRequired
    try:
        guarded = cross()
    except Exception as exc:
        if type(exc) is idempotency_error and exc.__cause__ is not None:
            raise exc.__cause__ from exc
        # [W-765 · Q-88] الأثرُ «ربما طُبِّق» عُوِّضَ تعويضًا نظيفًا ولا بقيّة: الحالةُ رجعت،
        # فيُرفَعُ السببُ الأصليُّ (خطأُ النطاقِ مثلًا) بملاحظةِ التعويض — ولا يتغيّرُ عقدُ
        # الأخطاءِ للمُنادين. وغيرُ النظيفِ أو ذو البقيّةِ يُرفَعُ كما هو (FAILED_FINAL).
        if isinstance(exc, compensation_required) and exc.state_is_clean:
            wrapped = exc.__cause__
            if type(wrapped) is idempotency_error and wrapped.__cause__ is not None:
                original = wrapped.__cause__
                original.add_note(
                    "[Q-88] المُطبِّقُ رفعَ فعُوِّضَ أثرُه «ربما طُبِّق» بمعوِّضٍ مُثبِّت: "
                    f"{exc.outcome.record.compensation_id} — الحالةُ رجعت"
                )
                raise original from exc
        raise
    if guarded.is_replay:
        # إعادةٌ لمفتاحٍ مُثبَّت: لا أثرَ ثانيًا ولا حدثَ ثانيًا — يُقال «أُعيد».
        return {
            "replayed": True,
            "operation_key": guarded.outcome.operation_key,
            "target": contract["target"],
        }
    return guarded.value


__all__ = [
    "ALLOWED_DECISION",
    "ConstitutionalMoneyDenialError",
    "money_crossing_contract",
    "money_crossing_kwargs",
    "require_constitutional_money_authority",
    "settle_money_crossing",
]
