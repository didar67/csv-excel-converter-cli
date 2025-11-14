"""
CLI handler for CSV ⇄ Excel Converter tool.
"""

import argparse
from script.converter import csv_to_excel, excel_to_csv
from script.config_loader import load_config
from core.logger import initialize_logger

logger = initialize_logger()

def parse_arguments():
    """
    Setup argparse CLI interface.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="CSV ⇄ Excel conversion CLI tool",
        epilog="Example: csv2excel input.csv output.xlsx --dry-run"
    )

    parser.add_argument(
        "mode", choices=["csv2excel", "excel2csv"], help="Conversion mode"
    )
    parser.add_argument(
        "--input", "-i", required=True, help="Input file path"
    )
    parser.add_argument(
        "--output", "-o", help="Output file path"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Simulate without writing files"
    )

    return parser.parse_args()

def main():
    """Main CLI entry point."""
    args = parse_arguments()

    # Load configuration
    config = load_config()

    # Trigger conversion based on mode
    if args.mode == "csv2excel":
        csv_to_excel(args.input, args.output, dry_run=args.dry_run)
    elif args.mode == "excel2csv":
        excel_to_csv(args.input, args.output, dry_run=args.dry_run)
