"""
Tests for model service.
"""

from src.services.model_service import ModelService


def test_model_service():

    service = ModelService()

    assert service is not None