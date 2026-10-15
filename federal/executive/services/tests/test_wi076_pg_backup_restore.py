"""WI-076 — النسخُ الاحتياطيُّ والاستعادةُ على PostgreSQL بإثباتٍ كاملٍ (W-339).

الهدف:
    حرسُ قدرةِ الاستردادِ الجديدةِ: أداةُ `tools/ops/pg_backup_restore.py` تُثبِتُ
    دورةَ النسخِ والاستعادةِ على قاعدةٍ حقيقيةٍ، وهذا الحارسُ يشغّلُها **بأمرِها
    نفسِها ويُمسِكُ رمزَ خروجِها** — فلا يُقرأَ نجاحٌ من نصٍّ في مخرجٍ بل من
    الخروجِ الصفريِّ، ولا يُقبلُ فشلٌ صامتٌ.

النطاق:
    حزمةُ PostgreSQL الحيّةِ فقط (تُشغَّلُ في حزمةِ services-postgres بلا تخطٍّ):
    `AMOS_RUN_POSTGRES_TESTS=1` معَ `AMOS_TEST_DATABASE_URL` تبدأُ بـpostgresql.
    القواعدُ التي تنشئها الأداةُ معزولةٌ ببادئةِ `wi076_` وتُهدمُ بعدَ كلِّ اختبار.

المالك: Perplexity Computer (WI-076 · W-339)
تاريخ الإنشاء: 2026-10-15 (WI-076)
تاريخ آخر تعديل: 2026-10-15 (WI-076 · المرّةُ الأولى)
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

SERVICES_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
TOOL = REPO_ROOT / "tools" / "ops" / "pg_backup_restore.py"
MIGRATIONS_DIR = SERVICES_DIR / "migrations"


def _pg_enabled() -> bool:
    return os.environ.get("AMOS_RUN_POSTGRES_TESTS") == "1" and os.environ.get(
        "AMOS_TEST_DATABASE_URL", ""
    ).startswith("postgresql")


pytestmark = pytest.mark.skipif(
    not _pg_enabled(),
    reason="Set AMOS_RUN_POSTGRES_TESTS=1 and AMOS_TEST_DATABASE_URL=postgresql://... to run",
)


def _run_tool(*args: str) -> subprocess.CompletedProcess:
    """تشغيلُ الأداةِ بأمرِها نفسِها — ورمزُ الخروجِ للأداةِ لا لـ`tail` بعدها."""
    return subprocess.run(
        [sys.executable, str(TOOL), *args],
        capture_output=True,
        text=True,
        env={**os.environ},
        cwd=str(REPO_ROOT),
    )


def _count_migrations() -> int:
    return len(sorted(MIGRATIONS_DIR.glob("[0-9][0-9][0-9]_*.sql")))


def test_wi076_prove_full_cycle_once() -> None:
    """الدورةُ الكاملةُ: مصدرٌ بالهجراتِ + كتابةٌ عبرَ الخدمةِ + نسخٌ + استعادةٌ + تحققٌ."""
    proc = _run_tool("prove", "--artifacts", "/tmp/wi076_test_artifacts")
    assert proc.returncode == 0, f"فشلُ الإثباتِ: {proc.stderr[-600:]}"
    # الخطواتُ الخمسُ المعلنةُ في معيارِ القبولِ كلُّها في المخرجِ
    for marker in (
        "أنشأَ المصدرَ",
        "هجرةً",
        "مسارِ الخدمةِ",
        "pg_dump",
        "استعادَ بـpg_restore",
        "صفرُ اختلافٍ",
    ):
        assert marker in proc.stdout, f"خطوةٌ غائبةٌ من المخرجِ: {marker}"
    # المصدرُ والهدفُ هُدما — لا بقايا قواعدَ الاختبارِ
    assert "wi076_" not in _list_wi076_databases()


def test_wi076_prove_is_repeatable() -> None:
    """قابليةُ التكرارِ: تشغيلانِ مستقلّانِ على قواعدَ جديدةٍ ينتهيانِ بصفرٍ."""
    for attempt in (1, 2):
        proc = _run_tool("prove", "--artifacts", f"/tmp/wi076_test_artifacts_{attempt}")
        assert proc.returncode == 0, f"المحاولةُ {attempt} فشلت: {proc.stderr[-600:]}"


def test_wi076_negative_probes_all_fail_as_required() -> None:
    """السلبيّاتُ الثلاثةُ — كلُّ واحدٍ منها يجبُ أن يُرفَضَ صراحةً لا أن ينجحَ بصمتٍ."""
    proc = _run_tool("probe-negative", "--artifacts", "/tmp/wi076_test_artifacts")
    assert proc.returncode == 0, f"سلبيٌّ لم يُرفَضْ كما يجبُ: {proc.stdout[-600:]}"
    for name in ("corrupt_dump", "missing_dump", "same_target"):
        assert f"{name}: " in proc.stdout, f"سلبيةٌ غائبةٌ: {name}"
        assert "كما يجبُ" in proc.stdout, f"السلبيةُ {name} لم تُرفَضْ بشكلٍ صحيحٍ"
    assert "wi076_" not in _list_wi076_databases()


def test_wi076_migrations_are_the_declared_schema_source() -> None:
    """معيارُ القبولِ 1: مصدرُ المخططِ الهجراتُ المعتمدةُ — عدُّها معلَنٌ ومقيسٌ."""
    count = _count_migrations()
    assert count >= 19, f"هجراتٌ أقلَّ من المعروفِ (19): {count}"
    proc = _run_tool("prove", "--artifacts", "/tmp/wi076_test_artifacts_count")
    assert proc.returncode == 0
    assert (
        f"طبّقَ {count} هجرةً" in proc.stdout
    ), f"المخرجُ لا يذكرُ العددَ المقيسَ {count}: {proc.stdout[-400:]}"


def _list_wi076_databases() -> str:
    """جردُ قواعدِ الاختبارِ الباقيةِ — يجبُ أن تكونَ فارغًا بعدَ كلِّ اختبار."""
    from sqlalchemy import create_engine, text

    from amos_federation.common.database import with_declared_driver

    url = with_declared_driver(os.environ["AMOS_TEST_DATABASE_URL"])
    engine = create_engine(url, isolation_level="AUTOCOMMIT")
    try:
        with engine.connect() as conn:
            rows = conn.execute(
                text(
                    "SELECT datname FROM pg_database "
                    "WHERE datname LIKE 'wi076_%' ORDER BY datname"
                )
            ).all()
        return ",".join(r[0] for r in rows)
    finally:
        engine.dispose()
