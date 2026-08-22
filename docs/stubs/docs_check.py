# =============================================================================
# File:        docs/stubs/docs_check.py
# الهدف · Purpose: فحص هيكل التوثيق — قياسٌ من نظامِ الملفّاتِ لا من قاعدةِ بيانات
# النطاق:     قراءةُ الشجرةِ فقط: عددُ نوى NUCLEUS.md · مخطّطاتُ العقودِ ·
#             سجلّاتُ الأقاليمِ المُعلَنة. لا كتابةَ ولا حكم.
# المالك · Owner: docs/
# Created:     2026-08-15
# Last Modified: 2026-08-22 (W-026)
# Phase:       P3 (Working Nuclei)
# Article 009: هذا الملف يلتزم بالمادة 009 — الشفافية والمراجعة المستمرة.
# =============================================================================
"""
أداة فحص هيكل التوثيق (Docs Structure Check).

الهدف: قياسُ حالةِ إقليمِ التوثيقِ من **نظامِ الملفّاتِ لحظةَ النداء**. ما يُقاس:
       عددُ ملفّاتِ `NUCLEUS.md` في المستودعِ · عددُ مخطّطاتِ العقودِ في
       `docs/contracts/schemas/` · وعددُ سجلّاتِ الأقاليمِ الموجودةِ فعلًا من
       قائمةِ السجلّاتِ الاثني عشرَ المُعلَنةِ في `docs/implementation/PROGRESS_LOG.md`.
النطاق: قراءةُ الشجرةِ فقط. لا قاعدةَ بياناتٍ ولا شبكةَ ولا تبعيّةً خارجَ المكتبةِ القياسيّة.
المالك: docs/
تاريخ الإنشاء: 2026-08-15
تاريخ آخر تعديل: 2026-08-22

سببُ التغيير (W-026): كانت ترويسةُ هذا الملفِّ تقولُ «إرجاع بيانات حقيقية من
قاعدة البيانات» و«جميع البيانات مأخوذة من قاعدة بيانات Supabase» — وهو **غيرُ
صحيحٍ بالقياس**: الملفُّ لا يمسُّ قاعدةَ بياناتٍ أصلًا، بل يقرأُ نظامَ الملفّات.
وكان يحملُ `SCHEMAS = 13` و`REGISTRIES = 12` ثمَّ يقارنُهما بأنفسِهما في شرطِ
النجاح، فكانَ الشرطُ **صادقًا دائمًا** (tautology) كما في W-025. فصارَ العددانِ
يُقاسانِ من الشجرةِ، وصارَ ما تُعلِنُه الترويسةُ هو ما يفعلُه الكود.
"""

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# مسارُ مخطّطاتِ العقودِ — يُقاسُ ما فيه، ولا يُخزَّنُ عددُه.
CONTRACT_SCHEMAS_DIR = os.path.join("docs", "contracts", "schemas")

# سجلّاتُ الأقاليمِ الاثنا عشرَ **كما أُعلِنَت** في `docs/implementation/PROGRESS_LOG.md`
# (‏P1: سجلُّ الذاكرةِ + أحدَ عشرَ سجلًّا وفهرسًا). هذه **خطّةٌ مُعلَنةٌ** لا دعوى
# واقعٍ: القياسُ هو عددُ الموجودِ منها فعلًا على القرص.
DECLARED_DOMAIN_REGISTRIES = (
    "core/memory/index.md",
    "core/meta/registry.md",
    "royal/decrees.md",
    "federal/index.md",
    "states/index.md",
    "institutions/registry/index.md",
    "agents/registry/index.md",
    "tools/registry/index.md",
    "interfaces/registry.md",
    "runtime/events/index.md",
    "docs/index.md",
    "ops/index.md",
)

# الحدُّ الأدنى المُعلَنُ لعددِ النوى — شرطُ نجاحٍ مُصرَّحٌ به، لا رقمٌ مُقتبَسٌ
# عن حالةٍ سابقة. من أرادَ رفعَه رفعَه بقيدٍ في السجل.
MIN_NUCLEUS_FILES = 105


def _count_nucleus_files():
    """عُدَّ ملفّاتِ NUCLEUS.md في المستودعِ كلِّه (عدا .git) — قياسٌ لا اقتباس."""
    count = 0
    for root, dirs, files in os.walk(PROJECT_ROOT):
        if ".git" in dirs:
            dirs.remove(".git")
        if "NUCLEUS.md" in files:
            count += 1
    return count


def _count_contract_schemas():
    """عُدَّ مخطّطاتِ العقودِ الموجودةَ فعلًا في `docs/contracts/schemas/`."""
    schemas_dir = os.path.join(PROJECT_ROOT, CONTRACT_SCHEMAS_DIR)
    if not os.path.isdir(schemas_dir):
        return 0
    return sum(1 for name in os.listdir(schemas_dir) if name.endswith(".schema.json"))


def _existing_domain_registries():
    """أرجِعْ سجلّاتِ الأقاليمِ المُعلَنةَ الموجودةَ فعلًا على القرص."""
    return tuple(
        rel for rel in DECLARED_DOMAIN_REGISTRIES
        if os.path.isfile(os.path.join(PROJECT_ROOT, rel))
    )


def check():
    """شغِّلْ فحصَ هيكلِ التوثيقِ — كلُّ رقمٍ فيه مقيسٌ لحظةَ النداء.

    Returns:
        dict: domain, nucleus_files, schemas, registries, source, status.
    """
    nucleus_files = _count_nucleus_files()
    schemas = _count_contract_schemas()
    existing = _existing_domain_registries()
    missing = [rel for rel in DECLARED_DOMAIN_REGISTRIES if rel not in existing]

    ok = (
        nucleus_files >= MIN_NUCLEUS_FILES
        and schemas > 0
        and not missing
    )
    result = {
        "domain": "docs",
        "nucleus_files": nucleus_files,
        "schemas": schemas,
        "registries": len(existing),
        "source": "filesystem",
        "status": "pass" if ok else "fail",
    }
    if not ok:
        reasons = []
        if nucleus_files < MIN_NUCLEUS_FILES:
            reasons.append(f"النوى {nucleus_files} < الحدّ {MIN_NUCLEUS_FILES}")
        if schemas == 0:
            reasons.append(f"لا مخطّطاتِ عقودٍ في {CONTRACT_SCHEMAS_DIR}")
        if missing:
            reasons.append("سجلّاتٌ مُعلَنةٌ مفقودة: " + " · ".join(missing))
        result["reason"] = " | ".join(reasons)
    return result


if __name__ == "__main__":
    import json

    print(json.dumps(check(), ensure_ascii=False, indent=2))
