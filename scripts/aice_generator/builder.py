from __future__ import annotations

import json
from pathlib import Path

from .models import ExamProfile
from .notebook import render_notebook
from .validator import build_validator


def write_package(profile: ExamProfile, output_root: Path) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    raw_dir = output_root / "data" / "raw"
    sub_dir = output_root / "data" / "submissions"
    tests_dir = output_root / "tests"
    raw_dir.mkdir(parents=True, exist_ok=True)
    sub_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)

    problem = render_notebook(profile, "problem")
    solution = render_notebook(profile, "solution")

    (output_root / "problem.ipynb").write_text(
        json.dumps(problem, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (output_root / "solution.ipynb").write_text(
        json.dumps(solution, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (raw_dir / "README.txt").write_text(
        "Place the following files here before executing the notebooks.\n"
        + "\n".join(f"- data/raw/{file_name}" for file_name in profile.raw_files)
        + "\n",
        encoding="utf-8",
    )
    (tests_dir / "validate_notebook.py").write_text(
        build_validator(profile),
        encoding="utf-8",
    )
