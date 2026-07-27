from pathlib import Path
import xml.etree.ElementTree as ET
import csv
import json
import pickle
import re

# Heavy optional dependencies (pandas, pyarrow, duckdb, openpyxl) are imported lazily


_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _neutralize_formula(value):
    if isinstance(value, str) and value.startswith(("=", "+", "-", "@", "\t", "\r")):
        return "'" + value
    return value


def _safe_xml_name(name: str) -> str:
    if not isinstance(name, str):
        name = str(name)
    safe_name = re.sub(r"\W+", "_", name).strip("_") or "field"
    if not re.match(r"^[A-Za-z_][A-Za-z0-9_.-]*$", safe_name):
        safe_name = re.sub(r"[^A-Za-z0-9_.-]", "_", safe_name)
    return safe_name


def _safe_identifier(name: str) -> str:
    if not isinstance(name, str):
        raise ValueError(
            f"[Exporter] Unsafe identifier: {name!r}. Must be a string.")
    if not _IDENTIFIER_RE.match(name):
        raise ValueError(
            f"[Exporter] Unsafe identifier '{name}'. Table/column names must match ^[A-Za-z_][A-Za-z0-9_]*$.")
    return name


class Exporter:

    @staticmethod
    def to_csv(data: list[dict], file_path: str):
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow({k: _neutralize_formula(v)
                                for k, v in row.items()})
        print(f"CSV saved to: {file_path}")

    @staticmethod
    def to_tsv(data: list[dict], file_path: str):
        """Export data to Tab-Delimited TSV."""
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(
                f, fieldnames=data[0].keys(), delimiter='\t')
            writer.writeheader()
            writer.writerows([
                {k: _neutralize_formula(v) for k, v in row.items()}
                for row in data
            ])
        print(f"TSV saved to: {file_path}")

    @staticmethod
    def to_json(data: list[dict], file_path: str):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"JSON saved to: {file_path}")

    @staticmethod
    def to_ndjson(data: list[dict], file_path: str):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            for row in data:
                json.dump(row, f)
                f.write("\n")
        print(f"NDJSON saved to: {file_path}")

    @staticmethod
    def to_html(data: list[dict], file_path: str, title: str = "Data"):
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        columns = list(data[0].keys())
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("<html><head><meta charset=\"utf-8\"><title>")
            f.write(title)
            f.write("</title></head><body>\n")
            f.write("<table border=\"1\">\n<tr>")
            for col in columns:
                f.write(f"<th>{col}</th>")
            f.write("</tr>\n")
            for row in data:
                f.write("<tr>")
                for col in columns:
                    value = row.get(col, "")
                    f.write(f"<td>{_neutralize_formula(value)}</td>")
                f.write("</tr>\n")
            f.write("</table>\n</body></html>")
        print(f"HTML saved to: {file_path}")

    @staticmethod
    def to_pickle(data: list[dict], file_path: str):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "wb") as f:
            pickle.dump(data, f)
        print(f"Pickle saved to: {file_path}")

    @staticmethod
    def to_dataframe(data: list[dict], engine: str = "pandas"):
        if engine == "pandas":
            try:
                import pandas as pd
            except Exception as e:
                raise ImportError(
                    "DataFrame export requires pandas. Install pandas and retry."
                ) from e
            return pd.DataFrame(data)
        if engine == "polars":
            try:
                import polars as pl
            except Exception as e:
                raise ImportError(
                    "DataFrame export requires polars. Install polars and retry."
                ) from e
            return pl.DataFrame(data)
        raise ValueError(f"Unknown dataframe engine: {engine}")

    @staticmethod
    def stream_to_csv(batch_iter, file_path: str):
        """Write batches (iterable of row lists) to CSV incrementally."""
        first_batch = None
        it = iter(batch_iter)
        try:
            first_batch = next(it)
        except StopIteration:
            raise ValueError("No data to export.")

        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=first_batch[0].keys())
            writer.writeheader()
            for row in first_batch:
                writer.writerow({k: _neutralize_formula(v)
                                for k, v in row.items()})
            for batch in it:
                for row in batch:
                    writer.writerow({k: _neutralize_formula(v)
                                    for k, v in row.items()})
        print(f"CSV saved to: {file_path}")

    @staticmethod
    def stream_to_json(batch_iter, file_path: str):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        first = True
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('[')
            for batch in batch_iter:
                for row in batch:
                    if not first:
                        f.write(',\n')
                    json.dump(row, f)
                    first = False
            f.write(']')
        print(f"JSON saved to: {file_path}")

    @staticmethod
    def stream_to_ndjson(batch_iter, file_path: str):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            for batch in batch_iter:
                for row in batch:
                    json.dump(row, f)
                    f.write("\n")
        print(f"NDJSON saved to: {file_path}")

    @staticmethod
    def to_sql(data: list[dict], table_name: str, file_path: str, create_table: bool):
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        columns = list(data[0].keys())
        table_name = _safe_identifier(table_name)
        columns = [_safe_identifier(c) for c in columns]

        def format_sql_value(v):
            if v is None:
                return "NULL"
            if isinstance(v, bool):
                return "TRUE" if v else "FALSE"
            if isinstance(v, (int,)) and not isinstance(v, bool):
                return str(v)
            if isinstance(v, float):
                return repr(v)
            s = str(v)
            return "'" + s.replace("'", "''") + "'"

        first_row = data[0]
        type_map = {}
        for col, val in first_row.items():
            if isinstance(val, bool):
                type_map[col] = "BOOLEAN"
            elif isinstance(val, int) and not isinstance(val, bool):
                type_map[col] = "INTEGER"
            elif isinstance(val, float):
                type_map[col] = "REAL"
            else:
                type_map[col] = "TEXT"

        with open(file_path, "w", encoding="utf-8") as f:
            if create_table:
                cols_def = ",\n    ".join(
                    f"{col} {type_map[col]}" for col in columns)
                f.write(
                    f"CREATE TABLE IF NOT EXISTS {table_name} (\n    {cols_def}\n);\n\n")

            cols_str = ", ".join(columns)
            for row in data:
                values = ", ".join(format_sql_value(row.get(col))
                                   for col in columns)
                f.write(
                    f"INSERT INTO {table_name} ({cols_str}) VALUES ({values});\n")

        print(f"SQL file saved to: {file_path}")

    @staticmethod
    def to_cql(data: list[dict], keyspace: str, table_name: str, file_path: str, create_table: bool = True):
        """Export data as Cassandra CQL script."""
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        columns = list(data[0].keys())
        keyspace = _safe_identifier(keyspace)
        table_name = _safe_identifier(table_name)
        columns = [_safe_identifier(c) for c in columns]

        type_map = {}
        for col, val in data[0].items():
            if isinstance(val, bool):
                type_map[col] = "boolean"
            elif isinstance(val, int):
                type_map[col] = "int"
            elif isinstance(val, float):
                type_map[col] = "double"
            else:
                type_map[col] = "text"

        def format_cql_value(v):
            if v is None:
                return "null"
            if isinstance(v, bool):
                return "true" if v else "false"
            if isinstance(v, (int, float)):
                return str(v)
            s = str(v)
            return "'" + s.replace("'", "''") + "'"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"USE {keyspace};\n\n")
            if create_table:
                cols_def = ",\n    ".join(
                    f"{col} {type_map[col]}" for col in columns)
                f.write(
                    f"CREATE TABLE IF NOT EXISTS {table_name} (\n    {cols_def},\n    PRIMARY KEY ({columns[0]})\n);\n\n")
            for row in data:
                cols_str = ", ".join(columns)
                values = ", ".join(format_cql_value(row.get(c))
                                   for c in columns)
                f.write(
                    f"INSERT INTO {table_name} ({cols_str}) VALUES ({values});\n")
        print(f"CQL saved to: {file_path}")

    @staticmethod
    def to_firebase(data: list[dict], file_path: str):
        """Export data as Firebase-style JSON (keyed by unique id if present)."""
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        if not data:
            raise ValueError("No data to export.")

        # Use `id` or first key as Firebase node key
        key_field = "id" if "id" in data[0] else list(data[0].keys())[0]
        firebase_data = {str(row[key_field]): row for row in data}
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(firebase_data, f, indent=2)
        print(f"Firebase JSON saved to: {file_path}")

    @staticmethod
    def to_xml(data: list[dict], file_path: str, root_element: str = "root", record_element: str = "record"):
        """Export data to generic XML with custom root/record element names."""
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        root = ET.Element(_safe_xml_name(root_element))
        for row in data:
            rec = ET.SubElement(root, _safe_xml_name(record_element))
            for k, v in row.items():
                el = ET.SubElement(rec, _safe_xml_name(k))
                el.text = "" if v is None else str(v)

        tree = ET.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"XML saved to: {file_path}")

    @staticmethod
    def to_dbunit_xml(data: list[dict], file_path: str, table_name: str):
        """Export data to DBUnit-compatible XML format."""
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        table_name = _safe_identifier(table_name)

        dataset = ET.Element("dataset")
        for row in data:
            table_el = ET.SubElement(dataset, table_name)
            for k, v in row.items():
                if v is not None:
                    table_el.set(k, str(v))
        tree = ET.ElementTree(dataset)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"DBUnit XML saved to: {file_path}")

    @staticmethod
    def to_parquet(data: list[dict], file_path: str):
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        try:
            import pandas as pd
        except Exception as e:
            raise ImportError(
                "Parquet export requires pandas and pyarrow. Install both packages and retry.") from e
        df = pd.DataFrame(data)
        df.to_parquet(file_path, index=False)
        print(f"Parquet file saved to: {file_path}")

    @staticmethod
    def to_duckdb(data: list[dict], file_path: str, table_name: str = "data"):
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        try:
            import pandas as pd
            import duckdb
        except Exception as e:
            raise ImportError(
                "DuckDB export requires pandas and duckdb. Install both packages and retry.") from e
        df = pd.DataFrame(data)
        table_name = _safe_identifier(table_name)
        con = duckdb.connect(file_path)
        con.execute(
            f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")

        con.close()
        print(f"DuckDB saved at: {file_path} (table: {table_name})")

    @staticmethod
    def to_sqlalchemy(data: list[dict], connection_string: str, table_name: str = "data", if_exists: str = "replace"):
        if not data:
            raise ValueError("No data to export.")
        try:
            import pandas as pd
            from sqlalchemy import create_engine
        except Exception as e:
            raise ImportError(
                "SQLAlchemy export requires pandas and SQLAlchemy. Install both packages and retry."
            ) from e
        df = pd.DataFrame(data)
        engine = create_engine(connection_string)
        df.to_sql(table_name, engine, if_exists=if_exists, index=False)
        engine.dispose()
        print(
            f"SQLAlchemy export complete to {connection_string} table {table_name}")

    @staticmethod
    def to_excel(data: list[dict], file_path: str, sheet_name: str = "Sheet1"):
        try:
            from openpyxl import Workbook
        except Exception as e:
            raise ImportError(
                "Excel export requires openpyxl. Install openpyxl and retry.") from e
        if not data:
            raise ValueError("No data to export.")
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        wb = Workbook()
        ws = wb.active
        ws.title = sheet_name

        headers = list(data[0].keys())
        ws.append(headers)
        for row in data:
            ws.append([_neutralize_formula(row.get(h)) for h in headers])
        wb.save(file_path)
        print(f"Excel saved to: {file_path}")
