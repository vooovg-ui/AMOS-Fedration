# إحاطةُ جولةِ مراجعةِ البندِ: WI-111 (الدفعةُ J2+J3 — أسطحُ القضاءِ المحسومةُ الخمسةَ عشرَ) — مقعدُ grok_4_7
> **الهدف:** إحاطةُ مراجعِ الجولةِ بكلِّ ما يصلُهُ — البندُ ومعاييرُهُ وأوامرُ المعاييرِ وحدودُ القراءةِ وأسئلةُ الحكمِ ومسبارُهُ الإلزاميُّ.

> **بنودٌ مساعدةٌ (ملزمةٌ):** العزلُ § 2.2 · التفاصيلُ § 2.3–2.9 · الحكمُ الفريدُ § 4.4 · التفتيتُ § 4.5 · التحقُّقُ § 4.7 · التقييدُ § 4.8 · مسبارُكَ الخاصُ § 4.9.
> **مرجعُكَ الأعلى:** [`COUNCIL_BRIEF_TEMPLATE.md`](../../../../governance/COUNCIL_BRIEF_TEMPLATE.md) (وتصحيحاتُهُ المؤرَّخةُ في [`COUNCIL_PROTOCOL.md`](../../../../governance/COUNCIL_PROTOCOL.md) § 4.9 — التوجيهُ 18 § 3 · وQ-63: لا اقتطاعَ).
> **المقاعدُ الثلاثةُ:** gemini_3_8_flash · grok_4_7 · kimi_k3 — والمنسِّقُ عندَ الإطلاقِ **Claude Opus 5.5** (لا مقعدَ من عائلةِ Claude) — جذرُ دليلِكَ الفريدُ: `/home/user/workspace/council_w641/grok_4_7/wi111` (§ 2.6).
> **الطابورُ الواحدُ (توجيهُ المستشارِ 21 § 3):** F1 (WI-106) وR1 (WI-107) وWI-084 وJ2/J3 (WI-111) تُطلَقُ بإطلاقٍ واحدٍ — وهذهِ إحاطةُ بندٍ واحدٍ منها، تُحكَمُ وحدَها.
> **تُبصَمُ sha256 في قيدِ W-641 قبلَ الإطلاقِ** — والبصماتُ في `docs/audit/evidence/W-641/briefs_wi111/SHA256SUMS`.

---

### أ · العقدةُ والمستودعُ
- المستودعُ: `vooovg-ui/AMOS-Fedration`
- **العقدةُ المرادُّ مراجعتُها (كاملةً):** رأسُ قيدِ **W-641** — التزامِ هذهِ الإحاطةِ نفسِهِ — **تُعرِّفُهُ بالأمرِ 1 أدناهُ** (`git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi111/` بعدَ الاستنساخِ) ثمَّ `git checkout` لهُ (الأمرُ 2). وهي فوقَ عقدةِ شِفرةِ J2+J3 `4247c68fea97c3bdba583f590ed5f3bda679d12e` (قيدُ W-640) بقيدٍ توثيقيٍّ وحدَه (الانتقالُ IN_PROGRESS→IN_REVIEW · الإحاطاتُ · مسبارُ الطفراتِ في evidence/W-641) — **وفرقُ الشِّفرةِ بينَ العقدتَينِ فارغٌ مقيسًا** (الأمرُ 4 ⇒ صفرُ ملفاتٍ) — فالشِّفرةُ المحكومةُ هي شِفرةُ J2+J3 نفسُها. وقاعدتُها قبلَ الشِّفرةِ main = `83994514d831d184c5fc1855ef5edc0bf777b0ad` (قيدُ W-639). والإحاطاتُ والبصماتُ موجودةٌ في الشجرةِ عندَ عقدةِ W-641 فتحقُّقُ البصمةِ يتمُّ عندَها.
- الاستنساخُ: استنسخْ المستودعَ بنفسِكَ من GitHub (استنساخًا كاملًا) إلى `/home/user/workspace/council_w641/grok_4_7/wi111/repo`، واعملْ داخلَهُ وحدَهُ.

### ب · البندُ ومعاييرُ قبولِهِ (كما كُتِبَت قبلَ التنفيذِ)

صفُّ البندِ في `docs/governance/work/ACTIVE_WORK.md` (كما هو عندَ عقدةِ المراجعةِ):

| WI-111 | federal-executive | T1 (الدفعةُ **J2+J3** — الجزءُ المحسومُ من أسطحِ `federal_judiciary` يعبرُ الحدَّ بفاعلِ الوحدةِ القضائيِّ وبأفعالِ **D17-2** المعتمدةِ (عدا الأفعالِ الأربعةِ المؤجَّلةِ · D21-أ بند 9) بنمطِ J1 · **حسّاسٌ: سيادة بقائمةِ Q-H** · فئةُ C3: ملحقُ تصميمٍ في التزامٍ يسبقُ الشِّفرةَ ثمَّ الشِّفرةُ بفحوصِها وطفراتِها ثمَّ جولةُ المجلسِ في الإطلاقِ الواحدِ (D21-هـ: «أطلقْ بعدَ J2/J3»)) | Perplexity Computer | مجلسُ المراجعةِ (بروتوكولُ المجلسِ · Q-59) — حسّاسٌ: إعادةُ تشغيلٍ وتقريرٌ حرفيٌّ ومسبارٌ لكلِّ مقعدٍ — ولا VERIFIED بيدِ المنفِّذِ (§ 4.3) | IN_REVIEW | federal/executive/services/src/amos_federation/services/federal_judiciary/service.py · federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py · federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py · core/constitutional_engine/rules.py · core/sovereignty/jurisdiction.py · docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md · docs/audit/evidence/W-638 · federal/executive/services/tests/test_wi111_judiciary_docket_sovereign.py · federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py · docs/audit/evidence/W-640 · docs/audit/evidence/W-641 | 2026-10-23 | 2026-11-21 | لا عائقَ — D17-2 محسومٌ (والأربعةُ مؤجَّلةٌ لا تعطِّلُ) | D-4: 157 ← (متوقَّعٌ 142 · إسقاطٌ — يُقاسُ بعدَ الشِّفرةِ) | — (يُكتَبُ عندَ الإغلاقِ) |

كتلةُ البندِ (كما هي عندَ عقدةِ المراجعةِ):

```text
المعرِّف: WI-111
النطاق: T1 (federal-executive · services/federal_judiciary/{service,docket,rulings}.py · ومعجمُ المُحرِّكِ core/constitutional_engine/rules.py · وجدارُ الاختصاصِ core/sovereignty/jurisdiction.py — حسّاسٌ: سيادة بقائمةِ Q-H · فئةُ C3)
المالك: Perplexity Computer (المنسِّقُ الحاضرُ Claude Opus 5.5 · بتوجيهِ المستشارِ 21 § 2)
المراجع: مجلسُ المراجعةِ (بروتوكولُ المجلسِ · Q-59) — **حسّاسٌ (سيادة · Q-H): يُعيدُ المراجعُ التشغيلَ ويحفظُ تقريرَهُ حرفيًّا ويكتبُ مسبارَهُ الخاصَّ (§ 4.9)** — ولا VERIFIED بيدِ المنفِّذِ (§ 4.3)
الحالة: IN_REVIEW   (قيدُ W-641: IN_PROGRESS→IN_REVIEW قيدًا مستقلًّا (H3) — الشِّفرةُ مُودَعةٌ في W-640 والحزمتانِ خضراوانِ مقيستَينِ (الخدماتُ 1523/53 · الجذرُ 2722/1) — والجولةُ في الطابورِ الواحدِ مع F1 وR1 وWI-084 وإحاطاتُها في evidence/W-641/briefs_wi111/) · والسابقُ (تاريخٌ لا يُمحى): IN_PROGRESS   (قيدُ W-639: RESERVED→IN_PROGRESS قيدًا مستقلًّا (H3) — انتقالٌ مستقلٌّ قبلَ الشِّفرةِ (سابقةُ W-624) — الملحقُ مُودَعٌ في W-638) · والسابقُ (تاريخٌ لا يُمحى): RESERVED   (قيدُ W-638: READY→RESERVED قيدًا مستقلًّا (H3) — ملحقُ التصميمِ مُودَعٌ في القيدِ نفسِه قبلَ الشِّفرةِ (Q-61) · وقياسُ ما قبلُ في evidence/W-638) · والسابقُ (تاريخٌ لا يُمحى): READY   (قيدُ W-636 · سندُه D17-2 المحسومُ: «تُنفَّذ الأسطح الأخرى بالأفعال المعتمدة في D17-2»)
المسارات: federal/executive/services/src/amos_federation/services/federal_judiciary/service.py · federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py · federal/executive/services/src/amos_federation/services/federal_judiciary/rulings.py · core/constitutional_engine/rules.py · core/sovereignty/jurisdiction.py · federal/executive/services/tests/test_wi111_judiciary_docket_sovereign.py (يُنشأُ معَ الشِّفرةِ) · docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md (ملحقُ التصميمِ — التزامٌ يسبقُ الشِّفرةَ) · docs/audit/evidence/W-638 · docs/audit/evidence/W-641
بدأ: 2026-10-23 · الأفق: 2026-11-21

قياسُ ما قبلُ (2026-10-23 · main = 6f3fba2 · sovereign_write_inventory.py --json): debt 157 · sovereign 42 · وفي federal_judiciary 25 سطحًا عامًّا دَينًا: 3 لـJ4 · 7 للأفعالِ الأربعةِ المؤجَّلةِ · **15 محسومةً** (رقمُ «22» في خطّةِ الحرقِ يضمُّ المؤجَّلَ — قياسٌ لا إسقاطٌ): service.{vacate_ruling, file_case, open_case, set_evidence_status, set_judge_status, close_case, assign_case, open_hearing, record_proceeding, add_party, add_claim} · docket.{open_case, record_proceeding, add_party, add_claim}

خارج النطاق: أسطحُ الأفعالِ الأربعةِ المؤجَّلةِ (submit_evidence · register_court/create_court · set_court_status · appoint_judge) · J4 (enforce_ruling_via_task · enforce_ruling_via_treasury · record_enforcement) · registry.py · models.py · authority.py · تغييرُ مَن يحقُّ له النداءُ

معيار القبول: (1) **قبلَ الشِّفرة**: الملحقُ docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md في التزامٍ يسبقُ الشِّفرةَ (Q-61) (2) الأسطحُ الخمسةَ عشرَ عابرةٌ (guard_declared( في جسدِها) أو خارجةٌ منَ العدِّ لأنَّها لا تكتبُ — بالأداةِ (3) الأفعالُ العشرةُ DENY لغيرِ القضاءِ بـR-003-1 مقيسًا (4) لا عبورَ داخلَ عبورٍ (5) الطفراتُ M1–M5 تُقتَلُ (6) الحزمةُ خضراءُ

الدليل المطلوب: الملحقُ · الجردُ قبلُ/بعدُ · مسبارُ البوّابةِ القضائيّةِ قبلُ/بعدُ · الطفراتُ — في قيدِ الدفعةِ المنفِّذةِ
```

معاييرُ القبولِ كما قُيِّدَت قبلَ العملِ (في التزامَي التسجيلِ والملحقِ W-636/W-638): الملحقُ قبلَ الشِّفرةِ (Q-61) · الأسطحُ الخمسةَ عشرَ عابرةٌ أو خارجةٌ منَ العدِّ لأنّها لا تكتبُ — بالأداةِ · الأفعالُ العشرةُ DENY لغيرِ القضاءِ بـR-003-1 مقيسًا · لا عبورَ داخلَ عبورٍ · الطفراتُ M1–M5 تُقتَلُ · الحزمةُ خضراءُ.

**إفصاحاتُ المنفِّذِ (تُحكَمُ لا تُسلَّمُ):** (1) مسبارُ البوّابةِ القضائيّةِ (`judicial_gate_probe.py`) لا يحملُ في قائمتِه الفعلَينِ `join_party` و`admit_claim` — فيقيسُ ثمانيةً منَ العشرةِ، والاثنانِ مقيسانِ بالفحصِ T1 المُعلْمَنِ على العشرةِ في `test_wi111_judiciary_docket_sovereign.py`. (2) الجردُ يَعُدُّ السياديَّ 42 ← 46 لا 53 لأنّه أعمى عنِ التفويضِ (الخدماتُ المُنسِّقةُ تُفوِّضُ ولا تكتبُ) — مشروحٌ في الملحقِ § 7 وDISC-132. (3) فحصُ J1 `test_wi105_issue_ruling_sovereign.py` **عُدِّلَ** في W-640: مساعدٌ `_ruling_results` يُرشِّحُ نتائجَ سجلِّ الحدِّ بالفعلِ `issue_ruling` — لأنَّ سطوحَ J2+J3 تُضيفُ قيودًا أخرى في السجلِّ نفسِه؛ فالتعديلُ مُعلَنٌ ويُحكَمُ عليه بالأمرِ 9 (هل أضعفَ الفحصَ؟). (4) `set_judge_status` يُكرِّرُ فحوصَ السجلِّ قبلَ العبورِ (مُعلَنٌ في الملحقِ).

### ج · أوامرُ المعاييرِ (منَ البندِ نفسِهِ)

1. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi111/`
2. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git checkout $(git log -1 --format=%H origin/main -- docs/audit/evidence/W-641/briefs_wi111/)`
3. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git rev-parse HEAD`
4. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff --stat 4247c68fea97c3bdba583f590ed5f3bda679d12e HEAD -- federal/ tools/ tests/ agents/ core/ src/`
5. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && bash tools/dev/bootstrap.sh --verify`
6. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log --format='%h %cI %s' 83994514d831d184c5fc1855ef5edc0bf777b0ad..HEAD --max-count=30`
7. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git log --format='%h %cI %s' -4 -- docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md federal/executive/services/src/amos_federation/services/federal_judiciary/docket.py`
8. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff 83994514d831d184c5fc1855ef5edc0bf777b0ad 4247c68fea97c3bdba583f590ed5f3bda679d12e -- federal/executive/services/src/amos_federation/services/federal_judiciary/ core/constitutional_engine/rules.py core/sovereignty/jurisdiction.py`
9. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && git diff 83994514d831d184c5fc1855ef5edc0bf777b0ad 4247c68fea97c3bdba583f590ed5f3bda679d12e -- federal/executive/services/tests/test_wi105_issue_ruling_sovereign.py federal/executive/services/tests/test_r7d_federal_judiciary.py`
10. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat federal/executive/services/tests/test_wi111_judiciary_docket_sovereign.py`
11. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/audit/sovereign_write_inventory.py`
12. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi111_judiciary_docket_sovereign.py -q`
13. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests/test_wi105_issue_ruling_sovereign.py tests/test_r7d_federal_judiciary.py -q`
14. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo/federal/executive/services && ../../..//.venv/bin/python -m pytest tests -q`
15. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/audit/judicial_gate_probe.py`
16. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/J2J3_JUDICIARY_DOCKET_DESIGN.md`
17. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-638/inventory_before_wi111.txt docs/audit/evidence/W-640/inventory_after_wi111.txt`
18. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-641/mutation_probe_wi111.py.txt`
19. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python docs/audit/evidence/W-641/mutation_probe_wi111.py.txt`
20. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && rg -n "D17-2|Q-61" docs/audit/SOVEREIGN_DECISION_REGISTER.md`
21. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && sha256sum docs/audit/evidence/W-641/briefs_wi111/briefing_grok_4_7.md`
22. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && cat docs/audit/evidence/W-641/briefs_wi111/SHA256SUMS`
23. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python -m pytest tests/governance/test_q3_branch_declaration_surface.py tests/governance/test_w120_suite_size_claims.py tests/governance/test_identity_law.py tests/governance/test_step7_factory_surfaces.py -q`
24. `cd /home/user/workspace/council_w641/grok_4_7/wi111/repo && .venv/bin/python tools/governance/measurement_provenance.py . --check --without-deps`

### د · حدودُ قراءتِكَ (مصادرُ المعاييرِ وحدَها)
- البندُ: `docs/governance/work/ACTIVE_WORK.md` (صفُّهُ وكتلتُهُ)
- هذا القالبُ المعبَّأُ
- القراراتُ المرتبطةُ في `docs/audit/SOVEREIGN_DECISION_REGISTER.md` (Q-###)
- **ولا يُطلَبُ منكَ قراءةُ أدلّةِ المنفِّذِ ولا حزمِهِ — احكمْ من إعادةِ تشغيلِكَ أنتَ.**

### هـ · أسئلةُ الحكمِ (أجِب عن كلٍّ منها بمخرجاتٍ خامّةٍ ورموزِ خروجٍ)
1. هل استنسختَ المستودعَ بنفسِكَ عندَ العقدةِ أعلاهُ؟ أعدِدْ مسارَ استنساخِكَ وأمرَ الاستنساخِ.
2. عن كلِّ أمرٍ في (ج): شغِّلْهُ كما هو **عبرَ أداةِ الالتقاطِ** (`.venv/bin/python tools/governance/council_raw_capture.py --n <رقم> --out <دليلُك>/raw/<رقم>.txt '<الأمرُ حرفيًّا>'`)، وضَعْ كتلتَهُ في جوابِكَ كما هي — **المخرجُ كلُّهُ بلا اقتطاعٍ ولا اختصارٍ ولا وصفٍ ولا إعادةِ كتابةٍ، مهما طالَ** (البروتوكولُ § 4.5).
3. عن كلِّ معيارِ قبولٍ في (ب): هل تحقَّقَ في تشغيلِكَ أنتَ؟ نعم/لا — وبالدليلِ.
4. أقرُّ أنّكَ لم تقرأْ شيئًا خارجَ استنساخِكَ وهذهِ الإحاطةِ: نعم/لا (مع بيانِ أيِّ استثناءٍ).
5. ملاحظاتٌ حاجبةٌ إن وُجدَت — وإن لم توجدْ فاكتبْ «لا ملاحظاتٍ حاجبةً».
6. **مسبارُكَ الخاصُّ (إلزاميٌّ في جولاتِ C3 · البروتوكولُ § 4.9):** اكتبْ مسبارًا واحدًا على الأقلِّ **من عندِكَ** — لا أمرًا من (ج) ولا نسخةً من فحصٍ قائمٍ — يُنادي **المسارَ الإنتاجيَّ** (`FederalJudiciaryService` وأسطحُ `docket`/`rulings`) ويحاولُ **كسرَ الخاصيّةِ المُدَّعاةِ** في (ب) (مثلًا: سطحٌ منَ الخمسةَ عشرَ يكتبُ بلا عبورٍ للحدِّ · فاعلٌ تنفيذيٌّ أو تشريعيٌّ يمرُّ بفعلٍ منَ العشرةِ · عبورٌ داخلَ عبورٍ · كتابةٌ فاشلةٌ لا تُعوَّضُ · إعادةٌ تُعيدُ نجاحًا لقضيّةٍ محذوفةٍ · فعلٌ مؤجَّلٌ دخلَ المعجمَ). احفظْه في دليلِكَ تحتَ `probe/`، واعرضْ شِفرتَه بأمرٍ مُلتقَطٍ (`nl -ba <المسار>`) وشغِّلْه بأمرٍ مُلتقَطٍ آخرَ عبرَ أداةِ الالتقاطِ، وأدرِجِ الأمرَينِ في `COMMANDS_RUN` وكتلتَيهما في `RAW_OUTPUTS` كاملتَين. **حكمُ PASS بلا مسبارٍ لا يُحتسَبُ.** ومسبارٌ كسرَ الخاصيّةَ ملاحظةٌ حاجبةٌ.

### و · صيغةُ جوابِكَ (يُحفظُ حرفيًّا بلا تحريرٍ)
```
MODEL: <اسمُ النموذجِ كما أعلنتْهُ المنصةُ>
FAMILY: <العائلةُ>
RUN_DATE: <YYYY-MM-DD HH:MM +00:00>
NODE: <sha>
CLONE_PATH: <المسارُ>
COMMANDS_RUN:
 1. <الأمرُ حرفيًّا كما في سطرِ CMD من كتلتِهِ>
 2. …
RAW_OUTPUTS:
<كتلُ RAW كما كتبتْها أداةُ الالتقاطِ — متتاليةً بلا أيِّ نصٍّ بينها:>
=== RAW [1] BEGIN ===
CMD: <الأمر>
EXIT: <رمزُ الخروج>
BYTES: <عدد>
SHA256: <بصمة>
NO_EOL: <0|1>
--- OUTPUT ---
<المخرجُ كلُّهُ>
=== RAW [1] END ===
VERDICT_PER_CRITERION: <معيارٌ ← نعم/لا + الدليلُ>
PROBES: <لكلِّ مسبارٍ: رقمُ كتلةِ شِفرتِه · رقمُ كتلةِ تشغيلِه · الخاصيّةُ التي حاولَ كسرَها · انكسرت؟ نعم/لا>
BLOCKING_REMARKS: <أو «لا ملاحظاتٍ حاجبةً»>
ISOLATION_DECLARATION: <الإقرار>
VERDICT: <PASS لكلِّ المعاييرِ · أو FAIL بسببٍ مسمًّى>
```

> **تذكيرٌ للمراجعِ (منَ البروتوكولِ):** حكمٌ بلا تشغيلٍ فعليٍّ باطلٌ · والمخرجاتُ تُعادُ خامًا **كاملةً** برموزِ خروجِها — **ممنوعٌ الاقتطاعُ والاختصارُ و«المقاطعُ المفتاحيّةُ» والوصفُ النثريُّ للمخرجِ وإعادةُ كتابتُه (§ 4.5)** · وحكمُكَ يُفحَصُ آليًّا بـ`tools/governance/council_verdict_raw_check.py` ولا يُحتسَبُ إن رُفِضَ (§ 4.7) · وحكمُ PASS بلا مسبارٍ خاصٍّ على المسارِ الإنتاجيِّ لا يُحتسَبُ (§ 4.9) · وملفُّ حكمِكَ في دليلِكَ يُحفَظُ حرفيًّا في المستودعِ (§ 4.8).
