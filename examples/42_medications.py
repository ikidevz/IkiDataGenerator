"""
42_medications.py - Medication & Prescriptions

Prescription data, medications, dosages, and side effects.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "medication_name",
        "label": "Medication",
    },
    {
        "key_label": "custom_list",
        "label": "Dosage",
        "options": {"values": ["100mg", "250mg", "500mg", "1000mg"]}
    },
    {
        "key_label": "custom_list",
        "label": "Frequency",
        "options": {"values": ["Once daily", "Twice daily", "Three times daily", "As needed"]}
    },
    {
        "key_label": "current_timestamp",
        "label": "Prescribed Date",
    },
    {
        "key_label": "current_timestamp",
        "label": "Expiration Date",
    },
    {
        "key_label": "words",
        "label": "Side Effects",
    },
    {
        "key_label": "words",
        "label": "Interactions",
    },
]

IkiDataGenerator(schema).many(350).export(
    "medications", formats=["csv", "json"])

print("[OK] Generated 350 medication records!")
