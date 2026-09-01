"""الهدف: عزلُ مخرَجِ التشغيلِ عن شجرةِ المستودعِ في كلِّ تشغيلِ اختبارات.

النطاق: جذرُ المستودع — يُحمَّل تلقائيًّا قبلَ جمعِ أيِّ اختبار.
المالك: governance/
تاريخ الإنشاء: 2026-08-21
تاريخ آخر تعديل: 2026-09-01

## المشكلةُ المقيسة (O-1N-1)

`ConsumedPermitLedger` موضعُه الافتراضيُّ `royal/authority/CONSUMED_PERMITS.json`
داخلَ الشجرةِ المُتعقَّبة. وقد قيسَ فعلًا — لا افتراضًا — أنَّ
`pytest tests/sovereignty/test_supreme_authority.py` على استنساخٍ نظيفٍ يُنشئُ
ذلك الملفَّ، لأنَّ الحدَّ يُبنى فيه بسجلِّ ذرّيّةٍ في `tmp_path` وبلا سجلِّ أذون،
فيهبِطُ إلى الافتراضيّ. فحالةُ تشغيلٍ تُكتَبُ في المستودعِ نفسِه، وهو ما
تمنعُه بطاقةُ الهويّة وما يُلوِّثُ كلَّ فحصِ انحرافٍ يعتمدُ على نظافةِ الشجرة.

## القرارُ هنا

الموضعُ الافتراضيُّ **لا يُنقَل**: نقلُه تغييرُ عقدِ مرحلةٍ مغلقةٍ (1G) وقرارٌ
بشريٌّ مُعلَنٌ في `PROJECT_STATE.md`. فالمعالجةُ إعلانٌ صريحٌ في البيئةِ لمدى
التشغيلِ وحدَه: كلُّ سجلٍّ يُبنى بلا موضعٍ صريحٍ يكتبُ في مجلدٍ مؤقّتٍ خارجَ
الشجرة. والإعلانُ يُوضَع هنا — في وحدةِ `conftest` الجذريّةِ التي تُحمَّل قبلَ
الجمع — لا في مُثبِّتٍ (fixture)، لأنَّ سجلًّا قد يُبنى في زمنِ الجمعِ نفسِه.

وإن كانت البيئةُ تُعلِن موضعًا سلفًا فهو أَولى: الإعلانُ الصريحُ لا يُنقَض هنا.

## حزمةُ الخدماتِ تُرى من شجرتِها إن لم تُركَّبْ (‏`W-064` · `DISC-026`)

قِيسَ من CI لا فُرِضَ: وظيفةُ «السيادةِ الملكيّةِ» تُركِّبُ `requirements-dev.txt`
وحدَها ولا تُركِّبُ حزمةَ `federal/executive/services`، فسقطَت ثلاثةُ اختباراتٍ في
`tests/sovereignty/test_enforcement_separation.py` بـ`ModuleNotFoundError:
amos_federation` — **لم تُقَسْ فحوصُ فصلِ الإنفاذِ الفدراليِّ فيها إطلاقًا**، وكانَ
ذلك مستورًا تحتَ سقوطِ بوّابةٍ أسبقَ في الوظيفةِ نفسِها.

والعلاجُ لا يُخفِّفُ فحصًا ولا يُتخطّى به اختبارٌ: يُضافُ مُجلَّدُ المصادرِ
`federal/executive/services/src` إلى مسارِ الاستيرادِ **إن لم تكنِ الحزمةُ
مُركَّبةً** — وهو نمطُ `src-layout` المعروفُ. فتُنفَّذُ الفحوصُ الثلاثةُ حقًّا لا
تُتخطّى. وملفُّ السيرِ نفسُه محجوزٌ للمالكِ (`DISC-006`) فلا يُعالَجُ فيه.

## قاعدةُ التشغيلِ لا تُكتَبُ في الجذرِ (‏`W-087` · `WI-026` · `DISC-029`)

قِيسَ لا افتُرِض: `get_database_url()` في
`federal/executive/services/src/amos_federation/common/database.py` يهبِطُ — بلا
`AMOS_DATABASE_URL` — إلى `os.getcwd()/amos_federation.db`، وتشغيلُ الاختباراتِ
من جذرِ المستودعِ يُنشئُ الملفَّ في **الجذرِ**. والملفُّ مُستبعَدٌ بـ`*.db` في
`.gitignore` فلا يُقيَّدُ أبدًا، فبوّابةُ أسماءِ الجذرِ خضراءُ في CI (‏تقرأُ
`git ls-files`) وحمراءُ على قرصِ كلِّ مَن أعادَ التشغيلَ بـ`UNDECLARED_ROOT_FILE`
— وحمرةٌ لا تدُلُّ على عَطبٍ في المستودعِ تُعلِّمُ تطبيعَ الحمرةِ (`RK-005`).

والمعالجةُ هي معالجةُ سجلِّ الأذونِ نفسُها ولا جديدَ في نمطِها: إعلانٌ صريحٌ في
البيئةِ لمدى التشغيلِ وحدَه. والموضعُ الافتراضيُّ الإنتاجيُّ **لا يُنقَل** —
نقلُه تغييرُ عقدٍ لا عزلُ أثرٍ — ولا يُخفَّفُ حرسُ أسماءِ الجذرِ ولا يُعلَنُ
الأثرُ استثناءً فيه. وإن كانت البيئةُ تُعلِنُ رابطًا سلفًا فهو أَولى.

## لماذا اسمُ المُتغيّرِ مكتوبٌ حرفًا لا مُستورَدًا

استيرادُ `core.sovereignty.enforcement` هنا يُلزِمُ `cryptography` في **كلِّ**
تشغيلِ pytest، ومنها بوّابةُ سجلِّ الإكمالِ في CI التي تُركِّبُ `pytest` وحدَها.
فكان الاستيرادُ يُسقِطُ بوّابةً لا علاقةَ لها بالسيادةِ بـ`ModuleNotFoundError`.
والحرفُ لا يُترَك بلا حارس: `tests/governance/`
`test_runtime_state_stays_outside_the_tree.py` يُقارنُ هذا الحرفَ بالثابتِ في
الوحدةِ نفسِها، فأيُّ افتراقٍ يُسقِطُ الاختبارَ لا يمرُّ صامتًا.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

#: نسخةٌ حرفيّةٌ من `core.sovereignty.enforcement.CONSUMED_PERMITS_PATH_ENV`
#: — محروسةٌ باختبارٍ يُقارنُ الاثنين (انظر الشرحَ أعلاه).
CONSUMED_PERMITS_PATH_ENV = "AMOS_CONSUMED_PERMITS_PATH"

if not os.environ.get(CONSUMED_PERMITS_PATH_ENV, "").strip():
    موضع = Path(tempfile.mkdtemp(prefix="amos-runtime-permits-"))
    os.environ[CONSUMED_PERMITS_PATH_ENV] = str(موضع / "CONSUMED_PERMITS.json")


#: نسخةٌ حرفيّةٌ من اسمِ المُتغيّرِ الذي يقرؤه `amos_federation.common.database`
#: — محروسةٌ باختبارٍ يُقارنُ الحرفَينِ نصًّا (`W-087` · `DISC-029`). ولا
#: يُستورَدُ المصدرُ هنا: استيرادُه يُلزِمُ `sqlalchemy` في كلِّ تشغيلِ pytest،
#: ومنها بوّاباتٌ في CI لا تُركِّبُ إلّا `pytest`.
DATABASE_URL_ENV = "AMOS_DATABASE_URL"

if not os.environ.get(DATABASE_URL_ENV, "").strip():
    موضع_القاعدة = Path(tempfile.mkdtemp(prefix="amos-runtime-db-"))
    os.environ[DATABASE_URL_ENV] = f"sqlite:///{موضع_القاعدة / 'amos_federation.db'}"


#: مُجلَّدُ مصادرِ حزمةِ خدماتِ الاتحاد (`src-layout`).
SERVICES_SRC = Path(__file__).resolve().parent / "federal" / "executive" / "services" / "src"

if (SERVICES_SRC / "amos_federation").is_dir():
    import importlib.util
    import sys

    # الشرطُ مقصودٌ: الحزمةُ المُركَّبةُ أَولى، ولا يُزاحُ مسارٌ مُعلَنٌ سلفًا.
    if importlib.util.find_spec("amos_federation") is None:
        sys.path.insert(0, str(SERVICES_SRC))
