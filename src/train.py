"""
Training module.
"""
from src.utils import save_dataframe
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from src.feature_engineering import FeatureEngineer
from src.config import load_config
from src.data import DataLoader
from src.logger import get_logger
from src.model import ModelFactory
from src.preprocessing import Preprocessor
from src.services.model_service import ModelService
from src.splitter import DataSplitter
from src.utils import (
    save_dataframe,
    save_json,
    set_seed,
)

logger = get_logger(__name__)

config = load_config()


class Trainer:
    """
    Train a time-series forecasting model.
    """

    def __init__(self):

        set_seed(config["seed"])

        self.service = ModelService()

    def train(self):

        logger.info("=" * 60)
        logger.info("Training Started")
        logger.info("=" * 60)

        # ==================================================
        # Load Dataset
        # ==================================================

        loader = DataLoader()

        df = loader.load_data()



        # ==================================================
        # Feature Engineering
        # ==================================================

        engineer = FeatureEngineer()
        df=engineer.generate(df)
        loader.validate_data(df)
        # ==================================================
        # Split Features / Target
        # ==================================================

        X, y = loader.split_features_target(df)

        # ==================================================
        # Time Series Split
        # ==================================================

        splitter = DataSplitter()

        (
            X_train,
            X_valid,
            X_test,
            y_train,
            y_valid,
            y_test,
        ) = splitter.split(X, y)

        # ==================================================
        # Save Split Datasets
        # ==================================================

        save_dataframe(
            X_train,
            config["output"]["train_features"],
        )

        save_dataframe(
            X_valid,
            config["output"]["validation_features"],
        )

        save_dataframe(
            X_test,
            config["output"]["test_features"],
        )

        save_dataframe(
            y_train.to_frame(),
            config["output"]["train_target"],
        )

        save_dataframe(
            y_valid.to_frame(),
            config["output"]["validation_target"],
        )

        save_dataframe(
            y_test.to_frame(),
            config["output"]["test_target"],
        )

        logger.info("Train / Validation / Test sets saved.")

        # ==================================================
        # Build Preprocessor
        # ==================================================

        preprocessor = Preprocessor()

        transformer = preprocessor.build()

        # ==================================================
        # Build Pipeline
        # ==================================================

        factory = ModelFactory()

        pipeline = factory.build_pipeline(
            transformer
        )

        # ==================================================
        # Train Model
        # ==================================================

        logger.info("Training model...")

        pipeline.fit(
            X_train,
            y_train,
        )

        logger.info("Model training completed.")

        # ==================================================
        # Validation
        # ==================================================

        logger.info("Evaluating validation set...")

        predictions = pipeline.predict(
            X_valid
        )

        metrics = {

            "validation_mae": float(
                mean_absolute_error(
                    y_valid,
                    predictions,
                )
            ),



            "validation_r2": float(
                r2_score(
                    y_valid,
                    predictions,
                )
            ),
        }

        logger.info(
            f"Validation MAE : {metrics['validation_mae']:.4f}"
        )

        

        logger.info(
            f"Validation R²  : {metrics['validation_r2']:.4f}"
        )

        # ==================================================
        # Save Pipeline
        # ==================================================

        self.service.save(
            pipeline
        )

        logger.info(
            "Pipeline saved successfully."
        )

        # ==================================================
        # Save Metrics
        # ==================================================

        save_json(
            metrics,
            config["output"]["metrics_path"],
        )

        logger.info(
            "Metrics saved successfully."
        )

        logger.info("=" * 60)
        logger.info("Training Finished")
        logger.info("=" * 60)

        return pipeline


if __name__ == "__main__":

    trainer = Trainer()

    trainer.train()