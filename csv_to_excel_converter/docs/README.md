# CSV ⇄ Excel Converter — Professional Documentation

## 📌 Overview

This project provides a fully automated, production-ready CLI tool for converting files between **CSV** and **Excel (.xlsx)** formats. It includes centralized logging, configuration-driven behavior, dry-run support, modular architecture, and end-to-end unit test coverage.

The tool is designed to meet real-world DevOps automation needs and follows industry-standard engineering practices.

---

## Features

* Convert **CSV → Excel** and **Excel → CSV**
* Dry-run mode (no file writes)
* Centralized rotating log system
* YAML-based configuration
* Clean CLI interface with argparse
* Fully modular Python package
* 100% unit-tested (pytest + mocks)
* Production-ready folder structure

---

## 📁 Project Structure

```
csv_to_excel_converter/
│
├── config/
│   └── config.yaml
│
├── core/
│   ├── __init__.py
│   └── logger.py
│
├── script/
│   ├── __init__.py
│   ├── cli.py
│   ├── converter.py
│   └── config_loader.py
│
├── utils/
│   ├── __init__.py
│   └── helper.py
│
├── tests/
│   ├── test_logger.py
│   ├── test_cli.py
│   ├── test_converter.py
│   └── test_config.py
│
├── docs/
│   ├── README.md
│   └── architecture.md
│
├── main.py
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Installation

```bash
git clone <repo-url>
cd csv_to_excel_converter
pip install -r requirements.txt
```

---

## Usage

### **1. CSV → Excel**

```bash
python main.py csv2excel --input data.csv --output data.xlsx
```

### **2. Excel → CSV**

```bash
python main.py excel2csv --input report.xlsx --output report.csv
```

### **3. Dry-run Mode**

```bash
python main.py csv2excel --input sample.csv --dry-run
```

---

## Configuration

All configurable paths/settings are stored in:

```
config/config.yaml
```

Edit this file to update default paths, behavior rules, settings, etc.

---

## Testing

Run complete test suite:

```bash
pytest -v
```

---

## Logging

Logs are stored under **logs/** directory:

* `info.log` → normal operations
* `error.log` → errors & exceptions

Rotating handlers ensure logs stay clean and manageable.

---

## Architecture Document

The full technical architecture, flow diagram, and module interaction breakdown is available in:

```
docs/architecture.md
```

---

## License

This project is licensed under the **MIT License**.
