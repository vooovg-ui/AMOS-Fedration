-- =============================================================================
-- AMOS-Federation — الهجرة 018: مواءمةُ المخطّطِ المُرحَّلِ مع النموذجِ — التوسيعُ الذي لا يُفقِدُ شيئًا
-- الهدف: تنفيذُ قرارِ المالكِ في DISC-088 (ب) (‏2026-10-10: «ORM» — النموذجُ مصدرُ المخطّط) في
--        الشقِّ الذي لا يُفقِدُ قيمةً ولا قدرةً: أطوالُ `varchar(n)` تُرفَعُ إلى `varchar` كما يُعلِنُ
--        النموذج، و`numeric(3,2)` إلى `double precision`، و`NOT NULL` يُرفَعُ حيثُ يقبلُ النموذجُ الفراغ.
-- النطاق: federal/executive/services/migrations
-- المالك: federal/executive/services
-- تاريخ الإنشاء: 2026-10-10 (WI-064 · DISC-088 (ب))
-- تعتمد على: 001_init.sql (هي التي أنشأَت الأعمدةَ بأطوالِها وأنواعِها)
-- =============================================================================
--
-- ## ما تفعلُه — وكلُّه توسيع
--
-- 1. `varchar(n)` ⇒ `varchar`: كلُّ قيمةٍ قائمةٍ تبقى كما هي. وفي PostgreSQL لا يُعادُ
--    بناءُ الجدولِ لهذا التحويل (‏توسيعُ طولٍ إلى غيرِ محدود). والقيدُ المفقودُ هو حدُّ
--    الطولِ وحدَه — والنموذجُ (‏المصدرُ بقرارِ المالك) لا يُعلِنُه، فكانَ قاعدةً لا يراها الكود.
-- 2. `experiences.quality_score` `numeric(3,2)` ⇒ `double precision`: كلُّ قيمةٍ في
--    [-9.99, 9.99] بمنزلتَينِ تُمثَّلُ في `double` دونَ اقتطاع.
-- 3. `DROP NOT NULL` في أربعةِ أعمدةٍ يقبلُ النموذجُ فيها الفراغ: رفعُ قيدٍ لا حذفُ صفّ.
--    والقيمةُ الافتراضيّةُ في الخادم (‏`'{}'::jsonb`) **تبقى**، فالإدراجُ بالـSQL الخامِ لا يتغيّر.
--
-- ## ما لا تفعلُه — عمدًا
--
-- - **لا `jsonb` ⇒ `json` (‏13 عمودًا) ولا `timestamptz` ⇒ `timestamp` (‏9 أعمدة).** هذانِ تخفيضٌ
--   لا توسيع: الثاني يجعلُ قيمةَ الوقتِ المُخزَّنةَ تابعةً لمنطقةِ الوقتِ في الجلسة، والكودُ
--   يكتبُ `datetime.now(UTC)` واعيًا بالمنطقة. فهما معلَّقانِ لسؤالٍ مُحدَّدٍ إلى المالك
--   (‏`WI-064` · خارجَ النطاق) ولا يُخترَعُ فيهما قرار (‏الموجِّهُ § 38).
-- - **لا `DROP COLUMN` ولا `DROP TABLE`:** 11 عمودًا و6 جداولَ في الهجراتِ لا يعرفُها النموذج.
--   حذفُها هجرةٌ هدّامة، والموجِّهُ يمنعُها تلقائيًّا؛ فهي باقيةٌ ومُسمّاةٌ في حرسِ
--   `tests/test_wi064_migrations_follow_orm.py` قائمةً صريحةً لا تكبرُ بصمت.
-- - **لا تُمَسُّ القيمُ الافتراضيّةُ في الخادم.**
--
-- ## التكرار
-- كلُّ أمرٍ هنا يُعادُ بلا خطأ: `TYPE character varying` على عمودٍ صارَ `varchar` لا يفعلُ شيئًا،
-- و`DROP NOT NULL` على عمودٍ يقبلُ الفراغَ لا يفعلُ شيئًا.

ALTER TABLE agents
    ALTER COLUMN agent_type TYPE character varying,
    ALTER COLUMN domain TYPE character varying,
    ALTER COLUMN id TYPE character varying,
    ALTER COLUMN name TYPE character varying,
    ALTER COLUMN role TYPE character varying,
    ALTER COLUMN status TYPE character varying,
    ALTER COLUMN tenant_id TYPE character varying;

ALTER TABLE audit_entries
    ALTER COLUMN action TYPE character varying,
    ALTER COLUMN actor TYPE character varying,
    ALTER COLUMN hash TYPE character varying,
    ALTER COLUMN id TYPE character varying,
    ALTER COLUMN prev_hash TYPE character varying;

ALTER TABLE experiences
    ALTER COLUMN agent_id TYPE character varying,
    ALTER COLUMN id TYPE character varying,
    ALTER COLUMN model_used TYPE character varying,
    ALTER COLUMN outcome DROP NOT NULL,
    ALTER COLUMN provenance DROP NOT NULL,
    ALTER COLUMN quality_score TYPE double precision,
    ALTER COLUMN task_id TYPE character varying,
    ALTER COLUMN tenant_id TYPE character varying,
    ALTER COLUMN type TYPE character varying;

ALTER TABLE memories
    ALTER COLUMN key TYPE character varying,
    ALTER COLUMN tenant_id TYPE character varying;

ALTER TABLE reviews
    ALTER COLUMN agent_id TYPE character varying,
    ALTER COLUMN id TYPE character varying,
    ALTER COLUMN task_id TYPE character varying;

ALTER TABLE tasks
    ALTER COLUMN assigned_agent TYPE character varying,
    ALTER COLUMN domain TYPE character varying,
    ALTER COLUMN id TYPE character varying,
    ALTER COLUMN priority TYPE character varying,
    ALTER COLUMN status TYPE character varying,
    ALTER COLUMN tenant_id TYPE character varying,
    ALTER COLUMN type TYPE character varying;

ALTER TABLE tools
    ALTER COLUMN category TYPE character varying,
    ALTER COLUMN endpoint TYPE character varying,
    ALTER COLUMN id TYPE character varying,
    ALTER COLUMN input_schema DROP NOT NULL,
    ALTER COLUMN name TYPE character varying,
    ALTER COLUMN output_schema DROP NOT NULL,
    ALTER COLUMN risk_level TYPE character varying,
    ALTER COLUMN tenant_id TYPE character varying,
    ALTER COLUMN version TYPE character varying;
