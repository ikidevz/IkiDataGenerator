"""
31_credit_cards.py - Credit Card Data

Credit card information, types, and details.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "credit_card_number",
        "label": "Card Number",
    },
    {
        "key_label": "credit_card_type",
        "label": "Card Type",
    },
    {
        "key_label": "current_timestamp",
        "label": "Issued Date",
    },
    {
        "key_label": "current_timestamp",
        "label": "Expiration Date",
    },
    {
        "key_label": "number",
        "label": "CVV",
        "options": {"min": 100, "max": 999}
    },
    {
        "key_label": "money",
        "label": "Credit Limit",
    },
    {
        "key_label": "money",
        "label": "Available Credit",
    },
]

IkiDataGenerator(schema).many(300).export(
    "credit_cards", formats=["csv", "json"])

print("[OK] Generated 300 credit card records!")
