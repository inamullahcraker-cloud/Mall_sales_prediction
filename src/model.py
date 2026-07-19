"""
Model factory module.

Creates regression models and combines them
with the preprocessing pipeline.
"""

from sklearn.pipeline import Pipeline

from sklearn.ensemble import (
    RandomForestRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
)

from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet,
)

from sklearn.tree import DecisionTreeRegressor

from sklearn.svm import SVR

from sklearn.neighbors import KNeighborsRegressor

from xgboost import XGBRegressor

from src.config import load_config
from src.logger import get_logger

logger = get_logger(__name__)

config = load_config()


class ModelFactory:
    """
    Factory class responsible for creating regression models.
    """

    def __init__(self):

        self.model_name = config["model"]["type"]

        self.params = config["model"]["parameters"]

    # ==================================================
    # Create Model
    # ==================================================

    def create_model(self):
        """
        Create a regression model.
        """

        logger.info(
            f"Creating model: {self.model_name}"
        )

        models = {

            "LinearRegression":
                LinearRegression,

            "Ridge":
                Ridge,

            "Lasso":
                Lasso,

            "ElasticNet":
                ElasticNet,

            "DecisionTreeRegressor":
                DecisionTreeRegressor,

            "RandomForestRegressor":
                RandomForestRegressor,

            "ExtraTreesRegressor":
                ExtraTreesRegressor,

            "GradientBoostingRegressor":
                GradientBoostingRegressor,

            "SVR":
                SVR,

            "KNeighborsRegressor":
                KNeighborsRegressor,

            "XGBRegressor":
                XGBRegressor,

        }

        if self.model_name not in models:

            raise ValueError(
                f"Unsupported model: {self.model_name}"
            )

        return models[self.model_name](
            **self.params
        )

    # ==================================================
    # Build Pipeline
    # ==================================================

    def build_pipeline(
        self,
        preprocessor,
    ):
        """
        Build complete sklearn pipeline.

        Parameters
        ----------
        preprocessor :
            ColumnTransformer

        Returns
        -------
        sklearn.pipeline.Pipeline
        """

        model = self.create_model()

        pipeline = Pipeline(

            steps=[

                (
                    "preprocessor",
                    preprocessor,
                ),

                (
                    "regressor",
                    model,
                ),
            ]
        )

        logger.info(
            "Training pipeline created."
        )

        return pipeline