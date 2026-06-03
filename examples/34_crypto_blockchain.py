"""
34_crypto_blockchain.py - Cryptocurrency & Blockchain Data

Crypto wallets, transactions, and blockchain data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "username",
    {
        "key_label": "cryptocurrency_symbol",
        "label": "Cryptocurrency",
    },
    {
        "key_label": "cryptocurrency_name",
        "label": "Cryptocurrency Name",
    },
    {
        "key_label": "cryptocurrency_address",
        "label": "Wallet Address",
    },
    {
        "key_label": "number",
        "label": "Holdings",
        "options": {"min": 0.0001, "max": 100}
    },
    {
        "key_label": "money",
        "label": "Value (USD)",
    },
    {
        "key_label": "current_timestamp",
        "label": "Purchase Date",
    },
    {
        "key_label": "uuid_v4",
        "label": "Last TX ID",
    },
    {
        "key_label": "custom_list",
        "label": "Wallet Type",
        "options": {"values": ["Cold", "Hot", "Exchange", "Hardware"]}
    },
]

IkiDataGenerator(schema).many(400).export(
    "crypto_wallets", formats=["csv", "json"])

print("[OK] Generated 400 crypto wallet records!")
