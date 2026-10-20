#!/usr/bin/env python3
"""التقاطُ مخرجِ أمرٍ خامًا كاملًا في كتلةٍ قابلةٍ للفحصِ الآليِّ — لمقاعدِ مجلسِ المراجعة.

طريقُ الإنفاذ: COVERED_TEST · tests/governance/test_council_verdict_raw.py يُشغِّلُه على أوامرَ حقيقيّةٍ ويشملُه استدعاءُ `pytest` في CI

الهدف:
    تنفيذُ قرارِ المالكِ Q-63 (2026-10-20): «أعد الجولة بمخرجات خام كاملة» —
    فيُشغِّلُ المقعدُ كلَّ أمرٍ من أوامرِ الإحاطةِ عبرَ هذه الأداةِ، فتكتبُ
    المخرجَ المدموجَ (stdout ثمَّ stderr مدموجًا كما يظهرُ) **كلَّه بلا اقتطاعٍ**
    في كتلةٍ مرقّمةٍ تحملُ الأمرَ ورمزَ الخروجِ وعددَ البايتاتِ وبصمةَ sha256.
    فلا ينقلُ المقعدُ مخرجًا بيدِهِ — والنقلُ اليدويُّ هو ما أنتجَ في جولةِ
    W-538 مقاطعَ ووصفًا نثريًّا وخليّةً مخالفةً للملفِّ (DISC-116).

النطاق:
    يُشغِّلُ أمرًا واحدًا بـ`bash -c` في دليلِ العملِ الحاضرِ ويكتبُ كتلتَه إلى
    `--out`. لا يحكمُ على شيءٍ ولا يختصرُ شيئًا. والفاحصُ المقابلُ هو
    `council_verdict_raw_check.py` (يعيدُ حسابَ البصمةِ ويرفضُ الحكمَ الناقص).

صيغةُ الكتلة (ثابتةٌ · يقرؤها الفاحصُ):
    === RAW [<n>] BEGIN ===
    CMD: <الأمرُ حرفيًّا في سطرٍ واحد>
    EXIT: <رمزُ الخروج>
    BYTES: <عددُ بايتاتِ المخرجِ>
    SHA256: <بصمةُ بايتاتِ المخرج>
    NO_EOL: <1 إن لم ينتهِ المخرجُ بسطرٍ جديدٍ فأُضيفَ للفصلِ فقط · وإلا 0>
    --- OUTPUT ---
    <المخرجُ كلُّه>
    === RAW [<n>] END ===

    والمخرجُ يُفكُّ UTF-8؛ وما لا يُفكُّ يُستبدَلُ بـU+FFFD — والبصمةُ والعددُ
    على النصِّ المكتوبِ نفسِه (فما في الملفِّ هو ما يُبصَم).

المالك: WI-100 (بروتوكولُ المجلسِ · قرارُ المالكِ Q-63 · قيدُ W-542)
تاريخ الإنشاء: 2026-10-20
تاريخ آخر تعديل: 2026-10-20
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path


def render_block(n: int, cmd: str, exit_code: int, output: str) -> str:
    """يبني الكتلةَ بصيغتِها الثابتة — يستعملُها الالتقاطُ والفحوصُ معًا."""
    if "\n" in cmd:
        raise ValueError("الأمرُ سطرٌ واحدٌ — الكتلةُ لا تحملُ أمرًا متعدّدَ الأسطر")
    data = output.encode("utf-8")
    no_eol = 0 if (output == "" or output.endswith("\n")) else 1
    body = output + ("\n" if no_eol else "")
    return (
        f"=== RAW [{n}] BEGIN ===\n"
        f"CMD: {cmd}\n"
        f"EXIT: {exit_code}\n"
        f"BYTES: {len(data)}\n"
        f"SHA256: {hashlib.sha256(data).hexdigest()}\n"
        f"NO_EOL: {no_eol}\n"
        f"--- OUTPUT ---\n"
        f"{body}"
        f"=== RAW [{n}] END ===\n"
    )


def capture(n: int, cmd: str) -> str:
    proc = subprocess.run(
        ["bash", "-c", cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = proc.stdout.decode("utf-8", errors="replace")
    return render_block(n, cmd, proc.returncode, output)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="التقاطُ مخرجِ أمرٍ خامًا كاملًا (Q-63)")
    ap.add_argument("--n", type=int, required=True, help="رقمُ الأمرِ في COMMANDS_RUN")
    ap.add_argument("--out", required=True, help="ملفُّ الكتلةِ (داخلَ دليلِ المقعد)")
    ap.add_argument("cmd", help="الأمرُ حرفيًّا كما في الإحاطة (سطرٌ واحد)")
    args = ap.parse_args(argv)
    block = capture(args.n, args.cmd)
    Path(args.out).write_text(block, encoding="utf-8")
    exit_line = block.split("\n", 3)[2]
    print(f"[RAW CAPTURE] [{args.n}] {exit_line} → {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
