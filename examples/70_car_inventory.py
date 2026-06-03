"""
70_car_inventory.py - Vehicle Inventory

Cars, models, makes, years, and pricing data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "car_make",
        "label": "Make",
    },
    {
        "key_label": "car_model",
        "label": "Model",
    },
    {
        "key_label": "car_model_year",
        "label": "Year",
    },
    {
        "key_label": "vehicle_type",
        "label": "Type",
    },
    {
        "key_label": "engine_type",
        "label": "Engine",
    },
    {
        "key_label": "fuel_type",
        "label": "Fuel Type",
    },
    {
        "key_label": "transmission_type",
        "label": "Transmission",
    },
    {
        "key_label": "color",
        "label": "Color",
    },
    {
        "key_label": "money",
        "label": "Price",
    },
    {
        "key_label": "car_vin",
        "label": "VIN",
    },
]

IkiDataGenerator(schema).many(600).export(
    "vehicles", formats=["csv", "json", "parquet"])

print("[OK] Generated 600 vehicles!")
