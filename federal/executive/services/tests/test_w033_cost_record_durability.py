"""
اختبارات W-033: سجلُّ المالِ دائمٌ · ويُكتَبُ فيه في مسارِ النداءِ
الهدف: إثباتُ أنَّ كلفةَ كلِّ نداءٍ تُقيَّدُ في جدولِ `model_cost_log` في مسارِ
       النداءِ نفسِه، وأنَّ `/v1/cost/summary` صارَ قراءةً فوقَ ذلك السجلِّ لا
       مخزنًا منافسًا — رقمٌ واحدٌ للمالِ لا اثنانِ — وأنَّ حدَّ تمثيلِ المالِ
       مقيسٌ مُعلَنٌ لا مسكوتٌ عنه.
النطاق: services/model-gateway · model_layer.cost_rows · GET /v1/cost/summary
المالك: federal/executive/services
تاريخ الإنشاء: 2026-08-23
بأيِّ سلطةٍ: حسمُ المالكِ Q-39 (ج) بتاريخ 2026-08-23 — «الدائمُ سجلًّا · ويُكتَبُ
             فيه في مسارِ النداءِ · والملخَّصُ المتطايرُ يُعادُ بناؤُه فوقَه لا
             يُنافِسُه».

## ما لا يُثبِتُه

لا يُثبِتُ صحّةَ **سعرِ** النموذجِ: في الخدمةِ جدولانِ للتسعيرِ
(`COST_PER_1K_TOKENS` في مسارِ النداءِ و`PRICING` في طبقةِ النماذجِ) وقد يختلفانِ
لنفسِ النموذجِ. وهذا سؤالُ مالٍ سياديٌّ قُيِّدَ **Q-42** ولم يُخترَعْ جوابُه هنا.
"""

from __future__ import annotations

import importlib
from typing import Any

import pytest
from fastapi.testclient import TestClient

model_gateway_main = importlib.import_module("amos_federation.services.model_gateway.main")
model_layer_module = importlib.import_module("amos_federation.services.model_gateway.model_layer")


@pytest.fixture()
def client() -> TestClient:
    """عميلُ خدمةِ بوّابةِ النماذجِ بتطبيقِها الحقيقيِّ لا بمُحاكاةٍ."""
    return TestClient(model_gateway_main.app)


@pytest.fixture()
def auth_headers() -> dict[str, str]:
    """ترويسةُ تصريحٍ كما تفعلُ حزمةُ الخدمةِ القائمةُ — لا تُخترَعُ طريقةٌ ثانيةٌ."""
    from amos_federation.common.auth import create_access_token

    token = create_access_token("w033-prover", ["*"])
    return {"Authorization": f"Bearer {token}"}


def _invoke(client: TestClient, headers: dict[str, str], prompt: str) -> dict[str, Any]:
    response = client.post("/v1/models/invoke", headers=headers, json={"prompt": prompt})
    assert response.status_code == 200, response.text
    return response.json()


# =============================================================================
# 1) الكتابةُ في مسارِ النداءِ وفي السجلِّ الدائمِ نفسِه
# =============================================================================
def test_invoking_a_model_writes_a_row_in_the_durable_record(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    """نداءٌ واحدٌ يُضيفُ قيدًا واحدًا في `model_cost_log` — لا في قائمةِ ذاكرةٍ."""
    layer = model_layer_module.get_model_layer()
    before = len(layer.cost_rows())
    response = _invoke(client, auth_headers, "قِسْ كلفةَ نداءٍ واحدٍ")
    rows = layer.cost_rows()
    assert len(rows) == before + 1, "النداءُ لم يُقيَّدْ في السجلِّ الدائمِ."
    row = rows[-1]
    assert (
        row["tokens"] == response["tokens_used"]
    ), "رموزُ القيدِ تخالفُ رموزَ الردِّ — القيدُ ليس عن هذا النداءِ."
    assert row["model"] == response["model_used"]
    assert row["cost_usd"] == pytest.approx(
        response["cost_usd"], abs=1e-4
    ), "كلفةُ القيدِ تخالفُ كلفةَ الردِّ بأكثرَ من دقّةِ عقدِ المالِ."
    assert row["latency_ms"] == response["latency_ms"]
    assert row["source"] in ("external", "local_fallback")
    # ولا يُشترَطُ هنا أن تكونَ الكلفةُ فوقَ الصفرِ: النموذجُ الاحتياطيُّ المحليُّ
    # سعرُه **صفرٌ مُعلَنٌ** في `COST_PER_1K_TOKENS`، فصفرٌ صادقٌ لا نقصُ قياسٍ.
    # وحدُّ التمثيلِ نفسُه مقيسٌ في فحصٍ مستقلٍّ أدناه.
    assert row["cost_usd"] >= 0


def test_the_volatile_list_no_longer_exists_in_the_source(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    """حرسٌ على الشِفرةِ نفسِها: لا قائمةَ تكلفةٍ في ذاكرةِ الخدمةِ."""
    assert not hasattr(
        model_gateway_main, "_cost_log"
    ), "عادَ سجلُّ التكلفةِ قائمةً في الذاكرةِ — نقضٌ لحسمِ Q-39 (ج)."


def test_the_service_declares_its_money_store_as_durable() -> None:
    """الإعلانُ في الشِفرةِ لا في وثيقةٍ، ومخزنُ الظلِّ يبقى مُعلَنَ التطايرِ."""
    assert model_gateway_main.COST_STORE_DURABILITY == "durable_record"
    assert (
        model_gateway_main.STORE_DURABILITY == "in_memory_volatile"
    ), "مخزنُ الظلِّ لم يُدَمْ في W-033، فإعلانُه المتطايرُ صدقٌ لا يُبدَّلُ بالقياسِ."


# =============================================================================
# 2) رقمٌ واحدٌ للمالِ — الملخَّصُ يُعادُ بناؤُه فوقَ السجلِّ لا يُنافِسُه
# =============================================================================
def test_both_money_endpoints_report_the_same_count(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    """`/v1/cost/summary` و`/v1/models/cost-summary` قراءتانِ لحقيقةٍ واحدةٍ."""
    _invoke(client, auth_headers, "نداءٌ يُقارَنُ به المصدرانِ")
    summary = client.get("/v1/cost/summary", headers=auth_headers).json()
    persistent = client.get("/v1/models/cost-summary", headers=auth_headers).json()
    assert (
        summary["total_invocations"] == persistent["total_invocations"]
    ), "رقمانِ مختلفانِ للمالِ في واجهةٍ واحدةٍ — نقضٌ لحسمِ Q-39 (ج)."
    assert summary["total_cost_usd"] == pytest.approx(
        persistent["total_cost_usd"], rel=1e-6
    ), "كلفتانِ مختلفتانِ للمالِ نفسِه."


def test_the_published_shape_of_the_summary_did_not_change(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    """لم يُحذَفْ مفتاحٌ منشورٌ: حذفُه عقدٌ مع مُستهلِكيه لا حكمُ عاملٍ."""
    _invoke(client, auth_headers, "نداءٌ يُتحقَّقُ به شكلُ الخرجِ")
    summary = client.get("/v1/cost/summary", headers=auth_headers).json()
    for key in (
        "total_invocations",
        "total_cost_usd",
        "by_model",
        "store_type",
        "persistent_source",
    ):
        assert key in summary, f"المفتاحُ المنشورُ {key} حُذِفَ من خرجِ النقطةِ."
    assert summary["store_type"] == "durable_record", "إعلانُ الإدامةِ في الخرجِ لم يصدُقْ بعدَ الإدامةِ."
    assert summary["persistent_source"] == "/v1/models/cost-summary"
    model_entry = next(iter(summary["by_model"].values()))
    for key in ("invocations", "total_tokens", "total_cost"):
        assert key in model_entry, f"مفتاحُ التفصيلِ {key} حُذِفَ."


def test_by_model_breakdown_is_rebuilt_from_the_rows(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    """تفصيلُ النماذجِ محسوبٌ من الصفوفِ لا من عدَّادٍ ثانٍ يُصانُ بيدٍ."""
    layer = model_layer_module.get_model_layer()
    _invoke(client, auth_headers, "نداءٌ يُتحقَّقُ به التفصيلُ")
    rows = layer.cost_rows()
    summary = client.get("/v1/cost/summary", headers=auth_headers).json()
    expected_invocations: dict[str, int] = {}
    for row in rows:
        expected_invocations[row["model"]] = expected_invocations.get(row["model"], 0) + 1
    for model, count in expected_invocations.items():
        assert (
            summary["by_model"][model]["invocations"] == count
        ), f"عددُ نداءاتِ {model} في الملخَّصِ يخالفُ صفوفَ السجلِّ."
    assert summary["total_invocations"] == len(rows)


# =============================================================================
# 3) الإدامةُ نفسُها: قيدُ المالِ يبقى بعدَ إقلاعٍ جديدٍ
# =============================================================================
def test_the_money_row_survives_a_fresh_reader(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    """قارئٌ جديدٌ — طبقةٌ جديدةٌ على القاعدةِ نفسِها — يرى القيدَ.

    وهذا هو معنى النجاةِ في مِسبارِ الإقلاعِ مُصغَّرًا: القيدُ في القاعدةِ لا في
    ذاكرةِ العمليّةِ التي كتبَتْه.
    """
    _invoke(client, auth_headers, "نداءٌ يُقرأُ بعدَ إقلاعٍ")
    fresh = model_layer_module.ModelLayer()
    rows = fresh.cost_rows()
    assert rows, "القيدُ لم يُرَ من طبقةٍ جديدةٍ — لم تكن كتابةً دائمةً."
    assert rows[-1]["invocation_id"].startswith("inv-"), "معرِّفُ النداءِ ليس من مسارِ النداءِ."


def test_cost_rows_never_invent_a_value(client: TestClient, auth_headers: dict[str, str]) -> None:
    """كلُّ حقلٍ في الصفِّ مقروءٌ من العمودِ، ولا قيمةَ افتراضيّةً تُختلَقُ."""
    layer = model_layer_module.get_model_layer()
    layer.log_cost(
        invocation_id="inv-w033-fidelity",
        model="claude-opus-4",
        tokens=4242,
        cost_usd=7.77,
        latency_ms=333,
        source="local_fallback",
    )
    row = next(r for r in layer.cost_rows() if r["invocation_id"] == "inv-w033-fidelity")
    assert row["model"] == "claude-opus-4"
    assert row["tokens"] == 4242
    assert row["cost_usd"] == pytest.approx(7.77, rel=1e-9)
    assert row["latency_ms"] == 333
    assert row["source"] == "local_fallback"
    assert row["created_at"], "قيدُ مالٍ بلا وقتٍ — لا يُراجَعُ."


def test_sub_scale_cost_is_recorded_as_zero_and_that_is_declared() -> None:
    """حدُّ تمثيلِ المالِ مقيسٌ لا مسكوتٌ عنه — وهو مادّةُ **Q-42** لا إصلاحُ عاملٍ.

    عقدُ المالِ `NUMERIC(20,4)` (قرارُ Q-20 · هجرةُ 014)، وكلفةُ نداءٍ صغيرٍ قد
    تكونُ أقلَّ من `0.00005$` فتُقيَّدُ **صفرًا** حينَ يُحوَّلُ العائمُ إلى مبلغٍ.
    وقبلَ W-033 كانَ هذا الصفرُ في جدولٍ لا يقرأُه ملخَّصُ `/v1/cost/summary`؛
    وبعدَه صارَ الجدولُ مصدرَ الرقمِ المنشورِ — فالحدُّ صارَ **ظاهرًا في الواجهةِ**.

    ولم يُوسَّعْ مقياسُ المالِ ولم يُبدَّلْ نوعُه: ذلك عقدُ مالٍ لا حكمُ عاملٍ،
    وقُيِّدَ سؤالًا (**Q-42**). وهذا الفحصُ يُثبِّتُ الحدَّ كما هو، فإن غُيِّرَ
    المقياسُ يومًا سقطَ الفحصُ ولزمَ قرارٌ مكتوبٌ — لا انحرافٌ صامتٌ.
    """
    convert = model_layer_module._money_from_provider_float
    assert str(convert(0.00003)) == "0.0000", "تغيَّرَ سلوكُ تمثيلِ المالِ بلا قرارٍ مكتوبٍ."
    assert str(convert(0.0003)) == "0.0003"
    assert str(convert(7.77)) == "7.7700"
