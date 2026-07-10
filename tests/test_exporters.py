from pathlib import Path
import pytest

from ikidatagen.core import IkiDataGenerator
from ikidatagen.exporters import Exporter


def test_exporter_to_csv_and_json(tmp_path):
    data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    csv_file = tmp_path / "data.csv"
    json_file = tmp_path / "data.json"

    Exporter.to_csv(data, str(csv_file))
    Exporter.to_json(data, str(json_file))

    assert csv_file.exists()
    assert json_file.exists()
    assert csv_file.read_text(encoding="utf-8").startswith("id,name")
    assert "Alice" in json_file.read_text(encoding="utf-8")


def test_exporter_to_tsv_and_firebase(tmp_path):
    data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    tsv_file = tmp_path / "data.tsv"
    firebase_file = tmp_path / "data_firebase.json"

    Exporter.to_tsv(data, str(tsv_file))
    Exporter.to_firebase(data, str(firebase_file))

    assert tsv_file.exists()
    assert firebase_file.exists()
    assert "Alice" in tsv_file.read_text(encoding="utf-8")
    assert "1" in firebase_file.read_text(encoding="utf-8")


def test_exporter_to_xml_and_dbunit(tmp_path):
    data = [{"id": 1, "name": "Alice"}]
    xml_file = tmp_path / "data.xml"
    dbunit_file = tmp_path / "data_dbunit.xml"

    Exporter.to_xml(data, str(xml_file))
    Exporter.to_dbunit_xml(data, str(dbunit_file), "people")

    assert xml_file.exists()
    assert dbunit_file.exists()
    assert "<root>" in xml_file.read_text(encoding="utf-8")
    assert "<people" in dbunit_file.read_text(encoding="utf-8")


def test_exporter_safe_sql_identifier(tmp_path):
    data = [{"id": 1, "name": "Alice"}]
    file_path = tmp_path / "valid.sql"
    assert Exporter.to_sql(data, "valid_name", str(
        file_path), create_table=True) is None


def test_exporter_invalid_identifier_raises(tmp_path):
    data = [{"id": 1}]
    with pytest.raises(ValueError):
        Exporter.to_sql(data, "123invalid", str(
            tmp_path / "invalid.sql"), create_table=True)


def test_exporter_optional_parquet_duckdb(tmp_path):
    data = [{"id": 1, "name": "Alice"}]
    parquet_file = tmp_path / "data.parquet"
    duckdb_file = tmp_path / "data.duckdb"

    Exporter.to_parquet(data, str(parquet_file))
    assert parquet_file.exists()

    Exporter.to_duckdb(data, str(duckdb_file), table_name="people")
    assert duckdb_file.exists()


def test_exporter_neutralizes_formula_injection_payloads(tmp_path):
    data = [{"notes": "=HYPERLINK(\"http://evil.example\", \"click\")"}]
    csv_file = tmp_path / "formula.csv"

    Exporter.to_csv(data, str(csv_file))
    content = csv_file.read_text(encoding="utf-8")
    assert "'=" in content


def test_exporter_to_xml_sanitizes_invalid_tag_names(tmp_path):
    data = [{"bad name": "Alice"}]
    xml_file = tmp_path / "data.xml"

    Exporter.to_xml(data, str(xml_file))
    assert xml_file.exists()
    assert "bad_name" in xml_file.read_text(encoding="utf-8")


def test_export_rejects_path_traversal_table_names(tmp_path):
    gen = IkiDataGenerator(["first_name"]).many(1)
    with pytest.raises(ValueError):
        gen.export("../../escape",
                   output_dir=str(tmp_path / "safe"), formats=["csv"])
