#!/bin/bash
# طفراتُ مرحلةِ المراقبةِ لـWI-085 (W-752): كلُّ طفرةٍ تُعكَسُ بعدَ قياسِها
set -u
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$ROOT"
GW=core/sovereignty/gateway.py
KS=core/sovereignty/kill_switch_source.py
FS=federal/executive/services/src/amos_federation/services/executive_core/kill_switch_level_source.py
BR=federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py
run() {
  local a b
  a=$(timeout 600 .venv/bin/python -m pytest -q -p no:cacheprovider tests/sovereignty/test_w752_kill_switch_observe.py 2>&1 | rg "passed|failed" | tail -1)
  b=$(cd federal/executive/services && timeout 600 ../../../.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_w752_kill_switch_observe.py 2>&1 | rg "^=+ .*(passed|failed)" | tail -1)
  echo "النواة: $a · الفدراليّ: $b"
}
mut() { local name="$1" file="$2" py="$3"; cp "$file" /tmp/w752_orig.py; python3 -c "$py" "$file"; echo -n "$name — "; run; cp /tmp/w752_orig.py "$file"; }
mut "M1 نزعُ الملاحظةِ من _execute_subordinate" $GW 'import sys;p=sys.argv[1];s=open(p).read();a="        self._observe_kill_switch(request, verdict, \"subordinate\")\n";assert a in s;open(p,"w").write(s.replace(a,""))'
mut "M2 المستوى الفعّالُ = مستوى الطلبِ وحدَه (لا حقن)" $KS 'import sys;p=sys.argv[1];s=open(p).read();a="effective = max(request.kill_switch_level, reading.level)";assert a in s;open(p,"w").write(s.replace(a,"effective = request.kill_switch_level"))'
mut "M3 غيابُ المصدرِ يُقرأُ 0 (فشلٌ مفتوح)" $KS 'import sys;p=sys.argv[1];s=open(p).read();a="        return LevelReading(FAIL_CLOSED_LEVEL, FORM_NO_SOURCE)";assert a in s;open(p,"w").write(s.replace(a,"        return LevelReading(0, FORM_NO_SOURCE)"))'
mut "M4 المراقبةُ تمنعُ (ترفعُ عندَ الملاحظة)" $GW 'import sys;p=sys.argv[1];s=open(p).read();a="            self._kill_switch_observations.append(observation)\n";assert a in s;open(p,"w").write(s.replace(a,a+"            raise SovereigntyViolation(verdict)\n").replace("        except Exception:  # noqa: BLE001 — «بلا منع»","        except SovereigntyViolation:\n            raise\n        except Exception:  # noqa: BLE001 — «بلا منع»"))'
mut "M5 عطلُ المُصرِّفِ يُبتلَعُ بلا عدّ" $GW 'import sys;p=sys.argv[1];s=open(p).read();a="            self._kill_switch_observation_errors += 1\n";assert a in s;open(p,"w").write(s.replace(a,"            pass\n"))'
mut "M6 المصدرُ الفدراليُّ يقرأُ بـget() (يُنشئُ normal)" $FS 'import sys;p=sys.argv[1];s=open(p).read();a="            if row is None:\n                return LevelReading(_FAIL_CLOSED, \"absent\")\n";assert a in s;open(p,"w").write(s.replace(a,"            if row is None:\n                from amos_federation.common.persistent import PersistentSystemStateStore\n                return LevelReading(*level_from_stored(PersistentSystemStateStore().get()[\"level\"]))\n"))'
mut "M7 الجسرُ لا يُسجِّلُ المصدر" $BR 'import sys;p=sys.argv[1];s=open(p).read();a="        gateway.register_kill_switch_source(PersistentKillSwitchLevelSource(), log_observation)\n";assert a in s;open(p,"w").write(s.replace(a,""))'
mut "M8 halt يُترجَمُ 3 لا 4" $FS 'import sys;p=sys.argv[1];s=open(p).read();a="\"halt\": 4}";assert a in s;open(p,"w").write(s.replace(a,"\"halt\": 3}"))'
echo -n "بلا طفرة — "; run
git diff --stat -- $GW $KS $FS $BR | tail -1
