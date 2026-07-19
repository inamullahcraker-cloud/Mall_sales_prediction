"""
Configuration loader for the ML project.

This module loads the YAML configuration file and makes it
available throughout the project.
"""

from pathlib import Path
from functools import lru_cache

import yaml


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Default configuration file
CONFIG_PATH = PROJECT_ROOT / "configs" / "config.yaml"


@lru_cache(maxsize=1)
def load_config(config_path: Path = CONFIG_PATH) -> dict:
    """
    Load the YAML configuration file.

    Parameters
    ----------
    config_path : Path
        Path to config.yaml

    Returns
    -------
    dict
        Parsed configuration dictionary.
    """

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config