-- =============================================================================
-- AMOS-Federation — الهجرة 019: تحويلُ قواعدَ بنَاها create_all إلى jsonb وtimestamptz — بعدَ التحقّقِ من UTC
-- الهدف: قاعدةٌ قائمةٌ بنَاها `Base.metadata.create_all` قبلَ WI-065 تحملُ في 22 عمودًا `json`
--        و`timestamp without time zone`. هذه الهجرةُ تُحوِّلُها إلى `jsonb` و`timestamptz` كما
--        يُعلِنُ النموذجُ الآن — **ولا تُحوِّلُ وقتًا واحدًا قبلَ أن يثبُتَ أنَّه كُتِبَ بتوقيتِ UTC**.
-- النطاق: federal/executive/services/migrations
-- المالك: federal/executive/services
-- تاريخ الإنشاء: 2026-10-10 (WI-066 · DISC-088 (ب))
-- تعتمد على: 001_init.sql أو create_all (‏الجداولُ السبعةُ موجودة) · 018 (‏لا تتعارضُ معها)
-- =============================================================================
--
-- ## القرار
--
-- المالكُ في 2026-10-10: «اكتب migration لتحويل قواعد البيانات الموجودة إلى JSONB وtimestamptz
-- بعد التحقق من UTC» — بعدَ أن أعلنَ النموذجُ النوعَين في WI-065.
--
-- ## لماذا يلزمُ التحقّق
--
-- الكودُ يكتبُ `datetime.now(UTC)`. وفي عمودِ `timestamp` بلا منطقةٍ يُحوِّلُ PostgreSQL
-- القيمةَ الواعيةَ إلى **منطقةِ الجلسةِ** ثمَّ يُسقِطُ المنطقة. والتطبيقُ لا يضبطُ منطقةً في
-- اتّصالِه، فمنطقةُ الجلسةِ هي منطقةُ الخادمِ أو تجاوزٌ على القاعدةِ/الدور. فلو لم تكن UTC
-- لكانَ `col AT TIME ZONE 'UTC'` يُزيحُ كلَّ لحظةٍ مخزَّنةٍ بفرقِ المنطقة — تحويلٌ صامتٌ خاطئ.
--
-- ## ما يُتحقَّقُ منه — وكلُّ إخفاقٍ استثناءٌ لا تخطٍّ
--
-- 1. منطقةُ جلسةِ الهجرةِ نفسِها UTC (‏`current_setting('TimeZone')`) — شُغِّلَت بإعداداتِ التطبيق.
-- 2. لا تجاوزَ لـ`TimeZone` بغيرِ UTC في `pg_db_role_setting` على هذه القاعدةِ أو أيِّ دورٍ فيها
--    (‏التطبيقُ قد يتّصلُ بدورٍ غيرِ دورِ الهجرة).
-- 3. **في البيانات:** لا قيمةَ في أيِّ عمودٍ يُحوَّلُ تقعُ في المستقبلِ إن قُرِئَت UTC (‏بسماحِ
--    5 دقائق لانحرافِ الساعة). قيمٌ كُتِبَت بمنطقةٍ شرقَ UTC (‏الرياض +03) تبدو أحدثَ صفوفِها
--    بعدَ «الآن» بساعات — وهو الأثرُ الذي يبقى في البياناتِ نفسِها.
--
-- **حدُّ ما يُثبِتُه هذا:** الإعداداتُ تشهدُ للحاضرِ والبياناتُ للأحدثِ منها؛ ولا شيءَ يُثبِتُ
-- منطقةً تغيّرَت ثمَّ عادت في الماضي. فإن عُرِفَ ذلك فلا تُشغَّلُ هذه الهجرة — يُحوَّلُ يدويًّا
-- بالمنطقةِ الصحيحة.
--
-- ## ما تفعلُه بعدَ التحقّق
--
-- لكلِّ عمودٍ من الـ22 **ما زالَ** `json` أو `timestamp without time zone` وحدَه:
--   `json` ⇒ `jsonb` بـ`USING col::jsonb` (‏تُطبَّعُ المسافاتُ وترتيبُ المفاتيح، ويبقى آخرُ مفتاحٍ مكرَّر)
--   `timestamp` ⇒ `timestamptz` بـ`USING col AT TIME ZONE 'UTC'` (‏اللحظةُ نفسُها)
-- وقاعدةٌ بنَتْها الهجراتُ (‏001 تبني `jsonb`/`timestamptz`) لا يتغيّرُ فيها شيء.
--
-- ## ما لا تفعلُه
--
-- - لا حذفَ لعمودٍ ولا لجدولٍ ولا لصفّ، ولا مساسَ بغيرِ الأعمدةِ الـ22.
-- - لا تخمينَ لمنطقةٍ غيرِ UTC، ولا بابَ تجاوزٍ للتحقّق.
-- - الكلُّ في كتلةٍ واحدة: يُلغى جميعُه إن سقطَ تحويلٌ واحد (‏مثلًا `\u0000` في `json` يرفضُه `jsonb`).
--
-- ## التكرار
-- التشغيلُ الثاني لا يجدُ عمودًا بنوعِه القديمِ فلا يفعلُ شيئًا.

DO $wi066$
DECLARE
    targets CONSTANT text[][] := ARRAY[
        ['agents', 'permissions', 'json'],
        ['agents', 'allowed_tools', 'json'],
        ['agents', 'created_at', 'ts'],
        ['agents', 'updated_at', 'ts'],
        ['tools', 'keywords', 'json'],
        ['tools', 'permissions_required', 'json'],
        ['tools', 'input_schema', 'json'],
        ['tools', 'output_schema', 'json'],
        ['tools', 'created_at', 'ts'],
        ['tasks', 'plan', 'json'],
        ['tasks', 'result', 'json'],
        ['tasks', 'created_at', 'ts'],
        ['tasks', 'updated_at', 'ts'],
        ['memories', 'keywords', 'json'],
        ['memories', 'created_at', 'ts'],
        ['experiences', 'outcome', 'json'],
        ['experiences', 'provenance', 'json'],
        ['experiences', 'created_at', 'ts'],
        ['reviews', 'criteria', 'json'],
        ['reviews', 'created_at', 'ts'],
        ['audit_entries', 'details', 'json'],
        ['audit_entries', 'created_at', 'ts']
    ];
    i int;
    tbl text;
    col text;
    kind text;
    current_type text;
    pending_ts text[] := '{}';
    pending_json text[] := '{}';
    bad_override text;
    latest timestamp;
    item text;
BEGIN
    FOR i IN 1 .. array_length(targets, 1) LOOP
        tbl := targets[i][1]; col := targets[i][2]; kind := targets[i][3];
        SELECT data_type INTO current_type
          FROM information_schema.columns
         WHERE table_schema = current_schema() AND table_name = tbl AND column_name = col;
        IF current_type IS NULL THEN
            RAISE EXCEPTION 'WI-066: العمودُ %.% غيرُ موجودٍ في المخطّط % — لا تحويلَ جزئيّ', tbl, col, current_schema();
        ELSIF kind = 'ts' AND current_type = 'timestamp without time zone' THEN
            pending_ts := pending_ts || (tbl || '.' || col);
        ELSIF kind = 'json' AND current_type = 'json' THEN
            pending_json := pending_json || (tbl || '.' || col);
        ELSIF NOT ((kind = 'ts' AND current_type = 'timestamp with time zone')
                   OR (kind = 'json' AND current_type = 'jsonb')) THEN
            RAISE EXCEPTION 'WI-066: %.% نوعُه % — لا هو القديمُ ولا الهدف', tbl, col, current_type;
        END IF;
    END LOOP;

    IF array_length(pending_ts, 1) IS NULL AND array_length(pending_json, 1) IS NULL THEN
        RAISE NOTICE 'WI-066: لا عمودَ بنوعٍ قديم — لا شيءَ يُحوَّل';
        RETURN;
    END IF;

    -- التحقّقُ من UTC — قبلَ أيِّ تعديل، ولأعمدةِ الوقتِ وحدَها حاجة؛ لكنّه يسبقُ الكلَّ عمدًا
    -- فلا تُحوَّلُ وثائقُ JSON في قاعدةٍ يُشَكُّ في أوقاتِها.
    IF array_length(pending_ts, 1) IS NOT NULL THEN
        IF current_setting('TimeZone') NOT IN ('UTC', 'Etc/UTC', 'GMT', 'Etc/GMT', 'UCT', 'Zulu') THEN
            RAISE EXCEPTION 'WI-066: منطقةُ جلسةِ الهجرةِ % لا UTC — شغِّلْها بإعداداتِ اتّصالِ التطبيق، أو حوِّلْ يدويًّا بالمنطقةِ الصحيحة', current_setting('TimeZone');
        END IF;
        SELECT string_agg(cfg, ', ') INTO bad_override
          FROM pg_db_role_setting s, unnest(s.setconfig) AS cfg
         WHERE (s.setdatabase = (SELECT oid FROM pg_database WHERE datname = current_database())
                OR s.setdatabase = 0)
           AND cfg ILIKE 'timezone=%'
           AND lower(split_part(cfg, '=', 2)) NOT IN ('utc', 'etc/utc', 'gmt', 'etc/gmt', 'uct', 'zulu');
        IF bad_override IS NOT NULL THEN
            RAISE EXCEPTION 'WI-066: تجاوزُ منطقةٍ غيرُ UTC على القاعدةِ أو دور: % — أوقاتٌ كُتِبَت به ليست UTC', bad_override;
        END IF;
        FOREACH item IN ARRAY pending_ts LOOP
            EXECUTE format('SELECT max(%I) FROM %I', split_part(item, '.', 2), split_part(item, '.', 1))
               INTO latest;
            IF latest IS NOT NULL AND (latest AT TIME ZONE 'UTC') > now() + interval '5 minutes' THEN
                RAISE EXCEPTION 'WI-066: أحدثُ قيمةٍ في % (‏%) تقعُ في المستقبلِ إن قُرِئَت UTC — كُتِبَت بمنطقةٍ أخرى؛ لا تحويل', item, latest;
            END IF;
        END LOOP;
    END IF;

    FOREACH item IN ARRAY pending_json LOOP
        EXECUTE format('ALTER TABLE %I ALTER COLUMN %I TYPE jsonb USING %I::jsonb',
                       split_part(item, '.', 1), split_part(item, '.', 2), split_part(item, '.', 2));
    END LOOP;
    FOREACH item IN ARRAY pending_ts LOOP
        EXECUTE format('ALTER TABLE %I ALTER COLUMN %I TYPE timestamptz USING %I AT TIME ZONE %L',
                       split_part(item, '.', 1), split_part(item, '.', 2), split_part(item, '.', 2), 'UTC');
    END LOOP;
    RAISE NOTICE 'WI-066: حُوِّلَ % عمودَ json و% عمودَ وقتٍ بعدَ التحقّقِ من UTC',
        coalesce(array_length(pending_json, 1), 0), coalesce(array_length(pending_ts, 1), 0);
END
$wi066$;
