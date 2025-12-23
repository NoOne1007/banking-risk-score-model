import os
import logging
import pandas as pd
from typing import Any, Dict


logger = logging.getLogger(__name__)


class DataIngestion:
    """
    Handles loading and basic validation of raw input data.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.data_path = config["data"]["raw_path"]
        self.target_column = config["data"]["target_column"]

    def load_data(self) -> pd.DataFrame:
        """
        Loads raw data from CSV and performs basic validation.

        Returns
        -------
        pd.DataFrame
            Loaded dataset
        """
        logger.info("Starting data ingestion")
        logger.info(f"Loading data from: {self.data_path}")

        if not os.path.exists(self.data_path):
            logger.error("Data file not found")
            raise FileNotFoundError(f"Data file not found at {self.data_path}")

        df = pd.read_csv(self.data_path)
        logger.info(f"Data loaded successfully with shape: {df.shape}")

        self._validate_schema(df)

        return df

    def _validate_schema(self, df: pd.DataFrame) -> None:
        """
        Validates expected schema elements.
        """
        if self.target_column not in df.columns:
            logger.error("Target column missing from dataset")
            raise ValueError(
                f"Target column '{self.target_column}' not found in data"
            )

        logger.info("Schema validation passed")
