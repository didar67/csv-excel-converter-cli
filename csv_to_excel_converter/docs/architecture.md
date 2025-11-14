# Architecture — CSV ⇄ Excel Converter

This document explains the internal structure, flow, and component responsibilities of the **CSV ⇄ Excel Converter** tool. It serves as a recruiter-friendly technical breakdown.

---

## High-Level Architecture

The system follows a clean, modular, layered architecture:

```
┌──────────────────────────┐
│         CLI Layer        │  ← script/cli.py
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│    Application Logic      │  ← converter, config_loader
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│   Core Infrastructure     │  ← logger, helpers, config
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│     External Systems      │  ← filesystem, pandas, yaml
└──────────────────────────┘
```

Each module has a single responsibility and communicates through stable function contracts.

---

## Module Breakdown

### **1. CLI Layer (script/cli.py)**

* Handles argparse-based command parsing
* Validates input/output arguments
* Dispatches execution to correct conversion function
* Integrates configuration loading

### **2. Converter Engine (script/converter.py)**

* Responsible for CSV ↔ Excel transformations
* Uses pandas for data manipulation
* Provides dry-run support
* Writes structured logs

### **3. Configuration Loader (script/config_loader.py)**

* Reads YAML config
* Optional Pydantic validation
* Handles invalid/missing configuration errors

### **4. Logger (core/logger.py)**

* Central logging system
* Rotating log handlers (info + error)
* Console and file logging
* Singleton logger to avoid duplicates

### **5. Helper Utilities (utils/helper.py)**

* Safe file path validation
* Reusable helper functions for CLI and conversions

### **6. Test Suite (tests/)**

* pytest-based end-to-end testing
* Mocks to isolate filesystem
* Validates CLI, converter, logger, configuration

---

## Data Flow Diagram

```
           User CLI
               │
               ▼
      parse_arguments()
               │
               ▼
         load_config()
               │
               ▼
    ┌────────────────────┐
    │ Conversion Engine  │
    └────────────────────┘
               │
               ▼
        pandas I/O ops
               │
               ▼
      Logging & Validation
               │
               ▼
        Output File (.csv/.xlsx)
```

---

## Execution Sequence

1. User runs: `python main.py csv2excel ...`
2. CLI parses arguments
3. Configuration is loaded
4. File validation occurs
5. Conversion is executed (or simulated via dry-run)
6. Logs record every step
7. Output written to filesystem

---

## Design Principles

* **Modularity** → each module has a single responsibility
* **Extensibility** → easy to add more formats later (JSON, SQL, etc.)
* **Testability** → every layer is unit-testable with mocks
* **Observability** → rich structured logging
* **Config-driven** → behavior controlled from YAML

---

## Summary

This architecture is designed to feel like a real professional DevOps automation tool — fully structured, testable, maintainable, and production-ready. Recruiters will immediately recognize the clean engineering standards and layered design.
