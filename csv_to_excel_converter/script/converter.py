"""
Converter module for CSV <-> Excel transformations.

This module provides the core business logic for converting files
between CSV and Excel formats using pandas. It supports dry-run mode,
structured logging, and integrates helper utilities for file validation.
"""

from pathlib import Path
from typing import Optional

import pandas as pd

from core.logger import initialize_logger
from utils.helper import validate_file_exists

logger = initialize_logger()

def csv_to_excel(
    csv_path: str,
    output_path: Optional[str] = None,
    dry_run: bool = False
) -> None:
    """
    Convert a CSV file to an Excel (.xlsx) file.

    Args:
        csv_path (str): Input CSV file path.
        output_path (str, optional): Output Excel file path.
        dry_run (bool): Only simulate operation without writing output.

    Raises:
        FileNotFoundError: If source file does not exist.
        ValueError: For read/write errors.
    """
    source = Path(csv_path)
    validate_file_exists(source)

    # Auto-generate output name if not provided
    target = Path(output_path) if output_path else source.with_suffix(".xlsx")

    logger.info(f"CSV → Excel conversion initiated: {source} → {target}")

    if dry_run:
        logger.info("Dry-run mode enabled — no file will be written.")
        return

    try:
        df = pd.read_csv(source)
        df.to_excel(target, index=False)
        logger.info(f"Conversion successful. Output written → {target}")
    except Exception as exc:
        logger.error(f"CSV → Excel conversion failed: {exc}")
        raise ValueError(f"Failed to convert CSV to Excel: {exc}") from exc


def excel_to_csv(
    excel_path: str,
    output_path: Optional[str] = None,
    dry_run: bool = False
) -> None:
    """
    Convert an Excel (.xlsx) file to CSV format.

    Args:
        excel_path (str): Input Excel file path.
        output_path (str, optional): Output CSV file path.
        dry_run (bool): Only simulate operation without writing output.

    Raises:
        FileNotFoundError: If source file does not exist.
        ValueError: For read/write errors.
    """
    source = Path(excel_path)
    validate_file_exists(source)

    # Auto-generate output name if not provided
    target = Path(output_path) if output_path else source.with_suffix(".csv")

    logger.info(f"Excel → CSV conversion initiated: {source} → {target}")

    if dry_run:
        logger.info("Dry-run mode enabled — no file will be written.")
        return

    try:
        df = pd.read_excel(source)
        df.to_csv(target, index=False)
        logger.info(f"Conversion successful. Output written → {target}")
    except Exception as exc:
        logger.error(f"Excel → CSV conversion failed: {exc}")
        raise ValueError(f"Failed to convert Excel to CSV: {exc}") from exc
