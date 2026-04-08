#!/usr/bin/env python3
"""Script to demonstrate the DDD folder structure."""

import os
from pathlib import Path


def show_structure(root_path: str) -> None:
    """Print the folder structure starting from root_path."""
    root = Path(root_path)
    for path in sorted(root.rglob("*")):
        if path.is_file():
            level = len(path.relative_to(root).parts) - 1
            indent = "  " * level
            print(f"{indent}{path.name}")


if __name__ == "__main__":
    print("DDD Folder Structure for Code and Tests:")
    print("=" * 50)
    show_structure("src")
    print("\nTests Structure:")
    print("=" * 20)
    show_structure("tests")