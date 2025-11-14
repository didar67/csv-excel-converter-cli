from pathlib import Path


def validate_file_exists(path: Path) -> None:
    """
    Ensure that a given file exists before processing.

    Args:
        path (Path): File path.

    Raises:
        FileNotFoundError: If file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
