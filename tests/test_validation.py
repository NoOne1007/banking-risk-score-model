from pathlib import Path
from data.ingestion import load_raw_data
from data.validation import validate_raw_data, DataValidationError


def test_validation_passes_on_valid_data():
    df = load_raw_data(Path("data/raw/application_train.csv"))
    validate_raw_data(df)


def test_validation_fails_on_empty_df():
    import pandas as pd
    df = pd.DataFrame()

    try:
        validate_raw_data(df)
        assert False, "Expected DataValidationError"
    except DataValidationError:
        assert True
