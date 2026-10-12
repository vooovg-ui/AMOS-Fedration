"""
AMOS-Federation Memory Service
الهدف: تخزين واسترجاع الذاكرة التشغيلية والمعرفية — دائم بـ SQLAlchemy
النطاق: خدمة memory-service على المنفذ 8005
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
"""

from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status

from amos_federation.common.auth_context import require_context
from amos_federation.common.persistent import PersistentMemoryStore
from amos_federation.common.principal import (
    DEFAULT_TENANT,
    AuthorizationContext,
    TenantIsolationError,
    tenant_scope,
)
from amos_federation.common.registry import SERVICES
from amos_federation.common.schemas import MemoryQuery
from amos_federation.common.schemas import MemoryStore as MemoryStoreModel
from amos_federation.common.service import create_service_app

router = APIRouter(prefix="/v1", tags=["memory-service"])
memory_store = PersistentMemoryStore()

#: R6.1 — نوع الاعتماد الكانوني لهذه الخدمة.
#
# كانت هذه النقاط تُسقِط حمولة الرمز (`_: Annotated[..., Depends(require_auth)]`)
# وتقرأ `tenant_id` **من جسم الطلب**. أي أن المستأجر كان حقلًا يرسله العميل عن
# نفسه ثم يُصدَّق — وهو نفس عيب `actor_role` قبل R6، على البيانات هذه المرّة لا
# على الأدوات. فمن حمل رمزًا صالحًا لمستأجر «أ» كان يقرأ ذاكرة «ب» بتغيير حقل.
#
# الآن المستأجر من السياق المُشتقّ من الرمز الموقَّع، و`tenant_id` في جسم الطلب
# **يُهمَل إهمالًا تامًّا** (بقي في المخطَّط للتوافُق ولا يُقرأ).
Context = Annotated[AuthorizationContext, Depends(require_context)]


@router.post("/memory/store", response_model=dict)
async def store_memory(entry: MemoryStoreModel, context: Context) -> dict[str, Any]:
    """حفظ عنصر ذاكرة جديد — في مستأجر المبدأ لا في مستأجر يقوله الطلب.

    عيبٌ كُشِف في R6.1: كان النداء `store(key, value, entry.tenant_id)` وترتيب
    معاملات `PersistentMemoryStore.store` هو `(key, value, keywords, tenant_id)`.
    فكان المستأجر يُكتَب في عمود **الكلمات المفتاحية**، وكل صفٍّ يُخزَّن في
    `default` أيًّا كان ما أرسله الطلب. أي أن تقسيم الذاكرة بالمستأجر لم يكن
    عاملًا قبل هذا التغيير، وكان اختبار `test_tenant_isolation` يمرّ خاويًا:
    يبحث في `default` بينما لا شيء في `tenant_a` أصلًا. صار المُعامل مُسمّى.
    """
    try:
        return memory_store.store(
            entry.key, entry.value, tenant_id=context.tenant_id or DEFAULT_TENANT
        )
    except TenantIsolationError as exc:
        # مفتاحٌ يملكُه مستأجرٌ آخر: لا كتابةَ فوقَه ولا ذِكرَ لمالكِه (‏`WI-063`).
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="مفتاحُ الذاكرةِ محجوز"
        ) from exc


@router.post("/memory/query", response_model=list[dict])
async def query_memory(query: MemoryQuery, context: Context) -> list[dict[str, Any]]:
    """البحث في الذاكرة بنص استعلام — في نطاق مستأجر المبدأ."""
    results = memory_store.query(
        query.query, limit=query.limit, tenant_id=context.tenant_id or DEFAULT_TENANT
    )
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="لم يتم العثور على ذكريات مطابقة",
        )
    return results


@router.post("/memory/search", response_model=list[dict])
async def search_memory(query: MemoryQuery, context: Context) -> list[dict[str, Any]]:
    """بحث في الذاكرة — اسم بديل لـ /memory/query."""
    results = memory_store.query(
        query.query, limit=query.limit, tenant_id=context.tenant_id or DEFAULT_TENANT
    )
    return results  # قد تكون قائمة فارغة


@router.get("/memory/{key}", response_model=dict)
async def get_memory(key: str, context: Context) -> dict[str, Any]:
    """إرجاع عنصر ذاكرة بالمفتاح في نطاق مستأجر السياق.

    كانت `PersistentMemoryStore.get` تقرأ بالمفتاح وحده — دَينٌ مُعلَنٌ في وثيقة R6،
    وقِيسَ حيًّا على PostgreSQL في `DISC-089`: رمزُ مستأجرٍ قرأَ ذاكرةَ آخر. سُدَّ في
    `WI-063` بترشيحِ الاستعلامِ نفسِه، فذاكرةُ مستأجرٍ آخرَ 404 لا 403. ونظيرُ المخزنِ
    في الذاكرة (مخزنُ المتّجهاتِ العابر) لا تستعملُه هذه الخدمةُ ولم يُمَسّ.
    """
    item = memory_store.get(key, tenant_id=tenant_scope(context))
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="العنصر غير موجود")
    return item


@router.get("/memory/stats/summary", response_model=dict)
async def memory_stats(context: Context) -> dict[str, Any]:
    """إحصائيات الذاكرة."""
    stats = memory_store.stats(tenant_id=tenant_scope(context))
    return {
        "total_items": stats.get("total_entries", 0),
        "store_type": "persistent_sqlalchemy",
    }


_service = SERVICES["memory-service"]
app = create_service_app(
    _service["name"], _service["port"], "ذاكرة تشغيلية ومعرفية دائمة", [router]
)
