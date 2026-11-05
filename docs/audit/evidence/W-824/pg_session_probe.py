"""الهدف: مسبارٌ مؤقّتٌ قبلَ الشِّفرة يحوّلُ الجلسةَ كلَّها إلى PostgreSQL بعدَ تحميلِ conftest (W-824 · Q-99 البند 6).

التعريف: يُحمَّلُ بـ`-p pg_session_probe` و`PYTHONPATH` يشيرُ إلى هذا المجلد · يطبعُ `db_dialect()` مرّةً بعدَ الجمع
— لا يفحصُ اللهجةَ لكلِّ اختبار (ذاك في مُلحَقِ W-825).
النطاق: docs/audit/evidence/W-824
المالك: Perplexity Computer (WI-127)
تاريخ الإنشاء: 2026-11-05
"""

import os
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_collection_finish(session):
    os.environ["AMOS_DATABASE_URL"] = os.environ["AMOS_TEST_DATABASE_URL"]
    from amos_federation.common import database

    database.reset_engine()
    print("\n[pgprobe] dialect:", database.db_dialect())
