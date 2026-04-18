from __future__ import annotations

from pathlib import Path

from .checks_content import run_content_checks
from .checks_format import run_format_checks
from .models import ValidationConfig, ValidationReport


def validate_package(package_dir: Path, config: ValidationConfig) -> ValidationReport:
    report = ValidationReport()
    state = run_format_checks(package_dir, config, report)
    run_content_checks(state, config, report)
    return report
