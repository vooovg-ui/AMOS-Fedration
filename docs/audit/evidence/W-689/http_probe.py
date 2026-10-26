"""مسبارُ HTTP حقيقيٌّ لحارسِ require_king على المساراتِ الخمسةِ — WI-117 (قياسُ ما بعدَ التحصين).

الهدف:
    يُشغِّلُ خدمتَي governance وcontrol_console بـuvicorn في عمليّتَينِ منفصلتَين على منفذَينِ
    محلّيَّين، ويُرسلُ طلباتِ HTTP حقيقيّةً بـurllib (لا TestClient)، ويطبعُ رمزَ الحالةِ والجسمَ حرفيًّا:
    الملكُ يرفعُ التوقّفَ ويوقّعُ (200) — والمواطنُ يُصدُّ على المساراتِ الخمسةِ (403)
    ويبقى المستوى halt.

النطاق:
    دليلٌ لا شفرةٌ إنتاجيّة. سرُّ التوقيعِ يُولَّدُ عشوائيًّا لكلِّ تشغيلٍ (لا سرَّ مكتوبًا)،
    وقاعدةُ البياناتِ SQLite مؤقّتة. معيارُ النجاحِ من تصميمِ W-687 § 3:
    مواطنٌ ⇒ 403 ×5 والمستوى halt باقيًا، والملكُ ⇒ 200 في الخمسةِ.

المالك: WI-117 (دليلُ W-689) · المنسِّقُ GLM-5.3
تاريخ الإنشاء: 2026-10-26
"""

from __future__ import annotations

import json
import os
import secrets
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

_JWT_KEY = secrets.token_urlsafe(48)


def _port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def _call(
    method: str, url: str, token: str, body: dict | None = None
) -> tuple[int, str]:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def main() -> int:
    db = tempfile.mktemp(suffix=".db", prefix="amos_probe_")
    env = {
        **os.environ,
        "AMOS_JWT_SECRET": _JWT_KEY,
        "AMOS_DATABASE_URL": f"sqlite:///{db}",
        "AMOS_ENVIRONMENT": "test",
        "OTEL_SDK_DISABLED": "true",
    }
    os.environ.update(env)
    from amos_federation.common.auth import (
        ROLE_CITIZEN,
        create_access_token,
        create_king_token,
    )

    citizen = create_access_token("citizen-probe", scopes=[], role=ROLE_CITIZEN)
    king = create_king_token()
    procs, base = [], {}
    for name, mod in (
        ("governance", "amos_federation.services.governance.main:app"),
        ("console", "amos_federation.services.control_console.main:app"),
    ):
        port = _port()
        procs.append(
            subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "uvicorn",
                    mod,
                    "--host",
                    "127.0.0.1",
                    "--port",
                    str(port),
                    "--log-level",
                    "warning",
                ],
                env=env,
            )
        )
        base[name] = f"http://127.0.0.1:{port}"
    try:
        for b in base.values():
            last_err: Exception | None = None
            for _ in range(100):
                try:
                    urllib.request.urlopen(b + "/health", timeout=1)
                    last_err = None
                    break
                except OSError as exc:
                    last_err = exc
                    time.sleep(0.2)
            if last_err is not None:
                raise RuntimeError(f"service at {b} never became healthy: {last_err!r}")
        g, c = base["governance"], base["console"]

        def show(label: str, method: str, url: str, tok: str, body: dict | None) -> tuple[int, str]:
            code, text = _call(method, url, tok, body)
            disp = url.replace(g, "<governance>").replace(c, "<console>")
            payload = " " + json.dumps(body, ensure_ascii=False) if body is not None else ""
            print(f"### {label}\n$ {method} {disp}{payload}\n-> {code} {text}\n")
            return code, text

        # 1) الملكُ يرفعُ halt — قياسُ نقطةِ البدايةِ.
        code, _ = show(
            "king raises halt (governance)",
            "POST",
            g + "/v1/system/kill-switch",
            king,
            {"level": "halt", "reason": "probe", "activated_by": "king"},
        )
        assert code == 200, "king activate must succeed"

        # 2) المواطنُ على المساراتِ الخمسةِ — كلُّها 403 والمستوى halt باقيًا.
        show(
            "CITIZEN reset (governance main.py:147 · guard require_king)",
            "POST",
            g + "/v1/system/kill-switch/reset",
            citizen,
            None,
        )
        code, text = show(
            "status after citizen governance reset",
            "GET",
            g + "/v1/system/status",
            king,
            None,
        )
        assert "halt" in text, "level must stay halt after citizen reset attempt"
        show(
            "CITIZEN reset (control_console main.py:209 · guard require_king)",
            "POST",
            c + "/v1/kill-switch/reset",
            citizen,
            None,
        )
        code, text = show(
            "status after citizen console reset",
            "GET",
            g + "/v1/system/status",
            king,
            None,
        )
        assert "halt" in text, "level must stay halt after citizen console reset attempt"
        show(
            "CITIZEN creates promotion (governance main.py:167 · guard require_king)",
            "POST",
            g + "/v1/promotions",
            citizen,
            {"model_id": "probe-model"},
        )
        code, text = show(
            "CITIZEN passes gate (governance main.py:199 · guard require_king)",
            "POST",
            g + "/v1/promotions/probe-promo/gates",
            citizen,
            {"gate_name": "human_approval", "passed": True, "notes": "citizen probe"},
        )
        show(
            "CITIZEN signs approval (control_console main.py:230 · guard require_king · "
            "signed_by منَ الرمزِ لا منَ الجسمِ)",
            "POST",
            c + "/v1/approval",
            citizen,
            {"decision": "approve", "signed_by": "spoofed-king", "model_id": "probe-model"},
        )

        # 3) الملكُ على المساراتِ الخمسةِ — كلُّها 200.
        code, _ = show(
            "KING reset (governance)",
            "POST",
            g + "/v1/system/kill-switch/reset",
            king,
            None,
        )
        assert code == 200, "king governance reset must succeed"
        show(
            "KING raises halt again (governance)",
            "POST",
            g + "/v1/system/kill-switch",
            king,
            {"level": "halt", "reason": "probe", "activated_by": "king"},
        )
        code, _ = show(
            "KING reset (control_console)",
            "POST",
            c + "/v1/kill-switch/reset",
            king,
            None,
        )
        assert code == 200, "king console reset must succeed"
        code, text = show(
            "KING creates promotion (governance)",
            "POST",
            g + "/v1/promotions",
            king,
            {"model_id": "probe-model"},
        )
        assert code == 201, "king promotion create must succeed"
        promo_id = json.loads(text).get("promotion_id")
        code, _ = show(
            "KING passes gate (governance)",
            "POST",
            f"{g}/v1/promotions/{promo_id}/gates",
            king,
            {"gate_name": "evaluation", "passed": True},
        )
        assert code == 200, "king gate check must succeed"
        code, text = show(
            "KING signs approval (console · signed_by هويةُ الرمزِ)",
            "POST",
            c + "/v1/approval",
            king,
            {"decision": "approve", "signed_by": "spoofed-king"},
        )
        assert code == 200, "king approval must succeed"
        assert '"signed_by":"king"' in text.replace(" ", ""), (
            "signer must come from the king token, not the body"
        )
    finally:
        for p in procs:
            p.terminate()
            p.wait(timeout=10)
        if os.path.exists(db):
            os.remove(db)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
