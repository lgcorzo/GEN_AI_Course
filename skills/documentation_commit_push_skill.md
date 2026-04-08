# Documentation Commit & Push Skill

This skill defines a repeatable process for generating documentation at commit and push time.
It ensures that every code change is reflected in `README.md` and in architecture documentation stored under `wiki/`.
The documentation follows MLOps lifecycle standards and Domain-Driven Design (DDD) structure, and uses Mermaid diagrams for UML and execution flows.

## Purpose

- Keep change documentation current in the repository root.
- Maintain a dedicated architecture reference in `wiki/architecture.md`.
- Align documentation with MLOps best practices and DDD boundaries.
- Make diagrams easy to inspect using Mermaid syntax.

## Standards

### 1. Commit and Push Documentation

- Generate documentation for every commit or push event.
- Update `README.md` with a summary of the files changed and the purpose of the change.
- Add or refresh `wiki/architecture.md` with architecture-level documentation.
- Use a scripted process to avoid manual drift.

### 2. README Documentation

- Include a `## Documentation Summary` section in `README.md`.
- Document the changes made in the most recent commit or push.
- Keep the summary short, clear, and linked to the relevant files.
- Preserve any existing README content outside of the generated section.

### 3. Wiki Architecture Documentation

- Store architecture docs in `wiki/architecture.md`.
- Use DDD concepts: domain, application, infrastructure, and integration boundaries.
- Describe how MLOps flows are implemented: experiment tracking, model deployment, monitoring, and retraining.
- Include Mermaid diagrams for:
  - class diagrams / domain model
  - component diagrams
  - execution/workflow diagrams

### 4. Mermaid Diagram Requirements

- Use `mermaid` fenced code blocks in Markdown.
- Generate at least one UML-style diagram for domain relationships.
- Generate at least one execution or flow diagram for runtime behavior.
- Keep diagrams aligned to the code structure and system boundaries.

### 5. Best Practices for Code Documentation

- Document the purpose of each major package or module.
- Describe how domain entities, services, and infrastructure interact.
- Keep architecture documentation at a high level, with links to source files when useful.
- Keep generated documentation in source control.

## Example project layout

```text
project-root/
  README.md
  environment.yml
  skills/
    documentation_commit_push_skill.md
    python_best_practices_skill.md
  scripts/
    generate_documentation_commit_push.py
  wiki/
    architecture.md
  tests/
    test_python_best_practices.py
```

## Recommended execution

- Run `python scripts/generate_documentation_commit_push.py --commit-message "Update docs and push" --push` before pushing changes.
- In CI, run the same script to refresh docs and verify the generated content.
- If using Git hooks, install the script as a pre-push helper.

## Notes

- The documentation should reflect the actual code base and recent changes.
- Keep architecture documentation updated with every major refactor.
- Use the README summary as the quick entry point for contributors.
