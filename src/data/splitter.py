import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(
    df: pd.DataFrame,
    target_col: str,
    train_size: float,
    val_size: float,
    test_size: float,
    random_state: int,
    stratify: bool = True,
):
    if not abs(train_size + val_size + test_size - 1.0) < 1e-6:
        raise ValueError("Train, val, test sizes must sum to 1")

    X = df.drop(columns=[target_col])
    y = df[target_col]

    stratify_y = y if stratify else None

    # Train vs temp
    X_train, X_temp, y_train, y_temp = train_test_split(
        X,
        y,
        test_size=(1 - train_size),
        random_state=random_state,
        stratify=stratify_y,
    )

    # Val vs test
    val_ratio = val_size / (val_size + test_size)
    stratify_temp = y_temp if stratify else None

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp,
        y_temp,
        test_size=(1 - val_ratio),
        random_state=random_state,
        stratify=stratify_temp,
    )

    return {
        "X_train": X_train,
        "y_train": y_train,
        "X_val": X_val,
        "y_val": y_val,
        "X_test": X_test,
        "y_test": y_test,
    }
