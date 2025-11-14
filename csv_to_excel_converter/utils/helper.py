"""
Helper utilities for CSV ⇄ Excel Converter.
"""

from pathlib import Path
from typing import Union

def validate_file_exists(file_path: Union[str, Path]) -> None:
    """
    Validate that a file exists at the given path.

    Args:
        file_path (str | Path): Path to the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
