from __future__ import annotations

import argparse
from pathlib import Path

from aice_generator import load_profile, write_package


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an AICE Associate notebook package from a JSON profile."
    )
    parser.add_argument(
        "--profile",
        required=True,
        help="Path to the dataset profile JSON.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where the notebook package will be written.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    profile = load_profile(Path(args.profile))
    write_package(profile, Path(args.output_dir))


if __name__ == "__main__":
    main()
