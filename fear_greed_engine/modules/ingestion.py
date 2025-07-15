"""
Module for ingesting data from various sources (Twitter, Reddit, News).
"""
import json
import os

def ingest_mock_data(source, data_dir="data"):
    """Read mock data from a JSON file in the data directory."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, data_dir, f"{source}_sample.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f) 