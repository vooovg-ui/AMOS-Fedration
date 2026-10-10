"""الهدف: مزوِّدُ صندوقٍ معزولٍ فعلًا على المضيف — bubblewrap بكلِّ مساحاتِ الأسماء ونظامِ ملفّاتٍ مُغلَق.

النطاق: services/tool_registry/providers
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-10 (WI-067 · قرارُ المالكِ في Q-33)

## لماذا مزوِّدٌ جديدٌ لا تعديلُ `local`

`LocalSubprocessProvider` يُعلِنُ حدَّه بنفسِه: العمليّةُ على **المضيفِ نفسِه** وتحتَ
**المستخدمِ نفسِه**، ونظامُ الملفّاتِ مشتركٌ خارجَ مجلّدِ العمل، والعزلُ شبكيٌّ وحدَه إن
توفّر. فلا يصحُّ أن يُسمّى صندوقًا. والمالكُ قرّرَ في 2026-10-10 (‏Q-33): «تشغيل
legal_search داخل sandbox فعلي». وتغييرُ `local` يُغيّرُ كلَّ أداةٍ تمرُّ به بلا قرار؛
فهذا مزوِّدٌ مستقلٌّ تختارُه الأداةُ التي قُرِّرَ عزلُها، ولا يُختارُ بالبيئةِ ضمنًا.

## ما يُفرَضُ — بالنواةِ لا بفحصِنا

- `--unshare-all`: مساحاتُ أسماءٍ جديدةٌ للمستخدمِ والشبكةِ والعمليّاتِ وIPC وUTS وcgroup —
  فلا شبكةَ إطلاقًا (‏لا واجهةَ غيرُ `lo` المُطفأة)، ولا رؤيةَ لعمليّاتِ المضيف.
- نظامُ ملفّاتٍ يُبنى من الصفر: `/usr` وروابطُه **للقراءةِ وحدَها**، و`/tmp` في الذاكرة،
  ومجلّدُ عملٍ مؤقّتٌ هو وحدَه قابلٌ للكتابة، وما يُمرَّرُ في `readonly_mounts` للقراءة.
  فلا `/home` ولا `/root` ولا `/etc` المضيفِ ولا شجرةُ المستودعِ إلّا ما سُمِّي.
- `--clearenv` ثمَّ بيئةٌ تُبنى من `secrets.build_sandbox_env` (‏قائمةُ سماحٍ فارغةٌ افتراضًا)
  — لا وراثةَ لبيئةِ المضيف.
- `--cap-drop ALL` · `--new-session` (‏لا `TIOCSTI`) · `--die-with-parent` (‏لا يتيمَ بعدَ المهلة).
- حدُّ الذاكرةِ بـ`RLIMIT_AS` داخلَ العمليّة، والمهلةُ من المُستدعي.

## ما يُقاسُ ولا يُفترَض

التوفُّرُ يُسبَرُ بتشغيلِ الصندوقِ نفسِه (‏`availability()`): `bwrap` غائبٌ، أو مساحاتُ أسماءِ
المستخدمِ ممنوعةٌ في النواة، أو لا `python3` في `/usr/bin` ⇒ `available=False` بسببٍ مُسمّى،
ولا سقوطَ إلى `local` (‏قاعدةُ `selection`: الغيابُ لا يُبدَّلُ بنجاح).

## حدودُه المُعلَنة

- لا ترشيحَ مضيفٍ في الشبكة: سياسةُ `DENY` وحدَها مقبولة، وغيرُها يُرفَضُ عندَ الإنشاء.
- العزلُ عزلُ مساحاتِ أسماءٍ على النواةِ نفسِها لا آلةٌ افتراضيّة: ثغرةُ نواةٍ تعبرُه.
- لا يُسجَّلُ في `selection.PROVIDERS`: لا يُختارُ بـ`AMOS_SANDBOX_PROVIDER` لأداةٍ لم يُقرَّرْ عزلُها.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import time
import uuid
from pathlib import Path

from amos_federation.services.executive_core.fidelity import ExecutionFidelity
from amos_federation.services.tool_registry.providers import network, secrets
from amos_federation.services.tool_registry.providers.contract import (
    ExecutionRequest,
    ExecutionResult,
    ProviderAvailability,
    ProviderUnavailableError,
    SandboxHandle,
    SandboxProvider,
    SandboxSpec,
)

#: نمطُ فرضِ الشبكةِ في هذا المزوِّد — مساحةُ أسماءِ شبكةٍ فارغة.
NETWORK_ENFORCEMENT = "NAMESPACE_ENFORCED"

#: وصفُ العزلِ المُعلَنُ في كلِّ نتيجة.
ISOLATION = "BWRAP_ALL_NAMESPACES_RO_ROOT"

#: المُفسِّرُ داخلَ الصندوق — من `/usr` المُركَّبِ للقراءة، لا مُفسِّرَ البيئةِ الافتراضيّة.
SANDBOX_PYTHON = "/usr/bin/python3"

#: مجلّدُ العملِ داخلَ الصندوق.
SANDBOX_WORKDIR = "/work"

_RLIMIT_PREAMBLE = "import resource as _r\n_r.setrlimit(_r.RLIMIT_AS, ({limit}, {limit}))\ndel _r\n"


def _root_layout() -> list[str]:
    """`/usr` للقراءة، وروابطُ الدمجِ (‏`/bin` → `usr/bin`…) كما هي على المضيف."""
    args = ["--ro-bind", "/usr", "/usr"]
    for top in ("/bin", "/sbin", "/lib", "/lib32", "/lib64", "/libx32"):
        path = Path(top)
        if path.is_symlink():
            args += ["--symlink", os.readlink(top), top]
        elif path.is_dir():
            args += ["--ro-bind", top, top]
    for etc in ("/etc/ld.so.cache", "/etc/alternatives"):
        if Path(etc).exists():
            args += ["--ro-bind", etc, etc]
    return args


class BubblewrapProvider(SandboxProvider):
    """صندوقٌ معزولٌ بـbubblewrap — REAL، وعزلُه مفروضٌ من النواةِ ومُعلَنٌ في النتيجة."""

    name = "bwrap"
    fidelity = ExecutionFidelity.REAL

    def __init__(self, readonly_mounts: dict[str, str] | None = None) -> None:
        """`readonly_mounts`: {مسارٌ داخلَ الصندوق: مسارٌ على المضيف} — للقراءةِ وحدَها."""
        self._mounts = dict(readonly_mounts or {})
        for inside in self._mounts:
            if not inside.startswith("/") or inside in {"/", "/usr", SANDBOX_WORKDIR}:
                raise ValueError(f"مسارُ تركيبٍ غيرُ مقبول داخلَ الصندوق: {inside!r}")

    # ── التوفُّر — يُسبَرُ بالتشغيل ─────────────────────────────────────────

    def _base_argv(self, workspace: str) -> list[str]:
        argv = [
            "bwrap",
            "--unshare-all",
            "--die-with-parent",
            "--new-session",
            "--cap-drop",
            "ALL",
            "--clearenv",
            *_root_layout(),
            "--proc",
            "/proc",
            "--dev",
            "/dev",
            "--tmpfs",
            "/tmp",
            "--bind",
            workspace,
            SANDBOX_WORKDIR,
            "--chdir",
            SANDBOX_WORKDIR,
            "--hostname",
            "amos-sandbox",
        ]
        for inside, host in sorted(self._mounts.items()):
            argv += ["--ro-bind", host, inside]
        return argv

    def availability(self) -> ProviderAvailability:
        if shutil.which("bwrap") is None:
            return ProviderAvailability(
                provider=self.name,
                available=False,
                fidelity=ExecutionFidelity.UNAVAILABLE.value,
                reason="bubblewrap غيرُ مُثبَّت على المضيف",
                missing_package="bubblewrap",
            )
        if not Path(SANDBOX_PYTHON).exists():
            return ProviderAvailability(
                provider=self.name,
                available=False,
                fidelity=ExecutionFidelity.UNAVAILABLE.value,
                reason=f"لا مُفسِّرَ في {SANDBOX_PYTHON}",
                missing_package="python3",
            )
        for inside, host in self._mounts.items():
            if not Path(host).is_dir():
                return ProviderAvailability(
                    provider=self.name,
                    available=False,
                    fidelity=ExecutionFidelity.UNAVAILABLE.value,
                    reason=f"مصدرُ التركيبِ {inside} غيرُ موجودٍ على المضيف",
                )
        probe_dir = tempfile.mkdtemp(prefix="amos_bwrap_probe_")
        try:
            probe = subprocess.run(  # noqa: S603
                [*self._base_argv(probe_dir), SANDBOX_PYTHON, "-I", "-c", "pass"],
                capture_output=True,
                text=True,
                timeout=15,
                check=False,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            return ProviderAvailability(
                provider=self.name,
                available=False,
                fidelity=ExecutionFidelity.UNAVAILABLE.value,
                reason=f"تعذّرَ سبرُ الصندوق: {exc}",
            )
        finally:
            shutil.rmtree(probe_dir, ignore_errors=True)
        if probe.returncode != 0:
            return ProviderAvailability(
                provider=self.name,
                available=False,
                fidelity=ExecutionFidelity.UNAVAILABLE.value,
                reason=(
                    "النواةُ رفضَت الصندوق (‏مساحاتُ أسماءِ المستخدمِ ممنوعة؟): "
                    + (probe.stderr or "").strip()[:200]
                ),
            )
        return ProviderAvailability(
            provider=self.name,
            available=True,
            fidelity=self.fidelity.value,
            reason=f"bubblewrap — {ISOLATION}",
        )

    # ── دورةُ الحياة ─────────────────────────────────────────────────────

    def create_sandbox(self, spec: SandboxSpec) -> SandboxHandle:
        self.assert_usable()
        if network.normalize_policy(spec.network_policy) != "DENY":
            raise ProviderUnavailableError(
                f"{self.name}: سياسةُ الشبكة '{spec.network_policy}' غيرُ مقبولة — "
                "هذا الصندوقُ يقطعُ الشبكةَ كلَّها ولا يُرشِّحُ مضيفًا"
            )
        secrets.assert_allowlist_is_safe(spec.secret_allowlist)
        workspace = tempfile.mkdtemp(prefix=f"amos_bwrap_{spec.tool_id}_")
        return SandboxHandle(
            sandbox_id=f"bwrap-{uuid.uuid4().hex[:12]}",
            provider=self.name,
            spec=spec,
            native=workspace,
        )

    def execute(self, handle: SandboxHandle, request: ExecutionRequest) -> ExecutionResult:
        self._guard_handle(handle)
        spec = handle.spec
        workspace = str(handle.native)
        timeout = request.timeout_seconds or spec.timeout_seconds

        env, plan = secrets.build_sandbox_env(
            spec.secret_allowlist,
            extra={
                "HOME": SANDBOX_WORKDIR,
                "TMPDIR": "/tmp",
                "PATH": "/usr/bin:/bin",
                "LANG": "C.UTF-8",
                "PYTHONIOENCODING": "utf-8",
                "AMOS_SANDBOX_ID": handle.sandbox_id,
                "AMOS_SANDBOX_PROVIDER": self.name,
                "AMOS_SANDBOX_NETWORK_POLICY": spec.network_policy,
            },
        )
        setenv: list[str] = []
        for key, value in sorted(env.items()):
            setenv += ["--setenv", key, value]

        if request.command:
            inner = list(request.command)
        else:
            script = os.path.join(workspace, "amos_tool_entry.py")
            preamble = _RLIMIT_PREAMBLE.format(limit=spec.memory_limit_mb * 1024 * 1024)
            with open(script, "w", encoding="utf-8") as handle_file:
                handle_file.write(preamble + request.code)
            inner = [SANDBOX_PYTHON, "-I", f"{SANDBOX_WORKDIR}/amos_tool_entry.py"]

        argv = [*self._base_argv(workspace), *setenv, *inner]
        started = time.monotonic()
        try:
            proc = subprocess.run(  # noqa: S603
                argv,
                capture_output=True,
                text=True,
                timeout=timeout,
                env={"PATH": "/usr/bin:/bin"},
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            return self.result(
                handle,
                request,
                network_enforcement=NETWORK_ENFORCEMENT,
                stdout=exc.stdout if isinstance(exc.stdout, str) else "",
                stderr=exc.stderr if isinstance(exc.stderr, str) else "",
                exit_code=None,
                duration_ms=int((time.monotonic() - started) * 1000),
                timed_out=True,
                secrets_injected=plan.injected,
                error=f"timeout بعد {timeout}s",
            )
        except OSError as exc:
            return self.result(
                handle,
                request,
                network_enforcement=NETWORK_ENFORCEMENT,
                stdout="",
                stderr=str(exc),
                exit_code=None,
                duration_ms=int((time.monotonic() - started) * 1000),
                secrets_injected=plan.injected,
                error=f"os_error: {exc}",
            )
        return self.result(
            handle,
            request,
            network_enforcement=NETWORK_ENFORCEMENT,
            stdout=proc.stdout or "",
            stderr=proc.stderr or "",
            exit_code=proc.returncode,
            duration_ms=int((time.monotonic() - started) * 1000),
            secrets_injected=plan.injected,
        )

    def terminate(self, handle: SandboxHandle) -> None:
        """`--die-with-parent` يُنهي الصندوقَ بانتهاءِ العمليّة — الإنهاءُ تعليمُ المقبض."""
        if handle.provider != self.name:
            return
        handle.terminated = True

    def cleanup(self, handle: SandboxHandle) -> None:
        if handle.provider != self.name:
            return
        handle.terminated = True
        if handle.native:
            shutil.rmtree(str(handle.native), ignore_errors=True)
            handle.native = None
