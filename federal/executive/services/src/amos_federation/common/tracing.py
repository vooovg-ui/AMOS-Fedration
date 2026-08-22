"""
AMOS-Federation OpenTelemetry Tracing
الهدف: تتبع موزع لكل الطلبات عبر الخدمات عند توفر حزم OpenTelemetry
النطاق: كل الخدمات
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-15
"""

from typing import Any

import structlog


def setup_tracing(
    service_name: str = "amos-federation", otlp_endpoint: str = "http://localhost:4317"
) -> Any | None:
    """إعداد OpenTelemetry اختياريًا وإرجاع tracer أو None في البيئة الخفيفة."""
    try:
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
    except ImportError as exc:
        # التتبُّعُ المعطَّلُ **يُعلَنُ**: خدمةٌ بلا آثارٍ تبدو سليمةً في السجلِّ
        # وهي غيرُ مُراقَبةٍ — و`OBSERVED` معيارٌ في مصفوفةِ الحقيقة.
        structlog.get_logger().warning(
            "tracing.unavailable",
            service=service_name,
            reason=f"{type(exc).__name__}: {exc}",
            effect="لا آثارَ تُصدَّرُ — الخدمةُ غيرُ مُراقَبةٍ بالتتبُّع",
        )
        return None
    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    exporter = OTLPSpanExporter(endpoint=otlp_endpoint, insecure=True)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name)


#: سببُ غيابِ التتبُّعِ — يُكتَبُ مرّةً ويُقرأُ عندَ السؤالِ بدلَ الصمت.
_TRACER_UNAVAILABLE_REASON: str | None = None


def get_tracer(name: str = "amos-federation") -> Any | None:
    """الحصول على tracer متاح أو None عندما لا تكون مكتبة OpenTelemetry مثبّتة."""
    try:
        from opentelemetry import trace
    except ImportError as exc:
        # لا يُحذَّرُ في كلِّ نداءٍ (يُنادى في مساراتٍ حارّةٍ) بل يُقيَّدُ السببُ
        # في حالةٍ يقرأُها من يسألُ: أَغائبٌ لغيابِ الحزمةِ أم لخللٍ؟
        global _TRACER_UNAVAILABLE_REASON
        _TRACER_UNAVAILABLE_REASON = f"{type(exc).__name__}: {exc}"
        return None
    return trace.get_tracer(name)


def tracer_unavailable_reason() -> str | None:
    """سببُ غيابِ التتبُّعِ إن غابَ — يُقرأُ ولا يُخمَّن."""
    return _TRACER_UNAVAILABLE_REASON
