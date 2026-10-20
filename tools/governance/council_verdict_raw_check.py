#!/usr/bin/env python3
"""فاحصُ خامِ الأحكامِ — يرفضُ أيَّ حكمِ مقعدٍ لا يحملُ مخرجاتِ أوامرِه خامًا كاملةً.

طريقُ الإنفاذ: COVERED_TEST · tests/governance/test_council_verdict_raw.py يحكُمُ به على أحكامِ الجولاتِ في الشجرةِ الحاضرةِ ويشملُه استدعاءُ `pytest` في CI

الهدف:
    تنفيذُ قرارِ المالكِ Q-63 (2026-10-20): «أضف فحصًا آليًا يرفض أي حكم لا يحمل
    مخرجات الأوامر خامًا». فحكمٌ يُرفَضُ هنا لا يُحتسَبُ في نصابِ § 5 منَ
    البروتوكولِ (§ 4.7) — والرفضُ رمزُ خروجٍ 1 لا رأيٌ.

النطاق — ما يُقاسُ (كلُّه آليٌّ بلا حكمٍ على المضمون):
    R1  الحقولُ الإلزاميّةُ حاضرةٌ أوّلَ السطر: MODEL · FAMILY · RUN_DATE · NODE ·
        CLONE_PATH · COMMANDS_RUN · RAW_OUTPUTS · VERDICT_PER_CRITERION ·
        BLOCKING_REMARKS · ISOLATION_DECLARATION · VERDICT
    R2  NODE بصمةُ التزامٍ كاملةٌ (40 خانةً ستّ‌عشريّة)
    R3  COMMANDS_RUN قائمةٌ مرقّمةٌ («n. الأمر») غيرُ فارغة
    R4  لكلِّ أمرٍ مرقّمٍ كتلةُ RAW واحدةٌ بالرقمِ نفسِه، وسطرُ CMD فيها يطابقُ
        الأمرَ المُعلَنَ حرفيًّا — ولا كتلةَ بلا أمرٍ مُعلَن
    R5  في كلِّ كتلةٍ: EXIT عددٌ صحيحٌ · BYTES وSHA256 يطابقانِ المخرجَ المكتوبَ
        (فأيُّ اقتطاعٍ أو تحريرٍ بعدَ الالتقاطِ يُسقِطُ البصمة)
    R6  قسمُ RAW_OUTPUTS لا يحملُ شيئًا غيرَ الكتلِ (لا نثرَ ولا مقاطعَ ولا وصفَ)
    R7  (بـ--brief) كلُّ أمرٍ في كتلِ ```bash من القسمِ «ج» في الإحاطةِ له كتلةٌ
        CMD تطابقُه حرفيًّا — فلا يُسقَطُ أمرٌ من أوامرِ المعايير
    R8  (بـ--repo) كلُّ كتلةٍ أمرُها «cd <دليل> && cat <مسار>» أو «cat <مسار>»
        يُقارَنُ مخرجُها بـ`git show <NODE>:<مسار>` في الاستنساخِ المُعطى —
        وفرقُ بايتٍ واحدٍ رفضٌ (خليّةُ MAPPING في W-538 · DISC-116)

    ولا يحكمُ الفاحصُ على صحّةِ المعاييرِ ولا على PASS/FAIL — ذلك حكمُ المقعد.
    وما لا يُقاسُ هنا ويُعلَنُ: أنَّ المخرجَ هو ما أخرجَه الأمرُ فعلًا في جلسةِ
    المقعدِ (البصمةُ تُثبِتُ سلامةَ النصِّ بعدَ الالتقاطِ لا صدقَ الالتقاطِ نفسِه).

المالك: WI-100 (بروتوكولُ المجلسِ · قرارُ المالكِ Q-63 · قيدُ W-542)
تاريخ الإنشاء: 2026-10-20
تاريخ آخر تعديل: 2026-10-20
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REQUIRED_FIELDS = (
    "MODEL",
    "FAMILY",
    "RUN_DATE",
    "NODE",
    "CLONE_PATH",
    "COMMANDS_RUN",
    "RAW_OUTPUTS",
    "VERDICT_PER_CRITERION",
    "BLOCKING_REMARKS",
    "ISOLATION_DECLARATION",
    "VERDICT",
)

_BLOCK = re.compile(
    r"^=== RAW \[(?P<n>\d+)\] BEGIN ===\n"
    r"CMD: (?P<cmd>[^\n]*)\n"
    r"EXIT: (?P<exit>[^\n]*)\n"
    r"BYTES: (?P<bytes>[^\n]*)\n"
    r"SHA256: (?P<sha>[^\n]*)\n"
    r"NO_EOL: (?P<noeol>[^\n]*)\n"
    r"--- OUTPUT ---\n"
    r"(?P<body>.*?)"
    r"^=== RAW \[(?P=n)\] END ===\n?",
    re.S | re.M,
)
_CMD_ITEM = re.compile(r"^\s*(\d+)\.\s+(.*?)\s*$")
_CAT = re.compile(r"^(?:cd (?P<cwd>\S+) && )?cat (?P<path>[^\s;&|<>]+)$")
_EXIT_SUFFIX = re.compile(r";\s*echo\s+\"?EXIT=\$\?\"?\s*$")


@dataclass
class Block:
    n: int
    cmd: str
    exit: str
    nbytes: str
    sha: str
    noeol: str
    body: str
    span: tuple[int, int]

    def output(self) -> str:
        if self.noeol == "1" and self.body.endswith("\n"):
            return self.body[:-1]
        return self.body


@dataclass
class Report:
    path: str
    problems: list[str] = field(default_factory=list)
    blocks: int = 0
    commands: int = 0

    @property
    def ok(self) -> bool:
        return not self.problems


def _field_line(text: str, name: str) -> int:
    m = re.search(rf"^{name}:", text, re.M)
    return m.start() if m else -1


def _section(text: str, start: str, end: str) -> str:
    a = _field_line(text, start)
    b = _field_line(text, end)
    if a < 0 or b < 0 or b < a:
        return ""
    return text[a + len(start) + 1 : b]


def brief_commands(brief_text: str) -> list[str]:
    """أوامرُ القسمِ «ج» في الإحاطةِ: كلُّ سطرٍ غيرِ فارغٍ داخلَ كتلِ ```bash."""
    m = re.search(r"^#{2,3} ج[^\n]*\n(?P<sec>.*?)(?=^#{2,3} (?!ج)|\Z)", brief_text, re.S | re.M)
    if not m:
        return []
    cmds: list[str] = []
    for fence in re.finditer(r"```bash\n(.*?)```", m.group("sec"), re.S):
        for line in fence.group(1).splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cmds.append(_EXIT_SUFFIX.sub("", line).strip())
    return cmds


def check_text(
    text: str,
    *,
    path: str = "<verdict>",
    brief_text: str | None = None,
    repo: Path | None = None,
) -> Report:
    rep = Report(path=path)
    p = rep.problems

    # الكتلُ أوّلًا — ثمَّ يُقرأُ ما سواها على نصٍّ مُقنَّعٍ (فلا يُعَدُّ حقلٌ داخلَ مخرجٍ خامٍ حقلًا)
    blocks: list[Block] = []
    masked_parts, last = [], 0
    for bm in _BLOCK.finditer(text):
        blocks.append(
            Block(
                n=int(bm.group("n")),
                cmd=bm.group("cmd"),
                exit=bm.group("exit"),
                nbytes=bm.group("bytes"),
                sha=bm.group("sha"),
                noeol=bm.group("noeol"),
                body=bm.group("body"),
                span=bm.span(),
            )
        )
        masked_parts.append(text[last : bm.start()])
        masked_parts.append(f"\x00RAWBLOCK{bm.group('n')}\x00\n")
        last = bm.end()
    masked_parts.append(text[last:])
    masked = "".join(masked_parts)
    rep.blocks = len(blocks)

    # R1
    for name in REQUIRED_FIELDS:
        if _field_line(masked, name) < 0:
            p.append(f"R1 حقلٌ إلزاميٌّ غائبٌ: {name}")

    # R2
    node_m = re.search(r"^NODE:\s*(\S+)", masked, re.M)
    node = node_m.group(1) if node_m else ""
    if node and not re.fullmatch(r"[0-9a-f]{40}", node):
        p.append(f"R2 NODE ليست بصمةً كاملةً: {node!r}")

    # R3
    listed: dict[int, str] = {}
    for line in _section(masked, "COMMANDS_RUN", "RAW_OUTPUTS").splitlines():
        mm = _CMD_ITEM.match(line)
        if mm:
            n = int(mm.group(1))
            if n in listed:
                p.append(f"R3 رقمُ أمرٍ مكرَّرٌ في COMMANDS_RUN: {n}")
            listed[n] = mm.group(2)
    rep.commands = len(listed)
    if not listed and _field_line(masked, "COMMANDS_RUN") >= 0:
        p.append("R3 COMMANDS_RUN بلا أمرٍ مرقّمٍ («n. الأمر»)")

    # R6 — قسمُ RAW_OUTPUTS لا يحملُ إلا الكتل
    raw = _section(masked, "RAW_OUTPUTS", "VERDICT_PER_CRITERION")
    outside = [b for b in blocks if f"\x00RAWBLOCK{b.n}\x00" not in raw]
    for b in outside:
        p.append(f"R6 كتلةُ [{b.n}] خارجَ قسمِ RAW_OUTPUTS")
    stray = re.sub(r"\x00RAWBLOCK\d+\x00", "", raw).strip()
    if stray:
        p.append(
            "R6 نصٌّ في RAW_OUTPUTS خارجَ كتلِ RAW (نثرٌ/مقاطعُ/وصفٌ): "
            + repr(stray[:120])
        )

    # R4
    seen: dict[int, Block] = {}
    for b in blocks:
        if b.n in seen:
            p.append(f"R4 كتلتانِ بالرقمِ نفسِه: [{b.n}]")
        seen[b.n] = b
        if b.n not in listed:
            p.append(f"R4 كتلةُ [{b.n}] بلا أمرٍ مُعلَنٍ في COMMANDS_RUN")
        elif listed[b.n].strip() != b.cmd.strip():
            p.append(
                f"R4 أمرُ الكتلةِ [{b.n}] يخالفُ المُعلَن: "
                f"{b.cmd!r} ≠ {listed[b.n]!r}"
            )
    for n in sorted(listed):
        if n not in seen:
            p.append(f"R4 الأمرُ [{n}] بلا كتلةِ RAW (مخرجٌ غيرُ خام): {listed[n][:80]!r}")

    # R5
    for b in blocks:
        if not re.fullmatch(r"-?\d+", b.exit.strip()):
            p.append(f"R5 [{b.n}] EXIT ليس عددًا: {b.exit!r}")
        if b.noeol not in ("0", "1"):
            p.append(f"R5 [{b.n}] NO_EOL ليس 0 أو 1: {b.noeol!r}")
        data = b.output().encode("utf-8")
        if b.nbytes.strip() != str(len(data)):
            p.append(f"R5 [{b.n}] BYTES {b.nbytes!r} ≠ المقيسِ {len(data)} — مخرجٌ مُقتطَعٌ أو مُحرَّر")
        if b.sha.strip() != hashlib.sha256(data).hexdigest():
            p.append(f"R5 [{b.n}] SHA256 لا يطابقُ المخرجَ المكتوبَ — مخرجٌ مُقتطَعٌ أو مُحرَّر")

    # R7
    if brief_text is not None:
        want = brief_commands(brief_text)
        if not want:
            p.append("R7 لم يُعثَرْ على أوامرَ في القسمِ «ج» منَ الإحاطة")
        have = {b.cmd.strip() for b in blocks}
        for c in want:
            if c not in have:
                p.append(f"R7 أمرٌ منَ الإحاطةِ بلا كتلةِ RAW: {c[:100]!r}")

    # R8
    if repo is not None and node:
        for b in blocks:
            cm = _CAT.match(b.cmd.strip())
            if not cm:
                continue
            rel = cm.group("path")
            cwd = cm.group("cwd")
            if rel.startswith("/"):
                if cwd is None:
                    continue
                rel = str(Path(rel).relative_to(cwd)) if rel.startswith(cwd) else rel
                if rel.startswith("/"):
                    continue
            proc = subprocess.run(
                ["git", "-C", str(repo), "show", f"{node}:{rel}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            if proc.returncode != 0:
                p.append(f"R8 [{b.n}] تعذّرَ git show {node[:7]}:{rel} — لا مقارنة")
                continue
            if proc.stdout.decode("utf-8", errors="replace") != b.output():
                p.append(f"R8 [{b.n}] مخرجُ «cat {rel}» يخالفُ الملفَّ عندَ العقدة {node[:7]}")
    return rep


def check_file(path: Path, *, brief: Path | None = None, repo: Path | None = None) -> Report:
    text = path.read_text(encoding="utf-8")
    # تُتجاوَزُ ترويسةُ الهويّةِ التي يضيفُها المنسِّقُ عندَ الحفظِ: النصُّ بعدَ أوّلِ «---» منفردٍ إن سبقَه عنوانُ ملف
    if text.startswith("# ") and "\n---\n" in text:
        text = text.split("\n---\n", 1)[1]
    brief_text = brief.read_text(encoding="utf-8") if brief else None
    return check_text(text, path=str(path), brief_text=brief_text, repo=repo)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="فاحصُ خامِ أحكامِ المجلس (Q-63)")
    ap.add_argument("verdicts", nargs="+", help="ملفّاتُ الأحكام")
    ap.add_argument("--brief", help="الإحاطةُ المعبَّأةُ للمقعد (R7) — مع حكمٍ واحد")
    ap.add_argument("--repo", help="استنساخٌ يحوي العقدةَ للمقارنةِ (R8)")
    args = ap.parse_args(argv)
    if args.brief and len(args.verdicts) != 1:
        print("[RAW CHECK] ✗ --brief يُعطى مع حكمٍ واحد (إحاطةٌ لكلِّ مقعد)")
        return 2
    bad = 0
    for v in args.verdicts:
        rep = check_file(
            Path(v),
            brief=Path(args.brief) if args.brief else None,
            repo=Path(args.repo) if args.repo else None,
        )
        state = "✓ مقبولٌ" if rep.ok else "✗ مرفوضٌ"
        print(f"[RAW CHECK] {state}: {rep.path} · أوامرُ {rep.commands} · كتلُ RAW {rep.blocks}")
        for prob in rep.problems:
            print(f"  - {prob}")
        bad += 0 if rep.ok else 1
    if bad:
        print(f"[RAW CHECK] ✗ {bad} حكمًا مرفوضًا — لا يُحتسَبُ في النصاب (البروتوكولُ § 4.7)")
        return 1
    print(f"[RAW CHECK] ✓ {len(args.verdicts)}/{len(args.verdicts)} حكمًا مقروءًا يحملُ مخرجاتِ أوامرِه خامًا كاملةً")
    return 0


if __name__ == "__main__":
    sys.exit(main())
