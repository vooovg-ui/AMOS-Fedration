#!/usr/bin/env bash
# W-721 · قياسُ D-1…D-7 حيًّا — كلُّ أمرٍ يُطبَعُ قبلَ مخرجِه ومعه [exit=]
# التشغيل من جذر المستودع: bash docs/audit/evidence/W-721/measure.sh > docs/audit/evidence/W-721/measure.txt 2>&1
cd "$(git rev-parse --show-toplevel)" || exit 1
PY=.venv/bin/python
run() { echo "\$ $*"; "$@"; echo "[exit=$?]"; echo; }
echo "HEAD=$(git rev-parse HEAD)"; echo
echo "## D-1 · مخالفاتُ مصفوفةِ الحقيقة (والأقاليمُ لـ D-2 في السطرِ الأوّل)"
run $PY tools/governance/truth_audit.py . --ratchet
run git diff --stat -- docs/audit/TRUTH_MATRIX.md docs/audit/truth_matrix.json
run git checkout -- docs/audit/TRUTH_MATRIX.md docs/audit/truth_matrix.json
echo "## D-2 · أقاليمُ PROVEN"
run grep -c "PROVEN" docs/audit/TRUTH_MATRIX.md
run grep -n "مُثبَت\|PROVEN" docs/audit/TRUTH_MATRIX.md
echo "## D-3 · مراحلُ Phase E"
run grep -n "^\*\*التقدم:\*\*" docs/audit/PHASE_E_ROADMAP.md
echo "## D-4 · الكتاباتُ غيرُ السياديّة"
run $PY tools/audit/sovereign_write_inventory.py --root .
run $PY tools/audit/decision_gate.py --measure
echo "## D-4 · أسطحُ G1 بعدَ استثناءاتِ التوجيه 27"
run $PY docs/audit/evidence/W-721/surface_recount.py
echo "## D-5 · أسئلةُ Q-1…Q-27"
run $PY docs/audit/evidence/W-721/d5_status.py
echo "## D-6 · CI على main + قابليّةُ إعادةِ القياس"
run gh run list --repo vooovg-ui/AMOS-Fedration --branch main --limit 4 --json databaseId,headSha,conclusion,name
run $PY tools/governance/measurement_provenance.py . --check --without-deps
echo "## D-7 · النشر"
run ls docs/governance/work/HANDOFFS/D7-DEPLOYMENT-REQUIREMENTS.md
echo "## معنى «المستوى N» (التوجيه 27 §1 ج)"
run env PYTHONPATH=. $PY docs/audit/evidence/W-721/killswitch_probe.py
