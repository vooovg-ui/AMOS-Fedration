#!/usr/bin/env python3
"""
حرسُ أسماءِ الملفّاتِ في جذرِ المستودعِ — Root File Names Guard

الهدف: تحويلُ القاعدةِ 14 من نصٍّ مكتوبٍ في دليلِ المشروعِ إلى **فحصٍ يُسقِطُ
       البناءَ**، فيُمنَعَ تكرارُ حادثةِ `W-038`: دفعٌ بُنِيَت شجرتُه من مفاتيحِ
       فهرسةِ الأجسامِ لا من خريطةِ المساراتِ، فهبطَ ثلاثةَ عشرَ ملفًّا محتواها
       صحيحٌ بايتًا وأسماؤها `0…12` في جذرِ المستودعِ، **ومرَّت سبعُ وظائفَ
       خضراءَ** لأنَّها قاسَت شجرةً لم يمسَّها العملُ.
النطاق: أسماءُ ملفّاتِ الجذرِ (لا محتواها)، وأسماءُ كلِّ ملفٍّ في الشجرةِ بحثًا عن
       أسماءِ مفاتيحِ الفهرسةِ.
المالك: tools/governance — المجلس التأسيسي
تاريخ الإنشاء: 2026-08-25
تاريخ آخر تعديل: 2026-08-25

## لماذا إعلانٌ مُغلَقٌ لا نمطٌ مفتوحٌ

منعُ الأرقامِ وحدَها حرسٌ ناقصٌ: الحادثةُ التاليةُ قد تُسمّي الملفَّ `blob` أو
`tmp` أو بصمةً سِتَّ عشريّةً. فالحرسُ هنا **إعلانٌ مُغلَقٌ** (`DECLARED_ROOT_FILES`):
كلُّ ملفٍّ في الجذرِ غيرُ مُعلَنٍ **مخالفةٌ**، لا كلُّ ملفٍّ يُشبِهُ ما رأيناه. وإضافةُ
ملفٍّ جذريٍّ جديدٍ تلزمُها **يدُ إنسانٍ تُعلِنُه هنا** — وهذا هو المقصودُ: الجذرُ
سطحُ عقدٍ لا مُلقًى.

وتُقاسُ الجهةُ الأخرى كذلك: **مُعلَنٌ غائبٌ مخالفةٌ** — لئلّا يتعفَّنَ الإعلانُ
فيصيرَ قائمةً لملفّاتٍ لا وجودَ لها، فيَضعُفَ الحرسُ بلا أن يحمرَّ.

## حدُّ هذا الحرسِ — مُعلَنًا لا مستورًا

هذا الفحصُ يقرأُ **الشجرةَ الحاضرةَ** لا **قائمةَ ملفّاتِ الالتزامِ**. فهو يمنعُ
بقاءَ الغريبِ، ولا يُغني عن الشطرِ الأوّلِ من القاعدةِ 14: أن يقرأَ الدافعُ
`GET /commits/{sha}` ← `files[].filename` ويُطابِقَه بخريطةِ ما نوى دفعَه **قبلَ**
أن يقرأَ حكمَ CI. الشطرُ الأوّلُ فعلُ إنسانٍ، والشطرُ الثاني — أن لا يبقى غريبٌ في
الجذرِ — هو ما يحرسُه هذا الملفُّ.

أنواعُ المخالفاتِ:
  INDEX_KEY_NAME          اسمُ ملفٍّ رقمٌ محضٌ (بصمةُ حادثةِ W-038) أينما كانَ
  ROOT_FILE_WITHOUT_SUFFIX  ملفُّ جذرٍ بلا لاحقةٍ وليسَ من المُعلَنِ
  UNDECLARED_ROOT_FILE    ملفٌّ في الجذرِ غيرُ مُعلَنٍ في هذه الأداةِ
  DECLARED_FILE_MISSING   مُعلَنٌ في هذه الأداةِ غائبٌ عن الجذرِ

الاستخدام:
    python tools/governance/check_root_file_names.py .
    python tools/governance/check_root_file_names.py . --json out.json
    python tools/governance/check_root_file_names.py . --source disk

ومصدرُ الأسماءِ **مُعلَنٌ لا مُستنتَجٌ**: الافتراضُ سجلُّ git، وحينَ يغيبُ لا يهبِطُ
الحرسُ صامتًا إلى قراءةِ القرصِ بل **يرتفعُ برمزِ 2** حتى يُعلِنَ المُشغِّلُ
`--source disk` بيدِه — فحرسٌ يقيسُ شجرةً غيرَ التي يُظَنُّ أنّه يقيسُها هو عينُ
علّةِ `W-038`.

رموزُ الخروج: 0 لا مخالفةَ · 1 مخالفةٌ واحدةٌ أو أكثرُ · 2 خطأُ استخدامٍ أو مصدرٌ
غائبٌ.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

# ── الإعلانُ الواحدُ لملفّاتِ الجذرِ ─────────────────────────────────────────────
# قِيسَ من شجرةِ `be4c44a` (رأسُ main بعدَ دمجِ W-039) وهي عشرةٌ لا أكثرُ.
DECLARED_ROOT_FILES = {
    ".env.example": "نموذجُ إعلانِ البيئةِ — لا أسرارَ فيه",
    ".gitignore": "إعلانُ ما لا يُتعقَّبُ",
    "ARCHITECTURE.md": "وثيقةُ العمارةِ",
    "EXECUTION_PLAN.md": "خطةُ التنفيذِ",
    "PROJECT_STATE.md": "حالةُ المشروعِ المُعلَنةُ",
    "README.md": "بطاقةُ هويّةِ الجذرِ (المادةُ التاسعةُ)",
    "conftest.py": "عزلُ مخرَجِ التشغيلِ عن الشجرةِ",
    "pytest.ini": "إعلانُ محرِّكِ الاختبارِ",
    "requirements-dev.txt": "تبعيّاتُ التطويرِ المُعلَنةُ",
    "requirements-tools.txt": "تبعيّاتُ الأدواتِ المُعلَنةُ",
}

SKIP_DIRS = {
    ".git", "__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache",
    "node_modules", ".venv", "venv", ".idea", ".vscode", "htmlcov",
}


class SourceUnavailable(RuntimeError):
    """مصدرُ الأسماءِ المطلوبُ غيرُ متاحٍ — ولا هبوطَ صامتًا إلى غيرِه."""


def _tracked_files(root: Path) -> list[Path]:
    """أسماءُ الملفّاتِ المُتعقَّبةِ من سجلِّ git — أو ارتفاعٌ مُعلَنٌ.

    سجلُّ git هو المصدرُ الافتراضيُّ لأنَّ مخرَجَ تشغيلٍ غيرِ مُتعقَّبٍ ليس دفعًا فلا
    يُحاكَمُ عليه. **ولا هبوطَ صامتًا إلى قراءةِ القرصِ حينَ يغيبُ السجلُّ**: الهبوطُ
    الصامتُ هو ما يجعلُ الحرسَ يقيسُ شجرةً غيرَ التي يُظَنُّ أنّه يقيسُها — وهي علّةُ
    حادثةِ `W-038` نفسِها. فمن أرادَ قراءةَ القرصِ أعلنَها بـ`--source disk`.
    """
    if shutil.which("git") is None:
        raise SourceUnavailable(
            "لا أداةَ git في البيئةِ — أعلِنِ المصدرَ صريحًا بـ`--source disk`"
        )
    out = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        capture_output=True, text=True, timeout=120,
    )
    if out.returncode != 0:
        raise SourceUnavailable(
            "سجلُّ git لا يُقرأُ في هذا المسارِ: "
            + (out.stderr.strip() or f"رمزُ {out.returncode}")
            + " — أعلِنِ المصدرَ صريحًا بـ`--source disk`"
        )
    if not out.stdout:
        raise SourceUnavailable("سجلُّ git لا يُعلِنُ ملفًّا واحدًا مُتعقَّبًا")
    return [Path(p) for p in out.stdout.split("\0") if p]


def _walked_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        parts = set(path.relative_to(root).parts)
        if parts & SKIP_DIRS:
            continue
        files.append(path.relative_to(root))
    return files


def collect(root: Path, source: str = "git") -> tuple[list[Path], str]:
    """أسماءُ الشجرةِ من المصدرِ **المُعلَنِ** — `git` أو `disk`، ولا ثالثَ صامتًا."""
    if source == "git":
        return _tracked_files(root), "git ls-files"
    if source == "disk":
        return _walked_files(root), "قراءةُ القرصِ (مُعلَنةً بـ--source disk)"
    raise SourceUnavailable(f"مصدرٌ غيرُ معروفٍ: {source}")


def audit(root: Path, source: str = "git") -> tuple[list[dict], str]:
    """اقرأْ أسماءَ الشجرةِ واحكمْ — بلا كتابةِ بايتٍ واحدٍ فيها."""
    files, source_label = collect(root, source)
    violations: list[dict] = []

    for rel in files:
        if rel.name.isdigit():
            violations.append({
                "kind": "INDEX_KEY_NAME",
                "path": str(rel),
                "detail": (
                    "اسمُ الملفِّ رقمٌ محضٌ — وهي بصمةُ حادثةِ W-038: شجرةٌ بُنِيَت "
                    "من مفاتيحِ فهرسةِ الأجسامِ لا من خريطةِ المساراتِ"
                ),
            })

    root_files = sorted({rel.name for rel in files if len(rel.parts) == 1})
    for name in root_files:
        if name in DECLARED_ROOT_FILES:
            continue
        if not Path(name).suffix:
            violations.append({
                "kind": "ROOT_FILE_WITHOUT_SUFFIX",
                "path": name,
                "detail": "ملفُّ جذرٍ بلا لاحقةٍ وليسَ من المُعلَنِ في هذه الأداةِ",
            })
        else:
            violations.append({
                "kind": "UNDECLARED_ROOT_FILE",
                "path": name,
                "detail": (
                    "ملفٌّ في جذرِ المستودعِ غيرُ مُعلَنٍ — الجذرُ سطحُ عقدٍ: "
                    "أعلِنْه في DECLARED_ROOT_FILES بيدِ إنسانٍ أو انقلْه إلى موضعِه"
                ),
            })

    present = set(root_files)
    for name in sorted(DECLARED_ROOT_FILES):
        if name not in present:
            violations.append({
                "kind": "DECLARED_FILE_MISSING",
                "path": name,
                "detail": (
                    "مُعلَنٌ في هذه الأداةِ وغائبٌ عن الجذرِ — الإعلانُ لا يُترَكُ "
                    "يتعفَّنُ فيَضعُفَ الحرسُ بلا حُمرةٍ"
                ),
            })

    return violations, source_label


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="حرسُ أسماءِ الملفّاتِ في جذرِ المستودعِ (القاعدةُ 14)",
    )
    parser.add_argument("root", nargs="?", default=".", help="جذرُ المستودعِ")
    parser.add_argument("--json", dest="json_path", help="اكتبِ الحكمَ ملفَّ JSON")
    parser.add_argument(
        "--source", choices=("git", "disk"), default="git",
        help="مصدرُ الأسماءِ: سجلُّ git (الافتراضُ) أو قراءةُ القرصِ مُعلَنةً",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"خطأ: ليس مجلدًا: {root}", file=sys.stderr)
        return 2

    try:
        violations, source = audit(root, args.source)
    except SourceUnavailable as exc:
        print(f"خطأ: {exc}", file=sys.stderr)
        return 2
    payload = {
        "root": str(root),
        "source": source,
        "declared_root_files": sorted(DECLARED_ROOT_FILES),
        "violations": violations,
        "summary": {
            "total": len(violations),
            **{
                kind: sum(1 for v in violations if v["kind"] == kind)
                for kind in (
                    "INDEX_KEY_NAME",
                    "ROOT_FILE_WITHOUT_SUFFIX",
                    "UNDECLARED_ROOT_FILE",
                    "DECLARED_FILE_MISSING",
                )
            },
        },
    }

    if args.json_path:
        Path(args.json_path).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(f"[ROOT NAMES GATE] المصدرُ: {source}")
    print(f"[ROOT NAMES GATE] المُعلَنُ في الجذرِ: {len(DECLARED_ROOT_FILES)} ملفًّا")
    if not violations:
        print("[ROOT NAMES GATE] ✓ لا اسمَ غريبًا في الجذرِ ولا اسمَ مفتاحِ فهرسةٍ في الشجرةِ.")
        return 0

    print(f"[ROOT NAMES GATE] ✗ {len(violations)} مخالفة:")
    for v in violations:
        print(f"  {v['kind']}: {v['path']} — {v['detail']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
