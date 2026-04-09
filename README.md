# GEN_AI_Course

A comprehensive Python project demonstrating Domain-Driven Design (DDD), MLOps best practices, and modern development workflows.

## 🚀 Quick Start

This project uses GitHub Codespaces with pre-configured conda environment:

1. **Open in Codespace**: Click the "Code" button → "Create codespace on main"
2. **Environment**: Automatically configured with `genai-course` conda environment
3. **Development**: Start coding immediately - all dependencies are installed

### Manual Setup (if not using Codespaces)

```bash
# Install Miniconda/Anaconda
# Create environment
conda env create -f settings/environment.yml
# Activate environment
conda activate genai-course
```

## 🏗️ Project Structure

- `src/`: Source code organized by DDD layers
  - `domain/`: Business logic and entities
  - `application/`: Use cases and workflows
  - `infrastructure/`: External integrations and adapters
- `tests/`: Hierarchical test structure
  - `unit/`: Unit tests by DDD layer
  - `integration/`: End-to-end workflow tests
- `settings/`: Environment configuration
- `skills/`: Development best practices documentation
- `scripts/`: Automation utilities

## Running Tests

- Run all tests: `pytest tests/`
- Run unit tests only: `pytest tests/unit/`
- Run integration tests only: `pytest tests/integration/`
- Run tests for a specific layer: `pytest tests/unit/domain/`

## Environment Setup

This project requires a Conda environment for proper dependency management:

1. Install Miniconda or Anaconda
2. Create environment: `conda env create -f settings/environment.yml`
3. Activate environment: `conda activate genai-course`
4. Run code/tests with environment activated
5. Deactivate when done: `conda deactivate`

All dependencies are version-pinned for reproducibility.

**Environment Status**: ✅ Created and tested - all tests pass with Python 3.12.1

<!-- DOC_SUMMARY_START -->
## Documentation Summary

- Generated: 2026-04-09 10:08:16 UTC
- Commit message: Update documentation for linting improvements
- Updated files:
- No tracked changes detected.

This section is generated automatically by `scripts/generate_documentation_commit_push.py`.
<!-- DOC_SUMMARY_END -->
