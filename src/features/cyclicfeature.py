"""
Cyclic feature engineering.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.config import load_config
from src.logger import get_logger

logger = get_logger(__name__)


class CyclicFeatures:
    """
    Generate cyclic encoded features.
    """

    def __init__(self):

        config = load_config()

        self.enabled = config["cyclic_features"]["enabled"]

        self.columns = config["cyclic_features"]["columns"]

    def generate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Generate cyclic encoded features.

        Parameters
        ----------
        df : pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """

        if not self.enabled:

            logger.info(
                "Cyclic feature engineering disabled."
            )

            return df

        df = df.copy()

        for column, period in self.columns.items():

            if column not in df.columns:

                raise ValueError(
                    f"'{column}' not found in dataframe."
                )

            df[f"{column}_sin"] = np.sin(
                2 * np.pi * df[column] / period
            )

            df[f"{column}_cos"] = np.cos(
                2 * np.pi * df[column] / period
            )

        logger.info(
            "Generated cyclic features for %d columns.",
            len(self.columns),
        )

        return df