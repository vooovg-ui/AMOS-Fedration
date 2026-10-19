"""فحوصُ السجلِّ الإلحاقيِّ لملفِ الذرّيّةِ — WI-096 (DISC-105 · التوجيهُ 15).

الهدف: حراسةُ خصائصِ الذرّةِ للسجلِّ الإلحاقيِّ (JSONL + flock + ضغطٌ دوريٌّ) وقتلُ الطفراتِ الثماني المُعلَنةِ في وثيقةِ التصميمِ
النطاق: `core/sovereignty/idempotency.py` — الواجهةُ العامةُ وتواقيعُها لا تتغيّرُ (§ 2.4)
المالك: Perplexity Computer (WI-096 · التوجيهُ 12 § 2 المأذونُ مسبقًا)

كلُّ فحصٍ هنا حارسٌ لخاصيّةٍ مُعلَنةٍ في وثيقةِ التصميمِ
(`docs/audit/DISC105_IDEMPOTENCY_APPEND_DESIGN.md`) — وقتلُ الطفراتِ الثماني
المُعلَنةِ فيها (§ 3) يُثبَتُ بأنَّ هذا الملفِّ هو الذي يحرسُ لا الصدفةُ.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.governance.repo_root import discover_repo_root

from core.sovereignty.idempotency import (
    IdempotencyError,
    IdempotencyKey,
    IdempotencyKeyReuseError,
    IdempotencyLedger,
    OperationStatus,
)

# الجذرُ بعلامةٍ لا بعُمقٍ مكتوبٍ (درسُ DISC-041): صعودٌ حتّى علاماتِ المستودعِ
REPO_ROOT = discover_repo_root(__file__)


def _make_ledger(tmp_path: Path, name: str = "idempotency.json") -> IdempotencyLedger:
    return IdempotencyLedger(path=tmp_path / name)


def _make_key(n: int = 1) -> IdempotencyKey:
    return IdempotencyKey("قياس", f"عمليّة-{n}")


def _read_events(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


# ── § 2.1: الإلحاقُ O(1) — كلُّ حدثٍ سطرٌ واحدٌ ──────────────────────────────


class TestAppendLogShape:
    def test_each_event_is_one_line(self, tmp_path):
        """كلُّ حدثٍ سطرُ JSONL واحدٌ متصلٌ — لا سطرٍ مكسورٍ ولا حدثٍ بلا سطرٍ."""
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        ledger.mark_running(key=key, attempt={"n": 1})
        ledger.mark_succeeded(key=key, result_digest="هاش")

        lines = ledger.path.read_text(encoding="utf-8").splitlines()
        # الترويسةُ + 3 أحداثٍ = 4 أسطرٍ، وكلُّ سطرٍ يُوزَنُ JSON وحيدَهُ
        assert len(lines) == 4, "حدثٌ كُتِبَ في أكثرَ من سطرٍ أو سطرٌ بلا حدثٍ"
        for line in lines:
            assert isinstance(json.loads(line), dict)

    def test_read_after_write_same_instance(self, tmp_path):
        """الإلحاقُ يُحدِّثِ الحالةَ في الذاكرةِ فورًا — لا قراءةَ تنسخُ ما بعدها."""
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        # لو لم يُحدَّثِ الإلحاقُ الحالةَ لما رأى `get` الحجزَ دونَ إعادةِ قراءةٍ
        assert ledger.get(key) is not None
        assert ledger.count() == 1

    def test_two_instances_share_the_log(self, tmp_path):
        """نسختانِ على السجلِّ نفسِهِ: الثانيةُ ترى أحداثَ الأولى (المزامنةُ التزايديّةُ)."""
        first = _make_ledger(tmp_path)
        second = _make_ledger(tmp_path)
        key = _make_key()
        first.reserve(key=key, fingerprint="بصمة-1")
        assert second.get(key) is not None, "المزامنةُ التزايديّةُ لم ترَ حدثَ الأخرى"

    def test_replacement_rebuilds_state_regardless_of_size(self, tmp_path):
        """استبدالُ السجلِّ (ضغطٌ بيدِ عمليّةٍ أخرى) يُبطلُ الحالةَ كلَّها مهما كانَ حجمُ الجديدِ.

        بلا ربطِ الحالةِ بهويّةِ الملفِّ تقعُ القراءةُ من موضعٍ قديمٍ في ملفٍّ
        جديدٍ أكبرَ — من منتصفِ سطرٍ — فتفسدُ أو تُهمَلُ (W-477 · مراجعةُ المستشارِ § 1).
        """
        first = _make_ledger(tmp_path)
        second = _make_ledger(tmp_path)
        first.reserve(key=_make_key(0), fingerprint="بصمة-0")
        assert second.get(_make_key(0)) is not None
        # الثانيةُ تضغطُ بعدَ 100 مفتاحٍ بمحاولاتِ إعادةٍ — اللقطةُ الناتجةُ أكبرُ
        # بكثيرٍ من موضعِ الأولى القديمِ (فحجمُ الجديدِ ليسَ حكمًا على الاستبدالِ)
        for i in range(1, 101):
            self._compaction_flow(second, i)
        assert second.count() == 101
        # الأولى يجبُ أن ترى كلَّ المفاتيحِ بعدَ الاستبدالِ (بناءٌ من الصفرِ بالهويّةِ)
        assert first.count() == 101, "استبدالُ السجلِّ لم يُبطلْ حالةَ النسخةِ المتأخّرةِ"
        for i in range(1, 101):
            assert first.get(IdempotencyKey("قياس", f"عمليّة-{i}")) is not None

    @staticmethod
    def _compaction_flow(ledger: IdempotencyLedger, i: int) -> None:
        """تدفّقٌ يُنتجُ 17 حدثًا فوقَ مفتاحٍ واحدٍ — يُشعلُ الضغطَ بثباتٍ."""
        key = IdempotencyKey("قياس", f"عمليّة-{i}")
        ledger.reserve(key=key, fingerprint=f"بصمة-{i}")
        ledger.mark_running(key=key)
        for _ in range(7):
            ledger.mark_failed(key=key, reason="عَرَضيّة", retryable=True)
            ledger.mark_running(key=key)
        ledger.mark_succeeded(key=key, result_digest="هاش")


# ── § 2.2: الذرّةُ والتحطّمُ الآمنُ ──────────────────────────────────────────


class TestCrashSafety:
    def test_torn_tail_is_ignored_and_retried(self, tmp_path):
        """سطرٌ ذيليٌّ ممزّقٌ (كتابةٌ انقطعت) يُهمَلُ ولا يُسقِطُ القراءةَ (§ 2.2)."""
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        # محاكاةُ انقطاعِ كتابةٍ: سطرٌ نصفُهُ فقطَ (لا `\\n` في آخرِهِ)
        with open(ledger.path, "a", encoding="utf-8") as stream:
            stream.write('{"v": 1, "op": "transition", "key": "ناق')
        # القراءةُ تتجاوزُ الذيلَ الممزّقَ ولا ترفعُ خطأً
        assert ledger.get(key) is not None
        assert ledger.count() == 1
        # والذيلُ يُستكمَلُ لاحقًا: كتابةٌ جديدةٌ فوقَهُ تُقرأُ سليمةً
        ledger.mark_running(key=key)
        assert ledger.get(key).status == OperationStatus.RUNNING

    def test_complete_corrupt_line_raises(self, tmp_path):
        """سطرٌ كاملٌ تالفٌ = استثناءٌ صريحٌ لا ابتلاعٌ صامتٌ (حارسُ الأصلِ)."""
        ledger = _make_ledger(tmp_path)
        ledger.path.parent.mkdir(parents=True, exist_ok=True)
        ledger.path.write_text("NOT JSON\n", encoding="utf-8")
        with pytest.raises(IdempotencyError, match="تالف"):
            ledger.get(_make_key())

    def test_log_not_starting_with_header_rejected(self, tmp_path):
        """ملفٌّ يبدأُ بحدثٍ لا ترويسةَ ليسَ سجلًّا شرعيًّا — يُرفَعُ لا يُتَسامَحُ (W-489 § 2)."""
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        lines = ledger.path.read_text(encoding="utf-8").splitlines(keepends=True)
        ledger.path.write_text("".join(lines[1:]), encoding="utf-8")
        with pytest.raises(IdempotencyError, match="تالف"):
            _make_ledger(tmp_path).get(key)

    def test_unknown_event_version_rejected(self, tmp_path):
        """حدثٌ بإصدارٍ مجهولٍ = تلفٌ صريحٌ — لا تجاوُزَ ولا صمتًا (W-489 § 2)."""
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        lines = ledger.path.read_text(encoding="utf-8").splitlines(keepends=True)
        event = json.loads(lines[1])
        event["v"] = 99
        lines[1] = json.dumps(event, ensure_ascii=False) + "\n"
        ledger.path.write_text("".join(lines), encoding="utf-8")
        with pytest.raises(IdempotencyError, match="تالف"):
            _make_ledger(tmp_path).get(key)

    def test_unknown_event_op_rejected(self, tmp_path):
        """حدثٌ بعمليةٍ مجهولةٍ = تلفٌ صريحٌ (W-489 § 2)."""
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        lines = ledger.path.read_text(encoding="utf-8").splitlines(keepends=True)
        event = json.loads(lines[1])
        event["op"] = "عمليةٌ مجهولةٌ"
        lines[1] = json.dumps(event, ensure_ascii=False) + "\n"
        ledger.path.write_text("".join(lines), encoding="utf-8")
        with pytest.raises(IdempotencyError, match="تالف"):
            _make_ledger(tmp_path).get(key)

    def test_null_record_rejected(self, tmp_path):
        """حدثٌ تامُّ البنيةِ بترويسةٍ وإصدارٍ وعمليةٍ لكنَّ سجلَّه معدومٌ = تلفٌ يُرفَعُ لا فقدٌ صامتٌ (W-489 § 2)."""
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        lines = ledger.path.read_text(encoding="utf-8").splitlines(keepends=True)
        event = json.loads(lines[1])
        event["record"] = None
        lines[1] = json.dumps(event, ensure_ascii=False) + "\n"
        ledger.path.write_text("".join(lines), encoding="utf-8")
        with pytest.raises(IdempotencyError, match="تالف"):
            _make_ledger(tmp_path).get(key)

    def test_invalid_utf8_in_complete_line_rejected(self, tmp_path):
        """سطرٌ كاملٌ جيدُ البنيةِ عدا بايتٌ فاسدُ الترميزِ = تلفٌ صريحٌ لا استبدالُ حرفٍ صامتٌ (W-489 § 2).

        الحدثُ تامُّ JSON عدا البايتُ الفاسدُ داخلَ قيمةِ المفتاحِ — فالرفضُ من
        فكِّ الترميزِ الصارمِ لا من موضعِ فحصٍ آخرَ.
        """
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        bad = b'{"v": 1, "op": "transition", "key": "\xff\xfe", "record": {"state": "reserved"}}\n'
        with open(ledger.path, "ab") as stream:
            stream.write(bad)
        with pytest.raises(IdempotencyError, match="تالف"):
            _make_ledger(tmp_path).get(key)

    def test_atomic_single_line_appends(self, tmp_path):
        """كلُّ حدثٍ يُكتَبُ بفتحةِ إلحاقٍ واحدةٍ — فتحتانِ متتاليتانِ لا تمحوانِ ما قبلَهما."""
        ledger = _make_ledger(tmp_path)
        ledger.reserve(key=_make_key(1), fingerprint="بصمة-1")
        # نسخةٌ ثانيةٌ تفتحُ الملفَّ من جديدٍ — لا يجوزُ أن تمحوَ أحداثَ الأولى
        second = _make_ledger(tmp_path)
        second.reserve(key=_make_key(2), fingerprint="بصمة-2")
        assert ledger.count() == 2, "فتحُ نسخةٍ ثانيةٍ محا أحداثَ الأولى (وضعُ w بدلَ a)"


# ── § 2.2: قفلُ العمليّةِ (DISC-095) ──────────────────────────────────────────


class TestProcessLock:
    def test_concurrent_processes_lose_no_event(self, tmp_path):
        """عمليّتانِ تُلحِقانِ معًا: لا حدثَ يضيعُ — هذا ما يُقتِلُ حذفَ flock (الطفرةُ 1)."""
        ledger = _make_ledger(tmp_path)
        ledger.reserve(key=_make_key(0), fingerprint="بصمة-0")  # تهيئةُ الملفِّ
        ledger_path = str(ledger.path)
        script = (
            "import sys; "
            "from pathlib import Path; "
            "from core.sovereignty.idempotency import IdempotencyKey, IdempotencyLedger; "
            f"ledger = IdempotencyLedger(path=Path({ledger_path!r})); "
            "[ledger.reserve(key=IdempotencyKey('قياس', f'عمليّة-{sys.argv[1]}-{i}'), "
            "fingerprint=f'بصمة-{sys.argv[1]}-{i}') for i in range(40)]"
        )
        workers = [
            subprocess.Popen(
                [sys.executable, "-c", script, str(tag)],
                cwd=str(REPO_ROOT),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            for tag in range(4)
        ]
        for worker in workers:
            _, stderr = worker.communicate(timeout=120)
            assert worker.returncode == 0, stderr.decode("utf-8", errors="replace")

        reader = _make_ledger(tmp_path)
        assert reader.count() == 1 + 4 * 40, "حدثٌ ضاعَ في تزاحمِ العمليّاتِ — القفلُ لا يُسلسِلُ"
        # وكلُّ سجلٍّ وصلَ سليمًا: لا سطرٍ ممزّقٍ بقيَ
        events = _read_events(ledger.path)
        assert len(events) == reader.count() + 1  # + الترويسةُ لا تُعدُّ... الترويسةُ ليست حدثًا


# ── § 2.3: الضغطُ الدوريُّ ─────────────────────────────────────────────────────


class TestCompaction:
    @staticmethod
    def _retry_flow(ledger: IdempotencyLedger, i: int, events: int) -> None:
        """تدفّقُ عمليّةٍ ذاتِ محاولاتٍ إعادةٍ: `events` أحداثٍ فوقَ مفتاحٍ واحدٍ."""
        key = _make_key(i)
        ledger.reserve(key=key, fingerprint=f"بصمة-{i}")
        ledger.mark_running(key=key)
        for _ in range(max(0, events - 3)):
            ledger.mark_failed(key=key, reason="عَرَضيّة", retryable=True)
            ledger.mark_running(key=key)
        ledger.mark_succeeded(key=key, result_digest="هاش")

    def test_compaction_keeps_all_live_keys(self, tmp_path):
        """الضغطُ لا يُسقِطُ مفتاحًا حيًّا (الطفرةُ 6) — ويُشغَّلُ فعلًا (الطفرةُ 5)."""
        ledger = _make_ledger(tmp_path)
        for i in range(20):
            self._retry_flow(ledger, i, events=5)  # 13 حدثًا لكلِّ مفتاحٍ = 260 سطرًا
        # 260 سطرًا ≥ عتبةِ 4×20 ⇒ ضغطٌ وقعَ: عددُ الأسطرِ دونَ عددِ الأحداثِ
        lines = len(ledger.path.read_text(encoding="utf-8").splitlines())
        assert lines < 20 * 13, "الضغطُ لم يُشغَّلْ بعدَ تجاوزِ العتبةِ (الطفرةُ 5)"
        assert ledger.count() == 20, "الضغطُ أسقطَ مفاتيحَ حيّةً (الطفرةُ 6)"
        # المفاتيحُ على **القرصِ** لا في الذاكرةِ وحدَها: نسخةٌ جديدةٌ تُعيدُ
        # البناءَ منَ السجلِّ فتُثبِتُ أنَّ الضغطَ لم يُسقِطْ شيئًا (الطفرةُ 6)
        fresh = _make_ledger(tmp_path)
        assert fresh.count() == 20, "الضغطُ محا المفاتيحَ منَ القرصِ (الطفرةُ 6)"
        for i in range(20):
            record = fresh.get(_make_key(i))
            assert record.status == OperationStatus.SUCCEEDED

    def test_log_grows_asymptotically_not_linearly(self, tmp_path):
        """الضغطُ يُهَلِّلُ: الأسطرُ لا تنمو معَ الأحداثِ بل تُعادُ إلى مضاعفِ المفاتيحِ الحيّةِ."""
        ledger = _make_ledger(tmp_path)
        total_events = 0
        for i in range(100):
            self._retry_flow(ledger, i, events=10)  # 23 حدثًا لكلِّ مفتاحٍ
            total_events += 23
        final_lines = len(ledger.path.read_text(encoding="utf-8").splitlines())
        # ثابتُ الثباتِ: بعدَ كلِّ إلحاقٍ يُفحَصُ الضغطُ فلا يزيدُ الأسطرُ على 4× الحيِّ
        assert final_lines <= 4 * ledger.count() + 1, "الضغطُ لا يضبطُ النموَّ (الطفرةُ 5)"
        assert final_lines < total_events, "السجلُّ ينمو معَ الأحداثِ لا معَ الحالةِ (الطفرةُ 5)"


# ── § 2.4: الترحيلُ والتوافقُ ──────────────────────────────────────────────────


class TestMigration:
    def test_legacy_json_object_is_migrated_once(self, tmp_path):
        """ملفُّ الصيغةِ القديمةِ (JSON كائنٍ) يُرحَّلُ تلقائيًّا وسجلّاتُهُ لا تضيعُ (الطفرةُ 7)."""
        from core.sovereignty.runtime_identity import stamped
        from core.sovereignty.idempotency import IDEMPOTENCY_STATE_CARD

        ledger = _make_ledger(tmp_path)
        key = _make_key()
        # اكتبِ الصيغةَ القديمةَ بيدٍ: كائنُ JSON بسجلٍّ واحدٍ (بصيغةِ as_dict نفسِها)
        legacy_payload = stamped(
            {
                key.composite: {
                    "key": key.composite,
                    "scope": key.scope,
                    "value": key.value,
                    "fingerprint": "بصمة-قديمة",
                    "status": "RESERVED",
                    "reserved_at": "2026-10-19T00:00:00+00:00",
                    "attempts": [],
                    "transitions": [],
                    "applied_effect_signatures": [],
                    "has_external_effect": False,
                }
            },
            card=IDEMPOTENCY_STATE_CARD,
        )
        ledger.path.parent.mkdir(parents=True, exist_ok=True)
        ledger.path.write_text(
            json.dumps(legacy_payload, ensure_ascii=False, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        # الفتحُ يُرحِّلُ: السجلُّ يُقرأُ منَ الصيغةِ الجديدةِ
        record = ledger.get(key)
        assert record is not None, "الترحيلُ محا السجلَّ القديمَ (الطفرةُ 7)"
        assert record.fingerprint == "بصمة-قديمة"
        # والملفُّ صارَ إلحاقيًّا: أسطرٌ JSONL
        first_event = _read_events(ledger.path)
        assert any(e.get("key") == key.composite for e in first_event)
        # والأحداثُ الجديدةُ تُلحَقُ فوقَهُ بلا مسحٍ
        ledger.mark_running(key=key)
        assert ledger.get(key).status == OperationStatus.RUNNING

    def test_reuse_with_different_fingerprint_still_refused(self, tmp_path):
        """حارسُ الأصلِ لا يتراجعُ: البصمةُ تُفحَصُ في الصيغةِ الجديدةِ كما القديمةِ (الطفرةُ 4)."""
        ledger = _make_ledger(tmp_path)
        key = _make_key()
        ledger.reserve(key=key, fingerprint="بصمة-1")
        with pytest.raises(IdempotencyKeyReuseError):
            ledger.reserve(key=key, fingerprint="بصمة-أخرى")
