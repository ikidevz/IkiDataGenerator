"""
51_international_locations.py - Countries & Cities Worldwide

International location data with countries, regions, and coordinates.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "country",
    {
        "key_label": "state",
        "label": "Region/Province",
    },
    {
        "key_label": "city",
        "label": "City",
    },
    {
        "key_label": "postal_code",
        "label": "Postal Code",
    },
    {
        "key_label": "latitude",
        "label": "Latitude",
    },
    {
        "key_label": "longitude",
        "label": "Longitude",
    },
    {
        "key_label": "timezone",
        "label": "Timezone",
    },
    {
        "key_label": "language",
        "label": "Primary Language",
    },
    {
        "key_label": "currency",
        "label": "Currency",
    },
]

IkiDataGenerator(schema).many(500).export("locations", formats=["csv", "json"])

print("[OK] Generated 500 international locations!")
