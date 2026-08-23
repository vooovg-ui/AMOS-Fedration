-- =============================================================================
-- AMOS-Federation — الهجرة 015: مِلكيّةُ سجلَّي الأدواتِ والوكلاءِ (Q-39 (ب) · W-032)
-- الهدف: أن يحملَ الجدولانِ المالكانِ كلَّ ما يُعلِنُه بيانُ التسجيلِ المنشورُ، بعدَ
--        أن حُوِّلَت كتابةُ `/v1/agents` و`/v1/tools` من قاموسَي ذاكرةٍ في
--        `api-gateway` إلى الخدمةِ المالكةِ الدائمة.
-- النطاق: federal/executive/services/migrations
-- المالك: federal/executive/services
-- تاريخ الإنشاء: 2026-08-23 (W-032)
-- تعتمد على: 001_init.sql (منشئُ `agents` و`tools`)
-- =============================================================================
--
-- ## بأيِّ سلطةٍ تُعدَّلُ أعمدةٌ قائمة
--
-- بنصِّ المالكِ في Q-39 (ب) بتاريخ 2026-08-23 المُقيَّدِ في
-- `docs/audit/SOVEREIGN_DECISION_REGISTER.md` § «حسمٌ سياديٌّ من المالكِ»:
-- «`tool-registry` يملكُ · `api-gateway` وسيطٌ». وتحويلُ الكتابةِ إلى المالكِ بلا
-- هذه الأعمدةِ يعني أن يُقبَلَ بيانٌ فيه `risk_level: critical` ثمَّ يُقرأَ `low` —
-- أي أن تُنقَلَ الحقيقةُ من التبخّرِ إلى التحريف. فالأعمدةُ شرطُ صحّةِ التحويلِ لا
-- زيادةٌ عليه.
--
-- ## ماذا يُفقَدُ ولا شيءَ يُمَسّ
--
-- كلُّ العباراتِ **إضافةُ عمودٍ** فقط: لا حذفَ عمودٍ، ولا تغييرَ نوعٍ، ولا حذفَ
-- صفٍّ، ولا قيدَ جديدًا على بياناتٍ قائمة. والصفوفُ الموجودةُ تأخذُ `NULL` في
-- العمودِ الجديدِ، وطبقةُ القراءةِ تُترجِمُها إلى قيمةِ العقدِ الافتراضيّةِ
-- (`1.0.0` · `low` · `{}` · `worker`) — والفرقُ مُعلَنٌ: `NULL` تعني «سُجِّلَ قبلَ
-- W-032 فلا بيانَ محفوظٌ» لا «أُعلِنَ هذا».
--
-- ## من يُطبِّقُ هذه الهجرة
--
-- من يُشغِّلُ PostgreSQL بملفّاتِ الهجرةِ يُطبِّقُها كما هي. ومن يُشغِّلُ عبرَ
-- المحرّكِ (SQLite أو PostgreSQL) فـ`init_db()` تستدعي `ensure_added_columns()`
-- في `src/amos_federation/common/database.py` فتُضيفُ **الناقصَ وحدَه** — والدالّةُ
-- والهجرةُ يُعلِنانِ نفسَ القائمةِ، وحرسُ `tests/test_w032_registry_ownership.py`
-- يُسقِطُ افتراقَهما.
-- =============================================================================

ALTER TABLE agents ADD COLUMN IF NOT EXISTS agent_type VARCHAR;
ALTER TABLE agents ADD COLUMN IF NOT EXISTS domain VARCHAR;
ALTER TABLE agents ADD COLUMN IF NOT EXISTS description TEXT;

ALTER TABLE tools ADD COLUMN IF NOT EXISTS version VARCHAR;
ALTER TABLE tools ADD COLUMN IF NOT EXISTS risk_level VARCHAR;
ALTER TABLE tools ADD COLUMN IF NOT EXISTS input_schema JSON;
ALTER TABLE tools ADD COLUMN IF NOT EXISTS output_schema JSON;
