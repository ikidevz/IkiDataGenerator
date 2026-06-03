"""
401_batch_processing.py - Batch Processing Multiple Datasets

Generate multiple independent datasets in one script.
Great for testing pipelines that process multiple data sources.
"""

from ikidatagen import IkiDataGenerator

print("🔄 Generating multiple datasets in batch...")

# Dataset 1: Users
print("[OK] Generating 500 users...")
user_schema = ["row_number", "first_name",
               "last_name", "email_address", "country"]
IkiDataGenerator(user_schema).many(500).export("batch_users", formats=["csv"])

# Dataset 2: Products
print("[OK] Generating 1000 products...")
product_schema = [
    "row_number",
    "product_name",
    "product_category",
    "product_price",
    "sku",
]
IkiDataGenerator(product_schema).many(
    1000).export("batch_products", formats=["csv"])

# Dataset 3: Orders
print("[OK] Generating 2000 orders...")
order_schema = [
    "row_number",
    "current_timestamp",
    "first_name",
    "last_name",
    "product_name",
    "product_price",
    {
        "key_label": "number",
        "label": "Quantity",
        "options": {"min": 1, "max": 10}
    },
]
IkiDataGenerator(order_schema).many(
    2000).export("batch_orders", formats=["csv"])

# Dataset 4: Transactions
print("[OK] Generating 3000 transactions...")
transaction_schema = [
    "row_number",
    "current_timestamp",
    "username",
    "money",
    "currency",
    {
        "key_label": "custom_list",
        "label": "Type",
        "options": {"values": ["Transfer", "Deposit", "Withdrawal"]}
    },
]
IkiDataGenerator(transaction_schema).many(
    3000).export("batch_transactions", formats=["csv"])

print("\n[OK] All datasets generated successfully!")
print("   [FOLDER] Check output/ folder for batch_*.csv files")
