import pytest
from unittest.mock import MagicMock, patch

from skills.python_best_practices_skill import ModelLoader, PredictionRequest, PredictionService


@patch("skills.python_best_practices_skill.ModelLoader.load_model")
def test_prediction_service_uses_model_loader(mock_load_model):
    mock_model = MagicMock()
    mock_model.predict.return_value = [0.75]
    mock_load_model.return_value = mock_model

    loader = ModelLoader("./models/latest.pkl")
    service = PredictionService(loader)
    request = PredictionRequest(features=[1.0, 2.0, 3.0])

    score = service.predict(request)

    mock_load_model.assert_called_once()
    mock_model.predict.assert_called_once_with([request.features])
    assert score == 0.75
