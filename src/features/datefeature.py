"""
Date feature engineering.
"""

from __future__ import annotations

import pandas as pd

from src.config import load_config
from src.logger import get_logger

logger = get_logger(__name__)


class DateFeatures:
    """
    Generate calendar-based features.
    """

    def __init__(self):

        config = load_config()

        self.enabled = config["date_features"]["enabled"]

        self.features = config["date_features"]["extract"]

        self.date_column = config["dataset"]["date_column"]

    def generate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Generate configured calendar features.

        Parameters
        ----------
        df : pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """

        if not self.enabled:

            logger.info(
                "Date feature engineering disabled."
            )

            return df

        df = df.copy()

        if self.date_column not in df.columns:

            raise ValueError(
                f"Missing column: '{self.date_column}'."
            )

        df[self.date_column] = pd.to_datetime(
            df[self.date_column]
        )

        dt = df[self.date_column].dt

        feature_map = {

            "year": dt.year,

            "quarter": dt.quarter,

            "month": dt.month,

            "weekofyear": dt.isocalendar().week.astype(int),

            "day": dt.day,

            "dayofweek": dt.dayofweek,

            "dayofyear": dt.dayofyear,

            "is_weekend": (
                dt.dayofweek >= 5
            ).astype(int),

            "is_month_start": (
                dt.is_month_start
            ).astype(int),

            "is_month_end": (
                dt.is_month_end
            ).astype(int),

            "is_quarter_start": (
                dt.is_quarter_start
            ).astype(int),

            "is_quarter_end": (
                dt.is_quarter_end
            ).astype(int),

            "is_year_start": (
                dt.is_year_start
            ).astype(int),

            "is_year_end": (
                dt.is_year_end
            ).astype(int),

            "days_in_month": dt.days_in_month,

            "month_name": dt.month_name(),

            "day_name": dt.day_name(),

        }

        for feature in self.features:

            if feature not in feature_map:

                raise ValueError(
                    f"Unsupported date feature: {feature}"
                )

            df[feature] = feature_map[feature]

        logger.info(
            "Generated %d date features.",
            len(self.features),
        )

        return df