"""
الهدف: إعادةُ قياسِ مستدعي مواضعِ A1 للفئتين (ج) و(د) على الشجرةِ الحاليّةِ بالمنهجِ نفسِه لـW-639 (نداءُ صفةٍ باسمِ الفعلِ + المستقبِلُ) — أداةُ قياسٍ لورقةِ المالكِ A1 (ج)/(د) في دليلِ W-758، لا شِفرةَ إنتاج.
الاستعمال: python3 a1cd_remeasure.py <repo_root>
المنهج: (1) تشغيلُ a1_callers.py.txt من W-639 نفسِه على الشجرة؛ (2) التصفيةُ بأزواجِ (الفعل، المستقبِل) المستخرجةِ حرفيًّا من a1_callers_filtered.txt في W-639؛
(3) طباعةُ المستقبِلاتِ «المرشَّحةِ الجديدة» لنفسِ الأفعالِ التي يدلُّ اسمُها على مخزنٍ/حافلةٍ/تدقيقٍ ولم تكن في مرشِّحِ W-639 — للإفصاحِ لا للعدّ.
"""
import pathlib, re, subprocess, sys
from collections import Counter
root = pathlib.Path(sys.argv[1])
ev = root / "docs/audit/evidence/W-639"
filt = (ev / "a1_callers_filtered.txt").read_text().splitlines()
pairs = set()
for ln in filt:
    m, _loc, recv, _in = ln.split("\t")
    pairs.add((m, recv))
methods = sorted({m for m, _ in pairs})
raw = subprocess.run([sys.executable, str(ev / "a1_callers.py.txt"), str(root), ",".join(methods)],
                     capture_output=True, text=True, check=True).stdout.splitlines()
kept, cand, excluded = [], [], []
hint = re.compile(r"audit|bus|store|publisher|memory|experience|critic|promotion|system_state", re.I)
skipped = 0
for ln in raw:
    if ln.count("\t") != 3:  # مستقبِلٌ متعدّدُ الأسطرِ في مخرجِ أداةِ W-639 — يُعَدُّ ويُفصَحُ عنه
        skipped += 1
        continue
    m, loc, recv, scope = ln.split("\t")
    if loc.startswith(("docs/", "core/")):  # تعريفُ «الإنتاج» في W-639 § 0: docs/ مستبعَد، وcore/ مستقبِلُه من نوعٍ آخر
        excluded.append(ln)
        continue
    if (m, recv) in pairs:
        kept.append(ln)
    elif hint.search(recv):
        cand.append(ln)
SITE = {  # الفعل/المستقبِل → البند في جدولِ W-639 § 3
    "append": "8 PersistentAuditStore.append", "store": "5 PersistentMemoryStore.store",
    "record": "6 PersistentExperienceStore.record",
}
def site(ln):
    m, loc, recv, scope = ln.split("\t")
    if m == "publish":
        r = recv.split("=", 1)[1]
        if r == "get_durable_event_bus()": return "25 DurableEventBus.publish"
        if r == "event_publisher": return "28 EventPublisher.publish"
        return "27 EventBus.publish"
    return SITE.get(m, f"other:{m}")
c = Counter(site(l) for l in kept)
wiring = Counter(site(l) for l in kept if "common/event_wiring.py" in l)
print("== أسطرٌ خامٌ متشظّيةٌ (مستقبِلٌ متعدّدُ الأسطر) لم تُصنَّف:", skipped)
print("== الأزواجُ المحفوظةُ من مرشِّحِ W-639:", len(pairs), "· النداءاتُ المطابقةُ الآن:", len(kept))
print("== العدُّ لكلِّ موضعٍ (ج) [منها في event_wiring.py الذي لا يبلغُه الإنتاج]")
for k in sorted(c, key=lambda s: int(s.split()[0]) if s[0].isdigit() else 99):
    if k.split()[0] in {"5", "6", "8", "25", "27", "28"}:
        print(f"{k}\t{c[k]}\t[wiring {wiring.get(k,0)}]")
print("== المطابقُ كاملًا (ج):")
for l in kept:
    if site(l).split()[0] in {"5", "6", "8", "25", "27", "28"}:
        print(l)
print("== مستبعَدٌ بتعريفِ الإنتاج (docs/ وcore/):", len(excluded))
print("== مرشَّحون جددٌ لم يكونوا في مرشِّحِ W-639 (للإفصاح لا للعدّ):", len(cand))
for l in cand: print(l)
