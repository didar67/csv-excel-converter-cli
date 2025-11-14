"""
Entry point for the CSV-to-Excel Converter tool.
Now testing config loader integration.
"""

from script.config_loader import load_config
from core.logger import initialize_logger


def main():
    logger = initialize_logger()

    try:
        config = load_config()
        logger.info("Config loaded successfully.")
    except Exception as e:
        logger.error(f"Config loading failed: {e}")


if __name__ == "__main__":
    main()
