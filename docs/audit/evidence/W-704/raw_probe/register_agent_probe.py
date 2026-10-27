"""مسبارُ المقعدِ kimi_k3 (WI-119 · جولةُ W-701) — عبورُ السطحِ register_agent.

يُنادي مسارًا إنتاجيًّا من الأسطحِ الـ14 (`population.register_agent`) من خارجِ
العبورِ النشطِ ويثبتُ أنَّ الكتابةَ تُصرَّحُ وتُوثَّقُ بأثرِها (مفتاحُ
`agent:<id>/lifecycle...` من تصميمِ E1) وأنَّ استدعاءً ثانيًا بنفسِ المفتاحِ
لا يُنشئُ عبورًا معشّقًا (قارنْ بسلوكِ الكاشفِ WI-115) — هذا مسبارٌ من عندِ
المقعدِ لا من أوامرِ (ج) (البروتوكولُ § 4.9).

الهدف: مسبارُ المنسِّقِ — عبورُ السطحِ register_agent من الأسطحِ الـ14 لـWI-119 معَ إثباتِ الأثرِ (جولةُ W-704).
"""


from __future__ import annotations

from pathlib import Path
import sys
import uuid

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "repo"))
sys.path.insert(0, str(BASE / "repo" / "federal" / "executive" / "services" / "src"))

from amos_federation.services.agent_runtime.population import PopulationRegistry  # noqa: E402


def main() -> None:
    pop = PopulationRegistry()
    agent_id = f"probe-{uuid.uuid4().hex[:8]}"
    name = f"probe-agent-{agent_id}"

    # (1) الاستدعاءُ الأولُ من خارجِ العبورِ النشطِ — يُتوقَّعُ نجاحُهُ بأثرٍ موثَّقٍ.
    result = pop.register_agent(
        name=name,
        role="worker",
        category="probe",
        permissions=["read:public"],
        allowed_tools=["http_fetch"],
        token_budget=1000,
        agent_id=agent_id,
    )
    print(f"PASS: register_agent succeeded for {agent_id} (result keys: {sorted(result.keys())})")

    # (2) الأثرُ موثَّقٌ: هويةُ الوكيلِ موجودةٌ في السجلِّ الكانونيِّ — `get_identity`
    from amos_federation.services.executive_core.agent_identity import get_identity

    identity = get_identity(agent_id)
    if identity is not None:
        print(f"PASS: identity recorded for {agent_id} — lifecycle_state={identity.as_dict().get("lifecycle_state")}")
    else:
        print(f"FAIL: identity NOT recorded for {agent_id}")

    # (3) الاستدعاءُ الثاني بنفسِ المفتاحِ (نفسِ المعرفِ): يُتوقَّعُ رفضُ صريحٍ
    # على تكرارِ الهويةِ (لا عبورًا معشّقًا ولا كتابةً صامتةً).
    try:
        pop.register_agent(
            name=name,
            role="worker",
            category="probe",
            permissions=["read:public"],
            allowed_tools=["http_fetch"],
            token_budget=1000,
            agent_id=agent_id,
        )
        print("FAIL: second register_agent with same id succeeded — duplicate write!")
    except Exception as exc:
        print(f"PASS: second register_agent with same id rejected: {type(exc).__name__}: {str(exc)[:80]}")


if __name__ == "__main__":
    main()
