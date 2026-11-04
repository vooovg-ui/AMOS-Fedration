# evidence/W-814 — توجيهُ المستشارِ 41: قراراتُ Q-96 · إغلاقُ الطلباتِ الخمسة · أحكامُ CI لـW-812 وW-813

## التعريف
أدلّةُ قيدِ W-814 (توثيقٌ وأوامرُ مستودعٍ مأذونة · لا شِّفرة — والشِّفرةُ في W-815 من الدفعةِ نفسِها): نصُّ التوجيهِ 41 حرفيًّا، وأوامرُ إغلاقِ الطلباتِ الخمسةِ وحذفِ الفرعِ ومخرجُها الخام، وأحكامُ CI الستّةُ لدفعتَي W-812 وW-813 مقيَّدةً في قيدٍ واحدٍ بحكمِ Q-95 القرار 2، وقياسُ D-4 قبلَ الشِّفرة.

## النطاق
- `OWNER_DIRECTIVE_41.md`: النصُّ الكاملُ حرفيًّا — سندُ Q-96.
- `gh_closures.txt`: `gh pr close <n> --comment …` للخمسة (#73 #71 #70 #69 #55 · كلُّها CLOSED بعدُ والفروعُ الخمسةُ باقيةٌ مقيسة) · `git push origin --delete api-test-branch` (HTTP 500) ثمَّ `gh api -X DELETE …/git/refs/heads/api-test-branch` (HTTP 422 «Cannot delete this branch») · وقراءةُ القاعدة: ruleset 23226080 «Main Security Rules» (`deletion` · `non_fast_forward`) ⇒ DISC-158. و#73 أُعيدَ أمرُه مرّةً بعدَ خطأِ GraphQL عابرٍ فأُغلِق.
- `ci/run_<id>_jobs.json` (ستّةٌ بتعليقِ `$comment`) و`ci/verdicts_readability.txt`: `ci_verdict_readability.py --from-json … --require-readable --expect-sha <sha>` لكلٍّ ⇒ EXIT=0 ستَّ مرّات:
  - W-812 على `ede2e8db`: ‏41759791838 (PR #262 · 13/13) · 41759768479 (push · 1/1) · 41763182430 (main · 13/13) · 41763182423 (main · 1/1).
  - W-813 على `d1ac08bd`: ‏41789383465 (PR #263 · 13/13) · 41789376894 (push · 1/1).
- `d4_before_stdout.txt`: الجردُ عندَ `d1ac08bd` قبلَ الشِّفرة — D-4 = 77 · العامّ 180 · العابر 94 · الحدودُ 7.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · قيدُ W-814 · WI-128)

## تاريخ الإنشاء
2026-11-04

## تاريخ آخر تعديل
2026-11-04

## المحتويات
- القراراتُ الثمانيةُ بحرفِها في `SOVEREIGN_DECISION_REGISTER.md` § Q-96، وRK-024 غيرُ مُقرَّر.
- التصميمانِ قبلَ الشِّفرة: `M1_MONEY_CROSSING_DESIGN.md` § 2.12 (DISC-155) · `DISC153_PREPUSH_ONLY_DEPS_DESIGN.md` (DISC-153).

## قانون الوكالة
لا VERIFIED ولا IN_REVIEW (RK-024 للمالكِ وحدَه). ولا يُعدِّلُ الوكيلُ قواعدَ المستودع: حذفُ `api-test-branch` باقٍ للمالك (DISC-158).
