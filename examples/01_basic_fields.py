"""
01_basic_fields.py - Common Basic Fields

Explore the most commonly used fields from the Basic category.
Great for test data and general-purpose datasets.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "email_address",
        "label": "Email",
    },
    {
        "key_label": "password",
        "label": "Password",
    },
    {
        "key_label": "boolean",
        "label": "Is Active",
    },
    {
        "key_label": "datetime",
        "label": "DOB",
    },
    {
        "key_label": "color",
        "label": "Favorite Color",
    },
    {
        "key_label": "emoji",
        "label": "Mood",
    },
    {
        "key_label": "sentiment",
        "label": "Review Sentiment",
    },
    {
        "key_label": "number",
        "label": "Random Number",
        "options": {"min": 1, "max": 100}
    },
    {
        "key_label": "words",
        "label": "Description",
    },
]

IkiDataGenerator(schema).many(50).export(
    "basic_fields", formats=["csv", "json"])

print("[OK] Generated 50 records with basic fields!")
