# حكمُ مقعدِ المجلسِ — kimi_k3 (عائلةُ Moonshot · Kimi) · جولةُ التصميمِ الثانيةِ على WI-105 (W-590)

## التعريف
نصُّ حكمِ المقعدِ كما وردَ حرفيًّا في الجولةِ الثانيةِ لمجلسِ المراجعةِ على وثيقةِ تصميمِ J1 (بروتوكولُ Q-59 · بندُ WI-105 · المعيارُ 1) — لا تحريرَ ولا تلخيصَ. المصدرُ: ملفُّ `VERDICT.md` الذي كتبَهُ المقعدُ في دليلِهِ الخاصِّ `council_w589/kimi_k3` (§ 4.8: ملفُّ الحكمِ هو الحكمُ) — منسوخٌ آليًّا، وما بعدَ الفاصلِ بايتًا ببايتٍ (sha256 `a24bb1565ce58b5a95d4b7feacd4e335618b63ca579b3b51afb94da56c3162c5`).

## النطاق
حكمُ مقعدٍ واحدٍ على المعيارِ (1) بأشقّهِ الثلاثةِ من البندِ WI-105 بإحاطتِهِ المبصومةِ في W-589 عندَ العقدةِ `4f357aab60567d3c43d2075d1f30191d74067174` (19 أمرًا مُلتقَطًا بـ`council_raw_capture.py`).

## المالك
بندُ WI-105 (المنسِّقُ: Perplexity Computer · النموذجُ المنسِّقُ الحاضرُ GLM-5.3 (عائلةُ GLM) كما تعرضُه المنصةُ — منسِّقٌ لا مُصوِّتٌ).

## تاريخ الإنشاء
2026-10-21

## تاريخ آخر تعديل
2026-10-21 (W-590 — حفظُ الحكمِ بعدَ اكتمالِ المقاعدِ كلِّها · § 2.3)

---

MODEL: kimi_k3
FAMILY: Moonshot AI Kimi
RUN_DATE: 2026-10-21 16:20 +00:00
NODE: 4f357aab60567d3c43d2075d1f30191d74067174
CLONE_PATH: /home/user/workspace/council_w589/kimi_k3/repo
COMMANDS_RUN:
 1. cd /home/user/workspace/council_w589/kimi_k3/repo && git rev-parse HEAD
 2. cd /home/user/workspace/council_w589/kimi_k3/repo && bash tools/dev/bootstrap.sh
 3. cd /home/user/workspace/council_w589/kimi_k3/repo && git log --format='%h %cI %s' 26947961f61d9d54439569d9d005cace589a762c..HEAD
 4. cd /home/user/workspace/council_w589/kimi_k3/repo && git diff --stat 26947961f61d9d54439569d9d005cace589a762c HEAD -- federal core tools/audit
 5. cd /home/user/workspace/council_w589/kimi_k3/repo && git log --format='%h %cI %s' -- docs/audit/J1_ISSUE_RULING_DESIGN.md
 6. cd /home/user/workspace/council_w589/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
 7. cd /home/user/workspace/council_w589/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/federal_judiciary --json /home/user/workspace/council_w589/kimi_k3/tmp/judiciary.json
 8. cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n "issue_ruling" /home/user/workspace/council_w589/kimi_k3/tmp/judiciary.json
 9. cd /home/user/workspace/council_w589/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/executive_core --json /home/user/workspace/council_w589/kimi_k3/tmp/executive_core.json
 10. cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n -A8 "agent_identity.py" /home/user/workspace/council_w589/kimi_k3/tmp/executive_core.json
 11. cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n "rulings\.issue_ruling|issue_ruling\(" --type py federal/executive/services/src | rg -v "def "
 12. cd /home/user/workspace/council_w589/kimi_k3/repo && rg -c "judiciary\.issue_ruling\(" federal/executive/services/tests/test_r7d_federal_judiciary.py
 13. cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n "def guard_declared|judicial_action" federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py core/sovereignty/enforcement_boundary.py
 14. cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n "issue_ruling|KILL_SWITCH_BLOCKS" core/constitutional_engine/rules.py
 15. cd /home/user/workspace/council_w589/kimi_k3/repo && AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER=/home/user/workspace/council_w589/kimi_k3/tmp/probe_ledger.json PYTHONPATH=federal/executive/services/src:. .venv/bin/python docs/audit/evidence/W-581/probe_issue_ruling_actors.py
 16. cd /home/user/workspace/council_w589/kimi_k3/repo && PYTHONPATH=federal/executive/services/src:. .venv/bin/python docs/audit/evidence/W-582/probe_branch_exclusive_agent_system.py
 17. cd /home/user/workspace/council_w589/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w589/kimi_k3/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py -q
 18. cd /home/user/workspace/council_w589/kimi_k3/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
 19. find /home/user/workspace/council_w589/kimi_k3 -maxdepth 1
RAW_OUTPUTS:
=== RAW [1] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && git rev-parse HEAD
EXIT: 0
BYTES: 41
SHA256: 75442f2f31f65e3f38d804304b1feae30a46bafd31a771a479d1c6bf9bfdab06
NO_EOL: 0
--- OUTPUT ---
4f357aab60567d3c43d2075d1f30191d74067174
=== RAW [1] END ===
=== RAW [2] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && bash tools/dev/bootstrap.sh
EXIT: 0
BYTES: 1286
SHA256: f81d5d260bc02c90db89a02b564f007a51a9816bfa43478dab40dd72c744c9d0
NO_EOL: 0
--- OUTPUT ---
• الجذر: /home/user/workspace/council_w589/kimi_k3/repo
• ثُبِّتَ خُطّافُ pre-push (يُشغِّلُ حرسَ ما قبلَ الدفعِ على كلِّ دفعٍ — WI-078)
• إنشاءُ بيئةٍ معزولةٍ في .venv
• تركيبُ تبعيّاتِ الجذر (requirements-dev.txt)
• تركيبُ حزمةِ الخدماتِ (قد تطولُ: تبعيّاتٌ كثيرة)
• تركيبُ ruff==0.6.9 (‏المُثبَّتُ في .github/workflows/ci.yml)
✓ البيئةُ جاهزة. للتنشيطِ في جلسةٍ جديدة: source .venv/bin/activate

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
=== RAW [2] END ===
=== RAW [3] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && git log --format='%h %cI %s' 26947961f61d9d54439569d9d005cace589a762c..HEAD
EXIT: 0
BYTES: 2784
SHA256: 236c5b3b56bc6a419c787322f2318da26d8a34f1915ebc46b8e51c26840302ce
NO_EOL: 0
--- OUTPUT ---
4f357aa 2026-10-21T13:53:07Z W-588: تصحيح أثر الأسطح في تصميم J1 بالإضافة (DISC-126 · وجده مقعد grok_4_7): 220 ← 219 ⇒ 220 ← 220 في D4 و§ 4 والمعيار (3) — الدين 183 ← 181 بلا تغيير — لا شِفرة — المنسِّق Claude Opus 5.5
3791993 2026-10-21T13:51:56Z W-587: أحكام جولة المجلس على تصميم J1 (WI-105 · المعيار 1) حرفيًّا — gemini PASS · kimi PASS · grok FAIL حاجب على أسطح D4 ⇒ لا إجماع (§ 5.1) · DISC-126 · الحزمة 2703 — لا شِفرة — المنسِّق Claude Opus 5.5
d3e4ba5 2026-10-21T13:14:14Z W-586: تصحيح حمرة CI على e766840 (39604470249 · Lint E731 في سكربت قياس D-5 — المخرج لم يتغير) + DISC-125 (البوابة المحلية بلا ruff) — لا شِفرة — المنسِّق Claude Opus 5.5
e766840 2026-10-21T12:46:13Z W-585: إحاطات جولة مجلس المراجعة على تصميم J1 (WI-105 · المعيار 1) عند d6dfaee — المقاعد gemini_3_8_flash · grok_4_7 · kimi_k3 (المنسِّق Claude ⇒ § 1.5) — لا شِفرة ولا إطلاق
d6dfaee 2026-10-21T12:42:51Z W-584: تصحيح بالإضافة قبل جولة تصميم J1 — «18 نداءً» ← 15 مقيسًا (DISC-124) في الوثيقة وكتلة WI-105 — لا شِفرة — المنسِّق Claude Opus 5.5
f8c504b 2026-10-21T12:39:55Z W-583: WI-105 IN_PROGRESS → IN_REVIEW لجولة مجلس المراجعة على وثيقة تصميم J1 وحدها (المعيار 1 · § 7.4 · H3) — لا شِفرة — المنسِّق Claude Opus 5.5
3826fb4 2026-10-21T12:38:34Z W-582: استلام معلن لـWI-105 بتوجيه المالك 17 (نصه حرفيًّا) + قياس المرحلة 0 (D-4 183 · D-6 ① 13/13 · WI-082 VERIFIED) + DISC-122 (القسم د غير معاد التشغيل) + DISC-123 (D-5 بلا أمر واحد: 5/9/15) — لا شِفرة — المنسِّق Claude Opus 5.5
8210a48 2026-10-21T10:28:55Z مصفوفةُ الحقيقةِ: خرجٌ مولَّدٌ بأداتِه بعدَ تغيُّرِ الشجرة
ce4b917 2026-10-21T10:26:52Z W-581: WI-105 RESERVED → IN_PROGRESS — وثيقة تصميم J1 قبل الشِّفرة + DISC-121 (AGENT/SYSTEM 54/54) + Q-68 + ورقة D17 + حكم CI على 2694796 — لا شِفرة — المنسِّق Claude Opus 5.5
7c732ce 2026-10-21T10:25:12Z W-580: WI-105 READY → RESERVED (حتى 2026-11-20 · H3) — لا شِفرة — المنسِّق Claude Opus 5.5
fb7dadb 2026-10-21T10:24:57Z W-579: تسجيل WI-105 (J1 · issue_ruling بفاعل قضائي معلن · Q-6 ①) READY + قياس المرحلة 0 — لا شِفرة — المنسِّق Claude Opus 5.5
=== RAW [3] END ===
=== RAW [4] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && git diff --stat 26947961f61d9d54439569d9d005cace589a762c HEAD -- federal core tools/audit
EXIT: 0
BYTES: 0
SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
NO_EOL: 0
--- OUTPUT ---
=== RAW [4] END ===
=== RAW [5] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && git log --format='%h %cI %s' -- docs/audit/J1_ISSUE_RULING_DESIGN.md
EXIT: 0
BYTES: 812
SHA256: 66fa6898a9a4dde79ff799378222a7a8bdbd272e80904b95e7df6f24d504c64a
NO_EOL: 0
--- OUTPUT ---
4f357aa 2026-10-21T13:53:07Z W-588: تصحيح أثر الأسطح في تصميم J1 بالإضافة (DISC-126 · وجده مقعد grok_4_7): 220 ← 219 ⇒ 220 ← 220 في D4 و§ 4 والمعيار (3) — الدين 183 ← 181 بلا تغيير — لا شِفرة — المنسِّق Claude Opus 5.5
d6dfaee 2026-10-21T12:42:51Z W-584: تصحيح بالإضافة قبل جولة تصميم J1 — «18 نداءً» ← 15 مقيسًا (DISC-124) في الوثيقة وكتلة WI-105 — لا شِفرة — المنسِّق Claude Opus 5.5
ce4b917 2026-10-21T10:26:52Z W-581: WI-105 RESERVED → IN_PROGRESS — وثيقة تصميم J1 قبل الشِّفرة + DISC-121 (AGENT/SYSTEM 54/54) + Q-68 + ورقة D17 + حكم CI على 2694796 — لا شِفرة — المنسِّق Claude Opus 5.5
=== RAW [5] END ===
=== RAW [6] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py
EXIT: 0
BYTES: 3502
SHA256: 484053ff6f3f42fe5738e5c6e778996bd38ae55a9dbaa867ea42d35c5b244ea7
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : .
  مواضعُ كتابةٍ (كلُّها)   : 220
  عمليّاتٌ عامّةٌ مُغيِّرة   : 202
  منها تعبرُ الحدَّ        : 17
  مساراتٌ قديمةٌ مُغلَقة    : 7
  **لا تعبرُ الحدَّ**       : 183
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    core                1 /   0 /    0
    service_common     28 /   0 /   28
    services          172 /  17 /  154
    tools               1 /   0 /    1
  التوزيعُ على الملفّات:
      20  federal/executive/services/src/amos_federation/common/persistent.py
      18  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
      16  federal/executive/services/src/amos_federation/services/national_economy/service.py
      15  federal/executive/services/src/amos_federation/services/governance/federation.py
      10  federal/executive/services/src/amos_federation/services/federal_state/service.py
       9  federal/executive/services/src/amos_federation/services/governance/treasury.py
       9  federal/executive/services/src/amos_federation/services/national_registry/service.py
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
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py
       1  federal/executive/services/src/amos_federation/services/government_services/service.py
       1  tools/migrations/r4_unify_agent_identity.py
=== RAW [6] END ===
=== RAW [7] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/federal_judiciary --json /home/user/workspace/council_w589/kimi_k3/tmp/judiciary.json
EXIT: 0
BYTES: 1166
SHA256: 625c6620bfd7bf5549f71fe520973b0f137db36481a16120e391cdbe13609fb7
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : federal/executive/services/src/amos_federation/services/federal_judiciary
  مواضعُ كتابةٍ (كلُّها)   : 27
  عمليّاتٌ عامّةٌ مُغيِّرة   : 27
  منها تعبرُ الحدَّ        : 0
  مساراتٌ قديمةٌ مُغلَقة    : 0
  **لا تعبرُ الحدَّ**       : 27
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    services           27 /   0 /   27
  التوزيعُ على الملفّات:
      18  federal/executive/services/src/amos_federation/services/federal_judiciary/service.py
       5  federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py
       2  federal/executive/services/src/amos_federation/services/federal_judiciary/registry.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/enforcement.py
       1  federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py
  التفصيلُ محفوظٌ في: /home/user/workspace/council_w589/kimi_k3/tmp/judiciary.json
=== RAW [7] END ===
=== RAW [8] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n "issue_ruling" /home/user/workspace/council_w589/kimi_k3/tmp/judiciary.json
EXIT: 0
BYTES: 70
SHA256: 95a08480b7dc91eb8ddd8acc9920250642a4106367ba2f69873e2e87b21363b7
NO_EOL: 0
--- OUTPUT ---
132:   "function": "issue_ruling",
249:   "function": "issue_ruling",
=== RAW [8] END ===
=== RAW [9] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py --service federal/executive/services/src/amos_federation/services/executive_core --json /home/user/workspace/council_w589/kimi_k3/tmp/executive_core.json
EXIT: 0
BYTES: 976
SHA256: 8e799a9e2cfe28c25296e1cc88aafd2e7653a7ab581776195e89ad2c2793cc5e
NO_EOL: 0
--- OUTPUT ---
== جردُ الكتاباتِ الإنتاجيّة ==
  جذرُ القياس            : federal/executive/services/src/amos_federation/services/executive_core
  مواضعُ كتابةٍ (كلُّها)   : 11
  عمليّاتٌ عامّةٌ مُغيِّرة   : 9
  منها تعبرُ الحدَّ        : 2
  مساراتٌ قديمةٌ مُغلَقة    : 1
  **لا تعبرُ الحدَّ**       : 6
  التوزيعُ على المناطق (عامّة / سياديّة / متجاوزة):
    services            9 /   2 /    6
  التوزيعُ على الملفّات:
       3  federal/executive/services/src/amos_federation/services/executive_core/repository.py
       2  federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py
       1  federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py
  التفصيلُ محفوظٌ في: /home/user/workspace/council_w589/kimi_k3/tmp/executive_core.json
=== RAW [9] END ===
=== RAW [10] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n -A8 "agent_identity.py" /home/user/workspace/council_w589/kimi_k3/tmp/executive_core.json
EXIT: 0
BYTES: 1320
SHA256: e5964c5e6b799e45719cd7ce7b5541590d1bd39d5fd713b1d06a246fe670f7a1
NO_EOL: 0
--- OUTPUT ---
18:   "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py": 2,
19-   "federal/executive/services/src/amos_federation/services/executive_core/dispatcher.py": 1
20-  }
21- },
22- "sites": [
23-  {
24:   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
25-   "owner": "-",
26-   "function": "_apply",
27-   "ordinal": 0,
28-   "public": false,
29-   "writes": [
30-    "add()",
31-    "commit()"
32-   ],
--
38:   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
39-   "owner": "-",
40-   "function": "register_identity",
41-   "ordinal": 0,
42-   "public": true,
43-   "writes": [
44-    "add()",
45-    "commit()"
46-   ],
--
54:   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
55-   "owner": "-",
56-   "function": "set_lifecycle_state",
57-   "ordinal": 0,
58-   "public": true,
59-   "writes": [
60-    "commit()"
61-   ],
62-   "guarded": false,
--
67:   "path": "federal/executive/services/src/amos_federation/services/executive_core/agent_identity.py",
68-   "owner": "-",
69-   "function": "update_identity",
70-   "ordinal": 0,
71-   "public": true,
72-   "writes": [
73-    "commit()"
74-   ],
75-   "guarded": false,
=== RAW [10] END ===
=== RAW [11] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n "rulings\.issue_ruling|issue_ruling\(" --type py federal/executive/services/src | rg -v "def "
EXIT: 0
BYTES: 141
SHA256: 5b42c1369a396ab2e232c34e3c71acb1f2b17ee9fb19d3b0afe908cadcaaa6ca
NO_EOL: 0
--- OUTPUT ---
federal/executive/services/src/amos_federation/services/federal_judiciary/service.py:672:            row, proceeding = rulings.issue_ruling(
=== RAW [11] END ===
=== RAW [12] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && rg -c "judiciary\.issue_ruling\(" federal/executive/services/tests/test_r7d_federal_judiciary.py
EXIT: 0
BYTES: 3
SHA256: 238903180cc104ec2c5d8b3f20c5bc61b389ec0a967df8cc208cdc7cd454174f
NO_EOL: 0
--- OUTPUT ---
15
=== RAW [12] END ===
=== RAW [13] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n "def guard_declared|judicial_action" federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py core/sovereignty/enforcement_boundary.py
EXIT: 0
BYTES: 839
SHA256: a335a4cb538abff42646c92397cb825477702951916c828be9e77fa4c1826828
NO_EOL: 0
--- OUTPUT ---
core/sovereignty/enforcement_boundary.py:300:        judicial_action: JudicialAction | None = None,
core/sovereignty/enforcement_boundary.py:318:        stages.extend(self._guard_jurisdiction(request, declared_effects, judicial_action))
core/sovereignty/enforcement_boundary.py:417:        judicial_action: JudicialAction | None,
core/sovereignty/enforcement_boundary.py:425:        if is_judicial and judicial_action is None:
core/sovereignty/enforcement_boundary.py:432:        if judicial_action is None:
core/sovereignty/enforcement_boundary.py:434:        self.wall.evaluate(judicial_action)
federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:128:    def guard_declared(
federal/executive/services/src/amos_federation/services/executive_core/sovereignty_bridge.py:355:    def guard_declared(
=== RAW [13] END ===
=== RAW [14] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && rg -n "issue_ruling|KILL_SWITCH_BLOCKS" core/constitutional_engine/rules.py
EXIT: 0
BYTES: 228
SHA256: d2b87446653b74094d1d9da7fba61bccad7b410075ca918d1a9855cde1d82e2e
NO_EOL: 0
--- OUTPUT ---
33:JUDICIAL_ACTIONS = frozenset({"adjudicate", "arbitrate", "interpret_constitution", "issue_ruling"})
141:KILL_SWITCH_BLOCKS: dict[int, frozenset[str]] = {
424:        if req.action in KILL_SWITCH_BLOCKS.get(lvl, frozenset()):
=== RAW [14] END ===
=== RAW [15] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && AMOS_EXECUTIVE_IDEMPOTENCY_LEDGER=/home/user/workspace/council_w589/kimi_k3/tmp/probe_ledger.json PYTHONPATH=federal/executive/services/src:. .venv/bin/python docs/audit/evidence/W-581/probe_issue_ruling_actors.py
EXIT: 0
BYTES: 1063
SHA256: 1b6acec88bf3db22b6e0cffcf1af1f3b3f4d69335e8b301c3872e09029aab00f
NO_EOL: 0
--- OUTPUT ---
## (أ) review_only — المراجعةُ بلا تنفيذ
JUDICIAL     ALLOW  layer=FEDERAL
EXECUTIVE    DENY   layer=FEDERAL
LEGISLATIVE  DENY   layer=FEDERAL
TREASURY     DENY   layer=FEDERAL
AGENT        ALLOW  layer=AGENT
SYSTEM       ALLOW  layer=AGENT
## (ب) guard_declared عبرَ الجسرِ — بلا طلبِ اختصاصٍ (الجسرُ لا يقبلُه اليومَ)
JUDICIAL     REFUSED JurisdictionNotDeclaredError
EXECUTIVE    REFUSED JurisdictionNotDeclaredError
LEGISLATIVE  REFUSED JurisdictionNotDeclaredError
TREASURY     REFUSED JurisdictionNotDeclaredError
AGENT        REFUSED JurisdictionNotDeclaredError
SYSTEM       REFUSED JurisdictionNotDeclaredError
## (ج) الحدُّ الجوهريُّ boundary.execute بطلبِ اختصاصٍ FEDERAL/FEDERAL/FEDERAL ومُعوِّض
JUDICIAL     EXECUTED applier_called=True
EXECUTIVE    REFUSED SovereigntyViolation
LEGISLATIVE  REFUSED SovereigntyViolation
TREASURY     REFUSED SovereigntyViolation
AGENT        EXECUTED applier_called=True
SYSTEM       EXECUTED applier_called=True
=== RAW [15] END ===
=== RAW [16] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && PYTHONPATH=federal/executive/services/src:. .venv/bin/python docs/audit/evidence/W-582/probe_branch_exclusive_agent_system.py
EXIT: 0
BYTES: 1827
SHA256: 1cb1db309e4a2158a50bb5dc4a1d68cfd37021de633d44ae4d5fe8e24ff1c8c3
NO_EOL: 0
--- OUTPUT ---
## (د) review_only لكلِّ فعلٍ حصريٍّ في _BRANCH_EXCLUSIVE — الفاعلانِ AGENT وSYSTEM
legislative  amend_policy             AGENT=ALLOW SYSTEM=ALLOW
legislative  enact_policy             AGENT=ALLOW SYSTEM=ALLOW
legislative  legislate                AGENT=ALLOW SYSTEM=ALLOW
legislative  repeal_policy            AGENT=ALLOW SYSTEM=ALLOW
judicial     adjudicate               AGENT=ALLOW SYSTEM=ALLOW
judicial     arbitrate                AGENT=ALLOW SYSTEM=ALLOW
judicial     interpret_constitution   AGENT=ALLOW SYSTEM=ALLOW
judicial     issue_ruling             AGENT=ALLOW SYSTEM=ALLOW
executive    coordinate               AGENT=ALLOW SYSTEM=ALLOW
executive    dispatch_agent           AGENT=ALLOW SYSTEM=ALLOW
executive    execute_task             AGENT=ALLOW SYSTEM=ALLOW
executive    orchestrate              AGENT=ALLOW SYSTEM=ALLOW
treasury     allocate_budget          AGENT=ALLOW SYSTEM=ALLOW
treasury     allocate_funds           AGENT=ALLOW SYSTEM=ALLOW
treasury     allocate_resources       AGENT=ALLOW SYSTEM=ALLOW
treasury     authorize_expenditure    AGENT=ALLOW SYSTEM=ALLOW
treasury     award_procurement        AGENT=ALLOW SYSTEM=ALLOW
treasury     book_expense             AGENT=ALLOW SYSTEM=ALLOW
treasury     create_budget            AGENT=ALLOW SYSTEM=ALLOW
treasury     disburse_funds           AGENT=ALLOW SYSTEM=ALLOW
treasury     establish_treasury       AGENT=ALLOW SYSTEM=ALLOW
treasury     execute_transfer         AGENT=ALLOW SYSTEM=ALLOW
treasury     issue_tokens             AGENT=ALLOW SYSTEM=ALLOW
treasury     open_account             AGENT=ALLOW SYSTEM=ALLOW
treasury     post_funding             AGENT=ALLOW SYSTEM=ALLOW
treasury     reverse_transaction      AGENT=ALLOW SYSTEM=ALLOW
treasury     transfer_treasury        AGENT=ALLOW SYSTEM=ALLOW
ALLOW 54/54
=== RAW [16] END ===
=== RAW [17] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && AMOS_DATABASE_URL=sqlite:////home/user/workspace/council_w589/kimi_k3/tmp/amos_seat.db .venv/bin/python -m pytest federal/executive/services/tests/test_r7d_federal_judiciary.py -q
EXIT: 0
BYTES: 705
SHA256: 6821ffa103452a20f813eb2122aef8d7f836d22d943738b59e73081d50cb6fa2
NO_EOL: 0
--- OUTPUT ---
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /home/user/workspace/council_w589/kimi_k3/repo/federal/executive/services
configfile: pyproject.toml
plugins: platformdirs-4.13.5, cov-7.1.0, anyio-4.15.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 27 items

federal/executive/services/tests/test_r7d_federal_judiciary.py ......... [ 33%]
..................                                                       [100%]

============================== 27 passed in 4.57s ==============================
=== RAW [17] END ===
=== RAW [18] BEGIN ===
CMD: cd /home/user/workspace/council_w589/kimi_k3/repo && cat docs/audit/J1_ISSUE_RULING_DESIGN.md
EXIT: 0
BYTES: 21076
SHA256: 99eb60c6c36379722bb73adf91121ffca597401915d44acb20846a392245236f
NO_EOL: 0
--- OUTPUT ---
# J1 · WI-105 — تصميمُ عبورِ `issue_ruling` الحدَّ السياديَّ بفاعلٍ قضائيٍّ مُعلَنٍ (Q-6 ①)

<!--
الهدف: وثيقةُ تصميمِ الدفعةِ J1 من خطّةِ حرقِ D-4 — عبورُ إصدارِ الحكمِ الحدَّ السياديَّ بفاعلٍ قضائيٍّ مُعلَنٍ، تُلتزَمُ قبلَ أيِّ شِفرةٍ
النطاق: بندُ WI-105 (federal-executive · services/federal_judiciary + جسرُ executive_core) — فئةُ التغييرِ C3 (حسّاسٌ: سيادةٌ بقائمةِ Q-H)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5) — بتوجيهِ المالكِ 17 § 3 المرحلةُ 1 — لا شِفرةَ قبلَ اعتمادِ هذه الوثيقةِ
تاريخ الإنشاء: 2026-10-21
-->

> **السند:** قرارُ المالكِ **Q-6 ①** (W-363): «قضاءٌ مستقلٌّ بفاعلٍ قضائيٍّ مُعلَنٍ ← لا يخلطُ السلطاتِ ولا يحتاجُ تفويضًا لكلِّ فعلٍ» — ويفتحُ هجرةَ `federal_judiciary` «في T1 بعدَ هجرةِ Q-15» · وهجرةُ Q-15 (`WI-082`) صارت `VERIFIED` بإجماعِ المجلسِ في `W-576` · والدفعةُ في `HANDOFFS/D4-BURN-PLAN.md` باسمِ **J1**.
> **البروتوكولُ (C3):** هذه الوثيقةُ في التزامٍ يسبقُ الشِفرةَ · ثمَّ جولةُ مجلسٍ على الوثيقةِ · ثمَّ عرضُها على المالكِ · **ولا شِفرةَ قبلَ الموافقةِ** (التوجيهُ 17 § 3 · المرحلةُ 1 · البندُ 4).
> **كلُّ رقمٍ هنا مقيسٌ في W-581 على العقدةِ `2694796`** بالأمرِ المذكورِ بجانبِه — ويُعادُ قياسُه في الدفعةِ التي تُنفِّذُ.

## 1. الوضعُ المقيسُ

### 1.1 الموضعانِ في الجرد

`sovereign_write_inventory.py --service …/federal_judiciary --json` (27 موضعًا في الوحدةِ · كلُّها غيرُ محروسةٍ):

| الموضع | الكتابة | الحالة |
|---|---|---|
| `rulings.py::issue_ruling` | `add()` (صفُّ الحكمِ) ثمَّ `flush` ثمَّ `docket.record_proceeding` ثمَّ `docket.advance_case` | دَينٌ |
| `service.py::FederalJudiciary.issue_ruling` | `commit()` | دَينٌ |

قاعدةُ الأداةِ (رأسُ `sovereign_write_inventory.py`): **الموضعُ محروسٌ إن ظهرَ `guard_declared(` في جسمِ الدالّةِ العامّةِ نفسِها** — لا يكفي أن يعبرَ معاونٌ · ومعاونٌ خاصٌّ يكتبُ ولا تصلُ إليه عمليّةٌ عامّةٌ في وحدتِه يُحصى موضعًا مستقلًّا (فإعادةُ التسميةِ إلى `_` لا تُخفي شيئًا).

### 1.2 النداءات

- إنتاجيًّا: **1** — `service.py:672` يُنادي `rulings.issue_ruling` · ولا مُنادٍ آخرَ (`rg 'rulings\.issue_ruling|issue_ruling\('`).
- الاختباراتُ: **18** نداءً لـ`judiciary.issue_ruling` (الخدمة) في `tests/test_r7d_federal_judiciary.py` — منها مسارُ «الحكمُ البديلُ بعدَ الإلغاءِ» (السطورُ 1049–1075).
  - **[W-584 · 2026-10-21 · تصحيحٌ بالإضافةِ لا بالمحوِ — `DISC-124`]** المقيسُ **15** لا 18: `rg -c "judiciary\.issue_ruling\(" federal/executive/services/tests/test_r7d_federal_judiciary.py` ⇒ `15` · و`rg -c "\.issue_ruling\("` على `federal/executive/services/tests` كلِّها ⇒ ملفٌّ واحدٌ · 15 — فلا نداءَ في غيرِه. والرقمُ 18 أعلاه باقٍ تاريخًا بنِسبتِه (W-581) · ولا أثرَ له في التصميمِ: المعيارُ «test_r7d كاملًا بلا تعديلٍ» لا يتوقّفُ على العدِّ.

### 1.3 الحدُّ اليومَ — ثلاثُ حقائقَ مقيسةٍ تُغيِّرُ التصميمَ عن WI-082

مقيسةٌ بـ`docs/audit/evidence/W-581/probe_issue_ruling_actors.py` (المخرجُ كاملًا بجانبِه):

1. **الجسرُ لا يحملُ طلبَ الاختصاصِ:** `ConstitutionalAuthorizer.guard_declared` (`sovereignty_bridge.py:355`) لا يقبلُ `judicial_action` ولا يُمرِّرُه، والحدُّ الجوهريُّ `EnforcementBoundary.execute` يقبلُه (`enforcement_boundary.py:300`) ويرفضُ كلَّ فعلٍ في `JUDICIAL_ACTIONS` بلا طلبٍ (`_guard_jurisdiction` · `JurisdictionNotDeclaredError`) ⇒ **عبرَ الجسرِ اليومَ يُرفَضُ `issue_ruling` لكلِّ فاعلٍ بلا استثناءٍ (6/6)** — فلا تُهاجَرُ الدفعةُ بلا توسيعِ الجسرِ.
2. **الحكمُ عبرَ الحدِّ الجوهريِّ بطلبِ اختصاصٍ ومُعوِّضٍ:** `JUDICIAL` ⇒ تنفيذٌ · `EXECUTIVE` و`LEGISLATIVE` و`TREASURY` ⇒ `SovereigntyViolation` (A003 · الفصلُ بينَ السلطاتِ) · **و`AGENT` و`SYSTEM` ⇒ تنفيذٌ** (يُراجَعانِ في طبقةِ `AGENT` وقاعدةُ الحصرِ `_BRANCH_EXCLUSIVE` في `rules.py:272` تخصُّ الفروعَ وحدَها) — **اكتشافُ `DISC-121`** وسؤالُ `Q-68` للمالكِ · خارجَ J1 ولا تحسمُه J1.
3. **الجدارُ يعملُ:** نطاقُ محكمةٍ ≠ نطاقِ قضيّةٍ ⇒ `JurisdictionError` · ونطاقُ منصبٍ `DEPARTMENT` ⇒ `JurisdictionError` · وأثرٌ مُغيِّرٌ بلا مُعوِّضٍ ⇒ `CompensationNotDeclaredError`.

وحقيقتانِ أُخرَيانِ: `issue_ruling` **غيرُ مُدرَجٍ في أيِّ مستوًى** من `KILL_SWITCH_BLOCKS` (`rules.py:141`) · و`JUDICIAL_EFFECT_KINDS` = {CREATE · WRITE · READ} و`DELETE` في `NON_JUDICIAL_EFFECT_KINDS` («الحذفُ شأنٌ تنفيذيّ» — `jurisdiction.py:152–167`).

## 2. التصميم

### D1 · الفاعلُ القضائيُّ المُعلَنُ — ثابتٌ في الوحدةِ لا معاملٌ للمُنادي

- `federal_judiciary/rulings.py`: `JUDICIARY_ACTOR = "JUDICIAL"` ومُفوِّضٌ افتراضيٌّ كسولٌ `_judiciary_authorizer()` على مثالِ `agent_identity._default_authorizer` (WI-082).
- **فرقٌ مقصودٌ عن WI-082:** لا يُضافُ معاملٌ عامٌّ `authorizer=` إلى `rulings.issue_ruling` ولا إلى الخدمة. السببُ مقيسٌ (§ 1.3 · 2): من يملكُ أن يُمرِّرَ مُفوِّضًا بفاعلِ `AGENT` يُصدِرُ حكمًا اليومَ. فاختيارُ الفاعلِ يبقى في الوحدةِ وحدَها (نصُّ Q-6: «فاعلٌ قضائيٌّ مُعلَنٌ»).
- الاختبارُ يُبدِّلُ الفاعلَ بـ`monkeypatch` على ثابتِ الوحدةِ (ويُفرِغُ المُفوِّضَ المحفوظَ) لا بمعاملٍ إنتاجيٍّ.
- البديلُ المرفوضُ: معاملٌ اختياريٌّ كـWI-082 — يُبقي ثغرةَ `DISC-121` مفتوحةً لكلِّ مُنادٍ.

### D2 · توسيعُ الجسرِ — `judicial_action` اختياريٌّ يُمرَّرُ كما هو

- `sovereignty_bridge.py`: `guard_declared(..., judicial_action: Any | None = None)` في البروتوكولِ (`:128`) والتنفيذِ (`:355`) — ويُمرَّرُ إلى `self.boundary.execute(..., judicial_action=judicial_action)`.
- **بلا أثرٍ على غيرِ القضائيِّ:** القيمةُ الافتراضيّةُ `None` هي افتراضُ `execute` نفسِه، فكلُّ نداءٍ قائمٍ يبقى بايتًا ببايتٍ في سلوكِه — ويُثبَتُ ذلك بتشغيلِ فحوصِ WI-082 وحزمةِ الجسرِ كاملةً بلا تعديلٍ.
- لا يُخفَّفُ شيءٌ: الجسرُ لا يقرِّرُ الاختصاصَ، الجدارُ (`JudicialJurisdictionWall.evaluate`) يقرِّرُه.

### D3 · طلبُ الاختصاصِ منَ البياناتِ الحيّةِ لا من ثوابتَ

`JudicialAction(action="issue_ruling", court_scope=…, case_scope=…, actor_scope=…, target=…, institution_id=…, case_institution_id=…)`:

| الحقل | المصدر | ملاحظة |
|---|---|---|
| `court_scope` | `authority.jurisdiction` (= `court.jurisdiction`) | موجودٌ اليومَ |
| `case_scope` | `case.jurisdiction` | موجودٌ اليومَ |
| `actor_scope` | `holding.authority_scope` | **حقلٌ جديدٌ `position_scope` في `JudicialAuthority`** (إضافةٌ لا تغييرٌ — يُملأُ في `require_judicial_authority`) |
| `institution_id` | `authority.institution_id` (= `court.institution_id`) | موجودٌ |
| `case_institution_id` | `court.institution_id` | القضيّةُ بلا عمودِ مؤسّسةٍ؛ مؤسّستُها مؤسّسةُ محكمتِها (`models.py` · `LegalCaseModel`) — مُعلَنٌ لا مُخمَّنٌ |
| `is_royal_decree_target` | `False` | إصدارُ الحكمِ هنا على قضيّةٍ لا على مرسومٍ · والجدارُ يقبلُ `issue_ruling` على المرسومِ أصلًا (`jurisdiction.py:341`) |

فالفحصُ المكرَّرُ اليومَ في `authority.py` (`assert_scope_covers_court` · `assert_jurisdiction_match`) يُفحَصُ ثانيةً في الحدِّ نفسِه — ازدواجٌ مقصودٌ: الأوّلُ قاعدةُ نطاقٍ قبلَ الحدِّ، والثاني قرارُ الحدِّ.
ملاحظةٌ مقيسةٌ عرَضًا (لا تُصلَحُ في J1): `authority.py:281` يمرِّرُ `case_institution_id=court.institution_id` لا مؤسّسةَ القضيّةِ — وهو مسارٌ `pragma: no cover` ولا عمودَ للقضيّةِ أصلًا؛ يُذكَرُ ولا يُغيَّرُ.

### D4 · موضعُ العبورِ ومِلكيّةُ المعاملةِ — العبورُ حيث الكتابةُ

- **العبورُ في `rulings.issue_ruling`** (حيث يُكتَبُ الصفُّ): جسمُها يحملُ `guard_declared(` والمُطبِّقُ يُنفِّذُ `add` + `flush` + `record_proceeding` + `advance_case` **+ `session.commit()`** في معاملةٍ واحدةٍ.
- **`service.issue_ruling` يفقدُ `session.commit()`** (الالتزامُ صارَ داخلَ العبورِ) ويبقى مالكَ الجلسةِ (`session.close()` في `finally`) والنشرِ والأثرِ.
- **أثرُه في الجردِ (يُعلَنُ قبلَ القياسِ):** `rulings.issue_ruling` محروسٌ (sovereign 17 ← 18) · و`service.issue_ruling` **يخرجُ من الجردِ لأنّه لم يعدْ يكتبُ** (أسطحٌ 220 ← 219) · **D-4: 183 ← 181**. وهذا ليس تجميلًا للعدِّ: الكتابةُ الوحيدةُ للحكمِ صارت خلفَ الحدِّ، والخدمةُ مُنسِّقٌ لا كاتبٌ. **نقطةُ حكمٍ للمجلسِ.**
  - **[W-588 · 2026-10-21 · تصحيحٌ بالإضافةِ لا بالمحوِ — `DISC-126` · وجدَه مقعدُ grok_4_7 في جولةِ W-585]** «أسطحٌ 220 ← 219» **غلطٌ**: المُطبِّقُ (`_apply`) دالّةٌ متداخلةٌ خاصّةٌ داخلَ `rulings.issue_ruling` على نمطِ WI-082 (`agent_identity._apply`)، وهي تحملُ `add` + `session.commit()` فتُحصى موضعَ كتابةٍ مستقلًّا (public=False) ⇒ **أسطحٌ 220 ← 220** (‏−1 بخروجِ `service.issue_ruling` · +1 بالمُطبِّقِ) · والدَّينُ **183 ← 181** والسياديُّ **17 ← 18** على حالِهما (المُطبِّقُ غيرُ عامٍّ فلا يدخلُ مقامَ الدَّينِ) · الدليلُ `evidence/W-587/coordinator_check_grok_d4.txt`. **وشكلُ المُطبِّقِ يصيرُ جزءًا من التصميمِ لا تفصيلَ تنفيذٍ**: دالّةٌ متداخلةٌ خاصّةٌ واحدةٌ — فإن نفّذَها المنفِّذُ بغيرِ هذا الشكلِ تغيّرَ عدُّ الأسطحِ ووجبَ إعلانُه قبلَ القياسِ.
- البديلُ A2: العبورُ في الخدمةِ ويبقى `rulings.issue_ruling` عامًّا بلا عبورٍ ⇒ مدخلٌ عامٌّ يكتبُ حكمًا متجاوزًا الحدَّ (183 ← 182) — **مرفوضٌ**: الثغرةُ تبقى.
- البديلُ A3: عبورانِ متداخلانِ (الخدمةُ ثمَّ `rulings`) ⇒ قراران في سجلِّ البوابةِ ومفتاحا ذرّيّةٍ لحكمٍ واحدٍ — **مرفوضٌ**: سجلٌّ مُضلِّلٌ.

### D5 · الأثرُ المُعلَنُ — أثرٌ واحدٌ لمعاملةٍ واحدةٍ

`declared_effect("CREATE", f"judiciary/rulings/{case_id}/{stage}", "حكمٌ في المرحلة … وإجراؤه وانتقالُ القضيّةِ إلى decided")` — `CREATE` ∈ `JUDICIAL_EFFECT_KINDS` فيمرُّ `assert_effect_judicial`. الصفوفُ الثلاثةُ (الحكمُ · الإجراءُ · حالةُ القضيّةِ) تُلتزَمُ معًا أو لا يُلتزَمُ شيءٌ، فإعلانُها ثلاثةَ آثارٍ يَعِدُ بتطبيقٍ جزئيٍّ لا يقعُ.

### D6 · مفتاحُ الذرّيّةِ — بجيلِ الإلغاءِ لا بالمرحلةِ وحدَها

- `operation_key("judiciary.ruling.issue", f"{case_id}:{stage}:g{n}")` و`n` = عددُ الأحكامِ المُلغاةِ (`vacated`) للقضيّةِ في المرحلةِ — يُقرأُ قبلَ الحدِّ.
- **لماذا لا `case_id:stage`:** بعدَ الإلغاءِ يُسمَحُ حكمٌ بديلٌ للمرحلةِ نفسِها (الاختبارُ القائمُ 1069) — فمفتاحٌ بلا جيلٍ يُعيدُ الحكمَ الأوّلَ «إعادةً» ولا يكتبُ البديلَ.
- **ترتيبٌ ملزِمٌ:** فحصُ «حكمٌ قائمٌ للمرحلةِ» (`DuplicateRulingError`) يبقى **قبلَ** الحدِّ — وإلّا عادَ الطلبُ الثاني إعادةً صامتةً للأوّلِ (المفتاحُ نفسُه `g0`) بدلَ الرفضِ الذي يفرضُه الاختبارُ القائمُ (السطورُ 1055–1061).
- **الإعادةُ:** إن رجعَ الحدُّ `is_replay` يُقرأُ الحكمُ القائمُ للمرحلةِ؛ فإن غابَ رُفِعَ `RulingLedgerDivergenceError` (على مثالِ `IdentityLedgerDivergenceError` في WI-082) — لا كتابةَ ثانيةً خارجَ الحدِّ.

### D7 · المُعوِّضُ — استعادةٌ تقنيّةٌ دقيقةٌ أم إلغاءٌ قضائيٌّ؟ (نقطةُ حكمٍ)

متى يعملُ (مقيسٌ في `compensation.py:797–808`): بعدَ تسجيلِ الأثرِ «مُطبَّقًا» وفشلِ خطوةٍ لاحقةٍ (مثلًا تثبيتُ النجاحِ في سجلِّ الذرّيّةِ) — أي والصفوفُ مُلتزَمةٌ.

| الخيار | ما يفعل | له | عليه |
|---|---|---|---|
| **(أ) الاستعادةُ التقنيّةُ — التوصية** | في جلسةٍ جديدةٍ: حذفُ صفِّ الإجراءِ (آخرُ تسلسلٍ للقضيّةِ) وصفِّ الحكمِ بمعرِّفَيهما، وإرجاعُ حالةِ القضيّةِ إلى ما كانت قبلَ العمليّةِ (تُحفَظُ قبلَ الحدِّ) | الحالةُ ترجعُ كما كانت بالضبطِ (`state_is_clean`) · والعمليّةُ لم تثبتْ فلا حكمَ قانونيًّا وُجِدَ | «الحذفُ شأنٌ تنفيذيّ» — والمُعوِّضُ ليس أثرًا مُعلَنًا ولا تراجعُه البوابةُ، فيُكتَبُ ذلك في شِفرتِه صريحًا |
| (ب) الإلغاءُ القضائيُّ | `status="vacated"` بسببٍ «تعويضٌ: لم يثبتْ نجاحُ العمليّةِ» | لا حذفَ | القضيّةُ تبقى `decided` بلا حكمٍ قائمٍ — حالةٌ متناقضةٌ · ويرفعُ جيلَ المفتاحِ (D6) بحكمٍ لم يصدرْ |

### D8 · ما يبقى قبلَ الحدِّ (قراءاتٌ لا كتابات)

`require_domain_permission` · `require_tenant` · `require_judicial_authority` (PROVEN) · فحوصُ المدخلِ (المرحلة · القرار · المنطوق) · فحصُ الحكمِ القائمِ · قراءةُ جيلِ الإلغاءِ وحالةِ القضيّةِ السابقةِ. ترتيبُ الأخطاءِ المرئيُّ للمُنادي لا يتغيّرُ.

### D9 · ما لا يتغيّرُ ويُعلَنُ

- زرُّ الإيقافِ: `issue_ruling` غيرُ مُدرَجٍ في أيِّ مستوًى — لا تُضيفُه J1 (مستويات الإيقافِ قرارُ مالكٍ).
- `rules.py` و`jurisdiction.py` و`royal/`: لا مساسَ · وثغرةُ `DISC-121` لا تُصلَحُ هنا (`Q-68`).
- `vacate_ruling` (J2) · `record_proceeding` العامُّ (J3) · وبقيّةُ الوحدةِ: خارجَ J1.

## 3. الفحوصُ والطفراتُ (تُكتَبُ في الدفعةِ المنفِّذةِ)

ملفٌّ جديدٌ `federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py`:

| الفحص | يُثبِت |
|---|---|
| T1 · ALLOW للقضائيّ | الحكمُ يصدرُ عبرَ الخدمةِ · وآخرُ قرارٍ في سجلِّ البوابةِ `issue_ruling` بفاعلِ `judicial` · والصفوفُ الثلاثةُ مُلتزَمةٌ |
| T2 · DENY للتنفيذيّ | `JUDICIARY_ACTOR="EXECUTIVE"` ⇒ `SovereigntyViolation` · لا صفَّ حكمٍ · لا إجراءَ · حالةُ القضيّةِ كما كانت |
| T3 · الاختصاصُ منَ البيانات | الطلبُ المُمرَّرُ يحملُ `case.jurisdiction` و`position_scope` الحقيقيَّينِ (جاسوسٌ على `boundary.execute`) |
| T4 · البديلُ بعدَ الإلغاء | حكمٌ ← إلغاءٌ ← بديلٌ = صفّانِ بمفتاحَي `g0` و`g1` |
| T5 · المكرَّرُ قبلَ الحدّ | الطلبُ الثاني للمرحلةِ ⇒ `DuplicateRulingError` ولا قرارَ جديدٌ في سجلِّ البوابةِ |
| T6 · المُعوِّض | إسقاطُ تثبيتِ النجاحِ بعدَ الالتزامِ ⇒ `CompensationRequired` و`state_is_clean` والصفوفُ غائبةٌ وحالةُ القضيّةِ مُستعادةٌ |
| T7 · التفرُّق | إعادةٌ وصفُّ الحكمِ غائبٌ ⇒ `RulingLedgerDivergenceError` |

الطفراتُ (تُشغَّلُ على نسخةٍ مؤقّتةٍ وتُقيَّدُ مخرجاتُها):
- **M1 · حذفُ العبورِ** (المُطبِّقُ يُنادى مباشرةً بلا `guard_declared`) ⇒ يسقطُ T1 وT2 (شرطُ التوجيهِ 17).
- M2 · مفتاحٌ بلا جيلٍ ⇒ يسقطُ T4.
- M3 · فحصُ المكرَّرِ بعدَ الحدِّ ⇒ يسقطُ T5.
- M4 · `judicial_action=None` في `rulings` ⇒ يسقطُ T1 (`JurisdictionNotDeclaredError`).

## 4. معيارُ القبولِ الرقميُّ

1. `sovereign_write_inventory.py`: **debt 183 ← 181** · sovereign 17 ← 18 · أسطحٌ 220 ← 219 (**[W-588] الصحيحُ 220 ← 220** — المُطبِّقُ المتداخلُ الخاصُّ يُحصى موضعًا · `DISC-126`) · بلا نموٍّ في غيرِ الوحدةِ.
2. T1–T7 ناجحةٌ · M1–M4 كلٌّ يُسقِطُ فحصَه.
3. `test_r7d_federal_judiciary.py` كاملًا بلا تعديلٍ (18 نداءً — **[W-584] المقيسُ 15** · `DISC-124`) · وفحوصُ WI-082 والجسرِ بلا تعديلٍ.
4. حزمُ services كاملةً خضراءَ في CI مقروءًا على العقدةِ نفسِها.
5. مراجعةٌ تُعيدُ التشغيلَ (Q-H) — ولا VERIFIED بيدِ المنفِّذِ.

## 5. الملفّاتُ التي ستُمَسُّ (ولا غيرُها)

`executive_core/sovereignty_bridge.py` · `federal_judiciary/rulings.py` · `federal_judiciary/service.py` · `federal_judiciary/authority.py` · `tests/test_wi105_issue_ruling_sovereign.py` (جديد) · دعاوى عددِ الحزمةِ في `docs/PROJECT_HANDBOOK.md`.

## 6. نقاطُ الحكمِ المطلوبةُ (للمجلسِ ثمَّ للمالكِ)

| النقطة | السؤال | التوصية |
|---|---|---|
| D1 | الفاعلُ ثابتٌ في الوحدةِ بلا معاملٍ عامٍّ؟ | نعم |
| D4 | العبورُ في `rulings` والالتزامُ داخلَه فتخرجُ الخدمةُ منَ الجردِ (183 ← 181)؟ | نعم |
| D6 | المفتاحُ بجيلِ الإلغاءِ والمكرَّرُ قبلَ الحدِّ؟ | نعم |
| D7 | المُعوِّضُ (أ) الاستعادةُ التقنيّةُ أم (ب) الإلغاءُ؟ | (أ) |

لا نقطةَ منها تمسُّ سؤالًا سياديًّا غيرَ محسومٍ: الفاعلُ محسومٌ بـQ-6 ① · وثغرةُ AGENT/SYSTEM منفصلةٌ في `Q-68` ولا تعتمدُ J1 عليها.
=== RAW [18] END ===
=== RAW [19] BEGIN ===
CMD: find /home/user/workspace/council_w589/kimi_k3 -maxdepth 1
EXIT: 0
BYTES: 234
SHA256: 8e952e4a20d33b3ca37107c2bdd672958ff7e65a569af91298fa84917aa9488b
NO_EOL: 0
--- OUTPUT ---
/home/user/workspace/council_w589/kimi_k3
/home/user/workspace/council_w589/kimi_k3/repo
/home/user/workspace/council_w589/kimi_k3/tmp
/home/user/workspace/council_w589/kimi_k3/VERDICT.md
/home/user/workspace/council_w589/kimi_k3/raw
=== RAW [19] END ===
VERDICT_PER_CRITERION: (1-أ) نعم — وثيقةُ التصميمِ `docs/audit/J1_ISSUE_RULING_DESIGN.md` أُلزِمَت أوّلًا في قيدِ W-581 بعقدةِ ce4b917 قبلَ أيِّ شِفرةٍ ثم صُحِّحَت بالإضافةِ في d6dfaee (W-584) و4f357aa (W-588) (الكتلة 5) · والفارقُ عن عقدةِ القياسِ 2694796 في `federal core tools/audit` صفرٌ تمامًا (الكتلة 4 · BYTES: 0) وكلُّ القيودِ بينهما حوكمةٌ وأدلّةٌ لا شِفرةَ إنتاجيّةَ فيها (الكتلة 3) · والعقدةُ 4f357aab60567d3c43d2075d1f30191d74067174 مؤكَّدةٌ (الكتلة 1). (1-ب) نعم — وقائعُ § 1 أُعيدَت كلُّها ومطابقةٌ: الجردُ الكلّيّ 220 موضعًا · 17 سياديًّا · 183 دَينًا (الكتلة 6 كما في الوثيقةِ § 4) · والوحدةُ القضائيّةُ 27 كلُّها دَينٌ في الملفّاتِ الخمسةِ نفسِها (الكتلة 7) · والموضعانِ rulings.py::issue_ruling وservice.py::issue_ruling ظاهران (الكتلة 8) · نداءٌ إنتاجيٌّ واحدٌ service.py:672 (الكتلة 11) · الاختباراتُ 15 (DISC-124 المصوَّب في الوثيقة) (الكتلة 12) · الجسرُ بلا judicial_action والحدُّ الجوهريُّ يقبله (الكتلة 13) · issue_ruling في JUDICIAL_ACTIONS وغيرُ مُدرَجٍ في KILL_SWITCH_BLOCKS (الكتلة 14) · عبرَ الجسرِ رفضٌ لكلِّ فاعلٍ 6/6 بـJurisdictionNotDeclaredError وبطلبِ اختصاصٍ JUDICIAL ينفذُ وEXECUTIVE/LEGISLATIVE/TREASURY تُرفَض SovereigntyViolation وAGENT/SYSTEM ينفذان (الكتلة 15) · سابقةُ WI-082 في D4 مؤكَّدةٌ: المُطبِّقُ المتداخلُ _apply في agent_identity يُحصى موضعًا public=False (الكتلتان 9 و10) مع find: الاعتماديات المثبَّتة (الكتلة 2). (1-ج) نعم — نقاطُ الحكمِ D1 · D4 · D6 · D7 (§ 6 · الكتلة 18) سليمةٌ تقنيًّا: D1 (فاعلٌ ثابتٌ بلا معاملٍ عامٍّ) قائمةٌ على القياساتِ 11/13/15 وتلبّي نصَّ Q-6 ① DECIDED في السجلِّ السياديِّ · D4 (العبورُ في rulings والخدمةُ تفقد commit فتخرج من الجرد: دَينٌ 183 ← 181 · سياديٌّ 17 ← 18 · أثرُ الأسطحِ المصوَّب 220 ← 220 بموجب W-588/DISC-126) يقومُ على سابقةِ WI-082 المؤكَّدةِ في الكتلتين 9/10 وقاعدةِ الأداةِ ولا تعارضَ فيه · D6 (مفتاحٌ بجيلِ الإلغاءِ وفحصُ المكرَّرِ قبلَ الحدِّ) منسجمةٌ مع فحصِ البديلِ بعدَ الإلغاءِ القائمِ في حزمةِ test_r7d الخضراءِ كاملةً 27/27 (الكتلة 17) ومع منطقِ الذرّيّةِ · D7 (الاختيارُ بينَ استعادةٍ تقنيّةٍ وإلغاءٍ قضائيٍّ معَ تحليلِ الواقعتين) مطروحةٌ للمالكِ بنصِّه ولا تفترضُ حسمًا. ولا نقطةَ منها تمسُّ سؤالًا سياديًّا غيرَ محسومٍ: الفاعلُ محسومٌ بـQ-6 ① DECIDED (W-363) · وثغرةُ AGENT/SYSTEM سؤالٌ منفصلٌ Q-68 PENDING_OWNER في السجلِّ السياديِّ نصًّا «لا تحسمُه J1 ولا تعتمدُ عليه» وقد أُعيدَ قياسُ سلوكِها (الكتلتان 15 و16) فلا تعتمدُ J1 عليها. شِقُّ «موافقةُ المالكِ بنصِّه» لا ينطبقُ على المقعدِ (بعدَ الجولةِ) · والمعاييرُ (2)–(6) لا تنطبقُ (لا شِفرةَ قبلَ الموافقةِ — فلا VERIFIED بهذه الجولةِ).
BLOCKING_REMARKS: لا ملاحظاتٍ حاجبةً
ISOLATION_DECLARATION: نعم — أقرُّ أنّني لم أقرأْ شيئًا خارجَ استنساخي /home/user/workspace/council_w589/kimi_k3/repo وهذهِ الإحاطةِ: استنسختُ المستودعَ بنفسي عندَ العقدةِ 4f357aab60567d3c43d2075d1f30191d74067174 · وشغّلتُ الأوامرَ الـ19 بترتيبِها عبرَ أداةِ الالتقاطِ council_raw_capture.py · ولم أقرأْ تقاريرَ ولا مخرجاتِ المنفِّذِ ولا حِزَمَ evidence (والسكربتانِ في الأمرَينِ 15 و16 أداةُ قياسٍ شغّلتُهما ولم أقرأهما قراءةَ تقريرٍ) · ولا أدلّةَ جولاتٍ سابقةٍ ولا ورقةَ HANDOFFS/OWNER-DECISIONS-D17.md · ولا أيَّ ملفٍّ في /home/user/workspace/amos خارجَ الإحاطةِ نفسِها · وكلُّ ما كتبتُه داخلَ دليلي الخاصِّ وحدَه (الكتلة 19) — بلا استثناءٍ.
VERDICT: PASS
