"""
400_mixed_categories.py - Combining Multiple Data Categories

This example demonstrates mixing fields from 5+ categories in one schema.
Great for complex real-world datasets with diverse attributes.
"""

from ikidatagen import IkiDataGenerator

print("🎨 Generating dataset with mixed categories...")

schema = [
    # Basic identifiers
    "row_number",
    "first_name",
    "last_name",
    "username",

    # Personal data
    "email_address",
    "phone",
    {
        "key_label": "date_of_birth",
        "label": "DOB",
    },

    # Location data
    "country",
    "city",
    {
        "key_label": "street_address",
        "label": "Address",
    },

    # Finance data
    {
        "key_label": "money",
        "label": "Account Balance",
    },
    {
        "key_label": "currency",
        "label": "Currency",
    },

    # Commerce data
    {
        "key_label": "product_name",
        "label": "Favorite Product",
    },
    {
        "key_label": "custom_list",
        "label": "Loyalty Tier",
        "options": {"values": ["Bronze", "Silver", "Gold", "Platinum"]}
    },

    # Education data
    {
        "key_label": "degree",
        "label": "Education Level",
    },
    {
        "key_label": "academic_subject",
        "label": "Field of Study",
    },

    # Tech data
    {
        "key_label": "programming_language",
        "label": "Favorite Language",
    },

    # Healthcare (minimal)
    {
        "key_label": "blood_type",
        "label": "Blood Type",
    },

    # Timestamps & misc
    {
        "key_label": "current_timestamp",
        "label": "Join Date",
    },
    {
        "key_label": "boolean",
        "label": "Verified",
    },
    {
        "key_label": "sentiment",
        "label": "Last Review Sentiment",
    },

    # Templates combining multiple fields
    {
        "key_label": "template",
        "label": "Full Profile",
        "options": {
            "template": "{{first_name}} {{last_name}} ({{username}}) - {{city}}, {{country}}"
        }
    },
]

IkiDataGenerator(schema).many(500).export(
    "mixed_dataset", formats=["csv", "json", "parquet"])

print("\n[OK] Generated mixed category dataset!")
print("   Includes: Personal, Finance, Location, Commerce, Education, Tech, Healthcare")
print("   Perfect for real-world scenarios with diverse attributes!")
