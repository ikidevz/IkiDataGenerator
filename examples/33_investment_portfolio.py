"""
33_investment_portfolio.py - Stock & Investment Data

Stock holdings, portfolio performance, and investment data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "stock_name",
        "label": "Company",
    },
    {
        "key_label": "stock_symbol",
        "label": "Symbol",
    },
    {
        "key_label": "number",
        "label": "Shares",
        "options": {"min": 1, "max": 1000}
    },
    {
        "key_label": "money",
        "label": "Purchase Price",
    },
    {
        "key_label": "money",
        "label": "Current Price",
    },
    {
        "key_label": "number",
        "label": "Gain/Loss %",
        "options": {"min": -50, "max": 150}
    },
    {
        "key_label": "current_timestamp",
        "label": "Purchase Date",
    },
    {
        "key_label": "stock_market",
        "label": "Market",
    },
]

IkiDataGenerator(schema).many(500).export(
    "investments", formats=["csv", "json"])

print("[OK] Generated 500 investment portfolios!")
