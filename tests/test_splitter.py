import pandas as pd
import pytest
from src.data.splitter import split_data


@pytest.fixture(scope="module")
def sample_df():
    return pd.read_csv("data/raw/application_train.csv").head(1000)


@pytest.fixture(scope="module")
def splits(sample_df):
    return split_data(
        df=sample_df,
        target_col="TARGET",
        train_size=0.7,
        val_size=0.15,
        test_size=0.15,
        random_state=42,
        stratify=True,
    )


def test_splitter_produces_correct_sizes(sample_df, splits):
    n = len(sample_df)

    assert len(splits["X_train"]) == len(splits["y_train"])
    assert len(splits["X_val"]) == len(splits["y_val"])
    assert len(splits["X_test"]) == len(splits["y_test"])

    # Ratio checks (±2% tolerance)
    assert abs(len(splits["X_train"]) / n - 0.7) < 0.02
    assert abs(len(splits["X_val"]) / n - 0.15) < 0.02
    assert abs(len(splits["X_test"]) / n - 0.15) < 0.02


def test_splitter_preserves_class_distribution(sample_df, splits):
    original_rate = sample_df["TARGET"].mean()

    train_rate = splits["y_train"].mean()
    val_rate = splits["y_val"].mean()
    test_rate = splits["y_test"].mean()

    tolerance = 0.01

    assert abs(train_rate - original_rate) < tolerance
    assert abs(val_rate - original_rate) < tolerance
    assert abs(test_rate - original_rate) < tolerance
