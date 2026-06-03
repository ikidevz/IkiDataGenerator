"""
40_patient_records.py - Patient Demographics & Records

Patient information, medical history, and healthcare data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "datetime",
        "label": "DOB",
    },
    "gender_binary",
    {
        "key_label": "blood_type",
        "label": "Blood Type",
    },
    "phone",
    "email_address",
    {
        "key_label": "street_address",
        "label": "Address",
    },
    {
        "key_label": "current_timestamp",
        "label": "Last Visit",
    },
    {
        "key_label": "vaccination_status",
        "label": "Vaccination Status",
    },
    {
        "key_label": "insurance_provider",
        "label": "Insurance",
    },
]

IkiDataGenerator(schema).many(300).export("patients", formats=["csv", "json"])

print("[OK] Generated 300 patient records!")
