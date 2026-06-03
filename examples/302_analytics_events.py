"""
302_analytics_events.py - Event Tracking & Analytics Data

Web/mobile analytics events for user behavior tracking.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "username",
    {
        "key_label": "current_timestamp",
        "label": "Event Time",
    },
    {
        "key_label": "custom_list",
        "label": "Event Type",
        "options": {"values": ["Page View", "Click", "Scroll", "Form Submit", "Purchase", "Sign Up", "Login", "Log Out"]}
    },
    {
        "key_label": "url",
        "label": "Page URL",
    },
    {
        "key_label": "words",
        "label": "Event Name",
    },
    {
        "key_label": "custom_list",
        "label": "Device Type",
        "options": {"values": ["Desktop", "Mobile", "Tablet"]}
    },
    {
        "key_label": "custom_list",
        "label": "Browser",
        "options": {"values": ["Chrome", "Firefox", "Safari", "Edge", "Mobile"]}
    },
    {
        "key_label": "country",
        "label": "Country",
    },
    {
        "key_label": "city",
        "label": "City",
    },
    {
        "key_label": "number",
        "label": "Session Duration (seconds)",
        "options": {"min": 1, "max": 3600}
    },
]

IkiDataGenerator(schema).many(5000).export(
    "analytics_events", formats=["json", "parquet"])

print("[OK] Generated 5000 analytics events!")
