"""الهدف: `legal_search` حقيقيّ — بحثٌ في نصِّ الدستورِ يجري داخلَ صندوقٍ معزولٍ فعلًا، أو لا يجري.

النطاق: services/tool_registry
المالك: federal/executive/services
تاريخ الإنشاء: 2026-10-10 (WI-067 · قرارُ المالكِ في Q-33)

## القرار

Q-33 سألَ: سجلُّ الأدواتِ يقولُ «معزولة» والتشغيلُ لا يعزلُ شيئًا — فما الحقيقة؟ وأجابَ المالكُ
في 2026-10-10 عن `legal_search` بعينِها: «تشغيل legal_search داخل sandbox فعلي». فهذه الوحدةُ
هي التنفيذ، ولا تتعدّاه إلى أداةٍ أخرى (‏الشقّانِ (٢) و(٣) من Q-33 باقيانِ لقرارِ المالك).

## ما كانَ قبلَها

لا تنفيذَ حقيقيٌّ لـ`legal_search` في أيِّ مكان: `tool_registry` يُرجِعُ `unknown_tool`،
وبيئةُ تشغيلِ الوكلاءِ تُرجِعُ «نص قانوني / المادة 1» مُصطنَعًا مُعلَنًا `SIMULATION`.

## ما تفعلُه

- **المصدر:** ملفّاتُ `core/constitution/**.md` — النصُّ نفسُه لا نسخةٌ ولا بياناتٌ ثابتة.
- **العزل:** `BubblewrapProvider` بتركيبِ المدوَّنةِ **للقراءةِ وحدَها** في `/corpus`؛ ولا يرى
  البحثُ غيرَها من المستودع، ولا شبكةَ، ولا بيئةَ المضيف.
- **لا سقوط:** إن لم يتوفّرِ الصندوقُ أو المدوَّنةُ تُرجَعُ `sandbox_unavailable` بـ
  `execution_fidelity = UNAVAILABLE` وسببِها — لا تنفيذَ على المضيفِ بلا عزل، ولا محاكاة.
- **المطابقة:** نصٌّ مُطبَّعٌ (‏بلا تشكيلٍ ولا تطويل، وألفاتٌ موحَّدة، وأحرفٌ صغيرة) يحوي كلَّ
  كلماتِ الاستعلام في السطرِ نفسِه.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

#: مسارُ المدوَّنةِ داخلَ الصندوق.
CORPUS_MOUNT = "/corpus"

#: أقصى عددِ نتائجَ يُقبَل.
MAX_RESULTS_CAP = 50

#: الشِّفرةُ التي تجري داخلَ الصندوق — مكتبةُ بايثون القياسيّةُ وحدَها، ولا شبكةَ ولا كتابةَ خارجَ /work.
_SEARCH_SCRIPT = r"""
import json, os, re, sys, unicodedata
PARAMS = json.loads(__PARAMS__)
_DIACRITICS = re.compile("[\u064B-\u0652\u0670\u0640]")
_ALEF = str.maketrans({"\u0623": "\u0627", "\u0625": "\u0627", "\u0622": "\u0627", "\u0671": "\u0627"})

def norm(text):
    text = unicodedata.normalize("NFKC", text)
    return _DIACRITICS.sub("", text).translate(_ALEF).casefold()

terms = [t for t in norm(PARAMS["query"]).split() if t]
if not terms:
    print(json.dumps({"error": "empty_query"}))
    sys.exit(2)
limit = PARAMS["max_results"]
root = "/corpus"
results, scanned = [], 0
for dirpath, dirnames, filenames in os.walk(root):
    dirnames.sort()
    for name in sorted(filenames):
        if not name.endswith(".md"):
            continue
        path = os.path.join(dirpath, name)
        scanned += 1
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        title = next((l.lstrip("#").strip() for l in lines if l.startswith("#")), name)
        for number, line in enumerate(lines, 1):
            if all(t in norm(line) for t in terms):
                results.append({
                    "source": os.path.relpath(path, root),
                    "title": title,
                    "line": number,
                    "snippet": line.strip()[:300],
                })
total = len(results)
print(json.dumps({"query": PARAMS["query"], "terms": terms, "files_scanned": scanned,
                  "total_matches": total, "results": results[:limit]}, ensure_ascii=False))
"""


def corpus_dir() -> Path | None:
    """`AMOS_LEGAL_CORPUS_DIR` إن ضُبِط، وإلّا `core/constitution` في أقربِ جذرٍ للمستودع."""
    override = os.environ.get("AMOS_LEGAL_CORPUS_DIR")
    if override:
        path = Path(override)
        return path if path.is_dir() else None
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "core" / "constitution"
        if candidate.is_dir():
            return candidate
    return None


def unavailable(tool_id: str, reason: str) -> dict[str, Any]:
    """نتيجةُ الرفض: لا صندوقَ ⇒ لا تنفيذ، بسببٍ مُسمّى."""
    return {
        "error": "sandbox_unavailable",
        "message": reason,
        "tool": tool_id,
        "provider": "bwrap",
        "execution_fidelity": "UNAVAILABLE",
        "fidelity_reason": reason,
        "exit_code": None,
        "returncode": None,
        "results": [],
    }


def prepare(params: dict[str, Any], *, agent_id: Any = None) -> dict[str, Any]:
    """حضِّرِ البحثَ ولا تُنفِّذْه — التنفيذُ في `sandbox._execute_isolated` بعدَ التخويلِ وحدَه.

    يُرجِعُ `{"error": …}` لمُدخَلٍ مرفوضٍ أو مدوَّنةٍ غائبة، وإلّا
    `{"spec", "request", "provider"}` — والمزوِّدُ `BubblewrapProvider` دائمًا، فلا تختارُ البيئةُ
    تنفيذًا غيرَ معزولٍ لهذه الأداة.
    """
    from amos_federation.services.tool_registry.providers.contract import (
        ExecutionContext,
        ExecutionRequest,
        SandboxSpec,
    )
    from amos_federation.services.tool_registry.providers.isolated_provider import (
        BubblewrapProvider,
    )

    tool_id = "legal_search"
    query = str(params.get("query", "")).strip()
    if not query:
        return {"error": "invalid_params", "message": "`query` مطلوب", "tool": tool_id}
    try:
        max_results = int(params.get("max_results", 10))
    except (TypeError, ValueError) as exc:
        logger.warning("legal_search: max_results غيرُ صالح (%s)", exc)
        return {"error": "invalid_params", "message": "`max_results` عددٌ صحيح", "tool": tool_id}
    max_results = max(1, min(max_results, MAX_RESULTS_CAP))

    corpus = corpus_dir()
    if corpus is None:
        return unavailable(tool_id, "مدوَّنةُ الدستورِ (‏core/constitution) غيرُ موجودة")

    payload = json.dumps({"query": query, "max_results": max_results}, ensure_ascii=False)
    return {
        "spec": SandboxSpec(tool_id=tool_id, timeout_seconds=15, memory_limit_mb=256),
        "request": ExecutionRequest(
            code=_SEARCH_SCRIPT.replace("__PARAMS__", repr(payload)),
            context=ExecutionContext(
                tool_id=tool_id,
                agent_id=str(agent_id) if agent_id else None,
                task_id=params.get("task_id"),
            ),
        ),
        "provider": BubblewrapProvider(readonly_mounts={CORPUS_MOUNT: str(corpus)}),
    }


def interpret(result: Any) -> dict[str, Any]:
    """ترجِمْ `ExecutionResult` الصندوقِ إلى نتيجةِ الأداة — والفشلُ فشلٌ مُعلَن."""
    from amos_federation.services.tool_registry.providers.isolated_provider import ISOLATION

    out = result.as_dict()
    out["tool"] = "legal_search"
    out["returncode"] = result.exit_code
    out["isolation"] = ISOLATION
    out["corpus"] = "core/constitution"
    if not result.succeeded:
        out.setdefault("error", "search_failed")
        out["results"] = []
        return out
    try:
        found = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        logger.warning("legal_search: مخرَجُ الصندوقِ ليسَ JSON: %s", exc)
        out["error"] = "malformed_output"
        out["message"] = f"مخرَجُ الصندوقِ ليسَ JSON: {exc}"
        out["results"] = []
        return out
    out.update(found)
    return out
