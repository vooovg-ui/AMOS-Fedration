#!/usr/bin/env bash
# طفراتُ WI-114 (W-675) — كلُّ طفرةٍ تُطبَّقُ على نسخةٍ ثمَّ يُستعادُ الأصلُ؛ الفحصُ يجبُ أن يسقط.
# التشغيل: من جذرِ المستودعِ بعدَ `source .venv/bin/activate`.
set -u
cd federal/executive/services
F=src/amos_federation/services/governance/canary.py
T=tests/test_wi114_canary_sovereign.py
cp "$F" /tmp/canary_orig.py
run() {
  echo "## $1"
  python - "$F" "$2" "$3" <<'PY'
import sys
p, old, new = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(p, encoding="utf-8").read()
assert s.count(old) == 1, ("anchor", old)
open(p, "w", encoding="utf-8").write(s.replace(old, new))
PY
  python -m pytest "$T" -q -p no:cacheprovider 2>&1 | grep -E "^(FAILED|[0-9]+ (passed|failed))|passed|failed" | grep -v Transient | tail -8
  cp /tmp/canary_orig.py "$F"
}
run "M1 · الخفضُ عبرَ التفعيلِ لا يُوجَّهُ إلى lower_kill_switch" \
  '        return ACTION_LOWER_KILL_SWITCH' '        return ACTION_ACTIVATE_KILL_SWITCH'
run "M2 · رفعُ الزرِّ يتجاوزُ الحدَّ (كتابةٌ مباشرة)" \
  '    violation = _core_sovereignty("gateway").SovereigntyViolation' \
  '    return store.set_level(level, reason, activated_by)
    violation = _core_sovereignty("gateway").SovereigntyViolation'
run "M3 · طلبُ الترقيةِ يتجاوزُ الحدَّ (كتابةٌ مباشرة)" \
  '    def _cancel() -> None:' \
  '    _promotion_store().create(promotion)
    return promotion

    def _cancel() -> None:'
run "M4 · مُعوِّضُ الزرِّ لا يستعيدُ شيئًا" \
  '        if before["level"] == "normal":
            store.reset()' \
  '        if True:
            return'
run "M5 · مُعوِّضُ الترقيةِ لا يُبطِل" \
  '            promotion_id, promotion["gates"], "cancelled", datetime.now(UTC).isoformat()' \
  '            promotion_id, promotion["gates"], "in_progress", datetime.now(UTC).isoformat()'
run "M6 · بلا مُعرِّفٍ في الهدف (تصادمُ رفعَينِ في ثانية)" \
  '    target = f"{SYSTEM_STATE_TARGET}/{nonce}"' \
  '    target = SYSTEM_STATE_TARGET'
cmp -s "$F" /tmp/canary_orig.py && echo "## الأصلُ مُستعادٌ (cmp: مطابق)"
