"""
Entry point for the CSV-to-Excel Converter tool.

This file currently initializes the centralized logger to verify
the logging system. Future versions will connect CLI, config,
and conversion logic.
"""

from core.logger import initialize_logger


def main():
    """Main orchestration function."""
    logger = initialize_logger()
    logger.info("Logging system initialized successfully.")
    logger.error("Error log test message.")


if __name__ == "__main__":
    main()
