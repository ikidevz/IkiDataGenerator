"""
500_test_data_unit_tests.py - Test Data for Unit Tests

Generate test fixtures for pytest, unittest, and other testing frameworks.
"""

from ikidatagen import IkiDataGenerator
import json

# Example 1: User Fixtures for Authentication Tests
print("🧪 Generating test data fixtures...")

user_fixture_schema = [
    {
        "key_label": "row_number",
        "label": "id",
        "options": {"blank_percentage": 0}
    },
    "username",
    {
        "key_label": "email_address",
        "label": "email",
    },
    {
        "key_label": "password",
        "label": "password_hash",
    },
    {
        "key_label": "boolean",
        "label": "is_active",
    },
]

# Example 2: Product Fixtures for E-Commerce Tests
product_fixture_schema = [
    {
        "key_label": "row_number",
        "label": "id",
    },
    "product_name",
    {
        "key_label": "product_price",
        "label": "price",
    },
    {
        "key_label": "number",
        "label": "stock",
        "options": {"min": 0, "max": 1000}
    },
]

# Example 3: Order Fixtures for Order Processing Tests
order_fixture_schema = [
    {
        "key_label": "row_number",
        "label": "id",
    },
    "username",
    {
        "key_label": "current_timestamp",
        "label": "created_at",
    },
    {
        "key_label": "money",
        "label": "total_amount",
    },
    {
        "key_label": "custom_list",
        "label": "status",
        "options": {"values": ["pending", "confirmed", "shipped", "delivered"]}
    },
]

# Generate test fixtures
print("[OK] Generating user fixtures (50 records)...")
IkiDataGenerator(user_fixture_schema).many(
    50).export("test_users", formats=["json"])

print("[OK] Generating product fixtures (100 records)...")
IkiDataGenerator(product_fixture_schema).many(
    100).export("test_products", formats=["json"])

print("[OK] Generating order fixtures (200 records)...")
IkiDataGenerator(order_fixture_schema).many(
    200).export("test_orders", formats=["json"])

print("\n[OK] Test fixtures generated!")
print("   [FOLDER] Use these in your pytest or unittest tests")
print("   💡 Tip: Load from JSON and use as test data in conftest.py")
