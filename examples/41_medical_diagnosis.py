"""
41_medical_diagnosis.py - Medical Diagnoses & Codes

ICD codes, diagnoses, symptoms, and medical classifications.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "disease_name",
        "label": "Diagnosis",
    },
    {
        "key_label": "icd10_diagnosis",
        "label": "ICD-10 Code",
    },
    {
        "key_label": "symptom_name",
        "label": "Primary Symptom",
    },
    {
        "key_label": "current_timestamp",
        "label": "Diagnosis Date",
    },
    {
        "key_label": "custom_list",
        "label": "Severity",
        "options": {"values": ["Mild", "Moderate", "Severe"]}
    },
    {
        "key_label": "medication_name",
        "label": "Prescribed Medication",
    },
    {
        "key_label": "words",
        "label": "Notes",
    },
]

IkiDataGenerator(schema).many(400).export("diagnoses", formats=["csv", "json"])

print("[OK] Generated 400 diagnoses!")
