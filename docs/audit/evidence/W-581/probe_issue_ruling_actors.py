"""
الهدف: قياسُ حكمِ الحدِّ السياديِّ على الفعلِ issue_ruling لكلِّ فاعلٍ — مسارُ التنفيذِ الكاملُ لا المراجعةُ وحدَها (DISC-121 · وثيقةُ تصميمِ J1)
النطاق: docs/audit/evidence/W-581 — سكربتُ قياسٍ لا يكتبُ في قاعدةِ بياناتٍ (المُطبِّقُ يُسجِّلُ نداءَه في قائمةٍ فقط)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — قيدُ W-581
تاريخ الإنشاء: 2026-10-21

التشغيل (من جذرِ المستودع):
  AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER=$(mktemp -u) PYTHONPATH=federal/executive/services/src:. \
    .venv/bin/python docs/audit/evidence/W-581/probe_issue_ruling_actors.py
"""

from __future__ import annotations

from amos_federation.services.executive_core.sovereignty_bridge import (
    ConstitutionalAuthorizer,
    compensator,
    declared_effect,
    operation_key,
)
from core.sovereignty.jurisdiction import JudicialAction

ACTORS = ("JUDICIAL", "EXECUTIVE", "LEGISLATIVE", "TREASURY", "AGENT", "SYSTEM")


def main() -> None:
    print("## (أ) review_only — المراجعةُ بلا تنفيذ")
    for actor in ACTORS:
        ev = ConstitutionalAuthorizer(actor=actor).review_only(
            "issue_ruling", "judiciary/rulings/review/FIRST_INSTANCE"
        )
        print(f"{actor:<12} {ev.decision:<6} layer={ev.authority_layer}")

    print("## (ب) guard_declared عبرَ الجسرِ — بلا طلبِ اختصاصٍ (الجسرُ لا يقبلُه اليومَ)")
    for i, actor in enumerate(ACTORS):
        a = ConstitutionalAuthorizer(actor=actor)
        t = f"judiciary/rulings/bridge{i}/FIRST_INSTANCE"
        e = declared_effect("CREATE", t, "probe")
        try:
            a.guard_declared(
                "issue_ruling", t, declared_effects=(e,), applier=lambda _e: None,
                operation_key=operation_key("probe.w579.bridge", str(i)),
                compensators=(compensator(e.signature, lambda: True, "probe"),),
            )
            print(f"{actor:<12} EXECUTED")
        except Exception as ex:  # noqa: BLE001 — القياسُ يطبعُ نوعَ الرفضِ
            print(f"{actor:<12} REFUSED {type(ex).__name__}")

    print("## (ج) الحدُّ الجوهريُّ boundary.execute بطلبِ اختصاصٍ FEDERAL/FEDERAL/FEDERAL ومُعوِّض")
    for i, actor in enumerate(ACTORS):
        a = ConstitutionalAuthorizer(actor=actor)
        t = f"judiciary/rulings/core{i}/FIRST_INSTANCE"
        e = declared_effect("CREATE", t, "probe")
        hit: list[int] = []
        ja = JudicialAction(action="issue_ruling", court_scope="FEDERAL",
                            case_scope="FEDERAL", actor_scope="FEDERAL", target=t)
        try:
            a.boundary.execute(
                a._request("issue_ruling", t, None),
                declared_effects=(e,), planner=lambda _p, e=e: (e,),
                applier=lambda _e: hit.append(1),
                operation_key=operation_key("probe.w579.core", str(i)),
                compensators=(compensator(e.signature, lambda: True, "probe"),),
                judicial_action=ja,
            )
            print(f"{actor:<12} EXECUTED applier_called={bool(hit)}")
        except Exception as ex:  # noqa: BLE001
            print(f"{actor:<12} REFUSED {type(ex).__name__}")


if __name__ == "__main__":
    main()
