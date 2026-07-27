from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from .base_generator import BaseGenerator
from .exporters import Exporter


# Formats supported by .export()
_SUPPORTED_FORMATS = frozenset({
    "csv", "tsv", "json", "ndjson", "sql", "cql",
    "firebase", "excel", "html", "pickle", "xml",
    "dbunit", "parquet", "duckdb",
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

    def __init__(
        self,
        schema: list[str | dict[str, Any]],
        seed: int | None = None,
    ):
        self._generator = BaseGenerator(schema, seed=seed)
        self._data: list[dict] | None = None

    # ------------------------------------------------------------------
    # Generation
    # ------------------------------------------------------------------

    def many(self, n: int) -> "IkiDataGenerator":
        """Generate n records.  Returns self for chaining."""
        self._data = self._generator.generate_many(n)
        return self

    def stream(self, n: int, batch_size: int = 1000):
        """Stream generated rows in batches using the internal generator.

        Yields lists of rows (dicts) of at most `batch_size` until n rows produced.
        """
        yield from self._generator.stream(n, batch_size=batch_size)

    def one(self) -> dict:
        """Generate and return a single record as a dict."""
        return self._generator.generate_many(1)[0]

    async def many_async(self, n: int) -> list[dict]:
        """Generate n records asynchronously. Returns a list of rows."""
        return await self._many_async_impl(n)

    async def _many_async_impl(self, n: int) -> list[dict]:
        return self._generator.generate_many(n)

    @property
    def data(self) -> list[dict]:
        """Access the generated records after calling .many()."""
        if self._data is None:
            raise ValueError(
                "No data generated yet. Call .many(n) before accessing .data."
            )
        return self._data

    def dataframe(self, engine: str = "pandas"):
        """Return generated records as a pandas or polars DataFrame."""
        if self._data is None:
            raise ValueError(
                "No data generated yet. Call .many(n) before accessing .data.")
        return Exporter.to_dataframe(self._data, engine)

    def generate_event_stream(
        self,
        n: int,
        start_time: str | datetime | None = None,
        step_seconds: int = 60,
        timestamp_field: str = "event_timestamp",
        sequence_field: str = "event_sequence",
    ) -> list[dict]:
        """Generate rows with synthetic event timestamps and monotonically increasing sequences."""
        if self._data is None:
            self.many(n)

        rows = list(self._data or self._generator.generate_many(n))
        base_time = start_time
        if base_time is None:
            base_time = datetime.utcnow().replace(microsecond=0)
        elif isinstance(base_time, str):
            base_time = datetime.fromisoformat(
                base_time.replace("Z", "+00:00"))

        event_rows = []
        for index, row in enumerate(rows, start=1):
            event_row = dict(row)
            event_row[sequence_field] = index
            event_row[timestamp_field] = (
                base_time + timedelta(seconds=(index - 1) * step_seconds)).isoformat()
            event_rows.append(event_row)
        return event_rows

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------

    def export(
        self,
        table_name: str,
        output_dir: str = "output",
        formats: list[str] | None = None,
        create_table: bool = True,
        n: int | None = None,
        stream: bool = False,
        batch_size: int = 1000,
    ) -> "IkiDataGenerator":
        """
        Export generated data to one or more file formats.

        Parameters
        ----------
        table_name   : Base name used for the output file(s) and SQL table name.
        output_dir   : Directory to write files into (created if it doesn't exist).
        formats      : List of format strings.  Defaults to ["csv"].
                       Supported: csv, tsv, json, ndjson, html, pickle,
                                  sql, cql, firebase, excel, xml, dbunit,
                                  parquet, duckdb.
        create_table : Whether to include CREATE TABLE in SQL / CQL output.
        """
        if not self._data and not stream:
            raise ValueError(
                "No data to export. Call .many(n) before .export(), or use stream=True to stream generation."
            )
        if stream and self._data is None and n is None:
            raise ValueError(
                "When using stream=True you must provide 'n' to indicate how many rows to generate.")

        target_formats = formats or ["csv"]
        stream_formats = {fmt.lower() for fmt in target_formats if fmt}
        if stream and self._data is None and n is not None and not stream_formats.issubset({"csv", "json", "ndjson"}):
            self._data = self._generator.generate_many(n)

        resolved_output_dir = Path(output_dir).resolve()
        resolved_output_dir.mkdir(parents=True, exist_ok=True)
        for fmt in target_formats:
            fmt_lower = fmt.lower()

            if fmt_lower not in _SUPPORTED_FORMATS:
                print(f"[Warning] Unknown export format '{fmt}' — skipped.")
                continue

            if Path(table_name).is_absolute() or ".." in Path(table_name).parts or "/" in table_name or "\\" in table_name or Path(table_name).name != table_name:
                raise ValueError(
                    "table_name must be a simple file name without path components.")

            base = str(resolved_output_dir / table_name)

            match fmt_lower:
                case "csv":
                    if stream and self._data is None:
                        Exporter.stream_to_csv(self._generator.stream(
                            n=n, batch_size=batch_size), f"{base}.csv")
                    else:
                        Exporter.to_csv(self._data, f"{base}.csv")
                case "tsv":
                    Exporter.to_tsv(self._data, f"{base}.tsv")
                case "json":
                    if stream and self._data is None:
                        Exporter.stream_to_json(self._generator.stream(
                            n=n, batch_size=batch_size), f"{base}.json")
                    else:
                        Exporter.to_json(self._data, f"{base}.json")
                case "ndjson":
                    if stream and self._data is None:
                        Exporter.stream_to_ndjson(
                            self._generator.stream(n=n, batch_size=batch_size),
                            f"{base}.ndjson",
                        )
                    else:
                        Exporter.to_ndjson(self._data, f"{base}.ndjson")
                case "html":
                    Exporter.to_html(self._data, f"{base}.html")
                case "pickle":
                    Exporter.to_pickle(self._data, f"{base}.pkl")
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
