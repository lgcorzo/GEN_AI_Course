# Python Best Practices Skill

This skill defines the best practices for developing Python code aligned with the following standards:

- **PEP 8** for code formatting, naming, and style.
- **Domain-Driven Design (DDD)** for code structure and organization.
- **MLOps** for the model development lifecycle, deployment, monitoring, and continuous improvement.
- **Conda** as the environment management system for reproducible Python environments.

## Purpose

Provide a consistent foundation for Python development by combining modern style, architecture, and lifecycle control.

## Standards

### 1. PEP 8: formatting and Python style

- Use 4-space indentation.
- Limit lines to 79 characters in code and 72 characters in comments/docstrings.
- Use `snake_case` for functions and variables, `PascalCase` for classes, and `UPPER_SNAKE_CASE` for constants.
- Keep imports ordered and grouped:
  1. standard library
  2. third-party libraries
  3. local application imports
- Add meaningful docstrings for modules, classes, and public methods.
- Use blank lines to separate top-level functions and classes, and logical sections inside functions.

### 2. Domain-Driven Design (DDD)

- Organize code by domain concepts, not by technical layers alone.
- Define clear boundaries for the domain model, application services, and infrastructure.
- Keep business logic inside domain classes and services.
- Use descriptive domain names and avoid technical or generic names.
- Use `application/`, `domain/`, and `infrastructure/` folders for a DDD-aligned structure.

### 3. MLOps: lifecycle and operational control

- Track experiments, models, and metrics consistently.
- Use version control for code, model artifacts, and environment definitions.
- Automate testing, validation, and deployment pipelines.
- Monitor model performance in production and implement retraining triggers.
- Document deployment requirements, data sources, and model assumptions.
- Use `pytest` for unit, integration, and post-release testing.
- Mock external dependencies in unit tests using `unittest.mock.patch` or `pytest-mock`.
- Integration tests should mock only external services and APIs while exercising internal module workflows.
- Post-release tests should execute complete code paths and validate the application in a production-like environment.
- Keep tests isolated, deterministic, and focused on single behaviors where appropriate.

### 4. Conda for environment control

- Define project dependencies in a `conda` environment YAML file.
- Keep environments reproducible by pinning Python and package versions when needed.
- Use `conda env create -f environment.yml` to create the environment.
- Use `conda activate <env-name>` before running or testing code.

## Recommended project structure

```text
project-root/
  README.md
  environment.yml
  src/
    domain/
      entities.py
      services.py
    application/
      workflows.py
    infrastructure/
      persistence.py
      mlops.py
  tests/
    unit/
      test_domain.py
      test_infrastructure.py
    integration/
      test_application.py
  scripts/
    generate_documentation_commit_push.py
  wiki/
    architecture.md
```

## Example Conda environment file

```yaml
name: genai-course
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.12
  - pip
  - numpy
  - pandas
  - scikit-learn
  - pyyaml
  - pytest
  - pylint
  - black
```

## Practical guidance

- Start each feature with a domain concept and map technical requirements to domain terms.
- Keep utility and infrastructure code separate from core domain logic.
- Apply static analysis and formatting tools such as `pylint` and `black` regularly.
- Use `conda` to manage environments and share `environment.yml` with the team.
- Review code for PEP 8 compliance, readability, and DDD consistency during development.
- Write tests with `pytest` and mock external calls using `@patch` decorators to keep unit tests isolated.

## Summary

This skill is aligned to:
- PEP 8 for formatting and style.
- DDD for structure and domain-focused code design.
- MLOps for lifecycle control and production readiness.
- Conda for environment management and reproducibility.
