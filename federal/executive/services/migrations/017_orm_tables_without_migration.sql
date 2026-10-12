-- =============================================================================
-- AMOS-Federation — الهجرة 017: ثلاثةُ جداولَ دائمةٍ يُنشئُها المحرّكُ ولا تُنشئُها الهجرات
-- الهدف: أن تحويَ قاعدةٌ بُنِيَت بالهجراتِ وحدَها كلَّ جدولٍ يُعلِنُه `Base.metadata`،
--        فلا يبقى مستوى مفتاحِ الإيقافِ (`system_state`) ولا موافقاتُ الترقيةِ
--        (`promotions`) ولا سجلُّ النماذجِ (`training_models`) رهينةَ `create_all`.
-- النطاق: federal/executive/services/migrations
-- المالك: federal/executive/services
-- تاريخ الإنشاء: 2026-10-10 (WI-062 · DISC-088)
-- تعتمد على: لا شيء — الجداولُ الثلاثةُ بلا مفاتيحَ أجنبيّة
-- =============================================================================
--
-- ## ما قِيسَ (PostgreSQL 18.6 · 2026-10-10)
--
-- قاعدةٌ فارغةٌ طُبِّقَت عليها 001–016 بالترتيبِ ⇒ 62 جدولًا. وقاعدةٌ فارغةٌ بنى
-- مخطّطَها `init_db()` بعدَ استيرادِ وحداتِ الحزمةِ كلِّها ⇒ 59. والجداولُ في النموذجِ
-- بلا هجرةٍ تُنشئُها: `system_state` (W-031) · `promotions` (W-031) · `training_models`
-- (WI-055/W-216). فمن يُرحِّلُ بالـSQL (‏README: «تُنفذ تلقائيًا عند بدء PostgreSQL»)
-- لا يجدُها حتى يُقلِعَ تطبيقٌ ينادي `init_db()`.
--
-- ## لماذا هذا الشكلُ حرفًا
--
-- الـDDL أدناه هو ما يُصدِرُه SQLAlchemy نفسُه لهذه النماذجِ بلهجةِ PostgreSQL
-- (`CreateTable(..., if_not_exists=True)`)، فلا يفترقُ جدولٌ أنشأَته الهجرةُ عن جدولٍ
-- أنشأَه المحرّك: الأعمدةُ والأنواعُ والقبولُ بالفراغِ سواء. والقيمُ الافتراضيّةُ في
-- النموذجِ قيمُ بايثون لا قيمُ خادمٍ، فلا `DEFAULT` هنا — كما في `create_all`.
-- و`IF NOT EXISTS` يجعلُها **إضافةً محضةً**: قاعدةٌ أنشأَ المحرّكُ فيها الجداولَ قبلًا
-- لا يُمَسُّ فيها صفٌّ ولا عمود.
--
-- ## الرجوع
--
-- لا يُنفَّذُ تلقائيًّا: `DROP TABLE` على `system_state` يُسقِطُ مستوى الإيقافِ القائم.
-- فإن لزمَ الرجوعُ على قاعدةٍ لم يُكتَبْ فيها صفٌّ في الجداولِ الثلاثةِ:
--   DROP TABLE IF EXISTS training_models; DROP TABLE IF EXISTS promotions;
--   DROP TABLE IF EXISTS system_state;
-- وعلى قاعدةٍ فيها صفوفٌ: لا رجوعَ — فالمحرّكُ يُعيدُ إنشاءَها عندَ أوّلِ إقلاعٍ أصلًا.
-- =============================================================================

BEGIN;

CREATE TABLE IF NOT EXISTS system_state (
	id VARCHAR NOT NULL,
	level VARCHAR NOT NULL,
	reason TEXT,
	activated_at VARCHAR,
	activated_by VARCHAR,
	updated_at TIMESTAMP WITHOUT TIME ZONE,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS promotions (
	id VARCHAR NOT NULL,
	model_id VARCHAR NOT NULL,
	gates JSON,
	status VARCHAR,
	created_at VARCHAR,
	updated_at VARCHAR,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS training_models (
	id VARCHAR NOT NULL,
	model_card JSON,
	status VARCHAR,
	created_at VARCHAR,
	updated_at VARCHAR,
	PRIMARY KEY (id)
);

COMMIT;
