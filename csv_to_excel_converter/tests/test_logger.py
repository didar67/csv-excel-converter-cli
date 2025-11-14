"""
Unit tests for the centralized logging system.

These tests ensure:
- Logger initializes correctly
- Log directory and files are created
- Handlers are not duplicated on repeated initialization
"""

from pathlib import Path
from core.logger import initialize_logger

def test_logger_initialization_creates_log_files(tmp_path, monkeypatch):
    """Ensure logger initializes without duplicate handlers."""
    # Redirect log directory to temp path
    monkeypatch.chdir(tmp_path)

    logger = initialize_logger()
    logger.info("Test info message")
    logger.error("Test error message")

    # Assert log files exist
    assert Path("logs/info.log").exists()
    assert Path("logs/error.log").exists()

def test_logger_handlers_not_duplicated():
    """Logger should not duplicate handlers on multiple calls."""
    logger1 = initialize_logger()
    handler_count_before = len(logger1.handlers)

    logger2 = initialize_logger()
    handler_count_after = len(logger2.handlers)

    assert handler_count_before == handler_count_after
