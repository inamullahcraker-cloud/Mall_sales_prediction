"""
Rolling standard deviation feature engineering.
"""

from __future__ import annotations

import pandas as pd

from src.config import load_config
from src.logger import get_logger

logger = get_logger(__name__)


class RollingStdFeatures:
    """
    Generate rolling standard deviation features.
    """

    def __init__(self):

        config = load_config()

        self.enabled = config["rolling_features"]["enabled"]

        self.windows = config["rolling_features"]["windows"]

        self.statistics = config["rolling_features"]["statistics"]

        self.target_column = config["dataset"]["target_column"]

        self.date_column = config["dataset"]["date_column"]

        self.group_columns = config["dataset"]["group_columns"]

    def generate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Generate rolling standard deviation features.

        Parameters
        ----------
        df : pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """

        if (
            not self.enabled
            or "std" not in self.statistics
        ):

            logger.info(
                "Rolling std feature engineering disabled."
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

        for window in self.windows:

            df[f"rolling_std_{window}"] = grouped.transform(
                lambda x: (
                    x.shift(1)
                     .rolling(
                         window=window,
                         min_periods=1,
                     )
                     .std()
                )
            )

        logger.info(
            "Generated %d rolling std features.",
            len(self.windows),
        )

        return df