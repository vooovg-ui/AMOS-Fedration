"""مسبارُ المعيارِ الخامسِ (الفرعُ الرابعُ) — رفضُ الاستعادةِ على قاعدةٍ مستقلةٍ غيرِ فارغةٍ.

التعريف:
    سكربتُ إثباتٍ قابلٌ للإعادةِ: يُنشئ مصدرًا وهجراتٍ ونسخةً صالحةً، ثم قاعدةً
    مستقلةً فيها جدولٌ واحدٌ وصفٌّ واحدٌ، ويحاولُ الاستعادةَ عليها — فيجبُ أن
    تُرفضَ قبلَ أيِّ كتابةٍ («قاعدةٍ غيرِ فارغةٍ») وأن تبقى القاعدةُ كما هي.

النطاق:
    جولةُ W-346 على بندِ WI-076 (المعيارُ 5 · فروعُه الأربعةِ) — يُشغَّلُ من جذرِ
    المستودعِ على PostgreSQL حيٍّ (البيئةُ أدناه).

المالك:
    Perplexity Computer (WI-076 · منفِّذُ الجولةِ — والحكمُ للمقعدِ الوحيدِ Q-G).

تاريخ الإنشاء: 2026-10-15 (WI-076 · W-346)
تاريخ آخر تعديل: 2026-10-15 (WI-076 · المرّةُ الأولى)

المحتويات:
    إعادةُ التشغيلِ (من جذرِ المستودعِ):
        PATH=/…/postgresql-18.6.0…/bin:$PATH \\
        LD_LIBRARY_PATH=/tmp/pglibs/usr/lib/x86_64-linux-gnu \\
        AMOS_DB_SSLMODE=disable \\
        .venv/bin/python docs/audit/evidence/W-346/nonempty_probe_script.py
    الخرجُ المتوقعُ: رفضٌ «قاعدةٍ غيرِ فارغةٍ» قبلَ أيِّ كتابةٍ · القاعدةُ
    المستقلةُ لم تُمسَّ · NONEMPTY_PROBE_OK (والدليلُ المُسجَّلُ في
    nonempty_target_run.log).
"""

from __future__ import annotations

import importlib.util
import sys
import uuid
from pathlib import Path

spec = importlib.util.spec_from_file_location("pgbr", "tools/ops/pg_backup_restore.py")
m = importlib.util.module_from_spec(spec)
sys.modules["pgbr"] = m
spec.loader.exec_module(m)

url = "postgresql://postgres@127.0.0.1:5433/postgres"
suffix = uuid.uuid4().hex[:10]
source = f"wi076_probe_{suffix}"
nonempty = f"wi076_nonempty_{suffix}"
art = Path("/tmp/w346_artifacts")
art.mkdir(exist_ok=True)
ok = True
try:
    m.create_database(url, source)
    m.apply_migrations(url, source)
    dump = art / f"{source}.dump"
    m.dump_database(url, source, dump)
    m.create_database(url, nonempty)
    from sqlalchemy import create_engine, text

    eng = create_engine(m._url_for(url, nonempty))
    with eng.connect() as c:
        c.execute(text("CREATE TABLE probe_marker (id int)"))
        c.execute(text("INSERT INTO probe_marker VALUES (1)"))
        c.commit()
    eng.dispose()
    m._CURRENT_SOURCE = source
    try:
        m.restore_database(url, nonempty, dump)
        print("FAIL: قبل الاستعادةُ على قاعدةٍ غيرِ فارغةٍ — عيبُ P0")
        ok = False
    except m.ProofError as exc:
        if "غيرِ فارغةٍ" in str(exc):
            print(f"✓ رُفضَ كما يجبُ: {exc}")
        else:
            print(f"؟ رُفضَ لسببٍ آخرَ: {exc}")
            ok = False
    eng2 = create_engine(m._url_for(url, nonempty))
    with eng2.connect() as c:
        rows = c.execute(text("SELECT count(*) FROM probe_marker")).scalar_one()
        tables = c.execute(
            text(
                "SELECT count(*) FROM information_schema.tables "
                "WHERE table_schema='public'"
            )
        ).scalar_one()
    eng2.dispose()
    print(f"✓ القاعدةُ المستقلةُ لم تُمسَّ: probe_marker={rows} صفًّا · جداولُ public={tables}")
    if rows != 1 or tables != 1:
        ok = False
finally:
    m.drop_database(url, source)
    m.drop_database(url, nonempty)
print("NONEMPTY_PROBE_OK" if ok else "NONEMPTY_PROBE_FAIL")
sys.exit(0 if ok else 1)
