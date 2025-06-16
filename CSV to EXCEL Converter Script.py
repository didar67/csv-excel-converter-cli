""" CSV ⇄ Excel Converter CLI Tool

Overview:
This CLI-based Python tool allows reliable conversion between CSV and Excel formats.
It features argparse-based CLI input, error handling, structured logging, and config file usage.
Perfect for data analysts, DevOps, or automation pipelines."""

import os
import sys
import logging
import argparse
import configparser
import pandas as pd

# Configuaration loader
"""Setup Configuaration"""
config = configparser.ConfigParser()
config.read("config.ini")
LOG_FILE = config.get("settings", "log_file", fallback="coversion.log")

# Logger setup
"""Configure logger to save logs to file"""
def init_logger():
    logging.basicConfig(
        filename= LOG_FILE,
        level= logging.INFO,
        format= "%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logger initialize successfully.")

# Coversion Functions of files
def csv_to_excel(csv_path, excel_path):
    """Read CSV and writes Excel format"""
    try:
       df = pd.read_csv(csv_path)
       df.to_excel(excel_path, index=False)
       logging.info(f"✅ CSV --> Excel: {csv_path} --> {excel_path}")
       print(f"✅ Converted to {excel_path}")

    except FileNotFoundError:
        logging.error(f"CSV file not found: {csv_path}")
        print("❌ CSV file not found.")
    except pd.errors.EmptyDataError:
        logging.error(f"CSV file is empty: {csv_path}")
        print("❌ CSV file is empty.")
    except pd.errors.ParserError:
        logging.error(f"CSV parssing error: {csv_path}")
        print("❌ CSV parssing error.")
    except PermissionError:
        logging.error(f"Permission denied while accessing: {csv_path}")
        print("❌ Permission denied.")
    except Exception as err:
        logging.error(f"Unhandled error during CSV --> Excel: {err}")
        print("❌ Unexpected error: {err}")


def excel_to_csv(excel_path, csv_path):
        """Read Excel and writes CSV format"""
        try:
            df = pd.read_excel(excel_path)
            df.to_csv(csv_path, index=False)
            logging.info(f"✅ EXCEL --> CSV: {excel_path} --> {csv_path}")
            print(f"✅ Covertewd to {csv_path}")

        except FileNotFoundError:
            logging.error(f"Excel file not found: {excel_path}")
            print(f"❌ File not found: {excel_path}")
        except ValueError:
            logging.error(f"Invalid excel file format: {excel_path}")
            print("❌ Invalid excel file.")
        except PermissionError:
            logging.error(f"Permission denied while accessing: {excel_path}")
            print("❌ Permission denied.")
        except Exception as err:
            logging.error(f"Unhandled erro during Excel --> CSV: {err}")
            print(f"❌ Unexpected error: {err}")

# CLI Argument parser
"""Parses command-line arguments """
def get_args():
  parser = argparse.ArgumentParser(description="🔄 Convert between CSV and Excel files using CLI.")

  parser.add_argument("mode", choices=["csv2excel", "excel2csv"], help="Choose conversion mode")
  parser.add_argument("input_path", help="Path of input file(.csv or .xlsx)")
  parser.add_argument("output_path", help="Path of output file(.xlsx or .csv)")

  return parser.parse_args()

# Main Function
def main():
    init_logger()
    args = get_args()

    if not os.path.isfile(args.input_path):
        logging.error(f"Input file does not exist: {args.input_path}")
        print(f"❌ Input file does not exist: {args.input_path}")
        sys.exit(1)

    if args.mode == "csv2excel":
        csv_to_excel(args.input_path, args.output_path)

    elif args.mode == "excel2csv":
        excel_to_csv(args.input_path, args.output_path)

# Entry Point
if __name__ == "__main__":
    try:
       main()

    except KeyboardInterrupt:
        logging.warning(f"⚠️ Script interrupted via KeyboardInterrupt.")
        print("Script manually interrupted by user.")

    finally:
        logging.info("Script finished.")