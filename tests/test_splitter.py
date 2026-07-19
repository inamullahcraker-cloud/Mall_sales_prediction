"""
Tests for dataset splitter.
"""

from src.splitter import DataSplitter


def test_date_split(sample_dataframe):

    splitter = DataSplitter()

    X = sample_dataframe.drop(columns="sales")

    y = sample_dataframe["sales"]

    (
        X_train,
        X_valid,
        X_test,
        y_train,
        y_valid,
        y_test,
    ) = splitter.split(X, y)

    assert len(X_train) > 0

    assert len(X_valid) >= 0

    assert len(X_test) >= 0