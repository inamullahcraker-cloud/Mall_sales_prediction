"""
Central model service.

Responsible for loading, saving and serving the trained pipeline.
"""

from pathlib import Path

import pandas as pd

from src.config import load_config
from src.logger import get_logger
from src.utils import load_model, save_model

logger = get_logger(__name__)


class ModelService:
    """
    Service responsible for loading, saving and using
    the trained machine learning pipeline.
    """

    def __init__(self):

        self.config = load_config()

        self.model_path = Path(
            self.config["output"]["model_path"]
        )

        self.pipeline = None

    # ==================================================
    # Load Model
    # ==================================================

    def load(self):

        """
        Load the trained pipeline only once.
        """

        if self.pipeline is None:

            logger.info(
                f"Loading pipeline from {self.model_path}"
            )

            self.pipeline = load_model(
                self.model_path
            )

        return self.pipeline

    # ==================================================
    # Save Model
    # ==================================================

    def save(
        self,
        pipeline,
    ):

        save_model(
            pipeline,
            self.model_path,
        )

        self.pipeline = pipeline

        logger.info(
            f"Pipeline saved to {self.model_path}"
        )

    # ==================================================
    # Predict
    # ==================================================

    def predict(
        self,
        X: pd.DataFrame,
    ):

        pipeline = self.load()

        logger.info(
            f"Predicting {len(X)} samples."
        )

        return pipeline.predict(X)

    # ==================================================
    # Predict Probabilities
    # ==================================================

    def predict_proba(
        self,
        X: pd.DataFrame,
    ):

        pipeline = self.load()

        if not hasattr(
            pipeline,
            "predict_proba",
        ):

            raise AttributeError(
                "Current model does not support predict_proba()."
            )

        logger.info(
            f"Predicting probabilities for {len(X)} samples."
        )

        return pipeline.predict_proba(X)

    # ==================================================
    # Forecast
    # ==================================================

    def forecast(
        self,
        future_df: pd.DataFrame,
    ):

        """
        Forecast future values.

        Alias for predict().
        """

        return self.predict(
            future_df
        )

    # ==================================================
    # Pipeline
    # ==================================================

    def get_pipeline(self):

        return self.load()

    # ==================================================
    # Metadata
    # ==================================================

    @property
    def is_loaded(self):

        return self.pipeline is not None