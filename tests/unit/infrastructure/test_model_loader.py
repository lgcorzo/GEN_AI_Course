import pickle
import pytest

from src.infrastructure.model_loader import ModelLoader


class DummyModel:
    def predict(self, data):
        return [0.5]


@pytest.mark.unit
def test_model_loader_loads_from_file(tmp_path):
    model_path = tmp_path / "model.pkl"
    with open(model_path, "wb") as handle:
        pickle.dump(DummyModel(), handle)

    loader = ModelLoader(str(model_path))
    model = loader.load_model()

    assert model.predict([[1.0]]) == [0.5]


@pytest.mark.unit
def test_model_loader_fallback_to_default():
    loader = ModelLoader("nonexistent.pkl")
    model = loader.load_model()

    # Test that the dummy model works
    result = model.predict([[1.0, 2.0]])
    assert result == [0.5]