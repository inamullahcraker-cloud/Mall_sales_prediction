"""
Feature engineering pipeline.
"""

from src.features.datefeature import DateFeatures
from src.features.lagfeature import LagFeatures
from src.features.rollingfeature import RollingMeanFeatures
from src.features.rollingstdfeature import RollingStdFeatures
from src.features.cyclicfeature import CyclicFeatures

from src.logger import get_logger

logger = get_logger(__name__)


class FeatureEngineer:
    """
    Apply all feature engineering steps.
    """

    def __init__(self):

        self.date_features = DateFeatures()

        self.lag_features = LagFeatures()

        self.rolling_mean_features = RollingMeanFeatures()

        self.rolling_std_features = RollingStdFeatures()

        self.cyclic_features = CyclicFeatures()

    def generate(self, df):

        logger.info(
            "Starting feature engineering..."
        )

        df = self.date_features.generate(df)

        df = self.lag_features.generate(df)

        df = self.rolling_mean_features.generate(df)

        df = self.rolling_std_features.generate(df)

        df = self.cyclic_features.generate(df)

        logger.info(
            "Feature engineering completed."
        )

        return df