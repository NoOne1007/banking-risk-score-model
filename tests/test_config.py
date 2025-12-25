import pytest
from src.config.config_loader import ConfigLoader, ConfigError


def test_config_loads_successfully():
    config = ConfigLoader.load()
    assert config is not None


def test_required_config_sections_exist():
    config = ConfigLoader.load()

    assert hasattr(config, "project")
    assert hasattr(config, "data")
    assert hasattr(config, "features")
    assert hasattr(config, "model")
    assert hasattr(config, "training")
    assert hasattr(config, "mlflow")


def test_model_params_accessible():
    config = ConfigLoader.load()
    params = config.model.params

    assert hasattr(params, "C")
    assert hasattr(params, "max_iter")


def test_missing_config_file_raises_error(tmp_path):
    fake_path = tmp_path / "missing_config.yaml"

    with pytest.raises(ConfigError):
        ConfigLoader.load(fake_path)
