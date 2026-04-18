from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ColumnSpec:
    name: str
    description: str
    note: str


@dataclass(frozen=True)
class QuestionSpec:
    title: str
    section: str | None = None
    guide: str | None = None
    visual: str | None = None
    problem_visual: str | None = None
    solution_visual: str | None = None
    problem_notice: str | None = None
    solution_notice: str | None = None
    problem_setup_code: str | None = None
    solution_setup_code: str | None = None
    problem_code: str | None = None
    solution_code: str | None = None
    problem_extra_code: list[str] = field(default_factory=list)
    solution_extra_code: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "QuestionSpec":
        return cls(
            title=data["title"],
            section=data.get("section"),
            guide=data.get("guide"),
            visual=data.get("visual"),
            problem_visual=data.get("problem_visual"),
            solution_visual=data.get("solution_visual"),
            problem_notice=data.get("problem_notice"),
            solution_notice=data.get("solution_notice"),
            problem_setup_code=data.get("problem_setup_code"),
            solution_setup_code=data.get("solution_setup_code"),
            problem_code=data.get("problem_code"),
            solution_code=data.get("solution_code"),
            problem_extra_code=list(data.get("problem_extra_code", [])),
            solution_extra_code=list(data.get("solution_extra_code", [])),
        )


@dataclass(frozen=True)
class ExamProfile:
    scenario_title: str
    domain: str
    goal: str
    scenario: str
    data_file: str
    submission_file: str
    cautions: list[str]
    columns: list[ColumnSpec]
    questions: list[QuestionSpec]
    problem_closing: str
    solution_closing: str
    raw_files: list[str]
    required_answers: list[str]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ExamProfile":
        raw_files = list(data.get("raw_files", [data["data_file"]]))
        return cls(
            scenario_title=data["scenario_title"],
            domain=data["domain"],
            goal=data["goal"],
            scenario=data["scenario"],
            data_file=data["data_file"],
            submission_file=data["submission_file"],
            cautions=list(data["cautions"]),
            columns=[ColumnSpec(**column) for column in data["columns"]],
            questions=[QuestionSpec.from_dict(question) for question in data["questions"]],
            problem_closing=data["problem_closing"],
            solution_closing=data["solution_closing"],
            raw_files=raw_files,
            required_answers=list(data.get("required_answers", [])),
        )
