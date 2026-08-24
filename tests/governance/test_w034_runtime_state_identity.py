# =============================================================================
# File:        tests/governance/test_w034_runtime_state_identity.py
# الهدف · Purpose: حرسُ W-034 (حسمُ Q-40 ج) — كلُّ كاتبِ حالةِ تشغيلٍ في النواةِ
#             السياديّةِ يسِمُ ملفَّه بترويسةِ هدفٍ ويُنشئُ بطاقةَ هويّةٍ معَ
#             المجلَّدِ، بلا تضييقِ كاشفٍ وبلا نقلِ موضعِ سجلٍّ وبلا فقدِ سجلّ
# النطاق:     شجرةٌ مؤقّتةٌ فقط. قاعدةُ الحكمِ تُستورَدُ من كاشفِ الهويّةِ نفسِه.
# المالك · Owner: tests/governance
# Created:     2026-08-24
# Phase:       W-034 · Q-40 (ج)
# Article 009: هذا الملف يلتزم بالمادة 009 — الشفافية والمراجعة المستمرة.
# =============================================================================
"""حرسُ هويّةِ أثرِ التشغيل — تنفيذُ حسمِ Q-40 (الخيارُ ج).

الهدف: إثباتُ ثلاثةِ أمورٍ بالقياسِ لا بالوعدِ:

1. **الوسمُ يقعُ فعلًا:** كلُّ كاتبِ حالةِ تشغيلٍ (سجلُّ الذرّيّةِ · الأذونُ
   المُستهلَكةُ · الصادرُ · التعويضُ) يكتبُ في ملفِّه ترويسةَ هدفٍ، ويُنشئُ
   `README.md` كاملَ الحقولِ معَ المجلَّدِ — ويُحكَمُ على ذلك **بكاشفِ الهويّةِ
   نفسِه** لا بقاعدةٍ ألطفَ تُكتَبُ هنا.
2. **الوسمُ لا يُفسِدُ سجلًّا:** الترويسةُ مفتاحٌ في خريطةٍ مفاتيحُها معرّفاتُ
   عملياتٍ، فيُثبَتُ أنَّ العدَّ والقراءةَ لا تتغيّرُ بها، وأنَّ `$comment` لا
   يُقرأُ إذنًا مُستهلَكًا ولا سجلَّ عمليّة.
3. **الكاشفُ لم يُضيَّقْ:** ملفُّ JSON بلا ترويسةٍ في المجلَّدِ نفسِه **يبقى
   مخالفًا** — فلو ضُيِّقَ الكاشفُ يومًا لأجلِ `.runtime/` سقطَ هذا الحرس.

النطاق: لا شبكةَ ولا قاعدةَ بياناتٍ ولا كتابةَ في شجرةِ المستودعِ: كلُّ قياسٍ في
        `tmp_path`، وهو حرسٌ على عدمِ تلويثِ المقيسِ أيضًا.
المالك: tests/governance
تاريخ الإنشاء: 2026-08-24

حدُّ صدقِ هذا الحرس: يُثبِتُ أنَّ الكتّابَ الأربعةَ في `core/sovereignty` يسِمون،
ولا يُثبِتُ أنَّ كلَّ كاتبِ حالةِ تشغيلٍ في المشروعِ كلِّه يسِمُ — كاتبٌ جديدٌ يُضافُ
غدًا بغيرِ هذه الوحدةِ يفلتُ من هذا الحرسِ حتّى يُضافَ إليه.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# قاعدةُ الحكمِ من الكاشفِ نفسِه — لا تُعادُ كتابتُها هنا.
sys.path.insert(0, str(REPO_ROOT / "tools" / "governance"))
import check_repository_identity as cri  # noqa: E402

from core.sovereignty.compensation import COMPENSATION_STATE_CARD  # noqa: E402
from core.sovereignty.enforcement import (  # noqa: E402
    CONSUMED_PERMITS_STATE_CARD,
    ConsumedPermitLedger,
    PermitReplayError,
)
from core.sovereignty.idempotency import (  # noqa: E402
    IDEMPOTENCY_STATE_CARD,
    IdempotencyKey,
    IdempotencyLedger,
)
from core.sovereignty.outbox import OUTBOX_STATE_CARD  # noqa: E402
from core.sovereignty.runtime_identity import (  # noqa: E402
    IDENTITY_KEY,
    RuntimeStateCard,
    ensure_directory_card,
    stamped,
    strip_identity,
)

ALL_CARDS = (
    IDEMPOTENCY_STATE_CARD,
    CONSUMED_PERMITS_STATE_CARD,
    OUTBOX_STATE_CARD,
    COMPENSATION_STATE_CARD,
)


# ── 1) الوسمُ يقعُ فعلًا ──────────────────────────────────────────────────────


def test_consumed_permit_ledger_stamps_purpose_and_writes_card(tmp_path: Path) -> None:
    """سجلُّ الأذونِ: ترويسةُ هدفٍ في الملفِّ وبطاقةٌ معَ المجلَّد."""
    ledger = ConsumedPermitLedger(path=tmp_path / "state" / "consumed_permits.json")
    ledger.consume("permit-1")

    raw = json.loads((tmp_path / "state" / "consumed_permits.json").read_text(encoding="utf-8"))
    assert IDENTITY_KEY in raw, "ملفُّ حالةِ التشغيلِ كُتِبَ بلا ترويسةِ هدفٍ"
    assert "الهدف:" in raw[IDENTITY_KEY]
    assert (tmp_path / "state" / "README.md").exists(), "المجلَّدُ كُتِبَ فيه بلا بطاقةِ هويّةٍ"


def test_idempotency_ledger_stamps_purpose_and_writes_card(tmp_path: Path) -> None:
    """سجلُّ الذرّيّةِ: الوسمُ نفسُه بالكاتبِ نفسِه لا بنسخةٍ ثانيةٍ من المنطق."""
    ledger = IdempotencyLedger(path=tmp_path / "state" / "idempotency.json")
    ledger.reserve(key=IdempotencyKey("قياس", "عمليّة-1"), fingerprint="بصمة-1")

    raw = json.loads((tmp_path / "state" / "idempotency.json").read_text(encoding="utf-8"))
    assert "الهدف:" in raw[IDENTITY_KEY]
    assert (tmp_path / "state" / "README.md").exists()


@pytest.mark.parametrize("card", ALL_CARDS, ids=lambda c: c.name)
def test_every_card_declares_all_article_nine_fields(card: RuntimeStateCard, tmp_path: Path) -> None:
    """بطاقةُ كلِّ كاتبٍ تمرُّ بحقولِ المادةِ التاسعةِ **بحكمِ الكاشفِ نفسِه**."""
    folder = tmp_path / "state"
    folder.mkdir()
    (folder / "runtime.json").write_text(
        json.dumps(stamped({"k": "v"}, card=card), ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    ensure_directory_card(folder, card=card)

    assert cri.audit(tmp_path) == [], "بطاقةٌ أو ترويسةٌ لا تمرُّ بقاعدةِ الكاشفِ"


def test_writing_runtime_state_leaves_identity_gate_green(tmp_path: Path) -> None:
    """المخالفةُ المقيسةُ في Q-40 لا تُعادُ: كتابةُ الأثرِ ثمَّ الكاشفُ = صِفرٌ.

    هذا هو نصُّ الشكوى في Q-40: «أيُّ عاملٍ يُشغِّلُ الخدماتَ من الجذرِ يجدُ حزمةَ
    الجذرِ حمراءَ». فيُقاسُ الأمرُ كما شُكِيَ: يُكتَبُ الأثرُ ثمَّ يُسألُ الكاشف.
    """
    folder = tmp_path / ".runtime" / "sovereignty"
    ConsumedPermitLedger(path=folder / "executive_core_consumed_permits.json").consume("p-1")
    IdempotencyLedger(path=folder / "executive_core_idempotency.json").reserve(
        key=IdempotencyKey("قياس", "عمليّة-1"), fingerprint="بصمة-1"
    )

    assert cri.audit(tmp_path) == []


# ── 2) الوسمُ لا يُفسِدُ سجلًّا ────────────────────────────────────────────────


def test_stamp_is_not_read_as_a_consumed_permit(tmp_path: Path) -> None:
    """`$comment` ترويسةٌ لا إذنٌ: لا يُعَدُّ ولا يُقرأُ مُستهلَكًا."""
    ledger = ConsumedPermitLedger(path=tmp_path / "state" / "consumed.json")
    ledger.consume("permit-1")
    ledger.consume("permit-2")

    assert ledger.count() == 2, "الترويسةُ حُسِبَت سجلًّا فزادَ العدُّ"
    assert not ledger.is_consumed(IDENTITY_KEY)
    assert ledger.is_consumed("permit-1") and ledger.is_consumed("permit-2")
    with pytest.raises(PermitReplayError):
        ledger.consume("permit-1")


def test_stamp_is_not_read_as_an_operation_record(tmp_path: Path) -> None:
    """سجلُّ الذرّيّةِ يُقرأُ سجلّاتِه وحدَها، والاستعادةُ لا تتعثّرُ بالترويسة."""
    ledger = IdempotencyLedger(path=tmp_path / "state" / "idempotency.json")
    key = IdempotencyKey("قياس", "عمليّة-1")
    ledger.reserve(key=key, fingerprint="بصمة-1")

    assert ledger.count() == 1, "الترويسةُ حُسِبَت سجلًّا فزادَ العدُّ"
    assert [r.key.composite for r in ledger.all_records()] == [key.composite]
    assert ledger.get(key) is not None


def test_strip_identity_removes_only_header_keys() -> None:
    """التجريدُ يُسقِطُ الترويسةَ ولا يُسقِطُ سجلًّا مفتاحُه يُشبِهُها."""
    assert strip_identity({IDENTITY_KEY: "ترويسة", "permit-1": "زمن"}) == {"permit-1": "زمن"}
    assert strip_identity({"comment": "سجلٌّ لا ترويسةٌ"}) == {"comment": "سجلٌّ لا ترويسةٌ"}


def test_existing_card_is_never_overwritten(tmp_path: Path) -> None:
    """بطاقةٌ كتبَها إنسانٌ لا تُمسَحُ ببطاقةٍ آليّةٍ."""
    folder = tmp_path / "state"
    folder.mkdir()
    (folder / "README.md").write_text("# بطاقةٌ بيدِ إنسانٍ\n", encoding="utf-8")

    assert ensure_directory_card(folder, card=CONSUMED_PERMITS_STATE_CARD) is None
    assert (folder / "README.md").read_text(encoding="utf-8") == "# بطاقةٌ بيدِ إنسانٍ\n"


# ── 3) الكاشفُ لم يُضيَّقْ ────────────────────────────────────────────────────


def test_unstamped_runtime_file_is_still_a_violation(tmp_path: Path) -> None:
    """الحلُّ وسمٌ لا تضييقٌ: ملفٌّ بلا ترويسةٍ يبقى مخالفًا وإن كانَ أثرَ تشغيلٍ."""
    folder = tmp_path / ".runtime" / "sovereignty"
    folder.mkdir(parents=True)
    (folder / "unstamped.json").write_text('{"a": 1}\n', encoding="utf-8")
    ensure_directory_card(folder, card=CONSUMED_PERMITS_STATE_CARD)

    kinds = {v["kind"] for v in cri.audit(tmp_path)}
    assert "MISSING_PURPOSE" in kinds, "الكاشفُ صارَ يُعفي `.runtime/` — وهذا تضييقٌ ممنوعٌ"
