"""
12_identity_documents.py - Identification & Documents

Passports, IDs, driver licenses, and legal documents.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "ssn",
        "label": "Passport",
    },
    {
        "key_label": "ssn",
        "label": "Social Security Number",
    },
    {
        "key_label": "driver_license_number",
        "label": "Driver License",
    },
    {
        "key_label": "uuid",
        "label": "UUID",
    },
    {
        "key_label": "ulid",
        "label": "ULID",
    },
    {
        "key_label": "isbn",
        "label": "ISBN",
    },
    {
        "key_label": "mongodb_object_id",
        "label": "MongoDB ID",
    },
]

IkiDataGenerator(schema).many(150).export("documents", formats=["csv", "json"])

print("[OK] Generated 150 identity documents!")
