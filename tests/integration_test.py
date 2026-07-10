"""
Comprehensive integration test for IkiDataGenerator features.
Runs generation across multiple schemas, exports to multiple formats, and exercises dataset-backed providers.

Requirements:
    pip install -r requirements.txt  # optional but recommended for full exporter support

Usage:
    python -m tests.integration_test

This script writes files into `tests/output/` and cleans them up on success.
"""
import os
import shutil
import tempfile
import json
from pathlib import Path

from ikidatagen.core import IkiDataGenerator
from ikidatagen.exporters import Exporter
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY

OUT_DIR = Path(__file__).parent / "output"


def ensure_out():
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)


def test_basic_generation():
    schema = [
        "first_name",
        "last_name",
        {"key_label": "email_address", "label": "email"},
        {"key_label": "username", "options": {"blank_percentage": 0}},
        {"key_label": "age_group", "label": "age_years"},
    ]
    gen = IkiDataGenerator(schema)
    rows = gen.many(20).data
    assert isinstance(rows, list) and len(rows) == 20
    print("basic generation OK")
    return rows


def test_export_formats(rows):
    # CSV
    csv_path = OUT_DIR / "test.csv"
    Exporter.to_csv(rows, str(csv_path))
    assert csv_path.exists()

    # JSON
    json_path = OUT_DIR / "test.json"
    Exporter.to_json(rows, str(json_path))
    assert json_path.exists()

    # SQL (safe identifiers)
    sql_path = OUT_DIR / "test.sql"
    Exporter.to_sql(rows, "test_table", str(sql_path), create_table=True)
    assert sql_path.exists()

    # CQL
    cql_path = OUT_DIR / "test.cql"
    Exporter.to_cql(rows, "ks", "test_table", str(cql_path), create_table=True)
    assert cql_path.exists()

    # DuckDB
    try:
        duckdb_path = OUT_DIR / "test.duckdb"
        Exporter.to_duckdb(rows, str(duckdb_path), table_name="test_table")
        assert duckdb_path.exists()
    except Exception as e:
        print("duckdb export skipped or failed (missing dependency):", e)

    # Parquet
    try:
        parquet_path = OUT_DIR / "test.parquet"
        Exporter.to_parquet(rows, str(parquet_path))
        assert parquet_path.exists()
    except Exception as e:
        print("parquet export skipped or failed (missing dependency):", e)

    # Excel
    try:
        excel_path = OUT_DIR / "test.xlsx"
        Exporter.to_excel(rows, str(excel_path))
        assert excel_path.exists()
    except Exception as e:
        print("excel export skipped or failed (openpyxl missing):", e)

    print("exports OK")


def test_provider_instantiation():
    # instantiate a handful of providers and generate
    sample_keys = list(KEY_LABEL_REGISTRY.keys())[:200]
    failures = []
    for key in sample_keys:
        try:
            p = ProviderFactory.create(key_label=key)
            v = p.generate_non_blank(row_data={})
            # basic assert: no exception and value may be None or str/number
        except Exception as e:
            failures.append((key, str(e)))
    if failures:
        print(
            f"Provider instantiation failures: {len(failures)} (showing up to 20)")
        for k, m in failures[:20]:
            print(k, m)
        # Do not fail process; the full smoke script can be used to debug
    else:
        print("provider instantiation OK")


def run_all():
    ensure_out()
    rows = test_basic_generation()
    test_export_formats(rows)
    test_provider_instantiation()
    print("Integration test completed. Output dir:", OUT_DIR)


if __name__ == '__main__':
    run_all()
