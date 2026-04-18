from __future__ import annotations

from typing import Any
from uuid import uuid4

from .models import ExamProfile, QuestionSpec


NOTEBOOK_METADATA = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    },
    "language_info": {
        "name": "python",
        "version": "3.11",
    },
}

TITLE_BANNER = "**AICE Associate <font color=red>\uc2e4\uc804\ubb38\ud56d</font>**"
CAUTION_HEADING = "#### **<span style=\"color:red\">[\uc8fc\uc758\uc0ac\ud56d]</span>**\n"
COLUMN_TABLE_HEADER = (
    "| \uceec\ub7fc\uba85 | \uc124\uba85 | \ube44\uace0 |\n"
    "| --- | --- | --- |\n"
)


def markdown_cell(text: str) -> dict[str, Any]:
    return {
        "cell_type": "markdown",
        "id": uuid4().hex[:8],
        "metadata": {},
        "source": [text],
    }


def code_cell(text: str) -> dict[str, Any]:
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": uuid4().hex[:8],
        "metadata": {},
        "outputs": [],
        "source": [text],
    }


def render_front_matter(profile: ExamProfile) -> list[dict[str, Any]]:
    caution_lines = "\n".join(f"- {line}" for line in profile.cautions)
    column_rows = "\n".join(
        f"| {column.name} | {column.description} | {column.note} |"
        for column in profile.columns
    )
    scenario = (
        f"### **{profile.scenario_title}**\n---\n\n"
        f"- \ub3c4\uba54\uc778: {profile.domain}\n"
        f"- \ubaa9\ud45c: {profile.goal}\n"
        f"- \uc0c1\ud669: {profile.scenario}\n---"
    )
    caution = f"{CAUTION_HEADING}{caution_lines}"
    column_table = (
        f"**[ \ub370\uc774\ud130 \uceec\ub7fc \uc124\uba85 ({profile.data_file}) ]**\n\n"
        f"{COLUMN_TABLE_HEADER}"
        f"{column_rows}"
    )
    return [
        markdown_cell(TITLE_BANNER),
        markdown_cell(scenario),
        markdown_cell(caution),
        markdown_cell(column_table),
    ]


def question_value(question: QuestionSpec, mode: str, key: str) -> str | None:
    mode_value = getattr(question, f"{mode}_{key}")
    if mode_value:
        return mode_value
    return getattr(question, key, None)


def render_question_block(question: QuestionSpec, mode: str) -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = [markdown_cell(question.title)]

    if question.guide:
        cells.append(markdown_cell(question.guide))

    visual = question_value(question, mode, "visual")
    if visual:
        cells.append(markdown_cell(visual))

    notice = question_value(question, mode, "notice")
    if notice:
        cells.append(markdown_cell(notice))

    setup_code = question_value(question, mode, "setup_code")
    if setup_code:
        cells.append(code_cell(setup_code))

    primary_code = question_value(question, mode, "code")
    if primary_code:
        cells.append(code_cell(primary_code))

    extra_code = getattr(question, f"{mode}_extra_code")
    for snippet in extra_code:
        cells.append(code_cell(snippet))

    return cells


def render_notebook(profile: ExamProfile, mode: str) -> dict[str, Any]:
    cells = render_front_matter(profile)
    current_section = None
    for question in profile.questions:
        if question.section and question.section != current_section:
            cells.append(markdown_cell(question.section))
            current_section = question.section
        cells.extend(render_question_block(question, mode))

    cells.append(markdown_cell(getattr(profile, f"{mode}_closing")))
    return {
        "cells": cells,
        "metadata": NOTEBOOK_METADATA,
        "nbformat": 4,
        "nbformat_minor": 5,
    }
