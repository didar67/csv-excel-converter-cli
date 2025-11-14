"""
Tests for YAML-based configuration loader.

Ensures:
- YAML loads successfully
- Missing config file raises FileNotFoundError
- Invalid YAML raises safe parsing error
"""

from pathlib import Path
import pytest
import yaml

from script.config_loader import load_config, CONFIG_PATH

def test_load_config_success(tmp_path, monkeypatch):
    """Valid YAML should load and return a dictionary."""
    fake_config = tmp_path / "config.yaml"
    fake_config.write_text("paths:\n  input: sample.csv\nsettings:\n  mode: test")

    monkeypatch.setattr("script.config_loader.CONFIG_PATH", fake_config)

    config = load_config()
    assert config["paths"]["input"] == "sample.csv"

def test_missing_config_file(monkeypatch):
    """Missing file should raise FileNotFoundError."""
    monkeypatch.setattr("script.config_loader.CONFIG_PATH", Path("nonexistent.yaml"))
    with pytest.raises(FileNotFoundError):
        load_config()

def test_invalid_yaml(tmp_path, monkeypatch):
    """Bad YAML must raise yaml.YAMLError."""
    bad_yaml = tmp_path / "config.yaml"
    bad_yaml.write_text("paths: [unclosed list")

    monkeypatch.setattr("script.config_loader.CONFIG_PATH", bad_yaml)

    with pytest.raises(yaml.YAMLError):
        load_config()
