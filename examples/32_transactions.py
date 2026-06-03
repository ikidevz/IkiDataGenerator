"""
32_transactions.py - Bank Transactions

Bank transfers, deposits, withdrawals, and transaction history.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "current_timestamp",
        "label": "Date",
    },
    "first_name",
    "last_name",
    {
        "key_label": "money",
        "label": "Amount",
    },
    {
        "key_label": "currency",
        "label": "Currency",
    },
    {
        "key_label": "custom_list",
        "label": "Type",
        "options": {"values": ["Transfer", "Deposit", "Withdrawal", "Fee", "Interest"]}
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Completed", "Pending", "Failed"]}
    },
    {
        "key_label": "words",
        "label": "Description",
    },
    {
        "key_label": "money",
        "label": "Balance After",
    },
]

IkiDataGenerator(schema).many(1000).export(
    "transactions", formats=["csv", "json"])

print("[OK] Generated 1000 transactions!")
