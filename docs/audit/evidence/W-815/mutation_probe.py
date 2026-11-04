"""الهدف: مِسبارُ طفراتِ W-815 — DISC-155 (M1 § 2.12) وDISC-153 (DISC153_PREPUSH_ONLY_DEPS_DESIGN § 3).

يُطبِّقُ كلَّ طفرةٍ على نسخةٍ في المكان، ويُشغِّلُ الفحوصَ المسمّاة، ثمَّ يُعيدُ الملفَّ
بايتًا بايتًا (`finally`). الطفرةُ «مقتولةٌ» إن سقطَ الفحصُ (رمزُ pytest غيرُ صفريّ)،
و«ناجيةٌ» إن نجح — والناجيةُ تُسقِطُ المسبارَ كلَّه (EXIT=1).

الاستعمال (من جذرِ المستودع):
    .venv/bin/python docs/audit/evidence/W-815/mutation_probe.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SVC = ROOT / "federal/executive/services"
PY = sys.executable

DELEG = SVC / "src/amos_federation/common/money_delegation.py"
JUD = SVC / "src/amos_federation/services/federal_judiciary/service.py"
GATE = ROOT / "tools/dev/prepush_gate.py"

Q19 = "tests/test_q19_money_delegation.py"
Q32 = "tests/test_q32_money_enforcement_surface.py"
R7D = "tests/test_r7d_federal_judiciary.py"
WI077 = "tests/governance/test_wi077_prepush_ci_parity.py"

ENTRY = """    MoneyDelegation(
        operation="treasury.disbursement.post",
        constitutional_action="disburse_funds",
        entrypoint="enforce_ruling_via_treasury","""
CALL = """        resolve_money_delegation(
            "treasury.disbursement.post", entrypoint="enforce_ruling_via_treasury"
        )
"""


def _drop_entry(s: str) -> str:
    start = s.index(ENTRY)
    end = s.index("    ),\n)\n", start) + len("    ),\n")
    return s[:start] + s[end:]


def _move_call_after_disburse(s: str) -> str:
    s = s.replace(CALL, "", 1)
    anchor = "            transaction = treasury.disburse("
    assert anchor in s, "مرساةُ الصرفِ غائبة"
    return s.replace(anchor, CALL.replace("        ", "            ", 1) + anchor, 1)


MUTATIONS = [
    (
        "DISC-155 ① حذفُ المدخلِ الحادي عشر",
        DELEG,
        _drop_entry,
        SVC,
        [Q19, R7D, "-k", "enforce or count or measured or resolve"],
    ),
    (
        "DISC-155 ② حذفُ نداءِ الاستخراجِ من القضاء",
        JUD,
        lambda s: s.replace(CALL, "", 1),
        SVC,
        [Q19],
    ),
    (
        "DISC-155 ③ فعلٌ غيرُ disburse_funds للمدخل",
        DELEG,
        lambda s: s.replace(
            ENTRY,
            ENTRY.replace(
                'constitutional_action="disburse_funds"',
                'constitutional_action="post_funding"',
            ),
            1,
        ),
        SVC,
        [Q19],
    ),
    (
        "DISC-155 ④ treasury.disburse يُستبدَلُ بنداءٍ آخر في القضاء",
        JUD,
        lambda s: s.replace("treasury.disburse(", "treasury.disburse_direct(", 1),
        SVC,
        [Q32],
    ),
    (
        "DISC-155 ⑤ الاستخراجُ بعدَ treasury.disburse",
        JUD,
        _move_call_after_disburse,
        SVC,
        [Q19, "-k", "before_any_work"],
    ),
    (
        "DISC-153 ① حذفُ الخطوةِ 34",
        GATE,
        lambda s: s[: s.index("        # ── نَسَبُ القياساتِ: الشطرُ الآخر")]
        + s[s.index("    ]\n", s.index("        # ── نَسَبُ القياساتِ: الشطرُ الآخر")) :],
        ROOT,
        [WI077],
    ),
    (
        "DISC-153 ② إعادةُ 0 دائمًا مع الحزمة",
        GATE,
        lambda s: s.replace(
            "        return result.returncode\n", "        return 0\n", 1
        ),
        ROOT,
        [WI077],
    ),
    (
        "DISC-153 ③ --without-deps بدلَ --only-deps في الفحصِ الداخليّ",
        GATE,
        lambda s: s.replace(
            '                "--check",\n                "--only-deps",\n',
            '                "--check",\n                "--without-deps",\n',
            1,
        ),
        ROOT,
        [WI077],
    ),
    (
        "DISC-153 ④ الغيابُ بلا سطرٍ مُعلَن",
        GATE,
        lambda s: s.replace(
            '                "[PREPUSH] شطرُ --only-deps لا يُقاسُ هنا: cryptography غائبةٌ في هذا "\n',
            '                ""\n',
            1,
        ),
        ROOT,
        [WI077],
    ),
]


def main() -> int:
    survived = 0
    for title, path, mutate, cwd, args in MUTATIONS:
        original = path.read_bytes()
        text = original.decode("utf-8")
        mutated = mutate(text)
        if mutated == text:
            print(f"✗ {title}: الطفرةُ لم تُغيِّرْ شيئًا — المِسبارُ معطوب")
            return 2
        try:
            path.write_text(mutated, encoding="utf-8")
            result = subprocess.run(
                [PY, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", *args],
                cwd=str(cwd),
                capture_output=True,
                text=True,
                check=False,
            )
        finally:
            path.write_bytes(original)
        tail = (result.stdout or "").strip().splitlines()[-1:] or [""]
        verdict = "مقتولة" if result.returncode != 0 else "ناجية"
        if result.returncode == 0:
            survived += 1
        print(f"{verdict} · {title} · pytest rc={result.returncode} · {tail[0]}")
    killed = len(MUTATIONS) - survived
    print(f"\nالحصيلة: {killed}/{len(MUTATIONS)} مقتولة · {survived} ناجية")
    return 1 if survived else 0


if __name__ == "__main__":
    sys.exit(main())
