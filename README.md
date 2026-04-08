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
- `tests/unit/`: Unit tests for individual components (domain and infrastructure).
- `tests/integration/`: Integration tests for end-to-end workflows (application).

- `scripts/show_ddd_structure.py`: Demonstrates the DDD folder structure.

