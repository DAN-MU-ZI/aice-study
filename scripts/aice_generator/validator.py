from __future__ import annotations

import re

from .models import ExamProfile


def required_answers(profile: ExamProfile) -> list[str]:
    if profile.required_answers:
        return profile.required_answers

    answers: list[str] = []
    seen: set[str] = set()
    for question in profile.questions:
        code_blocks = [
            question.problem_code,
            question.solution_code,
            *question.problem_extra_code,
            *question.solution_extra_code,
        ]
        for block in code_blocks:
            if not block:
                continue
            for match in re.findall(r"\b(answer_\d+(?:_blank_\d+)?(?:_model)?)\b", block):
                if match not in seen:
                    seen.add(match)
                    answers.append(match)
    return answers


def build_validator(profile: ExamProfile) -> str:
    raw_paths = ",\n".join(
        f"    ROOT / \"data\" / \"raw\" / \"{file_name}\"" for file_name in profile.raw_files
    )
    raw_names = ", ".join(profile.raw_files)
    answer_checks = "\n".join(
        f"assert '{answer_name}' in source_text, '{answer_name} variable is missing from solution notebook'"
        for answer_name in required_answers(profile)
    )
    return f"""import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
problem_path = ROOT / "problem.ipynb"
solution_path = ROOT / "solution.ipynb"
raw_files = [
{raw_paths}
]
submission_csv = ROOT / "data" / "submissions" / "{profile.submission_file}"

assert problem_path.exists(), "problem.ipynb not found"
assert solution_path.exists(), "solution.ipynb not found"

utf8_bom = b"\\xef\\xbb\\xbf"
assert problem_path.read_bytes()[:3] != utf8_bom, "problem.ipynb must be UTF-8 without BOM"
assert solution_path.read_bytes()[:3] != utf8_bom, "solution.ipynb must be UTF-8 without BOM"

problem = json.loads(problem_path.read_text(encoding="utf-8"))
solution = json.loads(solution_path.read_text(encoding="utf-8"))

assert len(problem["cells"]) > 0, "problem notebook is empty"
assert len(solution["cells"]) > 0, "solution notebook is empty"

problem_questions = [
    "".join(cell.get("source", []))
    for cell in problem["cells"]
    if cell.get("cell_type") == "markdown" and "".join(cell.get("source", [])).startswith("### **")
]
solution_questions = [
    "".join(cell.get("source", []))
    for cell in solution["cells"]
    if cell.get("cell_type") == "markdown" and "".join(cell.get("source", [])).startswith("### **")
]

assert problem_questions[:14] == solution_questions[:14], "question order mismatch"
assert sum(
    text.startswith("### **") and any(f"{{n}}." in text for n in range(1, 15))
    for text in problem_questions
) >= 14, "expected 14 scored questions"

source_text = "\\n".join(
    "".join(cell.get("source", []))
    for cell in solution["cells"]
    if cell.get("cell_type") == "code"
)
{answer_checks}

missing_raw = [path.name for path in raw_files if not path.exists()]
if missing_raw:
    print("missing raw files:", missing_raw)
else:
    print("raw files detected: {raw_names}")

if submission_csv.exists():
    print("submission file exists:", submission_csv)
"""
