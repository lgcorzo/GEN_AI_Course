"""Domain entities and services for prediction."""

from dataclasses import dataclass
from typing import List


@dataclass
class PredictionRequest:
    features: List[float]


class PredictionService:
    """Domain service for model predictions."""

    def __init__(self, model_loader):
        self._model_loader = model_loader

    def predict(self, request: PredictionRequest) -> float:
        """Return the prediction score for a request."""
        model = self._model_loader.load_model()
        return model.predict([request.features])[0]
