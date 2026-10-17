"""
السجل الدستوري غير القابل للعبث — Tamper-Evident Constitutional Ledger (E1)
الهدف: تسجيل كل حكم دستوري في سلسلة تجزئة متصلة، بحيث لا يمكن حذف قيد ولا تعديله ولا إعادة ترتيبه دون كشف فوري.
النطاق: الكتابة الملحقة فقط (append-only) والتحقق من السلسلة. لا حذف، ولا تعديل، ولا اقتطاع — بأي صلاحية.
المالك: core/constitutional_engine/
تاريخ الإنشاء: 2026-08-16
تاريخ آخر تعديل: 2026-10-17

المبدأ (المادة الأولى · 3 و 4، والمادة السابعة): الذاكرة مقدسة، والشفافية مطلقة.
كل قيد يحمل بصمة القيد السابق. كسر السلسلة يُكتشف بـ verify_chain() ولا يمكن إخفاؤه.

تصحيحُ ادّعاءٍ (2026-08-18): كان هذا الملفُّ يزعم في `append` أنّ «الكتابة ذرّية
(ملف مؤقت ثم استبدال)» وهو ما لم يفعله الكودُ قطعًا — كان `open(path, "a")`
مباشرًا بلا قفلٍ ولا ملفٍّ مؤقت. والزعمُ لم يكن تجميلًا: قسمُ الحرج
(اقرأ ← تحقّق ← احسب index ← ألحِق) كان بلا حصرٍ متبادل، فعمليّتان متزامنتان
تقرآن الطولَ N فتحسبان كلتاهما `index=N` وتُلحِقان، فينكسرُ الترتيبُ نهائيًّا.
وبما أنّ `append` يرفض الكتابةَ فوق سلسلةٍ مكسورة، فالسجلُّ يتعطّل إلى الأبد
ولا مسارَ إصلاح — أي إنكارُ سيادةٍ يُلحِقُه النظامُ بنفسه.

قياسٌ فعليٌّ للعطل (٦ عمليّاتٍ × ١٥ قيدًا = ٩٠ متوقَّعًا):
    قبل الإصلاح: كُتب قيدان، والسلسلةُ مكسورة، وكلُّ العمليّاتِ سقطت.
    بعد الإصلاح: ٩٠ قيدًا، والسلسلةُ سليمة.
الانحدارُ محروسٌ في tests/constitutional/test_ledger_concurrency.py.

الإصلاح: قفلٌ استئثاريٌّ عبر العمليّات (`fcntl.flock`) على ملفٍّ جانبيٍّ
`<path>.lock` يلفُّ قسمَ الحرج كلَّه. ولا يُستخدَم بديلٌ صامت: إن غاب `fcntl`
رُفع `LedgerLockUnavailableError` — فالإلحاقُ بلا حصرٍ متبادلٍ يُفسد السلسلة،
والسقوطُ المُعلَن أسلمُ من كتابةٍ تبدو ناجحةً وتُعطِّل الدولة.

الإلحاقُ بلا تحقّقٍ كاملٍ في كلِّ قيد (2026-10-17 · WI-086 · DISC-100 · قرارُ المالكِ «أ-2»):
كان `append` يقرأُ السلسلةَ كلَّها ويُعيدُ حسابَ كلِّ بصمةٍ مع كلِّ قيد — O(N) لكلِّ إلحاقٍ
وO(N²) تراكميًّا (مقيسٌ: ~20.6 µs لكلِّ قيدٍ سابقٍ في كلِّ إلحاق · evidence/W-411/).
والآن: تحقّقٌ كاملٌ **أوّلَ مرّةٍ** يُلحَقُ فيها بالمسارِ في العمليّة، ثمَّ حالةٌ مُتحقَّقٌ منها
على مستوى الوحدةِ مفهرسةٌ بالمسارِ الحقيقيّ (كائناتُ السجلِّ كثيرةٌ في العمليّةِ الواحدة):
`(st_dev, st_ino)` + طولُ الجزءِ المُتحقَّقِ منه + عددُ قيودِه + آخرُ بصمة + sha256 لبايتاتِه.
وفي كلِّ إلحاقٍ داخلَ القفل: تُطابَقُ sha256 لبايتاتِ الجزءِ المُتحقَّقِ منه (أيُّ تعديلٍ أو حذفٍ
أو إعادةِ ترتيبٍ أو اقتطاعٍ ⇒ رفضٌ فوريٌّ بلا نافذة) ثمَّ يُتحقَّقُ من الذيلِ الجديدِ وحدَه
(إلحاقاتُ عمليّاتٍ أخرى) بالقواعدِ نفسِها. والثمنُ مُعلَن: ما زالَ O(N) لكلِّ إلحاقٍ بثابتٍ
أصغرَ ~21–23 مرّة (قراءةُ البايتاتِ وبصمتُها لا تحليلُ JSON وإعادةُ حسابِ كلِّ بصمة).

تغييرُ سلوكٍ مُعلَنٌ (أشدّ): إعادةُ كتابةٍ **متّسقةٍ** للسلسلةِ (بصماتٌ مُعادٌ حسابُها) بعدَ أن
تحقّقت منها العمليّة يقبلُها `verify_chain()` — لا مرساةَ له — ويرفضُها `append` الآن.
وكذلك حذفُ الملفِّ كلِّه أو استبدالُه (inode جديد) بعدَ التحقّق. وما يبقى كما كان: عمليّةٌ
جديدةٌ لا حالةَ لها تتحقّقُ تحقّقًا كاملًا فتقبلُ سلسلةً متّسقةً أُعيدَت كتابتُها قبلَ بدئها.
`entries()` و`verify_chain()` وشكلُ الملفِّ بلا تغيير.
"""

from __future__ import annotations

import hashlib
import importlib
import importlib.util
import json
import os
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# حضورُ `fcntl` يُفحَص ولا يُجرَّب: المدقّقُ الدستوريّ رفع `SILENT_FALLBACK`
# على محاولةِ `try/except ImportError` — وكان مُحقًّا: بلاعةُ الاستثناء
# تُتلِف سببَ الفشل وتترك `None` مكانَ أداةٍ أمنيّة. والفحصُ المُعلَن أصدقُ:
# لا استثناءَ يُبتلع، والغيابُ يصير حالةً مقروءةً تُرفع صراحةً في
# `LedgerLockUnavailableError` عند أوّل محاولةِ إلحاق، لا بديلًا صامتًا.
_HAS_FLOCK = importlib.util.find_spec("fcntl") is not None
fcntl = importlib.import_module("fcntl") if _HAS_FLOCK else None

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LEDGER = REPO_ROOT / "core" / "constitution" / "ledger" / "constitutional_ledger.jsonl"

GENESIS_HASH = "0" * 64


def _canonical(payload: dict[str, Any]) -> str:
    """تمثيل نصي حتمي — نفس المحتوى ينتج نفس البصمة دائمًا."""
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _hash_entry(prev_hash: str, body: dict[str, Any]) -> str:
    return hashlib.sha256((prev_hash + _canonical(body)).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class LedgerEntry:
    index: int
    timestamp: str
    prev_hash: str
    entry_hash: str
    body: dict[str, Any]


class LedgerTamperError(RuntimeError):
    """يُرفع عند اكتشاف كسر في سلسلة السجل. لا يُبتلع أبدًا."""


class LedgerLockUnavailableError(RuntimeError):
    """يُرفع عند تعذّر الحصرِ المتبادل على السجل.

    الهدف: منعُ إلحاقٍ غيرِ محميٍّ يبدو ناجحًا ثم يُعطِّل السلسلةَ نهائيًّا.
    لا بديلَ صامتًا هنا: السقوطُ المُعلَن هو التصرّفُ المُغلَق عند الفشل.
    """


@dataclass(frozen=True)
class _VerifiedState:
    """ما تحقّقت منه هذه العمليّةُ تحقّقًا كاملًا في ملفِّ سجلٍّ — لا يُحفَظُ على القرص."""

    dev: int
    ino: int
    size: int
    count: int
    last_hash: str
    prefix_sha256: bytes


# الحالةُ على مستوى الوحدة لا الكائن: `ConstitutionalAuthorizer` يبني سجلًّا جديدًا للمسارِ نفسِه
# في ثمانيةِ مواضعَ إنتاجيّة، فحالةٌ على الكائنِ تُعيدُ التحقّقَ الكاملَ مع كلِّ كائن (DISC-100 § 3).
_VERIFIED: dict[str, _VerifiedState] = {}
_VERIFIED_GUARD = threading.Lock()


class ConstitutionalLedger:
    """سجل ملحق فقط بسلسلة تجزئة. لا يوفر — عمدًا — أي دالة حذف أو تعديل."""

    def __init__(self, path: Path | str | None = None) -> None:
        self.path = Path(path) if path else DEFAULT_LEDGER
        self.path.parent.mkdir(parents=True, exist_ok=True)

    # -- قراءة ------------------------------------------------------------
    def entries(self) -> list[LedgerEntry]:
        if not self.path.exists():
            return []
        return self._parse(self.path.read_text(encoding="utf-8"), where=str(self.path))

    @staticmethod
    def _parse(text: str, *, where: str) -> list[LedgerEntry]:
        out: list[LedgerEntry] = []
        for line_no, line in enumerate(text.splitlines(), start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as exc:
                raise LedgerTamperError(
                    f"قيد تالف في {where}:{line_no} — السجل غير قابل للقراءة: {exc}"
                ) from exc
            out.append(
                LedgerEntry(
                    index=rec["index"],
                    timestamp=rec["timestamp"],
                    prev_hash=rec["prev_hash"],
                    entry_hash=rec["entry_hash"],
                    body=rec["body"],
                )
            )
        return out

    def head_hash(self) -> str:
        entries = self.entries()
        return entries[-1].entry_hash if entries else GENESIS_HASH

    def __len__(self) -> int:
        return len(self.entries())

    # -- كتابة ------------------------------------------------------------
    @property
    def lock_path(self) -> Path:
        """ملفُّ القفل الجانبي. منفصلٌ عن السجل حتى لا يُعاق القارئون."""
        return self.path.with_suffix(self.path.suffix + ".lock")

    @contextmanager
    def _exclusive(self) -> Iterator[None]:
        """حصرٌ متبادلٌ عبر العمليّات على قسمِ الحرج (اقرأ ← تحقّق ← ألحِق)."""
        if fcntl is None:  # pragma: no cover - المستودع وCI على POSIX
            raise LedgerLockUnavailableError(
                "لا يوفّر هذا النظامُ `fcntl.flock`، فلا يمكن ضمانُ الحصرِ المتبادل "
                "على السجل الدستوري. الإلحاقُ بلا حصرٍ يُفسد السلسلةَ نهائيًّا، "
                "فيُرفَض الإلحاقُ صراحةً (المادة الأولى · 3)."
            )
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(self.lock_path, os.O_CREAT | os.O_WRONLY, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)

    def append(self, body: dict[str, Any], *, timestamp: str | None = None) -> LedgerEntry:
        """ألحق قيدًا جديدًا داخل حصرٍ متبادلٍ عبر العمليّات.

        قسمُ الحرج كلُّه (اقرأ ← تحقّق ← احسب `index` و`prev_hash` ← ألحِق ← fsync)
        محميٌّ بقفل `flock` استئثاريٍّ على `<path>.lock`. فبلا هذا القفل تقرأ
        عمليّتان الطولَ نفسَه فتُنتِجان `index` مكرَّرًا وتكسران السلسلةَ إلى
        الأبد. القفلُ ليس تحسينَ أداءٍ بل شرطُ صحّةٍ.
        """
        with self._exclusive():
            # لا نضيف فوق سلسلة مكسورة: كلُّ ما على القرصِ الآنَ مُتحقَّقٌ منه قبلَ الكتابة
            index, prev_hash, verified_size, hasher = self._verified_snapshot()
            ts = timestamp or datetime.now(timezone.utc).isoformat(timespec="microseconds")

            sealed_body = {"index": index, "timestamp": ts, **body}
            entry_hash = _hash_entry(prev_hash, sealed_body)

            record = {
                "index": index,
                "timestamp": ts,
                "prev_hash": prev_hash,
                "entry_hash": entry_hash,
                "body": sealed_body,
            }
            data = (json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")

            with open(self.path, "ab") as fh:
                fh.write(data)
                fh.flush()
                os.fsync(fh.fileno())
                st = os.fstat(fh.fileno())

            hasher.update(data)
            key = os.path.realpath(self.path)
            with _VERIFIED_GUARD:
                if st.st_size == verified_size + len(data):
                    _VERIFIED[key] = _VerifiedState(
                        st.st_dev, st.st_ino, st.st_size, index + 1, entry_hash, hasher.digest()
                    )
                else:
                    # كتبَ غيرُنا بلا القفلِ أثناءَ كتابتِنا: لا نعرفُ ما على القرصِ يقينًا،
                    # فنُسقِطُ الحالةَ ويعودُ الإلحاقُ التالي إلى التحقّقِ الكامل (لا إلى الثقة).
                    _VERIFIED.pop(key, None)

            return LedgerEntry(index, ts, prev_hash, entry_hash, sealed_body)

    def _verified_snapshot(self) -> tuple[int, str, int, Any]:
        """حالُ السجلِّ على القرصِ بعدَ التحقّقِ منه — يُنادى داخلَ القفلِ وحدَه.

        يُعيدُ (عددَ القيود · آخرَ بصمة · طولَ البايتاتِ المُتحقَّقِ منها · sha256 جاريًا عليها).
        أوّلَ مرّةٍ للمسارِ في العمليّة: تحقّقٌ كاملٌ كما كان. وبعدَها: بصمةُ بايتاتِ الجزءِ
        المُتحقَّقِ منه تُطابَق (أيُّ تغييرٍ غيرِ إلحاقيٍّ ⇒ رفض) ثمَّ يُتحقَّقُ من الذيلِ وحدَه.
        """
        key = os.path.realpath(self.path)
        st, raw = None, b""
        if self.path.exists():  # داخلَ القفل: لا كاتبَ مشروعًا بينَ الفحصِ والفتح
            with open(self.path, "rb") as fh:
                st = os.fstat(fh.fileno())
                raw = fh.read()
        with _VERIFIED_GUARD:
            state = _VERIFIED.get(key)

        if state is None:
            entries = self._parse(raw.decode("utf-8"), where=str(self.path))
            self._verify(entries)
            last = entries[-1].entry_hash if entries else GENESIS_HASH
            return len(entries), last, len(raw), hashlib.sha256(raw)

        if st is None:
            raise LedgerTamperError(
                f"ملفُّ السجلِّ {self.path} اختفى بعد أن تحقّقت منه هذه العمليّة ({state.count} قيدًا). "
                "حذفُ السجلِّ كلِّه مخالفةٌ دستوريّة (المادة الأولى · 3)."
            )
        if (st.st_dev, st.st_ino) != (state.dev, state.ino):
            raise LedgerTamperError(
                f"ملفُّ السجلِّ {self.path} استُبدِل (inode جديد) بعد أن تحقّقت منه هذه العمليّة. "
                "السجلُّ يُلحَقُ به ولا يُستبدَل (المادة الأولى · 3)."
            )
        view = memoryview(raw)
        hasher = hashlib.sha256(view[: state.size])
        if hasher.digest() != state.prefix_sha256:
            raise LedgerTamperError(
                f"بايتاتُ القيودِ الـ{state.count} المُتحقَّقِ منها في {self.path} تغيّرت: "
                "تعديلٌ أو حذفٌ أو إعادةُ ترتيبٍ أو اقتطاعٌ أو إعادةُ كتابةٍ للسلسلة — "
                "لا إلحاقَ فوقها (المادة الأولى · 3)."
            )
        tail = bytes(view[state.size :])
        new = self._parse(tail.decode("utf-8"), where=f"{self.path} (بعدَ البايت {state.size})")
        self._verify(new, start_index=state.count, prev_hash=state.last_hash)
        hasher.update(tail)
        last = new[-1].entry_hash if new else state.last_hash
        return state.count + len(new), last, len(raw), hasher

    # -- تحقق -------------------------------------------------------------
    @staticmethod
    def _verify(
        entries: list[LedgerEntry], *, start_index: int = 0, prev_hash: str = GENESIS_HASH
    ) -> None:
        prev = prev_hash
        for i, e in enumerate(entries, start=start_index):
            if e.index != i:
                raise LedgerTamperError(
                    f"ترتيب مكسور عند الموضع {i}: القيد يحمل index={e.index}. "
                    "حذف أو إعادة ترتيب قيود مخالفة دستورية (المادة الأولى · 3)."
                )
            if e.prev_hash != prev:
                raise LedgerTamperError(
                    f"سلسلة مكسورة عند القيد {i}: prev_hash={e.prev_hash[:12]}… "
                    f"والمتوقع {prev[:12]}…"
                )
            recomputed = _hash_entry(e.prev_hash, e.body)
            if recomputed != e.entry_hash:
                raise LedgerTamperError(
                    f"محتوى معدَّل في القيد {i}: البصمة المسجلة {e.entry_hash[:12]}… "
                    f"والمحسوبة {recomputed[:12]}…"
                )
            prev = e.entry_hash

    def verify_chain(self) -> list[str]:
        """يرجع قائمة المشاكل (فارغة = سلسلة سليمة). لا يرفع استثناءً."""
        try:
            self._verify(self.entries())
        except LedgerTamperError as exc:
            return [str(exc)]
        return []
