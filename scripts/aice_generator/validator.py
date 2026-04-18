from __future__ import annotations

import json
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
    sections = profile.required_sections or _derive_required_sections(profile)
    notices = profile.required_notices or list(profile.cautions)
    forbidden_tokens = profile.forbidden_problem_tokens or required_answers(profile)
    config_literal = json.dumps(
        {
            "expected_question_count": len(profile.questions),
            "required_answers": required_answers(profile),
            "required_sections": sections,
            "required_notices": notices,
            "required_closing": profile.problem_closing,
            "min_question_text_length": profile.min_question_text_length,
            "forbidden_problem_tokens": forbidden_tokens,
        },
        ensure_ascii=True,
        indent=2,
    )
    return f"""from pathlib import Path
import sys

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from aice_generator.validation import ValidationConfig, run_package_validation

CONFIG = ValidationConfig(**{config_literal})

if __name__ == "__main__":
    raise SystemExit(run_package_validation(PACKAGE_ROOT, CONFIG))
"""


def _derive_required_sections(profile: ExamProfile) -> list[str]:
    sections: list[str] = []
    seen: set[str] = set()
    for question in profile.questions:
        if question.section and question.section not in seen:
            seen.add(question.section)
            sections.append(question.section)
    return sections
