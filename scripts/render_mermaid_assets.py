from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import mermaido


DEFAULT_ROOTS = [
    Path("notebooks"),
    Path("tmp/style-audit"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render Mermaid .mmd assets to .svg with mermaid-cli."
    )
    parser.add_argument(
        "roots",
        nargs="*",
        help="Directories or .mmd files to render. Defaults to notebooks/ and tmp/style-audit/.",
    )
    parser.add_argument(
        "--pattern",
        default="*.mmd",
        help="Glob pattern for Mermaid source files when scanning directories.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress per-file progress output.",
    )
    return parser.parse_args()


def resolve_targets(args: argparse.Namespace) -> list[Path]:
    roots = [Path(item) for item in args.roots] if args.roots else DEFAULT_ROOTS
    targets: list[Path] = []

    for root in roots:
        if not root.exists():
            print(f"skip missing path: {root}", file=sys.stderr)
            continue
        if root.is_file():
            if root.suffix == ".mmd":
                targets.append(root)
            continue
        targets.extend(sorted(root.rglob(args.pattern)))

    seen: set[Path] = set()
    unique_targets: list[Path] = []
    for target in targets:
        resolved = target.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique_targets.append(target)
    return unique_targets


def render_file(source: Path, quiet: bool) -> None:
    output = source.with_suffix(".svg")
    if not quiet:
        print(f"render {source} -> {output}")

    if os.name == "nt":
        mmdc_cmd = Path(str(mermaido._MMDC) + ".cmd")
        if mmdc_cmd.exists():
            mermaido._MMDC = mmdc_cmd

    mermaido.render(source.read_text(encoding="utf-8"), output)


def main() -> int:
    args = parse_args()
    targets = resolve_targets(args)

    if not targets:
        print("no mermaid source files found")
        return 0

    for target in targets:
        render_file(target, quiet=args.quiet)

    print(f"rendered {len(targets)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
