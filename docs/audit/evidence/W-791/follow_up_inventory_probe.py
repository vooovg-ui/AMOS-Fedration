"""مِسبارُ قراءةِ الجردِ لصيغةِ `follow_up` قبلَ أوّلِ سطرِ شِفرةٍ في WI-127 (W-791).

الهدف: قياسُ — لا افتراضُ — كيف يعدُّ `tools/audit/sovereign_write_inventory.py` كما
هو اليومَ (بلا تعديل) سطحًا مركَّبًا يُسلِّمُ كتابتَه إلى عبورِ `disburse` بمُعامَلِ
`follow_up`، بأربعِ صيغٍ مرشَّحة، على وحداتٍ اصطناعيّةٍ صغيرةٍ تُكتَبُ في مجلَّدٍ مؤقَّت.
يُستدعى `collect` و`summarize` من الأداةِ نفسِها. يُشغَّلُ من جذرِ المستودع:
    .venv/bin/python docs/audit/evidence/W-791/follow_up_inventory_probe.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from tools.audit.sovereign_write_inventory import collect, summarize  # noqa: E402

#: الخزانةُ الاصطناعيّة: `disburse` يعبرُ (`guard_declared(` في جسدِه) ويُطبِّقُ الآثارَ
#: المُعلَنةَ داخلَ عبورِه — كما يقترحُ § 2.10.
TREASURY = """
class Treasury:
    def disburse(self, amount, follow_up=()):
        def _apply(session):
            session.add(("ledger", amount))
            for effect in follow_up:
                effect.apply(session)
        return guard_declared("treasury.disburse", _apply)
"""

#: الصيغُ الأربع للسطحِ المركَّب (`execute_expenditure` نموذجًا).
SHAPES: dict[str, str] = {
    "S0 اليوم: disburse ثمَّ كتابةٌ مباشرة": """
class Economy:
    def execute_expenditure(self, amount):
        self.treasury.disburse(amount)
        self._session.add(("op", amount))
        self._session.commit()
""",
    "S1 مُطبِّقٌ مُتداخِلٌ في جسدِ السطح": """
class Economy:
    def execute_expenditure(self, amount):
        def _record(session):
            session.add(("op", amount))
        def _undo(session):
            session.delete(("op", amount))
        return self.treasury.disburse(
            amount, follow_up=(FollowUp(apply=_record, compensate=_undo),)
        )
""",
    "S2 مُطبِّقٌ منهجٌ خاصٌّ يُمرَّرُ مرجعًا": """
class Economy:
    def execute_expenditure(self, amount):
        return self.treasury.disburse(
            amount,
            follow_up=(FollowUp(apply=self._record_op, compensate=self._undo_op),),
        )
    def _record_op(self, session):
        session.add(("op", 1))
    def _undo_op(self, session):
        session.delete(("op", 1))
""",
    "S3 مُطبِّقٌ منهجٌ خاصٌّ يُنادى في lambda": """
class Economy:
    def execute_expenditure(self, amount):
        return self.treasury.disburse(
            amount,
            follow_up=(
                FollowUp(
                    apply=lambda s: self._record_op(s),
                    compensate=lambda s: self._undo_op(s),
                ),
            ),
        )
    def _record_op(self, session):
        session.add(("op", 1))
    def _undo_op(self, session):
        session.delete(("op", 1))
""",
}


def main() -> int:
    for label, body in SHAPES.items():
        with tempfile.TemporaryDirectory() as tmp:
            pkg = Path(tmp) / "pkg"
            pkg.mkdir()
            (pkg / "treasury.py").write_text(TREASURY, encoding="utf-8")
            (pkg / "economy.py").write_text(body, encoding="utf-8")
            sites = collect(Path(tmp))
            summary = summarize(sites)
        print(f"## {label}")
        for s in sorted(sites, key=lambda x: (x.path, x.function)):
            print(
                f"  site {s.path}:{s.owner}.{s.function} public={s.public} "
                f"guarded={s.guarded} writes={list(s.writes)} via={list(s.writes_via)}"
            )
        print(
            "  summary: total={write_sites_total} public={public_write_operations} "
            "crossing={sovereign_write_operations} "
            "not_crossing={non_sovereign_write_operations}".format(**summary)
        )
        orphans = [s.function for s in sites if not s.public and s.writes]
        print(f"  private_writers_unattributed={orphans}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
