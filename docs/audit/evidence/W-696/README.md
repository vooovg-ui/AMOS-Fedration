# أدلّةُ دفعةِ W-696 — شِّفرةُ E1: أسطحُ executive_core الستةُ تعبرُ الحدَّ السياديَّ

## التعريف

دفعةُ شِّفرةِ WI-119 (E1) الأولى: عبورُ أسطحِ `executive_core` الستةِ
(`update_identity` · `set_lifecycle_state` · `register_agent` · `create` ·
`delete` · `compare_and_set`) الحدَّ السياديَّ بنمطِ WI-082، بتصميمِ
[`docs/audit/E1_EXECUTIVE_IDENTITY_CROSSING_DESIGN.md`](../../E1_EXECUTIVE_IDENTITY_CROSSING_DESIGN.md)
المودَعِ في W-694 وقاموسِ المالكِ الموسَّعِ **Q-73** («اعتماد تصميم E1
(13 اسمًا)» — قيدُه في `SOVEREIGN_DECISION_REGISTER.md` وورقةِ
`docs/governance/work/HANDOFFS/OWNER-DECISIONS-D26.md`). أسطحُ `agent_runtime`
الثمانيةُ تُنفَّذُ في دفعةٍ لاحقةٍ مستقلّةٍ (W-697) وفقَ انقسامِ 7+7 في التصميمِ.

وتتضمّنُ الدفعةُ واجبَ N+1 لدفعةِ W-695 (أحكامُ CI الخامّةُ على main في
[`ci/`](ci/README.md)).

## النطاق

- شِفرةُ العبورِ: `agent_identity.py` · `dispatcher.py` · `repository.py`
  (`engine.py` يكتبُ عبرَ النوى الخاصّةِ) + قاموسُ `core/constitutional_engine/rules.py`
- فحوصُ الأصنافِ الخمسةِ (§ 3): `tests/test_e1_executive_identity_crossing.py`
  (14 فحصًا) + تحديثُ وصلةِ `tests/test_executive_core.py`
- قياسُ القبولِ: `sovereign_write_inventory.py` قبلُ/بعدُ (`inventory_after_w696.json`)
- لا انتقالَ حالةٍ (WI-119 باقٍ IN_PROGRESS حتىَ W-697)

## المالك

المنسِّقُ GLM-5.3 (Perplexity Computer).

## تاريخ الإنشاء

2026-10-26 (UTC)

## تاريخ آخر تعديل

2026-10-26

## المحتويات

- `README.md` — بطاقة هوية هذا المجلد (المادة التاسعة)
- `inventory_after_w696.json` — حِملُ قياسِ D-4 الخامُّ بعدَ الشِّفرةِ (الدَّينُ 129 · السياديّةُ 51)
- `ci/` — حمولاتُ وظائفِ CI لواجبِ N+1 لدفعةِ W-695 (تشغيلُ main `40389905003` على العقدةِ `13f1edf6`)
