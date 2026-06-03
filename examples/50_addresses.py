"""
50_addresses.py - Address Data

Street addresses, postal codes, coordinates, and locations.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "street_address",
        "label": "Street Address",
    },
    {
        "key_label": "address_line_2",
        "label": "Apt/Suite",
        "options": {"blank_percentage": 50}
    },
    {
        "key_label": "city",
        "label": "City",
    },
    {
        "key_label": "state",
        "label": "State",
    },
    {
        "key_label": "postal_code",
        "label": "ZIP Code",
    },
    "country",
    {
        "key_label": "latitude",
        "label": "Latitude",
    },
    {
        "key_label": "longitude",
        "label": "Longitude",
    },
    {
        "key_label": "time_zone",
        "label": "Timezone",
    },
]

IkiDataGenerator(schema).many(500).export("addresses", formats=["csv", "json"])

print("[OK] Generated 500 addresses!")
