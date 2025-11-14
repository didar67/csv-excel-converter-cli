"""
Centralized logging module for the CSV-to-Excel Converter project.

This module provides a structured, reusable logging system with:
- Rotating file handlers for error and info logs
- Console logging for developer visibility
- Singleton-style logger creation (no duplicate handlers)
- Industry-standard log formatting

This logger is used across all modules for consistent observability.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def initialize_logger():
    """
    Initialize and configure the centralized logger.

    Returns:
        logging.Logger: Configured singleton logger instance.
    """

    logger = logging.getLogger("csv_tool")

    # Prevent adding duplicate handlers when imported multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    # Log Format 
    log_format = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
    )

    # INFO Log Handler 
    info_handler = RotatingFileHandler(
        LOG_DIR / "info.log",
        maxBytes=2_000_000,      # 2MB rotation
        backupCount=3
    )
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(log_format)

    # ERROR Log Handler 
    error_handler = RotatingFileHandler(
        LOG_DIR / "error.log",
        maxBytes=2_000_000,
        backupCount=3
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(log_format)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)

    # Add handlers
    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger
