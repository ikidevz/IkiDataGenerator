"""
203_blank_percentages.py - Handling Missing Data & Blanks

Use blank_percentage to simulate real-world data with missing values.
This is useful for testing data cleaning and validation logic.
"""

from ikidatagen import IkiDataGenerator

schema = [
    {
        "key_label": "row_number",
        "label": "ID",
        "options": {"blank_percentage": 0}  # No blanks for ID
    },
    "first_name",
    "last_name",
    {
        "key_label": "email_address",
        "label": "Email",
        "options": {"blank_percentage": 0}  # No blanks for email
    },
    {
        "key_label": "phone",
        "label": "Phone",
        "options": {"blank_percentage": 30}  # 30% missing phones
    },
    {
        "key_label": "street_address",
        "label": "Address",
        "options": {"blank_percentage": 20}  # 20% missing addresses
    },
    {
        "key_label": "datetime",
        "label": "DOB",
        "options": {"blank_percentage": 15}  # 15% missing DOBs
    },
    {
        "key_label": "company_name",
        "label": "Company",
        "options": {"blank_percentage": 40}  # 40% missing companies
    },
    {
        "key_label": "url",
        "label": "Website",
        "options": {"blank_percentage": 60}  # 60% missing websites
    },
]

IkiDataGenerator(schema).many(500).export(
    "missing_data", formats=["csv", "json"])

print("[OK] Generated 500 records with realistic missing data!")
print("   Perfect for testing data cleaning pipelines!")
