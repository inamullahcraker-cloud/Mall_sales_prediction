"""
Tests for model factory.
"""

from src.model import ModelFactory


def test_create_model():

    factory = ModelFactory()

    model = factory.create_model()

    assert model is not None