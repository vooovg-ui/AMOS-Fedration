#!/usr/bin/env python3
"""الهدف: سجلُّ نَسَبِ القياساتِ المنشورةِ وحرسُ طزاجتِها — W-037.

لا ملفَّ بلا قيدٍ، ولا قيدَ بلا سببٍ. تُقيسُ ولا تُصلِحُ، ولا تكتبُ ما تحكمُ عليه.

لماذا وُجِدَت هذه الأداةُ (العلّةُ مقيسةٌ لا مُتوهَّمة)
--------------------------------------------------
كانَ في `docs/audit/measurements/` عشرةُ قياساتٍ منشورةٍ، اثنانِ منها فقط لهما
بوّابةُ طزاجةٍ (`in_memory_inventory` بعدَ W-035، و`pricing_divergence` بعدَ
W-036). والثمانيةُ الباقيةُ تُقرَأُ في الوثائقِ كأنَّها حقيقةُ اليومِ ولا شيءَ
يمنعُ تقادُمَها. فجُرِّبَت إعادةُ توليدِها واحدًا واحدًا في W-037، فسقطَ الوهمُ:

* `write_inventory_p13.json`  : منشورٌ 203 موقعَ كتابةٍ · والمقيسُ 217.
* `decision_wave_map.json`    : منشورٌ دَينٌ 168 (W3=82) · والمقيسُ 182 (W3=96).
* `final_audit_p14.json`      : منشورٌ 27 سؤالًا سياديًّا · والمقيسُ 42،
                                و`program_mentions_168` منشورٌ 11 · والمقيسُ 73.

ثلاثةُ قياساتٍ متقادمةٌ من عشرةٍ، أُعيدَ توليدُها في W-037. والعلّةُ ليست
التقادمَ نفسَه — بل أنَّ لا شيءَ كانَ يُظهِرُه. فهذه الأداةُ تُقيِّدُ **كلَّ**
ملفٍّ منشورٍ بنَسَبِه، وتُشغِّلُ ما يُمكِنُ إعادةُ قياسِه، وتُعلِنُ ما لا يُمكِنُ
وسببَه رقمًا ظاهرًا — فالباقي بلا حرسٍ يُعَدُّ ويُرى، ولا يختفي.

القاعدةُ الحاكمةُ: «لا ملفَّ بلا قيدٍ، ولا قيدَ بلا سببٍ».

الحرسُ لا يكتبُ ما يحكمُ عليه
-----------------------------
بوّابةٌ تُصلِحُ ما تحكمُ عليه لا تُثبِتُ شيئًا. فلا تُشغَّلُ هنا إلّا أوضاعُ
قياسٍ لا تكتبُ في الشجرةِ: إمّا `--check` الخاصُّ بالمُولِّدِ، وإمّا طبعٌ على
المخرَجِ القياسيِّ، وإمّا كتابةٌ إلى ملفٍّ مؤقَّتٍ خارجَ الشجرة. والمُولِّدُ الذي
يكتبُ إلى مسارِ قياسِه ثابتًا ولا وضعَ قياسٍ له — يُعلَنُ ولا يُشغَّل.

الاستعمالُ
---------
    python tools/governance/measurement_provenance.py . --report
    python tools/governance/measurement_provenance.py . --check
    python tools/governance/measurement_provenance.py . --check --contract-only

يخرجُ بصفرٍ إن استقامَ العقدُ، وبواحدٍ مُسمِّيًا كلَّ خَرمٍ.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

#: مجلَّدُ القياساتِ المنشورةِ — نسبةً لجذرِ المستودع.
MEASUREMENTS = Path("docs") / "audit" / "measurements"

#: ملفّاتٌ في المجلَّدِ ليست قياسًا منشورًا فلا تُقيَّدُ بنَسَبٍ.
PROSE_FILES = ("README.md",)

# أوضاعُ إعادةِ القياسِ:
#   delegate : يُشغَّلُ `--check` الخاصُّ بالمُولِّدِ وهو يحكمُ بنفسِه.
#   stdout   : يُشغَّلُ أمرٌ يطبعُ القياسَ الطازجَ JSON على المخرَجِ القياسيّ.
#   tmpfile  : يُشغَّلُ أمرٌ يكتبُ القياسَ الطازجَ إلى ملفٍّ مؤقَّتٍ خارجَ الشجرة.
#   declared : لا إعادةَ قياسٍ ممكنةٌ في بوّابةٍ — يُعلَنُ السببُ ويُعَدُّ.
STRATEGIES = ("delegate", "stdout", "tmpfile", "declared")


@dataclass(frozen=True)
class Provenance:
    """قيدُ نَسَبٍ لقياسٍ منشورٍ واحدٍ."""

    name: str
    #: مسارُ المُولِّدِ نسبةً للجذرِ — فارغٌ حينَ لا مُولِّدَ برمجيًّا له.
    generator: str
    #: الأمرُ الذي يُعيدُ توليدَ الملفِّ حرفيًّا، ليُنفَّذَ لا ليُوصَف.
    command: str
    strategy: str
    #: أمرُ إعادةِ القياسِ بلا كتابةٍ في الشجرةِ. `{out}` تُبدَلُ بملفٍّ مؤقَّت.
    probe: tuple[str, ...] = ()
    #: مفاتيحُ المقارنةِ؛ فارغٌ = يُقارَنُ الحِملُ كلُّه.
    compare: tuple[str, ...] = ()
    #: مفاتيحُ لا تُقارَنُ، ولكلٍّ منها سببٌ في `reason`.
    ignore: tuple[str, ...] = ()
    #: سببُ الإعلانِ بلا إعادةِ قياسٍ، أو سببُ الاستثناءِ. واجبٌ لغيرِ المُقاسِ.
    reason: str = ""
    #: حزمٌ خارجيّةٌ يلزمُ تنصيبُها لإعادةِ القياسِ (W-038). وجودُها ينقلُ القيدَ
    #: إلى الشطرِ الذي يُفحَصُ في وظيفةٍ مُنصِّبةٍ، ولا يُعفيه من الحرسِ:
    #: القسمةُ مُعلَنةٌ ومعدودةٌ ومربوطةٌ بفحصٍ يقرأُ ملفَّ CI — لا تخطٍّ صامتٍ.
    needs: tuple[str, ...] = ()


#: قيدُ النَّسَبِ لكلِّ قياسٍ منشورٍ. أيُّ ملفٍّ يُضافُ إلى المجلَّدِ ولا يُقيَّدُ
#: هنا يُسقِطُ البوّابةَ — وذاكَ مقصودٌ: القيدُ شرطُ النشرِ لا زينةٌ بعدَه.
REGISTRY: tuple[Provenance, ...] = (
    Provenance(
        name="in_memory_inventory.json",
        generator="tools/governance/in_memory_inventory.py",
        command="python tools/governance/in_memory_inventory.py .",
        strategy="delegate",
        probe=("python", "tools/governance/in_memory_inventory.py", ".", "--check"),
    ),
    Provenance(
        name="pricing_divergence.json",
        generator="tools/governance/pricing_divergence.py",
        command="python tools/governance/pricing_divergence.py .",
        strategy="delegate",
        probe=("python", "tools/governance/pricing_divergence.py", ".", "--check"),
    ),
    Provenance(
        name="write_inventory_p13.json",
        generator="tools/audit/sovereign_write_inventory.py",
        command=(
            "python tools/audit/sovereign_write_inventory.py "
            "--json docs/audit/measurements/write_inventory_p13.json"
        ),
        strategy="tmpfile",
        probe=("python", "tools/audit/sovereign_write_inventory.py", "--json", "{out}"),
    ),
    Provenance(
        name="final_audit_p14.json",
        generator="tools/audit/final_audit.py",
        command=(
            "python tools/audit/final_audit.py "
            "> docs/audit/measurements/final_audit_p14.json"
        ),
        strategy="stdout",
        probe=("python", "tools/audit/final_audit.py"),
        reason=(
            "يعتمدُ حقلا `hashes_in_doc`/`hashes_not_in_history` على سجلِّ git "
            "(`git log -n 400`)، فتُستنسَخُ الوظيفةُ بعمقٍ كاملٍ (`fetch-depth: 0`) "
            "وإلّا حكمَ الحرسُ على سجلٍّ منقوصٍ فصارَ كاذبًا. وهشاشةٌ مُعلَنةٌ: حينَ "
            "يتجاوزُ المستودعُ 400 التزامٍ تسقطُ أقدمُ البصماتِ من النافذةِ فتُعَدُّ "
            "«ليست في السجلِّ» بلا حقيقةٍ — عندَها تُوسَّعُ النافذةُ أو يُراجَعُ تعريفُ "
            "الحقلِ، والعدُّ يومَ القيدِ 243 التزامًا."
        ),
    ),
    Provenance(
        name="decision_wave_map.json",
        generator="tools/audit/decision_gate.py",
        command="python tools/audit/decision_gate.py --map",
        strategy="stdout",
        probe=("python", "tools/audit/decision_gate.py", "--measure"),
        compare=("debt", "waves"),
        ignore=("git_head",),
        reason=(
            "يُقارَنُ بوضعِ `--measure` لأنَّ `--map` يكتبُ إلى مسارِ القياسِ نفسِه "
            "والحرسُ لا يكتبُ ما يحكمُ عليه. و`git_head` لا يُقارَنُ لأنَّه ختمُ "
            "الالتزامِ الذي وُلِّدَ عندَه الملفُّ: بعدَ قيدِه في التزامٍ جديدٍ لا يُساوي "
            "الرأسَ أبدًا، فمقارنتُه تُحمِّرُ البوّابةَ دائمًا بلا انحرافٍ حقيقيٍّ."
        ),
    ),
    Provenance(
        name="judicial_gate_matrix.json",
        generator="tools/audit/judicial_gate_probe.py",
        command="python tools/audit/judicial_gate_probe.py",
        strategy="tmpfile",
        probe=("python", "tools/audit/judicial_gate_probe.py", "--json", "{out}"),
        needs=("cryptography",),
        reason=(
            "رُفِعَ في W-038 ما أُعلِنَ في W-037: كانَ المُولِّدُ يكتبُ إلى مسارِ قياسِه "
            "ثابتًا فلا يُحرَسُ إلّا بأن يكتبَ الحرسُ ما يحكمُ عليه؛ فأُضيفَ إليه "
            "`--json PATH` فصارَ يكتبُ حيثُ يُقالُ له، وبلا الرايةِ لم يتغيَّرْ مُخرَجُه "
            "بايتًا. ويستوردُ المحرِّكَ الدستوريَّ ومن خلفِه `cryptography` (مرسومُ "
            "التاجِ يُوقَّعُ بـEd25519)، ووظيفةُ التدقيقِ لا تُنصِّبُ شيئًا — فيُفحَصُ هذا "
            "القيدُ في وظيفةِ النواةِ الدستوريّةِ بـ`--only-deps`، وهو موضعُه معنًى لا "
            "حيلةً: المِسبارُ يقيسُ أحكامَ ذاكَ المحرِّكِ. والقسمةُ مُعلَنةٌ ومعدودةٌ "
            "ومربوطةٌ بفحصٍ يقرأُ ملفَّ CI — فلا تنهارُ إلى تخطٍّ صامتٍ."
        ),
    ),
    Provenance(
        name="treasury_gate_matrix.json",
        generator="tools/audit/treasury_gate_probe.py",
        command="python tools/audit/treasury_gate_probe.py",
        strategy="tmpfile",
        probe=("python", "tools/audit/treasury_gate_probe.py", "--json", "{out}"),
        needs=("cryptography",),
        reason=(
            "كسابقِه حرفًا بحرفٍ ورُفِعَ معَه في W-038: أُضيفَ إليه `--json PATH` فصارَ "
            "يُعادُ قياسُه بلا أن يكتبَ الحرسُ ما يحكمُ عليه، وبلا الرايةِ لم يتغيَّرْ "
            "مُخرَجُه بايتًا. ويحتاجُ `cryptography` كسابقِه فيُفحَصُ في وظيفةِ النواةِ "
            "الدستوريّةِ بـ`--only-deps`."
        ),
    ),
    Provenance(
        name="restart_survival.json",
        generator="tools/governance/restart_survival_probe.py",
        command="python tools/governance/restart_survival_probe.py",
        strategy="declared",
        reason=(
            "يُولَّدُ بإطلاقِ خِدَمٍ حقيقيّةٍ وقتلِها وإعادةِ قراءتِها، فزمنُه دقائقُ "
            "ويحتاجُ بيئةَ خدمةٍ كاملةً. وله فحصُه الخاصُّ `--check` يُشغَّلُ في "
            "وظيفةٍ أخرى؛ فلا يُكرَّرُ هنا."
        ),
    ),
    Provenance(
        name="domain_truth_snapshot.json",
        generator="",
        command=(
            "قياسٌ يدويٌّ: تُنفَّذُ استعلاماتُ حقلِ `method` على قاعدةِ الفدراليّةِ "
            "الحيّةِ ويُقيَّدُ ناتجُها مع `measured_at`/`measured_by`"
        ),
        strategy="declared",
        reason=(
            "لا مُولِّدَ برمجيًّا له: قاسَه المنفِّذُ يدًا باستعلاماتٍ على قاعدةٍ حيّةٍ "
            "(بندُ السجل W-025)، والاستعلاماتُ نفسُها محفوظةٌ في الملفِّ تحتَ "
            "`method` فالقياسُ مُعادٌ بها لا بأداةٍ. ولا محرِّكَ قاعدةٍ في CI، فلو "
            "زُوِّرَ له مُولِّدٌ لصارَ الحرسُ يُصادِقُ على فراغٍ. ولذا يحملُ وحدَه من "
            "بينِ العشرةِ حقلَي `measured_at`/`measured_by` — وهي طزاجتُه المُعلَنةُ "
            "بتاريخٍ لا ببوّابة."
        ),
    ),
    Provenance(
        name="decision_gate_ledger.json",
        generator="tools/audit/decision_gate.py",
        command="python tools/audit/decision_gate.py --record Q-NN",
        strategy="declared",
        reason=(
            "سجلٌّ تراكميٌّ لا لَقطةٌ: تُضافُ إليه لَقطةٌ عندَ إغلاقِ كلِّ قرارٍ "
            "سياديٍّ، فلا حالةَ راهنةً يُعادُ توليدُها منها — وإعادةُ التوليدِ "
            "تعني محوَ تاريخٍ، وهو محرَّمٌ."
        ),
    ),
)

#: بواديءُ مساراتٍ تدلُّ على جهازِ عاملٍ بعينِه لا على المستودعِ. نشرُ واحدةٍ
#: منها في قياسٍ يُفشي مسارَ مَن شغَّلَ الأداةَ ويجعلُ الملفَّ غيرَ منقولٍ بينَ
#: البيئاتِ — وهي عينُ العلّةِ التي استثناها W-035 من المقارنةِ ولم يمنعْ نشرَها.
MACHINE_PREFIXES = ("/home/", "/Users/", "/root/", "/tmp/", "/var/folders/", "/private/")
_DRIVE = re.compile(r"^[A-Za-z]:[\\/]")


def _iter_strings(node: object) -> list[str]:
    """اجمعْ كلَّ نصٍّ في بنيةِ JSON مهما عَمُقَت — فالمسارُ قد يُدفَنُ."""
    found: list[str] = []
    if isinstance(node, str):
        found.append(node)
    elif isinstance(node, dict):
        for key, value in node.items():
            found.append(key)
            found.extend(_iter_strings(value))
    elif isinstance(node, list):
        for value in node:
            found.extend(_iter_strings(value))
    return found


def _machine_paths(payload: object) -> list[str]:
    """أعِدْ كلَّ نصٍّ يبدو مسارًا مُطلَقًا لجهازِ عاملٍ."""
    hits = []
    for text in _iter_strings(payload):
        if text.startswith(MACHINE_PREFIXES) or _DRIVE.match(text):
            hits.append(text)
    return hits


def _subset(payload: dict, entry: Provenance) -> dict:
    """اقتصِرْ على مفاتيحِ المقارنةِ واحذفِ المُستثنى — بلا توسُّعٍ خفيٍّ."""
    keys = entry.compare or tuple(k for k in payload if k != "$comment")
    return {k: payload[k] for k in keys if k in payload and k not in entry.ignore}


def _run(argv: list[str], root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        argv, cwd=str(root), capture_output=True, text=True, check=False, timeout=900
    )


def _freshness(root: Path, entry: Provenance) -> str | None:
    """أعِدْ نصَّ الخَرمِ إن كانَ المنشورُ متقادمًا، وإلّا `None`."""
    published_path = root / MEASUREMENTS / entry.name
    if entry.strategy == "delegate":
        done = _run([sys.executable, *entry.probe[1:]], root)
        if done.returncode != 0:
            tail = (done.stdout + done.stderr).strip().splitlines()[-3:]
            return f"فحصُ المُولِّدِ سقطَ: {' / '.join(tail)}"
        return None

    if entry.strategy == "stdout":
        done = _run([sys.executable, *entry.probe[1:]], root)
        if done.returncode != 0:
            return f"تعذَّرَ إعادةُ القياسِ (خروجٌ {done.returncode}): {done.stderr.strip()[:200]}"
        try:
            fresh = json.loads(done.stdout)
        except json.JSONDecodeError as exc:
            return f"مخرَجُ إعادةِ القياسِ ليس JSON: {exc}"
    elif entry.strategy == "tmpfile":
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "fresh.json"
            argv = [sys.executable] + [
                (str(out) if a == "{out}" else a) for a in entry.probe[1:]
            ]
            done = _run(argv, root)
            if done.returncode != 0 or not out.exists():
                return (
                    f"تعذَّرَ إعادةُ القياسِ (خروجٌ {done.returncode}): "
                    f"{done.stderr.strip()[:200]}"
                )
            fresh = json.loads(out.read_text(encoding="utf-8"))
    else:  # pragma: no cover — يُمنَعُ قبلَ الوصولِ
        return None

    published = json.loads(published_path.read_text(encoding="utf-8"))
    old, new = _subset(published, entry), _subset(fresh, entry)
    if old == new:
        return None
    drifted = sorted(k for k in set(old) | set(new) if old.get(k) != new.get(k))
    detail = "; ".join(
        f"{k}: منشورٌ {str(old.get(k))[:60]} · مقيسٌ {str(new.get(k))[:60]}"
        for k in drifted[:4]
    )
    return f"القياسُ المنشورُ متقادمٌ في {len(drifted)} حقلًا — {detail}"


def audit(
    root: Path, freshness: bool = True, deps: bool | None = None
) -> tuple[list[str], dict[str, int]]:
    """احكمْ على العقدِ كلِّه وأعِدْ (الخُرومَ، العدَّ).

    `deps` يقسمُ **إعادةَ القياسِ وحدَها**، لا بنودَ العقدِ: `None` = الكلُّ ·
    `False` = ما لا يحتاجُ حزمًا خارجيّةً (وظيفةُ التدقيقِ بلا تنصيبٍ) · `True` =
    ما يحتاجُها (وظيفةٌ مُنصِّبةٌ). والقسمةُ ليست إعفاءً: بنودُ العقدِ السبعةُ
    تُفحَصُ في الشطرَينِ، والمُؤَجَّلُ **يُعَدُّ ويُطبَعُ** في كلِّ تشغيلٍ، وربطُ
    الشطرَينِ في CI محروسٌ بفحصٍ يقرأُ ملفَّ الوقائعِ نصًّا — فحارسٌ يُتخطَّى
    بصمتٍ ليس حارسًا (القاعدةُ 10 · W-012).

    `freshness=False` يفحصُ العقدَ وحدَه بلا إعادةِ قياسٍ. وهو ليس تخفيفًا للحكمِ
    بل فصلٌ لازمٌ: إعادةُ قياسِ `final_audit_p14.json` تقرأُ سجلَّ git، فوظيفةٌ
    تستنسخُ بعمقِ واحدٍ لا تصلحُ لها — فتُفحَصُ فيها بنودُ العقدِ التي لا تحتاجُ
    سجلًّا، وتبقى الطزاجةُ في الوظيفةِ التي تجلبُ السجلَّ كاملًا.
    """
    breaches: list[str] = []
    deferred: list[str] = []
    directory = root / MEASUREMENTS
    if not directory.is_dir():
        return [f"مجلَّدُ القياساتِ مفقودٌ: {MEASUREMENTS}"], {}

    registered = {e.name: e for e in REGISTRY}

    # 1) تغطيةٌ في الاتجاهَينِ: لا ملفَّ بلا قيدٍ، ولا قيدَ بلا ملفٍّ.
    on_disk = {p.name for p in directory.iterdir() if p.is_file()}
    for name in sorted(on_disk - set(registered) - set(PROSE_FILES)):
        breaches.append(
            f"{name}: قياسٌ منشورٌ بلا قيدِ نَسَبٍ — يُقيَّدُ في REGISTRY أو لا يُنشَر."
        )
    for name in sorted(set(registered) - on_disk):
        breaches.append(f"{name}: قيدُ نَسَبٍ بلا ملفٍّ منشورٍ — يُحذَفُ القيدُ أو يُنشَرُ الملفُّ.")

    for entry in REGISTRY:
        path = directory / entry.name
        if entry.strategy not in STRATEGIES:
            breaches.append(f"{entry.name}: وضعُ إعادةِ قياسٍ مجهولٌ: {entry.strategy}")
        if not path.exists():
            continue

        # 2) المُولِّدُ المُعلَنُ موجودٌ فعلًا — لا نَسَبَ إلى معدومٍ.
        if entry.generator and not (root / entry.generator).exists():
            breaches.append(
                f"{entry.name}: المُولِّدُ المُعلَنُ مفقودٌ من الشجرةِ: {entry.generator}"
            )

        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            breaches.append(f"{entry.name}: ليس JSON صحيحًا: {exc}")
            continue

        # 3) ترويسةُ الملفِّ تُسمّي مُولِّدَه — فلا ينحرفُ النصُّ عن القيدِ صامتًا.
        header = str(payload.get("$comment", ""))
        if not header:
            breaches.append(f"{entry.name}: بلا ترويسةِ `$comment` — المادةُ التاسعةُ · 2.")
        elif entry.generator and entry.generator not in header:
            breaches.append(
                f"{entry.name}: الترويسةُ لا تُسمّي المُولِّدَ المُقيَّدَ "
                f"({entry.generator}) — القيدُ والنصُّ افترقا."
            )

        # 4) لا مسارَ جهازِ عاملٍ في قياسٍ منشورٍ — علّةُ W-035 تُمنَعُ لا تُستثنى.
        for hit in _machine_paths(payload):
            breaches.append(f"{entry.name}: مسارُ جهازٍ منشورٌ في القياسِ: {hit}")

        # 5) ما لا يُعادُ قياسُه يجبُ أن يُعلِنَ سببَه؛ وما له استثناءُ حقلٍ كذلك.
        if entry.strategy == "declared" and not entry.reason.strip():
            breaches.append(f"{entry.name}: مُعلَنٌ بلا إعادةِ قياسٍ وبلا سببٍ مكتوبٍ.")
        if entry.ignore and not entry.reason.strip():
            breaches.append(f"{entry.name}: يستثني حقولًا بلا سببٍ مكتوبٍ: {entry.ignore}")
        if entry.strategy != "declared" and not entry.probe:
            breaches.append(f"{entry.name}: وضعُه يقتضي أمرَ قياسٍ ولا أمرَ له.")

        # 6) الطزاجةُ نفسُها — لِمَن يُمكِنُ قياسُه بلا كتابةٍ في الشجرة.
        #    والقسمةُ على الحزمِ اللازمةِ: لا تخطٍّ صامتٌ بل تأجيلٌ مُعلَنٌ معدودٌ.
        if freshness and entry.strategy != "declared" and entry.probe:
            if deps is None or bool(entry.needs) is deps:
                breach = _freshness(root, entry)
                if breach:
                    breaches.append(f"{entry.name}: {breach}")
            else:
                deferred.append(entry.name)

        # 7) ما يحتاجُ حزمًا خارجيّةً لا يكونُ مُعلَنًا بلا حرسٍ — وإلّا صارَ
        #    حقلُ `needs` بابًا خلفيًّا للإعفاءِ من الحرسِ بلا سببٍ.
        if entry.needs and entry.strategy == "declared":
            breaches.append(
                f"{entry.name}: يُعلِنُ حزمًا لازمةً ({', '.join(entry.needs)}) وهو "
                f"مُعلَنٌ بلا حرسٍ — حقلُ `needs` قسمةٌ لا إعفاءٌ."
            )

    guarded = sum(1 for e in REGISTRY if e.strategy != "declared")
    counts = {
        "registered": len(REGISTRY),
        "guarded": guarded,
        "declared_only": len(REGISTRY) - guarded,
        "needs_deps": sum(1 for e in REGISTRY if e.needs),
        "deferred": len(deferred),
    }
    return breaches, counts


def report(root: Path) -> str:
    """اطبعِ العقدَ كما هو — ليُقرَأَ الباقي بلا حرسٍ رقمًا لا انطباعًا."""
    lines = ["# نَسَبُ القياساتِ المنشورةِ — W-037", ""]
    for entry in sorted(REGISTRY, key=lambda e: (e.strategy == "declared", e.name)):
        mark = "مُعلَنٌ فقط" if entry.strategy == "declared" else f"محروسٌ ({entry.strategy})"
        lines.append(f"- {entry.name} — {mark}")
        lines.append(f"  المُولِّدُ: {entry.generator or '— لا مُولِّدَ برمجيًّا —'}")
        lines.append(f"  الأمرُ: {entry.command}")
        if entry.needs:
            lines.append(f"  يحتاجُ: {', '.join(entry.needs)} — يُفحَصُ بـ`--only-deps`")
        if entry.reason:
            lines.append(f"  السببُ: {entry.reason}")
    guarded = sum(1 for e in REGISTRY if e.strategy != "declared")
    lines += [
        "",
        f"المقيَّدُ: {len(REGISTRY)} · المحروسُ بإعادةِ قياسٍ: {guarded} · "
        f"المُعلَنُ بلا حرسٍ: {len(REGISTRY) - guarded}",
    ]
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    root = Path(args[0] if args else ".").resolve()

    if "--report" in flags or not flags:
        print(report(root))
        if "--check" not in flags:
            return 0

    if "--only-deps" in flags and "--without-deps" in flags:
        print("لا تُجمَعُ `--only-deps` و`--without-deps`: القسمةُ شطرانِ لا شطرٌ واحدٌ.",
              file=sys.stderr)
        return 2
    deps: bool | None = None
    if "--only-deps" in flags:
        deps = True
    elif "--without-deps" in flags:
        deps = False
    breaches, counts = audit(
        root, freshness="--contract-only" not in flags, deps=deps
    )
    if breaches:
        print("سقطَ عقدُ نَسَبِ القياساتِ (W-037):", file=sys.stderr)
        for breach in breaches:
            print(f"  · {breach}", file=sys.stderr)
        print(
            "\nالقاعدةُ: لا ملفَّ بلا قيدٍ، ولا قيدَ بلا سببٍ. "
            "أعِدْ توليدَ المتقادمِ بأمرِه المُقيَّدِ، أو قيِّدْ ما نُشِرَ بلا قيدٍ.",
            file=sys.stderr,
        )
        return 1
    line = (
        f"عقدُ نَسَبِ القياساتِ مستقيمٌ: {counts['registered']} قياسًا مقيَّدًا · "
        f"{counts['guarded']} محروسًا بإعادةِ قياسٍ · "
        f"{counts['declared_only']} مُعلَنًا بسببٍ مكتوبٍ."
    )
    if counts.get("deferred"):
        # يُطبَعُ المُؤَجَّلُ رقمًا لا صمتًا: مَن قرأَ سطرَ الخُضرةِ يعرفُ ما لم يُقَسْ هنا.
        line += (
            f" ومُؤَجَّلٌ إلى الشطرِ الآخرِ: {counts['deferred']} "
            f"(‏من {counts['needs_deps']} يحتاجُ حزمًا خارجيّةً)."
        )
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
