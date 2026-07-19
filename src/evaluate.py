"""
Model evaluation module.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score,
)

from src.config import load_config
from src.logger import get_logger
from src.services.model_service import ModelService
from src.utils import (
    load_dataframe,
    save_dataframe,
    save_json,
)

logger = get_logger(__name__)

config = load_config()


class Evaluator:
    """
    Evaluate a trained regression model.
    """

    def __init__(self):

        self.service = ModelService()

    def evaluate(self) -> dict:

        logger.info(
            "Starting evaluation..."
        )

        # -----------------------------------------
        # Load test data
        # -----------------------------------------

        X_test = load_dataframe(
            config["output"]["test_features"]
        )

        y_test = (
            load_dataframe(
                config["output"]["test_target"]
            )
            .squeeze("columns")
        )

        # -----------------------------------------
        # Prediction
        # -----------------------------------------

        predictions = self.service.predict(
            X_test
        )

        # -----------------------------------------
        # Metrics
        # -----------------------------------------

        mse = mean_squared_error(
            y_test,
            predictions,
        )

        metrics = {

            "mae": mean_absolute_error(
                y_test,
                predictions,
            ),

            "mse": mse,

            "rmse": mse ** 0.5,

            "mape": mean_absolute_percentage_error(
                y_test,
                predictions,
            ),

            "r2_score": r2_score(
                y_test,
                predictions,
            ),
        }

        logger.info(metrics)

        # -----------------------------------------
        # Save metrics
        # -----------------------------------------

        save_json(
            metrics,
            config["output"]["metrics_path"],
        )

        # -----------------------------------------
        # Save predictions
        # -----------------------------------------

        prediction_df = pd.DataFrame(
            {
                "Actual": y_test,
                "Prediction": predictions,
                "Residual": y_test - predictions,
            }
        )

        save_dataframe(
            prediction_df,
            config["output"]["prediction_path"],
        )

        # -----------------------------------------
        # Actual vs Prediction Plot
        # -----------------------------------------

        figures_dir = Path(
            config["output"]["figure_dir"]
        )

        figures_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.figure(figsize=(8, 6))

        plt.scatter(
            y_test,
            predictions,
            alpha=0.7,
        )

        plt.plot(

            [

                y_test.min(),
                y_test.max(),

            ],

            [

                y_test.min(),
                y_test.max(),

            ],

            color="red",

            linestyle="--",

        )

        plt.xlabel(
            "Actual"
        )

        plt.ylabel(
            "Predicted"
        )

        plt.title(
            "Actual vs Predicted"
        )

        plt.tight_layout()

        plt.savefig(

            figures_dir /

            "actual_vs_prediction.png",

            dpi=300,

        )

        plt.close()

        logger.info(
            "Evaluation completed."
        )

        return metrics


if __name__ == "__main__":

    evaluator = Evaluator()

    evaluator.evaluate()