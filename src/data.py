"""
Data loading module.

Responsible for

- Loading dataset
- Validating dataset
- Sorting dataset
- Dataset summary
- Feature/Target split
"""

from pathlib import Path

import pandas as pd

from src.config import load_config
from src.logger import get_logger

logger = get_logger(__name__)


class DataLoader:
    """
    Generic dataset loader.
    """

    def __init__(self):

        self.config = load_config()

        # ----------------------------------------
        # Dataset
        # ----------------------------------------

        dataset = self.config["dataset"]

        self.data_path = Path(
            dataset["raw_data_path"]
        )

        self.target_column = (
            dataset["target_column"]
        )

        self.date_column = (
            dataset.get(
                "date_column",
                None,
            )
        )

        self.group_columns = (
            dataset.get(
                "group_columns",
                [],
            )
        )

        # ----------------------------------------
        # Features
        # ----------------------------------------

        self.numeric_features = (
            self.config["features"]["numerical"]
        )

        self.categorical_features = (
            self.config["features"]["categorical"]
        )

    # ============================================================
    # Load Dataset
    # ============================================================

    def load_data(self) -> pd.DataFrame:

        logger.info(
            "Loading dataset..."
        )

        if not self.data_path.exists():

            raise FileNotFoundError(
                f"Dataset not found: {self.data_path}"
            )

        df = pd.read_csv(
            self.data_path
        )

        if self.date_column:

            df[self.date_column] = pd.to_datetime(
                df[self.date_column]
            )

        logger.info(
            f"Dataset loaded successfully."
        )

        logger.info(
            f"Shape: {df.shape}"
        )

        return df

    # ============================================================
    # Validate Dataset
    # ============================================================

    def validate_data(
        self,
        df: pd.DataFrame,
    ):

        required_columns = []

        if self.date_column:

            required_columns.append(
                self.date_column
            )

        required_columns.extend(
            self.group_columns
        )

        required_columns.extend(
            self.numeric_features
        )

        required_columns.extend(
            self.categorical_features
        )

        required_columns.append(
            self.target_column
        )

        missing = [

            column

            for column in required_columns

            if column not in df.columns

        ]

        if missing:

            raise ValueError(

                f"Missing columns: {missing}"

            )

        logger.info(
            "Dataset validation successful."
        )

    # ============================================================
    # Sort Dataset
    # ============================================================

    def sort_data(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        if self.date_column is None:

            return df

        columns = []

        columns.extend(
            self.group_columns
        )

        columns.append(
            self.date_column
        )

        df = (

            df

            .sort_values(columns)

            .reset_index(drop=True)

        )

        logger.info(

            f"Dataset sorted by {columns}"

        )

        return df

    # ============================================================
    # Dataset Summary
    # ============================================================

    def summary(
        self,
        df: pd.DataFrame,
    ):

        logger.info(
            "=" * 60
        )

        logger.info(
            "DATASET SUMMARY"
        )

        logger.info(
            "=" * 60
        )

        logger.info(
            f"Rows      : {len(df)}"
        )

        logger.info(
            f"Columns   : {len(df.columns)}"
        )

        logger.info(
            f"Memory    : "
            f"{df.memory_usage(deep=True).sum()/1024**2:.2f} MB"
        )

        logger.info(
            "Column Types:"
        )

        logger.info(
            f"\n{df.dtypes}"
        )

        logger.info(
            "Missing Values:"
        )

        logger.info(
            f"\n{df.isna().sum()}"
        )

        logger.info(
            "=" * 60
        )

    # ============================================================
    # Split Features / Target
    # ============================================================

    def split_features_target(
        self,
        df: pd.DataFrame,
    ):

        X = df.drop(
            columns=self.target_column
        )

        y = df[
            self.target_column
        ]

        logger.info(
            f"Features Shape : {X.shape}"
        )

        logger.info(
            f"Target Shape   : {y.shape}"
        )

        return (
            X,
            y,
        )

    # ============================================================
    # Complete Pipeline
    # ============================================================

    def run(self):

        df = self.load_data()

        self.validate_data(df)

        df = self.sort_data(df)

        self.summary(df)

        X, y = self.split_features_target(df)

        return (
            X,
            y,
            df,
        )