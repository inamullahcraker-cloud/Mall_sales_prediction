"""
Tests for DataLoader.
"""

import pandas as pd

from src.data import DataLoader


def test_split_features_target(sample_dataframe):

    loader = DataLoader()

    X, y = loader.split_features_target(sample_dataframe)

    assert isinstance(X, pd.DataFrame)

    assert len(y) == len(X)

    assert "sales" not in X.columns