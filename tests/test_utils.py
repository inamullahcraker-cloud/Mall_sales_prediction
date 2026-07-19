"""
Tests for utility functions.
"""

from pathlib import Path

from src.utils import create_directory


def test_create_directory(tmp_path):

    directory = tmp_path / "test"

    create_directory(directory)

    assert Path(directory).exists()