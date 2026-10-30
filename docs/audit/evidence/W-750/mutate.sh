#!/bin/bash
# طفراتُ دفعةِ المعجم: كلُّ طفرةٍ تُعكَسُ بعدَ قياسِها
set -u
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)/federal/executive/services"
EX=src/amos_federation/services/governance/expansion.py
LC=src/amos_federation/services/governance/learning_cycle.py
run() { timeout 600 ../../../.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_w750_lexicon_batch.py tests/test_w724_g1_expansion.py tests/test_w728_g1_learning_security.py 2>&1 | rg "passed|failed" | tail -1; }
mut() { local name="$1" file="$2" py="$3"; cp "$file" /tmp/w750_orig.py; python3 -c "$py" "$file"; echo -n "$name: "; run; cp /tmp/w750_orig.py "$file"; }
mut "M1 graduate_batch يعودُ إلى release_agent" $EX 'import sys;p=sys.argv[1];s=open(p).read();open(p,"w").write(s.replace("ACTION_GRADUATE_BATCH = \"activate_agent\"","ACTION_GRADUATE_BATCH = \"release_agent\""))'
mut "M2 complete_training يعودُ إلى release_agent" $LC 'import sys;p=sys.argv[1];s=open(p).read();open(p,"w").write(s.replace("ACTION_COMPLETE_TRAINING = \"activate_agent\"","ACTION_COMPLETE_TRAINING = \"release_agent\""))'
mut "M3 enroll_batch بلا تحقّقٍ مسبق" $EX 'import sys;p=sys.argv[1];s=open(p).read();a="        self.authorizer.request_permit(\n            ACTION_ENROLL_BATCH, target, declared_effects=(permit_effect,)\n        )\n";assert a in s;open(p,"w").write(s.replace(a,""))'
mut "M4 create_batch على فعلٍ أخفّ (log_isolated_action)" $EX 'import sys;p=sys.argv[1];s=open(p).read();open(p,"w").write(s.replace("ACTION_CREATE_BATCH = \"create_task\"","ACTION_CREATE_BATCH = \"log_isolated_action\""))'
mut "M5 evaluate_model بلا معوِّضٍ فعّال" $LC 'import sys;p=sys.argv[1];s=open(p).read();a="EvaluationResultModel.eval_id == eval_id\n                ).delete(synchronize_session=False)";assert a in s;open(p,"w").write(s.replace(a,"EvaluationResultModel.eval_id == eval_id\n                ).count()"))'
mut "M6 enroll_batch بلا معوِّضٍ للعدّاد" $EX 'import sys;p=sys.argv[1];s=open(p).read();a="            _set_batch_column(self._Session, batch_id, \"enrolled\", previous)\n";assert a in s;open(p,"w").write(s.replace(a,"            pass\n"))'
echo -n "بلا طفرة: "; run
git diff --stat -- $EX $LC | tail -1
