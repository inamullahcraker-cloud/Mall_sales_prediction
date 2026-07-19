"""
Feature engineering tests.
"""

from src.feature_engineering import FeatureEngineer


def test_feature_engineering(sample_dataframe):

    engineer = FeatureEngineer()

    df = engineer.generate(sample_dataframe)

    assert "year" in df.columns

    assert "month" in df.columns

    assert "lag_1" in df.columns

    assert "rolling_mean_7" in df.columns