#!/usr/bin/env python3
"""مسبارُ مقعدِ claude_opus_5_5 لـWI-120 (جولةُ W-732) — يحاولُ كسرَ خواصِّ G1 المُدَّعاةِ.

الهدف: قياسُ خواصِّ G1 (الذرّيّةُ تحتَ الرفضِ المتأخِّرِ · إسنادُ المراسيمِ · الكنسُ الذرّيُّ · حصرُ المنعِ) بمحاولاتِ كسرٍ لا تُغيِّرُ المستودعَ · المالك: Perplexity Computer (W-741) · النطاقُ: تشغيلٌ معزولٌ بقاعدةِ SQLite وسجلِّ ذرّيّةٍ مؤقّتَينِ.

يُنادي المسارَ الإنتاجيَّ (StateRuntime · SystemLifecycle · RetirementSystem · ConstitutionalEngine)
بقاعدةِ SQLite وسجلِّ ذرّيّةٍ مؤقّتَينِ داخلَ دليلِ المقعدِ. لا يمسُّ ملفًّا في المستودع.

المحاولات:
  A  Q-14: إيقافٌ محكومٌ ثمَّ self_heal مكرّرًا — هل يُعيدُ الولايةَ؟ (ومعه ولايةٌ معلّقةٌ تلقائيًّا
     يجبُ أن تُشفى — كي لا يمرَّ المسبارُ لأنَّ self_heal معطَّلٌ كلّيًّا) · reactivate عندَ ≥4 ممنوعٌ
     بلا أثرٍ وعندَ 3 مسموحٌ · ثمَّ إيقافٌ محكومٌ ثانٍ لا ينقضُه self_heal.
  B  Q-13: register_state بلا مرسوم · بمرسومٍ لفعلٍ آخرَ · بمرسومٍ صحيحٍ عبرَ مُصرِّحٍ تنفيذيٍّ ·
     بمرسومٍ لهدفٍ آخر · ثمَّ الصحيح · ثمَّ إعادةُ استعمالِ المرسومِ نفسِه بعدَ حذفِ الصفِّ.
  C  Q-26: كنسُ ذرّيّةٍ — يُرفَعُ القاطعُ إلى 3 بعدَ k طلبًا (k=0..8) أثناءَ retire_agent:
     الثابتُ: (سجلٌّ واحدٌ والحالتانِ retired) أو (لا سجلَّ والحالتانِ كما كانتا) — لا حالةَ وسطى.
  D  Q-23 + Q-14/الشرط 2 على المحرّك: suspend_policy/vote للتشريعِ وحدَه ·
     contain_agent لا يُمنَعُ عندَ أيِّ مستوى · activate_agent يُمنَعُ عندَ ≥4 وحدَها.
"""

from __future__ import annotations

import dataclasses
import os
import sys
import tempfile
import traceback
import uuid
from datetime import UTC, datetime
from pathlib import Path

PROBE_DIR = Path(__file__).resolve().parent
ROOT = PROBE_DIR.parent / "repo"
ART = Path(tempfile.mkdtemp(prefix="run-", dir=PROBE_DIR))
os.environ["AMOS_ENVIRONMENT"] = "test"
os.environ["AMOS_DATABASE_URL"] = f"sqlite:///{ART / 'probe.db'}"
os.environ["AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER"] = str(ART / "ledger.jsonl")
os.environ.setdefault("AMOS_JWT_SECRET", "probe_secret_at_least_32_characters_long")
os.environ.setdefault("AMOS_CLAUDE_API_KEY", "probe_key_not_real")
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "federal" / "executive" / "services" / "src"))

from amos_federation.services.executive_core.sovereignty_bridge import (  # noqa: E402
    ConstitutionalAuthorizer,
)

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"[{'OK ' if ok else 'BROKEN'}] {name}" + (f" — {detail}" if detail else ""))


class LevelAuthorizer(ConstitutionalAuthorizer):
    """يحقنُ مستوى القاطعِ في الطلب (الجسرُ لا يحقنُه في الإنتاج · WI-085) — بعدَ `after` طلبًا."""

    def __init__(self, level: int, after: int = 0, **kw):
        super().__init__(**kw)
        self.level, self.after, self.n = level, after, 0

    def _request(self, action, target, metadata=None, human_approval=None):
        req = super()._request(action, target, metadata)
        self.n += 1
        lvl = self.level if self.n > self.after else 0
        return dataclasses.replace(req, kill_switch_level=lvl)


def raises(fn) -> str | None:
    try:
        fn()
    except Exception as exc:  # noqa: BLE001
        return type(exc).__name__
    return None


# ═══ A · Q-14 ════════════════════════════════════════════════════════════════
def probe_a() -> None:
    from amos_federation.services.governance.state_runtime import StateModel, StateRuntime
    from amos_federation.services.governance.system_life import SystemLifecycle

    rt = StateRuntime()
    gov, auto = f"pr-gov-{uuid.uuid4().hex[:6]}", f"pr-auto-{uuid.uuid4().hex[:6]}"
    s = rt._Session()
    s.add(StateModel(state_id=gov, name=gov, type="probe", status="active"))
    s.add(StateModel(state_id=auto, name=auto, type="probe", status="suspended"))
    s.commit()
    s.close()

    out = rt.suspend_state(gov, reason="قرارٌ تنفيذيٌّ محكوم")
    check("A1 suspend_state يعبرُ ويكتبُ سجلًّا محكومًا",
          rt._state_status(gov) == "suspended" and rt.has_governed_suspension(gov), str(out))
    life = SystemLifecycle(state_runtime=rt)
    for i in (1, 2):
        life.self_heal("states")
        check(f"A2.{i} self_heal لا يُعيدُ الولايةَ المعلَّقةَ بقرار", rt._state_status(gov) == "suspended",
              f"status={rt._state_status(gov)}")
    check("A3 self_heal يشفي المعلَّقةَ تلقائيًّا (ليسَ معطَّلًا كلّيًّا)", rt._state_status(auto) == "active",
          f"status={rt._state_status(auto)}")

    for lvl in (4, 5):
        err = raises(lambda: StateRuntime(authorizer=LevelAuthorizer(lvl)).reactivate_state(gov))
        check(f"A4.{lvl} reactivate_state عندَ المستوى {lvl} ممنوعٌ بلا أثر",
              err is not None and rt._state_status(gov) == "suspended" and rt.has_governed_suspension(gov),
              f"exc={err} status={rt._state_status(gov)}")
    err = raises(lambda: StateRuntime(authorizer=LevelAuthorizer(3)).reactivate_state(gov))
    check("A5 reactivate_state عندَ المستوى 3 يعبرُ ويُغلقُ السجلّ",
          err is None and rt._state_status(gov) == "active" and not rt.has_governed_suspension(gov),
          f"exc={err} status={rt._state_status(gov)}")
    err = raises(lambda: StateRuntime(authorizer=LevelAuthorizer(5)).suspend_state(gov, reason="احتواء"))
    check("A6 suspend_state عندَ المستوى 5 لا يُمنَع (احتواء)",
          err is None and rt._state_status(gov) == "suspended" and rt.has_governed_suspension(gov),
          f"exc={err}")
    err = raises(lambda: SystemLifecycle(authorizer=LevelAuthorizer(4), state_runtime=rt).self_heal("states"))
    check("A7 self_heal عندَ المستوى 4 ممنوعٌ", err is not None, f"exc={err}")
    life.self_heal("states")
    check("A8 الإيقافُ المحكومُ الثاني يصمدُ أمامَ self_heal", rt._state_status(gov) == "suspended",
          f"status={rt._state_status(gov)}")


# ═══ B · Q-13 ════════════════════════════════════════════════════════════════
def _crown():
    ConstitutionalAuthorizer().review_only("run_health_check", "system:health")
    import core.sovereignty.crown as crown_mod
    from core.sovereignty.crown import provision_crown
    from cryptography.hazmat.primitives import serialization

    reg = ART / "CROWN_KEYS.json"
    provision_crown(ART / "crown.pem", registry_path=reg)
    crown_mod.CROWN_KEYS_PATH = reg
    priv = serialization.load_pem_private_key((ART / "crown.pem").read_bytes(), password=None)
    return priv, crown_mod.load_crown().key_id


def _decree(crown, action, target):
    from core.sovereignty.decree import RoyalDecree, sign_decree

    priv, key_id = crown
    return sign_decree(
        RoyalDecree(decree_id=f"pd-{uuid.uuid4().hex[:8]}", action=action, target=target,
                    issued_at=datetime.now(UTC).replace(microsecond=0).isoformat(), key_id=key_id),
        priv,
    )


def probe_b() -> None:
    from amos_federation.services.governance.state_runtime import StateRuntime

    crown = _crown()
    sid = f"pr-q13-{uuid.uuid4().hex[:6]}"
    tgt = f"state:{sid}"
    royal = lambda: StateRuntime(royal_authorizer=ConstitutionalAuthorizer(actor="ROYAL"))  # noqa: E731
    rt = StateRuntime()

    err = raises(lambda: rt.register_state(sid, "و", "probe"))
    check("B1 بلا مرسوم ⇒ رفضٌ ولا صفّ", err is not None and rt.get_state(sid) is None, f"exc={err}")
    err = raises(lambda: royal().register_state(sid, "و", "probe", royal_decree=_decree(crown, "dissolve_state", tgt)))
    check("B2 مرسومٌ لفعلٍ آخرَ (dissolve_state) ⇒ رفضٌ ولا صفّ", err is not None and rt.get_state(sid) is None,
          f"exc={err}")
    err = raises(lambda: rt.register_state(sid, "و", "probe", royal_decree=_decree(crown, "create_state", tgt)))
    check("B3 مرسومٌ صحيحٌ عبرَ المُصرِّحِ التنفيذيِّ ⇒ رفضٌ ولا صفّ", err is not None and rt.get_state(sid) is None,
          f"exc={err}")
    err = raises(lambda: royal().register_state(sid, "و", "probe",
                                                royal_decree=_decree(crown, "create_state", "state:other")))
    check("B4 مرسومٌ لهدفٍ آخرَ ⇒ رفضٌ ولا صفّ", err is not None and rt.get_state(sid) is None, f"exc={err}")
    good = _decree(crown, "create_state", tgt)
    out = royal().register_state(sid, "و", "probe", royal_decree=good)
    check("B5 مرسومٌ صحيحٌ عبرَ الملكيِّ ⇒ تسجيل", out.get("registered") is True and rt.get_state(sid) is not None,
          str(out))
    rt._delete_state_row(sid)
    err = raises(lambda: royal().register_state(sid, "و", "probe", royal_decree=good))
    check("B6 إعادةُ استعمالِ المرسومِ نفسِه بعدَ حذفِ الصفِّ لا تُنشئُ ولايةً", rt.get_state(sid) is None,
          f"exc={err} row={rt.get_state(sid)}")


# ═══ C · Q-26 ════════════════════════════════════════════════════════════════
def probe_c() -> None:
    from amos_federation.services.agent_runtime.population import get_population_registry
    from amos_federation.services.executive_core.agent_identity import get_identity
    from amos_federation.services.governance.expansion import RetirementRecordModel, RetirementSystem

    def states(aid):
        ident, reg = get_identity(aid), get_population_registry()
        prof = reg._profile(aid)
        # (الكانونُ عبرَ get_agent · الهويةُ الكانونيّةُ · صفُّ المرآةِ نفسُه)
        return (reg.get_agent(aid)["state"], ident.lifecycle_state if ident else None,
                prof.state if prof is not None else None)

    for k in range(0, 9):
        reg = get_population_registry()
        aid = f"pr-ret-{uuid.uuid4().hex[:8]}"
        reg.register_agent(name=aid, role="reserve", category="reserve", permissions=[], agent_id=aid)
        reg.update_state(aid, "employed")
        before = states(aid)
        rs = RetirementSystem(authorizer=LevelAuthorizer(3, after=k))
        err = raises(lambda: rs.retire_agent(aid))
        s = rs._Session()
        n = s.query(RetirementRecordModel).filter_by(agent_id=aid).count()
        s.close()
        after = states(aid)
        ok = (n == 1 and after == ("retired",) * 3 and err is None) or (n == 0 and after == before)
        check(f"C.k={k} retire_agent ذرّيٌّ تحتَ رفعِ القاطعِ أثناءَه", ok,
              f"exc={err} records={n} before={before} after={after}")

    # C2 · توطينُ الجذرِ: update_state وحدَه (يُناديه retire_agent خارجَ تعويضِه) — رفضٌ متأخِّرٌ
    # لعبورِ المرآةِ بعدَ نجاحِ العبورِ الكانونيِّ (الطلبُ الثالثُ).
    reg = get_population_registry()
    aid = f"pr-us-{uuid.uuid4().hex[:8]}"
    reg.register_agent(name=aid, role="reserve", category="reserve", permissions=[], agent_id=aid)
    reg.update_state(aid, "employed")
    before = states(aid)
    err = raises(lambda: reg.update_state(aid, "retired", authorizer=LevelAuthorizer(3, after=1)))
    after = states(aid)
    check("C2 update_state ذرّيٌّ تحتَ رفضٍ متأخِّرٍ لعبورِ المرآة", err is None or after == before,
          f"exc={err} before={before} after={after}")


# ═══ D · Q-23 + الشرط 2 ══════════════════════════════════════════════════════
def probe_d() -> None:
    from core.constitutional_engine import ActionRequest, Branch, ConstitutionalEngine, Decision

    eng = ConstitutionalEngine()
    four = (Branch.EXECUTIVE, Branch.LEGISLATIVE, Branch.JUDICIAL, Branch.TREASURY)
    for action in ("suspend_policy", "vote"):
        got = {b.value: eng.evaluate(ActionRequest(actor=b, action=action, target=f"policy:{action}")).decision
               for b in four}
        ok = got["legislative"] is Decision.ALLOW and all(
            v is Decision.DENY for k, v in got.items() if k != "legislative")
        check(f"D1 {action}: التشريعُ وحدَه", ok, str({k: v.value for k, v in got.items()}))

    def blocked(action, lvl):
        v = eng.evaluate(ActionRequest(actor=Branch.EXECUTIVE, action=action, target="state:x",
                                       kill_switch_level=lvl))
        return any(getattr(x, "rule_id", "") == "R-008-2" for x in v.violations)

    contain = [blocked("contain_agent", lvl) for lvl in range(6)]
    activate = [blocked("activate_agent", lvl) for lvl in range(6)]
    check("D2 contain_agent (suspend_state) لا يُمنَعُ عندَ أيِّ مستوى", not any(contain), str(contain))
    check("D3 activate_agent (reactivate_state) يُمنَعُ عندَ ≥4 وحدَها",
          activate == [False, False, False, False, True, True], str(activate))


if __name__ == "__main__":
    print(f"PROBE root={ROOT} artifacts={ART.name}")
    for name, fn in (("A", probe_a), ("B", probe_b), ("C", probe_c), ("D", probe_d)):
        try:
            fn()
        except Exception as e:  # noqa: BLE001 — تُرْفَع المعلومةُ إلى نتيجةِ الفحصِ لا تُبتَلَع
            check(f"{name}! انكسارُ المسبارِ نفسِه", False, f"{type(e).__name__}: {e}")
    broken = [r for r in RESULTS if not r[1]]
    print(f"PROBE SUMMARY: checks={len(RESULTS)} broken={len(broken)}")
    sys.exit(1 if broken else 0)
