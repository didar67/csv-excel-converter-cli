"""
Tests for CSV <-> Excel conversion logic.

Ensures:
- CSV → Excel works
- Excel → CSV works
- Dry-run does not write output
"""

from pathlib import Path
import pandas as pd
import pytest

from script.converter import csv_to_excel, excel_to_csv

def test_csv_to_excel_conversion(tmp_path):
    """CSV file should convert to XLSX successfully."""
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("a,b\n1,2")

    output_excel = tmp_path / "output.xlsx"
    csv_to_excel(str(csv_file), str(output_excel))

    assert output_excel.exists()

def test_excel_to_csv_conversion(tmp_path):
    """Excel should convert to CSV successfully."""
    excel_file = tmp_path / "data.xlsx"
    df = pd.DataFrame({"a": [1], "b": [2]})
    df.to_excel(excel_file, index=False)

    output_csv = tmp_path / "converted.csv"
    excel_to_csv(str(excel_file), str(output_csv))

    assert output_csv.exists()

def test_dry_run_does_not_write(tmp_path):
    """Dry-run mode should NOT create output file."""
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("x,y\n5,6")

    target = tmp_path / "dry.xlsx"
    csv_to_excel(str(csv_file), str(target), dry_run=True)

    assert not target.exists()
