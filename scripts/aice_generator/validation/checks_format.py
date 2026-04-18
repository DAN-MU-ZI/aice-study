from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .models import ValidationConfig, ValidationReport


REQUIRED_NOTEBOOK_KEYS = ("cells", "metadata", "nbformat", "nbformat_minor")
QUESTION_PREFIX = "### **"
QUESTION_PATTERN = re.compile(r"^### \*\*(\d+)\.")


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def read_notebook(path: Path, report: ValidationReport, label: str) -> dict[str, Any] | None:
    if not path.exists():
        report.add_error("format.file_missing", f"{label} not found", path=str(path))
        return None

    raw = path.read_bytes()
    utf8_bom = b"\xef\xbb\xbf"
    if raw.startswith(utf8_bom):
        report.add_error("format.utf8_bom", f"{label} must be UTF-8 without BOM", path=str(path))

    try:
        notebook = json.loads(raw.decode("utf-8"))
    except UnicodeDecodeError as exc:
        report.add_error("format.decode", f"{label} could not be decoded as UTF-8: {exc}", path=str(path))
        return None
    except json.JSONDecodeError as exc:
        report.add_error("format.json", f"{label} is not valid JSON: {exc}", path=str(path))
        return None

    for key in REQUIRED_NOTEBOOK_KEYS:
        if key not in notebook:
            report.add_error("format.schema", f"{label} is missing top-level key '{key}'", path=str(path))

    cells = notebook.get("cells")
    if not isinstance(cells, list):
        report.add_error("format.cells_type", f"{label} has invalid cells payload", path=str(path))
        return None
    if not cells:
        report.add_error("format.empty", f"{label} notebook is empty", path=str(path))

    return notebook


def extract_markdown_texts(notebook: dict[str, Any]) -> list[str]:
    texts: list[str] = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown":
            texts.append("".join(cell.get("source", [])))
    return texts


def extract_question_markdowns(notebook: dict[str, Any]) -> list[str]:
    return [
        text
        for text in extract_markdown_texts(notebook)
        if text.startswith(QUESTION_PREFIX) and QUESTION_PATTERN.match(text)
    ]


def validate_question_numbering(
    questions: list[str],
    expected_count: int,
    report: ValidationReport,
    label: str,
    path: Path,
) -> None:
    numbers: list[int] = []
    for index, question in enumerate(questions, start=1):
        match = QUESTION_PATTERN.match(question)
        if not match:
            report.add_error(
                "format.question_title",
                f"{label} question {index} does not match the expected markdown title format",
                path=str(path),
            )
            continue
        numbers.append(int(match.group(1)))

    if len(numbers) >= expected_count:
        expected_numbers = list(range(1, expected_count + 1))
        if numbers[:expected_count] != expected_numbers:
            report.add_error(
                "format.question_numbering",
                f"{label} question numbering must start at 1 and increase sequentially",
                path=str(path),
            )


def validate_question_alignment(
    problem_questions: list[str],
    solution_questions: list[str],
    report: ValidationReport,
    problem_path: Path,
) -> None:
    aligned_problem = [normalize_text(text) for text in problem_questions]
    aligned_solution = [normalize_text(text) for text in solution_questions]
    if aligned_problem != aligned_solution:
        report.add_error(
            "format.question_order",
            "problem and solution notebooks do not share the same question order",
            path=str(problem_path),
        )


def run_format_checks(
    package_dir: Path,
    config: ValidationConfig,
    report: ValidationReport,
) -> dict[str, Any]:
    problem_path = package_dir / "problem.ipynb"
    solution_path = package_dir / "solution.ipynb"

    problem_nb = read_notebook(problem_path, report, "problem.ipynb")
    solution_nb = read_notebook(solution_path, report, "solution.ipynb")

    state: dict[str, Any] = {
        "problem_path": problem_path,
        "solution_path": solution_path,
        "problem_nb": problem_nb,
        "solution_nb": solution_nb,
        "problem_questions": [],
        "solution_questions": [],
        "problem_markdown": "",
        "solution_markdown": "",
    }

    if problem_nb is None or solution_nb is None:
        return state

    problem_questions = extract_question_markdowns(problem_nb)
    solution_questions = extract_question_markdowns(solution_nb)

    state["problem_questions"] = problem_questions
    state["solution_questions"] = solution_questions
    state["problem_markdown"] = "\n".join(extract_markdown_texts(problem_nb))
    state["solution_markdown"] = "\n".join(extract_markdown_texts(solution_nb))

    if len(problem_questions) != config.expected_question_count:
        report.add_error(
            "format.problem_question_count",
            f"problem notebook must contain {config.expected_question_count} scored questions; found {len(problem_questions)}",
            path=str(problem_path),
        )
    if len(solution_questions) != config.expected_question_count:
        report.add_error(
            "format.solution_question_count",
            f"solution notebook must contain {config.expected_question_count} scored questions; found {len(solution_questions)}",
            path=str(solution_path),
        )

    validate_question_numbering(
        problem_questions,
        config.expected_question_count,
        report,
        "problem.ipynb",
        problem_path,
    )
    validate_question_numbering(
        solution_questions,
        config.expected_question_count,
        report,
        "solution.ipynb",
        solution_path,
    )
    validate_question_alignment(problem_questions, solution_questions, report, problem_path)

    return state
