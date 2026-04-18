from __future__ import annotations

import json
from pathlib import Path

from .models import ExamProfile


def load_profile(profile_path: Path) -> ExamProfile:
    data = json.loads(profile_path.read_text(encoding="utf-8"))
    return ExamProfile.from_dict(data)
