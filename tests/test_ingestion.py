from pathlib import Path
import pandas as pd

from data.ingestion import load_raw_data


def test_load_raw_data_returns_dataframe():
    df = load_raw_data(Path("data/raw/application_train.csv"))
    assert isinstance(df, pd.DataFrame)


def test_load_raw_data_not_empty():
    df = load_raw_data(Path("data/raw/application_train.csv"))
    assert not df.empty


def test_load_raw_data_has_rows_and_columns():
    df = load_raw_data(Path("data/raw/application_train.csv"))
    assert df.shape[0] > 0
    assert df.shape[1] > 0
