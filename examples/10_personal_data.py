"""
10_personal_data.py - Personal & Identity Information

Generate realistic personal data including names, gender, dates, documents.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "title",
    "first_name",
    "last_name",
    {
        "key_label": "datetime",
        "label": "DOB",
    },
    "gender_binary",
    "nationality",
    {
        "key_label": "ssn",
        "label": "Passport",
    },
    {
        "key_label": "ssn",
        "label": "SSN",
    },
    {
        "key_label": "driver_license_number",
        "label": "Driver License",
    },
]

IkiDataGenerator(schema).many(100).export(
    "personal_data", formats=["csv", "json"])

print("[OK] Generated 100 personal profiles!")
