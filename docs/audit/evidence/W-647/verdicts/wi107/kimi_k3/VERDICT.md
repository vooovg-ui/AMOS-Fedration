# حكمُ مقعدِ المجلسِ — kimi_k3 (عائلةُ Moonshot AI Kimi) · جولةُ WI-107 (R1) (W-647)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في جولةِ المراجعةِ على WI-107 (R1) (الطابورُ الواحدُ · التوجيهُ 19 § 2 · بروتوكولُ Q-59) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في جذورِهِ الخاصّةِ (council_w628/kimi_k3) — منسوخٌ آليًّا، وما بعدَ الفاصلِ بايتًا ببايتٍ (sha256 `c7004583ae51c3efba5f577a83aa25ecb667b36acae8a3c571751a2139432b61`).

## النطاق
حكمُ مقعدٍ واحدٍ على WI-107 (R1) عندَ العقدةِ `3c6c91de` — إحاطةٌ مبصومةٌ ومسبارٌ خاصٌّ عندَ المقعدِ (§ 4.9).

## المالك
المنسِّقُ GLM-5.3 (قيدُ W-647) — منسِّقٌ لا مُصوِّتٌ · ولا VERIFIED بيدِ المنفِّذِ (§ 5).

## تاريخ الإنشاء
2026-10-24

---
MODEL: Kimi (kimi_k3)
FAMILY: Moonshot AI
RUN_DATE: 2026-10-24 06:50 +00:00
NODE: 3c6c91de6915846c547af26449e604233cdd2a11
CLONE_PATH: /home/user/workspace/council_w628/kimi_k3/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w628/kimi_k3/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-628/briefs/
 2. cd /home/user/workspace/council_w628/kimi_k3/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-628/briefs/)
 3. cd /home/user/workspace/council_w628/kimi_k3/repo && git rev-parse HEAD
 4. cd /home/user/workspace/council_w628/kimi_k3/repo && git diff --stat a458db66299602154f585590fe058aa343f86bed HEAD -- federal/ tools/ tests/ agents/ core/ src/
 5. cd /home/user/workspace/council_w628/kimi_k3/repo && bash tools/dev/bootstrap.sh --verify
 6. cd /home/user/workspace/council_w628/kimi_k3/repo && git log --format='%h %cI %s' e7609e1..HEAD --max-count=30
 7. cd /home/user/workspace/council_w628/kimi_k3/repo && git diff --stat e7609e1 HEAD
 8. cd /home/user/workspace/council_w628/kimi_k3/repo && git log --format='%h %cI %s' -3 -- docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md federal/executive/services/src/amos_federation/services/national_registry/service.py
 9. cd /home/user/workspace/council_w628/kimi_k3/repo && git diff e7609e1 HEAD -- federal/executive/services/tests/test_r7c_national_registry.py federal/executive/services/tests/test_2b_state_registry_sovereign.py federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py
 10. cd /home/user/workspace/council_w628/kimi_k3/repo && git diff e7609e1 HEAD -- federal/executive/services/src/amos_federation/services/national_registry/service.py
 11. cd /home/user/workspace/council_w628/kimi_k3/repo && cat federal/executive/services/tests/test_wi107_national_registry_register_sovereign.py
 12. cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 13. cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi107_national_registry_register_sovereign.py -q
 14. cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_r7c_national_registry.py -q
 15. cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_2b_state_registry_sovereign.py -q
 16. cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests -q
 17. cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md
 18. cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-622/inventory_before_wi107.json docs/audit/evidence/W-625/inventory_after_wi107.json
 19. cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-628/mutation_probe_wi107.py
 20. cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python docs/audit/evidence/W-628/mutation_probe_wi107.py
 21. cd /home/user/workspace/council_w628/kimi_k3/repo && rg -n "D17-3|Q-61|Q-71" docs/audit/SOVEREIGN_DECISION_REGISTER.md
 22. cd /home/user/workspace/council_w628/kimi_k3/repo && sha256sum docs/audit/evidence/W-628/briefs/briefing_kimi_k3.md
 23. cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-628/briefs/SHA256SUMS
 24. cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q
 25. cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
 26. nl -ba /home/user/workspace/council_w628/kimi_k3/probe/probe_wi107_kimi_k3.py
 27. cd /home/user/workspace/council_w628/kimi_k3/repo && cp /home/user/workspace/council_w628/kimi_k3/probe/probe_wi107_kimi_k3.py federal/executive/services/tests/test_probe_wi107_kimi_k3.py && cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w628/kimi_k3/tmp/probe_seat.db ../../..//.venv/bin/python -m pytest tests/test_probe_wi107_kimi_k3.py -q
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-628/briefs/
EXIT: 0
BYTES: 41
SHA256: e75f8868e18d51314d6a645db88f6c0f130b7e8153ea97c9fcf66d1482d6bc3a
NO_EOL: 0
--- OUTPUT ---
3c6c91de6915846c547af26449e604233cdd2a11
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-628/briefs/)
EXIT: 0
BYTES: 1370
SHA256: 7429acd463a0966bfa00ea35658e17071d9a9dd59aa332554512123dad216fdf
NO_EOL: 0
--- OUTPUT ---
Note: switching to '3c6c91de6915846c547af26449e604233cdd2a11'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 3c6c91de W-628 (الالتزامُ الثاني — توثيقُ توليدِ المصفوفةِ بأداتِها على فرعِ القيدِ · سابقةُ W-626): مصفوفةُ الحقيقةِ أُعيدَ توليدُها بعملِ سيرِ التوليدِ نفسِه (التزامُ 2dbe7ad · docs 345 ← 346 · المخالفاتُ ثابتةٌ 61) وقُيِّدَ ذلكَ في سجلِّ الإكمالِ · والعقدةُ المعلنةُ لجولةِ R1 صارتْ رأسَ الدفعةِ كاملًا (آخرُ التزامٍ يمسُّ evidence/W-628/briefs/ · يشملُ المصفوفةَ المولَّدةَ · وفرقُ الشِّفرةِ بينَه وبينَ a458db6 فارغٌ مقيسًا) — لا شِفرةَ · المنسِّقُ GLM-5.3
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: e75f8868e18d51314d6a645db88f6c0f130b7e8153ea97c9fcf66d1482d6bc3a
NO_EOL: 0
--- OUTPUT ---
3c6c91de6915846c547af26449e604233cdd2a11
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git diff --stat a458db66299602154f585590fe058aa343f86bed HEAD -- federal/ tools/ tests/ agents/ core/ src/
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && bash tools/dev/bootstrap.sh --verify
EXIT: 0
BYTES: 7003
SHA256: 77b1f6cb03d7f6cdff73de1537b8f5132a0244d209fce2314a3aafa0cf4d7027
NO_EOL: 0
--- OUTPUT ---
• الجذر: /home/user/workspace/council_w628/kimi_k3/repo
• ثُبِّتَ خُطّافُ pre-push (يُشغِّلُ حرسَ ما قبلَ الدفعِ على كلِّ دفعٍ — WI-078)
• إنشاءُ بيئةٍ معزولةٍ في .venv
• تركيبُ تبعيّاتِ الجذر (requirements-dev.txt)
• تركيبُ حزمةِ الخدماتِ (قد تطولُ: تبعيّاتٌ كثيرة)
• تركيبُ ruff==0.6.9 (‏المُثبَّتُ في .github/workflows/ci.yml)
✓ البيئةُ جاهزة. للتنشيطِ في جلسةٍ جديدة: source .venv/bin/activate
── حزمةُ الجذر ──
........................................................................ [  2%]
........................................................................ [  5%]
........................................................................ [  7%]
........................................................................ [ 10%]
........................................................................ [ 13%]
........................................................................ [ 15%]
........................................................................ [ 18%]
........................................................................ [ 21%]
........................................................................ [ 23%]
........................................................................ [ 26%]
........................................................................ [ 29%]
........................................................................ [ 31%]
........................................................................ [ 34%]
........................................................................ [ 37%]
........................................................................ [ 39%]
........................................................................ [ 42%]
........................................................................ [ 45%]
........................................................................ [ 47%]
........................................................................ [ 50%]
........................................................................ [ 53%]
........................................................................ [ 55%]
........................................................................ [ 58%]
........................................................................ [ 61%]
........................................................................ [ 63%]
........................................................................ [ 66%]
........................................................................ [ 69%]
........................................................................ [ 71%]
..................................................s..................... [ 74%]
........................................................................ [ 76%]
........................................................................ [ 79%]
........................................................................ [ 82%]
........................................................................ [ 84%]
........................................................................ [ 87%]
........................................................................ [ 90%]
........................................................................ [ 92%]
........................................................................ [ 95%]
........................................................................ [ 98%]
................................................                         [100%]
2711 passed, 1 skipped in 705.44s (0:11:45)
── بوّاباتُ الحوكمة ──
[TRUTH AUDIT] أقاليم: 12 | مُثبَتة: 0 | مخالفات: 61
  - IN_MEMORY_STORE: 59
  - HARDCODED_TRUTH: 2
[TRUTH AUDIT] كُتبت: /home/user/workspace/council_w628/kimi_k3/repo/docs/audit/TRUTH_MATRIX.md
فحص هوية المستودع (المادة التاسعة): .
==============================================================

نجح: كل مجلد يحمل بطاقة هوية كاملة، وكل ملف يُعلن هدفه.

================================================================
  AMOS-Federation P3 Smoke Tests — Summary
================================================================
Domain           Status   Detail
--------------------------------
tools            UNMEASURED   count=10, source=snapshot:2026-08-22T18:45:00+00:00
agents           UNMEASURED   count=5116, source=snapshot:2026-08-22T18:45:00+00:00
institutions     UNMEASURED   count=8, source=snapshot:2026-08-22T18:45:00+00:00
royal            UNMEASURED   guards=7, decrees=1, source=snapshot:2026-08-22T18:45:00+00:00
ops              UNMEASURED   count=71, source=snapshot:2026-08-22T18:45:00+00:00
federal          UNMEASURED   transactions=0, budgets=0, executive_roles=5, source=snapshot:2026-08-22T18:45:00+00:00
core             UNMEASURED   memories=3, experiences=11, source=snapshot:2026-08-22T18:45:00+00:00
runtime          UNMEASURED   tasks=28, events=1027, source=snapshot:2026-08-22T18:45:00+00:00
interfaces       UNMEASURED   count=0, source=snapshot:2026-08-22T18:45:00+00:00
states           UNMEASURED   legislations=0, compliance_reports=0, source=snapshot:2026-08-22T18:45:00+00:00
docs             PASS         nucleus_files=106, schemas=13, registries=12, source=filesystem
tests            PASS         nucleus_files=5, source=filesystem
--------------------------------
  2/12 أقاليمُ قِيسَت ونجحت | 10 غيرُ مقيسة | 0 فاشلة
  تنبيه: «غير مقيس» ليس نجاحًا — الأرقامُ أعلاه مُقتبَسةٌ من لَقطةٍ مُؤرَّخة،
  ولا تُقبَلُ دليلًا في بوّابةٍ تشترطُ إثباتًا. هيِّئ AMOS_TRUTH_DB_URL،
  أو شغِّلْ بـ --require-measured لتفشلَ البوّابةُ عندَ غيابِ القياس.
================================================================

لا إقليمَ فاشلًا — وبقيَ 10 إقليمًا غيرَ مقيس.
── نظافةُ الشجرةِ بعدَ التشغيل (O-1N-1) ──
✓ الشجرةُ نظيفةٌ بعدَ حزمةٍ كاملة.

الأوامرُ الواجبةُ قبلَ أيِّ دفع (دليلُ المشروع § 8 و§ 9):
  python -m pytest tests/ -q
  AMOS_DATABASE_URL="sqlite:////tmp/amos_test.db" \
    python -m pytest federal/executive/services/tests -q
  python tools/governance/truth_audit.py .
  python tools/governance/check_repository_identity.py .
  python tools/governance/check_completion_ledger.py --commit HEAD
  python tests/smoke/run_smoke_tests.py
  ruff check . && ruff format --check \
    federal/executive/services/src federal/executive/services/tests

وتذكّرْ: آخرُ أمرٍ يُغيِّرُ بايتًا من الكودِ يسبقُ آخرَ توليدٍ للمصفوفة.
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git log --format='%h %cI %s' e7609e1..HEAD --max-count=30
EXIT: 0
BYTES: 1968
SHA256: 82c46ad1ea3204e5d38f4ef3a86100da2e081064f39be6ee713397120000d375
NO_EOL: 0
--- OUTPUT ---
3c6c91de 2026-10-23T13:37:57Z W-628 (الالتزامُ الثاني — توثيقُ توليدِ المصفوفةِ بأداتِها على فرعِ القيدِ · سابقةُ W-626): مصفوفةُ الحقيقةِ أُعيدَ توليدُها بعملِ سيرِ التوليدِ نفسِه (التزامُ 2dbe7ad · docs 345 ← 346 · المخالفاتُ ثابتةٌ 61) وقُيِّدَ ذلكَ في سجلِّ الإكمالِ · والعقدةُ المعلنةُ لجولةِ R1 صارتْ رأسَ الدفعةِ كاملًا (آخرُ التزامٍ يمسُّ evidence/W-628/briefs/ · يشملُ المصفوفةَ المولَّدةَ · وفرقُ الشِّفرةِ بينَه وبينَ a458db6 فارغٌ مقيسًا) — لا شِفرةَ · المنسِّقُ GLM-5.3
2dbe7ad3 2026-10-23T13:35:23Z مصفوفةُ الحقيقةِ: خرجٌ مولَّدٌ بأداتِه بعدَ تغيُّرِ الشجرة
51e3e089 2026-10-23T13:34:56Z W-628: WI-107 (R1) IN_PROGRESS→IN_REVIEW (H3 · سابقةُ W-618) + واجبُ N+1 (حكمُ CI على العقدةِ المدموجةِ a458db6 مقروءٌ أخضرَ · التشغيلانِ 39936353180 و39960113632) + إحاطاتُ جولةِ R1 الثلاثةُ مبصَمةً في الطابورِ الواحدِ مع F1 (توجيهٌ 20 § 1 · evidence/W-628/briefs/) + مسبارُ طفراتٍ آليٌّ معادُ الحصادِ (M1–M5 مقتولةٌ سلوكيًّا · نمطُ W-617) — لا شِفرةَ · المنسِّقُ GLM-5.3
a458db66 2026-10-23T10:02:42Z W-627 · تصحيحٌ مؤرَّخٌ لحمرةِ CI الثانية على دفعةِ W-625 (سابقةُ W-626)
4b3b2104 2026-10-23T09:48:08Z W-626 · تصحيحٌ مؤرَّخٌ لحمرةِ CI على دفعةِ W-625 (سابقةُ W-594/W-600)
f65ae2d4 2026-10-23T08:46:07Z W-625 · R1 (WI-107): الأسطحُ التسعةُ تعبر الحدَّ السياديَّ بفاعلٍ تنفيذيٍّ مُعلَنٍ
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git diff --stat e7609e1 HEAD
EXIT: 0
BYTES: 2909
SHA256: 37fcca48e2ca1509fe2c355cf0f798f75ea8bdb28970351fecd2d3f4817c3ac2
NO_EOL: 0
--- OUTPUT ---
 PROJECT_STATE.md                                   |    4 +-
 docs/PROJECT_HANDBOOK.md                           |    7 +-
 docs/audit/ACTIVE_EXECUTION_STATE.md               |    2 +-
 docs/audit/COMPLETION_LEDGER.md                    |   11 +
 docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md |   14 +-
 docs/audit/SOVEREIGN_DECISION_REGISTER.md          |   19 +-
 docs/audit/TRUTH_MATRIX.md                         |    6 +-
 docs/audit/evidence/W-625/README.md                |   52 +
 .../evidence/W-625/inventory_after_wi107.json      | 3408 ++++++++++++++++++++
 docs/audit/evidence/W-625/mutation_M1.out.txt      |   31 +
 docs/audit/evidence/W-625/mutation_M2.out.txt      |   32 +
 docs/audit/evidence/W-625/mutation_M3.out.txt      |   31 +
 docs/audit/evidence/W-625/mutation_M4.out.txt      |   25 +
 docs/audit/evidence/W-625/mutation_M5.out.txt      |   25 +
 .../W-625/mutation_baseline_after_restore.out.txt  |   14 +
 .../evidence/W-625/owner_decision_Q71_verbatim.md  |   27 +
 .../evidence/W-625/repro_r7d_crown_pair.out.txt    |   22 +
 .../services_suite_after_conftest_fix.out.txt      |  116 +
 .../services_suite_before_conftest_fix.out.txt     | 1646 ++++++++++
 .../W-625/sovereign_write_inventory_after.txt      |   42 +
 docs/audit/evidence/W-626/README.md                |   24 +
 docs/audit/evidence/W-626/ci_jobs_first_run.txt    |   13 +
 docs/audit/evidence/W-627/README.md                |   28 +
 docs/audit/evidence/W-627/format_diff.patch        |  147 +
 docs/audit/evidence/W-627/lint_failure_log.txt     |    5 +
 docs/audit/evidence/W-627/lint_steps.txt           |   10 +
 docs/audit/evidence/W-628/README.md                |   39 +
 docs/audit/evidence/W-628/briefs/README.md         |   19 +
 docs/audit/evidence/W-628/briefs/SHA256SUMS        |    3 +
 .../W-628/briefs/briefing_gemini_3_8_flash.md      |  123 +
 .../evidence/W-628/briefs/briefing_grok_4_7.md     |  123 +
 .../evidence/W-628/briefs/briefing_kimi_k3.md      |  123 +
 .../evidence/W-628/ci_jobs_39960113632.api.txt     |    1 +
 .../W-628/ci_verdict_39960113632_green.txt         |    6 +
 .../evidence/W-628/mutation_probe_wi107.out.txt    |   12 +
 docs/audit/evidence/W-628/mutation_probe_wi107.py  |  106 +
 docs/audit/measurements/decision_gate_ledger.json  |   16 +
 docs/audit/measurements/decision_wave_map.json     |    6 +-
 docs/audit/measurements/final_audit_p14.json       |   22 +-
 docs/audit/measurements/write_inventory_p13.json   |  164 +-
 docs/audit/truth_matrix.json                       |   42 +-
 docs/governance/work/ACTIVE_WORK.md                |   16 +-
 .../services/national_registry/service.py          |  690 +++-
 federal/executive/services/tests/conftest.py       |   70 +-
 ...t_wi107_national_registry_register_sovereign.py |  700 ++++
 .../test_q3_branch_declaration_surface.py          |   43 +-
 46 files changed, 7860 insertions(+), 225 deletions(-)
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git log --format='%h %cI %s' -3 -- docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md federal/executive/services/src/amos_federation/services/national_registry/service.py
EXIT: 0
BYTES: 485
SHA256: 57560e3e91180ea02f8eb0a5b178451fa1700d109c6d7e3ffded8cddf94ad6be
NO_EOL: 0
--- OUTPUT ---
4b3b2104 2026-10-23T09:48:08Z W-626 · تصحيحٌ مؤرَّخٌ لحمرةِ CI على دفعةِ W-625 (سابقةُ W-594/W-600)
f65ae2d4 2026-10-23T08:46:07Z W-625 · R1 (WI-107): الأسطحُ التسعةُ تعبر الحدَّ السياديَّ بفاعلٍ تنفيذيٍّ مُعلَنٍ
0b0b84b2 2026-10-23T02:23:21Z W-623: WI-107 (الدفعةُ R1) READY → RESERVED (H3 · سابقةُ W-614 · حتى 2026-11-21) — لا شِفرةَ · المنسِّقُ GLM-5.3
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git diff e7609e1 HEAD -- federal/executive/services/tests/test_r7c_national_registry.py federal/executive/services/tests/test_2b_state_registry_sovereign.py federal/executive/services/tests/test_wi106_federation_coordinate_sovereign.py
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && git diff e7609e1 HEAD -- federal/executive/services/src/amos_federation/services/national_registry/service.py
EXIT: 0
BYTES: 45603
SHA256: 7ebdf0a0fa9b115f5ef577d706fd29d1e7298eec6b854442f24f307488aacd87
NO_EOL: 0
--- OUTPUT ---
diff --git a/federal/executive/services/src/amos_federation/services/national_registry/service.py b/federal/executive/services/src/amos_federation/services/national_registry/service.py
index f14e67cc..16ead7c6 100644
--- a/federal/executive/services/src/amos_federation/services/national_registry/service.py
+++ b/federal/executive/services/src/amos_federation/services/national_registry/service.py
@@ -29,14 +29,23 @@ AMOS-Federation National Registry — Service Layer
 
 from __future__ import annotations
 
+import copy
 import uuid
 from datetime import UTC, datetime
 from typing import TYPE_CHECKING, Any
 
+from sqlalchemy import inspect as sa_inspect
+
 from amos_federation.common.database import get_session_factory, init_db
 from amos_federation.common.money import to_money
 from amos_federation.common.principal import DEFAULT_TENANT
 from amos_federation.services.executive_core.agent_identity import get_identity
+from amos_federation.services.executive_core.sovereignty_bridge import (
+    ConstitutionalAuthorizer,
+    compensator,
+    declared_effect,
+    operation_key,
+)
 from amos_federation.services.national_registry.authorization import (
     PERMISSIONS_AGENT_LINK,
     PERMISSIONS_ASSIGNMENT_WRITE,
@@ -151,6 +160,116 @@ def _iso(value: datetime | None) -> str | None:
     return value.isoformat() if value else None
 
 
+# === عبورُ الحدِّ السياديِّ (R1 · ملحقُ التصميمِ D1–D8) =========================
+
+#: فاعلُ الوحدةِ (D1): السجلُّ الوطنيُّ كتابةٌ إداريّةٌ تنفيذيّةٌ — فاعلٌ مُعلَنٌ
+#: **ثابتٌ في الوحدةِ لا معاملًا للمُنادي**، على سابقةِ `federation.FEDERATION_ACTOR`
+#: (F1 · D1) و`rulings.JUDICIARY_ACTOR` (J1). والاختبارُ يُبدِّلُه بـ`monkeypatch`
+#: على هذا الثابتِ لا بمعاملٍ إنتاجيّ.
+REGISTRY_ACTOR = "EXECUTIVE"
+
+#: فعلُ الوحدةِ (D2): فعلٌ واحدٌ للأسطحِ التسعةِ كلِّها، واسمُ العمليّةِ يُحمَلُ في
+#: البياناتِ والنطاقِ لا في فعلٍ مُخترَعٍ (سؤالُ Q-2 المعلَّقُ). وحيادُ الفعلِ مقيسٌ
+#: (evidence/W-623): ليس في الاختصاصِ الملكيِّ الحصريِّ ولا في أفعالِ التآكلِ —
+#: واسمَا grant_authority/revoke_authority يبقيانِ محجوبَينِ للاسمِ في البوابةِ.
+REGISTRY_VERB = "register"
+
+_DEFAULT_REGISTRY_AUTHORIZER: ConstitutionalAuthorizer | None = None
+
+
+def _registry_authorizer() -> ConstitutionalAuthorizer:
+    """المُصرِّحُ الافتراضيُّ بفاعلِ الوحدةِ المُسمّى — واحدٌ للوحدةِ (D1)."""
+    global _DEFAULT_REGISTRY_AUTHORIZER
+    if _DEFAULT_REGISTRY_AUTHORIZER is None:
+        _DEFAULT_REGISTRY_AUTHORIZER = ConstitutionalAuthorizer(actor=REGISTRY_ACTOR)
+    return _DEFAULT_REGISTRY_AUTHORIZER
+
+
+def reset_registry_authorizer() -> None:
+    """أفرِغِ المُفوِّضَ المحفوظَ — للاختباراتِ التي تبدّلُ الفاعلَ (D1)."""
+    global _DEFAULT_REGISTRY_AUTHORIZER
+    _DEFAULT_REGISTRY_AUTHORIZER = None
+
+
+class RegistryReplayError(ValueError):
+    """مفتاحٌ طبيعيٌّ عبرَ بنجاحٍ من قبلُ — الإعادةُ ليست نجاحًا ثانيًا ولا كتابةً ثانيةً (D6)."""
+
+
+def _nonce() -> str:
+    """مُعرِّفُ استدعاءٍ (D3) حيثُ يُشرَعُ تكرارُ الفعلِ على الكيانِ نفسِه."""
+    return uuid.uuid4().hex
+
+
+class _RegistryUndo:
+    """سجلُّ تراجعٍ لعبورٍ واحدٍ (D7): ما أُنشِئَ وما كانَ قبلَ التغييرِ — ومُعوِّضُه.
+
+    المُطبِّقُ يُسجِّلُ قبلَ الكتابةِ؛ والحدُّ يُنادي `_restore` آليًّا إن فشلَ تثبيتُ
+    النجاحِ بعدَ الالتزامِ (قرارُ المالكِ Q-70). استعادةٌ تقنيّةٌ في جلسةٍ جديدةٍ —
+    «الحذفُ شأنٌ تنفيذيٌّ» والمُعوِّضُ ليس أثرًا مُعلَنًا ولا تراجعُه البوابة.
+    """
+
+    def __init__(self) -> None:
+        self._created: list[tuple[type, Any]] = []
+        self._prior: list[tuple[type, Any, dict[str, Any]]] = []
+
+    def created(self, row: Any) -> None:
+        self._created.append((type(row), sa_inspect(row).identity or _row_pk(row)))
+
+    def prior(self, row: Any, *columns: str) -> None:
+        values = {column: copy.deepcopy(getattr(row, column)) for column in columns}
+        self._prior.append((type(row), sa_inspect(row).identity, values))
+
+    def _restore(self) -> None:
+        session = get_session_factory()()
+        try:
+            for model, identity in reversed(self._created):
+                row = session.get(model, identity)
+                if row is not None:
+                    session.delete(row)
+            for model, identity, values in reversed(self._prior):
+                row = session.get(model, identity)
+                if row is not None:
+                    for column, value in values.items():
+                        setattr(row, column, value)
+            session.commit()
+        finally:
+            session.close()
+
+
+def _row_pk(row: Any) -> tuple[Any, ...]:
+    """المفتاحُ الأساسيُّ لصفٍّ لم يُدفَعْ بعدُ — من أعمدتِه المُعلَنةِ لا تخمينًا."""
+    return tuple(getattr(row, column.key) for column in type(row).__mapper__.primary_key)
+
+
+def _crossing(
+    operation: str, kind: str, suffix: str, detail: str, undo: _RegistryUndo
+) -> tuple[str, dict[str, Any]]:
+    """عقدُ عبورٍ واحدٍ (D3): الهدفُ = قيمةُ المفتاحِ · أثرٌ مُعلَنٌ · مُعوِّضُه · اسمُ العمليّة."""
+    target = f"registry/{suffix}"
+    effect = declared_effect(kind, target, detail)
+    return target, {
+        "declared_effects": (effect,),
+        "operation_key": operation_key(f"registry.{operation}", suffix),
+        "compensators": (
+            compensator(
+                effect.signature,
+                undo._restore,
+                "استعادةٌ تقنيّةٌ: حذفُ ما أُنشِئَ وإرجاعُ ما تغيَّرَ — العمليّةُ لم تثبتْ",
+            ),
+        ),
+        "metadata": {"operation": operation},
+    }
+
+
+def _refuse_replay(guarded: Any, operation: str, target: str) -> None:
+    """الإعادةُ على مفتاحٍ طبيعيٍّ تُرفَعُ صريحةً بلا كتابةٍ ثانيةٍ (D6)."""
+    if guarded.is_replay:
+        raise RegistryReplayError(
+            f"العمليّةُ «{operation}» على «{target}» عبرَت الحدَّ بنجاحٍ من قبلُ — "
+            "الإعادةُ ليست نجاحًا ثانيًا"
+        )
+
+
 class NationalRegistry:
     """السجل الوطني: الهوية الكانونية وروابطها ومناصبها وسلطاتها."""
 
@@ -273,6 +392,8 @@ class NationalRegistry:
     ) -> dict[str, Any]:
         """أنشئ هويةً كانونية — بمعرّفٍ مستقرّ لا باسمٍ ولا بدور.
 
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` بفاعلٍ تنفيذيٍّ مُعلَنٍ (R1 · D1/D2).
+
         `label` وصفٌ للعرض ولا يُستعمل في التعريف ولا يحمل قيدًا فريدًا. والغموض
         يُنشأ صريحًا: `status="unresolved"` مع سببٍ مكتوب، ولا هوية تُختلق.
         """
@@ -289,22 +410,43 @@ class NationalRegistry:
             raise ValueError("الهوية غير المحلولة تلزمها كتابة سببها — الغموض يُسمّى ولا يُترك فراغًا")
 
         tenant = self._tenant_of(context)
-        session = self._session()
-        try:
-            row = IdentityModel(
-                id=f"idn-{uuid.uuid4()}",
-                identity_type=identity_type,
-                status=status,
-                label=label,
-                status_reason=status_reason,
-                tenant_id=tenant,
-                created_by=context.principal_id,
-            )
-            session.add(row)
-            session.commit()
-            identity = self._identity_dict(row)
-        finally:
-            session.close()
+        # معرّفُ الصفّ يُولَّدُ قبلَ العبورِ فيحملهُ المفتاحُ والهدفُ معًا (D3):
+        # الإنشاءُ مشروعُ التكرارِ فالمفتاحُ بمعرّفِ استدعاءٍ لا طبيعيٌّ (D6).
+        identity_id = f"idn-{uuid.uuid4()}"
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                row = IdentityModel(
+                    id=identity_id,
+                    identity_type=identity_type,
+                    status=status,
+                    label=label,
+                    status_reason=status_reason,
+                    tenant_id=tenant,
+                    created_by=context.principal_id,
+                )
+                undo.created(row)
+                session.add(row)
+                session.commit()
+                return self._identity_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.create_identity",
+            "CREATE",
+            f"identities/{identity_id}/create",
+            "إنشاءُ هويةٍ كانونيةٍ بمعرّفٍ مستقرّ",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.create_identity", target)
+        identity = guarded.value
 
         trace = self._record(
             context,
@@ -327,7 +469,11 @@ class NationalRegistry:
         status: str,
         reason: str,
     ) -> dict[str, Any]:
-        """غيّر حالة هوية — تعليقًا أو تقاعدًا أو حلًّا لغموضٍ سابق."""
+        """غيّر حالة هوية — تعليقًا أو تقاعدًا أو حلًّا لغموضٍ سابق.
+
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` (R1). وتغييرُ الحالةِ متكرّرٌ مشروعًا
+        (تعليقٌ ثمّ تقاعدٌ) فالمفتاحُ بمعرّفِ استدعاءٍ (D3/D6).
+        """
         require_domain_permission(context, "identity.status", PERMISSIONS_IDENTITY_WRITE)
         if status not in IDENTITY_STATUSES:
             raise ValueError(
@@ -336,17 +482,42 @@ class NationalRegistry:
         if not reason:
             raise ValueError("تغيير حالة الهوية يلزمه سبب مكتوب")
 
-        session = self._session()
+        # D5: التحقّقُ قبلَ العبورِ — الرسائلُ والأنواعُ كما كانت
+        read = self._session()
         try:
-            row = self._identity_row(session, context, identity_id)
-            previous = row.status
-            row.status = status
-            row.status_reason = reason
-            row.updated_at = _now()
-            session.commit()
-            identity = self._identity_dict(row)
+            previous = self._identity_row(read, context, identity_id).status
         finally:
-            session.close()
+            read.close()
+
+        nonce = _nonce()
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                row = self._identity_row(session, context, identity_id)
+                undo.prior(row, "status", "status_reason", "updated_at")
+                row.status = status
+                row.status_reason = reason
+                row.updated_at = _now()
+                session.commit()
+                return self._identity_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.set_identity_status",
+            "WRITE",
+            f"identities/{identity_id}/status/{nonce}",
+            "تغييرُ حالةِ هويةٍ بسببٍ مكتوبٍ",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.set_identity_status", target)
+        identity = guarded.value
 
         trace = self._record(
             context,
@@ -374,6 +545,13 @@ class NationalRegistry:
     ) -> dict[str, Any]:
         """اربط مبدأً بهويته الكانونية — والربط قرارٌ إداريٌّ مُخوَّل.
 
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` (R1). والمفتاحُ طبيعيٌّ على
+        `(المستأجر، المبدأ)` (D3/D6 · تصحيحٌ مؤرَّخٌ W-625): قيدُ القاعدةِ
+        `UNIQUE (tenant_id, principal_id)` فالاسمُ نفسُهُ جائزٌ في مستأجرينِ،
+        والمفتاحُ يشملُ المستأجرَ كهدفِ 2B `institutions/{tenant}/{code}`.
+        والربطُ القائمُ نفسُهُ يُرجِعُ الردَّ الخاملَ **قبلَ العبورِ** (D5)
+        فلا عمليّةً ثانيةً.
+
         لا يستطيع مبدأٌ أن يربط نفسه بهوية عبر طلبٍ عاديّ: العملية تلزمها
         `manage:all`. وهذا هو معنى «لا يحدّد المُستدعي هويته»: الجلسة تحمل اسمًا،
         وتحويله إلى هوية يجري في هذا الجدول لا في جسم الطلب.
@@ -383,11 +561,14 @@ class NationalRegistry:
         """
         require_domain_permission(context, "identity.principal.link", PERMISSIONS_PRINCIPAL_LINK)
         tenant = self._tenant_of(context)
-        session = self._session()
+
+        # D5: فحصُ الربطِ القائمِ قبلَ العبورِ — السكوتُ المرتجَعُ والتعارضُ
+        # يُقرَّرانِ هنا بلا كتابةٍ ولا قيدٍ في الذرّيّةِ (نفسُ سلوكِ اليومِ)
+        read = self._session()
         try:
-            identity = self._identity_row(session, context, identity_id)
+            self._identity_row(read, context, identity_id)
             existing = (
-                session.query(IdentityPrincipalModel)
+                read.query(IdentityPrincipalModel)
                 .filter(
                     IdentityPrincipalModel.principal_id == principal_id,
                     IdentityPrincipalModel.tenant_id == tenant,
@@ -401,19 +582,44 @@ class NationalRegistry:
                     f"المبدأ '{principal_id}' مربوطٌ بالهوية '{existing.identity_id}' — "
                     "لا يُدمَج تلقائيًّا؛ افصل الربط بقرار صريح أولًا"
                 )
-            row = IdentityPrincipalModel(
-                id=f"idp-{uuid.uuid4()}",
-                principal_id=principal_id,
-                identity_id=identity.id,
-                binding_source=binding_source,
-                tenant_id=tenant,
-                linked_by=context.principal_id,
-            )
-            session.add(row)
-            session.commit()
-            link = self._link_dict(row)
+            link_id = f"idp-{uuid.uuid4()}"
         finally:
-            session.close()
+            read.close()
+
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                identity = self._identity_row(session, context, identity_id)
+                row = IdentityPrincipalModel(
+                    id=link_id,
+                    principal_id=principal_id,
+                    identity_id=identity.id,
+                    binding_source=binding_source,
+                    tenant_id=tenant,
+                    linked_by=context.principal_id,
+                )
+                undo.created(row)
+                session.add(row)
+                session.commit()
+                return self._link_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.link_principal",
+            "CREATE",
+            f"principals/{tenant}/{principal_id}/link",
+            "ربطُ مبدأٍ بهويته الكانونية",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.link_principal", target)
+        link = guarded.value
 
         trace = self._record(
             context,
@@ -452,6 +658,10 @@ class NationalRegistry:
     ) -> dict[str, Any]:
         """اربط وكيلًا تشغيليًّا قائمًا بهويةٍ كانونية — R7-C5.
 
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` (R1) والمفتاحُ طبيعيٌّ على
+        `agent_id` (D3/D6). وعندَ غيابِ `identity_id` يُنشئُ الهويةَ عبرَ السطحِ
+        العامّ `create_identity` فيعبُرُ كلُّ سطحٍ بعبورِهِ المستقلّ (D8-ب).
+
         الوكيل يجب أن يكون موجودًا في `agents` (سجلّ R4 الكانوني): لا يُنشأ وكيل
         هنا ولا تُنسَخ صلاحياته ولا تُلمَس دورة حياته. وإن لم تُعطَ `identity_id`
         أُنشئت هوية من نوع `AGENT` وربُطت به — وهذا **ليس** دمج الجدولين: صفّان في
@@ -477,11 +687,13 @@ class NationalRegistry:
             )
             identity_id = created_identity["id"]
 
-        session = self._session()
+        # D5: فحصُ الربطِ القائمِ قبلَ العبورِ — السكوتُ المرتجَعُ والتعارضُ
+        # يُقرَّرانِ هنا بلا كتابةٍ ولا قيدٍ في الذرّيّةِ (نفسُ سلوكِ اليومِ)
+        read = self._session()
         try:
-            identity = self._identity_row(session, context, identity_id)
+            self._identity_row(read, context, identity_id)
             by_agent = (
-                session.query(IdentityAgentModel)
+                read.query(IdentityAgentModel)
                 .filter(IdentityAgentModel.agent_id == agent_id)
                 .first()
             )
@@ -492,7 +704,7 @@ class NationalRegistry:
                     f"الوكيل '{agent_id}' مربوطٌ بالهوية '{by_agent.identity_id}' — لا دمج تلقائيّ"
                 )
             by_identity = (
-                session.query(IdentityAgentModel)
+                read.query(IdentityAgentModel)
                 .filter(IdentityAgentModel.identity_id == identity_id)
                 .first()
             )
@@ -500,18 +712,43 @@ class NationalRegistry:
                 raise IdentityConflictError(
                     f"الهوية '{identity_id}' مربوطةٌ بالوكيل '{by_identity.agent_id}'"
                 )
-            row = IdentityAgentModel(
-                id=f"ida-{uuid.uuid4()}",
-                agent_id=agent_id,
-                identity_id=identity.id,
-                tenant_id=tenant,
-                linked_by=context.principal_id,
-            )
-            session.add(row)
-            session.commit()
-            link = self._agent_link_dict(row)
+            link_id = f"ida-{uuid.uuid4()}"
         finally:
-            session.close()
+            read.close()
+
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                identity = self._identity_row(session, context, identity_id)
+                row = IdentityAgentModel(
+                    id=link_id,
+                    agent_id=agent_id,
+                    identity_id=identity.id,
+                    tenant_id=tenant,
+                    linked_by=context.principal_id,
+                )
+                undo.created(row)
+                session.add(row)
+                session.commit()
+                return self._agent_link_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.link_agent",
+            "CREATE",
+            f"agents/{agent_id}/link",
+            "ربطُ وكيلٍ تشغيليٍّ قائمٍ بهويةٍ كانونية",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.link_agent", target)
+        link = guarded.value
 
         trace = self._record(
             context,
@@ -552,6 +789,10 @@ class NationalRegistry:
     ) -> dict[str, Any]:
         """أنشئ منصبًا في مؤسسة — المنصب مصدر السلطة، مستقلٌّ عن شاغله.
 
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` (R1) بمعرّفِ استدعاءٍ (D3):
+        إنشاءُ منصبٍ مشروعُ التكرارِ بغيرِ المفتاحِ الطبيعيّ (رمزُ المنصبِ مفتاحُ
+        فريدٌ للمؤسسةِ ويُحفظُ به قيدُ التكرارِ لا بمفتاحِ العبورِ).
+
         نطاق `DEPARTMENT` يلزمه إدارة، وما فوقه لا يحمل إدارة — والقيد مفروضٌ في
         القاعدة أيضًا (`ck_state_positions_department_scope`) لا هنا وحده.
         """
@@ -560,9 +801,11 @@ class NationalRegistry:
             raise ValueError(
                 f"نطاق سلطة غير معروف '{authority_scope}' — المفردة: {list(AUTHORITY_SCOPES)}"
             )
-        session = self._session()
+
+        # D5: التحقّقُ كلّهُ قبلَ العبورِ — الرسائلُ والأنواعُ كما كانت
+        read = self._session()
         try:
-            institution = self._institution_row(session, context, institution_code)
+            institution = self._institution_row(read, context, institution_code)
             if institution.status != "active":
                 raise NationalRegistryError(
                     f"المؤسسة '{institution_code}' حالتها '{institution.status}' — لا منصب فيها"
@@ -570,7 +813,7 @@ class NationalRegistry:
             department_id = None
             if department_code:
                 department = (
-                    session.query(DepartmentModel)
+                    read.query(DepartmentModel)
                     .filter(
                         DepartmentModel.institution_id == institution.id,
                         DepartmentModel.code == department_code,
@@ -591,7 +834,7 @@ class NationalRegistry:
                     f"نطاق '{authority_scope}' لا يحمل إدارة — الإدارة تخصّ نطاق DEPARTMENT وحده"
                 )
             duplicate = (
-                session.query(PositionModel)
+                read.query(PositionModel)
                 .filter(
                     PositionModel.institution_id == institution.id,
                     PositionModel.code == code,
@@ -602,23 +845,50 @@ class NationalRegistry:
                 raise NationalRegistryError(
                     f"رمز المنصب '{code}' مستعمل في المؤسسة '{institution_code}'"
                 )
-            row = PositionModel(
-                id=f"pos-{uuid.uuid4()}",
-                code=code,
-                title=title,
-                institution_id=institution.id,
-                department_id=department_id,
-                authority_scope=authority_scope,
-                status="active",
-                mandate=mandate,
-                tenant_id=institution.tenant_id,
-                created_by=context.principal_id,
-            )
-            session.add(row)
-            session.commit()
-            position = self._position_dict(row)
+            institution_id = institution.id
+            institution_tenant = institution.tenant_id
         finally:
-            session.close()
+            read.close()
+
+        # معرّفُ الصفّ يُولَّدُ قبلَ العبورِ فيحملهُ المفتاحُ والهدفُ معًا (D3)
+        position_id = f"pos-{uuid.uuid4()}"
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                row = PositionModel(
+                    id=position_id,
+                    code=code,
+                    title=title,
+                    institution_id=institution_id,
+                    department_id=department_id,
+                    authority_scope=authority_scope,
+                    status="active",
+                    mandate=mandate,
+                    tenant_id=institution_tenant,
+                    created_by=context.principal_id,
+                )
+                undo.created(row)
+                session.add(row)
+                session.commit()
+                return self._position_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.create_position",
+            "CREATE",
+            f"positions/{position_id}/create",
+            "إنشاءُ منصبٍ في مؤسسةٍ — مصدرُ السلطةِ مستقلٌّ عن شاغله",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.create_position", target)
+        position = guarded.value
 
         trace = self._record(
             context,
@@ -644,6 +914,9 @@ class NationalRegistry:
     ) -> dict[str, Any]:
         """قلِّد مسؤولًا قائمًا منصبًا، ونسبه إلى هويته الكانونية — R7-C4.
 
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` (R1) بمعرّفِ استدعاءٍ (D3):
+        التقليدُ النشطُ مقيّدٌ بالفريدِ (مسؤول، منصب) ويُحفظُ بذلك لا بمفتاحِ العبورِ.
+
         شرطان لا يُتجاوزان: سجلّ المسؤول `appointed`، ووكيله مربوطٌ بهوية. فبلا
         هوية لا تقليد — لأن التقليد بلا هوية هو بالضبط ما جعل الإسناد `PARTIAL`
         قبل R7-C. والمؤسسة يجب أن تكون واحدة في الطرفين: منصبُ مؤسسةٍ لا يُقلَّد
@@ -655,9 +928,11 @@ class NationalRegistry:
         """
         require_domain_permission(context, "position.assign", PERMISSIONS_ASSIGNMENT_WRITE)
         tenant = self._tenant_of(context)
-        session = self._session()
+
+        # D5: التحقّقُ كلّهُ قبلَ العبورِ — الرسائلُ والأنواعُ كما كانت
+        read = self._session()
         try:
-            official = session.get(OfficialModel, official_id)
+            official = read.get(OfficialModel, official_id)
             if official is None or official.tenant_id != tenant:
                 raise AssignmentNotFoundError(
                     f"لا تقليد رسميّ بالمعرّف '{official_id}' في مستأجر '{tenant}'"
@@ -667,7 +942,7 @@ class NationalRegistry:
                 raise PositionInactiveError(
                     f"المسؤول '{official_id}' حالته '{official.status}' — لا منصب لغير القائم"
                 )
-            position = session.get(PositionModel, position_id)
+            position = read.get(PositionModel, position_id)
             if position is None or position.tenant_id != tenant:
                 raise PositionNotFoundError(f"لا منصب بالمعرّف '{position_id}'")
             if position.status != "active":
@@ -680,7 +955,7 @@ class NationalRegistry:
                     f"'{official.institution_id}' — لا تقليد عبر المؤسسات"
                 )
             agent_link = (
-                session.query(IdentityAgentModel)
+                read.query(IdentityAgentModel)
                 .filter(IdentityAgentModel.agent_id == official.agent_id)
                 .first()
             )
@@ -690,7 +965,7 @@ class NationalRegistry:
                     "اربطه بهوية قبل التقليد (R7-C5)"
                 )
             duplicate = (
-                session.query(OfficialPositionModel)
+                read.query(OfficialPositionModel)
                 .filter(
                     OfficialPositionModel.official_id == official_id,
                     OfficialPositionModel.position_id == position_id,
@@ -702,20 +977,46 @@ class NationalRegistry:
                 raise DuplicateAssignmentError(
                     f"المسؤول '{official_id}' يشغل المنصب '{position_id}' بالفعل ({duplicate.id})"
                 )
-            row = OfficialPositionModel(
-                id=f"opos-{uuid.uuid4()}",
-                official_id=official_id,
-                identity_id=agent_link.identity_id,
-                position_id=position_id,
-                status="active",
-                assigned_by=context.principal_id,
-                tenant_id=tenant,
-            )
-            session.add(row)
-            session.commit()
-            assignment = self._assignment_dict(row)
+            identity_id = agent_link.identity_id
         finally:
-            session.close()
+            read.close()
+
+        # معرّفُ الصفّ يُولَّدُ قبلَ العبورِ فيحملهُ المفتاحُ والهدفُ معًا (D3)
+        assignment_id = f"opos-{uuid.uuid4()}"
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                row = OfficialPositionModel(
+                    id=assignment_id,
+                    official_id=official_id,
+                    identity_id=identity_id,
+                    position_id=position_id,
+                    status="active",
+                    assigned_by=context.principal_id,
+                    tenant_id=tenant,
+                )
+                undo.created(row)
+                session.add(row)
+                session.commit()
+                return self._assignment_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.assign_position",
+            "CREATE",
+            f"assignments/{assignment_id}/assign",
+            "تقليدُ مسؤولٍ قائمٍ منصبًا ونسبُهُ إلى هويتهِ الكانونية",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.assign_position", target)
+        assignment = guarded.value
 
         trace = self._record(
             context,
@@ -738,26 +1039,57 @@ class NationalRegistry:
         assignment_id: str,
         reason: str,
     ) -> dict[str, Any]:
-        """اعزل تقليد منصب — والصفّ يبقى تاريخًا ولا يُحذَف."""
+        """اعزل تقليد منصب — والصفّ يبقى تاريخًا ولا يُحذَف.
+
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` (R1) بمفتاحٍ طبيعيٍّ على
+        `assignment_id` (D3/D6): العزلُ كتابةٌ واحدة، والمعزولُ سلفًا يُرجِعُ
+        الردَّ الخاملَ **قبلَ العبورِ** (D5).
+        """
         require_domain_permission(context, "position.revoke", PERMISSIONS_ASSIGNMENT_WRITE)
         if not reason:
             raise ValueError("العزل يلزمه سبب مكتوب")
         tenant = self._tenant_of(context)
-        session = self._session()
+
+        # D5: الردُّ الخاملُ للمعزولِ سلفًا قبلَ العبورِ (نفسُ سلوكِ اليومِ)
+        read = self._session()
         try:
-            row = session.get(OfficialPositionModel, assignment_id)
-            if row is None or row.tenant_id != tenant:
+            existing = read.get(OfficialPositionModel, assignment_id)
+            if existing is None or existing.tenant_id != tenant:
                 raise AssignmentNotFoundError(f"لا تقليد منصبٍ بالمعرّف '{assignment_id}'")
-            require_tenant(context, row.tenant_id)
-            if row.status == "revoked":
-                return {**self._assignment_dict(row), "changed": False}
-            row.status = "revoked"
-            row.revoked_at = _now()
-            row.revocation_reason = reason
-            session.commit()
-            assignment = self._assignment_dict(row)
+            require_tenant(context, existing.tenant_id)
+            if existing.status == "revoked":
+                return {**self._assignment_dict(existing), "changed": False}
         finally:
-            session.close()
+            read.close()
+
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                row = session.get(OfficialPositionModel, assignment_id)
+                undo.prior(row, "status", "revoked_at", "revocation_reason")
+                row.status = "revoked"
+                row.revoked_at = _now()
+                row.revocation_reason = reason
+                session.commit()
+                return self._assignment_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.revoke_assignment",
+            "WRITE",
+            f"assignments/{assignment_id}/revoke",
+            "عزلُ تقليدِ منصبٍ بسببٍ مكتوبٍ — الصفّ يبقى تاريخًا",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.revoke_assignment", target)
+        assignment = guarded.value
 
         trace = self._record(
             context,
@@ -791,6 +1123,9 @@ class NationalRegistry:
     ) -> dict[str, Any]:
         """امنح منصبًا سلطةً على عمليةٍ مُسمّاة وهدفٍ مُسمّى — R7-C8.
 
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` (R1) بمعرّفِ استدعاءٍ (D3):
+        المنحُ مشروعُ التكرارِ على المنصبِ نفسِهِ بعمليّاتٍ/أهدافٍ مختلفةٍ.
+
         الأهداف تُتحقَّق من القاعدة: الموازنة والحساب والإدارة يجب أن تنتمي إلى
         مؤسسة المِنحة. فلا مِنحة على موازنة مؤسسةٍ أخرى، ولو صحّ معرّفها.
 
@@ -806,9 +1141,11 @@ class NationalRegistry:
             raise ValueError(f"نطاق غير معروف '{scope}' — المفردة: {list(AUTHORITY_SCOPES)}")
 
         tenant = self._tenant_of(context)
-        session = self._session()
+
+        # D5: التحقّقُ كلّهُ قبلَ العبورِ — الرسائلُ والأنواعُ كما كانت
+        read = self._session()
         try:
-            position = session.get(PositionModel, position_id)
+            position = read.get(PositionModel, position_id)
             if position is None or position.tenant_id != tenant:
                 raise PositionNotFoundError(f"لا منصب بالمعرّف '{position_id}'")
             require_tenant(context, position.tenant_id)
@@ -827,38 +1164,62 @@ class NationalRegistry:
                 target_department = department_id or position.department_id
                 if target_department is None:
                     raise InvalidGrantTargetError("نطاق الإدارة يلزمه إدارة مُسمّاة")
-                self._assert_department_in(session, target_department, target_institution)
+                self._assert_department_in(read, target_department, target_institution)
                 department_id = target_department
             else:
                 if department_id is not None:
-                    self._assert_department_in(session, department_id, target_institution)
+                    self._assert_department_in(read, department_id, target_institution)
 
             if budget_id is not None:
-                self._assert_budget_in(session, budget_id, target_institution)
+                self._assert_budget_in(read, budget_id, target_institution)
             if account_id is not None:
-                self._assert_account_exists(session, account_id)
-
-            row = AuthorityGrantModel(
-                id=f"agr-{uuid.uuid4()}",
-                position_id=position_id,
-                operation=operation,
-                scope=scope,
-                institution_id=target_institution,
-                department_id=department_id,
-                budget_id=budget_id,
-                account_id=account_id,
-                # لا `str(max_amount)`: كانت تُبيِّضُ العائمَ فتُمرِّرُه عبرَ بابِ
-                # المالِ الذي يرفضُه. و`to_money` هو البابُ (Q-20).
-                max_amount=None if max_amount is None else to_money(max_amount),
-                status="active",
-                granted_by=context.principal_id,
-                tenant_id=tenant,
-            )
-            session.add(row)
-            session.commit()
-            grant = self._grant_dict(row)
+                self._assert_account_exists(read, account_id)
         finally:
-            session.close()
+            read.close()
+
+        # معرّفُ الصفّ يُولَّدُ قبلَ العبورِ فيحملهُ المفتاحُ والهدفُ معًا (D3)
+        grant_row_id = f"agr-{uuid.uuid4()}"
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                row = AuthorityGrantModel(
+                    id=grant_row_id,
+                    position_id=position_id,
+                    operation=operation,
+                    scope=scope,
+                    institution_id=target_institution,
+                    department_id=department_id,
+                    budget_id=budget_id,
+                    account_id=account_id,
+                    # لا `str(max_amount)`: كانت تُبيِّضُ العائمَ فتُمرِّرُه عبرَ بابِ
+                    # المالِ الذي يرفضُه. و`to_money` هو البابُ (Q-20).
+                    max_amount=None if max_amount is None else to_money(max_amount),
+                    status="active",
+                    granted_by=context.principal_id,
+                    tenant_id=tenant,
+                )
+                undo.created(row)
+                session.add(row)
+                session.commit()
+                return self._grant_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.grant_authority",
+            "CREATE",
+            f"grants/{grant_row_id}/grant",
+            "منحُ منصبٍ سلطةً على عمليّةٍ مُسمّاةٍ وهدفٍ مُسمّى",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.grant_authority", target)
+        grant = guarded.value
 
         trace = self._record(
             context,
@@ -882,26 +1243,57 @@ class NationalRegistry:
         grant_id: str,
         reason: str,
     ) -> dict[str, Any]:
-        """اسحب مِنحة سلطة — والصفّ يبقى، فيُقرأ لاحقًا أن السلطة كانت ثم سُحبت."""
+        """اسحب مِنحة سلطة — والصفّ يبقى، فيُقرأ لاحقًا أن السلطة كانت ثم سُحبت.
+
+        يعبرُ الحدَّ السياديَّ بالفعلِ `register` (R1) بمفتاحٍ طبيعيٍّ على
+        `grant_id` (D3/D6): السحبُ كتابةٌ واحدة، والمسحوبُ سلفًا يُرجِعُ الردَّ
+        الخاملَ **قبلَ العبورِ** (D5).
+        """
         require_domain_permission(context, "authority.revoke", PERMISSIONS_GRANT_WRITE)
         if not reason:
             raise ValueError("سحب المِنحة يلزمه سبب مكتوب")
         tenant = self._tenant_of(context)
-        session = self._session()
+
+        # D5: الردُّ الخاملُ للمسحوبِ سلفًا قبلَ العبورِ (نفسُ سلوكِ اليومِ)
+        read = self._session()
         try:
-            row = session.get(AuthorityGrantModel, grant_id)
-            if row is None or row.tenant_id != tenant:
+            existing = read.get(AuthorityGrantModel, grant_id)
+            if existing is None or existing.tenant_id != tenant:
                 raise GrantNotFoundError(f"لا مِنحة سلطةٍ بالمعرّف '{grant_id}'")
-            require_tenant(context, row.tenant_id)
-            if row.status == "revoked":
-                return {**self._grant_dict(row), "changed": False}
-            row.status = "revoked"
-            row.revoked_at = _now()
-            row.revocation_reason = reason
-            session.commit()
-            grant = self._grant_dict(row)
+            require_tenant(context, existing.tenant_id)
+            if existing.status == "revoked":
+                return {**self._grant_dict(existing), "changed": False}
         finally:
-            session.close()
+            read.close()
+
+        undo = _RegistryUndo()
+
+        def _apply(_effect: Any) -> dict[str, Any]:
+            """المُطبّقُ المتداخلُ الخاصّ — الكتابةُ الوحيدةُ داخلَ الحدّ (D4)."""
+            session = self._session()
+            try:
+                row = session.get(AuthorityGrantModel, grant_id)
+                undo.prior(row, "status", "revoked_at", "revocation_reason")
+                row.status = "revoked"
+                row.revoked_at = _now()
+                row.revocation_reason = reason
+                session.commit()
+                return self._grant_dict(row)
+            finally:
+                session.close()
+
+        target, crossing = _crossing(
+            "NationalRegistry.revoke_authority",
+            "WRITE",
+            f"grants/{grant_id}/revoke",
+            "سحبُ مِنحةِ سلطةٍ بسببٍ مكتوبٍ — الصفّ يبقى تاريخًا",
+            undo,
+        )
+        guarded = _registry_authorizer().guard_declared(
+            REGISTRY_VERB, target, applier=_apply, **crossing
+        )
+        _refuse_replay(guarded, "NationalRegistry.revoke_authority", target)
+        grant = guarded.value
 
         trace = self._record(
             context,
@@ -1143,7 +1535,11 @@ __all__ = [
     "NationalRegistryError",
     "PositionInactiveError",
     "PositionNotFoundError",
+    "REGISTRY_ACTOR",
+    "REGISTRY_VERB",
+    "RegistryReplayError",
     "UnknownAgentError",
     "get_national_registry",
     "reset_national_registry",
+    "reset_registry_authorizer",
 ]
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && cat federal/executive/services/tests/test_wi107_national_registry_register_sovereign.py
EXIT: 0
BYTES: 33729
SHA256: 71ec18aeaf566734dae397bf87e6b2e4c2b656c88712b5b2fb820898f3bd6a55
NO_EOL: 0
--- OUTPUT ---
"""
WI-107 · R1 — أسطحُ `national_registry/service.py` التسعةُ تعبرُ الحدَّ السياديَّ
بفاعلٍ تنفيذيٍّ مُعلَنٍ بالفعلِ `register` (قرارُ المالكِ D17-3 · سؤالُ Q-2 المعلَّقُ).

الهدف: إثباتُ أنَّ كلَّ سطحٍ عامٍّ مُغيِّرٍ في الوحدةِ يعبرُ الحدَّ بالفعلِ نفسِه وبالفاعلِ
       الثابتِ في الوحدةِ، وأنَّ الكتابةَ كلَّها خلفَ الحدِّ (لا صفَّ يُكتَبُ إن رُفِضَ)،
       وأنَّ المُعوِّضَ يستعيدُ الحالةَ كما كانت، وأنَّ الإعادةَ على مفتاحٍ طبيعيٍّ تُرفَعُ صريحةً.
النطاق: قياسُ سلوكِ الوحدةِ عبرَ الحدِّ وحدَه — لا تعديلَ للبوابةِ ولا للقواعدِ ولا لـ
        `test_r7c_national_registry.py` ولا `test_2b_state_registry_sovereign.py` (بلا تعديلٍ).
المالك: federal/executive/services — WI-107 (تصميمُ docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md
        المُلتزَمُ قبلَ الشِّفرةِ في W-623، والشِّفرةُ في W-625).
تاريخ الإنشاء: 2026-10-23 (WI-107 · الدفعةُ R1)

الفحوصُ كما وردتْ في التصميمِ (§ 4) — T1–T8:
- T1 · العبورُ: الأسطحُ التسعةُ كلُّها ⇒ 9 عمليّاتٍ متمايزةً بالفعلِ `register` وALLOW.
- T2 · الفاعلُ مُعلَنٌ لا مُثبَّتٌ (تصحيحٌ مؤرَّخٌ W-625): `register` مُنطَّقٌ لا حصريٌّ
        (مسبارُ W-623) فتبديلُ الثابتِ لا يُرفضُ — المقيسُ أنّ فاعلَ العبورِ يسري من
        ثابتِ الوحدةِ إلى سجلِّ البوّابةِ (LEGISLATIVE فوقَ الاختبارِ).
- T3 · لا كتابةَ خارجَ المُطبِّقِ: حكمُ رفضٍ حقيقيٌّ من المحرّكِ يُحاكى في `gateway.decide`
        (نمطُ 2B) ⇒ لكلِّ سطحٍ: الصفوفُ والأعمدةُ كما كانت.
- T4 · المُعوِّضُ على الإنشاءِ (`create_identity`) · T5 · على التحديثِ (`revoke_assignment`).
- T6 · الإعادةُ: (أ) الربطُ القائمُ نفسُهُ ⇒ `created: False` بلا عبورٍ ثانٍ ·
        (ب) على مستوى الحدِّ ⇒ `is_replay` و`RegistryReplayError` صريحًا ·
        (ج) الاسمُ نفسُهُ في مستأجرينِ مختلفَينِ ليسَ إعادةً (المفتاحُ بيشملُ المستأجرَ).
- T7 · الجردُ: 9 عامًّا في الوحدةِ كلُّها عابرةٌ · T8 · الثابتانِ.

الحدُّ المُعلَنُ: لا `VERIFIED` ولا `CLOSED` بيدِ المنفِّذِ (§ 4.3) — ملفُّ قياسٍ لا حُكمِ مراجعةٍ.

الدليلُ المُعادُ تشغيلُه (من federal/executive/services):
    ../../../.venv/bin/python -m pytest tests/test_wi107_national_registry_register_sovereign.py -q
"""

from __future__ import annotations

import importlib.util
import math
import sys
import time
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import pytest
from sqlalchemy import select

from amos_federation.common.database import get_session_factory, init_db
from amos_federation.common.principal import (
    DEFAULT_TENANT,
    AuthorizationContext,
    Principal,
)
from amos_federation.services.executive_core.agent_identity import register_identity
from amos_federation.services.national_registry import service as national_registry_module
from amos_federation.services.national_registry.models import (
    GRANTABLE_OPERATIONS,
    AuthorityGrantModel,
    IdentityAgentModel,
    IdentityModel,
    IdentityPrincipalModel,
    OfficialPositionModel,
    PositionModel,
)
from amos_federation.services.national_registry.service import (
    REGISTRY_ACTOR,
    REGISTRY_VERB,
    RegistryReplayError,
    get_national_registry,
    reset_national_registry,
)
from amos_federation.services.state_registry.models import (
    DepartmentModel,
    InstitutionModel,
    OfficialModel,
)
from amos_federation.services.state_registry.service import (
    get_state_registry,
    reset_state_registry,
)

#: الأسطحُ التسعةُ المقيسةُ بعدَ الشِّفرةِ (جردُ evidence/W-623 + تعديلاتُ W-625).
EXPECTED_OPERATIONS = frozenset(
    {
        "NationalRegistry.create_identity",
        "NationalRegistry.set_identity_status",
        "NationalRegistry.link_principal",
        "NationalRegistry.link_agent",
        "NationalRegistry.create_position",
        "NationalRegistry.assign_position",
        "NationalRegistry.revoke_assignment",
        "NationalRegistry.grant_authority",
        "NationalRegistry.revoke_authority",
    }
)

_MODELS = (
    AuthorityGrantModel,
    OfficialPositionModel,
    PositionModel,
    IdentityAgentModel,
    IdentityPrincipalModel,
    IdentityModel,
)
_STATE_MODELS = (
    OfficialModel,
    DepartmentModel,
    InstitutionModel,
)


def _purge_registry_state() -> None:
    """مسحٌ شاملٌ لكلِّ جداولِ قاعدةِ الفحصِ — من الفاحصِ لا من نماذجِ ORM.

    جداولُ الخدماتِ موزَّعةٌ على عدةِّ `Base` — فالترتيبُ من نماذجِ ORM ناقصٌ
    (قِيسَ في W-625: `DELETE FROM state_institutions` يُرفَضُ بقيودٍ من حساباتٍ
    خلَّفها ملفٌّ سابقٌ). فالفاحصُ يعدِّدُ الجداولِ الفعليةَ كلَّها، والمسحُ
    الكليُّ في اتصالٍ واحدٍ مخصَّصٍ معَ تعطيلِ فرضِ المفاتيحِ فيه لا يُخلِّفُ
    يتيمًا — وهو عينُ ما يفعلهُ حذفُ ملفِّ القاعدةِ نفسِه في بدايةِ الجلسةِ
    (`pytest_sessionstart`)، بلا إعادةِ إنشاءِ المخطَّطِ.
    """
    from sqlalchemy import inspect as sa_inspect
    from sqlalchemy import text as sa_text

    init_db()
    session = get_session_factory()()
    try:
        session.execute(sa_text("PRAGMA foreign_keys=OFF"))
        for table in sa_inspect(session.get_bind()).get_table_names():
            session.execute(sa_text(f'DELETE FROM "{table}"'))  # noqa: S608 — اسمٌ من الفاحصِ
        session.commit()
    finally:
        session.close()


_KING_PERMISSIONS = ("*",)


@pytest.fixture(autouse=True)
def _fresh_registry(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """جداولُ الوحدتينِ نظيفةٌ قبلَ كلِّ فحصٍ وبعدَه · والمُفوِّضُ المحفوظُ مُفرَغٌ (D1).

    وسجلُّ الذرّيّةِ **معزولٌ لكلِّ فحصٍ** (توجيهُ المستشارِ في W-625): المسارُ
    يُقرأُ من البيئةِ عندَ بناءِ الحدِّ، فتوجيهُهُ إلى ملفٍّ مؤقّتٍ يعزلُ الفحوصَ
    عن سجلِّ التشغيلِ الدائمِ — لا مسحَ لملفِّ `.runtime` لحلِّ مشكلةِ اختبارٍ.
    """
    monkeypatch.setenv(
        "AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER", str(tmp_path / "wi107-idempotency.json")
    )
    _purge_registry_state()
    reset_state_registry()
    reset_national_registry()
    national_registry_module.reset_registry_authorizer()
    yield
    _purge_registry_state()
    reset_state_registry()
    reset_national_registry()
    national_registry_module.reset_registry_authorizer()


class RecordingRegistryAuthorizer(national_registry_module.ConstitutionalAuthorizer):
    """يسجّلُ كلَّ عبورٍ (اسمَ العمليّةِ والدليلَ) — لقياسِ العبورِ لا لاتخاذِ قرارٍ."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.crossings: list[tuple[str, Any]] = []

    def guard_declared(self, *args: Any, **kwargs: Any) -> Any:
        guarded = super().guard_declared(*args, **kwargs)
        self.crossings.append(((kwargs.get("metadata") or {}).get("operation", ""), guarded))
        return guarded


def _install_recording_authorizer() -> RecordingRegistryAuthorizer:
    """مُصرِّحٌ مسجِّلٌ بثابتِ الوحدةِ نفسِه — المسارُ الإنتاجيُّ كما هو (D1)."""
    authorizer = RecordingRegistryAuthorizer(actor=national_registry_module.REGISTRY_ACTOR)
    national_registry_module._DEFAULT_REGISTRY_AUTHORIZER = authorizer
    return authorizer


def _context(role_id: str = "king", tenant_id: str = DEFAULT_TENANT) -> AuthorizationContext:
    """سياقٌ مُتحقَّقٌ منه بدورٍ وصلاحيّاتٍ صريحة — لا ادّعاءَ دورٍ من الطلب.

    الاسمُ فريدٌ في كلّ استدعاءٍ: مفتاحُ `link_principal` الطبيعيّ على `principal_id`
    وسجلُّ الذرّيّةِ ملفٌّ ثابتٌ — فتكرارُ الاسمِ بينَ الفحوصِ يُصبحُ إعادةً مرفوضةً
    لا علاقةَ لها بالمقيسِ (D6).
    """
    suffix = uuid.uuid4().hex[:8]
    return AuthorizationContext.from_principal(
        Principal.from_session_record(
            session_id=f"wi107-{role_id}-{suffix}",
            username=f"{role_id}-{suffix}",
            role_id=role_id,
            permissions=_KING_PERMISSIONS,
            expires_at=datetime.now(UTC) + timedelta(hours=1),
            tenant_id=tenant_id,
        )
    )


def _crown() -> AuthorizationContext:
    """التاج — `*` فيمرّ في كل حدّ عبر `has_permission` نفسها."""
    return _context("king")


def _code(prefix: str) -> str:
    return f"{prefix}-WI107-{uuid.uuid4().hex[:8].upper()}"


def _agent() -> str:
    """وكيلٌ حقيقيٌّ في `agents` — سجلّ R4 الكانوني، ولا يُنشئه السجلّ الوطني."""
    agent_id = f"agent-wi107-{uuid.uuid4().hex[:10]}"
    register_identity(agent_id, f"وكيل {agent_id}", "executor", tenant_id=DEFAULT_TENANT)
    return agent_id


def _count(model: type) -> int:
    session = get_session_factory()()
    try:
        return len(session.execute(select(model)).scalars().all())
    finally:
        session.close()


def _snapshot() -> dict[str, list[tuple[Any, ...]]]:
    """لقطةُ صفوفِ الوحدتينِ بأعمدتها — للمقارنةِ قبلَ الرفضِ وبعدَه (T3)."""
    session = get_session_factory()()
    try:
        out: dict[str, list[tuple[Any, ...]]] = {}
        for model in (*_STATE_MODELS, *_MODELS):
            columns = [c.key for c in model.__table__.columns]
            rows = session.execute(select(model)).scalars().all()
            out[model.__name__] = sorted(
                (tuple(repr(getattr(r, c)) for c in columns) for r in rows), key=repr
            )
        return out
    finally:
        session.close()


def _drop_settle(monkeypatch: pytest.MonkeyPatch, ledger: Any, label: str) -> Any:
    """إسقاطُ تثبيتِ النجاحِ بعدَ التزامِ المُطبِّقِ — يُرجِعُ الأصلَ لرفعِ الإسقاط."""
    original = type(ledger).mark_succeeded

    def failing_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError(f"تثبيتُ النجاحِ مُسقَطٌ — {label}")

    monkeypatch.setattr(type(ledger), "mark_succeeded", failing_mark_succeeded)
    return original


def _next_second() -> None:
    """معرِّفُ الإذنِ `EP-<العقد>-<الثانية>` (سابقةُ W-603): الإعادةُ تعبرُ إلى الثانيةِ التاليةِ."""
    now = time.time()
    time.sleep(math.ceil(now) - now + 0.05)


class _Chain:
    """سلسلةٌ كاملة جاهزة: مؤسسة · مسؤول · هوية · منصب · تقليد · مِنحة."""

    def __init__(self, **kwargs: object) -> None:
        self.__dict__.update(kwargs)


def _chain(crown: AuthorizationContext) -> _Chain:
    """ابنِ السلسلةَ بالعملياتِ الحقيقيةِ — لا صفوفًا مزروعةً يدويًّا.

    الترتيبُ كترتيبِ `test_r7c_national_registry._chain`: المؤسسةُ قبلَ المسؤولِ قبلَ
    الهويةِ قبلَ المنصبِ قبلَ التقليدِ — فكلُّ سطحٍ يعبُرُ بعبورِهِ المستقلِّ (D8).
    """
    state = get_state_registry()
    national = get_national_registry()
    institution = state.register_institution(
        context=crown,
        code=_code("INST"),
        name="وزارةُ قياسِ R1",
        kind="ministry",
        branch="executive",
    )
    agent_id = _agent()
    official = state.appoint_official(
        context=crown,
        agent_id=agent_id,
        institution_code=institution["code"],
        title="أمينُ الخزانة",
    )
    identity = national.create_identity(context=crown, identity_type="PERSON", label="أمينُ الخزانة")
    national.link_principal(
        context=crown, principal_id=crown.principal_id, identity_id=identity["id"]
    )
    national.link_agent(context=crown, agent_id=agent_id, identity_id=identity["id"])
    position = national.create_position(
        context=crown,
        code=_code("POS"),
        title="أمينُ الخزانة",
        institution_code=institution["code"],
        authority_scope="INSTITUTION",
    )
    assignment = national.assign_position(
        context=crown, official_id=official["id"], position_id=position["id"]
    )
    grant = national.grant_authority(
        context=crown,
        position_id=position["id"],
        operation=GRANTABLE_OPERATIONS[0],
        scope="INSTITUTION",
    )
    return _Chain(
        institution=institution,
        agent_id=agent_id,
        official=official,
        identity=identity,
        position=position,
        assignment=assignment,
        grant=grant,
    )


def _exercise_all_surfaces(crown: AuthorizationContext) -> None:
    """استدعاءُ الأسطحِ التسعةِ كلِّها مرّةً — بالواجهةِ العامّةِ كما هي."""
    national = get_national_registry()
    chain = _chain(crown)

    # بقايا السلسلةِ: الحالةُ والعزلُ والسحبُ — أسطحُ التحديثِ الثلاثةُ
    national.set_identity_status(
        context=crown, identity_id=chain.identity["id"], status="suspended", reason="قياسُ T1"
    )
    national.revoke_assignment(
        context=crown, assignment_id=chain.assignment["id"], reason="قياسُ T1"
    )
    national.revoke_authority(context=crown, grant_id=chain.grant["id"], reason="قياسُ T1")


# ── T1 · العبورُ: تسعُ عمليّاتٍ بالفعلِ register ──────────────────────────────


def test_wi107_t1_every_surface_crosses_as_register() -> None:
    authorizer = _install_recording_authorizer()
    crown = _crown()
    _exercise_all_surfaces(crown)

    operations = {name for name, _ in authorizer.crossings}
    assert operations == EXPECTED_OPERATIONS
    for name, guarded in authorizer.crossings:
        evidence = guarded.evidence.as_dict()
        assert evidence["action"] == "register", name
        assert evidence["decision"] == "ALLOW", name
        assert evidence["target"].startswith("registry/"), name
    record = authorizer.gateway.records[-1]
    assert record.action == "register"
    assert record.actor == "executive"


# ── T2 · الفاعلُ ثابتُ الوحدةِ — تبديلُه يُسقِطُ العبورَ ───────────────────────


def test_wi107_t2_declared_actor_flows_from_the_unit_constant(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """تصحيحٌ مؤرّخٌ (W-625): مسبارُ W-623 أثبتَ أنّ `register` مُنطّقٌ لا حصريٌّ —
    فتبديلُ الفاعلِ لا يُرفضُ (بخلافِ `coordinate` في F1). فالمقيسُ هنا جوهرُ D1:
    الفاعلُ **مُعلَنٌ في الوحدةِ** يسري على العبورِ كلِّه — ليس معاملًا للمُنادي ولا
    مثبتًا في نداءِ الحدّ — والرفضُ الحقيقيّ يُقاسُ في T3 بحكمِ محرّكٍ صريحٍ.
    """
    crown = _crown()
    monkeypatch.setattr(national_registry_module, "REGISTRY_ACTOR", "LEGISLATIVE")
    national_registry_module.reset_registry_authorizer()

    # لا مُصرِّحٌ مُحقونٌ هنا (توجيهُ المستشارِ): المسارُ الإنتاجيُّ نفسُهُ يبني
    # المُصرِّحَ عندَ أوّلِ عبورٍ، فسجلُّ البوّابةِ يُقرأُ من كائنِ الإنتاجِ
    national = get_national_registry()
    identity = national.create_identity(context=crown, identity_type="PERSON", label="فاعلٌ مُعلَنٌ")
    link = national.link_principal(
        context=crown,
        principal_id=f"pid-wi107-t2-{uuid.uuid4().hex[:8]}",
        identity_id=identity["id"],
    )
    assert _count(IdentityModel) == 1
    assert _count(IdentityPrincipalModel) == 1
    assert link["created"] is True

    # السطحانِ اللذانِ نصَّ عليهما التصميمُ (create_identity وlink_principal)
    # عبَرا بمُصرِّحِ الإنتاجِ وفاعلِهِ من ثابتِ الوحدةِ المُبدَّلِ فوقَ الاختبارِ
    authorizer = national_registry_module._registry_authorizer()
    records = authorizer.gateway.records
    assert len(records) >= 2
    for record in records:
        assert record.actor.lower() == "legislative", "الفاعلُ لا يسري من ثابتِ الوحدةِ"
    assert any(r.action == "register" for r in records)


# ── T3 · لا كتابةَ خارجَ المُطبِّقِ — لكلِّ سطحٍ ───────────────────────────────


def _real_denial_verdict() -> Any:
    """حكمُ رفضٍ **حقيقيٌّ** من المحرّكِ الدستوريّ نفسِه — لا نصٌّ مُصطنَع (نمطُ 2B).

    يُقرأُ على فعلٍ حصريٍّ لفاعلٍ لا يملكُه (المادةُ الثالثةُ · R-003-1)، ويُستعملُ
    ليُقاسَ **تصرّفُ الخدمةِ عندَ الرفضِ**، لا ليُقاسَ الدستورُ من جديد.
    """
    from core.constitutional_engine.engine import ConstitutionalEngine
    from core.constitutional_engine.model import ActionRequest, Branch

    return ConstitutionalEngine().evaluate(
        ActionRequest(actor=Branch.EXECUTIVE, action="allocate_budget", target="probe"),
        record=False,
    )


def test_wi107_t3_denied_crossing_leaves_every_surface_untouched(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.gateway import SovereigntyViolation

    # التحضيرُ بالفاعلِ الصحيحِ: كيانٌ قائمٌ لكلِّ سطحٍ، وسلسلةٌ كاملةٌ
    crown = _crown()
    national = get_national_registry()
    chain = _chain(crown)
    spare_identity = national.create_identity(
        context=crown, identity_type="PERSON", label="احتياطيّة"
    )
    spare_agent = _agent()
    spare_position = national.create_position(
        context=crown,
        code=_code("POS"),
        title="احتياطيّ",
        institution_code=chain.institution["code"],
        authority_scope="INSTITUTION",
    )
    before = _snapshot()

    # الرفضُ يُحاكى في موضعِهِ الحقيقيّ (`gateway.decide`) بحكمٍ حقيقيٍّ من
    # المحرّكِ — لا بتعطيلِ الحدّ ولا باستبدالِهِ (نمطُ 2B · تصحيحٌ مؤرّخٌ W-625:
    # مسبارُ W-623 أثبتَ أنّ تبديلَ الفاعلِ لا يرفضُ `register` فالرفضُ يُقرأُ صريحًا)
    authorizer = _install_recording_authorizer()
    denial = _real_denial_verdict()
    assert denial.decision.name == "DENY", "لم يُقرأْ حكمُ رفضٍ حقيقيٍّ من الدستور."

    def _deny(*_args: Any, **_kwargs: Any) -> None:
        raise SovereigntyViolation(denial)

    monkeypatch.setattr(authorizer.gateway, "decide", _deny)

    calls = [
        lambda: national.create_identity(context=crown, identity_type="PERSON", label="x"),
        lambda: national.set_identity_status(
            context=crown, identity_id=chain.identity["id"], status="suspended", reason="x"
        ),
        lambda: national.link_principal(
            context=crown,
            principal_id=f"pid-wi107-{uuid.uuid4().hex[:8]}",
            identity_id=spare_identity["id"],
        ),
        lambda: national.link_agent(
            context=crown, agent_id=spare_agent, identity_id=spare_identity["id"]
        ),
        lambda: national.create_position(
            context=crown,
            code=_code("POS"),
            title="x",
            institution_code=chain.institution["code"],
            authority_scope="INSTITUTION",
        ),
        lambda: national.assign_position(
            context=crown, official_id=chain.official["id"], position_id=spare_position["id"]
        ),
        lambda: national.revoke_assignment(
            context=crown, assignment_id=chain.assignment["id"], reason="x"
        ),
        lambda: national.grant_authority(
            context=crown,
            position_id=chain.position["id"],
            operation=GRANTABLE_OPERATIONS[-1],
            scope="INSTITUTION",
        ),
        lambda: national.revoke_authority(context=crown, grant_id=chain.grant["id"], reason="x"),
    ]
    assert len(calls) == len(EXPECTED_OPERATIONS)
    for call in calls:
        with pytest.raises(SovereigntyViolation):
            call()

    assert _snapshot() == before


# ── T4 · المُعوِّضُ على الإنشاءِ ─────────────────────────────────────────────


def test_wi107_t4_compensator_removes_created_identity(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired
    from core.sovereignty.idempotency import OperationStatus

    crown = _crown()
    # لا مُصرِّحٌ مُحقونٌ (توجيهُ المستشارِ): يُلتقطُ مفتاحُ العمليّةِ الفعليُّ
    # بلفٍّ يُفوِّضُ التنفيذَ الأصليَّ — فالقياسُ على مفتاحِ هذه العمليّةِ تحديدًا
    authorizer = national_registry_module._registry_authorizer()
    ledger = authorizer.boundary.idempotency_ledger
    captured: dict[str, Any] = {}
    original_guard = authorizer.guard_declared

    def _capturing_guard(*args: Any, **kwargs: Any) -> Any:
        captured["key"] = kwargs.get("operation_key")
        return original_guard(*args, **kwargs)

    monkeypatch.setattr(authorizer, "guard_declared", _capturing_guard)
    original = _drop_settle(monkeypatch, ledger, "T4")
    with pytest.raises(CompensationRequired) as caught:
        get_national_registry().create_identity(context=crown, identity_type="PERSON", label="مُعوَّضٌ")
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
    monkeypatch.setattr(authorizer, "guard_declared", original_guard)

    assert caught.value.outcome.state_is_clean is True
    assert caught.value.outcome.requires_human is False
    assert _count(IdentityModel) == 0
    # السجلُّ الإضافيُّ يشهدُ: فاشلةٌ قابلةٌ للإعادةِ — لا ناجحةً كاذبةً
    assert captured["key"] is not None, "لم يُلتقطْ مفتاحُ العمليّةِ الفاشلةِ"
    record = ledger.get(captured["key"])
    assert record is not None, "السجلُّ الإضافيُّ لم يشهدْ العمليّةَ الفاشلةَ"
    assert record.status is OperationStatus.FAILED_RETRYABLE
    assert record.key.scope == "registry.NationalRegistry.create_identity"

    # نداءٌ جديدٌ بعدَ التعويضِ ينجحُ (مفتاحُهُ جديدٌ بمعرّفِ استدعاءٍ — إثباتُ
    # الإعادةِ على المفتاحِ نفسِهِ فيما بعدُ هو T5): البوّابةُ لا تُعاقِبُ من
    # عُوِّضَ أثرُهُ، والمُعوِّضُ لم يتركْ صفًّا يتيمًا
    _next_second()
    identity = get_national_registry().create_identity(
        context=crown, identity_type="PERSON", label="نداءٌ جديدٌ بعدَ التعويضِ"
    )
    assert _count(IdentityModel) == 1
    assert identity["status"] == "active"


# ── T5 · المُعوِّضُ على التحديثِ ─────────────────────────────────────────────


def _assignment_fields(assignment_id: str) -> tuple[Any, Any, Any]:
    """أعمدةُ صفِّ التقليدِ من القاعدةِ — جلسةٌ واحدةٌ تُفتَحُ وتُغلَقُ نفسُها."""
    session = get_session_factory()()
    try:
        row = session.get(OfficialPositionModel, assignment_id)
        assert row is not None
        return (row.status, row.revoked_at, row.revocation_reason)
    finally:
        session.close()


def test_wi107_t5_compensator_restores_revoked_assignment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from core.sovereignty.compensation import CompensationRequired
    from core.sovereignty.idempotency import IdempotencyKey, OperationStatus

    _install_recording_authorizer()
    crown = _crown()
    chain = _chain(crown)
    assignment_id = chain.assignment["id"]
    ledger = national_registry_module._registry_authorizer().boundary.idempotency_ledger
    original = _drop_settle(monkeypatch, ledger, "T5")
    with pytest.raises(CompensationRequired) as caught:
        get_national_registry().revoke_assignment(
            context=crown, assignment_id=assignment_id, reason="قياسُ T5"
        )
    monkeypatch.setattr(type(ledger), "mark_succeeded", original)

    assert caught.value.outcome.state_is_clean is True
    # كلُّ الأعمدةِ التي يُلزمُ المُعوِّضُ استعادتَها (توجيهُ المستشارِ): الحالةُ
    # ووقتُ العزلِ وسببهُ — لا الحالةَ وحدها. والجلسةُ تُفتَحُ وتُغلَقُ نفسُها
    assert _assignment_fields(assignment_id) == ("active", None, ""), "المُعوِّضُ لم يُرجِعْ الصفَّ كما كان"
    record = ledger.get(
        IdempotencyKey(
            scope="registry.NationalRegistry.revoke_assignment",
            value=f"assignments/{assignment_id}/revoke",
        )
    )
    assert record is not None and record.status is OperationStatus.FAILED_RETRYABLE

    _next_second()
    revoked = get_national_registry().revoke_assignment(
        context=crown, assignment_id=assignment_id, reason="قياسُ T5"
    )
    assert revoked["changed"] is True
    status, revoked_at, revocation_reason = _assignment_fields(assignment_id)
    assert status == "revoked"
    assert revoked_at is not None
    assert revocation_reason == "قياسُ T5"


# ── T6 · الإعادةُ الطبيعيّةُ مرفوعةٌ صريحةً ─────────────────────────────────


def test_wi107_t6_second_link_is_refused_without_second_write() -> None:
    authorizer = _install_recording_authorizer()
    crown = _crown()
    national = get_national_registry()
    identity = national.create_identity(context=crown, identity_type="PERSON", label="ربطٌ واحدٌ")
    principal_id = f"pid-wi107-{uuid.uuid4().hex[:8]}"
    first = national.link_principal(
        context=crown, principal_id=principal_id, identity_id=identity["id"]
    )
    assert first["created"] is True
    link_id = first["id"]
    links_before = _count(IdentityPrincipalModel)
    crossings_before = len(authorizer.crossings)

    # (أ) الربطُ القائمُ نفسُهُ يُرجِعُ الردَّ الخاملَ **قبلَ العبورِ** (D5)
    second = national.link_principal(
        context=crown, principal_id=principal_id, identity_id=identity["id"]
    )
    assert second["created"] is False
    assert second["id"] == link_id
    assert _count(IdentityPrincipalModel) == links_before
    assert len(authorizer.crossings) == crossings_before, "الردُّ الخاملُ عبرَ الحدَّ"

    # (ب) على مستوى الحدِّ: مفتاحٌ طبيعيٌّ مُعادٌ ⇒ إعادةٌ تُرفَعُ صريحةً (D6)
    undo = national_registry_module._RegistryUndo()
    target, crossing = national_registry_module._crossing(
        "NationalRegistry.link_principal",
        "CREATE",
        f"principals/{DEFAULT_TENANT}/{principal_id}/link",
        "قياسُ الإعادةِ على مستوى الحدِّ",
        undo,
    )
    guarded = authorizer.guard_declared(
        national_registry_module.REGISTRY_VERB, target, applier=lambda _effect: {}, **crossing
    )
    assert guarded.is_replay
    with pytest.raises(RegistryReplayError):
        national_registry_module._refuse_replay(guarded, "NationalRegistry.link_principal", target)

    # (ج) الاسمُ نفسُهُ في مستأجرينِ مختلفَينِ ليسَ إعادةً (تصحيحٌ مؤرَّخٌ W-625:
    # قيدُ القاعدةِ `UNIQUE (tenant_id, principal_id)` فالمفتاحُ الطبيعيُّ يشملُ
    # المستأجرَ — ولو لم يشملْهُ لحَجَبَ سجلُّ الذرّيّةِ الربطَ الثانيَ ظلمًا)
    tenant_a = _crown()
    tenant_b = _context("king", tenant_id=f"tenant-wi107-{uuid.uuid4().hex[:8]}")
    identity_b = national.create_identity(
        context=tenant_b, identity_type="PERSON", label="هويةُ المستأجرِ الثاني"
    )
    shared_name = f"shared-{uuid.uuid4().hex[:8]}"
    first = national.link_principal(
        context=tenant_a, principal_id=shared_name, identity_id=identity["id"]
    )
    second = national.link_principal(
        context=tenant_b, principal_id=shared_name, identity_id=identity_b["id"]
    )
    assert first["created"] is True
    assert second["created"] is True, "ربطُ الاسمِ نفسِهِ في مستأجرٍ آخرَ حُجِبَ كإعادةٍ"


# ── T7 · الجردُ: الوحدةُ بلا دَينٍ ────────────────────────────────────────────

# ── T7 · الجردُ: الوحدةُ بلا دَينٍ ────────────────────────────────────────────


def _repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "tools" / "audit" / "sovereign_write_inventory.py").is_file():
            return parent
    raise AssertionError("جذرُ المستودعِ غيرُ موجود")


def test_wi107_t7_inventory_counts_nine_guarded_and_zero_debt() -> None:
    root = _repo_root()
    tool = root / "tools" / "audit" / "sovereign_write_inventory.py"
    spec = importlib.util.spec_from_file_location("_wi107_inventory", tool)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    sites = [s for s in module.collect(root) if s.path.endswith("national_registry/service.py")]
    public = [s for s in sites if s.public]
    assert {f"{s.owner}.{s.function}" for s in public} == EXPECTED_OPERATIONS
    assert all(s.guarded for s in public), [s.function for s in public if not s.guarded]


# ── T8 · الثابتانِ (D1 · D2) ──────────────────────────────────────────────────


def test_wi107_t8_actor_and_verb_constants() -> None:
    assert national_registry_module.REGISTRY_ACTOR == "EXECUTIVE"
    assert national_registry_module.REGISTRY_VERB == "register"
    assert national_registry_module._registry_authorizer()._actor == "EXECUTIVE"
    assert REGISTRY_ACTOR == "EXECUTIVE"
    assert REGISTRY_VERB == "register"


# ═══════════════════════════════════════════════════════════════════════════
# الأسطحُ القائمةُ لا تُمَسُّ — الاختباراتُ المرافقةُ تُشغَّلُ بلا تعديلٍ (التصميمُ § 3)
# ═══════════════════════════════════════════════════════════════════════════


def test_wi107_existing_r7c_suite_still_collects() -> None:
    """الملفُّ المرافقُ `test_r7c_national_registry.py` يُجمعُ كما هو — لا تعديلَ عليه."""
    path = Path(__file__).parent / "test_r7c_national_registry.py"
    assert path.is_file()
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3221
SHA256: 2933719db9bec04649240508cdd3c31bc0689717839e090a5405a3cfec863363
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 246
  عمليّاتٌ عامّةٌ مُغيِّرة   : 201
  منها تعبرُ الحدَّ        : 42
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 157
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          171 /  42 /  128
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      17  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
      10  federal/executive/services/src/amos_federation/services/federal_state/service.py
       9  federal/executive/services/src/amos_federation/services/governance/treasury.py
       9  federal/executive/services/src/amos_federation/services/royal/main.py
       8  federal/executive/services/src/amos_federation/services/governance/expansion.py
       7  federal/executive/services/src/amos_federation/services/governance/learning_cycle.py
       7  federal/executive/services/src/amos_federation/services/governance/system_life.py
       7  federal/executive/services/src/amos_federation/services/state_treasury/service.py
       5  federal/executive/services/src/amos_federation/services/agent_runtime/health.py
       5  federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
       5  federal/executive/services/src/amos_federation/services/governance/security.py
       5  federal/executive/services/src/amos_federation/services/governance/state_runtime.py
       4  federal/executive/services/src/amos_federation/common/database.py
       3  federal/executive/services/src/amos_federation/services/agent_runtime/population.py
       3  federal/executive/services/src/amos_federation/services/executive_core/repository.py
       2  federal/executive/services/src/amos_federation/common/durable_event_bus.py
       2  federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
       2  federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py
       2  federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py
       2  federal/executive/services/src/amos_federation/services/training/persistent_registry.py
       1  federal/executive/services/src/amos_federation/common/event_bus.py
       1  federal/executive/services/src/amos_federation/common/events.py
       1  federal/executive/services/src/amos_federation/services/api_gateway/store.py
       1  federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py
       1  federal/executive/services/src/amos_federation/services/government_services/service.py
       1  tools/migrations/r4_unify_agent_identity.py
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi107_national_registry_register_sovereign.py -q
EXIT: 0
BYTES: 624
SHA256: 6b3c5de91f6c8912e3bd126114e3b6d28389d051e112cc72fe3eae4809c50b52
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 9 items

tests/test_wi107_national_registry_register_sovereign.py .........       [100%]

============================== 9 passed in 5.60s ===============================
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_r7c_national_registry.py -q
EXIT: 0
BYTES: 625
SHA256: d688f185162e8a7eba9b6a540ef6e812221d1c8a99409c65967a114c2751af69
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 35 items

tests/test_r7c_national_registry.py ...................................  [100%]

============================== 35 passed in 3.90s ==============================
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_2b_state_registry_sovereign.py -q
EXIT: 0
BYTES: 705
SHA256: 65d16a107aeef5c0ac9785584f0a0278aebb6d0829d3dc2b87e46a27d811e96a
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 53 items

tests/test_2b_state_registry_sovereign.py .............................. [ 56%]
.......................                                                  [100%]

============================== 53 passed in 1.94s ==============================
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests -q
EXIT: 0
BYTES: 8980
SHA256: 7ccde314ad99e06708f03275f6fe7ef07c744769837ab8f40c256dab4fd5af1f
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1555 items

tests/test_1n_boundary_integration.py ..........                         [  0%]
tests/test_2a_precedent_correction.py ...........                        [  1%]
tests/test_2a_sovereign_runtime_integration.py .............             [  2%]
tests/test_2b_government_services_sovereign.py ......................... [  3%]
..............                                                           [  4%]
tests/test_2b_state_registry_sovereign.py .............................. [  6%]
.......................                                                  [  8%]
tests/test_agent_runtime.py ......                                       [  8%]
tests/test_api_gateway.py ...                                            [  8%]
tests/test_audit_canonical_record.py ..................                  [  9%]
tests/test_auth.py ...                                                   [ 10%]
tests/test_benchmark.py ..........                                       [ 10%]
tests/test_common_branches.py .......................................... [ 13%]
.....                                                                    [ 13%]
tests/test_config.py ...                                                 [ 13%]
tests/test_control_console.py .........................                  [ 15%]
tests/test_critic.py ...........                                         [ 16%]
tests/test_durable_bus_branches.py ...........                           [ 16%]
tests/test_e2e.py ...                                                    [ 17%]
tests/test_edge_branches.py .........                                    [ 17%]
tests/test_event_bus.py ..............                                   [ 18%]
tests/test_event_schemas.py .....                                        [ 18%]
tests/test_executive_core.py ..............................              [ 20%]
tests/test_expansion.py .....................................            [ 23%]
tests/test_experience.py ...........                                     [ 23%]
tests/test_federation.py ...........................................     [ 26%]
tests/test_governance.py ...........................                     [ 28%]
tests/test_governance_phase3.py .........................                [ 30%]
tests/test_hash_chain.py ......                                          [ 30%]
tests/test_health.py ..............                                      [ 31%]
tests/test_health_system.py ................................             [ 33%]
tests/test_inmemory_stores.py ................................           [ 35%]
tests/test_king_login_boundary.py ......................                 [ 36%]
tests/test_memory_service.py ........                                    [ 37%]
tests/test_model_gateway.py ....                                         [ 37%]
tests/test_model_layer.py ..............                                 [ 38%]
tests/test_models.py ...                                                 [ 38%]
tests/test_orchestrator.py .......                                       [ 39%]
tests/test_p13_factories_sovereign.py ......................             [ 40%]
tests/test_persistence.py ........                                       [ 41%]
tests/test_phase12_states.py .................                           [ 42%]
tests/test_phase13_factories.py .............                            [ 43%]
tests/test_phase14_15_learning.py ..............                         [ 43%]
tests/test_phase16_security.py ................                          [ 44%]
tests/test_phase17_system_life.py ............                           [ 45%]
tests/test_phase1_postgres.py ssssssss                                   [ 46%]
tests/test_phase1_postgres_events.py sssssssssssssssss                   [ 47%]
tests/test_phase2_events.py ...........................                  [ 49%]
tests/test_phase3_governance.py ........................                 [ 50%]
tests/test_phase4_tools.py ..................                            [ 51%]
tests/test_phase5_models.py ...........                                  [ 52%]
tests/test_phase6_population.py ...............                          [ 53%]
tests/test_phase7_health.py .........                                    [ 54%]
tests/test_population.py ..................                              [ 55%]
tests/test_q19_money_delegation.py ............................          [ 56%]
tests/test_q20_money_representation.py .......ss..................       [ 58%]
tests/test_q31_money_engine_wiring.py ............                       [ 59%]
tests/test_q32_money_enforcement_surface.py ...............              [ 60%]
tests/test_r1_canonical_execution_path.py .................              [ 61%]
tests/test_r2_task_execution_integration.py .........................    [ 63%]
tests/test_r3_agent_runtime_integration.py .............                 [ 63%]
tests/test_r4_agent_identity_and_population.py ................          [ 65%]
tests/test_r5_multi_provider_sandbox.py ...................              [ 66%]
tests/test_r6_1_authorization_closure.py ..................              [ 67%]
tests/test_r6_identity_authorization_root.py .................           [ 68%]
tests/test_r7_government_services.py ................................    [ 70%]
tests/test_r7_state_registry.py ..........................               [ 72%]
tests/test_r7b_state_treasury.py ....................................    [ 74%]
tests/test_r7c_national_registry.py ...................................  [ 76%]
tests/test_r7d_federal_judiciary.py ...........................          [ 78%]
tests/test_r8_federal_state_integration.py ............................. [ 80%]
....                                                                     [ 80%]
tests/test_r9_national_economic_state.py ............................... [ 82%]
..............                                                           [ 83%]
tests/test_real_tools.py ....................                            [ 84%]
tests/test_shadow.py ..........                                          [ 85%]
tests/test_step19_durable_governance_state.py ........                   [ 85%]
tests/test_step7_gate_denial.py .....                                    [ 86%]
tests/test_tool_registry.py .......                                      [ 86%]
tests/test_training.py ...............                                   [ 87%]
tests/test_treasury.py ................................                  [ 89%]
tests/test_w032_registry_ownership.py .............                      [ 90%]
tests/test_w033_cost_record_durability.py .........                      [ 91%]
tests/test_w036_cost_precision.py ...........                            [ 91%]
tests/test_w166_postgres_driver_declared.py ................             [ 92%]
tests/test_w190_durable_model_registry.py ..                             [ 93%]
tests/test_w308_test_ledger_is_per_session.py ...                        [ 93%]
tests/test_wi062_migrations_cover_orm_tables.py ..s                      [ 93%]
tests/test_wi063_tenant_isolation_http.py ..ss..ss.s..ss.s.s.s..s.s.     [ 95%]
tests/test_wi064_migrations_follow_orm.py .s                             [ 95%]
tests/test_wi065_orm_declares_jsonb_timestamptz.py ..s                   [ 95%]
tests/test_wi066_convert_create_all_databases.py .sssss                  [ 95%]
tests/test_wi066_pg_session_isolation.py .ss                             [ 96%]
tests/test_wi067_legal_search_isolated.py .......................        [ 97%]
tests/test_wi076_pg_backup_restore.py ssss                               [ 97%]
tests/test_wi082_agent_identity_sovereign.py ........                    [ 98%]
tests/test_wi105_issue_ruling_sovereign.py ..........                    [ 98%]
tests/test_wi106_federation_coordinate_sovereign.py ........             [ 99%]
tests/test_wi107_national_registry_register_sovereign.py .........       [100%]

=============================== warnings summary ===============================
../../../.venv/lib/python3.12/site-packages/fastapi/testclient.py:1
  /home/user/workspace/council_w628/kimi_k3/repo/.venv/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========== 1502 passed, 53 skipped, 1 warning in 318.79s (0:05:18) ============
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/R1_NATIONAL_REGISTRY_REGISTER_DESIGN.md
EXIT: 0
BYTES: 21114
SHA256: 66d4d2d82e0735124566678c0eeb09ce14543d676bd97b51e624cebd9c350d60
NO_EOL: 0
--- OUTPUT ---
# ملحقُ تصميمِ الدفعةِ R1 — أسطحُ `national_registry/service.py` التسعةُ تعبرُ الحدَّ بفاعلٍ تنفيذيٍّ مُعلَنٍ بالفعلِ `register`

## التعريف
ملحقُ تصميمٍ قصيرٌ للدفعةِ **R1** (بندُ `WI-107`) يُودَعُ **في التزامٍ مستقلٍّ يسبقُ أيَّ شِفرةٍ** (قرارُ المالكِ Q-61 · نمطُ «تُعرَضُ قبلَ الشِّفرةِ») وبتوجيهِ المستشارِ 20 § 2 («ملحقُ تصميمٍ قصيرٍ يسبقُ الشِّفرةَ، ثمَّ الشِّفرةُ بفحوصِها وطفراتِها. نفسُ نمطِ F1»). يحدِّدُ نقاطَ التصميمِ D1–D8 والأرقامَ المتوقَّعةَ قبلَ الكتابةِ والفحوصَ والطفراتِ، على نمطِ F1 ([`F1_FEDERATION_COORDINATE_DESIGN.md`](F1_FEDERATION_COORDINATE_DESIGN.md)) وJ1 ([`J1_ISSUE_RULING_DESIGN.md`](J1_ISSUE_RULING_DESIGN.md)).

## النطاق
`federal/executive/services/src/amos_federation/services/national_registry/service.py` وحدَه في الإنتاجِ · وملفُّ الفحوصِ `federal/executive/services/tests/test_wi107_national_registry_register_sovereign.py`. لا يمسُّ `models.py` ولا `authorization.py` ولا `core/` ولا `royal/` (K1 لا يُمَسُّ) ولا `resolver.py`.

## المالك
Perplexity Computer (المنسِّقُ الحاضرُ GLM-5.3 — منسِّقٌ لا مُصوِّتٌ · بتوجيهِ المستشارِ 20 § 2) — بندُ `WI-107`.

## تاريخ الإنشاء
2026-10-23

## تاريخ آخر تعديل
2026-10-23 (تصحيحاتٌ مؤرَّخةٌ في § 7 — دفعةُ W-625)

---

## 0. السندُ (لا اختراعَ)

- **قرارُ المالكِ D17-3** (نصُّهُ في [السجلِّ السياديِّ](SOVEREIGN_DECISION_REGISTER.md)): «خيار (1) الآن → يفتح R1 ثم بقية الموجة W1.»
- **خطّةُ حرقِ D-4** ([`HANDOFFS/D4-BURN-PLAN.md`](governance/work/HANDOFFS/D4-BURN-PLAN.md) صفُّ R1): السجلُّ الوطنيُّ · 9 أسطحٍ · **نمطٌ واحدٌ آليٌّ بعدَ قرارِه** («F1 · A1 · R1 تنتظرُ ثلاثةَ قراراتٍ صغيرةً لا اثنينِ وخمسين»).
- **توجيهُ المستشارِ 20 § 2**: «R1 (السجلُّ الوطنيُّ · 9 أسطحٍ · D17-3 محسومٌ): ملحقُ تصميمٍ قصيرٍ يسبقُ الشِّفرةَ، ثمَّ الشِّفرةُ بفحوصِها وطفراتِها. نفسُ نمطِ F1» — و§ 3: «لا شِفرةَ قبلَ التزامِ التصميمِ».
- **قياسُ ما قبلُ** (`evidence/W-622/`): D-4 = 166 · sovereign = 33 · المواضعُ 236 (`inventory_before_wi107.json`) — أسطحُ الوحدةِ التسعةُ دَينٌ كلُّها.
- **حيادُ الفعلِ `register` مقيسًا** (`evidence/W-622/session_measurements.txt` البندُ 4): ليسَ في الاختصاصِ الملكيِّ الحصريِّ (20 اسمًا · فيه `grant_authority` و`revoke_authority`) ولا في أفعالِ التآكلِ (16 اسمًا). **واسمَا `grant_authority`/`revoke_authority` يبقيانِ محجوبَينِ للاسمِ في البوابةِ**: العبورُ بفعلِ الوحدةِ `register` لا يعترفُ بالاسمَينِ الملكيَّينِ أفعالًا للعبورِ، فحجبُ الاسمِ كاملٌ كما هو — والسجلُّ يُقيِّدُ مِنحةً إداريًّا لا يمنحُ سلطةً ملكيًّا.
- **مسبارُ البوابةِ على `register`** (`evidence/W-623/probe_register_actors.out.txt` · نمطُ مسبارِ F1): `EXECUTIVE` ALLOW (FEDERAL) · والفعلُ محايدٌ يسمحُ لكلِّ الفروعِ الفدراليّةِ — والفاعلُ **ثابتُ وحدةٍ لا اختيارُ المُنادي** (D1) فلا يُفتحُ للفروعِ الأخرى مسارٌ عبرَ هذه الوحدةِ.

## 1. الأسطحُ التسعةُ (مقيسةً · `sovereign_write_inventory.py` · `inventory_before_wi107.json`)

| السطح | الأثرُ المُعلَن | الهدفُ (= قيمةُ المفتاحِ) | المفتاحُ |
|---|---|---|---|
| `create_identity` | CREATE | `registry/identities/{identity_id}/create` | بمعرِّفِ الصفِّ المولَّدِ (`idn-…`) |
| `set_identity_status` | UPDATE | `registry/identities/{identity_id}/status/{row_rev}` | بمعرِّفِ استدعاءٍ (`_nonce()`) |
| `link_principal` | CREATE | `registry/principals/{principal_id}/link` | طبيعيٌّ على `principal_id` |
| `link_agent` | CREATE | `registry/agents/{agent_id}/link` | طبيعيٌّ على `agent_id` |
| `create_position` | CREATE | `registry/positions/{position_id}/create` | بمعرِّفِ الصفِّ المولَّدِ (`pos-…`) |
| `assign_position` | CREATE | `registry/assignments/{assignment_id}/assign` | بمعرِّفِ الصفِّ المولَّدِ (`opos-…`) |
| `revoke_assignment` | UPDATE | `registry/assignments/{assignment_id}/revoke` | طبيعيٌّ على `assignment_id` |
| `grant_authority` | CREATE | `registry/grants/{grant_id}/grant` | بمعرِّفِ الصفِّ المولَّدِ (`agr-…`) |
| `revoke_authority` | UPDATE | `registry/grants/{grant_id}/revoke` | طبيعيٌّ على `grant_id` |

## 2. نقاطُ التصميم

**D1 · الفاعلُ:** ثابتُ وحدةٍ `REGISTRY_ACTOR = "EXECUTIVE"` ومُفوِّضٌ كسولٌ واحدٌ `_registry_authorizer()` (+ `reset_registry_authorizer()` للفحوصِ) — نمطُ `federation.FEDERATION_ACTOR` نفسُه (F1 · D1 · سابقةُ `rulings.JUDICIARY_ACTOR`). لا معامَلَ `authorizer` في توقيعاتِ الأسطحِ (لا تغييرَ في واجهتِها).

**D2 · الفعلُ:** `REGISTRY_VERB = "register"` للأسطحِ التسعةِ كلِّها. اسمُ العمليّةِ يُحمَلُ في `metadata["operation"]` (`"NationalRegistry.<method>"`) وفي نطاقِ المفتاحِ (`registry.<op>`) — لا يُخترَعُ فعلٌ لكلِّ سطحٍ (ذلك سؤالُ Q-2 المعلَّقُ). وحيادُ الفعلِ مقيسٌ في § 0، وحجبُ الاسمَينِ الملكيَّينِ (`grant_authority`/`revoke_authority`) باقٍ لأنَّ العبورَ بالفعلِ `register` لا بالاسمَينِ.

**D3 · الهدفُ والمفتاحُ:** الهدفُ بالجدولِ أعلاه، والمفتاحُ `operation_key("registry.<op>", <لاحقةِ الهدفِ>)` — الهويّةُ نفسُها في الاثنينِ (نمطُ F1 D3 · J1 D5/D6). بصمةُ العقدِ تُشتقُّ من (الفاعلِ · الفعلِ · الهدفِ · الآثارِ) ومعرِّفُ الإذنِ `EP-<العقد>-<الثانية>` يرفضُ عقدًا مكرَّرًا في الثانيةِ نفسِها، فالمفتاحُ يحملُ ما يُمايزُ الاستدعاءَ: **طبيعيٌّ** حيثُ لا يتكرّرُ الفعلُ مشروعًا على الكيانِ (الربطُ لمبدأٍ/وكيلٍ · سحبُ تقليدٍ/منحةٍ — لكلٍّ مرةً واحدةَ كتابةٍ) و**بمعرِّفِ استدعاءٍ** حيثُ يُشرَعُ التكرارُ (إنشاءُ هويةٍ/منصبٍ · تقليدٌ بعدَ عزلٍ سابقٍ · منحةٌ ثانيةٌ · تغييرُ حالةٍ متعاقبٌ) — فلا يتغيّرُ سلوكُ اليومِ.

**D4 · موضعُ العبورِ:** في **جسدِ كلِّ سطحٍ عامٍّ** (`guard_declared(` نصًّا فيه — قاعدةُ الجردِ)، والكتابةُ كلُّها في **مُطبِّقٍ متداخلٍ خاصٍّ** `_apply` لكلِّ سطحٍ يفتحُ الجلسةَ ويكتبُ ويلتزمُ (نمطُ F1 D4 · J1). لا كتابةَ خارجَ المُطبِّقِ في أيِّ سطحٍ.

**D5 · التحقُّقُ قبلَ العبورِ:** `require_domain_permission` وفحوصُ المُدخَلِ (أخطاءُ `ValueError` الراهنةُ) وفحوصُ الحالةِ القائمةِ تُنفَّذُ **قبلَ العبورِ** بجلسةِ قراءةٍ، ولا تتغيّرُ رسائلُها ولا أنواعُها — فلا يتحوّلُ رفضُ مُدخَلٍ إلى `CompensationRequired` ولا يُسجَّلُ في الذرّيّةِ عمليّةً فاشلةً. ومساراتُ «السكوتِ المرتجعِ» الراهنةُ تُحافَظُ كما هي قبلَ العبورِ: `link_principal`/`link_agent` على ربطٍ قائمٍ نفسِهِ يُعيدانِ `created: False` بلا عبورٍ · `revoke_assignment`/`revoke_authority` على صفٍّ مسحوبٍ سابقًا يُعيدانِ `changed: False` بلا عبورٍ · والتعارضُ (`IdentityConflictError` · `DuplicateAssignmentError` · …) يُرفَعُ قبلَ العبورِ بنوعِهِ. ويُعيدُ المُطبِّقُ تحميلَ الصفِّ داخلَ معاملتِهِ.

**D6 · الإعادةُ:** المفتاحُ الطبيعيُّ للأربعةِ الساكنةِ (الربطانِ · السحبانِ) لا تبلغُهُ الإعادةُ عبرَ الواجهةِ العامةِ لأنَّ فحصَ D5 المسبقَ يُرجِعُ الردَّ الخاملَ قبلَ العبورِ — فدفاعُ الإعادةِ على المفتاحِ الطبيعيِّ يُختبرُ على مستوى الحدِّ مباشرةً (T6) ويُرفَعُ `RegistryReplayError` صريحًا إن بلغَهُ استدعاءٌ (سباقُ لحظةٍ لا مسارًا عامًّا). والمفتاحُ بمعرِّفِ استدعاءٍ للخمسةِ المتكرِّرةِ مشروعًا (الجدولُ) فلا إعادةَ لهُ أصلًا. **لا تغييرَ في سلوكِ اليومِ.**

**D7 · المُعوِّضُ (نمطُ F1 D7 · J1 D7-أ):** استعادةٌ تقنيّةٌ دقيقةٌ في جلسةٍ جديدةٍ عبرَ سجلِّ تراجعٍ لكلِّ عبورٍ `_RegistryUndo`: المُطبِّقُ يُسجِّلُ قبلَ الكتابةِ (أ) كلَّ صفٍّ أنشأَهُ (`created(model, row)`) و(ب) القيمَ السابقةَ لكلِّ عمودٍ يغيّرُهُ (`prior(row, *columns)` — `status` · `status_reason` · `updated_at` · `revoked_at` · `revocation_reason`). ومُعوِّضُ الأثرِ يحذفُ المُنشَأَ ويُعيدُ السابقَ ويلتزمُ. الحدُّ يُنادي المُعوِّضَ آليًّا عندَ فشلِ تثبيتِ النجاحِ بعدَ الالتزامِ (قرارُ المالكِ Q-70) — «الحذفُ شأنٌ تنفيذيٌّ» والمُعوِّضُ ليس أثرًا مُعلَنًا.

**D8 · ما يبقى خارجَ العبورِ (مُعلَنٌ لا مسكوتٌ عنه):**
(أ) **الأثرُ الإجرائيُّ بعدَ الالتزامِ**: `self._record` (سجلُّ التتبّعِ الدائمُ `record_domain_trace` + ناقلُ الأحداثِ) يبقى بعدَ العبورِ كما هو اليومَ — أثرُ بنيةٍ تحتيةٍ، سؤالُ A1 المعلَّقُ (سابقةُ F1 D8-أ).
(ب) **تداخلُ `link_agent` مع `create_identity`**: عندَ `identity_id=None` ينادي `link_agent` السطحَ العامَّ `self.create_identity` — فيعبُرُ كلُّ سطحٍ بعبورِهِ المستقلِّ (عمليّتانِ مُسجَّلتانِ في الذرّيّةِ)، لا التفافٌ عبرَ خاصٍّ.
(ج) القراءاتُ (`get_identity_of_principal` · `list_positions` · `list_grants` · `authority_chain` · `registry_health` · `positions_of_identity`) لا تكتبُ فلا تعبرُ.
(د) `models.py` و`authorization.py` و`resolver.py` و`Ed25519Signer` (Q-37) لا تُمَسُّ.

## 3. الأرقامُ المتوقَّعةُ (مكتوبةٌ قبلَ الشِّفرةِ · بالأداةِ نفسِها)

- **الدَّينُ (D-4):** 166 ← **157** (التسعةُ تعبرُ).
- **السياديُّ:** 33 ← **42**.
- **الأسطحُ (المواضعُ):** 236 ← **246** متوقَّعًا — كلُّ مُطبِّقٍ متداخلٍ خاصٍّ يُحصى موضعًا مستقلًّا (سابقةُ DISC-126 في J1/WI-082/F1) فيزيدُ 9، ومُعوِّضُ `_RegistryUndo._restore` موضعٌ خاصٌّ واحدٌ (+1). ليست دَينًا (الدَّينُ عامٌّ غيرُ عابرٍ وحدَه). **إن خالفَ المقيسُ هذا الرقمَ أُعلِنَ الفرقُ بسببِهِ ولا يُعدَّلُ المتوقَّعُ بأثرٍ رجعيٍّ.**
- **بلا نموٍّ في غيرِ الوحدةِ:** دَينُ كلِّ ملفٍّ آخرَ كما هو.

## 4. الفحوصُ (`test_wi107_national_registry_register_sovereign.py`)

- **T1 · العبورُ:** مُصرِّحٌ مُسجِّلٌ بالثابتِ نفسِهِ؛ استدعاءُ الأسطحِ التسعةِ كلِّها ⇒ 9 عمليّاتٍ متمايزةً في `metadata["operation"]`، الفعلُ `register` في كلِّها، والقرارُ ALLOW.
- **T2 · الفاعلُ مُعلَنٌ لا مُثبَّتٌ:** تبديلُ `REGISTRY_ACTOR` إلى `JUDICIAL` ⇒ `create_identity` و`link_principal` يُرفَضانِ في البوابةِ ولا صفَّ يُكتَبُ.
- **T3 · لا كتابةَ خارجَ المُطبِّقِ:** مُصرِّحٌ يرفضُ قبلَ المُطبِّقِ ⇒ لكلِّ سطحٍ: الصفوفُ والأعمدةُ كما كانت.
- **T4 · المُعوِّضُ على الإنشاءِ (`create_identity`):** إسقاطُ تثبيتِ النجاحِ ⇒ `CompensationRequired` · `state_is_clean` · الصفُّ غائبٌ · الذرّيّةُ `FAILED_RETRYABLE` · والإعادةُ (الثانيةُ التاليةُ) تنجحُ.
- **T5 · المُعوِّضُ على التحديثِ (`revoke_assignment`):** الإسقاطُ نفسُهُ ⇒ الحالةُ والسببُ والمسحوبُ فيُعادانِ إلى ما قبلُ.
- **T6 · الإعادةُ:** (أ) عبرَ الواجهةِ: الاستدعاءُ الثاني لـ`link_principal` على الربطِ نفسِهِ ⇒ `created: False` ولا عمليّةً ثانيةً في الذرّيّةِ (سلوكُ اليومِ) · (ب) على مستوى الحدِّ مباشرةً: `guard_declared` بمفتاحٍ طبيعيٍّ مكرَّرٍ ⇒ `is_replay` ويُرفَعُ `RegistryReplayError` صريحًا بلا كتابةٍ ثانيةٍ.
- **T7 · الجردُ:** الأداةُ على الوحدةِ ⇒ 9 عامًّا كلُّها عابرةٌ (0 دَينٍ).
- **T8 · ثوابتُ D1/D2:** الفاعلُ الافتراضيُّ `EXECUTIVE` والفعلُ `register`.
- **بلا تعديلٍ:** `test_r7c_national_registry.py` و`test_2b_state_registry_sovereign.py` كاملَينِ.

## 5. الطفراتُ (كلٌّ يجبُ أن يُسقِطَ فحصَه)

- **M1:** `create_identity` يُنادي `_apply` مباشرةً بلا عبورٍ ⇒ يسقطُ T1 وT3.
- **M2:** `REGISTRY_ACTOR = "JUDICIAL"` ⇒ يسقطُ T1 وT8.
- **M3:** مُعوِّضُ `_RegistryUndo._restore` لا يفعلُ شيئًا ⇒ يسقطُ T4 وT5.
- **M4:** حذفُ `undo.prior(...)` من `revoke_assignment` ⇒ يسقطُ T5.
- **M5:** حذفُ الفحصِ المسبقِ (D5) من `link_principal` فيبلُغُ الاستدعاءُ الثاني الحدَّ بمفتاحٍ طبيعيٍّ ⇒ إعادةٌ تُرفَعُ بدلَ `created: False` ⇒ يسقطُ T6.

## 6. ما لا يُنجَزُ في R1 ولماذا

نشرُ الأحداثِ بعدَ الالتزامِ (A1 · D8-أ) بقرارِ المالكِ · والتعديلُ على جداولِ النماذجِ أو `authorization.py` خارجَ البندِ · وW1 وبقيةُ الموجةِ دفعاتٌ تاليةٌ بأبندتِها. وورقةُ القراراتِ الكاملةُ (توجيهُ 19 § 3 · Q-2/Q-16/Q-9/Q-8/Q-13/Q-14/Q-26/Q-32) تُقدَّمُ قبلَ أيِّ دفعةٍ بعدَ R1 (توجيهُ 20 § 2).

## 7. تصحيحاتٌ مؤرَّخةٌ (كُتِبَت مع شفرةِ W-625 — لا دفعاتِ تصحيحٍ لما فرقُهُ الشفريُّ فارغٌ)

**تصحيحٌ 1 · نوعُ الأثرِ (§ 1 الجدولُ):** الجدولُ فوقَ يذكرُ `UPDATE` لأسطحِ التحديثِ الثلاثةِ، ومفردةُ `EffectKind` في الجسرِ لا تحملُ `UPDATE` أصلًا — أنواعُها `READ/CREATE/WRITE/DELETE/TRANSFER/EXTERNAL`. فالشِّفرةُ تعلَمُ `WRITE`، وهو ما يعنيهِ الجدولُ (تحديثُ صفٍّ قائمٍ)، ولا تغييرَ في الدلالةِ.

**تصحيحٌ 2 · آليّةُ رفضِ T2 (§ 4):** افتراضُ T2 الأصليُّ («تبديلُ `REGISTRY_ACTOR` إلى `JUDICIAL` ⇒ رفضٌ») مقتبسٌ من F1 حيثُ `coordinate` فعلٌ حصريٌّ. لكنّ مسبارَ W-623 نفسِهِ (`evidence/W-623/probe_register_actors.out.txt` — دليلُ هذه الدفعةِ) أثبتَ أنّ `register` **مُنطَّقٌ** لا حصريٌّ: ALLOW لكلِّ الفاعلينِ الستةِ. فتبديلُ الفاعلِ لا يُنتجُ رفضًا، والمقيسُ في T2 صارَ جوهرَ D1 نفسِهِ: الفاعلُ المُعلَنُ في الوحدةِ يسري على سجلِّ البوابةِ (تبديلٌ إلى `LEGISLATIVE` فوقَ الاختبارِ فيُقرأُ في السجلِّ). والرفضُ الحقيقيُّ («لا كتابةَ عندَ الرفضِ» — T3) صارَ بنمطِ 2B المُقرَّرِ: حكمُ DENY حقيقيٌّ من المحرِّكِ الدستوريِّ نفسِهِ (فعلٌ حصريٌّ لفاعلٍ لا يملكُه) يُحاكى في `gateway.decide` — وهو ما فعلهُ سلفُ هذه الدفعةِ في `test_2b_state_registry_sovereign.py` حينَ واجهَ المسألةَ نفسَها. ولا يُدَّعى هنا أنّ الدستورَ يرفضُ `register` لفاعلٍ ما — لم يعدْ ذلكَ مقيسًا ولا مُدَّعًى.

**تصحيحٌ 3 · مفتاحُ `link_principal` (§ 1 الجدولُ · D3):** الجدولُ فوقَ يذكرُ المفتاحَ الطبيعيَّ على `principal_id` وحده. قيدُ القاعدةِ `UNIQUE (tenant_id, principal_id)` — فالاسمُ نفسُهُ جائزٌ في مستأجرينِ مختلفَينِ. فالهدفُ صارَ `registry/principals/{tenant}/{principal_id}/link` — يُضمُّ المستأجرُ كما في هدفِ 2B `institutions/{tenant}/{code}` — لولاهُ لحَجَبَ سجلُّ الذرّيّةِ ربطَ الاسمِ نفسِهِ في المستأجرِ الثاني كإعادةٍ. وفحصٌ (T6-ج) أُضيفَ يُثبتُ أنّ الربطَ الثانيَ ليسَ إعادةً. وربطُ الوكيلِ لم يتغيّر: قيدُهُ `UNIQUE (agent_id)` عالميٌّ.

**تصحيحٌ 4 · عزلُ سجلِّ الذرّيّةِ في الفحوصِ (§ 4):** سجلُّ الذرّيّةِ ملفٌّ ثابتٌ (`.runtime/sovereignty/…`) والمفاتيحُ الطبيعيّةُ تتراكمُ بينَ الفحوصِ والجولاتِ. فالملفُّ الجديدُ يوجّهُ `AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER` إلى ملفٍّ مؤقتٍ لكلِّ فحصٍ — عزلٌ كاملٌ لا مسحُ ملفِّ التشغيلِ (توجيهُ المستشارِ في مراجعةِ W-625).

**تصحيحٌ 5 · عزلُ سجلِّ الذرّيّةِ على مستوى الحزمةِ (conftest.py · قرارُ المالكِ Q-71):** تصحيحٌ 4 عزلَ سجلَّ ملفِّ الفحوصِ نفسِهِ بتوجيهِ البيئةِ؛ لكنَّ تجهيزاتِ ملفّاتٍ أخرى (r7d/r8/r9/wi105) تربطُ «crown» بمفتاحٍ طبيعيٍّ والقاعدةُ تُمسَحُ لكلِّ فحصٍ — فقِيسَ في الحزمةِ الكاملةِ 115 خطأَ تهيئةٍ كلُّها سببًا واحدًا (`evidence/W-625/repro_r7d_crown_pair.out.txt`). وبقرارِ المالكِ **Q-71** («أذن بـconftest.py تحت WI-107» · قسمةُ نطاقٍ كسابقةِ Q-45) نُفِّذَ العزلُ في `tests/conftest.py` لكلِّ الحزمةِ: سجلُّ ذرّيّةٍ **جديدٌ سليمُ الترويسةِ** لكلِّ فحصٍ (استبدالٌ بـ`os.replace` لا مسحًا — المسحُ تحتَ مصرِّحٍ حيٍّ يُنشئُ سجلًّا بلا ترويسةٍ فقِيسَ أنَّ فحوصًا تُرفَضُ «سجلٌّ تالفٌ») + `reset_registry_authorizer()` للمصرِّحِ الوطنيِّ وحدَه (توجيهُ المستشارِ: بلا إعادةِ ضبطٍ لبقيّةِ الخدماتِ). الإنتاجُ ومفتاحُ (المستأجر، المبدأ) وسلوكُ رفضِ الإعادةِ لم تتغيّر. والحزمةُ الكاملةُ خضراءُ مقيسةً: 1502 ناجحًا · 53 متخطًّى · exit=0 (`evidence/W-625/services_suite_after_conftest_fix.out.txt`).
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-622/inventory_before_wi107.json docs/audit/evidence/W-625/inventory_after_wi107.json
EXIT: 0
BYTES: 159132
SHA256: a023107eea05e4025bf8cc974baae22c859a29b98cb1c3625298291c7521f4f6
NO_EOL: 1
--- OUTPUT ---
{
 "$comment": "الهدف: جردُ مواضعِ الكتابةِ في المستودعِ وتصنيفُ ما عبرَ الحدَّ السّياديَّ وما لم يعبُر— مُخرَجُ tools/audit/sovereign_write_inventory.py --json. ومنه يُشتَقُّ رقمُ الدَّينِ وحدَه. المادةُ التاسعةُ · 2. ومفتاحُ الموقعِ (‏مسارٌ · مالكٌ · دالّةٌ · رتبةٌ) ولا يحملُ رقمَ سطرٍ: الإحداثيُّ يتحرَّكُ بسطرِ تعليقٍ فيُقادِمُ قياسًا لم يتغيَّرْ سلوكُه (DISC-039).",
 "summary": {
  "write_sites_total": 236,
  "by_area": {
   "core": {
    "public": 1,
    "sovereign": 0,
    "non_sovereign": 0
   },
   "service_common": {
    "public": 28,
    "sovereign": 0,
    "non_sovereign": 28
   },
   "services": {
    "public": 171,
    "sovereign": 33,
    "non_sovereign": 137
   },
   "tools": {
    "public": 1,
    "sovereign": 0,
    "non_sovereign": 1
   }
  },
  "public_write_operations": 201,
  "sovereign_write_operations": 33,
  "closed_legacy_paths": 7,
  "non_sovereign_write_operations": 166,
  "non_sovereign_by_file": {
   "federal/executive/services/src/amos_federation/common/persistent.py": 20,
   "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py": 17,
   "federal/executive/services/src/amos_federation/services/national_economy/service.py": 16,
   "federal/executive/services/src/amos_federation/services/federal_state/service.py": 10,
   "federal/executive/services/src/amos_federation/services/governance/treasury.py": 9,
   "federal/executive/services/src/amos_federation/services/national_registry/service.py": 9,
   "federal/executive/services/src/amos_federation/services/royal/main.py": 9,
   "federal/executive/services/src/amos_federation/services/governance/expansion.py": 8,
   "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py": 7,
   "federal/executive/services/src/amos_federation/services/governance/system_life.py": 7,
   "federal/executive/services/src/amos_federation/services/state_treasury/service.py": 7,
   "federal/executive/services/src/amos_federation/services/agent_runtime/health.py": 5,
   "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py": 5,
   "federal/executive/services/src/amos_federation/services/governance/security.py": 5,
   "federal/executive/services/src/amos_federation/services/governance/state_runtime.py": 5,
   "federal/executive/services/src/amos_federation/common/database.py": 4,
   "federal/executive/services/src/amos_federation/services/agent_runtime/population.py": 3,
   "federal/executive/services/src/amos_federation/services/executive_core/repository.py": 3,
   "federal/executive/services/src/amos_federation/common/durable_event_bus.py": 2,
   "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py": 2,
   "federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py": 2,
   "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py": 2,
   "federal/executive/services/src/amos_federation/services/training/persistent_registry.py": 2,
   "federal/executive/services/src/amos_federation/common/event_bus.py": 1,
   "federal/executive/services/src/amos_federation/common/events.py": 1,
   "federal/executive/services/src/amos_federation/services/api_gateway/store.py": 1,
   "federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py": 1,
   "federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py": 1,
   "federal/executive/services/src/amos_federation/services/government_services/service.py": 1,
   "tools/migrations/r4_unify_agent_identity.py": 1
  }
 },
 "sites": [
  {
   "path": "core/sovereignty/gateways.py",
   "owner": "SubordinateGateway",
   "function": "execute",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/database.py",
   "owner": "-",
   "function": "db_cursor",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/database.py",
   "owner": "-",
   "function": "ensure_added_columns",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/database.py",
   "owner": "-",
   "function": "with_db",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/database.py",
   "owner": "-",
   "function": "wrapper",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/durable_event_bus.py",
   "owner": "DurableEventBus",
   "function": "ack",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/durable_event_bus.py",
   "owner": "DurableEventBus",
   "function": "publish",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/event_bus.py",
   "owner": "EventBus",
   "function": "publish",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/events.py",
   "owner": "EventPublisher",
   "function": "publish",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentAgentStore",
   "function": "register",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentAuditStore",
   "function": "append",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()",
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentCriticStore",
   "function": "review",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentExperienceStore",
   "function": "record",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentMemoryStore",
   "function": "store",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "create",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 1,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 2,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 3,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 4,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 5,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 6,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 7,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "save_gates",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentSystemStateStore",
   "function": "reset",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentSystemStateStore",
   "function": "set_level",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentTaskStore",
   "function": "create",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentTaskStore",
   "function": "update_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentToolStore",
   "function": "_seed_from_yaml",
   "ordinal": 0,
   "public": false,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentToolStore",
   "function": "register",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "HealthChecker",
   "function": "check_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "IsolationSystem",
   "function": "isolate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "IsolationSystem",
   "function": "log_action",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "IsolationSystem",
   "function": "release",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "TreatmentSystem",
   "function": "start_treatment",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/population.py",
   "owner": "AgentSchool",
   "function": "take_step",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/population.py",
   "owner": "PopulationRegistry",
   "function": "register_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/population.py",
   "owner": "PopulationRegistry",
   "function": "update_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/api_gateway/store.py",
   "owner": "DatabaseTaskStore",
   "function": "create",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
   "owner": "-",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
   "owner": "-",
   "function": "register_identity",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_identity_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
   "owner": "-",
   "function": "set_lifecycle_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
   "owner": "-",
   "function": "update_identity",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py",
   "owner": "-",
   "function": "register_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/engine.py",
   "owner": "ExecutiveCore",
   "function": "_erase",
   "ordinal": 0,
   "public": false,
   "writes": [
    "delete()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/engine.py",
   "owner": "ExecutiveCore",
   "function": "submit",
   "ordinal": 0,
   "public": true,
   "writes": [
    "delete()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/repository.py",
   "owner": "ExecutiveTaskRepository",
   "function": "compare_and_set",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/repository.py",
   "owner": "ExecutiveTaskRepository",
   "function": "create",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/repository.py",
   "owner": "ExecutiveTaskRepository",
   "function": "delete",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py",
   "owner": "ConstitutionalAuthorizer",
   "function": "guard",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "add_claim",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "add_party",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "open_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "record_proceeding",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "submit_evidence",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py",
   "owner": "-",
   "function": "record_enforcement",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py",
   "owner": "-",
   "function": "appoint_judge",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py",
   "owner": "-",
   "function": "create_court",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py",
   "owner": "-",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py",
   "owner": "-",
   "function": "issue_ruling",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "add_claim",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "add_party",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "appoint_judge",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "assign_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "close_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "enforce_ruling_via_task",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "enforce_ruling_via_treasury",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "file_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "open_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "open_hearing",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "record_proceeding",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "register_court",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "set_court_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "set_evidence_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "set_judge_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "submit_evidence",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "vacate_ruling",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "bind_institution",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "execute_scoped_disbursement",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_operation"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "execute_scoped_operation",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_operation"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "grant_delegation",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "record_relation",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "register_government",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "revoke_delegation",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "scope_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "scope_service",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "set_government_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "PopulationExpansion",
   "function": "create_batch",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "PopulationExpansion",
   "function": "employ_batch",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "PopulationExpansion",
   "function": "enroll_batch",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "PopulationExpansion",
   "function": "graduate_batch",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "RetirementSystem",
   "function": "retire_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "SpecializationProgram",
   "function": "take_exam",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "University",
   "function": "approve_output",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "University",
   "function": "submit_output",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "_complete_step_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "_init_factory",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "_start_production_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "complete_step",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_complete_step_row",
    "_restore_product_pipeline"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "start_production",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_product_row",
    "_write_product_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "FactoryRegistry",
   "function": "_assign_manager_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "FactoryRegistry",
   "function": "assign_manager",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_set_manager_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ApprovalSystem",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ApprovalSystem",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ApprovalSystem",
   "function": "decide_approval",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ApprovalSystem",
   "function": "request_approval",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ExecutiveBranch",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ExecutiveBranch",
   "function": "_init_roles",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ExecutiveBranch",
   "function": "appoint",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "add_argument",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "file_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "rule",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 3,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 4,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "enact",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "open_debate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "open_voting",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "propose",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "vote",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "fail_gate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "pass_gate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "start_promotion",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "SupremeOversight",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "SupremeOversight",
   "function": "generate_compliance_report",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "_FederationUndo",
   "function": "_restore",
   "ordinal": 0,
   "public": false,
   "writes": [
    "commit()",
    "delete()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "EvaluationSystem",
   "function": "evaluate_model",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "LearningCycle",
   "function": "collect_experiences",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "LearningCycle",
   "function": "complete_training",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "LearningCycle",
   "function": "start_training",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "ModelPromotionCycle",
   "function": "_init_tracks",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "ModelPromotionCycle",
   "function": "promote_beta_to_alpha",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "ModelPromotionCycle",
   "function": "start_canary",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "ModelPromotionCycle",
   "function": "start_shadow",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "RBACSystem",
   "function": "_init_roles",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "RBACSystem",
   "function": "_migrate_session_tenant",
   "ordinal": 0,
   "public": false,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "RBACSystem",
   "function": "create_session",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "RateLimiter",
   "function": "check_rate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "SecretVault",
   "function": "store_secret",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "TLSCertManager",
   "function": "issue_certificate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "TLSCertManager",
   "function": "verify_certificate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "FederalMessageBus",
   "function": "send_message",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "_allocate_budget_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "_init_states",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "allocate_budget",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_add_to_budget"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "assign_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "reactivate_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "register_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "suspend_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "bootstrap",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "create_backup",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "graceful_shutdown",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "health_check",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "launch_checklist",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "restore_backup",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "self_heal",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "allocate_budget",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "charge_model_invoke",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "charge_retraining",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "charge_storage",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "generate_financial_report",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "process_real_costs",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "reward_quality_report",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "reward_successful_training",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "reward_task_completion",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "assign_case",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_assign_case_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "close_case",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_set_case_status_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "decide_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_decision_row",
    "_record_decision_provenance",
    "_set_case_status_row",
    "_write_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "open_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_case_row",
    "_write_case_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "process_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "publish_service",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_service_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "set_service_status",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_set_service_status_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py",
   "owner": "ModelLayer",
   "function": "log_cost",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py",
   "owner": "ModelLayer",
   "function": "set_cached",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "activate_policy",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "authorize_expenditure",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "authorize_procurement",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "authorize_transfer",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "create_program",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "define_indicator",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "execute_economic_decision",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "execute_expenditure",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "execute_transfer",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "issue_policy",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_category",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_public_asset",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_public_entity",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_public_liability",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_revenue_source",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_sector",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "assign_position",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "create_identity",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "create_position",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "grant_authority",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "link_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "link_principal",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "revoke_assignment",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "revoke_authority",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "set_identity_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "approve_promotion",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "close_institution",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "create_decree",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "create_institution",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "dismiss_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "generate_interface",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "request_agent_training",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "request_tool_generation",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "restore_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "_write_institution_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "appoint_official",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_official_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "create_department",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_department_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "register_institution",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_institution_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "revoke_official",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_revoke_official_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "set_institution_status",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_set_institution_status_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "allocate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "create_budget",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "disburse",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_post",
    "_record_transaction_authority"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "establish_treasury",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "open_account",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "post_funding",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_post",
    "_record_transaction_authority"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "reverse_transaction",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_post",
    "_record_transaction_authority"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/training/persistent_registry.py",
   "owner": "PersistentModelRegistry",
   "function": "register",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/training/persistent_registry.py",
   "owner": "PersistentModelRegistry",
   "function": "update_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "tools/migrations/r4_unify_agent_identity.py",
   "owner": "-",
   "function": "emit_sql",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  }
 ]
}{
 "$comment": "الهدف: جردُ مواضعِ الكتابةِ في المستودعِ وتصنيفُ ما عبرَ الحدَّ السّياديَّ وما لم يعبُر— مُخرَجُ tools/audit/sovereign_write_inventory.py --json. ومنه يُشتَقُّ رقمُ الدَّينِ وحدَه. المادةُ التاسعةُ · 2. ومفتاحُ الموقعِ (‏مسارٌ · مالكٌ · دالّةٌ · رتبةٌ) ولا يحملُ رقمَ سطرٍ: الإحداثيُّ يتحرَّكُ بسطرِ تعليقٍ فيُقادِمُ قياسًا لم يتغيَّرْ سلوكُه (DISC-039).",
 "summary": {
  "write_sites_total": 246,
  "by_area": {
   "core": {
    "public": 1,
    "sovereign": 0,
    "non_sovereign": 0
   },
   "service_common": {
    "public": 28,
    "sovereign": 0,
    "non_sovereign": 28
   },
   "services": {
    "public": 171,
    "sovereign": 42,
    "non_sovereign": 128
   },
   "tools": {
    "public": 1,
    "sovereign": 0,
    "non_sovereign": 1
   }
  },
  "public_write_operations": 201,
  "sovereign_write_operations": 42,
  "closed_legacy_paths": 7,
  "non_sovereign_write_operations": 157,
  "non_sovereign_by_file": {
   "federal/executive/services/src/amos_federation/common/persistent.py": 20,
   "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py": 17,
   "federal/executive/services/src/amos_federation/services/national_economy/service.py": 16,
   "federal/executive/services/src/amos_federation/services/federal_state/service.py": 10,
   "federal/executive/services/src/amos_federation/services/governance/treasury.py": 9,
   "federal/executive/services/src/amos_federation/services/royal/main.py": 9,
   "federal/executive/services/src/amos_federation/services/governance/expansion.py": 8,
   "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py": 7,
   "federal/executive/services/src/amos_federation/services/governance/system_life.py": 7,
   "federal/executive/services/src/amos_federation/services/state_treasury/service.py": 7,
   "federal/executive/services/src/amos_federation/services/agent_runtime/health.py": 5,
   "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py": 5,
   "federal/executive/services/src/amos_federation/services/governance/security.py": 5,
   "federal/executive/services/src/amos_federation/services/governance/state_runtime.py": 5,
   "federal/executive/services/src/amos_federation/common/database.py": 4,
   "federal/executive/services/src/amos_federation/services/agent_runtime/population.py": 3,
   "federal/executive/services/src/amos_federation/services/executive_core/repository.py": 3,
   "federal/executive/services/src/amos_federation/common/durable_event_bus.py": 2,
   "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py": 2,
   "federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py": 2,
   "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py": 2,
   "federal/executive/services/src/amos_federation/services/training/persistent_registry.py": 2,
   "federal/executive/services/src/amos_federation/common/event_bus.py": 1,
   "federal/executive/services/src/amos_federation/common/events.py": 1,
   "federal/executive/services/src/amos_federation/services/api_gateway/store.py": 1,
   "federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py": 1,
   "federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py": 1,
   "federal/executive/services/src/amos_federation/services/government_services/service.py": 1,
   "tools/migrations/r4_unify_agent_identity.py": 1
  }
 },
 "sites": [
  {
   "path": "core/sovereignty/gateways.py",
   "owner": "SubordinateGateway",
   "function": "execute",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/database.py",
   "owner": "-",
   "function": "db_cursor",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/database.py",
   "owner": "-",
   "function": "ensure_added_columns",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/database.py",
   "owner": "-",
   "function": "with_db",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/database.py",
   "owner": "-",
   "function": "wrapper",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/durable_event_bus.py",
   "owner": "DurableEventBus",
   "function": "ack",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/durable_event_bus.py",
   "owner": "DurableEventBus",
   "function": "publish",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/event_bus.py",
   "owner": "EventBus",
   "function": "publish",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/events.py",
   "owner": "EventPublisher",
   "function": "publish",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentAgentStore",
   "function": "register",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentAuditStore",
   "function": "append",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()",
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentCriticStore",
   "function": "review",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentExperienceStore",
   "function": "record",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentMemoryStore",
   "function": "store",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "create",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 1,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 2,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 3,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 4,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 5,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 6,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "get",
   "ordinal": 7,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentPromotionStore",
   "function": "save_gates",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentSystemStateStore",
   "function": "reset",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentSystemStateStore",
   "function": "set_level",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentTaskStore",
   "function": "create",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentTaskStore",
   "function": "update_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentToolStore",
   "function": "_seed_from_yaml",
   "ordinal": 0,
   "public": false,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/common/persistent.py",
   "owner": "PersistentToolStore",
   "function": "register",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "HealthChecker",
   "function": "check_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "IsolationSystem",
   "function": "isolate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "IsolationSystem",
   "function": "log_action",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "IsolationSystem",
   "function": "release",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/health.py",
   "owner": "TreatmentSystem",
   "function": "start_treatment",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/population.py",
   "owner": "AgentSchool",
   "function": "take_step",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/population.py",
   "owner": "PopulationRegistry",
   "function": "register_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/agent_runtime/population.py",
   "owner": "PopulationRegistry",
   "function": "update_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/api_gateway/store.py",
   "owner": "DatabaseTaskStore",
   "function": "create",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
   "owner": "-",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
   "owner": "-",
   "function": "register_identity",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_identity_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
   "owner": "-",
   "function": "set_lifecycle_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
   "owner": "-",
   "function": "update_identity",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py",
   "owner": "-",
   "function": "register_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/engine.py",
   "owner": "ExecutiveCore",
   "function": "_erase",
   "ordinal": 0,
   "public": false,
   "writes": [
    "delete()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/engine.py",
   "owner": "ExecutiveCore",
   "function": "submit",
   "ordinal": 0,
   "public": true,
   "writes": [
    "delete()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/repository.py",
   "owner": "ExecutiveTaskRepository",
   "function": "compare_and_set",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/repository.py",
   "owner": "ExecutiveTaskRepository",
   "function": "create",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/repository.py",
   "owner": "ExecutiveTaskRepository",
   "function": "delete",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py",
   "owner": "ConstitutionalAuthorizer",
   "function": "guard",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "add_claim",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "add_party",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "open_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "record_proceeding",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py",
   "owner": "-",
   "function": "submit_evidence",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py",
   "owner": "-",
   "function": "record_enforcement",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py",
   "owner": "-",
   "function": "appoint_judge",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py",
   "owner": "-",
   "function": "create_court",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py",
   "owner": "-",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py",
   "owner": "-",
   "function": "issue_ruling",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "add_claim",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "add_party",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "appoint_judge",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "assign_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "close_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "enforce_ruling_via_task",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "enforce_ruling_via_treasury",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "file_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "open_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "open_hearing",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "record_proceeding",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "register_court",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "set_court_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "set_evidence_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "set_judge_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "submit_evidence",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_judiciary/service.py",
   "owner": "FederalJudiciary",
   "function": "vacate_ruling",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "bind_institution",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "execute_scoped_disbursement",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_operation"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "execute_scoped_operation",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_operation"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "grant_delegation",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "record_relation",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "register_government",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "revoke_delegation",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "scope_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "scope_service",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/federal_state/service.py",
   "owner": "FederalStateGovernment",
   "function": "set_government_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "PopulationExpansion",
   "function": "create_batch",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "PopulationExpansion",
   "function": "employ_batch",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "PopulationExpansion",
   "function": "enroll_batch",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "PopulationExpansion",
   "function": "graduate_batch",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "RetirementSystem",
   "function": "retire_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "SpecializationProgram",
   "function": "take_exam",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "University",
   "function": "approve_output",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/expansion.py",
   "owner": "University",
   "function": "submit_output",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "_complete_step_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "_init_factory",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "_start_production_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "complete_step",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_complete_step_row",
    "_restore_product_pipeline"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "Factory",
   "function": "start_production",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_product_row",
    "_write_product_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "FactoryRegistry",
   "function": "_assign_manager_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/factories.py",
   "owner": "FactoryRegistry",
   "function": "assign_manager",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_set_manager_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ApprovalSystem",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ApprovalSystem",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ApprovalSystem",
   "function": "decide_approval",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ApprovalSystem",
   "function": "request_approval",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ExecutiveBranch",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ExecutiveBranch",
   "function": "_init_roles",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "ExecutiveBranch",
   "function": "appoint",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "add_argument",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "file_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "JudicialBranch",
   "function": "rule",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 3,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "_apply",
   "ordinal": 4,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "enact",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "open_debate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "open_voting",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "propose",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "LegislativeBranch",
   "function": "vote",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "fail_gate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "pass_gate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "PromotionSystem",
   "function": "start_promotion",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "SupremeOversight",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "SupremeOversight",
   "function": "generate_compliance_report",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/federation.py",
   "owner": "_FederationUndo",
   "function": "_restore",
   "ordinal": 0,
   "public": false,
   "writes": [
    "commit()",
    "delete()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "EvaluationSystem",
   "function": "evaluate_model",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "LearningCycle",
   "function": "collect_experiences",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "LearningCycle",
   "function": "complete_training",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "LearningCycle",
   "function": "start_training",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "ModelPromotionCycle",
   "function": "_init_tracks",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "ModelPromotionCycle",
   "function": "promote_beta_to_alpha",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "ModelPromotionCycle",
   "function": "start_canary",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/learning_cycle.py",
   "owner": "ModelPromotionCycle",
   "function": "start_shadow",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "RBACSystem",
   "function": "_init_roles",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "RBACSystem",
   "function": "_migrate_session_tenant",
   "ordinal": 0,
   "public": false,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "RBACSystem",
   "function": "create_session",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "RateLimiter",
   "function": "check_rate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "SecretVault",
   "function": "store_secret",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "TLSCertManager",
   "function": "issue_certificate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/security.py",
   "owner": "TLSCertManager",
   "function": "verify_certificate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "FederalMessageBus",
   "function": "send_message",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "_allocate_budget_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "_init_states",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "allocate_budget",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_add_to_budget"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "assign_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "reactivate_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "register_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/state_runtime.py",
   "owner": "StateRuntime",
   "function": "suspend_state",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "bootstrap",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "create_backup",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "graceful_shutdown",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "health_check",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "launch_checklist",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "restore_backup",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/system_life.py",
   "owner": "SystemLifecycle",
   "function": "self_heal",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_log_event"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "allocate_budget",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "charge_model_invoke",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "charge_retraining",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "charge_storage",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "generate_financial_report",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "process_real_costs",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "reward_quality_report",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "reward_successful_training",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/governance/treasury.py",
   "owner": "Treasury",
   "function": "reward_task_completion",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_record_transaction"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "assign_case",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_assign_case_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "close_case",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_set_case_status_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "decide_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_decision_row",
    "_record_decision_provenance",
    "_set_case_status_row",
    "_write_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "open_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_case_row",
    "_write_case_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "process_case",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "publish_service",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_service_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/government_services/service.py",
   "owner": "GovernmentServices",
   "function": "set_service_status",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_set_service_status_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py",
   "owner": "ModelLayer",
   "function": "log_cost",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/model_gateway/model_layer.py",
   "owner": "ModelLayer",
   "function": "set_cached",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "activate_policy",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "authorize_expenditure",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "authorize_procurement",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "authorize_transfer",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "create_program",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "define_indicator",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "execute_economic_decision",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "execute_expenditure",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "execute_transfer",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "issue_policy",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_category",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_public_asset",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_public_entity",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_public_liability",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_revenue_source",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_issue_decision"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_economy/service.py",
   "owner": "NationalEconomy",
   "function": "register_sector",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 3,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 4,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 5,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 6,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 7,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "_apply",
   "ordinal": 8,
   "public": false,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "assign_position",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "create_identity",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "create_position",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "grant_authority",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "link_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "link_principal",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "revoke_assignment",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "revoke_authority",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "NationalRegistry",
   "function": "set_identity_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/national_registry/service.py",
   "owner": "_RegistryUndo",
   "function": "_restore",
   "ordinal": 0,
   "public": false,
   "writes": [
    "commit()",
    "delete()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "approve_promotion",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "close_institution",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "create_decree",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "create_institution",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "dismiss_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "generate_interface",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "request_agent_training",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "request_tool_generation",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/royal/main.py",
   "owner": "-",
   "function": "restore_agent",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "_apply",
   "ordinal": 0,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "_apply",
   "ordinal": 1,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "_apply",
   "ordinal": 2,
   "public": false,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "_write_institution_unguarded",
   "ordinal": 0,
   "public": false,
   "writes": [],
   "guarded": false,
   "closed_legacy": true,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "appoint_official",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_official_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "create_department",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_department_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "register_institution",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_delete_institution_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "revoke_official",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_revoke_official_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_registry/service.py",
   "owner": "StateRegistry",
   "function": "set_institution_status",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": true,
   "closed_legacy": false,
   "writes_via": [
    "_set_institution_status_row"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "allocate",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "create_budget",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "disburse",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_post",
    "_record_transaction_authority"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "establish_treasury",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "open_account",
   "ordinal": 0,
   "public": true,
   "writes": [
    "add()",
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "post_funding",
   "ordinal": 0,
   "public": true,
   "writes": [],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_post",
    "_record_transaction_authority"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/state_treasury/service.py",
   "owner": "StateTreasury",
   "function": "reverse_transaction",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": [
    "_post",
    "_record_transaction_authority"
   ]
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/training/persistent_registry.py",
   "owner": "PersistentModelRegistry",
   "function": "register",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()",
    "merge()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "federal/executive/services/src/amos_federation/services/training/persistent_registry.py",
   "owner": "PersistentModelRegistry",
   "function": "update_status",
   "ordinal": 0,
   "public": true,
   "writes": [
    "commit()"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  },
  {
   "path": "tools/migrations/r4_unify_agent_identity.py",
   "owner": "-",
   "function": "emit_sql",
   "ordinal": 0,
   "public": true,
   "writes": [
    "raw-sql-write"
   ],
   "guarded": false,
   "closed_legacy": false,
   "writes_via": []
  }
 ]
}
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-628/mutation_probe_wi107.py
EXIT: 0
BYTES: 4552
SHA256: 609703dfe8e439d2509624ff45efcd0906e63a18e898a44aaf7c1d5e42236ca9
NO_EOL: 0
--- OUTPUT ---
"""مسبارُ طفراتِ WI-107 (الدفعةُ R1) — دليلُ قيدِ W-628.

الغرض: تطبيقُ كلِّ طفرةٍ مُعلَنةٍ في ملحقِ التصميمِ (§ 5 · M1–M5 · بحصادِ M5
المصحَّحِ كما قُيِّدَ في evidence/W-625/README.md) على نسخةِ الوحدةِ، وتشغيلُ
فحوصِ البندِ، وإثباتُ أنَّ كلَّ طفرةٍ تُسقِطُ فحصَها المُعلَنَ ثمَّ استعادةُ الأصلِ
بايتًا ببايتٍ (البصمةُ قبلُ وبعدُ).
التشغيل: من جذرِ المستودعِ — `.venv/bin/python docs/audit/evidence/W-628/mutation_probe_wi107.py`
النمطُ: mutation_probe_wi106.py (سابقةُ W-617) — لا اختلافَ في الميكانيكا.
المالك: Perplexity Computer · تاريخ الإنشاء: 2026-10-23 (W-628)
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SERVICES = ROOT / "federal" / "executive" / "services"
TARGET = SERVICES / "src/amos_federation/services/national_registry/service.py"
TESTS = "tests/test_wi107_national_registry_register_sovereign.py"

_M1_OLD = """        guarded = _registry_authorizer().guard_declared(
            REGISTRY_VERB, target, applier=_apply, **crossing
        )
        _refuse_replay(guarded, "NationalRegistry.create_identity", target)
        identity = guarded.value
"""
_M1_NEW = "        identity = _apply(None)\n"


def _m1(src: str) -> str:
    assert src.count(_M1_OLD) == 1, "مرساةُ M1 ليست فريدةً"
    return src.replace(_M1_OLD, _M1_NEW, 1)


MUTATIONS = {
    "M1 · create_identity يكتبُ بلا عبورٍ": (_m1, ["t1", "t3"]),
    "M2 · الفاعلُ JUDICIAL": (
        lambda s: s.replace('REGISTRY_ACTOR = "EXECUTIVE"', 'REGISTRY_ACTOR = "JUDICIAL"', 1),
        ["t1", "t8"],
    ),
    "M3 · المُعوِّضُ لا يفعلُ شيئًا": (
        lambda s: s.replace(
            "    def _restore(self) -> None:\n", "    def _restore(self) -> None:\n        return\n", 1
        ),
        ["t4", "t5"],
    ),
    "M4 · revoke_assignment بلا تسجيلِ السابقِ": (
        lambda s: s.replace(
            '                row = session.get(OfficialPositionModel, assignment_id)\n'
            '                undo.prior(row, "status", "revoked_at", "revocation_reason")\n',
            '                row = session.get(OfficialPositionModel, assignment_id)\n',
            1,
        ),
        ["t5"],
    ),
    "M5 · link_principal بلا رفضِ الإعادةِ (D5 مقتولةٌ)": (
        lambda s: s.replace("            if existing is not None:\n", "            if False:\n", 1),
        ["t6"],
    ),
}


def _run(selector: str) -> tuple[int, str]:
    r = subprocess.run(
        [sys.executable, "-m", "pytest", TESTS, "-q", "-p", "no:cacheprovider", "-k", selector],
        cwd=SERVICES,
        capture_output=True,
        text=True,
        timeout=900,
        check=False,
    )
    lines = [ln for ln in r.stdout.splitlines() if "passed" in ln or "failed" in ln]
    return r.returncode, (lines[-1] if lines else r.stdout[-300:])


def main() -> int:
    original = TARGET.read_bytes()
    digest = hashlib.sha256(original).hexdigest()
    print(f"sha256 قبلُ: {digest}")
    rc, line = _run("wi107")
    print(f"الأصلُ: rc={rc} · {line}")
    all_killed = rc == 0
    try:
        for name, (mutate, expected) in MUTATIONS.items():
            mutated = mutate(original.decode("utf-8"))
            assert mutated != original.decode("utf-8"), f"الطفرةُ لم تُطبَّق: {name}"
            TARGET.write_text(mutated, encoding="utf-8")
            for test in expected:
                rc, line = _run(f"wi107_{test}_")
                killed = rc != 0
                all_killed = all_killed and killed
                print(f"{name} ⇒ {test}: {'سقطَ (قُتِلَت)' if killed else 'نجحَ (نجَت!)'} · {line}")
            TARGET.write_bytes(original)
    finally:
        TARGET.write_bytes(original)
    after = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    print(f"sha256 بعدُ: {after} · {'مطابقٌ' if after == digest else 'مختلفٌ!'}")
    print("الحكمُ: كلُّ الطفراتِ قُتِلَت" if all_killed and after == digest else "الحكمُ: فشلٌ")
    return 0 if all_killed and after == digest else 1


if __name__ == "__main__":
    raise SystemExit(main())
=== RAW [19] END ===
=== RAW [20] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python docs/audit/evidence/W-628/mutation_probe_wi107.py
EXIT: 0
BYTES: 1685
SHA256: e0a79c4a9efa1d689751afaf87294d77ca925dca4b3058cb159eca591c4497ff
NO_EOL: 0
--- OUTPUT ---
sha256 قبلُ: ca1f05ec38b9b256e16e9c6b28a21a68c7468d36b10fb11d86a624060d514fbd
الأصلُ: rc=0 · ============================== 9 passed in 8.06s ===============================
M1 · create_identity يكتبُ بلا عبورٍ ⇒ t1: سقطَ (قُتِلَت) · ======================= 1 failed, 8 deselected in 1.43s ========================
M1 · create_identity يكتبُ بلا عبورٍ ⇒ t3: سقطَ (قُتِلَت) · ======================= 1 failed, 8 deselected in 1.12s ========================
M2 · الفاعلُ JUDICIAL ⇒ t1: سقطَ (قُتِلَت) · ======================= 1 failed, 8 deselected in 1.25s ========================
M2 · الفاعلُ JUDICIAL ⇒ t8: سقطَ (قُتِلَت) · ======================= 1 failed, 8 deselected in 0.63s ========================
M3 · المُعوِّضُ لا يفعلُ شيئًا ⇒ t4: سقطَ (قُتِلَت) · ======================= 1 failed, 8 deselected in 0.96s ========================
M3 · المُعوِّضُ لا يفعلُ شيئًا ⇒ t5: سقطَ (قُتِلَت) · ======================= 1 failed, 8 deselected in 1.59s ========================
M4 · revoke_assignment بلا تسجيلِ السابقِ ⇒ t5: سقطَ (قُتِلَت) · ======================= 1 failed, 8 deselected in 1.32s ========================
M5 · link_principal بلا رفضِ الإعادةِ (D5 مقتولةٌ) ⇒ t6: سقطَ (قُتِلَت) · ======================= 1 failed, 8 deselected in 0.92s ========================
sha256 بعدُ: ca1f05ec38b9b256e16e9c6b28a21a68c7468d36b10fb11d86a624060d514fbd · مطابقٌ
الحكمُ: كلُّ الطفراتِ قُتِلَت
=== RAW [20] END ===
=== RAW [21] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && rg -n "D17-3|Q-61|Q-71" docs/audit/SOVEREIGN_DECISION_REGISTER.md
EXIT: 0
BYTES: 12065
SHA256: 1ba0ca6129d26c36648e4f07a99bf282123f0c252b01ef20560c005e18a1ee4d
NO_EOL: 0
--- OUTPUT ---
8:تاريخ آخر تعديل: 2026-10-23 (`W-625` — **Q-71 DECIDED** بأمرِ المالكِ الصريحِ: «أذن بـconftest.py تحت WI-107» — قسمةُ نطاقِ مسارِ conftest.py من WI-072 إلى WI-107) · ووقبله (`W-612` — **D17-2** الأربعةُ مؤجَّلةٌ ولا تعطّلُ J2/J3 · **إبلاغُ ما بعدَ الدمجِ** يبقى إبلاغًا (توجيهُ المستشارِ 19 § 1)) · ووقبله ((`W-611` — **Q-61 DECIDED** بالخيارِ (3) بتطبيقٍ صريحٍ على WI-096 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-610` — **D19 DECIDED**: إذنُ المالكِ بإغلاقِ WI-105 (توجيهُ المستشارِ 19 § 1 · نصُّه حرفيًّا)) · ووقبله ((`W-601` — **Q-70 DECIDED** بالخيارِ (1) مشروطًا (توجيهُ المستشارِ 18 § 1 · نصُّ المالكِ حرفيًّا) · والقياسُ الشرطيُّ يضعُ الفجوةَ في الحدِّ نفسِه) · ووقبله (`W-599` — قُيِّدَ **Q-70** (PENDING_OWNER): تعويضُ فشلِ تثبيتِ النجاحِ في مسارِ `issue_ruling` — آليٌّ موصولٌ أم مُعوِّضٌ مسجَّلٌ · ملخصُه في `HANDOFFS/OWNER-DECISIONS-D18.md` · حاجبُ جولةِ مجلسِ دفعةِ J1) · وكانَ قبلَه: 2026-10-21 (`W-592` — قراراتُ المالكِ بتوجيهِ المستشارِ 17 مسجَّلةً بنصّها الحرفيِّ: Q-69 DECIDED · D17-1 · D17-2 · D17-3 · D17-4 · D17-5 · D17-6 · Q-67 DECIDED · Q-68 DECIDED) · وكانَ قبلَه: 2026-10-21 (`W-591` — سُجّلَ **Q-69** (PENDING_OWNER): هل تقفُ الجولةُ الثانيةُ على تصميمِ J1 أم تُعادُ بمقاعدِ § 1.3 — DISC-127) · وكانَ قبلَه: 2026-10-21 (`W-581` — سُجّلَ **Q-68** (PENDING_OWNER): الطرفُ خارجَ الفروعِ (AGENT · SYSTEM) يُمارسُ أفعالَ الفروعِ الحصريّةَ — DISC-121) · وكانَ قبلَه: 2026-10-21 (`W-570` — سُجّلَ **Q-67** (PENDING_OWNER): تجديداتُ W-569 الثلاثُ بلا إذنٍ صريحٍ · وإضافةٌ مؤرَّخةٌ على مخاطرِ Q-66: «لا تخفيفَ» غيرُ مُثبَتٍ حتى فحصِ الملاصقةِ) · ووقبله ((W-561 — قيدُ قرارِ المالكِ Q-66: الاستلامُ المعلنُ للخطِّ المفتوحِ PR #103 + إلحاقُ `tools/crown` بـ`tooling-gates` كسابقةِ W-052) · ووقبله ((W-553 — قيدُ قرارَي المالكِ Q-64 (ختمُ الوقتِ منَ الساعةِ الفعليةِ فقط + DISC-118 + حارسٌ) وQ-65 (إذنُ CLOSED لـWI-094 وWI-095 وWI-099 · وWI-098 بلا إذنٍ: PROPOSED لا جولةَ له) بنصَّيهما الحرفيَّينِ) · ووقبله (W-540 — قيدُ قرارِ المالكِ Q-63 (DECIDED · أمرٌ مباشرٌ) بنصِّهِ الحرفيِّ: إعادةُ جولةِ WI-094 بمخرجاتٍ خامٍ كاملةٍ ومنعُ الاقتطاعِ نصًّا وفحصًا) · ووقبله (W-535 — إضافةٌ مؤرَّخةٌ في موجزِ Q-3 (البندُ 4): مواضعُ بناءِ المُصرِّحِ صارت تسعةً (5 مُعلِنةٌ · 4 افتراضيّةٌ) بعدَ استعادةِ شِفرةِ WI-082 — رقمٌ مقيسٌ لا حسمٌ · Q-3 باقٍ HUMAN_DECISION_REQUIRED) · ووقبله (W-529 — **Q-62 مقرَّرٌ** بقرارِ المالكِ الحرفيِّ: الخيارُ (2) — النسخةُ المقصودةُ لـWI-082 هي `1c52572` · بندُ استعادةٍ فوقَ المعالجةِ معَ القياسِ ثمَّ مقارنةُ الكلفةِ واصطلاحِ الهدفِ بالقياسِ) · ووقبله (W-526 — سُجّلَ **Q-62** (PENDING_OWNER): أيُّ نسخةٍ من شِفرةِ `WI-082` مقصودةٌ للبندِ — نسخةُ العقدةِ الحاضرةِ (البايتيةُ من `wi-082-stage3` · أعادها W-465) أم نسخةُ main التي ردَّها W-425 والتي يُعيدُها Q-51 ③؟ — أثارَتْهُ جولةُ المجلسِ على WI-082 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ · DISC-115 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-521 — سُجّلَ **Q-61** (PENDING_OWNER): هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — أثارَتْهُ جولةُ المجلسِ على WI-096 (ملاحظةٌ حاجبةٌ من مقعدٍ واحدٍ على المعيارِ 1 · DISC-112 · لا إجماعَ فلا VERIFIED)) · ووقبله (W-509 — سُجّلَ **Q-60**: استبعادُ مقعدِ عائلةِ المنسِّقِ الحاضرِ (Claude) من مجلسِ المراجعةِ — المقاعدُ Gemini · Grok · Kimi بعدَ قياسِ توفرِ Kimi) · ووقبله (W-503 — سُجّلَ **Q-59**: مجلسُ مراجعةٍ من نماذجٍ متعددةِ العوائلِ في بيئاتٍ منفصلةٍ (عزلٌ إجرائيٌّ معلنٌ) — مسلكُ VERIFIED · وأُلغيَ اشتراطُ مقعدِ HuggingFace · وإغلاقُ Q-48 مؤجّلٌ حتى الجولاتِ) · ووقبله 2026-10-18 (W-446 — نقلُ قراراتِ «توجيهِ المستشارِ 11» التاريخيّةِ إلى main من المكدَّسِ الموازيِ بنصوصِها الحرفيّةِ (Q-25 ① · Q-35 ② · Q-38 (ج) · WI-082 ③ · إذنُ ترويسةِ HANDBOOK) بقرارِ Q-52/Q-56 · وW-442 — Q-58: تعارضُ نطاقِ WI-086 بندانِ منفصلانِ) · ووقبله (W-431 — Q-57: الجزءُ (د) من DISC-082 بندًا) · ووقبله (W-429 — قراراتُ المالكِ Q-54 · Q-55 · Q-56 جوابًا على OWNER-DECISIONS-D12) · ووقبله (W-363 — قراراتُ المالكِ بتوجيهِ المستشارِ 8 (2026-10-16 · الرياض 10:00): Q-6 · Q-15 · Q-21 · Q-22 · Q-24 · Q-25 · Q-H → DECIDED · وQ-16 DECIDED في الاختيارِ والتنفيذُ مشروطٌ · ومعلومةُ «لا رصيدَ Replicate» — بإضافاتٍ مؤرَّخةٍ لا بمحو) · ووقبله (W-348 — سُجِّلَ **Q-H** (PENDING_OWNER): هل يلزمُ لـVERIFIED أن يُعيدَ المراجعُ تشغيلَ أوامرِ المعاييرِ بنفسه؟ — بتوجيهِ المستشارِ 5 · G1 · والموقوفُ حتى الحسمِ: لا CLOSED لـWI-076 ولا عملٌ C3/C4 عليهِ · ووقبله W-346 — سُجِّلَ **Q-G**: اعتمادٌ بمقعدٍ واحدٍ لجولةِ مراجعةِ WI-076 حصرًا — بأمرَي المالكِ الصريحَينِ «أصدر قرار استبدال Q-### صراحةً وسمِّ المراجعين البدلاء» ثم «اعتماد بمقعد واحد» — والواقعةُ الدقيقةُ: طلبُ GPT 5.6 Terra عبرَ Replicate رُدَّ بـ402 (رصيدٌ غيرُ كافٍ لتشغيلِ الطلبِ)، ثم اختارَ المالكُ المقعدَ الواحدَ، واكتملَ اتصالُ Hugging Face لاحقًا — والمقعدُ الوحيدُ: قناةُ المراجعةِ الاستشاريةِ · ووقبله W-334 — أجابَ المالكُ جوابًا عامًّا: «ادرس كل خيار ثم قرر نيابه عن المالك · اذا كان الأمر يتطلب مراجعة خارجية فاعقد مجلس ونفذ جولة مجلس · لا تتوقف اطلاقا» ⇒ Q-A…Q-F ⇒ DECIDED بالتفويضِ · وDecision 1 (تجديدُ حجزِ WI-039/040 إلى 2026-10-31) نُفِّذَ) · وقبلَه  — سُجِّلَت أسئلةُ المالكِ Q-A…Q-D (PENDING_OWNER · لا يُفترَضُ جوابُها) · وقبلَه **W-327** — سُجِّلَ **Q-46**: تشكيلُ مجلسِ المراجعةِ (اعتمادُ `GPT 5.6 Terra` + `Grok 4.7` · سابقةُ الجولاتِ 8–11 مستمرةٌ · بتفويضِ المالكِ «ادرس كل خيار ثم قرر نيابه عن المالك»)) · وقبله 2026-10-13 (**W-310** — سُجِّلَ **Q-45**: قسمةُ نطاقِ `WI-026` لصالحِ `WI-072` بقرارِ المالك) · وقبله 2026-09-08 (**W-150** — سُجِّلَ **Q-44**: قسمةُ نطاقِ `WI-023` بتصريحِ المالكِ · وقبلَه **W-147** — نُفِّذَ **Q-43**: تعيينُ مجلسِ مراجعةٍ مستقلٍّ بالنماذجِ (GPT 5.6 + Grok 4.6) بقرارِ المالكِ — تحديثٌ لـ`A-2`)))
2296:### Q-61 · عرضُ التصميمِ قبلَ الشِّفرةِ في WI-096 — DECIDED (W-611)
2297:«Q-61: خيار (3) مع تطبيق صريح على WI-096. أقرّ أن شرط عرض التصميم قبل الشفرة لم يتحقق إجرائيًّا في WI-096 وأتجاوزه لهذا البند وحده لأن المعايير 2 و3 و4 تحققت بإجماع المقاعد، ويُقيَّد الإخلال كما هو. وللبنود القادمة يُودَع التصميم في التزام مستقل يسبق الشفرة. ثم تُعاد جولة WI-096 بمسبار كل مقعد.» ⇒ تفصيلُه تحتَ `## Q-61`.
2305:## Q-71 · ملكيةُ إصلاحِ عزلِ سجلِّ الذرّيّةِ في الفحوصِ بعدَ شِفرةِ R1 (W-625): مسارُ `tests/conftest.py` تحتَ WI-107 — DECIDED (2026-10-23 · W-625 · أمرُ المالكِ الصريح)
2370:### D17-3 · الإعلانُ الساكنُ للفرعِ — DECIDED
2380:«لا جولات مجلس على تصميم منفرد من الآن. الجولة الواحدة لكل دفعة تغطي التصميم والشفرة والأدلة معًا بعد التنفيذ. شرط الترتيب باقٍ: التزام وثيقة التصميم يسبق التزام الشفرة في التاريخ (يتحقق منه الفاحص)، وهذا هو درس Q-61. … حجم الدفعة: كل دفعة تقدَّم إلى main تنقص D-4 بما لا يقل عن عشرة أسطح حيث يسمح النمط، إلا ما فرضه التصميم (J1 = 2 لأنه يُرسي النمط).» — نُفِّذَ تعديلُ البروتوكولِ مؤرَّخًا (W-592).
2537:## Q-61 · هل يستوفي إيداعُ وثيقةِ تصميمِ WI-096 معَ شِفريتِها في التزامٍ واحدٍ معيارَ «تُعرَضُ قبلَ الشِفرةِ»؟ — DECIDED (2026-10-22 · W-611 · توجيهُ المستشارِ 19 § 1 · الخيارُ 3 بتطبيقٍ صريحٍ على WI-096) · وكانَ PENDING_OWNER (2026-10-19 · W-521)
2539:> **[إضافةٌ مؤرَّخةٌ · 2026-10-22 · W-611] DECIDED — نصُّ المالكِ حرفيًّا:** «Q-61: خيار (3) مع تطبيق صريح على WI-096. أقرّ أن شرط عرض التصميم قبل الشفرة لم يتحقق إجرائيًّا في WI-096 وأتجاوزه لهذا البند وحده لأن المعايير 2 و3 و4 تحققت بإجماع المقاعد، ويُقيَّد الإخلال كما هو. وللبنود القادمة يُودَع التصميم في التزام مستقل يسبق الشفرة. ثم تُعاد جولة WI-096 بمسبار كل مقعد.» (النصُّ الكاملُ للتوجيهِ في [`evidence/W-610/ADVISOR_DIRECTIVE_19.md`](evidence/W-610/ADVISOR_DIRECTIVE_19.md)) ⇒ (أ) **الإخلالُ مُقيَّدٌ كما هو**: وثيقةُ التصميمِ وشِفرتُه في الالتزامِ نفسِه `cacd1a7` (W-471) — والمعيارُ (1) لم يتحقق إجرائيًّا · (ب) تجاوزُه **لـWI-096 وحدَه** · (ج) **للبنودِ القادمةِ**: التصميمُ في التزامٍ مستقلٍّ يسبقُ الشِّفرةَ · (د) تُعادُ جولةُ WI-096 بمسبارِ كلِّ مقعدٍ (§ 4.9) — لا VERIFIED قبلَها.
=== RAW [21] END ===
=== RAW [22] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && sha256sum docs/audit/evidence/W-628/briefs/briefing_kimi_k3.md
EXIT: 0
BYTES: 119
SHA256: 3f5d0abe73c160c624dc2041a7f76e535aad47422819a7d02b82bf1420c8dbd8
NO_EOL: 0
--- OUTPUT ---
ec22c1d65b5a3eea45b71fe245d94a326ab9877a0e08b495a21c6e5f694456fb  docs/audit/evidence/W-628/briefs/briefing_kimi_k3.md
=== RAW [22] END ===
=== RAW [23] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && cat docs/audit/evidence/W-628/briefs/SHA256SUMS
EXIT: 0
BYTES: 268
SHA256: 20fab81d073197a3949dd2b633d2bed58e864f3dc7b5e15905e65faabe78b86b
NO_EOL: 0
--- OUTPUT ---
f42eca4441a14920ecbecc455c48a26b241bbebbfa0a44f00bcdeb97b2d3361c  briefing_gemini_3_8_flash.md
956b16caa823b5305cd33715cda5af265f6cf5e376480623ae000351035880a3  briefing_grok_4_7.md
ec22c1d65b5a3eea45b71fe245d94a326ab9877a0e08b495a21c6e5f694456fb  briefing_kimi_k3.md
=== RAW [23] END ===
=== RAW [24] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py -q
EXIT: 0
BYTES: 100
SHA256: 3b6ec151155052f77c4c188ca135abac3cea34a6644cb00c080efb73c86f0a8f
NO_EOL: 0
--- OUTPUT ---
..............................................................           [100%]
62 passed in 43.33s
=== RAW [24] END ===
=== RAW [25] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps
EXIT: 0
BYTES: 319
SHA256: e237b66d4e4686ec1d76c273157268e76598e93fa5418cfa9090f52a8c38efd9
NO_EOL: 0
--- OUTPUT ---
عقدُ نَسَبِ القياساتِ مستقيمٌ: 11 قياسًا مقيَّدًا · 8 محروسًا (‏منها 1 برباطٍ مقيسٍ نصًّا) · 3 مُعلَنًا بسببٍ مكتوبٍ. ومُؤَجَّلٌ إلى الشطرِ الآخرِ: 2 (‏من 2 يحتاجُ حزمًا خارجيّةً).
=== RAW [25] END ===
=== RAW [26] BEGIN ===
CMD: nl -ba /home/user/workspace/council_w628/kimi_k3/probe/probe_wi107_kimi_k3.py
EXIT: 0
BYTES: 11382
SHA256: e159888770186af7eb505c0d75856bda08d00baad2d4650161c2770bb1a55e5d
NO_EOL: 0
--- OUTPUT ---
     1	"""
     2	مسبارُ المقعدِ kimi_k3 الخاصُّ لجولةِ WI-107 (R1 · register) — يُنادي المسارَ
     3	الإنتاجيَّ وحدَه (NationalRegistry بالواجهةِ العامّةِ) ويحاولُ كسرَ ثلاثِ خواصَّ
     4	مُدَّعاةٍ في المعيارِ (2):
     5	
     6	  P1 · الإعادةُ الخفيّةُ بعدَ تلفٍ: إن ضاعَ صفُّ الربطِ من القاعدةِ نفسِها
     7	       (DELETE مباشرٌ — تحاكي فقدًا)، فإعادةُ link_principal على المفتاحِ
     8	       الطبيعيِّ (المستأجر، المبدأ) يجبُ أن تُرفَعَ RegistryReplayError من
     9	       سجلِّ الحدِّ لا أن تنجحَ صامتةً وتُنشئَ صفًّا ثانيًا «كأنّ شيئًا لم يكن».
    10	  P2 · المفتاحُ الطبيعيُّ يشملُ المستأجرَ حقًّا: ربطُ المبدأِ نفسِهِ في مستأجرٍ
    11	       آخر بهويةٍ أخرى في ذلك المستأجرِ يجبُ أن ينجحَ (ليس إعادةً) — فلو نُزِعَ
    12	       المستأجرُ منَ المفتاحِ لانكسرتْ هذه الخاصيةُ برفضٍ زائفٍ.
    13	  P3 · مُعوِّضُ الإنشاءِ على سطحٍ لم يُغطِّه T4/T5 — create_position: إسقاطُ
    14	       تثبيتِ النجاحِ بعدَ الأثرِ يجبُ أن يستعيدَ الحالةَ نظيفةً (لا صفَّ منصبٍ).
    15	
    16	الملفّ pytest بحتٌ يُنسَخُ مؤقّتًا إلى federal/executive/services/tests/ (إذنُ الإحاطةِ)
    17	ويُشغَّلُ من دليلِ الخدماتِ بقاعدةِ sqlite وسجلِّ ذرّيّةٍ معزولَينِ للمقعد.
    18	"""
    19	
    20	from __future__ import annotations
    21	
    22	import sys
    23	import uuid
    24	from datetime import UTC, datetime, timedelta
    25	from pathlib import Path
    26	from typing import TYPE_CHECKING, Any
    27	
    28	import pytest
    29	from sqlalchemy import select
    30	from sqlalchemy import text as sa_text
    31	
    32	# النواةُ السياديّةُ (core/) تُستوردُ بعدَ حقنِ جذرِ المستودعِ في المسارِ
    33	# (نفسُ آليّةِ `locate_repo_root` في جسرِ السيادةِ وconftest).
    34	_HERE = Path(__file__).resolve()
    35	for _cand in _HERE.parents:
    36	    if (_cand / "core" / "sovereignty").is_dir():
    37	        if str(_cand) not in sys.path:
    38	            sys.path.insert(0, str(_cand))
    39	        break
    40	
    41	from amos_federation.common.database import get_session_factory, init_db
    42	from amos_federation.common.principal import DEFAULT_TENANT, AuthorizationContext, Principal
    43	from amos_federation.services.national_registry import service as national_registry_module
    44	from amos_federation.services.national_registry.models import (
    45	    IdentityPrincipalModel,
    46	    PositionModel,
    47	)
    48	from amos_federation.services.national_registry.service import (
    49	    RegistryReplayError,
    50	    get_national_registry,
    51	    reset_national_registry,
    52	)
    53	from amos_federation.services.state_registry.service import (
    54	    get_state_registry,
    55	    reset_state_registry,
    56	)
    57	from core.sovereignty.compensation import CompensationRequired
    58	
    59	if TYPE_CHECKING:
    60	    from collections.abc import Iterator
    61	
    62	
    63	def _purge_all_tables() -> None:
    64	    """مسحٌ شاملٌ من الفاحصِ لا من نماذجِ ORM (الجداولُ موزّعةٌ على عدةِّ Base)."""
    65	    from sqlalchemy import inspect as sa_inspect
    66	
    67	    init_db()
    68	    session = get_session_factory()()
    69	    try:
    70	        session.execute(sa_text("PRAGMA foreign_keys=OFF"))
    71	        for table in sa_inspect(session.get_bind()).get_table_names():
    72	            session.execute(sa_text(f'DELETE FROM "{table}"'))  # noqa: S608
    73	        session.commit()
    74	    finally:
    75	        session.close()
    76	
    77	
    78	@pytest.fixture(autouse=True)
    79	def _isolated_registry(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    80	    monkeypatch.setenv(
    81	        "AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER", str(tmp_path / "kimi-probe-ledger.json")
    82	    )
    83	    _purge_all_tables()
    84	    reset_state_registry()
    85	    reset_national_registry()
    86	    national_registry_module.reset_registry_authorizer()
    87	    yield
    88	    _purge_all_tables()
    89	    reset_state_registry()
    90	    reset_national_registry()
    91	    national_registry_module.reset_registry_authorizer()
    92	
    93	
    94	def _seat_context(role_id: str = "king", tenant_id: str = DEFAULT_TENANT) -> AuthorizationContext:
    95	    suffix = uuid.uuid4().hex[:8]
    96	    return AuthorizationContext.from_principal(
    97	        Principal.from_session_record(
    98	            session_id=f"kimi-probe-{role_id}-{suffix}",
    99	            username=f"{role_id}-{suffix}",
   100	            role_id=role_id,
   101	            permissions=("*",),
   102	            expires_at=datetime.now(UTC) + timedelta(hours=1),
   103	            tenant_id=tenant_id,
   104	        )
   105	    )
   106	
   107	
   108	def _count(model: type) -> int:
   109	    session = get_session_factory()()
   110	    try:
   111	        return len(session.execute(select(model)).scalars().all())
   112	    finally:
   113	        session.close()
   114	
   115	
   116	def test_p1_replay_refused_even_if_link_row_vanishes() -> None:
   117	    """فقدانُ صفِّ الربطِ من القاعدةِ لا يجعلُ الإعادةَ نجاحًا ثانيًا."""
   118	    crown = _seat_context()
   119	    national = get_national_registry()
   120	    identity = national.create_identity(context=crown, identity_type="PERSON", label="مسبار p1")
   121	    principal_id = crown.principal_id
   122	    first = national.link_principal(
   123	        context=crown, principal_id=principal_id, identity_id=identity["id"]
   124	    )
   125	    assert first["created"] is True
   126	
   127	    # تلفٌ مقصود: حذفُ الصفِّ مباشرةً من القاعدة (لا عبرَ سطحٍ).
   128	    session = get_session_factory()()
   129	    try:
   130	        row = (
   131	            session.query(IdentityPrincipalModel)
   132	            .filter_by(principal_id=principal_id, tenant_id=DEFAULT_TENANT)
   133	            .one()
   134	        )
   135	        session.delete(row)
   136	        session.commit()
   137	    finally:
   138	        session.close()
   139	
   140	    session = get_session_factory()()
   141	    try:
   142	        assert (
   143	            session.query(IdentityPrincipalModel)
   144	            .filter_by(principal_id=principal_id, tenant_id=DEFAULT_TENANT)
   145	            .count()
   146	            == 0
   147	        )
   148	    finally:
   149	        session.close()
   150	
   151	    # الإعادةُ الآن يجبُ أن تُرفَعَ من الحدِّ — لا نجاحٌ «ثانٍ» يُعيدُ بناءَ الصفّ.
   152	    with pytest.raises(RegistryReplayError):
   153	        national.link_principal(context=crown, principal_id=principal_id, identity_id=identity["id"])
   154	
   155	
   156	def test_p2_same_principal_in_second_tenant_is_not_replay() -> None:
   157	    """المبدأُ نفسُه في مستأجرٍ آخر ليسَ إعادةً (المفتاح يشمل المستأجر)."""
   158	    national = get_national_registry()
   159	    crown_a = _seat_context(tenant_id=DEFAULT_TENANT)
   160	    other_tenant = f"tenant-kimi-{uuid.uuid4().hex[:8]}"
   161	    crown_b = _seat_context(tenant_id=other_tenant)
   162	
   163	    # مبدأٌ واحدٌ: نختارُ معرّفًا ثابتًا ونربطُه في المستأجرينِ بهويّتينِ مختلفتين.
   164	    shared_principal = f"principal-kimi-{uuid.uuid4().hex[:10]}"
   165	    id_a = national.create_identity(context=crown_a, identity_type="PERSON", label="في أ")["id"]
   166	    id_b = national.create_identity(context=crown_b, identity_type="PERSON", label="في ب")["id"]
   167	
   168	    link_a = national.link_principal(
   169	        context=crown_a, principal_id=shared_principal, identity_id=id_a
   170	    )
   171	    link_b = national.link_principal(
   172	        context=crown_b, principal_id=shared_principal, identity_id=id_b
   173	    )
   174	    assert link_a["created"] is True
   175	    assert link_b["created"] is True
   176	    assert link_a["tenant_id"] != link_b["tenant_id"]
   177	
   178	    # وفي المستأجرِ الثاني الربطُ القائمُ نفسُه يعودُ خاملًا قبلَ العبورِ.
   179	    again_b = national.link_principal(
   180	        context=crown_b, principal_id=shared_principal, identity_id=id_b
   181	    )
   182	    assert again_b["created"] is False
   183	
   184	
   185	def test_p3_create_position_compensated_on_settle_failure(
   186	    monkeypatch: pytest.MonkeyPatch,
   187	) -> None:
   188	    """فشلُ التثبيتِ بعد إنشاءِ المنصبِ يستعيدِهِ كاملًا — ومعاودةٌ سليمةٌ تنجح."""
   189	    crown = _seat_context()
   190	    state = get_state_registry()
   191	    national = get_national_registry()
   192	    institution = state.register_institution(
   193	        context=crown,
   194	        code=f"INST-KIMI-{uuid.uuid4().hex[:8].upper()}",
   195	        name="مؤسسةُ مسبارِ p3",
   196	        kind="ministry",
   197	        branch="executive",
   198	    )
   199	
   200	    authorizer = national_registry_module._registry_authorizer()
   201	    ledger = authorizer.boundary.idempotency_ledger
   202	    original = type(ledger).mark_succeeded
   203	
   204	    def _broken_mark_succeeded(*args: Any, **kwargs: Any) -> Any:
   205	        raise RuntimeError("مسبارُ kimi_k3: تثبيتُ النجاحِ مُسقَطٌ عمدًا")
   206	
   207	    monkeypatch.setattr(type(ledger), "mark_succeeded", _broken_mark_succeeded)
   208	    with pytest.raises(CompensationRequired) as caught:
   209	        national.create_position(
   210	            context=crown,
   211	            code=f"POS-KIMI-{uuid.uuid4().hex[:8].upper()}",
   212	            title="منصبُ مسبارِ p3",
   213	            institution_code=institution["code"],
   214	            authority_scope="INSTITUTION",
   215	        )
   216	    monkeypatch.setattr(type(ledger), "mark_succeeded", original)
   217	
   218	    assert caught.value.outcome.state_is_clean is True
   219	    assert caught.value.outcome.requires_human is False
   220	    before = _count(PositionModel)
   221	    national.create_position(
   222	        context=crown,
   223	        code=f"POS-KIMI-{uuid.uuid4().hex[:8].upper()}",
   224	        title="منصبُ مسبارِ p3 (سليمٌ)",
   225	        institution_code=institution["code"],
   226	        authority_scope="INSTITUTION",
   227	    )
   228	    assert _count(PositionModel) == before + 1
=== RAW [26] END ===
=== RAW [27] BEGIN ===
CMD: cd /home/user/workspace/council_w628/kimi_k3/repo && cp /home/user/workspace/council_w628/kimi_k3/probe/probe_wi107_kimi_k3.py federal/executive/services/tests/test_probe_wi107_kimi_k3.py && cd /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w628/kimi_k3/tmp/probe_seat.db ../../..//.venv/bin/python -m pytest tests/test_probe_wi107_kimi_k3.py -q
EXIT: 0
BYTES: 624
SHA256: 20b841ed0afe051655ecb305afb64575d62ad6db47d5a1e7c349cdae4aaf8a19
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w628/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 3 items

tests/test_probe_wi107_kimi_k3.py ...                                    [100%]

============================== 3 passed in 1.07s ===============================
=== RAW [27] END ===
VERDICT_PER_CRITERION:
(1) نعم — الملحقُ قبلَ الشِّفرةِ: كتلة 8 تُظهِرُ أنَّ آخِرَ ثلاثِ لمساتٍ للملحقِ والشِّفرةِ مرتَّبةٌ: الملحقُ أُودِعَ في 0b0b84b2 (قيدُ W-623 · 2026-10-23T02:23Z) وشِفرةُ الخدمةِ في f65ae2d4 (قيدُ W-625 · 2026-10-23T08:46Z) — أي التزامٌ مستقلٌّ سابقٌ (Q-61)، وكتلة 6 تؤكدُ ترتيبَ القيودِ كاملًا على المدى e7609e1..HEAD.
(2) نعم — الأسطحُ التسعةُ كلُّها تعبرُ بالفعلِ register بفاعلٍ تنفيذيٍّ مُعلَنٍ (REGISTRY_ACTOR) ومُعوِّضٍ حقيقيٍّ ومفتاحِ عمليّةٍ: كتلة 10 (فرقُ service.py كاملًا: guard_declared في الأسطحِ التسعةِ بعقدِ عبورٍ واحدٍ ومفاتيحَ طبيعيّةٍ حيثُ يتجدَّدُ النداءُ) وكتلة 13 (فحوصُ wi107 التسعةُ T1–T8+T6-ج ناجحةً: 9 passed) وكتلة 20 (الطفراتُ الخمسُ تُسقِطُ هذه الخواصَّ فيُقتَلنَ سلوكيًّا).
(3) نعم — D-4: 166 ← 157 مقيسًا بالأداةِ نفسِها في تشغيلي: كتلة 12 (مواضعُ كتابةٍ 246 · تعبرُ الحدَّ 42 · لا تعبرُ 157) وكتلة 18 (الجردانِ قبلُ 166/33/236 وبعدُ 157/42/246 متطابقانِ معَ تشغيلي) — ولا نموَّ في غيرِ الوحدةِ (توزيعُ الملفّاتِ في كتلة 12 يقابلُ جردَ «قبلُ» في كتلة 18 خارجَ national_registry).
(4) نعم — فحوصُ البندِ ناجحةٌ (كتلة 13: 9 passed) وكلُّ طفرةٍ مُعلَنةٍ تُسقِطُ فحصَها: كتلتا 19–20 حيثُ أعدتُ تشغيلَ مسبارِ الطفراتِ بنفسي: M1–M5 كلُّها «سقطَ (قُتِلَت)» والحكمُ «كلُّ الطفراتِ قُتِلَت» وبصمةُ sha256 للأصلِ بعدَ الاستعادةِ مطابقةٌ.
(5) نعم في شقِّ «بلا تعديلٍ» — كتلة 9: فرقُ الملفّاتِ الثلاثةِ القائمةِ (test_r7c · test_2b · test_wi106) بينَ e7609e1 وHEAD فارغٌ تمامًا، وحزمُ services في تشغيلي خضراءُ: wi107 ‏9 passed (كتلة 13) · test_r7c ‏35 passed (كتلة 14) · test_2b ‏53 passed (كتلة 15) · الحزمةُ الكاملةُ 1502 passed + ‏53 skipped + exit 0 (كتلة 16 — مطابقةٌ حرفيًّا للرقمِ المدوَّنِ في البند) · فحوصُ الحوكمةِ الثلاثةُ 62 passed (كتلة 24) · provenance ‏exit 0 (كتلة 25) · bootstrap --verify شاملٌ أخضرُ (كتلة 5). وأمامَ شقِّ CI: «يقرؤه المنسِّقُ ويُقيِّدُه».
(6) نعم — مراجعةٌ أعادَتِ التشغيلَ بمسبارِ المقعدِ: هذه الجولةُ، ومسباري الخاصُّ على المسارِ الإنتاجيِّ في الكتلتين 26 (الشِّفرة) و27 (التشغيل: 3 passed · exit 0).
PROBES: مسبارٌ واحدٌ — كتلةُ الشِّفرةِ 26 · كتلةُ التشغيلِ 27 (3 passed · exit 0) · الخواصُّ التي حاولَ كسرَها: (P1) إعادةُ link_principal على المفتاحِ الطبيعيِّ (المستأجر، المبدأ) بعدَ فقدانِ صفِّ الربطِ منَ القاعدةِ (DELETE مباشرٌ — تلفٌ مقصود) يجبُ أن تُرفَعَ RegistryReplayError من سجلِّ الحدِّ لا أن تنجحَ صامتةً · (P2) المبدأُ نفسُه في مستأجرٍ ثانٍ بهويةٍ أخرى يجبُ أن ينجحَ (المفتاحُ يشملُ المستأجرَ حقًّا — الرفضُ الزائفُ كانَ سيُثبِتُ الكسرَ) · (P3) فشلُ تثبيتِ النجاحِ بعدَ أثرِ الإنشاءِ على create_position (سطحٌ غيرِ المُغطَّى في T4/T5) يجبُ أن يُعوَّضَ كاملًا — **انكسرت؟ لا**: الثلاثةُ صمدَت فرفضَ الحدُّ الإعادةَ رغمَ فقدانِ الصفِّ، ونجحَ العبورُ عبرَ المستأجرَينِ، واستُعيدتِ الحالةُ نظيفةً.
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً. (ملاحظةٌ تشغيليّةٌ غيرُ حاجبة: أولُ تشغيلٍ للأمرينِ 16 و24 تلوَّثَ بوجودِ نسخةِ مسباري داخلَ دليلِ فحوصِ الخدماتِ — فرقمُ الحزمةِ ارتفعَ 3 وفحصُ الهويةِ رفضَ الملفَّ بلا ترويسةٍ؛ أزلتُ النسخةَ وأعدتُ التقاطَ الأمرينِ نفسَيهما حرفيًّا فرجعا نظيفَينِ تمامًا كما في كتلتَي 16 و24 الحاضرتينِ، وشجرةُ الاستنساخِ نظيفةٌ تحققًا بـgit status.)
ISOLATION_DECLARATION: أقرُّ أنّني لم أقرأْ شيئًا خارجَ استنساخي الخاصِّ /home/user/workspace/council_w628/kimi_k3/repo وهذهِ الإحاطةِ المنسوخةِ في دليلي — لا حزمَ منفِّذٍ ولا أحكامَ مقاعدَ أخرى: نعم، بلا أيِّ استثناءٍ.
VERDICT: PASS لكلِّ المعاييرِ (1)–(6).
