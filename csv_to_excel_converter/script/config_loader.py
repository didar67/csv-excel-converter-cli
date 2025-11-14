"""
Configuration loader module for the CSV-to-Excel Converter tool.

This module loads YAML-based configuration into a validated Python
dictionary. It ensures reliable configuration parsing with structured
exception handling and optional Pydantic validation.

Responsibilities:
- Read config.yaml
- Parse YAML safely
- Validate fields using Pydantic (optional but recommended)
- Provide a reusable load_config() function for other modules
"""

from pathlib import Path
from typing import Any, Dict

import yaml

# Optional Pydantic validation
try:
    from pydantic import BaseModel, ValidationError

    USE_PYDANTIC = True

    class ConfigModel(BaseModel):
        """Pydantic schema for configuration validation."""
        paths: Dict[str, str]
        settings: Dict[str, Any]

except ImportError:
    # Fallback when Pydantic is not installed
    USE_PYDANTIC = False
    ValidationError = ValueError


# Absolute path reference to config.yaml
CONFIG_PATH = Path(__file__).parent.parent / "config" / "config.yaml"


def load_config() -> Dict[str, Any]:
    """
    Load and optionally validate the YAML configuration file.

    Returns:
        dict: A dictionary containing the parsed configuration.

    Raises:
        FileNotFoundError: If the configuration file is missing.
        yaml.YAMLError: If YAML parsing fails.
        ValueError: If optional Pydantic validation fails.
    """
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Configuration file not found: {CONFIG_PATH}")

    # Load YAML safely
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            raw_config = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        raise yaml.YAMLError(f"Invalid YAML structure: {exc}") from exc

    # Optional Pydantic validation
    if USE_PYDANTIC:
        try:
            validated = ConfigModel(**raw_config)
            return validated.model_dump()
        except ValidationError as exc:
            raise ValueError(f"Config validation failed: {exc}") from exc

    return raw_config
