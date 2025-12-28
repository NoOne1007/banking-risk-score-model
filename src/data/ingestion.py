from pathlib import Path
import pandas as pd


def load_raw_data(file_path: Path) -> pd.DataFrame:
    """
    Load raw credit risk data from a CSV file.

    Parameters
    ----------
    file_path : Path
        Path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    pd.errors.EmptyDataError
        If the file is empty.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Raw data file not found at: {file_path}")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Loaded dataset is empty")

    return df
