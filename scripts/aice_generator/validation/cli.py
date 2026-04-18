from __future__ import annotations

import argparse
from pathlib import Path

from .models import ValidationConfig
from .runner import validate_package


def run_package_validation(package_dir: Path, config: ValidationConfig) -> int:
    report = validate_package(package_dir, config)
    print(report.render_text())
    return 1 if report.has_errors else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an AICE notebook package.")
    parser.add_argument("--package-dir", required=True, help="Notebook package directory.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run_package_validation(Path(args.package_dir), ValidationConfig())


if __name__ == "__main__":
    raise SystemExit(main())
