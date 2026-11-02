"""مولِّدُ حزمةِ الإحاطاتِ (ب) الثانية — W-787 · التوجيه 38 § 2 بند 2.

الهدف: توليدُ إحاطةٍ لكلِّ بندٍ بأوامرَ حرفيّةٍ من بطاقتِه، بلا تحريرٍ يدويٍّ للنصِّ.

إحاطةٌ لا ادّعاءُ مراجعةٍ: يكتبُ لكلِّ بندٍ ملفًّا بأوامرَ حرفيّةٍ، ولا ينقلُ حالةً.
يُشغَّلُ من جذرِ المستودعِ: python3 docs/audit/evidence/W-787/make_briefs.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / "docs/audit/evidence/W-787/briefs"
TRIAGE = ROOT / "docs/audit/evidence/W-770/in_review_triage_53bb0cc5.json"
WORK = ROOT / "docs/governance/work/ACTIVE_WORK.md"
REPO_URL = "https://github.com/vooovg-ui/AMOS-Fedration.git"
BASE = "/home/user/workspace/review_w787"
PY = ".venv/bin/python -m pytest -q -p no:cacheprovider"

# الحزمةُ الثانية: الثمانيةُ التاليةُ بالعمرِ (W-770 · العمرُ من أوّلِ دمجِ شِفرةٍ) — وأوامرُ أدلّةِ بطاقاتِها
# مُحوَّلةً إلى بيئةِ الاستنساخِ (.venv) حرفًا بحرف، وموضعُ الطفرةِ المقترَحُ.
# الطفرةُ: (الملفُّ، أمرُ التطبيقِ، الفحصُ الذي يُتوقَّعُ سقوطُه).
ITEMS: dict[str, dict] = {
    "WI-036": {
        "evid": [
            f"{PY} tests/governance/test_w115_truth_limit_integrity.py",
            ".venv/bin/python tools/governance/truth_limit_integrity.py --check",
            ".venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "tools/governance/truth_limit_integrity.py",
            "sed -i '276s/> declared\\[LIMITS_FIELD\\]/> declared[LIMITS_FIELD] + 10**6/; 283s/> declared\\[field\\]/> declared[field] + 10**6/' tools/governance/truth_limit_integrity.py",
            "tests/governance/test_w115_truth_limit_integrity.py",
            "إرخاءُ السقّاطةِ حتى لا يُسقِطَ النموُّ (المعيار 2)",
        ),
    },
    "WI-038": {
        "evid": [
            ".venv/bin/python tools/governance/suite_size_inventory.py --check",
            f"{PY} tests/governance/test_w120_suite_size_claims.py",
            f"{PY} tests/",
        ],
        "mut": (
            "tools/governance/suite_size_inventory.py",
            "sed -i 's/^        if claim.written_total != live:$/        if False:/' tools/governance/suite_size_inventory.py",
            "tests/governance/test_w120_suite_size_claims.py",
            "إسكاتُ مقارنةِ المكتوبِ بالجمعِ الحيِّ (الرقمُ الميّتُ يمرّ)",
        ),
    },
    "WI-043": {
        "evid": [
            ".venv/bin/python tools/governance/generator_settlement_closure.py --check",
            f"{PY} -p no:randomly tests/governance/test_w129_generator_settlement_closure.py",
        ],
        "mut": (
            "tools/governance/generator_settlement_closure.py",
            "sed -i '326s/> declared\\[UNBOUND_FIELD\\]/> declared[UNBOUND_FIELD] + 10**6/' tools/governance/generator_settlement_closure.py",
            "tests/governance/test_w129_generator_settlement_closure.py",
            "إرخاءُ سقّاطةِ المولِّداتِ غيرِ المربوطة",
        ),
    },
    "WI-045": {
        "evid": [
            ".venv/bin/python tools/governance/green_denominator_closure.py --check",
            f"{PY} -p no:randomly tests/governance/test_w130_green_denominator_closure.py",
        ],
        "mut": (
            "tools/governance/green_denominator_closure.py",
            'sed -i \'281s/> declared\\["unbounded"\\]/> declared["unbounded"] + 10**6/\' tools/governance/green_denominator_closure.py',
            "tests/governance/test_w130_green_denominator_closure.py",
            "إرخاءُ سقّاطةِ الأحكامِ الكلّيّةِ بلا مقام",
        ),
    },
    "WI-046": {
        "evid": [
            ".venv/bin/python tools/governance/artifact_witness_integrity.py --check",
            f"{PY} -p no:randomly tests/governance/test_w131_artifact_witness_integrity.py",
        ],
        "mut": (
            "tools/governance/artifact_witness_integrity.py",
            'sed -i \'177s/> declared\\["degraded"\\]/> declared["degraded"] + 10**6/\' tools/governance/artifact_witness_integrity.py',
            "tests/governance/test_w131_artifact_witness_integrity.py",
            "إرخاءُ سقّاطةِ الآثارِ الشاهدةِ المتدهورة",
        ),
    },
    "WI-047": {
        "evid": [
            ".venv/bin/python tools/governance/report_note_ratchet.py --check",
            f"{PY} -p no:randomly tests/governance/test_w132_report_note_ratchet.py",
        ],
        "mut": (
            "tools/governance/report_note_ratchet.py",
            'sed -i \'248s/> declared\\["unratcheted"\\]/> declared["unratcheted"] + 10**6/\' tools/governance/report_note_ratchet.py',
            "tests/governance/test_w132_report_note_ratchet.py",
            "إرخاءُ سقّاطةِ الملاحظاتِ غيرِ المحروسة",
        ),
    },
    "WI-041": {
        "evid": [
            ".venv/bin/python tools/governance/commit_timestamp_integrity.py",
            f"{PY} tests/governance/test_w110_commit_stamp_integrity.py tests/governance/test_w113_new_commit_stamp_utc.py",
        ],
        "mut": (
            "tools/governance/commit_timestamp_integrity.py",
            "sed -i 's/^    non_utc = sum(1 for s in stamps.values() if not s.endswith(UTC_SUFFIXES))$/    non_utc = 0/' tools/governance/commit_timestamp_integrity.py",
            "tests/governance/test_w110_commit_stamp_integrity.py tests/governance/test_w113_new_commit_stamp_utc.py",
            "تصفيرُ عدِّ الطوابعِ غيرِ العالميّة (إزاحةُ +03:00 لا تُرى)",
        ),
    },
    "WI-072": {
        "evid": [
            f"{PY} federal/executive/services/tests/test_w308_test_ledger_is_per_session.py",
            "ls docs/audit/evidence/WI-072/",
        ],
        "mut": (
            "federal/executive/services/tests/conftest.py",
            "sed -i 's/_cleanup_test_ledger(TEST_ARTIFACT_DIR)/_cleanup_test_ledger(workspace)/' federal/executive/services/tests/conftest.py",
            "federal/executive/services/tests/test_w308_test_ledger_is_per_session.py",
            "إعادةُ السجلِّ إلى مجلَّدِ الخدماتِ المشترك (تحوُّرُ البطاقةِ نفسُه)",
        ),
    },
}


def row_raises_truth_limit(row: str) -> bool:
    """هل يرفعُ نسخُ الصفِّ عدّادَ الإحالاتِ الملتبسةِ إلى حدودِ الصدق (W-115)؟

    الأنماطُ من الأداةِ نفسِها لا نسخةٌ منها؛ وإن رفعَ فالصفُّ يُطبَعُ من الاستنساخِ
    بأمرٍ (كالبطاقةِ في W-782) ولا يُنسَخُ — فلا تعلو السقّاطةُ بإحاطة.
    """
    sys.path.insert(0, str(ROOT))
    from tools.governance import truth_limit_integrity as tli

    text = tli.normalize(row)
    return any(p.search(text) for p in tli.REFERENCE_RES)


def card_and_row(text: str, wi: str) -> tuple[str, str, int, int]:
    """الصفُّ حرفيًّا، ومعيارُ القبولِ والدليلُ المطلوبُ حرفيًّا، وموضعُ البطاقةِ (السطرُ الأوّلُ والطول).

    البطاقةُ كاملةً لا تُنسَخُ في الإحاطةِ: تُطبَعُ من استنساخِ المراجعِ بالأمرِ 4 — فالمرجعُ
    ما عندَ العقدةِ لا نسخةٌ ثانيةٌ (ونسخُها يُضاعِفُ الإحالاتِ إلى حدودِ الصدقِ · W-115).
    """
    row = next(ln for ln in text.splitlines() if ln.startswith(f"| {wi} |"))
    m = re.search(rf"^### {wi} — .*?```text\n(.*?)```", text, re.S | re.M)
    assert m, wi
    body = m.group(1)
    # بطاقاتُ الحزمةِ الثانيةِ تكتبُ «معيار القبول» بلا ضمّةٍ، وبطاقةُ WI-072 تضعُه بعدَ «بدأ:».
    crit = re.search(
        r"^معيارُ? القبول:\n.*?(?=^بدأ:|^الخطوةُ التالية:|\Z)", body, re.S | re.M
    )
    assert crit, wi
    first = text.count("\n", 0, m.start()) + 1
    length = m.group(0).count("\n")
    return row, crit.group(0).rstrip(), first, length


def brief(
    wi: str, spec: dict, tri: dict, row: str, crit: str, first: int, length: int
) -> str:
    slug = wi.lower().replace("-", "")
    c = f"{BASE}/{slug}/repo"
    raw = f"{BASE}/{slug}/raw"
    node_q = "git log -1 --format=%H origin/main -- docs/audit/evidence/W-787/briefs/"
    cmds = [
        f"mkdir -p {BASE}/{slug} && cd {BASE}/{slug} && git clone {REPO_URL} repo",
        f"cd {c} && {node_q}",
        f"cd {c} && git checkout $({node_q}) && git rev-parse HEAD",
        f"cd {c} && bash tools/dev/bootstrap.sh",
        f"cd {c} && sed -n '{first},{first + length}p' docs/governance/work/ACTIVE_WORK.md",
    ]
    cmds += [f"cd {c} && {e}" for e in spec["evid"]]
    mfile, mcmd, mtest, mwhat = spec["mut"]
    cmds.append(
        f'cd {c} && {mcmd} && {PY} {mtest}; echo "pytest_exit=$? (غيرُ الصفرِ = الحرسُ أسقطَ الطفرةَ)"'
    )
    cmds.append(
        f"cd {c} && git checkout -- {mfile} && git status --porcelain && git diff --stat"
    )
    cmds.append(f"cd {c} && sha256sum docs/audit/evidence/W-787/briefs/{wi}.md")
    cmds.append(f"cd {c} && cat docs/audit/evidence/W-787/briefs/SHA256SUMS")
    row_block = (
        "(لا يُنسَخُ هنا: نصُّه يرفعُ عدّادَ الإحالاتِ الملتبسةِ في W-115 — "
        f"اطبعْه من استنساخِكَ: `grep -n '^| {wi} |' docs/governance/work/ACTIVE_WORK.md`)"
        if row_raises_truth_limit(row)
        else row
    )
    numbered = "\n".join(f"{i}. `{x}`" for i, x in enumerate(cmds, 1))
    nmut = len(cmds) - 3
    return f"""# إحاطةُ مراجعةِ البندِ: {wi} — مراجعٌ واحدٌ · مسار § 1.10 (§ 1.11)

> **الهدف:** إحاطةُ المراجعِ الواحدِ بكلِّ ما يصلُه — البندُ ومعاييرُه وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُه الإلزاميُّ.
> **إحاطةٌ لا مراجعة · لا تنقلُ حالة.** كتبَها المنفِّذُ (W-787 · التوجيه 38 § 2 بند 2) ولا يُقرأُ وجودُها حكمًا ولا تقدُّمًا في حالةِ البندِ.
> **المسار:** «مراجعٌ واحد · مسار § 1.10» (Q-92 · [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 1.11 — رُقِّمَ 1.11 لأنَّ 1.10 مأخوذٌ بـQ-91) — ليس نصابًا ولا يُحسَبُ بديلًا له. CLOSED يبقى بإذنِ المالكِ.
> **المراجعُ المعيَّنُ:** المستشارُ (Claude، خارجَ جلسةِ المنفِّذِ). **أهليّةُ العائلةِ معلَّقةٌ** (DISC-154): المنسِّقُ الحاضرُ Claude Opus 5.5 من عائلةِ المستشارِ نفسِها، وعائلةُ مؤلِّفِ هذا البندِ **غيرُ مقيَّدةٍ** في السجلِّ — يحسمُها المالكُ أو المراجعُ قبلَ أن يُقرأَ حكمُه للمسارِ.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) وQ-63 (لا اقتطاعَ · المخرجُ خامٌ كاملٌ).
> **تُبصَمُ sha256 في `SHA256SUMS` بجوارِ هذا الملفِّ** قبلَ الدفعِ.

**أهليّةُ المسارِ (من `docs/audit/evidence/W-770/in_review_triage_53bb0cc5.json`):** الطبقةُ `{tri['tier']}` · الصنفُ الفعّالُ `{tri['effective_class']}` · النطاقاتُ `{' · '.join(tri['path_domains'])}` · الأنواعُ `{' · '.join(tri['kinds'])}` · أوّلُ دمجِ شِفرةٍ `{' · '.join(tri['first_code_merge'][:3])}` · العمرُ {tri['age_days_from_first_code_merge']} يومًا · جولةٌ سابقةٌ: {'لا' if not tri['prior_round_evidence'] else tri['prior_round_evidence']} · عائلةُ المؤلِّفِ: غيرُ مقيَّدةٍ (DISC-154).

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُه بالأمرِ 2 أدناه** (شِفرةُ البندِ لم تُمَسَّ منذُ `4336852e213b1a4ba3039888979ad31038e143e6` في دفعةِ الإحاطةِ).
- الاستنساخُ: استنسخِ المستودعَ بنفسِكَ استنساخًا كاملًا إلى `{c}`، وأعدَّ بيئتَه بـ`bash tools/dev/bootstrap.sh` داخلَه، واعملْ داخلَ جذرِكَ وحدَه.

### ب · البندُ ومعاييرُ قبولِه (كما كُتِبَت قبلَ التنفيذِ)
صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذه الإحاطةِ — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

````text
{row_block}
````

بطاقتُه كاملةً **تُطبَعُ من استنساخِكَ بالأمرِ 5** (`docs/governance/work/ACTIVE_WORK.md` السطور {first}–{first + length} عندَ كتابةِ الإحاطةِ — فإن انزاحت فابحثْ عن العنوانِ `### {wi} — `). ومعيارُ القبولِ والدليلُ المطلوبُ منها حرفيًّا:

````text
{crit}
````

**سياقٌ مقيسٌ لا حكمٌ:** البطاقةُ تكتبُ السقّاطةَ «63» يومَ كُتِبَت؛ اقرأِ الرقمَ الحاضرَ من تشغيلِكَ للأمرِ `--ratchet` واحكمْ بمعنى المعيارِ (لم ترتفعْ).

### ج · أوامرُ المعاييرِ (من البطاقةِ نفسِها، في بيئةِ الاستنساخِ)
{numbered}

الأمرُ {nmut} **طفرةٌ مقترَحةٌ** في `{mfile}`: {mwhat} — يُتوقَّعُ أن يُسقِطَها `{mtest}`. والأمرُ {nmut + 1} يُعيدُ الملفَّ.

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّه وبطاقتُه · الأمرُ 5)
- هذه الإحاطةُ
- القراراتُ المذكورةُ في البطاقةِ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md`
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِه — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجبْ عن كلٍّ منها بمخرجاتٍ خامٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاه؟ اذكرْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْه كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out {raw}/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضعْ كتلَ RAW متتاليةً في جوابِكَ بلا اقتطاعٍ.
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذه الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجِدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يحاولُ كسرَ خاصيّةٍ يَعِدُ بها معيارٌ من (ب)، وأودِعْ شِفرتَه وتشغيلَه كتلتَي RAW.
7. **عائلةُ المؤلِّفِ (DISC-154):** اذكرْ ما تعرفُه من عائلتِكَ وهل تراها مختلفةً عن عائلةِ مؤلِّفِ البندِ — أو اكتبْ «غيرُ قابلةٍ للحسمِ من موضعي».

### و · صيغةُ جوابِكَ (تُحفَظُ حرفيًّا بلا تحريرٍ)
يُودَعُ الجوابُ خامًا في `docs/audit/evidence/<قيدُ الإيداعِ>/{slug}/verdict_<model>.md`، ويُفحَصُ بـ
`.venv/bin/python tools/governance/council_verdict_raw_check.py --brief docs/audit/evidence/W-787/briefs/{wi}.md --repo {c} <ملفُّ الحكمِ>` قبلَ أن يُقرأَ.

```
MODEL: <اسمُ النموذجِ كما أعلنتْه المنصّةُ>
FAMILY: <العائلةُ>
ROUTE: مراجعٌ واحد · مسار § 1.10
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: <sha>
CLONE_PATH: <المسارُ>
COMMANDS_RUN:
 1. <الأمرُ حرفيًّا كما في سطرِ CMD من كتلتِه>
 2. …
RAW_OUTPUTS:
<كتلُ RAW كما كتبتْها أداةُ الالتقاطِ — متتاليةً بلا أيِّ نصٍّ بينها:>
=== RAW [1] BEGIN ===
CMD: <الأمر>
EXIT: <رمزُ الخروج>
BYTES: <عدد>
SHA256: <بصمة>
NO_EOL: <0|1>
--- OUTPUT ---
<المخرجُ كلُّه>
=== RAW [1] END ===
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ>
PROBES: <لكلِّ مسبارٍ: رقمُ كتلةِ شِفرتِه · رقمُ كتلةِ تشغيلِه · الخاصيّةُ التي حاولَ كسرَها · انكسرت؟ نعم/لا>
AUTHOR_FAMILY: <جوابُ السؤالِ 7>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرارُ>
```
"""


def main() -> None:
    text = WORK.read_text(encoding="utf-8")
    tri = {x["wi"]: x for x in json.loads(TRIAGE.read_text(encoding="utf-8"))["items"]}
    OUT.mkdir(parents=True, exist_ok=True)
    for wi, spec in ITEMS.items():
        row, crit, first, length = card_and_row(text, wi)
        (OUT / f"{wi}.md").write_text(
            brief(wi, spec, tri[wi], row, crit, first, length), encoding="utf-8"
        )
        print(wi, "كُتِبَ")


if __name__ == "__main__":
    main()
