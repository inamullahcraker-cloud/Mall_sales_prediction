"""
Lag feature engineering.
"""

from __future__ import annotations

import pandas as pd

from src.config import load_config
from src.logger import get_logger

logger = get_logger(__name__)


class LagFeatures:
    """
    Generate lag features for time-series forecasting.
    """

    def __init__(self):

        config = load_config()

        self.enabled = config["lag_features"]["enabled"]

        self.lags = config["lag_features"]["lags"]

        self.target_column = config["dataset"]["target_column"]

        self.date_column = config["dataset"]["date_column"]

        self.group_columns = config["dataset"]["group_columns"]

    def generate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Generate lag features.

        Parameters
        ----------
        df : pd.DataFrame
            Input dataframe.

        Returns
        -------
        pd.DataFrame
        """

        if not self.enabled:

            logger.info(
                "Lag feature engineering disabled."
            )

            return df

        df = df.copy()

        required_columns = (
            self.group_columns
            + [
                self.date_column,
                self.target_column,
            ]
        )

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:

            raise ValueError(
                f"Missing columns: {missing_columns}"
            )

        df = df.sort_values(
            self.group_columns
            + [self.date_column]
        ).reset_index(drop=True)

        grouped = df.groupby(
            self.group_columns
        )[self.target_column]

        for lag in self.lags:

            df[f"lag_{lag}"] = grouped.shift(lag)

        logger.info(
            "Generated %d lag features.",
            len(self.lags),
        )

        return df