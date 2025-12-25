from pathlib import Path
import yaml
from types import SimpleNamespace


class ConfigError(Exception):
    """Raised when configuration is invalid."""
    pass


class ConfigLoader:
    REQUIRED_SECTIONS = [
        "project",
        "data",
        "features",
        "model",
        "training",
        "mlflow"
    ]

    @staticmethod
    def load(config_path: str | Path = None):
        if config_path is None:
            config_path = Path(__file__).parent / "config.yaml"
        else:
            config_path = Path(config_path)

        if not config_path.exists():
            raise ConfigError(f"Config file not found at {config_path}")

        with open(config_path, "r") as f:
            raw_config = yaml.safe_load(f)

        missing = [
            section for section in ConfigLoader.REQUIRED_SECTIONS
            if section not in raw_config
        ]

        if missing:
            raise ConfigError(f"Missing required config sections: {missing}")

        def to_namespace(d):
            if isinstance(d, dict):
                return SimpleNamespace(**{k: to_namespace(v) for k, v in d.items()})
            return d

        return to_namespace(raw_config)
