import os
import yaml
from typing import Dict, Any


class ConfigLoader:
    """
    Loads and validates project configuration from YAML.
    """

    def __init__(self, config_path: str):
        self.config_path = config_path

    def load(self) -> Dict[str, Any]:
        """
        Loads and validates the configuration file.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(
                f"Config file not found at {self.config_path}"
            )

        with open(self.config_path, "r") as f:
            config = yaml.safe_load(f)

        self._validate_config(config)
        return config

    def _validate_config(self, config: Dict[str, Any]) -> None:
        required_sections = [
            "project",
            "data",
            "split",
            "model",
            "mlflow",
        ]

        for section in required_sections:
            if section not in config:
                raise KeyError(
                    f"Missing required config section: '{section}'"
                )
