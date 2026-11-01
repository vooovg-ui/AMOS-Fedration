"""مولِّدُ حزمةِ الإحاطاتِ (ب) — W-782 · التوجيه 38 § 2 بند 2.

الهدف: توليدُ إحاطةٍ لكلِّ بندٍ بأوامرَ حرفيّةٍ من بطاقتِه، بلا تحريرٍ يدويٍّ للنصِّ.

إحاطةٌ لا ادّعاءُ مراجعةٍ: يكتبُ لكلِّ بندٍ ملفًّا بأوامرَ حرفيّةٍ، ولا ينقلُ حالةً.
يُشغَّلُ من جذرِ المستودعِ: python3 docs/audit/evidence/W-782/make_briefs.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / "docs/audit/evidence/W-782/briefs"
TRIAGE = ROOT / "docs/audit/evidence/W-770/in_review_triage_53bb0cc5.json"
WORK = ROOT / "docs/governance/work/ACTIVE_WORK.md"
REPO_URL = "https://github.com/vooovg-ui/AMOS-Fedration.git"
BASE = "/home/user/workspace/review_w782"
PY = ".venv/bin/python -m pytest -q -p no:cacheprovider"

# البنودُ الثمانيةُ الأقدمُ (W-770 · العمرُ من أوّلِ دمجِ شِفرةٍ) — وأوامرُ أدلّةِ بطاقاتِها
# مُحوَّلةً إلى بيئةِ الاستنساخِ (.venv) حرفًا بحرف، وموضعُ الطفرةِ المقترَحُ.
# الطفرةُ: (الملفُّ، أمرُ التطبيقِ، الفحصُ الذي يُتوقَّعُ سقوطُه).
ITEMS: dict[str, dict] = {
    "WI-026": {
        "evid": [
            f"{PY} tests/governance/test_runtime_state_stays_outside_the_tree.py",
            ".venv/bin/python tools/governance/check_root_file_names.py . --source disk",
            f"{PY} tests/governance",
            ".venv/bin/ruff check .",
            ".venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "conftest.py",
            "sed -i 's/^    os.environ\\[DATABASE_URL_ENV\\] = /    _ = /' conftest.py",
            "tests/governance/test_runtime_state_stays_outside_the_tree.py",
            "إسقاطُ إعلانِ `AMOS_DATABASE_URL` خارجَ الشجرةِ (المعيار 1)",
        ),
    },
    "WI-027": {
        "evid": [
            ".venv/bin/python tools/governance/state_document_drift.py",
            f"{PY} tests/governance/test_w057_state_document_drift.py",
            f"{PY} tests/governance",
            ".venv/bin/ruff check .",
            ".venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "tools/governance/state_document_drift.py",
            "sed -i 's/^    if anchor is None:$/    if anchor is None or True:/' tools/governance/state_document_drift.py",
            "tests/governance/test_w057_state_document_drift.py",
            "تجاهلُ المِرساةِ المُسمّاةِ كلِّها (المعياران 1 و2)",
        ),
    },
    "WI-028": {
        "evid": [
            f"{PY} tests/governance/test_w063_registered_claims.py",
            f"{PY} tests/governance",
            ".venv/bin/ruff check .",
            ".venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "tools/governance/mutation_claims.py",
            "sed -i 's/if CLAIM_MARKER in line or work in LEGACY_CLAIM_ROWS:/if re.search(\"طفر|وثب\", line):/' tools/governance/mutation_claims.py",
            "tests/governance/test_w063_registered_claims.py",
            "إرجاعُ القراءةِ إلى جذرِ الكلمةِ (المعياران 1 و2)",
        ),
    },
    "WI-029": {
        "evid": [
            f"{PY} tests/governance/test_w096_subprocess_measurement_site.py",
            f"{PY} tests/governance/test_w054_post_merge_reverse_link.py",
            f"{PY} tests/governance",
            ".venv/bin/ruff check .",
            ".venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "tests/governance/test_w054_post_merge_reverse_link.py",
            "sed -n 229,230p tests/governance/test_w054_post_merge_reverse_link.py && sed -i '229,230d' tests/governance/test_w054_post_merge_reverse_link.py",
            "tests/governance/test_w096_subprocess_measurement_site.py",
            "نزعُ `--repo-root` من الموضعِ المُرسى (المعياران 1 و3)",
        ),
    },
    "WI-030": {
        "evid": [
            ".venv/bin/python tools/governance/truth_audit.py . --check",
            f"{PY} tests/governance/test_w099_generated_artifact_freshness.py",
            f"{PY} tests/governance",
            ".venv/bin/ruff check .",
            ".venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "tools/governance/truth_audit.py",
            "sed -n 1102p tools/governance/truth_audit.py && sed -i '1102s/return 1$/return 0/' tools/governance/truth_audit.py",
            "tests/governance/test_w099_generated_artifact_freshness.py",
            "إسكاتُ رمزِ سقوطِ `--check` (المعياران 1 و3)",
        ),
    },
    "WI-031": {
        "evid": [
            f"{PY} -s tests/governance/test_w102_measurement_root_provenance.py",
            f"{PY} tests/governance",
            ".venv/bin/ruff check .",
            ".venv/bin/python tools/governance/truth_audit.py . --check && .venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "tests/constitutional/test_constitutional_cli.py",
            "echo 'ROOT = Path(__file__).resolve().parents[2]' >> tests/constitutional/test_constitutional_cli.py",
            "tests/governance/test_w102_measurement_root_provenance.py",
            "إضافةُ جذرٍ بعُمقٍ ثابتٍ بلا علامةٍ (المعيار 2: النموُّ يُسقِطُ)",
        ),
    },
    "WI-033": {
        "evid": [
            f"{PY} tests/constitutional tests/crown tests/sovereignty",
            f"{PY} tests/governance/test_w102_measurement_root_provenance.py",
            "bash tools/dev/bootstrap.sh --verify && .venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "tests/sovereignty/test_sovereignty_cli.py",
            "sed -i 's/^REPO_ROOT = discover_repo_root(__file__)$/REPO_ROOT = Path(__file__).resolve().parents[2]/' tests/sovereignty/test_sovereignty_cli.py",
            "tests/governance/test_w102_measurement_root_provenance.py",
            "إرجاعُ أحدِ المواضعِ التسعةِ إلى العُمقِ (المعيار 2)",
        ),
    },
    "WI-034": {
        "evid": [
            f"{PY} tests/governance/test_w109_commit_timestamp_timezone.py",
            ".venv/bin/python tools/governance/truth_audit.py . --ratchet",
        ],
        "mut": (
            "tools/governance/stamp_readme_identity.py",
            'sed -i \'s/datetime.now(timezone.utc).date()/datetime.now().date()/; s/"TZ": "UTC"/"TZ": "Asia\\/Riyadh"/\' tools/governance/stamp_readme_identity.py',
            "tests/governance/test_w109_commit_timestamp_timezone.py",
            "إرجاعُ اشتقاقِ اليومِ إلى منطقةِ الجهازِ والالتزامِ (المعيار 1)",
        ),
    },
}


def card_and_row(text: str, wi: str) -> tuple[str, str, int, int]:
    """الصفُّ حرفيًّا، ومعيارُ القبولِ والدليلُ المطلوبُ حرفيًّا، وموضعُ البطاقةِ (السطرُ الأوّلُ والطول).

    البطاقةُ كاملةً لا تُنسَخُ في الإحاطةِ: تُطبَعُ من استنساخِ المراجعِ بالأمرِ 4 — فالمرجعُ
    ما عندَ العقدةِ لا نسخةٌ ثانيةٌ (ونسخُها يُضاعِفُ الإحالاتِ إلى حدودِ الصدقِ · W-115).
    """
    row = next(ln for ln in text.splitlines() if ln.startswith(f"| {wi} |"))
    m = re.search(rf"^### {wi} — .*?```text\n(.*?)```", text, re.S | re.M)
    assert m, wi
    body = m.group(1)
    crit = re.search(r"^معيارُ القبول:\n.*?(?=^بدأ:|\Z)", body, re.S | re.M)
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
    node_q = "git log -1 --format=%H origin/main -- docs/audit/evidence/W-782/briefs/"
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
    cmds.append(f"cd {c} && sha256sum docs/audit/evidence/W-782/briefs/{wi}.md")
    cmds.append(f"cd {c} && cat docs/audit/evidence/W-782/briefs/SHA256SUMS")
    numbered = "\n".join(f"{i}. `{x}`" for i, x in enumerate(cmds, 1))
    nmut = len(cmds) - 3
    return f"""# إحاطةُ مراجعةِ البندِ: {wi} — مراجعٌ واحدٌ · مسار § 1.10 (§ 1.11)

> **الهدف:** إحاطةُ المراجعِ الواحدِ بكلِّ ما يصلُه — البندُ ومعاييرُه وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُه الإلزاميُّ.
> **إحاطةٌ لا مراجعة · لا تنقلُ حالة.** كتبَها المنفِّذُ (W-782 · التوجيه 38 § 2 بند 2) ولا يُقرأُ وجودُها حكمًا ولا تقدُّمًا في حالةِ البندِ.
> **المسار:** «مراجعٌ واحد · مسار § 1.10» (Q-92 · [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 1.11 — رُقِّمَ 1.11 لأنَّ 1.10 مأخوذٌ بـQ-91) — ليس نصابًا ولا يُحسَبُ بديلًا له. CLOSED يبقى بإذنِ المالكِ.
> **المراجعُ المعيَّنُ:** المستشارُ (Claude، خارجَ جلسةِ المنفِّذِ). **أهليّةُ العائلةِ معلَّقةٌ** (DISC-154): المنسِّقُ الحاضرُ Claude Opus 5.5 من عائلةِ المستشارِ نفسِها، وعائلةُ مؤلِّفِ هذا البندِ **غيرُ مقيَّدةٍ** في السجلِّ — يحسمُها المالكُ أو المراجعُ قبلَ أن يُقرأَ حكمُه للمسارِ.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) وQ-63 (لا اقتطاعَ · المخرجُ خامٌ كاملٌ).
> **تُبصَمُ sha256 في `SHA256SUMS` بجوارِ هذا الملفِّ** قبلَ الدفعِ.

**أهليّةُ المسارِ (من `docs/audit/evidence/W-770/in_review_triage_53bb0cc5.json`):** الطبقةُ `{tri['tier']}` · الصنفُ الفعّالُ `{tri['effective_class']}` · النطاقاتُ `{' · '.join(tri['path_domains'])}` · الأنواعُ `{' · '.join(tri['kinds'])}` · أوّلُ دمجِ شِفرةٍ `{' · '.join(tri['first_code_merge'][:3])}` · العمرُ {tri['age_days_from_first_code_merge']} يومًا · جولةٌ سابقةٌ: {'لا' if not tri['prior_round_evidence'] else tri['prior_round_evidence']} · عائلةُ المؤلِّفِ: غيرُ مقيَّدةٍ (DISC-154).

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُ مراجعتُها (كاملةً):** رأسُ main الذي يحملُ هذه الإحاطةَ — **تُعرِّفُه بالأمرِ 2 أدناه** (شِفرةُ البندِ لم تُمَسَّ منذُ `f607871c750966cc0c45988dceff1ed0e740d4c6` في دفعةِ الإحاطةِ).
- الاستنساخُ: استنسخِ المستودعَ بنفسِكَ استنساخًا كاملًا إلى `{c}`، وأعدَّ بيئتَه بـ`bash tools/dev/bootstrap.sh` داخلَه، واعملْ داخلَ جذرِكَ وحدَه.

### ب · البندُ ومعاييرُ قبولِه (كما كُتِبَت قبلَ التنفيذِ)
صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ كتابةِ هذه الإحاطةِ — والمرجعُ ما في استنساخِكَ عندَ العقدةِ):

````text
{row}
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
`.venv/bin/python tools/governance/council_verdict_raw_check.py --brief docs/audit/evidence/W-782/briefs/{wi}.md --repo {c} <ملفُّ الحكمِ>` قبلَ أن يُقرأَ.

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
