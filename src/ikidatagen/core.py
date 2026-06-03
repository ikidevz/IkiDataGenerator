from __future__ import annotations

from pathlib import Path
from typing import Any

from .base_generator import BaseGenerator
from .exporters import Exporter


# Formats supported by .export()
_SUPPORTED_FORMATS = frozenset({
    "csv", "tsv", "json", "sql", "cql",
    "firebase", "excel", "xml", "dbunit",
    "parquet", "duckdb",
})


class IkiDataGenerator:
    """
    Main entrypoint for IkiDataGenerator.

    Schema accepts a mix of plain strings (shorthand) and dicts (full control).

    Examples
    --------
    # Minimal — just list the fields you want
    schema = ["first_name", "last_name", "email_address", "gender_binary"]
    IkiDataGenerator(schema).many(100).export("users")

    # Mixed — strings for defaults, dicts when you need options or a custom label
    schema = [
        "first_name",
        "last_name",
        {
            "key_label": "salary_range",
            "label":     "Salary",           # renames the output column
            "options":   {"blank_percentage": 0.1},
        },
        {
            "key_label": "template",
            "options":   {"template": "{{first_name}} {{last_name}}"},
        },
    ]
    IkiDataGenerator(schema).many(50).export("staff", formats=["csv", "json"])

    # Old-style full dict (still works — group is now optional)
    schema = [
        {"label": "ID",    "key_label": "row_number"},
        {"label": "Email", "key_label": "email_address", "group": "it"},
    ]
    """

    def __init__(self, schema: list[str | dict[str, Any]]):
        self._generator = BaseGenerator(schema)
        self._data: list[dict] | None = None

    # ------------------------------------------------------------------
    # Generation
    # ------------------------------------------------------------------

    def many(self, n: int) -> "IkiDataGenerator":
        """Generate n records.  Returns self for chaining."""
        self._data = self._generator.generate_many(n)
        return self

    def one(self) -> dict:
        """Generate and return a single record as a dict."""
        return self._generator.generate_many(1)[0]

    @property
    def data(self) -> list[dict]:
        """Access the generated records after calling .many()."""
        if self._data is None:
            raise ValueError(
                "No data generated yet. Call .many(n) before accessing .data."
            )
        return self._data

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------

    def export(
        self,
        table_name: str,
        output_dir: str = "output",
        formats: list[str] | None = None,
        create_table: bool = True,
    ) -> "IkiDataGenerator":
        """
        Export generated data to one or more file formats.

        Parameters
        ----------
        table_name   : Base name used for the output file(s) and SQL table name.
        output_dir   : Directory to write files into (created if it doesn't exist).
        formats      : List of format strings.  Defaults to ["csv"].
                       Supported: csv, tsv, json, sql, cql, firebase,
                                  excel, xml, dbunit, parquet, duckdb.
        create_table : Whether to include CREATE TABLE in SQL / CQL output.
        """
        if not self._data:
            raise ValueError(
                "No data to export. Call .many(n) before .export()."
            )

        Path(output_dir).mkdir(parents=True, exist_ok=True)

        target_formats = formats or ["csv"]
        for fmt in target_formats:
            fmt_lower = fmt.lower()

            if fmt_lower not in _SUPPORTED_FORMATS:
                print(f"[Warning] Unknown export format '{fmt}' — skipped.")
                continue

            base = f"{output_dir}/{table_name}"

            match fmt_lower:
                case "csv":
                    Exporter.to_csv(self._data, f"{base}.csv")
                case "tsv":
                    Exporter.to_tsv(self._data, f"{base}.tsv")
                case "json":
                    Exporter.to_json(self._data, f"{base}.json")
                case "sql":
                    Exporter.to_sql(self._data, table_name,
                                    f"{base}.sql", create_table)
                case "cql":
                    Exporter.to_cql(
                        self._data,
                        keyspace=table_name,
                        table_name=table_name,
                        file_path=f"{base}.cql",
                        create_table=create_table,
                    )
                case "firebase":
                    Exporter.to_firebase(self._data, f"{base}_firebase.json")
                case "excel":
                    Exporter.to_excel(self._data, f"{base}.xlsx")
                case "xml":
                    Exporter.to_xml(
                        self._data,
                        f"{base}.xml",
                        root_element="root",
                        record_element="record",
                    )
                case "dbunit":
                    Exporter.to_dbunit_xml(
                        self._data, f"{base}_dbunit.xml", table_name)
                case "parquet":
                    Exporter.to_parquet(self._data, f"{base}.parquet")
                case "duckdb":
                    Exporter.to_duckdb(
                        self._data, f"{base}.duckdb", table_name)

        print(f"[OK] Export complete -> {output_dir}/{table_name}.*")
        return self
