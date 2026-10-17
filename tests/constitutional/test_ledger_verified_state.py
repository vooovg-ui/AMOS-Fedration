"""
فحوصُ الإلحاقِ بحالةٍ مُتحقَّقٍ منها في السجلِّ الدستوريِّ — البديلُ أ-2 لـDISC-100 (WI-086 · W-426).
الهدف: إثباتُ أنَّ `append()` بلا تحقّقٍ كاملٍ في كلِّ قيدٍ يحفظُ «لا إلحاقَ فوقَ سلسلةٍ معطوبة» و«كشفَ أيِّ تعديلٍ
  أو حذفٍ أو إعادةِ ترتيبٍ في قيدٍ سابق» **فورًا بلا نافذة** — والتحويراتُ M1–M10 من
  docs/audit/DISC100_LEDGER_APPEND_DESIGN.md § 6 وإعادةُ الكتابةِ المتّسقة (تغييرُ سلوكٍ مُعلَن).
النطاق: `core/constitutional_engine/ledger.py` وحدَه — كلُّ فحصٍ على سجلٍّ مؤقّتٍ في `tmp_path`.
المالك: core/constitutional_engine/ (WI-086 · Perplexity Computer)
تاريخ الإنشاء: 2026-10-17
تاريخ آخر تعديل: 2026-10-17
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from core.constitutional_engine import ledger as ledger_mod
from core.constitutional_engine.ledger import (
    GENESIS_HASH,
    ConstitutionalLedger,
    LedgerTamperError,
    _hash_entry,
)


def _forget(path: Path) -> None:
    """يُحاكي عمليّةً جديدةً لا حالةَ لها للمسار (الحالةُ في الذاكرةِ وحدَها)."""
    ledger_mod._VERIFIED.pop(os.path.realpath(path), None)


def _build(path: Path, n: int) -> ConstitutionalLedger:
    led = ConstitutionalLedger(path)
    for i in range(n):
        led.append({"type": "T", "seq": i})
    return led


def _lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def _write_in_place(path: Path, data: bytes) -> None:
    """كتابةٌ في المكانِ نفسِه (inode لا يتغيّر) مع إعادةِ mtime كما كان — أخبثُ العبث."""
    st = os.stat(path)
    with open(path, "r+b") as fh:
        fh.seek(0)
        fh.write(data)
        fh.truncate()
        fh.flush()
        os.fsync(fh.fileno())
    os.utime(path, ns=(st.st_atime_ns, st.st_mtime_ns))


@pytest.fixture
def verify_calls(monkeypatch):
    """يعدُّ نداءاتِ `_verify`: (start_index, عددُ القيود) — التحقّقُ الكاملُ هو start_index == 0."""
    calls: list[tuple[int, int]] = []
    original = ConstitutionalLedger._verify

    def spy(entries, *, start_index=0, prev_hash=GENESIS_HASH):
        calls.append((start_index, len(entries)))
        return original(entries, start_index=start_index, prev_hash=prev_hash)

    monkeypatch.setattr(ConstitutionalLedger, "_verify", staticmethod(spy))
    return calls


def _full(calls: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [c for c in calls if c[0] == 0 and c[1] > 0]


# ── التحقّقُ الكاملُ مرّةً واحدةً للمسارِ في العمليّة ──────────────────────────


class TestFullVerificationOncePerPath:
    def test_first_append_in_a_fresh_process_verifies_the_whole_chain(self, tmp_path, verify_calls):
        path = tmp_path / "l.jsonl"
        _build(path, 5)
        _forget(path)
        verify_calls.clear()
        ConstitutionalLedger(path).append({"type": "T", "seq": 5})
        assert _full(verify_calls) == [(0, 5)]

    def test_later_appends_verify_only_the_tail(self, tmp_path, verify_calls):
        path = tmp_path / "l.jsonl"
        led = _build(path, 5)
        verify_calls.clear()
        for i in range(5, 10):
            led.append({"type": "T", "seq": i})
        assert _full(verify_calls) == [], "إلحاقٌ لاحقٌ أعادَ التحقّقَ الكامل"
        assert led.verify_chain() == []
        assert [e.index for e in led.entries()] == list(range(10))

    def test_M10_two_objects_for_one_path_verify_fully_once(self, tmp_path, verify_calls):
        """كائنانِ للمسارِ نفسِه (ومسارٌ ثالثٌ برابطٍ رمزيٍّ إليه) ⇒ تحقّقٌ كاملٌ مرّةً واحدة."""
        path = tmp_path / "l.jsonl"
        _build(path, 4)
        _forget(path)
        verify_calls.clear()
        a = ConstitutionalLedger(path)
        b = ConstitutionalLedger(path)
        link = tmp_path / "alias.jsonl"
        link.symlink_to(path)
        c = ConstitutionalLedger(link)
        a.append({"type": "T", "seq": 4})
        b.append({"type": "T", "seq": 5})
        c.append({"type": "T", "seq": 6})
        assert _full(verify_calls) == [(0, 4)]
        assert a.verify_chain() == [] and len(a) == 7


# ── تحويراتُ العبثِ بينَ إلحاقين — كلُّها تُرفَضُ فورًا ────────────────────────


class TestTamperBetweenAppendsIsRefusedImmediately:
    def test_M1_size_changing_edit_of_an_old_entry(self, tmp_path):
        path = tmp_path / "l.jsonl"
        led = _build(path, 4)
        lines = _lines(path)
        rec = json.loads(lines[1])
        rec["body"]["seq"] = 123456
        lines[1] = json.dumps(rec, ensure_ascii=False, sort_keys=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        with pytest.raises(LedgerTamperError, match="تغيّرت"):
            led.append({"type": "T", "seq": 4})

    def test_M2_same_size_in_place_edit_with_mtime_restored(self, tmp_path):
        """التحويرُ الذي كانت نافذةُ أ-1/أ-3 تُمرِّرُه: الحجمُ نفسُه وinode نفسُه وmtime نفسُه."""
        path = tmp_path / "l.jsonl"
        led = _build(path, 4)
        raw = path.read_bytes()
        tampered = raw.replace(b'"seq": 1', b'"seq": 7', 1)
        assert tampered != raw and len(tampered) == len(raw)
        st_before = os.stat(path)
        _write_in_place(path, tampered)
        st_after = os.stat(path)
        assert (st_after.st_ino, st_after.st_size, st_after.st_mtime_ns) == (
            st_before.st_ino,
            st_before.st_size,
            st_before.st_mtime_ns,
        )
        with pytest.raises(LedgerTamperError, match="تغيّرت"):
            led.append({"type": "T", "seq": 4})

    def test_M3_deleting_a_middle_entry(self, tmp_path):
        path = tmp_path / "l.jsonl"
        led = _build(path, 4)
        lines = _lines(path)
        del lines[1]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        with pytest.raises(LedgerTamperError):
            led.append({"type": "T", "seq": 4})

    def test_M4_truncating_the_last_entry(self, tmp_path):
        path = tmp_path / "l.jsonl"
        led = _build(path, 4)
        lines = _lines(path)
        path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
        with pytest.raises(LedgerTamperError):
            led.append({"type": "T", "seq": 4})

    def test_M5_reordering_two_equal_length_entries(self, tmp_path):
        path = tmp_path / "l.jsonl"
        led = _build(path, 4)
        lines = _lines(path)
        assert len(lines[1]) == len(lines[2])
        lines[1], lines[2] = lines[2], lines[1]
        _write_in_place(path, ("\n".join(lines) + "\n").encode("utf-8"))
        with pytest.raises(LedgerTamperError):
            led.append({"type": "T", "seq": 4})

    def test_M7_replacing_the_file_even_with_identical_bytes(self, tmp_path):
        """inode جديد ⇒ رفض: السجلُّ يُلحَقُ به ولا يُستبدَل — ولو بالبايتاتِ نفسِها."""
        path = tmp_path / "l.jsonl"
        led = _build(path, 3)
        copy = tmp_path / "copy.jsonl"
        copy.write_bytes(path.read_bytes())
        os.replace(copy, path)
        with pytest.raises(LedgerTamperError, match="استُبدِل"):
            led.append({"type": "T", "seq": 3})

    def test_deleting_the_whole_ledger_after_verification(self, tmp_path):
        path = tmp_path / "l.jsonl"
        led = _build(path, 3)
        path.unlink()
        with pytest.raises(LedgerTamperError, match="اختفى"):
            led.append({"type": "T", "seq": 3})
        assert not path.exists(), "رُفِضَ الإلحاقُ لكنّه أنشأَ سجلًّا جديدًا"


# ── سلسلةٌ معطوبةٌ عندَ البدء (P1) ─────────────────────────────────────────────


class TestBrokenChainAtStart:
    def test_M6_broken_chain_in_a_fresh_process_refuses_and_writes_nothing(self, tmp_path):
        path = tmp_path / "l.jsonl"
        _build(path, 3)
        lines = _lines(path)
        rec = json.loads(lines[0])
        rec["body"]["seq"] = 99
        lines[0] = json.dumps(rec, ensure_ascii=False, sort_keys=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        _forget(path)
        before = path.read_bytes()
        with pytest.raises(LedgerTamperError, match="محتوى معدَّل"):
            ConstitutionalLedger(path).append({"type": "T", "seq": 3})
        assert path.read_bytes() == before


# ── الذيلُ: إلحاقاتُ غيرِنا ─────────────────────────────────────────────────────

_CHILD = """
import sys
from core.constitutional_engine.ledger import ConstitutionalLedger
led = ConstitutionalLedger(sys.argv[1])
for i in range(3):
    led.append({"type": "T", "actor": "other-process", "seq": i})
"""


class TestTailWrittenByOthers:
    def test_M8_legitimate_appends_by_another_process_are_accepted(self, tmp_path, verify_calls):
        path = tmp_path / "l.jsonl"
        led = _build(path, 3)
        # العمليّةُ الأخرى ترثُ مسارَ الاستيرادِ نفسَه — لا اشتقاقَ لجذرِ المستودعِ من عُمقٍ ثابت
        env = {**os.environ, "PYTHONPATH": os.pathsep.join(p for p in sys.path if p)}
        subprocess.run([sys.executable, "-c", _CHILD, str(path)], check=True, timeout=120, env=env)
        verify_calls.clear()
        entry = led.append({"type": "T", "seq": 3})
        assert entry.index == 6
        assert _full(verify_calls) == [], "ذيلُ عمليّةٍ أخرى أعادَ التحقّقَ الكامل"
        assert (3, 3) in verify_calls, "الذيلُ الجديدُ لم يُتحقَّقْ منه"
        assert led.verify_chain() == []

    def test_M9_a_tail_with_a_wrong_prev_hash_is_refused(self, tmp_path):
        path = tmp_path / "l.jsonl"
        led = _build(path, 3)
        sealed = {"index": 3, "timestamp": "2026-10-17T00:00:00.000000+00:00", "type": "X"}
        bad_prev = "f" * 64
        rec = {
            "index": 3,
            "timestamp": sealed["timestamp"],
            "prev_hash": bad_prev,
            "entry_hash": _hash_entry(bad_prev, sealed),
            "body": sealed,
        }
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")
        with pytest.raises(LedgerTamperError, match="سلسلة مكسورة عند القيد 3"):
            led.append({"type": "T", "seq": 4})

    def test_M9_a_tail_that_skips_an_index_is_refused(self, tmp_path):
        path = tmp_path / "l.jsonl"
        led = _build(path, 3)
        prev = led.entries()[-1].entry_hash
        sealed = {"index": 4, "timestamp": "2026-10-17T00:00:00.000000+00:00", "type": "X"}
        rec = {
            "index": 4,
            "timestamp": sealed["timestamp"],
            "prev_hash": prev,
            "entry_hash": _hash_entry(prev, sealed),
            "body": sealed,
        }
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")
        with pytest.raises(LedgerTamperError, match="ترتيب مكسور عند الموضع 3"):
            led.append({"type": "T", "seq": 4})

    def test_M9_an_unreadable_tail_is_refused(self, tmp_path):
        path = tmp_path / "l.jsonl"
        led = _build(path, 3)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write("NOT JSON\n")
        with pytest.raises(LedgerTamperError, match="قيد تالف"):
            led.append({"type": "T", "seq": 3})


# ── إعادةُ الكتابةِ المتّسقة — تغييرُ سلوكٍ مُعلَن (أشدّ) ─────────────────────


def _consistent_rewrite(path: Path, *, change_seq_of: int) -> None:
    """يُعيدُ كتابةَ السلسلةِ كلِّها ببصماتٍ مُعادٍ حسابُها — `_verify` لا يرى فيها عيبًا."""
    out, prev = [], GENESIS_HASH
    for line in _lines(path):
        rec = json.loads(line)
        body = rec["body"]
        if body["index"] == change_seq_of:
            body["seq"] = 1000 + change_seq_of
        h = _hash_entry(prev, body)
        out.append(
            json.dumps(
                {
                    "index": rec["index"],
                    "timestamp": rec["timestamp"],
                    "prev_hash": prev,
                    "entry_hash": h,
                    "body": body,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        prev = h
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


class TestConsistentRewrite:
    def test_rewrite_after_verification_is_refused_though_verify_chain_accepts_it(self, tmp_path):
        """الفرقُ عن السلوكِ السابقِ مقصود: كانَ `append` يقبلُ هذا، والآنَ يرفضُه."""
        path = tmp_path / "l.jsonl"
        led = _build(path, 4)
        _consistent_rewrite(path, change_seq_of=0)
        assert led.verify_chain() == [], "التحقّقُ الكاملُ بلا مرساةٍ يقبلُ الكتابةَ المتّسقة (كما كان)"
        with pytest.raises(LedgerTamperError, match="إعادةُ كتابةٍ للسلسلة"):
            led.append({"type": "T", "seq": 4})

    def test_rewrite_before_a_process_starts_is_still_accepted_as_before(self, tmp_path):
        """الحدُّ المُعلَن: عمليّةٌ لا حالةَ لها تتحقّقُ تحقّقًا كاملًا بلا مرساة — كما كان قبلَ WI-086."""
        path = tmp_path / "l.jsonl"
        _build(path, 4)
        _consistent_rewrite(path, change_seq_of=0)
        _forget(path)
        entry = ConstitutionalLedger(path).append({"type": "T", "seq": 4})
        assert entry.index == 4
