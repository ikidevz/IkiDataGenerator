"""
21_shopping_cart.py - Shopping & Order History

Complete shopping transactions with customers, items, and order details.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "current_timestamp",
        "label": "Order Date",
    },
    "first_name",
    "last_name",
    "email_address",
    {
        "key_label": "product_name",
        "label": "Item Purchased",
    },
    {
        "key_label": "product_price",
        "label": "Unit Price",
    },
    {
        "key_label": "number",
        "label": "Quantity",
        "options": {"min": 1, "max": 10}
    },
    {
        "key_label": "discount_percentage",
        "label": "Discount %",
    },
    {
        "key_label": "order_status",
        "label": "Status",
    },
    {
        "key_label": "payment_method",
        "label": "Payment Method",
    },
]

IkiDataGenerator(schema).many(1000).export(
    "shopping_orders", formats=["csv", "json"])

print("[OK] Generated 1000 shopping orders!")
