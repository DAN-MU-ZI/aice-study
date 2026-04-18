from __future__ import annotations

from pathlib import Path
from typing import Any

from .checks_format import normalize_text
from .models import Severity, ValidationConfig, ValidationReport


def collect_code_source(notebook: dict[str, Any]) -> str:
    return "\n".join(
        "".join(cell.get("source", []))
        for cell in notebook.get("cells", [])
        if cell.get("cell_type") == "code"
    )


def collect_full_source(notebook: dict[str, Any]) -> str:
    return "\n".join("".join(cell.get("source", [])) for cell in notebook.get("cells", []))


def validate_required_answers(
    solution_source: str,
    required_answers: list[str],
    report: ValidationReport,
    path: Path,
) -> None:
    for answer_name in required_answers:
        if answer_name not in solution_source:
            report.add_error(
                "content.required_answer",
                f"{answer_name} variable is missing from solution notebook",
                path=str(path),
            )


def validate_problem_leakage(
    problem_source: str,
    forbidden_tokens: list[str],
    report: ValidationReport,
    path: Path,
) -> None:
    seen: set[str] = set()
    for token in forbidden_tokens:
        if not token or token in seen:
            continue
        seen.add(token)
        if token in problem_source:
            severity = Severity.ERROR if token.startswith("answer_") else Severity.WARNING
            report.add(
                "content.answer_leakage",
                f"problem notebook contains forbidden token '{token}'",
                severity=severity,
                path=str(path),
            )


def validate_question_text_quality(
    questions: list[str],
    min_length: int,
    report: ValidationReport,
    path: Path,
    label: str,
) -> None:
    for index, question in enumerate(questions, start=1):
        normalized = normalize_text(question.replace("*", ""))
        if not normalized:
            report.add_error(
                "content.question_empty",
                f"{label} question {index} is empty",
                path=str(path),
            )
            continue
        if len(normalized) < min_length:
            report.add_warning(
                "content.question_short",
                f"{label} question {index} may be too short for an exam-style prompt",
                path=str(path),
            )


def validate_required_markers(
    combined_markdown: str,
    markers: list[str],
    report: ValidationReport,
    code: str,
    path: Path,
    noun: str,
) -> None:
    normalized_source = normalize_text(combined_markdown)
    for marker in markers:
        if normalize_text(marker) not in normalized_source:
            report.add_error(code, f"missing required {noun}: {marker}", path=str(path))


def validate_required_closing(
    combined_markdown: str,
    closing_text: str | None,
    report: ValidationReport,
    path: Path,
) -> None:
    if closing_text and normalize_text(closing_text) not in normalize_text(combined_markdown):
        report.add_error(
            "content.required_closing",
            "problem notebook is missing the expected closing text",
            path=str(path),
        )


def run_content_checks(
    state: dict[str, Any],
    config: ValidationConfig,
    report: ValidationReport,
) -> None:
    problem_nb = state.get("problem_nb")
    solution_nb = state.get("solution_nb")
    if problem_nb is None or solution_nb is None:
        report.add_warning(
            "content.skipped",
            "content checks skipped because notebook parsing failed",
        )
        return

    problem_path = state["problem_path"]
    solution_path = state["solution_path"]
    problem_questions = state["problem_questions"]
    solution_questions = state["solution_questions"]
    problem_markdown = state["problem_markdown"]

    validate_required_answers(
        collect_code_source(solution_nb),
        config.required_answers,
        report,
        solution_path,
    )

    forbidden_tokens = list(config.forbidden_problem_tokens)
    if not forbidden_tokens:
        forbidden_tokens = list(config.required_answers)
    validate_problem_leakage(collect_full_source(problem_nb), forbidden_tokens, report, problem_path)

    validate_question_text_quality(
        problem_questions,
        config.min_question_text_length,
        report,
        problem_path,
        "problem.ipynb",
    )
    validate_question_text_quality(
        solution_questions,
        config.min_question_text_length,
        report,
        solution_path,
        "solution.ipynb",
    )
    validate_required_markers(
        problem_markdown,
        config.required_sections,
        report,
        "content.required_section",
        problem_path,
        "section",
    )
    validate_required_markers(
        problem_markdown,
        config.required_notices,
        report,
        "content.required_notice",
        problem_path,
        "notice",
    )
    validate_required_closing(problem_markdown, config.required_closing, report, problem_path)
