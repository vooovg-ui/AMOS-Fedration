"""
AMOS-Federation National Registry
الهدف: السجل الوطني للهوية الكانونية — الحلقة التي تربط الجلسة بالمنصب بالمال
النطاق: services/national_registry
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-17 (R7-C)
"""

from amos_federation.services.national_registry.resolver import (
    AuthorityDecision,
    ForgedAuthorityError,
    IdentityResolution,
    IdentityResolutionError,
    resolve_authority,
    resolve_identity,
    resolve_official_for_principal,
)
from amos_federation.services.national_registry.service import (
    NationalRegistry,
    get_national_registry,
    reset_national_registry,
)

# `state_authority_grants` (في `models` هنا) يحمل مفتاحين أجنبيين إلى `state_budgets`
# و`state_accounts` المعرَّفين في `state_treasury.models`. فإن حُمِّلَ هذا السجلُّ وحده
# سقط كلُّ `create_all` لاحقٍ بـ`NoReferencedTableError` بحسب ترتيب استيراد المتصل.
# يُسجَّل جدولا الخزانة هنا — بعد اكتمال `resolver` و`service` — لأنّ الخزانة نفسها
# تستورد `national_registry.resolver`؛ فاستيرادها من داخل `models` يُنتج دورة استيراد.
# والترتيبُ هنا حِملٌ لا ذوق: `isort: split` يمنعُ الفرزَ من رفعِه فوقَ `resolver`.
# isort: split
import amos_federation.services.state_treasury.models  # noqa: F401

__all__ = [
    "AuthorityDecision",
    "ForgedAuthorityError",
    "IdentityResolution",
    "IdentityResolutionError",
    "NationalRegistry",
    "get_national_registry",
    "reset_national_registry",
    "resolve_authority",
    "resolve_identity",
    "resolve_official_for_principal",
]
