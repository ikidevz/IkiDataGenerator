"""
504_api_response_mocking.py - Mock API Responses

Generate fake API responses for testing without hitting real APIs.
Perfect for Postman, Jest, or other API testing tools.
"""

from ikidatagen import IkiDataGenerator
import json

print("🔌 Generating mock API response data...")

# User API Response
user_api_schema = [
    {
        "key_label": "row_number",
        "label": "id",
    },
    "username",
    "email_address",
    "first_name",
    "last_name",
    {
        "key_label": "current_timestamp",
        "label": "created_at",
    },
]

# Product API Response
product_api_schema = [
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
        "key_label": "product_category",
        "label": "category",
    },
    "sku",
    {
        "key_label": "number",
        "label": "stock",
        "options": {"min": 0, "max": 1000}
    },
]

# Order API Response
order_api_schema = [
    {
        "key_label": "row_number",
        "label": "order_id",
    },
    {
        "key_label": "current_timestamp",
        "label": "order_date",
    },
    "username",
    {
        "key_label": "money",
        "label": "total",
    },
    {
        "key_label": "custom_list",
        "label": "status",
        "options": {"values": ["pending", "processing", "shipped", "delivered"]}
    },
]

# Error Response (if needed)
error_schema = [
    {
        "key_label": "row_number",
        "label": "error_code",
    },
    {
        "key_label": "words",
        "label": "message",
    },
    {
        "key_label": "words",
        "label": "details",
    },
]

print("[OK] Generating user API responses...")
IkiDataGenerator(user_api_schema).many(
    100).export("api_users", formats=["json"])

print("[OK] Generating product API responses...")
IkiDataGenerator(product_api_schema).many(
    200).export("api_products", formats=["json"])

print("[OK] Generating order API responses...")
IkiDataGenerator(order_api_schema).many(
    150).export("api_orders", formats=["json"])

print("[OK] Generating error responses...")
IkiDataGenerator(error_schema).many(50).export("api_errors", formats=["json"])

print("\n[OK] Mock API responses generated!")
print("   💡 Use these in Postman or your API testing suite")
print("   💡 Perfect for frontend development without backend!")
