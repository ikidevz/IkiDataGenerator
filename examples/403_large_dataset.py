"""
403_large_dataset.py - Generating Large Datasets (1M+ Records)

Tips for generating and exporting massive datasets efficiently.
Use Parquet format for best performance and file size.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    "email_address",
    "gender_binary",
    "country",
    "city",
    {
        "key_label": "current_timestamp",
        "label": "Timestamp",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Active", "Inactive", "Pending"]}
    },
    {
        "key_label": "number",
        "label": "Score",
        "options": {"min": 0, "max": 100}
    },
]

print("[CHART] Generating large dataset...")
print("   This will create 1,000,000 records (may take a minute)")


IkiDataGenerator(schema).many(1000000).export(
    "large_dataset",
    formats=["parquet"]  # Parquet is most efficient for large datasets
)

print("[OK] Successfully generated 1,000,000 records!")
print("   [FOLDER] Output: output/large_dataset.parquet")
print("   Tip: Use Parquet for big data - much faster than CSV!")

# Advanced: Generate in chunks if memory is limited
print("\n Alternative: Generate in smaller chunks")
for i in range(10):
    print(f"   Generating chunk {i+1}/10 (100k records)...")
    IkiDataGenerator(schema).many(100000).export(
        f"large_dataset_chunk_{i+1}",
        formats=["parquet"]
    )

print("[OK] Chunk generation complete!")
