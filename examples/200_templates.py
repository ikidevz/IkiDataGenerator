"""
200_templates.py - Using Templates to Combine Fields

Templates let you combine fields with {{field_name}} syntax.
This creates computed or combined fields from other generated data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    "email_address",
    "city",
    "state",
    {
        "key_label": "template",
        "label": "Full Name",
        "options": {
            "template": "{{first_name}} {{last_name}}"
        }
    },
    {
        "key_label": "template",
        "label": "Email With Name",
        "options": {
            "template": "{{first_name}}.{{last_name}}@example.com"
        }
    },
    {
        "key_label": "template",
        "label": "Full Address",
        "options": {
            "template": "{{city}}, {{state}}"
        }
    },
    {
        "key_label": "template",
        "label": "Contact Card",
        "options": {
            "template": "Contact: {{first_name}} {{last_name}} | Email: {{email_address}}"
        }
    },
]

IkiDataGenerator(schema).many(200).export(
    "templates_example", formats=["csv", "json"])

print("[OK] Generated 200 records with templates!")
print("   Check how fields are combined in the output!")
