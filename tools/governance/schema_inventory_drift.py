#!/usr/bin/env python3
"""جردُ المخطَّطِ المُعلَنُ في `ARCHITECTURE.md` — يُقاسُ أو يُعلَنُ عجزُ قياسِه (W-055).

طريقُ الإنفاذ: PENDING_GATE_ITEM — ربطُه مشروعٌ (قِيسَ: 0.12ث · رمزُ 0) ومسارُ `.github/workflows/ci.yml` مقفولٌ بـWI-023 وهو IN_REVIEW

الهدف:
    إغلاقُ ما بقيَ مفتوحًا من الخطوةِ `T0.6`: كانَ في `ARCHITECTURE.md` جردٌ
    مقيسٌ بتاريخِه و«حدُّ صدقٍ» مكتوبٌ يقولُ نصًّا: «لا بوّابةَ في CI تحرسُ هذا
    القسم … وربطُ هذا الجردِ بأداةٍ تُقارِنُه بالقاعدةِ آليًّا يبقى بندًا
    مفتوحًا». فهذا الملفُّ هو ذاك البندُ مُنفَّذًا: يُقرأُ الجردُ المُعلَنُ
    **من الوثيقةِ نفسِها** فيصيرَ رقمًا يُقاسُ، لا نصًّا يُقرأُ.
النطاق:
    قراءةٌ محضة. لا يُعدِّلُ `ARCHITECTURE.md` ولا يكتبُ في قاعدةِ بياناتٍ ولا
    يُنشئُ جدولًا: يقرأُ الجردَ المُعلَنَ، ويقرأُ قياسًا حيًّا أو حِملًا محفوظًا،
    ويُعلِنُ الافتراقَ برمزِ خروج.
المالك: tools/governance — ديوانُ التدقيق، بتفويضٍ من المجلس التأسيسي
تاريخ الإنشاء: 2026-08-27
تاريخ آخر تعديل: 2026-08-27

لماذا أداةٌ لا فقرةٌ في وثيقة
-----------------------------
الجردُ المكتوبُ بيدٍ في `ARCHITECTURE.md` كُذِّبَ مرّةً بالقياسِ (`C-3` ثمَّ
`W-002`: كانَ يُعلِنُ 23 جدولًا والمقيسُ 85)، فرُفِعَ وحلَّ محلَّه **قياسٌ
مُؤرَّخٌ**. لكنَّ القياسَ المُؤرَّخَ يَبلى كما يَبلى الجردُ: لا شيءَ في الشجرةِ
كانَ يقرأُ تلك الأرقامَ أصلًا، فلو نقصَ جدولٌ أو تناقضَ المجموعُ مع تفصيلِه
لبقيَ النصُّ مُطمئنًّا. وهذه الأداةُ تفصلُ ثلاثةَ أشياءَ كانت مخلوطةً في جملةٍ
واحدةٍ («يلزمُه سرُّ خدمةٍ»):

1. **ما يُقاسُ بلا سرٍّ ولا شبكةٍ**: استقامةُ الجردِ المُعلَنِ في نفسِه —
   أن يكونَ موجودًا، وأن يُطابِقَ المجموعُ تفصيلَه، وأن يكونَ تاريخُه تاريخًا
   لا كلمةً، وألّا يكونَ في المستقبل. وهذا هو وضعُ `--check`، ويُشغَّلُ في أيِّ
   بيئةٍ.
2. **ما يلزمُه قاعدةٌ حيّةٌ**: مطابقةُ الجردِ بالواقع — وضعُ `--measure`
   بـ`AMOS_TRUTH_DB_URL`، أو وضعُ `--from-json` على حِملٍ قِيسَ خارجَ الشجرةِ
   وحُفِظَ (وبه تُعادُ المطابقةُ بلا سرٍّ).
3. **ما لا يُقاسُ**: طزاجةُ الرقمِ. عمرُ القياسِ يُحسَبُ ويُعلَنُ، ولا يُسقِطُ
   بوّابةً إلّا بـ`--enforce-staleness` صريحًا — لأنَّ إعادةَ القياسِ تلزمُها
   قاعدةٌ لا تملكُها البوّابةُ، وإسقاطٌ على ما لا يُستطاعُ عقوبةٌ لا حرسٌ
   (سابقةُ § 13.3 في خارطةِ العمل).

الحدُّ المُعلَنُ ولا يُزعَمُ أكثرُ منه
------------------------------------
* تُقاسُ **الأعدادُ** المُعلَنةُ: عددُ الجداولِ لكلِّ مخطَّطٍ وعددُ صفوفِ
  الجداولِ المذكورةِ. ولا يُقاسُ شكلُ جدولٍ ولا عمودٌ ولا قيدٌ ولا فهرسٌ —
  فمطابقةُ العددِ ليست مطابقةَ مخطَّط.
* لا تُعيدُ هذه الأداةُ كتابةَ `ARCHITECTURE.md`: بوّابةٌ تُصلِحُ ما تحكمُ عليه
  لا تُثبِتُ شيئًا (سابقةُ `W-037` · `W-038`).
* غيابُ مصدرِ القياسِ **رفضٌ مُصنَّفٌ** (رمز 2) لا حكمٌ: لا يُقالُ «لا افتراق»
  عن مقارنةٍ لم تُجرَ.

الاستعمالُ
---------
    python tools/governance/schema_inventory_drift.py --check
    python tools/governance/schema_inventory_drift.py --from-json live.json
    python tools/governance/schema_inventory_drift.py --measure \
        --json docs/audit/measurements/schema_inventory.json

يخرجُ بصفرٍ إن استقامَ المُعلَنُ وطابقَ المقيسَ، وبواحدٍ عندَ افتراقٍ أو تناقضٍ،
وباثنَينِ إذا عجزَ عن القياسِ أصلًا.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from pathlib import Path

#: جذرُ المستودعِ — يُشتَقُّ من موضعِ الملفِّ لا من مجلَّدِ التشغيل.
REPO_ROOT = Path(__file__).resolve().parents[2]

#: الوثيقةُ التي تحملُ الجردَ المُعلَن.
ARCHITECTURE = Path("ARCHITECTURE.md")

#: مُتغيِّراتُ البيئةِ التي يُقرأُ منها وصلُ القاعدةِ — لا سرَّ في الشجرة.
DSN_ENV = ("AMOS_TRUTH_DB_URL", "DATABASE_URL")

#: عنوانُ قسمِ الجردِ المُعلَن: «### المقيسُ في YYYY-MM-DD».
SECTION_RE = re.compile(r"^###\s+المقيسُ\s+في\s+(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)

#: صفُّ جداولِ مخطَّطٍ واحدٍ: «| جداولُ `public` | **86** |».
SCHEMA_ROW_RE = re.compile(
    r"^\|\s*جداولُ\s+`([A-Za-z_][A-Za-z0-9_]*)`\s*\|\s*\*\*([\d,]+)\*\*"
)

#: صفُّ المجموعِ وتفصيلِه: «| جداولُ … كلِّها | **122** (`public` 86 · …) |».
TOTAL_ROW_RE = re.compile(r"^\|\s*جداولُ\s+المخطَّطاتِ[^|]*\|\s*\*\*([\d,]+)\*\*([^|]*)\|")

#: زوجُ مخطَّطٍ وعددٍ داخلَ تفصيلِ المجموع: «`auth` 23».
BREAKDOWN_PAIR_RE = re.compile(r"`([A-Za-z_][A-Za-z0-9_]*)`\s*([\d,]+)")

#: صفُّ عددِ صفوفِ جدولٍ: «| صفوفُ `event_store` | **1,027** |».
ROWS_ROW_RE = re.compile(
    r"^\|\s*صفوفُ\s+`([A-Za-z_][A-Za-z0-9_.]*)`\s*\|\s*\*\*([\d,]+)\*\*"
)

#: إصدارُ المحرِّكِ المُعلَنُ في النصِّ: «PostgreSQL **17.6**».
VERSION_RE = re.compile(r"PostgreSQL\s+\*\*([\d.]+)\*\*")

#: ترويسةُ الملفِّ المنشورِ — تُسمّي مُولِّدَها كما تقتضي المادةُ التاسعةُ · 2
#: (‏`measurement_provenance.py` تُسقِطُ الدفعةَ على ترويسةٍ لا تُسمّي مُولِّدَها).
PUBLISHED_COMMENT = (
    "الهدف: مقابلةُ جردِ قاعدةِ البياناتِ **المُعلَنِ** في `ARCHITECTURE.md` "
    "بجردٍ **مقيسٍ** من قاعدةٍ حيّةٍ، فلا يبقى الجردُ نصًّا يُقرَأُ. "
    "النطاق: أعدادُ جداولِ المخطَّطاتِ وأعدادُ صفوفِ الجداولِ المذكورةِ وإصدارُ "
    "المحرِّكِ وحدَها — لا شكلَ جدولٍ ولا عمودٍ ولا فهرسٍ ولا قيدٍ. "
    "المالك: tools/governance. تاريخ الإنشاء: 2026-08-27. "
    "تاريخ آخر تعديل: 2026-08-27. "
    "المُولِّد: tools/governance/schema_inventory_drift.py."
)

#: استعلامُ الجردِ — هو نفسُه المكتوبُ في `ARCHITECTURE.md` تحتَ «كيف يُعادُ القياس».
SCHEMA_QUERY = """
select table_schema, count(*) as tables
from information_schema.tables
where table_type = 'BASE TABLE'
  and table_schema not in ('pg_catalog', 'information_schema')
group by 1 order by 2 desc
"""


class MeasurementRefused(RuntimeError):
    """عجزٌ عن القياسِ يُعلَنُ رفضًا مُصنَّفًا — لا يُبتلَعُ ولا يُقلَبُ حكمًا."""


@dataclass(frozen=True)
class Declared:
    """الجردُ كما هو مكتوبٌ في الوثيقةِ — لا كما يُتذكَّر."""

    measured_on: date
    version: str
    schemas: dict[str, int]
    breakdown_total: int
    rows: dict[str, int]
    source: str

    @property
    def breakdown_sum(self) -> int:
        return sum(self.schemas.values())


@dataclass
class Verdict:
    """حكمٌ على مقياسٍ واحدٍ — مُسمًّى، بقيمتَيه، لا برأيٍ مُجمَل."""

    metric: str
    declared: int | str | None
    live: int | str | None
    state: str  # MATCH · DRIFT · MISSING_LIVE · UNDECLARED

    @property
    def is_drift(self) -> bool:
        return self.state != "MATCH"


@dataclass
class Contract:
    """استقامةُ المُعلَنِ في نفسِه — تُقاسُ بلا قاعدةٍ ولا سرّ."""

    violations: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def read_declared(root: Path = REPO_ROOT) -> Declared:
    """يقرأُ الجردَ المُعلَنَ من `ARCHITECTURE.md`، أو يرفضُ مُعلِنًا سببَه."""
    path = root / ARCHITECTURE
    if not path.is_file():
        raise MeasurementRefused(f"لا وثيقةَ جردٍ في {ARCHITECTURE} — لا مُعلَنَ ليُقاس.")
    text = path.read_text(encoding="utf-8")

    section = SECTION_RE.search(text)
    if section is None:
        raise MeasurementRefused(
            "لا قسمَ «### المقيسُ في YYYY-MM-DD» في ARCHITECTURE.md — "
            "فالجردُ المُعلَنُ إمّا حُذِفَ وإمّا غُيِّرَ عنوانُه، وكِلاهما يُعلَنُ لا يُخمَّن."
        )
    measured_on = date.fromisoformat(section.group(1))

    schemas: dict[str, int] = {}
    rows: dict[str, int] = {}
    total = 0
    for line in text.splitlines():
        pair = SCHEMA_ROW_RE.match(line)
        if pair is not None:
            schemas[pair.group(1)] = int(pair.group(2).replace(",", ""))
            continue
        summed = TOTAL_ROW_RE.match(line)
        if summed is not None:
            total = int(summed.group(1).replace(",", ""))
            for name, count in BREAKDOWN_PAIR_RE.findall(summed.group(2)):
                schemas.setdefault(name, int(count.replace(",", "")))
            continue
        counted = ROWS_ROW_RE.match(line)
        if counted is not None:
            rows[counted.group(1)] = int(counted.group(2).replace(",", ""))

    if not schemas:
        raise MeasurementRefused(
            "قسمُ الجردِ موجودٌ ولا صفَّ مخطَّطٍ فيه يُقرأُ — لا يُحكَمُ على فراغٍ."
        )

    version = VERSION_RE.search(text)
    return Declared(
        measured_on=measured_on,
        version=version.group(1) if version else "",
        schemas=schemas,
        breakdown_total=total,
        rows=rows,
        source=str(ARCHITECTURE),
    )


def check_contract(declared: Declared, today: date, max_age_days: int) -> Contract:
    """يقيسُ استقامةَ المُعلَنِ في نفسِه: مجموعٌ · تاريخٌ · تفصيلٌ."""
    contract = Contract()

    if declared.breakdown_total and declared.breakdown_total != declared.breakdown_sum:
        contract.violations.append(
            f"INVENTORY_SUM_MISMATCH: المجموعُ المُعلَنُ {declared.breakdown_total} "
            f"وتفصيلُه يجمعُ {declared.breakdown_sum} "
            f"({' · '.join(f'{k}={v}' for k, v in declared.schemas.items())}) — "
            "رقمٌ يُخالِفُ تفصيلَه في السطرِ نفسِه."
        )

    if declared.measured_on > today:
        contract.violations.append(
            f"INVENTORY_DATE_IN_FUTURE: تاريخُ القياسِ {declared.measured_on} "
            f"واليومُ {today} — قياسٌ لم يحدُثْ بعدُ يُعلَنُ حاصلًا."
        )

    if not declared.rows:
        contract.violations.append(
            "INVENTORY_NO_ROW_METRIC: لا صفَّ «صفوفُ `جدول`» في الجردِ — "
            "فالمقيسُ عددُ جداولٍ بلا شاهدٍ على محتواها."
        )

    if not declared.version:
        contract.notes.append(
            "لا إصدارَ محرِّكٍ مُعلَنًا بصيغةِ «PostgreSQL **X.Y**» — فلا يُقاسُ الإصدار."
        )

    age = (today - declared.measured_on).days
    contract.notes.append(f"عمرُ الجردِ المُعلَنِ {age} يومًا (قِيسَ {declared.measured_on}).")
    if age > max_age_days:
        contract.notes.append(
            f"INVENTORY_STALE: تجاوزَ العمرُ الحدَّ المُعلَنَ ({max_age_days} يومًا) — "
            "وإعادةُ القياسِ تلزمُها قاعدةٌ حيّةٌ، فيُعلَنُ ولا يُسقَطُ إلّا بـ"
            "`--enforce-staleness`."
        )
    return contract


def _live_schemas(payload: object) -> dict[str, int]:
    if not isinstance(payload, dict):
        raise MeasurementRefused("الحِملُ ليس كائنًا — لا يُقرأُ منه جردٌ.")
    raw = payload.get("schemas")
    if not isinstance(raw, list) or not raw:
        raise MeasurementRefused(
            "لا مفتاحَ `schemas` غيرَ فارغٍ في الحِملِ — قياسٌ لم يُقَسْ لا يُحكَمُ به."
        )
    live: dict[str, int] = {}
    for item in raw:
        if (
            not isinstance(item, dict)
            or "table_schema" not in item
            or "tables" not in item
        ):
            raise MeasurementRefused(
                "صفٌّ في `schemas` بلا `table_schema`/`tables` — حِملٌ ناقصٌ يُرفَضُ لا يُكمَّل."
            )
        live[str(item["table_schema"])] = int(item["tables"])
    return live


def compare(declared: Declared, payload: object) -> list[Verdict]:
    """يقابلُ المُعلَنَ بالمقيسِ مقياسًا مقياسًا، ويُسمّي كلَّ فارق."""
    live = _live_schemas(payload)
    assert isinstance(payload, dict)  # مضمونٌ من `_live_schemas`
    verdicts: list[Verdict] = []

    for name, count in declared.schemas.items():
        if name not in live:
            verdicts.append(Verdict(f"schema:{name}", count, None, "MISSING_LIVE"))
        else:
            verdicts.append(
                Verdict(
                    f"schema:{name}",
                    count,
                    live[name],
                    "MATCH" if live[name] == count else "DRIFT",
                )
            )
    for name, count in live.items():
        if name not in declared.schemas:
            verdicts.append(Verdict(f"schema:{name}", None, count, "UNDECLARED"))

    if declared.breakdown_total:
        total_live = sum(live.values())
        verdicts.append(
            Verdict(
                "schemas:total",
                declared.breakdown_total,
                total_live,
                "MATCH" if total_live == declared.breakdown_total else "DRIFT",
            )
        )

    live_rows = payload.get("rows")
    for name, count in declared.rows.items():
        if not isinstance(live_rows, dict) or name not in live_rows:
            verdicts.append(Verdict(f"rows:{name}", count, None, "MISSING_LIVE"))
            continue
        measured = int(live_rows[name])
        verdicts.append(
            Verdict(
                f"rows:{name}",
                count,
                measured,
                "MATCH" if measured == count else "DRIFT",
            )
        )

    live_version = payload.get("server_version")
    if declared.version and isinstance(live_version, str) and live_version:
        verdicts.append(
            Verdict(
                "server_version",
                declared.version,
                live_version,
                "MATCH" if live_version.startswith(declared.version) else "DRIFT",
            )
        )
    return verdicts


def measure_live(dsn: str) -> dict[str, object]:
    """يقيسُ الجردَ من قاعدةٍ حيّةٍ — أو يرفضُ مُعلِنًا ما نقصَه."""
    if not dsn:
        raise MeasurementRefused(
            "لا وصلَ قاعدةٍ في البيئةِ: يُقرأُ من "
            + " أو ".join(DSN_ENV)
            + " — ولا يُقاسُ جردٌ بلا قاعدة. وللمطابقةِ بلا سرٍّ يُستعمَلُ `--from-json`."
        )
    try:
        from sqlalchemy import create_engine, text
    except ImportError as exc:  # مُعلَنٌ لا مبتلَع
        raise MeasurementRefused(
            f"لا مُحرِّكَ `sqlalchemy` في البيئةِ ({exc}) — يُركَّبُ أو يُقاسُ خارجًا ويُمرَّرُ بـ`--from-json`."
        ) from exc

    engine = create_engine(dsn)
    with engine.connect() as conn:
        schemas = [
            {"table_schema": row[0], "tables": int(row[1])}
            for row in conn.execute(text(SCHEMA_QUERY))
        ]
        rows: dict[str, int] = {}
        for table in read_declared().rows:
            if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", table):
                continue
            rows[table] = int(
                conn.execute(text(f"select count(*) from public.{table}")).scalar_one()
            )
        version = str(conn.execute(text("show server_version")).scalar_one())
    return {
        "measured_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "measured_by": "schema_inventory_drift.py --measure",
        "server_version": version,
        "schemas": schemas,
        "rows": rows,
    }


def render(declared: Declared, contract: Contract, verdicts: list[Verdict]) -> str:
    """خرجٌ يُقرأُ: ما قِيسَ · ما افترقَ · وما لم يُقَسْ."""
    lines = ["[SCHEMA INVENTORY] الجردُ المُعلَنُ يُقاسُ لا يُقرأُ"]
    lines.append(
        f"  المُعلَنُ في {declared.source}: قِيسَ {declared.measured_on} · "
        f"{len(declared.schemas)} مخطَّطًا · مجموعٌ {declared.breakdown_total or declared.breakdown_sum} · "
        f"{len(declared.rows)} عدَّادَ صفوف"
    )
    for violation in contract.violations:
        lines.append(f"  ✗ {violation}")
    for note in contract.notes:
        lines.append(f"  · {note}")
    if verdicts:
        drifted = [v for v in verdicts if v.is_drift]
        lines.append(
            f"  المطابقةُ بالمقيسِ: {len(verdicts) - len(drifted)} مطابقًا · {len(drifted)} مفترقًا"
        )
        for verdict in drifted:
            lines.append(
                f"  ✗ {verdict.state}: {verdict.metric} — مُعلَنٌ {verdict.declared} · مقيسٌ {verdict.live}"
            )
    else:
        lines.append("  المطابقةُ بالمقيسِ: لم تُجرَ — لا مصدرَ قياسٍ في هذا التشغيل.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="جردُ المخطَّطِ المُعلَنُ في ARCHITECTURE.md: استقامتُه تُقاسُ بلا سرٍّ، ومطابقتُه بقاعدةٍ أو بحِملٍ محفوظ."
    )
    parser.add_argument("--check", action="store_true", help="قياسُ استقامةِ المُعلَنِ وحدَه")
    parser.add_argument(
        "--from-json", default="", help="حِملُ جردٍ حيٍّ محفوظٌ — مطابقةٌ بلا سرّ"
    )
    parser.add_argument(
        "--measure", action="store_true", help="قياسٌ حيٌّ من قاعدةٍ (يلزمُه وصلٌ في البيئة)"
    )
    parser.add_argument("--json", default="", help="مسارُ كتابةِ حِملِ القياسِ المنشور")
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=30,
        help="حدُّ عمرِ الجردِ المُعلَنِ قبلَ إعلانِ تقادُمِه",
    )
    parser.add_argument(
        "--enforce-staleness", action="store_true", help="جعلُ التقادُمِ مخالفةً تُسقِطُ"
    )
    args = parser.parse_args(argv)

    if not (args.check or args.from_json or args.measure):
        parser.error("لا وضعَ: يلزمُ `--check` أو `--from-json` أو `--measure`.")

    today = datetime.now(UTC).date()
    try:
        declared = read_declared()
        payload: dict[str, object] | None = None
        if args.measure:
            dsn = next((os.environ[k] for k in DSN_ENV if os.environ.get(k)), "")
            payload = measure_live(dsn)
        elif args.from_json:
            path = Path(args.from_json)
            if not path.is_file():
                raise MeasurementRefused(f"لا حِملَ في {path} — لا يُقاسُ بما لا يُقرأ.")
            payload = json.loads(path.read_text(encoding="utf-8"))
        contract = check_contract(declared, today, args.max_age_days)
        verdicts = compare(declared, payload) if payload is not None else []
    except MeasurementRefused as exc:
        print(f"[SCHEMA INVENTORY] ✗ القياسُ مرفوضٌ: {exc}", file=sys.stderr)
        return 2

    print(render(declared, contract, verdicts))

    if args.json and payload is not None:
        out = Path(args.json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {
                    "$comment": PUBLISHED_COMMENT,
                    "schema_version": 1,
                    "measurement": "schema_inventory_drift",
                    **payload,
                    "declared": {
                        "source": declared.source,
                        "measured_on": declared.measured_on.isoformat(),
                        "server_version": declared.version,
                        "schemas": declared.schemas,
                        "schemas_total": declared.breakdown_total,
                        "rows": declared.rows,
                    },
                    "verdicts": [
                        {
                            "metric": v.metric,
                            "declared": v.declared,
                            "live": v.live,
                            "state": v.state,
                        }
                        for v in verdicts
                    ],
                    "drift_count": sum(1 for v in verdicts if v.is_drift),
                    "contract_violations": contract.violations,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"[SCHEMA INVENTORY] كُتبت: {out}")

    stale = [n for n in contract.notes if n.startswith("INVENTORY_STALE")]
    failing = list(contract.violations) + (stale if args.enforce_staleness else [])
    if failing or any(v.is_drift for v in verdicts):
        print(
            "[SCHEMA INVENTORY] ✗ الجردُ المُعلَنُ لا يستقيمُ أو لا يُطابِقُ المقيسَ — "
            "يُصحَّحُ في ARCHITECTURE.md بقيدٍ في سجلِّ الإكمال.",
            file=sys.stderr,
        )
        return 1
    print(
        "[SCHEMA INVENTORY] ✓ المُعلَنُ مستقيمٌ"
        + (" ومطابقٌ للمقيس." if verdicts else " (بلا مطابقةٍ حيّة).")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
