#!/usr/bin/env python3
"""النسخُ الاحتياطيُّ والاستعادةُ لقاعدةِ خدماتِ الاتحادِ على PostgreSQL (WI-076 · W-339).

الهدف:
    إثباتُ قدرةِ استردادٍ واحدةٍ مفقودةٍ مقيسةً: بطاقةُ `docs/audit/backups/README.md`
    تعلنُ «النسخُ التشغيليةُ الكاملةُ UNAVAILABLE — لا استرجاعًا مُختبَرًا»، والخطوةُ
    18 من خارطةِ الطريقِ (T4/E4) تنصُّ «نسخٌ احتياطي» ضمنَ إتمامِ E4. هذه الأداةُ
    تسدُّ الشقَّ المتاحَ بلا مفتاحِ مالكٍ: نسخُ قاعدةٍ حقيقيةٍ بـ`pg_dump` واستعادتُها
    بـ`pg_restore` إلى قاعدةٍ معزولةٍ ثانيةٍ، وإثباتُ عودةِ البياناتِ من اتصالٍ
    جديدٍ لا من ذاكرةِ عمليّةٍ قديمة.

النطاق:
    قواعدُ اختبارٍ معزولةٌ يُنشئها المُثبِتُ بنفسِهِ (بادئةُ `wi076_`) ويُهدمها بعده.
    مصدرُ المخططِ **الهجراتُ المعتمدةُ** `federal/executive/services/migrations/001-019`
    بالترتيبِ — لا `create_all`. الكتابةُ عبرَ مسارِ الخدمةِ القائمِ
    (`PersistentSystemStateStore` · `PersistentPromotionStore`) لا بـSQL خامٍ.
    **لا تَمسُّ هذه الأداةُ قاعدةَ إنتاجٍ ولا قاعدةَ المالكِ**: ترفضُ الاستعادةَ على
    المصدرِ نفسِهِ وعلى قاعدةٍ غيرِ فارغةٍ، ولا تُنشئُ قاعدةً بغيرِ بادئةِ `wi076_`.

المالك: tools/ops — بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-10-15 (WI-076)
تاريخ آخر تعديل: 2026-10-15 (WI-076 · المرّةُ الأولى)

طريق الإنفاذ: NEEDS_LIVE_DB — يلزمه رابطُ قاعدةِ بياناتٍ حيٍّ فيرفضُ بدونه (رمزُ 2)؛
    وهو مُثبِتُ قدرةٍ لا بوّابةُ حوكمةٍ، وإثباتُه المُختبَرُ في حزمةِ services-postgres
    (`test_wi076_pg_backup_restore.py` يشغّلُه بأمرِه ورمزِ خروجِه)
    `prove`    ⇒ الإثباتُ الكاملُ (مصدرٌ بالهجراتِ + كتابةٌ + نسخٌ + استعادةٌ + تحققٌ
                من اتصالٍ جديدٍ) — خرجٌ 0 عندَ النجاحِ وغيرُ صفريٍّ عندَ أيِّ فشلٍ.
    `probe-negative` ⇒ ثلاثةُ سلبيّاتٍ (نسخةٌ تالفةٌ · نسخةٌ مفقودةٌ · استعادةٌ على
                المصدرِ نفسِهِ) — خرجٌ 0 فقط إذا فشِلَ كلُّ سلبيٍّ كما يجبُ.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import subprocess
import sys
import uuid
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

# جذرُ القياسِ بعلامةٍ لا بعُمقٍ مكتوبٍ — نمطُ المستودعِ (DISC-041 · سابقةُ W-336)
_ROOT_FINDER_PATH = Path(__file__).resolve().parents[1] / "governance" / "repo_root.py"
_ROOT_FINDER_SPEC = importlib.util.spec_from_file_location(
    "amos_repo_root_finder", _ROOT_FINDER_PATH
)
if _ROOT_FINDER_SPEC is None or _ROOT_FINDER_SPEC.loader is None:
    raise ImportError(f"repo_root.py not loadable from {_ROOT_FINDER_PATH}")
_ROOT_FINDER = importlib.util.module_from_spec(_ROOT_FINDER_SPEC)
_ROOT_FINDER_SPEC.loader.exec_module(_ROOT_FINDER)
REPO_ROOT = _ROOT_FINDER.discover_repo_root(__file__)
MIGRATIONS_DIR = REPO_ROOT / "federal" / "executive" / "services" / "migrations"
TEST_DB_PREFIX = "wi076_"

#: بياناتُ الإثباتِ المميّزةُ — تُكتَبُ عبرَ مسارِ الخدمةِ وتُقرأُ من المستعادةِ.
HALT_STATE = {
    "level": "halt",
    "reason": "wi076: إثباتُ النسخِ والاستعادةِ — سببٌ مميّزٌ لا يُتوقَّعُ صدفةً",
    "activated_at": "2026-10-15T12:00:00Z",
    "activated_by": "wi076-probe",
}
PROMOTION = {
    "promotion_id": "wi076-probe-promotion",
    "model_id": "wi076-probe-model",
    "gates": {"human_approval": "granted", "canary": "passed"},
    "status": "in_progress",
    "created_at": "2026-10-15T12:00:00Z",
    "updated_at": "2026-10-15T12:01:00Z",
}


class ProofError(RuntimeError):
    """فشلُ خطوةٍ من خطواتِ الإثباتِ — رسالتُه السببُ ورمزُ الخروجِ غيرُ الصفريِّ."""


def _sslmode() -> str:
    """نمطُ SSL من البيئةِ كما تفعلُ CI لحاويتِها الزائلةِ (AMOS_DB_SSLMODE)."""
    return os.environ.get("AMOS_DB_SSLMODE", "require")


def _with_driver(url: str) -> str:
    """إعلانُ المُشغِّلِ صراحةً — افتراضُ SQLAlchemy 2.1 تغيّرَ إلى psycopg 3 غيرِ المُعلَنِ.

    سابقةُ المستودعِ نفسِه: `with_declared_driver` في `common/database.py` (DISC-067).
    """
    if url.startswith("postgresql://"):
        return "postgresql+psycopg2://" + url[len("postgresql://") :]
    return url


def _parse_url(url: str) -> dict:
    parts = urlsplit(url)
    return {
        "scheme": parts.scheme,
        "netloc": parts.netloc,
        "host": parts.hostname or "localhost",
        "port": parts.port or 5432,
        "user": parts.username or "",
        "password": parts.password or "",
    }


def _url_for(url: str, database: str, *, with_sslmode: bool = True) -> str:
    """رابطٌ لنفسِ الخادمِ نحوَ قاعدةٍ مسمّاةٍ (معَ إعلانِ المُشغِّلِ ومحلولِ SSL)."""
    parts = urlsplit(url)
    scheme = (
        "postgresql+psycopg2" if parts.scheme.startswith("postgresql") else parts.scheme
    )
    netloc = parts.netloc
    query = ""
    if with_sslmode:
        query = f"sslmode={_sslmode()}"
    return urlunsplit((scheme, netloc, f"/{database}", query, ""))


def _dsn_for(url: str, database: str) -> str:
    """DSN بلا مُشغِّلِ SQLAlchemy — لأدواتِ سطرِ الأوامرِ pg_dump/pg_restore/psql."""
    parts = urlsplit(url)
    auth = ""
    if parts.username:
        auth = parts.username
        if parts.password:
            auth += f":{parts.password}"
        auth += "@"
    netloc = f"{parts.hostname or 'localhost'}:{parts.port or 5432}"
    return f"postgresql://{auth}{netloc}/{database}?sslmode={_sslmode()}"


def _run(cmd: list[str], *, label: str) -> subprocess.CompletedProcess:
    """تشغيلُ أمرٍ والتقاطُ رمزِ خروجِه هو — لا رمزِ `tail` بعده (عيبُ P1 المُعلن)."""
    proc = subprocess.run(cmd, capture_output=True, text=True)  # noqa: S603 - أوامر مبنية داخليًا
    if proc.returncode != 0:
        raise ProofError(
            f"{label}: خرجَ برمزِ {proc.returncode} — "
            f"stderr: {proc.stderr.strip()[:400] or '(فارغ)'}"
        )
    return proc


def _admin_engine(url: str):
    from sqlalchemy import create_engine

    return create_engine(_with_driver(url), isolation_level="AUTOCOMMIT")


def create_database(admin_url: str, name: str) -> None:
    if not name.startswith(TEST_DB_PREFIX):
        raise ProofError(
            f"رفضُ إنشاءِ قاعدةٍ خارجَ نطاقِ الاختبارِ: {name!r} (البادئةُ المسموحةُ {TEST_DB_PREFIX})"
        )
    with _admin_engine(admin_url).connect() as conn:
        conn.exec_driver_sql(f'DROP DATABASE IF EXISTS "{name}"')
        conn.exec_driver_sql(f'CREATE DATABASE "{name}"')


def drop_database(admin_url: str, name: str) -> None:
    if not name.startswith(TEST_DB_PREFIX):
        return  # لا تُهدمْ قاعدةٌ ليست من هذا الإثباتِ أصلًا
    with _admin_engine(admin_url).connect() as conn:
        conn.exec_driver_sql(f'DROP DATABASE IF EXISTS "{name}"')


def apply_migrations(url: str, database: str) -> list[str]:
    """تطبيقُ الهجراتِ المعتمدةِ بالترتيبِ — مصدرُ المخططِ المعلنُ لا `create_all`.

    النمطُ هو نفسُه المُعتمدَ في `test_wi062_migrations_cover_orm_tables`: كلُّ ملفٍّ
    يحملُ BEGIN/COMMIT بنفسِه، فتُنفَّذُ بعباراتٍ خامٍّ على اتصالٍ واحدٍ.
    """
    from sqlalchemy import create_engine

    files = sorted(MIGRATIONS_DIR.glob("[0-9][0-9][0-9]_*.sql"))
    if not files:
        raise ProofError(f"لا هجراتٍ في {MIGRATIONS_DIR}")
    engine = create_engine(_url_for(url, database), isolation_level="AUTOCOMMIT")
    try:
        raw = engine.raw_connection()
        try:
            cur = raw.cursor()
            for f in files:
                cur.execute(f.read_text(encoding="utf-8"))
            cur.close()
        finally:
            raw.close()
    finally:
        engine.dispose()
    return [f.name for f in files]


def _write_through_service_path(url: str, database: str) -> dict:
    """كتابةُ بياناتِ الإثباتِ عبرَ مسارِ الخدمةِ القائمِ لا بـSQL مباشرٍ.

    المعيارُ المرجعيُّ للمقارنةِ هو **ما أعاده مسارُ الكتابةِ نفسُه** — فالإثباتُ
    يقيسُ أنَّ الاستعادةَ أعادتْ ما كتبَهُ المسارُ فعلًا، لا ما افتُرِضَ أنّه كُتِبَ.
    """
    os.environ["AMOS_DATABASE_URL"] = _url_for(url, database, with_sslmode=False)
    os.environ["AMOS_DB_SSLMODE"] = _sslmode()
    from amos_federation.common import persistent
    from amos_federation.common.database import reset_engine

    reset_engine()
    state_store = persistent.PersistentSystemStateStore()
    written_halt = state_store.set_level(
        HALT_STATE["level"], HALT_STATE["reason"], HALT_STATE["activated_by"]
    )
    promo_store = persistent.PersistentPromotionStore()
    written_promo = promo_store.create(
        {
            "promotion_id": PROMOTION["promotion_id"],
            "model_id": PROMOTION["model_id"],
            "gates": PROMOTION["gates"],
            "status": PROMOTION["status"],
            "created_at": PROMOTION["created_at"],
            "updated_at": PROMOTION["updated_at"],
        }
    )
    reset_engine()
    return {"halt": written_halt, "promotion": written_promo}


def _read_through_service_path(url: str, database: str) -> dict:
    """قراءةٌ من اتصالٍ جديدٍ كليًّا على القاعدةِ المستعادةِ — لا ذاكرةَ قديمةَ."""
    os.environ["AMOS_DATABASE_URL"] = _url_for(url, database, with_sslmode=False)
    os.environ["AMOS_DB_SSLMODE"] = _sslmode()
    from amos_federation.common import persistent
    from amos_federation.common.database import reset_engine

    reset_engine()
    state = persistent.PersistentSystemStateStore()
    got_halt = state.get()
    promo = persistent.PersistentPromotionStore()
    got_promo = promo.get(PROMOTION["promotion_id"])
    reset_engine()
    return {"halt": got_halt, "promotion": got_promo}


def dump_database(url: str, database: str, out: Path) -> None:
    """النسخُ الاحتياطيُّ بصيغةٍ مخصّصةٍ (`-Fc`) — رمزُ خروجِ pg_dump هو الحكم."""
    out.parent.mkdir(parents=True, exist_ok=True)
    _run(
        ["pg_dump", "--format=custom", f"--file={out}", _dsn_for(url, database)],
        label=f"pg_dump لقاعدةِ {database}",
    )
    if not out.exists() or out.stat().st_size == 0:
        raise ProofError(f"النسخةُ {out} غيرُ موجودةٍ أو فارغةٌ بعدَ pg_dump")


def restore_database(
    url: str, database: str, dump: Path, *, expect_failure: bool = False
) -> None:
    """الاستعادةُ بـpg_restore إلى قاعدةٍ فارغةٍ — معَ حراسِ الأمانِ الثلاثةِ."""
    if not dump.exists():
        raise ProofError(f"النسخةُ المطلوبةُ غيرُ موجودةٍ: {dump}")
    _assert_restore_target_safe(url, database)
    proc = subprocess.run(
        ["pg_restore", "--dbname", _dsn_for(url, database), str(dump)],
        capture_output=True,
        text=True,
    )  # noqa: S603 - أوامر مبنية داخليًا
    if proc.returncode != 0:
        if expect_failure:
            return  # السلبيُّ فشِلَ كما يجبُ — هذا هو النجاحُ المطلوبُ
        raise ProofError(
            f"pg_restore خرجَ برمزِ {proc.returncode} — stderr: {proc.stderr.strip()[:400]}"
        )


def _assert_restore_target_safe(url: str, database: str) -> None:
    """P0: لا استعادةَ على المصدرِ نفسِهِ ولا على قاعدةٍ غيرِ فارغةٍ."""
    from sqlalchemy import create_engine, text

    source = _current_source_database()
    if database == source:
        raise ProofError(f"رفضُ الاستعادةِ على قاعدةِ المصدرِ نفسِها: {database}")
    engine = create_engine(_url_for(url, database))
    try:
        with engine.connect() as conn:
            tables = conn.execute(
                text(
                    "SELECT count(*) FROM information_schema.tables "
                    "WHERE table_schema = 'public'"
                )
            ).scalar_one()
    finally:
        engine.dispose()
    if tables != 0:
        raise ProofError(
            f"رفضُ الاستعادةِ على قاعدةٍ غيرِ فارغةٍ: {database} ({tables} جدولًا)"
        )


_CURRENT_SOURCE: str | None = None


def _current_source_database() -> str | None:
    return _CURRENT_SOURCE


def prove(url: str, artifacts_dir: Path) -> dict:
    """الإثباتُ الكاملُ — كلُّ خطوةٍ برمزِ خروجٍ محفوظٍ، والفشلُ في أيٍّ منها يُسقطُ الكلَّ."""
    global _CURRENT_SOURCE
    suffix = uuid.uuid4().hex[:10]
    source = f"{TEST_DB_PREFIX}src_{suffix}"
    target = f"{TEST_DB_PREFIX}dst_{suffix}"
    _CURRENT_SOURCE = source
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    steps: list[str] = []

    create_database(url, source)
    steps.append(f"أنشأَ المصدرَ {source}")
    try:
        migrations = apply_migrations(url, source)
        steps.append(f"طبّقَ {len(migrations)} هجرةً ({migrations[0]}…{migrations[-1]})")
        written = _write_through_service_path(url, source)
        steps.append("كتبَ الحالةَ والترقيةَ عبرَ مسارِ الخدمةِ (والمرجعُ ما أعاده المسارُ)")

        dump = artifacts_dir / f"{source}.dump"
        dump_database(url, source, dump)
        steps.append(f"نسخَ بـpg_dump إلى {dump.name} ({dump.stat().st_size} بايت)")

        create_database(url, target)
        steps.append(f"أنشأَ هدفَ الاستعادةِ {target}")
        try:
            restore_database(url, target, dump)
            steps.append("استعادَ بـpg_restore")

            got = _read_through_service_path(url, target)
            expected = written
            if got != expected:
                raise ProofError(
                    "اختلافٌ بينَ المصدرِ والمستعادةِ من اتصالٍ جديدٍ: "
                    f"المتوقعُ {expected} · المقروءُ {got}"
                )
            steps.append("قرأَ من اتصالٍ جديدٍ على المستعادةِ ⇒ صفرُ اختلافٍ")
        finally:
            drop_database(url, target)
    finally:
        drop_database(url, source)
    _CURRENT_SOURCE = None
    return {
        "steps": steps,
        "migrations": len(migrations),
        "source": source,
        "target": target,
    }


def probe_negative(url: str, artifacts_dir: Path) -> dict:
    """ثلاثةُ سلبيّاتٍ — كلُّ واحدٍ منها يجبُ أن يفشَلَ صراحةً لا أن ينجحَ بصمتٍ.

    السلبيةُ الأولى تستهدفُ قاعدةً فارغةً ثانيةً (لا المصدرَ) حتى يبلغَ `pg_restore`
    النسخةَ التالفةَ فعلًا — فلو استُهدِفَ المصدرُ لرفضَهُ حارسُ الأمانِ قبلَ بلوغِ
    أداةِ الاستعادةِ، ولَمَا قِيسَ الفشلُ الصحيحُ.
    """
    global _CURRENT_SOURCE
    suffix = uuid.uuid4().hex[:10]
    source = f"{TEST_DB_PREFIX}neg_{suffix}"
    target = f"{TEST_DB_PREFIX}negdst_{suffix}"
    _CURRENT_SOURCE = source
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    results: dict[str, str] = {}

    create_database(url, source)
    try:
        migrations = apply_migrations(url, source)
        dump = artifacts_dir / f"{source}.dump"
        dump_database(url, source, dump)

        # (1) نسخةٌ تالفةٌ على قاعدةٍ فارغةٍ ⇒ pg_restore يفشلُ صراحةً
        corrupt = artifacts_dir / f"{source}.corrupt.dump"
        corrupt.write_bytes(b"NOT-A-VALID-POSTGRES-DUMP-HEADER")
        create_database(url, target)
        try:
            try:
                restore_database(url, target, corrupt)
                results["corrupt_dump"] = "لم يفشلْ — عيبُ P1"
            except ProofError as exc:
                # الفشلُ الصريحُ هو المطلوبُ — ومعلومتُه تنتقلُ إلى التقريرِ
                results["corrupt_dump"] = f"فشِلَ كما يجبُ ({exc})"
        finally:
            drop_database(url, target)
        corrupt.unlink(missing_ok=True)

        # (2) نسخةٌ مفقودةٌ ⇒ رفضٌ قبلَ بلوغِ pg_restore
        try:
            restore_database(url, target, artifacts_dir / "wi076_missing.dump")
            results["missing_dump"] = "لم يرفضْ — عيبُ P1"
        except ProofError as exc:
            # الرفضُ الصريحُ هو المطلوبُ — ومعلومتُه تنتقلُ إلى التقريرِ
            results["missing_dump"] = f"رُفضَ كما يجبُ ({exc})"

        # (3) الاستعادةُ على المصدرِ نفسِهِ ⇒ رفضُ حارسِ الأمانِ
        try:
            restore_database(url, source, dump)
            results["same_target"] = "لم يرفضْ — عيبُ P0"
        except ProofError as exc:
            if "نفسِها" in str(exc):
                results["same_target"] = "رُفضَ كما يجبُ"
            else:
                results["same_target"] = f"رُفضَ لكنْ لسببٍ آخرَ: {exc}"
    finally:
        drop_database(url, source)
    _CURRENT_SOURCE = None
    return {"results": results, "migrations": len(migrations)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="النسخُ الاحتياطيُّ والاستعادةُ — WI-076")
    sub = parser.add_subparsers(dest="command", required=True)

    p_prove = sub.add_parser(
        "prove", help="الإثباتُ الكاملُ: مصدرٌ → نسخٌ → استعادةٌ → تحققٌ"
    )
    p_prove.add_argument("--url", default=os.environ.get("AMOS_TEST_DATABASE_URL", ""))
    p_prove.add_argument("--artifacts", type=Path, default=Path("/tmp/wi076_artifacts"))

    p_neg = sub.add_parser(
        "probe-negative", help="السلبيّاتُ الثلاثةُ — كلٌّ منها يجبُ أن يفشلَ"
    )
    p_neg.add_argument("--url", default=os.environ.get("AMOS_TEST_DATABASE_URL", ""))
    p_neg.add_argument("--artifacts", type=Path, default=Path("/tmp/wi076_artifacts"))

    args = parser.parse_args(argv)
    if not args.url.startswith("postgresql"):
        parser.error("يلزمُ --url برابطِ PostgreSQL (أو AMOS_TEST_DATABASE_URL)")

    try:
        if args.command == "prove":
            report = prove(args.url, args.artifacts)
            print("[WI-076] الإثباتُ الكاملُ:")
            for step in report["steps"]:
                print(f"  ✓ {step}")
            return 0
        report = probe_negative(args.url, args.artifacts)
        print("[WI-076] السلبيّاتُ الثلاثةُ:")
        ok = True
        for name, verdict in report["results"].items():
            mark = "✓" if ("كما يجبُ" in verdict) else "✗"
            ok = ok and ("كما يجبُ" in verdict)
            print(f"  {mark} {name}: {verdict}")
        return 0 if ok else 1
    except ProofError as exc:
        print(f"[WI-076] ✗ فشلُ الإثباتِ: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
