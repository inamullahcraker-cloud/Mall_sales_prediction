"""
Training tests.
"""

from src.train import Trainer


def test_trainer_creation():

    trainer = Trainer()

    assert trainer is not None