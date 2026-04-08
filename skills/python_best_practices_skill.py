"""Python Best Practices Skill example.

This module demonstrates a simple Domain-Driven Design structure and comments
on how to apply PEP 8, MLOps, and Conda-based environment control.
"""

from dataclasses import dataclass
from typing import List


# Domain entity definition
@dataclass
class PredictionRequest:
    features: List[float]


# Domain service example
class PredictionService:
    """Domain service for model predictions."""

    def __init__(self, model_loader):
        self._model_loader = model_loader

    def predict(self, request: PredictionRequest) -> float:
        """Return the prediction score for a request."""
        model = self._model_loader.load_model()
        return model.predict([request.features])[0]


# Infrastructure adapter example
class ModelLoader:
    """Loads and manages model artifacts in a reproducible way."""

    def __init__(self, model_path: str):
        self.model_path = model_path

    def load_model(self):
        # Replace with MLOps pipeline artifact loading and validation
        from sklearn.linear_model import LogisticRegression

        model = LogisticRegression()
        return model


def main() -> None:
    """Main application workflow entry point."""
    loader = ModelLoader("./models/latest.pkl")
    service = PredictionService(loader)
    request = PredictionRequest(features=[1.0, 2.0, 3.0])
    score = service.predict(request)
    print(f"Prediction score: {score}")


if __name__ == "__main__":
    main()
