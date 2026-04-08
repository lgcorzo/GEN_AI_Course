# GEN_AI_Course

## Skills

- `skills/python_best_practices_skill.md`: Defines best practices for Python development using PEP 8, Domain-Driven Design, MLOps, and Conda environment management.
- `skills/documentation_commit_push_skill.md`: Defines the process for generating documentation on commit/push, updating `README.md`, and maintaining architecture documentation in `wiki/architecture.md`.
- `skills/code_generation_workflow_skill.md`: Describes the feature development workflow from code generation to unit tests, integration tests, and final documentation.

## Documentation Automation

This repository includes automation to keep documentation aligned with code changes.

- `scripts/generate_documentation_commit_push.py`: Generates a README documentation summary and ensures `wiki/architecture.md` is present for architecture documentation.
- `wiki/architecture.md`: Contains architecture documentation, DDD boundaries, MLOps lifecycle guidance, and Mermaid diagrams for UML and execution flow.

## Source and Tests

The codebase follows Domain-Driven Design (DDD) principles with the following structure:

- `src/domain/`: Core business entities, value objects, and domain services (e.g., `PredictionRequest`, `PredictionService`).
- `src/application/`: Use cases, workflows, and orchestration services (e.g., `main.py`).
- `src/infrastructure/`: Persistence, model loading, external integrations, and deployment adapters (e.g., `ModelLoader`).
- `tests/unit/domain/`: Unit tests for domain logic.
- `tests/unit/infrastructure/`: Unit tests for adapters.
- `tests/integration/application/`: Integration tests for workflows.

- `scripts/show_ddd_structure.py`: Demonstrates the DDD folder structure.

## Running Tests

- Run all tests: `pytest tests/`
- Run unit tests only: `pytest tests/unit/`
- Run integration tests only: `pytest tests/integration/`
- Run tests for a specific layer: `pytest tests/unit/domain/`

<!-- DOC_SUMMARY_START -->
## Documentation Summary

- Generated: 2026-04-08 15:38:02 UTC
- Commit message: Refactor test structure to hierarchical unit/integration with DDD subfolders and update skills/README
- Updated files:
- `README.md`
- `skills/code_generation_workflow_skill.md`
- `skills/documentation_commit_push_skill.md`
- `skills/python_best_practices_skill.md`
- `tests/integration/__pycache__/test_main.cpython-312-pytest-9.0.1.pyc`
- `tests/integration/__pycache__/test_prediction_integration.cpython-312-pytest-9.0.1.pyc`
- `tests/integration/test_main.py`
- `tests/unit/__pycache__/test_model_loader.cpython-312-pytest-9.0.1.pyc`
- `tests/unit/__pycache__/test_prediction.cpython-312-pytest-9.0.1.pyc`
- `tests/unit/test_model_loader.py`
- `tests/unit/test_prediction.py`

This section is generated automatically by `scripts/generate_documentation_commit_push.py`.
<!-- DOC_SUMMARY_END -->
