#!/usr/bin/env bash
# قياسُ «كم اختبارًا يمرُّ برمزٍ غيرِ ملكٍ» (التوجيهُ 23 § 2): يُبدَّلُ الحارسُ مؤقّتًا إلى require_king
# على المساراتِ ثمَّ تُشغَّلُ ملفّاتُ الفحصِ الثلاثةُ ثمَّ يُعادُ الملفّانِ (git checkout). لا يُلتزَمُ شيءٌ منه.
set -u
S=federal/executive/services; G=$S/src/amos_federation/services/governance/main.py; C=$S/src/amos_federation/services/control_console/main.py
run(){ (cd $S && python -m pytest -q -p no:cacheprovider tests/test_governance.py tests/test_governance_phase3.py tests/test_control_console.py 2>/dev/null | rg "^FAILED|passed|failed" | sed 's/ - .*//'); }
echo "== (0) خطُّ الأساسِ (العقدةُ كما هي)"; run
sed -i '14s/import require_auth$/import require_auth, require_king/' $G; sed -i '15s/import require_auth$/import require_auth, require_king/' $C
for n in 149 170 203; do sed -i "${n}s/Depends(require_auth)/Depends(require_king)/" $G; done; sed -i '211s/Depends(require_auth)/Depends(require_king)/' $C
echo "== (1) نطاقُ D25-2 حرفيًّا: reset ×2 · إنشاءُ الترقية · فحصُ البوابة"; git diff -U0 $G $C | rg '^[-+] '; run
sed -i '139s/Depends(require_auth)/Depends(require_king)/' $G; sed -i '198s/Depends(require_auth)/Depends(require_king)/' $C
echo "== (2) ومعَها activate ×2 (للقياسِ فقط — خارجَ نصِّ D25-2 · DISC-138)"; run
git checkout -- $G $C; echo "== أُعيدَ: $(git status --short $G $C | wc -l) ملفٌّ معدَّلٌ"
