"""
34_crypto_blockchain.py - Cryptocurrency & Blockchain Data

Crypto wallets, transactions, and blockchain data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "username",
    {
        "key_label": "crypto_currency",
        "label": "Cryptocurrency",
    },
    {
        "key_label": "crypto_address",
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
        "key_label": "crypto_transaction_id",
        "label": "Last TX ID",
    },
    {
        "key_label": "blockchain_type",
        "label": "Blockchain",
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
