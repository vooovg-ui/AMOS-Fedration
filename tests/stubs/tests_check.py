# =============================================================================
# File:        tests/stubs/tests_check.py
# الهدف · Purpose: فحص مجال الاختبارات — قياسٌ من نظامِ الملفّاتِ لمشغّلِ الدخانِ
#             وحرّاسِ الأقاليمِ ونوى المجال
# النطاق:     قراءةُ الشجرةِ فقط. لا قاعدةَ بياناتٍ ولا شبكةَ ولا استيرادَ للمشغّل.
# المالك · Owner: tests/
# Created:     2026-08-15
# Last Modified: 2026-08-22 (W-026)
# Phase:       P3 (Working Nuclei)
# Article 009: هذا الملف يلتزم بالمادة 009 — الشفافية والمراجعة المستمرة.
# =============================================================================
"""
أداة فحص مجال الاختبارات (Tests Domain Check).

الهدف: قياسُ حالةِ إقليمِ الاختباراتِ من **نظامِ الملفّاتِ لحظةَ النداء**. ما يُقاس:
       وجودُ مشغّلِ اختباراتِ الدخان · عددُ حرّاسِ الأقاليمِ الموجودينَ فعلًا
       (`*/stubs/*_check.py`) · عددُ نوى `NUCLEUS.md` تحتَ `tests/`.
النطاق: قراءةُ الشجرةِ فقط، ولا يُستورَدُ المشغّلُ لأنّه هو من يستوردُ هذا الملفّ
       (فيقعُ دورٌ في الاستيراد). لا تبعيّةَ خارجَ المكتبةِ القياسيّة.
المالك: tests/
تاريخ الإنشاء: 2026-08-15
تاريخ آخر تعديل: 2026-08-22

سببُ التغيير (W-026): كان الملفُّ يحملُ `SMOKE_DOMAINS = 12` **رقمًا مكتوبًا**
يُعادُ في نتيجةِ الفحصِ بلا أن يُقاسَ، فكانَ يُخبِرُ عن حالةٍ لا يفحصُها — وهو
عينُ العلّةِ التي قِيسَت في W-025. صارَ العددُ يُقاسُ بعدِّ حرّاسِ الأقاليمِ
الموجودينَ على القرص، ويُقارَنُ بالحدِّ المُعلَنِ `MIN_DOMAIN_GUARDS`.
"""

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# مشغّلُ اختباراتِ الدخان — وجودُه شرطُ نجاحٍ يُفحَصُ لا يُفترَض.
SMOKE_RUNNER = os.path.join("tests", "smoke", "run_smoke_tests.py")

# الحدُّ الأدنى المُعلَنُ لعددِ حرّاسِ الأقاليم: اثنا عشرَ إقليمًا لكلٍّ حارسٌ.
# رقمٌ **مُصرَّحٌ به كشرطٍ**، والمقيسُ هو ما يُوجَدُ فعلًا على القرص.
MIN_DOMAIN_GUARDS = 12

# الحدُّ الأدنى المُعلَنُ لنوى مجالِ الاختبارات: tests · smoke · integration · e2e.
MIN_TESTS_NUCLEUS_FILES = 4


def _count_domain_guards():
    """عُدَّ حرّاسَ الأقاليمِ الموجودينَ فعلًا: `<domain>/stubs/*_check.py`."""
    count = 0
    for entry in sorted(os.listdir(PROJECT_ROOT)):
        stubs_dir = os.path.join(PROJECT_ROOT, entry, "stubs")
        if not os.path.isdir(stubs_dir):
            continue
        count += sum(
            1 for name in os.listdir(stubs_dir)
            if name.endswith("_check.py")
        )
    return count


def _count_tests_nucleus_files():
    """عُدَّ ملفّاتِ NUCLEUS.md تحتَ `tests/`."""
    count = 0
    tests_dir = os.path.join(PROJECT_ROOT, "tests")
    for _root, _dirs, files in os.walk(tests_dir):
        if "NUCLEUS.md" in files:
            count += 1
    return count


def check():
    """شغِّلْ فحصَ مجالِ الاختبارات — كلُّ رقمٍ فيه مقيسٌ لحظةَ النداء.

    Returns:
        dict: domain, smoke_domains, nucleus_files, runner, source, status
    """
    runner_ok = os.path.isfile(os.path.join(PROJECT_ROOT, SMOKE_RUNNER))
    guards = _count_domain_guards()
    nucleus_count = _count_tests_nucleus_files()

    ok = (
        runner_ok
        and guards >= MIN_DOMAIN_GUARDS
        and nucleus_count >= MIN_TESTS_NUCLEUS_FILES
    )
    result = {
        "domain": "tests",
        "smoke_domains": guards,
        "nucleus_files": nucleus_count,
        "runner": "present" if runner_ok else "missing",
        "source": "filesystem",
        "status": "pass" if ok else "fail",
    }
    if not ok:
        reasons = []
        if not runner_ok:
            reasons.append(f"مشغّلُ الدخانِ مفقود: {SMOKE_RUNNER}")
        if guards < MIN_DOMAIN_GUARDS:
            reasons.append(f"حرّاسُ الأقاليمِ {guards} < الحدّ {MIN_DOMAIN_GUARDS}")
        if nucleus_count < MIN_TESTS_NUCLEUS_FILES:
            reasons.append(f"نوى الاختباراتِ {nucleus_count} < الحدّ {MIN_TESTS_NUCLEUS_FILES}")
        result["reason"] = " | ".join(reasons)
    return result


if __name__ == "__main__":
    import json

    print(json.dumps(check(), ensure_ascii=False, indent=2))
