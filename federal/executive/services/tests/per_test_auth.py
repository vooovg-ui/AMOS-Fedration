"""
ترويساتُ مصادقةٍ تُصدِرُ رمزًا جديدًا لكلِّ وصولٍ — WI-097 (T0)
الهدف: عزلُ العَرَضِ (الأحمرُ 401 عندَ طولِ التشغيلِ) عنِ الجذرِ (نموُّ زمنِ عبورِ الذرّيّةِ — علاجُهُ `WI-096`): فالرمزُ هنا يُسكُّ عندَ كلِّ قراءةٍ وقتَ الطلبِ فلا ينفدَ عمرُهُ (60 دقيقةً · `jwt_expire_minutes`) مهما طالَ التشغيلُ — **لا يغيّرُ الإنتاجَ ولا عمرَ الرمزِ** (رفعُ العمرِ مرفوضٌ بنصِّ التوجيهِ 15 § 1).
النطاق: حزمةُ فحوصِ الخدماتِ — 22 ملفًا كانت تُعرِّفُ `AUTH_HEADERS` بقاموسٍ ثابتٍ يُسكُّ رمزَهُ مرةً واحدةً عندَ الاستيرادِ.
المالك: Perplexity Computer (WI-097)
تاريخ الإنشاء: 2026-10-19
"""

from __future__ import annotations

from amos_federation.common.auth import ROLE_CITIZEN, create_access_token


class PerTestAuthHeaders(dict):
    """ترويساتُ `Authorization` تُسكُّ رمزًا جديدًا عندَ كلِّ قراءةٍ (WI-097).

    بديلُ القاموسِ الثابتِ الذي يُسكُّ رمزَهُ مرةً عندَ الاستيرادِ فيموتُ الرمزُ
    بعدَ 60 دقيقةَ تشغيلٍ (401) — هنا يُقرأُ الرمزُ وقتَ الطلبِ فيُصدَرُ جديدًا
    لكلِّ طلبٍ وحدَهُ. تُستعمَلُ في مواضعِ `headers=AUTH_HEADERS` نفسِها بلا
    تغييرِ مواضعِ الاستدعاءِ: فأيُّ قراءةٍ للقاموسِ (عنصرًا أو تكرارًا) تصدرُ
    رمزًا فتيًّا.
    """

    __slots__ = ("_subject", "_scopes", "_tenant_id", "_role")

    def __init__(
        self,
        subject: str,
        scopes: list[str],
        tenant_id: str | None = None,
        role: str = ROLE_CITIZEN,
    ) -> None:
        super().__init__()
        self._subject = subject
        self._scopes = list(scopes)
        self._tenant_id = tenant_id
        self._role = role

    def _authorization(self) -> str:
        """اسكِ رمزًا جديدًا الآن — لا تعتمدْ على رمزِ لحظةِ الاستيرادِ."""
        return "Bearer " + create_access_token(
            self._subject, self._scopes, self._tenant_id, role=self._role
        )

    def __getitem__(self, key: str) -> str:
        if key == "Authorization":
            return self._authorization()
        raise KeyError(key)

    def get(self, key: str, default=None):
        if key == "Authorization":
            return self._authorization()
        return default

    def items(self):
        return (("Authorization", self._authorization()),)

    def keys(self):
        return ("Authorization",)

    def values(self):
        return (self._authorization(),)

    def __iter__(self):
        return iter(("Authorization",))

    def __len__(self) -> int:
        return 1

    def __contains__(self, key: object) -> bool:
        return key == "Authorization"

    def copy(self) -> dict:
        return dict(self.items())
