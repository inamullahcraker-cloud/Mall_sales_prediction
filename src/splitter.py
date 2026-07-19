"""
Dataset splitting module.
"""

from __future__ import annotations

import pandas as pd

from sklearn.model_selection import train_test_split

from src.config import load_config
from src.logger import get_logger

logger = get_logger(__name__)


class DataSplitter:
    """
    Split dataset into train, validation and test sets.

    Supported strategies
    --------------------
    - date
    - random
    """

    def __init__(self):

        self.config = load_config()

    # =====================================================
    # Main Split
    # =====================================================

    def split(
        self,
        X,
        y,
    ):

        strategy = self.config["split"]["strategy"]

        if strategy == "date":

            return self._date_split(
                X,
                y,
            )

        if strategy == "random":

            return self._random_split(
                X,
                y,
            )

        raise ValueError(
            f"Unknown split strategy: {strategy}"
        )

    # =====================================================
    # Date Split
    # =====================================================

    def _date_split(
        self,
        X,
        y,
    ):

        cfg = self.config["split"]

        date_column = cfg["date_column"]

        train_end = pd.to_datetime(
            cfg["train_end"]
        )

        validation_end = pd.to_datetime(
            cfg["validation_end"]
        )

        df = X.copy()

        df["target"] = y

        df[date_column] = pd.to_datetime(
            df[date_column]
        )

        if cfg["sort"]:

            df = df.sort_values(
                date_column
            )

        train = df[
            df[date_column] <= train_end
        ]

        valid = df[
            (df[date_column] > train_end)
            &
            (df[date_column] <= validation_end)
        ]

        test = df[
            df[date_column] > validation_end
        ]

        X_train = train.drop(
            columns="target"
        )

        y_train = train["target"]

        X_valid = valid.drop(
            columns="target"
        )

        y_valid = valid["target"]

        X_test = test.drop(
            columns="target"
        )

        y_test = test["target"]

        self._log_split(
            X_train,
            X_valid,
            X_test,
        )

        return (
            X_train,
            X_valid,
            X_test,
            y_train,
            y_valid,
            y_test,
        )

    # =====================================================
    # Random Split
    # =====================================================

    def _random_split(
        self,
        X,
        y,
    ):

        cfg = self.config["split"]

        train_size = cfg["train_size"]

        validation_size = cfg["validation_size"]

        test_size = cfg["test_size"]

        X_train, X_temp, y_train, y_temp = train_test_split(
            X,
            y,
            train_size=train_size,
            random_state=cfg["random_state"],
            shuffle=cfg["shuffle"],
        )

        validation_ratio = (
            validation_size
            /
            (validation_size + test_size)
        )

        X_valid, X_test, y_valid, y_test = train_test_split(
            X_temp,
            y_temp,
            train_size=validation_ratio,
            random_state=cfg["random_state"],
            shuffle=cfg["shuffle"],
        )

        self._log_split(
            X_train,
            X_valid,
            X_test,
        )

        return (
            X_train,
            X_valid,
            X_test,
            y_train,
            y_valid,
            y_test,
        )

    # =====================================================
    # Logging
    # =====================================================

    def _log_split(
        self,
        X_train,
        X_valid,
        X_test,
    ):

        logger.info(
            "Dataset successfully split."
        )

        logger.info(
            f"Train: {X_train.shape}"
        )

        logger.info(
            f"Validation: {X_valid.shape}"
        )

        logger.info(
            f"Test: {X_test.shape}"
        )