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
  settings/
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
      domain/
        test_entities.py
        test_services.py
      infrastructure/
        test_persistence.py
        test_mlops.py
    integration/
      application/
        test_workflows.py
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

## Test Folder Structure

The test folder combines test types (unit/integration) with DDD boundaries to provide clear organization:

- `tests/unit/domain/`: Unit tests for domain entities and services, focusing on isolated business logic.
- `tests/unit/infrastructure/`: Unit tests for infrastructure adapters, mocking external dependencies.
- `tests/integration/application/`: Integration tests for application workflows, validating end-to-end behavior.

This hierarchical structure ensures tests are co-located with the code they test while separating unit from integration concerns. You can run tests by type using `pytest tests/unit/` for fast unit tests or `pytest tests/integration/` for end-to-end validation.

## Settings Folder

The `settings/` folder contains configuration files for the project environment:

- `settings/environment.yml`: Conda environment specification with all required dependencies and their versions. Use `conda env create -f settings/environment.yml` to set up the development environment.

## Environment Setup

This project uses Conda for environment management to ensure reproducible and isolated development environments:

1. Install Miniconda or Anaconda if not already installed
2. Create the environment: `conda env create -f settings/environment.yml`
3. Activate the environment: `conda activate genai-course`
4. The environment must be activated before running any code, tests, or development tools
5. Deactivate when done: `conda deactivate`

All dependencies are pinned to specific versions in `settings/environment.yml` to ensure consistency across different machines and deployments.

- Start each feature with a domain concept and map technical requirements to domain terms.
- Keep utility and infrastructure code separate from core domain logic.
- Apply static analysis and formatting tools such as `pylint` and `black` regularly.
- Use `conda` to manage environments and share `settings/environment.yml` with the team.
- Review code for PEP 8 compliance, readability, and DDD consistency during development.
- Write tests with `pytest` and mock external calls using `@patch` decorators to keep unit tests isolated.
- Aim for at least 95% test coverage using `pytest --cov=src`.

## Summary

This skill is aligned to:
- PEP 8 for formatting and style.
- DDD for structure and domain-focused code design.
- MLOps for lifecycle control and production readiness.
- Conda for environment management and reproducibility.
