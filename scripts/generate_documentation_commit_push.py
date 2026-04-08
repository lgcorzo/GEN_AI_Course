#!/usr/bin/env python3
"""Generate documentation in README and wiki before commit/push."""

import argparse
import os
import subprocess
from datetime import datetime


README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")
WIKI_PATH = os.path.join(os.path.dirname(__file__), "..", "wiki", "architecture.md")


def get_changed_files() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--staged"],
        capture_output=True,
        text=True,
        check=False,
    )
    files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    if not files:
        result = subprocess.run(
            ["git", "diff", "--name-only"],
            capture_output=True,
            text=True,
            check=True,
        )
        files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return files


def render_readme_section(changed_files: list[str], commit_message: str) -> str:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    file_list = "\n".join(f"- `{path}`" for path in changed_files) if changed_files else "- No tracked changes detected."
    return (
        "<!-- DOC_SUMMARY_START -->\n"
        "## Documentation Summary\n\n"
        f"- Generated: {now}\n"
        f"- Commit message: {commit_message}\n"
        f"- Updated files:\n{file_list}\n\n"
        "This section is generated automatically by `scripts/generate_documentation_commit_push.py`.\n"
        "<!-- DOC_SUMMARY_END -->"
    )


def update_readme(changed_files: list[str], commit_message: str) -> None:
    with open(README_PATH, "r", encoding="utf-8") as handle:
        content = handle.read()

    start_marker = "<!-- DOC_SUMMARY_START -->"
    end_marker = "<!-- DOC_SUMMARY_END -->"
    new_section = render_readme_section(changed_files, commit_message)

    if start_marker in content and end_marker in content:
        before, _rest = content.split(start_marker, 1)
        _, after = _rest.split(end_marker, 1)
        content = before + new_section + after
    else:
        content = content.strip() + "\n\n" + new_section + "\n"

    with open(README_PATH, "w", encoding="utf-8") as handle:
        handle.write(content)


def refresh_wiki_architecture() -> None:
    if not os.path.exists(WIKI_PATH):
        raise FileNotFoundError(f"Wiki architecture file not found: {WIKI_PATH}")

    with open(WIKI_PATH, "r", encoding="utf-8") as handle:
        content = handle.read()

    header = "# Architecture Documentation"
    if header not in content:
        raise ValueError("Expected architecture documentation file header not found.")

    # The script currently keeps the existing architecture file unchanged,
    # but it can be extended to rewrite or enrich the page automatically.
    print(f"Wiki architecture file exists at {WIKI_PATH}. Review or update diagrams manually if needed.")


def git_commit_and_push(commit_message: str, push: bool) -> None:
    subprocess.run(["git", "add", README_PATH, WIKI_PATH], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    if push:
        subprocess.run(["git", "push"], check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate README and wiki documentation before commit or push."
    )
    parser.add_argument(
        "--commit-message",
        default="Update documentation and push changes",
        help="Commit message for generated documentation updates.",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push the commit after creating documentation.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    changed_files = get_changed_files()
    update_readme(changed_files, args.commit_message)
    refresh_wiki_architecture()

    print("Documentation updated in README and wiki architecture file.")
    if args.push:
        git_commit_and_push(args.commit_message, push=True)
        print("Changes committed and pushed.")
    else:
        print("Run `git add README.md wiki/architecture.md` and commit locally when ready.")


if __name__ == "__main__":
    main()
