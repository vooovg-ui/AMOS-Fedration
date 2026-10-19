"""حاصدُ الطفراتِ الثماني — WI-096 § 3 (يعمل من المستودع · يعيدُ الملفَ دائمًا).

الهدف: إثباتٌ قابلٌ لإعادةِ التشغيلِ من المستودعِ أنَّ فحوصَ WI-096 تقتلُ
الطفراتِ الثماني المُعلَنةَ في وثيقةِ التصميمِ § 3 — لا صدفةَ تحرسُ الخصائصَ.
النطاق: core/sovereignty/idempotency.py · الوثيقةُ DISC105_IDEMPOTENCY_APPEND_DESIGN.md § 3.
المالك: Perplexity Computer (WI-096 · التوجيهُ 12 § 2 المأذونُ مسبقًا).

التشغيلُ: .venv/bin/python docs/audit/evidence/W-471/mutation_harness.py
قاعدةُ القتلِ (تصحيحُ مراجعةِ المستشارِ الثانيةِ · W-489 § 3): الطفرةُ مقتولةٌ
إن **سقطَ فحصٌ** — أي: خروجُ pytest بفشلِ فحوصٍ (failed > 0 في الملخصِ)
**بلا أخطاءِ جمعٍ أو تهيئةٍ** (error/collected-error ليسَ حكمَ الفحوصِ) —
وقبلهَا جولةٌ خضراءُ موثَّقةٌ على الشِفرةِ غيرِ المطفَّرةِ (خطُ الأساسِ).
ملاحظةُ حملٍّ موثَّقةٌ: تصحيحُ `_retry_flow` في W-477 (المعاملُ `events-3` ←
`events`) غيَّرَ **حملَ الاختبارِ نفسَهُ** لا تعليقَهُ فقط: كلُّ مفتاحٍ صارَ
يُنتجُ 3+2×`events` حدثًا بدلَ `events` — وهذا موثَّقٌ في القيدِ نفسِهِ.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
MODULE = REPO / 'core/sovereignty/idempotency.py'
TESTS = [
    'tests/sovereignty/test_idempotency_append_log.py',
    'tests/sovereignty/test_idempotency.py',
]
OUT_DIR = REPO / 'docs/audit/evidence/W-471/mutation_runs'

#: أسماءُ ملفاتِ المخارجِ ASCII قسرًا: git يقتبسُ المساراتِ غيرَ ASCII في مخرجاتِ
#: الفروقِ (quotepath) فلا تطابقُ الحارسُ حجزًا لها (اكتشافٌ W-489) — الأسماءُ
#: الموصوفةُ العربيةُ تُطبَّعُ هنا إلى M1…M8 والوصفُ في mutation_kills.json.
OUT_NAMES = {
    'M1_حذف_flock': 'M1_no_flock',
    'M2_فتح_بوضع_w_يمحو': 'M2_open_w_wipes',
    'M3_قراءة_الذيل_الممزق_كاملًا': 'M3_torn_tail_as_line',
    'M4_حذف_فحص_البصمة': 'M4_no_fingerprint_check',
    'M5_تعطيل_الضغط': 'M5_no_compaction',
    'M6_الضغط_يُسقِط_المفاتيح': 'M6_compaction_drops_keys',
    'M7_الترحيل_يُفرِغُ_المحتوى_القديم': 'M7_migration_empties',
    'M8_إلحاق_بلا_تحديثِ_الذاكرةِ': 'M8_no_memory_update',
}

MUTATIONS = {
    'M1_حذف_flock': (
        'fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)', 'pass'),
    'M2_فتح_بوضع_w_يمحو': (
        'open(self.path, "a", encoding="utf-8", newline="\\n")',
        'open(self.path, "w", encoding="utf-8", newline="\\n")'),
    'M3_قراءة_الذيل_الممزق_كاملًا': (
        'break  # ذيلٌ ممزّقٌ',
        'position += len(raw_line) + 1  # M3 ذيلٌ ممزّق'),
    'M4_حذف_فحص_البصمة': (
        'if record.fingerprint != fingerprint:', 'if False:'),
    'M5_تعطيل_الضغط': (
        'if self._lines < COMPACTION_MIN_LINES or self._lines < COMPACTION_FACTOR * live:',
        'if True:'),
    'M6_الضغط_يُسقِط_المفاتيح': (
        'tmp = self._write_snapshot_file(self._state)',
        'tmp = self._write_snapshot_file({})'),
    'M7_الترحيل_يُفرِغُ_المحتوى_القديم': (
        'legacy = strip_identity(raw)', 'legacy = {}'),
    'M8_إلحاق_بلا_تحديثِ_الذاكرةِ': (
        'self._state[rkey] = data', 'pass  # M8'),
}


def run_suite() -> tuple[subprocess.CompletedProcess, Path]:
    """جولةٌ بتقريرِ JUnit XML منظَّمٍ — الحكمُ من التقريرِ لا من نثرِ المخرجِ."""
    report = OUT_DIR / f'_junit_{len(list(OUT_DIR.glob("junit_*.xml")))}.xml'
    run = subprocess.run(
        [
            sys.executable, '-m', 'pytest', *TESTS, '-q', '--no-header',
            f'--junitxml={report}',
        ],
        cwd=REPO, capture_output=True, text=True, timeout=600,
    )
    return run, report


def parse_outcome(report: Path) -> dict:
    """الحكمُ من تقريرِ JUnit XML المنظَّمِ (مراجعةُ المستشارِ الثالثةِ § 4).

    القتلُ = خروجُ pytest **1** تحديدًا (فشلُ فحوصٍ) + فحصٌ فاشلٌ واحدٌ على
    الأقلَّ + صفرُ أخطاءِ جمعٍ/تهيئةٍ — كلُّها من أعدادِ `<testsuite>` لا من نثرِ
    المخرجِ النصيِّ.
    """
    import xml.etree.ElementTree as ET

    suite = ET.parse(report).getroot()  # <testsuites> أو <testsuite>
    testsuites = [suite] if suite.tag == 'testsuite' else list(suite.findall('testsuite'))
    failures = sum(int(ts.get('failures', 0)) for ts in testsuites)
    errors = sum(int(ts.get('errors', 0)) for ts in testsuites)
    return {
        'failures': failures,
        'errors': errors,
        'killed': failures > 0 and errors == 0,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for stale in OUT_DIR.glob('junit_*.xml'):
        stale.unlink()  # تقاريرُ الجولةِ السابقةِ لا تُختلطُ بهذهِ
    original = MODULE.read_text(encoding='utf-8')
    results = {}
    try:
        # خطُ الأساسِ: جولةٌ خضراءٌ موثَّقةٌ قبلَ أيِّ طفرةٍ (مراجعةُ المستشارِ § 3)
        baseline, baseline_report = run_suite()
        (OUT_DIR / 'baseline.txt').write_text(baseline.stdout, encoding='utf-8')
        (OUT_DIR / 'baseline.stderr.txt').write_text(baseline.stderr, encoding='utf-8')
        base = parse_outcome(baseline_report)
        assert baseline.returncode == 0 and base['failures'] == 0 and base['errors'] == 0, (
            'خطُ الأساسِ ليسَ أخضرَ — لا معنى لحصادِ طفراتٍ فوقَ أرضٍ حمراءَ: '
            + baseline.stdout[-300:]
        )
        print(f"خطُ الأساسِ أخضرُ ({base}) — الحصادُ يبدأُ")
        for name, (old, new) in MUTATIONS.items():
            assert old in original, f'{name}: المرساةُ غيرُ موجودةٍ'
            MODULE.write_text(original.replace(old, new), encoding='utf-8')
            run, report = run_suite()
            (OUT_DIR / f"{OUT_NAMES[name]}.txt").write_text(run.stdout, encoding='utf-8')
            (OUT_DIR / f"{OUT_NAMES[name]}.stderr.txt").write_text(run.stderr, encoding='utf-8')
            outcome = parse_outcome(report)
            outcome['exit_code'] = run.returncode
            outcome['exit_code_is_test_failure'] = run.returncode == 1
            killing = re.findall(r'^FAILED (\S+)', run.stdout, re.M)
            outcome['killed_by'] = killing[:5]
            outcome['killed'] = outcome['killed'] and run.returncode == 1
            results[name] = outcome
            print(
                ('قتلتها ' if outcome['killed'] else 'نجت !!!')
                + f" — {name}: failures={outcome['failures']}"
                + f" errors={outcome['errors']} القاتلُ={killing[0] if killing else '—'}"
            )
    finally:
        MODULE.write_text(original, encoding='utf-8')  # يُستعادُ دائمًا
        # جولةٌ خضراءُ بعدَ الاستعادةِ — الشِفرةُ عادَت سليمةً والقياسُ موثَّقٌ
        restored, restored_report = run_suite()
        (OUT_DIR / 'restored.txt').write_text(restored.stdout, encoding='utf-8')
        (OUT_DIR / 'restored.stderr.txt').write_text(restored.stderr, encoding='utf-8')
        restored_outcome = parse_outcome(restored_report)
        print(
            'بعدَ الاستعادةِ: '
            + ('أخضرُ' if restored.returncode == 0 and restored_outcome['failures'] == 0 else 'أحمرُ !!!')
            + f" ({restored_outcome})"
        )

    out = MODULE.parent.parent.parent / 'docs/audit/evidence/W-471/mutation_kills.json'
    data = json.loads(out.read_text(encoding='utf-8'))
    data['النتائج'] = results
    data['قاعدة_القتل'] = 'فشلُ فحصٍ فعليٌّ (failed>0 · بلا أخطاءِ جمعٍ) — وقبلَها خطُ أساسٍ أخضرُ موثَّقٌ'
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    all_killed = all(r['killed'] for r in results.values())
    print('ALL_KILLED =', all_killed)
    sys.exit(0 if all_killed else 1)


if __name__ == '__main__':
    main()
