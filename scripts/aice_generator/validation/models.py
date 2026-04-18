from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Severity(str, Enum):
    ERROR = "error"
    WARNING = "warning"


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    severity: Severity
    message: str
    path: str | None = None


@dataclass(frozen=True)
class ValidationConfig:
    expected_question_count: int = 14
    required_answers: list[str] = field(default_factory=list)
    required_sections: list[str] = field(default_factory=list)
    required_notices: list[str] = field(default_factory=list)
    required_closing: str | None = None
    min_question_text_length: int = 20
    forbidden_problem_tokens: list[str] = field(default_factory=list)


@dataclass
class ValidationReport:
    issues: list[ValidationIssue] = field(default_factory=list)

    def add(
        self,
        code: str,
        message: str,
        *,
        severity: Severity = Severity.ERROR,
        path: str | None = None,
    ) -> None:
        self.issues.append(
            ValidationIssue(code=code, severity=severity, message=message, path=path)
        )

    def add_error(self, code: str, message: str, *, path: str | None = None) -> None:
        self.add(code, message, severity=Severity.ERROR, path=path)

    def add_warning(self, code: str, message: str, *, path: str | None = None) -> None:
        self.add(code, message, severity=Severity.WARNING, path=path)

    @property
    def error_count(self) -> int:
        return sum(issue.severity == Severity.ERROR for issue in self.issues)

    @property
    def warning_count(self) -> int:
        return sum(issue.severity == Severity.WARNING for issue in self.issues)

    @property
    def has_errors(self) -> bool:
        return self.error_count > 0

    def render_text(self) -> str:
        status = "failed" if self.has_errors else "passed"
        lines = [
            f"Validation {status}: {self.error_count} error(s), {self.warning_count} warning(s)"
        ]
        for issue in self.issues:
            location = f" [{issue.path}]" if issue.path else ""
            lines.append(
                f"[{issue.severity.value.upper()}] {issue.code}{location}: {issue.message}"
            )
        return "\n".join(lines)
