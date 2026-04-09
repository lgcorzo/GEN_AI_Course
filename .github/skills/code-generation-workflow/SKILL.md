---
name: code-generation-workflow
description: "Use when: implementing code features with tests and documentation. Structured workflow for producing code, tests, and documentation following PEP 8 and Domain-Driven Design."
---

# Code Generation Workflow Skill

This skill describes a structured workflow for producing code, tests, and documentation.
It is designed for feature development with high coverage requirements and a final documentation step.

## Workflow Overview

1. Generate the feature code.
2. Write unit tests to achieve at least 95% coverage overall and 95% coverage for each pull request.
3. After the feature is finished, add integration tests to validate end-to-end behavior.
4. When the pull request is ready, generate the feature documentation.

## Step 1: Generate the code

- Start with a clear feature or user story.
- Translate requirements into domain concepts, services, and modules.
- Follow PEP 8 and Domain-Driven Design structure.
- Keep the feature implementation focused on its single responsibility.
- Use Conda-managed environments for reproducibility - ensure `conda activate genai-course` before development.

## Step 2: Add unit tests for coverage

- Use `pytest` for unit testing.
- Write tests that verify the behavior of individual components and services.
- Use `unittest.mock.patch` or `pytest-mock` to mock external dependencies.
- Aim for at least `95%` coverage across the repository.
- Ensure each PR maintains `95%` coverage for the code it introduces or changes.
- Prefer small, deterministic tests that are easy to review and maintain.
- Place unit tests in `tests/unit/` mirroring the DDD structure (e.g., `tests/unit/domain/` for domain tests).

### Unit test best practices

- Test each public function or method in isolation.
- Mock external calls, database access, and network interactions.
- Validate both success and failure paths.
- Keep fixture setup simple and reusable.
- Measure coverage with a tool such as `pytest-cov`.

## Step 3: Add integration tests when the feature is finished

- Add integration tests after the core feature implementation is complete.
- Integration tests should exercise multiple modules together.
- Mock only external services and APIs; let internal systems run normally.
- Validate workflow behavior, data transformations, and component interactions.
- Keep integration tests separate from unit tests in `tests/integration/` mirroring the DDD structure (e.g., `tests/integration/application/` for workflow tests).

## Step 4: Generate feature documentation

- Document the feature in `README.md` or in a dedicated documentation page.
- Describe the feature purpose, design decisions, and how it fits the domain.
- Document the testing strategy and coverage expectations.
- Add architecture diagrams when relevant, using Mermaid for clarity.
- Update `wiki/architecture.md` if the feature changes system boundaries or workflows.

## Recommended process for pull requests

- Open the PR after the feature implementation and unit tests are in place.
- Run `flake8` and `mypy` to ensure code quality and correctness before creating the PR.
- Include a summary of changed files and test coverage results.
- Run integration tests before final review.
- Refresh documentation for the feature and verify that the README summary is up to date.
- Use the generated documentation workflow to keep the repo consistent.

## Example artifact flow

```text
feature-branch/
  settings/
    environment.yml
  src/
    domain/
    application/
    infrastructure/
  tests/
    unit/
      domain/
      infrastructure/
    integration/
      application/
  scripts/
    generate_documentation_commit_push.py
  wiki/
    architecture.md
  README.md
```

## Notes

- This workflow is aligned with MLOps lifecycle control and DDD architecture.
- Keep documentation and tests as part of the same feature cycle, not as an afterthought.
- Use automation where possible to enforce coverage and documentation generation.
