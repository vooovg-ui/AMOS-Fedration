"""حاصدُ الطفراتِ الثماني — WI-096 § 3 (يعمل من المستودع · يعيدُ الملفَ دائمًا).

الهدف: إثباتٌ قابلٌ لإعادةِ التشغيلِ من المستودعِ أنَّ فحوصَ WI-096 تقتلُ
الطفراتِ الثماني المُعلَنةَ في وثيقةِ التصميمِ § 3 — لا صدفةَ تحرسُ الخصائصَ.
النطاق: core/sovereignty/idempotency.py · الوثيقةُ DISC105_IDEMPOTENCY_APPEND_DESIGN.md § 3.
المالك: Perplexity Computer (WI-096 · التوجيهُ 12 § 2 المأذونُ مسبقًا).

التشغيلُ: .venv/bin/python docs/audit/evidence/W-471/mutation_harness.py
قاعدةُ القتلِ: الطفرةُ تُعَدُّ مقتولةً إن **سقطَ فحصٌ** (failed) لا إن تعطّلَ
الجمعُ نفسُهُ (خطأُ استيرادٍ أو جمعٍ لا يُعَدُّ قتلًا — تصحيحُ مراجعةِ المستشارِ W-477 § 4).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
MODULE = REPO / 'core/sovereignty/idempotency.py'
TESTS = [
    'tests/sovereignty/test_idempotency_append_log.py',
    'tests/sovereignty/test_idempotency.py',
]

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


def run_suite() -> tuple[int, str]:
    run = subprocess.run(
        [sys.executable, '-m', 'pytest', *TESTS, '-q', '-x', '--no-header'],
        cwd=REPO, capture_output=True, text=True, timeout=600,
    )
    return run.returncode, run.stdout


def main() -> None:
    original = MODULE.read_text(encoding='utf-8')
    results = {}
    try:
        for name, (old, new) in MUTATIONS.items():
            assert old in original, f'{name}: المرساةُ غيرُ موجودةٍ'
            MODULE.write_text(original.replace(old, new), encoding='utf-8')
            code, out = run_suite()
            tail = out.strip().splitlines()[-1] if out.strip() else ''
            # القتلُ = سقوطُ فحصٍ لا تعطّلُ الجمعِ (استيرادٌ/جمعٌ ليسَ حكمَ الفحوصِ)
            collection_broken = 'error' in tail.lower() and 'failed' not in tail.lower()
            results[name] = {
                'killed': code != 0 and not collection_broken,
                'exit_code': code,
                'tail': tail,
            }
            print(f"{'قتلها' if results[name]['killed'] else 'نجت !!!'} — {name}: {tail[:100]}")
    finally:
        MODULE.write_text(original, encoding='utf-8')  # يُستعادُ دائمًا

    out = MODULE.parent.parent.parent / 'docs/audit/evidence/W-471/mutation_kills.json'
    data = json.loads(out.read_text(encoding='utf-8'))
    data['النتائج'] = results
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    all_killed = all(r['killed'] for r in results.values())
    print('ALL_KILLED =', all_killed)
    sys.exit(0 if all_killed else 1)


if __name__ == '__main__':
    main()
