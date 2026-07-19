"""
Evaluation tests.
"""

from src.evaluate import Evaluator


def test_evaluator_creation():

    evaluator = Evaluator()

    assert evaluator is not None