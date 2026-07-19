"""
Shared fixtures for unit tests.
"""

import pandas as pd
import pytest


@pytest.fixture
def sample_dataframe():
    """
    Sample Walmart dataset.
    """

    return pd.DataFrame(
        {
            "date": pd.to_datetime(
                [
                    "2016-01-01",
                    "2016-01-02",
                    "2016-01-03",
                    "2016-01-04",
                    "2016-01-05",
                ]
            ),
            "store": [1, 1, 1, 1, 1],
            "item": [1, 1, 1, 1, 1],
            "sales": [20, 21, 18, 22, 19],
        }
    )