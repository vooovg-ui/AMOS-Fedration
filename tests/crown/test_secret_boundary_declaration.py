"""
الهدف: إثباتُ أنَّ حارسَ حدودِ الأسرارِ يفرِّقُ بينَ سرٍّ حقيقيٍّ وذكرِ نمطِه في
       قيمةِ اختبارٍ سلبيّةٍ مُعلَنةٍ صراحةً — فيرفضُ الأوّلَ ولا يُحمِّرُ الثاني،
       ولا يصيرُ الإعلانُ بابًا يُخفَى منه سرٌّ صالحٌ للاستعمال (DISC-021).
النطاق: `_pem_hits` و`_declared_not_secret_at` و`_is_key_material_at`
        و`declared_exempt_lines` و`gate_no_private_key_in_tree` من
        `tools/crown/verify_secret_boundaries.py`.
المالك: tests/crown
تاريخ الإنشاء: 2026-08-28
تاريخ آخر تعديل: 2026-08-28

لماذا هذا الاختبار
------------------
قِيسَت `ci.yml` في المستودعِ التنفيذيِّ فسقطَت بوّابتا التاجِ 2ب والسيادةِ 6 على
`tests/sovereignty/test_outbox.py`، وليسَ فيه سرٌّ: القيمةُ مُختَرَعةٌ ومُعلَنٌ فوقَها
`truth-audit: not-a-secret`. فكانَ الحارسُ يُبلِّغُ عن تسريبٍ لا وجودَ له — أحمرُ
كاذبٌ يُفسِدُ صدقَ القياسِ. والإصلاحُ أن يعرِفَ الحارسُ العلامةَ عينَها التي يعرفُها
`truth_audit`، مشروطةً بثلاثةِ قيودٍ مجتمعةٍ تُثبَتُ هنا واحدًا واحدًا.

ولا يحملُ هذا الملفُّ نفسُه نمطَ PEM نصًّا: كلُّ كتلةٍ تُركَّبُ من أجزاءٍ في زمنِ
التشغيلِ، كما يفعلُ الحارسُ، فلا يُسقِطُ الاختبارُ البوّابةَ التي يقيسُها.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "tools" / "crown" / "verify_secret_boundaries.py"


def _load_tool():
    spec = importlib.util.spec_from_file_location("verify_secret_boundaries_disc021", TOOL_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


guard = _load_tool()

# ترويسةُ المفتاحِ تُركَّبُ من أجزاءٍ لسببَينِ مُعلَنَينِ، لا تحايلًا على حرسٍ:
#   1) بوّابةُ 2 في tools/crown/verify_crown_root_of_trust.py تمسحُ tests/crown/ بنمطٍ
#      حرفيٍّ على نصِّ الملفِّ، فملفُّ حرسِ الأسرارِ نفسُه لو حملَ الترويسةَ حرفيًّا لأسقطَها —
#      وهي العلّةُ التي قُيِّدَت DISC-023. وملفُّ الماسحِ يُركِّبُ نمطَه بالطريقةِ عينِها.
#   2) والقيمةُ المُركَّبةُ في زمنِ التشغيلِ **مطابِقةٌ حرفًا بحرفٍ** للترويسةِ الحقيقيّةِ،
#      فالمحروسُ يُقاسُ بها كما لو كُتبَت حرفيًّا؛ لا فحصَ أُضعِفَ ولا إعفاءَ أُضيف.
_DASHES = "-" * 5
BEGIN = _DASHES + "BEGIN " + "PRIVATE KEY" + _DASHES
END = _DASHES + "END " + "PRIVATE KEY" + _DASHES
BODY = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC" + "A" * 20
MARKER = "truth-audit: not-a-secret"

TEST_PATH = "tests/sovereignty/test_placeholder.py"
CODE_PATH = "core/crown/identity.py"


def _fixture_value(*, declared: bool) -> str:
    """قيمةُ اختبارٍ سلبيّةٍ في سطرٍ واحدٍ: بدايةٌ بلا جسدٍ ولا خاتمةٍ."""
    declaration = f"    # {MARKER} — قيمةٌ مُختَرَعةٌ لاختبارٍ سلبيّ\n" if declared else ""
    return declaration + f'    قيمة = "{BEGIN}abc"\n'


def _real_key(*, declared: bool) -> str:
    """مفتاحٌ صالحٌ للاستعمالِ: بدايةٌ وجسدُ base64 وخاتمةٌ."""
    declaration = f"    # {MARKER} — إعلانٌ يُحاولُ سترَ مفتاحٍ حقيقيّ\n" if declared else ""
    return declaration + f'    مفتاح = """{BEGIN}\n{BODY}\n{END}"""\n'


# ── أ) سرٌّ حقيقيٌّ يُرفَض ─────────────────────────────────────────────────────


def test_سرٌّ_حقيقيٌّ_بلا_إعلانٍ_يُرفَض() -> None:
    assert guard._pem_hits(TEST_PATH, _real_key(declared=False)) != []


def test_الإعلانُ_لا_يستُرُ_مفتاحًا_حقيقيًّا() -> None:
    """أهمُّ حدٍّ: الإعلانُ لا يُعفي مادةَ مفتاحٍ صالحةً وإن كانَ في شجرةِ الاختبار."""
    text = _real_key(declared=True)
    assert guard._is_key_material_at(text.splitlines(), 1) is True
    assert guard._pem_hits(TEST_PATH, text) != [], "إعلانٌ استرَ مفتاحًا — البابُ مفتوح"


def test_قيمةٌ_غيرُ_مُعلَنةٍ_تُرفَض_وإن_لم_تكنْ_مادةَ_مفتاح() -> None:
    """ما لم يُعلَنْ لا يُعفى: الصمتُ ليسَ إعلانًا."""
    assert guard._pem_hits(TEST_PATH, _fixture_value(declared=False)) != []


# ── ب) قيمةُ اختبارٍ مُعلَنةٌ لا تُعَدُّ سرًّا ────────────────────────────────────


def test_قيمةُ_اختبارٍ_مُعلَنةٌ_لا_تُعَدُّ_سرًّا() -> None:
    assert guard._pem_hits(TEST_PATH, _fixture_value(declared=True)) == []


# ── حدودُ الإعفاءِ: لا يُوسَّعُ بحيثُ يُخفي سرًّا ──────────────────────────────────


def test_الإعلانُ_لا_يُعفي_ملفًّا_كاملًا() -> None:
    """سطرٌ خالٍ يقطعُ الفقرةَ، فلا يمتدُّ الإعلانُ إلى ما بعدَه."""
    text = _fixture_value(declared=True).replace(
        "\n    قيمة", "\n\n    # سطرٌ فاصلٌ يقطعُ الفقرة\n    قيمة"
    )
    assert guard._pem_hits(TEST_PATH, text) != []


def test_الإعلانُ_لا_يُقبَلُ_خارجَ_شجرةِ_الاختبار() -> None:
    """الإعفاءُ مقصورٌ على `tests/`: لا يُعلَنُ في شِفرةِ الإنتاج."""
    text = _fixture_value(declared=True)
    assert guard._pem_hits(CODE_PATH, text) != []
    assert guard._declared_not_secret_at(CODE_PATH, text.splitlines(), 1) is False


def test_العلامةُ_عينُها_التي_يعرفُها_مدقّقُ_الحقيقة() -> None:
    """مصدرُ حقيقةٍ واحدٌ لمعنى «ليست سرًّا» — لا علامةٌ ثانيةٌ تُخترَع."""
    audit = REPO_ROOT / "tools" / "governance" / "truth_audit.py"
    assert f'"{guard.DECLARATION_MARKER}"' in audit.read_text(encoding="utf-8")


# ── الشجرةُ الحقيقيّةُ: قياسٌ لا وصفٌ ─────────────────────────────────────────


def test_الشجرةُ_الحقيقيّةُ_بلا_مادةِ_مفتاحٍ_وإعفاؤها_مَعدودٌ() -> None:
    """البوّابةُ خضراءُ على المستودعِ، والإعفاءاتُ تُعَدُّ وتُعلَنُ لا تُخفى."""
    guard.failures.clear()
    guard.passed.clear()
    guard.gate_no_private_key_in_tree()
    assert guard.failures == []
    assert len(guard.declared_exempt_lines()) >= 1
