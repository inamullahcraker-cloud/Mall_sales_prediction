"""
Data preprocessing module.
"""

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from src.config import load_config
from src.logger import get_logger

logger = get_logger(__name__)

config = load_config()


class Preprocessor:
    """
    Create preprocessing pipelines.

    Responsibilities
    ----------------
    - Handle missing values
    - Encode categorical features

    Feature engineering (Date, Lag, Rolling)
    is handled before this preprocessor.
    """

    def __init__(self):

        self.numeric_features = (
            config["features"]["numerical"]
        )

        self.categorical_features = (
            config["features"]["categorical"]
        )

    # ==================================================
    # Numeric Pipeline
    # ==================================================

    def numeric_pipeline(self):
        """
        Pipeline for numerical features.
        """

        return Pipeline(

            steps=[

                (
                    "imputer",
                    SimpleImputer(
                        strategy=config["preprocessing"][
                            "missing_strategy_numeric"
                        ],
                    ),
                ),

            ],
        )

    # ==================================================
    # Categorical Pipeline
    # ==================================================

    def categorical_pipeline(self):
        """
        Pipeline for categorical features.
        """

        return Pipeline(

            steps=[

                (
                    "imputer",
                    SimpleImputer(
                        strategy=config["preprocessing"][
                            "missing_strategy_categorical"
                        ],
                    ),
                ),

                (
                    "encoder",
                    OneHotEncoder(
                        handle_unknown="ignore",
                        sparse_output=False,
                    ),
                ),

            ],
        )

    # ==================================================
    # Build Preprocessor
    # ==================================================

    def build(self):
        """
        Build the complete preprocessing pipeline.

        Returns
        -------
        ColumnTransformer
        """

        logger.info(
            "Building preprocessing pipeline..."
        )

        transformer = ColumnTransformer(

            transformers=[

                (
                    "numeric",
                    self.numeric_pipeline(),
                    self.numeric_features,
                ),

                (
                    "categorical",
                    self.categorical_pipeline(),
                    self.categorical_features,
                ),

            ],

            remainder="drop",

        )

        logger.info(
            "Preprocessing pipeline created successfully."
        )

        return transformer