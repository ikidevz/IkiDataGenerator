"""
300_saas_users.py - SaaS Platform Users & Subscriptions

Complete SaaS platform data with users, plans, and usage metrics.
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
        "key_label": "company_name",
        "label": "company",
    },
    {
        "key_label": "custom_list",
        "label": "Subscription Plan",
        "options": {"values": ["Free", "Basic", "Pro", "Enterprise"]}
    },
    {
        "key_label": "money",
        "label": "Monthly Cost",
    },
    {
        "key_label": "current_timestamp",
        "label": "Sign Up Date",
    },
    {
        "key_label": "current_timestamp",
        "label": "Renewal Date",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Active", "Trial", "Cancelled", "Suspended"]}
    },
    {
        "key_label": "number",
        "label": "Team Members",
        "options": {"min": 1, "max": 100}
    },
    {
        "key_label": "number",
        "label": "API Calls/Month",
        "options": {"min": 0, "max": 1000000}
    },
    {
        "key_label": "number",
        "label": "Storage Used (GB)",
        "options": {"min": 0, "max": 1000}
    },
]

IkiDataGenerator(schema).many(1000).export(
    "saas_users", formats=["csv", "json", "parquet"])

print("[OK] Generated 1000 SaaS users with complete subscription data!")
