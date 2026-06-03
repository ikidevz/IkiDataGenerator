"""
60_student_records.py - Student & Enrollment Data

Student information, enrollment status, and academic records.
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
    "email_address",
    "phone",
    {
        "key_label": "university",
        "label": "University",
    },
    {
        "key_label": "degree",
        "label": "Degree Type",
    },
    {
        "key_label": "academic_subject",
        "label": "Major",
    },
    {
        "key_label": "current_timestamp",
        "label": "Enrollment Date",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Active", "Graduated", "On Leave", "Dropped"]}
    },
]

IkiDataGenerator(schema).many(400).export("students", formats=["csv", "json"])

print("[OK] Generated 400 student records!")
