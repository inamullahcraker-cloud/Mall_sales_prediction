"""
Tests for preprocessing.
"""

from src.preprocessing import Preprocessor


def test_preprocessor_build():

    preprocessor = Preprocessor()

    transformer = preprocessor.build()

    assert transformer is not None