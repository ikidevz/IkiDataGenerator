"""
00_quick_start.py - The Simplest Possible Example

This is the absolute minimum to get started with Iki Data Generator.
Run this to generate your first dataset in 30 seconds!
"""

from ikidatagen import IkiDataGenerator

# Define what fields you want
schema = ["first_name", "last_name", "email_address", "gender_binary"]

# Generate 100 records and export to CSV and JSON
IkiDataGenerator(schema).many(100).export("quick_start")

print("[OK] Generated 100 user records!")
print("[FOLDER] Check output/ folder for quick_start.csv and quick_start.json")
