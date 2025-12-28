from pathlib import Path

# This file's location:
# src/utils/paths.py
# parents[2] → project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

# Model artifacts
MODELS_DIR = PROJECT_ROOT / "models"

# MLflow tracking
MLRUNS_DIR = PROJECT_ROOT / "mlruns"
