"""
02_export_formats.py - Export to All Supported Formats

This example shows how to export to CSV, JSON, SQL, Excel, Parquet, and more!
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    "email_address",
    {
        "key_label": "current_timestamp",
        "label": "created_at",
    },
]

# Generate data and export to ALL formats
IkiDataGenerator(schema).many(100).export(
    "export_demo",
    formats=[
        "csv",      # Spreadsheet - universal
        "json",     # JSON - APIs and JavaScript
        "tsv",      # Tab-separated - Excel alternative
        "sql",      # SQL INSERT statements
        "parquet",  # Columnar - Big Data
        "duckdb",   # DuckDB database - instant querying
        "excel",    # Excel workbook
        "xml",      # XML - legacy systems
    ]
)

print("[OK] Generated data in 8 different formats!")
print("[FOLDER] Check output/ folder for:")
print("   - export_demo.csv")
print("   - export_demo.json")
print("   - export_demo.tsv")
print("   - export_demo.sql")
print("   - export_demo.parquet")
print("   - export_demo.duckdb")
print("   - export_demo.xlsx")
print("   - export_demo.xml")
