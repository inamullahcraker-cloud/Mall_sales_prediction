"""
Tests for config.py
"""

from src.config import load_config


def test_load_config():

    config = load_config()

    assert isinstance(config, dict)

    assert "dataset" in config

    assert "model" in config

    assert "output" in config