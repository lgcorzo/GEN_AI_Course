"""Infrastructure adapters for model loading."""

import os
import pickle


class ModelLoader:
    """Loads and manages model artifacts in a reproducible way."""

    def __init__(self, model_path: str):
        self.model_path = model_path

    def load_model(self):
        if self.model_path and os.path.exists(self.model_path):
            with open(self.model_path, "rb") as handle:
                return pickle.load(handle)

        # Fallback to a simple dummy model
        class DummyModel:
            def predict(self, data):
                return [0.5] * len(data)

        return DummyModel()