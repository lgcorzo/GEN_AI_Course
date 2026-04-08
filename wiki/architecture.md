# Architecture Documentation

This document describes the repository architecture using DDD and MLOps principles.
It includes Mermaid diagrams for the domain model and execution flow.

## Domain-Driven Design Structure

- `domain/`: core business entities, value objects, and domain services.
- `application/`: use cases, workflows, and orchestration services.
- `infrastructure/`: persistence, model loading, external integrations, and deployment adapters.

## MLOps Architecture

- Model artifacts and environment definitions are versioned.
- CI/CD pipelines validate tests, build packages, and deploy models.
- Monitoring and retraining guidelines are part of the operational process.

## Domain Model

```mermaid
classDiagram
    class PredictionRequest {
        +List<float> features
    }

    class PredictionService {
        +predict(request: PredictionRequest) float
    }

    class ModelLoader {
        +load_model() Model
    }

    PredictionService --> ModelLoader
    PredictionRequest --> PredictionService
```

## Execution Workflow

```mermaid
flowchart LR
    A[User request] --> B[Request validation]
    B --> C[Domain service invocation]
    C --> D[Model loader adapter]
    D --> E[ML model artifact]
    E --> F[Prediction result]
    F --> G[Response payload]
```

## MLOps Lifecycle Diagram

```mermaid
flowchart TB
    A[Code change] --> B[Generate docs & tests]
    B --> C[Run unit/integration tests]
    C --> D[Build artifacts]
    D --> E[Deploy model/service]
    E --> F[Monitor performance]
    F --> G[Trigger retraining]
    G --> B
```

## Notes

- Use this page to document architecture changes after each push.
- Keep the Mermaid diagrams aligned with the actual repository structure.
- Update the execution workflow when new data paths or services are added.
