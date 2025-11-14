"""
Unit tests for CLI argument parser and execution flow.

This suite ensures:
- CLI argument parsing works correctly.
- Invalid arguments raise appropriate errors.
- Converter functions are called with correct parameters using mocks.
"""

import pytest
from unittest.mock import patch

from script.cli import parse_arguments, main


def test_parse_arguments_valid_csv2excel():
    """Verify valid csv2excel argument parsing."""
    test_args = ["csv2excel", "--input", "sample.csv", "--output", "out.xlsx"]
    with patch("sys.argv", ["cli.py"] + test_args):
        args = parse_arguments()
        assert args.mode == "csv2excel"
        assert args.input == "sample.csv"
        assert args.output == "out.xlsx"


def test_parse_arguments_valid_excel2csv():
    """Verify valid excel2csv argument parsing."""
    test_args = ["excel2csv", "--input", "in.xlsx"]
    with patch("sys.argv", ["cli.py"] + test_args):
        args = parse_arguments()
        assert args.mode == "excel2csv"
        assert args.input == "in.xlsx"


def test_parse_arguments_invalid_mode():
    """Ensure invalid mode triggers argparse error."""
    test_args = ["invalid_mode", "--input", "x.csv"]
    with patch("sys.argv", ["cli.py"] + test_args):
        with pytest.raises(SystemExit):
            parse_arguments()


@patch("script.cli.csv_to_excel")
@patch("script.cli.load_config")
def test_main_calls_csv_to_excel(mock_config, mock_csv):
    """Verify main() triggers csv_to_excel with correct args."""
    mock_config.return_value = {}

    test_args = ["csv2excel", "--input", "a.csv", "--output", "b.xlsx"]
    with patch("sys.argv", ["cli.py"] + test_args):
        main()
        mock_csv.assert_called_once_with("a.csv", "b.xlsx", dry_run=False)


@patch("script.cli.excel_to_csv")
@patch("script.cli.load_config")
def test_main_calls_excel_to_csv(mock_config, mock_excel):
    """Verify main() triggers excel_to_csv with correct args."""
    mock_config.return_value = {}

    test_args = ["excel2csv", "--input", "a.xlsx"]
    with patch("sys.argv", ["cli.py"] + test_args):
        main()
        mock_excel.assert_called_once_with("a.xlsx", None, dry_run=False)
