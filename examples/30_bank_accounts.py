"""
30_bank_accounts.py - Banking & Accounts

Bank account data with account types, balances, and holders.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    "email_address",
    {
        "key_label": "current_timestamp",
        "label": "Account Created",
    },
    {
        "key_label": "account_type",
        "label": "Account Type",
    },
    {
        "key_label": "money",
        "label": "Balance",
    },
    {
        "key_label": "currency",
        "label": "Currency",
    },
    {
        "key_label": "iban",
        "label": "IBAN",
    },
    {
        "key_label": "bban",
        "label": "BBAN",
    },
    {
        "key_label": "boolean",
        "label": "Active",
    },
]

IkiDataGenerator(schema).many(200).export(
    "bank_accounts", formats=["csv", "json"])

print("[OK] Generated 200 bank accounts!")
