"""الهدف: حرسُ غيابِ `with_db` — شرطُ المالكِ (د-2) تحقَّقَ **أمرًا لا قراءةً**
(صفرُ ذكرٍ خارجَ التعريفِ) فحُذِفَ هو و`wrapper` من `common/database.py`
(§ 4 من A1_CD_DESIGN.md · Q-87 · W-806).

النطاق: `federal/executive/services/src/amos_federation/common/database.py`
بنيةً (AST) والشجرةُ كلُّها نصًّا — لا غيرَ: لا يُثبِتُ هذا الحرسُ أن الحذفَ كان
صوابًا (ذاك حكمُ مالكٍ مسجَّلٌ في Q-87) بل أنّه باقٍ لا يعودُ من الشبّاكِ.

المالك: governance/
تاريخ الإنشاء: 2026-11-03
تاريخ آخر تعديل: 2026-11-03

## لماذا هذا الحرسُ موجود

القرارُ حذفَ مُعاونًا عامًّا يفتحُ جلسةً ويُغلِقُها (`with_db` و`wrapper`
المتداخلةُ فيه). وبلا حرسٍ يعودُ التعريفُ — أو نداءٌ له — بصمتٍ: لا فحصًا يقيسُ
غيابَه ولا بوّابةً تُنذِر. فالغيابُ الذي تحقَّقَ أمرًا يُحرَسُ أمرًا: بنيةً في
ملفِّه ونصًّا في الشجرةِ كلِّها.

## حدُّ صدقِ هذا الحرس

بنيويٌّ: شجرةُ تحليلِ المصدرِ لملفِّ التعريفِ + بحثٌ نصّيٌّ في `federal` و`core`
و`tools` و`tests` (سابقةُ مِسبارِ W-799 نفسِه) — يستثني هذا الملفَّ وحده لأنه
يذكرُ الاسمَ ليحرُسَه. المضاعفُ الحيُّ (إعادةُ `with_db` ونداءً له) مقيسٌ في
`evidence/W-806/mutations/`.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

from tools.governance.repo_root import discover_repo_root  # noqa: E402

REPO_ROOT = discover_repo_root(__file__)
DATABASE = (
    REPO_ROOT
    / "federal"
    / "executive"
    / "services"
    / "src"
    / "amos_federation"
    / "common"
    / "database.py"
)

#: أسماءٌ يُبحَثُ عنها — النمطُ وحدُّه. `wrapper` لا يُبحثُ عنه نصًّا (اسمٌ شائعٌ
#: في الفحوص) بل يُحرَسُ بنيةً: دالّةٌ متداخلةٌ داخلَ `with_db` لا تكونُ إلّا بها.
SEARCH_PATTERN = re.compile(r"\bwith_db\b")

#: مجالاتُ البحثِ النصّيّ — سابقةُ مِسبارِ W-799 (الإنتاجُ والأدواتُ والفحوص).
SEARCH_DIRS = ("federal", "core", "tools", "tests")


def test_الملفُّ_لا_يعرِّفُ_with_db_بنيةً() -> None:
    tree = ast.parse(DATABASE.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            assert node.name != "with_db", (
                "عادَ تعريفُ with_db إلى database.py — القرارُ (د-2) لا يُنقَضُ "
                "بصمتٍ: قرارُ العَودِ للسجلِّ السياديّ لا للشِّفرة."
            )
            for decorator in node.decorator_list:
                name = ast.unparse(decorator)
                assert "with_db" not in name, (
                    f"زخرفَةٌ {name} تُعيدُ with_db من الشبّاكِ — القرارُ (د-2)."
                )
        if isinstance(node, ast.Name) and node.id == "with_db":
            raise AssertionError("اسمُ with_db عادَ إلى database.py بنيةً.")


def test_الشجرةُ_كلُّها_بلا_ذكرٍ_خارجَ_هذا_الحرسِ() -> None:
    hits: list[str] = []
    self_path = Path(__file__).resolve()
    for directory in SEARCH_DIRS:
        for path in (REPO_ROOT / directory).rglob("*.py"):
            if path.resolve() == self_path:
                continue  # هذا الحرسُ يذكرُ الاسمَ ليحرُسَه لا ليستعملَه.
            text = path.read_text(encoding="utf-8", errors="replace")
            if SEARCH_PATTERN.search(text):
                hits.append(str(path.relative_to(REPO_ROOT)))
    assert hits == [], (
        f"ذكرٌ لـ with_db خارجَ حرسِه — {hits}: الحذفَ تحقَّقَ أمرًا (صفرُ ذكرٍ "
        "خارجَ التعريفِ) ولا يُنقَضُ إلّا بقرارٍ."
    )
