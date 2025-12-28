import pandas as pd


class DataValidationError(Exception):
    """Raised when raw data validation fails."""
    pass


def validate_raw_data(df: pd.DataFrame) -> None:
    if df.empty:
        raise DataValidationError("DataFrame is empty.")

    required_columns = {"SK_ID_CURR", "TARGET"}
    missing = required_columns - set(df.columns)

    if missing:
        raise DataValidationError(f"Missing required columns: {missing}")

    if df["SK_ID_CURR"].duplicated().any():
        raise DataValidationError("Duplicate SK_ID_CURR values found.")

    # soft check (log-level conceptually)
    null_ratio = df.isnull().mean().mean()
    if null_ratio > 0.4:
        print(f"[WARN] High overall missingness: {null_ratio:.2%}")
