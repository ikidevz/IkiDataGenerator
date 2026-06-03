"""
20_ecommerce_shop.py - E-Commerce Store Data

Complete e-commerce dataset with products, prices, and inventory.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "product_name",
        "label": "Product",
    },
    {
        "key_label": "product_category",
        "label": "Category",
    },
    {
        "key_label": "product_subcategory",
        "label": "Subcategory",
    },
    {
        "key_label": "product_price",
        "label": "Price",
    },
    {
        "key_label": "sku",
        "label": "SKU",
    },
    {
        "key_label": "barcode_ean13",
        "label": "Barcode",
    },
    {
        "key_label": "inventory_status",
        "label": "Stock Status",
    },
    {
        "key_label": "currency",
        "label": "Currency",
    },
]

IkiDataGenerator(schema).many(500).export(
    "ecommerce_products", formats=["csv", "json", "parquet"])

print("[OK] Generated 500 e-commerce products!")
