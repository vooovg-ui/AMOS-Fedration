#!/usr/bin/env bash
# الهدف: إعادةُ قياسِ مواضعِ § 1 من EXECUTION_RECOVERY_DESIGN.md على العقدةِ الحاليّة (W-719 · WI-116)
# النطاق: قراءةٌ فقط (grep/sed) — لا تعديل
# المالك: Perplexity Computer · W-719
set -u
O=core/sovereignty/outbox.py
D=federal/executive/services/src/amos_federation/services/executive_core
run() { printf '\n$ %s\n' "$*"; "$@"; printf '[exit=%s]\n' "$?"; }
run git rev-parse HEAD
run grep -n "DEFAULT_LEASE_SECONDS: Final\|DEFAULT_MAX_DELIVERY_ATTEMPTS: Final" "$O"
run sed -n 455,475p "$O"
run grep -n "    def claim(\|    def begin_attempt(\|    def record_result(\|    def reclaim_expired(\|    def next_claimable(\|    def ambiguous(\|    def _call_provider(\|    def run_once(" "$O"
run sed -n 815,818p "$O"
run sed -n 875,877p "$O"
run sed -n 920,934p "$O"
run sed -n 1222,1226p "$O"
run sed -n 1260,1266p "$O"
run sed -n 337,353p "$D/engine.py"
run grep -n "    def _guarded_transition(\|    def _execute_step(\|self._runtime.dispatch(\|            TaskState.COMPLETED,\|    def run(\|    def recover(\|interrupted_execution" "$D/engine.py"
run sed -n 249,253p "$D/engine.py"
run grep -n "@router.post(\"/tasks/{task_id}/advance\")\|@router.post(\"/tasks/{task_id}/run\")\|@router.post(\"/recover\")" "$D/main.py"
run grep -rn "\.recover()" --include=*.py federal/executive/services/src
run grep -n "TaskState.EXECUTING: frozenset" "$D/states.py"
run grep -n "مفتاحُ أحاديّتِه\|EXECUTION:executive.task\|يُعَدُّ في الصادرِ كلُّ سجلٍّ" docs/audit/Q16_EXECUTION_EFFECT_DESIGN.md
