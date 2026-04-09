import pickle
import pytest

from src.application.main import main
from src.infrastructure.model_loader import ModelLoader


class DummyModel:
    def predict(self, data):
        return [sum(sample) * 0.1 for sample in data]


@pytest.mark.integration
def test_main_integration_with_model_artifact(tmp_path, capsys):
    model_path = tmp_path / "model.pkl"
    with open(model_path, "wb") as handle:
        pickle.dump(DummyModel(), handle)

    # Mock the ModelLoader path
    import src.application.main
    src.application.main.ModelLoader = (
        lambda path: ModelLoader(str(model_path))
    )

    main()

    captured = capsys.readouterr()
    assert "Prediction score: 0.6000000000000001" in captured.out
