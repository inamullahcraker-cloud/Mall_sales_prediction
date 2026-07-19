"""
Utility functions for the ML project.
"""
from __future__ import annotations
from src import config

import json
import random
import time
from pathlib import Path

import joblib
import numpy as np
import pandas as pd


def set_seed(seed: int) -> None:
    """
    Set random seed for reproducibility.

    Parameters
    ----------
    seed : int
        Random seed.
    """
    random.seed(seed)
    np.random.seed(seed)


def create_directory(path: str | Path) -> Path:
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    path : str | Path

    Returns
    -------
    Path
    """
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def save_model(model, filepath: str | Path) -> None:
    """
    Save a trained model using joblib.
    """
    filepath = Path(filepath)
    create_directory(filepath.parent)
    joblib.dump(model, filepath)


def load_model(filepath: str | Path):
    """
    Load a saved model.
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"Model not found: {filepath}")

    return joblib.load(filepath)


def save_json(data: dict, filepath: str | Path) -> None:
    """
    Save a dictionary as JSON.
    """
    filepath = Path(filepath)
    create_directory(filepath.parent)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(filepath: str | Path) -> dict:
    """
    Load JSON data.
    """
    filepath = Path(filepath)

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def save_dataframe(df: pd.DataFrame, filepath: str | Path) -> None:
    """
    Save a DataFrame as a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to save.
    filepath : str | Path
        Output CSV path.
    """
    
    filepath = Path(filepath)
    create_directory(filepath.parent)
    df.to_csv(filepath, index=False)


def load_dataframe(filepath: str | Path) -> pd.DataFrame:
    """
    Load a DataFrame from a CSV file.

    Parameters
    ----------
    filepath : str | Path
        CSV file path.

    Returns
    -------
    pd.DataFrame
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"CSV file not found: {filepath}")

    return pd.read_csv(filepath)


class Timer:
    """
    Simple execution timer.

    Example
    -------
    timer = Timer()
    timer.start()
    ...
    elapsed_time = timer.stop()
    """

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self) -> float:
        if self.start_time is None:
            raise RuntimeError("Timer has not been started.")

        elapsed = time.perf_counter() - self.start_time
        self.start_time = None  # Reset timer state after stopping
        return elapsed