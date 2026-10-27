"""مسبارُ المقعدِ kimi_k3 (WI-117 · جولةُ W-701) — كسرُ حارسِ require_king عبرَ HTTP حقيقيٍّ.

يشغِّلُ الخدمتَينِ عبرَ uvicorn برمزِ مواطنٍ (role=citizen) ويطلبُ المساراتِ الأربعةِ
المحروسةَ (المعيارُ 1) فيتوقَّعُ الرفضَ 403 دونَ تغييرِ المستوى، ثمَّ برمزِ الملكِ
فيجتازُ (المعيارُ 3) — هذا مسبارٌ من عندِ المقعدِ لا من أوامرِ (ج) (§ 4.9).
"""

الهدف: مسبارُ المنسِّقِ — حارسُ require_king عبرَ HTTP حقيقيٍّ (uvicorn) على مساراتِ WI-117 الأربعةِ (جولةُ W-704).


from __future__ import annotations

import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "repo"))
sys.path.insert(0, str(BASE / "repo" / "federal" / "executive" / "services" / "src"))

from cryptography.hazmat.primitives.asymmetric import ed25519  # noqa: E402

from core.constitutional_engine.engine import ConstitutionalEngine  # noqa: E402
from core.constitutional_engine.ledger import ConstitutionalLedger  # noqa: E402

REPO = BASE / "repo"
SERVICES = REPO / "federal" / "executive" / "services"


def make_token(role: str, permissions: list[str]) -> str:
    """صنعُ رمزٍ وصولٍ موقَّعٍ بنمطِ auth.py (create_access_token) — مواطنٌ أو ملكٌ."""
    from amos_federation.common.auth import create_access_token

    return create_access_token(subject="probe-sub", scopes=permissions, tenant_id="federal", role=role)


def http_get(port: int, path: str, token: str | None, method: str = "GET") -> tuple[int, str]:
    req = urllib.request.Request(f"http://127.0.0.1:{port}{path}", method=method)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


def run_uvicorn(module: str, port: int) -> subprocess.Popen:
    proc = subprocess.Popen(
        [str(REPO / ".venv/bin/python"), "-m", "uvicorn", module, "--host", "127.0.0.1", "--port", str(port)],
        cwd=str(SERVICES),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc


def wait_ready(port: int, proc: subprocess.Popen, tries: int = 40) -> bool:
    for _ in range(tries):
        if proc.poll() is not None:
            return False
        try:
            http_get(port, "/health", None)
            return True
        except Exception:
            time.sleep(0.25)
    return False


def main() -> None:
    gov_port, console_port = 8711, 8712
    gov = run_uvicorn("amos_federation.services.governance.main:app", gov_port)
    console = run_uvicorn("amos_federation.services.control_console.main:app", console_port)
    try:
        if not wait_ready(gov_port, gov):
            print("FAIL: governance service failed to start")
            return
        if not wait_ready(console_port, console):
            print("FAIL: console service failed to start")
            return

        citizen = make_token("citizen", ["governance:read", "governance:write"])
        king = make_token("king", ["governance:read", "governance:write"])

        paths = [
            ("governance", "/v1/system/kill-switch/reset", "POST"),
            ("governance", "/v1/promotions", "POST"),
            ("governance", "/v1/promotions/p1/gates", "POST"),
            ("console", "/v1/kill-switch/reset", "POST"),
        ]

        for svc, path, method in paths:
            port = gov_port if svc == "governance" else console_port
            status, body = http_get(port, path, citizen, method)
            if status == 403:
                print(f"PASS: citizen rejected (403) on {svc} {path}")
            else:
                print(f"FAIL: citizen NOT rejected ({status}) on {svc} {path} — {body[:120]}")

            # المستوىُ لم يتغيّرْ بعدَ الرفضِ (المعيارُ 2 — شقُّ «دونَ تغييرِ المستوى»)
            st2, body2 = http_get(port, "/v1/system/kill-switch" if svc == "governance" else "/v1/kill-switch", citizen)
            print(f"  level after citizen attempt: {json.loads(body2).get('level') if body2.startswith('{') else 'n/a'}")

        # رمزُ الملكِ يمرُّ (المعيارُ 3) — على مسارٍ واحدٍ من كلِّ خدمةٍ (reset)
        for svc, path in [("governance", "/v1/system/kill-switch/reset"), ("console", "/v1/kill-switch/reset")]:
            port = gov_port if svc == "governance" else console_port
            status, body = http_get(port, path, king, "POST")
            if status in (200, 409, 422):
                print(f"PASS: king accepted ({status}) on {svc} {path}")
            else:
                print(f"FAIL: king rejected ({status}) on {svc} {path} — {body[:120]}")
    finally:
        gov.terminate()
        console.terminate()
        gov.wait(timeout=5)
        console.wait(timeout=5)


if __name__ == "__main__":
    main()
