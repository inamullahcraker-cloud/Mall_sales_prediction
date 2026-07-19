"""
History lookup module.

Generate all features required for inference from
(date, store, item).
"""

from __future__ import annotations

import pandas as pd

from src.config import load_config
from src.features.datefeature import DateFeatures
from src.logger import get_logger

logger = get_logger(__name__)


class HistoryLookup:
    """
    Build all features required for prediction.

    Input
    -----
    date
    store
    item

    Output
    ------
    DataFrame ready for the trained sklearn pipeline.
    """

    def __init__(self):

        config = load_config()

        dataset_cfg = config["dataset"]

        self.target_column = dataset_cfg["target_column"]

        self.date_column = dataset_cfg["date_column"]

        self.group_columns = dataset_cfg["group_columns"]

        self.store_column = self.group_columns[0]

        self.item_column = self.group_columns[1]

        self.lags = config["lag_features"]["lags"]

        self.windows = config["rolling_features"]["windows"]

        # Reuse existing DateFeatures class
        self.date_features = DateFeatures()

        self.history = pd.read_csv(
            dataset_cfg["raw_data_path"],
            parse_dates=[self.date_column],
        )

        logger.info("History loaded successfully.")

    def build_features(
        self,
        date,
        store,
        item,
    ) -> pd.DataFrame:
        """
        Build one feature row for prediction.
        """

        date = pd.to_datetime(date)

        history = self.history.loc[
            (self.history[self.store_column] == store)
            & (self.history[self.item_column] == item)
            & (self.history[self.date_column] < date)
        ].sort_values(self.date_column)

        row = {
            self.date_column: date,
            self.store_column: store,
            self.item_column: item,
        }

        sales = history[self.target_column]

        # =====================================
        # Lag Features
        # =====================================

        for lag in self.lags:

            row[f"lag_{lag}"] = (
                float(sales.iloc[-lag])
                if len(sales) >= lag
                else 0.0
            )

        # =====================================
        # Rolling Features
        # =====================================

        for window in self.windows:

            values = sales.tail(window)

            if values.empty:

                row[f"rolling_mean_{window}"] = 0.0
                row[f"rolling_std_{window}"] = 0.0
                row[f"rolling_max_{window}"] = 0.0

            else:

                row[f"rolling_mean_{window}"] = float(
                    values.mean()
                )

                row[f"rolling_std_{window}"] = (
                    float(values.std())
                    if len(values) > 1
                    else 0.0
                )

                row[f"rolling_max_{window}"] = float(
                    values.max()
                )

        # =====================================
        # Convert to DataFrame
        # =====================================

        X = pd.DataFrame([row])

        # =====================================
        # Generate Date Features
        # =====================================

        X = self.date_features.generate(X)

        return X