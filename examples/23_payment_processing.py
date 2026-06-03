"""
23_payment_processing.py - Payment & Transaction Data

Credit cards, invoices, payment records, and receipts.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "invoice_number",
        "label": "Invoice",
    },
    "first_name",
    "last_name",
    "email_address",
    {
        "key_label": "credit_card_number",
        "label": "Card Number",
    },
    {
        "key_label": "credit_card_type",
        "label": "Card Type",
    },
    {
        "key_label": "money",
        "label": "Amount",
    },
    {
        "key_label": "currency",
        "label": "Currency",
    },
    {
        "key_label": "payment_method",
        "label": "Method",
    },
    {
        "key_label": "payment_status",
        "label": "Status",
    },
    {
        "key_label": "current_timestamp",
        "label": "Transaction Date",
    },
]

IkiDataGenerator(schema).many(500).export("payments", formats=["csv", "json"])

print("[OK] Generated 500 payment records!")
