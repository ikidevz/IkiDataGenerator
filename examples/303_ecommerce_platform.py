"""
303_ecommerce_platform.py - Complete E-Commerce Platform Data

Full e-commerce system with customers, products, orders, and reviews.
"""

from ikidatagen import IkiDataGenerator

# Customer base
customer_schema = [
    "row_number",
    "first_name",
    "last_name",
    "email_address",
    "phone",
    "street_address",
    "city",
    "state",
    "postal_code",
    {
        "key_label": "current_timestamp",
        "label": "Customer Since",
    },
    {
        "key_label": "custom_list",
        "label": "Loyalty Tier",
        "options": {"values": ["Bronze", "Silver", "Gold", "Platinum"]}
    },
]

# Orders
order_schema = [
    "row_number",
    {
        "key_label": "current_timestamp",
        "label": "Order Date",
    },
    "first_name",
    "last_name",
    {
        "key_label": "product_name",
        "label": "Product",
    },
    {
        "key_label": "product_price",
        "label": "Unit Price",
    },
    {
        "key_label": "number",
        "label": "Quantity",
        "options": {"min": 1, "max": 20}
    },
    {
        "key_label": "discount_percentage",
        "label": "Discount %",
        "options": {"blank_percentage": 70}
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Pending", "Processing", "Shipped", "Delivered", "Returned"]}
    },
    {
        "key_label": "payment_method",
        "label": "Payment Method",
    },
]

# Reviews
review_schema = [
    "row_number",
    {
        "key_label": "product_name",
        "label": "Product",
    },
    "username",
    {
        "key_label": "number",
        "label": "Rating",
        "options": {"min": 1, "max": 5}
    },
    {
        "key_label": "words",
        "label": "Review Title",
    },
    {
        "key_label": "paragraphs",
        "label": "Review Text",
    },
    {
        "key_label": "number",
        "label": "Helpful Votes",
        "options": {"min": 0, "max": 1000}
    },
    {
        "key_label": "current_timestamp",
        "label": "Review Date",
    },
]

print("Generating E-Commerce Platform Data...")
print("   [OK] Generating 500 customers...")
IkiDataGenerator(customer_schema).many(500).export(
    "ecommerce_customers", formats=["csv"])

print("   [OK] Generating 2000 orders...")
IkiDataGenerator(order_schema).many(2000).export(
    "ecommerce_orders", formats=["csv", "parquet"])

print("   [OK] Generating 1000 reviews...")
IkiDataGenerator(review_schema).many(1000).export(
    "ecommerce_reviews", formats=["csv", "json"])

print("[OK] Complete E-Commerce platform data generated!")
