"""
201_regex_patterns.py - Using Regular Expressions for Custom Patterns

Use regex patterns to generate data matching specific formats.
This is great for codes, IDs, and format validation testing.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "regular_expression",
        "label": "Order ID",
        "options": {
            "format": "ORD-[A-Z]{3}-[0-9]{6}"
        }
    },
    {
        "key_label": "regular_expression",
        "label": "Serial Number",
        "options": {
            "format": "SN[0-9]{10}"
        }
    },
    {
        "key_label": "regular_expression",
        "label": "Tracking Code",
        "options": {
            "format": "[A-Z]{2}[0-9]{4}[A-Z]{2}"
        }
    },
    {
        "key_label": "regular_expression",
        "label": "Product Code",
        "options": {
            "format": "P-[0-9]{3}-[A-Z]{4}-[0-9]{2}"
        }
    },
    {
        "key_label": "regular_expression",
        "label": "Reference",
        "options": {
            "format": "REF[0-9]{8}"
        }
    },
]

IkiDataGenerator(schema).many(300).export(
    "regex_patterns", formats=["csv", "json"])

print("[OK] Generated 300 records with regex patterns!")
print("   Check how patterns are applied to different formats!")
