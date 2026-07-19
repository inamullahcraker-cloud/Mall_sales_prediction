from sklearn.base import BaseEstimator, TransformerMixin


class WeekendFeature(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = X.copy()

        X["is_weekend"] = (
            X["dayofweek"] >= 5
        ).astype(int)

        return X