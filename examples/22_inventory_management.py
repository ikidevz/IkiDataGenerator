"""
22_inventory_management.py - Inventory & Stock Management

Warehouse inventory, stock levels, and supply chain data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "product_name",
        "label": "Product",
    },
    {
        "key_label": "sku",
        "label": "SKU",
    },
    {
        "key_label": "barcode_ean13",
        "label": "EAN13",
    },
    {
        "key_label": "barcode_upc",
        "label": "UPC",
    },
    {
        "key_label": "number",
        "label": "Stock Level",
        "options": {"min": 0, "max": 1000}
    },
    {
        "key_label": "number",
        "label": "Reorder Point",
        "options": {"min": 10, "max": 100}
    },
    {
        "key_label": "warehouse_location",
        "label": "Location",
    },
    {
        "key_label": "inventory_status",
        "label": "Status",
    },
    {
        "key_label": "current_timestamp",
        "label": "Last Updated",
    },
]

IkiDataGenerator(schema).many(300).export("inventory", formats=["csv", "json"])

print("[OK] Generated 300 inventory items!")
