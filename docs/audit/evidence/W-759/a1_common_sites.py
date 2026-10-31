"""
الهدف: سردُ مواضعِ الكتابةِ غيرِ المحروسةِ في `common/` من الجردِ الحيِّ (`tools/audit/sovereign_write_inventory.py`) على الشجرةِ الحاليّة — قياسُ «الـ28» في ورقةِ المالكِ A1 (ج)/(د) (W-759).
الاستعمال: python3 a1_common_sites.py  (من جذرِ المستودع)
"""
import sys

sys.path.insert(0, "tools/audit")
import sovereign_write_inventory as m  # noqa: E402

P = "federal/executive/services/src/amos_federation/common/"
sites = [x for x in m.collect(m.REPO_ROOT) if x["path"].startswith(P)] if isinstance(m.collect(m.REPO_ROOT)[0], dict) else None
if sites is None:
    sites = [x.__dict__ for x in m.collect(m.REPO_ROOT) if x.path.startswith(P)]
pub = [s for s in sites if s["public"] and not s["guarded"] and not s["closed_legacy"]]
print(f"مواضعُ common/ في الجرد: {len(sites)} · عامّةٌ غيرُ محروسة: {len(pub)} · خاصّة: {len(sites) - len([s for s in sites if s['public']])}")
for s in sites:
    print(f"{s['path'].removeprefix(P)}:{s['line']}\t{s['owner']}.{s['function']}\tpublic={s['public']}\tguarded={s['guarded']}")
