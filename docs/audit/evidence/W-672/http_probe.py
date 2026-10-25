"""مسبارُ HTTP حقيقيٌّ لأسطحِ زرِّ التوقّفِ والترقية — برمزِ مواطن (قياسُ ما قبلَ التحصين).

الهدف:
    يُشغِّلُ خدمتَي governance وcontrol_console بـuvicorn في عمليّتَينِ منفصلتَين على منفذَينِ
    محلّيَّين، ويُرسلُ طلباتِ HTTP حقيقيّةً بـurllib (لا TestClient)، ويطبعُ رمزَ الحالةِ والجسمَ حرفيًّا.

النطاق:
    دليلٌ لا شفرةٌ إنتاجيّة. سرُّ التوقيعِ يُولَّدُ عشوائيًّا لكلِّ تشغيلٍ (لا سرَّ مكتوبًا)،
    وقاعدةُ البياناتِ SQLite مؤقّتة.

المالك: WI-114 (دليلُ W-672) · يُعادُ استعمالُه مسبارًا لـWI-117 (توجيهُ المستشارِ 23 § 1 قرار 2)
تاريخ الإنشاء: 2026-10-25
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
        steps = [
            (
                "king raises halt (governance)",
                "POST",
                g + "/v1/system/kill-switch",
                king,
                {"level": "halt", "reason": "probe", "activated_by": "king"},
            ),
            ("citizen reads status", "GET", g + "/v1/system/status", citizen, None),
            (
                "CITIZEN reset (governance main.py:147 · guard :149)",
                "POST",
                g + "/v1/system/kill-switch/reset",
                citizen,
                None,
            ),
            ("status after citizen reset", "GET", g + "/v1/system/status", king, None),
            (
                "king raises halt again (console)",
                "POST",
                c + "/v1/kill-switch",
                king,
                {"level": "halt", "reason": "probe", "activated_by": "king"},
            ),
            (
                "CITIZEN reset (control_console main.py:209 · guard :211)",
                "POST",
                c + "/v1/kill-switch/reset",
                citizen,
                None,
            ),
            ("status after console reset", "GET", g + "/v1/system/status", king, None),
            (
                "king raises halt (third)",
                "POST",
                g + "/v1/system/kill-switch",
                king,
                {"level": "halt", "reason": "probe", "activated_by": "king"},
            ),
            (
                "CITIZEN lowers via activate level=normal (governance main.py:136 · guard :139)",
                "POST",
                g + "/v1/system/kill-switch",
                citizen,
                {"level": "normal", "reason": "probe-lower", "activated_by": "king"},
            ),
            (
                "status after citizen activate-normal",
                "GET",
                g + "/v1/system/status",
                king,
                None,
            ),
            (
                "king raises halt (fourth)",
                "POST",
                g + "/v1/system/kill-switch",
                king,
                {"level": "halt", "reason": "probe", "activated_by": "king"},
            ),
            (
                "CITIZEN lowers via activate level=normal (control_console main.py:195 · guard :198)",
                "POST",
                c + "/v1/kill-switch",
                citizen,
                {"level": "normal", "reason": "probe-lower", "activated_by": "king"},
            ),
            (
                "status after citizen console activate-normal",
                "GET",
                g + "/v1/system/status",
                king,
                None,
            ),
            (
                "CITIZEN creates promotion (governance main.py:167 · guard :170)",
                "POST",
                g + "/v1/promotions",
                citizen,
                {"model_id": "probe-model"},
            ),
        ]
        promo_id = None
        for label, method, url, tok, body in steps:
            code, text = _call(method, url, tok, body)
            print(
                f"### {label}\n$ {method} {url.replace(g, '<governance>').replace(c, '<console>')}"
                f"{' ' + json.dumps(body, ensure_ascii=False) if body else ''}\n-> {code} {text}\n"
            )
            if "creates promotion" in label and code < 300:
                promo_id = json.loads(text).get("id") or json.loads(text).get(
                    "promotion_id"
                )
        if promo_id:
            body = {
                "gate_name": "human_approval",
                "passed": True,
                "notes": "citizen self-approves",
            }
            code, text = _call(
                "POST", f"{g}/v1/promotions/{promo_id}/gates", citizen, body
            )
            print(
                f"### CITIZEN passes human_approval gate (governance main.py:199 · guard :203)\n$ POST <governance>/v1/promotions/{promo_id}/gates {json.dumps(body, ensure_ascii=False)}\n-> {code} {text}\n"
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
