"""Application workflows and use cases."""

from src.domain.prediction import PredictionRequest, PredictionService
from src.infrastructure.model_loader import ModelLoader


def main() -> None:
    """Main application workflow entry point."""
    loader = ModelLoader("./models/latest.pkl")
    service = PredictionService(loader)
    request = PredictionRequest(features=[1.0, 2.0, 3.0])
    score = service.predict(request)
    print(f"Prediction score: {score}")


if __name__ == "__main__":
    main()
