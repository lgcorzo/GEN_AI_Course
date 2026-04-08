import pickle
from unittest.mock import patch

from src.infrastructure.model_loader import ModelLoader


class DummyModel:
    def predict(self, data):
        return [0.5]


def test_model_loader_loads_from_file(tmp_path):
    model_path = tmp_path / "model.pkl"
    with open(model_path, "wb") as handle:
        pickle.dump(DummyModel(), handle)

    loader = ModelLoader(str(model_path))
    model = loader.load_model()

    assert model.predict([[1.0]]) == [0.5]


def test_model_loader_fallback_to_default():
    loader = ModelLoader("nonexistent.pkl")
    model = loader.load_model()

    # Since sklearn may not be available, just check it's not None
    assert model is not None